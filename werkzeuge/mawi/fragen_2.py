"""MaWi-Fragen, Oberthemen 4–7 (MGM, Analyse, Strategie, Instrumente)."""
from fr_basis import *
from fr_basis import _txt, _kasten, _pfeil

R, F = True, False


def quad(felder, xl, yl):
    """Vier-Felder-Portfolio zum Beschriften: felder = [oben links, oben rechts, unten links, unten rechts]"""
    kae = [(60, 10, 140, 80, felder[0]), (210, 10, 140, 80, felder[1]), (60, 100, 140, 80, felder[2]), (210, 100, 140, 80, felder[3])]
    deko = achse(50, 190, 355, 4) + _txt(200, 210, xl, 12, 700, 'var(--dg-b)') + f'<text x="20" y="100" font-size="12" font-weight="700" text-anchor="middle" transform="rotate(-90 20 100)" style="fill:var(--dg-b)">{yl}</text>'
    return kae, deko

# ================================================================ k4 MGM
fam('mgm-definition', 'grund', 'Definiert Materialgruppe und MGM',
    mc('Eine Materialgruppe ist …', 'eine Gruppe kohärenter Zukaufgüter', ['eine Abteilung des Zentraleinkaufs', 'die Liste aller A-Lieferanten im Werk', 'ein gemeinsames Lager für ähnliche Teile'], '', 1, True),
    mc('Wonach strukturiert MGM Waren und Dienstleistungen?', 'beschaffungsmarktorientiert', ['nach internen Kostenstellen', 'nach dem Alphabet der Teile', 'nach dem Lagerort im Werk'], '', 1, True),
    mc('Woher stammt das Category Management ursprünglich?', 'aus dem Marketing der 1980er Jahre', ['aus der Logistik der 1960er Jahre', 'aus der Kostenrechnung', 'aus dem Personalwesen'], '', 2),
    li('Nennen Sie zwei Gründe, warum MGM in den Einkauf kam.', [['Lieferantenmacht', 'zunehmende Lieferantenmacht', 'Globalisierung'], ['strategische Rolle', 'stärkere strategische Rolle des Einkaufs', 'strategischer Einkauf']], '', 2),
    li('Nennen Sie drei Aspekte der MGM-Definition nach O’Brian.', [['Segmentierung des Einkaufsvolumens', 'Segmentierung'], ['Funktion der Produkte', 'Funktionen'], ['Beschaffungsmärkte', 'Bezug zu Beschaffungsmärkten'], ['cross-funktional', 'cross-funktionale Zusammenarbeit']], '', 2, n=3),
    blk('Richtig oder falsch?', [('Die Materialgruppe wird wie eine strategische Geschäftseinheit behandelt.', R), ('Eine Materialgruppenstrategie richtet sich auf einen abgegrenzten Beschaffungsmarkt.', R), ('MGM ist ein Instrument der Lagerverwaltung.', F)], '', 2, True),
    rv('Definieren Sie Materialgruppenmanagement.', 'MGM ist ein Instrument der Einkaufsorganisation: Waren und Dienstleistungen werden beschaffungsmarktorientiert zu Materialgruppen strukturiert; darauf aufbauend werden Beschaffungsstrategien für Materialgruppen und Lieferanten definiert und Maßnahmen zur Verbesserung des Ergebnisbeitrags erarbeitet.', ['Instrument der Einkaufsorganisation', 'beschaffungsmarktorientiert strukturieren', 'Strategien und Maßnahmen'], 2, True))
fam('mgm-nutzen', 'grund', 'Kennt Nutzen, Ziele und Voraussetzungen des MGM',
    mc('Welche Ziele stehen im MGM laut Befragungen im Vordergrund?', 'Kosten- und Preisreduzierungen', ['Risikoreduzierung und Markenwert', 'Innovation und Nachhaltigkeit', 'Personalabbau im Einkauf'], '', 1, True),
    mc('Wie viel kostet ein Bestellvorgang laut Benchmark im Schnitt?', 'ca. 135 €', ['ca. 15 €', 'ca. 1.350 €', 'ca. 5 €'], '', 2),
    zu('Nutzen oder Voraussetzung?', ['Nutzen', 'Voraussetzung'], [('Innovationen der Lieferanten nutzen', 0), ('funktionierende Lieferantenintegration', 1), ('Spend-Analyse auf MG-Ebene', 1), ('bessere Verhandlungsbasis', 0), ('Einkauf auf Managementebene', 1), ('geringeres Supply-Chain-Risiko', 0)], '', 2),
    li('Nennen Sie vier Nutzenkategorien des MGM.', [['Kostenreduzierung', 'Kosten'], ['Effektivität und Effizienz', 'Effizienz'], ['Innovationen', 'Wettbewerbsvorteile'], ['Supply-Chain-Risiko', 'Risiko'], ['cross-funktionale Zusammenarbeit'], ['Management des gesamten Einkaufsvolumens', 'Einkaufsvolumen'], ['strategiegeleitete Beschaffung', 'Strategie']], '', 2, n=4),
    mc('Warum stehen Savings im MGM so stark im Fokus?', 'der Einkauf wird an Savings gemessen', ['andere Ziele sind gesetzlich verboten', 'die Lieferanten verlangen es so', 'Risiken spielen im Einkauf keine Rolle'], '', 2),
    blk('Richtig oder falsch?', [('Gutes MGM bringt nur Kosteneinsparungen.', F), ('Typische Einsparungen liegen meist zwischen 1 und 14 %.', R), ('Jeder Nutzen hat Voraussetzungen.', R), ('Gewinn steigt auch durch Kostensenkung bei gleichem Umsatz.', R)], '', 2, True))
fam('zentral-dezentral', 'grund', 'Vergleicht zentralen und dezentralen Einkauf',
    zu('Vorteil des zentralen oder dezentralen Einkaufs?', ['zentral', 'dezentral'], [('Verhandlungsstärke', 0), ('Flexibilität', 1), ('Synergien', 0), ('Nähe zum Bedarfsträger', 1), ('Bestandsoptimierung', 0), ('technisches Know-how', 1), ('Einkaufs-Know-how', 0), ('Problemorientierung', 1)], '', 1, True),
    mc('Wie verbindet MGM beide Organisationsformen?', 'als kooperative Beschaffungsform', ['durch Abschaffung des Zentraleinkaufs', 'durch Einkauf nur in den Werken', 'durch Auslagerung an Dienstleister'], '', 2, True),
    blk('Richtig oder falsch?', [('Der Zentraleinkauf ist flexibler als der dezentrale Einkauf.', F), ('Der dezentrale Einkauf ist näher am Bedarfsträger.', R), ('Bündelung ist eine Stärke des Zentraleinkaufs.', R)], '', 1))
fam('materialgruppen-bilden', 'grund', 'Bildet und grenzt Materialgruppen ab',
    mc('Nach welchem Kriterium wird eine Materialgruppe abgegrenzt?', 'eindeutiger Beschaffungsmarkt, weit', ['eigene Kostenstellen, möglichst eng', 'Lagerort und Lagerart der Teile', 'Name des bisherigen Hauptlieferanten'], '', 2, True),
    mc('Was passiert, wenn Materialgruppen sehr eng definiert werden?', 'es ergeben sich weniger Möglichkeiten', ['die Bündelungschancen steigen', 'die Zahl der Anbieter steigt', 'die Daten werden automatisch besser'], '', 2),
    li('Nennen Sie drei Gründe, warum man Materialgruppen braucht.', [['Daten analysieren', 'Einkaufsdaten', 'Analyse'], ['Bedarfe transparent', 'ähnliche Bedarfe'], ['Bündelung', 'Bündelungsmöglichkeiten'], ['Strategien', 'Strategien entwickeln'], ['Verhandlungen vorbereiten', 'Verhandlung'], ['Ziele definieren', 'Ziele']], '', 2, n=3, kl=True),
    li('Nennen Sie zwei Folgen einer falschen Materialgruppenzuordnung.', [['keine Datentransparenz', 'falsche Daten', 'unkorrekte Daten'], ['falsche Strategie', 'Strategie nicht korrekt'], ['Ziele nicht messbar', 'Zielabweichungen'], ['schlechte Verhandlungsvorbereitung', 'Verhandlungen']], '', 2),
    mc('Was besagt das Pareto-Prinzip bei der Bildung von Materialgruppen?', '80 % der Ausgaben, 20 % der Lieferanten', ['20 % der Ausgaben betreffen 80 % der Teile', 'alle Materialkosten sind gleich wichtig', 'nur die C-Teile sind zu analysieren'], '', 2),
    blk('Richtig oder falsch?', [('„Die“ Materialgruppenstruktur gibt es nicht.', R), ('Daten liegen oft nur auf Lieferantenebene vor.', R), ('Man sollte immer alle Materialkosten analysieren.', F)], '', 2))
fam('klassifikation', 'grund', 'Kennt UNSPSC und eCl@ss',
    mc('UNSPSC ist ein …', 'nicht-parametrischer Klassifikationsstandard', ['parametrischer Standard mit Merkmalleisten', 'deutsches Normenwerk für Schrauben', 'Verfahren der Bedarfsermittlung'], '', 2, True),
    rh('Ordnen Sie die UNSPSC-Ebenen von grob nach fein.', ['Segment', 'Family', 'Class', 'Commodity', 'Business Function'], '', 2),
    zu('UNSPSC oder eCl@ss?', ['UNSPSC', 'eCl@ss'], [('fünf Ebenen', 0), ('Sachgebiet, Hauptgruppe, Gruppe, Untergruppe', 1), ('Merkmalleisten mit Wertelisten', 1), ('vor allem in den USA verbreitet', 0), ('acht- oder zehnstelliger Code', 0)], '', 2),
    mc('Was beschreiben parametrische Standards zusätzlich?', 'Merkmale und Attribute der Produkte', ['nur die Hierarchie der Gruppen', 'die Lieferanten der Produkte', 'die Lagerplätze der Produkte'], '', 2),
    blk('Richtig oder falsch?', [('Bei UNSPSC sind die ersten vier Ebenen standardisiert.', R), ('eCl@ss hat seinen Schwerpunkt in Deutschland.', R), ('Jede UNSPSC-Ebene wird dreistellig codiert.', F)], '', 2))
fam('orientierungsrahmen', 'grund', 'Ordnet den MGM-Prozess',
    rh('Bringen Sie die Phasen des MGM in die richtige Reihenfolge.', ['Ziele, Nutzen, Materialgruppen bilden', 'IST-Analyse', 'Strategieentwicklung', 'Strategieumsetzung', 'Controlling und Optimierung'], '', 1),
    zu('In welche Phase gehört das Instrument?', ['IST-Analyse', 'Strategieentwicklung', 'Strategieumsetzung'], [('ABC-Analyse', 0), ('Kraljic-Portfolio', 1), ('TCO', 2), ('Business Requirements', 0), ('SWOT', 1), ('Linear Performance Pricing', 2)], '', 2, True),
    mc('Was begleitet alle Phasen des MGM-Prozesses?', 'das Lieferantenmanagement', ['die Stücklistenauflösung', 'die Losgrößenformel', 'die Wareneingangsprüfung'], '', 2))

# ================================================================ k5 Analyse
fam('vier-phasen', 'grund', 'Kennt das Vier-Phasen-Modell',
    rh('Ordnen Sie die vier Phasen.', ['Analyse', 'Strategieableitung', 'Implementieren', 'Optimieren'], '', 1, True),
    mc('Welche Phasen gehören zur „operativen Umsetzung“?', 'Implementieren und Optimieren', ['Analyse und Strategieableitung', 'Analyse und Optimieren', 'Strategieableitung und Implementieren'], '', 1),
    mc('Strategie ist laut Vorlesung …', 'die langfristige Verhaltensweise', ['eine einzelne kurzfristige Maßnahme', 'die Summe aller Bestellungen im Jahr', 'eine Kennzahl des Einkaufscontrollings'], '', 1, True),
    blk('Richtig oder falsch?', [('Ohne IST-Analyse gibt es kein Ziel.', R), ('Das Vier-Phasen-Modell gilt innerhalb einer Materialgruppe.', R), ('Die Strategieumsetzung erfolgt durch Maßnahmen.', R), ('Optimieren ist die erste Phase.', F)], '', 1))
fam('business-requirements', 'grund', 'Kennt Business Requirements und RAQSCI',
    rh('Bringen Sie die RAQSCI-Stufen in die richtige Reihenfolge (Fundament zuerst).', ['Regulatory', 'Assurance of Supply', 'Quality', 'Service', 'Cost/Commercial', 'Innovation'], '', 2, True),
    zu('Welche RAQSCI-Stufe?', ['Regulatory', 'Assurance of Supply', 'Quality', 'Service', 'Cost', 'Innovation'], [('gesetzliche Vorgaben', 0), ('Liefertreue und Kapazität', 1), ('ISO 9001, Fehlerquote', 2), ('Reaktionszeit, Support', 3), ('Incoterms, Zahlungsziel', 4), ('Simultaneous Engineering', 5)], '', 2, True),
    mc('Business Requirements definieren …', 'die Anforderungen der Kunden', ['die Lieferantenangebote am Beschaffungsmarkt', 'die Preise der direkten Wettbewerber', 'die verfügbare Lagerkapazität des Werks'], '', 1, True),
    li('Wofür sind Business Requirements Voraussetzung? Nennen Sie drei Aktivitäten.', [['RFP', 'RFQ', 'Anfrage'], ['Lieferantenauswahl', 'Auswahlkriterien'], ['Verhandlung'], ['Lieferantenbewertung'], ['Lieferantenmanagement']], '', 2, n=3),
    mc('Was ist in der Praxis häufig die suboptimale Situation?', 'der Lieferant schlägt seine eigene Lösung vor', ['der Einkauf kennt alle Anforderungen', 'die Entwicklung schreibt neutrale Lastenhefte', 'jede Abteilung bestellt selbst'], '', 2),
    blk('Richtig oder falsch?', [('Kosten sind die erste Stufe im RAQSCI-Modell.', F), ('Corporate Social Responsibility gehört zu Assurance of Supply.', R), ('Business Requirements übersetzen die Anforderungen des Geschäfts für die Lieferanten.', R)], '', 2, True))
fam('beschaffungsmarkt-macht', 'grund', 'Analysiert Machtverhältnisse im Beschaffungsmarkt',
    li('Nennen Sie vier Faktoren, die die Nachfragemacht beeinflussen.', [['Einkaufsvolumen', 'Volumen'], ['Kapazitätsauslastung'], ['Substitutionsmöglichkeiten', 'Substitution', 'Ersatzprodukte'], ['Differenzierung der Produkte', 'Produktdifferenzierung'], ['Anzahl der Nachfrager', 'wenige Nachfrager'], ['Lieferantenwechsel', 'Wechsel'], ['Bündelung']], '', 2, n=4, kl=True),
    li('Nennen Sie Porters fünf Kräfte mit Fokus Einkauf.', [['potenzielle Markteintritte', 'Markteintritte', 'neue Anbieter'], ['Marktmacht der Vorlieferanten', 'Vorlieferanten'], ['Rivalität', 'Branchenrivalität', 'Rivalität der Lieferanten'], ['Marktmacht des Kunden', 'Einkaufsmacht', 'Macht des Einkaufs'], ['Ersatzprodukte', 'Substitute']], '', 2, kl=True),
    mm('Wann ist die Einkaufsmacht hoch?', [('wenige Nachfrager', True), ('hohes Einkaufsvolumen', True), ('einfacher Lieferantenwechsel', True), ('starke Produktdifferenzierung', False), ('Monopol des Lieferanten', False)], '', 2, True),
    zu('Welche Preisbildung?', ['Hochpreis', 'Budget', 'Cost plus', 'Wettbewerb', 'Zielkosten'], [('Patentgeschütztes Spezialteil', 0), ('Marketingagentur richtet sich nach dem Etat', 1), ('Zeichnungsteil mit Open-Book-Kalkulation', 2), ('Strom an der Börse', 3), ('Autohersteller gibt Zielpreis für ein Modul vor', 4)], '', 3),
    mc('Wenn es beim Lieferanten schlecht läuft (geringe Auslastung), …', 'steigt die Macht des Einkaufs', ['sinkt die Macht des Einkaufs', 'ändert sich an der Macht nichts', 'muss der Einkauf mehr zahlen'], '', 2))
fam('datenbeschaffung', 'grund', 'Kennt Datenquellen der Analyse',
    zu('Interner, Lieferanten- oder Marktfokus?', ['intern', 'Lieferanten', 'Markt'], [('Was wurde bisher gekauft?', 0), ('Wie ist die Bonität des Lieferanten?', 1), ('Wie hoch ist die Rivalität?', 2), ('Wer sind die Bedarfsträger?', 0), ('Welche Zertifikate hat der Lieferant?', 1), ('Welche technologischen Trends gibt es?', 2)], '', 1),
    mc('Was unterscheidet Marktdaten von Lieferantendaten?', 'Marktdaten betreffen den ganzen Markt', ['Marktdaten betreffen einen Lieferanten', 'Lieferantendaten sind immer öffentlich', 'es gibt keinen Unterschied'], '', 2, True),
    li('Nennen Sie vier Quellen der Datenbeschaffung.', [['Business Requirements', 'Spezifikationen'], ['RFI', 'Request for Information'], ['Internet', 'Desk Research'], ['Lieferantenbesuche'], ['Messen'], ['Fachleute', 'Experten'], ['Veröffentlichungen', 'Fachbücher', 'Studien']], '', 1, n=4),
    mc('Welche Quelle liefert das bisherige Bedarfsvolumen?', 'Auswertungen von Bestellungen und Rechnungen', ['die Vertriebsplanung des nächsten Jahres', 'die Five-Forces-Analyse', 'Messebesuche bei Wettbewerbern'], '', 2))
fam('abc-analyse', 'grund', 'Führt eine ABC-Analyse durch',
    mc('Nach welchem Kriterium sortiert die ABC-Analyse?', 'nach dem Wertanteil am Einkaufsvolumen', ['nach der Stückzahl der Teile', 'nach der Verbrauchsschwankung', 'nach der Größe der Teile'], '', 1, True),
    nu('Teil X hat einen Jahreswert von {W} T€, das gesamte Einkaufsvolumen beträgt {G} T€. Anteil in %?', {'W': [200, 2000, 100], 'G': [5000, 20000, 1000]}, 'W/G*100', '{W} / {G} = {=W/G*100} %', '%', 1, lvl=1),
    zu('Welche Normstrategie passt?', ['A-Teile', 'B-Teile', 'C-Teile'], [('breiter anfragen, länger verhandeln', 0), ('Aufwand und Einsparung ausgewogen', 1), ('E-Commerce, Vollsortimenter, Dienstleister', 2), ('sorgfältige Verhandlungsvorbereitung', 0)], '', 2, True),
    rh('Bringen Sie das Vorgehen der ABC-Analyse in die richtige Reihenfolge.', ['Jahreswert je Position berechnen', 'absteigend nach Wert sortieren', 'Anteile kumulieren', 'Klassengrenzen setzen'], '', 2),
    mc('Welcher Anteil am Einkaufsvolumen entfällt typischerweise auf A-Teile?', 'ca. 80 %', ['ca. 5 %', 'ca. 15 %', 'ca. 50 %'], '', 1, True),
    li('Nennen Sie drei Anlässe für eine ABC-Analyse im Einkauf.', [['Preisverhandlungen', 'Verhandlungsvorbereitung'], ['Sourcing-Strategie'], ['Make-or-Buy'], ['Lieferantenentwicklung'], ['Risikomanagement', 'Risk-Management'], ['Beschaffungsmarktforschung', 'Anfragen']], '', 2, n=3),
    blk('Richtig oder falsch?', [('Die ABC-Analyse hilft vor allem bei der Priorisierung.', R), ('C-Teile machen die meisten Positionen, aber wenig Wert aus.', R), ('Pareto war ein italienischer Volkswirt und Soziologe.', R), ('Bei C-Teilen lohnt sich lange Verhandlung am meisten.', F)], '', 2, True))
fam('xyz-analyse', 'grund', 'Kombiniert ABC- und XYZ-Analyse',
    mc('Was ist das Einteilungskriterium der XYZ-Analyse?', 'Kontinuität und Vorhersagbarkeit des Bedarfs', ['Wertanteil am Einkaufsvolumen', 'Größe der Teile gemessen an der Palette', 'Anzahl der Lieferanten je Teil'], '', 1, True),
    zu('Welche Klasse (Schwankungsbreite)?', ['X', 'Y', 'Z'], [('bis 10 %', 0), ('bis 60 %', 1), ('über 60 %', 2), ('hohe Vorhersagegenauigkeit', 0), ('diskontinuierlicher Bedarf', 2)], '', 1, True),
    zu('Welche Normstrategie passt?', ['AX', 'AZ', 'CX', 'CZ'], [('Just-in-Time, Ship-to-Line', 0), ('fallweise Disposition', 1), ('Rahmenvertrag mit regelmäßiger Anlieferung, mehr Lager', 2), ('ausreichend Lager, Beschaffungsdienstleister', 3)], '', 2, True),
    bes('Ergänzen Sie die ABC-XYZ-Matrix (A-Spalte).', [(70, 10, 280, 50, 'JIT, STS/STL'), (70, 70, 280, 50, 'Rahmenvertrag mit Abruf, Konsignationslager'), (70, 130, 280, 50, 'fallweise Disposition')], ['Auktion', 'Spontanbeschaffung'], '', 3, True,
        deko=_txt(30, 35, 'AX', 14, 800, 'var(--dg-b)') + _txt(30, 95, 'AY', 14, 800, 'var(--dg-b)') + _txt(30, 155, 'AZ', 14, 800, 'var(--dg-b)'), H=190),
    mc('Was ist ein Konsignationslager?', 'Lieferantenware beim Kunden bis zur Entnahme', ['ein Lager nur für Ausschussteile', 'ein Zwischenlager beim Spediteur', 'ein Lager für Handelswaren des Kunden'], '', 2),
    blk('Richtig oder falsch?', [('Für AZ-Teile ist Just-in-Time ideal.', F), ('Die XYZ-Analyse bewertet nicht den Wert.', R), ('Die GMK-Analyse teilt nach Teilegröße ein.', R)], '', 2, True),
    rv('Ein teures Teil wird täglich gleichmäßig verbraucht. Ordnen Sie es ein und nennen Sie die Normstrategie.', 'Hoher Wert = A, gleichmäßiger, gut vorhersagbarer Bedarf = X, also AX-Teil. Normstrategie: bedarfssynchrone Beschaffung, Just-in-Time bzw. Ship-to-Stock- oder Ship-to-Line-Verträge, um Bestände und Kapitalbindung niedrig zu halten.', ['A wegen Wert', 'X wegen gleichmäßigem Bedarf', 'JIT/STS/STL'], 3, True))

# ================================================================ k6 Strategie
fam('einkaufsziele', 'grund', 'Leitet Einkaufsziele ab',
    mc('Wie werden Einkaufsziele abgeleitet?', 'top-down aus den Unternehmenszielen', ['bottom-up aus den Lieferantenwünschen', 'aus der Lagerbestandsliste', 'zufällig je nach Einkäufer'], '', 1, True),
    li('Nennen Sie drei Zielparameter, die dem Einkauf vorgegeben werden.', [['Preise', 'Mengen'], ['EM-Quote', 'Emerging Markets'], ['Lieferantenreduzierung'], ['Währungssicherung'], ['Liefersicherung', 'Versorgungssicherheit']], '', 2, n=3),
    zu('Welche Ebene, welches Erfolgskriterium?', ['Vorstand', 'Werk', 'Einkauf'], [('Dividende, Aktienkurs', 0), ('Bereichsergebnis', 1), ('Entwicklung der Materialkosten', 2)], '', 1),
    li('Nennen Sie die Top-3-Ziele des strategischen Einkaufs laut Benchmark.', [['Versorgungssicherheit'], ['Savings', 'Kostenreduzierung', 'Einsparungen'], ['Lieferantenmanagement']], '', 2),
    blk('Richtig oder falsch?', [('Originäre Einkaufsziele sichern langfristig Kosten, Qualität und Lieferung.', R), ('Natural Hedging gleicht Währungsrisiken über Einkaufsländer aus.', R), ('Materialgruppenziele brauchen kein Zieldreieck.', F)], '', 2))
fam('lieferantenpyramide', 'grund', 'Versteht Lieferantenpyramide und Lieferantenmanagement',
    rh('Ordnen Sie die Strategieebenen.', ['Einkaufsziele', 'Einkaufsstrategie', 'Materialgruppenstrategie', 'Lieferantenstrategie'], '', 1),
    mc('Womit muss eine Lieferantenpyramide immer verbunden werden?', 'mit einer Lieferantenbewertung', ['mit einer Stücklistenauflösung', 'mit der Andler-Formel', 'mit einer Inventur'], '', 2),
    li('Nennen Sie vier Bausteine des Lieferantenmanagements.', [['Lieferantenbewertung', 'Bewertung'], ['Lieferantenklassifizierung', 'Klassifizierung'], ['Lieferantenauszeichnung', 'Auszeichnung'], ['Lieferantenentwicklung', 'Entwicklung'], ['Risikomanagement', 'Risiko'], ['Eskalationsmanagement', 'Eskalation']], '', 2, n=4),
    blk('Richtig oder falsch?', [('Die Lieferantenstrategie folgt aus der Materialgruppenstrategie.', R), ('Die Pyramide zeigt nur den SOLL-Zustand.', F)], '', 1))
fam('portfolio-grundlagen', 'grund', 'Kennt Portfolio-Grundlagen und BCG',
    bes('Ergänzen Sie die BCG-Matrix.', quad(['Question Marks', 'Stars', 'Poor Dogs', 'Cash Cows'], 'relativer Marktanteil', 'Marktwachstum')[0], ['Hebelteile', 'Engpassteile'], '', 2,
        deko=quad(['', '', '', ''], 'relativer Marktanteil', 'Marktwachstum')[1], H=220),
    zu('Welche Normstrategie?', ['Question Marks', 'Stars', 'Cash Cows', 'Poor Dogs'], [('selektieren', 0), ('investieren', 1), ('abschöpfen', 2), ('desinvestieren', 3)], '', 1),
    rh('Ordnen Sie die Schritte der Portfolio-Aufstellung.', ['Objektauswahl', 'Kriterien festlegen', 'Bewertung', 'Ist-Positionierung', 'Strategieableitung'], '', 2),
    mc('Ein Portfolio stellt eine strategische Situation dar in …', 'zwei Dimensionen', ['einer Dimension', 'fünf Dimensionen', 'beliebig vielen Tabellen'], '', 1),
    blk('Richtig oder falsch?', [('Die Portfoliotechnik stammt ursprünglich aus dem Wertpapiermanagement.', R), ('In der Regel ist eine Achse intern, eine extern.', R), ('Cash Cows haben hohes Marktwachstum.', F)], '', 2))
fam('kraljic', 'grund', 'Wendet das Kraljic-Portfolio an',
    bes('Beschriften Sie das Kraljic-Portfolio.', [(60, 10, 140, 80, 'Hebelteile'), (210, 10, 140, 80, 'strategische Teile'), (60, 100, 140, 80, 'unkritische Teile'), (210, 100, 140, 80, 'Engpassteile')], ['Cash Cows', 'Stars'], '', 2, True,
        deko=achse(50, 190, 355, 4) + _txt(200, 210, 'Beschaffungskomplexität', 12, 700, 'var(--dg-b)') + '<text x="20" y="100" font-size="12" font-weight="700" text-anchor="middle" transform="rotate(-90 20 100)" style="fill:var(--dg-b)">Ergebniseinfluss</text>', H=220),
    zu('Welche Normstrategie?', ['Hebel', 'strategisch', 'unkritisch', 'Engpass'], [('Wettbewerb ausnutzen, Auktionen', 0), ('Allianzen, Lieferantenintegration', 1), ('Prozesskosten senken, Kataloge', 2), ('Sicherheitsbestände, Second Source', 3)], '', 2, True),
    zu('Welches Feld?', ['Hebel', 'strategisch', 'unkritisch', 'Engpass'], [('teure Alurohre, viele Anbieter', 0), ('teure Akkuzellen, drei Hersteller', 1), ('Büromaterial', 2), ('billiger Spezialchip, ein Lieferant', 3)], '', 2, True),
    mc('Was bedeutet „Ergebniseinfluss“ im Original?', 'profit impact, nicht spend', ['das Einkaufsvolumen allein', 'die Zahl der Lieferanten', 'die Länge der Lieferzeit'], '', 3, True),
    mc('Die Beschaffungskomplexität ist hoch, wenn …', 'es nur wenige geeignete Lieferanten gibt', ['viele Anbieter um Aufträge kämpfen', 'der Lieferantenwechsel leichtfällt', 'die Teile genormt und einfach sind'], '', 2, True),
    li('Nennen Sie die drei generischen Strategien nach der Portfolioanalyse.', [['Ausnutzen'], ['Ausbalancieren', 'Halten'], ['Diversifizieren']], '', 2, True),
    lu('K = [[0]], Z = [[1]], P = [[2]], S = [[3]]', [['Kosten'], ['Zusammenarbeit'], ['Prozess'], ['Sicherstellung', 'Sicherstellung der Versorgung']], '', 2),
    rv('Erklären Sie die Achsen des Kraljic-Portfolios.', 'Die interne Achse Ergebniseinfluss (profit impact) misst, wie stark ein kleiner Vorteil auf Teileebene das Gesamtergebnis beeinflusst (Volumen, Anteil an den Materialkosten, Qualität, Technologie). Die externe Achse Beschaffungskomplexität (Beschaffungsrisiko) erfasst, was die Auswahl einschränkt: wenige Lieferanten, schwieriger Wechsel, Kapazitätsengpässe, komplexe Teile.', ['Ergebniseinfluss intern', 'Beschaffungskomplexität extern', 'je ein Beispiel'], 3, True))
fam('kraljic-dynamik', 'grund', 'Denkt Kraljic dynamisch',
    mc('Wie wird ein Engpassteil zum Hebelteil?', 'durch neue Spezifikation oder Lieferanten', ['durch deutlich höhere Sicherheitsbestände', 'durch einen längeren Liefervertrag', 'durch weniger, aber größere Bestellungen'], '', 2, True),
    rh('Ordnen Sie den Weg des IKEA-Bilderrahmens.', ['unkritisches Teil', 'Engpassteil', 'Hebelteil', 'strategisches Teil'], '', 3),
    mc('Ein kleines Restaurant kauft „Lebensmittel“ beim Großhändler. Was zeigt das Beispiel?', 'Portfolio und Marktmacht gehören zusammen', ['Lebensmittel sind immer Engpassteile', 'Restaurants brauchen gar kein Portfolio', 'Großhändler verhandeln mit allen gleich'], '', 3),
    blk('Richtig oder falsch?', [('Unkritische Teile bündelt man Richtung Hebelteile.', R), ('Strategische Teile standardisiert man Richtung Hebelteile.', R), ('Die Felder im Portfolio sind unveränderlich.', F)], '', 2))
fam('marktmacht-portfolio', 'grund', 'Nutzt das Marktmacht-Portfolio',
    zu('Welche Strategie?', ['Emanzipation', 'Geschäftsfreunde', 'Anpassung/Selektion', 'Chancenrealisierung'], [('Lieferant stark, Abnehmer schwach', 0), ('beide stark', 1), ('beide schwach', 2), ('Abnehmer stark, Lieferant schwach', 3)], '', 2, True),
    mc('Welche Maßnahme passt zur Emanzipationsstrategie?', 'zusätzliche Lieferanten aufbauen', ['Gegengeschäfte vereinbaren', 'Konditionen nachverhandeln', 'Beziehung opportunistisch führen'], '', 2),
    mc('Was gehört zur Geschäftsfreundestrategie?', 'Kooperationen und Langzeitverträge', ['Lieferantenwechsel und Substitution', 'Nebenleistungswettbewerb', 'Eigenproduktion des Teils'], '', 2))
fam('risiko-portfolio', 'grund', 'Nutzt das Risikoportfolio',
    zu('Welche Strategie im Risikoportfolio?', ['Investition', 'Abschöpfung', 'selektiv'], [('Störungsgefahr hoch, Anfälligkeit hoch', 0), ('beides niedrig', 1), ('eins hoch, eins niedrig', 2)], '', 2, True),
    li('Nennen Sie drei Maßnahmen der Investitionsstrategie.', [['langfristige Verträge', 'Verträge'], ['Kooperationen', 'Allianzen'], ['Lagerhaltung', 'mehr Lager'], ['Substitution', 'technische Änderungen'], ['Dual Sourcing', 'Multiple Sourcing', 'zweiter Lieferant']], '', 2, n=3),
    mc('Wozu dient eine Akzeptanzlinie im Risikoportfolio?', 'zur Priorisierung der Materialgruppen', ['zur Berechnung der Bestellmenge', 'zur Auswahl des Spediteurs', 'zur Festlegung der Preise'], '', 2),
    rh('Ordnen Sie das Vorgehen der Risikoanalyse.', ['Team einberufen', 'Risikoklassifizierung', 'Priorisieren', 'Maßnahmen entwickeln', 'Aktionsplan', 'Monitoring'], '', 2))
fam('swot-scoring', 'grund', 'Leitet Strategien mit SWOT und Scoring ab',
    zu('Welche SWOT-Normstrategie?', ['S-O', 'W-O', 'S-T', 'W-T'], [('ausbauen', 0), ('aufholen', 1), ('absichern', 2), ('vermeiden', 3)], '', 1, True),
    zu('Intern oder extern?', ['intern', 'extern'], [('hohes Volumen in der Materialgruppe', 0), ('neue Anbieter auf dem Markt', 1), ('fehlende Digitalisierung', 0), ('drohende Zölle', 1)], '', 1),
    nu('Scoring: Punkte {A}, {B}, {C}, {D} bei Gewichten 15 %, 25 %, 20 %, 40 %. Score?', {'A': [0, 10, 1], 'B': [0, 10, 1], 'C': [0, 10, 1], 'D': [0, 10, 1]}, '0.15*A+0.25*B+0.2*C+0.4*D', '0,15·{A} + 0,25·{B} + 0,2·{C} + 0,4·{D} = {=0.15*A+0.25*B+0.2*C+0.4*D}', '', 2, lvl=2),
    mc('Warum empfiehlt die Vorlesung für die Praxis Portfolios statt der vollen SWOT-Ableitung?', 'die SWOT-Ableitung ist oft zu komplex', ['SWOT ist rechtlich nicht zulässig', 'Portfolios brauchen keine Daten', 'SWOT kennt keine Risiken'], '', 3),
    blk('Richtig oder falsch?', [('Die SWOT wird idealerweise cross-funktional erstellt.', R), ('Chancen und Risiken beziehen sich auf den Beschaffungsmarkt.', R), ('Im Scoring-Beispiel gewinnt „Do Nothing“.', F)], '', 2))

# ================================================================ k7 Instrumente
fam('early-involvement', 'grund', 'Begründet Early Involvement',
    mc('Wie viel Prozent der Produktkosten werden ungefähr in Design und Entwicklung festgelegt?', 'ca. 70 %', ['ca. 10 %', 'ca. 30 %', 'ca. 95 %'], '', 1, True),
    mc('Wann ist das Einsparpotenzial am größten?', 'neutrale Spezifikation, frühe Einbindung', ['vorausgewählter Lieferant, frühe Einbindung', 'neutrale Spezifikation, späte Einbindung', 'vorausgewählter Lieferant, späte Einbindung'], '', 2, True),
    li('Worüber informieren sich Fachabteilung und Einkauf beim Early Involvement? Nennen Sie drei Punkte.', [['Projekt'], ['Zeitachse', 'Termine'], ['geplante Mengen', 'Mengen']], '', 2),
    mc('In welcher Phase des Produktentstehungsprozesses sollte der Einkauf idealerweise dabei sein?', 'Projektvorbereitung', ['Serienfertigung', 'Vorserie', 'Produktauslauf'], '', 2),
    blk('Richtig oder falsch?', [('Kosten werden früh festgelegt, aber spät verursacht.', R), ('Die Einbindung des Einkaufs ist in der Praxis meist optimal.', F), ('Je früher der Einkauf eingebunden wird, desto größer der Kostenhebel.', R)], '', 2, True))
fam('buendelung-rfx', 'grund', 'Unterscheidet RFI, RFP und RFQ',
    zu('RFI, RFP oder RFQ?', ['RFI', 'RFP', 'RFQ'], [('Lieferanten kennenlernen, Kapazitäten erfragen', 0), ('Lösungsvorschläge der Lieferanten', 1), ('verbindliches Preisangebot nach Spezifikation', 2), ('früh im Prozess, viele Lieferanten', 0), ('an wenige Lieferanten, hohe Verbindlichkeit', 2)], '', 1, True),
    mc('Welche Anfrage hat die höchste Verbindlichkeit?', 'RFQ', ['RFI', 'RFP', 'NDA'], '', 1, True),
    mm('Wann ist die Bündelungsfähigkeit hoch?', [('ähnliche Beschaffungsobjekte', True), ('hohes gemeinsames Volumen', True), ('geringe Wechselkosten', True), ('hohe Spezifität', False), ('Single Sourcing', False)], '', 2, True),
    rh('Ordnen Sie den Prozess vom Bedarf zum Rahmenvertrag.', ['Bedarfe', 'Vorauswahl', 'RFP/RFQ', 'Angebotsvergleich', 'Verhandlung', 'Rahmenvertrag'], '', 2),
    kz('Wofür steht RFQ?', ['Request for Quotation'], '', 1))
fam('rahmenvertrag', 'grund', 'Versteht Rahmenverträge',
    rh('Ordnen Sie von unverbindlich zu verbindlich.', ['Rahmenvertrag', 'Jahres-/Preisabschluss', 'Einzelbestellung'], '', 1, True),
    mc('Begründet ein Rahmenvertrag eine Abnahmepflicht?', 'nur wenn eine Mindestabnahme vereinbart ist', ['ja, immer für die geschätzte Menge', 'ja, für mindestens ein Jahr', 'nein, er ist rechtlich nichtig'], '', 2, True),
    li('Nennen Sie drei Praxistipps für Rahmenverträge.', [['deutsches Recht'], ['Gerichtsstand', 'Gerichtsstand am Firmensitz'], ['UN-Kaufrecht ausschließen', 'UN-Kaufrecht'], ['Bezug auf Rahmenvertrag', 'Bestellungen beziehen sich auf den Rahmenvertrag']], '', 2, n=3),
    mc('Wie arbeiten MGM und dezentraler Einkauf beim Rahmenvertrag zusammen?', 'zentral abschließen, dezentral abrufen', ['dezentral abschließen, zentral abrufen', 'jedes Werk verhandelt selbst', 'nur der Lieferant ruft ab'], '', 2, True),
    blk('Richtig oder falsch?', [('Rahmenverträge unterliegen normalerweise nicht der AGB-Kontrolle.', R), ('Erst die Einzelbestellung verpflichtet zu Lieferung und Zahlung.', R), ('Ein NDA ist ein Preisabschluss.', F)], '', 2, True))
fam('vertragsrecht', 'grund', 'Kennt Grundlagen des Vertragsrechts',
    mc('Der Lieferant antwortet auf eine Bestellung mit „ja, aber 5 % teurer“. Das ist …', 'Ablehnung mit neuem Angebot', ['eine wirksame Annahme', 'ein kaufmännisches Bestätigungsschreiben', 'eine Vertragsstrafe'], '', 2, True),
    rh('Ordnen Sie die Rangfolge der Vertragsinhalte.', ['individuell ausgehandelte Regelungen', 'AGB', 'gesetzliche Regelungen'], '', 1, True),
    zu('Welcher Vertragstyp?', ['Kaufvertrag', 'Werkvertrag', 'Dienstvertrag'], [('Lieferung von 500 Sätteln', 0), ('Reparatur einer Maschine', 1), ('Beratertage', 2), ('Erstellung einer Software', 1)], '', 2, True),
    mc('Was verlangt § 377 HGB vom kaufmännischen Käufer?', 'Ware sofort prüfen und Mängel rügen', ['Ware binnen zwei Jahren zurückgeben', 'Rechnungen sofort bezahlen', 'Verträge schriftlich schließen'], '', 2, True),
    mc('Wann wird ein kaufmännisches Bestätigungsschreiben Vertragsinhalt?', 'wenn der Empfänger nicht widerspricht', ['wenn beide Parteien es unterschreiben', 'wenn ein Notar es formell beglaubigt', 'wenn es per Einschreiben zugestellt wird'], '', 2, True),
    blk('Richtig oder falsch?', [('Verträge sind grundsätzlich formfrei.', R), ('Ein Werkvertrag schuldet einen Erfolg.', R), ('Ein Dienstvertrag schuldet ein Ergebnis.', F), ('Beim Bestätigungsschreiben soll man eine Gegenzeichnung fordern.', F)], '', 2, True))
fam('tco', 'grund', 'Rechnet Einstandspreis und denkt in TCO',
    nu('Listenpreis {L} €, Rabatt {R} %, Skonto 2 %, Fracht {F} €. Einstandspreis?', {'L': [500, 2000, 100], 'R': [2, 10, 1], 'F': [10, 60, 5]}, 'L*(1-R/100)*0.98+F',
       '{L} · {=1-R/100} = {=L*(1-R/100)}; − 2 % Skonto = {=L*(1-R/100)*0.98}; + {F} = {=L*(1-R/100)*0.98+F}', '€', 2, lvl=2, kl=True),
    lu('Einstandspreis = Nettolistenpreis − [[0]] + [[1]]', [['Preisnachlässe', 'Nachlässe', 'Rabatte'], ['Bezugsnebenkosten', 'Bezugskosten', 'Nebenkosten']], '', 1, True),
    zu('Preisnachlass oder Bezugsnebenkosten?', ['Nachlass', 'Nebenkosten'], [('Skonto', 0), ('Fracht', 1), ('Bonus', 0), ('Zoll', 1), ('Rabatt', 0), ('Versicherung', 1)], '', 1, True),
    li('Nennen Sie vier Bestandteile der Landed Cost.', [['Teilepreis'], ['Werkzeugkosten', 'Nebenkosten'], ['Währung', 'Währungskosten'], ['Verpackung'], ['Versicherung'], ['Transport', 'Fracht'], ['Zölle', 'Zoll', 'Abgaben'], ['Zahlungsbedingungen']], '', 2, n=4, kl=True),
    mc('Was bedeutet „Ownership“ in TCO?', 'die gesamte Besitzphase', ['das Eigentum am Lieferanten', 'nur der Kaufzeitpunkt', 'die Rechte am Patent'], '', 2),
    mc('Ein Lieferant aus China hat den niedrigsten Teilepreis. Warum ist er nicht automatisch die beste Wahl?', 'Fracht, Zoll und Risiken erhöhen die TCO', ['weil Teilepreise immer falsch sind', 'weil Import gesetzlich verboten ist', 'weil die Qualität immer schlecht ist'], '', 2, True),
    blk('Richtig oder falsch?', [('Skonto wird bei Zahlung innerhalb einer Frist gewährt.', R), ('Ein Bonus wird sofort auf der Rechnung abgezogen.', F), ('Qualitätskosten sind schwer zu quantifizieren.', R), ('Die Vergabe entscheidet oft ein Buying-Center.', R)], '', 2))
fam('incoterms', 'grund', 'Ordnet Incoterms ein',
    zu('Welche Gruppe?', ['E', 'F', 'C', 'D'], [('EXW', 0), ('FCA', 1), ('FOB', 1), ('CIF', 2), ('CPT', 2), ('DDP', 3), ('DAP', 3)], '', 1, True),
    mc('Bei welchem Incoterm trägt der Verkäufer die maximalen Pflichten?', 'DDP', ['EXW', 'FCA', 'FOB'], '', 1, True),
    mc('Welche Klauseln gelten nur für See- und Binnenschifffahrt?', 'FAS, FOB, CFR, CIF', ['EXW, FCA, CPT, CIP', 'DAP, DAT, DDP', 'nur EXW'], '', 3),
    mc('Warum braucht der TCO-Vergleich Incoterms?', 'sie regeln Fracht, Versicherung, Zoll', ['sie legen den Teilepreis im Vertrag fest', 'sie ersetzen den Rahmenvertrag ganz', 'sie bestimmen die optimale Bestellmenge'], '', 2, True))
fam('ksa', 'grund', 'Kalkuliert mit der Zuschlagskalkulation',
    nu('Materialeinzelkosten {M} €, MGK {G} %, Fertigungskosten {F} €. Herstellkosten?', {'M': [20, 80, 5], 'G': [5, 10, 1], 'F': [10, 40, 5]}, 'M*(1+G/100)+F', 'MK = {M} · {=1+G/100} = {=M*(1+G/100)}; HK = {=M*(1+G/100)} + {F} = {=M*(1+G/100)+F}', '€', 2, lvl=2, kl=True),
    nu('Herstellkosten {H} €, Verwaltungs-GK 9 %, Vertriebs-GK 6 %, Wagnis 1 % (je auf HK). Selbstkosten?', {'H': [50, 150, 5]}, 'H*1.16', '{H} · (1 + 0,09 + 0,06 + 0,01) = {=H*1.16}', '€', 2, lvl=2, kl=True),
    rh('Ordnen Sie die Stufen der Zuschlagskalkulation.', ['Materialkosten', 'Fertigungskosten', 'Herstellkosten', 'Selbstkosten', 'Barverkaufspreis', 'Nettoverkaufspreis'], '', 2, True),
    zu('Welche Stufe der Kostenrechnung (AST)?', ['Kostenartenrechnung', 'Kostenstellenrechnung', 'Kostenträgerrechnung'], [('Welche Kosten sind angefallen?', 0), ('Wo sind Kosten angefallen?', 1), ('Wofür sind Kosten angefallen?', 2), ('Betriebsabrechnungsbogen', 1)], '', 1, True),
    li('Nennen Sie die sechs originären Kostenarten.', [['Materialkosten', 'Material'], ['Anlagenkosten', 'Maschinenkosten', 'Abschreibungen'], ['Personalkosten', 'Personal'], ['Kapitalkosten', 'kalkulatorische Zinsen'], ['Fremdleistungskosten', 'Fremdleistungen'], ['Wagniskosten', 'kalkulatorische Wagnisse']], '', 2),
    zu('Einzel- oder Gemeinkosten?', ['Einzelkosten', 'Gemeinkosten'], [('Fertigungsmaterial', 0), ('Wareneingangskontrolle', 1), ('Fertigungslohn', 0), ('Materialdisposition', 1), ('Werbung', 1)], '', 2),
    li('Nennen Sie drei Bestandteile des Maschinenstundensatzes.', [['Abschreibungen'], ['Instandhaltung', 'Reparatur'], ['kalkulatorische Zinsen', 'Zinsen'], ['Raumkosten', 'Flächenkosten'], ['Energiekosten', 'Energie'], ['Lohnkosten']], '', 2, n=3),
    mc('Worauf wird der Gewinnzuschlag im Kalkulationsschema berechnet?', 'auf die Selbstkosten', ['auf die Materialkosten', 'auf die Fertigungslöhne', 'auf den Barverkaufspreis'], '', 2))
fam('lpp', 'grund', 'Erklärt Linear Performance Pricing',
    mc('Was ist bei LPP die abhängige Variable?', 'der Preis', ['der Kostentreiber', 'die Teilenummer', 'die Lieferzeit'], '', 2, True),
    mc('Wie entsteht die Best-Practice-Linie?', 'Regression über die besten 20 % der Teile', ['Regression über alle Teile', 'Verbindung von teuerstem und billigstem Teil', 'Mittelwert aller Angebotspreise'], '', 2, True),
    rh('Ordnen Sie die Schritte von LPP.', ['Produktgruppe definieren', 'Treiber identifizieren', 'Daten erheben', 'Daten analysieren', 'Maßnahmen ableiten'], '', 2),
    li('Nennen Sie drei Anforderungen an den Kostentreiber bzw. die Daten bei LPP.', [['gleich für alle Teile', 'gleicher Kostentreiber'], ['leicht verfügbar', 'messbar'], ['positiv korreliert', 'Korrelation'], ['verlässliche Daten', 'vergleichbar'], ['vollständige Datensätze', 'vollständig'], ['mindestens 20 Teile', '20 Teile']], '', 2, n=3),
    mc('Welche Empfehlung gibt die Vorlesung zu LPP und KSA?', 'LPP zum Screening, KSA für Details', ['KSA zum Screening, LPP für Details', 'nur LPP, KSA ist veraltet', 'nur KSA, LPP ist zu ungenau'], '', 2, True),
    nu('Regressionsgerade y = {A} + {B}·x (Preis in € über Gewicht in kg). Erwarteter Preis bei {X} kg?', {'A': [0.5, 3, 0.5], 'B': [0.4, 1.6, 0.2], 'X': [2, 12, 1]}, 'A+B*X', 'y = {A} + {B} · {X} = {=A+B*X}', '€', 2, lvl=2),
    blk('Richtig oder falsch?', [('LPP braucht keine detaillierte Kenntnis der Fertigungsprozesse.', R), ('Die Best-Practice-Linie liegt oberhalb der Durchschnittslinie.', F), ('Die Regression minimiert die Summe der quadrierten Abweichungen.', R), ('NLPP ist einfacher als LPP.', F)], '', 2, True))
