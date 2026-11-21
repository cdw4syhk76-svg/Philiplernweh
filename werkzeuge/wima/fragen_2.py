"""Wirtschaftsmathe-Fragen, Oberthemen 6–9."""
from fr_basis import *

R, F = True, False

# ================================================================ k6
fam('stammfunktion', 'grund', 'Bildet Stammfunktionen',
    mc('Eine Stammfunktion von \\(3x^2\\):', '\\(x^3\\)', ['\\(6x\\)', '\\(x^3/3\\)', '\\(3x^3\\)'], '', 1),
    mc('\\(\\int \\frac{1}{x}\\,dx =\\)', '\\(\\ln|x| + C\\)', ['\\(\\frac{x^0}{0} + C\\)', '\\(-\\frac{1}{x^2} + C\\)', '\\(x + C\\)'], '', 1),
    mc('\\(\\int \\sin x\\,dx =\\)', '\\(-\\cos x + C\\)', ['\\(\\cos x + C\\)', '\\(-\\sin x + C\\)', '\\(\\sin x \\cos x + C\\)'], '', 1),
    nu('F(x) = ∫ {A}x^{N} dx mit F(0) = 0. Berechnen Sie F(1).', {'A': [2, 12, 2], 'N': [1, 5, 1]}, 'A/(N+1)', 'F(x) = {A}x^{=N+1}/{=N+1}; F(1) = {=A/(N+1)}', '', 3, lvl=1),
    nu("K′(x) = 1,5x² − 4x + 4, K(10) = {G}. Fixkosten?", {'G': [350, 420, 10]}, 'G-340', 'K = 0,5x³ − 2x² + 4x + C; 340 + C = {G}', 'GE', 0, lvl=2),
    blk('Richtig oder falsch?', [('Beim unbestimmten Integral gehört +C dazu.', R), ('∫ eˣ dx = eˣ + C', R), ('∫ e^(2x) dx = 2e^(2x) + C', F), ('Probe: Ableiten der Stammfunktion ergibt f.', R)], '', 2, True),
    zu('Stammfunktion zuordnen', ['x⁴/4', 'sin x', '−cos x', '½e^(2x)'], [('x³', 0), ('cos x', 1), ('sin x', 2), ('e^(2x)', 3)], '', 1),
    rv('Warum steht beim unbestimmten Integral „+ C“?', 'Konstanten fallen beim Ableiten weg. Deshalb hat jede Funktion unendlich viele Stammfunktionen, die sich nur um eine Konstante unterscheiden. Ökonomisch ist C bei Kostenfunktionen die Fixkosten.', ['Konstante fällt beim Ableiten weg', 'unendlich viele Stammfunktionen', 'Fixkosten'], 2))
fam('bestimmtes-integral', 'grund', 'Berechnet bestimmte Integrale',
    nu('Berechnen Sie ∫ von 0 bis {B} von {A}x dx.', {'A': [2, 8, 2], 'B': [1, 6, 1]}, 'A*B**2/2', '[{A}x²/2]₀^{B} = {=A*B**2/2}', '', 2, lvl=1),
    nu('Berechnen Sie ∫ von 0 bis {B} von x² dx.', {'B': [1, 6, 1]}, 'B**3/3', '[x³/3]₀^{B} = {=B**3/3}', '', 2, lvl=1),
    ns('\\(\\int_1^3 (3x^2 + 4x - 2)\\,dx\\)?', 38, '[x³ + 2x² − 2x]₁³ = 39 − 1', '', 2),
    blk('Richtig oder falsch?', [('∫ₐᵇ f dx = F(b) − F(a)', R), ('Flächen unter der x-Achse zählen positiv.', F), ('∫ₐᵃ f dx = 0', R), ('∫ₐᵇ f dx = −∫ᵦₐ f dx', R)], '', 2, True),
    nu('Berechnen Sie ∫ von 0 bis {B} von e^x dx (2 Stellen).', {'B': [1, 3, 1]}, 'exp(B)-1', '[eˣ]₀^{B} = e^{B} − 1 = {=exp(B)-1}', '', 2, lvl=2),
    mc('\\(\\int_0^{\\pi} \\sin x\\,dx =\\)', '2', ['0', '−2', 'π'], '[−cos x]₀^π = 1 + 1.', 2),
    kz('Wie heißt der Satz ∫ₐᵇ f dx = F(b) − F(a)?', ['Hauptsatz', 'Fundamentalsatz', 'Hauptsatz der Differential- und Integralrechnung'], '', 1),
    rv('Berechnen Sie \\(\\int_0^2 2x\\,dx\\) und deuten Sie das Ergebnis.', 'Stammfunktion x², [x²]₀² = 4 − 0 = 4. Das ist die Fläche des Dreiecks unter der Geraden 2x zwischen 0 und 2 (½ · 2 · 4 = 4).', ['Stammfunktion x²', '4', 'Dreiecksfläche'], 2))
fam('substitution', 'grund', 'Integriert mit Substitution',
    mc('Welche Substitution passt bei \\(\\int 2x e^{x^2}\\,dx\\)?', '\\(u = x^2\\)', ['\\(u = 2x\\)', '\\(u = e^{x}\\)', '\\(u = e^{x^2}\\)'], '', 1, True),
    ns('\\(\\int_0^1 2x e^{x^2}\\,dx\\) (2 Stellen)?', 1.72, 'e − 1', '', 2, True),
    mc('\\(\\int_0^a \\frac{6x}{\\sqrt{3x^2 + a^2}}\\,dx\\) (a > 0) =', '\\(2a\\)', ['\\(a\\)', '\\(4a\\)', '\\(6a\\)'], 'u = 3x² + a².', 3),
    nu('Berechnen Sie ∫ von 0 bis 1 von {A}(x + 1)^{N} dx (2 Stellen). Tipp: u = x + 1.', {'A': [1, 4, 1], 'N': [1, 3, 1]}, 'A*(2**(N+1)-1)/(N+1)', '{A}·[(x+1)^{=N+1}/{=N+1}]₀¹ = {=A*(2**(N+1)-1)/(N+1)}', '', 2, lvl=2),
    blk('Richtig oder falsch?', [('Substitution ist die Kettenregel rückwärts.', R), ('Bei u = 3x + 1 ist dx = du/3.', R), ('Beim bestimmten Integral muss man die Grenzen umrechnen oder zurücksubstituieren.', R), ('Bei u = x² ist du = x dx.', F)], '', 2, True),
    mc('\\(\\int t\\sqrt{t-1}\\,dt\\) mit \\(u = t - 1\\) ergibt …', '\\(\\int (u^{3/2} + u^{1/2})\\,du\\)', ['\\(\\int u^{1/2}\\,du\\)', '\\(\\int (u-1)u^{1/2}\\,du\\)', '\\(\\int u^{3/2}\\,du\\)'], 't = u + 1.', 3, True),
    rh('Ordnen Sie die Schritte.', ['u = g(x) wählen', 'dx durch du ersetzen', 'nach u integrieren', 'zurücksetzen bzw. Grenzen umrechnen'], '', 1),
    rv('Berechnen Sie \\(\\int_0^1 2x\\,e^{x^2}\\,dx\\) mit Substitution.', 'u = x², du = 2x dx; Grenzen: x = 0 → u = 0, x = 1 → u = 1. ∫₀¹ eᵘ du = [eᵘ]₀¹ = e − 1 ≈ 1,72.', ['u = x²', 'Grenzen umrechnen', 'e − 1'], 2, True))
fam('partielle-integration', 'grund', 'Integriert partiell',
    mc('Bei \\(\\int x e^x\\,dx\\) wählt man …', 'u = x, v′ = eˣ', ['u = eˣ, v′ = x', 'u = xeˣ, v′ = 1', 'keine partielle Integration'], 'Polynom ableiten.', 1, True),
    mc('\\(\\int x e^x\\,dx =\\)', '\\((x - 1)e^x + C\\)', ['\\(x e^x + C\\)', '\\(\\frac{x^2}{2}e^x + C\\)', '\\((x + 1)e^x + C\\)'], '', 2, True),
    ns('\\(\\int_0^2 t \\cdot e^{2t}\\,dt\\) (2 Stellen)?', 41.20, '¾e⁴ + ¼', '', 3, True),
    ns('\\(\\int_0^{\\pi} x\\cos x\\,dx\\)?', -2, '[x sin x + cos x]₀^π = −1 − 1', '', 3, True),
    blk('Richtig oder falsch?', [('∫ u·v′ dx = u·v − ∫ u′·v dx', R), ('Partielle Integration ist die Umkehrung der Produktregel.', R), ('Bei ∫ x sin x dx wählt man u = sin x.', F), ('Das neue Integral sollte einfacher sein.', R)], '', 2, True),
    nu('Berechnen Sie ∫ von 0 bis 1 von x·e^x dx + {A} (2 Stellen).', {'A': [0, 5, 1]}, '1+A', '[(x−1)eˣ]₀¹ = 0 − (−1) = 1; plus {A}', '', 2, lvl=2),
    zu('Was ist u (ableiten), was v′ (integrieren)?', ['u', 'v′'], [('t in t·e^(2t)', 0), ('e^(2t) in t·e^(2t)', 1), ('x in x·cos x', 0), ('cos x in x·cos x', 1)], '', 1),
    rv('Berechnen Sie \\(\\int_0^2 t\\,e^{2t}\\,dt\\).', 'u = t, u′ = 1; v′ = e^(2t), v = ½e^(2t). [t/2·e^(2t)]₀² − ∫₀² ½e^(2t) dt = e⁴ − [¼e^(2t)]₀² = e⁴ − ¼e⁴ + ¼ = ¾e⁴ + ¼ ≈ 41,20.', ['u, v′ richtig gewählt', 'Formel angewandt', '¾e⁴ + ¼ ≈ 41,20'], 3, True))

# ================================================================ k7
fam('vektoren', 'grund', 'Rechnet mit Vektoren',
    nu('(1, {A}, 3) + {L}·(2, 0, {B}). Wie lautet die 3. Komponente?', {'A': [1, 9, 1], 'B': [1, 9, 1], 'L': [2, 5, 1]}, '3+L*B', '3 + {L}·{B} = {=3+L*B}', '', 0, lvl=1),
    mc('Drei Vektoren im ℝ³ sind linear unabhängig, wenn …', 'die Determinante ihrer Matrix ≠ 0 ist', ['sie gleich lang sind', 'einer der Nullvektor ist', 'die Summe null ist'], '', 1),
    blk('Richtig oder falsch?', [('Vektoren werden komponentenweise addiert.', R), ('Ein Satz, der den Nullvektor enthält, ist linear unabhängig.', F), ('λa + μb heißt Linearkombination.', R), ('(1,2,3), (0,0,5), (−2,4,1) sind linear unabhängig.', R)], '', 2, True),
    mc('(2, 4, 6) und (1, 2, 3) sind …', 'linear abhängig', ['linear unabhängig', 'orthogonal', 'gleich'], 'Erster = 2 · zweiter.', 1),
    nu('Skalarprodukt (Zeile mal Spalte) von ({A}, {B}) und ({C}, {D})?', {'A': [1, 6, 1], 'B': [1, 6, 1], 'C': [1, 6, 1], 'D': [1, 6, 1]}, 'A*C+B*D', '{A}·{C} + {B}·{D} = {=A*C+B*D}', '', 0, lvl=1),
    lu('Vektoren sind linear unabhängig, wenn die Linearkombination nur für alle λᵢ = [[0]] den Nullvektor ergibt.', [['0', 'null']], '', 2),
    kz('Wie heißt eine Summe λ₁a + λ₂b + λ₃c?', ['Linearkombination'], '', 1),
    rv('Wie prüft man, ob a = (2,0,1), b = (3,0,0), c = (−3,1,5) linear unabhängig sind?', 'Man schreibt sie als Spalten einer 3×3-Matrix und berechnet die Determinante. Sie ist 3 ≠ 0, also sind die Vektoren linear unabhängig; jeder Vektor des ℝ³ ist eindeutig als Linearkombination darstellbar.', ['Matrix aus Spalten', 'Determinante ≠ 0', 'unabhängig'], 2))
fam('matrizen', 'grund', 'Addiert, skaliert, transponiert Matrizen',
    mc('\\(((A \\cdot B)^T)^T =\\)', '\\(A \\cdot B\\)', ['\\(B \\cdot A\\)', '\\(A^T B^T\\)', '\\(B^T A^T\\)'], 'Zweimal transponieren hebt sich auf.', 1, True),
    mc('Eine 4×3-Matrix transponiert ist …', '3×4', ['4×3', '4×4', '3×3'], '', 1, True),
    nu('A = [[{A}, 2], [3, {B}]]. Element (2,1) von 5·A?', {'A': [1, 9, 1], 'B': [1, 9, 1]}, '15', '5 · 3 = 15', '', 0, lvl=1, kl=True),
    nu('C = [[2, 3], [1, {A}]], D = [[1, 0], [{B}, 2]]. Element (2,1) von C + D?', {'A': [1, 9, 1], 'B': [1, 9, 1]}, '1+B', '1 + {B} = {=1+B}', '', 0, lvl=1),
    blk('Richtig oder falsch?', [('(Aᵀ)ᵀ = A', R), ('(A·B)ᵀ = Aᵀ·Bᵀ', F), ('Nur gleich große Matrizen kann man addieren.', R), ('Bei 5·A wird jedes Element mit 5 multipliziert.', R)], '', 2, True),
    zu('Welches Format hat das Ergebnis?', ['2×3', '3×2', 'nicht definiert'], [('Aᵀ für A (3×2)', 0), ('A + B mit A (2×3), B (2×3)', 0), ('A + B mit A (2×3), B (3×2)', 2), ('(Aᵀ)ᵀ für A (3×2)', 1)], '', 2),
    lu('Beim Transponieren werden [[0]] zu Spalten.', [['Zeilen']], '', 1),
    rv('Erklären Sie, warum ((A·B)ᵀ)ᵀ ohne Rechnen vereinfacht werden kann.', 'Zweimaliges Transponieren hebt sich auf: (Mᵀ)ᵀ = M. Mit M = A·B ist ((A·B)ᵀ)ᵀ = A·B. Man berechnet also nur das Produkt.', ['(Mᵀ)ᵀ = M', 'Ergebnis A·B'], 2, True))
fam('matrizenmultiplikation', 'grund', 'Multipliziert Matrizen',
    mc('(4×3)·(3×2) ergibt …', 'eine 4×2-Matrix', ['eine 3×3-Matrix', 'eine 4×3-Matrix', 'nichts (nicht definiert)'], '', 1, True),
    nu('A = [[{A}, {B}], [1, 2]], v = (3, {C}). Erste Komponente von A·v?', {'A': [1, 9, 1], 'B': [1, 9, 1], 'C': [1, 9, 1]}, '3*A+B*C', '{A}·3 + {B}·{C} = {=3*A+B*C}', '', 0, lvl=1, kl=True),
    nu('A = [[{A}, {B}], [{C}, {D}]], B = [[1, 2], [3, 4]]. Element (1,1) von A·B?', {'A': [1, 6, 1], 'B': [1, 6, 1], 'C': [1, 6, 1], 'D': [1, 6, 1]}, 'A+3*B', '{A}·1 + {B}·3 = {=A+3*B}', '', 0, lvl=2, kl=True),
    blk('Richtig oder falsch?', [('A·B = B·A gilt immer.', F), ('(3×2)·(3×2) ist definiert.', F), ('cᵢⱼ = Zeile i von A mal Spalte j von B', R), ('Matrix mal Vektor ist ein Spezialfall der Matrizenmultiplikation.', R)], '', 2, True),
    ns('Element (1,1) von A·B mit A = [[4,3,3],[2,4,6],[1,7,4],[3,3,0]], B = [[6,5],[4,3],[1,2]]?', 39, '4·6 + 3·4 + 3·1', '', 2),
    zu('Ist das Produkt definiert?', ['ja', 'nein'], [('(2×3)·(3×4)', 0), ('(3×2)·(3×2)', 1), ('(1×3)·(3×1)', 0), ('(2×2)·(3×2)', 1)], '', 1),
    mc('C·D und D·C für C = [[2,3,4],[1,3,5],[2,4,6]], D = [[1,0,1],[0,2,0],[3,3,3]] sind …', 'verschieden', ['gleich', 'beide Nullmatrizen', 'nicht definiert'], '', 2),
    rv('Unter welcher Bedingung ist A·B definiert, und welches Format hat das Ergebnis?', 'Die Spaltenzahl von A muss gleich der Zeilenzahl von B sein: (m×n)·(n×p). Das Ergebnis hat m Zeilen und p Spalten, also m×p.', ['Spalten A = Zeilen B', 'Ergebnis m×p'], 1))
fam('mehrstufige-produktion', 'grund', 'Rechnet mehrstufige Produktion',
    mc('Gesamtbedarfsmatrix bei zweistufiger Produktion:', '\\(C = M_{TB} \\cdot M_{BE}\\)', ['\\(C = M_{BE} \\cdot M_{TB}\\)', '\\(C = M_{TB} + M_{BE}\\)', '\\(C = M_{TB}^T\\)'], '', 1, True),
    nu('E1 braucht {A} B1, B1 braucht {B} T1. Wie viele T1 stecken (nur über B1) in einem E1?', {'A': [2, 8, 1], 'B': [2, 8, 1]}, 'A*B', '{A} · {B} = {=A*B}', 'Stück', 0, lvl=1, kl=True),
    nu('Baugruppenbedarf: M_BE = [[3, 6], [4, 1]], p = ({X}, {Y}). Bedarf an B1?', {'X': [100, 500, 100], 'Y': [100, 500, 100]}, '3*X+6*Y', '3·{X} + 6·{Y} = {=3*X+6*Y}', 'Stück', 0, lvl=2, kl=True),
    blk('Richtig oder falsch?', [('b = M_BE · p liefert den Baugruppenbedarf.', R), ('x = M_TB · b liefert den Einzelteilbedarf.', R), ('cᵢⱼ gibt Einzelteile i je Endprodukt j an.', R), ('Der Produktionsvektor wird von links multipliziert.', F)], '', 2, True),
    ns('Übungsblatt 7, A4: Bedarf an Baugruppe B1 bei p = (400, 500, 300)?', 4800, '3·400 + 6·500 + 2·300', 'Stück', 2, True),
    ns('Übungsblatt 7, A4: c₁₁ der Gesamtbedarfsmatrix (T1 je E1)?', 42, '2·3 + 1·4 + 3·0 + 4·8', 'Stück', 3, True),
    kz('Wie heißt der Graph der Mengenbeziehungen in der Produktion?', ['Gozinto-Graph', 'Gozintograph', 'Gozinto'], '', 1),
    rv('Erklären Sie, wie man den Einzelteilbedarf für einen Produktionsplan p berechnet.', 'Zuerst Baugruppenbedarf b = M_BE · p, dann Einzelteilbedarf x = M_TB · b. Oder direkt mit der Gesamtbedarfsmatrix C = M_TB · M_BE: x = C · p.', ['b = M_BE·p', 'x = M_TB·b', 'C = M_TB·M_BE'], 2, True))

# ================================================================ k8
fam('lgs-gauss', 'grund', 'Löst LGS und deutet Lösbarkeit',
    zu('Wie viele Lösungen?', ['genau eine', 'keine', 'unendlich viele'], [('5x₁ − 2x₂ = −4, x₂ = 5', 0), ('x₁ + x₂ = 0, x₁ + x₂ = 1', 1), ('x₁ + 2x₂ = 3, 2x₁ + 4x₂ = 6', 2)], '', 1, True),
    nu('x + y = {S}, x − y = {D}. Wie groß ist x?', {'S': [10, 30, 2], 'D': [2, 8, 2]}, '(S+D)/2', 'Addieren: 2x = {=S+D} ⇒ x = {=(S+D)/2}', '', 1, lvl=1),
    blk('Richtig oder falsch?', [('Ein LGS kann genau zwei Lösungen haben.', F), ('Zeile 0 = 5 heißt: keine Lösung.', R), ('Vertauschen von Zeilen ist eine elementare Umformung.', R), ('Zwei parallele Geraden haben einen Schnittpunkt.', F)], '', 2, True),
    ns('x₁ + 4x₂ + 3x₃ = 1, 2x₁ + 5x₂ + 4x₃ = 4, x₁ − 3x₂ − 2x₃ = 5. Wert von x₁?', 3, 'Lösung (3; −2; 2)', '', 3, True),
    mc('x₁ + 2x₂ = 3 und 2x₁ + 4x₂ = 6 sind geometrisch …', 'dieselbe Gerade', ['parallel', 'sich schneidend', 'senkrecht'], '', 1),
    li('Nennen Sie die drei elementaren Zeilenumformungen.', [['tauschen', 'vertauschen'], ['multiplizieren', 'mit Zahl multiplizieren'], ['addieren', 'Vielfaches addieren']], '', 2),
    nu('2x + {A}y = {B}, y = 2. Wie groß ist x?', {'A': [1, 6, 1], 'B': [20, 40, 2]}, '(B-2*A)/2', '2x = {B} − {=2*A} ⇒ x = {=(B-2*A)/2}', '', 1, lvl=1),
    rv('Untersuchen Sie x₁ + x₂ = 0, x₁ + x₂ = 1 auf Lösbarkeit und deuten Sie geometrisch.', 'Zieht man die Gleichungen voneinander ab, ergibt sich 0 = 1, ein Widerspruch: keine Lösung. Geometrisch sind es zwei parallele Geraden ohne Schnittpunkt.', ['0 = 1', 'keine Lösung', 'parallele Geraden'], 2, True))
fam('determinante', 'grund', 'Berechnet Determinanten',
    nu('Determinante von [[{A}, {B}], [{C}, {D}]]?', {'A': [1, 9, 1], 'B': [1, 9, 1], 'C': [1, 9, 1], 'D': [1, 9, 1]}, 'A*D-B*C', '{A}·{D} − {B}·{C} = {=A*D-B*C}', '', 0, lvl=1, kl=True),
    ns('det [[2, 4, −3], [−1, 5, 7], [−1, 1, −1]] (Sarrus)?', -68, '−35 − 33', '', 3, True),
    mc('det [[1, 2, 3], [2, 4, 6], [−3, 1, 0]] =', '0', ['12', '−6', '6'], 'Zeile 2 = 2 · Zeile 1.', 2, True),
    blk('Richtig oder falsch?', [('det ≠ 0 heißt: A·x = b ist eindeutig lösbar.', R), ('Sind zwei Zeilen gleich, ist det = 0.', R), ('det [[3, 5], [7, 4]] = 47', F), ('Bei det = 0 existiert die Inverse.', F)], '', 2, True),
    nu('Diagonalmatrix [[{A}, 0, 0], [0, {B}, 0], [0, 0, {C}]]: Determinante?', {'A': [1, 6, 1], 'B': [1, 6, 1], 'C': [1, 6, 1]}, 'A*B*C', 'Produkt der Diagonale: {=A*B*C}', '', 0, lvl=2),
    mc('Sarrus: Wie geht man vor?', 'Hauptdiagonalprodukte minus Nebendiagonalprodukte', ['alle Elemente addieren', 'Diagonale multiplizieren', 'Zeilen tauschen und addieren'], '', 1),
    ns('det [[1, 4, 1], [0, 2, −1], [1, −1, 0]]?', -7, 'Sarrus: 0 − 4 + 0 − (2 + 1 + 0)', '', 3, True),
    rv('Wozu berechnet man in der Klausur die Determinante eines LGS?', 'Ist die Determinante der Koeffizientenmatrix ungleich 0, ist das LGS eindeutig lösbar und die Matrix invertierbar; man kann die Lösung dann mit x = A⁻¹·b berechnen. Ist sie 0, gibt es keine oder unendlich viele Lösungen.', ['det ≠ 0 eindeutig', 'invertierbar', 'det = 0 keine/unendlich'], 2, True))
fam('inverse-matrix', 'grund', 'Invertiert Matrizen und löst LGS',
    mc('Die Inverse existiert genau dann, wenn …', 'det A ≠ 0', ['A symmetrisch ist', 'alle Elemente positiv sind', 'A eine Diagonale hat'], '', 1, True),
    nu('Inverse von [[{A}, 0], [0, {B}]]: Element (1,1)? (3 Stellen)', {'A': [2, 9, 1], 'B': [2, 9, 1]}, '1/A', 'Diagonal: 1/{A} = {=1/A}', '', 3, lvl=1),
    mc('Inverse von \\(\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}\\):', '\\(\\frac{1}{ad - bc}\\begin{pmatrix} d & -b \\\\ -c & a \\end{pmatrix}\\)', ['\\(\\frac{1}{ad - bc}\\begin{pmatrix} a & -b \\\\ -c & d \\end{pmatrix}\\)', '\\(\\begin{pmatrix} 1/a & 1/b \\\\ 1/c & 1/d \\end{pmatrix}\\)', '\\(\\begin{pmatrix} d & b \\\\ c & a \\end{pmatrix}\\)'], '', 2, True),
    blk('Richtig oder falsch?', [('A·A⁻¹ = E', R), ('Bei A·x = b ist x = A⁻¹·b.', R), ('Gauß-Jordan: (A | E) → (E | A⁻¹)', R), ('x = b·A⁻¹', F)], '', 2, True),
    ns('D = [[1,4,3],[2,5,4],[1,−3,−2]], b = (1, 4, 5). Wert von x₃ = (D⁻¹·b)₃?', 2, 'x = (3; −2; 2)', '', 3, True),
    nu('A⁻¹ = [[2, −1], [−1, 1]], b = ({X}, {Y}). Erste Komponente von x = A⁻¹·b?', {'X': [1, 9, 1], 'Y': [1, 9, 1]}, '2*X-Y', '2·{X} − {Y} = {=2*X-Y}', '', 0, lvl=2, kl=True),
    rh('Ordnen Sie das Vorgehen der Klausuraufgabe.', ['Determinante berechnen', 'eindeutige Lösbarkeit folgern', 'Inverse berechnen', 'x = A⁻¹·b', 'Probe A·x = b'], '', 1, True),
    rv('Lösen Sie D·x = b mit D = [[1,4,3],[2,5,4],[1,−3,−2]], b = (1, 4, 5) über die Inverse.', 'det D = 1 ≠ 0, also eindeutig lösbar. D⁻¹ = [[2, −1, 1], [8, −5, 2], [−11, 7, −3]]. x = D⁻¹·b = (2 − 4 + 5; 8 − 20 + 10; −11 + 28 − 15) = (3; −2; 2). Probe: 3 − 8 + 6 = 1 ✓.', ['det = 1', 'D⁻¹', 'x = (3; −2; 2)', 'Probe'], 3, True))

# ================================================================ k9
fam('partielle-ableitung', 'grund', 'Leitet partiell ab',
    mc('\\(f(x,y) = x^2 y\\). Was ist \\(f_y\\)?', '\\(x^2\\)', ['\\(2xy\\)', '\\(2x\\)', '\\(x^2 y\\)'], '', 1),
    mc('\\(f(x,y) = (xy)^3 + xy^2\\). Was ist \\(f_x\\)?', '\\(3x^2y^3 + y^2\\)', ['\\(3x^2y^3 + 2xy\\)', '\\(3(xy)^2\\)', '\\(x^3y^3 + y^2\\)'], '', 2),
    nu('f(x, y) = {A}x²y + {B}y. Berechnen Sie f_x an der Stelle (1; 2).', {'A': [1, 9, 1], 'B': [1, 9, 1]}, '4*A', 'f_x = {=2*A}xy ⇒ {=2*A}·1·2 = {=4*A}', '', 0, lvl=1),
    nu('f(x, y) = {A}x²y + {B}y. Berechnen Sie f_y an der Stelle (1; 2).', {'A': [1, 9, 1], 'B': [1, 9, 1]}, 'A+B', 'f_y = {A}x² + {B} ⇒ {=A+B}', '', 0, lvl=1),
    blk('Richtig oder falsch?', [('Beim Ableiten nach x ist y konstant.', R), ('Der Gradient ist (f_x, f_y).', R), ('Die Hesse-Matrix enthält die ersten Ableitungen.', F), ('Für stetige 2. Ableitungen gilt f_xy = f_yx.', R)], '', 2, True),
    zu('Welche Ableitung?', ['f_x', 'f_y'], [('2xy für f = x²y', 0), ('x² für f = x²y', 1), ('3y² für f = x + y³', 1), ('1 für f = x + y³', 0)], '', 1),
    kz('Wie heißt die Matrix der zweiten partiellen Ableitungen?', ['Hesse-Matrix', 'Hessematrix', 'Hesse'], '', 2),
    rv('Bilden Sie die partiellen Ableitungen von \\(f(x,y) = e^{x + y^2}\\).', 'f_x = e^(x + y²) · 1 (innere Ableitung nach x ist 1). f_y = e^(x + y²) · 2y (innere Ableitung nach y ist 2y).', ['f_x = e^(x+y²)', 'f_y = 2y·e^(x+y²)', 'Kettenregel'], 2))
fam('grenzprodukt', 'grund', 'Berechnet und deutet Grenzprodukte',
    nu('Y = 80·L^0,6·K^0,4, L = {L}, K = {K}. Grenzprodukt der Arbeit (2 Stellen)?', {'L': [500, 2000, 500], 'K': [100, 500, 100]}, '48*(K/L)**0.4', '∂Y/∂L = 48·(K/L)^0,4 = {=48*(K/L)**0.4}', '', 2, lvl=2, kl=True),
    nu('Y = 80·L^0,6·K^0,4, L = {L}, K = {K}. Grenzprodukt des Kapitals (2 Stellen)?', {'L': [500, 2000, 500], 'K': [100, 500, 100]}, '32*(L/K)**0.6', '∂Y/∂K = 32·(L/K)^0,6 = {=32*(L/K)**0.6}', '', 2, lvl=2, kl=True),
    ns('Y = 90·L^0,8·K^0,2, L = 1.000, K = 200. Grenzprodukt der Arbeit (2 Stellen)?', 52.18, '72 · 0,2^0,2', '', 3, True),
    mc('Partielle Ableitung von \\(Y = 80L^{0{,}6}K^{0{,}4}\\) nach L:', '\\(48L^{-0{,}4}K^{0{,}4}\\)', ['\\(48L^{0{,}4}K^{0{,}4}\\)', '\\(32L^{0{,}6}K^{-0{,}6}\\)', '\\(80L^{-0{,}4}\\)'], '', 1, True),
    blk('Richtig oder falsch?', [('Das Grenzprodukt der Arbeit gilt bei konstantem Kapital.', R), ('Bei a < 1 sinkt das Grenzprodukt, wenn L steigt.', R), ('Ohne Interpretation gibt es volle Punkte.', F), ('∂Y/∂K = b·c·L^a·K^(b−1)', R)], '', 2, True),
    mc('∂Y/∂L ≈ 25,21 bedeutet …', 'eine Arbeitseinheit mehr bringt etwa 25,21 Outputeinheiten mehr', ['der Output beträgt 25,21', 'Kapital und Arbeit steigen um 25,21 %', 'die Kosten steigen um 25,21'], '', 2, True),
    lu('Bei der Partialanalyse bleiben alle anderen Faktoren [[0]].', [['konstant', 'gleich']], '', 1),
    rv('Bestimmen und interpretieren Sie die partiellen Grenzprodukte von \\(Y = 80 L^{0{,}6} K^{0{,}4}\\) bei L = 1.500 AE, K = 300 GE.', '∂Y/∂L = 48·(K/L)^0,4 = 48·0,2^0,4 ≈ 25,21: Eine zusätzliche Arbeitseinheit erhöht den Output um etwa 25,21 Einheiten (K konstant). ∂Y/∂K = 32·(L/K)^0,6 = 32·5^0,6 ≈ 84,05: Eine zusätzliche Geldeinheit Kapital erhöht den Output um etwa 84,05 Einheiten (L konstant).', ['∂Y/∂L ≈ 25,21', '∂Y/∂K ≈ 84,05', 'Interpretation ceteris paribus'], 3, True))
fam('totales-differential', 'grund', 'Nutzt das totale Differential',
    mc('Das totale Differential lautet …', '\\(df = f_x\\,dx + f_y\\,dy\\)', ['\\(df = f_x \\cdot f_y\\)', '\\(df = dx + dy\\)', '\\(df = f(x + dx, y)\\)'], '', 1),
    nu('f_x = {A}, f_y = {B}; dx = 0,1, dy = −0,2. df?', {'A': [2, 9, 1], 'B': [2, 9, 1]}, '0.1*A-0.2*B', '{A}·0,1 + {B}·(−0,2) = {=0.1*A-0.2*B}', '', 2, lvl=1),
    blk('Richtig oder falsch?', [('Das totale Differential ist eine Näherung für kleine Änderungen.', R), ('Inputverringerungen gehen mit negativem Vorzeichen ein.', R), ('Es gilt exakt für beliebig große Änderungen.', F), ('Es addiert die partiellen Wirkungen.', R)], '', 2, True),
    ns('Blatt 9, A2: totale Output-Änderung (3 Stellen)?', 0.021, '0,3446·0,2 − 0,3141·0,1 − 0,1607·0,1', '', 3),
    mc('Was beschreibt das totale Differential ökonomisch?', 'die Gesamtänderung des Outputs bei gleichzeitiger Inputänderung', ['den maximalen Output', 'die Kosten je Stück', 'den Gleichgewichtspreis'], '', 2),
    nu('Y_L = {A}, Y_K = {B}; L steigt um {DL}, K sinkt um 1. dY?', {'A': [10, 30, 5], 'B': [40, 90, 10], 'DL': [2, 6, 1]}, 'A*DL-B', '{A}·{DL} − {B}·1 = {=A*DL-B}', '', 0, lvl=2),
    kz('Wie heißt df = f_x dx + f_y dy?', ['totales Differential', 'vollständiges Differential'], '', 1),
    rv('Erklären Sie, wie man mit dem totalen Differential die Output-Änderung abschätzt, wenn r₁ steigt und r₂, r₃ sinken.', 'Man berechnet die partiellen Grenzprodukte an der Stelle, multipliziert jedes mit der Änderung seines Inputs (Erhöhung positiv, Verringerung negativ) und addiert: dY = f₁·dr₁ + f₂·dr₂ + f₃·dr₃.', ['partielle Grenzprodukte', 'mal Änderung mit Vorzeichen', 'addieren'], 2))

# ---- Folienabgleich: Gliederung und Übungsblätter
fam('saettigungswert', 'fa-uneigentlich', 'Erkennt uneigentliche Grenzwerte',
    mc(r'\(\lim_{x \downarrow 0} \frac{1}{x}\) ist …', r'uneigentlich: \(+\infty\)', [r'\(0\)', r'\(1\)', r'\(-\infty\)'], 'Von rechts werden die Werte beliebig groß; von links geht es gegen −∞.', 2),
    mc(r'Was bedeutet \(\lim_{x\to\infty} f(x) = \infty\)?', 'f wächst über jede Schranke; es gibt keinen echten (endlichen) Grenzwert', ['f hat den Grenzwert „unendlich“ als Zahl', 'f ist an dieser Stelle stetig', 'f nähert sich einer waagerechten Asymptote'], 'Uneigentlicher Grenzwert.', 2),
    mc(r'\(\lim_{x\to\infty} \frac{x^3 + 1}{2x^2}\)', r'\(\infty\) (uneigentlich)', [r'\(\frac{1}{2}\)', r'\(0\)', r'\(1\)'], 'Zählergrad > Nennergrad.', 2))
fam('partielle-ableitung', 'fa-hesse', 'Kennt Hesse-Matrix und stetige partielle Differenzierbarkeit',
    mc(r'Hesse-Matrix des Paraboloids \(f(x,y) = x^2 + y^2\)?', r'\(\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}\)', [r'\(\begin{pmatrix} 2x & 0 \\ 0 & 2y \end{pmatrix}\)', r'\(\begin{pmatrix} 0 & 2 \\ 2 & 0 \end{pmatrix}\)', r'\(\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}\)'], 'f_xx = 2, f_yy = 2, f_xy = 0.', 2),
    mc('Was gilt bei zweimal stetig partiell differenzierbaren Funktionen?', r'Die Hesse-Matrix ist symmetrisch (\(f_{xy} = f_{yx}\))', ['Alle zweiten Ableitungen sind null', 'Der Gradient ist immer null', 'Die Hesse-Matrix ist eine Diagonalmatrix'], 'Satz von Schwarz.', 2),
    mc('Stetig partiell differenzierbar heißt …', 'alle partiellen Ableitungen existieren und sind stetig', ['die Funktion ist überall null', 'nur die erste partielle Ableitung existiert', 'die Funktion hat keine Extrema'], '', 2))
fam('determinante', 'fa-uebung', 'Rechnet Determinanten aus den Übungen',
    mc(r'\(\det \begin{pmatrix} 3 & 5 \\ 7 & 4 \end{pmatrix}\)', r'\(-23\)', [r'\(23\)', r'\(47\)', r'\(-47\)'], '3·4 − 5·7 = 12 − 35.', 1, True),
    mc(r'Ist \(\begin{pmatrix} 1 & 2 & -1 \\ 2 & 4 & 2 \\ -4 & -8 & -8 \end{pmatrix}\) invertierbar?', 'nein, die Determinante ist 0', ['ja, die Determinante ist 4', 'ja, weil sie quadratisch ist', 'nein, weil sie negative Einträge hat'], 'Spalte 2 = 2 · Spalte 1.', 2, True))
fam('lhospital', 'fa-polydiv', 'Führt Polynomdivisionen durch',
    mc(r'\((x^3 - 12x^2 + 5x + 150) : (x - 5)\)', r'\(x^2 - 7x - 30\)', [r'\(x^2 - 17x + 90\)', r'\(x^2 - 7x + 30\)', r'\(x^2 + 7x - 30\)'], 'Rest 0: x = 5 ist Nullstelle.', 2, True),
    mc(r'\((7x^5 - 2x^4 - 63x^3 + 33x^2 - 135) : (x^2 - 9)\)', r'\(7x^3 - 2x^2 + 15\)', [r'\(7x^3 - 2x^2 - 15\)', r'\(7x^3 + 2x^2 + 15\)', r'\(7x^2 - 2x + 15\)'], 'Rest 0.', 2, True))
fam('stetigkeit', 'fa-zws', 'Wendet den Zwischenwertsatz an',
    mc(r'f ist stetig auf [1; 2], f(1) = −3, f(2) = 4. Was folgt?', 'f hat in (1; 2) mindestens eine Nullstelle', ['f hat in (1; 2) genau zwei Nullstellen', 'f ist auf [1; 2] streng monoton', 'f hat in (1; 2) keine Nullstelle'], 'Zwischenwertsatz.', 2),
    mc('Welches Polynom hat sicher eine reelle Nullstelle?', r'\(x^3 - 7x + 100\)', [r'\(x^4 + 1\)', r'\(x^2 + 5\)', r'\(x^6 + x^2 + 3\)'], 'Ungerader Grad.', 2))
fam('funktion', 'fa-elementar', 'Kennt elementare Funktionen',
    mc(r'\(\lfloor -1{,}3 \rfloor =\)', r'\(-2\)', [r'\(-1\)', r'\(1\)', r'\(-1{,}3\)'], 'Größte ganze Zahl ≤ −1,3.', 2),
    mc(r'Wie viele reelle Nullstellen hat \(x^2 + 2x + 5\)?', 'keine', ['eine', 'zwei', 'drei'], r'\(b^2 - 4ac = 4 - 20 < 0\).', 1),
    mc(r'\(f(x) = \frac{a}{x}\) heißt …', 'Hyperbelfunktion (umgekehrt proportional)', ['Wurzelfunktion', 'Betragsfunktion', 'Exponentialfunktion'], '', 1))
fam('matrizen', 'fa-besondere', 'Erkennt besondere Matrizen',
    mc(r'\(\begin{pmatrix} 2 & 5 \\ 0 & 3 \end{pmatrix}\) ist …', 'eine obere Dreiecksmatrix', ['eine Diagonalmatrix', 'eine Einheitsmatrix', 'nicht quadratisch'], 'Unter der Diagonale steht 0, über ihr nicht.', 1))
