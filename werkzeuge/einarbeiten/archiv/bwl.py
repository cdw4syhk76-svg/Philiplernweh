"""ABWL: Folienstoff, der auf den Lernseiten fehlte, in den normalen Text eingearbeitet (Runde b1, 13.11.2026). Format: werkzeuge/einarbeiten.py."""
STAND = 'b1'
E = [
 dict(t='ag', nach='<h3>Merkmale aller Kapitalgesellschaften</h3>',
      block='<p>Kapitalgesellschaften sind Gebilde mit <b>eigener Rechtspersönlichkeit</b> (<b>juristische Personen</b>). Für Verbindlichkeiten <b>haftet die Gesellschaft, nicht der Gesellschafter</b>.</p>', frage=False),
 # ---- AG: Aufgaben der Organe ----
 dict(t='ag', vor='<div class="box bsp"><div class="box-h">Beispiel · Börsengang</div>',
      block='<h3>Die drei Organe der AG</h3><p>Leitungs- und Kontrollbefugnisse sind verteilt:</p><ul>'
            '<li><b>Vorstand</b>: leitet die Gesellschaft in eigener Verantwortung; ist nicht an Weisungen des AR oder der HV gebunden; erstellt den Jahresabschluss; '
            'Bestellung durch den AR für maximal 5 Jahre, Wiederwahl möglich; <b>weitgehende Berichtspflichten</b>, insbesondere gegenüber dem AR.</li>'
            '<li><b>Aufsichtsrat</b>: Überwachung des Vorstands; Bestellung und Abberufung des Vorstands; der AR wird durch die HV für maximal 4 Jahre bestellt.</li>'
            '<li><b>Hauptversammlung</b>: Versammlung der Aktionäre, eine Stimme pro Aktie; Bestellung des AR, Verwendung des <b>Bilanzgewinns</b>, Auflösung der Gesellschaft.</li></ul>'),
 # ---- Strategiewahl: Überblick der Strategiearten ----
 dict(t='ansoff', vor='<h3>Risiko in der Ansoff-Matrix</h3>',
      block='<h3>Strategiewahl: die Strategiearten im Überblick</h3><div class="tbl-scroll"><table class="t"><tr><th>Gruppe</th><th>Strategien</th></tr>'
            '<tr><td class=rowh>Produkt-Markt-Strategien (Ansoff)</td><td>Marktdurchdringungsstrategie · Marktentwicklungsstrategie · Produktentwicklungsstrategie · Diversifikationsstrategie</td></tr>'
            '<tr><td class=rowh>Wettbewerbsstrategien (Porter)</td><td>Strategie der Kostenführerschaft · Differenzierungsstrategie · Nischenstrategie</td></tr>'
            '<tr><td class=rowh><b>Organisationsstrategien</b></td><td>Unternehmensstrategie (corporate strategy) · <b>Geschäftsbereichsstrategie</b> (business strategy) · <b>Funktionsstrategie</b> (functional strategy)</td></tr>'
            '<tr><td class=rowh><b>Regionale Strategien</b></td><td>lokale · nationale · internationale · globale Strategie</td></tr>'
            '<tr><td class=rowh><b>Entwicklungsstrategien</b></td><td>Wachstumsstrategien · Stabilisierungsstrategien · Desinvestitionsstrategien</td></tr>'
            '<tr><td class=rowh>Strategien mit Bezug zur <b>Eigenständigkeit</b></td><td><b>Autonomiestrategie</b> · <b>Kooperationsstrategie</b> · <b>Integrationsstrategie</b></td></tr></table></div>'),
 # ---- Umweltanalyse: alle Fehleinschätzungen der Folie ----
 dict(t='umweltanalyse', nach='<li>„There is no reason anyone would want a computer in their home.“ (Ken Olsen, Digital Equipment, 1977)</li>',
      block='<li>„Whatever could possibly be invented, has now been invented.“ (Leiter der <b>US-Patentbehörde</b>)</li>'
            '<li>„Nobody wants to watch a box night after night.“ (Daryl Zanuck, CEO von 20th Century Fox, zur TV-Technologie)</li>'
            '<li>„Es gibt bereits über 15 ausländische Automarken auf dem Markt. Da haben die Japaner überhaupt keine Chance mehr.“ (Business Week, 1968)</li>'
            '<li>„640 MB ought to be enough for anybody.“ (Bill Gates, Gründer von Microsoft, 1981)</li>', frage=False),
 # ---- Märkte: Adam Smith vollständig ----
 dict(t='maerkte', alt='Adam Smith nannte das die <b>unsichtbare Hand</b>:',
      neu='Adam Smith nannte das die <b>unsichtbare Hand</b>[[. Seine Begründung: Märkte funktionieren nicht, weil sich Menschen mit Liebe und Gutmütigkeit begegnen. Der Mensch braucht dauernd die Hilfe seiner Mitmenschen und kommt eher zum Ziel, wenn er ihre <b>Eigenliebe</b> zu seinen Gunsten nutzt und zeigt, dass sie ihren eigenen Nutzen davon haben]]:', frage=False),
 # ---- Entscheidungstheorie: Einflussdiagramm ----
 dict(t='et-struktur', nach='<h3>Stufe 1: Strukturierung</h3>',
      block='<p>Die Vorlesung stellt die Vorbereitung als <b>Einflussdiagramm</b> dar: Das Entscheidungsproblem wird in Stufe 1 strukturiert in Zielsystem (Präferenzen) und Entscheidungsfeld (Alternativen, Umwelteinflüsse); in Stufe 2 folgt die Lösungsfindung.</p>'),
]
