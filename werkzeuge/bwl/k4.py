import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *

# Durchgehendes Beispiel: Robinson Crusoe auf seiner Insel, dazu Alltagsfälle aus der Mensa.

# ---------------------------------------------------------------- 1 Alternativen und Opportunitätskosten (Rechner)
t_opp = thema('opportunitaet', 'Abwägen und Opportunitätskosten', star=True, wide=True,
    kern='Wer sich für etwas entscheidet, verzichtet auf etwas anderes. Opportunitätskosten sind der entgangene Nutzen der besten nicht gewählten Alternative.',
    kurz=p('In der Mensa gibt es Spaghetti und Milchreis. Du nimmst den Milchreis. Was hat dich das gekostet? Nicht nur die 3,50 €, sondern auch die <b>Spaghetti, die du nicht gegessen hast</b>. Das sind die <b>Opportunitätskosten</b>: der Nutzen der besten Alternative, auf die du verzichtest.')
        + p('Robinson Crusoe hat auf seiner Insel 12 Stunden Tageslicht. Er kann Wildschweine jagen (5 am Tag) oder Wasser holen (10 Liter am Tag). Jede Stunde Jagd fehlt beim Wasser. 1 Wildschwein „kostet“ ihn 2 Liter Wasser.'),
    fig=fw('Robinsons Tag: Verteile die 12 Stunden. Der Punkt wandert auf der Grenze dessen, was möglich ist. Mit dem zweiten Regler erfindet Robinson eine Falle.')
        + regler([('robH', 'Stunden Jagd (Rest: Wasser)', 0, 12, 1, 6, 'h'), ('robF', 'Wildschweine pro Tag (Fortschritt)', 5, 10, 5, 5, 'Stück')])
        + '<svg id="figROB" viewBox="0 0 360 260" style="max-width:420px;width:100%;margin:0 auto;display:block" role="img" aria-label="Robinsons Möglichkeiten"></svg>'
        + schritte_karten([('① Ertrag Jagd', 'robR1', '#robT1'), ('② Ertrag Wasser', 'robR2', '#robT2'), ('③ Opportunitätskosten', 'robR3', '#robT3')]),
    figcap='Übung „Ein-Personen-Welt: Robinson Crusoe“ (Folie 70)',
    article=h3('Prinzip 1: Alle Menschen stehen vor abzuwägenden Alternativen')
        + p('„There is no such thing as a free lunch“ (Milton Friedman). ' + eg('Nichts ist umsonst.') + ' Wer etwas bekommt, gibt etwas anderes auf. Daraus entstehen <b>Zielkonflikte</b>: Freizeit oder Lernen, Brötchen oder Kaffee.')
        + weiter('Wenn alles etwas kostet: Was genau sind die Kosten?')
        + h3('Prinzip 2: Die Kosten eines Gutes bestehen in dem, was man dafür aufgibt')
        + p('Jede Handlung hat einen Preis. Zielkonflikte verlangen Entscheidungen durch <b>Vergleich von Kosten und Nutzen</b>. Hast du nur 1 € und kannst entweder ein Brötchen oder einen Kaffee kaufen, musst du dich entscheiden. Die Frage lautet: Was gebe ich auf, was kann ich mir danach nicht mehr leisten?')
        + p('<b>Opportunitätskosten</b> sind der <b>entgangene Nutzen der besten nicht gewählten Handlungsalternative</b>. ' + eg('Das, worauf du verzichtest, wenn du dich anders entscheidest.'))
        + bsp('Mensa: Spaghetti oder Milchreis', 'Es gibt Spaghetti und Milchreis. Man entscheidet sich für den Milchreis. Was sind die Opportunitätskosten?',
              [('Gewählt: Milchreis. Nicht gewählt: Spaghetti.', ''), ('Opportunitätskosten = Nutzen der besten nicht gewählten Alternative', 'die Spaghetti')],
              'Nicht der Milchreis selbst, nicht beides und nicht „keine“: Es gibt immer Opportunitätskosten, wenn es eine Alternative gibt.')
        + bsp('Mensa mit drei Gerichten', 'Es gibt Spaghetti und Suppe. An der Kasse merkst du, dass es dein Lieblingsessen Gulasch gibt, und nimmst Gulasch.',
              [('Gewählt: Gulasch. Nicht gewählt: Spaghetti und Suppe.', ''), ('Opportunitätskosten: der Nutzen der <b>besten</b> davon, nicht die Summe beider', 'das bessere der beiden anderen Gerichte')])
        + weiter('Die Robinson-Übung zeigt dasselbe mit Zahlen.')
        + h3('Robinson Crusoe: eine Ein-Personen-Welt')
        + p('Grundbedürfnisse: Hunger und Durst. Verfügbare Zeit: 12 Stunden Helligkeit, das Maximum dessen, was machbar ist. Alternative 1: Wildschweinjagd (5 Wildschweine in 12 h). Alternative 2: Wasser holen (10 Liter in 12 h).')
        + bsp('Die drei Fragen der Übung', '',
              [('a) Handlungsmöglichkeiten: alle Kombinationen auf und unter der Geraden von (0 Schweine | 10 Liter) bis (5 Schweine | 0 Liter). Auf der Linie nutzt er die Zeit voll aus, darunter verschenkt er Zeit, darüber ist unmöglich.', ''),
               (r'b) Opportunitätskosten: 1 Wildschwein mehr kostet \(\frac{10}{5} = 2\) Liter Wasser; 1 Liter Wasser kostet \(\frac{5}{10} = 0{,}5\) Wildschweine.', '1 Schwein = 2 l'),
               ('c) Technischer Fortschritt: Mit einer Falle fängt er 10 statt 5 Schweine. Die Linie dreht sich nach außen, mehr Kombinationen sind möglich, und ein Wildschwein kostet nur noch 1 Liter Wasser. Ein größerer Eimer würde die Linie zur anderen Seite drehen.', 'Linie dreht nach außen')])
        + klausur_hinweis('Opportunitätskosten sind sehr häufig gefragt, oft mit Mensa- oder Robinson-Beispielen. Immer fragen: Was ist die beste Alternative, auf die verzichtet wird?')
        + falle('Die gewählte Alternative als Opportunitätskosten nennen. Opportunitätskosten sind immer das Nicht-Gewählte.')
        + wahr('w-opp', [('Opportunitätskosten sind der Preis, den man für die gewählte Alternative zahlt.', False, 'Sie sind der entgangene Nutzen der besten nicht gewählten Alternative.'),
                         ('Bei Robinson kostet 1 Wildschwein 2 Liter Wasser.', True, '10 Liter ÷ 5 Schweine.'),
                         ('Wer zwischen drei Gerichten wählt, hat als Opportunitätskosten die Summe der beiden anderen.', False, 'Nur die beste nicht gewählte Alternative zählt.'),
                         ('„There is no such thing as a free lunch“ heißt: Nichts ist umsonst.', True, 'Prinzip 1.')]),
    merk='Prinzip 1: Alle stehen vor abzuwägenden Alternativen (kein „free lunch“). Prinzip 2: Kosten = was man aufgibt. Opportunitätskosten = entgangener Nutzen der besten nicht gewählten Alternative. Robinson: 1 Schwein = 2 Liter Wasser.',
    exam='Opportunitätskosten in Alltagsfällen bestimmen (Mensa, Robinson); Handlungsmöglichkeiten und Wirkung von technischem Fortschritt.',
    fehler=['Die gewählte Alternative als Opportunitätskosten angeben.', 'Bei mehreren Alternativen alle aufsummieren statt nur die beste zu nehmen.', '„Es gibt keine Opportunitätskosten“ ankreuzen.'],
    src='Folien 69–71')

# ---------------------------------------------------------------- 2 Denken in Grenzbegriffen
def grenz_bild():
    werte = [10, 8, 6, 4.5, 3, 2, 1.2]
    s = achsen(48, 212, 350, 14, '', 'Grenznutzen') + T(44, 228, 'Schluck', 12, 600, 'end', 'var(--muted)')
    for i, w in enumerate(werte):
        x = 52 + i * 42
        s += tpg(rechteck(x, 212 - w * 18, 32, w * 18, 'var(--primary)' if i == 0 else 'var(--c2)', 'none', 3),
                 f'Grenznutzen des {i + 1}. Schlucks: {str(w).replace(".", ",")}. ' + ('Der erste Schluck nach dem Durst ist am wertvollsten.' if i == 0 else 'Jeder weitere Schluck bringt weniger zusätzlichen Nutzen.'))
        s += T(x + 16, 228, str(i + 1), 12)
    s += strich(40, 212 - 3.5 * 18, 345, 212 - 3.5 * 18, 'var(--c3)', 2, True)
    s += T(345, 212 - 3.5 * 18 - 8, 'Grenzkosten', 13, 800, 'end', 'var(--c3)')
    s += T(196, 252, 'trinken, solange Grenznutzen > Grenzkosten', 13, 700, 'middle', 'var(--muted)')
    return svg(360, 262, s, 'Abnehmender Grenznutzen', maxw=420)

t_grenz = thema('grenznutzen', 'Denken in Grenzbegriffen: Grenznutzen und Grenzkosten', star=True,
    kern='Rational entscheidende Menschen denken in Grenzbegriffen: Sie fragen, was die nächste zusätzliche Einheit an Nutzen bringt und kostet. Der Grenznutzen nimmt in der Regel ab.',
    kurz=p('Robinson kommt durstig vom Strand zurück. Der <b>erste</b> Schluck Wasser ist unglaublich viel wert. Der zweite auch noch viel, der zehnte kaum noch. Was eine <b>zusätzliche</b> Einheit an Nutzen bringt, heißt <b>Grenznutzen</b>. Er wird mit jedem Schluck kleiner.')
        + p('Auf der anderen Seite stehen die <b>Grenzkosten</b>: Was kostet die nächste Einheit? Rational ist es, so lange weiterzumachen, wie der Grenznutzen größer ist als die Grenzkosten.'),
    fig=fw('Grenznutzen beim Trinken. Tippe auf die Balken.') + bild(grenz_bild()),
    figcap='nach Folie „Prinzip 3: Rational entscheidende Menschen denken in Grenzbegriffen“',
    article=h3('Prinzip 3: Rational entscheidende Menschen denken in Grenzbegriffen')
        + p('Wichtige Entscheidungen sind selten „alles oder nichts“. Meist geht es um <b>marginale Änderungen</b>: ein bisschen mehr oder weniger. Man fragt: Was kostet mich das Nächste? Was bringt mir das Nächste? Das ist eine sinnvolle Abwägung für zukünftige Entscheidungen.')
        + cards([('Grenznutzen', 'zusätzlicher Nutzen durch eine weitere Einheit, die man konsumiert'), ('Grenzkosten', 'zusätzliche Kosten durch eine weitere Einheit, die man herstellt oder kauft')])
        + p('„Grenznutzen und Grenzkosten sind zwei der wichtigsten Kernkonzepte der Wirtschaftswissenschaften. Sie beschreiben, wie sich der Nutzen für einen Verbraucher oder die Kosten für einen Produzenten verändern, wenn genau eine zusätzliche Einheit eines Gutes konsumiert oder hergestellt wird.“')
        + weiter('Typisch ist, dass der Nutzen am Anfang hoch ist und dann abflacht.')
        + h3('Abnehmender Grenznutzen')
        + p('Der Nutzen ist häufig am Anfang hoch und flacht dann ab. Jeder weitere Schluck Wasser, jedes weitere Stück Pizza bringt weniger zusätzliche Zufriedenheit als das vorige.')
        + bsp('Wasser ist lebensnotwendig', 'Wasser ist lebensnotwendig. Der Grenznutzen ist also: klein, groß, abnehmend oder zunehmend?',
              [('Lebensnotwendig heißt: Der <b>Gesamtnutzen</b> ist groß.', ''), ('Gefragt ist aber der <b>Grenznutzen</b>, der Nutzen jedes weiteren Schlucks.', ''), ('Mit jedem Schluck wird man weniger durstig.', 'abnehmend')],
              'Die Falle: „lebensnotwendig“ verleitet zu „groß“. Der Nutzen nimmt aber mit jedem Schluck ab.')
        + bsp('Grenzkosten in der Arbeit', 'Wie viele Fehler darf man machen, um Zeit zu sparen?',
              [('Mehr Tempo spart Zeit (Nutzen), erzeugt aber Fehler (Kosten).', ''), ('Man wird schneller, solange die Kosten der zusätzlichen Fehler kleiner sind als der Nutzen der gesparten Zeit.', 'Grenznutzen = Grenzkosten')])
        + falle('Gesamtnutzen und Grenznutzen verwechseln. Ein Gut kann insgesamt sehr wertvoll sein (Wasser) und trotzdem einen abnehmenden Grenznutzen haben.')
        + wahr('w-grenz', [('Der Grenznutzen ist der Nutzen einer zusätzlichen Einheit.', True, 'Definition.'),
                           ('Weil Wasser lebensnotwendig ist, steigt sein Grenznutzen mit jedem Schluck.', False, 'Er nimmt ab.'),
                           ('Rational ist es, eine Einheit mehr zu konsumieren, solange ihr Grenznutzen über den Grenzkosten liegt.', True, 'Danach lohnt sie sich nicht mehr.')]),
    merk='Prinzip 3: in Grenzbegriffen denken, marginale Änderungen abwägen. Grenznutzen = Nutzen einer zusätzlichen Einheit, meist abnehmend. Weitermachen, solange Grenznutzen > Grenzkosten.',
    exam='Grenznutzen in Alltagsfällen einordnen (Wasser: abnehmend); Grenznutzen und Grenzkosten abwägen.',
    fehler=['„Lebensnotwendig“ mit „großem Grenznutzen“ gleichsetzen.', 'Grenz- und Gesamtgrößen vermischen.'],
    src='Folien 72, 108')

# ---------------------------------------------------------------- 3 Anreize, Märkte und Staat
fig_markt = svg(360, 250,
    box(4, 6, 352, 58, 'Regel 4 · Menschen reagieren auf Anreize', size=13, tip='Rationales Verhalten reagiert auf Veränderungen von Kosten und Nutzen. Werden Kontrollen selten, fahren mehr Menschen schwarz. Achtung: unbeabsichtigte Konsequenzen.')
    + pfeil(180, 66, 180, 82)
    + box(4, 84, 352, 72, 'Regel 5 · Märkte können die\nEntscheidungen organisieren', size=13, art='hl', tip='Angebot und Nachfrage treffen sich am Markt und bilden Preise. Jeder verfolgt sein eigenes Interesse, die „unsichtbare Hand“ (Adam Smith) lenkt das zum Vorteil aller.')
    + pfeil(180, 158, 180, 174)
    + box(4, 176, 352, 66, 'Regel 6 · Staaten können\nMarktergebnisse manchmal verbessern', size=13, tip='Der Staat stellt Märkte bereit, schützt sie (z. B. gegen Kartelle) und kontrolliert sie. Eingriffe haben aber oft Nebenwirkungen (Mindestlohn, Mietpreisbremse).'),
    'Anreize, Märkte und Staat', maxw=420)

t_markt = thema('maerkte', 'Anreize, Märkte und die Rolle des Staates',
    kern='Menschen reagieren auf Anreize (Regel 4). Märkte organisieren Entscheidungen über Angebot und Nachfrage, gelenkt von der „unsichtbaren Hand“ (Regel 5). Der Staat kann Marktergebnisse manchmal verbessern (Regel 6), Eingriffe haben aber Nebenwirkungen.',
    kurz=p('Wenn in der Straßenbahn kaum noch kontrolliert wird, fahren mehr Leute schwarz: Menschen reagieren auf <b>Anreize</b>. Wenn eine Bäckerei morgens frische Brötchen anbietet, tut sie das nicht aus Nächstenliebe, sondern weil sie damit Geld verdient. Trotzdem haben alle etwas davon. Das ist die <b>unsichtbare Hand des Marktes</b>.')
        + p('Manchmal greift der <b>Staat</b> ein, etwa gegen Preisabsprachen. Gut gemeinte Eingriffe können aber unbeabsichtigte Folgen haben.'),
    fig=fw('Drei Regeln, die zusammengehören. Tippe auf die Kästen.') + bild(fig_markt),
    figcap='nach Folien „Funktionsweise wirtschaftlicher Prinzipien“, Regeln 4–6',
    article=h3('Regel 4: Menschen reagieren auf Anreize')
        + p('Rationales Verhalten reagiert auf Veränderungen von Kosten und Nutzen. Wird etwas teurer, macht man es seltener; wird es belohnt, öfter. Beispiel <b>Schwarzfahren</b>: Je seltener kontrolliert wird und je niedriger die Strafe, desto mehr Menschen fahren ohne Ticket.')
        + p('Es besteht die <b>Gefahr unbeabsichtigter Konsequenzen</b>. Ein Beispiel ist die Verdrängung der Motivation: Wer etwas aus eigener Überzeugung tut (<b>intrinsische Motivation</b>), macht es oft weniger gern, sobald man es bezahlt (<b>extrinsische Motivation</b>).')
        + weiter('Wenn jeder auf seine Anreize reagiert: Wer sorgt dann dafür, dass am Ende alles zusammenpasst?')
        + h3('Regel 5: Märkte können die Entscheidungen organisieren')
        + p('Auf dem Markt treffen <b>Angebot und Nachfrage</b> aufeinander. Der Preis gleicht beides aus. Adam Smith nannte das die <b>unsichtbare Hand</b>: „Nicht vom Wohlwollen des Fleischers, Brauers oder Bäckers erwarten wir unsere Mahlzeit, sondern von ihrer Bedachtnahme auf ihr eigenes Interesse.“ Wer sein eigenes Interesse verfolgt, befördert das der Gesellschaft oft wirksamer, als wenn er es direkt wollte.')
        + tabelle(['Welt ohne …', 'Problem'], [
            ['Geld', 'Tausch nur bei doppelter Übereinstimmung der Wünsche: Ich muss jemanden finden, der hat, was ich will, und will, was ich habe.'],
            ['Unternehmen', 'doppelte Übereinstimmung der Fähigkeiten und Wünsche: Jeder müsste alles selbst können.'],
            ['Märkte', 'keine Preisfindung']])
        + p('Greift die Politik in den Markt ein, wird er oft nicht besser. Beispiele: <b>Mietpreisbremse</b> (weniger Neubau), festgelegte Preise in der <b>DDR</b> (schlechtere Qualität, zu wenig Menge). Man kann den Markt nicht austricksen.')
        + weiter('Ganz ohne Staat geht es aber auch nicht.')
        + h3('Regel 6: Staaten können Marktergebnisse manchmal verbessern')
        + cards([('Bereitstellen von Märkten', 'Infrastruktur, Rechtssystem, Eigentumsrechte'), ('Marktschutz', 'z. B. gegen Kartelle, also Preisabsprachen mehrerer Unternehmen'), ('Marktkontrolle', 'Regeln und Aufsicht, z. B. Mindestlohn')])
        + p('Eingriffe haben Nebenwirkungen: Ein <b>Mindestlohn</b> schützt Beschäftigte, kann aber dazu führen, dass weniger billige Arbeitskräfte eingestellt werden, Arbeit in den Schwarzmarkt oder ins Ausland abwandert.')
        + wahr('w-markt', [('Die „unsichtbare Hand“ geht auf Adam Smith zurück.', True, 'Eigeninteresse lenkt zum Vorteil aller.'),
                           ('Ohne Geld bräuchte jeder Tausch eine doppelte Übereinstimmung der Wünsche.', True, 'Darum ist Geld so nützlich.'),
                           ('Staatliche Eingriffe in Märkte haben keine Nebenwirkungen.', False, 'Mindestlohn, Mietpreisbremse: unbeabsichtigte Folgen.'),
                           ('Schwarzfahren nimmt zu, wenn seltener kontrolliert wird.', True, 'Regel 4: Anreize.')]),
    merk='Regel 4: Menschen reagieren auf Anreize (Gefahr unbeabsichtigter Folgen). Regel 5: Märkte organisieren Entscheidungen, unsichtbare Hand (Adam Smith). Regel 6: Staat stellt Märkte bereit, schützt und kontrolliert sie; Eingriffe haben Nebenwirkungen.',
    exam='Regeln an Beispielen erkennen (Schwarzfahren, Kartell, Mindestlohn, unsichtbare Hand).',
    fehler=['Die unsichtbare Hand als staatliche Steuerung verstehen.', 'Glauben, Märkte bräuchten gar keinen Staat.'],
    src='Folien 73–76, 109–112')

# ---------------------------------------------------------------- 4 Schöpferische Zerstörung, Risiko, Arbitrage
def welle():
    import math
    s = achsen(20, 160, 350, 14, 'Zeit', '')
    pts = [(24 + i * 2, 100 - 46 * math.sin((i * 2) / 64 * 2 * math.pi)) for i in range(0, 162)]
    s += linie(pts, 'var(--primary)', 2.5)
    namen = ['Dampf,\nBaumwolle', 'Eisenbahn,\nStahl', 'Elektro,\nChemie', 'Auto,\nPetro', 'Informa-\ntionstechnik']
    for i, n in enumerate(namen):
        x = 24 + i * 64 + 16
        s += tpg(T(x + 4, 196, n, 12, 700), f'{i + 1}. Kondratieff-Zyklus (ab ca. {1800 + i * 50 if i < 4 else 1990}): getragen von {n.replace(chr(10), " ").replace("- ", "")}.')
    s += T(40, 36, 'P', 13, 800, 'middle', 'var(--c2)') + T(72, 92, 'R', 13, 800, 'middle', 'var(--c3)') + T(56, 150, 'D', 13, 800, 'middle', 'var(--neg)') + T(10, 96, 'W', 13, 800, 'middle', 'var(--c1)')
    return svg(360, 220, s, 'Lange Wellen der Konjunktur (Kondratieff)', maxw=420)

t_zerst = thema('innovation', 'Schöpferische Zerstörung, Risiko und Arbitrage',
    kern='Märkte schaffen „schöpferische Zerstörung“ (Schumpeter): Neues verdrängt Altes. Fortschritt gibt es nur, wenn jemand Unsicherheit oder Risiko übernimmt. Unternehmen nutzen Lücken, z. B. durch räumliche oder zeitliche Arbitrage.',
    kurz=p('Das Smartphone hat Wecker, Kamera und Stadtplan verdrängt. Ganze Branchen sind verschwunden, neue entstanden. Joseph Schumpeter nannte das <b>schöpferische Zerstörung</b>: Neues entsteht, indem Altes zerstört wird.')
        + p('Damit Neues entsteht, muss jemand ein <b>Risiko</b> eingehen. Wer eine Lücke im Markt erkennt, billig einkauft und teurer verkauft, betreibt <b>Arbitrage</b>.'),
    fig=fw('Lange Wellen der Wirtschaft: Jede wird von neuen Technologien getragen. Tippe auf die Beschriftungen.') + bild(welle()),
    figcap='nach Folie „Kondratieff-Zyklen“ (P = Prosperität, R = Rezession, D = Depression, W = Wachstum/Erholung)',
    article=h3('Regel 7: Märkte schaffen „schöpferische Zerstörung“')
        + p('Schumpeter beschreibt vier Wege, wie Neues entsteht:')
        + liste(['Herstellung eines neuen oder qualitativ veränderten Produkts', 'Einführung einer neuen Produktionsmethode', 'Erschließung eines neuen Absatzmarkts', 'Erschließung eines neuen Beschaffungsmarkts'])
        + p('Die Wirtschaft ist laut Schumpeter der „Prozess der schöpferischen Zerstörung“. Die <b>Aufgabe des Staates</b> ist, beim Neuen möglichst gut dabei zu sein und es zuzulassen, nicht den alten Markt künstlich zu verlängern.')
        + p('Die <b>Kondratieff-Zyklen</b> zeigen lange Wellen von etwa 50 Jahren, jede getragen von Basisinnovationen: Dampfmaschine und Baumwolle, Eisenbahn und Stahl, Elektrotechnik und Chemie, Automobil und Petrochemie, Informationstechnik. Jede Welle durchläuft Prosperität, Rezession, Depression und Erholung.')
        + weiter('Neues entsteht nicht von selbst. Jemand muss es wagen.')
        + h3('Regel 8: Ohne Unsicherheit oder Risiko kein Fortschritt')
        + gegen(('Risiko', 'Man kennt die möglichen Ergebnisse <b>und ihre Wahrscheinlichkeiten</b> (Würfel, Versicherung).'), ('Unsicherheit', 'Man kennt die Wahrscheinlichkeiten <b>nicht</b> (neues Produkt, das es noch nie gab).'))
        + p('Wer Möglichkeiten und Lücken erkennt und das Risiko trägt, kann Gewinn machen. Lücken zu füllen ist Aufgabe der Unternehmen, nicht des Staates.')
        + weiter('Eine besondere Art, Lücken zu nutzen, ist die Arbitrage.')
        + h3('Arbitrage')
        + p('Ausgangspunkt sind <b>unvollkommene Märkte</b>: Preise und Leistungen sind nicht überall gleich. Ein Unternehmen erkennt die Preislücke, kauft billig ein und verkauft teurer.')
        + cards([('räumlich bedingte Arbitrage', 'Preisunterschiede zwischen Orten nutzen, z. B. der Einzelhandel, der Ware vom Großhändler in die Stadt bringt'), ('zeitlich bedingte Arbitrage', 'Preisunterschiede zwischen Zeitpunkten nutzen, z. B. an Börsen oder Lagerhaltung von Saisonware')])
        + wahr('w-inno', [('Bei Risiko sind die Wahrscheinlichkeiten bekannt, bei Unsicherheit nicht.', True, 'Das ist der Unterschied.'),
                          ('Schöpferische Zerstörung heißt, dass der Staat alte Branchen schützen soll.', False, 'Neues verdrängt Altes; der Staat soll das Neue zulassen.'),
                          ('Wer Ware billig einkauft und an einem anderen Ort teurer verkauft, betreibt räumliche Arbitrage.', True, 'Preislücke zwischen Orten.')]),
    merk='Regel 7: schöpferische Zerstörung (Schumpeter): neues Produkt, neue Methode, neuer Absatzmarkt, neuer Beschaffungsmarkt. Regel 8: Fortschritt braucht Risikoübernahme. Risiko = Wahrscheinlichkeiten bekannt, Unsicherheit = unbekannt. Arbitrage räumlich/zeitlich.',
    exam='Risiko und Unsicherheit unterscheiden; Schumpeters vier Arten von Neuerungen; Arbitrage erkennen.',
    fehler=['Risiko und Unsicherheit vertauschen.'],
    src='Folien 77–81, 113–117')

# ---------------------------------------------------------------- 5 Wirtschaftsordnung
fig_ordnung = svg(360, 232,
    T(92, 18, 'Freie Marktwirtschaft', 13, 800) + T(268, 18, 'Planwirtschaft', 13, 800)
    + box(4, 30, 176, 40, 'Privateigentum', size=13, tip='Unternehmen gehören Privatleuten.') + box(184, 30, 172, 40, 'Volkseigentum', size=13, tip='Unternehmen gehören dem Staat bzw. dem Volk.')
    + box(4, 76, 176, 40, 'Angebot und Nachfrage', size=13, tip='Preise bilden sich am Markt.') + box(184, 76, 172, 40, 'Preis staatlich fest', size=13, tip='Der Staat legt Preise fest.')
    + box(4, 122, 176, 40, 'Konsum frei', size=13, tip='Völlige Konsum-, Berufs- und Vertragsfreiheit.') + box(184, 122, 172, 40, 'Konsum gelenkt', size=13, tip='Der Staat plant Produktion und Bedarf, regelt Beruf und Arbeitsplatz.')
    + box(4, 168, 176, 40, 'Individuum im Fokus', size=13, tip='Keine soziale Absicherung: Jeder ist selbst verantwortlich.') + box(184, 168, 172, 40, 'Staat im Mittelpunkt', size=13, tip='Völlige soziale Absicherung durch den Staat.')
    + T(180, 226, 'dazwischen: soziale Marktwirtschaft', 13, 800, 'middle', 'var(--primary)'),
    'Freie Marktwirtschaft und Planwirtschaft', maxw=420)

t_ordnung = thema('wirtschaftsordnung', 'Marktwirtschaft, Planwirtschaft und soziale Marktwirtschaft',
    kern='Freie Marktwirtschaft und Planwirtschaft sind Gegenpole bei Eigentum, Preisfindung, Freiheit und sozialer Sicherung. Die soziale Marktwirtschaft verbindet freien Markt mit sozialem Ausgleich.',
    kurz=p('In der freien Marktwirtschaft gehört Mias Fahrradladen Mia, sie setzt die Preise selbst, und die Kunden kaufen, was sie wollen. In der Planwirtschaft gehört der Laden dem Staat, der Staat legt fest, wie viele Räder es gibt und was sie kosten.')
        + p('Deutschland liegt dazwischen: In der <b>sozialen Marktwirtschaft</b> gibt es freien Wettbewerb, aber der Staat sorgt für Wettbewerbsregeln und soziale Absicherung.'),
    fig=fw('Die beiden Gegenpole. Tippe auf die Kästen.') + bild(fig_ordnung),
    figcap='nach Folie „Freie Marktwirtschaft – Planwirtschaft“',
    article=h3('Zwei Gegenpole')
        + tabelle(['Merkmal', 'Freie Marktwirtschaft', 'Planwirtschaft'], [
            ['Eigentum', 'Unternehmen in Privateigentum', 'Unternehmen in Staats- und Volkseigentum'], ['Preisfindung', 'Angebot und Nachfrage', 'staatlich festgesetzt'],
            ['Bedarfsdeckung', 'freier Wettbewerb', 'Staat plant Produktion und Bedarf'], ['Berufsfreiheit', 'Beruf und Arbeitsplatz frei wählbar', 'Staat regelt Wahl des Berufs und des Arbeitsplatzes'],
            ['Konsumfreiheit', 'völlige Konsumfreiheit', 'gelenkter Konsum'], ['Vertragsfreiheit', 'völlige Vertragsfreiheit', 'nur mit staatlicher Genehmigung'],
            ['Soziale Sicherung', 'keine Abdeckung', 'völlige Abdeckung'], ['Fokus', 'Individuum steht im Mittelpunkt', 'Staat steht im Mittelpunkt']])
        + weiter('Die Bundesrepublik hat nach dem Zweiten Weltkrieg einen Mittelweg gewählt.')
        + h3('Grundprinzipien der sozialen Marktwirtschaft')
        + p('Die soziale Marktwirtschaft (geprägt von Ludwig Erhard) verbindet den freien Markt mit sozialem Ausgleich. Der Staat betreibt dafür:')
        + liste(['Wettbewerbspolitik', 'Einkommens- und Vermögenspolitik', 'Struktur- und Wachstumspolitik', 'Konjunkturpolitik', 'Sozialpolitik'])
        + weiter('In der Vorlesung wurde dazu eine Grundsatzfrage diskutiert: Brauchen wir Wachstum?')
        + h3('Wachstum oder „Degrowth“?')
        + p('Die Vorlesung stellt zwei Sichtweisen gegenüber. <b>Degrowth</b> (Verzicht auf Wachstum): Ohne Wachstum gibt es keine Konjunktur, andere Länder überholen uns, und die Schulden werden im Verhältnis immer höher. <b>Growth</b> (Wachstum): Wirtschaftswachstum erleichtert die Schuldenlast, weil die Wirtschaft schneller wächst als die Schulden.')
        + p('Dazu fünf zugespitzte Sätze aus der Vorlesung: Man kann Arme nicht per Gesetz reich machen, indem man Reiche per Gesetz arm macht. Was einer bekommt, ohne dafür zu arbeiten, hat ein anderer erarbeitet. Die Regierung kann nur geben, was sie vorher jemandem genommen hat. Wohlstand lässt sich nicht durch Teilung mehren. Wenn die einen nicht arbeiten müssen und die anderen merken, dass sich ihre Arbeit nicht lohnt, hören beide auf.')
        + wahr('w-ord', [('In der Planwirtschaft setzt der Staat die Preise fest.', True, 'Keine Preisbildung am Markt.'),
                         ('Die freie Marktwirtschaft bietet völlige soziale Absicherung.', False, 'Keine Abdeckung; völlige Abdeckung bietet die Planwirtschaft.'),
                         ('Konjunkturpolitik gehört zu den Grundprinzipien der sozialen Marktwirtschaft.', True, 'Neben Wettbewerbs-, Einkommens-, Struktur- und Sozialpolitik.')]),
    merk='Freie Marktwirtschaft: Privateigentum, Preise durch Angebot und Nachfrage, alle Freiheiten, keine soziale Sicherung. Planwirtschaft: Volkseigentum, staatliche Preise, gelenkt, volle Absicherung. Soziale Marktwirtschaft: Wettbewerbs-, Einkommens-, Struktur-, Konjunktur-, Sozialpolitik.',
    exam='Merkmale den Wirtschaftsordnungen zuordnen; Grundprinzipien der sozialen Marktwirtschaft.',
    fehler=['Soziale Marktwirtschaft mit Planwirtschaft verwechseln.'],
    src='Folien 82–89, 118–127')

KAPITEL = kapitel('k4', 'Wirtschaftliche Prinzipien',
    'Acht Prinzipien und Regeln erklären, wie Menschen und Märkte funktionieren: von den Opportunitätskosten über den Grenznutzen bis zur schöpferischen Zerstörung. Durchgehendes Beispiel: Robinson Crusoe und die Mensa.',
    ['Opportunitätskosten', 'Grenznutzen', 'Märkte', 'Innovation', 'Ordnung'],
    [t_opp, t_grenz, t_markt, t_zerst, t_ordnung])

from mehr1 import ergaenze
ergaenze(KAPITEL)
