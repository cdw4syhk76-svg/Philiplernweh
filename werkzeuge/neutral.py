"""Formulierungen neutral halten: Keine sichtbare Aussage darf verraten, woher das Wissen über frühere Klausuren stammt.
Prüfernamen nur als Dozent/Folien/Übungsblätter, nicht mit „verlangt gern / fragt / Klausur von …“.
Wendet die Ersetzungen auf inhalte/**/*.json und die Fragen-Generatoren an. Wiederholbar. Aufruf: python3 werkzeuge/neutral.py"""
import re, pathlib
W = pathlib.Path(__file__).parent; IN = W.parent / 'inhalte'
ERSETZ = [
    # Kurs WIN26B: keine Aussagen über frühere Klausuren
    (r'Erste Aufgabe in jeder bekannten Klausur:', 'Typische erste Aufgabe:'),
    (r'Zwei Ableitungen kamen in jeder bekannten Klausur, typisch', 'Typisch sind zwei Ableitungen,'),
    (r'kam in allen bekannten Klausuren als erste Aufgabe', 'ist eine typische erste Aufgabe'),
    (r'Diese Aufgabe kam in jeder bekannten Klausur\.', 'Diese Aufgabe ist sehr häufig gefragt.'),
    (r'Kam in jeder bekannten Klausur\.', 'Sehr häufig gefragt.'),
    (r'In jeder bekannten Klausur:', 'Sehr häufig gefragt:'),
    (r'kam in jeder bekannten Klausur', 'ist sehr häufig gefragt'),
    (r'In beiden bekannten Klausuren gefragt:', 'Häufig gefragt:'),
    (r'In beiden bekannten Klausuren \(Glühweinstand\) und im Folienbeispiel', 'Typisch in Klausuren (z. B. Glühweinstand) und im Folienbeispiel'),
    (r'kam in mehreren Klausuren', 'wird häufig gefragt'),
    (r'\(kam in Klausuren\)', '(häufig gefragt)'),
    (r'kam in Klausuren', 'wird häufig gefragt'),
    (r'kam in einer Klausur', 'ist eine typische Klausuraufgabe'),
    (r'Opportunitätskosten kamen in einer Klausur gleich fünfmal vor, meist', 'Opportunitätskosten sind sehr häufig gefragt, oft'),
    (r'Meier-Block: Welche Aussagen sind richtig\?', '4er-Block: Welche Aussagen sind richtig?'),
    (r' \(Meier-Block\)', ' (4er-Block)'),
    (r' \(Meier-Klausur\)', ''),
    (r'(?:Wannenwetsch|Stein) verlangt oft ([^<"]+?) Punkte', r'Typisch in Wirtschaftsklausuren: \1 Punkte'),
    (r'Wannenwetsch verlangt die ABC-Analyse mit 5–6', 'Typisch für Logistik-Klausuren ist die ABC-Analyse mit 5–6'),
    (r'In Logistik \(Wannenwetsch\) wird die deutsche Form gefragt', 'In Logistik lernst du die deutsche Form'),
    (r'Logistics \(Wannenwetsch\) asks the German version', 'In Logistics you learn the German version'),
    (r'Meier lässt die Formel auch rückwärts rechnen:', 'Typische Variante in BWL-Klausuren: die Formel rückwärts rechnen:'),
    (r'Meier stellt das gern als Richtig-falsch-Aussage', 'In BWL-Klausuren steht das oft als Richtig-falsch-Aussage'),
    (r'Diese Unterscheidung fragt Meier gern als Richtig-falsch-Aussage ab\.', 'Diese Unterscheidung ist eine typische Richtig-falsch-Aussage in BWL-Klausuren.'),
    (r'Meier-Variante:', 'Klausurvariante:'),
    (r'exam style \(Prof\. Schief, calculation task\)', 'exam style (calculation task)'),
    (r'\(Schief exam style\)', '(exam style)'),
    (r'\(Schief-Stil\)', '(Klausurstil)'),
    (r'\(exam every year\)', '(typical exam question)'),
    (r'Wird gern gefragt\.', 'Typische Klausurfrage.'),
    (r'Zusatz: not in Schief’s exam; the German Andler/safety stock calculations are asked in Logistics\.', 'Zusatz: not part of this module’s calculations; the German Andler/safety stock calculations belong to Logistics.'),
    (r'Zusatz: nicht in Schiefs Klausur; die deutschen Andler- und Sicherheitsbestand-Rechnungen kommen in Logistik\.', 'Zusatz: gehört hier nicht zu den Rechnungen; die deutschen Andler- und Sicherheitsbestand-Rechnungen gehören zu Logistik.'),
]
n = 0
for p in list(IN.rglob('*.json')) + list(W.rglob('*.py')) + list(W.rglob('*.json')):
    if 'plan' in p.parts or p.name == 'neutral.py': continue
    s = p.read_text(encoding='utf-8'); t = s
    for a, b in ERSETZ: t = re.sub(a, b, t)
    if t != s: p.write_text(t, encoding='utf-8'); n += 1; print('geändert:', p.relative_to(W.parent))
print(n, 'Dateien')
