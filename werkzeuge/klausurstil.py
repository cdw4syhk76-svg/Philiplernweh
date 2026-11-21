"""Aufgaben im Klausurstil für Unterthemen, zu denen es keine/wenige Klausuraufgaben gibt.
Quelle: Karteikarten des Unterthemas (Aufzählungen, Vergleiche, Fragen, Begriffe) und vorhandene Rechenfragen.
Stil je Prüfer (Logistik/Marketing: „Nennen (und erklären) Sie n …“, „Unterscheiden Sie …“, „Erklären Sie …“; Rechnen mit Rechenweg).
Aufgabenstellungen von Hand geprüft: werkzeuge/klausurstil_<fach>.json („Vorderseite“: {"nennen": "…", "erklaeren": "…"} oder null = weglassen).
Familien „:ks-…“ (klausur: True, stil: 1) → inhalte/<fach>/fragen_neu.json. Wiederholbar.
Aufruf: python3 werkzeuge/klausurstil.py [fach] [--liste]"""
import sys, json, re, sys, html, hashlib, pathlib
W = pathlib.Path(__file__).parent; IN = W.parent / 'inhalte'
def txt(s): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s or ''))).strip()
ZAHL = {2: 'zwei', 3: 'drei', 4: 'vier', 5: 'fünf', 6: 'sechs', 7: 'sieben', 8: 'acht', 9: 'neun', 10: 'zehn'}
ZIEL = 4          # so viele Klausurstil-Aufgaben je Unterthema anstreben
MAX_NEU = 6       # höchstens so viele neue Familien je Unterthema
FORMEL = re.compile(r'[=÷√·×]|\bx_|Formel')
KW = r'Merkmale|Vorteile|Nachteile|Ziele|Aufgaben|Arten|Funktionen|Bestandteile|Gründe|Ursachen|Folgen|Maßnahmen|Kriterien|Schritte|Voraussetzungen|Phasen|Elemente|Formen|Beispiele|Risiken|Chancen|Typen|Stufen|Komponenten|Module'


def schluessel(s, n=4):
    w = [x for x in re.findall(r'[A-ZÄÖÜ][\wäöüß-]{4,}|[\wäöüß-]{10,}', txt(s)) if x.lower() not in {'beispiel', 'zusatz', 'material', 'unternehmen'}]
    return list(dict.fromkeys(w))[:n]


def split_ausser_klammer(b, sep):
    out, tiefe, cur, i = [], 0, '', 0
    while i < len(b):
        if b[i] in '([': tiefe += 1
        if b[i] in ')]': tiefe = max(0, tiefe - 1)
        if not tiefe and b.startswith(sep, i): out.append(cur); cur = ''; i += len(sep); continue
        cur += b[i]; i += 1
    return out + [cur]


def teile(back):
    b = txt(back.replace('\n', ' / '))
    for sep in (' / ', '; ', ', '):
        t = [x.strip(' .') for x in split_ausser_klammer(b, sep) if x.strip(' .')]
        if len(t) >= 3 and all(len(x) <= 70 for x in t): return t
    return []


def art(c):
    v, r = txt(c['v']), c['r']
    if FORMEL.search(r) or FORMEL.search(v): return None
    if re.search(r'\bvs\.?\b|Unterschied', v) and len(re.split(r'\n| / ', txt(r.replace('\n', ' / ')))) >= 2: return 'vergleich'
    if v.endswith('?'): return 'frage'
    if teile(r): return 'liste'
    if len(v) <= 40 and len(txt(r)) >= 30 and not re.search(r'\d{4}', v): return 'begriff'
    return None


def vorschlag(c):
    """automatische Aufgabenstellung (wird von Hand geprüft)"""
    v = re.sub(r'\s*\((Auswahl|Beispiele|Zusatz)\)', '', txt(c['v'])).strip(); a = art(c)
    if a == 'liste':
        n = min(len(teile(c['r'])), 8); z = ZAHL.get(n, str(n))
        m = re.match(r'^(.*?):\s*(' + KW + r')$', v)
        if m: return dict(nennen=f'Nennen Sie {z} {m.group(2)} von {m.group(1)}.', erklaeren=f'Nennen und erklären Sie die {m.group(2)} von {m.group(1)}.')
        if re.match(r'^(\d+|zwei|drei|vier|fünf|sechs|sieben|acht|neun|zehn)\s', v, re.I):
            v2 = re.sub(r'^\S+\s', '', v); return dict(nennen=f'Nennen Sie die {z} {v2}.', erklaeren=f'Nennen und erklären Sie die {z} {v2}.')
        if re.match(r'^(' + KW + r')\b', v): return dict(nennen=f'Nennen Sie {z} {v}.', erklaeren=f'Nennen und erklären Sie {z} {v}.')
        return dict(nennen=f'{v}: Nennen Sie {z} Punkte.', erklaeren=f'{v}: Nennen und erklären Sie die Punkte.')
    if a == 'vergleich': return dict(erklaeren=f'Unterscheiden und erklären Sie: {re.sub(r" vs\.? ", " und ", v)}.')
    if a == 'frage': return dict(erklaeren=v)
    if a == 'begriff': return dict(erklaeren=f'Erklären Sie „{v}“' + (' und nennen Sie ein Beispiel.' if re.search(r'z\. ?B\.|Beispiel|\(', c['r']) else '.'))
    return None


def familie(fid, t, kn, c, auf):
    a = art(c); r = c['r']; out = []
    if a == 'liste':
        items = teile(r); n = min(len(items), 8)
        if auf.get('nennen'): out.append(dict(y='liste', p=auf['nennen'], pk=[[x] + schluessel(x, 2) for x in items], n=n, w='', klausur=True, stil=1, lvl=3))
        if auf.get('erklaeren'): out.append(dict(y='rev', p=auf['erklaeren'], l=f'<ul>{"".join(f"<li>{x}</li>" for x in items)}</ul>',
                                                 pk=[re.split(r'[:(]', x)[0].strip()[:40] for x in items][:8], w='', klausur=True, stil=1, lvl=3))
    elif a in ('vergleich', 'frage', 'begriff') and not auf.get('erklaeren'):
        pass
    elif a == 'vergleich':
        seiten = [x for x in re.split(r'\n| / ', r) if x.strip()]
        out.append(dict(y='rev', p=auf['erklaeren'], l='<br>'.join(seiten), pk=[re.split(r'[:(]', s)[0].strip()[:40] for s in seiten][:4], w='', klausur=True, stil=1, lvl=3))
    elif a in ('frage', 'begriff'):
        out.append(dict(y='rev', p=auf['erklaeren'], l=r, pk=schluessel(r, 3) or [txt(r)[:40]], w='', klausur=True, stil=1, lvl=3))
    if not out: return None
    h = hashlib.sha1(txt(c['v']).encode()).hexdigest()[:6]
    z = f'Can answer in exam form: {txt(c["v"])}' if fid == 'ikm' else f'Kann in Klausurform antworten: {txt(c["v"])}'
    return dict(id=f'{fid}:{t}:ks-{h}', f=fid, t=t, k=kn, s=False, y='fam', fam=1, z=z, a=out)


def fach(fid, liste=False):
    lies = lambda n: json.loads((IN / fid / n).read_text(encoding='utf-8'))
    d = lies('fach.json'); fr = lies('fragen.json'); alt = (fr['familien'] if isinstance(fr, dict) else fr)
    p = IN / fid / 'fragen_neu.json'; neu = json.loads(p.read_text(encoding='utf-8'))
    alt_ks = [x for x in neu['familien'] if ':ks-' in x.get('id', '')]   # bisherige Klausurstil-Familien (Lernstand) bleiben erhalten
    neu['familien'] = [x for x in neu['familien'] if ':ks-' not in x.get('id', '')]
    fams = alt + neu['familien']
    po = W / f'klausurstil_{fid}.json'; hand = json.loads(po.read_text(encoding='utf-8')) if po.exists() else {}
    karten = [c for c in lies('karten.json')['karten'] if not c.get('b') and c.get('q') not in ('ml', 'kp')]
    kv = {}
    for A in lies('klausur.json')['aufgaben']:
        for T in A['teile']:
            for v in T['varianten']: kv[v['unter']] = kv.get(v['unter'], 0) + 1
    auf = lies('aufgaben.json')['aufgaben'] if (IN / fid / 'aufgaben.json').exists() else []
    neue, rechnen, offen = [], 0, {}
    for kn, k in enumerate(d['kapitel'], 1):
        for t in k['themen']:
            if t.get('aus'): continue   # ausgegraut („kommt nicht dran“): keine Fragen, keine Lücke
            tid = t['id']; F = [f for f in fams if f.get('t') == tid]
            hat = sum(1 for f in F for a in f['a'] if a.get('klausur') and not a.get('stil') or (a.get('stil') and a['y'] == 'num')) + kv.get(tid, 0) + sum(1 for A in auf if tid in A['unter'] and A.get('klausur'))
            if hat >= ZIEL: continue
            for f in F:   # vorhandene Rechenfragen mit wechselnden Zahlen sind Klausurstil (Rechnen mit Rechenweg)
                for a in f['a']:
                    if hat < ZIEL and a['y'] == 'num' and a.get('gen') and (a.get('lvl') or 1) >= 2 and not a.get('klausur'):
                        a['klausur'] = True; a['stil'] = 1; hat += 1; rechnen += 1
            kk = sorted([c for c in karten if c['t'] == tid and art(c)], key=lambda c: ['liste', 'vergleich', 'frage', 'begriff'].index(art(c)))
            n = 0
            for c in kk:
                if hat >= ZIEL + 2 or n >= MAX_NEU: break
                key = txt(c['v'])
                if key in hand and hand[key] is None: continue
                a = hand.get(key) or vorschlag(c)
                if key not in hand: offen[key] = vorschlag(c)
                fam = familie(fid, tid, kn, c, a)
                if fam: neue.append(fam); hat += len(fam['a']); n += 1
    ids_neu = {f['id'] for f in neue}
    tids = {t['id'] for k in d['kapitel'] for t in k['themen']}
    kh = {hashlib.sha1(txt(c['v']).encode()).hexdigest()[:6] for c in karten}
    neue += [f for f in alt_ks if f['id'] not in ids_neu and f.get('t') in tids and f['id'].rsplit('ks-', 1)[1] in kh]
    pf = W / f'klausurstil_{fid}_fest.json'   # von Hand korrigierte Fassungen ganzer Familien (z. B. nach Meldungen): ersetzen das Erzeugte
    if pf.exists():
        fest = json.loads(pf.read_text(encoding='utf-8'))
        for f in neue:
            if f['id'] in fest: f['a'] = fest[f['id']]
    neu['familien'] += neue
    p.write_text(json.dumps(neu, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if isinstance(fr, dict): (IN / fid / 'fragen.json').write_text(json.dumps(fr, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f'{fid}: {len(neue)} neue Familien ({sum(len(f["a"]) for f in neue)} Aufgaben), {rechnen} Rechenfragen als Klausurstil markiert, {len(offen)} Aufgabenstellungen ungeprüft')
    if liste: print(json.dumps(offen, ensure_ascii=False, indent=0))


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    for f in (args or ['bwl', 'mkt', 'wima', 'mawi', 'ikm', 'igt']): fach(f, '--liste' in sys.argv)
