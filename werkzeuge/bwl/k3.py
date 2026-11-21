import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *

# Durchgehendes Beispiel: das Parkhaus „Am Wasserturm“ mit 100 Plätzen (Preis je Tag, belegte Plätze).


def nachfragekurve(titel, art, text):
    """kleines Bild einer Nachfragekurve (für die Umschalt-Tafeln)"""
    X = lambda m: 50 + m * 2.6
    Y = lambda p: 200 - p * 30
    s = achsen(50, 200, 330, 14, 'Menge', 'Preis')
    if art == 0:
        s += linie([(X(40), Y(0.2)), (X(40), Y(5.8))], 'var(--primary)', 3)
    elif art == 4:
        s += linie([(X(0), Y(3)), (X(100), Y(3))], 'var(--primary)', 3)
    else:
        k = {1: 0.25, 2: 1.0, 3: 2.6}[art]
        s += kurve(lambda m: 4 * (60 / m) ** (1 / k), 60 * (4 / 5.8) ** k, min(105, 60 * (4 / 0.6) ** k), X, Y, farbe='var(--primary)', w=3)
    s += T(190, 234, text, 13, 700, 'middle', 'var(--primary)')
    return svg(360, 246, T(352, 26, titel, 14, 800, 'end') + s, titel, maxw=420)


fig_skala = svg(360, 214,
    linie([(24, 70), (336, 70)], 'var(--axis)', 2.5)
    + punkt(24, 70, 'var(--c3)', 7) + punkt(150, 70, 'var(--primary)', 7) + T(338, 76, '∞', 22, 700, 'start')
    + T(24, 48, '0', 15, 800) + T(150, 48, '1', 15, 800)
    + tpg(rechteck(4, 88, 40, 44, 'var(--pale)', 'var(--line)') + T(24, 110, '= 0', 13, 700), 'Völlig unelastisch (ε = 0): Die Nachfrage ändert sich nie, egal wie stark der Preis steigt. Beispiel: lebenswichtiges Medikament.')
    + tpg(rechteck(48, 88, 96, 44, 'var(--pale)', 'var(--line)') + T(96, 110, 'unelastisch', 13, 700), 'Unelastisch (0 < ε < 1): Die Menge reagiert schwächer als der Preis. Beispiele: Brot 0,25, Milch 0,3, Benzin 0,4.')
    + tpg(rechteck(156, 88, 200, 44, 'var(--pale)', 'var(--line)') + T(256, 110, 'elastisch', 13, 700), 'Elastisch (ε > 1): Die Menge reagiert stärker als der Preis. Beispiele: Möbel 3,04, spezielle Automarken 4,0. Es gibt Alternativen.')
    + pfeil(150, 78, 150, 150)
    + tpg(rechteck(80, 152, 140, 50, 'var(--primary)', 'var(--primary)') + T(150, 170, '= 1', 14, 800, 'middle', 'var(--on-primary)') + T(150, 189, 'einheitselastisch', 12, 600, 'middle', 'var(--on-primary)'), 'Einheitselastisch (ε = 1): Die Menge ändert sich um genau so viel Prozent wie der Preis.')
    + pfeil(338, 86, 338, 150)
    + tpg(rechteck(236, 152, 120, 50, 'var(--pale)', 'var(--line)') + T(296, 170, '→ ∞', 14, 800) + T(296, 189, 'völlig elastisch', 12, 600), 'Völlig elastisch (ε → ∞): Über einem bestimmten Preis kauft niemand mehr, darunter beliebig viel.'),
    'Wertebereiche der Preiselastizität', maxw=420)

t_begriff = thema('elastizitaet', 'Preiselastizität: Was sie misst und wovon sie abhängt', star=True,
    kern='Die Preiselastizität der Nachfrage misst, um wie viel Prozent sich die Nachfragemenge ändert, wenn sich der Preis um ein Prozent ändert. Unter 1 heißt unelastisch, über 1 elastisch.',
    kurz=p('Das Parkhaus am Wasserturm erhöht den Tagespreis. Bleiben die Autos trotzdem da, reagiert die Nachfrage <b>unelastisch</b>. Fahren viele zum Parkhaus nebenan, reagiert sie <b>elastisch</b>. Die <b>Preiselastizität</b> sagt genau, wie stark.')
        + p('Einstieg aus der Vorlesung: Steigt der Preis für Haferflocken um 10 % und sinkt die gekaufte Menge um 20 %, dann ist \\(\\varepsilon = \\frac{-20\\,\\%}{+10\\,\\%} = |-2| = 2\\). <b>Standardsatz</b>: „Ändert sich der Preis um 1 %, ändert sich die Nachfrage um 2 %.“ Das ist elastisch.'),
    fig=fw('Die Wertebereiche. Tippe auf die Bereiche.') + bild(fig_skala),
    figcap='nach Folie „Elastizität: Definitionsbereich, Konvention“',
    article=h3('Definition und Formel')
        + p('„Ein Maß für die Stärke, mit der die Nachfragemenge eines Gutes auf Änderungen seines Preises reagiert. Berechnet als Quotient von prozentualer Mengenänderung und prozentualer Preisänderung.“ Allgemein: die relative Änderung einer abhängigen Variable (Menge) auf eine relative Änderung einer unabhängigen Variable (Preis).')
        + fx('Preiselastizität der Nachfrage', r'\varepsilon = \left| \frac{\text{prozentuale Änderung der Nachfragemenge}}{\text{prozentuale Preisänderung}} \right|',
             'Prozent Mengenänderung geteilt durch Prozent Preisänderung. Weil Preis und Menge fast immer in entgegengesetzte Richtung laufen, ist der Quotient negativ; man gibt den <b>Betrag</b> an.',
             r'\(\left|\frac{-20\,\%}{+10\,\%}\right| = 2\)')
        + p('Diese Formel ist „formal wichtig“: Sie ist der Ausgangspunkt für alle Rechenmethoden. Welche Prozente man nimmt, legen die Methoden fest: <b>Mittelwertmethode</b> (Bogenelastizität) und <b>Punktelastizität</b>. Beides folgt in den nächsten Unterthemen.')
        + weiter('Wie liest man das Ergebnis? Es gibt feste Bereiche.')
        + h3('Wertebereiche und Standardsatz')
        + tabelle(['Wert', 'Bezeichnung', 'Bedeutung'], [
            ['ε = 0', 'völlig unelastisch', 'Die Nachfrage ändert sich nie, egal wie stark der Preis steigt.'],
            ['0 < ε < 1', 'unelastisch', 'Die Menge ändert sich prozentual weniger als der Preis.'],
            ['ε = 1', 'einheitselastisch', 'Preisanstieg und Nachfragerückgang sind prozentual gleich.'],
            ['ε > 1', 'elastisch (überproportional)', 'Die Menge ändert sich prozentual stärker als der Preis.'],
            ['ε → ∞', 'völlig elastisch', 'Über einem Preis kauft niemand mehr, darunter beliebig viel.']])
        + p('<b>Standardsatz</b> für jede Antwort: „Ändert sich der Preis um 1 %, dann ändert sich die Nachfrage um ε %.“ Bei ε = 0,6: um 0,6 %, also <b>unelastisch</b>.')
        + klausur_hinweis('Typische Auswahlfrage: „Wenn ε = 0,6 ist, dann …“ → unelastisch: Die Menge reagiert schwächer als der Preis. Und: „Elastizität ist …“ → das Maß für die Stärke der Mengenreaktion auf eine Preisänderung.')
        + weiter('Warum reagieren manche Güter stark und andere kaum?')
        + h3('Wovon die Elastizität abhängt')
        + cards([('Substitutionsfähigkeit', 'Gibt es Alternativen? Dann ist man preissensibel, die Nachfrage ist elastisch. Mehrere Anbieter, Parkhaus nebenan.'),
                 ('Verfügbares Einkommen', 'Macht das Gut einen großen Teil des Budgets aus, achtet man auf den Preis.'),
                 ('Zeit', 'Kurzfristig ist man oft nicht preissensibel, langfristig sucht man Alternativen: Die Nachfrage wird elastischer.'),
                 ('Not, Dringlichkeit', 'Wie groß ist das Bedürfnis? Medikamente, Benzin oder bei Sucht: unelastisch.')])
        + tabelle(['Produkt', 'Preiselastizität'], [['Brot', '0,25'], ['Milch', '0,3'], ['Tabak', '0,4'], ['Treibstoff', '0,4'], ['Wein', '0,6'], ['Schuhe', '0,7'], ['Kino', '0,9'], ['Unterhaltung', '1,4'], ['Autos', '1,9'], ['Möbel', '3,04'], ['spezielle Automarken', '4,0']])
        + p('Auffällig: <b>Luxusautos</b> sind weniger elastisch als „normale“ spezielle Automarken, weil die Käufer viel Geld haben und der Preis für sie kaum eine Rolle spielt.')
        + weiter('Wie sieht das in einer Grafik aus? Je flacher die Nachfragekurve, desto elastischer.')
        + h3('Fünf Formen der Nachfragekurve')
        + tafeln('tf-nf', ['ε = 0', 'ε < 1', 'ε = 1', 'ε > 1', 'ε → ∞'], [
            nachfragekurve('Völlig unelastisch', 0, 'Preis steigt um 22 %, Menge bleibt 100'),
            nachfragekurve('Unelastisch', 1, 'Preis +22 % → Menge −11 %'),
            nachfragekurve('Einheitselastisch', 2, 'Preis +22 % → Menge −22 %'),
            nachfragekurve('Elastisch', 3, 'Preis +22 % → Menge −67 %'),
            nachfragekurve('Völlig elastisch', 4, 'über 4 €: null, unter 4 €: unendlich')])
        + falle('Steilheit und Elastizität gleichsetzen ist nur eine Faustregel. Auf einer geraden Nachfragekurve ist die Elastizität an jeder Stelle anders (siehe Punktelastizität).')
        + wahr('w-el', [('Bei ε = 0,6 ist die Nachfrage elastisch.', False, 'Unter 1 ist sie unelastisch.'),
                        ('Gibt es viele Alternativen, ist die Nachfrage eher elastisch.', True, 'Man kann ausweichen.'),
                        ('Langfristig ist die Nachfrage meist elastischer als kurzfristig.', True, 'Mit der Zeit sucht man Alternativen.'),
                        ('Medikamente haben typischerweise eine hohe Preiselastizität.', False, 'Hohe Not: unelastisch.')]),
    merk='ε = |%-Änderung Menge ÷ %-Änderung Preis|. 0 völlig unelastisch, < 1 unelastisch, = 1 einheitselastisch, > 1 elastisch, ∞ völlig elastisch. Standardsatz: Preis +1 % → Nachfrage ändert sich um ε %. Einfluss: Substitute, Einkommen, Zeit, Not.',
    exam='Elastizität deuten (ε = 0,6 → unelastisch), Standardsatz formulieren, Einflussfaktoren und Grafiken zuordnen.',
    fehler=['Das Minuszeichen stehen lassen. In der Klausur immer den Betrag angeben.', 'Unelastisch und elastisch an der Grenze 1 vertauschen.'],
    src='Folien 49–51, 56–60')

# ---------------------------------------------------------------- Mittelwertmethode (Rechner)
t_mw = thema('mittelwert', 'Mittelwertmethode (Bogenelastizität)', star=True, wide=True,
    kern='Die Mittelwertmethode teilt die Änderungen durch den Mittelwert aus altem und neuem Wert. So kommt in beide Richtungen dasselbe Ergebnis heraus. Man nimmt sie, wenn zwei Punkte (Preis und Menge vorher und nachher) gegeben sind.',
    kurz=p('Das Parkhaus hatte bisher 50 von 100 Plätzen zu 12 € belegt. Nach einer Preissenkung auf 9 € stehen dort 80 Autos. Wie elastisch ist die Nachfrage?')
        + p('Die Mittelwertmethode rechnet die Mengen- und die Preisänderung in Prozent vom <b>Mittelwert</b>: Mengen 30 von 65 und Preis 3 von 10,5. Ergebnis: ε ≈ 1,62, also <b>elastisch</b>. Ändert sich der Preis um 1 %, ändert sich die Nachfrage um etwa 1,62 %.'),
    fig=fw('Rechner: Stell Preis und Menge vorher und nachher ein. Die Karten zeigen den Rechenweg wie auf Papier.')
        + regler([('mwP1', 'Preis vorher', 1, 20, 0.5, 12, '€'), ('mwP2', 'Preis nachher', 1, 20, 0.5, 9, '€'), ('mwM1', 'Menge vorher', 10, 200, 5, 50, 'Stück'), ('mwM2', 'Menge nachher', 10, 200, 5, 80, 'Stück')])
        + '<svg id="figMW" viewBox="0 0 360 230" style="max-width:420px;width:100%;margin:0 auto;display:block" role="img" aria-label="Zwei Punkte auf der Nachfragekurve"></svg>'
        + schritte_karten([('① Mengenänderung in %', 'mwR1', '#mwT1'), ('② Preisänderung in %', 'mwR2', '#mwT2'), ('③ Elastizität', 'mwR3', '#mwT3')]),
    figcap='Klausurbeispiel Parkhaus: 50 Plätze zu 12 €, nach Preissenkung 80 Plätze zu 9 €',
    article=h3('Die Formel')
        + fx('Mittelwertmethode', r'\varepsilon = \left| \frac{\dfrac{M_2 - M_1}{\frac{M_2 + M_1}{2}}}{\dfrac{p_2 - p_1}{\frac{p_2 + p_1}{2}}} \right|',
             'Oben: Mengenänderung geteilt durch die mittlere Menge. Unten: Preisänderung geteilt durch den mittleren Preis. Dann den Betrag nehmen. M<sub>1</sub>, p<sub>1</sub> = vorher; M<sub>2</sub>, p<sub>2</sub> = nachher.',
             r'Parkhaus: \(\frac{30/65}{-3/10{,}5} = \frac{0{,}4615}{-0{,}2857} \approx -1{,}62\), also \(\varepsilon \approx 1{,}62\)',
             'Rechnet man Prozente immer vom alten Wert, kommt bei einer Preissenkung etwas anderes heraus als bei derselben Preiserhöhung zurück. Mit dem Mittelwert als Bezug ist das Ergebnis in beide Richtungen gleich.')
        + p('Tipp fürs Kopfrechnen: Die „÷ 2“ im Mittelwert kürzen sich oben und unten weg. Man kann also auch rechnen: \\(\\varepsilon = \\left|\\frac{M_2 - M_1}{M_2 + M_1} \\div \\frac{p_2 - p_1}{p_2 + p_1}\\right|\\).')
        + bsp('Folienbeispiel', 'A: p = 4 €, Nachfrage 120. B: p = 6 €, Nachfrage 80.',
              [(r'Menge: \(\frac{80 - 120}{(80 + 120)/2} = \frac{-40}{100} = -0{,}4\)', '−40 %'), (r'Preis: \(\frac{6 - 4}{(6 + 4)/2} = \frac{2}{5} = 0{,}4\)', '+40 %'), (r'\(\varepsilon = \left|\frac{-0{,}4}{0{,}4}\right|\)', '1')],
              'Wenn sich der Preis um 40 % ändert, ändert sich die Nachfrage um 40 %: einheitselastisch.')
        + bsp('Shishabar (Kopfrechnen)', 'Ein Tabak kostet 10 € je Kopf, nur 5 Kunden bestellen. Bei 6 € bestellen 15.',
              [(r'Menge: \(\frac{15 - 5}{(15 + 5)/2} = \frac{10}{10} = 1\)', '+100 %'), (r'Preis: \(\frac{6 - 10}{(6 + 10)/2} = \frac{-4}{8} = -0{,}5\)', '−50 %'), (r'\(\varepsilon = \left|\frac{1}{-0{,}5}\right|\)', '2')], 'Elastisch: Preis −1 % → Menge +2 %.')
        + bsp('Orangensaft', 'Bei 1,90 € werden täglich 3.700 Flaschen verkauft. Nach einer guten Ernte sinkt der Preis auf 1,50 €, verkauft werden 4.800.',
              [(r'Menge: \(\frac{1.100}{4.250} \approx 0{,}259\)', ''), (r'Preis: \(\frac{-0{,}40}{1{,}70} \approx -0{,}235\)', ''), (r'\(\varepsilon \approx \frac{0{,}259}{0{,}235}\)', '≈ 1,1')], 'Leicht elastisch.')
        + weiter('Wann ist die Mittelwertmethode ungenau?')
        + h3('Grenzen der Methode')
        + p('Die Mittelwertmethode beschreibt den ganzen <b>Bogen</b> zwischen zwei Punkten. Liegen die Punkte weit auseinander (große Unterschiede), gehen viele Werte in der Mitte verloren; das Ergebnis wird unscharf. Dann ist die Punktelastizität genauer.')
        + klausur_hinweis('Sehr häufig gefragt. Achtung beim Einsetzen: M gehört zu Menge, p zu Preis, Index 1 = vorher. Am Ende Betrag und Standardsatz.')
        + falle('Den Mittelwert vergessen und durch den alten Wert teilen. Das ist die einfache Prozentrechnung, nicht die Mittelwertmethode.')
        + wahr('w-mw', [('Bei der Mittelwertmethode bezieht man die Änderung auf den Durchschnitt aus vorher und nachher.', True, 'Daher der Name.'),
                        ('Die Mittelwertmethode braucht eine Nachfragefunktion.', False, 'Zwei Punkte (Preis und Menge vorher und nachher) genügen.'),
                        ('Parkhaus 12 € → 9 €, 50 → 80 Plätze: ε ≈ 1,62.', True, '30/65 geteilt durch 3/10,5.')]),
    merk='Mittelwertmethode: ε = |((M₂ − M₁) ÷ ((M₂ + M₁)/2)) ÷ ((p₂ − p₁) ÷ ((p₂ + p₁)/2))|. Für zwei gegebene Punkte. Ungenau, wenn die Punkte weit auseinanderliegen.',
    exam='Elastizität nach der Mittelwertmethode ohne Taschenrechner berechnen (Parkplätze, Shisha, Orangensaft) und deuten.',
    fehler=['Durch den alten statt durch den mittleren Wert teilen.', 'Menge und Preis im Bruch vertauschen.', 'Betrag und Standardsatz vergessen.'],
    src='Folien 51, 55, 91, 95')

# ---------------------------------------------------------------- Punktelastizität (Rechner)
t_pkt = thema('punktelastizitaet', 'Punktelastizität mit Nachfragefunktion', star=True, wide=True,
    kern='Ist eine Nachfragefunktion gegeben, rechnet man die Elastizität in einem Punkt: ε = |∂Q/∂p · p/Q|. Die Ableitung der Nachfrage nach dem Preis mal Preis durch Menge.',
    kurz=p('Für das Parkhaus kennt man die Nachfrage als Funktion: \\(D(p) = 150 - 5p\\). Dann braucht man keine zwei Punkte, sondern rechnet die Elastizität <b>genau an einem Preis</b>: die <b>Punktelastizität</b>.')
        + p('Man nimmt die <b>Steigung</b> der Nachfrage (die Ableitung, hier −5) und multipliziert sie mit Preis durch Menge. Bei p = 20 € ist Q = 50, also \\(\\varepsilon = |-5 \\cdot \\frac{20}{50}| = 2\\). Auf einer geraden Nachfragelinie ist die Elastizität an jeder Stelle anders.'),
    fig=fw('Schiebe den Preis entlang der Nachfragegeraden. Oben links ist die Nachfrage elastisch, unten rechts unelastisch, genau in der Mitte ist ε = 1.')
        + regler([('peA', 'Achsenabschnitt a in D(p) = a − b·p', 60, 200, 10, 150, ''), ('peB', 'Steigung b', 1, 10, 0.5, 5, ''), ('peP', 'Preis p', 1, 29, 0.5, 20, '€')])
        + '<svg id="figPE" viewBox="0 0 360 250" style="max-width:420px;width:100%;margin:0 auto;display:block" role="img" aria-label="Punktelastizität auf der Nachfragegeraden"></svg>'
        + schritte_karten([('① Ableitung', 'peR1', '#peT1'), ('② Menge im Punkt', 'peR2', '#peT2'), ('③ Elastizität', 'peR3', '#peT3')]),
    figcap='Übung der Vorlesung: D(p) = 150 − 5p, Preis 20 €',
    article=h3('Vier Fälle: welche Methode wann?')
        + tabelle(['Fall', 'Rechnung'], [
            ['1. Prozentänderungen bekannt', r'\(\varepsilon = \frac{\Delta M\,\%}{\Delta p\,\%}\), z. B. \(\frac{-20\,\%}{10\,\%}\)'],
            ['2. Prozente unbekannt, lassen sich aber ausrechnen', 'erst die Prozente ausrechnen, dann wie Fall 1'],
            ['3. zwei Punkte gegeben', 'Mittelwertmethode'],
            ['4. Funktion gegeben', r'Punktelastizität \(\varepsilon = \left|\frac{\partial Q}{\partial p} \cdot \frac{p}{Q}\right|\)']])
        + fx('Punktelastizität', r'\varepsilon = \left| \frac{\partial Q}{\partial p} \cdot \frac{p}{Q} \right|',
             'Ableitung der Nachfragefunktion nach dem Preis, mal Preis, geteilt durch die Menge an dieser Stelle. ∂ (das „Del“, ein griechischer Buchstabe) ist nur eine andere Schreibweise für die Ableitung: \\(\\frac{\\partial f}{\\partial x} = f\'(x)\\).',
             r'\(D(p) = 8 - 2p\), \(p = 2\): \(Q = 8 - 4 = 4\); \(\varepsilon = \left|-2 \cdot \frac{2}{4}\right| = 1\)')
        + bsp('Klausuraufgabe', r'Die Nachfragekurve ist \(D(p) = 20.000 - 5p\). Wie hoch ist die Preiselastizität bei p = 800?',
              [(r'Ableitung: \(D^{\prime}(p) = -5\)', '−5'), (r'Menge: \(Q = 20.000 - 5 \cdot 800 = 16.000\)', '16.000'), (r'\(\varepsilon = \left|-5 \cdot \frac{800}{16.000}\right| = \frac{4.000}{16.000}\)', '0,25')],
              'Antwort c) 0,25: unelastisch. Preis +1 % → Nachfrage −0,25 %.')
        + bsp('Übung', r'\(D(p) = 150 - 5p\), Marktpreis 20 €.',
              [(r'\(Q = 150 - 100 = 50\)', ''), (r'\(\varepsilon = \left|-5 \cdot \frac{20}{50}\right|\)', '2')], 'Elastisch. Die Mittelwertmethode zwischen 20 € und 25 € ergab 3: Sie beschreibt den ganzen Bogen und ist „etwas unscharf“.')
        + weiter('Oft ist nicht der Preis gegeben, sondern ein Markt mit Angebot und Nachfrage.')
        + h3('Elastizität im Marktgleichgewicht')
        + p('Im <b>Marktgleichgewicht</b> treffen Angebot S(p) und Nachfrage D(p) aufeinander: \\(S(p) = D(p)\\). Daraus folgen Gleichgewichtspreis p* und Menge Q*. Wenn nichts anderes steht, ist immer die <b>Nachfrage</b>-Elastizität gemeint, also nimmt man die Ableitung von D(p).')
        + bsp('Marktgleichgewicht', r'Angebot \(S(p) = 1.800 + 240p\), Nachfrage \(D(p) = 3.550 - 266p\).',
              [(r'\(1.800 + 240p = 3.550 - 266p \Rightarrow 506p = 1.750\)', r'\(p^* \approx 3{,}46\)'), (r'\(Q^* = 3.550 - 266 \cdot 3{,}46\)', '≈ 2.630'),
               (r'\(\varepsilon = \left|-266 \cdot \frac{3{,}46}{2.630}\right|\)', '≈ 0,35')], 'Bei einer Preisänderung von 1 % ändert sich die Nachfrage um 0,35 %: unelastisch.')
        + falle('Die Ableitung von S(p) nehmen, obwohl nach der Nachfrageelastizität gefragt ist. Nur für die Angebotselastizität nimmt man S(p).')
        + wahr('w-pe', [('Auf einer geraden Nachfragekurve ist die Elastizität überall gleich.', False, 'Die Steigung ist gleich, p/Q aber nicht.'),
                        ('Bei D(p) = 20.000 − 5p und p = 800 ist ε = 0,25.', True, '5 · 800 ÷ 16.000.'),
                        ('Für die Punktelastizität braucht man eine Funktion oder Ableitung.', True, 'Fall 4.')]),
    merk='Punktelastizität: ε = |D\'(p) · p ÷ Q|. Erst Q = D(p) ausrechnen. Im Marktgleichgewicht S(p) = D(p) → p*, Q*; ohne Angabe Nachfrageelastizität (D).',
    exam='Punktelastizität aus einer linearen Nachfragefunktion, auch im Marktgleichgewicht (Auswahlfrage mit vier Werten).',
    fehler=['Q nicht ausrechnen und p durch die Funktion selbst teilen.', 'Vorzeichen stehen lassen statt Betrag.', 'Angebots- statt Nachfragefunktion ableiten.'],
    src='Folien 53–55, 92–93')

# ---------------------------------------------------------------- Preis-, Mengen-, Gesamteffekt (Rechner)
t_eff = thema('effekte', 'Preiseffekt, Mengeneffekt und Gesamteffekt', star=True, wide=True,
    kern='Bei einer Preisänderung ändert sich der Erlös. Mengeneffekt ME = (M_neu − M_alt) · p_neu, Preiseffekt PE = (p_neu − p_alt) · M_alt, Gesamteffekt GE = Erlös_neu − Erlös_alt = ME + PE. Bei elastischer Nachfrage lohnt eine Preissenkung.',
    kurz=p('Senkt das Parkhaus den Preis von 12 € auf 9 €, verliert es an den 50 alten Kunden je 3 €: Das ist der <b>Preiseffekt</b> (−150 €). Dafür kommen 30 neue Autos zu je 9 € dazu: der <b>Mengeneffekt</b> (+270 €).')
        + p('Unterm Strich steigt der Erlös um 120 €: der <b>Gesamteffekt</b>. Ob er positiv oder negativ ist, hängt an der Elastizität: Ist die Nachfrage elastisch, gewinnt bei einer Preissenkung der Mengeneffekt.'),
    fig=fw('Rechner wie auf der Folie: Die rote Fläche geht durch den niedrigeren Preis verloren, die grüne kommt durch die zusätzliche Menge dazu.')
        + regler([('efP1', 'Preis alt', 1, 6, 0.1, 4.5, '€'), ('efP2', 'Preis neu', 1, 6, 0.1, 4, '€')])
        + '<svg id="figEF" viewBox="0 0 360 270" style="max-width:420px;width:100%;margin:0 auto;display:block" role="img" aria-label="Preis-, Mengen- und Gesamteffekt"></svg>'
        + schritte_karten([('① Mengeneffekt', 'efR1', '#efT1'), ('② Preiseffekt', 'efR2', '#efT2'), ('③ Gesamteffekt', 'efR3', '#efT3')]),
    figcap='Folienbeispiel: Nachfrage D(p) = 1.000 − 200p; Preis 4,50 € → 4,00 €, Menge 100 → 200',
    article=h3('Die drei Effekte')
        + fx('Mengeneffekt', r'ME = (M_{neu} - M_{alt}) \cdot p_{neu}', 'Wie viel mehr (oder weniger) wird verkauft, und was bringt das zum neuen Preis?', r'\((200 - 100) \cdot 4{,}00 = 400\) €')
        + fx('Preiseffekt', r'PE = (p_{neu} - p_{alt}) \cdot M_{alt}', 'Was man bei der alten Menge durch den neuen Preis mehr oder weniger bekommt.', r'\((4{,}00 - 4{,}50) \cdot 100 = -50\) €')
        + fx('Gesamteffekt', r'GE = \text{Erlös}_{neu} - \text{Erlös}_{alt} = ME + PE', 'Die Änderung des Erlöses insgesamt.', r'\(800 - 450 = 350\) € \(= 400 - 50\)',
             r'\(p_{neu} M_{neu} - p_{alt} M_{alt} = p_{neu}(M_{neu} - M_{alt}) + M_{alt}(p_{neu} - p_{alt})\). Ausmultiplizieren zeigt, dass beide Seiten gleich sind.')
        + p('In der Vorlesung werden die Effekte als <b>Beträge</b> notiert: „GE = ME − PE = 400 − 50 = 350“. Gemeint ist dasselbe: Der Gewinn aus der Mehrmenge minus der Verlust aus dem niedrigeren Preis.')
        + weiter('Wann überwiegt welcher Effekt? Das verrät die Elastizität.')
        + h3('Zusammenhang mit der Elastizität')
        + tabelle(['Nachfrage', 'Preissenkung', 'Preiserhöhung'], [
            ['elastisch (ε > 1)', 'ME überwiegt PE → GE positiv', 'PE überwiegt ME → GE negativ'],
            ['einheitselastisch (ε = 1)', 'PE und ME heben sich auf', 'PE und ME heben sich auf'],
            ['unelastisch (ε < 1)', 'PE überwiegt ME → GE negativ', 'PE überwiegt ME → GE positiv']])
        + p('Merksatz: <b>Elastisch → Preis senken lohnt. Unelastisch → Preis erhöhen lohnt.</b> Deshalb erhöhen Anbieter bei Benzin und Zigaretten gern die Preise.')
        + bsp('Orangensaft', '1,90 € → 1,50 €, Menge 3.700 → 4.800 (ε ≈ 1,1).',
              [(r'\(ME = 1{,}50 \cdot 1.100\)', '+1.650 €'), (r'\(PE = -0{,}40 \cdot 3.700\)', '−1.480 €'), (r'\(GE = 1.650 - 1.480\)', '+170 €')],
              'Warum positiv? Die Nachfrage ist elastisch, bei der Preissenkung kompensiert der Mengeneffekt den negativen Preiseffekt.')
        + bsp('Preiserhöhung', r'\(D(p) = 150 - 5p\); der Preis steigt von 20 € auf 25 € (ε = 3, elastisch).',
              [(r'Mengen: \(D(20) = 50\), \(D(25) = 25\)', ''), (r'\(ME = (25 - 50) \cdot 25\)', '−625 €'), (r'\(PE = (25 - 20) \cdot 50\)', '+250 €'), (r'\(GE = -625 + 250\)', '−375 €')],
              'Bei elastischer Nachfrage und Preiserhöhung überwiegt der Mengeneffekt nach unten: Der Erlös sinkt (1.000 € → 625 €).')
        + falle('ME mit dem alten Preis und PE mit der neuen Menge rechnen. Merke: ME mal p<sub>neu</sub>, PE mal M<sub>alt</sub>.')
        + wahr('w-ef', [('Bei elastischer Nachfrage steigt der Erlös, wenn der Preis sinkt.', True, 'Der Mengeneffekt überwiegt.'),
                        ('Der Preiseffekt wird mit der neuen Menge berechnet.', False, 'Mit der alten Menge: PE = Δp · M_alt.'),
                        ('Bei unelastischer Nachfrage lohnt sich eine Preiserhöhung für den Erlös.', True, 'Der Preiseffekt überwiegt.')]),
    merk='ME = (M_neu − M_alt) · p_neu; PE = (p_neu − p_alt) · M_alt; GE = Erlös_neu − Erlös_alt = ME + PE. Elastisch: Preissenkung → GE positiv. Unelastisch: Preiserhöhung → GE positiv.',
    exam='Preis-, Mengen- und Gesamteffekt berechnen und mit der Elastizität erklären, wie sich der Erlös entwickelt.',
    fehler=['Preise und Mengen in ME und PE vertauschen.', 'Vorzeichen des Gesamteffekts nicht deuten.'],
    src='Folien 52, 55–57, 94–96')

KAPITEL = kapitel('k3', 'Elastizität',
    'Wie stark reagiert die Nachfrage auf den Preis? Begriff, Mittelwertmethode, Punktelastizität und die Wirkung auf den Erlös. Ein Lieblingsthema der Klausur, ohne Taschenrechner. Durchgehendes Beispiel: das Parkhaus am Wasserturm.',
    ['Begriff', 'Mittelwertmethode', 'Punktelastizität', 'Effekte'],
    [t_begriff, t_mw, t_pkt, t_eff])

from mehr1 import ergaenze
ergaenze(KAPITEL)
