/* LernTool · Kern: Daten (Fächer werden erst bei Bedarf geladen), Lernstand, Prüfungs-% mit Verfall,
   Fragen-Engine, Karteikarten, Drill, Arbeitsblatt, Timer. Die Ansichten stehen in ansichten.js. */
'use strict';
const D = window.LT_INDEX;
const F = Object.fromEntries(D.faecher.map(f => [f.id, f]));
const TOP = {};                       // „fach/unterthema“ → {f, k, t}
for (const f of D.faecher) for (const k of f.kapitel) for (const t of k.topics) TOP[f.id + '/' + t.id] = { f, k, t };
const DAY = 864e5;
const txt = s => String(s ?? '').replace(/<[^>]+>/g, '').replace(/&amp;/g, '&').replace(/&nbsp;/g, ' ').replace(/\s+/g, ' ').trim();

/* ---------- Fächer bei Bedarf laden (daten/<fach>.js) ---------- */
const LT = window.LT = { warte: {} };
LT.fachGeladen = (fid, d) => {
  const f = F[fid];
  for (const k of f.kapitel) for (const t of k.topics) { Object.assign(t, d.inhalt[t.id] || {}); t.fragen = d.fragen[t.id] || []; }
  f.glossar = d.glossar.map(g => ({ b: txt(g.begriff), t: g.heimat, e: txt(g.text), muster: g.muster, w: g.w }));
  f.karten = d.karten || [];
  f.defs = d.defs || {};   // Folien-Definitionen je df-Familie: {b, w (Wortlaut, Kernpunkte markiert), e (einfache, bekannte Fassung)} – Nachschärf-Karten
  f.klausur = d.klausur || null;   // Probeklausur-Bogen im Aufbau der echten Klausur   // reiner Text; Zeilenumbrüche = Aufzählung
  f.nichtMarkieren = d.nicht_markieren; f.uebers = d.uebers; f.geladen = true;
  /* große Aufgaben: Hoch- und Tiefzeichen setzen (x^2 → x², a_n → aₙ) */
  f.aufgaben = (d.aufgaben || []).map(A => ({ ...A, ausgang: hoch(A.ausgang), titel: A.titel, teile: A.teile.map(T => ({ ...T, text: hoch(T.text), tipp1: hoch(T.tipp1), tipp2: hoch(T.tipp2), loesung: hoch(T.loesung) })) }));
  (LT.warte[fid] || []).forEach(fn => fn()); delete LT.warte[fid];
};
LT.lade = fids => Promise.all([...new Set(fids)].filter(fid => F[fid] && !F[fid].geladen).map(fid => new Promise((ok, nein) => {
  if (LT.warte[fid]) { LT.warte[fid].push(ok); return; }
  LT.warte[fid] = [ok];
  const s = document.createElement('script'); s.src = 'daten/' + fid + '.js';
  s.onerror = () => { delete LT.warte[fid]; nein(new Error('Fach ' + fid + ' konnte nicht geladen werden')); };
  document.head.appendChild(s);
})));
const geladen = fids => fids.every(fid => !F[fid] || F[fid].geladen);
const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const shuffle = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.random() * (i + 1) | 0;[a[i], a[j]] = [a[j], a[i]]; } return a; };
const pick = a => a[Math.random() * a.length | 0];
const kapNr = (f, k) => f.kapitel.indexOf(k) + 1;

/* ---------- Lernstand (im Browser dieses Geräts, Version im Feld v) ---------- */
const KEY = 'lerntool-v1';
let S;
/* Geist-Ansicht (Admin-Bereich): fremden Lernstand nur ansehen. Daten kommen aus dem Admin-Tab (lt-geist), nichts wird gespeichert oder abgeglichen. */
const GEIST = /[?&]geist=1\b/.test(location.search) ? (() => { try {
  const g = JSON.parse(localStorage.getItem('lt-geist') || 'null') || JSON.parse(sessionStorage.getItem('lt-geist') || 'null');
  if (g) { sessionStorage.setItem('lt-geist', JSON.stringify(g)); localStorage.removeItem('lt-geist'); }
  return g; } catch (e) { return null; } })() : null;
try { S = GEIST ? GEIST.daten : JSON.parse(localStorage.getItem(KEY)); } catch (e) { S = null; }
if (!S || S.v !== 1) S = { v: 1, pruef: {}, wackel: {}, zuletztF: {}, einst: {} };
for (const k of ['pruef', 'wackel', 'zuletztF', 'einst', 'mark', 'notiz']) S[k] = S[k] || {};
delete S.wserie;
/* Testdatum (Einstellungen): verschiebt „heute“ um n Tage, um Verfall und Countdown zu prüfen */
const jetzt = () => Date.now() + (S.einst.testTage || 0) * DAY;
const save = () => { if (GEIST) return; try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) { } if (typeof syncNachSpeichern === 'function') syncNachSpeichern(); };

/* ---------- Prüfungs-% mit Verfall: einziger Ort mit Prozenten ---------- */
/* Verfall: Der Stand hält h Tage (gutes Ergebnis länger, jeder gelungene Refresh verdoppelt h), danach sinkt er um 2,4 % pro Tag (nach 10 Tagen ≈ 76 %) */
function faktor(tage, h = 4) { return tage <= h ? 1 : Math.max(.4, 1 - .024 * (tage - h)); }
function stand(fid, kid) {
  const p = S.pruef[fid + '/' + kid];
  if (!p) return null;
  const tage = (jetzt() - p.d) / DAY, h = p.h || 4;
  const pct = Math.round(p.s * faktor(tage, h));
  return { pct, s: p.s, h, tage: Math.floor(tage), faellt: pct < p.s, refresh: pct < p.s, haeltNoch: Math.max(0, Math.ceil(h - tage)) };
}
/* Prüfungsreife über den ganzen Stoff: ungeprüfte Oberthemen zählen 0 (1 von 10 mit 100 % = 10 %) */
function fachStand(f) {
  const n = f.kapitel.map(k => stand(f.id, k.id)).filter(Boolean);
  return { gesamt: Math.round(n.reduce((s, x) => s + x.pct, 0) / f.kapitel.length), geprueft: n.length, von: f.kapitel.length, refresh: n.filter(x => x.refresh).length };
}
/* Wackelthemen = rote Unterthemen aus dem Stufen-System (gedaechtnis.js) */
const istWackel = key => G.farbe(key) === 1;
const wackelListe = () => G.rote().map(k => ({ key: k, ...TOP[k] }));

/* ---------- Klausuren (aus plattform/studium.py) ---------- */
function klausurVon(fid) { return D.klausuren.find(k => k.faecher.includes(fid)); }
function tageBis(iso) { const h = new Date(jetzt()); h.setHours(0, 0, 0, 0); const z = new Date(iso); z.setHours(0, 0, 0, 0); return Math.round((z - h) / DAY); }
function datumKurz(iso) { return new Date(iso).toLocaleDateString('de-DE', { weekday: 'short', day: '2-digit', month: '2-digit' }); }
function uhr(iso) { return new Date(iso).toLocaleTimeString('de-DE', { hour: '2-digit', minute: '2-digit' }); }
const klausurenSortiert = () => D.klausuren.slice().sort((a, b) => a.beginn < b.beginn ? -1 : 1).filter(k => tageBis(k.ende) >= 0);
function gewichte(k) { const g = k.teile.reduce((s, t) => s + t[2], 0); return k.teile.map(t => ({ name: t[4], fid: t[1], pct: Math.round(t[2] / g * 100) })); }

/* ---------- Fragen: Varianten auswählen, Zahlen erzeugen ---------- */
const AUTO = new Set(['mc', 'mc_multi', 'zuord', 'kurz', 'luecke', 'num', 'reihe', 'beschr', 'hot']);
const FN = { round: (x, n = 0) => { const m = 10 ** n; return Math.round(x * m) / m; }, abs: Math.abs, sqrt: Math.sqrt, log: Math.log, ln: Math.log, exp: Math.exp, min: Math.min, max: Math.max, int: Math.trunc, floor: Math.floor, ceil: Math.ceil, pow: Math.pow, log10: Math.log10, sum: (...a) => a.reduce((x, y) => x + y, 0), float: Number };
const pyjs = e => String(e).replace(/\*\*/g, '^').replace(/\^/g, '**').replace(/math\./g, '').replace(/\band\b/g, '&&').replace(/\bor\b/g, '||').replace(/\bnot\b/g, '!').replace(/\bTrue\b/g, 'true').replace(/\bFalse\b/g, 'false');
function ev(expr, vars) {
  const n = [...Object.keys(FN), ...Object.keys(vars)];
  return Function(...n, '"use strict";return (' + pyjs(expr) + ')')(...Object.values(FN), ...Object.values(vars));
}
const zahl = (x, r = 4) => typeof x === 'number' ? x.toLocaleString('de-DE', { maximumFractionDigits: r }) : String(x);
function ziehe(spec) {
  if (Array.isArray(spec) && spec.length === 3 && spec.every(x => typeof x === 'number')) {
    const [a, b, st] = spec, n = Math.floor((b - a) / st + 1e-9);
    return +(a + st * (Math.random() * (n + 1) | 0)).toFixed(10);
  }
  return Array.isArray(spec) ? pick(spec) : spec;
}
function fuelle(txt, vars, r) {
  return String(txt || '').replace(/\{=([^}]+)\}/g, (_, e) => { try { return zahl(FN.round(ev(e, vars), r ?? 2), r ?? 2); } catch (x) { return '?'; } })
    .replace(/\{([A-Za-z_]\w*)\}/g, (m, v) => v in vars ? zahl(vars[v]) : m);
}
/* Hochzeichen setzen: „x^2“, „e^(2x)“, „a^{n+1}“ → echtes Hochzeichen (nur im angezeigten Text, nicht in Formeln zum Rechnen) */
function hoch(t) {
  if (!t || typeof t !== 'string') return t;
  /* Formeln (\( … \), \[ … \]) unangetastet lassen: dort setzt KaTeX Hoch- und Tiefzeichen */
  if (t.indexOf('\\(') >= 0 || t.indexOf('\\[') >= 0) return t.split(/(\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\])/).map((s, i) => i % 2 ? s : hoch0(s)).join('');
  return hoch0(t);
}
function hoch0(t) {
  if (!t) return t;
  if (t.indexOf('_') >= 0) t = t.replace(/([A-Za-zεπΔ])_(\{([^}]*)\}|[A-Za-z0-9]+)/g, (m, v, x, inner) => `${v}<sub>${inner ?? x}</sub>`);   // Index: a_7, p_l, f_x
  if (t.indexOf('^') < 0) return t;
  let out = '', i = 0;
  while (i < t.length) {
    const c = t[i];
    if (c === '^' && i > 0 && t[i - 1] !== ' ') {
      const z = t[i + 1];
      if (z === '(' || z === '{') {   // geklammerter Exponent: bis zur passenden Klammer
        const zu = z === '(' ? ')' : '}'; let tiefe = 0, j = i + 1;
        for (; j < t.length; j++) { if (t[j] === z) tiefe++; else if (t[j] === zu && --tiefe === 0) break; }
        out += `<sup>${t.slice(i + 2, j)}</sup>`; i = j + 1; continue;
      }
      const m = /^(\[\[\d+\]\]|[−-]?[\wäöüÄÖÜ]+(?:,\d+)?)/.exec(t.slice(i + 1));
      if (m) { out += `<sup>${m[1]}</sup>`; i += 1 + m[1].length; continue; }
    }
    out += c; i++;
  }
  return out;
}
/* Eine Aufgabe „spielbereit“ machen: bei Zahlen-Generatoren Werte ziehen, Text und Lösung füllen */
function inst(a) {
  const q = Object.assign({}, a);
  if (a.y === 'num' && a.gen) {
    let vars = {};
    for (let i = 0; i < 200; i++) {
      vars = {}; for (const [k, sp] of Object.entries(a.gen.v || {})) vars[k] = ziehe(sp);
      try { if (!a.gen.wenn || ev(a.gen.wenn, vars)) break; } catch (e) { break; }
    }
    const r = a.gen.r ?? 2;
    try { q.ans = FN.round(ev(a.gen.a, vars), r); } catch (e) { q.ans = NaN; }
    q.p = fuelle(a.p, vars, r); q.w = fuelle(a.w, vars, r); q.vars = vars;
    q.ansatz = String(a.w || '').replace(/\{=([^}]+)\}/g, '<span class="luecke-x">?</span>').replace(/\{([A-Za-z_]\w*)\}/g, (m, v) => v in vars ? zahl(vars[v]) : m);
  } else if (a.y === 'num') {
    q.ans = a.a;
    q.ansatz = String(a.w || '').replace(/=\s*[^=]*$/, '= <span class="luecke-x">?</span>');
  }
  q.p = hoch(q.p); q.w = hoch(q.w); if (q.ansatz) q.ansatz = hoch(q.ansatz);
  if (Array.isArray(q.o)) q.o = q.o.map(o => Array.isArray(o) ? [hoch(o[0]), ...o.slice(1)] : hoch(o));
  return q;
}
/* Stufen: grund (Einstieg, Stufe 1–2) · klausur (Stufe 2–3, Klausurfragen bevorzugt) · schwer (nur Stufe 3 und Klausurfragen)
   'leicht' = Mini-Quiz (Stufe 1–2, automatisch auswertbar) · 'egal' = alles */
const STUFEN = [['grund', 'Grundlagen'], ['klausur', 'Klausur'], ['schwer', 'Schwer']];
function variante(fam, wahl) {
  const a = fam.a.slice(), lv = x => x.lvl || 1;
  const nimm = (...filter) => { for (const f of filter) { const m = a.filter(f); if (m.length) return pick(m); } return pick(a); };
  if (wahl === 'leicht') return nimm(x => lv(x) <= 2 && AUTO.has(x.y), x => lv(x) <= 2);
  if (wahl === 'grund') return nimm(x => lv(x) <= 2);
  if (wahl === 'klausur') return Math.random() < .5 ? nimm(x => x.klausur, x => lv(x) >= 2) : nimm(x => lv(x) >= 2);
  if (wahl === 'schwer') { const m = Math.max(...a.map(lv)); return nimm(x => x.klausur && lv(x) >= 3, x => lv(x) >= 3, x => x.klausur, x => lv(x) === m); }
  if (wahl === 'auto') return nimm(x => AUTO.has(x.y));
  return pick(a);
}
/* Unterthemen ausblenden (aus LernWeh DBM26A übernommen): S.uaus = {„fach/thema“: 1 | 0}. Ausgeblendete Unterthemen bleiben lesbar,
   ihre Fragen kommen aber weder im Training (Pool, fällige Aufgaben, rote Liste) noch in Übungs-, Refresh- und Probeklausur.
   Unterthemen aus der Prüfungsausgrenzung (Index-Feld ag) sind von Haus aus ausgeblendet; Einblenden speichert 0.
   Ein Oberthema gilt als fertig, wenn alle eingeblendeten Unterthemen grün sind (kapFertig). Umschalten: Dock der Lernseite. */
const uStd = key => !!(TOP[key] && TOP[key].t.ag);
const uAus = key => { const v = S.uaus && S.uaus[key]; return v != null ? !!v : uStd(key); };
const kapSichtbar = (f, k) => k.topics.filter(t => !t.aus && !uAus(f.id + '/' + t.id));
const kapAusZahl = (f, k) => k.topics.filter(t => !t.aus).length - kapSichtbar(f, k).length;
function kapFertig(f, k) { const v = kapSichtbar(f, k); return v.length > 0 && v.every(t => G.farbe(f.id + '/' + t.id) >= 3); }
function uSetze(key, an) { S.uaus = S.uaus || {}; if (!!an === uStd(key)) delete S.uaus[key]; else S.uaus[key] = an ? 1 : 0; if (typeof G !== 'undefined') G.cache = null; save(); }
/* Pool aus Unterthemen: [{key, f, k, t}] */
function themen(filter) {
  const out = [];
  for (const f of D.faecher) {
    if (filter.f && filter.f.length && !filter.f.includes(f.id)) continue;
    for (const k of f.kapitel) {
      if (filter.k && filter.k.length && !filter.k.includes(f.id + '/' + k.id)) continue;
      for (const t of k.topics) {
        const key = f.id + '/' + t.id;
        if (t.aus) continue;   // „kommt nicht dran“: nicht in Training, Endlos, Karten, Arbeitsblatt
        if (uAus(key)) continue;   // ausgeblendet (selbst oder Prüfungsausgrenzung)
        if (filter.wackel && !istWackel(key)) continue;
        if (filter.wichtig && !t.w) continue;   // „Nur Wichtiges“: nur Unterthemen mit oft geprüften Punkten, darin nur diese Fragen
        out.push(filter.wichtig ? { key, f, k, t, nurW: true } : { key, f, k, t });
      }
    }
  }
  return out;
}
/* Fragen-Familien eines Unterthemas; bei „Nur Wichtiges“ nur die wichtigen */
const famsVon = x => (x.t.fragen || []).filter(q => !x.nurW || q.w);
/* Eine Frage spielbereit machen, mit fester Gedächtnis-ID (Familie + Aufgabenart) */
function frageItem(x, fam, a) {
  const q = inst(a);
  return { a: q, key: x.key, f: x.f, k: x.k, t: x.t, z: fam.z, fam, x, gid: `q:${fam.id}:${a.y}`, gv: { i: fam.a.indexOf(a), vars: q.vars } };
}
/* Genau die Variante (mit denselben Zahlen) wieder herstellen, die zuletzt falsch war */
function frageWieder(x, fam, v) {
  const a = fam.a[v && v.i] || fam.a[0], it = frageItem(x, fam, a);
  if (v && v.vars && a.gen) { const r = a.gen.r ?? 2; it.a.vars = v.vars; try { it.a.ans = FN.round(ev(a.gen.a, v.vars), r); } catch (e) { }
    it.a.p = fuelle(a.p, v.vars, r); it.a.w = fuelle(a.w, v.vars, r); it.gv.vars = v.vars; }
  return it;
}
function ziehFragen(pool, n, wahl, nur) {
  const fams = [];
  for (const x of pool) for (const fam of famsVon(x)) fams.push({ x, fam });
  const out = [];
  const bDa = new Set();   // je Begriff (Folien-Definition, Feld b) höchstens eine Frage
  for (const { x, fam } of shuffle(fams)) {
    if (fam.b) { if (bDa.has(fam.b)) continue; bDa.add(fam.b); }
    let a = variante(fam, wahl);
    if (nur) { const m = fam.a.filter(v => nur.includes(v.y)); if (!m.length) continue; a = pick(m); }
    out.push(frageItem(x, fam, a));
    if (out.length >= n) break;
  }
  /* Wenige Familien (z. B. Mini-Quiz eines Unterthemas mit 3–4 Familien): mit einer anderen Aufgabenart derselben Familie auffüllen.
     Gleiche Familie + gleiche Art zählt im Gedächtnis nur einmal; sonst bekäme das Unterthema nie die 5 Aufgaben für seine Farbe. */
  if (!nur && out.length < n) {
    const hat = new Set(out.map(it => it.gid));
    for (const { x, fam } of shuffle(fams)) {
      const frei = fam.a.filter(v => !hat.has(`q:${fam.id}:${v.y}`) && (wahl !== 'leicht' || (v.lvl || 1) <= 2));
      if (!frei.length) continue;
      const it = frageItem(x, fam, pick(frei)); hat.add(it.gid); out.push(it);
      if (out.length >= n) break;
    }
  }
  return out;
}

/* ---------- Fragen-Engine ---------- */
const IC_LUPE = '<svg viewBox="0 0 24 24" class="ic-lupe"><circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/></svg>';
/* Wörter, mit denen „Nachschlagen“ die passende Stelle im Text sucht: zuerst die richtige Antwort, dann die Frage */
function suchBegriffe(a) {
  const ant = [];
  if (a.y === 'mc' || a.y === 'mc_multi') a.o.forEach(o => o[1] && ant.push(o[0]));
  if (a.y === 'kurz') ant.push(...a.ok.slice(0, 2));
  if (a.y === 'luecke') a.l.forEach(x => ant.push(x[0]));
  if (a.y === 'zuord') ant.push(...a.k, ...a.e.map(e => e[0]));
  if (a.y === 'beschr') ant.push(...a.slots);
  if (a.y === 'reihe') ant.push(...a.o);
  if (a.y === 'liste') a.pk.forEach(p => ant.push(p[0]));
  if (a.y === 'rev' && a.pk) ant.push(...a.pk);
  if (a.y === 'num' && a.tipp) ant.push(a.tipp);
  return { antwort: ant.map(txt).join(' '), frage: txt(a.p) + ' ' + txt(a.w || '') };
}
const norm = s => String(s).toLowerCase().replace(/<[^>]+>/g, '').replace(/[\s.,;:!?„“"'()\-–]/g, '').replace(/ß/g, 'ss').replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue');
const num = s => parseFloat(String(s).replace(/\s/g, '').replace(/[−–]/g, '-').replace(/[%€]/g, '').replace(/\.(?=\d{3}(\D|$))/g, '').replace(',', '.'));
/* Tippfehler-Toleranz: Abstand nach Levenshtein, erlaubt je nach Wortlänge 0 / 1 / 2 Zeichen */
function abstand(a, b) {
  if (a === b) return 0; if (!a.length || !b.length) return Math.max(a.length, b.length);
  let v = Array.from({ length: b.length + 1 }, (_, j) => j);
  for (let i = 1; i <= a.length; i++) { const w = [i]; for (let j = 1; j <= b.length; j++) w[j] = Math.min(v[j] + 1, w[j - 1] + 1, v[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1)); v = w; }
  return v[b.length];
}
const toleranz = s => s.length <= 4 ? 0 : s.length <= 8 ? 1 : 2;
/* Schreibvarianten einer richtigen Antwort, die fachlich dasselbe meinen (Prinzip Bombe, aber nicht kulanter):
   · Teile in Klammern und mit „/“ sind Alternativen: „Sicherheitsbestand (eiserner Bestand)“ → beide Teile einzeln
   · Wortreihenfolge und Artikel egal: „Bestand, eiserner“ = „eiserner Bestand“, „der Meldebestand“ = „Meldebestand“ */
const FUELL_W = new Set(['der', 'die', 'das', 'den', 'dem', 'des', 'ein', 'eine', 'einer', 'eines', 'einen', 'einem', 'the', 'a', 'an', 'of']);
const woerterNorm = s => String(s).toLowerCase().replace(/<[^>]+>/g, ' ').replace(/ß/g, 'ss').replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue')
  .split(/[^a-z0-9%]+/).filter(w => w && !FUELL_W.has(w));
const sortiert = s => woerterNorm(s).sort().join('');
function varianten(o) {
  const t = String(o), out = new Set([t]);
  const ohne = t.replace(/\s*\([^)]*\)\s*/g, ' ').trim(); if (ohne.length >= 3) out.add(ohne);
  for (const m of t.matchAll(/\(([^)]+)\)/g)) { const x = m[1].trim();   // Alternative in Klammern: ab 4 Zeichen oder ein Kürzel wie „JIT“
    if ((x.replace(/\s/g, '').length >= 4 || /^[A-ZÄÖÜ]{2,6}$/.test(x)) && !/^(z\.|e\.g|bzw|engl|dt\.|vgl|siehe|nicht)/i.test(x)) out.add(x); }
  if (/\s\/\s/.test(ohne)) for (const x of ohne.split(/\s\/\s/)) if (x.trim().length >= 4) out.add(x.trim());   // nur „A / B“ mit Leerzeichen (nicht „Kosten/Nutzen“)
  return [...out];
}
/* 'exakt' | 'fast' (Tippfehler) | '' */
function vergleich(eingabe, richtige) {
  const v = norm(eingabe); if (!v) return '';
  const alle = richtige.flatMap(varianten);
  if (alle.some(o => norm(o) === v)) return 'exakt';
  const vs = sortiert(eingabe);   // andere Wortreihenfolge nur exakt (sonst wäre „Ware zum Mann“ fast „Mann zur Ware“)
  const ew = woerterNorm(eingabe).join('');   // ohne Artikel: „der Meldebestand“ = „Meldebestand“
  if (ew.length >= 3 && alle.some(o => woerterNorm(o).join('') === ew)) return 'exakt';
  if (woerterNorm(eingabe).length >= 2 && alle.some(o => sortiert(o) === vs)) return 'exakt';
  return alle.some(o => { const r = norm(o); return Math.abs(r.length - v.length) <= 2 && abstand(r, v) <= toleranz(r); }) ? 'fast' : '';
}
/* Text einer Aufzählung: die vorgegebenen Felder (je Punkt eins), sonst das Textfeld */
const listeText = box => { const f = [...box.querySelectorAll('.q-li')]; return f.length ? f.map(x => x.value.trim()).filter(Boolean).join('\n') : (box.querySelector('.q-ta') || {}).value || ''; };
/* Aufzählung prüfen: jede Gruppe pk[i] = Synonyme eines Punkts; Treffer, wenn eine Zeile der Eingabe ihn enthält */
function listePruefen(text, pk) {
  const zeilen = String(text).split(/[\n;,•]+|\s+-\s+|\s+und\s+/).map(norm).filter(z => z.length > 1);
  return pk.map(gr => zeilen.some(z => gr.some(o => { const r = norm(o); return r && (z.includes(r) || (r.length > 5 && r.includes(z) && z.length >= 4) || abstand(r, z) <= toleranz(r)); })));
}
/* Kernpunkte in einer Erklärung erkennen: genug Schlüsselwörter eines Punkts kommen vor.
   Füllwörter zählen nicht; Wörter mit gleicher Bedeutung (SYNONYME) gelten als Treffer. */
const FUELL = new Set('werden wurde wurden worden einer eines einem einen diese dieser dieses diesem diesen durch sowie sondern zwischen damit wobei deren dessen welche welcher welches welchem nicht allen aller alles immer jeweils dabei darin davon dafür daher gegen möglichst zusammen anderen andere anderer beziehungsweise insbesondere bestimmte bestimmten gegenüber innerhalb außerhalb unter einerseits andererseits meist meistens häufig bereits deshalb'.split(' '));
const SYNONYME = [
  ['unternehmen', 'betrieb', 'firma', 'unternehmung'], ['kunde', 'kunden', 'abnehmer', 'käufer', 'nachfrager', 'verbraucher', 'konsument'],
  ['lieferant', 'lieferanten', 'zulieferer', 'anbieter'], ['planung', 'planen', 'geplant'], ['steuerung', 'steuern', 'lenken', 'lenkung'],
  ['kontrolle', 'kontrollieren', 'überwachung', 'überwachen', 'prüfen', 'prüfung'], ['ziel', 'ziele', 'zweck'], ['knapp', 'knappe', 'knappheit', 'begrenzt'],
  ['gewinn', 'überschuss', 'ergebnis'], ['vermögen', 'aktiva'], ['kapital', 'mittel', 'geld'], ['material', 'werkstoff', 'werkstoffe', 'rohstoff', 'rohstoffe'],
  ['bestand', 'bestände', 'vorrat', 'vorräte', 'lagerbestand'], ['menge', 'anzahl', 'stückzahl'], ['zeitpunkt', 'termin', 'rechtzeitig'],
  ['herstellung', 'produktion', 'fertigung', 'erzeugung', 'herstellen', 'produzieren'], ['verkauf', 'absatz', 'vertrieb', 'verkaufen'],
  ['einkauf', 'beschaffung', 'beschaffen', 'einkaufen'], ['bedürfnis', 'bedürfnisse', 'wunsch', 'wünsche', 'mangel'], ['markt', 'märkte', 'marktplatz'],
  ['information', 'informationen', 'daten', 'wissen'], ['verhältnis', 'quotient', 'geteilt', 'dividiert'], ['erhöhen', 'steigern', 'vergrößern', 'mehr'],
  ['senken', 'verringern', 'reduzieren', 'weniger'], ['langfristig', 'dauerhaft', 'nachhaltig'], ['kurzfristig', 'schnell', 'sofort'],
  ['qualität', 'güte', 'beschaffenheit'], ['kosten', 'ausgaben'], ['mitarbeiter', 'beschäftigte', 'personal', 'arbeitnehmer'], ['eigentümer', 'gesellschafter', 'inhaber', 'anteilseigner'],
  ['haftung', 'haften', 'haftet'], ['entscheidung', 'entscheiden', 'wahl', 'auswahl'], ['wert', 'werte', 'nutzen'], ['risiko', 'unsicherheit', 'gefahr'],
].map(g => g.map(norm));
function kernpunkte(text, pk) {
  const t = norm(text), stamm = w => w.slice(0, Math.max(5, w.length - 2));
  const trifft = w => t.includes(stamm(w)) || SYNONYME.some(g => g.some(s => stamm(s) === stamm(w) || s === w) && g.some(s => t.includes(stamm(s))));
  return pk.map(p => { const ws = String(txt(p)).toLowerCase().split(/[^a-zäöüß0-9]+/).filter(w => w.length >= 5 && !FUELL.has(w)).map(norm); if (!ws.length) return false;
    return ws.filter(trifft).length >= Math.ceil(ws.length / 2); });
}
/* Zwei Tipps für eine Definition: Anfang/Oberbegriff, dann ein Kernpunkt */
function defTipps(def, pk) {
  const w = txt(def).split(/\s+/), anfang = w.slice(0, Math.min(4, Math.max(2, Math.ceil(w.length / 6)))).join(' ');
  return [`So fängt es an: „${anfang} …“ · gesucht sind ${pk.length} ${pk.length === 1 ? 'Kernpunkt' : 'Kernpunkte'}`, `Ein Kernpunkt: ${pk[pk.length > 1 ? 1 : 0]}`];
}
const SELBST = { rev: 1, karte: 1, teil: 1 };
const TIPPBAR = { kurz: 1, luecke: 1, num: 1, liste: 1 };
const TYPNAME = { mc: 'Auswahl', mc_multi: 'Richtig / falsch', block: 'Aussagenblock', zuord: 'Zuordnen', kurz: 'Kurzantwort', luecke: 'Lückentext', num: 'Rechnen', reihe: 'Reihenfolge', liste: 'Aufzählen', rev: 'Erklären', beschr: 'Beschriften', hot: 'Antippen', karte: 'Karteikarte', teil: 'Teilaufgabe' };

function frageHTML(q, i) { return schoen(frageRoh(q, i)); }
function frageRoh(q, i) {
  const a = q.a;
  let body = '';
  const bild = a.bild ? `<div class="q-bild">${a.bild}</div>` : '';
  if (a.y === 'mc' && a.weg) body = `<div class="q-hint">Tippe den Schritt an, in dem der Fehler steckt.</div><ol class="q-weg">${a.o.map((o, j) => `<li><button class="q-opt" data-j="${j}">${o[0]}</button></li>`).join('')}</ol>`;
  else if (a.y === 'mc') body = `<div class="q-opts">${shuffle(a.o.map((o, j) => [o, j])).map(([o, j]) => `<button class="q-opt" data-j="${j}">${o[0]}</button>`).join('')}</div>`;
  else if (a.y === 'mc_multi' || a.y === 'block') {   // jede Aussage einzeln: richtig oder falsch (Punkte nur, wenn alle stimmen)
    const aus = a.y === 'block' ? a.aussagen : a.o;
    body = `<div class="q-hint">Jede Aussage: richtig oder falsch? Gewertet wird nur, wenn alle stimmen.</div><div class="q-rf">${aus.map((o, j) => `<div class="q-rfz" data-j="${j}"><span>${o[0]}</span><span class="q-rfb"><button class="q-chip" data-rf="1">richtig</button><button class="q-chip" data-rf="0">falsch</button></span></div>`).join('')}</div>`;
  }
  else if (a.y === 'zuord' || a.y === 'beschr') {
    const kats = a.y === 'zuord' ? a.k : shuffle(a.slots.concat(a.extra || []));
    const items = a.y === 'zuord' ? shuffle(a.e.map((e, j) => [e[0], j])) : a.slots.map((s, j) => ['Nr. ' + (j + 1), j]);
    body = `<div class="q-zuord">${items.map(([t, j]) => `<div class="q-zrow" data-j="${j}"><span class="q-ztxt">${t}</span><span class="q-zk">${kats.map((k, m) => `<button class="q-chip" data-k="${esc(k)}" data-m="${m}">${k}</button>`).join('')}</span></div>`).join('')}</div>`;
  }
  else if (a.y === 'kurz') body = `<input class="q-in" placeholder="Antwort …" autocomplete="off" aria-label="Antwort">`;
  else if (a.y === 'num') body = `<div class="q-numrow"><input class="q-in" inputmode="decimal" placeholder="Ergebnis" autocomplete="off" aria-label="Ergebnis"><span class="q-unit">${esc(a.u || '')}</span></div>`;
  else if (a.y === 'luecke') return `<div class="q-p">${a.p.replace(/\[\[(\d+)\]\]/g, (_, n) => `<input class="q-gap" data-n="${n}" autocomplete="off" aria-label="Lücke ${+n + 1}">`)}</div>`;
  else if (a.y === 'reihe') body = `<div class="q-hint">In der richtigen Reihenfolge antippen.</div><ol class="q-seq"></ol><div class="q-opts">${shuffle(a.o.map((o, j) => [o, j])).map(([o, j]) => `<button class="q-opt" data-j="${j}">${o}</button>`).join('')}</div>`;
  else if (a.y === 'hot') body = `<div class="q-hint">Tippe in das Bild.</div>`;
  else if (a.y === 'liste') { const n = Math.min(a.n || a.pk.length, 10);
    body = `<div class="q-hint">Gefragt: ${n} ${n === 1 ? 'Punkt' : 'Punkte'}. Ein Stichwort pro Feld reicht.</div><ol class="q-liste">${Array.from({ length: n }, (_, j) => `<li><input class="q-li" autocomplete="off" aria-label="Punkt ${j + 1}"></li>`).join('')}</ol>`; }
  else if (a.y === 'karte') return `<div class="sw-wrap q-kwrap"><div class="sw-stack"><div class="sw-card q-kcard" tabindex="0">
      <div class="sw-face sw-front"><small>${esc(a.fach || '')}</small><div class="sw-t">${esc(a.p)}</div><span class="sw-tap">antippen zum Umdrehen</span></div>
      <div class="sw-face sw-back"><small>${esc(a.p)}</small><div class="sw-e">${a.l}</div></div></div></div></div>`;
  else if (a.y === 'teil') return `<div class="q-teil"><small>${esc(a.titel)}</small>${a.ausgang ? `<div class="ws-ausgang">${a.ausgang}</div>` : ''}<div class="q-p">${a.p}</div></div><textarea class="q-ta" rows="3" placeholder="Lösungsweg (Papier geht auch) …" aria-label="Dein Lösungsweg"></textarea>`;
  else body = `<textarea class="q-ta" rows="4" placeholder="Erst selbst formulieren (Papier geht auch) …" aria-label="Deine Erklärung"></textarea>`
    + ((a.tipps || (a.pk && a.pk.length)) ? `<div class="q-tipps">${(a.tipps || [`${a.pk.length} ${a.pk.length === 1 ? 'Kernpunkt' : 'Kernpunkte'}, sie beginnen so: ${anfaenge(a.pk.map(g => Array.isArray(g) ? g[0] : g))}`, `Ein Kernpunkt ganz: ${txt(Array.isArray(a.pk[0]) ? a.pk[0][0] : a.pk[0])}`]).map((t, j) => `<button class="q-tippb" data-tipp="${esc(t)}"${j ? ' hidden' : ''}>Tipp ${j + 1}</button>`).join('')}<div class="q-tippt" aria-live="polite"></div></div>` : '');
  return `<div class="q-p">${a.p}</div>${bild}${body}`;
}
function loesungHTML(q) { return schoen(loesungRoh(q)); }
function loesungRoh(q) {
  const a = q.a;
  let r = '';
  if (a.y === 'mc' && a.weg) { const j = a.o.findIndex(o => o[1]); r = `Der Fehler steckt in Schritt ${j + 1}: ${a.o[j][0]}`; }
  else if (a.y === 'mc') r = a.o.filter(o => o[1]).map(o => o[0]).join(' · ');
  else if (a.y === 'mc_multi' || a.y === 'block') r = (a.y === 'block' ? a.aussagen : a.o).map(o => `<span class="q-rfl ${o[1] ? 'r' : 'f'}">${o[1] ? 'richtig' : 'falsch'}</span> ${o[0]}`).join('<br>');
  else if (a.y === 'zuord') r = a.e.map(e => `${e[0]} → <b>${a.k[e[1]]}</b>`).join('<br>');
  else if (a.y === 'beschr') r = a.slots.map((s, j) => `${j + 1} = <b>${s}</b>`).join(' · ');
  else if (a.y === 'kurz') r = a.ok[0];
  else if (a.y === 'luecke') r = a.l.map(x => x[0]).join(' · ');
  else if (a.y === 'num') r = zahl(a.ans, 4) + ' ' + (a.u || '');
  else if (a.y === 'reihe') r = a.o.map((o, j) => `${j + 1}. ${o}`).join('<br>');
  else if (a.y === 'liste') r = '<ul class="q-check-l">' + a.pk.map((p, j) => `<li class="${q.treffer ? (q.treffer[j] ? 'ja' : 'nein') : ''}">${p[0]}</li>`).join('') + '</ul>' + (a.n && a.n < a.pk.length ? `<small>gefragt: ${a.n} von ${a.pk.length} möglichen</small>` : '');
  else if (a.y === 'karte' || a.y === 'teil') r = a.l;
  else if (a.y === 'rev') r = (a.l || '') + (a.pk ? '<ul class="q-check-l">' + a.pk.map((p, j) => `<li class="${q.treffer ? (q.treffer[j] ? 'ja' : 'nein') : ''}">${p}</li>`).join('') + '</ul>' : '');
  if (a.y === 'rev' && a.auch) r += `<div class="q-auch"><b>Auch richtig (sinngemäß):</b> ${a.auch}<small>Gezählt wird, ob die Kernpunkte inhaltlich drin sind, nicht der genaue Wortlaut.</small></div>`;
  return `<div class="q-loes"><div class="q-loes-r">${r}</div>${a.w ? `<div class="q-w">${a.w}</div>` : ''}</div>`;
}
/* quiz(el, {next(i, res): Item|null, feedback, onEnd(res), kopf(i, res, item): html, weiterText}) */
function quiz(el, opt) {
  const res = []; let i = 0, cur = null;
  const fertig = () => { el.innerHTML = ''; opt.onEnd && opt.onEnd(res, el); };
  function zeige() {
    cur = opt.next(i, res);
    if (!cur) return fertig();
    const a = cur.a, selbst = SELBST[a.y];
    el.innerHTML = `<div class="qz" data-y="${a.y}">
      <div class="q-kopf">${opt.kopf ? opt.kopf(i, res, cur) : ''}<span class="q-meta">${a.zf ? `<b class="bdg-zf" title="${a.zf === 3 ? 'In den Folien gestrichen' : 'Dieser Stoff steht nicht in den Folien'}">${a.zf === 3 ? 'in den Folien gestrichen · für die Klausur nicht nötig' : a.zf === 2 ? 'nicht in den Folien · für die Klausur nicht nötig' : 'nicht in den Folien'}</b>` : ''}${cur.nochmal ? '<b class="bdg-w">nochmal</b>' : ''}${(cur.fam && cur.fam.w) || cur.w ? '<b class="bdg-w">Wichtig</b>' : ''}${a.weg ? 'Fehler finden' : TYPNAME[a.y] || a.y} · ${esc(cur.t.title)}</span><button class="q-melde" title="Fehler melden" aria-label="Fehler melden" data-melde="Frage · ${esc(cur.f ? cur.f.name : '')} · ${esc(txt(cur.t.title))} · ${esc(txt(a.p || '').slice(0, 90))}">⚑</button></div>
      ${frageHTML(cur, i)}
      <div class="q-act">${selbst ? `<button class="btn q-show">Lösung zeigen</button>` : (['mc', 'hot', 'reihe'].includes(a.y) ? '' : `<button class="btn q-check">Prüfen</button>`)}${a.hilfe ? '<button class="btn q-hilfe-k">Hilfe</button>' : ''}<button class="q-leise q-weiss">Weiß ich nicht</button>${opt.skip ? '<button class="q-leise q-skip">Überspringen</button>' : ''}</div>
      <div class="q-fb"></div></div>`;
    const box = el.querySelector('.qz');
    const hk = box.querySelector('.q-hilfe-k'); if (hk) { const it = cur; hk.onclick = () => { it.hilfeGenutzt = true; hk.remove(); const ziel = box.querySelector('.q-p'); (ziel || box.querySelector('.q-kopf')).insertAdjacentHTML('afterend', `<div class="q-hilfe">${schoen(it.a.hilfe)}<small>Mit Hilfe zählt die Frage höchstens als „fast sicher“.</small></div>`); }; }
    const commit = (ok, notiz = '') => {
      const eintrag = { ok, item: cur }; res.push(eintrag);
      const hl = !!cur.hilfeGenutzt;
      let rueck = G.antwort(cur.gid, ok, { k: cur.key, v: cur.gv, hilfe: hl });
      box.classList.add('done', ok ? 'ok' : 'nok');
      box.querySelectorAll('button.q-opt,button.q-chip,input,textarea').forEach(b => b.disabled = true);
      const fb = box.querySelector('.q-fb'), act = box.querySelector('.q-act');
      act.innerHTML = '';
      if (opt.feedback === false || a.y === 'karte') { i++; setTimeout(zeige, 160); return; }
      const urteil = () => `<div class="q-verdict">${eintrag.ok ? 'Richtig.' : 'Nicht ganz.'}</div>${notiz ? `<div class="q-notiz">${notiz}</div>` : ''}`;
      fb.innerHTML = urteil() + loesungHTML(cur);
      act.innerHTML = `<button class="btn btn-main q-next">${opt.weiterText || 'Weiter'}</button>` +
        (cur.key && window.LT_nachschlagen ? `<button class="btn q-nach">${IC_LUPE}Im Text nachschlagen</button>` : '') +
        (!ok && TIPPBAR[a.y] ? `<button class="btn q-doch">Ich hatte es doch richtig</button>` : '') +
        (ok && cur.gid ? `<button class="q-leise q-geraten">War geraten</button>` : '') +
        (cur.f && cur.k && cur.t && !(typeof V !== 'undefined' && V.screen === 'lern' && V.tid === cur.t.id) ? `<button class="q-leise q-thema" data-go="lern|${cur.f.id}|${cur.k.id}|${cur.t.id}">Zum Thema →</button>` : '');
      const gr = act.querySelector('.q-geraten'); if (gr) { const it = cur; gr.onclick = () => { rueck(); rueck = G.antwort(it.gid, false, { k: it.key, v: it.gv }); gr.outerHTML = '<span class="q-notiz">Zählt als nicht gewusst und kommt in „Methodisch lernen“ wieder.</span>'; }; }
      act.querySelector('.q-next').onclick = () => { i++; zeige(); };
      const nb = act.querySelector('.q-nach'); if (nb) { const it = cur; nb.onclick = () => window.LT_nachschlagen(it.key, suchBegriffe(it.a)); }
      const db = act.querySelector('.q-doch'); if (db) db.onclick = () => { eintrag.ok = true; rueck(); rueck = G.antwort(cur.gid, true, { k: cur.key, v: cur.gv, hilfe: hl }); notiz = 'Als richtig gewertet.'; box.classList.replace('nok', 'ok'); fb.querySelector('.q-verdict').outerHTML = urteil(); db.remove(); nb && nb.remove(); };
      act.querySelector('.q-next').focus({ preventScroll: true });
    };
    if (a.y === 'mc') box.querySelectorAll('.q-opt').forEach(b => b.onclick = () => { const ok = a.o[+b.dataset.j][1]; b.classList.add(ok ? 'sel-ok' : 'sel-nok'); if (opt.feedback !== false) box.querySelectorAll('.q-opt').forEach(x => a.o[+x.dataset.j][1] && x.classList.add('is-ok')); commit(ok); });
    if (a.y === 'zuord' || a.y === 'beschr') box.querySelectorAll('.q-zrow').forEach(r => r.querySelectorAll('.q-chip').forEach(c => c.onclick = () => { r.querySelectorAll('.q-chip').forEach(x => x.classList.remove('on')); c.classList.add('on'); r.dataset.v = c.dataset.k; }));
    if (a.y === 'mc_multi' || a.y === 'block') box.querySelectorAll('.q-rfz').forEach(r => r.querySelectorAll('.q-chip').forEach(c => c.onclick = () => { r.querySelectorAll('.q-chip').forEach(x => x.classList.remove('on')); c.classList.add('on'); r.dataset.v = c.dataset.rf; }));
    if (a.y === 'reihe') {
      const seq = []; const ol = box.querySelector('.q-seq');
      box.querySelectorAll('.q-opt').forEach(b => b.onclick = () => { seq.push(+b.dataset.j); b.disabled = true; ol.insertAdjacentHTML('beforeend', `<li>${a.o[+b.dataset.j]}</li>`); if (seq.length === a.o.length) commit(seq.every((v, j) => v === j)); });
    }
    if (a.y === 'hot') {
      const svg = box.querySelector('.q-bild svg');
      if (svg) svg.style.cursor = 'crosshair', svg.onclick = ev2 => {
        const pt = svg.createSVGPoint(); pt.x = ev2.clientX; pt.y = ev2.clientY; const p = pt.matrixTransform(svg.getScreenCTM().inverse()); const z = a.z;
        const ok = z.length === 3 ? Math.hypot(p.x - z[0], p.y - z[1]) <= z[2] + 6 : (p.x >= z[0] - 4 && p.x <= z[0] + z[2] + 4 && p.y >= z[1] - 4 && p.y <= z[1] + z[3] + 4);
        svg.insertAdjacentHTML('beforeend', `<circle cx="${p.x}" cy="${p.y}" r="9" style="fill:none;stroke:${ok ? 'var(--q-ok)' : 'var(--q-nok)'};stroke-width:3"/>`); svg.onclick = null; commit(ok);
      };
    }
    const chk = box.querySelector('.q-check');
    if (chk) chk.onclick = () => {
      let ok, notiz = '';
      if (a.y === 'mc_multi' || a.y === 'block') { const aus = a.y === 'block' ? a.aussagen : a.o, rows = [...box.querySelectorAll('.q-rfz')]; if (rows.some(r => r.dataset.v == null)) return;
        rows.forEach(r => r.classList.add((r.dataset.v === '1') === aus[+r.dataset.j][1] ? 'r-ok' : 'r-nok')); ok = rows.every(r => r.classList.contains('r-ok'));
        if (!ok) notiz = `${rows.filter(r => r.classList.contains('r-ok')).length} von ${rows.length} Aussagen richtig eingeschätzt. In der Klausur gibt es dafür 0 Punkte.`; }
      if (a.y === 'zuord') { const rows = [...box.querySelectorAll('.q-zrow')]; if (rows.some(r => !r.dataset.v)) return; ok = rows.every(r => r.dataset.v === a.k[a.e[+r.dataset.j][1]]); rows.forEach(r => r.classList.add(r.dataset.v === a.k[a.e[+r.dataset.j][1]] ? 'r-ok' : 'r-nok')); }
      if (a.y === 'beschr') { const rows = [...box.querySelectorAll('.q-zrow')]; if (rows.some(r => !r.dataset.v)) return; ok = rows.every(r => r.dataset.v === a.slots[+r.dataset.j]); }
      if (a.y === 'kurz') { const v = box.querySelector('.q-in').value; if (!norm(v)) return; const t = vergleich(v, a.ok); ok = !!t; if (t === 'fast') notiz = `Kleiner Tippfehler, zählt trotzdem. Richtig geschrieben: „${esc(a.ok[0])}“.`; }
      if (a.y === 'luecke') { const g = [...box.querySelectorAll('.q-gap')]; let fast = false;
        g.forEach(x => { const t = vergleich(x.value, a.l[+x.dataset.n]); if (t === 'fast') fast = true; x.classList.add(t ? 'r-ok' : 'r-nok'); });
        ok = g.every(x => x.classList.contains('r-ok')); if (ok && fast) notiz = 'Kleiner Tippfehler, zählt trotzdem.'; }
      if (a.y === 'num') { const v = num(box.querySelector('.q-in').value); if (isNaN(v)) return; const tol = a.tol ?? Math.max(.01, Math.abs(a.ans) * .005); ok = Math.abs(v - a.ans) <= tol;
        if (!ok && a.ans) { const q = v / a.ans;
          if (Math.abs(q - 1) < .02) notiz = 'Fast: Prüfe die Rundung (Zwischenergebnisse nicht zu früh runden).';
          else if ([100, .01, 1000, .001].some(f => Math.abs(q / f - 1) < .02)) notiz = 'Der Wert stimmt bis auf eine Zehnerpotenz: Prüfe Einheit oder Prozent (z. B. 5 % = 0,05).';
          else if (Math.abs(q + 1) < .02) notiz = 'Nur das Vorzeichen ist falsch.'; } }
      if (a.y === 'liste') { const v = listeText(box); if (!norm(v)) return; cur.treffer = listePruefen(v, a.pk);
        const n = cur.treffer.filter(Boolean).length, soll = Math.min(a.n || a.pk.length, a.pk.length); ok = n >= soll;
        const fehlt = a.pk.filter((p, j) => !cur.treffer[j]).map(p => p[0]);
        notiz = `${n} von ${soll} erkannt${!ok && fehlt.length ? ` · es fehlt z. B.: ${esc(fehlt.slice(0, soll - n).join(', '))}` : ''}.`; }
      commit(!!ok, notiz);
    };
    if (a.y === 'karte') {   // Karteikarte: umdrehen, dann gewusst / nicht gewusst, ohne Lösungsblock
      const card = box.querySelector('.q-kcard'), act = box.querySelector('.q-act');
      const knoepfe = () => { act.innerHTML = `<div class="sw-ctrl"><button class="btn sw-l">← Nicht gewusst</button><button class="btn sw-r">Gewusst →</button></div>`;
        act.querySelector('.sw-l').onclick = () => commit(false); act.querySelector('.sw-r').onclick = () => commit(true); };
      const dreh = () => { card.classList.toggle('flip'); if (!act.querySelector('.sw-r')) knoepfe(); };
      card.onclick = dreh; act.innerHTML = `<button class="btn btn-main q-dreh">Umdrehen</button>`; act.querySelector('.q-dreh').onclick = dreh;
      card.onkeydown = e => { if (e.key === ' ') { e.preventDefault(); dreh(); } if (e.key === 'ArrowRight' && act.querySelector('.sw-r')) commit(true); if (e.key === 'ArrowLeft' && act.querySelector('.sw-l')) commit(false); };
      card.focus({ preventScroll: true });
    }
    const show = box.querySelector('.q-show');
    if (show) show.onclick = () => {
      const ta = box.querySelector('.q-ta'); if (a.pk && ta && norm(ta.value)) cur.treffer = kernpunkte(ta.value, a.pk);
      const n = cur.treffer ? cur.treffer.filter(Boolean).length : 0;
      box.querySelector('.q-fb').innerHTML = `<div class="q-verdict">Ehrlicher Selbst-Check</div>${cur.treffer ? `<div class="q-notiz">${n} von ${a.pk.length} Kernpunkten in deinem Text erkannt (grün). Zähl selbst nach: Hast du die anderen sinngemäß?</div>` : ''}` + loesungHTML(cur);
      box.querySelector('.q-act').innerHTML = `<button class="btn q-self" data-v="1">Hatte ich</button><button class="btn q-self" data-v="0">Hatte ich nicht</button>`;
      box.querySelectorAll('.q-self').forEach(b => b.onclick = () => { if (opt.feedback === false) box.querySelector('.q-fb').innerHTML = ''; commit(b.dataset.v === '1'); });
    };
    const sk = box.querySelector('.q-skip'); if (sk) sk.onclick = () => { opt.skip(cur); i++; zeige(); };
    const qw = box.querySelector('.q-weiss'); if (qw) qw.onclick = () => { if (a.y === 'mc') box.querySelectorAll('.q-opt').forEach(x => a.o[+x.dataset.j][1] && x.classList.add('is-ok')); commit(false, 'Nicht gewusst: Das ist ehrlich und kommt in „Methodisch lernen“ wieder.'); };
    box.querySelectorAll('input.q-in,input.q-gap').forEach(x => x.onkeydown = e => { if (e.key === 'Enter') chk && chk.click(); });
    box.querySelectorAll('input.q-li').forEach((x, j, l) => x.onkeydown = e => { if (e.key === 'Enter') { e.preventDefault(); if (l[j + 1]) l[j + 1].focus(); else chk && chk.click(); } });
    if (a.y === 'liste') listeFortschritt(box, a);
  }
  zeige();
  return { res };
}

/* ---------- Endlos-Quiz, das mitwächst ---------- */
/* Endlos-Quiz: einfache Aufgabentypen ohne viel Schreiben; Erklären/Definieren liegen im Definitions-Drill */
const ENDLOS_TYPEN = new Set(['mc', 'mc_multi', 'block', 'zuord', 'reihe', 'beschr', 'hot', 'kurz', 'luecke', 'liste', 'num']);
/* Hilfe für die leichte Klausurform: Anfangsbuchstaben bzw. Ansatz, die Aufgabe selbst bleibt wie in der Klausur.
   Die Hilfe steht nicht in der Aufgabe, sondern erscheint erst auf Knopfdruck (Quiz: „Hilfe“, Arbeitsblatt: Rettungsring 1). Mit Hilfe gelöst = höchstens Stufe 3. */
function mitHilfe(a) {
  const anf = w => txt(w).trim().split(/\s+/).map(x => x[0]).join('').slice(0, 3).toUpperCase() + ' …';
  let h = '';
  if (a.y === 'liste') h = `Hilfe: ${a.n || a.pk.length} Punkte, Anfänge: ${a.pk.slice(0, a.n || a.pk.length).map(g => anf(g[0])).join(' · ')}`;
  else if (a.y === 'rev' && a.pk) h = `Hilfe: Diese Punkte gehören hinein: ${a.pk.map(x => anf(x)).join(' · ')}`;
  else if (a.y === 'num' && a.tipp) h = `Hilfe: ${a.tipp}`;
  else if (a.y === 'kurz' && a.ok) h = `Hilfe: beginnt mit „${txt(a.ok[0]).slice(0, 2)}…“`;
  return h ? { ...a, hilfe: h } : a;
}
/* Endlos-Quiz: Verstehen und Klausurform gemischt, ohne Wiederholungen.
   · Jede Frage (Familie + Variante) kommt in einer Sitzung erst wieder, wenn alle anderen der Auswahl dran waren.
   · Reihenfolge: wichtige Punkte und lange nicht gesehene Fragen zuerst (kein Mehrfach-Eintrag).
   · Wichtige Punkte gehen eine Leiter hoch: 0 erkennen → 1 verstehen → 2 Klausurform mit Hilfe → 3 Klausurform; nur mit noch nicht gestellten Fragen.
   · Falsch beantwortet: Punkt eine Stufe zurück, nach einer Klausurfrage zuerst eine Verständnisfrage; dieselbe Frage kommt genau einmal wieder, nach etwa 8 anderen.
   · Übrige Unterthemen: etwa jede dritte Frage im Klausurstil (anfangs mit Hilfe). */
function endlos(pool) {
  const fams = []; for (const x of pool) for (const fam of famsVon(x)) if (fam.a.some(a => ENDLOS_TYPEN.has(a.y))) fams.push({ x, fam });
  const nv = {}, gut = {}, schlecht = {};
  const basis = key => { const t = G.thema(key); return !t.n ? 1 : t.avg < 2 ? 0 : t.avg < 3.5 ? 1 : 2; };
  const gesehen = new Set(), vk = (fam, a) => fam.id + '#' + fam.a.indexOf(a);
  const offen = (fam, a) => !gesehen.has(vk(fam, a));
  /* zuletzt gesehen (über Sitzungen): frühester Zeitpunkt der Aufgabenarten dieser Familie im Gedächtnis */
  const alter = fam => { let t = Infinity; for (const y of new Set(fam.a.map(a => a.y))) { const e = S.g[`q:${fam.id}:${y}`]; t = Math.min(t, e && e.t ? e.t : 0); } return t; };
  const runde = () => shuffle(fams).map(e => { const t = alter(e.fam), tage = t ? (jetzt() - t) / DAY : 99;
    return { e, w: Math.random() + (e.fam.w ? .7 : 0) + (tage > 2 ? .4 : 0) }; }).sort((a, b) => b.w - a.w).map(z => z.e);
  let stapel = runde(), serie = 0, schwerer = false, nr = 0;
  const leiter = {}, spaeter = [];
  const punkt = e => e.fam.p ? e.x.f.id + ':' + e.fam.p : null;
  const famsPunkt = {}; for (const e of fams) { const p = punkt(e); if (p) (famsPunkt[p] = famsPunkt[p] || []).push(e); }
  const zuletzt = [], bFam = {};   // bFam: Begriff (Folien-Definition) → die Familie, die ihn in dieser Sitzung abfragt
  const lang = a => a.y === 'mc' && !a.weg && (() => { const l = a.o.map(o => txt(o[0]).length), r = l[a.o.findIndex(o => o[1])], rest = l.filter((_, j) => !a.o[j][1]);
    return l.reduce((x, y) => x + y, 0) / l.length > 45 || r > 1.5 * Math.max(...rest); })();
  const passt = v => ENDLOS_TYPEN.has(v.y) && !(zuletzt.length >= 2 && zuletzt.slice(-2).every(t => t === v.y)) && !(v.y === 'mc' && zuletzt.slice(-1)[0] === 'mc') && !lang(v);
  /* Variante wählen: nur noch nicht gestellte; Filter der Reihe nach, erst mit Abwechslung, dann ohne */
  const waehle = (fam, l, ...filter) => { const m0 = l.filter(v => offen(fam, v) && !(v.bv && bFam[v.bv] && bFam[v.bv] !== fam.id)); if (!m0.length) return null;
    for (const f of filter) { const m = m0.filter(v => f(v) && passt(v)); if (m.length) return pick(m); }
    for (const f of filter) { const m = m0.filter(f); if (m.length) return pick(m); } return null; };
  const kl = fam => fam.a.filter(v => v.klausur && ENDLOS_TYPEN.has(v.y)), ver = fam => fam.a.filter(v => !v.klausur && ENDLOS_TYPEN.has(v.y));
  const alle = fam => fam.a.filter(v => ENDLOS_TYPEN.has(v.y));
  const fertig = (e, a, art, hilfe) => { gesehen.add(vk(e.fam, a)); if (a.bv && !bFam[a.bv]) bFam[a.bv] = e.fam.id; zuletzt.push(a.y); if (zuletzt.length > 4) zuletzt.shift();
    const it = frageItem(e.x, e.fam, hilfe ? mitHilfe(a) : a); it.art = art; it.punkt = punkt(e); it.orig = a; return it; };
  const verstehen = (e, leicht) => { const a = waehle(e.fam, ver(e.fam), ...(leicht ? [v => (v.lvl || 1) <= 1, v => (v.lvl || 1) <= 2, () => true] : [v => (v.lvl || 1) === 2, () => true]));
    return a ? fertig(e, a, 'verstehen', false) : null; };
  const klausurfrage = (e, hilfe) => { const a = waehle(e.fam, kl(e.fam), () => true); return a ? fertig(e, a, 'klausur', hilfe) : null; };
  const item = e => {
    const { x, fam } = e, p = punkt(e);
    if (p) {   // wichtiger Punkt: Leiter, nur mit noch nicht gestellten Fragen
      const st = leiter[p] ?? 0;
      if (st >= 2) { const it = klausurfrage(e, st === 2) || (famsPunkt[p] || []).map(f => klausurfrage(f, st === 2)).find(Boolean); if (it) return it; }
      return verstehen(e, st === 0) || klausurfrage(e, st <= 2) || (() => { const a = waehle(fam, alle(fam), () => true); return a ? fertig(e, a, a.klausur ? 'klausur' : 'verstehen', false) : null; })();
    }
    const n = nv[x.key] ?? (nv[x.key] = basis(x.key));
    if (kl(fam).length && Math.random() < (n === 0 ? .25 : .35)) { const it = klausurfrage(e, n === 0); if (it) return it; }
    const a = waehle(fam, ver(fam), v => n === 0 ? (v.lvl || 1) <= 2 : n === 2 ? (v.lvl || 1) >= 2 : true, () => true) || waehle(fam, alle(fam), () => true);
    return a ? fertig(e, a, a.klausur ? 'klausur' : 'verstehen', false) : null;
  };
  /* nächste Familie mit noch offener Frage; ist alles gestellt, beginnt eine neue Runde */
  const naechste = () => {
    for (let versuch = 0; versuch < 2; versuch++) {
      while (stapel.length) {
        const j = stapel.slice(0, 8).findIndex(f => alle(f.fam).some(v => offen(f.fam, v) && passt(v)));
        const e = stapel.splice(j >= 0 ? j : 0, 1)[0];
        if (!alle(e.fam).some(v => offen(e.fam, v))) continue;
        if (e.fam.b && bFam[e.fam.b] && bFam[e.fam.b] !== e.fam.id) continue;   // dieselbe Definition nur über eine Familie
        const it = item(e); if (it) { if (e.fam.b) bFam[e.fam.b] = e.fam.id; return it; }
      }
      if (!fams.some(f => alle(f.fam).some(v => offen(f.fam, v)))) gesehen.clear();   // erst wenn wirklich alles gestellt ist, darf es wieder von vorn losgehen
      stapel = runde();
    }
    return null;
  };
  return {
    get serie() { return serie; }, get schwerer() { const h = schwerer; schwerer = false; return h; },
    next(i, res) {
      if (!fams.length) return null;
      nr++;
      const l = res[res.length - 1];
      if (l) { const k = l.item.key, p = l.item.punkt;
        if (l.ok) { serie++; schlecht[k] = 0; gut[k] = (gut[k] || 0) + 1; if (gut[k] >= 3 && nv[k] < 2) { nv[k]++; gut[k] = 0; schwerer = true; } }
        else { serie = 0; gut[k] = 0; schlecht[k] = (schlecht[k] || 0) + 1; if (schlecht[k] >= 2 && nv[k] > 0) { nv[k]--; schlecht[k] = 0; } }
        if (p) { const st = leiter[p] ?? 0; leiter[p] = l.ok ? Math.min(3, st + 1) : Math.max(0, st - 1); }
        if (!l.ok && !l.item.nochmal) {   // dieselbe Frage genau einmal wieder, nach etwa 8 anderen
          const e = { x: l.item.x, fam: l.item.fam }, a = l.item.orig || l.item.fam.a[l.item.gv.i];
          spaeter.push({ bei: nr + 8, mach: () => { const it = frageItem(e.x, e.fam, a); Object.assign(it, { art: l.item.art, punkt: l.item.punkt, orig: a, nochmal: true }); return it; } });
          if (l.item.art === 'klausur' && p) { const v = verstehen(e, false) || (famsPunkt[p] || []).map(f => verstehen(f, false)).find(Boolean); if (v) return v; }
        } }
      const f = spaeter.findIndex(z => z.bei <= nr);
      if (f >= 0) return spaeter.splice(f, 1)[0].mach();
      return naechste();
    },
  };
}

/* ---------- Karteikarten zum Swipen ---------- */
function kartenFuer(pool) {
  const keys = new Set(pool.map(x => x.t.id));
  const out = [];
  const nurW = pool.some(x => x.nurW);
  for (const f of new Set(pool.map(x => x.f))) for (const g of f.glossar) if (keys.has(g.t) && (!nurW || g.w)) out.push({ front: g.b, back: g.e, key: f.id + '/' + g.t, fach: f.name, id: `k:${f.id}:${g.b}`, w: g.w });
  for (const f of new Set(pool.map(x => x.f))) for (const c of f.karten || []) if (keys.has(c.t) && (!nurW || c.w)) out.push({ front: c.v, back: c.r, key: f.id + '/' + c.t, fach: f.name + (c.zf === 3 ? ' · in den Folien gestrichen, für die Klausur nicht nötig' : c.zf === 2 ? ' · nicht in den Folien, für die Klausur nicht nötig' : c.zf ? ' · nicht in den Folien' : ''), id: `c:${f.id}:${txt(c.v)}`, kr: c.kr, w: c.w, zf: c.zf });
  for (const x of pool) for (const [id, c] of Object.entries(S.eigen || {})) if (c.k === x.key) out.push({ front: c.v, back: c.r, key: x.key, fach: x.f.name + ' · deine Karte', eigen: 1, id: 'e:' + id });
  for (const x of pool) if (x.t.merk) out.push({ front: 'Merksatz · ' + x.t.title, back: txt(x.t.merk), key: x.key, fach: x.f.name, merk: 1, id: 'm:' + x.key });
  for (const x of pool) for (const m of (S.mark[x.key] || [])) if (m.farbe === 'gruen') out.push({
    front: m.notiz || (m.satz ? m.satz.replace(m.text, ' ____ ') : 'Was hast du hier markiert?'), back: m.text, key: x.key, fach: x.f.name + ' · von dir', eigen: 1, id: `g:${x.key}:${m.id}` });
  return out;
}
/* Karteikarten wie bei Quizlet: Was nicht gewusst war, kommt in der nächsten Runde wieder, bis alles sitzt.
   Die Sitzung wird gespeichert (opt.sitzung): Wer abbricht, macht später dort weiter. Jede Antwort geht sofort ins Gedächtnis. */
function swipe(el, karten, opt = {}) {
  const sk = opt.sitzung || 'karten', byId = Object.fromEntries(karten.map(c => [c.id, c]));
  const neu = () => ({ stapel: shuffle(karten).slice(0, opt.max || 30).map(c => c.id), nicht: [], runde: 1, erste: { g: 0, n: 0 }, name: opt.name || '', keys: opt.keys || [] });
  let z = S.ks[sk], weiter = false;
  if (z) { z.stapel = z.stapel.filter(id => byId[id]); z.nicht = z.nicht.filter(id => byId[id]); weiter = z.stapel.length + z.nicht.length > 0 && (z.runde > 1 || z.erste.g + z.erste.n > 0); }
  if (!z || !(z.stapel.length + z.nicht.length)) z = neu();
  const merke = () => { S.ks[sk] = z; save(); };
  merke();
  let pause = null;
  function neuStart() { clearTimeout(pause); z = neu(); weiter = false; merke(); zeige(); }
  function zeige() {
    if (!z.stapel.length && z.nicht.length) {   // Runde geschafft: sofort weiter mit den nicht gewussten
      const n = z.nicht.length;
      el.innerHTML = `<div class="sw-end"><div class="sw-runde"><span>Runde ${z.runde} geschafft</span><b>Jetzt nochmal die ${n} ${n === 1 ? 'Karte' : 'Karten'}, die du nicht gewusst hast.</b><i class="sw-zeit"></i></div>
        <button class="btn btn-main sw-los">Sofort weiter</button><button class="btn sw-stop">Später weitermachen</button></div>`;
      const los = () => { clearTimeout(pause); z.stapel = shuffle(z.nicht); z.nicht = []; z.runde++; merke(); zeige(); };
      pause = setTimeout(los, 2200);
      el.querySelector('.sw-los').onclick = los;
      el.querySelector('.sw-stop').onclick = () => { clearTimeout(pause); el.innerHTML = `<div class="sw-end"><div class="sw-sum">Gespeichert. Beim nächsten Öffnen geht es mit den ${n} Karten weiter.</div></div>`; };
      return;
    }
    if (!z.stapel.length) {
      const e = z.erste; delete S.ks[sk]; save();
      el.innerHTML = `<div class="sw-end"><div class="sw-sum"><b>Alles gewusst.</b> ${z.runde === 1 ? 'Gleich beim ersten Durchgang.' : `Beim ersten Durchgang ${e.g} gewusst, ${e.n} nicht. Nach ${z.runde} Runden sitzt jetzt alles.`}</div>
        <button class="btn btn-main sw-new">Neu mischen</button></div>`;
      el.querySelector('.sw-new').onclick = neuStart;
      return;
    }
    const sicht = z.stapel.slice(0, 3).map(id => byId[id]);
    el.innerHTML = `${weiter ? `<div class="sw-weiter">Du machst dort weiter, wo du aufgehört hast. <button class="sw-neu">Neu beginnen</button></div>` : ''}
      <div class="sw-wrap"><div class="sw-stack">${sicht.map((c, j) => `<div class="sw-card${j ? ' behind b' + j : ''}"${j ? '' : ' tabindex="0"'}>
        <div class="sw-face sw-front"><small>${esc(c.fach)}</small><div class="sw-t">${schoen(esc(c.front))}</div><span class="sw-tap">antippen zum Umdrehen</span></div>
        <div class="sw-face sw-back"><small>${schoen(esc(c.front))}</small><div class="sw-e">${schoen(esc(c.back))}</div></div></div>`).reverse().join('')}</div>
      <div class="sw-ctrl"><button class="btn sw-l" title="Pfeil links">← Nicht gewusst</button><span class="sw-n">${z.runde > 1 ? `Runde ${z.runde} · ` : ''}${z.stapel.length} übrig</span><button class="btn sw-r" title="Pfeil rechts">Gewusst →</button></div></div>`;
    el.querySelector('.sw-neu')?.addEventListener('click', neuStart);
    const card = el.querySelector('.sw-card:not(.behind)');
    let x0 = null, dx = 0, moved = false, fort = false;
    const weg = dir => {
      if (fort) return; fort = true; weiter = false;
      card.style.transition = 'transform .25s, opacity .25s'; card.style.transform = `translateX(${dir * 140}%) rotate(${dir * 18}deg)`; card.style.opacity = 0;
      const id = z.stapel.shift(), c = byId[id];
      G.antwort(id, dir > 0, { k: c.key, runde: z.runde });
      if (dir < 0) z.nicht.push(id);
      if (z.runde === 1) z.erste[dir > 0 ? 'g' : 'n']++;
      merke(); setTimeout(zeige, 220);
    };
    card.onpointerdown = e => { x0 = e.clientX; dx = 0; moved = false; card.setPointerCapture(e.pointerId); card.style.transition = 'none'; };
    card.onpointermove = e => { if (x0 === null) return; dx = e.clientX - x0; if (Math.abs(dx) > 6) moved = true; card.style.transform = `translateX(${dx}px) rotate(${dx / 18}deg)`; card.dataset.hint = dx > 40 ? 'r' : dx < -40 ? 'l' : ''; };
    card.onpointerup = () => { if (x0 === null) return; x0 = null; if (Math.abs(dx) > 90) weg(Math.sign(dx)); else { card.style.transition = 'transform .2s'; card.style.transform = ''; card.dataset.hint = ''; if (!moved) card.classList.toggle('flip'); } };
    el.querySelector('.sw-l').onclick = () => weg(-1);
    el.querySelector('.sw-r').onclick = () => weg(1);
    el.onkeydown = e => { if (e.key === 'ArrowLeft') weg(-1); if (e.key === 'ArrowRight') weg(1); if (e.key === ' ') { e.preventDefault(); card.classList.toggle('flip'); } };
  }
  el.tabIndex = -1; zeige();
}

/* Kernpunkte einer Definition: an Satzzeichen und „und“ in 2–4 Teile zerlegen (für die Prüfung beim Schreiben) */
function kernteile(def) {
  const t = txt(def).split(/[,;:–]|\s+und\s+|\s+sowie\s+|\.\s/).map(x => x.trim()).filter(x => x.split(/\s+/).length >= 2);
  return (t.length ? t : [txt(def)]).slice(0, 4);
}
/* Definitions-Drill, Modus „Schreiben“: Begriff selbst definieren (Glossar) oder Erklär-Fragen (rev) beantworten */
/* Wie tief der Definitionsdrill geht, legt das Fachprofil fest (f.tiefe):
   1 = nur Punkte, die so in der Klausur verlangt werden · 2 = dazu die Begriffe der Klausurthemen (Stern) · 3 = alle Begriffe */
function drillKarten(pool) {
  const alle = kartenFuer(pool).filter(c => !c.merk && !c.eigen && TOP[c.key]);
  const k = alle.filter(c => { const x = TOP[c.key], t = x.f.tiefe || 3; return c.kr || t >= 3 || (t >= 2 && x.t.star); });
  return k.length >= 4 ? k : alle;
}
function drillSchreiben(el, pool, kopfFn) {
  const karten = drillKarten(pool);
  const erklaer = []; for (const x of pool) for (const fam of famsVon(x)) for (const a of fam.a) if (a.y === 'rev') { erklaer.push({ x, fam, a }); break; }
  if (!karten.length && !erklaer.length) { el.innerHTML = '<div class="leer">In dieser Auswahl gibt es keine Begriffe und Erklär-Fragen.</div>'; return; }
  let serie = 0, best = 0;
  quiz(el, {
    weiterText: 'Nächster',
    next: () => {
      if (karten.length && (Math.random() < .65 || !erklaer.length)) {
        const c = pick(karten), x = TOP[c.key];
        const pk = kernteile(c.back);
        return { a: { y: 'rev', p: `Definieren Sie: <b>${esc(c.front)}</b>`, pk, tipps: defTipps(c.back, pk), l: `<p>${esc(c.back)}</p>` }, t: x.t, f: x.f, k: x.k, key: c.key, w: c.w,
          gid: `b:${c.key.split('/')[0]}:${c.front}`, gv: { modus: 'schreiben' } };
      }
      const { x, fam, a } = pick(erklaer); return frageItem(x, fam, a);
    },
    kopf: (i, res) => { const l = res[res.length - 1]; if (l) { serie = l.ok ? serie + 1 : 0; best = Math.max(best, serie); } return kopfFn ? kopfFn(serie, best, res) : ''; },
  });
}
/* ---------- Definitions-Drill: Begriff zur Erklärung, Lücken, Kurzantworten – schnell hintereinander ---------- */
function drill(el, pool, kopfFn, stufe = 'klausur') {
  const karten = drillKarten(pool);
  const fragen = ziehFragen(pool, 80, stufe, ['luecke', 'kurz']);
  let streak = 0, best = 0;
  /* falsche Antwortoptionen: zuerst aus demselben Oberthema, dann aus demselben Fach (nie offensichtlich fachfremd) */
  const ablenker = c => { const x = TOP[c.key], gleich = karten.filter(y => y.front !== c.front && TOP[y.key].k === x.k), fach = karten.filter(y => y.front !== c.front && TOP[y.key].f === x.f && TOP[y.key].k !== x.k);
    return [...shuffle(gleich), ...shuffle(fach)].slice(0, 3); };
  quiz(el, {
    weiterText: 'Nächste',
    next: () => {
      if (karten.length >= 4 && (Math.random() < .55 || !fragen.length)) {
        const c = pick(karten), x = TOP[c.key], def = `<span class="drill-def">„${esc(c.back)}“</span>`;
        const gid = `b:${c.key.split('/')[0]}:${c.front}`;
        if (streak >= 5) return { a: { y: 'kurz', p: def + '<br><small>Welcher Begriff ist das? Eintippen.</small>', ok: [c.front, c.front.replace(/\s*\(.*?\)\s*/g, ' ').trim(), c.front.split(': ').slice(1).join(': ')].filter(Boolean) }, t: x.t, f: x.f, k: x.k, key: c.key, w: c.w, gid, gv: { modus: 'tippen' } };
        return { a: { y: 'mc', p: def + '<br><small>Welcher Begriff ist das?</small>', o: shuffle([[esc(c.front), true], ...ablenker(c).map(f => [esc(f.front), false])]) }, t: x.t, f: x.f, k: x.k, key: c.key, w: c.w, gid, gv: { modus: 'wahl' } };
      }
      return fragen.length ? fragen[Math.random() * fragen.length | 0] : null;
    },
    kopf: (i, res) => { const l = res[res.length - 1]; if (l) { streak = l.ok ? streak + 1 : 0; best = Math.max(best, streak); } return kopfFn ? kopfFn(streak, best, res) : `<span class="drill-streak">Serie ${streak}</span>`; },
  });
}

/* ---------- Arbeitsblatt: große Aufgaben (a–d) und Fragen als Papier-Aufgaben, mit Rettungsringen ---------- */
const ARTEN = [['rechnen', 'Rechnen'], ['anwendung', 'Anwendung'], ['transfer', 'Transfer'], ['zeichnen', 'Zeichnen']];
const ARTNAME = Object.fromEntries(ARTEN);
function artVon(a) {
  if (a.zeichnen) return 'zeichnen';
  if (a.y === 'num') return 'rechnen';
  if (a.y === 'beschr' || a.y === 'hot') return 'zeichnen';
  if (a.y === 'rev') return (a.lvl || 1) >= 3 ? 'transfer' : 'anwendung';
  if (a.y === 'liste' || a.y === 'zuord') return 'anwendung';
  return null;
}
/* Frage → Papier-Aufgabe (ein Teil). Auswahl- und Lückenfragen werden zu statischem Text zum Ankreuzen/Ausfüllen. */
function papierText(a) {
  const bild = a.bild ? `<div class="q-bild">${a.bild}</div>` : '';
  if (a.y === 'mc') return `${a.p}<ol class="ws-opt" type="A">${a.o.map(o => `<li>${o[0]}</li>`).join('')}</ol>`;
  if (a.y === 'mc_multi' || a.y === 'block') return `${a.p}<p class="ws-hinw">Jede Aussage: richtig oder falsch?</p><ol class="ws-opt">${(a.y === 'block' ? a.aussagen : a.o).map(o => `<li>${o[0]} <span class="ws-rf">R / F</span></li>`).join('')}</ol>`;
  if (a.y === 'luecke') return a.p.replace(/\[\[(\d+)\]\]/g, '<span class="ws-luecke"></span>');
  if (a.y === 'zuord') return `${a.p}<ul class="ws-opt">${a.e.map(e => `<li>${e[0]}</li>`).join('')}</ul><p class="ws-hinw">Kategorien: ${a.k.join(' · ')}</p>`;
  if (a.y === 'reihe') return `${a.p}<ul class="ws-opt">${shuffle(a.o).map(o => `<li>${o}</li>`).join('')}</ul>`;
  if (a.y === 'beschr') return `${a.p}${bild}<p class="ws-hinw">Begriffe: ${shuffle(a.slots.concat(a.extra || [])).join(' · ')}</p>`;
  return a.p + bild;
}
/* Passt eine Fragenart zum Stil der echten Klausur des Fachs (f.mix aus dem Klausurprofil)?
   2 = kommt so in der Klausur vor · 1 = offene Antwort (immer klausurnah) · 0 = Antippen/Zuordnen, das es in dieser Klausur nicht gibt */
const OFFEN = new Set(['num', 'kurz', 'liste', 'luecke', 'rev', 'beschr']);
function klausurStil(f, y) {
  const mix = (f && f.mix) || {};
  if (mix[y] || (y === 'block' && mix.mc_multi)) return 2;
  return OFFEN.has(y) ? 1 : 0;
}
/* Rettungsringe mit echtem Inhalt: Ring 1 = konkrete Denkhilfe oder gleich die Formel, Ring 2 = Ansatz bzw. ein Teil der Lösung.
   Nie nur „schau dir die Formel an“. */
const anfaenge = l => l.map(w => { const t = txt(w).trim(); return t.slice(0, Math.min(3, t.length)) + '…'; }).join(' · ');
const kurzSatz = s => { const t = txt(s || ''); const m = t.match(/^.{20,220}?[.!?](\s|$)/); return m ? m[0].trim() : t.slice(0, 220); };
/* Formeln eines Unterthemas „in Worten“ (aus den Formel-Kacheln), für Rechenaufgaben ohne eigene Formelangabe */
function formelnVon(t) {
  const h = (t && (t.html || t.article)) || '', out = [];
  const re = /<div class="fx-n">([\s\S]*?)<\/div>[\s\S]*?<div class="fx-iw"><b>In Worten<\/b>([\s\S]*?)<\/div>/g; let m;
  while ((m = re.exec(h)) && out.length < 4) out.push(`<b>${txt(m[1])}:</b> ${txt(m[2])}`);
  return out;
}
function rettungsringe(a, t) {
  const merk = t && t.merk ? kurzSatz(t.merk) : '', kern = t && t.kern ? kurzSatz(t.kern) : '';
  if (a.y === 'num') {
    const f = a.tipp ? `Formel: ${a.tipp}` : (formelnVon(t).join('<br>') || kern);
    return { tipp1: f, tipp2: a.ansatz ? `Ansatz: ${a.ansatz}` : (a.tipp ? `${a.tipp}<br>Setze die Werte aus der Aufgabe mit Einheit ein und rechne Schritt für Schritt.` : merk) };
  }
  if (a.y === 'liste' && a.pk) { const n = a.n || a.pk.length;
    return { tipp1: `${n} ${n === 1 ? 'Punkt' : 'Punkte'}, sie beginnen so: ${anfaenge(a.pk.slice(0, Math.min(a.pk.length, Math.max(n, 3))).map(g => g[0]))}`, tipp2: `Zwei Punkte ganz: ${a.pk.slice(0, 2).map(g => txt(g[0])).join(' · ')}` }; }
  if (a.y === 'rev' && a.pk) return { tipp1: `Diese Punkte gehören hinein: ${anfaenge(a.pk)}`, tipp2: `Ein Kernpunkt ganz: ${txt(a.pk[0])}` };
  if (a.y === 'kurz' && a.ok) { const w = txt(a.ok[0]);
    return { tipp1: `Gesucht ist ein Fachbegriff mit ${w.replace(/\s/g, '').length} Zeichen, er beginnt mit „${w.slice(0, 2)}…“.`, tipp2: merk || kern }; }
  if (a.hilfe) return { tipp1: a.hilfe.replace(/^Hilfe: /, ''), tipp2: merk || kern };
  return { tipp1: kern || merk || 'Welcher Begriff des Unterthemas ist gemeint?', tipp2: merk || kern };
}
/* Aufzählung: jedes Feld wird nach dem Tippen geprüft. Erkannte Punkte werden durchgestrichen (grün), doppelt genannte
   markiert, oben steht „2 von 5 erkannt“. Verraten wird nichts: es zählt nur, was man selbst geschrieben hat. */
function listeFortschritt(box, a) {
  const felder = [...box.querySelectorAll('input.q-li')], n = Math.min(a.n || a.pk.length, a.pk.length), hint = box.querySelector('.q-hint');
  const pruefe = () => {
    const belegt = new Set(); let ok = 0;
    felder.forEach(f => {
      f.classList.remove('q-li-ok', 'q-li-dopp'); const v = f.value.trim(); if (norm(v).length < 3) return;
      const t = listePruefen(v, a.pk), i = t.findIndex((x, k) => x && !belegt.has(k));
      if (i >= 0) { belegt.add(i); ok++; f.classList.add('q-li-ok'); } else if (t.some(Boolean)) f.classList.add('q-li-dopp');
    });
    if (hint) hint.innerHTML = `Gefragt: ${n} ${n === 1 ? 'Punkt' : 'Punkte'}. <b class="q-li-zahl">${ok} von ${n} erkannt</b>${felder.some(f => f.classList.contains('q-li-dopp')) ? ' · ein Punkt ist doppelt' : ''}`;
  };
  let t = 0;
  felder.forEach(f => { f.addEventListener('input', () => { clearTimeout(t); t = setTimeout(pruefe, 700); }); f.addEventListener('blur', pruefe); f.addEventListener('keydown', e => { if (e.key === 'Enter') pruefe(); }); });
}
function ausFrage(it) {
  const a = it.a, art = artVon(a) || 'kurz', max = typeof punkteVon === 'function' ? punkteVon(a) : 2;
  const { tipp1, tipp2 } = rettungsringe(a, it.t);
  return { titel: it.t.title, w: it.fam && it.fam.w, art, stufe: a.lvl || 1, klausur: !!a.klausur, punkte: max, quelle: it.f.name, ausgang: '', key: it.key, t: it.t, frage: true,
    teile: [{ text: papierText(a), punkte: max, tipp1, tipp2, loesungQ: it, ergebnis: a.y === 'num' ? a.ans : null, einheit: a.u || '', tol: a.tol }] };
}
function ausAufgabe(f, A) {
  const x = TOP[f.id + '/' + A.unter.find(u => TOP[f.id + '/' + u])];
  return { ...A, klausur: !!A.klausur || /Übung|Probeklausur|Klausurstil|Fallstudie/.test(A.quelle || ''), punkte: A.teile.reduce((s, t) => s + t.punkte, 0), quelle: A.quelle, key: x ? x.key : '', t: x ? x.t : { title: A.titel }, gross: A.teile.length > 1 };
}
/* Niveau des Arbeitsblatts: Einfach (grund) · Mittel (klausur) · Klausurniveau (klausurmaessig, früher auch „schwer“) */
const BLATT_NIVEAU = [['grund', 'Einfach'], ['klausur', 'Mittel'], ['klausurmaessig', 'Klausurniveau']];
const blattNiveau = st => st === 'grund' ? 'grund' : st === 'klausur' ? 'klausur' : 'klausurmaessig';
const passtStufe = (st, A) => st === 'grund' ? A.stufe <= 2 : st === 'klausur' ? A.stufe >= 2 : true;
/* Blatt ziehen: Teile mit Aufgaben und Reserve (zum Tauschen einzelner Aufgaben) */
/* Teilaufgabe aus dem Probeklausur-Bogen (Klausur- und Übungsaufgaben) als Arbeitsblatt-Aufgabe */
function ausVariante(f, K, T, v) {
  const x = TOP[f.id + '/' + v.unter], rechnet = v.felder.some(fd => fd.typ !== 'text' && fd.typ !== 'rf');
  const fo = x ? formelnVon(x.t) : [];
  const tipp1 = rechnet ? (fo.length ? 'Die Formeln dazu:<br>' + fo.join('<br>') : (x && x.t.merk ? 'Merksatz: ' + kurzSatz(x.t.merk) : 'Schreibe zuerst die allgemeine Formel hin, dann setze ein.'))
    : (x && x.t.merk ? 'Merksatz: ' + kurzSatz(x.t.merk) : 'Antworte in Stichworten, aber vollständig.');
  const name = fd => fd.label ? txt(mathe(fd.label)).replace(/=\s*$/, '').trim() : '';
  const basis = { id: 'kv-' + v.id, w: v.w, titel: K.titel, art: rechnet ? 'rechnen' : 'transfer', stufe: 3, klausur: true, punkte: T.punkte, quelle: '', key: x ? x.key : '', t: x ? x.t : { title: K.titel }, kv: true };
  /* mehrere Ergebnisse (x₁, x₂, …): Aufgabentext als Ausgangslage, je Ergebnis eine Teilaufgabe a), b), c) mit eigener Prüfung */
  if (v.felder.length > 1 && v.felder.every(fd => fd.p)) {
    const weg = `<details class="ws-weg"><summary>ganzer Lösungsweg</summary>${v.loesung}</details>`;
    return Object.assign(basis, { ausgang: v.text, teile: v.felder.map(fd => {
      const lab = fd.label ? fd.label.replace(/\s*=\s*(\\\))?$/, '$1') : '';
      return { text: fd.typ === 'text' || fd.typ === 'rf' ? (lab || 'Erläutern Sie.') : `${fd.typ === 'matrix' || fd.typ === 'ausdruck' ? 'Berechnen' : 'Bestimmen'} Sie ${lab}.`, punkte: fd.p, tipp1,
        tipp2: name(fd) ? 'Gesucht: ' + name(fd) : 'Vergleiche mit dem Merksatz des Unterthemas.',
        loesung: (fd.typ === 'text' ? '' : `<b>${sollText(fd)}</b><br>`) + weg, ergebnis: fd.typ === 'zahl' ? +fd.loesung : null, einheit: fd.einheit || '', tol: fd.tol }; }) });
  }
  const z = v.felder.filter(fd => fd.typ === 'zahl'), was = v.felder.map(name).filter(Boolean);
  const rf = v.felder.find(fd => fd.typ === 'rf');   // 4er-Block: Aussagen zum Ankreuzen auf Papier
  const text = (v.text || 'Kreuzen Sie an: richtig oder falsch? (4er-Block, nur alles richtig gibt Punkte)') + (rf ? `<ol class="ws-opt">${rf.aussagen.map(a => `<li>${a[0]} <span class="ws-rf">R / F</span></li>`).join('')}</ol>` : '');
  return Object.assign(basis, { ausgang: '', teile: [{ text: rf ? text : v.text, punkte: T.punkte, loesung: v.loesung, tipp1,
      tipp2: was.length ? 'Gesucht: ' + was.join(' · ') : 'Vergleiche mit dem Merksatz des Unterthemas.',
      ergebnis: z.length === 1 && v.felder.length === 1 ? +z[0].loesung : null, einheit: z.length === 1 ? (z[0].einheit || '') : '' }] });
}
/* Mischen mit Vorrang: aus „vor“ (Klausur- und Übungsaufgaben) je zwei, dann eine aus „rest“ */
function vorrangMix(vor, rest, je = 2) {
  const out = [], a = vor.slice(), b = rest.slice();
  while (a.length || b.length) { for (let i = 0; i < je && a.length; i++) out.push(a.shift()); if (b.length) out.push(b.shift()); }
  return out;
}
function blattZiehen(pool, opt) {
  const stufe = blattNiveau(opt.stufe), arten = opt.arten || ARTEN.map(a => a[0]), ids = new Set(pool.map(x => x.key));
  const eigene = [];
  const nurW = pool.some(x => x.nurW);
  for (const f of new Set(pool.map(x => x.f))) for (const A of (f.aufgaben || [])) if (A.unter.some(u => ids.has(f.id + '/' + u)) && (!nurW || A.w)) eigene.push(ausAufgabe(f, A));
  /* auf Mittel und Klausurniveau: Aufgaben aus Klausuren und Übungen (Probeklausur-Bogen) kommen bevorzugt dran */
  if (stufe !== 'grund') for (const f of new Set(pool.map(x => x.f))) if (f.klausur) for (const K of f.klausur.aufgaben) for (const T of K.teile) for (const v of T.varianten)
    if (ids.has(f.id + '/' + v.unter) && (!nurW || v.w)) eigene.push(ausVariante(f, K, T, v));
  const alleFragen = ziehFragen(pool, 200, stufe === 'grund' ? 'grund' : 'klausur').map(ausFrage);
  const stilOk = A => !A.frage || klausurStil(F[(A.key || '').split('/')[0]], A.teile[0].loesungQ.a.y) > 0;   // kein Antippen, wo die Klausur keins hat
  const wv = l => vorrangMix(l.filter(A => A.w), l.filter(A => !A.w), 2);
  /* Klausurniveau: erst alle Fragen aus Klausuren, Probeklausur und Übungen, dann eigene; Mittel: gemischt (1 : 1) */
  const fragen = stufe === 'grund' ? alleFragen : stufe === 'klausurmaessig' ? [...alleFragen.filter(A => A.klausur), ...alleFragen.filter(A => !A.klausur)]
    : vorrangMix(alleFragen.filter(A => A.klausur), alleFragen.filter(A => !A.klausur), 1);
  if (stufe === 'klausurmaessig') {   // wie die Klausur: erst kurze Aufgaben, dann große, schwere
    const stil = stilOk;
    /* Klausurniveau: NUR Aufgaben, die so in Klausuren und Übungen vorkommen (keine eigenen Übungsfragen als Füllung) */
    const kurz = wv(fragen.filter(A => A.klausur && A.punkte <= 3 && stil(A))), ziel = opt.ziel || 40;
    const ok = A => A.klausur && A.stufe >= 3 && A.punkte >= 4 && arten.includes(A.art), gE = eigene.filter(ok);
    const kand = [...wv(shuffle(gE.filter(A => A.kv))), ...wv(shuffle(gE.filter(A => !A.kv))), ...wv(fragen.filter(A => A.klausur && A.punkte >= 4 && arten.includes(A.art) && stil(A)))], gross = [];
    const teilA = kurz.slice(0, 4); let summe = teilA.reduce((s, A) => s + A.punkte, 0);
    for (const A of kand) { if (gross.length && summe + A.punkte > ziel + 3) continue; gross.push(A); summe += A.punkte; if (summe >= ziel - 2) break; }
    /* Fächer ohne kurze Klausuraufgaben (z. B. nur „Nennen und erklären“ mit 6–10 Punkten): nur ein Teil */
    if (teilA.length < 2) return [{ name: '', liste: gross, reserve: kand.filter(A => !gross.includes(A)) }];
    return [{ name: 'Teil A · kurze Aufgaben', liste: teilA, reserve: kurz.slice(4) }, { name: 'Teil B · große Aufgaben', liste: gross, reserve: kand.filter(A => !gross.includes(A)) }];
  }
  const pE = eigene.filter(A => arten.includes(A.art) && passtStufe(stufe, A));
  /* Einfach und Mittel: vor allem Klausurstil (2 : 1), Wichtiges zuerst (2 : 1); Übungsfragen nur in Formen, die die Klausur auch hat.
     Einfach: Klausuraufgaben in leichter Form (mit Hilfe: Anfänge, Ansatz), je Familie eine. */
  const einfach = stufe !== 'grund' ? [] : (() => { const out = [];
    for (const x of pool) for (const fam of famsVon(x)) for (const a of shuffle(fam.a.filter(a => a.klausur && ['liste', 'kurz', 'num', 'luecke', 'beschr', 'mc_multi', 'block', 'rev'].includes(a.y))).slice(0, 1))
      out.push({ ...ausFrage(frageItem(x, fam, mitHilfe(a))), stufe: 2, klausur: true });
    return out.filter(A => arten.includes(A.art)); })();
  const uebung = fragen.filter(A => !A.klausur && arten.includes(A.art) && passtStufe(stufe, A) && stilOk(A));
  const passend = stufe === 'grund'
    ? vorrangMix(wv(shuffle([...pE.filter(A => A.klausur), ...einfach])), shuffle([...pE.filter(A => !A.klausur), ...uebung]), 2)
    : vorrangMix(wv(shuffle([...pE.filter(A => A.klausur), ...fragen.filter(A => A.klausur && arten.includes(A.art))])), shuffle([...pE.filter(A => !A.klausur), ...uebung]), 2);
  const n = opt.n || 5;
  return [{ name: '', liste: passend.slice(0, n), reserve: passend.slice(n) }];
}
/* Gedächtnis-ID eines Teils: große Aufgabe → Teilaufgabe, sonst die zugrunde liegende Frage */
const teilId = (A, j) => A.teile[j].loesungQ ? A.teile[j].loesungQ.gid : A.id ? `a:${(A.key || '').split('/')[0]}:${A.id}:${j}` : null;
function teilHTML(T, j, mehrere) {
  return schoen(`<li class="ws-teil" data-j="${j}"><div class="ab-tt">${mehrere ? `<span class="ab-bu">${'abcdefghijklmnopqrstuvwxyz'[j]})</span>` : ''}<div class="ws-p">${T.text}</div>${mehrere ? `<em>${T.punkte} P</em>` : ''}</div>
    <div class="ws-tools">
      <button class="ring" data-r="1"><span class="ring-ic"></span>Rettungsring 1</button>
      <button class="ring" data-r="2"><span class="ring-ic"></span>Rettungsring 2</button>
      <button class="ring ring-l" data-r="3">Lösung</button>
      <button class="ring ws-nach" title="Die Stelle im Lerntext öffnen">${IC_LUPE}Nachschlagen</button>
      ${T.ergebnis != null ? `<span class="ws-check"><input class="q-in" inputmode="decimal" placeholder="Ergebnis prüfen" aria-label="Ergebnis prüfen"><span class="q-unit">${esc(T.einheit || '')}</span></span>` : ''}
    </div>
    <div class="ws-out" data-o="1" hidden><b>Rettungsring 1 · Denkanstoß</b>${T.tipp1}</div>
    <div class="ws-out" data-o="2" hidden><b>Rettungsring 2 · Ansatz</b>${T.tipp2}</div>
    <div class="ws-out ws-sol" data-o="3" hidden><b>Lösungsweg</b>${T.loesungQ ? loesungHTML(T.loesungQ) : T.loesung}${T.loesungQ && T.loesungQ.a.y === 'num' ? `<div class="ws-res">= ${zahl(T.loesungQ.a.ans, 4)} ${esc(T.einheit || '')}</div>` : ''}
      <div class="ab-selbst"><span>Konntest du es?</span><button data-selbstab="1">Ja</button><button data-selbstab="0.5">Teilweise</button><button data-selbstab="0">Nein</button><small class="ab-hinweis">„Nein“ und „Teilweise“ kommen später unter Methodisch lernen zurück, „Ja“ wird zurückgestellt.</small></div></div></li>`);
}
function aufgabeHTML(A, nr, tauschbar) {
  const mehrere = A.teile.length > 1;
  return `<section class="ab-a ws-task" data-nr="${nr}">
    <div class="ab-ak"><span class="ab-nr">Aufgabe ${nr}</span><b class="ab-ti">${esc(A.titel)}</b>${A.w ? '<b class="bdg-w">Wichtig</b>' : ''}<span class="ab-art">${ARTNAME[A.art] || 'Kurz'}</span><span class="ab-p">${A.punkte} P</span>
      ${tauschbar ? '<button class="ab-tausch" title="Gegen eine andere Aufgabe tauschen">⇄ tauschen</button>' : ''}<button class="q-melde" title="Fehler melden" aria-label="Fehler melden" data-melde="Aufgabe · ${esc(A.quelle && A.frage ? A.quelle : '')} ${esc(A.titel)}">⚑</button></div>
    ${A.ausgang ? `<div class="ws-ausgang">${schoen(A.ausgang)}</div>` : ''}
    <ol class="ws-teile">${A.teile.map((T, j) => teilHTML(T, j, mehrere)).join('')}</ol>
    ${A.quelle && !A.frage ? `<div class="ab-src">${esc(A.quelle)}</div>` : ''}</section>`;
}
function blatt(el, pool, opt = {}) {
  /* ganzes Blatt neu: frisch ziehen, schon gezeigte Aufgaben möglichst durch noch nicht gezeigte ersetzen */
  const gesehen = opt.gesehen || (opt.gesehen = new Set()), kennung = A => A.id || A.titel;
  const teile = opt.nur ? [{ name: '', liste: opt.nur, reserve: [] }] : blattZiehen(pool, opt);   // opt.nur: genau diese Aufgaben (z. B. aus den Originalfolien)
  for (const t of teile) t.liste = t.liste.map(A => {
    if (!gesehen.has(kennung(A))) return A;
    const j = t.reserve.findIndex(B => !gesehen.has(kennung(B)) && B.art === A.art), k = j >= 0 ? j : t.reserve.findIndex(B => !gesehen.has(kennung(B)));
    if (k < 0) return A; const neu = t.reserve.splice(k, 1)[0]; t.reserve.push(A); return neu;
  });
  teile.forEach(t => t.liste.forEach(A => gesehen.add(kennung(A))));
  const alle = teile.flatMap(t => t.liste);
  if (!alle.length) { el.innerHTML = `<div class="leer">Für diese Auswahl gibt es keine passenden Aufgaben. Anderes Niveau oder mehr Aufgabenarten wählen.</div>`; return; }
  const niv = (BLATT_NIVEAU.find(n => n[0] === blattNiveau(opt.stufe)) || [])[1] || '';
  function zeichne() {
    const summe = teile.reduce((s, t) => s + t.liste.reduce((u, A) => u + A.punkte, 0), 0); let nr = 0;
    el.innerHTML = `<article class="ab">${opt.kopf === false ? '' : `<header class="ab-kopf"><div><small>Arbeitsblatt · zur Selbstkontrolle</small><h2>${esc(opt.titel || 'Übungsblatt')}</h2></div>
        <dl class="ab-meta"><div><dt>Niveau</dt><dd>${niv}</dd></div><div><dt>Punkte</dt><dd>${summe}</dd></div><div><dt>Richtzeit</dt><dd>${summe} min</dd></div></dl><button class="ab-neu" title="Alle Aufgaben gegen neue tauschen">⟳ Ganzes Blatt neu</button></header>`}
      ${teile.map((t, ti) => `${t.name && t.liste.length ? `<h3 class="ab-teil">${t.name}</h3>` : ''}${t.liste.map((A, i) => `<div data-ti="${ti}" data-i="${i}">${aufgabeHTML(A, ++nr, t.reserve.length > 0)}</div>`).join('')}`).join('')}${opt.kopf === false && !opt.nur ? '<div class="ab-fuss"><button class="ab-neu" title="Alle Aufgaben gegen neue tauschen">⟳ Ganzes Blatt neu</button></div>' : ''}</article>`;
    el.querySelectorAll('.ab-neu').forEach(b => b.onclick = () => { blatt(el, pool, opt); el.scrollIntoView({ block: 'start', behavior: 'smooth' }); });
    el.querySelectorAll('[data-ti]').forEach(w => verdrahteAufgabe(w, teile[+w.dataset.ti].liste[+w.dataset.i], teile[+w.dataset.ti], +w.dataset.i));
  }
  function verdrahteAufgabe(w, A, teil, i) {
    w.querySelector('.ab-tausch')?.addEventListener('click', () => {   // nur diese Aufgabe gegen eine andere tauschen (gleiche Art bevorzugt)
      const j = Math.max(0, teil.reserve.findIndex(B => B.art === A.art)), neu = teil.reserve.splice(j, 1)[0]; if (!neu) return;
      teil.reserve.push(A); teil.liste[i] = neu; zeichne();
      el.querySelector(`[data-ti="${teile.indexOf(teil)}"][data-i="${i}"]`)?.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
    });
    w.querySelectorAll('.ws-teil').forEach(tl => {
      const j = +tl.dataset.j, T = A.teile[j];
      const nb = tl.querySelector('.ws-nach');
      if (nb) { if (!A.key || !window.LT_nachschlagen) nb.remove(); else nb.onclick = () => window.LT_nachschlagen(A.key, T.loesungQ ? suchBegriffe(T.loesungQ.a) : { antwort: txt(T.loesung || ''), frage: txt(A.titel + ' ' + T.text) }); }
      tl.querySelectorAll('.ring:not(.ws-nach)').forEach(b => b.onclick = () => { const o = tl.querySelector(`[data-o="${b.dataset.r}"]`); o.hidden = !o.hidden; b.classList.toggle('on', !o.hidden); if (b.dataset.r !== '3') tl.dataset.hilfe = '1'; });
      tl.querySelectorAll('[data-selbstab]').forEach(b => b.onclick = () => {   // Selbstkontrolle geht ins Gedächtnis: nur „Ja“ zählt als gekonnt
        tl.querySelectorAll('[data-selbstab]').forEach(x => x.classList.toggle('on', x === b));
        tl.classList.remove('r-ok', 'r-nok'); tl.classList.add(b.dataset.selbstab === '1' ? 'r-ok' : 'r-nok');
        G.antwort(teilId(A, j), b.dataset.selbstab === '1', { k: A.key, v: T.loesungQ && T.loesungQ.gv, hilfe: !!tl.querySelector('.ring.on[data-r="1"], .ring.on[data-r="2"]') || tl.dataset.hilfe === '1' });
      });
      const inp = tl.querySelector('.ws-check input'); if (!inp) return;
      const pruefe = () => { const v = num(inp.value); if (isNaN(v)) return; const tol = T.tol ?? Math.max(.01, Math.abs(T.ergebnis) * .005); tl.classList.remove('r-ok', 'r-nok'); tl.classList.add(Math.abs(v - T.ergebnis) <= tol ? 'r-ok' : 'r-nok'); };
      inp.onkeydown = e => { if (e.key === 'Enter') pruefe(); }; inp.onblur = () => inp.value && pruefe();
    });
  }
  zeichne();
}

/* ---------- Fokus-Timer: läuft über Seitenwechsel und Neuladen weiter (S.uhr), Signal am Ende ---------- */
S.uhr = S.uhr || { len: 25 * 60, ende: 0, rest: 25 * 60 };
const T = { iv: 0 };
const uhrRest = () => S.uhr.ende ? Math.max(0, Math.round((S.uhr.ende - Date.now()) / 1000)) : S.uhr.rest;
function timerSet(min) { min = Math.max(1, Math.min(180, Math.round(+min) || 25)); S.uhr = { len: min * 60, ende: 0, rest: min * 60 }; save(); timerLauf(); }
function timerToggle() {
  if (S.uhr.ende) S.uhr = { ...S.uhr, rest: uhrRest(), ende: 0 };
  else { if (!S.uhr.rest) S.uhr.rest = S.uhr.len; S.uhr.ende = Date.now() + S.uhr.rest * 1000; uhrTon(true); }
  save(); timerLauf();
}
function timerLauf() {
  clearInterval(T.iv);
  if (S.uhr.ende) T.iv = setInterval(() => { if (!uhrRest()) { S.uhr = { ...S.uhr, ende: 0, rest: 0 }; save(); clearInterval(T.iv); uhrSignal(); } timerUpd(); }, 1000);
  timerUpd();
}
let AC = null;
function uhrTon(vorbereiten) {   // Ton nur nach einem Klick erlaubt: beim Start vorbereiten, am Ende abspielen
  try { AC = AC || new (window.AudioContext || window.webkitAudioContext)(); if (vorbereiten) return;
    [0, .35, .7].forEach(t => { const o = AC.createOscillator(), g = AC.createGain(); o.frequency.value = 660; g.gain.setValueAtTime(.0001, AC.currentTime + t);
      g.gain.exponentialRampToValueAtTime(.2, AC.currentTime + t + .03); g.gain.exponentialRampToValueAtTime(.0001, AC.currentTime + t + .3); o.connect(g).connect(AC.destination); o.start(AC.currentTime + t); o.stop(AC.currentTime + t + .32); });
  } catch (e) { }
}
function uhrSignal() {
  uhrTon(false);
  document.querySelectorAll('.uhr').forEach(u => { u.classList.add('fertig'); setTimeout(() => u.classList.remove('fertig'), 6000); });
  const alt = document.title; document.title = 'Zeit um · ' + alt; setTimeout(() => { document.title = alt; }, 8000);
}
const mmss = s => String(s / 60 | 0).padStart(2, '0') + ':' + String(s % 60).padStart(2, '0');
function timerUpd() {
  const rest = uhrRest(), lauf = !!S.uhr.ende;
  document.querySelectorAll('[data-timer]').forEach(e => { e.textContent = mmss(rest); });
  document.querySelectorAll('[data-timer-p]').forEach(e => e.style.setProperty('--p', (1 - rest / S.uhr.len).toFixed(4)));
  document.querySelectorAll('[data-timer-btn]').forEach(e => e.textContent = lauf ? 'Pause' : (rest && rest < S.uhr.len ? 'Weiter' : 'Start'));
  document.querySelectorAll('[data-timer-min]').forEach(e => e.classList.toggle('on', +e.dataset.timerMin * 60 === S.uhr.len));
  document.querySelectorAll('.uhr').forEach(u => u.classList.toggle('laeuft', lauf));
}
if (S.uhr.ende) setTimeout(timerLauf, 0);
/* Zeitbalken als 12 Striche (für Designs, die keine Ringe wollen) */
const timerTicks = () => `<span class="ticks" data-timer-p>${'<i></i>'.repeat(12)}</span>`;

/* Tipps beim Erklären: nacheinander aufdecken */
document.addEventListener('click', e => {
  const b = e.target.closest('.q-tippb'); if (!b) return;
  const box = b.closest('.q-tipps'), out = box.querySelector('.q-tippt');
  out.insertAdjacentHTML('beforeend', `<p>${b.dataset.tipp}</p>`); b.hidden = true;
  const n = b.nextElementSibling; if (n && n.classList.contains('q-tippb')) n.hidden = false;
});

/* Geist-Ansicht: Hinweisleiste oben */
if (GEIST) document.addEventListener('DOMContentLoaded', () => {
  document.documentElement.classList.add('lw-geist');
  document.body.insertAdjacentHTML('afterbegin', `<div class="geist-leiste" role="status"><b>Geist-Ansicht</b><span>${esc(GEIST.person || 'Person')} · nur ansehen, nichts wird gespeichert</span><button type="button" onclick="sessionStorage.removeItem('lt-geist'); window.close(); location.href='admin.html'">Beenden</button></div>`);
});
