"""Zweisprachige Bausteine für Introduction to English Linguistics (Englisch = Klausursprache, Schalter auf Deutsch).
Durchgehende Beispiele: das Wort „nice“ (k1) und der Frosch /frɒg/ (k2)."""
import re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_zweisprachig import *          # noqa: F401,F403
from bausteine_zweisprachig import sp, zw, E


def p(en, de): return zw(f'<p>{en}</p>', f'<p>{de}</p>')
def fw(en, de): return f'<p class="fig-what">{sp(en, de)}</p>'
def txt(t): return re.sub(r'<[^>]+>', '', t)


def thema(id, titel, *, kern, kurz, article, merk, exam, fehler=(), fig='', figcap=('', ''), star=False, wide=False, src=''):
    return dict(id=id, title=sp(*titel), titel_text=titel[0], thumb='', star=star, kern=sp(*kern), kurz=zw(*kurz),
                fig=fig, figcap=sp(*figcap) if figcap[0] else '', wide=wide, merk=sp(*merk), article=article, exam=sp(*exam),
                fehler=[sp(*f) for f in fehler], src=src)


def kapitel(id, titel, intro, kette, themen):
    return dict(id=id, title=sp(*titel), titel_text=titel[0], intro=sp(*intro), kette=list(kette), teil=None, themen=list(themen))


def seiten(hoch, tief, titel):
    """zwei Kästen mit Aufzählung: hoch/tief = ((kopf_en, kopf_de), [(en, de)], tip)"""
    h = round(max(punkthoehe(180, hoch[1]), punkthoehe(180, tief[1])))
    return svg(372, h + 34, T(186, 14, titel[0], titel[1], 13, 800)
               + punktkasten(4, 30, 180, h, hoch[0], hoch[1], tip=hoch[2])
               + punktkasten(188, 30, 180, h, tief[0], tief[1], tip=tief[2], art='hl'), titel[0], maxw=440)
