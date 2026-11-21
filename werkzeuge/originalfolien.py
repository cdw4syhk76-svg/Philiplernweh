"""Originalfolien: Jede Seite der Unterlagen (Folien, Skript, Übungen) einer Stelle in LernWeh zuordnen.

Ergebnis je Fach: inhalte/<fach>/folien.json (wird gebaut) und die PDFs in inhalte/<fach>/folien/ (werden nach dist/folien/ kopiert).
Die App zeigt damit in „Originalfolien“ jede Seite, wie sie im PDF steht, und daneben, auf welcher Lernseite der Stoff steht
und ob die Übungsaufgaben als Aufgabe eingebaut sind.

So wird zugeordnet (wiederholbar, ohne Handarbeit):
  1. Seitentext: pdftotext; reine Scans per Texterkennung (tesseract, einmal, Zwischenspeicher inhalte/<fach>/plan/folien_text/).
  2. Verweise: Das Feld `src` jedes Unterthemas („Deck 2.1 · Folien 19–28“, „Skript S. 3–5“, „Fallstudien S. 12“) nennt Seiten.
     Foliennummer und PDF-Seite weichen je Deck oft um einen festen Betrag ab. Dieser Versatz wird je Deck geschätzt:
     der Versatz, bei dem die genannten Seiten am besten zum Text der Unterthemen passen.
  3. Textähnlichkeit (TF-IDF, Wortstämme) zwischen Seite und jedem Unterthema (Lerntext, Karten, Glossar).
     Verweis + Ähnlichkeit ergeben die Unterthemen einer Seite (höchstens drei).
  4. Stand: Wie viel vom Seitentext (gewichtet nach Seltenheit) steht auf den zugeordneten Lernseiten bzw. irgendwo im Fach.
     Kurze Seiten ohne Inhalt (Titel, Gliederung, Kopf) zählen als „ohne Lernstoff“; inhalte/<fach>/plan/folien_weg.json („durchgestrichen“) als „bewusst weggelassen“.
  5. Übungsblätter: Seiten werden an den Überschriften („Aufgabe 12“, „Übung“, „7. Fallstudie“) in Aufgaben zerlegt;
     jede Aufgabe wird mit den LernWeh-Aufgaben (aufgaben.json, Probeklausur-Bogen) verglichen, Zahlen zählen dabei stark.
     Nennt eine LernWeh-Aufgabe ihre Herkunft („Übung 20“), gilt das als sicher.

Keine Prozentzahlen in der App (Regel: Prozent nur aus Übungsklausur und Refresh) – nur Stufen.
Aufruf: python3 werkzeuge/originalfolien.py [fach …] [--bericht]"""
import sys, json, re, math, pathlib, subprocess, shutil, collections, hashlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
IN = ROOT / 'inhalte'
import unicodedata
def _nfc(p):
    """Pfad mit Umlauten finden, egal ob der Dateiname NFC oder NFD gespeichert ist (Hochladen über GitHub/macOS)"""
    p = pathlib.Path(p)
    if p.exists() or not p.parent.exists(): return p
    n = unicodedata.normalize('NFC', p.name)
    return next((q for q in p.parent.iterdir() if unicodedata.normalize('NFC', q.name) == n), p)
U = ROOT / 'unterlagen'
IW = next(iter(ROOT.glob('Industrielle Wertsch*')), ROOT / 'fehlt')   # neues Fach IBL (Ordner mit Umlaut, vom Nutzer hochgeladen)
MU = U / 'Mathe/uebungen'

# Decks je Fach: (id, Datei, Titel, Art, Verweis-Muster in src)
# Art: folien · skript · uebung · formeln · orga. Das Muster erkennt die Stelle in `src`, die dieses Deck meint.
# Nie aufnehmen: Altklausuren, Gedächtnisprotokolle, Definitionslisten mit Klausurfragen (Herkunft der Klausurdaten bleibt intern).
DECKS = {
    'bwl': [
        ('vl', U / 'ABWL/folien/Einführung in die Bwl_compressed.pdf', 'Einführung in die BWL (Vorlesungsfolien)', 'folien', r'Folien?'),
        ('zf', U / 'ABWL/folien/ABWL Zusammenfassung_Paul_WIN22B.pdf', 'Zusammenfassung ABWL', 'skript', r'Zusammenfassung'),
    ],
    'mkt': [('vl', U / 'Marketing/folien/Marketing_compressed.pdf', 'Vorlesung Marketing', 'folien', r'Folien?')],
    'mawi': [('vl', U / 'Materialwirtschaft/folien/Materialwirtschaft_compressed.pdf', 'Vorlesung Materialwirtschaft', 'folien', r'Folien?')],
    'ikm': [('sk', U / 'Interkulturelles Management/folien/interkulturelles Management _compressed.pdf', 'Script Intercultural Management', 'skript', r'Script')],
    'igt': [('vl', U / 'Internationale Geschaeftstaetigkeit/folien/Rahmenbedingungen internationaler Geschäftstätigkeit.pdf', 'Rahmenbedingungen internationaler Geschäftstätigkeit', 'folien', r'Folien?')],
    'wima': [
        ('gl', U / 'Mathe/folien/Vorlesung MA-WIN26 Gliederung.pdf', 'Gliederung der Vorlesung', 'skript', r'Gliederung'),
        ('ms', U / 'Mathe/folien/Einstieg _compressed.pdf', 'Mitschrift (Einstieg)', 'skript', r'Mitschrift'),
        *[(f'b{i}', (MU / 'Übungsaufgaben Blatt 9 (2 Aufgaben).pdf' if i == 9 else MU / f'Übungsaufgaben Blatt {i}.pdf'), f'Übungsblatt {i}', 'uebung', rf'Übungsblatt {i}\b') for i in range(1, 10)],
        *[(f'l{i}', MU / f'Übungsaufgaben Blatt {i} - Musterlösungen.pdf', f'Übungsblatt {i} · Musterlösung', 'uebung', None) for i in range(1, 6)],
        ('ana', MU / 'Übungsaufgaben Analysis I.pdf', 'Übungen Analysis I', 'uebung', r'Analysis I\b'),
        ('la', MU / 'Übungsaufgaben lineare Algebra.pdf', 'Übungen lineare Algebra', 'uebung', r'lineare Algebra'),
        ('oek', MU / 'Übungsaufgaben Ökonomische Funktionen.pdf', 'Übungen ökonomische Funktionen', 'uebung', r'ökonomische Funktionen'),
    ],
    'ibl': [
        ('sk', IW / 'Hauptskript-Industrielle Wertschöpfung.pdf', 'Hauptskript Industrielle Wertschöpfung', 'skript', r'Skript|Folien?'),
    ],
}
# Herkunft der Übungsaufgaben: welche LernWeh-Aufgabe gehört sicher zu welcher Aufgabe eines Übungsblatts ('<blatt>/<nr>': [Aufgaben-IDs]).
# Blatt = Deck-Kennung ohne Buchstaben (b1 und l1 sind Blatt 1 mit Musterlösung); 'la', 'oek', 'ana' wie die Decks.
HERKUNFT = {
    'wima': {'1/1': ['wima-terme-blatt1'], '1/2': ['wima-folgen-blatt1'], '1/3': ['wima-folgen'], '1/4': ['wima-folgen'],
             '1/5': ['wima-folgen-blatt1'], '2/4': ['wima-fa-b2a4'], '3/3': ['wima-fa-b3a34'], '3/4': ['wima-fa-b3a34'],
             '4/1': ['wima-fa-b4a1'], '4/3': ['wima-saettigung'], '4/5': ['wima-fa-b4a5'], '5/1': ['wima-blatt5'], '5/2': ['wima-blatt5', 'wima-ableitungen'], '5/3': ['wima-blatt5'],
             '6/4': ['wima-integrale'], '7/2': ['wima-blatt7-8'], '7/3': ['wima-matrizen'], '7/4': ['wima-produktion'],
             '8/2': ['wima-lgs-inverse'], '8/3': ['wima-blatt7-8'], '8/4': ['wima-lgs-inverse'], '9/1': ['wima-blatt9'],
             '7/5': ['l:lgs-gauss'], 'oek/1': ['wima-kosten-gewinn'], 'la/1': ['wima-lineare-algebra'], 'la/2': ['wima-lineare-algebra'], 'la/3': ['wima-lineare-algebra'],
             'la/4': ['wima-lineare-algebra'], 'la/5': ['wima-lineare-algebra']},
}
# Name eines Übungsdecks, wie er auf den Lernseiten in „Beispiel · <Name>, Aufgabe n“ steht
BLATT_NAME = {'oek': 'Übung ökonomische Funktionen', 'la': 'Übung lineare Algebra', 'ana': 'Übungen Analysis I'}

GLIEDERUNG = re.compile(r'(?:ABWL\s+)?(?:Gliederungsübersicht|Gliederung(?!\s+(?:der|nach|des|von))\b|Agenda\b|Inhaltsverzeichnis|Table of Contents|Roadmap\b|Formelsammlung \w+ Inhalt)', re.I)
ANDERE_SPRACHE = set()   # Folien englisch, Lernseiten deutsch: Wortvergleich taugt nicht, die Verweise der Lernseiten zählen
ART_NAME = {'orga': 'Vorlesungsfolien', 'folien': 'Vorlesungsfolien', 'skript': 'Skript', 'uebung': 'Übungen und Fallstudien', 'formeln': 'Formelsammlung'}

STOP = set('''paul chammout weinberger krcal kersten frisch aber alle allem allen aller alles also andere anderen anderer anders auch auf aus bei beim bereits besonders bitte bzw dabei dadurch dafür daher damit dann darauf daraus darin darum darüber dass dein deine dem den denen denn der deren des dessen deshalb die dies diese diesem diesen dieser dieses doch dort durch eben ebenfalls eher eigene eigenen ein eine einem einen einer eines einige einigen einmal etwa etwas euch eure für gegen gegenüber haben hat hier hinaus ihre ihrem ihren ihrer ihres immer innerhalb insbesondere ist jede jedem jeden jeder jedes jedoch jetzt kann kein keine keinen können könnte machen mehr mehrere meist mit muss müssen nach neben nicht noch nur oder ohne schon sehr sein seine seinem seinen seiner seit sich sie sind solche solchen soll sollen sollte sowie sowohl statt über unter usw viel viele vom von vor während was weitere weiteren welche welchen wenn werden wie wieder will wird wurde wurden zum zur zwar zwei drei vier fünf zwischen beispiel beispiele quelle quellen folie seite prof meier schneider stützer stuetzer stein schmidt dhbw mannheim abwl grundlagen bwl vorlesung kapitel aufgabe aufgaben lösung loesung
the and for with that this from are was were which have has had not but they their them these those there what when where who will would could should can may might into than then also such other more most some any each only very just about over under between within without upon your you our its his her him she use used using based example examples source page slide'''.split())


def norm(s):
    import html
    s = html.unescape(re.sub(r'<[^>]+>', ' ', s or ''))
    s = s.replace('\u00ad', '').replace('\u200b', '')
    return s.lower().replace('ß', 'ss').replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')


def stamm(w):
    for suf in ('ungen', 'ierung', 'ung', 'heit', 'keit', 'ern', 'en', 'er', 'es', 'em', 'e', 'n', 's'):
        if len(w) > len(suf) + 4 and w.endswith(suf): return w[:-len(suf)]
    return w


def toks(s):
    """Wortstämme (ohne Stoppwörter) und Zahlen (ab 3 Ziffern, ohne Tausenderpunkt) als Merkmale"""
    t = norm(s)
    out = [stamm(w) for w in re.findall(r'[a-z][a-z]{3,}', t) if w not in STOP]
    out += ['#' + z.replace('.', '').replace(',', '') for z in re.findall(r'\d{1,3}(?:\.\d{3})+(?:,\d+)?|\d{3,}(?:,\d+)?|\d+,\d+', t)]
    return out


def sammle(o, out):
    if isinstance(o, str): out.append(o)
    elif isinstance(o, dict):
        for k, v in o.items():
            if k not in ('id', 'thumb', 'fig', 'rel'): sammle(v, out)
    elif isinstance(o, list):
        for v in o: sammle(v, out)
    return out


def ohne_of(t):
    """Unterthema ohne die Ergänzungsblöcke aus der Folienprüfung (<!--of:…-->): gemessen wird, was ursprünglich auf der Lernseite stand"""
    return {**t, 'article': re.sub(r'<!--(of|df):([\w-]+)-->.*?<!--/\1:\2-->', '', t.get('article', ''), flags=re.S)}


def lade(fid, d):
    p = IN / fid / d
    return json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}


# ---------- Seitentext ----------
def seitentexte(fid, did, pdf):
    cache = IN / fid / 'plan' / 'folien_text'; cache.mkdir(parents=True, exist_ok=True)
    h = hashlib.sha1(pdf.read_bytes()).hexdigest()[:10]
    c = cache / f'{did}-{h}.json'
    if c.exists(): return json.loads(c.read_text(encoding='utf-8'))
    roh = subprocess.run(['pdftotext', '-layout', str(pdf), '-'], capture_output=True, text=True).stdout.split('\f')
    n = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', str(pdf)], capture_output=True, text=True).stdout).group(1))
    roh = (roh + [''] * n)[:n]
    leer = [i for i, s in enumerate(roh) if len(s.strip()) < 40]
    if leer and shutil.which('tesseract'):
        # Scans: Texterkennung je Seite (Ergebnis bleibt in plan/folien_text/ocr_<deck>/ liegen, intern).
        # Gedrehte Seiten: Liefert die Erkennung kaum echte Wörter, wird die Seite um 90°/180°/270° gedreht neu erkannt.
        tmp = cache / ('ocr_' + did); tmp.mkdir(exist_ok=True)
        alt = cache / ('_ocr_' + did)
        print(f'  Texterkennung {did}: {len(leer)} Seiten …', flush=True)
        for i in leer:
            t = tmp / f'{i + 1}.txt'
            if not t.exists() and (alt / t.name).exists(): shutil.copyfile(alt / t.name, t)
            if not t.exists():
                png = tmp / f'{i + 1}'
                subprocess.run(['pdftoppm', '-r', '150', '-gray', '-png', '-singlefile', '-f', str(i + 1), '-l', str(i + 1), str(pdf), str(png)], check=True)
                subprocess.run(['tesseract', str(png) + '.png', str(png), '-l', 'deu+eng'], capture_output=True)
            text = t.read_text(encoding='utf-8', errors='replace')
            rot = tmp / f'{i + 1}.rot'
            if not rot.exists() and guete(text) < 12:
                from PIL import Image
                png = tmp / f'{i + 1}.png'
                if not png.exists(): subprocess.run(['pdftoppm', '-r', '150', '-gray', '-png', '-singlefile', '-f', str(i + 1), '-l', str(i + 1), str(pdf), str(tmp / f'{i + 1}')], check=True)
                best, bg = text, guete(text)
                for w in (90, 180, 270):
                    q = tmp / f'{i + 1}_r{w}'
                    Image.open(png).rotate(w, expand=True).save(str(q) + '.png')
                    subprocess.run(['tesseract', str(q) + '.png', str(q), '-l', 'deu+eng'], capture_output=True)
                    x = pathlib.Path(str(q) + '.txt').read_text(encoding='utf-8', errors='replace')
                    if guete(x) > bg: best, bg = x, guete(x)
                    for e in (str(q) + '.png', str(q) + '.txt'): pathlib.Path(e).unlink(missing_ok=True)
                t.write_text(best, encoding='utf-8'); rot.write_text('ok'); text = best
            for e in tmp.glob(f'{i + 1}.png'): e.unlink()
            roh[i] = text
        shutil.rmtree(alt, ignore_errors=True)
    c.write_text(json.dumps(roh, ensure_ascii=False), encoding='utf-8')
    return roh


def aussagen(seite):
    """Seitentext (pdftotext -layout) in Aussagen zerlegen: Spalten trennen, umbrochene Zeilen derselben Spalte zusammenfügen,
    an Aufzählungszeichen und Satzenden neu beginnen."""
    bloecke = []   # [spalte, text, letzte_zeile]
    for nr, l in enumerate(seite.splitlines()):
        for m in re.finditer(r'\S(?:.*?\S)?(?=\s{3,}|\s*$)', l):
            frag, x = m.group(0), m.start()
            neu = re.match(r'^([-–•▪►●o*]|\d+[.)]|[a-z]\)|[IVX]+\.)\s', frag)
            ziel = next((b for b in reversed(bloecke) if abs(b[0] - x) <= 3 and b[2] == nr - 1), None)
            if ziel and not neu and not re.search(r'[.!?:]$', ziel[1]) and (frag[:1].islower() or len(ziel[1]) < 60):
                ziel[1] += ' ' + frag; ziel[2] = nr
            else: bloecke.append([x, frag, nr])
    out = []
    for _, t, _ in bloecke:
        t = re.sub(r'\s+', ' ', t).strip(' -–•▪►●*·;,|')
        for teil in re.split(r'(?<=[.!?])\s+(?=[A-ZÄÖÜ])', t):
            if len(teil) >= 12: out.append(teil)
    return out


_VOK = None
# großgeschriebene Satzanfänge und Füllwörter, die kein Fachbegriff sind
KEIN_BEGRIFF = set('hieraus daraus dadurch hierbei hierzu hiermit dabei wichtige wichtiger bekannte bekannten untersuchen beispiel beispiele beispielsweise insgesamt grundsaetzlich allgemein allgemeine weiterhin ausserdem zusaetzlich letztlich schliesslich naechste naechsten folgende folgenden erstens zweitens drittens moeglichkeiten'.split())


def guete(text):
    """Anzahl echter Wörter (aus den Lernseiten aller Fächer bekannt) – misst, ob die Texterkennung lesbaren Text geliefert hat"""
    global _VOK
    if _VOK is None:
        _VOK = set()
        for p in IN.glob('*/fach.json'): _VOK |= set(re.findall(r'[a-z]{4,}', norm(re.sub(r'<!--(of|df):([\w-]+)-->.*?<!--/\1:\2-->', '', p.read_text(encoding='utf-8'), flags=re.S))))   # ohne Ergänzungsblöcke
    return sum(1 for w in re.findall(r'[a-z]{4,}', norm(text)) if w in _VOK)


QUELLZEILE = re.compile(r'Quelle:|Quellen:|Source:|Sources:|Duale Hochschule|DBM\d{3}\b|\bSlide \d+|\bWS 20\d\d|Aufl\.|Auflage|Verlag|Prof\. ?Dr\.|Dr\.-Ing|\bFolie \d+|BAMA_|©|https?:|www\.|\bS\. \d+\.?\s*$|\b(?:19|20)\d\d\b.*\bS\. \d', re.I)


def ohne_kopf(seiten):
    """Zeilen, die auf vielen Seiten stehen (Kopf-/Fußzeilen), und Literatur-/Quellenzeilen entfernen"""
    k = lambda l: re.sub(r'\s+', ' ', l).strip()
    zc = collections.Counter(k(l) for s in seiten for l in set(s.splitlines()) if l.strip())
    grenze = max(3, len(seiten) * .2)
    return ['\n'.join(l for l in s.splitlines() if l.strip() and zc[k(l)] <= grenze and not QUELLZEILE.search(l)) for s in seiten]


# ---------- Verweise aus src ----------
def verweise(src, decks):
    """'Deck 2.1 · Folien 38–40 · Deck 2.2 · Folien 130–132' -> [(deck, {38,39,40}), (deck22, {130,131,132})]"""
    out, cur = [], None
    default = next((d for d in decks if d['muster'] and re.search(d['muster'], 'Folien 1')), None)
    for teil in re.split(r'\s*[·;|]\s*', src or ''):
        if re.search(r'\bBuch\b|Zusatz|Labor', teil): cur = 'nix'; continue
        for d in decks:
            if d['muster'] and re.search(d['muster'], teil) and not (d is default and re.match(r'\s*Folien?\b', teil) and cur not in (None, 'nix')):
                cur = d; break
        nums = set()
        for a, b in re.findall(r'(\d+)\s*(?:[–-]\s*(\d+))?', re.sub(r'Kap\.\s*\d+|Deck [\d.]+[a-zA-Z]?|VS I+|\(\d{4}\)|Tasks? [\d.]+(?:\s*[–-]\s*[\d.]+)?|critical incident [\d.]+|exercises? [\d.–-]+|Übungsblatt \d+|Blatt \d+|\bA\d+(?:\s*[–-]\s*A?\d+)?|[Aa]ufgaben? \d+', ' ', teil)):
            a, b = int(a), int(b or a)
            if 0 < a <= b and b - a < 60: nums.update(range(a, b + 1))
        d = cur if cur not in (None, 'nix') else (default if cur is None else None)
        if nums and d: out.append((d, nums))
    return out


LUECKEN = None   # --luecken: Zeilen von Folien „teilweise“/„kaum“, die auf den zugeordneten Lernseiten fehlen → plan/folien_luecken.json


def main():
    global LUECKEN
    arg = [a for a in sys.argv[1:] if not a.startswith('--')]
    bericht = '--bericht' in sys.argv
    for fid in arg or list(DECKS):
        if '--luecken' in sys.argv: LUECKEN = []
        baue(fid, bericht)
        if LUECKEN is not None:
            (IN / fid / 'plan' / 'folien_luecken.json').write_text(json.dumps(LUECKEN, ensure_ascii=False, indent=1), encoding='utf-8')
            print(f'{fid}: {len(LUECKEN)} Folien teilweise/kaum, {sum(len(x["zeilen"]) for x in LUECKEN)} Zeilen ohne Entsprechung → plan/folien_luecken.json')


def baue(fid, bericht):
    fach = lade(fid, 'fach.json')
    if not fach: return
    themen = [(k, t) for k in fach['kapitel'] for t in k['themen']]
    kap_von = {t['id']: k['id'] for k, t in themen}
    karten, glossar = lade(fid, 'karten.json').get('karten', []), lade(fid, 'glossar.json').get('begriffe', [])
    decks = []
    for did, pdf, titel, art, muster in DECKS[fid]:
        pdf = _nfc(pdf)
        if not pdf.exists() and (IN / fid / 'folien' / f'{did}.pdf').exists(): pdf = IN / fid / 'folien' / f'{did}.pdf'   # Kopie im Repo (lernubersicht nicht geklont)
        if not pdf.exists(): print(f'  {fid}/{did}: PDF fehlt ({pdf.name}), übersprungen'); continue
        decks.append(dict(id=did, pdf=pdf, titel=titel, art=art, muster=muster))
    for d in decks:
        d['roh'] = seitentexte(fid, d['id'], d['pdf'])
        d['text'] = ohne_kopf(d['roh'])
        d['tok'] = [toks(s) for s in d['text']]

    # Unterthemen: Merkmale mit TF-IDF
    T = {}
    for k, t in themen:
        teile = sammle(ohne_of(t), []) + sammle([c for c in karten if c.get('t') == t['id']], []) + sammle([g for g in glossar if g.get('heimat') == t['id']], [])
        T[t['id']] = collections.Counter(toks(' '.join(teile)))
    df = collections.Counter(w for c in T.values() for w in c)
    W2 = set(w for k, t in themen for w in toks(' '.join(sammle(t, []))))
    N = len(T)
    idf = lambda w: math.log((N + 1) / (df.get(w, 0) + .5))
    def vek(c):
        v = {w: (1 + math.log(n)) * idf(w) for w, n in c.items()}
        l = math.sqrt(sum(x * x for x in v.values())) or 1
        return {w: x / l for w, x in v.items()}
    TV = {tid: vek(c) for tid, c in T.items()}
    TX, TX2 = {}, {}
    for k, t in themen:
        rest = sammle([c for c in karten if c.get('t') == t['id']], []) + sammle([g for g in glossar if g.get('heimat') == t['id']], [])
        TX2[t['id']] = norm(' '.join(sammle(t, []) + rest)).replace('-', '')
        TX[t['id']] = norm(' '.join(sammle(ohne_of(t), []) + rest)).replace('-', '')
    FX, FX2 = ' '.join(TX.values()), ' '.join(TX2.values())
    fach_w2 = set(df) | W2
    def drin(w, menge, text):
        if w in menge: return True
        return len(w) >= 6 and w in text
    fach_w = set(df)
    def aehnlich(pv):
        return {tid: sum(x * tv.get(w, 0) for w, x in pv.items()) for tid, tv in TV.items()}

    for d in decks:
        d['vek'] = [vek(collections.Counter(tk)) for tk in d['tok']]
        d['sim'] = [aehnlich(v) if v else {} for v in d['vek']]

    # Verweise je Deck sammeln, Versatz (Foliennummer -> PDF-Seite) schätzen
    ver = collections.defaultdict(list)   # deck-id -> [(tid, nummer)]
    for k, t in themen:
        for d, nums in verweise(t.get('src', ''), decks):
            for n in nums: ver[d['id']].append((t['id'], n))
    for d in decks:
        pairs, n = ver.get(d['id'], []), len(d['text'])
        best, bv = 0, -1
        for off in range(-70, 71):
            s = sum(d['sim'][p - 1 + off].get(tid, 0) for tid, p in pairs if 0 <= p - 1 + off < n)
            s -= .002 * abs(off)   # bei Gleichstand: kleiner Versatz
            if s > bv: bv, best = s, off
        d['versatz'] = best if pairs else 0
        # Aufgedruckte Foliennummer („Folie 60“, „Slide 12“) gilt vor dem geschätzten Versatz: Decks verrutschen oft in der Mitte
        nr = {}
        for i, r in enumerate(d['roh']):
            m = re.findall(r'\b(?:Folie|Slide)\s+(\d{1,3})\b', r)
            if m: nr.setdefault(int(m[-1]), i)
        d['nr'] = nr if len(nr) >= n * .4 else {}
        d['verw'] = collections.defaultdict(set)
        for tid, p in pairs:
            i = d['nr'].get(p, p - 1 + d['versatz'])
            if 0 <= i < n: d['verw'][i].add(tid)

    LERN_ART = {t['id']: re.sub(r'<[^>]+>', ' ', t.get('article', '')) for k, t in themen}
    TITEL = {t['id']: re.sub(r'<[^>]+>', '', t.get('titel_text', '')) for k, t in themen}
    # Aufgaben in LernWeh (eigene Aufgaben, Probeklausur-Bogen)
    A = []
    for a in lade(fid, 'aufgaben.json').get('aufgaben', []):
        A.append(dict(id='a:' + a['id'], titel=a['titel'], unter=a['unter'], quelle=a.get('quelle', ''), tok=collections.Counter(toks(' '.join(sammle([a['titel'], a.get('ausgang', ''), a['teile']], []))))))
    for K in lade(fid, 'klausur.json').get('aufgaben', []):
        for T_ in K['teile']:
            for v in T_['varianten']:
                A.append(dict(id='k:' + v['id'], titel=K['titel'], unter=[v.get('unter')], quelle='', tok=collections.Counter(toks(' '.join(sammle([v.get('text', ''), v.get('loesung', '')], []))))))
    adf = collections.Counter(w for a in A for w in a['tok'])
    aidf = lambda w: math.log((len(A) + 1) / (adf.get(w, 0) + .5)) * (2.2 if w.startswith('#') else 1)

    def aufgabe_finden(text, nr, d):
        tk = collections.Counter(toks(text))
        # Überschrift der Aufgabe („Fall 2) Die Unternehmensnachfolge“): steht sie wörtlich in einer LernWeh-Aufgabe, ist es diese
        kopfz = re.sub(r'^\s*(Aufgabe|Übung(?:saufgabe)?|Fallstudie|Fallbeispiel|Fall|Frage|Teilfrage)?\s*\d*[.:)]?\s*', '', text.strip().splitlines()[0] if text.strip() else '', flags=re.I)
        kw = [w for w in toks(re.sub(r'\[|\]|\d+\s*Punkte', ' ', kopfz)) if not w.startswith('#')]
        if len(tk) < 3: return []
        ges = sum(aidf(w) for w in tk) or 1
        treffer = []
        for a in A:
            gem = sum(aidf(w) for w in tk if w in a['tok'])
            zahl = sum(1 for w in tk if w.startswith('#') and w in a['tok'])
            sc = gem / ges
            sicher = False
            m = re.search(r'Übung (\d+)', a['quelle'])
            if d['id'] == 'auf' and m and nr and int(m.group(1)) == nr: sicher = True
            for m2 in re.finditer(r'Übung (\d+)[^·]*?\b(?:und|,)\s*(\d+)', a['quelle']):
                if d['id'] == 'auf' and nr and int(m2.group(2)) == nr: sicher = True
            m3 = re.search(r'-ue(\d+)', a['id'])   # Probeklausur-Bogen: Kennung nennt die Übung (…-ue13d)
            if d['id'] == 'auf' and m3 and nr and int(m3.group(1)) == nr: sicher = True
            m4 = re.match(r'k:(\d)[a-z]?-probe', a['id'])
            if d['id'] == 'probe' and m4 and nr and int(m4.group(1)) == nr: sicher = True
            kopf_ok = bool(kw) and all(w in a['tok'] for w in kw) and sum(aidf(w) for w in kw) >= 3
            if kopf_ok and sc >= .2: sicher = True   # Überschrift passt und der Inhalt auch
            if sicher or (sc >= .34 and zahl >= 2) or sc >= .5 or kopf_ok:
                treffer.append((1 if sicher else 0, sc, a))
        treffer.sort(key=lambda x: (-x[0], -x[1]))
        out = [dict(id=a['id'], titel=a['titel'], st='drin' if (s or sc >= .42) else 'aehnlich') for s, sc, a in treffer[:3]]
        # sicher zugeordnet (HERKUNFT) und Beispiele auf der Lernseite („Beispiel · Übungsblatt 2, Aufgabe 2“)
        blatt = re.sub(r'^[bl](?=\d)', '', d['id'])
        if nr is not None:
            sicher_ = ['a:' + x for x in HERKUNFT.get(fid, {}).get(f'{blatt}/{nr}', [])]
            out = [dict(id=a['id'], titel=a['titel'], st='drin') for i in sicher_ for a in A if a['id'] == i] + [o for o in out if o['id'] not in sicher_]
            out += [dict(id=i, titel='Beispiel auf der Lernseite: ' + TITEL[i[2:]], st='drin') for i in sicher_ if i.startswith('a:l:') and i[4:] in TITEL for i in [i[2:]]]
            name = BLATT_NAME.get(blatt, f'Übungsblatt {blatt}')
            for tid_, art_ in LERN_ART.items():
                if re.search(re.escape(name) + r',? Aufgaben? ' + str(nr) + r'(?!\d)', art_):
                    out.append(dict(id='l:' + tid_, titel='Beispiel auf der Lernseite: ' + TITEL[tid_], st='drin'))
        return out[:3]

    ergebnis = dict(stand=None, decks=[], seiten={})
    pg = IN / fid / 'plan' / 'folien_geprueft.json'   # einzeln geprüft (werkzeuge/originalfolien_ergaenzungen.py)
    gp_roh = json.loads(pg.read_text(encoding='utf-8')) if pg.exists() else {}
    geprueft = {k: dict(x.split(':', 1)[::-1] for x in v) for k, v in gp_roh.get('geprueft', {}).items()}   # stelle -> {begriff: grund}
    nicht_kl = gp_roh.get('nicht_klausur', {})
    weg = {int(k): v for k, v in lade(fid, 'plan/folien_weg.json').items()} if (IN / fid / 'plan/folien_weg.json').exists() else {}
    zaehl = collections.Counter()
    for d in decks:
        seiten, kopf = [], re.compile(r'^\s*(Aufgabe\s+\d+|Übung(?:saufgabe)?\b|Übungen\b|Fallstudie\b|Fallbeispiel\b|\d{1,2}\.\s*Fall(?:studie|beispiel)|[a-e]\)\s*Fallbeispiel|Fall \d+\)|Frage \d+|Teilfrage [a-e]\))', re.M | re.I)
        offen_nr = None; letzte = None
        _k = [re.sub(r'\W+', '', norm(x))[:400] for x in d['text']]
        wiederholt = [d['art'] in ('folien', 'skript') and _k.count(x) > 1 for x in _k]   # gleicher Text auf mehreren Seiten: Gliederungs-/Agendafolie
        for i, s in enumerate(d['text']):
            tk = d['tok'][i]
            inh = set(w for w in tk if not w.startswith('#'))
            sim = d['sim'][i]
            kand = {tid: v + (.25 if tid in d['verw'].get(i, ()) else 0) for tid, v in sim.items()}
            top = sorted(kand.items(), key=lambda x: -x[1])
            mx = top[0][1] if top else 0
            gew = [tid for tid, v in top[:3] if v >= max(.12, mx * .7)]
            for tid in d['verw'].get(i, ()):
                if tid not in gew and sim.get(tid, 0) >= .05: gew.append(tid)
            gew = gew[:3]
            # Stand
            wsum = sum(idf(w) for w in inh) or 1
            lok = set().union(*[T[t] for t in gew]) if gew else set()
            nb = set().union(*[T[u] for u in T if kap_von[u] in {kap_von[t] for t in gew}]) if gew else set()
            ltx = ' '.join(TX[u] for u in T if gew and kap_von[u] in {kap_von[t] for t in gew})
            # zeilenweise wie /folien-abgleich: eine Zeile gilt als abgedeckt, wenn 60 % ihrer Wörter dort stehen
            def zeilen(menge, text):
                ok = alle = 0
                for l in s.splitlines():
                    ws = [w for w in toks(l) if not w.startswith('#')]
                    if len(ws) < 2: continue
                    alle += 1; ok += sum(drin(w, menge, text) for w in ws) / len(ws) >= .6
                return ok / alle if alle else 1
            lm = lok | nb
            cov_l, cov_g = zeilen(lm, ltx), zeilen(fach_w, FX)
            if (i + 1) in weg and d['art'] in ('folien', 'skript'): z = 'weg'
            elif d['art'] == 'orga' or (len(inh) >= 6 and wiederholt[i]) or GLIEDERUNG.match(re.sub(r'\s+', ' ', s).strip()): z = 'titel'   # Gliederung, Agenda, Inhaltsverzeichnis: kein Lernstoff
            elif len(inh) < 6: z = 'voll' if d['verw'].get(i) else 'titel'   # wenig Text: Bild-Folie, die eine Lernseite ausdrücklich nennt, gilt als zugeordnet
            elif cov_l < .5 and re.search(r'\b(Gliederung|Gliederungsübersicht|Literatur|Literaturhinweise|Modulbeschreibung|Agenda|Inhaltsverzeichnis|Table of Contents|Contents|Overview of the lecture|Literature|References|Syllabus|Timing|Educational Objectives|Context|Menti\.com|Thank you|Vielen Dank|Organisatorisches)\b', s[:160], re.I): z = 'titel'
            elif gew and (cov_l >= .7 or (cov_l >= .6 and cov_g >= .85)): z = 'voll'
            elif gew and cov_g >= .45: z = 'teil'
            else: z = 'offen'
            if fid in ANDERE_SPRACHE and z in ('teil', 'offen') and d['verw'].get(i):   # Folie englisch, Lernseite deutsch: Verweis zählt
                z = 'voll' if cov_l >= .15 or len(d['verw'][i]) else 'teil'
            if z in ('titel', 'offen') and len(inh) < 6: gew = [t for t in gew if t in d['verw'].get(i, ())]
            eintrag = dict(n=i + 1, z=z, t=gew)
            if f"{d['id']}/{i + 1}" in nicht_kl: eintrag['nk'] = nicht_kl[f"{d['id']}/{i + 1}"]
            # Was fehlt? Aussagen der Seite, in denen ein Fachbegriff auf der Lernseite (bzw. im Fach) nicht vorkommt
            if z in ('voll', 'teil', 'offen') and fid not in ANDERE_SPRACHE and d['art'] != 'uebung':
                vm, vt = (lm, ltx) if gew else (fach_w, FX)
                fehlt, gesehen = [], set()
                for satz in aussagen(s):
                    ws = [w for w in toks(satz) if not w.startswith('#')]
                    if len(ws) < 2 or satz.lower() in gesehen: continue
                    miss = {w for w in ws if not drin(w, vm, vt)}
                    if len(miss) / len(ws) <= .34: continue
                    woerter = re.findall(r'[A-Za-zÄÖÜäöüß][\wÄÖÜäöüß-]*', satz)
                    if sum(bool(re.fullmatch(r'[A-ZÄÖÜa-zäöüß][a-zäöüß]+(?:-[A-Za-zÄÖÜäöüß]+)*', w)) for w in woerter) / len(woerter) < .7: continue   # Texterkennungs-Reste
                    guete('')   # Wortschatz aller Lernseiten laden
                    fach = sorted({w for w in woerter if any(t in miss and not drin(t, fach_w, FX) for t in toks(w)) and norm(w) not in _VOK and norm(w) not in KEIN_BEGRIFF
                                   and ((w[0].isupper() and len(w) >= 7) or '-' in w[1:])}, key=len, reverse=True)   # Fachbegriff, der nirgends in LernWeh vorkommt
                    if not fach: continue
                    # Stand je Begriff: fehlt · erg (ergänzt, steht jetzt gold im Text der Lernseite) · anders · kein
                    gp = geprueft.get(f"{d['id']}/{i + 1}", {})
                    def stand(x):
                        if x in gp: return gp[x]
                        if '*' in gp: return gp['*']
                        return 'erg' if all(drin(t, fach_w2, FX2) for t in toks(x) if not t.startswith('#')) else 'fehlt'
                    st = {x: stand(x) for x in fach}
                    gesamt = 'fehlt' if 'fehlt' in st.values() else 'erg' if 'erg' in st.values() else 'anders' if 'anders' in st.values() else 'kein'
                    gesehen.add(satz.lower())
                    fehlt.append([satz[:180] + ('…' if len(satz) > 180 else ''), [x for x in fach if st[x] == 'fehlt'][:5] or fach[:5], gesamt])
                    if len(fehlt) >= 14: break
                if fehlt: eintrag['f'] = fehlt
            if bericht: eintrag['_c'] = f'{cov_l:.2f}/{cov_g:.2f}'
            if LUECKEN is not None and z in ('teil', 'offen') and d['art'] != 'uebung':   # --luecken: Zeilen, die auf den zugeordneten Lernseiten fehlen
                fz = []
                for l in s.splitlines():
                    ws = [w for w in toks(l) if not w.startswith('#')]
                    if len(ws) >= 2 and sum(drin(w, lm, ltx) for w in ws) / len(ws) < .6: fz.append(l.strip())
                LUECKEN.append(dict(stelle=f"{d['id']}/{i + 1}", z=z, t=gew, zeilen=fz))
            # Übungen: Aufgaben auf der Seite
            if d['art'] == 'uebung':
                aufg = []
                stellen = [m for m in kopf.finditer(s)]
                if stellen:
                    for j, m in enumerate(stellen):
                        stueck = s[m.start(): stellen[j + 1].start() if j + 1 < len(stellen) else len(s)]
                        if j + 1 == len(stellen) and i + 1 < len(d['text']) and not kopf.search(d['text'][i + 1][:200]):
                            stueck += '\n' + d['text'][i + 1]   # Aufgabe läuft auf der nächsten Seite weiter
                        zeile = stueck.strip().splitlines()[0].strip()
                        nrm = re.match(r'(?:Aufgabe|Übung)\s+(\d+)', zeile)
                        nr = int(nrm.group(1)) if nrm else None
                        offen_nr = nr
                        tr = aufgabe_finden(stueck, nr, d)
                        sv = aehnlich(vek(collections.Counter(toks(stueck))))
                        stoff = [tid for tid, v in sorted(sv.items(), key=lambda x: -x[1])[:2] if v >= .06]
                        if tr: stoff = list(dict.fromkeys([u for a in A if a['id'] == tr[0]['id'] for u in a['unter'] if u in T] + stoff))[:2]
                        aufg.append(dict(l=re.sub(r'\s{2,}', ' ', zeile)[:90], a=tr, t=stoff))
                else:
                    tr = aufgabe_finden(s, None, d) if len(inh) >= 6 else []
                    if not tr and letzte and letzte['a']: aufg.append(dict(l=letzte['l'], a=letzte['a'], t=letzte['t'] or gew[:2], f=1))   # Fortsetzung
                    elif tr or len(inh) >= 6: aufg.append(dict(l=letzte['l'] if letzte else '', a=tr, t=gew[:2], f=1))
                if aufg and not aufg[-1].get('f'): letzte = aufg[-1]
                elif aufg and aufg[-1]['a'] and not letzte: letzte = aufg[-1]
                eintrag['a'] = aufg
                if aufg and not eintrag['t']: eintrag['t'] = list(dict.fromkeys(t for x in aufg for t in x['t']))[:3]
                if aufg and z in ('offen', 'teil') and all(any(a['st'] == 'drin' for a in x['a']) for x in aufg): eintrag['z'] = z = 'voll'
                for x in aufg:
                    zaehl['aufg_' + ('drin' if any(a['st'] == 'drin' for a in x['a']) else 'aehnlich' if x['a'] else 'keine')] += 1
            # Suchtext (gekürzt)
            eintrag['x'] = re.sub(r'\s+', ' ', re.sub(r'[\ufffd\x00-\x08\x0b-\x1f\ue000-\uf8ff]', ' ', s)).strip()[:500]   # ohne Ersatz- und Steuerzeichen aus der PDF
            seiten.append(eintrag)
            zaehl[z] += 1
        ergebnis['decks'].append(dict(id=d['id'], titel=d['titel'], art=d['art'], gruppe=ART_NAME[d['art']], datei=f'folien/{fid}/{d["id"]}.pdf', n=len(seiten)))
        ergebnis['seiten'][d['id']] = seiten
        ziel = IN / fid / 'folien'; ziel.mkdir(exist_ok=True)
        if d['pdf'] != ziel / f'{d["id"]}.pdf' and (not (ziel / f'{d["id"]}.pdf').exists() or (ziel / f'{d["id"]}.pdf').read_bytes() != d['pdf'].read_bytes()):
            shutil.copyfile(d['pdf'], ziel / f'{d["id"]}.pdf')
        if bericht:
            print(f'--- {fid}/{d["id"]} {d["titel"]}: {len(seiten)} Seiten, Versatz {d["versatz"]:+d}, aufgedruckte Nummern {len(d["nr"])}')
            for e in seiten:
                print(f"  {e['n']:3d} {e['z']:5s} {e.pop('_c', ''):9s} {','.join(e['t'])[:50]:50s} {e['x'][:70]}")
                for x in e.get('a', []): print(f"        ▸ {x['l'][:50]:50s} → {'; '.join(a['st'] + ':' + a['id'] for a in x['a']) or '–'}  (Stoff: {','.join(x['t'])})")
    # alte PDFs von entfernten Decks weg
    for p in (IN / fid / 'folien').glob('*.pdf'):
        if p.stem not in {d['id'] for d in decks}: p.unlink()
    ergebnis['stand'] = __import__('datetime').date.today().isoformat()
    (IN / fid / 'folien.json').write_text(json.dumps(ergebnis, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    print(f'{fid}: {len(decks)} Unterlagen, {sum(len(v) for v in ergebnis["seiten"].values())} Seiten · ' + ', '.join(f'{k} {v}' for k, v in sorted(zaehl.items())))


if __name__ == '__main__':
    main()
