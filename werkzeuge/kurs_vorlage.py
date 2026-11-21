"""Neuer Kurs: die alten Fächer (DBM26A) aus dem Bau nehmen und als Muster ablegen.
Erst aufrufen, wenn mindestens ein eigenes Fach in inhalte/faecher.json steht und baut (python3 bau.py).
Logistik & MaWi bleibt danach unter muster/ als Vorbild zum Nachschauen (Inhalt, Schaubilder, Fragen, Aufgaben, Klausurbogen).
Aufruf: python3 werkzeuge/kurs_vorlage.py --alte-faecher-weg"""
import json, pathlib, shutil, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
IN, MU = ROOT / 'inhalte', ROOT / 'muster'
ALT = ['abwl', 'marketing', 'logistik', 'produktion', 'mathe']
ALT_WERKZEUGE = ['abwl_klausur.py', 'marketing_klausur.py', 'logistik_klausur.py', 'mathe_klausur.py', 'mathe_zufall.py', 'mathe_aufgaben2.py',
                 'klausurfragen.py', 'gp_ergaenzungen.py', 'gp_fragen.py', 'spiele.py', 'aufgaben_extra.py', 'karten_extra.py',
                 'karten_begriffe.py', 'karten_begriffe_daten.json', 'folien_ergaenzungen.py', 'klausurthemen_check.py', 'import_alt.py', 'produktion']

if '--alte-faecher-weg' not in sys.argv:
    sys.exit(__doc__)
reg = json.loads((IN / 'faecher.json').read_text(encoding='utf-8'))
eigene = [f['id'] for f in reg['faecher'] if f['id'] not in ALT]
if not eigene:
    sys.exit('Noch kein eigenes Fach in inhalte/faecher.json. Erst ein Fach anlegen (docs/KURS-NEU.md, Schritt 2), dann dieses Skript.')
(MU / 'inhalte').mkdir(parents=True, exist_ok=True); (MU / 'werkzeuge').mkdir(parents=True, exist_ok=True)
for f in ALT:
    if (IN / f).exists():
        shutil.move(str(IN / f), str(MU / 'inhalte' / f))
for w in ALT_WERKZEUGE:
    if (ROOT / 'werkzeuge' / w).exists():
        shutil.move(str(ROOT / 'werkzeuge' / w), str(MU / 'werkzeuge' / w))
reg['faecher'] = [f for f in reg['faecher'] if f['id'] not in ALT]
(IN / 'faecher.json').write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
st = json.loads((IN / 'studium.json').read_text(encoding='utf-8'))
st['klausuren'] = [k for k in st['klausuren'] if not set(k.get('faecher', [])) & set(ALT)]
st['module'] = [m for m in st['module'] if not any(t[2] in ALT for t in m.get('teile', []) if len(t) > 2)]
(IN / 'studium.json').write_text(json.dumps(st, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(IN / 'umbenannt.json').write_text('{}\n', encoding='utf-8')
print(f'Alte Fächer nach muster/ verschoben. Im Bau bleiben: {", ".join(eigene)}.')
print('Jetzt die Tests auf eigene Fächer umstellen (docs/KURS-NEU.md, Abschnitt „Tests“): tests/t_klick.js, tests/t_engine.js, tests/t_online.mjs.')
