"""Prüfbericht Zielgrößen je Unterthema (intern):
  ohne wichtigen Punkt: >= 8 Verständnisfragen, >= 3 Aufgaben im Klausurstil
  mit wichtigem Punkt: je Punkt >= 8 Verständnisfragen, Leiter: Stufe 0 (erkennen) >= 2, Stufe 1 (verstehen) >= 2, Klausurform >= 2
Schreibt inhalte/<fach>/plan/zielgroessen.md. Aufruf: python3 werkzeuge/zielgroessen.py [fach] [--kurz]"""
import sys, json, sys, pathlib, re, html, hashlib
IN = pathlib.Path(__file__).resolve().parents[1] / 'inhalte'
ENDLOS = {'mc', 'mc_multi', 'block', 'zuord', 'reihe', 'beschr', 'hot', 'kurz', 'luecke', 'liste', 'num'}
def txt(s): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s or ''))).strip()
btxt = lambda s: re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s or '')).replace('&amp;', '&').replace('&nbsp;', ' ').strip()


def fach(fid, kurz=False):
    lies = lambda n: json.loads((IN / fid / n).read_text(encoding='utf-8'))
    d = lies('fach.json'); fr = lies('fragen.json'); fams = (fr['familien'] if isinstance(fr, dict) else fr) + lies('fragen_neu.json')['familien']
    for q in fams: q.setdefault('id', f"{fid}:{q['t']}:" + hashlib.sha1(btxt(q['a'][0].get('p', '')).encode()).hexdigest()[:8])
    wi = lies('wichtig.json'); kv = {}
    for A in lies('klausur.json')['aufgaben']:
        for T in A['teile']:
            for v in T['varianten']: kv[v['unter']] = kv.get(v['unter'], 0) + 1
    auf = lies('aufgaben.json')['aufgaben'] if (IN / fid / 'aufgaben.json').exists() else []
    zeilen, fehl = [], 0
    for k in d['kapitel']:
        for t in k['themen']:
            if t.get('aus'): continue   # ausgegraut („kommt nicht dran“): keine Fragen, keine Lücke
            tid = t['id']; F = [f for f in fams if f.get('t') == tid]
            ver = sum(1 for f in F for a in f['a'] if not a.get('klausur'))
            kl = sum(1 for f in F for a in f['a'] if a.get('klausur')) + kv.get(tid, 0) + sum(1 for A in auf if tid in A['unter'] and A.get('klausur'))
            luecke = []
            if kl < (1 if 'nicht klausurrelevant' in txt(t.get('titel_text') or t['title']) else 3): luecke.append(f'Klausurstil {kl}/3')
            if ver < 8: luecke.append(f'Verstehen {ver}/8')
            fehl += bool(luecke)
            zeilen.append(f"| {txt(k.get('title_text') or k['title'])[:30]} | {txt(t.get('titel_text') or t['title'])[:45]} | {ver} | {kl} | {'; '.join(luecke) or 'ok'} |")
    # Leiter je wichtigem Punkt (über alle Unterthemen des Punkts)
    punkte = sorted(set(wi['familien'].values()))
    for p in punkte:
        P = [f for f in fams if wi['familien'].get(f.get('id')) == p]
        s0 = sum(1 for f in P for a in f['a'] if not a.get('klausur') and (a.get('lvl') or 1) <= 1 and a['y'] in ENDLOS)
        s1 = sum(1 for f in P for a in f['a'] if not a.get('klausur') and (a.get('lvl') or 1) >= 2 and a['y'] in ENDLOS)
        s2 = sum(1 for f in P for a in f['a'] if a.get('klausur') and a['y'] in ENDLOS)
        v = sum(1 for f in P for a in f['a'] if not a.get('klausur'))
        ok = s0 >= 2 and s1 >= 2 and s2 >= 2 and v >= 8
        fehl += not ok
        zeilen.append(f"| ★ Leiter | {p} | {v} | {s2} | {'ok' if ok else f'erkennen {s0}/2, verstehen {s1}/2, Klausurform {s2}/2, Verständnis gesamt {v}/8'} |")
    (IN / fid / 'plan' / 'zielgroessen.md').write_text(f"# Zielgrößen {fid} (intern)\n\n| Oberthema | Unterthema | Verstehen | Klausurstil | offen |\n|---|---|---|---|---|\n" + '\n'.join(zeilen) + '\n', encoding='utf-8')
    print(f'{fid}: {len(zeilen)} Unterthemen, {fehl} mit Lücken')
    if not kurz: print('\n'.join(z for z in zeilen if not z.endswith('| ok |')))


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    for f in (args or ['bwl', 'mkt', 'wima', 'mawi', 'ikm', 'igt']): fach(f, '--kurz' in sys.argv)
