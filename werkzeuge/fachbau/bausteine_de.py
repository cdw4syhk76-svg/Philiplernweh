"""Bausteine für einsprachige (deutsche) Lernseiten – dieselben Bausteine wie in Production, nur mit einem Text statt (en, de).
Für Fächer mit fremdsprachiger Klausur stattdessen bausteine_zweisprachig.py (gleicher Ordner) nehmen.
Nutzung in einem Kapitel-Skript:  from bausteine_de import *   (Pfad: sys.path.insert(0, '<repo>/werkzeuge/fachbau'))
Alle Funktionen liefern HTML/SVG-Text für das Feld article (oder kurz/fig) eines Unterthemas. Muster: werkzeuge/produktion/k1.py."""
import re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import bausteine_zweisprachig as _b

E = _b.E
_DOPPEL = re.compile(r'<span class="l-en" lang="en">(.*?)</span><span class="l-de" lang="de">\1</span>', re.S)
_DOPPEL_DIV = re.compile(r'<div class="zw2"><div class="l-en" lang="en">(.*?)</div><div class="l-de" lang="de">\1</div></div>', re.S)


def _ein(html):
    """gleiche Texte in beiden Sprachen zu einem zusammenfassen (keine doppelten Spans im deutschen Fach)"""
    for _ in range(3):
        html = _DOPPEL_DIV.sub(r'\1', _DOPPEL.sub(r'\1', html))
    return html


def _p2(x):
    return x if isinstance(x, tuple) else (x, x)


# ---------- Text ----------
def p(t): return f'<p>{t}</p>'
def h3(t): return f'<h3>{t}</h3>'
def weiter(t): return f'<p class="bruecke">{t}</p>'                                        # Überleitung (roter Faden)
def fw(t): return f'<p class="fig-what">{t}</p>'                                            # Satz über dem Hauptschaubild: was man sieht
def eg(t): return f'<span class="eg"><b>Einfach gesagt:</b> {t}</span>'                    # direkt nach einem schweren Begriff
def einfacher(t): return f'<details class="easy"><summary>Noch einfacher erklärt</summary><div>{t}</div></details>'
def falle(t): return f'<div class="lesson warn"><b>Typischer Fehler:</b> {t}</div>'
def klausur_hinweis(t): return f'<div class="box excl">⚠ <b>Klausur:</b> {t}</div>'
def zusatz(t): return ''  # Durchgestrichenes kommt nicht dran und wird komplett weggelassen (Nutzerregel)
def liste(punkte): return '<ul>' + ''.join(f'<li>{x}</li>' for x in punkte) + '</ul>'
def key(punkte): return '<ul class="key">' + ''.join(f'<li>{x}</li>' for x in punkte) + '</ul>'


# ---------- Karten, Tabellen, Gegenüberstellungen ----------
def cards(liste_):
    """kleine Karten: [(kopf, text)]"""
    return '<div class="cards">' + ''.join(f'<div><b>{a}</b>{b}</div>' for a, b in liste_) + '</div>'


def karten(liste_, klasse='levgrid'):
    """Ergebnis-/Merkkarten (z. B. für Rechner ①②③): [(kopf, gross, text, id)]"""
    return _ein(_b.karten([(k, k, g, t, t) + ((x[3],) if len(x) > 3 else ()) for x in liste_ for k, g, t in [x[:3]]], klasse))


def tabelle(kopf, zeilen):
    """kopf [str], zeilen [[str]]; erste Spalte als Zeilenkopf"""
    return _b.tabelle(kopf, zeilen)


def zwei(links, rechts):
    """zwei Spalten: je (kopf, [punkte])"""
    return f'<div class="two"><div><b>{links[0]}</b>{liste(links[1])}</div><div><b>{rechts[0]}</b>{liste(rechts[1])}</div></div>'


def procon(pro_kopf, pro, con_kopf, con):
    return f'<div class="two"><div class="pro"><b>{pro_kopf}</b>{liste(pro)}</div><div class="con"><b>{con_kopf}</b>{liste(con)}</div></div>'


def gegen(links, rechts):
    """zwei Begriffe gegenüber: je (kopf, text)"""
    return '<div class="two">' + ''.join(f'<div><b>{a}</b>{b}</div>' for a, b in (links, rechts)) + '</div>'


def fluss(schritte, hl=None):
    """Pfeilfluss: [(kopf, text)]; hl = Index der einen Hervorhebung"""
    return '<div class="d-flow">' + ''.join(f'<div{" class=hl" if i == hl else ""}><b>{a}</b>{b}</div>' for i, (a, b) in enumerate(schritte)) + '</div>'


def merkliste(kopf, unter, punkte, esel=None):
    """Klausur-Merkliste mit optionaler Eselsbrücke"""
    e = f'<p class="ml-esel"><b>Eselsbrücke:</b> {esel}</p>' if esel else ''
    return f'<div class="mliste"><div class="ml-h"><span>{kopf}</span><small>{unter}</small></div><ol>' + ''.join(f'<li>{x}</li>' for x in punkte) + '</ol>' + e + '</div>'


# ---------- Beispiel und Formel ----------
def bsp(titel, given, schritte=(), lesson=None):
    """Beispiel wie in Logistik: Ausgangslage, nummerierte Schritte [(text, ergebnis)], Lehre"""
    out = f'<div class="box bsp"><div class="box-h">Beispiel · {titel}</div><p class="given">{given}</p>'
    for i, st in enumerate(schritte, 1):
        rc = f'<div class="rc">{st[1]}</div>' if len(st) > 1 and st[1] else ''
        out += f'<div class="step"><span class="no">{i}</span><div>{st[0]}</div>{rc}</div>'
    return out + (f'<p class="lesson">{lesson}</p>' if lesson else '') + '</div>'


def fx(name, tex, worte, beispiel, warum=None):
    """Formel-Dreiklang: Name, Formel (LaTeX), In Worten, Beispiel, optional Woher"""
    w = f'<details class="fx-why"><summary>Woher kommt die Formel?</summary><p>{warum}</p></details>' if warum else ''
    return (f'<div class="fx"><div class="fx-n">{name}</div>\\[ {tex} \\]<div class="fx-iw"><b>In Worten</b>{worte}</div>'
            f'<div class="fx-z">{beispiel}</div>{w}</div>')


# ---------- Schaubilder (SVG, Theme-Farben) ----------
def T(x, y, t, size=12, w=400, anchor='middle', fill='var(--ink)'):
    """Text; Zeilen mit \\n trennen. Schrift im Hauptschaubild ≥ 12."""
    return _b.T(x, y, t, None, size, w, anchor, fill)


def box(x, y, w, h, t, tip=None, art='card', size=12, bold=700, rx=10):
    """Kasten; art: card | hl (die EINE Hervorhebung) | pale | weak; tip = Erklärung beim Antippen"""
    return _ein(_b.box(x, y, w, h, t, None, (tip, tip) if tip else None, art, size, bold, rx))


def tpg(inner, tip):
    """beliebiges SVG-Stück antippbar machen"""
    return f'<g class="tp" tabindex="0" data-tip="{E(tip)}">{inner}</g>'


pfeil = _b.pfeil
svg = _b.svg            # svg(breite, hoehe, inhalt, label, maxw=760, sid='')  → Hauptschaubild höchstens ~400 breit (Handy!)
bild = lambda s: s + '<div class="tip mtip">Tippe auf einen Teil des Schaubilds für eine Erklärung.</div>'


def mfig(titel, inhalt, cap=''):
    """aufklappbares Schaubild im Text („Ganz erklären“)"""
    return _ein(_b.mfig(titel, titel, inhalt, cap)).replace(_b.TIPP, '<div class="tip mtip">Tippe auf einen Teil des Schaubilds für eine Erklärung.</div>')


def tafeln(tid, namen, inhalte):
    """Umschalt-Tafeln: Knöpfe [namen] + je Knopf ein Inhalt (SVG/HTML)"""
    return _ein(_b.tafeln(tid, [(n, n) for n in namen], inhalte))


def tabs(tid, namen):
    return _ein(_b.tabs(tid, [(n, n) for n in namen]))


# ---------- Spiele ----------
def spiel(sid, frage, kategorien, karten_):
    """Zuordnungsspiel (nur wo es beim Durchdenken hilft): kategorien [str], karten_ [(text, richtige_kategorie_index, warum)]"""
    return _b.spiel(sid, (frage, frage), [(k, k) for k in kategorien], [(t, t, k, w, w) for t, k, w in karten_])


def wahr(sid, aussagen):
    """Kurz-Check richtig/falsch (wo die Klausur R/F-Blöcke hat): aussagen [(text, richtig:bool, warum)]"""
    return h3('Kurz-Check: richtig oder falsch?') + spiel(sid, 'Richtig oder falsch?', ['Richtig', 'Falsch'], [(t, 0 if r else 1, w) for t, r, w in aussagen])


def thema(id, titel, *, kern, kurz, article, merk, exam, fehler=(), fig='', figcap='', thumb='', star=False, wide=False, src='', aus=False):
    """ein Unterthema (Felder wie in inhalte/logistik/fach.json). kern = 1–2 Sätze oben, kurz = „Kurz erklärt“,
    fig = Hauptschaubild (mit fw(...) davor), article = „Ganz erklären“, merk = Merksatz, exam = was in der Klausur kommt.
    aus=True: Unterthema kommt in der Klausur nicht dran (z. B. in den Folien gestrichen) – ausgegraut, keine Fragen, Karten, Aufgaben."""
    d = dict(id=id, title=titel, titel_text=re.sub(r'<[^>]+>', '', titel), thumb=thumb, star=star, kern=kern, kurz=kurz,
             fig=fig, figcap=figcap, wide=wide, merk=merk, article=article, exam=exam, fehler=list(fehler), src=src)
    if aus: d.update(aus=True, star=False, exam='')
    return d


def kapitel(id, titel, intro, kette, themen):
    """ein Oberthema: kette = Stichworte des roten Fadens (eins je Unterthema)"""
    return dict(id=id, title=titel, titel_text=re.sub(r'<[^>]+>', '', titel), intro=intro, kette=list(kette), teil=None, themen=list(themen))


# ---------- Rechner wie in Logistik (Meldebestand): Regler → Bild → Karten ①②③ ----------
def regler(liste):
    """Regler-Leiste: [(id, beschriftung, min, max, schritt, wert, einheit)]; Ausgabe-Feld id-o wird vom Schaubild-Skript gefüllt.
    Das Skript dazu gehört in werkzeuge/<fach>/k<N>_figuren.js (Muster: Meldebestand in inhalte/logistik/figuren.js, id mbV/mbT/mbS)."""
    return '<div class="rgs">' + ''.join(
        f'<div class="rg"><label for="{i}">{b}</label><output id="{i}-o" for="{i}" data-u=" {e}">{w} {e}</output>'
        f'<input type="range" id="{i}" min="{a}" max="{z}" step="{s}" value="{w}"></div>' for i, b, a, z, s, w, e in liste) + '</div>'


def schritte_karten(liste):
    """Ergebnis-Karten ①②③ unter einem Rechner: [(kopf, id_gross, text_oder_id)]; letzte Karte = Ergebnis (hervorgehoben)"""
    out = []
    for n, (kopf, gid, txt_) in enumerate(liste):
        res = ' res' if n == len(liste) - 1 else ''
        t = f'<div class="lc-t" id="{txt_[1:]}"></div>' if txt_.startswith('#') else f'<div class="lc-t">{txt_}</div>'
        out.append(f'<div class="levcard{res}"><div class="lc-h">{kopf}</div><div class="lbig" id="{gid}"></div>{t}</div>')
    return '<div class="levgrid">' + ''.join(out) + '</div>'
