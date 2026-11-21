# Industriebetriebslehre (Krcal). Jeder Stichpunkt „fehlt vielleicht“ geprüft (13.11.2026). Das Fach wurde direkt aus dem Hauptskript gebaut;
# echte Folieninhalte (HGB-Fehlbetrag, Hinterhuber-Text, Typ/Variante/Komplexitätsmanagement, Kapitelüberschriften) sind eingearbeitet.
# Übrig sind Texterkennungsreste der handschriftlichen Mitschrift (z. B. „Brundland“, „Kuckuckschren“, „Furdistischer“), Ortsnamen der
# Werksstatistik (Folie 11) und Bildunterschriften. Durchgestrichene Folien: inhalte/ibl/plan/folien_weg.json.
DECKNAME[F] = {'sk': 'Hauptskript'}
ANDERS = {4, 6, 46, 49, 67}   # Kanbanprinzip, Prozess „zeitlogisch“, Homogenität, ökonomisches Konstrukt, Organigramm = Strukturbild: steht mit anderen Worten da
import json as _j
_fo = _j.loads((IN / F / 'folien.json').read_text(encoding='utf-8'))
for _s in _fo['seiten']['sk']:
    if any(it[2] == 'fehlt' or it[2] in ('anders', 'kein') for it in _s.get('f') or []):
        (ok if _s['n'] in ANDERS else kein)(F, f"sk/{_s['n']}", '*')
