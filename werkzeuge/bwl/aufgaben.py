"""Erzeugt inhalte/bwl/aufgaben.json (große Aufgaben). Aufruf: python3 werkzeuge/bwl/aufgaben.py
Alle Zahlen werden hier gerechnet und geprüft, nie von Hand eingetragen."""
import json, math, pathlib
from fractions import Fraction as Fr
ROOT = pathlib.Path(__file__).resolve().parents[2]
A = []


def de(x, nk=None):
    """Zahl deutsch formatiert: 1.234,5"""
    if nk is None:
        nk = 0 if abs(x - round(x)) < 1e-9 else (1 if abs(x * 10 - round(x * 10)) < 1e-9 else 2)
    s = f'{x:,.{nk}f}'.replace(',', '#').replace('.', ',').replace('#', '.')
    return s.replace('-', '−')


def ol(*schritte): return '<ol>' + ''.join(f'<li>{s}</li>' for s in schritte) + '</ol>'
def eh(t): return f'<p><b>Erwartungshorizont</b>: {t}</p>'


def teil(text, punkte, tipp1, tipp2, loesung, ergebnis=None, einheit=None, tol=None):
    d = {'text': text, 'punkte': punkte, 'tipp1': tipp1, 'tipp2': tipp2, 'loesung': loesung}
    if ergebnis is not None:
        d['ergebnis'] = round(ergebnis, 4)
        if einheit: d['einheit'] = einheit
        if tol is not None: d['tol'] = tol
    return d


def aufgabe(id, unter, art, stufe, titel, ausgang, teile, klausur=True):
    A.append({'id': 'bwl-' + id, 'unter': unter, 'art': art, 'stufe': stufe, 'klausur': klausur, 'titel': titel,
              'quelle': 'im Klausurstil', 'ausgang': ausgang, 'teile': teile})


# ---------------------------------------------------------------- k2: Break-even, Gewinn- und Rentabilitätsmaximum
p, a2, a1, a0, kap = 120, 1, 20, 1600, 100          # E = p·x, K = a2 x² + a1 x + a0, Kap = kap·x
g2, g1, g0 = -a2, p - a1, -a0                         # G = −x² + 100x − 1600
D = g1 ** 2 - 4 * g2 * g0
x_be = sorted([(-g1 + s * math.sqrt(D)) / (2 * g2) for s in (1, -1)])
x_g = -g1 / (2 * g2); G = lambda x: g2 * x * x + g1 * x + g0
x_r = math.sqrt(-g0 / -g2)                            # R = (g2 x + g1 + g0/x)/kap → R' = (g2 − g0/x²)/kap = 0
R = G(x_r) / (kap * x_r) * 100
assert x_be == [20, 80] and x_g == 50 and G(50) == 900 and x_r == 40 and R == 20
aufgabe('gewinnschwelle', ['breakeven', 'gewinnmax', 'rentmax'], 'rechnen', 3, 'Gewinnschwelle, Gewinn- und Rentabilitätsmaximum',
    f'<p>Die Rösterei „Bohnenwerk“ verkauft Kaffeepakete für <b>{p} €</b> je Paket. Ihre Kostenfunktion lautet '
    f'\\(K(x) = x^2 + {a1}x + {de(a0)}\\) (x in Paketen pro Tag). Für die Produktion wird Kapital gebunden: \\(\\text{{Kap}}(x) = {kap}x\\). '
    'Rechnen Sie ohne Taschenrechner.</p>',
    [teil('Stellen Sie die Gewinnfunktion auf und berechnen Sie die Gewinnschwelle (kleinere Menge).', 4,
          'Gewinn = Erlös − Kosten. Wo ist der Gewinn null?',
          '\\(G(x) = 120x - (x^2 + 20x + 1.600)\\); dann \\(G(x) = 0\\) mit der Mitternachtsformel lösen.',
          ol('\\(G(x) = -x^2 + 100x - 1.600\\)', '\\(x^2 - 100x + 1.600 = 0\\)',
             '\\(x_{1,2} = 50 \\pm \\sqrt{2.500 - 1.600} = 50 \\pm 30\\)', 'Gewinnschwelle <b>x = 20 Pakete</b> (die Gewinngrenze liegt bei 80 Paketen)'),
          20, 'Pakete'),
     teil('Bei welcher Menge ist der Gewinn maximal?', 3, 'Hochpunkt der Gewinnfunktion: Ableitung null setzen.',
          "\\(G^{\\prime}(x) = -2x + 100\\)",
          ol("\\(G^{\\prime}(x) = -2x + 100 = 0\\)", '<b>x = 50 Pakete</b>', 'Probe: liegt genau in der Mitte zwischen 20 und 80.'), 50, 'Pakete'),
     teil('Wie hoch ist der maximale Gewinn?', 2, 'Setze die Menge aus b) in G(x) ein.', '\\(G(50) = -2.500 + 5.000 - 1.600\\)',
          ol('\\(G(50) = -50^2 + 100 \\cdot 50 - 1.600\\)', '<b>G = 900 €</b>'), 900, '€'),
     teil('Berechnen Sie das Rentabilitätsmaximum (Menge und Rentabilität) und vergleichen Sie mit dem Gewinnmaximum.', 5,
          'R(x) = G(x) ÷ Kap(x). Teile jeden Summanden durch 100x.',
          "\\(R(x) = -\\frac{x}{100} + 1 - \\frac{16}{x}\\); \\(R^{\\prime}(x) = -\\frac{1}{100} + \\frac{16}{x^2}\\)",
          ol("\\(R(x) = \\frac{-x^2 + 100x - 1.600}{100x} = -0{,}01x + 1 - 16x^{-1}\\)",
             "\\(R^{\\prime}(x) = -0{,}01 + \\frac{16}{x^2} = 0 \\Rightarrow x^2 = 1.600 \\Rightarrow x = 40\\)",
             '\\(R(40) = \\frac{G(40)}{\\text{Kap}(40)} = \\frac{800}{4.000} = 0{,}2\\) → <b>20 %</b>',
             'Vergleich: Das Rentabilitätsmaximum (x = 40) liegt links vom Gewinnmaximum (x = 50), weil das Kapital mit der Menge wächst.'),
          40, 'Pakete')])

# ---------------------------------------------------------------- k2: Kennzahlen, Rentabilität, Liquidität
EK, FK, Gew, U, Er, Au = 150000, 250000, 22500, 450000, 472500, 450000
assert Er - Au == Gew
ekr, gkr, ur, ekq, wi = Gew / EK * 100, Gew / (EK + FK) * 100, Gew / U * 100, EK / (EK + FK) * 100, Er / Au
ZM, FO, VO, KV = 90000, 60000, 120000, 200000
l1, l2, l3 = ZM / KV * 100, (ZM + FO) / KV * 100, (ZM + FO + VO) / KV * 100
assert (ekr, gkr, ur, ekq, wi, l1, l2, l3) == (15, 5.625, 5, 37.5, 1.05, 45, 75, 135)
aufgabe('kennzahlen', ['kennzahlen', 'rentabilitaet', 'liquiditaet'], 'rechnen', 2, 'Kennzahlen einer Fahrradwerkstatt',
    f'<p>Die „Speichenwerk GmbH“ hat im Jahr Erträge von <b>{de(Er)} €</b> und Aufwendungen von <b>{de(Au)} €</b>; der Umsatz beträgt <b>{de(U)} €</b>. '
    f'Sie arbeitet mit <b>{de(EK)} €</b> Eigenkapital und <b>{de(FK)} €</b> Fremdkapital. In der Bilanz stehen außerdem: Zahlungsmittel {de(ZM)} €, '
    f'Forderungen {de(FO)} €, Vorräte {de(VO)} €, kurzfristige Verbindlichkeiten {de(KV)} €.</p>',
    [teil('Berechnen Sie Gewinn und Eigenkapitalrentabilität.', 3, 'Gewinn = Ertrag − Aufwand. Rentabilität = Erfolgsgröße ÷ Basisgröße · 100 %.',
          '\\(\\frac{22.500}{150.000} \\cdot 100\\,\\%\\)',
          ol('Gewinn = 472.500 − 450.000 = 22.500 €', 'EK-Rentabilität = \\(\\frac{22.500}{150.000} \\cdot 100\\,\\% = \\) <b>15 %</b>'), ekr, '%'),
     teil('Berechnen Sie Umsatzrentabilität, Gesamtkapitalrentabilität und Eigenkapitalquote.', 4,
          'Was steht jeweils im Nenner: Umsatz, gesamtes Kapital (EK + FK) oder wieder das gesamte Kapital?',
          'Gesamtkapital = 400.000 €.',
          ol('Umsatzrentabilität = 22.500 ÷ 450.000 = <b>5 %</b>', 'Gesamtkapitalrentabilität = 22.500 ÷ 400.000 = <b>5,625 %</b>',
             'EK-Quote = 150.000 ÷ 400.000 = <b>37,5 %</b>'), ekq, '%'),
     teil('Ist der Betrieb wirtschaftlich? Begründen Sie mit einer Kennzahl.', 2, 'Wirtschaftlichkeit = Ertrag ÷ Aufwand.',
          'Über 1 heißt wirtschaftlich.', ol('472.500 ÷ 450.000 = <b>1,05</b>', 'Größer als 1: Der Betrieb arbeitet wirtschaftlich.'), wi, ''),
     teil('Berechnen Sie die Liquidität 1., 2. und 3. Grades und beurteilen Sie die Zahlungsfähigkeit.', 4,
          'Jeder Grad nimmt mehr Vermögen in den Zähler: erst Zahlungsmittel, dann Forderungen, dann Vorräte.',
          'Nenner ist immer: kurzfristige Verbindlichkeiten (200.000 €).',
          ol('L1 = 90.000 ÷ 200.000 = <b>45 %</b>', 'L2 = 150.000 ÷ 200.000 = <b>75 %</b>', 'L3 = 270.000 ÷ 200.000 = <b>135 %</b>',
             'Sofort zahlen kann sie nur knapp die Hälfte; erst mit dem Verkauf der Vorräte sind alle kurzfristigen Schulden gedeckt.'), l3, '%')])

# ---------------------------------------------------------------- k2: Produktionsprogramm mit Kapazitäten
dA, dB, m = 40, 30, ((2, 1, 800), (1, 2, 700))
# Schnittpunkt 2a + b = 800, a + 2b = 700
det = m[0][0] * m[1][1] - m[0][1] * m[1][0]
xa = (m[0][2] * m[1][1] - m[0][1] * m[1][2]) / det; xb = (m[0][0] * m[1][2] - m[0][2] * m[1][0]) / det
ecken = {(0, 0): 0, (400, 0): dA * 400, (0, 350): dB * 350, (xa, xb): dA * xa + dB * xb}
assert (xa, xb) == (300, 200) and max(ecken.values()) == 18000 == ecken[(300, 200)]
aufgabe('kapazitaet', ['kapazitaet'], 'rechnen', 3, 'Welches Programm bei knappen Stunden?',
    '<p>Eine Tischlerei baut Tische (a) und Bänke (b). Ein Tisch bringt <b>40 €</b>, eine Bank <b>30 €</b> Deckungsbeitrag. '
    'Ein Tisch braucht 2 h an der Säge und 1 h in der Montage, eine Bank 1 h an der Säge und 2 h in der Montage. '
    'Im Monat stehen <b>800 h</b> Säge und <b>700 h</b> Montage zur Verfügung.</p>',
    [teil('Schreiben Sie die beiden Kapazitätsgrenzen als Ungleichungen.', 2, 'Stunden je Stück · Stückzahl ≤ verfügbare Stunden.',
          'Säge: 2a + 1b ≤ …', ol('Säge: <b>2a + b ≤ 800</b>', 'Montage: <b>a + 2b ≤ 700</b>', 'dazu a, b ≥ 0')),
     teil('Berechnen Sie den Schnittpunkt der beiden Grenzgeraden: Wie viele Tische?', 3, 'Setze beide Grenzen als Gleichungen gleich.',
          'Aus der ersten: b = 800 − 2a. In die zweite einsetzen.',
          ol('b = 800 − 2a', 'a + 2(800 − 2a) = 700 → −3a = −900', '<b>a = 300 Tische</b>, b = 200 Bänke'), xa, 'Tische'),
     teil('Wie hoch ist der Deckungsbeitrag im Schnittpunkt? Prüfen Sie die Eckpunkte.', 3,
          'Das Optimum liegt in einer Ecke des zulässigen Bereichs.', 'Ecken: (400 | 0), (0 | 350), (300 | 200).',
          ol('(400 | 0): 16.000 €', '(0 | 350): 10.500 €', '(300 | 200): 40 · 300 + 30 · 200 = <b>18.000 €</b> → Optimum'), 18000, '€')])

# ---------------------------------------------------------------- k2: Wertschöpfung, Effizienz
Um, Vl, Lo, Zi, St = 900000, 540000, 240000, 30000, 40000
WS = Um - Vl; Eig = WS - Lo - Zi - St
assert (WS, Eig) == (360000, 50000)
aufgabe('wertschoepfung', ['effizienz', 'kennzahlen'], 'rechnen', 2, 'Wer bekommt die Wertschöpfung?',
    f'<p>Eine Bäckereikette setzt im Jahr <b>{de(Um)} €</b> um. Für Mehl, Energie und andere Vorleistungen zahlt sie <b>{de(Vl)} €</b>. '
    f'An Löhnen zahlt sie {de(Lo)} €, an Zinsen {de(Zi)} €, an Steuern {de(St)} €.</p>',
    [teil('Berechnen Sie die Wertschöpfung.', 2, 'Was hat die Kette selbst hinzugefügt?', 'Umsatz − Vorleistungen.',
          ol('900.000 − 540.000 = <b>360.000 €</b>'), WS, '€'),
     teil('Wie viel bleibt den Eigentümern?', 2, 'Die Wertschöpfung wird an vier Gruppen verteilt.', 'Mitarbeiter, Fremdkapitalgeber, Staat; der Rest gehört den Eigentümern.',
          ol('360.000 − 240.000 − 30.000 − 40.000 = <b>50.000 €</b>'), Eig, '€'),
     teil('Die Kette stellt ihre Öfen so ein, dass sie 10 % weniger Strom brauchen, verkauft aber Brote, die niemand will. Beurteilen Sie Effizienz und Effektivität.', 3,
          '„Die Dinge richtig tun“ und „die richtigen Dinge tun“.', 'Was gehört zum Aufwand, was zum Ziel?',
          eh('Effizienz steigt: gleiches Ergebnis mit weniger Aufwand (die Dinge richtig tun). Effektivität fehlt: Das Ziel, verkaufbare Brote anzubieten, wird verfehlt (nicht die richtigen Dinge tun). Beides ist nötig.'))])

# ---------------------------------------------------------------- k3: Bogenelastizität und Effekte
p1, m1, p2, m2 = 20, 120, 16, 180
eps = abs(Fr(m2 - m1, Fr(m1 + m2, 2)) / Fr(p2 - p1, Fr(p1 + p2, 2)))
ME, PE = (m2 - m1) * p2, (p2 - p1) * m1; GE = p2 * m2 - p1 * m1
assert eps == Fr(9, 5) and (ME, PE, GE) == (960, -480, 480) and GE == ME + PE
aufgabe('bogenelastizitaet', ['mittelwert', 'elastizitaet', 'effekte'], 'rechnen', 3, 'Lohnt sich der günstigere Yogakurs?',
    f'<p>Ein Yogastudio verlangt <b>{p1} €</b> je Kurs und hat <b>{m1}</b> Teilnehmende im Monat. Nach einer Senkung auf <b>{p2} €</b> kommen <b>{m2}</b>.</p>',
    [teil('Berechnen Sie die Preiselastizität der Nachfrage mit der Mittelwertmethode (Betrag).', 4,
          'Relative Mengenänderung durch relative Preisänderung, jeweils bezogen auf den Mittelwert.',
          '\\(\\varepsilon = \\frac{60 / 150}{-4 / 18}\\)',
          ol('Mengenänderung: \\(\\frac{180 - 120}{150} = 0{,}4\\)', 'Preisänderung: \\(\\frac{16 - 20}{18} = -\\frac{2}{9}\\)',
             '\\(|\\varepsilon| = 0{,}4 \\cdot \\frac{9}{2} = \\) <b>1,8</b>'), float(eps), '', 0.01),
     teil('Deuten Sie das Ergebnis in einem Satz.', 2, 'Größer oder kleiner als 1?', 'Standardsatz: „Ändert sich der Preis um 1 %, …“',
          eh('Ändert sich der Preis um 1 %, ändert sich die Nachfrage um 1,8 %. Die Nachfrage ist elastisch (|ε| > 1).')),
     teil('Berechnen Sie Mengeneffekt, Preiseffekt und Gesamteffekt.', 4, 'ME mit dem neuen Preis, PE mit der alten Menge.',
          'ME = (M_neu − M_alt) · p_neu; PE = (p_neu − p_alt) · M_alt.',
          ol('ME = 60 · 16 = <b>960 €</b>', 'PE = −4 · 120 = <b>−480 €</b>', 'GE = 2.880 − 2.400 = <b>480 €</b> (= ME + PE)'), GE, '€'),
     teil('War die Preissenkung richtig? Begründen Sie mit der Elastizität.', 2, 'Welcher Effekt überwiegt?', 'Elastisch → Mengeneffekt überwiegt.',
          eh('Ja: Bei elastischer Nachfrage überwiegt der Mengeneffekt den Preiseffekt, der Erlös steigt um 480 €.'))])

# ---------------------------------------------------------------- k3: Punktelastizität, Marktgleichgewicht
da, db, sb = 1200, 4, 2       # D(p) = 1200 − 4p, S(p) = 2p
pg = Fr(da, db + sb); qg = da - db * pg; eg = Fr(db) * pg / qg
p_e1 = Fr(da, 2 * db)
assert (pg, qg, eg, p_e1) == (200, 400, 2, 150)
aufgabe('punktelastizitaet', ['punktelastizitaet', 'elastizitaet'], 'rechnen', 3, 'Elastizität im Marktgleichgewicht',
    '<p>Für Konzertkarten gilt die Nachfrage \\(D(p) = 1.200 - 4p\\) und das Angebot \\(S(p) = 2p\\).</p>',
    [teil('Berechnen Sie den Gleichgewichtspreis.', 2, 'Im Gleichgewicht ist Angebot gleich Nachfrage.', '\\(1.200 - 4p = 2p\\)',
          ol('\\(1.200 = 6p\\)', '<b>p = 200 €</b>'), float(pg), '€'),
     teil('Wie viele Karten werden im Gleichgewicht verkauft?', 1, 'Preis in eine der beiden Funktionen einsetzen.', '\\(S(200) = 2 \\cdot 200\\)',
          ol('<b>Q = 400 Karten</b>'), float(qg), 'Karten'),
     teil('Berechnen Sie die Punktelastizität der Nachfrage im Gleichgewicht (Betrag) und deuten Sie sie.', 3,
          '\\(\\varepsilon = \\frac{\\partial Q}{\\partial p} \\cdot \\frac{p}{Q}\\); ohne Angabe nimmt man die Nachfrage.', "\\(D^{\\prime}(p) = -4\\)",
          ol('\\(|\\varepsilon| = 4 \\cdot \\frac{200}{400} = \\) <b>2</b>', 'Elastisch: 1 % Preisänderung → 2 % Mengenänderung.'), float(eg), ''),
     teil('Bei welchem Preis ist die Nachfrage genau einheitselastisch?', 3, 'Setze |ε| = 1 und löse nach p.', '\\(4 \\cdot \\frac{p}{1.200 - 4p} = 1\\)',
          ol('\\(4p = 1.200 - 4p\\)', '<b>p = 150 €</b> (Mitte der Nachfragegeraden)'), float(p_e1), '€')])

# ---------------------------------------------------------------- k4: Opportunitätskosten
h, fi, ko = 10, 4, 6           # 10 h; pro Stunde 4 Fische oder 6 Kokosnüsse
ok_f = Fr(ko, fi); ziel_f = 20; std = Fr(ziel_f, fi); rest = (h - std) * ko
assert (ok_f, std, rest) == (Fr(3, 2), 5, 30)
aufgabe('opportunitaet', ['opportunitaet', 'grenznutzen'], 'rechnen', 2, 'Fische oder Kokosnüsse?',
    f'<p>Eine Schiffbrüchige hat am Tag <b>{h} Stunden</b> Licht. In einer Stunde fängt sie <b>{fi} Fische</b> oder sammelt <b>{ko} Kokosnüsse</b>.</p>',
    [teil('Wie hoch sind die Opportunitätskosten eines Fisches (in Kokosnüssen)?', 2, 'Worauf verzichtet sie für einen Fisch?',
          'In der Zeit für 4 Fische hätte sie 6 Kokosnüsse sammeln können.', ol('\\(\\frac{6}{4} = \\) <b>1,5 Kokosnüsse</b> je Fisch'), float(ok_f), 'Kokosnüsse'),
     teil('Sie will 20 Fische fangen. Wie viele Kokosnüsse kann sie dann noch sammeln?', 2, 'Wie viele Stunden kostet das Fischen?',
          '20 ÷ 4 = 5 Stunden.', ol('5 h Fischen, 5 h bleiben', '5 · 6 = <b>30 Kokosnüsse</b>'), float(rest), 'Kokosnüsse'),
     teil('Erklären Sie mit dem Grenznutzen, warum sie nicht den ganzen Tag nur fischt.', 3, 'Ist der 30. Fisch so viel wert wie der erste?',
          'Gesetz vom abnehmenden Grenznutzen.',
          eh('Jeder weitere Fisch stiftet weniger zusätzlichen Nutzen (abnehmender Grenznutzen), während die ersten Kokosnüsse einen hohen Nutzen hätten. Sie teilt die Zeit so auf, dass die letzte Stunde in beiden Tätigkeiten etwa gleich viel Nutzen bringt.'))])

# ---------------------------------------------------------------- k5: Shareholder Value
K5, i5, E5, A5 = 800000, 6, 1490000, 1450000
G5 = E5 - A5; r5 = G5 / K5 * 100; lat = K5 * i5 / 100
assert (G5, r5, lat) == (40000, 5, 48000)
aufgabe('shareholder', ['shareholder-value', 'stakeholder'], 'rechnen', 3, 'Schafft die Brauerei Wert?',
    f'<p>In einer Brauerei stecken <b>{de(K5)} €</b> Kapital der Eigentümer. Am Kapitalmarkt bekämen sie <b>{i5} %</b>. '
    f'Die Brauerei hat Erträge von {de(E5)} € und Aufwendungen von {de(A5)} €.</p>',
    [teil('Berechnen Sie die Rendite r der Brauerei.', 2, 'r = (E − A) ÷ K.', '40.000 ÷ 800.000.', ol('E − A = 40.000 €', '<b>r = 5 %</b>'), r5, '%'),
     teil('Wie hoch ist die Messlatte K · i? Schafft die Brauerei Wert im Sinne des Shareholder-Value-Ansatzes?', 3,
          'Vergleiche den Gewinn mit dem, was das Kapital anderswo bringen würde.', 'Bedingung: E − A ≥ K · i, also r ≥ i.',
          ol('K · i = 800.000 · 0,06 = <b>48.000 €</b>', '40.000 € < 48.000 € bzw. 5 % < 6 %', 'Obwohl ein Gewinn entsteht, wird Wert vernichtet.'), lat, '€'),
     teil('Ein Stakeholder-Vertreter sagt: „Aber die Brauerei sichert 30 Arbeitsplätze im Dorf.“ Stellen Sie beide Sichtweisen gegenüber.', 3,
          'Wessen Interessen zählen jeweils?', 'Shareholder: Eigentümer; Stakeholder: alle Anspruchsgruppen.',
          eh('Shareholder-Sicht: Die Eigentümer sollten ihr Kapital abziehen, weil es anderswo mehr bringt; niemand wird zur Mitarbeit gezwungen. Stakeholder-Sicht: Mitarbeiter, Gemeinde und Lieferanten haben ebenfalls berechtigte Ansprüche; der Betrieb soll alle Interessen ausgleichen.'))])

# ---------------------------------------------------------------- k6: Zielsystem mit mehreren Zielen
alt = {'Innenstadt': (60, 900), 'Bahnhof': (80, 600), 'Uni': (50, 500)}   # Fläche m², Passanten/h
w = (Fr(4, 10), Fr(6, 10))
mx = [max(v[j] for v in alt.values()) for j in (0, 1)]
nutz = {k: w[0] * Fr(v[0], mx[0]) + w[1] * Fr(v[1], mx[1]) for k, v in alt.items()}
assert nutz == {'Innenstadt': Fr(9, 10), 'Bahnhof': Fr(4, 5), 'Uni': Fr(7, 12)}
aufgabe('zielsystem', ['zielsystem', 'zielbeziehungen'], 'rechnen', 3, 'Welcher Laden für das Eiscafé?',
    '<p>Ein Eiscafé wählt zwischen drei Läden. Ziele: möglichst viel <b>Fläche</b> und möglichst viele <b>Passanten</b>.</p>'
    '<table class="tbl"><tr><th>Laden</th><th>Fläche (m²)</th><th>Passanten je Stunde</th></tr>'
    + ''.join(f'<tr><td>{k}</td><td>{v[0]}</td><td>{v[1]}</td></tr>' for k, v in alt.items()) + '</table>',
    [teil('Welche Läden sind effizient? Begründen Sie.', 2, 'Gibt es einen Laden, der in beiden Zielen schlechter ist als ein anderer?',
          'Vergleiche Uni mit Innenstadt und Bahnhof.',
          ol('Uni ist in beiden Zielen schlechter als die Innenstadt → ineffizient (dominiert).', 'Innenstadt und Bahnhof sind <b>effizient</b>: Jeder ist in einem Ziel besser.')),
     teil('Welcher Laden wird gewählt, wenn die Passanten lexikographisch zuerst kommen?', 1, 'Erst nur nach dem wichtigsten Ziel entscheiden.',
          'Nur bei Gleichstand zählt das zweite Ziel.', ol('Meiste Passanten: <b>Innenstadt</b> (900)')),
     teil('Normieren Sie, indem Sie jeden Wert durch den höchsten Wert des Ziels teilen, und gewichten Sie Fläche mit 0,4 und Passanten mit 0,6. Welcher Nutzen ergibt sich für die Innenstadt?', 4,
          'Höchste Fläche 80, höchste Passantenzahl 900.', 'Innenstadt: 0,4 · 60/80 + 0,6 · 900/900.',
          ol('Innenstadt: 0,4 · 0,75 + 0,6 · 1 = <b>0,9</b>', 'Bahnhof: 0,4 · 1 + 0,6 · 0,667 = 0,8', 'Uni: 0,4 · 0,625 + 0,6 · 0,556 ≈ 0,58', 'Gewählt: Innenstadt'), 0.9, '', 0.01),
     teil('Erklären Sie, warum man vor dem Gewichten normieren muss.', 2, 'Was passiert, wenn man m² und Passanten einfach addiert?',
          'Einheiten und Größenordnungen.', eh('Die Ziele haben verschiedene Einheiten und Größenordnungen (m² gegen Hunderte Passanten). Ohne Normierung würde das Ziel mit den größeren Zahlen das Ergebnis allein bestimmen, egal wie es gewichtet ist.'))])

# ---------------------------------------------------------------- k7: Entscheidungsregeln
M = {'a1': (40, 70, 100), 'a2': (60, 60, 70), 'a3': (20, 90, 120)}
pz = (Fr(3, 10), Fr(5, 10), Fr(2, 10)); lam = Fr(2, 5)
mm_ = {k: min(v) for k, v in M.items()}; mx_ = {k: max(v) for k, v in M.items()}
hw = {k: lam * mx_[k] + (1 - lam) * mm_[k] for k in M}
best = [max(v[j] for v in M.values()) for j in range(3)]
sav = {k: max(best[j] - v[j] for j in range(3)) for k, v in M.items()}
lap = {k: Fr(sum(v), 3) for k, v in M.items()}
bay = {k: sum(pz[j] * v[j] for j in range(3)) for k, v in M.items()}
assert mm_ == {'a1': 40, 'a2': 60, 'a3': 20} and hw == {'a1': 64, 'a2': 64, 'a3': 60}
assert sav == {'a1': 20, 'a2': 50, 'a3': 40} and bay == {'a1': 67, 'a2': 62, 'a3': 75}
assert lap == {'a1': 70, 'a2': Fr(190, 3), 'a3': Fr(230, 3)}
tab = '<table class="tbl"><tr><th></th><th>z1</th><th>z2</th><th>z3</th></tr>' + ''.join(
    f'<tr><td>{k}</td>' + ''.join(f'<td>{x}</td>' for x in v) + '</tr>' for k, v in M.items()) + '</table>'
aufgabe('entscheidungsregeln', ['maximin', 'hurwicz', 'savage-niehans', 'laplace', 'bayes'], 'rechnen', 3, 'Drei Regeln, drei Antworten',
    '<p>Ein Festivalveranstalter wählt zwischen drei Bühnenkonzepten a1–a3. Der Gewinn (in Tausend €) hängt vom Wetter ab (z1 Regen, z2 wechselhaft, z3 Sonne):</p>' + tab,
    [teil('Welche Alternative wählt die Maximin-Regel?', 2, 'Für jede Alternative das schlechteste Ergebnis.', 'Minima: 40, 60, 20.',
          ol('Zeilenminima: a1 = 40, a2 = 60, a3 = 20', 'Größtes Minimum: <b>a2</b>')),
     teil('Berechnen Sie den Hurwicz-Wert von a1 mit λ = 0,4.', 3, 'Φ = λ · Maximum + (1 − λ) · Minimum.', '0,4 · 100 + 0,6 · 40.',
          ol('a1: 0,4 · 100 + 0,6 · 40 = 40 + 24 = <b>64</b>', 'a2: 0,4 · 70 + 0,6 · 60 = 64; a3: 0,4 · 120 + 0,6 · 20 = 60', 'a1 und a2 gleichauf'), 64, 'T€'),
     teil('Welche Alternative wählt die Savage-Niehans-Regel? Wie groß ist ihr maximales Bedauern?', 4,
          'Bedauern = bestes Ergebnis im Zustand − eigenes Ergebnis.', 'Spaltenbeste: 60, 90, 120.',
          ol('Bedauern a1: 20, 20, 20 → max 20', 'a2: 0, 30, 50 → max 50', 'a3: 40, 0, 0 → max 40', 'Kleinstes Maximum: <b>a1 mit 20</b>'), 20, 'T€'),
     teil('Die Wahrscheinlichkeiten sind 0,3 / 0,5 / 0,2. Welche Alternative wählt die Bayes-Regel, und mit welchem Erwartungswert?', 3,
          'E = Σ p · e für jede Zeile.', 'a3: 0,3 · 20 + 0,5 · 90 + 0,2 · 120.',
          ol('a1: 12 + 35 + 20 = 67', 'a2: 18 + 30 + 14 = 62', 'a3: 6 + 45 + 24 = <b>75</b> → a3'), 75, 'T€')])

# ---------------------------------------------------------------- k8: Verhaltenswissenschaft (Transfer)
aufgabe('prospect', ['prospect-theory', 'begrenzte-rationalitaet', 'homo-oeconomicus'], 'transfer', 3, 'Warum hält Jonas an seiner Aktie fest?',
    '<p>Jonas hat Aktien für 5.000 € gekauft, sie sind nur noch 3.000 € wert. Er verkauft nicht, „weil der Verlust sonst echt wäre“. '
    'Eine andere Aktie, die von 5.000 € auf 6.000 € gestiegen ist, verkauft er sofort. Beim Kauf hatte er „ein gutes Gefühl“ und keine Zahlen verglichen.</p>',
    [teil('Erklären Sie sein Verhalten mit der Prospect Theory.', 4, 'Wie verhalten sich Menschen bei Gewinnen und bei Verlusten?',
          'Risikoscheu bei Gewinnen, risikofreudig bei Verlusten; Verluste wiegen schwerer.',
          eh('Bei Gewinnen ist Jonas risikoscheu und sichert ihn sofort. Im Verlustbereich ist er risikofreudig und pokert auf Erholung, weil Verluste schwerer wiegen als gleich große Gewinne (Verlustaversion). Bezugspunkt ist der Kaufpreis.')),
     teil('Welcher weitere Effekt steckt in „der Verlust wäre sonst echt“? Ordnen Sie ein.', 2, 'Das Geld ist schon weg, egal wie er entscheidet.',
          'Versunkene Kosten.', eh('Sunk-Cost-Effekt: Bereits verlorenes Geld beeinflusst die Entscheidung, obwohl es nicht zurückkommt. Rational zählt nur die Zukunft.')),
     teil('Warum widerspricht der Kauf „nach Gefühl“ dem homo oeconomicus? Welches Konzept beschreibt ihn besser?', 3,
          'Was nimmt der homo oeconomicus über Informationen an?', 'Simon: begrenzte Rationalität.',
          eh('Der homo oeconomicus kennt alle Alternativen und maximiert seinen Nutzen. Jonas hat weder Informationen gesammelt noch verglichen. Er ist begrenzt rational: Er nimmt die erste zufriedenstellende Lösung.'))], klausur=False)

# ---------------------------------------------------------------- k9: Five Forces (Anwendung)
aufgabe('five-forces', ['five-forces', 'markteintritt', 'verhandlungsmacht', 'umweltanalyse'], 'anwendung', 3, 'Branchenanalyse: Bubble Tea in der Innenstadt',
    '<p>In einer Innenstadt gibt es fünf Bubble-Tea-Läden. Die Tapiokaperlen kommen von nur einem Großhändler. Ein Laden lässt sich mit 40.000 € eröffnen. '
    'Kundinnen wechseln je nach Laune zu Kaffee, Smoothies oder Eistee. Über eine App vergleichen sie Preise in Sekunden.</p>',
    [teil('Ordnen Sie jede Angabe einer der fünf Wettbewerbskräfte nach Porter zu.', 5, 'Fünf Kräfte: Rivalität, neue Anbieter, Substitute, Lieferanten, Kunden.',
          'Jeder Satz im Fall passt zu genau einer Kraft.',
          ol('Fünf Läden: <b>Rivalität</b> unter bestehenden Wettbewerbern hoch', 'Ein Großhändler: <b>Verhandlungsmacht der Lieferanten</b> hoch',
             '40.000 € Eröffnung: niedrige Markteintrittsbarriere → <b>Bedrohung durch neue Anbieter</b> hoch',
             'Kaffee, Smoothies: <b>Bedrohung durch Substitute</b> hoch', 'App-Preisvergleich: <b>Verhandlungsmacht der Kunden</b> hoch')),
     teil('Wie attraktiv ist die Branche? Begründen Sie in zwei Sätzen.', 2, 'Je stärker die Kräfte, desto …', 'Starke Kräfte drücken den Gewinn.',
          eh('Unattraktiv: Alle fünf Kräfte sind stark, sie drücken Preise und Margen. Dauerhaft hohe Gewinne sind kaum zu erwarten.')),
     teil('Nennen Sie zwei Markteintrittsbarrieren, die ein Laden selbst aufbauen könnte.', 2, 'Vertrauens-, politische und wirtschaftliche Barrieren.',
          'z. B. Stammkunden, Größenvorteile.', eh('z. B. Treueprogramm/Stammkunden (Vertrauensbarriere, Käuferpfadabhängigkeit), Einkauf für mehrere Filialen (Economies of Scale), exklusive Lage oder Vertriebskanal.'))])

# ---------------------------------------------------------------- k10: Erfahrungskurve und BCG
k0, lr = 100, Fr(8, 10); kum = [10000, 20000, 40000]
kst = [k0 * lr ** i for i in range(3)]
assert kst == [100, 80, 64]
prod = {'Classic': (2, Fr(16, 10)), 'Vegan': (18, Fr(4, 10)), 'Kids': (15, Fr(25, 10)), 'Light': (1, Fr(3, 10))}
quad = {k: ('Star' if wg >= 10 and rm >= 1 else 'Question Mark' if wg >= 10 else 'Cash Cow' if rm >= 1 else 'Poor Dog') for k, (wg, rm) in prod.items()}
assert quad == {'Classic': 'Cash Cow', 'Vegan': 'Question Mark', 'Kids': 'Star', 'Light': 'Poor Dog'}
aufgabe('erfahrung-bcg', ['erfahrungskurve', 'bcg-matrix', 'lebenszyklus'], 'anwendung', 3, 'Müsli-Hersteller: Kosten und Portfolio',
    '<p>Ein Müsli-Hersteller hat bisher <b>10.000 Tonnen</b> produziert, die Stückkosten liegen bei <b>100 € je Tonne</b>. '
    'Je Verdopplung der kumulierten Menge sinken die Stückkosten um <b>20 %</b>. Sein Portfolio (Grenze Marktwachstum 10 %, relativer Marktanteil 1):</p>'
    '<table class="tbl"><tr><th>Produkt</th><th>Marktwachstum</th><th>relativer Marktanteil</th></tr>'
    + ''.join(f'<tr><td>{k}</td><td>{wg} %</td><td>{de(float(rm))}</td></tr>' for k, (wg, rm) in prod.items()) + '</table>',
    [teil('Wie hoch sind die Stückkosten nach 40.000 Tonnen kumulierter Menge?', 3, 'Wie oft verdoppelt sich die Menge von 10.000 auf 40.000?',
          'Zweimal; jedes Mal · 0,8.', ol('10.000 → 20.000: 100 · 0,8 = 80 €', '20.000 → 40.000: 80 · 0,8 = <b>64 €</b>'), 64, '€'),
     teil('Ordnen Sie die vier Produkte in die BCG-Matrix ein.', 4, 'Hohes Wachstum + hoher Anteil = ?', 'Zwei Achsen: Marktwachstum (oben hoch), relativer Marktanteil (≥ 1 hoch).',
          ol('Classic: <b>Cash Cow</b>', 'Vegan: <b>Question Mark</b>', 'Kids: <b>Star</b>', 'Light: <b>Poor Dog</b>')),
     teil('Leiten Sie je eine Normstrategie ab und erklären Sie, wie die Erfahrungskurve das Portfolio verbindet.', 4,
          'Investieren, abschöpfen, alles oder raus, beenden.', 'Wer den größten Marktanteil hat, ist auf der Erfahrungskurve am weitesten.',
          eh('Kids investieren, Classic abschöpfen, Vegan: alles investieren oder raus, Light beenden. Hoher relativer Marktanteil heißt hohe kumulierte Menge, also niedrigere Stückkosten als die Konkurrenz; Cash Cows liefern so das Geld für Stars und Question Marks.'))])

# ---------------------------------------------------------------- k11: Strategiewahl (Anwendung)
aufgabe('strategie', ['ansoff', 'porter-strategien', 'swot'], 'anwendung', 2, 'Wie wächst die Fahrradmanufaktur?',
    '<p>Eine kleine Fahrradmanufaktur baut handgefertigte Stahlräder für Kunden in Deutschland. Sie überlegt: (1) mehr Werbung bei bestehenden Kunden, '
    '(2) dieselben Räder in Skandinavien verkaufen, (3) ein E-Lastenrad für die bisherigen Kunden entwickeln, (4) eine Kaffeebar eröffnen. '
    'Ihre Räder sind teurer als Massenware, dafür langlebig und individuell.</p>',
    [teil('Ordnen Sie die vier Optionen der Ansoff-Matrix zu.', 4, 'Zwei Fragen: Neues Produkt? Neuer Markt?', 'Alt/alt, alt/neu, neu/alt, neu/neu.',
          ol('(1) <b>Marktdurchdringung</b>', '(2) <b>Marktentwicklung</b>', '(3) <b>Produktentwicklung</b>', '(4) <b>Diversifikation</b> (höchstes Risiko)')),
     teil('Welche Wettbewerbsstrategie nach Porter verfolgt die Manufaktur? Begründen Sie.', 2, 'Preis oder Besonderheit? Ganzer Markt oder Teilmarkt?',
          'Teurer, aber besonders, kleine Zielgruppe.', eh('Differenzierung in einer Nische (Fokus): Sie bietet etwas Besonderes für eine kleine Zielgruppe statt niedriger Preise für alle.')),
     teil('Nennen Sie je eine Stärke und eine Bedrohung im Sinne einer SWOT-Analyse.', 2, 'Stärken sind intern, Bedrohungen kommen von außen.',
          'Unternehmen ↔ Umwelt.', eh('Stärke: Handarbeit, Langlebigkeit, Individualität. Bedrohung: günstige E-Bikes großer Hersteller, steigende Stahlpreise.'))], klausur=False)

# ---------------------------------------------------------------- k12: Rechtsformen (Fall mit Zahlen)
schuld, priv_t, ein_k = 200000, 250000, 30000
aufgabe('rechtsform', ['rechtsform-fall', 'kg', 'gmbh', 'personengesellschaften'], 'anwendung', 3, 'Wer zahlt die Schulden?',
    f'<p>Tom und Mia betreiben einen Fahrradladen. Der Laden hat <b>{de(schuld)} €</b> Schulden, das Geschäftsvermögen ist aufgebraucht. '
    f'Tom hat privat {de(priv_t)} €, Mia hat {de(ein_k)} € eingebracht.</p>',
    [teil('Der Laden ist eine OHG. Wer haftet und womit?', 3, 'Wie haften OHG-Gesellschafter?', 'Unbeschränkt, unmittelbar, gesamtschuldnerisch.',
          eh('Beide haften unbeschränkt mit ihrem gesamten Privatvermögen. Die Gläubiger dürfen sich aussuchen, bei wem sie die vollen 200.000 € holen, z. B. bei Tom, der das Geld hat. Tom kann sich danach einen Teil von Mia zurückholen.')),
     teil('Der Laden ist eine KG, Tom ist Komplementär, Mia Kommanditistin. Wie viel kann Mia höchstens verlieren?', 2, 'Kommanditisten haften nur …',
          'mit ihrer Einlage.', ol('Mia haftet nur mit ihrer Einlage: <b>30.000 €</b>', 'Tom haftet unbeschränkt mit seinem Privatvermögen.'), ein_k, '€'),
     teil('Der Laden ist eine GmbH mit dem Mindeststammkapital. Was verlieren die beiden höchstens, und wie hoch ist das Mindeststammkapital?', 3,
          'Wer haftet bei einer Kapitalgesellschaft?', 'Die GmbH selbst haftet mit ihrem Vermögen.',
          ol('Mindeststammkapital: <b>25.000 €</b>', 'Die GmbH haftet mit dem Gesellschaftsvermögen; die Gesellschafter verlieren nur ihre Einlage, ihr Privatvermögen bleibt geschützt.'), 25000, '€'),
     teil('Empfehlen Sie Tom und Mia eine Rechtsform, wenn Mia nicht mitarbeiten, aber mitverdienen will und Tom den Laden allein führen möchte.', 2,
          'Wer leitet, wer gibt nur Geld?', 'Eine Personengesellschaft mit zwei Arten von Gesellschaftern.',
          eh('KG: Tom als Komplementär leitet und haftet voll, Mia als Kommanditistin gibt Kapital, leitet nicht und haftet nur mit ihrer Einlage.'))])

# ---------------------------------------------------------------- k1: Betrieb (Anwendung)
aufgabe('betrieb', ['betrieb', 'leistungsart', 'dienstleistung', 'betriebszweck'], 'anwendung', 1, 'Was ist ein Friseursalon für ein Betrieb?',
    '<p>Ein Friseursalon hat drei Angestellte, zwei Stühle, Föhne und Scheren. Er kauft Shampoo und Farbe ein und verkauft auch Pflegeprodukte. '
    'Die Inhaberin will Gewinn erzielen.</p>',
    [teil('Ordnen Sie die Produktionsfaktoren zu.', 3, 'Arbeit, Betriebsmittel, Werkstoffe.', 'Was wird verbraucht, was nur genutzt?',
          ol('Arbeit: drei Angestellte, Inhaberin', 'Betriebsmittel: Stühle, Föhne, Scheren', 'Werkstoffe: Shampoo, Farbe')),
     teil('Begründen Sie, warum der Haarschnitt eine Dienstleistung ist, mit dem Uno-actu-Prinzip.', 2, 'Kann man einen Haarschnitt auf Lager legen?',
          'Produktion und Konsum fallen zusammen.', eh('Der Haarschnitt wird im selben Moment erstellt und verbraucht (uno actu), der Kunde muss anwesend sein. Er ist nicht lagerbar.')),
     teil('Ordnen Sie den Salon nach dem Betriebszweck ein.', 1, 'Wessen Bedarf wird gedeckt, und mit welchem Ziel?', 'Fremdbedarfsdeckung, Gewinnziel.',
          eh('Privates Unternehmen (Fremdbedarfsdeckung mit Gewinnziel), kein Haushalt.'))], klausur=False)

ids = {t['id'] for k in json.load(open(ROOT / 'inhalte/bwl/fach.json'))['kapitel'] for t in k['themen']}
for a in A:
    assert set(a['unter']) <= ids, (a['id'], set(a['unter']) - ids)
(ROOT / 'inhalte/bwl/aufgaben.json').write_text(json.dumps({'hinweis': 'Große Aufgaben: gemeinsame Ausgangslage, Teilaufgaben mit Punkten, zwei Tipps, Lösungsweg. Zahlen in werkzeuge/bwl/aufgaben.py gerechnet.', 'aufgaben': A}, ensure_ascii=False, indent=1))
kap = {k['id']: {t['id'] for t in k['themen']} for k in json.load(open(ROOT / 'inhalte/bwl/fach.json'))['kapitel']}
ohne = [k for k, s in kap.items() if not any(set(a['unter']) & s for a in A)]
print(f'bwl: {len(A)} große Aufgaben; Oberthemen ohne Aufgabe: {ohne}')
