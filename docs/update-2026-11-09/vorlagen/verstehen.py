"""Von Hand geschriebene Verständnisfragen (und einzelne Klausurformen) je Fach, damit jedes Unterthema die Zielgrößen erreicht.
Familien „:vs-…“ → inhalte/<fach>/fragen_neu.json. Wiederholbar. Aufruf: python3 werkzeuge/verstehen.py"""
import json, pathlib
IN = pathlib.Path(__file__).resolve().parents[1] / 'inhalte'


def mc(p, r, f, w='', lvl=2): return dict(y='mc', p=p, o=[[r, True]] + [[x, False] for x in f], w=w, lvl=lvl)
def zu(p, k, e, lvl=1): return dict(y='zuord', p=p, k=k, e=e, w='', lvl=lvl)
def lu(p, l, w='', lvl=2): return dict(y='luecke', p=p, l=l, w=w, lvl=lvl)
def re_(p, o, w='', lvl=2): return dict(y='reihe', p=p, o=o, w=w, lvl=lvl)
def ku(p, ok, w='', lvl=2): return dict(y='kurz', p=p, ok=ok, w=w, lvl=lvl)
def li(p, pk, n=None, lvl=3): return dict(y='liste', p=p, pk=pk, n=n or len(pk), w='', klausur=True, lvl=lvl)
def rv(p, l, pk, lvl=3): return dict(y='rev', p=p, l=l, pk=pk, w='', klausur=True, lvl=lvl)


LOGISTIK = {
 'logistik': [
   li('Nennen Sie die Teilbereiche der Logistik entlang des Materialflusses.', [['Beschaffungslogistik', 'Beschaffung'], ['Produktionslogistik', 'Produktion'], ['Distributionslogistik', 'Distribution'], ['Entsorgungslogistik', 'Entsorgung']]),
   rv('Erklären Sie, wie die Logistik Raum und Zeit überbrückt, mit je einem Beispiel.', 'Raum: Die Ware ist woanders, als sie gebraucht wird → Transport (Rohre aus Asien ins Werk). Zeit: Die Ware ist früher da, als sie gebraucht wird → Lager (Lieferung alle sechs Wochen, Verbrauch täglich).', ['Raum', 'Transport', 'Zeit', 'Lager'])],
 'bereiche': [
   li('Nennen Sie die Bereiche der Unternehmenslogistik in der Reihenfolge des Materialflusses.', [['Einkauf', 'Beschaffung'], ['Lager'], ['Produktion'], ['Distribution'], ['Versand'], ['After-Sales', 'Service']]),
   rv('Nennen und erklären Sie Makro-, Mikro- und Metalogistik mit je einem Beispiel.', 'Makrologistik: gesamtwirtschaftlich, z. B. Güterverkehr eines Landes. Mikrologistik: eine einzelne Organisation, z. B. Unternehmen, Krankenhaus. Metalogistik: mehrere Organisationen arbeiten logistisch zusammen, z. B. City-Logistik mit gemeinsamem Spediteur.', ['Makrologistik', 'Mikrologistik', 'Metalogistik'])],
 'mittelwert#abw': [
   mc('Im Juli gab es einen Großauftrag. Warum verzerrt er den gewogenen gleitenden Mittelwert für August besonders stark?', 'Der jüngste Monat hat das größte Gewicht', ['Alle Monate zählen gleich', 'Der Juli fällt heraus', 'Große Werte werden halbiert']),
   mc('Der Bedarf steigt seit Monaten gleichmäßig. Was passiert mit dem gleitenden Mittelwert?', 'Er liegt immer etwas zu niedrig', ['Er liegt genau richtig', 'Er liegt zu hoch', 'Er schwankt stark']),
   zu('Ursache der Abweichung oder Maßnahme dagegen?', ['Ursache', 'Maßnahme'], [['Saisonschwankung', 0], ['Sonderaktion mit Rabatt', 0], ['Streik beim Lieferanten', 0], ['Ausreißer bereinigen', 1], ['mehr Perioden einbeziehen', 1], ['Außendienst nach Aufträgen fragen', 1]], lvl=2),
   mc('Warum hilft es, Informationen von Vertrieb und Außendienst einzuholen?', 'Sie kennen künftige Aufträge, die die Vergangenheit nicht zeigt', ['Sie rechnen genauer', 'Sie dürfen die Gewichte festlegen', 'Sie ersetzen die Prognose ganz']),
   mc('Wann ist ein gewogener gleitender Mittelwert besser als der einfache?', 'Wenn jüngere Werte aussagekräftiger sind', ['Wenn der Bedarf völlig konstant ist', 'Wenn es nur zwei Werte gibt', 'Wenn alle Werte gleich wichtig sind']),
   lu('Ein Wert, der wegen eines Einmaleffekts stark abweicht, heißt <b>[[0]]</b>; man bereinigt ihn vor der Prognose.', [['Ausreißer', 'ausreißer']])],
 'material': [li('Nennen Sie sechs Betriebs- und Werkstoffe mit je einem Beispiel.', [['Rohstoffe', 'Rohstoff'], ['Hilfsstoffe', 'Hilfsstoff'], ['Betriebsstoffe', 'Betriebsstoff'], ['Halbzeuge', 'Halbzeug'], ['Zulieferteile', 'Zulieferteil'], ['unfertige Erzeugnisse', 'unfertig'], ['Fertigerzeugnisse', 'Fertigerzeugnis'], ['Handelswaren', 'Handelsware']], n=6)],
 'prodlog': [li('Nennen Sie zwei Maschinen der Produktion 4.0 und den Unterschied zwischen ihnen.', [['NC', 'numerical control'], ['CNC', 'computerized'], ['DNC', 'direct', 'distributed']], n=2)],
 'pruefung': [li('Nennen Sie drei zerstörungsfreie Prüfverfahren.', [['Eindringverfahren', 'Farbe', 'Farbeindring'], ['Röntgen', 'Röntgenprüfung'], ['Ultraschall', 'Ultraschallprüfung']])],
 'bestellverfahren': [
   mc('Der Verbrauch schwankt stark. Welches Verfahren reagiert besser?', 'Bestellpunktverfahren', ['Bestellrhythmusverfahren', 'beide gleich', 'keines von beiden']),
   mc('Warum lassen sich beim Bestellrhythmusverfahren Bestellungen gut bündeln?', 'Bestellt wird zu festen Terminen', ['Die Menge ist immer gleich', 'Es gibt keinen Sicherheitsbestand', 'Der Lieferant bestimmt den Termin']),
   zu('Welches Verfahren?', ['Bestellrhythmus', 'Bestellpunkt'], [['feste Zeitabstände', 0], ['Kontrolle nur zum Bestelltermin', 0], ['feste Bestellgrenze', 1], ['ständige Bestandskontrolle', 1]])],
 'glaettung': [
   mc('Man will, dass die Prognose schnell auf Änderungen reagiert. Welches α wählt man?', 'ein großes α, z. B. 0,7', ['ein kleines α, z. B. 0,1', 'α = 0', 'α ist egal']),
   mc('Was passiert bei α = 0?', 'Die Prognose bleibt immer die alte', ['Die Prognose ist der Ist-Wert', 'Die Prognose halbiert sich', 'Die Formel geht nicht']),
   lu('Bei der exponentiellen Glättung wird die alte Prognose um einen Teil der <b>[[0]]</b> zwischen Ist und Prognose korrigiert.', [['Abweichung', 'Differenz', 'abweichung']])],
 'engpass': [
   mc('Teil A spart 10 € je Stück und braucht 5 Minuten, Teil B spart 6 € und braucht 2 Minuten. Welches Teil fertigt man zuerst selbst?', 'B, es spart 3 € je Minute', ['A, es spart mehr je Stück', 'beide gleich', 'keines']),
   mc('Ein Teil kostet im Einkauf weniger als die variablen Kosten der Eigenfertigung. Was tut man?', 'Zukaufen, egal ob Engpass', ['Selbst fertigen', 'Erst die Engpasszeit prüfen', 'Lagerbestand erhöhen'])],
 'dynlos': [
   mc('Warum passt die Andler-Formel bei schwankendem Bedarf nicht?', 'Sie setzt konstanten Bedarf voraus', ['Sie kennt keine Bestellkosten', 'Sie rechnet nur in Stück', 'Sie gilt nur für A-Teile']),
   mc('Kostenausgleich: Wann hört man auf, Perioden zusammenzufassen?', 'Wenn Lagerkosten ≈ Bestellkosten', ['Nach genau drei Perioden', 'Wenn der Bedarf sinkt', 'Wenn das Lager voll ist'])],
 'preise': [mc('Der Materialanteil am Preis ist 40 %, Material wird 10 % teurer. Um wie viel darf der Preis steigen?', 'um 4 %', ['um 10 %', 'um 40 %', 'um 14 %'])],
 'milkrun': [mc('Ein Lieferant liefert jede Woche eine volle Lkw-Ladung. Passt ein Milk Run?', 'Nein, Komplettladungen fahren direkt', ['Ja, immer', 'Ja, wenn er nah ist', 'Nur bei Leergut'])],
 'standort': [mc('Ein Werk in Fernost hat niedrige Löhne. Warum steigen trotzdem oft die Kosten?', 'Längere Wege brauchen mehr Sicherheitsbestand', ['Löhne steigen sofort', 'Steuern sind dort höher', 'Maschinen sind teurer'])],
 'qkz': [mc('Ein Lieferant hat eine QKZ von 92. Wie ist er eingestuft?', 'B: akzeptabel', ['A: gut', 'C: nicht akzeptabel', 'Das hängt von der Menge ab'])],
 'einkauf40': [
   mc('Was zeigt der Unterschied „65 % halten sich für digital, 16 % sind es“?', 'Viele überschätzen ihren Stand', ['Die Studie ist fehlerhaft', 'Fast alle sind digital', 'Digitalisierung ist unwichtig']),
   mc('Warum bremst schlechtes Lieferanten-Onboarding die Digitalisierung?', 'Ohne Lieferanten auf der Plattform bleibt man beim Papier', ['Lieferanten zahlen dann mehr', 'Die IT wird teurer', 'Man darf nicht mehr bestellen'])],
 'm-industrie40': [
   zu('Horizontale oder vertikale Vernetzung?', ['horizontal', 'vertikal'], [['Kunde sieht den Fertigungsstand seiner Bestellung', 0], ['Lieferant bekommt Lagerdaten in Echtzeit', 0], ['Maschine meldet Störung an das ERP', 1], ['Sensor am Band steuert die Feinplanung', 1]], lvl=2),
   mc('Was ist das Neue an Produktion 4.0 gegenüber klassischer Automatisierung?', 'Maschinen und Werkstücke tauschen selbst Daten aus', ['Es gibt mehr Roboter', 'Es wird nur noch nachts produziert', 'Menschen werden überflüssig']),
   mc('Welches Ziel verfolgt Produktion 4.0?', 'Individuelle Produkte in kleiner Stückzahl wirtschaftlich fertigen', ['Nur noch Massenfertigung', 'Weniger Qualität für weniger Geld', 'Mehr Lagerbestand'])],
 'm-lagerfunktion': [
   zu('Welche Lagerfunktion?', ['Ausgleich', 'Sicherung', 'Veredelung', 'Spekulation'], [['Anlieferung und Verbrauch laufen zeitlich auseinander', 0], ['Puffer gegen Lieferausfall', 1], ['Wein reift im Lager', 2], ['Kauf vor einer erwarteten Preiserhöhung', 3]]),
   mc('Warum hat ein zentrales Lager meist weniger Bestand als mehrere dezentrale?', 'Schwankungen gleichen sich aus', ['Es ist größer gebaut', 'Es liefert langsamer', 'Es hat weniger Artikel'])],
 'm-lagerplatz': [
   mc('Warum spart die chaotische Lagerung etwa 20 % Platz?', 'Kein Platz bleibt für einen fehlenden Artikel frei', ['Die Regale sind höher', 'Es gibt weniger Artikel', 'Die Gänge sind schmaler']),
   mc('Wo lagert man Gefahrgut?', 'in einer eigenen, festen Zone', ['frei wie alle anderen Artikel', 'ganz vorn bei den Schnellläufern', 'im Wareneingang'])],
 'm-verpackung': [
   zu('Welche Funktion der Verpackung?', ['Schutz', 'Information', 'Lagerung', 'Marketing'], [['Polster verhindert Bruch', 0], ['Barcode auf dem Karton', 1], ['Ware passt auf die Europalette', 2], ['edler Flakon beim Parfüm', 3]]),
   mc('Warum sind Standardmaße bei Verpackungen wichtig?', 'Sie erleichtern Lagerung, Transport und Umschlag', ['Sie sind gesetzlich Pflicht', 'Sie sehen besser aus', 'Sie sind immer billiger']),
   mc('Bei welchem Produkt ist der Verpackungsanteil am Warenwert typisch hoch?', 'Parfüm', ['Stahlträger', 'Getreide als Schüttgut', 'Rohöl']),
   ku('Nennen Sie eine Maßnahme, um Verpackungskosten zu senken.', ['reduzieren', 'Mehrweg', 'umweltgerecht', 'verkaufen'])],
 'm-lieferservice': [
   mc('Was ist Kunden oft wichtiger: kurze Lieferzeit oder Termintreue?', 'Termintreue', ['kurze Lieferzeit', 'beides unwichtig', 'nur der Preis']),
   zu('Welches Element des Lieferservice?', ['Lieferzeit', 'Lieferzuverlässigkeit', 'Lieferbeschaffenheit'], [['3 Tage ab Bestellung', 0], ['zugesagter Termin wird gehalten', 1], ['Ware kommt unbeschädigt und vollständig', 2]]),
   mc('Was bedeutet „kostenoptimaler Lieferservice“?', 'So viel Service, wie der Kunde erwartet und bezahlt', ['Immer alles sofort lieferbar', 'Möglichst wenig Service', 'Lieferung nur ab Lager'])],
 'm-productsupport': [
   zu('Pre-Sales oder After-Sales?', ['Pre-Sales', 'After-Sales'], [['Bedarfsermittlung beim Kunden', 0], ['Investitionsrechnung', 0], ['Inbetriebnahme', 1], ['Wartung und Störungsbehebung', 1], ['Schulung der Bediener', 1]]),
   mc('Warum lohnt sich After-Sales trotz nur 5–15 % Umsatzanteil?', 'Es bringt einen großen Teil des Gewinns', ['Es ist gesetzlich vorgeschrieben', 'Es senkt die Lagerkosten', 'Es ersetzt den Vertrieb']),
   mc('Was ist das Ziel des Product Support?', 'Kundenbindung über den ganzen Lebenszyklus', ['Neukunden gewinnen', 'Lager leeren', 'Preise senken']),
   lu('Leistungen vor dem Kauf heißen <b>[[0]]</b>, Leistungen danach <b>[[1]]</b>.', [['Pre-Sales', 'pre-sales', 'Pre Sales'], ['After-Sales', 'after-sales', 'After Sales']])],
 'm-et-praxis': [
   mc('Ein Flugzeug steht wegen eines fehlenden Teils am Boden. Welche Bestellung?', 'AOG-Eilbestellung', ['Stock-Order', 'Sammelbestellung', 'Rahmenabruf']),
   mc('Warum lagert man seltene Ersatzteile zentral?', 'Wenig Bestand, im Notfall per Luftfracht schnell da', ['Sie gehen leichter kaputt', 'Kunden holen sie selbst', 'Sie sind billiger']),
   re_('Bestellschluss rückwärts: Bringe die Schritte vor der Abfahrt in die Reihenfolge, in der sie ablaufen.', ['Kommissionieren', 'Verpacken', 'Laden', 'Papiere erstellen'])],
 'm-transport': [
   mc('Warum erhöht Just-in-Time den Transportbedarf?', 'Kleine Lose werden häufiger geliefert', ['Die Ware wird schwerer', 'Es gibt weniger Lieferanten', 'Lager werden größer']),
   mc('Was bedeutet Kabotage?', 'Ausländische Lkw fahren Inlandstransporte', ['Transport ohne Papiere', 'Gefahrguttransport', 'Transport per Schiff'])],
 'm-strasse-schiene': [
   mc('Welcher Verkehrsträger hat in Deutschland den größten Anteil am Güterverkehr?', 'Straße, etwa 70 %', ['Schiene', 'Binnenschiff', 'Luftfracht']),
   zu('Straße oder Schiene?', ['Straße', 'Schiene'], [['Haus-zu-Haus ohne Umschlag', 0], ['JIT-tauglich', 0], ['kein Wochenendfahrverbot', 1], ['große Mengen Massengut', 1]]),
   mc('Warum ist die Schiene weniger flexibel?', 'Dünneres Netz, Umschlag nötig', ['Züge sind langsamer als Lkw', 'Sie fährt nur nachts', 'Sie darf kein Stückgut']),
   mc('Ein Kunde will Ersatzteile über Nacht direkt ans Band. Welcher Verkehrsträger?', 'Straße', ['Schiene', 'Binnenschiff', 'Pipeline'])],
 'm-wasser-luft': [
   zu('Welcher Verkehrsträger?', ['Seeschiff', 'Binnenschiff', 'Luftfracht'], [['80 % des EU-Außenhandels', 0], ['Massengut auf dem Rhein', 1], ['1 % der Menge, aber hoher Wert', 2]]),
   mc('Warum hängt die Binnenschifffahrt vom Wetter ab?', 'Bei Niedrigwasser kann weniger geladen werden', ['Schiffe fahren nicht bei Regen', 'Häfen schließen im Winter', 'Wind bremst die Schiffe']),
   mc('Für welche Ware lohnt sich Luftfracht?', 'hochwertige, eilige Güter', ['Kohle', 'Getreide', 'Baustoffe'])],
 'm-transportketten': [zu('Welche Form der Transportkette?', ['Huckepack', 'Ro-Ro', 'Lash'], [['Lkw fährt auf dem Zug mit', 0], ['Sattelzug rollt aufs Schiff', 1], ['beladene Leichter kommen aufs Mutterschiff', 2]])],
 'm-frachtkosten': [
   mc('Die Strecke wird zehnmal so lang. Was passiert mit dem Frachtpreis?', 'Er steigt deutlich weniger als zehnfach', ['Er steigt genau zehnfach', 'Er bleibt gleich', 'Er steigt mehr als zehnfach']),
   mc('Warum steigt der Frachtpreis unterproportional?', 'Fixe Kosten je Sendung verteilen sich auf mehr km', ['Diesel ist auf langen Strecken billiger', 'Lkw fahren schneller', 'Maut sinkt je km']),
   ku('Nennen Sie die Maßeinheit für Transportleistung (Tonnen mal Kilometer).', ['tkm', 'Tonnenkilometer'], lvl=1),
   mc('Container Hamburg–München, schwere Ladung. Was ist meist günstiger?', 'die Bahn', ['der Lkw', 'die Luftfracht', 'beide gleich'])],
}

PUNKT = {'mittelwert#abw': dict(punkt='abweichung')}   # Familie gehört zu diesem wichtigen Punkt (interne Zuordnung)

def tf(o, p='True or false? (exam style, all or nothing)', w='', lvl=2): return dict(y='mc_multi', p=p, o=[[x, b] for x, b in o], w=w, klausur=True, stil=1, lvl=lvl)
def li_en(p, pk, n=None, lvl=3): return dict(y='liste', p=p, pk=pk, n=n or len(pk), w='', klausur=True, stil=1, lvl=lvl)
def rv_en(p, l, pk, lvl=3): return dict(y='rev', p=p, l=l, pk=pk, w='', klausur=True, stil=1, lvl=lvl)


PRODUKTION = {
 # ---------- Klausurstil (Schief: True/False-Blöcke, Name and explain, am Beispiel) ----------
 'op-intro#ks': [
   tf([['Operations strategy is shaped only top down by the business strategy.', False], ['Inbound logistics is a primary activity in Porter’s value chain.', True],
       ['Procurement is a support activity in Porter’s value chain.', True], ['Operations management deals only with manufacturing, not with services.', False]]),
   li_en('Name the four influences on operations strategy.', [['top down', 'corporate', 'business strategy'], ['bottom up', 'experience'], ['market requirements', 'market'], ['operations resources', 'resources']])],
 'op-align#ks': [
   tf([['Strategic alignment means that resources fit market requirements over time.', True], ['Once aligned, a strategy never needs to be adapted again.', False],
       ['Personal values of key implementers are an internal factor (Porter).', True], ['Societal expectations are an internal factor.', False]]),
   li_en('Name two internal and two external factors of the context of strategy formulation (Porter).', [['strengths and weaknesses', 'strengths', 'weaknesses'], ['personal values', 'values'], ['opportunities and threats', 'opportunities', 'threats'], ['societal expectations', 'society']]),
   rv_en('A bicycle maker’s market moves to e-bikes. Explain with this example why alignment must be achieved over time.', 'Markets change (e-bikes, new competitors); resources (battery know-how, suppliers, production lines) must be adapted again and again so that they keep fitting the market requirements.', ['markets change', 'resources', 'adapted'])],
 'op-analysis#ks': [tf([['PESTL stands for Political, Economic, Socio-cultural, Technological, Legal.', True], ['Strong five forces make an industry more attractive.', False],
                        ['Order qualifiers make the customer choose you over competitors.', False], ['Threat of substitutes is one of Porter’s five forces.', True]])],
 'op-fit#ks': [
   tf([['Functional products should be produced in a responsive supply chain.', False], ['Innovative products have unpredictable demand and short life cycles.', True],
       ['An efficient supply chain aims at low cost and high utilisation.', True], ['A mismatch leads to stock-outs and markdowns for innovative products.', True]]),
   rv_en('A fashion company launches a new trend collection. Which supply chain fits (Fisher)? Explain.', 'Fashion is an innovative product: unpredictable demand, short life cycle, high margin → responsive supply chain (speed, buffer capacity, short lead times). An efficient chain would cause stock-outs and markdowns.', ['innovative', 'responsive', 'unpredictable'])],
 'op-expansion#ks': [
   tf([['A lead strategy builds capacity ahead of demand.', True], ['A lag strategy carries a high risk of overcapacity.', False],
       ['Greenfield means expanding an existing site.', False], ['Overtime and extra shifts are tactical capacity expansion.', True]]),
   li_en('Name four types of capacity expansion.', [['greenfield'], ['brownfield'], ['external', 'acquisition', 'outsourcing'], ['process improvement', 'improvement'], ['tactical', 'overtime', 'shifts']], n=4)],
 'op-location#ks': [
   tf([['Location planning starts with number, capacity and location of plants.', True], ['Political stability is a quantitative location criterion.', False],
       ['A scoring model rates, weights and adds up criteria.', True], ['Relocation increases the number of sites.', False]]),
   li_en('Name four location strategies.', [['expansion'], ['relocation'], ['split'], ['contraction']]),
   rv_en('Explain the difference between a scoring model and an optimisation model for location planning.', 'Scoring: each criterion is rated, weighted and the weighted scores are added up (also qualitative criteria). Optimisation: the best location is computed mathematically, e.g. minimum transport cost.', ['scoring', 'weighted', 'optimisation'])],
 'op-process#ks': [li_en('Name the seven levers of process design.', [['eliminate'], ['accelerate'], ['integrate'], ['automate'], ['shift', 'outsource'], ['change sequence', 'postpone'], ['parallelise', 'parallelize']])],
 'op-types#ks': [
   tf([['Job production makes one or a few pieces to customer order.', True], ['Mass production serves an anonymous market with homogeneous products.', True],
       ['High volume and low variety lead to a job shop.', False], ['Mass customization means individual products at near mass-production cost.', True]]),
   li_en('Name the three production types and give an example for each.', [['mass production', 'mass'], ['batch production', 'batch'], ['job production', 'job']]),
   rv_en('Place a car manufacturer, a bakery making several breads and a yacht builder in the product-process matrix. Explain.', 'Car manufacturer: high volume, low variety → assembly line / continuous (mass). Bakery: medium volume, several products → batch. Yacht builder: low volume, high variety → job shop.', ['assembly line', 'batch', 'job'])],
 'op-little#ks': [tf([['Little’s Law: WIP = throughput × cycle time.', True], ['A pull system releases work based on a forecast.', False],
                      ['The bottleneck limits the throughput of the whole line.', True], ['Kanban is a push system.', False]])],
 'op-related#ks': [
   tf([['TCO considers all costs over the life cycle, not just the price.', True], ['Transaction cost theory compares make and buy.', True],
       ['In the principal-agent problem the principal knows more than the agent.', False], ['Humanitarian logistics is a service-part topic.', True]]),
   li_en('Name four sourcing topics in operations.', [['make or buy'], ['outsourcing'], ['principal-agent'], ['transaction cost'], ['break-even'], ['TCO', 'total cost'], ['supplier evaluation']], n=4),
   rv_en('Explain TCO with the example of buying a production machine.', 'Total cost of ownership: not only the price, but all costs over the life cycle – transport, installation, training, energy, maintenance, spare parts, downtime, disposal.', ['life cycle', 'maintenance', 'price'])],
 'op-mrp#ks': [
   tf([['Net requirement = gross requirement − stock − scheduled receipts (+ safety stock).', True], ['A planned order release is shifted later by the lead time.', False],
       ['Lot-for-lot orders exactly the net requirement of each period.', True], ['MRP inputs are master schedule, bill of materials and inventory status.', True]]),
   li_en('Name the three inputs of MRP.', [['master production schedule', 'master'], ['bill of materials', 'BOM'], ['inventory status', 'inventory']])],
 'op-lotsize#ks': [
   tf([['At the EOQ, ordering cost equals holding cost.', True], ['A higher holding cost increases the EOQ.', False],
       ['Safety stock buffers uncertain demand and lead time.', True], ['z = 1.65 corresponds to about a 95 % service level.', True]]),
   rv_en('Explain the trade-off behind the EOQ.', 'Bigger lots → fewer orders → lower ordering cost, but more stock → higher holding cost. The EOQ is the lot size where total cost is minimal; there ordering cost = holding cost.', ['ordering cost', 'holding cost', 'minimal'])],
 'op-tqm#ks': [
   tf([['In TQM quality is built in and everyone is responsible.', True], ['TQM relies mainly on inspection at the end of the line.', False],
       ['Continuous improvement (kaizen) means small improvements every day.', True], ['Benchmarking compares with the worst competitor.', False]]),
   li_en('Name the three core elements of TQM.', [['customer satisfaction', 'customer'], ['employee involvement', 'employee'], ['continuous improvement', 'kaizen']]),
   rv_en('Explain the difference between TQM and classic inspection.', 'Classic: quality is inspected at the end, defects are sorted out. TQM: quality is built into design and processes, every employee is responsible, continuous improvement.', ['inspection', 'built in', 'everyone'])],
 'op-leantools#ks': [
   tf([['Poka-yoke makes errors impossible by design.', True], ['Kanban is a pull system controlled by cards.', True],
       ['The 5S are Sort, Straighten, Shine, Standardise, Sustain.', True], ['JIT increases inventory to secure supply.', False]]),
   li_en('Name the 5S.', [['sort'], ['straighten'], ['shine'], ['standardise', 'standardize'], ['sustain']]),
   li_en('Name the four steps of value stream mapping.', [['scope'], ['status quo', 'current'], ['to-be', 'future'], ['realisation plan', 'plan']])],
 'op-sixsigma#ks': [
   li_en('Name the five phases of DMAIC.', [['define'], ['measure'], ['analyse', 'analyze'], ['improve'], ['control']]),
   rv_en('Explain the difference between Lean and Six Sigma.', 'Lean: eliminate waste (muda) and improve flow. Six Sigma: reduce variation and defects with statistics (DMAIC).', ['waste', 'variation', 'defects'])],
 'op-digital#ks': [
   tf([['Digitalisation of dispositive factors concerns planning and information.', True], ['In system-driven planning the human decides, the system only suggests.', False],
       ['Robots substituting workers is elementary digitalisation.', True], ['MES and ERP are common technologies in operations.', True]]),
   li_en('Name the three levels of system support in planning.', [['elementary', 'manual'], ['system-based', 'suggests'], ['system-driven', 'decides']]),
   rv_en('Explain the difference between digitalising dispositive and elementary factors with an example.', 'Dispositive: planning and information are done by systems (ERP plans orders). Elementary: machines augment or substitute humans (picking robot, 3D printer).', ['dispositive', 'elementary', 'planning'])],
 'op-techselect#ks': [
   tf([['Key technologies have high competitive advantage and high integration.', True], ['Basic technologies give a high competitive advantage.', False],
       ['Pacemaker technologies are tomorrow’s key technologies.', True], ['The technology portfolio leads to invest, select or disinvest.', True]]),
   li_en('Name the four technology types of the technology matrix.', [['key'], ['pacemaker'], ['basic', 'basis'], ['future']]),
   rv_en('A computer manufacturer uses chip design, standard screws, AI-based cooling and quantum research. Place them in the technology matrix and explain.', 'Chip design: key technology (high advantage, high integration). Screws: basic technology (everyone has it). AI cooling: pacemaker (high advantage, still low integration). Quantum research: future technology (low, low).', ['key', 'basic', 'pacemaker', 'future'])],
 'op-oee#ks': [
   tf([['OEE = availability × performance × quality.', True], ['The OEE factors are added up.', False], ['World-class OEE is about 85 %.', True], ['Breakdowns reduce the quality factor.', False]]),
   li_en('Name the six big losses of OEE.', [['breakdowns'], ['setup', 'changeover'], ['minor stops'], ['reduced speed'], ['defects'], ['start-up']])],
 'ds-intro#ks': [
   tf([['Industry 4.0 is based on cyber-physical systems.', True], ['Industry 2.0 brought electronics and IT.', False],
       ['People tend to extrapolate exponential progress linearly.', True], ['A CPS consists only of software.', False]]),
   li_en('Name the four industrial revolutions with their key technology.', [['mechanical', 'steam'], ['mass production', 'electricity'], ['electronics', 'IT'], ['cyber-physical', 'CPS']])],
 'ds-exp#ks': [
   tf([['Doubling every two years gives 32 times after ten years.', True], ['Linear growth multiplies, exponential growth adds.', False],
       ['L = L₀ · 2^(t ÷ T) describes exponential growth.', True], ['After 20 years of doubling every 2 years: 1,024 times.', True]]),
   rv_en('Explain why exponential progress surprises managers, with an example.', 'Intuition extrapolates linearly; exponential growth multiplies. Example: computing power doubling every 2 years → 32× in 10 years instead of the expected 5×; the gap is the surprise factor.', ['linear', 'multiplies', 'doubling']),
   li_en('Name the actors of mobility in 2030.', [['AI providers', 'AI'], ['OEMs', 'OEM'], ['ride hailing'], ['users']])],
 # ---------- Verstehen ----------
 'op-intro': [mc('A hospital organises beds, nurses and operating theatres. Is this operations management?', 'Yes, services are operations too', ['No, only factories', 'Only the pharmacy', 'Only if it makes profit'])],
 'op-tradeoff#to': [
   mc('A retailer ships everything by express. What happens?', 'Lead time falls, transport cost rises', ['Both fall', 'Lead time rises', 'Nothing changes']),
   mc('Which pair is a classic cost/offer trade-off?', 'Transport cost ↔ lead time', ['Quality ↔ brand', 'Price ↔ logo', 'Revenue ↔ sales'])],
 'op-flex#v': [
   mc('Two plants, each makes only one product. Demand for A is low, for B high. Why are sales lost?', 'Idle capacity of A cannot make B', ['Total capacity is too small', 'Prices are too high', 'B has no customers']),
   mc('What does chaining achieve?', 'Most of the benefit of full flexibility at lower cost', ['Full flexibility for free', 'Lower demand', 'More plants']),
   mc('No flexibility: capacities 100 and 100, demand A = 60, B = 140. Sales?', '160', ['200', '140', '100']),
   mc('Full flexibility in the same case. Sales?', '200', ['160', '140', '240'])],
 'op-swing#v': [
   mc('All criteria start at their worst value. Which swing gets 100 points?', 'The most valuable swing to best', ['The cheapest criterion', 'Always price', 'The smallest range']),
   mc('Price ranges only from 40 € to 44 €. What weight will it get?', 'a low weight', ['always 100', 'a high weight', 'zero by rule']),
   mc('Why does SWING look at real ranges instead of abstract importance?', 'A criterion matters only as much as its alternatives differ', ['Ranges are easier to compute', 'Importance is unknown', 'Weights must add to 100']),
   mc('Weight 50 vs. 100 means …', 'The first swing is worth half the second', ['The first criterion is useless', 'Both are equal', 'The second costs twice as much']),
   lu('In SWING weighting, all criteria are first set to their <b>[[0]]</b> value.', [['worst', 'lowest']])],
 'op-decision#mece': [
   mc('Alternatives: “train”, “car”, “public transport”. Are they MECE?', 'No, train and public transport overlap', ['Yes', 'No, a gap only', 'MECE is not relevant']),
   mc('Alternatives: “under 18”, “18 to 65”. Are they MECE?', 'No, there is a gap above 65', ['Yes', 'No, they overlap', 'Only if sorted']),
   mc('What does “collectively exhaustive” mean?', 'No gaps', ['No overlaps', 'Equal weights', 'Sorted alternatives'], lvl=1),
   mc('What does “mutually exclusive” mean?', 'No overlaps', ['No gaps', 'Same scores', 'Only two options'], lvl=1),
   lu('MECE: mutually <b>[[0]]</b> and collectively <b>[[1]]</b>.', [['exclusive'], ['exhaustive']], lvl=1),
   mc('A hospital lists: “surgery”, “day clinic”, “outpatient treatment”. Problem?', 'Day clinic and outpatient overlap', ['There is a gap', 'Nothing', 'Too few options']),
   tf([['Alternatives that overlap violate “mutually exclusive”.', True], ['A gap violates “collectively exhaustive”.', True], ['MECE requires exactly three alternatives.', False], ['MECE alternatives cannot be compared.', False]])],
 'op-decision#calc': [mc('Weights 2 and 3. What is the weighting factor of the first criterion?', '0.4', ['0.2', '0.67', '2'])],
 'op-experience#v': [
   mc('Why does the experience curve use cumulative quantity?', 'Learning builds up over all units ever made', ['Annual output is unknown', 'It is simpler', 'Prices are cumulative']),
   mc('Cost falls 25 % per doubling. From 1,000 to 4,000 units, how many doublings?', '2', ['3', '4', '1'])],
 'op-scurve#v': [
   mc('When should a firm switch to a new technology (S-curve)?', 'When the old curve flattens', ['At the start of the old curve', 'Never', 'When R&D is cheapest']),
   mc('The aggregated adopters form an S-curve. When is it steepest?', 'At the peak of the bell curve', ['At the start', 'At the end', 'It is never steep'])],
 'sv-purchase#v': [
   mc('Why is information search the bottleneck when choosing a tax consultant?', 'Quality is hard to assess before purchase', ['Prices are secret', 'There are no consultants', 'It takes no time']),
   mc('Which quality of a master programme can you check only after you finished it?', 'Experience quality', ['Search quality', 'Price quality', 'Brand quality'])],
 'sv-marketing': [mc('For a complex IT service, why can a relationship contract beat a formal contract?', 'Trust and flexibility matter where details cannot be specified', ['It is cheaper to print', 'It is always shorter', 'Formal contracts are illegal'])],
 'sv-spn#v': [
   mc('Why do solution providers work in networks?', 'No single firm can deliver the whole solution', ['To avoid customers', 'To raise prices', 'Networks are required by law']),
   mc('A scanner maker charges per scan. What is this?', 'Performance-based pricing', ['Cost-plus pricing', 'Dumping', 'Licence fee'])],
 'op-techstrat': [mc('A technology gives a big advantage but is hardly used in products yet. Type?', 'Pacemaker', ['Key', 'Basic', 'Future'])],
 'ds-oss#v': [
   mc('A company introduces free open-source software. Where are most costs?', 'Implementation, operations, support, training', ['Licence fees', 'There are none', 'Hardware only']),
   mc('Why do companies contribute to open source?', 'Collaboration and complementary products', ['To pay fewer taxes', 'To keep code secret', 'Because it is required'])],
 'ds-platform#v': [
   mc('Android: a phone is useful even with no other users. What is that?', 'Base value', ['Network value', 'Two-sided effect', 'Lock-in']),
   mc('Why do platform markets tend to “winner takes it all”?', 'Network effects pull users to the largest platform', ['Platforms are cheaper', 'States forbid competition', 'Users like monopolies']),
   mc('Uber: more drivers lead to shorter waiting times, which attracts riders. Which effect?', 'Two-sided', ['Direct', 'Base value', 'Indirect']),
   tf([['The value of a platform is base value plus network value.', True], ['WhatsApp shows an indirect network effect.', False], ['Apps on Android show an indirect network effect.', True], ['Lock-in makes switching easier.', False]]),
   mc('All your contacts and photos are on one platform. Why is switching hard?', 'Lock-in effect', ['Base value', 'High prices', 'Law'])],
 'sv-purchase#v2': [mc('Customers reduce risk when buying services. How?', 'Recommendations, reviews, guarantees', ['Buying the cheapest', 'Buying in bulk', 'Never buying'])],
 'op-experience#v2': [],
 'op-scurve#v2': [],
 'op-tradeoff#ks': [tf([['Higher product variety raises inventory and set-up cost.', True], ['Faster transport lowers transportation cost.', False],
                        ['Higher utilisation raises waiting time.', True], ['A better offer always lowers costs.', False]]),
                    tf([['The efficient frontier shows the best combinations of cost and offer.', True], ['Points above the efficient frontier are efficient.', False],
                        ['Better processes can move the efficient frontier.', True], ['Higher service levels raise inventory and transport cost.', True]])],
 'op-strategy#ansoff': [mc('Selling existing products to new customer groups abroad. Ansoff strategy?', 'Market development', ['Market penetration', 'Product development', 'Diversification'])],
 'op-mrp#ks2': [rv_en('Explain how the planned order release is derived from the net requirement.', 'Net requirement of a period = planned order receipt (lot-for-lot); the planned order release is the same quantity shifted earlier by the lead time.', ['net requirement', 'receipt', 'lead time'])],
 'op-lotsize#ks2': [li_en('Name the three variables of the EOQ formula.', [['demand', 'D'], ['ordering cost', 'S'], ['holding cost', 'H']])],
 'op-techstrat#ks': [li_en('Name the four strategies of the technology strategy matrix.', [['intensify', 'intensification'], ['product technology innovation', 'product'], ['process technology innovation', 'process'], ['technology innovation', 'both new']])],
 'op-oee#ks2': [rv_en('Explain the three OEE factors with one typical loss each.', 'Availability: run time ÷ planned time (loss: breakdowns, setup). Performance: actual ÷ ideal rate (loss: minor stops, reduced speed). Quality: good ÷ total units (loss: defects, start-up losses).', ['availability', 'performance', 'quality'])],
 'sv-operations#ks': [tf([['Overbooking sells more capacity than exists because of no-shows.', True], ['Yield management sets one fixed price for all customers.', False],
                          ['An SLA defines measurable service levels.', True], ['Services can be stored like goods to match capacity.', False]])],
 'sv-marketing#ks': [li_en('Name the 7 P of the service marketing mix.', [['product'], ['price'], ['place'], ['promotion'], ['people'], ['process'], ['physical evidence', 'evidence']])],
 'sv-smart#ks': [tf([['A SMART service is data based, individually configured and platform based.', True], ['Predictive maintenance repairs a machine only after it failed.', False],
                     ['The installed base is all products already in use at customers.', True], ['SMART services need no data from the customer’s machines.', False]])],
 'ds-platform#v3': [mc('VISA: what is the network value for a cardholder?', 'More shops accept the card', ['Paying without cash', 'A nicer card design', 'Lower interest'])],
 'sv-purchase#v3': [mc('Service purchase process: what comes right after information search?', 'Options assessment', ['Purchase', 'Post-purchase evaluation', 'Problem recognition'])],
 'op-swing#v3': [mc('Price swing 40–500 € gets 100 points, comfort swing gets 50. What does that mean?', 'Comfort’s swing is worth half of price’s', ['Comfort is unimportant', 'Price is cheap', 'Both are equal'])],
}
PUNKT.update({'ds-platform#v3': dict(punkt='platform'), 'sv-purchase#v3': dict(punkt='purchase'), 'op-swing#v3': dict(punkt='swing')})
PUNKT.update({'op-decision#mece': dict(punkt='mece'), 'op-swing#v': dict(punkt='swing'), 'op-flex#v': dict(punkt='flex'), 'ds-platform#v': dict(punkt='platform'),
              'sv-purchase#v': dict(punkt='purchase'), 'sv-purchase#v2': dict(punkt='purchase'), 'op-scurve#v': dict(punkt='scurve'), 'op-experience#v': dict(punkt='experience'),
              'op-decision#calc': dict(punkt='decision'), 'op-tradeoff#ks': dict(punkt='tf-tradeoff'), 'op-tradeoff#to': dict(punkt='tf-tradeoff'),
              'op-strategy#ansoff': dict(punkt='tf-ansoff'), 'sv-marketing': dict(punkt='tf-contracts')})

def nu(p, gen, w, tipp, lvl=2, kl=True): return dict(y='num', p=p, gen=gen, u='', w=w, kopf=False, tipp=tipp, lvl=lvl, **(dict(klausur=True, stil=1) if kl else {}))
def lu_kl(p, l, w='', lvl=2): return dict(y='luecke', p=p, l=l, w=w, klausur=True, stil=1, lvl=lvl)


MATHE = {
 'm1-mengen#mengen': [
   mc('A = {1, 2, 3}, B = {3, 4}. Was ist A \\ B?', '{1, 2}', ['{3}', '{4}', '{1, 2, 3, 4}'], lvl=1),
   mc('Wann lässt sich das Komplement von A bezüglich B bilden?', 'wenn A eine Teilmenge von B ist', ['immer', 'wenn A und B gleich groß sind', 'nie'])],
 'm1-terme': [mc('(a + b)² ist gleich …', 'a² + 2ab + b²', ['a² + b²', '2a + 2b', 'a² · b²'], lvl=1)],
 'm1-summen': [mc('Σ (i = 1 bis 4) 3 ergibt …', '12', ['3', '7', '10'], lvl=1)],
 'm2-zins#auf': [mc('Warum wächst ein Kapital mit Zinseszins schneller als linear?', 'Die Zinsen werden mitverzinst', ['Der Zinssatz steigt', 'Die Bank zahlt Boni', 'Es wächst nur linear'])],
 'm2-kapitalwert#kw': [
   mc('Der Kapitalwert bei 8 % ist −500 €. Was bedeutet das?', 'Die Anlage zu 8 % ist besser', ['Die Investition bringt 500 € Gewinn', 'Der interne Zins ist 8 %', 'Man verliert genau 8 %']),
   mc('Der Kalkulationszins steigt. Was passiert mit dem Kapitalwert?', 'Er sinkt', ['Er steigt', 'Er bleibt gleich', 'Er wird immer negativ'])],
 'm2-izf#izf': [
   mc('Was ist der interne Zinsfuß?', 'der Zins, bei dem der Kapitalwert 0 ist', ['der Bankzins', 'der höchste mögliche Zins', 'der Zins im ersten Jahr'], lvl=1),
   nu('Bei i₁ = {A} % ist C₀ = {B}, bei i₂ = {=A+5} % ist C₀ = −{D}. Bestimmen Sie den internen Zinsfuß mit linearer Interpolation (in %).', {'v': {'A': [6, 14, 1], 'B': [2, 9, 1], 'D': [2, 9, 1]}, 'a': 'A+B*5/(B+D)', 'r': 2},
      'r = i₁ + C₀₁ · (i₂ − i₁) ÷ (C₀₁ − C₀₂) = {A} + {B} · 5 ÷ ({B} + {D}) = {=A+B*5/(B+D)} %', 'r = i₁ + C₀₁ · (i₂ − i₁) ÷ (C₀₁ − C₀₂)')],
 'm3-funktion#ks': [
   nu('f(x) = {A}x² − {B}. Berechnen Sie f({C}).', {'v': {'A': [2, 5, 1], 'B': [1, 9, 1], 'C': [2, 4, 1]}, 'a': 'A*C^2-B', 'r': 0}, 'f({C}) = {A} · {C}² − {B} = {=A*C^2-B}', 'x einsetzen, Potenz zuerst'),
   lu_kl('Eine Funktion ordnet jedem x aus dem Definitionsbereich genau <b>[[0]]</b> y-Wert zu.', [['einen', 'einem', 'ein']]),
   lu_kl('Der Definitionsbereich von f(x) = 1 ÷ (x − 3) ist ℝ ohne <b>[[0]]</b>.', [['3', 'x = 3', '{3}']])],
 'm4-quotient#ks': [
   nu('f(x) = x². Berechnen Sie den Differenzenquotienten zwischen x = 1 und x = {A}.', {'v': {'A': [2, 9, 1]}, 'a': 'A+1', 'r': 0}, '({A}² − 1²) ÷ ({A} − 1) = {=A+1}', '(f(b) − f(a)) ÷ (b − a)'),
   lu_kl('Der Grenzwert des Differenzenquotienten heißt <b>[[0]]</b>.', [['Differentialquotient', 'Ableitung', 'differentialquotient']])],
 'm4-quotient': [
   mc('Was beschreibt der Differenzenquotient geometrisch?', 'die Steigung der Sekante', ['die Steigung der Tangente', 'die Fläche', 'den y-Achsenabschnitt'], lvl=1),
   mc('Was beschreibt der Differentialquotient geometrisch?', 'die Steigung der Tangente', ['die Steigung der Sekante', 'den Nullpunkt', 'die Krümmung'], lvl=1)],
 'm4-extrem': [mc('f′(x₀) = 0 und f″(x₀) < 0. Was liegt bei x₀ vor?', 'ein Maximum', ['ein Minimum', 'ein Wendepunkt', 'eine Nullstelle'])],
 'm4-elastizitaet#el': [
   mc('|ε| > 1 bedeutet …', 'elastisch: Menge reagiert stärker als der Preis', ['unelastisch', 'Preis steigt nicht', 'kein Zusammenhang']),
   mc('ε = −0,5, der Preis steigt um 2 %. Was passiert mit der Menge?', 'sie sinkt um etwa 1 %', ['sie sinkt um 4 %', 'sie steigt um 1 %', 'sie bleibt gleich'])],
 'm4-lagrange#lg': [
   mc('Was bedeutet λ im Lagrange-Ansatz inhaltlich?', 'wie stark sich der Zielwert ändert, wenn die Nebenbedingung um 1 gelockert wird', ['der optimale x-Wert', 'die Steigung von f', 'immer 0']),
   mc('Zwei Variablen, eine Nebenbedingung: Wie viele Gleichungen entstehen beim Ableiten von L?', '3', ['2', '1', '4'])],
 'm5-gauss#gs': [
   mc('Was ist das Ziel des Gauß-Algorithmus?', 'die Stufenform', ['die Determinante', 'die Inverse', 'eine Diagonale aus Nullen'], lvl=1),
   mc('Welche Umformung ist beim Gauß-Algorithmus erlaubt?', 'Vielfaches einer Zeile zu einer anderen addieren', ['Zwei Zahlen in einer Zeile tauschen', 'Eine Zeile quadrieren', 'Eine Spalte löschen']),
   mc('Es entsteht die Zeile 0 0 0 | 5. Was bedeutet das?', 'keine Lösung', ['genau eine Lösung', 'unendlich viele Lösungen', 'x₃ = 5']),
   mc('Rang(A) = Rang(A | b) = Zahl der Variablen. Was folgt?', 'genau eine Lösung', ['keine Lösung', 'unendlich viele Lösungen', 'nichts']),
   nu('Zwei Länder haben zusammen {=X+Y} Titel, das erste hat {=X-Y} Titel mehr als das zweite. Wie viele Titel hat das erste Land?', {'v': {'X': [5, 9, 1], 'Y': [1, 4, 1]}, 'a': 'X', 'r': 0},
      'x₁ + x₂ = {=X+Y}, x₁ − x₂ = {=X-Y} → addieren: 2x₁ = {=2*X} → x₁ = {X}', 'Gleichungen addieren, dann eine Variable fällt weg')],
 'm5-verrechnung#ks': [rv('Erklären Sie, warum man für innerbetriebliche Verrechnungspreise ein Gleichungssystem braucht.', 'Die Hilfsabteilungen beliefern sich gegenseitig; der Preis jeder Abteilung hängt vom Preis der anderen ab. Deshalb müssen alle Preise gleichzeitig bestimmt werden (LGS). Probe: Leistungen an die Hauptabteilung decken alle Primärkosten.', ['gegenseitig', 'gleichzeitig', 'Primärkosten'])],
 'm1-gleichungen#lgs': [mc('Was ist der erste Schritt bei einer Textaufgabe mit mehreren Unbekannten?', 'Variablen festlegen', ['Gauß anwenden', 'Determinante berechnen', 'Ergebnis schätzen'], lvl=1),
                         mc('„Der Erste zahlt ein Drittel vom Dritten.“ Welche Gleichung?', 'x₁ = ⅓ · x₃', ['x₃ = ⅓ · x₁', 'x₁ + x₃ = 3', 'x₁ = 3 · x₃'], lvl=1)],
 'm5-verrechnung': [mc('Werkstatt und Fuhrpark beliefern sich gegenseitig. Was passiert, wenn man das ignoriert?', 'Die Verrechnungspreise sind falsch', ['Nichts', 'Die Primärkosten sinken', 'Das LGS wird einfacher'])],
 'm1-mengen#mengen2': [mc('A = {s, a, m}, B = {a, n, k, e}. Was ist A ∩ B?', '{a}', ['{s, m}', '{n, k, e}', '{ }'], lvl=1)],
}
PUNKT.update({'m1-mengen#mengen': dict(punkt='mengen'), 'm1-mengen#mengen2': dict(punkt='mengen'), 'm2-zins#auf': dict(punkt='aufzinsung'), 'm2-kapitalwert#kw': dict(punkt='kapitalwert'),
              'm2-izf#izf': dict(punkt='izf'), 'm4-lagrange#lg': dict(punkt='lagrange'), 'm5-gauss#gs': dict(punkt='gauss'), 'm1-gleichungen#lgs': dict(punkt='lgs-text')})

BLOCK = 'Kreuzen Sie an: richtig oder falsch? (4er-Block, nur alles richtig gibt Punkte)'
def bl(aus, w=''): return dict(y='block', p=BLOCK, aussagen=[[x, b] for x, b in aus], w=w, klausur=True, stil=1, lvl=3)
def rk(p, l, pk): return dict(y='rev', p=p, l=l, pk=pk, w='', klausur=True, stil=1, lvl=3)


ABWL = {
 'bwlvwl#ks': [bl([['BWL und VWL unterscheiden sich vor allem in der Größe der betrachteten Unternehmen.', False], ['Betriebe betreiben Fremdbedarfsdeckung.', True],
                   ['Die VWL betrachtet die gesamte Volkswirtschaft.', True], ['Ein Datum ist eine Größe, die das Unternehmen frei gestalten kann.', False]])],
 'gliederung#ks': [
   bl([['Die Industriebetriebslehre ist Teil der institutionellen Gliederung.', True], ['Finanzierung ist Teil der funktionalen Gliederung.', True],
       ['Die Kostenrechnung gehört zur Allgemeinen BWL im engeren Sinn.', False], ['Die Spezielle BWL gilt für alle Betriebe gleichermaßen.', False]]),
   bl([['Die Handelsbetriebslehre ist eine institutionelle Spezielle BWL.', True], ['Personal und Organisation sind funktionale Gliederungsbereiche.', True],
       ['Die funktionale Gliederung richtet sich nach dem Wirtschaftszweig.', False], ['Die betriebswirtschaftliche Verfahrenstechnik umfasst das Rechnungswesen.', True]]),
   rk('Erklären Sie die institutionelle und die funktionale Gliederung der BWL mit je einem Beispiel.', 'Institutionell: nach der Art des Betriebs (Wirtschaftszweig), z. B. Industrie-, Handels-, Bankbetriebslehre. Funktional: nach den Aufgaben im Betrieb, z. B. Beschaffung, Produktion, Absatz, Finanzierung.', ['institutionell', 'Wirtschaftszweig', 'funktional', 'Aufgaben'])],
 'maslow#ks': [
   bl([['Selbstverwirklichung ist ein Wachstumsbedürfnis.', True], ['Die Stufen 1 bis 4 sind Defizitbedürfnisse.', True],
       ['Nach Maslow müssen die Stufen zu 100 % erfüllt sein, bevor die nächste wirkt.', False], ['Wertschätzung liegt unter den Sicherheitsbedürfnissen.', False]]),
   bl([['Soziale Bedürfnisse bilden die dritte Stufe.', True], ['Die Reihenfolge der Stufen gilt in allen Kulturen gleich.', False],
       ['Maslow ist empirisch kaum belegt.', True], ['Für Unternehmen zeigt Maslow, dass Lohn allein nicht motiviert.', True]]),
   rk('Nennen Sie die fünf Stufen der Bedürfnispyramide nach Maslow und erklären Sie ihre Bedeutung für Unternehmen.', '1 physiologische Grundbedürfnisse, 2 Sicherheit, 3 soziale Bedürfnisse, 4 Wertschätzung, 5 Selbstverwirklichung. Bedeutung: Mitarbeitermotivation (Lohn reicht nicht allein) und Marketing (Produkte sprechen bestimmte Stufen an).', ['Grundbedürfnisse', 'Sicherheit', 'soziale', 'Wertschätzung', 'Selbstverwirklichung'])],
 'motivation#ks': [
   bl([['Die Gleichheitstheorie nach Adams ist eine Prozesstheorie.', True], ['Maslow ist eine Prozesstheorie.', False],
       ['Nach Adams vergleichen Menschen ihr Verhältnis von Ertrag zu Einsatz mit anderen.', True], ['Extrinsische Motivation entsteht aus der Tätigkeit selbst.', False]]),
   bl([['Gefühlte Ungerechtigkeit erzeugt nach Adams eine Spannung.', True], ['Eine Reaktion auf Ungerechtigkeit kann die Kündigung sein.', True],
       ['Inhaltstheorien erklären, wie Motivation entsteht.', False], ['Lob ist intrinsische Motivation.', False]]),
   rk('Erklären Sie die Gleichheitstheorie nach Adams und nennen Sie zwei Reaktionen auf gefühlte Ungerechtigkeit.', 'Menschen vergleichen das Verhältnis Outcome/Input (Ertrag zu Einsatz) mit dem anderer. Gefühlte Ungerechtigkeit erzeugt Spannung. Reaktionen: Einsatz senken oder erhöhen, mehr Ertrag fordern, Vergleich anders deuten, Vergleichsperson wechseln, kündigen.', ['vergleichen', 'Einsatz', 'Ungerechtigkeit', 'Spannung'])],
 'bedarf#ks': [bl([['Ein Bedarf ist ein Bedürfnis mit Kaufkraft.', True], ['Luft ist ein knappes Gut.', False],
                   ['Dasselbe Auto kann Konsum- oder Produktionsgut sein.', True], ['Nachfrage ist ein Bedürfnis ohne Kaufkraft.', False]])],
 'aufwand#ks': [
   bl([['Eine Spende ist betriebsfremder Aufwand.', True], ['Kalkulatorische Abschreibungen sind Anderskosten.', True],
       ['Zusatzkosten sind Kosten, denen ein Aufwand in gleicher Höhe gegenübersteht.', False], ['Neutraler Aufwand fließt in die Kostenrechnung ein.', False]]),
   bl([['Grundkosten entsprechen dem Zweckaufwand.', True], ['Ein Brandschaden ist außerordentlicher Aufwand.', True],
       ['Die Finanzbuchhaltung rechnet mit Kosten und Leistungen.', False], ['Der kalkulatorische Unternehmerlohn ist ein Zusatzkostenbeispiel.', True]]),
   rk('Erklären Sie Grund-, Anders- und Zusatzkosten mit je einem Beispiel.', 'Grundkosten: Zweckaufwand = Kosten (Löhne, Material). Anderskosten: Kosten in anderer Höhe als der Aufwand (kalkulatorische Abschreibung). Zusatzkosten: Kosten ohne Aufwand (kalkulatorischer Unternehmerlohn, kalk. Eigenkapitalzins).', ['Grundkosten', 'Anderskosten', 'Zusatzkosten'])],
 'umsatz#ks': [
   bl([['Produktivität ist Output durch Input in Mengen.', True], ['Produktivität berücksichtigt Preise und Qualität.', False],
       ['Umsatz = Preis · Menge.', True], ['Verschiedene Produktionsfaktoren lassen sich zu einer Gesamtproduktivität addieren.', False]]),
   nu('Ein Betrieb fertigt {A} Stück in {B} Arbeitsstunden. Wie hoch ist die Arbeitsproduktivität (Stück je Stunde)?', {'v': {'A': [200, 900, 50], 'B': [20, 60, 5]}, 'a': 'A/B', 'r': 2},
      '{A} ÷ {B} = {=A/B} Stück je Stunde', 'Arbeitsproduktivität = Ausbringung ÷ Arbeitsstunden'),
   rk('Erklären Sie, warum die Produktivität allein den Erfolg eines Betriebs nicht messen kann.', 'Sie ist eine Mengengröße: Sie sieht keine Preise und keine Qualität, und verschiedene Faktoren lassen sich nicht addieren (nur Teilproduktivitäten). Erfolg zeigen erst Wirtschaftlichkeit, Gewinn und Rentabilität.', ['Mengen', 'Preise', 'Qualität', 'Teilproduktivitäten'])],
 'finregeln#ks': [bl([['Die Goldene Bilanzregel verlangt, dass langfristiges Kapital das Anlagevermögen deckt.', True], ['Die vertikale Kapitalstrukturregel betrifft das Verhältnis EK zu FK.', True],
                      ['Finanzierungsregeln sagen künftige Zahlungen sicher voraus.', False], ['Die weiteste Fassung der Goldenen Bilanzregel bezieht den eisernen Bestand ein.', True]])],
 'insolvenz#ks': [bl([['Zahlungsunfähigkeit ist für alle Rechtsformen ein Insolvenzgrund.', True], ['Drohende Zahlungsunfähigkeit berechtigt auch die Gläubiger zum Antrag.', False],
                      ['Überschuldung ist ein Insolvenzgrund für juristische Personen.', True], ['Im Berichtstermin entscheiden die Gläubiger über Fortführung oder Auflösung.', True]])],
 'abzinsen#ks': [
   bl([['Der Abzinsungsfaktor lautet 1 ÷ (1 + i)ᵗ.', True], ['Der Barwert einer ewigen Rente ist Zahlung · Zinssatz.', False],
       ['Der Rentenbarwertfaktor ist der Kehrwert des Annuitätenfaktors.', True], ['Ein positiver Kapitalwert heißt: Die Investition ist schlechter als die Alternative.', False]]),
   nu('Eine ewige Rente zahlt jährlich {A} €, der Zinssatz ist {B} %. Wie hoch ist der Barwert?', {'v': {'A': [1000, 9000, 500], 'B': [2, 8, 1]}, 'a': 'A/(B/100)', 'r': 2},
      '{A} ÷ {=B/100} = {=A/(B/100)} €', 'Barwert = Zahlung ÷ Zinssatz'),
   nu('In {B} Jahren erhalten Sie {A} €. Wie viel ist das heute bei {C} % wert?', {'v': {'A': [5000, 20000, 1000], 'B': [2, 5, 1], 'C': [3, 8, 1]}, 'a': 'A/(1+C/100)^B', 'r': 2},
      '{A} ÷ (1 + {=C/100})^{B} = {=A/(1+C/100)^B} €', 'Barwert = Betrag ÷ (1 + i)ᵗ')],
 'eva#ks': [
   bl([['EVA = (Rendite − WACC) · Kapital.', True], ['Ein negativer EVA ist bei positivem Gewinn unmöglich.', False],
       ['Der EVA zieht zusätzlich die Kosten des Eigenkapitals ab.', True], ['Der MVA ist der Barwert aller künftigen EVAs.', True]]),
   nu('Rendite {A} %, WACC {B} %, investiertes Kapital {C} Mio. €. Wie hoch ist der EVA (in Mio. €)?', {'v': {'A': [6, 14, 1], 'B': [5, 10, 1], 'C': [10, 90, 10]}, 'a': '(A-B)/100*C', 'r': 2},
      '({A} % − {B} %) · {C} = {=(A-B)/100*C} Mio. €', 'EVA = (Rendite − WACC) · Kapital'),
   rk('Erklären Sie, warum ein Unternehmen mit Gewinn trotzdem Wert vernichten kann (EVA).', 'Der Gewinn zieht nur die Fremdkapitalzinsen ab. Der EVA zieht auch die Kosten des Eigenkapitals ab: Liegt die Rendite unter dem WACC, ist der EVA negativ – es wird weniger verdient, als das Kapital kostet.', ['Eigenkapital', 'WACC', 'negativ'])],
 'roi#ks': [bl([['ROI = Umsatzrentabilität · Kapitalumschlag.', True], ['Kapitalumschlag = Gesamtkapital ÷ Umsatz.', False],
                ['Bei kleiner Umsatzrendite wirkt eine Kostensenkung wie ein großer Umsatzzuwachs.', True], ['ROI = betriebsnotwendiges Vermögen ÷ Gewinn.', False]])],
 'geschichte#ks': [bl([['Eugen Schmalenbach gilt als Begründer der BWL.', True], ['Im ersten Methodenstreit vertrat Rieger die praktische Kunstlehre.', False],
                       ['Schmalenbach sah die BWL als praxisorientierte Kunstlehre.', True], ['Der erste Methodenstreit ging um Kunstlehre oder Wissenschaft.', True]])],
 'geschichte': [mc('Was war der Streitpunkt im ersten Methodenstreit?', 'Kunstlehre (Praxis) oder Wissenschaft (Theorie)', ['Markt oder Staat', 'Gewinn oder Umsatz', 'Kosten oder Leistung']),
                mc('Wer vertrat die BWL als theoretische Wissenschaft?', 'Rieger', ['Schmalenbach', 'Gutenberg', 'Heinen'], lvl=1)],
 'ansaetze#ks': [bl([['Die Ansätze der BWL ersetzen einander zeitlich.', False], ['Gutenbergs Ansatz ist produktionsfaktortheoretisch.', True],
                     ['Ulrich vertritt den systemorientierten Ansatz.', True], ['Der situative Ansatz geht auf Heinen zurück.', False]])],
 'heinen#ks': [bl([['Bei Heinen stehen Entscheidungen von Menschen im Mittelpunkt.', True], ['Heinen verbindet Nicklisch und Gutenberg.', True],
                   ['Erklärungsmodelle sagen, welche Alternative gewählt werden sollte.', False], ['Nach Heinen verfolgen Unternehmen nur das Ziel Gewinn.', False]])],
 'ulrich#ks': [bl([['Negative Rückkopplung bremst die Ursache und stabilisiert.', True], ['Positive Rückkopplung ist immer erwünscht.', False],
                   ['Nach Ulrich ist die Unternehmung ein offenes, produktives soziales System.', True], ['Lineares Denken beachtet Nebenwirkungen und Kreisläufe.', False]])],
 'situativ#ks': [
   bl([['Nach dem situativen Ansatz gibt es keine allgemein beste Organisation.', True], ['Die Situation ist im situativen Ansatz die abhängige Variable.', False],
       ['Größe und Technologie sind Situationsfaktoren.', True], ['Ein Kritikpunkt ist, dass Korrelation nicht Ursache bedeutet.', True]]),
   bl([['Die Gestaltung (z. B. Zahl der Hierarchieebenen) ist die abhängige Variable.', True], ['Der situative Ansatz lässt Managern viel Gestaltungsspielraum.', False],
       ['Die Auswahl der Situationsfaktoren gilt als willkürlich.', True], ['Externe Faktoren wie Konkurrenz zählen nicht zur Situation.', False]]),
   rk('Erklären Sie den situativen Ansatz mit seinen Variablen und nennen Sie einen Kritikpunkt.', 'Es gibt keine allgemein beste Lösung. Situation (unabhängige Variable: Größe, Technologie, Branche, Umwelt) → Gestaltung/Struktur (abhängige Variable) → Erfolg. Kritik: deterministisch, Faktorenauswahl willkürlich, Korrelation ≠ Ursache.', ['Situation', 'Gestaltung', 'abhängig', 'Erfolg'])],
 'verhalten#ks': [
   bl([['Die arbeitsorientierte Einzelwirtschaftslehre stellt die Interessen der Arbeitnehmer in den Mittelpunkt.', True], ['Der verhaltensorientierte Ansatz hält am strengen Rationalprinzip fest.', False],
       ['Der ökologieorientierte Ansatz bezieht die natürliche Umwelt ein.', True], ['Der marketingorientierte Ansatz richtet das Unternehmen am Markt aus.', True]]),
   bl([['Der verhaltensorientierte Ansatz baut auf Heinen auf.', True], ['Die arbeitsorientierte Einzelwirtschaftslehre stammt vom Arbeitgeberverband.', False],
       ['Begrenzte Rationalität ist ein Kernbegriff des verhaltensorientierten Ansatzes.', True], ['Der ökologieorientierte Ansatz ignoriert Emissionen.', False]]),
   rk('Nennen und erklären Sie zwei Ansätze neben Gutenberg, Heinen, Ulrich und dem situativen Ansatz.', 'Arbeitsorientiert (WSI/DGB): Interessen der Arbeitnehmer. Marketingorientiert: ganzes Unternehmen am Markt ausgerichtet. Ökologieorientiert: Umwelt einbeziehen. Verhaltensorientiert: tatsächliches Verhalten, begrenzte Rationalität.', ['arbeitsorientiert', 'marketingorientiert', 'ökologieorientiert', 'verhaltensorientiert'])],
 'feld#ks': [bl([['Bei Risiko sind die Wahrscheinlichkeiten der Umweltzustände bekannt.', True], ['Bei Unsicherheit kennt man die möglichen Ergebnisse nicht.', False],
                 ['Die Zeilen der Ergebnismatrix sind die eigenen Alternativen.', True], ['Ein Spiel liegt vor, wenn ein rationaler Gegenspieler handelt.', True]])],
 'eis#ks': [
   bl([['Im Eisstand-Modell landen beide Händler in der Mitte.', True], ['Die Positionen 1/4 und 3/4 sind ein stabiles Gleichgewicht.', False],
       ['Die Badegäste an den Rändern verlieren durch längere Wege.', True], ['Das Modell nimmt unterschiedliche Preise der Händler an.', False]]),
   bl([['Das Ergebnis in der Mitte ist ein Nash-Gleichgewicht.', True], ['Parteien, die in die politische Mitte drängen, folgen demselben Muster.', True],
       ['Jeder Händler gewinnt Kunden, wenn er nach außen rückt.', False], ['Im Modell geht jeder Gast zum nächsten Stand.', True]]),
   rk('Erklären Sie das Eisstand-Modell (Hotelling) und warum das Ergebnis für die Badegäste nicht optimal ist.', 'Zwei Händler an einem Strand, gleiche Produkte und Preise, Gäste gehen zum nächsten Stand. Wer Richtung Mitte rückt, gewinnt Kunden; deshalb stehen am Ende beide in der Mitte (Nash-Gleichgewicht). Für die Gäste wären 1/4 und 3/4 besser: kürzere Wege für die am Rand.', ['Mitte', 'Nash', 'Kunden', 'Wege'])],
 'eis': [mc('Warum bleiben die Händler nicht bei 1/4 und 3/4 stehen?', 'Wer zur Mitte rückt, gewinnt Kunden', ['Die Mitte ist billiger', 'Das Gesetz verlangt es', 'Die Gäste wollen es'])],
 'scoring#ks': [
   bl([['K.-o.-Kriterien werden vorab geprüft und nicht mitgewichtet.', True], ['Die Gewichte der Nutzwertanalyse sind objektiv messbar.', False],
       ['Die Summe der Gewichte ist 1 bzw. 100 %.', True], ['Eine Schwäche ist Scheingenauigkeit.', True]]),
   nu('Zwei Kriterien mit Gewicht {A} % und {=100-A} %. Alternative X erhält {B} und {C} Punkte. Nutzwert?', {'v': {'A': [20, 80, 10], 'B': [1, 10, 1], 'C': [1, 10, 1]}, 'a': '(A*B+(100-A)*C)/100', 'r': 2},
      '{=A/100} · {B} + {=(100-A)/100} · {C} = {=(A*B+(100-A)*C)/100}', 'Nutzwert = Σ Gewicht · Punkte'),
   rk('Beschreiben Sie die Schritte einer Nutzwertanalyse und nennen Sie einen Kritikpunkt.', '1. K.-o.-Kriterien prüfen 2. Kriterien festlegen und gewichten (Summe 100 %) 3. Punkte je Alternative vergeben 4. Punkte · Gewicht addieren 5. höchster Nutzwert gewinnt. Kritik: subjektive Gewichte und Punkte, Überschneidungen, Scheingenauigkeit.', ['K.-o.', 'gewichten', 'Punkte', 'subjektiv'])],
 'ueberblick#ks': [bl([['Ein Istkaufmann betreibt ein Handelsgewerbe, der Eintrag ist nur deklaratorisch.', True], ['Kapitalgesellschaften stehen in Abteilung A des Handelsregisters.', False],
                       ['Für Nicht-Kaufleute gilt das HGB.', False], ['Die GmbH ist ein Formkaufmann.', True]])],
 'einzel#ks': [bl([['Der Einzelunternehmer haftet mit seinem Privatvermögen.', True], ['Für ein Einzelunternehmen ist ein Mindestkapital von 25.000 € nötig.', False],
                   ['Der Einzelunternehmer zahlt sich ein Gehalt als Betriebsausgabe.', False], ['Die Ein-Mann-GmbH ist kein Einzelunternehmen.', True]])],
 'stille#ks': [bl([['Der stille Gesellschafter tritt nach außen nicht auf.', True], ['Der typische stille Gesellschafter ist an den stillen Reserven beteiligt.', False],
                   ['Der stille Gesellschafter hat ein Kontrollrecht, aber keine Geschäftsführung.', True], ['Die stille Gesellschaft ist eine Handelsgesellschaft.', False]])],
 'stille': [mc('Warum gilt die stille Einlage wirtschaftlich eher als Eigenkapital?', 'Der Stille trägt das Risiko mit', ['Sie ist zinslos', 'Sie steht im Handelsregister', 'Sie ist unkündbar']),
            mc('Was unterscheidet die atypische von der typischen stillen Gesellschaft?', 'Beteiligung auch an stillen Reserven', ['Haftung nach außen', 'Geschäftsführung', 'Eintrag ins Register'])],
 'kgaa#ks': [bl([['In der KGaA haftet mindestens ein Komplementär persönlich.', True], ['Die Aktionäre einer KGaA können den Komplementär absetzen.', False],
                 ['Merck und Henkel sind Beispiele für eine KGaA.', True], ['In der GmbH & Co. KGaA ist eine GmbH Komplementär.', True]])],
 'kgaa': [mc('Warum wählen Familienunternehmen gern die KGaA?', 'Kapital über die Börse, Führung bleibt bei der Familie', ['Keine Haftung', 'Keine Steuern', 'Kein Aufsichtsrat'])],
 'partg#ks': [bl([['Freiberufler dürfen keine OHG gründen.', True], ['In der PartG mbB haftet für Berufsfehler nur das Gesellschaftsvermögen.', True],
                  ['Die PartG wird ins Handelsregister eingetragen.', False], ['Eine Stiftung hat Eigentümer und Mitglieder.', False]])],
 'cashflow': [mc('Warum wird die Abschreibung beim Cash Flow addiert?', 'Sie mindert den Gewinn, kostet aber kein Geld', ['Sie erhöht den Umsatz', 'Sie ist eine Einzahlung', 'Das HGB schreibt es vor'])],
 'gbr': [mc('Eine Lerngruppe teilt sich Kosten. Welche GbR?', 'Innen-GbR', ['Außen-GbR', 'eGbR', 'OHG'])],
 'ohg': [mc('Ein OHG-Gesellschafter kauft eine Maschine allein. Ist die OHG gebunden?', 'Ja, Einzelvertretung', ['Nein, alle müssen zustimmen', 'Nur mit Notar', 'Nur bis 10.000 €'])],
 'ug': [mc('Warum muss die UG 25 % des Jahresüberschusses zurücklegen?', 'Um Kapital bis zu 25.000 € aufzubauen', ['Für Steuern', 'Für die Dividende', 'Für den Notar'])],
 'eg': [mc('Wie profitiert ein Genossenschaftsmitglied vor allem?', 'Über günstige Preise und Leistungen', ['Über hohe Dividenden', 'Über Aktienkurse', 'Über Steuervorteile']),
        mc('Ein Mitglied hat 10 Anteile, ein anderes einen. Stimmrecht?', 'Jedes hat eine Stimme', ['10 zu 1', 'nach Einlage', 'nur der Vorstand stimmt'])],
 # Leitern
 'shv#beta': [mc('Was bedeutet ein Beta von 1?', 'Die Aktie schwankt wie der Markt', ['Kein Risiko', 'Doppeltes Risiko', 'Sie schwankt gar nicht'])],
 'guv#gkv': [mc('Lagerbestand an fertigen Erzeugnissen steigt. Wie zeigt das GKV das?', 'als Bestandserhöhung (Ertrag)', ['gar nicht', 'als Aufwand', 'als Umsatz'])],
 'insolvenz#kl': [dict(y='kurz', p='Wie heißt der Insolvenzgrund für juristische Personen, wenn das Vermögen die Schulden nicht mehr deckt?', ok=['Überschuldung'], w='', klausur=True, stil=1, lvl=2)],
 'bilanz#negek': [dict(y='kurz', p='Auf welcher Seite der Bilanz steht ein negatives Eigenkapital?', ok=['Aktivseite', 'Aktiva', 'aktiv'], w='als „nicht durch Eigenkapital gedeckter Fehlbetrag“', klausur=True, stil=1, lvl=2),
                  mc('Was bedeutet ein negatives Eigenkapital?', 'Die Schulden übersteigen das Vermögen', ['Das Unternehmen hat keinen Gewinn', 'Die Kasse ist leer', 'Es gibt keine Aktionäre']),
                  mc('Wie heißt der Posten für negatives Eigenkapital?', 'nicht durch EK gedeckter Fehlbetrag', ['Jahresfehlbetrag', 'Verlustrücklage', 'Bilanzverlust'], lvl=1)],
 'rent#lev': [
   mc('Was beschreibt der Leverage-Effekt?', 'Hebel des Fremdkapitals auf die EK-Rendite', ['Hebel der Werbung auf den Umsatz', 'Wirkung von Steuern auf den Gewinn', 'Zinseszins'], lvl=1),
   mc('r_GK = 10 %, Zins 6 %. Mehr Fremdkapital …', 'erhöht die EK-Rendite', ['senkt die EK-Rendite', 'ändert nichts', 'senkt den Zins']),
   mc('r_GK fällt unter den Fremdkapitalzins. Was passiert?', 'Der Hebel kehrt sich um, Verluste wachsen', ['Die EK-Rendite steigt weiter', 'Nichts', 'Der Zins sinkt automatisch']),
   mc('Warum ist unbegrenzt mehr Fremdkapital nicht sinnvoll?', 'Zinsen und Tilgung sind auch in schlechten Jahren fällig', ['Banken verbieten es', 'Eigenkapital wird teurer', 'Steuern steigen']),
   mc('Welchen Vorteil hat Wachstum über Fremdkapital für die Eigentümer?', 'Keine Verwässerung der Stimmrechte', ['Keine Zinsen', 'Keine Haftung', 'Höhere Steuern'])],
 'wacc#ts': [
   mc('Was ist der Tax-Shield?', 'Steuerersparnis, weil Zinsen den Gewinn mindern', ['Schutz vor Insolvenz', 'Steuer auf Dividenden', 'Rücklage für Steuern'], lvl=1),
   mc('Wie wirkt der Tax-Shield auf die Fremdkapitalkosten?', 'Er senkt sie auf i · (1 − s)', ['Er erhöht sie', 'Er ändert nichts', 'Er senkt die EK-Kosten']),
   mc('Warum steigen die EK-Kosten mit dem Verschuldungsgrad?', 'Das Risiko der Eigentümer steigt', ['Die Steuer steigt', 'Banken verlangen es', 'Der Tax-Shield fällt weg']),
   mc('Kreditzins 5 %, Steuersatz 30 %. FK-Kosten nach Steuern?', '3,5 %', ['5 %', '1,5 %', '6,5 %'])],
 'polent#ziele': [
   mc('Warum konkurrieren Liquidität und Rentabilität?', 'Liquide Mittel bringen kaum Rendite', ['Sie sind dasselbe', 'Das HGB schreibt es vor', 'Rentabilität erhöht Liquidität']),
   mc('Kosten senken und Gewinn steigern sind …', 'komplementär', ['konkurrierend', 'indifferent', 'identisch'], lvl=1),
   mc('Ein Unternehmen hält viel Bargeld als Reserve. Was leidet?', 'die Rentabilität', ['die Liquidität', 'der Umsatz', 'nichts']),
   mc('Ein Ziel hat keinen Einfluss auf ein anderes. Zielbeziehung?', 'indifferent', ['komplementär', 'konkurrierend', 'identisch'], lvl=1),
   lu('Rentabilität und Liquidität stehen meist in einer <b>[[0]]</b> Zielbeziehung.', [['konkurrierenden', 'konkurrierend']]),
   mc('Warum kann ein Unternehmen mit Gewinn pleitegehen?', 'Gewinn ist kein Geld am Fälligkeitstag', ['Gewinn wird versteuert', 'Gewinn ist geheim', 'Das ist unmöglich'])],
}
PUNKT.update({'shv#beta': dict(punkt='beta'), 'guv#gkv': dict(punkt='gkv'), 'insolvenz#kl': dict(punkt='insolvenz'), 'bilanz#negek': dict(punkt='neg-ek'),
              'rent#lev': dict(punkt='leverage'), 'wacc#ts': dict(punkt='taxshield'), 'polent#ziele': dict(punkt='ziele-konkurrierend')})

MARKETING = {
 'leitprinzipien': [mc('Bei Überangebot hat der Absatz den Engpass. Was folgt nach der Engpasstheorie?', 'Der Absatz dominiert zeitweise', ['Die Produktion dominiert', 'Alle Bereiche sind gleich', 'Die Finanzen dominieren'])],
 'meffert': [mc('Welcher moderne Ansatz nach Meffert ist bis heute dominant?', 'entscheidungsorientiert', ['verhaltenswissenschaftlich', 'systemtheoretisch', 'warenorientiert']),
             mc('Was ist die Schwäche von Kotlers Phasenmodell laut Meffert?', 'Es muss mit jeder Entwicklung ergänzt werden', ['Es ist zu mathematisch', 'Es kennt keine Kunden', 'Es gilt nur für Industrie'])],
 'infooek#ks': [dict(y='liste', p='Nennen Sie zwei Instrumente, mit denen Anbieter und Nachfrager Informationsasymmetrien abbauen, und je ein Beispiel.', pk=[['Signaling', 'Signal', 'Garantie', 'Marke', 'Zertifikat'], ['Screening', 'Test', 'Bewertung']], n=2, w='', klausur=True, stil=1, lvl=3)],
 'marktformen#ks': [
   dict(y='liste', p='Nennen Sie die drei Marktformen nach der Zahl der Anbieter.', pk=[['Monopol', 'einer'], ['Oligopol', 'wenige'], ['Polypol', 'viele']], n=3, w='', klausur=True, stil=1, lvl=2),
   dict(y='rev', p='Erklären Sie das Marktformenschema und ordnen Sie den Glühweinstand auf dem Weihnachtsmarkt ein.', l='3 × 3-Schema: Anbieter und Nachfrager je einer (Monopol), wenige (Oligopol), viele (Polypol). Glühweinstand: viele Anbieter und viele Nachfrager → Polypol (auf einem unvollkommenen Markt: Polypoloid).', pk=['Monopol', 'Oligopol', 'Polypol', 'viele'], w='', klausur=True, stil=1, lvl=3),
   dict(y='rev', p='Erklären Sie, was „-oid“-Marktformen sind, und nennen Sie ein Beispiel.', l='„-oid“: die Marktform auf einem unvollkommenen Markt, z. B. Oligopoloid = Oligopol auf einem unvollkommenen Markt (Tankstellen mit unterschiedlichen Standorten).', pk=['unvollkommen', 'Oligopoloid'], w='', klausur=True, stil=1, lvl=3)],
 'infodreieck': [mc('Die Qualität einer Autoreparatur kann man kaum je prüfen. Welche Eigenschaft?', 'Vertrauenseigenschaft', ['Sucheigenschaft', 'Erfahrungseigenschaft', 'Grundnutzen'])],
 'abc': [mc('Ein C-Produkt hat einen kleinen Umsatz. Warum streicht man es nicht sofort?', 'Verbundbeziehungen, z. B. Drucker und Patronen', ['C-Produkte sind gesetzlich geschützt', 'Sie haben immer hohe Gewinne', 'Kunden kaufen nur C-Produkte']),
         mc('Was ist der Deckungsbeitrag je Stück?', 'Preis minus variable Kosten', ['Preis minus Fixkosten', 'Umsatz minus Gewinn', 'Gewinn je Kunde'], lvl=1)],
 'werte': [mc('Was bedeutet der Wertewandel für das Marketing?', 'Produkte und Werbung an wachsende Werte anpassen', ['Preise senken', 'Werbung einstellen', 'Nur noch online verkaufen'])],
 'aspekte#kl': [dict(y='liste', p='Nennen Sie vier Aspekte des Marketing und erklären Sie sie in je einem Satz.', pk=[['Philosophieaspekt', 'Philosophie'], ['Verhaltensaspekt', 'Verhalten'], ['Informationsaspekt', 'Information'], ['Strategieaspekt', 'Strategie'], ['Aktionsaspekt', 'Aktion'], ['Segmentierungsaspekt', 'Segment'], ['Koordinationsaspekt', 'Koordination'], ['Sozialaspekt', 'Sozial']], n=4, w='', klausur=True, stil=1, lvl=2)],
 'einsatz#kl': [dict(y='liste', p='Nennen Sie vier Bereiche, in denen Marketing neben dem Absatz eingesetzt wird.', pk=[['Personalmarketing', 'Personal'], ['Beschaffungsmarketing', 'Beschaffung'], ['Finanzmarketing', 'Investor'], ['Stadtmarketing', 'Regionalmarketing', 'Stadt'], ['Non-Profit', 'Sozio'], ['politisches Marketing', 'Wahl']], n=4, w='', klausur=True, stil=1, lvl=2)],
 'gratifikation#kl': [dict(y='liste', p='Nennen Sie drei Formen der Gratifikation außer Geld.', pk=[['Zeitersparnis', 'Zeit'], ['Ansehen', 'Prestige', 'Anerkennung'], ['gutes Gefühl', 'Gefühl', 'Freude']], n=3, w='', klausur=True, stil=1, lvl=2)],
}
PUNKT.update({'aspekte#kl': dict(punkt='aspekte'), 'einsatz#kl': dict(punkt='einsatz'), 'gratifikation#kl': dict(punkt='gratifikation')})

def weg(p, schritte, falsch, w, lvl=2): return dict(y='mc', weg=1, p=p, o=[[x, j == falsch] for j, x in enumerate(schritte)], w=w, lvl=lvl)


MATHE_KREATIV = {
 'm1-mengen#weg': [weg('A = {1, 2, 3, 4}, B = {3, 4, 5}. Wo steckt der Fehler?', ['A ∩ B = {3, 4}', 'A ∪ B = {1, 2, 3, 4, 5}', 'A \\ B = {1, 2, 5}', 'B \\ A = {5}'], 2, 'A \\ B enthält nur Elemente aus A, die nicht in B liegen: {1, 2}. Die 5 gehört gar nicht zu A.'),
                   dict(y='zuord', p='Welches Zeichen gehört zu welcher Operation?', k=['∩', '∪', '\\', '⊂'], e=[['Schnittmenge', 0], ['Vereinigungsmenge', 1], ['Differenzmenge', 2], ['Teilmenge', 3]], w='', lvl=1)],
 'm1-potenzen#weg': [weg('Vereinfachen Sie (x³ · x⁻⁵) ÷ x⁻⁴. Wo steckt der Fehler?', ['x³ · x⁻⁵ = x⁻²', 'x⁻² ÷ x⁻⁴ = x⁻⁶', 'Ergebnis: x⁻⁶'], 1, 'Beim Teilen werden Exponenten subtrahiert: −2 − (−4) = 2, also x².'),
                     weg('Lösen Sie 2ˣ = 32. Wo steckt der Fehler?', ['ln(2ˣ) = ln 32', 'x · ln 2 = ln 32', 'x = ln 32 − ln 2', 'x ≈ 2,77'], 2, 'Man teilt durch ln 2: x = ln 32 ÷ ln 2 = 5.'),
                     dict(y='luecke', p='2ˣ = 32 → x · ln 2 = ln 32 → x = ln 32 <b>[[0]]</b> ln 2 = <b>[[1]]</b>', l=[['÷', ':', '/', 'geteilt durch'], ['5']], w='Exponent mit dem Logarithmus „herunterholen“, dann teilen.', lvl=2)],
 'm1-terme#weg': [weg('Kürzen Sie (a² − b²) ÷ (a − b). Wo steckt der Fehler?', ['a² − b² = (a + b)(a − b)', 'Kürzen durch (a − b)', 'Ergebnis: a − b'], 2, 'Nach dem Kürzen bleibt (a + b) stehen.'),
                  weg('Lösen Sie (x − 3)² auf. Wo steckt der Fehler?', ['(x − 3)² = x² − 2 · 3 · x + 3²', '= x² − 6x − 9', 'fertig'], 1, '3² = +9, das Vorzeichen bleibt positiv: x² − 6x + 9.')],
 'm1-gleichungen#weg': [weg('Lösen Sie 3(x − 2) = 2x + 4. Wo steckt der Fehler?', ['3x − 2 = 2x + 4', 'x − 2 = 4', 'x = 6'], 0, 'Die 3 multipliziert beide Glieder der Klammer: 3x − 6. Richtig ist x = 10.'),
                        weg('x + y = 10 und x − y = 4. Wo steckt der Fehler?', ['Addieren: 2x = 14', 'x = 7', 'y = 10 + 7 = 17'], 2, 'Aus x + y = 10 folgt y = 10 − 7 = 3.')],
 'm1-summen#weg': [weg('Berechnen Sie Σ (i = 1 bis 3) (2i + 1). Wo steckt der Fehler?', ['i = 1: 3', 'i = 2: 5', 'i = 3: 6', 'Summe: 14'], 2, 'Für i = 3: 2 · 3 + 1 = 7. Die Summe ist 15.'),
                   weg('Berechnen Sie Σ (i = 1 bis 2) Σ (j = 1 bis 2) i · j. Wo steckt der Fehler?', ['i = 1: 1 · 1 + 1 · 2 = 3', 'i = 2: 2 · 1 + 2 · 2 = 6', 'Gesamt: 3 · 6 = 18'], 2, 'Die äußere Summe addiert: 3 + 6 = 9.')],
 'm2-folgen#weg': [weg('Geometrische Folge 3, 6, 12, … Gesucht: a₆. Wo steckt der Fehler?', ['q = 6 ÷ 3 = 2', 'aₙ = a₁ · qⁿ', 'a₆ = 3 · 2⁶ = 192'], 1, 'Richtig ist aₙ = a₁ · qⁿ⁻¹, also a₆ = 3 · 2⁵ = 96.')],
 'm2-zins#weg': [weg('10.000 € werden 3 Jahre zu 5 % angelegt. Wo steckt der Fehler?', ['K₃ = 10.000 · 1,05³', '1,05³ = 1,15', 'K₃ = 11.500 €'], 1, 'Mit Zinseszins: 1,05³ = 1,157625, also K₃ = 11.576,25 €. 1,15 wären nur einfache Zinsen.'),
                 weg('Nach wie vielen Jahren verdreifacht sich ein Kapital bei 8 %? Wo steckt der Fehler?', ['3 · K₀ = K₀ · 1,08ⁿ', '3 = 1,08ⁿ', 'n = 3 ÷ 1,08', 'n ≈ 2,78 Jahre'], 2, 'n steht im Exponenten: n = ln 3 ÷ ln 1,08 ≈ 14,27 Jahre.'),
                 dict(y='zuord', p='Welcher Faktor beantwortet welche Frage?', k=['(1 + i)ⁿ', '1 ÷ (1 + i)ⁿ', 'Rentenbarwertfaktor', 'Annuitätenfaktor'], e=[['Was wird aus 1 € heute in n Jahren?', 0], ['Was ist 1 € in n Jahren heute wert?', 1], ['Was sind n Raten von 1 € heute wert?', 2], ['Welche gleiche Rate tilgt 1 € in n Jahren?', 3]], w='', lvl=2)],
 'm2-rente#weg': [weg('3 × 10.000 € am Jahresende bei 5 %: Barwert? Wo steckt der Fehler?', ['10.000 ÷ 1,05 = 9.523,81', '10.000 ÷ 1,05² = 9.070,29', '10.000 ÷ (1,05 · 3) = 3.174,60', 'Summe bilden'], 2, 'Die dritte Zahlung wird mit 1,05³ abgezinst: 8.638,38. Barwert gesamt 27.232,48 €.')],
 'm2-annuitaet#weg': [weg('20.000 € sollen in 3 Jahren bei 1 % gleichmäßig entnommen werden. Wo steckt der Fehler?', ['q = 1,01', 'Annuitätenfaktor = 1,01³ · 0,01 ÷ (1,01³ − 1) ≈ 0,34002', 'A = 20.000 ÷ 0,34002', 'A ≈ 58.820 €'], 2, 'Man multipliziert: A = 20.000 · 0,34002 ≈ 6.800,44 € pro Jahr.')],
 'm2-kapitalwert#weg': [weg('Investition 100, Rückflüsse 60 und 60, Kalkulationszins 10 %. Wo steckt der Fehler?', ['60 ÷ 1,1 = 54,55', '60 ÷ 1,1² = 49,59', 'C₀ = 54,55 + 49,59 = 104,14', 'Die Investition lohnt sich.'], 2, 'Die Anschaffungsauszahlung fehlt: C₀ = −100 + 104,14 = 4,14 > 0. Die Investition lohnt sich trotzdem.'),
                        dict(y='reihe', p='Bringen Sie den Rechenweg zum Kapitalwert in die richtige Reihenfolge.', o=['Einzahlungsüberschüsse je Jahr bestimmen', 'Jeden Überschuss abzinsen', 'Barwerte addieren', 'Anschaffungsauszahlung abziehen', 'Vorzeichen deuten'], w='', lvl=2)],
 'm2-izf#weg': [weg('i₁ = 10 %: C₀ = 5,41; i₂ = 15 %: C₀ = −4,21. Wo steckt der Fehler?', ['r = i₁ + C₀₁ · (i₂ − i₁) ÷ (C₀₁ − C₀₂)', 'r = 10 + 5,41 · 5 ÷ (5,41 − 4,21)', 'r = 10 + 22,5 = 32,5 %'], 1, 'C₀₁ − C₀₂ = 5,41 − (−4,21) = 9,62. Also r = 10 + 27,05 ÷ 9,62 ≈ 12,8 %.'),
                dict(y='reihe', p='Bringen Sie das Vorgehen beim internen Zinsfuß in die richtige Reihenfolge.', o=['Zwei Versuchszinssätze wählen', 'Kapitalwerte für beide berechnen (einer positiv, einer negativ)', 'Linear interpolieren', 'Mit dem Kalkulationszins vergleichen'], w='', lvl=2)],
 'm3-breakeven#weg': [weg('G(x) = 2x − 10.000. Break-even? Wo steckt der Fehler?', ['G(x) = 0 setzen', '2x = 10.000', 'x = 20.000'], 2, 'x = 10.000 ÷ 2 = 5.000.'),
                      dict(y='reihe', p='Bringen Sie den Rechenweg zum Break-even in die richtige Reihenfolge.', o=['Erlösfunktion aus Preis und Menge aufstellen', 'Gewinn = Erlös − Kosten', 'Gewinn gleich null setzen', 'Nach x auflösen und deuten'], w='', lvl=2)],
 'm3-grenzwerte#weg': [weg('lim (x → 0) (eˣ − 1) ÷ x. Wo steckt der Fehler?', ['Einsetzen ergibt 0 ÷ 0', 'l’Hospital: Zähler und Nenner getrennt ableiten', 'eˣ ÷ 1 bei x = 0 ergibt 0'], 2, 'e⁰ = 1, der Grenzwert ist 1.')],
 'm3-monotonie#weg': [weg('f(x) = x³ − 3x. Wo steckt der Fehler?', ['f′(x) = 3x² − 3', 'f′(x) = 0 bei x = −1 und x = 1', 'f′(0) = −3, also ist f bei 0 steigend'], 2, 'f′(0) < 0: f ist zwischen −1 und 1 fallend.')],
 'm4-regeln#weg': [weg('Ableiten Sie f(x) = x² · eˣ. Wo steckt der Fehler?', ['u = x², v = eˣ', 'u′ = 2x, v′ = eˣ', 'f′(x) = 2x · eˣ'], 2, 'Produktregel: f′ = u′v + uv′ = 2x · eˣ + x² · eˣ.'),
                   weg('Ableiten Sie f(x) = (3x + 1)⁴. Wo steckt der Fehler?', ['äußere Ableitung: 4(3x + 1)³', 'innere Ableitung: 3', 'f′(x) = 4(3x + 1)³ + 3'], 2, 'Kettenregel: äußere mal innere Ableitung, f′ = 12(3x + 1)³.'),
                   dict(y='zuord', p='Welche Ableitung gehört zu welcher Funktion?', k=['x³', 'eˣ', 'ln x', '5x'], e=[['3x²', 0], ['eˣ', 1], ['1 ÷ x', 2], ['5', 3]], w='', lvl=1)],
 'm4-extrem#weg': [weg('G(x) = −x² + 40x − 300. Wo steckt der Fehler?', ['G′(x) = −2x + 40', 'G′(x) = 0 → x = 20', 'G″(x) = −2 < 0 → Minimum'], 2, 'G″ < 0 bedeutet Maximum. Gewinnmaximum bei x = 20.'),
                   dict(y='reihe', p='Bringen Sie den Rechenweg zur Gewinnmaximierung in die richtige Reihenfolge.', o=['Gewinnfunktion aufstellen', 'Erste Ableitung bilden', 'Gleich null setzen und lösen', 'Zweite Ableitung prüfen', 'Preis und Gewinn berechnen'], w='', lvl=2)],
 'm4-elastizitaet#weg': [weg('x(p) = 100 − 2p, p = 30. Elastizität? Wo steckt der Fehler?', ['x(30) = 40', 'x′(p) = −2', 'ε = x′ · x ÷ p = −2 · 40 ÷ 30'], 2, 'ε = x′ · p ÷ x = −2 · 30 ÷ 40 = −1,5 (elastisch).'),
                         dict(y='zuord', p='Was bedeutet das Ergebnis?', k=['elastisch', 'unelastisch', 'proportional'], e=[['ε = −2,5', 0], ['ε = −0,3', 1], ['ε = −1', 2]], w='', lvl=2)],
 'm4-partiell#weg': [weg('f(x, y) = x²y + 3y. Wo steckt der Fehler?', ['∂f/∂x = 2xy', '∂f/∂y = 2x + 3', 'df = 2xy · dx + … · dy'], 1, 'Nach y abgeleitet: x² ist ein Faktor, ∂f/∂y = x² + 3.')],
 'm4-lagrange#weg': [weg('Maximieren Sie x · y unter x + y = 10. Wo steckt der Fehler?', ['L = xy + λ(10 − x − y)', 'L_x = y − λ = 0, L_y = x − λ = 0', 'x = y', 'x = y = 10'], 3, 'Aus x = y und x + y = 10 folgt x = y = 5.'),
                     dict(y='reihe', p='Bringen Sie den Lagrange-Rechenweg in die richtige Reihenfolge.', o=['Lagrangefunktion aufstellen', 'Partielle Ableitungen nach x, y und λ bilden', 'Alle gleich null setzen', 'Gleichungssystem lösen', 'Optimum angeben'], w='', lvl=2)],
 'm5-matrizen#weg': [weg('A ist eine 2×3-, B eine 2×3-Matrix. Gesucht A · B. Wo steckt der Fehler?', ['A hat 3 Spalten', 'B hat 2 Zeilen', 'A · B ist eine 2×3-Matrix'], 2, 'Spalten von A (3) ≠ Zeilen von B (2): Das Produkt ist nicht definiert.')],
 'm5-gauss#weg': [weg('I: x + y = 5, II: 2x + y = 8. Wo steckt der Fehler?', ['II − 2 · I: −y = −2', 'y = 2', 'x = 5 + 2 = 7'], 2, 'Aus x + y = 5 folgt x = 5 − 2 = 3.'),
                  dict(y='reihe', p='Bringen Sie den Gauß-Algorithmus in die richtige Reihenfolge.', o=['Erweiterte Matrix (A | b) aufschreiben', 'Unter dem ersten Pivot Nullen erzeugen', 'Unter dem zweiten Pivot Nullen erzeugen', 'Rückwärts einsetzen', 'Probe machen'], w='', lvl=2)],
 'm5-rang#weg': [weg('A = (2 4 | 1 2). Wo steckt der Fehler?', ['det A = 2 · 2 − 4 · 1', 'det A = 0', 'A ist invertierbar'], 2, 'det A = 0: A hat keinen vollen Rang und ist nicht invertierbar.'),
                 dict(y='zuord', p='Was folgt aus dem Ergebnis?', k=['genau eine Lösung', 'keine Lösung', 'unendlich viele Lösungen'], e=[['Rang(A) = Rang(A | b) = Zahl der Variablen', 0], ['Rang(A) < Rang(A | b)', 1], ['Rang(A) = Rang(A | b) < Zahl der Variablen', 2]], w='', lvl=2)],
}
MATHE.update(MATHE_KREATIV)

ALLE = {'logistik': LOGISTIK, 'produktion': PRODUKTION, 'mathe': MATHE, 'abwl': ABWL, 'marketing': MARKETING}


def main():
    for fid, d in ALLE.items():
        fach = json.loads((IN / fid / 'fach.json').read_text(encoding='utf-8'))
        kn = {t['id']: i for i, k in enumerate(fach['kapitel'], 1) for t in k['themen']}
        p = IN / fid / 'fragen_neu.json'; neu = json.loads(p.read_text(encoding='utf-8'))
        neu['familien'] = [x for x in neu['familien'] if ':vs-' not in x.get('id', '')]
        for schl, a in d.items():
            tid, _, suf = schl.partition('#'); suf = '-' + suf if suf else ''
            assert tid in kn, tid
            ver = [x for x in a if not x.get('klausur')]; kl = [x for x in a if x.get('klausur')]
            if ver: neu['familien'].append(dict(id=f'{fid}:{tid}:vs-verstehen{suf}', f=fid, t=tid, k=kn[tid], s=False, y='fam', fam=1, z='Versteht die Zusammenhänge des Unterthemas', a=ver, **PUNKT.get(schl, {})))
            if kl: neu['familien'].append(dict(id=f'{fid}:{tid}:vs-klausur{suf}', f=fid, t=tid, k=kn[tid], s=False, y='fam', fam=1, z='Kann in Klausurform antworten', a=kl, **PUNKT.get(schl, {})))
        p.write_text(json.dumps(neu, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(fid, sum(len(a) for a in d.values()), 'Fragen')


if __name__ == '__main__':
    main()
