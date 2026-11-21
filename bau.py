"""Baut LernTool aus inhalte/ und app/ nach dist/.

  python3 bau.py            bauen
  python3 bau.py --test     bauen und alle Tests (tests/*.js) laufen lassen

dist/ enthält alles, was veröffentlicht wird:
  index.html          zum lokalen Öffnen (vollständiges Dokument)
  artifact.html       dieselbe Seite ohne Dokument-Gerüst (für die Veröffentlichung als Artifact)
  app.css, inhalt.css, katex.css, katex.js, laufzeit.js, kern.js, ansichten.js
  daten/index.js      Übersicht aller Fächer (Oberthemen, Unterthemen, Klausuren), sofort geladen
  daten/<fach>.js     Inhalte, Fragen, Glossar und Schaubild-Skripte eines Fachs, erst bei Bedarf geladen
"""
import hashlib, html
import os
import json, pathlib, re, shutil, subprocess, sys

HIER = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HIER / 'werkzeuge'))
from js_teile import stmts

IN, APP, DIST = HIER / 'inhalte', HIER / 'app', HIER / 'dist'
FARBE = {'abwl': '#1f4e8c'}   # ABWL hat im alten System keine eigene Akzentfarbe
JS_DATEIEN = ['kern.js', 'gedaechtnis.js', 'lesen.js', 'pruefung.js', 'klausur.js', 'willkommen.js', 'handy.js', 'ansichten.js', 'sync.js', 'folien.js']


def lies(p):
    return json.loads((IN / p).read_text(encoding='utf-8'))


def txt(s):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s or '')).replace('&amp;', '&').replace('&nbsp;', ' ').strip()


# ---------- Schaubild-Laufzeit aus dem alten Unterbau (nur die Teile, die Schaubilder brauchen) ----------
EINMAL = {  # Anweisungen, die einmal beim Start laufen (Helfer, Fenster für Mini-Schaubilder, Antipp-Tipps)
    'alt_base.js': ['const fmt', 'const eur', 'const $ =', 'function parseNum', 'function bindHot', 'function drawTree',
                    "const FM = ", 'FM.innerHTML', 'document.body.appendChild(FM)', 'let fmSrc', 'function closeFig', 'const tipAn',
                    "document.addEventListener('click', e => { const t = e.target.closest('.tp')",
                    "document.addEventListener('keydown', e => { const t = e.target.closest && e.target.closest('.tp')",
                    "$('.qmclose', FM)", "document.addEventListener('keydown', e => { if (e.key === 'Escape') closeFig"],
    'alt_sb.js': ['const MP', 'const phi', 'const Phi', 'const binom', 'function UM', 'const NEU', 'function LG', 'const ZWS',
                  'function KS', 'const TXS', 'const ARDEFS', 'const ARS', 'function M2S'],
    'alt_end.js': ['function fitSvgs', 'const fold', 'function wideFx'],
}
JE_SEITE = {  # Anweisungen, die nach jedem Seitenwechsel auf den neuen Inhalt angewandt werden
    'alt_base.js': ["$$('.topic.v3')", "$$('.zoom')", "$$('.mfig')", "$$('.deep')", "$$('.q .rev')", "$$('.q .chk')", "$$('.q.mc')", 'bindHot(document)'],
    'alt_sb.js': ["document.querySelectorAll('.sortier')"],
    'alt_end.js': ["$$('.ctrl label')", "$$('.rg input[type=range]')"],
}


def waehle(datei, praefixe):
    teile = stmts((IN / 'basis' / datei).read_text(encoding='utf-8'))
    out = []
    for p in praefixe:
        treffer = [s for s in teile if s.startswith(p)]
        if len(treffer) != 1:
            sys.exit(f'Laufzeit: „{p}“ in {datei} {len(treffer)}× gefunden (erwartet 1)')
        out.append(treffer[0])
    return '\n'.join(out)


def laufzeit():
    einmal = '\n'.join(waehle(d, p) for d, p in EINMAL.items())
    vor = waehle('alt_base.js', JE_SEITE['alt_base.js']) + '\n' + waehle('alt_sb.js', JE_SEITE['alt_sb.js'])
    nach = waehle('alt_end.js', JE_SEITE['alt_end.js'])
    nach = (IN / 'basis' / 'gemeinsam.js').read_text(encoding='utf-8') + '\n' + nach   # Spiele und Tafeln in allen Fächern
    return f'''/* Schaubild-Laufzeit: Helfer und Seiten-Logik aus dem alten Lernportal (automatisch aus inhalte/basis/alt_*.js gewählt). */
{einmal}
window.addEventListener('resize', fitSvgs);
/* Das Fenster für Mini-Schaubilder braucht die Lernseiten-Stile (inhalt.css gilt nur innerhalb von .inhalt) */
(function () {{ const w = document.createElement('div'); w.className = 'inhalt lt-modale'; document.body.appendChild(w); w.appendChild(FM); }})();
window.LT_FIG = window.LT_FIG || {{}};
window.LT_nachRender = function (fach) {{
  NEU.length = 0;
{vor}
  try {{ if (LT_FIG[fach]) LT_FIG[fach](); }} catch (e) {{ console.error('Schaubild', fach, e); }}
{nach}
  try {{
    if (window.renderMathInElement) renderMathInElement(document.querySelector('.inhalt') || document.body, {{
      delimiters: [{{ left: '\\\\[', right: '\\\\]', display: true }}, {{ left: '\\\\(', right: '\\\\)', display: false }}],
      throwOnError: false, trust: c => c.command === '\\\\htmlClass', strict: c => c === 'htmlExtension' ? 'ignore' : 'warn' }});
  }} catch (e) {{ console.error('KaTeX', e); }}
  fitSvgs(); wideFx();
}};
'''


# ---------- Lernseiten-CSS auf .inhalt begrenzen ----------
def bloecke(css):
    i, n, out = 0, len(css), []
    while i < n:
        j = css.find('{', i)
        if j < 0:
            break
        d, k = 1, j + 1
        while d and k < n:
            d += {'{': 1, '}': -1}.get(css[k], 0); k += 1
        out.append((css[i:j].strip(), css[j + 1:k - 1])); i = k
    return out


def scope_sel(s):
    s = s.strip()
    if re.match(r'^(:root|html|body)', s):
        if 'data-theme' in s and 'dark' in s:
            return None
        return re.sub(r'^(:root(:not\([^)]*\))?|html|body(\.\w+)?)', '.inhalt', s)
    return '.inhalt ' + s


def scope(css):
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    out = []
    for sel, body in bloecke(css):
        if sel.startswith('@media'):
            if 'prefers-color-scheme' in sel or 'print' in sel:
                continue
            out.append(f'{sel}{{{scope(body)}}}')
        elif sel.startswith('@'):
            out.append(f'{sel}{{{body}}}')
        else:
            sels = [x for x in (scope_sel(p) for p in sel.split(',')) if x]
            if sels:
                out.append(f'{",".join(sels)}{{{body}}}')
    return '\n'.join(out)


DEF_FRAGE = re.compile(r'(definier|was (ist|sind|versteht man unter|bedeutet|beschreibt)|wie (ist|wird|lautet) .{0,40}defini|was heißt)', re.I)


def definitionen_fragen(fid, fr):
    """Eine Definition je Begriff (Wunsch des Nutzers, 13.11.2026):
    - Jede Familie, die eine Folien-Definition abfragt, bekommt den Begriffs-Schlüssel b. Die App zieht je Sitzung höchstens eine Familie je b
      (Übungsklausur, Refresh, Mini-Quiz, Endlos-Quiz, Nacharbeiten): nie zwei Fragen zur selben Definition.
    - Die Definitionsfrage (df-) zeigt unter der Lösung „Auch richtig (sinngemäß)“: die einfache Fassung, die vorher auf der Lernseite stand
      (werkzeuge/definitionen/einfach.py). Bewertet wird nach den Kernpunkten, nicht wortgenau.
    - Nachschärf-Karten für „Nacharbeiten“: bekannte Fassung → Folien-Definition, Kernpunkte gold (nur für Lernende, die das Unterthema schon kannten).
    Rückgabe: (defs je df-Familie für daten/<fach>.js, nachDef für den Index)"""
    if not (IN / fid / 'definitionen.json').exists(): return {}, []
    sys.path.insert(0, str(HIER / 'werkzeuge' / 'definitionen'))
    from einfach import EINFACH
    einf = EINFACH.get(fid, {})
    slug = lambda b: re.sub(r'[^a-z0-9]+', '-', b.lower().replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')).strip('-')[:30]
    nach, nutz = [], {}
    nach_thema = {}
    for q in fr: nach_thema.setdefault(q['t'], []).append(q)
    for D_ in lies(f'{fid}/definitionen.json')['definitionen']:
        b, t = D_['begriff'], D_['t']
        df = f"{fid}:{t}:df-{slug(b)}"
        fam = next((q for q in nach_thema.get(t, []) if q.get('id') == df), None)
        if not fam: continue
        assert b in einf, f'{fid}: „Einfach gesagt“ fehlt für {b} (werkzeuge/definitionen/einfach.py)'
        fam['b'] = b
        for v in fam['a']:
            if v['y'] == 'rev': v['auch'] = einf[b]
        wort = html.escape(D_['wortlaut'], quote=False)
        for k in sorted(D_['kern'], key=len, reverse=True): wort = wort.replace(html.escape(k, quote=False), f'<b class="def-k">{html.escape(k, quote=False)}</b>', 1)
        nutz[df] = dict(b=b, w=wort, e=einf[b])
        nach.append([df, 0, 'def', t])
        # andere Familien, die dieselbe Definition abfragen: gleicher Schlüssel (nie zusammen mit der Definitionsfrage in einer Sitzung)
        kurz = re.escape(b.split(' (')[0])
        for q in nach_thema.get(t, []):
            if q is fam or q.get('b'): continue
            treffer = [bool(DEF_FRAGE.search(txt(v.get('p', ''))) and re.search(r'\b' + kurz, txt(v.get('p', '')), re.I)) for v in q['a']]
            if not any(treffer): continue
            if treffer[0] or sum(treffer) * 2 >= len(treffer): q['b'] = b   # die Familie fragt die Definition ab
            else:   # nur einzelne Varianten fragen die Definition: diese Varianten kennzeichnen (Übungsklausur nimmt dann eine andere)
                for v, tr in zip(q['a'], treffer):
                    if tr: v['bv'] = b
    return nutz, nach


def definitionen_gold(fach, defs):
    """Kernpunkte jeder Folien-Definition (inhalte/<fach>/definitionen.json) im Lerntext gold markieren (<span class="fo-wl">):
    jeweils die erste Stelle, an der der Wortlaut ohne Tags dazwischen im Text steht (nie in einem Tag, nie doppelt)."""
    T = {t['id']: t for k in fach['kapitel'] for t in k['themen']}
    for D_ in defs:
        t = T.get(D_['t'])
        if not t: continue
        h = t.get('article', '')
        for kern in sorted(D_.get('kern', []), key=len, reverse=True):
            k = html.escape(kern, quote=False)
            if any(k in z for z in re.findall(r'<!--nz-->(.*?)<!--/nz-->', h, flags=re.S)): continue   # steht schon im goldenen Folienstoff
            for m in re.finditer(re.escape(k), h):
                vor = h[:m.start()]
                if vor.rfind('<') > vor.rfind('>') or vor.endswith('<span class="fo-wl">'): continue   # in einem Tag oder schon markiert
                if re.search(r'<span class="fo-wl">[^<]*$', vor): continue
                h = vor + '<span class="fo-wl">' + h[m.start():m.end()] + '</span>' + h[m.end():]
                break
        # Kennzeichnung „Definition (Folie)“: das goldene Element, in dem der erste Kernpunkt steht (einmal je Begriff)
        k0 = html.escape(D_['kern'][0], quote=False) if D_.get('kern') else ''
        pos = h.find(k0) if k0 else -1
        while pos >= 0:
            vor = h[:pos]; a_ = vor.rfind('data-nz="')
            if a_ >= 0 and vor.rfind('<!--/nz-->') < a_ and vor.rfind('<!--nz-->') < a_ and 'data-def=' not in h[a_:a_ + 80]:
                e_ = h.index('"', a_ + 9) + 1; z_ = h.index('>', e_) + 1
                anfang = re.sub(r'^\s*(Genau gesagt|Genauer|Genau|Definition|In der Fassung der Vorlesung)\s*:\s*', '', txt(h[z_:z_ + 600]))
                w1 = re.sub(r'\W.*', '', D_['begriff'].split(' (')[0].replace('-', '')).lower(); wort1 = w1[:max(5, len(w1) - 2)]
                # nur ganze Definitionssätze, die den Begriff selbst nennen (keine Satzbruchstücke, nicht der Nachbarbegriff)
                if re.match(r'[A-ZÄÖÜ]', anfang) and wort1 and wort1 in anfang[:70].lower().replace('-', ''):
                    h = h[:e_] + f' data-def="{html.escape(D_["begriff"])}"' + h[e_:z_] + re.sub(r'^(\s*)(Genau gesagt|Genauer|Genau|Definition|In der Fassung der Vorlesung)\s*:\s*', r'\1', h[z_:], count=1)
                break
            pos = h.find(k0, pos + 1)
        t['article'] = h


# ---------- Themen-Körper wie im alten Lernportal (base.topic_v3, ohne Kopfzeile, Üben- und Gelernt-Knöpfe) ----------
def figur(inner, cap=''):
    c = f'<div class="fig-cap"><span>{cap}</span></div>' if cap else ''
    m = re.match(r'\s*(<p class="fig-what">.*?</p>)', inner, re.S)
    what, inner = (m.group(1), inner[m.end():]) if m else ('', inner)
    return f'<div class="figure"><div class="fig-top">{what}<button class="zoom" type="button">⤢ Vergrößern</button></div>{inner}{c}</div>'


def koerper(fid, d, ziel, zurueck):
    out = []
    if d.get('aus'):   # ausgegrautes Unterthema: Hinweis oben, kein Merksatz
        out.append('<div class="box aus-hinweis"><b>Kommt nicht dran.</b> Dieses Unterthema ist für die Klausur nicht nötig (in den Folien gestrichen). '
                   'Es bleibt nur zum Nachlesen stehen; es gibt keine Fragen, Karten oder Aufgaben dazu.</div>')
        d = dict(d, merk='', exam='')
    if d.get('ag'):   # Prüfungsausgrenzung: ganzes Unterthema für die Klausur nicht notwendig, von Haus aus ausgeblendet (S.uaus)
        out.append('<div class="box ag-hinweis"><b>Nicht in der Klausur notwendig.</b> ' + (d.get('ag_text') or 'Dieses Unterthema ist laut Prüfungsausgrenzung ausgegrenzt.')
                   + ' Es ist deshalb ausgeblendet: Die Fragen kommen nicht in Training, Übungs- und Probeklausur. Lesen kannst du es weiter; '
                   'über „Einblenden“ in der Werkzeugleiste holst du es zurück.</div>')
    if d.get('ag_hinweis'):   # Prüfungsausgrenzung: Teile dieses Unterthemas sind ausgegrenzt (stehen eingeklappt weiter unten)
        out.append(f'<div class="box ag-hinweis"><b>Prüfungsausgrenzung.</b> {d["ag_hinweis"]}</div>')
    if d.get('grob'):   # Prüfungsausgrenzung „nicht im Detail relevant“: Überblick oben, Details eingeklappt
        out.append(f'<div class="box grob-ueberblick"><b>Nur grob wissen.</b> {d["grob"]}</div>')
    if d.get('chips'):
        out.append(f'<div class="chips v2top">{d["chips"]}</div>')
    f, cap = d.get('fig', ''), d.get('figcap', '')
    m = re.search(r'<div class="fig-cap"><span>([^<]*)</span>(?:<span>[^<]*</span>)?</div>\s*$', f)
    if m and not cap:
        f, cap = f[:m.start()], m.group(1)
    main = figur(f, cap) if f else ''
    if main and d.get('fig_ag'):   # Schaubild gehört zu einem ausgegrenzten Teil: eingeklappt
        main = f'<details class="ag-teil"><summary>{d["fig_ag"]}</summary>{main}</details>'
    elif main and d.get('fig_grob'):   # Schaubild nur zur Veranschaulichung („nicht im Detail relevant“): eingeklappt
        main = f'<details class="grob-teil"><summary>{d["fig_grob"]}</summary>{main}</details>'
    kurz = f'<div><div class="sec-h">Kurz erklärt</div><div class="kurz">{d.get("kurz", "")}</div></div>'
    mw = [int(x) for x in re.findall(r'min-width:(\d+)px', f)]
    if main and (d.get('wide') or (mw and max(mw) >= 540)):
        out.append(f'<div class="lv1 stack">{kurz}</div><div class="sec">{main}</div>')
    elif main:
        out.append(f'<div class="lv1">{kurz}<div>{main}</div></div>')
    else:
        out.append(f'<div class="lv1 stack">{kurz}</div>')
    if d.get('merk'):
        out.append(f'<div class="merk"><b>Merksatz</b>{d["merk"]}</div>')
    if d.get('article'):
        out.append('<div class="mainbtns"><button class="bigbtn a gobtn" type="button">Ganz erklären <span class="ar">▾</span></button></div>')
    fall = ('<div class="box fall"><div class="box-h">Klausurfallen</div><ul>' + ''.join(f'<li>{x}</li>' for x in d['fehler']) + '</ul></div>') if d.get('fehler') else ''
    exam = f'<div class="box excl">★ <b>Klausur:</b> {d["exam"]}</div>' if d.get('exam') else ''
    links = lambda ids: '<div class="links">' + ''.join(f'<a data-go="lern|{fid}|{ziel[i][0]}|{i}">→ {ziel[i][1]}</a>' for i in ids if i in ziel) + '</div>'
    rin = d.get('rel', []); rout = [x for x in zurueck.get(d['id'], []) if x not in rin]
    rel = ('<div class="relline">' + (f'<span>Baut auf:</span>{links(rin)}' if rin else '') + (f'<span>Weiter mit:</span>{links(rout)}' if rout else '') + '</div>') if (rin or rout) else ''
    out.append(f'<div class="article"><div class="toc"></div>{d.get("article", "")}{exam}{fall}{rel}</div>')
    return f'<article class="topic v3 open" id="{d["id"]}" data-id="{d["id"]}"><div class="t-body">{"".join(out)}</div></article>'


def schuetze(js):
    """Jede ausführende Anweisung eines Schaubild-Skripts einzeln absichern: Fehlt das Element eines anderen Unterthemas,
    soll das nicht alle folgenden Schaubilder abbrechen. Deklarationen (const/let/function) bleiben unverändert im selben Gültigkeitsbereich."""
    out = []
    for st in stmts(js):
        if re.match(r'^(const|let|var|function|class|async\s+function)\b', st) or st.startswith('/*') or st.startswith('//'):
            out.append(st)
        else:
            out.append('try {\n' + st + '\n} catch (e) { LT_FIG.fehler = (LT_FIG.fehler || 0) + 1; }')
    return '\n'.join(out)


# ---------- Auswahlfragen: Ist die richtige Antwort zu oft die längste? (dann lässt sie sich raten) ----------
def mc_bericht(fid, fr):
    n = l = 0
    for q in fr:
        for a in q['a']:
            if a['y'] != 'mc' or len(a['o']) < 3:
                continue
            n += 1
            L = [len(txt(o[0])) for o in a['o']]
            if L[[k for k, o in enumerate(a['o']) if o[1]][0]] == max(L):
                l += 1
    if n and l / n > .5:
        print(f'  Hinweis {fid}: Bei {round(100 * l / n)} % der {n} Auswahlfragen ist die richtige Antwort die längste (Ziel: unter 40 %).')


# ---------- Gedächtnis: feste IDs je Aufgabe (müssen zu app/js/gedaechtnis.js passen) ----------
def ohne_tex_reste(o):
    """„{,}“ (TeX-Dezimalkomma) außerhalb von \\( … \\) wird zu „,“ – sonst steht es roh im Text (z. B. im Arbeitsblatt)."""
    if isinstance(o, str):
        teile = re.split(r'(\\\(.*?\\\)|\\\[.*?\\\])', o, flags=re.S)
        return ''.join(t if i % 2 else t.replace('{,}', ',') for i, t in enumerate(teile))
    if isinstance(o, list): return [ohne_tex_reste(x) for x in o]
    if isinstance(o, dict): return {k: ohne_tex_reste(v) for k, v in o.items()}
    return o


def pruefe_klausur(fid, K, ziel, aus=()):
    """Probeklausur-Bogen prüfen: Punkte je Aufgabe = Summe der Teile, jede Variante hat genau die Punkte ihres Teils."""
    K = ohne_tex_reste(K)
    for A in K['aufgaben']:   # Prüfungsausgrenzung (ag: true an einer Variante): bleibt in inhalte/, wird aber nicht gebaut
        for T in A['teile']: T['varianten'] = [v for v in T['varianten'] if not v.get('ag') and (not v.get('unter') or v['unter'] in ziel)]   # auch Varianten zu weggelassenen Unterthemen
    for A in K['aufgaben']:
        assert A['punkte'] == sum(T['punkte'] for T in A['teile']), f"{fid}/klausur.json Aufgabe {A['titel']}: Punkte passen nicht"
        for T in A['teile']:
            assert T['varianten'], f"{fid}/klausur.json: Teil ohne Varianten"
            for v in T['varianten']:
                assert sum(f['p'] for f in v['felder']) == T['punkte'], f"{fid}/klausur.json {v['id']}: {sum(f['p'] for f in v['felder'])} statt {T['punkte']} Punkte"
                assert not v.get('unter') or v['unter'] in ziel, f"{fid}/klausur.json {v['id']}: unbekanntes Unterthema {v.get('unter')}"
                assert not v.get('unter') or v['unter'] not in aus, f"{fid}/klausur.json {v['id']}: Variante zu ausgegrautem Unterthema {v['unter']}"
    ids = [v['id'] for A in K['aufgaben'] for T in A['teile'] for v in T['varianten']]
    assert len(ids) == len(set(ids)), f"{fid}/klausur.json: doppelte IDs"
    return K


def aufgaben_ids(fid, pro, begriffe, fach, aufg, karten=()):
    """IDs je Unterthema: Frage = Familie + Aufgabenart, Karte/Begriff je Glossarbegriff, Merksatz, Teilaufgaben.
    Verschwindet eine ID gegenüber dem letzten Bau, warnt der Bau (Stand ginge verloren → inhalte/umbenannt.json)."""
    out = {}
    for k in fach['kapitel']:
        for t in k['themen']:
            l = out.setdefault(t['id'], [])
            for q in pro.get(t['id'], []):
                l += [f"q:{q['id']}:{y}" for y in dict.fromkeys(a['y'] for a in q['a'])]
            for g in begriffe:
                if g['heimat'] == t['id']:
                    b = txt(g['begriff']); l += [f'k:{fid}:{b}', f'b:{fid}:{b}']
            if t.get('merk') and not t.get('aus'):
                l.append(f"m:{fid}/{t['id']}")
            l += [f"c:{fid}:{txt(c['v'])}" for c in karten if c['t'] == t['id']]
            for A in aufg:
                if A['unter'][0] == t['id']:
                    l += [f"a:{fid}:{A['id']}:{j}" for j in range(len(A['teile']))]
    alle = sorted(i for l in out.values() for i in l)
    pfad = IN / fid / 'ids.json'
    if pfad.exists():
        weg = sorted(set(json.loads(pfad.read_text())) - set(alle))
        umb = json.loads((IN / 'umbenannt.json').read_text()) if (IN / 'umbenannt.json').exists() else {}
        weg = [i for i in weg if i not in umb]
        if weg:
            print(f'  Achtung {fid}: {len(weg)} Aufgaben-IDs sind weggefallen (Lernstand dazu geht verloren), z. B. {weg[:3]}.'
                  ' Umbenannt? Dann alt → neu in inhalte/umbenannt.json eintragen.')
    pfad.write_text(json.dumps(alle, ensure_ascii=False, indent=0) + '\n', encoding='utf-8')
    return out


def wichtig_varianten(kl, ids):
    for A in kl['aufgaben']:
        for T in A['teile']:
            for v in T['varianten']:
                if v['id'] in ids: v['w'] = 1
    return kl


# ---------- Daten ----------
DEF_OFFEN = []


def daten():
    reg, stud = lies('faecher.json')['faecher'], lies('studium.json')
    neu = sorted(lies('neuigkeiten.json')['eintraege'], key=lambda e: e['id'], reverse=True) if (IN / 'neuigkeiten.json').exists() else []
    index = dict(semester=stud['semester'], klausuren=stud['klausuren'], faecher=[], neu=neu,
                 umbenannt=lies('umbenannt.json') if (IN / 'umbenannt.json').exists() else {})
    for f in reg:
        fid = f['id']
        if not (IN / fid / 'fach.json').exists():   # Fach eingetragen, aber noch nicht gebaut (neuer Kurs): überspringen
            print(f'  {fid}: noch keine Lernseiten (inhalte/{fid}/fach.json fehlt) – übersprungen')
            continue
        fach, fr, gl = lies(f'{fid}/fach.json'), lies(f'{fid}/fragen.json')['familien'], lies(f'{fid}/glossar.json')
        if (IN / fid / 'definitionen.json').exists(): definitionen_gold(fach, lies(f'{fid}/definitionen.json')['definitionen'])   # Wortlaut der Folien-Definitionen gold
        if (IN / fid / 'fragen_neu.json').exists():   # neue Fragen-Familien (LernTool) ergänzen die alten
            fr = fr + lies(f'{fid}/fragen_neu.json')['familien']
        weg = set(lies(f'{fid}/ausgeblendet.json')['themen']) if (IN / fid / 'ausgeblendet.json').exists() else set()
        if weg:   # ausgeblendete Unterthemen (nicht klausurrelevant): Inhalte bleiben in inhalte/, werden aber nicht gebaut
            for k in fach['kapitel']: k['themen'] = [t for t in k['themen'] if t['id'] not in weg]
            fach['kapitel'] = [k for k in fach['kapitel'] if k['themen']]
            fr = [q for q in fr if q['t'] not in weg]
            gl = dict(gl, begriffe=[g for g in gl['begriffe'] if g.get('heimat') not in weg])   # nicht klausurrelevant: komplett weg (Nutzerwunsch 17.11.2026)
        fr = [q for q in fr if not q.get('ag')]   # Prüfungsausgrenzung (ag: true): Familie bleibt in inhalte/, wird aber nicht gebaut
        gl = dict(gl, begriffe=[g for g in gl['begriffe'] if not g.get('ag')])
        for q in fr:   # jede Familie braucht eine feste ID (Gedächtnis: Stufe je Aufgabe)
            q.setdefault('id', f"{fid}:{q['t']}:" + hashlib.sha1(txt(q['a'][0].get('p', '')).encode()).hexdigest()[:8])
        doppelt = {q['id'] for q in fr if sum(1 for r in fr if r['id'] == q['id']) > 1}
        assert not doppelt, f'{fid}: doppelte Fragen-IDs {sorted(doppelt)[:5]}'
        defs_nutz, nach_def = definitionen_fragen(fid, fr)   # eine Definition je Begriff: Begriffs-Schlüssel b, „auch richtig“, Nachschärf-Karten
        # „Wichtig“: oft geprüfte Punkte (werkzeuge/wichtig.py) → w an Unterthema, Familie (mit Punkt-Kürzel p), Karte, Begriff, Aufgabe, Variante
        wi = lies(f'{fid}/wichtig.json') if (IN / fid / 'wichtig.json').exists() else dict(themen={}, familien={}, karten=[], begriffe=[], aufgaben=[], varianten=[])
        pro = {}
        for q in fr:
            pro.setdefault(q['t'], []).append(dict(id=q['id'], z=q.get('z', ''), a=q['a'], **({'b': q['b']} if q.get('b') else {}), **(dict(w=1, p=wi['familien'][q['id']]) if q['id'] in wi['familien'] else {})))
        aufg = lies(f'{fid}/aufgaben.json')['aufgaben'] if (IN / fid / 'aufgaben.json').exists() else []
        karten = lies(f'{fid}/karten.json')['karten'] if (IN / fid / 'karten.json').exists() else []   # Karteikarten (Aufzählungen, Formeln, Begriffe)
        aufg = [A for A in aufg if not A.get('ag')]   # Prüfungsausgrenzung: Aufgabe/Karte bleibt in inhalte/, wird aber nicht gebaut
        karten = [c for c in karten if not c.get('ag')]
        karten = [c for c in karten if c.get('t') not in weg]   # ausgeblendete Unterthemen: auch ihre Karten und Aufgaben weg
        aufg = [A for A in aufg if not (A.get('unter') and set(A['unter']) <= weg)]
        for A in aufg:
            if A.get('unter'): A['unter'] = [u for u in A['unter'] if u not in weg]
        vorne = [txt(c['v']) for c in karten]
        assert len(vorne) == len(set(vorne)), f"{fid}/karten.json: doppelte Vorderseiten {sorted({v for v in vorne if vorne.count(v) > 1})[:5]}"
        # Ausgegraute Unterthemen (aus: True, „kommt nicht dran“): keine Fragen, Karten, Begriffskarten, Aufgaben, Merksatz-Karte
        aus = {t['id'] for k in fach['kapitel'] for t in k['themen'] if t.get('aus')}
        if aus:
            fr = [q for q in fr if q['t'] not in aus]
            pro = {t: v for t, v in pro.items() if t not in aus}
            karten = [c for c in karten if c['t'] not in aus]
            gl = dict(gl, begriffe=[g for g in gl['begriffe'] if g['heimat'] not in aus])
            aufg = [A for A in aufg if not set(A['unter']) & aus]
        mc_bericht(fid, fr)
        wk, wb, wa, wv = set(wi['karten']), set(wi['begriffe']), set(wi['aufgaben']), set(wi['varianten'])
        for c in karten:
            if txt(c['v']) in wk: c['w'] = 1
        for g in gl['begriffe']:
            if g['begriff'] in wb: g['w'] = 1
        for A in aufg:
            if A['id'] in wa: A['w'] = 1
        ids = aufgaben_ids(fid, pro, gl['begriffe'], fach, aufg, karten)
        kap, inhalt = [], {}
        ziel = {t['id']: (k['id'], t['titel_text']) for k in fach['kapitel'] for t in k['themen']}
        zurueck = {}
        for k in fach['kapitel']:
            for t in k['themen']:
                for r in t.get('rel', []):
                    zurueck.setdefault(r, []).append(t['id'])
        for k in fach['kapitel']:
            kap.append(dict(id=k['id'], title=k['titel_text'], intro=txt(k.get('intro', '')), topics=[
                dict(id=t['id'], title=t['titel_text'], star=bool(t.get('star')), **(dict(aus=1) if t.get('aus') else {}), **(dict(ag=1) if t.get('ag') else {}), **(dict(w=1) if t['id'] in wi['themen'] else {}), alt=txt(t.get('alt', '')), nf=len(pro.get(t['id'], [])), ni=len(ids.get(t['id'], [])),
                     **(dict(nk=1) if t.get('aus') else {}),   # ausgegraut = nicht klausurrelevant: nicht in Übungsklausur und Refresh
                     **({'nz': sorted(set(re.findall(r'data-nz="([^"]+)"', t.get('article', ''))))} if 'data-nz=' in t.get('article', '') else {}))   # eingearbeiteter Folienstoff (werkzeuge/einarbeiten.py)
                for t in k['themen']]))
            for t in k['themen']:
                inhalt[t['id']] = dict(kern=t.get('kern', ''), merk='' if t.get('aus') else t.get('merk', ''), exam='' if t.get('aus') else t.get('exam', ''), fehler=t.get('fehler', []), src=txt(t.get('src', '')),
                                       html=koerper(fid, t, ziel, zurueck))
        farbe = FARBE.get(fid) or ((f.get('farben') or {}).get('hell') or {}).get('primary', '#334')
        # Nacharbeiten: Fragen-Varianten, die an eingearbeiteten Folienstoff angepasst wurden (Feld „vorher“ = alte Fassung) → [Familie, Index, Art, Unterthema]
        nach = [[q['id'], i, a['y'], q['t']] for q in fr for i, a in enumerate(q['a']) if 'vorher' in a]
        # Nacharbeiten, Teil 2: je Familie zum eingearbeiteten Folienstoff (ID „:nz-“, werkzeuge/einarbeiten.py) die erste Variante → [Familie, Index, Art, Unterthema]
        nach_nz = [[q['id'], 0, q['a'][0]['y'], q['t']] for q in fr if ':nz-' in q['id'] and q.get('a')]
        index['faecher'].append(dict(**({'nach': {'b1': nach}} if nach else {}), **({'nachNz': nach_nz} if nach_nz else {}), **({'nachDef': nach_def} if nach_def else {}),
                                     id=fid, name=f['name'], lang=f['lang'], person=f['person'], mix=f.get('mix', {}), tiefe=f.get('tiefe', 3),
                                     farbe=farbe, rechnen=f.get('rechnen', fid == 'mathe'), englisch=f.get('englisch', fid == 'produktion'), kapitel=kap,
                                     **(dict(folien=originalfolien(fid)) if (IN / fid / 'folien.json').exists() else {})))
        figuren = schuetze((IN / fid / 'figuren.js').read_text(encoding='utf-8'))
        uebers = lies(f'{fid}/uebers.json') if (IN / fid / 'uebers.json').exists() else None
        for A in aufg:   # jede große Aufgabe muss an echten Unterthemen hängen
            assert A['unter'] and all(u in ziel for u in A['unter']), f"{fid}/aufgaben.json {A['id']}: unbekanntes Unterthema {A['unter']}"
            assert all(T['punkte'] > 0 for T in A['teile']), A['id']
        for c in karten:
            assert c['t'] in ziel, f"{fid}/karten.json: unbekanntes Unterthema {c['t']}"
        if (IN / fid / 'definitionen.json').exists():   # wichtige Definitionen: überall im Wortlaut der Folie (werkzeuge/definitionen_folien.py)
            nur = lambda h: re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', h or ''))).strip().casefold()
            themen_ = {t['id']: t for k in fach['kapitel'] for t in k['themen']}
            for D_ in lies(f'{fid}/definitionen.json')['definitionen']:
                seite = nur(themen_[D_['t']]['article'])
                if not all(nur(k) in seite for k in D_['kern']): DEF_OFFEN.append(f"{fid}/{D_['t']}: {D_['begriff']}")   # noch nicht eingearbeitet (Hinweis, kein Abbruch)
                assert any(c.get('r') == D_['wortlaut'] for c in karten), f"{fid}: Definition „{D_['begriff']}“ fehlt als Karteikarte"
                assert any(q.get('id', '').endswith(':df-' + re.sub(r'[^a-z0-9]+', '-', D_['begriff'].lower().replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')).strip('-')[:30]) for q in fr), f"{fid}: Definition „{D_['begriff']}“ fehlt in den Fragen"
        for q in fr:
            assert q['t'] in ziel, f"{fid}: Frage zu unbekanntem Unterthema {q['t']}"
        nutz = dict(inhalt=inhalt, fragen=pro, defs=defs_nutz, glossar=gl['begriffe'], nicht_markieren=gl['nicht_markieren'], uebers=uebers, aufgaben=aufg, karten=karten,
                    klausur=wichtig_varianten(pruefe_klausur(fid, lies(f'{fid}/klausur.json'), ziel, aus), wv) if (IN / fid / 'klausur.json').exists() else None)
        nutz, figuren = ohne_folienverweise(nutz), ohne_fv(figuren)
        (DIST / 'daten' / f'{fid}.js').write_text(
            f'LT_FIG[{json.dumps(fid)}] = function () {{\n{figuren}\n}};\nLT.fachGeladen({json.dumps(fid)}, {json.dumps(nutz, ensure_ascii=False)});\n', encoding='utf-8')
    for e in index['neu']:   # Pflicht-Hinweis zu eingearbeitetem Stoff: alle Unterthemen mit dieser Überarbeitung
        if e.get('nz'): e['themen'] = [f"{f['id']}/{t['id']}" for f in index['faecher'] for k in f['kapitel'] for t in k['topics'] if e['nz'] in t.get('nz', [])]
    index = ohne_folienverweise(index)
    (DIST / 'daten' / 'index.js').write_text('window.LT_INDEX = ' + json.dumps(index, ensure_ascii=False) + ';\n', encoding='utf-8')
    return index



# ---------- Keine Folienverweise im Lernstoff (Wunsch des Nutzers, 12.11.2026) ----------
# „Folie 12 nennt …“, „nach Folie 5“, „(Folie 3)“, „Slide 24.“ werden beim Bauen neutral umformuliert oder entfernt.
# Ausgenommen: das Feld „src“ (Quelle eines Unterthemas, führt in die Originalfolien) und die Originalfolien selbst.
_N = r'(?:\d+[a-z]?|#)'
_F = rf'(?:Folien?|Slides?)(?:\s|&nbsp;)*{_N}(?:\s*(?:–|-|,|und|and|bis|/|&amp;)\s*{_N})*'
_E = r'(?=[\s.,;:!?)\]·<"&*/]|$)'
F = _F + _E
_FV_REGELN = [
    # Sonderfälle zuerst
    (rf'\bwie (?:in|auf) {F}', 'wie oben'),
    (rf'\bnur {F}:\s*', 'nur '),
    (rf'\b{_F} \(([^()]+)\) ist', r'Der Punkt „\1“ ist'),
    (rf'\bIn der Mitte von {F}', 'In der Mitte des Schaubilds'),
    (rf'\bIn the middle of {F}', 'In the middle of the figure'),
    (rf'\bLinks auf {F}', 'Links im Schaubild'),
    (rf'\bOn the left of {F}', 'On the left of the figure'),
    (rf'\b(?:Musterfrage|Sample question|Definition) {F}\.?', ''),
    (rf'<small>{_F}</small>', ''),
    (rf'(?<=>){_F}(?=<)', ''),
    (r"(?:Folien?|Slides?) <span class='fr'>(?:<span>\d+</span>){2}</span>\.?\s*(?:·\s*)?", ''),
    (rf'^{_F}(?:\s+#)*$', ''),
    (rf'^{F}\s*·\s*', ''),
    (rf'\b[Ss]ample question {F}', ''),
    # Klammern
    (rf'\s*\(\s*(?:Bild auf |siehe )?{F}\s*\)', ''),
    (rf'\(\s*{F}\s*[,:;]\s*', '('),
    (rf'\s*[,;]\s*{F}(?=\s*\))', ''),
    # „nach Haller, Folie 5“, „DMAIC, Slide 83.“
    (rf'(?<=\w)(\.?)\s*,\s*{F}', r'\1'),
    # Präpositionen
    (rf'\bnach (?:den |der )?{F}', 'nach der Vorlesung'),
    (rf'\bNach (?:den |der )?{F}', 'Nach der Vorlesung'),
    (rf'\b(?:laut|gemäß) (?:den |der )?{F}', 'laut Vorlesung'),
    (rf'\bafter {F}', 'after the lecture'),
    (rf'\baccording to {F}', 'according to the lecture'),
    (rf'\b[Aa]uf (?:den |der )?{F}', lambda m: ('In' if m.group(0)[0] == 'A' else 'in') + ' der Vorlesung'),
    (rf'\b[Oo]n {F}', lambda m: ('In' if m.group(0)[0] == 'O' else 'in') + ' the lecture'),
    (rf'\b(?:von|aus) (?:den |der )?{F}', 'aus der Vorlesung'),
    (rf'\bfrom {F}', 'from the lecture'),
    (rf'\bzu (?:den |der )?{F}', 'zur Vorlesung'),
    (rf'\bto {F}', 'to the lecture'),
    (rf'\bder {F}', 'der Vorlesung'),
    (rf'\bof {F}', 'of the lecture'),
    (rf'\bwie {F}', 'wie in der Vorlesung'),
    (rf'\b(?:like|as on) {F}', 'as in the lecture'),
    # Satzanfang „Folie 5: …“ / Erklärung nur „Folie 5.“
    (rf'(?:(?<=^)|(?<=· )|(?<=&quot;)|(?<=")|(?<=>)){F}\.\s*(?:·\s*)?', ''),
    (rf'(?:(?<=^)|(?<=\. )|(?<=· )|(?<=&quot;)|(?<=")|(?<=>)){F}:\s*([\w#])', lambda m: m.group(1).upper()),
    (rf'{_F} \(([^()]*=[^()]*)\):', lambda m: ('Example' if m.group(0).startswith('S') else 'Beispiel') + ' (' + m.group(1) + '):'),
    (rf'(?<=>){F}\s*·\s*', ''),
    (rf'(?<=>){F},\s*(\w)', lambda m: m.group(1).upper()),
    (rf'(?<=^){F}\s*(?=\()', ''),
    (rf'{_F} \((ein|a) ([^()]+)\)', lambda m: m.group(1).capitalize() + ' ' + m.group(2)),
    (rf'(?:(?<=^)|(?<=[.!?:] )|(?<=· )|(?<=&quot;)|(?<=")|(?<=>)|(?<=\n)){_F}(?= \()', lambda m: 'The lecture' if m.group(0).startswith('S') else 'Die Vorlesung'),
    # Subjekt: „Folie 12 nennt …“, „Welche … nennt Folie 3?“
    (rf'(?:(?<=^)|(?<=[.!?:] )|(?<=· )|(?<=&quot;)|(?<=")|(?<=>)|(?<=\n)){_F}(?= \w)', lambda m: 'The lecture' if m.group(0).startswith('S') else 'Die Vorlesung'),
    (rf'(?<=\w ){_F}(?=[\s?.,])', lambda m: 'the lecture' if m.group(0).startswith('S') else 'die Vorlesung'),
    (rf'\s*·\s*{F}', ''),
    # ohne Nummer: „So steht es auf der Folie“, „nicht in den Folien“, „Beispiel der Folien“
    (r'\b(Beispiel|Example) (?:Folien?|Slides?):\s*', r'\1: '),
    (r'\b([Ll])aut Folie\b', r'\1aut Vorlesung'),
    (r'\bBeispiel Folie\b', 'Beispiel'),
    (r'\beine der wichtigsten Folien\b', 'eines der wichtigsten Themen'),
    (r'\b([Ww])eitere Folien folgen', r'\1eitere Inhalte folgen'),
    (r'\bfehlenden Folien\b', 'fehlenden Unterlagen'),
    (r'-Folie\b', '-Vorlesung'),
    (r'\b([Aa])uf (?:den )?(?:zwei|drei|vier|beiden) Folien\b', lambda m: ('In' if m.group(1) == 'A' else 'in') + ' der Vorlesung'),
    (r'\s*\((?:Folien?|slides?)\)', ''),
    (r'\b([Aa])uf (?:der|den|dieser|einer) (?:aktuellen )?Folien?\b', lambda m: ('In' if m.group(1) == 'A' else 'in') + ' der Vorlesung'),
    (r'\b([Ii])n (?:der|den) (?:aktuellen )?Folien?\b', r'\1n der Vorlesung'),
    (r'\b(aus|von) (?:der|den) Folien?\b', r'\1 der Vorlesung'),
    (r'\bzu (?:der|den) Folien?\b', 'zur Vorlesung'),
    (r'\b(?:der|den) Folien?\b', 'der Vorlesung'),
    (r'\b([Dd])ie Folien?\b', r'\1ie Vorlesung'),
    (r'\b(?:Example )?Slide #:\s*', 'Example: '),
    (r'\b([Oo]n|[Ii]n) the (?:current )?slides?\b', lambda m: ('In' if m.group(1)[0] in 'OI' else 'in') + ' the lecture'),
    (r'(?<=’s) slides\b', ' lecture'),
    (r'\b([Tt])he slides?\b', r'\1he lecture'),
]
_FV_REGELN = [(re.compile(a), b) for a, b in _FV_REGELN]
FV_REST = re.compile(_F + _E + r'|\b(?:[Aa]uf|[Ii]n|laut|von|aus|der|den|[Dd]ie|the|on) (?:aktuellen |current )?(?:Folien?|[Ss]lides?)\b')

_FV_TAB = re.compile(r'<table\b.*?</table>', re.S)
_FV_ZEILE = re.compile(r'<tr\b[^>]*>.*?</tr>', re.S)
_FV_ZELLE = re.compile(r'<t[hd]\b[^>]*>.*?</t[hd]>', re.S)


def _fv_tabelle(m):
    """Tabellenspalte „Folie“/„Folien“ (nur Foliennummern) ganz weglassen."""
    t = m.group(0); kopf = _FV_ZEILE.search(t)
    if not kopf: return t
    zellen = _FV_ZELLE.findall(kopf.group(0))
    weg = [i for i, z in enumerate(zellen) if re.sub(r'<[^>]+>', '', z).strip() in ('Folie', 'Folien', 'Slide', 'Slides')]
    if not weg: return t
    def zeile(z):
        n = [-1]
        def zelle(c):
            n[0] += 1
            return '' if n[0] in weg else c.group(0)
        return _FV_ZELLE.sub(zelle, z.group(0))
    return _FV_ZEILE.sub(zeile, t)


def ohne_fv(s):
    if 'olie' not in s and 'lide' not in s: return s
    if '<table' in s: s = _FV_TAB.sub(_fv_tabelle, s)
    for a, b in _FV_REGELN: s = a.sub(b, s)
    return s

def ohne_folienverweise(o, k=None):
    if isinstance(o, dict): return {ohne_fv(kk): (v if kk == 'src' else ohne_folienverweise(v, kk)) for kk, v in o.items()}
    if isinstance(o, list): return [ohne_folienverweise(v, k) for v in o]
    return ohne_fv(o) if isinstance(o, str) else o


# Fächer, die Wort für Wort auf Folienstand sein müssen (Nutzerwunsch: nur IBL); alle anderen wie vor dem Folien-Update vom 13.11.2026
FOLIENTREU = {'ibl', 'mkt'}   # Marketing: Folien und Randnotizen vollständig, Durchgestrichenes weg (Nutzerwunsch 17.11.2026)


def originalfolien(fid):
    """Originalfolien (werkzeuge/originalfolien.py): PDFs nach dist/folien/<fach>/, Zuordnung nach dist/folien/<fach>.js (lädt erst in der Ansicht).
    Im Index nur die Zahl der Unterlagen und Seiten."""
    fo = lies(f'{fid}/folien.json')
    if fid not in FOLIENTREU:   # nur die Seiten und ihre Lernseiten zeigen, keine Abgleichslisten (Nutzerwunsch 17.11.2026)
        for ss in fo['seiten'].values():
            for x in ss: x.pop('f', None)
    (DIST / 'folien' / fid).mkdir(parents=True, exist_ok=True)
    for d in fo['decks']:
        shutil.copy(IN / fid / 'folien' / (d['id'] + '.pdf'), DIST / 'folien' / fid / (d['id'] + '.pdf'))
        # vorab gerenderte Seitenbilder (werkzeuge/folienbilder.py): schnelle Anzeige ohne PDF-Zeichnen im Browser
        bilder = IN / fid / 'folien' / 'bilder' / d['id']
        if bilder.is_dir() and len(list(bilder.glob('*.webp'))) == d['n']:
            ziel = DIST / 'folien' / fid / d['id']
            if ziel.exists(): shutil.rmtree(ziel)
            shutil.copytree(bilder, ziel, ignore=shutil.ignore_patterns('stand.txt'))
            d['bilder'] = f"folien/{fid}/{d['id']}/"
    (DIST / 'folien' / f'{fid}.js').write_text(f'LT_folienGeladen({json.dumps(fid)}, {json.dumps(fo, ensure_ascii=False, separators=(",", ":"))});\n', encoding='utf-8')
    return dict(u=len(fo['decks']), s=sum(d['n'] for d in fo['decks']))


SEITE = '''<title>Lernweh</title>
<meta name="description" content="Lernwerkzeug Introduction to English Linguistics: Lernseiten, Sandbox und Übungsklausuren">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&display=swap">
<link rel="stylesheet" href="katex.css">
<link rel="stylesheet" href="inhalt.css">
<link rel="stylesheet" href="app.css">
<script>(function(){try{var t=localStorage.getItem('lt-theme');if(t==='light'||t==='dark')document.documentElement.setAttribute('data-theme',t);}catch(e){}})();</script>
<div id="app" class="app"></div>
<script src="katex.js"></script>
<script src="laufzeit.js"></script>
<script src="daten/index.js"></script>
''' + ''.join(f'<script src="{j}"></script>\n' for j in JS_DATEIEN)


def main():
    if DIST.exists():
        for p in DIST.rglob('*'):
            if p.is_file():
                p.unlink()
    (DIST / 'daten').mkdir(parents=True, exist_ok=True)
    index = daten()
    # Nichts darf verloren gehen: jede Definition vollständig im Text, jede Folienformulierung eingearbeitet oder begründet vermerkt
    assert not DEF_OFFEN, f'{len(DEF_OFFEN)} Definitionen nicht vollständig im Text der Lernseite (werkzeuge/einarbeiten/): {DEF_OFFEN[:5]}'
    for f_ in lies('faecher.json')['faecher']:
        po = IN / f_['id'] / 'plan' / 'einarbeiten_offen.json'
        if po.exists():
            offen_ = json.loads(po.read_text(encoding='utf-8'))
            assert not offen_, f"{f_['id']}: {len(offen_)} Folienformulierungen noch nicht eingearbeitet (python3 werkzeuge/einarbeiten_liste.py {f_['id']}), z. B. {[(x['t'], x['stelle']) for x in offen_[:3]]}"
        pf_ = IN / f_['id'] / 'folien.json'   # Originalfolien: kein Stichpunkt „fehlt vielleicht“ mehr offen (nur foliengetreue Fächer, FOLIENTREU)
        if pf_.exists() and f_['id'] in FOLIENTREU:
            fe_ = [(dk, x['n'], it[1]) for dk, ss in json.loads(pf_.read_text(encoding='utf-8'))['seiten'].items() for x in ss for it in x.get('f') or [] if it[2] == 'fehlt']
            if os.environ.get('FOLIEN_OFFEN') and fe_: print(f"  Hinweis: {f_['id']}: {len(fe_)} Stichpunkte noch auf „fehlt“ (nur Zwischenstand, FOLIEN_OFFEN)"); fe_ = []
            assert not fe_, f"{f_['id']}: {len(fe_)} Stichpunkte der Originalfolien stehen noch auf „fehlt“: {fe_[:5]}"
    (DIST / 'laufzeit.js').write_text(laufzeit(), encoding='utf-8')
    alt_css = (IN / 'basis' / 'alt_inhalt.css').read_text(encoding='utf-8') + '[data-lang="en"] .l-de,[data-lang="de"] .l-en{display:none!important}'
    sprache = ('\n.inhalt[data-lang="en"] .l-de,.inhalt[data-lang="de"] .l-en,html[data-lang="en"] .l-de,html[data-lang="de"] .l-en{display:none!important}'   # Sprachschalter (auch im aufgeklappten Schaubild)
               '\n.inhalt .zw2 p{margin:0 0 .8em}.inhalt .zw2 ul,.inhalt .zw2 ol{margin:.2em 0 .9em}'
               '\n.p-spiel{background:var(--pale-2);border:1px solid var(--line);border-radius:14px;padding:14px 16px;margin:14px 0}.sp-kopf{display:flex;justify-content:space-between;gap:10px;font-weight:800;font-size:.8rem;letter-spacing:.04em;text-transform:uppercase;color:var(--primary-2)}.sp-kopf small{color:var(--muted)}'
               '.sp-karte{font-size:1.06rem;font-weight:700;margin:8px 0 12px}.sp-wahl button.sp-richtig{outline:2px solid var(--pos);outline-offset:1px}.sp-aus{margin-top:10px;line-height:1.55}.sp-aus .btn,.p-spiel .btn{margin-left:6px;border:1px solid var(--line);background:var(--card);border-radius:20px;padding:4px 12px;font-weight:700}.sp-ok{color:var(--pos)}.sp-nok{color:var(--neg)}.sp-ende{margin-bottom:10px}'
               '\n.p1a-leg{display:flex;flex-wrap:wrap;gap:4px 14px;justify-content:center;font-size:.82rem;color:var(--muted);margin:4px 0 2px}.p1a-leg span[class^="lg"]{display:inline-block;width:22px;height:0;border-top:3px solid var(--primary);vertical-align:middle;margin:0 4px 0 10px}.p1a-leg .lg-w{border-top:2px dashed var(--muted)!important}.p1a-leg .lg-l{border-top:2px dashed var(--neg)!important}'
               '\n.inhalt .two>div>b:first-child{display:block;margin-bottom:4px}.inhalt .t td small{color:var(--muted);font-size:.78rem}'
               '\n.inhalt .bruecke{border-left:3px solid var(--primary-2);padding:2px 0 2px 12px;color:var(--muted);font-style:italic;margin:18px 0 10px}\n')
    (DIST / 'inhalt.css').write_text('/* Lernseiten-CSS aus dem alten Lernportal, auf .inhalt begrenzt (bau.py) */\n' + scope(alt_css) + sprache, encoding='utf-8')
    for d in ('katex.js', 'katex.css'):
        shutil.copy(IN / 'basis' / d, DIST / d)
    (DIST / 'pdfjs').mkdir(exist_ok=True)   # PDF-Anzeige der Originalfolien (pdf.js, Apache-2.0, lokal statt aus dem Netz)
    for d in ('pdf.min.js', 'pdf.worker.min.js'):
        shutil.copy(IN / 'basis' / 'pdfjs' / d, DIST / 'pdfjs' / d)
    (DIST / 'app.css').write_text((APP / 'css' / 'app.css').read_text(encoding='utf-8') + '\n' + (APP / 'css' / 'folien.css').read_text(encoding='utf-8'), encoding='utf-8')
    for h in ('login.html', 'admin.html'):   # Online-Version (Vercel): Anmeldung und Code-Verwaltung
        shutil.copy(APP / h, DIST / h)
    # Admin-Auswertung: Titel der Fächer, Oberthemen und Unterthemen (nur Namen) direkt einbauen
    titel, struktur = {}, []
    for f in json.loads((DIST / 'daten' / 'index.js').read_text(encoding='utf-8').split('=', 1)[1].rstrip().rstrip(';'))['faecher']:
        struktur.append(dict(id=f['id'], name=f['name'], farbe=f.get('farbe', '#334'), kapitel=[dict(id=k['id'], title=k['title'], topics=[t['id'] for t in k['topics']]) for k in f['kapitel']]))
        titel[f['id']] = f['name']
        for k in f['kapitel']:
            titel[f"{f['id']}/{k['id']}"] = f"{f['name']} · {k['title']}"
            for t in k['topics']: titel[f"{f['id']}/{t['id']}"] = f"{f['name']} · {t['title']}"
    a_html = (DIST / 'admin.html').read_text(encoding='utf-8').replace('/*TITEL*/{}', json.dumps(titel, ensure_ascii=False)).replace('/*STRUKTUR*/[]', json.dumps(struktur, ensure_ascii=False))
    (DIST / 'admin.html').write_text(a_html, encoding='utf-8')
    for j in JS_DATEIEN:
        shutil.copy(APP / 'js' / j, DIST / j)
    (DIST / 'artifact.html').write_text(SEITE, encoding='utf-8')
    (DIST / 'index.html').write_text('<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n</head>\n<body>\n' + SEITE + '</body>\n</html>\n', encoding='utf-8')
    spuren = re.compile(r'Klausurnotiz|[Ee]xam notes|Gedächtnisprot|Ged\.-Prot|[Mm]eier-Protokoll|Klausurprotokoll|in den Protokollen|Altklausur|Klausureinsicht|bekannten Klausur|kamen? in (?:jeder|allen|mehreren|einer|beiden)? ?Klausur|Prüferstil|\bGPs\b|\bGP-|(?:Klausur|Exam|exam)(?:en|s)?[ -]?(?:Stil )?(?:19|20)\d\d')
    # Prüfer nur als Dozent nennen, nie mit Aussagen über frühere Klausuren (werkzeuge/neutral.py)
    spuren = re.compile(spuren.pattern + r'|\b(?:Meier|Wannenwetsch|Stein|Schief|Stützer|Paul|Chammout|Weinberger|Kersten-Frisch|Krcal)(?:-Block|-Klausur|-Stil|-Variante| verlangt| fragt| stellt das gern| lässt die)|Schiefs Klausur|Schief’s exam|exam every year')
    funde = [(p.name, m.group(0)) for p in DIST.rglob('*') if p.suffix in ('.js', '.html', '.css') and p.parent.name != 'pdfjs' for m in spuren.finditer(p.read_text(encoding='utf-8'))]
    if funde:   # Herkunft der Klausurdaten darf nirgends sichtbar sein
        print('FEHLER: Hinweise auf Klausurquellen in dist:', funde[:10]); sys.exit(1)
    fv = [(p.name, m.group(0)) for p in (DIST / 'daten').glob('*.js') for m in FV_REST.finditer(re.sub(r'"src": "[^"]*"', '', p.read_text(encoding='utf-8')))]
    if fv:   # keine Folienverweise im Lernstoff (Regeln bei ohne_fv)
        print('FEHLER: Folienverweise im Lernstoff:', fv[:10]); sys.exit(1)
    groesse = sum(p.stat().st_size for p in DIST.rglob('*') if p.is_file())
    n = sum(len(k['topics']) for f in index['faecher'] for k in f['kapitel'])
    print(f'gebaut: {len(index["faecher"])} Fächer, {n} Unterthemen, dist {groesse / 1e6:.1f} MB')
    if '--test' in sys.argv:
        fehler = 0
        for t in sorted([*(HIER / 'tests').glob('t_*.js'), *(HIER / 'tests').glob('t_*.mjs')]):
            r = subprocess.run(['node', str(t)], cwd=HIER, capture_output=True, text=True)
            print(f'── {t.name}: ' + ((r.stdout + r.stderr).strip().splitlines() or ['(keine Ausgabe)'])[-1])
            fehler += r.returncode != 0
        print('TESTS OK' if not fehler else f'{fehler} TEST(S) FEHLGESCHLAGEN')
        sys.exit(1 if fehler else 0)


if __name__ == '__main__':
    main()
