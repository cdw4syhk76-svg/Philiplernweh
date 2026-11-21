"""Erzeugt inhalte/wima/klausur.json: Probeklausur Mathematik (60 Punkte, 60 Minuten) im Aufbau der bekannten Klausuren:
1 Grenzwert/Sättigungswert · 2 zwei Ableitungen · 3 Integral · 4 ökonomische Funktionen · 5 Matrizen · 6 mehrstufige Produktion ·
7 LGS mit Determinante und Inverse · 8 partielle Grenzprodukte. Alle Lösungen mit sympy berechnet. Aufruf: python3 werkzeuge/wima/klausur.py"""
import json, pathlib
import sympy as sp
ROOT = pathlib.Path(__file__).resolve().parents[2]
IN = ROOT / 'inhalte' / 'wima'
x, t, y, L, K = sp.symbols('x t y L K', positive=True)
fl = lambda v: round(float(v), 4)
d = lambda v, n=2: f'{float(v):.{n}f}'.replace('.', ',')


def Z(label, wert, p, einheit='', tol=0.02):
    r = dict(typ='zahl', label=label, loesung=fl(wert), p=p, tol=tol)
    if einheit: r['einheit'] = einheit
    return r
def MX(label, m, p): return dict(typ='matrix', label=label, loesung=[[fl(v) for v in m.row(i)] for i in range(m.rows)], p=p)
def T(label, p, z=4): return dict(typ='text', label=label, p=p, zeilen=z)
def V(id, unter, text, felder, loesung, vorrang=False):
    r = dict(id=id, unter=unter, text=text, felder=felder, loesung=loesung)
    if vorrang: r['vorrang'] = True
    return r
def tex(m): return r'\begin{pmatrix}' + r' \\ '.join(' & '.join(str(v) for v in m.row(i)) for i in range(m.rows)) + r'\end{pmatrix}'


# ---------------- A1 Grenzwert / Sättigungswert (6 P)
a1 = []
for i, (a, b, c, k) in enumerate([(180, '0,5', 10, '0,5'), (210, '0,1', 20, '0,5'), (240, '0,4', 12, '0,2'), (150, '0,25', 8, '0,3')]):
    bb = sp.Rational(b.replace(',', '.')); kk = sp.Rational(k.replace(',', '.'))
    S = a / (bb + c * sp.exp(-kk * t)); lim = sp.limit(S, t, sp.oo); s0 = S.subs(t, 0)
    a1.append(V(f'1-satt{i}', 'saettigungswert', rf'Das Einkommen eines Wirtschaftszweigs entwickelt sich nach \(S(t) = \frac{{{a}}}{{{b} + {c} \cdot e^{{-{k}t}}}}\), \(t \ge 0\) (Jahre). Bestimmen Sie den Sättigungswert auf lange Sicht (t → ∞) und den Wert zum Zeitpunkt t = 0.',
                [Z('Sättigungswert', lim, 4), Z('S(0)', s0, 2)], rf'Für \(t \to \infty\) geht \(e^{{-{k}t}} \to 0\): \(\lim S(t) = \frac{{{a}}}{{{b}}} = {d(lim, 0)}\) (4 P). \(S(0) = \frac{{{a}}}{{{b} + {c}}} \approx {d(s0)}\) (2 P).', i == 0))
for i, (a, c) in enumerate([(4, 160), (3, 120), (5, 200)]):
    C = (a * y**2 - c) / (y**2 + 4 * y); lim = sp.limit(C, y, sp.oo); c10 = C.subs(y, 10)
    a1.append(V(f'1-rat{i}', 'saettigungswert', rf'Die Verkaufsmenge in Abhängigkeit vom Einkommen y der Haushalte ist \(C(y) = \frac{{{a}y^2 - {c}}}{{y^2 + 4y}}\). Was passiert, wenn das Einkommen über alle Grenzen steigt? Berechnen Sie außerdem C(10).',
                [Z(r'\(\lim_{y\to\infty} C(y)\)', lim, 4), Z('C(10)', c10, 2)], rf'Höchste Potenz \(y^2\) ausklammern: \(\frac{{{a} - {c}/y^2}}{{1 + 4/y}} \to {a}\) (4 P). \(C(10) = \frac{{{a * 100 - c}}}{{140}} \approx {d(c10)}\) (2 P).'))
for i, (A, B) in enumerate([(2, 3), (1, 4), (3, 2)]):
    cval = B * A - 1 - A**2
    a1.append(V(f'1-stet{i}', 'stetigkeit', rf'Gegeben ist \(f(x) = \begin{{cases}} x^2 + c, & x \le {A} \\ {B}x - 1, & x > {A} \end{{cases}}\). Bestimmen Sie c so, dass f überall stetig ist, und begründen Sie kurz.',
                [Z('c', cval, 4), T('Begründung', 2, 3)], rf'Beide Teile sind Polynome und damit stetig; zu prüfen ist nur \(x_0 = {A}\): links \({A**2} + c\), rechts \({B * A - 1}\). Gleichsetzen: \(c = {cval}\) (4 P), Begründung (2 P).'))
A1 = dict(titel='Grenzwerte', punkte=6, teile=[dict(punkte=6, varianten=a1)])

# ---------------- A2 Ableitungen (10 P: 2 × 5)
def abl(id, unter, f, ftex, v=False):
    fd = sp.simplify(sp.diff(f, x))
    return V(id, unter, rf'Bestimmen Sie die erste Ableitung von \(f(x) = {ftex}\).', [T("f′(x) mit Lösungsweg (u, v, u′, v′ bzw. innen/außen)", 5, 5)],
             rf"\(f'(x) = {sp.latex(fd)}\). Bewertung: richtige Regel(n) erkannt und Teilableitungen (3 P), korrekt zusammengesetzt (2 P).", v)
a2a = [abl('2a-prod', 'produkt-quotient', sp.cos(x) * sp.exp(x**2 + 4), r'\cos(x) \cdot e^{x^2 + 4}', True), abl('2a-kette2', 'kettenregel', sp.cos(sp.sin(x)**2), r'\cos(\sin^2(x))', True),
       abl('2a-prod2', 'produkt-quotient', sp.exp(1 / x**2) * sp.sin(4 * x + 1), r'e^{1/x^2} \cdot \sin(4x + 1)'), abl('2a-wurzel', 'kettenregel', sp.root(x, 4) * sp.log(x), r'\sqrt[4]{x} \cdot \ln(x)'),
       abl('2a-kette', 'kettenregel', (5 * x + 3)**3 * sp.exp(2 * x), r'(5x + 3)^3 \cdot e^{2x}')]
a2b = [abl('2b-quot', 'produkt-quotient', sp.cbrt(2 * x) / (x + 2), r'\frac{\sqrt[3]{2x}}{x + 2}', True), abl('2b-quot2', 'produkt-quotient', sp.root(x**2 + 3 * x, 4) / sp.log(x), r'\frac{\sqrt[4]{x^2 + 3x}}{\ln(x)}', True),
       abl('2b-quot3', 'produkt-quotient', sp.exp(2 * x**2) / sp.cos(x), r'\frac{e^{2x^2}}{\cos(x)}'), abl('2b-quot4', 'produkt-quotient', (2 * x + 9) / (4 * x - 7), r'\frac{2x + 9}{4x - 7}'),
       abl('2b-wurz', 'kettenregel', 1 / sp.sqrt(x**2 + 5), r'\frac{1}{\sqrt{x^2 + 5}}')]
A2 = dict(titel='Ableitungen', punkte=10, teile=[dict(punkte=5, varianten=a2a), dict(punkte=5, varianten=a2b)])

# ---------------- A3 Integral (7 P)
def integ(id, unter, f, a, b, ftex, hinweis, v=False):
    val = sp.integrate(f, (x, a, b))
    return V(id, unter, rf'Berechnen Sie \(\int_{{{sp.latex(a)}}}^{{{sp.latex(b)}}} {ftex}\,dx\). Geben Sie den Lösungsweg an.', [Z('Wert', val, 4, tol=0.02), T('Lösungsweg', 3, 5)],
             rf'{hinweis} Ergebnis: \({sp.latex(sp.nsimplify(val))} \approx {d(val)}\). (4 P Ergebnis, 3 P Weg)', v)
a3 = [integ('3-teexp', 'partielle-integration', x * sp.exp(2 * x), 0, 2, r'x \cdot e^{2x}', r'Partielle Integration: \(u = x,\ v\' = e^{2x}\); \(\left[\frac{x}{2}e^{2x}\right]_0^2 - \int_0^2 \frac12 e^{2x}dx\).', True),
      integ('3-xcos', 'partielle-integration', x * sp.cos(x), 0, sp.pi, r'x \cdot \cos(x)', r'Partielle Integration: \(u = x,\ v\' = \cos x\); \([x\sin x + \cos x]_0^{\pi}\).'),
      integ('3-xex', 'partielle-integration', x * sp.exp(x), 0, 1, r'x \cdot e^{x}', r'Partielle Integration: \([(x-1)e^x]_0^1\).'),
      integ('3-subst', 'substitution', 2 * x * sp.exp(x**2), 0, 1, r'2x \cdot e^{x^2}', r'Substitution \(u = x^2\), \(du = 2x\,dx\), Grenzen 0 bis 1.'),
      integ('3-wurzel', 'substitution', x * sp.sqrt(1 + 2 * x), 0, 4, r'x\sqrt{1 + 2x}', r'Substitution \(u = 1 + 2x\), \(x = \frac{u-1}{2}\), \(dx = \frac{du}{2}\), Grenzen 1 bis 9.')]
A3 = dict(titel='Integralrechnung', punkte=7, teile=[dict(punkte=7, varianten=a3)])

# ---------------- A4 Ökonomische Funktionen (12 P)
a4 = []
for i, (a, b, c, dd, p) in enumerate([(1, 15, 125, 375, 150), (1, 12, 60, 200, 96), (2, 30, 200, 400, 200), (1, 9, 40, 100, 61)]):
    Kx = a * x**3 - b * x**2 + c * x + dd; G = p * x - Kx
    xs = [r for r in sp.solve(sp.diff(G, x), x) if r.is_real and r > 0 and sp.diff(G, x, 2).subs(x, r) < 0]
    assert len(xs) == 1, i
    xg = xs[0]; gmax = G.subs(x, xg)
    ktex = (f'{a}x^3' if a != 1 else 'x^3') + f' - {b}x^2 + {c}x + {dd}'
    a4.append(V(f'4-kosten{i}', 'kostenfunktion', rf'Die Gesamtkosten eines Herstellers sind \(K(x) = {ktex}\), die Umsatzfunktion \(U(x) = {p}x\).<br>a) Wie hoch sind die Fixkosten?<br>b) Geben Sie die Funktion der variablen Kosten an.<br>c) Geben Sie die Funktionen der Grenzkosten und der Stückkosten an.<br>d) Berechnen Sie das Gewinnmaximum (Menge und Gewinn).',
                [Z('a) Fixkosten', dd, 1, 'GE'), T('b) variable Kosten', 1, 2), T('c) Grenzkosten und Stückkosten', 3, 3), Z('d) gewinnmaximale Menge', xg, 4, 'ME', 0.05), Z('d) maximaler Gewinn', gmax, 3, 'GE', 0.5)],
                rf"a) \(K_f = {dd}\). b) \(K_v(x) = {sp.latex(Kx - dd)}\). c) \(K'(x) = {sp.latex(sp.diff(Kx, x))}\), \(k(x) = {sp.latex(sp.expand(Kx / x))}\). d) \(G(x) = {sp.latex(sp.expand(G))}\); \(G'(x) = 0\) ⇒ \(x \approx {d(xg)}\); \(G''(x) < 0\); \(G \approx {d(gmax)}\).", i == 0))
# Stückkostenvariante aus der Klausureinsicht: k(x) = 3x² + 3x + 12 (Stückkosten), u = 7x? sinnvoller mit Preis 120
for i, (s2, s1, s0, p) in enumerate([(3, 3, 12, 120), (2, 4, 20, 100)]):
    Kx = s2 * x**3 + s1 * x**2 + s0 * x; Kx_full = Kx
    G = p * x - Kx; xg = [r for r in sp.solve(sp.diff(G, x), x) if r > 0][0]
    a4.append(V(f'4-stueck{i}', 'gewinnmaximum', rf'Die Stückkostenfunktion lautet \(k(x) = {s2}x^2 + {s1}x + {s0}\), der Marktpreis beträgt {p} GE/ME.<br>a) Wie hoch sind die Fixkosten?<br>b) Geben Sie die Gesamtkostenfunktion an.<br>c) Geben Sie die Grenzkostenfunktion an.<br>d) Berechnen Sie die gewinnmaximale Menge und den maximalen Gewinn.',
                [Z('a) Fixkosten', 0, 1, 'GE'), T('b) Gesamtkosten', 1, 2), T('c) Grenzkosten', 3, 2), Z('d) gewinnmaximale Menge', xg, 4, 'ME', 0.05), Z('d) maximaler Gewinn', G.subs(x, xg), 3, 'GE', 0.5)],
                rf"a) K(x) = k(x)·x hat kein konstantes Glied: Fixkosten 0. b) \(K(x) = {sp.latex(Kx)}\). c) \(K'(x) = {sp.latex(sp.diff(Kx, x))}\). d) \(G(x) = {sp.latex(sp.expand(G))}\), \(G' = 0\) ⇒ \(x \approx {d(xg)}\), \(G \approx {d(G.subs(x, xg))}\)."))
A4 = dict(titel='Ökonomische Funktionen', punkte=12, teile=[dict(punkte=12, varianten=a4)])

# ---------------- A5 Matrizen (8 P)
a5 = []
for i, (A, B, C, v) in enumerate([
        (sp.Matrix([[1, 2, 3], [0, 3, -1], [-4, 1, 0]]), sp.Matrix([[2, 2, 1], [-1, 0, 4], [3, 1, 0]]), sp.Matrix([[3, 4, 6], [1, 3, -9], [-2, 0, 5]]), sp.Matrix([1, 2, -1])),
        (sp.Matrix([[4, 3], [2, 4], [1, 7]]), sp.Matrix([[6, 5], [4, 3]]), sp.Matrix([[1, 0], [0, 2], [3, 3]]), sp.Matrix([2, -1])),
        (sp.Matrix([[2, 3, 4], [1, 3, 5]]), sp.Matrix([[1, 0], [0, 2], [3, 3]]), sp.Matrix([[1, 1, 1], [0, 2, -1]]), sp.Matrix([1, 0, 2]))]):
    a5.append(V(f'5-mat{i}', 'matrizen', rf'Gegeben sind \(A = {tex(A)}\), \(B = {tex(B)}\), \(C = {tex(C)}\), \(v = {tex(v)}\).<br>Berechnen Sie a) \(A^T\),<br>b) \(A \cdot v\),<br>c) \(A + C\),<br>d) \(((A \cdot B)^T)^T\).',
                [MX('a) Aᵀ', A.T, 2), MX('b) A·v', A * v, 2), MX('c) A + C', A + C, 2), MX('d) ((A·B)ᵀ)ᵀ', A * B, 2)],
                rf'a) \(A^T = {tex(A.T)}\) b) \(A v = {tex(A * v)}\) c) \(A + C = {tex(A + C)}\) d) Zweimal transponieren hebt sich auf: \(A B = {tex(A * B)}\).', i == 0))
A5 = dict(titel='Matrizenrechnung', punkte=8, teile=[dict(punkte=8, varianten=a5)])

# ---------------- A6 Mehrstufige Produktion (5 P)
a6 = []
for i, (RZ, ZE, p) in enumerate([
        (sp.Matrix([[2, 1], [3, 2], [1, 4]]), sp.Matrix([[1, 2, 0], [3, 1, 2]]), sp.Matrix([100, 50, 80])),
        (sp.Matrix([[1, 2], [0, 3], [4, 1]]), sp.Matrix([[2, 1], [1, 3]]), sp.Matrix([200, 100])),
        (sp.Matrix([[3, 1, 0], [1, 2, 2]]), sp.Matrix([[1, 1], [2, 0], [0, 3]]), sp.Matrix([50, 40]))]):
    Cm = RZ * ZE
    a6.append(V(f'6-prod{i}', 'mehrstufige-produktion', rf'Rohstoffe → Zwischenprodukte: \(M_{{RZ}} = {tex(RZ)}\); Zwischenprodukte → Endprodukte: \(M_{{ZE}} = {tex(ZE)}\). Produktionsplan \(p = {tex(p)}\).<br>a) Bestimmen Sie die Verbrauchskoeffizienten der Rohstoffe je Endprodukt.<br>b) Wie hoch ist der Rohstoffbedarf?',
                [MX('a) Gesamtbedarfsmatrix', Cm, 3), MX('b) Rohstoffbedarf', Cm * p, 2)], rf'a) \(C = M_{{RZ}} \cdot M_{{ZE}} = {tex(Cm)}\) b) \(C \cdot p = {tex(Cm * p)}\)', i == 0))
A6 = dict(titel='Mehrstufige Produktion', punkte=5, teile=[dict(punkte=5, varianten=a6)])

# ---------------- A7 LGS (7 P)
a7 = []
for i, (D, b) in enumerate([(sp.Matrix([[1, 4, 3], [2, 5, 4], [1, -3, -2]]), sp.Matrix([1, 4, 5])), (sp.Matrix([[1, 2, -1], [2, 5, 2], [1, 1, 1]]), sp.Matrix([1, 4, 5])),
                            (sp.Matrix([[2, 1, 0], [1, 1, 1], [0, 1, 3]]), sp.Matrix([3, 4, 5])), (sp.Matrix([[1, 0, 1], [3, 5, 2], [0, 4, 1]]), sp.Matrix([2, 10, 5]))]):
    det = D.det(); assert det != 0
    xs = D.inv() * b
    def term(k, c):
        return ('' if k == 1 else '-' if k == -1 else str(k)) + f'x_{c + 1}'
    gl = r' \\ '.join(' + '.join(term(D[r, c], c) for c in range(3) if D[r, c] != 0).replace('+ -', '- ') + f' = {b[r]}' for r in range(3))
    a7.append(V(f'7-lgs{i}', 'inverse-matrix', rf'Bestimmen Sie mit Hilfe der Determinante, ob das LGS eindeutig lösbar ist, und bestimmen Sie die Lösung mit Hilfe der inversen Matrix.<br>\(\begin{{array}}{{l}} {gl} \end{{array}}\)',
                [Z('Determinante', det, 2), MX('inverse Matrix', D.inv(), 3), MX('Lösung x', xs, 2)],
                rf'\(\det = {det} \ne 0\) ⇒ eindeutig lösbar (2 P). \(A^{{-1}} = {tex(D.inv())}\) (3 P). \(x = A^{{-1}} b = {tex(xs)}\) (2 P).', i == 0))
A7 = dict(titel='Lineare Gleichungssysteme', punkte=7, teile=[dict(punkte=7, varianten=a7)])

# ---------------- A8 Grenzprodukte (5 P)
a8 = []
for i, (c, a, b, l0, k0) in enumerate([(80, '0,6', '0,4', 1500, 300), (90, '0,8', '0,2', 1000, 200), (50, '0,5', '0,5', 400, 100), (100, '0,7', '0,3', 2000, 500)]):
    aa = sp.Rational(a.replace(',', '.')); bb = sp.Rational(b.replace(',', '.'))
    Y = c * L**aa * K**bb; gL = sp.diff(Y, L).subs({L: l0, K: k0}); gK = sp.diff(Y, K).subs({L: l0, K: k0})
    a8.append(V(f'8-cd{i}', 'grenzprodukt', rf'Produktionsfunktion \(Y(L; K) = {c} \cdot L^{{{a}}} \cdot K^{{{b}}}\) mit L = Arbeit in AE, K = Kapital in GE. Bestimmen und interpretieren Sie die partiellen Grenzprodukte der Arbeit und des Kapitals für L = {l0:,} AE und K = {k0} GE.'.replace(',', '.'),
                [Z('∂Y/∂L', gL, 2, tol=0.05), Z('∂Y/∂K', gK, 2, tol=0.05), T('Interpretation', 1, 3)],
                rf'\(\frac{{\partial Y}}{{\partial L}} = {d(aa * c)} L^{{{d(aa - 1)}}} K^{{{b}}} \approx {d(gL)}\): Eine zusätzliche Arbeitseinheit erhöht den Output um etwa {d(gL)} Einheiten (K konstant). '
                rf'\(\frac{{\partial Y}}{{\partial K}} = {d(bb * c)} L^{{{a}}} K^{{{d(bb - 1)}}} \approx {d(gK)}\): Eine zusätzliche Geldeinheit Kapital erhöht den Output um etwa {d(gK)} Einheiten (L konstant).', i < 2))
A8 = dict(titel='Partielle Ableitungen', punkte=5, teile=[dict(punkte=5, varianten=a8)])

KL = dict(deckblatt=dict(fach='Mathematik', pruefer='Prof. Dr. Weinberger', hilfsmittel='keine',
                         bemerkungen='Lösungsweg und Begründung angeben. 60 Minuten für 8 Aufgaben: Zeit einteilen.'),
          aufgaben=[A1, A2, A3, A4, A5, A6, A7, A8])
KAP = {t_['id'] for k in json.loads((IN / 'fach.json').read_text())['kapitel'] for t_ in k['themen']}
for A in KL['aufgaben']:
    assert sum(T_['punkte'] for T_ in A['teile']) == A['punkte'], A['titel']
    for T_ in A['teile']:
        assert 3 <= len(T_['varianten']) <= 10, (A['titel'], len(T_['varianten']))
        for v in T_['varianten']:
            assert abs(sum(f['p'] for f in v['felder']) - T_['punkte']) < 1e-9, v['id']; assert v['unter'] in KAP
summe = sum(A['punkte'] for A in KL['aufgaben']); assert summe == 60, summe
(IN / 'klausur.json').write_text(json.dumps(KL, ensure_ascii=False, indent=1))
print(f'wima: Probeklausur {summe} P, {len(KL["aufgaben"])} Aufgaben, {sum(len(T_["varianten"]) for A in KL["aufgaben"] for T_ in A["teile"])} Varianten')
