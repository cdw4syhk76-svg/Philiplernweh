"""Markierung „Wichtig“: Punkte, die oft in Prüfungen gefragt wurden (plan/gp_inventar.json, j >= wichtig_ab),
werden auf Unterthemen, Fragen-Familien, Karten, große Aufgaben und Probeklausur-Varianten übertragen.
Schreibt inhalte/<fach>/wichtig.json (neutral: nur IDs und Punkt-Kürzel). Aufruf: python3 werkzeuge/wichtig.py"""
import sys, json, re, sys, pathlib, html, hashlib
IN = pathlib.Path(__file__).resolve().parents[1] / 'inhalte'
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from abdeckung import text_von
def txt(s): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s or ''))).strip()


def muster(such):
    teile = []
    for s in such:
        if s.isupper() and len(s) <= 4: teile.append(r'(?-i:\b' + re.escape(s) + r'\b)')   # Abkürzungen nur als ganzes Wort
        else: teile.append(re.escape(s))
    return re.compile('|'.join(teile), re.I)


def fach(fid):
    lies = lambda n: json.loads((IN / fid / n).read_text(encoding='utf-8'))
    inv = lies('plan/gp_inventar.json'); ab = inv.get('wichtig_ab', 2)
    wp = [P for P in inv['punkte'] if not P.get('aus') and P.get('j', 0) >= ab]
    fr = lies('fragen.json'); fams = (fr['familien'] if isinstance(fr, dict) else fr) + lies('fragen_neu.json')['familien']
    btxt = lambda s: re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s or '')).replace('&amp;', '&').replace('&nbsp;', ' ').strip()   # wie bau.py
    for q in fams: q.setdefault('id', f"{fid}:{q['t']}:" + hashlib.sha1(btxt(q['a'][0].get('p', '')).encode()).hexdigest()[:8])
    karten = lies('karten.json')['karten'] if (IN / fid / 'karten.json').exists() else []
    gl = lies('glossar.json')['begriffe']
    auf = lies('aufgaben.json')['aufgaben'] if (IN / fid / 'aufgaben.json').exists() else []
    kl = lies('klausur.json')['aufgaben'] if (IN / fid / 'klausur.json').exists() else []
    out = dict(themen={}, familien={}, karten=[], begriffe=[], aufgaben=[], varianten=[])
    # jede Familie gehört zu dem wichtigen Punkt, dessen Suchwörter am häufigsten in ihr vorkommen
    for f in fams:
        t = ' '.join(text_von(a) for a in f['a']) + ' ' + f.get('z', '')
        treffer = [(len(muster(P['such']).findall(t)), -i, P['id']) for i, P in enumerate(wp) if f.get('t') in P['t']]
        treffer = [x for x in treffer if x[0]]
        if f.get('punkt') and any(P['id'] == f['punkt'] for P in wp): treffer = [(1, 0, f['punkt'])]   # von Hand zugeordnet
        if treffer:
            pid = max(treffer)[2]; out['familien'][f['id']] = pid; out['themen'].setdefault(f['t'], []).append(pid)
    for P in wp:
        m = muster(P['such']); ts = set(P['t'])
        out['karten'] += [txt(c['v']) for c in karten if c['t'] in ts and m.search(txt(c['v'] + ' ' + c['r']))]
        out['begriffe'] += [g['begriff'] for g in gl if g.get('heimat') in ts and m.search(txt(g['begriff'] + ' ' + g['text']))]
        out['aufgaben'] += [A['id'] for A in auf if ts & set(A['unter']) and m.search(txt(A['titel'] + ' ' + A.get('ausgang', '') + ' ' + ' '.join(T.get('text', '') for T in A['teile'])))]
        for A in kl:
            for T in A['teile']:
                for v in T['varianten']:
                    if v['unter'] in ts and m.search(txt(A['titel'] + ' ' + v['text'])): out['varianten'].append(v['id'])
    out['themen'] = {t: sorted(set(p)) for t, p in out['themen'].items()}
    for k in ('karten', 'begriffe', 'aufgaben', 'varianten'): out[k] = sorted(set(out[k]))
    (IN / fid / 'wichtig.json').write_text(json.dumps(out, ensure_ascii=False, indent=0) + '\n', encoding='utf-8')
    ohne = [P['id'] for P in wp if not any(P['id'] in v for v in out['themen'].values())]
    print(f"{fid}: {len(wp)} wichtige Punkte, {len(out['themen'])} Unterthemen, {len(out['familien'])} Familien, {len(out['karten'])} Karten, "
          f"{len(out['begriffe'])} Begriffe, {len(out['aufgaben'])} Aufgaben, {len(out['varianten'])} Probeklausur-Varianten" + (f"; ohne Treffer: {ohne}" if ohne else ''))


if __name__ == '__main__':
    for f in (sys.argv[1:] or ['bwl', 'mkt', 'wima', 'mawi', 'ikm', 'igt']): fach(f)
