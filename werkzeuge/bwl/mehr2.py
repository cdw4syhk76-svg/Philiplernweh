"""Ergänzungen (Erklärtiefe und weitere Schaubilder) für die Oberthemen 7–12."""
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *
from mehr1 import MEHR, ergaenze

MEHR['maximin'] = (h3('Wer entscheidet so?')
    + p('Maximin passt zu Situationen, in denen ein schlechter Ausgang existenzbedrohend wäre: Wer nur eine Saison übersteht, wenn sie nicht katastrophal wird, achtet auf das Schlimmste. Maximax passt zu Spielern und Gründern, die auf den großen Wurf setzen und einen Verlust verkraften können.')
    + bsp('Neue Matrix', 'Strategien b1 (20, 40, 30), b2 (−10, 90, 50), b3 (25, 25, 25).',
          [('Maximin: Minima 20, −10, 25', 'b3'), ('Maximax: Maxima 40, 90, 25', 'b2')], 'b3 ist die „sichere Bank“: Sie bringt immer 25.')
    + falle('Bei Maximax das größte Minimum wählen. Maximax schaut nur auf die Zeilenmaxima.'))

MEHR['hurwicz'] = (h3('Hurwicz bei gleichen Werten')
    + p('Hat eine Alternative in allen Zuständen dasselbe Ergebnis (z. B. 125.000 im Zentrum, egal ob die Straße kommt), sind Maximum und Minimum gleich. Dann ist Φ unabhängig von λ immer genau dieser Wert. Hurwicz unterscheidet nur bei Alternativen mit Spannweite.')
    + bsp('Kopfrechnen mit λ = 0,4', 'Alternative mit Maximum 90 und Minimum −20.',
          [(r'\(0{,}4 \cdot 90 = 36\)', ''), (r'\(0{,}6 \cdot (-20) = -12\)', ''), (r'\(\Phi = 36 - 12\)', '24')])
    + p('Kritik an der Hurwicz-Regel: Auch sie schaut nur auf zwei Werte je Zeile (bestes und schlechtestes Ergebnis). Alles dazwischen ignoriert sie, und das λ ist subjektiv.'))

MEHR['savage-niehans'] = (h3('Bedauern im Alltag')
    + p('Du kaufst ein Bahnticket für 29 € im Voraus. Am Reisetag gibt es spontan eins für 19 €: Du bedauerst 10 €. Hättest du gewartet und es hätte 59 € gekostet, hättest du 30 € bedauert. Savage-Niehans wählt die Entscheidung, bei der das größtmögliche Bedauern am kleinsten ist: hier das Vorab-Ticket.')
    + bsp('Kurze Matrix', 'a1 (10, 50), a2 (40, 20).',
          [('Spaltenmaxima: 40 und 50', ''), ('Bedauern a1: 30, 0 → Maximum 30', ''), ('Bedauern a2: 0, 30 → Maximum 30', 'gleich: beide Alternativen gleich gut')]))

MEHR['laplace'] = (h3('Laplace ist Bayes mit gleichen Gewichten')
    + p('Das Laplace-Kriterium ist ein Spezialfall der Bayes-Regel: Man setzt einfach alle Wahrscheinlichkeiten gleich (bei vier Zuständen je 25 %). Sobald man mehr weiß, etwa dass Regen viel wahrscheinlicher ist als Sonne, sollte man die echten Wahrscheinlichkeiten nehmen (Entscheidung unter Risiko).')
    + mfig('Fünf Regeln, fünf Logiken', svg(560, 200,
        box(4, 6, 104, 120, 'Maximin\nschlechtestes\nErgebnis', size=12, tip='risikoscheu') + box(116, 6, 104, 120, 'Maximax\nbestes\nErgebnis', size=12, tip='risikofreudig') + box(228, 6, 104, 120, 'Hurwicz\nMischung mit λ', size=12, art='hl', tip='λ = Optimismusparameter') + box(340, 6, 104, 120, 'Savage-\nNiehans\nkleinstes\nBedauern', size=12) + box(452, 6, 104, 120, 'Laplace\nDurchschnitt', size=12)
        + T(56, 150, 'a1', 14, 800) + T(168, 150, 'a2', 14, 800) + T(280, 150, 'a2', 14, 800) + T(392, 150, 'a1', 14, 800) + T(504, 150, 'a3', 14, 800)
        + T(280, 186, 'Wahl in der Folienmatrix', 12, 600, 'middle', 'var(--muted)'),
        'Zusammenführung'), 'nach Folie „Klassische Entscheidungstheorie: Zusammenführung“'))

MEHR['bayes'] = (h3('Erwartungswert verstehen')
    + p('Der Erwartungswert ist der Durchschnitt, den man bei sehr vielen Wiederholungen bekäme. Würde die Eisdiele 100-mal vor derselben Entscheidung stehen, käme sie mit der Randlage im Schnitt auf 129.000 €. Bei einer einzigen Entscheidung bekommt sie aber entweder 150.000 € oder 80.000 €. Wer 80.000 € nicht verkraften kann, wählt vielleicht trotzdem das Zentrum: Das ist dann nicht irrational, sondern risikoscheu. Genau das bildet das Bernoulli-Prinzip ab.')
    + bsp('Drei Zustände', 'Wetter: sonnig 50 %, wechselhaft 30 %, Regen 20 %. Strategie A: 100 / 60 / 10. Strategie B: 70 / 70 / 50.',
          [(r'\(\mu_A = 50 + 18 + 2\)', '70'), (r'\(\mu_B = 35 + 21 + 10\)', '66'), ('Bayes wählt', 'A')], 'B ist sicherer, A hat den höheren Erwartungswert.'))

MEHR['bernoulli'] = (h3('Wie die Nutzenfunktion Risikoscheu abbildet')
    + mfig('Wurzel-Nutzenfunktion', svg(560, 220,
        achsen(50, 190, 540, 14, 'Ergebnis e', 'Nutzen u')
        + kurve(lambda e: math.sqrt(e), 0, 12100, lambda e: 50 + e / 12100 * 470, lambda u: 190 - u * 1.5, farbe='var(--primary)', w=3)
        + T(300, 70, 'u(e) = √e: flacher werdend', 13, 800, 'middle', 'var(--primary)')
        + T(300, 92, 'jeder weitere Euro stiftet weniger Nutzen', 12, 600, 'middle', 'var(--muted)'),
        'Konkave Nutzenfunktion'), 'Eine nach unten gekrümmte Nutzenfunktion steht für einen risikoscheuen Entscheider.')
    + p('Bei einer Wurzelfunktion bringen 1.600 € einen Nutzen von 40, aber 10.000 € nur 100, nicht 250. Hohe Ergebnisse zählen also weniger stark, schlechte relativ mehr. Darum bevorzugt jemand mit dieser Nutzenfunktion sichere Ergebnisse: Er ist risikoscheu.'))

MEHR['begrenzte-rationalitaet'] = (h3('Wie wir trotzdem gute Entscheidungen treffen')
    + p('Weil wir nicht alles wissen können, arbeiten wir mit vereinfachten Modellen: Faustregeln, Gewohnheiten, Empfehlungen. Wir suchen nicht die beste Lösung, sondern eine, die „gut genug“ ist. Das spart Zeit und Kraft und ist oft sinnvoll, denn auch die Suche nach Informationen kostet.')
    + bsp('Begrenzt rational einkaufen', 'Lena kauft eine neue Röstmaschine.',
          [('Sie vergleicht drei Hersteller, die ihr Kollegen empfehlen, nicht alle 40 am Markt.', 'unvollständiges Wissen'), ('Sie weiß nicht, wie sich ihr Geschäft in fünf Jahren entwickelt.', 'Ziel-Mittel-Ergebnis nicht überblickbar'), ('Nach einer Messe findet sie Design plötzlich wichtiger.', 'instabile Präferenzen')]))

MEHR['prospect-theory'] = (h3('Verlustaversion im Alltag')
    + p('Verluste schmerzen etwa doppelt so stark, wie gleich große Gewinne freuen. Deshalb behalten Anleger fallende Aktien zu lange („die kommt wieder“) und verkaufen steigende zu früh. Deshalb wirken „Sie verlieren 50 €, wenn Sie nicht wechseln“-Formulierungen stärker als „Sie sparen 50 €“.')
    + bsp('Effekt erkennen', '',
          [('„Ich habe das Konzertticket bezahlt, also gehe ich hin, obwohl ich krank bin.“', 'Sunk Cost'), ('„Mein altes Fahrrad gebe ich nicht unter 400 € her.“ (Marktwert 250 €)', 'Besitztumseffekt'), ('Das erste Angebot über 3.000 € prägt die ganze Gehaltsverhandlung.', 'Ankereffekt'), ('„Bei meinem Fachwissen kann bei der Gründung nichts schiefgehen.“', 'Overconfidence')]))

MEHR['garbage-can'] = (h3('Garbage Can im Projektalltag')
    + p('Das Fallbeispiel der Vorlesung (Projekt „Zentrale Reservierung“ einer Fluggesellschaft) zeigt die typischen Muster: In jeder Sitzung saßen andere Teilnehmer, die Ziele wurden mehrfach umformuliert, und am Ende wurden Lösungen beschlossen, die einzelne Teilnehmer schon mitgebracht hatten (ein Softwaresystem). Das ursprüngliche Problem, die telefonische Erreichbarkeit, trat in den Hintergrund.')
    + p('Was hilft? Klare Ziele zu Beginn festhalten, feste Teilnehmer, Protokolle. Wer die Muster kennt, kann sie auch nutzen: Wer seine Lösung im richtigen Moment einbringt, setzt sie eher durch.'))

MEHR['fuehrung'] = (h3('Eine Strategie in fünf Phasen: Stride')
    + tabelle(['Phase', 'Stride'], [['Zielsetzung', 'Vision „Jeder soll gern laufen“; Ziel: Umsatz +10 %'], ['Umweltanalyse', 'Trailrunning boomt; Billiganbieter drängen in den Markt'], ['Unternehmensanalyse', 'Stärke Entwicklung, Schwäche Onlinevertrieb'], ['Strategiewahl', 'Produktentwicklung: Trailschuh-Serie (Ansoff), Differenzierung (Porter)'], ['Implementierung und Kontrolle', 'Team, Budget, Zeitplan; monatlicher Soll-Ist-Vergleich']])
    + p('Die Phasen sind kein starres Nacheinander: Ergibt die Kontrolle große Abweichungen, beginnt man wieder bei der Zielsetzung oder Analyse. Strategie ist ein Kreislauf.'))

MEHR['zielhierarchie'] = (h3('Gute Ziele formulieren')
    + p('Je weiter unten in der Pyramide, desto konkreter und messbarer sollen Ziele sein: Inhalt (was?), Ausmaß (wie viel?), Zeitbezug (bis wann?). „Wir wollen wachsen“ ist eine Richtung, „Umsatz im Bereich Trailschuhe bis Ende 2027 um 2 Mio. € steigern“ ist ein Unternehmens- bzw. Geschäftsbereichsziel.')
    + bsp('Stufe zuordnen', '',
          [('„Wir bringen Menschen in Bewegung.“', 'Vision/Leitbild'), ('„Konzernumsatz 2027: 250 Mio. €“', 'Unternehmensziel'), ('„Sparte Trail: Marktanteil 5 %“', 'Geschäftsbereichsziel'), ('„Einkauf: Materialkosten −3 %“', 'Funktionsziel')]))

MEHR['umweltanalyse'] = (h3('Umweltfaktoren erkennen')
    + bsp('Stride: Was gehört wohin?', '',
          [('Neue EU-Regeln zur Nachhaltigkeit von Textilien', 'rechtlich'), ('Zinsen steigen, Konsum sinkt', 'wirtschaftlich'), ('Laufen wird zum Lifestyle', 'gesellschaftlich'), ('Handelsstreit mit Asien, Zölle', 'politisch'), ('Ein Konkurrent senkt die Preise', 'Wettbewerbsumfeld (Konkurrenz)')])
    + p('Die Fehleinschätzungen der Geschichte zeigen: Umweltanalysen sind Prognosen, und Prognosen können krass danebenliegen. Gerade bei neuen Technologien unterschätzt man oft, wie schnell sie sich durchsetzen.'))

MEHR['five-forces'] = (h3('Five Forces auf Stride angewendet')
    + tabelle(['Kraft', 'Stride', 'Stärke'], [['Rivalität', 'große Marken und viele Anbieter, Markt wächst aber', 'mittel'], ['neue Konkurrenz', 'Online-Marken (Direktvertrieb) kommen leicht in den Markt', 'hoch'],
                                             ['Lieferanten', 'Spezialschäume nur von wenigen Herstellern', 'hoch'], ['Abnehmer', 'große Sporthandelsketten drücken Preise', 'hoch'], ['Ersatzprodukte', 'Barfußschuhe, andere Sportarten', 'gering']])
    + p('Ergebnis: Der Markt ist hart umkämpft. Stride sollte sich klar positionieren (Differenzierung oder Nische) und die Abhängigkeit von wenigen Lieferanten verringern.'))

MEHR['markteintritt'] = (h3('Economies of Scale im Kopf rechnen')
    + bsp('Fixkostendegression', 'Ein Werkzeug für die Sohlenform kostet 60.000 €. Variable Kosten je Paar 20 €.',
          [('bei 1.000 Paar: 60.000 ÷ 1.000 + 20', '80 € je Paar'), ('bei 10.000 Paar: 60.000 ÷ 10.000 + 20', '26 € je Paar')],
          'Der große Anbieter produziert viel billiger. Ein Neuling mit kleiner Menge kann preislich kaum mithalten: eine Markteintrittsbarriere.')
    + mfig('Fixkostendegression', svg(560, 210,
        achsen(50, 180, 540, 14, 'Menge', 'Stückkosten')
        + kurve(lambda x: 60000 / x + 20, 800, 12000, lambda x: 50 + x / 12000 * 480, lambda k: 180 - k * 1.8, farbe='var(--primary)', w=3)
        + strich(50, 180 - 20 * 1.8, 530, 180 - 20 * 1.8) + T(530, 180 - 20 * 1.8 - 6, 'variable Kosten 20 €', 12, 600, 'end', 'var(--muted)'),
        'Stückkosten sinken mit der Menge'), 'Größeneffekte (Economies of Scale)'))

MEHR['verhandlungsmacht'] = (h3('Machtverhältnisse einschätzen')
    + bsp('Wer ist mächtiger?', '',
          [('Ein Autohersteller kauft Standardschrauben, die 50 Firmen herstellen.', 'Abnehmer mächtig (standardisiert)'), ('Ein Chiphersteller beliefert als einziger mit einem speziellen Bauteil.', 'Lieferant mächtig (kein Ersatz)'),
           ('Ein Supermarktkonzern macht 60 % des Umsatzes einer Molkerei aus.', 'Abnehmer mächtig (großer Umsatzanteil)'), ('Ein Lieferant kündigt an, eigene Läden zu eröffnen.', 'Lieferant mächtiger (Vorwärtsintegration)')]))

MEHR['swot'] = (h3('Eine SWOT für Stride')
    + tabelle(['', 'Inhalt'], [['Strengths', 'starke Entwicklungsabteilung, treue Laufvereine, Made in Germany'], ['Weaknesses', 'kein eigener Onlineshop, hohe Lohnkosten'], ['Opportunities', 'Trailrunning-Boom, Gesundheitstrend'], ['Threats', 'Billiganbieter, Rohstoffpreise']])
    + bsp('Handlungsempfehlungen ableiten', '',
          [('SO: Entwicklungsstärke + Trail-Boom', 'Trailschuh-Serie'), ('ST: treue Vereine gegen Billiganbieter', 'Vereinsprogramm mit Rabatten'), ('WO: kein Shop, aber Onlinekauf wächst', 'Onlineshop aufbauen'), ('WT: hohe Kosten + Preiskampf', 'Prozesse automatisieren')]))

MEHR['mbv-rbv'] = (h3('Beide Sichten am Beispiel')
    + p('Warum ist ein Discounter erfolgreich? Market-based View: Er hat sich als Kostenführer positioniert und nutzt seine Marktmacht gegenüber Lieferanten. Resource-based View: Er hat einzigartige Logistikprozesse und eine Unternehmenskultur der Sparsamkeit, die man nicht einfach kopieren kann.')
    + p('In der Praxis ergänzen sich beide: Die Five Forces zeigen, wo ein Markt attraktiv ist; die Ressourcenanalyse zeigt, ob das Unternehmen die Fähigkeiten hat, dort zu gewinnen. Die SWOT-Analyse verbindet beides: S/W aus der Ressourcensicht, O/T aus der Marktsicht.')
    + mfig('Verbindung der Sichten', svg(560, 160,
        box(4, 20, 170, 80, 'Market-based View\n(outside-in)\nO / T', size=12) + pfeil(176, 60, 196, 60) + box(198, 20, 164, 80, 'SWOT-\nAnalyse', size=13, art='hl') + pfeil(384, 60, 364, 60) + box(386, 20, 170, 80, 'Resource-based View\n(inside-out)\nS / W', size=12)
        + T(280, 134, 'die SWOT verbindet Markt- und Ressourcensicht', 12, 600, 'middle', 'var(--muted)'),
        'MBV, RBV und SWOT'), ''))

MEHR['lebenszyklus'] = (h3('Was man je Phase tut')
    + tabelle(['Phase', 'typische Maßnahmen'], [['Einführung', 'bekannt machen, Werbung, Probleme beheben, Preis festlegen'], ['Wachstum', 'Kapazität ausbauen, Vertrieb erweitern, Marke stärken'], ['Reife', 'Kosten senken, Varianten anbieten, Kunden binden'], ['Sättigung', 'Relaunch/Facelift oder Rückzug, Nachfolger vorbereiten']])
    + p('Zusammenhang mit der BCG-Matrix: Produkte in Einführung und Wachstum sind oft Question Marks oder Stars, in der Reife Cash Cows, in der Sättigung Poor Dogs. Ein gesundes Unternehmen hat Produkte in allen Phasen: Die Cash Cows von heute finanzieren die Stars von morgen.'))

MEHR['erfahrungskurve'] = (h3('Strategische Folgen')
    + p('Wer zuerst große Mengen produziert, rutscht schneller die Kurve hinunter und hat dauerhaft niedrigere Kosten. Das spricht dafür, früh Marktanteile zu gewinnen, auch mit niedrigen Einführungspreisen. Gleichzeitig hilft die Kurve bei „make or buy“: Ein Zulieferer, der eine Million Teile gebaut hat, ist vermutlich billiger als die eigene Fertigung mit zehntausend.')
    + p('Die Erfahrungskurve beschreibt die Kosten in Abhängigkeit von der <b>kumulierten</b> Menge (Erfahrung), Economies of Scale die Kosten in Abhängigkeit von der Menge <b>je Periode</b> (Betriebsgröße). Beides senkt die Stückkosten, aber aus unterschiedlichen Gründen.'))

MEHR['bcg-matrix'] = (h3('Normstrategien und Geldflüsse')
    + mfig('Geldflüsse in der BCG-Matrix', svg(560, 230,
        box(130, 10, 140, 90, 'Question\nMarks', size=13) + box(290, 10, 140, 90, 'Stars', size=13, art='hl') + box(130, 120, 140, 90, 'Poor Dogs', size=13) + box(290, 120, 140, 90, 'Cash Cows', size=13)
        + pfeil(310, 120, 230, 100, 'var(--pos)', 2.2) + pfeil(360, 120, 360, 102, 'var(--pos)', 2.2)
        + T(470, 170, 'Geld fließt zu', 12, 700, 'start', 'var(--pos)') + T(470, 186, 'Stars und', 12, 700, 'start', 'var(--pos)') + T(470, 202, 'Question Marks', 12, 700, 'start', 'var(--pos)'),
        'Geldflüsse'), 'Cash Cows finanzieren Stars und ausgewählte Question Marks.')
    + p('Der „relative“ Marktanteil ist der eigene Marktanteil geteilt durch den des größten Konkurrenten. Ein relativer Marktanteil über 1 heißt: Man ist Marktführer.')
    + bsp('Relativer Marktanteil', 'Stride hat 8 % Marktanteil, der größte Konkurrent 20 %.', [('8 ÷ 20', '0,4: niedrig')]))

MEHR['ansoff'] = (h3('Risiko in der Ansoff-Matrix')
    + p('Je mehr Neues, desto größer das Risiko: Bei der Marktdurchdringung kennt man Produkt und Kunden. Bei Produkt- oder Marktentwicklung ist eine Seite neu. Bei der Diversifikation beides. Deshalb wählen Unternehmen meist zuerst die Marktdurchdringung und diversifizieren nur, wenn der Kernmarkt keine Chancen mehr bietet oder sie Risiken streuen wollen.')
    + bsp('Stride einordnen', '',
          [('Rabattaktion für bestehende Laufschuhe in Deutschland', 'Marktdurchdringung'), ('Laufschuhe jetzt auch in Japan', 'Marktentwicklung'), ('neue Trail-Serie für die bisherigen Kunden', 'Produktentwicklung'), ('Stride eröffnet Fitnessstudios', 'Diversifikation')]))

MEHR['porter-strategien'] = (h3('Stuck in the middle')
    + p('Ein Anbieter, der weder der Günstigste noch der Beste ist, hat ein Problem: Preisbewusste Kunden kaufen beim Kostenführer, qualitätsbewusste beim Differenzierer. Übrig bleibt eine schrumpfende Mitte. Porters Rat: sich klar für eine Strategie entscheiden.')
    + bsp('Zuordnen', '',
          [('Ryanair', 'Kostenführerschaft'), ('Apple', 'Differenzierung'), ('Montblanc-Füller', 'Nische'), ('Aldi', 'Kostenführerschaft')]))

MEHR['implementierung'] = (h3('Warum Strategien scheitern')
    + p('Viele Strategien scheitern nicht an der Idee, sondern an der Umsetzung: Die Mitarbeiter verstehen sie nicht (Kommunikation fehlt), es fehlen Budget oder Personal, oder niemand prüft, ob die Ziele erreicht werden. Darum gehören Implementierungsziele, konkrete Maßnahmen und eine laufende Kontrolle zur Strategie.')
    + bsp('Soll-Ist-Kontrolle', 'Stride plant für das erste Halbjahr 4.000 verkaufte Trailschuhe. Verkauft wurden 3.200.',
          [('Abweichung: 3.200 − 4.000', '−800 Paar'), ('Zielerreichungsgrad: 3.200 ÷ 4.000', '80 %'), ('Ursachen suchen und gegensteuern', 'z. B. Werbung, Vertrieb')]))

MEHR['rechtsform-kriterien'] = (h3('Haftung gegen Finanzierung')
    + p('Je mehr jemand persönlich haftet, desto leichter bekommt er Kredit, denn die Bank kann im Notfall auf sein Privatvermögen zugreifen. Wer die Haftung beschränkt (GmbH), schützt sein Privatvermögen, muss aber oft trotzdem privat bürgen, damit die Bank Geld gibt. Die Rechtsformwahl ist also immer ein Abwägen.')
    + tabelle(['Rechtsform', 'Mindestkapital', 'Haftung', 'Publizität'], [['e.K.', 'keins', 'unbeschränkt', 'nein'], ['GbR', 'keins', 'unbeschränkt (alle)', 'nein'], ['OHG', 'keins', 'unbeschränkt (alle)', 'gering'], ['KG', 'keins', 'Komplementär unbeschränkt, Kommanditist Einlage', 'etwas'], ['GmbH', '25.000 €', 'Gesellschaft mit Vermögen', 'ja'], ['AG', '50.000 €', 'Gesellschaft mit Vermögen', 'voll']]))

MEHR['personengesellschaften'] = (h3('GbR oder OHG?')
    + p('Die GbR passt für kleine gemeinsame Vorhaben: Freiberufler (Ärzte, Architekten), eine Band, eine Fahrgemeinschaft. Die OHG ist für ein kaufmännisches Handelsgewerbe gedacht, das eine gewisse Größe hat. Sie hat ein ausgefeilteres Regelwerk (Handelsgesetzbuch), und ihre Gesellschafter haften auch noch fünf Jahre nach dem Austritt.')
    + bsp('Nachhaftung', 'Tom tritt am 1. März aus der OHG aus. Im September geht die OHG pleite; ein Kredit stammt aus dem Vorjahr.',
          [('Tom war bei Entstehung der Schuld Gesellschafter.', ''), ('Er haftet bis zu fünf Jahre nach dem Austritt weiter.', 'Tom haftet mit')]))

MEHR['kg'] = (h3('Warum die KG beliebt ist')
    + p('Die KG verbindet zwei Bedürfnisse: Ein Unternehmer will führen und trägt dafür das volle Risiko; Kapitalgeber wollen sich beteiligen, aber nicht mitarbeiten und nicht mehr verlieren als ihre Einlage. Viele Familienunternehmen sind KGs: Ein Familienmitglied führt, die anderen sind Kommanditisten.')
    + p('Eine beliebte Sonderform ist die <b>GmbH &amp; Co. KG</b>: Komplementär ist eine GmbH. Damit haftet am Ende niemand mehr persönlich unbeschränkt, denn die GmbH haftet nur mit ihrem Vermögen.')
    + bsp('Haftung in der KG', 'Lea (Komplementärin, Privatvermögen 80.000 €) und Tante Rosi (Kommanditistin, Einlage 50.000 €). Die KG hat 200.000 € Schulden, Vermögen 60.000 €.',
          [('KG-Vermögen geht an die Gläubiger', '60.000 €'), ('Rosi verliert ihre Einlage (steckt schon im KG-Vermögen)', 'keine weitere Haftung'), ('Lea haftet für den Rest mit ihrem Privatvermögen', 'bis 80.000 €')]))

MEHR['ag'] = (h3('Aktien: Eigentum in Stücken')
    + p('Eine Aktie ist ein Anteil am Grundkapital der AG. Wer Aktien besitzt, ist Miteigentümer: Er hat ein Stimmrecht in der Hauptversammlung (eine Stimme pro Aktie, bei Stammaktien) und erhält einen Teil des Gewinns als Dividende, wenn die Hauptversammlung das beschließt. Vorzugsaktien bringen meist eine höhere Dividende, aber kein Stimmrecht.')
    + p('Vorteil der AG: Man kann sehr viel Kapital von sehr vielen Anlegern einsammeln, und die Anteile sind (an der Börse) leicht handelbar. Nachteil: hohe Gründungs- und Verwaltungskosten, strenge Regeln, volle Publizität, Mitbestimmung der Arbeitnehmer im Aufsichtsrat.'))

MEHR['gmbh'] = (h3('Warum die GmbH so häufig ist')
    + p('Die GmbH ist die häufigste Kapitalgesellschaft in Deutschland: Sie schützt das Privatvermögen, braucht „nur“ 25.000 € Stammkapital und hat weniger strenge Regeln als die AG. Für sehr kleine Gründungen gibt es zusätzlich die UG (haftungsbeschränkt), die „Mini-GmbH“ mit sehr geringem Stammkapital.')
    + p('Der Preis: Banken vertrauen einer GmbH weniger als einem voll haftenden Einzelkaufmann. Deshalb müssen GmbH-Gründer oft persönlich bürgen. Dann haften sie für diesen Kredit doch privat, aber nur, weil sie es selbst vereinbart haben.'))

MEHR['rechtsform-fall'] = (h3('Fallfragen sicher lösen')
    + merkliste('Rechtsform erkennen', 'in drei Fragen', ['Wie viele Personen? Eine → e.K. (oder Ein-Personen-GmbH).', 'Haftet jemand privat unbeschränkt? Alle → GbR/OHG; einer ja, einer nur mit Einlage → KG; niemand → GmbH/AG.', 'Welche Organe/welches Kapital? Geschäftsführer + 25.000 € → GmbH; Vorstand, Aufsichtsrat, Hauptversammlung + 50.000 € → AG.'])
    + bsp('Klausurfall', 'Ein Unternehmen hat einen Vorstand, der vom Aufsichtsrat bestellt wird. Die Eigentümer haften nur mit ihrem eingesetzten Kapital. Das Grundkapital beträgt 80.000 €.',
          [('Vorstand und Aufsichtsrat', 'Kapitalgesellschaft'), ('Grundkapital über 50.000 €', 'AG')]))
