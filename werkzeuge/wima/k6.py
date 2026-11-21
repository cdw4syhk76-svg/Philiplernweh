import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *
import sympy as sp

x, t, a = sp.symbols('x t a', positive=True)
assert sp.integrate(t * sp.exp(2 * t), (t, 0, 2)) == sp.Rational(1, 4) + 3 * sp.exp(4) / 4
assert sp.integrate(x * sp.cos(x), (x, 0, sp.pi)) == -2
assert sp.integrate(x * sp.sqrt(1 + 2 * x), (x, 0, 4)) == sp.Rational(298, 15)
assert sp.integrate(6 * x / sp.sqrt(3 * x**2 + a**2), (x, 0, a)) == 2 * a
assert sp.integrate(3 * x**2 + 4 * x - 2, (x, 1, 3)) == 38
assert sp.integrate(2 * x * sp.exp(x**2), (x, 0, 1)) == sp.E - 1
assert sp.simplify(sp.diff((x - 1) * sp.exp(x), x) - x * sp.exp(x)) == 0

# ---------------------------------------------------------------- 1 Stammfunktion, unbestimmtes Integral
t_stamm = thema('stammfunktion', 'Stammfunktion und unbestimmtes Integral',
    kern="F ist Stammfunktion von f, wenn F′(x) = f(x). Das unbestimmte Integral ∫ f(x) dx = F(x) + C ist die Menge aller Stammfunktionen. Grundintegrale: ∫ xⁿ dx = xⁿ⁺¹/(n+1) + C (n ≠ −1), ∫ 1/x dx = ln|x| + C, ∫ eˣ dx = eˣ + C, ∫ sin x dx = −cos x + C, ∫ cos x dx = sin x + C. Probe immer durch Ableiten.",
    kurz=p('Integrieren ist Ableiten rückwärts. Gesucht ist eine Funktion F, deren Ableitung f ergibt. Zu \\(f(x) = 3x^2\\) passt \\(F(x) = x^3\\), aber auch \\(x^3 + 5\\): Konstanten verschwinden beim Ableiten, deshalb schreibt man \\(+ C\\).')
        + p('Ökonomisch: Aus den Grenzkosten K′(x) erhält man so die Kostenfunktion K(x). Das C sind dann die Fixkosten.'),
    fig=fw('Ableiten und Integrieren sind Gegenrichtungen. Tippe auf die Kästen.')
        + bild(svg(360, 150, box(4, 40, 140, 70, 'F(x) = x³ + C', size=15, tip='Stammfunktion, inklusive beliebiger Konstante C.') + box(216, 40, 140, 70, 'f(x) = 3x²', size=15, art='hl', tip='Die abgeleitete Funktion.')
                       + pfeil(144, 60, 216, 60) + pfeil(216, 92, 144, 92) + T(180, 52, 'ableiten', 12, 700, fill='var(--muted)') + T(180, 112, 'integrieren', 12, 700, fill='var(--muted)'), 'Stammfunktion', maxw=420)),
    figcap='nach Gliederung 6: Das unbestimmte Integral',
    article=h3('Grundintegrale')
        + tabelle(['f(x)', 'Stammfunktion F(x)'], [['xⁿ (n ≠ −1)', 'xⁿ⁺¹/(n + 1)'], ['1/x', 'ln|x|'], ['eˣ', 'eˣ'], ['e^(ax)', '(1/a)·e^(ax)'], ['sin x', '−cos x'], ['cos x', 'sin x'], ['√x = x^(1/2)', '⅔·x^(3/2)']])
        + p('Faktor- und Summenregel gelten wie beim Ableiten: \\(\\int (3x^2 + 4x - 2)\\,dx = x^3 + 2x^2 - 2x + C\\).')
        + bsp('Von Grenzkosten zu Kosten', r"\(K'(x) = 1{,}5x^2 - 4x + 4\), \(K(10) = 372\)", [(r'\(K(x) = 0{,}5x^3 - 2x^2 + 4x + C\)', ''), (r'\(K(10) = 340 + C = 372\)', r'\(C = 32\) = Fixkosten')])
        + falle('Bei ∫ x⁻¹ die Potenzregel anwenden (Division durch 0). Hier gilt ln|x|.')
        + wahr('w-stamm', [(r'\(\int x^3\,dx = \frac{x^4}{4} + C\)', True, 'Potenzregel rückwärts.'), (r'\(\int \frac{1}{x}\,dx = \frac{x^0}{0} + C\)', False, 'ln|x| + C.'),
                           (r'\(\int \sin x\,dx = \cos x + C\)', False, '−cos x + C.')]),
    merk="F′ = f; ∫ f dx = F + C. ∫xⁿ = xⁿ⁺¹/(n+1), ∫1/x = ln|x|, ∫eˣ = eˣ, ∫sin = −cos, ∫cos = sin. Probe durch Ableiten. Aus Grenzkosten: K = ∫K′ dx, C = Fixkosten.",
    exam='Grundlage für die Integralaufgabe (jede Klausur).',
    fehler=['+C vergessen.', 'Vorzeichen bei ∫ sin x.'],
    src='Gliederung 6')

# ---------------------------------------------------------------- 2 Bestimmtes Integral, Hauptsatz
def flaeche_bild():
    f = lambda v: 0.25 * v * v + 1
    s, X, Y = graph([(f, 0, 4.6, 'var(--primary)', 'f', 'f(x) = 0,25x² + 1', 4.3)], (-0.3, 4.8), (0, 6.5), ticks_x=(1, 3), ticks_y=(2, 4))
    s = tpg(flaeche([(X(1), Y(0))] + [(X(1 + i * 0.05), Y(f(1 + i * 0.05))) for i in range(41)] + [(X(3), Y(0))], 'var(--primary)', .22),
            'Fläche unter f zwischen 1 und 3: ∫₁³ f(x) dx = F(3) − F(1) = (27/12 + 3) − (1/12 + 1) = 4 1/6 ≈ 4,17.') + s
    return svg(360, 250, s, 'Bestimmtes Integral', maxw=420)

t_best = thema('bestimmtes-integral', 'Bestimmtes Integral und Hauptsatz',
    kern='Das bestimmte Integral ∫ₐᵇ f(x) dx ist die (orientierte) Fläche zwischen Graph und x-Achse von a bis b. Fundamentalsatz (Hauptsatz): ∫ₐᵇ f(x) dx = F(b) − F(a) = [F(x)]ₐᵇ für jede Stammfunktion F. Flächen unterhalb der x-Achse zählen negativ.',
    kurz=p('Mit dem bestimmten Integral misst man Flächen und summiert Änderungen auf: Aus der Grenzkostenkurve erhält man, wie stark die Kosten zwischen 10 und 20 Stück steigen.')
        + p('Gerechnet wird mit dem <b>Hauptsatz</b>: Stammfunktion bilden, obere Grenze einsetzen, untere Grenze einsetzen, subtrahieren.'),
    fig=fw('Die Fläche unter der Kurve. Tippe auf die Fläche.') + bild(flaeche_bild()),
    figcap='eigenes Beispiel zu Gliederung 6: Fundamentalsatz',
    article=h3('Der Hauptsatz')
        + fx('Hauptsatz der Differential- und Integralrechnung', r'\int_a^b f(x)\,dx = \big[F(x)\big]_a^b = F(b) - F(a)', 'Stammfunktion an der oberen Grenze minus an der unteren Grenze. Das C hebt sich weg.',
             r'\(\int_1^3 (3x^2 + 4x - 2)\,dx = [x^3 + 2x^2 - 2x]_1^3 = 39 - 1 = 38\)')
        + bsp('Übungsblatt 6, Aufgabe 4 b (Ergebnis)', r'\(\int_0^{\pi} x \cos x\,dx\)', [(r'Stammfunktion (partielle Integration, nächstes Unterthema): \(x \sin x + \cos x\)', ''),
               (r'\([x \sin x + \cos x]_0^{\pi} = (0 - 1) - (0 + 1)\)', r'\(-2\)')], 'Ein negatives Ergebnis heißt: Mehr Fläche liegt unter als über der x-Achse.')
        + h3('Rechenregeln')
        + liste([r'\(\int_a^b (f + g)\,dx = \int_a^b f\,dx + \int_a^b g\,dx\)', r'\(\int_a^b c \cdot f\,dx = c \int_a^b f\,dx\)', r'\(\int_a^a f\,dx = 0\), \(\int_a^b f\,dx = -\int_b^a f\,dx\)'])
        + wahr('w-best', [(r'\(\int_0^2 2x\,dx = 4\)', True, '[x²]₀² = 4.'), ('Beim bestimmten Integral muss man +C angeben.', False, 'C hebt sich weg.'),
                          ('Flächen unter der x-Achse zählen beim Integral negativ.', True, 'Orientierte Fläche.')]),
    merk='∫ₐᵇ f dx = F(b) − F(a) (Hauptsatz); C fällt weg; Flächen unter der x-Achse negativ; Linearität.',
    exam='Bestimmte Integrale berechnen (z. B. ∫₀² t·e^(2t) dt).',
    fehler=['Untere Grenze nicht abziehen.', 'Vorzeichen beim Einsetzen.'],
    src='Gliederung 6')

# ---------------------------------------------------------------- 3 Substitution
t_subst = thema('substitution', 'Integration durch Substitution', star=True,
    kern='Substitution löst Integrale der Form ∫ f(g(x))·g′(x) dx: Man setzt u = g(x), ersetzt dx = du/g′(x) und integriert nach u. Beim bestimmten Integral rechnet man die Grenzen mit um (oder resubstituiert). Typisch: innere Funktion, deren Ableitung als Faktor dasteht.',
    kurz=p('\\(\\int 2x \\cdot e^{x^2}\\,dx\\): Die innere Funktion \\(x^2\\) hat die Ableitung \\(2x\\), und die steht als Faktor davor. Mit \\(u = x^2\\) wird daraus \\(\\int e^u\\,du = e^u\\). Das ist die Kettenregel rückwärts.')
        + p('Auch wenn die Ableitung nicht genau passt, hilft Substitution oft, etwa bei \\(\\int t\\sqrt{t - 1}\\,dt\\) mit \\(u = t - 1\\).'),
    fig=fw('Die Schritte der Substitution. Tippe auf die Kästen.')
        + bild(svg(360, 210, ''.join(box(4, 4 + i * 52, 352, 46, t_, size=13, art='hl' if i == 1 else 'card', tip=tip) for i, (t_, tip) in enumerate([
            ('1. u = g(x) wählen (innere Funktion)', 'Hier u = x² bei ∫ 2x·e^(x²) dx.'), ('2. du = g′(x) dx  →  dx = du / g′(x)', 'du = 2x dx; das 2x kürzt sich mit dem Faktor vorne.'),
            ('3. nach u integrieren', '∫ e^u du = e^u.'), ('4. zurücksetzen oder Grenzen umrechnen', 'e^(x²) + C; bei Grenzen 0 und 1: u von 0 bis 1.')])), 'Substitution', maxw=420)),
    figcap='nach Übungsblatt 6, Aufgabe 4 a und c',
    article=h3('Vorgehen')
        + bsp('Grundbeispiel', r'\(\int_0^1 2x \cdot e^{x^2}\,dx\)', [(r'\(u = x^2,\ du = 2x\,dx\); Grenzen: \(x = 0 \to u = 0,\ x = 1 \to u = 1\)', ''), (r'\(\int_0^1 e^u\,du = [e^u]_0^1\)', r'\(e - 1 \approx 1{,}72\)')])
        + bsp('Übungsblatt 6, Aufgabe 4 c', r'\(\int t\sqrt{t - 1}\,dt\)',
              [(r'\(u = t - 1\Rightarrow t = u + 1,\ dt = du\)', ''), (r'\(\int (u + 1)\sqrt{u}\,du = \int (u^{3/2} + u^{1/2})\,du\)', ''),
               (r'\(= \frac{2}{5}u^{5/2} + \frac{2}{3}u^{3/2} + C\)', r'\(\frac{2}{5}(t-1)^{5/2} + \frac{2}{3}(t-1)^{3/2} + C\)')])
        + bsp('Übungen Analysis I, Integration b', r'\(\int_0^a \frac{6x}{\sqrt{3x^2 + a^2}}\,dx\) (a > 0)',
              [(r'\(u = 3x^2 + a^2,\ du = 6x\,dx\); Grenzen \(a^2\) bis \(4a^2\)', ''), (r'\(\int_{a^2}^{4a^2} u^{-1/2}\,du = [2\sqrt{u}]_{a^2}^{4a^2} = 4a - 2a\)', r'\(2a\)')])
        + p('Übungsblatt 6, Aufgabe 4 a lautet allgemein \\(\\int_a^b t \\cdot f(t^2)\\,dt\\): Mit \\(u = t^2\\), \\(du = 2t\\,dt\\) wird daraus \\(\\frac{1}{2}\\int_{a^2}^{b^2} f(u)\\,du\\).')
        + falle('Beim bestimmten Integral die Grenzen nicht umrechnen, aber trotzdem in u einsetzen.')
        + wahr('w-subst', [('Substitution ist die Umkehrung der Kettenregel.', True, 'f(g(x))·g′(x).'), (r'Bei \(u = 3x + 1\) gilt \(dx = 3\,du\).', False, 'du = 3 dx, also dx = du/3.')]),
    merk='∫ f(g(x))·g′(x) dx: u = g(x), du = g′(x) dx, nach u integrieren, zurücksetzen oder Grenzen umrechnen. Kettenregel rückwärts.',
    exam='Integralaufgabe (kam jede Klausur), häufig mit Substitution.',
    fehler=['Grenzen nicht umrechnen.', 'dx falsch ersetzen.'],
    src='Übungsblatt 6 A4, Übungen Analysis I')

# ---------------------------------------------------------------- 4 Partielle Integration
t_part = thema('partielle-integration', 'Partielle Integration', star=True,
    kern="Partielle Integration ist die Umkehrung der Produktregel: ∫ u·v′ dx = u·v − ∫ u′·v dx. Man wählt u so, dass es beim Ableiten einfacher wird (Polynom wie x oder t), und v′ so, dass man es leicht integrieren kann (eˣ, sin, cos). Klausurklassiker: ∫₀² t·e^(2t) dt.",
    kurz=p('Bei \\(\\int x \\cdot e^x\\,dx\\) hilft keine Substitution. Aber: x wird beim Ableiten zu 1, \\(e^x\\) bleibt beim Integrieren \\(e^x\\). Genau das nutzt die <b>partielle Integration</b>.')
        + p('Merkregel: Das <b>Polynom ableiten</b>, die <b>e- oder Winkelfunktion integrieren</b>.'),
    fig=fw('Was ableiten, was integrieren? Tippe auf die Kästen.')
        + bild(svg(360, 180, box(4, 4, 352, 50, '∫ u · v′ dx = u · v − ∫ u′ · v dx', size=15, art='hl', tip='Umkehrung der Produktregel (u·v)′ = u′v + uv′.')
                   + box(4, 66, 172, 110, 'u = t\n(ableiten)\nu′ = 1', size=14, tip='Das Polynom wird beim Ableiten einfacher.') + box(184, 66, 172, 110, 'v′ = e^(2t)\n(integrieren)\nv = ½ e^(2t)', size=14, tip='Die e-Funktion lässt sich leicht integrieren (Faktor 1/2 wegen der 2 im Exponenten).'),
                   'Partielle Integration', maxw=420)),
    figcap='nach der Klausuraufgabe ∫₀² t·e^(2t) dt und Übungsblatt 6, Aufgabe 4 b und d',
    article=h3('Formel')
        + fx('Partielle Integration', r"\int_a^b u \cdot v'\,dx = \big[u \cdot v\big]_a^b - \int_a^b u' \cdot v\,dx", 'Ein Faktor wird abgeleitet (u), der andere integriert (v′). Das neue Integral muss einfacher sein.',
             r"\(\int x e^x\,dx = x e^x - \int e^x\,dx = (x - 1)e^x + C\)")
        + bsp('Klausurstil', r'\(\int_0^2 t \cdot e^{2t}\,dt\)',
              [(r"\(u = t,\ u' = 1\); \(v' = e^{2t},\ v = \frac{1}{2}e^{2t}\)", ''), (r'\(= \left[\frac{t}{2}e^{2t}\right]_0^2 - \int_0^2 \frac{1}{2}e^{2t}\,dt = e^4 - \left[\frac{1}{4}e^{2t}\right]_0^2\)', ''),
               (r'\(= e^4 - \frac{1}{4}e^4 + \frac{1}{4}\)', r'\(\frac{3}{4}e^4 + \frac{1}{4} \approx 41{,}20\)')],
              'Sauber aufschreiben: u, u′, v′, v; dann Formel; Grenzen erst am Ende einsetzen.')
        + bsp('Übungsblatt 6, Aufgabe 4 b', r'\(\int_0^{\pi} x \cos x\,dx\)', [(r"\(u = x,\ v' = \cos x,\ v = \sin x\)", ''), (r'\([x \sin x]_0^{\pi} - \int_0^{\pi} \sin x\,dx = 0 - [-\cos x]_0^{\pi}\)', r'\(-2\)')])
        + klausur_hinweis('„Integral berechnen“ ist eine typische Klausuraufgabe, z. B. ∫₀² t·e^(2t) dt.')
        + falle('Die falsche Wahl: u = eˣ und v′ = x macht das Integral schwerer (x²/2 · eˣ).')
        + wahr('w-part', [('Partielle Integration ist die Umkehrung der Produktregel.', True, '(uv)′ = u′v + uv′.'), (r'Bei \(\int x e^x\,dx\) wählt man \(u = x\).', True, 'Polynom ableiten.'),
                          (r'\(\int_0^2 t e^{2t}\,dt = e^4\)', False, '¾e⁴ + ¼.')]),
    merk="∫ u·v′ = u·v − ∫ u′·v (Produktregel rückwärts). Polynom = u (ableiten), eˣ/sin/cos = v′ (integrieren). ∫₀² t·e^(2t) dt = ¾e⁴ + ¼ ≈ 41,20.",
    exam='Integral mit partieller Integration (Klausuraufgabe).',
    fehler=['u und v′ ungünstig wählen.', 'Vorzeichen beim zweiten Integral.'],
    src='Übungsblatt 6 A4')

KAPITEL = kapitel('k6', 'Integralrechnung',
    'Stammfunktionen, bestimmte Integrale, Substitution und partielle Integration.',
    ['Stammfunktion', 'Hauptsatz', 'Substitution', 'partielle Integration'], [t_stamm, t_best, t_subst, t_part])
