"""Ergänzungen aus der Prüfung „Fehlt vielleicht auf der Lernseite“ (Ansicht Originalfolien).

Jeder Stichpunkt der Liste wurde einzeln geprüft (Folientext gegen Lernseite) und genau einer Entscheidung zugeordnet:
  w(...)    Folienformulierung, die auf der Lernseite stehen muss. Eingearbeitet wird von Hand in den normalen Text
            (werkzeuge/einarbeiten/<fach>.py, gold für Lernende, die das Unterthema schon kannten). Dieses Skript prüft nur:
            Begriffe schon im ursprünglichen Text → „anders“, durch das Einarbeiten → „ergänzt“, sonst offen (plan/einarbeiten_offen.json).
  add(...)  Fehlt wirklich: eigener Erklärabschnitt am Ende des Unterthemas.
  ok(...)   Kein Lernstoff (Name, Literatur, Bildunterschrift, Zeilenrest, Tippfehler der Folie) oder schon wörtlich drin:
            Der Begriff verschwindet aus der Liste dieser Seite (inhalte/<fach>/plan/folien_geprueft.json, intern).
  quelle(...) Quellenangabe eines Unterthemas berichtigen (bessere Zuordnung Folie → Lernseite).
Blöcke stehen zwischen <!--of:schlüssel--> … <!--/of:schlüssel--> in inhalte/<fach>/fach.json und werden bei jedem Lauf ersetzt.
Die Entscheidungen je Fach stehen in werkzeuge/folienpruefung/<fach>.py (dort stehen nur Aufrufe von w, ok, kein, quelle, nicht_klausur).
Aufruf: python3 werkzeuge/originalfolien_ergaenzungen.py && python3 werkzeuge/originalfolien.py <fach>"""
import json, pathlib, re, collections, html as html_

IN = pathlib.Path(__file__).resolve().parents[1] / 'inhalte'
WORT = collections.defaultdict(list)    # (fach, tid) -> [(stelle, begriff, text)]
BLOCK = collections.defaultdict(list)   # (fach, tid) -> [(key, html)]
GEPRUEFT = collections.defaultdict(lambda: collections.defaultdict(list))   # fach -> stelle -> [begriffe]
QUELLE = []                             # (fach, tid, alt, neu)
DECKNAME = {}


def w(f, tid, stelle, begriff, text=''):
    """Folienwortlaut: begriff (fett) und text, wie auf der Folie; stelle 'd21/4' (Deck/Seite) für den Verweis"""
    WORT[(f, tid)].append((stelle, begriff, text))


def add(f, tid, key, html): BLOCK[(f, tid)].append((key, html))
def ok(f, stelle, *begriffe, grund='anders'):
    """Begriff bleibt in der Liste, mit Stand: 'anders' = steht auf der Lernseite mit anderen Worten (oder richtig geschrieben),
    'kein' = kein Lernstoff (Literatur, Weblink, Lebenslauf, Bildquelle)"""
    for b in (begriffe or ['*']): GEPRUEFT[f][stelle].append(f'{grund}:{b}')


def kein(f, stelle, *begriffe): ok(f, stelle, *begriffe, grund='kein')


NICHT_KLAUSUR = collections.defaultdict(dict)   # fach -> stelle -> Hinweis
def nicht_klausur(f, stellen, text):
    for st in stellen: NICHT_KLAUSUR[f][st] = text
def quelle(f, tid, alt, neu): QUELLE.append((f, tid, alt, neu))


def ul(*xs): return '<ul>' + ''.join(f'<li>{x}</li>' for x in xs) + '</ul>'


def aufzaehlung(pdf, n):
    """Seite im Lesefluss (pdftotext -raw) in Aufzählungspunkte zerlegen: neue Punkte beginnen bei ➢ • - oder einer Nummer, umbrochene Zeilen werden angehängt"""
    import subprocess
    if not pdf.exists(): return []
    roh = subprocess.run(['pdftotext', '-raw', '-f', str(n), '-l', str(n), str(pdf), '-'], capture_output=True, text=True).stdout
    punkte = []
    for z in roh.splitlines():
        z = z.strip()
        if not z or re.fullmatch(r'\d{1,3}', z): continue
        if re.match(r'^([➢•\uf0b7\uf0d8\uf076▪-]|\d+(\.\d+)*\.?\s|[a-z]\)\s)', z) or not punkte: punkte.append(z)
        else: punkte[-1] += ' ' + z
    return [re.sub(r'\s+', ' ', re.sub(r'^[➢•\uf0b7\uf0d8\uf076▪\s-]+', '', x)).strip() for x in punkte if len(x) > 3]


def ganzer_punkt(satz, fett, punkte):
    """Bruchstück aus der Fehlliste durch den vollständigen Aufzählungspunkt ersetzen, der den Begriff enthält
    (lange Punkte: nur die Sätze mit dem Begriff)"""
    kern = re.sub(r'\s+', ' ', satz).strip(' ➢•-')[:40]
    def kurz(x):
        if len(x) <= 350: return x
        teile = [t for t in re.split(r'(?<=[.:;!?])\s+', x) if any(w in t for w in fett)]
        return ' … '.join(teile)[:600] if teile else satz
    for x in punkte:
        if kern and kern[:25] in x and all(w in x for w in fett): return kurz(x)
    for x in punkte:
        if all(w in x for w in fett): return kurz(x)
    return satz


def woertlich(f, ausser=()):
    """Skriptwortlaut übernehmen: je Folie mit fehlenden Formulierungen die betroffenen Sätze (Begriffe fett) als Ergänzung ins Unterthema.
    Sätze, deren Begriffe alle als Tippfehler/kein Lernstoff vermerkt sind, bleiben draußen."""
    fo = json.loads((IN / f / 'folien.json').read_text(encoding='utf-8'))
    for d in fo['decks']:
        if d['art'] in ('uebung',): continue
        for s_ in fo['seiten'][d['id']]:
            st = f"{d['id']}/{s_['n']}"
            if not s_.get('f') or not s_['t'] or st in ausser: continue
            ausgenommen = {x.split(':', 1)[1] for x in GEPRUEFT[f].get(st, [])}
            if '*' in ausgenommen: continue
            saetze, roh_gesehen, punkte = [], set(), aufzaehlung(IN / f / 'folien' / f"{d['id']}.pdf", s_['n'])
            for satz, fett, *_ in s_['f']:
                fett = [x for x in fett if x not in ausgenommen]
                if not fett: continue
                satz = ganzer_punkt(satz, fett, punkte)
                if satz in roh_gesehen: continue
                roh_gesehen.add(satz)
                h = satz.replace('&', '&amp;').replace('<', '&lt;')
                for x in sorted(fett, key=len, reverse=True): h = re.sub(r'(?<![\wÄÖÜäöüß])' + re.escape(x) + r'(?![\wÄÖÜäöüß])', f'<b>{x}</b>', h, count=1)
                saetze.append(h.strip(' ➢•-'))
            if saetze: w(f, s_['t'][0], st, '', ' · '.join(saetze))



# =====================================================================================================================
# Entscheidungen je Fach laden (werkzeuge/folienpruefung/<fach>.py)
# =====================================================================================================================
AUFGABEN = collections.defaultdict(list)
_ORDNER = pathlib.Path(__file__).resolve().parent / 'folienpruefung'
for _p in sorted(_ORDNER.glob('*.py')):
    exec(compile(_p.read_text(encoding='utf-8'), str(_p), 'exec'), dict(globals(), F=_p.stem))

# =====================================================================================================================
# Schreiben
# =====================================================================================================================
def _txt(h): return re.sub(r'\s+', ' ', html_.unescape(re.sub(r'<[^>]+>', ' ', h or ''))).strip()
def _norm(h): return _txt(h).casefold()
ANDERS = collections.defaultdict(lambda: collections.defaultdict(list))   # fach -> stelle -> Begriffe, die schon auf der Seite stehen


OFFEN = collections.defaultdict(list)   # fach -> [{t, stelle, begriff, text, fehlt:[…]}]: noch einzuarbeiten (plan/einarbeiten_offen.json)


def einbauen(f, tid, art, eintraege):
    """Nichts einfügen: Die Folienformulierungen werden von Hand in den normalen Text eingearbeitet (werkzeuge/einarbeiten/<fach>.py).
    Hier nur der Stand je Eintrag: Begriffe im ursprünglichen Text → „anders“; erst durch das Einarbeiten (gold, span.nz) → „ergänzt“;
    sonst noch offen (erscheint in den Originalfolien als „fehlt“ und in plan/einarbeiten_offen.json)."""
    weg = json.loads((IN / f / 'ausgeblendet.json').read_text(encoding='utf-8'))['themen'] if (IN / f / 'ausgeblendet.json').exists() else []
    if tid in weg: return art, []   # ausgeblendetes Unterthema (nicht klausurrelevant, wird nicht gebaut): nichts einzuarbeiten
    alt = _norm(re.sub(r'<!--nz-->.*?<!--/nz-->', ' ', art, flags=re.S))
    voll = _norm(art)
    eingebaut = []
    for stelle, begriff, text in eintraege:
        kopf = re.sub(r'\s*\(.*?\)', '', begriff).strip()   # Folientitel: ohne Klammerzusatz; lange Titel und „Titel: Unterpunkt“ zählen nicht als Begriff
        ausser = {x.split(':', 1)[1] for x in GEPRUEFT[f].get(stelle, [])}   # mit ok()/kein() als „anders“/„kein Lernstoff“ vermerkt
        begriffe = [x for x in (_txt(y) for y in ([kopf] if len(kopf.split()) <= 3 and '/' not in kopf and ':' not in kopf else []) + re.findall(r'<b>(.*?)</b>', text)) if x and x not in ausser]
        fehlt = [x for x in begriffe if x.casefold() not in voll]
        if fehlt: OFFEN[f].append(dict(t=tid, stelle=stelle, begriff=begriff, text=_txt(text), fehlt=fehlt)); continue
        if all(x.casefold() in alt for x in begriffe):
            for x in begriffe: ANDERS[f][stelle].append(x)
        else: eingebaut.append(stelle)
    return art, eingebaut


def vor_jetzt_du(art, block):
    """Mathe: Ergänzungen vor „Jetzt du“ einfügen (wie folien_abgleich_ergaenzungen.py), sonst ans Ende"""
    return art.replace('<h3 class="jd-h">', block + '<h3 class="jd-h">', 1) if '<h3 class="jd-h">' in art else art + block


if __name__ == '__main__':
    ERG_ALLE = collections.defaultdict(lambda: collections.defaultdict(list))
    for fach in sorted({f for f, _ in WORT} | {f for f, _ in BLOCK} | {q[0] for q in QUELLE}):
        pf = IN / fach / 'fach.json'; d = json.loads(pf.read_text(encoding='utf-8'))
        T_ = {t['id']: t for k in d['kapitel'] for t in k['themen']}
        for t in T_.values():   # alte Blöcke entfernen (wiederholbar)
            t['article'] = re.sub(r'<!--of:([\w-]+)-->.*?<!--/of:\1-->', '', t['article'], flags=re.S)
        for (f, tid), liste_ in BLOCK.items():
            if f != fach: continue
            for key, html in liste_: T_[tid]['article'] = vor_jetzt_du(T_[tid]['article'], f'<!--of:{key}-->{html}<!--/of:{key}-->')
        for (f, tid), eintraege in WORT.items():
            if f != fach: continue
            T_[tid]['article'], st_ = einbauen(f, tid, T_[tid]['article'], eintraege)
            for x in st_: ERG_ALLE[fach][x].append(tid)
        for f, tid, alt, neu in QUELLE:
            if f == fach and alt in T_[tid].get('src', ''): T_[tid]['src'] = T_[tid]['src'].replace(alt, neu)
        pf.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(fach, 'Lernseiten:', sum(1 for k in WORT if k[0] == fach), 'Wortlaut-Kästen,', sum(len(v) for k, v in BLOCK.items() if k[0] == fach), 'Erklärabschnitte')
    for fach, aus in AUFGABEN.items():
        pa = IN / fach / 'aufgaben.json'; d = json.loads(pa.read_text(encoding='utf-8'))
        d['aufgaben'] = [x for x in d['aufgaben'] if not x['id'].startswith(f'{fach}-of-')] + aus
        pa.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(fach, len(aus), 'Aufgaben (aus dem Probeklausur-Bogen ins Arbeitsblatt)')
    # Stand je Seite für originalfolien.py: geprüfte Begriffe (Grund:Begriff), ergänzte Begriffe, nicht klausurrelevante Seiten
    for fach in sorted(set(GEPRUEFT) | set(NICHT_KLAUSUR) | {f for f, _ in WORT} | {f for f, _ in BLOCK}):
        for st, bs in ANDERS[fach].items(): GEPRUEFT[fach][st] += [f'anders:{b}' for b in bs]
        g = {k: sorted(set(v)) for k, v in sorted(GEPRUEFT[fach].items())}
        erg = ERG_ALLE[fach]
        out = dict(geprueft=g, ergaenzt={k: sorted(set(v)) for k, v in sorted(erg.items())}, nicht_klausur=dict(sorted(NICHT_KLAUSUR[fach].items())))
        (IN / fach / 'plan' / 'einarbeiten_offen.json').write_text(json.dumps(OFFEN[fach], ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        p = IN / fach / 'plan' / 'folien_geprueft.json'
        p.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(fach, len(g), 'Seiten mit geprüften Begriffen,', len(NICHT_KLAUSUR[fach]), 'nicht klausurrelevante Seiten')
