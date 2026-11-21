import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *

# Durchgehendes Beispiel: weiter mit der Stride GmbH (Laufschuhe).

# ---------------------------------------------------------------- 1 SWOT
fig_swot = svg(360, 270,
    T(144, 18, 'Opportunities', 13, 800, 'middle', 'var(--muted)') + T(286, 18, 'Threats', 13, 800, 'middle', 'var(--muted)')
    + T(36, 90, 'Strengths', 13, 800, 'middle', 'var(--muted)') + T(36, 206, 'Weak-', 13, 800, 'middle', 'var(--muted)') + T(36, 222, 'nesses', 13, 800, 'middle', 'var(--muted)')
    + box(74, 30, 140, 116, 'SO\nStärken nutzen,\num Chancen zu\nergreifen', size=13, art='hl', tip='SO-Strategie: Mit den eigenen Stärken die Chancen des Marktes nutzen. Stride: gute Entwicklungsabteilung (S) + Trailrunning-Trend (O) → neue Trailschuh-Serie.')
    + box(218, 30, 138, 116, 'ST\nStärken nutzen,\num Bedrohungen\nabzuwehren', size=13, tip='ST-Strategie: Mit Stärken Bedrohungen abwehren. Stride: treue Laufvereine (S) gegen Billiganbieter (T) → Vereinsprogramm.')
    + box(74, 150, 140, 116, 'WO\nSchwächen aus-\ngleichen, um\nChancen zu nutzen', size=13, tip='WO-Strategie: Schwächen abbauen, damit man Chancen nutzen kann. Stride: kein Onlineshop (W) + Onlinekauf wächst (O) → Shop aufbauen.')
    + box(218, 150, 138, 116, 'WT\nSchwächen aus-\ngleichen, um Be-\ndrohungen abzu-\nwehren', size=13, tip='WT-Strategie: Schwächen abbauen, um Bedrohungen abzuwehren. Stride: hohe Kosten (W) + Preiskampf (T) → Produktion effizienter machen.'),
    'SWOT-Analyse mit Handlungsempfehlungen', maxw=420)

t_swot = thema('swot', 'Phase 3: SWOT-Analyse', star=True,
    kern='Die SWOT-Analyse ermittelt und bewertet die internen Stärken (Strengths) und Schwächen (Weaknesses) sowie die externen Chancen (Opportunities) und Risiken (Threats) und leitet daraus vier Handlungsempfehlungen ab: SO, ST, WO, WT.',
    kurz=p('Stride legt zwei Listen nebeneinander. <b>Innen</b>: Was können wir gut (Stärken), was schlecht (Schwächen)? <b>Außen</b>: Welche Chancen bietet der Markt, welche Bedrohungen gibt es?')
        + p('Die Kunst ist der dritte Schritt: Stärken und Schwächen mit Chancen und Risiken <b>kombinieren</b>. So entstehen vier Strategien, die <b>Handlungsempfehlungen</b>.'),
    fig=fw('Die vier Felder der SWOT-Matrix. Tippe auf die Felder.') + bild(fig_swot),
    figcap='nach Folie „Unternehmensanalyse: SWOT-Analyse“',
    article=h3('Wann, wie, Grenzen?')
        + p('„Ermittlung und Bewertung der unternehmensinternen Ressourcen und Fähigkeiten einer unternehmerischen Einheit mit anschließender Einteilung in Stärken, Schwächen, Chancen und Risiken.“')
        + merkliste('SWOT in drei Schritten', 'Vorgehen', ['Ermittlung der unternehmensinternen Ressourcen und Fähigkeiten (und der externen Einflüsse)', 'Bewertung der Ressourcen und Fähigkeiten', 'Ableiten von Handlungsempfehlungen'])
        + tabelle(['', 'Opportunities (extern)', 'Threats (extern)'], [
            ['Strengths (intern)', 'SO: Stärken nutzen, um Chancen zu ergreifen', 'ST: Stärken nutzen, um Bedrohungen abzuwehren'],
            ['Weaknesses (intern)', 'WO: Schwächen ausgleichen, um Chancen nutzen zu können', 'WT: Schwächen ausgleichen, um Bedrohungen abwehren zu können']])
        + bsp('SWOT einer Fluggesellschaft (Folie)', '',
              [('Stärken: niedrige Schulden, Star Alliance, Partnerschaften (Swiss, Bahn, Bus), Qualifikation der Piloten', 'intern'), ('Schwächen: Flugzeugflotte veraltet, hohe Personalkosten', 'intern'),
               ('Chancen: loyale Firmenkunden, Flughafen Frankfurt, Preisverfall des Euros', 'extern'), ('Bedrohungen: Volatilität des Ölpreises, Billigflieger', 'extern')])
        + p('<b>Wann</b> setzt man sie ein? In der Unternehmensanalyse, um Ausgangslage und Optionen zu verdichten. <b>Grenzen</b>: Die Einordnung ist subjektiv (ist etwas eine Stärke oder nicht?), die Analyse ist eine Momentaufnahme, und erst die Kombination der Felder liefert Empfehlungen.')
        + klausur_hinweis('In den Folien steht dazu „Klausur: Wann setze ich sie ein? Wie funktioniert sie? Grenzen?“. Wichtig: S und W sind intern, O und T extern.')
        + falle('Chancen und Stärken vermischen. Eine Stärke liegt im Unternehmen (gute Entwickler), eine Chance im Markt (Lauftrend).')
        + wahr('w-swot', [('Stärken und Schwächen sind interne Faktoren.', True, 'Opportunities und Threats sind extern.'),
                          ('Eine WT-Strategie nutzt Stärken, um Chancen zu ergreifen.', False, 'Das ist SO; WT gleicht Schwächen aus, um Bedrohungen abzuwehren.')]),
    merk='SWOT: Strengths, Weaknesses (intern), Opportunities, Threats (extern). Schritte: ermitteln, bewerten, Handlungsempfehlungen ableiten. SO, ST, WO, WT.',
    exam='SWOT erklären (wann, wie, Grenzen) und Faktoren intern/extern zuordnen; Strategien SO/ST/WO/WT.',
    fehler=['Interne und externe Faktoren vertauschen.'],
    src='Folien 269–273')

# ---------------------------------------------------------------- 2 Market-based vs. Resource-based View
fig_mbv = svg(360, 220,
    box(4, 6, 172, 70, 'Market-based View\noutside-in', size=13, tip='Das Unternehmen ist geprägt von Beziehungen zur Umwelt. Erfolg kommt aus der Position am Markt (Five Forces).')
    + box(184, 6, 172, 70, 'Resource-based View\ninside-out', size=13, art='hl', tip='Das Unternehmen ist ein Reservoir von Ressourcen. Erfolg kommt aus besonderen Ressourcen und Fähigkeiten.')
    + pfeil(90, 150, 90, 86) + T(90, 168, 'Markt', 13, 700, 'middle', 'var(--muted)') + T(90, 186, '→ Unternehmen', 13, 700, 'middle', 'var(--muted)')
    + pfeil(270, 86, 270, 150) + T(270, 168, 'Ressourcen', 13, 700, 'middle', 'var(--muted)') + T(270, 186, '→ Markt', 13, 700, 'middle', 'var(--muted)')
    + T(90, 212, 'kurzfristig', 12, 600, 'middle', 'var(--muted)') + T(270, 212, 'langfristig', 12, 600, 'middle', 'var(--muted)'),
    'Market-based View und Resource-based View', maxw=420)

t_mbv = thema('mbv-rbv', 'Market-based View und Resource-based View',
    kern='Der Market-based View (outside-in) sieht den Erfolg in der Position am Markt (Marktanteile, Produkt- und Kostenvorteile, kurzfristig). Der Resource-based View (inside-out) sieht ihn in besonderen Ressourcen (dauerhaft schwer angreifbar, langfristig).',
    kurz=p('Warum ist Stride erfolgreich? Antwort 1: weil sie sich im Markt gut positioniert, etwa günstiger als die Konkurrenz ist. Das ist der <b>Market-based View</b>: Man schaut von <b>außen nach innen</b>.')
        + p('Antwort 2: weil sie Entwicklerinnen hat, die keiner sonst hat. Das ist der <b>Resource-based View</b>: Man schaut von <b>innen nach außen</b>. Dafür braucht man die Ressourcenanalyse (nächstes Unterthema).'),
    fig=fw('Zwei Blickrichtungen. Tippe auf die Kästen.') + bild(fig_mbv),
    figcap='nach Folie „Unternehmensanalyse: Market-based View vs. Resource-based View“',
    article=h3('Die beiden Sichtweisen im Vergleich')
        + tabelle(['Merkmal', 'Market-based View', 'Resource-based View'], [
            ['Denkfigur', 'Unternehmen geprägt von Beziehungen zur Umwelt', 'Unternehmen als Reservoir von Ressourcen'],
            ['Perspektive', 'outside-in', 'inside-out'], ['Wettbewerbsobjekt', 'Marktanteile (gegenüber Konkurrenten)', 'Chancenanteile (zur Sicherung wettbewerbsrelevanter Ressourcen)'],
            ['Konkurrenzobjekt', 'Produkt- oder Kostenvorteile', 'Ressourcenvorteile'], ['Wettbewerbsvorteil', 'zeitlich befristet', 'dauerhaft, schwer angreifbar'],
            ['Planungshorizont', 'kurzfristig', 'langfristig'], ['Geschäftseinheiten', 'Profit Center', 'Center of Competence'],
            ['Instrument', 'Porters Five Forces', 'Ressourcenanalyse']])
        + wahr('w-mbv', [('Der Resource-based View blickt von innen nach außen.', True, 'Inside-out.'),
                         ('Im Market-based View sind Wettbewerbsvorteile dauerhaft und schwer angreifbar.', False, 'Zeitlich befristet; dauerhaft ist der Resource-based View.')]),
    merk='Market-based View: outside-in, Marktanteile, Produkt-/Kostenvorteile, befristet, kurzfristig, Profit Center, Five Forces. Resource-based View: inside-out, Ressourcenvorteile, dauerhaft, langfristig, Center of Competence.',
    exam='Merkmale den beiden Sichtweisen zuordnen.',
    fehler=['Outside-in und inside-out vertauschen.'],
    src='Folie 274')

# ---------------------------------------------------------------- 3 Ressourcenanalyse
def vrio():
    kopf = ['spezifisch?', 'selten?', 'Imitation\ngeschützt?', 'Substitution\ngeschützt?']
    zeilen = [['nein', 'ja', 'ja', 'ja'], ['ja', 'nein', 'nein', 'nein'], ['ja', 'ja', 'nein', 'nein'], ['ja', 'ja', 'ja', 'nein'], ['ja', 'ja', 'ja', 'ja']]
    s = ''
    for j, k in enumerate(kopf):
        s += T(8 + j * 70 + 35, 22, k, 12, 800, 'middle', 'var(--muted)')
    s += T(320, 22, 'Folge', 12, 800, 'middle', 'var(--muted)')
    for i, z in enumerate(zeilen):
        y = 42 + i * 36
        for j, v in enumerate(z):
            s += rechteck(8 + j * 70 + 6, y, 58, 28, 'var(--c2)' if v == 'ja' else 'var(--neg)', 'none', 6) + T(8 + j * 70 + 35, y + 18, v, 13, 800, 'middle', 'var(--on-primary)')
    s += tpg(T(320, 42 + 18, 'Nachteil', 13, 800, 'middle', 'var(--neg)'), 'Wettbewerbsnachteil, unterdurchschnittlicher Erfolg: Die Ressource passt nicht zum Unternehmen (nicht spezifisch).')
    s += T(320, 42 + 2 * 36 + 18, '…', 13, 800)
    s += tpg(T(320, 42 + 4 * 36 + 18, 'Vorteil', 13, 800, 'middle', 'var(--pos)'), 'Nur wenn alle vier Fragen mit Ja beantwortet werden: Wettbewerbsvorteil, überdurchschnittlicher Erfolg.')
    return svg(360, 228, s, 'Ressourcenanalyse: vier Fragen', maxw=420)


t_res = thema('ressourcen', 'Ressourcenanalyse: Welche Ressource bringt Wettbewerbsvorteile?', star=True,
    kern='Ressourcen sind materiell (Sach- und Finanzanlagen) oder immateriell (organisatorisch, human). Einen dauerhaften Wettbewerbsvorteil bringt eine Ressource nur, wenn sie spezifisch, selten, vor Imitation geschützt und vor Substitution geschützt ist.',
    kurz=p('Stride hat eine Schuhtechnik, die kein anderer hat. Bringt das einen dauerhaften Vorteil? Vier Fragen: Ist die Ressource <b>spezifisch</b> (passt sie genau zu uns)? Ist sie <b>selten</b>? Ist sie <b>vor Imitation geschützt</b>? Ist sie <b>vor Substitution geschützt</b>?')
        + p('Nur wenn alle vier Antworten <b>ja</b> lauten, entsteht ein <b>Wettbewerbsvorteil</b> mit überdurchschnittlichem Erfolg. Ist schon die erste Antwort nein, ist es ein Wettbewerbsnachteil.'),
    fig=fw('Die Tabelle der Folie. Tippe auf „Nachteil“ und „Vorteil“.') + bild(vrio()),
    figcap='nach Folie „Ressourcenanalyse“ (Ist die Ressource …)',
    article=h3('Arten von Ressourcen')
        + mfig('Ressourcenarten', svg(560, 200,
            box(210, 6, 140, 36, 'Ressourcen', art='hl', size=13) + pfeil(250, 44, 120, 62) + pfeil(310, 44, 420, 62)
            + box(30, 64, 180, 36, 'Materielle Ressourcen', size=13) + box(330, 64, 200, 36, 'Immaterielle Ressourcen', size=13)
            + box(30, 116, 180, 70, 'Sachanlagen\nFinanzanlagen', size=13, art='weak')
            + box(250, 116, 140, 70, 'Organisatorisch\nVerfahrensweisen\nProduktionsprozesse', size=12, art='weak', tip='Beispiel McDonald’s: Die Abläufe sind der Vorteil, nicht besonders gute Mitarbeiter.')
            + box(400, 116, 150, 70, 'Human\nFähigkeiten\nFertigkeiten', size=12, art='weak', tip='Beispiel SAP-Beratung: Branchenwissen und Können der Mitarbeiter.')
            + pfeil(430, 102, 320, 114) + pfeil(430, 102, 474, 114),
            'Ressourcenarten'), 'nach Folie „Ressourcenanalyse“')
        + weiter('Welche Ressource bringt einen echten Vorteil? Dafür gibt es vier Prüffragen.')
        + h3('Vier Prüffragen')
        + tabelle(['Frage', 'Bedeutung'], [
            ['spezifisch?', 'Passt die Ressource genau zu diesem Unternehmen und seinem Geschäft?'], ['selten?', 'Haben andere sie auch?'],
            ['vor Imitation geschützt?', 'Kann man sie nachmachen (Patent, Wissen, Kultur)?'], ['vor Substitution geschützt?', 'Kann man sie durch etwas anderes ersetzen?']])
        + p('Nur bei viermal „ja“ entsteht ein <b>Wettbewerbsvorteil</b> mit überdurchschnittlichem Erfolg. Fehlt eine Eigenschaft, ist der Vorteil kleiner oder nur vorübergehend. Beispiele der Vorlesung: Ein Burgerladen mit nicht spezifischen Ressourcen hat einen Nachteil; SAP-Berater mit seltenem, geschütztem Branchenwissen einen Vorteil.')
        + bsp('Klausurfall Holzerei', 'Eine Holzerei mit drei Mitarbeitern stellt einen Elektroingenieur ein. Welche Voraussetzung des Ressourcenansatzes ist typischerweise verletzt? a) spezifisch b) Seltenheit c) Imitation d) Substitution',
              [('Ein Elektroingenieur ist eine wertvolle Ressource, aber nicht für eine kleine Holzerei.', ''), ('Er passt nicht zum Geschäft des Unternehmens.', 'a) spezifisch')])
        + klausur_hinweis('Diese Fallfrage kam schon: Prüfe immer zuerst, ob die Ressource überhaupt zum Unternehmen passt (spezifisch).')
        + wahr('w-res', [('Eine Ressource bringt nur dann einen Wettbewerbsvorteil, wenn alle vier Fragen mit Ja beantwortet werden.', True, 'Spezifisch, selten, imitations- und substitutionsgeschützt.'),
                         ('Fähigkeiten von Mitarbeitern sind materielle Ressourcen.', False, 'Humane, also immaterielle Ressourcen.')]),
    merk='Ressourcen: materiell (Sach-, Finanzanlagen), immateriell (organisatorisch: Verfahren, Prozesse; human: Fähigkeiten, Fertigkeiten). Wettbewerbsvorteil nur, wenn spezifisch + selten + vor Imitation + vor Substitution geschützt.',
    exam='Fall zur verletzten Voraussetzung des Ressourcenansatzes lösen (Holzerei → spezifisch).',
    fehler=['Seltenheit wählen, obwohl die Ressource gar nicht zum Unternehmen passt.'],
    src='Folien 275–276')

# ---------------------------------------------------------------- 4 Renten
fig_renten = svg(360, 252,
    T(180, 16, 'Quelle von Gewinn: vier Rentenarten', 13, 800)
    + box(4, 28, 172, 104, 'Ricardo-Rente\nknappe Ressourcen\n→ kostengünstiger\ninput-orientiert', size=12, tip='Verfügungsgewalt über knappe Ressourcen, die es erlauben, kostengünstiger zu produzieren. Beispiele: besserer Zugang zu High Potentials in Metropolregionen, Zugang zu billiger Energie.')
    + box(184, 28, 172, 104, 'Quasi-Rente\noptimaler Einsatz\nvon Ressourcen\nintermediär', size=12, tip='Spezifischer (optimaler) Einsatz von Ressourcen. Beispiele: optimale Teamzusammenstellung, überlegene Mitarbeiterauswahl, Wissensmanagement-Systeme.')
    + box(4, 140, 172, 104, 'Monopol-Rente\nEintrittsbarrieren\ndurch Marktmacht\ninput/output-orient.', size=12, art='hl', tip='Errichtung von Markteintrittsbarrieren durch Marktmacht. Beispiele: Standortvorteile, Image, überdurchschnittliche Vergütung als Instrument des Personalmarketings, Skaleneffekte.')
    + box(184, 140, 172, 104, 'Schumpeter-Rente\nInnovation schafft\nPioniergewinne\noutput-orientiert', size=12, tip='Innovationsfähigkeit schafft Pioniergewinne (und den Aufbau von Monopol-Renten): schneller den Markt lesen. Beispiele: Change-Management-Kultur, innovationsfördernde Praktiken.'),
    'Vier Rentenarten', maxw=420)

t_renten = thema('renten', 'Renten: Ricardo, Quasi, Monopol, Schumpeter', star=True,
    kern='Renten erklären, woher überdurchschnittlicher Gewinn kommt: Ricardo-Renten aus knappen Ressourcen (input-orientiert), Quasi-Renten aus optimalem Ressourceneinsatz (intermediär), Monopol-Renten aus Markteintrittsbarrieren (z. B. Skaleneffekte) und Schumpeter-Renten aus Innovation (output-orientiert).',
    kurz=p('Eine IT-Beratung in Frankfurt findet leichter Top-Leute als eine in den Alpen: Sie hat Zugang zu einer <b>knappen Ressource</b> und verdient eine <b>Ricardo-Rente</b>. Ein Team, das perfekt zusammengestellt ist, verdient eine <b>Quasi-Rente</b>.')
        + p('Wer Skaleneffekte oder ein starkes Image hat, hält andere vom Markt fern: <b>Monopol-Rente</b>. Wer als Erster mit einer Innovation kommt, verdient eine <b>Schumpeter-Rente</b>. „Im Zweifel auswendig lernen“: In der Klausur wird ein Sachverhalt beschrieben und gefragt, welche Rente das ist.'),
    fig=fw('Die vier Renten. Tippe auf die Felder für Beispiele.') + bild(fig_renten),
    figcap='nach Folie „Ressourcenanalyse“ (Renten-Tabelle)',
    article=h3('Die Tabelle der Vorlesung')
        + tabelle(['', 'Ricardo-Renten', 'Quasi-Renten', 'Monopol-Renten', 'Schumpeter-Renten'], [
            ['Wirkung', 'Verfügungsgewalt über knappe Ressourcen, die es erlauben, kostengünstiger zu produzieren', 'spezifischer (optimaler) Einsatz von Ressourcen', 'Errichtung von Markteintrittsbarrieren durch Marktmacht', 'Innovationsfähigkeit schafft Pioniergewinne (und den Aufbau von Monopol-Renten)'],
            ['Verortung', 'input-orientiert', 'intermediär', 'input- oder output-orientiert', 'output-orientiert'],
            ['Beispiel', 'besserer Zugang zu High Potentials in Metropolregionen; Zugang zu billiger Energie', 'optimale Teamzusammenstellung; überlegene Mitarbeiterauswahl; Wissensmanagement-Systeme', 'Standortvorteile, Image, überdurchschnittliche Vergütung (Personalmarketing), <b>Skaleneffekte</b>', 'Change-Management-Kultur; innovationsfördernde Praktiken']])
        + bsp('Klausurfall Skaleneffekte', 'Einem Unternehmen gelingt es, Skaleneffekte zu erzielen. Welche Rentenart wird beschrieben?',
              [('Skaleneffekte stehen in der Tabelle bei den Monopol-Renten: Sie wirken als Markteintrittsbarriere.', 'Monopol-Rente')],
              'Bei den Antwortmöglichkeiten „Ricardo-Rente“ und „Quasi-Rente“: Keine passt sauber. Ricardo verlangt eine knappe Ressource, Quasi einen optimalen Einsatz. Lies alle Möglichkeiten und achte auf die Stichworte der Tabelle.')
        + bsp('Zuordnen', 'Welche Rente?',
              [('Ein Rechenzentrum sitzt neben einem Wasserkraftwerk mit billigem Strom.', 'Ricardo'), ('Ein Start-up bringt als Erstes eine neue App auf den Markt.', 'Schumpeter'), ('Ein Unternehmen stellt Teams aus genau passenden Spezialisten zusammen.', 'Quasi'), ('Eine Marke hat ein so starkes Image, dass Neue kaum Kunden finden.', 'Monopol')])
        + falle('Ricardo und Quasi verwechseln: Ricardo = <b>Besitz</b> einer knappen Ressource; Quasi = <b>Einsatz</b> (Kombination) von Ressourcen.')
        + wahr('w-ren', [('Schumpeter-Renten entstehen durch Innovationen.', True, 'Pioniergewinne.'),
                         ('Ricardo-Renten sind output-orientiert.', False, 'Input-orientiert.'),
                         ('Skaleneffekte werden in der Vorlesung den Monopol-Renten zugeordnet.', True, 'Markteintrittsbarriere.')]),
    merk='Ricardo: knappe Ressourcen → kostengünstiger (input). Quasi: optimaler Ressourceneinsatz (intermediär). Monopol: Eintrittsbarrieren durch Marktmacht, z. B. Skaleneffekte, Image, Standort (input/output). Schumpeter: Innovation → Pioniergewinne (output).',
    exam='Einen Sachverhalt der richtigen Rentenart zuordnen (Auswahlfrage).',
    fehler=['Ricardo (Besitz) und Quasi (Einsatz) verwechseln.', 'Skaleneffekte der Ricardo-Rente zuordnen.'],
    src='Folie 277')

# ---------------------------------------------------------------- 5 Lebenszyklus
def lzk():
    X = lambda t: 30 + t * 3.2
    Y = lambda v: 140 - v * 1.1
    s = pfeil(30, 140, 350, 140) + pfeil(30, 230, 30, 10) + T(346, 156, 'Zeit', 12, 600, 'end', 'var(--muted)')
    um = [(X(t), Y(100 * math.exp(-((t - 55) / 24) ** 2))) for t in range(0, 101, 2)]
    ge = [(X(t), Y(70 * math.exp(-((t - 50) / 20) ** 2) - 25 * math.exp(-((t - 12) / 9) ** 2) - 5)) for t in range(0, 101, 2)]
    s += linie(um, 'var(--c2)', 3) + linie(ge, 'var(--primary)', 3)
    for i, (n, a, b) in enumerate([('Einführung', 0, 25), ('Wachstum', 25, 50), ('Reife', 50, 75), ('Sättigung', 75, 100)]):
        s += strich(X(b), 20, X(b), 230) if b < 100 else ''
        s += tpg(T(X((a + b) / 2), 24, n, 12, 800), ['Einführung: Umsatz klein, Investitionen hoch, Verlust.', 'Wachstum: Umsatz steigt schnell, die Gewinnschwelle wird überschritten.', 'Reife: Umsatz-Maximum, Gewinn am höchsten.', 'Sättigung: Umsatz sinkt; absetzen oder weiterentwickeln (z. B. Facelift beim Auto).'][i])
    s += linie([(170, 222), (196, 222)], 'var(--c2)', 3) + T(200, 226, 'Umsatz', 12, 800, 'start', 'var(--c2)') + linie([(260, 222), (286, 222)], 'var(--primary)', 3) + T(290, 226, 'Gewinn', 12, 800, 'start', 'var(--primary)')
    s += T(X(10), 196, 'Verlust', 12, 700, 'middle', 'var(--neg)')
    return svg(360, 240, s, 'Produktlebenszyklus', maxw=420)

t_lzk = thema('lebenszyklus', 'Lebenszyklusmodell',
    kern='Jedes Produkt durchläuft einen typischen Prozess: Einführung, Wachstum, Reife, Sättigung. Erst Verlust (Investitionen), dann Gewinnschwelle, Umsatz-Maximum in der Reife, danach Rückgang. Ein idealisiertes Modell, kein Naturgesetz.',
    kurz=p('Ein neuer Laufschuh kostet erst einmal Geld (Entwicklung, Werbung) und verkauft sich kaum: <b>Einführung</b>. Dann spricht er sich herum: <b>Wachstum</b>. Irgendwann hat ihn jeder: <b>Reife</b> mit dem höchsten Umsatz. Danach sinkt der Umsatz: <b>Sättigung</b>.')
        + p('Am Ende muss man entscheiden: Produkt <b>absetzen</b> oder <b>weiterentwickeln</b> (neues Feature, Facelift).'),
    fig=fw('Umsatz und Gewinn über den Lebenszyklus. Tippe auf die Phasen.') + bild(lzk()),
    figcap='nach Folie „Unternehmensanalyse: Lebenszyklusmodell“',
    article=h3('Vier Phasen')
        + tabelle(['Phase', 'Umsatz', 'Gewinn'], [['Einführung', 'klein', 'Verlust (Investitionen)'], ['Wachstum', 'steigt stark', 'Gewinnschwelle wird überschritten'], ['Reife', 'Umsatz-Maximum', 'hoch'], ['Sättigung', 'sinkt', 'sinkt, bis zur Verlustschwelle']])
        + p('Das Modell ist eine <b>idealisierte Idee</b>: tausendfach nachgewiesen, aber kein Naturgesetz. Es hilft, ein Gefühl für die Lage eines Produkts zu bekommen. Ausnahmen entstehen durch neue Features oder ein Facelift, das den Zyklus verlängert.')
        + wahr('w-lzk', [('In der Einführungsphase macht ein Produkt meist Verlust.', True, 'Hohe Investitionen, wenig Umsatz.'),
                         ('Der Lebenszyklus ist ein Naturgesetz.', False, 'Idealisiert, kein Naturgesetz.')]),
    merk='Lebenszyklus: Einführung (Verlust) → Wachstum (Gewinnschwelle) → Reife (Umsatz-Maximum) → Sättigung (Rückgang; absetzen oder weiterentwickeln). Idealisiert, kein Naturgesetz.',
    exam='Phasen und typische Umsatz-/Gewinnlage zuordnen.',
    fehler=['Das Umsatz-Maximum in die Wachstumsphase legen.'],
    src='Folie 278')

# ---------------------------------------------------------------- 6 Erfahrungskurve
def ekurve():
    X = lambda m: 40 + m * 37
    Y = lambda k: 210 - k * 1.8
    s = achsen(40, 210, 350, 10, '', 'Stückkosten') + T(350, 246, 'kumulierte Menge (Verdopplungen)', 12, 600, 'end', 'var(--muted)')
    pts = []
    for i in range(8):
        k = 100 * 0.75 ** i
        pts.append((X(i), Y(k)))
        s += tpg(punkt(X(i), Y(k), 'var(--primary)', 5), f'Nach {i} Verdopplung(en): Stückkosten {round(k)} (bei 25 % Senkung je Verdopplung).')
        s += T(X(i), 226, ['1', '2', '4', '8', '16', '32', '64', '128'][i], 12)
    s += linie(pts, 'var(--primary)', 2.5)
    s += T(X(1) + 8, Y(75) - 8, '−20 bis 30 % je Verdopplung', 13, 800, 'start', 'var(--primary)')
    return svg(360, 254, s, 'Erfahrungskurve', maxw=420)

t_ek = thema('erfahrungskurve', 'Erfahrungskurve',
    kern='Bei jeder Verdopplung der eigenen kumulierten Produktionsmenge sinken die eigenen Stückkosten um 20–30 %. Gründe: Lerneffekte, Spezialisierung, Rationalisierung, Know-how und technischer Fortschritt.',
    kurz=p('Den ersten Schuh einer neuen Serie zu bauen dauert lange. Beim tausendsten weiß jeder, was zu tun ist. Die <b>Erfahrungskurve</b> sagt: Bei jeder <b>Verdopplung</b> der (eigenen) Produktionsmenge sinken die (eigenen) Kosten um <b>20 bis 30 %</b>.')
        + p('Das hilft, die eigene Kostenstruktur zu verstehen, über „selbst herstellen oder einkaufen“ zu entscheiden und die Kosten der Konkurrenz zu schätzen.'),
    fig=fw('Stückkosten über die Verdopplungen (Beispiel mit 25 %). Tippe auf die Punkte.') + bild(ekurve()),
    figcap='nach Folien „Unternehmensanalyse: Erfahrungskurve“',
    article=h3('Aussage und Gründe')
        + p('„Bei einer Verdoppelung der (eigenen) Produktionsmenge sinken die (eigenen) Kosten um 20–30 %.“ Gemeint ist die <b>kumulierte</b> Menge, also alles, was man bisher insgesamt produziert hat.')
        + cards([('Lerneffekte', 'Übung macht schneller.'), ('Spezialisierungseffekte', 'Arbeitsteilung: Jeder macht, was er am besten kann.'), ('Rationalisierungseffekte', 'Prozesse werden verbessert, Automatisierung (Economies of Scale).'), ('Know-how, technischer Fortschritt', 'Bessere Technik verbessert das Produkt und den Prozess.')])
        + bsp('Rechnen mit der Erfahrungskurve', 'Ein Schuh kostet nach 10.000 Stück 40 €. Die Kosten sinken je Verdopplung um 20 %.',
              [('20.000 Stück: 40 · 0,8', '32 €'), ('40.000 Stück: 32 · 0,8', '25,60 €')])
        + p('Nutzen: Die Kosten der Wettbewerber lassen sich auf Basis der eigenen Erfahrungskurve schätzen. Wer mehr produziert hat, kann günstiger anbieten.')
        + wahr('w-ek', [('Die Erfahrungskurve bezieht sich auf die Verdopplung der kumulierten Menge.', True, 'Nicht auf die Menge pro Jahr.'),
                        ('Laut Erfahrungskurve sinken die Kosten je Verdopplung um etwa 50 %.', False, 'Um 20–30 %.')]),
    merk='Erfahrungskurve: Verdopplung der kumulierten eigenen Menge → Stückkosten −20 bis 30 %. Gründe: Lernen, Spezialisierung, Rationalisierung, Know-how/Fortschritt. Nutzen: Kostenstruktur, make or buy, Konkurrenz schätzen.',
    exam='Aussage der Erfahrungskurve und ihre Ursachen; einfache Rechnung je Verdopplung.',
    fehler=['Die Prozentsenkung auf jede zusätzliche Einheit statt auf jede Verdopplung beziehen.'],
    src='Folien 279–281')

# ---------------------------------------------------------------- 7 BCG
fig_bcg = svg(360, 280,
    pfeil(50, 236, 350, 236) + pfeil(50, 236, 50, 10)
    + T(200, 268, 'relativer Marktanteil →', 13, 700, 'middle', 'var(--muted)') + T(14, 124, 'Marktwachstum →', 13, 700, 'middle', 'var(--muted)').replace('<text ', '<text transform="rotate(-90 14 124)" ', 1)
    + T(110, 252, 'niedrig', 12, 400, 'middle', 'var(--muted)') + T(280, 252, 'hoch', 12, 400, 'middle', 'var(--muted)')
    + box(58, 16, 140, 104, 'Question\nMarks\n(Fragezeichen)', size=13, tip='Hohes Marktwachstum, niedriger relativer Marktanteil: der unbestimmteste Teil. Entscheidung: alles investieren oder raus.')
    + box(206, 16, 140, 104, 'Stars', size=14, art='hl', tip='Hohes Wachstum, hoher Marktanteil: investieren, um die Position zu halten. Später werden Stars zu Cash Cows.')
    + box(58, 126, 140, 104, 'Poor Dogs', size=14, tip='Niedriges Wachstum, niedriger Marktanteil: beenden (desinvestieren).')
    + box(206, 126, 140, 104, 'Cash Cows', size=14, tip='Niedriges Wachstum, hoher Marktanteil: melken. Sie bringen das Geld, mit dem man Stars und Question Marks finanziert.'),
    'BCG-Matrix', maxw=420)

t_bcg = thema('bcg-matrix', 'BCG-Matrix (Portfolio)', star=True,
    kern='Die BCG-Matrix (Boston Consulting Group) ordnet Produkte nach Marktwachstum und relativem Marktanteil: Question Marks (alles oder raus), Stars (investieren), Cash Cows (abschöpfen) und Poor Dogs (beenden).',
    kurz=p('Stride hat mehrere Produkte: eine neue Trail-Serie in einem boomenden Markt, aber mit wenig Marktanteil; einen Bestseller-Straßenschuh in einem gesättigten Markt; ein Auslaufmodell. Die <b>BCG-Matrix</b> sortiert sie in vier Felder.')
        + p('Die Achsen: <b>Marktwachstum</b> (wie schnell wächst der Markt?) und <b>relativer Marktanteil</b> (wie stark bin ich im Vergleich zum größten Konkurrenten?). Daraus folgen klare Handlungsempfehlungen.'),
    fig=fw('Die vier Felder der Matrix. Tippe auf die Felder.') + bild(fig_bcg),
    figcap='nach Folie „Unternehmensanalyse: BCG-Matrix“',
    article=h3('Vier Felder, vier Empfehlungen')
        + tabelle(['Feld', 'Marktwachstum', 'rel. Marktanteil', 'Empfehlung'], [
            ['Question Marks', 'hoch', 'niedrig', 'unbestimmtester Teil: alles investieren oder raus'],
            ['Stars', 'hoch', 'hoch', 'investieren, Position halten'],
            ['Cash Cows', 'niedrig', 'hoch', 'abschöpfen („melken“), finanziert die anderen'],
            ['Poor Dogs', 'niedrig', 'niedrig', 'beenden']])
        + p('Der Mehrwert: Die Matrix hilft, einen Überblick über das Portfolio zu bekommen. Sie zeigt aber die historische Leistung; die Zukunft muss man selbst einschätzen.')
        + bsp('Einordnen', 'Stride: Trailschuhe (Markt wächst 15 %, Marktanteil klein), Straßenschuh (Markt wächst 1 %, Marktführer), Hallenschuh (Markt schrumpft, kleiner Anteil).',
              [('Trailschuhe', 'Question Mark'), ('Straßenschuh', 'Cash Cow'), ('Hallenschuh', 'Poor Dog')])
        + klausur_hinweis('Auswahlfrage BCG-Matrix: Achsen und Felder sicher kennen. Cash Cow = niedriges Wachstum + hoher Marktanteil.')
        + wahr('w-bcg', [('Cash Cows haben einen hohen Marktanteil in einem wenig wachsenden Markt.', True, 'Sie liefern Geld.'),
                         ('Stars sollte man beenden.', False, 'Stars: investieren. Beenden: Poor Dogs.'),
                         ('Die Achsen der BCG-Matrix sind Marktwachstum und relativer Marktanteil.', True, 'Senkrecht Wachstum, waagerecht Marktanteil.')]),
    merk='BCG: Achsen Marktwachstum (senkrecht) und relativer Marktanteil (waagerecht). Question Marks (hoch/niedrig): alles oder raus. Stars (hoch/hoch): investieren. Cash Cows (niedrig/hoch): melken. Poor Dogs (niedrig/niedrig): beenden.',
    exam='Felder und Normstrategien der BCG-Matrix zuordnen (Auswahlfrage).',
    fehler=['Cash Cows und Stars vertauschen.', 'Absoluten statt relativen Marktanteil nehmen.'],
    src='Folie 282')

KAPITEL = kapitel('k10', 'Unternehmensanalyse',
    'Wo steht das Unternehmen? SWOT, Market- und Resource-based View, Ressourcen und Renten, Lebenszyklus, Erfahrungskurve und BCG-Matrix. Durchgehendes Beispiel: die Stride GmbH.',
    ['SWOT', 'MBV/RBV', 'Ressourcen', 'Renten', 'Lebenszyklus', 'Erfahrungskurve', 'BCG'],
    [t_swot, t_mbv, t_res, t_renten, t_lzk, t_ek, t_bcg])

from mehr2 import ergaenze
ergaenze(KAPITEL)
