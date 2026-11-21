import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *
import sympy as sp

x = sp.symbols('x', positive=True)
# Übung ökonomische Funktionen, Aufgabe 1
K1 = x**3 - 15 * x**2 + 125 * x + 375; U1 = 150 * x; G1 = sp.expand(U1 - K1)
assert sorted(sp.solve(G1, x)) == [5, 15]
xg = [r for r in sp.solve(sp.diff(G1, x), x)][0]; assert abs(float(xg) - 10.773) < 1e-3 and abs(float(G1.subs(x, xg)) - 384.900) < 1e-2
xbo = float(sp.nsolve(sp.diff(K1 / x, x), x, 12)); kbo = float((K1 / x).subs(x, xbo)); assert abs(xbo - 9.554) < 1e-3 and abs(kbo - 112.219) < 1e-2
assert sp.solve(sp.diff((K1 - 375) / x, x), x) == [sp.Rational(15, 2)] and ((K1 - 375) / x).subs(x, sp.Rational(15, 2)) == sp.Rational(275, 4)
# Übungsblatt 6, Aufgabe 3
K6 = (x - 10)**3 / 50 + 20; G6 = 2 * x - K6
assert sorted(sp.solve(G6, x)) == [10, 20]
assert abs(float(sp.nsolve(sp.diff(G6, x), x, 15)) - 15.7735) < 1e-3 and abs(float(G6.subs(x, 10 + 10 / sp.sqrt(3))) - 7.698) < 1e-3
assert abs(float(sp.nsolve(sp.diff(K6 / x, x), x, 14)) - 15) < 1e-6 and (K6 / x).subs(x, 15) == sp.Rational(3, 2)
# Übung ökonomische Funktionen, Aufgabe 2 und 4
assert sp.integrate(sp.Rational(3, 2) * x**2 - 4 * x + 4, x) + 32 - (sp.Rational(1, 2) * x**3 - 2 * x**2 + 4 * x + 32) == 0
assert (sp.Rational(1, 2) * x**3 - 2 * x**2 + 4 * x + 32).subs(x, 10) == 372
K4 = x**3 - 6 * x**2 + 12 * x + 12; assert K4.subs(x, 0) == 12 and K4.subs(x, 2) == 20 and sp.diff(K4, x).subs(x, 2) == 0 and sp.diff(K4, x, 2).subs(x, 2) == 0
G4 = 7 * x - K4; assert sorted(sp.solve(G4, x)) == [3, 4]
# Markt
assert abs(float(sp.nsolve(100 / (20 - x) - (35 - x**2 / 15), x, 10)) - 15) < 1e-6

KF = lambda v: v**3 - 15 * v * v + 125 * v + 375


def kosten_bild():
    s, X, Y = graph([(KF, 0, 17, 'var(--c3)', 'K(x)', 'K(x) = x³ − 15x² + 125x + 375: erst steigen die Kosten langsamer (Wendepunkt bei x = 5), dann immer schneller.', 16),
                     (lambda v: 375, 0, 17, 'var(--axis)', 'Fixkosten 375', 'Fixkosten K_f = K(0) = 375: fallen auch ohne Produktion an.', 12),
                     (lambda v: 150 * v, 0, 17, 'var(--c2)', 'U(x)', 'U(x) = 150x: Umsatz bei festem Preis 150.', 15.5)],
                    (0, 17.5), (0, 2700), xl='x', yl='GE', ticks_x=(5, 10, 15), ticks_y=(375, 1000, 2000))
    s = tpg(flaeche([(X(5), Y(KF(5)))] + [(X(5 + i * 0.25), Y(150 * (5 + i * 0.25))) for i in range(41)] + [(X(15 - i * 0.25), Y(KF(15 - i * 0.25))) for i in range(41)], 'var(--pos)', .18),
            'Gewinnzone zwischen Gewinnschwelle x = 5 und Gewinngrenze x = 15: U(x) > K(x).') + s
    return svg(360, 250, s, 'Kosten, Umsatz, Gewinnzone', maxw=420)


# ---------------------------------------------------------------- 1 Kostenfunktion
t_kost = thema('kostenfunktion', 'Kostenfunktion: fixe, variable, Stück- und Grenzkosten', star=True,
    kern='Die Gesamtkostenfunktion K(x) = K_v(x) + K_f setzt sich aus variablen Kosten K_v(x) (hängen von der Menge ab) und Fixkosten K_f = K(0) zusammen. Stückkosten k(x) = K(x)/x, variable Stückkosten k_v(x) = K_v(x)/x, Grenzkosten K′(x). Typisch ist eine ertragsgesetzliche Kostenfunktion 3. Grades K(x) = ax³ + bx² + cx + d.',
    kurz=p('Ein Zahnpastahersteller hat die Kostenfunktion \\(K(x) = x^3 - 15x^2 + 125x + 375\\). Was kostet es, wenn er gar nichts produziert? \\(K(0) = 375\\): das sind die <b>Fixkosten</b>. Der Rest, \\(x^3 - 15x^2 + 125x\\), sind die <b>variablen Kosten</b>.')
        + p('Aus K(x) leitet man alles Weitere ab: <b>Stückkosten</b> (Kosten je Stück) durch Teilen durch x, <b>Grenzkosten</b> (Kosten der nächsten Einheit) durch Ableiten.'),
    fig=fw('Kosten, Fixkosten und Umsatz. Tippe auf Kurven und Fläche.') + bild(kosten_bild()),
    figcap='nach Übung „ökonomische Funktionen“, Aufgabe 1',
    article=h3('Die Bausteine')
        + tabelle(['Größe', 'Formel', 'beim Zahnpasta-Beispiel'], [
            ['Fixkosten', r'\(K_f = K(0)\)', '375'], ['variable Kosten', r'\(K_v(x) = K(x) - K_f\)', r'\(x^3 - 15x^2 + 125x\)'],
            ['Stückkosten', r'\(k(x) = \frac{K(x)}{x}\)', r'\(x^2 - 15x + 125 + \frac{375}{x}\)'], ['variable Stückkosten', r'\(k_v(x) = \frac{K_v(x)}{x}\)', r'\(x^2 - 15x + 125\)'],
            ['Grenzkosten', r"\(K'(x)\)", r'\(3x^2 - 30x + 125\)']])
        + klausur_hinweis('Sehr häufig gefragt: „Wie hoch sind die Fixkosten?“ (= d), „Geben Sie die variablen Kosten an“, „Funktionen der Grenzkosten und Stückkosten“. Grenzkosten sind K′(x), nicht U = K.')
        + weiter('Manchmal ist nicht K gegeben, sondern die Grenzkosten. Dann muss man zurückrechnen.')
        + h3('Von den Grenzkosten zu den Gesamtkosten')
        + bsp('Übung ökonomische Funktionen, Aufgabe 2', r"\(K'(x) = 1{,}5x^2 - 4x + 4\); bei 10 ME betragen die Gesamtkosten 372 GE.",
              [(r'Integrieren: \(K(x) = 0{,}5x^3 - 2x^2 + 4x + C\)', ''), (r'\(K(10) = 500 - 200 + 40 + C = 372\)', r'\(C = 32\) (Fixkosten)'),
               (r'Stückkosten', r'\(k(x) = 0{,}5x^2 - 2x + 4 + \frac{32}{x}\)')], 'Die Integrationskonstante sind genau die Fixkosten.')
        + bsp('Übung ökonomische Funktionen, Aufgabe 4', 'Ganzrationale Kostenfunktion 3. Grades: Fixkosten 12, K(2) = 20, an der Stelle 2 sind die Grenzkosten null und minimal.',
              [(r"Ansatz \(K(x) = ax^3 + bx^2 + cx + 12\); \(K''(2) = 0\): \(12a + 2b = 0\)", r'\(b = -6a\)'), (r"\(K'(2) = 0\): \(12a + 4b + c = 0\)", r'\(c = 12a\)'),
               (r'\(K(2) = 8a + 4b + 2c + 12 = 8a + 12 = 20\)', r'\(a = 1\)'), ('Ergebnis', r'\(K(x) = x^3 - 6x^2 + 12x + 12\)')])
        + wahr('w-kost', [('Fixkosten sind K(0).', True, 'Kosten ohne Produktion.'), ("Grenzkosten erhält man durch K(x)/x.", False, "Das sind Stückkosten; Grenzkosten sind K′(x)."),
                          ("Die Fixkosten beeinflussen die Grenzkosten nicht.", True, 'Konstante fällt beim Ableiten weg.')]),
    merk="K(x) = K_v(x) + K_f; K_f = K(0) (bei ax³+bx²+cx+d: d). Stückkosten k = K/x, variable Stückkosten k_v = K_v/x, Grenzkosten K′(x). Aus K′ zurück: integrieren, Konstante = Fixkosten.",
    exam='Fixkosten, variable Kosten, Stück- und Grenzkostenfunktion angeben (jede Klausur).',
    fehler=['Grenz- und Stückkosten verwechseln.', 'Fixkosten mit variablen Kosten mischen.'],
    src='Übung ökonomische Funktionen A1, A2, A4')

# ---------------------------------------------------------------- 2 Umsatz, Gewinn, Gewinnzone
t_gz = thema('gewinnzone', 'Umsatz, Gewinn und Gewinnzone', star=True,
    kern='Umsatz U(x) = p·x (bei festem Preis), Gewinn G(x) = U(x) − K(x). Die Gewinnzone liegt zwischen Gewinnschwelle (kleinste Menge mit G = 0, ab der Gewinn entsteht) und Gewinngrenze (größte Menge mit G = 0). Bei kubischen Kostenfunktionen hilft Raten einer Nullstelle und Polynomdivision.',
    kurz=p('Verkauft der Zahnpastahersteller zu 150 € je Mengeneinheit, ist \\(U(x) = 150x\\). Gewinn macht er, wenn der Umsatz über den Kosten liegt. Bei kleinen Mengen erdrücken ihn die Fixkosten, bei großen die steigenden variablen Kosten.')
        + p('Dazwischen liegt die <b>Gewinnzone</b>: von der <b>Gewinnschwelle</b> x = 5 bis zur <b>Gewinngrenze</b> x = 15.'),
    fig=fw('Die Gewinnzone zwischen den Schnittpunkten. Tippe auf die Fläche.') + bild(kosten_bild()),
    figcap='nach Übung „ökonomische Funktionen“, Aufgabe 1',
    article=h3('Gewinnfunktion aufstellen')
        + fx('Gewinn', r'G(x) = U(x) - K(x) = p \cdot x - K(x)', 'Umsatz minus Gesamtkosten.', r'\(G(x) = 150x - (x^3 - 15x^2 + 125x + 375) = -x^3 + 15x^2 + 25x - 375\)')
        + h3('Gewinnzone berechnen')
        + bsp('Übung ökonomische Funktionen, Aufgabe 1 ii', r'\(G(x) = -x^3 + 15x^2 + 25x - 375 = 0\)',
              [(r'Nullstelle raten: \(G(5) = -125 + 375 + 125 - 375 = 0\)', r'\(x_1 = 5\)'), (r'Polynomdivision: \(G(x) = (x - 5)(-x^2 + 10x + 75)\)', ''),
               (r'\(-x^2 + 10x + 75 = 0 \Rightarrow x = 5 \pm 10\)', r'\(x_2 = 15\) (−5 entfällt)'), ('Gewinnzone', r'\([5;\ 15]\): Gewinnschwelle 5, Gewinngrenze 15')],
              'Raten: Teiler des Absolutglieds probieren (hier 375: 1, 3, 5, …).')
        + bsp('Übungsblatt 6, Aufgabe 3 a', r'\(K(x) = \frac{1}{50}(x - 10)^3 + 20\), \(U(x) = 2x\)',
              [(r'\(G(10) = 20 - 20 = 0\), \(G(20) = 40 - 20 - 20 = 0\)', 'Gewinnschwelle 10, Gewinngrenze 20'), (r"Grenzkosten \(K'(x) = \frac{3}{50}(x - 10)^2\)", '')])
        + bsp('Übung ökonomische Funktionen, Aufgabe 4 ii', r'\(K(x) = x^3 - 6x^2 + 12x + 12\), \(U(x) = 7x\)',
              [(r'\(G(x) = -x^3 + 6x^2 - 5x - 12\); \(G(3) = 0\), \(G(4) = 0\)', 'Gewinnzone [3; 4]')])
        + wahr('w-gz', [('Die Gewinnschwelle ist die kleinste Menge mit G = 0, ab der Gewinn entsteht.', True, 'Definition laut Übungsblatt.'),
                        ('Außerhalb der Gewinnzone macht die Firma Gewinn.', False, 'Dort macht sie Verlust.'), ('Bei festem Preis p ist U(x) = p·x.', True, 'Lineare Umsatzfunktion.')]),
    merk='U(x) = p·x, G(x) = U(x) − K(x). Gewinnzone zwischen Gewinnschwelle (kleinste Nullstelle von G) und Gewinngrenze (größte). Kubisch: Nullstelle raten (Teiler des Absolutglieds), Polynomdivision, Mitternachtsformel.',
    exam='Gewinnschwelle/-zone berechnen; wird häufig gefragt.',
    fehler=['Negative Nullstellen mitnehmen.', 'Vorzeichen beim Aufstellen von G (Klammer um K!).'],
    src='Übung ökonomische Funktionen A1, A4; Übungsblatt 6 A3')

# ---------------------------------------------------------------- 3 Gewinnmaximum
def gmax_bild():
    Gf = lambda v: -v**3 + 15 * v * v + 25 * v - 375
    s, X, Y = graph([(Gf, 0, 16.5, 'var(--primary)', 'G(x)', 'G(x) = −x³ + 15x² + 25x − 375', 14)], (0, 17), (-420, 450), xl='x', yl='G', ticks_x=(5, 15), ticks_y=(-375, 385))
    s += tpg(punkt(X(10.773), Y(384.9), 'var(--c2)', 6), 'Gewinnmaximum: G′(x) = 0 bei x ≈ 10,77; G ≈ 384,90.')
    s += strich(X(10.773), Y(0), X(10.773), Y(384.9)) + T(X(10.773), Y(0) + 16, '10,77', 12, 700, fill='var(--c2)')
    return svg(360, 250, s, 'Gewinnmaximum', maxw=420)

t_gmax = thema('gewinnmaximum', 'Gewinnmaximum', star=True,
    kern="Das Gewinnmaximum liegt bei G′(x) = 0 mit G″(x) < 0; gleichwertig: Grenzumsatz = Grenzkosten, U′(x) = K′(x). Bei festem Preis p heißt das K′(x) = p. Den maximalen Gewinn erhält man durch Einsetzen in G(x).",
    kurz=p('Innerhalb der Gewinnzone gibt es eine Menge mit dem höchsten Gewinn. Dort ist die Gewinnkurve waagerecht: \\(G\'(x) = 0\\).')
        + p('Ökonomisch heißt das: Die letzte Einheit bringt genau so viel Umsatz, wie sie kostet. <b>Grenzumsatz = Grenzkosten</b>.'),
    fig=fw('Die Gewinnkurve und ihr Hochpunkt. Tippe auf den Punkt.') + bild(gmax_bild()),
    figcap='nach Übung „ökonomische Funktionen“, Aufgabe 1 iv',
    article=h3('Vorgehen')
        + fluss([('G aufstellen', 'U − K'), ("G′ = 0", 'Mitternachtsformel'), ("G″ < 0", 'Maximum prüfen'), ('einsetzen', 'G(x*)')], hl=1)
        + bsp('Übung ökonomische Funktionen, Aufgabe 1 iv', r'\(G(x) = -x^3 + 15x^2 + 25x - 375\)',
              [(r"\(G'(x) = -3x^2 + 30x + 25 = 0 \Rightarrow x^2 - 10x - \frac{25}{3} = 0\)", ''), (r'\(x = 5 + \sqrt{25 + \frac{25}{3}} \approx 10{,}77\)', ''),
               (r"\(G''(x) = -6x + 30\); \(G''(10{,}77) < 0\)", 'Maximum'), (r'\(G(10{,}77)\)', r'\(\approx 384{,}90\) GE')])
        + bsp('Übungsblatt 6, Aufgabe 3 b', r'\(G(x) = 2x - \frac{1}{50}(x - 10)^3 - 20\)',
              [(r"\(G'(x) = 2 - \frac{3}{50}(x - 10)^2 = 0 \Rightarrow (x - 10)^2 = \frac{100}{3}\)", ''), (r'\(x = 10 + \frac{10}{\sqrt{3}} \approx 15{,}77\)', r'\(G \approx 7{,}70\)')])
        + p('Alternative: \\(U\'(x) = K\'(x)\\). Bei \\(U = 150x\\) ist \\(U\' = 150\\), also \\(3x^2 - 30x + 125 = 150\\): dieselbe Gleichung.')
        + klausur_hinweis('„Berechnen Sie das Maximum des Gewinns“ bzw. „den Punkt des maximalen Gewinns“ ist sehr häufig gefragt.')
        + wahr('w-gmax', [("Im Gewinnmaximum gilt Grenzumsatz = Grenzkosten.", True, "U′ = K′."), ('Das Gewinnmaximum liegt immer an der Gewinngrenze.', False, 'Dort ist der Gewinn 0.')]),
    merk="Gewinnmaximum: G′(x) = 0 und G″(x) < 0 ⇔ U′(x) = K′(x) (bei festem Preis: K′(x) = p). Maximaler Gewinn: G(x*) einsetzen.",
    exam='Gewinnmaximum berechnen (jede Klausur).',
    fehler=['Nur x angeben, nicht den Gewinn.', "G″ nicht prüfen."],
    src='Übung ökonomische Funktionen A1; Übungsblatt 6 A3')

# ---------------------------------------------------------------- 4 Betriebsoptimum und -minimum
def bo_bild():
    k = lambda v: v * v - 15 * v + 125 + 375 / v
    kv = lambda v: v * v - 15 * v + 125
    Kp = lambda v: 3 * v * v - 30 * v + 125
    s, X, Y = graph([(k, 2, 16, 'var(--c3)', 'k(x)', 'Stückkosten k(x) = K(x)/x', 3.2), (kv, 0.5, 16, 'var(--c2)', 'k_v(x)', 'variable Stückkosten k_v(x)', 14.4),
                     (Kp, 0.5, 13, 'var(--primary)', "K′(x)", "Grenzkosten K′(x): schneiden k und k_v in deren Minimum.", 12.4)], (0, 16.5), (0, 260), xl='x', yl='GE/ME', ticks_x=(5, 7.5, 10, 15), ticks_y=(68.75, 112.2, 200))
    s += tpg(punkt(X(9.554), Y(112.219), 'var(--c3)', 6), 'Betriebsoptimum x ≈ 9,55: Minimum der Stückkosten k ≈ 112,22 = langfristige Preisuntergrenze. Dort gilt K′(x) = k(x).')
    s += tpg(punkt(X(7.5), Y(68.75), 'var(--c2)', 6), 'Betriebsminimum x = 7,5: Minimum der variablen Stückkosten k_v = 68,75 = kurzfristige Preisuntergrenze.')
    return svg(360, 260, s, 'Betriebsoptimum und Betriebsminimum', maxw=420)

t_bo = thema('betriebsoptimum', 'Betriebsoptimum, Betriebsminimum, Preisuntergrenzen', star=True,
    kern="Das Betriebsoptimum ist die Menge mit minimalen Stückkosten (k′(x) = 0); dort gilt K′(x) = k(x). Das Minimum der Stückkosten ist die langfristige Preisuntergrenze. Das Betriebsminimum ist das Minimum der variablen Stückkosten k_v; es ist die kurzfristige Preisuntergrenze (deckt wenigstens die veränderlichen Kosten).",
    kurz=p('Bei welcher Menge ist jedes Stück am billigsten? Das ist das <b>Betriebsoptimum</b>. Dort schneiden sich Stückkosten- und Grenzkostenkurve: \\(K\'(x) = k(x)\\).')
        + p('Und welcher Preis muss mindestens erzielt werden? Langfristig die minimalen Stückkosten (alle Kosten gedeckt), kurzfristig die minimalen <b>variablen</b> Stückkosten (Fixkosten fallen sowieso an).'),
    fig=fw('Grenzkosten schneiden die Stückkosten im Minimum. Tippe auf Kurven und Punkte.') + bild(bo_bild()),
    figcap='nach Übung „ökonomische Funktionen“, Aufgabe 1 v–vii und Übungsblatt 6, Aufgabe 3 c–d',
    article=h3('Definitionen')
        + tabelle(['Begriff', 'Bedingung', 'Bedeutung'], [
            ['Betriebsoptimum', r"\(k'(x) = 0\) bzw. \(K'(x) = k(x)\)", 'minimale Stückkosten = langfristige Preisuntergrenze'],
            ['Betriebsminimum', r"\(k_v'(x) = 0\) bzw. \(K'(x) = k_v(x)\)", 'minimale variable Stückkosten = kurzfristige Preisuntergrenze']])
        + bsp('Übungsblatt 6, Aufgabe 3 c, d', r'\(K(x) = \frac{1}{50}(x - 10)^3 + 20\)',
              [(r'\(k(x) = \frac{K(x)}{x}\); Minimum bei \(x = 15\)', r'\(k(15) = \frac{2{,}5 + 20}{15} = 1{,}5\)'), (r"Probe: \(K'(15) = \frac{3}{50} \cdot 25 = 1{,}5 = k(15)\)", 'Betriebsoptimum bei 15 ME')],
              'Laut Übungsblatt: „Ist die Änderung der Gesamtkosten K′(x) genauso groß wie die Stückkosten, nennt man diese Menge Betriebsoptimum.“')
        + bsp('Übung ökonomische Funktionen, Aufgabe 1 vi–vii', r'\(K(x) = x^3 - 15x^2 + 125x + 375\)',
              [(r"\(k_v(x) = x^2 - 15x + 125\), \(k_v'(x) = 2x - 15 = 0\)", r'\(x = 7{,}5;\ k_v = 68{,}75\): kurzfristige Preisuntergrenze'),
               (r"\(k(x) = x^2 - 15x + 125 + \frac{375}{x}\), \(k'(x) = 2x - 15 - \frac{375}{x^2} = 0\)", r'\(x \approx 9{,}55;\ k \approx 112{,}22\): Mindestpreis ohne Verlust')],
              'Die Gleichung für das Betriebsoptimum ist kubisch; ein Näherungswert genügt (Probieren oder Newton).')
        + klausur_hinweis('„Betriebsoptimum berechnen; Gewinn im Betriebsoptimum bei gegebenem Preis“ ist eine typische Klausuraufgabe.')
        + wahr('w-bo', [("Im Betriebsoptimum sind die Stückkosten minimal.", True, 'Definition.'), ('Die kurzfristige Preisuntergrenze deckt alle Kosten.', False, 'Nur die variablen Kosten.'),
                        ("Die Grenzkostenkurve schneidet die Stückkostenkurve in deren Minimum.", True, "K′ = k im Betriebsoptimum.")]),
    merk="Betriebsoptimum: min k(x), k′ = 0 ⇔ K′ = k; langfristige Preisuntergrenze. Betriebsminimum: min k_v(x); kurzfristige Preisuntergrenze (deckt nur variable Kosten).",
    exam='Betriebsoptimum und Preisuntergrenzen berechnen.',
    fehler=['Betriebsoptimum und -minimum vertauschen.', 'Fixkosten bei k_v mitnehmen.'],
    src='Übung ökonomische Funktionen A1; Übungsblatt 6 A3')

# ---------------------------------------------------------------- 5 Angebot, Nachfrage, Marktpreis
def markt_bild():
    s, X, Y = graph([(lambda v: 100 / (20 - v), 1, 18, 'var(--c2)', 'f_A', 'Angebotsfunktion f_A(x) = 100/(20 − x): je höher der Preis, desto mehr wird angeboten.', 17.2),
                     (lambda v: 35 - v * v / 15, 1, 18, 'var(--c3)', 'f_N', 'Nachfragefunktion f_N(x) = 35 − x²/15: je höher der Preis, desto weniger wird nachgefragt.', 4)],
                    (0, 18.5), (0, 52), xl='x', yl='p', ticks_x=(5, 10, 15), ticks_y=(20, 35))
    s += tpg(punkt(X(15), Y(20), 'var(--primary)', 6), 'Marktgleichgewicht: f_A(x) = f_N(x) bei x = 15, Marktpreis p = 20.')
    return svg(360, 250, s, 'Marktgleichgewicht', maxw=420)

t_markt = thema('angebot-nachfrage', 'Angebots-, Nachfragefunktion und Marktpreis',
    kern='Die Angebotsfunktion f_A gibt an, welcher Preis zu einer angebotenen Menge gehört (meist steigend), die Nachfragefunktion f_N, welcher Preis für eine nachgefragte Menge bezahlt wird (meist fallend). Der Marktpreis ergibt sich im Schnittpunkt f_A(x) = f_N(x).',
    kurz=p('Anbieter wollen bei hohen Preisen viel verkaufen, Nachfrager bei hohen Preisen wenig kaufen. Wo sich beide Kurven schneiden, passen Angebot und Nachfrage zusammen: das <b>Marktgleichgewicht</b> mit dem <b>Marktpreis</b>.'),
    fig=fw('Angebot und Nachfrage schneiden sich. Tippe auf Kurven und Punkt.') + bild(markt_bild()),
    figcap='nach Übung „ökonomische Funktionen“, Aufgabe 3',
    article=h3('Gleichgewicht berechnen')
        + bsp('Übung ökonomische Funktionen, Aufgabe 3', r'\(f_A(x) = \frac{100}{20 - x}\), \(f_N(x) = 35 - \frac{x^2}{15}\), \(1 \le x \le 18\)',
              [(r'Gleichsetzen: \(\frac{100}{20 - x} = 35 - \frac{x^2}{15}\)', ''), (r'Probe mit \(x = 15\): \(\frac{100}{5} = 20\) und \(35 - \frac{225}{15} = 20\)', ''), ('Ergebnis', 'x = 15 ME, Marktpreis p = 20')],
              'Gleichungen höheren Grades: sinnvolle Werte probieren und durch Einsetzen bestätigen.')
        + p('Aus einer Nachfragefunktion p(x) erhält man den Umsatz: \\(U(x) = p(x) \\cdot x\\). Dann ist der Umsatz nicht mehr linear (Monopolfall).')
        + wahr('w-markt', [('Im Marktgleichgewicht gilt f_A(x) = f_N(x).', True, 'Schnittpunkt.'), ('Die Nachfragefunktion steigt typischerweise.', False, 'Sie fällt.')]),
    merk='Angebotsfunktion steigend, Nachfragefunktion fallend; Marktpreis im Schnittpunkt f_A(x) = f_N(x). Mit Preis-Absatz-Funktion p(x): U(x) = p(x)·x.',
    exam='Übungsstoff; Gleichsetzen und Probe.',
    fehler=['Angebot und Nachfrage vertauschen.'],
    src='Übung ökonomische Funktionen A3')

KAPITEL = kapitel('k5', 'Ökonomische Funktionen',
    'Kosten, Umsatz und Gewinn als Funktionen: Fixkosten, Grenzkosten, Gewinnzone, Gewinnmaximum, Betriebsoptimum, Marktpreis.',
    ['Kostenfunktion', 'Gewinnzone', 'Gewinnmaximum', 'Betriebsoptimum', 'Marktpreis'], [t_kost, t_gz, t_gmax, t_bo, t_markt])
