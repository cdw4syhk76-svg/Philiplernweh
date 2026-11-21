import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *

# Durchgehendes Beispiel: Die Eisdiele „Gelato Quadrat“ wählt zwischen drei Strategien a1–a3; das Wetter (z1–z4) entscheidet über den Gewinn.

def zahl(v):
    if isinstance(v, str):
        return v
    s = f'{v:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
    s = s[:-3] if s.endswith(',00') else s.rstrip('0')
    return s.replace('-', '−')


def matrix(zeilen, spalten, extra=None, best=None, marks=(), unter='', kopf2=None, breite=360):
    """Entscheidungsmatrix wie auf den Folien. zeilen [(name, [werte])], extra (kopf, [werte]) als letzte Spalte,
    best = Index der gewählten Zeile, marks = {(zeile, spalte)} hervorgehobene Zellen, kopf2 = zweite Kopfzeile (z. B. Wahrscheinlichkeiten)"""
    n = len(spalten); ew = 78 if extra else 0; nw = 36
    cw = (breite - 8 - nw - ew) / n; rh = 32; y0 = 8; hh = 30 if not kopf2 else 48
    s = ''
    for j, k in enumerate(spalten):
        x = 4 + nw + j * cw
        s += T(x + cw / 2, y0 + 18, k, 13, 800, 'middle', 'var(--muted)')
        if kopf2:
            s += T(x + cw / 2, y0 + 36, kopf2[j], 12, 600, 'middle', 'var(--muted)')
    if extra:
        s += T(breite - 4 - ew / 2, y0 + 18, extra[0], 13, 800, 'middle', 'var(--primary)')
    for i, (name, werte) in enumerate(zeilen):
        y = y0 + hh + i * rh
        s += rechteck(4, y, breite - 8, rh - 3, 'var(--pale)' if i == best else 'var(--card)', 'var(--primary)' if i == best else 'var(--line)', 6)
        s += T(4 + nw / 2 + 2, y + 18, name, 13, 800)
        for j, v in enumerate(werte):
            x = 4 + nw + j * cw
            if (i, j) in marks:
                s += rechteck(x + 4, y + 3, cw - 8, rh - 9, 'var(--c3)', 'var(--c3)', 5)
                s += T(x + cw / 2, y + 18, zahl(v), 13, 800, 'middle', 'var(--on-primary)')
            else:
                s += T(x + cw / 2, y + 18, zahl(v), 13, 500)
        if extra:
            ex = breite - 4 - ew
            if i == best:
                s += rechteck(ex + 2, y + 2, ew - 6, rh - 7, 'var(--primary)', 'var(--primary)', 5)
            s += T(ex + ew / 2, y + 18, zahl(extra[1][i]), 13, 800, 'middle', 'var(--on-primary)' if i == best else 'var(--ink)')
    h = y0 + hh + len(zeilen) * rh + (24 if unter else 6)
    if unter:
        s += T(breite / 2, h - 8, unter, 13, 700, 'middle', 'var(--muted)')
    return svg(breite, h, s, 'Entscheidungsmatrix', maxw=440)


Z = ['z1', 'z2', 'z3', 'z4']
M = [('a1', [60, 30, 50, 60]), ('a2', [10, 10, 10, 140]), ('a3', [-30, 100, 120, 130])]

# ---------------------------------------------------------------- 1 Dominanz
M5 = [('a1', [0, 20, 10, 60, 25]), ('a2', [-20, 80, 10, 10, 60]), ('a3', [20, 60, 20, 60, 50]), ('a4', [55, 40, 60, 10, 40]), ('a5', [50, 10, 30, 5, 20])]


def wdom_bild():
    X = lambda p: 50 + p * 2.9
    Y = lambda e: 200 - e * 2.9
    s = achsen(50, 200, 350, 10, '', 'Ergebnis') + T(350, 236, 'Wahrscheinlichkeit, mindestens e zu erreichen', 12, 600, 'end', 'var(--muted)')
    for k in (20, 40, 60):
        s += T(44, Y(k) + 4, str(k), 12, 400, 'end')
    for k in (25, 50, 75, 100):
        s += T(X(k), 216, f'{k} %', 12, 400)
    a1 = [(50, 10), (40, 20), (20, 30), (10, 40)]
    a2 = [(60, 30), (50, 40), (30, 20), (20, 10)]
    for wert, farbe, name in ((a1, 'var(--c3)', 'a1'), (a2, 'var(--primary)', 'a2')):
        pts, cum = [], 0
        for e, p in wert:
            pts += [(X(cum), Y(e)), (X(cum + p), Y(e))]
            cum += p
        s += linie(pts, farbe, 3)
    s += T(X(62), Y(44), 'a2', 14, 800, 'middle', 'var(--primary)') + T(X(36), Y(26), 'a1', 14, 800, 'middle', 'var(--c3)')
    return svg(360, 244, s, 'Wahrscheinlichkeitsdominanz', maxw=440)


t_dom = thema('dominanz', 'Dominanzregeln: Zustands- und Wahrscheinlichkeitsdominanz',
    kern='Eine Alternative ist zustandsdominant, wenn sie in jedem Umweltzustand mindestens so gut und in einem besser ist. Wahrscheinlichkeitsdominant ist sie, wenn die Wahrscheinlichkeit, mindestens einen Wert zu erreichen, nie kleiner und einmal größer ist. Dominierte Alternativen fallen weg.',
    kurz=p('Bevor man rechnet, räumt man auf: Gibt es eine Alternative, die <b>immer</b> schlechter ist als eine andere, egal welches Wetter kommt? Dann streicht man sie. Das ist die <b>Zustandsdominanz</b>.')
        + p('In der Matrix stehen die Alternativen (a) als Zeilen und die Umweltzustände (z) als Spalten. Jede Zelle ist das Ergebnis, wenn man a wählt und z eintritt.'),
    fig=fw('Zustandsdominanz im Folienbeispiel: a3 ist überall mindestens so gut wie a1, a4 überall mindestens so gut wie a5. a1 und a5 fallen weg.')
        + bild(matrix(M5, ['z1', 'z2', 'z3', 'z4', 'z5'], best=2, marks={(0, j) for j in range(5)} | {(4, j) for j in range(5)}, unter='a3 dominiert a1 · a4 dominiert a5')),
    figcap='nach Folien „Zustandsdominanz“; orange = dominierte Zeilen, umrandet = dominierende Alternative a3',
    article=h3('Überblick: Entscheidungsregeln für die Umwelt')
        + mfig('Umweltereignisse: drei Gruppen von Regeln', svg(560, 220,
            box(200, 6, 160, 40, 'Umweltereignisse', art='hl', size=13)
            + pfeil(250, 48, 96, 68) + pfeil(280, 48, 280, 68) + pfeil(310, 48, 464, 68)
            + box(8, 70, 176, 140, 'Dominanzregeln\n\n· Zustandsdominanz\n· Wahrscheinlichkeits-\n  dominanz', size=13, tip='Vorab aufräumen: dominierte Alternativen streichen.')
            + box(192, 70, 176, 140, 'unter Ungewissheit\n\n· Maximin · Maximax\n· Hurwicz\n· Savage-Niehans\n· Laplace', size=13, tip='Ungewissheit: Wahrscheinlichkeiten der Umweltzustände sind unbekannt.')
            + box(376, 70, 176, 140, 'unter Risiko\n\n· Bayes-Regel\n  (µ-Kriterium)\n· Bernoulli-Prinzip', size=13, tip='Risiko: Wahrscheinlichkeiten sind bekannt.'),
            'Übersicht der Entscheidungsregeln'), 'nach Folie „Klassische Entscheidungstheorie: Umwelt – Übersicht“')
        + p('<b>Unterschied:</b> Unter <b>Risiko</b> kennt man die Wahrscheinlichkeiten der Umweltzustände, unter <b>Ungewissheit</b> nicht.')
        + weiter('Zuerst wird aufgeräumt: Welche Alternativen sind nie die beste Wahl?')
        + h3('Zustandsdominanz')
        + fx('Zustandsdominanz', r'a_1 \text{ dominiert } a_2, \text{ wenn } e_{1j} \geq e_{2j} \text{ für alle } j \text{ und } e_{1j} > e_{2j} \text{ für mindestens ein } j',
             'a1 ist in jedem Umweltzustand mindestens so gut wie a2 und in mindestens einem besser. Dann ist a1 „auf jeden Fall“ vorzuziehen.',
             'a1 (Zentrum) 125.000 / 90.000 gegen a2 (Randlage) 100.000 / 80.000: a1 ist zustandsdominant.')
        + p('Im großen Beispiel vergleicht man je zwei Zeilen Zelle für Zelle: a3 (20, 60, 20, 60, 50) ist überall mindestens so gut wie a1 (0, 20, 10, 60, 25) → a1 fällt weg. a4 (55, 40, 60, 10, 40) schlägt a5 (50, 10, 30, 5, 20) → a5 fällt weg. a2, a3, a4 bleiben, keine von ihnen dominiert eine andere.')
        + weiter('Kennt man die Wahrscheinlichkeiten, gibt es eine schärfere Prüfung.')
        + h3('Wahrscheinlichkeitsdominanz')
        + p('„Eine Alternative dominiert eine andere, wenn bei ihr die Wahrscheinlichkeit, mindestens einen Ergebniswert e′ zu erzielen, nie kleiner und mindestens einmal größer als bei der anderen ist.“ Sie kann bei Entscheidungen unter Risiko geprüft werden.')
        + matrix([('a1', [20, 40, 10, 50]), ('a2', [60, 30, 50, 20])], Z, kopf2=['p = 30 %', 'p = 20 %', 'p = 40 %', 'p = 10 %'])
        + p('Zustandsweise ist keine besser (mal a1, mal a2). Deshalb zwei Schritte:')
        + bsp('Wahrscheinlichkeitsdominanz prüfen', '',
              [('Schritt 1: Ergebnisse je Alternative von groß nach klein ordnen. a1: 50 (10 %), 40 (20 %), 20 (30 %), 10 (40 %). a2: 60 (30 %), 50 (40 %), 30 (20 %), 20 (10 %).', ''),
               ('Schritt 2: Für jedes Ergebnis die Wahrscheinlichkeit „mindestens so viel“ aufsummieren und zeichnen. Mindestens 50: a1 10 %, a2 70 %. Mindestens 30: a1 30 %, a2 90 %. Mindestens 20: a1 60 %, a2 100 %.', ''),
               ('Die Linie von a2 liegt nie unter der von a1.', 'a2 ist wahrscheinlichkeitsdominant')])
        + mfig('Wahrscheinlichkeitsdominanz grafisch', wdom_bild(), 'Treppenkurven der beiden Alternativen')
        + wahr('w-dom', [('Eine zustandsdominierte Alternative kann gestrichen werden.', True, 'Sie ist nie besser.'),
                         ('Für Zustandsdominanz muss eine Alternative in jedem Zustand strikt besser sein.', False, 'Mindestens gleich gut, in einem besser.'),
                         ('Wahrscheinlichkeitsdominanz prüft man unter Risiko.', True, 'Man braucht Wahrscheinlichkeiten.')]),
    merk='Zustandsdominanz: in allen Zuständen ≥, in einem >. Wahrscheinlichkeitsdominanz: P(Ergebnis ≥ e) nie kleiner, einmal größer (unter Risiko). Dominierte Alternativen streichen. Risiko = Wahrscheinlichkeiten bekannt, Ungewissheit = unbekannt.',
    exam='Dominierte Alternativen in einer Matrix erkennen.',
    fehler=['Nur einzelne Spalten vergleichen statt alle.', 'Risiko und Ungewissheit vertauschen.'],
    src='Folien 193–199')

# ---------------------------------------------------------------- 2 Maximin und Maximax
t_maxi = thema('maximin', 'Maximin- und Maximax-Regel',
    kern='Maximin (extrem risikoscheu): für jede Alternative das schlechteste Ergebnis nehmen, dann das beste davon wählen. Maximax (extrem risikofreudig): das beste Ergebnis jeder Alternative nehmen, dann das beste davon.',
    kurz=p('Die Eisdiele hat drei Strategien, das Wetter vier mögliche Zustände, Wahrscheinlichkeiten kennt niemand (<b>Ungewissheit</b>). Ein Pessimist fragt: Was ist bei jeder Strategie das <b>Schlimmste</b>, und wo ist das Schlimmste am wenigsten schlimm? Das ist die <b>Maximin-Regel</b>.')
        + p('Ein Optimist fragt: Wo ist das <b>Beste</b> am besten? Das ist die <b>Maximax-Regel</b>.'),
    fig=fw('Umschalten zwischen den beiden Regeln. Orange: das jeweils schlechteste bzw. beste Ergebnis jeder Zeile.')
        + tafeln('tf-maxi', ['Maximin', 'Maximax'], [
            matrix(M, Z, ('Minimum', [30, 10, -30]), best=0, marks={(0, 1), (1, 0), (1, 1), (1, 2), (2, 0)}, unter='bestes schlechtestes Ergebnis: a1'),
            matrix(M, Z, ('Maximum', [60, 140, 130]), best=1, marks={(0, 0), (0, 3), (1, 3), (2, 3)}, unter='bestes bestes Ergebnis: a2')]),
    figcap='Matrix der Folien „Maximin-Regel“ und „Maximax-Regel“',
    article=h3('Maximin: das beste schlechteste Ergebnis')
        + p('Intention: Entscheidungsverhalten eines <b>extrem risikoscheuen</b> Akteurs. Beurteilt wird nur nach dem schlechtestmöglichen Ergebnis. ' + eg('Man geht davon aus, dass immer das Schlimmste eintritt.'))
        + bsp('Maximin', 'Matrix: a1 (60, 30, 50, 60), a2 (10, 10, 10, 140), a3 (−30, 100, 120, 130).',
              [('Zeilenminimum: a1 → 30, a2 → 10, a3 → −30', ''), ('das größte Minimum', 'a1 (30)')], 'Bei a1 ist das schlechtestmögliche Ergebnis 30: am wenigsten schlimm.')
        + p('Problem: Die Regel schaut nur auf ein einziges Ergebnis. Bei a1 (1.000.000, 2.000.000, 1, 3.000.000) gegen a2 (10, 2, 100, 10) würde Maximin a2 wählen (Minimum 2 > 1), obwohl a1 sonst Millionen bringt.')
        + weiter('Das Gegenstück schaut nur auf das beste Ergebnis.')
        + h3('Maximax: das beste beste Ergebnis')
        + p('Intention: Entscheidungsverhalten eines <b>extrem risikofreudigen</b> Akteurs. Beurteilt wird nur nach dem bestmöglichen Ergebnis.')
        + bsp('Maximax', 'Gleiche Matrix.', [('Zeilenmaximum: a1 → 60, a2 → 140, a3 → 130', ''), ('das größte Maximum', 'a2 (140)')])
        + falle('Bei Maximin das Minimum der Minima nehmen. Richtig: erst je Zeile das Minimum, dann davon das <b>Maximum</b>.')
        + wahr('w-maxi', [('Die Maximin-Regel beschreibt einen risikoscheuen Entscheider.', True, 'Er schaut nur auf das Schlimmste.'),
                          ('Bei Maximax wählt man die Alternative mit dem größten Zeilenmaximum.', True, 'Das beste beste Ergebnis.'),
                          ('In der Folienmatrix wählt Maximin a3.', False, 'a3 hat das schlechteste Minimum (−30); Maximin wählt a1.')]),
    merk='Maximin (risikoscheu): Zeilenminimum, davon das Maximum. Maximax (risikofreudig): Zeilenmaximum, davon das Maximum. Folienmatrix: Maximin a1, Maximax a2.',
    exam='Maximin und Maximax in einer Matrix anwenden; Risikoeinstellung zuordnen.',
    fehler=['Minimum der Minima wählen.', 'Risikoscheu und risikofreudig vertauschen.'],
    src='Folien 200–203')

# ---------------------------------------------------------------- 3 Hurwicz (Rechner)
t_hur = thema('hurwicz', 'Hurwicz-Regel mit Optimismusparameter', star=True, wide=True,
    kern='Die Hurwicz-Regel kombiniert Maximin und Maximax: Φ(a) = λ · Maximum + (1 − λ) · Minimum. λ ist der Optimismusparameter; in der Vorlesung gilt λ = 0,4.',
    kurz=p('Weder nur Pessimist noch nur Optimist: Die Eisdiele gewichtet das beste und das schlechteste Ergebnis jeder Strategie. Mit welchem Gewicht, sagt der <b>Optimismusparameter λ</b>. Ist λ groß, zählt das Beste mehr (risikofreudig), ist λ klein, zählt das Schlimmste mehr (risikoscheu).')
        + p('In der Vorlesung ist λ = 0,4 („immer 0,4“). Dann zählt das Maximum zu 40 %, das Minimum zu 60 %.'),
    fig=fw('Schiebe λ. Bei λ = 0 entspricht Hurwicz der Maximin-Regel, bei λ = 1 der Maximax-Regel.')
        + regler([('huL', 'Optimismusparameter λ', 0, 1, 0.1, 0.4, '')])
        + '<svg id="figHU" viewBox="0 0 360 200" style="max-width:440px;width:100%;margin:0 auto;display:block" role="img" aria-label="Hurwicz-Werte"></svg>'
        + schritte_karten([('① a1', 'huR1', '#huT1'), ('② a2 und a3', 'huR2', '#huT2'), ('③ Wahl', 'huR3', '#huT3')]),
    figcap='Matrix der Folie „Hurwicz-Regel“',
    article=h3('Die Formel')
        + fx('Hurwicz-Regel', r'\Phi(a_i) = \lambda \cdot \max_j e_{ij} + (1 - \lambda) \cdot \min_j e_{ij}',
             'Für jede Alternative: λ mal bestes Ergebnis plus (1 − λ) mal schlechtestes Ergebnis. Gewählt wird das größte Φ.',
             r'a1: \(0{,}4 \cdot 60 + 0{,}6 \cdot 30 = 24 + 18 = 42\)')
        + bsp('Folienbeispiel mit λ = 0,4', 'a1 (60, 30, 50, 60), a2 (10, 10, 10, 140), a3 (−30, 100, 120, 130).',
              [(r'a1: \(0{,}4 \cdot 60 + 0{,}6 \cdot 30\)', '42'), (r'a2: \(0{,}4 \cdot 140 + 0{,}6 \cdot 10 = 56 + 6\)', '62'), (r'a3: \(0{,}4 \cdot 130 + 0{,}6 \cdot (-30) = 52 - 18\)', '34'), ('größtes Φ', 'a2')])
        + bsp('Zweites Folienbeispiel', 'a1 (1.000.000, 2.000.000, 1, 3.000.000), a2 (10, 2, 100, 10).',
              [(r'a1: \(0{,}4 \cdot 3.000.000 + 0{,}6 \cdot 1\)', '1.200.000,6'), (r'a2: \(0{,}4 \cdot 100 + 0{,}6 \cdot 2\)', '41,2'), ('Wahl', 'a1')], 'Anders als Maximin übersieht Hurwicz die Millionen nicht.')
        + weiter('Wie hängt λ mit der Risikoeinstellung zusammen?')
        + h3('λ und die Risikoeinstellung')
        + tabelle(['λ', 'Gewicht', 'Verhalten'], [['0', 'nur Minimum', 'Maximin: extrem risikoscheu'], ['zwischen 0 und 1', 'Mischung', 'je größer λ, desto optimistischer'], ['1', 'nur Maximum', 'Maximax: extrem risikofreudig']])
        + klausur_hinweis('Die Hurwicz-Regel ist sehr häufig gefragt, meist als Auswahlfrage: risikofreudig oder risikoscheu? Antwort: Sie verbindet beides, je nach λ. Ein großes λ steht für einen risikofreudigeren Entscheider. Rechne mit λ = 0,4, wenn nichts anderes angegeben ist.')
        + falle('λ und (1 − λ) vertauschen: λ gehört zum Maximum.')
        + wahr('w-hur', [('Bei λ = 1 entspricht die Hurwicz-Regel der Maximax-Regel.', True, 'Nur das Maximum zählt.'),
                         ('Ein kleines λ steht für einen optimistischen Entscheider.', False, 'Kleines λ: das Minimum zählt mehr, also eher pessimistisch.'),
                         ('Mit λ = 0,4 wählt man in der Folienmatrix a2.', True, 'Φ = 42 / 62 / 34.')]),
    merk='Hurwicz: Φ = λ · Max + (1 − λ) · Min, größtes Φ wählen. λ = Optimismusparameter (Vorlesung: 0,4). λ = 0 → Maximin, λ = 1 → Maximax. Folienmatrix: 42 / 62 / 34 → a2.',
    exam='Hurwicz-Werte im Kopf rechnen (λ = 0,4); Risikoeinstellung deuten (Auswahlfrage).',
    fehler=['λ beim Minimum statt beim Maximum ansetzen.', 'Negatives Minimum falsch einsetzen (0,6 · (−30) = −18).'],
    src='Folien 204–205')

# ---------------------------------------------------------------- 4 Savage-Niehans
t_sav = thema('savage-niehans', 'Savage-Niehans-Regel: das kleinste Bedauern',
    kern='Die Savage-Niehans-Regel minimiert das maximale Bedauern: Für jeden Zustand das beste Ergebnis suchen, die Bedauernsmatrix bilden (bestes Ergebnis minus eigenes), je Alternative das größte Bedauern nehmen und davon das kleinste wählen.',
    kurz=p('Nachdem man die Zukunft kennt, ärgert man sich über die alte Entscheidung: „Hätte ich doch …“. Die <b>Savage-Niehans-Regel</b> fragt: Wie sehr würde ich mich im schlimmsten Fall ärgern? Und sie wählt die Alternative, bei der dieser Ärger am kleinsten ist. Daher der Name <b>Regel des kleinsten Bedauerns</b>.'),
    fig=fw('Schalte durch die drei Schritte.')
        + tafeln('tf-sav', ['1 Maximum', '2 Bedauern', '3 Wahl'], [
            matrix(M, Z, marks={(0, 0), (2, 1), (2, 2), (1, 3)}, unter='Maximum je Spalte: 60 · 100 · 120 · 140'),
            matrix([('a1', [0, 70, 70, 80]), ('a2', [50, 90, 110, 0]), ('a3', [90, 0, 0, 10])], Z, unter='Bedauern = Spaltenmaximum − eigenes Ergebnis'),
            matrix([('a1', [0, 70, 70, 80]), ('a2', [50, 90, 110, 0]), ('a3', [90, 0, 0, 10])], Z, ('max. Bed.', [80, 110, 90]), best=0, marks={(0, 3), (1, 2), (2, 0)}, unter='kleinstes maximales Bedauern: a1 (80)')]),
    figcap='Matrix der Folien „Savage-Niehans-Regel“',
    article=h3('Drei Schritte')
        + bsp('Savage-Niehans', 'a1 (60, 30, 50, 60), a2 (10, 10, 10, 140), a3 (−30, 100, 120, 130).',
              [('Schritt 1: für jeden Umweltzustand das Maximum: z1 60, z2 100, z3 120, z4 140', ''),
               ('Schritt 2: Bedauernsmatrix = Maximum der Spalte minus eigenes Ergebnis. a1: 0, 70, 70, 80. a2: 50, 90, 110, 0. a3: 90, 0, 0, 10.', ''),
               ('Schritt 3: je Zeile das größte Bedauern (80, 110, 90), davon das kleinste', 'a1')],
              'Mit a1 ärgert man sich höchstens um 80.')
        + p('„Wie sehr würde ich mich ärgern, wenn die einzelnen Zustände eintreten?“ Das ist die Frage der Bedauernsmatrix. ' + eg('Bedauern = was man hätte haben können minus was man hat.'))
        + falle('Das Bedauern zeilenweise statt spaltenweise berechnen. Das Maximum wird je <b>Umweltzustand</b> (Spalte) gesucht.')
        + wahr('w-sav', [('Die Savage-Niehans-Regel minimiert das maximale Bedauern.', True, 'Regel des kleinsten Bedauerns.'),
                         ('Das Bedauern berechnet man als Zeilenmaximum minus Ergebnis.', False, 'Spaltenmaximum (je Umweltzustand) minus Ergebnis.'),
                         ('In der Folienmatrix wählt die Regel a1.', True, 'Maximales Bedauern 80 / 110 / 90.')]),
    merk='Savage-Niehans: 1) Spaltenmaximum je Zustand, 2) Bedauern = Spaltenmaximum − Ergebnis, 3) je Zeile größtes Bedauern, davon das kleinste wählen. Folienmatrix: a1.',
    exam='Bedauernsmatrix aufstellen und die Alternative mit dem kleinsten maximalen Bedauern bestimmen.',
    fehler=['Zeilen- statt Spaltenmaximum nehmen.', 'Am Ende das größte statt das kleinste maximale Bedauern wählen.'],
    src='Folien 206–208')

# ---------------------------------------------------------------- 5 Laplace
t_lap = thema('laplace', 'Laplace-Kriterium und Vergleich der Regeln',
    kern='Das Laplace-Kriterium nimmt an, dass alle Umweltzustände gleich wahrscheinlich sind (p = 1/n, „Prinzip des mangelnden Grundes“), und wählt den höchsten Durchschnitt. Jede Regel kann zu einer anderen Wahl führen.',
    kurz=p('Wenn man gar nichts über die Wahrscheinlichkeiten weiß, warum sollte ein Zustand wahrscheinlicher sein als ein anderer? Das <b>Laplace-Kriterium</b> gibt jedem Zustand dasselbe Gewicht und rechnet einfach den <b>Durchschnitt</b> jeder Zeile.'),
    fig=fw('Laplace: der Durchschnitt jeder Zeile.') + bild(matrix(M, Z, ('Ø', [50, 42.5, 80]), best=2, unter='p = ¼ je Zustand → a3')),
    figcap='Matrix der Folie „Laplace-Kriterium“',
    article=h3('Prinzip des mangelnden Grundes')
        + fx('Laplace-Kriterium', r'E(a_i) = \frac{1}{n} \sum_{j=1}^{n} e_{ij}', 'Alle n Zustände gleich wahrscheinlich: Zeilensumme durch n. Größten Wert wählen.', r'a3: \(\frac{1}{4}(-30 + 100 + 120 + 130) = \frac{320}{4} = 80\)')
        + bsp('Laplace', 'Gleiche Matrix.', [(r'a1: \(\frac{60 + 30 + 50 + 60}{4} = \frac{200}{4}\)', '50'), (r'a2: \(\frac{170}{4}\)', '42,5'), (r'a3: \(\frac{320}{4}\)', '80'), ('größter Durchschnitt', 'a3')])
        + weiter('Jede Regel hat ihre eigene Logik und wählt hier anders.')
        + h3('Zusammenführung')
        + tabelle(['Regel', 'Wahl', 'Logik'], [['Maximin', 'a1', 'bestes schlechtestes Ergebnis'], ['Maximax', 'a2', 'bestes bestes Ergebnis'], ['Hurwicz (λ = 0,4)', 'a2', 'Mischung aus Maximum und Minimum'], ['Savage-Niehans', 'a1', 'kleinstes maximales Bedauern'], ['Laplace', 'a3', 'höchster Durchschnitt']])
        + p('Was bringt das? Es gibt nicht <b>die</b> richtige Regel. Als Betriebswirt muss man herausfinden, welche Regel zur eigenen Lage und Risikoeinstellung passt.')
        + wahr('w-lap', [('Das Laplace-Kriterium setzt alle Zustände gleich wahrscheinlich.', True, 'Prinzip des mangelnden Grundes.'),
                         ('Alle Regeln unter Ungewissheit führen zur selben Wahl.', False, 'Hier: a1, a2, a2, a1, a3.')]),
    merk='Laplace: p = 1/n für jeden Zustand (Prinzip des mangelnden Grundes), Zeilendurchschnitt, höchsten wählen. Folienmatrix: Maximin a1, Maximax a2, Hurwicz a2, Savage a1, Laplace a3.',
    exam='Laplace-Durchschnitt berechnen; Ergebnisse der Regeln vergleichen.',
    fehler=['Durch die Zahl der Alternativen statt der Zustände teilen.'],
    src='Folien 209–210')

# ---------------------------------------------------------------- 6 Bayes
t_bay = thema('bayes', 'Entscheidung unter Risiko: Bayes-Regel (µ-Kriterium)', star=True,
    kern='Unter Risiko sind die Wahrscheinlichkeiten bekannt. Die Bayes-Regel (µ-Kriterium) wählt die Alternative mit dem höchsten Erwartungswert E = Σ p_j · e_ij. Sie unterstellt Risikoneutralität.',
    kurz=p('Jetzt weiß die Eisdiele, wie wahrscheinlich die Zustände sind, etwa aus Erfahrung: Mit 70 % Wahrscheinlichkeit kommt keine Umgehungsstraße. Dann rechnet man den <b>Erwartungswert</b>: jedes Ergebnis mal seine Wahrscheinlichkeit, alles addieren.')
        + p('Gewählt wird der höchste Erwartungswert. Das ist die <b>Bayes-Regel</b>, auch <b>µ-Kriterium</b> (µ = Erwartungswert).'),
    fig=fw('Standortentscheidung unter Risiko.') + bild(matrix([('a1', [125000, 125000]), ('a2', [150000, 80000])], ['z1: keine Straße', 'z2: Straße'], ('µ', [125000, 129000]), best=1, kopf2=['p = 0,7', 'p = 0,3'], unter='a1 = Zentrum, a2 = Randlage → a2')),
    figcap='Beispiel der Folie „Entscheidung unter Risiko: µ-Kriterium / Bayes-Regel“',
    article=h3('Erwartungswert')
        + fx('Bayes-Regel (µ-Kriterium)', r'E(a_i) = \mu_i = \sum_{j=1}^{n} p_j \cdot e_{ij}', 'Jedes Ergebnis mal Wahrscheinlichkeit des Zustands, aufsummieren; höchsten Wert wählen.',
             r'a2: \(0{,}7 \cdot 150.000 + 0{,}3 \cdot 80.000 = 105.000 + 24.000 = 129.000\)')
        + bsp('Standort', 'a1 (Zentrum): 125.000 in beiden Fällen; a2 (Randlage): 150.000 ohne, 80.000 mit Umgehungsstraße; p = 0,7 / 0,3.',
              [(r'\(\mu_1 = 0{,}7 \cdot 125.000 + 0{,}3 \cdot 125.000\)', '125.000'), (r'\(\mu_2 = 105.000 + 24.000\)', '129.000'), ('höchster Erwartungswert', 'a2')])
        + p('<b>Kritik:</b> Die Regel unterstellt <b>Risikoneutralität</b>. Bei unendlich vielen Wiederholungen ist sie richtig, bei einer einzelnen Entscheidung nicht zwingend: Wer nur einmal entscheidet, bekommt entweder 150.000 oder 80.000, nie den Durchschnitt.')
        + klausur_hinweis('Auswahlfragen mit Wahrscheinlichkeiten: Erwartungswert im Kopf ausrechnen. Prozente als Dezimalzahl (70 % = 0,7); die Wahrscheinlichkeiten müssen zusammen 1 ergeben.')
        + wahr('w-bay', [('Die Bayes-Regel wählt den höchsten Erwartungswert.', True, 'µ-Kriterium.'),
                         ('Die Bayes-Regel berücksichtigt die Risikoeinstellung des Entscheiders.', False, 'Sie unterstellt Risikoneutralität; das leistet erst Bernoulli.'),
                         ('Bei p = 0,7 und 0,3 hat die Randlage den Erwartungswert 129.000.', True, '105.000 + 24.000.')]),
    merk='Bayes (µ-Kriterium): E = Σ p_j · e_ij, höchsten wählen. Unterstellt Risikoneutralität (richtig bei vielen Wiederholungen). Beispiel: 125.000 gegen 129.000 → Randlage.',
    exam='Erwartungswerte berechnen und die Kritik (Risikoneutralität) kennen.',
    fehler=['Wahrscheinlichkeiten den falschen Spalten zuordnen.', 'Mit Prozentzahlen statt Dezimalzahlen rechnen.'],
    src='Folien 211–212')

# ---------------------------------------------------------------- 7 Bernoulli
t_ber = thema('bernoulli', 'Bernoulli-Prinzip: Erwartungsnutzen statt Erwartungswert',
    kern='Das Bernoulli-Prinzip rechnet die Ergebnisse erst mit einer Nutzenfunktion in Nutzen um (Nutzenmatrix) und wählt dann den höchsten erwarteten Nutzen. So wird die Risikoeinstellung berücksichtigt.',
    kurz=p('100 € mehr sind für einen Studenten viel, für eine Millionärin wenig. Geld stiftet erst mehr Nutzen, irgendwann bringt mehr kaum noch etwas. Deshalb zählt laut <b>Bernoulli</b> nicht der Erwartungswert des Geldes, sondern der <b>erwartete Nutzen</b>.')
        + p('Vorgehen: Ergebnisse mit der Nutzenfunktion in Nutzen umrechnen (Schritt 1), dann den Erwartungswert der Nutzen bilden (Schritt 2). Die Alternative mit dem größten erwarteten Nutzen gewinnt.'),
    fig=fw('Das Folienbeispiel mit u(e) = 300e − e² in zwei Schritten.')
        + tafeln('tf-ber', ['Ergebnisse', '1 Nutzen', '2 Erwartung'], [
            matrix([('a1', [30, 20, 20]), ('a2', [140, -40, -30]), ('a3', [40, 10, 60])], ['z1', 'z2', 'z3'], kopf2=['p = 0,5', 'p = 0,2', 'p = 0,3'], unter='u(e) = 300e − e²'),
            matrix([('a1', [8100, 5600, 5600]), ('a2', [22400, -13600, -9900]), ('a3', [10400, 2900, 14400])], ['z1', 'z2', 'z3'], kopf2=['p = 0,5', 'p = 0,2', 'p = 0,3'], unter='Nutzenmatrix'),
            matrix([('a1', [8100, 5600, 5600]), ('a2', [22400, -13600, -9900]), ('a3', [10400, 2900, 14400])], ['z1', 'z2', 'z3'], ('E(u)', [6850, 5510, 10100]), best=2, kopf2=['p = 0,5', 'p = 0,2', 'p = 0,3'], unter='höchster Erwartungsnutzen: a3')]),
    figcap='Beispiel der Folien „Bernoulli-Prinzip“',
    article=h3('Die Idee')
        + p('„Nicht der Erwartungswert des Auszahlungsbetrags ist entscheidend, sondern der erwartete Nutzen aus dem Auszahlungsbetrag.“ Die Abwägung soll die Risikostruktur berücksichtigen. Wähle die Alternative mit dem größten erwarteten Nutzen.')
        + fx('Bernoulli-Prinzip', r'E\big(u(a_i)\big) = \sum_{j=1}^{n} p_j \cdot u(e_{ij})', 'Erst jedes Ergebnis in Nutzen umrechnen, dann mit den Wahrscheinlichkeiten gewichten und addieren.', r'a1: \(0{,}5 \cdot 8.100 + 0{,}2 \cdot 5.600 + 0{,}3 \cdot 5.600 = 4.050 + 1.120 + 1.680 = 6.850\)')
        + bsp('Folienbeispiel', r'Nutzenfunktion \(u(e) = 300e - e^2\) (für e ≤ 150).',
              [(r'Nutzen a1: \(300 \cdot 30 - 900 = 8.100\); \(300 \cdot 20 - 400 = 5.600\)', ''), (r'Nutzen a2: \(42.000 - 19.600 = 22.400\); \(-12.000 - 1.600 = -13.600\); \(-9.000 - 900 = -9.900\)', ''),
               (r'Nutzen a3: \(12.000 - 1.600 = 10.400\); \(3.000 - 100 = 2.900\); \(18.000 - 3.600 = 14.400\)', ''),
               (r'E(u): a1 6.850; a2 \(11.200 - 2.720 - 2.970 = 5.510\); a3 \(5.200 + 580 + 4.320 = 10.100\)', 'a3')])
        + bsp('Weizen oder Erdbeeren?', r'Erträge Weizen 1.600 / 3.600 / 10.000, Erdbeeren 12.100 / 8.100 / 6.400 bei trocken (p = 0,1), mild (0,3), feucht (0,6). Nutzenfunktion \(u(e) = \sqrt{e}\).',
              [('Nutzenmatrix: Weizen 40 / 60 / 100, Erdbeeren 110 / 90 / 80', ''), (r'Weizen: \(0{,}1 \cdot 40 + 0{,}3 \cdot 60 + 0{,}6 \cdot 100 = 4 + 18 + 60\)', '82'),
               (r'Erdbeeren: \(0{,}1 \cdot 110 + 0{,}3 \cdot 90 + 0{,}6 \cdot 80 = 11 + 27 + 48\)', '86')], 'Erdbeeren bringen den höheren erwarteten Nutzen.')
        + falle('Die Wahrscheinlichkeiten auf die Geldbeträge anwenden und danach erst die Nutzenfunktion. Richtig: zuerst Nutzen, dann Erwartungswert.')
        + wahr('w-ber', [('Beim Bernoulli-Prinzip zählt der erwartete Nutzen, nicht der erwartete Geldbetrag.', True, 'So wird die Risikoeinstellung berücksichtigt.'),
                         ('Im Folienbeispiel gewinnt a2, weil es das höchste Einzelergebnis hat.', False, 'a3 hat den höchsten Erwartungsnutzen (10.100).')]),
    merk='Bernoulli: 1) Nutzenmatrix u(e_ij), 2) Erwartungsnutzen Σ p_j · u(e_ij), höchsten wählen. Berücksichtigt die Risikoeinstellung (abnehmender Nutzen des Geldes).',
    exam='Nutzenmatrix aufstellen und Erwartungsnutzen vergleichen.',
    fehler=['Erst Erwartungswert, dann Nutzenfunktion rechnen.'],
    src='Folien 213–217')

KAPITEL = kapitel('k7', 'Entscheidungen unter Ungewissheit und Risiko',
    'Welche Alternative wählt man, wenn die Zukunft offen ist? Dominanzregeln, Regeln unter Ungewissheit (Maximin, Maximax, Hurwicz, Savage-Niehans, Laplace) und unter Risiko (Bayes, Bernoulli). Durchgehendes Beispiel: die Eisdiele und ihre Strategien.',
    ['Dominanz', 'Maximin/Maximax', 'Hurwicz', 'Savage-Niehans', 'Laplace', 'Bayes', 'Bernoulli'],
    [t_dom, t_maxi, t_hur, t_sav, t_lap, t_bay, t_ber])

from mehr2 import ergaenze
ergaenze(KAPITEL)
