"""Begriffs-Check (intern, Skill /begriffs-check): Wird jeder Fachbegriff der Unterlagen auf der Lernseite ERKLÄRT – nicht nur erwähnt?
Ziel: In der Klausur darf kein Begriff auftauchen, den man nie gehört hat, und keine Definition verlangt werden, die nirgends steht.

Kandidaten aus den Unterlagen (Folien/Skript/Übungen, ohne durchgestrichene Seiten aus plan/folien_weg.json):
  · Begriffe in Definitionszusammenhang („Definition“, „versteht man“, „bezeichnet“, „heißt“, „bedeutet“, „Begriff“, „:“ am Zeilenanfang)
  · Abkürzungen (RAQSCI, TCO, EPRG …), Bindestrich-Komposita, lange Substantive (≥ 9 Buchstaben), englische Fachwörter (IKM)
Status je Begriff:
  FEHLT       kommt auf der Lernseite gar nicht vor                                  → erklären (oder begründet als nicht Stoff markieren)
  ERWÄHNT     kommt vor, aber nirgends erklärt (nicht fett, kein Glossar, keine Karte, keine Tabellen-Erstspalte, kein „heißt/ist/bedeutet“-Satz)
  ERKLÄRT     fett/Glossar/Karteikarte/Tabellenkopfzelle/Definitionssatz
  + Spalte F: Gibt es eine Frage/Aufgabe, in der der Begriff vorkommt?
Ausnahmen (geprüft, kein Fachbegriff oder bewusst nicht Stoff): inhalte/<fach>/plan/begriffe_ok.json {"Begriff": "Grund"}
Aufruf: python3 werkzeuge/begriffs_check.py <fach> [--alle] [--min-seiten 1] [--nur fehlt|erwaehnt]"""
import sys, re, json, html, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parents[1]
IN = ROOT / 'inhalte'
sys.path.insert(0, str(ROOT / 'werkzeuge'))
from folien_abgleich import QUELLE, norm, stamm, sammle  # noqa: E402

GENERISCH = set('''unternehmen beispiel beispiele vorlesung kapitel folie folien gliederung inhalt inhalte definition definitionen überblick einführung
zusammenfassung grundlagen aufgabe aufgaben lösung lösungen ergebnis ergebnisse literatur quelle quellen abbildung tabelle frage fragen antwort
übung übungen hinweis hinweise bedeutung möglichkeiten möglichkeit verfahren methode methoden beispielsweise unterschied unterschiede bereich bereiche
zeitpunkt entwicklung entwicklungen anforderungen voraussetzungen voraussetzung vorteile nachteile vorteil nachteil ansatzpunkte maßnahmen
mitarbeiter mitarbeitern kunden kunde produkte produkt markt märkte prozess prozesse informationen information situation ziele ziel strategie
strategien analyse analysen management organisation unternehmens unternehmen verhältnis verhältnisse aspekte aspekt wichtig wichtige
einheiten einheit menge mengen preise preis kosten zahlen zahl werte wert faktoren faktor gruppe gruppen beziehungen beziehung
semester studierende studierenden prüfung klausur minuten punkte termin termine teilnehmer professor'''.split())
DEF_CUE = re.compile(r'\b(definition|versteht man|bezeichnet|bezeichnung|heißt|hei[ßs]en|bedeutet|begriff|definiert|nennt man|spricht man|is defined|means|refers to|is called)\b', re.I)


def lade(fid, n):
    p = IN / fid / n
    return json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}


def quellen_seiten(fid):
    q = IN / fid / 'plan' / 'quellen'
    weg = {int(k) for k in lade(fid, 'plan/folien_weg.json')}
    from folien_abgleich import seiten_aus   # Folien ausgegrauter Unterthemen („kommt nicht dran“) zählen nicht
    weg |= {n for k in lade(fid, 'fach.json')['kapitel'] for t in k['themen'] if t.get('aus') for n in seiten_aus(t.get('src', ''))}
    seiten = []
    haupt = q / QUELLE[fid]
    for i, s in enumerate(haupt.read_text(encoding='utf-8').split('\f'), 1):
        if i not in weg: seiten.append((f'S.{i}', s))
    if fid == 'wima':   # Mathe: auch Gliederung und Übungsblätter (ohne Musterlösungen und Protokolle)
        for p in sorted(q.glob('*.txt')):
            if p.name == QUELLE[fid] or 'Musterl' in p.name or 'Weinberger' in p.name: continue
            seiten.append((p.stem.replace('Ubungsaufgaben_', 'Ü-'), p.read_text(encoding='utf-8')))
    return seiten


WORT = r"[A-ZÄÖÜ][A-Za-zÄÖÜäöüß]+(?:-[A-Za-zÄÖÜäöüß]+)*"


DEF_MUSTER = [
    r'[Uu]nter\s+(?:dem|der|den|einem|einer)?\s*(?P<t>[A-ZÄÖÜ][\w\-]+(?:\s+[A-ZÄÖÜa-zäöü][\w\-]+)?)\s+versteht\s+man',
    r'(?P<t>[A-ZÄÖÜ][\w\-]{3,}(?:\s+[A-ZÄÖÜ][\w\-]+)?)\s+(?:ist|sind|bezeichnet|bedeutet|beschreibt|umfasst|meint)\s+(?:die|der|das|ein|eine|den|dem|alle|jede)\b',
    r'(?:wird|werden)\s+(?:als|auch als)\s+(?P<t>[A-ZÄÖÜ][\w\-]+(?:\s+[A-ZÄÖÜ][\w\-]+)?)\s+bezeichnet',
    r'(?:heißt|heißen|nennt man|spricht man von)\s+(?:man\s+)?(?:eine[nm]?\s+|der\s+|die\s+|das\s+)?[„"]?(?P<t>[A-ZÄÖÜ][\w\-]{3,}(?:\s+[A-ZÄÖÜ][\w\-]+)?)',
    r'[Dd]efinition(?:\s+(?:von|der|des|nach))?[:\s]+[„"]?(?P<t>[A-ZÄÖÜ][\w\-]{3,}(?:[\s\-][A-ZÄÖÜ][\w\-]+)?)',
    r'(?<![\w,] )(?P<t>[A-Z][\w\-]+(?: [\w\-]+){0,2})\s+(?:is|are)\s+(?:defined as|the|a|an)\b',
]
RAUS = re.compile(r'https?:|www\.|@|©|Prof\. Dr\.|Vorlesung Marketing|^\s*(Quelle|Quellen|Literatur|Vgl\.|In Anlehnung|Abb\.|Archivbild|Source)', re.I)
NAMENSWOERTER = set('wannenwetsch gabler wikipedia arnolds heege oeldorf olfert kummer schulte steffenhagen meffert burmann kirchgeorg homburg bruhn weis sinus bme bmenet bvl chammout paul meier schneider kersten frisch weinberger springer kiehl münchen berlin wiesbaden mannheim heidelberg dortmund'.split())


def kandidaten(fid, seiten):
    kopf = collections.Counter(l.strip() for _, s in seiten for l in set(s.splitlines()) if l.strip())
    haeufig = {l for l, c in kopf.items() if c > 4}
    gefunden = collections.defaultdict(lambda: {'seiten': [], 'def': False, 'zeile': ''})
    def add(w, name, l, d):
        k = re.sub(r'\s+', ' ', w.strip(' -„"“”:'))
        if len(k) < 2 or norm(k) in GENERISCH or norm(k.split()[0]) in NAMENSWOERTER or norm(k).split()[-1] in GENERISCH: return
        g = gefunden[k]
        if name not in g['seiten']: g['seiten'].append(name)
        if d and not g['def']: g['def'] = True; g['zeile'] = re.sub(r'\s+', ' ', l.strip())[:110]
        elif not g['zeile']: g['zeile'] = re.sub(r'\s+', ' ', l.strip())[:110]
    for name, s in seiten:
        zeilen = [l for l in s.splitlines() if l.strip() and l.strip() not in haeufig and not RAUS.search(l)]
        text = re.sub(r'\s+', ' ', ' '.join(zeilen))
        for mu in DEF_MUSTER:
            for m in re.finditer(mu, text):
                add(m.group('t'), name, text[max(0, m.start() - 30):m.end() + 60], True)
        for l in zeilen:
            for w in re.findall(r'\b[A-Z][A-Z0-9]{1,6}\b', l):   # Abkürzungen
                if w not in ('DHBW', 'II', 'III', 'IV', 'VI', 'VII', 'VIII', 'IX', 'XI', 'USA', 'EUR', 'USD', 'DM', 'CEO', 'PDF', 'GE', 'ME', 'ZE', 'OK', 'TU'): add(w, name, l, False)
            for w in re.findall(r'\b[A-ZÄÖÜ][a-zäöüß]+(?:-[A-ZÄÖÜa-zäöüß][a-zäöüß]+)+\b', l):   # Bindestrich-Komposita
                add(w, name, l, False)
            for w in re.findall(r'\b[A-ZÄÖÜ][a-zäöüß]{11,}\b', l):   # lange Substantive (Komposita)
                add(w, name, l, False)
            m = re.match(r'\s*(?:[•▪■◦·\-–]|\d+[.)]|[a-z][.)])\s+([A-ZÄÖÜ][a-zäöüß]{4,}(?:[- ][A-ZÄÖÜ][a-zäöüß]+)?)', l)   # Begriff am Anfang eines Aufzählungspunkts
            if m: add(m.group(1), name, l, True)
    # lange Substantive nur, wenn sie auf ≥ 2 Seiten stehen oder in Definitionsnähe
    return {k: g for k, g in gefunden.items() if g['def'] or re.fullmatch(r'[A-Z][A-Z0-9]{1,6}', k) or '-' in k or len(g['seiten']) >= 2}


def lernseite(fid):
    fach = lade(fid, 'fach.json')
    roh = []; sammle(fach, roh); roh = ' '.join(roh)
    text = norm(roh)
    fett = norm(' '.join(re.findall(r'<b>(.*?)</b>', roh)) + ' ' + ' '.join(re.findall(r'<strong>(.*?)</strong>', roh)))
    zellen = norm(' '.join(re.findall(r'<td[^>]*>(.*?)</td>', roh)) + ' ' + ' '.join(re.findall(r'<th[^>]*>(.*?)</th>', roh)))
    gl = lade(fid, 'glossar.json').get('begriffe', [])
    karten = lade(fid, 'karten.json').get('karten', [])
    erkl = norm(' '.join(g['begriff'] for g in gl) + ' ' + ' '.join(c['v'] for c in karten))
    muster = []
    for g in gl:
        try: muster.append(re.compile(g.get('muster') or re.escape(g['begriff']), re.I))
        except re.error: pass
    saetze = re.split(r'(?<=[.!?])\s', text)
    fr = []; sammle([lade(fid, 'fragen.json'), lade(fid, 'fragen_neu.json'), lade(fid, 'aufgaben.json'), lade(fid, 'klausur.json')], fr)
    return dict(text=text, fett=fett, zellen=zellen, erkl=erkl, saetze=saetze, fragen=norm(' '.join(fr)), muster=muster)


def such(w):
    n = norm(w)
    s = stamm(n) if ' ' not in n else n
    return re.compile(r'(?<![a-z])' + re.escape(s[:max(4, len(s))]) if len(s) >= 4 else r'\b' + re.escape(n) + r'\b')


def status(w, L):
    if any(m.search(w) for m in L['muster']): return 'ERKLÄRT'
    r = such(w)
    if not r.search(L['text']):
        # Komposita: alle Teile vorhanden? (Bindestrich)
        teile = [t for t in norm(w).split('-') if len(t) > 3]
        if len(teile) > 1 and all(such(t).search(L['text']) for t in teile): return 'ERWÄHNT'
        return 'FEHLT'
    if r.search(L['fett']) or r.search(L['erkl']) or r.search(L['zellen']): return 'ERKLÄRT'
    if any(r.search(s) and re.search(r'\b(heisst|hei[ßs]t|ist|sind|bedeutet|bezeichnet|versteht man|einfach gesagt|means|is|are)\b', s) for s in L['saetze']): return 'ERKLÄRT'
    return 'ERWÄHNT'


def main():
    a = sys.argv[1:]
    fid = a[0]
    mins = int(a[a.index('--min-seiten') + 1]) if '--min-seiten' in a else 1
    nur = a[a.index('--nur') + 1] if '--nur' in a else None
    ok = lade(fid, 'plan/begriffe_ok.json')
    seiten = quellen_seiten(fid)
    kand = kandidaten(fid, seiten)
    L = lernseite(fid)
    zahl = collections.Counter()
    zeilen = []
    for w, g in sorted(kand.items(), key=lambda kv: (-kv[1]['def'], -len(kv[1]['seiten']), kv[0])):
        if len(g['seiten']) < mins and not g['def']: continue
        if w in ok or w[:40].strip() in ok: zahl['ok'] += 1; continue
        st = status(w, L)
        f = 'F' if such(w).search(L['fragen']) else '-'
        zahl[st] += 1
        if st == 'ERKLÄRT' and '--alle' not in a: continue
        if nur == 'fehlt' and st != 'FEHLT': continue
        if nur == 'erwaehnt' and st != 'ERWÄHNT': continue
        zeilen.append(f"{st:8} {f} {'D' if g['def'] else ' '} {w[:40]:40} {','.join(g['seiten'][:4]):22} | {g['zeile']}")
    print('\n'.join(zeilen))
    print(f"== {fid}: {sum(zahl.values())} Begriffe · erklärt {zahl['ERKLÄRT']} · nur erwähnt {zahl['ERWÄHNT']} · fehlt {zahl['FEHLT']} · als ok markiert {zahl['ok']}"
          f"   (D = steht in Definitionsnähe, F = kommt in Fragen/Aufgaben vor)")


if __name__ == '__main__':
    main()
