"""Ergänzungen (Erklärtiefe und weitere Schaubilder) für die Oberthemen 1–6. Wird von k1.py … k6.py eingebunden."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *

MEHR = {}

MEHR['leistungsart'] = (h3('Warum die Einteilung nützlich ist')
    + p('Die Art der Leistung bestimmt, welche Probleme ein Betrieb hat. Ein <b>Sachleistungsbetrieb</b> muss Lager, Material und Maschinen planen: Er kann auf Vorrat produzieren, trägt aber das Risiko, dass Ware liegen bleibt. Ein <b>Dienstleistungsbetrieb</b> muss vor allem seine Kapazität planen: Ein leerer Friseurstuhl um 10 Uhr ist für immer verloren, denn Dienstleistungen kann man nicht lagern.')
    + p('Auch die Kundschaft unterscheidet sich: Produktionsmittelbetriebe verkaufen an andere Betriebe (B2B, business to business), Konsumgüterbetriebe an private Endverbraucher (B2C, business to consumer). Mias Laden verkauft Räder an Privatleute (B2C), ein Großhändler beliefert Läden wie ihren (B2B).')
    + mfig('Vom Rohstoff zum Endkunden', svg(560, 150,
        box(4, 40, 120, 60, 'Kieswerk,\nErzbergbau', size=13, tip='Rohstoffgewinnung (primärer Sektor).')
        + pfeil(126, 70, 144, 70) + box(146, 40, 120, 60, 'Stahlwerk,\nMaschinenbau', size=13, tip='Produktionsmittel: Maschinen für andere Betriebe.')
        + pfeil(268, 70, 286, 70) + box(288, 40, 120, 60, 'Fahrrad-\nhersteller', size=13, tip='Konsumgüter für Endverbraucher.')
        + pfeil(410, 70, 428, 70) + box(430, 40, 126, 60, 'Mias Laden\n(Handel, Service)', size=12, art='hl', tip='Dienstleistung: Handel und Reparatur.')
        + T(64, 124, 'primär', 12, 600, 'middle', 'var(--muted)') + T(277, 124, 'sekundär', 12, 600, 'middle', 'var(--muted)') + T(493, 124, 'tertiär', 12, 600, 'middle', 'var(--muted)'),
        'Wertschöpfungskette über die Sektoren'), 'Beispiel: der Weg eines Fahrrads durch die Sektoren')
    + bsp('Gut einordnen', 'Mia kauft einen Montageständer (500 €), Kettenöl (8 €) und verkauft ein Stadtrad (900 €) an eine Studentin.',
          [('Montageständer: Inputgut, Investitionsgut, Gebrauchsgut, materiell', ''), ('Kettenöl: Inputgut, Verbrauchsgut (Betriebsstoff), materiell', ''), ('Stadtrad: Outputgut, Konsumgut, Gebrauchsgut, eher problemvoll (Beratung nötig)', '')],
          'Dasselbe Gut kann je nach Verwendung anders heißen: Ein Rad für einen Kurierdienst ist ein Investitionsgut, dasselbe Rad für eine Studentin ein Konsumgut.'))

MEHR['dienstleistung'] = (h3('Was das Uno-actu-Prinzip für den Betrieb bedeutet')
    + p('Weil Dienstleistungen nicht lagerbar sind, muss die Kapazität zur Nachfrage passen. Ist samstags die Werkstatt voll und dienstags leer, kann Mia die Dienstag-Stunden nicht für Samstag „aufheben“. Darum arbeiten Dienstleister mit Terminen, Reservierungen, unterschiedlichen Preisen zu Stoßzeiten (Happy Hour, Frühbucherrabatt) und flexiblen Arbeitszeiten.')
    + p('Weil der Kunde beteiligt ist, beeinflusst er das Ergebnis: Eine Kundin, die nicht erklärt, welches Geräusch ihr Rad macht, bekommt eine schlechtere Reparatur. Deshalb ist die Qualität schwankend, und deshalb vertraut man bei Dienstleistungen stark auf Empfehlungen.')
    + tabelle(['Merkmal', 'Folge für den Betrieb'], [['immateriell', 'Qualität vorher schwer prüfbar → Vertrauen, Referenzen, Garantien wichtig'], ['uno actu', 'Anbieter und Kunde müssen zur gleichen Zeit am gleichen Ort sein (oder online verbunden)'],
                                                   ['nicht lagerfähig', 'Kapazität planen, Terminbuchung, Preisstaffeln'], ['schwankende Qualität', 'Standards, Schulungen, Checklisten'], ['Kunde beteiligt', 'Kunde einbeziehen, gut informieren']])
    + mfig('Drei Definitionsversuche', svg(560, 150,
        box(4, 30, 176, 90, '1 Negativdefinition\n„alles, was keine\nSachleistung ist“', size=12, art='weak', tip='Funktioniert nicht: Sie sagt nur, was Dienstleistung nicht ist.')
        + box(192, 30, 176, 90, '2 Enumerative\nDefinition\nAufzählung', size=12, art='weak', tip='Unvollständig: Neue Dienste fehlen immer.')
        + box(380, 30, 176, 90, '3 Merkmals-\ndefinition\nImmaterialität, uno actu …', size=12, art='hl', tip='Der beste Weg: typische Merkmale beschreiben.')
        + pfeil(182, 75, 190, 75) + pfeil(370, 75, 378, 75),
        'Definitionsversuche Dienstleistung'), 'nach Folie „Definition Dienstleistung“'))

MEHR['betriebszweck'] = (h3('Warum öffentliche Betriebe anders ticken')
    + p('Ein öffentliches Unternehmen bekommt seinen Zweck vom Gesetz: Das Bürgeramt muss Pässe ausstellen, egal ob es sich „lohnt“. Es finanziert sich aus Steuern und Gebühren, nicht am Markt. Weil kein Wettbewerb herrscht, gibt es wenig Druck, besser zu werden: „Ich bekomme keinen Termin, habe aber keine andere Wahl.“ Deshalb ist das Ziel die <b>Kostenminimierung</b>: Die vorgegebene Leistung soll möglichst günstig erbracht werden.')
    + p('Ein Privatunternehmen dagegen sucht sich den Zweck selbst (etwa: Arzneimittel herstellen), steht im Wettbewerb, finanziert sich mit Eigen- und Fremdkapital und trägt das Risiko. Sein Globalziel ist die <b>Gewinnmaximierung</b>.')
    + bsp('Zuordnen', 'Welches Ziel passt?',
          [('Die Stadtbibliothek Mannheim', 'Kostenminimierung'), ('Ein Pharmaunternehmen', 'Gewinnmaximierung'), ('Eine Familie plant ihren Urlaub', 'Nutzenmaximierung'), ('Die Stadt finanziert das Nationaltheater', 'Wohlfahrtsmaximierung')]))

MEHR['geschichte'] = (h3('Warum die Positionen bis heute wichtig sind')
    + p('Der Streit zwischen Gemeinnutz und Eigennutz ist nicht vorbei. Er steckt im Gegensatz von <b>Shareholder</b>- und <b>Stakeholder</b>-Ansatz (Oberthema „Positionen der BWL“): Soll ein Unternehmen vor allem den Eigentümern dienen (Eigennutz) oder allen Anspruchsgruppen (Gemeinnutz)? Riegers Gedanke, dass aus Eigennutz Gemeinnutz entsteht, ist die Grundidee der Marktwirtschaft und der „unsichtbaren Hand“.')
    + mfig('Drei Positionen und ihr Nachwirken', svg(560, 160,
        box(4, 20, 176, 70, 'Nicklisch\nGemeinnutz vor\nEigennutz', size=12, tip='Sozialistische Perspektive.') + box(192, 20, 176, 70, 'Schmalenbach\ngemeinwirtschaftliche\nWirtschaftlichkeit', size=12, tip='Kapitalistische Perspektive (laut Vorlesung).') + box(380, 20, 176, 70, 'Rieger\nGemeinnutz kommt\nvom Eigennutz', size=12, art='hl', tip='Kombiniert beides: soziale Marktwirtschaft.')
        + pfeil(92, 92, 160, 120) + pfeil(468, 92, 400, 120)
        + box(140, 114, 280, 40, 'heute: Stakeholder- vs. Shareholder-Ansatz', size=12, art='pale'),
        'Positionen der Gründerzeit'), 'nach Folie „Geschichte der BWL“')
    + p('Seit 1912 ist die BWL ein eigenes Fach neben der VWL: Die VWL betrachtet die ganze Volkswirtschaft (Konjunktur, Inflation, Arbeitslosigkeit), die BWL den einzelnen Betrieb und seine Entscheidungen.'))

MEHR['wirtschaften'] = (h3('Langfristig und unter Nebenbedingungen: was das konkret heißt')
    + p('„Langfristig“ heißt: nicht den schnellen Euro, sondern die dauerhafte Ertragskraft. Lena könnte ihre Stammkunden mit überhöhten Preisen abkassieren und hätte diesen Monat mehr Gewinn, nächstes Jahr aber keine Stammkunden mehr. „Unter Nebenbedingungen“ heißt: Gesetze, Umweltauflagen, Arbeitsschutz und gesellschaftliche Erwartungen gelten immer. Ein Gewinn, der nur durch Regelbruch entsteht, zählt nicht.')
    + mfig('Drei Obersätze und ihr Problem', svg(560, 180,
        box(4, 10, 176, 110, 'Obersatz I\nGewinn\nmaximieren', size=13, art='weak', tip='Problem: Ausverkauf. Kurzfristig bringt es am meisten, alles zu verkaufen.')
        + box(192, 10, 176, 110, 'Obersatz II\nlangfristig Gewinn\nmaximieren', size=13, art='weak', tip='Problem: Auch Betrug kann lange Gewinn bringen.')
        + box(380, 10, 176, 110, 'Obersatz III\nlangfristig unter\nNebenbedingungen', size=13, art='hl', tip='Gültige Lösung: langfristige Gewinnmaximierung unter Beachtung der gesellschaftlichen Vorgaben.')
        + T(92, 146, 'Problem: Ausverkauf', 12, 700, 'middle', 'var(--neg)') + T(280, 146, 'Problem: Betrug', 12, 700, 'middle', 'var(--neg)') + T(468, 146, 'gültig', 12, 700, 'middle', 'var(--pos)')
        + pfeil(182, 65, 190, 65) + pfeil(370, 65, 378, 65),
        'Obersätze'), 'nach Folie „Definition: Wirtschaften (Lösungsweg)“')
    + bsp('Welcher Obersatz wird verletzt?', '',
          [('Ein Unternehmen verkauft seine Produktionsanlagen, um den Jahresgewinn zu verdoppeln.', 'langfristig verletzt (Obersatz I)'), ('Ein Hersteller manipuliert Abgaswerte und spart so jahrelang Kosten.', 'Nebenbedingung verletzt (Obersatz II)'), ('Eine Rösterei investiert in eine energiesparende Anlage, die sich in vier Jahren bezahlt macht.', 'erfüllt Obersatz III')]))

MEHR['oekprinzip'] = (h3('Warum nicht beides zugleich?')
    + p('„Mit möglichst wenig Rohkaffee möglichst viele Packungen“ klingt gut, ist aber unlösbar: Das Minimum an Rohkaffee ist null, dann gibt es null Packungen. Man muss eine Seite festhalten. Entweder ist der Einsatz gegeben (Maximumprinzip), oder das Ergebnis ist gegeben (Minimumprinzip). Beim Optimumprinzip ist zwar keine Seite fest, aber gesucht wird das beste <b>Verhältnis</b>, nicht „alles maximal und alles minimal“.')
    + bsp('Mit Zahlen', 'Lena hat 60 kg Rohkaffee. Aus 1 kg werden 4 Packungen. Eine Packung kostet im Verkauf 12 €, 1 kg Rohkaffee 15 €.',
          [('Maximumprinzip: 60 kg gegeben, möglichst viele Packungen: 60 · 4', '240 Packungen'), ('Ertrag = 240 · 12 €', '2.880 €'), ('Aufwand = 60 · 15 €', '900 €'),
           ('Minimumprinzip: 200 Packungen bestellt, möglichst wenig Rohkaffee: 200 ÷ 4', '50 kg')])
    + mfig('Input und Output in Menge und Euro', svg(560, 160,
        box(4, 30, 170, 90, 'Input (Menge)\n× Faktorpreis\n= Aufwand', size=13, tip='60 kg · 15 € = 900 €')
        + pfeil(176, 75, 194, 75) + box(196, 30, 168, 90, 'Betrieb\n(Transformation)', size=13, art='hl')
        + pfeil(366, 75, 384, 75) + box(386, 30, 170, 90, 'Output (Menge)\n× Güterpreis\n= Ertrag', size=13, tip='240 Packungen · 12 € = 2.880 €'),
        'Input, Output, Aufwand und Ertrag'), 'nach Folie „Ökonomisches Prinzip“'))

MEHR['kennzahlen'] = (h3('Drei Kennzahlen im Vergleich')
    + tabelle(['Kennzahl', 'Formel', 'Einheit', 'Frage'], [['Gewinn', 'Ertrag − Aufwand', 'Euro (absolut)', 'Wie viel bleibt übrig?'], ['Wirtschaftlichkeit', 'Ertrag ÷ Aufwand', 'Verhältniszahl (ohne Einheit)', 'Wie gut ist das Verhältnis in Euro?'], ['Produktivität', 'Output ÷ Input', 'Menge je Menge (z. B. Stück je Stunde)', 'Wie effizient wird mengenmäßig gearbeitet?']])
    + bsp('Kopfrechnen wie in der Klausur', 'Ertrag 84.000 €, Aufwand 70.000 €.',
          [('Gewinn: 84.000 − 70.000', '14.000 €'), (r'Wirtschaftlichkeit: \(\frac{84.000}{70.000} = \frac{84}{70} = \frac{12}{10}\)', '1,2')], 'Tipp: Nullen kürzen, dann mit kleinen Zahlen rechnen.')
    + bsp('Produktivität verbessern', 'Lenas Packerin schafft 120 Packungen in 4 Stunden. Mit einer neuen Waage schafft sie 150 in 4 Stunden.',
          [('vorher: 120 ÷ 4', '30 Packungen/h'), ('nachher: 150 ÷ 4', '37,5 Packungen/h'), ('Steigerung: 7,5 ÷ 30', '+25 %')]))

MEHR['breakeven'] = (h3('Break-even im Kopf: drei Abkürzungen')
    + liste(['Erst die <b>Deckung je Stück</b> bilden (Preis minus variable Kosten), dann die Fixkosten dadurch teilen.', 'Nullen kürzen: \\(\\frac{21.000}{30} = \\frac{2.100}{3} = 700\\).', 'Ist das Ergebnis keine ganze Zahl, muss man <b>aufrunden</b>: Bei 700,4 Stück braucht man 701, um wirklich Gewinn zu machen.'])
    + bsp('Klausurtypisch mit Funktionen', r'Gegeben \(E(x) = 25x\) und \(K(x) = 15x + 3.400\). Bei welcher Menge liegt der Break-even-Punkt?',
          [(r'Gleichsetzen: \(25x = 15x + 3.400\)', ''), (r'\(10x = 3.400\)', ''), (r'\(x = 340\)', '340 Stück')], 'Probe: E(340) = 8.500, K(340) = 5.100 + 3.400 = 8.500. Stimmt.')
    + p('Was passiert bei Änderungen? Steigt der Preis, wird die Deckung je Stück größer und der Break-even-Punkt sinkt. Steigen die Fixkosten (z. B. höhere Miete), steigt er. Steigen die variablen Kosten (teurerer Einkauf), wird die Deckung kleiner und der Break-even-Punkt steigt. Probiere das mit den Reglern oben aus.'))

MEHR['gewinnmax'] = (h3('Warum die Ableitung den Hochpunkt findet')
    + p('Die Ableitung \\(G\'(x)\\) ist die Steigung der Gewinnkurve, also der <b>Grenzgewinn</b>: Wie viel Gewinn bringt ein zusätzliches Stück? Solange \\(G\'(x) > 0\\) ist, lohnt sich jedes weitere Stück. Wird \\(G\'(x) < 0\\), macht jedes weitere Stück den Gewinn kleiner. Genau dazwischen, bei \\(G\'(x) = 0\\), liegt der höchste Punkt. Das ist dasselbe Denken wie Grenznutzen und Grenzkosten (Oberthema „Wirtschaftliche Prinzipien“).')
    + mfig('Gewinnkurve und Steigung', svg(560, 220,
        achsen(40, 190, 540, 14, 'x', 'G(x)')
        + kurve(lambda x: -0.5 * x * x + 4 * x - 6, 0.5, 7.6, lambda x: 40 + x * 64, lambda y: 140 - y * 26, farbe='var(--primary)', w=3)
        + linie([(40 + 2 * 64 - 50, 140 - 0 * 26 + 2 * 26 * 0.78), (40 + 2 * 64 + 50, 140 - 0 * 26 - 2 * 26 * 0.78)], 'var(--c2)', 2)
        + linie([(40 + 4 * 64 - 60, 140 - 2 * 26), (40 + 4 * 64 + 60, 140 - 2 * 26)], 'var(--c3)', 2)
        + punkt(40 + 4 * 64, 140 - 2 * 26, 'var(--c3)', 6) + T(40 + 4 * 64, 140 - 2 * 26 - 14, 'G\'(x) = 0: Hochpunkt', 13, 800, 'middle', 'var(--c3)')
        + T(40 + 2 * 64 - 54, 140 + 40, 'G\'(x) > 0: steigt', 12, 700, 'start', 'var(--c2)') + T(40 + 6 * 64 + 10, 140 - 0 * 26 + 10, 'G\'(x) < 0: fällt', 12, 700, 'start', 'var(--neg)'),
        'Steigung der Gewinnkurve'), 'Gewinnfunktion G(x) = −½x² + 4x − 6')
    + bsp('Kurzaufgabe', r'\(G(x) = -2x^2 + 120x - 1.000\). Gewinnmaximale Menge und maximaler Gewinn?',
          [(r'\(G\'(x) = -4x + 120 = 0\)', 'x = 30'), (r'\(G(30) = -2 \cdot 900 + 3.600 - 1.000 = -1.800 + 3.600 - 1.000\)', '800')]))

MEHR['rentmax'] = (h3('Schritt für Schritt: Rentabilitätsfunktion ableiten')
    + p('Der Trick ist, den Bruch vor dem Ableiten aufzuteilen. Aus \\(R(x) = \\frac{-20x^2 + 40x - 80}{2x}\\) wird \\(R(x) = -10x + 20 - 40x^{-1}\\). Jetzt leitet man jeden Summanden einzeln ab: \\(-10x\\) wird zu \\(-10\\), die Konstante 20 fällt weg, und \\(-40x^{-1}\\) wird zu \\(+40x^{-2} = \\frac{40}{x^2}\\).')
    + fx('Ableitung einer Potenz', r'\left(x^n\right)^{\prime} = n \cdot x^{n-1}', 'Exponent nach vorne, dann Exponent minus eins. Gilt auch für negative Exponenten.', r'\(\left(-40x^{-1}\right)^{\prime} = -40 \cdot (-1) \cdot x^{-2} = \frac{40}{x^2}\)')
    + bsp('Rentabilität bei festem Kapital', 'Gewinnfunktion wie in Folie 39: \\(G(x) = -10x^2 + 500x - 5.000\\), Kapital fest 1.000 €.',
          [(r'\(R(x) = \frac{G(x)}{1.000}\)', ''), (r'Maximum von R dort, wo G maximal ist: \(x = 25\)', ''), (r'\(R(25) = \frac{1.250}{1.000}\)', '125 %')],
          'Teilt man durch eine feste Zahl, verschiebt sich der Hochpunkt nicht. Erst wenn das Kapital mit x wächst, wandert er.'))

MEHR['kapazitaet'] = (h3('Warum das Optimum in einer Ecke liegt')
    + p('Die Gewinnfunktion \\(G = 300x + 200y\\) ist eine Gerade, die man parallel verschieben kann (Isogewinnlinie): Je weiter nach oben rechts, desto höher der Gewinn. Man schiebt sie so weit, bis sie die zulässige Fläche gerade noch berührt. Das passiert immer an einer <b>Ecke</b> der Fläche. Deshalb reicht es, die Ecken zu vergleichen.')
    + tabelle(['Ecke', 'x (S)', 'y (R)', 'Gewinn'], [['Ursprung', '0', '0', '0 €'], ['nur S (Facharbeit voll)', '500', '0', '150.000 €'], ['Schnittpunkt', '375', '250', '162.500 €'], ['nur R (Maschinen voll)', '0', '400', '80.000 €']])
    + p('Am Schnittpunkt sind beide Kapazitäten voll ausgelastet: Facharbeit \\(375 + 0{,}5 \\cdot 250 = 500\\) Stunden, Maschinen \\(375 + 2{,}5 \\cdot 250 = 1.000\\) Stunden.'))

MEHR['liquiditaet'] = (h3('Rentabel und trotzdem pleite?')
    + p('Gewinn und Liquidität sind verschiedene Dinge. Ein Gewinn kann in Forderungen stecken, die erst in drei Monaten bezahlt werden, oder im Lager. Die Miete ist aber am 1. fällig. Deshalb schauen Banken und Lieferanten genau auf die Liquiditätsgrade. Als grobe Faustregel gilt: Die Liquidität 2. Grades sollte mindestens 100 % betragen, sonst kann man die kurzfristigen Schulden nicht aus Kasse und Forderungen bedienen.')
    + bsp('Kopfrechnen EK-Quote rückwärts', 'Die Eigenkapitalquote beträgt 25 %, die Bilanzsumme 800.000 €. Wie hoch ist das Eigenkapital?',
          [('EK = 0,25 · 800.000', '200.000 €'), ('Fremdkapital = 800.000 − 200.000', '600.000 €')])
    + bsp('Liquidität 2. Grades', 'Kasse 30.000 €, Forderungen 50.000 €, Vorräte 40.000 €, kurzfristige Verbindlichkeiten 64.000 €.',
          [(r'\(L_1 = \frac{30.000}{64.000} \approx 46{,}9\,\%\)', ''), (r'\(L_2 = \frac{80.000}{64.000} = 125\,\%\)', ''), (r'\(L_3 = \frac{120.000}{64.000} = 187{,}5\,\%\)', '')]))

MEHR['effizienz'] = (h3('Wertschöpfung rechnen')
    + bsp('Rösterei', 'Lena verkauft geröstete Bohnen für 480.000 €. Sie kauft Rohkaffee, Verpackung und Strom für 300.000 €. Davon zahlt sie 120.000 € Löhne, 10.000 € Zinsen und 20.000 € Steuern.',
          [('Wertschöpfung = 480.000 − 300.000', '180.000 €'), ('Verteilt: 120.000 + 10.000 + 20.000 = 150.000', ''), ('Rest für die Eigentümer: 180.000 − 150.000', '30.000 € Gewinn')],
          'Der Gewinn ist nur der Teil der Wertschöpfung, der den Eigenkapitalgebern bleibt.')
    + p('Effizienz und Effektivität gehören zusammen: Effektiv sein ist wichtiger, denn wer das Falsche sehr effizient tut, verschwendet trotzdem. Ideal ist beides: die richtigen Dinge richtig tun.'))

MEHR['mittelwert'] = (h3('Warum nicht einfach vom alten Wert rechnen?')
    + bsp('Asymmetrie der einfachen Prozentrechnung', 'Preis 10 € → 8 €, Menge 100 → 125.',
          [('Vom alten Wert: Menge +25 %, Preis −20 %: ε = 1,25', ''), ('Rückweg 8 € → 10 €, Menge 125 → 100 vom alten Wert: Menge −20 %, Preis +25 %: ε = 0,8', 'je nach Richtung anders'),
           (r'Mittelwertmethode: Menge \(\frac{25}{112{,}5} \approx 0{,}222\), Preis \(\frac{2}{9} \approx 0{,}222\): ε = 1 in beide Richtungen', 'eindeutig')])
    + mfig('Bogen zwischen zwei Punkten', svg(560, 220,
        achsen(50, 190, 540, 14, 'Menge', 'Preis')
        + kurve(lambda m: 2400 / m, 40, 230, lambda m: 50 + m * 2.1, lambda p: 190 - p * 3.2, farbe='var(--primary)', w=2.5)
        + punkt(50 + 50 * 2.1, 190 - 48 * 3.2, 'var(--c3)', 6) + punkt(50 + 150 * 2.1, 190 - 16 * 3.2, 'var(--c3)', 6)
        + linie([(50 + 50 * 2.1, 190 - 48 * 3.2), (50 + 150 * 2.1, 190 - 16 * 3.2)], 'var(--c3)', 2, True)
        + T(50 + 100 * 2.1, 190 - 32 * 3.2 - 10, 'Bogen: ein Durchschnittswert', 13, 800, 'middle', 'var(--c3)'),
        'Bogenelastizität'), 'Die Mittelwertmethode beschreibt den ganzen Bogen, nicht einen Punkt.')
    + bsp('Klausuraufgabe Parkhaus komplett', '100 Plätze; bisher 50 zu 12 €, jetzt 80 zu 9 €.',
          [(r'Menge: \(\frac{30}{65}\) (Kopf: 30 ÷ 65 ≈ 0,46)', ''), (r'Preis: \(\frac{-3}{10{,}5}\) (Kopf: 3 ÷ 10,5 ≈ 0,286)', ''), (r'\(\varepsilon = \frac{0{,}46}{0{,}286} = \frac{30}{65} \cdot \frac{10{,}5}{3} = \frac{315}{195}\)', '≈ 1,62')],
          'Mit Brüchen statt Dezimalzahlen rechnet es sich ohne Taschenrechner leichter: Doppelbruch auflösen, dann kürzen.'))

MEHR['punktelastizitaet'] = (h3('Warum die Elastizität entlang der Geraden wandert')
    + p('Bei \\(D(p) = 150 - 5p\\) ist die Steigung überall −5. Das Verhältnis \\(\\frac{p}{Q}\\) ändert sich aber: Oben links (hoher Preis, kleine Menge) ist \\(\\frac{p}{Q}\\) groß, unten rechts (niedriger Preis, große Menge) klein. Bei \\(p = 15\\) ist \\(Q = 75\\) und \\(\\varepsilon = 5 \\cdot \\frac{15}{75} = 1\\): genau in der Mitte der Geraden ist die Nachfrage einheitselastisch.')
    + tabelle(['p', 'Q = 150 − 5p', 'ε = 5 · p/Q', 'Bereich'], [['5', '125', '0,2', 'unelastisch'], ['10', '100', '0,5', 'unelastisch'], ['15', '75', '1', 'einheitselastisch'], ['20', '50', '2', 'elastisch'], ['25', '25', '5', 'elastisch']])
    + bsp('Klausurtypisch: vier Antworten', r'\(D(p) = 200 - 4p\), p = 30. Ist ε a) 0,6, b) 1,5, c) 1,25, d) 2,4?',
          [(r'\(Q = 200 - 120 = 80\)', ''), (r'\(\varepsilon = 4 \cdot \frac{30}{80} = \frac{120}{80}\)', 'b) 1,5')]))

MEHR['effekte'] = (h3('Effekte schnell deuten')
    + p('Man muss den Gesamteffekt nicht immer ausrechnen, um seine Richtung zu kennen. Es reicht die Elastizität: Ist die Nachfrage elastisch (ε > 1), bewegen sich Erlös und Menge in dieselbe Richtung; ist sie unelastisch, bewegen sich Erlös und Preis in dieselbe Richtung.')
    + bsp('Parkhaus', '12 € → 9 €, 50 → 80 Plätze (ε ≈ 1,62).',
          [(r'ME = (80 − 50) · 9', '+270 €'), (r'PE = (9 − 12) · 50', '−150 €'), ('GE = 720 − 600', '+120 €')], 'Elastisch und Preissenkung: Der Erlös steigt.')
    + bsp('Unelastisch', 'Benzin: Preis 1,80 € → 2,00 €, Menge 1.000 → 950 Liter (ε ≈ 0,49).',
          [('ME = (950 − 1.000) · 2,00', '−100 €'), ('PE = (2,00 − 1,80) · 1.000', '+200 €'), ('GE = 1.900 − 1.800', '+100 €')], 'Unelastisch und Preiserhöhung: Der Erlös steigt.'))

MEHR['opportunitaet'] = (h3('Opportunitätskosten im Studium')
    + p('Wer studiert, verzichtet auf das Gehalt, das er in der Zeit verdienen könnte. Wer abends Netflix schaut, verzichtet auf Lernzeit oder Schlaf. Opportunitätskosten sind oft kein Geld, sondern entgangene Zeit, Erlebnisse oder Chancen. Sie tauchen in keiner Rechnung auf und sind trotzdem real.')
    + bsp('Zeit als Opportunitätskosten', 'Tom kann am Samstag 8 Stunden im Café jobben (12 €/h) oder zum Festival gehen (Ticket 60 €).',
          [('Kosten des Festivals: Ticket', '60 €'), ('plus entgangener Lohn: 8 · 12', '96 €'), ('volle Kosten des Festivals', '156 €')], 'Wer nur auf das Ticket schaut, unterschätzt, was der Tag kostet.'))

MEHR['grenznutzen'] = (h3('Gesamtnutzen und Grenznutzen')
    + p('Der <b>Gesamtnutzen</b> ist die Summe aller Grenznutzen. Er steigt, solange der Grenznutzen positiv ist, aber immer langsamer. Ist der Grenznutzen null, ist man satt: Der Gesamtnutzen ist am höchsten. Ein negativer Grenznutzen (der zwölfte Schluck, wenn man nicht mehr kann) senkt den Gesamtnutzen sogar.')
    + tabelle(['Schluck', 'Grenznutzen', 'Gesamtnutzen'], [['1', '10', '10'], ['2', '8', '18'], ['3', '6', '24'], ['4', '4,5', '28,5'], ['5', '3', '31,5']])
    + p('Das erklärt das <b>Wasser-Diamanten-Paradox</b>: Wasser ist lebenswichtig (großer Gesamtnutzen), kostet aber fast nichts, weil man genug davon hat (kleiner Grenznutzen). Diamanten sind unwichtig, aber selten: Der Grenznutzen eines weiteren Diamanten ist hoch.'))

MEHR['maerkte'] = (h3('Angebot und Nachfrage im Bild')
    + mfig('Marktgleichgewicht', svg(560, 230,
        achsen(50, 200, 540, 14, 'Menge', 'Preis')
        + linie([(70, 40), (500, 190)], 'var(--c2)', 3) + linie([(70, 190), (500, 40)], 'var(--c3)', 3)
        + T(500, 210, 'Nachfrage', 13, 800, 'end', 'var(--c2)') + T(500, 32, 'Angebot', 13, 800, 'end', 'var(--c3)')
        + punkt(285, 115, 'var(--primary)', 7) + T(295, 108, 'Gleichgewicht: Preis und Menge', 13, 800, 'start', 'var(--primary)')
        + strich(50, 115, 285, 115) + strich(285, 115, 285, 200),
        'Angebot und Nachfrage'), 'Wo sich Angebot und Nachfrage treffen, entsteht der Marktpreis.')
    + p('Ist der Preis zu hoch, bleibt Ware liegen (Angebotsüberschuss), und der Preis sinkt. Ist er zu niedrig, reicht die Ware nicht (Nachfrageüberschuss), und der Preis steigt. Ohne dass jemand plant, finden Angebot und Nachfrage zusammen. Eine Höchstmiete unter dem Gleichgewicht (Mietpreisbremse) erzeugt dauerhaft Nachfrageüberschuss: lange Wartelisten, wenig Neubau.'))

MEHR['innovation'] = (h3('Beispiele für schöpferische Zerstörung')
    + tabelle(['Neues', 'verdrängt', 'Schumpeters Art'], [['Streaming', 'Videotheken, DVDs', 'neues Produkt'], ['Fließband', 'Handfertigung', 'neue Produktionsmethode'], ['Onlinehandel nach China', '–', 'neuer Absatzmarkt'], ['Lithium aus Südamerika für Akkus', '–', 'neuer Beschaffungsmarkt']])
    + bsp('Risiko oder Unsicherheit?', '',
          [('Eine Versicherung kalkuliert Fahrraddiebstähle aus jahrzehntelangen Daten.', 'Risiko'), ('Ein Start-up bringt eine Technik auf den Markt, die es noch nie gab.', 'Unsicherheit'), ('Beim Würfeln auf eine Sechs setzen.', 'Risiko')]))

MEHR['wirtschaftsordnung'] = (h3('Die soziale Marktwirtschaft im Alltag')
    + tabelle(['Politikbereich', 'Beispiel'], [['Wettbewerbspolitik', 'Kartellamt verbietet Preisabsprachen'], ['Einkommens- und Vermögenspolitik', 'progressive Einkommensteuer'], ['Struktur- und Wachstumspolitik', 'Förderung strukturschwacher Regionen'], ['Konjunkturpolitik', 'Konjunkturpakete in der Krise'], ['Sozialpolitik', 'Arbeitslosen-, Kranken-, Rentenversicherung']])
    + p('Die Idee: Der Markt sorgt für Wohlstand und Effizienz, der Staat für Fairness und Absicherung. Wie viel Staat genau, ist eine politische Dauerfrage.'))

MEHR['homo-oeconomicus'] = (h3('Wo der homo oeconomicus scheitert')
    + p('Im Supermarkt stehen 40 Joghurtsorten. Der homo oeconomicus würde Preis, Geschmack und Inhaltsstoffe aller Sorten vergleichen und die beste wählen. Echte Menschen nehmen die gewohnte Sorte oder die, die auf Augenhöhe steht. Nicht aus Dummheit: Die Suche kostet Zeit, und die Zeit ist mehr wert als der kleine Vorteil.')
    + mfig('Zeitstrahl der Perspektiven', svg(560, 120,
        linie([(20, 60), (540, 60)], 'var(--axis)', 2)
        + box(20, 20, 160, 80, 'bis 1960er/70er\nökonomisch\n(homo oeconomicus)', size=12, art='weak') + box(200, 20, 160, 80, 'ca. 1970–2000\nverhaltens-\nwissenschaftlich', size=12, art='weak') + box(380, 20, 160, 80, 'seit ca. 2000\nbeide verbinden', size=12, art='hl'),
        'Zeitstrahl'), 'nach Folie „Ökonomische und Verhaltenswissenschaftliche BWL“'))

MEHR['shareholder-value'] = (h3('Rendite gegen Zins vergleichen')
    + fx('Kapitalrendite des Unternehmens', r'r = \frac{E - A}{K}', 'Ergebnis aus der Unternehmenstätigkeit geteilt durch das eingesetzte Kapital.', r'\(\frac{110.000}{1.000.000} = 11\,\% > 8\,\%\)')
    + p('Ist r größer als der Zins der Alternativanlage i, schafft das Unternehmen Wert für die Eigentümer (Shareholder Value). Ist r kleiner, vernichtet es Wert, obwohl es vielleicht Gewinn macht: Die Eigentümer hätten ihr Geld besser angelegt.')
    + bsp('Gewinn, aber Wertvernichtung', 'Kapital 2 Mio. €, Alternativzins 5 %, E − A = 70.000 €.',
          [('Messlatte K · i = 2.000.000 · 0,05', '100.000 €'), ('70.000 € < 100.000 €', 'kein Mehrwert'), ('Rendite 70.000 ÷ 2.000.000', '3,5 % < 5 %')]))

MEHR['werturteile'] = (h3('Werturteile erkennen')
    + bsp('Primär oder sekundär?', '',
          [('„Unternehmen sollten nicht nur auf Gewinn achten, sondern auch das Klima schützen.“', 'primär (bewertet ein Ziel)'), ('„Um die Kosten zu senken, ist Leasing hier günstiger als Kauf.“', 'sekundär (bewertet ein Mittel)'),
           ('„Kinderarbeit in der Lieferkette ist unvertretbar.“', 'primär'), ('„Für das Ziel Kundenbindung ist ein Bonusprogramm wirksamer als Rabatte.“', 'sekundär')])
    + p('Die ökonomische BWL hält sich mit Wertungen über Ziele zurück: Sie sagt nicht, ob Gewinnmaximierung gut ist, sondern wie man sie am besten erreicht. Die verhaltenswissenschaftliche BWL scheut sich nicht, auch Ziele zu bewerten, etwa im Personalwesen bei Fragen von Fairness und Motivation.')
    + mfig('Werturteile in der Übersicht', svg(560, 170,
        box(180, 6, 200, 40, 'Werturteilsfrage', size=13, art='pale') + pfeil(240, 48, 120, 66) + pfeil(320, 48, 440, 66)
        + box(20, 68, 200, 90, 'primär\nabsolutes Urteil\nbewertet Ziele\nethisch-normativ', size=12) + box(340, 68, 200, 90, 'sekundär\nabgeleitetes Urteil\nbewertet Mittel\npraktisch-normativ', size=12, art='hl'),
        'Werturteile'), 'nach Folie „Werturteile“'))

MEHR['et-ueberblick'] = (h3('Ein Beispiel für beide Richtungen')
    + p('Die Eisdiele überlegt, ob sie einen zweiten Laden eröffnet. Die <b>klassische</b> Entscheidungstheorie würde sagen: Liste alle Standorte, bewerte sie nach deinen Zielen, rechne die Ergebnisse für jeden möglichen Sommer aus und wähle nach einer klaren Regel. Die <b>verhaltenswissenschaftliche</b> Entscheidungstheorie beobachtet: Der Inhaber schaut sich zwei Läden an, die ein Bekannter empfohlen hat, und nimmt den ersten, der „gut genug“ ist.')
    + p('Beides hat seinen Platz: Die klassische Theorie zeigt, wie man es besser machen kann (Training für rationale Entscheidungen). Die verhaltenswissenschaftliche erklärt, warum es in der Praxis anders läuft.')
    + tabelle(['Würdigung der klassischen ET', ''], [['positiv', 'hilft, Probleme vorher (ex ante) zu strukturieren; Training für rationale Entscheidungen'], ['negativ', 'Modell einer idealen Welt, unrealistisch (homo oeconomicus)']]))

MEHR['et-struktur'] = (h3('Strukturieren an einem zweiten Beispiel')
    + bsp('Neue Eissorte', 'Die Eisdiele will eine neue Sorte einführen.',
          [('Zielsystem: möglichst viel Umsatz, Image als „kreative“ Eisdiele, geringe Zusatzkosten', ''), ('Alternativen: Pistazie-Salz, Mango-Chili, Gurke-Minze', ''), ('Umwelteinflüsse: Wetter im Sommer, Trends in sozialen Medien, Preis für Pistazien', '')])
    + mfig('Stufen eines Entscheidungsproblems', svg(560, 180,
        box(180, 6, 200, 36, 'Entscheidungsproblem', size=13, art='pale') + pfeil(280, 44, 280, 56)
        + rechteck(10, 58, 540, 80, 'var(--pale-2)', 'var(--line)', 10) + T(20, 76, 'Stufe 1: Strukturierung', 12, 800, 'start')
        + box(30, 86, 230, 44, 'Zielsystem: Präferenzen', size=12) + box(300, 86, 230, 44, 'Entscheidungsfeld: Alternativen, Umwelt', size=12)
        + pfeil(280, 140, 280, 150) + box(180, 152, 200, 26, 'Stufe 2: Lösungsfindung', size=12, art='hl'),
        'Zwei Stufen'), 'nach Folie „Klassische Entscheidungstheorie: Visualisierung“'))

MEHR['zielbeziehungen'] = (h3('Zielbeziehungen sind nicht immer gleich')
    + p('Ob zwei Ziele sich helfen oder stören, kann vom Bereich abhängen. Umsatz und Gewinn sind meist komplementär. Wenn man aber den Umsatz nur noch mit Rabattschlachten steigern kann, sinkt der Gewinn: Dann werden sie konkurrierend. Auch Kosten und Qualität konkurrieren oft, aber eine bessere Qualitätskontrolle kann Reklamationskosten senken; dann sind sie für eine Weile komplementär.')
    + bsp('Einordnen', '',
          [('Mehr Werbung und höherer Bekanntheitsgrad', 'komplementär'), ('Höhere Löhne und niedrigere Personalkosten', 'konkurrierend'), ('Neues Logo und kürzere Lieferzeiten', 'indifferent'), ('Mehr Bio-Zutaten und niedrigere Einkaufspreise', 'konkurrierend')])
    + p('Bei konkurrierenden Zielen muss man eine Lösung finden: ein Ziel dominieren lassen, nur effiziente Alternativen betrachten, die Ziele der Reihe nach abarbeiten oder gewichten (nächstes Unterthema).'))

MEHR['zielsystem'] = (h3('Welche Methode wann?')
    + tabelle(['Methode', 'passt, wenn …', 'Schwäche'], [['Zieldominanz', 'ein Ziel klar am wichtigsten ist', 'alle anderen Ziele werden ignoriert'], ['Effizienz', 'man erst einmal aussortieren will', 'meist bleiben mehrere Alternativen übrig'],
                                                   ['lexikographisch', 'Ziele sich klar ranken lassen', 'kleine Vorteile im wichtigsten Ziel schlagen große in den anderen'], ['Nutzenfunktion', 'man Ziele gegeneinander abwägen will', 'Gewichte sind subjektiv; ohne Normierung Verzerrung']]))


def ergaenze(kapitel):
    """hängt die Ergänzungen vor den Kurz-Check an"""
    for t in kapitel['themen']:
        extra = MEHR.get(t['id'])
        if not extra:
            continue
        a = t['article']
        i = a.find('<h3>Kurz-Check')
        t['article'] = a[:i] + extra + a[i:] if i >= 0 else a + extra
    return kapitel
