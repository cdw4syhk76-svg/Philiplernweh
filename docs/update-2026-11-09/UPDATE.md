# Update aus Lernweh DBM26A (Stand 09.11.2026) übernehmen

Alles, was in Lernweh DBM26A (Repo `LernTool`) seit der Abspaltung dieses Repos verbessert wurde: Handy, Fehler,
Fragenmethoden, Endlos, Admin. **Ein Befehl:** `/update-uebernehmen` (Skill in `.claude/skills/update-uebernehmen/`)
arbeitet diese Datei von oben nach unten ab.

Bestandteile dieses Ordners:
- `plattform.patch`: Code-Änderungen an `app/`, `api/`, `middleware.js`, `bau.py`, `tests/` und an den
  allgemeinen Werkzeugen in `werkzeuge/`. Erstellt als `git diff 8acad77..4d2eb24` aus LernTool; 8acad77 ist der Stand,
  von dem dieses Repo kopiert wurde.
- `vorlagen/`: fachbezogene Generatoren aus DBM26A als **Muster** (nicht ausführen, Inhalte gehören zum alten Kurs).
  Darin `verstehen.py`, `zeichnen.py`, `klausurpunkte.py` und `klausurstil_marketing.json`.

Regeln wie immer: `python3 bau.py --test` grün vor jedem Commit, kleine Commits, Inhalte nie ersatzlos löschen,
Dunkelmodus unverändert, Farben nur über Tokens.

---

## Teil A · Plattform-Code (Patch)

```bash
git apply -3 docs/update-2026-11-09/plattform.patch
```

Erwartet sind **4 kleine Konflikte**. So löst du sie:
1. **`app/js/sync.js`, `syncStart()`:** beide Zeilen behalten. Zuerst die eigene Zeile (`semester.login === false` → return),
   dann die neue Zeile (`if (typeof GEIST !== 'undefined' && GEIST) return;`).
2. **`app/js/kern.js`, `app/js/ansichten.js`:** Die Änderungen dieses Repos zusammenführen, z. B. Probeklausur anteilig,
   Hochzeichen, Sterne. Nichts Eigenes verwerfen.
3. **`tests/t_engine.js`:** beide Tests behalten.

Danach `python3 bau.py --test`. Schlägt der Spuren-Check an, siehe Teil D.

### Was der Patch enthält

**Handy (nur unter 600 px):**
- Neue Datei `app/js/handy.js`, in `bau.py` eingetragen. In „Ganz erklären“ sind die Abschnitte zuklappbar:
  der erste ist offen, der Rest zu. Ein Sprung aus dem Inhaltsverzeichnis öffnet den Abschnitt.
- CSS-Block „Handy-Prototyp“:
  - eine Spalte; Fächer als kompakte Zeilen mit Ring, die beim Antippen ihre Oberthemen aufklappen
  - die Statistik-Pillen scrollen waagrecht
  - die Werkzeugleiste der Lernseite sitzt oben fest statt schwebend
  - Training-Werkzeuge als kleine Kacheln, engere Abstände
- Abprüfen:
  - Die Oberthemen-Liste ist wieder lesbar (weiße Schrift auf Weiß behoben).
  - Der Prüfen-Bereich ist schlanker.
  - Akzentfarbe statt Gelb.
  - „Ganze Klausur prüfen“ ist eine kompakte Pille mit Pfeil.

**Fehler behoben:**
- **Endlos-Quiz wiederholte Fragen** nach 9–10 Fragen. Ursachen: Wichtiges wurde als Kopie mehrfach in den Stapel gelegt,
  die Leiter zog immer dieselben Klausurfragen, und die Gesehen-Liste wurde je Runde geleert.
  Jetzt gilt: Jede Frage (Familie + Variante) kommt erst wieder, wenn alle anderen der Auswahl dran waren.
  Test in `tests/t_engine.js` (80 Ziehungen, 0 Wiederholungen).
- **„Unsicher“ ließ sich nicht aufheben.** Jetzt schaltet ein erneuter Klick um.
  `S.unsicher[key] = {t, alt}` merkt den Stand davor, `G.sicher(key)` stellt ihn wieder her.
  Was vorher schon unsicher war, bleibt unsicher; was seitdem geübt wurde, bleibt geübt.
- **„Finde den Fehler“:** Die Antwort „Stimmt so“ war erratbar und wurde entfernt.
  Das Werkzeug dafür ist `werkzeuge/fehler_fix.py`; es entfernt die Option in allen Fächern.
- **Hilfe in der leichten Klausurform stand sofort in der Aufgabe** („Hilfe: 6 Punkte, Anfänge: R … · H …“).
  Jetzt erscheint sie erst auf Knopfdruck: im Quiz über den Knopf „Hilfe“, im Arbeitsblatt hinter Rettungsring 1.
  Mit Hilfe gelöst = höchstens Stufe 3, nie Stufe 4. Dafür übergibt `G.antwort(id, ok, {hilfe: true})` die Hilfe,
  auch Rettungsring 1 und 2 zählen. Die Lösung ansehen zählt nicht als Hilfe.
- Ein Fehler beim Laden der Startseite (TDZ) ist behoben: Funktionen, die beim ersten `render()` gebraucht werden,
  sind Funktionsdeklarationen und keine `const`.

**Lernen und Üben:**
- **Suche:** Volltext in allen Lernseiten, auch mit gleichbedeutenden Wörtern (z. B. Determinanten ↔ Bestimmungsgrößen).
- **Nachschlagen überall:** Nach jeder Quizantwort gibt es „Im Text nachschlagen“, im Arbeitsblatt jederzeit
  (`window.LT_nachschlagen`). Nach jeder Frage steht „Zum Thema →“.
- **Endlos-Quiz** (`endlos()` in `kern.js`):
  - Es mischt Fragearten (nicht dreimal dieselbe Art, nicht zweimal MC hintereinander) und meidet lange Auswahlantworten.
  - Wichtiges und lange nicht Gesehenes kommt zuerst, aber ohne Kopien.
  - **Leiter je wichtigem Punkt:** 0 erkennen → 1 verstehen → 2 Klausurform mit Hilfe → 3 Klausurform.
  - **Nach einem Fehler:** eine Stufe zurück, zuerst eine Verständnisfrage, dieselbe Frage genau einmal nach etwa 8 anderen
    (Abzeichen „nochmal“).
  - Übrige Unterthemen: etwa jede dritte Frage im Klausurstil.
- **Arbeitsblatt:**
  - Einfach und Mittel: Klausurstil zu Übung 2 : 1, Wichtiges zuerst; Übungsfragen nur in Formen, die die Klausur auch hat.
  - Einfach: Klausuraufgaben in leichter Form mit Hilfe.
  - Klausurniveau: nur Klausur- und Übungsaufgaben.
- **Definitions-Drill:** Tiefe je Fach über `faecher.json` → `tiefe` (1–3, Standard 3); Karten mit `kr: 1` sind klausurrelevant.
- **Wichtig:**
  - Abzeichen „Wichtig“ an Fragen, Aufgaben und Unterthemen.
  - Schalter „Nur Wichtiges“ in der Auswahl aller Werkzeuge, gemerkt in `S.einst.wichtig`.
  - Die Daten kommen aus `inhalte/<fach>/wichtig.json`, erzeugt von `werkzeuge/wichtig.py` (siehe Teil B).
- **Neue Frageart „Fehler im Rechenweg antippen“:** `mc` mit `weg: 1`. Die Optionen sind die Schritte eines Rechenwegs,
  richtig ist der fehlerhafte Schritt. Darstellung `ol.q-weg`, Lösung „Der Fehler steckt in Schritt n“.
- **Zeichenaufgaben:** `rev` mit `zeichnen: 1`, Musterskizze (`bild`) und Checkliste (`pk`). Vorlage: `vorlagen/zeichnen.py`.

**Startseite:** Neuigkeiten als **kleine Kachel „Neu“ oben rechts** (am Handy unter dem „?“).
- Sie klappt kurz auf, wenn es Ungelesenes gibt oder die Sitzung beginnt, und schließt nach 6 s.
- „Alle Neuigkeiten“ öffnet die Liste.
- Die Einträge stehen in `inhalte/neuigkeiten.json` (`{"eintraege":[{"id":"2026-11-09-1","datum":"2026-11-09","art":"neu|besser|behoben","titel":"…","text":"…"}]}`).
- **Nur eintragen, was der Nutzer freigibt.** Ohne Datei bleibt die Kachel weg.

**Admin-Bereich (`app/admin.html`, `api/admin.mjs`, `api/_auswertung.mjs`, `middleware.js`):**
- Reiter **Auswertung** und **Codes**. Links: „Alle (Durchschnitt)“ und jede Person mit **Namen**.
  Der Name kommt aus dem Namen in der App, sonst aus der Notiz zum Code, sonst „Person n“.
- Zu jeder Person:
  - „gerade aktiv“ bzw. „online vor X min“
  - Kennzahlen, Lernzeit der letzten 30 Tage, Prüfungsreife je Fach
  - Werkzeuge, „Wo es hakt“, gemeldete Fehler
- **Durchschnitt:** gleiche Kennzahlen, Vergleichstabelle, schwierigste Fragen, Übungsklausuren je Oberthema, alle Meldungen.
- **Geist-Ansicht:** „Als Geist ansehen“ öffnet die App mit dem Lernstand der Person, nur zum Ansehen.
  Es wird nichts gespeichert und nichts abgeglichen; der eigene Lernstand bleibt unberührt.
  Dafür sorgt ein Cookie `lt_geist` für 2 Stunden, `middleware.js` lässt es zu.
- Die App zählt Nutzung je Tag in `S.nutzung` (Besuche, aktive Minuten, Antworten, richtig, je Werkzeug).
  Eine Minute zählt, solange der Tab sichtbar ist und es in den letzten 5 Minuten eine Aktion gab (auch Scrollen).
  Gespeichert wird alle 2 Minuten und beim Verlassen des Tabs; daraus entsteht „gerade aktiv“.
- Die Auswertung schätzt die Lernzeit zusätzlich aus Zeitstempeln (Antworten, Prüfungen, Unsicher, Meldungen),
  rückwirkend und für ältere App-Stände; je Tag zählt der größere Wert. Tage nach deutscher Ortszeit.
- Gilt nur mit Online-Version und Login-Codes (`semester.login: true`). Ohne Login sind Admin und Geist ohne Wirkung.

**Bau (`bau.py`):**
- Der Index enthält `neu`, Fach-`tiefe`, Unterthema `w` und Familie `w`/`p`.
- Karten, Glossar, Aufgaben und Probeklausur-Varianten tragen `w`.
- Neuer **Spuren-Check:** Im gebauten `dist/` darf kein Hinweis auf Herkunft oder Prüfervorlieben stehen (siehe Teil D).

---

## Teil B · Fragenmethoden (je Fach anwenden, in dieser Reihenfolge)

Die Werkzeuge kommen mit dem Patch. Ziel je Unterthema (`werkzeuge/zielgroessen.py` prüft es):
**mindestens 8 Verständnisfragen, mindestens 3 Aufgaben im Klausurstil**, und für jeden wichtigen Punkt eine Leiter
erkennen → verstehen → Klausurform.

**1. Klausurpunkte-Inventar (intern):** `inhalte/<fach>/plan/gp_inventar.json`. Es wird nicht gebaut.
- Je Prüfungspunkt: `id`, `text`, `t` (Unterthemen), `art` (nennen | erklaeren | rechnen | zeichnen | rf …), `such` (Suchwörter),
  `j` (in wie vielen Jahren beim aktuellen Prüfer gefragt), `aus: true` (nicht mehr relevant).
- Kopf: `wichtig_ab` (ab wie vielen Jahren „Wichtig“; bei nur einem Protokoll 1).
- `werkzeuge/abdeckung.py <fach>` zeigt, welcher Punkt in welchem Werkzeug noch fehlt.
- **Bestehende Sterne (`star=True`):** Diese Themen sind die wichtigen Punkte. Trage sie ins Inventar ein, damit
  `wichtig.py` sie markiert. Das Abzeichen heißt in diesem Kurs „★ Wichtig!“; den Text in `ansichten.js` (`badges`) anpassen.

**2. Merklisten → Fragen:** `werkzeuge/merklisten_fragen.py <fach>`.
- Aus jeder Merkliste entstehen „Nennen/Erklären“ (Klausurform), Verknüpfen, Zuordnen, „Was gehört nicht dazu“,
  Lückentext und Karten (`kr`).
- Prüfpunkte im Format „Begriff: Erklärung“, damit „Nennen und erklären“ auch die Erklärung prüft.

**3. Hand-Familien je Klausurpunkt:** nach dem Muster `vorlagen/klausurpunkte.py`, IDs `:kp-`.

**4. Klausurstil je Unterthema:** `werkzeuge/klausurstil.py <fach> --liste` macht Vorschläge aus den Karteikarten.
- Die Aufgabenstellungen **von Hand prüfen** und in `werkzeuge/klausurstil_<fach>.json` ablegen
  (`{"Vorderseite": {"nennen": "…", "erklaeren": "…"}}`, `null` = weglassen). Danach erneut ausführen.
- Stil des jeweiligen Prüfers („Nennen Sie drei …“, „Unterscheiden Sie …“, Rechnen mit Rechenweg, R/F-Blöcke).
- Ergebnis: Familien `:ks-` mit `klausur: true, stil: 1`.

**5. Verständnisfragen von Hand:** nach `vorlagen/verstehen.py`. Je Fach eine Liste.
- Familien `:vs-verstehen-…` und `:vs-klausur-…`; die Zuordnung zum Klausurpunkt steht in `PUNKT`.
- **Kreativ, besonders in Mathe:**
  - „Fehler im Rechenweg antippen“ (`weg()`)
  - „Was passiert, wenn …“
  - Grenzfälle, Vorzeichen, Einheiten
  - Aussagen-Blöcke (R/F)
  - Reihenfolge von Rechenschritten
- In Mathe gab es 40 solche Fragen.

**6. Zeichenaufgaben**, wo die Klausur zeichnen lässt: nach `vorlagen/zeichnen.py`.

**7. Aufräumen:** `werkzeuge/fehler_fix.py` (kein „Stimmt so“), dann `werkzeuge/mc_kuerzen.py <fach>`.
- Lange Auswahlantworten kürzen; die ausführliche Antwort bleibt als Erklärung.
- Ziel: Die richtige Antwort ist in unter 40 % der Fälle die längste. `bau.py` meldet den Anteil.

**8. Markieren und prüfen:**
- `werkzeuge/wichtig.py <fach>` erzeugt `wichtig.json`.
- `werkzeuge/zielgroessen.py <fach>`: 0 Lücken (Ausnahme: Unterthemen mit „nicht klausurrelevant“ im Titel).
- `werkzeuge/abdeckung.py <fach>`: alle Punkte abgedeckt.
- `werkzeuge/uebersicht.py` zeigt die Zahl der Fragen je Fach, Oberthema, Unterthema und Werkzeug.

**Generator-Reihenfolge:** merklisten_fragen → klausurpunkte → klausurstil → verstehen → zeichnen → fehler_fix →
mc_kuerzen → wichtig → zielgroessen/abdeckung.

---

## Teil C · Pro Fach umsetzen

Für jedes fertige Fach dieses Kurses (`bwl`, `mkt`, `wima`, `mawi`, danach die neuen) Teil B ganz durchgehen.
Je Fach ein Commit, Nachricht z. B. „mawi: Klausurstil und Verständnisfragen je Unterthema, Leitern“.
In `faecher.json` `tiefe` setzen: 1 bei Rechenfächern, 2 bei gemischten, 3 bei Begriffs-Fächern.

---

## Teil D · Neutral formulieren (Pflicht)

**Nirgends auf der Website darf stehen oder erkennbar sein, woher Klausurwissen stammt.** Gemeint sind Protokolle,
Altklausuren und Aussagen wie „Prof. X fragt gern …“ oder „kam 2023 dran“.
- Das Wissen wirkt nur im Hintergrund: Auswahl, Gewicht, „Wichtig“, Aufgabenstil.
- Allgemein formulieren, z. B. „in Wirtschaftsklausuren typisch“ oder „häufig gefragt“.
- Lehrpersonen nur nennen als Lehrperson, für Folien oder offizielle Übungen.
- `werkzeuge/neutral.py` ersetzt bekannte Formulierungen.
- Der Spuren-Check in `bau.py` bricht den Bau ab, wenn etwas durchrutscht.
  **Die Namensliste im Check auf die Lehrpersonen dieses Kurses umstellen:** Paul, Chammout, Weinberger, Meier,
  Kersten-Frisch, Krcal. Die alten Namen bleiben drin, solange die alten Fächer gebaut werden.
- Achtung: Das bisherige Abzeichen „★ Wichtig!“ ist in Ordnung, ein Text wie „aus Protokoll“ nicht.

---

## Teil E · Abschluss
- `python3 bau.py --test` grün, Screenshots (`node tests/screenshots.js`): Handy 390 px, hell und dunkel, kein Überlauf.
- In `UMSETZUNGSPLAN.md` einen Abschnitt „Update aus DBM26A übernommen“ mit Stand je Fach ergänzen.
- An die Artifact-Adresse dieses Kurses veröffentlichen (nie an die alte).
- **Keine Neuigkeiten-Einträge ohne Freigabe des Nutzers.**
