import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *

# Durchgehendes Beispiel in diesem Oberthema: der Fahrradladen „Radwerk“ von Mia in der Mannheimer Neckarstadt.

# ---------------------------------------------------------------- 1 Was ist BWL?
fig_bwl = svg(360, 250,
    T(180, 16, 'Betriebs · wirtschafts · lehre', 14, 800)
    + box(4, 34, 112, 92, 'Betrieb\nWO?', size=13, tip='Betrieb: eine planvoll organisierte Wirtschaftseinheit, in der Produktionsfaktoren kombiniert werden, um Güter oder Dienstleistungen herzustellen oder abzusetzen. Beispiel: Mias Fahrradladen.')
    + box(124, 34, 112, 92, 'Wirtschaften\nWIE?', size=13, art='hl', tip='Wirtschaften: langfristige Maximierung des Gewinns unter Beachtung von Nebenbedingungen, nach dem ökonomischen Prinzip.')
    + box(244, 34, 112, 92, 'Lehre\nWOZU?', size=13, tip='Lehre: betriebswirtschaftliche Erkenntnisse beschreiben, begreiflich machen und für den Einsatz nutzbar machen.')
    + pfeil(180, 132, 180, 156)
    + box(4, 160, 352, 80, 'Grundproblem:\nunendliche Bedürfnisse,\nknappe Mittel', size=13, art='pale', tip='Darum gibt es BWL überhaupt: Man will mehr, als man hat. Also muss man entscheiden, wofür man Geld, Zeit und Material einsetzt.'),
    'Der Begriff Betriebswirtschaftslehre in drei Teilen', maxw=420)

t_bwl = thema('bwl-def', 'Was ist Betriebswirtschaftslehre?',
    kern='BWL untersucht, wie Betriebe mit knappen Mitteln ihre Ziele erreichen. Die beste Definition: BWL befasst sich mit der Zusammenarbeit mit anderen zum gegenseitigen Vorteil.',
    kurz=p('Mia will einen Fahrradladen eröffnen. Sie hat 40.000 Euro gespart, möchte aber Werkstatt, Verkaufsraum, Lager und Onlineshop. Alles zugleich geht nicht. Genau hier beginnt die <b>Betriebswirtschaftslehre (BWL)</b>: Sie fragt, wie man mit <b>knappen Mitteln</b> möglichst gut ans Ziel kommt.')
        + p('Der Name verrät schon den Aufbau. <b>Betrieb</b> ist der Ort, an dem gewirtschaftet wird. <b>Wirtschaften</b> ist die Art, wie entschieden wird. <b>Lehre</b> heißt, dass man dieses Wissen weitergibt und nutzbar macht.'),
    fig=fw('Der Name in drei Teilen. Tippe auf einen Kasten.') + bild(fig_bwl),
    figcap='nach Folie „Definition: Zusammenführung“',
    article=h3('Vier Versuche einer Definition')
        + p('Was BWL genau ist, wird seit über hundert Jahren diskutiert. In der Vorlesung stehen vier Definitionen nebeneinander. Jede hat eine Schwäche, und gerade die Schwächen zeigen, worum es geht.')
        + tabelle(['Definition', 'Was daran stört'], [
            ['„Betriebswirtschaft ist das, was Betriebswirte tun.“', 'nicht verkehrt, aber ohne Inhalt: Man erfährt nicht, <i>was</i> sie tun'],
            ['„… die Wissenschaft von den Betrieben und der Wirtschaft.“', 'zu breit: Der Architekt, der die Lagerhalle entwirft, arbeitet auch für einen Betrieb, ist aber kein Betriebswirt'],
            ['„… untersucht menschliches Verhalten, das eine Beziehung zwischen Zielen und knappen Mitteln mit unterschiedlicher Verwendung herstellt.“', 'inhaltlich sehr gut, sprachlich etwas zu breit (trifft auch auf andere Fächer zu)'],
            ['„… befasst sich mit den Möglichkeiten und Problemen der Zusammenarbeit mit anderen zum gegenseitigen Vorteil.“', 'die beste Fassung: Wirtschaft ist Tausch, bei dem beide gewinnen']])
        + p('Die dritte Definition trifft das <b>Grundproblem</b>: Ziele und knappe Mittel müssen in Einklang gebracht werden. ' + eg('Man will mehr, als man bezahlen kann. Also muss man auswählen.'))
        + bsp('Zwei Produkte, ein Werbebudget', 'Mias Laden verkauft E-Bikes (laufen gut) und Kinderräder (laufen schlecht). Für eine Werbekampagne reicht das Geld nur einmal.',
              [('Ziel: mehr Umsatz mit beiden Produkten.', ''), ('Mittel: ein Budget, das nur für <b>eine</b> Kampagne reicht.', ''), ('Mia muss entscheiden: Kampagne für E-Bikes (sicherer Erfolg) oder für Kinderräder (größerer Nachholbedarf).', 'Ziele und knappe Mittel abwägen')],
              'Genau diese Abwägung ist der Kern der BWL.')
        + weiter('Die vierte Definition schaut auf die andere Seite: Warum tauschen Menschen überhaupt?')
        + h3('Zusammenarbeit zum gegenseitigen Vorteil')
        + p('Beim Kauf eines Smartphones für 1.500 Euro bekommt die Käuferin das Gerät und gibt das Geld her. Der Hersteller bekommt das Geld und gibt das Gerät her. <b>Beide</b> fühlen sich danach besser gestellt, sonst hätten sie nicht getauscht. Die Frage der BWL lautet deshalb: Wie schaffe ich es, dass Menschen mein Produkt kaufen, weil <b>sie</b> dadurch einen Vorteil haben?')
        + cards([('Käuferin', 'gibt 1.500 €, bekommt ein Gerät, das ihr mehr wert ist'), ('Hersteller', 'gibt das Gerät, bekommt 1.500 €, die ihm mehr wert sind'), ('Ergebnis', 'beide gewinnen: freiwilliger Tausch')])
        + weiter('Aus „Betrieb“, „Wirtschaften“ und „Lehre“ wird eine Gesamtdefinition.')
        + h3('Die Zusammenführung')
        + cards([('„Betriebs-“', 'Ein <b>Betrieb</b> ist eine planvoll organisierte Wirtschaftseinheit, in der Produktionsfaktoren kombiniert werden, um Güter oder Dienstleistungen herzustellen oder abzusetzen.'),
                 ('„-wirtschafts-“', '<b>Wirtschaften</b> bedeutet eine langfristige Maximierung des Gewinns unter Beachtung von Nebenbedingungen und folgt dem ökonomischen Prinzip.'),
                 ('„-lehre“', 'Die <b>Lehre</b> umfasst die Beschreibung und Verdeutlichung betriebswirtschaftlicher Erkenntnisse, um sie für den Einsatz nutzbar zu machen.')])
        + p('Ein Beispiel für „Lehre“: Marketingstrategien lassen sich mit den <b>4 P</b> beschreiben: Product (Produkt), Price (Preis), Place (Vertrieb) und Promotion (Kommunikation). Im Studium wird dieses Wissen in Vorlesungen vermittelt und in Projekt-, Seminar- und Bachelorarbeiten mit der Praxis verbunden.')
        + klausur_hinweis('Definitionen werden nicht wörtlich abgefragt. Du musst aber erkennen, was BWL ausmacht: Ziele gegen knappe Mittel abwägen und Tausch zum gegenseitigen Vorteil.')
        + wahr('w-bwl', [('Die BWL beschäftigt sich mit dem Grundproblem „unendliche Bedürfnisse, knappe Mittel“.', True, 'Das ist der Ausgangspunkt jeder betriebswirtschaftlichen Entscheidung.'),
                         ('„BWL ist das, was Betriebswirte tun“ ist eine inhaltlich genaue Definition.', False, 'Sie ist nicht falsch, sagt aber nichts über den Inhalt.'),
                         ('Bei einem freiwilligen Kauf haben Käufer und Verkäufer einen Vorteil.', True, 'Sonst käme der Tausch nicht zustande.')]),
    merk='BWL: Ziele und knappe Mittel in Einklang bringen. Beste Definition: Zusammenarbeit mit anderen zum gegenseitigen Vorteil. Betrieb (wo) + Wirtschaften (wie) + Lehre (wozu).',
    exam='Erkennen, was BWL ausmacht (Grundproblem knappe Mittel, Tausch zum gegenseitigen Vorteil); die drei Teile des Begriffs.',
    fehler=['Glauben, BWL sei einfach „alles, was mit Wirtschaft zu tun hat“. Es geht um Entscheidungen bei knappen Mitteln.', 'Beim Tausch denken, einer verliert. Beim freiwilligen Tausch gewinnen beide.'],
    src='Folien 5–9, 69–71')

# ---------------------------------------------------------------- 2 Der Betrieb
fig_betrieb = svg(360, 300,
    box(116, 106, 128, 84, 'Betrieb\nkombiniert die\nProduktions-\nfaktoren', size=13, art='hl', tip='Im Betrieb werden die drei Produktionsfaktoren Arbeit, Betriebsmittel und Werkstoffe kombiniert. Ergebnis sind Produkte und Dienstleistungen.')
    + box(4, 6, 112, 42, 'Staat', size=13, tip='Der Staat setzt Gesetze und Vorschriften, erhebt Steuern (nicht zweckgebunden) und Abgaben (zweckgebunden) und stellt Verkehrswege, Gewerbegebiete und ein Finanzsystem bereit.')
    + box(244, 6, 112, 42, 'Gesellschaft', size=13, tip='Die Gesellschaft hat Erwartungen an den Betrieb, etwa Umweltschutz, faire Löhne und Sicherheit.')
    + box(4, 122, 102, 52, 'Beschaffungs-\nmarkt', size=13, tip='Hier kauft der Betrieb Rohstoffe, Teile und Maschinen ein. Mia kauft Fahrräder und Ersatzteile beim Großhändler.')
    + box(254, 122, 102, 52, 'Absatz-\nmarkt', size=13, tip='Hier verkauft der Betrieb seine Produkte und Dienstleistungen. Mia verkauft Räder und Reparaturen an Kundinnen und Kunden.')
    + box(4, 248, 110, 46, 'Kapital-\nmarkt', size=13, tip='Hier bekommt der Betrieb Geld: Kredite von Banken (gegen Zinsen und Sicherheiten) oder Eigenkapital von Anteilseignern (gegen einen Teil des Gewinns).')
    + box(125, 248, 110, 46, 'Arbeits-\nmarkt', size=13, tip='Hier findet der Betrieb Personal. Mia sucht eine Zweiradmechanikerin.')
    + box(246, 248, 110, 46, 'Konkurrenz', size=13, tip='Andere Anbieter desselben oder eines Ersatzprodukts. Für Mia: andere Fahrradläden, aber auch Carsharing und die Straßenbahn als Ersatz (Substitut).')
    + pfeil(106, 148, 114, 148) + pfeil(246, 148, 254, 148) + pfeil(60, 50, 130, 104) + pfeil(300, 50, 230, 104)
    + pfeil(59, 246, 130, 192) + pfeil(180, 246, 180, 192) + pfeil(301, 246, 230, 192),
    'Der Betrieb und sein Umfeld', maxw=420)

t_betrieb = thema('betrieb', 'Der Betrieb: Produktionsfaktoren und Umfeld',
    kern='Ein Betrieb ist eine planvoll organisierte Wirtschaftseinheit. Er kombiniert Arbeit, Betriebsmittel und Werkstoffe, um Güter oder Dienstleistungen herzustellen oder abzusetzen.',
    kurz=p('Mias Laden ist ein <b>Betrieb</b>: kein Zufall und keine spontane Aktion, sondern <b>planvoll organisiert</b>. Dort kommen drei Dinge zusammen, die <b>Produktionsfaktoren</b>: Mias Arbeit, die Werkstatt mit Montageständer und die Teile, die sie verbaut.')
        + p('Der Betrieb lebt nicht allein. Er kauft auf dem <b>Beschaffungsmarkt</b> ein, verkauft auf dem <b>Absatzmarkt</b>, holt Geld auf dem <b>Kapitalmarkt</b> und Personal auf dem <b>Arbeitsmarkt</b>. Dazu kommen Staat, Gesellschaft und Konkurrenz.'),
    fig=fw('Der Betrieb in seinem Umfeld. Tippe auf einen Kasten.') + bild(fig_betrieb),
    figcap='nach Folien „Betrieb als Erfahrungsobjekt der BWL“',
    article=h3('Die Definition, Wort für Wort')
        + p('„Als <b>Betrieb</b> bezeichnet man eine planvoll organisierte Wirtschaftseinheit, in der Produktionsfaktoren kombiniert werden, um Güter und Dienstleistungen herzustellen oder abzusetzen.“')
        + cards([('planvoll organisiert', 'nicht zufällig und nicht spontan: Es gibt Abläufe, Zuständigkeiten, Ziele'), ('Wirtschaftseinheit', 'eine abgegrenzte Einheit, die wirtschaftet'), ('Produktionsfaktoren kombiniert', 'Arbeit, Betriebsmittel und Werkstoffe werden zusammengebracht'), ('herstellen oder absetzen', 'auch ein Händler, der nur verkauft, ist ein Betrieb')])
        + weiter('Was genau wird kombiniert? Die drei Produktionsfaktoren.')
        + h3('Die drei Produktionsfaktoren')
        + tabelle(['Faktor', 'Was gehört dazu?', 'Im Fahrradladen'], [
            ['Arbeit', 'menschliche Arbeit, das Personal', 'Mia und ihre Mechanikerin'],
            ['Betriebsmittel', 'alles, was genutzt, aber nicht verbraucht wird: Maschinen, Gebäude, Werkzeug, Bürostuhl', 'Werkstatt, Montageständer, Kasse'],
            ['Werkstoffe', 'alles, was verarbeitet wird: Rohstoffe, Hilfsstoffe, Betriebsstoffe', 'Schläuche, Ketten, Schrauben, Kettenöl']])
        + p('Die <b>Werkstoffe</b> teilt man noch einmal auf:')
        + cards([('Rohstoffe', 'Hauptbestandteil des Produkts: Holz, Eisen, Stahl, Kunststoff'), ('Hilfsstoffe', 'gehen ins Produkt ein, sind aber nebensächlich: Schrauben, Klebstoff, Schnur'), ('Betriebsstoffe', 'gehen nicht ins Produkt ein, halten den Betrieb am Laufen: Strom, Diesel, Öl, Fette')])
        + falle('Betriebsmittel und Betriebsstoffe verwechseln. Die Maschine ist ein Betriebs<b>mittel</b> (bleibt da). Das Öl, mit dem sie läuft, ist ein Betriebs<b>stoff</b> (wird verbraucht).')
        + weiter('Ein Betrieb braucht Partner, von denen er kauft und an die er verkauft.')
        + h3('Das Umfeld: Märkte, Staat, Gesellschaft')
        + p('Der Betrieb ist in mehrere Märkte eingebunden. Auf jedem Markt tauscht er etwas:')
        + tabelle(['Markt', 'Der Betrieb gibt', 'Der Betrieb bekommt'], [
            ['Beschaffungsmarkt', 'Geld', 'Rohstoffe, Teile, Maschinen'],
            ['Absatzmarkt', 'Produkte, Dienstleistungen', 'Geld (Umsatz)'],
            ['Kapitalmarkt (Kredit)', 'Zinsen und Sicherheiten', 'Fremdkapital'],
            ['Kapitalmarkt (Aktien)', 'Anteile am Unternehmen, Teil des Gewinns', 'Eigenkapital'],
            ['Arbeitsmarkt', 'Lohn', 'Arbeit, Wissen']])
        + p('Der <b>Staat</b> setzt Gesetze und Vorschriften, verlangt Steuern (nicht zweckgebunden) und Abgaben (zweckgebunden) und stellt dafür Verkehrswege, Gewerbegebiete und ein Finanzsystem bereit. Die <b>Konkurrenz</b> besteht nicht nur aus gleichen Anbietern, sondern auch aus <b>Substitutionsprodukten</b>: Mandelmilch ersetzt Milch, die Bahn ersetzt das Auto oder das Flugzeug.')
        + p('Innen im Betrieb arbeiten Bereiche zusammen: Unternehmensführung, Controlling, Bilanzierung, Produktion, Marketing, Vertrieb, Forschung und Entwicklung, IT und Personalmanagement.')
        + mfig('Innenleben eines Betriebs', svg(400, 190,
            box(130, 8, 140, 34, 'Unternehmensführung', size=12, tip='Gibt Ziele und Richtung vor.')
            + box(8, 56, 120, 32, 'Controlling', tip='Plant und kontrolliert Zahlen.') + box(140, 56, 120, 32, 'Produktion', art='hl', tip='Kombiniert die Produktionsfaktoren.') + box(272, 56, 120, 32, 'Marketing', tip='Bringt Produkt und Kunde zusammen.')
            + box(8, 100, 120, 32, 'Bilanzierung', tip='Hält Vermögen und Schulden fest.') + box(140, 100, 120, 32, 'F&amp;E', tip='Forschung und Entwicklung: neue Produkte.') + box(272, 100, 120, 32, 'Vertrieb', tip='Verkauft die Produkte.')
            + box(8, 144, 120, 32, 'IT', tip='Daten und Systeme.') + box(140, 144, 120, 32, 'Personal', tip='Sucht, entwickelt und bezahlt Mitarbeitende.') + box(272, 144, 120, 32, 'Einkauf', tip='Beschafft Material.'),
            'Bereiche in einem Betrieb'))
        + wahr('w-betrieb', [('Ein Montageständer in der Fahrradwerkstatt ist ein Werkstoff.', False, 'Er wird genutzt, nicht verbraucht: ein Betriebsmittel.'),
                             ('Kettenöl ist ein Betriebsstoff.', True, 'Es hält die Werkstatt am Laufen und wird verbraucht, steckt aber nicht im verkauften Produkt.'),
                             ('Auch ein Handelsbetrieb, der nur weiterverkauft, ist ein Betrieb.', True, 'Die Definition sagt: herstellen oder absetzen.')]),
    merk='Betrieb = planvoll organisierte Wirtschaftseinheit, die Produktionsfaktoren (Arbeit, Betriebsmittel, Werkstoffe) kombiniert, um Güter/Dienstleistungen herzustellen oder abzusetzen. Werkstoffe: Roh-, Hilfs-, Betriebsstoffe.',
    exam='Produktionsfaktoren zuordnen (Arbeit, Betriebsmittel, Werkstoffe; Roh-/Hilfs-/Betriebsstoffe) und die Märkte des Betriebs kennen.',
    fehler=['Betriebsmittel (bleibt) und Betriebsstoff (wird verbraucht) verwechseln.', 'Hilfsstoff und Betriebsstoff verwechseln: Der Hilfsstoff steckt im Produkt (Schraube), der Betriebsstoff nicht (Strom).'],
    src='Folien 10–14')

# ---------------------------------------------------------------- 3 Arten von Betrieben (nach Leistung)
fig_arten = svg(360, 312,
    box(4, 132, 72, 44, 'Betrieb', size=13, art='pale', tip='Betriebe lassen sich nach der Art der Leistung einteilen.')
    + box(90, 58, 106, 48, 'Sach-\nleistung', size=13, tip='Der Betrieb stellt etwas Greifbares her (sekundärer Sektor; Rohstoffgewinnung = primärer Sektor).')
    + box(90, 204, 106, 48, 'Dienst-\nleistung', size=13, art='hl', tip='Der Betrieb erbringt eine nicht greifbare Leistung (tertiärer Sektor).')
    + box(212, 6, 144, 40, 'Rohstoffgewinnung', size=13, tip='Gewinnt Rohstoffe aus der Natur. Beispiel: Kieswerk. Primärer Sektor.')
    + box(212, 54, 144, 40, 'Produktionsmittel', size=13, tip='Stellt Maschinen und Anlagen für andere Betriebe her. Beispiel: Bosch, Maschinenbauer.')
    + box(212, 102, 144, 40, 'Konsumgüter', size=13, tip='Stellt Güter für Endverbraucher her. Beispiel: Samsung (Fernseher), Brauerei.')
    + box(212, 162, 144, 38, 'Handel', size=13, tip='Kauft und verkauft weiter. Beispiel: Edeka, Rewe.')
    + box(212, 206, 144, 38, 'Banken', size=13, tip='Finanzbetriebe: Kredite, Konten, Zahlungsverkehr.')
    + box(212, 250, 144, 38, 'Versicherungen', size=13, tip='Versicherungsbetriebe, z. B. Allianz.')
    + T(284, 302, '… Verkehr, Beratung, IT', 12, 400, 'middle', 'var(--muted)')
    + pfeil(76, 146, 88, 92) + pfeil(76, 162, 88, 218)
    + pfeil(196, 76, 210, 28) + pfeil(196, 82, 210, 75) + pfeil(196, 88, 210, 120)
    + pfeil(196, 222, 210, 182) + pfeil(196, 228, 210, 225) + pfeil(196, 234, 210, 268),
    'Betriebe nach der Art der Leistung', maxw=420)

t_arten = thema('leistungsart', 'Betriebe nach der Art der Leistung und Güterarten',
    kern='Nach der Leistung unterscheidet man Sachleistungsbetriebe (Rohstoffgewinnung, Produktionsmittel, Konsumgüter) und Dienstleistungsbetriebe (Handel, Banken, Versicherungen, sonstige).',
    kurz=p('Nicht jeder Betrieb baut etwas. Das Kieswerk holt Rohstoffe aus dem Boden, der Maschinenbauer baut Maschinen für andere Betriebe, die Brauerei braut Bier für uns alle. Das sind <b>Sachleistungsbetriebe</b>.')
        + p('Mias Werkstatt repariert Räder: Sie erbringt eine <b>Dienstleistung</b>. Auch Supermärkte, Banken und Versicherungen sind <b>Dienstleistungsbetriebe</b>. Viele Betriebe sind beides: Mia verkauft Räder <i>und</i> repariert sie.'),
    fig=fw('Die Einteilung nach der Art der Leistung. Tippe auf die Kästen.') + bild(fig_arten),
    figcap='nach Folie „Betrieb … nach der Art der Leistung“',
    article=h3('Sachleistung oder Dienstleistung')
        + tabelle(['Art', 'Was wird geleistet?', 'Beispiel', 'Sektor'], [
            ['Rohstoffgewinnungsbetrieb', 'Rohstoffe aus der Natur', 'Kieswerk, Bergbau', 'primär'],
            ['Produktionsmittelbetrieb', 'Maschinen, Anlagen für andere Betriebe', 'Bosch, Maschinenbau', 'sekundär'],
            ['Konsumgüterbetrieb', 'Güter für Endverbraucher', 'Samsung, Brauerei', 'sekundär'],
            ['Handelsbetrieb', 'Waren einkaufen und weiterverkaufen', 'Edeka, Rewe', 'tertiär'],
            ['Finanzbetrieb (Bank)', 'Kredite, Konten, Zahlungen', 'Sparkasse', 'tertiär'],
            ['Versicherungsbetrieb', 'Absicherung gegen Risiken', 'Allianz', 'tertiär'],
            ['sonstige Dienstleister', 'Beratung, Verkehr, IT', 'IT-Beratung, Internetdienste', 'tertiär']])
        + p('Manche sprechen von einem <b>quartären Sektor</b> für reine Informationsdienstleistungen (IT-Beratung, Internetdienste). Das wird seit etwa zwanzig Jahren diskutiert. Ohne Kritik ist das aber nicht: Eigentlich sind auch das Dienstleistungsbetriebe.')
        + p('Die Gewichte der Sektoren haben sich verschoben: Früher arbeiteten die meisten Menschen in der Landwirtschaft, heute die meisten im Dienstleistungsbereich. ' + eg('Es gibt eine Entwicklung von der Rohstoffgewinnung über die Industrie zu den Dienstleistungen.'))
        + p('Viele Betriebe sind <b>beides</b>: Eine Brauerei produziert Bier (Sachleistung) und betreibt davor ein Restaurant (Dienstleistung).')
        + '<!--mf:handel-->' + p('<b>Achtung beim Handel:</b> Ein Handelsbetrieb stellt nichts her. Handels-, Finanz- und Versicherungsbetriebe zählen deshalb zu den <b>Dienstleistungsbetrieben</b>. Eine Autowerkstatt, die repariert und Ersatzteile verkauft, ist also ein reiner Dienstleistungsbetrieb: Reparatur ist Dienstleistung, Ersatzteilverkauf ist Handel.')
        + weiter('Nicht nur Betriebe, auch die Güter selbst lassen sich einteilen.')
        + h3('Wirtschaftsgüter klassifizieren')
        + tabelle(['Gegensatzpaar', 'Unterschied', 'Beispiel'], [
            ['Input- vs. Outputgüter', 'geht in die Produktion ein oder kommt heraus', 'Stahl (Input) · Fahrrad (Output)'],
            ['Investitions- vs. Konsumgüter', 'für Betriebe zur Produktion oder für private Verbraucher', 'Montageständer · Stadtrad für Privatkunden'],
            ['Verbrauchs- vs. Gebrauchsgüter', 'einmal verbraucht oder lange genutzt', 'Kettenöl · Fahrrad'],
            ['materielle vs. immaterielle Güter', 'greifbar oder nicht greifbar', 'Fahrrad · Reparatur, Software'],
            ['Real- vs. Nominalgüter', 'Sachen und Dienste oder Geld und Rechte', 'Fahrrad · Aktien, Fonds, Geld'],
            ['problemlose vs. problemvolle Güter', 'Kauf ohne Nachdenken oder mit viel Beratung', 'Klingel · E-Bike für 4.000 €']])
        + falle('Real- und Nominalgüter verwechseln. Nominalgüter sind Geld und Rechte auf Geld (Aktien, Fonds, Forderungen), nicht „wertlose“ Güter.')
        + spiel('sp-gueter', 'Ordne zu: Sachleistung oder Dienstleistung?', ['Sachleistung', 'Dienstleistung'],
                [('Kieswerk', 0, 'Rohstoffgewinnung: greifbare Leistung'), ('Versicherung', 1, 'Absicherung ist nicht greifbar'), ('Maschinenbauer', 0, 'Produktionsmittel'), ('Supermarkt', 1, 'Handel ist eine Dienstleistung'), ('Brauerei (nur Bierherstellung)', 0, 'Konsumgüter'), ('Friseur', 1, 'Haarschnitt: nicht lagerbar, Kunde wirkt mit')]),
    merk='Sachleistungsbetriebe: Rohstoffgewinnung, Produktionsmittel, Konsumgüter. Dienstleistungsbetriebe: Handel, Banken, Versicherungen, sonstige. Viele Betriebe sind beides.',
    exam='Betriebe nach der Art der Leistung zuordnen; Güterpaare unterscheiden (z. B. Real- vs. Nominalgüter).',
    fehler=['Den Handel zu den Sachleistungen zählen. Er stellt nichts her, er verteilt: Dienstleistung.', 'Nominalgüter für „wertlos“ halten. Gemeint sind Geld und Rechte (Aktien, Fonds).'],
    src='Folien 15–19')

# ---------------------------------------------------------------- 4 Dienstleistung und Uno-actu-Prinzip
def zeitstrahl():
    s = T(4, 18, 'Sachgut (Fahrrad)', 14, 800, 'start')
    s += box(4, 30, 108, 50, 'herstellen', size=13, tip='Das Fahrrad wird in der Fabrik gebaut, ohne dass die Kundin dabei ist.')
    s += pfeil(113, 55, 123, 55)
    s += box(126, 30, 108, 50, 'lagern,\nversenden', size=13, tip='Das Fahrrad kann gelagert und verschickt werden. Man kann auf Vorrat produzieren.')
    s += pfeil(235, 55, 245, 55)
    s += box(248, 30, 108, 50, 'nutzen', size=13, tip='Erst viel später fährt die Kundin damit. Herstellen und Nutzen sind zeitlich getrennt.')
    s += T(4, 112, 'Dienstleistung (Haarschnitt)', 14, 800, 'start')
    s += box(4, 124, 352, 60, 'herstellen und nutzen gleichzeitig:\nUno-actu-Prinzip', size=13, art='hl', tip='Uno actu (lateinisch „in einem Akt“): Leistung und Konsum fallen zeitlich zusammen. Der Friseur schneidet, während die Kundin die Leistung bekommt. Auf Vorrat geht das nicht.')
    s += T(180, 204, 'Kundin ist dabei · nicht lagerbar', 13, 600, 'middle', 'var(--muted)')
    return svg(360, 214, s, 'Sachgut und Dienstleistung im Zeitablauf', maxw=420)

t_dl = thema('dienstleistung', 'Was ist eine Dienstleistung? Das Uno-actu-Prinzip', star=True,
    kern='Dienstleistungen sind immateriell, werden nach dem Uno-actu-Prinzip im selben Moment erbracht und genutzt, sind nicht lager- und transportfähig, schwanken in der Qualität, und der Kunde wirkt mit.',
    kurz=p('Ein Fahrrad kann man im Januar bauen, im März verschicken und im Mai verkaufen. Eine Reparatur nicht: Mia repariert das Rad <b>genau dann</b>, wenn die Kundin es bringt. Herstellung und Nutzung fallen zusammen. Das nennt man das <b>Uno-actu-Prinzip</b> („in einem Akt“).')
        + p('Am klarsten sieht man es beim <b>Friseur</b>: Er kann nicht auf Vorrat fünf Haarschnitte produzieren. Und ohne die Kundin und ihre Haare geht es gar nicht. Sie ist an der Leistung <b>beteiligt</b>.'),
    fig=fw('Sachgut und Dienstleistung im Zeitablauf. Tippe auf die Kästen.') + bild(zeitstrahl()),
    figcap='nach Folie „Definition Dienstleistung“ (Merkmalsdefinition)',
    article=h3('Drei Wege, Dienstleistung zu definieren')
        + p('Was eine Dienstleistung ist, scheint klar, ist aber schwer zu fassen. Die Vorlesung zeigt drei Versuche:')
        + tabelle(['Versuch', 'Idee', 'Problem'], [
            ['1. Negativdefinition', '„Dienstleistungen sind alle Tätigkeiten, die keine Sachleistung sind.“', 'funktioniert nicht: Man sagt nur, was sie <i>nicht</i> ist'],
            ['2. Enumerative Definition', 'Aufzählung aller Dienstleistungen (Handel, Bank, Versicherung …)', 'nie vollständig, neue Dienste fehlen'],
            ['3. Merkmalsdefinition', 'typische Merkmale nennen', 'der beste Weg, Merkmale siehe unten']])
        + weiter('Die Merkmalsdefinition ist die wichtigste. Diese Merkmale musst du sicher erkennen.')
        + h3('Die Merkmale einer Dienstleistung')
        + merkliste('Merkmale', 'Merkmalsdefinition', [
            '<b>Immaterialität</b>: Dienstleistungen kann man nicht anfassen (Rechtsberatung, Haarschnitt).',
            '<b>Uno-actu-Prinzip</b>: Leistung und Konsum erfolgen in einem Schritt. Beim Sachgut wird erst produziert, dann konsumiert.',
            '<b>Nicht lager- und transportfähig</b>: Man kann nicht „auf Vorrat produzieren“, keine fünf Haarschnitte im Voraus.',
            '<b>Schwankungen der Leistungsqualität</b>: Jeder Haarschnitt wird etwas anders (das schwächste Argument, denn auch Sachgüter schwanken).',
            '<b>Der Dienstleistungsnehmer ist beteiligt</b>: Der Friseur braucht meine Haare, um sie zu schneiden (externer Faktor).'],
            'I-U-N-S-B: Immateriell, Uno actu, Nicht lagerbar, Schwankend, Beteiligt')
        + p('Das <b>Uno-actu-Prinzip</b> ist das Merkmal, das am häufigsten gefragt wird. ' + eg('Herstellen und Nutzen passieren gleichzeitig. Der Kunde ist dabei.'))
        + bsp('Uno actu erkennen', 'Welche Aussage passt zum Uno-actu-Prinzip? a) Die Werkstatt baut Laufräder vor, um im Frühjahr schneller zu sein. b) Mia stellt die Schaltung ein, während die Kundin daneben steht und Probe fährt.',
              [('a) Laufräder vorbauen heißt auf Vorrat produzieren. Das geht nur bei Sachgütern.', 'passt nicht'), ('b) Leistung (Einstellen) und Nutzung (Probefahrt) im selben Moment, Kundin beteiligt.', 'passt: Uno actu')])
        + falle('Uno actu mit „schnell“ verwechseln. Es geht nicht um Tempo, sondern darum, dass Erbringen und Nutzen zeitlich zusammenfallen.')
        + weiter('In der Praxis ist die Grenze zwischen Sachgut und Dienstleistung oft fließend.')
        + h3('Mischformen')
        + p('„Manchmal sind Betriebe beides“: Eine Brauerei braut Bier (Sachleistung) und betreibt davor ein Restaurant (Dienstleistung). Mia verkauft Räder (Sachgut) und wartet sie (Dienstleistung). Viele Produkte werden heute als Paket aus Sachgut und Service verkauft, etwa das E-Bike mit Inspektionsvertrag.')
        + klausur_hinweis('Typische Auswahlfrage: „Was versteht man unter dem Uno-actu-Prinzip?“ oder „Welche Aussage passt dazu?“. Denk an den Friseur: Leistung und Konsum fallen zeitlich zusammen.')
        + wahr('w-dl', [('Beim Uno-actu-Prinzip fallen Produktion und Konsum zeitlich zusammen.', True, 'Das ist die Definition.'),
                        ('Dienstleistungen kann man gut auf Vorrat produzieren.', False, 'Sie sind nicht lagerfähig.'),
                        ('Die Negativdefinition ist der beste Weg, Dienstleistungen zu beschreiben.', False, 'Sie funktioniert nicht; am besten ist die Merkmalsdefinition.'),
                        ('Beim Friseur ist die Kundin an der Leistung beteiligt.', True, 'Ohne ihre Haare keine Leistung: externer Faktor.')]),
    merk='Dienstleistung (Merkmalsdefinition): immateriell, Uno actu (Leistung und Konsum gleichzeitig), nicht lager- und transportfähig, schwankende Qualität, Kunde beteiligt.',
    exam='Uno-actu-Prinzip erklären bzw. passende Aussage auswählen (Friseur); Merkmale einer Dienstleistung erkennen.',
    fehler=['Uno actu als „besonders schnell“ verstehen. Es heißt: gleichzeitig herstellen und nutzen.', 'Schwankende Qualität als stärkstes Merkmal nennen. Es ist das schwächste.'],
    src='Folien 17–18')

# ---------------------------------------------------------------- 5 Betriebe nach Zweck und Größe
fig_zweck = svg(360, 168,
    T(90, 14, 'fremder Bedarf', 13, 700, 'middle', 'var(--muted)') + T(270, 14, 'eigener Bedarf', 13, 700, 'middle', 'var(--muted)')
    + box(4, 26, 84, 66, 'Privat-\nunter-\nnehmen', size=13, art='hl', tip='Erwerbswirtschaftlicher Betrieb. Ziel: Gewinnmaximierung. Beispiele: SAP, Roche, Mias Fahrradladen.')
    + box(92, 26, 84, 66, 'Öffentl.\nUnter-\nnehmen', size=13, tip='Gehört dem Staat. Ziel: Kostenminimierung bei vorgegebener Leistung. Beispiele: Stadtbücherei, DHBW, Uniklinikum, Bürgeramt.')
    + box(184, 26, 84, 66, 'Privater\nHaushalt', size=13, tip='Deckt den eigenen Bedarf. Ziel: Nutzenmaximierung.')
    + box(272, 26, 84, 66, 'Öffentl.\nHaushalt', size=13, tip='Deckt den Bedarf der Allgemeinheit. Ziel: Wohlfahrtsmaximierung (z. B. bestmögliche Kulturdarbietung).')
    + strich(180, 22, 180, 160)
    + T(46, 114, 'Gewinn-', 12, 700) + T(46, 130, 'maximierung', 12, 700) + T(134, 114, 'Kosten-', 12, 700) + T(134, 130, 'minimierung', 12, 700)
    + T(226, 114, 'Nutzen-', 12, 700) + T(226, 130, 'maximierung', 12, 700) + T(314, 114, 'Wohlfahrts-', 12, 700) + T(314, 130, 'maximierung', 12, 700)
    + T(90, 156, 'Unternehmen', 12, 400, 'middle', 'var(--muted)') + T(270, 156, 'Haushalte', 12, 400, 'middle', 'var(--muted)'),
    'Betriebe nach ihrem Zweck', maxw=420)

t_zweck = thema('betriebszweck', 'Betriebe nach Zweck und Größe', star=True,
    kern='Nach dem Zweck unterscheidet man Privatunternehmen (Gewinnmaximierung), öffentliche Unternehmen (Kostenminimierung), private Haushalte (Nutzenmaximierung) und öffentliche Haushalte (Wohlfahrtsmaximierung).',
    kurz=p('Mia führt ihren Laden, um <b>Gewinn</b> zu machen. Die Stadtbücherei nebenan soll dagegen keinen Gewinn machen, sondern ihre Aufgabe mit möglichst <b>wenig Kosten</b> erfüllen. Beide sind Betriebe, aber mit verschiedenem <b>Zweck</b>.')
        + p('Unternehmen decken <b>fremden Bedarf</b>: Sie produzieren für andere. Haushalte decken ihren <b>eigenen Bedarf</b>. Aus diesen zwei Unterscheidungen entstehen vier Arten mit vier verschiedenen Zielen.'),
    fig=fw('Vier Arten von Wirtschaftseinheiten und ihre Ziele. Tippe auf die Kästen.') + bild(fig_zweck),
    figcap='nach Folien „Betrieb … nach ihrem Zweck“',
    article=h3('Privat oder öffentlich')
        + tabelle(['Merkmal', 'Privatunternehmen', 'Öffentliches Unternehmen'], [
            ['Globalziel', 'Gewinnmaximierung', 'Kostenminimierung'],
            ['Zweck', 'frei gewählt (z. B. Arzneimittel herstellen)', 'vom Gesetz vorgegeben (z. B. Pässe ausstellen)'],
            ['Leistungsbestimmung', 'Kunde und Markt', 'Staat (Gesetz)'],
            ['Wettbewerb', 'ja', 'kaum („Ich bekomme keinen Termin, habe aber keine andere Wahl.“)'],
            ['Finanzierung', 'Eigen- und Fremdkapital', 'Steuern und Gebühren'],
            ['Risiko', 'Eigentümer', 'keiner'],
            ['Beispiele', 'SAP, MVV, Roche, Mias Laden', 'Stadtbücherei, DHBW, Uniklinikum, Ordnungsamt, Rathaus']])
        + p('Die Unterschiede sind „intuitiv nachvollziehbar“: Wer sich den Zweck selbst aussucht und im Wettbewerb steht, finanziert sich am Markt und trägt das Risiko selbst.')
        + weiter('Neben den Unternehmen gibt es die Haushalte. Sie wirtschaften für sich selbst.')
        + h3('Unternehmen und Haushalte')
        + tabelle(['', 'Ziel', 'Beispiel'], [
            ['Privatunternehmen', 'Gewinnmaximierung', 'Fahrradladen'],
            ['Öffentliches Unternehmen', 'Kostenminimierung', 'Stadtwerke, Bücherei'],
            ['Privater Haushalt', 'Nutzenmaximierung', 'Familie, die ihr Einkommen verteilt'],
            ['Öffentlicher Haushalt', 'Wohlfahrtsmaximierung', 'Stadt, die die bestmögliche Kulturdarbietung bietet (z. B. Nationaltheater)']])
        + klausur_hinweis('Auswahlfrage „Betrieb nach Zweck“: Ordne Beispiel und Ziel richtig zu. Öffentliches Unternehmen = Kostenminimierung, nicht Gewinnmaximierung.')
        + weiter('Ein weiterer Blick auf Betriebe: Wie groß sind sie?')
        + h3('Betriebe nach Größe')
        + p('Welche Kriterien eignen sich, um die Größe eines Unternehmens festzustellen? Es gibt drei Gruppen:')
        + mfig('Kriterien der Unternehmensgröße', svg(560, 230,
            box(200, 6, 160, 40, 'Unternehmensgröße', art='hl', size=13, tip='Welche Kriterien eignen sich zur Feststellung der Unternehmensgröße? Drei Gruppen.')
            + pfeil(250, 48, 96, 70) + pfeil(280, 48, 280, 70) + pfeil(310, 48, 464, 70)
            + box(8, 72, 176, 48, 'Finanzielle\nKennzahlen', size=13, tip='Gewinn, Umsatz, Eigenkapital, Bilanzsumme.')
            + box(192, 72, 176, 48, 'Arbeitsrelevante\nAnknüpfungspunkte', size=13, tip='Mitarbeiteranzahl, geleistete Arbeitsstunden.')
            + box(376, 72, 176, 48, 'Branchenspezifische\nFaktoren', size=13, tip='Verkaufsfläche (Einzelhandel), Hektoliter Ausstoß (Brauerei), vergebene Kreditsummen (Banken), beförderte Personen (Lufthansa).')
            + box(8, 132, 176, 88, '· Gewinn\n· Umsatz\n· Eigenkapital\n· Bilanzsumme', size=13, art='weak')
            + box(192, 132, 176, 88, '· Mitarbeiteranzahl\n· Arbeitsstunden', size=13, art='weak')
            + box(376, 132, 176, 88, '· Verkaufsfläche\n· Hektoliter Ausstoß\n· Kreditsummen\n· beförderte Personen', size=13, art='weak'),
            'Kriterien der Unternehmensgröße'), 'nach Folie „Betrieb … (nach Größe)“')
        + p('<b>Eine Kennzahl reicht nicht.</b> Google macht mit verhältnismäßig wenigen Mitarbeitern sehr hohe Gewinne, Volkswagen hat sehr viele Mitarbeiter. Nach Mitarbeitern wäre VW viel größer, nach Gewinn vielleicht nicht. Deshalb nimmt man mehrere Kennzahlen.')
        + zusatz('Die Tabellen mit Vor- und Nachteilen einzelner Größenkriterien, die Größenklassen nach Handelsrecht und EU (Kleinst-, kleine, mittlere, große Unternehmen) und die Zahlen zu KMU (99,6 % aller Unternehmen, 60 % der Beschäftigten) stehen in den Folien, wurden aber übersprungen.')
        + wahr('w-zweck', [('Öffentliche Unternehmen verfolgen das Ziel der Gewinnmaximierung.', False, 'Ihr Globalziel ist die Kostenminimierung.'),
                           ('Private Haushalte maximieren ihren Nutzen.', True, 'Sie decken den eigenen Bedarf.'),
                           ('Die Größe eines Unternehmens misst man am besten mit nur einer Kennzahl.', False, 'Eine Kennzahl reicht nicht (Google gegen VW).')]),
    merk='Privatunternehmen: Gewinnmaximierung. Öffentliches Unternehmen: Kostenminimierung. Privater Haushalt: Nutzenmaximierung. Öffentlicher Haushalt: Wohlfahrtsmaximierung. Größe: mehrere Kennzahlen nötig.',
    exam='Betriebe nach Zweck zuordnen (Ziel, Finanzierung, Risiko); Kriterien der Unternehmensgröße nennen.',
    fehler=['Öffentlichen Unternehmen Gewinnmaximierung zuschreiben.', 'Haushalte und Unternehmen verwechseln: Haushalte decken den eigenen Bedarf.'],
    src='Folien 20–23')

# ---------------------------------------------------------------- 6 Geschichte der BWL
fig_gesch = svg(360, 228,
    linie([(20, 50), (340, 50)], 'var(--axis2)', 2)
    + punkt(60, 50, 'var(--c1)') + punkt(180, 50, 'var(--primary)', 7) + punkt(300, 50, 'var(--c1)')
    + T(60, 26, '1898', 15, 800) + T(180, 26, '1907', 15, 800) + T(300, 26, '1912', 15, 800)
    + box(4, 66, 112, 54, 'Geburtsjahr\nder BWL', size=13, tip='1898 gilt als Geburtsjahr der BWL als Wissenschaft.')
    + box(124, 66, 112, 54, 'Handelshoch-\nschule Mannheim', size=12, art='hl', tip='1907 wird die Handelshochschule Mannheim gegründet. Mannheim ist ganz weit vorne in der Geschichte der BWL.')
    + box(244, 66, 112, 54, 'Abgrenzung\nzur VWL', size=13, tip='1912: Die BWL grenzt sich als eigenes Fach von der Volkswirtschaftslehre ab.')
    + box(4, 140, 112, 80, 'Nicklisch\n\nsozialistisch', size=12, tip='Heinrich Nicklisch: sozialistische Perspektive. „Gemeinnutz geht vor Eigennutz“: Was allen guttut, ist auch für den Einzelnen gut.')
    + box(124, 140, 112, 80, 'Schmalenbach\n\nkapitalistisch', size=12, tip='Eugen Schmalenbach (1873–1955): kapitalistische Perspektive, der Gegenpol zu Nicklisch. Leitsatz: „Gemeinwirtschaftliche Wirtschaftlichkeit“.')
    + box(244, 140, 112, 80, 'Rieger\n\nkombiniert\nbeides', size=12, tip='Wilhelm Rieger (1878–1971): kombiniert beide Sichten, die Idee der sozialen Marktwirtschaft. „Gemeinnutz kommt vom Eigennutz.“'),
    'Geschichte der BWL vor dem Zweiten Weltkrieg', maxw=420)

t_gesch = thema('geschichte', 'Geschichte der BWL', aus=True,
    kern='Die BWL ist eine junge Wissenschaft: 1898 gilt als Geburtsjahr, 1907 wird die Handelshochschule Mannheim gegründet, 1912 grenzt sich die BWL von der VWL ab.',
    kurz=p('Lange war BWL eine reine <b>Lehre</b>: Man brachte Kaufleuten bei, wie man Bücher führt und kalkuliert, ohne Theorie dahinter. Erst um 1900 wurde daraus eine <b>Wissenschaft</b>.')
        + p('Mannheim war dabei „ganz weit vorne“: 1907 wurde hier eine der ersten Handelshochschulen gegründet. Drei Professoren prägten früh die Frage, ob ein Betrieb dem Einzelnen oder der Gemeinschaft dienen soll.'),
    fig=fw('Drei Daten und drei Positionen. Tippe auf die Kästen.') + bild(fig_gesch),
    figcap='nach Folie „Geschichte der BWL: Vor dem Zweiten Weltkrieg“',
    article=h3('Von der Lehre zur Wissenschaft')
        + p('Am Anfang stand die <b>Lehre</b>: Buchführung, Kalkulation, Kaufmannsrecht. Eine eigene Theorie gab es nicht. Erst mit den Handelshochschulen wurde die BWL zur <b>Wissenschaft</b>.')
        + tabelle(['Jahr', 'Ereignis'], [['1898', 'Geburtsjahr der BWL als Wissenschaft'], ['1907', 'Gründung der Handelshochschule Mannheim'], ['1912', 'Abgrenzung zur Volkswirtschaftslehre']])
        + weiter('Früh stritten Fachleute darüber, wem das Wirtschaften dienen soll.')
        + h3('Drei Positionen: Gemeinnutz oder Eigennutz?')
        + tabelle(['Person', 'Leitsatz', 'Perspektive'], [
            ['Heinrich Nicklisch', '„Gemeinnutz geht vor Eigennutz“', 'eher sozialistisch: Was allen guttut, ist auch für den Einzelnen gut'],
            ['Eugen Schmalenbach', '„Gemeinwirtschaftliche Wirtschaftlichkeit“', 'kapitalistisch: der Gegenpol zu Nicklisch'],
            ['Wilhelm Rieger', '„Gemeinnutz kommt vom Eigennutz“', 'kombiniert beides: soziale Marktwirtschaft, wer eigene Ziele verfolgt, nützt auch allen']])
        + p('Nicklisch und Schmalenbach stehen sich gegensätzlich gegenüber, Rieger verbindet beide. Riegers Gedanke findet sich später in Adam Smiths „unsichtbarer Hand“ wieder (siehe Oberthema „Wirtschaftliche Prinzipien“).')
        + weiter('Nach dem Zweiten Weltkrieg rückte das Entscheiden in den Mittelpunkt.')
        + h3('Nach dem Zweiten Weltkrieg <span class="zusatz zf zu">in den Folien gestrichen · für die Klausur nicht nötig</span>')
        + zusatz('Curt Sandig (BWL als Treffen von Entscheidungen, 1966; konstitutive und situative Entscheidungen), Konrad Mellerowicz (BWL als regelhaftes Entscheiden, 1976) und Hans Ulrich (BWL als Gestaltung von Regelkreisen, 1978/1990) stehen in den Folien, wurden aber übersprungen. Ebenso die Einordnung der BWL in die Wissenschaften (Sozialwissenschaft) und die Entwicklung der Lehre von der Handelshochschule zur Business School.')
        + p('Bis in die 1960er/70er Jahre war die BWL rein <b>ökonomisch</b> ausgerichtet: nüchterne Berechnung mit Kennzahlen. Ab den 1970ern kamen <b>verhaltenswissenschaftliche</b> Ansätze hinzu, die den Menschen realistischer sehen. Seit etwa 2000 versucht man, beides zu verbinden. Mehr dazu im Oberthema „Positionen der BWL“.')
        + wahr('w-gesch', [('Die Handelshochschule Mannheim wurde 1907 gegründet.', True, 'Mannheim war ganz vorne dabei.'),
                           ('Rieger vertrat „Gemeinnutz geht vor Eigennutz“.', False, 'Das war Nicklisch. Rieger: „Gemeinnutz kommt vom Eigennutz“.'),
                           ('1912 grenzte sich die BWL von der VWL ab.', True, 'Seitdem ist sie ein eigenes Fach.')]),
    merk='1898 Geburtsjahr der BWL, 1907 Handelshochschule Mannheim, 1912 Abgrenzung zur VWL. Nicklisch (sozialistisch): Gemeinnutz vor Eigennutz; Schmalenbach (kapitalistisch); Rieger kombiniert beides: Gemeinnutz kommt vom Eigennutz.',
    exam='Daten und Positionen (Nicklisch, Schmalenbach, Rieger) einordnen.',
    fehler=['Nicklisch und Rieger vertauschen.'],
    src='Folien 146–153')

KAPITEL = kapitel('k1', 'BWL, Betrieb und Betriebsarten',
    'Worum geht es in der BWL, was ist ein Betrieb und welche Arten von Betrieben gibt es? Durchgehendes Beispiel: Mias Fahrradladen „Radwerk“ in der Neckarstadt.',
    ['Definition', 'Betrieb', 'Leistungsart', 'Dienstleistung', 'Zweck', 'Geschichte'],
    [t_bwl, t_betrieb, t_arten, t_dl, t_zweck, t_gesch])

from mehr1 import ergaenze
ergaenze(KAPITEL)
