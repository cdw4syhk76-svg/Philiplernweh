"""„Finde den Fehler“: Die Option „Stimmt so / Richtig / Kein Fehler“ war fast nie richtig und damit erratbar.
Sie wird entfernt (die Aufgabe sagt ja, dass es einen Fehler gibt); es bleiben die echten Korrekturen. Wiederholbar.
Aufruf: python3 werkzeuge/fehler_fix.py"""
import sys, json, re, html, pathlib
IN = pathlib.Path(__file__).resolve().parents[1] / 'inhalte'
def txt(s): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s or ''))).strip()
STIMMT = re.compile(r'^(Stimmt|Richtig\b|Kein Fehler|Correct|The statement is correct|Nichts fehlt|Nichts\b)', re.I)
for fid in ([a for a in sys.argv[1:] if not a.startswith('-') and not a.endswith('.json')] or ['bwl', 'mkt', 'wima', 'mawi', 'ikm', 'igt']):
    n = 0
    for datei in ('fragen.json', 'fragen_neu.json'):
        q = IN / fid / datei; d = json.loads(q.read_text(encoding='utf-8')); fams = d['familien'] if isinstance(d, dict) else d
        for f in fams:
            for a in f['a']:
                if a['y'] != 'mc' or not re.search(r'Finde den Fehler|Find the (error|mistake)', a['p'], re.I): continue
                weg = [o for o in a['o'] if not o[1] and STIMMT.match(txt(o[0]))]
                if weg and len(a['o']) - len(weg) >= 3:
                    a['o'] = [o for o in a['o'] if o not in weg]; n += 1
        q.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(fid, n, 'Fragen ohne „Stimmt so“')
