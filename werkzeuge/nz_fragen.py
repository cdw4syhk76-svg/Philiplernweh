"""Fragen zum eingearbeiteten Folienstoff: ersetzt die automatisch erzeugten Lückentexte (Familien „:nz-“, werkzeuge/einarbeiten.py)
durch ausformulierte Fragen aus werkzeuge/nz_fragen/<fach>.py (FR = {'<kurz>': [Varianten …]}).
Die Familien-ID bleibt gleich (Schlüssel im Lernstand); nur die Varianten werden ersetzt. Familien ohne Eintrag bleiben unverändert.
Wiederholbar; läuft am Ende von einarbeiten.py automatisch mit.
Aufruf: python3 werkzeuge/nz_fragen.py [fach …]"""
import sys, json, pathlib, importlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
IN = ROOT / 'inhalte'
sys.path.insert(0, str(ROOT / 'werkzeuge' / 'nz_fragen'))


def fach(fid):
    if not (ROOT / 'werkzeuge' / 'nz_fragen' / f'{fid}.py').exists(): return   # (werkzeuge/<fach>/ sind Ordner gleichen Namens)
    mod = importlib.import_module(fid)
    from anwendung import UEBER   # Familien, die sonst eine Folien-Definition doppelt abfragen würden: Anwendung statt Definition
    FR = {**mod.FR, **UEBER.get(fid, {})}
    p = IN / fid / 'fragen_neu.json'; d = json.loads(p.read_text(encoding='utf-8'))
    da, fehlt = set(), []
    for x in d['familien']:
        if ':nz-' not in x.get('id', ''): continue
        k = x['id'].split(':nz-')[1]
        if k in FR:
            x['a'] = FR[k]; x['z'] = 'Versteht den ergänzten Stoff'; da.add(k)
        else: fehlt.append(k)
    unbekannt = sorted(set(FR) - da)
    assert not unbekannt, f'{fid}: unbekannte Kennungen {unbekannt}'
    p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f'{fid}: {len(da)} Familien ausformuliert' + (f', noch als Lückentext: {len(fehlt)} ({", ".join(fehlt[:8])}…)' if fehlt else ''))


if __name__ == '__main__':
    for f in sys.argv[1:] or ['bwl', 'mkt', 'wima', 'mawi', 'ikm', 'igt', 'ibl']: fach(f)
