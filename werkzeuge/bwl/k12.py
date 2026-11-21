import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *

# Durchgehendes Beispiel: Lea und Tom gründen den Saftladen „Pressbar“ und wählen eine Rechtsform.


def steckbrief(name, zeilen):
    """Steckbrief einer Rechtsform wie in der Vorlesungstabelle (Leitung, Kontrolle, Haftung …)"""
    s = T(180, 18, name, 14, 800)
    for i, (k, v, tip) in enumerate(zeilen):
        y = 30 + i * 34
        s += rechteck(4, y, 112, 30, 'var(--pale)', 'var(--line)', 6) + T(60, y + 19, k, 12, 800)
        s += tpg(rechteck(120, y, 236, 30, 'var(--primary)' if k == 'Haftung' else 'var(--card)', 'var(--primary)' if k == 'Haftung' else 'var(--line)', 6)
                 + T(238, y + 19, v, 12, 700, 'middle', 'var(--on-primary)' if k == 'Haftung' else 'var(--ink)'), tip)
    return svg(360, 34 + len(zeilen) * 34, s, 'Steckbrief ' + name, maxw=420)


# ---------------------------------------------------------------- 1 Kriterien und Überblick
fig_rf = svg(360, 306,
    box(110, 6, 140, 40, 'Rechtsformen', size=13, art='hl') + pfeil(150, 48, 90, 66) + pfeil(210, 48, 270, 66)
    + box(4, 68, 172, 40, 'Personengesellschaften', size=12, tip='Gesellschafter haften (mindestens einer) mit dem Privatvermögen. Keine eigene Rechtspersönlichkeit.')
    + box(184, 68, 172, 40, 'Kapitalgesellschaften', size=12, tip='Juristische Personen mit eigener Rechtspersönlichkeit: Die Gesellschaft haftet, nicht der Gesellschafter.')
    + box(4, 116, 172, 130, '· Einzelunternehmen (e.K.)\n· GbR\n· OHG\n· KG', size=12, art='weak')
    + box(184, 116, 172, 130, '· AG\n· SE (Europäische AG)\n· GmbH', size=12, art='weak')
    + box(4, 254, 352, 46, 'außerdem: Genossenschaft (eG) ·\nVersicherungsverein auf Gegenseitigkeit', size=12, art='pale'),
    'Überblick über die Rechtsformen', maxw=420)

t_krit = thema('rechtsform-kriterien', 'Wahl der Rechtsform: Kriterien und Überblick',
    kern='Die Rechtsform regelt das Innenverhältnis (zwischen den Gesellschaftern) und das Außenverhältnis (zu anderen Wirtschaftsteilnehmern). Kriterien: Leitung, Kontrolle, Haftung, Mindesteinlage, Gewinn- und Verlustbeteiligung, Finanzierung, Publizität, Mitbestimmung, Steuern.',
    kurz=p('Lea und Tom wollen einen Saftladen gründen. Voraussetzungen: eine <b>Geschäftsidee</b>, die <b>Kompetenz</b>, sie umzusetzen, und <b>Eigenkapital</b>. Dann die große Frage: Welche <b>Rechtsform</b>?')
        + p('Die wichtigste Frage ist die <b>Haftung</b>: Haften sie als Privatpersonen mit allem, was sie haben, oder haftet nur die Firma mit dem, was ihr gehört? Dazu kommen: Wer leitet? Wer kontrolliert? Wie viel Geld muss man einlegen? Muss man Zahlen veröffentlichen?'),
    fig=fw('Die Rechtsformen im Überblick. Tippe auf die Kästen.') + bild(fig_rf),
    figcap='nach Folie „Wahl der Rechtsform im Gesellschaftsrecht“',
    article=h3('Was die Rechtsform regelt')
        + p('Die Wahl der Rechtsform regelt die Rechtsbeziehung zwischen den Gesellschaftern (<b>Innenverhältnis</b>) und die Rechtsbeziehungen zwischen dem Unternehmen und anderen Wirtschaftsteilnehmern (<b>Außenverhältnis</b>).')
        + tabelle(['Kriterium', 'Frage'], [
            ['Leitungsbefugnis', 'Wer entscheidet? Habe ich die Leitung allein?'], ['Kontrollbefugnis', 'Wer überwacht die Leitung?'],
            ['Haftung', 'Haftet man als Privatperson mit allem, was man hat, oder die Organisation mit allem, was ihr zur Verfügung steht?'],
            ['Mindesteinlage', 'Wie viel Kapital muss man einbringen? Wie viel kostet die Anmeldung?'], ['Gewinn- und Verlustbeteiligung', 'Wer bekommt den Gewinn, wer trägt Verluste?'],
            ['Finanzierungsmöglichkeiten', 'Wie leicht bekommt man Geld? Je mehr Haftung, desto kreditwürdiger'], ['Publizität', 'Muss man Zahlen veröffentlichen?'],
            ['Mitbestimmung', 'Haben Stakeholder (z. B. Arbeitnehmer im Aufsichtsrat) Mitspracherecht?'], ['Steuerbelastung', 'Wie wird besteuert?']])
        + p('Ein Zusammenhang, den man verstehen muss: Wer <b>persönlich mit allem haftet</b> (Einzelkaufmann), bekommt eher einen Kredit als jemand, dessen Firma nur mit ihrem Stammkapital haftet (GmbH). <b>Alle Rechtsformen haben Vor- und Nachteile.</b>')
        + klausur_hinweis('In der Klausur wird ein Sachverhalt mit Kriterien beschrieben, und du musst die Rechtsform erkennen. Lerne deshalb für jede Rechtsform den Steckbrief: Leitung, Kontrolle, Haftung, Mindesteinlage, Publizität.')
        + zusatz('Die Standortwahl (Standortfaktoren, IWD-Modell, Nutzwertanalyse, Optimierungsmodell zentraler Auslieferungslager) ist in den Folien durchgestrichen.')
        + wahr('w-krit', [('Die Rechtsform regelt auch das Verhältnis der Gesellschafter untereinander.', True, 'Innenverhältnis.'),
                          ('Eine GmbH ist eine Personengesellschaft.', False, 'Kapitalgesellschaft.'),
                          ('Wer persönlich unbeschränkt haftet, bekommt eher Kredit.', True, 'Mehr Haftungsmasse für die Bank.')]),
    merk='Rechtsform regelt Innen- und Außenverhältnis. Kriterien: Leitung, Kontrolle, Haftung, Mindesteinlage, GuV, Finanzierung, Publizität, Mitbestimmung, Steuern. Personengesellschaften: e.K., GbR, OHG, KG; Kapitalgesellschaften: AG, SE, GmbH.',
    exam='Kriterien der Rechtsformwahl nennen; Rechtsformen den Gruppen zuordnen.',
    fehler=['Die KG für eine Kapitalgesellschaft halten (das K steht für Kommandit).'],
    src='Folien 305, 319–322')

# ---------------------------------------------------------------- 2 Einzelunternehmen, GbR, OHG
t_pers = thema('personengesellschaften', 'Einzelunternehmen, GbR und OHG', star=True,
    kern='Beim Einzelunternehmen (e.K.) entscheidet, kontrolliert und haftet die Eigentümerin allein und unbeschränkt. In GbR und OHG haften alle Gesellschafter unbeschränkt mit ihrem gesamten Vermögen; die OHG ist die ausgefeiltere „Schwester“ der GbR für größere Handelsgeschäfte, mit fünf Jahren Nachhaftung nach Austritt.',
    kurz=p('Lea fängt allein an, ohne Vertrag, ohne Mindesteinlage: Sie ist <b>Einzelunternehmerin</b>. Sie leitet, kontrolliert, bekommt den Gewinn und <b>haftet bis auf den letzten Cent</b> mit allem, was sie hat.')
        + p('Steigt Tom ein, ist es automatisch eine <b>GbR</b> (Gesellschaft bürgerlichen Rechts): Sobald mehrere Personen etwas zusammen machen, auch eine Band oder ein gemeinsamer Kauf. Wird das Geschäft groß, nehmen sie die <b>OHG</b>, mit ausgefeilteren Regeln.'),
    fig=fw('Steckbriefe wie in der Vorlesungstabelle. Schalte um.')
        + tafeln('tf-pers', ['e.K.', 'GbR', 'OHG'], [
            steckbrief('Einzelunternehmen (e.K.)', [('Leitung', 'Eigentümerin', 'Die einfachste Form: Man fängt einfach an.'), ('Kontrolle', 'Eigentümerin', 'Niemand kontrolliert sie.'), ('Haftung', 'Eigentümerin: alles', 'Bis auf den letzten Cent, mit dem gesamten Privatvermögen.'),
                                                    ('Mindesteinl.', 'keine', 'Keine Mindesteinlage nötig.'), ('Finanzierung', 'über Eigentümerin', 'Hängt an der Person: Hat sie zwei Häuser, bekommt sie eher Kredit.'), ('Publizität', 'nicht erforderlich', 'Keine Veröffentlichungspflicht.'), ('Mitbestimm.', 'kein Aufsichtsrat', 'Keine Mitbestimmung (Beispiel: Schlecker).')]),
            steckbrief('GbR', [('Leitung', 'alle Gesellschafter', 'Mindestens 2 Gesellschafter; intern frei organisierbar. Ohne Vertrag leiten alle.'), ('Kontrolle', 'alle', 'Die Gesellschafter kontrollieren sich gegenseitig.'), ('Haftung', 'alle mit allem', 'Unbeschränkt: Gläubiger holen sich das Geld, wo es ist, z. B. beim Gesellschafter mit 1 Mio. Vermögen. Ausgleich wird intern geklärt.'),
                               ('Mindesteinl.', 'keine', 'Kein Mindestkapital.'), ('GuV', 'nach Vertrag', 'z. B. 75 % / 25 %; sonst gleich.'), ('Publizität', 'nicht erforderlich', ''), ('Mitbestimm.', 'kein Aufsichtsrat', '')]),
            steckbrief('OHG', [('Leitung', 'Gesellschafter', 'Wie bei der GbR, aber für einen großen Geschäftsbetrieb mit mehr Regeln.'), ('Kontrolle', 'Gesellschafter', ''), ('Haftung', 'alle mit allem', 'Unbeschränkt, und noch 5 Jahre nach dem Austritt (sonst würden alle austreten, sobald es kippt).'),
                               ('Mindesteinl.', 'keine', ''), ('GuV', 'nach Gesetz/Vertrag', ''), ('Publizität', 'gering', ''), ('Mitbestimm.', 'kein Aufsichtsrat', '')])]),
    figcap='nach Folien „Wahl der Rechtsform im Gesellschaftsrecht“ (e.K., GbR, OHG)',
    article=h3('Einzelunternehmen (e.K.)')
        + p('Die einfachste Form von allen: Man fängt einfach an. Wer nichts weiter regelt, ist Einzelunternehmer. Leitung, Kontrolle, Gewinn und Haftung liegen bei <b>einer</b> Person; die Haftung ist <b>unbeschränkt</b> („bis auf den letzten Cent“). Eine Mindesteinlage braucht man nicht, veröffentlichen muss man nichts. Finanzierung: hängt an der Person; wer Vermögen hat (etwa zwei Häuser), bekommt eher Kredit.')
        + weiter('Sobald mehr als eine Person etwas zusammen macht, entsteht eine Gesellschaft.')
        + h3('Gesellschaft bürgerlichen Rechts (GbR)')
        + p('Mindestens zwei Gesellschafter, kein Vertrag nötig: „Man fängt an.“ Beispiele: eine Band, ein gemeinsamer Kauf, Lea und Tom ohne weitere Regelung. Die Gesellschafter organisieren sich intern, wie sie wollen; ohne Vertrag leiten alle gemeinsam.')
        + bsp('Haftung in der GbR', 'Lea hat kein Vermögen, Tom hat 1 Mio. €. Die GbR hat 200.000 € Schulden.',
              [('Alle haften unbeschränkt mit ihrem gesamten Vermögen.', ''), ('Die Gläubiger holen sich das Geld dort, wo es ist: bei Tom.', 'Tom zahlt 200.000 €'), ('Den Ausgleich (z. B. Gewinnverteilung 75 % / 25 %) klären Lea und Tom intern.', 'Innenverhältnis')])
        + h3('Offene Handelsgesellschaft (OHG)')
        + p('Die „Schwester der GbR“: gleiche Grundidee, aber für einen großen Geschäftsbetrieb mit ausgefeilterem Regelwerk. Wichtig: Die Gesellschafter haften auch noch <b>fünf Jahre nach dem Austritt</b>. Sonst würden alle austreten, sobald sie merken, dass das Geschäft kippt.')
        + wahr('w-pers', [('Ein Einzelunternehmer haftet nur mit dem Geschäftsvermögen.', False, 'Mit seinem gesamten Vermögen.'),
                          ('Eine GbR entsteht auch ohne schriftlichen Vertrag.', True, 'Sobald mehrere etwas zusammen machen.'),
                          ('OHG-Gesellschafter haften noch fünf Jahre nach ihrem Austritt.', True, 'Gesetzliche Nachhaftung.')]),
    merk='e.K.: eine Person leitet, kontrolliert, haftet unbeschränkt, keine Mindesteinlage, keine Publizität. GbR: ≥ 2 Gesellschafter, kein Vertrag nötig, alle haften unbeschränkt. OHG: wie GbR für große Handelsgeschäfte, Nachhaftung 5 Jahre.',
    exam='Rechtsform aus Merkmalen erkennen (Haftung, Mindesteinlage, Anzahl Gesellschafter).',
    fehler=['Bei der GbR beschränkte Haftung annehmen.'],
    src='Folien 323–325')

# ---------------------------------------------------------------- 3 KG
t_kg = thema('kg', 'Kommanditgesellschaft (KG)', star=True,
    kern='Die KG hat zwei Arten von Gesellschaftern: Komplementäre leiten, kontrollieren und haften unbeschränkt mit ihrem gesamten Vermögen. Kommanditisten geben Geld, kontrollieren (wie vereinbart), leiten nicht und haften nur bis zur Höhe ihrer Einlage.',
    kurz=p('Lea will den Laden führen, braucht aber Geld. Ihre Tante gibt 50.000 €, will aber nicht mitarbeiten und nicht mehr riskieren als diese 50.000 €. Dafür gibt es die <b>KG</b>: Lea wird <b>Komplementärin</b> (leitet, haftet mit allem), die Tante <b>Kommanditistin</b> (gibt Geld, haftet nur mit der Einlage).')
        + p('Man denke an „Die Höhle der Löwen“: Die Investoren geben Geld, aber die Gründer führen das Geschäft.'),
    fig=fw('Die klare Zweiteilung der KG. Tippe auf die Felder.')
        + bild(svg(360, 220,
            T(180, 18, 'Kommanditgesellschaft', 14, 800)
            + box(4, 30, 172, 70, 'Komplementär\n(Leitung)', size=13, art='hl', tip='Leitet die Gesellschaft und haftet unbeschränkt mit seinem gesamten Vermögen.')
            + box(184, 30, 172, 70, 'Kommanditist\n(Geldgeber)', size=13, tip='Gibt Kapital, hat Kontrollrechte (wie vereinbart), aber kein Leitungsrecht. Haftet nur mit seiner Einlage.')
            + T(90, 122, 'Haftung: unbeschränkt', 12, 700) + T(270, 122, 'Haftung: nur Einlage', 12, 700)
            + T(90, 144, 'Kontrollrecht: ja', 12, 600, 'middle', 'var(--muted)') + T(270, 144, 'Kontrollrecht: ja', 12, 600, 'middle', 'var(--muted)')
            + T(90, 166, 'Leitungsrecht: ja', 12, 600, 'middle', 'var(--muted)') + T(270, 166, 'Leitungsrecht: nein', 12, 600, 'middle', 'var(--muted)')
            + box(4, 180, 352, 34, 'GuV: nach Gesellschaftsvertrag', size=12, art='pale'),
            'Komplementär und Kommanditist', maxw=420)),
    figcap='nach Folie „Kommanditgesellschaft“ (Tabelle Komplementär – Kommanditist)',
    article=h3('Komplementär und Kommanditist')
        + tabelle(['', 'Komplementär', 'Kommanditist'], [['Haftung', 'unbeschränkt mit gesamtem Vermögen', 'beschränkt auf Kapitaleinlage'], ['Kontrollrecht', 'ja', 'ja (so wie vereinbart)'], ['Leitungsrecht', 'ja', 'nein'], ['GuV', 'nach Gesellschaftervertrag', 'nach Gesellschaftervertrag']])
        + p('Mindesteinlage: keine gesetzliche, hängt vom Vertrag ab. Finanzierung: unbegrenzt über den Komplementär, zusätzlich Kapital der Kommanditisten. Publizität: etwas mehr, es gibt ein öffentliches Interesse. Mitbestimmung: kein Aufsichtsrat. Ein bekanntes Beispiel ist Storck (Süßwaren).')
        + zusatz('Die Stille Gesellschaft (Kapitalgeber beteiligt sich unsichtbar am Handelsgewerbe, wenig Kontrolle) ist in den Folien durchgestrichen.')
        + wahr('w-kg', [('Der Kommanditist leitet die KG.', False, 'Leitung hat der Komplementär.'),
                        ('Der Kommanditist haftet nur bis zur Höhe seiner Einlage.', True, 'Beschränkte Haftung.'),
                        ('Eine KG braucht mindestens einen Komplementär.', True, 'Jemand muss unbeschränkt haften.')]),
    merk='KG: Komplementär = Leitung + unbeschränkte Haftung; Kommanditist = Geldgeber, Kontrolle, keine Leitung, Haftung nur mit Einlage. GuV nach Vertrag.',
    exam='Rechte und Haftung von Komplementär und Kommanditist zuordnen.',
    fehler=['Komplementär und Kommanditist vertauschen. Merkhilfe: Der Kommanditist „kommandiert“ gerade nicht.'],
    src='Folien 326–328')

# ---------------------------------------------------------------- 4 AG
fig_ag = svg(360, 266,
    box(110, 6, 140, 56, 'Hauptversammlung\n(Aktionäre)', size=12, tip='Versammlung der Aktionäre. Eine Stimme pro Aktie. Wählt den Aufsichtsrat, entscheidet über die Verwendung des Bilanzgewinns und die Auflösung.')
    + pfeil(180, 64, 180, 100) + T(186, 86, 'wählt (max. 4 J.)', 12, 600, 'start', 'var(--muted)')
    + box(110, 102, 140, 56, 'Aufsichtsrat\n(Kontrolle)', size=12, tip='Überwacht den Vorstand, bestellt und beruft ihn ab (für maximal 5 Jahre, Wiederwahl möglich). Mitbestimmung: paritätisch mit Arbeitnehmern ab einer bestimmten Größe.')
    + pfeil(180, 160, 180, 196) + T(186, 182, 'bestellt (max. 5 J.)', 12, 600, 'start', 'var(--muted)')
    + box(110, 198, 140, 56, 'Vorstand\n(Leitung)', size=12, art='hl', tip='Leitet die Gesellschaft in eigener Verantwortung, ist nicht an Weisungen von Aufsichtsrat oder Hauptversammlung gebunden, erstellt den Jahresabschluss, weitgehende Berichtspflichten.')
    + T(54, 206, 'Haftung:', 12, 800) + T(54, 222, 'Gesellschaft mit', 12, 600) + T(54, 238, 'ihrem Vermögen', 12, 600)
    + T(306, 214, 'Aktionär:', 12, 800) + T(306, 230, 'nur Einlage', 12, 600),
    'Organe der Aktiengesellschaft', maxw=420)

t_ag = thema('ag', 'Kapitalgesellschaften und Aktiengesellschaft (AG)', star=True,
    kern='Kapitalgesellschaften sind juristische Personen: Die Gesellschaft haftet unbeschränkt mit ihrem Vermögen, die Gesellschafter nur mit ihrer Einlage. Die AG hat mindestens 50.000 € Grundkapital und drei Organe: Vorstand (Leitung), Aufsichtsrat (Kontrolle), Hauptversammlung (Aktionäre). Volle Publizität.',
    kurz=p('Der Saftladen wird eine Kette mit 40 Filialen. Lea und Tom wollen nicht mehr persönlich haften und brauchen viel Geld. Sie gründen eine <b>Aktiengesellschaft</b>: Viele Anleger kaufen Aktien und werden Miteigentümer.')
        + p('Die AG ist eine eigene Person vor dem Gesetz (<b>juristische Person</b>). Für ihre Schulden haftet die <b>Gesellschaft mit ihrem Vermögen</b>. Ein Aktionär kann höchstens das verlieren, was er für seine Aktien bezahlt hat.'),
    fig=fw('Die drei Organe der AG. Tippe auf die Kästen.') + bild(fig_ag),
    figcap='nach Folie „Aktiengesellschaft“ (Vorstand, Aufsichtsrat, Hauptversammlung)',
    article=h3('Merkmale aller Kapitalgesellschaften')
        + liste(['eigene Rechtspersönlichkeit (juristische Person)', 'unbeschränkte Haftung der Gesellschaft', 'beschränkte Haftung der Gesellschafter („man muss halt vorher was reingeben“)', 'Leitung durch bestellte Organe', 'unabhängig vom Bestand der Mitglieder', 'Mitspracherecht abhängig vom Kapitalanteil'])
        + weiter('Die bekannteste Kapitalgesellschaft ist die AG.')
        + h3('Aktiengesellschaft')
        + p('Eine Kapitalgesellschaft, an der sich Eigenkapitalgeber durch den Erwerb von Aktien beteiligen. Die Satzung lässt nur wenig Spielraum, das Aktiengesetz regelt fast alles. <b>Mindestgrundkapital: 50.000 €.</b> Die Rechte aus der Aktie definieren die Mitgliedschaft. Eine AG muss nicht an der Börse sein.')
        + tabelle(['', 'AG'], [['Leitung', 'Vorstand'], ['Kontrolle', 'Aufsichtsrat'], ['Haftung', 'Gesellschaft mit ihrem Vermögen; Aktionär nur mit dem, was er investiert hat'], ['Mindesteinlage', '50.000 € Grundkapital'],
                               ['GuV', 'Aktionäre erhalten anteilig den Gewinn, den die Hauptversammlung als Dividende beschließt'], ['Finanzierung', 'über neue Aktien (Stamm-, Vorzugsaktien) und Fremdkapital'],
                               ['Publizität', 'volle Publizität (Bilanz …)'], ['Mitbestimmung', 'Aufsichtsrat paritätisch (ab bestimmter Größe)']])
        + bsp('Börsengang', 'Ein Malermeister bringt 25 % seiner Firma als AG an die Börse.',
              [('Vorteile: Geld kommt herein, Bekanntheit steigt.', ''), ('Nachteile: Publizitätspflichten, Mitsprache der Aktionäre.', '')])
        + bsp('Klausurfrage: Womit haftet eine AG im Insolvenzfall?', '',
              [('Die AG als juristische Person haftet mit ihrem gesamten Gesellschaftsvermögen.', ''), ('Die Aktionäre haften nicht persönlich; sie verlieren höchstens ihre Einlage (der Wert ihrer Aktien).', ''), ('Vorstand und Aufsichtsrat haften nicht mit ihrem Privatvermögen für die Schulden der AG.', 'mit dem Gesellschaftsvermögen')],
              'Achte bei den Antwortmöglichkeiten auf „keines der oben genannten“ und „a) bis c) sind richtig“: genau lesen.')
        + zusatz('Die Kommanditgesellschaft auf Aktien (KGaA: mindestens ein voll haftender Komplementär plus Kommanditaktionäre; Beispiel Merck) ist in den Folien durchgestrichen. Die SE ist die Europäische Gesellschaft (europäische AG).')
        + wahr('w-ag', [('Bei der AG haften die Aktionäre mit ihrem Privatvermögen.', False, 'Nur mit ihrer Einlage.'),
                        ('Der Aufsichtsrat überwacht den Vorstand.', True, 'Und bestellt ihn.'),
                        ('Das Mindestgrundkapital der AG beträgt 50.000 €.', True, 'Laut Aktiengesetz.'),
                        ('Eine AG muss an der Börse notiert sein.', False, 'Muss sie nicht.')]),
    merk='Kapitalgesellschaft = juristische Person; Gesellschaft haftet mit ihrem Vermögen, Gesellschafter nur mit Einlage. AG: Grundkapital ≥ 50.000 €; Vorstand (Leitung), Aufsichtsrat (Kontrolle, bestellt Vorstand ≤ 5 J.), Hauptversammlung (wählt AR ≤ 4 J., eine Stimme je Aktie, Gewinnverwendung); volle Publizität.',
    exam='Haftung der AG im Insolvenzfall; Organe und Mindestkapital; AG aus Merkmalen erkennen.',
    fehler=['Aktionäre persönlich haften lassen.', 'Vorstand und Aufsichtsrat in den Aufgaben vertauschen.'],
    src='Folien 329–334')

# ---------------------------------------------------------------- 5 GmbH
t_gmbh = thema('gmbh', 'Gesellschaft mit beschränkter Haftung (GmbH)', star=True,
    kern='Die GmbH ist eine Kapitalgesellschaft mit mindestens 25.000 € Stammkapital. Leitung: Geschäftsführer; Kontrolle: Gesellschafter(versammlung). Die GmbH haftet unbeschränkt mit ihrem Gesellschaftsvermögen, die Gesellschafter nur mit ihrer Einlage. Publizität ja, aber weniger als bei der AG.',
    kurz=p('Lea und Tom wollen nicht mit ihrem Privatvermögen haften, aber auch keine große AG. Sie gründen eine <b>GmbH</b> mit 25.000 € Stammkapital. Ein <b>Geschäftsführer</b> (quasi der Vorstand) leitet, die Gesellschafter kontrollieren.')
        + p('Geht die GmbH pleite, haftet <b>die GmbH mit allem, was ihr gehört</b>. Lea und Tom verlieren ihre Einlage, aber nicht ihre Wohnung. Deshalb bekommen GmbHs schwerer Kredit als Einzelkaufleute: Die Bank verlangt oft private Bürgschaften.'),
    fig=fw('Steckbrief der GmbH wie in der Vorlesungstabelle. Tippe auf die Haftung.')
        + bild(steckbrief('GmbH', [('Leitung', 'Geschäftsführer', 'Der Geschäftsführer ist quasi der Vorstand der GmbH.'), ('Kontrolle', 'Gesellschafter', 'Die Gesellschafterversammlung kontrolliert.'),
                                   ('Haftung', 'GmbH mit ihrem Vermögen', 'Die GmbH haftet uneingeschränkt mit allem, was in ihr steckt (mindestens 25.000 €). Die Gesellschafter nur mit ihrer Einlage.'),
                                   ('Mindesteinl.', '25.000 € Stammkapital', 'Mindeststammkapital 25.000 €.'), ('GuV', 'nach Anteil/Vertrag', 'Intern geregelt.'), ('Finanzierung', 'schwieriger', 'Schwieriger, weil niemand privat haftet.'),
                                   ('Publizität', 'ja, weniger als AG', 'Publizitätspflicht, aber nicht ganz so umfangreich wie bei der AG.'), ('Mitbestimm.', 'ab bestimmter Größe AR', 'Ab einer bestimmten Größe Aufsichtsrat.')])),
    figcap='nach Folie „Gesellschaft mit beschränkter Haftung“',
    article=h3('Steckbrief')
        + tabelle(['', 'GmbH', 'AG zum Vergleich'], [['Leitung', 'Geschäftsführer', 'Vorstand'], ['Kontrolle', 'Gesellschafterversammlung (ab Größe Aufsichtsrat)', 'Aufsichtsrat'], ['Haftung', 'GmbH mit Gesellschaftsvermögen; Gesellschafter bis zur Einlage', 'AG mit Gesellschaftsvermögen; Aktionär bis zur Einlage'], ['Mindestkapital', '25.000 €', '50.000 €'], ['Publizität', 'ja, aber weniger', 'volle Publizität']])
        + bsp('Insolvenz einer GmbH', 'Die Pressbar GmbH (Stammkapital 25.000 €, Gesellschafter Lea und Tom) kann ihre Lieferanten nicht mehr bezahlen.',
              [('Die GmbH ist zahlungsunfähig: Insolvenz.', ''), ('Gläubiger bekommen Geld aus dem Vermögen der GmbH (Kasse, Einrichtung, Forderungen).', 'Gesellschaftsvermögen'), ('Lea und Tom verlieren ihre Einlage, haften aber nicht privat (außer sie haben persönlich gebürgt).', 'nur Einlage')])
        + falle('„beschränkte Haftung“ falsch verstehen: Die GmbH selbst haftet <b>unbeschränkt</b> mit ihrem ganzen Vermögen. Beschränkt ist die Haftung der <b>Gesellschafter</b>.')
        + wahr('w-gmbh', [('Das Mindeststammkapital der GmbH beträgt 25.000 €.', True, 'Bei der AG 50.000 €.'),
                          ('In der GmbH haften die Gesellschafter mit ihrem Privatvermögen.', False, 'Nur mit ihrer Einlage.'),
                          ('Die GmbH wird von einem Geschäftsführer geleitet.', True, 'Quasi der Vorstand.')]),
    merk='GmbH: Stammkapital ≥ 25.000 €; Leitung Geschäftsführer, Kontrolle Gesellschafter; GmbH haftet mit Gesellschaftsvermögen, Gesellschafter nur mit Einlage; Publizität geringer als AG; Finanzierung schwieriger.',
    exam='GmbH aus Merkmalen erkennen; Insolvenzfall erklären.',
    fehler=['Glauben, die GmbH selbst hafte beschränkt.'],
    src='Folie 335')

# ---------------------------------------------------------------- 6 Rechtsform erkennen, Insolvenz (Zuordnen)
def haftungsbild():
    zeilen = [('e.K.', 'Inhaberin: alles', 'unbeschränkt'), ('GbR', 'alle Gesellschafter: alles', 'unbeschränkt'), ('OHG', 'alle: alles (+5 J.)', 'unbeschränkt'),
              ('KG', 'Komplementär: alles\nKommanditist: Einlage', 'gemischt'), ('GmbH', 'Gesellschaft: ihr Vermögen\nGesellschafter: Einlage', 'beschränkt'), ('AG', 'Gesellschaft: ihr Vermögen\nAktionär: Einlage', 'beschränkt')]
    s = T(60, 16, 'Rechtsform', 12, 800, 'middle', 'var(--muted)') + T(236, 16, 'Wer haftet womit?', 12, 800, 'middle', 'var(--muted)')
    for i, (n, w, art) in enumerate(zeilen):
        y = 26 + i * 44
        farbe = {'unbeschränkt': 'var(--neg)', 'gemischt': 'var(--c3)', 'beschränkt': 'var(--c2)'}[art]
        s += rechteck(4, y, 112, 38, farbe, farbe, 6) + T(60, y + 24, n, 13, 800, 'middle', 'var(--on-primary)')
        s += rechteck(120, y, 236, 38, 'var(--card)', 'var(--line)', 6) + T(238, y + 20 if '\n' in w else y + 24, w, 12, 700)
    return svg(360, 296, s, 'Haftung nach Rechtsform', maxw=420)

t_fall = thema('rechtsform-fall', 'Rechtsform erkennen und der Insolvenzfall', star=True,
    kern='Rechtsformen erkennt man an wenigen Merkmalen: Wer haftet womit, wie viel Mindestkapital, wer leitet. Personengesellschaften (e.K., GbR, OHG; Komplementär der KG) haften unbeschränkt privat, Kapitalgesellschaften (GmbH, AG) mit dem Gesellschaftsvermögen.',
    kurz=p('In der Klausur steht ein Fall: „Zwei Gesellschafter, kein Mindestkapital, beide haften mit ihrem gesamten Vermögen, kein Handelsgewerbe.“ Welche Rechtsform? Die GbR. Oder: „Ein Geschäftsführer leitet, Stammkapital 25.000 €.“ Die GmbH.')
        + p('Am schnellsten geht es über die <b>Haftung</b>: Rot heißt privat unbeschränkt, grün heißt nur die Gesellschaft mit ihrem Vermögen.'),
    fig=fw('Haftung auf einen Blick. Rot = unbeschränkt privat, Orange = gemischt, Grün = Gesellschaft haftet.') + bild(haftungsbild()),
    figcap='zusammengefasst aus den Rechtsform-Steckbriefen der Vorlesung',
    article=h3('Erkennungsmerkmale')
        + tabelle(['Merkmal im Fall', 'Rechtsform'], [
            ['eine Person, keine Mindesteinlage, haftet mit allem', 'Einzelunternehmen (e.K.)'], ['mehrere Personen, kein Vertrag nötig, alle haften mit allem', 'GbR'],
            ['wie GbR, großes Handelsgewerbe, Nachhaftung 5 Jahre', 'OHG'], ['ein Vollhafter leitet, Geldgeber haften nur mit Einlage', 'KG'],
            ['Geschäftsführer, 25.000 € Stammkapital, Haftung beschränkt', 'GmbH'], ['Vorstand, Aufsichtsrat, Hauptversammlung, 50.000 € Grundkapital, Aktien', 'AG']])
        + spiel('sp-rf', 'Welche Rechtsform ist gemeint?', ['e.K.', 'GbR', 'KG', 'GmbH', 'AG'],
                [('Drei Freundinnen kaufen gemeinsam einen Food-Truck, ohne Vertrag.', 1, 'Mehrere Personen ohne Vertrag: GbR.'),
                 ('Ein Gründer leitet, eine Investorin gibt 50.000 € und haftet nur damit.', 2, 'Komplementär und Kommanditistin.'),
                 ('Geschäftsführer, Gesellschafterversammlung, 25.000 € Stammkapital.', 3, 'GmbH.'),
                 ('Eine Frau eröffnet allein ein Nagelstudio und haftet mit allem.', 0, 'Einzelunternehmen.'),
                 ('Die Hauptversammlung wählt den Aufsichtsrat.', 4, 'AG.'),
                 ('Mindestkapital 50.000 €, Anteile frei handelbar.', 4, 'AG.')])
        + weiter('Was heißt das, wenn es schiefgeht?')
        + h3('Der Insolvenzfall')
        + p('Ein Unternehmen ist <b>insolvent</b>, wenn es fällige Rechnungen nicht mehr zahlen kann (siehe Liquidität). Dann zeigt sich, was die Haftung bedeutet:')
        + tabelle(['Rechtsform', 'Wer zahlt die Schulden?'], [
            ['e.K.', 'die Inhaberin mit Geschäfts- und Privatvermögen'], ['GbR, OHG', 'jeder Gesellschafter mit seinem gesamten Vermögen; Gläubiger wählen, bei wem sie holen'],
            ['KG', 'Komplementär mit allem; Kommanditist verliert seine Einlage'], ['GmbH, AG', 'die Gesellschaft mit ihrem Vermögen; Gesellschafter/Aktionäre verlieren ihre Einlage']])
        + klausur_hinweis('Fallfrage „Was passiert im Insolvenzfall?“ (meist mit GmbH): Die Gesellschaft haftet mit ihrem Vermögen, die Gesellschafter nur mit der Einlage. Und „Womit haftet eine AG?“: mit dem Gesellschaftsvermögen.')
        + wahr('w-fall', [('Bei der Insolvenz einer GmbH müssen die Gesellschafter mit ihrem Privatvermögen zahlen.', False, 'Nur mit der Einlage (außer bei privaten Bürgschaften).'),
                          ('Im Insolvenzfall einer OHG können Gläubiger auf das Privatvermögen der Gesellschafter zugreifen.', True, 'Unbeschränkte Haftung.')]),
    merk='Haftung entscheidet: e.K., GbR, OHG, Komplementär → privat unbeschränkt; Kommanditist, GmbH-Gesellschafter, Aktionär → nur Einlage; GmbH und AG haften mit Gesellschaftsvermögen. Insolvenz = fällige Rechnungen nicht zahlbar.',
    exam='Rechtsform anhand von Kriterien erkennen; Folgen einer Insolvenz für Gesellschafter.',
    fehler=['Bei der KG alle Gesellschafter gleich behandeln.'],
    src='Folien 319–336')

KAPITEL = kapitel('k12', 'Rechtsformen',
    'Welche Rechtsform passt, und wer haftet womit? Kriterien, Personen- und Kapitalgesellschaften, Erkennen im Fall und der Insolvenzfall. Durchgehendes Beispiel: Lea und Tom gründen den Saftladen „Pressbar“.',
    ['Kriterien', 'e.K., GbR, OHG', 'KG', 'AG', 'GmbH', 'Erkennen'],
    [t_krit, t_pers, t_kg, t_ag, t_gmbh, t_fall])

from mehr2 import ergaenze
ergaenze(KAPITEL)
