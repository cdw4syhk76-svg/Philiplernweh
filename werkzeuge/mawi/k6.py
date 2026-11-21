import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *


def portfolio(felder, xl, yl, hl=None, extra='', h=264, titel='Portfolio'):
    """Vier-Felder-Portfolio. felder = [(text, tip)] in Reihenfolge oben links, oben rechts, unten links, unten rechts."""
    x0, y0, w, hh = 56, 8, 296, h - 80
    s = ''
    pos = [(x0, y0), (x0 + w / 2, y0), (x0, y0 + hh / 2), (x0 + w / 2, y0 + hh / 2)]
    for i, ((t, tip), (x, y)) in enumerate(zip(felder, pos)):
        s += box(x + 3, y + 3, w / 2 - 6, hh / 2 - 6, t, size=12, art='hl' if i == hl else 'card', tip=tip, rx=6) if t else tpg(rechteck(x + 3, y + 3, w / 2 - 6, hh / 2 - 6, 'var(--card)', 'var(--primary-2)', 6), tip)
    s += pfeil(x0 - 4, y0 + hh + 4, x0 + w + 4, y0 + hh + 4) + pfeil(x0 - 4, y0 + hh + 4, x0 - 4, y0 - 4)
    s += T(x0 + w / 2, y0 + hh + 42, xl, 12, 700) + T(x0 + 4, y0 + hh + 24, 'niedrig', 12, 400, 'start', 'var(--muted)') + T(x0 + w, y0 + hh + 24, 'hoch', 12, 400, 'end', 'var(--muted)')
    s += f'<text x="18" y="{y0 + hh / 2:.0f}" font-size="12" font-weight="700" text-anchor="middle" transform="rotate(-90 18 {y0 + hh / 2:.0f})" style="fill:var(--ink)">{yl}</text>'
    s += T(38, y0 + 14, 'hoch', 12, 400, 'middle', 'var(--muted)') + T(38, y0 + hh - 4, 'nie-\ndrig', 12, 400, 'middle', 'var(--muted)')
    return svg(360, h, s + extra, titel, maxw=420)

# ---------------------------------------------------------------- 1 Ziele und Zielentfaltung
fig_ziele = svg(360, 250,
    f'<polygon points="180,8 20,214 340,214" style="fill:var(--pale);stroke:var(--line)" stroke-width="1.3"/>'
    + box(118, 40, 124, 46, 'Vorstand:\nGewinn, Dividende', size=12, tip='Unternehmensebene: Zieldimension Aufwand/Ertrag bzw. Gewinn; Erfolgskriterium Dividende, Aktienkurs.')
    + box(84, 98, 192, 46, 'Bereich/Werk: Kosten,\nLeistungen, Bereichsergebnis', size=12, tip='Bereichs- bzw. Werksleitung: Kosten und Leistungen, Profitbeitrag; Erfolgskriterium Bereichsergebnis.')
    + box(52, 156, 256, 46, 'Einkauf: Kosten → Entwicklung\nder Materialkosten', size=12, art='hl', tip='Einkauf: Zieldimension Kosten; Erfolgskriterium Entwicklung der Materialkosten. Auf jeder Ebene werden die Ziele operationalisiert.')
    + pfeil(352, 30, 352, 206) + T(348, 236, 'top-down, immer\nkonkreter', 12, 600, 'end', 'var(--muted)'),
    'Zielentfaltung top-down', maxw=420)

t_ziele = thema('einkaufsziele', 'Ziele und Zielentfaltung im Einkauf',
    kern='Einkaufsziele leiten sich top-down aus den strategischen und operativen Unternehmenszielen ab und werden auf jeder Ebene operationalisiert (Vorstand: Gewinn; Werk: Bereichsergebnis; Einkauf: Materialkosten). Vorgegebene Zielparameter: Preise/Mengen, Emerging-Markets-Quote, Lieferantenreduzierung, Währungssicherung, Liefersicherung. Top-3-Ziele der Praxis: Versorgungssicherheit, Savings, Lieferantenmanagement. Originäre strategische Einkaufsziele sichern langfristig Kosten, Qualität und Lieferung.',
    kurz=p('Der Vorstand der Neckarrad GmbH will 8 % Umsatzrendite. Daraus wird für das Werk ein Kostenziel, und für den Einkauf: „Materialkosten der Antriebe um 4 % senken, ohne die Versorgung zu gefährden.“ So entfalten sich Ziele <b>von oben nach unten</b> und werden immer konkreter.')
        + p('Für jede Materialgruppe gilt wieder das <b>Zieldreieck</b> aus Kosten, Qualität und Lieferleistung, und es muss ausbalanciert werden.'),
    fig=fw('Zielentfaltung von oben nach unten. Tippe auf die Ebenen.') + bild(fig_ziele),
    figcap='nach Folien „Ableitung der Einkaufsziele“ und „Planung von Materialkostenzielen“',
    article=h3('Schritte einer Materialgruppenstrategie')
        + tabelle(['Schritt', 'Leitfragen'], [
            ['Analyse der Situation', 'klare Übersicht über die Beschaffungsausgaben (Spend-Analyse); von welchen Lieferanten wird bezogen; wie viele Lieferanten je Ware/Warengruppe?'],
            ['Zielbildung und Entwicklung der Strategie', 'Produkte standardisieren und Vielfalt verringern? Zahl der Lieferanten verringern? Lieferantenbeziehungen (um)gestalten?'],
            ['Umsetzung der Strategien', 'Pläne: wer ist für welche Maßnahme zuständig, in welchem Zeitrahmen, wie wird der Fortschritt überwacht?']])
        + p('MGM-Ziele werden aus den Unternehmenszielen und den Einkaufszielen abgeleitet; die MGM-Strategie ist ein Maßnahmenbündel zur Zielerreichung.')
        + h3('Top-down-Ableitung')
        + p('<b>Die Ziele des Einkaufs leiten sich top-down aus den strategischen und operativen Zielen des Unternehmens ab. Auf der jeweiligen Ebene findet dann eine Operationalisierung der Ziele statt.</b> Wesentliche Zielparameter, die dem Einkauf vorgegeben werden:')
        + liste(['Preise/Mengen', 'EM-Quote (Anteil Einkauf in Emerging Markets)', 'Lieferantenreduzierung', 'Währungssicherung (z. B. Natural Hedging: in Ländern einkaufen, in die man auch exportiert, um Währungsschwankungen auszugleichen)', 'Liefersicherung'])
        + tabelle(['Ebene', 'Zieldimension', 'Erfolgskriterium'], [['Vorstand/Geschäftsführung', 'Aufwand/Ertrag, Gewinn', 'Dividende, Aktienkurs'], ['Bereichs-/Werksleitung', 'Kosten/Leistungen, Profitbeitrag', 'Bereichsergebnis'], ['Einkauf', 'Kosten', 'Entwicklung der Materialkosten']])
        + p('In der Praxis werden Ziele häufig top-down mit geringer Einbindung vorgegeben (Benchmark: 42 %). Die Top-3-Ziele im strategischen Einkauf: Versorgungssicherheit, Savings (Kostenreduzierung), Lieferantenmanagement.')
        + h3('Materialgruppenspezifische Ziele')
        + p('Aus dem Zieldreieck (Kosten, Qualität, Lieferleistung, Requirements in der Mitte) werden Ziele je Materialgruppe abgeleitet. Strategien als Mittel zur Zielerreichung legen fest: angestrebte Lieferantenanzahl, Anforderungen an Lieferanten/Leistungen, Standorte/geographische Verteilung der Lieferanten, Art der angestrebten Lieferantenbeziehung, angestrebte Vertragsart. <b>Ausbalancierung des Zieldreiecks!</b>')
        + tabelle(['Ecke des Zieldreiecks', 'mögliche Zielgrößen je Materialgruppe'], [
            ['Kosten', 'Materialkosten, Beschaffungskosten, Prozesskosten'],
            ['Qualität', 'Spezifikation, Erfüllung der Anforderungen'],
            ['Lieferleistung', 'Wiederbeschaffungszeiten, Termintreue, Gutteile'],
            ['Mitte: Requirements', 'die Anforderungen der Kunden, an denen sich alle drei Ecken ausrichten']])
        + h3('Originäre Einkaufsziele der strategischen Beschaffung')
        + p('<b>Langfristige Sicherung der Kosten-, Qualitäts- und Lieferziele.</b> Mögliche Einzelziele:')
        + liste(['Global-, Single-, Modular-Sourcing von A-Artikeln', 'permanente Sicherung der Materialversorgung, Streuung des Beschaffungsrisikos', 'Lieferantenentwicklung, Aufbau einer globalen Lieferantenbasis',
                 'Sicherung der technologischen Leistungsfähigkeit der Lieferanten', 'Verbesserung der Beschaffungsprozesse (Einkaufsdienstleister, C-Teile-Management)', 'Reduzierung der Bestände und Beschaffungskosten', 'Risikomanagement'])
        + h3('Originäre Einkaufsziele der operativen Beschaffung')
        + p('<b>Kurz- und mittelfristige Sicherung der Materialverfügbarkeit.</b> Während die strategische Beschaffung langfristig denkt, sorgt die operative Beschaffung dafür, dass das Material heute und in den nächsten Wochen da ist. Mögliche Einzelziele:')
        + liste(['Disposition und Prognosen, Abrufe, Anfragen, Bestellungen', 'Sicherung der Materialverfügbarkeit',
                 '<b>Desktop-Purchasing</b> (Bedarfsträger bestellen selbst am Arbeitsplatz aus elektronischen Katalogen; einfach gesagt: Bestellen wie im Onlineshop, ohne den Einkauf bei jeder Kleinigkeit)',
                 'Lieferanten-Monitoring (laufende Überwachung von Liefertreue, Qualität und Lage der Lieferanten)', 'Risk-Management'])
        + tabelle(['', 'strategische Beschaffung', 'operative Beschaffung'], [
            ['Zeithorizont', 'langfristig', 'kurz- und mittelfristig'],
            ['Kernziel', 'Sicherung der Kosten-, Qualitäts- und Lieferziele', 'Sicherung der Materialverfügbarkeit'],
            ['Beispiele', 'Global-/Single-/Modular-Sourcing, Lieferantenentwicklung', 'Disposition, Bestellungen, Desktop-Purchasing, Lieferanten-Monitoring']]),
    merk='Ziele top-down aus Unternehmenszielen, auf jeder Ebene operationalisiert (Vorstand: Gewinn/Dividende; Werk: Bereichsergebnis; Einkauf: Materialkosten). Vorgaben: Preise/Mengen, EM-Quote, Lieferantenreduzierung, Währungssicherung, Liefersicherung. Top 3: Versorgungssicherheit, Savings, Lieferantenmanagement. Originär strategisch: langfristige Sicherung von Kosten, Qualität, Lieferung; originär operativ: kurz- und mittelfristige Sicherung der Materialverfügbarkeit (Disposition, Desktop-Purchasing, Lieferanten-Monitoring, Risk-Management).',
    exam='Zielableitung top-down erklären; Zielparameter, Zielgrößen des Zieldreiecks und originäre strategische und operative Einkaufsziele nennen.',
    fehler=['Ziele bottom-up aus dem Einkauf ableiten.', 'Strategische (langfristig) und operative (kurz- und mittelfristig) Einkaufsziele vermischen.'],
    src='Folien 157–165')

# ---------------------------------------------------------------- 2 Lieferantenpyramide und Lieferantenmanagement
def pyramide(a, b, c, titel):
    return (f'<polygon points="{90 if titel == "IST" else 270},20 {14 if titel == "IST" else 194},220 {166 if titel == "IST" else 346},220" style="fill:var(--pale);stroke:var(--line)" stroke-width="1.3"/>'
            + T(90 if titel == 'IST' else 270, 14, f'{titel}', 12, 800)
            + tpg(T(90 if titel == 'IST' else 270, 90, str(a), 16, 800, fill='var(--primary)'), f'{titel}: {a} A-Lieferanten (Top-Lieferanten).')
            + tpg(T(90 if titel == 'IST' else 270, 150, str(b), 16, 800), f'{titel}: {b} B-Lieferanten.')
            + tpg(T(90 if titel == 'IST' else 270, 206, str(c), 16, 800, fill='var(--muted)'), f'{titel}: {c} C-Lieferanten.'))

fig_pyr = svg(360, 262, pyramide(2, 8, 12, 'IST') + pyramide(4, 5, 4, 'SOLL') + strich(28, 120, 152, 120, 'var(--line)', 1, False) + strich(46, 176, 134, 176, 'var(--line)', 1, False)
              + strich(208, 120, 332, 120, 'var(--line)', 1, False) + strich(226, 176, 314, 176, 'var(--line)', 1, False) + pfeil(150, 236, 210, 236)
              + T(180, 248, 'Strategie', 12, 600, fill='var(--muted)'), 'Lieferantenpyramide IST und SOLL', maxw=420)

t_pyr = thema('lieferantenpyramide', 'Einkaufsstrategie, Materialgruppenstrategie, Lieferantenpyramide',
    kern='Die Materialgruppenstrategie basiert auf der Einkaufsstrategie und diese auf den Einkaufszielen. Sie schlägt sich zwangsläufig in einer Lieferantenstrategie nieder, die sich als Lieferantenpyramide (A-, B-, C-Lieferanten) auf IST- und SOLL-Basis abbilden lässt. Das ist immer mit einer Lieferantenbewertung (z. B. Ampel) zu verbinden. Bausteine des Lieferantenmanagements: Bewertung, Klassifizierung, Auszeichnung, Entwicklung, Risiko- und Eskalationsmanagement.',
    kurz=p('Die Neckarrad GmbH hat für Kunststoffteile heute 22 Lieferanten, davon nur 2 Top-Lieferanten. Ziel: 13 Lieferanten, davon 4 Top-Lieferanten. Das zeigt die <b>Lieferantenpyramide</b> vorher (IST) und nachher (SOLL).')
        + p('Vorsicht: Wer zu stark auf wenige Lieferanten setzt, hat ein Problem, wenn einer davon insolvent wird.'),
    fig=fw('Lieferantenpyramide IST und SOLL. Tippe auf die Zahlen.') + bild(fig_pyr),
    figcap='nach Folie „Zusammenhang zwischen Einkaufsstrategie, Materialgruppenstrategie und Lieferantenmanagement“',
    article=h3('Von den Zielen zum Lieferanten')
        + fluss([('Einkaufsziele', 'abgeleitet aus Unternehmenszielen'), ('Einkaufsstrategie', 'baut auf den Einkaufszielen auf'), ('Materialgruppenstrategie', 'baut auf der Einkaufsstrategie auf'), ('Lieferantenstrategie', 'folgt zwangsläufig aus der MG-Strategie')], hl=3)
        + liste(['Die Lieferantenstrategie kann in einer <b>Lieferantenpyramide</b> auf IST- und SOLL-Basis abgebildet werden (A-, B-, C-Lieferanten).', 'Dies ist immer mit einer <b>Lieferantenbewertung</b> zu verbinden (z. B. Ampelschaltung), die die Performance der Lieferanten anhand verschiedener Kriterien misst.',
                 'Beispiel: IST 2 A-, 8 B-, 12 C-Lieferanten → SOLL 4 A-, 5 B-, 4 C-Lieferanten.'])
        + h3('Bausteine des Lieferantenmanagements')
        + liste(['Lieferantenbewertung', 'Lieferantenklassifizierung', 'Lieferantenauszeichnung', 'Lieferantenentwicklung', 'Risikomanagement', 'Eskalationsmanagement'])
        + p('<b>Die Materialgruppenstrategie ist die Basis der Lieferantenstrategie.</b>'),
    merk='Einkaufsziele → Einkaufsstrategie → Materialgruppenstrategie → Lieferantenstrategie. Lieferantenpyramide (A/B/C) als IST und SOLL, immer mit Lieferantenbewertung (Ampel). Lieferantenmanagement: Bewertung, Klassifizierung, Auszeichnung, Entwicklung, Risiko-, Eskalationsmanagement.',
    exam='Zusammenhang der Strategieebenen erklären; Lieferantenpyramide deuten.',
    fehler=['Lieferantenstrategie unabhängig von der Materialgruppenstrategie festlegen.'],
    src='Folien 166–167')

# ---------------------------------------------------------------- 3 Portfolio-Grundlagen und BCG
bcg = portfolio([('Question Marks\nselektieren', 'Fragezeichen: hohes Marktwachstum, niedriger relativer Marktanteil. Normstrategie: selektieren, durch Investitionen zum Star ausbauen oder desinvestieren.'),
                 ('Stars\ninvestieren', 'Stars: hohes Wachstum, hoher Marktanteil. Normstrategie: investieren, Wachstum durch weitere Investitionen, Marktführerschaft anstreben.'),
                 ('Poor Dogs\ndesinvestieren', 'Arme Hunde: niedriges Wachstum, niedriger Marktanteil, wenig Gewinn. Normstrategie: desinvestieren, Produkte aus dem Programm nehmen, evtl. Outsourcing.'),
                 ('Cash Cows\nabschöpfen', 'Melkkühe: niedriges Wachstum, hoher Marktanteil. Normstrategie: abschöpfen; der Cashflow finanziert die Stars.')],
                'relativer Marktanteil', 'Marktwachstum', hl=1, titel='BCG-Portfolio')

t_pf = thema('portfolio-grundlagen', 'Portfolios: Grundlagen und BCG-Matrix',
    kern='Ein Portfolio stellt eine strategische Situation in zwei Dimensionen dar (i. d. R. eine interne Unternehmens- und eine externe Marktdimension), bewertet sie und leitet aus der Positionierung standardisierte Normstrategien ab. Herkunft: Wertpapiermanagement, in den 70ern von der Boston Consulting Group auf die Unternehmensanalyse übertragen (BCG: Question Marks, Stars, Cash Cows, Poor Dogs). Schritte: Objektauswahl, zwei Kriterien, Bewertung, Ist-Positionierung, Strategieableitung.',
    kurz=p('Ein <b>Portfolio</b> ist ursprünglich ein Bündel von Wertpapieren. In der Strategie ist es ein Vier-Felder-Bild: Zwei Achsen, jedes Objekt bekommt einen Platz, und jedes Feld hat eine <b>Normstrategie</b>.')
        + p('Das bekannteste Beispiel ist die <b>BCG-Matrix</b>. Für den Einkauf gibt es eigene Portfolios, allen voran das von <b>Kraljic</b>.'),
    fig=fw('Die BCG-Matrix. Tippe auf die Felder.') + bild(bcg),
    figcap='nach Folie „Das BCG-Portfolio und seine Normstrategien“',
    article=h3('Was ist ein Portfolio?')
        + p('<b>In einem Portfolio wird eine strategische Situation in zwei Dimensionen dargestellt, bewertet und aus der Positionierung der Betrachtungsobjekte standardisierte Normstrategien abgeleitet.</b> Eine Dimension ist in der Regel intern (Unternehmen), die andere extern (Markt). Die Portfoliotechnik ist ein wichtiges Instrument der strategischen Planung und unterstützt den Einkäufer bei der Marktbearbeitung.')
        + h3('BCG-Portfolio')
        + p('Die Anfänge liegen im Wertpapiermanagement; in den 70er Jahren übertrug die Boston Consulting Group die Technik auf die strategische Unternehmensanalyse. Achsen: Marktwachstum (wie schnell wird der Markt größer?) und relativer Marktanteil (Umsatz gegenüber dem größten Konkurrenten, kann über 100 % liegen).')
        + tabelle(['Feld', 'Lage', 'Normstrategie'], [['Question Marks', 'hohes Wachstum, niedriger Anteil', 'selektieren: zum Star ausbauen oder desinvestieren'], ['Stars', 'hohes Wachstum, hoher Anteil', 'investieren, Marktführerschaft anstreben'],
                                                       ['Cash Cows', 'niedriges Wachstum, hoher Anteil', 'abschöpfen; Cashflow finanziert die Stars'], ['Poor Dogs', 'niedriges Wachstum, niedriger Anteil', 'desinvestieren, evtl. Outsourcing']])
        + h3('Schritte zur Portfolio-Aufstellung')
        + fluss([('1 Objektauswahl', 'Materialgruppen, Märkte …'), ('2 Kriterien', 'zwei Bewertungskriterien, i. d. R. ein externer und ein interner Faktor, eindeutig definiert'), ('3 Bewertung', 'möglichst quantitativ, ggf. Schätzungen'),
                 ('4 Ist-Positionierung', 'eintragen; ggf. dritte Dimension (Umsatz) über die Symbolgröße'), ('5 Strategieableitung', 'Normstrategien ableiten, angestrebte Position mit Pfeil markieren')], hl=4),
    merk='Portfolio: zwei Dimensionen (intern/extern), Positionierung → Normstrategien. Herkunft Wertpapiere, BCG in den 70ern: Question Marks (selektieren), Stars (investieren), Cash Cows (abschöpfen), Poor Dogs (desinvestieren). Schritte: Objektauswahl, Kriterien, Bewertung, Ist-Positionierung, Strategieableitung (Pfeil zur Soll-Position).',
    exam='Portfolio-Begriff und Schritte; BCG-Felder mit Normstrategien.',
    fehler=['BCG-Achsen vertauschen: x = relativer Marktanteil, y = Marktwachstum.'],
    src='Folien 169–172')

# ---------------------------------------------------------------- 4 Kraljic
kraljic_felder = [('Hebelteile\nK: Kosten', 'Hebelteile: hoher Ergebniseinfluss, niedrige Beschaffungskomplexität. Normstrategie K (Kosten): Marktmacht einsetzen, Wettbewerb ausnutzen, Auktionen, Kostenverlagerung auf den Lieferanten, Global Sourcing, mittelfristige Verträge.'),
                  ('strategische Teile\nZ: Zusammenarbeit', 'Strategische Teile: hoher Ergebniseinfluss, hohe Komplexität. Normstrategie Z (Zusammenarbeit): genaue Bedarfsplanung und Abstimmung, Allianzen, Kooperationen, Lieferantenintegration, langfristige Verträge, Risikomanagement.'),
                  ('unkritische Teile\nP: Prozess', 'Unkritische Teile: niedriger Ergebniseinfluss, niedrige Komplexität. Normstrategie P (Prozess: Qualität und Service): Prozesskosten senken, Beschaffung automatisieren, Kataloge, Beschaffungsdienstleister, Lieferanten reduzieren, Bündelung.'),
                  ('Engpassteile\nS: Sicherstellung', 'Engpassteile: niedriger Ergebniseinfluss, hohe Komplexität. Normstrategie S (Sicherstellung der Versorgung): Sicherheitsbestände, Lieferantensubstitution, Second Source, Vorzugslieferanten, Materialsubstitution, technische Lösungen, langfristige Verträge.')]
fig_kraljic = portfolio(kraljic_felder, 'Beschaffungskomplexität (extern)', 'Ergebniseinfluss (intern)', hl=1, titel='Sourcing-Strategie-Portfolio nach Kraljic')

t_kraljic = thema('kraljic', 'Sourcing-Strategie-Portfolio nach Kraljic',
    kern='Das Sourcing-Strategie-Portfolio nach Kraljic (1983) ordnet Materialgruppen nach Ergebniseinfluss (intern, „profit impact“, nicht „spend“) und Beschaffungskomplexität (extern, im Original Beschaffungsrisiko). Vier Felder mit Normstrategien: Hebelteile (K: Kosten, Marktmacht nutzen), strategische Teile (Z: Zusammenarbeit), unkritische Teile (P: Prozesskosten senken), Engpassteile (S: Sicherstellung der Versorgung). Vorgehen: klassifizieren, Machtverhältnisse berücksichtigen, Strategie bestimmen (Ausnutzen, Ausbalancieren, Diversifizieren).',
    kurz=p('Bei der Neckarrad GmbH: Aluminiumrohre sind teuer und es gibt viele Anbieter: <b>Hebelteile</b>, hier drückt man die Preise. Akkuzellen sind teuer und es gibt nur wenige Hersteller: <b>strategische Teile</b>, hier braucht man Partnerschaft. Schrauben sind billig und überall zu haben: <b>unkritisch</b>, nur der Bestellprozess soll billig sein. Ein Spezialchip für das Display ist billig, aber nur bei einem Lieferanten: <b>Engpassteil</b>, hier geht es um Versorgungssicherheit.')
        + p('Merkhilfe: <b>K Z P S</b> – Kosten, Zusammenarbeit, Prozess, Sicherstellung.'),
    fig=fw('Das Kraljic-Portfolio. Tippe auf die Felder.') + bild(fig_kraljic),
    figcap='nach Folien „Sourcing-Strategie-Portfolio nach Kraljic (der Klassiker)“',
    article=h3('Idee')
        + p('Im MGM wird nach <b>Hebeln</b> gesucht, um die Einkaufsziele zu erreichen. Zu klären ist, ob in einer Materialgruppe Hebel bestehen und wie diese erreicht und beibehalten werden können. <b>Das Sourcing-Strategie-Portfolio geht auf Kraljic (1983) zurück. Zielsetzung: Je nach Situation der Materialgruppe wird eine geeignete Strategie abgeleitet.</b>')
        + h3('Die zwei Dimensionen')
        + tabelle(['Dimension', 'Bedeutung', 'hoch, wenn …'], [
            ['Ergebniseinfluss (intern, „Bedarf“)', 'im Original „profit impact“ (nicht „spend“!): ein relativ geringer Vorteil auf Teileebene hat bedeutenden Einfluss auf das Gesamtergebnis', 'hohes Einkaufsvolumen der MG; hoher Anteil an den Gesamtausgaben oder an den Materialkosten der Fertigteile; großer Einfluss auf die Produktqualität; technologischer Wettbewerbsvorteil'],
            ['Beschaffungskomplexität (extern, „Beschaffungsmarkt“)', 'im Original „Beschaffungsrisiko“: alle Aspekte, die die Auswahl bei der Beschaffung einschränken', 'Lieferantenwechsel schwierig; nur wenige geeignete Lieferanten; komplexe MG mit enger Zusammenarbeit (Lieferantenqualifizierung); eingeschränktes Angebot (Kapazitäten); hoher Wettbewerb auf der Nachfrageseite']])
        + h3('Felder und Normstrategien')
        + tabelle(['Feld', 'Lage', 'Normstrategie', 'Maßnahmen'], [
            ['Hebelteile', 'Einfluss hoch, Komplexität niedrig', '<b>K</b>: Kosten', 'Marktmacht einsetzen durch Ausnutzung des Wettbewerbs, Auktionen, Kostenverlagerung auf den Lieferanten, Global Sourcing, mittelfristige Vertragsbindungen'],
            ['strategische Teile', 'beides hoch', '<b>Z</b>: Zusammenarbeit', 'genaue Bedarfsplanung und Abstimmung, Allianzen, Kooperationen, Lieferantenintegration, langfristige Verträge, Risikomanagement'],
            ['unkritische Teile', 'beides niedrig', '<b>P</b>: Prozess (Qualität und Service)', 'Prozesskostenreduzierung (Automatisierung), Kataloge, Beschaffungsdienstleister, Lieferantenreduktion, Bündelung'],
            ['Engpassteile', 'Einfluss niedrig, Komplexität hoch', '<b>S</b>: Sicherstellung der Versorgung', 'Sicherheitsbestände, Lieferantensubstitution, Second Source, Vorzugslieferanten, Materialsubstitution, technische Lösungen, langfristige Verträge']])
        + h3('Vorgehen')
        + fluss([('1', 'Klassifizierung anhand des Portfolios (innerhalb der Materialgruppe, z. B. Kunststoffteile)'), ('2', 'Berücksichtigung der Machtverhältnisse im Markt'), ('3', 'Bestimmung der Strategie')], hl=2)
        + merkliste('Drei generische Strategien', 'je nach Machtposition', ['<b>Ausnutzen</b>: Stärke der eigenen Situation nutzen', '<b>Ausbalancieren</b>: die gegenwärtige Position halten', '<b>Diversifizieren</b>: Maßnahmen ergreifen, um in eine erfolgversprechendere Position zu kommen'])
        + falle('Ergebniseinfluss mit Einkaufsvolumen gleichsetzen. Gemeint ist der Einfluss auf das Gesamtergebnis („profit impact“); das Volumen ist nur ein Indikator.')
        + spiel('sp-kraljic', 'Welches Feld im Kraljic-Portfolio?', ['Hebel', 'strategisch', 'unkritisch', 'Engpass'], [
            ('Aluminiumrohre: hoher Anteil an den Kosten, viele Anbieter weltweit', 0, 'Einfluss hoch, Komplexität niedrig.'), ('Akkuzellen: teuer, nur drei qualifizierte Hersteller', 1, 'Beides hoch.'),
            ('Büromaterial', 2, 'Beides niedrig.'), ('Spezialchip, billig, aber nur ein Lieferant', 3, 'Einfluss niedrig, Komplexität hoch.'), ('Gehäuse eines Elektrogeräts, einfach zu beschaffen und relevant', 0, 'Folienbeispiel Hebel.'), ('KI-Chips, extrem teuer und schwierig zu beschaffen', 1, 'Folienbeispiel strategisch.')]),
    merk='Kraljic 1983: y = Ergebniseinfluss (intern, profit impact), x = Beschaffungskomplexität (extern, Beschaffungsrisiko). Hebel (hoch/niedrig): K Kosten, Wettbewerb nutzen. Strategisch (hoch/hoch): Z Zusammenarbeit, Partnerschaft. Unkritisch (niedrig/niedrig): P Prozesskosten senken. Engpass (niedrig/hoch): S Versorgung sichern. Vorgehen: klassifizieren, Machtverhältnisse, Strategie (Ausnutzen, Ausbalancieren, Diversifizieren).',
    exam='Portfolio zeichnen, Achsen benennen, Felder und Normstrategien zuordnen, Beispiele einordnen.',
    fehler=['Achsen vertauschen.', 'Engpassteile und strategische Teile verwechseln: Engpass hat geringen Ergebniseinfluss.', 'Bei Engpassteilen auf Preisdruck setzen statt auf Versorgungssicherheit.'],
    src='Folien 173–177, 185')

# ---------------------------------------------------------------- 5 Kraljic dynamisch, Machtverhältnisse
dyn_extra = (T(130, 28, 'Hebelteile', 12, 800) + T(278, 28, 'strategische Teile', 12, 800) + T(138, 124, 'unkritische Teile', 12, 800) + T(278, 124, 'Engpassteile', 12, 800)
             + pfeil(72, 190, 72, 40, 'var(--primary)', 2.4) + pfeil(330, 186, 168, 186, 'var(--primary)', 2.4) + pfeil(330, 66, 168, 66, 'var(--primary)', 2.4)
             + tpg(T(82, 146, 'bündeln,\nstandardisieren', 12, 700, 'start', 'var(--primary)'), 'Unkritische Teile: Volumen bündeln, standardisieren, Synergien nutzen, um sie in Richtung Hebelteile zu verändern.')
             + tpg(T(278, 176, 'Engpass eliminieren', 12, 700, 'middle', 'var(--primary)'), 'Engpassteile: Engpässe durch Änderung der Spezifikation und/oder neue Lieferanten eliminieren; wenn nicht möglich, Versorgung sicherstellen.')
             + tpg(T(278, 90, 'standardisieren', 12, 700, 'middle', 'var(--primary)'), 'Strategische Teile: durch Standardisieren in Richtung Hebelteile verändern; aktives Lieferantenmanagement bei fehlender Performance.'))
fig_dyn = portfolio([('Hebel: den Markt\nnutzen, mit den\n„Besten“', 'Hebelteile: mit den besten Lieferanten zusammenarbeiten, ohne dass sich das Teil zum strategischen Teil entwickelt; Vergaben durch Wettbewerb nutzen.'),
                     ('strategisch:\neigenes Geschäft\nweiterentwickeln', 'Strategische Teile: Weiterentwicklung des eigenen Geschäfts.'),
                     ('unkritisch:\nbündeln, effizient\nversorgen', 'Unkritische Teile: bündeln, effiziente Versorgung sicherstellen.'),
                     ('Engpass:\neliminieren,\nVersorgung sichern', 'Engpassteile: Engpässe eliminieren, Versorgung sicherstellen.')],
                    'Beschaffungskomplexität', 'Wertpotenzial', extra='', titel='Dynamische Betrachtung')

t_dyn = thema('kraljic-dynamik', 'Kraljic dynamisch: Positionen verändern, Machtverhältnisse',
    kern='Das Portfolio ist nicht statisch: Ziel ist oft, Teile in Richtung Hebelteile zu verschieben. Engpassteile: Engpass über Spezifikationsänderung oder neue Lieferanten eliminieren, sonst Versorgung sichern. Unkritische Teile: bündeln und standardisieren. Strategische Teile: standardisieren, aktives Lieferantenmanagement. IKEA-Beispiel: Bilderrahmen wanderten von unkritisch über Engpass zu Hebel und strategisch. Die Portfolioanalyse muss mit der Machtposition im Markt kombiniert werden.',
    kurz=p('Ein Spezialchip ist für die Neckarrad GmbH ein Engpassteil. Ändert die Entwicklung das Design so, dass ein Standardchip passt, gibt es plötzlich viele Anbieter: aus dem Engpassteil wird ein <b>Hebelteil</b>. Kraljic ist also auch ein Werkzeug, um <b>Positionen zu verändern</b>.')
        + p('Und: Die Einordnung allein reicht nicht. Ein kleines Steakhaus kauft „Lebensmittel“ (für es ein Hebelteil), aber bei einem Großhändler ist es ein winziger Kunde, Macht hat es keine. <b>Portfolio und Machtposition gehören zusammen.</b>'),
    fig=fw('Normstrategien in Bewegung. Tippe auf Felder und Pfeile.')
        + tafeln('tf-dyn', ['Ziele je Feld', 'Bewegungen'], [fig_dyn, portfolio([('', 'Hebelteile: Ziel vieler Bewegungen, hier lässt sich Wettbewerb nutzen.'), ('', 'Strategische Teile: standardisieren Richtung Hebel.'),
                                                                              ('', 'Unkritische Teile: bündeln Richtung Hebel.'), ('', 'Engpassteile: Engpass eliminieren Richtung unkritisch, dann Hebel.')],
                                                                             'Beschaffungskomplexität', 'Ergebniseinfluss', extra=dyn_extra, h=270, titel='Bewegungen im Portfolio')]),
    figcap='nach Folien „Dynamische Betrachtung“ und „Kraljic als Change Agent“',
    article=h3('Dynamische Betrachtung: Normstrategien je Feld')
        + tabelle(['Feld', 'Ziel', 'Maßnahmen'], [
            ['Engpassteile', 'Engpass eliminieren, Versorgung sicherstellen', 'Spezifikation ändern und/oder neue Lieferanten suchen; wenn der Engpass bleibt: Versorgung sichern'],
            ['unkritische Teile', 'bündeln, effizient versorgen', 'Volumen bündeln, standardisieren, Synergien nutzen, um die Teile Richtung Hebelteile zu verändern'],
            ['Hebelteile', 'den Markt nutzen, Kooperation mit den „Besten“', 'mit den besten Lieferanten zusammenarbeiten, ohne Entwicklung zum strategischen Teil; Vergaben über Wettbewerb'],
            ['strategische Teile', 'eigenes Geschäft weiterentwickeln', 'standardisieren Richtung Hebelteile; aktives Lieferantenmanagement bei fehlender Performance']])
        + h3('Kraljic als Change Agent: IKEA-Bilderrahmen')
        + fluss([('unkritisch', 'Holzbilderrahmen aus Asien von vielen konkurrierenden Lieferanten'), ('Engpass', 'steigende Stückzahlen: manuelle Fertigung, Qualitätsmängel, Kapazitätsengpässe, Materialprobleme'),
                 ('Hebel', 'Designänderung: MDF mit 1 mm Holzfurnier statt Massivholz; weniger Material, mehr Kapazität, bessere Qualität, mehrere Lieferanten konkurrieren'),
                 ('strategisch', 'mit einem Zulieferer hocheffiziente Industrieproduktion nahe am Absatzmarkt entwickelt; Preise sinken, Mengen steigen')], hl=3)
        + h3('Machtverhältnisse')
        + p('<b>Die Portfolioanalyse muss mit der Position im Markt (Machtverhältnis) kombiniert werden.</b> Beispiele der Vorlesung:')
        + liste(['Ein kleines lokales Restaurant und die Materialgruppe „Lebensmittel“: Ergebnisbeitrag hoch, Komplexität gering, also eigentlich Hebelteile. Aber beim Großhändler ist das Restaurant ein kleiner Kunde; die Kassiererin verhandelt nicht. Kein Hebelteil!',
                 'Ein großes, globales Unternehmen (z. B. BASF) und eine Engpass-Materialgruppe: Ergebnisbeitrag niedrig, Komplexität hoch. Wegen seiner Größe hat es aber trotzdem Macht, also kein klassisches Engpassteil.'])
        + p('Bei Hebel- und Engpassteilen ist die Machtsituation eindeutig (Einkauf bzw. Lieferant), bei unkritischen und strategischen Teilen ist sie geteilt. Unterschiedliche Machtpositionen im Markt verschieben die Verhältnisse; bestimmt wird die Position über Einkaufsvolumen, Bündelung, Kapazitätsauslastung, Substitutionsmöglichkeiten, Produktdifferenzierung und Five Forces.')
        + h3('Vom Portfolio zu Maßnahmen (Vorlage)')
        + p('Für die Praxis gibt es eine Vorlage je Materialgruppe bzw. Lieferant (mit Datum): links das Sourcing-Strategie-Portfolio mit der eingetragenen Position, rechts zwei Felder: <b>Erkenntnisse aus der Portfolio-Positionierung</b> („So sieht es aus …“) und <b>Maßnahmen zur Verbesserung der Position</b>. So wird aus der Einordnung ein konkreter Plan.'),
    merk='Dynamisch: Engpass eliminieren (Spezifikation, neue Lieferanten) oder Versorgung sichern; unkritisch bündeln/standardisieren Richtung Hebel; Hebel: Markt nutzen mit den Besten; strategisch: Geschäft weiterentwickeln, standardisieren. IKEA-Rahmen: unkritisch → Engpass → Hebel (MDF) → strategisch. Portfolio immer mit Machtposition kombinieren (Restaurant/Großhändler).',
    exam='Wanderung eines Teils im Portfolio erklären; Grenzen des Portfolios (Machtverhältnisse).',
    fehler=['Kraljic-Felder als unveränderlich betrachten.', 'Die eigene Größe/Marktmacht bei der Strategiewahl ignorieren.'],
    src='Folien 178–185, 188')

# ---------------------------------------------------------------- 6 Marktmacht-Portfolio
fig_mm = portfolio([('Emanzipations-\nstrategie', 'Lieferant stark, Abnehmer schwach: Emanzipation, z. B. zusätzliche Lieferanten aufbauen, Lieferantenwechsel, Materialsubstitution oder Eigenproduktion.'),
                    ('Geschäftsfreunde-\nstrategie', 'Beide stark: Kooperationen, Gegengeschäfte, Langzeitverträge.'),
                    ('Anpassungs- und\nSelektionsstrategie', 'Beide schwach: Geschäftsbeziehung beenden oder ausweiten; opportunistisches Verhalten je nach Gelegenheit. Beispiel: ein Unternehmen mit 300 Mitarbeitern und eine kleine Fensterputzfirma.'),
                    ('Chancenrealisie-\nrungsstrategie', 'Abnehmer stark, Lieferant schwach: Einsparungen realisieren, Konditionen verbessern, Nebenleistungswettbewerb.')],
                   'Stärke des Abnehmers (Einkäufers)', 'Stärke des Lieferanten', hl=3, titel='Marktmacht-/Einkaufsstärkenportfolio')

t_mm = thema('marktmacht-portfolio', 'Marktmacht- bzw. Einkaufsstärkenportfolio',
    kern='Das Marktmacht- bzw. Einkaufsstärkenportfolio stellt die Stärke des Abnehmers (Einkäufers) der Stärke des Lieferanten gegenüber. Normstrategien: Emanzipation (Lieferant stark, Abnehmer schwach: neue Lieferanten, Substitution, Eigenproduktion), Geschäftsfreunde (beide stark: Kooperation, Gegengeschäfte, Langzeitverträge), Anpassung und Selektion (beide schwach: Beziehung beenden oder ausweiten, opportunistisch), Chancenrealisierung (Abnehmer stark: Einsparungen, Konditionen, Nebenleistungswettbewerb).',
    kurz=p('Wie stark ist die Neckarrad GmbH gegenüber einem Lieferanten, und wie stark ist er? Ist der Lieferant übermächtig, muss man sich <b>emanzipieren</b> (zweiten Lieferanten aufbauen). Sind beide stark, wird man <b>Geschäftsfreunde</b>. Ist man selbst stark, <b>realisiert</b> man Chancen: bessere Preise und Konditionen.'),
    fig=fw('Vier Machtkonstellationen. Tippe auf die Felder.') + bild(fig_mm),
    figcap='nach Folie „Marktmacht-/Einkaufsstärkenportfolio“',
    article=tabelle(['Feld', 'Lage', 'Normstrategie'], [
            ['Emanzipationsstrategie', 'Lieferant stark, Abnehmer schwach', 'zusätzliche Lieferanten aufbauen, Lieferantenwechsel, Materialsubstitution, Eigenproduktion'],
            ['Geschäftsfreundestrategie', 'beide stark', 'Kooperationen, Gegengeschäfte, Langzeitverträge'],
            ['Anpassungs- und Selektionsstrategie', 'beide schwach', 'Geschäftsbeziehung beenden oder ausweiten; opportunistisches Verhalten je nach Gelegenheit'],
            ['Chancenrealisierungsstrategie', 'Abnehmer stark, Lieferant schwach', 'Einsparungen realisieren, Konditionsverbesserungen, Nebenleistungswettbewerb']])
        + p('Folienbeispiel für beide schwach: ein Unternehmen mit 300 Mitarbeitern, das eine kleine Reinigungsfirma zum Fensterputzen beauftragt.')
        + spiel('sp-mm', 'Welche Strategie?', ['Emanzipation', 'Geschäftsfreunde', 'Anpassung/Selektion', 'Chancenrealisierung'], [
            ('Einziger Hersteller einer Zelle diktiert die Preise; wir sind ein kleiner Kunde.', 0, 'Lieferant stark: emanzipieren.'), ('Großer Autohersteller und großer Systemlieferant', 1, 'Beide stark.'),
            ('Mittelständler und kleiner Fensterputzer', 2, 'Beide schwach.'), ('Großkonzern kauft bei vielen kleinen Spritzgießern', 3, 'Abnehmer stark.')]),
    merk='Achsen: x = Stärke des Abnehmers, y = Stärke des Lieferanten. Emanzipation (L stark, A schwach): neue Lieferanten, Substitution, Eigenproduktion. Geschäftsfreunde (beide stark): Kooperation, Gegengeschäfte, Langzeitverträge. Anpassung/Selektion (beide schwach): beenden/ausweiten, opportunistisch. Chancenrealisierung (A stark): Einsparungen, Konditionen, Nebenleistungswettbewerb.',
    exam='Felder und Normstrategien zuordnen.',
    fehler=['Emanzipation und Chancenrealisierung vertauschen.'],
    src='Folie 182')

# ---------------------------------------------------------------- 7 Risiko-Portfolio
fig_risk = portfolio([('selektive\nStrategie', 'Hohe Störungsgefahr, geringe Anfälligkeit: Versorgungssicherheit und kostengünstige Beschaffung halten sich die Waage; gleichgewichtete Strategie.'),
                      ('Investitions-\nstrategie', 'Beides hoch: Versorgungssicherheit steht im Vordergrund und kostet Geld. Langfristige Verträge, Kooperationen, Allianzen, mehr Lagerhaltung, technische Änderungen/Substitution, Dual- oder Multiple-Sourcing.'),
                      ('Abschöpfungs-\nstrategie', 'Beides niedrig: Abschöpfung durch aktive Preis- und Konditionenpolitik, Senkung von Einstandspreisen und Beschaffungskosten.'),
                      ('selektive\nStrategie', 'Geringe Störungsgefahr, hohe Anfälligkeit: gleichgewichtete Strategie.')],
                     'Anfälligkeit (intern)', 'Gefahr von Störungen (Markt)', hl=1, titel='Portfolio der Beschaffungsrisiken')

t_risk = thema('risiko-portfolio', 'Portfolio der Beschaffungsrisiken',
    kern='Das Risikoportfolio stellt die Gefahr marktbedingter Versorgungsstörungen (extern) der Anfälligkeit gegenüber Versorgungsstörungen (intern) gegenüber. Normstrategien: Investitionsstrategie (beides hoch: Versorgungssicherheit hat Vorrang und kostet Geld), Abschöpfungsstrategie (beides niedrig: Preise und Konditionen), selektive Strategie (gemischt: gleichgewichtet). Vorgehen: cross-funktionales Team, Risikoklassifizierung, Priorisierung (Akzeptanzlinie), Maßnahmen, Aktionsplan, Monitoring; ergänzt durch eine Lieferanten-Risikoanalyse.',
    kurz=p('Akkuzellen kommen fast nur aus Asien (hohe Störungsgefahr), und ohne sie steht die Montage still (hohe Anfälligkeit): Hier <b>investiert</b> die Neckarrad GmbH in Sicherheit, etwa mit einem zweiten Lieferanten und mehr Lager. Büromaterial: weder gefährdet noch kritisch, hier wird <b>abgeschöpft</b>, also auf den Preis geschaut.'),
    fig=fw('Risikoportfolio. Tippe auf die Felder.') + bild(fig_risk),
    figcap='nach Folien „Portfolio der Beschaffungsrisiken“',
    article=h3('Achsen und Normstrategien')
        + tabelle(['Feld', 'Lage', 'Normstrategie'], [
            ['Investitionsstrategie', 'Störungsgefahr hoch, Anfälligkeit hoch', 'Versorgungssicherheit steht im Vordergrund und kostet Geld: langfristige Verträge, Kooperationen, Allianzen, Erhöhung der Lagerhaltung, technische Änderungen/Substitution, Dual- oder Multiple-Sourcing'],
            ['Abschöpfungsstrategie', 'beides niedrig', 'aktive Preis- und Konditionenpolitik, Senkung von Einstandspreisen und Beschaffungskosten'],
            ['selektive Strategie', 'eines hoch, eines niedrig', 'Versorgungssicherheit und kostengünstige Beschaffung halten sich die Waage: gleichgewichtete Strategie']])
        + h3('Vorgehen bei der Risikoanalyse der Materialgruppen')
        + fluss([('1', 'cross-funktionales Team einberufen'), ('2', 'Risikoklassifizierung ableiten'), ('3', 'priorisieren (Akzeptanzlinie festlegen)'), ('4', 'Maßnahmen auf Basis der Normstrategien entwickeln'), ('5', 'Aktionsplan aufstellen'), ('6', 'Umsetzung monitoren')], hl=2)
        + p('Eine <b>Akzeptanzlinie</b> im Portfolio hilft bei der Priorisierung: Materialgruppen oberhalb der Linie brauchen Maßnahmen. Ergänzend gibt es eine <b>lieferantenbezogene Risikoanalyse</b> (Achsen: Bedeutung des Lieferanten und Risikosituation des Lieferanten; Risiko-Checklisten), Vorgehen analog.')
        + h3('Ableitung von Maßnahmen (Vorlage)')
        + p('Auch für das Risikoportfolio gibt es eine Vorlage je Materialgruppe (mit Datum): links das Risikoportfolio (Gefahr marktbedingter Versorgungsstörungen über Anfälligkeit gegenüber Versorgungsstörungen), rechts <b>Erkenntnisse aus der Risikoanalyse</b> und <b>Maßnahmen zur Reduzierung des Risikos</b>. Beispiel Akkuzellen: Erkenntnis „ein Lieferant in Asien, ohne Zellen steht die Montage“; Maßnahmen „zweite Quelle qualifizieren, Sicherheitsbestand erhöhen, langfristigen Vertrag schließen“.'),
    merk='Risikoportfolio: y = Gefahr marktbedingter Versorgungsstörungen, x = Anfälligkeit (intern). Investitionsstrategie (beides hoch: Sicherheit kostet Geld, Dual Sourcing, Lager, Allianzen), Abschöpfung (beides niedrig: Preise, Konditionen), selektiv (gemischt, gleichgewichtet). Vorgehen: Team, Klassifizierung, Akzeptanzlinie, Maßnahmen, Aktionsplan, Monitoring; plus Lieferanten-Risikoanalyse.',
    exam='Felder und Normstrategien; Vorgehen der Risikoanalyse.',
    fehler=['Bei hohem Risiko „Abschöpfung“ wählen.'],
    src='Folien 193–196')

# ---------------------------------------------------------------- 8 SWOT und Scoring
fig_swot = svg(360, 280,
    box(110, 4, 120, 36, 'Stärken (S)', size=12, art='pale', tip='Interner Fokus: Stärken in Bezug auf die Bedarfe, z. B. hohes Volumen, erfahrene Materialgruppenmanager.')
    + box(236, 4, 120, 36, 'Schwächen (W)', size=12, art='pale', tip='Interner Fokus: Schwächen, z. B. viele Engpassteile, Bedarfsträger bestellen nicht abgestimmt.')
    + box(4, 46, 100, 110, 'Chancen (O)', size=12, art='pale', tip='Externer Fokus (Beschaffungsmarkt): z. B. neue Anbieter, Bündelungsmöglichkeiten, Best Cost Countries.')
    + box(4, 162, 100, 110, 'Risiken (T)', size=12, art='pale', tip='Externer Fokus: z. B. Hauptlieferant nutzt die Beziehung aus, Zölle, Verteuerung von Vorprodukten.')
    + box(110, 46, 120, 110, 'S-O\n„ausbauen“\n\nStärken nutzen,\num Chancen\nzu nutzen', size=12, art='hl', tip='S-O-Strategien: Wie kann ich meine Stärken einsetzen, um die Chancen zu nutzen?')
    + box(236, 46, 120, 110, 'W-O\n„aufholen“\n\nSchwächen\nverringern, um\nChancen zu nutzen', size=12, tip='W-O-Strategien: Wie kann ich meine Schwächen verringern, um die Chancen zu nutzen?')
    + box(110, 162, 120, 110, 'S-T\n„absichern“\n\nStärken nutzen,\num Risiken zu\nverringern', size=12, tip='S-T-Strategien: Wie kann ich meine Stärken einsetzen, um die Risiken zu verringern?')
    + box(236, 162, 120, 110, 'W-T\n„vermeiden“\n\nSchwächen ver-\nringern, Risiken\nvermeiden', size=12, tip='W-T-Strategien: Wie kann ich meine Schwächen verringern, um Risiken abzufedern oder zu vermeiden?'),
    'SWOT-Matrix mit Normstrategien', maxw=420)

SC = [('Volumenbündelung (Single Sourcing)', [8, 8, 2, 6]), ('Low-Cost-Country', [4, 2, 3, 8]), ('Do Nothing', [10, 10, 3, 0])]
G = [0.15, 0.25, 0.20, 0.40]
SCORE = [round(sum(w * g for w, g in zip(ws, G)), 2) for _, ws in SC]
assert SCORE == [6.0, 4.9, 4.6]

t_swot = thema('swot-scoring', 'SWOT-Analyse und Scoring-Modell zur Strategieauswahl',
    kern='Die SWOT-Matrix fasst die Analyseergebnisse zusammen: intern Stärken und Schwächen, extern Chancen und Risiken des Beschaffungsmarkts, möglichst im cross-funktionalen Team. Aus den Kombinationen folgen Normstrategien: S-O ausbauen, W-O aufholen, S-T absichern, W-T vermeiden. Die Strategieoptionen werden verglichen und bewertet, z. B. mit einem gewichteten Scoring-Modell; dann folgt ein Maßnahmenplan.',
    kurz=p('Die Materialgruppe „Kunststoffteile“ der Neckarrad GmbH: Stärke ist das hohe Volumen, Schwäche die schlechte Datenlage; Chance sind neue Anbieter, Risiko drohende Zölle. Was folgt daraus? Mit dem hohen Volumen die neuen Anbieter in den Wettbewerb holen: <b>S-O „ausbauen“</b>.')
        + p('Mehrere Optionen werden am Ende mit einem <b>Scoring-Modell</b> verglichen: Kriterien gewichten, Punkte vergeben, gewichtete Summe bilden.'),
    fig=fw('SWOT-Matrix mit den vier Normstrategien. Tippe auf die Felder.') + bild(fig_swot),
    figcap='nach Folien „SWOT-Analyse auf Materialgruppenebene“',
    article=h3('SWOT im MGM')
        + liste(['Die bisherigen Ergebnisse aus den unterschiedlichen Analysen werden in der SWOT-Matrix zusammengefasst, idealerweise in einem cross-funktionalen Team.', 'Kurze, prägnante „Überschriften“ zu den zentralen Aspekten.',
                 '<b>Interner Fokus</b>: Stärken und Schwächen (bezogen auf die Bedarfe). <b>Externer Fokus</b>: Chancen und Risiken (Beschaffungsmarkt).', 'Aus der Matrix werden Strategieoptionen abgeleitet, verglichen und bewertet; danach Maßnahmenplan.'])
        + tabelle(['', 'Stärken (S)', 'Schwächen (W)'], [['Chancen (O)', 'S-O „ausbauen“: Stärken einsetzen, um Chancen zu nutzen', 'W-O „aufholen“: Schwächen verringern, um Chancen zu nutzen'],
                                                        ['Risiken (T)', 'S-T „absichern“: Stärken einsetzen, um Risiken zu verringern', 'W-T „vermeiden“: Schwächen verringern, um Risiken abzufedern oder zu vermeiden']])
        + p('Problem: Dieser Schritt wird wegen seiner Komplexität in der Praxis meist nicht oder nur sehr allgemein vollzogen. <b>Als Lösung bieten sich für die praktische Umsetzung Portfolios an.</b>')
        + h3('Praxisbeispiel einer SWOT')
        + tabelle(['Stärken', 'Schwächen'], [['relativ hohes Volumen in der MG; Ansätze zur Standardisierung von Spezifikationen; cross-funktionale Teams entstehen; gute Daten über aktuelle Bedarfe; erfahrene Materialgruppenmanager',
                                             'viele Engpassteile; Bedarfsträger bestellen nicht abgestimmt und binden den Einkauf spät ein; schlechte Daten über künftige Bedarfe; hohe Einkaufskosten mangels Digitalisierung; keine MG-Strategien']])
        + tabelle(['Chancen', 'Risiken'], [['mehr Wettbewerb durch neue Anbieter; Bündelungsmöglichkeiten; Cost Break Down zeigt Einsparpotenziale; Best Cost Countries; Unterauslastung bei Lieferanten',
                                            'Hauptlieferant betrachtet die Beziehung als „Ausnutzen“; kleinere Speziallieferanten könnten ausscheiden; Zölle auf Produkte aus Asien; Verteuerung bei Vorprodukten']])
        + h3('Scoring-Modell zur Strategieauswahl')
        + p('Ziel: Kostensenkung. Kriterien mit Gewichten; Punkte von 0 (schlechtester) bis 10 (bester Wert); Score = gewichtete Summe.')
        + tabelle(['Option', 'Einfachheit Implementierung (15 %)', 'Kosten Implementierung (25 %)', 'Risiko (20 %)', 'Nutzen (40 %)', 'Score'],
                  [[n] + [str(x) for x in ws] + [f'{s:.1f}'.replace('.', ',')] for (n, ws), s in zip(SC, SCORE)])
        + bsp('Score der Volumenbündelung', 'Punkte 8, 8, 2, 6; Gewichte 15, 25, 20, 40 %', [('gewichtete Summe', '8·0,15 + 8·0,25 + 2·0,20 + 6·0,40 = 1,2 + 2,0 + 0,4 + 2,4 = 6,0')], 'Höchster Score: Volumenbündelung (6,0) vor Low-Cost-Country (4,9) und Do Nothing (4,6).'),
    merk='SWOT: intern Stärken/Schwächen, extern Chancen/Risiken; cross-funktional; S-O ausbauen, W-O aufholen, S-T absichern, W-T vermeiden; in der Praxis oft zu komplex → Portfolios. Strategieauswahl per Scoring: Kriterien gewichten, 0–10 Punkte, gewichtete Summe (Bündelung 6,0; LCC 4,9; Do Nothing 4,6).',
    exam='SWOT-Felder und Normstrategien; Scoring-Modell rechnen.',
    fehler=['Chancen und Stärken vermischen: Stärken sind intern, Chancen extern.', 'Beim Scoring die Gewichte vergessen.'],
    src='Folien 198–207')

KAPITEL = kapitel('k6', 'Strategieentwicklung: Ziele, Portfolios, SWOT',
    'Wie wird aus der Analyse eine Strategie? Ziele top-down, Lieferantenpyramide, Portfolios (BCG, Kraljic, Marktmacht, Risiko) und SWOT mit Scoring-Modell.',
    ['Ziele', 'Lieferantenpyramide', 'Portfolios', 'Kraljic', 'Kraljic dynamisch', 'Marktmacht', 'Risiko', 'SWOT'],
    [t_ziele, t_pyr, t_pf, t_kraljic, t_dyn, t_mm, t_risk, t_swot])
