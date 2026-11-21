"""Fragen zu den ergänzten Fachbegriffen (Skill /begriffs-check): je Unterthema eine Familie „<fach>:<unterthema>:bg-begriffe“ in fragen_neu.json.
  · „Was bedeutet …?“ (Auswahl; Ablenker = Erklärungen anderer Begriffe desselben Fachs, ähnlich lang)
  · „Wie heißt der Begriff …?“ (Kurzantwort)
  · Verknüpfen Begriff ↔ Erklärung (ab drei Begriffen im Unterthema)
Quelle: werkzeuge/<fach>/begriffe_ergaenzt.py (B). Wiederholbar (alte bg-Familien werden ersetzt).
Aufruf: python3 werkzeuge/begriffs_fragen.py <fach>"""
import sys, json, re, pathlib, hashlib, importlib.util

ROOT = pathlib.Path(__file__).resolve().parents[1]


def kurz(t, n=110):
    t = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', t)).strip()
    t = re.sub(r'\s*\((?:z\. ?B\.|e\. ?g\.|etwa|bspw\.)[^)]*\)', '', t)   # Beispiele in Klammern weglassen
    t = re.split(r'(?<!z\.)(?<!B\.)(?<!d\.)(?<!i\.)(?<!u\.)(?<!e\.)(?<!g\.)(?<=[.;:])\s(?=[A-ZÄÖÜ„])', t)[0].split('; ')[0].rstrip('.;:')
    return t if len(t) <= n else t[:n].rsplit(' ', 1)[0] + ' …'


def main(fid):
    p = ROOT / 'werkzeuge' / fid / 'begriffe_ergaenzt.py'
    spec = importlib.util.spec_from_file_location('b', p); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    fach = json.loads((ROOT / 'inhalte' / fid / 'fach.json').read_text(encoding='utf-8'))
    kn = {t['id']: i + 1 for i, k in enumerate(fach['kapitel']) for t in k['themen']}
    star = {t['id']: bool(t.get('star')) for k in fach['kapitel'] for t in k['themen']}
    gl = json.loads((ROOT / 'inhalte' / fid / 'glossar.json').read_text(encoding='utf-8'))['begriffe']
    pool = [(g['begriff'], kurz(g['text']), kn.get(g['heimat'], 0)) for g in gl]
    en = fid == 'ikm'
    fams = {}
    for b, _mu, t, text in m.B:
        assert t in kn, (b, t)
        richtig = kurz(text)
        h = int(hashlib.sha1(b.encode()).hexdigest(), 16)
        kand = sorted([(e, k) for bb, e, k in pool if bb != b and e != richtig and not re.search(re.escape(b.split(' (')[0]), e, re.I)],
                      key=lambda ek: (ek[1] != kn[t], abs(len(ek[0]) - len(richtig)) // 15, hashlib.sha1((b + ek[0]).encode()).hexdigest()))
        kand = [e for e, _ in kand]   # zuerst Erklärungen aus demselben Oberthema (plausibel), ähnlich lang
        falsch = kand[:3]
        f = fams.setdefault(t, [])
        if len(falsch) == 3:
            q = {'y': 'mc', 'p': (f'What does “{b}” mean?' if en else f'Was bedeutet „{b}“?'), 'o': [[richtig, True]] + [[x, False] for x in falsch], 'w': text, 'lvl': 1}
            if en: q['de'] = f'Was bedeutet „{b}“?'
            f.append(q)
        q = {'y': 'kurz', 'p': (f'Which term is meant? {richtig}' if en else f'Wie heißt der Begriff? {richtig}'), 'ok': [b] + [x.strip() for x in re.split(r'[()/,]', b) if len(x.strip()) > 2 and x.strip() != b], 'w': text, 'lvl': 2}
        if en: q['de'] = 'Welcher Begriff ist gemeint?'
        f.append(q)
    out = []
    for t, qs in fams.items():
        bs = [(b, kurz(x, 70)) for b, _mu, tt, x in m.B if tt == t]
        if len(bs) >= 3:
            q = {'y': 'zuord', 'p': ('Match each term with its explanation.' if en else 'Verknüpfe: Welcher Begriff passt zu welcher Erklärung?'), 'k': [b for b, _ in bs[:5]], 'e': [[e, i] for i, (_, e) in enumerate(bs[:5])], 'w': '', 'lvl': 1}
            if en: q['de'] = 'Ordne jedem Begriff seine Erklärung zu.'
            qs.append(q)
        out.append({'id': f'{fid}:{t}:bg-begriffe', 'f': fid, 't': t, 'k': kn[t], 's': star[t], 'y': 'fam', 'fam': 1,
                    'z': ('Knows the terms of this topic' if en else 'Kennt die Fachbegriffe des Unterthemas'), 'a': qs})
    pn = ROOT / 'inhalte' / fid / 'fragen_neu.json'
    d = json.loads(pn.read_text(encoding='utf-8')) if pn.exists() else {'familien': []}
    d['familien'] = [x for x in d['familien'] if ':bg-' not in x.get('id', '')] + out
    pn.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f'{fid}: {len(m.B)} ergänzte Begriffe → {len(out)} Familien, {sum(len(x["a"]) for x in out)} Fragen')


if __name__ == '__main__':
    main(sys.argv[1])
