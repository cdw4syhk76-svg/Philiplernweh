import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *

# Durchgehendes Beispiel: weiter mit der Stride GmbH.

fig_ansoff = svg(360, 270,
    T(140, 18, 'bestehendes Produkt', 12, 800, 'middle', 'var(--muted)') + T(284, 18, 'neues Produkt', 12, 800, 'middle', 'var(--muted)')
    + T(32, 92, 'beste-', 12, 800, 'middle', 'var(--muted)') + T(32, 108, 'hender', 12, 800, 'middle', 'var(--muted)') + T(32, 124, 'Markt', 12, 800, 'middle', 'var(--muted)')
    + T(32, 204, 'neuer', 12, 800, 'middle', 'var(--muted)') + T(32, 220, 'Markt', 12, 800, 'middle', 'var(--muted)')
    + box(66, 30, 144, 114, 'Markt-\ndurchdringung', size=13, tip='Bestehendes Produkt, bestehender Markt: Marktanteile gewinnen, z. B. durch günstigere Preise oder auffälligere Verpackung. Haferflocken in einem gesättigten Markt.')
    + box(214, 30, 142, 114, 'Produkt-\nentwicklung', size=13, tip='Neues Produkt für den bestehenden Markt: z. B. Porridge statt nur Haferflocken.')
    + box(66, 150, 144, 114, 'Markt-\nentwicklung', size=13, tip='Bestehendes Produkt auf einem neuen Markt: Milchpulver für Kinder wird nach einer Milchkrise in China anders etikettiert und an Erwachsene verkauft.')
    + box(214, 150, 142, 114, 'Diversifikation\n(höchstes Risiko)', size=13, art='hl', tip='Neues Produkt auf einem neuen Markt: am riskantesten, weil man beides nicht kennt.'),
    'Ansoff-Matrix', maxw=420)

t_ansoff = thema('ansoff', 'Phase 4: Produkt-Markt-Strategien (Ansoff-Matrix)',
    kern='Die Ansoff-Matrix kombiniert bestehende oder neue Produkte mit bestehenden oder neuen Märkten: Marktdurchdringung, Produktentwicklung, Marktentwicklung und Diversifikation (höchstes Risiko).',
    kurz=p('Wie kann Stride wachsen? Mit den <b>gleichen Schuhen</b> mehr verkaufen (Marktdurchdringung), <b>neue Schuhe</b> für die gleichen Kunden bauen (Produktentwicklung), die gleichen Schuhe in <b>neue Märkte</b> bringen (Marktentwicklung) oder etwas <b>ganz Neues</b> wagen (Diversifikation).')
        + p('Die <b>Ansoff-Matrix</b> ist eine Unternehmensstrategie (Produkt-Markt-Strategie). Je weiter weg vom Bekannten, desto höher das Risiko.'),
    fig=fw('Die vier Felder. Tippe auf die Felder für die Beispiele der Vorlesung.') + bild(fig_ansoff),
    figcap='nach Folie „Strategiewahl: Produkt-Markt-Kombination (Ansoff)“',
    article=h3('Vier Strategien')
        + tabelle(['', 'bestehendes Produkt', 'neues Produkt'], [
            ['bestehender Markt', 'Marktdurchdringung (market penetration): Marktanteile gewinnen', 'Produktentwicklung (product development)'],
            ['neuer Markt', 'Marktentwicklung (market development)', 'Diversifikation (diversification): höchstes Risiko']])
        + bsp('Beispiele der Vorlesung', '',
              [('Ein Haferflockenhersteller im gesättigten Markt wird günstiger oder auffälliger.', 'Marktdurchdringung'), ('Er bringt Porridge heraus.', 'Produktentwicklung'),
               ('Milchpulver (eigentlich für Kinder) wird nach der Milchkrise in China anders etikettiert und an Erwachsene verkauft.', 'Marktentwicklung'), ('Ein Hersteller steigt in ein völlig fremdes Geschäft ein.', 'Diversifikation')])
        + p('Auf der Ebene der Geschäftsbereiche folgen die <b>Wettbewerbsstrategien</b> nach Porter, auf der Ebene der Funktionen die Funktionalstrategien (Beschaffung, Vertrieb, Finanzen, Personal, F&amp;E, Produktion).')
        + zusatz('Die Übersicht weiterer Strategiearten (Organisations-, regionale, Entwicklungs- und Eigenständigkeitsstrategien), die Management-Funktionen (Planning, Organizing, Staffing, Directing, Coordinating, Reporting, Budgeting) und das SKF-Beispiel sind in den Folien eingeklammert bzw. durchgestrichen.')
        + wahr('w-ans', [('Ein bestehendes Produkt auf einem neuen Markt heißt Marktentwicklung.', True, 'Neuer Markt, altes Produkt.'),
                         ('Die Marktdurchdringung hat das höchste Risiko.', False, 'Die Diversifikation.')]),
    merk='Ansoff: Marktdurchdringung (alt/alt), Produktentwicklung (neues Produkt/alter Markt), Marktentwicklung (altes Produkt/neuer Markt), Diversifikation (neu/neu, höchstes Risiko).',
    exam='Beispiele den vier Feldern der Ansoff-Matrix zuordnen.',
    fehler=['Produkt- und Marktentwicklung vertauschen.'],
    src='Folien 284–288')

fig_porter = svg(360, 236,
    T(130, 18, 'Wettbewerbsvorteil durch …', 12, 800, 'middle', 'var(--muted)')
    + T(88, 36, 'Einzigartigkeit', 12, 700, 'middle', 'var(--muted)') + T(266, 36, 'Kostenvorsprung', 12, 700, 'middle', 'var(--muted)')
    + T(18, 100, 'bran-', 12, 700, 'middle', 'var(--muted)') + T(18, 116, 'chen-', 12, 700, 'middle', 'var(--muted)') + T(18, 132, 'weit', 12, 700, 'middle', 'var(--muted)')
    + T(18, 190, 'Seg-', 12, 700, 'middle', 'var(--muted)') + T(18, 206, 'ment', 12, 700, 'middle', 'var(--muted)')
    + box(40, 48, 154, 112, 'Differenzierung\n(Qualitäts-\nführerschaft)', size=13, tip='Branchenweit einzigartig sein, etwa durch Design oder Qualität: Apple, Nike, Mercedes. Man ist der Beste.')
    + box(200, 48, 156, 112, 'Kosten-\nführerschaft', size=13, art='hl', tip='Branchenweit der Günstigste sein, mit großer Absatzmenge: Aldi, Ryanair, Medion.')
    + box(40, 166, 316, 64, 'Nischenstrategie', size=13, tip='Konzentration auf ein kleines Marktsegment, etwa Montblanc-Füller oder ein Spezialist für Laufschuhe für Ultramarathons.'),
    'Wettbewerbsstrategien nach Porter', maxw=420)

t_porter = thema('porter-strategien', 'Wettbewerbsstrategien nach Porter',
    kern='Porter nennt drei Wettbewerbsstrategien: Differenzierung (branchenweit der Beste), Kostenführerschaft (branchenweit der Günstigste) und Nische (auf ein Segment konzentriert). Wer in der Mitte bleibt, ist „stuck in the middle“.',
    kurz=p('Stride muss sich entscheiden: Will sie der <b>Beste</b> sein (bester Schuh, höchster Preis) oder der <b>Günstigste</b> (große Mengen, kleine Marge)? Oder sie konzentriert sich auf eine <b>Nische</b>, etwa Schuhe für Ultraläufer.')
        + p('Porter warnt: Wer ein bisschen von allem will, ist „<b>stuck in the middle</b>“: weder der Beste noch der Billigste, und damit für niemanden die erste Wahl.'),
    fig=fw('Die drei Normstrategien. Tippe auf die Felder.') + bild(fig_porter),
    figcap='nach Folie „Strategiewahl: Wettbewerbsstrategien (Porter)“',
    article=h3('Zwei Normstrategien und die Nische')
        + p('Die zwei Normstrategien: Du zeichnest dich dadurch aus, dass du der <b>Beste</b> oder der <b>Günstigste</b> bist. Dazu kommt die Konzentration auf ein Segment.')
        + tabelle(['Strategie', 'Reichweite', 'Vorteil', 'Beispiele'], [
            ['Differenzierung', 'branchenweit', 'Einzigartigkeit (Design, Qualität)', 'Apple, Nike, Mercedes'],
            ['Kostenführerschaft', 'branchenweit', 'Kostenvorsprung, große Absatzmenge', 'Aldi, Ryanair, Medion'],
            ['Nische', 'Marktsegment', 'Spezialisierung', 'Montblanc, Flugverbindung Mannheim–Berlin']])
        + p('Die Vorlesung ordnet Branchen zu: Automobil, Uhren, Handel, Reisen, Computer, Fluggesellschaften haben jeweils Differenzierer, Kostenführer und Nischenanbieter.')
        + falle('Kostenführerschaft mit Niedrigqualität gleichsetzen. Es geht um die niedrigsten Kosten in der Branche, nicht um schlechte Produkte.')
        + wahr('w-por', [('Wer weder Kostenführer noch Differenzierer ist, ist „stuck in the middle“.', True, 'Porters Warnung.'),
                         ('Die Nischenstrategie zielt auf die ganze Branche.', False, 'Auf ein Marktsegment.')]),
    merk='Porter: Differenzierung (branchenweit, Beste), Kostenführerschaft (branchenweit, Günstigste), Nische (Segment). Dazwischen: stuck in the middle.',
    exam='Unternehmen den Wettbewerbsstrategien zuordnen.',
    fehler=['Nische mit Differenzierung verwechseln: Die Nische ist auf ein Segment beschränkt.'],
    src='Folien 289–290')

fig_impl = svg(360, 250,
    box(4, 6, 352, 44, 'formulierte Unternehmens-, Geschäftsbereichs-\nund Funktionalstrategie', size=12, art='pale')
    + pfeil(180, 52, 180, 66)
    + box(4, 68, 172, 86, 'Implementierungs-\nplanung\nZiele · Maßnahmen', size=12, tip='Ableitung von Implementierungszielen und Bestimmung von Implementierungsmaßnahmen.')
    + box(184, 68, 172, 86, 'Umsetzung\nKommunikation ·\nUmsetzung · Einsatz', size=12, art='hl', tip='Phase der Kommunikation, der Umsetzung und des Einsatzes.')
    + pfeil(176, 111, 184, 111)
    + pfeil(270, 156, 270, 170)
    + box(4, 172, 352, 70, 'Implementierungskontrolle\nSoll-Ist-Abweichungskontrolle · Zielerreichungsgrad', size=12, tip='Kontrolle: Wird umgesetzt wie geplant (Abweichung Soll/Ist), und wie weit sind die Ziele erreicht?'),
    'Implementierung und Kontrolle', maxw=420)

t_impl = thema('implementierung', 'Phase 5: Implementierung und Kontrolle',
    kern='Die gewählte Strategie wird geplant umgesetzt (Implementierungsplanung mit Zielen und Maßnahmen; Kommunikation, Umsetzung, Einsatz) und kontrolliert (Soll-Ist-Abweichung, Zielerreichungsgrad).',
    kurz=p('Eine Strategie auf dem Papier bringt nichts. Stride muss sie <b>planen</b> (Wer macht was bis wann?), <b>kommunizieren</b> und <b>umsetzen</b>, und dann <b>kontrollieren</b>: Läuft es wie geplant? Wie weit sind wir am Ziel?'),
    fig=fw('Der Ablauf der Implementierung. Tippe auf die Kästen.') + bild(fig_impl),
    figcap='nach Folie „Implementierung und Kontrolle“',
    article=h3('Planung, Umsetzung, Kontrolle')
        + tabelle(['Schritt', 'Inhalt'], [['Implementierungsplanung', 'Implementierungsziele ableiten, Implementierungsmaßnahmen bestimmen'], ['Umsetzung', 'Phase der Kommunikation, der Umsetzung, des Einsatzes'], ['Implementierungskontrolle', 'Abweichungskontrolle (Soll – Ist) und Zielerreichungsgrad']])
        + zusatz('Geschäftsmodelle (Business Model Management, Business Model Canvas, Four Forces of digital business), digitale Geschäftsmodelle und Big Data sind in den Folien durchgestrichen.')
        + wahr('w-impl', [('Zur Implementierungskontrolle gehört ein Soll-Ist-Vergleich.', True, 'Abweichungskontrolle.'),
                          ('Die Implementierung ist die erste Phase der Unternehmensführung.', False, 'Die letzte (Phase 5).')]),
    merk='Implementierung: Planung (Ziele, Maßnahmen) → Umsetzung (Kommunikation, Umsetzung, Einsatz) → Kontrolle (Soll-Ist, Zielerreichungsgrad).',
    exam='Bestandteile von Implementierung und Kontrolle nennen.',
    fehler=['Kontrolle nur als Endkontrolle sehen; sie begleitet die Umsetzung.'],
    src='Folien 302–304')

KAPITEL = kapitel('k11', 'Strategiewahl und Umsetzung',
    'Welchen Weg wählt das Unternehmen, und wie setzt es ihn um? Ansoff-Matrix, Porters Wettbewerbsstrategien, Implementierung und Kontrolle. Durchgehendes Beispiel: die Stride GmbH.',
    ['Ansoff', 'Porter', 'Implementierung'],
    [t_ansoff, t_porter, t_impl])

from mehr2 import ergaenze
ergaenze(KAPITEL)
