---
name: folien-abgleich
description: Gleicht ein Fach Folie für Folie mit den Unterlagen ab (Lernseite, Fragen, Karten) und schließt jede Lücke – ohne Fehlertoleranz. Durchgestrichenes bleibt weg. Aufruf: /folien-abgleich <fach-id|alle> [kapitel kN]
argument-hint: <fach-id|alle> [kN]
---

# /folien-abgleich – jede Folie muss drin sein

Regel des Nutzers: **Alles, was in den Folien nicht durchgestrichen ist, muss auf der Lernseite stehen, und es muss Fragen dazu geben.**
Durchgestrichen = Folie mit diagonalem Strich, Folie in Klammern, „Back-Up“-Folien mit Strich, einzelne durchgestrichene Zeilen.
Das bleibt weg (oder höchstens als `zusatz(...)` „Zusatz · kommt nicht dran“). Notizen der Mitschrift auf den Folien gehören dazu
(z. B. Beispiele, „wichtig“), außer sie sagen ausdrücklich „geskippt“ **und** die Folie ist durchgestrichen.

Lies vorher `CLAUDE.md` und `docs/KURS-NEU.md` (Bausteine, Formate, Schreibregeln, keine Quellenspur).

## Werkzeuge
| Befehl | Zweck |
|---|---|
| `python3 werkzeuge/folien_abgleich.py <fach>` | jede Folienzeile gegen das Unterthema, dessen `src` die Folie nennt (Lernseite **L** = Text, Karten, Glossar; Fragen **F** = Fragen, Aufgaben, Probeklausur). Folien ohne Unterthema: „KEIN UNTERTHEMA“ |
| `… --seiten 160-180` | nur ein Bereich (= ein Kapitel) |
| `… --versatz N` | wenn PDF-Seite ≠ Foliennummer (IKM: Skriptseite) |
| `python3 werkzeuge/folien_bogen.py <fach> <ordner>` | Übersichtsbögen (24 Folien je Bild) zum Finden durchgestrichener Folien |
| `python3 werkzeuge/folien_bogen.py <fach> <ordner> --seite N --dpi 90` | eine Folie groß (durchgestrichene Zeilen, handschriftliche Notizen) |

Die Textfassung der Folien liegt in `inhalte/<fach>/plan/quellen/`. Handschriftliche Notizen stehen **nicht** im Text: Folien mit
Handschrift groß ansehen.

## Ablauf je Fach
1. **Bögen ansehen**, alle durchgestrichenen Folien in `inhalte/<fach>/plan/folien_weg.json` eintragen (`{"165": "Grund"}`).
   Nur echte Striche/Klammern zählen, nicht „sieht unwichtig aus“.
2. **Kapitel für Kapitel** `folien_abgleich.py <fach> --seiten a-b` laufen lassen. Jede gemeldete Zeile prüfen:
   - nur Füllwörter/Layout-Bruchstücke → ok
   - Inhalt fehlt → in `werkzeuge/<fach>/kN.py` beim passenden Unterthema ergänzen (Folienwortlaut erhalten, einfach erklärt,
     `src` um die Folie erweitern), Schaubild der Folie originalgetreu nachzeichnen, wenn es eines gibt
   - Folie ohne Unterthema → passendem Unterthema zuordnen (`src` ergänzen) oder neues Unterthema anlegen
3. **Fragen**: Zu jedem ergänzten Inhalt mindestens eine Frage (Familie im passenden `werkzeuge/<fach>/fragen_*.py` oder `fragen_neu.json`
   über das Fach-Skript) und eine Karteikarte (`karten.py`). Fallstudien/Übungsfolien als große Aufgabe (`aufgaben.py`, Zahlen in Python).
   IDs vorhandener Familien nie ändern.
4. Bauen: `python3 werkzeuge/fachbau/bauen.py <fach>`, Fragen/Karten/Aufgaben-Skripte des Fachs, dann `python3 bau.py --test` (grün).
5. Erneut `folien_abgleich.py` laufen lassen, bis jede gemeldete Zeile geklärt ist. Ergebnis je Kapitel in
   `inhalte/<fach>/plan/folien_abgleich.md` festhalten (Kapitel · Folien · ergänzt · weggelassen weil durchgestrichen).
6. Commit je Fach („<fach> Folienabgleich: …“), Push, Artifact an die Adresse aus `UMSETZUNGSPLAN.md` (alle Dateien aus `dist/`).

Danach immer **`/begriffs-check <fach>`**: Der Folienabgleich findet fehlende Inhalte, der Begriffs-Check stellt sicher, dass jeder Fachbegriff erklärt (nicht nur erwähnt) ist. Beispiele nur übernehmen, wenn sie beim Verstehen helfen.

Antwort an den Nutzer: kurz, deutsch, je Fach was ergänzt wurde, Commit-Hash.
