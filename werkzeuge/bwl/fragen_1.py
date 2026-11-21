"""ABWL-Fragen, Oberthemen 1–6. Auswahlantworten kurz und gleichartig; viele Schaubild-, Zuordnungs- und Verknüpfungsfragen."""
from fr_basis import *
from fr_basis import _pfeil, _txt, _kasten

# ================= k1 =================
t = 'bwl-def'
fam(t, 'grund', 'Weiß, womit sich die BWL beschäftigt',
    mc('Mit welchem Grundproblem beschäftigt sich die BWL?', 'unendliche Bedürfnisse, knappe Mittel', ['zu viele Betriebe, zu wenige Kunden', 'zu hohe Steuern, zu wenig Staat', 'schwankende Preise, feste Löhne'], 'Ziele und knappe Mittel in Einklang bringen.', 1),
    mc('Welche Definition hält die Vorlesung für die beste?', 'Zusammenarbeit zum gegenseitigen Vorteil', ['das, was Betriebswirte tun', 'Wissenschaft von Betrieben und Wirtschaft', 'Lehre von der Buchführung'], '', 2),
    kz('Beim freiwilligen Kauf: Wer hat danach einen Vorteil?', ['beide', 'beide Seiten', 'Käufer und Verkäufer'], 'Sonst käme der Tausch nicht zustande.', 1),
    blk('Richtig oder falsch?', [('Die BWL untersucht, wie man Ziele mit knappen Mitteln erreicht.', True), ('„BWL ist, was Betriebswirte tun“ ist inhaltlich genau.', False), ('Beim freiwilligen Tausch verliert immer eine Seite.', False), ('Ein Architekt arbeitet für Betriebe, ist aber kein Betriebswirt.', True)], '', 2))
fam(t, 'teile', 'Ordnet die drei Teile des Begriffs zu',
    bes('Beschrifte die drei Teile des Begriffs Betriebswirtschaftslehre (wo – wie – wozu).', [(4, 10, 112, 70, 'Betrieb'), (124, 10, 112, 70, 'Wirtschaften'), (244, 10, 112, 70, 'Lehre'), (4, 100, 352, 50, '=Grundproblem: unendliche Bedürfnisse, knappe Mittel')], ['Markt'], '', 1),
    zu('Welcher Teil ist gemeint?', ['Betrieb', 'Wirtschaften', 'Lehre'], [('kombiniert Produktionsfaktoren', 0), ('langfristige Gewinnmaximierung', 1), ('Erkenntnisse nutzbar machen', 2), ('folgt dem ökonomischen Prinzip', 1)], '', 1),
    li('Nennen Sie die 4 P des Marketings.', [['Product', 'Produkt'], ['Price', 'Preis'], ['Place', 'Vertrieb', 'Distribution'], ['Promotion', 'Kommunikation', 'Werbung']], '', 2))
fam(t, 'verkn', 'Verbindet die Definition mit späteren Themen',
    mc('Welches spätere Thema greift die Idee „knappe Mittel“ direkt auf?', 'Opportunitätskosten', ['Rechtsformen', 'Uno-actu-Prinzip', 'Five Forces'], 'Wer knappe Mittel einsetzt, verzichtet auf Alternativen.', 3),
    rv('Warum passt die Definition „Zusammenarbeit zum gegenseitigen Vorteil“ zum Stakeholder-Ansatz?', 'Beide betonen, dass mehrere Seiten vom Wirtschaften profitieren sollen: beim Tausch Käufer und Verkäufer, im Stakeholder-Ansatz alle Anspruchsgruppen.', ['mehrere Seiten profitieren', 'Tausch nützt beiden', 'Stakeholder: alle Anspruchsgruppen beteiligen'], 3))

t = 'betrieb'
fam(t, 'faktoren', 'Ordnet Produktionsfaktoren zu',
    zu('Arbeit, Betriebsmittel oder Werkstoff?', ['Arbeit', 'Betriebsmittel', 'Werkstoff'], [('Mechanikerin', 0), ('Montageständer', 1), ('verbaute Schläuche', 2), ('Werkstattgebäude', 1), ('Kettenöl', 2), ('Bürostuhl', 1)], 'Betriebsmittel werden genutzt, Werkstoffe verbraucht.', 1),
    zu('Rohstoff, Hilfsstoff oder Betriebsstoff?', ['Rohstoff', 'Hilfsstoff', 'Betriebsstoff'], [('Holz beim Tischler', 0), ('Leim beim Tischler', 1), ('Strom für die Säge', 2), ('Stahl im Fahrrad', 0), ('Schrauben am Fahrrad', 1), ('Schmierfett', 2)], '', 2),
    mc('Diesel für den Gabelstapler ist ein …', 'Betriebsstoff', ['Hilfsstoff', 'Rohstoff', 'Betriebsmittel'], '', 2),
    mc('Der Gabelstapler selbst ist ein …', 'Betriebsmittel', ['Betriebsstoff', 'Werkstoff', 'Hilfsstoff'], '', 1))
fam(t, 'umfeld', 'Kennt das Umfeld des Betriebs',
    bes('Beschrifte die Märkte rund um den Betrieb.', [(130, 70, 100, 50, '=Betrieb'), (4, 70, 110, 50, 'Beschaffungsmarkt'), (246, 70, 110, 50, 'Absatzmarkt'), (4, 150, 110, 50, 'Kapitalmarkt'), (246, 150, 110, 50, 'Arbeitsmarkt'), (125, 6, 110, 46, 'Staat')],
        ['Wertschöpfung'], 'Einkauf links, Verkauf rechts, Geld und Personal unten, Staat oben.', 2, deko=_pfeil(114, 95, 128, 95) + _pfeil(232, 95, 244, 95) + _pfeil(60, 148, 140, 122) + _pfeil(300, 148, 220, 122) + _pfeil(180, 54, 180, 68)),
    zu('Was bekommt der Betrieb auf diesem Markt?', ['Material', 'Umsatz', 'Kredit', 'Arbeitskraft'], [('Beschaffungsmarkt', 0), ('Absatzmarkt', 1), ('Kapitalmarkt', 2), ('Arbeitsmarkt', 3)], '', 1),
    mc('Mandelmilch für einen Milchbauern ist …', 'ein Substitut', ['ein Betriebsstoff', 'ein Absatzmarkt', 'eine Abgabe'], '', 1),
    mc('Was unterscheidet Abgaben von Steuern?', 'Abgaben sind zweckgebunden', ['Steuern sind zweckgebunden', 'Abgaben zahlen nur Firmen', 'Steuern gibt es nur auf Gewinn'], '', 2),
    lu('Ein Betrieb ist eine [[0]] organisierte Wirtschaftseinheit, in der [[1]] kombiniert werden, um Güter und Dienstleistungen herzustellen oder [[2]].', [['planvoll', 'planmäßig'], ['Produktionsfaktoren'], ['abzusetzen', 'zu verkaufen']], '', 2))

t = 'leistungsart'
fam(t, 'arten', 'Ordnet Betriebe nach der Art der Leistung',
    zu('Sachleistung oder Dienstleistung?', ['Sachleistung', 'Dienstleistung'], [('Kieswerk', 0), ('Allianz', 1), ('Maschinenbauer', 0), ('Rewe', 1), ('Sparkasse', 1), ('Brauerei', 0)], '', 1),
    zu('Welcher Sektor?', ['primär', 'sekundär', 'tertiär'], [('Erzbergwerk', 0), ('Autohersteller', 1), ('Versicherung', 2), ('Landwirtschaft', 0), ('Supermarkt', 2)], '', 2),
    bes('Beschrifte den Baum der Betriebsarten.', [(4, 90, 80, 44, '=Betrieb'), (110, 40, 110, 44, 'Sachleistung'), (110, 140, 110, 44, 'Dienstleistung'), (246, 6, 110, 36, 'Rohstoffgewinnung'), (246, 48, 110, 36, 'Konsumgüter'), (246, 150, 110, 36, 'Handel')],
        ['Arbitrage'], '', 2, deko=_pfeil(84, 104, 108, 66) + _pfeil(84, 120, 108, 160) + _pfeil(220, 56, 244, 26) + _pfeil(220, 66, 244, 66) + _pfeil(220, 162, 244, 168)))
fam(t, 'gueter', 'Klassifiziert Wirtschaftsgüter',
    mc('Aktien, Fonds und Geld sind …', 'Nominalgüter', ['Realgüter', 'Verbrauchsgüter', 'Konsumgüter'], '', 1),
    zu('Verbrauchs- oder Gebrauchsgut?', ['Verbrauchsgut', 'Gebrauchsgut'], [('Kettenöl', 0), ('Fahrrad', 1), ('Druckerpapier', 0), ('Laptop', 1)], '', 1),
    mc('Ein Lieferwagen für einen Kurierdienst ist ein …', 'Investitionsgut', ['Konsumgut', 'Nominalgut', 'Verbrauchsgut'], '', 2),
    mc('Dasselbe Fahrrad gekauft von einer Studentin für die Freizeit ist ein …', 'Konsumgut', ['Investitionsgut', 'Nominalgut', 'Inputgut'], 'Die Verwendung entscheidet.', 3),
    mc('Der quartäre Sektor ist …', 'umstritten: reine Informationsdienste', ['die Landwirtschaft', 'die Industrie', 'der öffentliche Dienst'], '', 3))

t = 'dienstleistung'
fam(t, 'unoactu', 'Erklärt das Uno-actu-Prinzip',
    mc('Was versteht man unter dem Uno-actu-Prinzip?', 'Leistung und Konsum fallen zeitlich zusammen', ['Leistung entsteht in einem Arbeitsschritt', 'Jeder Kunde kauft genau eine Einheit', 'Leistungen werden auf Vorrat erbracht'], 'Beispiel Friseur.', 1, True),
    mc('Welches Beispiel passt zum Uno-actu-Prinzip?', 'ein Haarschnitt beim Friseur', ['Brötchen für den nächsten Tag', 'Autos für das Lager', 'Bücher für den Buchhandel'], '', 1, True),
    blk('Richtig oder falsch zum Uno-actu-Prinzip?', [('Man kann nicht auf Vorrat produzieren.', True), ('Der Kunde ist an der Leistung beteiligt.', True), ('Erst wird produziert, dann konsumiert.', False), ('Uno actu heißt „besonders schnell“.', False)], '', 2, True),
    hot('Tippe auf den Kasten, der das Uno-actu-Prinzip zeigt.', [(4, 10, 110, 60, 'herstellen'), (124, 10, 110, 60, 'lagern'), (244, 10, 110, 60, 'nutzen'), (4, 100, 350, 60, 'herstellen = nutzen')], 3, '', 2))
fam(t, 'merkmale', 'Kennt die Merkmale einer Dienstleistung',
    li('Nennen Sie vier Merkmale einer Dienstleistung.', [['immateriell', 'nicht anfassbar'], ['uno actu', 'gleichzeitig'], ['nicht lagerfähig', 'nicht lagerbar', 'nicht transportfähig'], ['Qualität schwankt', 'schwankende Qualität'], ['Kunde beteiligt', 'externer Faktor', 'Kunde wirkt mit']], '', 2, n=4),
    mc('Welches Merkmal gilt als das schwächste?', 'schwankende Qualität', ['Immaterialität', 'Uno-actu-Prinzip', 'fehlende Lagerfähigkeit'], 'Auch Sachgüter schwanken.', 3),
    zu('Welcher Definitionsversuch?', ['negativ', 'enumerativ', 'Merkmale'], [('„alles, was keine Sachleistung ist“', 0), ('Liste: Handel, Banken …', 1), ('immateriell, uno actu …', 2)], '', 2),
    mc('Warum arbeiten Friseure mit Terminen? Welches Merkmal steckt dahinter?', 'nicht lagerfähig', ['immateriell', 'schwankende Qualität', 'Nominalgut'], 'Ein leerer Stuhl um 10 Uhr ist für immer verloren.', 3))

t = 'betriebszweck'
fam(t, 'zweck', 'Ordnet Betriebe nach ihrem Zweck',
    zu('Welches Ziel?', ['Gewinnmax.', 'Kostenmin.', 'Nutzenmax.', 'Wohlfahrtsmax.'], [('Pharmaunternehmen', 0), ('Bürgeramt', 1), ('Familie', 2), ('Stadt beim Kulturangebot', 3), ('Stadtbücherei', 1)], '', 1, True),
    bes('Beschrifte die vier Wirtschaftseinheiten (links fremder, rechts eigener Bedarf).', [(4, 30, 84, 60, 'Privatunternehmen'), (92, 30, 84, 60, 'öffentl. Unternehmen'), (184, 30, 84, 60, 'privater Haushalt'), (272, 30, 84, 60, 'öffentl. Haushalt')], ['Bank'], '', 2,
        deko=_txt(90, 14, 'fremder Bedarf', 12, 700) + _txt(270, 14, 'eigener Bedarf', 12, 700) + _txt(46, 108, 'Gewinn', 12, 600) + _txt(134, 108, 'Kosten', 12, 600) + _txt(226, 108, 'Nutzen', 12, 600) + _txt(314, 108, 'Wohlfahrt', 12, 600)),
    mc('Wie finanziert sich ein öffentliches Unternehmen?', 'Steuern und Gebühren', ['Eigen- und Fremdkapital', 'nur Spenden', 'nur Kredite'], '', 2, True),
    mc('Wer trägt bei einem öffentlichen Unternehmen das Risiko?', 'keiner', ['der Eigentümer', 'die Kunden', 'die Bank'], '', 2, True))
fam(t, 'groesse', 'Kennt Kriterien der Unternehmensgröße',
    zu('Welche Gruppe?', ['finanziell', 'arbeitsrelevant', 'branchenspezifisch'], [('Bilanzsumme', 0), ('Mitarbeiteranzahl', 1), ('Verkaufsfläche', 2), ('Umsatz', 0), ('Hektoliter Ausstoß', 2)], '', 2),
    mc('Warum reicht eine Kennzahl zur Größe nicht?', 'Sie kann stark verzerren', ['Sie ist gesetzlich verboten', 'Nur Umsatz zählt', 'Banken verbieten es'], 'Google: wenige Mitarbeiter, hoher Gewinn.', 2))

# ================= k2 =================
t = 'wirtschaften'
fam(t, 'obersatz', 'Unterscheidet die drei Obersätze',
    zu('Welcher Obersatz?', ['I', 'II', 'III'], [('höchster Gewinn', 0), ('langfristig höchster Gewinn', 1), ('langfristig, unter Nebenbedingungen', 2)], '', 1),
    rh('Ordne die vier Schritte vom Problem zum Ergebnis.', ['Grundproblem', 'Lösung (Obersätze)', 'Prinzipien', 'Ergebnisse messen'], '', 1),
    mc('Welches Problem hat Obersatz I?', 'Ausverkauf', ['Betrug', 'Bürokratie', 'Inflation'], 'Kurzfristig bringt Verkaufen am meisten.', 2),
    mc('Ein Hersteller manipuliert jahrelang Abgaswerte. Welcher Obersatz verbietet das erst?', 'Obersatz III', ['Obersatz I', 'Obersatz II', 'keiner'], '', 2),
    lu('Wirtschaften bedeutet eine [[0]] Maximierung des Gewinns unter Beachtung von [[1]].', [['langfristige'], ['Nebenbedingungen']], '', 2))

t = 'oekprinzip'
fam(t, 'maxmin', 'Unterscheidet Maximum-, Minimum- und Optimumprinzip',
    zu('Maximum- oder Minimumprinzip?', ['Maximum', 'Minimum'], [('10 l Kraftstoff, möglichst weit', 0), ('100 km, möglichst wenig Kraftstoff', 1), ('10 kWh, möglichst warm', 0), ('20 Grad, möglichst wenig Energie', 1), ('5 t Kartoffeln, wenig Dünger', 1), ('8 Stunden, möglichst viele Reparaturen', 0)], '', 1),
    mc('Beim Maximumprinzip ist gegeben …', 'der Input', ['der Output', 'beides', 'nichts'], '', 1),
    mc('Beim Optimumprinzip ist gegeben …', 'nichts', ['der Input', 'der Output', 'beides'], 'Gesucht ist das beste Verhältnis.', 2),
    mc('„Mit möglichst wenig Input möglichst viel Output“ ist …', 'kein ökonomisches Prinzip', ['das Maximumprinzip', 'das Minimumprinzip', 'das Optimumprinzip'], '', 2),
    mc('Wann handelt man nach dem Rationalprinzip?', 'wenn man die bessere Alternative wählt', ['wenn man die billigste nimmt', 'wenn man würfelt', 'wenn man nichts tut'], '', 1))
fam(t, 'ertrag', 'Rechnet Ertrag und Aufwand',
    lu('Output · [[0]] = Ertrag; Input · [[1]] = Aufwand', [['Güterpreis', 'Preis', 'Verkaufspreis'], ['Faktorpreis', 'Einkaufspreis']], '', 2),
    nu('Lena verkauft {M} Packungen zu je {P} €. Ertrag?', {'M': [20, 200, 10], 'P': [6, 15, 1]}, 'M*P', 'Ertrag = {M} · {P} = {=M*P} €', '€', 0, lvl=1),
    nu('Aus 1 kg Rohkaffee werden 4 Packungen. Wie viele kg braucht man mindestens für {N} Packungen?', {'N': [40, 400, 20]}, 'N/4', '{N} ÷ 4 = {=N/4} kg (Minimumprinzip)', 'kg', 1, lvl=2))

t = 'kennzahlen'
fam(t, 'wirtsch', 'Rechnet und deutet die Wirtschaftlichkeit',
    nu('Ertrag {E} €, Aufwand {A} €. Wirtschaftlichkeit?', {'E': [40000, 200000, 4000], 'A': [20000, 160000, 4000]}, 'E/A', 'W = {E} ÷ {A} = {=E/A}', '', 2, wenn='E/A == round(E/A, 2) and E != A', tipp='Ertrag ÷ Aufwand', lvl=2, kl=True),
    mc('Vorjahr: E 240.000 €, A 200.000 €. Jetzt: E 330.000 €, A 300.000 €. Ist die Wirtschaftlichkeit gestiegen?', 'nein, 1,2 → 1,1', ['ja, 1,1 → 1,2', 'ja, Ertrag +90.000 €', 'gleich, 1,15'], '', 2, True),
    mc('Ab welchem Wert ist ein Betrieb unwirtschaftlich?', 'unter 1', ['unter 0', 'unter 100', 'über 1'], '', 1, True),
    nu('Ertrag {E} €, Aufwand {A} €. Gewinn?', {'E': [10000, 90000, 1500], 'A': [5000, 60000, 1500]}, 'E-A', 'G = {E} − {A} = {=E-A} €', '€', 0, wenn='E > A', lvl=1))
fam(t, 'prod', 'Rechnet Produktivität und unterscheidet Kennzahlen',
    nu('In {H} Stunden werden {S} Teile gefertigt. Produktivität (Teile je Stunde)?', {'H': [2, 10, 1], 'S': [10, 120, 2]}, 'S/H', '{S} ÷ {H} = {=S/H}', 'Teile/h', 2, wenn='S/H == round(S/H, 1)', lvl=1),
    zu('Welche Kennzahl?', ['Gewinn', 'Wirtschaftlichkeit', 'Produktivität'], [('E − A', 0), ('E ÷ A', 1), ('Output ÷ Input in Mengen', 2), ('absoluter Euro-Betrag', 0), ('0,5 Verträge je Stunde', 2)], '', 1),
    mc('Gewinn steigt, Wirtschaftlichkeit sinkt. Wie ist das möglich?', 'Aufwand wächst stärker als Ertrag', ['Ertrag sinkt stärker als Aufwand', 'gar nicht möglich', 'nur bei Verlust'], '', 3),
    blk('Richtig oder falsch?', [('Mindestbedingung: Ertrag ≥ Aufwand.', True), ('Produktivität wird in Euro gemessen.', False), ('Wirtschaftlichkeit 0,9 bedeutet Verlust.', True), ('Gewinn ist eine Verhältniszahl.', False)], '', 2))

t = 'breakeven'
fam(t, 'rechnen', 'Berechnet den Break-even-Punkt',
    nu('Preis {P} €, variable Kosten {V} €/Stück, Fixkosten {F} €. Break-even-Menge?', {'P': [20, 80, 5], 'V': [5, 40, 5], 'F': [3000, 60000, 1500]}, 'F/(P-V)', 'x = {F} ÷ ({P} − {V}) = {=F/(P-V)}', 'Stück', 0, wenn='P > V and F % (P-V) == 0', tipp='G(x) = 0 setzen', lvl=2, kl=True),
    nu('E(x) = {P}x, K(x) = {V}x + {F}. Gewinnschwelle?', {'P': [15, 60, 1], 'V': [5, 30, 1], 'F': [1000, 9000, 100]}, 'F/(P-V)', '{=P-V}x = {F} → x = {=F/(P-V)}', 'Stück', 0, wenn='P > V and F % (P-V) == 0', lvl=2, kl=True),
    ns('Preis 40 €, variable Kosten 10 €, Fixkosten 21.000 €. Ertrag an der Gewinnschwelle?', 28000, '700 Stück · 40 € = 28.000 €', '€', 2),
    nu('Break-even liegt bei {X} Stück, Preis {P} €, variable Kosten {V} €. Wie hoch sind die Fixkosten?', {'X': [100, 2000, 100], 'P': [20, 60, 5], 'V': [5, 15, 5]}, 'X*(P-V)', 'K_f = {X} · ({P} − {V}) = {=X*(P-V)} €', '€', 0, wenn='P > V', lvl=3))
fam(t, 'deuten', 'Deutet Break-even-Diagramme',
    hotpunkt('Tippe auf den Break-even-Punkt.', achse(40, 220, 350, 10, 'Menge', '€') + linie([(40, 220), (340, 30)]) + linie([(40, 150), (340, 90)], 'var(--dg-b)') + _txt(330, 46, 'E', 13, 800) + _txt(330, 106, 'K', 13, 800),
             (40 + 300 * (70 / 130), 220 - 190 * (70 / 130) * 1.0, 16), 'Dort schneiden sich Ertrags- und Kostengerade.', 1),
    mc('Was passiert mit der Break-even-Menge, wenn die Fixkosten steigen?', 'sie steigt', ['sie sinkt', 'gleich', 'wird null'], '', 1),
    mc('Was passiert, wenn der Verkaufspreis steigt?', 'sie sinkt', ['sie steigt', 'gleich', 'wird negativ'], 'Mehr Deckung je Stück.', 2),
    mc('G(x) = −½x² + 4x − 6. Wo ist der Gewinn null?', 'x = 2 und x = 6', ['x = 4 und x = 8', 'nur x = 4', 'x = 0 und x = 6'], '', 3, True),
    mc('Am Break-even-Punkt gilt …', 'Gewinn = 0', ['Gewinn maximal', "G'(x) = 0", 'Umsatz maximal'], '', 1))

t = 'rentabilitaet'
fam(t, 'rechnen', 'Rechnet Rentabilitäten im Kopf, auch rückwärts',
    nu('Es werden {K} € eingesetzt, die Rentabilität soll {R} % sein. Nötiger Gewinn?', {'K': [10000, 60000, 2500], 'R': [4, 20, 1]}, 'K*R/100', '{R} % von {K} = {=K*R/100} €', '€', 2, tipp='Gewinn = R · Kapital', lvl=2, kl=True),
    nu('EK-Rendite {R} %, Gewinn {=EK*R/100} €. Eingesetztes Eigenkapital?', {'EK': [50000, 400000, 10000], 'R': [5, 25, 5]}, 'EK', '{=EK*R/100} ÷ {=R/100} = {EK} €', '€', 0, tipp='Kapital = Gewinn ÷ R (Dezimalzahl)', lvl=2, kl=True),
    nu('{EK} € Eigenkapital, {G} € Gewinn. EK-Rentabilität?', {'EK': [200, 2000, 100], 'G': [100, 3000, 100]}, 'G/EK*100', '{G} ÷ {EK} · 100 % = {=G/EK*100} %', '%', 2, wenn='(G/EK*100) == round(G/EK*100, 1)', lvl=2, kl=True),
    ns('Eine Influencerin hat 15 % EK-Rendite bei 22.500 € Gewinn. Wie viel Eigenkapital?', 150000, '22.500 ÷ 0,15', '€', 2, True))
fam(t, 'arten', 'Unterscheidet Rentabilitätsarten und deutet sie',
    zu('Was steht im Nenner?', ['eingesetztes Kapital', 'Eigenkapital', 'Umsatz'], [('Kapitalrentabilität', 0), ('EK-Rendite', 1), ('Umsatzrentabilität', 2)], '', 1, True),
    ns('Aufwand 100, Ertrag 110. Umsatzrentabilität in % (zwei Stellen)?', 9.09, '10 ÷ 110', '%', 2, True),
    mc('Gewinn 500.000 → 750.000 €, Umsatz 1 → 3 Mio. €. Die Umsatzrentabilität …', 'sinkt von 50 % auf 25 %', ['steigt von 50 % auf 75 %', 'bleibt bei 50 %', 'steigt von 25 % auf 50 %'], '', 2, True),
    blk('Richtig oder falsch?', [('Gewinn ist absolut, Rentabilität relativ.', True), ('Mehr Gewinn heißt immer mehr Rentabilität.', False), ('Rentabilität über 100 % ist möglich.', True), ('Rentabilität = Basisgröße ÷ Erfolgsgröße.', False)], '', 2, True),
    mc('Welche Rentabilität passt zum Shareholder Value (Vergleich mit dem Zins)?', 'Kapitalrendite r', ['Umsatzrentabilität', 'Wirtschaftlichkeit', 'Produktivität'], 'r ≥ i.', 3))

t = 'gewinnmax'
fam(t, 'max', 'Bestimmt das Gewinnmaximum',
    nu('G(x) = −{A}x² + {=2*A*X}x − {C}. Gewinnmaximale Menge?', {'A': [1, 5, 1], 'X': [5, 40, 5], 'C': [100, 2000, 100]}, 'X', "G'(x) = −{=2*A}x + {=2*A*X} = 0 → x = {X}", 'Stück', 0, tipp="G'(x) = 0", lvl=2, kl=True),
    nu('G(x) = −{A}x² + {=2*A*X}x − {C}. Maximaler Gewinn?', {'A': [1, 4, 1], 'X': [5, 30, 5], 'C': [50, 1000, 50]}, 'A*X*X-C', 'G({X}) = {=A*X*X-C}', '€', 0, lvl=3, kl=True),
    ns('p(x) = 6 − x/2, Kosten 2x + 6. Gewinnmaximale Menge?', 4, "G = −½x² + 4x − 6; G' = −x + 4", 'Stück', 2, True),
    ns('Im selben Beispiel: Umsatz beim höchsten Gewinn?', 16, 'E(4) = 4 · 4', '€', 2, True),
    ns('K(x) = 50x − 4,5x² + 5.000, E(x) = 550x − 14,5x². Maximaler Gewinn?', 1250, 'G = −10x² + 500x − 5.000; x = 25', '€', 3, True))
fam(t, 'begriff', 'Versteht Preis-Absatz-Funktion und Ableitung',
    mc('Was beschreibt p(x) = 6 − x/2?', 'Preis bei Absatz x', ['Kosten bei x Stück', 'Gewinn je Stück', 'Menge bei 6 €'], '', 1),
    mc('E(x) aus der Preis-Absatz-Funktion:', 'p(x) · x', ['p(x) + x', 'p(x) ÷ x', 'p(x) − K(x)'], '', 1),
    hotpunkt('Tippe auf das Gewinnmaximum.', achse(40, 200, 350, 10, 'x', 'G') + linie([(60 + i * 14, 200 - (-(i - 10) ** 2 + 100) * 1.6) for i in range(0, 21)]),
             (60 + 10 * 14, 200 - 160, 16), '', 1),
    mc("G'(x) = 0 und G''(x) < 0 bedeutet …", 'Hochpunkt', ['Tiefpunkt', 'Nullstelle', 'Wendepunkt'], '', 2),
    mc('Welches Prinzip steckt in „produzieren, solange G′(x) > 0“?', 'Denken in Grenzbegriffen', ['Uno-actu-Prinzip', 'Laplace-Kriterium', 'Lexikographie'], 'Grenzgewinn = Gewinn der nächsten Einheit.', 3))

t = 'rentmax'
fam(t, 'rmax', 'Bestimmt das Rentabilitätsmaximum',
    mc('G(x) = −20x² + 40x − 80, Kap(x) = 2x. R(x) = …', '−10x + 20 − 40/x', ['−40x + 40', '−10x² + 20x − 40', '−20x + 40 − 80/x'], '', 3, True),
    ns('Wo ist R(x) = −10x + 20 − 40/x maximal?', 2, "R'(x) = −10 + 40/x² = 0", 'Stück', 3, True),
    mc('Wann liegen Gewinn- und Rentabilitätsmaximum gleich?', 'bei konstantem Kapital', ['bei negativem Gewinn', 'immer', 'bei Fixkosten 0'], '', 2),
    mc('G(x) = −20x² + 40x − 80: das „Gewinnmaximum“ ist …', '−60, unrentabel', ['+60, rentabel', '0, Gewinnschwelle', '−240'], '', 2, True),
    mc('Ableitung von −40/x:', '40/x²', ['−40/x²', '40x', '−40'], '', 2),
    kz('Wie heißt die Funktion G(x) ÷ Kap(x)?', ['Rentabilitätsfunktion', 'Rentabilität', 'R(x)'], '', 1),
    mc('Rentabilität −20 als Prozent:', '−2.000 %', ['−20 %', '−0,2 %', '−200 %'], '', 2),
    mc('Warum ist x = −2 keine Lösung?', 'Mengen sind nicht negativ', ['x² ist negativ', 'R ist dort null', 'Division durch null'], '', 1))

t = 'kapazitaet'
fam(t, 'lp', 'Löst ein Produktionsprogramm mit Kapazitätsgrenzen',
    ns('x + 0,5y ≤ 500 und x + 2,5y ≤ 1.000. y im Schnittpunkt?', 250, '2y = 500', 'Stück', 2),
    ns('x im selben Schnittpunkt?', 375, '500 − 125', 'Stück', 2),
    ns('Gewinn 300 € je S, 200 € je R. Gewinn bei (375 | 250)?', 162500, '112.500 + 50.000', '€', 2),
    rh('Ordne das Vorgehen.', ['Ungleichungen aufschreiben', 'Grenzgeraden zeichnen', 'Schnittpunkt berechnen', 'Ecken vergleichen'], '', 1),
    mc('„1 h Facharbeit je S, 0,5 h je R, 500 h verfügbar“ formal:', 'x + 0,5y ≤ 500', ['x + 0,5y ≥ 500', '0,5x + y ≤ 500', 'x + y ≤ 500'], '', 2),
    hotpunkt('Tippe auf den Punkt mit dem höchsten Gewinn.', achse(40, 230, 350, 10, 'S', 'R') + f'<polygon points="40,230 250,230 197,125 40,62" style="fill:var(--dg-soft)"/>' + linie([(145, 20), (250, 230)]) + linie([(40, 62), (334, 180)], 'var(--dg-b)'),
             (197, 125, 16), 'Schnittpunkt der beiden Kapazitätsgeraden.', 2),
    mc('Warum liegt das Optimum an einer Ecke?', 'die Gewinngerade berührt die Fläche zuletzt dort', ['dort ist der Aufwand null', 'Ecken sind immer billig', 'nur dort gilt x = y'], '', 3))

t = 'liquiditaet'
fam(t, 'ekq', 'Berechnet Eigenkapitalquote und Eigenkapital',
    nu('EK {E} €, FK {F} €. Eigenkapitalquote?', {'E': [100000, 900000, 50000], 'F': [100000, 900000, 50000]}, 'E/(E+F)*100', '{E} ÷ {=E+F} · 100 % = {=E/(E+F)*100} %', '%', 2, wenn='(E/(E+F)*100) == round(E/(E+F)*100, 1)', tipp='EK ÷ Gesamtkapital', lvl=2, kl=True),
    nu('EK-Quote {Q} %, Bilanzsumme {B} €. Eigenkapital?', {'Q': [10, 60, 5], 'B': [200000, 2000000, 100000]}, 'Q*B/100', '{Q} % · {B} = {=Q*B/100} €', '€', 0, lvl=2, kl=True),
    mc('Typischer Fehler bei der EK-Quote:', 'durch das Fremdkapital teilen', ['durch die Bilanzsumme teilen', 'mal 100 nehmen', 'EK oben einsetzen'], '', 2, True))
fam(t, 'liq', 'Unterscheidet die Liquiditätsgrade',
    zu('Was steht im Zähler?', ['1. Grad', '2. Grad', '3. Grad'], [('nur Zahlungsmittel', 0), ('+ Forderungen', 1), ('+ Vorräte', 2)], '', 1),
    nu('Kasse {K} €, Forderungen {F} €, kurzfr. Verbindlichkeiten {V} €. Liquidität 2. Grades?', {'K': [20000, 200000, 20000], 'F': [20000, 400000, 20000], 'V': [40000, 400000, 40000]}, '(K+F)/V*100', '({K} + {F}) ÷ {V} · 100 % = {=(K+F)/V*100} %', '%', 1, wenn='((K+F)/V*100) == round((K+F)/V*100, 1)', lvl=2),
    mc('Liquidität heißt …', 'zahlen bei Fälligkeit', ['Ertrag ≥ Aufwand', 'hoher Gewinn', 'viel Eigenkapital'], '', 1),
    mc('Warum zählen Grundstücke nicht zur Liquidität?', 'schwer schnell zu verkaufen', ['gehören zum Fremdkapital', 'sind Zahlungsmittel', 'haben keinen Wert'], '', 2),
    mc('Rentabel, aber zahlungsunfähig: Was droht?', 'Insolvenz', ['Diversifikation', 'Arbitrage', 'Normierung'], 'Verknüpfung zu den Rechtsformen.', 3))

t = 'effizienz'
fam(t, 'eff', 'Unterscheidet Effizienz und Effektivität',
    zu('Effizienz oder Effektivität?', ['Effizienz', 'Effektivität'], [('Dinge richtig tun', 0), ('richtige Dinge tun', 1), ('Ergebnis ÷ Aufwand', 0), ('Ergebnis ÷ Ziel', 1), ('Kosten-Nutzen', 0), ('Soll-Ist', 1)], '', 1),
    mc('Ein Kraftwerk hat 60 % Wirkungsgrad. Das betrifft …', 'Effizienz', ['Effektivität', 'Liquidität', 'Rentabilität'], '', 2),
    mc('300 Tüten in Rekordzeit, aber die Sorte kauft niemand:', 'effizient, nicht effektiv', ['effektiv, nicht effizient', 'weder noch', 'beides'], '', 2),
    nu('Umsatz {U} €, Vorleistungen {V} €. Wertschöpfung?', {'U': [200000, 3000000, 100000], 'V': [100000, 2000000, 100000]}, 'U-V', '{U} − {V} = {=U-V} €', '€', 0, wenn='U > V', lvl=1),
    bes('Beschrifte, wer welchen Teil der Wertschöpfung erhält.', [(130, 6, 100, 40, '=Wertschöpfung'), (4, 90, 82, 50, 'Lohn'), (94, 90, 82, 50, 'Zins'), (184, 90, 82, 50, 'Gewinn'), (274, 90, 82, 50, 'Steuer')],
        ['Miete'], 'Mitarbeiter, Fremdkapitalgeber, Eigenkapitalgeber, Staat.', 2, deko=_pfeil(180, 48, 45, 88) + _pfeil(180, 48, 135, 88) + _pfeil(180, 48, 225, 88) + _pfeil(180, 48, 315, 88) + _txt(45, 156, 'Mitarbeiter', 12, 600) + _txt(135, 156, 'Bank', 12, 600) + _txt(225, 156, 'Eigentümer', 12, 600) + _txt(315, 156, 'Staat', 12, 600)))

# ================= k3 =================
t = 'elastizitaet'
fam(t, 'deuten', 'Deutet Elastizitätswerte',
    mc('Wenn ε = 0,6 ist, ist die Nachfrage …', 'unelastisch', ['elastisch', 'einheitselastisch', 'völlig unelastisch'], '', 1, True),
    mc('Elastizität ist …', 'Stärke der Mengenreaktion auf den Preis', ['Preis im Marktgleichgewicht', 'Umsatzänderung je 1 € Preis', 'Anteil zufriedener Kunden'], '', 1, True),
    zu('Welcher Bereich?', ['unelastisch', 'einheitselastisch', 'elastisch'], [('ε = 0,4', 0), ('ε = 1', 1), ('ε = 2,5', 2), ('ε = 0,9', 0), ('ε = 1,9', 2)], '', 1),
    nu('Preis +{P} %, Menge −{M} %. Elastizität (Betrag)?', {'P': [5, 20, 5], 'M': [5, 40, 5]}, 'M/P', '{M} ÷ {P} = {=M/P}', '', 2, wenn='(M/P) == round(M/P, 2)', lvl=1, kl=True),
    mc('Standardsatz bei ε = 2:', 'Preis +1 % → Nachfrage −2 %', ['Preis +1 € → Nachfrage −2 Stück', 'Preis +2 % → Nachfrage −1 %', 'Preis +1 % → Umsatz +2 %'], '', 2, True))
fam(t, 'kurven', 'Erkennt Nachfragekurven und Einflussfaktoren',
    hotpunkt('Tippe auf die völlig unelastische Nachfrage.',
        _kasten(4, 10, 110, 130) + _kasten(124, 10, 110, 130) + _kasten(244, 10, 110, 130) + linie([(60, 22), (60, 128)]) + linie([(136, 75), (222, 75)]) + linie([(256, 30), (290, 90), (342, 120)]),
        (60, 75, 30), 'Senkrecht: Menge bleibt bei jedem Preis gleich.', 2, H=150),
    li('Wovon hängt die Elastizität ab? Nennen Sie vier Faktoren.', [['Substitution', 'Alternativen', 'Ersatz'], ['Einkommen', 'Budget'], ['Zeit', 'kurzfristig', 'langfristig'], ['Not', 'Dringlichkeit', 'Bedürfnis', 'Sucht']], '', 2),
    mc('Benzin ist kurzfristig eher …', 'unelastisch', ['elastisch', 'völlig elastisch', 'einheitselastisch'], '', 1),
    mc('Luxusautos sind weniger elastisch als normale Marken, weil …', 'Preis für Käufer kaum zählt', ['es mehr Ersatz gibt', 'der Staat sie fördert', 'sie Verbrauchsgüter sind'], '', 2, True),
    mc('Welcher Begriff aus der Five-Forces-Analyse hängt eng mit hoher Elastizität zusammen?', 'Ersatzprodukte', ['Austrittsbarrieren', 'Rückwärtsintegration', 'Netzwerkeffekt'], 'Viele Substitute → elastisch.', 3))

t = 'mittelwert'
fam(t, 'rechnen', 'Rechnet nach der Mittelwertmethode',
    ns('Parkhaus: 50 Plätze zu 12 €, nach Senkung 80 Plätze zu 9 €. ε (Mittelwertmethode, zwei Stellen)?', 1.62, '(30/65) ÷ (3/10,5)', '', 2, True),
    ns('Shishabar: 5 Köpfe zu 10 €, 15 Köpfe zu 6 €. ε (Mittelwertmethode)?', 2, '(10/10) ÷ (4/8)', '', 2, True),
    ns('Orangensaft 1,90 € → 1,50 €, 3.700 → 4.800. ε (eine Stelle)?', 1.1, '(1.100/4.250) ÷ (0,4/1,7)', '', 2, True),
    ns('D(p) = 150 − 5p, Preis 20 € → 25 €. ε (Mittelwertmethode)?', 3, 'Mengen 50 → 25', '', 3, True),
    nu('Preis {P1} € → {P2} €, Menge {M1} → {M2}. ε (Mittelwertmethode, zwei Stellen)?', {'P1': [2, 10, 1], 'P2': [3, 12, 1], 'M1': [40, 200, 10], 'M2': [20, 180, 10]}, 'abs(((M2-M1)/((M2+M1)/2))/((P2-P1)/((P2+P1)/2)))', 'ε = {=abs(((M2-M1)/((M2+M1)/2))/((P2-P1)/((P2+P1)/2)))}', '', 2, wenn='P2 > P1 and M2 < M1', lvl=2, kl=True))
fam(t, 'formel', 'Kennt die Formel und ihre Grenzen',
    lu('ε = |((M₂ − M₁) ÷ ((M₂ + M₁) ÷ [[0]])) ÷ ((p₂ − p₁) ÷ ((p₂ + p₁) ÷ [[1]]))|', [['2'], ['2']], 'Mittelwerte bilden.', 2),
    mc('Warum teilt man durch den Mittelwert?', 'gleiches Ergebnis in beide Richtungen', ['Ergebnis immer über 1', 'nur ein Punkt bekannt', 'Ableitung unbekannt'], '', 2),
    mc('Wann ist die Mittelwertmethode ungenau?', 'Punkte weit auseinander', ['Preise ganzzahlig', 'Menge steigt', 'Funktion gegeben'], '', 2),
    mc('Preis 4 € → 6 €, Nachfrage 120 → 80. ε = ?', '1', ['0,4', '2', '40'], '', 2, True),
    rh('Ordne die Rechenschritte.', ['Mengenänderung durch mittlere Menge', 'Preisänderung durch mittleren Preis', 'beides teilen', 'Betrag und Standardsatz'], '', 1))

t = 'punktelastizitaet'
fam(t, 'rechnen', 'Rechnet die Punktelastizität',
    mc('D(p) = 20.000 − 5p. Preiselastizität bei p = 800?', '0,25', ['2', '4', '0,5'], '5 · 800 ÷ 16.000.', 2, True),
    nu('D(p) = {A} − {B}p. ε bei p = {P} (zwei Stellen)?', {'A': [100, 1000, 50], 'B': [1, 10, 1], 'P': [5, 60, 5]}, 'B*P/(A-B*P)', 'Q = {=A-B*P}; ε = {B} · {P} ÷ {=A-B*P} = {=B*P/(A-B*P)}', '', 2, wenn='A - B*P > 0 and (B*P/(A-B*P)) == round(B*P/(A-B*P), 2)', tipp='ε = |D′(p) · p ÷ Q|', lvl=2, kl=True),
    ns('D(p) = 8 − 2p, p = 2. ε?', 1, 'Q = 4; 2 · 2 ÷ 4', '', 1, True),
    ns('S(p) = 1.800 + 240p, D(p) = 3.550 − 266p. ε im Gleichgewicht (zwei Stellen)?', 0.35, 'p* ≈ 3,46; Q* ≈ 2.630', '', 3, True),
    nu('D(p) = {A} − {B}p. Bei welchem Preis ist die Nachfrage genau einheitselastisch?', {'A': [100, 2000, 100], 'B': [1, 10, 1]}, 'A/(2*B)', 'Mitte der Geraden: p = {A} ÷ (2 · {B}) = {=A/(2*B)} €', '€', 2, lvl=3))
fam(t, 'methode', 'Wählt die richtige Methode',
    zu('Welche Methode?', ['Mittelwert', 'Punkt'], [('zwei Preis-Mengen-Paare', 0), ('Nachfragefunktion', 1), ('Marktgleichgewicht', 1), ('Parkhaus vorher/nachher', 0)], '', 1),
    mc('Gerade Nachfrage: Ist ε überall gleich?', 'nein, p/Q ändert sich', ['ja, Steigung gleich', 'ja, immer 1', 'nein, immer 0'], '', 2),
    hotpunkt('Tippe auf den Bereich der Nachfragegeraden, in dem die Nachfrage elastisch ist.', achse(40, 220, 350, 10, 'Q', 'p') + linie([(40, 30), (330, 220)]) + _txt(185, 120, 'ε = 1', 12, 600, 'var(--dg-b)', 'start'),
             (90, 63, 30), 'Oben links (hoher Preis, kleine Menge): elastisch.', 3),
    mc('Ohne Angabe nimmt man im Marktgleichgewicht die Ableitung von …', 'D(p)', ['S(p)', 'S(p) + D(p)', 'G(x)'], '', 2))

t = 'effekte'
fam(t, 'rechnen', 'Berechnet Preis-, Mengen- und Gesamteffekt',
    nu('Preis {P1} € → {P2} €, Menge {M1} → {M2}. Mengeneffekt?', {'P1': [5, 20, 1], 'P2': [3, 18, 1], 'M1': [20, 200, 10], 'M2': [30, 300, 10]}, '(M2-M1)*P2', '({M2} − {M1}) · {P2} = {=(M2-M1)*P2} €', '€', 2, wenn='P2 < P1 and M2 > M1', lvl=2, kl=True),
    nu('Preis {P1} € → {P2} €, Menge {M1} → {M2}. Preiseffekt?', {'P1': [5, 20, 1], 'P2': [3, 18, 1], 'M1': [20, 200, 10], 'M2': [30, 300, 10]}, '(P2-P1)*M1', '({P2} − {P1}) · {M1} = {=(P2-P1)*M1} €', '€', 2, wenn='P2 < P1 and M2 > M1', lvl=2, kl=True),
    nu('Preis {P1} € → {P2} €, Menge {M1} → {M2}. Gesamteffekt?', {'P1': [5, 20, 1], 'P2': [3, 18, 1], 'M1': [20, 200, 10], 'M2': [30, 300, 10]}, 'P2*M2-P1*M1', '{=P2*M2} − {=P1*M1} = {=P2*M2-P1*M1} €', '€', 2, wenn='P2 < P1 and M2 > M1', lvl=2, kl=True),
    ns('Orangensaft 1,90 € → 1,50 €, 3.700 → 4.800. Gesamteffekt?', 170, '1.650 − 1.480', '€', 2, True),
    bes('Beschrifte die Flächen im Preis-Mengen-Diagramm (Preissenkung).', [(40, 60, 120, 30, 'Preiseffekt'), (160, 90, 90, 130, 'Mengeneffekt'), (40, 90, 120, 130, 'Erlös, der bleibt')], ['Fixkosten'], '', 3,
        deko=achse(40, 220, 350, 10, 'Menge', 'Preis') + linie([(40, 30), (330, 160)], 'var(--dg-b)'), H=240))
fam(t, 'deuten', 'Verbindet Effekte und Elastizität',
    mc('Elastische Nachfrage, Preissenkung:', 'ME überwiegt, Erlös steigt', ['PE überwiegt, Erlös sinkt', 'beide gleich', 'Menge sinkt'], '', 2, True),
    mc('Unelastische Nachfrage, Preiserhöhung:', 'Erlös steigt', ['Erlös sinkt', 'Erlös gleich', 'Erlös negativ'], '', 2, True),
    zu('Wirkung?', ['heben sich auf', 'ME überwiegt', 'PE überwiegt'], [('ε = 1', 0), ('elastisch, Preissenkung', 1), ('unelastisch, Preissenkung', 2)], '', 2, True),
    blk('Richtig oder falsch?', [('PE rechnet mit der alten Menge.', True), ('ME rechnet mit dem alten Preis.', False), ('GE = Erlös neu − Erlös alt.', True), ('Bei ε > 1 lohnt eine Preiserhöhung für den Erlös.', False)], '', 2, True))

# ================= k4 =================
t = 'opportunitaet'
fam(t, 'alltag', 'Bestimmt Opportunitätskosten',
    mc('Spaghetti oder Milchreis, man nimmt Milchreis. Opportunitätskosten?', 'die Spaghetti', ['der Milchreis', 'beides', 'keine'], '', 1, True),
    mc('Spaghetti und Suppe, Sie nehmen Gulasch. Opportunitätskosten?', 'das bessere der beiden anderen', ['das Gulasch', 'Spaghetti + Suppe', 'nur der Preis'], '', 2, True),
    mc('Opportunitätskosten sind …', 'entgangener Nutzen der besten Alternative', ['Preis des gewählten Guts', 'Summe aller Alternativen', 'Kosten in der Zukunft'], '', 1, True),
    ns('Tom kann 8 h jobben (12 €/h) oder ein Festival besuchen (Ticket 60 €). Volle Kosten des Festivals?', 156, '60 + 8 · 12', '€', 3))
fam(t, 'robinson', 'Rechnet mit Robinson',
    nu('In 12 h: {S} Wildschweine oder {W} Liter Wasser. Wie viele Liter kostet ein Schwein?', {'S': [2, 10, 1], 'W': [4, 30, 2]}, 'W/S', '{W} ÷ {S} = {=W/S}', 'Liter', 2, wenn='(W/S) == round(W/S, 1)', lvl=2, kl=True),
    ns('5 Schweine oder 10 Liter: Wie viele Schweine kostet 1 Liter?', 0.5, '5 ÷ 10', 'Schweine', 2, True),
    hotpunkt('Tippe auf eine Kombination, die Robinson mit 12 Stunden NICHT erreichen kann.', achse(40, 220, 350, 10, 'Wasser', 'Schweine') + linie([(40, 60), (320, 220)]) + _txt(120, 180, 'möglich', 12, 600, 'var(--dg-b)'),
             (270, 90, 40), 'Oberhalb der Linie: unmöglich.', 2),
    mc('Robinson baut eine Falle (10 statt 5 Schweine). Die Möglichkeitengrenze …', 'dreht nach außen', ['dreht nach innen', 'bleibt gleich', 'verschwindet'], '', 2, True),
    kz('„There is no such thing as a free lunch“ heißt: Nichts ist …?', ['umsonst', 'gratis', 'kostenlos'], '', 1))

t = 'grenznutzen'
fam(t, 'gn', 'Versteht Grenznutzen und Grenzkosten',
    mc('Wasser ist lebensnotwendig. Der Grenznutzen ist also …', 'abnehmend', ['zunehmend', 'groß', 'klein'], '', 1, True),
    mc('Grenznutzen ist …', 'Nutzen einer weiteren Einheit', ['Nutzen aller Einheiten', 'Nutzen der ersten Einheit', 'Preis der letzten Einheit'], '', 1, True),
    ns('Grenznutzen: 10, 8, 6, 4,5. Gesamtnutzen nach vier Einheiten?', 28.5, '10 + 8 + 6 + 4,5', '', 2),
    mc('Konsumieren lohnt, solange …', 'Grenznutzen > Grenzkosten', ['Gesamtnutzen steigt', 'Preis sinkt', 'Grenznutzen > 0'], '', 2),
    lu('Rational entscheidende Menschen denken in [[0]].', [['Grenzbegriffen', 'Grenzgrößen']], '', 2),
    mc('Das Wasser-Diamanten-Paradox erklärt sich durch …', 'den Grenznutzen', ['die Elastizität', 'den Break-even', 'die Hurwicz-Regel'], '', 3),
    mc('Welcher Begriff aus der Gewinnrechnung entspricht dem Grenznutzen-Denken?', "G'(x), der Grenzgewinn", ['der Break-even-Punkt', 'die Fixkosten', 'die EK-Quote'], '', 3))

t = 'maerkte'
fam(t, 'regeln', 'Erkennt die Regeln 4 bis 6',
    zu('Welche Regel?', ['4: Anreize', '5: Märkte', '6: Staat'], [('wenig Kontrollen → mehr Schwarzfahrer', 0), ('unsichtbare Hand', 1), ('Kartellamt', 2), ('Angebot und Nachfrage', 1), ('Mindestlohn', 2)], '', 1),
    mc('Die „unsichtbare Hand“ stammt von …', 'Adam Smith', ['Schumpeter', 'Kondratieff', 'Porter'], '', 1),
    mc('Problem einer Welt ohne Geld:', 'doppelte Übereinstimmung der Wünsche', ['keine Arbeitsteilung', 'keine Dienstleistungen', 'keine Steuern'], '', 2),
    mc('Nebenwirkung eines Mindestlohns:', 'weniger einfache Jobs', ['höhere Gewinne', 'sinkende Preise', 'mehr Banken'], '', 2),
    li('Wie kann der Staat Marktergebnisse verbessern? Nennen Sie drei Wege.', [['Märkte bereitstellen', 'Bereitstellen', 'Infrastruktur'], ['Marktschutz', 'Kartelle'], ['Marktkontrolle', 'Kontrolle']], '', 2),
    hotpunkt('Tippe auf das Marktgleichgewicht.', achse(40, 220, 350, 10, 'Menge', 'Preis') + linie([(60, 40), (330, 200)]) + linie([(60, 200), (330, 40)], 'var(--dg-b)'), (195, 120, 18), '', 1),
    mc('Was erzeugt eine Höchstmiete unter dem Gleichgewicht?', 'Nachfrageüberschuss', ['Angebotsüberschuss', 'Gleichgewicht', 'Preisanstieg'], '', 3))

t = 'innovation'
fam(t, 'schumpeter', 'Kennt schöpferische Zerstörung, Risiko und Arbitrage',
    li('Nennen Sie Schumpeters vier Arten von Neuerungen.', [['neues Produkt', 'Produkt'], ['Produktionsmethode', 'Methode'], ['Absatzmarkt'], ['Beschaffungsmarkt']], '', 2),
    zu('Risiko oder Unsicherheit?', ['Risiko', 'Unsicherheit'], [('Wahrscheinlichkeiten bekannt', 0), ('Wahrscheinlichkeiten unbekannt', 1), ('Würfeln', 0), ('völlig neues Produkt', 1)], '', 1),
    zu('Welche Arbitrage?', ['räumlich', 'zeitlich'], [('Ware vom Großhändler in die Stadt', 0), ('günstig kaufen, später teurer verkaufen', 1), ('Börse zu verschiedenen Zeiten', 1)], '', 2),
    zu('Welche Art von Neuerung?', ['Produkt', 'Methode', 'Absatzmarkt', 'Beschaffungsmarkt'], [('Streaming', 0), ('Fließband', 1), ('Export nach China', 2), ('Lithium aus Südamerika', 3)], '', 2),
    mc('Aufgabe des Staates bei schöpferischer Zerstörung:', 'Neues zulassen', ['Altes schützen', 'Innovation verbieten', 'Preise festsetzen'], '', 2),
    rh('Ordne die Kondratieff-Wellen.', ['Dampfmaschine, Baumwolle', 'Eisenbahn, Stahl', 'Elektro, Chemie', 'Auto, Petrochemie', 'Informationstechnik'], '', 2))

t = 'wirtschaftsordnung'
fam(t, 'ordnung', 'Unterscheidet Wirtschaftsordnungen',
    zu('Marktwirtschaft oder Planwirtschaft?', ['Markt', 'Plan'], [('Privateigentum', 0), ('Preise staatlich', 1), ('Vertragsfreiheit', 0), ('gelenkter Konsum', 1), ('keine Absicherung', 0), ('volle Absicherung', 1)], '', 1),
    li('Nennen Sie Grundprinzipien der sozialen Marktwirtschaft.', [['Wettbewerb'], ['Einkommen', 'Vermögen'], ['Struktur', 'Wachstum'], ['Konjunktur'], ['Sozial']], '', 2, n=4),
    mc('Für Wachstum spricht laut Vorlesung:', 'es erleichtert die Schuldenlast', ['es senkt die Preise', 'es ersetzt den Staat', 'es senkt die Löhne'], '', 2),
    mc('Im Mittelpunkt der Planwirtschaft steht …', 'der Staat', ['das Individuum', 'der Markt', 'der Aktionär'], '', 1),
    zu('Welcher Politikbereich?', ['Wettbewerb', 'Konjunktur', 'Sozial'], [('Kartellverbot', 0), ('Konjunkturpaket in der Krise', 1), ('Arbeitslosenversicherung', 2)], '', 2),
    blk('Richtig oder falsch?', [('Freie Marktwirtschaft: völlige Konsumfreiheit.', True), ('Planwirtschaft: freie Berufswahl.', False), ('Soziale Marktwirtschaft verbindet Markt und Ausgleich.', True), ('Freie Marktwirtschaft: völlige soziale Absicherung.', False)], '', 2))

# ================= k5 =================
t = 'homo-oeconomicus'
fam(t, 'ho', 'Kennt homo oeconomicus und die beiden Perspektiven',
    blk('Gehört das zum homo oeconomicus?', [('verarbeitet Informationen kostenlos und sofort', True), ('kennt alle Alternativen', True), ('lässt sich von der Tagesform leiten', False), ('wählt den größten Nutzen', True)], '', 2),
    zu('Ökonomisch oder verhaltenswissenschaftlich?', ['ökonomisch', 'verhaltenswiss.'], [('rational', 0), ('begrenzt rational', 1), ('Nutzen maximieren', 0), ('Nutzen unter Nebenbedingungen', 1)], '', 1),
    mc('Warum gibt es den homo oeconomicus trotzdem?', 'Er erleichtert das Rechnen', ['Er beschreibt Menschen genau', 'Das Gesetz verlangt ihn', 'Menschen kaufen rational'], '', 2),
    rh('Ordne die Phasen der BWL.', ['ökonomisch (bis 1960er/70er)', 'verhaltenswissenschaftlich (1970–2000)', 'beide verbinden (seit 2000)'], '', 1),
    mc('Welches spätere Thema baut auf dem homo oeconomicus auf?', 'klassische Entscheidungstheorie', ['Prospect Theory', 'Garbage Can', 'Werturteile'], '', 3))

t = 'stakeholder'
fam(t, 'ansatz', 'Ordnet Aussagen zu',
    zu('Shareholder oder Stakeholder?', ['Shareholder', 'Stakeholder'], [('langfristige Gewinnmaximierung', 0), ('Ausgleich von Interessen', 1), ('Risikoträger entscheidet', 0), ('Interessensgruppen entscheiden', 1), ('Gewinn wird aufgeteilt', 1), ('Risikoträger profitiert', 0)], '', 1, True),
    mc('Nach dem Stakeholder-Ansatz gilt:', 'Risiko und Entscheidung getrennt', ['Risiko und Entscheidung zusammen', 'nur Eigentümer profitieren', 'Ziel nur Gewinnmaximierung'], '', 2, True),
    mc('Widerspruch im Stakeholder-Ansatz:', 'günstige Preise vs. hohe Gehälter', ['Eigentümer vs. Aktionäre', 'Staat vs. Steuern', 'Bank vs. Zinsen'], '', 2, True),
    zu('Welcher Anspruch?', ['Gewinn', 'Zinsen', 'Gehalt', 'günstiger Preis'], [('Eigentümer', 0), ('Bank', 1), ('Arbeitnehmer', 2), ('Kunden', 3)], '', 1),
    bes('Beschrifte die Antworten des Shareholder-Ansatzes auf die drei Fragen.', [(4, 10, 160, 50, '=Ziele?'), (196, 10, 160, 50, 'langfristige Gewinnmaximierung'), (4, 70, 160, 50, '=Wer entscheidet?'), (196, 70, 160, 50, 'Risikoträger'), (4, 130, 160, 50, '=Wer profitiert?'), (196, 130, 160, 50, 'Eigentümer')],
        ['Ausgleich von Interessen', 'Interessensgruppen'], '', 3, kl=True, deko=_pfeil(166, 35, 194, 35) + _pfeil(166, 95, 194, 95) + _pfeil(166, 155, 194, 155)))

t = 'shareholder-value'
fam(t, 'sv', 'Wendet die Shareholder-Value-Bedingung an',
    nu('Kapital {K} €, Alternativzins {I} %. Wie hoch muss E − A mindestens sein?', {'K': [100000, 2000000, 100000], 'I': [2, 10, 1]}, 'K*I/100', '{K} · {=I/100} = {=K*I/100} €', '€', 0, lvl=2),
    mc('Die Investition lohnt sich, wenn …', 'E − A > K · i', ['E − A > 0', 'K · i > E − A', 'E > K'], '', 1),
    ns('Kapital 500.000 €, Zins 6 %, E − A = 25.000 €. Fehlbetrag zur Messlatte?', 5000, '30.000 − 25.000', '€', 2),
    mc('Betrag über K · i heißt …', 'Economic Value Added', ['Deckungsbeitrag', 'Opportunitätskosten', 'Wertschöpfung'], '', 2),
    zu('Welche Perspektive?', ['ökonomisch', 'verhaltenswiss.'], [('Vorrang der Eigentümer', 0), ('gleicher Anspruch aller', 1), ('Konflikte per Vertrag', 0), ('Konflikte per Diskurs', 1)], '', 2),
    mc('K · i ist eng verwandt mit welchem Begriff aus den Prinzipien?', 'Opportunitätskosten', ['Grenznutzen', 'Arbitrage', 'Uno actu'], 'Der entgangene Zins ist der Preis der Investition.', 3))

t = 'werturteile'
fam(t, 'wu', 'Unterscheidet Werturteile',
    zu('Primär oder sekundär?', ['primär', 'sekundär'], [('absolutes Urteil', 0), ('abgeleitetes Urteil', 1), ('bewertet Ziele', 0), ('bewertet Mittel', 1), ('ethisch-normativ', 0), ('praktisch-normativ', 1)], '', 1),
    zu('Was für eine Aussage?', ['primär', 'sekundär'], [('„Kinderarbeit ist unvertretbar.“', 0), ('„Leasing ist hier günstiger als Kauf.“', 1), ('„Bonusprogramm bindet besser als Rabatt.“', 1), ('„Firmen sollen das Klima schützen.“', 0)], '', 2),
    mc('Die ökonomische BWL beschränkt sich auf …', 'sekundäre Werturteile', ['primäre Werturteile', 'keine Urteile', 'ethische Urteile'], '', 2),
    lu('Primäre Werturteile bewerten die [[0]], sekundäre die [[1]].', [['Ziele'], ['Mittel']], '', 1),
    rv('Erklären Sie primäre und sekundäre Werturteile.', 'Primäre Werturteile sind absolute Urteile über Ziele. Sekundäre Werturteile sind abgeleitet und bewerten nur die Mittel zu einem gegebenen Ziel.', ['primär: absolut, Ziele', 'sekundär: abgeleitet, Mittel'], 3),
    mc('Wo spielen primäre Werturteile eher eine Rolle?', 'Personalwesen', ['Kostenrechnung', 'Break-even', 'Bilanzsumme'], '', 2),
    mc('Welche Position passt zur Bewertung der Ziele?', 'verhaltenswiss. BWL', ['ökonomische BWL', 'klassische ET', 'Shareholder-Ansatz'], '', 2))

# ================= k6 =================
t = 'et-ueberblick'
fam(t, 'et', 'Kennt Ziel und Richtungen der Entscheidungstheorie',
    zu('Klassisch oder verhaltenswissenschaftlich?', ['klassisch', 'verhaltenswiss.'], [('präskriptiv', 0), ('deskriptiv', 1), ('Rational Choice', 0), ('Entscheidungslogik', 0), ('wie Menschen wirklich entscheiden', 1)], '', 1),
    zu('Ex ante oder ex post?', ['ex ante', 'ex post'], [('vorher durchdenken', 0), ('hinterher erklären', 1)], '', 1),
    mc('Menschenbild der klassischen ET:', 'homo oeconomicus', ['begrenzt rationaler Mensch', 'würfelnder Affe', 'Stakeholder'], '', 1),
    zu('Würdigung der klassischen ET?', ['positiv', 'negativ'], [('strukturiert Probleme ex ante', 0), ('Modell einer idealen Welt', 1), ('Training für rationale Entscheidungen', 0), ('unrealistisch', 1)], '', 2),
    mc('„Präskriptiv“ heißt …', 'wie man entscheiden soll', ['wie man entscheidet', 'warum man entschied', 'ohne Regel'], '', 2),
    mc('Synonym der verhaltenswissenschaftlichen ET:', 'deskriptive ET', ['normative ET', 'Rational Choice', 'Decision science'], '', 2),
    rh('Zwei Stufen:', ['Problem strukturieren', 'Lösung finden'], '', 1),
    blk('Richtig oder falsch?', [('Die klassische ET ist normativ.', True), ('Die verhaltenswiss. ET schreibt vor, wie man entscheidet.', False), ('Decision science gehört zur klassischen ET.', True), ('Ex post heißt vorher.', False)], '', 2))

t = 'et-struktur'
fam(t, 'struktur', 'Strukturiert ein Entscheidungsproblem',
    zu('Zielsystem, Alternative oder Umwelt?', ['Zielsystem', 'Alternative', 'Umwelt'], [('niedriger Kaufpreis', 0), ('Innenstadt', 1), ('Immobilienkonjunktur', 2), ('gute Anbindung', 0), ('Vorort', 1), ('Schnellstraße kommt', 2)], '', 1),
    bes('Beschrifte den Aufbau eines Entscheidungsproblems.', [(90, 4, 180, 36, '=Entscheidungsproblem'), (4, 60, 170, 70, 'Zielsystem'), (186, 60, 170, 32, 'Alternativen'), (186, 98, 170, 32, 'Umwelteinflüsse'), (4, 150, 352, 36, 'Lösungsfindung')],
        ['Garbage Can'], 'Stufe 1: Zielsystem + Entscheidungsfeld; Stufe 2: Lösung.', 2, deko=_pfeil(180, 42, 180, 58) + _pfeil(180, 132, 180, 148)),
    mc('Das Entscheidungsfeld besteht aus …', 'Alternativen und Umwelt', ['Zielsystem und Alternativen', 'Zielsystem und Umwelt', 'nur Präferenzen'], '', 2),
    li('Welche Abwägungen gehören zum Abbruchkriterium?', [['Vollständigkeit', 'Übersichtlichkeit'], ['Suchkosten', 'Verbesserungspotenzial'], ['Realität', 'Fantasie']], '', 3),
    mc('Warum sucht man nicht ewig nach Alternativen?', 'Suchkosten übersteigen den Nutzen', ['gesetzlich verboten', 'es gibt nur drei', 'Alternativen nutzen nichts'], 'Wieder Grenzdenken.', 2),
    mc('Welches Thema zeigt, dass echte Menschen schon nach wenigen Alternativen aufhören?', 'begrenzte Rationalität', ['Bayes-Regel', 'Zieldominanz', 'Shareholder Value'], '', 3))

t = 'zielbeziehungen'
fam(t, 'zb', 'Erkennt Zielbeziehungen',
    zu('Welche Zielbeziehung?', ['komplementär', 'konkurrierend', 'indifferent'], [('Kostensenkung und Gewinn', 0), ('Qualität rauf, Kosten runter', 1), ('Kantinenkasse und Produktionskosten', 2), ('Umsatz und Gewinn', 0), ('hohe Löhne, niedrige Personalkosten', 1)], '', 1, True),
    mc('Zielkonkurrenz heißt …', 'ein Ziel geht zu Lasten des anderen', ['Ziele fördern sich', 'kein Einfluss', 'Firmen konkurrieren'], '', 1, True),
    hotpunkt('Tippe auf das Diagramm mit konkurrierenden Zielen.', _kasten(4, 10, 110, 120) + _kasten(124, 10, 110, 120) + _kasten(244, 10, 110, 120) + linie([(20, 118), (100, 30)]) + linie([(140, 30), (220, 118)]) + linie([(260, 74), (340, 74)]),
        (179, 70, 50), 'Fallende Linie.', 2, True, H=145),
    mc('Was tut man bei konkurrierenden Zielen?', 'Lösungsverfahren wählen', ['beide voll erreichen', 'eins vergessen', 'nichts'], '', 2),
    blk('Richtig oder falsch?', [('Umsatz und Gewinn sind meist komplementär.', True), ('Zielkonkurrenz = zwei Firmen konkurrieren.', False), ('Zielbeziehungen können sich je nach Bereich ändern.', True), ('Indifferente Ziele behindern sich.', False)], '', 2, True),
    kz('Wie heißen Ziele, die sich gegenseitig fördern?', ['komplementär', 'komplementäre'], '', 1, True),
    mc('Rabattschlachten: mehr Umsatz, weniger Gewinn. Umsatz und Gewinn sind dann …', 'konkurrierend', ['komplementär', 'indifferent', 'identisch'], '', 3))

t = 'zielsystem'
fam(t, 'loesung', 'Wählt bei mehreren Zielen eine Alternative',
    mc('Absatz a1 800, a2 600, a3 400, a4 200. Absatz dominant:', 'a1', ['a2', 'a3', 'a4'], '', 1, True),
    mc('Gewinn a1 7.000 / a2 7.000 / a3 6.000; Umwelt −4 / −2 / 0. Erst Gewinn, dann Umwelt:', 'a2', ['a1', 'a3', 'a4'], '', 2, True),
    mc('Eine Alternative ist effizient, wenn …', 'keine andere sie dominiert', ['sie überall die beste ist', 'sie den höchsten Gewinn hat', 'sie am billigsten ist'], '', 2, True),
    mc('Warum normiert man vor der Gewichtung?', 'große Zahlen überdecken sonst', ['Ergebnisse werden negativ', 'man braucht keine Gewichte', 'Gewinn = Umsatz'], '', 2, True),
    ns('a1: Umsatz 800.000, Gewinn 7.000; Gewichte 25 % / 75 %. Einfache Multiplikation?', 205250, '200.000 + 5.250', '', 2),
    ns('Normierung: a2 Umsatz 600.000 (max 800.000), Gewinn 8.000 (max). Wert bei 25/75 (vier Stellen)?', 0.9375, '0,25 · 0,75 + 0,75', '', 3),
    zu('Welche Methode?', ['Dominanz', 'Effizienz', 'Lexikographie', 'Nutzenfunktion'], [('ein Ziel entscheidet', 0), ('Dominierte streichen', 1), ('Ziele nacheinander', 2), ('Ziele gewichten', 3)], '', 1, True),
    mc('a3 (400 / 6.000 / 0) gegen a4 (200 / 4.000 / 0):', 'a3 dominiert a4', ['a4 dominiert a3', 'keine dominiert', 'gleich gut'], '', 2, True),
    nu('Gewicht Umsatz {W} %. a1: Umsatz normiert 1, Gewinn normiert 0,875. Nutzenwert (vier Stellen)?', {'W': [10, 90, 10]}, 'W/100*1+(1-W/100)*0.875', '{=W/100} · 1 + {=1-W/100} · 0,875 = {=W/100+(1-W/100)*0.875}', '', 4, lvl=3))
