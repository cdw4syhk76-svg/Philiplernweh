"""Erzeugt inhalte/wima/aufgaben.json (große Aufgaben im Klausurstil; alle Zahlen mit sympy gerechnet). Aufruf: python3 werkzeuge/wima/aufgaben.py"""
import json, pathlib
import sympy as sp
ROOT = pathlib.Path(__file__).resolve().parents[2]
x, t, L, K = sp.symbols('x t L K', positive=True)
A = []
d = lambda v, n=2: (f'{float(v):,.{n}f}').replace(',', '#').replace('.', ',').replace('#', '.').rstrip('0').rstrip(',') if n else f'{float(v):,.0f}'.replace(',', '.')


def ol(*s): return '<ol>' + ''.join(f'<li>{z}</li>' for z in s) + '</ol>'
def teil(text, punkte, t1, t2, loesung, ergebnis=None, einheit=None, tol=None):
    r = dict(text=text, punkte=punkte, tipp1=t1, tipp2=t2, loesung=loesung)
    if ergebnis is not None:
        r['ergebnis'] = round(float(ergebnis), 4)
        if einheit: r['einheit'] = einheit
        r['tol'] = tol if tol is not None else 0.01
    return r
def aufgabe(id, unter, art, stufe, titel, ausgang, teile, klausur=True):
    A.append(dict(id='wima-' + id, unter=unter, art=art, stufe=stufe, klausur=klausur, titel=titel, quelle='im Klausurstil', ausgang=ausgang, teile=teile))


# 1 Sättigungswert und Stetigkeit
S = 180 / (sp.Rational(1, 2) + 10 * sp.exp(-t / 2)); s_inf = sp.limit(S, t, sp.oo); s0 = S.subs(t, 0)
t_half = sp.solve(sp.Eq(S, 180), t)[0]
assert s_inf == 360
aufgabe('saettigung', ['saettigungswert', 'exp-ln', 'stetigkeit'], 'rechnen', 2, 'Einkommen auf lange Sicht',
    r'<p>Das Gesamteinkommen eines Wirtschaftszweigs entwickelt sich nach \(S(t) = \frac{180}{0{,}5 + 10 \cdot e^{-0{,}5t}}\), t in Jahren.</p>', [
    teil('Berechnen Sie den Sättigungswert für t → ∞.', 3, 'Was passiert mit e^(−0,5t)?', 'Es geht gegen 0.', ol(r'\(e^{-0{,}5t} \to 0\)', r'\(\lim S(t) = \frac{180}{0{,}5} = 360\)'), s_inf),
    teil('Wie hoch ist das Einkommen zum Planungszeitpunkt t = 0?', 2, 'Einsetzen.', 'e⁰ = 1.', ol(r'\(S(0) = \frac{180}{10{,}5}\)', f'≈ {d(s0)}'), s0),
    teil('Nach wie vielen Jahren ist die Hälfte des Sättigungswerts (180) erreicht?', 3, 'S(t) = 180 setzen, nach t auflösen.', '0,5 + 10e^(−0,5t) = 1.',
         ol(r'\(\frac{180}{0{,}5 + 10e^{-0{,}5t}} = 180 \Rightarrow 10e^{-0{,}5t} = 0{,}5\)', r'\(e^{-0{,}5t} = 0{,}05 \Rightarrow t = -2\ln 0{,}05\)', f'≈ {d(t_half)} Jahre'), t_half, 'Jahre')])

# 2 Ableitungen
aufgabe('ableitungen', ['produkt-quotient', 'kettenregel'], 'rechnen', 3, 'Zwei Ableitungen wie in der Klausur',
    '<p>Bestimmen Sie die erste Ableitung der folgenden Funktionen.</p>', [
    teil(r'\(f(x) = \cos(x) \cdot e^{x^2 + 4}\)', 5, 'Produkt zweier Funktionen; der zweite Faktor ist verkettet.', "u = cos x, v = e^(x²+4), v′ = 2x·e^(x²+4).",
         ol(r"\(u' = -\sin x\), \(v' = 2x e^{x^2+4}\)", r"\(f'(x) = -\sin(x) e^{x^2+4} + \cos(x) \cdot 2x e^{x^2+4} = e^{x^2+4}(2x\cos x - \sin x)\)")),
    teil(r'\(g(x) = \frac{\sqrt[4]{x^2 + 3x}}{\ln x}\)', 5, 'Quotient; der Zähler ist verkettet.', 'Zähler als (x² + 3x)^(1/4) schreiben.',
         ol(r"\(u = (x^2+3x)^{1/4},\ u' = \frac{2x + 3}{4(x^2+3x)^{3/4}}\); \(v = \ln x,\ v' = \frac{1}{x}\)", r"\(g'(x) = \frac{\frac{2x+3}{4(x^2+3x)^{3/4}} \ln x - (x^2+3x)^{1/4} \cdot \frac{1}{x}}{(\ln x)^2}\)")),
    teil(r'\(h(x) = \cos(\sin^2 x)\)', 4, 'Doppelte Verkettung.', 'außen cos, Mitte Quadrat, innen sin.', ol(r"\(h'(x) = -\sin(\sin^2 x) \cdot 2\sin x \cdot \cos x\)"))])

# 3 Integrale
I1 = sp.integrate(t * sp.exp(2 * t), (t, 0, 2)); I2 = sp.integrate(x * sp.sqrt(1 + 2 * x), (x, 0, 4))
aufgabe('integrale', ['partielle-integration', 'substitution', 'bestimmtes-integral'], 'rechnen', 3, 'Integrale berechnen', '<p>Berechnen Sie die bestimmten Integrale.</p>', [
    teil(r'\(\int_0^2 t \cdot e^{2t}\,dt\)', 5, 'Partielle Integration: Polynom ableiten.', "u = t, v′ = e^(2t), v = ½e^(2t).",
         ol(r'\(\left[\frac{t}{2}e^{2t}\right]_0^2 - \int_0^2 \frac12 e^{2t}\,dt = e^4 - \left[\frac14 e^{2t}\right]_0^2\)', r'\(= \frac34 e^4 + \frac14\)', f'≈ {d(I1)}'), I1),
    teil(r'\(\int_0^4 x\sqrt{1 + 2x}\,dx\)', 5, 'Substitution u = 1 + 2x.', 'x = (u − 1)/2, dx = du/2, Grenzen 1 bis 9.',
         ol(r'\(\int_1^9 \frac{u-1}{2}\sqrt{u}\,\frac{du}{2} = \frac14\int_1^9 (u^{3/2} - u^{1/2})\,du\)', r'\(= \frac14\left[\frac25 u^{5/2} - \frac23 u^{3/2}\right]_1^9 = \frac{298}{15}\)', f'≈ {d(I2)}'), I2)])

# 4 Ökonomische Funktionen
Kx = x**3 - 15 * x**2 + 125 * x + 375; G = 150 * x - Kx
xg = sp.solve(sp.diff(G, x), x)[0]; xbo = sp.nsolve(sp.diff(Kx / x, x), x, 10)
aufgabe('kosten-gewinn', ['kostenfunktion', 'gewinnzone', 'gewinnmaximum', 'betriebsoptimum'], 'rechnen', 3, 'Zahnpasta: Kosten, Gewinn, Betriebsoptimum',
    r'<p>Die Gesamtkosten eines Zahnpastaherstellers: \(K(x) = x^3 - 15x^2 + 125x + 375\); Umsatz \(U(x) = 150x\).</p>', [
    teil('Wie hoch sind die Fixkosten? Geben Sie die variablen Kosten, die Stückkosten und die Grenzkosten an.', 4, 'Fixkosten = K(0).', 'k = K/x, Grenzkosten = K′.',
         ol('Fixkosten 375', r'\(K_v(x) = x^3 - 15x^2 + 125x\)', r'\(k(x) = x^2 - 15x + 125 + \frac{375}{x}\)', r"\(K'(x) = 3x^2 - 30x + 125\)"), 375, 'GE'),
    teil('Bestimmen Sie die Gewinnzone.', 4, 'G = U − K; eine Nullstelle raten.', 'G(5) = 0, dann Polynomdivision.',
         ol(r'\(G(x) = -x^3 + 15x^2 + 25x - 375 = (x - 5)(-x^2 + 10x + 75)\)', r'\(x = 5\) und \(x = 15\) (−5 entfällt)', 'Gewinnzone [5; 15]'), 15, 'ME'),
    teil('Bei welcher Menge ist der Gewinn maximal, und wie hoch ist er?', 4, "G′(x) = 0.", "G′ = −3x² + 30x + 25.",
         ol(r"\(G'(x) = -3x^2 + 30x + 25 = 0 \Rightarrow x = 5 + \sqrt{25 + \frac{25}{3}}\)", f'x ≈ {d(xg)}', f'G ≈ {d(G.subs(x, xg))} GE'), xg, 'ME'),
    teil('Bestimmen Sie das Betriebsoptimum (Näherung) und die kurzfristige Preisuntergrenze.', 4, "Minimum von k(x) bzw. k_v(x).", "k_v′(x) = 2x − 15 = 0.",
         ol(f'Betriebsoptimum: k′(x) = 0 ⇒ x ≈ {d(xbo)}, k ≈ {d((Kx / x).subs(x, xbo))}', r'Betriebsminimum: \(x = 7{,}5,\ k_v = 68{,}75\) = kurzfristige Preisuntergrenze'), xbo, 'ME')])

# 5 Ökonomische Funktionen: Kostenfunktion aus Eigenschaften
aufgabe('kosten-bestimmen', ['kostenfunktion', 'gewinnzone'], 'rechnen', 3, 'Bleistiftfabrik: Kostenfunktion bestimmen',
    '<p>Die Gesamtkostenfunktion einer Bleistiftfabrik ist ganzrational 3. Grades. Die fixen Kosten betragen 12, die Gesamtkosten an der Stelle 2 betragen 20, bei der Menge 2 sind die Grenzkosten null und minimal. Umsatz U(x) = 7x.</p>', [
    teil('Bestimmen Sie K(x).', 5, 'Ansatz ax³ + bx² + cx + 12 und drei Bedingungen.', "K(2) = 20, K′(2) = 0, K″(2) = 0.",
         ol(r"\(K''(2) = 12a + 2b = 0 \Rightarrow b = -6a\)", r"\(K'(2) = 12a + 4b + c = 0 \Rightarrow c = 12a\)", r'\(K(2) = 8a + 12 = 20 \Rightarrow a = 1\)', r'\(K(x) = x^3 - 6x^2 + 12x + 12\)')),
    teil('Berechnen Sie die Gewinnzone.', 4, 'G = 7x − K, Nullstellen raten.', 'Probiere 3 und 4.', ol(r'\(G(x) = -x^3 + 6x^2 - 5x - 12\)', 'G(3) = 0, G(4) = 0', 'Gewinnzone [3; 4]'), 4, 'ME')], klausur=False)

# 6 Matrizen
Am = sp.Matrix([[1, 2, 3], [0, 3, -1], [-4, 1, 0]]); Bm = sp.Matrix([[2, 2, 1], [-1, 0, 4]]); v = sp.Matrix([1, 2, -1])
aufgabe('matrizen', ['matrizen', 'matrizenmultiplikation'], 'rechnen', 2, 'Matrizenrechnung',
    r'<p>\(A = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 3 & -1 \\ -4 & 1 & 0 \end{pmatrix}\), \(B = \begin{pmatrix} 2 & 2 & 1 \\ -1 & 0 & 4 \end{pmatrix}\), \(v = \begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix}\)</p>', [
    teil('Berechnen Sie Aᵀ und 2·A.', 2, 'Zeilen werden Spalten.', 'Jedes Element verdoppeln.', ol(r'\(A^T = \begin{pmatrix} 1 & 0 & -4 \\ 2 & 3 & 1 \\ 3 & -1 & 0 \end{pmatrix}\)', r'\(2A = \begin{pmatrix} 2 & 4 & 6 \\ 0 & 6 & -2 \\ -8 & 2 & 0 \end{pmatrix}\)')),
    teil('Berechnen Sie A·v.', 2, 'Zeile mal Vektor.', '1·1 + 2·2 + 3·(−1).', ol(r'\(A v = (' + '; '.join(str(c) for c in (Am * v)) + r')^T\)'), (Am * v)[0]),
    teil('Berechnen Sie B·A. Ist A·B definiert?', 3, 'Format prüfen: (2×3)·(3×3).', 'A·B: (3×3)·(2×3).',
         ol(r'\(B A = ' + r'\begin{pmatrix}' + r' \\ '.join(' & '.join(str(c) for c in (Bm * Am).row(i)) for i in range(2)) + r'\end{pmatrix}\)', 'A·B ist nicht definiert (3 Spalten, 2 Zeilen).'), (Bm * Am)[0, 0])])

# 7 Mehrstufige Produktion
RZ = sp.Matrix([[2, 1], [3, 2], [1, 4]]); ZE = sp.Matrix([[1, 2, 0], [3, 1, 2]]); p = sp.Matrix([100, 50, 80])
C = RZ * ZE; xr = C * p
aufgabe('produktion', ['mehrstufige-produktion'], 'rechnen', 3, 'Rohstoffbedarf in zwei Stufen',
    r'<p>Drei Rohstoffe R1–R3 werden zu zwei Zwischenprodukten Z1, Z2 verarbeitet, daraus entstehen drei Endprodukte E1–E3. Verbrauch je Einheit: '
    r'\(M_{RZ} = \begin{pmatrix} 2 & 1 \\ 3 & 2 \\ 1 & 4 \end{pmatrix}\), \(M_{ZE} = \begin{pmatrix} 1 & 2 & 0 \\ 3 & 1 & 2 \end{pmatrix}\). Geplant: 100 E1, 50 E2, 80 E3.</p>', [
    teil('Berechnen Sie die Gesamtbedarfsmatrix (Rohstoffe je Endprodukt).', 3, 'Welche Matrix kommt zuerst?', 'M_RZ · M_ZE.', ol(r'\(C = M_{RZ} M_{ZE} = \begin{pmatrix}' + r' \\ '.join(' & '.join(str(c) for c in C.row(i)) for i in range(3)) + r'\end{pmatrix}\)'), C[0, 0]),
    teil('Wie viele Einheiten R1 werden insgesamt gebraucht?', 2, 'C mal Produktionsvektor.', 'Erste Zeile von C mal p.', ol(f'R1: {C[0, 0]}·100 + {C[0, 1]}·50 + {C[0, 2]}·80 = {xr[0]}', f'R2: {xr[1]}, R3: {xr[2]}'), xr[0], 'Einheiten')])

# 8 LGS mit Inverse
D1 = sp.Matrix([[1, 4, 3], [2, 5, 4], [1, -3, -2]]); b1 = sp.Matrix([1, 4, 5]); sol = D1.inv() * b1
aufgabe('lgs-inverse', ['determinante', 'inverse-matrix', 'lgs-gauss'], 'rechnen', 3, 'LGS mit Determinante und Inverse',
    r'<p>\(x_1 + 4x_2 + 3x_3 = 1\), \(2x_1 + 5x_2 + 4x_3 = 4\), \(x_1 - 3x_2 - 2x_3 = 5\)</p>', [
    teil('Prüfen Sie mit der Determinante, ob das LGS eindeutig lösbar ist.', 3, 'Sarrus.', 'Hauptdiagonalen minus Nebendiagonalen.', ol('det = (−10 + 16 − 18) − (15 − 12 − 16) = −12 + 13 = 1 ≠ 0', 'eindeutig lösbar'), D1.det()),
    teil('Bestimmen Sie die inverse Matrix.', 4, '(D | E) mit Gauß-Jordan.', 'Probe D·D⁻¹ = E.', ol(r'\(D^{-1} = \begin{pmatrix} 2 & -1 & 1 \\ 8 & -5 & 2 \\ -11 & 7 & -3 \end{pmatrix}\)')),
    teil('Lösen Sie das LGS mit der Inversen. Geben Sie x₁ an.', 2, 'x = D⁻¹·b.', 'Erste Zeile von D⁻¹ mal b.', ol('x = (3; −2; 2)'), sol[0])])

# 9 Grenzprodukte
Y = 80 * L**sp.Rational(3, 5) * K**sp.Rational(2, 5); gL = sp.diff(Y, L).subs({L: 1500, K: 300}); gK = sp.diff(Y, K).subs({L: 1500, K: 300})
aufgabe('grenzprodukte', ['grenzprodukt', 'partielle-ableitung', 'totales-differential'], 'rechnen', 3, 'Cobb-Douglas: Grenzprodukte',
    r'<p>\(Y(L; K) = 80 \cdot L^{0{,}6} \cdot K^{0{,}4}\); L = 1.500 AE (Arbeit), K = 300 GE (Kapital).</p>', [
    teil('Berechnen und interpretieren Sie das partielle Grenzprodukt der Arbeit.', 3, 'Nach L ableiten, K konstant.', '48·(K/L)^0,4.', ol(r'\(\frac{\partial Y}{\partial L} = 48 L^{-0{,}4}K^{0{,}4} = 48 \cdot 0{,}2^{0{,}4}\)', f'≈ {d(gL)}: Eine Arbeitseinheit mehr erhöht den Output um etwa {d(gL)} Einheiten (K konstant).'), gL),
    teil('Berechnen und interpretieren Sie das partielle Grenzprodukt des Kapitals.', 3, 'Nach K ableiten.', '32·(L/K)^0,6.', ol(r'\(\frac{\partial Y}{\partial K} = 32 \cdot 5^{0{,}6}\)', f'≈ {d(gK)}: Eine Geldeinheit Kapital mehr erhöht den Output um etwa {d(gK)} Einheiten (L konstant).'), gK),
    teil('L steigt um 10 AE, K sinkt um 2 GE. Schätzen Sie die Output-Änderung mit dem totalen Differential.', 2, 'dY = Y_L·dL + Y_K·dK.', 'dK ist negativ.', ol(f'dY ≈ {d(gL)}·10 − {d(gK)}·2 ≈ {d(10 * gL - 2 * gK)}'), 10 * gL - 2 * gK)])

# 10 Folgen
aufgabe('folgen', ['folgen', 'grenzwert-folge', 'ungleichungen'], 'rechnen', 1, 'Zins, Abschreibung, Ungleichung',
    '<p>50.000 € werden 10 Jahre zu 5 % angelegt. Eine Maschine für 50.000 € wird linear in 10 Jahren auf 2.000 € abgeschrieben.</p>', [
    teil('Kontostand nach 10 Jahren?', 2, 'Geometrische Folge.', '50.000 · 1,05¹⁰.', ol('≈ 81.444,73 €'), 50000 * 1.05**10, '€'),
    teil('Restwert der Maschine nach 6 Jahren?', 2, 'Arithmetische Folge, d = −4.800.', '50.000 − 6 · 4.800.', ol('50.000 − 28.800 = 21.200 €'), 21200, '€'),
    teil(r'Bestimmen Sie \(\lim_{n\to\infty} \frac{3n^2 + 2n}{5n^2 - 1}\).', 2, 'Höchste Potenz ausklammern.', 'Gleicher Grad.', ol('3/5 = 0,6'), 0.6),
    teil(r'Ab welcher Laufzeit n übersteigt das Kapital 70.000 €? Lösen Sie \(50.000 \cdot 1{,}05^n > 70.000\).', 3, 'Durch 50.000 teilen, logarithmieren.', 'n > ln 1,4 / ln 1,05.', ol(r'\(1{,}05^n > 1{,}4 \Rightarrow n > \frac{\ln 1{,}4}{\ln 1{,}05} \approx 6{,}90\)', 'ab dem 7. Jahr'), 7, 'Jahre')], klausur=False)

import sys; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from aufgaben_uebung import ergaenze
ergaenze(aufgabe, teil, ol)   # Übungsblatt-Aufgaben aus dem Folienabgleich

ids = {t_['id'] for k in json.loads((ROOT / 'inhalte/wima/fach.json').read_text())['kapitel'] for t_ in k['themen']}
for a in A: assert set(a['unter']) <= ids, a['id']
kap = {k['id']: {t_['id'] for t_ in k['themen']} for k in json.loads((ROOT / 'inhalte/wima/fach.json').read_text())['kapitel']}
(ROOT / 'inhalte/wima/aufgaben.json').write_text(json.dumps({'hinweis': 'Große Aufgaben im Klausurstil, Zahlen mit sympy gerechnet.', 'aufgaben': A}, ensure_ascii=False, indent=1))
print(f'wima: {len(A)} große Aufgaben; Oberthemen ohne Aufgabe: {[k for k, s in kap.items() if not any(set(a["unter"]) & s for a in A)]}')
