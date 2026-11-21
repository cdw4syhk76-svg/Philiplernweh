"""Je Unterthema: Klausurpunkte aus den Quellen (plan/gp_inventar.json), daraus abgeleitete Klausuraufgaben, übrige Klausuraufgaben.
Aufruf: python3 werkzeuge/klausurbezug.py [ziel.json]   (intern)"""
import sys, json, re, sys, pathlib, html
IN = pathlib.Path(__file__).resolve().parents[1] / 'inhalte'
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from abdeckung import text_von
def txt(s): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s or ''))).strip()
out = []
for fid in ([a for a in sys.argv[1:] if not a.startswith('-') and not a.endswith('.json')] or ['bwl', 'mkt', 'wima', 'mawi', 'ikm', 'igt']):
    lies = lambda n: json.loads((IN / fid / n).read_text(encoding='utf-8'))
    d = lies('fach.json'); fr = lies('fragen.json'); fams = (fr['familien'] if isinstance(fr, dict) else fr) + lies('fragen_neu.json')['familien']
    inv = [P for P in lies('plan/gp_inventar.json')['punkte'] if not P.get('aus')]
    kv = []
    for A in lies('klausur.json')['aufgaben']:
        for T in A['teile']:
            for v in T['varianten']: kv.append((v['unter'], txt(A['titel'] + ' ' + v['text'])))
    auf = lies('aufgaben.json')['aufgaben'] if (IN / fid / 'aufgaben.json').exists() else []
    F = dict(id=fid, kapitel=[], punkte=len(inv))
    for k in d['kapitel']:
        K = dict(name=txt(k.get('title_text') or k['title']), themen=[])
        for t in k['themen']:
            tid = t['id']
            ps = [P for P in inv if tid in P['t']]
            such = re.compile('|'.join(re.escape(s) for P in ps for s in P['such']), re.I) if ps else None
            kl = [a for f in fams if f.get('t') == tid for a in f['a'] if a.get('klausur')]
            kvt = [x for u, x in kv if u == tid]
            gross = [A for A in auf if tid in A['unter'] and (A.get('klausur') or A.get('stufe', 1) >= 3)]
            direkt = (sum(1 for a in kl if such and such.search(text_von(a))) + sum(1 for x in kvt if such and such.search(x))) if ps else 0
            alle = len(kl) + len(kvt) + len(gross)
            K['themen'].append(dict(name=txt(t.get('titel_text') or t['title']), stern=bool(t.get('star')), punkte=[P['text'] for P in ps],
                                    direkt=direkt, stil=alle - direkt, alle=alle, fragen=sum(len(f['a']) for f in fams if f.get('t') == tid)))
        F['kapitel'].append(K)
    out.append(F)
if len(sys.argv) > 1: pathlib.Path(sys.argv[1]).write_text(json.dumps(out, ensure_ascii=False))
for F in out:
    T = [t for K in F['kapitel'] for t in K['themen']]
    mit = [t for t in T if t['punkte']]; ohne = [t for t in T if not t['punkte']]
    print(f"{F['id']}: {F['punkte']} Punkte, Themen {len(T)}, mit Punkt {len(mit)} (direkt {sum(t['direkt'] for t in mit)}, im Stil {sum(t['stil'] for t in mit)}), "
          f"ohne Punkt {len(ohne)}: davon mit Klausurstil-Aufgaben {sum(1 for t in ohne if t['alle'])} ({sum(t['alle'] for t in ohne)} Aufgaben), ganz ohne {sum(1 for t in ohne if not t['alle'])}")
