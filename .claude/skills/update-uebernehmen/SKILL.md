---
name: update-uebernehmen
description: Übernimmt alle Verbesserungen aus Lernweh DBM26A (Handy, Fehler, Fragenmethoden, Endlos, Admin) in diesen Kurs – Patch einspielen, Konflikte lösen, Fragenmethoden je Fach anwenden, neutral formulieren, testen, veröffentlichen. Aufruf: /update-uebernehmen [teil A|B|C|D|E] [fach-id].
argument-hint: [teil] [fach-id]
---

# /update-uebernehmen

Lies `docs/update-2026-11-09/UPDATE.md` ganz und `CLAUDE.md`. Arbeite die Teile A bis E der Reihe nach ab.
Ist ein Teil oder Fach angegeben, nur diesen bzw. dieses.

- Teil A: `git apply -3 docs/update-2026-11-09/plattform.patch`, Konflikte wie beschrieben lösen, eigene Änderungen nie verwerfen.
  Dann `python3 bau.py --test`, Commit „Update aus DBM26A: Plattform“, Push.
- Teil B/C: je Fach die Fragenmethoden; nach jedem Fach Test, Commit, Push. Die Dateien in `vorlagen/` sind nur Muster.
- Teil D gilt durchgehend. Teil E zum Schluss.
- Kein Eintrag in `inhalte/neuigkeiten.json` ohne Freigabe des Nutzers.

Antworten an den Nutzer: kurz, deutsch, Status und Commit-Hash.
