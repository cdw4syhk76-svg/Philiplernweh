import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *

# Durchgehendes Beispiel: die Brauerei „Neckarperle AG“ mit Aktionären, Mitarbeitern, Kunden, Bank und Stadt.

# ---------------------------------------------------------------- 1 homo oeconomicus, ökonomische und verhaltenswissenschaftliche BWL
fig_homo = svg(360, 280,
    box(4, 4, 352, 40, 'Wie entscheiden Menschen?', size=14, art='pale')
    + box(4, 56, 172, 150, 'Ökonomische\nPerspektive\n\nhomo oeconomicus\nrational\nNutzen maximieren', size=13, tip='Die klassische, ökonomische BWL (bis in die 1960er/70er Jahre) unterstellt den homo oeconomicus: vollständig informiert, völlig rational, maximiert seinen Nutzen.')
    + box(184, 56, 172, 150, 'Verhaltenswiss.\nPerspektive\n\nbegrenzt rational\nNutzen maximieren\nunter Nebenbed.', size=13, art='hl', tip='Die verhaltenswissenschaftliche BWL (ca. 1970–2000) sieht den Menschen realistischer: Er will rational handeln, stößt aber an Grenzen (bounded rationality) und lässt sich beeinflussen, z. B. durch Marketing.')
    + box(4, 216, 352, 58, 'seit etwa 2000: Versuch,\nbeide Perspektiven zu verbinden', size=13, tip='Heute nutzt man beide: das klare Rechenmodell und das realistische Menschenbild.'),
    'Ökonomische und verhaltenswissenschaftliche BWL', maxw=420)

t_homo = thema('homo-oeconomicus', 'Homo oeconomicus: ökonomische und verhaltenswissenschaftliche BWL',
    kern='Die ökonomische BWL unterstellt den homo oeconomicus: vollständig informiert und völlig rational. Die verhaltenswissenschaftliche BWL sieht den Menschen begrenzt rational. Seit etwa 2000 verbindet man beide Sichten.',
    kurz=p('Der <b>homo oeconomicus</b> ist eine Kunstfigur: Er weiß genau, was er will, kennt alle Angebote, rechnet alles durch und nimmt immer das Beste. Echte Menschen kaufen dagegen mal aus Laune, mal aus Gewohnheit, mal wegen der Werbung.')
        + p('Warum gibt es ihn trotzdem? Weil man mit ihm <b>leicht rechnen</b> kann. Die <b>verhaltenswissenschaftliche</b> BWL ergänzt das realistischere Bild: Wir wollen rational sein, sind es aber nur <b>begrenzt</b>. Wir sind aber auch keine „würfelnden Affen“: Unser Verhalten folgt Mustern.'),
    fig=fw('Zwei Menschenbilder. Tippe auf die Kästen.') + bild(fig_homo),
    figcap='nach Folien „Ökonomische und Verhaltenswissenschaftliche BWL“',
    article=h3('Die Annahmen des homo oeconomicus')
        + p('Der homo oeconomicus kann:')
        + liste(['Zieldimensionen spezifizieren (er weiß mit extremer Klarheit, was er will, etwa welches Produkt mit welchen Eigenschaften)', 'Nutzenfunktionen ableiten (er weiß genau, was ihm wie wichtig ist)', 'Alternativen und Umweltzustände abschließend identifizieren', 'Konsequenzen für jede Alternative und jeden Umweltzustand berechnen', 'alle Informationen kostenlos und unmittelbar verarbeiten', 'Entscheidungen treffen, die ihm den größten Nutzen oder Gewinn einbringen'])
        + p('Die sechs Punkte musst du nicht auswendig lernen. Wichtig ist der Kern: <b>vollständige Information und volle Rationalität</b>. Im echten Leben spielen bei Kaufentscheidungen viele unberechenbare Faktoren mit, etwa die Tagesform.')
        + weiter('Warum arbeitet die BWL trotzdem mit dieser Figur, und was setzt man ihr entgegen?')
        + h3('Zwei Perspektiven')
        + tabelle(['', 'Ökonomische Perspektive', 'Verhaltenswissenschaftliche Perspektive'], [
            ['Zeit', 'bis in die 1960er/Anfang 1970er', 'ca. 1970–2000'], ['Handlungsweise', 'rational (homo oeconomicus)', 'begrenzt rational (bounded rationality)'],
            ['Zielsystem', 'Nutzen maximieren', 'Nutzen maximieren unter Nebenbedingungen']])
        + p('Der homo oeconomicus macht die Berechnung leichter. Ab 1970 wollte man realistischer werden, seit etwa 2000 kombiniert man beides. Die verhaltenswissenschaftliche Sicht zeigt sich im Marketing: Wir lassen uns beeinflussen.')
        + wahr('w-homo', [('Der homo oeconomicus verarbeitet alle Informationen kostenlos und sofort.', True, 'Eine seiner Annahmen.'),
                          ('Die verhaltenswissenschaftliche BWL geht von begrenzter Rationalität aus.', True, 'Bounded rationality.'),
                          ('Der homo oeconomicus beschreibt, wie echte Menschen meistens entscheiden.', False, 'Er ist eine Kunstfigur zum Rechnen.')]),
    merk='Homo oeconomicus: vollständig informiert, völlig rational, maximiert Nutzen (Kunstfigur, erleichtert das Rechnen). Ökonomische BWL: rational; verhaltenswissenschaftliche BWL: begrenzt rational, Nutzen unter Nebenbedingungen. Seit ca. 2000 kombiniert.',
    exam='Ökonomische und verhaltenswissenschaftliche Perspektive unterscheiden; Annahmen des homo oeconomicus erkennen.',
    fehler=['Glauben, der homo oeconomicus solle echte Menschen beschreiben.'],
    src='Folien 153–155')

# ---------------------------------------------------------------- 2 Shareholder vs. Stakeholder
def sh_tafel(frage, sh, st):
    s = T(180, 18, frage, 14, 800)
    s += box(4, 32, 172, 120, 'Shareholder-Ansatz\n\n' + sh, size=13, tip='Shareholder = Anteilseigner (Aktionäre, Eigentümer).')
    s += box(184, 32, 172, 120, 'Stakeholder-Ansatz\n\n' + st, size=13, art='hl', tip='Stakeholder = alle Anspruchsgruppen: Eigentümer, Banken, Mitarbeiter, Management, Kunden, Lieferanten, Staat.')
    return svg(360, 160, s, frage, maxw=420)

t_stake = thema('stakeholder', 'Shareholder- und Stakeholder-Ansatz', star=True,
    kern='Der Shareholder-Ansatz stellt die Eigentümer in den Mittelpunkt: Ziel langfristige Gewinnmaximierung, wer das Risiko trägt, entscheidet und profitiert. Der Stakeholder-Ansatz will die Interessen aller Anspruchsgruppen ausgleichen.',
    kurz=p('Wem gehört die Brauerei Neckarperle eigentlich, und für wen soll sie arbeiten? Für die <b>Aktionäre</b>, die ihr Geld riskieren? Oder auch für Mitarbeiter, Kunden, Lieferanten, Bank und Stadt? Drei Fragen trennen die beiden Ansätze: Welche Ziele? Wer entscheidet? Wer profitiert?')
        + p('Im <b>Shareholder-Ansatz</b> zählen die Eigentümer (Shareholder). Im <b>Stakeholder-Ansatz</b> sollen alle Anspruchsgruppen (Stakeholder) angemessen beteiligt werden.'),
    fig=fw('Die drei Fragen. Schalte um und vergleiche.')
        + tafeln('tf-sh', ['Ziele', 'Entscheidung', 'Erfolg'], [
            sh_tafel('Welche Ziele verfolgt das Unternehmen?', 'langfristige\nGewinnmaxi-\nmierung', 'Ausgleich von\nInteressen'),
            sh_tafel('Wer trifft die Entscheidungen?', 'derjenige, der\ndas Risiko trägt', 'Interessens-\ngruppen'),
            sh_tafel('Wer profitiert vom Erfolg?', 'der Risikoträger\n(haftet auch\nbei Verlust)', 'Gewinn wird\naufgeteilt')]),
    figcap='nach Folien „Shareholder vs Stakeholder“',
    article=h3('Welche Ziele verfolgt das Unternehmen?')
        + gegen(('Shareholder-Ansatz', '„Die Unternehmensleitung hat die Aufgabe, unternehmerische Entscheidungen so zu treffen, dass die Einkommens- und Vermögenspositionen der Shareholder (= Eigentümer) verbessert werden.“ Ziel: <b>langfristige Gewinnmaximierung</b>.'),
                ('Stakeholder-Ansatz', '„Die Unternehmensleitung hat die Aufgabe, die Interessen der Anspruchsgruppen im Verhandlungsweg zusammenzuführen und alle Stakeholder angemessen am Unternehmenshandeln und am Unternehmenserfolg teilhaben zu lassen.“ Ziel: <b>Ausgleich von Interessen</b>.'))
        + p('Die Anspruchsgruppen haben unterschiedliche Ansprüche und leisten unterschiedliche Beiträge (die Tabelle musst du nicht auswendig lernen):')
        + tabelle(['Anspruchsgruppe', 'Anspruch', 'Beitrag'], [
            ['Eigentümer', 'Gewinn', 'Kapital (Geld)'], ['Fremdkapitalgeber (Bank)', 'Zinsen', 'Kredite'], ['Arbeitnehmer', 'möglichst hohes Gehalt', 'Arbeit, Zeit, Wissen, Expertise'],
            ['Management', 'Einfluss und Gewinn', 'Arbeit, Zeit, Verantwortung, Expertise'], ['Kunden', 'gutes Produkt zu günstigem Preis', 'Geld'],
            ['Lieferanten', 'sichere Verträge zu guten Preisen', 'Produkte'], ['Öffentlichkeit, Staat', 'Steuern', 'Straßen, Rechtssicherheit']])
        + p('Man sieht sofort den <b>Widerspruch</b> im Stakeholder-Ansatz: Kunden wollen gute Produkte zu günstigen Preisen, Mitarbeiter hohe Gehälter, Eigentümer hohen Gewinn. Alle gleichzeitig glücklich zu machen ist kaum möglich.')
        + weiter('Wenn die Ziele verschieden sind: Wer darf entscheiden?')
        + h3('Wer entscheidet, wer profitiert?')
        + tabelle(['Frage', 'Shareholder-Ansatz', 'Stakeholder-Ansatz'], [
            ['Wer trifft die Entscheidungen?', 'derjenige, der das Risiko trägt: Risikoübernahme und Entscheidungsbefugnis gehören zusammen', 'die Interessensgruppen: Risikoübernahme und Entscheidungsbefugnis sind getrennt'],
            ['Wer profitiert vom Erfolg?', 'der Risikoträger, so wie er beim Verlust mit seinem Vermögen haftet', 'der Gewinn soll zwischen den Interessengruppen aufgeteilt werden']])
        + p('Ein Argument für den Shareholder-Ansatz: Niemand wird gezwungen, für das Unternehmen zu arbeiten oder dort zu kaufen. Wer mitmacht, schließt freiwillig Verträge.')
        + klausur_hinweis('Typische Auswahlfrage: „Nach dem Stakeholder-Ansatz … welche Aussage ist richtig?“ Achte auf die drei Fragen: Ziele (Ausgleich), Entscheidung (Interessengruppen, Risiko und Entscheidung getrennt), Erfolg (wird aufgeteilt).')
        + wahr('w-st', [('Nach dem Stakeholder-Ansatz entscheidet, wer das Risiko trägt.', False, 'Das ist der Shareholder-Ansatz.'),
                        ('Nach dem Stakeholder-Ansatz wird der Gewinn zwischen den Interessengruppen aufgeteilt.', True, 'Alle sollen teilhaben.'),
                        ('Im Shareholder-Ansatz gehören Risikoübernahme und Entscheidungsbefugnis zusammen.', True, 'Wer haftet, entscheidet.'),
                        ('Ziel des Shareholder-Ansatzes ist der Ausgleich von Interessen.', False, 'Ziel ist die langfristige Gewinnmaximierung.')]),
    merk='Shareholder: Ziel langfristige Gewinnmaximierung, Risikoträger (Eigentümer) entscheidet und profitiert. Stakeholder: Ziel Interessenausgleich, Interessengruppen entscheiden (Risiko und Entscheidung getrennt), Gewinn wird aufgeteilt.',
    exam='Aussagen dem Shareholder- oder Stakeholder-Ansatz zuordnen (Auswahlfrage).',
    fehler=['Bei „wer entscheidet“ die Ansätze vertauschen.', 'Die Anspruchsgruppen-Tabelle auswendig lernen statt die drei Fragen zu verstehen.'],
    src='Folien 156–161')

# ---------------------------------------------------------------- 3 Shareholder Value
def eva_bild():
    s = achsen(40, 210, 350, 14, '', '€')
    s += tpg(rechteck(80, 210 - 80 * 1.6, 90, 80 * 1.6, 'var(--c3)', 'var(--c3)', 4), 'Alternativanlage: 1.000.000 € zu 8 % am Kapitalmarkt bringen K · i = 80.000 €. Das ist die Messlatte.')
    s += tpg(rechteck(186, 210 - 110 * 1.6, 90, 110 * 1.6, 'var(--primary)', 'var(--primary)', 4), 'Das Unternehmen erwirtschaftet E − A = 110.000 €. Das sind 30.000 € mehr als die Alternativanlage: unternehmerischer Mehrwert (Economic Value Added).')
    s += strich(40, 210 - 80 * 1.6, 340, 210 - 80 * 1.6, 'var(--c3)', 1.6, True)
    s += T(125, 72, '80.000', 13, 800) + T(231, 24, '110.000', 13, 800)
    s += T(125, 228, 'K · i', 13, 700) + T(231, 228, 'E − A', 13, 700)
    s += T(125, 246, 'Kapitalmarkt', 12, 400, 'middle', 'var(--muted)') + T(231, 246, 'Unternehmen', 12, 400, 'middle', 'var(--muted)')
    s += pfeil(290, 210 - 80 * 1.6, 290, 210 - 110 * 1.6 + 2, 'var(--pos)') + T(296, 210 - 95 * 1.6 + 4, '+30.000', 12, 800, 'start', 'var(--pos)')
    return svg(360, 256, s, 'Shareholder Value: E − A gegen K · i', maxw=420)

t_shv = thema('shareholder-value', 'Shareholder Value und unternehmerischer Mehrwert',
    kern='Shareholder Value (wertorientierte Unternehmensführung): Entscheidungen so treffen, dass das Eigenkapital möglichst stark wächst und die Investition mehr bringt als eine vergleichbare Alternativanlage: E − A > K · i.',
    kurz=p('Ein Investor hat 1 Mio. € und könnte sie am Kapitalmarkt zu 8 % anlegen. Das bringt ihm sicher 80.000 € im Jahr. Steckt er das Geld in die Brauerei, muss die Brauerei <b>mehr</b> als 80.000 € erwirtschaften, sonst lohnt es sich nicht.')
        + p('Genau das ist die Idee des <b>Shareholder Value</b>: Das Ergebnis aus der unternehmerischen Tätigkeit (Ertrag minus Aufwand) muss größer sein als das Ergebnis der Alternativanlage (Kapital mal Zins).'),
    fig=fw('Die Messlatte: Kapitalmarkt gegen Unternehmen. Tippe auf die Balken.') + bild(eva_bild()),
    figcap='nach Folien „Shareholder Value“ (Beispiel mit 1 Mio. € und 8 %)',
    article=h3('Zwei Ideen')
        + tabelle(['', 'Idee', 'Formal'], [['Idee 1', 'Betriebliche Entscheidungen so treffen, dass der Eigenkapitalzuwachs möglichst groß ist.', 'max EK!'],
                                          ['Idee 2', 'Betriebliche Entscheidungen so treffen, dass die Investition in ein Unternehmen eine höhere Rentabilität aufweist als eine vergleichbare Alternativanlage.', r'\(E - A > K \cdot i\)']])
        + fx('Shareholder-Value-Bedingung', r'E - A \geq K \cdot i \qquad\Leftrightarrow\qquad r \geq i',
             'Ertrag minus Aufwand muss mindestens so groß sein wie Kapital mal Zinssatz der Alternativanlage. Anders gesagt: Die Rendite r des Unternehmens muss mindestens so hoch sein wie der Zins i.',
             r'\(K \cdot i = 1.000.000 \cdot 0{,}08 = 80.000\) €. Das Unternehmen muss \(E - A \geq 80.000\) € erreichen.')
        + p('Was darüber hinausgeht, heißt <b>unternehmerischer Mehrwert</b> (Economic Value Added). Erwirtschaftet die Brauerei 110.000 €, beträgt der Mehrwert 30.000 €.')
        + weiter('Damit lassen sich ökonomische und verhaltenswissenschaftliche Sicht noch genauer vergleichen.')
        + h3('Die beiden Perspektiven im Vergleich')
        + tabelle(['', 'Ökonomische Perspektive', 'Verhaltenswissenschaftliche Perspektive'], [
            ['Handlungsweise', 'rational', 'begrenzt rational'], ['Zielsystem', 'Nutzen maximieren', 'Nutzen maximieren unter Nebenbedingungen'],
            ['Koordinationsmodell', 'Vorrangstellung der Eigentümer', 'alle Anspruchsgruppen haben gleichen Anspruch'],
            ['Auflösung von Interessenkonflikten', 'durch Vertragsgestaltung (keiner wird gezwungen)', 'durch Diskurs']])
        + bsp('Lohnt sich die Investition?', 'Kapital 500.000 €, Alternativanlage 6 %. Das Unternehmen erwirtschaftet E − A = 25.000 €.',
              [(r'Messlatte \(K \cdot i = 500.000 \cdot 0{,}06\)', '30.000 €'), ('25.000 € < 30.000 €', 'lohnt sich nicht'), (r'Rendite \(r = \frac{25.000}{500.000} = 5\,\% < 6\,\%\)', 'r < i')])
        + wahr('w-shv', [('Die Investition lohnt sich im Sinne des Shareholder Value, wenn E − A > K · i.', True, 'Mehr als die Alternativanlage.'),
                         ('Bei 1 Mio. € und 8 % Alternativzins muss E − A mindestens 8.000 € betragen.', False, '1.000.000 · 0,08 = 80.000 €.'),
                         ('Im ökonomischen Koordinationsmodell haben die Eigentümer Vorrang.', True, 'Vorrangstellung der Eigentümer.')]),
    merk='Shareholder Value: EK-Zuwachs maximieren; E − A > K · i (Rendite r > Zins i der Alternativanlage). Überschuss = unternehmerischer Mehrwert (Economic Value Added).',
    exam='Bedingung E − A > K · i anwenden und im Kopf rechnen.',
    fehler=['Den Prozentsatz nicht in eine Dezimalzahl umrechnen (8 % = 0,08).'],
    src='Folien 162–164')

# ---------------------------------------------------------------- 4 Werturteile
fig_wert = svg(360, 236,
    T(180, 18, 'Soll die BWL Werturteile abgeben?', 14, 800)
    + box(4, 32, 172, 140, 'Primäre\nWerturteile\n\nabsolutes Urteil\nbewertet die Ziele', size=13, tip='Primäre Werturteile bewerten die Ziele selbst („Dieses Ziel ist gut oder schlecht“). Ethisch-normative BWL, eher verhaltenswissenschaftlich.')
    + box(184, 32, 172, 140, 'Sekundäre\nWerturteile\n\nabgeleitetes Urteil\nbewertet die Mittel', size=13, art='hl', tip='Sekundäre Werturteile bewerten nur die Mittel zu einem gegebenen Ziel („Mit welchem Mittel erreiche ich das Ziel am besten?“). Praktisch-normative BWL, ökonomische BWL.')
    + T(90, 196, 'ethisch-normativ', 13, 700) + T(270, 196, 'praktisch-normativ', 13, 700)
    + T(90, 216, 'verhaltenswiss. BWL', 12, 400, 'middle', 'var(--muted)') + T(270, 216, 'ökonomische BWL', 12, 400, 'middle', 'var(--muted)'),
    'Primäre und sekundäre Werturteile', maxw=420)

t_wert = thema('werturteile', 'Werturteile in der BWL',
    kern='Primäre Werturteile bewerten die Ziele selbst (ethisch-normativ, verhaltenswissenschaftliche BWL). Sekundäre Werturteile bewerten nur die Mittel zu gegebenen Zielen (praktisch-normativ, ökonomische BWL).',
    kurz=p('<b>Soll die BWL Werturteile abgeben oder wertfrei Erkenntniszuwachs erzielen?</b> Soll sie also sagen, welche Ziele <b>gut</b> sind, oder nur, wie man ein gegebenes Ziel am besten erreicht? Das ist die <b>Werturteilsfrage</b>.')
        + p('Ein überspitztes Beispiel aus der Vorlesung: Kinder sollen ein Gedicht auswendig lernen. Variante a) „Bitte lernt das Gedicht, es ist wichtig für eure Entwicklung.“ Variante b) eine grausame Drohung. Mit b) lernen sie vielleicht schneller. Wer nur die Mittel bewertet, müsste b) empfehlen. Wer auch Ziele und Werte bewertet, lehnt b) ab.'),
    fig=fw('Zwei Arten von Werturteilen. Tippe auf die Kästen.') + bild(fig_wert),
    figcap='nach Folie „Werturteile“',
    article=h3('Primäre und sekundäre Werturteile')
        + tabelle(['', 'Primäre Werturteile', 'Sekundäre Werturteile'], [
            ['Art', 'absolutes Urteil', 'abgeleitetes Urteil'], ['bewertet', 'die Ziele', 'die Mittel'],
            ['Richtung', 'ethisch-normative BWL', 'praktisch-normative BWL'], ['Perspektive', 'verhaltenswissenschaftliche BWL', 'ökonomische BWL']])
        + p('Je nach Fach sind die Schwerpunkte verschieden: Im Personalwesen spielen ethisch-normative Fragen eine größere Rolle als etwa in der Kostenrechnung.')
        + h3('Empirische oder normative Wissenschaft?')
        + p('Hinter der Werturteilsfrage steht die Unterscheidung <b>empirische vs. normative Wissenschaft</b>. Eine <b>empirische</b> Wissenschaft beschreibt und erklärt, was ist („Wenn der Preis steigt, sinkt die Nachfrage“), und urteilt wertfrei. Eine <b>normative</b> Wissenschaft sagt, was sein soll („Unternehmen sollen fair bezahlen“), und fällt wertgebundene Urteile. Einfach gesagt: empirisch = „so ist es“, normativ = „so soll es sein“. Die BWL vermittelt beide Perspektiven; welche man einnimmt, hängt von der Fragestellung ab.')
        + weiter('Damit ist der Vergleich der beiden Perspektiven vollständig.')
        + h3('Gesamtvergleich der beiden Perspektiven')
        + tabelle(['', 'Ökonomische Perspektive', 'Verhaltenswissenschaftliche Perspektive'], [
            ['Handlungsweise', 'rational', 'begrenzt rational'], ['Zielsystem', 'Nutzen maximieren', 'Nutzen maximieren unter Nebenbedingungen'],
            ['Koordinationsmodell', 'Vorrangstellung der Eigentümer', 'alle Anspruchsgruppen haben gleichen Anspruch'],
            ['Interessenkonflikte', 'durch Vertragsgestaltung', 'durch Diskurs'],
            ['Werturteilsfrage', 'Beschränkung auf sekundäre Werturteile', 'primäre Werturteile durch sozialphilosophische Überlegungen']])
        + wahr('w-wert', [('Sekundäre Werturteile bewerten die Mittel zu einem gegebenen Ziel.', True, 'Abgeleitetes Urteil.'),
                          ('Die ökonomische BWL fällt vor allem primäre Werturteile.', False, 'Sie beschränkt sich auf sekundäre.'),
                          ('Primäre Werturteile gehören zur ethisch-normativen BWL.', True, 'Sie bewerten Ziele.')]),
    merk='Werturteilsfrage: Soll die BWL Werturteile abgeben oder wertfrei Erkenntniszuwachs erzielen? Empirisch (beschreibt, wertfrei) vs. normativ (sagt, was sein soll). Primäre Werturteile: absolut, bewerten Ziele, ethisch-normativ, verhaltenswissenschaftliche BWL. Sekundäre: abgeleitet, bewerten Mittel, praktisch-normativ, ökonomische BWL.',
    exam='Primäre und sekundäre Werturteile unterscheiden; Merkmale den beiden Perspektiven zuordnen.',
    fehler=['Primär und sekundär vertauschen: primär = Ziele, sekundär = Mittel.'],
    src='Folien 165–166')

KAPITEL = kapitel('k5', 'Positionen der BWL',
    'Welches Menschenbild hat die BWL, für wen arbeitet ein Unternehmen, und darf die BWL werten? Durchgehendes Beispiel: die Brauerei Neckarperle AG.',
    ['homo oeconomicus', 'Shareholder/Stakeholder', 'Shareholder Value', 'Werturteile'],
    [t_homo, t_stake, t_shv, t_wert])

from mehr1 import ergaenze
ergaenze(KAPITEL)
