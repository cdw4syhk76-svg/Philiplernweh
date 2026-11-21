"""Arbeitsliste zum Einarbeiten: je Unterthema, was noch fehlt (Definitionen: fehlende Kernpunkte; Folienformulierungen: fehlende Begriffe),
dazu der Aufbau der Lernseite (Zwischenüberschriften, Absatzanfänge), um die passende Stelle zu finden.
Aufruf: python3 werkzeuge/einarbeiten_liste.py <fach> [unterthema …]"""
import sys, json, re, pathlib, html
IN = pathlib.Path(__file__).resolve().parents[1] / 'inhalte'
fach, nur = sys.argv[1], set(sys.argv[2:])
d = json.loads((IN / fach / 'fach.json').read_text()); T = {t['id']: t for k in d['kapitel'] for t in k['themen']}
offen = json.loads((IN / fach / 'plan' / 'einarbeiten_offen.json').read_text())
defs = json.loads((IN / fach / 'definitionen.json').read_text())['definitionen']
txt = lambda h: re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', h))).strip()
for tid, t in T.items():
    if nur and tid not in nur: continue
    o = [x for x in offen if x['t'] == tid]; df = [x for x in defs if x['t'] == tid and x['lernseite'] != 'vollständig']
    if not o and not df: continue
    print(f'\n######## {tid} · {txt(t.get("titel_text", ""))}')
    for x in df: print(f'  DEF {x["begriff"]} ({x["folie"]}): {x["wortlaut"]}\n      FEHLT: {x["lernseite"][7:]}')
    for x in o: print(f'  FOLIE {x["stelle"]} {x["begriff"]}: {x["text"][:400]}\n      FEHLT: {" · ".join(x["fehlt"])}')
    if '-v' in sys.argv or nur:
        for m in re.finditer(r'<(h3|p|li)[^>]*>(.*?)</\1>', t['article'], flags=re.S):
            print(f'    [{m.group(1)}] {txt(m.group(2))[:160]}')
