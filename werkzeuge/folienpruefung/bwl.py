# ABWL (Einführung in die BWL, Paul; Zusammenfassung WIN22B). Jeder Stichpunkt „fehlt vielleicht“ einzeln geprüft (13.11.2026).
# Die meisten Treffer sind Texterkennung bzw. Schreibfehler der Mitschrift auf den Folien. Echte Lücken stehen in werkzeuge/einarbeiten/bwl.py.
DECKNAME[F] = {'vl': 'Folien', 'zf': 'Zusammenfassung'}
kein(F, 'vl/2', 'Endgeräte'); kein(F, 'vl/4', '*')            # Klausurorganisation (Ablauf, Hilfsmittel)
ok(F, 'vl/5', 'Eingrenzung', 'Innenperspektive'); ok(F, 'vl/319', 'Innenperspektive')   # Gliederungsfolien
kein(F, 'vl/13', 'Kredity'); ok(F, 'vl/15', 'Quartiärer'); kein(F, 'vl/28', 'Gedanklich'); kein(F, 'vl/30', 'Schadstoffwerte')
kein(F, 'vl/31', 'Handleso'); kein(F, 'vl/34', 'Grad-warme'); kein(F, 'vl/36', 'Produktivitätsparadox')   # „lassen wir aus“
kein(F, 'vl/41', 'Gewinntunktion'); kein(F, 'vl/44', 'Geradengleichung'); kein(F, 'vl/45', 'Raufy-Ader'); kein(F, 'vl/46', 'Esgröße')
kein(F, 'vl/49', 'Dingerichtig'); kein(F, 'vl/53', 'Nachfrageändertsichnie', 'Preisanstiegsteigtgleich'); kein(F, 'vl/55', 'Steigtder', 'Verändertsich')
ok(F, 'vl/61', 'Preisbereich'); ok(F, 'vl/98', 'Preisbereich')   # Übung Mittelwertmethode steht in mittelwert/effekte
ok(F, 'vl/78', 'Gutmütigkeit', 'Streben', 'Gunsten'); ok(F, 'vl/114', 'Gutmütigkeit', 'Streben', 'Gunsten', 'Eigenliebe')   # Adam Smith in maerkte
kein(F, 'vl/90', 'Notizen'); kein(F, 'vl/91', 'preissensibell-elastisch')
kein(F, 'vl/94', 'Preisenkung', 'Unen-Malt', 'Erlösnen-Erlös'); ok(F, 'vl/94', 'Ausgangsmenge'); kein(F, 'vl/95', 'Pgegeben')
ok(F, 'vl/96', 'Nachfragepreiselastizität'); ok(F, 'vl/103', 'Luxusmarken'); kein(F, 'vl/154', 'instinkt-gestwerte')
ok(F, 'vl/161', 'Unternehmensgewinn'); ok(F, 'vl/163', 'Kapitalbetrag')
kein(F, 'vl/185', 'Aufwandstunktion', 'Nutzenfuktion', 'Antwandsmaximum'); ok(F, 'vl/185', 'Nutzenmaximum')   # Abbruchkriterium steht in et-struktur
ok(F, 'vl/210', 'Präferierte'); ok(F, 'vl/228', 'Besitzfall'); kein(F, 'vl/230', 'Koordinatensystem')
ok(F, 'vl/231', 'Besitzfall'); kein(F, 'vl/231', 'Mutungen', 'AnTafel')   # Besitztumseffekt und Ankereffekt (Fluss-Beispiel) in prospect-theory
kein(F, 'vl/258', 'Rüstungen'); ok(F, 'vl/264', 'Flixtrain', 'Flixbus', 'DBahn-', 'Fernreisen')
kein(F, 'vl/267', 'Century', 'Microfost'); kein(F, 'vl/270', 'Handengsempfehlungen'); ok(F, 'vl/276', 'Implikation'); ok(F, 'vl/287', 'Ansoffsche')
kein(F, 'vl/290', 'Mannheit-Berlin'); ok(F, 'vl/305', 'Mikropolitik'); kein(F, 'vl/305', 'Werbekommt'); kein(F, 'vl/319', 'Klausuri', 'Werbekommt')
ok(F, 'vl/319', 'Mikropolitik'); kein(F, 'vl/321', 'Werbekommt'); kein(F, 'vl/323', 'Eigentimerin'); kein(F, 'vl/326', 'Komplimentär')
for st in ('vl/174', 'vl/175', 'vl/176', 'vl/177', 'vl/178'): pass   # Einflussdiagramm jetzt in et-struktur
# Zusammenfassung (WIN22B): Schreibfehler der Vorlage; Inhalte stehen in den genannten Unterthemen
kein(F, 'zf/2', 'Preisgrenzen'); ok(F, 'zf/2', 'Absatzmärkte'); kein(F, 'zf/3', 'Grundgedanke', 'Zustandsbestrebung')
kein(F, 'zf/4', 'Nutzfunktionen'); ok(F, 'zf/4', 'Teilrisiko'); kein(F, 'zf/6', 'Deskreptives', 'Norminatives', 'Geszkostes', 'Komplimentäre'); ok(F, 'zf/6', 'Nachhinein', 'Wissenschaftsziel')
ok(F, 'zf/7', 'Vergleichswert'); kein(F, 'zf/10', 'Maximat'); kein(F, 'zf/11', 'Verkalteswissenschaftliche', 'Individum'); kein(F, 'zf/12', 'Kandeln'); ok(F, 'zf/12', 'Arbeitsvolumen')
kein(F, 'zf/14', 'ABIEHMER', 'Refferenz'); ok(F, 'zf/14', 'Nachfrageniveau', 'Rechtsanwälten', 'Selbständigen', 'Erfahrungseffekt', 'Homogenität')
kein(F, 'zf/15', 'Inovation'); kein(F, 'zf/16', 'Resourcel', 'Ressourcel', 'Hostalgünstige'); kein(F, 'zf/17', 'Verfügungsgewallt', 'Rotatial', 'Quasi-Mestel', 'Monopol-Resten'); ok(F, 'zf/17', 'Generierung')
ok(F, 'zf/18', 'Preisführer'); kein(F, 'zf/18', 'Monblanc-Kugelschreiber')
kein(F, 'zf/19', 'Platformel', 'Inovations'); ok(F, 'zf/19', 'Bestellvorgänge'); kein(F, 'zf/19', 'Kl-Komanditgesellschaft', 'Kauffrau')   # Business-Model-Folie und stille Gesellschaft sind in den Folien gestrichen
kein(F, 'zf/20', 'Komplimentär', 'Komplimentür')
