import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *
import sympy as sp
from k7 import mat, mzellen, klammer

D1 = sp.Matrix([[1, 4, 3], [2, 5, 4], [1, -3, -2]]); b1 = sp.Matrix([1, 4, 5])
assert D1.det() == 1 and D1.inv() == sp.Matrix([[2, -1, 1], [8, -5, 2], [-11, 7, -3]]) and (D1.inv() * b1).T == sp.Matrix([[3, -2, 2]])
A8 = sp.Matrix([[2, 4, -3], [-1, 5, 7], [-1, 1, -1]]); B8 = sp.Matrix([[1, 2, 3], [2, 4, 6], [-3, 1, 0]]); C8 = sp.Matrix([[1, 4], [2, -5]])
assert (A8.det(), B8.det(), C8.det()) == (-68, 0, -13)
I3 = sp.Matrix([[1, 2, -1], [2, 4, 2], [1, 1, 1]]); assert I3.det() == 4 and I3.inv() == sp.Matrix([[sp.Rational(1, 2), -sp.Rational(3, 4), 2], [0, sp.Rational(1, 2), -1], [-sp.Rational(1, 2), sp.Rational(1, 4), 0]])
assert sp.Matrix([[1, 2, -1], [2, 4, 2], [-4, -8, -8]]).det() == 0


def lgs_tafel(art):
    if art == 'eins':
        f1, f2, txt, tip = (lambda v: (5 * v + 4) / 2), (lambda v: 5), 'genau eine Lösung', 'Zwei Geraden schneiden sich in einem Punkt: x₁ = 1,2; x₂ = 5.'
    elif art == 'keine':
        f1, f2, txt, tip = (lambda v: -v), (lambda v: 1 - v), 'keine Lösung', 'x₁ + x₂ = 0 und x₁ + x₂ = 1: parallele Geraden, kein Schnittpunkt.'
    else:
        f1, f2, txt, tip = (lambda v: (3 - v) / 2), (lambda v: (6 - 2 * v) / 4), 'unendlich viele', 'x₁ + 2x₂ = 3 und 2x₁ + 4x₂ = 6 sind dieselbe Gerade.'
    s, X, Y = graph([(f1, -3, 4, 'var(--primary)', '', tip, None), (f2, -3, 4, 'var(--c2)', '', tip, None)], (-3, 4), (-3, 7), xl='x₁', yl='x₂', ticks_x=(1, 3), ticks_y=(2, 5))
    s += T(X(-2.8), Y(6.3), txt, 14, 800, 'start', 'var(--c3)')
    return svg(360, 250, s, txt, maxw=420)

# ---------------------------------------------------------------- 1 LGS und Gauß
t_gauss = thema('lgs-gauss', 'Lineare Gleichungssysteme und Gauß-Verfahren',
    kern='Ein LGS A·x = b hat keine, genau eine oder unendlich viele Lösungen. Das Gauß-Verfahren bringt die erweiterte Matrix (A | b) mit elementaren Zeilenumformungen (Zeilen tauschen, mit Zahl ≠ 0 multiplizieren, Vielfaches einer Zeile addieren) in Zeilenstufenform; dann löst man von unten nach oben. Geometrisch (2 Variablen): Schnittpunkt, parallele Geraden, identische Geraden.',
    kurz=p('Drei Gleichungen, drei Unbekannte: Das <b>Gauß-Verfahren</b> eliminiert Schritt für Schritt Variablen, bis unten nur noch eine steht. Dann setzt man von unten nach oben ein.')
        + p('Bei zwei Variablen ist jede Gleichung eine Gerade. Schneiden sie sich, gibt es <b>eine</b> Lösung; sind sie parallel, <b>keine</b>; liegen sie aufeinander, <b>unendlich viele</b>.'),
    fig=fw('Drei Fälle geometrisch. Schalte um und tippe auf die Geraden.') + tafeln('tf-lgs', ['eine', 'keine', 'unendlich'], [lgs_tafel('eins'), lgs_tafel('keine'), lgs_tafel('unendlich')]),
    figcap='nach Übungsblatt 7, Aufgabe 5 bzw. Blatt 8, Aufgabe 1',
    article=h3('Elementare Zeilenumformungen')
        + liste(['zwei Zeilen vertauschen', 'eine Zeile mit einer Zahl ≠ 0 multiplizieren', 'ein Vielfaches einer Zeile zu einer anderen addieren'])
        + bsp('Übungsblatt 8, Aufgabe 1', 'Lösbarkeit und geometrische Deutung',
              [(r'\(5x_1 - 2x_2 = -4,\ x_2 = 5\)', r'\(x_1 = 1{,}2\): genau eine Lösung (Schnittpunkt)'), (r'\(x_1 + x_2 = 0,\ x_1 + x_2 = 1\)', 'Widerspruch 0 = 1: keine Lösung (parallel)'),
               (r'\(x_1 + 2x_2 = 3,\ 2x_1 + 4x_2 = 6\)', r'2. Gleichung = 2 · 1.: unendlich viele, \(x_1 = 3 - 2t,\ x_2 = t\)')])
        + h3('Gauß-Verfahren bei drei Variablen')
        + bsp('Übungsblatt 8, Aufgabe 4 (i), mit Gauß', r'\(x_1 + 4x_2 + 3x_3 = 1,\ 2x_1 + 5x_2 + 4x_3 = 4,\ x_1 - 3x_2 - 2x_3 = 5\)',
              [(r'II − 2·I: \(-3x_2 - 2x_3 = 2\); III − I: \(-7x_2 - 5x_3 = 4\)', ''), (r'3·III − 7·II: \(-x_3 = -2\)', r'\(x_3 = 2\)'),
               (r'einsetzen: \(-3x_2 - 4 = 2\)', r'\(x_2 = -2\)'), (r'\(x_1 - 8 + 6 = 1\)', r'\(x_1 = 3\)')])
        + p('Eine Nullzeile mit Wert ≠ 0 rechts (0 = c) heißt: keine Lösung. Eine reine Nullzeile heißt: eine Variable ist frei, unendlich viele Lösungen.')
        + wahr('w-gauss', [('Ein LGS kann genau zwei Lösungen haben.', False, 'Keine, eine oder unendlich viele.'), ('Eine Zeile 0 = 3 bedeutet: keine Lösung.', True, 'Widerspruch.')]),
    merk='LGS: keine, eine oder unendlich viele Lösungen. Gauß: (A|b) mit Zeilenumformungen in Stufenform, rückwärts einsetzen. 0 = c (c ≠ 0): keine Lösung; Nullzeile: freie Variable.',
    exam='Lösbarkeit prüfen (häufig gefragt).',
    fehler=['Beim Addieren von Zeilen rechte Seite vergessen.'],
    src='Übungsblatt 7 A2, A5; Blatt 8 A1')

# ---------------------------------------------------------------- 2 Determinante
t_det = thema('determinante', 'Determinanten (2×2, 3×3 Sarrus)', star=True,
    kern='2×2: det = a·d − b·c. 3×3: Regel von Sarrus (drei Hauptdiagonalprodukte minus drei Nebendiagonalprodukte) oder Entwicklung nach einer Zeile/Spalte. Ist det(A) ≠ 0, ist A invertierbar und A·x = b eindeutig lösbar; ist det(A) = 0, gibt es keine oder unendlich viele Lösungen.',
    kurz=p('Die <b>Determinante</b> ist eine einzige Zahl, die einer quadratischen Matrix verrät, ob ein LGS eindeutig lösbar ist. Nicht null: genau eine Lösung, und es gibt eine inverse Matrix. Null: Vorsicht.')
        + p('Für 3×3-Matrizen gibt es ein Rezept: die <b>Regel von Sarrus</b>.'),
    fig=fw('Sarrus: erste zwei Spalten rechts anhängen. Tippe auf die Kästen.')
        + bild(svg(360, 200, box(4, 4, 352, 92, '', size=14, tip='Matrix A aus Übungsblatt 8, Aufgabe 2, mit den ersten zwei Spalten rechts angehängt.') + klammer(70, 14, 128, 72) + mzellen(96, 30, [[2, 4, -3], [-1, 5, 7], [-1, 1, -1]], dx=38) + mzellen(232, 30, [[2, 4], [-1, 5], [-1, 1]], dx=38, farbe='var(--muted)')
                   + box(4, 104, 172, 92, '↘ Hauptdiagonalen\n2·5·(−1) + 4·7·(−1)\n+ (−3)·(−1)·1 = −35', size=12, tip='Drei Produkte von links oben nach rechts unten: −10 − 28 + 3 = −35.')
                   + box(184, 104, 172, 92, '↗ Nebendiagonalen\n(−3)·5·(−1) + 2·7·1\n+ 4·(−1)·(−1) = 33', size=12, art='hl', tip='Drei Produkte von links unten nach rechts oben: 15 + 14 + 4 = 33. Det = −35 − 33 = −68.'), 'Sarrus', maxw=420)),
    figcap='nach Übungsblatt 8, Aufgabe 2',
    article=h3('2×2 und 3×3')
        + fx('2×2-Determinante', r'\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = a \cdot d - b \cdot c', 'Hauptdiagonale minus Nebendiagonale.', r'\(\det\begin{pmatrix} 1 & 4 \\ 2 & -5 \end{pmatrix} = -5 - 8 = -13\)')
        + bsp('Übungsblatt 8, Aufgabe 2 (A)', r'\(A = ' + mat(A8) + r'\)', [('Hauptdiagonalen: −10 − 28 + 3 = −35', ''), ('Nebendiagonalen: 15 + 14 + 4 = 33', ''), ('det A = −35 − 33', r'\(-68\)')])
        + bsp('Übungsblatt 8, Aufgabe 2 (B)', r'\(B = ' + mat(B8) + r'\)', [('Zeile 2 = 2 · Zeile 1', r'\(\det B = 0\)')], 'Sind zwei Zeilen Vielfache voneinander, ist die Determinante 0 (linear abhängig).')
        + h3('Was die Determinante sagt')
        + tabelle(['det A', 'A·x = b', 'Inverse'], [['≠ 0', 'genau eine Lösung', 'existiert'], ['= 0', 'keine oder unendlich viele', 'existiert nicht']])
        + klausur_hinweis('„Bestimmen Sie mit Hilfe der Determinante, ob das LGS eindeutig lösbar ist“ wird häufig gefragt.')
        + wahr('w-det', [('Ist det A ≠ 0, ist A·x = b eindeutig lösbar.', True, 'Und A ist invertierbar.'), (r'\(\det\begin{pmatrix} 3 & 5 \\ 7 & 4 \end{pmatrix} = 47\)', False, '12 − 35 = −23.'),
                         ('Sind zwei Zeilen gleich, ist die Determinante 0.', True, 'Linear abhängig.')]),
    merk='2×2: ad − bc. 3×3: Sarrus (3 Haupt- minus 3 Nebendiagonalprodukte). det ≠ 0 ⇔ eindeutig lösbar ⇔ invertierbar; det = 0 bei linear abhängigen Zeilen.',
    exam='Determinante berechnen und daraus die eindeutige Lösbarkeit folgern.',
    fehler=['Vorzeichen bei Sarrus.', 'Nebendiagonalen addieren statt subtrahieren.'],
    src='Übungsblatt 8 A2, Übung lineare Algebra A4')

# ---------------------------------------------------------------- 3 Inverse Matrix und LGS
t_inv = thema('inverse-matrix', 'Inverse Matrix und Lösen mit der Inversen', star=True,
    kern='Die inverse Matrix A⁻¹ erfüllt A·A⁻¹ = E. Man berechnet sie mit dem Gauß-Jordan-Verfahren: (A | E) umformen zu (E | A⁻¹). Für 2×2: A⁻¹ = 1/(ad − bc)·[[d, −b], [−c, a]]. Ein eindeutig lösbares LGS A·x = b löst man mit x = A⁻¹·b.',
    kurz=p('Bei Zahlen löst man \\(3x = 6\\) durch Teilen. Bei Matrizen gibt es kein Teilen, aber die <b>inverse Matrix</b>: \\(A \\cdot x = b\\) ⇒ \\(x = A^{-1} \\cdot b\\).')
        + p('Die Inverse gibt es nur, wenn \\(\\det A \\ne 0\\). Man berechnet sie, indem man neben A die Einheitsmatrix schreibt und so lange umformt, bis links die Einheitsmatrix steht.'),
    fig=fw('Gauß-Jordan: links A, rechts E. Tippe auf die Kästen.')
        + bild(svg(360, 170, box(4, 4, 172, 76, '( A | E )', size=16, tip='Start: links die Matrix, rechts die Einheitsmatrix.') + box(184, 4, 172, 76, '( E | A⁻¹ )', size=16, art='hl', tip='Ziel: links die Einheitsmatrix, dann steht rechts die Inverse.')
                   + pfeil(176, 42, 184, 42) + box(4, 92, 352, 74, 'x = A⁻¹ · b\nProbe: A · x = b', size=15, tip='Mit der Inversen löst man das LGS durch eine Matrix-Vektor-Multiplikation.'), 'Inverse', maxw=420)),
    figcap='nach Übungsblatt 8, Aufgaben 3 und 4',
    article=h3('Inverse berechnen')
        + fx('Inverse einer 2×2-Matrix', r'\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}', 'Diagonale tauschen, Nebendiagonale Vorzeichen wechseln, durch die Determinante teilen.',
             r'\(\begin{pmatrix} 1 & 4 \\ 2 & -5 \end{pmatrix}^{-1} = \frac{1}{-13}\begin{pmatrix} -5 & -4 \\ -2 & 1 \end{pmatrix}\)')
        + bsp('Übungsblatt 8, Aufgabe 3 (A)', r'\(A = ' + mat(I3) + r'\), \(\det A = 4\)', [('(A | E) mit Gauß-Jordan umformen', r'\(A^{-1} = ' + mat(I3.inv()) + r'\)')],
              'Die Matrix B aus derselben Aufgabe hat det = 0 (Spalte 2 = 2 · Spalte 1): keine Inverse.')
        + h3('LGS mit der Inversen lösen')
        + bsp('Übungsblatt 8, Aufgabe 4 (i)', r'\(D = ' + mat(D1) + r'\), \(b = ' + mat(b1) + r'\)',
              [(r'\(\det D = 1 \ne 0\)', 'eindeutig lösbar'), (r'\(D^{-1} = ' + mat(D1.inv()) + r'\)', ''), (r'\(x = D^{-1} \cdot b\)', r'\(x = (3;\ -2;\ 2)^T\)')],
              'Probe: 3 + 4·(−2) + 3·2 = 1 ✓.')
        + klausur_hinweis('„Bestimmen Sie mit Hilfe der Determinante, ob das LGS eindeutig lösbar ist, und bestimmen Sie die Lösung mit Hilfe der Inversen“ ist sehr häufig gefragt.')
        + wahr('w-inv', [('A·A⁻¹ ergibt die Einheitsmatrix.', True, 'Definition.'), ('Jede quadratische Matrix hat eine Inverse.', False, 'Nur bei det ≠ 0.'), ('Bei A·x = b ist x = b·A⁻¹.', False, 'x = A⁻¹·b (von links).')]),
    merk='A·A⁻¹ = E; nur bei det A ≠ 0. Gauß-Jordan: (A|E) → (E|A⁻¹). 2×2: 1/(ad−bc)·[[d,−b],[−c,a]]. LGS: x = A⁻¹·b; Probe A·x = b.',
    exam='Inverse berechnen und LGS damit lösen (jede Klausur).',
    fehler=['A⁻¹ von rechts multiplizieren.', 'Rechenfehler beim Gauß-Jordan: Probe A·A⁻¹ = E machen.'],
    src='Übungsblatt 8 A3–A4, Übung lineare Algebra A5')

KAPITEL = kapitel('k8', 'Lineare Gleichungssysteme, Determinante, Inverse',
    'LGS lösen, Lösbarkeit mit der Determinante prüfen und mit der inversen Matrix rechnen.',
    ['LGS und Gauß', 'Determinante', 'Inverse'], [t_gauss, t_det, t_inv])
