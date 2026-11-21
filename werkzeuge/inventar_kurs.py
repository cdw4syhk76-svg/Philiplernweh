"""Klausurpunkte-Inventar (intern, wird nie gebaut) für die Fächer dieses Kurses: inhalte/<fach>/plan/gp_inventar.json.
Wichtige Punkte = Unterthemen mit Stern „★ Wichtig!“ (aus Protokollen, Klausurprofil oder ausdrücklichen Markierungen) – j = 1, wichtig_ab = 1.
Weitere Klausurpunkte aus dem Klausurprofil mit j = 0 (abgedeckt, aber nicht als wichtig markiert).
Aufruf: python3 werkzeuge/inventar_kurs.py"""
import json, pathlib
IN = pathlib.Path(__file__).resolve().parents[1] / 'inhalte'

# fach: [(id, text, [unterthemen], art, [suchwörter], j)]
P = {
'mawi': [
    ('bedarfsarten', 'Primär-, Sekundär-, Tertiärbedarf nennen und erklären', ['bedarfsarten'], 'erklaeren', ['Primärbedarf', 'Sekundärbedarf', 'Tertiärbedarf'], 1),
    ('brutto-netto', 'Vom Brutto- zum Nettobedarf: Positionen nennen und erklären', ['brutto-netto'], 'erklaeren', ['Bruttobedarf', 'Nettobedarf', 'Zusatzbedarf', 'Bestellbestand'], 1),
    ('meldebestand', 'Sicherheitsbestand, Wiederbeschaffungszeit, Meldebestand', ['bestellbegriffe'], 'rechnen', ['Meldebestand', 'Sicherheitsbestand', 'Wiederbeschaffungszeit'], 1),
    ('bestellsysteme', 'Bestellverfahren aus Abbildung erkennen, benennen, begründen', ['bestellsysteme'], 'zeichnen', ['Bestellrhythmus', 'Bestellpunkt', 's,Q', 'r,S', 't,S', 's,S'], 1),
    ('dilemma', 'Dilemma der optimalen Bestellmenge', ['losgroessen-dilemma'], 'erklaeren', ['Dilemma', 'Bestellkosten', 'Lagerkosten', 'gegenläufig'], 1),
    ('andler', 'Optimale Bestellmenge nach Andler berechnen', ['andler'], 'rechnen', ['Andler', 'optimale Bestellmenge'], 1),
    ('abc-xyz', 'XYZ-Analyse und ABC-XYZ-Kombination', ['xyz-analyse'], 'erklaeren', ['XYZ', 'ABC-XYZ', 'Verbrauchsschwankung'], 1),
    ('abc', 'ABC-Analyse durchführen', ['abc-analyse'], 'rechnen', ['ABC'], 0),
    ('glaettung', 'Exponentielle Glättung', ['exp-glaettung'], 'rechnen', ['Glättung', 'Glättungsfaktor'], 0),
],
'bwl': [
    ('dienstleistung', 'Dienstleistung, Uno-actu-Prinzip', ['dienstleistung'], 'erklaeren', ['Dienstleistung', 'uno-actu', 'Uno-actu'], 1),
    ('betriebszweck', 'Betriebe nach Zweck und Größe', ['betriebszweck'], 'nennen', ['Sachleistung', 'Dienstleistung', 'Größe', 'Zweck'], 1),
    ('kennzahlen', 'Gewinn, Wirtschaftlichkeit, Produktivität berechnen', ['kennzahlen'], 'rechnen', ['Wirtschaftlichkeit', 'Produktivität', 'Gewinn'], 1),
    ('breakeven', 'Break-even-Punkt berechnen', ['breakeven'], 'rechnen', ['Break-even', 'Gewinnschwelle'], 1),
    ('rentabilitaet', 'Kapital-, EK-, Umsatzrentabilität', ['rentabilitaet'], 'rechnen', ['Rentabilität', 'Eigenkapitalrentabilität', 'Umsatzrentabilität'], 1),
    ('gewinnmax', 'Gewinnmaximum mit Preis-Absatz-Funktion', ['gewinnmax'], 'rechnen', ['Gewinnmaximum', 'Preis-Absatz'], 1),
    ('rentmax', 'Rentabilitätsmaximum vs. Gewinnmaximum', ['rentmax'], 'rechnen', ['Rentabilitätsmaximum'], 1),
    ('liquiditaet', 'Liquidität, EK-Quote, Leverage', ['liquiditaet'], 'rechnen', ['Liquidität', 'Eigenkapitalquote', 'Leverage'], 1),
    ('elastizitaet', 'Preiselastizität und Einflussfaktoren', ['elastizitaet'], 'erklaeren', ['Elastizität', 'elastisch'], 1),
    ('mittelwert', 'Bogenelastizität (Mittelwertmethode)', ['mittelwert'], 'rechnen', ['Mittelwertmethode', 'Bogenelastizität'], 1),
    ('punktelastizitaet', 'Punktelastizität', ['punktelastizitaet'], 'rechnen', ['Punktelastizität'], 1),
    ('effekte', 'Preis-, Mengen-, Gesamteffekt', ['effekte'], 'rechnen', ['Preiseffekt', 'Mengeneffekt', 'Gesamteffekt'], 1),
    ('opportunitaet', 'Opportunitätskosten', ['opportunitaet'], 'erklaeren', ['Opportunitätskosten'], 1),
    ('grenznutzen', 'Grenznutzen und Grenzkosten', ['grenznutzen'], 'erklaeren', ['Grenznutzen', 'Grenzkosten'], 1),
    ('stakeholder', 'Shareholder- und Stakeholder-Ansatz', ['stakeholder'], 'erklaeren', ['Shareholder', 'Stakeholder'], 1),
    ('zielbeziehungen', 'Zielbeziehungen', ['zielbeziehungen'], 'erklaeren', ['komplementär', 'konkurrierend', 'indifferent'], 1),
    ('zielsystem', 'Dominanz, Effizienz, Lexikographie, Nutzenfunktion', ['zielsystem'], 'rechnen', ['Dominanz', 'Lexikograph', 'Nutzenfunktion', 'effizient'], 1),
    ('hurwicz', 'Hurwicz-Regel', ['hurwicz'], 'rechnen', ['Hurwicz', 'Optimismus'], 1),
    ('bayes', 'Bayes-Regel', ['bayes'], 'rechnen', ['Bayes', 'Erwartungswert', 'µ'], 1),
    ('five-forces', 'Porters Five Forces', ['five-forces'], 'nennen', ['Five Forces', 'Rivalität', 'Ersatzprodukte', 'Verhandlungsmacht'], 1),
    ('swot', 'SWOT-Analyse', ['swot'], 'erklaeren', ['SWOT', 'Stärken', 'Chancen'], 1),
    ('ressourcen', 'Ressourcenanalyse (VRIO)', ['ressourcen'], 'erklaeren', ['Ressource', 'VRIO', 'wertvoll', 'imitierbar'], 1),
    ('renten', 'Renten: Ricardo, Quasi, Monopol, Schumpeter', ['renten'], 'erklaeren', ['Rente', 'Ricardo', 'Schumpeter', 'Quasi'], 1),
    ('bcg', 'BCG-Matrix', ['bcg-matrix'], 'erklaeren', ['BCG', 'Cash Cow', 'Star', 'Poor Dog', 'Question Mark'], 1),
    ('personengesellschaften', 'Einzelunternehmen, GbR, OHG', ['personengesellschaften'], 'erklaeren', ['GbR', 'OHG', 'Einzelunternehm'], 1),
    ('kg', 'Kommanditgesellschaft', ['kg'], 'erklaeren', ['KG', 'Kommandit', 'Komplementär'], 1),
    ('ag', 'Aktiengesellschaft', ['ag'], 'erklaeren', ['AG', 'Aktie', 'Vorstand', 'Aufsichtsrat', 'Hauptversammlung'], 1),
    ('gmbh', 'GmbH', ['gmbh'], 'erklaeren', ['GmbH', 'Stammkapital', 'Geschäftsführer'], 1),
    ('rechtsform-fall', 'Rechtsform erkennen, Insolvenzfall', ['rechtsform-fall'], 'erklaeren', ['Insolvenz', 'Haftung', 'Rechtsform'], 1),
],
'mkt': [
    ('konsum-industrie', 'Konsum- und Industriegütermarketing', ['konsum-industrie'], 'erklaeren', ['Konsumgüter', 'Industriegüter', 'B2B', 'B2C'], 1),
    ('service-beeinflusser', 'Service-Anbieter und Beeinflusser', ['service-beeinflusser'], 'nennen', ['Service', 'Beeinflusser'], 1),
    ('beziehungen', 'Beziehungen zwischen den Marktbeteiligten', ['beziehungen'], 'erklaeren', ['Beziehung', 'Marktbeteiligte', 'Absatzmittler'], 1),
    ('marktumwelten', 'Marktumwelten', ['marktumwelten'], 'nennen', ['Umwelt', 'ökonomisch', 'technologisch', 'rechtlich', 'gesellschaftlich'], 1),
    ('marktabgrenzung', 'Marktabgrenzung: drei Kriterien', ['marktabgrenzung'], 'nennen', ['Marktabgrenzung', 'abgrenz', 'produktbezogen', 'funktional', 'nachfragerbezogen'], 1),
    ('abgrenzung-anwenden', 'Marktabgrenzung anwenden', ['abgrenzung-anwenden'], 'erklaeren', ['eng', 'weit', 'Wettbewerber', 'Glühwein', 'Marktsegment', 'Substitution', 'Teilmärkte'], 1),
    ('segment', 'Nachfragersegment und Zielgruppe', ['segment'], 'erklaeren', ['Segment', 'Zielgruppe'], 1),
    ('segmentierungsmerkmale', 'Segmentierungsmerkmale', ['segmentierungsmerkmale'], 'nennen', ['demograph', 'psychograph', 'sozio-ökonomisch', 'Verhaltensmerkmal', 'Merkmalsgruppe', 'Segmentierung'], 1),
    ('zufriedenheit', 'Kundenzufriedenheit, C/D-Paradigma', ['zufriedenheit'], 'erklaeren', ['Zufriedenheit', 'C/D', 'Confirmation', 'Disconfirmation'], 1),
    ('kano', 'Kano-Modell', ['kano'], 'zeichnen', ['Kano', 'Basis', 'Leistung', 'Begeisterung'], 1),
    ('kundenbindung', 'Kundenbindung: Begriff und Formen', ['kundenbindung'], 'erklaeren', ['Kundenbindung', 'Gebundenheit', 'Verbundenheit'], 1),
    ('determinanten', 'Determinanten der Kundenbindung', ['determinanten'], 'nennen', ['Determinante', 'Wechselbarriere', 'Attraktivität', 'Gebundenheit', 'Verbundenheit', 'wechseln', 'Variety Seeking'], 1),
],
'wima': [
    ('saettigung', 'Grenzwert / Sättigungswert', ['saettigungswert'], 'rechnen', ['Sättigung', 'Grenzwert'], 1),
    ('stetigkeit', 'Stetigkeit', ['stetigkeit'], 'rechnen', ['stetig', 'Unstetigkeit'], 1),
    ('produkt-quotient', 'Produkt- und Quotientenregel', ['produkt-quotient'], 'rechnen', ['Produktregel', 'Quotientenregel'], 1),
    ('kettenregel', 'Kettenregel', ['kettenregel'], 'rechnen', ['Kettenregel', 'verkettet'], 1),
    ('kostenfunktion', 'Kostenfunktion, Fixkosten, Grenzkosten', ['kostenfunktion'], 'rechnen', ['Fixkosten', 'Grenzkosten', 'Stückkosten', 'Kostenfunktion'], 1),
    ('gewinnzone', 'Gewinnschwelle, Gewinnzone', ['gewinnzone'], 'rechnen', ['Gewinnschwelle', 'Gewinnzone', 'Gewinngrenze'], 1),
    ('gewinnmaximum', 'Gewinnmaximum', ['gewinnmaximum'], 'rechnen', ['Gewinnmaximum', 'maximalen Gewinn'], 1),
    ('betriebsoptimum', 'Betriebsoptimum, Betriebsminimum', ['betriebsoptimum'], 'rechnen', ['Betriebsoptimum', 'Betriebsminimum', 'Preisuntergrenze'], 1),
    ('substitution', 'Integration durch Substitution', ['substitution'], 'rechnen', ['Substitution'], 1),
    ('partielle-integration', 'Partielle Integration', ['partielle-integration'], 'rechnen', ['partielle Integration', 'partiell integrieren'], 1),
    ('matrizen', 'Matrizen addieren, transponieren', ['matrizen'], 'rechnen', ['transponier', 'Matrix', 'Matrizen'], 1),
    ('matrizenmultiplikation', 'Matrizenmultiplikation', ['matrizenmultiplikation'], 'rechnen', ['Matrizenmultiplikation', 'multiplizier'], 1),
    ('mehrstufig', 'Mehrstufige Produktion', ['mehrstufige-produktion'], 'rechnen', ['Gozinto', 'mehrstufig', 'Verbrauchskoeffizient'], 1),
    ('determinante', 'Determinante, Lösbarkeit', ['determinante'], 'rechnen', ['Determinante', 'Sarrus'], 1),
    ('inverse', 'Inverse Matrix', ['inverse-matrix'], 'rechnen', ['Inverse'], 1),
    ('partielle-ableitung', 'Partielle Ableitungen', ['partielle-ableitung'], 'rechnen', ['partielle Ableitung', 'partiell'], 1),
    ('grenzprodukt', 'Grenzprodukte (Cobb-Douglas) interpretieren', ['grenzprodukt'], 'rechnen', ['Grenzprodukt', 'Cobb-Douglas'], 1),
],
'ikm': [
    ('space', 'Space: critical incident', ['hall-space'], 'erklaeren', ['space', 'personal space', 'territory'], 1),
    ('barbecue', 'Barbecue case', ['case-barbecue'], 'erklaeren', ['barbecue', 'Koji', 'Alan'], 1),
    ('china', 'Preparing a meeting in China', ['china-germany'], 'erklaeren', ['China', 'Chinese'], 1),
    ('ci-method', 'Analysing a critical incident', ['critical-incident-method'], 'erklaeren', ['critical incident', 'perspective', 'recommend'], 1),
    ('incidents', 'Cultural factor in critical incidents', ['gibson-incidents'], 'erklaeren', ['incident', 'flight', 'phones', 'retreat', 'reservation', 'congratulations', 'parts'], 1),
    ('bias', 'Match biases with statements', ['bias-types'], 'zuordnen', ['bias', 'halo', 'horns', 'groupthink', 'anchoring', 'similarity', 'confirmation', 'affective heuristic'], 1),
    ('role-play', 'Case: role play (Wagner, Smith, Ningchu)', ['role-play'], 'erklaeren', ['Wagner', 'Smith', 'Ningchu'], 1),
    ('battery', 'Case: battery factory', ['battery-factory'], 'erklaeren', ['battery', 'expat', 'locals', 'factory'], 1),
],
'igt': [
    ('phasentabelle', 'Phasentabelle: Merkmale der sechs Phasen', ['phasentabelle', 'phase13', 'phase4', 'phase56'], 'zuordnen', ['Phase', 'staatlicher Einfluss', 'Handelsgüter'], 1),
    ('integration', 'Integrationsstufen unterscheiden', ['integrationsstufen'], 'zuordnen', ['Zollunion', 'Freihandelszone', 'Gemeinsamer Markt'], 1),
    ('statik', 'Komparative Statik anwenden', ['statik'], 'erklaeren', ['Verschiebung', 'Preis steigt', 'komparative Statik'], 1),
    ('ricardo', 'Komparative Kostenvorteile rechnen', ['ricardobeispiele', 'ricardo'], 'rechnen', ['Opportunitätskosten', 'Ricardo'], 1),
    ('theorien', 'Theorie, Faktor und Leitfrage zuordnen', ['theorievergleich'], 'zuordnen', ['Leitfrage', 'Heckscher', 'Gravitation'], 1),
    ('eprg', 'EPRG-Orientierungen', ['eprg'], 'zuordnen', ['ethnozentrisch', 'polyzentrisch', 'geozentrisch'], 1),
    ('wertkette', 'Aktivitäten der Wertkette zuordnen', ['wertkette'], 'zuordnen', ['Wertkette', 'Eingangslogistik', 'Kundenservice'], 1),
    ('oli', 'OLI-Paradigma anwenden', ['oli'], 'erklaeren', ['OLI', 'Ownership', 'Lizenz'], 1),
    ('tak', 'Transaktionskostentheorie anwenden', ['tak'], 'erklaeren', ['Transaktionskosten', 'Spezifität'], 1),
    ('nutzwert', 'Nutzwertanalyse rechnen', ['nutzwert'], 'rechnen', ['Nutzwert', 'Gewicht'], 1),
    ('typen', 'Unternehmenstypen einordnen', ['typen'], 'zuordnen', ['transnational', 'multinational', 'global'], 1),
    ('matrix', 'Matrixstruktur', ['matrix'], 'erklaeren', ['Matrix'], 1),
    ('konflikte', 'Thomas-Kilmann-Konfliktstile', ['konflikte'], 'zuordnen', ['Competing', 'Collaborating', 'Avoiding'], 1),
],
}

for fid, punkte in P.items():
    ids = {t['id'] for k in json.loads((IN / fid / 'fach.json').read_text())['kapitel'] for t in k['themen']}
    for p in punkte:
        assert set(p[2]) <= ids, (fid, p)
    inv = dict(hinweis='intern, wird nie gebaut', wichtig_ab=1, punkte=[dict(id=i, text=t, t=ts, art=a, such=s, j=j) for i, t, ts, a, s, j in punkte])
    (IN / fid / 'plan').mkdir(exist_ok=True)
    (IN / fid / 'plan' / 'gp_inventar.json').write_text(json.dumps(inv, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(fid, len(punkte), 'Punkte,', sum(1 for p in punkte if p[5] >= 1), 'wichtig')
