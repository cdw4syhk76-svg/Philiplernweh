"""Erzeugt inhalte/bwl/klausur.json: ABWL-Teil der Klausur „ABWL & Marketing“ (80 Punkte) im Aufbau des Prüfers:
Teil A Rechenaufgaben ohne Taschenrechner, nur das Ergebnis zählt (40 P); Teil B Single Choice, je vier Antworten,
genau eine richtig, keine Minuspunkte (20 × 2 P). Zahlen werden hier berechnet. Aufruf: python3 werkzeuge/bwl/klausur.py"""
import json, math, pathlib, random, re
from fractions import Fraction as Fr
ROOT = pathlib.Path(__file__).resolve().parents[2]
IN = ROOT / 'inhalte' / 'bwl'
rnd = random.Random(26)
txt = lambda s: re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', str(s))).strip()


def de(x, nk=2):
    x = float(x)
    if abs(x - round(x)) < 1e-9: nk = 0
    s = f'{x:,.{nk}f}'.replace(',', '#').replace('.', ',').replace('#', '.')
    if ',' in s: s = s.rstrip('0').rstrip(',')
    return s.replace('-', '−')


def Z(label, wert, p, einheit='', tol=None):
    d = dict(typ='zahl', label=label, loesung=round(float(wert), 4), p=p)
    if einheit: d['einheit'] = einheit
    if tol is not None: d['tol'] = tol
    return d


def V(id, unter, text, felder, loesung): return dict(id=id, unter=unter, text=text, felder=felder, loesung=loesung)


# ================================================================ Teil A: Rechnen
# ---------- 1a Rentabilität
rent = []
for i, (g, ek) in enumerate([(22500, 150000), (18000, 120000), (36000, 240000), (13500, 90000)]):
    r = Fr(g, ek) * 100
    rent.append(V(f'a1a-ek{i}', 'rentabilitaet', f'Ein Unternehmen erzielt eine Eigenkapitalrentabilität von {de(r)} % bei einem Gewinn von {de(g)} €. Wie hoch ist das Eigenkapital?',
                  [Z('Eigenkapital', ek, 4, '€')], f'\\(EK = \\frac{{{de(g)}}}{{{de(r)}\\,\\%}} = {de(ek)}\\) €'))
for i, (r, ek) in enumerate([(12, 22500), (8, 37500), (15, 42000)]):
    g = Fr(r, 100) * ek
    rent.append(V(f'a1a-g{i}', 'rentabilitaet', f'Die Eigenkapitalrentabilität beträgt {r} %, das Eigenkapital {de(ek)} €. Wie hoch ist der Gewinn?',
                  [Z('Gewinn', g, 4, '€')], f'\\(G = {r}\\,\\% \\cdot {de(ek)} = {de(g)}\\) €'))
rent.append(V('a1a-infl', 'rentabilitaet', 'Eine Influencerin startet mit 500 € Eigenkapital und macht im ersten Jahr 1.000 € Gewinn. Wie hoch ist ihre Eigenkapitalrentabilität?',
              [Z('EK-Rentabilität', 200, 4, '%')], '\\(\\frac{1.000}{500} \\cdot 100\\,\\% = 200\\,\\%\\)'))
for i, (g, u) in enumerate([(27000, 450000), (12000, 300000)]):
    rent.append(V(f'a1a-u{i}', 'rentabilitaet', f'Umsatz {de(u)} €, Gewinn {de(g)} €. Wie hoch ist die Umsatzrentabilität?',
                  [Z('Umsatzrentabilität', Fr(g, u) * 100, 4, '%')], f'\\(\\frac{{{de(g)}}}{{{de(u)}}} \\cdot 100\\,\\% = {de(Fr(g, u) * 100)}\\,\\%\\)'))

rent = rent[:3] + rent[4:6] + rent[7:9]

# ---------- 1b Break-even (quadratisch, ganzzahlige Nullstellen): G(x) = −a(x − r1)(x − r2)
be = []
for i, (p, a, r1, r2) in enumerate([(120, 1, 20, 80), (100, 1, 30, 50), (90, 2, 10, 30), (150, 1, 40, 90), (60, 0.5, 20, 60)]):
    # E(x) = p x;  K(x) = p x − G(x) = a x² + (p − a(r1+r2)) x + a r1 r2
    k1, k0 = p - a * (r1 + r2), a * r1 * r2
    assert k1 > 0
    kf = f'{de(a)}x^2' if a != 1 else 'x^2'
    be.append(V(f'a1b-{i}', 'breakeven', f'Erlösfunktion \\(E(x) = {p}x\\), Kostenfunktion \\(K(x) = {kf} + {de(k1)}x + {de(k0)}\\). Bei welcher Menge liegt die Gewinnschwelle (Break-even-Punkt)?',
                [Z('Gewinnschwelle x', r1, 5, 'ME')],
                f'\\(G(x) = -{kf} + {de(p - k1)}x - {de(k0)} = 0\\) → \\(x_1 = {r1}\\), \\(x_2 = {r2}\\). Gewinnschwelle ist die kleinere Lösung: <b>{r1} ME</b>.'))
for i, (p, kv, kf) in enumerate([(25, 15, 7000), (40, 28, 9600)]):
    x = Fr(kf, p - kv)
    be.append(V(f'a1b-lin{i}', 'breakeven', f'Preis {p} €, variable Kosten {kv} € je Stück, Fixkosten {de(kf)} €. Break-even-Menge?',
                [Z('Break-even x', x, 5, 'Stück')], f'\\(x = \\frac{{{de(kf)}}}{{{p} - {kv}}} = {de(x)}\\) Stück'))

# ---------- 1c Gewinnmaximum: G(x) = −a x² + b x − c
gm = []
for i, (a, b, c) in enumerate([(1, 100, 1600), (2, 80, 300), (0.5, 60, 1000), (3, 120, 500), (1, 64, 200)]):
    x = b / (2 * a); g = -a * x * x + b * x - c
    assert x == int(x) and g == int(g)
    af = f'{de(a)}x^2' if a != 1 else 'x^2'
    gm.append(V(f'a1c-{i}', 'gewinnmax', f'Gewinnfunktion \\(G(x) = -{af} + {b}x - {de(c)}\\). Bestimmen Sie die gewinnmaximale Menge und den maximalen Gewinn.',
                [Z('x', x, 2, 'ME'), Z('G(x)', g, 3, '€')],
                f"\\(G^{{\\prime}}(x) = -{de(2 * a)}x + {b} = 0\\) → x = {de(x)}; \\(G({de(x)}) = {de(g)}\\) €"))

# ---------- 1d Rentabilitätsmaximum / Kennzahlen
rm = []
for i, (a, b, c, k) in enumerate([(20, 40, 80, 2), (1, 100, 1600, 100), (2, 60, 200, 10), (1, 50, 400, 4)]):
    # R(x) = (−a x² + b x − c)/(k x) → R' = (−a + c/x²)/k = 0 → x = √(c/a)
    x = math.sqrt(c / a); assert x == int(x)
    R = (-a * x * x + b * x - c) / (k * x)
    af = f'{a}x^2' if a != 1 else 'x^2'
    rm.append(V(f'a1d-r{i}', 'rentmax', f'Gewinn \\(G(x) = -{af} + {b}x - {de(c)}\\), Kapitalbedarf \\(\\text{{Kap}}(x) = {k}x\\). Bei welcher Menge ist die Rentabilität maximal?',
                [Z('x', x, 4, 'ME')], f"\\(R(x) = -{de(a / k)}x + {de(b / k)} - \\frac{{{de(c / k)}}}{{x}}\\); \\(R^{{\\prime}}(x) = -{de(a / k)} + \\frac{{{de(c / k)}}}{{x^2}} = 0\\) → x = {de(x)} (R = {de(R * 100)} %)"))
for i, (ek, fk) in enumerate([(150000, 250000), (60000, 240000), (90000, 110000)]):
    q = Fr(ek, ek + fk) * 100
    rm.append(V(f'a1d-q{i}', 'liquiditaet', f'Eigenkapital {de(ek)} €, Fremdkapital {de(fk)} €. Wie hoch ist die Eigenkapitalquote?',
                [Z('EK-Quote', q, 4, '%')], f'\\(\\frac{{{de(ek)}}}{{{de(ek + fk)}}} \\cdot 100\\,\\% = {de(q)}\\,\\%\\)'))

# ---------- 2a Mittelwertmethode
def mw(p1, m1, p2, m2):
    return abs(Fr(m2 - m1, Fr(m1 + m2, 2)) / Fr(p2 - p1, Fr(p1 + p2, 2)))
mwv = []
for i, (was, p1, m1, p2, m2) in enumerate([('Shisha-Bar: Bei 10 € je Kopf kommen 5 Gäste, bei 6 € kommen 15.', 10, 5, 6, 15),
                                            ('Parkhaus: Bei 12 € werden 50 Plätze gebucht, bei 9 € sind es 80.', 12, 50, 9, 80),
                                            ('Yogastudio: Bei 20 € kommen 120 Teilnehmende, bei 16 € kommen 180.', 20, 120, 16, 180),
                                            ('Kino: Bei 8 € werden 300 Karten verkauft, bei 12 € nur 200.', 8, 300, 12, 200),
                                            ('Bäckerei: Bei 3 € je Brot werden 90 verkauft, bei 5 € noch 70.', 3, 90, 5, 70)]):
    e = mw(p1, m1, p2, m2)
    mwv.append(V(f'a2a-{i}', 'mittelwert', was + ' Berechnen Sie die Preiselastizität der Nachfrage mit der Mittelwertmethode (Betrag, auf zwei Nachkommastellen).',
                 [Z('|ε|', e, 5, '', 0.011)],
                 f'\\(\\varepsilon = \\frac{{({m2} - {m1}) / {de(Fr(m1 + m2, 2))}}}{{({p2} - {p1}) / {de(Fr(p1 + p2, 2))}}}\\) → |ε| ≈ <b>{de(round(float(e), 2))}</b>'
                 + (' (elastisch)' if e > 1 else ' (unelastisch)' if e < 1 else ' (einheitselastisch)')))

# ---------- 2b Punktelastizität
pe = []
for i, (a, b, p) in enumerate([(20000, 5, 800), (1200, 4, 200), (500, 2, 50), (900, 3, 150), (2400, 6, 100)]):
    q = a - b * p; e = Fr(b * p, q)
    pe.append(V(f'a2b-{i}', 'punktelastizitaet', f'Nachfrage \\(D(p) = {de(a)} - {b}p\\). Wie groß ist die Punktelastizität (Betrag) beim Preis p = {p}?',
                [Z('|ε|', e, 4, '', 0.011)], f'Q = {de(q)}; \\(|\\varepsilon| = {b} \\cdot \\frac{{{p}}}{{{de(q)}}} = {de(round(float(e), 4))}\\)'))
pe.append(V('a2b-gg', 'punktelastizitaet', 'Nachfrage \\(D(p) = 1.200 - 4p\\), Angebot \\(S(p) = 2p\\). Wie groß ist die Punktelastizität der Nachfrage im Marktgleichgewicht (Betrag)?',
            [Z('|ε|', 2, 4)], 'S = D → 6p = 1.200 → p = 200, Q = 400; |ε| = 4 · 200/400 = 2'))

# ---------- 2c Effekte
ef = []
for i, (p1, m1, p2, m2) in enumerate([(20, 120, 16, 180), (10, 5, 6, 15), (12, 50, 9, 80), (8, 300, 12, 200), (5, 400, 4, 450)]):
    ME, PE, GE = (m2 - m1) * p2, (p2 - p1) * m1, p2 * m2 - p1 * m1
    assert GE == ME + PE
    ef.append(V(f'a2c-{i}', 'effekte', f'Der Preis ändert sich von {p1} € auf {p2} €, die Menge von {m1} auf {m2} Stück. Berechnen Sie Mengen-, Preis- und Gesamteffekt (mit Vorzeichen).',
                [Z('ME', ME, 2, '€'), Z('PE', PE, 1, '€'), Z('GE', GE, 2, '€')],
                f'ME = ({m2} − {m1}) · {p2} = {de(ME)} €; PE = ({p2} − {p1}) · {m1} = {de(PE)} €; GE = {de(p2 * m2)} − {de(p1 * m1)} = {de(GE)} €'))

# ---------- 3 Entscheidungsregeln
def matrix_html(M):
    return ('<table class="tbl"><tr><th></th>' + ''.join(f'<th>z{j + 1}</th>' for j in range(len(M[0]))) + '</tr>'
            + ''.join(f'<tr><td>a{i + 1}</td>' + ''.join(f'<td>{de(x)}</td>' for x in r) + '</tr>' for i, r in enumerate(M)) + '</table>')
hw, by = [], []
for i, M in enumerate([[(40, 70, 100), (60, 60, 70), (20, 90, 120)], [(10, 50, 30), (20, 25, 40), (5, 80, 15)], [(100, 200, 150), (120, 130, 140), (50, 300, 100)],
                       [(30, 30, 30), (10, 40, 60), (0, 20, 90)]]):
    lam = Fr(2, 5)
    w = [lam * max(r) + (1 - lam) * min(r) for r in M]; b = max(range(3), key=lambda k: w[k])
    assert w.count(w[b]) == 1 or i == 0
    if i == 0: b = 0
    hw.append(V(f'a3a-{i}', 'hurwicz', 'Ergebnismatrix (Gewinn in T€):' + matrix_html(M) + f'Berechnen Sie den Hurwicz-Wert der Alternative a{b + 1} (λ = 0,4).',
                [Z(f'Φ(a{b + 1})', w[b], 4, 'T€')],
                ' · '.join(f'Φ(a{k + 1}) = 0,4 · {max(r)} + 0,6 · {min(r)} = {de(w[k])}' for k, r in enumerate(M))))
for i, (M, ps) in enumerate([([(40, 70, 100), (60, 60, 70), (20, 90, 120)], (3, 5, 2)), ([(10, 50, 30), (20, 25, 40), (5, 80, 15)], (2, 5, 3)),
                             ([(100, 200, 150), (120, 130, 140), (50, 300, 100)], (5, 3, 2)), ([(30, 30, 30), (10, 40, 60), (0, 20, 90)], (1, 6, 3))]):
    p = [Fr(x, 10) for x in ps]
    E = [sum(p[j] * r[j] for j in range(3)) for r in M]; b = max(range(3), key=lambda k: E[k])
    by.append(V(f'a3b-{i}', 'bayes', 'Ergebnismatrix (Gewinn in T€):' + matrix_html(M) + f'Die Wahrscheinlichkeiten sind {", ".join(de(x) for x in p)}. Welchen Erwartungswert hat die Alternative, die die Bayes-Regel wählt?',
                [Z('µ', E[b], 4, 'T€')], ' · '.join(f'µ(a{k + 1}) = {de(E[k])}' for k in range(3)) + f' → a{b + 1}'))

for L in (rent, be, gm, rm, mwv, pe, ef, hw, by):
    assert 3 <= len(L) <= 7, len(L)
    for v in L: assert sum(f['p'] for f in v['felder']) == sum(f['p'] for f in L[0]['felder'])

teilA = [
    dict(titel='Teil A · Erfolgskennzahlen', punkte=18, intro='Nur das Ergebnis wird gewertet. Ohne Taschenrechner.',
         teile=[dict(punkte=4, varianten=rent), dict(punkte=5, varianten=be), dict(punkte=5, varianten=gm), dict(punkte=4, varianten=rm)]),
    dict(titel='Teil A · Elastizität', punkte=14, intro='Nur das Ergebnis wird gewertet. Elastizität immer als Betrag.',
         teile=[dict(punkte=5, varianten=mwv), dict(punkte=4, varianten=pe), dict(punkte=5, varianten=ef)]),
    dict(titel='Teil A · Entscheidungsregeln', punkte=8, intro='Nur das Ergebnis wird gewertet. Hurwicz mit λ = 0,4.',
         teile=[dict(punkte=4, varianten=hw), dict(punkte=4, varianten=by)]),
]

# ================================================================ Teil B: Single Choice
GRUPPEN = [
    ['betrieb', 'leistungsart', 'dienstleistung', 'betriebszweck', 'bwl-def', 'wirtschaften'],
    ['oekprinzip', 'kennzahlen', 'effizienz'],
    ['rentabilitaet', 'rentmax', 'liquiditaet', 'breakeven', 'gewinnmax', 'kapazitaet'],
    ['elastizitaet', 'mittelwert'],
    ['punktelastizitaet', 'effekte'],
    ['opportunitaet'],
    ['grenznutzen', 'maerkte', 'innovation'],
    ['homo-oeconomicus', 'stakeholder', 'shareholder-value', 'werturteile'],
    ['zielbeziehungen', 'zielsystem', 'et-struktur'],
    ['hurwicz'],
    ['maximin', 'savage-niehans', 'laplace', 'dominanz'],
    ['bayes', 'bernoulli'],
    ['begrenzte-rationalitaet', 'prospect-theory', 'garbage-can'],
    ['five-forces', 'markteintritt', 'verhandlungsmacht', 'umweltanalyse'],
    ['swot', 'mbv-rbv', 'ressourcen'],
    ['renten'],
    ['bcg-matrix', 'lebenszyklus', 'erfahrungskurve'],
    ['ansoff', 'porter-strategien', 'fuehrung', 'zielhierarchie', 'implementierung'],
    ['personengesellschaften', 'kg', 'rechtsform-kriterien'],
    ['ag', 'gmbh', 'rechtsform-fall'],
]
fam = json.loads((IN / 'fragen.json').read_text())['familien']
mcs = {}
for f in fam:
    if ':fa-' in f['id']: continue   # Folienabgleich-Ergänzungen: nicht im Probeklausur-Bogen (Varianten-IDs bleiben stabil)
    for a in f['a']:
        if a['y'] == 'mc' and len(a['o']) == 4 and sum(1 for o in a['o'] if o[1]) == 1 and '<svg' not in a['p']:
            mcs.setdefault(f['t'], []).append(a)
teileB = []
for gi, g in enumerate(GRUPPEN):
    kand = [(t, a) for t in g for a in mcs.get(t, [])]
    kand.sort(key=lambda x: (not x[1].get('klausur'), (x[1].get('lvl') or 1) == 1))   # Klausurfragen zuerst, leichte zuletzt
    vs, gesehen = [], set()
    for t, a in kand:
        if a['p'] in gesehen: continue
        gesehen.add(a['p'])
        o = a['o'][:]; rnd.shuffle(o)
        r = next(j for j, x in enumerate(o) if x[1])
        vs.append(V(f'b{gi + 1}-{len(vs)}', t, a['p'], [dict(typ='sc', o=[x[0] for x in o], r=r, p=2)],
                    f'<b>{"abcd"[r]}) {o[r][0]}</b>' + (f'<br>{a["w"]}' if a.get('w') else '')))
        if len(vs) == 7: break
    assert len(vs) >= 3, (g, len(vs))
    teileB.append(dict(punkte=2, varianten=vs))
pos = [v['felder'][0]['r'] for T in teileB for v in T['varianten']]
teilB = [dict(titel='Teil B · Single Choice', punkte=40, intro='Je Frage ist genau eine Antwort richtig. Keine Minuspunkte. Auch hier wird teilweise gerechnet.', teile=teileB)]

K = dict(deckblatt=dict(fach='Einführung in die BWL', pruefer='Prof. Dr. C. Paul', hilfsmittel='keine (kein Taschenrechner)',
                        bemerkungen='Matrikelnummer auf das Deckblatt. Blätter nicht trennen. Teil A: nur das Ergebnis zählt. Teil B: genau eine Antwort je Frage.'),
         aufgaben=teilA + teilB)
summe = sum(A['punkte'] for A in K['aufgaben'])
assert summe == 80, summe
for A in K['aufgaben']: assert sum(T['punkte'] for T in A['teile']) == A['punkte'], A['titel']
(IN / 'klausur.json').write_text(json.dumps(K, ensure_ascii=False, indent=1))
print(f'bwl: Probeklausur {summe} P, {len(K["aufgaben"])} Aufgaben, {sum(len(T["varianten"]) for A in K["aufgaben"] for T in A["teile"])} Varianten; '
      f'richtige Antwort a/b/c/d: {[pos.count(k) for k in range(4)]}')
