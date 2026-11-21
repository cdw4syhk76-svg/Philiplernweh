# Lernweh für einen neuen Kurs – Handbuch für die umsetzende KI

Dieses Repo ist **Lernweh**, ein Lernwerkzeug für einen Studienkurs. Es wurde für den Kurs DBM26A gebaut
(Fächer ABWL, Marketing, Logistik & MaWi, Production, Wirtschaftsmathe). Du baust es jetzt für einen **anderen Kurs**:
andere Fächer, andere Professoren, andere Folien und Altklausuren. **Alle Inhalte sind neu, Technik und Stil bleiben gleich.**

Das Ergebnis soll sich anfühlen wie das heutige Lernweh: gut erklärt, viele Schaubilder, Mini-Quiz, alle Werkzeuge
(Quiz, Drill, Karteikarten, Arbeitsblatt, Übungsklausur je Oberthema, Probeklausur, Methodisch lernen) und
**genauso viele Aufgaben** wie hier. **Vorbild für alles Inhaltliche ist das Fach Logistik & MaWi.**

Lies dieses Handbuch einmal ganz. Danach arbeitest du **Fach für Fach** mit `/fach-komplett <fach-id> neu`.

---

## 1. Grundsätze (vom Nutzer festgelegt, gelten überall)

1. **Werkzeug, kein Lernplan.** Drei Bereiche: Start · Lernen · Training. Keine Ampel, kein Tagesplan, keine Strafen,
   keine Statistik-Spielereien. Prozente entstehen **nur** durch die Übungsklausur je Oberthema (und den Refresh).
2. **Logistik & MaWi ist der Maßstab.** Bevor du ein Unterthema schreibst, sieh dir ein vergleichbares Logistik-Thema an
   (Befehle in Abschnitt 9). Erklärtiefe, Beispiele, Schaubilder, Aufgabenmenge: mindestens so gut.
3. **Klausurnähe vor allem anderen.** Was in Altklausuren, Gedächtnisprotokollen, Probeklausur und Übungen vorkommt,
   muss auf der Lernseite vorkommen, gut erklärt, und als Frage, Aufgabe und Probeklausur-Variante geübt werden können.
4. **Vollständigkeit vor Kürze.** Der Folienstoff kommt komplett vor. Was nur ergänzt, ist als „Zusatz · kommt nicht dran“
   markiert. Nie Inhalte ersatzlos löschen.
5. **Keine sichtbare Spur der Quellen.** Auf der Seite steht nie „Gedächtnisprotokoll“, „GP“, „Altklausur“,
   „Klausurnotizen“, „exam notes“, „frühere Klausur“ oder Jahreszahlen früherer Klausuren. Die Daten werden genutzt, der
   Nutzer darf die Herkunft nicht sehen. `bau.py` prüft eine Liste solcher Wörter in `dist/` und bricht ab.
   Erlaubt ist „im Klausurstil“ oder „Klausur:“-Hinweise.
6. **Einfach erklären.** Kurze, klare Sätze, ein durchgehendes Alltagsbeispiel je Oberthema, „Einfach gesagt:“ nach
   schweren Begriffen. Keine Floskeln, keine Emojis in Inhalten und Schaubildern.
7. **Fremdsprachige Klausur:** Die ganze Seite in Klausursprache, ein Schalter übersetzt alles ins Deutsche
   (Bausteine `werkzeuge/fachbau/bausteine_zweisprachig.py`, Muster: Production, Registry-Flag `"englisch": true`).
8. **Antworten an den Nutzer:** kurz, deutsch, Status + Commit-Hash.

## 2. Start: Repo vorbereiten

1. Der Nutzer legt ein **neues GitHub-Repo** an und kopiert diesen Stand hinein (oder „Use this template“).
   Arbeite nur dort, nie im alten Repo.
2. **Die alten Fächer bleiben zunächst im Bau.** Damit funktionieren `python3 bau.py --test` und alle Tests sofort,
   und du kannst Logistik im Browser jederzeit mit deinem Fach vergleichen. Deine Fächer erscheinen daneben.
3. **Kursdaten** in `inhalte/studium.json` eintragen (Format siehe vorhandene Datei):
   - `semester`: Kurs, Studiengang, Hochschule, Semester, Beginn/Ende, Leitung, **`login: false` behalten** (Website ohne Codes)
   - `module`: je Modul `id`, `name`, `ects`, `sem`, `teile` = [[Teilname, Professor, fach-id]], `pruefung`
   - `klausuren`: je Klausur `modul`, `titel`, `kurz`, `beginn`/`ende` (ISO), `raum`,
     `teile` = [[Teilname, fach-id, Reihenfolge, Kürzel, Kurzname]], `faecher`, `stoff` (Gewichte in %), `punkte`, `minuten`
4. **Fächer** in `inhalte/faecher.json` eintragen, je Fach:
   - `id` (kurz, klein, ohne Umlaute), `name`, `lang` (voller Name), `modul`, `person` (Prüfer)
   - `farbe` (Kürzel), `farben.hell.primary` (Fachfarbe, kräftig und dunkel genug für weiße Schrift) und `farben.dunkel` (wie bei Marketing)
   - `mix`: welche Fragearten der Prüfer bevorzugt (z. B. `{"liste": 2.5, "kurz": 1, "num": 1}`), `pruefer`: ein Satz zum Stil
   - `modus: "lernen"`, `brueche: true` bei Rechenfächern (a/b wird automatisch zum Bruch)
   - optional `"rechnen": true` (Fach mit „Direkt üben“-Rechenblock wie Mathe), `"englisch": true` (fremdsprachige Klausur)
5. **Name und Titel:** `bau.py` Zeile mit `<meta name="description" …DBM26A…>` an den Kurs anpassen;
   `app/admin.html` Titel prüfen. Der Name bleibt **Lernweh**.
6. **Quellen:** Der Nutzer legt die Unterlagen in `unterlagen/<Fach>/` ab (Folien, Klausuren, Übungen, `info.txt`). Fehlt etwas Wesentliches, frag einmal gesammelt nach.
   Daraus Text machen und intern ablegen (wird nie gebaut): `inhalte/<fach>/plan/quellen/`.
   - PDFs mit Text: `pdftotext -layout datei.pdf quellen/datei.txt` (danach nur noch den Text lesen, nie das PDF)
   - Scans: `pdftoppm -r 70 -f N -l N -png datei.pdf seite` und Bild ansehen
   - Word: `python3 -c "import docx; …"` oder `pandoc`

## 3. Ablauf je Fach (Reihenfolge einhalten, nach jedem Schritt testen und committen)

| # | Schritt | Ergebnis | Zielgröße (Logistik-Werte) |
|---|---------|----------|----------------------------|
| 1 | **Klausurprofil** | `inhalte/<fach>/plan/profil.md` (intern): jede bekannte Klausuraufgabe mit Thema, Typ, Punkten, Häufigkeit; Aufbau, Punkteverteilung, Lieblingsthemen, Operatoren | alle Altklausuren und Protokolle ausgewertet |
| 2 | **Gliederung** | Oberthemen = Kapitel der Folien, Unterthemen 3–9 je Oberthema, roter Faden (`kette`) | Logistik: 15 Oberthemen, 88 Unterthemen |
| 3 | **Lernseiten** | `werkzeuge/<fach>/k1.py …` mit `bausteine_de.py`, gebaut mit `python3 werkzeuge/fachbau/bauen.py <fach>` | je Unterthema ~3.000 Zeichen „Ganz erklären“ |
| 4 | **Schaubilder** | Hauptschaubild je Unterthema (antippbar oder Rechner), weitere als aufklappbare Schaubilder; Skripte in `werkzeuge/<fach>/k<N>_figuren.js` | Median 3 je Unterthema |
| 5 | **Glossar** | `inhalte/<fach>/glossar.json` | Logistik: 145 Begriffe |
| 6 | **Fragen** | `inhalte/<fach>/fragen.json` (Familien) | Median 10 je Unterthema, mindestens 8; alle Klausur- und Übungsfragen mit `klausur: true` |
| 7 | **Große Aufgaben** | `inhalte/<fach>/aufgaben.json` | ≥ 1 je Oberthema, Rechenfächer mehr; Logistik: 15 |
| 8 | **Karteikarten** | `inhalte/<fach>/karten.json` | jedes Unterthema ≥ 4, dazu **jeder fett gedruckte Fachbegriff** als Karte oder im Glossar |
| 9 | **Probeklausur-Bogen** | `inhalte/<fach>/klausur.json` | Aufbau 1:1 wie die echte Klausur, 3–7 Varianten je Teil; Logistik: 10 Aufgaben, 71 Varianten |
| 10 | **Prüfen** | Abschnitt 7 | alles grün, Screenshots angesehen |

### Schritt 3–4 im Detail: ein Unterthema wie in Logistik

Ein Unterthema hat diese Felder (Baustein `thema(...)` in `werkzeuge/fachbau/bausteine_de.py`):

| Feld | Inhalt | Logistik-Beispiel (`meldebestand`) |
|------|--------|------------------------------------|
| `kern` | 1–2 Sätze: das Wichtigste | „Sinkt der Bestand auf den Meldebestand, wird bestellt …“ |
| `kurz` | „Kurz erklärt“: 2–4 einfache Absätze mit Alltagsbeispiel | „Wer erst bestellt, wenn das Regal leer ist …“ |
| `fig` | Hauptschaubild mit Satz davor (`fw(...)`), bei Rechenthemen Regler → Bild → Karten ①②③ | Lagerbestandsdiagramm mit drei Reglern |
| `figcap` | Herkunft des Bildes (Folie/Skriptseite) | „nach Skript S. 14“ |
| `merk` | Merksatz (wird zur Karteikarte) | „Meldebestand = Verbrauch je Periode × Lieferzeit + Sicherheitsbestand …“ |
| `article` | „Ganz erklären“: Abschnitte (`h3`) mit Überleitungen (`weiter`), Karten, Tabellen, Formel-Dreiklang (`fx`), Beispiel mit Schritten (`bsp`), typischer Fehler (`falle`), Klausur-Hinweis, weitere Schaubilder (`mfig`), Kurz-Check (`wahr`) oder Spiel (`spiel`) wo sinnvoll | siehe `inhalte/logistik/fach.json` |
| `exam` | was in der Klausur dazu kommt | „Meldebestand berechnen (Formel nennen!) …“ |
| `fehler` | Liste typischer Fehler | „Den Sicherheitsbestand vergessen …“ |
| `src` | Folien-/Skriptstelle | „Skript S. 13–15“ |
| `star` | Kernthema (oft in der Klausur) | `True` |

**Formeln** immer als Dreiklang: Formel (LaTeX in `\[ … \]`), „In Worten“, „Im Beispiel“, optional „Woher kommt die Formel?“.
Schreibweise wie auf Papier: `\frac{…}{…}`, `\cdot`, `\sum_{i=1}^{n}`, keine „a / b“ im Fließtext von Rechenfächern.

**Schaubilder** (gleiche Regeln wie Logistik):
- Hauptschaubild höchstens ~400 px breit (viewBox), Schrift ≥ 12, damit es am Handy (390 px) ohne Wischen lesbar ist.
  Lieber Wischen als winzige Schrift; nicht vollstopfen.
- Farben nur über Theme-Variablen (`var(--ink)`, `var(--primary)`, `var(--card)`, `var(--line)` …), nie feste Hex-Werte.
  So bleibt alles im Dunkelmodus lesbar.
- **Eine** Hervorhebung je Bild (`art='hl'`), ruhige Linien, keine Verläufe, keine Emojis.
- Jeder Kasten erklärt sich beim Antippen (`tip=`), darunter der Hinweis „Tippe auf einen Teil …“ (`bild(...)`).
- Rechenthemen interaktiv: `regler([...])` + SVG mit `id` + `schritte_karten([...])`, das Skript dazu in
  `werkzeuge/<fach>/k<N>_figuren.js`. **Muster: das Meldebestand-Skript in `inhalte/logistik/figuren.js`** (`mbV`, `mbT`, `mbS`, `figMB`).
  Jedes Skript beginnt mit `if (!document.getElementById('…')) return;`, es läuft nach jedem Seitenwechsel.
  Hilfen aus `inhalte/basis/alt_sb.js` und `alt_base.js`: `MP` (Plot), `svgAxes`, `TXS` (Text), `drawTree` (Baum), `LG(en, de)`.
- **Spiele** (Zuordnen) nur, wo sie beim Durchdenken wirklich helfen (Logistik: Materialarten, Fertigungsarten, Incoterms).
  **Richtig/Falsch-Checks** (`wahr`) dort, wo die Klausur R/F-Blöcke hat.

### Schritt 5–9: Formate

Am schnellsten lernst du die Formate an den Logistik-Dateien (Abschnitt 9). Kurzfassung:

- **Glossar** `{"begriffe": [{"begriff", "muster" (Suchmuster im Text), "heimat" (Unterthema), "text"}], "nicht_markieren": []}`
- **Fragen** `{"familien": [{"id", "t" (Unterthema), "f", "k" (Oberthema-Nr.), "s" (Kernthema), "y": "fam", "fam": 1, "z" (Lernziel), "a": [Fragen]}]}`.
  Fragearten `y`: `mc`, `mc_multi` (Mehrfachauswahl, R/F „alles oder nichts“), `liste` (Aufzählen), `kurz`, `zuord`, `reihe`,
  `num` (Rechnen, mit Generator `gen` und Formel `ev`), `luecke`, `hot` (Schaubild beschriften), `beschr`.
  Jede Frage: `p` (Text), `w` (Erklärung), `lvl` 1–3, `klausur: true` wenn aus Klausur/Übung.
  **Ablenker gleich lang und plausibel:** Der Bau warnt, wenn die richtige Antwort zu oft die längste ist (Ziel unter 40 %).
  Muster für Rechenfragen mit Zufallszahlen: `num`-Fragen in `inhalte/logistik/fragen.json`.
- **Große Aufgaben** `{"aufgaben": [{"id", "unter": [Unterthemen], "art": rechnen|anwendung|zeichnen|transfer, "stufe" 1–3, "klausur": true,
  "titel", "quelle" („im Klausurstil“), "ausgang" (Fall), "teile": [{"text", "punkte", "tipp1", "tipp2", "loesung", "ergebnis"?, "einheit"?, "tol"?}]}]}`.
  **Zahlen immer in Python rechnen**, nie im Kopf (Muster: `muster/werkzeuge/aufgaben_extra.py` nach Schritt 11, vorher `werkzeuge/aufgaben_extra.py`).
  Fallbeispiele mit Firma, Zahlen und Entscheidung.
- **Karteikarten** `{"karten": [{"t" (Unterthema), "v" (Vorderseite), "r" (Rückseite)}]}`, Vorderseiten eindeutig.
  Glossarbegriffe und Merksätze werden automatisch zu Karten; zusätzlich Aufzählungen, Formeln, Unterscheidungen.
  Danach **jeden fett gedruckten Fachbegriff** der Lernseiten abgleichen (Muster: `werkzeuge/karten_begriffe.py`).
- **Probeklausur** `{"deckblatt": {fach, pruefer, hilfsmittel}, "aufgaben": [{"titel", "punkte", "intro"?, "teile": [{"punkte", "varianten": [
  {"id", "unter", "text", "felder": [{"typ": text|zahl|rf|menge|ausdruck|matrix|wort, "p", …}], "loesung", "vorrang"?}]}]}]}`.
  Aufbau, Punkte, Operatoren und Antwortformen **wie die echte Klausur**. Per Generator-Skript schreiben
  (Muster: `werkzeuge/logistik_klausur.py`, Rechenfach: `werkzeuge/mathe_klausur.py` + `mathe_zufall.py`).

## 4. Werkzeuge im Repo

| Werkzeug | Zweck |
|----------|-------|
| `python3 bau.py [fach]` | baut nach `dist/` |
| `python3 bau.py --test` | bauen + Engine-, Klick- und Online-Test. **Vor jedem Commit grün.** |
| `node tests/screenshots.js` | Screenshots Handy/Desktop, hell/dunkel, meldet Überlauf und JS-Fehler |
| `python3 werkzeuge/fachbau/bauen.py <fach>` | baut Lernseiten aus `werkzeuge/<fach>/k1.py …` |
| `werkzeuge/fachbau/bausteine_de.py` | alle Bausteine der Logistik-Seiten (deutsch) |
| `werkzeuge/fachbau/bausteine_zweisprachig.py` | dieselben Bausteine zweisprachig (fremdsprachige Klausur) |
| `python3 werkzeuge/kurs_vorlage.py --alte-faecher-weg` | am Ende: alte Fächer nach `muster/` |

Gerüst für ein Kapitel (`werkzeuge/<fach>/k1.py`):

```python
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *

t1 = thema('lagerfunktionen', 'Wozu ein Lager? Funktionen und Lagerarten', star=True,
    kern='Ein Lager gleicht Unterschiede zwischen Anlieferung und Verbrauch aus …',
    kurz=p('Zu Hause hast du einen Vorratsschrank …') + fw('Das Schaubild zeigt …') + bild(svg(400, 220, box(…, tip='…') + …, 'Lagerfunktionen')),
    article=h3('…') + p('…') + cards([...]) + weiter('…') + h3('…') + fx(...) + bsp(...) + falle('…') + mfig('…', svg(...)),
    merk='…', exam='Funktionen des Lagers nennen und mit Beispiel erklären.', fehler=['…'], src='Skript S. 18–20')

KAPITEL = kapitel('k1', 'Lager und Bestände', 'Worum es in diesem Oberthema geht …', ['Funktionen', '…'], [t1, …])
```

## 5. Schreibregeln

- Deutsch, kurze Sätze, aktive Sprache. Fachbegriff fett beim ersten Auftreten, dann „Einfach gesagt: …“.
- Ein **durchgehendes Beispiel** je Oberthema (Logistik: Getränkemarkt, Tischlerei; Production: Bäckerei).
- Überleitungen zwischen Abschnitten (`weiter(...)`): woher wir kommen, wohin es geht.
- Folieninhalt bleibt als Text erhalten; Schaubilder nur, wo sie klarer machen.
- Ergänzungen außerhalb des Folienstoffs: `zusatz(...)`.
- Klausurrelevantes zusätzlich mit `klausur_hinweis(...)` und im Feld `exam`.

## 6. Typische Fehler (hier schon einmal passiert, bitte vermeiden)

1. Quellenspur im Text („Your exam notes say …“, „im Protokoll“). → nie.
2. „÷“ oder „a/b“ statt Bruch in Rechenfächern. → LaTeX `\frac`, Registry `brueche: true`.
3. Hauptschaubild zu breit oder Schrift unter 12. → am Handy unlesbar.
4. Feste Farben in SVG oder Kästen. → im Dunkelmodus unsichtbar. Nur Theme-Variablen.
5. Richtige Antwort ist immer die längste. → Ablenker gleich lang formulieren.
6. Fragen-Familien ohne feste `id` oder IDs nachträglich geändert → Lernstand der Nutzer geht verloren.
   Muss umbenannt werden: alt → neu in `inhalte/umbenannt.json`.
7. Doppelte Karten-Vorderseiten (der Bau bricht ab).
8. Große Aufgabe mit `unter`, das es nicht gibt (der Bau bricht ab).
9. Zahlen in Aufgaben/Lösungen von Hand gerechnet → Fehler. Immer im Generator rechnen.
10. Unterthemen ohne Karten oder mit unter 8 Fragen.
11. Zuordnungsspiele überall eingestreut. → nur wo sie beim Verstehen helfen.
12. Probeklausur weicht im Aufbau von der echten Klausur ab.

## 7. Prüfen (je Fach, vor dem Commit)

1. `python3 bau.py --test` grün, keine Warnungen zu Ablenkern oder weggefallenen IDs.
2. `node tests/screenshots.js` und Bilder ansehen: Handy 390 px, Dunkelmodus, kein Überlauf, keine JS-Fehler.
3. Je Oberthema eine Lernseite ganz ansehen (Kurz erklärt, Schaubild antippen, Ganz erklären, Mini-Quiz).
4. Probeklausur des Fachs starten, abgeben, Musterlösung ansehen; Arbeitsblatt auf Klausurniveau ansehen.
5. Abdeckung: Jedes Thema aus Klausurprofil und Folien kommt auf einer Lernseite vor (Muster für einen Abgleich:
   `werkzeuge/klausurthemen_check.py`).

## 8. Abschluss des Kurses

1. Wenn alle eigenen Fächer stehen: `python3 werkzeuge/kurs_vorlage.py --alte-faecher-weg`
   (verschiebt ABWL, Marketing, Logistik, Production, Mathe nach `muster/`; Logistik bleibt dort zum Nachschauen).
2. **Tests** auf eigene Fächer umstellen (`grep -n "logistik\|marketing\|mathe\|abwl" tests/*`):
   - `tests/t_klick.js`: Fachwechsel (`lernf|mathe`), Fachauswahl im Training (`marketing`), Neuladen (`lern|marketing|m1|`),
     Probeklausur (`probe|Wirtschaftsmathe`), Fachkarte (`.fk[data-f="logistik"]`) → eigene Fach-IDs, Oberthemen, Klausurkürzel
   - `tests/t_engine.js`: Fächerliste und Logistik-Themen → eigene
   - `tests/t_online.mjs`: `/daten/mathe.js` → eine eigene Daten-Datei
3. `python3 bau.py --test` grün.
4. **Website ohne Login-Codes** (für diesen Kurs so festgelegt): Der Nutzer verbindet das Repo mit Vercel (Import, keine Umgebungsvariablen). `vercel.json` baut mit `python3 bau.py` und liefert `dist/` aus. Ohne `LOGIN=an` ist die Seite offen; `semester.login: false` in `inhalte/studium.json` schaltet den Online-Abgleich aus, der Lernstand bleibt im Browser. Den Namen für den Gruß trägt jeder selbst ein (auf „dein Name“ tippen). Jeder Push auf `main` aktualisiert die Website.
5. **Artifact-Version:** neue eigene Adresse (nicht die des alten Kurses), danach immer an dieselbe Adresse veröffentlichen.

## 9. Logistik als Vorbild ansehen (Befehle)

```bash
# Gliederung
python3 -c "import json;d=json.load(open('inhalte/logistik/fach.json'));[print(k['id'],k['titel_text'],[t['id'] for t in k['themen']]) for k in d['kapitel']]"
# ein Unterthema komplett (Felder und HTML)
python3 -c "import json;d=json.load(open('inhalte/logistik/fach.json'));t=[t for k in d['kapitel'] for t in k['themen'] if t['id']=='meldebestand'][0];[print('==',k,'\n',str(v)[:3000]) for k,v in t.items()]"
# Fragen eines Unterthemas
python3 -c "import json;f=json.load(open('inhalte/logistik/fragen.json'))['familien'];[print(json.dumps(x,ensure_ascii=False)[:600]) for x in f if x['t']=='meldebestand']"
# Schaubild-Skript zum Rechner
grep -n "mbV" inhalte/logistik/figuren.js
```

Nach Schritt 8.1 liegen dieselben Dateien unter `muster/inhalte/logistik/`.
Im Browser: `#lernen--logistik--l2--meldebestand` (solange die alten Fächer noch gebaut werden).
