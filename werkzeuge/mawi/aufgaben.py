"""Erzeugt inhalte/mawi/aufgaben.json (große Aufgaben im Klausurstil mit Tipps und Lösungsweg).
Zahlen werden hier gerechnet. Aufruf: python3 werkzeuge/mawi/aufgaben.py"""
import json, math, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
A = []


def de(x, n=2):
    s = f'{x:,.{n}f}'.replace(',', '#').replace('.', ',').replace('#', '.')
    return s[:-3] if n == 2 and s.endswith(',00') else s


def eh(t): return f'<p><b>Lösung</b>: {t}</p>'


def teil(text, punkte, t1, t2, loesung, ergebnis=None, einheit=None, tol=None):
    d = dict(text=text, punkte=punkte, tipp1=t1, tipp2=t2, loesung=loesung)
    if ergebnis is not None:
        d['ergebnis'] = round(ergebnis, 4)
        if einheit: d['einheit'] = einheit
        if tol is not None: d['tol'] = tol
    return d


def aufgabe(id, unter, art, stufe, titel, ausgang, teile, klausur=True):
    A.append(dict(id='mawi-' + id, unter=unter, art=art, stufe=stufe, klausur=klausur, titel=titel, quelle='im Klausurstil', ausgang=ausgang, teile=teile))


# ---------------------------------------------------------------- 1 Andler Bonbons (Vorlesung)
m, kb, w, i = 12, 150, 600, 0.15
x = math.sqrt(2 * m * kb / (w * i)); K = lambda q: m / q * kb + q / 2 * w * i
assert abs(x - math.sqrt(40)) < 1e-9 and K(6) == 570
aufgabe('andler-bonbon', ['andler', 'losgroessen-dilemma'], 'rechnen', 2, 'Optimale Bestellmenge: Zucker für Bonbons',
    '<p>Ein Bonbon-Produzent hat einen Jahresbedarf von <b>12 Tonnen</b> Weißzucker. Zucker kostet derzeit <b>600 €/t</b>. Jede Bestellung verursacht interne und externe Kosten von <b>150 €</b>. Der Lagerhaltungskostensatz (Kapitalbindung und physische Lagerung) beträgt <b>15 %</b>. Bestellt werden kann nur in ganzen Tonnen.</p>', [
    teil('Berechnen Sie die optimale Bestellmenge nach Andler (zunächst ohne Rundung).', 4, 'Formel: x = √(2·m·k_b / (w·i_L)).', 'Prozentsatz als Dezimalzahl: 15 % = 0,15.',
         eh(f'x = √(2 · 12 · 150 / (600 · 0,15)) = √(3.600 / 90) = √40 ≈ <b>{de(x)} t</b>.'), x, 't', 0.02),
    teil('Welche ganzzahlige Bestellmenge wählen Sie? Begründen Sie mit den Gesamtkosten.', 5, 'Vergleichen Sie die beiden Nachbarn von 6,32.', 'K(x) = m/x · k_b + x/2 · w · i_L.',
         eh(f'K(6) = 12/6 · 150 + 6/2 · 90 = 300 + 270 = 570 €; K(7) = 12/7 · 150 + 7/2 · 90 ≈ 257,14 + 315 = 572,14 €. Also <b>6 t</b>, rund 2,14 € günstiger.'), 6, 't'),
    teil('Wie oft muss im Jahr bestellt werden?', 2, 'Bestellhäufigkeit = Jahresbedarf / Bestellmenge.', '12 / 6.', eh('12 / 6 = <b>2-mal</b> im Jahr.'), 2, '-mal'),
    teil('Nennen Sie drei Annahmen des Modells und erläutern Sie eine Schwäche in der Praxis.', 3, 'Was setzt die Formel über Bedarf, Preise, Lieferung voraus?', 'Denken Sie an Mengenrabatte oder Paletten.',
         eh('Konstanter Bedarf je Zeiteinheit, keine Mengenrabatte (Preis unabhängig von der Menge), keine Fehlmengen, sofortige Lieferung, keine Restriktionen, beliebig teilbare Mengen. Schwäche: Gibt es z. B. Mengenrabatte oder Bindung an Paletten/Lkw-Ladungen, stimmt das Optimum nicht mehr; man muss die Kosten der Alternativen vergleichen.'))])

# ---------------------------------------------------------------- 2 Andler Akkus
m2, kb2, w2, i2 = 7200, 120, 250, 0.12
x2 = math.sqrt(2 * m2 * kb2 / (w2 * i2)); K2 = lambda q: m2 / q * kb2 + q / 2 * w2 * i2
aufgabe('andler-akku', ['andler', 'lagerkennzahlen', 'losgroessen-dilemma'], 'rechnen', 3, 'Akkus für die E-Bike-Montage',
    '<p>Die Neckarrad GmbH verbraucht <b>7.200 Akkus</b> pro Jahr gleichmäßig. Ein Akku kostet <b>250 €</b>, eine Bestellung <b>120 €</b>, der Lagerhaltungskostensatz beträgt <b>12 %</b>. Der Lieferant liefert in Kartons zu je <b>40 Stück</b>.</p>', [
    teil('Berechnen Sie die optimale Bestellmenge.', 3, 'Andler-Formel einsetzen.', '2 · 7.200 · 120 / (250 · 0,12).', eh(f'x = √(2 · 7.200 · 120 / 30) = √57.600 = <b>{de(x2, 0)} Stück</b>.'), x2, 'Stück', 0.5),
    teil('Wie hoch sind Bestell-, Lager- und Gesamtkosten bei dieser Menge?', 4, 'K_B = m/x · k_b, K_L = x/2 · w · i_L.', 'Im Optimum sind beide gleich groß.',
         eh(f'K_B = 7.200/240 · 120 = {de(m2 / x2 * kb2)} €; K_L = 240/2 · 250 · 0,12 = {de(x2 / 2 * w2 * i2)} €; K = <b>{de(K2(x2))} €</b>.'), K2(x2), '€', 1),
    teil('Der Lieferant liefert nur ganze Kartons (40 Stück). Passt die optimale Menge? Wie oft wird bestellt?', 2, '240 / 40 = ?', 'Häufigkeit = 7.200 / 240.',
         eh('240 = 6 Kartons, passt genau. Bestellhäufigkeit 7.200 / 240 = <b>30-mal</b> pro Jahr.'), 30, '-mal'),
    teil('Wie hoch ist der durchschnittliche Lagerbestand (ohne Sicherheitsbestand) und die Umschlagshäufigkeit?', 3, 'Ø Bestand = x/2.', 'Umschlag = Jahresverbrauch / Ø Bestand.',
         eh('Ø Bestand = 240 / 2 = 120 Stück; Umschlagshäufigkeit = 7.200 / 120 = <b>60-mal</b>.'), 60, '-mal')])

# ---------------------------------------------------------------- 3 Brutto-Netto
S, Z, L, B, Rv = 2400, 0.04, 380, 500, 120
brutto = S * (1 + Z); netto = brutto - L - B + Rv
aufgabe('brutto-netto', ['brutto-netto', 'bedarfsarten', 'stuecklisten'], 'rechnen', 2, 'Vom Primär- zum Nettobedarf: Laufräder',
    '<p>Die Neckarrad GmbH plant für das Quartal <b>1.200 E-Bikes</b>. Jedes E-Bike hat <b>2 Laufräder</b>. Erfahrungsgemäß fallen <b>4 %</b> Ausschuss an. Im Lager liegen <b>380</b> Laufräder, <b>500</b> sind bestellt, <b>120</b> der Lagerlaufräder sind für Ersatzteilaufträge reserviert.</p>', [
    teil('Welche Bedarfsart sind die E-Bikes, welche die Laufräder? Wie wird der Laufradbedarf ermittelt?', 3, 'Verkaufsfähig oder Bestandteil?', 'Stückliste.',
         eh('E-Bikes: <b>Primärbedarf</b> (verkaufsfähige Enderzeugnisse aus der Vertriebsplanung). Laufräder: <b>Sekundärbedarf</b>, ermittelt über die Stücklistenauflösung: 1.200 · 2 = 2.400.')),
    teil('Berechnen Sie den Bruttobedarf.', 2, 'Sekundärbedarf + Zusatzbedarf.', '4 % von 2.400.', eh(f'2.400 + 4 % = 2.400 + 96 = <b>{de(brutto, 0)}</b> Laufräder.'), brutto, 'Stück'),
    teil('Berechnen Sie den Nettobedarf.', 3, 'Was steht zur Verfügung?', 'Lager und Bestellungen abziehen, Reservierungen wieder addieren.',
         eh(f'{de(brutto, 0)} − 380 − 500 + 120 = <b>{de(netto, 0)}</b> Laufräder.'), netto, 'Stück'),
    teil('Erklären Sie, warum reservierte Bestände addiert werden, und definieren Sie den Bruttobedarf.', 4, 'Sind reservierte Teile verfügbar?', 'Definition: „… benötigter Periodenbedarf“.',
         eh('Reservierte Bestände liegen zwar im Lager (und wurden mit dem Lagerbestand abgezogen), sind aber für vorgemerkte Aufträge bestimmt und stehen nicht zur Verfügung; deshalb werden sie wieder addiert. Bruttobedarf: der für die Fertigung der Erzeugnisse benötigte Periodenbedarf (Sekundärbedarf + Zusatzbedarf).'))])

# ---------------------------------------------------------------- 4 Bestellverfahren und Meldebestand
V, T, SB = 120, 0.5, 180
MB = V * T + SB
aufgabe('bestellverfahren', ['bestellsysteme', 'bestellbegriffe'], 'transfer', 3, 'Bestellverfahren erkennen und begründen',
    '<p>Ein Lagerbestandsverlauf zeigt: Der Bestand sinkt unterschiedlich schnell. Jedes Mal, wenn er die Höhe von <b>240 Stück</b> erreicht, wird bestellt; die Bestellungen erfolgen deshalb in unterschiedlichen Abständen. Nach der Wiederbeschaffungszeit steigt der Bestand jedes Mal um <b>genau 400 Stück</b>. Unten im Bild ist ein Band von <b>180 Stück</b> eingezeichnet.</p>', [
    teil('Benennen Sie das Verfahren und begründen Sie Ihre Antwort anhand der Abbildung.', 4, 'Was löst die Bestellung aus: ein Termin oder ein Bestand?', 'Sind die Sprünge gleich hoch?',
         eh('<b>Bestellpunktverfahren mit fester Bestellmenge</b> (Bestellpunkt-Losgrößen-Verfahren, (s,q)): Bestellt wird immer beim Meldebestand (240), deshalb sind die Zeitpunkte variabel; die Sprünge sind immer gleich hoch (400), also feste Menge.')),
    teil('Benennen Sie die eingezeichneten Größen 240 und 180 und erklären Sie sie.', 4, 'Bei welcher Höhe wird bestellt?', 'Was soll nicht angegriffen werden?',
         eh('240 = <b>Meldebestand</b>: Bestandshöhe, bei der die Bestellung ausgelöst wird. 180 = <b>Sicherheitsbestand</b> (eiserner Bestand): Puffer gegen Fehlmengen, der normalerweise nicht angegriffen wird.')),
    teil('Der Verbrauch beträgt 120 Stück/Monat, die Wiederbeschaffungszeit 0,5 Monate. Bestätigen Sie den Meldebestand rechnerisch.', 3, 'MB = Verbrauch je Periode × WBZ + SB.', '120 · 0,5 + 180.',
         eh(f'MB = 120 · 0,5 + 180 = <b>{de(MB, 0)}</b> Stück.'), MB, 'Stück'),
    teil('Für welchen Bedarfsverlauf ist dieses Verfahren geeignet? Nennen Sie einen Vor- und einen Nachteil.', 3, 'Schwankender oder gleichmäßiger Verbrauch?', 'Was muss ständig passieren?',
         eh('Für Güter mit <b>schwankendem Bedarf</b>. Vorteil: kurzfristige Schwankungen werden ausgeglichen, niedrige Mindestbestände, geringere Kapitalbindung. Nachteil: Bestände müssen ständig kontrolliert werden, höherer Aufwand im Lagerbetrieb.')),
    teil('Wie ändert sich das Bild beim Bestellrhythmusverfahren mit Auffüllen auf einen Soll-Lagerbestand (t,S)?', 2, 'Was ist dann fest, was variabel?', 'Termin fest, Menge variabel.',
         eh('Bestellungen in <b>gleichen Zeitabständen</b>; die Bestellmengen sind <b>variabel</b>, weil jeweils bis zum Soll-Lagerbestand S aufgefüllt wird; eingezeichnet wird eine Linie S statt eines Meldebestands.'))])

# ---------------------------------------------------------------- 5 ABC + XYZ
ITEMS = [('Akkuzellen', 4200, 'X'), ('Motoren', 2600, 'X'), ('Rahmen', 1300, 'Y'), ('Schaltungen', 620, 'Y'), ('Bremsen', 480, 'X'), ('Laufräder', 360, 'Y'), ('Displays', 180, 'Z'), ('Kabel', 110, 'X'), ('Schrauben', 90, 'X'), ('Lack', 60, 'Z')]
kum = []
s = 0
for n_, v, _ in ITEMS:
    s += v; kum.append(s / 100)
aufgabe('abc-xyz', ['abc-analyse', 'xyz-analyse'], 'rechnen', 3, 'ABC- und XYZ-Analyse der Neckarrad GmbH',
    '<p>Jahreseinkaufswerte (T€) und Bedarfsverlauf: Akkuzellen 4.200 (X), Motoren 2.600 (X), Rahmen 1.300 (Y), Schaltungen 620 (Y), Bremsen 480 (X), Laufräder 360 (Y), Displays 180 (Z), Kabel 110 (X), Schrauben 90 (X), Lack 60 (Z). Gesamt 10.000 T€.</p>', [
    teil('Berechnen Sie den kumulierten Wertanteil nach den ersten drei Positionen.', 3, 'Sortieren, aufsummieren, durch 10.000 teilen.', '4.200 + 2.600 + 1.300.',
         eh('(4.200 + 2.600 + 1.300) / 10.000 = <b>81 %</b>.'), 81, '%'),
    teil('Bilden Sie A-, B- und C-Klassen (ca. 80/15/5) und nennen Sie je eine Normstrategie.', 5, 'Grenzen beim kumulierten Anteil.', 'A bis ca. 81 %, B bis ca. 96 %.',
         eh('A: Akkuzellen, Motoren, Rahmen (81 %) → sorgfältig vorbereiten, breit anfragen, lange verhandeln. B: Schaltungen, Bremsen, Laufräder (14,6 %, kumuliert 95,6 %) → Aufwand und Einsparung ausgewogen. C: Displays, Kabel, Schrauben, Lack (4,4 %) → C-Teile-Management: E-Commerce, Kataloge, Beschaffungsdienstleister.')),
    teil('Ordnen Sie Akkuzellen, Displays und Schrauben in die ABC-XYZ-Matrix ein und nennen Sie die Normstrategie.', 6, 'Kombinieren Sie Wertklasse und Bedarfsklasse.', 'AX, CZ, CX.',
         eh('Akkuzellen <b>AX</b>: Just-in-Time, Ship-to-Stock/Ship-to-Line. Displays <b>CZ</b>: ausreichende Lagerhaltung, Beschaffungsdienstleister (bzw. kurzfristige Spontanbeschaffung). Schrauben <b>CX</b>: Rahmenvertrag mit regelmäßiger Anlieferung und erhöhter Lagerhaltung.')),
    teil('Warum ist JIT für ein AZ-Teil ungeeignet?', 2, 'Was setzt JIT voraus?', 'Vorhersagbarkeit.', eh('JIT braucht einen gut planbaren, kontinuierlichen Bedarf. Z-Teile haben diskontinuierlichen, kaum vorhersagbaren Bedarf; Normstrategie ist fallweise Disposition.'))])

# ---------------------------------------------------------------- 6 Kraljic Fall
aufgabe('kraljic-fall', ['kraljic', 'kraljic-dynamik', 'beschaffungsmarkt-macht'], 'transfer', 3, 'Portfolio für die Neckarrad GmbH',
    '<p>Vier Materialgruppen: (1) <b>Aluminiumrohre</b>: 22 % der Materialkosten, viele Anbieter weltweit. (2) <b>Akkuzellen</b>: 35 % der Materialkosten, nur drei qualifizierte Hersteller, lange Qualifizierung. (3) <b>Büromaterial</b>: unter 1 %, überall erhältlich. (4) <b>Display-Controller</b>: 1 % der Materialkosten, nur ein Hersteller, Allokation.</p>', [
    teil('Nennen Sie die beiden Achsen des Kraljic-Portfolios und ordnen Sie sie intern/extern zu.', 2, 'Eine Achse betrifft den Bedarf, eine den Markt.', 'Ergebniseinfluss, Beschaffungskomplexität.',
         eh('<b>Ergebniseinfluss</b> (intern, „profit impact“) und <b>Beschaffungskomplexität</b> (extern, im Original Beschaffungsrisiko).')),
    teil('Ordnen Sie die vier Materialgruppen in das Portfolio ein.', 4, 'Hoch/niedrig je Achse bestimmen.', 'Rohre: Einfluss hoch, Komplexität niedrig.',
         eh('Aluminiumrohre: <b>Hebelteile</b>. Akkuzellen: <b>strategische Teile</b>. Büromaterial: <b>unkritische Teile</b>. Display-Controller: <b>Engpassteile</b>.')),
    teil('Nennen Sie für jedes Feld eine Normstrategie mit konkreter Maßnahme.', 6, 'K, Z, P, S.', 'Kosten, Zusammenarbeit, Prozess, Sicherstellung.',
         eh('Rohre (K): Wettbewerb ausnutzen, Auktion/Global Sourcing. Akkuzellen (Z): langfristige Partnerschaft, Lieferantenintegration, Risikomanagement. Büromaterial (P): Katalog/Dienstleister, Prozesskosten senken, bündeln. Controller (S): Sicherheitsbestand, Second Source aufbauen, Spezifikation auf Standardchip ändern.')),
    teil('Wie kann der Display-Controller zum Hebelteil werden? Und warum reicht das Portfolio allein nicht?', 4, 'Engpass eliminieren.', 'Machtverhältnisse.',
         eh('Durch Änderung der Spezifikation auf einen Standardchip bzw. Qualifizierung weiterer Lieferanten; dann konkurrieren mehrere Anbieter. Das Portfolio muss mit der eigenen Marktposition (Einkaufsvolumen, Bündelung, Substitution, Five Forces) kombiniert werden: Ein kleiner Kunde hat auch bei „Hebelteilen“ wenig Macht.'))])

# ---------------------------------------------------------------- 7 Einstandspreis / TCO
lp, zu_, rab, sk, fr, vp, vs, zo = 1200, 52, 0.02, 0.03, 26, 12.5, 5.2, 0
ber = (lp + zu_) * (1 - rab); ein = ber * (1 - sk) + fr + vp + vs + zo
assert round(ein, 2) == 1233.85
aufgabe('einstandspreis', ['tco', 'incoterms'], 'rechnen', 2, 'Einstandspreis und TCO-Gedanke',
    '<p>Ein Lieferant bietet ein Bauteil für <b>1.200 €</b> netto an. Wegen der kleinen Menge kommt ein Mindermengenzuschlag von <b>52 €</b> dazu. Sie erhalten <b>2 % Kundenrabatt</b> und <b>3 % Skonto</b>. Fracht 26 €, Verpackung 12,50 €, Versicherung 5,20 €, Zoll 0 €.</p>', [
    teil('Berechnen Sie den bereinigten Einkaufspreis.', 2, '(Angebot + Zuschlag) − Rabatt.', '2 % von 1.252 €.', eh(f'1.252 − 25,04 = <b>{de(ber)} €</b>.'), ber, '€', 0.02),
    teil('Berechnen Sie den Einstandspreis.', 3, 'Skonto auf den bereinigten Einkaufspreis, dann Bezugsnebenkosten addieren.', '3 % von 1.226,96 € = 36,81 €.',
         eh(f'1.226,96 − 36,81 + 26 + 12,50 + 5,20 + 0 = <b>{de(ein)} €</b>.'), ein, '€', 0.02),
    teil('Unterscheiden Sie Rabatt, Bonus und Skonto.', 3, 'Wann wird der Nachlass gewährt?', 'sofort, nachträglich, bei schneller Zahlung.',
         eh('Rabatt: sofortiger Preisnachlass (z. B. Mengen- oder Kundenrabatt). Bonus: nachträglich gewährter Nachlass (z. B. nach Jahresumsatz). Skonto: Abzug bei Zahlung innerhalb einer bestimmten Frist.')),
    teil('Ein zweiter Lieferant in Asien bietet 980 € EXW an. Warum sind die Angebote so nicht vergleichbar? Nennen Sie vier weitere TCO-Bestandteile.', 4, 'Was bedeutet EXW?', 'Landed Cost, Risiken.',
         eh('EXW heißt ab Werk: Transport, Versicherung, Ausfuhr, Einfuhrzoll und Risiko trägt der Käufer; diese Kosten fehlen im Preis. Weitere TCO-Bestandteile: Fracht und Versicherung, Zölle, Währungs- und Währungssicherungskosten, Kapitalbindung durch lange Transportzeit, Qualitätskosten, Lieferantenauditierung/Reisekosten, Bezugsrisiken (Länderrisiko).'))])

# ---------------------------------------------------------------- 8 Zuschlagskalkulation
mek, mgk, fl1, fgk1, fl2, fgk2 = 50, 0.08, 5, 1.0, 6, 1.5
mk = mek * (1 + mgk); fk = fl1 * (1 + fgk1) + fl2 * (1 + fgk2); hk = mk + fk; sk_ = hk * 1.16; vk = sk_ * 1.1
assert round(hk, 2) == 79 and round(sk_, 2) == 91.64 and round(vk, 2) == 100.80
aufgabe('zuschlagskalkulation', ['ksa'], 'rechnen', 2, 'Kostenstrukturanalyse: Was darf das Teil kosten?',
    '<p>Ein Lieferant verlangt für ein Gehäuse 112 €. Sie kalkulieren nach: Materialeinzelkosten 50 €, Materialgemeinkosten 8 %; Fertigungslohn Kostenstelle 1: 5 € mit 100 % FGK, Kostenstelle 2: 6 € mit 150 % FGK; Verwaltungs-GK 9 %, Vertriebs-GK 6 %, Wagnis 1 % (je auf Herstellkosten); Gewinn 10 % auf Selbstkosten.</p>', [
    teil('Berechnen Sie die Herstellkosten.', 3, 'Materialkosten + Fertigungskosten.', 'MK = 54; FK = 10 + 15.', eh('MK = 50 + 4 = 54 €; FK = (5 + 5) + (6 + 9) = 25 €; HK = <b>79 €</b>.'), hk, '€'),
    teil('Berechnen Sie Selbstkosten und Verkaufspreis ab Werk.', 3, 'Zuschläge auf HK: 9 + 6 + 1 %.', 'Gewinn auf Selbstkosten.',
         eh('SK = 79 + 7,11 + 4,74 + 0,79 = 91,64 €; Verkaufspreis = 91,64 + 9,16 = <b>100,80 €</b>.'), vk, '€', 0.02),
    teil('Was folgt für die Verhandlung mit dem Lieferanten?', 2, 'Vergleichen Sie mit dem Angebot.', '112 € vs. 100,80 €.',
         eh('Das Angebot liegt rund 11,20 € (ca. 11 %) über der Nachkalkulation. Argument für die Verhandlung: Kostentreiber offenlegen lassen (Cost Break Down), Zuschläge und Materialpreise hinterfragen.')),
    teil('Nennen Sie die drei Stufen der Kostenrechnung mit ihrer Leitfrage.', 3, 'Eselsbrücke AST.', 'welche, wo, wofür.',
         eh('Kostenartenrechnung: Welche Kosten sind angefallen? Kostenstellenrechnung: Wo sind sie angefallen? Kostenträgerrechnung: Wofür sind sie angefallen?'))])

# ---------------------------------------------------------------- 9 Prognose
werte = [100, 103, 138, 114, 126, 98, 169, 144]
arith = sum(werte) / 8; gl6 = sum(werte[2:]) / 6; gew = sum(v * g for v, g in zip(werte[2:], [6, 9, 13, 18, 24, 30])) / 100
assert arith == 124 and gl6 == 131.5 and round(gew, 2) == 136.32
aufgabe('prognose', ['mittelwerte', 'exp-glaettung', 'methoden'], 'rechnen', 2, 'Bedarfsprognose für Bremsbeläge',
    '<p>Verbrauch Januar bis August: 100, 103, 138, 114, 126, 98, 169, 144 Stück.</p>', [
    teil('Prognostizieren Sie den September mit dem arithmetischen Mittelwert.', 2, 'Alle acht Werte.', 'Summe 992.', eh('992 / 8 = <b>124</b> Stück.'), arith, 'Stück'),
    teil('… mit dem gleitenden Mittelwert über 6 Perioden.', 2, 'März bis August.', 'Summe 789.', eh('789 / 6 = <b>131,5</b> Stück.'), gl6, 'Stück'),
    teil('… mit dem gewichteten gleitenden Mittelwert (Gewichte 6, 9, 13, 18, 24, 30 %).', 3, 'Neueste Periode mit 30 %.', 'Σ T·G / 100.', eh('(138·6 + 114·9 + 126·13 + 98·18 + 169·24 + 144·30) / 100 = <b>136,32</b> Stück.'), gew, 'Stück', 0.01),
    teil('Die alte Prognose für September war 130, verbraucht wurden 102. Neue Prognose mit exponentieller Glättung (α = 0,2)?', 2, 'V_neu = V_alt + α (T − V_alt).', '130 + 0,2 · (−28).',
         eh('130 + 0,2 · (102 − 130) = 130 − 5,6 = <b>124,4</b> Stück.'), 124.4, 'Stück'),
    teil('Für welche Materialien eignen sich solche stochastischen Verfahren, und wo stoßen sie an Grenzen?', 3, 'Kontinuität.', 'Krisen.',
         eh('Für Materialien mit kontinuierlichem Verbrauch, für die eine deterministische Ermittlung nicht möglich oder zu aufwendig ist (Hilfs-/Betriebsstoffe, C-Teile). Grenze: Sie sind immer unsicher und versagen bei Strukturbrüchen (z. B. Corona), weil die Vergangenheit dann nichts über die Zukunft sagt.'))])

# ---------------------------------------------------------------- 10 ROI-Hebel
aufgabe('roi-hebel', ['materialkosten-roi', 'lagerkosten'], 'rechnen', 2, 'Der Hebel des Einkaufs',
    '<p>Ein Unternehmen: Umsatz 200 Mio. €, Materialkosten 100 Mio. €, sonstige Kosten 85 Mio. €, betriebsnotwendiges Kapital 80 Mio. €. Durchschnittlicher Lagerwert 4,5 Mio. €, Lagerkostensatz 11 % pro Jahr.</p>', [
    teil('Berechnen Sie Umsatzrentabilität, Kapitalumschlag und ROI.', 3, 'Gewinn = 200 − 100 − 85.', 'ROI = UR × KU.', eh('Gewinn 15 Mio. €; UR = 7,5 %; KU = 2,5; ROI = <b>18,75 %</b>.'), 18.75, '%'),
    teil('Der Einkauf senkt die Materialkosten um 5 %. Neuer ROI?', 3, 'Material 95 Mio. €.', 'Gewinn 20 Mio. €.', eh('Gewinn 20 Mio. €, UR = 10 %, ROI = 10 % · 2,5 = <b>25 %</b>.'), 25, '%'),
    teil('Welchen Umsatz bräuchte man ohne Kostensenkung für 20 Mio. € Gewinn (Umsatzrentabilität 7,5 %)?', 2, '20 / 0,075.', '', eh('20 / 0,075 = <b>266,67 Mio. €</b>, also +33 %.'), 266.67, 'Mio. €', 0.02),
    teil('Berechnen Sie die jährlichen Lagerkosten.', 2, 'K_L = Ø Lagerwert · T · k_L.', '4,5 Mio. · 1 · 0,11.', eh('4,5 Mio. € · 1 · 0,11 = <b>495.000 €</b>.'), 495000, '€')])

# ---------------------------------------------------------------- 11 LPP-Fallstudie (Vorlesung: LPP als Basis für eine MG-Strategie)
TEILE = [('K01', 'A', 200, 38), ('K02', 'B', 300, 45), ('K03', 'A', 400, 70), ('K04', 'C', 500, 64), ('K05', 'B', 600, 74),
         ('K06', 'C', 700, 112), ('K07', 'A', 800, 92), ('K08', 'B', 900, 101), ('K09', 'C', 1000, 150), ('K10', 'A', 1100, 118)]
xs = [t[2] for t in TEILE]; ys = [t[3] for t in TEILE]; nn = len(TEILE)
mx_, my_ = sum(xs) / nn, sum(ys) / nn
b_ = sum((x - mx_) * (y - my_) for x, y in zip(xs, ys)) / sum((x - mx_) ** 2 for x in xs); a_ = my_ - b_ * mx_
abw = {t[0]: t[3] - (a_ + b_ * t[2]) for t in TEILE}
ueber = [k for k, v in abw.items() if v > 10]
assert ueber == ['K06', 'K09'], ueber
soll = {k: a_ + b_ * dict((t[0], t[2]) for t in TEILE)[k] for k in ueber}
sp = sum(abw[k] for k in ueber)
aufgabe('lpp-fall', ['lpp', 'einkaufsziele', 'swot-scoring'], 'transfer', 3, 'Fallstudie: LPP als Basis für eine Materialgruppenstrategie',
    '<p>Die Materialgruppe „Kunststoff-Spritzgussteile“ umfasst zehn Teile von drei Lieferanten (A, B, C). Kostentreiber ist das Teilegewicht (g), betrachtet wird der Preis je 100 Stück (€).</p>'
    + '<table><tr><th>Teil</th><th>Lieferant</th><th>Gewicht (g)</th><th>Preis/100 (€)</th></tr>' + ''.join(f'<tr><td>{k}</td><td>{l}</td><td>{x}</td><td>{y}</td></tr>' for k, l, x, y in TEILE) + '</table>'
    + f'<p>Die Regression über alle Teile ergibt die Durchschnittspreislinie <b>y = {de(a_)} + {de(b_, 4)} · x</b>.</p>', [
    teil('Analysieren Sie die Materialgruppe: Welche Teile liegen mehr als 10 € über der Durchschnittslinie, und was fällt bei den Lieferanten auf?', 4,
         'Setzen Sie das Gewicht in die Geradengleichung ein und vergleichen Sie mit dem Preis.', 'Schauen Sie, welcher Lieferant die auffälligen Teile liefert.',
         eh('Linienpreise: ' + ', '.join(f'{k}: {de(a_ + b_ * x)} € (Abweichung {de(abw[k])} €)' for k, l, x, y in TEILE) + '. Mehr als 10 € darüber: <b>' + ' und '.join(ueber) + '</b>, beide von <b>Lieferant C</b>. Lieferant A liegt durchgehend auf oder unter der Linie (wettbewerbsfähig).')),
    teil('Wie hoch ist das rechnerische Einsparpotenzial je 100 Stück, wenn die auffälligen Teile auf den Linienpreis gesenkt werden?', 2, 'Summe der Abweichungen der auffälligen Teile.', 'Nur die Teile über der Linie zählen.',
         eh(' + '.join(f'{de(abw[k])}' for k in ueber) + f' = <b>{de(sp)} €</b> je 100 Stück (Basis Durchschnittslinie; mit der Best-Practice-Linie wäre das Potenzial noch größer).'), sp, '€', 0.05),
    teil('Definieren Sie zwei strategische Ziele für die Materialgruppe (Zieldreieck beachten).', 3, 'Kosten, Qualität, Lieferleistung.', 'Ziele messbar formulieren.',
         eh('z. B. <b>Kosten</b>: Preise aller Teile höchstens auf Durchschnittslinie, mittelfristig Richtung Best-Practice-Linie; <b>Lieferantenbasis</b>: von drei auf zwei Lieferanten bündeln; <b>Lieferleistung/Qualität</b> trotz Wechsel halten (Termintreue, Gutteile). Ausbalancierung des Zieldreiecks beachten.')),
    teil('Leiten Sie Maßnahmen ab und bewerten Sie sie kurz.', 4, 'Was tun Sie mit Lieferant C, was mit Lieferant A?', 'Denken Sie an Nachverhandlung, Bündelung, KSA.',
         eh('<b>Nachverhandlung</b> mit C mit den LPP-Daten als Argument (schnell, geringer Aufwand); bei Scheitern <b>Verlagerung</b> von K06 und K09 zu A (Bündelung, Volumen für A steigt, Wechselkosten und Werkzeuge beachten); für die auffälligen Teile eine <b>KSA</b> als Detailanalyse (LPP = Screening, KSA = Detail); Ergebnisse in einer Präsentation zusammenfassen, Umsetzung mit Verantwortlichen und Terminen planen, Controlling über die Strategieüberprüfung.'))])

ids = {t['id'] for k in json.loads((ROOT / 'inhalte/mawi/fach.json').read_text())['kapitel'] for t in k['themen']}
for a in A:
    for u in a['unter']:
        assert u in ids, (a['id'], u)
(ROOT / 'inhalte/mawi/aufgaben.json').write_text(json.dumps({'hinweis': 'Große Aufgaben im Klausurstil, Zahlen in Python nachgerechnet.', 'aufgaben': A}, ensure_ascii=False, indent=1) + '\n')
print(f'mawi: {len(A)} Aufgaben, {sum(len(a["teile"]) for a in A)} Teilaufgaben')
