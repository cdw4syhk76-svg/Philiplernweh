"""Baut ein Fach aus seinen Kapitel-Skripten: werkzeuge/<fach>/k1.py, k2.py, … (je eine Variable KAPITEL, siehe bausteine_de.kapitel)
und optional werkzeuge/<fach>/k1_figuren.js … (Schaubild-Skripte, laufen nach jedem Seitenwechsel).
Schreibt inhalte/<fach>/fach.json (alle Kapitel in Reihenfolge) und inhalte/<fach>/figuren.js. Wiederholbar.
Aufruf: python3 werkzeuge/fachbau/bauen.py <fach-id>"""
import importlib.util, json, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
fid = sys.argv[1] if len(sys.argv) > 1 else sys.exit('Aufruf: python3 werkzeuge/fachbau/bauen.py <fach-id>')
QUELLE, ZIEL = ROOT / 'werkzeuge' / fid, ROOT / 'inhalte' / fid
sys.path[:0] = [str(QUELLE), str(ROOT / 'werkzeuge' / 'fachbau')]
skripte = sorted(QUELLE.glob('k[0-9]*.py'), key=lambda p: int(re.match(r'k(\d+)', p.stem).group(1)))
skripte = [p for p in skripte if re.fullmatch(r'k\d+', p.stem)]   # k1.py, k2.py …; Hilfsdateien wie k1_bilder.py werden von dort importiert
if not skripte: sys.exit(f'keine Kapitel-Skripte in {QUELLE} (k1.py, k2.py …)')
kapitel = []
for p in skripte:
    spec = importlib.util.spec_from_file_location(p.stem, p); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    kapitel.append(m.KAPITEL)
ids = [t['id'] for k in kapitel for t in k['themen']]
assert len(ids) == len(set(ids)), f'doppelte Unterthemen-IDs: {[i for i in ids if ids.count(i) > 1]}'
ZIEL.mkdir(parents=True, exist_ok=True)
# Begriffs-Check: ergänzte Fachbegriffe (werkzeuge/<fach>/begriffe_ergaenzt.py), die im Text des Unterthemas noch nicht vorkommen,
# erscheinen am Ende des Unterthemas als „Weitere Begriffe“ – so steht jeder Begriff der Unterlagen erklärt auf der Lernseite.
_bp = QUELLE / 'begriffe_ergaenzt.py'
if _bp.exists():
    _spec = importlib.util.spec_from_file_location('begriffe_ergaenzt', _bp); _m = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_m)
    _zw = (QUELLE / 'z.py').exists() or fid in ('ikm', 'ling')
    for _k in kapitel:
        for _t in _k['themen']:
            _txt = re.sub(r'<[^>]+>', ' ', json.dumps(_t, ensure_ascii=False))
            _fehlt = [g for g in _m.B if g[2] == _t['id'] and not re.search(g[1], _txt)]
            if not _fehlt: continue
            if _zw:
                _kopf = '<div class="zw2"><div class="l-en" lang="en"><h3>Further terms</h3></div><div class="l-de" lang="de"><h3>Weitere Begriffe</h3></div></div>'
            else:
                _kopf = '<h3>Weitere Begriffe</h3>'
            _t['article'] += _kopf + '<div class="tbl-scroll"><table class="t">' + ''.join(f'<tr><td class=rowh><b>{g[0]}</b></td><td>{g[3]}</td></tr>' for g in _fehlt) + '</table></div>'
# Überlagerung (werkzeuge/<fach>/ausgrenzung.py, A = {unterthema: {feld: wert}}): Prüfungsausgrenzung und angepasste Texte nach dem Bau
_ap = QUELLE / 'ausgrenzung.py'
if _ap.exists():
    _spec = importlib.util.spec_from_file_location('ausgrenzung', _ap); _m = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_m)
    _alle = {t['id']: t for k in kapitel for t in k['themen']}
    for _id, _f in _m.A.items():
        assert _id in _alle, f'ausgrenzung.py: Unterthema {_id} unbekannt'
        _alle[_id].update(_f)
# Weitere Schaubilder und Hinweise (werkzeuge/<fach>/schaubilder.py, Z = {unterthema: [(anker, html)]}): anker = <h3>-Text (davor), '^' = Anfang, None = Ende
_sp = QUELLE / 'schaubilder.py'
if _sp.exists():
    _spec = importlib.util.spec_from_file_location('schaubilder', _sp); _m = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_m)
    _alle = {t['id']: t for k in kapitel for t in k['themen']}
    for _id, _liste in _m.Z.items():
        assert _id in _alle, f'schaubilder.py: Unterthema {_id} unbekannt'
        for _anker, _html in _liste:
            _a = _alle[_id]['article']
            if _anker == 'FIG': _alle[_id].update(fig=_html[0], figcap=_html[1]); continue
            if _anker == '^': _alle[_id]['article'] = _html + _a
            elif _anker is None: _alle[_id]['article'] = _a + _html
            else:
                _pos = _a.find(f'<h3>{_anker}</h3>')
                assert _pos >= 0, f'schaubilder.py: Überschrift „{_anker}“ fehlt in {_id}'
                _alle[_id]['article'] = _a[:_pos] + _html + _a[_pos:]
(ZIEL / 'fach.json').write_text(json.dumps({'kapitel': kapitel}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
js = ['/* Schaubild-Skripte (aus werkzeuge/%s/k*_figuren.js zusammengesetzt; nicht hier bearbeiten) */' % fid]
for p in sorted(QUELLE.glob('k*_figuren.js'), key=lambda p: int(re.match(r'k(\d+)', p.stem).group(1))):
    js.append(p.read_text(encoding='utf-8').strip())
(ZIEL / 'figuren.js').write_text('\n\n'.join(js) + '\n', encoding='utf-8')
print(f'{fid}: {len(kapitel)} Oberthemen, {len(ids)} Unterthemen → {ZIEL / "fach.json"}')
