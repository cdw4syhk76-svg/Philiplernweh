"""Zeichenaufgaben im Klausurstil: auf Papier skizzieren, dann Musterskizze (Bild aus vorhandener Frage) und Checkliste aufdecken.
Familien „:zn-…“ (rev, zeichnen: 1, klausur: True) → inhalte/<fach>/fragen_neu.json. Aufruf: python3 werkzeuge/zeichnen.py"""
import json, pathlib, html
IN = pathlib.Path(__file__).resolve().parents[1] / 'inhalte'
HINWEIS = '<small class="q-hilfe">Auf Papier zeichnen und erklären, dann die Lösung aufdecken und mit Musterskizze und Checkliste vergleichen.</small>'

# (Unterthema, Quelle (Familie, Index) für die Musterskizze, Aufgabe, Checkliste, Punkt)
LOGISTIK = [
 ('fertigungsarten', ('logistik:fertigungsarten:halle', 0), 'werkstatt', 'Zeichnen Sie die Werkstattfertigung als Hallenplan und erklären Sie sie detailliert.',
  ['gleichartige Maschinen in Werkstätten gruppiert (Dreherei, Fräserei, Bohrerei)', 'Weg des Werkstücks mit Pfeilen hin und her zwischen den Werkstätten',
   'Vorteil: flexibel, viele Varianten und kleine Lose', 'Nachteil: lange Wege, hohe Liege-, Rüst- und Durchlaufzeiten', 'Beispiel: Einzel- und Kleinserienfertigung (Möbel, Schmiede)']),
 ('fertigungsarten', ('logistik:fertigungsarten:halle', 0), 'insel', 'Zeichnen Sie eine Fertigungsinsel bzw. Fertigungszelle und erklären Sie sie detailliert.',
  ['verschiedene Maschinen (NC, CNC, DNC) eng um eine Teilefamilie angeordnet', 'das Teil wird in der Insel komplett bearbeitet, kurze Wege',
   'Gruppe arbeitet selbstständig, teils automatisiert (Zelle)', 'Vorteil: flexibel und schnell; Nachteil: Investition in Steuerungstechnik', 'Beispiel: Zahnräder, Motoren']),
 ('fertigungsarten', ('logistik:fertigungsarten:halle', 0), 'fliess', 'Zeichnen Sie die Serien- bzw. Fließfertigung und erklären Sie sie detailliert.',
  ['Maschinen in der Reihenfolge der Arbeitsgänge', 'Pfeil in eine Richtung, ohne Umwege', 'hohe Stückzahlen gleicher oder ähnlicher Teile',
   'Vorteil: geringe Rüstzeiten, schneller Durchlauf, hohe Auslastung', 'Nachteil: hohe Investition, wenig flexibel', 'Beispiel: Pkw, Montageband']),
 ('m-lagertypen', ('logistik:m-lagertypen:durchlauf', 0), 'durchlauf', 'Zeichnen Sie ein Durchlaufregallager und erklären Sie es detailliert.',
  ['Regal schräg, mehrere Kanäle übereinander mit Gefälle zur Entnahmeseite', 'links „Einlagerung“ mit Pfeil hinein', 'rechts „Entnahme“ mit Pfeil heraus',
   'Pfeil „FIFO“ unter dem Regal von links nach rechts', 'in jedem Kanal nur ein Artikel', 'Vorteile: FIFO zwangsläufig, gute Flächennutzung; Nachteile: störanfällig, teuer']),
 ('bullwhip', ('logistik:bullwhip:effekt', 0), 'bullwhip', 'Erklären Sie den Bullwhip-Effekt und stellen Sie ihn grafisch dar.',
  ['Stufen: Endkunde → Einzelhandel → Großhandel → Hersteller', 'Schwankung der Bestellmengen wird von Stufe zu Stufe größer', 'Endkunde schwankt kaum',
   'Ursachen: lokale Prognosen, Sicherheitsbestände je Stufe, Auftragsbündelung, Rabatte', 'Gegenmittel: POS-Daten teilen, VMI, Direktbelieferung']),
 ('aufloesung', ('logistik:aufloesung:umbau', 1), 'dispo', 'Übertragen Sie die Erzeugnisstruktur E1 (E1 → 2 G1, 1 G2, 5 T1; G1 → 2 G2, 3 T1; G2 → 2 T3, 3 T4) vom Fertigungsstufen- in das Dispositionsstufenverfahren.',
  ['jedes Teil steht auf der tiefsten Stufe, auf der es vorkommt', 'G2 und T1 werden nach unten gezogen', 'gleiche Teile stehen auf einer Ebene',
   'Mengen an den Pfeilen bleiben gleich', 'Vorteil: jedes Teil wird nur einmal disponiert']),
 ('lieferanten', ('logistik:lieferanten:pyramide', 0), 'pyramide', 'Stellen Sie die Lieferantenhierarchie grafisch dar und erklären Sie sie mit Beispielen.',
  ['Spitze: Hersteller (OEM)', '1st Tier: System- und Modullieferanten (Cockpit)', '2nd Tier: Komponentenlieferanten (Tachometer)',
   '3rd Tier: Rohmaterial- und Normteillieferanten (Schrauben)', 'nach unten: mehr Lieferanten, weniger Partnerschaft, leichter austauschbar']),
 ('auktionen', ('logistik:auktionen:reverse', 0), 'reverse', 'Nennen Sie die Arten von Auktionen und stellen Sie die Reverse Auction grafisch dar.',
  ['Achsen: Zeit (waagrecht) und Preis (senkrecht)', 'Startpreis des Einkäufers oben', 'Gebote der Lieferanten fallen treppenförmig',
   'Zuschlag an den günstigsten Bieter am Ende', 'Arten: englisch, holländisch, Höchstpreis, Vickrey, Reverse, Scorecard']),
]
ALLE = {'logistik': LOGISTIK}


def main():
    for fid, liste in ALLE.items():
        fach = json.loads((IN / fid / 'fach.json').read_text(encoding='utf-8'))
        kn = {t['id']: i for i, k in enumerate(fach['kapitel'], 1) for t in k['themen']}
        fr = json.loads((IN / fid / 'fragen.json').read_text(encoding='utf-8'))
        p = IN / fid / 'fragen_neu.json'; neu = json.loads(p.read_text(encoding='utf-8'))
        neu['familien'] = [x for x in neu['familien'] if ':zn-' not in x.get('id', '')]
        alle = {f.get('id'): f for f in fr['familien'] + neu['familien']}
        for tid, (qid, i), nid, aufgabe, check in liste:
            q = alle[qid]['a'][i]; bild = q.get('bild', '')
            leg = ''.join(f'<li>{html.escape(s)}</li>' for s in q.get('slots', []))
            l = (f'<b>Musterskizze</b><div class="q-bild">{bild}</div>' + (f'<ol class="zn-leg">{leg}</ol>' if leg else '') +
                 '<b>Checkliste</b><ul>' + ''.join(f'<li>{c}</li>' for c in check) + '</ul>')
            a = dict(y='rev', p=aufgabe + HINWEIS, l=l, pk=[c.split(':')[0].split(' (')[0][:40] for c in check], w='', klausur=True, zeichnen=1, lvl=3)
            neu['familien'].append(dict(id=f'{fid}:{tid}:zn-{nid}', f=fid, t=tid, k=kn[tid], s=True, y='fam', fam=1, z='Kann zeichnen und erklären', a=[a]))
        p.write_text(json.dumps(neu, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(fid, len(liste), 'Zeichenaufgaben')


if __name__ == '__main__':
    main()
