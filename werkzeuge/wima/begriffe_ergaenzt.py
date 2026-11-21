"""Fachbegriffe aus den Unterlagen, die auf der Lernseite fehlten oder nur erwähnt waren (Skill /begriffs-check).
Je Eintrag: (Begriff, Suchmuster (Regex), Unterthema, Erklärung). Sie werden Glossar-Einträge (markiert im Text, Karteikarte),
fehlen sie im Text des Unterthemas, erscheinen sie dort unter „Weitere Begriffe“. Fragen dazu: werkzeuge/begriffs_fragen.py."""
B = [
    ('Zahlensysteme', r'Zahlensystem', 'zahlenmengen', 'Die Zahlbereiche ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ: natürliche, ganze, rationale (Brüche, abbrechende oder periodische Dezimalzahlen) und reelle Zahlen (dazu irrationale wie √2, π).'),
    ('Relation', r'Relation', 'funktion', 'Beliebige Zuordnung zwischen Elementen zweier Mengen. Eine Funktion ist eine spezielle Relation: Jedem x aus D wird genau ein y zugeordnet (Zuordnungsvorschrift).'),
    ('Konvergenz (ε-Definition)', r'ε-Kriterium|Konvergenz-Definition|\\varepsilon', 'grenzwert-folge', 'Eine Folge (aₙ) konvergiert gegen a, wenn es zu jedem ε > 0 ein N(ε) gibt, sodass |aₙ − a| < ε für alle n ≥ N(ε). Einfach gesagt: Ab einem Index liegen alle Glieder beliebig nah an a.'),
    ('Grenzübergang', r'Grenzübergang', 'differentialquotient', 'Übergang zum Grenzwert, z. B. h → 0 beim Differentialquotienten: aus der Sekantensteigung wird die Tangentensteigung.'),
    ('Vorzeichenwechsel', r'Vorzeichenwechsel', 'kurvendiskussion', 'Wechselt f′ an einer Stelle das Vorzeichen (+ → −: Hochpunkt, − → +: Tiefpunkt), liegt ein Extremum vor; wechselt f″ das Vorzeichen, ein Wendepunkt.'),
    ('Krümmungsverhalten', r'Krümmung', 'kurvendiskussion', 'f″ > 0: linksgekrümmt (konvex, „Schale“), f″ < 0: rechtsgekrümmt (konkav, „Dach“); am Wendepunkt ändert sich die Krümmung.'),
    ('Umsatzfunktion', r'Umsatzfunktion|Erlösfunktion', 'kostenfunktion', 'U(x) = p · x (bei festem Preis) bzw. U(x) = p(x) · x mit Preis-Absatz-Funktion; G(x) = U(x) − K(x).'),
    ('Snob-Effekt', r'Snob', 'angebot-nachfrage', 'Ausnahme vom fallenden Nachfrageverlauf: Bei manchen Luxusgütern steigt die Nachfrage mit dem Preis, weil der hohe Preis Status signalisiert.'),
]
