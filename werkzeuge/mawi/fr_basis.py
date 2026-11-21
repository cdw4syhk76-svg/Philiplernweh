"""Bausteine für die MaWi-Fragen (Format wie inhalte/logistik/fragen.json). IDs sind fest: mawi:<unterthema>:<kürzel>."""
import json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[2]
FACH = json.loads((ROOT / 'inhalte' / 'mawi' / 'fach.json').read_text(encoding='utf-8'))
K = {t['id']: i + 1 for i, k in enumerate(FACH['kapitel']) for t in k['themen']}
STAR = {t['id']: bool(t.get('star')) for k in FACH['kapitel'] for t in k['themen']}
FAM = []


def fam(t, kurz, z, *qs):
    assert t in K, t
    FAM.append({'id': f'mawi:{t}:{kurz}', 'f': 'mawi', 't': t, 'k': K[t], 's': STAR[t], 'y': 'fam', 'fam': 1, 'z': z, 'a': [q for q in qs if q]})


def _m(d, w, lvl, kl):
    d['w'] = w; d['lvl'] = max(lvl, 2) if kl else lvl   # Klausurfragen sind nie Einstiegsfragen
    if kl:
        d['klausur'] = True
    return d


def mc(p, richtig, falsch, w='', lvl=1, kl=False):
    return _m({'y': 'mc', 'p': p, 'o': [[richtig, True]] + [[f, False] for f in falsch]}, w, lvl, kl)


def mm(p, opts, w='', lvl=2, kl=False):
    return _m({'y': 'mc_multi', 'p': p, 'o': [[t, r] for t, r in opts]}, w, lvl, kl)


def zu(p, kat, eintr, w='', lvl=1, kl=False):
    return _m({'y': 'zuord', 'p': p, 'k': kat, 'e': [[t, i] for t, i in eintr]}, w, lvl, kl)


def kz(p, ok, w='', lvl=2, kl=False):
    return _m({'y': 'kurz', 'p': p, 'ok': ok}, w, lvl, kl)


def li(p, pk, w='', lvl=2, kl=False, n=None):
    return _m({'y': 'liste', 'p': p, 'pk': pk, 'n': n or len(pk)}, w, lvl, kl)


def lu(p, l, w='', lvl=2, kl=False):
    return _m({'y': 'luecke', 'p': p, 'l': l}, w, lvl, kl)


def rh(p, o, w='', lvl=1, kl=False):
    return _m({'y': 'reihe', 'p': p, 'o': o}, w, lvl, kl)


def rv(p, l, pk, lvl=3, kl=False):
    return _m({'y': 'rev', 'p': p, 'l': l, 'pk': pk}, '', lvl, kl)


def nu(p, v, a, w, u='', r=2, wenn=None, tipp='', lvl=2, kl=False, kopf=True):
    g = {'v': v, 'a': a, 'r': r}
    if wenn:
        g['wenn'] = wenn
    d = {'y': 'num', 'p': p, 'gen': g, 'u': u, 'kopf': kopf}
    if tipp:
        d['tipp'] = tipp
    return _m(d, w, lvl, kl)


def ns(p, a, w, u='', lvl=2, kl=False, tipp=''):
    d = {'y': 'num', 'p': p, 'a': a, 'u': u}
    if tipp:
        d['tipp'] = tipp
    return _m(d, w, lvl, kl)


def schreibe():
    ids = [f['id'] for f in FAM]
    doppelt = {i for i in ids if ids.count(i) > 1}
    assert not doppelt, doppelt
    fehlt = [t for t in K if not any(f['t'] == t for f in FAM)]
    mcs = [a for f in FAM for a in f['a'] if a.get('y') == 'mc']
    lang = sum(1 for a in mcs if len(a['o'][0][0]) >= max(len(o[0]) for o in a['o'][1:]) + 4)
    print(f'MC: {len(mcs)}, richtige Antwort deutlich am längsten: {lang} ({lang / max(1, len(mcs)) * 100:.0f} %)')
    (ROOT / 'inhalte' / 'mawi' / 'fragen.json').write_text(json.dumps({'familien': FAM}, ensure_ascii=False, indent=0) + '\n', encoding='utf-8')
    n = {}
    for f in FAM:
        n[f['t']] = n.get(f['t'], 0) + len(f['a'])
    wenig = {t: n.get(t, 0) for t in K if n.get(t, 0) < 8}
    print(f'mawi: {len(FAM)} Familien, {sum(n.values())} Fragen; Unterthemen ohne Fragen: {fehlt}; unter 8 Fragen: {wenig}')


# ---------- Schaubild-Fragen (beschriften, antippen) im Stil der Logistik-Fragen ----------
def _esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def _txt(x, y, s, size=13, w=700, fill='var(--dg-ink, var(--ink))', a='middle'):
    zeilen = str(s).split('\n'); dy = size * 1.2; y0 = y - (len(zeilen) - 1) * dy / 2
    return ''.join(f'<text x="{x}" y="{y0 + i * dy + size * .35:.1f}" text-anchor="{a}" font-size="{size}" font-weight="{w}" style="fill:{fill}">{_esc(z)}</text>' for i, z in enumerate(zeilen))


def _marke(n, x, y):
    return (f'<g class="dg-m" data-m="{n}"><circle cx="{x}" cy="{y}" r="15" style="fill:var(--dg-a)"/>'
            f'<text x="{x}" y="{y + 5.5}" text-anchor="middle" font-size="16" font-weight="800" style="fill:var(--dg-on)">{n}</text></g>')


def _kasten(x, y, w, h, hell=True):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" style="fill:{"var(--dg-soft)" if hell else "var(--dg-bg)"};stroke:var(--dg-a)" stroke-width="2"/>'


def _pfeil(x1, y1, x2, y2):
    import math
    a = math.atan2(y2 - y1, x2 - x1); L = 9
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" style="stroke:var(--dg-b)" stroke-width="2"/>'
            f'<polygon points="{x2},{y2} {x2 - L * math.cos(a - .4):.1f},{y2 - L * math.sin(a - .4):.1f} {x2 - L * math.cos(a + .4):.1f},{y2 - L * math.sin(a + .4):.1f}" style="fill:var(--dg-b)"/>')


def bes(p, kaesten, extra=(), w='', lvl=2, kl=False, W=360, H=None, deko='', label='Schaubild zum Beschriften'):
    """Beschriften: kaesten [(x, y, b, h, richtige_beschriftung)] bekommen der Reihe nach die Marken 1, 2, 3 …;
    kaesten mit Beschriftung None werden nur gezeichnet; deko = zusätzliches SVG (Pfeile, feste Texte)."""
    H = H or max(y + h for x, y, b, h, _ in kaesten) + 10
    s, slots, n = deko, [], 0
    for x, y, b, h, lab in kaesten:
        s += _kasten(x, y, b, h, n % 2 == 0)
        if lab is None:
            continue
        if lab.startswith('='):          # fest beschrifteter Kasten
            s += _txt(x + b / 2, y + h / 2, lab[1:]); continue
        n += 1; slots.append(lab); s += _marke(n, x + b / 2, y + h / 2)
    bild = f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{_esc(label)}">{s}</svg>'
    return _m({'y': 'beschr', 'p': p, 'slots': slots, 'extra': list(extra), 'bild': bild, 'vb': [float(W), float(H)]}, w, lvl, kl)


def hot(p, kaesten, ziel, w='', lvl=2, kl=False, W=360, H=None, deko='', label='Schaubild zum Antippen'):
    """Antippen: kaesten [(x, y, b, h, text_oder_'')]; ziel = Index des richtigen Kastens"""
    H = H or max(y + h for x, y, b, h, _ in kaesten) + 10
    s = deko
    for x, y, b, h, t in kaesten:
        s += _kasten(x, y, b, h) + (_txt(x + b / 2, y + h / 2, t) if t else '')
    x, y, b, h, _ = kaesten[ziel]
    bild = f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{_esc(label)}">{s}</svg>'
    return _m({'y': 'hot', 'p': p, 'z': [x, y, b, h], 'bild': bild, 'vb': [float(W), float(H)]}, w, lvl, kl)


def hotpunkt(p, deko, punkt, w='', lvl=2, kl=False, W=360, H=260, label='Diagramm zum Antippen'):
    """Antippen eines Punkts in einem Diagramm: punkt = (x, y, radius)"""
    bild = f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{_esc(label)}">{deko}</svg>'
    return _m({'y': 'hot', 'p': p, 'z': list(punkt), 'bild': bild, 'vb': [float(W), float(H)]}, w, lvl, kl)


def achse(x0, y0, x1, y1, xl='', yl=''):
    return (_pfeil(x0, y0, x1, y0) + _pfeil(x0, y0, x0, y1) + (_txt(x1 - 4, y0 - 12, xl, 12, 600, 'var(--dg-b)', 'end') if xl else '')
            + (_txt(x0 + 8, y1 + 4, yl, 12, 600, 'var(--dg-b)', 'start') if yl else ''))


def linie(pts, farbe='var(--dg-a)', w=3, dash=False):
    return f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" style="fill:none;stroke:{farbe}" stroke-width="{w}"{" stroke-dasharray=\"6 4\"" if dash else ""}/>'


def blk(p, aussagen, w='', lvl=2, kl=False):
    """Richtig/Falsch-Block: aussagen [(text, richtig)]"""
    return _m({'y': 'block', 'p': p, 'aussagen': [[t, r] for t, r in aussagen]}, w, lvl, kl)
