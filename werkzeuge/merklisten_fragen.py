"""Aus jeder Klausur-Merkliste der Lernseiten Fragen für alle Werkzeuge erzeugen.
  · Klausur (liste, rev, klausur:true)  → Arbeitsblatt, Klausurniveau, Endlos
  · Verknüpfen / Zuordnen / Reihenfolge  → Endlos, Arbeitsblatt Einfach
  · „Welcher Punkt ist gemeint?“, „Was gehört nicht dazu?“, Lückentext → Endlos, Drill
  · Karteikarten mit kr=1 (klausurrelevant)  → Definitionsdrill Methode 1 und 2
Schreibt Familien „:ml…“ nach inhalte/<fach>/fragen_neu.json und Karten (q='ml') nach karten.json. Wiederholbar.
Aufruf: python3 werkzeuge/merklisten_fragen.py"""
import sys, json, random, re, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from merklisten import listen, IN, txt

random.seed(11)
AUSSER = {'beispiel', 'zusammenspiel', 'einordnung', 'warum', 'prinzip', 'example'}

# je Liste: art (paare | saetze | gruppen | muster | reihe), thema (für „Nennen Sie n …“), kurz (Kartenvorderseite), n, gruppe (Geschwisterlisten)
K = {
    'logistik/material#0': dict(art='paare', thema='Materialarten (Betriebs- und Werkstoffe)', kurz='Materialart', n=8),
    'logistik/lagerkosten#0': dict(fremd=['logistik/losgroesse#0'], art='paare', thema='Bestandteile der Lagerhaltungskosten', kurz='Lagerhaltungskosten', n=6, gruppe='lhk'),
    'logistik/lagerkosten#1': dict(art='paare', thema='Möglichkeiten, die Lagerhaltungskosten zu senken', kurz='Lagerhaltungskosten senken', n=6, gruppe='lhk'),
    'logistik/abc#0': dict(fremd=['logistik/abc#1'], art='saetze', thema='Maßnahmen des A-Teile-Managements', label='A-Teile', n=6, gruppe='abc'),
    'logistik/abc#1': dict(fremd=['logistik/abc#0'], art='saetze', thema='Maßnahmen des C-Teile-Managements', label='C-Teile', n=6, gruppe='abc'),
    'logistik/mittelwert#0': dict(art='gruppen', thema='Abweichungen vom Mittelwert', frage='Warum weicht der tatsächliche Bedarf vom gewogen gleitenden Mittelwert ab, und wie erhält man aussagekräftigere Werte?', sep=', ', n=4,
                                  labels={'Ursachen': 'Gründe, warum der tatsächliche Bedarf vom Mittelwert abweicht', 'Maßnahmen': 'Maßnahmen für verlässlichere Prognosewerte'}),
    'logistik/bestellung#0': dict(art='saetze', thema='Folgen des Wareneingangs (im ERP-System)', n=4),
    'logistik/losgroesse#0': dict(fremd=['logistik/lagerkosten#0'], art='paare', thema='Bestandteile der Bestellkosten', kurz='Bestellkosten', n=6, gruppe='bk'),
    'logistik/losgroesse#1': dict(art='paare', thema='Wege, die Bestellkosten zu senken', kurz='Bestellkosten senken', n=6, gruppe='bk'),
    'logistik/pruefung#0': dict(art='paare', thema='Prüfmethoden bzw. Prüfverfahren', kurz='Prüfmethode', n=8),
    'logistik/qms#0': dict(art='saetze', thema='Anforderungen der IATF 16949 über ISO 9001 hinaus', label='IATF 16949', n=6, gruppe='qm'),
    'logistik/qms#1': dict(art='paare', thema='Hauptabschnitte der ISO 9001:2015', kurz='ISO 9001', n=6, reihe=True, gruppe='qm'),
    'logistik/umwelt#0': dict(art='paare', thema='Forderungen (Bestandteile) der ISO 14001', kurz='ISO 14001', n=6),
    'logistik/m-grundlagen#0': dict(art='paare', thema='Lösungsansätze für den Zielkonflikt zwischen Lager und Einkauf', kurz='Zielkonflikt Lager–Einkauf', n=5),
    'logistik/smartfactory#0': dict(art='paare', thema='Begriffe der Industrie 4.0', kurz='Industrie 4.0', n=5,
                                    frage='Erklären Sie detailliert Big Data, Embedded System, CPS, Smart Factory und Smart Product.'),
    'logistik/m-lagertypen#0': dict(art='muster', thema='Durchlaufregallager', frage='Zeichnen Sie ein Durchlaufregallager und erklären Sie es detailliert.'),
    'logistik/m-lagerkosten#0': dict(art='paare', thema='Möglichkeiten, die Lagerhaltungskosten zu senken', kurz='Lagerhaltungskosten senken', n=6),
    'logistik/kommission#0': dict(art='paare', thema='Kommissioniersysteme', kurz='Kommissioniersystem', n=8),
    'logistik/m-bestandscontrolling#0': dict(art='paare', thema='Möglichkeiten, überhöhte Bestände zu vermeiden', kurz='Überhöhte Bestände', n=7),
    'logistik/m-wws#0': dict(art='paare', thema='Aufgaben eines Warenwirtschaftssystems', kurz='Warenwirtschaftssystem', n=8),
    'logistik/m-ecr#0': dict(art='paare', thema='Merkmale des Vendor Managed Inventory (VMI)', kurz='VMI', n=7),
    'logistik/m-ersatzteile#0': dict(art='paare', thema='Gründe für eine optimale Ersatzteilversorgung', kurz='Ersatzteilversorgung', n=7),
    'logistik/maverick#0': dict(fremd=['logistik/maverick#1'], art='saetze', thema='Ursachen für Maverick Buying', label='Ursache', n=6, gruppe='mav'),
    'logistik/maverick#1': dict(fremd=['logistik/maverick#0'], art='saetze', thema='Gegenmaßnahmen gegen Maverick Buying', label='Gegenmaßnahme', n=6, gruppe='mav'),
    'logistik/m-nichttrad#0': dict(art='paare', thema='Möglichkeiten, Reisekosten zu senken', kurz='Reisekosten', n=7),
    'logistik/bullwhip#0': dict(art='gruppen', thema='Bullwhip-Effekt', frage='Erklären Sie den Bullwhip-Effekt mit je 4 Ursachen, Folgen und Gegenmaßnahmen.', sep=' · ', n=4,
                                labels={'Ursachen': 'Ursachen des Bullwhip-Effekts', 'Folgen': 'Folgen des Bullwhip-Effekts', 'Gegenmittel': 'Gegenmaßnahmen gegen den Bullwhip-Effekt'}),
    'marketing/begriff#0': dict(art='muster', thema='Definitionen von Marketing', frage='Nennen und erläutern Sie verschiedene Definitionen von Marketing.'),
    'marketing/gratifikation#0': dict(art='muster', thema='Gratifikationsprinzip', frage='Erklären Sie das Gratifikationsprinzip mit einem Beispiel.'),
    'marketing/einsatz#0': dict(fremd=['marketing/aspekte#0'], art='paare', thema='Bereiche des Marketing neben dem Absatz (je mit Beispiel)', kurz='Marketingbereich', n=6),
    'marketing/aspekte#0': dict(fremd=['marketing/einsatz#0'], art='paare', thema='Aspekte des Marketing', kurz='Marketing-Aspekt', n=8),
    'marketing/preis#0': dict(art='paare', thema='Eckpunkte des preispolitischen Dreiecks (3 K)', kurz='Preispolitisches Dreieck', n=3,
                              frage='Erklären Sie das preispolitische Dreieck.'),
    'marketing/vertrieb#0': dict(art='muster', thema='direkter und indirekter Vertrieb', frage='Erklären Sie direkten und indirekten Vertrieb mit Vor- und Nachteilen.'),
    'marketing/maslow#0': dict(art='muster', thema='Bedürfnispyramide nach Maslow', frage='Erklären Sie die Bedürfnispyramide nach Maslow und ihre Bedeutung für das Marketing.'),
    'marketing/aufgaben#0': dict(art='paare', thema='Aufgabendimensionen des Marketing', kurz='Aufgabendimension', n=3),
    'produktion/op-views#0': dict(art='gruppen', thema='the 12 questions of operations strategy', frage='Explain the 12 questions of operations strategy (resources, processes, competencies).', sep=' · ', n=4, en=True,
                                  labels={'Resources': 'Resources', 'Processes': 'Processes', 'Competencies': 'Competencies'}),
    'produktion/op-analysis#0': dict(art='reihe', thema='how to answer a Five Forces question', en=True),
    'produktion/op-lean#0': dict(fremd=['produktion/sv-intro#0'], art='saetze', thema='the 7 wastes (Lean)', n=7, en=True),
    'produktion/sv-intro#0': dict(fremd=['produktion/op-lean#0', 'produktion/sv-operations#0'], art='saetze', thema='characteristics of services', n=4, en=True),
    'produktion/sv-operations#0': dict(fremd=['produktion/sv-intro#0'], art='saetze', thema='e-process criteria', n=5, en=True),
    'produktion/ds-ep#0': dict(fremd=['produktion/ds-svc#0'], art='saetze', thema='groups of the evaluation profile', n=6, en=True, reihe=True),
    'produktion/ds-svc#0': dict(fremd=['produktion/ds-ep#0'], art='saetze', thema='activities of the service life cycle', n=10, en=True, reihe=True),
    # Kurs WIN26B
    'mawi/zieldreieck#0': dict(art='saetze', thema='Bestandteile der 7R nach Plowman', n=7),
    'mawi/zieldreieck#1': dict(art='saetze', thema='Bestandteile der 6R nach Jünemann', n=6),
    'mawi/mgm-definition#0': dict(art='saetze', thema='Merkmale des Materialgruppenmanagements', n=4),
    'mawi/beschaffungsmarkt-macht#0': dict(art='saetze', thema='Merkmale hoher Marktmacht des Kunden', n=5),
    'mawi/kraljic#0': dict(art='paare', thema='Normstrategien nach Machtposition', kurz='Normstrategie', n=3),
    'bwl/dienstleistung#0': dict(art='paare', thema='Merkmale von Dienstleistungen', kurz='Dienstleistungsmerkmal', n=5),
    'bwl/gewinnmax#0': dict(art='reihe', thema='Schritte zum Gewinnmaximum'),
    'bwl/swot#0': dict(art='reihe', thema='Vorgehen der Ressourcen- und SWOT-Analyse'),
    'mkt/marktakteure#0': dict(art='paare', thema='Absatzmittler nach Name und Rechnung', kurz='Absatzmittler', n=3),
    'ikm/nonverbal#0': dict(art='paare', thema='categories of non-verbal communication', kurz='Non-verbal category', n=6, en=True),
    'ikm/bias-types#0': dict(art='paare', thema='types of bias', kurz='Bias', n=7, en=True),
}


def norm(s): return re.sub(r'[^a-zäöüß0-9]', '', s.lower())


def kurzform(s, n=42):
    """kurze Antwort für Auswahl: ohne Klammern, erster Satzteil"""
    s = re.sub(r'\s*\([^)]*\)', '', s).strip()
    return re.split(r',\s|:\s|;\s', s)[0].strip()


def erkl(s, n=80):
    """Erklärung kurz, aber vollständig: ohne Klammern, bis zum letzten Komma vor n Zeichen"""
    s = re.sub(r'\s*\([^)]*\)', '', s).split('; ')[0].strip()
    while len(s) > n and ', ' in s: s = s.rsplit(', ', 1)[0]
    return s


def ohne(expl, name):
    for w in {name, kurzform(name)} | set(re.split(r'\s*/\s*|\s+und\s+|,\s*', name)):
        w = w.strip()
        if len(w) > 3: expl = re.sub(re.escape(w), '…', expl, flags=re.I)
    return expl


def schluessel(s):
    """Suchwörter für das Prüfen einer Aufzählung: ganzer Punkt + markante Wörter"""
    k = [s, kurzform(s)]
    k += [w for w in re.findall(r'[A-ZÄÖÜ][\wäöüß-]{5,}|[\wäöüß-]{12,}', s)][:3]
    return list(dict.fromkeys(x for x in k if x))


def familien(fid, alle, vorhandene_listen):
    en = fid in ('produktion', 'ikm')
    T = (lambda de, e: e) if en else (lambda de, e: de)
    out, karten = [], []
    andere = [L for L in alle if K.get(f"{L['fid']}/{L['tid']}#{L['nr']}")]
    for L in alle:
        key = f"{fid}/{L['tid']}#{L['nr']}"; c = K.get(key)
        if not c: continue
        pk = [(a, b) for a, b in L['punkte']]
        if c['art'] == 'paare':
            pk = [tuple(x.strip() for x in re.split(r'\s+[:–]\s+', a, maxsplit=1)) if not b and re.search(r'\s[:–]\s', a) else (a, b) for a, b in pk]
        if c['art'] == 'paare' and any(len(a) == 1 for a, _ in pk):   # „A · marktbezogen: … · Erklärung“
            pk = [(b.split(' · ')[0], ' · '.join(b.split(' · ')[1:])) if len(a) == 1 else (a, b) for a, b in pk]
        echte = [(a, b) for a, b in pk if norm(a.split(' ')[0].split('(')[0]) not in AUSSER]
        thema, n = c['thema'], min(c.get('n', len(echte)), len(echte))
        basis = dict(f=fid, t=L['tid'], k=L['kn'], s=True, y='fam', fam=1)
        fk, fu, fq = [], [], []          # Klausur · Zuordnen/Reihenfolge · schnelle Fragen
        loes = '<ol>' + ''.join(f'<li><b>{a}</b>{": " + b if b else ""}</li>' for a, b in pk) + '</ol>'
        geschw = [M for M in andere if M is not L and M['fid'] == fid and c.get('gruppe') and K[f"{fid}/{M['tid']}#{M['nr']}"].get('gruppe') == c['gruppe']]

        if c['art'] in ('paare', 'saetze'):
            namen = [a for a, _ in echte]
            schon = vorhandene_listen.get(L['tid'], [])
            doppelt = any(len({norm(kurzform(x)) for x in namen} & s) >= len(namen) / 2 for s in schon)
            if not doppelt:
                fk.append(dict(y='liste', p=c.get('frage_liste') or T(f'Nennen Sie {n} {thema}.', f'Name {n} {thema}.'),
                               pk=[schluessel(a) for a in namen], n=n, w='', klausur=True, lvl=3))
            fk.append(dict(y='rev', p=c.get('frage') or T(f'Nennen und erklären Sie detailliert {n} {thema}.', f'Name and explain {n} {thema}.'),
                           l=loes, pk=([f'{kurzform(a)}: {erkl(b, 45)}' for a, b in echte if b] if c['art'] == 'paare' else [kurzform(a) for a in namen])[:8], w='', klausur=True, lvl=3))
            if c['art'] == 'paare':
                pa = [(kurzform(a), ohne(erkl(b), a)) for a, b in echte if b]
                random.shuffle(pa)
                for g in range(0, min(len(pa), 8), 4):
                    teil = pa[g:g + 4]
                    if len(teil) >= 3:
                        fu.append(dict(y='zuord', p=T(f'{thema}: Verknüpfe jeden Punkt mit seiner Erklärung.', f'{thema}: match each point with its explanation.'),
                                       k=[a for a, _ in teil], e=[[d, j] for j, (_, d) in enumerate(teil)], w='', lvl=1))
                for a, b in random.sample(pa, min(3, len(pa))):
                    opts = [a] + random.sample([x for x, _ in pa if x != a], min(3, len(pa) - 1))
                    if len(opts) == 4:
                        fq.append(dict(y='mc', p=T(f'{thema}: Welcher Punkt ist gemeint?<br>„{b}“', f'{thema}: which point is meant?<br>“{b}”'),
                                       o=[[o, o == a] for o in random.sample(opts, 4)], w=f'{a}: {b}', lvl=1))
                for a, b in [x for x in echte if x[1] and len(kurzform(x[0]).split()) <= 3][:2]:
                    fq.append(dict(y='luecke', p=T(f'{thema}: <b>[[0]]</b> · {ohne(b, a)}', f'{thema}: <b>[[0]]</b> · {ohne(b, a)}'),
                                   l=[[kurzform(a), kurzform(a).lower()]], w=f'{a}: {b}', lvl=2))
            # „Was gehört nicht dazu?“: Eindringling aus der Geschwisterliste, sonst aus einer anderen Liste des Fachs
            quelle = [M for M in andere if f"{M['fid']}/{M['tid']}#{M['nr']}" in c.get('fremd', ())]
            woerter = {w.lower()[:6] for x in namen for w in re.findall(r'[\wäöüß]{5,}', x)}
            for _ in range(2 if len(namen) >= 3 and quelle else 0):
                M = random.choice(quelle); fremd = [kurzform(a) for a, _ in M['punkte'] if norm(a.split(' ')[0]) not in AUSSER and not woerter & {w.lower()[:6] for w in re.findall(r'[\wäöüß]{5,}', a)}]
                if not fremd: continue
                e = random.choice(fremd); drei = random.sample([kurzform(x) for x in namen], 3)
                fq.append(dict(y='mc', p=T(f'{thema}: Was gehört <b>nicht</b> dazu?', f'{thema}: which one does <b>not</b> belong?'),
                               o=[[o, o == e] for o in random.sample(drei + [e], 4)], w=T(f'„{e}“ gehört zu: {M["titel"]}', f'“{e}” belongs to: {M["titel"]}'), lvl=1))
            # Zwei Geschwisterlisten (A/C-Teile, Ursachen/Gegenmaßnahmen): Punkte der richtigen Liste zuordnen
            if c['art'] == 'saetze' and geschw and K[f"{fid}/{geschw[0]['tid']}#{geschw[0]['nr']}"].get('label') and L['nr'] == min(M['nr'] for M in geschw + [L]):
                M = geschw[0]; cm = K[f"{fid}/{M['tid']}#{M['nr']}"]
                for _ in range(2):
                    a = random.sample([kurzform(x, 50) for x, _ in L['punkte']], 2); b = random.sample([kurzform(x, 50) for x, _ in M['punkte']], 2)
                    e = [[x, 0] for x in a] + [[x, 1] for x in b]; random.shuffle(e)
                    fu.append(dict(y='zuord', p=T(f'Wohin gehört der Punkt: {c["label"]} oder {cm["label"]}?', f'Where does it belong?'), k=[c['label'], cm['label']], e=e, w='', lvl=1))
            if c.get('reihe') and 3 <= len(namen) <= 10:
                fu.append(dict(y='reihe', p=T(f'Bringe die {thema} in die richtige Reihenfolge.', f'Put the {thema} in the right order.'),
                               o=[re.sub(r'\s*\(.*?\)', '', kurzform(x, 40)) for x in namen], w='', lvl=2))
            if c['art'] == 'paare':
                kurz = c.get('kurz') or thema
                for a, b in echte:
                    if b: karten.append(dict(t=L['tid'], v=f'{kurz}: {a}', r=b, b=1, kr=1, q='ml'))
            karten.append(dict(t=L['tid'], v=T(f'{n} {thema}', f'{n} {thema}'), r=' · '.join(a for a, _ in echte), kr=1, q='ml'))

        elif c['art'] == 'gruppen':
            gr = []
            for a, b in pk:
                if not b and ':' in a: a, b = a.split(':', 1)
                gr.append((a.strip(), [x.strip(' ·') for x in re.split(re.escape(c['sep']), b) if x.strip(' ·')]))
            for a, items in gr:
                lab = c['labels'].get(a, a)
                m = min(c['n'], len(items))
                fk.append(dict(y='liste', p=T(f'Nennen Sie {m} {lab}.', f'{lab}: name {m} of the questions.'), pk=[schluessel(x) for x in items], n=m, w='', klausur=True, lvl=3))
                karten.append(dict(t=L['tid'], v=T(f'{thema}: {a}', f'{thema}: {a}'), r=' · '.join(items), kr=1, q='ml'))
            for _ in range(2):
                e = []
                for j, (a, items) in enumerate(gr): e += [[x, j] for x in random.sample(items, min(2, len(items)))]
                random.shuffle(e)
                fu.append(dict(y='zuord', p=T(f'{thema}: Wohin gehört der Punkt?', f'{thema}: where does each item belong?'), k=[a for a, _ in gr], e=e[:8], w='', lvl=1))
            fk.append(dict(y='rev', p=c.get('frage') or T(f'Erklären Sie {thema}: ' + ', '.join(a for a, _ in gr) + '.', f'Explain {thema}.'),
                           l=loes, pk=[a for a, _ in gr], w='', klausur=True, lvl=3))

        elif c['art'] == 'muster':
            fk.append(dict(y='rev', p=c['frage'], l=loes, pk=[kurzform(a) for a, _ in pk][:6], w='', klausur=True, lvl=3))
            pa = [(kurzform(a), ohne(erkl(b), a)) for a, b in echte if b]
            if len(pa) >= 3:
                teil = random.sample(pa, min(4, len(pa)))
                fu.append(dict(y='zuord', p=T(f'{thema}: Was gehört zu welchem Baustein der Antwort?', ''), k=[a for a, _ in teil], e=[[d, j] for j, (_, d) in enumerate(teil)], w='', lvl=1))
            for a, b in echte:
                if b: karten.append(dict(t=L['tid'], v=f'{thema}: {a}', r=b, b=1, kr=1, q='ml'))

        elif c['art'] == 'reihe':
            st = [kurzform(a, 60) for a, _ in pk]
            fu.append(dict(y='reihe', p=T(f'{thema}: Bringe die Schritte in die richtige Reihenfolge.', f'{thema}: put the steps in the right order.'), o=st, w='', lvl=2))
            fk.append(dict(y='rev', p=T(f'{thema}', f'Explain {thema}.'), l=loes, pk=st, w='', klausur=True, lvl=3))

        z = T(f'Kann {thema} nennen und erklären', f'Can name and explain {thema}')
        for suf, a in (('k', fk), ('z', fu), ('q', fq)):
            if a: out.append(dict(id=f"{fid}:{L['tid']}:ml{L['nr']}{suf}", z=z, a=a, **basis))
    return out, karten


def main():
    for fid in ([a for a in sys.argv[1:] if not a.startswith('-') and not a.endswith('.json')] or ['bwl', 'mkt', 'wima', 'mawi', 'ikm', 'igt']):
        alle = listen(fid)
        fr = json.loads((IN / fid / 'fragen.json').read_text(encoding='utf-8'))
        fams = fr['familien'] if isinstance(fr, dict) else fr
        p = IN / fid / 'fragen_neu.json'
        neu = json.loads(p.read_text(encoding='utf-8'))
        vorh = {}
        for f in fams + [x for x in neu['familien'] if ':ml' not in x.get('id', '')]:
            for a in f['a']:
                if a['y'] == 'liste' and a.get('klausur'):
                    vorh.setdefault(f['t'], []).append({norm(kurzform(g[0])) for g in a['pk']})
        out, karten = familien(fid, alle, vorh)
        neu['familien'] = [x for x in neu['familien'] if ':ml' not in x.get('id', '')] + out
        p.write_text(json.dumps(neu, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        pk = IN / fid / 'karten.json'
        kd = json.loads(pk.read_text(encoding='utf-8'))
        kd['karten'] = [x for x in kd['karten'] if x.get('q') != 'ml']
        da = {txt(x['v']) for x in kd['karten']}
        for x in karten:
            if txt(x['v']) not in da: kd['karten'].append(x); da.add(txt(x['v']))
        pk.write_text(json.dumps(kd, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(fid, len(out), 'Familien', sum(len(f['a']) for f in out), 'Fragen', len(karten), 'Karten')


if __name__ == '__main__':
    main()
