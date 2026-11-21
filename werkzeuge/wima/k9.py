import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *
import sympy as sp

L, K, x, y = sp.symbols('L K x y', positive=True)
Y1 = 80 * L**sp.Rational(3, 5) * K**sp.Rational(2, 5)
gL, gK = [float(sp.diff(Y1, v).subs({L: 1500, K: 300})) for v in (L, K)]
assert abs(gL - 25.2147) < 1e-3 and abs(gK - 84.0489) < 1e-3
Y2 = 90 * L**sp.Rational(4, 5) * K**sp.Rational(1, 5)
g2L, g2K = [float(sp.diff(Y2, v).subs({L: 1000, K: 200})) for v in (L, K)]
assert abs(g2L - 52.1841) < 1e-3 and abs(g2K - 65.2302) < 1e-3
F = (x * y)**3 + x * y**2
assert sp.diff(F, x) == 3 * x**2 * y**3 + y**2 and sp.diff(F, y) == 3 * x**3 * y**2 + 2 * x * y
d = lambda v, n=2: f'{v:.{n}f}'.replace('.', ',')

# ---------------------------------------------------------------- 1 Partielle Ableitungen
t_part = thema('partielle-ableitung', 'Funktionen mehrerer Veränderlicher und partielle Ableitungen', star=True,
    kern='Bei f(x, y) leitet man partiell nach einer Variablen ab, indem man alle anderen wie Konstanten behandelt: f_x = ∂f/∂x, f_y = ∂f/∂y. Alle Ableitungsregeln gelten weiter. Der Gradient fasst die partiellen Ableitungen zusammen: grad f = (f_x, f_y).',
    kurz=p('Der Output einer Fabrik hängt von Arbeit L <b>und</b> Kapital K ab: \\(Y(L, K)\\). Wie ändert sich Y, wenn nur L steigt und K gleich bleibt? Das beantwortet die <b>partielle Ableitung</b> nach L.')
        + p('Der Trick: Beim Ableiten nach x ist y einfach eine Zahl, wie eine 5. Dann gelten alle bekannten Regeln.'),
    fig=fw('Nach x ableiten heißt: y einfrieren. Tippe auf die Kästen.')
        + bild(svg(360, 200, box(4, 4, 352, 52, 'f(x, y) = (xy)³ + xy²', size=16, tip='Übungsblatt 9, Aufgabe 1 i.')
                   + box(4, 70, 172, 126, 'nach x\n(y konstant)\n\nf_x = 3x²y³ + y²', size=13, art='hl', tip='(xy)³ = x³y³ → 3x²y³; xy² → y² (y² ist ein konstanter Faktor).')
                   + box(184, 70, 172, 126, 'nach y\n(x konstant)\n\nf_y = 3x³y² + 2xy', size=13, tip='x³y³ → 3x³y²; xy² → 2xy.'), 'Partielle Ableitung', maxw=420)),
    figcap='nach Übungsblatt 9, Aufgabe 1',
    article=h3('Vorgehen')
        + fluss([('Variable wählen', 'nach welcher ableiten?'), ('Rest einfrieren', 'andere Variablen = Konstanten'), ('Regeln anwenden', 'Potenz, Produkt, Kette')], hl=1)
        + bsp('Übungsblatt 9, Aufgabe 1 i', r'\(f(x, y) = (xy)^3 + xy^2\)', [(r'\(f_x = 3x^2y^3 + y^2\)', ''), (r'\(f_y = 3x^3y^2 + 2xy\)', '')])
        + bsp('Übungsblatt 9, Aufgabe 1 iii (Kettenregel)', r'\(f(x, y) = e^{x + y^2} \cdot \sin(2xy)\)',
              [(r'\(f_x = e^{x+y^2}\sin(2xy) + e^{x+y^2} \cdot 2y\cos(2xy)\)', 'Produktregel'), (r'\(f_y = 2y\,e^{x+y^2}\sin(2xy) + e^{x+y^2} \cdot 2x\cos(2xy)\)', '')])
        + h3('Gradient und höhere Ableitungen')
        + p('Der <b>Gradient</b> \\(\\nabla f = (f_x, f_y)\\) zeigt in die Richtung des steilsten Anstiegs. Leitet man partielle Ableitungen nochmals ab, erhält man die zweiten Ableitungen \\(f_{xx}, f_{xy}, f_{yx}, f_{yy}\\); zusammen bilden sie die <b>Hesse-Matrix</b> \\(H = \\begin{pmatrix} f_{xx} & f_{xy} \\\\ f_{yx} & f_{yy} \\end{pmatrix}\\) (bei stetigen zweiten Ableitungen symmetrisch, \\(f_{xy} = f_{yx}\\)).')
        + p('<b>Stetig partiell differenzierbar</b> heißt: Alle partiellen Ableitungen existieren und sind selbst stetige Funktionen. Dann ist f (total) differenzierbar, das totale Differential ist eine gute Näherung, und bei zweimal stetig partiell differenzierbaren Funktionen sind die gemischten Ableitungen gleich (Satz von Schwarz).')
        + bsp('Paraboloid', r'\\(f(x, y) = x^2 + y^2\\): eine nach oben geöffnete „Schüssel“ mit Tiefpunkt in (0, 0).',
              [(r'\\(f_x = 2x,\\ f_y = 2y\\)', r'\\(\\nabla f(1, 2) = (2, 4)\\)'), (r'\\(f_{xx} = 2,\\ f_{yy} = 2,\\ f_{xy} = f_{yx} = 0\\)', r'\\(H = \\begin{pmatrix} 2 & 0 \\\\ 0 & 2 \\end{pmatrix}\\)')],
              'Die Hesse-Matrix ist symmetrisch; hier ist sie zudem positiv definit (beide Hauptdiagonal-Einträge positiv, det H = 4 > 0) – das passt zum Minimum der Schüssel.')
        + p('<b>Eigenschaften der Hesse-Matrix:</b> quadratisch (n × n bei n Variablen), bei zweimal stetig partiell differenzierbarem f symmetrisch; ihr Vorzeichenverhalten (Definitheit) zeigt die Krümmung: positiv definit → Minimum, negativ definit → Maximum, indefinit → Sattelpunkt (wenn der Gradient null ist).')
        + wahr('w-part', [('Beim partiellen Ableiten nach x wird y wie eine Konstante behandelt.', True, 'Kern der Methode.'), (r'Für \(f = x^2y\) gilt \(f_y = 2xy\).', False, 'f_y = x².'),
                          ('Der Gradient enthält alle partiellen Ableitungen erster Ordnung.', True, '(f_x, f_y).')]),
    merk='Partiell nach x: alle anderen Variablen als Konstanten behandeln, Regeln wie gewohnt. Gradient ∇f = (f_x, f_y). Zweite Ableitungen → Hesse-Matrix (symmetrisch).',
    exam='Partielle Ableitungen bilden (jede Klausur, meist an einer Produktionsfunktion).',
    fehler=['Die andere Variable mit ableiten.', 'Bei Produkten in einer Variablen die Produktregel vergessen.'],
    src='Übungsblatt 9, A1; Gliederung 8')

# ---------------------------------------------------------------- 2 Grenzprodukte Cobb-Douglas
t_gp = thema('grenzprodukt', 'Partielle Grenzprodukte (Cobb-Douglas) berechnen und interpretieren', star=True,
    kern='Für eine Produktionsfunktion Y(L, K) = c·L^a·K^b sind die partiellen Grenzprodukte ∂Y/∂L = a·c·L^(a−1)·K^b (Grenzprodukt der Arbeit) und ∂Y/∂K = b·c·L^a·K^(b−1) (Grenzprodukt des Kapitals). Interpretation: Steigt L um eine Einheit (K konstant), steigt der Output um etwa ∂Y/∂L Einheiten (Partialanalyse, ceteris paribus).',
    kurz=p('\\(Y(L, K) = 80 \\cdot L^{0{,}6} \\cdot K^{0{,}4}\\) mit L = 1.500 Arbeitseinheiten und K = 300 Geldeinheiten. Was bringt eine zusätzliche Arbeitseinheit? Das ist das <b>Grenzprodukt der Arbeit</b> \\(\\frac{\\partial Y}{\\partial L}\\).')
        + p('Diese Aufgabe ist sehr häufig gefragt. Wichtig sind beide Teile: <b>berechnen</b> und <b>interpretieren</b>.'),
    fig=fw('Das Rechenschema. Tippe auf die Kästen.')
        + bild(svg(360, 230, box(4, 4, 352, 50, 'Y(L, K) = 80 · L^0,6 · K^0,4;  L = 1.500, K = 300', size=13, tip='Cobb-Douglas-Produktionsfunktion, ein typisches Klausurbeispiel.')
                   + box(4, 66, 172, 160, '∂Y/∂L\n= 48 · L^(−0,4) · K^0,4\n= 48 · (K/L)^0,4\n= 48 · 0,2^0,4\n≈ ' + d(gL), size=12, art='hl', tip=f'Grenzprodukt der Arbeit: Eine Arbeitseinheit mehr bringt etwa {d(gL)} Outputeinheiten mehr (K konstant).')
                   + box(184, 66, 172, 160, '∂Y/∂K\n= 32 · L^0,6 · K^(−0,6)\n= 32 · (L/K)^0,6\n= 32 · 5^0,6\n≈ ' + d(gK), size=12, tip=f'Grenzprodukt des Kapitals: Eine Geldeinheit Kapital mehr bringt etwa {d(gK)} Outputeinheiten mehr (L konstant).'),
                   'Grenzprodukte', maxw=420)),
    figcap='nach der Klausuraufgabe Y(L; K) und Übungsblatt 9, Aufgabe 2',
    article=h3('Formeln')
        + fx('Partielle Grenzprodukte (Cobb-Douglas)', r'\frac{\partial Y}{\partial L} = a \cdot c \cdot L^{a-1} K^{b}, \qquad \frac{\partial Y}{\partial K} = b \cdot c \cdot L^{a} K^{b-1}', 'Exponent nach vorn, Exponent minus 1, die andere Variable bleibt stehen.',
             r'\(Y = 80L^{0{,}6}K^{0{,}4}\): \(\frac{\partial Y}{\partial L} = 48 L^{-0{,}4}K^{0{,}4} = 48\left(\frac{K}{L}\right)^{0{,}4}\)')
        + bsp('Klausurstil', r'\(Y(L; K) = 80 \cdot L^{0{,}6} \cdot K^{0{,}4}\), \(L = 1.500\) AE, \(K = 300\) GE',
              [(r'\(\frac{\partial Y}{\partial L} = 48 \cdot \left(\frac{300}{1.500}\right)^{0{,}4} = 48 \cdot 0{,}2^{0{,}4}\)', r'\(\approx ' + d(gL).replace(',', '{,}') + r'\)'),
               (r'\(\frac{\partial Y}{\partial K} = 32 \cdot \left(\frac{1.500}{300}\right)^{0{,}6} = 32 \cdot 5^{0{,}6}\)', r'\(\approx ' + d(gK).replace(',', '{,}') + r'\)'),
               ('Interpretation', f'Eine zusätzliche Arbeitseinheit erhöht den Output um etwa {d(gL)} Einheiten, eine zusätzliche Geldeinheit Kapital um etwa {d(gK)} Einheiten, jeweils wenn der andere Faktor konstant bleibt.')],
              'Tipp: L^(a−1)·K^b als (K/L)^(1−a) schreiben, dann sind die Zahlen einfacher.')
        + bsp('Klausurstil', r'\(Y(L; K) = 90 \cdot L^{0{,}8} \cdot K^{0{,}2}\), \(L = 1.000\) AE, \(K = 200\) GE',
              [(r'\(\frac{\partial Y}{\partial L} = 72 \cdot 0{,}2^{0{,}2}\)', r'\(\approx ' + d(g2L).replace(',', '{,}') + r'\)'), (r'\(\frac{\partial Y}{\partial K} = 18 \cdot 5^{0{,}8}\)', r'\(\approx ' + d(g2K).replace(',', '{,}') + r'\)')])
        + klausur_hinweis('„Bestimmen und interpretieren Sie die partiellen Grenzprodukte der Arbeit und des Kapitals“ ist sehr häufig gefragt. Ohne Interpretation fehlen Punkte.')
        + wahr('w-gp', [(r'Bei \(Y = 80L^{0{,}6}K^{0{,}4}\) ist \(\frac{\partial Y}{\partial L} = 48L^{-0{,}4}K^{0{,}4}\).', True, '0,6 · 80 = 48.'),
                        ('Das Grenzprodukt der Arbeit gibt an, wie sich Y ändert, wenn L und K steigen.', False, 'Nur L steigt, K bleibt konstant.'),
                        ('Bei a < 1 sinkt das Grenzprodukt der Arbeit, wenn L wächst.', True, 'L^(a−1) fällt.')]),
    merk='Y = c·L^a·K^b: ∂Y/∂L = a·c·L^(a−1)K^b = a·c·(K/L)^(1−a); ∂Y/∂K = b·c·L^a·K^(b−1) = b·c·(L/K)^(1−b). Interpretation: Output-Änderung pro zusätzlicher Einheit eines Faktors, der andere konstant.',
    exam='Grenzprodukte an einer Stelle (L, K) berechnen und interpretieren (jede Klausur).',
    fehler=['Interpretation vergessen.', 'Exponenten falsch reduzieren (0,6 − 1 = −0,4).'],
    src='Übungsblatt 9 A2')

# ---------------------------------------------------------------- 3 Totales Differential
t_tot = thema('totales-differential', 'Totales Differential',
    kern='Das totale Differential schätzt die Änderung einer Funktion mehrerer Variablen bei kleinen gleichzeitigen Änderungen: df = f_x·dx + f_y·dy (+ f_z·dz). Ökonomisch: totale Output-Änderung = Summe der partiellen Grenzprodukte mal Inputänderungen.',
    kurz=p('Was passiert, wenn man gleichzeitig mehr Arbeit einsetzt und weniger Kapital? Man addiert die Effekte: Grenzprodukt der Arbeit mal Änderung der Arbeit plus Grenzprodukt des Kapitals mal Änderung des Kapitals. Das ist das <b>totale Differential</b>.'),
    fig=fw('Teilwirkungen addieren. Tippe auf die Kästen.')
        + bild(svg(360, 170, box(4, 4, 112, 80, 'f_x · dx', size=15, tip='Wirkung der Änderung von x allein.') + T(124, 50, '+', 18, 800) + box(132, 4, 112, 80, 'f_y · dy', size=15, tip='Wirkung der Änderung von y allein.')
                   + T(252, 50, '=', 18, 800) + box(260, 4, 96, 80, 'df', size=16, art='hl', tip='Geschätzte Gesamtänderung von f.')
                   + box(4, 98, 352, 68, 'Blatt 9, A2: r₁ + 0,2; r₂ − 0,1; r₃ − 0,1\n→ df ≈ 0,345·0,2 − 0,314·0,1 − 0,161·0,1 ≈ 0,021', size=12, tip='Partielle Grenzprodukte bei (4; 5; 9): 0,3446; 0,3141; 0,1607. Die Gesamtänderung ist leicht positiv.'), 'Totales Differential', maxw=420)),
    figcap='nach Übungsblatt 9, Aufgaben 1 und 2',
    article=h3('Formel')
        + fx('Totales Differential', r'df = \frac{\partial f}{\partial x}\,dx + \frac{\partial f}{\partial y}\,dy + \frac{\partial f}{\partial z}\,dz', 'Jede partielle Ableitung mal die Änderung ihrer Variablen, alles addieren.',
             r'\(f = (xy)^3 + xy^2\): \(df = (3x^2y^3 + y^2)\,dx + (3x^3y^2 + 2xy)\,dy\)')
        + bsp('Übungsblatt 9, Aufgabe 2', r'\(f(r_1, r_2, r_3) = 0{,}5r_1^{0{,}5}r_2^{0{,}5} + 0{,}1r_1^{0{,}4}r_3^{0{,}6} + 0{,}2r_2^{0{,}3}r_3^{0{,}7}\) bei \((4; 5; 9)\); \(dr_1 = 0{,}2,\ dr_2 = dr_3 = -0{,}1\)',
              [(r'partielle Grenzprodukte: \(f_{r_1} \approx 0{,}3446,\ f_{r_2} \approx 0{,}3141,\ f_{r_3} \approx 0{,}1607\)', ''),
               (r'\(df \approx 0{,}3446 \cdot 0{,}2 - 0{,}3141 \cdot 0{,}1 - 0{,}1607 \cdot 0{,}1\)', r'\(\approx 0{,}0214\)')], 'Der Output steigt also leicht, obwohl zwei Inputs sinken.')
        + wahr('w-tot', [('Das totale Differential addiert die partiellen Wirkungen.', True, 'df = f_x dx + f_y dy.'), ('Das totale Differential gilt exakt für große Änderungen.', False, 'Es ist eine Näherung für kleine Änderungen.')]),
    merk='df = f_x·dx + f_y·dy (+ f_z·dz): Näherung der Gesamtänderung bei kleinen gleichzeitigen Änderungen; Summe aus partiellen Grenzprodukten mal Inputänderungen.',
    exam='Übungsstoff (Blatt 9); in der Klausur selten.',
    fehler=['Vorzeichen der Inputänderungen vergessen.'],
    src='Übungsblatt 9')

KAPITEL = kapitel('k9', 'Analysis II: Funktionen mehrerer Veränderlicher',
    'Partielle Ableitungen, Grenzprodukte einer Produktionsfunktion und das totale Differential.',
    ['partielle Ableitung', 'Grenzprodukte', 'totales Differential'], [t_part, t_gp, t_tot])
