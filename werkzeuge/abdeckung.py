"""Abdeckungsbericht (intern): Steckt jeder Punkt aus inhalte/<fach>/plan/gp_inventar.json in jedem Werkzeug?
Spalten: Klausurniveau (klausur-markierte Fragen + Probeklausur-Varianten) · Einfach (einfache Klausurfragen: Nennen, Lücke, Rechnen)
· Endlos kreativ (Zuordnen, Reihenfolge, Lücke, Beschriften, Antippen, kurze Auswahl) · Drill (klausurrelevante Karten, Lücke, Kurzantwort)
Schreibt inhalte/<fach>/plan/abdeckung.md und gibt die Lücken aus. Aufruf: python3 werkzeuge/abdeckung.py [fach]"""
import sys, json, re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from merklisten import IN, txt

KREATIV = {'zuord', 'reihe', 'luecke', 'beschr', 'hot', 'mc', 'mc_multi', 'block'}


def text_von(a):
    t = [a.get('p', ''), a.get('w', ''), str(a.get('l', '')), ' '.join(map(str, a.get('k', []))), json.dumps(a.get('o', ''), ensure_ascii=False),
         json.dumps(a.get('pk', ''), ensure_ascii=False), ' '.join(map(str, a.get('slots', [])))]
    return txt(' '.join(t))


def fach(fid):
    p = IN / fid / 'plan' / 'gp_inventar.json'
    if not p.exists(): return
    inv = json.loads(p.read_text(encoding='utf-8'))['punkte']
    fr = json.loads((IN / fid / 'fragen.json').read_text(encoding='utf-8'))
    fams = (fr['familien'] if isinstance(fr, dict) else fr)
    if (IN / fid / 'fragen_neu.json').exists(): fams += json.loads((IN / fid / 'fragen_neu.json').read_text(encoding='utf-8'))['familien']
    karten = json.loads((IN / fid / 'karten.json').read_text(encoding='utf-8'))['karten'] if (IN / fid / 'karten.json').exists() else []
    kv = []
    if (IN / fid / 'klausur.json').exists():
        for A in json.loads((IN / fid / 'klausur.json').read_text(encoding='utf-8'))['aufgaben']:
            for T in A['teile']:
                for v in T['varianten']: kv.append((v['unter'], txt(A['titel'] + ' ' + v['text'])))
    zeilen, luecken = [], []
    for P in inv:
        if P.get('aus'): zeilen.append(f"| {P['id']} | {P['text']} | – | – | – | – | {P['aus']} |"); continue
        such = re.compile('|'.join(re.escape(s) for s in P['such']), re.I)
        ts = set(P['t'])
        qs = [(f, a) for f in fams for a in f['a'] if f.get('t') in ts and such.search(text_von(a) + ' ' + f.get('z', ''))]
        z = dict(
            klausur=sum(1 for _, a in qs if a.get('klausur')) + sum(1 for u, t in kv if u in ts and such.search(t)),
            einfach=sum(1 for _, a in qs if a.get('klausur') and a['y'] in ('liste', 'kurz', 'num', 'luecke', 'beschr', 'mc_multi', 'block')),
            kreativ=sum(1 for _, a in qs if (a['y'] in KREATIV or (P['art'] == 'rechnen' and a['y'] == 'num')) and not a.get('klausur')),
            drill=sum(1 for c in karten if c['t'] in ts and (c.get('kr') or c.get('b')) and such.search(txt(c['v'] + ' ' + c['r']))) + sum(1 for _, a in qs if a['y'] in ('luecke', 'kurz')),
        )
        fehlt = [k for k, v in z.items() if v == 0]
        if P['art'] == 'rechnen' and 'drill' in fehlt: fehlt.remove('drill')   # Rechenaufgaben brauchen keine Definitionen
        zeilen.append(f"| {P['id']} | {P['text']} | {z['klausur']} | {z['einfach']} | {z['kreativ']} | {z['drill']} | {', '.join(fehlt) or 'ok'} |")
        if fehlt: luecken.append(f"{fid}/{P['id']}: fehlt {', '.join(fehlt)}  ({z})")
    (IN / fid / 'plan' / 'abdeckung.md').write_text(
        f"# Abdeckung {fid} (intern, erzeugt von werkzeuge/abdeckung.py)\n\n| Punkt | verlangt | Klausurniveau | Einfach | Endlos kreativ | Drill | Lücke |\n|---|---|---|---|---|---|---|\n"
        + '\n'.join(zeilen) + '\n', encoding='utf-8')
    print(f'{fid}: {len(inv)} Punkte, {len(luecken)} mit Lücken')
    for l in luecken: print('  ', l)


if __name__ == '__main__':
    for f in (sys.argv[1:] or ['bwl', 'mkt', 'wima', 'mawi', 'ikm', 'igt']): fach(f)
