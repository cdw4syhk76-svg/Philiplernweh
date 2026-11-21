"""Zusätzliche Fragen für Unterthemen der Oberthemen 1–6 (Mindestzahl, Verknüpfungen, schwere Fragen)."""
from fr_basis import *
from fr_basis import _pfeil, _txt, _kasten

fam('betriebszweck', 'verkn', 'Verbindet Betriebszweck mit anderen Themen',
    mc('Welches Prinzip passt zum Ziel „Kostenminimierung bei vorgegebener Leistung“?', 'Minimumprinzip', ['Maximumprinzip', 'Optimumprinzip', 'Hurwicz-Regel'], 'Output gegeben, Input minimieren.', 3),
    blk('Richtig oder falsch?', [('Öffentliche Unternehmen stehen kaum im Wettbewerb.', True), ('Private Haushalte decken fremden Bedarf.', False), ('Privatunternehmen wählen ihren Zweck frei.', True), ('Öffentliche Haushalte maximieren den Gewinn.', False)], '', 2, True))
fam('wirtschaften', 'mehr', 'Erkennt Verstöße gegen die Obersätze',
    zu('Welcher Obersatz wird verletzt?', ['I erfüllt, II verletzt', 'II erfüllt, III verletzt', 'III erfüllt'], [('Maschinen verkaufen für Rekordgewinn', 0), ('jahrelanger Betrug ohne Entdeckung', 1), ('Investition in energiesparende Anlage', 2)], '', 3),
    mc('„Langfristig“ im Obersatz III soll verhindern, dass …', 'Substanz verkauft wird', ['Gesetze gelten', 'Kunden zahlen', 'Steuern anfallen'], '', 2),
    li('Nennen Sie die vier Schritte vom Grundproblem zum Ergebnis.', [['Grundproblem'], ['Lösung', 'Obersätze', 'Obersatz'], ['Prinzipien', 'Rationalprinzip', 'ökonomisches Prinzip'], ['Ergebnisse', 'Kennzahlen', 'Erfolgsmaßstäbe']], '', 2))
fam('kapazitaet', 'mehr', 'Prüft Kapazitäten',
    ns('Wie viele Maschinenstunden braucht das Programm (375 S, 250 R) bei 1 h je S und 2,5 h je R?', 1000, '375 + 625', 'h', 2))
fam('effizienz', 'mehr', 'Rechnet und deutet Wertschöpfung',
    ns('Wertschöpfung 180.000 €; Löhne 120.000 €, Zinsen 10.000 €, Steuern 20.000 €. Was bleibt den Eigentümern?', 30000, '180.000 − 150.000', '€', 2),
    mc('Ist die Wertschöpfung dasselbe wie der Gewinn?', 'nein, Gewinn ist nur ein Teil', ['ja, immer', 'nein, Gewinn ist größer', 'nur bei AGs'], '', 2),
    mc('„Die richtigen Dinge tun“ heißt …', 'Effektivität', ['Effizienz', 'Produktivität', 'Liquidität'], '', 1))
fam('grenznutzen', 'mehr', 'Liest ein Grenznutzen-Diagramm',
    hotpunkt('Tippe auf den Balken mit dem höchsten Grenznutzen.', ''.join(f'<rect x="{40 + i * 44}" y="{200 - h}" width="32" height="{h}" rx="4" style="fill:var(--dg-a)"/>' for i, h in enumerate([170, 140, 108, 80, 54, 36, 22])) + _pfeil(30, 200, 350, 200),
             (56, 120, 22), 'Der erste Schluck nach dem Durst.', 1, H=220))
fam('maerkte', 'mehr', 'Erkennt Anreizwirkungen',
    mc('Wird extrinsische Belohnung eingeführt, kann die eigene Motivation …', 'verdrängt werden', ['nur steigen', 'unverändert bleiben', 'zur Pflicht werden'], 'Unbeabsichtigte Konsequenz.', 3))
fam('innovation', 'mehr', 'Verbindet Innovation mit Strategie',
    mc('Welche Rente entsteht durch Innovation?', 'Schumpeter-Rente', ['Ricardo-Rente', 'Quasi-Rente', 'Monopol-Rente'], 'Verknüpfung zur Unternehmensanalyse.', 3),
    mc('Welches Feld der Ansoff-Matrix trägt bei Innovationen das höchste Risiko?', 'Diversifikation', ['Marktdurchdringung', 'Marktentwicklung', 'Produktentwicklung'], '', 3))
fam('wirtschaftsordnung', 'mehr', 'Kennt Argumente zur Ordnung',
    mc('„Man kann Wohlstand nicht durch Teilung mehren.“ Das ist ein Argument für …', 'Wachstum statt Umverteilung', ['Planwirtschaft', 'Degrowth', 'Höchstpreise'], '', 2),
    mc('Was bedeutet „Degrowth“?', 'Verzicht auf Wachstum', ['schnelles Wachstum', 'Inflation', 'Arbeitsteilung'], '', 1))
fam('homo-oeconomicus', 'mehr', 'Grenzen des homo oeconomicus',
    mc('Im Supermarkt mit 40 Joghurtsorten nimmt man die gewohnte. Das widerspricht der Annahme …', 'alle Alternativen kennen', ['Nutzen maximieren wollen', 'Ziele haben', 'Geld besitzen'], '', 2),
    lu('Der Mensch ist laut Vorlesung [[0]] rational.', [['begrenzt', 'beschränkt']], '', 1),
    mc('Was ist ein Beispiel für begrenzte Rationalität im Alltag?', 'Kauf nach Tagesform', ['Kauf mit Preisvergleich aller Anbieter', 'perfekte Planung', 'Erwartungswert rechnen'], '', 2))
fam('stakeholder', 'mehr', 'Bewertet Stakeholder-Argumente',
    mc('Argument für den Shareholder-Ansatz:', 'niemand wird zur Mitarbeit gezwungen', ['alle haben gleiche Rechte', 'Gewinn wird verteilt', 'Kunden entscheiden'], '', 3, True),
    mc('Welcher frühe Denker passt eher zum Stakeholder-Gedanken?', 'Nicklisch', ['Rieger', 'Smith', 'Porter'], 'Gemeinnutz geht vor Eigennutz.', 3),
    kz('Wie nennt man Anspruchsgruppen auf Englisch?', ['Stakeholder', 'Stakeholders'], '', 1))
fam('shareholder-value', 'mehr', 'Rechnet Renditen',
    nu('E − A = {G} €, Kapital {K} €. Rendite r in %?', {'G': [10000, 200000, 10000], 'K': [100000, 2000000, 100000]}, 'G/K*100', '{G} ÷ {K} · 100 % = {=G/K*100} %', '%', 2, wenn='(G/K*100) == round(G/K*100, 1) and G < K', lvl=2),
    mc('r = 3,5 %, i = 5 %, aber Gewinn positiv. Was gilt?', 'Wert wird vernichtet', ['Wert entsteht', 'Break-even', 'Liquidität sinkt'], '', 3))
fam('werturteile', 'mehr', 'Bewertet Werturteile', blk('Richtig oder falsch?', [('„Steuern sind zu hoch“ ist ein primäres Werturteil.', True), ('Sekundäre Werturteile bewerten Ziele.', False), ('Praktisch-normativ heißt Mittel bewerten.', True), ('Die ökonomische BWL fällt bevorzugt primäre Urteile.', False)], '', 3, True))
fam('et-struktur', 'mehr', 'Strukturiert ein neues Problem',
    zu('Eisdiele, neue Sorte: was ist was?', ['Zielsystem', 'Alternative', 'Umwelt'], [('kreatives Image', 0), ('Pistazie-Salz', 1), ('Wetter im Sommer', 2), ('Mango-Chili', 1), ('Pistazienpreis', 2)], '', 2))
fam('zielbeziehungen', 'mehr', 'Verknüpft Ziele und Strategien',
    mc('Welche Wettbewerbsstrategie löst die Zielkonkurrenz „Qualität vs. Kosten“ zugunsten der Kosten?', 'Kostenführerschaft', ['Differenzierung', 'Nische', 'Diversifikation'], '', 3))

# Erklärfragen (selbst bewerten) für Oberthema 3, auch für „Selbst schreiben“ im Drill
fam('elastizitaet', 'erkl', 'Erklärt Elastizität in eigenen Worten',
    rv('Erklären Sie, was eine Preiselastizität von 0,6 bedeutet.', 'Steigt der Preis um 1 %, sinkt die Nachfrage um 0,6 %. Die Nachfrage ist unelastisch: Die Menge reagiert schwächer als der Preis.', ['Preis +1 % → Nachfrage −0,6 %', 'unelastisch', 'Menge reagiert schwächer als Preis'], 2, True))
fam('mittelwert', 'erkl', 'Erklärt die Mittelwertmethode',
    rv('Warum verwendet man bei der Bogenelastizität die Mittelwerte?', 'Weil die einfache Prozentrechnung vom alten Wert je nach Richtung (Preissenkung oder -erhöhung) ein anderes Ergebnis liefert. Mit den Mittelwerten als Bezug ist das Ergebnis in beide Richtungen gleich.', ['einfache Prozente hängen von der Richtung ab', 'Mittelwert als Bezug', 'gleiches Ergebnis in beide Richtungen'], 3))
fam('punktelastizitaet', 'erkl', 'Erklärt die Punktelastizität',
    rv('Erklären Sie, warum die Elastizität auf einer geraden Nachfragekurve nicht überall gleich ist.', 'Die Steigung ist zwar überall gleich, aber das Verhältnis Preis durch Menge ändert sich. Oben links (hoher Preis, kleine Menge) ist die Nachfrage elastisch, unten rechts unelastisch, in der Mitte genau einheitselastisch.', ['Steigung gleich', 'p/Q ändert sich', 'oben elastisch, unten unelastisch'], 3))
fam('effekte', 'erkl', 'Erklärt den Gesamteffekt',
    rv('Erläutern Sie mit Mengen- und Preiseffekt, wie sich der Erlös bei einer Preissenkung und elastischer Nachfrage entwickelt.', 'Durch die Preissenkung verliert man an der alten Menge (negativer Preiseffekt). Dafür wird viel mehr verkauft (positiver Mengeneffekt). Bei elastischer Nachfrage überwiegt der Mengeneffekt, der Gesamteffekt und damit der Erlös steigt.', ['Preiseffekt negativ', 'Mengeneffekt positiv', 'elastisch: Mengeneffekt überwiegt', 'Erlös steigt'], 3, True))

# Auffüllen nach Entfernen des Durchgestrichenen
fam('et-struktur', 'mehr2', 'Ordnet Bausteine der Entscheidungstheorie',
    mm('Welche Bausteine gehören zum Entscheidungsfeld?', [('Handlungsalternativen', True), ('Umwelteinflüsse', True), ('Zielsystem', False), ('Rechtsform', False)], 'Das Zielsystem steht neben dem Entscheidungsfeld.', 2))
fam('garbage-can', 'mehr', 'Kennt die Ströme im Mülleimer-Modell',
    li('Nennen Sie die vier Ströme, die im Garbage-Can-Modell zusammentreffen.', [['Probleme', 'Problem'], ['Lösungen', 'Lösung'], ['Teilnehmer'], ['Entscheidungsgelegenheiten', 'Entscheidungsgelegenheit', 'Gelegenheiten']], '', 2))
fam('rechtsform-kriterien', 'mehr', 'Ordnet Kriterien zu',
    zu('Innen- oder Außenverhältnis?', ['Innenverhältnis', 'Außenverhältnis'], [('Leitungsbefugnis', 0), ('Haftung gegenüber Gläubigern', 1), ('Gewinnverteilung', 0), ('Publizitätspflicht', 1)], '', 2))
fam('kg', 'mehr', 'Unterscheidet Komplementär und Kommanditist',
    zu('Wer ist das?', ['Komplementär', 'Kommanditist'], [('haftet unbeschränkt', 0), ('haftet nur mit der Einlage', 1), ('führt die Geschäfte', 0), ('gibt Kapital, leitet aber nicht', 1)], '', 2, True))
