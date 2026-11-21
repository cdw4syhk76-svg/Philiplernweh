"""ABWL: Fragen zum eingearbeiteten Folienstoff (ersetzen die Lückentexte, IDs bleiben). Klausur: Single Choice und Rechnen."""
from dsl import mc, mm, bl, zu, li, ku, rh

FR = {
    '962c22bc': [
        zu('Welches Organ der AG ist zuständig?', ['Vorstand', 'Aufsichtsrat', 'Hauptversammlung'],
           [('erstellt den Jahresabschluss', 0), ('bestellt und beruft den Vorstand ab', 1), ('beschließt über die Verwendung des Bilanzgewinns', 2),
            ('leitet die Gesellschaft in eigener Verantwortung', 0), ('bestellt den Aufsichtsrat', 2), ('überwacht den Vorstand', 1)],
           'Vorstand leitet, Aufsichtsrat kontrolliert, Hauptversammlung (eine Stimme pro Aktie) bestellt den AR und entscheidet über Bilanzgewinn und Auflösung.'),
        mc('Für wie lange wird der Vorstand einer AG höchstens bestellt?', 'Maximal 5 Jahre (durch den AR), Wiederwahl möglich',
           ['Maximal 4 Jahre (durch die HV)', 'Unbefristet', 'Maximal 1 Jahr'],
           'Der AR wird von der HV für maximal 4 Jahre bestellt, der Vorstand vom AR für maximal 5 Jahre.'),
    ],
    'ca59f063': [
        zu('Zu welcher Gruppe gehört die Strategie?', ['Organisationsstrategie', 'Entwicklungsstrategie', 'Eigenständigkeit'],
           [('Geschäftsbereichsstrategie (business strategy)', 0), ('Desinvestitionsstrategie', 1), ('Kooperationsstrategie', 2),
            ('Funktionsstrategie (functional strategy)', 0), ('Wachstumsstrategie', 1), ('Integrationsstrategie', 2)],
           'Organisationsstrategien nach Ebene (Unternehmen, Geschäftsbereich, Funktion); Entwicklungsstrategien nach Richtung; Eigenständigkeit: autonom, kooperativ, integriert.'),
        mc('Welche Strategie ist eine Produkt-Markt-Strategie nach Ansoff?', 'Marktentwicklungsstrategie', ['Nischenstrategie', 'Globale Strategie', 'Autonomiestrategie'],
           'Nischenstrategie ist eine Wettbewerbsstrategie (Porter), globale Strategie eine regionale, Autonomie eine Strategie mit Bezug zur Eigenständigkeit.'),
    ],
    'cd1b6af1': [
        mc('Was gehört im Einflussdiagramm zum Entscheidungsfeld?', 'Alternativen und Umwelteinflüsse', ['Präferenzen und Ziele', 'Nur die Umwelteinflüsse', 'Die Lösungsfindung'],
           'Stufe 1 strukturiert das Problem in Zielsystem (Präferenzen) und Entscheidungsfeld (Alternativen, Umwelteinflüsse); Stufe 2 ist die Lösungsfindung.'),
    ],
}
