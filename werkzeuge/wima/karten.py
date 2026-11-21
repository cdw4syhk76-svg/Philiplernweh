"""Erzeugt inhalte/wima/karten.json. Aufruf: python3 werkzeuge/wima/karten.py"""
import json, pathlib
from collections import Counter
ROOT = pathlib.Path(__file__).resolve().parents[2]
K = {
'zahlenmengen': [('Zahlenmengen ineinander', 'ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ'), ('Ungleichung mal negative Zahl', 'Zeichen dreht sich um'), ('Intervall [a; b] vs. (a; b)', 'mit Rändern vs. ohne Ränder')],
'terme': [('Potenzgesetze (3)', 'aᵐ·aⁿ = aᵐ⁺ⁿ; (aᵐ)ⁿ = aᵐⁿ; a⁻ⁿ = 1/aⁿ'), ('Wurzel als Potenz', 'ⁿ√(aᵐ) = a^(m/n), z. B. ∛x² = x^(2/3)'), ('Binomische Formeln', '(a+b)² = a²+2ab+b²; (a−b)² = a²−2ab+b²; (a+b)(a−b) = a²−b²'), ('Darf man (x+2)/x kürzen?', 'Nein, x ist Summand; nur Faktoren kürzen.')],
'ungleichungen': [('Quadratische Ungleichung lösen', 'Nullstellen, Öffnung, Bereich ablesen'), ('x² + 2x − 3 < 0', '(−3; 1)'), ('x² − 4x > 0', '(−∞; 0) ∪ (4; ∞)'), ('Bruchungleichung', 'Fallunterscheidung nach dem Vorzeichen des Nenners')],
'folgen': [('Teilfolge', 'unendlich viele Glieder in Reihenfolge; konvergiert die Folge gegen a, dann jede Teilfolge'), ('Arithmetische Folge', 'aₙ = a₀ + n·d (konstante Differenz)'), ('Geometrische Folge', 'aₙ = a₀·qⁿ (konstanter Quotient)'), ('Zinseszins 50.000 €, 5 %, 10 Jahre', '≈ 81.444,73 €'), ('Beschränkte Folge', '|aₙ| ≤ M für alle n')],
'grenzwert-folge': [('Bruchfolge, Zählergrad < Nennergrad', 'Grenzwert 0'), ('Bruchfolge, gleicher Grad', 'Quotient der Leitkoeffizienten'), ('Konvergent ⇒ ?', 'beschränkt (Umkehrung gilt nicht)'), ('(−1)ⁿ·(n+3)/n', 'divergent (pendelt)')],
'funktion': [('Gaußklammer ⌊x⌋', 'größte ganze Zahl ≤ x, z. B. ⌊2,7⌋ = 2, ⌊−1,3⌋ = −2'), ('Dreiecksungleichung', '|x + y| ≤ |x| + |y|'), ('Hyperbelfunktion', 'f(x) = a/x, x ≠ 0: umgekehrt proportional'), ('Drei Einschränkungen des Definitionsbereichs', 'Nenner ≠ 0, Radikand ≥ 0, ln-Argument > 0'), ('Funktion: Definition', 'jedem x ∈ D genau ein f(x)'), ('D von ln(4 − x²)', '(−2; 2)'), ('D von √(t − 16)', '[16; ∞)')],
'verkettung': [('(f∘g)(x)', 'f(g(x)): erst g (innen), dann f (außen)'), ('Gilt f∘g = g∘f?', 'meist nicht'), ('Zerlegung cos(x²)', 'innen x², außen cos'), ('Zerlegung cos(sin²x)', 'innen sin x, Mitte Quadrat, außen cos')],
'umkehrfunktion': [('Umkehrfunktion bilden', 'nach x auflösen, x und y tauschen'), ('Graph der Umkehrfunktion', 'Spiegelung an y = x'), ('D(f⁻¹) =', 'W(f)'), ('Wann umkehrbar?', 'wenn eindeutig, z. B. streng monoton')],
'exp-ln': [('ln(a·b), ln(aᵇ)', 'ln a + ln b; b·ln a'), ('e^(ln x), ln(eˣ)', 'x; x'), ('eˣ für x → −∞', '→ 0'), ('Definitionsbereich ln x', 'x > 0')],
'saettigungswert': [('Uneigentlicher Grenzwert', 'f wächst über jede Schranke: lim f = ∞ (bzw. −∞), z. B. 1/x für x ↓ 0; typisch an Polstellen'), ('Sättigungswert a/(b + c·e^(−kt))', 'a/b (weil e^(−kt) → 0)'), ('180/(0,5 + 10e^(−0,5t)) für t → ∞', '360'), ('210/(0,1 + 20e^(−kt)) für t → ∞', '2.100'), ('(4y² − 160)/(y² + 4y) für y → ∞', '4')],
'stetigkeit': [('Zwischenwertsatz', 'f stetig auf [a,b], f(a) < 0 < f(b) ⇒ es gibt x ∈ (a,b) mit f(x) = 0'), ('Polynom ungeraden Grades', 'hat mindestens eine reelle Nullstelle (Zwischenwertsatz)'), ('Stetig in x₀', 'linker GW = rechter GW = f(x₀)'), ('Sprung, Pol, Lücke', 'Sprung: einseitige GW verschieden; Pol: ±∞; Lücke: GW existiert, aber ≠ f(x₀) oder x₀ ∉ D'), ('Konstante c für Stetigkeit', 'beide Teile an der Nahtstelle gleichsetzen'), ('Rabattstaffel', 'Sprungstellen, nicht monoton')],
'differentialquotient': [('Differentialquotient', "f′(x₀) = lim(h→0) [f(x₀+h) − f(x₀)]/h"), ('Geometrische Bedeutung', 'Tangentensteigung'), ('Ökonomische Bedeutung', 'Grenzfunktion, z. B. Grenzkosten K′(x)')],
'ableitungsregeln': [('Potenzregel', "(xⁿ)′ = n·xⁿ⁻¹"), ("(eˣ)′, (ln x)′", 'eˣ; 1/x'), ("(sin x)′, (cos x)′", 'cos x; −sin x'), ("(√x)′", '1/(2√x)')],
'produkt-quotient': [('Produktregel', "(u·v)′ = u′v + uv′"), ('Quotientenregel', "(u/v)′ = (u′v − uv′)/v²"), ("(cos x · e^(x²+4))′", 'e^(x²+4)(2x cos x − sin x)'), ('Merkspruch Quotientenregel', 'NAZ minus ZAN durch N²')],
'kettenregel': [('Kettenregel', 'äußere Ableitung mal innere Ableitung'), ("((5t+3)³)′", '15(5t+3)²'), ("(cos(sin²x))′", '−sin(sin²x)·2 sin x cos x'), ("(e^(x²))′", '2x·e^(x²)')],
'lhospital': [("L'Hospital", 'bei 0/0 oder ∞/∞: lim f/g = lim f′/g′'), ('lim ln x/(x−1), x → 1', '1'), ('lim x⁴/eˣ, x → ∞', '0'), ('Polynomdivision Rest 0', 'Divisor-Nullstelle ist Nullstelle')],
'kurvendiskussion': [('Hochpunkt', "f′ = 0 und f″ < 0"), ('Tiefpunkt', "f′ = 0 und f″ > 0"), ('Wendepunkt', "f″ = 0 und f‴ ≠ 0"), ('Ablauf Kurvendiskussion', 'D, Nullstellen, Extrema, Wendepunkte, Ränder')],
'kostenfunktion': [('Fixkosten', 'K(0), bei ax³+bx²+cx+d: d'), ('Stückkosten', 'k(x) = K(x)/x'), ('Grenzkosten', "K′(x)"), ('Von K′ zu K', 'integrieren; Konstante = Fixkosten')],
'gewinnzone': [('Gewinnfunktion', 'G(x) = U(x) − K(x)'), ('Gewinnschwelle', 'kleinste Menge mit G = 0, ab der Gewinn entsteht'), ('Gewinngrenze', 'größte Menge mit G = 0'), ('Nullstelle raten', 'Teiler des Absolutglieds probieren, dann Polynomdivision')],
'gewinnmaximum': [('Gewinnmaximum', "G′ = 0, G″ < 0"), ('Gleichwertige Bedingung', "Grenzumsatz = Grenzkosten (U′ = K′)"), ('Bei festem Preis p', "K′(x) = p"), ('Zahnpasta-Beispiel', 'x ≈ 10,77, G ≈ 384,90')],
'betriebsoptimum': [('Betriebsoptimum', "Minimum der Stückkosten; K′ = k"), ('Betriebsminimum', 'Minimum der variablen Stückkosten'), ('Langfristige Preisuntergrenze', 'minimale Stückkosten'), ('Kurzfristige Preisuntergrenze', 'minimale variable Stückkosten')],
'angebot-nachfrage': [('Marktgleichgewicht', 'f_A(x) = f_N(x)'), ('Verlauf Angebot/Nachfrage', 'Angebot steigend, Nachfrage fallend'), ('Umsatz mit Preis-Absatz-Funktion', 'U(x) = p(x)·x')],
'stammfunktion': [('Stammfunktion', "F′ = f"), ('∫ xⁿ dx', 'xⁿ⁺¹/(n+1) + C (n ≠ −1)'), ('∫ 1/x dx', 'ln|x| + C'), ('∫ sin x dx, ∫ cos x dx', '−cos x + C; sin x + C')],
'bestimmtes-integral': [('Hauptsatz', '∫ₐᵇ f dx = F(b) − F(a)'), ('Fläche unter der x-Achse', 'zählt negativ'), ('∫₀^π x cos x dx', '−2')],
'substitution': [('Substitution: Idee', 'Kettenregel rückwärts; u = g(x), du = g′(x)dx'), ('Grenzen bei Substitution', 'umrechnen oder zurücksubstituieren'), ('∫₀¹ 2x·e^(x²) dx', 'e − 1 ≈ 1,72'), ('∫₀^a 6x/√(3x²+a²) dx', '2a')],
'partielle-integration': [('Partielle Integration', '∫u·v′ = u·v − ∫u′·v'), ('Was wird u?', 'das Polynom (wird beim Ableiten einfacher)'), ('∫₀² t·e^(2t) dt', '¾e⁴ + ¼ ≈ 41,20'), ('∫ x·eˣ dx', '(x − 1)eˣ + C')],
'vektoren': [('Linear unabhängig', 'nur die triviale Linearkombination ergibt 0'), ('Test bei 3 Vektoren im ℝ³', 'det ≠ 0'), ('Linearkombination', 'λ₁a + λ₂b + λ₃c')],
'matrizen': [('Dreiecksmatrix vs. Diagonalmatrix', 'obere Dreiecksmatrix: aᵢⱼ = 0 für i > j\nDiagonalmatrix: aᵢⱼ = 0 für i ≠ j'), ('Transponieren', 'Zeilen werden Spalten; m×n → n×m'), ('((A·B)ᵀ)ᵀ', 'A·B'), ('(A·B)ᵀ', 'Bᵀ·Aᵀ'), ('Addition von Matrizen', 'nur bei gleichem Format, elementweise')],
'matrizenmultiplikation': [('Wann ist A·B definiert?', 'Spalten(A) = Zeilen(B)'), ('Format (m×n)·(n×p)', 'm×p'), ('Element cᵢⱼ', 'Zeile i von A mal Spalte j von B'), ('Ist A·B = B·A?', 'im Allgemeinen nein')],
'mehrstufige-produktion': [('Gesamtbedarfsmatrix', 'C = M_TB · M_BE (bzw. M_RZ · M_ZE)'), ('Baugruppenbedarf', 'b = M_BE · p'), ('Einzelteilbedarf', 'x = M_TB · b = C · p'), ('cᵢⱼ der Gesamtbedarfsmatrix', 'Einzelteile i je Endprodukt j')],
'lgs-gauss': [('Lösungsmöglichkeiten eines LGS', 'keine, genau eine, unendlich viele'), ('Elementare Zeilenumformungen', 'tauschen, mit Zahl ≠ 0 multiplizieren, Vielfaches addieren'), ('Zeile 0 = c (c ≠ 0)', 'keine Lösung'), ('Geometrie bei 2 Variablen', 'Schnittpunkt / parallel / identisch')],
'determinante': [('2×2-Determinante', 'ad − bc'), ('Sarrus', '3 Hauptdiagonalprodukte minus 3 Nebendiagonalprodukte'), ('det ≠ 0 bedeutet', 'eindeutig lösbar, invertierbar'), ('Zwei Zeilen Vielfache', 'det = 0')],
'inverse-matrix': [('Inverse', 'A·A⁻¹ = E; nur bei det ≠ 0'), ('Gauß-Jordan', '(A | E) → (E | A⁻¹)'), ('Inverse 2×2', '1/(ad−bc)·[[d, −b], [−c, a]]'), ('LGS mit Inverse', 'x = A⁻¹·b')],
'partielle-ableitung': [('Stetig partiell differenzierbar', 'alle partiellen Ableitungen existieren und sind stetig → f differenzierbar, f_xy = f_yx'), ('Hesse-Matrix: Eigenschaften', 'n × n, symmetrisch; positiv definit → Min, negativ definit → Max, indefinit → Sattel'), ('Paraboloid x² + y²', '∇f = (2x, 2y), H = (2 0; 0 2), Minimum in (0,0)'), ('Partielle Ableitung nach x', 'alle anderen Variablen konstant'), ('Gradient', '(f_x, f_y)'), ('Hesse-Matrix', 'Matrix der zweiten partiellen Ableitungen'), ('f = (xy)³ + xy²: f_x', '3x²y³ + y²')],
'grenzprodukt': [('∂Y/∂L bei Y = c·L^a·K^b', 'a·c·L^(a−1)·K^b'), ('Y = 80L^0,6K^0,4, L = 1.500, K = 300', '∂Y/∂L ≈ 25,21; ∂Y/∂K ≈ 84,05'), ('Interpretation Grenzprodukt der Arbeit', 'Output-Zuwachs je zusätzlicher Arbeitseinheit bei konstantem Kapital'), ('Was wird in der Klausur zusätzlich verlangt?', 'Interpretation der Grenzprodukte')],
'totales-differential': [('Totales Differential', 'df = f_x dx + f_y dy (+ f_z dz)'), ('Bedeutung', 'Näherung der Gesamtänderung bei kleinen Änderungen'), ('Verringerung eines Inputs', 'geht mit negativem Vorzeichen ein')],
}
fach = json.loads((ROOT / 'inhalte/wima/fach.json').read_text())
ids = [t['id'] for k in fach['kapitel'] for t in k['themen']]
assert set(K) == set(ids), (set(ids) - set(K), set(K) - set(ids))
karten = [{'t': t, 'v': v, 'r': r} for t in ids for v, r in K[t]]
vs = [k['v'] for k in karten]; assert len(vs) == len(set(vs)), [v for v in vs if vs.count(v) > 1]
(ROOT / 'inhalte/wima/karten.json').write_text('{\n "karten": [\n' + ',\n'.join('  ' + json.dumps(x, ensure_ascii=False) for x in karten) + '\n ]\n}\n')
gl = json.loads((ROOT / 'inhalte/wima/glossar.json').read_text())['begriffe']
c = Counter(k['t'] for k in karten) + Counter(g['heimat'] for g in gl) + Counter(ids)
print(f'wima: {len(karten)} Karten; unter 5 je Unterthema: {({t: n for t, n in c.items() if n < 5})}')
