# LernTool online stellen (Vercel + Supabase)

Ergebnis: Die Website läuft unter einer eigenen Adresse. Wer sie öffnet, sieht zuerst nur die Anmeldeseite.
Mit einem Code (z. B. `ABCDE-FGH23`) meldet man sich einmal pro Gerät an; der Lernstand liegt dann online und ist auf
Laptop, iPad und Handy derselbe (höchstens 3 Geräte je Code). Codes erzeugst und verwaltest du unter `/admin.html`.

## 1. Supabase (Datenbank) – ca. 5 Minuten
1. Auf supabase.com kostenlos registrieren → **New project**. Region: *Central EU (Frankfurt)*. Datenbank-Passwort irgendwo notieren.
2. Links **SQL Editor** → **New query** → den Inhalt von `werkzeuge/supabase.sql` einfügen → **Run**.
3. Links **Project Settings → API** (bzw. „Data API“ und „API Keys“). Zwei Werte brauchst du gleich:
   - **Project URL**, z. B. `https://abcdxyz.supabase.co`
   - den geheimen **service_role**-Schlüssel (bei neuen Projekten heißt er „secret key“, `sb_secret_…`).
   Diesen Schlüssel nie weitergeben und nie in den Code schreiben.

## 2. Vercel (Website) – ca. 5 Minuten
1. Auf vercel.com mit deinem GitHub-Konto anmelden → **Add New… → Project** → Repository **LernTool** importieren.
2. Framework Preset: **Other**. Build-Befehl und Ausgabeordner stehen schon in `vercel.json` (`python3 bau.py` → `dist`).
3. Unter **Environment Variables** vier Einträge anlegen:

| Name | Wert |
|---|---|
| `SUPABASE_URL` | die Project URL aus Schritt 1 |
| `SUPABASE_SERVICE_KEY` | der service_role- bzw. secret-Schlüssel |
| `SITZUNG_GEHEIMNIS` | ein langer Zufallstext (mind. 20 Zeichen, z. B. aus einem Passwort-Generator) |
| `ADMIN_PASSWORT` | dein Passwort für die Code-Verwaltung (mind. 10 Zeichen) |

Beim erneuten Öffnen mit „Edit“ zeigt Vercel geheime Werte leer an – das ist normal, der Wert ist trotzdem gespeichert.
Ob alles angekommen ist, zeigt `https://<deine-adresse>/api/status` (nur „ok“/„fehlt“, nie die Werte).

4. **Deploy**. Danach bekommst du eine Adresse wie `lerntool.vercel.app` (unter Settings → Domains änderbar).

Jeder Push auf `main` baut die Seite automatisch neu. Neue oder geänderte Umgebungsvariablen gelten erst ab dem nächsten Bau – statt „Redeploy“ (fragt manchmal nach einem E-Mail-Code) reicht auch ein neuer Push.

## 3. Codes verkaufen
1. `https://<deine-adresse>/admin.html` öffnen, Admin-Passwort eingeben.
2. **Neue Codes**: Anzahl und Notiz (z. B. Name des Käufers) → **Erzeugen** → Code kopieren und weitergeben.
3. Die Liste zeigt je Code: auf welchen Geräten er angemeldet ist, wann zuletzt gelernt wurde.
   - **Geräte zurücksetzen**: wenn jemand ein neues Handy hat und nicht mehr an das alte kommt. Der Lernstand bleibt.
   - **Sperren**: Code funktioniert nicht mehr (z. B. weitergegeben).

## Gut zu wissen
- **Ohne Code gibt es keine Inhalte**: Alle Seiten und Daten liefert Vercel erst nach der Anmeldung aus.
- **Gleichzeitiges Lernen auf zwei Geräten** geht: Änderungen werden je Aufgabe zusammengeführt, nichts wird überschrieben.
  Gespeichert wird ein paar Sekunden nach jeder Änderung und beim Schließen der Seite; ohne Internet wird nachgeholt.
- **Wer vorher schon im Browser gelernt hat**, nimmt seinen Stand beim ersten Anmelden auf diesem Gerät mit.
- Pro Gerät bleibt man angemeldet (1 Jahr). Abmelden und fremde Geräte entfernen: in der App unter **Einstellungen → Konto**.
- Kosten: Supabase und Vercel sind für diese Größe kostenlos (Supabase pausiert Gratis-Projekte nach 7 Tagen ohne Nutzung –
  sobald jemand lernt, passiert das nicht).
- Das Claude-Artifact funktioniert weiter wie bisher (ohne Anmeldung, Lernstand nur im Browser).

## Rechtliches (bitte vor dem Verkauf klären)
- **Urheberrecht**: Die Inhalte beruhen auf den Vorlesungsfolien der Dozierenden. Folien gegen Geld weiterzugeben oder eng daran
  angelehnte Texte und Abbildungen zu verkaufen, kann deren Urheberrecht verletzen. Am sichersten: die Dozierenden bzw. die DHBW fragen.
- **Impressum und Datenschutzerklärung**: Eine Website, mit der man Geld verdient, braucht ein Impressum (§ 5 DDG) und – weil
  Gerätename und Lernstand gespeichert werden – eine Datenschutzerklärung (Supabase in Frankfurt, Vercel als Hoster).
- **Einnahmen**: Kleine Beträge sind meist als Kleinunternehmer möglich; ggf. Gewerbe anmelden.
