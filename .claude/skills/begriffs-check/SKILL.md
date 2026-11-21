---
name: begriffs-check
description: Prüft, ob JEDER Fachbegriff aus Folien, Skript und Übungen auf der Lernseite ERKLÄRT wird (nicht nur erwähnt), und ergänzt fehlende Erklärungen mit Glossar, Lernseite und Fragen. Ziel – in der Klausur taucht kein Begriff auf, den man nie gehört hat, und keine Definition wird verlangt, die nirgends abgebildet war. Aufruf: /begriffs-check <fach-id|alle>
argument-hint: <fach-id|alle>
---

# /begriffs-check – kein Begriff, den man nie gehört hat

**Ziel des Nutzers:** Jedes Thema, das drankommen könnte, ist behandelt. Es darf nicht passieren, dass man in der Klausur einen Begriff
liest, den man nie gehört hat, oder eine Definition schreiben muss, die nirgends abgebildet war, aber auf den Folien stand.
**Beispiele** werden nicht 1:1 übernommen: nur die, die beim Verstehen wirklich helfen (Ermessen der KI). Begriffe und Zusammenhänge dagegen vollständig.

Vorher lesen: `CLAUDE.md`, `docs/KURS-NEU.md` (Schreibregeln, keine Quellenspur). Durchgestrichenes (`inhalte/<fach>/plan/folien_weg.json`,
Skill `/folien-abgleich`) ist kein Stoff.

## Werkzeuge
| Befehl | Zweck |
|---|---|
| `python3 werkzeuge/begriffs_check.py <fach>` | Kandidaten aus den Unterlagen (Definitionssätze „versteht man / heißt / bezeichnet / ist ein…“, Begriffe am Anfang von Aufzählungspunkten, Abkürzungen, Bindestrich-Komposita, lange Substantive) mit Status **FEHLT** (nirgends auf der Lernseite), **ERWÄHNT** (kommt vor, aber ohne Erklärung) oder **ERKLÄRT** (fett, Glossar, Karteikarte, Tabellenzelle, Definitionssatz). Spalte F = kommt in Fragen vor, D = stand in Definitionsnähe |
| `… --alle` | auch die erklärten anzeigen |
| `werkzeuge/<fach>/begriffe_ergaenzt.py` | Liste `B = [(Begriff, Suchmuster, Unterthema, Erklärung)]` der ergänzten Begriffe |
| `inhalte/<fach>/plan/begriffe_ok.json` | geprüfte Treffer, die kein Fachbegriff sind (Überschrift, Beispieldaten, Name, Quelle) oder als Schreibvariante schon erklärt sind |
| `python3 werkzeuge/begriffs_fragen.py <fach>` | Fragen zu den ergänzten Begriffen (Familie `…:bg-begriffe` je Unterthema: „Was bedeutet …?“, „Wie heißt der Begriff …?“, Verknüpfen) |
| `bash werkzeuge/fach_erzeugen.sh <fach>` | ganze Erzeugungskette (Glossar → Lernseite → Fragen/Karten/Aufgaben → Begriffsfragen → Generatoren); `--nur-fach` für Fächer, deren Bestand die allgemeinen Generatoren umbauen (hier: igt) |

**So wirkt ein Eintrag in `begriffe_ergaenzt.py`:** Er wird Glossarbegriff (im Text markiert, mit Erklärung beim Antippen, eigene Karteikarte,
im Nachschlagen). Kommt der Begriff im Text seines Unterthemas noch gar nicht vor, erscheint er dort automatisch im Block **„Weitere Begriffe“**
(`werkzeuge/fachbau/bauen.py`). Dazu entstehen Fragen.

## Ablauf je Fach
1. `python3 werkzeuge/begriffs_check.py <fach>` – Liste ansehen (FEHLT zuerst, dann ERWÄHNT).
2. **Jeden Treffer von Hand beurteilen** (die Erkennung ist eine Heuristik):
   - echter Fachbegriff, der fehlt oder nur erwähnt ist → Eintrag in `begriffe_ergaenzt.py`: kurze, einfache Erklärung im Wortlaut der Folie
     (ein bis zwei Sätze, „Einfach gesagt“-Niveau), richtiges Unterthema (dessen `src` die Folie nennt), Suchmuster, das Schreibvarianten trifft.
     Ist der Begriff zentral (Definition/Aufzählung, die abgefragt werden kann), zusätzlich im Text des Unterthemas erklären (`werkzeuge/<fach>/kN.py`).
   - Schreibvariante eines schon erklärten Begriffs, Überschrift, Name, Quelle, Beispieldaten, Notiz → bleibt für `begriffe_ok.json`.
   - Zusammenhang statt Begriff fehlt (z. B. „A führt zu B“) → im Text des Unterthemas ergänzen und eine Frage dazu schreiben.
3. Nach der Sichtung die übrigen Treffer als geprüft eintragen (Schlüssel = Begriff wie in der Liste, Wert = Grund).
4. **Zusätzlich von Hand:** Die Folien jedes Kapitels einmal als Bild ansehen (`python3 werkzeuge/folien_bogen.py <fach> <ordner>`) und auf
   Begriffe achten, die die Heuristik nicht findet: kurze Fachwörter in Grafiken, handschriftliche Begriffe der Mitschrift, Fachwörter in Tabellen.
5. `bash werkzeuge/fach_erzeugen.sh <fach>` (igt: `--nur-fach`), dann `python3 bau.py --test` (grün, keine weggefallenen IDs außer bewusst
   entfernten), erneut `begriffs_check.py` → **0 FEHLT, 0 ERWÄHNT**.
6. Commit („<fach> Begriffs-Check: …“), Push, Artifact an die Adresse aus `UMSETZUNGSPLAN.md`.

## Regeln
- Erklärungen sachlich richtig und im Sinne der Vorlesung; im Zweifel den Folientext nehmen. Keine Quellenspur (keine „Gedächtnisprotokoll“-Wörter).
- Fremdsprachige Fächer (`"englisch": true`): Erklärung in Klausursprache mit deutscher Übersetzung in Klammern, wie die übrigen Glossareinträge.
- Nie bestehende Fragen-IDs ändern. Die `bg-`Familien werden bei jedem Lauf neu erzeugt (IDs bleiben je Unterthema gleich).
- Antwort an den Nutzer: je Fach Zahl der ergänzten Begriffe und die wichtigsten, Commit-Hash.
