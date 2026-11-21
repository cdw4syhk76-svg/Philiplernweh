"""Lange Auswahlantworten durch kurze ersetzen (Liste je Fach in werkzeuge/mc_kurz/<fach>.json: "familien-id#index": [Optionen in derselben Reihenfolge]).
Die alte, ausführliche richtige Antwort wird zur Erklärung (w), damit nichts verloren geht. Wiederholbar (schon gekürzte werden übersprungen).
Aufruf: python3 werkzeuge/mc_kuerzen.py"""
import json, pathlib, re, html
W = pathlib.Path(__file__).parent; IN = W.parent / 'inhalte'
def txt(s): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s or ''))).strip()
for p in sorted((W / 'mc_kurz').glob('*.json')):
    fid = p.stem; neu = json.loads(p.read_text(encoding='utf-8'))
    n = 0
    for datei in ('fragen.json', 'fragen_neu.json'):
        q = IN / fid / datei
        d = json.loads(q.read_text(encoding='utf-8')); fams = d['familien'] if isinstance(d, dict) else d
        for f in fams:
            for i, a in enumerate(f.get('a', [])):
                k = f"{f.get('id')}#{i}"
                if k not in neu or a['y'] != 'mc' or a.get('kurz'): continue
                o = neu[k]; assert len(o) == len(a['o']), k
                alt = next(txt(x[0]) for x in a['o'] if x[1])
                if alt not in txt(a.get('w', '')): a['w'] = (alt + ('<br>' + a['w'] if a.get('w') else ''))
                a['o'] = [[o[j], x[1]] for j, x in enumerate(a['o'])]; a['kurz'] = 1; n += 1
        q.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(fid, n, 'gekürzt')
