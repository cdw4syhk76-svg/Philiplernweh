"""Erzeugt inhalte/mawi/klausur.json: Probeklausur Grundlagen der Materialwirtschaft (MaWi-Teil, 60 Punkte, 60 Minuten)
im Aufbau des Protokolls: 1 Multiple Choice · 2 optimale Bestellmenge · 3 Bestellverfahren (Abbildung) · 4 Brutto- zum Nettobedarf.
Zahlen werden hier gerechnet. Aufruf: python3 werkzeuge/mawi/klausur.py"""
import json, math, pathlib, random
ROOT = pathlib.Path(__file__).resolve().parents[2]
IN = ROOT / 'inhalte' / 'mawi'
rnd = random.Random(26)


def de(x, n=2):
    s = f'{x:,.{n}f}'.replace(',', '#').replace('.', ',').replace('#', '.')
    return s[:-3] if n == 2 and s.endswith(',00') else s


def Z(label, wert, p, einheit='', tol=None):
    d = dict(typ='zahl', label=label, loesung=round(float(wert), 4), p=p)
    if einheit: d['einheit'] = einheit
    if tol is not None: d['tol'] = tol
    return d
def T(label, p, z=4): return dict(typ='text', label=label, p=p, zeilen=z)
def V(id, unter, text, felder, loesung, vorrang=False, bild=None):
    r = dict(id=id, unter=unter, text=text, felder=felder, loesung=loesung)
    if vorrang: r['vorrang'] = True
    if bild: r['bild'] = bild
    return r


# ---------------------------------------------------------------- A1 Multiple Choice (20 P = 10 × 2 P)
fam = json.loads((IN / 'fragen.json').read_text())['familien']
mcs = {}
for f in fam:
    if ':fa-' in f['id']: continue   # Folienabgleich-Ergänzungen: nicht im Probeklausur-Bogen (Varianten-IDs bleiben stabil)
    for a in f['a']:
        if a['y'] == 'mc' and len(a['o']) == 4 and sum(1 for o in a['o'] if o[1]) == 1:
            mcs.setdefault(f['t'], []).append(a)
GRUPPEN = [['begriffe', 'zieldreieck', 'zielkonflikte', 'bedeutungswandel'], ['materialkosten-roi', 'lagerkosten', 'materialarten'], ['bedarfsarten', 'methoden', 'stuecklisten'],
           ['mittelwerte', 'exp-glaettung', 'bestaende-lager', 'lagerkennzahlen'], ['mgm-definition', 'mgm-nutzen', 'zentral-dezentral', 'materialgruppen-bilden', 'klassifikation'],
           ['business-requirements', 'beschaffungsmarkt-macht', 'datenbeschaffung', 'vier-phasen'], ['abc-analyse', 'xyz-analyse'], ['kraljic', 'kraljic-dynamik', 'marktmacht-portfolio', 'risiko-portfolio', 'portfolio-grundlagen'],
           ['early-involvement', 'buendelung-rfx', 'rahmenvertrag', 'vertragsrecht'], ['tco', 'incoterms', 'ksa', 'lpp', 'swot-scoring', 'einkaufsziele']]
teile1, pos_alle = [], []
for gi, g in enumerate(GRUPPEN):
    kand = [(t, a) for t in g for a in mcs.get(t, [])]
    kand.sort(key=lambda x: (not x[1].get('klausur'), (x[1].get('lvl') or 1) == 1))
    vs, gesehen = [], set()
    for t, a in kand:
        if a['p'] in gesehen: continue
        gesehen.add(a['p'])
        falsch = [x for x in a['o'] if not x[1]]; rnd.shuffle(falsch)
        r = len(pos_alle) % 4; o = falsch[:r] + [next(x for x in a['o'] if x[1])] + falsch[r:]; pos_alle.append(r)
        vs.append(V(f'1-{gi + 1}-{len(vs)}', t, a['p'], [dict(typ='sc', o=[x[0] for x in o], r=r, p=2)], f'<b>{"abcd"[r]}) {o[r][0]}</b>' + (f'<br>{a["w"]}' if a.get('w') else '')))
        if len(vs) == 7: break
    assert len(vs) >= 3, (g, len(vs))
    teile1.append(dict(punkte=2, varianten=vs))
pos = [v['felder'][0]['r'] for T_ in teile1 for v in T_['varianten']]
A1 = dict(titel='Multiple Choice', punkte=20, intro='Je Frage ist genau eine Antwort richtig.', teile=teile1)

# ---------------------------------------------------------------- A2 Optimale Bestellmenge (14 P)
a2 = []
for i, (ware, m, kb, w, il, einheit, ganz) in enumerate([('Weißzucker', 12, 150, 600, 15, 't', 'nur ganze Tonnen'), ('Aluminiumrohre', 24, 200, 1500, 12, 't', 'nur ganze Tonnen'),
                                                          ('Akkus', 7200, 120, 250, 12, 'Stück', 'nur volle Kartons zu 40 Stück'), ('Granulat', 50, 90, 400, 20, 't', 'nur ganze Tonnen'),
                                                          ('Speichen', 180000, 60, 0.4, 15, 'Stück', 'nur volle Kartons zu 1.000 Stück')]):
    x = math.sqrt(2 * m * kb / (w * il / 100)); K = lambda q: m / q * kb + q / 2 * w * il / 100
    schritt = 40 if ware == 'Akkus' else (1000 if ware == 'Speichen' else 1)
    lo = math.floor(x / schritt) * schritt; hi = lo + schritt; best = lo if K(lo) <= K(hi) else hi
    h = m / best
    a2.append(V(f'2-andler{i}', 'andler',
        f'Ein Unternehmen hat einen Jahresbedarf von <b>{de(m, 0)} {einheit}</b> {ware}. Der Preis beträgt <b>{de(w)} € je {"t" if einheit == "t" else "Stück"}</b>, jede Bestellung verursacht Kosten von <b>{de(kb, 0)} €</b>, der Lagerhaltungskostensatz beträgt <b>{il} %</b>. Bestellt werden kann {ganz}.<br>'
        f'a) Berechnen Sie die optimale Bestellmenge nach Andler (ohne Rundung).<br>b) Welche Bestellmenge wählen Sie unter der Liefereinschränkung? Begründen Sie mit den Gesamtkosten.<br>c) Wie oft wird im Jahr bestellt?<br>d) Nennen Sie zwei Modellannahmen und eine Schwäche in der Praxis.',
        [Z('a) x_opt', x, 5, einheit, tol=max(0.02, x * 0.003)), Z('b) gewählte Menge', best, 3, einheit), Z('c) Bestellhäufigkeit', h, 2, '-mal', tol=0.05), T('b) Begründung und d) Annahmen', 4, 5)],
        rf'a) \(x_{{opt}} = \sqrt{{\frac{{2 \cdot {de(m, 0)} \cdot {de(kb, 0)}}}{{{de(w)} \cdot {de(il / 100)}}}}} \approx {de(x)}\) {einheit} (5 P). '
        f'b) K({de(lo, 0)}) = {de(K(lo))} €, K({de(hi, 0)}) = {de(K(hi))} € → <b>{de(best, 0)} {einheit}</b> (3 P). c) {de(m, 0)} / {de(best, 0)} = {de(h)}-mal (2 P). '
        'd) z. B. konstanter Bedarf, keine Mengenrabatte, keine Fehlmengen, sofortige Lieferung, beliebig teilbar; Schwäche: Rabatte oder Verpackungseinheiten verletzen die Annahmen (4 P).', i == 0))
A2 = dict(titel='Optimale Bestellmenge', punkte=14, teile=[dict(punkte=14, varianten=a2)])

# ---------------------------------------------------------------- A3 Bestellverfahren (14 P)
RATEN = [6.5, 8.0, 5.0, 7.5, 6.0, 8.5, 5.5]


def sim(politik, MAXB=84, MELDE=46, Q=48, TW=2.5, IV=7.0):
    b, t, pts, best, ank, offen, nxt = 62.0, 0.0, [], [], [], [], 2.0
    while t <= 26:
        for a, m in list(offen):
            if t >= a - 1e-9:
                pts.append((t, b)); ank.append((t, b, b + m)); b += m; offen.remove((a, m)); pts.append((t, b))
        if politik[0] == 't' and t >= nxt - 1e-9:
            m = Q if politik == 'tq' else round(MAXB - b + 6.4 * TW); best.append((t, b)); offen.append((t + TW, m)); nxt += IV
        if politik[0] == 's' and b <= MELDE and not offen:
            m = Q if politik == 'sq' else round(MAXB - b + 6.4 * TW); best.append((t, b)); offen.append((t + TW, m))
        pts.append((t, b)); b -= RATEN[int(t) % 7] * 0.05; t += 0.05
    return pts, best, ank


def bild(politik):
    X = lambda t: 40 + t * 9.6
    Y = lambda v: 200 - v * 2.0
    pts, best, ank = sim(politik)
    m = lambda n, x, y: f'<circle cx="{x:.0f}" cy="{y:.0f}" r="11" style="fill:var(--x-acc)"/><text x="{x:.0f}" y="{y + 4.5:.0f}" text-anchor="middle" style="fill:var(--x-card);font-weight:800">{n}</text>'
    s = f'<rect x="40" y="{Y(26):.0f}" width="250" height="{Y(0) - Y(26):.0f}" style="fill:var(--x-soft)"/>'
    s += '<path class="ax" d="M40,200 H296 M40,200 V14"/>'
    s += '<text x="44" y="12">Lagerbestand</text><text x="296" y="216" text-anchor="end">Zeit</text>'
    if politik in ('tS', 'sS'):
        s += f'<path class="ax" d="M40,{Y(84):.0f} H290" stroke-dasharray="6 4"/>'
    if politik[0] == 's':
        s += f'<path class="ax" d="M40,{Y(46):.0f} H290" stroke-dasharray="6 4"/>'
    s += '<polyline class="k" points="' + ' '.join(f'{X(t):.1f},{Y(v):.1f}' for t, v in pts) + '"/>'
    t0, b0 = best[0]
    s += f'<path class="ax" d="M{X(t0):.0f},210 H{X(t0 + 2.5):.0f} M{X(t0):.0f},205 V215 M{X(t0 + 2.5):.0f},205 V215"/>'
    if politik[0] == 's' or politik[1] == 'S':
        s += m(1, 312, Y(46) if politik[0] == 's' else Y(84))
    else:
        s += m(1, 312, Y(max(v for _, v in pts)))
        s += f'<path class="ax" d="M40,{Y(max(v for _, v in pts)):.0f} H290" stroke-dasharray="2 4"/>'
    s += m(2, 312, Y(13))
    ta, v0, v1 = ank[1]
    s += m(3, X(ta) + 16, Y(v0 + 0.6 * (v1 - v0)))
    s += m(4, X(t0 + 1.25), 230)
    return f'<svg class="kb-svg" viewBox="0 0 330 246" role="img" aria-label="Lagerbestandsverlauf">{s}</svg>'

NAMEN = {'tq': ('Bestellrhythmusverfahren mit fester Bestellmenge (t,q)', 'gleiche Zeitabstände zwischen den Bestellungen, gleich hohe Sprünge', '① = maximaler Lagerbestand (es gibt keinen Meldebestand)',
                'gleichmäßigen (konstanten) Bedarf', 'einfach, wenig Koordinationsaufwand, automatisierbar', 'Verbrauchsschwankungen werden nicht berücksichtigt (Engpässe oder zu hohe Bestände)'),
         'tS': ('Bestellrhythmusverfahren mit Auffüllen auf den Soll-Lagerbestand (t,S)', 'gleiche Zeitabstände, unterschiedlich hohe Sprünge bis in Richtung Linie S', '① = Soll-Lagerbestand S',
                'eher gleichmäßigen Bedarf mit leichten Schwankungen', 'Lagerhöchstmenge auf S gedeckelt, Schwankungen teilweise ausgeglichen', 'erhöhter Koordinationsaufwand, Gefahr von Fehlmengen'),
         'sq': ('Bestellpunktverfahren mit fester Bestellmenge (s,q)', 'Bestellung immer beim selben Bestand (Linie ①), dadurch unterschiedliche Abstände; gleich hohe Sprünge', '① = Meldebestand',
                'schwankenden Bedarf', 'gleicht kurzfristige Schwankungen aus, niedrige Bestände, geringe Kapitalbindung', 'Bestände müssen ständig kontrolliert werden'),
         'sS': ('Bestellpunktverfahren mit Auffüllen auf den Soll-Lagerbestand (s,S)', 'Bestellung beim Meldebestand, unterschiedliche Abstände; Sprünge bis zur Linie S, also variabel', '① = Meldebestand (untere Linie), obere Linie = Soll-Lagerbestand S',
                'schwankenden Bedarf', 'gleicht Schwankungen aus, Bestand nach oben begrenzt', 'ständige Bestandskontrolle, höherer Aufwand')}
a3 = []
for i, pol in enumerate(['sq', 'tq', 'sS', 'tS']):
    n, merk, eins, bed, vor, nach = NAMEN[pol]
    V_, T_, SB = [(120, 0.5, 180), (90, 1, 120), (200, 0.5, 250), (60, 1.5, 90)][i]
    MB = V_ * T_ + SB
    a3.append(V(f'3-best{i}', 'bestellsysteme',
        f'Die Abbildung (im Antwortfeld) zeigt den Lagerbestandsverlauf eines Materials. '
        f'a) Benennen Sie die in der Abbildung markierten Größen ①–④.<br>b) Um welches Bestellverfahren handelt es sich? Begründen Sie anhand der Abbildung.<br>'
        f'c) Für welchen Bedarfsverlauf ist es geeignet? Nennen Sie je einen Vor- und Nachteil.<br>d) Verbrauch {V_} Stück/Monat, Wiederbeschaffungszeit {de(T_, 1)} Monate, Sicherheitsbestand {SB} Stück: Berechnen Sie den Meldebestand.',
        [T('a) Größen ①–④', 4, 4), T('b) Verfahren und Begründung', 4, 4), T('c) Eignung, Vor- und Nachteil', 3, 3), Z('d) Meldebestand', MB, 3, 'Stück')],
        f'a) {eins}; ② Sicherheitsbestand; ③ Bestellmenge (Wareneingang); ④ Wiederbeschaffungszeit (4 P). b) <b>{n}</b>: {merk} (4 P). '
        f'c) Geeignet für {bed}; Vorteil: {vor}; Nachteil: {nach} (3 P). d) MB = {V_} · {de(T_, 1)} + {SB} = <b>{de(MB, 0)}</b> Stück (3 P).', i == 0, bild(pol)))
A3 = dict(titel='Bestellverfahren', punkte=14, teile=[dict(punkte=14, varianten=a3)])

# ---------------------------------------------------------------- A4 Brutto- zum Nettobedarf (12 P)
SCHEMA = '<table class="tbl"><tr><th>Position</th><th>Erläuterung</th></tr>' + ''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in [
    ('Sekundärbedarf', '…'), ('+ …', '…'), ('= Bruttobedarf', '…'), ('− …', '…'), ('− …', '…'), ('+ …', '…'), ('= Nettobedarf', '…')]) + '</table>'
LOES = ('Sekundärbedarf: aus dem Primärbedarf über Stücklistenauflösung abgeleitet. + <b>Zusatzbedarf</b>: ungeplanter Mehrbedarf (Ausschuss, Schwund, Verschnitt), statistisch als Prozentsatz. '
        '= <b>Bruttobedarf</b>: für die Fertigung der Erzeugnisse benötigter Periodenbedarf. − <b>Lagerbestände</b>: im Lager vorhanden. − <b>Bestellbestände</b>: offene Bestellungen (intern/extern). '
        '+ <b>reservierte Bestände</b>: für vorgemerkte Aufträge, nicht verfügbar. = <b>Nettobedarf</b>: Ausgangspunkt für Disposition und Beschaffung.')
a4 = [
    V('4-schema', 'brutto-netto', f'Ermitteln Sie den Nettobedarf aus dem Bruttobedarf. Vervollständigen Sie das Schema (Positionen) und erläutern Sie jede Position kurz.{SCHEMA}',
      [T('fehlende Positionen', 6, 4), T('Erläuterungen', 6, 7)], LOES + ' (je Position 1 P, je Erläuterung 1 P)', True),
    V('4-erklaeren', 'brutto-netto', f'Das Schema zur Nettobedarfsermittlung lautet: Sekundärbedarf + Zusatzbedarf = Bruttobedarf − Lagerbestände − Bestellbestände + reservierte Bestände = Nettobedarf.<br>'
      'a) Definieren Sie den Bruttobedarf. b) Erläutern Sie Zusatzbedarf, Bestellbestände und reservierte Bestände. c) Warum werden reservierte Bestände addiert? d) Wozu dient der Nettobedarf?',
      [T('a) Bruttobedarf', 2, 2), T('b) drei Positionen', 6, 5), T('c) reservierte Bestände', 2, 2), T('d) Nettobedarf', 2, 2)],
      'a) Für die Fertigung der Erzeugnisse benötigter Periodenbedarf (2 P). b) Zusatzbedarf: Ausschuss, Schwund, Verschnitt als Prozentsatz; Bestellbestände: offene Bestellungen; reservierte Bestände: für vorgemerkte Aufträge (6 P). '
      'c) Sie liegen zwar im Lager, stehen aber nicht zur Verfügung; sie wurden mit dem Lagerbestand abgezogen und müssen wieder addiert werden (2 P). d) Ausgangspunkt für Materialdisposition und Beschaffung (Bestellanforderung an den Einkauf) (2 P).'),
    V('4-bedarfsarten', 'bedarfsarten', 'a) Definieren Sie Primär-, Sekundär- und Tertiärbedarf und nennen Sie jeweils die Quelle bzw. ein Beispiel.<br>b) Stellen Sie das Schema vom Sekundärbedarf zum Nettobedarf als Tabelle dar (nur Positionen).',
      [T('a) Bedarfsarten', 6, 5), T('b) Schema', 6, 5)],
      'a) Primärbedarf: verkaufsfähige Enderzeugnisse, Ersatzteile; aus der Vertriebsplanung (Jeans). Sekundärbedarf: Rohstoffe, Teile, Baugruppen für den Primärbedarf; aus der Stücklistenauflösung (Stoff). Tertiärbedarf: Hilfs- und Betriebsstoffe für die Produktion (Strom) (6 P). '
      'b) Sekundärbedarf + Zusatzbedarf = Bruttobedarf − Lagerbestände − Bestellbestände + reservierte Bestände = Nettobedarf (6 P).'),
]
S_, Zp, L_, B_, R_ = 2400, 4, 380, 500, 120
br = S_ * (1 + Zp / 100); ne = br - L_ - B_ + R_
a4.append(V('4-rechnen', 'brutto-netto', f'Sekundärbedarf {de(S_, 0)} Stück, Zusatzbedarf {Zp} %, Lagerbestand {L_}, Bestellbestand {B_}, reservierte Bestände {R_}.<br>a) Berechnen Sie Brutto- und Nettobedarf. b) Erläutern Sie die Positionen Bestellbestand und reservierte Bestände.',
    [Z('a) Bruttobedarf', br, 3, 'Stück'), Z('a) Nettobedarf', ne, 4, 'Stück'), T('b) Erläuterung', 5, 4)],
    f'a) Brutto = {de(S_, 0)} · 1,04 = {de(br, 0)} (3 P); Netto = {de(br, 0)} − {L_} − {B_} + {R_} = <b>{de(ne, 0)}</b> (4 P). b) Bestellbestand: offene Bestellungen, die noch eintreffen; reservierte Bestände: für Aufträge vorgemerkt, nicht verfügbar, deshalb addiert (5 P).'))
A4 = dict(titel='Vom Brutto- zum Nettobedarf', punkte=12, teile=[dict(punkte=12, varianten=a4)])

KL = dict(deckblatt=dict(fach='Grundlagen der Materialwirtschaft', pruefer='Prof. Dr. A. Meier', hilfsmittel='Taschenrechner (Annahme)',
                         bemerkungen='MaWi-Teil der Modulklausur (zusammen mit Industriebetriebslehre, 120 Minuten). Lösungswege angeben.'),
          aufgaben=[A1, A2, A3, A4])
KAP = {t_['id'] for k in json.loads((IN / 'fach.json').read_text())['kapitel'] for t_ in k['themen']}
for A in KL['aufgaben']:
    assert sum(T_['punkte'] for T_ in A['teile']) == A['punkte'], A['titel']
    for T_ in A['teile']:
        assert 3 <= len(T_['varianten']) <= 10, (A['titel'], len(T_['varianten']))
        for v in T_['varianten']:
            assert abs(sum(f['p'] for f in v['felder']) - T_['punkte']) < 1e-9, v['id']; assert v['unter'] in KAP
summe = sum(A['punkte'] for A in KL['aufgaben']); assert summe == 60, summe
(IN / 'klausur.json').write_text(json.dumps(KL, ensure_ascii=False, indent=1))
print(f'mawi: Probeklausur {summe} P, {len(KL["aufgaben"])} Aufgaben, {sum(len(T_["varianten"]) for A in KL["aufgaben"] for T_ in A["teile"])} Varianten; a/b/c/d: {[pos.count(k) for k in range(4)]}')
