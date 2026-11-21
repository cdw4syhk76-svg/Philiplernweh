"""Liest alle „Klausur-Merklisten“ (div.mliste) aus den Lernseiten: Liste von dict(fid, tid, kn, nr, titel, hinweis, punkte[(name, erklaerung)])."""
import json, re, html, pathlib
IN = pathlib.Path(__file__).resolve().parents[1] / 'inhalte'
NUR_EN = lambda h: re.sub(r'<(span|div) class="l-de"[^>]*>.*?</\1>', ' ', h or '', flags=re.S)
def txt(s): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s or ''))).strip()

def listen(fid):
    d = json.loads((IN / fid / 'fach.json').read_text(encoding='utf-8'))
    out = []
    for kn, k in enumerate(d['kapitel'], 1):
        for t in k['themen']:
            if t.get('aus'): continue   # ausgegraut („kommt nicht dran“): keine Fragen, keine Lücke
            for nr, m in enumerate(re.finditer(r'<div class="mliste">(.*?)</ol>', t.get('article', ''), re.S)):
                b = NUR_EN(m.group(1)) if fid in ('produktion', 'ikm') else m.group(1)
                h = re.search(r'<small>(.*?)</small>', b); ti = re.search(r'<p class="ml-t">(.*?)</p>', b)
                punkte = []
                for li in re.findall(r'<li>(.*?)</li>', b, re.S):
                    mm = re.match(r'\s*<b>(.*?)</b>\s*·\s*(.*)$', li, re.S)
                    punkte.append((txt(mm.group(1)), txt(mm.group(2))) if mm else (txt(li), ''))
                out.append(dict(fid=fid, tid=t['id'], kn=kn, nr=nr, titel=txt(ti.group(1)) if ti else txt(h.group(1)) if h else '',
                                hinweis=txt(h.group(1)) if h else '', punkte=punkte))
    return out
