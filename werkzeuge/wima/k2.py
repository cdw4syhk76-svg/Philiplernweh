import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *

K0, Q = 50000, 1.05
K10 = K0 * Q ** 10
assert abs(K10 - 81444.73) < 0.01


def folgen_bild():
    pts_g = [(n, K0 * Q ** n / 1000) for n in range(11)]
    pts_a = [(n, (50000 - 4800 * n) / 1000) for n in range(11)]
    s, X, Y = graph([], (0, 10.5), (0, 90), xl='n (Jahre)', yl='Tsd. €', ticks_x=(2, 4, 6, 8, 10), ticks_y=(20, 50, 80))
    for n, v in pts_g:
        s += tpg(punkt(X(n), Y(v), 'var(--c2)', 4.5), f'Geometrische Folge (Zinseszins): nach {n} Jahren {v * 1000:,.2f} €'.replace(',', 'X').replace('.', ',').replace('X', '.'))
    for n, v in pts_a:
        s += tpg(punkt(X(n), Y(v), 'var(--c3)', 4.5), f'Arithmetische Folge (lineare Abschreibung): Restwert nach {n} Jahren {int(v * 1000):,} €'.replace(',', '.'))
    s += T(X(1), Y(78), 'Zinseszins', 12, 800, 'start', 'var(--c2)') + T(X(1), Y(8), 'lineare Abschreibung', 12, 800, 'start', 'var(--c3)')
    return svg(360, 250, s, 'Arithmetische und geometrische Folge', maxw=420)


t_folgen = thema('folgen', 'Folgen: arithmetisch, geometrisch, beschränkt, monoton',
    kern='Eine Folge ordnet jeder natürlichen Zahl n ein Glied aₙ zu. Arithmetische Folgen haben konstante Differenz d (aₙ = a₀ + n·d, z. B. lineare Abschreibung), geometrische Folgen konstanten Quotienten q (aₙ = a₀·qⁿ, z. B. Zinseszins). Eine Folge ist beschränkt, wenn alle Glieder in einem Band |aₙ| ≤ M liegen, monoton wachsend, wenn aₙ₊₁ ≥ aₙ.',
    kurz=p('50.000 € liegen zu 5 % Zinsen auf dem Konto. Nach einem Jahr sind es 52.500 €, nach zwei Jahren 55.125 €, … Jedes Jahr wird mit 1,05 multipliziert: eine <b>geometrische Folge</b>.')
        + p('Eine Maschine für 50.000 € wird in 10 Jahren auf 2.000 € abgeschrieben, jedes Jahr um den gleichen Betrag. Jedes Jahr wird 4.800 € abgezogen: eine <b>arithmetische Folge</b>.'),
    fig=fw('Zwei Folgen im Vergleich. Tippe auf die Punkte.') + bild(folgen_bild()),
    figcap='nach Übungsblatt 1, Aufgaben 3 und 4',
    article=h3('Was ist eine Folge?')
        + p('Eine <b>Folge</b> \\((a_n)_{n \\in \\mathbb{N}}\\) ist eine Funktion, die jeder natürlichen Zahl n eine reelle Zahl \\(a_n\\) zuordnet. Man kann sie <b>explizit</b> angeben (\\(a_n = 2n + 1\\)) oder <b>rekursiv</b> (\\(a_{n+1} = a_n + 2\\), \\(a_0 = 1\\)).')
        + h3('Arithmetische und geometrische Folge')
        + fx('Arithmetische Folge', r'a_n = a_0 + n \cdot d', 'Jedes Glied entsteht aus dem vorigen durch Addieren derselben Zahl d.',
             r'Lineare Abschreibung: \(d = -\frac{50.000 - 2.000}{10} = -4.800\); \(a_n = 50.000 - 4.800n\); \(a_{10} = 2.000\) €')
        + fx('Geometrische Folge', r'a_n = a_0 \cdot q^n', 'Jedes Glied entsteht aus dem vorigen durch Multiplizieren mit derselben Zahl q.',
             r'Zinseszins: \(a_n = 50.000 \cdot 1{,}05^n\); \(a_{10} \approx 81.444{,}73\) €')
        + bsp('Übungsblatt 1, Aufgabe 3', '50.000 € werden 10 Jahre mit 5 % pro Jahr angelegt. Entwicklung des Betrags und Name der Folge?',
              [(r'\(K_1 = 52.500\), \(K_2 = 55.125\), \(K_3 = 57.881{,}25\), …', ''), (r'\(K_{10} = 50.000 \cdot 1{,}05^{10}\)', '≈ 81.444,73 €'), ('Name', 'geometrische Folge (q = 1,05)')])
        + weiter('Wie verhalten sich Folgen auf lange Sicht? Dafür braucht man Beschränktheit und Monotonie.')
        + h3('Beschränktheit und Monotonie')
        + tabelle(['Eigenschaft', 'Bedeutung', 'Beispiel'], [
            ['beschränkt (durch M)', '|aₙ| ≤ M für alle n', 'aₙ = (−1)ⁿ ist durch M = 1 beschränkt'],
            ['nach oben beschränkt durch k', 'aₙ ≤ k', 'aₙ = −n (durch 0 nach oben beschränkt, nach unten unbeschränkt)'],
            ['nach unten beschränkt durch k', 'aₙ ≥ k', 'aₙ = n (durch 0 nach unten beschränkt, nach oben unbeschränkt)'],
            ['monoton wachsend / fallend', 'aₙ₊₁ ≥ aₙ bzw. aₙ₊₁ ≤ aₙ', 'Zinsfolge wächst, Abschreibungsfolge fällt']])
        + wahr('w-folgen', [('Die Folge aₙ = 50.000 · 1,05ⁿ ist geometrisch.', True, 'Konstanter Quotient 1,05.'), ('Lineare Abschreibung ergibt eine geometrische Folge.', False, 'Arithmetisch: konstante Differenz.'),
                            ('aₙ = (−1)ⁿ ist beschränkt, aber nicht monoton.', True, 'Sie springt zwischen −1 und 1.')])
        + p(r'<b>Teilfolge:</b> Lässt man aus einer Folge Glieder weg (behält aber unendlich viele in der ursprünglichen Reihenfolge), entsteht eine Teilfolge, z. B. \((a_{2n})\). Konvergiert eine Folge gegen a, dann konvergiert auch jede Teilfolge gegen a. Beispiel: Die ungeraden natürlichen Zahlen 1, 3, 5, 7, … bilden eine arithmetische Folge.'),
    merk='Arithmetisch: aₙ = a₀ + n·d (konstante Differenz, lineare Abschreibung). Geometrisch: aₙ = a₀·qⁿ (konstanter Quotient, Zinseszins). Beschränkt: |aₙ| ≤ M. Monoton wachsend: aₙ₊₁ ≥ aₙ.',
    exam='Vorstufe zu Grenzwerten; Zins- und Abschreibungsfolgen.',
    fehler=['Arithmetisch und geometrisch verwechseln.'],
    src='Übungsblatt 1, A3–A5')


def gw_bild():
    s, X, Y = graph([], (0, 20.5), (0, 1.1), xl='n', yl='aₙ', ticks_x=(5, 10, 15, 20), ticks_y=(0.6, 1))
    s += tpg(rechteck(X(0), Y(0.68), X(20.5) - X(0), Y(0.52) - Y(0.68), 'var(--pale)', 'var(--pale)', 2), 'ε-Schlauch um den Grenzwert 0,6: Ab einem bestimmten n liegen alle Glieder darin, egal wie schmal der Schlauch ist.')
    s += f'<line x1="{X(0)}" y1="{Y(0.6)}" x2="{X(20.5)}" y2="{Y(0.6)}" style="stroke:var(--c2)" stroke-width="1.6" stroke-dasharray="6 4"/>'
    for n in range(1, 21):
        a = (3 * n * n + 2 * n) / (5 * n * n - 1)
        s += tpg(punkt(X(n), Y(a), 'var(--primary)', 4), f'a_{n} = {a:.4f}'.replace('.', ','))
    s += T(X(20), Y(0.4), 'Grenzwert 3/5 (gestrichelt)', 12, 800, 'end', 'var(--c2)')
    return svg(360, 250, s, 'Konvergente Folge', maxw=420)


t_gw = thema('grenzwert-folge', 'Grenzwerte von Folgen',
    kern='Eine Folge konvergiert gegen a, wenn für jedes ε > 0 ab einem Index alle Glieder im ε-Schlauch um a liegen. Bei Bruchfolgen klammert man die höchste Potenz von n in Zähler und Nenner aus: Gleicher Grad → Quotient der Leitkoeffizienten, Zählergrad kleiner → 0, Zählergrad größer → bestimmt divergent. Folgen wie (−1)ⁿ divergieren.',
    kurz=p('Was passiert mit \\(a_n = \\frac{3n^2 + 2n}{5n^2 - 1}\\), wenn n riesig wird? Die Glieder kommen der Zahl \\(\\frac35\\) beliebig nahe. Man sagt: Die Folge <b>konvergiert</b> gegen den <b>Grenzwert</b> 3/5.')
        + p('Der Trick: Für große n zählen nur die <b>höchsten Potenzen</b>. Man klammert sie aus, und alle Reste wie \\(\\frac{2}{n}\\) werden zu null.'),
    fig=fw('Die Glieder nähern sich 3/5. Tippe auf die Punkte und den Schlauch.') + bild(gw_bild()),
    figcap='eigenes Beispiel nach Übungen Analysis I, Folgen',
    article=h3('Definition der Konvergenz')
        + p('Die Folge \\((a_n)\\) <b>konvergiert</b> gegen \\(a\\), wenn es zu jedem \\(\\varepsilon > 0\\) ein \\(n_0\\) gibt, sodass \\(|a_n - a| < \\varepsilon\\) für alle \\(n \\ge n_0\\). Schreibweise: \\(\\lim_{n \\to \\infty} a_n = a\\). Eine Folge mit Grenzwert 0 heißt <b>Nullfolge</b>. Jede konvergente Folge ist beschränkt.')
        + h3('Rechenregeln')
        + p('Sind \\(a_n \\to a\\) und \\(b_n \\to b\\), dann gilt \\(a_n + b_n \\to a + b\\), \\(a_n \\cdot b_n \\to a \\cdot b\\) und \\(\\frac{a_n}{b_n} \\to \\frac{a}{b}\\) (falls \\(b \\ne 0\\)). Die Umkehrung gilt nicht: \\((-1)^n + (-1)^{n+1} = 0\\) konvergiert, die Summanden nicht.')
        + weiter('Mit diesen Regeln und dem Ausklammern löst man fast jede Bruchfolge.')
        + h3('Bruchfolgen: höchste Potenz ausklammern')
        + bsp('Grad gleich', r'\(a_n = \frac{3n^2 + 2n}{5n^2 - 1}\)',
              [(r'\(n^2\) ausklammern: \(\frac{n^2(3 + \frac{2}{n})}{n^2(5 - \frac{1}{n^2})}\)', ''), (r'\(\frac{2}{n} \to 0\), \(\frac{1}{n^2} \to 0\)', r'\(\lim a_n = \frac{3}{5}\)')])
        + bsp('Übungen Analysis I, Folgen 1a', r'\(a_n = \frac{2}{n^2} + \frac{3}{2n - 1}\)', [('Beide Summanden haben einen konstanten Zähler und einen wachsenden Nenner', r'\(\lim a_n = 0 + 0 = 0\)')])
        + tabelle(['Zählergrad … Nennergrad', 'Grenzwert für n → ∞'], [['kleiner', '0'], ['gleich', 'Quotient der Leitkoeffizienten'], ['größer', '±∞ (bestimmt divergent)']])
        + p('<b>Divergent</b> ist auch \\(c_n = (-1)^n \\frac{n+3}{n}\\): Der Bruch geht gegen 1, das Vorzeichen springt, die Glieder pendeln zwischen etwa −1 und 1.')
        + falle('Nur die Zahlen im Zähler und Nenner vergleichen, ohne auf die Potenzen von n zu achten.')
        + wahr('w-gw', [(r'\(\lim_{n\to\infty} \frac{4n^3}{2n^3 + n} = 2\)', True, 'Gleicher Grad: 4/2.'), (r'\(\lim_{n\to\infty} \frac{n}{n^2 + 1} = 1\)', False, 'Zählergrad kleiner: 0.'),
                        ('Jede konvergente Folge ist beschränkt.', True, 'Satz aus der Vorlesung.')]),
    merk='Konvergenz: ab einem n₀ liegen alle Glieder im ε-Schlauch um a. Bruchfolgen: höchste Potenz ausklammern; Grad Zähler < Nenner → 0, gleich → Leitkoeffizienten-Quotient, größer → divergent. (−1)ⁿ·… pendelt → divergent. Konvergent ⇒ beschränkt.',
    exam='Grundlage für Grenzwerte von Funktionen und Sättigungswerte.',
    fehler=['Höchste Potenz nicht ausklammern.', 'Alternierende Folgen für konvergent halten.'],
    src='Übungsblatt 1 A2, Übungen Analysis I')

KAPITEL = kapitel('k2', 'Folgen und Grenzwerte',
    'Wohin läuft eine Zahlenfolge? Von Zinseszins und Abschreibung zum Grenzwert.',
    ['Folgen', 'Grenzwerte'], [t_folgen, t_gw])
