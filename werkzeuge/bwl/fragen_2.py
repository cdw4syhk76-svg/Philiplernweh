"""ABWL-Fragen, Oberthemen 7–12."""
from fr_basis import *
from fr_basis import _pfeil, _txt, _kasten
import fragen_1b  # noqa: F401  (Ergänzungen zu Oberthema 1–6)

M = 'a1 (60, 30, 50, 60), a2 (10, 10, 10, 140), a3 (−30, 100, 120, 130)'

# ================= k7 =================
t = 'dominanz'
fam(t, 'dom', 'Erkennt dominierte Alternativen',
    mc('a1 (125.000 / 90.000) gegen a2 (100.000 / 80.000):', 'a1 ist zustandsdominant', ['a2 ist zustandsdominant', 'keine dominiert', 'beide gleich'], '', 1),
    mc('a1 (0, 20, 10, 60, 25) und a3 (20, 60, 20, 60, 50):', 'a3 dominiert a1', ['a1 dominiert a3', 'keine dominiert', 'beide gleich'], '', 2),
    zu('Risiko oder Ungewissheit?', ['Risiko', 'Ungewissheit'], [('Wahrscheinlichkeiten bekannt', 0), ('Wahrscheinlichkeiten unbekannt', 1), ('Bayes-Regel', 0), ('Laplace-Kriterium', 1), ('Hurwicz-Regel', 1), ('Bernoulli-Prinzip', 0)], '', 1),
    lu('a1 dominiert a2, wenn a1 in [[0]] Zuständen mindestens so gut und in [[1]] besser ist.', [['allen'], ['mindestens einem', 'einem']], '', 2),
    mc('Wahrscheinlichkeitsdominanz prüft man …', 'unter Risiko', ['unter Ungewissheit', 'ohne Zahlen', 'nur bei zwei Zuständen'], '', 2),
    bes('Beschrifte die drei Gruppen von Entscheidungsregeln.', [(110, 4, 140, 36, '=Umweltereignisse'), (4, 70, 112, 60, 'Dominanzregeln'), (124, 70, 112, 60, 'Ungewissheit'), (244, 70, 112, 60, 'Risiko')], ['Zielsystem'], '', 2,
        deko=_pfeil(150, 42, 60, 68) + _pfeil(180, 42, 180, 68) + _pfeil(210, 42, 300, 68) + _txt(180, 152, 'Maximin, Hurwicz …', 12, 600) + _txt(300, 170, 'Bayes, Bernoulli', 12, 600), H=180),
    mc('a1: 50 (10 %), 40 (20 %), 20 (30 %), 10 (40 %); a2: 60 (30 %), 50 (40 %), 30 (20 %), 20 (10 %). Was gilt?', 'a2 ist wahrscheinlichkeitsdominant', ['a1 ist wahrscheinlichkeitsdominant', 'keine dominiert', 'a1 ist zustandsdominant'], '', 3),
    blk('Richtig oder falsch?', [('Dominierte Alternativen kann man streichen.', True), ('Zustandsdominanz verlangt in jedem Zustand „strikt besser“.', False), ('Unter Risiko sind Wahrscheinlichkeiten bekannt.', True), ('Laplace ist eine Regel unter Risiko.', False)], '', 2))

t = 'maximin'
fam(t, 'mm', 'Wendet Maximin und Maximax an',
    mc(f'Matrix {M}. Maximin wählt …', 'a1', ['a2', 'a3', 'keine'], 'Minima 30, 10, −30.', 1, True),
    mc(f'Matrix {M}. Maximax wählt …', 'a2', ['a1', 'a3', 'keine'], 'Maxima 60, 140, 130.', 1, True),
    zu('Welche Risikoeinstellung?', ['risikoscheu', 'risikofreudig'], [('Maximin', 0), ('Maximax', 1), ('Hurwicz mit λ = 0,1', 0), ('Hurwicz mit λ = 0,9', 1)], '', 2, True),
    mc('b1 (20, 40, 30), b2 (−10, 90, 50), b3 (25, 25, 25). Maximin?', 'b3', ['b1', 'b2', 'keine'], '', 2),
    mc('b1 (20, 40, 30), b2 (−10, 90, 50), b3 (25, 25, 25). Maximax?', 'b2', ['b1', 'b3', 'keine'], '', 2),
    mc('Maximin heißt …', 'bestes schlechtestes Ergebnis', ['schlechtestes bestes Ergebnis', 'bestes bestes Ergebnis', 'Durchschnitt'], '', 1, True),
    nu('Zeile 1: ({A}, {B}, {C}); Zeile 2: ({D}, {E}, {F}). Wie hoch ist das größte Zeilenminimum?', {'A': [-20, 60, 10], 'B': [0, 90, 10], 'C': [10, 80, 10], 'D': [-30, 70, 10], 'E': [0, 100, 10], 'F': [20, 60, 10]}, 'max(min(A,B,C), min(D,E,F))', 'Minima {=min(A,B,C)} und {=min(D,E,F)}; das größere: {=max(min(A,B,C), min(D,E,F))}', '', 0, lvl=2),
    mc('Schwäche von Maximin:', 'schaut nur auf ein Ergebnis', ['braucht Wahrscheinlichkeiten', 'braucht eine Nutzenfunktion', 'ist zu optimistisch'], '', 2))

t = 'hurwicz'
fam(t, 'hu', 'Rechnet und deutet die Hurwicz-Regel',
    mc('Die Hurwicz-Regel ist …', 'eine Mischung aus Maximin und Maximax', ['streng risikofreudig', 'streng risikoscheu', 'eine Regel unter Risiko'], '', 1, True),
    nu('Bestes Ergebnis {X}, schlechtestes {N}, λ = 0,4. Φ = ?', {'X': [40, 200, 10], 'N': [-50, 30, 10]}, '0.4*X+0.6*N', '0,4 · {X} + 0,6 · {N} = {=0.4*X+0.6*N}', '', 1, lvl=2, kl=True, tipp='Φ = λ · Max + (1 − λ) · Min'),
    mc(f'Matrix {M}, λ = 0,4. Hurwicz wählt …', 'a2', ['a1', 'a3', 'keine'], 'Φ = 42 / 62 / 34.', 2, True),
    ns('a3 (−30, 100, 120, 130), λ = 0,4. Φ?', 34, '0,4 · 130 + 0,6 · (−30)', '', 2, True),
    mc('λ = 0 entspricht …', 'Maximin', ['Maximax', 'Laplace', 'Savage-Niehans'], '', 2, True),
    mc('Ein großes λ steht für …', 'Optimismus', ['Pessimismus', 'Risikoneutralität', 'Bedauern'], '', 1, True),
    lu('Φ(a) = [[0]] · Maximum + (1 − λ) · [[1]]', [['λ', 'lambda', 'Lambda'], ['Minimum', 'Min']], '', 2, True),
    hotpunkt('Auf der Skala zwischen Minimum (−30) und Maximum (130): Tippe ungefähr auf Φ bei λ = 0,4.', achse(30, 120, 340, 60) + linie([(40, 100), (320, 100)], 'var(--dg-b)', 8) + _txt(40, 80, '−30', 13) + _txt(320, 80, '130', 13),
             (40 + (34 + 30) / 160 * 280, 100, 22), 'Φ = 34, also 40 % des Weges vom Minimum zum Maximum.', 3, kl=True, H=140))

t = 'savage-niehans'
fam(t, 'sn', 'Wendet die Savage-Niehans-Regel an',
    rh('Ordne die Schritte.', ['Spaltenmaximum je Zustand', 'Bedauernsmatrix bilden', 'größtes Bedauern je Zeile', 'kleinstes davon wählen'], '', 1),
    mc(f'Matrix {M}. Savage-Niehans wählt …', 'a1', ['a2', 'a3', 'keine'], 'Max. Bedauern 80 / 110 / 90.', 2),
    ns('Spaltenmaximum 140, eigenes Ergebnis 60. Bedauern?', 80, '140 − 60', '', 1),
    mc('Savage-Niehans heißt auch …', 'Regel des kleinsten Bedauerns', ['Regel des größten Nutzens', 'Prinzip des mangelnden Grundes', 'µ-Kriterium'], '', 1),
    mc('Das Maximum für die Bedauernsmatrix sucht man …', 'je Spalte (Zustand)', ['je Zeile (Alternative)', 'in der ganzen Matrix', 'gar nicht'], '', 2),
    nu('Im Zustand z ist das beste Ergebnis {B}, Alternative a erreicht {E}. Bedauern von a in z?', {'B': [50, 200, 10], 'E': [-40, 150, 10]}, 'B-E', '{B} − {E} = {=B-E}', '', 0, wenn='B >= E', lvl=1),
    mc('a1 (10, 50), a2 (40, 20). Maximales Bedauern?', 'beide 30', ['a1 10, a2 30', 'a1 40, a2 30', 'beide 0'], '', 3),
    mc('Bedauern im Alltag: Ticket für 29 € vorab, später für 19 € zu haben. Bedauern?', '10 €', ['19 €', '29 €', '48 €'], '', 1))

t = 'laplace'
fam(t, 'la', 'Wendet das Laplace-Kriterium an',
    mc('Laplace setzt alle Zustände …', 'gleich wahrscheinlich', ['unwahrscheinlich', 'nach Bauchgefühl', 'nach Bedauern'], '', 1),
    nu('Ergebnisse ({A}, {B}, {C}, {D}). Laplace-Wert?', {'A': [-40, 100, 10], 'B': [0, 120, 10], 'C': [0, 150, 10], 'D': [10, 160, 10]}, '(A+B+C+D)/4', '({A} + {B} + {C} + {D}) ÷ 4 = {=(A+B+C+D)/4}', '', 2, lvl=1),
    mc(f'Matrix {M}. Laplace wählt …', 'a3', ['a1', 'a2', 'keine'], 'Ø 50 / 42,5 / 80.', 2),
    kz('Wie heißt der Grundsatz hinter Laplace? „Prinzip des …“', ['mangelnden Grundes'], '', 2),
    zu('Welche Regel wählt in der Folienmatrix welche Alternative?', ['a1', 'a2', 'a3'], [('Maximin', 0), ('Maximax', 1), ('Hurwicz', 1), ('Savage-Niehans', 0), ('Laplace', 2)], '', 3),
    mc('Laplace ist ein Spezialfall von …', 'Bayes mit gleichen Gewichten', ['Maximax', 'Hurwicz mit λ = 1', 'Savage-Niehans'], '', 3),
    mc('Bei vier Zuständen ist jedes p =', '0,25', ['0,4', '0,5', '1'], '', 1),
    mc('Was ist die Lehre aus dem Regelvergleich?', 'keine Regel ist „die richtige“', ['Laplace ist immer richtig', 'Maximin ist immer richtig', 'alle wählen gleich'], '', 2))

t = 'bayes'
fam(t, 'by', 'Rechnet Erwartungswerte',
    nu('p₁ = {P} %, p₂ = {=100-P} %. Ergebnisse {A} und {B}. Erwartungswert?', {'P': [10, 90, 10], 'A': [50000, 200000, 10000], 'B': [20000, 150000, 10000]}, 'P/100*A+(1-P/100)*B', '{=P/100} · {A} + {=1-P/100} · {B} = {=P/100*A+(1-P/100)*B}', '€', 0, lvl=2, kl=True),
    ns('Randlage: 150.000 (p = 0,7) oder 80.000 (p = 0,3). Erwartungswert?', 129000, '105.000 + 24.000', '€', 2, True),
    mc('Kritik an der Bayes-Regel:', 'unterstellt Risikoneutralität', ['braucht keine Zahlen', 'ist zu pessimistisch', 'gilt nur für Laplace'], '', 2, True),
    mc('µ steht für …', 'Erwartungswert', ['Bedauern', 'Optimismus', 'Nutzen'], '', 1),
    mc('Sonnig 50 %, wechselhaft 30 %, Regen 20 %. A (100, 60, 10), B (70, 70, 50). Bayes wählt …', 'A (70 gegen 66)', ['B (66 gegen 70)', 'beide gleich', 'keine'], '', 3, True),
    blk('Richtig oder falsch?', [('Die Wahrscheinlichkeiten müssen zusammen 1 ergeben.', True), ('Bayes ist eine Regel unter Ungewissheit.', False), ('Bei vielen Wiederholungen ist Bayes sinnvoll.', True), ('Bayes berücksichtigt die Risikoeinstellung.', False)], '', 2, True),
    mc('Welche Regel berücksichtigt zusätzlich die Risikoeinstellung?', 'Bernoulli-Prinzip', ['Laplace', 'Maximax', 'Zieldominanz'], '', 2),
    lu('E(a) = Σ [[0]] · e', [['p', 'Wahrscheinlichkeit', 'p_j']], '', 2))

t = 'bernoulli'
fam(t, 'be', 'Wendet das Bernoulli-Prinzip an',
    rh('Ordne die Schritte.', ['Nutzenfunktion anwenden (Nutzenmatrix)', 'mit Wahrscheinlichkeiten gewichten', 'Erwartungsnutzen vergleichen'], '', 1),
    ns('u(e) = 300e − e². Nutzen von e = 30?', 8100, '9.000 − 900', '', 2),
    ns('Weizen: Nutzen 40 / 60 / 100 bei p = 0,1 / 0,3 / 0,6. Erwartungsnutzen?', 82, '4 + 18 + 60', '', 2),
    ns('Erdbeeren: Nutzen 110 / 90 / 80 bei p = 0,1 / 0,3 / 0,6. Erwartungsnutzen?', 86, '11 + 27 + 48', '', 2),
    mc('Beim Bernoulli-Prinzip zählt …', 'der erwartete Nutzen', ['der erwartete Geldbetrag', 'das schlechteste Ergebnis', 'das Bedauern'], '', 1),
    mc('u(e) = √e beschreibt einen Entscheider, der …', 'risikoscheu ist', ['risikofreudig ist', 'risikoneutral ist', 'nur Verluste sieht'], 'Konkave Nutzenfunktion.', 3),
    nu('u(e) = √e. Ergebnis {Q} € (Quadratzahl). Nutzen?', {'Q': [100, 10000, 100]}, 'sqrt(Q)', '√{Q} = {=sqrt(Q)}', '', 0, wenn='sqrt(Q) == int(sqrt(Q))', lvl=1),
    mc('Typischer Fehler beim Bernoulli-Prinzip:', 'erst Erwartungswert, dann Nutzen', ['erst Nutzen, dann Erwartungswert', 'Wahrscheinlichkeiten addieren', 'Matrix transponieren'], '', 2))

# ================= k8 =================
t = 'begrenzte-rationalitaet'
fam(t, 'br', 'Erklärt begrenzte Rationalität',
    li('Warum ist Rationalität begrenzt? Nennen Sie drei Gründe.', [['unvollständiges Wissen', 'Wissen', 'Information'], ['nicht alle Optionen', 'Handlungsoptionen', 'Alternativen'], ['instabile Präferenzen', 'Präferenzen']], '', 2),
    mc('Begrenzt rationale Menschen …', 'wollen rational handeln, stoßen an Grenzen', ['handeln zufällig', 'handeln immer perfekt', 'haben keine Ziele'], '', 1),
    zu('Wer gehört wozu?', ['Begründer begrenzte Rationalität', 'Prospect Theory'], [('Herbert Simon', 0), ('Daniel Kahneman', 1), ('Chester Barnard', 0), ('Cyert und March', 0)], '', 2),
    mc('Lena vergleicht nur drei empfohlene Röstmaschinen. Welche Grenze zeigt sich?', 'unvollständiges Wissen', ['instabile Präferenzen', 'Risikoneutralität', 'Zieldominanz'], '', 2),
    mc('Simon erhielt den Nobelpreis …', '1978', ['1898', '1912', '2002'], '', 2),
    kz('Englischer Begriff für begrenzte Rationalität?', ['bounded rationality'], '', 1),
    mc('Welches Menschenbild steht im Gegensatz?', 'homo oeconomicus', ['Stakeholder', 'Komplementär', 'Question Mark'], '', 1),
    mc('Nach einer Messe findet Lena Design plötzlich wichtiger. Welche Grenze?', 'instabile Präferenzen', ['unvollständiges Wissen', 'Suchkosten', 'Ankereffekt'], '', 2))

t = 'prospect-theory'
fam(t, 'pt', 'Erkennt Effekte der Prospect Theory',
    mc('Sicher 240 € oder 25 % Chance auf 1.000 €: Die meisten wählen …', 'die sicheren 240 €', ['die Chance', 'gar nichts', 'beides'], 'Risikoscheu im Gewinnfall.', 1),
    mc('Sicher −750 € oder 75 % Chance auf −1.000 €: Die meisten wählen …', 'die Chance', ['den sicheren Verlust', 'gar nichts', 'beides'], 'Risikofreudig im Verlustfall.', 1),
    zu('Welcher Effekt?', ['Besitztum', 'Anker', 'Overconfidence', 'Sunk Cost'], [('Tasse: Besitzer verlangen mehr', 0), ('7.500 an der Tafel', 1), ('„Bei mir geht nichts schief“', 2), ('Tennishalle bezahlt, trotz Sonne drinnen', 3)], '', 2),
    hotpunkt('Tippe auf den Bereich der Wertfunktion, in dem Menschen risikofreudig sind.', achse(20, 120, 350, 10) + linie([(180, 120), (220, 90), (270, 72), (340, 64)]) + linie([(180, 120), (150, 170), (110, 210), (40, 232)], 'var(--dg-b)'),
             (120, 200, 50), 'Verlustbereich (links unten).', 2, H=240),
    mc('Asiatische Grippe: Warum wählen Menschen je nach Formulierung anders?', 'Framing verschiebt den Referenzpunkt', ['Zahlen sind verschieden', 'Zufall', 'Bayes-Regel'], '', 3),
    mc('Verluste wiegen etwa …', 'doppelt so schwer wie Gewinne', ['halb so schwer', 'gleich schwer', 'gar nicht'], '', 2),
    blk('Richtig oder falsch?', [('Im Gewinnfall sind Menschen risikoscheu.', True), ('Der Ankereffekt betrifft bereits bezahlte Kosten.', False), ('Prospect Theory stammt von Kahneman und Tversky.', True), ('Besitz wird typischerweise unterbewertet.', False)], '', 2),
    mc('„Ich habe das Konzertticket bezahlt, also gehe ich krank hin.“', 'Sunk Cost', ['Ankereffekt', 'Besitztumseffekt', 'Overconfidence'], '', 1))

t = 'garbage-can'
fam(t, 'gc', 'Kennt das Garbage-Can-Modell',
    bes('Beschrifte das Garbage-Can-Modell.', [(4, 6, 110, 40, 'Teilnehmer'), (124, 6, 110, 40, 'Probleme'), (244, 6, 110, 40, 'Lösungen'), (60, 80, 240, 46, 'Entscheidungsgelegenheit')], ['Zielsystem'], '', 2,
        deko=_pfeil(60, 48, 140, 78) + _pfeil(180, 48, 180, 78) + _pfeil(300, 48, 220, 78)),
    li('Wie kommt es im Garbage-Can-Modell zu Entscheidungen?', [['Übersehen'], ['Flucht'], ['Problemlösung', 'Lösung']], '', 2),
    mc('Organisationale Entscheidungen sind laut Modell geprägt von …', 'Ambiguität', ['vollständiger Information', 'Risikoneutralität', 'Zieldominanz'], '', 1),
    mc('Ziele im Garbage-Can-Modell sind …', 'instabil, schlecht definiert', ['klar und stabil', 'immer quantitativ', 'vom Staat vorgegeben'], '', 2),
    mc('„Entscheidung durch Flucht“ heißt:', 'Problem wandert ab, dann wird entschieden', ['Teilnehmer verlassen die Firma', 'Lösung wird verboten', 'man entscheidet nie'], '', 3),
    kz('Wie heißt das Modell auf Deutsch?', ['Mülleimer-Modell', 'Mülleimermodell', 'Mülleimer'], '', 1),
    mc('Das Garbage-Can-Modell gehört zur …', 'verhaltenswiss. Entscheidungstheorie', ['klassischen Entscheidungstheorie', 'Kostenrechnung', 'Five-Forces-Analyse'], '', 1))

# ================= k9 =================
t = 'fuehrung'
fam(t, 'ph', 'Kennt die fünf Phasen der Unternehmensführung',
    rh('Ordne die Phasen.', ['Zielsetzung', 'Umweltanalyse', 'Unternehmensanalyse', 'Strategiewahl', 'Implementierung und Kontrolle'], '', 1),
    zu('Welche Phase nutzt das Werkzeug?', ['Umweltanalyse', 'Unternehmensanalyse', 'Strategiewahl'], [('Five Forces', 0), ('SWOT', 1), ('Ansoff-Matrix', 2), ('BCG-Matrix', 1), ('Porters Wettbewerbsstrategien', 2)], '', 2),
    zu('Wer sagte das über Strategie?', ['Clausewitz', 'Porter', 'Simon'], [('Gebrauch des Gefechts zum Zweck des Krieges', 0), ('stimmige Anordnung von Aktivitäten', 1), ('profitables Überleben sichern', 2)], '', 3),
    li('Welche drei Fragen beantwortet eine Strategie?', [['Ziele', 'wo wollen wir hin'], ['Ausgangslage', 'wo sind wir'], ['Weg', 'wie kommen wir dahin']], '', 2),
    mc('Die Umweltanalyse schaut …', 'nach außen', ['nach innen', 'nur auf Kosten', 'nur auf Mitarbeiter'], '', 1),
    hot('Tippe auf die Phase, in der die SWOT-Analyse stattfindet.', [(4, 6, 220, 36, 'Zielsetzung'), (38, 50, 220, 36, 'Umweltanalyse'), (72, 94, 220, 36, 'Unternehmensanalyse'), (106, 138, 220, 36, 'Strategiewahl'), (140, 182, 216, 36, 'Implementierung')], 2, '', 2),
    mc('Ergibt die Kontrolle große Abweichungen, …', 'beginnt der Kreislauf neu', ['ist die Strategie fertig', 'wird nichts geändert', 'endet das Unternehmen'], '', 2),
    mc('Phase 5 heißt …', 'Implementierung und Kontrolle', ['Strategiewahl', 'Umweltanalyse', 'Zielsetzung'], '', 1))

t = 'zielhierarchie'
fam(t, 'zh', 'Ordnet die Zielhierarchie',
    rh('Ordne von oben nach unten.', ['Vision', 'Unternehmensleitbild', 'Unternehmensziele', 'Geschäftsbereichsziele', 'Funktionsziele'], '', 1),
    zu('Welche Stufe?', ['Vision', 'Unternehmensziel', 'Geschäftsbereichsziel', 'Funktionsziel'], [('„A car for everybody“', 0), ('Konzernumsatz 250 Mio. €', 1), ('Sparte Trucks: Marktanteil 5 %', 2), ('Einkauf: Materialkosten −3 %', 3)], '', 2),
    mc('Marketing ist …', 'eine Funktion', ['ein Geschäftsbereich', 'eine Vision', 'ein Leitbild'], '', 1),
    mc('Je weiter unten in der Pyramide, desto …', 'konkreter', ['abstrakter', 'unwichtiger', 'langfristiger'], '', 1),
    bes('Beschrifte die Zielpyramide.', [(140, 6, 80, 36, 'Vision'), (110, 48, 140, 36, 'Leitbild'), (80, 90, 200, 36, 'Unternehmensziele'), (50, 132, 260, 36, 'Geschäftsbereichsziele'), (20, 174, 320, 36, 'Funktionsziele')], ['Strategiewahl'], '', 2),
    mc('Für die Vorlesung sind Vision und Leitbild …', 'fast ein Punkt', ['Gegensätze', 'unwichtig', 'Funktionsziele'], '', 2),
    li('Was gehört zu einem guten Ziel?', [['Inhalt', 'was'], ['Ausmaß', 'wie viel'], ['Zeitbezug', 'bis wann', 'Zeit']], '', 3),
    mc('„If you have a body, you are an athlete“ ist …', 'ein Leitbild', ['ein Funktionsziel', 'ein Geschäftsbereich', 'eine Kennzahl'], '', 1))

t = 'umweltanalyse'
fam(t, 'uw', 'Ordnet Umweltfaktoren',
    zu('Welche Umwelt?', ['politisch', 'wirtschaftlich', 'gesellschaftlich', 'rechtlich'], [('Zölle', 0), ('Zinsen steigen', 1), ('Lauftrend', 2), ('neue EU-Vorschrift', 3)], '', 1),
    zu('Allgemeine Umwelt oder Wettbewerbsumfeld?', ['Umwelt', 'Wettbewerbsumfeld'], [('Konjunktur', 0), ('Konkurrent senkt Preise', 1), ('Gesetzesänderung', 0), ('Markt wächst', 1)], '', 2),
    mc('Instrument für das Wettbewerbsumfeld:', 'Five Forces', ['SWOT', 'BCG-Matrix', 'Laplace'], '', 1),
    li('Nennen Sie die vier Bereiche der allgemeinen Umwelt.', [['politisch'], ['wirtschaftlich'], ['gesellschaftlich'], ['rechtlich']], '', 2),
    mc('„Weltweit Markt für fünf Computer“ zeigt …', 'Fehleinschätzungen der Umwelt', ['Economies of Scale', 'Arbitrage', 'Zieldominanz'], '', 2),
    hot('Tippe auf das Wettbewerbsumfeld.', [(4, 4, 352, 210, ''), (36, 70, 288, 130, ''), (110, 120, 140, 50, 'Unternehmen')], 1, '', 2, deko='') ,
    mc('Umweltanalyse vs. Unternehmensanalyse:', 'außen vs. innen', ['innen vs. außen', 'Kosten vs. Erlöse', 'Ziele vs. Mittel'], '', 1),
    mc('Was wirkt auf alle Unternehmen einer Branche gleichermaßen?', 'die allgemeine Umwelt', ['die eigenen Ressourcen', 'die Funktionsziele', 'die BCG-Position'], '', 3))

t = 'five-forces'
fam(t, 'ff', 'Kennt und nutzt Porters Five Forces',
    bes('Beschrifte die fünf Kräfte.', [(110, 76, 140, 60, 'Rivalität'), (100, 4, 160, 50, 'neue Konkurrenz'), (100, 158, 160, 50, 'Ersatzprodukte'), (4, 76, 96, 60, 'Lieferanten'), (260, 76, 96, 60, 'Abnehmer')], ['Staat'], '', 2, kl=True,
        deko=_pfeil(180, 56, 180, 74) + _pfeil(180, 156, 180, 138) + _pfeil(100, 106, 108, 106) + _pfeil(260, 106, 252, 106)),
    li('Nennen Sie Porters fünf Kräfte.', [['Rivalität', 'Wettbewerb in der Branche'], ['neue Konkurrenz', 'neue Anbieter', 'Markteintritt'], ['Ersatzprodukte', 'Substitute'], ['Lieferanten'], ['Abnehmer', 'Kunden']], '', 2, kl=True),
    zu('Welche Kraft?', ['Rivalität', 'neue Konkurrenz', 'Ersatzprodukte', 'Lieferanten', 'Abnehmer'], [('Fernbus statt Bahn', 2), ('Zulieferer droht, selbst Autos zu bauen', 3), ('Handelskette drückt Preise', 4), ('Online-Marken drängen in den Markt', 1), ('viele etablierte Wettbewerber', 0)], '', 2, kl=True),
    mc('Hohe Austrittsbarrieren …', 'erhöhen die Rivalität', ['senken die Rivalität', 'senken Eintritte', 'sind Ersatzprodukte'], '', 2),
    mc('Wächst die Branche, …', 'sinkt die Rivalität', ['steigt die Rivalität', 'steigt die Abnehmermacht', 'entstehen Substitute'], '', 2),
    li('Was treibt die Bedrohung durch Ersatzprodukte?', [['Technologiewandel', 'Technologie'], ['Kostenvorteile', 'günstiger'], ['geringe Umstellungskosten', 'Umstellungskosten'], ['Wechselneigung', 'wechseln']], '', 3, n=3),
    mc('Lebensmittelhandel mit 1 % Marge zeigt …', 'hohe Rivalität', ['hohe Lieferantenmacht', 'Netzwerkeffekte', 'Monopol'], '', 2),
    mc('Zu welcher Analyse-Sicht gehören die Five Forces?', 'Market-based View', ['Resource-based View', 'Bernoulli-Prinzip', 'Garbage Can'], '', 3))

t = 'markteintritt'
fam(t, 'me', 'Erkennt Markteintrittsbarrieren',
    zu('Welche Barriere?', ['Vertrauen', 'Politik', 'Wirtschaft'], [('Referenzen', 0), ('Lizenzpflicht', 1), ('Economies of Scale', 2), ('Käuferpfadabhängigkeit', 0), ('Netzwerkeffekt', 2), ('Regalplätze im Handel', 0)], '', 2),
    mc('WhatsApp ist schwer zu ersetzen, weil …', 'alle es nutzen (Netzwerkeffekt)', ['es billig ist (Scale)', 'es Patente hat', 'es staatlich ist'], '', 1),
    mc('McCafé im McDonald’s ist ein …', 'räumlicher Verbundeffekt', ['Netzwerkeffekt', 'Größeneffekt', 'Patent'], '', 2),
    nu('Werkzeug {F} €, variable Kosten {V} € je Paar. Stückkosten bei {X} Paar?', {'F': [20000, 100000, 10000], 'V': [10, 30, 5], 'X': [1000, 20000, 1000]}, 'F/X+V', '{F} ÷ {X} + {V} = {=F/X+V} €', '€', 2, wenn='(F/X) == round(F/X, 2)', lvl=2),
    mc('Bosch mit dem ABS-Patent hatte …', 'absolute Kostenvorteile', ['Economies of Scope', 'Netzwerkeffekte', 'Referenzbarrieren'], '', 2),
    mc('Hohe Eintrittsbarrieren bedeuten …', 'geringe Bedrohung durch Neue', ['hohe Bedrohung', 'hohe Rivalität', 'viele Substitute'], '', 1),
    mc('Welche Rente entsteht durch Eintrittsbarrieren?', 'Monopol-Rente', ['Ricardo-Rente', 'Quasi-Rente', 'Schumpeter-Rente'], '', 3),
    mc('Unternehmensberater: rechtliche Hürde niedrig, aber …', 'Vertrauensbarriere hoch', ['Scale hoch', 'Netzwerkeffekt hoch', 'Patente nötig'], '', 2))

t = 'verhandlungsmacht'
fam(t, 'vm', 'Schätzt Verhandlungsmacht ein',
    zu('Wer ist mächtiger?', ['Lieferant', 'Abnehmer'], [('einziger Hersteller eines Spezialchips', 0), ('Standardschrauben von 50 Firmen', 1), ('Kunde macht 60 % des Umsatzes', 1), ('Lieferant droht mit eigenen Läden', 0)], '', 2),
    zu('Vorwärts- oder Rückwärtsintegration?', ['vorwärts', 'rückwärts'], [('Blechnerei will selbst Autos bauen', 0), ('Autohersteller macht Blech selbst', 1)], '', 1),
    mc('Lieferanten sind mächtig, wenn die Substitutionsgefahr …', 'gering ist', ['hoch ist', 'egal ist', 'staatlich ist'], '', 2),
    mc('Standardisierte Produkte stärken …', 'die Abnehmer', ['die Lieferanten', 'die Rivalität', 'den Staat'], '', 2),
    mc('VW und Prevent zeigen:', 'Abhängigkeit von einem Lieferanten ist riskant', ['große Firmen sind unangreifbar', 'Lieferanten sind machtlos', 'Abnehmer bestimmen immer'], '', 2),
    bes('Beschrifte die Drohungen.', [(4, 70, 100, 50, '=Lieferant'), (130, 70, 100, 50, '=Unternehmen'), (256, 70, 100, 50, '=Abnehmer'), (4, 4, 230, 40, 'Rückwärtsintegration'), (4, 150, 230, 40, 'Vorwärtsintegration')], ['Diversifikation'], '', 3,
        deko=_pfeil(106, 95, 128, 95) + _pfeil(232, 95, 254, 95) + _pfeil(180, 68, 70, 46) + _pfeil(54, 122, 160, 148)),
    mc('Was senkt die Abhängigkeit von einem Lieferanten?', 'zweiten Lieferanten aufbauen', ['Auftragsvolumen kürzen', 'Preise erhöhen', 'Produkt standardisieren'], '', 2),
    mc('Ein kleiner Zulieferer, für den der Auftrag nebensächlich ist, hat …', 'große Verhandlungsmacht', ['keine Macht', 'kleine Macht', 'Abnehmermacht'], '', 3))

# ================= k10 =================
t = 'swot'
fam(t, 'sw', 'Nutzt die SWOT-Analyse',
    zu('Intern oder extern?', ['intern', 'extern'], [('Strengths', 0), ('Weaknesses', 0), ('Opportunities', 1), ('Threats', 1)], '', 1, True),
    zu('Welche Strategie?', ['SO', 'ST', 'WO', 'WT'], [('Stärken nutzen, Chancen ergreifen', 0), ('Stärken nutzen, Bedrohungen abwehren', 1), ('Schwächen ausgleichen, Chancen nutzen', 2), ('Schwächen ausgleichen, Bedrohungen abwehren', 3)], '', 2, True),
    zu('Stride: was ist was?', ['S', 'W', 'O', 'T'], [('starke Entwicklung', 0), ('kein Onlineshop', 1), ('Trail-Boom', 2), ('Billiganbieter', 3)], '', 2, True),
    rh('Ordne die drei Schritte der SWOT.', ['ermitteln', 'bewerten', 'Handlungsempfehlungen ableiten'], '', 1, True),
    hot('Tippe auf das Feld für „Stärken nutzen, um Chancen zu ergreifen“.', [(80, 30, 136, 90, ''), (220, 30, 136, 90, ''), (80, 124, 136, 90, ''), (220, 124, 136, 90, '')], 0, '', 2, True,
        deko=_txt(148, 16, 'Opportunities', 12, 700) + _txt(288, 16, 'Threats', 12, 700) + _txt(40, 75, 'Strengths', 12, 700) + _txt(40, 169, 'Weaknesses', 12, 700)),
    li('Nennen Sie Grenzen der SWOT-Analyse.', [['subjektiv', 'Einordnung'], ['Momentaufnahme', 'statisch'], ['erst Kombination liefert Empfehlung', 'Kombination', 'keine Empfehlung']], '', 3, True, n=2),
    mc('Ein Lauftrend ist …', 'eine Chance', ['eine Stärke', 'eine Schwäche', 'eine Bedrohung'], '', 1, True),
    mc('Die SWOT verbindet …', 'Markt- und Ressourcensicht', ['Kosten und Erlöse', 'Ziele und Mittel', 'Vision und Leitbild'], '', 3))

t = 'mbv-rbv'
fam(t, 'mr', 'Unterscheidet MBV und RBV',
    zu('MBV oder RBV?', ['Market-based', 'Resource-based'], [('outside-in', 0), ('inside-out', 1), ('Marktanteile', 0), ('Ressourcenvorteile', 1), ('kurzfristig', 0), ('langfristig', 1), ('Profit Center', 0), ('Center of Competence', 1)], '', 1),
    mc('Wettbewerbsvorteil im RBV:', 'dauerhaft, schwer angreifbar', ['zeitlich befristet', 'sofort kopierbar', 'staatlich garantiert'], '', 2),
    mc('Instrument des MBV:', 'Five Forces', ['Ressourcenanalyse', 'Laplace', 'Rentenanalyse'], '', 1),
    mc('Ein Discounter mit einzigartiger Logistik-Kultur erklärt seinen Erfolg aus Sicht des …', 'RBV', ['MBV', 'Shareholder Value', 'Bernoulli'], '', 2),
    lu('Der Market-based View denkt [[0]], der Resource-based View [[1]].', [['outside-in', 'von außen nach innen'], ['inside-out', 'von innen nach außen']], '', 2),
    mc('Wettbewerbsobjekt im RBV:', 'Chancenanteile', ['Marktanteile', 'Kunden', 'Preise'], '', 3),
    mc('Planungshorizont im MBV:', 'kurzfristig', ['langfristig', 'unendlich', 'keiner'], '', 2),
    blk('Richtig oder falsch?', [('Der RBV sieht das Unternehmen als Ressourcenreservoir.', True), ('Der MBV schaut von innen nach außen.', False), ('Beide Sichten ergänzen sich.', True), ('Im MBV sind Vorteile dauerhaft.', False)], '', 2))

t = 'ressourcen'
fam(t, 'rs', 'Prüft Ressourcen auf Wettbewerbsvorteile',
    mc('Holzerei (3 Mitarbeiter) stellt einen Elektroingenieur ein. Welche Voraussetzung ist verletzt?', 'spezifisch', ['Seltenheit', 'Imitation', 'Substitution'], '', 2, True),
    li('Nennen Sie die vier Prüffragen der Ressourcenanalyse.', [['spezifisch'], ['selten'], ['Imitation', 'imitieren'], ['Substitution', 'ersetzen']], '', 2, True),
    zu('Welche Ressourcenart?', ['materiell', 'organisatorisch', 'human'], [('Maschinen', 0), ('Produktionsprozesse', 1), ('Fertigkeiten', 2), ('Finanzanlagen', 0), ('Verfahrensweisen', 1), ('Fähigkeiten', 2)], '', 2),
    mc('Wann entsteht ein Wettbewerbsvorteil?', 'alle vier Fragen ja', ['eine Frage ja', 'nur selten', 'nur spezifisch'], '', 1, True),
    bes('Beschrifte den Ressourcenbaum.', [(130, 4, 100, 34, '=Ressourcen'), (20, 60, 140, 40, 'materiell'), (200, 60, 140, 40, 'immateriell'), (160, 130, 90, 40, 'organisatorisch'), (260, 130, 90, 40, 'human')], ['finanziell'], '', 2,
        deko=_pfeil(160, 40, 90, 58) + _pfeil(200, 40, 270, 58) + _pfeil(250, 102, 205, 128) + _pfeil(290, 102, 305, 128)),
    mc('McDonald’s Vorteil liegt laut Vorlesung eher in …', 'Prozessen', ['besseren Mitarbeitern', 'Patenten', 'Grundstücken'], '', 2),
    mc('SAP-Beratung mit seltenem Branchenwissen hat …', 'einen Wettbewerbsvorteil', ['einen Nachteil', 'keinen Vorteil', 'eine Monopolrente'], '', 2, True),
    mc('Zu welcher Sicht gehört die Ressourcenanalyse?', 'Resource-based View', ['Market-based View', 'Five Forces', 'Laplace'], '', 1))

t = 'renten'
fam(t, 'rn', 'Ordnet Sachverhalte Rentenarten zu',
    mc('Einem Unternehmen gelingt es, Skaleneffekte zu erzielen. Welche Rente?', 'Monopol-Rente', ['Ricardo-Rente', 'Quasi-Rente', 'Schumpeter-Rente'], 'Skaleneffekte stehen bei Monopol-Renten.', 2, True),
    zu('Welche Rente?', ['Ricardo', 'Quasi', 'Monopol', 'Schumpeter'], [('billige Energie am Standort', 0), ('optimale Teamzusammenstellung', 1), ('starkes Image', 2), ('Pionier mit neuer App', 3), ('High Potentials in Metropolregion', 0), ('innovationsfördernde Praktiken', 3)], '', 2, True),
    zu('Welche Verortung?', ['input', 'intermediär', 'output'], [('Ricardo', 0), ('Quasi', 1), ('Schumpeter', 2)], '', 2, True),
    mc('Ricardo-Renten entstehen aus …', 'knappen Ressourcen', ['Innovation', 'Marktmacht', 'Teamarbeit'], '', 1, True),
    mc('Schumpeter-Renten heißen auch …', 'Pioniergewinne', ['Grundrenten', 'Zinsen', 'Dividenden'], '', 2, True),
    mc('Ricardo vs. Quasi:', 'Besitz vs. Einsatz', ['Einsatz vs. Besitz', 'Input vs. Output', 'Zins vs. Gewinn'], '', 3, True),
    blk('Richtig oder falsch?', [('Monopol-Renten können input- oder output-orientiert sein.', True), ('Quasi-Renten sind output-orientiert.', False), ('Überdurchschnittliche Vergütung steht bei Monopol-Renten.', True), ('Ricardo-Renten entstehen durch Innovation.', False)], '', 3, True),
    mc('Welche Rente passt zur schöpferischen Zerstörung?', 'Schumpeter-Rente', ['Ricardo-Rente', 'Quasi-Rente', 'Monopol-Rente'], '', 2))

t = 'lebenszyklus'
fam(t, 'lz', 'Kennt den Lebenszyklus',
    rh('Ordne die Phasen.', ['Einführung', 'Wachstum', 'Reife', 'Sättigung'], '', 1),
    zu('Welche Phase?', ['Einführung', 'Wachstum', 'Reife', 'Sättigung'], [('Verlust, hohe Investitionen', 0), ('Gewinnschwelle überschritten', 1), ('Umsatz-Maximum', 2), ('Umsatz sinkt', 3)], '', 2),
    hotpunkt('Tippe auf das Umsatz-Maximum.', achse(30, 200, 350, 10, 'Zeit', 'Umsatz') + linie([(30 + i * 8, 200 - 160 * __import__('math').exp(-((i - 22) / 9) ** 2)) for i in range(0, 40)]),
             (30 + 22 * 8, 40, 22), 'In der Reifephase.', 1),
    mc('Was tut man in der Sättigung?', 'Relaunch oder Rückzug', ['Kapazität ausbauen', 'Markt erschließen', 'nichts'], '', 2),
    mc('Ist der Lebenszyklus ein Naturgesetz?', 'nein, idealisiert', ['ja', 'nur für Autos', 'nur für Software'], '', 1),
    mc('Produkte in der Reife sind in der BCG-Matrix oft …', 'Cash Cows', ['Stars', 'Question Marks', 'Poor Dogs'], '', 3),
    mc('Ein Facelift beim Auto …', 'verlängert den Zyklus', ['beendet ihn', 'startet die Einführung', 'senkt die Qualität'], '', 2),
    mc('In welcher Phase macht ein Produkt meist Verlust?', 'Einführung', ['Wachstum', 'Reife', 'Sättigung'], '', 1))

t = 'erfahrungskurve'
fam(t, 'ek', 'Wendet die Erfahrungskurve an',
    nu('Stückkosten {K} €, Senkung {R} % je Verdopplung. Kosten nach einer Verdopplung?', {'K': [20, 200, 10], 'R': [20, 30, 5]}, 'K*(1-R/100)', '{K} · {=1-R/100} = {=K*(1-R/100)} €', '€', 2, lvl=2),
    nu('Stückkosten {K} €, Senkung 20 % je Verdopplung. Kosten nach zwei Verdopplungen?', {'K': [25, 250, 25]}, 'K*0.64', '{K} · 0,8 · 0,8 = {=K*0.64} €', '€', 2, lvl=3),
    li('Nennen Sie Ursachen der Erfahrungskurve.', [['Lerneffekte', 'Lernen'], ['Spezialisierung'], ['Rationalisierung', 'Automatisierung'], ['Know-how', 'technischer Fortschritt']], '', 2, n=3),
    mc('Um wie viel sinken die Kosten je Verdopplung?', '20–30 %', ['50 %', '5 %', '100 %'], '', 1),
    mc('Bezugsgröße der Erfahrungskurve:', 'kumulierte Menge', ['Menge je Jahr', 'Umsatz', 'Mitarbeiterzahl'], '', 2),
    mc('Erfahrungskurve vs. Economies of Scale:', 'kumuliert vs. je Periode', ['je Periode vs. kumuliert', 'gleich', 'Kosten vs. Preis'], '', 3),
    mc('Nutzen der Erfahrungskurve:', 'Kosten der Konkurrenz schätzen', ['Elastizität bestimmen', 'Vision formulieren', 'Haftung klären'], '', 2),
    mc('Was folgt strategisch aus der Erfahrungskurve?', 'früh Marktanteile gewinnen', ['spät in den Markt', 'kleine Mengen produzieren', 'Preise erhöhen'], '', 3))

t = 'bcg-matrix'
fam(t, 'bcg', 'Nutzt die BCG-Matrix',
    bes('Beschrifte die BCG-Matrix (oben hohes Wachstum, rechts hoher Marktanteil).', [(50, 10, 150, 90, 'Question Marks'), (206, 10, 150, 90, 'Stars'), (50, 106, 150, 90, 'Poor Dogs'), (206, 106, 150, 90, 'Cash Cows')], ['Nische'], '', 1, True,
        deko=_pfeil(44, 200, 360, 200) + _pfeil(44, 200, 44, 4)),
    zu('Welche Empfehlung?', ['investieren', 'melken', 'beenden', 'alles oder raus'], [('Stars', 0), ('Cash Cows', 1), ('Poor Dogs', 2), ('Question Marks', 3)], '', 1, True),
    mc('Niedriges Wachstum, hoher Marktanteil:', 'Cash Cow', ['Star', 'Poor Dog', 'Question Mark'], '', 1, True),
    nu('Eigener Marktanteil {A} %, größter Konkurrent {B} %. Relativer Marktanteil?', {'A': [2, 40, 2], 'B': [10, 50, 5]}, 'A/B', '{A} ÷ {B} = {=A/B}', '', 2, wenn='A/B == round(A/B, 2)', lvl=2),
    zu('Stride einordnen:', ['Question Mark', 'Cash Cow', 'Poor Dog'], [('Trail: Markt +15 %, kleiner Anteil', 0), ('Straße: Markt +1 %, Marktführer', 1), ('Halle: Markt schrumpft, kleiner Anteil', 2)], '', 2, True),
    mc('Achsen der BCG-Matrix:', 'Wachstum und rel. Marktanteil', ['Umsatz und Gewinn', 'Preis und Menge', 'Zeit und Kosten'], '', 1, True),
    mc('Woher kommt das Geld für Stars?', 'von den Cash Cows', ['von den Poor Dogs', 'vom Staat', 'aus Question Marks'], '', 2),
    mc('Relativer Marktanteil > 1 heißt …', 'Marktführer', ['Nischenanbieter', 'Neueinsteiger', 'Verlustbringer'], '', 3))

# ================= k11 =================
t = 'ansoff'
fam(t, 'an', 'Ordnet Produkt-Markt-Strategien',
    bes('Beschrifte die Ansoff-Matrix (oben bestehender Markt, links bestehendes Produkt).', [(60, 10, 146, 90, 'Marktdurchdringung'), (210, 10, 146, 90, 'Produktentwicklung'), (60, 106, 146, 90, 'Marktentwicklung'), (210, 106, 146, 90, 'Diversifikation')], ['Kostenführerschaft'], '', 1),
    zu('Welches Feld?', ['Durchdringung', 'Produktentw.', 'Marktentw.', 'Diversifikation'], [('Rabatt auf alte Schuhe in Deutschland', 0), ('neue Trail-Serie für bisherige Kunden', 1), ('alte Schuhe nach Japan', 2), ('Fitnessstudios eröffnen', 3)], '', 2),
    mc('Höchstes Risiko:', 'Diversifikation', ['Marktdurchdringung', 'Marktentwicklung', 'Produktentwicklung'], '', 1),
    mc('Milchpulver für Kinder wird an Erwachsene in China verkauft:', 'Marktentwicklung', ['Produktentwicklung', 'Diversifikation', 'Marktdurchdringung'], '', 2),
    mc('Ansoff gehört zur Ebene …', 'Unternehmensstrategie', ['Funktionalstrategie', 'Geschäftsbereich', 'Vision'], '', 3),
    mc('Haferflocken → Porridge:', 'Produktentwicklung', ['Marktentwicklung', 'Diversifikation', 'Marktdurchdringung'], '', 1),
    mc('Welches Feld wählen Unternehmen meist zuerst?', 'Marktdurchdringung', ['Diversifikation', 'Marktentwicklung', 'Produktentwicklung'], '', 2),
    blk('Richtig oder falsch?', [('Neues Produkt im alten Markt = Produktentwicklung.', True), ('Altes Produkt im neuen Markt = Diversifikation.', False), ('Diversifikation: neues Produkt, neuer Markt.', True), ('Marktdurchdringung hat das höchste Risiko.', False)], '', 2))

t = 'porter-strategien'
fam(t, 'po', 'Ordnet Wettbewerbsstrategien',
    zu('Welche Strategie?', ['Kostenführer', 'Differenzierung', 'Nische'], [('Ryanair', 0), ('Apple', 1), ('Montblanc', 2), ('Aldi', 0), ('Nike', 1)], '', 1),
    kz('Wie nennt Porter Firmen, die weder Kostenführer noch Differenzierer sind?', ['stuck in the middle'], '', 2),
    bes('Beschrifte Porters Matrix (oben branchenweit, unten Segment).', [(40, 10, 156, 90, 'Differenzierung'), (200, 10, 156, 90, 'Kostenführerschaft'), (40, 106, 316, 60, 'Nische')], ['Diversifikation'], '', 2),
    mc('Die Nische zielt auf …', 'ein Marktsegment', ['die ganze Branche', 'alle Länder', 'nur Kosten'], '', 1),
    mc('Kostenführerschaft heißt …', 'niedrigste Kosten der Branche', ['schlechteste Qualität', 'höchster Preis', 'kleinste Menge'], '', 2),
    mc('Porters Strategien gehören zur Ebene …', 'Geschäftsbereich', ['Unternehmen', 'Funktion', 'Vision'], '', 3),
    mc('Welche Strategie passt zu hohen Erfahrungskurveneffekten?', 'Kostenführerschaft', ['Nische', 'Differenzierung', 'Diversifikation'], '', 3),
    mc('Differenzierung heißt …', 'der Beste sein', ['der Günstigste sein', 'klein bleiben', 'alles anbieten'], '', 1))

t = 'implementierung'
fam(t, 'im', 'Kennt Implementierung und Kontrolle',
    rh('Ordne die Schritte.', ['Implementierungsplanung', 'Umsetzung', 'Implementierungskontrolle'], '', 1),
    nu('Plan {S} Paar, verkauft {I} Paar. Zielerreichungsgrad?', {'S': [1000, 10000, 1000], 'I': [500, 9000, 500]}, 'I/S*100', '{I} ÷ {S} · 100 % = {=I/S*100} %', '%', 1, wenn='I <= S and (I/S*100) == round(I/S*100, 1)', lvl=1),
    zu('Welcher Schritt?', ['Planung', 'Umsetzung', 'Kontrolle'], [('Implementierungsziele ableiten', 0), ('Kommunikation', 1), ('Soll-Ist-Vergleich', 2), ('Maßnahmen bestimmen', 0), ('Zielerreichungsgrad', 2)], '', 2),
    mc('Viele Strategien scheitern an …', 'der Umsetzung', ['der Idee', 'der Vision', 'der Mathematik'], '', 1),
    mc('Geschäftsmodelle und Big Data sind …', 'nicht klausurrelevant', ['Pflichtstoff', 'Kern der Phase 5', 'Teil der SWOT'], '', 1),
    ns('Soll 4.000, Ist 3.200. Abweichung (Ist − Soll)?', -800, '3.200 − 4.000', 'Paar', 1),
    mc('Implementierung ist Phase …', '5', ['1', '2', '4'], '', 1),
    mc('Was folgt aus einer großen Soll-Ist-Abweichung?', 'Ursachen suchen, gegensteuern', ['nichts', 'Strategie feiern', 'Ziele verstecken'], '', 2))

# ================= k12 =================
t = 'rechtsform-kriterien'
fam(t, 'kr', 'Kennt Kriterien und Gruppen der Rechtsformen',
    zu('Personen- oder Kapitalgesellschaft?', ['Personen', 'Kapital'], [('GbR', 0), ('GmbH', 1), ('KG', 0), ('AG', 1), ('OHG', 0)], '', 1, True),
    li('Nennen Sie Kriterien der Rechtsformwahl.', [['Haftung'], ['Leitung'], ['Kontrolle'], ['Mindesteinlage', 'Mindestkapital'], ['Gewinn', 'GuV', 'Verlust'], ['Finanzierung'], ['Publizität'], ['Mitbestimmung'], ['Steuer']], '', 2, True, n=5),
    mc('Wer persönlich unbeschränkt haftet, …', 'bekommt eher Kredit', ['bekommt nie Kredit', 'zahlt keine Steuern', 'muss veröffentlichen'], '', 2, True),
    lu('Die Rechtsform regelt das [[0]]verhältnis (Gesellschafter untereinander) und das [[1]]verhältnis.', [['Innen'], ['Außen']], '', 2),
    li('Voraussetzungen einer Gründung?', [['Geschäftsidee', 'Idee'], ['Kompetenz'], ['Eigenkapital', 'Kapital']], '', 1),
    mc('Was ist die wichtigste Frage bei der Rechtsform?', 'die Haftung', ['die Farbe des Logos', 'der Standort', 'die Branche'], '', 1, True),
    mc('Gehört die KG zu den Kapitalgesellschaften?', 'nein', ['ja', 'nur mit Aktien', 'nur ohne Vertrag'], '', 2, True))

t = 'personengesellschaften'
fam(t, 'pg', 'Erkennt e.K., GbR und OHG',
    zu('Welche Rechtsform?', ['e.K.', 'GbR', 'OHG'], [('eine Person, haftet mit allem', 0), ('Band ohne Vertrag', 1), ('großes Handelsgewerbe, Nachhaftung 5 Jahre', 2), ('gemeinsamer Kauf zweier Freunde', 1)], '', 1, True),
    mc('Wie haften GbR-Gesellschafter?', 'unbeschränkt mit allem', ['nur mit Einlage', 'gar nicht', 'bis 25.000 €'], '', 1, True),
    mc('Lea hat kein Vermögen, Tom 1 Mio. €; GbR-Schulden 200.000 €. Wer zahlt zuerst?', 'Tom', ['Lea', 'niemand', 'die Bank'], 'Gläubiger holen, wo Geld ist.', 2, True),
    mc('OHG-Nachhaftung nach Austritt:', '5 Jahre', ['1 Jahr', '10 Jahre', 'keine'], '', 2, True),
    mc('Mindesteinlage beim Einzelunternehmen:', 'keine', ['25.000 €', '50.000 €', '1 €'], '', 1, True),
    blk('Richtig oder falsch?', [('Eine GbR entsteht ohne schriftlichen Vertrag.', True), ('Der e.K. haftet nur mit dem Geschäftsvermögen.', False), ('Die OHG ist die „Schwester“ der GbR.', True), ('GbR-Gesellschafter haften beschränkt.', False)], '', 2, True),
    mc('Warum gibt es die OHG-Nachhaftung?', 'sonst träten alle beim Kippen aus', ['wegen der Steuer', 'wegen der Börse', 'wegen der Publizität'], '', 3),
    mc('Ein Einzelunternehmer mit zwei Häusern bekommt …', 'eher Kredit', ['nie Kredit', 'nur Leasing', 'keine Zulassung'], '', 2))

t = 'kg'
fam(t, 'kg', 'Kennt Komplementär und Kommanditist',
    zu('Komplementär oder Kommanditist?', ['Komplementär', 'Kommanditist'], [('haftet unbeschränkt', 0), ('haftet mit Einlage', 1), ('Leitungsrecht', 0), ('kein Leitungsrecht', 1), ('Geldgeber', 1)], '', 1, True),
    mc('Hat der Kommanditist ein Kontrollrecht?', 'ja, wie vereinbart', ['nein', 'nur vor Gericht', 'nur als Vorstand'], '', 2, True),
    mc('KG-Schulden 200.000 €, KG-Vermögen 60.000 €, Kommanditistin Einlage 50.000 € (schon im KG-Vermögen). Was zahlt sie zusätzlich?', 'nichts', ['50.000 €', '140.000 €', '200.000 €'], '', 3, True),
    mc('GmbH & Co. KG: Komplementär ist …', 'eine GmbH', ['eine AG', 'ein Kommanditist', 'der Staat'], '', 3),
    mc('„Die Höhle der Löwen“ erinnert an …', 'Kommanditisten', ['Komplementäre', 'Vorstände', 'Aktionäre'], '', 2),
    kz('Wer haftet in der KG unbeschränkt?', ['Komplementär', 'der Komplementär', 'Komplementäre'], '', 1, True),
    bes('Beschrifte die KG.', [(4, 30, 170, 60, 'Komplementär'), (186, 30, 170, 60, 'Kommanditist')], ['Vorstand'], '', 2, True, deko=_txt(89, 112, 'leitet, haftet voll', 12, 600) + _txt(271, 112, 'Geld, haftet mit Einlage', 12, 600), H=124))

t = 'ag'
fam(t, 'ag', 'Kennt die AG',
    mc('Womit haftet eine Aktiengesellschaft im Insolvenzfall?', 'mit ihrem Gesellschaftsvermögen', ['mit dem Vermögen der Aktionäre', 'mit dem Vermögen des Vorstands', 'gar nicht'], '', 1, True),
    zu('Welches Organ?', ['Vorstand', 'Aufsichtsrat', 'Hauptversammlung'], [('leitet', 0), ('überwacht', 1), ('Aktionäre', 2), ('bestellt den Vorstand', 1), ('wählt den Aufsichtsrat', 2), ('erstellt Jahresabschluss', 0)], '', 1, True),
    mc('Mindestgrundkapital der AG:', '50.000 €', ['25.000 €', '1 €', '100.000 €'], '', 1, True),
    bes('Beschrifte die Organe der AG.', [(110, 4, 140, 48, 'Hauptversammlung'), (110, 86, 140, 48, 'Aufsichtsrat'), (110, 168, 140, 48, 'Vorstand')], ['Geschäftsführer'], '', 2, True,
        deko=_pfeil(180, 54, 180, 84) + _pfeil(180, 136, 180, 166) + _txt(186, 70, 'wählt', 12, 600, 'var(--dg-b)', 'start') + _txt(186, 152, 'bestellt', 12, 600, 'var(--dg-b)', 'start')),
    blk('Richtig oder falsch?', [('Aktionäre haften mit Privatvermögen.', False), ('Eine AG muss nicht an die Börse.', True), ('Eine Stimme pro Aktie.', True), ('Der Vorstand ist an Weisungen der HV gebunden.', False)], '', 2, True),
    mc('Vorzugsaktien bringen meist …', 'höhere Dividende, kein Stimmrecht', ['Stimmrecht, keine Dividende', 'Haftung', 'Vorstandsposten'], '', 3),
    mc('Publizität der AG:', 'voll', ['keine', 'gering', 'freiwillig'], '', 1, True),
    mc('Für wie lange bestellt der Aufsichtsrat den Vorstand höchstens?', '5 Jahre', ['1 Jahr', '4 Jahre', '10 Jahre'], '', 3))

t = 'gmbh'
fam(t, 'gm', 'Kennt die GmbH',
    mc('Mindeststammkapital der GmbH:', '25.000 €', ['50.000 €', '1 €', '10.000 €'], '', 1, True),
    mc('Wer leitet die GmbH?', 'Geschäftsführer', ['Vorstand', 'Aufsichtsrat', 'Komplementär'], '', 1, True),
    mc('Wie haften die Gesellschafter einer GmbH?', 'nur mit ihrer Einlage', ['mit allem', 'gar nicht', 'fünf Jahre nach'], '', 1, True),
    mc('Was haftet bei der GmbH unbeschränkt?', 'die GmbH mit ihrem Vermögen', ['der Geschäftsführer privat', 'die Gesellschafter privat', 'niemand'], '', 2, True),
    zu('GmbH oder AG?', ['GmbH', 'AG'], [('25.000 €', 0), ('50.000 €', 1), ('Geschäftsführer', 0), ('Vorstand', 1), ('volle Publizität', 1)], '', 2, True),
    mc('Warum bekommen GmbHs schwerer Kredit?', 'niemand haftet privat', ['zu viel Kapital', 'keine Publizität', 'zu viele Organe'], '', 2, True),
    mc('Die GmbH geht insolvent. Was verlieren die Gesellschafter?', 'ihre Einlage', ['ihr Privatvermögen', 'nichts', 'ihre Wohnung'], '', 2, True),
    mc('Was hebelt den Haftungsschutz der GmbH aus?', 'private Bürgschaft', ['Stammkapital', 'Gesellschafterversammlung', 'Publizität'], '', 3))

t = 'rechtsform-fall'
fam(t, 'fall', 'Erkennt Rechtsformen in Fällen',
    zu('Welche Rechtsform?', ['e.K.', 'GbR', 'KG', 'GmbH', 'AG'], [('Nagelstudio allein, haftet mit allem', 0), ('drei Freundinnen, Food-Truck ohne Vertrag', 1), ('Gründer leitet, Investorin haftet mit Einlage', 2), ('Geschäftsführer, 25.000 € Stammkapital', 3), ('Hauptversammlung wählt Aufsichtsrat', 4)], '', 2, True),
    mc('Vorstand, Aufsichtsrat, Eigentümer haften nur mit Kapital, Grundkapital 80.000 €:', 'AG', ['GmbH', 'KG', 'OHG'], '', 2, True),
    hot('Tippe auf die Rechtsform, bei der alle Gesellschafter unbeschränkt haften und kein Vertrag nötig ist.', [(4, 6, 110, 44, 'e.K.'), (124, 6, 110, 44, 'GbR'), (244, 6, 110, 44, 'KG'), (4, 60, 110, 44, 'GmbH'), (124, 60, 110, 44, 'AG'), (244, 60, 110, 44, 'OHG')], 1, '', 2, True),
    zu('Wer zahlt die Schulden?', ['privat unbeschränkt', 'nur Einlage'], [('Gesellschafter einer OHG', 0), ('Aktionär', 1), ('Komplementär', 0), ('Kommanditist', 1), ('GmbH-Gesellschafter', 1), ('Einzelunternehmer', 0)], '', 2, True),
    mc('Was passiert im Insolvenzfall einer GmbH mit den Gesellschaftern?', 'sie verlieren ihre Einlage', ['sie zahlen privat', 'nichts passiert', 'sie werden Vorstand'], '', 2, True),
    mc('Insolvenz heißt …', 'fällige Rechnungen nicht zahlbar', ['Gewinn negativ', 'Umsatz gesunken', 'Kapital zu hoch'], '', 1, True),
    rv('Ein Fall: zwei Gründer, beide haften unbeschränkt, großes Handelsgewerbe. Welche Rechtsform, und was passiert bei Austritt?', 'Es ist eine OHG. Wer austritt, haftet noch fünf Jahre für die bis dahin entstandenen Schulden.', ['OHG', 'unbeschränkte Haftung', 'Nachhaftung 5 Jahre'], 3, True),
    mc('Liquidität fehlt, aber die Firma ist rentabel. Wer haftet bei einer KG für die Schulden zuerst?', 'die KG mit ihrem Vermögen', ['der Kommanditist privat', 'der Staat', 'die Kunden'], '', 3))

# ---- Folienabgleich: ergänzte Folieninhalte
fam('stakeholder', 'fa-beitrag', 'Kennt die Beiträge der Anspruchsgruppen',
    zu('Ordnen Sie den Beitrag der Anspruchsgruppe zu.', ['Eigentümer', 'Fremdkapitalgeber', 'Arbeitnehmer', 'Kunden'], [('Kapital (Geld)', 0), ('Kredite', 1), ('Arbeit, Zeit, Wissen, Expertise', 2), ('Geld für Produkte', 3)], 'Management: Arbeit, Zeit, Verantwortung, Expertise; Lieferanten: Produkte; Staat: Straßen, Rechtssicherheit.', 2),
    mc('Was bringen Arbeitnehmer laut Anspruchsgruppen-Tabelle in das Unternehmen ein?', 'Arbeit, Zeit, Wissen und Expertise', ['Kapital und Kredite', 'Steuern und Rechtssicherheit', 'Produkte zu günstigen Preisen'], '', 1))
fam('werturteile', 'fa-frage', 'Formuliert die Werturteilsfrage',
    mc('Wie lautet die Werturteilsfrage der BWL?', 'Soll die BWL Werturteile abgeben oder wertfrei Erkenntniszuwachs erzielen?', ['Soll die BWL Gewinne oder Umsätze maximieren?', 'Soll die BWL nur Großunternehmen untersuchen?', 'Soll die BWL Märkte oder Staaten bewerten?'], '', 2),
    zu('Empirisch oder normativ?', ['empirisch', 'normativ'], [('„Steigt der Preis, sinkt die Nachfrage.“', 0), ('„Unternehmen sollen fair bezahlen.“', 1), ('„70 % der Kunden kaufen online.“', 0), ('„Die BWL soll Nachhaltigkeit fördern.“', 1)], 'Empirisch beschreibt, was ist (wertfrei); normativ sagt, was sein soll (wertgebunden).', 2),
    kz('Wie nennt man eine Wissenschaft, die beschreibt und erklärt, was ist, und wertfrei urteilt?', ['empirisch', 'empirische Wissenschaft'], 'Gegenstück: normative Wissenschaft (was sein soll).', 2))
fam('zielhierarchie', 'fa-leitbild', 'Erkennt Leitbilder bekannter Unternehmen',
    zu('Welches Unternehmen hat dieses Leitbild?', ['Google', 'McDonald’s', 'Amazon', 'Nike'], [('Don’t be evil', 0), ('To be our customers’ favorite place and way to eat', 1), ('to be earth’s most customer centric company', 2), ('If you have a body, you are an athlete', 3)], '', 1))
