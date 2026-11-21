import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *

# ---------------------------------------------------------------- 1 Ursprung und Definition
fig_ursprung = svg(360, 250,
    box(4, 8, 168, 96, 'Marketing\nAnfang 1980er:\nCategory Management\nsteuert Produktgruppen\nwie Kunden sie nutzen', size=12, tip='Ursprung im Marketing Anfang der 1980er Jahre als Markenmanagement-Ansatz: Gruppen von Produkten werden danach gesteuert, wie der Konsument sie verwendet (Sortiment, Preise, Verkaufsaktivitäten). Begriff geprägt von Brian F. Harris.')
    + box(188, 8, 168, 96, 'Einkauf\nspäte 1980er:\nReaktion auf mehr\nLieferantenmacht und\nstrategischen Einkauf', size=12, tip='Im Einkauf entstand Category Management in den späten 1980er Jahren als Reaktion auf zunehmende Lieferantenmacht durch die Globalisierung und auf die Erkenntnis, dass der Einkauf eine stärkere strategische Rolle spielen sollte.')
    + box(60, 144, 240, 88, 'Materialgruppe als eigene\n„Strategische Business Unit“:\nsegmentiert nach Funktion\nund Beschaffungsmarkt', size=13, art='hl', tip='Fokus: Segmentierung der Produkte oder Dienstleistungen nach ihren Funktionen und den Märkten, auf denen sie angeboten werden. „Die Beschaffung nach Produkt- oder Handelswarengruppen ist das Herzstück jeder modernen Beschaffungsorganisation.“ (van Weele/Eßig)')
    + pfeil(88, 106, 150, 142) + pfeil(272, 106, 210, 142),
    'Ursprung des Materialgruppenmanagements', maxw=420)

t_def = thema('mgm-definition', 'Materialgruppenmanagement: Ursprung und Definition',
    kern='Materialgruppenmanagement (MGM, Category Management) stammt aus dem Marketing der 1980er und kam Ende der 1980er in den Einkauf, als Reaktion auf zunehmende Lieferantenmacht. Eine Materialgruppe ist eine Gruppe kohärenter, auf Märkten erworbener Produkte oder Dienstleistungen zur Deckung des Bedarfs interner oder externer Kunden. MGM strukturiert Waren und Dienstleistungen beschaffungsmarktorientiert und leitet daraus Strategien und Maßnahmen ab.',
    kurz=p('Die Neckarrad GmbH kauft Akkus, Motoren, Schrauben, Lacke, IT und Frachten. Statt jede Bestellung einzeln zu betrachten, bildet sie <b>Materialgruppen</b>, etwa „Akkus und Zellen“, und behandelt jede wie ein eigenes kleines Geschäft: mit Zielen, Marktanalyse und Strategie.')
        + p('Die Idee kommt aus dem Supermarkt (Category Management: „Zahnpasta“ als Kategorie) und wurde in den Einkauf übertragen.'),
    fig=fw('Vom Marketing in den Einkauf. Tippe auf die Kästen.') + bild(fig_ursprung),
    figcap='nach Folien „Anfänge des Materialgruppenmanagements“',
    article=h3('Ursprung')
        + liste(['<b>Marketing, Anfang der 1980er Jahre</b>: Category Management als Markenmanagement-Ansatz; Gruppen von Produkten werden danach gesteuert, wie der Konsument sie verwendet (Sortiment, Verkaufspreise, Verkaufsaktivitäten). Vorher übernahmen oft die Lieferanten diese Funktionen, bezogen auf „ihre“ Produkte und nicht auf die Bedürfnisse der Kunden. Der Begriff wurde von Brian F. Harris geprägt.',
                 '<b>Einkauf, späte 1980er Jahre</b>: Reaktion auf die zunehmende Lieferantenmacht als Folge der Globalisierung und auf die Erkenntnis, dass es vorteilhaft ist, wenn der Einkauf eine stärkere strategische Rolle spielt.'])
        + p('Fokus: Segmentierung der Produkte oder Dienstleistungen nach ihren Funktionen und den Märkten, auf denen sie angeboten werden; die Materialgruppe wird als eigene <b>„Strategische Business Unit“</b> behandelt. „Die Beschaffung nach Produkt- oder Handelswarengruppen ist das Herzstück jeder modernen Beschaffungsorganisation.“ (van Weele/Eßig)')
        + h3('Definitionen')
        + p('<b>Materialgruppe:</b> eine Gruppe von kohärenten, auf Märkten erworbenen Produkten oder Dienstleistungen, die im Unternehmen zur Deckung des Bedarfs interner oder externer Kunden eingesetzt werden.')
        + p('<b>Materialgruppenmanagement (MGM)</b> ist ein Instrument der Einkaufsorganisation. Dabei werden Waren und Dienstleistungen <b>beschaffungsmarktorientiert</b> strukturiert. Darauf aufbauend werden Beschaffungsstrategien für Materialgruppen und Lieferanten definiert und Maßnahmen zur Verbesserung des Ergebnisbeitrags erarbeitet.')
        + p('<b>O’Brian (2019)</b>: das Einkaufsvolumen wird nach der Funktion der Güter in Gruppen segmentiert, so dass die Gruppen die Organisation der Beschaffungsmärkte widerspiegeln; die Organisation arbeitet cross-funktional an den einzelnen Kategorien.')
        + merkliste('Wichtige Aspekte nach O’Brian', 'MGM bedeutet …', ['Segmentierung des Einkaufsvolumens', 'Bezug zu den Funktionen der Produkte', 'Bezug zu den betreffenden Beschaffungsmärkten',
                                                                     'cross-funktionale Zusammenarbeit an den Materialgruppen mit den Zielen: Einkaufsvolumen analysieren, Verwendung der Produkte, Beschaffungsmärkte und Lieferanten analysieren'])
        + h3('Strategie und Materialgruppenstrategie')
        + p('<b>Strategie</b> ist die grundsätzliche, langfristige Verhaltensweise (Maßnahmenkombination) gegenüber der Umwelt zur Verwirklichung der langfristigen Ziele. Eine <b>Materialgruppenstrategie</b> beschreibt die strategische Ausrichtung auf den jeweiligen, nach Materialgruppen abgegrenzten Beschaffungsmärkten; Aufgabe ist es, die Materialgruppenziele durch Maßnahmen oder Maßnahmenbündel zu realisieren.'),
    merk='MGM = Category Management im Einkauf (Marketing 1980er, Einkauf späte 1980er: Lieferantenmacht, strategischer Einkauf). Materialgruppe: kohärente, auf Märkten erworbene Produkte/Dienstleistungen für interne oder externe Kunden. MGM: beschaffungsmarktorientiert strukturieren, dann Strategien und Maßnahmen ableiten; Materialgruppe als Strategische Business Unit; cross-funktional.',
    exam='Definition Materialgruppe und MGM; Ursprung; Aspekte nach O’Brian.',
    fehler=['Materialgruppen nach internen Abteilungen statt nach Beschaffungsmärkten bilden.'],
    src='Folien 87–92')

# ---------------------------------------------------------------- 2 Nutzen und Ziele
t_nutzen = thema('mgm-nutzen', 'Nutzen und Ziele des Materialgruppenmanagements',
    kern='MGM steigert den Gewinn vor allem über Kostensenkung bei gleichem Umsatz (Materialkosten sind der größte Block). Kosten- und Preisreduzierungen sind die zentralen Ziele; typische Einsparungen liegen bei 1–14 %, maximal 10–20 %. Weitere Nutzenkategorien: Effektivität und Effizienz, Innovationen, geringeres Supply-Chain-Risiko, cross-funktionale Zusammenarbeit, Management des gesamten Einkaufsvolumens, strategiegeleitete Beschaffung. Jeder Nutzen hat Voraussetzungen.',
    kurz=p('Mehr Gewinn bekommt die Neckarrad GmbH auf zwei Wegen: den Kuchen vergrößern (mehr Umsatz) oder das Material-Stück des Kuchens verkleinern (weniger Kosten). Weil Material über die Hälfte des Umsatzes ausmacht, ist der zweite Weg oft der stärkere.')
        + p('Gutes MGM bringt aber <b>nicht nur Kosteneinsparungen</b>: auch Innovationen von Lieferanten, weniger Risiko und bessere Zusammenarbeit im Haus. Jeder Nutzen hat allerdings <b>Voraussetzungen</b>.'),
    fig=fw('Drei Wege zu mehr Gewinn. Schalte um.')
        + tafeln('tf-kuchen', ['heute', 'mehr Umsatz', 'weniger Material'], [
            svg(360, 130, box(4, 36, 136, 80, 'Material\n56 %', size=12, tip='Materialkosten: der größte Block.') + box(144, 36, 80, 80, 'Personal\n18 %', size=12, tip='Personalkosten.')
                + box(228, 36, 76, 80, 'sonst.\nKosten', size=12, tip='Sonstige Kosten.') + box(308, 36, 48, 80, 'Ge-\nwinn', size=12, art='hl', tip='Gewinn: das kleine Stück am Ende.')
                + T(180, 20, 'Umsatz 100 %', 13, 700), 'Ausgangslage', maxw=420),
            svg(360, 130, box(10, 36, 136, 80, 'Material\n(größer)', size=12, tip='Mehr Umsatz bei gleicher Verteilung: Alle Kosten wachsen mit.') + box(150, 36, 78, 80, 'Personal', size=12, tip='Personal wächst mit.')
                + box(232, 36, 76, 80, 'sonst.\nKosten', size=12, tip='Sonstige Kosten wachsen mit.') + box(312, 36, 44, 80, 'Ge-\nwinn', size=12, art='hl', tip='Der Gewinn wächst nur proportional: „Vergrößerung des Kuchens“ bei gleicher Verteilung der Anteile.')
                + T(180, 20, 'Umsatz +20 %, Anteile gleich', 13, 700), 'Gewinnsteigerung über Umsatz', maxw=420),
            svg(360, 130, box(4, 36, 100, 80, 'Material\n(kleiner)', size=12, tip='Kostensenkung beim Material, z. B. durch Bündelung und MGM.') + box(108, 36, 80, 80, 'Personal', size=12, tip='Unverändert.')
                + box(192, 36, 76, 80, 'sonst.\nKosten', size=12, tip='Unverändert.') + box(272, 36, 84, 80, 'Gewinn\n(größer)', size=12, art='hl', tip='Gewinnsteigerung über Kostensenkung bei gleichem Umsatz: Jeder eingesparte Euro wird Gewinn.')
                + T(180, 20, 'Umsatz gleich, Material weniger', 13, 700), 'Gewinnsteigerung über Kostensenkung', maxw=420)]),
    figcap='nach Folie „Ansätze zur Gewinnsteigerung“',
    article=h3('Ansätze zur Gewinnsteigerung')
        + liste(['Gewinnsteigerung über <b>Umsatzsteigerung</b>: „Vergrößerung des Kuchens“ bei gleicher Verteilung der Anteile.', 'Gewinnsteigerung über <b>Kostensenkung bei gleichem Umsatz</b>.',
                 'Gewinnsteigerung über eine <b>Kombination</b> aus Kostensenkung (relativ und absolut, z. B. Mengenbündelungskonzept) und Umsatzsteigerung.'])
        + h3('Ziele und Einsparungen')
        + liste(['<b>Kosten- und Preisreduzierungen sind die zentralen Ziele</b> im MGM (Befragung von Einkaufsleitern); andere Ziele wie Risikoreduzierung oder Wertsteigerung (je ca. 10 %) haben geringere Bedeutung.',
                 'Grund: Die Einkaufsleistung wird nach wie vor überwiegend über Preissenkungen und Kostenreduzierung gemessen.',
                 'Einsparungen: überwiegend 1–14 %, am häufigsten 10–14 %, kaum über 14 %. MGM kann Savings über eine große Bandbreite hervorbringen.',
                 'Prozesskosten: Jeder Bestellvorgang kostet im Schnitt ca. 135 € (2022: 105 €). „Kosten je Bestellvorgang“ ist auf operativer Ebene ein wichtiger Richtwert.'])
        + h3('Nutzenkategorien und ihre Voraussetzungen')
        + tabelle(['Nutzenkategorie', 'Nutzen durch MGM', 'Voraussetzungen'], [
            ['Kostenreduzierungen', 'max. 10–20 % (vor allem, wenn vorher schlecht gearbeitet wurde)', 'MGM konsequent implementiert; niedriger Reifegrad der MG; Wettbewerb auf dem Markt (Hebelprodukte); MG breit und gering differenziert; relativ hohe Wertschöpfung'],
            ['Effektivität und Effizienz', 'höhere Effektivität und Effizienz, weniger Verschwendung, nachhaltige Ergebnisse', 'cross-funktionale Zusammenarbeit; Instrumente (Enabler, Lean); Lieferantenintegration'],
            ['Innovationen, Wettbewerbsvorteile', 'Innovationen der Lieferanten nutzen, Differenzierung, höhere Marge, Prozessinnovationen, Synergien', 'funktionierende Lieferantenintegration; Lieferanten als Impulsgeber; Vorteile für Lieferanten sichtbar machen'],
            ['Reduzierung des Supply-Chain-Risikos', 'höhere Sicherheit, rechtzeitige Gegenmaßnahmen', 'Risikobewertung, Lieferantenbewertungen, Marktkenntnis'],
            ['cross-funktionale Zusammenarbeit', 'Einkaufs-Know-how fließt in den Wertschöpfungsprozess ein (Entwicklung, Fertigung, Qualität, Produktmanagement, Vertrieb)', 'MGM konsequent implementiert; Funktionen erkennen den Wertbeitrag des Einkaufs'],
            ['Management des gesamten Einkaufsvolumens', 'Transparenz, Genauigkeit, bessere Verhandlungsbasis (Neuvergaben mit bestehendem Geschäft verknüpfen), umfassendere Rahmenverträge', 'Spend-Analyse auf MG-Ebene; Materialgruppen klar definiert und erfasst'],
            ['strategiegeleitete Beschaffung', 'Einkauf wird als strategische Funktion wahrgenommen; Einkaufsstrategie aus Unternehmensstrategie abgeleitet', 'Einkauf auf Managementebene; Strategiebildungsprozess im Einkauf']])
        + p('<b>Um den Nutzen zu realisieren, müssen die jeweiligen Voraussetzungen gegeben sein!</b> Fazit: Gutes MGM bringt nicht nur Kosteneinsparung.'),
    merk='Gewinn über Umsatz (Kuchen vergrößern), über Kostensenkung oder Kombination. Zentrale Ziele: Kosten- und Preisreduzierung (Einkauf wird an Savings gemessen); Savings meist 1–14 %, max. 10–20 %; Bestellvorgang ≈ 135 €. Weitere Nutzen: Effizienz, Innovation, Risiko, cross-funktional, gesamtes Einkaufsvolumen, strategiegeleitet. Jeder Nutzen braucht Voraussetzungen.',
    exam='Nutzenkategorien nennen und mit Voraussetzungen verbinden; Gewinnhebel erklären.',
    fehler=['MGM nur als Sparprogramm darstellen.', 'Voraussetzungen vergessen.'],
    src='Folien 95–101')

# ---------------------------------------------------------------- 3 Zentral vs. dezentral
krit = [('Verhandlungsstärke', 1), ('Bestandsoptimierung', 1), ('Einkaufs-Know-how', 1), ('Synergien', 1),
        ('Flexibilität', 0), ('Problemorientierung', 0), ('Nähe zum Bedarfsträger', 0), ('technisches Know-how', 0)]
fig_zd = svg(360, 318,
    box(4, 4, 96, 36, 'zentral', size=13, tip='Zentraleinkauf: eine Einkaufsabteilung für das ganze Unternehmen.')
    + box(260, 4, 96, 36, 'dezentral', size=13, tip='Dezentraler Einkauf: Einkauf in den einzelnen Werken, Sparten oder Standorten.')
    + ''.join(T(50, 66 + i * 26, '+' if z else '−', 15, 800, fill='var(--primary)' if z else 'var(--muted)')
              + tpg(T(180, 66 + i * 26, k, 12, 600), f'{k}: Vorteil des {"Zentraleinkaufs" if z else "dezentralen Einkaufs"}.')
              + T(308, 66 + i * 26, '−' if z else '+', 15, 800, fill='var(--muted)' if z else 'var(--primary)') for i, (k, z) in enumerate(krit))
    + box(40, 272, 280, 42, 'MGM vereint beide:\nkooperative Beschaffungsform', size=12, art='hl', tip='Materialgruppenmanagement als kooperative Beschaffungsform für die gesamte Organisation: zentrale Bündelung und Strategie je Materialgruppe, dezentrale Nähe zum Bedarf.'),
    'Zentraler und dezentraler Einkauf', maxw=420)

t_zd = thema('zentral-dezentral', 'Zentraler oder dezentraler Einkauf? MGM verbindet beides',
    kern='Zentraleinkauf: Vorteile bei Verhandlungsstärke, Bestandsoptimierung, Einkaufs-Know-how und Synergien. Dezentraler Einkauf: Vorteile bei Flexibilität, Problemorientierung, Nähe zum Bedarfsträger und technischem Know-how. MGM vereint die Vorteile beider als kooperative Beschaffungsform für die gesamte Organisation.',
    kurz=p('Die Neckarrad GmbH hat Werke in Mannheim und Polen. Kauft jedes Werk selbst ein, ist man nah am Bedarf und flexibel, verschenkt aber Verhandlungsmacht. Kauft eine Zentrale alles, bündelt sie Mengen, ist aber weit weg von der Werkstatt.')
        + p('<b>MGM</b> verbindet beides: Je Materialgruppe gibt es eine zentrale Strategie und Bündelung, die Werke bleiben beteiligt.'),
    fig=fw('Plus und Minus je Organisationsform. Tippe auf die Kriterien.') + bild(fig_zd),
    figcap='nach Folie „MGM vereint die Vorteile des Zentraleinkaufs mit denen des dezentralen Einkaufs“',
    article=tabelle(['Kriterium', 'Zentraleinkauf', 'dezentraler Einkauf'], [[k, '+' if z else '−', '−' if z else '+'] for k, z in krit])
        + p('<b>MGM vereint die Vorteile des Zentraleinkaufs mit denen des dezentralen Einkaufs: Materialgruppenmanagement als kooperative Beschaffungsform für die gesamte Organisation.</b>')
        + spiel('sp-zd', 'Vorteil des zentralen oder des dezentralen Einkaufs?', ['zentral', 'dezentral'], [(k, 0 if z else 1, 'laut Folie ein Vorteil des ' + ('Zentraleinkaufs.' if z else 'dezentralen Einkaufs.')) for k, z in krit]),
    merk='Zentral: Verhandlungsstärke, Bestandsoptimierung, Einkaufs-Know-how, Synergien. Dezentral: Flexibilität, Problemorientierung, Nähe zum Bedarfsträger, technisches Know-how. MGM = kooperative Beschaffungsform, vereint beides.',
    exam='Vor- und Nachteile zuordnen (Multiple Choice); Rolle des MGM.',
    fehler=['Technisches Know-how dem Zentraleinkauf zuschreiben: Es sitzt vor Ort.'],
    src='Folien 102–103')

# ---------------------------------------------------------------- 4 Materialgruppen bilden
fig_markt = svg(360, 250,
    f'<ellipse cx="160" cy="136" rx="150" ry="108" style="fill:var(--pale);stroke:var(--line)" stroke-width="1.3"/>'
    + f'<ellipse cx="160" cy="166" rx="100" ry="72" style="fill:var(--card);stroke:var(--primary-2)" stroke-width="1.3"/>'
    + f'<ellipse cx="160" cy="200" rx="54" ry="36" style="fill:var(--primary);stroke:var(--primary)" stroke-width="1.3"/>'
    + tpg(T(160, 52, 'weit definierter Markt', 12, 700), 'Weit: an Anforderungen und Funktionen orientiert, global. Viele Anbieter, viele Möglichkeiten.')
    + tpg(T(160, 116, 'weiter definiert', 12, 700), 'Mittel: an Produkten und Spezifikationen orientiert, (über)regional.')
    + tpg(T(160, 204, 'eng', 13, 800, fill='var(--on-primary)'), 'Eng: Marken, sehr differenziert, Single Source. Je enger, desto weniger Möglichkeiten.')
    + T(330, 26, 'Chancen\nfür MGM', 12, 700, 'end', 'var(--muted)') + pfeil(318, 46, 318, 230) + T(326, 236, 'weniger', 12, 400, 'end', 'var(--muted)'),
    'Weite und enge Beschaffungsmärkte', maxw=420)

t_bilden = thema('materialgruppen-bilden', 'Materialgruppen bilden und abgrenzen',
    kern='Materialgruppen braucht man, um Einkaufsdaten strukturiert zu analysieren, ähnliche Bedarfe transparent zu machen, Bündelung aufzuzeigen, Strategien zu entwickeln, Verhandlungen vorzubereiten und Ziele zu definieren. Falsche Zuordnung führt zu falschen Daten, Strategien und Zielmessungen. Abgrenzung: Alle Ausgaben einer Materialgruppe beziehen sich auf einen eindeutig identifizierbaren Beschaffungsmarkt, dessen Grenzen so weit wie möglich gesteckt sind.',
    kurz=p('Wenn die Neckarrad GmbH Lithium-Zellen mal unter „Elektronik“, mal unter „Akkus“ bucht, weiß niemand, wie viel sie insgesamt dafür ausgibt. Dann kann man weder bündeln noch gut verhandeln.')
        + p('Gute Materialgruppen orientieren sich am <b>Beschaffungsmarkt</b>: Wer sind die Anbieter? Und sie sind <b>so weit wie möglich</b> gefasst, denn je enger die Gruppe, desto weniger Spielraum für Wettbewerb und Bündelung.'),
    fig=fw('Weite und enge Märkte. Tippe auf die Ringe.') + bild(fig_markt),
    figcap='nach Folie „Identifizierung und Abgrenzung der Materialgruppen – Beschaffungsmarkt“',
    article=h3('Warum Materialgruppen?')
        + liste(['um strukturierte Einkaufsdaten (Mengen, Werte, Preise …) zu analysieren', 'um überlappende und ähnliche Bedarfe transparent zu machen', 'um Bündelungsmöglichkeiten aufzuzeigen',
                 'um geeignete Strategien für die einzelnen Materialgruppen zu entwickeln', 'um im Vorfeld von Verhandlungen alle Informationen zu sammeln und aufzubereiten', 'um auf Materialebene Ziele zu definieren'])
        + p('Anforderungen: Strukturierungskriterien definieren, Materialgruppenschlüssel durchgängig und korrekt anwenden, „passender“ Differenzierungsgrad. <b>„Die“ Materialgruppenstruktur gibt es nicht!</b> Jedes Unternehmen muss eigene Strukturierungskriterien festlegen.')
        + h3('Folgen falscher Zuordnung')
        + liste(['keine Datentransparenz, unkorrekte Daten', 'Ausgangsbasis der Materialgruppenstrategie ist nicht korrekt', 'abgeleitete Strategien sind nicht korrekt', 'Zielabweichungen nicht korrekt messbar',
                 'suboptimale Vorbereitung von Verhandlungen (z. B. falsche Werte für einzelne Lieferanten)'])
        + h3('Vorgehensweise')
        + p('Zuerst die Ausgaben je Materialgruppe identifizieren. Problem: Die Daten liegen oft nicht in ausreichender Qualität vor (Ausgaben z. T. nur auf Lieferantenebene); Lösung: spezielle Software. Erste Schritte:')
        + liste(['Daten aus unterschiedlichen IT-Systemen mit IT-Experten herausfiltern', 'Bestellungen der Vergangenheit durchsehen (PO für PO)', 'von den wichtigsten Lieferanten eine Aufstellung der Lieferungen nach MG erbitten',
                 'Bedarfsträger nach den größten Bedarfen fragen', 'von gefertigten Teilen auf eingesetzte Materialien schließen', 'aufgrund von Erfahrung einzelne MG vertieft analysieren'])
        + p('<b>Fokussierung auf Chancen</b>: Pareto-Prinzip (ABC-Analyse), 80 % der Ausgaben entfallen in der Regel auf 20 % der Lieferanten; nicht alle Materialkosten analysieren, sondern adressierbare Materialgruppen bestimmen (Rest „out of scope“).')
        + h3('Abgrenzung nach dem Beschaffungsmarkt')
        + p('Die Materialgruppen müssen entsprechend den <b>Beschaffungsmärkten</b> abgegrenzt sein, nicht nur nach eigenen Ausgabenkategorien. Weit definierter Markt: an Anforderungen/Funktionen orientiert, global. Weiter definiert: an Produkten und Spezifikationen orientiert, (über)regional. Eng: Marken, sehr differenziert, Single Source. <b>Je enger die Beschaffungsmärkte definiert werden, desto weniger Möglichkeiten ergeben sich.</b>')
        + p('<b>Fazit: Grenze die Materialgruppe so ab, dass alle Ausgaben der Materialgruppe sich auf einen spezifischen und eindeutig identifizierbaren Beschaffungsmarkt beziehen, dessen Grenzen so weit wie möglich abgesteckt sind, um die Chancen des MGM zu ermöglichen.</b>')
        + bsp('Case Study: Kategorie „Reisen“', 'Flüge 16,0 · Hotels 7,4 · Reisebüro 3,8 · Mietwagen 1,5 · Bahn 0,8 · Taxis 0,9 Mio. €', [
            ('Flüge', 'eigene MG: großer Markt (Airlines), Rahmenverträge mit Fluggesellschaften'), ('Hotels', 'eigene MG: Rahmenverträge mit Hotelketten'),
            ('Reisebüro', 'Buchungsdienstleistung; kann Flug und Hotel bündeln'), ('Mietwagen, Bahn, Taxi', 'als MG „Bodentransport“ bündeln, z. B. einheitlicher Vertrag mit einem Mietwagenanbieter; Taxis sind lokal und schwer zu bündeln')],
            'Mehrere begründbare Lösungen sind möglich; entscheidend ist der Bezug zum Beschaffungsmarkt.'),
    merk='Warum MG: Daten analysieren, Bedarfe transparent, Bündelung, Strategien, Verhandlungsvorbereitung, Ziele. Falsche Zuordnung: falsche Daten, Strategien, Zielmessung, Verhandlungen. Vorgehen: Ausgaben je MG identifizieren (Daten aus IT, POs, Lieferanten, Bedarfsträger), Pareto-Fokus. Abgrenzung: eindeutiger Beschaffungsmarkt, so weit wie möglich; je enger, desto weniger Chancen.',
    exam='Gründe für Materialgruppen und Folgen falscher Zuordnung nennen; Abgrenzungskriterium formulieren; Fall (z. B. Reisen) gliedern.',
    fehler=['Materialgruppen möglichst eng bilden: Das nimmt Bündelungs- und Wettbewerbschancen.'],
    src='Folien 106–108, 117–121')

# ---------------------------------------------------------------- 5 Klassifikationsstandards
ebenen = [('Segment', '43', 'Informationstechnik'), ('Family', '20', 'Medien-/Computerzubehör'), ('Class', '17', 'Multimedia-Speicher'), ('Commodity', '03', 'CD-Taschen'), ('Business Function', '14', 'Wiederverkauf (opt.)')]
fig_unspsc = svg(360, 280,
    ''.join(box(4 + i * 6, 6 + i * 48, 120, 40, e, size=12, art='pale' if i == 4 else 'card', tip=f'Ebene {i + 1}: {e}. ' + ('Standardisiert.' if i < 4 else 'Unternehmensspezifisch ergänzbar, z. B. Wartung oder Leasing.'))
            + box(130 + i * 6, 6 + i * 48, 36, 40, c, size=13, art='hl' if i == 3 else 'card', tip=f'Zweistelliger Code der Ebene {e}: {c}.')
            + T(172 + i * 6, 30 + i * 48, b, 12, 400, 'start', 'var(--muted)') for i, (e, c, b) in enumerate(ebenen))
    + T(180, 268, 'Code: 43201703 (8-stellig) bzw. 4320170314', 12, 700),
    'UNSPSC-Ebenen am Beispiel CD-Tasche', maxw=420)

t_klass = thema('klassifikation', 'Klassifikationsstandards: UNSPSC und eCl@ss',
    kern='Produktklassifikationsstandards ordnen Objekte hierarchisch (Taxonomie). Nicht-parametrische Standards strukturieren nur (UNSPSC: 5 Ebenen Segment, Family, Class, Commodity, Business Function, je zweistellig, 8- bzw. 10-stelliger Code, v. a. USA). Parametrische Standards beschreiben zusätzlich Merkmale und Attribute (eCl@ss: 4 Stufen Sachgebiet, Hauptgruppe, Gruppe, Untergruppe, Schwerpunkt Deutschland; auch Proficl@ss, GPC, ETIM).',
    kurz=p('Damit alle im Unternehmen dieselbe Sprache sprechen, nutzt man <b>Klassifikationsstandards</b>: wie im Tierreich Säugetiere → Hunde → Dackel, nur für Produkte.')
        + p('<b>UNSPSC</b> sortiert nur (nicht-parametrisch). <b>eCl@ss</b> beschreibt die Produkte zusätzlich mit Merkmalen wie Leistung oder Größe (parametrisch).'),
    fig=fw('So entsteht ein UNSPSC-Code. Tippe auf die Ebenen.') + bild(fig_unspsc),
    figcap='nach Folien „Beispiel: UNSPSC“',
    article=h3('Zwei Arten von Standards')
        + p('<b>Produktklassifikationsstandards strukturieren verschiedene Objekte nach einheitlichen Kriterien, indem sie eine hierarchische Ordnung (Taxonomie) der Produkte in Gruppen bzw. Klassen vornehmen.</b>')
        + gegen(('nicht-parametrisch', 'nehmen nur eine Strukturierung vor; Beispiel: UNSPSC'),
                ('parametrisch', 'beschreiben die Objekte zusätzlich über Merkmale und Attribute (vordefinierte Merkmale und Wertelisten wie Leistung, Größe); dienen der Zusammenfassung und Auswahl ähnlicher Produkte; Beispiele: eCl@ss, Proficl@ss, GPC-Code, ETIM'))
        + h3('UNSPSC (United Nations Standard Products and Services Code)')
        + liste(['branchenübergreifender, international verwendeter Standard für Produkte und Dienstleistungen, v. a. im US-Raum', 'nicht-parametrisch: keine Beschreibung von Artikeln',
                 'acht- oder zehnstelliger Nummerncode; fünf Ebenen: Segment, Family, Class, Commodity, Business Function', 'die ersten vier Ebenen sind standardisiert; Business Function kann unternehmensspezifisch ergänzt werden (z. B. Wartung, Leasing)'])
        + p('Beispiel CD-Tasche: Segment 43 Informationstechnik · Family 20 Medien- und Computerzubehör · Class 17 Multimedia-Speicher · Commodity 03 CD-Taschen · (Business Function 14 Wiederverkauf) → <b>43201703</b> bzw. 4320170314.')
        + h3('eCl@ss')
        + liste(['branchenübergreifender, internationaler Standard mit Schwerpunkt in Deutschland', 'beschreibt und gruppiert Materialien, Produkte und Dienstleistungen', 'vierstufige Klassenstruktur: Sachgebiet, Hauptgruppe, Gruppe, Untergruppe',
                 'Ausprägungen und Attribute über Standardmerkmalleisten (Merkmale, Definitionen, Wertelisten) und Schlagworte: parametrisch'])
        + h3('Eigene Warengruppenstruktur')
        + p('Unternehmen ordnen Materialgruppen nach Ober- und Untergruppen, z. B. direktes Material: A Aluminium → A5 Aluminiumprofile → A51 Aluminiumrohre; indirektes Material: Logistikdienstleistungen → Landfracht → nationale Lkw-Transporte (Stückgut). Das ermöglicht Konsolidierung und ist Voraussetzung für Zuordnung, Bündelung und Controlling. Herausforderung: einheitliches Verständnis und eindeutige Zuordnung der Bauteile.')
        + spiel('sp-klass', 'UNSPSC oder eCl@ss?', ['UNSPSC', 'eCl@ss'], [
            ('fünf Ebenen bis zur Business Function', 0, 'UNSPSC.'), ('vier Stufen: Sachgebiet, Hauptgruppe, Gruppe, Untergruppe', 1, 'eCl@ss.'), ('nicht-parametrisch', 0, 'Nur Struktur.'),
            ('Merkmalleisten mit Wertelisten', 1, 'Parametrisch.'), ('Schwerpunkt Deutschland', 1, 'eCl@ss.'), ('vor allem im US-Raum verbreitet', 0, 'UNSPSC.')]),
    merk='Klassifikationsstandards = Taxonomie. Nicht-parametrisch (nur Struktur): UNSPSC, 5 Ebenen (Segment, Family, Class, Commodity, Business Function), je 2 Ziffern, 8/10 Stellen, erste 4 standardisiert, v. a. USA. Parametrisch (Merkmale, Attribute): eCl@ss (4 Stufen: Sachgebiet, Hauptgruppe, Gruppe, Untergruppe; DE), Proficl@ss, GPC, ETIM.',
    exam='Parametrisch vs. nicht-parametrisch; UNSPSC-Ebenen; eCl@ss-Stufen (Multiple Choice).',
    fehler=['UNSPSC für parametrisch halten.', 'Die Ebenenzahl verwechseln: UNSPSC 5 (4 standardisiert), eCl@ss 4.'],
    src='Folien 109–116')

# ---------------------------------------------------------------- 6 Orientierungsrahmen
phasen = [('Ziele, Nutzen, Materialgruppen', 'Abgrenzung, Ziele und Nutzen des MGM, Bildung von Materialgruppen, erste Priorisierung (Oberthema 4).'),
          ('IST-Analyse', 'Bedarfsanalyse intern (Business Requirements, Einkaufsvolumen) und Beschaffungsmarktanalyse extern (Marktstruktur, Marktmacht, ABC, XYZ). Oberthema 5.'),
          ('Strategieentwicklung', 'Zielentfaltung, Portfolios, SWOT, Strategiewahl. Oberthema 6.'),
          ('Strategieumsetzung', 'Enabler/Tools: Early Involvement, RFX, TCO, Cost Break Down, LPP, Auktionen. Oberthema 7.'),
          ('Controlling, Optimierung', 'KPIs, Controlling und kontinuierliche Optimierung.')]
fig_rahmen = svg(360, 300,
    ''.join(box(4, 6 + i * 52, 250, 38, t, size=12, art='hl' if i == 1 else 'card', tip=tip) + (pfeil(129, 45 + i * 52, 129, 57 + i * 52) if i < 4 else '') for i, (t, tip) in enumerate(phasen))
    + box(266, 6, 90, 252, 'Lieferanten-\nmanage-\nment\n(begleitet\nalle\nPhasen)', size=12, art='pale', tip='Lieferantenmanagement: Lieferantenbewertung, -klassifizierung, -entwicklung, Risiko- und Eskalationsmanagement; begleitet den ganzen Prozess.')
    + T(180, 290, 'Wegweiser durch die folgenden Oberthemen', 12, 600, fill='var(--muted)'),
    'Orientierungsrahmen des strategischen MGM', maxw=420)

t_rahmen = thema('orientierungsrahmen', 'Orientierungsrahmen: der MGM-Prozess im Überblick',
    kern='Das strategische Materialgruppenmanagement läuft in Phasen: Abgrenzung, Ziele und Nutzen sowie Bildung und Priorisierung der Materialgruppen; IST-Analyse (Bedarfsanalyse intern, Beschaffungsmarktanalyse extern); Strategieentwicklung (Zielentfaltung, Portfolios, SWOT, Strategiewahl); Strategieumsetzung mit Enablern (Early Involvement, RFX, TCO, Cost Break Down, LPP, Auktionen); Controlling und Optimierung. Das Lieferantenmanagement begleitet alles.',
    kurz=p('Für jede Materialgruppe der Neckarrad GmbH, zum Beispiel „Akkus“, läuft derselbe Prozess: erst verstehen (Was brauchen wir? Wie sieht der Markt aus?), dann eine Strategie wählen, dann umsetzen und kontrollieren.')
        + p('Dieser Rahmen ist der rote Faden der nächsten Oberthemen.'),
    fig=fw('Die Phasen des MGM. Tippe auf die Kästen.') + bild(fig_rahmen),
    figcap='nach Folie „Überblick strategisches Materialgruppenmanagement: Orientierungsrahmen und Ablaufprozess“',
    article=tabelle(['Phase', 'Inhalte', 'hier'], [
            ['Abgrenzung, Ziele, Nutzen; Bildung und Priorisierung der MG', 'Was ist MGM, was bringt es, welche Materialgruppen?', 'Oberthema 4'],
            ['IST-Analyse', 'Bedarfsanalyse intern (Einkaufsvolumen, Business Requirements, Struktur der Bedarfe); Beschaffungsmarktanalyse extern (Anbieter, Marktstruktur, Verteilung der Marktmacht; ABC-, XYZ-Analyse)', 'Oberthema 5'],
            ['Strategieentwicklung', 'Zielentfaltung, Portfolios, SWOT, Strategiewahl', 'Oberthema 6'],
            ['Strategieumsetzung (Enabler/Tools)', 'Early Involvement, RFX, TCO, Cost Break Down (KSA), LPP, Auktionen', 'Oberthema 7'],
            ['KPIs, Controlling, Optimierung', 'Zielerreichung messen und nachsteuern', ''],
            ['Lieferantenmanagement', 'begleitet alle Phasen', '']])
        + p('Das Vier-Phasen-Modell (Oberthema 5) ist die Kurzform: Analyse, Strategieableitung, Implementieren, Optimieren.'),
    merk='MGM-Prozess: Abgrenzung/Ziele/Nutzen und Bildung der MG → IST-Analyse (intern: Bedarfe, Requirements; extern: Beschaffungsmarkt, Marktmacht, ABC/XYZ) → Strategieentwicklung (Zielentfaltung, Portfolios, SWOT, Strategiewahl) → Umsetzung (Early Involvement, RFX, TCO, KSA, LPP, Auktionen) → Controlling/Optimierung; Lieferantenmanagement begleitet.',
    exam='Phasen in die richtige Reihenfolge bringen; Instrumente einer Phase zuordnen.',
    fehler=['TCO oder LPP als Analysephase einordnen: Sie sind Enabler der Umsetzung.'],
    src='Folie 124')

KAPITEL = kapitel('k4', 'Materialgruppenmanagement (MGM)',
    'Wie organisiert man einen professionellen Einkauf? Materialgruppen als „Geschäftseinheiten“ des Einkaufs: Ursprung, Nutzen, Organisation, Bildung, Klassifikation und der Prozess im Überblick.',
    ['Definition', 'Nutzen und Ziele', 'zentral/dezentral', 'MG bilden', 'Klassifikation', 'Prozess'],
    [t_def, t_nutzen, t_zd, t_bilden, t_klass, t_rahmen])
