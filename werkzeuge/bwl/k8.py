import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *

# Durchgehendes Beispiel: Alltagsentscheidungen von Studierenden (Tasse aus dem College-Shop, Tennishalle, Lotterie).

# ---------------------------------------------------------------- 1 Begrenzte Rationalität
fig_bounded = svg(360, 236,
    box(4, 6, 352, 52, 'begrenzte Rationalität (bounded rationality)', size=13, art='hl', tip='Individuen handeln intentional rational, stoßen dabei aber an Grenzen. Sie entscheiden auf Basis eines begrenzten, vereinfachten Modells.')
    + pfeil(180, 60, 180, 76)
    + box(4, 78, 112, 80, 'unvollständiges\nWissen', size=13, tip='Man kennt nicht alle Informationen.')
    + box(124, 78, 112, 80, 'nicht alle\nOptionen\nerfassbar', size=13, tip='Es ist schwierig, alle Handlungsoptionen zu erfassen.')
    + box(244, 78, 112, 80, 'instabile\nPräferenzen', size=13, tip='Was man will, ändert sich (Tagesform, Stimmung).')
    + pfeil(180, 160, 180, 176)
    + box(4, 178, 352, 52, 'Ziel-Mittel-Ergebnis-Verbindung\nnicht wirklich überblickbar', size=13, art='pale'),
    'Begrenzte Rationalität', maxw=420)

t_bounded = thema('begrenzte-rationalitaet', 'Begrenzte Rationalität',
    kern='Menschen handeln intentional rational, stoßen aber an Grenzen: unvollständiges Wissen, nicht alle Optionen erfassbar, instabile Präferenzen. Sie entscheiden auf Basis eines vereinfachten Modells. Das ist die Grundlage der verhaltenswissenschaftlichen Entscheidungstheorie.',
    kurz=p('Wir sind keine würfelnden Affen: Wir wollen vernünftig entscheiden. Aber wir kennen nicht alle Angebote, können nicht alles durchrechnen und wissen morgen vielleicht nicht mehr, was wir heute wollten. Das nennt man <b>begrenzte Rationalität</b> (bounded rationality). Das sind wir.'),
    fig=fw('Warum Rationalität begrenzt ist. Tippe auf die Kästen.') + bild(fig_bounded),
    figcap='nach Folie „Verhaltenswissenschaftliche Entscheidungstheorie: Begrenzte Rationalität“',
    article=h3('Die Begründer')
        + tabelle(['Person', 'Werk'], [['Chester I. Barnard (1886–1961)', '„The Functions of the Executive“'], ['Herbert A. Simon (1916–2001, Nobelpreis 1978)', '„Administrative Behavior“'],
                                       ['James G. March (geb. 1928)', 'mit Simon: „Organizations“'], ['Richard M. Cyert (1921–1998)', 'mit March: „A Behavioral Theory of the Firm“'],
                                       ['Daniel Kahneman (geb. 1934, Nobelpreis 2002)', 'Prospect Theory']])
        + weiter('Was heißt begrenzt rational genau?')
        + h3('Begrenzte Rationalität')
        + p('„Das Konzept der begrenzten Rationalität beschreibt Individuen, die zwar intentional rational handeln, aufgrund ihres unvollständigen Wissens, der Schwierigkeit, alle Handlungsoptionen zu erfassen, und ihrer instabilen Präferenzstruktur die eigentliche Ziel-Mittel-Ergebnis-Verbindung tatsächlich nicht überblicken können.“')
        + liste(['Individuen handeln intentional rational (keine würfelnden Affen),', 'stoßen dabei aber auf Grenzen (Grenzen des homo oeconomicus),', 'Entscheidungsfindung auf Basis eines begrenzten, simplifizierten Modells.'])
        + zusatz('Betriebliche Entscheidungshilfen (Arbeitsteilung, Standardisierung, Hierarchie, kanalisierte Kommunikation), individuelle Entscheidungsmuster (Satisficing, Anspruchsniveaus, Situationsdefinition, habituelles Verhalten), die Anreiz-Beitrags-Theorie und die Würdigung sind in den Folien durchgestrichen.')
        + wahr('w-bound', [('Begrenzt rationale Menschen handeln zufällig.', False, 'Sie wollen rational handeln, stoßen aber an Grenzen.'),
                           ('Herbert Simon gehört zu den Begründern der verhaltenswissenschaftlichen Entscheidungstheorie.', True, 'Nobelpreis 1978.')]),
    merk='Begrenzte Rationalität: intentional rational, aber unvollständiges Wissen, nicht alle Optionen erfassbar, instabile Präferenzen → vereinfachtes Modell. Begründer: Barnard, Simon, March, Cyert; Kahneman (Prospect Theory).',
    exam='Begrenzte Rationalität erklären und vom homo oeconomicus abgrenzen.',
    fehler=['Begrenzte Rationalität mit Irrationalität gleichsetzen.'],
    src='Folien 221–223')

# ---------------------------------------------------------------- 2 Prospect Theory
def wertfunktion():
    X = lambda x: 180 + x * 1.5
    Y = lambda v: 120 - v * 1.5
    s = pfeil(20, 120, 346, 120) + pfeil(180, 226, 180, 10)
    s += T(342, 112, 'Gewinne', 12, 700, 'end', 'var(--muted)') + T(24, 112, 'Verluste', 12, 700, 'start', 'var(--muted)') + T(186, 18, 'Wert', 12, 700, 'start', 'var(--muted)')
    gew = [(X(x), Y(60 * (1 - math.exp(-x / 45)))) for x in range(0, 111, 4)]
    ver = [(X(-x), Y(-2.25 * 60 * (1 - math.exp(-x / 45)) * 0.7)) for x in range(0, 101, 4)]
    s += tpg(linie(gew, 'var(--c2)', 3), 'Gewinnbereich: flach und nach unten gekrümmt. Ein sicherer Gewinn wird vorgezogen: risikoscheu im Gewinnfall.')
    s += tpg(linie(ver, 'var(--neg)', 3), 'Verlustbereich: steiler. Verluste schmerzen etwa doppelt so stark, wie gleich große Gewinne freuen. Man spielt lieber, um den Verlust zu vermeiden: risikofreudig im Verlustfall.')
    s += punkt(180, 120, 'var(--primary)', 6) + T(188, 138, 'Referenzpunkt', 12, 700, 'start', 'var(--primary)')
    s += T(300, 104, 'risikoscheu', 13, 800, 'middle', 'var(--c2)') + T(76, 154, 'risikofreudig', 13, 800, 'middle', 'var(--neg)')
    return svg(360, 232, s, 'Wertfunktion der Prospect Theory', maxw=420)

t_prospect = thema('prospect-theory', 'Prospect Theory und typische Denkfehler',
    kern='Nach der Prospect Theory sind Menschen bei Gewinnen risikoscheu und bei Verlusten risikofreudig; Verluste wiegen schwerer als gleich große Gewinne. Dazu kommen Besitztumseffekt, Ankereffekt, Overconfidence Bias und Sunk-Cost-Effekt.',
    kurz=p('Würdest du lieber <b>sicher 240 €</b> nehmen oder eine <b>25 %-Chance auf 1.000 €</b>? Die meisten nehmen die 240 €, obwohl die Chance im Schnitt 250 € wert ist. Menschen wollen nicht verlieren, was sie haben: Im Gewinnfall sind sie <b>risikoscheu</b>.')
        + p('Umgekehrt: <b>sicher 750 € verlieren</b> oder <b>75 % Chance, 1.000 € zu verlieren</b>, und 25 %, nichts zu verlieren? Jetzt spielen die meisten („gambling on losses“): Im Verlustfall sind sie <b>risikofreudig</b>. Das beschreibt die <b>Prospect Theory</b> von Kahneman und Tversky.'),
    fig=fw('Die Wertfunktion: Gewinne flach, Verluste steil. Tippe auf die Kurven.') + bild(wertfunktion()),
    figcap='nach Folie „Weiterentwicklung: Prospect Theory“ (Wertfunktion)',
    article=h3('Die Experimente')
        + tabelle(['Fall', 'Variante 1', 'Variante 2', 'Wahl der meisten'], [
            ['Gewinn', 'sicherer Gewinn von 240 €', '25 % Chance auf 1.000 €, 75 % nichts (Erwartungswert 250 €)', 'Variante 1 (ca. 80 %): risikoscheu'],
            ['Verlust', 'sicherer Verlust von 750 €', '75 % Chance, 1.000 € zu verlieren, 25 % nichts (Erwartungswert −750 €)', 'Variante 2: risikofreudig']])
        + p('Rational wäre im Gewinnfall Variante 2 (Erwartungswert 250 > 240). Menschen wollen aber nicht verlieren, was sie sicher haben könnten.')
        + bsp('Asiatische Grippe (Framing)', 'Eine Grippewelle bedroht 600 Menschen.',
              [('Positiv formuliert: A rettet sicher 200 Menschen; B rettet mit 33 % alle 600, mit 66 % niemanden. Die meisten wählen A.', 'risikoscheu'),
               ('Negativ formuliert: Mit C sterben sicher 400 Menschen; mit D stirbt mit 33 % niemand, mit 66 % sterben alle 600. Die meisten wählen D.', 'risikofreudig')],
              'A und C sind dasselbe, B und D auch. Nur die Formulierung (Gewinn oder Verlust) ändert die Wahl: Der Referenzpunkt kann sprachlich verschoben werden.')
        + weiter('Neben der Prospect Theory gibt es weitere typische Muster.')
        + h3('Weitere Effekte')
        + cards([('Besitztumseffekt', 'Was man besitzt, bewertet man höher. Bekommt die Hälfte der Klasse eine Tasse aus dem College-Shop, verlangen die Besitzer viel mehr dafür, als die anderen zahlen wollen.'),
                 ('Ankereffekt', 'Eine vorher gesehene Zahl beeinflusst die Schätzung. Steht 7.500 an der Tafel, schätzen viele die Länge eines erfundenen Flusses auf etwa 7.500 km.'),
                 ('Overconfidence Bias', 'Man überschätzt sich und seine Erfahrung.'),
                 ('Sunk-Cost-Effekt', 'Bereits bezahltes Geld beeinflusst die Entscheidung, obwohl es weg ist. Die Tennishalle ist bezahlt, also spielt man drinnen, obwohl draußen die Sonne scheint.')])
        + p('Daraus folgt: Der Mensch handelt nicht immer rational, aber er folgt <b>Mustern</b>. Diese Muster kann man kennen und nutzen.')
        + wahr('w-pt', [('Im Gewinnfall sind Menschen laut Prospect Theory risikofreudig.', False, 'Risikoscheu; risikofreudig im Verlustfall.'),
                        ('Der Sunk-Cost-Effekt beschreibt, dass bereits bezahlte Kosten die Entscheidung beeinflussen.', True, 'Tennishalle.'),
                        ('Beim Ankereffekt beeinflusst eine vorher genannte Zahl die Schätzung.', True, '7.500 an der Tafel.')]),
    merk='Prospect Theory: Gewinnfall risikoscheu, Verlustfall risikofreudig („gambling on losses“); Verluste wiegen schwerer; Referenzpunkt sprachlich verschiebbar (Framing). Besitztums-, Anker-, Overconfidence-, Sunk-Cost-Effekt.',
    exam='Effekte an Beispielen erkennen; Risikoverhalten bei Gewinn und Verlust.',
    fehler=['Risikoverhalten bei Gewinn und Verlust vertauschen.'],
    src='Folien 228–231')

# ---------------------------------------------------------------- 3 Garbage Can
fig_gc = svg(360, 256,
    box(4, 6, 112, 46, 'Teilnehmer', size=13, tip='Wer gerade dabei ist, wechselt; die Aufmerksamkeit auch.')
    + box(124, 6, 112, 46, 'Probleme', size=13, tip='Probleme suchen nach Gelegenheiten, behandelt zu werden.')
    + box(244, 6, 112, 46, 'Lösungen', size=13, tip='Lösungen existieren oft schon und suchen nach passenden Problemen.')
    + pfeil(60, 54, 150, 92) + pfeil(180, 54, 180, 92) + pfeil(300, 54, 210, 92)
    + box(60, 94, 240, 50, 'Entscheidungsgelegenheit\n(der „Mülleimer“)', size=13, art='hl', tip='In der Entscheidungsgelegenheit (z. B. einer Sitzung) treffen Teilnehmer, Probleme und Lösungen mehr oder weniger zufällig zusammen.')
    + pfeil(180, 146, 180, 162)
    + T(180, 178, 'Entscheidung', 13, 800)
    + box(4, 192, 112, 56, 'durch\nÜbersehen', size=13, tip='Man entscheidet, bevor das Problem überhaupt angekommen ist.')
    + box(124, 192, 112, 56, 'durch\nFlucht', size=13, tip='Das Problem wandert in eine andere Gelegenheit ab, dann wird ohne es entschieden.')
    + box(244, 192, 112, 56, 'durch Problem-\nlösung', size=13, tip='Das Problem wird tatsächlich gelöst: der seltenere Fall.'),
    'Garbage-Can-Modell', maxw=420)

t_gc = thema('garbage-can', 'Garbage-Can-Modell (Mülleimer-Modell)',
    kern='Im Garbage-Can-Modell treffen Teilnehmer, Probleme und Lösungen in Entscheidungsgelegenheiten fast zufällig zusammen. Entschieden wird durch Übersehen, durch Flucht oder (seltener) durch Problemlösung.',
    kurz=p('Wer schon einmal in einer langen Projektsitzung saß, kennt das: Es kommen andere Leute als letztes Mal, jeder bringt sein Lieblingsthema mit, und am Ende wird eine Lösung beschlossen, die schon vorher in der Schublade lag. Das <b>Garbage-Can-Modell</b> beschreibt genau das.')
        + p('Organisationale Entscheidungen sind von <b>Ambiguität</b> geprägt: Trotz aller Hilfsmittel bleibt vieles unklar.'),
    fig=fw('Das Modell. Tippe auf die Kästen.') + bild(fig_gc),
    figcap='nach Folie „Weiterentwicklung: Garbage Can-Modell“',
    article=h3('Warum ein Mülleimer?')
        + p('Organisationale Entscheidungsprozesse sind von Ambiguität geprägt. Trotz Entscheidungshilfsmitteln bleibt Unklarheit, weil:')
        + liste(['das Wissen beschränkt ist und die Technologien unvollkommen sind,', 'die Ziele inkonsistent, instabil und schlecht definiert sind,', 'Teilnehmer und Aufmerksamkeit wechseln.'])
        + p('Teilnehmer, Probleme und Lösungen werden wie in einen <b>Mülleimer</b> geworfen und finden sich in der <b>Entscheidungsgelegenheit</b> mehr oder weniger zufällig zusammen. So entstehen Lösungen für Probleme, die man am Anfang gar nicht im Blick hatte.')
        + cards([('Entscheidung durch Übersehen', 'Man entscheidet schnell, bevor das Problem in der Sitzung auftaucht.'), ('Entscheidung durch Flucht', 'Das Problem wird vertagt oder wandert in eine andere Runde; danach wird ohne es entschieden.'), ('Entscheidung durch Problemlösung', 'Das Problem wird wirklich gelöst.')])
        + zusatz('Das Fallbeispiel „Projekt Zentrale Reservierung“ und die Fragen, wie man Mülleimersituationen vermeidet oder nutzt, sind in den Folien durchgestrichen.')
        + wahr('w-gc', [('Im Garbage-Can-Modell treffen Probleme und Lösungen zufällig zusammen.', True, 'In Entscheidungsgelegenheiten.'),
                        ('Das Garbage-Can-Modell geht von klaren, stabilen Zielen aus.', False, 'Ziele sind inkonsistent, instabil, schlecht definiert.')]),
    merk='Garbage Can: Ambiguität (beschränktes Wissen, instabile Ziele, wechselnde Teilnehmer). Teilnehmer, Probleme, Lösungen treffen in Entscheidungsgelegenheiten zufällig zusammen. Entscheidung durch Übersehen, Flucht oder Problemlösung.',
    exam='Bestandteile des Garbage-Can-Modells und die drei Arten der Entscheidung kennen.',
    fehler=['Glauben, im Garbage-Can-Modell würden Probleme systematisch gelöst.'],
    src='Folien 233–234')

KAPITEL = kapitel('k8', 'Verhaltenswissenschaftliche Entscheidungstheorie',
    'Wie Menschen wirklich entscheiden: begrenzt rational, mit typischen Mustern und in chaotischen Sitzungen. Durchgehendes Beispiel: Alltagsentscheidungen von Studierenden.',
    ['Begrenzte Rationalität', 'Prospect Theory', 'Garbage Can'],
    [t_bounded, t_prospect, t_gc])

from mehr2 import ergaenze
ergaenze(KAPITEL)
