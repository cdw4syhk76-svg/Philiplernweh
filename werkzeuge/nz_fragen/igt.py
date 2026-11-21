"""Internationale Geschäftstätigkeit: Fragen zum eingearbeiteten Folienstoff (ersetzen die Lückentexte, IDs bleiben).
Klausur: Single Choice mit vier Möglichkeiten – darum vor allem Auswahlfragen."""
from dsl import mc, mm, bl, zu, li, ku, rh

FR = {
    '74c8e3e2': [
        mc('Was ist der Ausgangspunkt der Stellenbildung?', 'Der Gesamtkomplex der Leistungserstellung und -verwertung, zerlegt in Elementaraufgaben',
           ['Die Zahl der vorhandenen Mitarbeiter', 'Die Führungsspanne des Vorstands', 'Das Organigramm der Konkurrenz'],
           'Erst wird der Gesamtkomplex der Leistungserstellung und -verwertung in Elementaraufgaben zerlegt; diese werden zu Stellen gebündelt, Stellen zu Abteilungen.'),
        rh('Bringen Sie die Schritte der Organisationsbildung in die richtige Reihenfolge.',
           ['Gesamtkomplex der Leistungserstellung und -verwertung', 'Zerlegung in Elementaraufgaben', 'Stellenbildung', 'Abteilungsbildung'],
           'Vom Ganzen zum Kleinsten und wieder zusammen: Aufgaben zerlegen, zu Stellen bündeln, Stellen zu Abteilungen.'),
    ],
    '9b4d324f': [
        mc('Ein Unternehmen spürt starken Druck zur weltweiten Vereinheitlichung und zugleich starke unterschiedliche lokale Anforderungen. Welcher Typ passt?',
           'Transnational', ['International', 'Multinational', 'Global'],
           'Beide Kräfte hoch (Forces for global integration und Forces for local responsiveness) = transnational.'),
        zu('Ordnen Sie die Typen der Matrix zu.', ['global integration hoch', 'global integration schwach'],
           [('Global (keine local responsiveness nötig)', 0), ('Transnational (beide Kräfte hoch)', 0), ('International (beide Kräfte schwach)', 1), ('Multinational (local responsiveness hoch)', 1)],
           'Senkrechte Achse: Forces for global integration; waagerechte Achse: Forces for local responsiveness.'),
        mc('Wie heißen die zwei Achsen, mit denen die Vorlesung die vier Typen einordnet?', 'Forces for global integration und Forces for local responsiveness',
           ['Marktgröße und Wachstum', 'Kosten und Qualität', 'Adaptation und Arbitrage'],
           'Global integration = Druck zur Vereinheitlichung; local responsiveness = Druck zur Anpassung an lokale Anforderungen.'),
    ],
}
