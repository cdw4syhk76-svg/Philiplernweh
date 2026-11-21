"""Zeichenhilfen für die ABWL-Schaubilder (nur Theme-Farben, Schrift ≥ 12)."""
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


def graph(funcs, xr, yr, W=360, H=250, xl='x', yl='y', ticks_x=(), ticks_y=(), extra='', box_=(44, 16, 344, 222)):
    """Koordinatensystem mit Graphen. funcs: [(f, xa, xb, farbe, label, tip, label_x)];
    xr=(xmin,xmax), yr=(ymin,ymax); gibt (svg_inhalt, X, Y) zurück."""
    L, Tp, R, B = box_
    X = lambda x: L + (x - xr[0]) / (xr[1] - xr[0]) * (R - L)
    Y = lambda y: B - (y - yr[0]) / (yr[1] - yr[0]) * (B - Tp)
    x0 = X(0) if xr[0] <= 0 <= xr[1] else L
    y0 = Y(0) if yr[0] <= 0 <= yr[1] else B
    s = pfeil(L, y0, R + 6, y0, 'var(--axis)', 1.4) + pfeil(x0, B, x0, Tp - 4, 'var(--axis)', 1.4)
    s += T(R + 4, y0 - 8, xl, 12, 700, 'end', 'var(--muted)') + T(x0 + 6, Tp + 4, yl, 12, 700, 'start', 'var(--muted)')
    for v in ticks_x:
        s += f'<line x1="{X(v):.1f}" y1="{y0 - 3}" x2="{X(v):.1f}" y2="{y0 + 3}" style="stroke:var(--axis)"/>' + T(X(v), y0 + 16, f'{v:g}'.replace('.', ','), 12, 400)
    for v in ticks_y:
        s += f'<line x1="{x0 - 3}" y1="{Y(v):.1f}" x2="{x0 + 3}" y2="{Y(v):.1f}" style="stroke:var(--axis)"/>' + T(x0 - 6, Y(v) + 4, f'{v:g}'.replace('.', ','), 12, 400, 'end')
    for f, xa, xb, farbe, lab, tip, lx in funcs:
        pts = []
        for i in range(161):
            x = xa + (xb - xa) * i / 160
            try:
                y = f(x)
            except (ZeroDivisionError, ValueError, OverflowError):
                y = None
            if y is None or not (yr[0] - (yr[1] - yr[0]) * .05 <= y <= yr[1] + (yr[1] - yr[0]) * .05):
                if len(pts) > 1:
                    s += tpg(linie(pts, farbe, 2.6), tip) if tip else linie(pts, farbe, 2.6)
                pts = []
                continue
            pts.append((X(x), Y(y)))
        if len(pts) > 1:
            s += tpg(linie(pts, farbe, 2.6), tip) if tip else linie(pts, farbe, 2.6)
        if lab and lx is not None:
            s += T(X(lx), Y(f(lx)) - 9, lab, 12, 800, 'middle', farbe)
    return s + extra, X, Y


# ---------- Formeln in Spiel-Daten (Kurz-Check) als Klartext: LaTeX in data-Attributen bricht das JSON ----------
import re as _re
import bausteine_de as _bd


def klartext(s):
    s = str(s)
    rep = [(r'\\left|\\right|\\displaystyle|\\,|\;|\\!', ''), (r'\{,\}', ','), (r'\\cdot', '·'), (r'\\to', '→'), (r'\\infty', '∞'), (r'\\le(?![a-z])', '≤'), (r'\\ge(?![a-z])', '≥'),
           (r'\\ne(?![a-z])', '≠'), (r'\\mathbb\{R\}', 'ℝ'), (r'\\setminus', '∖'), (r'\\uparrow', '↑'), (r'\\downarrow', '↓'), (r'\\varepsilon', 'ε'), (r'\\pi', 'π'),
           (r'\\ln', 'ln'), (r'\\sin', 'sin'), (r'\\cos', 'cos'), (r'\\lim_\{([^{}]*)\}', r'lim(\1) '), (r'\\int_\{?([^{} ]*)\}?\^\{?([^{} ]*)\}?', r'∫ von \1 bis \2 '), (r'\\int', '∫'),
           (r'\\sum_\{([^{}]*)\}\^\{([^{}]*)\}', r'Σ(\1 bis \2) ')]
    for a, b in rep:
        s = _re.sub(a, b, s)
    for _ in range(4):
        s = _re.sub(r'\\[dt]?frac\{([^{}]*)\}\{([^{}]*)\}', r'(\1)/(\2)', s)
        s = _re.sub(r'\\sqrt\[3\]\{([^{}]*)\}', r'∛(\1)', s)
        s = _re.sub(r'\\sqrt\[4\]\{([^{}]*)\}', r'∜(\1)', s)
        s = _re.sub(r'\\sqrt\{([^{}]*)\}', r'√(\1)', s)
        s = _re.sub(r'\^\{([^{}]*)\}', r'^(\1)', s)
        s = _re.sub(r'_\{([^{}]*)\}', r'_\1', s)
    s = s.replace(r'\(', '').replace(r'\)', '').replace('\\', '')
    return s


def wahr(sid, aussagen):
    return _bd.wahr(sid, [(klartext(t), r, klartext(w)) for t, r, w in aussagen])


def spiel(sid, frage, kategorien, karten_):
    return _bd.spiel(sid, klartext(frage), [klartext(k) for k in kategorien], [(klartext(t), k, klartext(w)) for t, k, w in karten_])
