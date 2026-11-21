"""Zählt je Fach → Oberthema → Unterthema, wie viele Fragen in welchem Werkzeug verfügbar sind (Logik wie in app/js/kern.js).
Aufruf: python3 werkzeuge/uebersicht.py [ziel.json]"""
import sys, json, re, sys, html, pathlib
IN = pathlib.Path(__file__).resolve().parents[1] / 'inhalte'
def txt(s): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s or ''))).strip()
ENDLOS = {'mc', 'mc_multi', 'block', 'zuord', 'reihe', 'beschr', 'hot', 'kurz', 'luecke', 'liste', 'num'}
KREATIV = {'zuord', 'reihe', 'beschr', 'hot', 'luecke'}
EINFACH = {'liste', 'kurz', 'num', 'luecke', 'beschr', 'mc_multi', 'block'}
reg = {f['id']: f for f in json.loads((IN / 'faecher.json').read_text())['faecher']}
out = []
for fid in ([a for a in sys.argv[1:] if not a.startswith('-') and not a.endswith('.json')] or ['bwl', 'mkt', 'wima', 'mawi', 'ikm', 'igt']):
    lies = lambda n: json.loads((IN / fid / n).read_text(encoding='utf-8'))
    d = lies('fach.json'); fr = lies('fragen.json'); fams = fr['familien'] if isinstance(fr, dict) else fr
    if (IN / fid / 'fragen_neu.json').exists(): fams += lies('fragen_neu.json')['familien']
    gl = lies('glossar.json')['begriffe']; ka = lies('karten.json')['karten'] if (IN / fid / 'karten.json').exists() else []
    auf = lies('aufgaben.json')['aufgaben'] if (IN / fid / 'aufgaben.json').exists() else []
    kv = {}
    if (IN / fid / 'klausur.json').exists():
        for A in lies('klausur.json')['aufgaben']:
            for T in A['teile']:
                for v in T['varianten']: kv[v['unter']] = kv.get(v['unter'], 0) + 1
    tiefe = reg[fid].get('tiefe', 3)
    F = dict(id=fid, name=reg[fid]['name'], tiefe=tiefe, kapitel=[])
    for k in d['kapitel']:
        K = dict(name=txt(k.get('title_text') or k['title']), themen=[])
        for t in k['themen']:
            tid = t['id']; vs = [a for f in fams if f.get('t') == tid for a in f['a']]
            karten = [g for g in gl if g.get('heimat') == tid] + [c for c in ka if c['t'] == tid]
            drillk = [c for c in karten if c.get('kr') or tiefe >= 3 or (tiefe >= 2 and t.get('star'))] or karten
            z = dict(
                name=txt(t.get('titel_text') or t['title']), stern=bool(t.get('star')),
                endlos=sum(a['y'] in ENDLOS for a in vs),
                kreativ=sum(a['y'] in KREATIV for a in vs),
                drill1=len(drillk) + sum(a['y'] in ('luecke', 'kurz') for a in vs),
                drill2=len(drillk) + sum(a['y'] == 'rev' for a in vs),
                karten=len(karten),
                einfach=sum(bool(a.get('klausur') and a['y'] in EINFACH) for a in vs) + sum(1 for A in auf if tid in A['unter'] and A.get('stufe', 1) <= 2),
                klausur=sum(bool(a.get('klausur')) for a in vs) + sum(1 for A in auf if tid in A['unter'] and (A.get('klausur') or A.get('stufe', 1) >= 3)) + kv.get(tid, 0),
                probe=kv.get(tid, 0), alle=len(vs))
            K['themen'].append(z)
        F['kapitel'].append(K)
    out.append(F)
ziel = next((a for a in sys.argv[1:] if a.endswith('.json')), '/dev/stdout')
pathlib.Path(ziel).write_text(json.dumps(out, ensure_ascii=False))
for F in out:
    s = lambda key: sum(t[key] for K in F['kapitel'] for t in K['themen'])
    print(F['name'], {k: s(k) for k in ['alle', 'endlos', 'kreativ', 'drill1', 'drill2', 'karten', 'einfach', 'klausur', 'probe']}, file=sys.stderr)
