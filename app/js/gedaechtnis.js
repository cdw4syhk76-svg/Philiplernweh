/* LernTool · Gedächtnis: Stufe 1–4 je Aufgabe, nächster Termin, Farbe je Unterthema.
   Alle Regeln stehen hier (REGELN). Werkzeuge melden nur: G.antwort(id, richtig, {k: Unterthema, runde, v: Variante, hilfe: mit Hilfe gelöst}).
   IDs (müssen zu aufgaben_ids() in bau.py passen):
     q:<familie>:<art>   Frage (gleiche Familie, gleiche Aufgabenart; Auswahl hebt also keine Erklär-Aufgabe)
     k:<fach>:<begriff>  Karteikarte zum Begriff      b:<fach>:<begriff>  Begriff im Definitions-Drill
     m:<fach>/<thema>    Merksatz-Karte               g:<fach>/<thema>:<id>  grün markierte Stelle (Karte „von dir“)
     a:<fach>:<aufgabe>:<teil>  Teilaufgabe aus Arbeitsblatt/Klausur */
'use strict';
const REGELN = {
  tagBeginn: 4,                                  // Uhrzeit, ab der ein neuer Lerntag beginnt (Lernen nach Mitternacht zählt zum Vortag)
  abstand: { 1: 1, 2: 1, 3: 3, 4: 7 },           // Tage bis zum nächsten Termin je Stufe
  bestaetigt: 21,                                // Stufe 4, die schon einmal bestätigt wurde
  neuSitzt: 3,                                   // heute neu gelernt und sofort gewusst → Bestätigung nach 3 Tagen
  klausurAnteil: 1 / 3, endspurt: 3,             // kein Abstand länger als 1/3 bis zur Klausur; in den letzten 3 Tagen alles unter 4 täglich
  karteRunde: r => r <= 1 ? 4 : r === 2 ? 3 : 2, // Karteikarten: Stufe nach der Runde, in der die Karte geschafft wurde
  minFarbe: 5,                                   // so viele bearbeitete Aufgaben braucht ein Unterthema für seine Farbe
  farbe: o => o < 1.5 ? 1 : o < 2.5 ? 2 : o < 3.5 ? 3 : 4,
};
const STUFE_NAME = ['neu', 'nicht gekonnt', 'mühsam', 'fast sicher', 'sitzt'];
S.g = S.g || {};
/* S.kannte[fach/thema] = Überarbeitungen (data-nz), die beim ersten Besuch des Unterthemas schon da waren. Was danach dazukam, ist für diese
   Person neu und steht gold. Beim ersten Start mit dieser Version: Unterthemen, die man schon geübt oder zuletzt gelesen hat, gelten als
   „vor allen Überarbeitungen gekannt“ (leere Liste). */
if (!S.kannte) {
  S.kannte = {};
  for (const e of Object.values(S.g)) if (e && e.k) S.kannte[e.k] = [];
  for (const [fid, z] of Object.entries(S.zuletztF || {})) if (z && z.tid) S.kannte[fid + '/' + z.tid] = [];
  if (S.zuletzt && S.zuletzt.tid) S.kannte[S.zuletzt.fid + '/' + S.zuletzt.tid] = [];
}
/* Nacharbeiten: Fragen, die man schon vor einer Überarbeitung bearbeitet hatte und die seitdem an neuen Stoff angepasst wurden.
   S.nach = offene Einträge „fach|familie|index|art|thema“; jeder Eintrag des Index wird genau einmal geprüft (S.nachGeprueft).
   Erledigt ist ein Eintrag, sobald die Frage richtig beantwortet ist. Ist die Liste leer, verschwindet das Werkzeug. */
S.nach = S.nach || []; S.nachGeprueft = S.nachGeprueft || {};
for (const f of D.faecher) for (const [b, l] of Object.entries(f.nach || {})) for (const [fam, i, y, tid] of l) {
  const k = `${f.id}|${fam}|${i}|${y}|${tid}`, pk = b + ':' + k; if (S.nachGeprueft[pk]) continue;
  S.nachGeprueft[pk] = 1; const e = S.g[`q:${fam}:${y}`];
  if (e && e.s && !S.nach.includes(k)) S.nach.push(k);
}
/* Nur Einträge, die der Index noch kennt (z. B. fällt ein früherer Lückentext weg, wenn die Frage neu formuliert wurde) */
{ const gueltig = new Set(D.faecher.flatMap(f => [...Object.values(f.nach || {}).flat(), ...(f.nachNz || []), ...(f.nachDef || [])].map(([fam, i, y, tid]) => `${f.id}|${fam}|${i}|${y}|${tid}`)));
  S.nach = S.nach.filter(k => gueltig.has(k)); }
/* Teil 3: Nachschärfen der Definitionen (Index nachDef, bau.py definitionen_fragen) – gleiche Regel wie Teil 2: nur für Unterthemen, die man vor der
   Überarbeitung kannte. Eine Karte je Definition: bekannte Fassung → Folien-Definition. Wer die Definitionsfrage schon sicher kann (Stufe ≥ 3), braucht sie nicht. */
for (const f of D.faecher) for (const [fam, i, y, tid] of f.nachDef || []) {
  const key = f.id + '/' + tid, x = TOP[key]; if (!x || !(key in S.kannte)) continue;
  const k = `${f.id}|${fam}|${i}|${y}|${tid}`, pk = 'df:' + k; if (S.nachGeprueft[pk]) continue;
  S.nachGeprueft[pk] = 1;
  const e = S.g[`q:${fam}:rev`];
  if ((x.t.nz || []).some(b => !S.kannte[key].includes(b)) && !(e && e.s >= 3) && !S.nach.includes(k)) S.nach.unshift(k);   // Definitionen zuerst
}
/* Teil 2: Fragen zum neu eingearbeiteten Stoff (Familien „:nz-“) – nur für Unterthemen, die man schon vor der Überarbeitung kannte
   (S.kannte ohne den Stand der Überarbeitung). Wer ein Unterthema erst danach öffnet, liest den Stoff ohnehin neu. */
for (const f of D.faecher) for (const [fam, i, y, tid] of f.nachNz || []) {
  const key = f.id + '/' + tid, x = TOP[key]; if (!x || !(key in S.kannte)) continue;
  const k = `${f.id}|${fam}|${i}|${y}|${tid}`, pk = 'nz:' + k; if (S.nachGeprueft[pk]) continue;
  S.nachGeprueft[pk] = 1;
  const e = S.g[`q:${fam}:${y}`];
  if ((x.t.nz || []).some(b => !S.kannte[key].includes(b)) && !(e && e.s >= 3) && !S.nach.includes(k)) S.nach.push(k);
}
S.ks = S.ks || {};
S.eigen = S.eigen || {};   // eigene Karteikarten: id → { k: Unterthema, v: Vorderseite, r: Rückseite, t: Zeit }   // offene Karteikarten-Sitzungen (zum Weitermachen)

const G = {
  /* Lerntag als Zahl (lokale Zeit, Wechsel um 4 Uhr) */
  tag(ts = jetzt()) { const d = new Date(ts - REGELN.tagBeginn * 36e5); return Math.floor((d.getTime() - d.getTimezoneOffset() * 6e4) / DAY); },
  werkzeug: id => ({ q: 'quiz', k: 'karte', m: 'karte', g: 'karte', e: 'karte', c: 'karte', b: 'begriff', a: 'aufgabe' })[id[0]],
  stufe: id => (S.g[id] || {}).s || 0,

  /* Eine Antwort verbuchen. Gibt eine Funktion zurück, die die Buchung rückgängig macht. */
  antwort(id, ok, m = {}) {
    if (!id) return () => {};
    const h = G.tag(), alt = S.g[id] ? { ...S.g[id] } : null;
    const e = S.g[id] || (S.g[id] = { s: 0, e: h });
    if (m.k) e.k = m.k;
    if (ok && S.nach && S.nach.length) S.nach = S.nach.filter(k => { const [, fam, , y] = k.split('|'); return `q:${fam}:${y}` !== id; });   // Nacharbeiten: richtig = erledigt
    if (m.k && S.kannte && !(m.k in S.kannte)) S.kannte[m.k] = ((TOP[m.k] && TOP[m.k].t.nz) || []).slice();   // geübt (auch im Mini-Quiz) = Unterthema bekannt
    if (m.v) e.v = m.v;
    if (!ok) { e.s = 1; e.d = h; e.nl = false; e.b = false; if (m.v) e.vf = m.v; }        // falsch, „Weiß ich nicht“, „War geraten“
    else if (e.s === 0) { e.s = m.runde ? REGELN.karteRunde(m.runde) : 4; e.d = h; e.nl = true; if (e.s === 4) e.e4 = h; }
    else if (m.runde && e.e === h) { e.s = Math.max(e.s, REGELN.karteRunde(m.runde)); e.nl = true; if (e.s === 4) e.e4 = h; }   // neue Karte: Runde zählt
    else if (e.d === h) e.nl = true;                                                       // heute schon gestiegen oder heute falsch: nur Nachlernen
    else { if (e.s === 4 && e.e4 < h) e.b = true; if (e.s < 4) { e.s++; if (e.s === 4) e.e4 = h; } e.d = h; e.nl = true; }
    if (ok && m.hilfe && e.s === 4) { e.s = 3; e.b = false; }                            // mit Hilfe gelöst: höchstens „fast sicher“
    e.t = jetzt();
    nutzung(t => { t.a++; if (ok) t.r++; const w = id[0]; t.w = t.w || {}; t.w[w] = (t.w[w] || 0) + 1; });
    G.geaendert(id);
    return () => { if (alt) S.g[id] = alt; else delete S.g[id]; G.geaendert(id); };
  },
  geaendert(id) { save(); G.cache = null; },

  /* Klausur des Fachs: Tage bis zum Beginn (null = keine) */
  klausurTage(fid) { const k = klausurVon(fid); return k ? tageBis(k.beginn) : null; },
  /* Lerntag, an dem die Aufgabe wieder dran ist (Infinity = ruht, weil die Klausur vorbei ist) */
  termin(id) {
    const e = S.g[id]; if (!e || !e.s) return Infinity;
    const zuletzt = G.tag(e.t || 0);
    if (e.s === 1 && !e.nl) return zuletzt;                                              // frischer Fehler: sofort
    let ab = e.s === 4 ? (e.b ? REGELN.bestaetigt : e.e === zuletzt ? REGELN.neuSitzt : REGELN.abstand[4]) : REGELN.abstand[e.s];
    if (e.s < 4 && e.e === zuletzt) ab = 1;                                              // heute neu gelernt: morgen wieder
    const kt = e.k ? G.klausurTage(e.k.split('/')[0]) : null;
    if (kt != null) {
      if (kt < 0) return Infinity;
      ab = Math.min(ab, Math.max(1, Math.floor(kt * REGELN.klausurAnteil)));
      if (kt <= REGELN.endspurt && e.s < 4) ab = 1;
    }
    return zuletzt + ab;
  },
  faellig: id => G.termin(id) <= G.tag(),
  frisch: id => { const e = S.g[id]; return !!e && e.s === 1 && !e.nl; },

  /* Alle Aufgaben-IDs eines Unterthemas (Fach muss geladen sein) */
  itemsVon(key) {
    const x = TOP[key]; if (!x || !x.f.geladen) return null;
    const { f, t } = x, l = [];
    for (const fam of t.fragen || []) for (const y of new Set(fam.a.map(a => a.y))) l.push(`q:${fam.id}:${y}`);
    for (const g of f.glossar) if (g.t === t.id) l.push(`k:${f.id}:${g.b}`, `b:${f.id}:${g.b}`);
    for (const c of f.karten || []) if (c.t === t.id) l.push(`c:${f.id}:${txt(c.v)}`);
    for (const [id, c] of Object.entries(S.eigen || {})) if (c.k === key) l.push('e:' + id);
    if (t.merk) l.push('m:' + key);
    for (const A of f.aufgaben) if (A.unter[0] === t.id) A.teile.forEach((T, j) => l.push(`a:${f.id}:${A.id}:${j}`));
    for (const m of S.mark[key] || []) if (m.farbe === 'gruen') l.push(`g:${key}:${m.id}`);
    return l;
  },
  von(key) { const l = G.itemsVon(key); if (l) return l.length; const x = TOP[key]; return x ? (x.t.ni || 0) + (S.mark[key] || []).filter(m => m.farbe === 'gruen').length : 0; },

  /* Stand eines Unterthemas: Durchschnitt der bearbeiteten Aufgaben → Farbe 0 (grau) bis 4 */
  thema(key) {
    if (!G.cache) { G.cache = {}; for (const [id, e] of Object.entries(S.g)) if (e.k && e.s) { const c = G.cache[e.k] || (G.cache[e.k] = { n: 0, sum: 0, faellig: 0 }); c.n++; c.sum += e.s; if (G.faellig(id)) c.faellig++; } }
    const c = G.cache[key] || { n: 0, sum: 0, faellig: 0 }, von = Math.max(G.von(key), c.n);
    const avg = c.n ? c.sum / c.n : 0, farbe = c.n >= Math.min(REGELN.minFarbe, Math.max(1, von)) ? REGELN.farbe(avg) : 0;
    return { n: c.n, von, avg, farbe, faellig: c.faellig };
  },
  farbe: key => G.thema(key).farbe,
  text(key) { const s = G.thema(key); return s.n ? `Ø ${s.avg.toLocaleString('de-DE', { maximumFractionDigits: 1 })} · ${s.n} von ${s.von} bearbeitet` : `noch nichts bearbeitet · ${s.von} Aufgaben`; },
  punkt: key => { const s = G.thema(key); return `<span class="st st-${s.farbe}" title="${esc(G.text(key))}"></span>`; },
  /* Oberthema: schmaler Balken aus den Farben seiner Unterthemen */
  balken: (f, k) => `<span class="st-balken" aria-hidden="true">${k.topics.filter(t => !t.aus).map(t => `<b class="${uAus(f.id + '/' + t.id) ? 'st-aus' : 'st-' + G.farbe(f.id + '/' + t.id)}"></b>`).join('')}</span>`,

  /* Unterthema selbst als unsicher markieren: alle Aufgaben auf 1. Gibt „Rückgängig“ zurück. */
  unsicher(key) {
    const l = G.itemsVon(key); if (!l) return () => {};
    const h = G.tag(), alt = {}, t0 = jetzt();
    for (const id of l) { alt[id] = S.g[id] ? { ...S.g[id] } : 0; const e = S.g[id] || (S.g[id] = { e: h }); Object.assign(e, { s: 1, k: key, d: h, nl: false, b: false, t: t0 }); }
    /* Stand vor dem Markieren merken, damit man es später wieder aufheben kann (auch nach Tagen) */
    (S.unsicher || (S.unsicher = {}))[key] = { t: t0, alt };
    G.geaendert(); save();
    return () => G.sicher(key);
  },
  istUnsicher: key => !!(S.unsicher && S.unsicher[key]),
  /* „Unsicher“ aufheben: Jede Aufgabe bekommt ihren Stand von vorher zurück, also bleibt unsicher, was vorher schon unsicher war.
     Aufgaben, die seit dem Markieren neu beantwortet wurden, behalten ihren neuen Stand. */
  sicher(key) {
    const u = S.unsicher && S.unsicher[key]; if (!u) return;
    for (const [id, e] of Object.entries(u.alt)) {
      const jetztE = S.g[id];
      if (jetztE && jetztE.t !== u.t) continue;   // nach dem Markieren geübt: neuer Stand gilt
      if (e) S.g[id] = e; else delete S.g[id];
    }
    delete S.unsicher[key]; G.geaendert(); save();
  },
  /* Rote Unterthemen (früher: Wackelthemen) */
  rote: () => Object.keys(TOP).filter(k => !uAus(k) && G.farbe(k) === 1),

  /* Fällige Aufgaben, nach Dringlichkeit: frische Fehler · am stärksten überfällig (nahe Klausur zuerst) · heute fällig */
  faelligListe(filter = {}) {
    const h = G.tag(), out = [];
    for (const [id, e] of Object.entries(S.g)) {
      if (!e.s || !e.k || !TOP[e.k] || uAus(e.k)) continue;   // ausgeblendete Unterthemen sind nie fällig
      if (filter.w && G.werkzeug(id) !== filter.w) continue;
      if (filter.keys && !filter.keys.has(e.k)) continue;
      const t = G.termin(id); if (!(t <= h)) continue;
      const ab = Math.max(1, t - G.tag(e.t || 0)), kt = G.klausurTage(e.k.split('/')[0]);
      out.push({ id, e, frisch: G.frisch(id), druck: (h - t) / ab, kt: kt == null ? 999 : kt });
    }
    return out.sort((a, b) => (b.frisch - a.frisch) || (b.druck - a.druck) || (a.kt - b.kt) || ((a.e.t || 0) - (b.e.t || 0)));
  },
  /* Umbenannte IDs übernehmen (inhalte/umbenannt.json) */
  umbenennen() { for (const [alt, neu] of Object.entries(D.umbenannt || {})) if (S.g[alt] && !S.g[neu]) { S.g[neu] = S.g[alt]; delete S.g[alt]; } },
};
G.umbenennen();

/* Eine gespeicherte Aufgabe genau im Originalformat wiederherstellen (Fach muss geladen sein) */
function itemAus(id) {
  const e = S.g[id], x = e && TOP[e.k]; if (!x || !x.f.geladen) return null;
  const basis = { key: e.k, f: x.f, k: x.k, t: x.t, x, gid: id }, typ = id[0], nach2 = id.indexOf(':', 2);
  if (typ === 'q') {
    const y = id.slice(id.lastIndexOf(':') + 1), famId = id.slice(2, id.lastIndexOf(':')), fam = (x.t.fragen || []).find(f => f.id === famId);
    if (!fam) return null;
    const v = e.vf || e.v, vv = v && fam.a[v.i] && fam.a[v.i].y === y ? v : { i: fam.a.findIndex(a => a.y === y) };
    return vv.i < 0 ? null : frageWieder(x, fam, vv);
  }
  if (typ === 'b') {
    const b = id.slice(nach2 + 1), g = x.f.glossar.find(g => g.b === b); if (!g) return null;
    const def = `<span class="drill-def">„${esc(g.e)}“</span>`, modus = (e.vf || e.v || {}).modus || 'wahl';
    if (modus === 'tippen') return { ...basis, a: { y: 'kurz', p: def + '<br><small>Welcher Begriff ist das? Eintippen.</small>', ok: [g.b] }, gv: { modus } };
    if (modus === 'schreiben') { const pk = kernteile(g.e); return { ...basis, a: { y: 'rev', p: `Definieren Sie: <b>${esc(g.b)}</b>`, pk, tipps: defTipps(g.e, pk), l: `<p>${esc(g.e)}</p>` }, gv: { modus } }; }
    const andere = shuffle(x.f.glossar.filter(o => o !== g && TOP[x.f.id + '/' + o.t] && TOP[x.f.id + '/' + o.t].k === x.k)).concat(shuffle(x.f.glossar.filter(o => o !== g))).filter((o, i, l) => l.indexOf(o) === i).slice(0, 3);
    return { ...basis, a: { y: 'mc', p: def + '<br><small>Welcher Begriff ist das?</small>', o: shuffle([[esc(g.b), true], ...andere.map(o => [esc(o.b), false])]) }, gv: { modus } };
  }
  if (typ === 'k' || typ === 'm' || typ === 'g' || typ === 'c' || typ === 'e') {
    const c = kartenFuer([{ key: e.k, f: x.f, k: x.k, t: x.t }]).find(c => c.id === id); if (!c) return null;
    return { ...basis, a: { y: 'karte', p: c.front, l: esc(c.back), fach: c.fach } };
  }
  if (typ === 'a') {
    const [, , aid, j] = id.split(':'), A = x.f.aufgaben.find(a => a.id === aid), T = A && A.teile[+j]; if (!T) return null;
    return { ...basis, a: { y: 'teil', titel: A.titel, ausgang: A.ausgang, p: `<b>${'abcdefghijklmnopqrstuvwxyz'[+j]})</b> ${T.text}`, l: T.loesung } };
  }
  return null;
}
/* Methodisch lernen: fällige Aufgaben nach Dringlichkeit, jede im Originalformat.
   Falsches kommt nach etwa 4 Aufgaben wieder, bis es einmal richtig war. Jederzeit aufhören. */
function methodisch(el, filter = {}) {
  const liste = G.faelligListe(filter).map(z => z.id), gesamt = liste.length, wieder = [], geschafft = new Set(), bFam = {};
  if (!gesamt) { el.innerHTML = `<div class="leer-z"><b>Nichts fällig</b><span>Hier landet alles, was du irgendwo nicht auf Anhieb konntest, und kommt zum richtigen Zeitpunkt wieder.</span></div>`; return; }
  quiz(el, {
    weiterText: 'Weiter',
    next(i, res) {
      const l = res[res.length - 1];
      if (l) { if (l.ok) geschafft.add(l.item.gid); else wieder.push({ id: l.item.gid, bei: i + 4 }); }
      for (let n = 0; n < 500; n++) {
        const w = wieder.findIndex(z => z.bei <= i);
        const id = w >= 0 ? wieder.splice(w, 1)[0].id : liste.length ? liste.shift() : wieder.length ? wieder.shift().id : null;
        if (!id) return null;
        const it = itemAus(id); if (!it) continue;
        const b = it.fam && it.fam.b;   // dieselbe Definition (Feld b) nur über eine Familie je Sitzung; die andere bleibt fällig
        if (b && bFam[b] && bFam[b] !== it.fam.id) continue;
        if (b) bFam[b] = it.fam.id;
        return { ...it, nochmal: w >= 0 };
      }
      return null;
    },
    kopf: (i, res, it) => `<span class="q-zaehl">${geschafft.size} von ${gesamt} geschafft</span>${it.nochmal ? '<span class="q-wieder">nochmal</span>' : ''}<span class="q-stufe">Stufe ${G.stufe(it.gid)}</span>`,
    skip: it => { liste.push(it.gid); },   // überspringen: kommt am Ende noch einmal, Stufe bleibt
    onEnd: (res, box) => { box.innerHTML = `<div class="leer-z"><b>Für jetzt alles geschafft</b><span>${geschafft.size} Aufgaben sitzen wieder ein Stück fester. Was als Nächstes dran ist, steht morgen hier.</span></div>`; },
  });
}
/* Werkzeug → Aufgabenart im Gedächtnis (für den Schalter „Frei · Methodisch“) */
const WERKZEUG_ART = { quiz: 'quiz', drill: 'begriff', swipe: 'karte', blatt: 'aufgabe' };

/* Alte Wackelthemen (vor dem Stufen-System) einmalig als „unsicher“ übernehmen, sobald ihr Fach geladen ist.
   Rot markierte Textstellen ändern das Unterthema nicht mehr. */
(function () {
  const alt = Object.entries(S.wackel || {}).filter(([k, g]) => g !== 'unklar' && TOP[k]);
  if (!alt.length) { S.wackel = {}; return; }
  const ueber = () => { for (const [k] of alt) if (TOP[k].f.geladen && S.wackel[k]) { G.unsicher(k); delete S.wackel[k]; } for (const k of Object.keys(S.wackel)) if (S.wackel[k] === 'unklar') delete S.wackel[k]; save(); };
  const vorher = LT.fachGeladen;
  LT.fachGeladen = (fid, d) => { vorher(fid, d); ueber(); };
})();

/* ---------- Nutzung (für die anonyme Auswertung im Admin-Bereich) ----------
   Je Kalendertag: b Besuche (neue Sitzung nach 30 Minuten Pause), m aktive Minuten (Seite sichtbar und in den letzten 2 Minuten bedient),
   a Antworten, r davon richtig, w Antworten je Werkzeug. Nur Zahlen, keine Inhalte. Ältere Tage als 180 werden entfernt. */
function nutzung(fn) {
  if (GEIST) return {};
  const n = S.nutzung && typeof S.nutzung === 'object' ? S.nutzung : (S.nutzung = {});
  const k = new Date(Date.now() - new Date().getTimezoneOffset() * 6e4).toISOString().slice(0, 10);
  const t = n[k] || (n[k] = { b: 0, m: 0, a: 0, r: 0 });
  if (fn) fn(t);
  return t;
}
(function () {
  if (GEIST) return;   // Geist-Ansicht zählt nicht als Nutzung
  let aktiv = Date.now(), minuten = 0;
  const neueSitzung = () => { if (Date.now() - (S.nutzZuletzt || 0) > 30 * 6e4) { nutzung(t => t.b++); S.nutzZuletzt = Date.now(); save(); } S.nutzZuletzt = Date.now(); };
  neueSitzung();
  const alt = new Date(Date.now() - 180 * DAY).toISOString().slice(0, 10);
  for (const k of Object.keys(S.nutzung || {})) if (k < alt) delete S.nutzung[k];
  ['pointerdown', 'pointermove', 'keydown', 'wheel', 'touchstart', 'scroll'].forEach(ev => addEventListener(ev, () => { if (Date.now() - aktiv > 30 * 6e4) neueSitzung(); aktiv = Date.now(); }, { passive: true, capture: true }));
  setInterval(() => {
    if (document.visibilityState !== 'visible' || Date.now() - aktiv > 5 * 6e4) return;   // Lesen ohne Scrollen zählt bis zu 5 Minuten
    nutzung(t => t.m++); S.nutzZuletzt = Date.now();
    if (++minuten % 2 === 0) save();   // alle 2 aktiven Minuten speichern (online abgleichen; zeigt im Admin-Bereich „gerade aktiv“)
  }, 6e4);
  addEventListener('pagehide', () => { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) { } });
})();
