import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *

# ---------------------------------------------------------------- 1 Einkaufsspektrum und Materialarten
fig_arten = svg(360, 270,
    box(110, 8, 140, 44, 'E-Bike\n„Neckar 7“', size=12, art='pale', tip='Das Enderzeugnis der Neckarrad GmbH. Was geht hinein, was wird nur verbraucht?')
    + box(4, 80, 112, 56, 'Rohstoffe\nAlu-Rohre,\nAkku-Modul', size=12, art='hl', tip='Rohstoffe (Erzeugnisrohstoffe) sind Hauptbestandteile und gehen direkt in das Produkt ein, auch Halbzeuge und Module.')
    + box(124, 80, 112, 56, 'Hilfsstoffe\nLeim, Lack,\nKleber', size=12, tip='Hilfsstoffe gehen nur mit einer Hilfsfunktion in das Endprodukt ein.')
    + box(244, 80, 112, 56, 'Betriebsstoffe\nStrom,\nSchmieröl', size=12, tip='Betriebsstoffe werden im Produktionsprozess verbraucht, gehen aber nicht ins Produkt ein.')
    + box(4, 176, 170, 56, 'Handelswaren\nHelme, Schlösser\n(unverändert)', size=12, tip='Handelswaren werden ohne große Änderungen weiterverkauft: breiteres Sortiment, zusätzliche Verdienstmöglichkeiten.')
    + box(186, 176, 170, 56, 'Dienstleistungen\nWartung, Versicherung,\nFracht, Beratung', size=12, tip='Dienstleistungen haben keine materielle Substanz, können nicht gelagert werden und werden direkt erbracht.')
    + pfeil(150, 52, 70, 78) + pfeil(180, 52, 180, 78) + strich(210, 52, 290, 78)
    + T(180, 252, 'Pfeil: geht ins Produkt ein\ngestrichelt: wird nur verbraucht', 12, 400, fill='var(--muted)'),
    'Materialarten am Beispiel E-Bike', maxw=420)

t_arten = thema('materialarten', 'Einkaufsspektrum und Materialarten',
    kern='Das Einkaufsspektrum eines Unternehmens reicht von Stanzteilen, Elektronik und Getrieben über Energie und Büromaterial bis zu Dienstleistungen. Materialarten: Rohstoffe (Hauptbestandteile, gehen direkt ins Produkt ein), Hilfsstoffe (gehen mit Hilfsfunktion ein), Betriebsstoffe (werden im Prozess verbraucht), Handelswaren (unverändert weiterverkauft), Dienstleistungen (keine materielle Substanz).',
    kurz=p('Die Neckarrad GmbH kauft nicht nur Rahmen und Akkus, sondern auch Strom, Leim, Frachten, Software und Versicherungen. Alles zusammen ist das <b>Einkaufsspektrum</b>.')
        + p('Geordnet wird es nach <b>Materialarten</b>: Was geht als Hauptbestandteil ins Rad ein (Rohstoff), was nur als Hilfe (Hilfsstoff), was wird verbraucht (Betriebsstoff)? Dazu Handelswaren und Dienstleistungen.'),
    fig=fw('Fünf Materialarten am E-Bike. Tippe auf die Kästen.') + bild(fig_arten),
    figcap='nach Folien „Einkaufsspektrum eines Unternehmens“ und „Einteilungsmöglichkeiten zur Systematisierung der Bedarfe“',
    article=h3('Einkaufsspektrum')
        + p('Beispiele aus dem Einkaufsspektrum: Stanz- und Umformteile, elektronische Bauteile, Gehäuse, Schrauben, Baugruppen, Elektromotoren, Leiterplatten, Getriebe, Zahnräder, Werkzeuge, Maschinen und Anlagen, Energie (Strom, Gas, Brennstoffe), Hardware, Software, Büromaterial, Fahrzeuge, Frachten, Reise-, Personal-, Beratungs-, Marketing-, Reinigungs- und Baudienstleistungen, Versicherungen, Telekommunikation.')
        + p('<b>Qualität und vor allem die Quantität/Menge der benötigten Bedarfe werden zum Ausgangspunkt der materialwirtschaftlichen Planung und der Einkaufsaktivitäten!</b>')
        + h3('Materialarten')
        + p('<b>Die Einteilung der Materialarten ist primär abhängig vom Zweck, der damit verfolgt wird, und kann als eine erste (einfache) Bedarfs- und Marktstrukturierung gesehen werden.</b>')
        + tabelle(['Materialart', 'Kennzeichen', 'Beispiele'], [
            ['Rohstoffe (Erzeugnisrohstoffe)', 'Hauptbestandteile der Erzeugnisse, gehen direkt in das Produkt ein (auch Halbzeuge und Module)', 'Aluminium, Kupfer, Kunststoffgranulat'],
            ['Hilfsstoffe', 'gehen lediglich mit einer Hilfsfunktion in das Endprodukt ein', 'Leim, Öl'],
            ['Betriebsstoffe', 'werden im Produktionsprozess verbraucht', 'Energie, Wasser, Öl'],
            ['Handelswaren', 'werden ohne große Änderungen weiterverkauft; breiteres Sortiment, zusätzliche Verdienstmöglichkeiten', 'Helme, Zubehör'],
            ['Dienstleistungen', 'haben keine materielle Substanz; können nicht gelagert werden, werden direkt erbracht', 'Beratung, Versicherung, Wartung, Service']])
        + falle('Hilfs- und Betriebsstoffe verwechseln. Hilfsstoffe stecken (als Nebensache) im Produkt, Betriebsstoffe nicht: Strom ist im fertigen Rad nicht mehr drin.')
        + spiel('sp-arten', 'Welche Materialart?', ['Rohstoff', 'Hilfsstoff', 'Betriebsstoff', 'Handelsware', 'Dienstleistung'], [
            ('Aluminiumrohr für den Rahmen', 0, 'Hauptbestandteil.'), ('Klebstoff für das Typenschild', 1, 'Geht mit Hilfsfunktion ein.'),
            ('Strom für die Schweißroboter', 2, 'Wird im Prozess verbraucht.'), ('Fahrradhelm, unverändert weiterverkauft', 3, 'Handelsware.'),
            ('Wartung der Lackieranlage', 4, 'Keine materielle Substanz.'), ('Schmieröl für die Maschinen', 2, 'Verbraucht im Prozess.'), ('zugekaufter Akku als Modul', 0, 'Module zählen zu den Rohstoffen.')]),
    merk='Rohstoffe: Hauptbestandteile, direkt im Produkt (auch Halbzeuge, Module). Hilfsstoffe: Hilfsfunktion im Produkt (Leim). Betriebsstoffe: im Prozess verbraucht (Energie, Wasser). Handelswaren: unverändert weiterverkauft. Dienstleistungen: keine materielle Substanz, nicht lagerbar. Menge und Qualität der Bedarfe sind Ausgangspunkt der Planung.',
    exam='Materialarten definieren und Beispiele zuordnen (Multiple Choice).',
    fehler=['Hilfs- und Betriebsstoffe vertauschen.', 'Module/Halbzeuge nicht als Rohstoffe erkennen.'],
    src='Folien 42–43')

# ---------------------------------------------------------------- 2 Primär-, Sekundär-, Tertiärbedarf
fig_bedarf = svg(360, 280,
    box(4, 8, 108, 64, 'Primärbedarf\nverkaufsfähige\nE-Bikes', size=12, art='hl', tip='Primärbedarf: Marktbedarf an verkaufsfähigen Enderzeugnissen (und Ersatzteilen, Handelswaren). Kommt aus der Vertriebsplanung. Wird an externe Kunden geliefert.')
    + box(126, 8, 230, 64, 'Quelle: Vertriebsplanung, Markt-\nbedarf. Z. B. 1.200 E-Bikes im\nQuartal (Beispiel Jeans: die Jeans)', size=12, art='pale', tip='Auch Ersatzteile, die direkt an Kunden gehen, sind Primärbedarf.')
    + box(4, 106, 108, 64, 'Sekundär-\nbedarf\nRahmen, Akkus', size=12, tip='Sekundärbedarf: Bedarf an Werkstoffen (Baugruppen, Einzelteilen, Rohstoffen) zur Fertigung des Primärbedarfs.')
    + box(126, 106, 230, 64, 'Quelle: Stücklistenauflösung (BOM).\n1.200 Räder → 1.200 Rahmen,\n2.400 Laufräder … (Jeans: Stoff)', size=12, art='pale', tip='Der Sekundärbedarf wird aus dem Primärbedarf über die Stückliste bzw. Rezepturen abgeleitet.')
    + box(4, 204, 108, 64, 'Tertiärbedarf\nStrom, Öl,\nWerkzeug', size=12, tip='Tertiärbedarf: Bedarf an Hilfs- und Betriebsstoffen für die Produktion. Nötig für den Fertigungsprozess, fließt aber nicht direkt ins Endprodukt.')
    + box(126, 204, 230, 64, 'Quelle: Verbrauch der Produktion,\nmeist geschätzt (stochastisch)\n(Jeans: Strom für die Nähmaschine)', size=12, art='pale', tip='Tertiärbedarf wird meist aus Vergangenheitswerten geschätzt.')
    + pfeil(58, 72, 58, 104) + pfeil(58, 170, 58, 202),
    'Primär-, Sekundär- und Tertiärbedarf', maxw=420)

t_bedarfsarten = thema('bedarfsarten', 'Primär-, Sekundär- und Tertiärbedarf', star=True,
    kern='Primärbedarf: Marktbedarf an verkaufsfähigen Enderzeugnissen (aus der Vertriebsplanung). Sekundärbedarf: Bedarf an Werkstoffen (Baugruppen, Einzelteile, Rohstoffe) zur Fertigung des Primärbedarfs (aus der Stücklistenauflösung). Tertiärbedarf: Bedarf an Hilfs- und Betriebsstoffen für die Produktion.',
    kurz=p('Die Neckarrad GmbH will im Quartal 1.200 E-Bikes verkaufen: das ist der <b>Primärbedarf</b>. Daraus folgt über die Stückliste, wie viele Rahmen, Akkus und Schrauben man braucht: der <b>Sekundärbedarf</b>. Und für die Montage braucht man Strom, Öl und Schweißdraht: der <b>Tertiärbedarf</b>.')
        + p('Merkhilfe aus der Vorlesung: Bei einer Jeans ist die Jeans der Primärbedarf, der Stoff der Sekundärbedarf und der Strom für die Nähmaschine der Tertiärbedarf.'),
    fig=fw('Drei Ebenen des Materialbedarfs. Tippe auf die Kästen.') + bild(fig_bedarf),
    figcap='nach Folie „Einteilung der Materialbedarfsarten“',
    article=h3('Arten des Materialbedarfs (nach Ursprung und Erzeugnisebene)')
        + tabelle(['Bedarfsart', 'Definition', 'Quelle', 'Beispiel Jeans'], [
            ['Primärbedarf', 'Marktbedarf an verkaufsfähigen Enderzeugnissen (fertige Maschinen, Ersatzteile, Handelswaren); wird an externe Kunden geliefert', 'Vertriebsplanung', 'die Jeans'],
            ['Sekundärbedarf', 'Bedarf an Werkstoffen (Baugruppen, Einzelteilen, Rohstoffen, Vorprodukten) zur Fertigung des Primärbedarfs', 'Stücklistenauflösung (BOM), Rezepturen', 'Stoff, Knöpfe, Garn'],
            ['Tertiärbedarf', 'Bedarf an Hilfs- und Betriebsstoffen für die Produktion; nötig für den Fertigungsprozess, fließt aber nicht direkt ins Endprodukt', 'Verbrauch der Produktion', 'Strom']])
        + klausur_hinweis('Laut Vorlesung „extrem wichtig“, wird abgefragt: die drei Bedarfsarten definieren, ihre Quelle nennen (Vertriebsplanung, Stücklistenauflösung, Hilfs-/Betriebsstoffe) und Beispiele zuordnen.')
        + h3('Vom Primär- zum Sekundärbedarf')
        + p('Die programmorientierte (deterministische) Bedarfsermittlung leitet den Sekundärbedarf aus dem Primärbedarf über die <b>Auflösung von Stücklisten</b> ab. Mehr dazu im Unterthema Stücklisten.')
        + spiel('sp-bedarf', 'Primär-, Sekundär- oder Tertiärbedarf?', ['Primär', 'Sekundär', 'Tertiär'], [
            ('1.200 E-Bikes laut Absatzplan', 0, 'Verkaufsfähiges Enderzeugnis.'), ('Ersatz-Akkus für Kunden', 0, 'Ersatzteile an externe Kunden sind Primärbedarf.'),
            ('2.400 Laufräder für die Montage', 1, 'Aus der Stückliste abgeleitet.'), ('Aluminium für die Rahmenfertigung', 1, 'Rohstoff für den Primärbedarf.'),
            ('Strom für die Lackieranlage', 2, 'Betriebsstoff.'), ('Schmieröl der Maschinen', 2, 'Betriebsstoff.')]),
    merk='Primärbedarf: verkaufsfähige Enderzeugnisse und Ersatzteile (Vertriebsplanung, Marktbedarf). Sekundärbedarf: Baugruppen, Einzelteile, Rohstoffe für den Primärbedarf (Stücklistenauflösung). Tertiärbedarf: Hilfs- und Betriebsstoffe für die Produktion. Jeans – Stoff – Strom.',
    exam='Definieren, Quelle nennen, Beispiele zuordnen; gilt als besonders wichtig.',
    fehler=['Ersatzteile als Sekundärbedarf einordnen: Gehen sie an Kunden, sind sie Primärbedarf.', 'Tertiärbedarf mit Zusatzbedarf verwechseln.'],
    src='Folie 44')

# ---------------------------------------------------------------- 3 Brutto- und Nettobedarf
zeilen_bn = [('Sekundärbedarf', 'aus Stücklistenauflösung', 1000, ''), ('+ Zusatzbedarf', 'Ausschuss, Schwund …', 50, '+'),
             ('= Bruttobedarf', 'benötigter Periodenbedarf', 1050, '='), ('− Lagerbestände', 'im Lager vorhanden', 300, '−'),
             ('− Bestellbestände', 'offene Bestellungen', 200, '−'), ('+ reservierte Bestände', 'für Aufträge vorgemerkt', 80, '+'), ('= Nettobedarf', 'zu disponieren / beschaffen', 630, '=')]

def bn_svg():
    s = ''
    for i, (k, e, w, op) in enumerate(zeilen_bn):
        y = 4 + i * 38
        art = 'hl' if k == '= Nettobedarf' else ('pale' if op == '=' else 'card')
        s += box(4, y, 150, 32, k, size=12, art=art, tip={'Sekundärbedarf': 'Wird aus dem Primärbedarf über die Stücklistenauflösung abgeleitet.',
                '+ Zusatzbedarf': 'Ungeplanter Bedarf, der zusätzlich benötigt wird (Ausschuss, Schwund, Verschnitt); statistisch ermittelt und als Prozentsatz zugeschlagen.',
                '= Bruttobedarf': 'Der für die Fertigung der Erzeugnisse benötigte Periodenbedarf.',
                '− Lagerbestände': 'Im Lager vorhandener Bestand: muss nicht beschafft werden.',
                '− Bestellbestände': 'Offene Bestellungen (intern oder extern): erwartete Zugänge.',
                '+ reservierte Bestände': 'Bestände für vorgemerkte Aufträge, die in Kürze entnommen werden und daher nicht zur Verfügung stehen.',
                '= Nettobedarf': 'Ausgangspunkt für die Materialdisposition und Beschaffung.'}[k])
        s += T(160, y + 21, e, 12, 400, 'start', 'var(--muted)')
        s += T(352, y + 21, f'{w:,}'.replace(',', '.'), 13, 700, 'end')
    return svg(360, 274, s, 'Vom Sekundär- zum Nettobedarf', maxw=420)

t_netto = thema('brutto-netto', 'Vom Bruttobedarf zum Nettobedarf', star=True,
    kern='Sekundärbedarf + Zusatzbedarf = Bruttobedarf (der für die Fertigung benötigte Periodenbedarf). Bruttobedarf − Lagerbestände − Bestellbestände + reservierte Bestände = Nettobedarf (Ausgangspunkt für Disposition und Beschaffung).',
    kurz=p('Die Montage braucht im Quartal 1.000 Rahmen (Sekundärbedarf). Weil erfahrungsgemäß 5 % Ausschuss anfallen, plant man 1.050 (<b>Bruttobedarf</b>). Im Lager liegen 300, 200 sind schon bestellt. Aber 80 der Lagerrahmen sind für einen Großauftrag reserviert, die zählen nicht.')
        + p('Also bestellt man 1.050 − 300 − 200 + 80 = <b>630 Rahmen</b>: das ist der <b>Nettobedarf</b>.'),
    fig=fw('Das Schema Zeile für Zeile. Tippe auf die Zeilen, dann rechne selbst.') + bild(bn_svg())
        + regler([('bnS', 'Sekundärbedarf', 200, 3000, 50, 1000, 'Stück'), ('bnZ', 'Zusatzbedarf', 0, 20, 1, 5, '%'), ('bnL', 'Lagerbestand', 0, 1500, 10, 300, 'Stück'),
                  ('bnB', 'Bestellbestand', 0, 1000, 10, 200, 'Stück'), ('bnR', 'reserviert', 0, 500, 10, 80, 'Stück')])
        + schritte_karten([('① Bruttobedarf', 'bnA', '#bnAt'), ('② verfügbar', 'bnV', '#bnVt'), ('③ Nettobedarf', 'bnN', '#bnNt')]),
    figcap='nach Folie „Ermittlung des Netto- aus dem Bruttobedarf“',
    article=h3('Das Schema')
        + tabelle(['Position', 'Erläuterung'], [
            ['Sekundärbedarf', 'wird aus dem Primärbedarf über Stücklistenauflösung abgeleitet'],
            ['+ Zusatzbedarf', 'ungeplanter Bedarf, der zusätzlich benötigt wird (z. B. Ausschuss, Schwund, Verschnitt); wird statistisch ermittelt und als Prozentsatz zugeschlagen'],
            ['<b>= Bruttobedarf</b>', '<b>für die Fertigung der Erzeugnisse benötigter Periodenbedarf</b>'],
            ['− Lagerbestände', 'im Lager vorhandener Bestand'],
            ['− Bestellbestände', 'offene Bestellungen (intern oder extern), erwartete Zugänge'],
            ['+ reservierte Bestände', 'Bestände für vorgemerkte Aufträge, die in Kürze aus dem Lager entnommen werden und daher nicht zur Verfügung stehen'],
            ['<b>= Nettobedarf</b>', '<b>Ausgangspunkt für die Materialdisposition / -beschaffung</b>']])
        + klausur_hinweis('Genau diese Definition des Bruttobedarfs („für die Fertigung der Erzeugnisse benötigter Periodenbedarf“) wird abgefragt. In der Klausur kam eine Tabelle: Aus dem Bruttobedarf den Nettobedarf bestimmen, ohne Rechnen, nur die Positionen nennen und erklären.')
        + h3('Warum werden reservierte Bestände addiert?')
        + p('Reservierte Bestände liegen zwar physisch im Lager und wurden mit dem Lagerbestand abgezogen. Sie sind aber schon für einen anderen Auftrag vorgemerkt und stehen nicht zur Verfügung. Deshalb werden sie <b>wieder hinzugerechnet</b>.')
        + h3('Prozessablauf der Materialbedarfsermittlung')
        + fluss([('1', 'Primärbedarf für Erzeugnisse und Ersatzteile ermitteln'), ('2', 'Sekundärbedarf ermitteln (deterministisch oder stochastisch)'), ('3', 'Tertiärbedarf bestimmen'),
                 ('4', 'Zusatzbedarf bestimmen'), ('5', 'Bruttobedarf ermitteln'), ('6', 'Lagerbestand abfragen')], hl=5)
        + p('Danach folgen Aktivitäten zur Sicherstellung der Materialverfügbarkeit, z. B. Material reservieren oder den Bestellvorgang anstoßen.')
        + bsp('Rechnen mit dem Schema', 'Sekundärbedarf 1.000 Rahmen, Zusatzbedarf 5 %, Lager 300, bestellt 200, reserviert 80', [
            ('Zusatzbedarf', '5 % von 1.000 = 50'), ('Bruttobedarf', '1.000 + 50 = 1.050'), ('Nettobedarf', '1.050 − 300 − 200 + 80 = 630')], 'Der Nettobedarf ist die Menge, die tatsächlich beschafft werden muss.')
        + falle('Reservierte Bestände abziehen statt addieren. Sie stehen nicht zur Verfügung, also erhöhen sie den Nettobedarf.'),
    merk='Sekundärbedarf + Zusatzbedarf (Ausschuss, Schwund, Verschnitt, in %) = Bruttobedarf (für die Fertigung benötigter Periodenbedarf) − Lagerbestände − Bestellbestände (offene Bestellungen) + reservierte Bestände (vorgemerkt, nicht verfügbar) = Nettobedarf (Ausgangspunkt der Disposition/Beschaffung).',
    exam='Schema als Tabelle vervollständigen, jede Position erklären; Bruttobedarf exakt definieren; ggf. kleine Rechnung.',
    fehler=['Reservierte Bestände abziehen.', 'Bestellbestände vergessen.', 'Zusatzbedarf erst nach dem Bruttobedarf ansetzen.'],
    src='Folien 45–46')

# ---------------------------------------------------------------- 4 Methoden der Bedarfsermittlung
fig_meth = svg(360, 300,
    box(4, 6, 112, 52, 'programm-\norientiert /\ndeterministisch', size=12, tip='Programmorientierte (deterministische) Bedarfsplanung: exakte Ableitung aus dem Produktionsprogramm über Stücklisten.')
    + box(124, 6, 112, 52, 'verbrauchs-\norientiert /\nstochastisch', size=12, tip='Verbrauchsorientierte (stochastische) Bedarfsplanung: aus Vergangenheitsdaten wird auf zukünftige Bedarfe geschlossen.')
    + box(244, 6, 112, 52, 'subjektiv /\nheuristisch\n(Schätzung)', size=12, art='weak', tip='Analog- und Intuitivschätzung. Laut Vorlesung: sollte nicht gemacht werden.')
    + box(4, 84, 54, 44, 'analy-\ntisch', size=12, art='hl', tip='Analytische Verfahren: Auflösung der Stücklisten vom Erzeugnis zu den Teilen. Im Kurs behandelt.')
    + box(62, 84, 54, 44, 'synthe-\ntisch', size=12, tip='Synthetische Verfahren: vom Teil aus über Teileverwendungsnachweise.')
    + box(124, 84, 74, 44, 'Mittelwert-\nbildung', size=12, art='hl', tip='Methoden der Mittelwertbildung: arithmetischer, gleitender und gewichteter gleitender Mittelwert. Im Kurs behandelt.')
    + box(202, 84, 74, 44, 'exponent.\nGlättung', size=12, art='hl', tip='Exponentielle Glättung 1. und 2. Ordnung. Die 1. Ordnung wird im Kurs behandelt.')
    + box(280, 84, 76, 44, 'Regressions-\nanalyse', size=12, tip='Regressionsanalyse: Bedarf als Funktion der Zeit oder anderer Größen.')
    + box(244, 150, 112, 44, 'Analog- /\nIntuitivschätzung', size=12, art='weak', tip='Subjektive Schätzungen: nur, wenn nichts anderes geht.')
    + box(124, 150, 112, 64, 'arithm. MW\ngleitender MW\ngewichteter\ngleitender MW', size=12, art='pale', tip='Varianten der Mittelwertbildung.')
    + box(124, 222, 112, 44, 'exp. Glättung\n1. Ordnung', size=12, art='pale', tip='Wichtigstes Verfahren der verbrauchsorientierten Bedarfsermittlung.')
    + strich(60, 58, 31, 84) + strich(60, 58, 89, 84) + strich(180, 58, 161, 84) + strich(180, 58, 239, 84) + strich(180, 58, 318, 84) + strich(300, 58, 300, 150)
    + strich(161, 128, 161, 150) + strich(239, 128, 200, 222)
    + T(4, 290, 'Hervorgehoben: im Kurs behandelt (auf der Folie rot umrandet)', 12, 400, 'start', 'var(--muted)'),
    'Methoden der Materialbedarfsermittlung', maxw=420)

t_meth = thema('methoden', 'Methoden der Bedarfsermittlung im Überblick',
    kern='Drei Gruppen: programmorientiert/deterministisch (analytisch über Stücklistenauflösung, synthetisch), verbrauchsorientiert/stochastisch (Mittelwertbildung, exponentielle Glättung, Regressionsanalyse) und subjektiv/heuristisch (Analog- und Intuitivschätzung, sollte vermieden werden). Deterministisch braucht Primärbedarf nach Menge und Termin, Stücklisten, Wiederbeschaffungs- und Durchlaufzeiten und ein leistungsfähiges ERP-System.',
    kurz=p('Wie viele Rahmen braucht die Neckarrad GmbH? Das lässt sich <b>genau ausrechnen</b>: 1.200 Räder, je ein Rahmen. Das ist <b>deterministisch</b> (programmorientiert).')
        + p('Wie viel Schmieröl braucht die Werkstatt? Das rechnet niemand aus, man schaut auf den <b>Verbrauch der Vergangenheit</b>: <b>stochastisch</b>. Und wenn es gar keine Daten gibt, wird <b>geschätzt</b>, was man möglichst vermeiden sollte.'),
    fig=fw('Der Methodenbaum. Hervorgehoben ist, was im Kurs behandelt wird.') + bild(fig_meth),
    figcap='nach Folie „Methoden der Materialbedarfsermittlung (Überblick)“',
    article=h3('Drei Gruppen')
        + tabelle(['Gruppe', 'Idee', 'Verfahren'], [
            ['programmorientiert / deterministisch', 'exakte Ableitung aus dem Produktionsprogramm', 'analytisch (Stücklistenauflösung), synthetisch'],
            ['verbrauchsorientiert / stochastisch', 'aus Vergangenheitsdaten auf künftige Bedarfe schließen', 'Mittelwertbildung (arithmetisch, gleitend, gewichtet gleitend), exponentielle Glättung 1. und 2. Ordnung, Regressionsanalyse'],
            ['subjektiv / heuristisch', 'Schätzung', 'Analogschätzung, Intuitivschätzung; sollte nicht gemacht werden']])
        + h3('Voraussetzungen der deterministischen Bedarfsermittlung')
        + liste(['primärer Erzeugnisbedarf nach Menge und Termin (Vertriebsplanung)', 'Struktur- und Baukastenstücklisten', 'Wiederbeschaffungszeiten der zu beschaffenden Materialien',
                 'Durchlaufzeiten für eigengefertigte Materialien und Montagevorgänge', 'leistungsfähiges Warenwirtschafts-/ERP-System, verlässliche Datenbasis'])
        + h3('Eigenschaften der stochastischen Verfahren')
        + liste(['mathematisch-statistischer Natur: aus Vergangenheitsdaten wird auf zukünftige Bedarfe geschlossen',
                 'immer durch Unsicherheiten geprägt, besonders bei größeren Bedarfsschwankungen',
                 'eignen sich für <b>kontinuierliche</b> Bedarfe (Voraussetzung: Kontinuität im Bedarf) und werden dort eingesetzt, wo deterministische Verfahren nicht möglich oder zu aufwendig sind'])
        + gegen(('deterministisch', 'genau, aber aufwendig; braucht Stücklisten und Programmplanung; für hochwertige Teile (A-Teile)'),
                ('stochastisch', 'einfach, aber unsicher; braucht gleichmäßigen Verbrauch; für Kleinteile, Hilfs- und Betriebsstoffe (C-Teile)'))
        + p('Hinweis der Folie: Das Thema Bedarfsermittlung ist auch in Produktionswirtschaft und Logistik wichtig und wird im weiteren Studium vertieft.'),
    merk='Deterministisch/programmorientiert: analytisch (Stücklistenauflösung) und synthetisch; braucht Primärbedarf nach Menge und Termin, Stücklisten, WBZ, Durchlaufzeiten, ERP. Stochastisch/verbrauchsorientiert: Mittelwerte, exponentielle Glättung, Regression; aus Vergangenheit, unsicher, für kontinuierliche Bedarfe. Subjektiv: Analog-/Intuitivschätzung (vermeiden).',
    exam='Methoden gruppieren und zuordnen; Voraussetzungen deterministischer Verfahren; wann stochastisch?',
    fehler=['Exponentielle Glättung den deterministischen Verfahren zuordnen.', 'Vergessen, dass stochastische Verfahren kontinuierlichen Bedarf voraussetzen.'],
    src='Folien 47–48, 52')

# ---------------------------------------------------------------- 5 Stücklisten
def baum(menge):
    k = lambda x, y, w, t, tip, art='card': box(x, y, w, 40, t, size=12, art=art, tip=tip)
    return svg(360, 250,
        k(120, 6, 120, 'E-Bike (1)', 'Erzeugnis, Stufe 0.', 'hl')
        + k(8, 84, 104, 'Rahmen-\nmodul (1)', 'Baugruppe Stufe 1: 1 je E-Bike.') + k(128, 84, 104, 'Laufrad (2)', 'Baugruppe Stufe 1: 2 je E-Bike.') + k(248, 84, 104, 'Antrieb (1)', 'Baugruppe Stufe 1: Motor und Akku.')
        + k(8, 170, 104, 'Rahmen (1)\nGabel (1)', 'Einzelteile Stufe 2 im Rahmenmodul.') + k(128, 170, 104, 'Felge (1)\nSpeichen (36)', 'Je Laufrad 1 Felge und 36 Speichen.')
        + k(248, 170, 104, 'Motor (1)\nAkku (1)', 'Einzelteile Stufe 2 im Antrieb.')
        + strich(180, 46, 60, 84, dash=False) + strich(180, 46, 180, 84, dash=False) + strich(180, 46, 300, 84, dash=False)
        + strich(60, 124, 60, 170, dash=False) + strich(180, 124, 180, 170, dash=False) + strich(300, 124, 300, 170, dash=False)
        + T(180, 240, f'Für {menge} E-Bikes: {2 * menge} Laufräder, {72 * menge} Speichen', 12, 700, fill='var(--muted)'),
        'Strukturstückliste E-Bike', maxw=420)

t_stl = thema('stuecklisten', 'Stücklisten und Stücklistenauflösung',
    kern='Stücklisten sind ein Verzeichnis der Rohstoffe, Teile und Baugruppen eines Erzeugnisses (quantitativer und qualitativer Aufbau). Ausgangspunkt sind die Konstruktionsunterlagen. Strukturstücklisten zeigen, in welcher Fertigungsstufe eine Baugruppe oder ein Einzelteil verwendet wird; Mengenstücklisten dokumentieren nur die Mengen. Durch Auflösung der Stückliste wird aus dem Primärbedarf der Sekundärbedarf.',
    kurz=p('Ein E-Bike besteht aus einem Rahmenmodul, zwei Laufrädern und einem Antrieb. Jedes Laufrad hat eine Felge und 36 Speichen. Das steht in der <b>Stückliste</b>.')
        + p('Will man 100 E-Bikes bauen, multipliziert man durch: 200 Laufräder, 7.200 Speichen. Diese <b>Stücklistenauflösung</b> macht aus dem Primärbedarf den Sekundärbedarf.'),
    fig=fw('Eine Strukturstückliste als Baum. Schalte die Menge um.') + tafeln('tf-stl', ['1 E-Bike', '100 E-Bikes'], [baum(1), baum(100)]),
    figcap='nach Folien „Exkurs: Stücklisten und Stücklistenauflösung“ (Beispiel dort: Stahlrohrtisch)',
    article=h3('Was ist eine Stückliste?')
        + p('<b>Stücklisten stellen ein Verzeichnis der Rohstoffe, Teile und Baugruppen eines Erzeugnisses dar (quantitativer und qualitativer Aufbau eines Erzeugnisses).</b> Die <b>Konstruktionsunterlagen</b> bilden den Ausgangspunkt für die Erstellung einer Stückliste.')
        + tabelle(['Stücklistenart', 'zeigt', 'Beispiel'], [
            ['Strukturstückliste', 'in welcher Fertigungsstufe eine Baugruppe oder ein Einzelteil verwendet wird (Erzeugnisstruktur als Baum)', 'E-Bike → Laufrad → Speiche'],
            ['Mengenstückliste (Mengenübersichtsstückliste)', 'quantitative Dokumentation der verwendeten Materialien in einem Erzeugnis, ohne Struktur', 'Speichen: 72, Felgen: 2, Rahmen: 1 …'],
            ['Baukastenstückliste', 'jeweils nur eine Stufe (Baugruppe und ihre direkten Bestandteile)', 'Laufrad: 1 Felge, 36 Speichen']])
        + p('Folienbeispiel: Stahlrohrtisch mit Tischplatte, Querrohr, Längsrohren, Verstärkungsstreben, Tischbein, Lasche, Fuß-Stöpsel und Schrauben (Mengenübersichtsstückliste mit Positionsnummer, Teilenummer, Bezeichnung, Menge).')
        + h3('Stücklistenauflösung')
        + p('Bei der <b>analytischen</b> Bedarfsermittlung wird der Primärbedarf über die Stückliste Stufe für Stufe in Baugruppen und Einzelteile zerlegt. Mengen werden entlang des Baums multipliziert: 100 E-Bikes × 2 Laufräder × 36 Speichen = 7.200 Speichen.')
        + bsp('Auflösung', 'Primärbedarf 100 E-Bikes; Stückliste wie im Schaubild', [
            ('Laufräder', '100 · 2 = 200'), ('Speichen', '200 · 36 = 7.200'), ('Akkus', '100 · 1 = 100')], 'Danach kommen Zusatzbedarf und Bestände: Brutto-/Nettorechnung.'),
    merk='Stückliste: Verzeichnis der Rohstoffe, Teile, Baugruppen (quantitativer und qualitativer Aufbau); Basis: Konstruktionsunterlagen. Strukturstückliste: Fertigungsstufen. Mengenstückliste: nur Mengen. Auflösung: Primärbedarf × Mengen entlang des Baums = Sekundärbedarf (analytisches Verfahren).',
    exam='Stücklistenarten unterscheiden; Sekundärbedarf durch Auflösung berechnen.',
    fehler=['Mengen nicht über die Stufen multiplizieren (Speichen je Laufrad mal Laufräder je Rad).'],
    src='Folien 48–51')

# ---------------------------------------------------------------- 6 Mittelwerte
monate = ['Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug']
werte = [100, 103, 138, 114, 126, 98, 169, 144]
assert sum(werte) / 8 == 124 and sum(werte[2:]) / 6 == 131.5
assert round(sum(w * g for w, g in zip(werte[2:], [6, 9, 13, 18, 24, 30])) / 100, 2) == 136.32

def mw_svg():
    X = lambda i: 38 + i * 25
    Y = lambda v: 220 - (v - 88) * 2.2
    s = achsen(30, 220, 352, 20, 'Monat', 'Stück')
    for v in (100, 140):
        s += strich(30, Y(v), 340, Y(v), 'var(--line)', 1, True) + T(26, Y(v) + 4, str(v), 12, 400, 'end', 'var(--muted)')
    s += linie([(X(i), Y(w)) for i, w in enumerate(werte)], 'var(--axis2)', 2)
    for i, w in enumerate(werte):
        s += tpg(punkt(X(i), Y(w), 'var(--primary)', 5), f'{monate[i]}: {w} Stück') + T(X(i), 238, monate[i], 12, 400, fill='var(--muted)')
    for v, t, f, dy in [(124, 'arithm. 124', 'var(--axis)', 14), (131.5, 'gleitend 131,5', 'var(--primary-2)', 4), (136.32, 'gewichtet 136,3', 'var(--primary)', -8)]:
        s += tpg(punkt(X(8), Y(v), f, 6) + strich(X(8) + 7, Y(v), X(8) + 16, Y(v) + dy - 4, f, 1, False) + T(X(8) + 18, Y(v) + dy, t, 12, 700, 'start', f), f'Prognose September, {t}')
    s += T(X(8), 238, 'Sep', 12, 700)
    return svg(360, 250, s, 'Verbrauch Januar bis August und drei Prognosen für September', maxw=420)

t_mw = thema('mittelwerte', 'Stochastisch: arithmetischer, gleitender und gewichteter Mittelwert',
    kern='Arithmetischer Mittelwert: Summe aller Periodenbedarfe durch Anzahl der Perioden. Gleitender Mittelwert: Mittel der letzten n Perioden; die älteste Periode fällt heraus, die neueste kommt hinzu. Gewichteter gleitender Mittelwert: neuere Perioden werden stärker gewichtet, so fließen Trends in die Vorhersage ein.',
    kurz=p('Die Werkstatt der Neckarrad GmbH hat von Januar bis August 100, 103, 138, 114, 126, 98, 169 und 144 Bremsbeläge verbraucht. Wie viele braucht sie im September?')
        + p('Drei Antworten: <b>124</b> (Durchschnitt aller acht Monate), <b>131,5</b> (Durchschnitt der letzten sechs) oder <b>136,32</b> (letzte sechs, neuere stärker gewichtet). Je mehr Gewicht auf den jüngsten Werten liegt, desto stärker folgt die Prognose dem Trend.'),
    fig=fw('Verbrauch und drei Prognosen für September. Tippe auf die Punkte.') + bild(mw_svg()),
    figcap='nach Folien „Stochastische Bedarfsermittlung“ (Zahlenbeispiel der Vorlesung)',
    article=h3('Arithmetischer Mittelwert')
        + fx('arithmetischer Mittelwert', r'V = \frac{T_1 + T_2 + \dots + T_n}{n}', 'V = Vorhersagebedarf der nächsten Periode, T = Materialbedarf der Periode, n = Anzahl der Perioden', r'\(V_{Sep} = \frac{992}{8} = 124\)')
        + h3('Gleitender Mittelwert')
        + p('<b>Beim gleitenden Mittelwertverfahren wird aus einer bestimmten Anzahl Perioden ein Mittelwert berechnet. Bei der Berechnung wird das am weitesten zurückliegende Periodenergebnis eliminiert und durch den neusten Periodenverbrauch ersetzt.</b>')
        + fx('gleitender Mittelwert (6 Perioden)', r'V = \frac{T_1 + T_2 + \dots + T_6}{6}', 'immer die letzten sechs Perioden', r'\(V_{Sep} = \frac{138+114+126+98+169+144}{6} = 131{,}5 \approx 132\)')
        + p('Tatsächlicher Verbrauch im September: 102. Dann fällt der März heraus: \\(V_{Okt} = \\frac{114+126+98+169+144+102}{6} = 125{,}5 \\approx 126\\).')
        + h3('Gewichteter gleitender Mittelwert')
        + p('<b>Weiter zurückliegende Perioden werden schwächer gewichtet als neuere Perioden, so fließen Trends in die Vorhersage ein.</b>')
        + fx('gewichteter gleitender Mittelwert', r'V = \frac{T_1 G_1 + T_2 G_2 + \dots + T_n G_n}{G_1 + G_2 + \dots + G_n}', 'G = Gewichtung der Periode', r'\(V_{Sep} = \frac{138 \cdot 6 + 114 \cdot 9 + 126 \cdot 13 + 98 \cdot 18 + 169 \cdot 24 + 144 \cdot 30}{100} = 136{,}32\)')
        + p('Die Gewichte (6, 9, 13, 18, 24, 30 %) sind im Beispiel willkürlich gesetzt; sie summieren sich zu 100.')
        + tabelle(['Verfahren', 'Prognose September', 'Eigenschaft'], [['arithmetisch (8 Monate)', '124', 'alle Werte gleich, reagiert träge'],
                                                                    ['gleitend (6 Monate)', '131,5', 'alte Werte fallen heraus'], ['gewichtet gleitend (6 Monate)', '136,32', 'neue Werte zählen mehr, Trend fließt ein']])
        + falle('Beim gleitenden Mittelwert alle Perioden nehmen statt nur der letzten n.'),
    merk='Arithmetisch: Summe / n (Beispiel 992/8 = 124). Gleitend: letzte n Perioden, älteste fällt heraus (131,5; Oktober 125,5). Gewichtet gleitend: Σ T·G / Σ G, neuere Perioden stärker (136,32), Trends fließen ein.',
    exam='Prognose mit einem der drei Mittelwerte berechnen; Unterschiede erklären.',
    fehler=['Gleitend mit allen Perioden rechnen.', 'Beim gewichteten Mittel nicht durch die Summe der Gewichte teilen.'],
    src='Folien 53–57')

# ---------------------------------------------------------------- 7 Exponentielle Glättung
t_exp = thema('exp-glaettung', 'Exponentielle Glättung 1. Ordnung',
    kern='Wichtigstes Verfahren der verbrauchsorientierten Bedarfsermittlung, geeignet für konstante Verbrauchsverläufe: V_neu = V_alt + α (T_i − V_alt). Die Abweichung der alten Vorhersage vom tatsächlichen Verbrauch wird mit dem Glättungsfaktor α berücksichtigt. Je kleiner α, desto stärker zählen die Vergangenheitswerte und desto stärker werden Zufallsschwankungen geglättet.',
    kurz=p('Die Neckarrad GmbH hat für den Oktober 200 Akkus prognostiziert, verbraucht wurden 250. Die neue Prognose korrigiert die alte um einen Teil des Fehlers: mit α = 0,2 um 20 % von 50, also auf <b>210</b>.')
        + p('Kleines α: ruhige Prognose, reagiert langsam. Großes α: reagiert schnell, aber auch auf Zufälle. In der Praxis ist das Verfahren sehr beliebt; in Krisen wie Corona versagt es, weil die Vergangenheit dann nichts mehr über die Zukunft sagt.'),
    fig=fw('Verschiebe α und den tatsächlichen Verbrauch.')
        + regler([('egA', 'Glättungsfaktor α', 0.1, 0.9, 0.1, 0.2, ''), ('egV', 'alte Vorhersage V_alt', 100, 300, 10, 200, 'Stück'), ('egT', 'tatsächlicher Verbrauch T_i', 100, 400, 10, 250, 'Stück')])
        + schritte_karten([('① Abweichung', 'egD', '#egDt'), ('② Korrektur', 'egK', '#egKt'), ('③ neue Vorhersage', 'egN', '#egNt')]),
    figcap='nach Folie „Exponentielle Glättung 1. Ordnung“',
    article=h3('Idee')
        + p('<b>Ein berechneter Prognosewert wird mit einem tatsächlich eingetretenen Verbrauch verglichen und die dabei entstehende Abweichung berücksichtigt. Zur Gewichtung wird der Glättungsfaktor α verwendet.</b> Die exponentielle Glättung eignet sich für <b>konstante Verbrauchsverläufe</b>.')
        + fx('exponentielle Glättung 1. Ordnung', r'V_{neu} = V_{alt} + \alpha \cdot (T_i - V_{alt})', 'neue Vorhersage = alte Vorhersage + α mal Prognosefehler; T_i = tatsächlicher Bedarf der abgelaufenen Periode, α zwischen 0 und 1', r'\(200 + 0{,}2 \cdot (250 - 200) = 210\)')
        + tabelle(['α', 'Rechnung', 'V_neu'], [['0,2', '200 + 0,2 · (250 − 200)', '210'], ['0,5', '200 + 0,5 · (250 − 200)', '225'], ['0,7', '200 + 0,7 · (250 − 200)', '235']])
        + h3('Wirkung von α')
        + gegen(('kleines α (üblich ca. 0,1–0,3)', 'Vergangenheitswerte zählen stark; starke Glättung von Zufallsschwankungen; reagiert träge auf echte Veränderungen'),
                ('großes α', 'neueste Werte zählen stark; reagiert schnell; aber auch auf Zufallsschwankungen'))
        + p('Der Name „exponentiell“: Jede alte Beobachtung steckt mit dem Gewicht α(1−α)<sup>k</sup> in der Prognose; die Gewichte nehmen exponentiell ab. Die 2. Ordnung berücksichtigt zusätzlich einen Trend.')
        + p('In der Praxis sehr beliebt. Grenze: Bei Krisen wie Corona versagt das Verfahren, weil plötzliche Strukturbrüche nicht aus der Vergangenheit ableitbar sind.')
        + falle('Den Fehler andersherum bilden (V_alt − T_i): Dann bewegt sich die Prognose vom tatsächlichen Wert weg.'),
    merk='V_neu = V_alt + α (T_i − V_alt). Wichtigstes stochastisches Verfahren, für konstante Verläufe. Kleines α: starke Glättung, träge; großes α: schnell, schwankungsanfällig. Beispiel 200/250: α 0,2 → 210, 0,5 → 225, 0,7 → 235. Versagt bei Strukturbrüchen (Corona).',
    exam='Neue Vorhersage berechnen; Wirkung von α erklären.',
    fehler=['Abweichung falsch herum.', 'α groß wählen und „stärkere Glättung“ behaupten: Es ist umgekehrt.'],
    src='Folie 58')

KAPITEL = kapitel('k2', 'Bedarfsermittlung',
    'Was braucht das Unternehmen, und wie viel davon? Von den Materialarten über Primär-, Sekundär- und Tertiärbedarf und das Brutto-Netto-Schema bis zu Stücklisten und Prognoseverfahren.',
    ['Materialarten', 'Bedarfsarten', 'Brutto → Netto', 'Methoden', 'Stücklisten', 'Mittelwerte', 'Exp. Glättung'],
    [t_arten, t_bedarfsarten, t_netto, t_meth, t_stl, t_mw, t_exp])
