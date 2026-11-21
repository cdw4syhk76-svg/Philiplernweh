import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *

# ---------------------------------------------------------------- Sägezahn-Simulation für die vier Bestellpolitiken
MAXB, MELDE, SB, Q, INTERVALL, TW = 84, 46, 26, 48, 7.0, 2.5
RATEN = [6.5, 8.0, 5.0, 7.5, 6.0, 8.5, 5.5]          # Verbrauch je Zeiteinheit, wechselt jede Zeiteinheit


def simulieren(politik, ende=26.0, dt=0.05):
    b, t, pts, bestellt, ankunft, offen = 62.0, 0.0, [], [], [], []
    naechste = 2.0
    while t <= ende + 1e-9:
        for a, m in list(offen):
            if t >= a - 1e-9:
                ankunft.append((t, b, b + m)); b += m; offen.remove((a, m)); pts.append((t, b - m)); pts.append((t, b))
        if politik in ('tq', 'tS') and t >= naechste - 1e-9:
            m = Q if politik == 'tq' else round(MAXB - b + 6.4 * TW)
            bestellt.append((t, b, m)); offen.append((t + TW, m)); naechste += INTERVALL
        if politik in ('sq', 'sS') and b <= MELDE and not offen:
            m = Q if politik == 'sq' else round(MAXB - b + 6.4 * TW)
            bestellt.append((t, b, m)); offen.append((t + TW, m))
        pts.append((t, b))
        b -= RATEN[int(t) % len(RATEN)] * dt
        t += dt
    return pts, bestellt, ankunft


def saege(politik, titel):
    X = lambda t: 44 + t * 8.6
    Y = lambda v: 222 - v * 2.2
    pts, best, ank = simulieren(politik)
    assert max(v for _, v in pts) <= 92 and min(v for _, v in pts) >= 0, (politik, max(v for _, v in pts), min(v for _, v in pts))
    s = rechteck(44, Y(SB), 228, Y(0) - Y(SB), 'var(--pale)', 'var(--line)', 0)
    s += tpg(T(276, Y(SB) + 18, 'Sicherheits-\nbestand', 12, 600, 'start', 'var(--muted)'), 'Sicherheitsbestand (eiserner Bestand): Puffer gegen Fehlmengen, wird im Normalfall nicht angegriffen.')
    s += achsen(44, 222, 272, 16, '', 'Lagerbestand') + T(276, 226, 'Zeit', 12, 600, 'start', 'var(--muted)')
    if politik in ('tS', 'sS'):
        s += tpg(strich(44, Y(MAXB), 272, Y(MAXB), 'var(--primary-2)', 1.4) + T(276, Y(MAXB) + 4, 'Soll-Lager-\nbestand S', 12, 700, 'start', 'var(--primary-2)'), 'Soll-Lagerbestand S: Bis zu diesem Niveau wird bei jeder Bestellung aufgefüllt; die Bestellmenge ist deshalb variabel.')
    if politik in ('sq', 'sS'):
        s += tpg(strich(44, Y(MELDE), 272, Y(MELDE), 'var(--axis)', 1.4) + T(276, Y(MELDE) + 4, 'Melde-\nbestand', 12, 700, 'start'), 'Meldebestand (Bestellpunkt): Wird er erreicht, wird bestellt. Er deckt den Verbrauch während der Wiederbeschaffungszeit plus Sicherheitsbestand.')
    s += linie([(X(t), Y(v)) for t, v in pts], 'var(--primary)', 2.4)
    for i, (t, b, m) in enumerate(best[:3]):
        s += tpg(f'<polygon points="{X(t):.1f},{Y(b) + 4:.1f} {X(t) - 6:.1f},{Y(b) + 15:.1f} {X(t) + 6:.1f},{Y(b) + 15:.1f}" style="fill:var(--axis)"/>'
                 + T(X(t), Y(b) + 29, f't{i + 1}', 12, 700),
                 f'Bestellzeitpunkt t{i + 1}: Bestand {b:.0f}, bestellt werden {m:.0f} Stück. ' + ('Der Zeitpunkt ist fest (Rhythmus).' if politik[0] == 't' else 'Ausgelöst, weil der Meldebestand erreicht wurde; der Zeitpunkt ist variabel.'))
        s += tpg(strich(X(t), 236, X(t + TW), 236, 'var(--axis)', 2, False) + strich(X(t), 231, X(t), 241, 'var(--axis)', 1.4, False) + strich(X(t + TW), 231, X(t + TW), 241, 'var(--axis)', 1.4, False)
                 + T(X(t + TW / 2), 252, 'Tw', 12, 700, fill='var(--muted)'),
                 'Tw = Wiederbeschaffungszeit: Dauer zwischen Auslösen der Bestellung und Bereitstehen der Ware.')
    for i, (t, v0, v1) in enumerate(ank[:3]):
        s += tpg(T(X(t) + 5, Y(v0 + 0.72 * (v1 - v0)) + 4, f'q{i + 1}' if politik[1] == 'S' else 'q', 12, 700, 'start', 'var(--primary)'),
                 f'Wareneingang: {v1 - v0:.0f} Stück. ' + ('Variable Menge: aufgefüllt in Richtung S.' if politik[1] == 'S' else 'Immer dieselbe Bestellmenge q.'))
    s += T(354, 12, titel, 12, 800, 'end')
    s += tpg(T(276, 60, 'Bestand\nzu Beginn\nder Grafik', 12, 400, 'start', 'var(--muted)'), 'Die Linie zeigt den Lagerbestand: Er sinkt mit dem Verbrauch und springt beim Wareneingang um die Liefermenge nach oben.') if False else ''
    return svg(360, 258, s, titel, maxw=420)


TAFEL_BEST = tafeln('tf-best', ['(t,q)', '(t,S)', '(s,q)', '(s,S)'], [
    saege('tq', 'Bestellrhythmus, feste Menge'), saege('tS', 'Bestellrhythmus, auf S auffüllen'),
    saege('sq', 'Bestellpunkt, feste Menge'), saege('sS', 'Bestellpunkt, auf S auffüllen')])

# ---------------------------------------------------------------- 1 Bestände, Lagerfunktionen, Lagerarten
fig_best = svg(360, 232,
    box(4, 8, 168, 148, 'Bestände ermöglichen\n\nreibungslose Produktion\nprompte Lieferung\nÜberbrückung von\nStörungen\nwirtschaftliche Fertigung\nkonstante Auslastung', size=12, tip='Die positive Seite: Bestände sorgen für Versorgungssicherheit und gleichmäßige Abläufe.')
    + box(188, 8, 168, 148, 'Bestände verdecken\n\nstöranfällige Prozesse\nunabgestimmte\nKapazitäten\nmangelnde Flexibilität\nAusschuss\nmangelnde Liefertreue', size=12, art='hl', tip='Die negative Seite: Hohe Bestände wirken wie Wasser über Felsen. Probleme bleiben unsichtbar, bis der Bestand sinkt.')
    + tpg(f'<polygon points="200,226 214,196 228,214 246,190 262,212 280,194 300,216 318,198 336,212 350,226" style="fill:var(--axis2)"/>'
          + f'<rect x="196" y="176" width="158" height="50" style="fill:var(--primary-2);opacity:0.35"/>'
          + strich(196, 176, 354, 176, 'var(--primary)', 2, False), 'Hoher Bestand ist wie hoher Wasserstand: Die Felsen (Probleme) bleiben unter der Oberfläche. Senkt man den Bestand, werden sie sichtbar.')
    + T(352, 170, 'hoher Bestand', 12, 600, 'end', 'var(--muted)')
    + tpg(f'<polygon points="22,226 36,196 50,214 68,190 84,212 102,194 122,216 140,198 158,212 172,226" style="fill:var(--axis2)"/>'
          + f'<rect x="18" y="206" width="158" height="20" style="fill:var(--primary-2);opacity:0.35"/>'
          + strich(18, 206, 176, 206, 'var(--primary)', 2, False), 'Niedriger Bestand: Die Probleme ragen heraus und müssen gelöst werden.')
    + T(20, 180, 'niedriger Bestand:\nProbleme sichtbar', 12, 600, 'start', 'var(--muted)'),
    'Bestandsfunktionen', maxw=420)

t_bestand = thema('bestaende-lager', 'Bestände, Lagerfunktionen, Lagerarten',
    kern='Bestände ermöglichen reibungslose Produktion, prompte Lieferung, Überbrückung von Störungen, wirtschaftliche Fertigung und konstante Auslastung, verdecken aber störanfällige Prozesse, unabgestimmte Kapazitäten, mangelnde Flexibilität, Ausschuss und mangelnde Liefertreue. Lagerfunktionen: Mengenausgleich, Sicherung, Puffer, Spekulation, Umformung/Veredelung. Lagerarten: Block-, Fachboden-, Verschiebe-, Umlauf-, Hochregal-, Paletten-, Schüttgut-, Tank- und Durchlaufregallager.',
    kurz=p('Ein volles Lager bei der Neckarrad GmbH fühlt sich sicher an: Die Montage steht nie still. Aber es <b>versteckt</b> auch Probleme. Wenn ein Lieferant ständig zu spät kommt, merkt es niemand, solange genug Akkus im Regal liegen.')
        + p('Bild dazu: Bestände sind wie Wasser, das Felsen bedeckt. Senkt man den Wasserstand, tauchen die Felsen auf: störanfällige Prozesse, Ausschuss, unzuverlässige Lieferanten.'),
    fig=fw('Zwei Seiten der Bestände. Tippe auf die Kästen.') + bild(fig_best),
    figcap='nach Folie „Bestandsfunktionen“ (Schulte)',
    article=h3('Nettobedarf als Ausgangspunkt')
        + p('Der Nettobedarf wird zum Ausgangspunkt der Beschaffungsaktivitäten: Er führt zur Bestellanforderung an den Einkauf und startet die Einkaufsaktivitäten.')
        + h3('Bestandsfunktionen')
        + tabelle(['Bestände ermöglichen', 'Bestände verdecken'], [['reibungslose Produktion', 'störanfällige Prozesse'], ['prompte Lieferung', 'unabgestimmte Kapazitäten'],
                                                                 ['Überbrückung von Störungen', 'mangelnde Flexibilität'], ['wirtschaftliche Fertigung', 'Ausschuss'], ['konstante Auslastung', 'mangelnde Liefertreue']])
        + h3('Lagerfunktionen (Auswahl)')
        + tabelle(['Funktion', 'Bedeutung', 'Beispiel'], [
            ['Mengenausgleichsfunktion', 'Beschaffungsmenge höher als in der Produktion unmittelbar benötigt', 'Mindestbestellmengen: Mehl gibt es nur in 1-kg-Säcken, gebraucht werden 397 g'],
            ['Sicherungsfunktion', 'Erhalt der Lieferfähigkeit bei ungeplanten Versorgungsengpässen', 'Sicherheitsbestand an Akkus'],
            ['Pufferfunktion', 'Ausgleich von Bedarfsschwankungen oder Produktionsengpässen', 'Zwischenlager vor der Lackiererei'],
            ['Spekulationsfunktion', 'günstige Beschaffungszeitpunkte bei starken Preisschwankungen ausnutzen', 'Kupfer kaufen, wenn der Preis niedrig ist'],
            ['Umformungs- und Veredelungsfunktion', 'auch Produktionsfunktion: Produkte „reifen“ im Lager', 'Wein, Käse; manches muss z. B. mindestens drei Jahre gelagert werden']])
        + h3('Lagerarten (Auswahl)')
        + tabelle(['Lagerart', 'Merkmal'], [
            ['Blocklager', 'statische Bodenlagerung für Stückgut mit und ohne Ladehilfsmittel'], ['Fachbodenregal', 'statische Regallagerung für Stückgut'],
            ['Verschieberegal', 'dynamisch: bewegte Regalzeilen'], ['Umlaufregal (horizontal/vertikal)', 'dynamisch: Regale laufen horizontal oder vertikal um'],
            ['Hochregallager', 'statische Regallagerung mit Ladehilfsmitteln, meist automatisch'], ['Palettenregallager', 'statische Lagerung auf Paletten (z. B. mit Gabelstapler)'],
            ['Schüttgutlager', 'Sand, Steine, Erde, Beton in Containern oder Lagerbuchten'], ['Tanklager', 'Flüssiggüter'],
            ['Durchlaufregallager', 'Einlagerung auf einer, Auslagerung auf der gegenüberliegenden Seite (Schwerkraft oder mechanisch); stellt FIFO sicher']])
        + spiel('sp-lagerfkt', 'Welche Lagerfunktion?', ['Mengenausgleich', 'Sicherung', 'Puffer', 'Spekulation', 'Veredelung'], [
            ('Schrauben gibt es nur in 10.000er-Kartons, gebraucht werden 3.200', 0, 'Mindestbestellmenge.'), ('Reserve-Akkus für den Fall eines Lieferausfalls', 1, 'Lieferfähigkeit bei Engpässen.'),
            ('Lager zwischen Rahmenbau und Montage gleicht Taktunterschiede aus', 2, 'Produktionsengpässe ausgleichen.'), ('Aluminium vor der erwarteten Preiserhöhung einkaufen', 3, 'Preisschwankungen ausnutzen.'),
            ('Whisky reift im Fass', 4, 'Produkt reift im Lager.')]),
    merk='Bestände ermöglichen (reibungslose Produktion, prompte Lieferung, Störungen überbrücken, wirtschaftliche Fertigung, konstante Auslastung) und verdecken (störanfällige Prozesse, unabgestimmte Kapazitäten, mangelnde Flexibilität, Ausschuss, mangelnde Liefertreue). Lagerfunktionen: Mengenausgleich, Sicherung, Puffer, Spekulation, Umformung/Veredelung. Durchlaufregal = FIFO.',
    exam='Bestands- und Lagerfunktionen nennen und Beispielen zuordnen.',
    fehler=['Puffer- und Sicherungsfunktion verwechseln: Puffer gleicht geplante Schwankungen aus, Sicherung schützt vor ungeplanten Engpässen.'],
    src='Folien 59–62')

# ---------------------------------------------------------------- 2 Lagerkennzahlen
t_kennz = thema('lagerkennzahlen', 'Lagerwirtschaftliche Kennzahlen',
    kern='Durchschnittlicher Lagerbestand = (Anfangsbestand + Endbestand) / 2. Lagerumschlagshäufigkeit = Wareneinsatz / Ø Lagerbestand (hoch ist gut). Lagerreichweite = Ø Lagerbestand × 365 / Jahresverbrauch. Lagerkostensatz = Lagerkosten × 100 / Ø Lagerbestand. Kapitalbindung = Ø Lagerbestand × Einkaufspreis. Lieferbereitschaftsgrad = ausgelieferte / bestellte Menge, ideal 97–98 %.',
    kurz=p('Wie gut wirtschaftet das Akkulager der Neckarrad GmbH? Ein paar Kennzahlen sagen es: Wie oft dreht sich der Bestand im Jahr um (<b>Umschlagshäufigkeit</b>)? Wie lange reicht er (<b>Reichweite</b>)? Wie viel Geld steckt darin (<b>Kapitalbindung</b>)?')
        + p('Und: Wie oft konnte die Montage sofort beliefert werden (<b>Lieferbereitschaftsgrad</b>)? Zu niedrig gibt Ärger mit den Kunden, zu hoch deutet auf zu viel Bestand: ideal sind etwa 97–98 %.'),
    fig=fw('Kennzahlen rechnen. Verschiebe die Regler.')
        + regler([('kzA', 'Anfangsbestand', 0, 2000, 50, 800, 'Stück'), ('kzE', 'Endbestand', 0, 2000, 50, 400, 'Stück'), ('kzV', 'Jahresverbrauch', 1000, 20000, 500, 7200, 'Stück'), ('kzP', 'Einkaufspreis', 10, 500, 10, 250, '€')])
        + schritte_karten([('① Ø Lagerbestand', 'kz1', '#kz1t'), ('② Umschlag', 'kz2', '#kz2t'), ('③ Reichweite', 'kz3', '#kz3t'), ('④ Kapitalbindung', 'kz4', '#kz4t')]),
    figcap='nach Folie „Wichtige lagerwirtschaftliche Kennzahlen“',
    article=h3('Die Kennzahlen')
        + tabelle(['Kennzahl', 'Berechnung', 'Aussage'], [
            ['durchschnittlicher Lagerbestand', r'\(\frac{\text{Anfangsbestand} + \text{Endbestand}}{2}\)', 'durchschnittlich vorhandene Warenmenge im Lager'],
            ['Lagerumschlagshäufigkeit', r'\(\frac{\text{Wareneinsatz}}{\varnothing\,\text{Lagerbestand}}\)', 'wie oft der Ø Bestand in einem Zeitraum umgeschlagen wird; hoch ist gut'],
            ['Lagerreichweite', r'\(\frac{\varnothing\,\text{Lagerbestand} \cdot 365}{\text{Jahresverbrauch}}\)', 'wie lange der Bestand bei gleichbleibendem Verbrauch reicht (Tage)'],
            ['Lagerkostensatz', r'\(\frac{\text{Lagerkosten} \cdot 100}{\varnothing\,\text{Lagerbestand}}\)', 'Lagerkosten im Verhältnis zum Ø Bestand (%)'],
            ['Kapitalbindung im Lager', r'\(\varnothing\,\text{Lagerbestand} \cdot \text{Einkaufspreis}\)', 'wie viel Kapital im Bestand gebunden ist'],
            ['Lieferbereitschaftsgrad', r'\(\frac{\text{ausgelieferte Menge}}{\text{bestellte (benötigte) Menge}}\)', 'Maß der Lieferbereitschaft in einem Zeitraum']])
        + h3('Lieferbereitschaftsgrad: nicht zu hoch, nicht zu niedrig')
        + p('<b>Ein niedriger Lieferbereitschaftsgrad führt zu Auftragsverlusten und Produktionsstillstand. Ein sehr hoher Lieferbereitschaftsgrad kann auf einen (zu) hohen Lagerbestand hinweisen.</b> Ideal sind etwa 97–98 %. Zu niedrig: Ärger mit den Kunden; zu hoch: Ärger mit der Produktion bzw. dem Controlling wegen der Kapitalbindung.')
        + bsp('Akkulager', 'Anfangsbestand 800, Endbestand 400, Jahresverbrauch 7.200 Stück, Preis 250 €', [
            ('Ø Lagerbestand', '(800 + 400) / 2 = 600 Stück'), ('Umschlagshäufigkeit', '7.200 / 600 = 12-mal im Jahr'), ('Reichweite', '600 · 365 / 7.200 ≈ 30,4 Tage'), ('Kapitalbindung', '600 · 250 € = 150.000 €')],
            'Umschlagshäufigkeit und Reichweite hängen zusammen: Reichweite = 365 / Umschlagshäufigkeit.')
        + falle('Bei der Umschlagshäufigkeit „niedrig ist gut“ denken. Ein hoher Umschlag heißt: wenig Bestand im Verhältnis zum Verbrauch, also wenig gebundenes Kapital.'),
    merk='Ø Bestand = (AB + EB)/2. Umschlag = Wareneinsatz / Ø Bestand (hoch = gut). Reichweite = Ø Bestand · 365 / Jahresverbrauch = 365 / Umschlag. Lagerkostensatz = Lagerkosten · 100 / Ø Bestand. Kapitalbindung = Ø Bestand · Preis. Lieferbereitschaftsgrad = ausgeliefert / bestellt, ideal 97–98 %.',
    exam='Kennzahlen berechnen und interpretieren; Lieferbereitschaftsgrad zu hoch oder zu niedrig?',
    fehler=['Reichweite mit Umschlagshäufigkeit verwechseln.', 'Mit dem Endbestand statt dem Durchschnitt rechnen.'],
    src='Folie 63')

# ---------------------------------------------------------------- 3 Sicherheitsbestand, WBZ, Meldebestand
t_begriffe = thema('bestellbegriffe', 'Sicherheitsbestand, Wiederbeschaffungszeit, Meldebestand', star=True,
    kern='Sicherheitsbestand (eiserner Bestand): Puffer gegen Fehlmengen, z. B. Ø Verbrauch je Periode × Wiederbeschaffungszeit. Wiederbeschaffungszeit: Dauer zwischen Auslösen der Bestellung und Bereitstehen der Ware. Meldebestand: Bestandshöhe, bei der die Bestellung ausgelöst wird, meist Verbrauch je Periode × Wiederbeschaffungszeit + Sicherheitsbestand.',
    kurz=p('Die Montage braucht im Schnitt 120 Akkus im Monat; vom Bestellen bis zum Eintreffen vergehen 0,5 Monate. Damit es nicht eng wird, soll immer ein Puffer von 180 Akkus da sein (<b>Sicherheitsbestand</b>).')
        + p('Wann muss man bestellen? Wenn der Bestand so weit gesunken ist, dass er gerade noch die Wartezeit plus Puffer abdeckt: 120 · 0,5 + 180 = <b>240 Akkus</b>. Das ist der <b>Meldebestand</b>.'),
    fig=fw('Die Begriffe im Lagerbestandsverlauf. Tippe auf Linien und Markierungen.') + bild(saege('sq', 'Lagerbestandsverlauf und Begriffe')),
    figcap='nach Folie „Überblick und wichtige Begriffe“',
    article=h3('Sicherheitsbestand')
        + p('<b>Sicherheitsbestand (eiserner Bestand, Mindestbestand, Reservebestand): der Bestand an Material, der im Allgemeinen nicht in der Fertigung eingesetzt wird, aber in Sondersituationen, zur Vermeidung von Fehlmengen oder bei Lieferschwierigkeiten der Lieferanten doch zum Einsatz kommt.</b> Er ist ein Puffer gegen Fehlmengen (Zusatzbedarf bei Schwund, Qualitätsmängeln, außerplanmäßigem Mehrbedarf).')
        + p('Er richtet sich nach Wiederbeschaffungszeit, Bedeutung, Wert und Planbarkeit des Teils sowie der Belieferungsstrategie. Berechnung (auf Basis des Durchschnittsverbrauchs):')
        + liste(['a) Ø Verbrauch pro Periode × Wiederbeschaffungszeit, z. B. 20 Stück × 1,5 Monate = 30 Stück; Folienbeispiel: 120 × 1,5 = 180', 'b) Faustformel: Prozentsatz des Ø Lagerbestands (Erfahrung), z. B. 20 % von 600 = 120'])
        + h3('Wiederbeschaffungszeit (Tw)')
        + p('<b>„Dauer, die zwischen dem Auslösen einer Bestellung und dem Zeitpunkt liegt, an dem die bestellte Ware zur Befriedigung der Kundennachfrage bereitsteht.“</b> Sie hängt ab von: Bearbeitung der Bestellung, Auftragsbearbeitung beim Lieferanten, Produktion beim Lieferanten, Transport, Wareneingangsprüfung, Produktionsversorgung/Einlagerung.')
        + h3('Meldebestand')
        + p('<b>Festgelegte Bestandshöhe, bei der durch den Disponenten (Einkauf) die Teilebestellung beim Lieferanten ausgelöst wird.</b> Die Bestellung erfolgt automatisch, schriftlich, (fern)mündlich, via Intra- oder Internet. Zu berücksichtigen sind Bestellabwicklung, Produktion beim Lieferanten, Transport, Wareneingang, Qualitätsprüfung und Einlagerung.')
        + fx('Meldebestand (Formel 1)', r'MB = \text{Verbrauch je Periode} \cdot T_w + SB', 'deckt den Verbrauch während der Wiederbeschaffungszeit plus Sicherheitsbestand', r'\(120 \cdot 0{,}5 + 180 = 240\)')
        + p('Alternative Formeln: 2. <b>2 × Sicherheitsbestand</b> (360), 3. Mindestbestellmenge + Sicherheitsbestand, 4. Faustformel: Prozentsatz des Ø Lagerbestands. Je kontinuierlicher der Verbrauch, desto besser funktioniert die Formel.')
        + tabelle(['Monat', 'Verbrauch', 'Tw', 'SB', 'MB Formel 1', 'MB Formel 2'], [
            ['Dezember', '120', '0,5', '180', '240', '360'], ['Januar', '127', '0,5', '190', '254', '380'], ['März', '108', '0,5', '162', '216', '324']])
        + h3('Weitere Begriffe im Bild')
        + liste(['<b>Maximaler Lagerbestand</b>: Höchststand direkt nach dem Wareneingang (Sicherheitsbestand + Bestellmenge).', '<b>Durchschnittlicher Lagerbestand</b>: bei gleichmäßigem Abgang Sicherheitsbestand + Bestellmenge / 2.', '<b>Bestellzeitpunkt</b>: Zeitpunkt, an dem bestellt wird; die Ware kommt eine Wiederbeschaffungszeit später.'])
        + falle('Den Meldebestand mit dem Sicherheitsbestand gleichsetzen. Bestellt wird schon beim Meldebestand, damit der Sicherheitsbestand nicht angegriffen wird.'),
    merk='SB: Puffer gegen Fehlmengen; Ø Verbrauch × Tw (120 × 1,5 = 180) oder % vom Ø Bestand. Tw: Auslösen der Bestellung bis Ware bereitsteht (Bestellung, Lieferant, Produktion, Transport, Prüfung, Einlagerung). Meldebestand: löst Bestellung aus; Verbrauch × Tw + SB (120 × 0,5 + 180 = 240); Alternativen: 2 × SB, Mindestbestellmenge + SB, Faustformel.',
    exam='Begriffe in der Sägezahn-Abbildung eintragen; Meldebestand und Sicherheitsbestand berechnen.',
    fehler=['Meldebestand ohne Sicherheitsbestand rechnen.', 'Wiederbeschaffungszeit nur als Transportzeit verstehen.'],
    src='Folien 64–69')

# ---------------------------------------------------------------- 4 Bestellsysteme
t_systeme = thema('bestellsysteme', 'Bestellrhythmus- und Bestellpunktverfahren', star=True,
    kern='Bestellrhythmusverfahren (terminorientiert): Bestellung zu festen Terminen; (t,q) mit fester Menge, (t,S) mit Auffüllen bis zum Soll-Lagerbestand S; geeignet für gleichmäßigen Bedarf. Bestellpunktverfahren (mengenorientiert): Bestellung, wenn der Meldebestand erreicht ist, Zeitpunkt variabel; Bestellpunkt-Losgrößen-Verfahren mit fester Menge, Lagerniveau-Verfahren mit Auffüllen auf S; geeignet für schwankenden Bedarf. Beide sind verbrauchsorientiert.',
    kurz=p('Zwei Grundfragen: <b>Wann</b> bestelle ich, und <b>wie viel</b>? Beim <b>Bestellrhythmusverfahren</b> ist das Wann fest: immer am Monatsanfang. Beim <b>Bestellpunktverfahren</b> bestellt man, sobald der Meldebestand erreicht ist, das Wann ist also variabel.')
        + p('Bei der Menge gibt es wieder zwei Möglichkeiten: <b>immer gleich viel</b> (q) oder <b>auffüllen bis zum Soll-Lagerbestand S</b>. Macht zusammen vier Verfahren. Laut Vorlesung müssen alle bekannt sein.'),
    fig=fw('Vier Bestellpolitiken. Schalte um und tippe auf Bestellzeitpunkte, Linien und Tw.') + TAFEL_BEST,
    figcap='nach Folien „Bestellrhythmusverfahren“ und „Bestellpunktverfahren“',
    article=h3('Überblick')
        + tabelle(['', 'Bestellrhythmusverfahren', 'Bestellpunktverfahren'], [
            ['Auslöser', 'festgelegte Termine / Zeitintervalle (z. B. immer Anfang des Monats): <b>terminorientiert</b>', 'Lagerbestand erreicht den Meldebestand: <b>mengenorientiert</b>'],
            ['Merkmale', 'regelmäßige Bestellintervalle', 'verschiedene Bestellzeitpunkte, gleiche Bestellmengen (z. B. optimale Bestellmenge)'],
            ['geeignet für', 'gleichmäßigen Materialbedarf', 'ungleichmäßigen Materialbedarf']])
        + p('<b>Beide Verfahren gehören zu den verbrauchsorientierten Bestellverfahren.</b>')
        + h3('Die vier Varianten')
        + tabelle(['Verfahren', 'Zeitpunkt', 'Menge', 'Bild'], [
            ['Bestellrhythmusverfahren (t,q)', 'konstant (t0)', 'konstant (q0)', 'gleiche Abstände, gleich hohe Sprünge; Höchststand schwankt'],
            ['Bestellrhythmus-Lagerniveau-Politik (t,S)', 'konstant (t0)', 'variabel (qi): Auffüllen auf Soll-Lagerbestand S', 'gleiche Abstände, unterschiedlich hohe Sprünge, Linie S'],
            ['Bestellpunkt-Losgrößen-Verfahren (s,q)', 'variabel (ti), bei Meldebestand', 'konstant (q0)', 'Bestellung immer auf Höhe der Meldebestandslinie, gleich hohe Sprünge'],
            ['Bestellpunkt-Lagerniveau-Verfahren (s,S)', 'variabel (ti), bei Meldebestand', 'variabel (qi): Auffüllen auf S', 'Meldebestandslinie und Linie S']])
        + p('Die Kurzbezeichnungen (t,q) und (t,S) stehen so auf den Folien; (s,q) und (s,S) sind die übliche Schreibweise für die beiden Bestellpunktverfahren (s = Meldebestand bzw. Bestellpunkt).')
        + h3('Vor- und Nachteile')
        + procon('Bestellrhythmus (t,q): Vorteile', ['einfaches Verfahren, wenig Koordinationsaufwand', 'evtl. Sammelbestellungen, Mengenrabatte', 'Automatisierung des Bestellprozesses einfach'],
                 'Nachteile', ['unterschiedliche Verbräuche werden nicht berücksichtigt', 'bei schwankendem Verbrauch Versorgungsengpässe oder zu hohe Bestände und Lagerkosten'])
        + p('→ Geeignet für Güter mit konstanten (gleichmäßigen) Bedarfen bzw. sehr geringen Schwankungen. Variante (t,S): Lagerhöchstmenge auf S gedeckelt, schwankender Verbrauch wird zum Teil ausgeglichen; dafür erhöhter Koordinationsaufwand und Gefahr von Fehlbeständen und Fehlmengenkosten.')
        + procon('Bestellpunktverfahren: Vorteile', ['kurzfristige Bedarfsschwankungen können ausgeglichen werden', 'Mindestbestände können relativ gering gehalten werden', 'geringere Kapitalbindung durch niedrigere Bestände'],
                 'Nachteile', ['Lagerbestände müssen ständig kontrolliert werden', 'höhere Anforderungen und Aufwendungen für den Lagerbetrieb'])
        + p('→ Geeignet für Güter mit höheren Bedarfsschwankungen bei gleichzeitig höherem Lagerhaltungsaufwand.')
        + klausur_hinweis('Typische Aufgabe: eine Abbildung des Lagerbestandsverlaufs vervollständigen (Meldebestand, Sicherheitsbestand, Bestellmenge, Tw, Bestellzeitpunkte eintragen), das Verfahren benennen und die Wahl begründen. So erkennst du es: gleiche Abstände = Rhythmus; Bestellung immer auf derselben Bestandshöhe = Bestellpunkt; gleich hohe Sprünge = feste Menge; Auffüllen bis zu einer Linie = Lagerniveau (S).')
        + spiel('sp-best', 'Welches Verfahren?', ['(t,q)', '(t,S)', '(s,q)', '(s,S)'], [
            ('Jeden Montag werden 500 Schrauben bestellt.', 0, 'Fester Termin, feste Menge.'), ('Jeden Monatsersten wird das Regal bis 2.000 Stück aufgefüllt.', 1, 'Fester Termin, Auffüllen auf S.'),
            ('Fallen die Akkus unter 240, werden 400 nachbestellt.', 2, 'Meldebestand löst feste Menge aus.'), ('Fallen die Akkus unter 240, wird bis 900 aufgefüllt.', 3, 'Meldebestand, Auffüllen auf S.'),
            ('Optimale Bestellmenge wird immer dann bestellt, wenn der Meldebestand erreicht ist.', 2, 'Bestellpunkt-Losgrößen-Verfahren.')]),
    merk='Rhythmus = terminorientiert (feste Termine, gleichmäßiger Bedarf): (t,q) feste Menge, (t,S) auf Soll-Lagerbestand S auffüllen. Bestellpunkt = mengenorientiert (Meldebestand löst aus, Zeitpunkt variabel, schwankender Bedarf): (s,q) Bestellpunkt-Losgrößen-Verfahren, (s,S) Lagerniveau-Verfahren. Beide verbrauchsorientiert. Rhythmus: einfach, automatisierbar, aber unflexibel. Bestellpunkt: flexibel, niedrige Bestände, aber ständige Bestandskontrolle.',
    exam='Abbildung vervollständigen, Verfahren benennen und begründen; Vor- und Nachteile; für welchen Bedarf geeignet.',
    fehler=['Rhythmus und Bestellpunkt bei der Begründung vertauschen.', 'Beim Bestellpunktverfahren die Wiederbeschaffungszeit vergessen: Die Ware kommt erst Tw nach dem Meldebestand.'],
    src='Folien 70–76')

# ---------------------------------------------------------------- 5 Dilemma der optimalen Bestellmenge
M, KB, W, IL = 12, 150, 600, 0.15
XOPT = math.sqrt(2 * M * KB / (W * IL))
assert abs(XOPT - math.sqrt(40)) < 1e-9
K = lambda x: M / x * KB + x / 2 * W * IL
assert K(6) == 570 and round(K(7), 2) == 572.14

def kosten_svg():
    X = lambda x: 44 + x * 21.5
    Y = lambda y: 220 - y * 0.17
    s = achsen(44, 220, 354, 16, 'Bestellmenge x (t)', 'Kosten (€/Jahr)')
    for v in (400, 800):
        s += strich(44, Y(v), 340, Y(v), 'var(--line)', 1, True) + T(40, Y(v) + 4, str(v), 12, 400, 'end', 'var(--muted)')
    for x in (2, 4, 6, 8, 10, 12):
        s += T(X(x), 236, str(x), 12, 400, fill='var(--muted)')
    s += tpg(kurve(lambda x: M / x * KB, 1.6, 13.5, X, Y, farbe='var(--axis2)'), 'Bestellkosten K_B = m/x · k_b fallen mit steigender Bestellmenge (degressiv): weniger Bestellungen.')
    s += tpg(kurve(lambda x: x / 2 * W * IL, 0.3, 13.5, X, Y, farbe='var(--primary-2)'), 'Lagerkosten K_L = x/2 · w · i_L steigen linear: Der Ø Bestand ist x/2.')
    s += tpg(kurve(K, 1.6, 13.5, X, Y, farbe='var(--primary)', w=3), 'Gesamtkosten K = K_B + K_L; Minimum bei x_opt.')
    s += strich(X(XOPT), Y(K(XOPT)), X(XOPT), 220, 'var(--axis)', 1.4) + tpg(punkt(X(XOPT), Y(K(XOPT)), 'var(--primary)', 6) + punkt(X(XOPT), Y(K(XOPT) / 2), 'var(--axis)', 5),
        f'Optimum: x_opt = √40 ≈ 6,32 t. Hier schneiden sich Bestell- und Lagerkosten (je ≈ 285 €), und die Gesamtkosten sind minimal (≈ 569 €).')
    s += T(X(XOPT) + 6, 212, 'optimale Menge', 12, 700, 'start')
    s += T(X(13.4), Y(K(13.4)) - 8, 'Gesamtkosten', 12, 700, 'end', 'var(--primary)') + T(X(13.4), Y(13.4 / 2 * W * IL) + 18, 'Lagerkosten', 12, 700, 'end', 'var(--primary-2)') + T(X(13.4), Y(M / 13.4 * KB) - 6, 'Bestellkosten', 12, 700, 'end', 'var(--muted)')
    return svg(360, 248, s, 'Kostenverläufe der Bestellmenge', maxw=420)

t_dilemma = thema('losgroessen-dilemma', 'Das Dilemma der optimalen Bestellmenge', star=True,
    kern='Gesamtkosten = Bestellkosten + Lagerkosten: K(x) = K_B(x) + K_L(x). Große Bestellmengen senken die Bestellkosten (weniger Bestellungen, Rabatte, bestellfixe Kosten), kleine senken die Lagerkosten. Das Dilemma: Beide Kosten entwickeln sich gegenläufig. Im Andler-Modell liegt das Minimum der Gesamtkosten beim Schnittpunkt der Bestell- und Lagerkostenkurve.',
    kurz=p('Beispiel der Vorlesung: Ein Bonbonhersteller braucht 12 t Zucker im Jahr. Bestellt er alles auf einmal, zahlt er nur einmal 150 € Bestellkosten, hat aber im Schnitt 6 t im Lager. Bestellt er monatlich, ist das Lager fast leer, aber er zahlt zwölfmal Bestellkosten.')
        + p('Irgendwo dazwischen sind die <b>Gesamtkosten minimal</b>. Dort schneiden sich die fallende Bestellkostenkurve und die steigende Lagerkostenkurve.'),
    fig=fw('Kostenverläufe im Vorlesungsbeispiel. Tippe auf die Kurven und den Optimalpunkt.') + bild(kosten_svg()),
    figcap='nach Folien „Dilemma der optimalen Losgröße“ und „Kostenverläufe“',
    article=h3('Zwei gegenläufige Kosten')
        + fx('Gesamtkosten', r'K(x) = K_B(x) + K_L(x)', 'Gesamtkosten = Bestellkosten + Lagerkosten', '')
        + gegen(('Bestellkosten', 'große Menge optimal (Rabatte, bestellfixe Kosten …); fallen degressiv mit x'), ('Lagerkosten', 'kleine Menge optimal; steigen linear mit x (Annahme linearer Lagerkosten)'))
        + p('<b>Das (klassische) Dilemma der optimalen Bestellmenge resultiert aus der gegenläufigen Entwicklung von Lager- und Bestellkosten bei sich ändernder Bestellmenge.</b> Bei steigender Bestellmenge fallen die Bestellkosten, die Lagerkosten wachsen. Der Schnittpunkt der beiden Kurven markiert die optimale Menge im Minimum der Gesamtkostenkurve.')
        + h3('Wer hat’s erfunden?')
        + p('Ford Whitman Harris (1877–1962), amerikanischer Patentanwalt, publizierte 1913 als Erster eine Formel zur klassischen Losgröße. Kurt Andler (1894–1984), deutscher Ingenieur, veröffentlichte sie 1929 erstmals im deutschsprachigen Raum. Daher: Andler-Harris-Formel bzw. Andlersche Losgrößenformel.')
        + falle('Den Einkaufspreis (Wareneinsatz) in die Gesamtkosten der Formel einrechnen. Das Modell betrachtet nur Bestell- und Lagerkosten; der Einkaufspreis ist von der Menge unabhängig (keine Rabatte).'),
    merk='K(x) = K_B(x) + K_L(x). Bestellkosten fallen mit x (große Menge optimal), Lagerkosten steigen mit x (kleine Menge optimal): gegenläufig = Dilemma. Optimum im Minimum der Gesamtkosten = Schnittpunkt K_B = K_L. Harris 1913, Andler 1929.',
    exam='Kostenverläufe skizzieren und erklären; Dilemma in eigenen Worten.',
    fehler=['Das Optimum dort einzeichnen, wo die Lagerkosten null sind.', 'Bestellkosten als linear steigend zeichnen.'],
    src='Folien 77–78')

# ---------------------------------------------------------------- 6 Andler-Formel
t_andler = thema('andler', 'Andler-Formel: optimale Bestellmenge berechnen', star=True,
    kern='K_B = m/x · k_b (Bestellhäufigkeit × Kosten je Bestellung), K_L = x/2 · w · i_L (Ø Bestand × Wert × Lagerhaltungskostensatz). Gleichsetzen und nach x auflösen: x_opt = √(2 · m · k_b / (w · i_L)). Bestellhäufigkeit = m / x_opt. Die Annahmen (konstanter Bedarf, keine Rabatte, keine Fehlmengen, beliebig teilbar …) sind in der Praxis z. T. nicht gegeben.',
    kurz=p('Bonbonhersteller: 12 t Zucker im Jahr, 600 €/t, 150 € pro Bestellung, Lagerhaltungskostensatz 15 %. Einsetzen: x = √(2 · 12 · 150 / (600 · 0,15)) = √40 ≈ <b>6,32 t</b>.')
        + p('Kann man nur ganze Tonnen bestellen, vergleicht man 6 t und 7 t: K(6) = 300 + 270 = <b>570 €</b>, K(7) ≈ 257 + 315 = 572 €. Also <b>6 t</b>, und man bestellt <b>2-mal</b> im Jahr.'),
    fig=fw('Andler-Rechner mit den Werten der Vorlesung. Verschiebe die Regler.')
        + regler([('anM', 'Jahresbedarf m', 2, 60, 1, 12, 't'), ('anK', 'Bestellkosten k_b', 20, 500, 10, 150, '€'), ('anW', 'Preis w', 100, 2000, 50, 600, '€/t'), ('anI', 'Lagerkostensatz i_L', 5, 40, 1, 15, '%')])
        + schritte_karten([('① x_opt', 'an1', '#an1t'), ('② ganze Tonnen', 'an2', '#an2t'), ('③ Bestellhäufigkeit', 'an3', '#an3t')]),
    figcap='nach Folien „Andler-Harris-Formel“ und „Beispielaufgabe“',
    article=h3('Die Kostenfunktionen')
        + fx('Bestellkosten', r'K_B = \frac{m}{x} \cdot k_b', 'Bestellhäufigkeit (m/x) mal Bestellkosten pro Auftrag', r'\(\frac{12}{6} \cdot 150 = 300\)')
        + fx('Lagerkosten', r'K_L = \frac{x}{2} \cdot w \cdot i_L = \frac{x}{2} \cdot w \cdot (i_k + i_{ph})', 'durchschnittlicher Bestand (x/2) mal Wert pro Stück mal Lagerhaltungskostensatz (Kapitalbindung + physische Lagerung)', r'\(\frac{6}{2} \cdot 600 \cdot 0{,}15 = 270\)')
        + p('Variablen: x = Menge einer Bestellung, m = im Zeitraum benötigte Menge (z. B. Jahresbedarf), k_b = Bestellkosten pro Auftrag, w = Wert pro Stück, i_L = Lagerhaltungskostensatz aus i_k (Kapitalbindungskosten) und i_ph (physische Lagerhaltungskosten).')
        + h3('Herleitung')
        + p('Das Minimum der Gesamtkosten liegt beim Schnittpunkt von K_B und K_L. Gleichsetzen:')
        + p(r'\[\frac{m}{x} \cdot k_b = \frac{x}{2} \cdot w \cdot i_L \;\Rightarrow\; x^2 = \frac{2 \cdot m \cdot k_b}{w \cdot i_L} \;\Rightarrow\; x_{opt} = \sqrt{\frac{2 \cdot m \cdot k_b}{w \cdot i_L}}\]')
        + p('(Die negative Wurzel ergibt keinen Sinn.) Dasselbe Ergebnis liefert die Ableitung K’(x) = 0.')
        + bsp('Beispielaufgabe der Vorlesung: Bonbon-Produzent', 'm = 12 t/Jahr, w = 600 €/t, k_b = 150 €/Bestellung, i_L = 15 %; nur ganze Tonnen bestellbar', [
            ('a) x_opt', r'\(\sqrt{\frac{2 \cdot 12 \cdot 150}{600 \cdot 0{,}15}} = \sqrt{\frac{3600}{90}} = \sqrt{40} \approx 6{,}32\) t'),
            ('nur ganze Tonnen: K(6)', r'\(\frac{12}{6} \cdot 150 + \frac{6}{2} \cdot 90 = 300 + 270 = 570\) €'),
            ('K(7)', r'\(\frac{12}{7} \cdot 150 + \frac{7}{2} \cdot 90 \approx 257{,}14 + 315 = 572{,}14\) €'),
            ('Entscheidung', '6 t: rund 2,14 € günstiger als 7 t'), ('b) Bestellhäufigkeit', '12 / 6 = 2-mal im Jahr')],
            'Bei ganzzahligen Mengen immer beide Nachbarn prüfen; die Kostenkurve ist nicht symmetrisch.')
        + h3('Modellannahmen')
        + liste(['nur ein Material wird betrachtet', 'Lagerabbau kontinuierlich und linear, Bedarf je Zeiteinheit konstant', 'Beschaffung bzw. Lagerauffüllung ohne Zeitverzug',
                 'Bestellmenge innerhalb des Planungszeitraums konstant', 'keine Restriktionen (Lagerkapazität, Finanzvolumen, Produktionskapazität, Absatz)',
                 'Faktorpreise unabhängig von der Bestellmenge (keine Mengenrabatte, keine Transportkostenstaffelung)', 'Bedarf jederzeit gedeckt (keine Fehlmengen)',
                 'konstante Materialqualität', 'Beschaffungsmengen beliebig teilbar (keine Bindung an Paletten, Container, Lkw-Ladungen)'])
        + p('<b>Die Andlersche Losgrößenformel gehört zu den bekanntesten betriebswirtschaftlichen Optimierungsmodellen. Die Annahmen sind z. T. in der praktischen Anwendung nicht gegeben.</b>')
        + klausur_hinweis('In der Klausur kam „optimale Bestellmenge berechnen“. Formel auswendig, Werte sauber einsetzen (Prozent als Dezimalzahl), bei ganzzahligen Mengen beide Nachbarn vergleichen, Bestellhäufigkeit angeben.')
        + falle('i_L als 15 statt 0,15 einsetzen, oder den Faktor 2 im Zähler vergessen.'),
    merk='x_opt = √(2·m·k_b / (w·i_L)); K_B = m/x·k_b; K_L = x/2·w·i_L; Häufigkeit = m/x_opt. Beispiel: √(2·12·150/(600·0,15)) = √40 ≈ 6,32 t; ganzzahlig K(6) = 570 € < K(7) = 572,14 € → 6 t, 2 Bestellungen/Jahr. Annahmen: konstanter Bedarf, keine Rabatte, keine Fehlmengen, keine Restriktionen, sofortige Auffüllung, beliebig teilbar.',
    exam='Optimale Bestellmenge und Bestellhäufigkeit berechnen; ggf. ganzzahlig vergleichen; Annahmen nennen und kritisieren.',
    fehler=['Faktor 2 vergessen.', 'Prozentsatz nicht in Dezimalzahl umrechnen.', 'Bei ganzzahligen Mengen einfach runden statt K(6) und K(7) zu vergleichen.'],
    src='Folien 79–84')

KAPITEL = kapitel('k3', 'Bestände, Bestellsysteme, optimale Bestellmenge',
    'Wie viel Lager braucht man, wann wird bestellt, und wie viel? Von Bestandsfunktionen und Lagerkennzahlen über Meldebestand und die vier Bestellpolitiken bis zur Andler-Formel.',
    ['Bestände und Lager', 'Kennzahlen', 'Meldebestand', 'Bestellsysteme', 'Dilemma', 'Andler-Formel'],
    [t_bestand, t_kennz, t_begriffe, t_systeme, t_dilemma, t_andler])
