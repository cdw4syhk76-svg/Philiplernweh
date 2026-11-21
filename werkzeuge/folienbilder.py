"""Folienbilder: jede Seite der Originalfolien vorab als kleines WebP-Bild (schnelle Anzeige ohne PDF-Zeichnen im Browser).

Ergebnis: inhalte/<fach>/folien/bilder/<deck>/<seite>.webp (wird von bau.py nach dist/folien/<fach>/<deck>/ kopiert).
Die App zeigt in „Originalfolien“ und im Folienfenster diese Bilder; nur die Großansicht zeichnet scharf aus dem PDF.
Quer gedruckte Folien auf Hochformat-Seiten werden wie in der App aufrecht gedreht (Textrichtung über pypdf).
Wiederholbar: Ein Deck wird nur neu gerendert, wenn sich sein PDF geändert hat (Prüfsumme in bilder/<deck>/stand.txt).

Aufruf: python3 werkzeuge/folienbilder.py [fach …]   (braucht pdftoppm und Pillow; nur lokal, nicht beim Bauen)"""
import sys, json, pathlib, subprocess, hashlib, tempfile, shutil

ROOT = pathlib.Path(__file__).resolve().parents[1]
IN = ROOT / 'inhalte'
BREITE, QUALI = 760, 52


def drehung(pdf):
    """Je Seite die Drehung (0/90/270), damit Text waagrecht steht – wie foBildRendern in app/js/folien.js."""
    try:
        from pypdf import PdfReader
    except ImportError:
        return {}
    out = {}
    for i, page in enumerate(PdfReader(str(pdf)).pages, 1):
        senk = waag = 0
        def v(text, cm, tm, fd, fs):
            nonlocal senk, waag
            a, b = tm[0] * cm[0] + tm[1] * cm[2], tm[0] * cm[1] + tm[1] * cm[3]
            n = len(text.strip())
            if abs(b) > abs(a): senk += n * (1 if b > 0 else -1)
            else: waag += n
        try: page.extract_text(visitor_text=v)
        except Exception: pass
        rot = page.get('/Rotate', 0) or 0
        if abs(senk) > waag: rot = (rot + (90 if senk > 0 else 270)) % 360
        out[i] = rot - (page.get('/Rotate', 0) or 0)   # pdftoppm beachtet /Rotate schon selbst
    return out


def deck_bilder(fid, deck):
    from PIL import Image
    pdf = IN / fid / 'folien' / (deck['id'] + '.pdf')
    ziel = IN / fid / 'folien' / 'bilder' / deck['id']
    summe = hashlib.sha1(pdf.read_bytes()).hexdigest()[:16] + f'-{BREITE}-{QUALI}'
    stand = ziel / 'stand.txt'
    if stand.exists() and stand.read_text().strip() == summe and len(list(ziel.glob('*.webp'))) == deck['n']:
        return 0
    if ziel.exists(): shutil.rmtree(ziel)
    ziel.mkdir(parents=True)
    rot = drehung(pdf)
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(['pdftoppm', '-r', '110', '-png', str(pdf), f'{tmp}/s'], check=True)
        for p in sorted(pathlib.Path(tmp).glob('s-*.png')):
            n = int(p.stem.split('-')[-1])
            im = Image.open(p).convert('RGB')
            r = rot.get(n, 0) % 360
            if r: im = im.rotate(-r, expand=True)   # PIL dreht gegen den Uhrzeigersinn
            if im.width > BREITE: im = im.resize((BREITE, round(im.height * BREITE / im.width)), Image.LANCZOS)
            im.save(ziel / f'{n}.webp', 'WEBP', quality=QUALI, method=5)
    stand.write_text(summe + '\n')
    return deck['n']


def main():
    faecher = sys.argv[1:] or sorted(p.parent.name for p in IN.glob('*/folien.json'))
    for fid in faecher:
        fo = json.loads((IN / fid / 'folien.json').read_text(encoding='utf-8'))
        neu = sum(deck_bilder(fid, d) for d in fo['decks'])
        groesse = sum(p.stat().st_size for p in (IN / fid / 'folien' / 'bilder').rglob('*.webp'))
        print(f'{fid}: {neu} Seiten neu gerendert, zusammen {groesse / 1e6:.1f} MB')


if __name__ == '__main__':
    main()
