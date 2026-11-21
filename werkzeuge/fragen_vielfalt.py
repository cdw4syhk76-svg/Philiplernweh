"""Mehr Abwechslung im Quiz: erzeugt je Unterthema neue Fragen aus den vorhandenen Inhalten.
  · Verknüpfen   (zuord): Begriff ↔ kurze Erklärung, aus Glossar und Karteikarten des Unterthemas
  · Reihenfolge  (reihe): Abläufe aus Pfeilketten (A → B → C) in Merksätzen/Kernsätzen und Fluss-Bausteinen
  · Lückentext   (luecke): Merksatz mit ausgeblendetem Fachbegriff
  (Beschriften aus vorhandenen Bildern ist abgeschaltet; Schaubild-Fragen werden von Hand gebaut)
Antworten bewusst kurz. Schreibt Familien mit „:v-“ in der ID nach inhalte/<fach>/fragen_neu.json (wiederholbar).
Aufruf: python3 werkzeuge/fragen_vielfalt.py"""
import json, pathlib, random, re, html
IN = pathlib.Path(__file__).resolve().parents[1] / 'inhalte'
FAECHER = ['bwl', 'mkt', 'wima', 'mawi', 'ikm', 'igt']
random.seed(7)


def txt(s): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s or ''))).strip()


def kurz(s, n=80):
    """erste Aussage, höchstens n Zeichen (an Wortgrenze)"""
    s = txt(s)
    s = re.split(r'(?<=[.!?])\s|\s[–—]\s|;\s', s)[0].strip()
    if len(s) > n:
        s = s[:n].rsplit(' ', 1)[0].rstrip(',:;–- ') + ' …'
    return s.rstrip('.')


def ohne_begriff(defi, begriff):
    """Erklärung darf den Begriff nicht verraten"""
    for w in {begriff, begriff.split(' (')[0]}:
        if len(w) > 3:
            defi = re.sub(re.escape(w), '…', defi, flags=re.I)
    return defi


def verknuepfen(f, tid, paare):
    """Familien „Verknüpfe Begriff und Erklärung“ (3–4 Paare je Frage)"""
    out = []
    random.shuffle(paare)
    for g in range(0, min(len(paare), 8), 4):
        teil = paare[g:g + 4]
        if len(teil) < 3:
            break
        out.append(dict(y='zuord', p='Verknüpfe: Welcher Begriff passt zu welcher Erklärung?', k=[b for b, _ in teil],
                        e=[[d, j] for j, (_, d) in enumerate(teil)], w='Jede Erklärung gehört zu genau einem Begriff.', lvl=1))
    return out


PFEIL = re.compile(r'\s*(?:→|->|►|⇒)\s*')


def reihen(texte):
    out = []
    for t in texte:
        for satz in re.split(r'(?<=[.!?])\s', txt(t)):
            teile = [x.strip(' .,;:') for x in PFEIL.split(satz)]
            if len(teile) < 3 or len(teile) > 7:
                continue
            # vorderen Satzteil vor dem ersten Schritt abschneiden („Ablauf: A → B“)
            teile[0] = re.split(r':\s*', teile[0])[-1]
            teile = [re.sub(r'^(?:\d+[.)]?|[IVX]+[.)])\s+', '', x).strip() for x in teile]   # Nummern würden die Lösung verraten
            if any(not x or len(x) > 45 or len(x.split()) > 6 for x in teile) or len(set(teile)) < len(teile):
                continue
            out.append(teile)
    return out


def luecken(merk, begriffe):
    m = txt(merk)
    treffer = [b for b in sorted(begriffe, key=len, reverse=True) if len(b) > 4 and re.search(r'\b' + re.escape(b) + r'\b', m)]
    if not treffer or len(m) > 260:
        return None
    wahl = treffer[:2]
    s = m
    for n, b in enumerate(wahl):
        s = re.sub(r'\b' + re.escape(b) + r'\b', f'[[{n}]]', s, count=1)
    if '[[0]]' not in s:
        return None
    l = [[b, b.lower()] for b in wahl if f'[[{wahl.index(b)}]]' in s]
    return dict(y='luecke', p=s, l=l, w=f'Merksatz: {m}', lvl=2)


TEXT = re.compile(r'<text([^>]*)>([^<]{2,28})</text>')


def beschriften(svg, sprache):
    """Hauptschaubild: 3–4 kurze Beschriftungen durch nummerierte Marken ersetzen"""
    if not svg or '<svg' not in svg or 'viewBox' not in svg:
        return None
    s = svg
    if sprache == 'en':   # zweisprachige Bilder: nur Englisch behalten
        s = re.sub(r'<text class="l-de"[^>]*>.*?</text>', '', s)
        s = s.replace('class="l-en" ', '')
    s = re.sub(r'<g class="tp[^"]*"[^>]*>', '<g>', s)
    kand = []
    for m in TEXT.finditer(s):
        attr, t = m.group(1), html.unescape(m.group(2)).strip()
        if 'l-de' in attr or not re.search(r'[A-Za-zÄÖÜäöü]{3}', t) or re.search(r'\d{2,}|[%€=]', t):
            continue
        x, y = re.search(r'\bx="([\d.]+)"', attr), re.search(r'\by="([\d.]+)"', attr)
        if x and y:
            kand.append((m.start(), m.end(), t, float(x.group(1)), float(y.group(1))))
    namen = [k[2] for k in kand]
    kand = [k for k in kand if namen.count(k[2]) == 1]
    if len(kand) < 4:
        return None
    wahl = sorted(random.sample(kand, min(4, len(kand) - 1)), key=lambda k: (k[4], k[3]))
    rest = [k[2] for k in kand if k not in wahl]
    neu, pos = [], 0
    for n, (a, e, t, x, y) in enumerate(sorted(wahl, key=lambda k: k[0])):
        nr = [w[0] for w in wahl].index(a) + 1
        neu.append(s[pos:a] + f'<g class="dg-m" data-m="{nr}"><circle cx="{x}" cy="{y - 4}" r="11" style="fill:var(--dg-a)"/>'
                   f'<text x="{x}" y="{y + 0.5}" text-anchor="middle" font-size="13" font-weight="800" style="fill:var(--dg-on)">{nr}</text></g>')
        pos = e
    neu.append(s[pos:])
    random.shuffle(rest)
    return dict(y='beschr', p='Beschrifte das Schaubild: Welcher Begriff gehört zu welcher Nummer?' if sprache == 'de' else 'Label the figure: which term belongs to which number?',
                slots=[k[2] for k in wahl], extra=rest[:2], bild=''.join(neu), w='', lvl=2)


NUR_EN = lambda h: re.sub(r'<(span|div) class="l-de"[^>]*>.*?</\1>', ' ', h or '', flags=re.S)
SCHLECHT = re.compile(r':|\b(Vorteil|Nachteil|Beispiel|Formel|Bedingung|Einstufung|example|advantage)', re.I)
def norm(b): return re.sub(r'[^a-zäöüß]', '', b.lower())[:7]


def fach(fid):
    d = json.loads((IN / fid / 'fach.json').read_text(encoding='utf-8'))
    if fid == 'produktion':   # Klausursprache Englisch: deutsche Fassung aus allen Feldern entfernen
        for k in d['kapitel']:
            for t in k['themen']:
                for f_ in ('title', 'kern', 'kurz', 'merk', 'article', 'fig'):
                    if isinstance(t.get(f_), str): t[f_] = NUR_EN(t[f_])
    gl = json.loads((IN / fid / 'glossar.json').read_text(encoding='utf-8'))['begriffe']
    karten = json.loads((IN / fid / 'karten.json').read_text(encoding='utf-8'))['karten'] if (IN / fid / 'karten.json').exists() else []
    sprache = 'en' if fid == 'produktion' else 'de'
    fams, zahl = [], {'zuord': 0, 'reihe': 0, 'luecke': 0, 'beschr': 0}
    for kn, k in enumerate(d['kapitel'], 1):
        for t in k['themen']:
            tid, a = t['id'], []
            paare, gesehen = [], set()
            for g in gl:
                if g.get('heimat') == tid:
                    b = txt(g['begriff']); dd = ohne_begriff(kurz(g['text']), b)
                    if 3 < len(b) <= 40 and len(dd) >= 12 and norm(b) not in gesehen and not SCHLECHT.search(b):
                        paare.append((b, dd)); gesehen.add(norm(b))
            for c in karten:
                if c['t'] == tid:
                    b = txt(c['v']); dd = ohne_begriff(kurz(c['r']), b)
                    if 3 < len(b) <= 34 and len(dd) >= 12 and '?' not in b and norm(b) not in gesehen and not SCHLECHT.search(b) and not b.startswith(('Merksatz', 'Nenne', 'Was ', 'Wie ')):
                        paare.append((b, dd)); gesehen.add(norm(b))
            a += verknuepfen(fid, tid, paare)
            for r in ([] if fid == 'mathe' else reihen([t.get('merk', ''), t.get('kern', ''), t.get('kurz', '')]))[:2]:
                a.append(dict(y='reihe', p=f'Bringe in die richtige Reihenfolge ({txt(t["title"])}).' if sprache == 'de' else f'Put in the right order ({txt(t["titel_text"])}).',
                              o=r, w=' → '.join(r), lvl=1))
            fl = [m for m in re.findall(r'<div class="d-flow">(.*?)</div>\s*(?=<(?!div><b))', t.get('article', ''), re.S)]
            for blk in re.findall(r'<div class="d-flow">((?:<div[^>]*><b>.*?</b>.*?</div>)+)</div>', t.get('article', ''), re.S)[:1]:
                schritte = [txt(x) for x in re.findall(r'<div[^>]*><b>(.*?)</b>', blk)]
                if 3 <= len(schritte) <= 7 and all(len(x) <= 45 for x in schritte):
                    a.append(dict(y='reihe', p=f'Bringe die Schritte in die richtige Reihenfolge ({txt(t["title"])}).' if sprache == 'de' else f'Put the steps in the right order ({txt(t["titel_text"])}).',
                                  o=schritte, w=' → '.join(schritte), lvl=1))
            lu = luecken(t.get('merk', ''), [txt(g['begriff']) for g in gl if g.get('heimat') == tid])
            if lu:
                a.append(lu)
            # Beschriften aus vorhandenen Bildern bewusst aus: deren Beschriftungen (Tooltips, zweisprachige Texte) lassen sich nicht sauber herauslösen
            for x in a:
                zahl[x['y']] += 1
            if a:
                fams.append(dict(id=f'{fid}:{tid}:v-vielfalt', f=fid, t=tid, k=kn, s=bool(t.get('star')), y='fam', fam=1,
                                 z='Begriffe, Abläufe und Schaubilder sicher zuordnen' if sprache == 'de' else 'Match terms, sequences and figures', a=a))
    p = IN / fid / 'fragen_neu.json'
    alt = json.loads(p.read_text(encoding='utf-8')) if p.exists() else {'hinweis': 'Neue Fragen-Familien (LernTool), ergänzen fragen.json', 'familien': []}
    alt['familien'] = [x for x in alt['familien'] if ':v-' not in x.get('id', '')] + fams
    p.write_text(json.dumps(alt, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(fid, len(fams), 'Familien', zahl)


if __name__ == '__main__':
    for f in FAECHER:
        fach(f)
