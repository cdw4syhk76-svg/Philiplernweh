import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *

# Durchgehendes Beispiel: Die Eisdiele „Gelato Quadrat“ sucht einen Standort und legt ihr Sortiment fest.

# ---------------------------------------------------------------- 1 Überblick
fig_et = svg(360, 240,
    box(110, 6, 140, 40, 'Entscheidungs-\ntheorie', size=13, art='pale', tip='Sie hilft, Entscheidungen ex ante (vorher) analytisch zu durchdringen und ex post (danach) zu erklären.')
    + pfeil(150, 48, 90, 66) + pfeil(210, 48, 270, 66)
    + box(4, 68, 172, 164, 'Klassische ET\n\npräskriptiv\nnormativ\nEntscheidungslogik\nDecision science\nRational Choice\nformale ET', size=13, art='hl', tip='Die klassische Entscheidungstheorie sagt, wie man rational entscheiden SOLL (präskriptiv, normativ). Grundlage: homo oeconomicus.')
    + box(184, 68, 172, 164, 'Verhaltenswiss. ET\n\ndeskriptiv\n\nbeschreibt, wie\nMenschen wirklich\nentscheiden', size=13, tip='Die verhaltenswissenschaftliche Entscheidungstheorie beschreibt, wie Menschen tatsächlich entscheiden (deskriptiv): begrenzt rational, mit typischen Mustern.'),
    'Zwei Richtungen der Entscheidungstheorie', maxw=420)

t_et = thema('et-ueberblick', 'Entscheidungstheorie: Ziel und zwei Richtungen',
    kern='Die Entscheidungstheorie hilft, Entscheidungen vorher (ex ante) zu durchdringen und hinterher (ex post) zu erklären. Die klassische ET ist präskriptiv (wie man entscheiden soll), die verhaltenswissenschaftliche deskriptiv (wie man wirklich entscheidet).',
    kurz=p('Wo soll die Eisdiele hin, welche Sorten soll sie anbieten? Bevor man entscheidet, hilft es, das Problem zu <b>sortieren</b>: Was will ich, welche Möglichkeiten habe ich, was kann passieren? Erst dann wird entschieden.')
        + p('Die <b>klassische Entscheidungstheorie</b> sagt, wie ein rationaler Mensch entscheiden <b>soll</b>. Die <b>verhaltenswissenschaftliche</b> beschreibt, wie Menschen tatsächlich entscheiden.'),
    fig=fw('Die zwei Richtungen mit ihren Synonymen. Tippe auf die Kästen.') + bild(fig_et),
    figcap='nach Folie „Zielsetzung und Übersicht“',
    article=h3('Wozu Entscheidungstheorie?')
        + cards([('ex ante (vorher)', 'Entscheidungssituationen analytisch durchdringen: Was steht zur Wahl, was ist mir wichtig, was kann passieren?'), ('ex post (danach)', 'getroffene Entscheidungen erklären: Warum wurde so entschieden?')])
        + p('Vorgehen in <b>zwei Stufen</b>: 1) sortieren (Strukturierung des Entscheidungsproblems), 2) dann erst entscheiden (Lösungsfindung).')
        + weiter('Es gibt zwei große Richtungen, mit vielen Namen.')
        + h3('Klassische und verhaltenswissenschaftliche Entscheidungstheorie')
        + tabelle(['', 'Klassische ET', 'Verhaltenswissenschaftliche ET'], [
            ['Synonyme', 'präskriptive ET, normative ET, Entscheidungslogik, Decision science, Rational Choice, formale ET', 'deskriptive ET'],
            ['Frage', 'Wie soll man rational entscheiden?', 'Wie entscheiden Menschen tatsächlich?'],
            ['Menschenbild', 'homo oeconomicus', 'begrenzt rationaler Mensch']])
        + p('Grundlage der klassischen ET sind die Annahmen des homo oeconomicus: Er kann Ziele spezifizieren, Nutzenfunktionen ableiten, alle Alternativen und Umweltzustände kennen, alle Konsequenzen berechnen, alle Informationen kostenlos verarbeiten und wählt das Beste.')
        + wahr('w-et', [('Die klassische Entscheidungstheorie ist präskriptiv.', True, 'Sie sagt, wie man entscheiden soll.'),
                        ('Die verhaltenswissenschaftliche ET heißt auch Rational Choice.', False, 'Rational Choice ist ein Synonym der klassischen ET.'),
                        ('Ex post heißt: Entscheidungen im Nachhinein erklären.', True, 'Ex ante = vorher.')]),
    merk='Entscheidungstheorie: ex ante durchdringen, ex post erklären; erst strukturieren, dann lösen. Klassisch = präskriptiv/normativ (Rational Choice, Entscheidungslogik); verhaltenswissenschaftlich = deskriptiv.',
    exam='Synonyme und Ziel der beiden Richtungen zuordnen.',
    fehler=['Präskriptiv und deskriptiv vertauschen.'],
    src='Folien 169–172')

# ---------------------------------------------------------------- 2 Struktur des Entscheidungsproblems
fig_struk = svg(360, 300,
    box(90, 4, 180, 40, 'Standortentscheidung', size=13, art='pale')
    + rechteck(4, 54, 352, 176, 'var(--pale-2)', 'var(--line)')
    + T(12, 72, 'Stufe 1: Strukturierung', 13, 800, 'start')
    + box(12, 84, 160, 136, 'Zielsystem\n(Präferenzen)\n\n· Kaufpreis\n· Verkehrsanbindung\n· politischer Einfluss', size=12, tip='Was will ich erreichen? Monetäre Ziele (Kaufpreis), Verkehrsanbindung (möglichst gut), politische Einflussnahme (hoch).')
    + box(188, 84, 160, 62, 'Alternativen\nInnenstadt · Stadtrand\n· Vorort', size=12, art='hl', tip='Das Entscheidungsfeld enthält die Handlungsalternativen: Was kann ich tun?')
    + box(188, 154, 160, 66, 'Umwelteinflüsse\nImmobilienkonjunktur\nSchnellstraße kommt?', size=12, tip='Nicht beeinflussbare Umweltzustände: Immobilienkonjunktur, Bau einer Schnellstraße, Termin der Gemeinderatssitzung.')
    + T(348, 72, 'Entscheidungsfeld', 12, 700, 'end', 'var(--muted)')
    + pfeil(180, 232, 180, 248)
    + box(4, 250, 352, 44, 'Stufe 2: Lösungsfindung', size=13, tip='Erst wenn das Problem sortiert ist, wird mit Entscheidungsregeln eine Lösung gesucht.'),
    'Aufbau eines Entscheidungsproblems', maxw=420)

t_struk = thema('et-struktur', 'Das Entscheidungsproblem strukturieren',
    kern='Stufe 1 strukturiert das Problem: Zielsystem (Präferenzen) und Entscheidungsfeld (Alternativen und Umwelteinflüsse). Stufe 2 ist die Lösungsfindung. Bei der Suche nach Alternativen braucht man ein Abbruchkriterium.',
    kurz=p('Die Eisdiele sucht einen Standort. Zuerst schreibt sie auf, <b>was sie will</b>: niedriger Kaufpreis, gute Verkehrsanbindung. Das ist das <b>Zielsystem</b>. Dann, <b>was sie tun kann</b>: Innenstadt, Stadtrand oder Vorort, die <b>Alternativen</b>. Und <b>was passieren kann</b>, ohne dass sie es beeinflusst: Kommt die neue Schnellstraße? Das sind die <b>Umwelteinflüsse</b>.')
        + p('Alternativen und Umwelt zusammen heißen <b>Entscheidungsfeld</b>. Erst wenn alles sortiert ist, folgt Stufe 2: die Lösung.'),
    fig=fw('Das Standortbeispiel der Vorlesung. Tippe auf die Kästen.') + bild(fig_struk),
    figcap='nach Folien „Klassische Entscheidungstheorie“',
    article=h3('Stufe 1: Strukturierung')
        + tabelle(['Baustein', 'Frage', 'Standortbeispiel'], [
            ['Zielsystem (Präferenzen)', 'Was will ich?', 'Kaufpreis (monetär), Verkehrsanbindung (möglichst gut), politische Einflussnahme (hoch)'],
            ['Alternativen', 'Was kann ich tun?', 'Innenstadt, Stadtrand, Vorort'],
            ['Umwelteinflüsse', 'Was passiert, ohne dass ich es beeinflussen kann?', 'Immobilienkonjunktur, Bau einer Schnellstraße, Termin der nächsten Gemeinderatssitzung']])
        + p('Je genauer die Struktur, desto besser die Lösungsansätze.')
        + zusatz('Einflussdiagramme zeichnen (Symbole für Entscheidung, Zielvariable, Zufallsereignis und Einfluss) ist laut Vorlesung nicht klausurrelevant.')
        + weiter('In Stufe 2 geht es um drei Bausteine: Handlungsalternativen, Zielsystem und Umweltereignisse.')
        + h3('Stufe 2: Lösungsfindung und die Suche nach Alternativen')
        + p('Wie lange soll man nach Alternativen suchen? Der homo oeconomicus hat den vollen Überblick über den Markt, wir nicht. Jede weitere Suche kostet Zeit und Geld, bringt aber vielleicht eine bessere Lösung. Man sucht so lange, bis der Aufwand den zusätzlichen Nutzen übersteigt: <b>Abbruchkriterium</b>.')
        + cards([('Vollständigkeit vs. Übersichtlichkeit', 'Alle Möglichkeiten erfassen oder den Überblick behalten?'), ('Suchkosten vs. Verbesserungspotenzial', 'Lohnt die weitere Suche?'), ('Realität vs. Fantasie', 'Nur realistische, umsetzbare Optionen aufnehmen.')])
        + p('Die Zielsysteme (Zielbeziehungen und wie man mit mehreren Zielen umgeht) und die Umweltereignisse (Entscheidungsregeln) folgen in den nächsten Unterthemen.')
        + wahr('w-struk', [('Alternativen und Umwelteinflüsse bilden zusammen das Entscheidungsfeld.', True, 'Das Zielsystem steht daneben.'),
                           ('Umwelteinflüsse kann der Entscheider steuern.', False, 'Sie sind nicht beeinflussbar.'),
                           ('Bei der Suche nach Alternativen braucht man ein Abbruchkriterium.', True, 'Suchkosten vs. Verbesserungspotenzial.')]),
    merk='Stufe 1 Strukturierung: Zielsystem (Präferenzen) + Entscheidungsfeld (Alternativen, Umwelteinflüsse). Stufe 2 Lösungsfindung. Alternativensuche: Abbruchkriterium (Suchkosten vs. Verbesserung, Vollständigkeit vs. Übersicht, Realität vs. Fantasie).',
    exam='Bestandteile eines Entscheidungsproblems an einem Beispiel zuordnen.',
    fehler=['Umwelteinflüsse zu den Alternativen zählen.'],
    src='Folien 174–185')

# ---------------------------------------------------------------- 3 Zielbeziehungen
def ziel_mini(x, titel, art, tip, hl=False):
    s = rechteck(x, 30, 112, 120, 'var(--card)', 'var(--primary)' if hl else 'var(--line)')
    s += pfeil(x + 16, 134, x + 104, 134) + pfeil(x + 16, 134, x + 16, 42)
    s += T(x + 102, 148, 'Ziel 1', 12, 600, 'end', 'var(--muted)') + T(x + 20, 44, 'Ziel 2', 12, 600, 'start', 'var(--muted)')
    if art == 'k':
        s += linie([(x + 22, 126), (x + 92, 58)], 'var(--c2)', 3)
    elif art == 'z':
        s += linie([(x + 22, 58), (x + 90, 120)], 'var(--neg)', 3)
    else:
        s += linie([(x + 22, 92), (x + 96, 92)], 'var(--c3)', 3)
    return tpg(s + T(x + 56, 18, titel, 13, 800), tip)

fig_ziel = svg(360, 200,
    ziel_mini(4, 'komplementär', 'k', 'Komplementäre Ziele: Je mehr Ziel 1 erreicht wird, desto mehr auch Ziel 2. Beispiel: Kostensenkung und Gewinn.')
    + ziel_mini(124, 'konkurrierend', 'z', 'Konkurrierende Ziele (Zielkonkurrenz): Die Erreichung des einen Ziels geht zu Lasten des anderen. Beispiel: mehr Qualität und weniger Kosten.', True)
    + ziel_mini(244, 'indifferent', 'n', 'Indifferente (neutrale) Ziele: Die Erreichung hat keinen Einfluss aufeinander. Beispiel: Kostensenkung in der Produktion und neue Kasse in der Kantine.')
    + T(180, 178, 'je mehr Ziel 1, desto … Ziel 2', 13, 700, 'middle', 'var(--muted)'),
    'Drei Zielbeziehungen', maxw=420)

t_ziel = thema('zielbeziehungen', 'Zielbeziehungen: komplementär, konkurrierend, indifferent', star=True,
    kern='Ziele können komplementär sein (fördern sich gegenseitig), konkurrierend (das eine geht zu Lasten des anderen: Zielkonkurrenz) oder indifferent (beeinflussen sich nicht).',
    kurz=p('Die Eisdiele will <b>bessere Qualität</b> (Bio-Milch) und <b>niedrigere Kosten</b>. Beides zugleich geht schlecht: Bio-Milch ist teurer. Diese Ziele <b>konkurrieren</b>.')
        + p('Andere Ziele helfen sich gegenseitig: Weniger Kosten bedeuten mehr Gewinn, sie sind <b>komplementär</b>. Und manche haben nichts miteinander zu tun, etwa eine neue Kasse und die Sorte des Monats: <b>indifferent</b>.'),
    fig=fw('Die drei Zielbeziehungen wie auf der Folie. Tippe auf die Bilder.') + bild(fig_ziel),
    figcap='nach Folie „Klassische Entscheidungstheorie: Zielsystem“',
    article=h3('Drei Zielformen')
        + tabelle(['Zielbeziehung', 'Bedeutung', 'Beispiel'], [
            ['komplementär', 'je mehr Ziel 1, desto mehr Ziel 2', 'Kostensenkung und Gewinn; Umsatz und Gewinn'],
            ['konkurrierend (Zielkonkurrenz)', 'Zielerreichung des einen geht zu Lasten des anderen', 'mehr Qualität und weniger Kosten; günstige Produktion und beste Qualität'],
            ['indifferent (neutral)', 'die Ziele haben keinen Einfluss aufeinander', 'Kostensenkung in der Produktion und neue Kasse in der Kantine']])
        + klausur_hinweis('Auswahlfrage „Zielformen“ und „Zielkonkurrenz“: Bei Zielkonkurrenz verschlechtert die Verbesserung des einen Ziels das andere.')
        + weiter('Problematisch sind konkurrierende Ziele: Man muss sich entscheiden. Wie, zeigt das nächste Unterthema.')
        + falle('„Konkurrierend“ mit „zwei Unternehmen konkurrieren“ verwechseln. Gemeint ist das Verhältnis zweier Ziele desselben Entscheiders.')
        + wahr('w-ziel', [('Umsatz und Gewinn sind typischerweise komplementäre Ziele.', True, 'Mehr Umsatz bringt meist mehr Gewinn.'),
                          ('Bei Zielkonkurrenz kann man beide Ziele gleichzeitig voll erreichen.', False, 'Das eine geht zu Lasten des anderen.'),
                          ('Indifferente Ziele beeinflussen sich nicht.', True, 'Neutral.')]),
    merk='Komplementär: fördern sich. Konkurrierend (Zielkonkurrenz): eins geht zu Lasten des anderen. Indifferent: kein Einfluss aufeinander.',
    exam='Zielbeziehungen an Beispielen erkennen (Auswahlfrage zur Zielkonkurrenz).',
    fehler=['Komplementär und konkurrierend vertauschen.'],
    src='Folien 186–187')

# ---------------------------------------------------------------- 4 Mehrere Ziele: Lösungen (Rechner Nutzenfunktion)
TAB = tabelle(['', 'Preis', 'Absatz', 'Gewinn', 'Umweltschäden'], [['a1', '15', '800', '7.000', '−4'], ['a2', '20', '600', '7.000', '−2'], ['a3', '25', '400', '6.000', '0'], ['a4', '30', '200', '4.000', '0']])

t_loes = thema('zielsystem', 'Mehrere Ziele: Dominanz, Effizienz, Lexikographie, Nutzenfunktion', star=True, wide=True,
    kern='Bei mehreren Zielen hilft: Zieldominanz (ein Ziel entscheidet), effiziente Alternativen (keine andere ist besser, ohne irgendwo schlechter zu sein), lexikographische Ordnung (Ziele der Reihe nach) oder eine Nutzenfunktion (Ziele gewichten, vorher normieren).',
    kurz=p('Die Eisdiele hat vier Preisvarianten mit verschiedenem Absatz, Gewinn und Umweltschaden. Welche ist die beste? Das hängt davon ab, wie man die Ziele zusammenführt.')
        + p('Vier Wege: Ein Ziel <b>dominiert</b>. Man streicht Alternativen, die überall schlechter sind (<b>Effizienz</b>). Man geht die Ziele <b>der Reihe nach</b> durch (lexikographisch). Oder man <b>gewichtet</b> die Ziele in einer Nutzenfunktion.'),
    fig=fw('Rechner zur Nutzenfunktion: zwei Alternativen, zwei Ziele. Schiebe die Gewichtung und vergleiche die drei Lösungswege.')
        + regler([('nfW', 'Gewicht Umsatz (Rest: Gewinn)', 0, 100, 5, 25, '%')])
        + '<svg id="figNF" viewBox="0 0 360 250" style="max-width:420px;width:100%;margin:0 auto;display:block" role="img" aria-label="Nutzenwerte nach drei Methoden"></svg>'
        + schritte_karten([('① einfache Multiplikation', 'nfR1', '#nfT1'), ('② einfache Normierung', 'nfR2', '#nfT2'), ('③ Normierung', 'nfR3', '#nfT3')]),
    figcap='Folienbeispiel: a1 = 800.000 € Umsatz / 7.000 € Gewinn, a2 = 600.000 € / 8.000 €',
    article=h3('Das Beispiel')
        + TAB
        + weiter('Vier Lösungswege für dieselbe Tabelle.')
        + h3('Zieldominanz')
        + p('„Zieldominanz besteht dann, wenn ein Ziel als entscheidend betrachtet wird und dessen Erfüllung als wichtiger als die Erfüllung anderer Ziele erachtet wird.“ Ist der <b>Absatz</b> das dominante Ziel, wählt man <b>a1</b> (höchster Absatz, 800).')
        + h3('Effiziente Alternativen')
        + p('„Eine Alternative ist effizient, wenn es keine andere Alternative gibt, die bezüglich mindestens eines Ziels besser und bezüglich keines Ziels schlechter ist.“')
        + bsp('Effizienz prüfen', 'Ziele: Absatz, Gewinn, Umweltschäden (je höher, desto besser; −4 ist schlechter als 0).',
              [('a1 gegen a2: a1 hat mehr Absatz, aber mehr Umweltschaden.', 'keine ist besser'), ('a3 gegen a4: a3 hat mehr Absatz und Gewinn, gleich wenig Umweltschaden.', 'a3 dominiert a4'), ('Keine Alternative ist allen anderen überlegen; a4 fällt weg.', 'effizient: a1, a2, a3')],
              'Hätte a1 keinen Umweltschaden (0), wäre a1 allen überlegen.')
        + h3('Lexikographische Ordnung')
        + p('„Ziele werden vollständig priorisiert und so als absteigende Entscheidungskriterien nutzbar gemacht.“ Ist der <b>Gewinn</b> am wichtigsten, fliegen a3 und a4 raus (7.000 bei a1 und a2). Zweitwichtigstes Ziel Umweltschäden: a2 (−2) schlägt a1 (−4). Es gewinnt <b>a2</b>.')
        + weiter('Die Nutzenfunktion ist der rechnerische Weg. Dabei ist das Normieren entscheidend.')
        + h3('Nutzenfunktion: drei Rechenwege')
        + p('„Den Zielen werden Nutzengewichte zugeordnet und deren Ergebniswerte verglichen.“ Beispiel: a1 (Umsatz 800.000, Gewinn 7.000), a2 (600.000, 8.000), Gewichtung Umsatz 25 %, Gewinn 75 %.')
        + bsp('Lösung 1: einfache Multiplikation', 'Gewicht mal Wert, addieren.',
              [(r'a1: \(0{,}25 \cdot 800.000 + 0{,}75 \cdot 7.000\)', '205.250'), (r'a2: \(0{,}25 \cdot 600.000 + 0{,}75 \cdot 8.000\)', '156.000')],
              'a1 gewinnt, aber nur, weil die Umsatzzahlen so groß sind: Der Gewinn kommt gar nicht zum Tragen. Deshalb normieren.')
        + bsp('Lösung 2: einfache Normierung', 'Der höhere Wert wird 1, der niedrigere 0.',
              [(r'a1: \(0{,}25 \cdot 1 + 0{,}75 \cdot 0\)', '0,25'), (r'a2: \(0{,}25 \cdot 0 + 0{,}75 \cdot 1\)', '0,75')], 'a2 gewinnt. Aber Informationen gehen verloren: Wie weit die Werte auseinanderliegen, zählt nicht mehr.')
        + bsp('Lösung 3: Normierung', 'Jeder Wert wird durch den höchsten Wert geteilt. So bleibt die Relation der Zahlen erhalten.',
              [(r'Umsatz: a1 \(\frac{800}{800} = 1\), a2 \(\frac{600}{800} = 0{,}75\); Gewinn: a1 \(\frac{7.000}{8.000} = 0{,}875\), a2 = 1', ''),
               (r'a1: \(0{,}25 \cdot 1 + 0{,}75 \cdot 0{,}875\)', '≈ 0,906'), (r'a2: \(0{,}25 \cdot 0{,}75 + 0{,}75 \cdot 1\)', '0,9375')],
              'a2 ist die bessere Alternative. Hohe absolute Zahlen „ertränken“ das Ergebnis nicht mehr.')
        + klausur_hinweis('„Bestimmung des Zielsystems: Welche Aussage passt?“ Kenne die vier Wege und ihre Logik: dominant = ein Ziel entscheidet; effizient = nicht dominiert; lexikographisch = Ziele nacheinander; Nutzenfunktion = gewichten nach Normierung.')
        + wahr('w-loes', [('Bei der lexikographischen Ordnung werden die Ziele nacheinander nach Wichtigkeit abgearbeitet.', True, 'Absteigende Entscheidungskriterien.'),
                          ('Bei einfacher Multiplikation können große Zahlen kleinere Ziele überdecken.', True, 'Darum normiert man.'),
                          ('Eine Alternative ist effizient, wenn sie in allen Zielen die beste ist.', False, 'Effizient heißt: Keine andere ist irgendwo besser, ohne woanders schlechter zu sein.')]),
    merk='Zieldominanz: ein Ziel entscheidet. Effizient: keine andere Alternative ist in einem Ziel besser und in keinem schlechter. Lexikographisch: Ziele nach Rang abarbeiten. Nutzenfunktion: gewichten, vorher normieren (Wert ÷ Maximum), sonst überdecken große Zahlen.',
    exam='Eine Alternative nach Zieldominanz, Effizienz, lexikographischer Ordnung oder gewichteter Nutzenfunktion auswählen.',
    fehler=['Ohne Normierung gewichten.', 'Effizient mit „überall am besten“ verwechseln.'],
    src='Folien 188–192')

KAPITEL = kapitel('k6', 'Entscheidungstheorie: Aufbau und Zielsysteme',
    'Wie strukturiert man eine Entscheidung, und was tut man, wenn mehrere Ziele gelten? Durchgehendes Beispiel: die Eisdiele „Gelato Quadrat“.',
    ['Überblick', 'Struktur', 'Zielbeziehungen', 'Mehrere Ziele'],
    [t_et, t_struk, t_ziel, t_loes])

from mehr1 import ergaenze
ergaenze(KAPITEL)
