import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *

# Durchgehendes Beispiel: die „Neckarrad GmbH“ in Mannheim, ein Hersteller von E-Bikes (Rahmen, Akkus, Motoren, Schrauben, Strom …).

# ---------------------------------------------------------------- 1 Begriffe: MaWi, Einkauf, Logistik, SCM
fig_kette = svg(360, 250,
    box(4, 100, 70, 52, 'Liefe-\nranten', size=12, art='pale', tip='Lieferanten (Tier 1, Tier 2, Tier 3 …) liefern Material, Teile und Module.')
    + box(286, 100, 70, 52, 'Kunden', size=12, art='pale', tip='Kunden: Abnehmer der fertigen Produkte, auch Märkte.')
    + box(84, 100, 60, 52, 'Beschaf-\nfung', size=12, art='hl', tip='Schwerpunkt dieser Vorlesung: Beschaffung, Einkauf, Inbound-Logistik und Supply-Chain-Optimierung.')
    + box(150, 100, 60, 52, 'Produk-\ntion', size=12, tip='Produktionswirtschaft und interne Logistik: Thema im nächsten Semester.')
    + box(216, 100, 60, 52, 'Vertrieb', size=12, tip='Outbound- oder Vertriebslogistik: Weg der Fertigerzeugnisse zum Kunden.')
    + box(4, 14, 210, 44, 'Inbound- / Beschaffungslogistik', size=12, art='pale', tip='Logistik auf der Beschaffungsseite: Güter- und Informationsfluss von den Lieferanten ins Unternehmen.')
    + box(222, 14, 134, 44, 'Outbound- /\nVertriebslogistik', size=12, art='pale', tip='Logistik auf der Absatzseite: vom Unternehmen zu den Kunden.')
    + box(4, 190, 352, 52, 'Supply-Chain-Management: die ganze Kette, dazu\nAuftragsabwicklung und Geldfluss', size=12, tip='SCM gestaltet integrierte Logistikketten von der Rohstoffgewinnung bis zum Endverbraucher. Anders als Logistik umfasst es auch Auftragsabwicklungs- und Geldflussprozesse.')
    + pfeil(74, 126, 82, 126) + pfeil(144, 126, 148, 126) + pfeil(210, 126, 214, 126) + pfeil(276, 126, 284, 126)
    + strich(114, 60, 114, 98) + strich(290, 60, 250, 98) + strich(180, 154, 180, 188),
    'Wertschöpfungskette und Begriffe der Materialwirtschaft', maxw=420)

t_begr = thema('begriffe', 'Materialwirtschaft, Einkauf, Logistik, Supply-Chain-Management',
    kern='Materialwirtschaft im engeren Sinn versorgt die Produktion mit Material; im weiteren Sinn umfasst sie alle materialbezogenen Funktionen bis zur Auslieferung der Fertigerzeugnisse. Einkauf ist enger als Beschaffung (ohne Beschaffungslogistik). Logistik plant und steuert Güter- und Informationsflüsse; Supply-Chain-Management umfasst zusätzlich Auftragsabwicklung und Geldfluss über die ganze Kette.',
    kurz=p('Die Neckarrad GmbH baut E-Bikes. Damit die Montage läuft, müssen Rahmen, Akkus, Motoren und tausend Schrauben rechtzeitig da sein. Dafür sorgt die <b>Materialwirtschaft</b>.')
        + p('Die Begriffe überlappen sich: <b>Einkauf</b> verhandelt und bestellt, <b>Logistik</b> bewegt Güter und Informationen, <b>Supply-Chain-Management</b> denkt die ganze Kette vom Rohstoff bis zum Endkunden, inklusive Geldfluss. Diese Vorlesung konzentriert sich auf die Beschaffungsseite.'),
    fig=fw('Wo liegt der Schwerpunkt dieser Vorlesung? Tippe auf die Kästen.') + bild(fig_kette),
    figcap='nach Folien „Begriffsabgrenzung Materialwirtschaft“',
    article=h3('Materialwirtschaft im engeren und weiteren Sinn')
        + p('<b>Materialwirtschaft i. e. S. umfasst die Aufgabe der Versorgung der Produktion mit Material. I. w. S. werden ihr die Gesamtheit aller materialbezogenen Funktionen zugeordnet</b>, also alle Funktionen, die sich mit der Versorgung des Betriebes und der Steuerung des Materialflusses durch die Fertigung bis hin zur Auslieferung der Fertigerzeugnisse befassen.')
        + liste(['<b>Objekte:</b> Roh-, Hilfs- und Betriebsstoffe, Zulieferteile, Handelswaren sowie Abfälle.',
                 '<b>Aufgaben technischer Natur:</b> Bereitstellung der benötigten Güter und Dienstleistungen in der erforderlichen Art, Menge und Qualität zur rechten Zeit am rechten Ort.',
                 '<b>Aufgaben betriebswirtschaftlich-organisatorischer Natur:</b> die Wirtschaftlichkeit der Bereitstellung optimieren (materialwirtschaftliches Optimum).',
                 '<b>Teilaufgaben</b> (voneinander abhängig): Bedarfsermittlung, Disposition, Bestellmengenplanung, Wareneingangskontrolle, Lagerung, innerbetrieblicher Transport.'])
        + h3('Einkauf')
        + p('<b>Einkauf ist die Summe aller operativen und strategischen Tätigkeiten eines Unternehmens, die im Rahmen der Beschaffung von Werkstoffen, Waren, Betriebsmitteln und Dienstleistungen durchzuführen sind.</b> Der Begriff Einkauf wird häufig <b>enger</b> verstanden als Beschaffung, weil sich die Beschaffung zusätzlich mit der Beschaffungslogistik beschäftigt.')
        + liste(['<b>Ziel:</b> Sicherstellung der Versorgung (Ort, Termin, Menge, Qualität) und Optimierung des Preis-Leistungs-Verhältnisses.',
                 '<b>Tätigkeiten:</b> Einkaufspolitik festlegen, Beschaffungsmarktforschung, Beschaffungsprozess abwickeln, Einkaufscontrolling; zunehmend auch Lieferantenbeziehungsmanagement.'])
        + h3('Logistik')
        + p('<b>Logistik umfasst alle Aufgaben zur integrierten Planung, Koordination, Durchführung und Kontrolle der Güterflüsse sowie der güterbezogenen Informationen von den Entstehungssenken bis hin zu den Verbrauchssenken.</b> Übergeordnete Ziele: Kosten logistischer Aktivitäten senken, Wert und Nutzen von Produkten und Dienstleistungen verbessern, Flexibilität gegenüber Umfeldveränderungen erhöhen.')
        + h3('Supply-Chain-Management (SCM)')
        + p('<b>SCM bezeichnet den Aufbau und die Verwaltung integrierter Logistikketten (Material- und Informationsflüsse) über den gesamten Wertschöpfungsprozess, von der Rohstoffgewinnung über die Veredelungsstufen bis zum Endverbraucher.</b> Im Unterschied zur Logistik umfasst SCM neben den physischen Aktivitäten auch die <b>Auftragsabwicklungs- und Geldflussprozesse</b>.')
        + liste(['<b>Ziel:</b> Leistungen und Services der Supply Chain im Verhältnis zu den eingesetzten Kosten optimieren.',
                 '<b>Voraussetzungen:</b> Integration der Informationsverarbeitung zwischen den Partnern (Schnittstellen) und ein hohes Maß an <b>Vertrauen</b>, weil man Zulieferer und Abnehmer über eigene Störungen informieren muss.'])
        + p('Beispiel Automobilindustrie: Tier-3-Lieferant → Tier-2 → Tier-1 (z. B. ein großer Systemlieferant) → OEM (Original Equipment Manufacturer), verbunden durch ERP-Systeme mit integrierten Informationsströmen. Der Umstieg vom Verbrenner auf E-Autos verändert diese Kette gerade grundlegend.')
        + spiel('sp-begr', 'Welcher Begriff passt?', ['Materialwirtschaft i. e. S.', 'Einkauf', 'Logistik', 'SCM'], [
            ('Versorgung der Produktion mit Material', 0, 'Das ist die enge Definition.'),
            ('Lieferanten auswählen, Preise verhandeln, Einkaufscontrolling', 1, 'Tätigkeiten des Einkaufs.'),
            ('Güter- und Informationsflüsse von der Entstehungs- zur Verbrauchssenke planen und steuern', 2, 'Logistik-Definition.'),
            ('Material-, Informations- und Geldflüsse vom Rohstoff bis zum Endkunden gestalten', 3, 'Geldfluss und ganze Kette: SCM.')]),
    merk='MaWi i. e. S.: Versorgung der Produktion mit Material; i. w. S.: alle materialbezogenen Funktionen bis zur Auslieferung. Einkauf: operative und strategische Beschaffungstätigkeiten, enger als Beschaffung (ohne Beschaffungslogistik). Logistik: Güter- und Informationsflüsse. SCM: ganze Kette inkl. Auftragsabwicklung und Geldfluss; braucht Informationsintegration und Vertrauen.',
    exam='Begriffe abgrenzen (enger/weiter, Einkauf vs. Beschaffung, Logistik vs. SCM), meist als Multiple Choice.',
    fehler=['Einkauf und Beschaffung gleichsetzen: Beschaffung umfasst zusätzlich die Beschaffungslogistik.', 'SCM nur als „große Logistik“ sehen: SCM umfasst auch Auftragsabwicklung und Geldfluss.'],
    src='Folien 13–20')

# ---------------------------------------------------------------- 2 Zieldreieck, 7R, 6R
fig_drei = svg(360, 270,
    f'<polygon points="180,42 40,222 320,222" style="fill:var(--pale);stroke:var(--line)" stroke-width="1.4"/>'
    + box(124, 14, 112, 40, 'Kosten', size=13, tip='Ziel 1 Kosten: Materialkosten, Beschaffungskosten, Prozesskosten (dazu Lager- und Kapitalbindungskosten).')
    + box(4, 206, 120, 40, 'Qualität', size=13, tip='Ziel 2 Qualität: Spezifikation, Erfüllung der Anforderungen.')
    + box(236, 206, 120, 40, 'Lieferleistung', size=13, tip='Ziel 3 Lieferleistung: Wiederbeschaffungszeiten, Termintreue, Gutteile.')
    + box(116, 120, 128, 64, 'Kunden-\nanforderungen /\n-nutzen', size=12, art='hl', tip='Für wen machen wir das? Für die Kunden, auch interne Kunden wie die Produktion. Kundennutzen ergibt sich aus den übergeordneten Unternehmenszielen.')
    + T(180, 266, 'Die drei Ziele sind z. T. konfliktär: ständig ausbalancieren!', 12, 600, fill='var(--muted)'),
    'Zieldreieck der Materialwirtschaft', maxw=420)

t_ziele = thema('zieldreieck', 'Zieldreieck, 7R und 6R',
    kern='Die Materialwirtschaft verfolgt drei Ziele: Kosten, Qualität und Lieferleistung, ausgerichtet auf die Kundenanforderungen. Die Ziele sind zum Teil konfliktär, das Zieldreieck muss ständig ausbalanciert werden. Die 7R nach Plowman: richtiges Gut, Menge, Zustand, Ort, Zeit, Kunde, Kosten. Die 6R nach Jünemann: Menge, Ort, Qualität, Zeitpunkt, Kosten, Information.',
    kurz=p('Die Neckarrad GmbH will billig einkaufen (<b>Kosten</b>), einwandfreie Akkus (<b>Qualität</b>) und pünktliche Lieferungen (<b>Lieferleistung</b>). In der Mitte steht, wofür das alles passiert: der <b>Kundennutzen</b>, auch für interne Kunden wie die Montage.')
        + p('Die drei Ziele ziehen in verschiedene Richtungen. Der billigste Lieferant ist selten der schnellste. Deshalb: <b>ständig ausbalancieren</b>.'),
    fig=fw('Das Zieldreieck. Tippe auf die Ecken und die Mitte.') + bild(fig_drei),
    figcap='nach Folie „Zieldreieck der Materialwirtschaft“',
    article=h3('Das Zieldreieck')
        + tabelle(['Ziel', 'Inhalt'], [['Kosten', 'Materialkosten, Beschaffungskosten, Prozesskosten'], ['Qualität', 'Spezifikation, Erfüllung der Anforderungen'],
                                       ['Lieferleistung', 'Wiederbeschaffungszeiten, Termintreue, Gutteile'], ['Mitte: Kundenanforderungen / -nutzen', 'ergeben sich aus den übergeordneten Unternehmenszielen, z. B. Produktionsmenge, Kostenziele, Qualitätserwartungen; Kunden sind auch interne Kunden (Produktion)']])
        + p('<b>Die Zielsetzungen der Materialwirtschaft sind zum Teil konfliktär. Das Zieldreieck muss (ständig) ausbalanciert werden.</b>')
        + weiter('Wie lässt sich „gute Versorgung“ konkret beschreiben? Mit den R-Regeln.')
        + h3('Die 7R nach Plowman (1964)')
        + p('Der US-Amerikaner Grosvenor E. Plowman hat 1964 die Seven-Rights-Definition etabliert, um die Aufgaben der Logistik zu beschreiben. Sie ist bis heute eine gängige Zielbeschreibung für Materialwirtschaft und Logistik:')
        + merkliste('7R (Plowman)', 'Logistik sichert die Verfügbarkeit …', ['des richtigen <b>Gutes</b>', 'in der richtigen <b>Menge</b>', 'im richtigen <b>Zustand</b>', 'am richtigen <b>Ort</b>', 'zur richtigen <b>Zeit</b>', 'für den richtigen <b>Kunden</b>', 'zu den richtigen <b>Kosten</b>'])
        + h3('Die 6R nach Jünemann')
        + p('Reinhardt Jünemann, Begründer der industriellen Logistik in Deutschland, formulierte ein 6R-Konzept als Leitfaden, um Effizienz und Qualität zu verbessern und Überbestände, Verschwendung und unnötige Kosten zu reduzieren:')
        + merkliste('6R (Jünemann)', 'neu gegenüber 7R: die Information', ['richtige <b>Menge</b>', 'richtiger <b>Ort</b>', 'richtige <b>Qualität</b>', 'richtiger <b>Zeitpunkt</b>', 'richtige <b>Kosten</b>', 'richtige <b>Information</b> (Informationstechnologie)'])
        + gegen(('7R Plowman', 'Gut, Menge, Zustand, Ort, Zeit, Kunde, Kosten'), ('6R Jünemann', 'Menge, Ort, Qualität, Zeitpunkt, Kosten, Information'))
        + spiel('sp-r', 'Gehört das R zu Plowman (7R), Jünemann (6R) oder zu beiden?', ['nur 7R', 'nur 6R', 'beide'], [
            ('richtiger Kunde', 0, 'Nur bei Plowman.'), ('richtige Information', 1, 'Jünemanns Ergänzung: Informationstechnologie.'),
            ('richtige Menge', 2, 'In beiden.'), ('richtiger Zustand', 0, 'Nur bei Plowman (bei Jünemann: Qualität).'), ('richtige Kosten', 2, 'In beiden.'), ('richtige Qualität', 1, 'Bei Jünemann ausdrücklich.')]),
    merk='Zieldreieck: Kosten (Material-, Beschaffungs-, Prozesskosten), Qualität (Spezifikation, Anforderungen), Lieferleistung (Wiederbeschaffungszeit, Termintreue, Gutteile); Mitte: Kundennutzen. Ständig ausbalancieren. 7R Plowman 1964: Gut, Menge, Zustand, Ort, Zeit, Kunde, Kosten. 6R Jünemann: Menge, Ort, Qualität, Zeitpunkt, Kosten, Information.',
    exam='Zieldreieck zeichnen oder ergänzen; 7R aufzählen; 7R und 6R unterscheiden.',
    fehler=['Die Mitte des Dreiecks vergessen: Kundenanforderungen/-nutzen.', '7R und 6R vermischen: „Information“ gehört zu Jünemann, „Kunde“ und „Zustand“ zu Plowman.'],
    src='Folien 21–23')

# ---------------------------------------------------------------- 3 Zielkonflikte
t_konfl = thema('zielkonflikte', 'Zielkonflikte im multidimensionalen Zielsystem',
    kern='Das multidimensionale Zielsystem führt zu Zielkonflikten zwischen den Zieldimensionen (z. B. Kosten gegen Lieferleistung), innerhalb einer Dimension (z. B. Lagerkosten gegen Beschaffungskosten) und zwischen der Materialwirtschaft und anderen Unternehmensfunktionen (Entwicklung, Vertrieb, Fertigung).',
    kurz=p('Eine Bestellung kostet bei der Neckarrad GmbH rund 150 €. Bestellt man lieber 6.000 Klingeln auf einmal und lagert sie drei Jahre? Oder 2.000 und lagert ein Jahr? Weniger Bestellungen sparen <b>Beschaffungskosten</b>, erhöhen aber die <b>Lagerkosten</b>.')
        + p('Das ist ein Konflikt <b>innerhalb</b> der Dimension Kosten. Dazu kommen Konflikte <b>zwischen</b> den Dimensionen und mit <b>anderen Abteilungen</b>. Man muss die Kosten immer austarieren.'),
    fig=fw('Drei Arten von Zielkonflikten. Schalte um.')
        + tafeln('tf-konfl', ['zwischen', 'innerhalb', 'Abteilungen'], [
            svg(360, 200, box(110, 10, 140, 44, 'Kosten', size=13, tip='Billige Lieferanten aus Fernost senken die Kosten …')
                + box(10, 140, 140, 44, 'Qualität', size=13, tip='… aber vielleicht nicht die Qualität …')
                + box(210, 140, 140, 44, 'Lieferleistung', size=13, art='hl', tip='… und die Lieferzeit wird lang. Konflikt zwischen den Zieldimensionen.')
                + pfeil(160, 56, 90, 136) + pfeil(200, 56, 270, 136) + pfeil(152, 162, 206, 162) + T(180, 110, 'Konflikte zwischen\nden Zieldimensionen', 12, 600, fill='var(--muted)'), 'Konflikte zwischen Dimensionen', maxw=420),
            svg(360, 200, box(10, 20, 160, 70, 'große Bestellmenge\n6.000 Stück, 3 Jahre\nLager', size=12, tip='Wenige Bestellungen: niedrige Beschaffungskosten, aber hohe Lager- und Kapitalbindungskosten.')
                + box(190, 20, 160, 70, 'kleine Bestellmenge\n2.000 Stück, 1 Jahr\nLager', size=12, tip='Viele Bestellungen: hohe Beschaffungskosten (je ca. 150 €), aber niedrige Lagerkosten.')
                + box(60, 124, 240, 56, 'Lagerkosten vs.\nBeschaffungskosten', size=13, art='hl', tip='Konflikt innerhalb der Kostendimension; gelöst wird er mit der optimalen Bestellmenge (Andler).')
                + pfeil(90, 92, 150, 122) + pfeil(270, 92, 210, 122), 'Konflikt innerhalb der Kosten', maxw=420),
            svg(360, 200, ''.join(box(4, 8 + i * 47, 110, 40, b, size=12, art='pale', tip=f'{b}: will {z.replace(chr(10), " ")}; Logistikziel dagegen: {l.replace(chr(10), " ")}.')
                                  + box(122, 8 + i * 47, 116, 40, z, size=12, tip=f'Bereichsziel {b}: {z.replace(chr(10), " ")}')
                                  + box(246, 8 + i * 47, 110, 40, l, size=12, art='hl' if i == 3 else 'card', tip=f'Konkurrierendes Logistikziel: {l.replace(chr(10), " ")}')
                                  for i, (b, z, l) in enumerate([('Entwicklung', 'neuester\ntechn. Stand', 'Standar-\ndisierung'), ('Vertrieb', 'Kunden-\nwünsche erfüllen', 'Varianten be-\nschränken'),
                                                                 ('Fertigung', 'große Puffer\nund Lose', 'niedrige\nBestände'), ('Beschaffung', 'große Bestell-\nmengen (Preis)', 'kleine Anliefer-\nmengen')])),
                'Konflikte mit anderen Bereichen', maxw=420)]),
    figcap='nach Folien „Zielkonflikte durch multidimensionales Zielsystem“ und „Ausgewählte materialwirtschaftliche Zielkonflikte“',
    article=h3('Drei Ebenen von Zielkonflikten')
        + p('<b>Das multidimensionale Zielsystem der Materialwirtschaft führt sowohl innerhalb der Materialwirtschaft zu Zielkonflikten als auch zu Zielkonflikten zwischen der Materialwirtschaft und anderen Unternehmensfunktionen (z. B. Entwicklung, Vertrieb).</b>')
        + liste(['<b>Zwischen den Zieldimensionen</b>: Kosten, Qualität und Lieferleistung konkurrieren.',
                 '<b>Innerhalb einer Zieldimension</b>: z. B. in der Kostendimension Lagerkosten gegen Beschaffungskosten (eine Bestellung kostet ca. 150 €; 6.000 Stück für drei Jahre oder 2.000 Stück für ein Jahr?).',
                 '<b>Mit anderen Unternehmensfunktionen</b>: siehe Tabelle.'])
        + h3('Ausgewählte Zielkonflikte (nach Schulte)')
        + tabelle(['Bereich', 'Bereichsziel', 'konkurrierendes Logistikziel'], [
            ['Entwicklung', 'ausgereifte Produkte (mehrmaliges Ändern), neuester technischer Stand (Typen- und Teilevielfalt)', 'wenig Änderungen, Standardisierung'],
            ['Vertrieb', 'Kundenwünsche erfüllen (Variantenvielfalt), hohe Lieferbereitschaft', 'Variantenbeschränkung, lange Lieferzeiten akzeptieren, niedrige Bestände'],
            ['Fertigung', 'hohe und gleichmäßige Auslastung (Kapazitätsvorhalt, große Puffer und Lose)', 'Abbau von Überkapazitäten, kundenspezifische Fertigung'],
            ['Beschaffung', 'Preisvorteile (große Bestellmengen), hohe Versorgungssicherheit (viele Lieferanten)', 'kleine Anlieferungsmengen, kurze Wiederbeschaffungszeit']])
        + klausur_hinweis('Der Konflikt Lagerkosten gegen Beschaffungskosten ist der Ausgangspunkt der optimalen Bestellmenge (Andler, Oberthema 3).'),
    merk='Zielkonflikte: zwischen den Dimensionen (Kosten, Qualität, Lieferleistung), innerhalb einer Dimension (Lagerkosten vs. Beschaffungskosten) und mit anderen Funktionen (Entwicklung: neuester Stand vs. Standardisierung; Vertrieb: Varianten vs. Beschränkung; Fertigung: große Lose vs. niedrige Bestände; Beschaffung: große Mengen vs. kleine Anlieferung).',
    exam='Zielkonflikt erklären und mit Beispiel belegen; Lager- gegen Beschaffungskosten.',
    fehler=['Nur Konflikte zwischen den drei Ecken nennen und den Konflikt innerhalb der Kosten übersehen.'],
    src='Folien 24–25')

# ---------------------------------------------------------------- 4 Materialkosten und ROI
def roi_baum(u, mk, sk, kap, titel):
    g = u - mk - sk; skos = mk + sk; ur = g / u * 100; ku = u / kap; roi = ur * ku
    f = lambda x: f'{x:.2f}'.rstrip('0').rstrip('.').replace('.', ',')
    k = lambda x, y, w, t, tip, art='card': box(x, y, w, 44, t, size=12, art=art, tip=tip)
    v = lambda x1, y1, x2, y2: strich(x1, y1, x2, y2, 'var(--axis2)', 1.4, False)
    return svg(360, 336,
        k(120, 4, 120, f'ROI\n{f(roi)} %', f'ROI = Umsatzrentabilität × Kapitalumschlag = {f(ur)} % × {f(ku)} = {f(roi)} %.', 'hl')
        + k(18, 74, 136, f'Umsatzrentabilität\n{f(ur)} %', f'Umsatzrentabilität = Gewinn / Umsatz = {g} / {u} = {f(ur)} %.')
        + k(206, 74, 136, f'Kapitalumschlag\n{f(ku)}', f'Kapitalumschlag = Umsatz / betriebsnotwendiges Kapital = {u} / {kap} = {f(ku)}.')
        + k(4, 146, 82, f'Gewinn\n{g}', f'Gewinn = Umsatz − Selbstkosten = {u} − {skos} = {g} Mio. €.')
        + k(96, 146, 76, f'Umsatz\n{u}', 'Umsatz in Mio. €.')
        + k(188, 146, 76, f'Umsatz\n{u}', 'Umsatz in Mio. €.')
        + k(280, 146, 76, f'Kapital\n{kap}', 'Betriebsnotwendiges Kapital in Mio. €.')
        + k(4, 218, 82, f'Umsatz\n{u}', 'Umsatz in Mio. €.')
        + k(110, 218, 100, f'Selbstkosten\n{skos}', f'Selbstkosten = Materialkosten + sonstige Kosten = {mk} + {sk} = {skos} Mio. €.')
        + k(110, 288, 100, f'Material\n{mk}', f'Materialkosten {mk} Mio. €. Hier setzt der Einkauf an.', 'hl' if mk != 100 else 'card')
        + k(236, 288, 100, f'Sonstige\n{sk}', f'Sonstige Kosten {sk} Mio. €.')
        + v(180, 48, 86, 74) + v(180, 48, 274, 74) + T(180, 66, '×', 14, 700)
        + v(86, 118, 45, 146) + v(86, 118, 134, 146) + T(90, 138, '÷', 14, 700)
        + v(274, 118, 226, 146) + v(274, 118, 318, 146) + T(274, 138, '÷', 14, 700)
        + v(45, 190, 45, 218) + v(45, 190, 160, 218) + T(98, 246, '−', 16, 700)
        + v(160, 262, 160, 288) + v(160, 262, 286, 288) + T(223, 316, '+', 16, 700)
        + T(354, 236, titel, 12, 700, 'end', 'var(--muted)') + T(354, 252, '(Mio. €)', 12, 400, 'end', 'var(--muted)'),
        'ROI-Baum: ' + titel, maxw=420)

t_roi = thema('materialkosten-roi', 'Materialkosten und ROI: der Hebel des Einkaufs',
    kern='Im verarbeitenden Gewerbe machen Materialkosten rund 63 % des Umsatzes aus. Der ROI (Umsatzrentabilität × Kapitalumschlag) zeigt die Hebelwirkung: Im Beispiel steigt der ROI bei 5 % weniger Materialkosten von 18,75 % auf 25 %. Um denselben Gewinn über Umsatz zu erreichen, wäre bei 7,5 % Umsatzrentabilität ein Umsatzplus von 33 % nötig. Der Einkauf hat den Kostenhebel.',
    kurz=p('Ein Unternehmen macht 200 Mio. € Umsatz, 100 Mio. € davon sind Materialkosten. Gelingt es dem Einkauf, das Material um <b>5 %</b> billiger einzukaufen, steigt der Gewinn von 15 auf 20 Mio. €.')
        + p('Wollte der Vertrieb dieselben 20 Mio. € Gewinn über mehr Umsatz holen, bräuchte er bei 7,5 % Umsatzrentabilität <b>266,67 Mio. € Umsatz</b>, also 33 % mehr. Fazit: <b>Der Einkauf hat den Kostenhebel.</b>'),
    fig=fw('Der ROI-Baum vorher und nachher. Schalte um und tippe auf die Kästen.')
        + tafeln('tf-roi', ['Ausgangslage', 'Material −5 %'], [roi_baum(200, 100, 85, 80, 'Ausgangslage'), roi_baum(200, 95, 85, 80, 'Material −5 %')]),
    figcap='nach Folien „Beispiel Ermittlung des ROI“ und „Auswirkung einer Senkung der Materialkosten um 5 %“',
    article=h3('Anteil der Materialkosten am Umsatz')
        + tabelle(['Wirtschaftszweig (Bundesbank 2024)', 'Material in % vom Umsatz', 'Personal in %'], [
            ['Verarbeitendes Gewerbe gesamt', '63,1', '18,0'], ['Metallerzeugung und -bearbeitung', '76,8', '11,9'], ['Kraftwagen und Kraftwagenteile', '69,5', '16,3'],
            ['Chemische Erzeugnisse', '64,6', '16,6'], ['Maschinenbau', '55,0', '25,7'], ['Datenverarbeitungsgeräte, Elektronik', '51,3', '27,0']])
        + p('Materialkosten sind in der Industrie der mit Abstand größte Kostenblock, mehr als dreimal so groß wie die Personalkosten.')
        + h3('Der ROI')
        + p('<b>Kennzahlensysteme sollen einen höheren Informationsgehalt als Einzelkennzahlen besitzen</b>; durch eine vorgegebene Struktur sollen Manipulationen ausgeschlossen werden (Beispiele: DuPont-Kennzahlenpyramide, ZVEI-Kennzahlensystem). <b>Der ROI ist eine Kennzahl, welche die Verzinsung des investierten (bzw. betriebsnotwendigen) Kapitals misst.</b>')
        + fx('ROI', r'\mathit{ROI} = \underbrace{\frac{\text{Gewinn}}{\text{Umsatz}}}_{\text{Umsatzrentabilität}} \cdot \underbrace{\frac{\text{Umsatz}}{\text{Kapital}}}_{\text{Kapitalumschlag}}', 'Umsatzrentabilität mal Kapitalumschlag', '7,5 % · 2,5 = 18,75 %',
             'Der Umweg über zwei Faktoren (statt einfach Gewinn/Kapital) schafft Transparenz und einen besseren Vergleich: Man sieht, ob die Rendite aus der Marge oder aus dem Kapitalumschlag kommt.')
        + bsp('Hebelwirkung: 5 % weniger Materialkosten', 'Umsatz 200, Material 100, Sonstige 85, Kapital 80 (Mio. €)', [
            ('Gewinn vorher', '200 − 100 − 85 = 15 Mio. €'), ('Umsatzrentabilität vorher', '15 / 200 = 7,5 %; ROI = 7,5 % · 2,5 = 18,75 %'),
            ('Material −5 %', '100 → 95 Mio. €, Gewinn 20 Mio. €'), ('ROI nachher', '20 / 200 = 10 %; 10 % · 2,5 = 25 % (+6,25 Prozentpunkte bzw. +33 %)'),
            ('Gleicher Gewinn über Umsatz?', '20 / x = 0,075 → x = 266,67 Mio. €: +66,67 Mio. € bzw. +33 % Umsatz')],
            'Bei 7,5 % Umsatzrentabilität entspricht eine Kostensenkung von 5 % (5 Mio. €) einer Umsatzsteigerung von 33 % (66,67 Mio. €).')
        + p('Die Selbstkosten sinken dabei nur um 2,7 % (185 → 180 Mio. €), der Gewinn steigt aber um 33 %.')
        + falle('Den ROI als Gewinn / Umsatz berechnen. Das ist nur die Umsatzrentabilität; der ROI multipliziert noch mit dem Kapitalumschlag.'),
    merk='Material ≈ 63 % vom Umsatz (verarbeitendes Gewerbe). ROI = Umsatzrentabilität × Kapitalumschlag = Gewinn/Umsatz × Umsatz/Kapital. Beispiel: 7,5 % · 2,5 = 18,75 %; Material −5 % → Gewinn 15 → 20, ROI 25 %. Gleicher Effekt über Umsatz: +33 % (266,67 Mio. €). Der Einkauf hat den Kostenhebel.',
    exam='ROI-Baum ausfüllen, Wirkung einer Materialkostensenkung rechnen, erforderliche Umsatzsteigerung bestimmen; „Warum der Umweg über zwei Faktoren?“ (Transparenz, Vergleich).',
    fehler=['ROI mit Umsatzrentabilität verwechseln.', 'Umsatzsteigerung falsch: nicht 5 %, sondern x = Gewinn / Umsatzrentabilität.'],
    src='Folien 26–31')

# ---------------------------------------------------------------- 5 Lagerkosten und Kapitalbindung
t_lager = thema('lagerkosten', 'Bestandskosten: Kapitalbindung und Lagerkosten',
    kern='Neben den Einstandspreisen beeinflusst die Materialwirtschaft die Lagerkosten: Kapitalbindung (Zinsen), Lagerraum, Personal, Abschreibungen, Transport, IT, Überalterung. Formel: Lagerkosten = durchschnittlicher Lagerwert × Planungsperiode × Lagerkostensatz. Daraus folgt das Ziel möglichst niedriger Bestände, das aber mit anderen Zielen konkurriert.',
    kurz=p('Im Lager der Neckarrad GmbH liegt Material im Wert von durchschnittlich 4,5 Mio. €. Bei einem Lagerkostensatz von 11 % pro Jahr kostet das <b>495.000 € im Jahr</b>, ohne dass ein einziges Rad mehr verkauft wird.')
        + p('Deshalb will man <b>niedrige Bestände</b>. Aber niedrige Bestände heißen öfter bestellen und höheres Fehlmengenrisiko: wieder ein Zielkonflikt, den die optimale Bestellmenge löst.'),
    fig=fw('Lagerkosten berechnen. Verschiebe die Regler.')
        + regler([('lkW', 'durchschnittlicher Lagerwert', 0.5, 10, 0.5, 4.5, 'Mio. €'), ('lkS', 'Lagerkostensatz', 4, 25, 1, 11, '% pro Jahr'), ('lkT', 'Planungsperiode', 1, 12, 1, 12, 'Monate')])
        + schritte_karten([('① Periode in Jahren', 'lkA', '#lkAt'), ('② Rechnung', 'lkB', '#lkBt'), ('③ Lagerkosten', 'lkC', '#lkCt')]),
    figcap='nach Folien „Auswirkungen von Bestandskosten“',
    article=h3('Kosten der Lagerung')
        + p('<b>Neben den Einstandspreisen beeinflusst die Materialwirtschaft die Lagerkosten.</b> Ausgewählte Kosten der Lagerung:')
        + liste(['<b>Kapitalbindung</b> (Zinskosten) der Lagerware, allein ca. 8–11 % pro Jahr in großen Unternehmen', 'Kosten für den Lagerraum (z. B. Miete)', 'Personalkosten', 'Abschreibungen', 'Transportkosten', 'DV-Kosten', 'Überalterung, Verderb'])
        + p('<b>Bei gleichmäßigem Lagerabgang können Kapitalbindung und Lagerkosten über den durchschnittlichen Lagerbestand bzw. Lagerwert und die Einstandspreise errechnet werden.</b>')
        + fx('Lagerkosten', r'K_L = \varnothing\,\text{Lagerwert} \cdot T \cdot k_L', 'durchschnittlicher Lagerwert mal Planungsperiode mal Lagerkostensatz', '4,5 Mio. € · 1 Jahr · 0,11/Jahr = 495.000 €')
        + fx('Lagerkostensatz', r'k_L = \frac{\text{Lagerkosten} \cdot 100}{\varnothing\,\text{Lagerwert}}', 'Lagerkosten in Prozent des durchschnittlichen Lagerwerts', '495.000 € · 100 / 4,5 Mio. € = 11 %')
        + h3('Folgerung')
        + p('<b>Aus dem Ziel der Reduzierung der Lagerkosten ergibt sich das Ziel möglichst niedriger Bestände! Niedrige Bestände wiederum stehen im Zielkonflikt mit weiteren Zielen der Materialwirtschaft</b> (Lieferbereitschaft, Bestellkosten). Daraus entsteht Optimierungsbedarf, z. B. die Ermittlung der optimalen Bestellmenge (Andlersche Losgrößenformel).'),
    merk='Lagerkosten: Kapitalbindung (Zinsen, ca. 8–11 %), Raum, Personal, Abschreibungen, Transport, DV, Überalterung/Verderb. K_L = Ø Lagerwert × T × k_L (4,5 Mio. × 1 × 0,11 = 495.000 €). Ziel: niedrige Bestände; Konflikt mit Lieferbereitschaft und Bestellkosten → Andler.',
    exam='Lagerkosten mit der Formel berechnen, Lagerkostenarten nennen, Zielkonflikt niedriger Bestände erklären.',
    fehler=['Mit dem Höchstbestand statt dem durchschnittlichen Lagerwert rechnen.', 'Den Lagerkostensatz in Prozent statt als Dezimalzahl einsetzen (11 statt 0,11).'],
    src='Folien 32–33')

# ---------------------------------------------------------------- 6 Bedeutungswandel
fig_wandel = svg(360, 250,
    box(4, 8, 120, 36, 'Operational', size=12, tip='Fokus auf Teilepreis: Lieferantenauswahl, Teilepreisvergleich, Preis- und Vertragsverhandlungen.')
    + box(64, 58, 120, 36, 'Standard', size=12, tip='Fokus Total Cost of Ownership: Bündeln, Lead-Buyer-Konzept, Internationalisierung, Standardinstrumente (C-Teile-Management).')
    + box(124, 108, 120, 36, 'Advanced', size=12, tip='Fokus auf den Produktpreis: aktives Management der Einkaufsorganisation, Vorzugslieferanten, Simultaneous Engineering, Konzeptwettbewerbe, Einkaufscontrolling, aktives Vertragsmanagement.')
    + box(184, 158, 172, 52, 'World Class:\nSupply-Chain-Excellence', size=12, art='hl', tip='Supply-Chain-Integration, Datenintegration/Purchasing 4.0, Materialgruppenmanagement, Lieferantenentwicklung, Supply-Risk-Management, Wertschöpfungsmanagement über die ganze Supply Chain.')
    + pfeil(64, 44, 84, 56) + pfeil(124, 94, 144, 106) + pfeil(184, 144, 210, 156)
    + T(4, 226, 'In erfolgreichen Unternehmen steht die\ngesamte Supply Chain im Fokus.', 12, 600, 'start', 'var(--muted)'),
    'Entwicklungsstufen des Einkaufs', maxw=420)

t_wandel = thema('bedeutungswandel', 'Bedeutungswandel: vom Verkäufer- zum Käufermarkt',
    kern='Nach dem Krieg herrschte ein Verkäufermarkt (Nachfrage > Angebot); spätestens ab der ersten Rezession 1972 und der Ölkrise wurde daraus ein Käufermarkt (Angebot > Nachfrage). Produktlebenszyklen und Wertschöpfungstiefe sanken, Komplexität und Internationalisierung der Einkaufsgüter stiegen: Der Einkauf wurde von der untergeordneten Funktion zur Schlüsselfunktion. Entwicklungsstufen: Operational → Standard → Advanced → World Class.',
    kurz=p('Früher hat die Neckarrad GmbH fast alles selbst gemacht. Heute kauft sie ganze Komponenten: Motor, Akku, Schaltung. Je mehr man zukauft, desto wichtiger wird der Einkauf.')
        + p('Dazu kam der Wandel vom <b>Verkäufermarkt</b> (Waren knapp) zum <b>Käufermarkt</b> (Waren im Überfluss, Wettbewerb und Kostendruck). Der Einkauf ist von der Nebenrolle zur <b>Schlüsselfunktion</b> geworden.'),
    fig=fw('Vier Entwicklungsstufen des Einkaufs. Tippe auf die Stufen.') + bild(fig_wandel),
    figcap='nach Folien „Bedeutungswandel und Folgen“',
    article=h3('From Seller’s to Buyer’s Market')
        + p('<b>Bei der Wandlung der Märkte vom Verkäufer- zum Käufermarkt ändern sich die Rollen von Marketing und Materialwirtschaft/Einkauf.</b> Zahlreiche Krisen und Marktverschiebungen stellen Materialversorgung und Profitabilität vor immer neue Herausforderungen: Ende des Zweiten Weltkriegs (1945), Währungsreform (1949), Wirtschaftswunder (50er), Ölkrise und erste Rezession (1972), Wiedervereinigung (1989), Rezession (1993), Dotcom-Blase (2000), Finanzkrise (2008), Brexit-Votum (2016), Corona-Pandemie (2020).')
        + gegen(('Verkäufermarkt (Seller’s market)', 'Nachfrage > Angebot (Supply < Demand); lange Wartezeiten auf Produkte; der Verkäufer bestimmt'),
                ('Käufermarkt (Buyer’s market)', 'Angebot > Nachfrage (Demand < Supply); Wettbewerb und Kostendruck; der Käufer bestimmt; Marketing wird wichtig'))
        + h3('Was hat sich verändert?')
        + tabelle(['Merkmal', 'Verkäufermarkt', 'Käufermarkt'], [
            ['Länge des Produktlebenszyklus', 'lang', 'kürzer'], ['eigene Wertschöpfungstiefe', 'hoch (man macht alles selbst)', 'niedriger (man kauft ganze Komponenten)'],
            ['Komplexität der Einkaufsgüter', 'niedrig', 'höher'], ['Internationalisierung der Einkaufsaktivitäten', 'gering', 'höher'],
            ['Engpassfunktion im Einkauf', 'Materialversorgung für die Produktion', 'Wettbewerb und Kostendruck'], ['Bedeutung des Einkaufs', 'untergeordnete Funktion', 'Schlüsselfunktion']])
        + p('<b>Mit veränderten Umfeldbedingungen und dem Bedeutungswandel haben die Anforderungen an Einkauf und Materialwirtschaft zugenommen</b>: verschärfter Wettbewerb, Globalisierung, gesteigerte Organisationskomplexität, gestiegene Qualifikationsanforderungen, neue DV-Tools (KI, Industrie 4.0), kürzere Entwicklungs- und Produktlebenszyklen, abnehmende Wertschöpfungstiefe, erhöhte Interdisziplinarität. Im Zentrum stehen wieder Zeit, Kosten und Qualität.')
        + h3('Entwicklungsstufen des Einkaufs')
        + tabelle(['Stufe', 'Fokus', 'Beispiele'], [
            ['Operational', 'Teilepreis (parts price)', 'Lieferantenauswahl, Teilepreisvergleich, Preis- und Vertragsverhandlungen'],
            ['Standard', 'Total Cost of Ownership', 'Bündeln, Lead-Buyer-Konzept, Internationalisierung, Standardinstrumente (C-Teile-Management)'],
            ['Advanced', 'Produktpreis (product price)', 'aktives Management der Einkaufsorganisation, Vorzugslieferanten, Simultaneous Engineering, Konzeptwettbewerbe, Einkaufscontrolling, Vertragsmanagement'],
            ['World Class', 'Supply-Chain-Excellence', 'Supply-Chain-Integration, Purchasing 4.0, Materialgruppenmanagement, Lieferantenentwicklung, Supply-Risk-Management, Wertschöpfungsmanagement über die ganze Kette']])
        + spiel('sp-markt', 'Verkäufer- oder Käufermarkt?', ['Verkäufermarkt', 'Käufermarkt'], [
            ('Nachfrage übersteigt das Angebot', 0, 'Supply < Demand.'), ('Einkauf als Schlüsselfunktion', 1, 'Wettbewerb und Kostendruck.'),
            ('hohe eigene Wertschöpfungstiefe', 0, 'Früher hat man alles selbst gemacht.'), ('kurze Produktlebenszyklen', 1, 'Heute.'), ('Engpass: Materialversorgung der Produktion', 0, 'Knappheit.')]),
    merk='Verkäufermarkt (Nachfrage > Angebot) → Käufermarkt (Angebot > Nachfrage), Wende um die erste Rezession/Ölkrise 1972. Kürzere Lebenszyklen, geringere Wertschöpfungstiefe, komplexere und internationalere Einkaufsgüter → Einkauf wird Schlüsselfunktion. Stufen: Operational (Teilepreis) → Standard (TCO) → Advanced (Produktpreis) → World Class (Supply-Chain-Excellence).',
    exam='Wandel vom Verkäufer- zum Käufermarkt und seine Folgen für den Einkauf erklären; Merkmale zuordnen.',
    fehler=['Verkäufer- und Käufermarkt vertauschen: Im Käufermarkt ist das Angebot größer, der Käufer hat die Macht.'],
    src='Folien 34–38')

KAPITEL = kapitel('k1', 'Grundlagen: Begriffe, Ziele, Bedeutung',
    'Was gehört zur Materialwirtschaft, welche Ziele verfolgt sie, und warum ist der Einkauf heute eine Schlüsselfunktion? Durchgehendes Beispiel: die Neckarrad GmbH, ein E-Bike-Hersteller in Mannheim.',
    ['Begriffe', 'Zieldreieck, 7R', 'Zielkonflikte', 'ROI-Hebel', 'Lagerkosten', 'Bedeutungswandel'],
    [t_begr, t_ziele, t_konfl, t_roi, t_lager, t_wandel])
