"""Von Hand geschriebene Fragen zu Klausurpunkten, die die Merklisten nicht abdecken (je Fach).
Familien „:kp-…“ → inhalte/<fach>/fragen_neu.json, Karten (q='kp', kr=1) → karten.json. Wiederholbar.
Aufruf: python3 werkzeuge/klausurpunkte.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from merklisten import IN, txt


def F(fid, t, k, nid, z, *a): return dict(id=f'{fid}:{t}:kp-{nid}', f=fid, t=t, k=k, s=True, y='fam', fam=1, z=z, a=list(a))
def liste(p, pk, n=None, lvl=2, w=''): return dict(y='liste', p=p, pk=pk, n=n or len(pk), w=w, klausur=True, lvl=lvl)
def mc(p, richtig, falsch, w='', lvl=1): return dict(y='mc', p=p, o=[[richtig, True]] + [[x, False] for x in falsch], w=w, lvl=lvl)
def luecke(p, l, w='', lvl=2): return dict(y='luecke', p=p, l=l, w=w, lvl=lvl)
def zuord(p, k, e, lvl=1): return dict(y='zuord', p=p, k=k, e=e, w='', lvl=lvl)
def rev(p, l, pk, lvl=3): return dict(y='rev', p=p, l=l, pk=pk, w='', klausur=True, lvl=lvl)
def karte(t, v, r): return dict(t=t, v=v, r=r, b=1, kr=1, q='kp')


LOGISTIK = dict(fams=[
    F('logistik', 'prodlog', 3, 'nc', 'Kann NC, CNC und DNC unterscheiden',
      liste('Nennen Sie drei Maschinentypen der Produktion 4.0.', [['NC', 'numerical control'], ['CNC', 'computerized'], ['DNC', 'direct', 'distributed']]),
      mc('Welche Steuerung lenkt mehrere CNC- und NC-Maschinen von einem Rechner aus?', 'DNC', ['CNC', 'NC', 'SPS']),
      mc('Eine Maschine bearbeitet ein ganzes Werkstück mit mehreren Arbeitsgängen automatisch. Welcher Typ?', 'CNC', ['NC', 'DNC', 'Handarbeitsplatz']),
      luecke('<b>[[0]]</b>-Maschine: ein einzelner Fertigungsvorgang läuft automatisch nach einem Programm ab.', [['NC', 'nc']]),
      zuord('Ordne zu: Welcher Maschinentyp?', ['NC', 'CNC', 'DNC'], [['ein Fertigungsvorgang automatisch', 0], ['ganzes Werkstück, mehrere Vorgänge', 1], ['steuert mehrere NC- und CNC-Maschinen', 2]])),
    F('logistik', 'fertigungsarten', 3, 'formen', 'Kann die Fertigungsarten mit Vor- und Nachteil erklären',
      liste('Nennen Sie vier Fertigungsarten bzw. Organisationsformen der Fertigung.', [['Werkstattfertigung', 'Werkstatt'], ['Serienfertigung', 'Serie'], ['Fließfertigung', 'Fließ', 'Reihe'],
            ['Massenfertigung', 'Masse'], ['Fertigungsinsel', 'Fertigungszelle', 'Insel', 'Zelle'], ['Einzelfertigung']], n=4),
      zuord('Welche Fertigungsart passt?', ['Werkstattfertigung', 'Fließfertigung', 'Fertigungsinsel/-zelle'],
            [['gleichartige Maschinen stehen zusammen, das Teil wandert', 0], ['Maschinen in der Reihenfolge der Arbeitsgänge', 1], ['eine Teilefamilie wird komplett bearbeitet', 2],
             ['flexibel, aber hohe Rüst- und Durchlaufzeiten', 0], ['hohe Auslastung, wenig Rüsten, hohe Investition', 1], ['NC-, CNC- und DNC-Maschinen arbeiten zusammen', 2]]),
      mc('Werkstattfertigung: Was ist der typische Nachteil?', 'lange Durchlaufzeiten', ['hohe Investition', 'geringe Flexibilität', 'nur ein Produkt']),
      mc('Fertigungsinsel: Was wird dort bearbeitet?', 'eine Teilefamilie komplett', ['nur ein Arbeitsgang', 'nur Einzelstücke', 'nur Rohstoffe']),
      luecke('Bei der <b>[[0]]</b> stehen die Maschinen in der Reihenfolge der Arbeitsgänge; das Teil läuft ohne Umwege durch.', [['Fließfertigung', 'fließfertigung', 'Reihenfertigung']])),
    F('logistik', 'kontrakt', 7, 'pl', 'Kann 1PL bis 5PL nennen und erklären',
      liste('Nennen Sie die fünf Formen der Kontraktlogistik.', [['1PL', 'eigene Logistik'], ['2PL', 'Spediteur', 'Transport'], ['3PL', 'Systemdienstleister', 'Value Added'], ['4PL', 'Systemintegrator'], ['5PL', 'Beratung', 'SCM']]),
      mc('Welcher Dienstleister koordiniert als Systemintegrator, hat aber keine eigenen Fahrzeuge?', '4PL', ['2PL', '3PL', '1PL']),
      luecke('<b>[[0]]</b>: Systemdienstleister, der zusätzlich Value Added Services wie Montage oder Etikettierung übernimmt.', [['3PL', '3pl']])),
    F('logistik', 'auktionen', 7, 'arten', 'Kann die Auktionsarten nennen und erklären',
      liste('Nennen Sie vier Arten von Auktionen.', [['Englische Auktion', 'Englisch'], ['Holländische Auktion', 'Holländisch'], ['Höchstpreisauktion', 'Höchstpreis', 'verdeckt'],
            ['Vickrey-Auktion', 'Vickrey', 'Zweitpreis'], ['Reverse Auktion', 'Reverse', 'umgekehrt'], ['Scorecard-Auktion', 'Scorecard']], n=4),
      mc('Bei welcher Auktion gewinnt der Höchstbietende, zahlt aber nur das zweithöchste Gebot?', 'Vickrey-Auktion', ['Holländische Auktion', 'Englische Auktion', 'Reverse Auktion']),
      mc('Reverse Auktion: Wer gewinnt?', 'der billigste Anbieter', ['der höchste Bieter', 'der erste Bieter', 'der beste Lieferant']),
      luecke('Bei der <b>[[0]]</b> Auktion fällt der Preis, bis der erste Bieter zuschlägt.', [['holländischen', 'Holländischen', 'hollaendischen']])),
    F('logistik', 'lieferanten', 5, 'tier', 'Kann die Lieferantenpyramide mit Beispielen erklären',
      liste('Nennen Sie die drei Stufen der Lieferantenpyramide mit je einem Beispiel.', [['1st Tier', 'System', 'Modul'], ['2nd Tier', 'Komponent'], ['3rd Tier', 'Rohmaterial', 'Normteil', 'DIN']]),
      zuord('Welche Stufe der Lieferantenpyramide?', ['1st Tier', '2nd Tier', '3rd Tier'], [['Cockpit-Modul fertig montiert', 0], ['Tachometer als Komponente', 1], ['Schrauben, DIN-Teile, Rohmaterial', 2]]),
      luecke('<b>[[0]]</b>-Lieferanten liefern ganze Systeme und Module direkt an den Hersteller.', [['1st Tier', '1st-Tier', 'First Tier']])),
    F('logistik', 'm-lagertypen', 12, 'durchlauf', 'Kann Vor- und Nachteile des Durchlaufregals nennen',
      liste('Nennen Sie drei Vorteile des Durchlaufregals.', [['FIFO', 'first in'], ['Flächennutzung', 'Platz'], ['automatisierbar', 'Automatisierung'], ['getrennte Ein- und Auslagerung', 'Einlagerung', 'Entnahme']], n=3),
      liste('Nennen Sie zwei Nachteile des Durchlaufregals.', [['störanfällig', 'Störung'], ['ein Artikel je Kanal', 'nur ein Artikel'], ['teuer', 'Antrieb', 'Investition']], n=2),
      mc('Warum ist FIFO beim Durchlaufregal zwangsläufig?', 'Eingelagert wird hinten, entnommen vorn', ['Ein Rechner sortiert die Ware', 'Jedes Fach hat ein Datum', 'Der Stapler fährt im Kreis'])),
], karten=[
    karte('prodlog', 'NC-Maschine', 'Numerical Control: ein einzelner Fertigungsvorgang läuft automatisch nach Programm.'),
    karte('prodlog', 'CNC-Maschine', 'Computerized Numerical Control: bearbeitet ein ganzes Werkstück mit mehreren Vorgängen automatisch.'),
    karte('prodlog', 'DNC-System', 'Direct/Distributed Numerical Control: ein Rechner steuert mehrere CNC- und NC-Maschinen.'),
    karte('fertigungsarten', 'Werkstattfertigung', 'Gleichartige Maschinen stehen zusammen, das Teil wandert von Werkstatt zu Werkstatt; flexibel, aber lange Durchlaufzeiten.'),
    karte('fertigungsarten', 'Fertigungsinsel / Fertigungszelle', 'NC-, CNC- und DNC-Maschinen bearbeiten eine Teilefamilie komplett; flexibel und weitgehend automatisch.'),
    karte('lieferanten', '1st-Tier-Lieferant', 'System- oder Modullieferant, liefert direkt an den Hersteller (z. B. Cockpit); enge Partnerschaft.'),
    karte('lieferanten', '2nd-Tier-Lieferant', 'Komponentenlieferant, liefert an den 1st-Tier-Lieferanten (z. B. Tachometer).'),
    karte('lieferanten', '3rd-Tier-Lieferant', 'Rohmaterial-, Norm- und DIN-Teile-Lieferant; leicht austauschbar (z. B. Schrauben).'),
    karte('auktionen', 'Reverse Auktion', 'Einkaufsauktion: Lieferanten unterbieten sich, der billigste Anbieter erhält den Zuschlag.'),
    karte('auktionen', 'Vickrey-Auktion', 'Verdeckte Auktion: Der Höchstbietende gewinnt, zahlt aber nur das zweithöchste Gebot.'),
])


PRODUKTION = dict(fams=[
    F('produktion', 'ds-platform', 5, 'effects', 'Can explain base value, network value and the three network effects',
      zuord('Which network effect is it?', ['direct', 'indirect', 'two-sided'], [['more WhatsApp users make WhatsApp more useful', 0], ['more Android users attract more apps', 1],
            ['Uber: more riders attract more drivers', 2], ['more telephone owners, more people to call', 0], ['Windows users attract Office software', 1], ['game console: players ↔ game makers', 2]]),
      mc('VISA: what is the base value of a credit card?', 'paying without cash, even if few shops accept it', ['more shops accept it because more people use it', 'more banks issue it because shops accept it', 'the card gets cheaper with more users']),
      mc('Which effect describes “more users attract more complementary products”?', 'indirect', ['direct', 'two-sided', 'base value']),
      luecke('<b>[[0]]</b> value: what the good is worth on its own, even with only one user.', [['Base', 'base']]),
      luecke('<b>[[0]]</b> value: what other users and partners add to the good.', [['Network', 'network']])),
    F('produktion', 'sv-expect', 4, 'tolerance', 'Can explain the tolerance zone and what shapes expectations',
      mc('What lies between desired and adequate service?', 'the tolerance zone', ['the service gap', 'the Kano curve', 'the change barrier']),
      mc('A friend says: “best pizza in town.” What shapes your expectation?', 'informal communication', ['formal communication', 'situational factors', 'past experience']),
      zuord('What shapes the expectation?', ['informal communication', 'formal communication', 'situational factors'],
            [['a friend recommends the restaurant', 0], ['the app promises delivery in 20 minutes', 1], ['it is raining, you accept a delay', 2]])),
    F('produktion', 'op-capacity', 2, 'utilization', 'Can explain the trade-offs of higher utilization',
      mc('Utilization rises close to 100 %. What happens to waiting times?', 'they rise sharply', ['they fall', 'they stay the same', 'they rise slightly and linearly']),
      liste('Name two trade-offs of a higher utilization.', [['waiting time', 'lead time', 'queue'], ['flexibility', 'buffer'], ['quality', 'maintenance', 'breakdown']], n=2)),
], karten=[
    karte('ds-platform', 'Base value', 'What the good is worth on its own, even with only one user (e.g. a game console you can play alone).'),
    karte('ds-platform', 'Network value', 'What other users and partners add (online friends, more games, more drivers).'),
    karte('ds-platform', 'Direct network effect', 'More users of the same good make it more valuable (telephone, WhatsApp).'),
    karte('ds-platform', 'Indirect network effect', 'More users attract more complementary products (apps on Android, Office on Windows).'),
    karte('ds-platform', 'Two-sided network effect', 'Supply and demand side attract each other (Uber: riders ↔ drivers; consoles: players ↔ game makers).'),
    karte('sv-expect', 'Tolerance zone', 'Range between desired service (maximal expectation) and adequate service (minimal expectation).'),
    karte('sv-expect', 'Informal communication (expectations)', 'What friends, reviews and word of mouth say about a service; it strongly shapes expectations.'),
    karte('op-capacity', 'Trade-off of high utilization', 'Close to 100 % utilization, waiting and lead times rise sharply; less buffer and flexibility.'),
])


def num(p, gen, w, tipp, lvl=2): return dict(y='num', p=p, gen=gen, u='', w=w, kopf=False, tipp=tipp, klausur=True, lvl=lvl)


MATHE = dict(fams=[
    F('mathe', 'm4-regeln', 4, 'regeln', 'Kann mit Produkt- und Kettenregel ableiten',
      num('Gegeben ist f(x) = ({A}x + {B}) · e^x. Bilden Sie f′(x) mit der Produktregel und berechnen Sie f′(0).', {'v': {'A': [1, 5, 1], 'B': [1, 6, 1]}, 'a': 'A+B', 'r': 0},
          'f′(x) = {A} · e^x + ({A}x + {B}) · e^x → f′(0) = {A} + {B} = {=A+B}.', 'Produktregel: (u · v)′ = u′ · v + u · v′'),
      num('Gegeben ist f(x) = ({A}x² + {B})^{N}. Bilden Sie f′(x) mit der Kettenregel und berechnen Sie f′(1).', {'v': {'A': [1, 3, 1], 'B': [1, 2, 1], 'N': [2, 3, 1]}, 'a': 'N*(A+B)^(N-1)*2*A', 'r': 0},
          'f′(x) = {N}({A}x² + {B})^{=N-1} · {=2*A}x → f′(1) = {=N*(A+B)^(N-1)*2*A}.', 'Kettenregel: äußere Ableitung mal innere Ableitung'),
      num('Gegeben ist f(x) = x^{N} · ln(x). Bilden Sie f′(x) und berechnen Sie f′(1).', {'v': {'N': [2, 5, 1]}, 'a': '1', 'r': 0},
          'f′(x) = {N}x^{=N-1} · ln(x) + x^{N} · 1/x → f′(1) = 0 + 1 = 1.', 'Produktregel; ln(1) = 0'),
      mc('Welche Regel braucht man für f(x) = e^{3x²}?', 'Kettenregel', ['Produktregel', 'Quotientenregel', 'Faktorregel'])),
], karten=[
    karte('m3-monotonie', 'Monotonie: zwei Methoden', '1. Definition: für alle x₂ > x₁ prüfen, ob f(x₂) > f(x₁). 2. Ableitung: f′(x) > 0 im Intervall ⇒ streng monoton wachsend (f′ < 0 ⇒ fallend).'),
    karte('m5-rang', 'Determinante = 0', 'Die Matrix hat keinen vollen Rang, ist nicht invertierbar; das LGS ist nicht eindeutig lösbar.'),
])


MARKETING = dict(fams=[
    F('marketing', 'gratifikation', 1, 'prinzip', 'Kann das Gratifikationsprinzip benennen',
      dict(y='kurz', p='Wie heißt das Prinzip: Ein Austausch findet nur statt, wenn er für alle Parteien vorteilhaft ist?', ok=['Gratifikationsprinzip', 'Gratifikation'], w='', klausur=True, lvl=2),
      mc('Bäcker und Kunde tauschen Brötchen gegen 2 €. Warum kommt der Tausch zustande?', 'Beide sehen einen Vorteil', ['Der Kunde muss essen', 'Der Preis ist gesetzlich fest', 'Der Bäcker hat Überschuss'])),
    F('marketing', 'kundenbindung', 3, 'kano', 'Kann Basis-, Leistungs- und Begeisterungsfaktoren am Beispiel erklären',
      zuord('Glühweinstand: Welcher Faktor im Kano-Modell?', ['Basisfaktor', 'Leistungsfaktor', 'Begeisterungsfaktor'],
            [['heißer Glühwein', 0], ['saubere Tassen', 0], ['kurze Wartezeit', 1], ['fairer Preis', 1], ['Gratis-Lebkuchen', 2], ['Feuerschale zum Aufwärmen', 2]]),
      mc('Ein Faktor fehlt und die Kunden sind stark unzufrieden; ist er da, lobt ihn niemand. Welcher Faktor?', 'Basisfaktor', ['Leistungsfaktor', 'Begeisterungsfaktor', 'Hygienefaktor']),
      mc('Früher begeisterte Kartenzahlung, heute wird sie erwartet. Was ist passiert?', 'Begeisterung wurde zum Basisfaktor', ['Basis wurde zur Begeisterung', 'Leistung wurde zur Begeisterung', 'Nichts, sie blieb gleich']),
      liste('Nennen Sie die drei Faktoren des Kano-Modells.', [['Basisfaktoren', 'Basis'], ['Leistungsfaktoren', 'Leistung'], ['Begeisterungsfaktoren', 'Begeisterung']])),
    F('marketing', 'kundenbindung', 3, 'cd', 'Kann das C/D-Paradigma erklären',
      zuord('C/D-Paradigma: Was folgt aus dem Vergleich?', ['Zufriedenheit', 'Begeisterung', 'Unzufriedenheit'], [['Ist = Soll', 0], ['Ist > Soll', 1], ['Ist < Soll', 2]]),
      mc('Womit vergleicht der Kunde im C/D-Paradigma die wahrgenommene Leistung?', 'mit seiner Erwartung', ['mit dem Preis', 'mit der Konkurrenz', 'mit der Werbung']),
      luecke('Zufriedenheit entsteht aus dem Vergleich von Erwartung (<b>[[0]]</b>) und wahrgenommener Leistung (<b>[[1]]</b>).', [['Soll', 'soll'], ['Ist', 'ist']])),
    F('marketing', 'kundenbindung', 3, 'determinanten', 'Kann die Determinanten der Kundenbindung am Beispiel zuordnen',
      zuord('Welche Determinante der Kundenbindung?', ['ökonomisch', 'technologisch', 'juristisch', 'situativ', 'sozial', 'psychologisch'],
            [['Bonuspunkte, Bahncard', 0], ['Kapselmaschine, Druckerpatronen', 1], ['Handyvertrag mit 24 Monaten', 2], ['Bäckerei liegt auf dem Arbeitsweg', 3], ['alle Freunde nutzen denselben Messenger', 4], ['Friseur, dem man seit Jahren vertraut', 5]]),
      zuord('Gebundenheit oder Verbundenheit?', ['Gebundenheit (nicht wechseln können)', 'Verbundenheit (nicht wechseln wollen)'],
            [['Vertrag mit Laufzeit', 0], ['hohe Wechselkosten', 0], ['Vertrauen in die Marke', 1], ['persönliche Beziehung', 1]]),
      mc('Glühweinstand: Welche Determinante spielt kaum eine Rolle?', 'Gebundenheit, z. B. juristisch', ['psychologisch: Zufriedenheit', 'situativ: Lage am Eingang', 'sozial: Freunde trinken dort']),
      liste('Nennen Sie sechs Determinanten der Kundenbindung.', [['ökonomisch'], ['psychologisch'], ['technologisch'], ['juristisch', 'vertraglich'], ['situativ'], ['sozial']])),
    F('marketing', 'markt', 4, 'akteure', 'Kann Marktakteure am Beispiel einordnen',
      zuord('Glühweinstand: Welche Rolle im Markt?', ['Nachfrager', 'Service-Anbieter', 'Beeinflusser'],
            [['Besucher des Weihnachtsmarkts', 0], ['Kartenzahlungsdienst', 1], ['Getränkelieferant', 1], ['Lokalzeitung', 2], ['Food-Blogger', 2]]),
      liste('Definieren Sie Service-Anbieter und Beeinflusser und nennen Sie je ein Beispiel für den Glühweinstand.',
            [['unterstützt den Austausch', 'Absatzhelfer', 'Service-Anbieter'], ['Kartenzahlung', 'Lieferant', 'Standvermieter'], ['wirkt auf die Entscheidung', 'Beeinflusser'], ['Zeitung', 'Blogger', 'Ordnungsamt']], n=4)),
    F('marketing', 'umwelt', 3, 'umsysteme', 'Kann Einflüsse den Umsystemen zuordnen',
      zuord('E-Bike-Hersteller: Wohin gehört der Einfluss?', ['Umsystem I (Aufgabenumwelt)', 'Umsystem II (Makro-Umwelt)'],
            [['Händler verlangen höhere Margen', 0], ['Akku-Lieferant liefert verspätet', 0], ['Billiganbieter im Discounter', 0], ['steigende Zinsen', 1], ['neue Akkutechnik', 1], ['neues Gesetz zu Radwegen', 1]]),
      liste('Nennen Sie die vier Bereiche der Makro-Umwelt mit je einem Beispiel.', [['ökonomisch', 'Konjunktur', 'Zinsen'], ['technologisch', 'Digitalisierung'], ['ökologisch', 'Klima'], ['politisch', 'rechtlich', 'Gesetze']])),
], karten=[
    karte('kundenbindung', 'Kano: Basisfaktoren', 'Werden vorausgesetzt: fehlen sie, entsteht starke Unzufriedenheit; sind sie da, gibt es kein Lob (Glühwein heiß, Tassen sauber).'),
    karte('kundenbindung', 'Kano: Leistungsfaktoren', 'Je besser erfüllt, desto zufriedener, linear (kurze Wartezeit, fairer Preis, Geschmack).'),
    karte('kundenbindung', 'Kano: Begeisterungsfaktoren', 'Werden nicht erwartet: fehlen sie, stört es nicht; sind sie da, begeistern sie (Gratis-Lebkuchen, Feuerschale).'),
    karte('kundenbindung', 'C/D-Paradigma', 'Zufriedenheit als Vergleich von Erwartung (Soll) und wahrgenommener Leistung (Ist): Ist = Soll Zufriedenheit, Ist > Soll Begeisterung, Ist < Soll Unzufriedenheit.'),
    karte('kundenbindung', 'Kundenbindung: Determinanten', 'ökonomisch, psychologisch, technologisch, juristisch, situativ, sozial.'),
    karte('kundenbindung', 'Gebundenheit vs. Verbundenheit', 'Gebundenheit: Kunde muss bleiben (Vertrag, Wechselkosten, Technik). Verbundenheit: Kunde will bleiben (Zufriedenheit, Vertrauen); langfristig stabiler.'),
    karte('markt', 'Service-Anbieter', 'Unterstützt den Austausch, ohne selbst zu kaufen oder zu verkaufen (Absatzhelfer): Kartenzahlungsdienst, Lieferant, Standvermieter.'),
    karte('markt', 'Beeinflusser', 'Wirkt auf die Entscheidungen der anderen, ohne selbst Partei zu sein: Lokalzeitung, Food-Blogger, Ordnungsamt.'),
])

ABWL = dict(fams=[
    F('abwl', 'guv', 3, 'gkv', 'Kann Gesamt- und Umsatzkostenverfahren unterscheiden',
      zuord('GKV oder UKV?', ['Gesamtkostenverfahren', 'Umsatzkostenverfahren'],
            [['Basis: produzierte Menge', 0], ['Bestandserhöhung als Ertrag', 0], ['Aufwand nach Arten', 0], ['Basis: abgesetzte Menge', 1], ['Lagerware taucht nicht auf', 1], ['Aufwand nach Funktionen', 1]]),
      mc('Welches Verfahren weist Bestandserhöhungen als Ertrag aus?', 'Gesamtkostenverfahren', ['Umsatzkostenverfahren', 'beide', 'keines']),
      dict(y='mc_multi', p='Richtig oder falsch? (alles oder nichts)', o=[['GKV und UKV führen zum selben Jahresergebnis.', True], ['Beim UKV wird der Aufwand nach Arten gegliedert.', False],
           ['Beim GKV ist die produzierte Menge die Basis.', True], ['Beim UKV werden Lagerbestände als Ertrag gezählt.', False]], w='', klausur=True, lvl=2)),
    F('abwl', 'polent', 5, 'zielbez', 'Kann Zielbeziehungen zuordnen',
      zuord('Welche Zielbeziehung?', ['komplementär', 'konkurrierend', 'indifferent'],
            [['Kosten senken ↔ Gewinn steigern', 0], ['Gewinn ↔ Marktanteil (oft)', 0], ['Rentabilität ↔ Liquidität', 1], ['Mehr Lager ↔ weniger Kapitalbindung', 1], ['Logo ändern ↔ Zinssatz', 2]]),
      mc('Rentabilität und Liquidität sind meist …', 'konkurrierend', ['komplementär', 'indifferent', 'identisch'])),
    F('abwl', 'wacc', 3, 'taxshield', 'Kann den Tax-Shield erklären',
      mc('Warum sind Fremdkapitalkosten nach Steuern niedriger?', 'Zinsen mindern den steuerpflichtigen Gewinn', ['Banken zahlen die Steuer', 'Fremdkapital ist steuerfrei', 'Eigenkapital wird höher besteuert']),
      luecke('Fremdkapitalkosten nach Steuern: r<sub>FK</sub> = i<sub>FK</sub> · (1 − <b>[[0]]</b>)', [['s', 'Steuersatz']])),
    F('abwl', 'stakeholder', 3, 'gruppen', 'Kann Stakeholder mit Beitrag und Anspruch nennen',
      liste('Nennen Sie 5 Stakeholder-Gruppen.', [['Eigenkapitalgeber', 'EK-Geber', 'Eigentümer', 'Aktionäre'], ['Fremdkapitalgeber', 'FK-Geber', 'Banken'], ['Arbeitnehmer', 'Mitarbeiter'],
            ['Kunden'], ['Lieferanten'], ['Staat', 'Öffentlichkeit', 'Gesellschaft']], n=5),
      zuord('Was erwartet die Gruppe?', ['EK-Geber', 'FK-Geber', 'Arbeitnehmer', 'Kunden'], [['Gewinn, Wertsteigerung', 0], ['Zinsen, Tilgung', 1], ['Lohn, sicherer Arbeitsplatz', 2], ['gute Leistung zum fairen Preis', 3]])),
    F('abwl', 'bwlvwl', 1, 'bedarf', 'Kann Fremd- und Eigenbedarfsdeckung unterscheiden',
      luecke('Betriebe betreiben <b>[[0]]</b>deckung, Haushalte <b>[[1]]</b>deckung.', [['Fremdbedarfs', 'Fremdbedarf'], ['Eigenbedarfs', 'Eigenbedarf']]),
      dict(y='kurz', p='Wie nennt man es, wenn Betriebe Güter und Leistungen für Dritte erstellen?', ok=['Fremdbedarfsdeckung', 'Fremdbedarf'], w='', klausur=True, lvl=2)),
], karten=[
    karte('guv', 'Gesamtkostenverfahren (GKV)', 'Basis produzierte Menge; Bestandserhöhung als Ertrag; Aufwand nach Arten (Material, Personal, Abschreibungen).'),
    karte('guv', 'Umsatzkostenverfahren (UKV)', 'Basis abgesetzte Menge; Lagerware taucht nicht auf; Aufwand nach Funktionen (Herstellung, Vertrieb, Verwaltung).'),
    karte('wacc', 'Tax-Shield', 'Zinsen mindern den steuerpflichtigen Gewinn: r_FK = i_FK · (1 − s). Fremdkapital wird dadurch billiger; die EK-Kosten steigen mit dem Verschuldungsgrad (höheres Risiko).'),
    karte('bwlvwl', 'Fremdbedarfsdeckung', 'Betriebe erstellen Güter und Leistungen für Dritte; Haushalte decken ihren Eigenbedarf (Konsum).'),
])

ALLE = {'logistik': LOGISTIK, 'produktion': PRODUKTION, 'mathe': MATHE, 'marketing': MARKETING, 'abwl': ABWL}


def main():
    for fid, d in ALLE.items():
        p = IN / fid / 'fragen_neu.json'; neu = json.loads(p.read_text(encoding='utf-8'))
        neu['familien'] = [x for x in neu['familien'] if ':kp-' not in x.get('id', '')] + d['fams']
        p.write_text(json.dumps(neu, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        pk = IN / fid / 'karten.json'; kd = json.loads(pk.read_text(encoding='utf-8'))
        kd['karten'] = [x for x in kd['karten'] if x.get('q') != 'kp']
        da = {txt(x['v']) for x in kd['karten']}
        for x in d['karten']:
            if txt(x['v']) not in da: kd['karten'].append(x); da.add(txt(x['v']))
        pk.write_text(json.dumps(kd, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(fid, len(d['fams']), 'Familien', sum(len(f['a']) for f in d['fams']), 'Fragen')


if __name__ == '__main__':
    main()
