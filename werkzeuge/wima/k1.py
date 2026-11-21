import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *

# ---------------------------------------------------------------- 1 Zahlenmengen und Begriffe
fig_mengen = svg(360, 220,
    tpg('<ellipse cx="180" cy="112" rx="172" ry="104" style="fill:var(--pale);stroke:var(--line)"/>', 'ℝ: reelle Zahlen, also alle Zahlen auf dem Zahlenstrahl, auch √2 und π.')
    + tpg('<ellipse cx="160" cy="120" rx="128" ry="80" style="fill:var(--card);stroke:var(--line)"/>', 'ℚ: rationale Zahlen, alle Brüche p/q mit ganzen p, q und q ≠ 0.')
    + tpg('<ellipse cx="140" cy="128" rx="88" ry="56" style="fill:var(--pale);stroke:var(--line)"/>', 'ℤ: ganze Zahlen …, −2, −1, 0, 1, 2, …')
    + tpg('<ellipse cx="120" cy="134" rx="48" ry="32" style="fill:var(--primary);stroke:var(--line)"/>', 'ℕ: natürliche Zahlen 1, 2, 3, … (in der Vorlesung oft mit 0 als ℕ₀).')
    + T(120, 139, 'ℕ', 15, 800, fill='var(--on-primary)') + T(205, 132, 'ℤ', 15, 800) + T(258, 126, 'ℚ', 15, 800) + T(316, 116, 'ℝ', 15, 800)
    + T(300, 196, '√2, π', 12, 700, fill='var(--muted)') + T(236, 176, '3/4', 12, 700, fill='var(--muted)') + T(168, 166, '−5', 12, 700, fill='var(--muted)'),
    'Zahlenmengen', maxw=420)

t_zahlen = thema('zahlenmengen', 'Zahlenmengen und Standardbezeichnungen',
    kern='Die Zahlenmengen sind ineinander geschachtelt: ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ. In ℝ gelten die Körperaxiome (Rechenregeln für + und ·) und die Anordnungsaxiome (Regeln für <). Wichtig für Ungleichungen: Multipliziert man mit einer negativen Zahl, dreht sich das Ungleichheitszeichen um.',
    kurz=p('In der Wirtschaftsmathematik rechnet man fast immer mit den <b>reellen Zahlen ℝ</b>. Sie enthalten die natürlichen Zahlen (Stückzahlen), die ganzen Zahlen (Gewinne und Verluste), die Brüche (Anteile) und Zahlen wie √2 oder e.')
        + p('Für ℝ gelten feste Spielregeln: die <b>Körperaxiome</b> (wie man addiert und multipliziert) und die <b>Anordnungsaxiome</b> (wie man mit „kleiner als“ umgeht).'),
    fig=fw('Die Zahlenmengen liegen ineinander. Tippe auf die Bereiche.') + bild(fig_mengen),
    figcap='nach der Gliederung „Begriffsbestimmungen, Zahlensysteme“',
    article=h3('Die Zahlenmengen')
        + tabelle(['Zeichen', 'Name', 'Beispiele'], [['ℕ', 'natürliche Zahlen', '1, 2, 3, …'], ['ℤ', 'ganze Zahlen', '−3, 0, 7'], ['ℚ', 'rationale Zahlen (Brüche)', '3/4, −0,5'], ['ℝ', 'reelle Zahlen', '√2, π, e']])
        + p('Weitere Bezeichnungen: ℝ\\{0} (alle reellen Zahlen außer 0), Intervalle wie [a, b] (mit Rändern), (a, b) oder ]a, b[ (ohne Ränder), ∀ (für alle), ∃ (es gibt), ∈ (Element von).')
        + h3('Körper- und Anordnungsaxiome')
        + p('Die Körperaxiome sagen, dass man in ℝ wie gewohnt rechnen darf: Kommutativ-, Assoziativ- und Distributivgesetz, es gibt 0 und 1, zu jeder Zahl die Gegenzahl und zu jeder Zahl außer 0 den Kehrwert.')
        + p('Die Anordnungsaxiome regeln „&lt;“. Die wichtigsten Folgerungen:')
        + liste(['a &lt; b ⇒ a + c &lt; b + c (Addieren ändert nichts)', 'a &lt; b und c &gt; 0 ⇒ a·c &lt; b·c', '<b>a &lt; b und c &lt; 0 ⇒ a·c &gt; b·c</b> (Zeichen dreht sich!)', 'a² ≥ 0 für alle a'])
        + falle('Beim Multiplizieren oder Dividieren mit einer negativen Zahl das Ungleichheitszeichen nicht umdrehen.')
        + wahr('w-zahlen', [('Jede natürliche Zahl ist auch eine reelle Zahl.', True, 'ℕ ⊂ ℝ.'), ('√2 ist eine rationale Zahl.', False, 'Sie lässt sich nicht als Bruch schreiben.'),
                            ('Aus a &lt; b folgt −a &gt; −b.', True, 'Multiplikation mit −1 dreht das Zeichen.')]),
    merk='ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ. Körperaxiome: Rechenregeln für + und ·. Anordnungsaxiome: Regeln für <; bei Multiplikation mit negativer Zahl dreht sich das Zeichen.',
    exam='Grundlage für alle Aufgaben; selbst nicht gefragt.',
    fehler=['Zeichen bei negativer Multiplikation nicht umdrehen.'],
    src='Gliederung 1, Mitschrift')

# ---------------------------------------------------------------- 2 Terme und Brüche
t_terme = thema('terme', 'Terme vereinfachen und Brüche kürzen',
    kern='Terme vereinfacht man mit Distributivgesetz (ausmultiplizieren), Ausklammern und Zusammenfassen gleichartiger Glieder. Brüche kürzt man nur über Faktoren, nicht über Summanden; vorher faktorisiert man (ausklammern, binomische Formeln). Potenzen: aᵐ·aⁿ = aᵐ⁺ⁿ, √x = x^(1/2).',
    kurz=p('Fast jede Aufgabe beginnt oder endet mit dem Vereinfachen eines Terms: eine Ableitung zusammenfassen, einen Grenzwert vorbereiten, einen Bruch kürzen. Die Regeln sind wenige, aber sie müssen sitzen.')
        + p('Die wichtigste Warnung zuerst: <b>Aus Summen kürzen nur die Dummen.</b> \\(\\frac{x+2}{x}\\) ist nicht \\(2\\).'),
    fig=fw('Kürzen: links richtig, rechts falsch. Tippe auf die Kästen.')
        + bild(svg(360, 170,
            box(4, 4, 172, 160, 'richtig\n\n(x²−4)/(x+2)\n= (x+2)(x−2)/(x+2)\n= x − 2', size=13, art='hl', tip='Erst faktorisieren (3. binomische Formel), dann den gemeinsamen Faktor (x+2) kürzen.')
            + box(184, 4, 172, 160, 'falsch\n\n(x+2)/x\n≠ 2\n\n(Summand x\nnicht kürzbar)', size=13, tip='x ist hier ein Summand im Zähler, kein Faktor. Man darf nur Faktoren kürzen.'),
            'Kürzen', maxw=420)),
    figcap='nach Übungsblatt 1, Aufgabe 1',
    article=h3('Ausmultiplizieren und zusammenfassen')
        + bsp('Übungsblatt 1, Aufgabe 1 vii', r'\((4a + 3b - 5c) \cdot 7x - (5a - 4b + 6c) \cdot 3x\)',
              [(r'Ausmultiplizieren: \(28ax + 21bx - 35cx - 15ax + 12bx - 18cx\)', ''), (r'Gleichartige Glieder zusammenfassen', r'\(13ax + 33bx - 53cx\)')],
              'Das Minus vor der zweiten Klammer ändert alle Vorzeichen darin.')
        + h3('Potenzgesetze')
        + tabelle(['Regel', 'Beispiel'], [['aᵐ · aⁿ = aᵐ⁺ⁿ', 'x² · x³ = x⁵'], ['aᵐ : aⁿ = aᵐ⁻ⁿ', 'x⁵ : x² = x³'], ['(aᵐ)ⁿ = aᵐ·ⁿ', '(x²)³ = x⁶'],
                                          ['a⁻ⁿ = 1/aⁿ', 'x⁻² = 1/x²'], ['ⁿ√a = a^(1/n)', '√x = x^(1/2), ∛x² = x^(2/3)']])
        + bsp('Übungsblatt 1, Aufgabe 1 xviii', r'\(x \cdot x \cdot x \cdot \sqrt{x}\)', [(r'\(x^1 \cdot x^1 \cdot x^1 \cdot x^{1/2} = x^{3 + 1/2}\)', r'\(x^{7/2} = x^3\sqrt{x}\)')],
              'Wurzeln als Potenzen schreiben, dann Exponenten addieren. Das braucht man ständig beim Ableiten.')
        + h3('Binomische Formeln')
        + liste(['(a + b)² = a² + 2ab + b²', '(a − b)² = a² − 2ab + b²', '(a + b)(a − b) = a² − b²'])
        + falle('Aus Summen kürzen: \\(\\frac{x + 4}{x} = 4\\) ist falsch. Nur gemeinsame Faktoren dürfen weg.')
        + wahr('w-terme', [(r'\(x^{-3} = \frac{1}{x^3}\)', True, 'Negativer Exponent = Kehrwert.'), (r'\(\sqrt[3]{x^2} = x^{3/2}\)', False, 'Es ist x^(2/3).'),
                           (r'\(\frac{x^2 - 9}{x - 3} = x + 3\) für \(x \ne 3\)', True, '3. binomische Formel.')]),
    merk='Ausmultiplizieren, Vorzeichen bei Minus vor Klammer drehen, gleichartige Glieder zusammenfassen. Potenzgesetze; Wurzeln als Potenzen (ⁿ√a = a^(1/n)). Nur Faktoren kürzen, vorher faktorisieren (binomische Formeln).',
    exam='Vorarbeit in fast jeder Aufgabe (Ableitungen, Grenzwerte).',
    fehler=['Aus Summen kürzen.', 'Wurzel falsch in Potenz umschreiben.'],
    src='Übungsblatt 1, A1')

# ---------------------------------------------------------------- 3 Ungleichungen
def ungl_bild():
    s, X, Y = graph([(lambda x: x * x + 2 * x - 3, -4.2, 2.2, 'var(--primary)', 'x²+2x−3', 'Die Parabel liegt zwischen den Nullstellen −3 und 1 unter der x-Achse: dort ist x² + 2x − 3 < 0.', 1.6)],
                    (-4.5, 2.5), (-4.5, 5.5), ticks_x=(-3, 1), ticks_y=(-4, 4))
    s = tpg(rechteck(X(-3), Y(0) - 6, X(1) - X(-3), 12, 'var(--pos)', 'var(--pos)', 3), 'Lösungsmenge L = (−3, 1): alle x zwischen den Nullstellen.') + s
    return svg(360, 250, s, 'Quadratische Ungleichung', maxw=420)

t_ungl = thema('ungleichungen', 'Ungleichungen lösen',
    kern='Lineare Ungleichungen löst man wie Gleichungen, dreht aber beim Multiplizieren/Dividieren mit einer negativen Zahl das Zeichen um. Quadratische Ungleichungen löst man über die Nullstellen: Bei nach oben offener Parabel ist der Term zwischen den Nullstellen negativ, außerhalb positiv. Bei Bruchungleichungen Fallunterscheidung nach dem Vorzeichen des Nenners.',
    kurz=p('Eine Ungleichung hat meist keine einzelne Lösung, sondern eine <b>Lösungsmenge</b>, oft ein Intervall. Bei \\(x^2 + 2x - 3 < 0\\) sind es alle x zwischen −3 und 1.')
        + p('Der Trick bei quadratischen Ungleichungen: erst die <b>Nullstellen</b> bestimmen, dann schauen, wo die Parabel unter oder über der x-Achse liegt.'),
    fig=fw('Wo liegt die Parabel unter der x-Achse? Tippe auf Kurve und Balken.') + bild(ungl_bild()),
    figcap='nach Übungsblatt 2, Aufgabe 1 iii',
    article=h3('Lineare Ungleichungen')
        + bsp('Übungsblatt 2, Aufgabe 1 i', r'\(x + 5 > 3x - 6\)', [(r'\(-2x > -11\)', ''), (r'durch \(-2\) teilen, Zeichen drehen: \(x < 5{,}5\)', r'\(L = (-\infty;\ 5{,}5)\)')])
        + h3('Quadratische Ungleichungen')
        + fluss([('1. Nullstellen', 'p-q- oder Mitternachtsformel'), ('2. Öffnung', 'nach oben (a > 0) oder unten'), ('3. Ablesen', 'zwischen oder außerhalb der Nullstellen')], hl=2)
        + bsp('Übungsblatt 2, Aufgabe 1 iii', r'\(x^2 + 2x - 3 < 0\)', [(r'Nullstellen: \(x = -1 \pm \sqrt{1 + 3}\)', r'\(x_1 = -3,\ x_2 = 1\)'), (r'Parabel nach oben offen, negativ zwischen den Nullstellen', r'\(L = (-3;\ 1)\)')])
        + bsp('Übungsblatt 2, Aufgabe 1 iv', r'\(x^2 - 4x > 0\)', [(r'\(x(x - 4) > 0\), Nullstellen 0 und 4', ''), (r'positiv außerhalb', r'\(L = (-\infty;\ 0) \cup (4;\ \infty)\)')])
        + h3('Bruchungleichungen')
        + p('Bei \\(\\frac{a}{x - 2} > 1\\) darf man nicht einfach mit \\(x - 2\\) multiplizieren: Ob sich das Zeichen dreht, hängt vom Vorzeichen des Nenners ab. Deshalb zwei Fälle: Nenner positiv (Zeichen bleibt) und Nenner negativ (Zeichen dreht sich).')
        + falle('Mit einem Term wie \\((x - 2)\\) multiplizieren, ohne den Fall „Nenner negativ“ zu betrachten.')
        + wahr('w-ungl', [(r'Die Lösung von \(x^2 - 4 < 0\) ist \((-2;\ 2)\).', True, 'Zwischen den Nullstellen.'), (r'Aus \(-3x < 6\) folgt \(x < -2\).', False, 'Zeichen drehen: x > −2.')]),
    merk='Linear: wie Gleichung, Zeichen drehen bei negativem Faktor. Quadratisch: Nullstellen, Öffnung, ablesen (nach oben offen: negativ zwischen den Nullstellen). Bruch: Fallunterscheidung nach dem Vorzeichen des Nenners.',
    exam='Hilfsmittel für Definitionsbereiche (z. B. ln(4 − x²) braucht 4 − x² > 0).',
    fehler=['Zeichen nicht drehen.', 'Bei Bruchungleichungen keine Fallunterscheidung.'],
    src='Übungsblatt 2, A1')

KAPITEL = kapitel('k1', 'Grundlagen: Zahlen, Terme, Ungleichungen',
    'Das Handwerkszeug für alles Weitere: Zahlenmengen, Terme umformen, Ungleichungen lösen.',
    ['Zahlenmengen', 'Terme', 'Ungleichungen'], [t_zahlen, t_terme, t_ungl])
