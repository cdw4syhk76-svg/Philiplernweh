# Philip Lernweh · Introduction to English Linguistics (Demo)

Lernwerkzeug im Stil von Lernweh für das Worksheet „Key Concepts in Linguistics“ (JLU Gießen).
Alles auf Englisch (Klausursprache), ein Schalter im Werkzeug-Dock übersetzt die Lernseiten ins Deutsche.

- **Start** · **Lernen** (2 Oberthemen, 9 Unterthemen mit antippbaren Schaubildern) · **Training** (Quiz, Drill, Karteikarten, Arbeitsblatt, Übungs- und Probeklausur)
- Viele Lückentexte im Wortlaut des Arbeitsblatts, Richtig/Falsch mit Korrektur, Aufzählen, Beschriften des Zeichenmodells

## Bauen und testen
```bash
python3 werkzeuge/fachbau/bauen.py ling   # Lernseiten aus werkzeuge/ling/k1.py, k2.py
python3 werkzeuge/ling/fragen.py          # Fragen (danach karten, glossar, aufgaben, klausur .py)
python3 bau.py --test                     # dist/ bauen + Klicktests
node tests/screenshots.js                 # Screenshots Handy/Desktop, hell/dunkel
```
Vercel baut mit `python3 bau.py` und liefert `dist/` aus (siehe `vercel.json`).
