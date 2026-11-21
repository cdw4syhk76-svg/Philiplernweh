import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *

# ---------------------------------------------------------------- 1 Vier-Phasen-Modell
phasen = [('Analyse', 'Ausgangssituation analysieren: Bedarfsanalyse (intern) und Beschaffungsmarktanalyse (extern). Ohne Ausgangsbestimmung (IST-Analyse) gibt es auch kein Ziel.'),
          ('Strategie-\nableitung', 'Aus Analyse und Zielen die Materialgruppenstrategie ableiten (Portfolios, SWOT, Strategiewahl).'),
          ('Imple-\nmentieren', 'Strategie durch Maßnahmen umsetzen (Enabler: Early Involvement, RFX, TCO, KSA, LPP …).'),
          ('Opti-\nmieren', 'Controlling und Strategieüberprüfung; kontinuierlich verbessern.')]
fig_4p = svg(360, 220,
    box(4, 6, 172, 34, 'Strategie', size=13, art='pale', tip='Phase 1 und 2 bilden die Strategiefestlegung.')
    + box(184, 6, 172, 34, 'operative Umsetzung', size=13, art='pale', tip='Phase 3 und 4 bilden die operative Umsetzung.')
    + ''.join(box(4 + i * 90, 56, 82, 110, t, size=12, art='hl' if i == 0 else 'card', tip=tip) + (pfeil(86 + i * 90, 111, 94 + i * 90, 111) if i < 3 else '') for i, (t, tip) in enumerate(phasen))
    + T(180, 196, 'alles innerhalb einer Materialgruppe', 12, 700, fill='var(--muted)'),
    'Vier-Phasen-Modell', maxw=420)

t_4p = thema('vier-phasen', 'Vier-Phasen-Modell: Analyse, Strategie, Umsetzung, Optimierung',
    kern='Strategiefestlegung und operative Umsetzung laufen innerhalb einer Materialgruppe in vier Phasen: Analyse, Strategieableitung (zusammen: Strategie), Implementieren und Optimieren (zusammen: operative Umsetzung). Ausgangspunkt sind die MGM-Ziele; die Strategieumsetzung zur Zielerreichung erfolgt durch Maßnahmen; Controlling überprüft die Strategie.',
    kurz=p('Für die Materialgruppe „Akkus“ der Neckarrad GmbH heißt das: Erst <b>analysieren</b> (Was brauchen wir, wer liefert, wer hat die Macht?), dann eine <b>Strategie ableiten</b> (z. B. zweiten Lieferanten aufbauen), sie <b>umsetzen</b> und anschließend <b>optimieren</b>.')
        + p('Merksatz der Vorlesung: Ohne Ausgangsbestimmung (IST-Analyse) gibt es auch kein Ziel.'),
    fig=fw('Die vier Phasen. Tippe auf die Kästen.') + bild(fig_4p),
    figcap='nach Folie „Vier Phasen zur Strategiefestlegung und operativen Umsetzung des MGM“',
    article=h3('Strategie und Ziele')
        + p('<b>Strategie ist die grundsätzliche, langfristige Verhaltensweise (Maßnahmenkombination) gegenüber der Umwelt zur Verwirklichung der langfristigen Ziele.</b> Ablauf: MGM-Ziele (z. B. Kostenführer werden) → Analyse der Ausgangssituation (Bedarfsanalyse, Beschaffungsmarktanalyse) → Materialgruppenstrategie → operative Umsetzung durch Maßnahmen → Controlling/Strategieüberprüfung.')
        + p('In der Praxis ist der Umsetzungsgrad sehr unterschiedlich: Nicht für alle Materialgruppen werden Strategien definiert und rollierend überarbeitet.')
        + h3('Die vier Phasen')
        + tabelle(['Phase', 'Gruppe', 'Inhalt', 'hier'], [['1 Analyse', 'Strategie', 'Business Requirements, Beschaffungsmarktanalyse, ABC/XYZ', 'dieses Oberthema'],
                                                      ['2 Strategieableitung', 'Strategie', 'Ziele, Portfolios, SWOT, Strategiewahl', 'Oberthema 6'],
                                                      ['3 Implementieren', 'operative Umsetzung', 'Enabler und Tools', 'Oberthema 7'], ['4 Optimieren', 'operative Umsetzung', 'Controlling, Verbesserung', '']])
        + p('<b>Alles findet innerhalb einer Materialgruppe statt.</b>'),
    merk='Vier Phasen je Materialgruppe: Analyse → Strategieableitung (= Strategie) → Implementieren → Optimieren (= operative Umsetzung). Strategie = grundsätzliche, langfristige Verhaltensweise zur Verwirklichung langfristiger Ziele. Ohne IST-Analyse kein Ziel.',
    exam='Phasen nennen und ordnen; Definition Strategie.',
    fehler=['Mit der Strategie beginnen, ohne die Ausgangssituation zu analysieren.'],
    src='Folien 127–129')

# ---------------------------------------------------------------- 2 Business Requirements RAQSCI
raq = [('R', 'Regulatory', 'Erfüllung der geltenden Gesetze und Anforderungen (z. B. keine verbotenen, giftigen Stoffe).'),
       ('A', 'Assurance of Supply', 'Verfügbarkeit zum benötigten Zeitpunkt: Lieferantenrisiko (Insolvenz), Kapazität, Liefertreue, Umgang mit Störungen, CSR inkl. Umwelt.'),
       ('Q', 'Quality', 'Qualitätsanforderungen: Design, Spezifikationen, Zuverlässigkeit, Fehlerquote, QM-System (z. B. ISO 9001).'),
       ('S', 'Service', 'Wie wird geliefert, welcher Service: Flexibilität, Kommunikation, Vorlauf- und Reaktionszeit, Prozesse, Support.'),
       ('C', 'Cost / Commercial', 'Kosten und kommerzielle Bedingungen: Einstandskosten, Incoterms (Lieferbedingungen), Kostenabbaustufen, Währung, TCO, Teilzahlung (Zahlungsbedingungen).'),
       ('I', 'Innovation', 'Neue und verbesserte Produkte und Prozesse: Innovationsfähigkeit, neue Technologien, Simultaneous Engineering.')]
fig_raq = svg(360, 290,
    ''.join(box(4 + i * 40, 246 - i * 44, 152, 38, f'{k}  {n}', size=12, art='hl' if k == 'R' else 'card', tip=f'{n}: {t}') for i, (k, n, t) in enumerate(raq))
    + T(4, 18, 'Stufe für Stufe: zuerst das', 12, 700, 'start') + T(4, 34, 'Fundament (Gesetze).', 12, 700, 'start')
    + T(356, 274, '„Der Einkauf ist doch nur an\nden Kosten interessiert!“ – nein.', 12, 400, 'end', 'var(--muted)'),
    'RAQSCI-Treppe', maxw=420)

t_raq = thema('business-requirements', 'Business Requirements und das RAQSCI-Modell',
    kern='Business Requirements definieren die Anforderungen der internen und externen Kunden und beantworten die Lieferantenfrage „Was können wir tun, um Sie optimal zu unterstützen?“. Sie werden nach dem RAQSCI-Modell Stufe für Stufe berücksichtigt: Regulatory, Assurance of Supply, Quality, Service, Cost/Commercial, Innovation. Sie sind Voraussetzung für RFP/RFQ, Lieferantenauswahl, Verhandlung und Lieferantenbewertung.',
    kurz=p('Bevor die Neckarrad GmbH einen neuen Akkulieferanten sucht, muss klar sein, <b>was sie eigentlich braucht</b>: Zulassung nach EU-Recht, sichere Lieferung, Qualität, Service, Preis, Innovation. Das sind die <b>Business Requirements</b>.')
        + p('Das <b>RAQSCI-Modell</b> ordnet sie wie eine Treppe: Erst das Fundament (Gesetze), ganz oben Innovation. Die Kosten stehen erst auf Stufe 5. Typisch in der Praxis: Der Lieferant erzählt, was er im Angebot hat, weil die Anforderungen schwammig sind.'),
    fig=fw('Die RAQSCI-Treppe. Tippe auf die Stufen.') + bild(fig_raq),
    figcap='nach Folie „RAQSCI Model“',
    article=h3('Was sind Business Requirements?')
        + p('<b>Business Requirements definieren die Kundenanforderungen (interne und externe Kunden).</b> Sie sind die Antwort auf die Frage eines Lieferanten nach der optimalen Lieferperformance: „Was können wir als Lieferant tun, um Sie als Kunden bei Ihrem Geschäft optimal zu unterstützen?“ Mögliche Antworten: Spezifikation und Beschreibung des Produkts, Beschaffungszeit, Lieferanforderungen, Zielpreis, Qualitätsanforderungen.')
        + p('Die Antworten müssen sorgfältig als Anforderungen verschiedener Unternehmensfunktionen abgeleitet werden. In der Praxis häufig suboptimal: Der Lieferant sagt, was er im Angebot hat, und schlägt eine Lösung aus seiner Sicht vor.')
        + p('Entstehung: aus Strategie, Kundenbedürfnis, Sourcing und Stakeholdern (alle, die Interesse am Unternehmen haben).')
        + h3('RAQSCI')
        + tabelle(['', 'Requirement', 'Inhalt und Umfang'], [[k, n, t] for k, n, t in raq])
        + p('<b>Anforderungen müssen Schritt für Schritt berücksichtigt werden</b>: Ohne Erfüllung der unteren Stufe (z. B. Gesetze) zählt die obere nicht.')
        + h3('Wofür man sie braucht')
        + p('<b>Die Festlegung der Business Requirements ist eine notwendige Voraussetzung für eine Vielzahl von Aktivitäten</b>: RFP, RFQ, Auswahlkriterien für Lieferanten, Verhandlung, Lieferantenbewertung, Lieferantenmanagement. Daran scheitert es meistens, weil die Anforderungen schwammig sind. Business Requirements „übersetzen“ die Anforderungen des Geschäfts für die Lieferantenbasis.')
        + spiel('sp-raq', 'Welche RAQSCI-Stufe?', ['R', 'A', 'Q', 'S', 'C', 'I'], [
            ('Akkus müssen die EU-Batterieverordnung erfüllen', 0, 'Regulatory.'), ('Lieferant darf nicht insolvenzgefährdet sein', 1, 'Assurance of Supply.'),
            ('Fehlerquote unter 50 ppm, ISO 9001', 2, 'Quality.'), ('Reaktion auf Reklamationen binnen 24 Stunden', 3, 'Service.'),
            ('Lieferung DDP, Zahlung 60 Tage netto', 4, 'Cost/Commercial (Incoterms, Zahlungsbedingungen).'), ('Lieferant entwickelt mit uns die nächste Zellgeneration', 5, 'Innovation.')]),
    merk='Business Requirements = Anforderungen interner und externer Kunden, Antwort auf „Was können wir für Sie tun?“. RAQSCI Stufe für Stufe: Regulatory (Gesetze), Assurance of Supply (Verfügbarkeit, Risiko, Kapazität, Liefertreue, CSR), Quality (Spezifikation, Fehlerquote, ISO 9001), Service (Flexibilität, Reaktionszeit, Support), Cost/Commercial (Einstandskosten, Incoterms, TCO, Währung), Innovation. Voraussetzung für RFP/RFQ, Auswahl, Verhandlung, Bewertung.',
    exam='RAQSCI ausschreiben und Beispiele zuordnen; Zweck der Business Requirements.',
    fehler=['Reihenfolge vertauschen: Regulatory ist das Fundament, Kosten kommen erst auf Stufe 5.', 'Assurance of Supply mit Quality verwechseln.'],
    src='Folien 132–136')

# ---------------------------------------------------------------- 3 Machtverhältnisse, Five Forces, Preisbildung
fig_5f = svg(360, 290,
    box(110, 6, 140, 52, 'potenzielle\nMarkteintritte', size=12, tip='Können neue Anbieter leicht in den Markt eintreten? Beispiel Kunststoffteile: Der Markt ist bedient, wenige Neueintritte.')
    + box(4, 118, 104, 64, 'Marktmacht\nder Vor-\nlieferanten', size=12, tip='Macht der Lieferanten unserer Lieferanten, z. B. großer Polymerhersteller für Kunststoffteile: Riesenunternehmen mit großer Macht.')
    + box(124, 112, 112, 76, 'Rivalität der\nLieferanten in\nder Material-\ngruppe', size=12, art='hl', tip='Branchenrivalität: viele mittelständische Lieferanten erzeugen hohe Rivalität, das stärkt den Einkauf.')
    + box(252, 118, 104, 64, 'Marktmacht\ndes Kunden\n(Einkauf)', size=12, tip='Hohe Einkaufsmacht bei: geringer Anzahl Nachfrager, relativ hohem Einkaufsvolumen, einfachem Lieferantenwechsel, geringer Produktdifferenzierung, unterschiedlichen (nicht koordinierten) Bezugskanälen der Lieferanten.')
    + box(110, 232, 140, 52, 'Ersatzprodukte', size=12, tip='Gibt es Substitute? Für manche Kunststoffe gibt es wenige Ersatzprodukte, das schwächt den Einkauf.')
    + pfeil(180, 60, 180, 110) + pfeil(110, 150, 122, 150) + pfeil(250, 150, 238, 150) + pfeil(180, 230, 180, 190),
    'Porters Five Forces mit Fokus Einkauf', maxw=420)

t_macht = thema('beschaffungsmarkt-macht', 'Beschaffungsmarktanalyse: Machtverhältnisse und Five Forces',
    kern='Die Machtverhältnisse auf dem Beschaffungsmarkt hängen ab von Einkaufsvolumen, Kapazitätsauslastung der Lieferanten, Substitutionsmöglichkeiten, Produktdifferenzierung und Porters Five Forces (aus dem Vertrieb auf die Beschaffung übertragen): Markteintritte, Marktmacht der Vorlieferanten, Rivalität der Lieferanten, Marktmacht des Kunden, Ersatzprodukte. Je nach Marktsituation unterscheiden sich die Preisbildungsmechanismen: Hochpreis, Budget, Cost plus, Wettbewerb, Zielkosten.',
    kurz=p('Wer hat in der Materialgruppe „Kunststoffteile“ die Macht: die Neckarrad GmbH oder ihre Lieferanten? Gibt es viele mittelständische Spritzgießer, die um Aufträge kämpfen, ist der Einkauf stark. Gibt es nur einen Polymerhersteller weltweit, ist er schwach.')
        + p('Porters <b>Five Forces</b>, eigentlich ein Werkzeug aus Strategie und Vertrieb, helfen, das systematisch zu prüfen.'),
    fig=fw('Fünf Kräfte rund um die Materialgruppe. Tippe auf die Kästen.') + bild(fig_5f),
    figcap='nach Folie „Porter’s 5 forces – Fokus Einkauf“',
    article=h3('Bestimmung der Machtverhältnisse')
        + p('Die Position im Markt und damit die Machtverhältnisse bestimmt man über:')
        + liste(['<b>Einkaufsvolumen</b> (große Mengen: A-Kunde)', '<b>Kapazitätsauslastung</b> der Lieferanten (läuft es beim Lieferanten schlecht, braucht er das Geschäft)', '<b>Substitutionsmöglichkeiten</b> (mehrere Lieferanten, von denen ich die Produkte beziehen könnte)',
                 '<b>Differenzierung</b> der Produkte', '<b>Porters Five Forces</b>'])
        + h3('Five Forces mit Fokus Einkauf')
        + tabelle(['Kraft', 'Frage', 'Beispiel Kunststoffteile'], [
            ['potenzielle Markteintritte', 'Können neue Lieferanten leicht dazukommen?', 'Markt ist bedient, wenige Neueintritte'],
            ['Marktmacht der Vorlieferanten', 'Wie mächtig sind die Lieferanten unserer Lieferanten?', 'Riesenunternehmen als Polymerhersteller (z. B. BASF): hohe Macht'],
            ['Rivalität der Lieferanten in der Materialgruppe', 'Wie stark konkurrieren die Anbieter?', 'viele Mittelständler: hohe Rivalität'],
            ['Marktmacht des Kunden (Einkauf)', 'Wie stark sind wir?', 'siehe unten'],
            ['Ersatzprodukte', 'Gibt es Substitute?', 'wenige Ersatzprodukte für Kunststoff']])
        + merkliste('Hohe Einkaufsmacht bei', 'Marktmacht des Kunden', ['geringer Anzahl Nachfrager', 'relativ hohem Einkaufsvolumen', 'einfachem Lieferantenwechsel', 'geringer Produktdifferenzierung', 'unterschiedlichen (nicht koordinierten) Bezugskanälen'])
        + p('Die Analyse wird als Tabelle dokumentiert (Kraft, Einflussfaktoren bezogen auf die Materialgruppe, Stärke des Einflusses) und mündet in Schlussfolgerungen.')
        + h3('Marktsituation und Preisbildung')
        + tabelle(['Preisbildung', 'Marktsituation', 'Merkmale, Beispiele'], [
            ['Hochpreisstrategie', 'Monopolmärkte, knappes Angebot, hohe Nachfrage (Anbietermarkt); der Lieferant bestimmt den Preis nach Zahlungsbereitschaft', 'keine Alternativen, hohe Margen, knappe Kapazität; Rohstoffe, Standardsoftware, Hochtechnologie, Patentschutz'],
            ['Budget', 'Einkaufsverhalten durch Budgets bestimmt, häufig Dienstleistungen/indirekte Bedarfe; Lieferanten orientieren sich am Budget', 'individuelle Leistungen, wenig spezifiziert, regionale Lieferanten; FCM, Marketing-Services, Engineering'],
            ['Cost plus', 'reife Märkte mit Standardverfahren und hoher Kostentransparenz; Preis = Kosten + übliche Marge (Zuschlagskalkulation)', 'z. T. Open-Book-Kalkulation, niedrige Fertigungstiefe, Fertigung nach Kundenvorgabe, Zeichnungsteile'],
            ['Wettbewerb', 'Standardgüter mit geringer Spezifizierung, z. T. Börsenhandel; Preise nach Wettbewerbsverhältnissen', 'hohes Substitutionspotenzial, hohe Transparenz, einfacher Wechsel, viele Anbieter; Strom, Transport, Verbrauchsmaterial, Drucksachen'],
            ['Zielkosten', 'hohe Spezifität und hohe Einkaufsmacht bei komplexen Gütern mit hohem Engineering-Anteil; Lieferanten erhalten Zielkosten und Anforderungen', 'hoher Wettbewerb, anspruchsvolle Serienprodukte, Lastenheft, enge Zusammenarbeit (SE); Automobil, Sondermaschinen, Luftfahrt']]),
    merk='Macht über Einkaufsvolumen, Kapazitätsauslastung der Lieferanten, Substitution, Differenzierung, Five Forces (Markteintritte, Vorlieferanten, Rivalität der Lieferanten, Macht des Kunden, Ersatzprodukte). Hohe Einkaufsmacht: wenige Nachfrager, hohes Volumen, leichter Wechsel, geringe Differenzierung. Preisbildung: Hochpreis, Budget, Cost plus, Wettbewerb, Zielkosten.',
    exam='Einflussfaktoren der Nachfragemacht nennen; Five Forces auf eine Materialgruppe anwenden.',
    fehler=['Five Forces aus Sicht des Lieferanten statt des Einkaufs auslegen.'],
    src='Folien 138–142')

# ---------------------------------------------------------------- 4 Datenbeschaffung
t_daten = thema('datenbeschaffung', 'Datenbeschaffung: intern, Lieferanten, Markt',
    kern='Quellen für die Analyse: Business Requirements, Request for Information (RFI), Internet/Desk Research, Lieferantenbesuche, Messen, Fachleute, Veröffentlichungen. Drei Blickrichtungen: interner Fokus (was, wie viel, wer, wofür), Lieferantenfokus (wer, was, wo, Entwicklung, Volumen je Lieferant) und Marktfokus (Abgrenzung, Rivalität, Trends). Marktdaten betreffen den ganzen Markt, Lieferantendaten einzelne Lieferanten.',
    kurz=p('Für die Analyse braucht die Neckarrad GmbH Daten aus drei Richtungen: aus dem <b>eigenen Haus</b> (Was haben wir gekauft? Was brauchen wir künftig?), über die <b>Lieferanten</b> (Wer liefert was, wie gut, wie stabil?) und über den <b>Markt</b> (Wie viel Rivalität? Welche Trends?).'),
    fig=fw('Drei Blickrichtungen. Schalte um.')
        + tafeln('tf-daten', ['intern', 'Lieferanten', 'Markt'], [
            svg(360, 200, ''.join(box(4 + (i % 2) * 178, 6 + (i // 2) * 64, 174, 56, t, size=12, art='hl' if i == 0 else 'card', tip=tip) for i, (t, tip) in enumerate([
                ('Was und wie viel\nwurde gekauft?', 'Quellen: Auswertungen von Bestellungen und Rechnungen.'), ('Wie sind die\nkünftigen Bedarfe?', 'Quellen: Vertriebsplanung, Strategie.'),
                ('Wer beschafft?', 'Bedarfsträger im Unternehmen.'), ('Wie werden die\nBedarfe verwendet?', 'Verwendungszweck, Spezifikation: interne Unterlagen aus Engineering und Fertigung.'),
                ('Anforderungen\n(RAQSCI)', 'Business Requirements.'), ('Qualität, Bestände,\nPreisentwicklung', 'Q-Wesen, Wareneingang, Disposition, Logistik.')])), 'Interner Fokus', maxw=420),
            svg(360, 200, ''.join(box(4 + (i % 2) * 178, 6 + (i // 2) * 64, 174, 56, t, size=12, art='hl' if i == 0 else 'card', tip=tip) for i, (t, tip) in enumerate([
                ('Wer sind die\nLieferanten?', 'Status aktiv/passiv, potenzielle neue Lieferanten.'), ('Was bieten sie an,\nwo sitzen sie?', 'Quellen: Broschüren, Internet, Messen.'),
                ('Wie entwickeln\nsie sich?', 'Finanzielle Situation, Zertifizierungen (z. B. ISO 9001).'), ('Was haben wir dort\ngekauft?', 'Einkaufsvolumen je Lieferant aus Bestellungen und Rechnungen.'),
                ('Lieferperformance,\nFlexibilität', 'Qualitätsauswertungen, Lieferantenbesuche.'), ('RFI', 'Request for Information: strukturierte Abfrage von Lieferanteninformationen.')])), 'Lieferantenfokus', maxw=420),
            svg(360, 200, ''.join(box(4 + (i % 2) * 178, 6 + (i // 2) * 64, 174, 56, t, size=12, art='hl' if i == 0 else 'card', tip=tip) for i, (t, tip) in enumerate([
                ('Wie ist der Markt\nabgegrenzt?', 'Regionale oder globale Märkte.'), ('Wie hoch ist die\nRivalität?', 'Five-Forces-Analyse.'),
                ('Welche Trends?', 'Technologische Trends, Branchenentwicklung; Expertenbefragungen.'), ('Eigene Macht\nals Kunde?', 'Einkaufsmacht.'),
                ('Quellen: Messen,\nStudien', 'Studien, Veröffentlichungen, beauftragte Marktforschung.'), ('Marktdaten ≠\nLieferantendaten', 'Marktdaten: ganzer Markt, einzelne Lieferanten spielen keine Rolle. Lieferantendaten: einzelne Lieferanten.')])), 'Marktfokus', maxw=420)]),
    figcap='nach Folien „Datenbeschaffung“',
    article=h3('Quellen der Datenbeschaffung auf Materialgruppenebene')
        + liste(['Definition der Business Requirements (u. a. Spezifikationen)', 'Request for Information (RFI)', 'Internet und Desk Research', 'Lieferantenbesuche', 'Messen', 'Fachleute (intern/extern)', 'Veröffentlichungen, Fachbücher'])
        + h3('Interner Fokus')
        + tabelle(['zu beschaffende Daten', 'Quellen'], [['Anforderungen an die MG', 'Business Requirements (RAQSCI)'], ['Bedarfsvolumen bisher', 'Auswertungen von Bestellungen, Rechnungen'],
                                                     ['Bedarfsvolumen zukünftig', 'Vertriebsplanungen, Strategie'], ['Spezifikation der Produkte', 'interne Unterlagen (Engineering, Fertigung)'],
                                                     ['Herkunft (Lieferant, Region), Preise', 'Bestellungen, Rechnungen'], ['Lagerbestände, Logistikdaten', 'Disposition, Logistik'],
                                                     ['Bedarfsträger, Verwendungszweck, technologische Veränderungen', 'Experten'], ['Erfüllung der Qualitätsanforderungen', 'interne Statistiken, Q-Wesen, Wareneingang']])
        + h3('Lieferantenfokus')
        + p('Angebotene Produkte, Einkaufsvolumen je Lieferant, Herkunft, Qualität, Zertifizierungen (z. B. ISO 9001), finanzielle Situation, Status (aktiv/passiv), potenzielle neue Lieferanten, Lieferperformance, Flexibilität. Quellen: Lieferanteninformationen, Bestellungen/Rechnungen, Qualitätsauswertungen, Lieferantenbesuche, RFI, Befragung von Experten und Stakeholdern.')
        + h3('Marktfokus')
        + p('Branchenrivalität (Five Forces), Branchenentwicklung, technologische Trends, regionale/globale Märkte, eigene Einkaufsmacht. Quellen: Brancheninformationen, Expertenbefragungen, Messen, Studien, beauftragte Marktforschung.')
        + gegen(('Marktdaten', 'Informationen über den gesamten Markt; einzelne Lieferanten spielen keine Rolle'), ('Lieferantendaten', 'Informationen über einzelne Lieferanten in dem betreffenden Markt')),
    merk='Quellen: Business Requirements, RFI, Desk Research, Lieferantenbesuche, Messen, Fachleute, Veröffentlichungen. Intern: was/wie viel gekauft, künftige Bedarfe, wer beschafft, Verwendung. Lieferanten: wer, was, wo, Entwicklung, Volumen je Lieferant. Markt: Abgrenzung, Rivalität, Trends. Marktdaten = ganzer Markt, Lieferantendaten = einzelne Lieferanten.',
    exam='Datenquellen zuordnen; Unterschied Markt- und Lieferantendaten.',
    fehler=['Markt- und Lieferantendaten gleichsetzen.'],
    src='Folien 143–147')

# ---------------------------------------------------------------- 5 ABC-Analyse
ITEMS = [('Akkuzellen', 4200), ('Motoren', 2600), ('Rahmen', 1300), ('Schaltungen', 620), ('Bremsen', 480), ('Laufräder', 360), ('Displays', 180), ('Kabel', 110), ('Schrauben', 90), ('Lack', 60)]
GES = sum(w for _, w in ITEMS)
assert GES == 10000
KUM = [sum(w for _, w in ITEMS[:i + 1]) / GES * 100 for i in range(len(ITEMS))]
KLASSE = ['A'] * 3 + ['B'] * 3 + ['C'] * 4
assert abs(KUM[2] - 81) < 1e-9 and abs(KUM[5] - 95.6) < 1e-9

def lorenz():
    X = lambda p: 50 + p * 2.9
    Y = lambda p: 222 - p * 1.86
    s = achsen(50, 222, 352, 14, '', 'Anteil am Einkaufsvolumen')
    s += rechteck(X(0), Y(100), X(30) - X(0), Y(0) - Y(100), 'var(--pale)', 'var(--line)', 0)
    for v in (50, 80, 100):
        s += strich(50, Y(v), 340, Y(v), 'var(--line)', 1, True) + T(46, Y(v) + 4, f'{v} %', 12, 400, 'end', 'var(--muted)')
    for v in (30, 60, 100):
        s += T(X(v), 238, f'{v} %', 12, 400, fill='var(--muted)')
    pts = [(X(0), Y(0))] + [(X((i + 1) * 10), Y(k)) for i, k in enumerate(KUM)]
    s += linie(pts, 'var(--primary)', 2.6)
    for i, ((n, w), k) in enumerate(zip(ITEMS, KUM)):
        s += tpg(punkt(X((i + 1) * 10), Y(k), 'var(--primary)', 4.5), f'{n}: {w} T€ ({w / 100:.1f} %), kumuliert {k:.1f} % → {KLASSE[i]}-Teil')
    s += tpg(T(X(15), Y(22), 'A', 22, 800, fill='var(--primary)'), 'A-Teile: 30 % der Positionen, 81 % des Einkaufsvolumens.')
    s += tpg(T(X(45), Y(22), 'B', 22, 800, fill='var(--primary-2)'), 'B-Teile: 30 % der Positionen, 14,6 % des Volumens.')
    s += tpg(T(X(80), Y(22), 'C', 22, 800, fill='var(--muted)'), 'C-Teile: 40 % der Positionen, nur 4,4 % des Volumens.')
    s += strich(X(30), 222, X(30), Y(100), 'var(--axis2)', 1.2) + strich(X(60), 222, X(60), Y(100), 'var(--axis2)', 1.2)
    s += T(200, 252, 'Anteil an der Anzahl der Positionen', 12, 600, fill='var(--muted)')
    return svg(360, 260, s, 'ABC-Analyse als Konzentrationskurve', maxw=420)

t_abc = thema('abc-analyse', 'ABC-Analyse',
    kern='Die ABC-Analyse (80/20-Regel, Pareto-Prinzip) gehört zu den wichtigsten Analyseinstrumenten im Einkauf: Wenige Positionen (A) bestimmen den größten Teil des Einkaufsvolumens. Vorgehen: Positionen nach Wert sortieren, Anteile kumulieren, Klassen bilden (A ca. 80 %, B ca. 15 %, C ca. 5 % des Volumens). Normstrategien: A sorgfältig und breit anfragen und lange verhandeln, B ausgewogen, C den Beschaffungsaufwand senken (C-Teile-Management).',
    kurz=p('Die Neckarrad GmbH kauft zehn Materialarten für zusammen 10 Mio. € im Jahr. Akkuzellen, Motoren und Rahmen allein machen <b>81 %</b> aus, Kabel, Schrauben und Lack zusammen nicht einmal 3 %.')
        + p('Die <b>ABC-Analyse</b> macht das sichtbar und hilft beim <b>Priorisieren</b>: Bei den A-Teilen lohnt sich jede Verhandlungsstunde, bei den C-Teilen soll das Bestellen vor allem billig und einfach sein.'),
    fig=fw('Konzentrationskurve des Beispiels. Tippe auf die Punkte und Buchstaben.') + bild(lorenz()),
    figcap='eigenes Beispiel nach dem Vorgehen der Folien „ABC-Analyse“',
    article=h3('Grundidee')
        + p('<b>Die ABC-Analyse (auch 80/20-Regel oder Pareto-Prinzip, nach Vilfredo Pareto) gehört zu den wichtigsten Analyseinstrumenten der Einkaufsarbeit. Grunderkenntnis: Wenige Teile/Materialien (A-Teile) bestimmen den größten Teil des Einkaufsvolumens. Sie hilft im Wesentlichen bei der Priorisierung.</b> A-Produkte haben den größten Effekt auf das gesamte Einkaufsvolumen.')
        + liste(['<b>Anwendungen:</b> Analyse des Einkaufsvolumens, der Materialgruppen, auf Erzeugnisebene, auf Lieferantenebene.',
                 '<b>Anlässe:</b> Beschaffungsmarktforschung/Anfragen (Breite und Häufigkeit), Vorbereitung von Preisverhandlungen, Sourcing-Strategie, Make-or-Buy, Priorisierung der Lieferantenentwicklung und im Risikomanagement.'])
        + h3('Vorgehen am Beispiel')
        + tabelle(['Rang', 'Material', 'Jahreswert (T€)', 'Anteil', 'kumuliert', 'Klasse'], [[str(i + 1), n, f'{w:,}'.replace(',', '.'), f'{w / 100:.1f} %'.replace('.', ','), f'{k:.1f} %'.replace('.', ','), KLASSE[i]] for i, ((n, w), k) in enumerate(zip(ITEMS, KUM))])
        + fluss([('1', 'Jahreswert je Position = Menge × Preis'), ('2', 'absteigend nach Wert sortieren'), ('3', 'Anteile und kumulierte Anteile berechnen'), ('4', 'Klassengrenzen setzen (ca. 80/15/5 %)')], hl=3)
        + p('Ergebnis: A = 30 % der Positionen, 81 % des Werts; B = 30 %, 14,6 %; C = 40 %, 4,4 %.')
        + h3('Normstrategien')
        + tabelle(['Klasse', 'Anteil Einkaufsvolumen', 'Normstrategie'], [
            ['A', 'ca. 80 %', 'Hauptinteresse, Priorisierung: erhebliche Sorgfalt bei der Verhandlungsvorbereitung, breiter anfragen (breitere Marktuntersuchung), sorgfältiger und länger verhandeln, gezielter Einsatz von A-Positionen als Verhandlungsargument bei der Gestaltung von Verhandlungspaketen (einfach gesagt: das große A-Volumen in die Waagschale werfen, damit der Lieferant auch bei anderen Teilen nachgibt)'],
            ['B', 'ca. 15 %', 'ausgewogenes Verhältnis zwischen Kostensenkungsbemühungen und Beschaffungsaufwand'],
            ['C', 'ca. 5 %', '„C-Teile-Management“: Beschaffungsaufwand gezielt senken, z. B. durch E-Commerce, Beschaffungsdienstleister, Vollsortimenter']])
        + falle('Nach der Stückzahl statt nach dem Wert sortieren. Die ABC-Analyse klassifiziert nach dem Wertanteil (Menge × Preis); viele Schrauben sind trotzdem C-Teile.'),
    merk='ABC = Pareto/80-20: wenige A-Teile machen den Großteil des Volumens. Vorgehen: Wert = Menge × Preis, absteigend sortieren, kumulieren, Klassen (A ≈ 80 %, B ≈ 15 %, C ≈ 5 % des Werts). Zweck: Priorisierung. Normstrategien: A sorgfältig, breit, lang verhandeln; B ausgewogen; C Aufwand senken (C-Teile-Management, E-Commerce, Dienstleister).',
    exam='ABC-Analyse aus einer Tabelle durchführen, Normstrategien nennen.',
    fehler=['Nach Stückzahl statt Wert sortieren.', 'Nicht kumulieren.'],
    src='Folien 149–150')

# ---------------------------------------------------------------- 6 XYZ und Kombination
matrix = {('X', 'A'): 'JIT-Liefe-\nrung, STS/STL', ('X', 'B'): 'Rahmen-\nvertrag mit\nAbruf', ('X', 'C'): 'Rahmen-\nvertrag, mehr\nLager',
          ('Y', 'A'): 'Rahmen-\nvertrag, Kon-\nsignationslager', ('Y', 'B'): 'Rahmen-\nvertrag mit\nAbruf', ('Y', 'C'): 'Lager, Be-\nschaffungs-\ndienstleister',
          ('Z', 'A'): 'fallweise\nDisposition', ('Z', 'B'): 'fallweise\nDisposition', ('Z', 'C'): 'Lager, Be-\nschaffungs-\ndienstleister'}
mtip = {('X', 'A'): 'AX: JIT-Belieferung, Ship-to-Stock/Ship-to-Line-Verträge, so bedarfssynchron wie möglich.', ('X', 'B'): 'BX: Rahmenverträge mit Bedarfsabruf.',
        ('X', 'C'): 'CX: Rahmenvertrag mit regelmäßiger Anlieferung und erhöhter Lagerhaltung.', ('Y', 'A'): 'AY: Rahmenverträge mit Bedarfsabruf, Konsignationslager (Ware gehört bis zur Entnahme dem Lieferanten).',
        ('Y', 'B'): 'BY: Rahmenverträge mit Bedarfsabruf.', ('Y', 'C'): 'CY: ausreichende Lagerhaltung, Beschaffungsdienstleister.', ('Z', 'A'): 'AZ: fallweise Disposition.',
        ('Z', 'B'): 'BZ: fallweise Disposition.', ('Z', 'C'): 'CZ: ausreichende Lagerhaltung, Beschaffungsdienstleister.'}
fig_abcxyz = svg(360, 300,
    ''.join(box(46 + j * 104, 4, 100, 32, k, size=14, art='pale', tip={'A': 'A: hoher Wertanteil.', 'B': 'B: mittlerer Wertanteil.', 'C': 'C: geringer Wertanteil.'}[k]) for j, k in enumerate('ABC'))
    + ''.join(box(4, 42 + i * 86, 38, 80, z, size=14, art='pale', tip={'X': 'X: kontinuierlicher Bedarf, Schwankung bis 10 %, hohe Vorhersagegenauigkeit.', 'Y': 'Y: fluktuierender Bedarf, bis 60 %, mittlere Genauigkeit.', 'Z': 'Z: diskontinuierlicher Bedarf, über 60 %, geringe Genauigkeit.'}[z]) for i, z in enumerate('XYZ'))
    + ''.join(box(46 + j * 104, 42 + i * 86, 100, 80, matrix[(z, a)], size=12, art='hl' if (z, a) == ('X', 'A') else 'card', tip=mtip[(z, a)])
            for i, z in enumerate('XYZ') for j, a in enumerate('ABC')),
    'Normstrategien der ABC-XYZ-Kombination', maxw=420)

t_xyz = thema('xyz-analyse', 'XYZ-Analyse und ABC-XYZ-Kombination', star=True,
    kern='Die XYZ-Analyse teilt nach Kontinuität und Vorhersagbarkeit des Bedarfs ein (nicht nach Wert): X kontinuierlich (Schwankung bis 10 %, Vorhersage hoch), Y fluktuierend (bis 60 %, mittel), Z diskontinuierlich (über 60 %, gering). Kombiniert mit ABC ergeben sich Normstrategien: AX Just-in-Time und Ship-to-Stock/Ship-to-Line, AY/BX/BY Rahmenverträge mit Bedarfsabruf (AY auch Konsignationslager), AZ/BZ fallweise Disposition, C-Teile Lagerhaltung und Beschaffungsdienstleister.',
    kurz=p('Akkuzellen sind bei der Neckarrad GmbH teuer (A) und werden jeden Tag gleichmäßig verbraucht (X): ideal für <b>Just-in-Time</b>. Ersatzmotoren für Reparaturen sind teuer (A), werden aber nur sporadisch gebraucht (Z): die bestellt man <b>fallweise</b>.')
        + p('Die <b>XYZ-Analyse</b> fragt nach der Regelmäßigkeit des Bedarfs, die ABC-Analyse nach dem Wert. <b>Zusammen</b> ergeben sie eine Matrix mit Normstrategien. Laut Vorlesung kann diese Kombination auch klausurrelevant sein.'),
    fig=fw('Die ABC-XYZ-Matrix. Tippe auf die Felder.') + bild(fig_abcxyz),
    figcap='nach Folien „Kombination von ABC- und XYZ-Analyse“',
    article=h3('XYZ-Analyse')
        + p('<b>Einteilungskriterium: Kontinuität und Vorhersagbarkeit des Bedarfs.</b> Die XYZ-Analyse bezieht sich auf den Bedarfsverlauf, nicht auf die Wertigkeit.')
        + tabelle(['Klasse', 'Bedarfsanfall', 'Schwankungsbreite', 'Vorhersagegenauigkeit', 'Normstrategie'], [
            ['X', 'kontinuierlicher Bedarf, gelegentliche Abweichungen, geringe Schwankungen', 'bis 10 %', 'hoch', 'wertige Teile: fertigungssynchron (Just-in-Time, Ship-to-Stock, Ship-to-Line); niederwertige: ausreichende Lagerbevorratung'],
            ['Y', 'fluktuierender Bedarf', 'bis 60 %', 'mittel', 'vorausschauende Disposition'],
            ['Z', 'diskontinuierlicher Bedarf', 'über 60 %', 'gering', 'niederwertige Convenience-Güter (z. B. Schrauben): kurzfristige Spontanbeschaffung; hochwertige: vorausschauende Disposition']])
        + h3('Kombination ABC und XYZ')
        + tabelle(['', 'A', 'B', 'C'], [
            ['X', 'JIT-Belieferung, STS/STL-Verträge (so bedarfssynchron wie möglich)', 'Rahmenverträge mit Bedarfsabruf', 'Rahmenvertrag mit regelmäßiger Anlieferung und erhöhter Lagerhaltung'],
            ['Y', 'Rahmenverträge mit Bedarfsabruf, Konsignationslager', 'Rahmenverträge mit Bedarfsabruf', 'ausreichende Lagerhaltung, Beschaffungsdienstleister'],
            ['Z', 'fallweise Disposition', 'fallweise Disposition', 'ausreichende Lagerhaltung, Beschaffungsdienstleister']])
        + liste(['<b>JIT</b> (Just-in-Time): Anlieferung genau zum Bedarfszeitpunkt.', '<b>STS</b> (Ship-to-Stock): Lieferung direkt ins Lager ohne Eingangsprüfung; <b>STL</b> (Ship-to-Line): direkt an die Fertigungslinie.',
                 '<b>Konsignationslager</b>: Lager des Lieferanten beim Kunden; die Ware gehört bis zur Entnahme dem Lieferanten.', '<b>Rahmenvertrag mit Bedarfsabruf</b>: Konditionen langfristig fest, Mengen werden nach Bedarf abgerufen.'])
        + p('Ergänzend gibt es die GMK-Analyse (auch BMS: big, medium, small), die nach der Teilegröße einteilt, z. B. gemessen an einer Europalette.')
        + klausur_hinweis('Laut Vorlesung „kann auch klausurrelevant sein“: die ABC-XYZ-Matrix mit Normstrategien ausfüllen oder einer Position eine Strategie zuordnen.')
        + spiel('sp-xyz', 'Welche Klasse?', ['AX', 'AZ', 'CX', 'CZ'], [
            ('teure Akkuzellen, täglich gleichmäßig verbraucht', 0, 'Wert hoch, Bedarf stetig: JIT.'), ('teure Ersatzmotoren, sporadisch für Reparaturen', 1, 'Wert hoch, Bedarf unregelmäßig: fallweise Disposition.'),
            ('Standardschrauben, täglich gleichmäßig', 2, 'Wert gering, stetig: Rahmenvertrag, regelmäßige Lieferung, Lager.'), ('Sonderwerkzeug für 15 €, ab und zu', 3, 'Wert gering, unregelmäßig: Lager, Dienstleister, spontan.')]),
    merk='XYZ = Kontinuität/Vorhersagbarkeit (nicht Wert): X bis 10 % Schwankung, hoch vorhersagbar; Y bis 60 %, mittel; Z über 60 %, gering. Matrix: AX JIT, STS/STL; AY Rahmenvertrag mit Abruf, Konsignationslager; BX/BY Rahmenvertrag mit Abruf; AZ/BZ fallweise Disposition; CX Rahmenvertrag mit regelmäßiger Lieferung und mehr Lager; CY/CZ Lager und Beschaffungsdienstleister.',
    exam='XYZ-Klassen beschreiben; ABC-XYZ-Matrix ausfüllen und Normstrategien zuordnen.',
    fehler=['XYZ nach dem Wert einteilen.', 'JIT bei Z-Teilen empfehlen: Unvorhersagbarer Bedarf passt nicht zu bedarfssynchroner Lieferung.'],
    src='Folien 151–153')

KAPITEL = kapitel('k5', 'Vier-Phasen-Modell und Analysephase',
    'Wie analysiert man eine Materialgruppe? Vier Phasen, Business Requirements nach RAQSCI, Machtverhältnisse und Five Forces, Datenquellen sowie ABC- und XYZ-Analyse.',
    ['Vier Phasen', 'RAQSCI', 'Marktmacht', 'Datenquellen', 'ABC', 'XYZ'],
    [t_4p, t_raq, t_macht, t_daten, t_abc, t_xyz])
