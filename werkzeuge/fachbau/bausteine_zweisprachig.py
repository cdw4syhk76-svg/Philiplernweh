"""Bausteine (zweisprachig, für Fächer mit fremdsprachiger Klausur; Kopie aus werkzeuge/produktion/bausteine.py): zweisprachige Texte (Englisch = Klausursprache, Schalter auf Deutsch)
und ruhige SVG-Schaubilder mit Theme-Farben. Jeder Text erscheint als Paar (en, de)."""
import html

E = html.escape


def sp(en, de):
    """kurzer Text in beiden Sprachen (inline)"""
    return f'<span class="l-en" lang="en">{en}</span><span class="l-de" lang="de">{de}</span>'


def zw(en, de):
    """Absätze in beiden Sprachen"""
    return f'<div class="zw2"><div class="l-en" lang="en">{en}</div><div class="l-de" lang="de">{de}</div></div>'


def h3(en, de):
    return zw(f'<h3>{en}</h3>', f'<h3>{de}</h3>')


TIPP = '<div class="tip mtip"><span class="l-en" lang="en">Tap a part of the figure for an explanation.</span><span class="l-de" lang="de">Tippe auf einen Teil des Schaubilds für eine Erklärung.</span></div>'


def bild(svg_):
    """Schaubild mit Erklärfeld darunter (für das Hauptschaubild eines Themas)"""
    return svg_ + TIPP


def weiter(en, de):
    """Überleitung: woher wir kommen, wohin es geht (roter Faden)"""
    return f'<p class="bruecke">{sp(en, de)}</p>'


def mfig(titel_en, titel_de, inhalt, cap=''):
    """aufklappbares Schaubild im Text („Ganz erklären“)"""
    c = f'<div class="fig-cap"><span>{cap}</span></div>' if cap else ''
    if 'class="tp' in inhalt and 'mtip' not in inhalt:
        inhalt += TIPP
    return (f'<div class="mfig"><button class="mfig-btn" type="button" aria-label="Schaubild öffnen: {E(titel_de)}"><span class="mfig-prev"></span>'
            f'<span class="mfig-lbl">⤢ {sp("Figure:", "Schaubild:")} <span>{sp(titel_en, titel_de)}</span><span class="mfig-tap">{sp("tap", "antippen")}</span></span></button>'
            f'<div class="mfig-body"><b class="mfig-t">{sp(titel_en, titel_de)}</b><div class="figure">{inhalt}{c}</div></div></div>')


def karten(liste, klasse='levgrid'):
    """Ergebnis- oder Merkkarten: [(kopf_en, kopf_de, gross, text_en, text_de, id)]"""
    out = []
    for i, k in enumerate(liste):
        ke, kd, gross, te, td = k[:5]
        kid = k[5] if len(k) > 5 else ''
        idg = f' id="{kid}"' if kid else ''
        idt = f' id="{kid}t"' if kid else ''
        res = ' res' if i == len(liste) - 1 and kid else ''
        out.append(f'<div class="levcard{res}"><div class="lc-h">{sp(ke, kd)}</div><div class="lbig"{idg}>{gross}</div><div class="lc-t"{idt}>{sp(te, td) if te or td else ""}</div></div>')
    return f'<div class="{klasse}">' + ''.join(out) + '</div>'


# ---------- SVG ----------
def T(x, y, en, de=None, size=12, w=400, anchor='middle', fill='var(--ink)'):
    """Text in beiden Sprachen; Zeilen mit \\n trennen"""
    def eine(t, kl):
        zeilen = t.split('\n'); dy = size * 1.22; y0 = y - (len(zeilen) - 1) * dy / 2
        return ''.join(f'<text class="{kl}" x="{x}" y="{y0 + i * dy + size * .35:.1f}" font-size="{size}" font-weight="{w}" text-anchor="{anchor}" style="fill:{fill}">{E(z)}</text>' for i, z in enumerate(zeilen))
    if de is None or de == en:
        zeilen = en.split('\n'); dy = size * 1.22; y0 = y - (len(zeilen) - 1) * dy / 2
        return ''.join(f'<text x="{x}" y="{y0 + i * dy + size * .35:.1f}" font-size="{size}" font-weight="{w}" text-anchor="{anchor}" style="fill:{fill}">{E(z)}</text>' for i, z in enumerate(zeilen))
    return eine(en, 'l-en') + eine(de, 'l-de')


def box(x, y, w, h, en, de=None, tip=None, art='card', size=12, bold=700, rx=10):
    """Kasten mit Text; art: card (normal), hl (die eine Hervorhebung), pale (Gruppe), weak (gedämpft)"""
    stil = {'card': 'fill:var(--card);stroke:var(--primary-2)', 'hl': 'fill:var(--primary);stroke:var(--primary)',
            'pale': 'fill:var(--pale);stroke:var(--line)', 'weak': 'fill:var(--pale-2);stroke:var(--line)'}[art]
    farbe = 'var(--on-primary)' if art == 'hl' else 'var(--ink)'
    inner = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" style="{stil}" stroke-width="1.3"/>' + T(x + w / 2, y + h / 2, en, de, size, bold, 'middle', farbe)
    if tip:
        te, td = tip
        return f'<g class="tp l-en" tabindex="0" data-tip="{E(te)}">{_nur(inner, "en")}</g><g class="tp l-de" tabindex="0" data-tip="{E(td)}">{_nur(inner, "de")}</g>'
    return inner


def _nur(svg, lang):
    """aus einem zweisprachigen SVG-Stück nur eine Sprache behalten (für Kästen mit Tooltip je Sprache)"""
    import re
    weg = 'l-de' if lang == 'en' else 'l-en'
    return re.sub(rf'<text class="{weg}"[^>]*>.*?</text>', '', svg).replace(f'class="l-{lang}" ', '')


def pfeil(x1, y1, x2, y2, farbe='var(--axis2)', w=1.6, kopf=True, dash=False):
    import math
    a = math.atan2(y2 - y1, x2 - x1); L = 8
    p = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" style="stroke:{farbe}" stroke-width="{w}"{" stroke-dasharray=\"5 4\"" if dash else ""}/>'
    if kopf:
        p += f'<polygon points="{x2},{y2} {x2 - L * math.cos(a - .4):.1f},{y2 - L * math.sin(a - .4):.1f} {x2 - L * math.cos(a + .4):.1f},{y2 - L * math.sin(a + .4):.1f}" style="fill:{farbe}"/>'
    return p


def svg(w, h, inhalt, label, maxw=760, sid=''):
    i = f' id="{sid}"' if sid else ''
    return f'<svg{i} viewBox="0 0 {w} {h}" role="img" aria-label="{E(label)}" style="max-width:{maxw}px;width:100%;margin:0 auto;display:block">{inhalt}</svg>'


def tabs(tid, namen):
    """Umschalter: [(en, de)]; erster aktiv"""
    return f'<div class="rules" id="{tid}">' + ''.join(f'<button type="button"{" class=on" if i == 0 else ""} data-k="{i}">{sp(e, d)}</button>' for i, (e, d) in enumerate(namen)) + '</div>'


def tabelle(kopf, zeilen):
    """zweisprachige Tabelle: kopf [(en,de)], zeilen [[(en,de) | str]]; erste Spalte als Zeilenkopf"""
    zelle = lambda c: sp(*c) if isinstance(c, tuple) else c
    return ('<div class="tbl-scroll"><table class="t"><tr>' + ''.join(f'<th>{zelle(c)}</th>' for c in kopf) + '</tr>'
            + ''.join('<tr>' + ''.join(f'<td{" class=rowh" if j == 0 else ""}>{zelle(c)}</td>' for j, c in enumerate(z)) + '</tr>' for z in zeilen) + '</table></div>')


def liste(punkte):
    return '<ul>' + ''.join(f'<li>{sp(*p) if isinstance(p, tuple) else p}</li>' for p in punkte) + '</ul>'


def cards(liste_):
    """kleine Karten: [(kopf_en, kopf_de, text_en, text_de)]"""
    return '<div class="cards">' + ''.join(f'<div><b>{sp(a, b)}</b>{sp(c, d)}</div>' for a, b, c, d in liste_) + '</div>'


def zwei(links, rechts):
    """zwei Spalten: je (kopf_en, kopf_de, [(en,de), …])"""
    sp_ = lambda k: f'<div><b>{sp(k[0], k[1])}</b>{liste(k[2])}</div>'
    return f'<div class="two">{sp_(links)}{sp_(rechts)}</div>'


def bsp(titel_en, titel_de, given, schritte=(), lesson=None):
    """Beispiel wie in Logistik: Ausgangslage, nummerierte Schritte mit Ergebnis rechts, Lehre"""
    out = f'<div class="box bsp"><div class="box-h">{sp("Example · " + titel_en, "Beispiel · " + titel_de)}</div><p class="given">{sp(*given)}</p>'
    for i, st in enumerate(schritte, 1):
        rc = f'<div class="rc">{sp(st[2], st[3])}</div>' if len(st) > 2 else ''
        out += f'<div class="step"><span class="no">{i}</span><div>{sp(st[0], st[1])}</div>{rc}</div>'
    if lesson:
        out += f'<p class="lesson">{sp(*lesson)}</p>'
    return out + '</div>'


def fx(name, tex, worte, beispiel, warum=None):
    """Formel-Dreiklang: Formel, In Worten, Beispiel, Woher"""
    w = f'<details class="fx-why"><summary>{sp("Where does it come from?", "Woher kommt die Formel?")}</summary><p>{sp(*warum)}</p></details>' if warum else ''
    return (f'<div class="fx"><div class="fx-n">{sp(*name)}</div>\\[ {tex} \\]<div class="fx-iw"><b>{sp("In words", "In Worten")}</b>{sp(*worte)}</div>'
            f'<div class="fx-z">{sp(*beispiel)}</div>{w}</div>')


def merkliste(kopf, unter, punkte, esel=None):
    """Klausur-Merkliste: kopf (en,de), unter (en,de), punkte [(en,de)], esel (en,de) = Eselsbrücke"""
    e = f'<p class="ml-esel">{sp("<b>Memory hook:</b> " + esel[0], "<b>Eselsbrücke:</b> " + esel[1])}</p>' if esel else ''
    return (f'<div class="mliste"><div class="ml-h"><span>{sp(*kopf)}</span><small>{sp(*unter)}</small></div><ol>'
            + ''.join(f'<li>{sp(*p)}</li>' for p in punkte) + '</ol>' + e + '</div>')


def zusatz(en, de):
    return f'<p><span class="zusatz">{sp("Extra · not in the exam", "Zusatz · kommt nicht dran")}</span> {sp(en, de)}</p>'


def spiel(sid, frage, kategorien, karten):
    """Zuordnungsspiel wie in Logistik (Materialarten): eine Karte nach der anderen, Kategorie antippen, sofort Rückmeldung.
    frage (en, de) · kategorien [(en, de)] · karten [(text_en, text_de, richtige_kategorie, warum_en, warum_de)]"""
    import json
    daten = dict(f=list(frage), k=[list(k) for k in kategorien], c=[list(c) for c in karten])
    return f'<div class="p-spiel" id="{sid}" data-spiel="{E(json.dumps(daten, ensure_ascii=False))}"></div>'


def procon(pro_kopf, pro, con_kopf, con):
    """Vorteile ↔ Nachteile: pro_kopf (en,de), pro [(en,de)], con_kopf, con"""
    return (f'<div class="two"><div class="pro"><b>{sp(*pro_kopf)}</b>{liste(pro)}</div>'
            f'<div class="con"><b>{sp(*con_kopf)}</b>{liste(con)}</div></div>')


def gegen(links, rechts):
    """Gegenüberstellung zweier Begriffe: je (kopf_en, kopf_de, text_en, text_de)"""
    return '<div class="two">' + ''.join(f'<div><b>{sp(a, b)}</b>{sp(c, d)}</div>' for a, b, c, d in (links, rechts)) + '</div>'


def fluss(schritte, hl=None):
    """Pfeilfluss: [(kopf_en, kopf_de, text_en, text_de)]; ab 4 Schritten automatisch senkrecht"""
    return '<div class="d-flow">' + ''.join(f'<div{" class=hl" if i == hl else ""}><b>{sp(a, b)}</b>{sp(c, d)}</div>' for i, (a, b, c, d) in enumerate(schritte)) + '</div>'


def eg(en, de):
    """„Einfach gesagt“ direkt nach einem schweren Begriff"""
    return f'<span class="eg">{sp("<b>Simply put:</b> " + en, "<b>Einfach gesagt:</b> " + de)}</span>'


def einfacher(en, de):
    """aufklappbar „Noch einfacher erklärt“ (sparsam: 1–2 je Kapitel)"""
    return f'<details class="easy"><summary>{sp("Explained even more simply", "Noch einfacher erklärt")}</summary><div>{zw(en, de)}</div></details>'


def falle(en, de):
    return f'<div class="lesson warn">{sp("<b>Typical mistake:</b> " + en, "<b>Typischer Fehler:</b> " + de)}</div>'


def klausur_hinweis(en, de):
    return f'<div class="box excl">⚠ {sp("<b>Exam:</b> " + en, "<b>Klausur:</b> " + de)}</div>'


def key(punkte):
    """Stichpunkte unter einem Bild: was man darin sieht"""
    return '<ul class="key">' + ''.join(f'<li>{sp(*p)}</li>' for p in punkte) + '</ul>'


def tafeln(tid, namen, inhalte):
    """Umschalt-Tafeln: Knöpfe + je Knopf ein Inhalt (SVG oder HTML); JS in gemeinsam_figuren.js"""
    knoepfe = f'<div class="rules" id="{tid}" data-tafeln="1">' + ''.join(f'<button type="button"{" class=on" if i == 0 else ""} data-k="{i}">{sp(e, d)}</button>' for i, (e, d) in enumerate(namen)) + '</div>'
    return knoepfe + ''.join(f'<div class="umpanel" data-for="{tid}" data-k="{i}"{"" if i == 0 else " hidden"}>{x}</div>' for i, x in enumerate(inhalte))


def wahr(sid, aussagen):
    """Kurz-Check wie in der Klausur: Aussagen richtig/falsch. aussagen [(en, de, richtig:bool, warum_en, warum_de)]"""
    return (h3('Quick check: true or false?', 'Kurz-Check: richtig oder falsch?')
            + spiel(sid, ('True or false?', 'Richtig oder falsch?'), [('True', 'Richtig'), ('False', 'Falsch')],
                    [(e, d, 0 if r else 1, we, wd) for e, d, r, we, wd in aussagen]))


def tpg(inner, tip):
    """beliebiges zweisprachiges SVG-Stück antippbar machen; tip = (en, de) wie bei box"""
    te, td = tip
    return f'<g class="tp l-en" tabindex="0" data-tip="{E(te)}">{_nur(inner, "en")}</g><g class="tp l-de" tabindex="0" data-tip="{E(td)}">{_nur(inner, "de")}</g>'


def _umbruch(t, n):
    """Text auf höchstens n Zeichen je Zeile umbrechen"""
    zeilen, z = [], ''
    for w in t.split(' '):
        if z and len(z) + 1 + len(w) > n:
            zeilen.append(z); z = w
        else:
            z = (z + ' ' + w).strip()
    return zeilen + ([z] if z else [])


def punktkasten(x, y, w, h, kopf, punkte, tip=None, art='card', size=11.5):
    """Kasten mit Überschrift und Aufzählung; kopf = (en, de), punkte = [(en, de)]; Umbruch automatisch mit hängendem Einzug"""
    stil = {'card': 'fill:var(--card);stroke:var(--primary-2)', 'hl': 'fill:var(--primary);stroke:var(--primary)',
            'pale': 'fill:var(--pale);stroke:var(--line)'}[art]
    farbe = 'var(--on-primary)' if art == 'hl' else 'var(--ink)'
    n = int((w - 26) / (size * .54)); dy = size * 1.25
    inner = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" style="{stil}" stroke-width="1.3"/>'
    inner += f'<line x1="{x + 10}" y1="{y + 30}" x2="{x + w - 10}" y2="{y + 30}" style="stroke:{farbe};opacity:.35"/>'
    for lang, i in (('en', 0), ('de', 1)):
        inner += f'<text class="l-{lang}" x="{x + w / 2}" y="{y + 20}" font-size="{size + 1}" font-weight="800" text-anchor="middle" style="fill:{farbe}">{E(kopf[i])}</text>'
        yy = y + 30 + dy + 2
        for pk in punkte:
            for j, z in enumerate(_umbruch(pk[i], n)):
                if j == 0:
                    inner += f'<text class="l-{lang}" x="{x + 10}" y="{yy:.1f}" font-size="{size}" font-weight="800" style="fill:{farbe}">•</text>'
                inner += f'<text class="l-{lang}" x="{x + 20}" y="{yy:.1f}" font-size="{size}" font-weight="600" style="fill:{farbe}">{E(z)}</text>'
                yy += dy
            yy += 3
    if tip:
        return tpg(inner, tip)
    return inner


def punkthoehe(w, punkte, size=11.5):
    """nötige Höhe eines punktkasten (längere Sprache zählt)"""
    n = int((w - 26) / (size * .54))
    return 30 + 14 + max(sum(len(_umbruch(pk[i], n)) * size * 1.25 + 3 for pk in punkte) for i in (0, 1))
