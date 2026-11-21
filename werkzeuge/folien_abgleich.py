"""Folien-Abgleich (intern, Skill /folien-abgleich): Kommt jede Folienzeile auf der Lernseite und in den Fragen vor?
Jede Folie wird gegen die Unterthemen geprüft, deren `src` sie nennt (sonst gegen das ganze Fach):
  L = Lernseite (Text, Karten, Glossar), F = Fragen (Fragen, Aufgaben, Probeklausur). Wortstamm-Vergleich je Zeile.
Kopf-/Fußzeilen (auf mehr als 4 Seiten) werden übersprungen. Durchgestrichene Folien: inhalte/<fach>/plan/folien_weg.json {"165": "Grund"}.
Aufruf: python3 werkzeuge/folien_abgleich.py <fach> [--seiten 10-20] [--grenze 0.6] [--versatz N] [--global] [--alle]   (--global: ohne Zuordnung über src, z. B. wenn Skriptseiten ≠ PDF-Seiten)"""
import sys, json, re, pathlib, html, collections

ROOT = pathlib.Path(__file__).resolve().parents[1]
IN = ROOT / 'inhalte'
QUELLE = {
    'bwl': 'Einfuhrung_in_die_Bwl_compressed.txt',
    'mkt': 'Marketing_compressed.txt',
    'mawi': 'Materialwirtschaft_compressed.txt',
    'ikm': 'interkulturelles_Management__compressed.txt',
    'igt': 'Rahmenbedingungen_internationaler_Geschaftstatigkeit.txt',
    'wima': 'Einstieg__compressed.txt',
}
STOP = set('''aber alle allem allen aller alles also andere anderen anderer anders auch auf aus bei beim bereits besonders bitte bzw dabei dadurch dafür daher damit dann darauf daraus darin darum darüber dass dein deine dem den denen denn der deren des dessen deshalb die dies diese diesem diesen dieser dieses doch dort durch eben ebenfalls eher eigene eigenen ein eine einem einen einer eines einige einigen einmal etwa etwas euch eure für gegen gegenüber ggf haben hat hier hinaus ihre ihrem ihren ihrer ihres immer innerhalb insbesondere ist jede jedem jeden jeder jedes jedoch jetzt kann kein keine keinen können könnte machen mehr mehrere meist mit muss müssen nach neben nicht noch nur ob oder ohne schon sehr sein seine seinem seinen seiner seit sich sie sind so sodass solche solchen soll sollen sollte sowie sowohl statt über um und uns unser unsere unter usw viel viele vom von vor während was weitere weiteren welche welchen wenn werden wie wieder will wird wo wurde wurden zu zum zur zwar zwei drei vier fünf zwischen beispiel beispiele quelle quellen folie seite prof meier schneider paul chammout kersten frisch weinberger dhbw mannheim
the and for with that this from are was were which have has had not but they their them these those there what when where who will would could should can may might into than then also such other more most some any each only very just about over under between within without upon your you our its it's his her him she use used using based example examples source'''.split())


def norm(s):
    s = html.unescape(re.sub(r'<[^>]+>', ' ', s))
    s = s.lower().replace('ß', 'ss').replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')
    return s


def woerter(s):
    return re.findall(r'[a-z][a-z\-]{3,}', norm(s))


def stamm(w):
    w = w.strip('-')
    for suf in ('ungen', 'ungen', 'ierung', 'ung', 'heit', 'keit', 'ern', 'en', 'er', 'es', 'em', 'e', 'n', 's'):
        if len(w) > len(suf) + 4 and w.endswith(suf): return w[:-len(suf)]
    return w


def sammle(o, out):
    if isinstance(o, str): out.append(o)
    elif isinstance(o, dict):
        for v in o.values(): sammle(v, out)
    elif isinstance(o, list):
        for v in o: sammle(v, out)


def korpus(fid, dateien):
    out = []
    for d in dateien:
        p = IN / fid / d
        if p.exists(): sammle(json.loads(p.read_text(encoding='utf-8')), out)
    t = norm(' '.join(out))
    w = set(re.findall(r'[a-z][a-z\-]{3,}', t))
    st = set(stamm(x) for x in w)
    # auch Teile von Bindestrich-/Komposita-Wörtern
    for x in list(w):
        for teil in x.split('-'):
            if len(teil) > 3: st.add(stamm(teil))
    return t, st


def drin(wort, text, staemme):
    s = stamm(wort)
    if s in staemme: return True
    if len(s) >= 6 and s in text: return True   # Kompositum-Teil
    for teil in wort.split('-'):
        if len(teil) > 3 and stamm(teil) not in staemme and stamm(teil) not in text: return False
    return '-' in wort



def seiten_aus(src):
    """'Folien 5–9, 69–71; Folie 42' -> {5,6,7,8,9,69,70,71,42}"""
    out = set()
    m = re.search(r'(?:Folien?|Slides?|Script p\.|S\.)\s*([0-9 ,–\-]+(?:\s*(?:,|und)\s*[0-9–\-]+)*)', src)
    for teil in re.findall(r'\d+\s*[–-]\s*\d+|\d+', ' '.join(re.findall(r'(?:Folien?|Slides?|p\.|S\.)\s*([0-9 ,–\-]+)', src))):
        x = re.split(r'\s*[–-]\s*', teil)
        a, b = int(x[0]), int(x[-1])
        if b >= a and b - a < 60: out.update(range(a, b + 1))
    return out


def main():
    a = sys.argv[1:]
    fid = a[0]
    off = int(a[a.index('--versatz') + 1]) if '--versatz' in a else 0   # PDF-Seite = Folie + versatz
    seiten = open(IN / fid / 'plan' / 'quellen' / QUELLE[fid], encoding='utf-8').read().split('\f')
    weg = {}
    pw = IN / fid / 'plan' / 'folien_weg.json'
    if pw.exists(): weg = {int(k): v for k, v in json.loads(pw.read_text(encoding='utf-8')).items()}
    von, bis = 1, len(seiten)
    if '--seiten' in a:
        x = a[a.index('--seiten') + 1].split('-'); von, bis = int(x[0]), int(x[-1])
    grenze = float(a[a.index('--grenze') + 1]) if '--grenze' in a else 0.6
    zc = collections.Counter(l.strip() for s in seiten for l in set(s.splitlines()) if l.strip())
    haeufig = {l for l, n in zc.items() if n > 4}
    fach = json.loads((IN / fid / 'fach.json').read_text(encoding='utf-8'))
    themen = {t['id']: t for k in fach['kapitel'] for t in k['themen'] if not t.get('aus')}   # ausgegraute Unterthemen: kein Stoff
    kap = {t['id']: k['id'] for k in fach['kapitel'] for t in k['themen']}
    for k in fach['kapitel']:
        for t in k['themen']:
            if t.get('aus'):
                for f in seiten_aus(t.get('src', '')): weg.setdefault(f + off, 'Unterthema ausgegraut (kommt nicht dran)')
    def lade(d):
        p = IN / fid / d
        return json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}
    fams = lade('fragen.json').get('familien', []) + lade('fragen_neu.json').get('familien', [])
    karten = lade('karten.json').get('karten', [])
    glossar = lade('glossar.json').get('begriffe', [])
    aufg = lade('aufgaben.json').get('aufgaben', [])
    klaus = [v for A in lade('klausur.json').get('aufgaben', []) for T in A['teile'] for v in T['varianten']]
    folie_zu = collections.defaultdict(list)
    for tid, t in themen.items():
        for f in seiten_aus(t.get('src', '')): folie_zu[f + off].append(tid)
    def mk(objs):
        out = []; sammle(objs, out); t = norm(' '.join(out))
        st = set(stamm(x) for x in re.findall(r'[a-z][a-z\-]{3,}', t))
        return t, st
    lok_l, lok_f = {}, {}
    for tid, t in themen.items():
        lok_l[tid] = mk([t, [c for c in karten if c.get('t') == tid], [g for g in glossar if g.get('heimat') == tid]])
        lok_f[tid] = mk([[f for f in fams if f.get('t') == tid], [x for x in aufg if tid in x.get('unter', [])], [v for v in klaus if v.get('unter') == tid]])
    gl = mk([fach, karten, glossar]); gf = mk([fams, aufg, klaus])
    n_auff = 0
    for i in range(von, min(bis, len(seiten)) + 1):
        if i in weg and '--alle' not in a: continue
        s = seiten[i - 1]
        tids = [] if '--global' in a else folie_zu.get(i, [])
        if tids:
            nb = sorted({u for t in tids for u in themen if kap[u] == kap[t]})   # ganzes Oberthema (Inhalt kann beim Nachbarn stehen)
            L = (' '.join(lok_l[t][0] for t in nb), set().union(*[lok_l[t][1] for t in nb]))
            F = (' '.join(lok_f[t][0] for t in nb), set().union(*[lok_f[t][1] for t in nb]))
        else:
            L, F = gl, gf
        luecken = []
        for l in s.splitlines():
            if not l.strip() or l.strip() in haeufig: continue
            if re.search(r'https?:|www\.|©|Vorlesung Marketing,|Prof\. Dr\.|^\s*(Quelle|Abb\.|Literatur|Archivbild|Bildquelle)', l): continue
            l = re.sub(r'\(?(Quelle|Abb\.|Literatur)[^)]*\)?', ' ', l)
            ws = [w for w in dict.fromkeys(woerter(l)) if w not in STOP]
            if len(ws) < 2: continue
            fl = [w for w in ws if not drin(w, *L)]
            ff = [w for w in ws if not drin(w, *F)]
            ql, qf = 1 - len(fl) / len(ws), 1 - len(ff) / len(ws)
            if ql < grenze or qf < grenze * 0.6:
                luecken.append(f"   {'L' if ql < grenze else ' '}{'F' if qf < grenze * 0.6 else ' '} {ql:.0%}/{qf:.0%} {l.strip()[:110]}   [fehlt: {' '.join(fl or ff)[:80]}]")
        if luecken or not tids:
            n_auff += 1
            print(f"--- S.{i} → {', '.join(tids) or 'KEIN UNTERTHEMA (global geprüft)'}")
            for z in luecken: print(z)
    print(f'== {fid}: {len(seiten)} Seiten, {n_auff} auffällig, {len(weg)} als weggelassen geprüft')


if __name__ == '__main__':
    main()
