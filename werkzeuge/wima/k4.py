import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *
import sympy as sp

x, t, h = sp.symbols('x t h', real=True)
gleich = lambda a, b: sp.simplify(a - b) == 0
# Ableitungen der Beispiele prüfen
assert gleich(sp.diff(sp.cos(x) * sp.exp(x**2 + 4), x), -sp.sin(x) * sp.exp(x**2 + 4) + 2 * x * sp.cos(x) * sp.exp(x**2 + 4))
assert gleich(sp.diff(sp.cos(sp.sin(x)**2), x), -sp.sin(sp.sin(x)**2) * 2 * sp.sin(x) * sp.cos(x))
assert gleich(sp.diff((5 * t + 3)**3, t), 15 * (5 * t + 3)**2)
assert gleich(sp.diff(sp.cbrt(2 * x) / (x + 2), x), ((sp.Rational(2, 3) * (2 * x)**sp.Rational(-2, 3)) * (x + 2) - sp.cbrt(2 * x)) / (x + 2)**2)
assert gleich(sp.diff(sp.exp(2 * x**2) / sp.cos(x), x), (4 * x * sp.exp(2 * x**2) * sp.cos(x) + sp.exp(2 * x**2) * sp.sin(x)) / sp.cos(x)**2)
assert gleich(sp.diff(x**2 * sp.sqrt(x), x), sp.Rational(5, 2) * x**sp.Rational(3, 2))
assert sp.limit(((x + h)**2 - x**2) / h, h, 0) == 2 * x
assert sp.limit(sp.log(x) / (x - 1), x, 1) == 1 and sp.limit(x**4 / sp.exp(x), x, sp.oo) == 0
assert sp.expand((x - 5) * (x**2 - 7 * x - 30)) == x**3 - 12 * x**2 + 5 * x + 150
fk = sp.Rational(1, 2) * x**4 - sp.Rational(1, 6) * x**3 - x**2
krit = sorted(float(r) for r in sp.solve(sp.diff(fk, x), x))
assert abs(krit[0] + 0.8828) < 1e-3 and krit[1] == 0 and abs(krit[2] - 1.1328) < 1e-3

# ---------------------------------------------------------------- 1 Differentialquotient
def dq_bild():
    f = lambda v: 0.3 * v * v + 0.5
    x0, x1 = 2, 4
    s, X, Y = graph([(f, 0, 5, 'var(--primary)', 'f', 'f(x) = 0,3x² + 0,5', 4.6)], (-0.3, 5.3), (-0.2, 8.5), ticks_x=(2, 4), ticks_y=())
    m_s = (f(x1) - f(x0)) / (x1 - x0); m_t = 0.6 * x0
    s += tpg(linie([(X(0.6), Y(f(x0) + m_s * (0.6 - x0))), (X(5), Y(f(x0) + m_s * (5 - x0)))], 'var(--c3)', 2), f'Sekante durch (2|f(2)) und (4|f(4)): Steigung = Differenzenquotient = {m_s:.1f}'.replace('.', ','))
    s += tpg(linie([(X(0.3), Y(f(x0) + m_t * (0.3 - x0))), (X(4.6), Y(f(x0) + m_t * (4.6 - x0)))], 'var(--c2)', 2.4), f'Tangente in x₀ = 2: Steigung = Grenzwert des Differenzenquotienten für h → 0 = f′(2) = {m_t:.1f}'.replace('.', ','))
    s += punkt(X(x0), Y(f(x0)), 'var(--primary)', 5) + punkt(X(x1), Y(f(x1)), 'var(--c3)', 5)
    s += T(X(4.4), Y(7.4), 'Sekante', 12, 800, 'end', 'var(--c3)') + T(X(4.6), Y(3.2), 'Tangente', 12, 800, 'end', 'var(--c2)')
    return svg(360, 250, s, 'Sekante und Tangente', maxw=420)

t_dq = thema('differentialquotient', 'Der Differentialquotient: Steigung in einem Punkt',
    kern='Die Ableitung f′(x₀) ist der Grenzwert des Differenzenquotienten: f′(x₀) = lim(h→0) [f(x₀ + h) − f(x₀)]/h. Geometrisch ist das die Steigung der Tangente in x₀, ökonomisch die Grenzrate (z. B. Grenzkosten: Kosten der nächsten Einheit). Existiert der Grenzwert, heißt f in x₀ differenzierbar.',
    kurz=p('Wie stark steigen die Kosten, wenn man ein Stück mehr produziert? Die Antwort ist die <b>Steigung</b> der Kostenkurve an dieser Stelle. Zwischen zwei Punkten misst man sie mit einer <b>Sekante</b>, an einem Punkt mit der <b>Tangente</b>.')
        + p('Lässt man den zweiten Punkt immer näher an den ersten rücken (h → 0), wird aus der Sekante die Tangente. Dieser Grenzwert ist die <b>Ableitung</b>.'),
    fig=fw('Aus der Sekante wird die Tangente. Tippe auf die Linien.') + bild(dq_bild()),
    figcap='nach Übungsblatt 5, Aufgabe 1',
    article=h3('Definition')
        + fx('Differentialquotient', r"f'(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}", 'Steigung der Sekante zwischen x₀ und x₀ + h, und dann h gegen null.',
             r"\(f(x) = x^2\): \(\frac{(x+h)^2 - x^2}{h} = \frac{2xh + h^2}{h} = 2x + h \to 2x\)")
        + bsp('Übungsblatt 5, Aufgabe 1 ii', r'\(f(x) = \frac{1}{x}\), \(x \ne 0\)',
              [(r'\(\frac{\frac{1}{x+h} - \frac{1}{x}}{h} = \frac{x - (x+h)}{h \cdot x(x+h)} = \frac{-1}{x(x+h)}\)', ''), (r'\(h \to 0\)', r"\(f'(x) = -\frac{1}{x^2}\)")],
              'Erst auf einen Bruchstrich bringen, h kürzen, dann h = 0 setzen.')
        + h3('Ökonomische Bedeutung')
        + p('Die Ableitung einer ökonomischen Funktion heißt <b>Grenzfunktion</b>: K′(x) sind die <b>Grenzkosten</b> (ungefähr die Kosten der nächsten Mengeneinheit), U′(x) der Grenzumsatz, G′(x) der Grenzgewinn.')
        + wahr('w-dq', [('Die Ableitung ist die Steigung der Tangente.', True, 'Grenzwert der Sekantensteigungen.'), ('Der Differenzenquotient ist schon die Ableitung.', False, 'Erst sein Grenzwert für h → 0.')]),
    merk="f′(x₀) = lim(h→0) [f(x₀+h) − f(x₀)]/h: Tangentensteigung. Ökonomisch Grenzfunktion (Grenzkosten K′, Grenzumsatz U′, Grenzgewinn G′).",
    exam='Grundverständnis; die Klausur verlangt Ableitungen über Regeln.',
    fehler=['h zu früh null setzen (dann 0/0).'],
    src='Übungsblatt 5, A1')

# ---------------------------------------------------------------- 2 Grundregeln
t_regeln = thema('ableitungsregeln', 'Grundregeln: Potenz-, Faktor-, Summenregel und Standardableitungen',
    kern='Potenzregel (xⁿ)′ = n·xⁿ⁻¹ (auch für Brüche und negative n, also auch für Wurzeln), Faktorregel (c·f)′ = c·f′, Summenregel (f + g)′ = f′ + g′. Standardableitungen: (eˣ)′ = eˣ, (ln x)′ = 1/x, (sin x)′ = cos x, (cos x)′ = −sin x. Wurzeln vor dem Ableiten als Potenz schreiben.',
    kurz=p('Mit vier Regeln und einer kleinen Tabelle leitet man alle Grundfunktionen ab. Der wichtigste Trick: <b>Wurzeln und Brüche als Potenzen schreiben</b>. \\(\\sqrt{x} = x^{1/2}\\), \\(\\frac{1}{x^2} = x^{-2}\\).')
        + p('Dann gilt immer die Potenzregel: Exponent nach vorn, Exponent minus 1.'),
    fig=fw('Die Standardableitungen. Tippe auf die Kästen.')
        + bild(svg(360, 200, ''.join(box(4 + (i % 3) * 120, 4 + (i // 3) * 98, 112, 90, t_, size=13, art='hl' if i == 0 else 'card', tip=tip) for i, (t_, tip) in enumerate([
            ('xⁿ → n·xⁿ⁻¹', 'Potenzregel, gilt für alle reellen n: x⁵ → 5x⁴, √x = x^(1/2) → ½x^(−1/2), 1/x = x⁻¹ → −x⁻².'),
            ('eˣ → eˣ', 'Die e-Funktion ist ihre eigene Ableitung.'), ('ln x → 1/x', 'Für x > 0.'),
            ('sin x → cos x', 'Sinus abgeleitet ist Kosinus.'), ('cos x → −sin x', 'Achtung Minus.'), ('c → 0', 'Konstanten fallen weg (Fixkosten!).')])), 'Standardableitungen', maxw=420)),
    figcap='nach Gliederung 4: Ableitungsregeln',
    article=h3('Die Regeln')
        + tabelle(['Regel', 'Formel', 'Beispiel'], [['Potenzregel', "(xⁿ)′ = n·xⁿ⁻¹", "(x⁴)′ = 4x³"], ['Faktorregel', "(c·f)′ = c·f′", "(5x²)′ = 10x"],
                                                   ['Summenregel', "(f + g)′ = f′ + g′", "(x³ + eˣ)′ = 3x² + eˣ"], ['Konstante', "c′ = 0", "(375)′ = 0"]])
        + bsp('Übungsblatt 5, Aufgabe 2 viii', r'\(f(x) = x^2 \cdot \sqrt{x}\)', [(r'Als Potenz: \(x^2 \cdot x^{1/2} = x^{5/2}\)', ''), (r'Potenzregel', r"\(f'(x) = \frac{5}{2} x^{3/2} = \frac{5}{2} x\sqrt{x}\)")],
              'Erst vereinfachen, dann ableiten: spart die Produktregel.')
        + bsp('Kostenfunktion', r'\(K(x) = x^3 - 15x^2 + 125x + 375\)', [(r'Summand für Summand', r"\(K'(x) = 3x^2 - 30x + 125\)")], 'Die Fixkosten 375 fallen beim Ableiten weg: Grenzkosten hängen nicht von den Fixkosten ab.')
        + h3('Höhere Ableitungen')
        + p('Leitet man f′ noch einmal ab, erhält man f″ (2. Ableitung, Krümmung), dann f‴ usw. Bei \\(K(x)\\) oben: \\(K\'\'(x) = 6x - 30\\).')
        + wahr('w-regeln', [(r"\((\sqrt{x})' = \frac{1}{2\sqrt{x}}\)", True, 'x^(1/2) → ½x^(−1/2).'), (r"\((\cos x)' = \sin x\)", False, 'Es ist −sin x.'), ('Fixkosten fallen beim Ableiten weg.', True, 'Konstante → 0.')])
        + p(r"""<b>Höhere Ableitungen:</b> Ist \(f'\) wieder differenzierbar, heißt \(f'' = (f')'\) zweite Ableitung; mit vollständiger Induktion verallgemeinert man das auf Ableitungen k-ter Ordnung \(f^{(k)}\). Beispiel: \(f(x) = x^3\): \(f' = 3x^2\), \(f'' = 6x\), \(f''' = 6\), \(f^{(4)} = 0\)."""),
    merk="(xⁿ)′ = n·xⁿ⁻¹, (c·f)′ = c·f′, (f+g)′ = f′+g′, c′ = 0; (eˣ)′ = eˣ, (ln x)′ = 1/x, (sin x)′ = cos x, (cos x)′ = −sin x. Wurzeln/Brüche erst als Potenz schreiben.",
    exam='Teil jeder Ableitungsaufgabe.',
    fehler=['Vorzeichen bei (cos x)′ vergessen.', 'Wurzel nicht als Potenz umschreiben.'],
    src='Übungsblatt 5, A2')

# ---------------------------------------------------------------- 3 Produkt- und Quotientenregel
t_pq = thema('produkt-quotient', 'Produkt- und Quotientenregel', star=True,
    kern="Produktregel: (u·v)′ = u′·v + u·v′. Quotientenregel: (u/v)′ = (u′·v − u·v′)/v². Man schreibt u, v, u′, v′ getrennt auf und setzt dann ein. In Klausuren kommen sie mit e-Funktion, Wurzel, ln und Winkelfunktionen und oft zusammen mit der Kettenregel.",
    kurz=p('Steht ein Produkt wie \\(\\cos(x) \\cdot e^{x^2+4}\\) da, darf man nicht einfach beide Faktoren getrennt ableiten. Man braucht die <b>Produktregel</b>. Bei einem Bruch die <b>Quotientenregel</b>.')
        + p('Merkhilfe für den Quotienten: „<b>NAZ minus ZAN durch N²</b>“: Nenner mal Ableitung Zähler minus Zähler mal Ableitung Nenner, durch Nenner zum Quadrat.'),
    fig=fw('Die Formeln als Schema. Tippe auf die Kästen.')
        + tafeln('tf-pq', ['Produkt', 'Quotient'], [
            svg(360, 150, box(4, 4, 352, 50, "(u · v)′ = u′ · v + u · v′", size=15, art='hl', tip='Erst den ersten Faktor ableiten und den zweiten stehen lassen, dann umgekehrt, und addieren.')
                + box(4, 66, 172, 80, 'u = cos x\nu′ = −sin x', size=13, tip='Erster Faktor und seine Ableitung.') + box(184, 66, 172, 80, 'v = e^(x²+4)\nv′ = 2x · e^(x²+4)', size=13, tip='Zweiter Faktor; seine Ableitung braucht die Kettenregel.'), 'Produktregel', maxw=420),
            svg(360, 150, box(4, 4, 352, 50, "(u / v)′ = (u′ · v − u · v′) / v²", size=15, art='hl', tip='„NAZ minus ZAN durch N²“. Reihenfolge im Zähler beachten: Minus!')
                + box(4, 66, 172, 80, 'u = ∛(2x)\nu′ = ⅔ · (2x)^(−2/3)', size=13, tip='Zähler: (2x)^(1/3), Kettenregel mit innerer Ableitung 2.') + box(184, 66, 172, 80, 'v = x + 2\nv′ = 1', size=13, tip='Nenner und seine Ableitung.'), 'Quotientenregel', maxw=420)]),
    figcap='nach Übungsblatt 5, Aufgabe 2 und den Klausuraufgaben zu Ableitungen',
    article=h3('Produktregel')
        + fx('Produktregel', r"(u \cdot v)' = u' \cdot v + u \cdot v'", 'Ableitung des ersten mal zweiter plus erster mal Ableitung des zweiten.', r"\((x^2 e^x)' = 2x e^x + x^2 e^x\)")
        + bsp('Klausurstil', r'\(f(x) = \cos(x) \cdot e^{x^2 + 4}\)',
              [(r"\(u = \cos x,\ u' = -\sin x\); \(v = e^{x^2+4},\ v' = 2x \cdot e^{x^2+4}\) (Kettenregel)", ''),
               (r"\(f'(x) = -\sin(x) \cdot e^{x^2+4} + \cos(x) \cdot 2x \cdot e^{x^2+4}\)", r"\(f'(x) = e^{x^2+4}\,(2x\cos x - \sin x)\)")],
              'Am Ende den gemeinsamen Faktor ausklammern.')
        + h3('Quotientenregel')
        + fx('Quotientenregel', r"\left(\frac{u}{v}\right)' = \frac{u' \cdot v - u \cdot v'}{v^2}", 'NAZ minus ZAN durch N².', r"\(\left(\frac{x}{x+1}\right)' = \frac{1 \cdot (x+1) - x \cdot 1}{(x+1)^2} = \frac{1}{(x+1)^2}\)")
        + bsp('Klausurstil', r'\(f(x) = \frac{\sqrt[3]{2x}}{x + 2}\)',
              [(r"\(u = (2x)^{1/3},\ u' = \frac{1}{3}(2x)^{-2/3} \cdot 2 = \frac{2}{3\sqrt[3]{(2x)^2}}\)", ''), (r"\(v = x + 2,\ v' = 1\)", ''),
               (r"\(f'(x) = \frac{\frac{2}{3\sqrt[3]{(2x)^2}} \cdot (x + 2) - \sqrt[3]{2x}}{(x + 2)^2}\)", '')],
              'Vereinfachen ist erlaubt, aber nicht nötig: Die Punkte gibt es für die richtige Anwendung der Regeln.')
        + bsp('Übungsblatt 5, Aufgabe 2 i', r'\(f(x) = \frac{e^{2x^2}}{\cos x}\)',
              [(r"\(u' = 4x e^{2x^2}\), \(v' = -\sin x\)", ''), (r"\(f'(x) = \frac{4x e^{2x^2} \cos x + e^{2x^2} \sin x}{\cos^2 x}\)", '')])
        + falle('Im Zähler der Quotientenregel die Reihenfolge vertauschen: u·v′ − u′·v ergibt das falsche Vorzeichen.')
        + klausur_hinweis('Typisch sind zwei Ableitungen, eine mit Produkt- und eine mit Quotientenregel, beide mit Kettenregel kombiniert.')
        + wahr('w-pq', [(r"\((x \cdot e^x)' = e^x + x e^x\)", True, 'Produktregel.'), (r"\(\left(\frac{1}{x}\right)' = \frac{1}{x^2}\)", False, 'Es ist −1/x².'),
                        ('Bei der Quotientenregel steht im Nenner v².', True, 'Nenner zum Quadrat.')]),
    merk="Produkt: (u·v)′ = u′v + uv′. Quotient: (u/v)′ = (u′v − uv′)/v² („NAZ − ZAN durch N²“). u, v, u′, v′ getrennt aufschreiben, dann einsetzen.",
    exam='Ableitungen mit Produkt- und Quotientenregel (oft mit Wurzel, ln, e und Kettenregel).',
    fehler=['Faktoren einzeln ableiten und multiplizieren.', 'Vorzeichen im Quotientenzähler.'],
    src='Übungsblatt 5 A2, Klausuraufgaben')

# ---------------------------------------------------------------- 4 Kettenregel
t_kette = thema('kettenregel', 'Kettenregel (auch doppelt verkettet)', star=True,
    kern="Kettenregel: (f(g(x)))′ = f′(g(x))·g′(x), „äußere Ableitung mal innere Ableitung“. Bei mehrfacher Verkettung multipliziert man alle inneren Ableitungen nacheinander, z. B. (cos(sin² x))′ = −sin(sin² x)·2 sin x·cos x.",
    kurz=p('\\((5t + 3)^3\\) könnte man ausmultiplizieren. Schneller: Äußere Funktion \\(u^3\\) ableiten (\\(3u^2\\)), innere \\(5t + 3\\) ableiten (5), multiplizieren: \\(15(5t + 3)^2\\).')
        + p('Das ist die <b>Kettenregel</b>: <b>äußere Ableitung mal innere Ableitung</b>. In einer Klausur kam sogar eine doppelte Verkettung: \\(\\cos(\\sin^2 x)\\).'),
    fig=fw('Von außen nach innen ableiten. Tippe auf die Schalen.')
        + bild(svg(360, 210,
            box(4, 4, 352, 58, 'außen: cos(□)   →   −sin(□)', size=14, art='hl', tip='Äußerste Funktion ableiten, das Innere unverändert lassen: −sin(sin²x).')
            + box(40, 74, 280, 58, 'Mitte: (□)²   →   2·(□)', size=14, tip='Die mittlere Funktion ist das Quadrat: Ableitung 2·sin x.')
            + box(76, 144, 208, 58, 'innen: sin x  →  cos x', size=14, tip='Innerste Funktion ableiten: cos x. Alles miteinander multiplizieren.'),
            'Doppelte Kettenregel', maxw=420)),
    figcap='nach der Klausuraufgabe f(x) = cos(sin²(x))',
    article=h3('Die Regel')
        + fx('Kettenregel', r"\big(f(g(x))\big)' = f'(g(x)) \cdot g'(x)", 'Äußere Ableitung (mit dem Inneren unverändert drin) mal innere Ableitung.', r"\((e^{3x})' = e^{3x} \cdot 3\)")
        + bsp('Übungsblatt 5, Aufgabe 2 iii', r'\(h(t) = (5t + 3)^3\)', [(r"außen \(u^3 \to 3u^2\), innen \(5t + 3 \to 5\)", r"\(h'(t) = 15(5t + 3)^2\)")])
        + bsp('Klausurstil: doppelt verkettet', r'\(f(x) = \cos(\sin^2 x) = \cos\big((\sin x)^2\big)\)',
              [(r'außen: \(\cos(\square) \to -\sin(\square)\)', r'\(-\sin(\sin^2 x)\)'), (r'Mitte: \((\square)^2 \to 2\square\)', r'\(2\sin x\)'), (r'innen: \(\sin x \to \cos x\)', r'\(\cos x\)'),
               (r'multiplizieren', r"\(f'(x) = -\sin(\sin^2 x) \cdot 2\sin x \cos x\)")],
              'Schicht für Schicht von außen nach innen; jede Schicht liefert einen Faktor.')
        + bsp('Wurzel', r'\(f(x) = \sqrt[4]{x^2 + 3x} = (x^2 + 3x)^{1/4}\)', [(r"\(f'(x) = \frac{1}{4}(x^2 + 3x)^{-3/4} \cdot (2x + 3)\)", r"\(\frac{2x + 3}{4\sqrt[4]{(x^2 + 3x)^3}}\)")])
        + falle('Die innere Ableitung vergessen, z. B. (e^(x²))′ = e^(x²) statt 2x·e^(x²).')
        + wahr('w-kette', [(r"\((e^{x^2})' = 2x e^{x^2}\)", True, 'Innere Ableitung 2x.'), (r"\((\ln(3x))' = \frac{1}{3x}\)", False, 'Mal 3: 1/x.'),
                           (r"\((\sin(4x+1))' = 4\cos(4x+1)\)", True, 'Innere Ableitung 4.')]),
    merk="Kettenregel: äußere Ableitung (Inneres unverändert) mal innere Ableitung. Mehrfach: Schicht für Schicht, alle inneren Ableitungen multiplizieren. Wurzeln als Potenz schreiben.",
    exam='In jeder Ableitungsaufgabe, auch doppelt verkettet (cos(sin²x)).',
    fehler=['Innere Ableitung vergessen.', 'Bei Mehrfachverkettung eine Schicht auslassen.'],
    src='Übungsblatt 5 A2, Klausuraufgaben')

# ---------------------------------------------------------------- 5 L'Hospital und Polynomdivision
t_hosp = thema('lhospital', "Regel von L'Hospital und Polynomdivision",
    kern="Bei Grenzwerten der Form 0/0 oder ∞/∞ darf man Zähler und Nenner getrennt ableiten: lim f/g = lim f′/g′ (Regel von L’Hospital), notfalls mehrmals. Polynomdivision teilt ein Polynom durch (x − a), wenn a eine Nullstelle ist, und vereinfacht so Brüche und Nullstellensuche.",
    kurz=p('\\(\\lim_{x \\to 1} \\frac{\\ln x}{x - 1}\\): Einsetzen ergibt \\(\\frac{0}{0}\\). Kürzen geht nicht. <b>L’Hospital</b> hilft: Zähler und Nenner einzeln ableiten, \\(\\frac{1/x}{1} \\to 1\\).')
        + p('Und bei \\(\\frac{x^3 - 12x^2 + 5x + 150}{x - 5}\\) hilft die <b>Polynomdivision</b>: Das Ergebnis ist \\(x^2 - 7x - 30\\).'),
    fig=fw('Wann darf man L’Hospital anwenden? Tippe auf die Kästen.')
        + bild(svg(360, 170, box(4, 4, 172, 160, 'erlaubt\n\n„0/0“\nln x/(x−1), x→1\n\n„∞/∞“\nx⁴/eˣ, x→∞', size=13, art='hl', tip='Nur bei unbestimmten Ausdrücken 0/0 oder ∞/∞.')
                       + box(184, 4, 172, 160, 'nicht erlaubt\n\n„2/0“ oder „3/5“\n\nerst einsetzen\nund prüfen!', size=13, tip='Ist der Ausdruck nicht unbestimmt, liefert L’Hospital falsche Ergebnisse.'), "L'Hospital", maxw=420)),
    figcap="nach Übungsblatt 6, Aufgabe 2 und Übungsblatt 5, Aufgabe 3",
    article=h3("Regel von L'Hospital")
        + fx("L'Hospital", r"\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}", 'Nur bei 0/0 oder ∞/∞: Zähler und Nenner getrennt ableiten (keine Quotientenregel!).', r"\(\lim_{x\to1}\frac{\ln x}{x-1} = \lim_{x\to1}\frac{1/x}{1} = 1\)")
        + bsp('Übungsblatt 6, Aufgabe 2 b', r'\(\lim_{x \to \infty} \frac{x^4}{e^x}\)', [('∞/∞, viermal ableiten', r'\(\frac{24}{e^x} \to 0\)')], 'Die e-Funktion wächst schneller als jede Potenz.')
        + bsp('Übungsblatt 6, Aufgabe 2 c', r'\(\lim_{x \to \infty} \frac{\ln x}{x^2}\)', [(r'∞/∞: \(\frac{1/x}{2x} = \frac{1}{2x^2}\)', r'\(\to 0\)')])
        + h3('Polynomdivision')
        + bsp('Übungsblatt 5, Aufgabe 3 i', r'\((x^3 - 12x^2 + 5x + 150) : (x - 5)\)',
              [(r'\(x^3 : x = x^2\); \(x^2(x - 5) = x^3 - 5x^2\) abziehen → \(-7x^2 + 5x\)', ''), (r'\(-7x^2 : x = -7x\); abziehen → \(-30x + 150\)', ''), (r'\(-30x : x = -30\); Rest 0', r'\(x^2 - 7x - 30\)')],
              'Rest 0 heißt: x = 5 ist Nullstelle. Probe durch Ausmultiplizieren.')
        + falle('Bei L’Hospital die Quotientenregel anwenden. Zähler und Nenner werden getrennt abgeleitet.')
        + wahr('w-hosp', [("L'Hospital darf man bei jedem Bruch anwenden.", False, 'Nur bei 0/0 oder ∞/∞.'), (r'\(\lim_{x\to\infty} \frac{x^{10}}{e^x} = 0\)', True, 'e wächst schneller.')]),
    merk="L’Hospital: bei 0/0 oder ∞/∞ lim f/g = lim f′/g′ (getrennt ableiten, ggf. wiederholen). eˣ wächst schneller als jede Potenz, ln langsamer. Polynomdivision durch (x − a), Rest 0 ⇔ a ist Nullstelle.",
    exam='Hilfsmittel für Grenzwerte (Aufgabe 1).',
    fehler=['Quotientenregel statt getrenntem Ableiten.', 'Ohne Prüfen auf 0/0 anwenden.'],
    src='Übungsblatt 5 A3, Übungsblatt 6 A2')

# ---------------------------------------------------------------- 6 Extrema und Kurvendiskussion
def kd_bild():
    f = lambda v: 0.5 * v**4 - v**3 / 6 - v * v
    s, X, Y = graph([(f, -1.75, 2.05, 'var(--primary)', 'f', 'f(x) = ½x⁴ − ⅙x³ − x²', 1.9)], (-1.9, 2.2), (-1.8, 1.6), ticks_x=(-1, 1, 2), ticks_y=(-1, 1))
    for xv, typ in [(krit[0], 'Tiefpunkt'), (0, 'Hochpunkt'), (krit[2], 'Tiefpunkt')]:
        s += tpg(punkt(X(xv), Y(f(xv)), 'var(--c2)' if typ == 'Hochpunkt' else 'var(--c3)', 6), f"{typ} bei x ≈ {xv:.3f}: f′(x) = 0 und f″(x) {'< 0' if typ == 'Hochpunkt' else '> 0'}".replace('.', ','))
    return svg(360, 250, s, 'Kurvendiskussion', maxw=420)

t_kd = thema('kurvendiskussion', 'Extremwerte, Wendepunkte, Kurvendiskussion',
    kern="Notwendige Bedingung für ein Extremum: f′(x₀) = 0. Hinreichend: f″(x₀) < 0 → Hochpunkt (Maximum), f″(x₀) > 0 → Tiefpunkt (Minimum). Wendepunkt: f″(x₀) = 0 und f‴(x₀) ≠ 0. Eine Kurvendiskussion umfasst Definitionsbereich, Symmetrie, Nullstellen, Extrema, Wendepunkte, Verhalten an den Rändern bzw. Polstellen.",
    kurz=p('Wo ist der Gewinn am größten, wo sind die Stückkosten am kleinsten? Das sind <b>Extremwerte</b>. An einem Hoch- oder Tiefpunkt ist die Tangente waagerecht: \\(f\'(x) = 0\\).')
        + p('Ob es ein Maximum oder Minimum ist, sagt die zweite Ableitung: \\(f\'\'(x) < 0\\) heißt „Kurve nach unten gekrümmt“, also <b>Maximum</b>.'),
    fig=fw('Zwei Tiefpunkte und ein Hochpunkt. Tippe auf die Punkte.') + bild(kd_bild()),
    figcap='nach Übungsblatt 6, Aufgabe 1 ii',
    article=h3('Bedingungen')
        + tabelle(['Was', 'notwendig', 'hinreichend'], [['Hochpunkt (Maximum)', "f′(x₀) = 0", "f″(x₀) < 0"], ['Tiefpunkt (Minimum)', "f′(x₀) = 0", "f″(x₀) > 0"], ['Wendepunkt', "f″(x₀) = 0", "f‴(x₀) ≠ 0"]])
        + bsp('Übungsblatt 6, Aufgabe 1 ii', r'\(f(x) = \frac{1}{2}x^4 - \frac{1}{6}x^3 - x^2\)',
              [(r"\(f'(x) = 2x^3 - \frac{1}{2}x^2 - 2x = x\,(2x^2 - \frac{1}{2}x - 2)\)", ''),
               (r"\(f'(x) = 0\): \(x_1 = 0\) und \(x_{2,3} = \frac{\frac12 \pm \sqrt{\frac14 + 16}}{4}\)", r'\(x_2 \approx 1{,}133;\ x_3 \approx -0{,}883\)'),
               (r"\(f''(x) = 6x^2 - x - 2\): \(f''(0) = -2 < 0\)", 'Hochpunkt bei x = 0'), (r"\(f''(1{,}133) > 0,\ f''(-0{,}883) > 0\)", 'zwei Tiefpunkte')])
        + h3('Ablauf einer Kurvendiskussion')
        + fluss([('Definitionsbereich', 'Polstellen?'), ('Nullstellen', 'f(x) = 0'), ('Extrema', "f′ = 0, f″"), ('Wendepunkte', "f″ = 0"), ('Ränder', 'x → ±∞, Pole')], hl=2)
        + p('Bei gebrochenrationalen Funktionen wie \\(f(x) = \\frac{x^2 - 1}{x^2 + x - 2}\\) (Übungsblatt 6, Aufgabe 1 i) zuerst faktorisieren: \\(\\frac{(x-1)(x+1)}{(x-1)(x+2)}\\). An x = 1 liegt eine Lücke, an x = −2 ein Pol.')
        + wahr('w-kd', [("f′(x₀) = 0 reicht für ein Extremum.", False, 'Nur notwendig; f″ prüfen.'), ("f″(x₀) < 0 bei f′(x₀) = 0 heißt Hochpunkt.", True, 'Rechtskrümmung.')]),
    merk="Extremum: f′ = 0 (notwendig), f″ < 0 → Maximum, f″ > 0 → Minimum. Wendepunkt: f″ = 0, f‴ ≠ 0. Kurvendiskussion: D, Nullstellen, Extrema, Wendepunkte, Ränder/Pole.",
    exam='Grundlage für Gewinnmaximum und Betriebsoptimum (Oberthema 5).',
    fehler=['Nur f′ = 0 prüfen.', 'f″ < 0 und > 0 verwechseln.'],
    src='Übungsblatt 6, A1')

KAPITEL = kapitel('k4', 'Differentialrechnung',
    'Von der Tangentensteigung zu den Ableitungsregeln, Grenzwerten mit L’Hospital und Extremwerten.',
    ['Differentialquotient', 'Grundregeln', 'Produkt, Quotient', 'Kettenregel', "L'Hospital", 'Extrema'],
    [t_dq, t_regeln, t_pq, t_kette, t_hosp, t_kd])
