"""Folienstoff in die Lernseiten einarbeiten – so, als hätte er immer dort gestanden.

Je Fach eine Liste in werkzeuge/einarbeiten/<fach>.py:
  STAND = 'b1'                      Kennung dieser Überarbeitung (neue Runde → neue Kennung, z. B. 'b2')
  E = [dict(t='unterthema', alt='genauer HTML-Ausschnitt der Lernseite', neu='derselbe Ausschnitt mit Ergänzung'), …]
In `neu` steht alles Neue in [[…]] (innerhalb eines Elements, nie über Tags hinweg). Daraus wird
<span class="nz" data-nz="b1">…</span>. Die App färbt das gold, aber nur für Lernende, die das Unterthema schon vor dieser
Überarbeitung kannten (S.kannte). Wer neu dazukommt, sieht normalen Text.
Statt alt/neu geht auch nach='Ausschnitt' + block='<li>…</li>' (ganze neue Elemente direkt hinter dem Ausschnitt, alles gold)
oder vor='Ausschnitt' + block='…' (davor).

Fragen: Aus jedem neuen Teil mit einem fett gesetzten Begriff entsteht ein Lückentext
(Familie <fach>:<thema>:nz-<kurz>), damit das Neue auch geübt wird. Mit frage=False unterdrücken,
mit frage=dict(...) eine eigene Familie angeben (Format wie fragen.json).

Nur ergänzen: `neu` ohne die [[…]]-Teile muss genau `alt` sein (Leerzeichen gehören in die Klammern).
Wiederholbar: Jeder Lauf nimmt zuerst alle eingearbeiteten Teile heraus (der ursprüngliche Text bleibt) und setzt sie neu ein;
`alt` muss dann genau einmal vorkommen.
Reihenfolge: … → DIESES SKRIPT → originalfolien_ergaenzungen.py → definitionen_folien.py <fach> → originalfolien.py <fach> → bau.py --test
Aufruf: python3 werkzeuge/einarbeiten.py <fach …>"""
import sys, json, re, pathlib, importlib, hashlib, html as _html

ROOT = pathlib.Path(__file__).resolve().parents[1]
IN = ROOT / 'inhalte'
sys.path.insert(0, str(ROOT / 'werkzeuge' / 'einarbeiten'))


def lies(p): return json.loads(p.read_text(encoding='utf-8'))
def schreib(p, d): p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
def txt(h): return re.sub(r'\s+', ' ', _html.unescape(re.sub(r'<[^>]+>', ' ', h or ''))).strip()


def gold(h, stand):
    assert h.count('[[') == h.count(']]'), f'[[ ]] nicht ausgeglichen: {h[:80]}'
    return re.sub(r'\[\[(.*?)\]\]', lambda m: f'<!--nz--><span class="nz" data-nz="{stand}">{m.group(1)}</span><!--/nz-->', h, flags=re.S)


def block_gold(h, stand):
    """Ganze neue Elemente (Absatz, Listenpunkt, Tabellenzeile, Abschnitt): jedes Element der obersten Ebene bekommt data-nz"""
    tiefe, out, i = 0, '', 0
    for m in re.finditer(r'<(/?)([a-zA-Z0-9]+)([^>]*?)(/?)>', h):
        out += h[i:m.start()]; tag = m.group(0)
        if not m.group(1) and tiefe == 0: tag = f'<{m.group(2)}{m.group(3)} data-nz="{stand}"{m.group(4)}>'
        if not m.group(1) and not m.group(4) and m.group(2).lower() not in ('br', 'img', 'hr', 'input'): tiefe += 1
        elif m.group(1): tiefe -= 1
        out += tag; i = m.end()
    return '<!--nz-->' + out + h[i:] + '<!--/nz-->'


NZ = re.compile(r'<!--nz-->.*?<!--/nz-->', re.S)


def frage_aus(fach, tid, kap, star, neu, stand):
    """Lückentext aus jedem neuen Teil mit fettem Begriff (ganzer Satz als Kontext)"""
    varianten = []
    segs = re.findall(r'\[\[(.*?)\]\]', neu, flags=re.S) or re.findall(r'<(?:p|li|td|div)[^>]*>(.*?)</(?:p|li|td|div)>', neu, flags=re.S)
    for seg in segs:
        b = re.search(r'<b>(.*?)</b>', seg)
        if not b or len(txt(seg)) < 25: continue
        wort = txt(b.group(1))
        p = seg[:b.start()] + '<b>[[0]]</b>' + seg[b.end():]
        p = re.sub(r'<(?!/?b>)[^>]+>', '', p).strip(' ,;:·')
        varianten.append(dict(y='luecke', p=p[0].upper() + p[1:] if p[:1].islower() else p, l=[[wort, wort.lower()] if wort.lower() != wort else [wort]],
                              w=txt(seg), lvl=2))
    if not varianten: return None
    kurz = hashlib.sha1(neu.encode()).hexdigest()[:8]
    return dict(id=f'{fach}:{tid}:nz-{kurz}', f=fach, t=tid, k=kap, s=star, y='fam', fam=1, z='Kennt den ergänzten Folienstoff', a=varianten[:3])


def fach_bauen(fach):
    mod = importlib.import_module(fach); stand = mod.STAND
    pf = IN / fach / 'fach.json'; d = lies(pf)
    T = {t['id']: t for k in d['kapitel'] for t in k['themen']}
    kap = {t['id']: n + 1 for n, k in enumerate(d['kapitel']) for t in k['themen']}
    fams, fehler, neu_n = [], [], 0
    for t in T.values(): t['article'] = NZ.sub('', t['article'])   # zurück zum ursprünglichen Text
    for e in mod.E:
        tid = e['t']; assert tid in T, f'{fach}: Unterthema {tid} unbekannt'
        art = T[tid]['article']
        if 'block' in e:
            alt = e.get('nach') or e['vor']; bh = block_gold(gold(e['block'], stand), stand)
            neu_h = alt + bh if 'nach' in e else bh + alt; neu = e['block']
        else:
            alt, neu = e['alt'], e['neu']
            if re.sub(r'\[\[.*?\]\]', '', neu, flags=re.S) != alt: fehler.append(f'{tid}: `neu` ändert den alten Text (nur ergänzen): „{alt[:70]}“'); continue
            if any(re.search(r'<(div|p|li|ul|ol|table|tr|td|h3|section)\b', x) for x in re.findall(r'\[\[(.*?)\]\]', neu, flags=re.S)):
                fehler.append(f'{tid}: [[…]] enthält ganze Elemente (div, p, li …); dafür nach=/vor= mit block= nehmen: „{alt[:70]}“'); continue
            neu_h = gold(neu, stand)
        if art.count(alt) == 1: T[tid]['article'] = art.replace(alt, neu_h); neu_n += 1
        else: fehler.append(f'{tid}: Ausschnitt {art.count(alt)}× gefunden: „{alt[:70]}“'); continue
        if e.get('frage') is False: continue
        f_ = e['frage'] if isinstance(e.get('frage'), dict) else frage_aus(fach, tid, kap[tid], bool(T[tid].get('star')), neu if 'block' not in e else '[[' + e['block'] + ']]', stand)
        if f_: fams.append(f_)
    if fehler: raise SystemExit(f'{fach}:\n' + '\n'.join(fehler))
    schreib(pf, d)
    pq = IN / fach / 'fragen_neu.json'; fq = lies(pq) if pq.exists() else {'familien': []}
    fq['familien'] = [x for x in fq['familien'] if ':nz-' not in x.get('id', '')] + fams
    schreib(pq, fq)
    print(f'{fach}: {neu_n} Ergänzungen eingearbeitet, {len(fams)} Fragen-Familien')


if __name__ == '__main__':
    import subprocess
    for fach in sys.argv[1:]: fach_bauen(fach)
    subprocess.run([sys.executable, str(ROOT / 'werkzeuge' / 'nz_fragen.py'), *sys.argv[1:]], check=True)   # Lückentexte durch ausformulierte Fragen ersetzen
