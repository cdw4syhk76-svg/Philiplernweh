"""Zeichenaufgaben im Klausurstil: auf Papier skizzieren, dann Musterskizze (Bild aus vorhandener Frage) und Checkliste aufdecken.
Familien „:zn-…“ (rev, zeichnen: 1, klausur: True) → inhalte/<fach>/fragen_neu.json. Aufruf: python3 werkzeuge/zeichnen.py [fach …]"""
import json, pathlib, html, sys
IN = pathlib.Path(__file__).resolve().parents[1] / 'inhalte'
HINWEIS = '<small class="q-hilfe">Auf Papier zeichnen und erklären, dann die Lösung aufdecken und mit Musterskizze und Checkliste vergleichen.</small>'
HINWEIS_EN = '<small class="q-hilfe">Draw and explain on paper, then reveal the solution and compare with the sample sketch and checklist.</small>'

# (Unterthema, Quelle (Familie, Index) für die Musterskizze, Kürzel, Aufgabe, Checkliste)
ALLE = {
'mawi': [
 ('bestellbegriffe', ('mawi:bestellbegriffe:grund', 0), 'verlauf', 'Zeichnen Sie den Lagerbestandsverlauf beim Bestellpunktverfahren und tragen Sie Meldebestand, Sicherheitsbestand und Wiederbeschaffungszeit ein.',
  ['Achsen: Zeit (waagrecht), Bestand (senkrecht)', 'Sägezahn: Bestand sinkt gleichmäßig, steigt bei Lieferung senkrecht', 'Meldebestand als waagrechte Linie: dort wird bestellt',
   'Wiederbeschaffungszeit zwischen Bestellung und Lieferung', 'Sicherheitsbestand als unterste Linie, wird normalerweise nicht unterschritten']),
 ('bestellsysteme', ('mawi:bestellbegriffe:grund', 0), 'rhythmus', 'Skizzieren Sie den Lagerbestandsverlauf beim Bestellrhythmusverfahren (t,S) und grenzen Sie es vom Bestellpunktverfahren ab.',
  ['feste Bestellzeitpunkte in gleichen Abständen', 'Bestellmenge = Auffüllen bis zum Sollbestand S, daher schwankend', 'Bestand wird nur zum Bestelltermin geprüft',
   'Bestellpunktverfahren: Zeitpunkt variabel, ausgelöst beim Meldebestand', 'Rhythmus eignet sich für gleichmäßigen Bedarf, Bündelung möglich']),
 ('losgroessen-dilemma', ('mawi:losgroessen-dilemma:grund', 3), 'kosten', 'Stellen Sie das Dilemma der optimalen Bestellmenge grafisch dar und erklären Sie es.',
  ['Achsen: Bestellmenge x (waagrecht), Kosten (senkrecht)', 'Lagerkosten steigen linear mit x', 'Bestellkosten fallen hyperbelförmig',
   'Gesamtkosten als Summe, U-förmig', 'Minimum beim Schnittpunkt von Lager- und Bestellkosten = x_opt']),
 ('kraljic', ('mawi:kraljic:grund', 0), 'kraljic', 'Zeichnen Sie das Sourcing-Strategie-Portfolio nach Kraljic und nennen Sie die Normstrategien.',
  ['Achsen: Ergebniseinfluss und Beschaffungskomplexität', 'Hebelteile: Marktmacht nutzen', 'strategische Teile: Zusammenarbeit, Partnerschaft',
   'Engpassteile: Versorgung sichern, Engpass beseitigen', 'unkritische Teile: Prozesse vereinfachen, bündeln']),
 ('xyz-analyse', ('mawi:xyz-analyse:grund', 3), 'abcxyz', 'Stellen Sie die ABC-XYZ-Matrix dar und ordnen Sie Bereitstellungsstrategien zu.',
  ['Zeilen A, B, C (Wert), Spalten X, Y, Z (Vorhersagbarkeit)', 'AX: Just-in-Time', 'AZ, BZ: Einzelbeschaffung bei Bedarf', 'CX, CY: Vorratshaltung, einfache Verfahren',
   'Neun Felder, Aufwand dort, wo Wert hoch und Bedarf planbar']),
],
'bwl': [
 ('breakeven', ('bwl:breakeven:deuten', 0), 'be', 'Stellen Sie den Break-even-Punkt grafisch dar und erklären Sie Gewinn- und Verlustzone.',
  ['Achsen: Menge x, Euro', 'Erlösgerade durch den Ursprung', 'Kostengerade beginnt bei den Fixkosten', 'Schnittpunkt = Break-even-Menge', 'links Verlust-, rechts Gewinnzone']),
 ('five-forces', ('bwl:five-forces:ff', 0), 'ff', 'Stellen Sie Porters Five Forces grafisch dar und erklären Sie jede Kraft kurz.',
  ['Mitte: Rivalität der Wettbewerber', 'oben: Bedrohung durch neue Anbieter', 'unten: Bedrohung durch Ersatzprodukte', 'links: Verhandlungsmacht der Lieferanten', 'rechts: Verhandlungsmacht der Abnehmer']),
 ('bcg-matrix', ('bwl:bcg-matrix:bcg', 0), 'bcg', 'Zeichnen Sie die BCG-Matrix und erklären Sie die vier Felder mit Normstrategie.',
  ['Achsen: relativer Marktanteil und Marktwachstum', 'Question Marks: selektieren', 'Stars: investieren', 'Cash Cows: abschöpfen', 'Poor Dogs: desinvestieren']),
],
'mkt': [
 ('zufriedenheit', ('mkt:zufriedenheit:grund', 4), 'cd', 'Stellen Sie das C/D-Paradigma grafisch dar und erklären Sie es.',
  ['Erwartung (Soll) und wahrgenommene Leistung (Ist) werden verglichen', 'Ist = Soll: Bestätigung, Zufriedenheit', 'Ist > Soll: positive Diskonfirmation, hohe Zufriedenheit',
   'Ist < Soll: negative Diskonfirmation, Unzufriedenheit']),
 ('kano', ('mkt:kano:grund', 4), 'kano', 'Zeichnen Sie das Kano-Modell und erklären Sie die drei Faktoren mit Beispielen.',
  ['Achsen: Erfüllungsgrad (waagrecht), Zufriedenheit (senkrecht)', 'Basisfaktoren: Kurve unten, Fehlen macht unzufrieden', 'Leistungsfaktoren: Gerade, je mehr desto zufriedener',
   'Begeisterungsfaktoren: Kurve oben, Fehlen stört nicht', 'Beispiele, z. B. Bremsen, Verbrauch, Massagesitz']),
 ('marktumwelten', ('mkt:marktumwelten:grund', 6), 'umwelt', 'Stellen Sie den Markt mit seinen Umwelten grafisch dar.',
  ['Markt in der Mitte', 'fünf Umwelten außen herum: natürlich, technologisch, gesellschaftlich, ökonomisch, rechtlich-politisch', 'je ein Beispiel (Klima, Kommunikation, Werte, Konjunktur, Gesetze)', 'Pfeile: Umwelten wirken auf den Markt']),
],
'ikm': [
 ('iceberg', ('ikm:iceberg:eis', 0), 'eis', 'Draw the iceberg model of culture and give two examples for each part.',
  ['water line separating visible and invisible part', 'visible: small tip (architecture, language, rituals)', 'invisible: large part below (values, norms, attitudes)', 'the invisible part explains the visible behaviour']),
 ('comm-model', ('ikm:comm-model:mod', 0), 'modell', 'Draw the communication model and explain noise and the cultural filter.',
  ['sender encodes', 'message via channel', 'receiver decodes', 'noise: context, values, expectations, norms', 'cultural filter of the receiver, feedback']),
],
}


def main():
    for fid in (sys.argv[1:] or list(ALLE)):
        liste = ALLE.get(fid, [])
        en = fid == 'ikm'
        fach = json.loads((IN / fid / 'fach.json').read_text(encoding='utf-8'))
        kn = {t['id']: i for i, k in enumerate(fach['kapitel'], 1) for t in k['themen']}
        fr = json.loads((IN / fid / 'fragen.json').read_text(encoding='utf-8'))
        p = IN / fid / 'fragen_neu.json'; neu = json.loads(p.read_text(encoding='utf-8'))
        neu['familien'] = [x for x in neu['familien'] if ':zn-' not in x.get('id', '')]
        alle = {f.get('id'): f for f in fr['familien'] + neu['familien']}
        for tid, (qid, i), nid, aufgabe, check in liste:
            q = alle[qid]['a'][i]; bild = q.get('bild', '')
            leg = ''.join(f'<li>{html.escape(s)}</li>' for s in q.get('slots', []))
            l = (f'<b>{"Sample sketch" if en else "Musterskizze"}</b><div class="q-bild">{bild}</div>' + (f'<ol class="zn-leg">{leg}</ol>' if leg else '') +
                 f'<b>{"Checklist" if en else "Checkliste"}</b><ul>' + ''.join(f'<li>{c}</li>' for c in check) + '</ul>')
            a = dict(y='rev', p=aufgabe + (HINWEIS_EN if en else HINWEIS), l=l, pk=[c.split(':')[0].split(' (')[0][:40] for c in check], w='', klausur=True, zeichnen=1, lvl=3)
            neu['familien'].append(dict(id=f'{fid}:{tid}:zn-{nid}', f=fid, t=tid, k=kn[tid], s=True, y='fam', fam=1, z='Can draw and explain' if en else 'Kann zeichnen und erklären', a=[a]))
        p.write_text(json.dumps(neu, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(fid, len(liste), 'Zeichenaufgaben')


if __name__ == '__main__':
    main()
