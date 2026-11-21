import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *

# Durchgehendes Beispiel: Lenas Kaffeerösterei „Bohnenwerk“ in Mannheim-Jungbusch.

# ---------------------------------------------------------------- 1 Wirtschaften: Grundproblem und Lösungsweg
fig_weg = svg(360, 286,
    box(4, 4, 352, 54, 'Schritt 1 · Grundproblem\nunendliche Bedürfnisse, knappe Mittel', size=13, art='pale', tip='Ausgangspunkt: Man will mehr, als man hat. Also muss man auswählen.')
    + pfeil(180, 60, 180, 72)
    + box(4, 74, 352, 64, 'Schritt 2 · Lösung (Obersätze)\nlangfristige Gewinnmaximierung\nunter Nebenbedingungen', size=13, art='hl', tip='Obersatz III ist die gültige Lösung: Mach das, was langfristig den höchsten Gewinn verspricht, und beachte dabei die gesellschaftlichen Vorgaben.')
    + pfeil(180, 140, 180, 152)
    + box(4, 154, 352, 54, 'Schritt 3 · Prinzipien\nRationalprinzip · ökonomisches Prinzip', size=13, tip='Wie entscheidet man im Einzelfall? Nach dem Rationalprinzip und dem ökonomischen Prinzip (Maximum, Minimum, Optimum).')
    + pfeil(180, 210, 180, 222)
    + box(4, 224, 352, 54, 'Schritt 4 · Ergebnisse messen\nGewinn, Wirtschaftlichkeit, Rentabilität …', size=13, tip='Ob gut gewirtschaftet wurde, zeigen die Erfolgsmaßstäbe: Gewinn, Wirtschaftlichkeit, Produktivität, Rentabilität, Liquidität.'),
    'Vier Schritte vom Grundproblem zum Ergebnis', maxw=420)

t_wirt = thema('wirtschaften', 'Wirtschaften: vom Grundproblem zur Gewinnmaximierung',
    kern='Wirtschaften heißt: Weil die Mittel knapp sind, versucht man langfristig den Gewinn zu maximieren und beachtet dabei die Nebenbedingungen der Gesellschaft.',
    kurz=p('Lena röstet Kaffee. Sie könnte noch zehn neue Sorten anbieten, einen zweiten Laden eröffnen und eine Rösterei in Italien kaufen. Das Geld reicht für einen Bruchteil. Das ist das <b>Grundproblem</b>: <b>unendliche Bedürfnisse, knappe Mittel</b>.')
        + p('Die Lösung der BWL: Lena macht das, was <b>langfristig</b> den höchsten Gewinn verspricht, und hält sich dabei an Gesetze und gesellschaftliche Regeln. So kommt man in vier Schritten vom Problem zum Ergebnis.'),
    fig=fw('Der Weg in vier Schritten. Tippe auf die Kästen.') + bild(fig_weg),
    figcap='nach Folie „Definition BWL: Grundproblem, Lösung, Prinzipien, Ergebnisse“',
    article=h3('Schritt 1: Das Grundproblem')
        + p('Hätte man unendlich viele Mittel für jedes Bedürfnis, gäbe es nichts zu entscheiden. In der Wirklichkeit stehen unendlich viele Bedürfnisse knappen Mitteln gegenüber. Wer wirtschaftet, muss deshalb auswählen.')
        + weiter('Wie wählt man aus? Die BWL hat dafür nacheinander drei „Obersätze“ entwickelt. Jeder repariert ein Problem des vorigen.')
        + h3('Schritt 2: Drei Obersätze')
        + tabelle(['Obersatz', 'Regel', 'Problem'], [
            ['I: Maximierung des Gewinns', 'Mach das, was den höchsten Gewinn verspricht.', 'Kurzfristig wäre der höchste Gewinn: alles verkaufen, Maschinen, Gebäude, Marke. Danach ist alles weg.'],
            ['II: Langfristige Maximierung des Gewinns', 'Mach das, was langfristig den höchsten Gewinn verspricht.', 'Auch Betrug kann langfristig Gewinn bringen, bis er auffliegt (Abgasmanipulation bei Dieselmotoren).'],
            ['III: Langfristige Maximierung unter Nebenbedingungen', 'Mach das, was langfristig den höchsten Gewinn verspricht, <b>und</b> beachte die gesellschaftlichen Vorgaben.', 'die gültige Lösung']])
        + p('Obersatz III steckt in der Definition von <b>Wirtschaften</b>: langfristige Maximierung des Gewinns unter Beachtung von Nebenbedingungen. ' + eg('Möglichst viel Gewinn, auf Dauer und ehrlich.'))
        + bsp('Lenas drei Möglichkeiten', 'Lena hat ein Angebot: Ein Großhändler will ihre gesamte Röstmaschine samt Kundenliste kaufen. Alternativ könnte sie billigen Kaffee als „fair gehandelt“ etikettieren. Oder sie investiert in einen zweiten Röster.',
              [('Alles verkaufen bringt heute den höchsten Gewinn, danach ist der Betrieb weg.', 'verstößt gegen Obersatz II'), ('Falsches Etikett bringt lange Gewinn, ist aber Betrug.', 'verstößt gegen Obersatz III'), ('Zweiter Röster: mehr Gewinn auf Dauer und legal.', 'Obersatz III')])
        + weiter('Wie trifft man im Alltag die einzelnen Entscheidungen? Dafür gibt es Prinzipien (nächstes Unterthema), und man misst das Ergebnis mit Kennzahlen.')
        + h3('Schritt 3 und 4: Prinzipien und Ergebnisse')
        + p('Schritt 3 sind das <b>Rationalprinzip</b> und das <b>ökonomische Prinzip</b> mit Maximum-, Minimum- und Optimumprinzip. Schritt 4 sind die <b>Erfolgsmaßstäbe</b>: Gewinn, Wirtschaftlichkeit, Produktivität, Break-even, Rentabilität, Liquidität, Wertschöpfung, Effizienz und Effektivität. Diese Kennzahlen werden in der Klausur gerechnet.')
        + wahr('w-wirt', [('Obersatz I (Gewinnmaximierung ohne Zusatz) ist die gültige Lösung.', False, 'Er würde zum Ausverkauf führen. Gültig ist Obersatz III.'),
                          ('Wirtschaften heißt langfristige Gewinnmaximierung unter Nebenbedingungen.', True, 'Das ist Obersatz III.'),
                          ('Ein Gesetzesverstoß kann nach Obersatz II zulässig wirken, nach Obersatz III nicht.', True, 'Erst Obersatz III verlangt, Nebenbedingungen zu beachten.')]),
    merk='Grundproblem: unendliche Bedürfnisse, knappe Mittel. Lösung (Obersatz III): langfristige Maximierung des Gewinns unter Beachtung von Nebenbedingungen.',
    exam='Die drei Obersätze unterscheiden und erkennen, warum erst Obersatz III gilt.',
    fehler=['Gewinnmaximierung ohne „langfristig“ und „Nebenbedingungen“ als Ziel nennen.'],
    src='Folien 28–30')

# ---------------------------------------------------------------- 2 Ökonomisches Prinzip
def prinzip_tafel(titel, inp, out, frage, hl):
    s = T(180, 18, titel, 15, 800)
    s += box(4, 34, 150, 64, 'Input (Aufwand)\n' + inp, size=13, art='hl' if hl == 0 else 'card', tip='Was eingesetzt wird: Material, Zeit, Geld.')
    s += pfeil(156, 66, 202, 66)
    s += box(206, 34, 150, 64, 'Output (Ertrag)\n' + out, size=13, art='hl' if hl == 1 else 'card', tip='Was herauskommt: Menge oder Wert der Güter.')
    s += T(180, 122, frage, 13, 600, 'middle', 'var(--muted)')
    return svg(360, 134, s, titel, maxw=420)

t_oek = thema('oekprinzip', 'Rationalprinzip und ökonomisches Prinzip',
    kern='Das ökonomische Prinzip verlangt, das Verhältnis von Output (Ertrag) zu Input (Aufwand) zu optimieren. Maximumprinzip: Input gegeben, Output maximal. Minimumprinzip: Output gegeben, Input minimal. Optimumprinzip: beides frei.',
    kurz=p('Lena hat genau 60 kg Rohkaffee. Sie will daraus so viele verkaufsfertige Packungen wie möglich rösten: Der <b>Input ist gegeben</b>, der <b>Output soll maximal</b> sein. Das ist das <b>Maximumprinzip</b>.')
        + p('Ein Café bestellt 200 Packungen. Lena will sie mit möglichst wenig Rohkaffee und Gas herstellen: Der <b>Output ist gegeben</b>, der <b>Input soll minimal</b> sein. Das ist das <b>Minimumprinzip</b>. Sind beide Seiten frei, sucht sie das beste Verhältnis: <b>Optimumprinzip</b>.'),
    fig=fw('Umschalten zwischen den drei Ausprägungen. Was ist gegeben, was wird optimiert?')
        + tafeln('tf-oek', ['Maximum', 'Minimum', 'Optimum'], [
            prinzip_tafel('Maximumprinzip', 'gegeben', 'max!', 'Mit 60 kg Rohkaffee möglichst viele Packungen', 0),
            prinzip_tafel('Minimumprinzip', 'min!', 'gegeben', '200 Packungen mit möglichst wenig Rohkaffee', 1),
            prinzip_tafel('Optimumprinzip', 'frei', 'frei', 'bestes Verhältnis von Packungen zu Rohkaffee', 2)]),
    figcap='nach Folien „Definition: Wirtschaften (Prinzipien)“',
    article=h3('Das Rationalprinzip')
        + p('„Ein Akteur handelt nach dem <b>Rationalprinzip</b>, wenn er sich bei der Wahl zwischen Alternativen für die bessere Lösung entscheidet.“ ' + eg('Nimm von zwei Möglichkeiten die bessere.') + ' Das ist richtig, aber noch nicht sehr konkret. Was „besser“ heißt, sagt erst das ökonomische Prinzip.')
        + weiter('Das ökonomische Prinzip macht „besser“ messbar: als Verhältnis von dem, was herauskommt, zu dem, was hineingeht.')
        + h3('Das ökonomische Prinzip')
        + p('„Das <b>ökonomische Prinzip</b> verlangt, das Verhältnis aus Produktionsergebnis (Output, Ertrag) und Produktionseinsatz (Input, Aufwand) zu optimieren.“ Beide Seiten kann man in Menge oder in Euro messen:')
        + fx('Ertrag und Aufwand', r'\text{Ertrag} = \text{Output} \cdot \text{Güterpreis} \qquad \text{Aufwand} = \text{Input} \cdot \text{Faktorpreis}',
             'Der Ertrag ist die verkaufte Menge mal Verkaufspreis. Der Aufwand ist die eingesetzte Menge mal Einkaufspreis.',
             'Lena verkauft 10 Packungen zu 12 €: Ertrag 120 €. Sie braucht 3 kg Rohkaffee zu 15 €: Aufwand 45 €.')
        + weiter('Je nachdem, welche Seite festliegt, gibt es drei Ausprägungen.')
        + h3('Maximum, Minimum, Optimum')
        + tabelle(['Prinzip', 'gegeben', 'Ziel', 'Beispiel'], [
            ['Maximumprinzip', 'Input (Faktoreinsatz)', 'größtmöglicher Output', 'Mit 10 Litern Kraftstoff möglichst weit fahren. Mit 10 kWh möglichst warm heizen.'],
            ['Minimumprinzip', 'Output (Gütermenge)', 'geringstmöglicher Input', '100 km mit möglichst wenig Kraftstoff fahren. Die Wohnung mit möglichst wenig Energie auf 20 Grad bringen. 5 Tonnen Kartoffeln mit möglichst wenig Dünger.'],
            ['Optimumprinzip', 'nichts', 'möglichst günstiges Verhältnis von Output zu Input', 'Lena wählt Menge und Einsatz so, dass das Verhältnis am besten ist.']])
        + p('Merkhilfe: Das <b>Gegebene</b> nennt man auch das „Datum“. Das andere wird maximiert oder minimiert.')
        + falle('Beides zugleich verlangen: „Mit möglichst wenig Input möglichst viel Output“. Das ist unmöglich und kein ökonomisches Prinzip. Eine Seite muss gegeben sein (Maximum/Minimum), oder man optimiert das Verhältnis (Optimum).')
        + spiel('sp-oek', 'Maximum- oder Minimumprinzip?', ['Maximumprinzip', 'Minimumprinzip'],
                [('Mit 50 € Werbebudget möglichst viele Kunden erreichen', 0, 'Input (50 €) gegeben, Output maximieren'),
                 ('Eine Bestellung über 200 Packungen mit möglichst wenig Gas rösten', 1, 'Output gegeben, Input minimieren'),
                 ('Mit einer Tankfüllung möglichst weit fahren', 0, 'Input gegeben'),
                 ('Die Strecke Mannheim–Heidelberg mit möglichst wenig Benzin fahren', 1, 'Output (Strecke) gegeben'),
                 ('In 8 Stunden Arbeitszeit möglichst viele Räder reparieren', 0, 'Input (Zeit) gegeben'),
                 ('5 Tonnen Kartoffeln mit möglichst wenig Dünger ernten', 1, 'Output gegeben')]),
    merk='Ökonomisches Prinzip: Verhältnis Output/Input optimieren. Maximum: Input gegeben → Output max. Minimum: Output gegeben → Input min. Optimum: bestes Verhältnis. „Möglichst viel mit möglichst wenig“ ist falsch.',
    exam='Beispiele dem Maximum-, Minimum- oder Optimumprinzip zuordnen; Ertrag und Aufwand als Menge mal Preis.',
    fehler=['„Mit möglichst wenig möglichst viel“ als ökonomisches Prinzip bezeichnen.', 'Maximum- und Minimumprinzip vertauschen. Fragen: Was liegt fest?'],
    src='Folien 31–34')

# ---------------------------------------------------------------- 3 Gewinn, Wirtschaftlichkeit, Produktivität
fig_wirt = svg(360, 256,
    achsen(40, 196, 350, 14, '', '€')
    + rechteck(70, 196 - 150, 70, 150, 'var(--c2)', 'var(--c2)', 4) + T(105, 214, 'Ertrag', 13, 700) + T(105, 40, '1.500 €', 13, 800)
    + rechteck(160, 196 - 50, 70, 50, 'var(--axis2)', 'var(--axis)', 4) + T(195, 214, 'Aufwand', 13, 700) + T(195, 140, '500 €', 13, 800)
    + tpg(rechteck(250, 196 - 100, 70, 100, 'var(--primary)', 'var(--primary)', 4) + T(285, 214, 'Gewinn', 13, 700) + T(285, 90, '1.000 €', 13, 800), 'Gewinn = Ertrag − Aufwand = 1.500 € − 500 € = 1.000 €. Ein absoluter Betrag in Euro.')
    + T(195, 246, 'Wirtschaftlichkeit = 1.500 ÷ 500 = 3', 13, 800, 'middle', 'var(--primary)'),
    'Ertrag, Aufwand und Gewinn', maxw=420)

t_wirtk = thema('kennzahlen', 'Gewinn, Wirtschaftlichkeit und Produktivität', star=True,
    kern='Gewinn = Ertrag − Aufwand (ein Eurobetrag). Wirtschaftlichkeit = Ertrag ÷ Aufwand (über 1 heißt wirtschaftlich). Produktivität = Output ÷ Input in Mengen.',
    kurz=p('Lena verkauft in einer Woche Kaffee für 1.500 € und hat dafür 500 € ausgegeben. Ihr <b>Gewinn</b> ist der Unterschied: 1.000 €. Die <b>Wirtschaftlichkeit</b> ist das Verhältnis: 1.500 ÷ 500 = 3. Jeder eingesetzte Euro bringt 3 € Ertrag.')
        + p('Die <b>Produktivität</b> misst dagegen Mengen: wie viele Packungen pro Arbeitsstunde. Mindestens muss immer gelten: <b>Ertrag ≥ Aufwand</b>, sonst ist der Betrieb auf Dauer nicht überlebensfähig.'),
    fig=fw('Lenas Woche in Zahlen. Tippe auf den Gewinn.') + bild(fig_wirt),
    figcap='nach Folien „Definition: Wirtschaften (Ergebnisse)“',
    article=h3('Mindestbedingung und Gewinn')
        + p('Langfristig muss gelten: <b>Ertrag ≥ Aufwand</b>. Das ist die Mindestbedingung für jeden Betrieb.')
        + fx('Gewinn', r'G = E - A', 'Gewinn ist Ertrag minus Aufwand: ein absoluter Geldbetrag.', '1.500 € − 500 € = 1.000 €')
        + weiter('Der Gewinn sagt, wie viel übrig bleibt. Die Wirtschaftlichkeit sagt, wie gut das Verhältnis ist.')
        + h3('Wirtschaftlichkeit')
        + fx('Wirtschaftlichkeit', r'W = \frac{\text{Ertrag}}{\text{Aufwand}}', 'Ertrag geteilt durch Aufwand. Liegt der Wert über 1, ist der Betrieb wirtschaftlich. Sobald der Ertrag kleiner ist als der Aufwand (Wert unter 1), ist er nicht wirtschaftlich.',
             r'\(\frac{1.500}{500} = 3\)')
        + bsp('Ist die Wirtschaftlichkeit gestiegen?', 'Letztes Jahr: Ertrag 240.000 €, Aufwand 200.000 €. Dieses Jahr: Ertrag 330.000 €, Aufwand 300.000 €.',
              [(r'Letztes Jahr: \(\frac{240.000}{200.000} = 1{,}2\)', '1,2'), (r'Dieses Jahr: \(\frac{330.000}{300.000} = 1{,}1\)', '1,1'), ('Der Ertrag ist gestiegen, aber der Gewinn sank von 40.000 € auf 30.000 €, und das Verhältnis ist schlechter geworden.', 'Wirtschaftlichkeit gesunken')],
              'Nicht auf den höheren Ertrag hereinfallen: Entscheidend ist das Verhältnis.')
        + weiter('Wirtschaftlichkeit rechnet in Euro. Die Produktivität rechnet in Mengen.')
        + h3('Produktivität')
        + fx('Produktivität', r'P = \frac{\text{Output}}{\text{Input}}', 'Mengenverhältnis: Was kommt heraus, bezogen auf das, was hineingeht. Welche Mengen gemeint sind, wird erst aus dem Zusammenhang klar.',
             'a) 10 Autos in 10 Stunden: 1 Auto pro Stunde (Arbeitsproduktivität). b) 1 Vertrag in 2 Stunden: 0,5 Verträge pro Stunde („Vertragsproduktivität“).')
        + p('Produktivität steigern heißt: Input klein halten, Output hoch halten, oder beide in ein besseres Verhältnis bringen.')
        + zusatz('Das „Produktivitätsparadox“ (mehr IT, aber kaum messbar höhere Produktivität) steht auf der Folie, wurde aber ausgelassen.')
        + falle('Gewinn und Wirtschaftlichkeit gleichsetzen. Der Gewinn kann steigen, während die Wirtschaftlichkeit sinkt, wenn der Aufwand stärker wächst als der Ertrag.')
        + wahr('w-kz', [('Bei einer Wirtschaftlichkeit von 0,9 ist der Betrieb wirtschaftlich.', False, 'Unter 1 ist der Ertrag kleiner als der Aufwand.'),
                        ('Gewinn ist ein absoluter Betrag, Wirtschaftlichkeit eine Verhältniszahl.', True, 'G = E − A; W = E ÷ A.'),
                        ('Produktivität wird in Mengen gemessen.', True, 'Output-Menge durch Input-Menge.')]),
    merk='Mindestbedingung: Ertrag ≥ Aufwand. Gewinn = E − A. Wirtschaftlichkeit = E ÷ A (> 1 wirtschaftlich). Produktivität = Output ÷ Input (Mengen).',
    exam='Wirtschaftlichkeit für zwei Jahre berechnen und vergleichen („ist sie gestiegen?“); Gewinn und Produktivität im Kopf rechnen.',
    fehler=['Nur auf den höheren Ertrag oder Gewinn schauen, wenn nach Wirtschaftlichkeit gefragt ist.', 'Wirtschaftlichkeit als Aufwand ÷ Ertrag rechnen (umgedreht).'],
    src='Folien 35–36')

# ---------------------------------------------------------------- 4 Break-even-Punkt (Rechner)
t_be = thema('breakeven', 'Break-even-Punkt: ab wann sich das Geschäft lohnt', star=True, wide=True,
    kern='Der Break-even-Punkt (Gewinnschwelle) ist die Menge, bei der Ertrag und Aufwand gleich sind, also der Gewinn null ist. Man setzt G(x) = 0 oder E(x) = A(x).',
    kurz=p('Lena verkauft eine Kaffeemühle für 40 €. Jede Mühle kostet sie im Einkauf 10 € (<b>variable Kosten</b>). Dazu kommen 21.000 € im Jahr für Miete und Versicherung, egal wie viel sie verkauft (<b>Fixkosten</b>).')
        + p('Wie viele Mühlen muss sie verkaufen, damit alle Kosten gedeckt sind? Jede Mühle bringt 40 − 10 = 30 € zur Deckung der Fixkosten. 21.000 ÷ 30 = <b>700 Stück</b>. Das ist der <b>Break-even-Punkt</b>: Ab der 701. Mühle macht sie Gewinn.'),
    fig=fw('Schiebe die Regler. Wo sich Ertragsgerade und Aufwandsgerade schneiden, liegt der Break-even-Punkt.')
        + regler([('beP', 'Verkaufspreis', 20, 60, 1, 40, '€'), ('beV', 'variable Kosten je Stück', 0, 18, 1, 10, '€'), ('beF', 'Fixkosten', 9000, 30000, 1000, 21000, '€')])
        + '<svg id="figBE" viewBox="0 0 360 260" style="max-width:420px;width:100%;margin:0 auto;display:block" role="img" aria-label="Break-even-Diagramm"></svg>'
        + schritte_karten([('① Deckung je Stück', 'beR1', '#beT1'), ('② Gewinnfunktion', 'beR2', '#beT2'), ('③ Break-even-Menge', 'beR3', '#beT3')]),
    figcap='Zahlen wie im Beispiel der Folie „Break-Even-Punkt“',
    article=h3('Drei Funktionen')
        + p('Für den Break-even-Punkt braucht man drei Funktionen der Menge \\(x\\):')
        + fx('Ertrags-, Aufwands- und Gewinnfunktion', r'E(x) = p \cdot x \qquad A(x) = k_v \cdot x + K_f \qquad G(x) = E(x) - A(x)',
             'Ertrag = Preis mal Menge. Aufwand = variable Kosten je Stück mal Menge plus Fixkosten. Gewinn = Ertrag minus Aufwand.',
             r'\(E(x) = 40x\), \(A(x) = 10x + 21.000\), \(G(x) = 40x - 10x - 21.000 = 30x - 21.000\)')
        + weiter('Der Break-even-Punkt ist dort, wo der Gewinn genau null ist.')
        + h3('Break-even-Punkt berechnen')
        + fx('Break-even-Menge', r'G(x) = 0 \quad\Leftrightarrow\quad E(x) = A(x) \quad\Rightarrow\quad x_{BE} = \frac{K_f}{p - k_v}',
             'Gewinnfunktion gleich null setzen (oder Ertrag gleich Aufwand) und nach x auflösen. Bei linearen Funktionen: Fixkosten geteilt durch die Deckung je Stück.',
             r'\(30x - 21.000 = 0 \Rightarrow 30x = 21.000 \Rightarrow x = 700\) Stück',
             'Jedes verkaufte Stück bringt p − k<sub>v</sub> Euro, die zuerst die Fixkosten abtragen. Sind die Fixkosten ganz gedeckt, ist man am Break-even-Punkt.')
        + bsp('Ertrag am Break-even-Punkt', 'Wie hoch ist der Ertrag bei der Gewinnschwelle?',
              [(r'Menge an der Gewinnschwelle: 700 Stück', ''), (r'Ertrag = Output · Güterpreis \(= 700 \cdot 40\)', '28.000 €'), (r'Probe: Aufwand \(= 10 \cdot 700 + 21.000 = 28.000\) €', 'Gewinn 0')])
        + klausur_hinweis('Ohne Taschenrechner! Der Break-even-Punkt kommt fast immer dran, oft „durch Gleichsetzen“ mit gegebenen Funktionen. Nur das Ergebnis zählt, also am Ende die Probe machen.')
        + weiter('Sind die Funktionen nicht linear (z. B. weil der Preis mit der Menge sinkt), gibt es zwei Gewinnschwellen. Das steht im Unterthema „Gewinnmaximum“.')
        + h3('Gewinnschwelle bei quadratischer Gewinnfunktion')
        + p(r'Ist die Gewinnfunktion eine nach unten offene Parabel, etwa \(G(x) = -\tfrac{1}{2}x^2 + 4x - 6\), dann setzt man \(G(x) = 0\) und löst mit der <b>Mitternachtsformel</b> (oder pq-Formel). Hier: \(x^2 - 8x + 12 = 0\), also \(x = 2\) oder \(x = 6\). Zwischen 2 und 6 Stück macht man Gewinn. Die <b>Gewinnschwelle</b> ist die kleinere Lösung (\(x = 2\)), die größere heißt <b>Gewinngrenze</b>.')
        + falle('Den Break-even-Punkt mit dem Gewinnmaximum verwechseln. Am Break-even-Punkt ist der Gewinn null, beim Gewinnmaximum am größten (Ableitung gleich null).')
        + wahr('w-be', [('Am Break-even-Punkt ist der Gewinn null.', True, 'Ertrag = Aufwand.'),
                        ('Steigen die Fixkosten, sinkt die Break-even-Menge.', False, 'Mehr Fixkosten müssen gedeckt werden: Die Menge steigt.'),
                        ('Bei p = 40 €, k<sub>v</sub> = 10 € und K<sub>f</sub> = 21.000 € liegt der Break-even-Punkt bei 700 Stück.', True, '21.000 ÷ 30 = 700.')]),
    merk='Break-even: G(x) = 0 bzw. E(x) = A(x). Linear: x = Fixkosten ÷ (Preis − variable Stückkosten). Ertrag dort = Menge · Preis.',
    exam='Break-even-Menge durch Gleichsetzen berechnen (Funktionen gegeben), Ertrag an der Gewinnschwelle; ohne Taschenrechner.',
    fehler=['Nur durch den Preis teilen statt durch Preis minus variable Kosten.', 'Break-even mit Gewinnmaximum verwechseln.', 'Bei quadratischem Gewinn nur eine Lösung angeben.'],
    src='Folie 37, 41, 43')

# ---------------------------------------------------------------- 5 Rentabilität
fig_rent = svg(360, 250,
    T(180, 18, 'Rentabilität = Erfolgsgröße ÷ Basisgröße', 14, 800)
    + box(118, 34, 124, 46, 'Gewinn', size=14, art='hl', tip='Die Erfolgsgröße steht oben im Bruch, meist der Gewinn.')
    + linie([(30, 92), (330, 92)], 'var(--ink)', 2)
    + box(4, 104, 112, 62, 'eingesetztes\nKapital', size=13, tip='Kapitalrentabilität: Gewinn je eingesetztem Euro Kapital.')
    + box(124, 104, 112, 62, 'Eigen-\nkapital', size=13, tip='Eigenkapitalrentabilität (Eigenkapitalrendite): Gewinn je Euro, den die Eigentümer eingesetzt haben.')
    + box(244, 104, 112, 62, 'Umsatz\n(Ertrag)', size=13, tip='Umsatzrentabilität: Gewinn je Euro Umsatz.')
    + T(60, 186, 'Kapital-', 12, 700) + T(60, 202, 'rentabilität', 12, 700)
    + T(180, 186, 'EK-', 12, 700) + T(180, 202, 'rentabilität', 12, 700)
    + T(300, 186, 'Umsatz-', 12, 700) + T(300, 202, 'rentabilität', 12, 700)
    + T(180, 236, '× 100 % → Angabe in Prozent', 13, 600, 'middle', 'var(--muted)'),
    'Rentabilität: Gewinn im Verhältnis zu einer Basisgröße', maxw=420)

t_rent = thema('rentabilitaet', 'Rentabilität: Kapital-, Eigenkapital- und Umsatzrentabilität', star=True, wide=True,
    kern='Rentabilität = Erfolgsgröße ÷ Basisgröße · 100 %. Sie setzt den Gewinn ins Verhältnis zum eingesetzten Kapital, zum Eigenkapital oder zum Umsatz und zeigt, wie effizient Kapital arbeitet.',
    kurz=p('Lena hat 100.000 € in die Rösterei gesteckt und macht 10.000 € Gewinn im Jahr. Ist das viel? Das zeigt erst die <b>Rentabilität</b>: 10.000 ÷ 100.000 = 10 %. Mit jedem eingesetzten Euro verdient sie 10 Cent.')
        + p('Die Rentabilität ist immer ein Bruch: oben die <b>Erfolgsgröße</b> (meist der Gewinn), unten eine <b>Basisgröße</b>. Je nachdem, was unten steht, heißt sie Kapital-, Eigenkapital- oder Umsatzrentabilität.'),
    fig=fw('Der Aufbau jeder Rentabilität. Tippe auf die Kästen.') + bild(fig_rent)
        + fw('Rechner: Schiebe Gewinn und Kapital. Das Ergebnis ist die Rentabilität in Prozent.')
        + regler([('rtG', 'Gewinn', 0, 60000, 500, 22500, '€'), ('rtK', 'eingesetztes Kapital', 10000, 300000, 2500, 150000, '€')])
        + schritte_karten([('① Formel', 'rtR1', '#rtT1'), ('② Rechnung', 'rtR2', '#rtT2'), ('③ Rentabilität', 'rtR3', '#rtT3')]),
    figcap='nach Folien „Definition: Wirtschaften (Ergebnisse): Rentabilität“',
    article=h3('Die Formel')
        + fx('Rentabilität', r'R = \frac{\text{Erfolgsgröße}}{\text{Basisgröße}} \cdot 100\,\%',
             'Gewinn geteilt durch die Bezugsgröße, mal 100 für Prozent. Lies das Ergebnis so: „Mit jedem eingesetzten Euro mache ich … Cent Gewinn.“',
             r'\(\frac{10.000}{100.000} \cdot 100\,\% = 10\,\%\)')
        + tabelle(['Rentabilität', 'Formel', 'Frage'], [
            ['Kapitalrentabilität', r'\(\frac{\text{Gewinn}}{\text{eingesetztes Kapital}}\)', 'Wie viel Gewinn bringt jeder Euro, der im Betrieb steckt?'],
            ['Eigenkapitalrentabilität (EK-Rendite)', r'\(\frac{\text{Gewinn}}{\text{Eigenkapital}}\)', 'Wie viel Gewinn bringt jeder Euro der Eigentümer?'],
            ['Umsatzrentabilität', r'\(\frac{\text{Gewinn}}{\text{Umsatz}}\)', 'Wie viel Gewinn bleibt von jedem Euro Umsatz?']])
        + p('Es gibt „tausende“ Rentabilitäten. Sie müssen nur sauber definiert sein: Was steht oben, was steht unten?')
        + bsp('Folienbeispiel', 'Aufwand = 100, Ertrag = 110, eingesetztes Kapital = 100.',
              [('Gewinn = 110 − 100', '10'), (r'Kapitalrentabilität \(= \frac{10}{100} \cdot 100\,\%\)', '10 %'), (r'Umsatzrentabilität \(= \frac{10}{110} \cdot 100\,\%\)', '≈ 9,09 %')],
              'Mit jedem eingesetzten Euro Kapital mache ich 10 Cent Gewinn, mit jedem Euro Umsatz gut 9 Cent.')
        + weiter('In der Klausur wird die Formel oft rückwärts gebraucht: Rentabilität und Gewinn sind gegeben, gesucht ist das Kapital, oder umgekehrt.')
        + h3('Die Formel umstellen')
        + fx('Umgestellt', r'\text{Gewinn} = R \cdot \text{Kapital} \qquad \text{Kapital} = \frac{\text{Gewinn}}{R}',
             'Steht die Rentabilität als Prozentzahl da, rechnet man mit der Dezimalzahl (15 % = 0,15).',
             r'\(\text{EK} = \frac{22.500}{0{,}15} = 150.000\) €')
        + bsp('Klausurtypisch: Gewinn gesucht', 'Es werden 22.500 € eingesetzt. Die Rentabilität soll 12 % betragen. Wie viel Gewinn muss erzielt werden?',
              [(r'\(\text{Gewinn} = 0{,}12 \cdot 22.500\)', ''), ('Kopfrechnen: 10 % = 2.250, 2 % = 450', ''), ('2.250 + 450', '2.700 €')], 'Bei 15 % wären es 2.250 + 1.125 = 3.375 €.')
        + bsp('Klausurtypisch: Eigenkapital gesucht', 'Eine Influencerin kauft 1 Mio. Follower. Die Eigenkapitalrendite beträgt 15 %, der Gewinn 22.500 €. Wie viel Eigenkapital hat sie eingesetzt?',
              [(r'\(\text{EK} = \frac{\text{Gewinn}}{R} = \frac{22.500}{0{,}15}\)', ''), ('Kopfrechnen: 22.500 ÷ 15 = 1.500, mal 100', '150.000 €')], 'Probe: 15 % von 150.000 = 22.500. Stimmt.')
        + bsp('Klausurtypisch: EK-Rentabilität gesucht', 'Ein Influencer kauft mit 500 € Eigenkapital 10.000 Bots und macht damit 1.000 € Gewinn.',
              [(r'\(\frac{1.000}{500} \cdot 100\,\%\)', '200 %')], 'Rentabilitäten über 100 % sind möglich.')
        + weiter('Ein häufiger Denkfehler: Mehr Gewinn bedeutet automatisch mehr Rentabilität. Das stimmt nicht.')
        + h3('Gewinn und Rentabilität sind nicht dasselbe')
        + p('<b>Gewinn</b> ist ein absoluter Geldbetrag (E − A). <b>Rentabilität</b> ist eine relative Verhältniszahl und misst die Effizienz. Beide können sich in verschiedene Richtungen bewegen (hier Umsatzrentabilität):')
        + tabelle(['Fall', 'Gewinn alt → neu', 'Umsatz alt → neu', 'Rentabilität alt → neu'], [
            ['Gewinn und Rentabilität steigen', '500.000 → 800.000', '1.000.000 → 1.200.000', '50 % → 66,7 %'],
            ['Gewinn steigt, Rentabilität sinkt', '500.000 → 750.000', '1.000.000 → 3.000.000', '50 % → 25 %'],
            ['Gewinn sinkt, Rentabilität steigt', '500.000 → 400.000', '5.000.000 → 2.000.000', '10 % → 20 %']])
        + p('Lernziel: Steigen beide Kennzahlen, ist das ein gutes Zeichen. Steigt nur eine, muss man genauer hinsehen.')
        + falle('Prozent und Dezimalzahl mischen: 22.500 ÷ 15 = 1.500 ist nicht das Ergebnis. Mit 0,15 teilen ergibt 150.000.')
        + wahr('w-rent', [('Steigt der Gewinn, steigt immer auch die Rentabilität.', False, 'Wächst die Basisgröße stärker, sinkt die Rentabilität.'),
                          ('Eine Eigenkapitalrendite von 200 % ist möglich.', True, '500 € EK, 1.000 € Gewinn.'),
                          ('Bei 15 % Rendite und 22.500 € Gewinn beträgt das Eigenkapital 150.000 €.', True, '22.500 ÷ 0,15.')]),
    merk='Rentabilität = Erfolgsgröße ÷ Basisgröße · 100 %. Kapital-R. = G ÷ eingesetztes Kapital; EK-R. = G ÷ EK; Umsatz-R. = G ÷ Umsatz. Umgestellt: Kapital = G ÷ R; G = R · Kapital.',
    exam='Rentabilität in allen Varianten im Kopf rechnen, auch rückwärts (Gewinn oder Kapital gesucht); Gewinn vs. Rentabilität deuten.',
    fehler=['Bei der Umstellung mit 15 statt 0,15 rechnen.', 'Umsatz- und Kapitalrentabilität verwechseln: Was steht im Nenner?', 'Gewinn und Rentabilität gleichsetzen.'],
    src='Folien 38–40, 46')

# ---------------------------------------------------------------- 6 Gewinnmaximum (Rechner)
t_gmax = thema('gewinnmax', 'Gewinnmaximum mit Preis-Absatz-Funktion', star=True, wide=True,
    kern='Das Gewinnmaximum liegt am Hochpunkt der Gewinnfunktion: G\'(x) = 0 setzen, nach x auflösen und mit G\'\'(x) < 0 prüfen. Sinkt der Preis mit der Menge (Preis-Absatz-Funktion), ist der Gewinn eine nach unten offene Parabel.',
    kurz=p('Lena verkauft Röstkurse. Je mehr Plätze sie anbietet, desto niedriger muss der Preis sein, damit alle voll werden. Diesen Zusammenhang beschreibt die <b>Preis-Absatz-Funktion</b>, etwa \\(p(x) = 6 - \\tfrac{x}{2}\\).')
        + p('Dann wächst der Gewinn nicht endlos: Erst steigt er, dann fällt er wieder. Den höchsten Punkt findet man mit der <b>Ableitung</b>: Wo die Steigung null ist, liegt das <b>Gewinnmaximum</b>.'),
    fig=fw('Schiebe die Regler. Die Kurve G ist der Gewinn; der Hochpunkt ist das Gewinnmaximum, die Nullstellen sind die Gewinnschwellen.')
        + regler([('gmA', 'Höchstpreis a in p(x) = a − x/2', 4, 10, 0.5, 6, '€'), ('gmV', 'variable Kosten je Stück', 0, 4, 0.5, 2, '€'), ('gmF', 'Fixkosten', 0, 12, 1, 6, '€')])
        + '<svg id="figGM" viewBox="0 0 360 270" style="max-width:420px;width:100%;margin:0 auto;display:block" role="img" aria-label="Erlös, Kosten und Gewinn"></svg>'
        + schritte_karten([('① Gewinnfunktion', 'gmR1', '#gmT1'), ('② Ableitung null setzen', 'gmR2', '#gmT2'), ('③ maximaler Gewinn', 'gmR3', '#gmT3')]),
    figcap='Ausgangswerte wie in der Übung der Folie 41: 2 € je Stück, 6 € Fixkosten, p(x) = 6 − x/2',
    article=h3('Vorgehen in vier Schritten')
        + merkliste('Gewinnmaximum', 'immer gleich', [
            r'Erlösfunktion aufstellen: \(E(x) = p(x) \cdot x\)',
            r'Kostenfunktion aufstellen: \(A(x) = k_v \cdot x + K_f\) (oder gegeben)',
            r'Gewinnfunktion: \(G(x) = E(x) - A(x)\), ausmultiplizieren und zusammenfassen',
            r'\(G^{\prime}(x) = 0\) setzen, nach x auflösen; \(G^{\prime\prime}(x) < 0\) heißt Hochpunkt; x in G(x) einsetzen'],
            'Erlös, Kosten, Gewinn, Ableitung')
        + bsp('Übung der Vorlesung', r'Ein Betrieb produziert für 2 €/Stück, Fixkosten 6 €. Preis-Absatz-Funktion \(p(x) = 6 - \frac{x}{2}\).',
              [(r'a) Interpretation: p(x) ist der Preis, den man erzielen kann, wenn man x Stück verkaufen will. Je mehr man verkaufen will, desto billiger muss es werden.', ''),
               (r'b) \(A(x) = 2x + 6\), \(E(x) = \left(6 - \frac{x}{2}\right) x = 6x - \frac{x^2}{2}\)', ''),
               (r'c) \(G(x) = 6x - \frac{x^2}{2} - 2x - 6 = -\frac{x^2}{2} + 4x - 6\); \(G^{\prime}(x) = -x + 4 = 0 \Rightarrow x = 4\)', 'x = 4'),
               (r'Gewinn: \(G(4) = -8 + 16 - 6 = 2\) €; \(G^{\prime\prime}(x) = -1 < 0\): Hochpunkt', '2 €'),
               (r'd) Umsatz beim höchsten Gewinn: \(E(4) = 24 - 8 = 16\) € (Preis p(4) = 4 €)', '16 €'),
               (r'e) Break-even: \(G(x) = 0 \Rightarrow x^2 - 8x + 12 = 0 \Rightarrow x = 2\) oder \(x = 6\)', 'mindestens 2 Stück')])
        + weiter('Ein zweites Beispiel mit größeren Zahlen, wie es in der Klausur vorkommt.')
        + h3('Beispiel mit Kosten- und Ertragsfunktion')
        + bsp('Folie 39', r'\(K(x) = 50x - 4{,}5x^2 + 5.000\), \(E(x) = 550x - 14{,}5x^2\) (p = 1), eingesetztes Kapital 1.000 €.',
              [(r'a) \(G(x) = 550x - 14{,}5x^2 - 50x + 4{,}5x^2 - 5.000 = -10x^2 + 500x - 5.000\)', ''),
               (r'b) Break-even: \(-10x^2 + 500x - 5.000 = 0 \Rightarrow x^2 - 50x + 500 = 0 \Rightarrow x = 25 \pm \sqrt{125}\)', 'x ≈ 13,82 und 36,18'),
               (r'c) \(G^{\prime}(x) = -20x + 500 = 0 \Rightarrow x = 25\); \(G^{\prime\prime}(x) = -20 < 0\)', 'Hochpunkt bei 25'),
               (r'd) \(G(25) = -6.250 + 12.500 - 5.000 = 1.250\) €; Umsatz \(E(25) = 13.750 - 9.062{,}5 = 4.687{,}5\) €', 'Gewinn 1.250 €'),
               (r'e) Kapitalrentabilität: \(\frac{1.250}{1.000} = 125\,\%\)', '125 %')],
              'Mit jedem eingesetzten Euro macht der Betrieb 1,25 € Gewinn.')
        + fx('Mitternachtsformel', r'x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}', 'Für \\(ax^2 + bx + c = 0\\). Brauchst du für die Gewinnschwellen bei quadratischem Gewinn.',
             r'\(x^2 - 8x + 12 = 0\): \(x = \frac{8 \pm \sqrt{64 - 48}}{2} = \frac{8 \pm 4}{2}\), also 2 und 6')
        + klausur_hinweis('„Maximaler Gewinn“ kommt regelmäßig. Ableiten, null setzen, einsetzen. Kontrolliere am Ende, ob der Gewinn positiv ist; ein negativer „maximaler Gewinn“ heißt: Das Geschäft lohnt sich nie.')
        + falle('Den Preis beim Gewinnmaximum mit dem Umsatz verwechseln. Umsatz = Preis · Menge = E(x*).')
        + wahr('w-gm', [(r'Das Gewinnmaximum findet man, indem man G(x) = 0 setzt.', False, 'G(x) = 0 liefert die Gewinnschwellen. Fürs Maximum setzt man G\'(x) = 0.'),
                        ("Ist G''(x) negativ, liegt ein Hochpunkt vor.", True, 'Die Kurve ist nach unten gekrümmt.'),
                        (r'Bei G(x) = −x²/2 + 4x − 6 liegt das Maximum bei x = 4.', True, 'G\'(x) = −x + 4 = 0.')]),
    merk='Gewinnmaximum: G(x) = E(x) − K(x); G\'(x) = 0 → x*; G\'\'(x*) < 0 → Hochpunkt; G(x*) = maximaler Gewinn; Umsatz = E(x*). Gewinnschwellen: G(x) = 0 (Mitternachtsformel).',
    exam='Gewinnfunktion aufstellen, Gewinnmaximum und Umsatz dort, Break-even-Mengen; Rentabilität beim Gewinnmaximum.',
    fehler=['G(x) = 0 statt G\'(x) = 0 für das Maximum setzen.', 'Vorzeichen beim Abziehen der Kostenfunktion vergessen (−(−4,5x²) = +4,5x²).', 'Die Preis-Absatz-Funktion nicht mit x multiplizieren.'],
    src='Folien 41, 43')

# ---------------------------------------------------------------- 7 Rentabilitätsmaximum
def rmax_bild():
    X = lambda x: 40 + x * 100
    YG = lambda g: 44 + (-g) * 1.15
    YR = lambda r: 44 + (-r) * 2.9
    s = pfeil(40, 44, 350, 44) + pfeil(40, 250, 40, 20) + T(352, 62, 'x', 13, 700, 'end', 'var(--muted)') + T(32, 48, '0', 12, 400, 'end')
    s += ''.join(strich(X(k), 40, X(k), 48, 'var(--axis)', 1.3, False) + T(X(k), 32, str(k), 12) for k in (1, 2, 3))
    s += kurve(lambda x: -20 * x * x + 40 * x - 80, 0.2, 3.05, X, YG, farbe='var(--c3)')
    s += kurve(lambda x: -10 * x + 20 - 40 / x, 0.62, 3.05, X, YR, farbe='var(--primary)')
    s += strich(X(1), 44, X(1), YG(-60)) + strich(X(2), 44, X(2), YR(-20))
    s += tpg(punkt(X(1), YG(-60), 'var(--c3)', 6), "Gewinnmaximum: G'(x) = −40x + 40 = 0 → x = 1, G(1) = −60. Selbst der beste Gewinn ist ein Verlust.")
    s += tpg(punkt(X(2), YR(-20), 'var(--primary)', 6), "Rentabilitätsmaximum: R(x) = −10x + 20 − 40/x, R'(x) = −10 + 40/x² = 0 → x = 2, R(2) = −20, also −2.000 %.")
    s += T(X(1) - 12, YG(-60) - 12, 'G(1) = −60', 13, 800, 'end', 'var(--c3)') + T(X(2) + 8, YR(-20) - 12, 'R(2) = −20', 13, 800, 'start', 'var(--primary)')
    s += T(X(3) - 18, YG(-140) + 4, 'G(x)', 13, 800, 'end', 'var(--c3)') + T(X(3), YR(-23.3) + 22, 'R(x)', 13, 800, 'end', 'var(--primary)')
    s += T(200, 262, 'unter der Achse: negativ → unrentabel', 12, 600, 'middle', 'var(--muted)')
    return svg(360, 270, s, 'Gewinnfunktion und Rentabilitätsfunktion', maxw=420)

t_rmax = thema('rentmax', 'Rentabilitätsmaximum: nicht dasselbe wie das Gewinnmaximum', star=True,
    kern='Für das Rentabilitätsmaximum stellt man die Rentabilitätsfunktion R(x) = G(x) ÷ Kapital(x) auf, leitet sie ab und setzt R\'(x) = 0. Es liegt meist bei einer anderen Menge als das Gewinnmaximum.',
    kurz=p('Lena überlegt: Lieber möglichst viel Gewinn oder möglichst viel Gewinn <b>je eingesetztem Euro</b>? Wächst das nötige Kapital mit der Menge, sind das zwei verschiedene Fragen.')
        + p('Die <b>Rentabilitätsfunktion</b> teilt den Gewinn durch das Kapital: \\(R(x) = \\frac{G(x)}{\\text{Kap}(x)}\\). Ihr Hochpunkt ist das <b>Rentabilitätsmaximum</b>.'),
    fig=fw('Gewinn und Rentabilität im Folienbeispiel: Die Hochpunkte liegen an verschiedenen Stellen. Tippe auf die Punkte.') + bild(rmax_bild()),
    figcap='Folie 40: G(x) = −20x² + 40x − 80, Kap(x) = 2x (schematisch, Werte negativ nach unten)',
    article=h3('Die Rentabilitätsfunktion')
        + fx('Rentabilitätsfunktion', r'R(x) = \frac{G(x)}{\text{Kap}(x)}', 'Gewinn geteilt durch das eingesetzte Kapital, beides als Funktion der Menge.', r'\(G(x) = -20x^2 + 40x - 80\), \(\text{Kap}(x) = 2x\) → \(R(x) = -10x + 20 - \frac{40}{x}\)')
        + p('Man teilt jeden Summanden durch \\(2x\\): \\(\\frac{-20x^2}{2x} = -10x\\), \\(\\frac{40x}{2x} = 20\\), \\(\\frac{-80}{2x} = -\\frac{40}{x}\\).')
        + weiter('Dann wird wie beim Gewinnmaximum abgeleitet.')
        + h3('Ableiten und null setzen')
        + bsp('Folie 40', r'Gewinn \(G(x) = -20x^2 + 40x - 80\), Kapitalbedarf \(\text{Kap}(x) = 2x\) (nicht die Kostenfunktion!).',
              [(r'a) \(R(x) = -10x + 20 - 40x^{-1}\); \(R^{\prime}(x) = -10 + \frac{40}{x^2} = 0 \Rightarrow x^2 = 4 \Rightarrow x = 2\)', 'x = 2 (nur positiv)'),
               (r'\(R(2) = -20 + 20 - 20 = -20\)', '−2.000 %'),
               (r'b) \(G^{\prime}(x) = -40x + 40 = 0 \Rightarrow x = 1\); \(G(1) = -20 + 40 - 80\)', '−60')],
              'Der „maximale Gewinn“ ist ein Verlust von 60: ein unrentables Geschäft. Und Gewinn- und Rentabilitätsmaximum liegen an verschiedenen Stellen (x = 1 und x = 2).')
        + p('Im Folienbeispiel 39 war das Kapital fest (1.000 €). Dann ist \\(R(x) = \\frac{G(x)}{1.000}\\), und das Rentabilitätsmaximum liegt an derselben Stelle wie das Gewinnmaximum (x = 25, R = 125 %). Nur wenn das Kapital mit der Menge wächst, verschieben sich die Hochpunkte.')
        + falle('Die Lösung x = −2 mitnehmen. Mengen sind nicht negativ, und x = 0 ist verboten (Division durch null).')
        + wahr('w-rmax', [('Gewinn- und Rentabilitätsmaximum liegen immer bei derselben Menge.', False, 'Nur wenn das Kapital konstant ist.'),
                          ("Für das Rentabilitätsmaximum setzt man R'(x) = 0.", True, 'Hochpunkt der Rentabilitätsfunktion.')]),
    merk='Rentabilitätsmaximum: R(x) = G(x) ÷ Kap(x) aufstellen, R\'(x) = 0, nur positive x. Bei konstantem Kapital gleiche Stelle wie das Gewinnmaximum, sonst nicht.',
    exam='Rentabilitätsfunktion aufstellen und ihr Maximum berechnen; mit dem Gewinnmaximum vergleichen.',
    fehler=['Kapitalfunktion mit Kostenfunktion verwechseln.', 'Beim Teilen durch 2x einen Summanden vergessen.'],
    src='Folien 39–40')

# ---------------------------------------------------------------- 8 Produktionsprogramm mit Kapazitätsgrenzen
def lp_bild():
    X = lambda x: 40 + x * 0.42
    Y = lambda y: 236 - y * 0.42
    s = achsen(40, 236, 350, 14, '', 'R') + T(350, 226, 'S', 13, 700, 'end', 'var(--muted)')
    s += flaeche([(X(0), Y(0)), (X(500), Y(0)), (X(375), Y(250)), (X(0), Y(400))], 'var(--pale)', 1)
    s += linie([(X(250), Y(500)), (X(500), Y(0))], 'var(--c1)', 2.2)
    s += linie([(X(0), Y(400)), (X(700), Y(400 - 700 * 0.4))], 'var(--c3)', 2.2)
    s += linie([(X(0), Y(500)), (X(700), Y(500))], 'var(--axis)', 1.3, True) + linie([(X(700), Y(0)), (X(700), Y(520))], 'var(--axis)', 1.3, True)
    s += tpg(punkt(X(375), Y(250), 'var(--primary)', 7), 'Optimum: Schnittpunkt der beiden Kapazitätsgeraden. x + 0,5y = 500 und x + 2,5y = 1.000 → 2y = 500 → y = 250, x = 375. Gewinn 300 · 375 + 200 · 250 = 162.500 €.')
    s += T(X(375) + 10, Y(250) - 10, '(375 | 250)', 13, 800, 'start', 'var(--primary)')
    s += T(X(300), Y(470), 'Facharbeit', 12, 700, 'start', 'var(--c1)') + T(X(20), Y(430), 'Maschinen', 12, 700, 'start', 'var(--c3)')
    s += T(X(160), Y(120), 'zulässig', 13, 700)
    s += T(X(500), 252, '500', 12) + T(X(700), 252, '700', 12) + T(32, Y(400) + 4, '400', 12, 400, 'end') + T(32, Y(500) + 4, '500', 12, 400, 'end')
    return svg(360, 262, s, 'Produktionsprogramm mit zwei Kapazitätsgrenzen', maxw=420)

t_lp = thema('kapazitaet', 'Produktionsprogramm mit Kapazitätsgrenzen',
    kern='Sind Maschinen- und Arbeitsstunden knapp, sucht man die Produktionsmengen mit dem höchsten Gewinn. Die Kapazitäten werden als Ungleichungen geschrieben; das Optimum liegt meist im Schnittpunkt der Grenzgeraden.',
    kurz=p('Lena röstet zwei Sorten: <b>S</b> und <b>R</b>. Ihre Maschine und ihre Mitarbeiter haben nur begrenzt Zeit. Jede Sorte braucht unterschiedlich viel davon und bringt unterschiedlich viel Gewinn.')
        + p('Die Frage: Wie viel von jeder Sorte soll sie herstellen? Man schreibt die Grenzen als <b>Ungleichungen</b>, zeichnet sie und findet das beste Programm meist dort, wo sich zwei Grenzen schneiden.'),
    fig=fw('Die zulässigen Kombinationen (Fläche) und das Optimum. Tippe auf den Punkt.') + bild(lp_bild()),
    figcap='Übung Folie 42 (in der Vorlesung nur angerissen)',
    article=h3('Die Aufgabe')
        + p('Maschinenkapazität 1.000 Stunden, Facharbeit 500 Stunden. Produkt S braucht 1 Stunde Facharbeit und 1 Maschinenstunde, Produkt R 0,5 Stunden Facharbeit und 2,5 Maschinenstunden. Absetzbar sind höchstens 700 Stück S und 500 Stück R. Gewinn: 300 € je S, 200 € je R.')
        + weiter('Zuerst wird alles als Formel aufgeschrieben (a).')
        + h3('a) Formale Darstellung')
        + fx('Modell', r'\max\; G = 300x + 200y \quad \text{u. d. N.} \quad x + 0{,}5y \le 500,\; x + 2{,}5y \le 1.000,\; x \le 700,\; y \le 500,\; x, y \ge 0',
             'x = Stück S, y = Stück R. Zielfunktion Gewinn, dazu Facharbeit, Maschinen, Absatzgrenzen und Nicht-Negativität.', '')
        + h3('b) Grafisch')
        + p('Jede Ungleichung wird zur Geraden, indem man sie als Gleichung nach y auflöst: Facharbeit \\(y = 1.000 - 2x\\), Maschinen \\(y = 400 - 0{,}4x\\). Zulässig ist die Fläche unter beiden Geraden.')
        + h3('c) Optimum rechnerisch')
        + bsp('Schnittpunkt', 'Beide Kapazitätsgeraden gleichsetzen.',
              [(r'\(x + 0{,}5y = 500\) und \(x + 2{,}5y = 1.000\)', ''), (r'Zweite minus erste: \(2y = 500 \Rightarrow y = 250\)', 'y = 250'), (r'Einsetzen: \(x = 500 - 125 = 375\)', 'x = 375'),
               (r'Gewinn \(= 300 \cdot 375 + 200 \cdot 250\)', '162.500 €'), ('Vergleich der Ecken: (500 | 0) → 150.000 €; (0 | 400) → 80.000 €', 'Schnittpunkt ist am besten')])
        + p('Das Vorgehen (Geraden gleichsetzen) solltest du sicher können.')
        + wahr('w-lp', [('Das Optimum liegt bei zwei knappen Kapazitäten oft im Schnittpunkt der Grenzgeraden.', True, 'Dort werden beide Kapazitäten voll genutzt.'),
                        ('Die Absatzgrenze von 700 Stück S ist hier die entscheidende Grenze.', False, 'Schon die Facharbeit erlaubt höchstens 500 Stück S.')]),
    merk='Kapazitätsplanung: Zielfunktion (Gewinn) + Nebenbedingungen als Ungleichungen; Grenzgeraden zeichnen; Optimum meist im Schnittpunkt (Geraden gleichsetzen); Ecken vergleichen.',
    exam='Bedingungen formal aufschreiben und den Schnittpunkt zweier Kapazitätsgeraden berechnen.',
    fehler=['Die Absatzgrenzen für die wichtigste Grenze halten, ohne die Kapazitäten zu prüfen.'],
    src='Folie 42')

# ---------------------------------------------------------------- 9 Liquidität und Eigenkapital
fig_liq = svg(360, 262,
    achsen(40, 216, 350, 40, '', '')
    + strich(40, 216 - 600 * 0.08, 340, 216 - 600 * 0.08, 'var(--neg)', 1.8, True)
    + strich(40, 16, 66, 16, 'var(--neg)', 1.8, True) + T(72, 20, 'kurzfristige Verbindlichkeiten 600.000 €', 12, 700, 'start', 'var(--neg)')
    + tpg(rechteck(64, 216 - 380 * 0.08, 72, 380 * 0.08, 'var(--c2)', 'var(--c2)', 4), 'Liquidität 1. Grades: nur Zahlungsmittel (Kasse I + II = 380.000 €). 380.000 ÷ 600.000 ≈ 63,3 %.')
    + tpg(rechteck(156, 216 - 1200 * 0.08, 72, 1200 * 0.08, 'var(--c2)', 'var(--c2)', 4), 'Liquidität 2. Grades: Zahlungsmittel + Forderungen an Kunden (380.000 + 820.000 = 1,2 Mio. €). 1,2 Mio. ÷ 600.000 = 200 %.')
    + tpg(rechteck(248, 216 - 2100 * 0.08, 72, 2100 * 0.08, 'var(--primary)', 'var(--primary)', 4), 'Liquidität 3. Grades: gesamtes Umlaufvermögen, also auch die Vorräte (380.000 + 820.000 + 900.000 = 2,1 Mio. €). 2,1 Mio. ÷ 600.000 = 350 %.')
    + T(100, 234, '1. Grad', 13, 700) + T(192, 234, '2. Grad', 13, 700) + T(284, 234, '3. Grad', 13, 700)
    + T(100, 252, 'Kasse', 12, 400, 'middle', 'var(--muted)') + T(192, 252, '+ Forderungen', 12, 400, 'middle', 'var(--muted)') + T(284, 252, '+ Vorräte', 12, 400, 'middle', 'var(--muted)')
    + T(100, 216 - 380 * 0.08 - 8, '63 %', 14, 800) + T(192, 216 - 1200 * 0.08 - 8, '200 %', 14, 800) + T(284, 216 - 2100 * 0.08 - 8, '350 %', 14, 800),
    'Liquidität ersten bis dritten Grades', maxw=420)

t_liq = thema('liquiditaet', 'Liquidität, Eigenkapitalquote und Eigenkapitalrendite', star=True,
    kern='Liquidität ist die Fähigkeit, Rechnungen bei Fälligkeit zu zahlen. Liquidität 1., 2. und 3. Grades setzen immer mehr Vermögen ins Verhältnis zu den kurzfristigen Verbindlichkeiten. Eigenkapitalquote = Eigenkapital ÷ Gesamtkapital.',
    kurz=p('Lena kann sehr rentabel sein und trotzdem pleitegehen, wenn am Monatsende das Geld für die Miete fehlt. <b>Liquidität</b> heißt: Rechnungen <b>zum Zeitpunkt der Fälligkeit</b> zahlen können. Kann ein Unternehmen eine fällige Rechnung nicht mehr zahlen, ist es <b>zahlungsunfähig</b>, das führt zur Insolvenz.')
        + p('Man misst die Liquidität in drei Stufen: erst nur das Bargeld, dann mit den Forderungen an Kunden, dann mit den Vorräten. Jedes Mal wird durch die <b>kurzfristigen Verbindlichkeiten</b> geteilt.'),
    fig=fw('Die drei Liquiditätsgrade im Folienbeispiel. Tippe auf die Balken.') + bild(fig_liq),
    figcap='Bilanz aus Folie 44: Bilanzsumme 3,9 Mio. €',
    article=h3('Drei Liquiditätsgrade')
        + fx('Liquidität 1. Grades', r'L_1 = \frac{\text{Zahlungsmittelbestand}}{\text{kurzfristige Verbindlichkeiten}} \cdot 100\,\%', 'Nur das, was bar da liegt (Kasse, Bank).', r'\(\frac{380.000}{600.000} \approx 63{,}3\,\%\)')
        + fx('Liquidität 2. Grades', r'L_2 = \frac{\text{Zahlungsmittel} + \text{kurzfristige Forderungen}}{\text{kurzfristige Verbindlichkeiten}} \cdot 100\,\%', 'Bargeld plus das, was Kunden bald zahlen (kurzfristiges Umlaufvermögen).', r'\(\frac{380.000 + 820.000}{600.000} = 200\,\%\). Mit Bargeld und Forderungen könnte man die Rechnungen doppelt bezahlen.')
        + fx('Liquidität 3. Grades', r'L_3 = \frac{\text{gesamtes Umlaufvermögen}}{\text{kurzfristige Verbindlichkeiten}} \cdot 100\,\%', 'Auch die Vorräte zählen mit.', r'\(\frac{380.000 + 820.000 + 900.000}{600.000} = 350\,\%\)')
        + p('Warum zählen die <b>Vorräte</b> mit, die <b>Grundstücke</b> aber nicht? Vorräte (Handelswaren) haben einen Marktwert und lassen sich, wenn es hart auf hart kommt, schnell verkaufen. Ein Grundstück bekommt man nicht so schnell zu Geld.')
        + tabelle(['Aktiva', '€', 'Passiva', '€'], [
            ['Grundstücke', '1.200.000', 'Eigenkapital', '1.500.000'], ['Maschinen', '600.000', 'Rückstellungen', '250.000'],
            ['Vorräte', '900.000', 'Verbindlichkeiten langfristig', '620.000'], ['Forderungen an Kunden', '820.000', 'Verbindlichkeiten kurzfristig', '600.000'],
            ['Kasse I', '300.000', 'Gewinn', '930.000'], ['Kasse II', '80.000', '', ''], ['Summe', '3.900.000', 'Summe', '3.900.000']])
        + weiter('Mit derselben Bilanz lassen sich auch Kennzahlen zum Eigenkapital rechnen. Die Eigenkapitalquote ist eine Klausuraufgabe.')
        + h3('Eigenkapitalquote und Eigenkapitalrendite')
        + fx('Eigenkapitalquote', r'\text{EK-Quote} = \frac{\text{Eigenkapital}}{\text{Gesamtkapital}} \cdot 100\,\%', 'Welcher Anteil des Kapitals gehört den Eigentümern? Gesamtkapital = Bilanzsumme.', r'\(\frac{1.500.000}{3.900.000} \approx 38{,}5\,\%\)')
        + fx('Eigenkapitalrendite', r'r_{EK} = \frac{\text{Gewinn}}{\text{Eigenkapital}} \cdot 100\,\%', 'Gewinn je Euro Eigenkapital.', r'\(\frac{930.000}{1.500.000} = 62\,\%\)')
        + bsp('Kopfrechnen EK-Quote', 'Eigenkapital 240.000 €, Fremdkapital 360.000 €.',
              [('Gesamtkapital = 240.000 + 360.000', '600.000 €'), (r'\(\frac{240.000}{600.000} = \frac{24}{60} = \frac{2}{5}\)', '40 %')], 'Nicht durch das Fremdkapital teilen! Unten steht das Gesamtkapital.')
        + falle('Bei der EK-Quote durch das Fremdkapital statt durch das Gesamtkapital teilen. Das wäre der Verschuldungsgrad, nicht die Quote.')
        + wahr('w-liq', [('Ein Unternehmen mit hoher Rentabilität kann zahlungsunfähig werden.', True, 'Gewinn auf dem Papier ist kein Geld in der Kasse.'),
                         ('Die Liquidität 1. Grades enthält die Vorräte.', False, 'Nur die Zahlungsmittel; Vorräte erst im 3. Grad.'),
                         ('Eigenkapitalquote = Eigenkapital ÷ Gesamtkapital.', True, 'Gesamtkapital = Bilanzsumme.')]),
    merk='Liquidität = Zahlungsfähigkeit bei Fälligkeit. L1 = Zahlungsmittel, L2 = + Forderungen, L3 = gesamtes Umlaufvermögen, jeweils ÷ kurzfristige Verbindlichkeiten. EK-Quote = EK ÷ Gesamtkapital; EK-Rendite = Gewinn ÷ EK.',
    exam='Eigenkapitalquote und Eigenkapital berechnen (Zahlen gegeben); Liquiditätsgrade zuordnen.',
    fehler=['EK-Quote durch das Fremdkapital teilen.', 'Grundstücke zur Liquidität zählen.'],
    src='Folie 44')

# ---------------------------------------------------------------- 10 Wertschöpfung, Effizienz und Effektivität
fig_eff = svg(360, 190,
    box(4, 4, 170, 110, 'Effizienz\n„die Dinge\nrichtig tun“', size=14, tip='Effizienz = Ergebnis ÷ Aufwand. Eine Kosten-Nutzen-Relation: Wie viel Ergebnis je eingesetztem Euro? Beispiel: Ein Kohlekraftwerk mit 60 % Wirkungsgrad arbeitet effizient.')
    + box(186, 4, 170, 110, 'Effektivität\n„die richtigen\nDinge tun“', size=14, art='hl', tip='Effektivität = Ergebnis ÷ Ziel. Eine Soll-Ist-Relation: Erreichen wir, was wir wollen? Beispiel: Wollen wir überhaupt Kohle verbrennen?')
    + T(89, 136, 'Ergebnis ÷ Aufwand', 13, 700) + T(271, 136, 'Ergebnis ÷ Ziel', 13, 700)
    + T(89, 156, 'Kosten-Nutzen', 12, 400, 'middle', 'var(--muted)') + T(271, 156, 'Soll-Ist', 12, 400, 'middle', 'var(--muted)')
    + T(89, 176, '(Wirkungsgrad)', 12, 400, 'middle', 'var(--muted)') + T(271, 176, '(Wirksamkeit)', 12, 400, 'middle', 'var(--muted)'),
    'Effizienz und Effektivität', maxw=420)

t_eff = thema('effizienz', 'Wertschöpfung, Effizienz und Effektivität',
    kern='Wertschöpfung = Umsatz minus Vorleistungen; sie wird an Mitarbeiter, Fremdkapitalgeber, Eigenkapitalgeber und Staat verteilt. Effizienz heißt „die Dinge richtig tun“ (Ergebnis ÷ Aufwand), Effektivität „die richtigen Dinge tun“ (Ergebnis ÷ Ziel).',
    kurz=p('Lena kauft Rohkaffee für 2 Mio. € und verkauft geröstete Bohnen für 3 Mio. €. Was ihre Rösterei <b>hinzugefügt</b> hat, sind 1 Mio. €: die <b>Wertschöpfung</b>. Davon bekommen die Mitarbeiter Lohn, die Bank Zinsen, die Eigentümer Gewinn und der Staat Steuern.')
        + p('Zwei weitere Maßstäbe klingen ähnlich, sind aber verschieden: <b>Effizienz</b> fragt, ob man ohne Verschwendung arbeitet. <b>Effektivität</b> fragt, ob man überhaupt das Richtige tut.'),
    fig=fw('Die beiden Begriffe nebeneinander. Tippe auf die Kästen.') + bild(fig_eff),
    figcap='nach Folien „Effektivität und Effizienz“',
    article=h3('Wertschöpfung')
        + p('Die <b>Wertschöpfung</b> (value added) ist ein Grundkonzept: das, was ich verkaufe, minus das, was ich an Vorleistungen eingesetzt habe. Dazwischen liegt die „Transformation“ im Betrieb. ' + eg('Der Wert, den der Betrieb selbst hinzufügt.'))
        + fx('Wertschöpfung', r'\text{Wertschöpfung} = \text{Umsatz} - \text{Vorleistungen}', 'Umsatz aus verkauften Produkten und Dienstleistungen minus eingekaufte Vorleistungen.', r'\(3.000.000 - 2.000.000 = 1.000.000\) €')
        + tabelle(['Empfänger', 'erhält', 'im Beispiel'], [['Mitarbeiter', 'Lohn und Gehalt', '600.000 €'], ['Fremdkapitalgeber', 'Zins', '100.000 €'], ['Eigenkapitalgeber', 'Gewinn', '100.000 €'], ['Staat', 'Steuer', '200.000 €'], ['Summe', '', '1.000.000 €']])
        + mfig('Wertschöpfung und ihre Verteilung', svg(560, 250,
            box(8, 10, 160, 56, 'Umsatz\n3.000.000 €', size=13, tip='Verkaufte Produkte und Dienstleistungen.')
            + T(184, 42, '−', 22, 800)
            + box(200, 10, 160, 56, 'Vorleistungen\n2.000.000 €', size=13, tip='Was man eingekauft und eingesetzt hat.')
            + T(376, 42, '=', 22, 800)
            + box(392, 10, 160, 56, 'Wertschöpfung\n1.000.000 €', size=13, art='hl', tip='Der Wert, den der Betrieb durch die Transformation selbst hinzugefügt hat.')
            + pfeil(472, 68, 70, 132) + pfeil(472, 68, 206, 132) + pfeil(472, 68, 342, 132) + pfeil(472, 68, 478, 132)
            + box(8, 134, 128, 70, 'Mitarbeiter\nLohn, Gehalt\n600.000 €', size=13) + box(144, 134, 128, 70, 'FK-Geber\nZins\n100.000 €', size=13)
            + box(280, 134, 128, 70, 'EK-Geber\nGewinn\n100.000 €', size=13) + box(416, 134, 136, 70, 'Staat\nSteuer\n200.000 €', size=13)
            + T(280, 232, 'Die Wertschöpfung wird an vier Gruppen verteilt.', 13, 600, 'middle', 'var(--muted)'),
            'Wertschöpfung und ihre Verteilung'), 'nach Folie „Wertschöpfung“')
        + zusatz('Die ausführliche Wertschöpfungsrechnung eines Konzerns (Umsatzerlöse, Materialaufwand, Abschreibungen … bis Gewinn) ist in den Folien durchgestrichen.')
        + weiter('Nun zu zwei Begriffen, die oft verwechselt werden.')
        + h3('Effizienz und Effektivität')
        + tabelle(['', 'Effizienz', 'Effektivität'], [
            ['Wirkungsdimension', 'Wirkungsgrad', 'Wirksamkeit'], ['Formale Darstellung', 'Ergebnis ÷ Aufwand', 'Ergebnis ÷ Ziel'],
            ['Relation', 'Kosten-Nutzen-Relation', 'Soll-Ist-Relation'], ['Merksatz', 'Die Dinge richtig tun!', 'Die richtigen Dinge tun!']])
        + bsp('Kraftwerk', 'Ein Kohlekraftwerk hat einen Wirkungsgrad von 60 %.',
              [('Es arbeitet <b>effizient</b>: Aus der Kohle wird viel Strom gemacht.', 'Effizienz'), ('Aber: Wollen wir überhaupt Kohle verbrennen? Wäre eine andere Energiequelle für unser Ziel besser?', 'Frage der Effektivität')])
        + p('Lenas Mitarbeiterin packt in Rekordzeit 300 Tüten der Sorte, die keiner kauft: sehr effizient, aber nicht effektiv.')
        + spiel('sp-eff', 'Effizienz oder Effektivität?', ['Effizienz', 'Effektivität'],
                [('Die Röstmaschine verbraucht 10 % weniger Gas pro Kilo', 0, 'Gleiches Ergebnis mit weniger Aufwand'),
                 ('Lena stellt fest, dass Kunden lieber Kapseln wollen, und steigt um', 1, 'Das richtige Produkt für das Ziel'),
                 ('Die Werbekampagne erreicht die geplanten 2.000 Neukunden', 1, 'Ziel erreicht: Soll-Ist'),
                 ('Packen dauert dank neuer Abläufe nur noch halb so lang', 0, 'Kosten-Nutzen')]),
    merk='Wertschöpfung = Umsatz − Vorleistungen; verteilt an Mitarbeiter (Lohn), FK-Geber (Zins), EK-Geber (Gewinn), Staat (Steuer). Effizienz: Dinge richtig tun (Ergebnis ÷ Aufwand). Effektivität: richtige Dinge tun (Ergebnis ÷ Ziel).',
    exam='Effizienz und Effektivität an Beispielen unterscheiden; Wertschöpfung als Umsatz minus Vorleistungen.',
    fehler=['Effizienz und Effektivität vertauschen.', 'Wertschöpfung mit Gewinn gleichsetzen: Der Gewinn ist nur ein Teil davon.'],
    src='Folien 45, 47–48')

KAPITEL = kapitel('k2', 'Wirtschaften und Erfolgskennzahlen',
    'Wie entscheidet ein Betrieb, und wie misst man, ob er gut gewirtschaftet hat? Hier stecken die meisten Rechenaufgaben der Klausur. Durchgehendes Beispiel: Lenas Kaffeerösterei „Bohnenwerk“.',
    ['Obersätze', 'Ökonomisches Prinzip', 'Gewinn und Wirtschaftlichkeit', 'Break-even', 'Rentabilität', 'Gewinnmaximum', 'Rentabilitätsmaximum', 'Kapazitäten', 'Liquidität', 'Effizienz'],
    [t_wirt, t_oek, t_wirtk, t_be, t_rent, t_gmax, t_rmax, t_lp, t_liq, t_eff])

from mehr1 import ergaenze
ergaenze(KAPITEL)
