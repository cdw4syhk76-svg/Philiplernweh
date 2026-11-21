import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *
import sympy as sp

A = sp.Matrix([[4, 3, 3], [2, 4, 6], [1, 7, 4], [3, 3, 0]]); B = sp.Matrix([[6, 5], [4, 3], [1, 2]])
C = sp.Matrix([[2, 3, 4], [1, 3, 5], [2, 4, 6]]); D = sp.Matrix([[1, 0, 1], [0, 2, 0], [3, 3, 3]])
assert A * B == sp.Matrix([[39, 35], [34, 34], [38, 34], [30, 24]]) and C + D == sp.Matrix([[3, 3, 5], [1, 5, 5], [5, 7, 9]])
assert C * D == sp.Matrix([[14, 18, 14], [16, 21, 16], [20, 26, 20]]) and D * C == sp.Matrix([[4, 7, 10], [2, 6, 10], [15, 30, 45]])
TB = sp.Matrix([[2, 1, 3, 4], [2, 0, 5, 3], [6, 3, 4, 2], [3, 4, 0, 1], [1, 1, 1, 0]]); BE = sp.Matrix([[3, 6, 2], [4, 1, 6], [0, 4, 5], [8, 0, 0]]); P = sp.Matrix([400, 500, 300])
assert (BE * P).T == sp.Matrix([[4800, 3900, 3500, 3200]]) and (TB * BE * P).T == sp.Matrix([[36800, 36700, 60900, 33200, 12200]])
assert TB * BE == sp.Matrix([[42, 25, 25], [30, 32, 29], [46, 55, 50], [33, 22, 30], [7, 11, 13]])
Mv = sp.Matrix([[1, 0, -2], [2, 0, 4], [3, 5, 1]]); assert Mv.det() == -40 and Mv.solve(sp.Matrix([1, 1, -1])).T == sp.Matrix([[sp.Rational(3, 4), -sp.Rational(5, 8), -sp.Rational(1, 8)]])


def mzellen(x0, y0, zeilen, dx=36, dy=22, size=14, farbe='var(--ink)'):
    """Matrix-Einträge spaltenweise ausgerichtet (Mitte der ersten Zelle bei x0, y0)"""
    return ''.join(T(x0 + j * dx, y0 + i * dy, str(v).replace('-', '−'), size, 700, 'middle', farbe) for i, r in enumerate(zeilen) for j, v in enumerate(r))


def klammer(x, y, w, h):
    return (f'<path d="M{x + 6},{y} q-8,{h / 2} 0,{h}" style="fill:none;stroke:var(--ink)" stroke-width="1.6"/>'
            f'<path d="M{x + w - 6},{y} q8,{h / 2} 0,{h}" style="fill:none;stroke:var(--ink)" stroke-width="1.6"/>')


def mat(m):
    return r'\begin{pmatrix}' + r' \\ '.join(' & '.join(str(v) for v in m.row(i)) for i in range(m.rows)) + r'\end{pmatrix}'


# ---------------------------------------------------------------- 1 Vektoren, Linearkombination, lineare Unabhängigkeit
t_vek = thema('vektoren', 'Vektoren, Linearkombination, lineare Unabhängigkeit',
    kern='Vektoren sind geordnete n-Tupel; man addiert sie komponentenweise und multipliziert sie mit Skalaren. Eine Linearkombination ist λ₁a + λ₂b + λ₃c. Vektoren sind linear unabhängig, wenn λ₁a + λ₂b + λ₃c = 0 nur für λ₁ = λ₂ = λ₃ = 0 gilt; bei drei Vektoren im ℝ³ genau dann, wenn die Determinante der Matrix aus ihnen ≠ 0 ist.',
    kurz=p('Ein Vektor fasst mehrere Zahlen zusammen, etwa die Bestellmengen dreier Produkte: \\((400, 500, 300)\\). Man rechnet komponentenweise: addieren, mit einer Zahl malnehmen.')
        + p('Kann man einen Vektor aus anderen „zusammenbauen“, ist er eine <b>Linearkombination</b>. Sind Vektoren so verschieden, dass keiner aus den anderen entsteht, heißen sie <b>linear unabhängig</b>.'),
    fig=fw('Linear unabhängige Vektoren und eine Linearkombination. Tippe auf die Kästen.')
        + bild(svg(360, 180, ''.join(box(4 + i * 90, 4, 82, 90, t_, size=13, art='hl' if i == 3 else 'card', tip=tip) for i, (t_, tip) in enumerate([
            ('a\n(1, 2, 3)', 'erster Vektor'), ('b\n(0, 0, 5)', 'zweiter Vektor'), ('c\n(−2, 4, 1)', 'dritter Vektor'), ('Ziel\n(1, 1, −1)', 'Dieser Vektor soll als λ₁a + λ₂b + λ₃c dargestellt werden.')]))
            + box(4, 106, 352, 70, 'λ₁ = 3/4,  λ₂ = −5/8,  λ₃ = −1/8\n(Determinante = −40 ≠ 0 → linear unabhängig)', size=13, tip='Lösung des LGS λ₁a + λ₂b + λ₃c = Ziel. Weil die Determinante ≠ 0 ist, gibt es genau eine Lösung.'),
            'Linearkombination', maxw=420)),
    figcap='nach Übungsblatt 7, Aufgabe 1',
    article=h3('Rechenoperationen')
        + p('Für Vektoren gleicher Länge: \\((1, 2, 3) + (0, 0, 5) = (1, 2, 8)\\); \\(2 \\cdot (1, 2, 3) = (2, 4, 6)\\).')
        + h3('Linearkombination und lineare Unabhängigkeit')
        + p('Eine <b>Linearkombination</b> der Vektoren a, b, c ist \\(\\lambda_1 a + \\lambda_2 b + \\lambda_3 c\\). Die Vektoren sind <b>linear unabhängig</b>, wenn aus \\(\\lambda_1 a + \\lambda_2 b + \\lambda_3 c = 0\\) folgt, dass alle \\(\\lambda_i = 0\\). Sonst sind sie linear abhängig (einer lässt sich durch die anderen ausdrücken).')
        + bsp('Übungsblatt 7, Aufgabe 1', r'\(a = (1, 2, 3)\), \(b = (0, 0, 5)\), \(c = (-2, 4, 1)\); stelle \((1, 1, -1)\) dar.',
              [(r'Matrix aus den Spalten a, b, c: \(\det = -40 \ne 0\)', 'linear unabhängig'), (r'LGS: \(\lambda_1 - 2\lambda_3 = 1\), \(2\lambda_1 + 4\lambda_3 = 1\), \(3\lambda_1 + 5\lambda_2 + \lambda_3 = -1\)', ''),
               ('Lösung', r'\(\lambda_1 = \frac{3}{4},\ \lambda_2 = -\frac{5}{8},\ \lambda_3 = -\frac{1}{8}\)')])
        + wahr('w-vek', [('Vektoren werden komponentenweise addiert.', True, 'Stelle für Stelle.'), ('Drei Vektoren im ℝ³ mit Determinante 0 sind linear unabhängig.', False, 'Det = 0 heißt abhängig.')]),
    merk='Vektoren komponentenweise addieren und skalieren. Linearkombination λ₁a + λ₂b + λ₃c. Linear unabhängig ⇔ nur triviale Lösung ⇔ (3 Vektoren im ℝ³) det ≠ 0.',
    exam='Übungsstoff; Determinante und LGS kommen in der LGS-Aufgabe.',
    fehler=['Det = 0 als unabhängig deuten.'],
    src='Übungsblatt 7 A1, Übung lineare Algebra A3')

# ---------------------------------------------------------------- 2 Matrizen: Addition, Skalar, Transponieren
t_matr = thema('matrizen', 'Matrizen: addieren, mit Zahl multiplizieren, transponieren', star=True,
    kern='Eine m×n-Matrix hat m Zeilen und n Spalten. Addition und Subtraktion nur bei gleichem Format, elementweise. Skalarmultiplikation: jedes Element mal die Zahl. Transponieren: Zeilen werden zu Spalten, (Aᵀ)ᵢⱼ = aⱼᵢ; aus m×n wird n×m. Regeln: (Aᵀ)ᵀ = A, (A·B)ᵀ = Bᵀ·Aᵀ.',
    kurz=p('Matrizen sind Tabellen von Zahlen, z. B. wie viele Einzelteile in jede Baugruppe gehen. Rechnen geht meist <b>elementweise</b>: \\(C + D\\) addiert die Zahlen an gleicher Stelle, \\(5 \\cdot A\\) multipliziert jede Zahl mit 5.')
        + p('Beim <b>Transponieren</b> klappt man die Matrix an der Diagonale: Die erste Zeile wird zur ersten Spalte. Klausur-Trick: \\(((A \\cdot B)^T)^T = A \\cdot B\\).'),
    fig=fw('Transponieren: Zeilen werden Spalten. Tippe auf die Kästen.')
        + bild(svg(360, 170, box(4, 20, 160, 130, '', size=14, tip='2 Zeilen, 3 Spalten.') + T(84, 46, 'A (2×3)', 14, 800) + klammer(30, 70, 108, 50) + mzellen(48, 88, [[1, 2, 3], [4, 5, 6]]) + pfeil(168, 85, 196, 85)
                   + box(200, 4, 156, 162, '', size=14, tip='3 Zeilen, 2 Spalten: Die erste Zeile (1 2 3) ist jetzt die erste Spalte.') + T(278, 30, 'Aᵀ (3×2)', 14, 800) + klammer(240, 52, 76, 74) + mzellen(260, 70, [[1, 4], [2, 5], [3, 6]]), 'Transponieren', maxw=420)),
    figcap='nach Übungsblatt 7, Aufgabe 3 und Übung lineare Algebra, Aufgabe 1',
    article=h3('Addition und Skalarmultiplikation')
        + bsp('Übungsblatt 7, Aufgabe 3 (i)', r'\(C + D = ' + mat(C) + ' + ' + mat(D) + r'\)', [('elementweise addieren', r'\(' + mat(C + D) + r'\)')])
        + p('\\(D - C\\) entsprechend elementweise. \\(5 \\cdot A\\): jedes Element mal 5. Nur gleich große Matrizen kann man addieren oder subtrahieren.')
        + h3('Transponieren und Rechenregeln')
        + tabelle(['Regel', 'Bedeutung'], [['(Aᵀ)ᵀ = A', 'zweimal transponieren hebt sich auf'], ['(A + B)ᵀ = Aᵀ + Bᵀ', ''], ['(c·A)ᵀ = c·Aᵀ', ''], ['(A·B)ᵀ = Bᵀ·Aᵀ', 'Reihenfolge dreht sich!']])
        + klausur_hinweis('In zwei Klausuren: a) Aᵀ bzw. 2·A, b) A·v, c) A + C bzw. B + C, d) ((A·B)ᵀ)ᵀ. Bei d) nicht zweimal transponieren: Es ist einfach A·B.')
        + wahr('w-matr', [('Eine 2×3-Matrix kann man zu einer 3×2-Matrix addieren.', False, 'Nur gleiche Formate.'), ('((A·B)ᵀ)ᵀ = A·B', True, 'Zweimal transponieren hebt sich auf.'),
                          ('(A·B)ᵀ = Aᵀ·Bᵀ', False, 'Es ist Bᵀ·Aᵀ.')])
        + h3('Besondere Matrizen')
        + p(r'Eine Matrix mit gleich vielen Zeilen und Spalten heißt <b>quadratisch</b>; \(a_{11}, \dots, a_{nn}\) sind ihre <b>Diagonalelemente</b>. Ist \(a_{ij} = 0\) für \(i > j\) (unter der Diagonale nur Nullen), heißt sie <b>obere Dreiecksmatrix</b>; ist \(a_{ij} = 0\) für alle \(i \ne j\), heißt sie <b>Diagonalmatrix</b>. Die j-te Spalte heißt <b>Spaltenvektor</b> \(a_j\), die i-te Zeile <b>Zeilenvektor</b>.'),
    merk='m×n: m Zeilen, n Spalten. Addition nur bei gleichem Format (elementweise), c·A elementweise. Transponieren: Zeilen ↔ Spalten; (Aᵀ)ᵀ = A, (AB)ᵀ = BᵀAᵀ.',
    exam='Matrizenaufgabe: Aᵀ, 2A, A + C, ((A·B)ᵀ)ᵀ.',
    fehler=['Ungleiche Formate addieren.', '(AB)ᵀ = AᵀBᵀ.'],
    src='Übungsblatt 7 A3, Übung lineare Algebra A1')

# ---------------------------------------------------------------- 3 Matrizenmultiplikation
t_mult = thema('matrizenmultiplikation', 'Matrizenmultiplikation und Matrix mal Vektor', star=True,
    kern='A·B ist nur definiert, wenn A so viele Spalten hat wie B Zeilen: (m×n)·(n×p) = m×p. Element cᵢⱼ = Zeile i von A mal Spalte j von B (Skalarprodukt). Die Multiplikation ist nicht kommutativ: meist A·B ≠ B·A. Matrix mal Vektor ist der Spezialfall p = 1.',
    kurz=p('Matrizen multipliziert man <b>Zeile mal Spalte</b>: Die erste Zeile von A mal die erste Spalte von B (paarweise multiplizieren, addieren) ergibt das Element oben links.')
        + p('Damit das geht, muss die <b>Spaltenzahl von A gleich der Zeilenzahl von B</b> sein. Und die Reihenfolge zählt: \\(C \\cdot D\\) und \\(D \\cdot C\\) sind verschieden.'),
    fig=fw('Zeile mal Spalte. Tippe auf die Kästen.')
        + bild(svg(360, 200, box(4, 60, 110, 80, 'Zeile 1 von A\n(4  3  3)', size=13, art='hl', tip='Erste Zeile von A (4×3).')
                   + box(130, 4, 90, 130, 'Spalte 1\nvon B\n6\n4\n1', size=13, art='hl', tip='Erste Spalte von B (3×2).')
                   + box(236, 60, 120, 80, '4·6 + 3·4 + 3·1\n= 39', size=13, tip='Element oben links von A·B: Skalarprodukt aus Zeile 1 und Spalte 1.')
                   + T(180, 172, '(4×3) · (3×2) = (4×2): innen gleich, außen das Ergebnis', 12, 700, fill='var(--muted)'), 'Matrizenmultiplikation', maxw=420)),
    figcap='nach Übungsblatt 7, Aufgabe 3 (iv)',
    article=h3('Regel')
        + fx('Matrizenprodukt', r'(A \cdot B)_{ij} = \sum_{k=1}^{n} a_{ik} \cdot b_{kj}', 'Zeile i von A mal Spalte j von B: paarweise multiplizieren und addieren.', r'\(4 \cdot 6 + 3 \cdot 4 + 3 \cdot 1 = 39\)')
        + bsp('Übungsblatt 7, Aufgabe 3 (iv)', r'\(A \cdot B = ' + mat(A) + r' \cdot ' + mat(B) + r'\)', [('(4×3)·(3×2) ist möglich, Ergebnis 4×2', r'\(' + mat(A * B) + r'\)')])
        + bsp('Übungsblatt 7, Aufgabe 3 (v), (vi)', r'\(C \cdot D\) und \(D \cdot C\)', [(r'\(C \cdot D = ' + mat(C * D) + r'\)', ''), (r'\(D \cdot C = ' + mat(D * C) + r'\)', 'verschieden!')])
        + h3('Matrix mal Vektor')
        + p('Ein Spaltenvektor ist eine n×1-Matrix. \\(A \\cdot v\\) geht, wenn A n Spalten hat; das Ergebnis ist ein Spaltenvektor mit so vielen Zeilen wie A.')
        + falle('Ohne Formatprüfung multiplizieren. Erst (m×n)·(n×p) prüfen: Die inneren Zahlen müssen gleich sein.')
        + wahr('w-mult', [('(2×3)·(3×4) ergibt eine 2×4-Matrix.', True, 'Außen bleibt übrig.'), ('Für Matrizen gilt immer A·B = B·A.', False, 'Nicht kommutativ.'),
                          ('(3×2)·(3×2) ist definiert.', False, 'Spalten von A (2) ≠ Zeilen von B (3).')]),
    merk='A·B nur wenn Spalten(A) = Zeilen(B); (m×n)(n×p) = m×p; cᵢⱼ = Zeile i · Spalte j. Nicht kommutativ. A·v ist Spezialfall.',
    exam='A·v und A·B in der Matrizenaufgabe.',
    fehler=['Format nicht prüfen.', 'Zeile mal Zeile rechnen.'],
    src='Übungsblatt 7 A3, Übung lineare Algebra A1–A2')

# ---------------------------------------------------------------- 4 Mehrstufige Produktion
def gozinto():
    s = ''
    for i in range(5):
        s += box(4, 6 + i * 48, 64, 40, f'T{i + 1}', size=13, tip=f'Einzelteil T{i + 1}')
    for j in range(4):
        s += box(148, 18 + j * 58, 64, 40, f'B{j + 1}', size=13, tip=f'Baugruppe B{j + 1}: braucht Einzelteile laut Matrix T×B.')
    for k in range(3):
        s += box(292, 40 + k * 64, 64, 40, f'E{k + 1}', size=13, tip=f'Endprodukt E{k + 1}: braucht Baugruppen laut Matrix B×E.')
    for i in range(5):
        for j in range(4):
            if TB[i, j]:
                s += f'<line x1="68" y1="{26 + i * 48}" x2="148" y2="{38 + j * 58}" style="stroke:var(--axis2)" stroke-width="1"/>'
    for j in range(4):
        for k in range(3):
            if BE[j, k]:
                s += f'<line x1="212" y1="{38 + j * 58}" x2="292" y2="{60 + k * 64}" style="stroke:var(--axis2)" stroke-width="1"/>'
    return svg(360, 250, s, 'Gozinto-Graph', maxw=420)

t_prod = thema('mehrstufige-produktion', 'Mehrstufige Produktion (Gozinto, Verbrauchskoeffizienten)', star=True,
    kern='Bei mehrstufiger Produktion beschreibt die Matrix T×B, wie viele Einzelteile je Baugruppe nötig sind, und B×E, wie viele Baugruppen je Endprodukt. Der Baugruppenbedarf ist b = (B×E)·p, der Einzelteilbedarf x = (T×B)·b = C·p mit der Gesamtbedarfsmatrix C = (T×B)·(B×E). Die Reihenfolge der Faktoren folgt dem Materialfluss rückwärts.',
    kurz=p('Ein Betrieb montiert aus fünf Einzelteilen vier Baugruppen und daraus drei Endprodukte. Wie viele Einzelteile braucht er für 400, 500 und 300 Endprodukte?')
        + p('Zwei Matrizen beschreiben die Stufen. Multipliziert man sie, erhält man die <b>Gesamtbedarfsmatrix</b> C: Wie viele Einzelteile stecken in einem Endprodukt? Dann nur noch C mal Produktionsvektor.'),
    fig=fw('Gozinto-Graph: Einzelteile → Baugruppen → Endprodukte. Tippe auf die Kästen.') + bild(gozinto()),
    figcap='nach Übungsblatt 7, Aufgabe 4',
    article=h3('Das Modell')
        + fluss([('Einzelteile T', '5 Arten'), ('Baugruppen B', 'Matrix T×B (5×4)'), ('Endprodukte E', 'Matrix B×E (4×3)')], hl=1)
        + p(r'\(M_{TB} = ' + mat(TB) + r'\), \(M_{BE} = ' + mat(BE) + r'\), \(p = ' + mat(P) + r'\)')
        + bsp('Übungsblatt 7, Aufgabe 4', 'E1: 400, E2: 500, E3: 300 Stück.',
              [(r'Baugruppenbedarf \(b = M_{BE} \cdot p\)', r'\(b = (4.800;\ 3.900;\ 3.500;\ 3.200)^T\)'),
               (r'Einzelteilbedarf \(x = M_{TB} \cdot b\)', r'\(x = (36.800;\ 36.700;\ 60.900;\ 33.200;\ 12.200)^T\)'),
               (r'Direkt: \(C = M_{TB} \cdot M_{BE} = ' + mat(TB * BE) + r'\), \(x = C \cdot p\)', 'gleiches Ergebnis')],
              'c₁₁ = 42 heißt: In einem E1 stecken insgesamt 42 Einzelteile T1.')
        + klausur_hinweis('„Matrix mit Rohstoffen und Endprodukt“ bzw. „Verbrauchskoeffizienten: Rohstoffbedarf der Endprodukte bestimmen (R×Z, Z×E; zweistufige Produktion)“ wird häufig gefragt.')
        + falle('Die Matrizen in falscher Reihenfolge multiplizieren: C = M_TB · M_BE (Einzelteile × Baugruppen, Baugruppen × Endprodukte), innere Dimensionen müssen passen.')
        + wahr('w-prod', [('Der Gesamtbedarf an Einzelteilen ist C·p mit C = M_TB·M_BE.', True, 'Zweistufig.'), ('M_BE · M_TB liefert den Einzelteilbedarf.', False, 'Falsche Reihenfolge, Formate passen nicht.')]),
    merk='Zweistufig: b = M_BE·p (Zwischenprodukte), x = M_TB·b = (M_TB·M_BE)·p. Gesamtbedarfsmatrix C = M_TB·M_BE; cᵢⱼ = Einzelteile i je Endprodukt j.',
    exam='Rohstoff- bzw. Einzelteilbedarf über Verbrauchskoeffizienten berechnen.',
    fehler=['Reihenfolge der Matrizen.', 'Produktionsvektor als Zeilenvektor rechts dranmultiplizieren.'],
    src='Übungsblatt 7, A4')

KAPITEL = kapitel('k7', 'Vektoren und Matrizen',
    'Rechnen mit Vektoren und Matrizen bis zur mehrstufigen Produktion.',
    ['Vektoren', 'Matrizen', 'Multiplikation', 'mehrstufige Produktion'], [t_vek, t_matr, t_mult, t_prod])
