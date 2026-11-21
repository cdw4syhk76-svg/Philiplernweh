import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *

# Durchgehendes Beispiel: der Laufschuh-Hersteller „Stride GmbH“ aus Mannheim.

PHASEN = ['Zielsetzung', 'Umweltanalyse', 'Unternehmensanalyse', 'Strategiewahl', 'Implementierung\nund Kontrolle']


def phasen_bild(hl):
    s = ''
    for i, n in enumerate(PHASEN):
        x, y = 4 + i * 34, 6 + i * 50
        s += box(x, y, 216, 42, 'Phase der ' + n.replace('\n', ' ') if i < 4 else 'Phase der Implementierung\nund Kontrolle', size=13, art='hl' if i == hl else 'card',
                 tip=['Wo wollen wir hin? Vision, Leitbild, Unternehmens-, Geschäftsbereichs- und Funktionsziele.', 'Was passiert um uns herum? Allgemeine Umwelt und Wettbewerbsumfeld (Five Forces).',
                      'Wo stehen wir? SWOT, Ressourcen, Lebenszyklus, Erfahrungskurve, BCG-Matrix.', 'Welchen Weg gehen wir? Ansoff-Matrix, Wettbewerbsstrategien nach Porter.',
                      'Umsetzen und prüfen: Implementierungsplanung, Umsetzung, Soll-Ist-Kontrolle.'][i])
        if i < 4:
            s += pfeil(x + 108, y + 44, x + 130, y + 50)
    return svg(360, 258, s, 'Fünf Phasen der Unternehmensführung', maxw=420)


t_phasen = thema('fuehrung', 'Unternehmensführung: Strategie und fünf Phasen',
    kern='Strategische Unternehmensführung beantwortet drei Fragen: Wo wollen wir hin? Wo stehen wir? Wie kommen wir dahin? Sie läuft in fünf Phasen: Zielsetzung, Umweltanalyse, Unternehmensanalyse, Strategiewahl, Implementierung und Kontrolle.',
    kurz=p('Die Stride GmbH baut Laufschuhe. Die Chefin fragt: <b>Wo wollen wir hin</b> (Ziele)? <b>Wo stehen wir jetzt</b> (Ausgangslage)? <b>Wie kommen wir dahin</b> (Weg)? Die Antwort auf diese Fragen ist eine <b>Strategie</b>.')
        + p('Der Weg dahin läuft in <b>fünf Phasen</b> ab, die die nächsten Unterthemen der Reihe nach behandeln.'),
    fig=fw('Die fünf Phasen wie auf der Folie. Tippe auf die Kästen.') + bild(phasen_bild(0)),
    figcap='nach Folie „Unternehmensführung“ (Phasenmodell)',
    article=h3('Aufgaben der Unternehmensführung')
        + tabelle(['Frage', 'Inhalt'], [['Was sind die Ziele?', 'wo wollen wir hin'], ['Was ist die Ausgangslage?', 'wo sind wir jetzt'], ['Wie kommen wir da hin?', 'welchen Weg sollen wir gehen']])
        + p('Drei berühmte Definitionen von <b>Strategie</b>:')
        + cards([('Carl von Clausewitz', '„Gebrauch des Gefechts zum Zweck des Krieges“'), ('Michael Porter', '„In sich stimmige Anordnung von Aktivitäten, die ein Unternehmen von einem Konkurrenten unterscheidet“'), ('Herbert Simon', '„Kunst, alle Kräfte eines Unternehmens so einzusetzen, dass ein profitables Überleben gesichert ist“')])
        + weiter('Die Unternehmensführung arbeitet die Fragen in fünf Phasen ab.')
        + h3('Die fünf Phasen')
        + tabelle(['Phase', 'Leitfrage', 'Werkzeuge'], [
            ['1 Zielsetzung', 'Wo wollen wir hin?', 'Vision, Leitbild, Ziele'], ['2 Umweltanalyse', 'Was passiert um uns herum?', 'Umweltsphären, Porters Five Forces'],
            ['3 Unternehmensanalyse', 'Wo stehen wir?', 'SWOT, Ressourcenanalyse, Lebenszyklus, Erfahrungskurve, BCG-Matrix'],
            ['4 Strategiewahl', 'Welchen Weg gehen wir?', 'Ansoff-Matrix, Wettbewerbsstrategien nach Porter'], ['5 Implementierung und Kontrolle', 'Läuft es wie geplant?', 'Implementierungsplanung, Soll-Ist-Vergleich']])
        + wahr('w-ph', [('Die Umweltanalyse kommt vor der Unternehmensanalyse.', True, 'Phase 2 vor Phase 3.'),
                        ('Die Strategiewahl ist die erste Phase.', False, 'Zuerst kommt die Zielsetzung.')]),
    merk='Fünf Phasen: Zielsetzung → Umweltanalyse → Unternehmensanalyse → Strategiewahl → Implementierung und Kontrolle. Strategie beantwortet: Wo wollen wir hin, wo stehen wir, wie kommen wir dahin?',
    exam='Phasen in die richtige Reihenfolge bringen und Werkzeuge zuordnen.',
    fehler=['Umwelt- und Unternehmensanalyse vertauschen: Umwelt = außen, Unternehmen = innen.'],
    src='Folien 243–244')

# ---------------------------------------------------------------- 2 Zielhierarchie
def pyramide():
    s = ''
    stufen = [('Vision', 'Die große Idee, die Richtung gibt: „A car for everybody“, „The man on the moon“. Für die Vorlesung sind Vision und Leitbild fast dasselbe.'),
              ('Unternehmensleitbild', 'Konkretisiert die Vision: Werte und Mission. Beispiel: „Don’t be evil“, „Wenn du einen Körper hast, bist du Athlet“.'),
              ('Unternehmensziele', 'Konkret und messbar, z. B. Umsatz, Marktanteil oder Nachhaltigkeitsziele bis zu einem Jahr.'),
              ('Geschäftsbereichsziele', 'Jeder Geschäftsbereich (z. B. Pkw, Busse, Lkw, Vans) hat eigene Ziele, die zum Leitbild passen.'),
              ('Funktionsziele', 'Ziele der Funktionen: Personal, Qualitätswesen, Forschung, Marketing, Logistik, Engineering, Entwicklung.')]
    for i, (n, tip) in enumerate(stufen):
        y = 6 + i * 46; ob = 0 if i == 0 else 26 + i * 30; un = 26 + (i + 1) * 30
        if i == 0:
            s += tpg(f'<polygon points="180,{y} {180 + un},{y + 44} {180 - un},{y + 44}" style="fill:var(--primary)"/>' + T(180, y + 32, n, 13, 800, 'middle', 'var(--on-primary)'), tip)
        else:
            s += tpg(f'<polygon points="{180 - ob},{y} {180 + ob},{y} {180 + un},{y + 44} {180 - un},{y + 44}" style="fill:var(--pale);stroke:var(--primary-2)" stroke-width="1.2"/>' + T(180, y + 24, n.replace('Unternehmensleitbild', 'Unternehmens-\nleitbild'), 13 if i > 1 else 12, 800), tip)
    return svg(360, 242, s, 'Zielhierarchie', maxw=420)


t_ziele = thema('zielhierarchie', 'Phase 1: Vision, Leitbild und Zielhierarchie',
    kern='Die Zielsetzung ist eine Hierarchie: Vision → Unternehmensleitbild → Unternehmensziele → Geschäftsbereichsziele → Funktionsziele. Von oben nach unten wird es immer konkreter.',
    kurz=p('Ganz oben steht die <b>Vision</b>: eine große Idee, die Richtung gibt („A car for everybody“, „The man on the moon“). Das <b>Leitbild</b> beschreibt die Werte. Darunter werden die Ziele immer konkreter: Ziele des ganzen Unternehmens, Ziele jedes Geschäftsbereichs und Ziele jeder Funktion wie Marketing oder Personal.')
        + p('Bei Stride: Vision „Jeder Mensch soll gern laufen.“ Unternehmensziel: 10 % mehr Umsatz bis 2027. Geschäftsbereichsziel Trailschuhe: Marktanteil 5 %. Funktionsziel Personal: zwei neue Entwicklerinnen.'),
    fig=fw('Die Zielpyramide. Tippe auf die Stufen.') + bild(pyramide()),
    figcap='nach Folie „Phase der Zielsetzung“',
    article=h3('Von der Vision zu den Funktionszielen')
        + tabelle(['Stufe', 'Was ist das?', 'Beispiel'], [
            ['Vision', 'Grundidee für die Zukunft, gibt Richtung', '„A PC for everybody“, „I have a dream“'],
            ['Unternehmensleitbild', 'Konkretisierung der Vision, Mission und Werte', 'Google: „Don’t be evil“ und „die Informationen der Welt organisieren und für alle zugänglich machen“; McDonald’s: „To be our customers’ favorite place and way to eat“; Amazon: „to be earth’s most customer centric company …“; Nike: „If you have a body, you are an athlete“'],
            ['Unternehmensziele', 'mit Zahlen darstellbar', 'Umsatz von x € bis Jahresende'],
            ['Geschäftsbereichsziele', 'Ziele je Geschäftsbereich', 'Mercedes-Benz: Cars, Busses, Trucks, Vans'],
            ['Funktionsziele', 'Ziele innerbetrieblicher Funktionen', 'Personal, Qualitätswesen, Forschung, Marketing, Logistik']])
        + p('Für die Vorlesung sind Vision und Leitbild fast ein Punkt. Wichtig sind der <b>Übergang</b> von oben nach unten und der Unterschied zwischen <b>Geschäftsbereichszielen</b> (je Sparte, etwa Pkw oder Lkw) und <b>Funktionszielen</b> (je Funktion, etwa Personal oder Marketing).')
        + falle('Geschäftsbereich und Funktion verwechseln. Geschäftsbereich = was man verkauft (Sparte). Funktion = was man im Betrieb tut (Einkauf, Personal …).')
        + wahr('w-zh', [('Unternehmensziele sind konkreter als die Vision.', True, 'Je weiter unten, desto konkreter.'),
                        ('„Marketing“ ist ein Geschäftsbereich.', False, 'Marketing ist eine Funktion.')]),
    merk='Zielhierarchie: Vision → Leitbild → Unternehmensziele → Geschäftsbereichsziele (je Sparte) → Funktionsziele (je Funktion). Nach unten konkreter.',
    exam='Stufen der Zielhierarchie ordnen; Geschäftsbereichs- und Funktionsziele unterscheiden.',
    fehler=['Funktions- und Geschäftsbereichsziele vertauschen.'],
    src='Folien 245–254')

# ---------------------------------------------------------------- 3 Umweltanalyse
fig_umwelt = svg(360, 258,
    tpg(rechteck(4, 4, 352, 250, 'var(--pale-2)', 'var(--line)', 14), 'Die allgemeine Umwelt: politische, wirtschaftliche, gesellschaftliche und rechtliche Umwelt. Sie wirkt auf alle Unternehmen einer Branche.')
    + T(180, 24, 'Umwelt', 14, 800)
    + box(10, 34, 82, 40, 'politisch', size=12, art='weak') + box(96, 34, 82, 40, 'wirtschaftl.', size=12, art='weak') + box(182, 34, 82, 40, 'gesellschaftl.', size=12, art='weak') + box(268, 34, 82, 40, 'rechtlich', size=12, art='weak')
    + tpg(rechteck(36, 88, 288, 154, 'var(--pale)', 'var(--line)', 12), 'Das Wettbewerbsumfeld: Branche, Konkurrenz, Markt. Ein Instrument dafür ist Porters Five Forces.')
    + T(180, 108, 'Wettbewerbsumfeld', 13, 800)
    + T(96, 132, 'Branche', 12, 600, 'middle', 'var(--muted)') + T(180, 132, 'Konkurrenz', 12, 600, 'middle', 'var(--muted)') + T(264, 132, 'Markt', 12, 600, 'middle', 'var(--muted)')
    + box(96, 150, 168, 70, 'Unternehmen', size=14, art='hl', tip='Das Unternehmen in der Mitte, umgeben vom Wettbewerbsumfeld und der allgemeinen Umwelt.'),
    'Umwelt und Wettbewerbsumfeld', maxw=420)

t_umwelt = thema('umweltanalyse', 'Phase 2: Umweltanalyse',
    kern='Die Umweltanalyse schaut nach außen: auf die allgemeine Umwelt (politisch, wirtschaftlich, gesellschaftlich, rechtlich) und auf das Wettbewerbsumfeld (Branche, Konkurrenz, Markt). Instrument für das Wettbewerbsumfeld: Porters Five Forces.',
    kurz=p('Bevor Stride eine Strategie wählt, schaut sie nach <b>außen</b>: Gibt es neue Gesetze (rechtlich)? Läuft die Konjunktur (wirtschaftlich)? Laufen mehr Menschen (gesellschaftlich)? Und im engeren Kreis: Was machen die Konkurrenten, wie entwickelt sich der Markt?')
        + p('Das Unternehmen sitzt in der Mitte von zwei Ringen: dem <b>Wettbewerbsumfeld</b> und der allgemeinen <b>Umwelt</b>.'),
    fig=fw('Die zwei Ringe der Umweltanalyse. Tippe auf die Bereiche.') + bild(fig_umwelt),
    figcap='nach Folie „Umweltanalyse“',
    article=h3('Allgemeine Umwelt und Wettbewerbsumfeld')
        + tabelle(['Ebene', 'Teile', 'Beispiel Stride'], [
            ['Umwelt', 'politische, wirtschaftliche, gesellschaftliche, rechtliche Umwelt', 'Zölle auf Schuhe aus Asien, Konjunktur, Lauftrend, Umweltauflagen'],
            ['Wettbewerbsumfeld', 'Branche, Konkurrenz, Markt', 'große Sportmarken, neue Online-Anbieter, wachsender Trailrunning-Markt']])
        + p('Das wichtigste Instrument für das Wettbewerbsumfeld ist <b>Porters Five Forces</b> (nächstes Unterthema).')
        + weiter('Wie leicht man sich bei der Umwelt irren kann, zeigen berühmte Fehleinschätzungen.')
        + h3('Historische Fehleinschätzungen der Umwelt')
        + liste(['„Das Telefon hat zu viele ernsthaft zu bedenkende Mängel für ein Kommunikationsmittel.“ (Western Union, 1876)',
                 '„Wer zum Teufel will Schauspieler reden hören?“ (Warner Brothers über Tonfilme, 1920)',
                 '„Ich denke, es gibt weltweit einen Markt für vielleicht fünf Computer.“ (Thomas Watson, IBM, 1943)',
                 '„Guitar music is on the way out.“ (Decca Recording lehnt die Beatles ab, 1962)',
                 '„There is no reason anyone would want a computer in their home.“ (Ken Olsen, Digital Equipment, 1977)'])
        + wahr('w-uw', [('Die rechtliche Umwelt gehört zur allgemeinen Umwelt.', True, 'Neben politischer, wirtschaftlicher und gesellschaftlicher.'),
                        ('Porters Five Forces analysieren das Unternehmen von innen.', False, 'Sie analysieren das Wettbewerbsumfeld (außen).')]),
    merk='Umweltanalyse (außen): allgemeine Umwelt (politisch, wirtschaftlich, gesellschaftlich, rechtlich) + Wettbewerbsumfeld (Branche, Konkurrenz, Markt) → Instrument Five Forces.',
    exam='Einflüsse der allgemeinen Umwelt oder dem Wettbewerbsumfeld zuordnen.',
    fehler=['Umweltanalyse (außen) und Unternehmensanalyse (innen) verwechseln.'],
    src='Folien 256, 267')

# ---------------------------------------------------------------- 4 Five Forces
fig_ff = svg(360, 290,
    box(110, 112, 140, 66, 'Rivalität in\nder Branche', size=13, art='hl', tip='Wettbewerb unter den bestehenden Unternehmen. Hängt ab von Branchenwachstum, Marktaustrittsbarrieren und Anzahl der Wettbewerber.')
    + box(100, 6, 160, 56, 'Bedrohung durch\nneue Konkurrenz', size=13, tip='Wie leicht können neue Anbieter in den Markt eintreten? Das hängt von Markteintrittsbarrieren ab: Vertrauen, Politik, wirtschaftliche Vorteile.')
    + box(100, 228, 160, 56, 'Bedrohung durch\nErsatzprodukte', size=13, tip='Substitute mit gleichen oder ähnlichen Eigenschaften: Smartphone statt Wecker, Auto statt Kutsche, Online statt Reisebüro.')
    + box(4, 112, 92, 66, 'Verhand-\nlungsmacht\nLieferanten', size=12, tip='Wie stark können Lieferanten Preise und Bedingungen diktieren?')
    + box(264, 112, 92, 66, 'Verhand-\nlungsmacht\nAbnehmer', size=12, tip='Wie stark können Kunden Preise drücken?')
    + pfeil(180, 64, 180, 110) + pfeil(180, 226, 180, 180) + pfeil(96, 145, 108, 145) + pfeil(264, 145, 252, 145),
    "Porter's Five Forces", maxw=420)

t_ff = thema('five-forces', 'Porters Five Forces: Rivalität und Ersatzprodukte', star=True,
    kern='Porters Five Forces (Branchenstrukturanalyse): Ein Unternehmen ist Spielball von fünf Kräften: Rivalität in der Branche, Bedrohung durch neue Konkurrenz, Verhandlungsmacht der Lieferanten, Verhandlungsmacht der Abnehmer, Bedrohung durch Ersatzprodukte.',
    kurz=p('Wie attraktiv ist der Laufschuhmarkt für Stride? Michael Porter sagt: Das hängt an <b>fünf Kräften</b>. In der Mitte die <b>Rivalität</b> mit den bestehenden Konkurrenten. Von oben drohen <b>neue Konkurrenten</b>, von unten <b>Ersatzprodukte</b>. Links drücken die <b>Lieferanten</b>, rechts die <b>Abnehmer</b>.')
        + p('Je stärker die Kräfte, desto härter der Wettbewerb und desto kleiner der Gewinn. Für jede Kraft gibt es Kriterien, mit denen man sie einschätzt.'),
    fig=fw('Die fünf Kräfte wie auf der Folie. Tippe auf die Kästen.') + bild(fig_ff),
    figcap='nach Folie „Porter´s Five Forces (Branchenstrukturanalyse)“',
    article=h3('Kraft 1: Rivalität bestehender Unternehmen')
        + tabelle(['Kriterium', 'Wirkung'], [
            ['Wachstum der Branche', 'wächst ein Markt, gibt es weniger Rivalität (alle können wachsen)'],
            ['Marktaustrittsbarrieren', 'wer schon viel investiert hat oder durch Verträge gebunden ist (rechtliche, wirtschaftliche Barrieren), kann nicht einfach aussteigen und kämpft weiter'],
            ['Anzahl der Wettbewerber', 'viele Wettbewerber → höhere Konkurrenz']])
        + p('Ein Beispiel für extreme Rivalität: der Lebensmitteleinzelhandel mit Margen von etwa 1 %.')
        + weiter('Neben den Konkurrenten im gleichen Markt gibt es eine zweite Gefahr: Produkte, die das eigene ersetzen.')
        + h3('Kraft 5: Bedrohung durch Ersatzprodukte')
        + p('<b>Substitute</b> sind Ersatzprodukte mit gleichen oder ähnlichen Eigenschaften: Smartphone statt Wecker, Auto statt Kutsche, DVD statt CD, Online-Buchung statt Reisebüro.')
        + cards([('Technologiewandel', 'Neue Technik ersetzt alte (CD ersetzt Schallplatte).'), ('Kostenvorteile', 'Das Ersatzprodukt ist günstiger.'), ('geringe Umstellungskosten', 'Für Abnehmer ist der Wechsel einfach.'), ('hohe Wechselneigung', 'Abnehmer wechseln gern; etwa wenn Monopole aufgehoben werden (Fernbus statt Bahn).')])
        + weiter('Die Kräfte 2 bis 4 (neue Konkurrenz und Verhandlungsmacht) haben eigene Unterthemen. Die Five Forces führen am Ende zu einer Frage: Wie stellt man sich im Wettbewerb auf?')
        + h3('Von den Five Forces zur Wettbewerbsstrategie')
        + p('Wer die Kräfte kennt, kann sich positionieren: als <b>Kostenführer</b>, durch <b>Qualitätsführerschaft</b> (Differenzierung) oder in einer <b>Nische</b>. Das sind Porters Wettbewerbsstrategien (Oberthema „Strategiewahl“).')
        + klausur_hinweis('Auswahlfrage zu Porters Five Forces: die fünf Kräfte kennen und Beispiele zuordnen (z. B. „Fernbusse ersetzen die Bahn“ = Ersatzprodukte; „ein Zulieferer droht, selbst Autos zu bauen“ = Verhandlungsmacht der Lieferanten).')
        + wahr('w-ff', [('Wächst die Branche, nimmt die Rivalität eher ab.', True, 'Alle können wachsen.'),
                        ('Hohe Marktaustrittsbarrieren verringern die Rivalität.', False, 'Wer nicht aussteigen kann, kämpft weiter: mehr Rivalität.'),
                        ('Das Smartphone ist für den Wecker ein Ersatzprodukt.', True, 'Substitut.')]),
    merk='Five Forces: Rivalität (Mitte), neue Konkurrenz, Ersatzprodukte, Verhandlungsmacht Lieferanten, Verhandlungsmacht Abnehmer. Rivalität: Branchenwachstum, Austrittsbarrieren, Anzahl Wettbewerber. Substitute: Technologiewandel, Kostenvorteile, geringe Umstellungskosten, Wechselneigung.',
    exam='Die fünf Kräfte nennen und Beispiele zuordnen (Auswahlfrage).',
    fehler=['Austrittsbarrieren mit Eintrittsbarrieren verwechseln.'],
    src='Folien 257–259, 264–266')

# ---------------------------------------------------------------- 5 Markteintrittsbarrieren
fig_me = svg(360, 270,
    box(100, 6, 160, 44, 'Markteintritts-\nbarrieren', size=13, art='hl', tip='Hürden, die neue Konkurrenten abhalten. Je höher, desto geringer die Bedrohung durch neue Konkurrenz.')
    + pfeil(150, 52, 60, 70) + pfeil(180, 52, 180, 70) + pfeil(210, 52, 300, 70)
    + box(4, 72, 112, 44, 'Vertrauen', size=13, tip='Vertrauensbarrieren: Referenzen, Käuferpfadabhängigkeit, Vertriebskanäle, Abschreckungsmaßnahmen.')
    + box(124, 72, 112, 44, 'Politik', size=13, tip='Politische Barrieren: rechtliche Hürden (Lizenzen, Zulassungen).')
    + box(244, 72, 112, 44, 'Wirtschaft', size=13, tip='Wirtschaftliche Barrieren: Economies of Scale, Economies of Scope, Netzwerkeffekte, absolute Kostenvorteile.')
    + box(4, 124, 112, 140, '· Referenzen\n· Käuferpfad-\n  abhängigkeit\n· Vertriebskanäle\n· Abschreckung', size=12, art='weak')
    + box(124, 124, 112, 140, '· rechtliche\n  Hürden\n  (Lizenzen,\n  Zulassung)', size=12, art='weak')
    + box(244, 124, 112, 140, '· Economies\n  of Scale\n· Economies\n  of Scope\n· Netzwerkeffekt\n· absolute\n  Kostenvorteile', size=12, art='weak'),
    'Markteintrittsbarrieren', maxw=420)

t_me = thema('markteintritt', 'Kraft 2: Bedrohung durch neue Konkurrenz (Markteintrittsbarrieren)',
    kern='Wie stark neue Konkurrenten drohen, hängt von Markteintrittsbarrieren ab: Vertrauensbarrieren (Referenzen, Käuferpfadabhängigkeit, Vertriebskanäle, Abschreckung), politische (rechtliche Hürden) und wirtschaftliche Barrieren (Economies of Scale und Scope, Netzwerkeffekt, absolute Kostenvorteile).',
    kurz=p('Unternehmensberater kann jeder werden: Gewerbe anmelden, fertig. Die <b>rechtliche</b> Hürde ist niedrig. Aber wer vertraut einem Neuling ohne Referenzen? Die <b>Vertrauensbarriere</b> ist hoch.')
        + p('Bei Laufschuhen ist es ähnlich: Eine neue Marke müsste gegen die Größenvorteile der Großen (<b>Economies of Scale</b>) und gegen ihre Regalplätze im Handel (<b>Vertriebskanäle</b>) ankommen.'),
    fig=fw('Drei Gruppen von Barrieren. Tippe auf die Kästen.') + bild(fig_me),
    figcap='nach Folie „Bedrohung durch neue Konkurrenz“',
    article=h3('Drei Gruppen von Barrieren')
        + tabelle(['Barriere', 'Bedeutung', 'Beispiel'], [
            ['Referenzbarrieren', 'Kunden wollen Nachweise', 'Berater, Anwälte, Handwerker'], ['Käuferpfadabhängigkeit', 'Kunden wechseln ungern, weil sie an ein System gewöhnt sind', 'von Apple zu Samsung'],
            ['Vertriebskanäle', 'Zugang zu Verkaufsplätzen', 'Regalmeter im Handel'], ['Abschreckungsmaßnahmen', 'Etablierte drohen mit Preiskampf', 'Preissenkung bei Markteintritt'],
            ['rechtliche Hürden', 'Lizenzen, Zulassungen, Patente', 'Arzneimittel, Banken'],
            ['Economies of Scale', 'Größeneffekte: Fixkostendegression, Mengenrabatte, Spezialisierung', 'Großserie senkt die Stückkosten'],
            ['Economies of Scope', 'Verbundeffekte: dieselben Maschinen, Orte, Zeiten für mehrere Produkte', 'sachlich: Zug oder Auto aus Rohstahl; räumlich: McCafé im McDonald’s'],
            ['Netzwerkeffekt', 'Der Wert eines Produkts steigt, je mehr andere es nutzen', 'WhatsApp, schwer zu ersetzen, weil jeder es nutzt'],
            ['absolute Kostenvorteile', 'Patente, Wissen, eingespielte Lieferanten', 'Bosch hatte das ABS-Patent; jahrzehntelang aufgebaute Filialen und Kunden']])
        + falle('Netzwerkeffekt und Economies of Scale verwechseln. Beim Netzwerkeffekt wird das Produkt für den <b>Kunden</b> wertvoller, je mehr es nutzen. Bei Scale sinken die <b>Kosten</b> des Anbieters mit der Menge.')
        + wahr('w-me', [('WhatsApp ist ein Beispiel für einen Netzwerkeffekt.', True, 'Der Nutzen steigt mit der Zahl der Nutzer.'),
                        ('Ein McCafé im McDonald’s nutzt Economies of Scope.', True, 'Räumlicher Verbundeffekt.'),
                        ('Hohe Markteintrittsbarrieren erhöhen die Bedrohung durch neue Konkurrenz.', False, 'Sie verringern sie.')]),
    merk='Markteintrittsbarrieren: Vertrauen (Referenzen, Käuferpfadabhängigkeit, Vertriebskanäle, Abschreckung), Politik (rechtliche Hürden), Wirtschaft (Economies of Scale, Economies of Scope, Netzwerkeffekt, absolute Kostenvorteile).',
    exam='Barrieren an Beispielen erkennen und zuordnen.',
    fehler=['Scale (Größe) und Scope (Verbund) verwechseln.'],
    src='Folie 260')

# ---------------------------------------------------------------- 6 Verhandlungsmacht
fig_vm = svg(360, 250,
    box(4, 84, 104, 76, 'Lieferant\n(Blechnerei\nMüller)', size=12, tip='Liefert Blech an den Autohersteller.')
    + box(128, 84, 104, 76, 'Unternehmen\n(Autoherst.)', size=12, art='hl', tip='Steht zwischen Lieferanten und Abnehmern.')
    + box(252, 84, 104, 76, 'Abnehmer\n(Händler,\nKunden)', size=12, tip='Kauft die Autos.')
    + pfeil(110, 122, 126, 122) + pfeil(234, 122, 250, 122)
    + linie([(180, 82), (180, 64), (56, 64)], 'var(--c3)', 2) + pfeil(56, 64, 56, 80, 'var(--c3)', 2)
    + T(8, 22, 'Rückwärtsintegration: Der Abnehmer', 12, 700, 'start', 'var(--c3)') + T(8, 40, 'droht: „Dann machen wir das Blech selbst!“', 12, 700, 'start', 'var(--c3)')
    + linie([(56, 162), (56, 180), (180, 180)], 'var(--neg)', 2) + pfeil(180, 180, 180, 164, 'var(--neg)', 2)
    + T(8, 210, 'Vorwärtsintegration: Der Lieferant droht:', 12, 700, 'start', 'var(--neg)') + T(8, 228, '„Dann bauen wir eben selbst Autos!“', 12, 700, 'start', 'var(--neg)'),
    'Verhandlungsmacht, Vorwärts- und Rückwärtsintegration', maxw=420)

t_vm = thema('verhandlungsmacht', 'Kraft 3 und 4: Verhandlungsmacht von Lieferanten und Abnehmern',
    kern='Lieferanten sind mächtig, wenn die Firmen der Branche klein sind, kaum Ersatz existiert, das Auftragsvolumen für sie gering ist und sie glaubhaft mit Vorwärtsintegration drohen können. Abnehmer sind mächtig, wenn sie einen großen Umsatzanteil ausmachen, die Produkte standardisiert sind und sie mit Rückwärtsintegration (Eigenfertigung) drohen können.',
    kurz=p('Die Blechnerei Müller liefert Blech an Audi. Erhöht sie die Preise, kann Audi drohen: „Dann stellen wir unser Blech selbst her.“ Das ist <b>Rückwärtsintegration</b>, und sie gibt dem Abnehmer Macht.')
        + p('Umgekehrt könnte ein Lieferant drohen, selbst in den Markt einzutreten (<b>Vorwärtsintegration</b>). Wie gefährlich ein Zulieferer werden kann, zeigte der Streit zwischen VW und dem Getriebeteile-Lieferanten Prevent: Ein kleiner Lieferant stoppte die Golf-Produktion.'),
    fig=fw('Vorwärts- und Rückwärtsintegration. Tippe auf die Kästen.') + bild(fig_vm),
    figcap='nach Folie „Verhandlungsstärke der Lieferanten und Abnehmer“',
    article=h3('Wann ist die Verhandlungsmacht groß?')
        + tabelle(['Faktor', 'Lieferanten sind mächtig, wenn …', 'Abnehmer sind mächtig, wenn …'], [
            ['Konzentrationsgrad', 'die Firmen der Branche (ihre Kunden) klein sind', 'die Abnehmer einen großen Anteil am Umsatz des Lieferanten ausmachen'],
            ['Gefahr durch Ersatzprodukte', 'die Substitutionsgefahr gering ist', 'die Produkte standardisiert sind (leicht zu ersetzen)'],
            ['Bedeutung des Auftragsvolumens', 'das Auftragsvolumen für den Lieferanten gering ist', 'das Auftragsvolumen für den Lieferanten groß ist'],
            ['Integration', 'sie glaubhaft drohen können, in den Markt einzutreten (Vorwärtsintegration)', 'sie die Möglichkeit der Eigenfertigung haben (Rückwärtsintegration)']])
        + bsp('VW und Prevent', 'Ein relativ unbekannter Zulieferer stoppt nach einem Streit über eine Auftragsstornierung die Lieferung von Getriebeteilen. Die Golf-Produktion steht still.',
              [('VW hatte sich bei speziellen Teilen von einem Lieferanten abhängig gemacht (keine Ersatzlieferanten).', 'geringe Substitutionsgefahr'), ('Der kleine Lieferant hat plötzlich große Macht.', 'Verhandlungsmacht der Lieferanten')],
              'Lehre: Mache dich bei speziellen Teilen nicht von einem Zulieferer abhängig, und unterschätze nie den Verhandlungspartner.')
        + zusatz('Der Zeitungsartikel über Kaufland, Mars und Iglo (Lieferstopp im Handel) ist in den Folien eingeklammert.')
        + wahr('w-vm', [('Droht ein Abnehmer mit Eigenfertigung, nennt man das Rückwärtsintegration.', True, 'Er übernimmt eine vorgelagerte Stufe.'),
                        ('Standardisierte Produkte stärken die Verhandlungsmacht der Lieferanten.', False, 'Sie stärken die Abnehmer, die leicht wechseln können.')]),
    merk='Lieferantenmacht groß: Kunden klein, kaum Substitute, Auftrag für Lieferant unwichtig, Drohung mit Vorwärtsintegration. Abnehmermacht groß: großer Umsatzanteil, standardisierte Produkte, Auftrag wichtig für Lieferant, Drohung mit Rückwärtsintegration.',
    exam='Fälle der Verhandlungsmacht von Lieferanten oder Abnehmern zuordnen; Vorwärts- und Rückwärtsintegration unterscheiden.',
    fehler=['Vorwärts- und Rückwärtsintegration vertauschen.'],
    src='Folien 261–263')

KAPITEL = kapitel('k9', 'Unternehmensführung: Ziele und Umwelt',
    'Wie ein Unternehmen seine Strategie entwickelt: fünf Phasen, Zielhierarchie und die Analyse der Umwelt mit Porters Five Forces. Durchgehendes Beispiel: der Laufschuh-Hersteller Stride GmbH.',
    ['Phasen', 'Zielhierarchie', 'Umwelt', 'Five Forces', 'Markteintritt', 'Verhandlungsmacht'],
    [t_phasen, t_ziele, t_umwelt, t_ff, t_me, t_vm])

from mehr2 import ergaenze
ergaenze(KAPITEL)
