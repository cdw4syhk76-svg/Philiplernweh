"""Marketing: Fragen zum eingearbeiteten Folienstoff (ersetzen die Lückentexte, IDs bleiben)."""
from dsl import mc, mm, bl, zu, li, ku, rh

FR = {
    '6bf5f74b': [
        mc('Ein Getränkehändler startet eine witzige Werbekampagne, die bei der Zielgruppe gut ankommt. Ist das automatisch Kundenorientierung?',
           'Nicht unbedingt: Die Werbetreibenden haben sich gut in die Köpfe der Nachfrager versetzt, aber Kundenorientierung heißt, Bedürfnisse und Probleme zur Leitlinie zu machen',
           ['Ja, jede gelungene Marketing-Aktivität ist Kundenorientierung', 'Ja, weil der Umsatz steigt', 'Nein, Werbung hat mit Kunden nichts zu tun'],
           'Kundenorientierung ist schwer zu fassen; ob ein Verhalten Ausdruck besonderer Kundenorientierung ist, ist im Einzelfall Interpretationssache.'),
    ],
    '81e933c8': [
        mm('Was wirkt im Wahrnehmungsmodell (Steffenhagen) auf den Ablauf ein?', [('Inhalte des Langzeitgedächtnisses', True), ('Merkmale der Kontaktsituation', True), ('der Listenpreis des Produkts', False), ('die Anzahl der Wettbewerber', False)],
           'Ergebnis sind die momentanen Resultate eines Reizkontakts.'),
    ],
    '6d58aabc': [
        mc('Assoziationsnetz Milka: Woran ist ein Unternehmen interessiert?', 'Dass das Netz dichter bei den positiven Assoziationen ist (Genuss, Alpen) als bei den negativen (Kalorien, Karies)',
           ['Dass möglichst wenige Assoziationen bestehen', 'Dass nur sprachliche Assoziationen gespeichert sind', 'Dass die Verpackung keine Rolle spielt'],
           'Ein Image umfasst Assoziationen in allen Modalitäten (lila Verpackung, Bruchstellen der Tafel, Alpenlandschaft …), kognitiv und emotional.'),
    ],
    '900d77a6': [
        mm('Welche Theorien erklären im SOR-Denkrahmen, was im Organismus passiert?', [('Wahrnehmungstheorie', True), ('Lern- und Gedächtnistheorie', True), ('Motivationstheorie', True), ('Gravitationsmodell des Handels', False)],
           'Dazu Kognitions-, Entscheidungs- und Persönlichkeitstheorie. Das SR-Paradigma lässt den Organismus als Black Box.'),
    ],
}
