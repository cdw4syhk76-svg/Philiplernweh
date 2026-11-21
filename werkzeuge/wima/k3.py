import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *
import sympy as sp

x, t = sp.symbols('x t', real=True)
assert sp.limit(180 / (sp.Rational(1, 2) + 10 * sp.exp(-t / 2)), t, sp.oo) == 360
assert sp.limit(210 / (sp.Rational(1, 10) + 20 * sp.exp(-t / 2)), t, sp.oo) == 2100
assert sp.limit((4 * x**2 - 160) / (x**2 + 4 * x), x, sp.oo) == 4
assert sp.limit((6 * x**3 - 4 * x**2 + 1) / (5 * x + 2 * x**3), x, sp.oo) == 3
assert sp.solve(sp.Eq(6 * sp.sqrt(3 * x - 120), sp.Symbol('y')), x) == [sp.Symbol('y')**2 / 108 + 40]

# ---------------------------------------------------------------- 1 Funktionsbegriff, Definitionsbereich
t_funk = thema('funktion', 'Funktionsbegriff und Definitionsbereich',
    kern='Eine Funktion f: D → ℝ ordnet jedem x aus dem Definitionsbereich D genau ein y = f(x) zu. Der maximale Definitionsbereich schließt aus, was nicht erlaubt ist: Nenner = 0, negative Zahlen unter einer geraden Wurzel, nicht positive Argumente im Logarithmus.',
    kurz=p('Eine Funktion ist eine Zuordnungsvorschrift mit einer strengen Regel: <b>Jedem x wird genau ein y zugeordnet.</b> Eine Menge wie {(1,1), (2,3), (1,4)} ist keine Funktion, weil der 1 zwei Werte zugeordnet werden.')
        + p('Der <b>Definitionsbereich</b> sind alle x, die man einsetzen darf. Drei Dinge sind verboten: durch null teilen, aus Negativem eine (gerade) Wurzel ziehen, den Logarithmus von Null oder Negativem nehmen.'),
    fig=fw('Drei Verbote, drei Beispiele. Tippe auf die Kästen.')
        + bild(svg(360, 200, ''.join(box(4 + i * 120, 4, 112, 192, t_, size=12, art='hl' if i == 1 else 'card', tip=tip) for i, (t_, tip) in enumerate([
            ('Nenner ≠ 0\n\nf(x) = 3/(x²−16)\n\nD = ℝ \\ {−4, 4}', 'x² − 16 = 0 für x = ±4. Diese Stellen fallen aus dem Definitionsbereich.'),
            ('Radikand ≥ 0\n\ng(t) = √(t−16)\n\nD = [16; ∞)', 'Unter der Wurzel darf nichts Negatives stehen: t − 16 ≥ 0 ⇒ t ≥ 16.'),
            ('ln-Argument > 0\n\nh(x) = ln(4−x²)\n\nD = (−2; 2)', '4 − x² > 0 ⇔ x² < 4 ⇔ −2 < x < 2. Übungsblatt 4, Aufgabe 5 iii.')])), 'Definitionsbereiche', maxw=420)),
    figcap='nach Übungsblatt 2, Aufgaben 2 und 4',
    article=h3('Definition')
        + p('Eine <b>Funktion</b> \\(f: D \\to \\mathbb{R},\\ x \\mapsto f(x)\\) ordnet jedem Element x der Menge D (<b>Definitionsbereich</b>) genau ein Element f(x) zu. Die Menge aller Funktionswerte heißt <b>Wertebereich</b> f(D).')
        + bsp('Übungsblatt 2, Aufgabe 2', 'Sind das Funktionen?',
              [(r'\(f(x) = \sqrt{x},\ x \in \mathbb{R}\)', 'nein: für x < 0 nicht definiert'), (r'\(f(x) = \sqrt{-x},\ x \in \mathbb{R}\)', 'nein: für x > 0 nicht definiert'),
               (r'\(\{(1,1), (2,3), (1,4), (2,5), (3,7)\}\)', 'nein: 1 und 2 haben je zwei Werte')],
              'Eine Funktion braucht die passende Angabe von D. Mit D = [0; ∞) wäre √x eine Funktion.')
        + h3('Maximaler Definitionsbereich')
        + fluss([('Nenner', '≠ 0 setzen'), ('gerade Wurzel', 'Radikand ≥ 0'), ('Logarithmus', 'Argument > 0')], hl=1)
        + p('Bei abschnittsweise definierten Funktionen (z. B. Übungsblatt 2, Aufgabe 3) gilt in jedem Abschnitt eine eigene Vorschrift; zum Skizzieren zeichnet man jeden Abschnitt einzeln.')
        + wahr('w-funk', [('Einer Stelle x darf eine Funktion zwei Werte zuordnen.', False, 'Genau ein Wert.'), (r'\(\ln(x - 3)\) ist für x = 3 definiert.', False, 'Argument 0 ist verboten.'),
                          (r'Der Definitionsbereich von \(\frac{1}{x}\) ist \(\mathbb{R} \setminus \{0\}\).', True, 'Nenner ≠ 0.')])
        + h3('Elementare Funktionen im Überblick')
        + tabelle(['Funktion', 'Vorschrift', 'Bemerkung'], [
            ['Betragsfunktion', r'\(f(x) = |x|\)', r'\(|x| = x\) für \(x \ge 0\), sonst \(-x\); Dreiecksungleichung \(|x + y| \le |x| + |y|\)'],
            ['Abrundungsfunktion (Gaußklammer)', r'\(f(x) = \lfloor x \rfloor = \max\{k \in \mathbb{Z} : k \le x\}\)', r'Treppenfunktion, z. B. \(\lfloor 2{,}7 \rfloor = 2\), \(\lfloor -1{,}3 \rfloor = -2\)'],
            ['lineare Funktion', r'\(f(x) = ax + b\)', 'a = Steigung, b = Schnitt mit der y-Achse'],
            ['quadratische Funktion (Parabel)', r'\(f(x) = ax^2 + bx + c\)', r'Nullstellen \(x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}\) bzw. \(x_{1,2} = -\frac{p}{2} \pm \sqrt{\left(\frac{p}{2}\right)^2 - q}\); \(b^2 > 4ac\): zwei, \(= 4ac\): eine, \(< 4ac\): keine reelle Nullstelle'],
            ['Polynomfunktion', r'\(p(x) = a_n x^n + \dots + a_1 x + a_0 = \sum_{i=0}^{n} a_i x^i\)', r'für \(a_n \ne 0\) Polynom vom Grad n; Potenzfunktion \(x^n\) („Parabel n-ter Ordnung“) ist ein Spezialfall'],
            ['rationale Funktion', r'\(r(x) = \frac{p(x)}{q(x)}\), \(D = \{x : q(x) \ne 0\}\)', 'Polynome sind spezielle rationale Funktionen (q = konstant)'],
            ['Hyperbelfunktion', r'\(f(x) = \frac{a}{x}\), \(x \ne 0\)', '„umgekehrt proportional“; einfachster Fall einer rationalen Funktion'],
            ['Wurzelfunktion', r'\(f(x) = x^{\frac{1}{n}} = \sqrt[n]{x}\), \(x \ge 0\)', r'nur für nichtnegative Radikanden definiert; Vorsicht: \(\sqrt[3]{-8} = -2\), aber \((-8)^{2/6} = 2\)'],
            ['Exponentialfunktion', r'\(f(x) = a^x\), \(a > 0, a \ne 1\)', r'Basis a; für a = e (Euler’sche Zahl ≈ 2,71828): \(e^x = \exp(x)\)'],
            ['Logarithmusfunktion', r'\(f(x) = \log_a x\), \(x > 0\)', r'Umkehrung von \(a^x\); a = e: \(\ln x\), a = 10: \(\lg x\)']]),
    merk='Funktion: jedem x aus D genau ein f(x). Maximaler Definitionsbereich: Nenner ≠ 0, Radikand (gerade Wurzel) ≥ 0, ln-Argument > 0.',
    exam='Vorarbeit für Stetigkeit, Grenzwerte, Kurvendiskussion.',
    fehler=['Bei ln „≥ 0“ statt „> 0“.'],
    src='Übungsblatt 2, A2–A4')

# ---------------------------------------------------------------- 2 Verkettung
t_verk = thema('verkettung', 'Verkettung von Funktionen',
    kern='Die Verkettung f∘g bedeutet (f∘g)(x) = f(g(x)): Erst wird g angewendet, dann f auf das Ergebnis. Sie ist nur möglich, wenn die Werte von g im Definitionsbereich von f liegen. In der Regel ist f∘g ≠ g∘f. Verkettungen erkennen ist die Grundlage der Kettenregel.',
    kurz=p('Eine Verkettung ist eine Maschine hinter einer anderen: Erst rechnet die innere Funktion g, ihr Ergebnis geht in die äußere Funktion f. Bei \\(h(x) = \\cos(x^2)\\) ist \\(g(x) = x^2\\) innen und \\(f(u) = \\cos(u)\\) außen.')
        + p('Die Reihenfolge zählt: \\(f(g(x))\\) ist meistens etwas anderes als \\(g(f(x))\\).'),
    fig=fw('Erst innen, dann außen. Tippe auf die Kästen.')
        + bild(svg(360, 130, box(4, 40, 70, 50, 'x', size=15, tip='Eingabe.') + box(100, 30, 100, 70, 'g\ninnen\n5x + 3', size=13, tip='Die innere Funktion rechnet zuerst.')
                   + box(226, 30, 100, 70, 'f\naußen\nu/5', size=13, art='hl', tip='Die äußere Funktion bekommt das Ergebnis der inneren.') + pfeil(74, 65, 100, 65) + pfeil(200, 65, 226, 65)
                   + T(180, 124, 'f(g(x)) = (5x + 3)/5 = x + 3/5', 13, 800), 'Verkettung', maxw=420)),
    figcap='nach Übungsblatt 3, Aufgabe 1',
    article=h3('Definition und Bedingung')
        + p('Für \\(f: D \\to \\mathbb{R}\\) und \\(g: E \\to \\mathbb{R}\\) ist \\((f \\circ g)(x) = f(g(x))\\) definiert, wenn \\(g(x) \\in D\\) liegt. Man liest „f nach g“.')
        + bsp('Übungsblatt 3, Aufgabe 1 i', r'\(f(x) = 5x + 3\), \(g(x) = \frac{1}{5}x\)',
              [(r'\(f(g(x)) = 5 \cdot \frac{x}{5} + 3\)', r'\(x + 3\)'), (r'\(g(f(x)) = \frac{1}{5}(5x + 3)\)', r'\(x + \frac{3}{5}\)')], 'Verschiedene Ergebnisse: Die Reihenfolge zählt.')
        + h3('Verkettungen zerlegen')
        + bsp('Übungsblatt 3, Aufgabe 2', 'Finde f und g mit f∘g = h.',
              [(r'\(h(x) = \cos(x^2)\)', r'innen \(g(x) = x^2\), außen \(f(u) = \cos u\)'), (r'\(h(x) = \cos^2(x) = (\cos x)^2\)', r'innen \(g(x) = \cos x\), außen \(f(u) = u^2\)')],
              'Beim Ableiten mit der Kettenregel muss man genau diese Zerlegung sehen, auch doppelt: cos(sin²(x)).')
        + wahr('w-verk', [('f∘g bedeutet: erst g, dann f.', True, 'Innen zuerst.'), ('f∘g und g∘f sind immer gleich.', False, 'Meist verschieden.')]),
    merk='(f∘g)(x) = f(g(x)): erst innen g, dann außen f; nur wenn g(x) ∈ D(f). Meist f∘g ≠ g∘f. Zerlegen in innen/außen ist die Vorarbeit für die Kettenregel.',
    exam='Vorarbeit für die Kettenregel (Ableitungen kommen immer).',
    fehler=['Innen und außen vertauschen.'],
    src='Übungsblatt 3')

# ---------------------------------------------------------------- 3 Umkehrfunktion
def umk_bild():
    f = lambda v: 0.25 * v * v + 2
    fi = lambda v: 2 * math.sqrt(v - 2)
    s, X, Y = graph([(f, 0, 3.6, 'var(--primary)', 'f', 'f(x) = 0,25x² + 2 für x ≥ 0 (streng monoton steigend, also umkehrbar).', 3.0),
                     (fi, 2, 8, 'var(--c2)', 'f⁻¹', 'f⁻¹(x) = 2√(x − 2): Spiegelung von f an der Winkelhalbierenden.', 7),
                     (lambda v: v, 0, 8, 'var(--axis2)', 'y = x', 'Winkelhalbierende: Spiegelachse.', 7.6)], (-0.3, 8.3), (-0.3, 8.3), ticks_x=(2, 4, 6, 8), ticks_y=(2, 4, 6, 8))
    return svg(360, 250, s, 'Umkehrfunktion', maxw=420)

t_umk = thema('umkehrfunktion', 'Umkehrfunktion',
    kern='Eine Funktion ist umkehrbar, wenn jedem y genau ein x gehört (z. B. bei strenger Monotonie). Man erhält f⁻¹, indem man y = f(x) nach x auflöst und dann x und y vertauscht. Der Definitionsbereich von f⁻¹ ist der Wertebereich von f. Graphisch: Spiegelung an der Winkelhalbierenden y = x.',
    kurz=p('Die Umkehrfunktion läuft „rückwärts“: Kennt man den Funktionswert, liefert sie das x. Aus \\(y = 0{,}25x^2 + 2\\) wird \\(x = 2\\sqrt{y - 2}\\).')
        + p('Das klappt nur, wenn die Zuordnung eindeutig umkehrbar ist. \\(x^2\\) auf ganz ℝ ist es nicht (2 und −2 haben denselben Wert). Schränkt man auf x ≥ 0 ein, geht es.'),
    fig=fw('Spiegelung an der Winkelhalbierenden. Tippe auf die Graphen.') + bild(umk_bild()),
    figcap='nach Übungen Analysis I, Funktionen 1b',
    article=h3('Vorgehen')
        + fluss([('1. Prüfen', 'umkehrbar? (streng monoton)'), ('2. Auflösen', 'y = f(x) nach x'), ('3. Tauschen', 'x und y vertauschen'), ('4. Bereiche', 'D(f⁻¹) = W(f)')], hl=1)
        + bsp('Übungen Analysis I, Funktionen 1a', r'\(f(x) = 6\sqrt{3x - 120}\)',
              [(r'Definitionsbereich: \(3x - 120 \ge 0 \Rightarrow x \ge 40\)', r'\(D = [40;\ \infty)\), Wertebereich \([0;\ \infty)\)'),
               (r'\(y = 6\sqrt{3x - 120} \Rightarrow \frac{y^2}{36} = 3x - 120 \Rightarrow x = \frac{y^2}{108} + 40\)', ''),
               (r'Tauschen', r'\(f^{-1}(x) = \frac{x^2}{108} + 40\), \(D(f^{-1}) = [0;\ \infty)\)')])
        + p('Graphisch erhält man \\(f^{-1}\\), indem man das Schaubild von f an der Winkelhalbierenden \\(y = x\\) spiegelt (Übungsblatt 4, Aufgabe 2). Ist eine Zuordnung nicht eindeutig umkehrbar, entsteht nur eine <b>Umkehrrelation</b>.')
        + wahr('w-umk', [('Der Definitionsbereich von f⁻¹ ist der Wertebereich von f.', True, 'Die Rollen tauschen.'), ('f(x) = x² auf ganz ℝ ist umkehrbar.', False, 'Nicht eindeutig: 2 und −2.')]),
    merk='Umkehrbar, wenn eindeutig (streng monoton). Auflösen nach x, x und y tauschen; D(f⁻¹) = W(f); graphisch Spiegelung an y = x.',
    exam='Übungsstoff; Umformen nach x braucht man überall.',
    fehler=['Bereiche nicht mittauschen.'],
    src='Übungsblatt 4 A1–A2, Übungen Analysis I')

# ---------------------------------------------------------------- 4 exp und ln
def expln_bild():
    s, X, Y = graph([(math.exp, -3, 2.1, 'var(--primary)', 'eˣ', 'eˣ: immer positiv, streng steigend, e⁰ = 1, für x → −∞ gegen 0.', 1.7),
                     (math.log, 0.05, 8, 'var(--c2)', 'ln x', 'ln x: nur für x > 0 definiert, ln 1 = 0, Umkehrfunktion von eˣ.', 7)], (-3.2, 8.2), (-3.2, 8.2), ticks_x=(1, 4, 8), ticks_y=(1, 4, 8))
    return svg(360, 250, s, 'Exponential- und Logarithmusfunktion', maxw=420)

t_expln = thema('exp-ln', 'Exponentialfunktion und Logarithmus',
    kern='eˣ ist für alle x definiert, immer positiv und streng steigend; für x → −∞ geht eˣ → 0. ln x ist die Umkehrfunktion, nur für x > 0 definiert. Rechenregeln: eᵃ·eᵇ = eᵃ⁺ᵇ, (eᵃ)ᵇ = eᵃᵇ, ln(a·b) = ln a + ln b, ln(aᵇ) = b·ln a, e^(ln x) = x, ln(eˣ) = x.',
    kurz=p('Wachstum, Zinsen, Sättigung: Überall steckt die <b>e-Funktion</b>. Ihre Umkehrung, der <b>natürliche Logarithmus ln</b>, holt Exponenten herunter, etwa beim Auflösen von \\(e^{0{,}5t} = 20\\).')
        + p('Für Sättigungswerte ist eine Eigenschaft entscheidend: \\(e^{-t} \\to 0\\) für \\(t \\to \\infty\\).'),
    fig=fw('eˣ und ln x sind Spiegelbilder. Tippe auf die Graphen.') + bild(expln_bild()),
    figcap='nach Gliederung 3: exp und ln, Funktionalgleichungen',
    article=h3('Rechenregeln (Funktionalgleichungen)')
        + tabelle(['e-Funktion', 'Logarithmus'], [['eᵃ · eᵇ = eᵃ⁺ᵇ', 'ln(a · b) = ln a + ln b'], ['eᵃ : eᵇ = eᵃ⁻ᵇ', 'ln(a : b) = ln a − ln b'], ['(eᵃ)ᵇ = eᵃ·ᵇ', 'ln(aᵇ) = b · ln a'], ['e⁰ = 1', 'ln 1 = 0'], ['e^(ln x) = x', 'ln(eˣ) = x']])
        + bsp('Gleichung lösen', r'\(20 \cdot e^{-0{,}5t} = 1\)', [(r'\(e^{-0{,}5t} = 0{,}05\)', ''), (r'\(-0{,}5t = \ln 0{,}05 \approx -2{,}996\)', r'\(t \approx 5{,}99\)')])
        + h3('Verhalten an den Rändern')
        + liste([r'\(e^{x} \to \infty\) für \(x \to \infty\); \(e^{x} \to 0\) für \(x \to -\infty\)', r'\(e^{-0{,}5t} \to 0\) für \(t \to \infty\): Das braucht man für Sättigungswerte.',
                 r'\(\ln x \to -\infty\) für \(x \downarrow 0\); \(\ln x \to \infty\) für \(x \to \infty\), aber sehr langsam'])
        + wahr('w-expln', [(r'\(\ln(a + b) = \ln a + \ln b\)', False, 'Nur für Produkte: ln(a·b).'), (r'\(e^{-t} \to 0\) für \(t \to \infty\)', True, 'Sättigungswerte nutzen das.'),
                           (r'\(\ln 0\) ist nicht definiert.', True, 'Argument muss positiv sein.')]),
    merk='eˣ > 0, streng steigend, e⁰ = 1, eˣ → 0 für x → −∞. ln x nur für x > 0, ln 1 = 0, Umkehrfunktion. Regeln: eᵃeᵇ = eᵃ⁺ᵇ, ln(ab) = ln a + ln b, ln(aᵇ) = b ln a.',
    exam='Grundlage für Sättigungswert, Ableitungen und Integrale.',
    fehler=['ln einer Summe zerlegen.'],
    src='Gliederung 3, Mitschrift')

# ---------------------------------------------------------------- 5 Grenzwerte von Funktionen, Sättigungswert
def satt_bild():
    Yf = lambda v: 180 / (0.5 + 10 * math.exp(-0.5 * v))
    s, X, Y = graph([(Yf, 0, 20, 'var(--primary)', 'S(t)', 'S(t) = 180/(0,5 + 10e^(−0,5t)): steigt erst langsam, dann schnell, dann flacht sie ab.', 4)],
                    (0, 20.5), (0, 400), xl='t', yl='S(t)', ticks_x=(5, 10, 15, 20), ticks_y=(100, 200, 360))
    s += tpg(f'<line x1="{X(0)}" y1="{Y(360)}" x2="{X(20.5)}" y2="{Y(360)}" style="stroke:var(--c2)" stroke-width="2" stroke-dasharray="6 4"/>', 'Sättigungswert 360: Für t → ∞ geht e^(−0,5t) → 0, also S → 180/0,5 = 360.')
    s += T(X(20), Y(360) - 8, 'Sättigungswert 360', 12, 800, 'end', 'var(--c2)')
    s += tpg(punkt(X(0), Y(Yf(0)), 'var(--primary)', 5), f'Startwert S(0) = 180/10,5 ≈ {Yf(0):.1f}'.replace('.', ','))
    return svg(360, 250, s, 'Sättigungswert', maxw=420)

t_satt = thema('saettigungswert', 'Grenzwerte von Funktionen und Sättigungswert', star=True,
    kern='Für x → ∞ verhält sich eine gebrochenrationale Funktion wie der Quotient der höchsten Potenzen (gleicher Grad: Quotient der Leitkoeffizienten). Bei logistischen Funktionen wie S(t) = a/(b + c·e^(−kt)) geht e^(−kt) → 0, der Sättigungswert ist a/b. Ausdrücke „0/0“ oder „∞/∞“ löst man durch Kürzen, Erweitern oder mit L’Hospital.',
    kurz=p('Ein Wirtschaftszweig wächst, aber nicht ewig. Das Einkommen folgt einer <b>logistischen Funktion</b> \\(S(t) = \\frac{180}{0{,}5 + 10e^{-0{,}5t}}\\). Welcher Wert wird „auf lange Sicht“ erreicht?')
        + p('Für \\(t \\to \\infty\\) wird \\(e^{-0{,}5t}\\) winzig, also bleibt \\(\\frac{180}{0{,}5} = 360\\). Das ist der <b>Sättigungswert</b>. Diese Aufgabe ist sehr häufig gefragt.'),
    fig=fw('Die Kurve nähert sich ihrem Sättigungswert. Tippe auf Kurve, Linie und Punkt.') + bild(satt_bild()),
    figcap='nach Übungsblatt 4, Aufgabe 3 und der Klausuraufgabe zum Sättigungswert',
    article=h3('Sättigungswert einer logistischen Funktion')
        + fx('Sättigungswert', r'\lim_{t \to \infty} \frac{a}{b + c \cdot e^{-kt}} = \frac{a}{b + c \cdot 0} = \frac{a}{b}', 'Der e-Term verschwindet für große t, es bleibt Zähler durch die Konstante im Nenner.',
             r'\(\lim_{t\to\infty} \frac{180}{0{,}5 + 10e^{-0{,}5t}} = \frac{180}{0{,}5} = 360\)')
        + bsp('Übungsblatt 4, Aufgabe 3', r'\(Y(t) = \frac{210}{0{,}1 + 20 \cdot e^{-kt}},\ t \ge 0\)', [(r'Für \(t \to \infty\): \(e^{-kt} \to 0\)', ''), (r'\(\lim Y(t) = \frac{210}{0{,}1}\)', r'\(2.100\)')],
              'Schreibe in der Klausur den Grenzwert sauber hin und begründe kurz, warum der e-Term verschwindet.')
        + h3('Gebrochenrationale Funktionen für x → ∞')
        + bsp('Klausurstil', r'Absatz in Abhängigkeit vom Einkommen: \(C(y) = \frac{4y^2 - 160}{y^2 + 4y}\). Was passiert für \(y \to \infty\)?',
              [(r'\(y^2\) ausklammern: \(\frac{y^2(4 - \frac{160}{y^2})}{y^2(1 + \frac{4}{y})}\)', ''), (r'Reste gehen gegen 0', r'\(\lim_{y \to \infty} C(y) = 4\)')],
              'Wächst das Einkommen über alle Grenzen, nähert sich der Absatz 4 Mengeneinheiten an.')
        + bsp('Übungen Analysis I, Grenzwerte 2c', r'\(\lim_{x\to\infty} \frac{6x^3 - 4x^2 + 1}{5x + 2x^3}\)', [('Gleicher Grad 3', r'\(\frac{6}{2} = 3\)')])
        + weiter('Und wenn Zähler und Nenner beide gegen 0 gehen?')
        + h3('Unbestimmte Ausdrücke')
        + p('„0/0“ oder „∞/∞“ hat keinen festen Wert. Hilfen: <b>kürzen</b> (z. B. \\(\\frac{x^2 - 4}{x - 2} = x + 2\\)), <b>erweitern</b> (bei Wurzeln mit \\(\\sqrt{h + 1} + 1\\), Übungsblatt 4, Aufgabe 4) oder die <b>Regel von L’Hospital</b> (Zähler und Nenner getrennt ableiten, Oberthema 4).')
        + h3('Uneigentliche Grenzwerte')
        + p('Wächst \\(f(x)\\) für \\(x \\to x_0\\) (oder \\(x \\to \\infty\\)) über jede Schranke, schreibt man \\(\\lim f(x) = \\infty\\) bzw. \\(-\\infty\\) und spricht von einem <b>uneigentlichen Grenzwert</b>. Einfach gesagt: Es gibt keinen echten Grenzwert (keine Zahl), aber eine klare Richtung. Beispiele: \\(\\lim_{x \\to \\infty} x^2 = \\infty\\); \\(\\lim_{x \\downarrow 0} \\frac{1}{x} = \\infty\\), \\(\\lim_{x \\uparrow 0} \\frac{1}{x} = -\\infty\\) – an einer <b>Polstelle</b> ist der Grenzwert uneigentlich, links und rechts oft mit verschiedenem Vorzeichen. Bei gebrochen-rationalen Funktionen mit höherem Zählergrad ist der Grenzwert für \\(x \\to \\infty\\) ebenfalls uneigentlich.')
        + klausur_hinweis('Sättigungswert bzw. Grenzwert für t → ∞ ist eine typische erste Aufgabe.')
        + wahr('w-satt', [(r'\(\lim_{t\to\infty} \frac{100}{0{,}2 + 5e^{-t}} = 500\)', True, '100/0,2.'), (r'Für \(t \to \infty\) geht \(e^{-0{,}5t} \to \infty\).', False, 'Gegen 0.'),
                          (r'\(\lim_{x\to\infty} \frac{3x^2}{x^3 + 1} = 3\)', False, 'Zählergrad kleiner: 0.')]),
    merk='Sättigungswert: lim a/(b + c·e^(−kt)) = a/b, weil e^(−kt) → 0. Gebrochenrational für x → ∞: höchste Potenz ausklammern. 0/0 und ∞/∞: kürzen, erweitern, L’Hospital.',
    exam='Typische erste Aufgabe: Sättigungswert oder Grenzwert für t → ∞ bzw. y → ∞.',
    fehler=['e^(−kt) gegen ∞ statt gegen 0 laufen lassen.', 'Konstante im Nenner übersehen.'],
    src='Übungsblatt 4 A3–A4, Übungen Analysis I')

# ---------------------------------------------------------------- 6 Stetigkeit
def unst_tafel(art):
    if art == 'sprung':
        s, X, Y = graph([(lambda v: v - 1, -3, 0, 'var(--primary)', '', 'Links: x − 1, Grenzwert an 0 ist −1.', None), (lambda v: 2 * v + 1, 0.01, 2, 'var(--primary)', '', 'Rechts: 2x + 1, Grenzwert an 0 ist 1.', None)], (-3, 2.2), (-4, 5), ticks_x=(-2, 1), ticks_y=(-1, 1))
        s += punkt(X(0), Y(-1), 'var(--primary)', 5) + f'<circle cx="{X(0)}" cy="{Y(1)}" r="5" style="fill:var(--card);stroke:var(--primary)" stroke-width="2"/>'
        s += T(X(1.5), Y(4.4), 'Sprung', 14, 800, 'middle', 'var(--c3)')
    elif art == 'pol':
        s, X, Y = graph([(lambda v: 1 / (v - 1), -2, 0.97, 'var(--primary)', '', 'Für x ↑ 1 geht f gegen −∞.', None), (lambda v: 1 / (v - 1), 1.03, 4, 'var(--primary)', '', 'Für x ↓ 1 geht f gegen +∞.', None)], (-2, 4), (-6, 6), ticks_x=(1,), ticks_y=(-4, 4))
        s += f'<line x1="{X(1)}" y1="{Y(6)}" x2="{X(1)}" y2="{Y(-6)}" style="stroke:var(--c3)" stroke-dasharray="5 4"/>' + T(X(2.6), Y(5), 'Pol', 14, 800, 'middle', 'var(--c3)')
    else:
        s, X, Y = graph([(lambda v: v + 2, -3, 3, 'var(--primary)', '', 'f(x) = (x² − 4)/(x − 2) = x + 2 für x ≠ 2.', None)], (-3, 3.5), (-2, 6), ticks_x=(2,), ticks_y=(4,))
        s += f'<circle cx="{X(2)}" cy="{Y(4)}" r="5.5" style="fill:var(--card);stroke:var(--c3)" stroke-width="2.4"/>' + T(X(-1.5), Y(5.2), 'Lücke', 14, 800, 'middle', 'var(--c3)')
    return svg(360, 250, s, art, maxw=420)

t_stet = thema('stetigkeit', 'Stetigkeit und Unstetigkeitsstellen', star=True,
    kern='f ist an x₀ stetig, wenn der linksseitige und der rechtsseitige Grenzwert existieren, gleich sind und mit f(x₀) übereinstimmen. Unstetigkeitstypen: Sprung (links- und rechtsseitiger Grenzwert verschieden), Pol (Grenzwert ±∞) und Lücke (Grenzwert existiert, aber ≠ f(x₀) oder x₀ ∉ D, hebbar). Bei abschnittsweise definierten Funktionen bestimmt man eine Konstante c so, dass beide Seiten zusammenpassen.',
    kurz=p('Anschaulich: Eine Funktion ist <b>stetig</b>, wenn man ihren Graphen ohne Absetzen zeichnen kann. Eine Rabattstaffel ist es nicht: Ab 500 Stück springt der Preis plötzlich nach unten.')
        + p('Es gibt drei Typen von Unstetigkeit: <b>Sprung</b>, <b>Pol</b> und <b>Lücke</b>. Und eine typische Klausuraufgabe: „Bestimmen Sie c so, dass die Funktion stetig ist.“'),
    fig=fw('Drei Unstetigkeitstypen. Schalte um und tippe auf die Graphen.') + tafeln('tf-unst', ['Sprung', 'Pol', 'Lücke'], [unst_tafel('sprung'), unst_tafel('pol'), unst_tafel('luecke')]),
    figcap='nach Übungsblatt 4, Einleitung zu Aufgabe 5',
    article=h3('Definition')
        + fx('Stetigkeit in x₀', r'\lim_{x \uparrow x_0} f(x) = \lim_{x \downarrow x_0} f(x) = f(x_0)', 'Linksseitiger Grenzwert, rechtsseitiger Grenzwert und Funktionswert sind gleich.',
             r'\(f(x) = x^2\) ist überall stetig.')
        + h3('Die drei Unstetigkeitstypen')
        + tabelle(['Typ', 'Kennzeichen', 'Beispiel'], [
            ['Sprung', r'\(\lim_{x \downarrow x_0} f(x) = c_1 \ne c_2 = \lim_{x \uparrow x_0} f(x)\)', 'Rabattstaffel, abschnittsweise Funktion'],
            ['Pol (Unendlichkeitsstelle)', 'f geht für x ↓ x₀ und/oder x ↑ x₀ gegen ±∞', r'\(\frac{1}{x - 1}\) an \(x_0 = 1\)'],
            ['Lücke (hebbar)', 'beidseitiger Grenzwert c existiert, aber c ≠ f(x₀) oder x₀ ∉ D', r'\(\frac{x^2 - 4}{x - 2}\) an \(x_0 = 2\)']])
        + weiter('Die Klausuraufgabe dreht das um: Man soll die Funktion stetig machen.')
        + h3('Konstante c bestimmen')
        + bsp('Klausurstil', r'\(f(x) = \begin{cases} x^2 + c, & x \le 2 \\ 3x - 1, & x > 2 \end{cases}\). Für welches c ist f stetig?',
              [(r'Links an \(x_0 = 2\): \(\lim_{x \uparrow 2} f(x) = 4 + c = f(2)\)', ''), (r'Rechts: \(\lim_{x \downarrow 2} f(x) = 3 \cdot 2 - 1 = 5\)', ''), (r'Gleichsetzen: \(4 + c = 5\)', r'\(c = 1\)')],
              'Außerhalb der Nahtstelle sind beide Teile (Polynome) stetig; nur die Nahtstelle muss man prüfen.')
        + bsp('Übungsblatt 4, Aufgabe 6 (Rabattstaffel)', 'Basispreis 50 €/ME; ab 500 ME 10 %, ab 1.000 ME 20 %, ab 2.000 ME 35 % Rabatt auf die gesamte Menge.',
              [(r'Bei 500 ME: \(\lim_{x \uparrow 500} = 25.000\), \(f(500) = 22.500\)', 'Sprung'), ('Monotonie', 'nicht monoton: Der Bestellwert fällt an den Sprungstellen'),
               ('Folge für Kunden', 'Bestellungen knapp unter einer Stufe werden aufgestockt (z. B. 950 ME → 1.000 ME ist billiger)')])
        + klausur_hinweis('„Wann ist die gegebene Funktion stetig? Bestimmen Sie die Konstante c so, dass die Funktion stetig ist.“ kam so in einer Klausur.')
        + wahr('w-stet', [('Bei einer Lücke existiert der Grenzwert.', True, 'Er stimmt nur nicht mit f(x₀) überein oder x₀ fehlt in D.'),
                          ('Eine Rabattstaffel mit Mengenrabatt auf die gesamte Menge ist stetig.', False, 'Sie springt an den Rabattgrenzen.'),
                          (r'\(\frac{1}{x}\) hat an 0 einen Pol.', True, 'Grenzwerte ±∞.')])
        + h3('Eigenschaften stetiger Funktionen')
        + p(r'<b>Zwischenwertsatz:</b> Ist \(f: [a, b] \to \mathbb{R}\) stetig mit \(f(a) < 0\) und \(f(b) > 0\) (oder umgekehrt), dann gibt es ein \(x \in (a, b)\) mit \(f(x) = 0\). Einfach gesagt: Eine stetige Kurve kann nicht von unten nach oben springen, ohne die x-Achse zu treffen.')
        + p(r'Folgerung: <b>Jedes Polynom ungeraden Grades hat mindestens eine reelle Nullstelle</b> (für \(a_n > 0\) gilt \(\lim_{x\to\infty} p(x) = +\infty\) und \(\lim_{x\to-\infty} p(x) = -\infty\)). Ein Polynom geraden Grades muss keine Nullstelle haben, z. B. \(x^{2k} + 1\).')
        + p(r'<b>Stetigkeit der Umkehrfunktion:</b> Ist f auf [a, b] stetig und streng monoton wachsend (fallend), dann ist auch die Umkehrfunktion stetig und streng monoton wachsend (fallend). Beispiele: die k-te Wurzel als Umkehrung von \(x^k\) auf \(\mathbb{R}_0^+\), der natürliche Logarithmus als Umkehrung von \(e^x\). Intervalle: \([a,b]\) abgeschlossen, \((a,b)\) offen, \([a,b)\) und \((a,b]\) halboffen.'),
    merk='Stetig in x₀: links- und rechtsseitiger Grenzwert = f(x₀). Sprung: einseitige Grenzwerte verschieden; Pol: ±∞; Lücke: Grenzwert existiert, aber ≠ f(x₀) oder x₀ ∉ D. Konstante c: beide Seiten an der Nahtstelle gleichsetzen.',
    exam='Konstante c für Stetigkeit bestimmen; Unstetigkeitstypen erkennen.',
    fehler=['Nur einen einseitigen Grenzwert prüfen.', 'Lücke und Pol verwechseln.'],
    src='Übungsblatt 4, A5–A6')

KAPITEL = kapitel('k3', 'Funktionen, Grenzwerte, Stetigkeit',
    'Funktionen verstehen, verketten, umkehren; Grenzwerte und Sättigungswerte berechnen; Stetigkeit prüfen.',
    ['Funktionsbegriff', 'Verkettung', 'Umkehrfunktion', 'exp und ln', 'Sättigungswert', 'Stetigkeit'],
    [t_funk, t_verk, t_umk, t_expln, t_satt, t_stet])
