# Ein Fach komplett bauen (oder neu bauen)

Diese Anleitung beschreibt alle Schritte, mit denen die Fächer im LernTool gebaut wurden. Sie gilt für ein **neues Fach**
und für ein Fach, das **neu gemacht** wird (z. B. Production nach der Überarbeitung der Lernseite).

Kurzbefehl für Claude: **`/fach-komplett <fach-id>`** (Skill in `.claude/skills/fach-komplett/`). Der Skill arbeitet
diese Liste ab, Schritt für Schritt, mit Commit nach jedem Schritt.

Unverhandelbar in jedem Schritt:
- **Klausurnähe vor allem anderen.** Was in früheren Klausuren (Gedächtnisprotokolle, Altklausuren), in der Probeklausur
  und in den Übungen des Dozenten vorkam, wird übernommen, markiert (`klausur: true`) und überall bevorzugt gezogen:
  Mini-Quiz-Auswahl, Endlos-Quiz, Arbeitsblatt (Mittel/Klausurniveau), Übungsklausur, Probeklausur.
- **Keine sichtbare Spur der Quellen.** Nie „Gedächtnisprotokoll“, „GP“, „Altklausur“, „Klausur 2024“, Prüfernamen mit
  Jahr usw. in Texten. Der Bau bricht ab, wenn so etwas in `dist/` landet.
- **Schreibweise wie auf Papier.** Formeln in `\( … \)` (KaTeX), Brüche als echte Brüche, Malpunkt `·`,
  Summen/Produkte mit Grenzen oben und unten, Matrizen als Matrizen. Einfache Fälle (`a ÷ b`, `K/Y`) werden automatisch
  zu Brüchen (`schoen()` in `app/js/klausur.js`).
- Inhalte nie ersatzlos löschen. Fremdsprachige Klausur → Inhalte in Klausursprache.

## Quellen (einmal sammeln)
| Was | Wo |
|---|---|
| Folien, Skript, Übungen, Lösungen, Probeklausur | vom Nutzer; PDFs als Text-Inventar (`python3 plattform/tools/folien_text.py` im alten Repo `lernubersicht`) und Formeln/Tabellen **als Seitenbild lesen** (`pdftoppm -r 75 -png`) |
| Gedächtnisprotokolle, Altklausuren | `lernubersicht/Altklausuren GEdächtnisprotokolle/…` (docx → Text mit python-docx oder `unzip -p x.docx word/document.xml`) |
| Termine, Punkte, Minuten, Kombi-Teile | `inhalte/studium.json` |
| Prüfer, Aufgabenmix | `inhalte/faecher.json` (Registry) |

## Schritte
1. **Registry und Termin**: Fach in `inhalte/faecher.json` (id, Name, Prüfer, Farbe, `mix` = Gewichte der Aufgabenarten
   nach Klausurprofil), Klausur in `inhalte/studium.json` (Datum, `punkte`, `minuten`, Teile mit Gewicht).
2. **Klausurprofil** (in `inhalte/<fach>/plan/profil.md`, nur intern): Aus allen Protokollen, Altklausuren und der
   Probeklausur je Aufgabe festhalten: Thema, Aufgabentyp (Definieren, Aufzählen, Rechnen, Richtig/Falsch-Block, Fall,
   Zeichnen), Punkte, wie oft gekommen. Daraus: Aufbau der Klausur (Aufgaben, Punkte, Reihenfolge), Lieblingsthemen,
   Operatoren („Nennen“, „Erläutern“, „Berechnen“), Stil des Prüfers.
3. **Lernseite** (`inhalte/<fach>/fach.json`, `figuren.js`, `glossar.json`): Kapitel → Unterthemen mit Kern, Merksatz,
   Text, Schaubildern. Vorbild Logistik. Kernthemen (`star`) = die Themen, die laut Profil oft kommen.
4. **Fragen** (`fragen.json`, Familien je Unterthema, Stufen 1–3): Jede Klausur-/Übungsfrage als Familie übernehmen und
   mit `klausur: true` markieren; dazu eigene Fragen zum restlichen Stoff. Auswahlfragen: Ablenker gleich lang und
   plausibel (der Bau meldet, wenn die richtige Antwort zu oft die längste ist; Ziel < 40 %).
5. **Große Aufgaben** (`aufgaben.json`): Übungs- und Klausuraufgaben mit Teilaufgaben a–d, Punkten, zwei Tipps,
   Lösungsweg; Zahlen mit Python nachrechnen. `klausur: true`, wenn aus Klausur/Übung.
6. **Karteikarten** (`karten.json`): je Unterthema ≥ 5 (Aufzählungen, Formeln, Begriffe), reiner Text, Zeilen = Punkte.
7. **Probeklausur-Bogen** (`klausur.json`, für Mathe erzeugt von `werkzeuge/mathe_klausur.py`): Aufbau genau wie die
   echte Klausur (Aufgaben, Teile a/b/c, Punkte, Minuten, Deckblatt-Angaben). Je Teil 4–7 gleichwertige Varianten aus
   Probeklausur, Protokollen und Übungen. Antwortfelder: `zahl`, `menge`, `ausdruck` (Mathe-Feld), `matrix`, `text`
   (Selbstbewertung). Lösung mit Formel, Weg, Ergebnis. Der Bau prüft Punkte und Unterthemen.
8. **Prüfen**: `python3 bau.py --test` (Spuren-Prüfung, Punkte, IDs, Engine, Klicktest, Online), Screenshots Handy und
   Dunkelmodus (`node tests/screenshots.js`), Probeklausur einmal komplett durchklicken.
9. **Veröffentlichen**: Commit + Push (Vercel baut selbst), Artifact an dieselbe Adresse (geänderte Dateien aus `dist/`).

## Wo was gezogen wird (Vorrang für Klausur- und Übungsaufgaben)
| Werkzeug | Vorrang |
|---|---|
| Übungsklausur je Oberthema | Fragen mit `klausur: true` dreifach gewichtet (`klausurAufgaben` in `pruefung.js`) |
| Arbeitsblatt Mittel/Klausurniveau | Probeklausur-Varianten und Klausur-/Übungsaufgaben zuerst (2 : 1 gemischt), Fragen 1 : 1 (`blattZiehen` in `kern.js`) |
| Probeklausur | nur Bogen-Varianten aus Klausuren/Übungen, länger nicht gesehene zuerst (`klausurZiehen`) |
