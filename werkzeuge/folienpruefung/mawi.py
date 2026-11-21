# Materialwirtschaft (Meier). Jeder Stichpunkt „fehlt vielleicht“ geprüft (13.11.2026). Die Lernseiten geben die Folien sehr vollständig wieder;
# die Treffer sind andere Wortformen (z. B. „Bestellrhythmusverfahren“ statt Schreibfehler „Bestellrythmus…“), Quellenangaben, Mitschrift-Reste
# oder Beispiellisten. Echte Lücke war nur die BVL-Logistikdefinition (werkzeuge/einarbeiten/mawi.py).
DECKNAME[F] = {'vl': 'Folien'}
KEIN = {2, 3, 13, 14, 15, 16, 22, 23, 54, 57, 67, 82, 84, 113, 114, 115, 116, 149, 153, 180, 181, 237, 241, 254, 263, 264, 266, 272, 273, 279, 292}
# 2/3: Mitschrift-Reste · 13–16/22/23: Quellen (Gabler, BVL-Netzwerk, Jünemann-Lebenslauf) · 54/57: Monatsnamen der Beispieltabelle
# 67/180/181: Literatur und Mitschrift · 113–116: Beispiellisten der Klassifikation (eCl@ss-Einträge) · 263/264/266: Eingabemaske des TCO-Tools
# übrige: Schreibfehler der Folien/Mitschrift (z. B. „Maschinenkoksten“, „Entricklung“)
import json as _j
_fo = _j.loads((IN / F / 'folien.json').read_text(encoding='utf-8'))
for _s in _fo['seiten']['vl']:
    if any(it[2] == 'fehlt' or it[2] in ('anders', 'kein') for it in _s.get('f') or []):
        (kein if _s['n'] in KEIN else ok)(F, f"vl/{_s['n']}", '*')
