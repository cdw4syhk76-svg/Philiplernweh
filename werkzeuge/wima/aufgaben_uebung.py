"""Übungsaufgaben der Blätter 1, 5, 7, 8, 9 und „Lineare Algebra“, die als einzelne Aufgaben noch fehlten (Folienabgleich).
Alle Ergebnisse werden hier mit sympy gerechnet. Wird von aufgaben.py importiert: ergaenze(aufgabe, teil, ol)."""
import sympy as sp

x, y, z, t, a, b, c, m = sp.symbols('x y z t a b c m')
n = sp.symbols('n', positive=True, integer=True)
def L(e): return sp.latex(e, mat_str='pmatrix', mat_delim='', ln_notation=True).replace(r'\log', r'\ln')


def M(*rows): return sp.Matrix(rows)


def ml(A): return r'\(' + L(A) + r'\)'


def ergaenze(aufgabe, teil, ol):
    # ------------------------------------------------ Blatt 1, Aufgabe 1: Terme vereinfachen
    terme = [
        (r'2ab \cdot 10ab \cdot 4bx \cdot 3abx', 2*a*b*10*a*b*4*b*x*3*a*b*x, 'Zahlen und gleiche Variablen getrennt multiplizieren (Assoziativgesetz).'),
        (r'ab \cdot (bc)', a*b*(b*c), 'Klammer weglassen, b · b = b².'),
        (r'(-3x) \cdot (ay)(-2xy)', (-3*x)*(a*y)*(-2*x*y), 'Minus mal Minus ergibt Plus.'),
        (r'(x + 2y)^2 - (2x - y)^2', sp.expand((x + 2*y)**2 - (2*x - y)**2), '1. und 2. binomische Formel, Klammer nach dem Minus beachten.'),
        (r'(ax + bx - cx) : x', sp.cancel((a*x + b*x - c*x) / x), 'x ausklammern und kürzen.'),
        (r'(ax \cdot bx \cdot cx) : x', sp.cancel((a*x*b*x*c*x) / x), 'x³ : x = x².'),
        (r'(4a + 3b - 5c) \cdot 7x - (5a - 4b + 6c) \cdot 3x', sp.factor(sp.expand((4*a + 3*b - 5*c)*7*x - (5*a - 4*b + 6*c)*3*x)), 'Ausmultiplizieren, zusammenfassen, x ausklammern.'),
        (r'\frac{-abc}{a-b} \cdot \frac{b-a}{(-b) \cdot c} \cdot \frac{1}{a}', sp.cancel((-a*b*c)/(a - b) * (b - a)/((-b)*c) * 1/a), 'b − a = −(a − b); dann alles kürzen.'),
        (r'\frac{2x+1}{x} + \frac{1}{2x} - \frac{x+5}{x^2}', sp.cancel((2*x + 1)/x + 1/(2*x) - (x + 5)/x**2), 'Hauptnenner 2x².'),
        (r'\frac{am + a}{m} : \frac{ax + ay}{x}', sp.factor(sp.cancel(((a*m + a)/m) / ((a*x + a*y)/x))), 'Durch einen Bruch teilen = mit dem Kehrwert malnehmen; a ausklammern und kürzen.'),
        (r'-x + \frac{x}{1 - \frac{2}{x-1}}', sp.factor(sp.cancel(-x + x/(1 - 2/(x - 1)))), 'Doppelbruch zuerst auflösen: 1 − 2/(x−1) = (x−3)/(x−1).'),
        (r'\frac{(a-b)^2 - c^2}{a - b - c}', sp.cancel(((a - b)**2 - c**2)/(a - b - c)), '3. binomische Formel: u² − v² = (u − v)(u + v).'),
        (r'\frac{-x^2 + 4x - 4}{x - 2}', sp.cancel((-x**2 + 4*x - 4)/(x - 2)), 'Zähler = −(x − 2)².'),
        (r'\frac{4x^2 - 9y^2}{16x^2 + 81y^2}', sp.cancel((4*x**2 - 9*y**2)/(16*x**2 + 81*y**2)), 'Der Nenner lässt sich nicht zerlegen (Summe von Quadraten): nicht weiter kürzbar.'),
    ]
    aufgabe('terme-blatt1', ['terme'], 'rechnen', 2, 'Terme vereinfachen und Brüche kürzen',
        '<p>Vereinfachen Sie die Ausdrücke so weit wie möglich (Brüche so weit wie möglich kürzen).</p>',
        [teil(r'\(' + tx + r' =\)', 1, tip, 'Erst ordnen, dann zusammenfassen bzw. kürzen.', ol(r'\(' + L(erg) + r'\)')) for tx, erg, tip in terme]
        + [teil(r'\(\sqrt{x \cdot \sqrt{x \cdot \sqrt{x \cdot \sqrt{x}}}} =\)', 2, 'Wurzeln als Potenzen schreiben, von innen nach außen.', 'Exponenten: 1/2 + 1/4 + 1/8 + 1/16.',
                ol(r'\(x^{\frac12} \cdot x^{\frac14} \cdot x^{\frac18} \cdot x^{\frac1{16}} = x^{' + L(sp.Rational(1, 2) + sp.Rational(1, 4) + sp.Rational(1, 8) + sp.Rational(1, 16)) + r'}\)')),
           teil(r'\(-(a - x)(b - y)(c - z) =\)', 1, 'Lohnt sich Ausmultiplizieren?', 'Nein.', ol('Das ist bereits die einfachste Form; Ausmultiplizieren macht die Darstellung nur länger.'))])

    # ------------------------------------------------ Blatt 1, Aufgabe 2: Grenzwerte von Folgen
    folgen = [(r'\frac{(-1)^n}{\sqrt{n}}', sp.Integer(0) * n, r'Betrag \(\frac{1}{\sqrt n} \to 0\); ε-Kriterium: wähle \(N(\varepsilon) > \frac{1}{\varepsilon^2}\).'),
              (r'\frac{4}{5n - 3}', 4/(5*n - 3), 'Zähler konstant, Nenner wächst.'),
              (r'\frac{4 + 2n + n^2}{n^3}', (4 + 2*n + n**2)/n**3, 'Höchste Potenz im Nenner ist größer: Grenzwert 0.'),
              (r'\frac{2n^4 - 3n^2 + 7}{n^4 + n^3 - 4n}', (2*n**4 - 3*n**2 + 7)/(n**4 + n**3 - 4*n), r'Gleicher Grad: Quotient der Leitkoeffizienten \(\frac{2}{1}\).'),
              (r'\frac{1}{\sqrt{n + 1}}', 1/sp.sqrt(n + 1), r'ε-Kriterium: wähle \(N(\varepsilon) > \frac{1}{\varepsilon^2}\).')]
    aufgabe('folgen-blatt1', ['grenzwert-folge', 'folgen'], 'rechnen', 2, 'Konvergenz von Folgen nachweisen',
        r'<p>Zeigen Sie, dass die Folgen konvergieren, und bestimmen Sie den Grenzwert (\(n \in \mathbb{N}\)). Bei i. und v. mit dem ε-Kriterium.</p>',
        [teil(r'\(a_n = ' + tx + r'\)', 2, 'Höchste Potenz von n ausklammern.', tip, ol(tip, r'\(\lim_{n\to\infty} a_n = ' + L(sp.limit(e, n, sp.oo)) + r'\)'), sp.limit(e, n, sp.oo)) for tx, e, tip in folgen]
        + [teil('Geben Sie je ein Beispiel an: (i) eine durch M = 2 beschränkte Folge, (ii) eine durch k = 0 nach oben beschränkte, nach unten unbeschränkte Folge, (iii) eine durch k = 0 nach unten beschränkte, nach oben unbeschränkte Folge.', 3,
                'Beschränkt heißt |aₙ| ≤ M für alle n.', 'Denken Sie an (−1)ⁿ, −n und n.',
                ol(r'(i) \(a_n = 2 \cdot (-1)^n\) oder \(a_n = \frac{1}{n}\)', r'(ii) \(a_n = -n\)', r'(iii) \(a_n = n\)'))])

    # ------------------------------------------------ Blatt 5: Differentialquotient, Ableitungen, Polynomdivision
    h = sp.symbols('h')
    abl = [(r'f(x) = \frac{e^{2x^2}}{\cos(x)}', sp.exp(2*x**2)/sp.cos(x), x, r"\frac{e^{2x^2}\,(4x\cos x + \sin x)}{\cos^2 x}", (sp.exp(2*x**2)*(4*x*sp.cos(x) + sp.sin(x)))/sp.cos(x)**2, 'Quotientenregel; Zähler mit Kettenregel.'),
           (r'f(x) = e^{\frac{1}{x^2}} \cdot \sin(4x + 1)', sp.exp(1/x**2)*sp.sin(4*x + 1), x, r"e^{\frac{1}{x^2}}\left(-\frac{2}{x^3}\sin(4x+1) + 4\cos(4x+1)\right)", sp.exp(1/x**2)*(-2/x**3*sp.sin(4*x + 1) + 4*sp.cos(4*x + 1)), 'Produktregel, beide Faktoren verkettet.'),
           (r'h(t) = (5t + 3)^3', (5*t + 3)**3, t, r"15\,(5t + 3)^2", 15*(5*t + 3)**2, 'Kettenregel: äußere mal innere Ableitung.'),
           (r'\tan(x) = \frac{\sin(x)}{\cos(x)}', sp.sin(x)/sp.cos(x), x, r"\frac{\cos^2 x + \sin^2 x}{\cos^2 x} = \frac{1}{\cos^2 x}", 1/sp.cos(x)**2, 'Quotientenregel, sin² + cos² = 1.'),
           (r'f(x) = \frac{2x + 9}{4x - 7}', (2*x + 9)/(4*x - 7), x, r"\frac{2(4x-7) - 4(2x+9)}{(4x-7)^2} = -\frac{50}{(4x - 7)^2}", -50/(4*x - 7)**2, 'Quotientenregel.'),
           (r'g(x) = \frac{\sin(x)}{x}', sp.sin(x)/x, x, r"\frac{x\cos x - \sin x}{x^2}", (x*sp.cos(x) - sp.sin(x))/x**2, 'Quotientenregel.'),
           (r'h(t) = t \cdot \cos\left(t - \frac{\pi}{6}\right)', t*sp.cos(t - sp.pi/6), t, r"\cos\left(t - \frac{\pi}{6}\right) - t\,\sin\left(t - \frac{\pi}{6}\right)", sp.cos(t - sp.pi/6) - t*sp.sin(t - sp.pi/6), 'Produktregel.'),
           (r'f(x) = x^2 \cdot \sqrt{x}', x**2*sp.sqrt(x), x, r"\frac{5}{2}\,x^{\frac{3}{2}} = \frac{5}{2}\,x\sqrt{x}", sp.Rational(5, 2)*x**sp.Rational(3, 2), r'Als Potenz schreiben: \(x^{5/2}\).'),
           (r'f(x) = \left(\sqrt{x} + x\right)^5', (sp.sqrt(x) + x)**5, x, r"5\left(\sqrt{x} + x\right)^4 \cdot \left(\frac{1}{2\sqrt{x}} + 1\right)", 5*(sp.sqrt(x) + x)**4*(1/(2*sp.sqrt(x)) + 1), 'Kettenregel.'),
           (r'f(x) = \frac{1}{\sqrt{x^2 + 5}}', 1/sp.sqrt(x**2 + 5), x, r"-\frac{x}{(x^2 + 5)^{\frac{3}{2}}}", -x/(x**2 + 5)**sp.Rational(3, 2), r'Als \((x^2+5)^{-1/2}\) schreiben, Kettenregel.')]
    pol = [(r'(x^3 - 12x^2 + 5x + 150) : (x - 5)', x**3 - 12*x**2 + 5*x + 150, x - 5),
           (r'(7x^5 - 2x^4 - 63x^3 + 33x^2 - 135) : (x^2 - 9)', 7*x**5 - 2*x**4 - 63*x**3 + 33*x**2 - 135, x**2 - 9),
           (r'(4x^5 - x^4 + 2x^3 + x^2 - 1) : (x^2 + 1)', 4*x**5 - x**4 + 2*x**3 + x**2 - 1, x**2 + 1)]
    teile = [teil(r'Zeigen Sie mit dem Differentialquotienten, dass \(f(x) = x^2\) differenzierbar ist, und bestimmen Sie \(f\'(x)\).', 2, r'\(\lim_{h\to0}\frac{f(x+h)-f(x)}{h}\)', r'\((x+h)^2 = x^2 + 2xh + h^2\)',
                  ol(r'\(\frac{(x+h)^2 - x^2}{h} = \frac{2xh + h^2}{h} = 2x + h\)', r'\(h \to 0\): \(f\'(x) = 2x\)')),
             teil(r'Ebenso für \(f(x) = \frac{1}{x}\), \(x \neq 0\).', 2, 'Brüche im Zähler auf den Hauptnenner bringen.', r'\(\frac{1}{x+h} - \frac{1}{x} = \frac{-h}{x(x+h)}\)',
                  ol(r'\(\frac{\frac{1}{x+h} - \frac{1}{x}}{h} = \frac{-1}{x(x+h)}\)', r'\(h \to 0\): \(f\'(x) = -\frac{1}{x^2}\)'))]
    for tx, f, v, anz, wert, tip in abl:
        assert sp.simplify(sp.diff(f, v) - wert) == 0, tx
        teile.append(teil(r'\(' + tx + r'\)', 2, tip, 'Erst die Regel wählen, dann Schritt für Schritt ableiten.', ol(r'\(' + ({'g': "g'", 'h': "h'", '\\': "\\tan'"}.get(tx[0], "f'")) + '(' + str(v) + ') = ' + anz + r'\)')))
    for tx, p, q in pol:
        qu, r = sp.div(p, q, x)
        teile.append(teil(r'\(' + tx + r'\)', 2, 'Höchste Potenz durch höchste Potenz teilen, zurückmultiplizieren, abziehen, wiederholen.', 'Fehlende Potenzen mit 0 auffüllen.',
                          ol(r'\(= ' + L(qu) + (r' + \frac{' + L(r) + '}{' + L(q) + '}' if r != 0 else '') + r'\)', 'Rest: ' + r'\(' + L(r) + r'\)')))
    aufgabe('blatt5', ['differentialquotient', 'ableitungsregeln', 'produkt-quotient', 'kettenregel', 'lhospital'], 'rechnen', 2, 'Differentialquotient, Ableitungsregeln, Polynomdivision',
            '<p>Übungsaufgaben zur Differentialrechnung.</p>', teile)

    # ------------------------------------------------ Lineare Algebra
    A1, B1, C1 = M([1, 2, 3], [0, 3, -1], [-4, 1, 0]), M([2, 2, 1], [-1, 0, 4]), M([3, 4, 6], [1, 3, -9], [-2, 0, 5])
    def prod(P, Q):
        return ml(P * Q) if P.shape[1] == Q.shape[0] else 'nicht definiert (Spaltenzahl ≠ Zeilenzahl)'
    aus_la = r'<p>Gegeben \(A = ' + L(A1) + r'\), \(B = ' + L(B1) + r'\), \(C = ' + L(C1) + r'\).</p>'
    teile = [teil('Berechnen Sie ' + nm + ' (Matrizen A, B, C aus Aufgabe 1).', 1, 'Zeile mal Spalte; Format prüfen.', 'Aᵀ: Zeilen werden Spalten.', ol(erg))
             for nm, erg in [('A·B', prod(A1, B1)), ('B·A', prod(B1, A1)), (r'\(A^T \cdot B\)', prod(A1.T, B1)), (r'\(A \cdot B^T\)', prod(A1, B1.T)),
                             (r'\(A^2\)', ml(A1 * A1)), (r'\(B^2\)', prod(B1, B1)), (r'\((B^T)^2\)', prod(B1.T, B1.T)), ('A − C', ml(A1 - C1))]]
    for P, Q in [(M([1, 5, 7], [3, -2, 1], [0, 2, 6]), M([1, 0], [2, 2], [-1, 5])), (M([2, 3, 7], [4, 1, -8]), M([1, 3, -2], [2, 7, 0])), (M([1, 5, 7], [3, -2, 1]), M([2, 1], [6, -1], [8, 0]))]:
        teile.append(teil(r'Multiplizieren Sie, sofern möglich: \(' + L(P) + r' \cdot ' + L(Q) + r'\)', 2, 'Spaltenzahl von A = Zeilenzahl von B?', 'Ergebnisformat: Zeilen von A × Spalten von B.', ol(prod(P, Q))))
    va, vb, vc, ziel = M([2], [0], [1]), M([3], [0], [0]), M([-3], [1], [5]), M([1], [4], [-2])
    V = va.row_join(vb).row_join(vc); koef = V.solve(ziel)
    teile.append(teil(r'Zeigen Sie, dass \(a = (2\ 0\ 1)\), \(b = (3\ 0\ 0)\), \(c = (-3\ 1\ 5)\) linear unabhängig sind, und stellen Sie \((1\ 4\ -2)\) als Linearkombination dar.', 4,
                      'Determinante der Matrix aus den drei Vektoren ≠ 0 ⇒ linear unabhängig.', 'Dann das LGS λ₁a + λ₂b + λ₃c = (1 4 −2) lösen.',
                      ol(r'\(\det(a\ b\ c) = ' + L(V.det()) + r' \neq 0\) ⇒ linear unabhängig', r'\(\lambda_1 = ' + L(koef[0]) + r',\ \lambda_2 = ' + L(koef[1]) + r',\ \lambda_3 = ' + L(koef[2]) + r'\)')))
    for nm, D_ in [('A', M([1, 5, 7], [3, -2, 1], [0, 2, 6])), ('B', M([1, 2, 3], [0, 3, -1], [-4, 1, 0])), ('C', M([3, 5], [7, 4])), ('D', M([1, 0, 3, 2], [4, 2, 0, 5], [3, 6, 1, 2], [4, 1, 2, 7]))]:
        teile.append(teil(r'Berechnen Sie \(\det ' + nm + r'\) für \(' + nm + ' = ' + L(D_) + r'\).', 2 if D_.shape[0] < 4 else 4,
                          '2×2: ad − bc; 3×3: Sarrus.' if D_.shape[0] < 4 else 'Entwicklung nach einer Zeile/Spalte mit vielen Nullen (Laplace) oder Gauß bis zur Dreiecksform.', 'Vorzeichen-Schachbrett beachten.',
                          ol(r'\(\det ' + nm + ' = ' + L(D_.det()) + r'\)'), D_.det()))
    for A_, b_ in [(M([1, 2, -1], [2, 5, 2], [1, 1, 1]), M([1], [4], [5])), (M([2, -2, -1], [1, -1, 2], [1, 1, 3]), M([8], [7], [-3]))]:
        teile.append(teil(r'Zeigen Sie, dass \(A x = b\) mit \(A = ' + L(A_) + r'\), \(b = ' + L(b_) + r'\) eindeutig lösbar ist, und lösen Sie es mit der inversen Matrix.', 5,
                          r'Eindeutig lösbar ⇔ \(\det A \neq 0\).', r'\(x = A^{-1} b\); Inverse mit Gauß-Jordan (A | E).',
                          ol(r'\(\det A = ' + L(A_.det()) + r' \neq 0\)', r'\(A^{-1} = ' + L(A_.inv()) + r'\)', r'\(x = A^{-1} b = ' + L(A_.inv() * b_) + r'\)')))
    aufgabe('lineare-algebra', ['matrizen', 'matrizenmultiplikation', 'vektoren', 'determinante', 'inverse-matrix', 'lgs-gauss'], 'rechnen', 3, 'Übungsaufgaben lineare Algebra',
            '<p>Matrizenrechnung, lineare Unabhängigkeit, Determinanten und lineare Gleichungssysteme.</p>' + aus_la, teile)

    # ------------------------------------------------ Blatt 7 A2, Blatt 8 A3/A4: Zeilenstufenform und Inverse
    Z = M([1, 0, 3, 2, 1], [4, 2, 0, 5, 3], [3, 6, 1, 2, 2], [4, 1, 2, 7, 2])
    E, _ = Z.echelon_form(), None
    teile = [teil(r'Bringen Sie \(' + L(Z) + r'\) mit dem Gauß’schen Eliminationsverfahren auf Zeilenstufenform.', 4, 'Mit Zeile 1 die erste Spalte unten auf 0 bringen.', 'Dann mit Zeile 2 die zweite Spalte, usw. Die Stufenform ist nicht eindeutig.',
                  ol(r'eine mögliche Zeilenstufenform: \(' + L(E) + r'\)', r'Rang = ' + str(Z.rank())))]
    for nm, A_ in [('A', M([1, 2, -1], [2, 4, 2], [1, 1, 1])), ('B', M([1, 2, -1], [2, 4, 2], [-4, -8, -8])), ('C', M([1, 0, 1], [3, 5, 2], [0, 4, 1]))]:
        d_ = A_.det()
        teile.append(teil(r'Invertieren Sie \(' + nm + ' = ' + L(A_) + r'\), sofern möglich.', 4, r'Erst \(\det\) prüfen: = 0 ⇒ keine Inverse.', 'Gauß-Jordan: (A | E) → (E | A⁻¹).',
                          ol(r'\(\det ' + nm + ' = ' + L(d_) + r'\)', (r'\(' + nm + r'^{-1} = ' + L(A_.inv()) + r'\)') if d_ != 0 else 'keine Inverse (singulär)')))
    D1, b1 = M([1, 4, 3], [2, 5, 4], [1, -3, -2]), M([1], [4], [5])
    teile.append(teil(r'Lösen Sie \(D x = b\) mit \(D = ' + L(D1) + r'\), \(b = ' + L(b1) + r'\) mit der inversen Matrix.', 5, r'\(\det D \neq 0\) zeigen.', r'\(x = D^{-1} b\).',
                      ol(r'\(\det D = ' + L(D1.det()) + r'\)', r'\(D^{-1} = ' + L(D1.inv()) + r'\)', r'\(x = ' + L(D1.inv() * b1) + r'\)')))
    aufgabe('blatt7-8', ['lgs-gauss', 'inverse-matrix', 'determinante'], 'rechnen', 3, 'Zeilenstufenform und inverse Matrizen',
            '<p>Gauß-Verfahren und Matrizeninversion.</p>', teile)

    # ------------------------------------------------ Blatt 9 A1: partielle Ableitungen und totales Differential
    fs = [(r'f(x,y) = (xy)^3 + xy^2', (x*y)**3 + x*y**2, [x, y]),
          (r'f(x,y) = \frac{x^4 - 3x^2 y}{3x + 2y^2}', (x**4 - 3*x**2*y)/(3*x + 2*y**2), [x, y]),
          (r'f(x,y) = e^{x + y^2} \cdot \sin(x \cdot 2y)', sp.exp(x + y**2)*sp.sin(2*x*y), [x, y]),
          (r'f(x,y,z) = e^{x + z^2} \cdot 2y^3', sp.exp(x + z**2)*2*y**3, [x, y, z]),
          (r'g(x,y,z) = (z \cdot \ln(z) + x^3) \cdot \sqrt{2y}', (z*sp.log(z) + x**3)*sp.sqrt(2*y), [x, y, z])]
    teile = []
    for tx, f, vs in fs:
        ds = [sp.factor(sp.cancel(sp.diff(f, v))) for v in vs]
        fn = tx[0]
        teile.append(teil(r'\(' + tx + r'\)', 4, 'Nach einer Variablen ableiten, die anderen wie Konstanten behandeln.', r'Totales Differential: \(df = f_x\,dx + f_y\,dy\,(+ f_z\,dz)\).',
                          ol(*[r'\(' + fn + '_{' + str(v) + '} = ' + L(dv) + r'\)' for v, dv in zip(vs, ds)], r'\(d' + fn + ' = ' + ' + '.join(r'\left(' + L(dv) + r'\right) d' + str(v) for v, dv in zip(vs, ds)) + r'\)')))
    aufgabe('blatt9', ['partielle-ableitung', 'totales-differential'], 'rechnen', 3, 'Partielle Ableitungen und totales Differential',
            '<p>Bestimmen Sie die partiellen Ableitungen und das totale Differential mit den Inputänderungen dx, dy (und dz).</p>', teile)
