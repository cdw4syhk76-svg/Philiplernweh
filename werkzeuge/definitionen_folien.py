"""Wichtige Definitionen im Wortlaut der Folien – überall gleich (Lernseite, Fragen, Karteikarte, Glossar).

Jede Definition steht einmal in DEF (je Fach in werkzeuge/definitionen/<fach>.py) mit
  begriff · Unterthema · Folie ('d21/3' = Deck/PDF-Seite) · Folienwortlaut · Kernpunkte (Teilstücke des Wortlauts, die Punkte bringen)
  · anker (Text der Lernseite, in dessen Absatz der Begriff eingeführt wird) · ueberarbeite (bestehende Fragen, die diese Definition abfragen).
Das Skript schreibt daraus:
  1. Lernseite: nichts. Die Kernpunkte stehen im normalen Text (von Hand eingearbeitet, werkzeuge/einarbeiten.py); geprüft wird nur, ob alle da sind.
  2. Fragen: Familie <fach>:<thema>:df-<begriff> mit „Definieren Sie …“ (Erklären, Kernpunkte = Bewertung) und Lückentext aus dem Wortlaut;
     bestehende Varianten aus `ueberarbeite` bekommen denselben Wortlaut (Lücke → Lücke, Erklären → Erklären, sonst die Erklärung).
  3. Karteikarte „<Begriff> (Definition)“ und Glossar-Fenster: Folienwortlaut, dazu „einfach gesagt“.
  5. inhalte/<fach>/definitionen.json: Verzeichnis für die Prüfung beim Bauen (bau.py) – jede Definition muss überall stehen.
Wiederholbar (alte Blöcke <!--df:…--> und Familien „:df-“ werden ersetzt).
Reihenfolge: … → originalfolien_ergaenzungen.py → DIESES SKRIPT → originalfolien.py <fach> → bau.py --test
Aufruf: python3 werkzeuge/definitionen_folien.py [fach …]"""
import sys, json, re, pathlib, importlib, html as _html

ROOT = pathlib.Path(__file__).resolve().parents[1]
IN = ROOT / 'inhalte'
sys.path.insert(0, str(ROOT / 'werkzeuge' / 'definitionen'))
FAECHER = ['bwl', 'mkt', 'wima', 'mawi', 'ikm', 'igt', 'ibl']


def lies(p): return json.loads(p.read_text(encoding='utf-8'))
def schreib(p, d): p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
def txt(h): return re.sub(r'\s+', ' ', _html.unescape(re.sub(r'<[^>]+>', ' ', h or ''))).strip()
def slug(s): return re.sub(r'[^a-z0-9]+', '-', s.lower().replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')).strip('-')[:30]


def fett(wortlaut, kern):
    h = _html.escape(wortlaut, quote=False)
    for k in sorted(kern, key=len, reverse=True):
        h = h.replace(_html.escape(k, quote=False), f'<b>{_html.escape(k, quote=False)}</b>', 1)
    return h


def luecke(wortlaut, kern, n=3):
    """Lückentext: bis zu n Kernpunkte als Lücken (die längsten zuerst nicht – die ersten n in Reihenfolge des Wortlauts)"""
    stellen = sorted([(wortlaut.find(k), k) for k in kern if wortlaut.find(k) >= 0])[:n]
    p, l, pos = '', [], 0
    for i, (at, k) in enumerate(stellen):
        p += _html.escape(wortlaut[pos:at], quote=False) + f'[[{i}]]'; l.append([k, k.lower()] if k.lower() != k else [k]); pos = at + len(k)
    return p + _html.escape(wortlaut[pos:], quote=False), l


def fach_bauen(fach):
    mod = importlib.import_module(fach)
    DEF = mod.DEF
    folien_deck = getattr(mod, 'DECK', {})
    EN = getattr(mod, 'EN', False)
    KL = getattr(mod, 'KLAUSUR', True)   # False: Prüfer fragt Definitionen nicht qualitativ ab – Definitionsfragen nicht als Klausurform   # Klausursprache Englisch (IKM): Fragen englisch
    TX = dict(def_p='Define the term “{}”.', def_w='Points for the key points in bold (from the script); your own words count if every key point is there.', so='As in the script: ', kann='Can define “{}” completely') if EN else \
         dict(def_p='Definieren Sie den Begriff „{}“.', def_w='Punkte bringen die fett gedruckten Kernpunkte der Folie; eigene Worte zählen, wenn alle Kernpunkte enthalten sind.', so='So steht es auf der Folie: ', kann='Kann „{}“ vollständig definieren')
    pf = IN / fach / 'fach.json'; d = lies(pf)
    T = {t['id']: t for k in d['kapitel'] for t in k['themen']}
    kap_von = {t['id']: n + 1 for n, k in enumerate(d['kapitel']) for t in k['themen']}
    fehler = []
    for t in T.values(): t['article'] = re.sub(r'<!--df:([\w-]+)-->.*?<!--/df:\1-->', '', t['article'], flags=re.S)
    verzeichnis = []
    fams = []
    for e in DEF:
        tid, begriff, folie, wort, kern = e['t'], e['begriff'], e['folie'], e['wortlaut'], e['kern']
        assert tid in T, f'{fach}: Unterthema {tid} unbekannt ({begriff})'
        for k in kern: assert k in wort, f'{fach}/{begriff}: Kernpunkt „{k}“ steht nicht wörtlich im Wortlaut'
        dk, n = folie.split('/')
        key = slug(begriff)
        # Lernseite: nichts einfügen. Die Kernpunkte werden von Hand in den normalen Text eingearbeitet (werkzeuge/einarbeiten/<fach>.py,
        # gold für Lernende, die das Unterthema schon kannten); hier wird nur geprüft, ob jeder Kernpunkt auf der Seite steht.
        basis = txt(re.sub(r'<!--(of|df):([\w-]+)-->.*?<!--/\1:\2-->', '', T[tid]['article'], flags=re.S)).casefold()
        offen = [k for k in kern if re.sub(r'\s+', ' ', k).casefold() not in basis]
        stand = 'vollständig' if not offen else 'fehlt: ' + ' · '.join(offen)
        # Fragen
        lp, ll = luecke(wort, kern)
        fams.append(dict(id=f'{fach}:{tid}:df-{key}', f=fach, t=tid, k=kap_von[tid], s=bool(T[tid].get('star')), y='fam', fam=1,
                         z=TX['kann'].format(begriff), a=[
            dict(y='rev', p=TX['def_p'].format(begriff), l=f'<b>{_html.escape(begriff, quote=False)}</b>: {fett(wort, kern)}', pk=kern,
                 w=TX['def_w'], klausur=KL, lvl=3),
            dict(y='luecke', p=f'<b>{_html.escape(begriff, quote=False)}</b>: {lp}', l=ll, w=TX['so'] + fett(wort, kern), klausur=KL, lvl=2)]))
        verzeichnis.append(dict(begriff=begriff, t=tid, folie=folie, wortlaut=wort, kern=kern, lernseite=stand, ueberarbeite=e.get('ueberarbeite', [])))
    if fehler: raise SystemExit(f'{fach}: ' + '\n'.join(fehler))
    schreib(pf, d)

    # Fragen: eigene Familien neu, bestehende Varianten überarbeiten
    pq = IN / fach / 'fragen_neu.json'; fq = lies(pq) if pq.exists() else {'familien': []}
    fq['familien'] = [x for x in fq['familien'] if ':df-' not in x.get('id', '')] + fams
    schreib(pq, fq)
    alle = {}
    for fn in ('fragen.json', 'fragen_neu.json'):
        p = IN / fach / fn
        if p.exists(): alle[fn] = lies(p)
    for e in DEF:
        for fam_id, idx, *art in e.get('ueberarbeite', []):
            art = art[0] if art else 'ersetze'
            v = next((q['a'][idx] for fn in alle for q in alle[fn]['familien'] if q.get('id') == fam_id), None)
            assert v is not None, f'{fach}: Frage {fam_id}#{idx} nicht gefunden'
            v.setdefault('vorher', {k: v.get(k) for k in ('p', 'l', 'pk', 'w') if k in v})   # ursprüngliche Fassung bleibt erhalten
            alt = v['vorher']
            if art == 'ergaenze' and v['y'] == 'rev':   # Frage verlangt mehr als die Definition: Definition vorn ergänzen, Rest bleibt
                v.update(l=f'<b>{_html.escape(e["begriff"], quote=False)}</b>: {fett(e["wortlaut"], e["kern"])}<br>{alt.get("l", "")}', pk=list(e['kern']) + [x for x in (alt.get('pk') or []) if x not in e['kern']])
            elif v['y'] == 'luecke':
                lp, ll = luecke(e['wortlaut'], e['kern']); v.update(p=f'<b>{_html.escape(e["begriff"], quote=False)}</b>: {lp}', l=ll)
            elif v['y'] == 'rev':
                v.update(l=f'<b>{_html.escape(e["begriff"], quote=False)}</b>: {fett(e["wortlaut"], e["kern"])}', pk=e['kern'])
            v['w'] = TX['so'] + fett(e["wortlaut"], e["kern"]) + (f' {alt["w"]}' if art == 'ergaenze' and alt.get('w') else '')
    for fn, dd in alle.items():
        if fn == 'fragen_neu.json': dd['familien'] = [x for x in dd['familien'] if ':df-' not in x.get('id', '')] + fams
        schreib(IN / fach / fn, dd)

    # Karteikarten
    pk = IN / fach / 'karten.json'; ka = lies(pk)
    ka['karten'] = [c for c in ka['karten'] if not c.get('df')]
    for e in DEF:
        for c in ka['karten']:
            if txt(c['v']).casefold() in (e['begriff'].casefold(), f"{e['begriff']}: definition".casefold(), f"{e['begriff']} (definition)".casefold()):
                c.setdefault('vorher', c['r']); c['r'] = e['wortlaut']
        if not any(txt(c['v']).casefold().startswith(e['begriff'].casefold()) and c['r'] == e['wortlaut'] for c in ka['karten']):
            ka['karten'].append(dict(t=e['t'], v=f"{e['begriff']} (Definition)", r=e['wortlaut'], df=1, kr=1))
    schreib(pk, ka)

    # Glossar
    pg = IN / fach / 'glossar.json'; gl = lies(pg)
    for e in DEF:
        g = next((x for x in gl['begriffe'] if x['begriff'].casefold() == e['begriff'].casefold()), None)
        if g is None:
            gl['begriffe'].append(dict(begriff=e['begriff'], muster=re.escape(e['begriff'].split(' (')[0]), heimat=e['t'], text=e['wortlaut'], df=1))
        else:
            g.setdefault('einfach', g['text'])
            g['text'] = f"{e['wortlaut']} <i>Einfach gesagt:</i> {g['einfach']}" if g['einfach'] != e['wortlaut'] else e['wortlaut']
    schreib(pg, gl)

    schreib(IN / fach / 'definitionen.json', {'hinweis': 'erzeugt von werkzeuge/definitionen_folien.py; Prüfung in bau.py', 'definitionen': verzeichnis})
    print(f'{fach}: {len(DEF)} Definitionen · Lernseite, {len(fams)} Fragen-Familien, Karten, Glossar · überarbeitet: {sum(len(e.get("ueberarbeite", [])) for e in DEF)} Fragen')


def kandidaten(fach, begriff, tid):
    """Bestehende Fragen, die diese Definition abfragen könnten (für die Auswahl von `ueberarbeite`)"""
    out = []
    for fn in ('fragen.json', 'fragen_neu.json'):
        p = IN / fach / fn
        if not p.exists(): continue
        for q in lies(p)['familien']:
            if q.get('t') != tid or ':df-' in q.get('id', ''): continue
            for i, v in enumerate(q['a']):
                s = txt(v.get('p', ''))
                if re.search(re.escape(begriff), s, re.I) and re.search(r'Definier|versteht man|Was ist|ist ein|ist eine|heißt|bezeichnet|\[\[', s):
                    out.append((q['id'], i, v['y'], s[:110]))
    return out


if __name__ == '__main__':
    arg = [a for a in sys.argv[1:] if not a.startswith('--')]
    if '--kandidaten' in sys.argv:
        for fach in arg:
            mod = importlib.import_module(fach)
            for e in mod.DEF:
                for k in kandidaten(fach, e['begriff'], e['t']): print(fach, e['begriff'], '|', k)
    else:
        for fach in arg or FAECHER:
            if (ROOT / 'werkzeuge' / 'definitionen' / f'{fach}.py').exists(): fach_bauen(fach)
