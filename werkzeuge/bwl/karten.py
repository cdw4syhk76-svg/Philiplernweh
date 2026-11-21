"""Erzeugt inhalte/bwl/karten.json. Aufruf: python3 werkzeuge/bwl/karten.py
Glossarbegriffe und Merksätze werden in der App automatisch zu Karten; hier stehen Aufzählungen, Formeln,
Unterscheidungen und Anwendungen. Danach: fett gedruckte Begriffe der Lernseiten ohne Karte werden gemeldet."""
import json, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[2]
K = {
'bwl-def': [
    ('Grundproblem der BWL', 'Unbegrenzte Bedürfnisse treffen auf knappe Mittel. Daraus folgt: wirtschaften.'),
    ('Beste Definition der BWL laut Vorlesung', 'Zusammenarbeit mit anderen zum gegenseitigen Vorteil (Herstellerin und Käuferin haben beide etwas davon).'),
    ('Betriebs-wirtschafts-lehre: die drei Wortteile', 'Betrieb: wo gewirtschaftet wird\nWirtschaft: mit knappen Mitteln umgehen\nLehre: systematisches Wissen darüber'),
    ('BWL vs. VWL', 'BWL: einzelner Betrieb und seine Entscheidungen\nVWL: die Volkswirtschaft als Ganzes (Märkte, Staat, Gesamtwirtschaft)'),
],
'betrieb': [
    ('Drei Produktionsfaktoren', 'Arbeit, Betriebsmittel, Werkstoffe'),
    ('Betriebsmittel vs. Werkstoffe', 'Betriebsmittel werden genutzt, nicht verbraucht (Maschine, Gebäude).\nWerkstoffe werden verarbeitet oder verbraucht (Holz, Schrauben, Strom).'),
    ('Rohstoff, Hilfsstoff, Betriebsstoff: je ein Beispiel bei einer Tischlerei', 'Rohstoff: Holz (Hauptbestandteil)\nHilfsstoff: Leim, Schrauben (im Produkt, nebensächlich)\nBetriebsstoff: Strom, Öl (nicht im Produkt)'),
    ('Märkte rund um den Betrieb', 'Beschaffungsmarkt, Absatzmarkt, Kapitalmarkt (Kredit und Aktien), Arbeitsmarkt. Dazu im Umfeld, aber keine Märkte: Staat, Gesellschaft, Konkurrenz'),
    ('Definition Betrieb (drei Merkmale)', 'planvoll organisierte Wirtschaftseinheit · kombiniert Produktionsfaktoren · stellt Güter/Dienstleistungen her oder setzt sie ab'),
],
'leistungsart': [
    ('Sachleistungsbetriebe: drei Arten', 'Rohstoffgewinnung, Produktionsmittel, Konsumgüter'),
    ('Dienstleistungsbetriebe: vier Arten', 'Handel, Banken, Versicherungen, sonstige Dienstleister'),
    ('Eine Autowerkstatt repariert und verkauft Ersatzteile. Sach- oder Dienstleistung?', 'Dienstleistungsbetrieb: Reparatur ist eine Dienstleistung, der Verkauf von Ersatzteilen ist Handel, und Handelsbetriebe zählen ebenfalls zu den Dienstleistungsbetrieben (tertiärer Sektor).'),
    ('Ein Stahlwerk ist welcher Betrieb?', 'Sachleistungsbetrieb, Produktionsmittel (Vorprodukt für andere Betriebe)'),
],
'dienstleistung': [
    ('Fünf Merkmale einer Dienstleistung', 'immateriell · uno actu · nicht lager- und transportfähig · schwankende Qualität · Kunde wirkt mit'),
    ('Uno-actu-Prinzip', 'Erstellung und Verbrauch fallen zeitlich zusammen (Friseur schneidet, Kunde „konsumiert“ im selben Moment).'),
    ('Warum schwankt die Qualität einer Dienstleistung?', 'Sie hängt von Mensch, Tagesform und Mitwirkung des Kunden ab; sie lässt sich nicht vorab prüfen.'),
    ('Welches Merkmal fehlt beim Kauf eines Brotes?', 'Uno actu und Mitwirkung: Brot ist eine lagerfähige Sachleistung.'),
],
'betriebszweck': [
    ('Vier Wirtschaftseinheiten nach Zweck und Ziel', 'Privatunternehmen: Gewinnmaximierung\nÖffentliche Unternehmen: Kostenminimierung\nPrivate Haushalte: Nutzenmaximierung\nÖffentliche Haushalte: Wohlfahrtsmaximierung'),
    ('Eigenbedarf vs. Fremdbedarf', 'Haushalte decken den eigenen Bedarf, Unternehmen (Betriebe) den fremden Bedarf.'),
    ('Stadtwerke: Zweck und Ziel?', 'Öffentliches Unternehmen: Fremdbedarfsdeckung, Ziel Kostenminimierung (Versorgung zu geringen Kosten)'),
    ('Warum reicht eine Kennzahl nicht, um alle Betriebe zu messen?', 'Die Ziele unterscheiden sich: Gewinn passt zu Privatunternehmen, nicht zu einer Behörde.'),
],
'wirtschaften': [
    ('Drei Obersätze des Wirtschaftens', 'I: Maximierung des Gewinns\nII: langfristige Maximierung des Gewinns\nIII: langfristige Maximierung des Gewinns unter Beachtung von Nebenbedingungen (Gesetze, Moral)'),
    ('Warum steht „langfristig“ im Obersatz III?', 'Damit niemand Substanz verkauft oder betrügt, um kurzfristig Gewinn zu zeigen.'),
    ('Vier Schritte vom Grundproblem zum Ergebnis', 'Grundproblem → Lösung (Obersätze) → Prinzipien (Rationalprinzip, ökonomisches Prinzip) → Ergebnisse (Erfolgsmaßstäbe)'),
],
'oekprinzip': [
    ('Maximum-, Minimum-, Optimumprinzip', 'Maximum: Input gegeben, Output maximal\nMinimum: Output gegeben, Input minimal\nOptimum: beides frei, bestes Verhältnis'),
    ('„Mit 60 kg Kaffee möglichst viele Packungen“: welches Prinzip?', 'Maximumprinzip (Input gegeben)'),
    ('„200 Packungen mit möglichst wenig Gas“: welches Prinzip?', 'Minimumprinzip (Output gegeben)'),
    ('Typischer Fehler beim ökonomischen Prinzip', '„Mit minimalem Einsatz maximalen Ertrag“: geht nicht, eine Seite muss fest sein (außer beim Optimum als Verhältnis).'),
],
'kennzahlen': [
    ('Gewinn, Wirtschaftlichkeit, Produktivität: Formeln', 'Gewinn = Ertrag − Aufwand (€)\nWirtschaftlichkeit = Ertrag ÷ Aufwand\nProduktivität = Output ÷ Input (Mengen)'),
    ('Wann ist ein Betrieb wirtschaftlich?', 'Wenn Ertrag ÷ Aufwand > 1, also Ertrag > Aufwand.'),
    ('Produktivität vs. Wirtschaftlichkeit', 'Produktivität: Mengen (Stück je Stunde)\nWirtschaftlichkeit: Werte in € (Ertrag je € Aufwand)'),
    ('Wirtschaftlichkeit 1,2: was heißt das?', 'Jeder Euro Aufwand bringt 1,20 € Ertrag.'),
],
'breakeven': [
    ('Break-even-Punkt berechnen', 'G(x) = 0 setzen oder E(x) = A(x); bei Parabeln Mitternachtsformel'),
    ('Break-even bei linearen Funktionen', '\\(x = \\frac{K_f}{p - k_v}\\): Fixkosten durch Deckung je Stück'),
    ('Gewinnschwelle vs. Gewinngrenze', 'Gewinnschwelle: ab hier Gewinn (kleinere Nullstelle)\nGewinngrenze: ab hier wieder Verlust (größere Nullstelle)'),
    ('Break-even ergibt 699,3 Stück: was antworten?', 'Aufrunden auf 700 Stück, erst dann ist der Gewinn nicht mehr negativ.'),
    ('Ertrags- und Aufwandsfunktion (linear)', 'E(x) = p · x;  A(x) = k_v · x + K_f'),
],
'rentabilitaet': [
    ('Rentabilität: Grundformel', 'Erfolgsgröße ÷ Basisgröße · 100 %'),
    ('Drei Rentabilitäten und ihr Nenner', 'Eigenkapitalrentabilität: Eigenkapital\nKapitalrentabilität: eingesetztes Kapital\nUmsatzrentabilität: Umsatz'),
    ('EK-Rentabilität 15 %, Gewinn 22.500 €: Eigenkapital?', '22.500 ÷ 0,15 = 150.000 €'),
    ('Gewinn vs. Rentabilität', 'Gewinn ist ein Betrag in €; Rentabilität setzt ihn ins Verhältnis (in %). Hoher Gewinn kann geringe Rentabilität bedeuten.'),
],
'gewinnmax': [
    ('Gewinnmaximum: drei Schritte', "1. G'(x) = 0 setzen\n2. nach x auflösen\n3. G''(x) < 0 prüfen (Hochpunkt)"),
    ('Preis-Absatz-Funktion', 'Der Preis sinkt mit der Menge, z. B. p(x) = 100 − 2x; dann E(x) = p(x) · x, eine Parabel.'),
    ('Grenzgewinn', "G'(x): zusätzlicher Gewinn der nächsten Einheit; im Maximum null."),
    ('G(x) = −x² + 100x − 1.600: Gewinnmaximum?', "G'(x) = −2x + 100 = 0 → x = 50; G(50) = 900"),
],
'rentmax': [
    ('Rentabilitätsfunktion', 'R(x) = G(x) ÷ Kap(x)'),
    ('Rentabilitätsmaximum berechnen', "R(x) aufstellen, jeden Summanden durch Kap(x) teilen, R'(x) = 0, nur positive x"),
    ('Wann liegen Gewinn- und Rentabilitätsmaximum an derselben Stelle?', 'Wenn das Kapital konstant ist (z. B. fest 1.000 €).'),
    ('Häufiger Fehler beim Rentabilitätsmaximum', 'Kapitalfunktion mit der Kostenfunktion verwechseln.'),
],
'kapazitaet': [
    ('Produktionsprogramm mit knappen Kapazitäten: Vorgehen', '1. Kapazitäten als Ungleichungen\n2. Grenzgeraden zeichnen/gleichsetzen\n3. Eckpunkte prüfen, höchster Gewinn'),
    ('Wo liegt das Optimum bei zwei Kapazitätsgrenzen meist?', 'Im Schnittpunkt der Grenzgeraden (einer Ecke des zulässigen Bereichs).'),
    ('Warum prüft man alle Eckpunkte?', 'Das Optimum liegt immer in einer Ecke; manchmal ist eine Achsenecke besser als der Schnittpunkt.'),
    ('Kapazitätsgrenze als Ungleichung', 'Stunden je Stück · Menge ≤ verfügbare Stunden, z. B. 2a + b ≤ 800'),
],
'liquiditaet': [
    ('Liquidität 1., 2., 3. Grades', 'L1: Zahlungsmittel\nL2: + Forderungen\nL3: + Vorräte\njeweils ÷ kurzfristige Verbindlichkeiten · 100 %'),
    ('Eigenkapitalquote', 'Eigenkapital ÷ Gesamtkapital · 100 %'),
    ('Definition Liquidität', 'Fähigkeit, Rechnungen zum Zeitpunkt der Fälligkeit zu zahlen.'),
    ('Warum zählen Grundstücke nicht zur Liquidität 3. Grades?', 'Sie lassen sich nicht schnell zu Geld machen (Anlagevermögen).'),
],
'effizienz': [
    ('Wertschöpfung', 'Umsatz − Vorleistungen'),
    ('Wer bekommt die Wertschöpfung?', 'Mitarbeiter (Löhne), Fremdkapitalgeber (Zinsen), Staat (Steuern), Eigenkapitalgeber (Gewinn)'),
    ('Effizienz vs. Effektivität', 'Effizienz: die Dinge richtig tun (Ergebnis ÷ Aufwand)\nEffektivität: die richtigen Dinge tun (Ergebnis ÷ Ziel)'),
    ('Ist Wertschöpfung gleich Gewinn?', 'Nein, der Gewinn ist nur der Teil für die Eigentümer.'),
],
'elastizitaet': [
    ('Standardsatz zur Elastizität', '„Ändert sich der Preis um 1 %, ändert sich die Nachfrage um ε %.“'),
    ('elastisch, unelastisch, einheitselastisch', '|ε| > 1 elastisch\n|ε| < 1 unelastisch\n|ε| = 1 einheitselastisch'),
    ('Einflussfaktoren der Preiselastizität', 'Dringlichkeit (Not), Substitutionsfähigkeit, verfügbares Einkommen, Zeit'),
    ('ε = 0,6: Deutung', 'Preis +1 % → Nachfrage −0,6 %; unelastisch'),
    ('Elastizität in der Klausur angeben als …', 'Betrag (ohne Minus)'),
],
'mittelwert': [
    ('Mittelwertmethode: Formel', '\\(\\varepsilon = \\frac{(M_2 - M_1) / \\frac{M_1 + M_2}{2}}{(p_2 - p_1) / \\frac{p_1 + p_2}{2}}\\)'),
    ('Warum Mittelwerte?', 'Damit Preissenkung und Preiserhöhung dieselbe Elastizität ergeben.'),
    ('Wann Mittelwertmethode, wann Punktelastizität?', 'Zwei Punkte (vorher/nachher) gegeben: Mittelwert. Nachfragefunktion gegeben: Punkt.'),
    ('20 € → 16 €, 120 → 180 Stück: Elastizität?', '(60/150) ÷ (4/18) = 0,4 · 4,5 = 1,8'),
],
'punktelastizitaet': [
    ('Punktelastizität: Formel', '\\(\\varepsilon = \\left|\\frac{\\partial Q}{\\partial p} \\cdot \\frac{p}{Q}\\right|\\)'),
    ('D(p) = 20.000 − 5p, p = 800: Elastizität?', 'Q = 16.000; 5 · 800 / 16.000 = 0,25'),
    ('Elastizität auf einer geraden Nachfragekurve', 'Oben links elastisch, unten rechts unelastisch, in der Mitte genau 1; die Steigung ist gleich, p/Q ändert sich.'),
    ('Marktgleichgewicht', 'Angebot = Nachfrage: S(p) = D(p)'),
],
'effekte': [
    ('Mengen-, Preis- und Gesamteffekt', 'ME = (M_neu − M_alt) · p_neu\nPE = (p_neu − p_alt) · M_alt\nGE = Erlös_neu − Erlös_alt = ME + PE'),
    ('Preissenkung bei elastischer Nachfrage', 'Mengeneffekt überwiegt → Erlös steigt'),
    ('Preissenkung bei unelastischer Nachfrage', 'Preiseffekt überwiegt → Erlös sinkt'),
    ('Mengeneffekt: mit welchem Preis?', 'mit dem neuen Preis; der Preiseffekt mit der alten Menge'),
],
'opportunitaet': [
    ('Opportunitätskosten', 'Entgangener Nutzen der besten nicht gewählten Alternative'),
    ('Mensa: Spaghetti, Suppe, Gulasch; du nimmst Gulasch, Spaghetti wäre zweite Wahl. Opportunitätskosten?', 'Der Nutzen der Spaghetti (nur die beste Alternative zählt, nicht alle).'),
    ('Robinson: 12 h, 5 Wildschweine oder 10 l Wasser am Tag. Opportunitätskosten eines Wildschweins?', '2 Liter Wasser'),
    ('Regel 1 und 2 der Ökonomie', '1: Alle Entscheidungen erfordern Zielkonflikte (Trade-offs)\n2: Die Kosten eines Gutes sind das, was man dafür aufgibt'),
],
'grenznutzen': [
    ('Grenznutzen', 'Zusätzlicher Nutzen der nächsten Einheit; nimmt in der Regel ab.'),
    ('Wasser-Diamanten-Paradox', 'Wasser ist lebenswichtig (hoher Gesamtnutzen), aber reichlich da (geringer Grenznutzen) → billig. Diamanten: selten, hoher Grenznutzen → teuer.'),
    ('Rationale Entscheidung am Rand', 'Eine Einheit mehr lohnt sich, solange Grenznutzen ≥ Grenzkosten.'),
    ('Gesamtnutzen vs. Grenznutzen', 'Gesamtnutzen: Summe aller Einheiten\nGrenznutzen: nur die letzte, zusätzliche Einheit'),
],
'maerkte': [
    ('Regeln 4, 5, 6 der Ökonomie', '4: Menschen reagieren auf Anreize\n5: Märkte organisieren Wirtschaft (unsichtbare Hand)\n6: Der Staat kann Marktergebnisse manchmal verbessern'),
    ('Intrinsische vs. extrinsische Motivation', 'intrinsisch: von innen (Spaß, Sinn)\nextrinsisch: von außen (Geld, Strafe); kann die intrinsische verdrängen'),
    ('Unbeabsichtigte Konsequenz: Beispiel Mietpreisbremse', 'Weniger Neubau, weniger Angebot, längere Suche'),
    ('Aufgaben des Staates im Markt', 'Märkte bereitstellen, Markt kontrollieren, Markt schützen'),
],
'innovation': [
    ('Schöpferische Zerstörung (Schumpeter)', 'Neues verdrängt Altes; so entsteht Fortschritt (z. B. Smartphone verdrängt Kamera).'),
    ('Risiko vs. Unsicherheit', 'Risiko: Zustände und ihre Wahrscheinlichkeiten bekannt\nUnsicherheit: Wahrscheinlichkeiten unbekannt'),
    ('Räumliche vs. zeitliche Arbitrage', 'räumlich: hier billig kaufen, dort teuer verkaufen\nzeitlich: heute billig kaufen, später teuer verkaufen'),
    ('Kondratieff-Zyklen', 'Lange Wellen der Wirtschaft, jeweils angestoßen durch Basisinnovationen (Dampfmaschine, Eisenbahn …).'),
],
'wirtschaftsordnung': [
    ('Freie Marktwirtschaft vs. Planwirtschaft', 'Markt: Privateigentum, Preise durch Angebot und Nachfrage, viel Freiheit\nPlan: Staatseigentum, Preise vom Staat, wenig Freiheit'),
    ('Soziale Marktwirtschaft', 'Freier Markt plus sozialer Ausgleich durch den Staat'),
    ('Growth vs. Degrowth', 'Growth: Wohlstand durch Wachstum\nDegrowth: Verzicht auf Wachstum'),
],
'homo-oeconomicus': [
    ('Homo oeconomicus: Kern', 'vollständig informiert, völlig rational, maximiert seinen Nutzen'),
    ('Ökonomische vs. verhaltenswissenschaftliche BWL: Menschenbild', 'ökonomisch: homo oeconomicus (leicht zu rechnen)\nverhaltenswissenschaftlich: begrenzt rational (realistischer)'),
    ('Ein Beispiel gegen den homo oeconomicus', 'Im Supermarkt mit 40 Joghurtsorten greift man zur gewohnten Sorte, ohne alle zu vergleichen.'),
],
'stakeholder': [
    ('Shareholder- vs. Stakeholder-Ansatz', 'Shareholder: Eigentümer im Mittelpunkt, langfristige Gewinnmaximierung\nStakeholder: Interessen aller Anspruchsgruppen ausgleichen'),
    ('Typische Stakeholder', 'Mitarbeiter, Kunden, Lieferanten, Kapitalgeber, Staat, Gesellschaft/Anwohner'),
    ('Argument für den Shareholder-Ansatz', 'Wer das Risiko trägt, soll entscheiden und profitieren; niemand wird zur Mitarbeit gezwungen.'),
    ('Kritik am Stakeholder-Ansatz', 'Interessen widersprechen sich, ein Ausgleich ist schwer messbar; unklar, wer entscheidet.'),
    ('Beitrag von Arbeitnehmern und Management', 'Arbeitnehmer: Arbeit, Zeit, Wissen, Expertise\nManagement: Arbeit, Zeit, Verantwortung, Expertise'),
],
'shareholder-value': [
    ('Shareholder-Value-Bedingung', 'E − A ≥ K · i, also r ≥ i'),
    ('Rendite r', 'r = (E − A) ÷ K · 100 %'),
    ('r = 5 %, i = 6 %, Gewinn positiv: was gilt?', 'Wert wird vernichtet; das Kapital brächte am Kapitalmarkt mehr.'),
    ('K = 1.000.000 €, i = 8 %: Messlatte?', 'K · i = 80.000 €'),
],
'werturteile': [
    ('Primäre vs. sekundäre Werturteile', 'primär: bewerten die Ziele selbst (ethisch-normativ)\nsekundär: bewerten nur die Mittel zu gegebenen Zielen (praktisch-normativ)'),
    ('Welche BWL fällt welche Werturteile?', 'ökonomische BWL: sekundäre\nverhaltenswissenschaftliche BWL: auch primäre'),
    ('„Die Steuern sind zu hoch.“ Welche Art Werturteil?', 'primäres Werturteil (bewertet ein Ziel/einen Zustand)'),
    ('Die Werturteilsfrage', 'Soll die BWL Werturteile abgeben oder wertfrei Erkenntniszuwachs erzielen?'),
    ('Empirische vs. normative Wissenschaft', 'empirisch: beschreibt, was ist (wertfrei)\nnormativ: sagt, was sein soll (wertgebunden)'),
],
'et-ueberblick': [
    ('Ex ante vs. ex post', 'ex ante: vor der Entscheidung durchdringen\nex post: hinterher erklären'),
    ('Präskriptiv vs. deskriptiv', 'präskriptiv (klassische ET): wie man entscheiden soll\ndeskriptiv (verhaltenswiss. ET): wie man wirklich entscheidet'),
    ('Klassische vs. verhaltenswissenschaftliche Entscheidungstheorie', 'klassisch: rationale Regeln, präskriptiv\nverhaltenswissenschaftlich: reales Verhalten, deskriptiv'),
    ('Zwei Stufen der Entscheidung', 'Stufe 1: Problem strukturieren\nStufe 2: Lösung finden'),
],
'et-struktur': [
    ('Bausteine der Problemstrukturierung', 'Zielsystem (was will ich?) und Entscheidungsfeld: Alternativen (was kann ich tun?) und Umwelteinflüsse (was kann passieren?)'),
    ('Abbruchkriterium bei der Suche nach Alternativen', 'Suchkosten vs. Verbesserungspotenzial; Vollständigkeit vs. Übersichtlichkeit; Realität vs. Fantasie'),
    ('Eisdiele: „Wetter im Sommer“ gehört zu …', 'Umwelteinflüssen'),
],
'zielbeziehungen': [
    ('Drei Zielbeziehungen', 'komplementär: fördern sich\nkonkurrierend: eines geht zu Lasten des anderen\nindifferent: beeinflussen sich nicht'),
    ('Bessere Qualität und niedrigere Kosten: Beziehung?', 'meist konkurrierend (Zielkonkurrenz)'),
    ('Mehr Absatz und mehr Umsatz bei festem Preis: Beziehung?', 'komplementär'),
],
'zielsystem': [
    ('Vier Wege bei mehreren Zielen', 'Zieldominanz, effiziente Alternativen, lexikographische Ordnung, Nutzenfunktion'),
    ('Effiziente Alternative', 'Keine andere Alternative ist in einem Ziel besser, ohne in einem anderen schlechter zu sein.'),
    ('Lexikographische Ordnung', 'Ziele der Reihe nach: erst nur das wichtigste; das nächste nur bei Gleichstand.'),
    ('Nutzenfunktion: warum normieren?', 'Ziele haben verschiedene Einheiten; ohne Normierung bestimmt das Ziel mit den größten Zahlen.'),
    ('Zwei Arten zu normieren', 'Höchster Wert = 1, niedrigster = 0, oder jeden Wert durch den höchsten Wert teilen.'),
],
'dominanz': [
    ('Zustandsdominanz', 'In jedem Umweltzustand mindestens so gut und in einem besser.'),
    ('Wahrscheinlichkeitsdominanz', 'Die Wahrscheinlichkeit, mindestens einen Wert zu erreichen, ist nie kleiner und einmal größer.'),
    ('Was passiert mit dominierten Alternativen?', 'Sie fallen weg, bevor eine Regel angewandt wird.'),
],
'maximin': [
    ('Maximin-Regel', 'Je Alternative das schlechteste Ergebnis, davon das beste; extrem risikoscheu (Pessimist).'),
    ('Maximax-Regel', 'Je Alternative das beste Ergebnis, davon das beste; extrem risikofreudig (Optimist).'),
    ('Kritik an Maximin und Maximax', 'Nur ein Wert je Alternative zählt, alle anderen Ergebnisse werden ignoriert.'),
],
'hurwicz': [
    ('Hurwicz-Regel', 'Φ(a) = λ · Maximum + (1 − λ) · Minimum'),
    ('λ in der Vorlesung', 'λ = 0,4 (immer)'),
    ('λ nahe 1 / nahe 0', 'nahe 1: optimistisch, risikofreudig (Maximax)\nnahe 0: pessimistisch, risikoscheu (Maximin)'),
    ('Max 100, Min 40, λ = 0,4: Hurwicz-Wert?', '0,4 · 100 + 0,6 · 40 = 64'),
],
'savage-niehans': [
    ('Savage-Niehans: vier Schritte', '1. Bestes Ergebnis je Zustand\n2. Bedauern = Bestes − eigenes Ergebnis\n3. Je Alternative das größte Bedauern\n4. Davon das kleinste wählen'),
    ('Anderer Name der Savage-Niehans-Regel', 'Regel des kleinsten Bedauerns (Minimax-Regret)'),
    ('Ist das Bedauern je negativ?', 'Nein, mindestens 0 (beim besten Ergebnis eines Zustands).'),
],
'laplace': [
    ('Laplace-Kriterium', 'Alle Zustände gleich wahrscheinlich (p = 1/n); höchster Durchschnitt gewinnt.'),
    ('Prinzip des mangelnden Grundes', 'Ohne Grund, einen Zustand für wahrscheinlicher zu halten, gibt man allen das gleiche Gewicht.'),
    ('Ergebnisse 40, 70, 100: Laplace-Wert?', '(40 + 70 + 100) ÷ 3 = 70'),
],
'bayes': [
    ('Bayes-Regel (µ-Kriterium)', 'E = Σ p_j · e_ij; höchster Erwartungswert gewinnt'),
    ('Welche Risikoeinstellung unterstellt die Bayes-Regel?', 'Risikoneutralität'),
    ('Ungewissheit vs. Risiko', 'Ungewissheit: Wahrscheinlichkeiten unbekannt (Maximin, Hurwicz, Savage, Laplace)\nRisiko: bekannt (Bayes, Bernoulli)'),
],
'bernoulli': [
    ('Bernoulli-Prinzip', 'Ergebnisse mit einer Nutzenfunktion in Nutzen umrechnen, dann den höchsten Erwartungsnutzen wählen.'),
    ('Was leistet Bernoulli gegenüber Bayes?', 'Berücksichtigt die Risikoeinstellung über die Form der Nutzenfunktion.'),
    ('Bernoulli: zwei Schritte', '1. Ergebnismatrix mit der Nutzenfunktion in eine Nutzenmatrix umrechnen\n2. Erwartungsnutzen je Alternative, den höchsten wählen'),
],
'begrenzte-rationalitaet': [
    ('Begrenzte Rationalität (Simon): drei Grenzen', 'unvollständiges Wissen, nicht alle Optionen erfassbar, instabile Präferenzen'),
    ('Intentional rational', 'Menschen wollen rational handeln, schaffen es aber nur begrenzt.'),
    ('Wie entscheiden begrenzt rationale Menschen?', 'auf Basis eines vereinfachten Modells der Wirklichkeit'),
],
'prospect-theory': [
    ('Prospect Theory: Kernaussage', 'Bei Gewinnen risikoscheu, bei Verlusten risikofreudig; Verluste wiegen schwerer als gleich große Gewinne.'),
    ('Vier Verzerrungen neben der Prospect Theory', 'Besitztumseffekt, Ankereffekt, Overconfidence Bias, Sunk-Cost-Effekt'),
    ('Sunk-Cost-Effekt', 'Bereits verlorenes Geld beeinflusst die Entscheidung, obwohl es nicht zurückkommt.'),
    ('Besitztumseffekt', 'Was man besitzt, bewertet man höher als dasselbe Gut, das man nicht besitzt.'),
],
'garbage-can': [
    ('Garbage-Can-Modell: vier Ströme', 'Teilnehmer, Probleme, Lösungen, Entscheidungsgelegenheiten'),
    ('Drei Arten, wie im Garbage-Can-Modell entschieden wird', 'durch Übersehen, durch Flucht, (seltener) durch Problemlösung'),
    ('Garbage-Can: Was ist der „Mülleimer“?', 'Die Entscheidungsgelegenheit (z. B. eine Sitzung), in der Teilnehmer, Probleme und Lösungen fast zufällig zusammentreffen.'),
],
'fuehrung': [
    ('Drei Fragen der strategischen Führung', 'Wo wollen wir hin? Wo stehen wir? Wie kommen wir dahin?'),
    ('Fünf Phasen der strategischen Unternehmensführung', 'Zielsetzung → Umweltanalyse → Unternehmensanalyse → Strategiewahl → Implementierung und Kontrolle'),
    ('Welche Phase folgt auf die Umweltanalyse?', 'die Unternehmensanalyse (danach Strategiewahl)'),
    ('Umweltanalyse vs. Unternehmensanalyse', 'Umwelt: Blick nach außen (Chancen, Risiken)\nUnternehmen: Blick nach innen (Stärken, Schwächen)'),
],
'zielhierarchie': [
    ('Zielhierarchie von oben nach unten', 'Vision → Unternehmensleitbild → Unternehmensziele → Geschäftsbereichsziele → Funktionsziele'),
    ('Was ändert sich von oben nach unten?', 'Die Ziele werden immer konkreter und kurzfristiger.'),
    ('Vision vs. Leitbild', 'Vision: langfristiges Zukunftsbild\nLeitbild: Werte und Grundsätze, wie man dorthin will'),
    ('Leitbild-Beispiele', 'Google: Don’t be evil\nMcDonald’s: favorite place and way to eat\nAmazon: earth’s most customer centric company\nNike: If you have a body, you are an athlete'),
],
'umweltanalyse': [
    ('Allgemeine Umwelt: vier Bereiche', 'politisch, wirtschaftlich, gesellschaftlich, rechtlich'),
    ('Wettbewerbsumfeld', 'Branche, Konkurrenz, Markt; Instrument: Porters Five Forces'),
    ('Neues Lieferkettengesetz: welcher Teil der Umwelt?', 'allgemeine, rechtliche Umwelt'),
    ('Steigende Energiepreise: welcher Teil der Umwelt?', 'allgemeine, wirtschaftliche Umwelt'),
],
'five-forces': [
    ('Porters fünf Wettbewerbskräfte', 'Rivalität in der Branche, neue Konkurrenten, Lieferanten, Abnehmer, Ersatzprodukte'),
    ('Wann ist eine Branche attraktiv?', 'Wenn die fünf Kräfte schwach sind; starke Kräfte drücken die Gewinne.'),
    ('Mandelmilch für eine Molkerei ist …', 'ein Ersatzprodukt (Substitut)'),
],
'markteintritt': [
    ('Drei Arten von Markteintrittsbarrieren', 'Vertrauensbarrieren, politische Barrieren, wirtschaftliche Barrieren'),
    ('Wirtschaftliche Markteintrittsbarrieren', 'Economies of Scale und Scope, Netzwerkeffekt, absolute Kostenvorteile'),
    ('Vertrauensbarrieren', 'Referenzen, Käuferpfadabhängigkeit, Vertriebskanäle, Abschreckung'),
    ('Economies of Scale vs. Scope', 'Scale: Größenvorteile (mehr Menge, sinkende Stückkosten)\nScope: Verbundvorteile (mehrere Produkte nutzen dieselben Ressourcen)'),
],
'verhandlungsmacht': [
    ('Wann sind Lieferanten mächtig?', 'Branchenfirmen klein, kaum Ersatz, Auftrag für sie unbedeutend, Drohung mit Vorwärtsintegration'),
    ('Wann sind Abnehmer mächtig?', 'großer Umsatzanteil, standardisierte Produkte, Drohung mit Rückwärtsintegration'),
    ('Vorwärts- vs. Rückwärtsintegration', 'vorwärts: Lieferant übernimmt die nächste Stufe (verkauft selbst)\nrückwärts: Abnehmer fertigt selbst'),
],
'swot': [
    ('SWOT: vier Felder', 'intern: Strengths, Weaknesses\nextern: Opportunities, Threats'),
    ('Vier SWOT-Strategien', 'SO: Stärken nutzen, Chancen ergreifen\nST: Stärken gegen Risiken\nWO: Schwächen abbauen, Chancen nutzen\nWT: Schwächen und Risiken vermeiden'),
    ('Neue Konkurrenz aus Asien ist …', 'ein Risiko (Threat), extern'),
],
'mbv-rbv': [
    ('Market-based vs. Resource-based View', 'MBV: outside-in, Erfolg durch Marktposition, eher kurzfristig\nRBV: inside-out, Erfolg durch besondere Ressourcen, langfristig'),
    ('Welcher Ansatz gehört zu Porter?', 'Market-based View'),
],
'ressourcen': [
    ('Vier Bedingungen für einen dauerhaften Wettbewerbsvorteil', 'spezifisch, selten, vor Imitation geschützt, vor Substitution geschützt'),
    ('Materielle vs. immaterielle Ressourcen', 'materiell: Sach- und Finanzanlagen\nimmateriell: organisatorisch (Marke, Prozesse) und human (Wissen)'),
    ('Patent auf ein Verfahren schützt die Ressource vor …', 'Imitation'),
    ('Holzerei stellt einen Elektroingenieur ein, den jede Firma brauchen kann. Welche Bedingung fehlt?', 'spezifisch'),
],
'renten': [
    ('Vier Renten und ihre Quelle', 'Ricardo: knappe Ressourcen (input)\nQuasi: optimaler Ressourceneinsatz (intermediär)\nMonopol: Eintrittsbarrieren (Marktmacht)\nSchumpeter: Innovation (output)'),
    ('Skaleneffekte führen zu welcher Rente?', 'Monopol-Rente'),
    ('Billige Energie am Standort führt zu welcher Rente?', 'Ricardo-Rente'),
    ('Ein Pionier mit neuer App erzielt …', 'Schumpeter-Rente'),
],
'lebenszyklus': [
    ('Vier Phasen des Produktlebenszyklus', 'Einführung, Wachstum, Reife, Sättigung'),
    ('Wo liegt das Umsatzmaximum im Lebenszyklus?', 'in der Reife'),
    ('Warum ist am Anfang der Gewinn negativ?', 'Hohe Investitionen (Entwicklung, Werbung) bei noch geringem Umsatz'),
    ('Kritik am Lebenszyklusmodell', 'idealisiert, kein Naturgesetz; Länge der Phasen ist vorher unbekannt'),
],
'erfahrungskurve': [
    ('Erfahrungskurve', 'Je Verdopplung der kumulierten Menge sinken die Stückkosten um 20–30 %.'),
    ('Gründe für den Erfahrungskurveneffekt', 'Lerneffekte, Spezialisierung, Rationalisierung, Know-how, technischer Fortschritt'),
    ('100 € Stückkosten, 20 % Effekt, Menge vervierfacht: Stückkosten?', '100 · 0,8 · 0,8 = 64 €'),
],
'bcg-matrix': [
    ('BCG-Matrix: Achsen', 'Marktwachstum (senkrecht) und relativer Marktanteil (waagerecht)'),
    ('Vier Felder und Normstrategien', 'Question Mark: alles oder raus\nStar: investieren\nCash Cow: abschöpfen\nPoor Dog: beenden'),
    ('Hohes Wachstum, niedriger relativer Marktanteil', 'Question Mark'),
    ('Wofür nutzt man das Geld der Cash Cows?', 'Für Stars und ausgewählte Question Marks'),
],
'ansoff': [
    ('Ansoff-Matrix: vier Felder', 'altes Produkt/alter Markt: Marktdurchdringung\naltes Produkt/neuer Markt: Marktentwicklung\nneues Produkt/alter Markt: Produktentwicklung\nneu/neu: Diversifikation'),
    ('Welches Ansoff-Feld hat das höchste Risiko?', 'Diversifikation'),
    ('Bestehende Räder in Skandinavien verkaufen', 'Marktentwicklung'),
],
'porter-strategien': [
    ('Drei Wettbewerbsstrategien nach Porter', 'Differenzierung, Kostenführerschaft, Nische'),
    ('Stuck in the middle', 'Weder Kostenführer noch differenziert: keine klare Position, geringer Erfolg.'),
    ('Discounter mit niedrigsten Preisen: Strategie?', 'Kostenführerschaft'),
],
'implementierung': [
    ('Implementierung: drei Schritte', 'Kommunikation, Umsetzung, Einsatz (geplant mit Zielen und Maßnahmen)'),
    ('Kontrolle der Strategie', 'Soll-Ist-Abweichung und Zielerreichungsgrad messen'),
    ('Zielerreichungsgrad', 'Ist ÷ Soll: wie weit das Ziel erreicht ist'),
    ('Warum scheitern Strategien oft?', 'Nicht an der Planung, sondern an der Umsetzung: fehlende Kommunikation, Widerstand, keine Kontrolle.'),
],
'rechtsform-kriterien': [
    ('Innen- vs. Außenverhältnis', 'innen: zwischen den Gesellschaftern (Leitung, Gewinnverteilung)\naußen: zu Dritten (Haftung, Publizität)'),
    ('Kriterien der Rechtsformwahl', 'Leitung, Kontrolle, Haftung, Mindesteinlage, Gewinn- und Verlustbeteiligung, Finanzierung, Publizität, Mitbestimmung, Steuern'),
    ('Personen- vs. Kapitalgesellschaft', 'Personen: e.K., GbR, OHG, KG (Menschen haften)\nKapital: GmbH, AG, SE (juristische Person haftet)'),
    ('Wichtigste Frage bei der Rechtsform', 'Wer haftet womit?'),
],
'personengesellschaften': [
    ('Haftung in GbR und OHG', 'alle Gesellschafter unbeschränkt, mit dem gesamten Privatvermögen'),
    ('GbR vs. OHG', 'GbR: einfache Zusammenarbeit\nOHG: ausgefeiltere „Schwester“ für größere Handelsgeschäfte'),
    ('Nachhaftung nach Austritt aus der OHG', 'fünf Jahre'),
    ('Einzelunternehmen (e.K.)', 'Eine Person entscheidet, kontrolliert und haftet allein und unbeschränkt.'),
],
'kg': [
    ('Komplementär vs. Kommanditist', 'Komplementär: leitet, haftet unbeschränkt\nKommanditist: gibt Kapital, leitet nicht, haftet nur mit der Einlage'),
    ('Wie viele Komplementäre braucht eine KG?', 'mindestens einen'),
    ('Kommanditistin mit 30.000 € Einlage: maximaler Verlust?', '30.000 €'),
],
'ag': [
    ('Drei Organe der AG', 'Vorstand (Leitung), Aufsichtsrat (Kontrolle), Hauptversammlung (Aktionäre)'),
    ('Mindestgrundkapital der AG', '50.000 €'),
    ('Womit haftet die AG?', 'Die AG mit ihrem gesamten Gesellschaftsvermögen; die Aktionäre nur mit ihrer Einlage.'),
    ('Publizität der AG', 'volle Publizität (Jahresabschluss veröffentlichen)'),
],
'gmbh': [
    ('Mindeststammkapital der GmbH', '25.000 €'),
    ('Leitung und Kontrolle in der GmbH', 'Leitung: Geschäftsführer\nKontrolle: Gesellschafterversammlung'),
    ('GmbH in der Insolvenz: was verlieren die Gesellschafter?', 'Nur ihre Einlage; das Privatvermögen bleibt geschützt.'),
],
'rechtsform-fall': [
    ('Drei Merkmale, an denen man die Rechtsform erkennt', 'Wer haftet womit? Wie viel Mindestkapital? Wer leitet?'),
    ('„Mindestens 50.000 €, Vorstand, Aufsichtsrat“: Rechtsform?', 'AG'),
    ('„Zwei Freunde machen zusammen ein kleines Projekt, beide haften privat“: Rechtsform?', 'GbR'),
    ('„Einer haftet voll und leitet, die anderen geben nur Geld“: Rechtsform?', 'KG'),
],
}

fach = json.loads((ROOT / 'inhalte/bwl/fach.json').read_text())
ids = [t['id'] for k in fach['kapitel'] for t in k['themen'] if not t.get('aus')]   # ausgegraute Unterthemen: keine Karten
assert set(K) == set(ids), (set(ids) - set(K), set(K) - set(ids))
karten = [{'t': t, 'v': v, 'r': r} for t in ids for v, r in K[t]]
vs = [k['v'] for k in karten]; assert len(vs) == len(set(vs)), [v for v in vs if vs.count(v) > 1]
(ROOT / 'inhalte/bwl/karten.json').write_text('{\n "karten": [\n' + ',\n'.join('  ' + json.dumps(x, ensure_ascii=False) for x in karten) + '\n ]\n}\n')
gl = json.loads((ROOT / 'inhalte/bwl/glossar.json').read_text())['begriffe']
from collections import Counter
c = Counter(k['t'] for k in karten) + Counter(g['heimat'] for g in gl) + Counter(ids)  # + Merksatz
wenig = {t: n for t, n in c.items() if n < 5}
print(f'bwl: {len(karten)} Karten (+ {len(gl)} Glossar + {len(ids)} Merksätze); unter 5 je Unterthema: {wenig}')
