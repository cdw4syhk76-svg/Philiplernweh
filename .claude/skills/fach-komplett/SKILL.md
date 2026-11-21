---
name: fach-komplett
description: Baut ein Fach im LernTool vollständig (neu) – Lernseite übernehmen, Klausurprofil aus Protokollen/Altklausuren/Probeklausur, Fragen mit Klausur-Markierung, große Aufgaben, Karteikarten, Probeklausur-Bogen im Aufbau der echten Klausur, Schreibweise wie auf Papier, Tests, Veröffentlichen. Aufruf: /fach-komplett <fach-id> [neu|nachruesten].
argument-hint: <fach-id> [neu|nachruesten]
---

# /fach-komplett – ein Fach von Anfang bis Ende

Lies zuerst `docs/FACH-ANLEGEN.md` (die verbindliche Schrittliste) und `CLAUDE.md`. **Neuer Kurs** (anderes Studium, alle Inhalte neu):
zuerst `docs/KURS-NEU.md` ganz lesen; es ersetzt die Verweise auf `lernubersicht` und gibt Formate, Zielgrößen und Regeln vor.
Vorbild für Inhalt, Erklärtiefe, Schaubilder und Aufgabenmenge ist immer **Logistik & MaWi** (`inhalte/logistik/` bzw. `muster/inhalte/logistik/`). Arbeite die Schritte 1–9 der Reihe nach ab.
Nach jedem Schritt: `python3 bau.py --test`, Commit (Nachricht nennt Fach und Schritt), Push. Antworten an den Nutzer kurz,
deutsch, Status + Commit-Hash.

## Vorgehen
1. **Bestandsaufnahme**: Was gibt es schon in `inhalte/<fach>/`? Welche Quellen liegen vor (Folien, Übungen, Lösungen,
   Probeklausur, Protokolle; im neuen Kurs alles in `unterlagen/<Fach>/`, siehe `unterlagen/README.md`)? Fehlt etwas Wesentliches
   (z. B. Probeklausur, Übungslösungen), frag den Nutzer **einmal** gesammelt danach und arbeite mit dem Rest weiter.
2. **Klausurprofil** schreiben (`inhalte/<fach>/plan/profil.md`, intern): jede bekannte Klausuraufgabe mit Thema, Typ,
   Punkten, Häufigkeit; daraus Aufbau, Punkteverteilung, Lieblingsthemen, Operatoren, Stil. `mix` in `faecher.json` danach setzen.
3. **Lernseite**: im neuen Kurs direkt hier bauen: `werkzeuge/<fach>/k1.py …` mit `werkzeuge/fachbau/bausteine_de.py`,
   dann `python3 werkzeuge/fachbau/bauen.py <fach>` (siehe `docs/KURS-NEU.md`, Schritt 3–4). Im alten Kurs: mit `/fach-planen`
   und `/fach-bauen` im Repo `lernubersicht` bauen und übernehmen. Bei `nachruesten` nur ergänzen.
4. **Fragen**: alle Klausur- und Übungsfragen als Familien mit `klausur: true`, dazu eigene Fragen für den restlichen Stoff
   (Stufen 1–3). Auswahlfragen mit gleich langen, plausiblen Ablenkern.
5. **Große Aufgaben** (`aufgaben.json`) aus Übungen/Klausuren mit Tipps und Lösungsweg; Zahlen in Python nachrechnen.
6. **Karteikarten** (`karten.json`): jedes Unterthema ≥ 5.
7. **Probeklausur-Bogen** (`klausur.json`): Aufbau 1:1 wie die echte Klausur, je Teil 4–7 Varianten aus Klausur/Übung,
   passende Antwortfelder, Musterlösung mit Formel/Weg/Ergebnis. Bei Rechenfächern per Generator-Skript wie
   `werkzeuge/mathe_klausur.py` (Zahlen werden berechnet, nicht abgetippt).
8. **Prüfen**: Tests, Screenshots (Handy 390 px, Dunkelmodus), Probeklausur und ein Arbeitsblatt auf Klausurniveau ansehen:
   Formeln gesetzt? Brüche als Brüche? Keine Spur der Quellen?
9. **Veröffentlichen**: Push (Vercel), Artifact an dieselbe Adresse, Plan `UMSETZUNGSPLAN.md` aktualisieren.

## Regeln
- Klausur- und Übungsinhalte haben überall Vorrang, nicht nur ihr Stil.
- Nie sichtbar: „Gedächtnisprotokoll“, „GP“, „Altklausur“, Jahreszahlen früherer Klausuren.
- Schreibweise wie auf Papier: `\( … \)`, `\frac`, `\cdot`, `\sum_{i=1}^{n}`, `\begin{pmatrix}`.
- Fremdsprachige Klausur: alles in Klausursprache.
