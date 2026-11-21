"""Übersichtsbögen der Folien (intern): je Bild 24 Folien klein mit Seitennummer, um durchgestrichene Folien
(diagonaler Strich, Klammern, „Back-Up“) schnell zu finden. Einzelne Folie groß: --seite N.
Aufruf: python3 werkzeuge/folien_bogen.py <fach> <zielordner> [--von 1 --bis 999] [--seite N] [--dpi 30]"""
import sys, subprocess, pathlib, glob, tempfile
from PIL import Image, ImageDraw

ROOT = pathlib.Path(__file__).resolve().parents[1]
PDF = {
    'bwl': 'unterlagen/ABWL/folien/Einf*hrung in die Bwl_compressed.pdf',
    'mkt': 'unterlagen/Marketing/folien/Marketing_compressed.pdf',
    'mawi': 'unterlagen/Materialwirtschaft/folien/Materialwirtschaft_compressed.pdf',
    'ikm': 'unterlagen/Interkulturelles Management/folien/interkulturelles Management _compressed.pdf',
    'igt': 'unterlagen/Internationale Geschaeftstaetigkeit/folien/Rahmenbedingungen*.pdf',
    'wima': 'unterlagen/Mathe/folien/Einstieg _compressed.pdf',
}


def pdf(fid):
    return glob.glob(str(ROOT / PDF[fid]))[0]


def main():
    a = sys.argv[1:]
    fid, ziel = a[0], pathlib.Path(a[1]); ziel.mkdir(parents=True, exist_ok=True)
    opt = lambda k, d: int(a[a.index(k) + 1]) if k in a else d
    if '--seite' in a:
        n = opt('--seite', 1)
        subprocess.run(['pdftoppm', '-r', str(opt('--dpi', 80)), '-f', str(n), '-l', str(n), '-png', '-singlefile', pdf(fid), str(ziel / f'{fid}-s{n}')], check=True)
        print(ziel / f'{fid}-s{n}.png'); return
    von, bis, dpi = opt('--von', 1), opt('--bis', 9999), opt('--dpi', 30)
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(['pdftoppm', '-r', str(dpi), '-f', str(von), '-l', str(bis), '-png', pdf(fid), td + '/p'], check=True)
        bilder = sorted(pathlib.Path(td).glob('p-*.png'), key=lambda p: int(p.stem.split('-')[1]))
        for b0 in range(0, len(bilder), 24):
            grp = bilder[b0:b0 + 24]
            ims = [Image.open(p) for p in grp]
            w = max(i.width for i in ims); h = max(i.height for i in ims)
            bogen = Image.new('RGB', (w * 4, (h + 14) * 6), 'white'); d = ImageDraw.Draw(bogen)
            for k, (p, im) in enumerate(zip(grp, ims)):
                x, y = (k % 4) * w, (k // 4) * (h + 14)
                bogen.paste(im, (x, y + 14)); d.text((x + 3, y + 1), f'S.{int(p.stem.split("-")[1])}', fill='red')
            n1, n2 = int(grp[0].stem.split('-')[1]), int(grp[-1].stem.split('-')[1])
            out = ziel / f'{fid}-{n1:03d}-{n2:03d}.png'; bogen.save(out); print(out)


if __name__ == '__main__':
    main()
