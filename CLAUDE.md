# Philip Lernweh – Arbeitsregeln für Claude

**Dieses Repo ist Lernweh als Demo für Philip: ein Fach „Introduction to English Linguistics“ (JLU Gießen), Englisch mit Schalter auf Deutsch.** Technik und Stil kommen aus Litschlernweh (Vorbild für das zweisprachige Fach: Intercultural Management dort). Quelle: `unterlagen/Linguistics/` (Worksheet „Key Concepts in Linguistics“). Fach-ID `ling`, Skripte in `werkzeuge/ling/`.
**Zuerst `docs/KURS-NEU.md` ganz lesen** (Handbuch: Ablauf, Formate, Zielgrößen, Regeln). Vorbild für alles Inhaltliche: Fach **Logistik & MaWi**.
Unterlagen des Nutzers liegen in `unterlagen/<Fach>/`. Plan und Stand: `UMSETZUNGSPLAN.md`.
Antworten an den Nutzer: kurz, deutsch, Status + Commit-Hash.
**Website ohne Login** (Demo): `semester.login: false`, in Vercel keine Umgebungsvariablen. Jeder Push auf `main` baut die Website neu.
**Nie** an Adressen oder Repos anderer Kurse veröffentlichen (`LernTool`, `litschlernweh`).

## Prinzipien (vom Nutzer festgelegt)
- **Werkzeug, kein Lernplan.** Drei Bereiche: Heute · Lernen · Sandbox. Keine Ampel, kein Tagesplan, keine Strafen, keine Statistik-Spielereien.
- Neue Schaltflächen nur, wenn nötig, vom Typ passend und nicht verwirrend.
- Prozent nur aus Übungsklausur (je Oberthema) und Refresh. Hierarchie: Fach → Oberthema (Kapitel) → Unterthema (Thema).
- Inhalte nie ersatzlos löschen. Die alten Fächer sind hier nicht enthalten (Vorbilder in `litschlernweh`).
- Hell und Dunkel: der Dunkelmodus soll so bleiben, wie er ist. Farben nur über Tokens in `app/css/app.css`.
- Keine Mathe-Videos.

## Befehle
```
python3 bau.py --test        bauen + Klicktest (muss vor jedem Commit grün sein)
node tests/screenshots.js    Screenshots Desktop/Handy/hell/dunkel nach tests/bilder/ (Überlauf und JS-Fehler werden gemeldet)
```

## Regeln
- Inhalte stehen in `inhalte/`; nie generierte Dateien in `dist/` bearbeiten. Große JSON-Dateien gezielt lesen (grep, python), nicht ganz.
- Schaubild-Skripte (`inhalte/<fach>/figuren.js`) laufen nach jedem Seitenwechsel; jede ausführende Anweisung wird beim Bauen abgesichert.
- Quiz-Klassen heißen `.qz` (nicht `.q`, das gehört den alten Lernseiten-Skripten).
- Veröffentlichen: beim ersten Mal ein NEUES Artifact anlegen, die Adresse in `UMSETZUNGSPLAN.md` eintragen, danach immer an diese Adresse; alle Dateien aus `dist/` mitschicken.
- Ein Fach komplett bauen oder neu bauen: `docs/FACH-ANLEGEN.md`, Kurzbefehl `/fach-komplett <fach-id> [neu|nachruesten]`.
- **Meldungen der Lernenden** (⚑ Melden): nie blind umsetzen – erst prüfen, ob es stimmt und ob es schon behoben ist; Kurzbefehl `/meldungen-pruefen`.
- **Update aus Lernweh DBM26A** (Handy, Fehler, Fragenmethoden, Endlos, Admin): `docs/update-2026-11-09/UPDATE.md`, Kurzbefehl `/update-uebernehmen`.
- **Lernweh für einen neuen Kurs** (andere Fächer, alle Inhalte neu, gleicher Stil): `docs/KURS-NEU.md`. Vorbild ist Logistik & MaWi.
