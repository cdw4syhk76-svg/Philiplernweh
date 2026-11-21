# Design-Konzept LernTool (Stand 08.11.2026, noch nicht umgesetzt)

Grundlage: Screenshots aller Hauptansichten (Handy 390 px und Desktop 1360 px, hell und dunkel).
Es gelten weiter die Prinzipien aus CLAUDE.md: Werkzeug statt Lernplan, keine Ampel, keine Strafen,
keine Statistik-Spielereien. Der Dunkelmodus bleibt, wie er ist. Farben nur über Tokens.

## 1. Was heute unruhig oder unpassend wirkt

| # | Stelle | Problem |
|---|--------|---------|
| 1 | Überall | **Zu viele gleich laute Farben.** Start: 5 kräftige Fachkarten, darunter 3 Pastellkacheln (blau, grün, apricot). Training: weiße, schwarze und gelb umrandete Fläche, dazu 4 unterschiedlich getönte Werkzeugkacheln und drei farbige Etiketten. Das Auge findet keinen Einstieg. |
| 2 | Handy, alle Seiten | **Die schwebende Navigation verdeckt Inhalt** (Start: Überschrift „Verblasst“; Desktop-Training: Titel „Wirtschaftsmathematik“). Auf der Lernseite liegen zwei Leisten übereinander (Werkzeuge und Navigation). Sie nehmen etwa 20 % des Bildschirms ein, und „Sandbox“ ist rechts abgeschnitten. |
| 3 | Start, Neustart | **Leerzustände wirken wie Versagen:** fünfmal „0 % prüfungsreif“, „0 verblasst“, „0 fällig“ und eine riesige „0“. |
| 4 | Start, Handy | Fachkarten sind 380 px hoch und größtenteils leerer Ring. Man sieht nur 1,3 Karten. Die Erklärung „Karte antippen: sie dreht sich um“ zeigt, dass die Bedienung sich nicht selbst erklärt. Die Kennzahlen umbrechen in zwei Zeilen. |
| 5 | Lernseite, Handy | Vor dem eigentlichen Text kommen: Fachwahl, großer lila Kopf, Unterthemen-Leiste und drei Kacheln (Prüfungsstand „–“, Klausur, gelber Spruch). Der Inhalt beginnt erst unterhalb des ersten Bildschirms. Die gelbe Spruchkachel ist das lauteste Element der Seite. |
| 6 | Training | Auf dem Handy 2.800 px lang. Im hellen Modus steht ein dunkles Feld. Die Erklärtexte („Nicht hier: Mini-Quiz …“, „Fach antippen zum Auswählen …“) sind ein Zeichen für zu viel Komplexität. |
| 7 | Namen | Uneinheitlich: Start/Heute, Training/Sandbox (die Lern-Leiste sagt „Sandbox“), „Methodisch lernen“, „Oberthema prüfen“, „Übungsklausur“, „Refresh“. |
| 8 | Quiz | Drei Rahmen ineinander (blau umrandet, grauer Kasten, weißes Feld). Darüber steht ein langer Erklärtext zu den Fragearten. |
| 9 | Selbstbewertung | Nach „Lösung“ erscheinen „Konntest du es? Ja / Teilweise / Nein“ unscheinbar. Man versteht nicht, **wozu** man bewerten soll: dass „Nein“ die Aufgabe später zurückbringt, steht nirgends. |
| 10 | Typografie | Viele kleine graue Hilftexte (12–13 px), dazu der schwere Display-Font in fast jeder Überschrift. Es gibt kaum Abstufung zwischen wichtig und nebensächlich. |

## 2. Leitidee: „ruhige Fläche, eine Akzentfarbe je Moment“

- **Neutrale Flächen** (Papier und Karte) für alles. Die Fachfarbe nur noch als Akzent: Streifen, Punkt, Fortschrittsbalken, Kopf der Lernseite.
- **Eine Primärfarbe für die Hauptaktion** je Bildschirm (z. B. „Weiterlernen“). Alles andere sekundär (Umriss oder Text).
- **Keine Pastell-Kachelwand mehr.** Gleiche Flächenfarbe, Unterschiede über Icon und Überschrift.
- **Leerzustände freundlich und konkret:** statt „0 %“ steht „noch nicht geprüft“. Ringe erscheinen erst, wenn es etwas zu zeigen gibt.
- **Inhalt zuerst:** Auf jeder Seite ist der erste Bildschirm das, weswegen man gekommen ist.

## 3. Startseite neu

```
Hallo Nick,
noch 30 Tage bis Wertschöpfung – heute reicht schon ein Unterthema.

┌ Weiterlernen ───────────────────────────────┐
│ Logistik · Meldebestand & Höchstbestand      │
│ zuletzt gestern · 3 von 5 Abschnitten  [→]   │
└──────────────────────────────────────────────┘
Deine Fächer          (kompakte Zeilen statt Riesenkarten)
● ABWL            39 Tage   ▬▬▬▭▭  2/6 geprüft
● Marketing       39 Tage   ▭▭▭▭▭  noch nicht geprüft
…
Wiederholen: 4 fällig  ·  1 Oberthema verblasst   (nur sichtbar, wenn > 0)
```

**Gruß (gewünscht):**
- Steht oben, eine Zeile „Hallo Nick,“ im Display-Font (28–32 px). Darunter eine kurze Zeile Motivation (15 px, gedämpfte Farbe). Kein Kasten, keine Grafik, keine Emojis: nicht einnehmend.
- Der Satz entsteht aus echten Fakten, ohne Druck und ohne Zählerspiele. Er wechselt täglich:
  - Tageszeit: „Guten Morgen, Nick.“ oder „Schön, dass du da bist.“
  - Nächste Klausur: „Noch 30 Tage bis Wertschöpfung, ein Unterthema am Tag reicht.“
  - Letzte Sitzung: „Gestern hast du Bestellverfahren abgeschlossen. Weiter so.“
  - Nach einer Pause: „Schön, dass du wieder da bist. Fang klein an.“
  - Wenige Tage vor der Klausur: „Endspurt. Probeklausur und Refresh sind jetzt am wertvollsten.“
- Name: Beim ersten Besuch steht statt des Grußes eine kleine Zeile „Wie soll ich dich nennen? [____]“. Sie lässt sich wegklicken und in den Einstellungen ändern. Der Name wird über den Login-Code mit abgeglichen.

**Weiterlernen-Karte:** die wichtigste Aktion. Sie führt zum zuletzt geöffneten Unterthema und zeigt, wo man stehen geblieben ist. Sie ersetzt „Fang mit einem Fach an“, sobald es einen Stand gibt.

**Fächer:** auf dem Handy als kompakte Liste (Fachpunkt, Name, Tage bis zur Klausur, schmaler Balken). Antippen öffnet die Oberthemen. Kein Umdrehen mehr, das braucht keine Erklärung. Auf dem Desktop bleiben Karten, aber flacher (etwa 180 px statt 380 px).

## 4. Weitere Ansichten

- **Navigation (Handy):** eine Leiste. Die Lern-Werkzeuge (Verdecken, Karten, Markiert, Suche, Unsicher) kommen in einen „Werkzeuge“-Knopf oben rechts im Lernkopf oder als ausklappbares Menü. Jede Seite bekommt unten genug Abstand, damit nichts verdeckt wird. „Sandbox“ heißt überall „Training“.
- **Lernseite:**
  - Der Kopf wird auf dem Handy kompakt: Titel, „2 von 15“ als kleiner Text und schmaler Balken.
  - Die drei Kacheln werden zu einer Zeile („Klausur in 30 Tagen · Übungsklausur →“).
  - Der Spruch wandert ans Ende des Unterthemas, in ruhiger Farbe.
- **Training:**
  - Schritt 1 als waagerechte Fach-Chips.
  - Schritt 2 als Werkzeugraster auf heller Fläche, mit gleicher Kachelfarbe, Icon in Fachfarbe.
  - Schritt 3 „Prüfen“ bleibt, aber ohne gelben Rahmen. Gelb nur für „Ganze Klausur prüfen“.
  - Erklärtexte werden zu kurzen Untertiteln.
- **Quiz:** ein Rahmen statt drei. Oben eine schmale Fortschritts- und Serienzeile, die Erklärung zu den Fragearten nur als „?“. Auf dem Desktop Tastenkürzel (1–4, Enter, Pfeil).
- **Selbstbewertung** (Punkt 9):
  - Nach „Lösung zeigen“ erscheint direkt darunter eine hervorgehobene Zeile: „Wie lief’s? Ja · Teilweise · Nein“. Dazu der Hinweis: „Nein und Teilweise kommen später in ‚Wiederholen‘ zurück.“
  - Bis zur Bewertung bleibt die Teilaufgabe markiert, z. B. mit einem Punkt am Rand.
  - Am Blattende steht: „2 Teile noch nicht bewertet“ (antippen springt hin) und „3 Teile kommen zum Wiederholen“.
  - Auf der Startseite erscheint dann „Wiederholen: 3 fällig“. So sieht man den Sinn der Bewertung sofort.
- **Arbeitsblatt „Ganzes Blatt neu“** (Rückfrage): Gerade wird jede *gezeigte* Aufgabe zurückgestellt. Wichtiges, das man nur übersprungen hat, käme also erst spät wieder. Vorschlag:
  - Zurückgestellt werden nur Aufgaben, die mit „Ja“ bewertet wurden.
  - Übersprungene und unbewertete Aufgaben dürfen sofort wiederkommen.
  - „Nein“ und „Teilweise“ kommen ohnehin über „Wiederholen“ zurück.

## 5. Mögliche neue Funktionen (passend zu „Werkzeug, kein Lernplan“)

1. **Weiterlernen** (siehe oben): der größte Komfortgewinn.
2. **Formelsammlung je Fach:** alle Formelkästen eines Fachs auf einer Seite, druckbar. Ideal kurz vor der Klausur.
3. **Fokusmodus Lernseite:** blendet Kopf, Leisten und Kacheln aus, nur Text und Schaubilder.
4. **Druckansicht** für Arbeitsblatt und Probeklausur (sauberes A4, Lösungen auf letzter Seite).
5. **„Meine Fehler“-Liste:** alle mit „Nein“ bewerteten Teile und falsch beantworteten Fragen mit Sprung zur Stelle. Keine Statistik, nur eine Liste.
6. **Kleine Rückmeldungen:** ein ruhiges Häkchen bei richtig, eine kurze Bewegung beim Umdrehen. Kein Konfetti.
7. **Als App installieren** (Startbildschirm-Symbol, offline lesbar), falls die Veröffentlichung es zulässt.

## 6. Name „Lernweh“ und Führung durch das Tool

**Name:** Das Tool heißt **Lernweh** (wie Fernweh).
- Der Name steht als ruhige Wortmarke klein oben links bzw. im Seitentitel. Auf der Startseite steht er nicht über dem Gruß, der Gruß bleibt das Erste.
- Die Fernweh-Idee lässt sich leise aufgreifen: Die Führung ist eine „Reise“ mit Stationen. Keine Koffer- oder Flugzeug-Grafiken.

**Führung („Rundgang“):** Sie startet automatisch beim ersten Besuch, nach dem Namen. Danach jederzeit über Einstellungen → „Rundgang starten“ und als kleines „?“ in der Leiste.

Ablauf je Station:
1. Lernweh springt („teleportiert“) zur echten Ansicht. Dabei wechselt die Adresse wirklich, scrollt zum Element und öffnet es bei Bedarf.
2. Das Element wird hervorgehoben: alles andere leicht abgedunkelt, ein Rahmen um das Element.
3. Daneben eine kleine Sprechblase: Titel, 1–2 Sätze, „Station 3 von 12“.
4. Darunter die Knöpfe „Zurück“ · „Weiter“ · „Beenden“ und Pfeiltasten.
5. „Weiter“ springt zur nächsten Station, auch auf eine andere Seite.
6. Abbrechen ist jederzeit möglich. Lernweh merkt sich die Station und bietet beim nächsten Mal „Rundgang fortsetzen“ an.

Stationen (Vorschlag, je ein Satz Text):

| # | Wo | Was gezeigt wird |
|---|----|------------------|
| 1 | Start · Gruß | Hallo, das ist Lernweh: ein Werkzeug, kein Lernplan. Du entscheidest, was du lernst. |
| 2 | Start · Weiterlernen | Hier geht es immer dort weiter, wo du aufgehört hast. |
| 3 | Start · Fächer | Deine Fächer mit Klausurtermin und Stand, nur aus Übungsklausuren berechnet. |
| 4 | Lernen · Kopf | Fach → Oberthema → Unterthema. Oben wechselst du das Oberthema. |
| 5 | Lernen · Text und Schaubild | Erklärungen, Formeln mit „In Worten“ und Beispiel, Schaubilder zum Antippen und Rechnen. |
| 6 | Lernen · Mini-Quiz | Am Ende jedes Unterthemas fünf schnelle Fragen. |
| 7 | Lernen · Werkzeuge | Verdecken, Markieren, Unsicher, Suche, Karten aus dem Text. |
| 8 | Lernen · ⚑ Fehler melden | Wenn etwas falsch oder unklar ist: antippen, kurz beschreiben. |
| 9 | Training · Fächer | Wähle, was du üben willst, bis hinunter zum einzelnen Oberthema. |
| 10 | Training · Werkzeuge | Quiz, Definitions-Drill, Karteikarten, Arbeitsblatt. |
| 11 | Training · Arbeitsblatt (Selbstbewertung) | Nach „Lösung“ bewerten. „Nein“ kommt später wieder. |
| 12 | Training · Wiederholen | Was du nicht konntest, kommt hier zum richtigen Zeitpunkt zurück. |
| 13 | Training · Prüfen | Übungsklausur je Oberthema, je Fach oder die ganze Klausur, mit Zeit und Note. |
| 14 | Einstellungen | Login-Code für mehrere Geräte, Hell/Dunkel, deine Meldungen, Rundgang neu starten. |

Technik (für später):
- Eine Stationsliste mit Adresse, Selektor und Text.
- Ein Overlay-Element mit Ausschnitt über `box-shadow` oder `clip-path`.
- Am Handy sitzt die Sprechblase unten über der Leiste, damit nichts verdeckt wird.
- Funktioniert hell und dunkel.
- Keine Bibliothek nötig.

## 7. Reihenfolge, falls umgesetzt wird

1. Gruß und Name, Weiterlernen-Karte, Leerzustände (Startseite), Name „Lernweh“.
2. Selbstbewertung sichtbar machen und Arbeitsblatt-Regel anpassen.
3. Navigation am Handy (eine Leiste, nichts verdeckt), Namen vereinheitlichen.
4. Farbsystem beruhigen (Start, Training, Lernkopf).
5. Rundgang durch Lernweh (braucht die neuen Namen und die feste Navigation).
6. Quiz entschlacken, dann die neuen Funktionen nach Wunsch.
