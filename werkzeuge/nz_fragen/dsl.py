"""Kurzschreibweise für die Fragen zum eingearbeiteten Folienstoff (Familien „:nz-“). Format wie fragen.json."""
def mc(p, r, f, w='', l=2): return dict(y='mc', p=p, o=[[r, True]] + [[x, False] for x in f], w=w, lvl=l)
def mm(p, o, w='', l=2): return dict(y='mc_multi', p=p, o=[[a, b] for a, b in o], w=w, lvl=l)
def bl(p, aus, w='', l=3): return dict(y='block', p=p or 'Richtig oder falsch? (4er-Block, nur alles richtig gibt Punkte)', aussagen=[[a, b] for a, b in aus], w=w, lvl=l)
def zu(p, k, e, w='', l=2): return dict(y='zuord', p=p, k=k, e=[[a, b] for a, b in e], w=w, lvl=l)
def li(p, pk, w='', l=2, n=None): return dict(y='liste', p=p, pk=[x if isinstance(x, list) else [x] for x in pk], n=n or len(pk), w=w, lvl=l)
def ku(p, ok, w='', l=2): return dict(y='kurz', p=p, ok=ok if isinstance(ok, list) else [ok], w=w, lvl=l)
def rh(p, o, w='', l=2): return dict(y='reihe', p=p, o=o, w=w, lvl=l)
