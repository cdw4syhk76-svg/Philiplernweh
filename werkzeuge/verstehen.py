"""Von Hand geschriebene Verständnisfragen je Fach (Daten in werkzeuge/verstehen/<fach>.py, Dict Unterthema[#Zusatz] → Fragen).
Familien „:vs-verstehen…“ / „:vs-klausur…“ → inhalte/<fach>/fragen_neu.json. Familien zu Unterthemen eines wichtigen Punkts
(plan/gp_inventar.json) bekommen punkt=… für die Leiter. Wiederholbar. Aufruf: python3 werkzeuge/verstehen.py [fach …]"""
import json, pathlib, sys, importlib
W = pathlib.Path(__file__).parent; IN = W.parent / 'inhalte'
sys.path.insert(0, str(W / 'verstehen'))
FAECHER = ['bwl', 'mkt', 'wima', 'mawi', 'ikm', 'igt']


def main():
    for fid in ([a for a in sys.argv[1:]] or FAECHER):
        if not (W / 'verstehen' / f'{fid}.py').exists(): continue
        d = importlib.import_module(fid).FRAGEN
        fach = json.loads((IN / fid / 'fach.json').read_text(encoding='utf-8'))
        kn = {t['id']: i for i, k in enumerate(fach['kapitel'], 1) for t in k['themen']}
        inv = json.loads((IN / fid / 'plan' / 'gp_inventar.json').read_text(encoding='utf-8'))['punkte']
        punkt = {t: P['id'] for P in inv if P.get('j', 0) >= 1 for t in P['t']}
        en = fach.get('englisch') or fid == 'ikm'
        p = IN / fid / 'fragen_neu.json'; neu = json.loads(p.read_text(encoding='utf-8'))
        neu['familien'] = [x for x in neu['familien'] if ':vs-' not in x.get('id', '')]
        for schl, a in d.items():
            tid, _, suf = schl.partition('#'); suf = '-' + suf if suf else ''
            assert tid in kn, (fid, tid)
            extra = dict(punkt=punkt[tid]) if tid in punkt else {}
            ver = [x for x in a if not x.get('klausur')]; kl = [x for x in a if x.get('klausur')]
            if ver: neu['familien'].append(dict(id=f'{fid}:{tid}:vs-verstehen{suf}', f=fid, t=tid, k=kn[tid], s=False, y='fam', fam=1,
                                                z='Understands the connections of the topic' if en else 'Versteht die Zusammenhänge des Unterthemas', a=ver, **extra))
            if kl: neu['familien'].append(dict(id=f'{fid}:{tid}:vs-klausur{suf}', f=fid, t=tid, k=kn[tid], s=False, y='fam', fam=1,
                                               z='Can answer in exam form' if en else 'Kann in Klausurform antworten', a=kl, **extra))
        p.write_text(json.dumps(neu, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(fid, sum(len(a) for a in d.values()), 'Fragen von Hand')


if __name__ == '__main__':
    main()
