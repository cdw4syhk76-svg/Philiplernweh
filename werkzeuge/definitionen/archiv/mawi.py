"""Materialwirtschaft: Definitionen im Wortlaut der Folien (Meier; Gabler, van Weele/Eßig, BVL, Plowman). Stelle = Deck/PDF-Seite."""
D = lambda b, t, f, w, k, **x: dict(begriff=b, t=t, folie=f, wortlaut=w, kern=k, **x)
DEF = [
 D('Materialwirtschaft (i. e. S. und i. w. S.)', 'begriffe', 'vl/13', 'Materialwirtschaft i.e.S. umfasst die Aufgabe der Versorgung der Produktion mit Material. I.w.S. werden ihr die Gesamtheit aller materialbezogenen Funktionen zugeordnet, dazu gehören alle diejenigen Funktionen, die sich mit der Versorgung des Betriebes und der Steuerung des Materialflusses durch die Fertigung bis hin zur Auslieferung der Fertigerzeugnisse befassen.',
   ['Versorgung der Produktion mit Material', 'Gesamtheit aller materialbezogenen Funktionen', 'Steuerung des Materialflusses', 'Auslieferung der Fertigerzeugnisse']),
 D('Einkauf', 'begriffe', 'vl/14', 'Einkauf: Summe aller operativen und strategischen Tätigkeiten eines Unternehmens, die im Rahmen der Beschaffung von Werkstoffen, Waren, Betriebsmitteln und Dienstleistungen durchzuführen sind. Zielsetzung des Einkaufs ist die Sicherstellung der Versorgung (Ort, Termin, Menge, Qualität) und die Optimierung des Preis-Leistungsverhältnisses der Beschaffungsobjekte.',
   ['Summe aller operativen und strategischen Tätigkeiten', 'Werkstoffen, Waren, Betriebsmitteln und Dienstleistungen', 'Sicherstellung der Versorgung', 'Preis-Leistungs']),
 D('Logistik (Gabler)', 'begriffe', 'vl/15', 'Die Logistik umfasst alle Aufgaben zur integrierten Planung, Koordination, Durchführung und Kontrolle der Güterflüsse sowie der güterbezogenen Informationen von den Entstehungssenken bis hin zu den Verbrauchssenken.',
   ['integrierten Planung, Koordination, Durchführung und Kontrolle der Güterflüsse', 'güterbezogenen Informationen', 'Entstehungssenken bis hin zu den Verbrauchssenken']),
 D('Logistik (BVL)', 'begriffe', 'vl/16', 'Logistik ist ein System, das zunächst im Unternehmen, aber auch unternehmensübergreifend mit Lieferanten und Kunden, eine optimale Versorgung mit Materialien, Informationen, Teilen und Modulen für die Produktion – und auf der anderen Seite natürlich der Märkte bedeutet.',
   ['System', 'unternehmensübergreifend mit Lieferanten und Kunden', 'optimale Versorgung mit Materialien, Informationen, Teilen und Modulen']),
 D('Supply Chain Management', 'begriffe', 'vl/17', 'Supply Chain Management bezeichnet den Aufbau und die Verwaltung integrierter Logistikketten (Material- und Informationsflüsse) über den gesamten Wertschöpfungsprozess, ausgehend von der Rohstoffgewinnung über die Veredelungsstufen bis hin zum Endverbraucher.',
   ['Aufbau und die Verwaltung integrierter Logistikketten', 'Material- und Informationsflüsse', 'gesamten Wertschöpfungsprozess']),
 D('Materialgruppe', 'mgm-definition', 'vl/90', 'Eine Materialgruppe kann definiert werden als Gruppe von kohärenten, auf Märkten erworbenen Produkten oder Dienstleistungen, die im Unternehmen zur Deckung des Bedarfs interner oder externen Kunden eingesetzt werden.',
   ['kohärenten', 'auf Märkten erworbenen Produkten oder Dienstleistungen', 'Deckung des Bedarfs interner oder externe']),
 D('Materialgruppenmanagement (MGM)', 'mgm-definition', 'vl/90', 'Materialgruppenmanagement (MGM) ist ein Instrument der Einkaufsorganisation. Dabei werden Waren und Dienstleistungen beschaffungsmarktorientiert strukturiert. Darauf aufbauend werden Beschaffungsstrategien für Materialgruppen und Lieferanten definiert und Maßnahmen zur Verbesserung des Ergebnisbeitrags erarbeitet.',
   ['Instrument der Einkaufsorganisation', 'beschaffungsmarktorientiert strukturiert', 'Beschaffungsstrategien für Materialgruppen und Lieferanten', 'Verbesserung des Ergebnisbeitrags'], ueberarbeite=[('mawi:mgm-definition:grund', 6)]),
 D('Strategie', 'mgm-definition', 'vl/92', 'Strategie wird definiert als die grundsätzliche, langfristige Verhaltensweise (Maßnahmenkombination) gegenüber der Umwelt zur Verwirklichung der langfristigen Ziele.',
   ['grundsätzliche, langfristige Verhaltensweise', 'Maßnahmenkombination', 'Verwirklichung der langfristigen Ziele']),
 D('Materialgruppenstrategie', 'mgm-definition', 'vl/92', 'Eine Materialgruppenstrategie beschreibt die strategische Ausrichtung auf den jeweiligen, nach Materialgruppen abgegrenzten, Beschaffungsmärkten. Aufgabe ist es, die definierten Materialgruppenziele durch Maßnahmen oder Maßnahmenbündel zu realisieren.',
   ['strategische Ausrichtung', 'nach Materialgruppen abgegrenzten', 'Materialgruppenziele durch Maßnahmen']),
 D('Einstandspreis', 'tco', 'vl/255', 'Einstandspreis = Nettolistenpreis – Preisnachlässe + Bezugsnebenkosten.',
   ['Nettolistenpreis', 'Preisnachlässe', 'Bezugsnebenkosten'], ueberarbeite=[('mawi:tco:grund', 1), ('mawi:tco:vs-verstehen', 5)]),
]
