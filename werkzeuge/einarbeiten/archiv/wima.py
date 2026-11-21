"""Mathe: Stoff der handschriftlichen Mitschrift (Einstieg_compressed, 63 S.), der auf den Lernseiten fehlte (Runde b1, 13.11.2026).
Jede Seite als Bild gelesen (Texterkennung der Handschrift taugt nicht). Format: werkzeuge/einarbeiten.py.
Schreibweise wie in der Mitschrift (Definition/Satz/Bemerkung). Laut Mitschrift (S. 53): keine Definitionen auswendig, aber
Nachweis „n von ε“, Nachweis Stetigkeit mit ε, Differenzierbarkeit mit η, Determinante 4×4."""
STAND = 'b1'
KC = '<h3>Kurz-Check: richtig oder falsch?</h3>'


def vor_kc(t, html, frage=True):
    return dict(t=t, vor=KC, block=html, **({} if frage is True else {'frage': frage}))


E = [
 # ---------------- 1 Zahlen ----------------
 vor_kc('zahlenmengen',
  '<h3>Aus der Mitschrift: Zahlen, Verknüpfungen, Axiome</h3>'
  '<p>\\(\\mathbb{N}_0 = \\{0\\} \\cup \\mathbb{N}\\) ist die Menge der natürlichen Zahlen plus Null. Rationale Zahlen \\(\\mathbb{Q} = \\{p/q : p, q \\in \\mathbb{Z},\\ q \\ne 0\\}\\) sind '
  '<b>periodische</b> (\\(\\tfrac13 = 0{,}333\\ldots\\)) oder <b>abbrechende</b> Dezimalzahlen (\\(\\tfrac12 = 0{,}5\\)). \\(\\mathbb{R} = \\mathbb{Q} \\cup \\{\\text{irrationale Zahlen}\\}\\); '
  '<b>irrationale Zahlen</b> sind nicht periodisch und nicht abbrechend, z. B. \\(\\pi\\), \\(e\\), \\(\\sqrt2\\).</p>'
  '<p>Man betrachtet die reellen Zahlen mit den beiden <b>Verknüpfungen</b> Addition \\(\\mathbb{R}\\times\\mathbb{R}\\to\\mathbb{R},\\ (x, y)\\mapsto x + y\\) und Multiplikation \\((x, y)\\mapsto x\\cdot y\\). Sie genügen den Axiomen:</p>'
  '<ul><li><b>Axiome der Addition</b>: I.1 Assoziativgesetz \\(x + (y + z) = (x + y) + z\\) · I.2 Kommutativgesetz · I.3 Existenz der Null (\\(x + 0 = x\\)) · I.4 Existenz des Negativen (\\(x + (-x) = 0\\)).</li>'
  '<li><b>Axiome der Multiplikation</b>: II.1 Assoziativgesetz · II.2 Kommutativgesetz · II.3 Existenz der Eins (\\(1 \\ne 0,\\ x\\cdot 1 = x\\)) · II.4 Existenz des Inversen (\\(x \\ne 0:\\ x\\cdot x^{-1} = 1\\)).</li>'
  '<li><b>III. Distributivgesetz</b> \\(x\\cdot(y + z) = x\\cdot y + x\\cdot z\\).</li></ul>'
  '<p>Die Axiome gelten für die reellen und die rationalen Zahlen, nicht für die ganzen bzw. natürlichen Zahlen (in \\(\\mathbb{Z}\\) fehlt das Inverse, in \\(\\mathbb{N}\\) schon die Null). '
  'Aus ihnen folgen alle Rechenregeln, z. B. \\(x\\cdot y = 0 \\Leftrightarrow x = 0\\) oder \\(y = 0\\); die <b>Division durch Null</b> ist nicht definiert (die Null hat kein Inverses).</p>'
  '<p><b>Anordnungsaxiome</b>: (A.1) Für jedes x gilt genau eine der drei Beziehungen \\(x > 0\\), \\(x = 0\\), \\(-x > 0\\). (A.2) \\(x > 0,\\ y > 0 \\Rightarrow x + y > 0\\). (A.3) \\(x > 0,\\ y > 0 \\Rightarrow x\\cdot y > 0\\). '
  'Man setzt \\(x > y\\), falls \\(x - y > 0\\). Folgerungen: <b>Transitivität</b> \\(x < y,\\ y < z \\Rightarrow x < z\\) und \\(0 < x < y \\Rightarrow \\tfrac1x > \\tfrac1y\\).</p>'),
 # ---------------- 2 Folgen ----------------
 vor_kc('folgen',
  '<h3>Aus der Mitschrift: Beispiele von Folgen</h3>'
  '<p>Unter einer <b>Folge reeller Zahlen</b> versteht man eine Abbildung \\(\\mathbb{N}_0 \\to \\mathbb{R},\\ n \\mapsto a_n\\); \\(a_n\\) ist das n-te Glied. Schreibweise \\((a_n)_{n\\in\\mathbb{N}_0}\\) oder \\((a_0, a_1, a_2, \\ldots)\\).</p>'
  '<ul><li><b>konstante Folge</b> \\(a_n = a\\): \\((a, a, a, \\ldots)\\)</li>'
  '<li><b>harmonische Folge</b> \\(a_n = \\tfrac1n\\): \\((1, \\tfrac12, \\tfrac13, \\ldots)\\)</li>'
  '<li><b>alternierende Folge</b> \\(a_n = (-1)^n\\): \\((1, -1, 1, -1, \\ldots)\\)</li>'
  '<li><b>geometrische Folge</b> \\(a_n = b^n\\): der Quotient zweier benachbarter Glieder ist konstant, \\(\\tfrac{b^n}{b^{n-1}} = b\\)</li>'
  '<li><b>arithmetische Folge</b>: die Differenz zweier benachbarter Glieder ist immer gleich, z. B. die ungeraden Zahlen \\(1, 3, 5, 7, \\ldots\\) (\\(5 - 3 = 2\\))</li>'
  '<li><b>rekursiv definierte Folge</b> (man muss die Vorgänger kennen): die Folge der <b>Fibonacci-Zahlen</b> \\(a_0 = 1,\\ a_1 = 1,\\ a_n = a_{n-1} + a_{n-2}\\) für \\(n \\ge 2\\): \\((1, 1, 2, 3, 5, 8, 13, 21, \\ldots)\\). Das Verhältnis zweier aufeinanderfolgender Glieder nähert sich dem <b>goldenen Schnitt</b>.</li></ul>'),
 vor_kc('grenzwert-folge',
  '<h3>Aus der Mitschrift: Grenzwert nachweisen („n von ε“)</h3>'
  '<p><b>Definition</b>: Die Folge \\((a_n)\\) heißt <b>konvergent</b> gegen den Grenzwert a, falls es zu jedem \\(\\varepsilon > 0\\) ein \\(N(\\varepsilon) \\in \\mathbb{N}\\) gibt, so dass \\(|a_n - a| < \\varepsilon\\) für alle \\(n \\ge N(\\varepsilon)\\). '
  'N(ε) bedeutet, dass diese natürliche Zahl von ε abhängt: Je kleiner ε, desto größer muss man N wählen. Eine Folge, die gegen 0 konvergiert, heißt <b>Nullfolge</b>; eine Folge, die gegen keine reelle Zahl konvergiert, heißt <b>divergent</b>.</p>'
  '<p><b>Nachweis</b> (immer gleich aufgebaut): Sei \\(\\varepsilon > 0\\) beliebig; wähle \\(N(\\varepsilon)\\) passend; zeige \\(|a_n - a| < \\varepsilon\\) für \\(n \\ge N(\\varepsilon)\\).</p>'
  '<ul><li>\\(\\lim \\tfrac1n = 0\\): wähle \\(N(\\varepsilon) > \\tfrac1\\varepsilon\\). Dann \\(|\\tfrac1n - 0| = \\tfrac1n \\le \\tfrac{1}{N(\\varepsilon)} < \\varepsilon\\).</li>'
  '<li>\\(\\lim \\tfrac{n}{n+1} = 1\\): wähle \\(N(\\varepsilon) > \\tfrac1\\varepsilon\\). Dann \\(|\\tfrac{n}{n+1} - 1| = |\\tfrac{-1}{n+1}| = \\tfrac{1}{n+1} < \\tfrac{1}{N(\\varepsilon)} < \\varepsilon\\).</li>'
  '<li>\\(\\lim \\tfrac{(-1)^n}{\\sqrt n} = 0\\): wähle \\(N(\\varepsilon) > \\tfrac{1}{\\varepsilon^2}\\). Dann \\(|\\tfrac{(-1)^n}{\\sqrt n}| = \\tfrac{1}{\\sqrt n} \\le \\tfrac{1}{\\sqrt{N(\\varepsilon)}} < \\varepsilon\\).</li>'
  '<li>\\(((-1)^n)\\) divergiert: Angenommen, sie konvergiert gegen a. Für \\(\\varepsilon = 1\\) gäbe es N(1) mit \\(|a_n - a| < 1\\) für \\(n \\ge N(1)\\). Dann \\(2 = |a_{n+1} - a_n| \\le |a_{n+1} - a| + |a - a_n| < 2\\) (Dreiecksungleichung): Widerspruch.</li></ul>'
  '<h3>Aus der Mitschrift: Sätze über Folgen</h3>'
  '<ul><li><b>Satz</b>: Jede konvergente Folge ist beschränkt. Die Umkehrung gilt nicht: \\((-1)^n\\) ist durch M = 1 beschränkt, aber nicht konvergent. '
  'Die Folge der Fibonacci-Zahlen divergiert, denn es gilt \\(a_n \\ge n\\): Sie ist nicht beschränkt und daher divergent.</li>'
  '<li>Das Konvergenzverhalten von \\((b^n)\\) hängt von b ab: \\(|b| < 1\\): \\(\\lim b^n = 0\\) · \\(b = 1\\): konstante Folge, Grenzwert 1 · \\(b = -1\\): \\((-1, 1, -1, \\ldots)\\) divergent · \\(|b| > 1\\): divergent, da unbeschränkt.</li>'
  '<li><b>Eindeutigkeit des Grenzwertes</b>: Konvergiert eine Folge sowohl gegen a als auch gegen ã, dann ist a = ã.</li>'
  '<li>Rechenregeln (Summe, Produkt, Quotient konvergenter Folgen, oben); dazu <b>Corollar</b>: \\(\\lim(\\lambda\\cdot a_n) = \\lambda\\cdot\\lim a_n\\) und \\(\\lim(a_n - b_n) = \\lim a_n - \\lim b_n\\). Beim Quotienten gibt es ein \\(n_0\\), ab dem \\(b_n \\ne 0\\) ist.</li>'
  '<li><b>Satz</b>: Aus \\(a_n < b_n\\) für alle n folgt \\(\\lim a_n \\le \\lim b_n\\), aber nicht notwendig „<“: \\(0 < \\tfrac1n\\), beide Grenzwerte sind 0.</li>'
  '<li>Jede Teilfolge einer konvergenten Folge ist konvergent mit demselben Grenzwert, z. B. \\(\\lim \\tfrac{1}{n^p} = 0\\), denn \\(\\tfrac{1}{n^p}\\) ist eine Teilfolge von \\(\\tfrac1n\\).</li></ul>'),
 # ---------------- 3 Funktionen ----------------
 vor_kc('funktion',
  '<h3>Aus der Mitschrift: Abbildung, Bild und Urbild</h3>'
  '<p><b>Definition</b>: Es seien X und Y zwei nichtleere, sonst beliebige Mengen. Unter einer <b>Funktion oder Abbildung</b> f von X nach Y versteht man eine Vorschrift, die jedem \\(x \\in X\\) in vollkommen eindeutiger Weise genau ein \\(y \\in Y\\) zuordnet. '
  'Das x zugeordnete Element heißt f(x), der <b>Wert der Funktion</b> an der Stelle x oder das <b>Bild</b> von x unter f; x ist ein <b>Urbild</b> von f(x). X heißt <b>Definitionsmenge</b>, Y die <b>Zielmenge</b> von f. '
  'Der <b>Graph</b> von f ist die Menge \\(\\{(x, y) \\in D\\times\\mathbb{R} : y = f(x)\\}\\).</p>'
  '<p>Eigenschaften: (1) Jedes \\(x \\in D\\) tritt als Urbild auf. (2) Aus \\(x_1 = x_2\\) folgt \\(y_1 = y_2\\). (3) Es gibt nicht notwendig zu jedem y ein x mit f(x) = y; die Teilmenge der tatsächlich getroffenen Werte heißt <b>Wertebereich</b>. '
  'Keine Funktion ist z. B. \\(x \\mapsto \\pm\\sqrt x\\) (zwei y-Werte zu einem x).</p>'
  '<p>Weitere Beispiele: <b>konstante Funktion</b> \\(f(x) = c\\), <b>identische Abbildung</b> \\(f(x) = x\\), Funktionen, deren Graph man nicht zeichnen kann (f(x) = 0 für rationale, 1 für irrationale x). '
  'Aus f, g und \\(\\lambda\\) bildet man \\(f + g\\), \\(f\\cdot g\\), \\(\\lambda\\cdot f\\) punktweise und \\(\\tfrac fg\\) auf \\(D\' = \\{x \\in D : g(x) \\ne 0\\}\\).</p>'
  '<p><b>Betrag</b> \\(|x| = x\\) für \\(x \\ge 0\\), sonst \\(-x\\): \\(|x| \\ge 0\\) und \\(|x| = 0 \\Leftrightarrow x = 0\\) · \\(|-x| = |x|\\) · \\(|x\\cdot y| = |x|\\cdot|y|\\) · \\(|\\tfrac xy| = \\tfrac{|x|}{|y|}\\) · Dreiecksungleichung \\(|x + y| \\le |x| + |y|\\) · \\(|x + y| \\ge |x| - |y|\\).</p>'
  '<h3>Trigonometrische Funktionen</h3>'
  '<p>Am Einheitskreis: <b>Sinus</b> = Gegenkathete/Hypotenuse, <b>Kosinus</b> = Ankathete/Hypotenuse; \\(\\sin, \\cos: \\mathbb{R}\\to\\mathbb{R}\\). Eigenschaften:</p>'
  '<ul><li><b>Periodizität</b> (alles wiederholt sich im Abstand des Kreisumfangs \\(2\\pi\\)): \\(\\sin(x + n\\cdot2\\pi) = \\sin x\\), \\(\\cos(x + n\\cdot2\\pi) = \\cos x\\).</li>'
  '<li>Im Intervall \\(0 \\le x < 2\\pi\\) je zwei Nullstellen: \\(\\sin 0 = \\sin\\pi = 0\\), \\(\\cos\\tfrac\\pi2 = \\cos\\tfrac{3\\pi}2 = 0\\).</li>'
  '<li><b>Additionstheoreme</b>: \\(\\cos(x + y) = \\cos x\\cos y - \\sin x\\sin y\\), \\(\\sin(x + y) = \\sin x\\cos y + \\cos x\\sin y\\).</li>'
  '<li>\\(\\cos(-x) = \\cos x\\) (achsensymmetrisch), \\(\\sin(-x) = -\\sin x\\) (punktsymmetrisch); \\(\\sin^2 x + \\cos^2 x = 1\\) (Satz des Pythagoras).</li></ul>'),
 vor_kc('umkehrfunktion',
  '<h3>Aus der Mitschrift: Definition und Preis-Absatz-Funktion</h3>'
  '<p><b>Definition</b>: Eine Funktion \\(f: X\\to Y\\) heißt <b>eindeutig umkehrbar</b>, wenn zu jedem \\(y \\in Y\\) genau ein \\(x \\in X\\) mit f(x) = y existiert. Die Funktion \\(f^{-1}: Y\\to X\\) heißt Umkehrfunktion oder inverse Funktion zu f; es gilt \\(f^{-1}(y) = x \\Leftrightarrow f(x) = y\\). '
  'Vorsicht: \\(f^{-1}(x)\\) nicht mit \\(\\tfrac{1}{f(x)}\\) verwechseln. Beispiel: \\(f(x) = 2x + 1\\): \\(y - 2x - 1 = 0 \\Leftrightarrow x = \\tfrac{y - 1}{2} = f^{-1}(y)\\).</p>'
  '<p><b>Einführendes Beispiel</b>: Die Nachfrage- oder Preis-Absatz-Funktion \\(x = x(p)\\) oder \\(p = p(x)\\) beschreibt den Zusammenhang zwischen dem Preis p eines Gutes und der nachgefragten (abgesetzten) Menge x. '
  'Sie ist in der Regel <b>monoton fallend</b> (Ausnahme: Snob-Effekt). Oft interessiert die umgekehrte Zuordnung: gegeben ein Marktpreis p, gesucht die nachgefragte Menge x, etwa wenn ein Hersteller die Produktionsmenge nach dem erzielbaren Preis richten muss. '
  'Aus \\(p = -2x + 8\\) folgt durch Auflösen nach x: \\(x(p) = -\\tfrac12 p + 4\\). Die Darstellung in der Form p(x) hat den Vorteil, dass ohne Änderung der Abszissenbezeichnung (x-Achse) Umsatz-, Kosten- und Gewinnfunktionen in dasselbe Koordinatensystem passen.</p>'),
 vor_kc('saettigungswert',
  '<h3>Aus der Mitschrift: Grenzwerte bei Funktionen</h3>'
  '<p><b>Definition</b>: Man schreibt \\(\\lim_{x\\to a} f(x) = c\\), falls für jede Folge \\((x_n)\\) mit \\(x_n \\in D\\) und \\(\\lim x_n = a\\) gilt \\(\\lim f(x_n) = c\\). Rechtsseitig (\\(x \\downarrow a\\)) bzw. linksseitig (\\(x \\uparrow a\\)): nur Folgen mit \\(x_n > a\\) bzw. \\(x_n < a\\); '
  '\\(x \\to \\infty\\): Folgen mit \\(\\lim x_n = \\infty\\). Der Grenzwert existiert, wenn rechts- und linksseitiger Grenzwert übereinstimmen. Beispiel: Gaußklammer, \\(\\lim_{x\\downarrow1}\\lfloor x\\rfloor = 1\\), \\(\\lim_{x\\uparrow1}\\lfloor x\\rfloor = 0\\): kein Grenzwert an 1.</p>'
  '<p><b>Rechenregeln</b> (\\(\\lim f_1 = c_1,\\ \\lim f_2 = c_2\\)): Summe \\(c_1 + c_2\\), Produkt \\(c_1\\cdot c_2\\), Quotient \\(\\tfrac{c_1}{c_2}\\) (\\(c_2 \\ne 0\\)), Verkettung \\(\\lim f_1(f_2(x)) = f_1(\\lim f_2(x))\\); also z. B. \\(\\lim (f_1)^n = c_1^n\\), \\(\\lim \\sqrt[n]{f_1} = \\sqrt[n]{c_1}\\), \\(\\lim e^{f_1} = e^{c_1}\\), \\(\\lim \\ln f_1 = \\ln c_1\\).</p>'
  '<ul><li>Potenzen: \\(\\lim_{x\\to\\infty} x^n = \\infty\\); \\(\\lim_{x\\to-\\infty} x^n = +\\infty\\) (n gerade) bzw. \\(-\\infty\\) (n ungerade); \\(\\lim_{x\\to\\pm\\infty} x^{-n} = 0\\).</li>'
  '<li>Exponentialfunktion: \\(\\lim_{x\\to\\infty} a^x = 0\\) (0 < a < 1), \\(\\infty\\) (a > 1), 1 (a = 1); für a > 1 wächst sie schneller gegen ∞ als jede Potenz: \\(\\lim \\tfrac{x^n}{a^x} = 0\\).</li>'
  '<li>Logarithmus: \\(\\lim_{x\\to\\infty}\\log_a x = \\infty\\), \\(\\lim_{x\\downarrow0}\\log_a x = -\\infty\\); er wächst langsamer als jede positive Potenz: \\(\\lim \\tfrac{\\ln x}{x^n} = 0\\).</li>'
  '<li>\\(\\lim_{x\\downarrow0}\\tfrac1x = +\\infty\\), \\(\\lim_{x\\uparrow0}\\tfrac1x = -\\infty\\): \\(x_0 = 0\\) heißt <b>Polstelle</b>; die Funktion verhält sich <b>asymptotisch</b>, x- bzw. y-Achse sind die <b>Asymptoten</b> von \\(\\tfrac1x\\) für \\(x\\to\\pm\\infty\\) bzw. \\(x\\to0\\).</li></ul>'),
 vor_kc('stetigkeit',
  '<h3>Aus der Mitschrift: ε-δ-Definition und Nachweis</h3>'
  '<p><b>Definition</b>: f heißt <b>stetig im Punkt a</b>, falls \\(\\lim_{x\\to a} f(x) = f(a)\\); f heißt stetig in D, falls f in jedem Punkt von D stetig ist. '
  '<b>Satz (ε-δ-Definition)</b>: f ist genau dann in a stetig, wenn es zu jedem \\(\\varepsilon > 0\\) ein \\(\\delta > 0\\) gibt, so dass \\(|f(x) - f(a)| < \\varepsilon\\) für alle x mit \\(|x - a| < \\delta\\). '
  'Anschaulich: Zu jedem horizontalen ε-Streifen um f(a) findet man einen vertikalen δ-Streifen um a, so dass das Schaubild den ε-δ-Kasten nicht verlässt (graphisch: Funktion zeichnen, ohne den Stift abzusetzen).</p>'
  '<p><b>Nachweis</b> für \\(f(x) = bx + c\\), \\(b \\ne 0\\): Sei \\(\\varepsilon > 0\\) und \\(x_0\\) beliebig; wähle \\(\\delta < \\tfrac{\\varepsilon}{|b|}\\). Für \\(|x - x_0| < \\delta\\) gilt '
  '\\(|x - x_0| < \\tfrac{\\varepsilon}{|b|} \\Leftrightarrow |b|\\cdot|x - x_0| < \\varepsilon \\Leftrightarrow |(bx + c) - (bx_0 + c)| < \\varepsilon\\), also \\(|f(x) - f(x_0)| < \\varepsilon\\): f ist in \\(x_0\\) stetig.</p>'
  '<ul><li><b>Sätze</b>: Sind f, g in a stetig, dann auch \\(f + g\\), \\(\\lambda f\\), \\(f\\cdot g\\) und, falls \\(g(a) \\ne 0\\), \\(\\tfrac fg\\). Ist f in a und g in f(a) stetig, ist auch \\(g\\circ f\\) in a stetig.</li>'
  '<li>Stetig sind konstante Funktionen, die identische Funktion, die Betragsfunktion, alle rationalen Funktionen in ihrem Definitionsbereich und \\(\\exp\\).</li>'
  '<li>Folgerung aus dem Zwischenwertsatz: Jedes Polynom <b>ungeraden Grades</b> hat mindestens eine reelle Nullstelle; ein Polynom geraden Grades muss keine haben (\\(x^{2k} + 1\\)).</li>'
  '<li><b>Stetigkeit der Umkehrfunktion</b>: Ist f auf [a, b] stetig und streng monoton, bildet f [a, b] eineindeutig auf das Bildintervall ab, und \\(f^{-1}\\) ist ebenfalls stetig und streng monoton. Daraus: die k-te Wurzel und \\(\\ln\\) (Umkehrung von exp) sind stetig und streng monoton wachsend.</li></ul>'),
 # ---------------- 4 Differentialrechnung ----------------
 vor_kc('differentialquotient',
  '<h3>Aus der Mitschrift: Definition mit η, Beispiele</h3>'
  '<p><b>Definition</b>: f heißt im Punkt x <b>differenzierbar</b>, falls der Grenzwert \\(f\'(x) = \\lim_{\\eta\\to x,\\ \\eta\\ne x}\\frac{f(\\eta) - f(x)}{\\eta - x}\\) existiert; er heißt Differentialquotient oder Ableitung (Schreibweise auch \\(\\frac{df(x)}{dx}\\)). '
  'f heißt differenzierbar in D, falls f in jedem Punkt von D differenzierbar ist. Gleichwertig: \\(f\'(x) = \\lim_{h\\to0}\\frac{f(x + h) - f(x)}{h}\\). '
  'Geometrisch ist \\(\\frac{f(\\eta) - f(x)}{\\eta - x}\\) die Steigung der Sekante durch \\((x, f(x))\\) und \\((\\eta, f(\\eta))\\); für \\(\\eta\\to x\\) wird aus der Sekante die Tangente.</p>'
  '<ul><li>konstante Funktion: \\(\\lim \\frac{c - c}{\\eta - x} = 0\\) · lineare Funktion \\(ax + c\\): \\(\\lim \\frac{a\\eta + c - (ax + c)}{\\eta - x} = \\lim \\frac{a(\\eta - x)}{\\eta - x} = a\\)</li>'
  '<li>\\(x^2\\): \\(\\lim \\frac{\\eta^2 - x^2}{\\eta - x} = \\lim \\frac{(\\eta + x)(\\eta - x)}{\\eta - x} = \\lim(\\eta + x) = 2x\\) (3. binomische Formel) · \\(\\tfrac1x\\): \\(\\lim \\frac{\\frac1\\eta - \\frac1x}{\\eta - x} = \\lim\\frac{-1}{\\eta x} = -\\frac{1}{x^2}\\)</li>'
  '<li>\\(\\exp\'(x) = \\exp(x)\\), \\(\\sin\' = \\cos\\), \\(\\cos\' = -\\sin\\).</li>'
  '<li>Die Betragsfunktion ist an der Stelle 0 <b>nicht differenzierbar</b> (Knick): Für \\(h_n = \\tfrac{(-1)^n}{n} \\to 0\\) ist \\(\\frac{|0 + h_n| - |0|}{h_n} = (-1)^n\\) divergent.</li>'
  '<li>Eine in \\(x_0\\) stetige Funktion muss dort nicht differenzierbar sein; umgekehrt ist eine in \\(x_0\\) differenzierbare Funktion dort auch stetig. Stetigkeit ist also eine <b>notwendige, aber nicht hinreichende</b> Bedingung für Differenzierbarkeit.</li></ul>'),
 vor_kc('ableitungsregeln',
  '<h3>Aus der Mitschrift: weitere Ableitungen</h3>'
  '<ul><li>\\((a^x)\' = \\ln(a)\\cdot a^x\\) (a > 0) · \\(\\tan\'(x) = \\frac{1}{\\cos^2 x}\\) (Quotientenregel mit \\(\\tan = \\frac{\\sin}{\\cos}\\))</li>'
  '<li><b>Satz (Ableitung der Umkehrfunktion)</b>: Ist f auf [a, b] stetig und streng monoton, in x differenzierbar mit \\(f\'(x) \\ne 0\\), dann ist \\(f^{-1}\\) in \\(y = f(x)\\) differenzierbar mit \\((f^{-1})\'(y) = \\frac{1}{f\'(x)} = \\frac{1}{f\'(f^{-1}(y))}\\). '
  'Beispiel: \\((\\log_a y)\' = \\frac{1}{\\ln(a)\\cdot a^{\\log_a y}} = \\frac{1}{\\ln(a)\\cdot y}\\).</li>'
  '<li>f heißt <b>k-mal differenzierbar</b> in D, wenn f in jedem Punkt k-mal differenzierbar ist, und <b>k-mal stetig differenzierbar</b>, wenn überdies die k-te Ableitung stetig ist. '
  'Die k-te Ableitung erhält man mit \\(f^{(k)}(x) = (f^{(k-1)}(x))\'\\) (Verallgemeinerung durch vollständige Induktion).</li></ul>'
  '<p><b>Vollständige Induktion</b> am Beispiel \\(\\sum_{i=1}^{n} i = \\frac{n(n+1)}{2}\\): Induktionsanfang n = 1: \\(\\frac{1\\cdot2}{2} = 1\\) ✓. Induktionsannahme: Die Formel gilt für beliebiges n. '
  'Induktionsschluss n → n + 1: \\(\\sum_{i=1}^{n+1} i = \\frac{n(n+1)}{2} + (n+1) = \\frac{n(n+1) + 2(n+1)}{2} = \\frac{(n+1)(n+2)}{2}\\).</p>'),
 vor_kc('kurvendiskussion',
  '<h3>Aus der Mitschrift: Extrema genau</h3>'
  '<p><b>Definition</b>: f hat in x ein <b>lokales Maximum (Minimum)</b>, wenn ein \\(\\varepsilon > 0\\) existiert, so dass \\(f(x) \\ge f(y)\\) (bzw. \\(f(x) \\le f(y)\\)) für alle y mit \\(|x - y| < \\varepsilon\\). '
  '<b>Extremum</b> ist der gemeinsame Oberbegriff für Maximum und Minimum. Gilt das Gleichheitszeichen nur für x = y, spricht man von einem <b>isolierten</b> lokalen Maximum (Minimum).</p>'
  '<ul><li><b>Satz</b>: Hat f in x ein lokales Extremum und ist f dort differenzierbar, dann gilt f′(x) = 0. Das ist nur notwendig, nicht hinreichend: \\(f(x) = x^3\\) hat \\(f\'(0) = 0\\), aber kein Extremum.</li>'
  '<li>Wechselt f′ das Vorzeichen von + nach − (Maximum) bzw. − nach + (Minimum), ist das hinreichend.</li>'
  '<li><b>Globale Extrema</b>: größtes lokales Maximum mit den Randwerten des Intervalls vergleichen. Liegt der Extremwert am Rand, ist dort nicht notwendig f′(x) = 0 (z. B. \\(f(x) = x\\) auf [0, 1]).</li>'
  '<li><b>Satz von Rolle</b>: Ist f auf [a, b] stetig, in (a, b) differenzierbar und f(a) = f(b), dann gibt es ein \\(\\xi \\in (a, b)\\) mit \\(f\'(\\xi) = 0\\): Zwischen zwei Nullstellen von f liegt eine Nullstelle der Ableitung.</li>'
  '<li><b>Monotonie</b>: Gilt \\(f\'(x) \\ge 0\\) (> 0, ≤ 0, < 0) in (a, b), ist f in [a, b] monoton wachsend (streng monoton wachsend, monoton fallend, streng monoton fallend).</li>'
  '<li>f′(x) = 0 und f″(x) > 0 ist hinreichend, aber nicht notwendig für ein isoliertes lokales Minimum: \\(x^4\\) hat in 0 ein isoliertes Minimum mit f″(0) = 0 (f′ wechselt das Vorzeichen).</li>'
  '<li><b>Wendepunkt</b>: η heißt Wendepunkt, wenn f″ beim Durchgang durch η das Vorzeichen wechselt. Nach dem Zwischenwertsatz ist dann f″(η) = 0 (nur notwendig); im Wendepunkt geht positive in negative Krümmung über oder umgekehrt.</li></ul>'),
 # ---------------- 5 Ökonomische Funktionen ----------------
 vor_kc('gewinnmaximum',
  '<h3>Aus der Mitschrift: Preis gleich Grenzkosten</h3>'
  '<p>Bei festem Preis p ist \\(G(x) = U(x) - K(x) = p\\cdot x - K(x)\\), also \\(G\'(x) = p - K\'(x)\\). Gewinn maximal ⇒ \\(G\'(x) = 0 \\Rightarrow p = K\'(x)\\): Die <b>Übereinstimmung des Preises mit den Grenzkosten</b> ist notwendig für einen maximalen Gewinn. '
  'Verlustfrei arbeitet eine Produktion, wenn \\(G(x) \\ge 0\\), d. h. wenn der Preis mindestens die Stückkosten \\(k(x) = \\frac{K(x)}{x}\\) deckt.</p>'),
 # ---------------- 6 Integral ----------------
 vor_kc('stammfunktion',
  '<h3>Aus der Mitschrift: Sätze zum unbestimmten Integral</h3>'
  '<p>Bisher wurde das Integral anschaulich als Flächeninhalt definiert; nun wird gezeigt, dass die Integration die Umkehrung der Differentiation ist. '
  '<b>Satz und Definition</b>: Ist f auf dem Intervall I stetig und \\(a \\in I\\), dann ist \\(F(x) = \\int_a^x f(t)\\,dt\\) differenzierbar mit \\(F\' = f\\). '
  '<b>Satz</b>: Ist F eine Stammfunktion von f, ist G genau dann ebenfalls Stammfunktion, wenn F − G eine Konstante ist. '
  '<b>Linearität</b>: \\(\\int_a^b (\\alpha f + \\beta g)\\,dx = \\alpha\\int_a^b f\\,dx + \\beta\\int_a^b g\\,dx\\).</p>'
  '<p>Aus jeder Ableitungsformel folgt eine Integrationsformel: \\(\\int_a^b x^n dx = [\\frac{x^{n+1}}{n+1}]_a^b\\) · \\(\\int_a^b \\frac1x dx = [\\ln|x|]_a^b\\) (für a, b > 0 bzw. a, b < 0; x = 0 darf nicht im Intervall liegen) · \\(\\int\\sin x\\,dx = -\\cos x\\) · \\(\\int\\cos x\\,dx = \\sin x\\) · \\(\\int\\exp(x)dx = \\exp(x)\\).</p>'),
 vor_kc('substitution',
  '<h3>Aus der Mitschrift: Substitutionsregel genau</h3>'
  '<p><b>Satz</b>: Ist f auf I stetig und φ: [a, b] → ℝ stetig differenzierbar mit φ([a, b]) ⊂ I, dann gilt \\(\\int_a^b f(\\varphi(t))\\,\\varphi\'(t)\\,dt = \\int_{\\varphi(a)}^{\\varphi(b)} f(x)\\,dx\\). '
  'Wird \\(x = \\varphi(t)\\) substituiert, muss auch das Differential transformiert werden: \\(dx = \\varphi\'(t)\\,dt\\), und die Grenzen werden zu \\(\\varphi(a)\\), \\(\\varphi(b)\\).</p>'
  '<ul><li>\\(\\int_a^b f(t + c)\\,dt = \\int_{a+c}^{b+c} f(x)\\,dx\\) · \\(\\int_a^b f(ct)\\,dt = \\frac1c\\int_{ac}^{bc} f(x)\\,dx\\) (c ≠ 0)</li>'
  '<li>\\(\\int_a^b \\frac{\\varphi\'(t)}{\\varphi(t)}\\,dt = [\\ln|\\varphi(t)|]_a^b\\) (φ(t) ≠ 0), daraus \\(\\int\\tan t\\,dt = \\int\\frac{\\sin t}{\\cos t}dt = [-\\ln(\\cos t)]\\) für \\([a, b] \\subset (-\\frac\\pi2, \\frac\\pi2)\\).</li></ul>'),
 vor_kc('partielle-integration',
  '<h3>Aus der Mitschrift: Beispiel und Bemerkungen</h3>'
  '<p>\\(\\int_a^b \\ln x\\,dx\\) (a, b > 0): setze \\(f = \\ln x\\), \\(g\' = 1\\), \\(g = x\\): \\([\\ln(x)\\cdot x]_a^b - \\int_a^b \\frac1x\\cdot x\\,dx = [x(\\ln x - 1)]_a^b\\).</p>'
  '<ul><li>Die Zerlegung des Integranden h in ein Produkt \\(f\\cdot g\'\\) ist nicht eindeutig.</li>'
  '<li>Partielle Integration führt nur zum Ziel, wenn man zu g′ und zu \\(f\'\\cdot g\\) eine Stammfunktion angeben kann.</li>'
  '<li>Häufig wählt man für g′ einen Term, der sich bei der Integration nicht oder nur wenig verändert (exp, trigonometrische Funktionen).</li></ul>'),
 # ---------------- 7 Lineare Algebra ----------------
 vor_kc('vektoren',
  '<h3>Aus der Mitschrift: ℝⁿ und kanonische Basis</h3>'
  '<p>Für jede natürliche Zahl n bildet \\(\\mathbb{R}^n\\) die Menge der <b>geordneten n-Tupel</b> \\((x_1, \\ldots, x_n)\\); zwei n-Tupel heißen gleich, wenn \\(x_1 = y_1, \\ldots, x_n = y_n\\). '
  'Für n = 1 erhält man eine Gerade, für n = 2 die Menge der geordneten Paare (eine Ebene: jeder Punkt entspricht einem Paar (x, y)). Die n-Tupel heißen <b>Vektoren</b>, reelle Zahlen heißen <b>Skalare</b>.</p>'
  '<p>Die Vektoren \\(e_i = (0, \\ldots, 0, 1, 0, \\ldots, 0)\\) (1 an der i-ten Stelle) sind linear unabhängig, denn aus \\(\\lambda_1 e_1 + \\ldots + \\lambda_n e_n = (\\lambda_1, \\ldots, \\lambda_n) = 0\\) folgt \\(\\lambda_1 = \\ldots = \\lambda_n = 0\\). Sie heißen <b>kanonische Basis</b> des \\(\\mathbb{R}^n\\).</p>'),
 vor_kc('matrizen',
  '<h3>Aus der Mitschrift: Begriffe</h3>'
  '<p>Ein rechteckiges Schema \\(A = (a_{ij})\\), \\(1 \\le i \\le m,\\ 1 \\le j \\le n\\), von Elementen \\(a_{ij} \\in \\mathbb{R}\\) heißt <b>Matrix</b>; die \\(a_{ij}\\) sind die <b>Komponenten</b>. Eine Matrix mit m Zeilen und n Spalten heißt <b>m×n-Matrix</b>; i heißt Zeilenindex, j Spaltenindex. '
  '\\(M(m\\times n; \\mathbb{R})\\) ist die Menge aller m×n-Matrizen. Die <b>Nullmatrix</b> hat nur Nullen; die zu A <b>negative Matrix</b> ist \\(-A = (-a_{ij})\\).</p>'),
 vor_kc('matrizenmultiplikation',
  '<h3>Aus der Mitschrift: Eigenschaften des Produkts</h3>'
  '<ul><li>Für m = n kann man A·B und B·A bilden; im Allgemeinen gilt aber \\(A\\cdot B \\ne B\\cdot A\\).</li>'
  '<li>Das Produkt zweier Matrizen kann die Nullmatrix ergeben, obwohl beide Matrizen von der Nullmatrix verschieden sind (in ℝ gilt dagegen \\(x\\cdot y = 0 \\Leftrightarrow x = 0\\) oder \\(y = 0\\)).</li>'
  '<li>Die <b>n-reihige Einheitsmatrix</b> \\(E_n\\) hat \\(e_{ij} = 1\\) für i = j und 0 sonst; \\(A\\cdot E_n = E_n\\cdot A = A\\).</li>'
  '<li><b>Rechenregeln</b>: Distributivgesetze \\(A(B + \\tilde B) = AB + A\\tilde B\\), \\((A + \\tilde A)B = AB + \\tilde AB\\) · \\(A(\\lambda B) = (\\lambda A)B = \\lambda(AB)\\) · Assoziativgesetz \\((AB)C = A(BC)\\) · \\((AB)^T = B^T A^T\\).</li></ul>'),
 vor_kc('mehrstufige-produktion',
  '<h3>Aus der Mitschrift: Produktionsverflechtung und Gozinto-Graph</h3>'
  '<p>Bei komplexen Produktionsprozessen (Fahrzeugbau, chemische Industrie) werden Zwischenprodukte einerseits direkt auf den Markt gebracht, andererseits als weiter zu verarbeitendes Produkt im Produktionsprozess eingesetzt. '
  'Eine solche <b>Verflechtung</b> über mehrere Produktionsstufen mit festen Mengenbeziehungen zwischen Rohstoffen, Zwischenprodukten und Halbfertigbauteilen stellt man im <b>Gozinto-Graphen</b> dar (Zepartzat Gozinto, „the part that goes into“, A. Vazsonyi).</p>'
  '<p>i, j sind Produktionsknoten mit zu produzierenden Mengen \\(x_i\\), \\(x_j\\); \\(a_i\\) ist die Menge des Produkts i, die ausgeliefert wird; der Koeffizient \\(k_{ij}\\) gibt an, wie viele Einheiten von i für eine Einheit von j benötigt werden. '
  'Aus dem Graphen liest man nur den direkten Bedarf ab; interessant ist, wie viel insgesamt bereitstehen muss: \\(x_i = a_i + \\sum_j k_{ij}\\cdot x_j\\). '
  'Beispiel (5 Knoten, Programm \\(a_4 = 6\\), \\(a_5 = 5\\)): \\(x_1 = 2x_3 + x_5\\), \\(x_2 = 3x_3 + 3x_4 + 7x_5\\), \\(x_3 = x_4 + 2x_5\\), \\(x_4 = 3x_5 + 6\\), \\(x_5 = 5\\); als LGS mit oberer Dreiecksmatrix, durch sukzessives Einsetzen '
  '\\(x_5 = 5,\\ x_4 = 21,\\ x_3 = 31,\\ x_2 = 181,\\ x_1 = 67\\).</p>'),
 vor_kc('lgs-gauss',
  '<h3>Aus der Mitschrift: LGS, Zeilenstufenform, Lösungsverhalten</h3>'
  '<p>Ein <b>LGS</b> ist eine Anzahl linearer Gleichungen \\(a_{11}x_1 + \\ldots + a_{1n}x_n = b_1, \\ldots, a_{m1}x_1 + \\ldots + a_{mn}x_n = b_m\\); alle Variablen treten nur linear (ohne Potenzen) und ohne Produkte von Variablen auf. '
  'In Matrizennotation \\(A\\cdot x = b\\). <b>Satz</b>: Die Lösungsmenge ändert sich nicht, wenn man das LGS durch elementare Zeilenumformungen vom Typ I–IV umformt: '
  'I Multiplikation der i-ten Zeile mit λ ≠ 0 · II Addition der j-ten Zeile zur i-ten · III Addition des λ-fachen der j-ten Zeile zur i-ten · IV Vertauschen zweier Zeilen (III und IV erhält man durch wiederholte Anwendung von I und II).</p>'
  '<p><b>Zeilenstufenform</b> (Stufen- oder Treppenform): Unter der „Stufenlinie“ stehen nur Nullen. Sie ist nicht eindeutig, die Anzahl der Nullzeilen ist aber in jeder Zeilenstufenform gleich. '
  '<b>Lemma</b>: Jede m×n-Matrix kann durch endlich viele elementare Zeilenumformungen in Zeilenstufenform gebracht werden; dieses Verfahren heißt <b>Gaußsches Eliminationsverfahren</b>.</p>'
  '<p>Lösungsverhalten aus dem Schema (k Stufen): eindeutig lösbar, wenn k = m = n (obere Dreiecksmatrix) · unlösbar, wenn einer der Werte \\(b\'_{k+1}, \\ldots, b\'_m\\) von Null verschieden ist · mehrdeutig lösbar, wenn alle diese Werte 0 sind; dann gibt es n − k freie Parameter. '
  'Ein LGS kann nicht genau 2, 3, … verschiedene Lösungen haben: Aus zwei Lösungen folgen beliebig viele.</p>'),
 vor_kc('determinante',
  '<h3>Aus der Mitschrift: Entwicklung nach einer Spalte (auch 4×4) und Regeln</h3>'
  '<p>Allgemein: \\(A_{ij}\\) sei die (n−1)×(n−1)-Matrix, die aus A durch Weglassen der i-ten Zeile und j-ten Spalte entsteht. Dann gilt (<b>Entwicklung nach der j-ten Spalte</b>) '
  '\\(\\det A = \\sum_{i=1}^{n}(-1)^{i+j}\\,a_{ij}\\,\\det A_{ij}\\). Beispiel 4×4, Entwicklung nach der 1. Spalte von \\(\\begin{pmatrix}1&0&3&2\\\\4&2&0&5\\\\3&6&1&2\\\\4&1&2&7\\end{pmatrix}\\): '
  '\\((-1)^2\\cdot1\\cdot\\det\\begin{pmatrix}2&0&5\\\\6&1&2\\\\1&2&7\\end{pmatrix} + (-1)^3\\cdot4\\cdot\\det\\begin{pmatrix}0&3&2\\\\6&1&2\\\\1&2&7\\end{pmatrix} + (-1)^4\\cdot3\\cdot\\det\\begin{pmatrix}0&3&2\\\\2&0&5\\\\1&2&7\\end{pmatrix} + (-1)^5\\cdot4\\cdot\\det\\begin{pmatrix}0&3&2\\\\2&0&5\\\\6&1&2\\end{pmatrix}\\); '
  'die 3×3-Determinanten rechnet man mit Sarrus.</p>'
  '<ul><li>\\(\\det(\\lambda A) = \\lambda^n\\det A\\) · Hat A eine Nullzeile, ist det A = 0; det A = 0 bedeutet, dass die Zeilenvektoren linear abhängig sind.</li>'
  '<li>Obere Dreiecksmatrix: \\(\\det A = \\lambda_1\\cdot\\lambda_2\\cdots\\lambda_n\\) (Produkt der Diagonalelemente) · \\(\\det(A\\cdot B) = \\det A\\cdot\\det B\\) · \\(\\det A = \\det A^T\\).</li>'
  '<li>Die Inverse existiert genau dann, wenn det A ≠ 0; \\(A\\cdot x = b\\) ist genau dann eindeutig lösbar, wenn det A ≠ 0.</li></ul>'),
 vor_kc('inverse-matrix',
  '<h3>Aus der Mitschrift: invertierbar, Gauß-Jordan, Determinantenmethode</h3>'
  '<p><b>Definition</b>: \\(A \\in M(n\\times n; \\mathbb{R})\\) heißt <b>invertierbar</b> (oder <b>regulär</b>), falls es \\(\\tilde A\\) gibt mit \\(A\\tilde A = \\tilde AA = E_n\\); Bezeichnung \\(\\tilde A = A^{-1}\\). Nicht invertierbare Matrizen heißen <b>singulär</b>. '
  'Aus \\(Ax = b\\) folgt durch Multiplikation von links mit \\(A^{-1}\\): \\(x = A^{-1}b\\). Das setzt m = n voraus (Anzahl der Gleichungen gleich Anzahl der Unbekannten).</p>'
  '<p>Elementare Zeilenumformungen an A wirken genauso im Produkt A·B. Überführt man A durch Zeilenumformungen in \\(E_n\\), verwandeln dieselben Umformungen \\(E_n\\) in \\(A^{-1}\\) (Schema \\((A\\,|\\,E_n) \\to (E_n\\,|\\,A^{-1})\\)).</p>'
  '<p>Andere Berechnung: \\(c_{ij} = (-1)^{i+j}\\det A_{ij}\\); dann \\(A^{-1} = \\frac{1}{\\det A}\\,C^T\\) (Determinantenmethode). Für 2×2: \\(\\begin{pmatrix}a&b\\\\c&d\\end{pmatrix}^{-1} = \\frac{1}{ad - bc}\\begin{pmatrix}d&-b\\\\-c&a\\end{pmatrix}\\). '
  'Äquivalent sind: \\(A^{-1}\\) existiert · det A ≠ 0 · die Zeilenvektoren von A sind linear unabhängig · Ax = b ist eindeutig lösbar.</p>'),
 # ---------------- 8 Analysis II ----------------
 vor_kc('partielle-ableitung',
  '<h3>Aus der Mitschrift: Definition der partiellen Ableitung</h3>'
  '<p>Funktionen \\(f: U \\to \\mathbb{R}\\), \\(U \\subset \\mathbb{R}^n\\); der Graph ist die Menge \\(\\{(x, y) \\in U\\times\\mathbb{R}: y = f(x)\\} \\subset \\mathbb{R}^{n+1}\\), für n = 2 eine <b>Fläche im dreidimensionalen Raum</b> (z. B. Paraboloid \\(f(x, y) = 1 - x^2 - y^2\\), unten offen). '
  'In einem Punkt der Fläche gibt es je nach Richtung beliebig viele Steigungen; man fragt zuerst nach der Steigung in x-Richtung (y konstant) und in y-Richtung (x konstant): die <b>partiellen Ableitungen</b>.</p>'
  '<p><b>Definition</b>: f heißt im Punkt x <b>partiell differenzierbar</b> bzgl. der i-ten Koordinatenrichtung, falls \\(\\frac{\\partial f(x)}{\\partial x_i} = \\lim_{h\\to0}\\frac{f(x + h\\,e_i) - f(x)}{h}\\) existiert (\\(e_i\\) = i-ter Einheitsvektor). '
  'Die partielle Ableitung ist nichts anderes als die gewöhnliche Ableitung nach \\(x_i\\) bei Festhaltung der übrigen n − 1 Variablen; es gelten dieselben Rechenregeln. Schreibweise auch \\(\\frac{\\partial f}{\\partial x_i}\\) oder \\(f\'_{x_i}\\). '
  'Sind alle partiellen Ableitungen selbst partiell differenzierbar, heißt f <b>zweimal partiell differenzierbar</b>; die Hesse-Matrix ist quadratisch und, da \\(\\frac{\\partial^2 f}{\\partial x_i\\partial x_j} = \\frac{\\partial^2 f}{\\partial x_j\\partial x_i}\\), symmetrisch (wichtig für die Berechnung von Extremwerten).</p>'),
 vor_kc('grenzprodukt',
  '<h3>Aus der Mitschrift: ökonomische Interpretation</h3>'
  '<p><b>Satz</b>: Der Wert \\(\\frac{\\partial f(P_0)}{\\partial x_i}\\) gibt (näherungsweise) an, um wie viele Einheiten sich \\(f(P_0)\\) ändert, wenn sich \\(x_i\\) um eine Einheit ändert und alle anderen unabhängigen Variablen unverändert bleiben (<b>ceteris-paribus-Bedingung</b>, c. p.). '
  'Partielle Ableitungen sind das Hilfsmittel der <b>Partialanalyse</b> ökonomischer Funktionen: Man variiert eine einzige Variable und hält alle übrigen Einflussfaktoren konstant. '
  'Alle ökonomischen Begriffe wie Grenzkosten oder Grenzgewinn lassen sich mit dem Zusatz „partiell“ auf Funktionen mit mehreren Variablen übertragen.</p>'
  '<p>Beispiel \\(y(A, K) = 2A^{0{,}4}K^{0{,}6}\\) (A Arbeit, K Kapital): \\(\\frac{\\partial y}{\\partial A} = 0{,}8\\,A^{-0{,}6}K^{0{,}6}\\) ist die (partielle) <b>Grenzproduktivität der Arbeit</b>, \\(\\frac{\\partial y}{\\partial K} = 1{,}2\\,A^{0{,}4}K^{-0{,}4}\\) die <b>Grenzproduktivität des Kapitals</b>.</p>'),
 vor_kc('totales-differential',
  '<h3>Aus der Mitschrift: partielles und vollständiges Differential</h3>'
  '<p>Unter dem <b>Differential</b> df einer Funktion f: ℝ → ℝ versteht man die Änderung der Tangentenfunktion (näherungsweise die Änderung Δf), wenn sich x um dx = Δx ändert: \\(df = f\'(x)\\,dx\\). '
  '<b>Definition</b>: Das i-te <b>partielle Differential</b> ist \\(df_{x_i} = \\frac{\\partial f}{\\partial x_i}\\,dx_i\\); es hängt von der Stelle und von der Änderung \\(dx_i\\) ab und gibt (näherungsweise) die Änderung von f an, wenn nur \\(x_i\\) um \\(dx_i\\) geändert wird (für \\(dx_i = 1\\) gleich der partiellen Ableitung). '
  'Das <b>vollständige (totale) Differential</b> ist die Summe aller partiellen Differentiale; es gibt an, wie sich f ändert, wenn sich gleichzeitig jede Variable ändert.</p>'
  '<p>Beispiel \\(y(A, K) = 2A^{0{,}2}K^{0{,}8}\\) bei A = 20, K = 10: \\(dy \\approx 0{,}2297\\,dA + 1{,}8379\\,dK\\) (dy heißt auch <b>totales Grenzprodukt</b>). Arbeit −0,3, Kapital +0,1: \\(dy \\approx 0{,}2297\\cdot(-0{,}3) + 1{,}8379\\cdot0{,}1 = 0{,}115\\) Einheiten; '
  'exakt \\(\\Delta y = y(19{,}7;\\ 10{,}1) - y(20, 10) = 0{,}114\\): Das vollständige Differential liefert gute Näherungswerte.</p>'),
]
