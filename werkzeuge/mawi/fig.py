"""Zeichenhilfen für die MaWi-Schaubilder (nur Theme-Farben, Schrift ≥ 12)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import T, box, pfeil, tpg, svg, bild, E


def achsen(x0, y0, x1, y1, xl='', yl='', farbe='var(--axis)'):
    """Koordinatenachsen: Ursprung (x0, y0), x-Achse bis x1, y-Achse bis y1 (oben)"""
    s = pfeil(x0, y0, x1, y0, farbe, 1.4) + pfeil(x0, y0, x0, y1, farbe, 1.4)
    if xl:
        s += T(x1 - 4, y0 - 10, xl, 12, 600, 'end', 'var(--muted)')
    if yl:
        s += T(x0 + 6, y1 + 4, yl, 12, 600, 'start', 'var(--muted)')
    return s


def linie(punkte, farbe='var(--primary)', w=2.4, dash=False):
    d = ' '.join(f'{x:.1f},{y:.1f}' for x, y in punkte)
    return f'<polyline points="{d}" style="fill:none;stroke:{farbe}" stroke-width="{w}"{" stroke-dasharray=\"6 4\"" if dash else ""}/>'


def strich(x1, y1, x2, y2, farbe='var(--axis2)', w=1.3, dash=True):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" style="stroke:{farbe}" stroke-width="{w}"{" stroke-dasharray=\"4 4\"" if dash else ""}/>'


def punkt(x, y, farbe='var(--primary)', r=5):
    return f'<circle cx="{x}" cy="{y}" r="{r}" style="fill:{farbe}"/>'


def flaeche(punkte, farbe='var(--pale)', deck=1):
    d = ' '.join(f'{x:.1f},{y:.1f}' for x, y in punkte)
    return f'<polygon points="{d}" style="fill:{farbe};opacity:{deck}"/>'


def rechteck(x, y, w, h, farbe='var(--pale)', rand='var(--line)', rx=8):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" style="fill:{farbe};stroke:{rand}" stroke-width="1.2"/>'


def kurve(f, xa, xb, X, Y, n=60, **kw):
    """Funktion f über [xa, xb] mit Umrechnung X(x), Y(y) in Bildkoordinaten"""
    return linie([(X(xa + (xb - xa) * i / n), Y(f(xa + (xb - xa) * i / n))) for i in range(n + 1)], **kw)


def hb(bild_svg):
    """Hauptschaubild mit Tipp-Hinweis"""
    return bild(bild_svg)


def pfeil(x1, y1, x2, y2, farbe='var(--axis)', w=1.6, kopf=True, dash=False):
    """Pfeil in kräftigerer Achsenfarbe (im Hell- und Dunkelmodus gut sichtbar)"""
    import bausteine_zweisprachig as _z
    return _z.pfeil(x1, y1, x2, y2, farbe, w, kopf, dash)
