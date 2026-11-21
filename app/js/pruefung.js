/* LernTool · Übungsklausur je Oberthema und Refresh-Sprint (der einzige Ort, an dem Prozente entstehen).
   Aufbau wie die echte Klausur des Prüfers: erst kurze, einfache Aufgaben, dann die großen. Punkte je Aufgabe,
   Zeitlimit (1 Punkt ≈ 1 Minute, abschaltbar), keine Hilfen; nach der Abgabe Auswertung mit Teilpunkten,
   ehrlicher Selbstbewertung bei Erklärfragen, Durchsicht und Nachschlagen. */
'use strict';

/* Punkte je Aufgabe (Klausurstil) */
function punkteVon(a) {
  const schwer = (a.lvl || 1) >= 3 || a.klausur;
  if (a.y === 'liste') return Math.min(a.n || a.pk.length, 8);
  if (a.y === 'num') return schwer ? 6 : 4;
  if (a.y === 'rev') return schwer ? 6 : 4;
  return { mc: 2, mc_multi: 3, block: 3, kurz: 2, luecke: 2, zuord: 3, beschr: 3, reihe: 3, hot: 2 }[a.y] || 2;
}
const pkt = it => it.gross ? it.max : punkteVon(it.a);
const TEIL = it => it.gross || punkteVon(it.a) > 3 ? 'B' : 'A';   // A: kurze Aufgaben · B: größere Aufgaben (große Aufgaben immer B)

/* Unterthemen, die laut Vorlesung nicht in der Klausur drankommen (Index-Feld nk), bleiben aus Übungsklausur und Refresh draußen;
   im Training sind sie weiter übbar. Ist ein ganzes Oberthema so gekennzeichnet, gilt alles. */
/* Ausgeblendete Unterthemen (uAus) fehlen immer. f: Fach (für den Schlüssel), sonst wird es über das Oberthema gesucht. */
function klausurThemen(k, f) {
  f = f || D.faecher.find(x => x.kapitel.includes(k));
  const v = f ? k.topics.filter(t => !uAus(f.id + '/' + t.id)) : k.topics, r = v.filter(t => !t.nk);
  return r.length ? r : v;
}
/* Prüfen nur mit Folienstoff: Varianten „nicht in den Folien“ (zf) übt man im Endlos-Quiz, geprüft werden sie nicht.
   bv: Variante fragt eine Folien-Definition ab, die die Definitionsfrage (df-) schon abdeckt; je Begriff (Feld b) höchstens eine Aufgabe. */
function pruefVariante(fam) {
  const a0 = variante(fam, 'klausur'); if (a0 && !a0.zf && !a0.bv) return a0;
  const v = fam.a.filter(a => !a.zf), v1 = v.filter(a => !a.bv), w = v1.length ? v1 : v;
  return w.find(a => a.klausur) || w[0] || null;
}
/* Aufgaben für die Übungsklausur eines Oberthemas: jedes Unterthema mindestens einmal, Aufgabenarten nach dem Prüfer-Mix */
function klausurAufgaben(f, k) {
  const pool = klausurThemen(k, f).map(t => ({ key: f.id + '/' + t.id, f, k, t })).filter(x => (x.t.fragen || []).length);
  const mix = f.mix || {}, gew = y => (mix[y] || (y === 'block' ? mix.mc_multi : 0) || [.05, .6][klausurStil(f, y)]);   // Antippen nur, wo die Klausur es auch hat
  const ziel = Math.max(18, Math.min(40, Math.round(k.topics.length * 3.2)));
  const benutzt = new Set(), out = [], bBenutzt = new Set();
  const dfVon = {}; for (const x of pool) for (const fam of x.t.fragen) if (fam.b && /:df-/.test(fam.id)) dfVon[fam.b] = fam;
  const eng = pool.length * 3 > ziel;   // viele Unterthemen: für die Abdeckung kurze Aufgaben bevorzugen, damit die Zeit realistisch bleibt
  const nimm = (x, nurSchwer) => {
    /* je Begriff (Folien-Definition) die Definitionsfrage statt einer anderen Frage dazu, und nur einmal */
    const fams = [...new Set(x.t.fragen.map(fam => fam.b && dfVon[fam.b] && !fam.p ? dfVon[fam.b] : fam))].filter(fam => !benutzt.has(fam) && !(fam.b && bBenutzt.has(fam.b) && !fam.p));
    let kand = fams.map(fam => ({ fam, a: pruefVariante(fam) })).filter(c => c.a && (!nurSchwer || punkteVon(c.a) >= 4));   // „nicht in den Folien“ (zf) kommt in der Übungsklausur nicht dran
    if (!kand.length) return null;
    /* Vorrang: gibt es Fragen aus Klausuren, Probeklausur oder Übungen (klausur: true), kommt eine davon dran; eigene füllen nur auf */
    const ausKlausur = kand.filter(c => c.a.klausur || c.fam.a.some(a => a.klausur));
    if (ausKlausur.length) kand = ausKlausur.map(c => c.a.klausur ? c : { fam: c.fam, a: c.fam.a.find(a => a.klausur && !a.zf) || c.a });
    /* Fragen, die so schon in Klausuren oder Übungen vorkamen (klausur: true), deutlich bevorzugen */
    const w = c => gew(c.a.y) * (c.a.klausur || c.fam.a.some(a => a.klausur) ? 3 : 1) * (eng && !nurSchwer ? (punkteVon(c.a) <= 3 ? 4 : .3) : 1);
    const sum = kand.reduce((s, c) => s + w(c), 0); let r = Math.random() * sum;
    const c = kand.find(c => (r -= w(c)) <= 0) || kand[0];
    benutzt.add(c.fam); if (c.fam.b) bBenutzt.add(c.fam.b);
    return { a: inst(c.a), vi: c.fam.a.indexOf(c.a), key: x.key, f, k, t: x.t, fam: c.fam, x };
  };
  const vorrang = new Set((S.pruef[f.id + '/' + k.id] || {}).ausgelassen || []);   // beim letzten Mal ausgelassene Unterthemen zuerst
  for (const x of [...shuffle(pool.filter(x => vorrang.has(x.t.id))), ...shuffle(pool.filter(x => !vorrang.has(x.t.id)))]) { const it = nimm(x); if (it) out.push(it); }
  /* eine große Aufgabe zu diesem Oberthema: zuerst Klausuraufgaben (Probeklausur-Bogen, Klausuren, Übungen), sonst eigene a–d */
  const imKap = u => klausurThemen(k, f).some(t => t.id === u);
  const ausBogen = [];
  if (f.klausur) for (const K of f.klausur.aufgaben) for (const T of K.teile) for (const v of T.varianten)
    if (imKap(v.unter) && T.punkte >= 6) ausBogen.push(Object.assign(ausVariante(f, K, T, v), { unter: [v.unter], vorrang: !!v.vorrang }));
  const eigeneG = (f.aufgaben || []).filter(A => A.unter.some(imKap));
  const kGross = [ausBogen.filter(A => A.vorrang), ausBogen, eigeneG.filter(A => A.klausur || /Übung|Probeklausur|Klausurstil|Fallstudie/.test(A.quelle || '')), eigeneG].find(l => l.length) || [];
  if (kGross.length) { const A = pick(kGross), x = pool.find(x => A.unter.includes(x.t.id)) || pool[0];
    out.push({ gross: A, key: x.key, f, k, t: x.t, x, max: A.teile.reduce((s, T) => s + T.punkte, 0) }); }
  let summe = () => out.reduce((s, it) => s + pkt(it), 0);
  for (const x of shuffle(pool)) { if (summe() >= ziel) break; const it = nimm(x, true); if (it) out.push(it); }
  while (summe() > ziel + 6) {   // kürzen, aber nie die einzige Aufgabe eines Unterthemas
    const doppelt = out.filter(it => !it.gross && out.filter(o => o.t === it.t).length > 1);
    if (!doppelt.length) break;
    out.splice(out.indexOf(doppelt.filter(it => !it.gross).sort((a, b) => pkt(a) - pkt(b))[0] ?? doppelt[0]), 1);
  }
  /* höchstens 45 Minuten: passt nicht alles, fallen große Aufgaben weg; diese Unterthemen kommen beim nächsten Mal zuerst */
  const aus = [];
  while (summe() > 45) {
    const kand = out.filter(it => !it.gross && !vorrang.has(it.t.id)).sort((a, b) => pkt(b) - pkt(a));
    const weg = kand[0] || out.filter(it => !it.gross).sort((a, b) => pkt(b) - pkt(a))[0]; if (!weg) break;
    out.splice(out.indexOf(weg), 1); if (!out.some(o => o.t === weg.t)) aus.push(weg.t.id);
  }
  out.forEach(it => { if (!it.gross) it.max = punkteVon(it.a); });
  out.ausgelassen = aus;
  return out.sort((a, b) => a.max - b.max || (a.gross ? 1 : 0) - (b.gross ? 1 : 0) || ((a.a || {}).lvl || 1) - ((b.a || {}).lvl || 1));
}
/* Refresh-Sprint: 4 kurze Fragen, zuerst aus Unterthemen, die zuletzt falsch waren */
function refreshAufgaben(f, k) {
  const p = S.pruef[f.id + '/' + k.id] || {}, falsch = new Set(p.falsch || []);
  const pool = klausurThemen(k, f).map(t => ({ key: f.id + '/' + t.id, f, k, t })).filter(x => (x.t.fragen || []).length);
  const reihe = [...shuffle(pool.filter(x => falsch.has(x.t.id))), ...shuffle(pool.filter(x => !falsch.has(x.t.id)))];
  const out = [], bDa = new Set();
  for (const x of reihe) { const fams = x.t.fragen.filter(q => q.a.some(v => !v.zf)); if (!fams.length) continue; const fam = pick(fams), a = pruefVariante(fam); if (!a) continue;
    if (fam.b) { if (bDa.has(fam.b)) continue; bDa.add(fam.b); } if (punkteVon(a) > 4 && Math.random() < .6) continue;
    out.push({ a: inst(a), vi: fam.a.indexOf(a), key: x.key, f, k, t: x.t, fam, x, max: punkteVon(a) }); if (out.length >= 4) break; }
  return out.sort((a, b) => a.max - b.max);
}

/* ---------- Bewerten einer Aufgabe (nach der Abgabe) ---------- */
function bewerte(it, box) {
  if (it.gross) return { gross: true, teile: it.gross.teile.map((T, j) => {
    const li = box.querySelector(`.pb-teile > li[data-j="${j}"]`), inp = li.querySelector('input.q-in'), ta = li.querySelector('textarea');
    if (T.ergebnis != null) { const v = num(inp.value); if (isNaN(v)) return { anteil: 0, leer: true };
      const tol = T.tol ?? Math.max(.01, Math.abs(T.ergebnis) * .005); if (Math.abs(v - T.ergebnis) <= tol) return { anteil: 1 };
      return Math.abs(v / T.ergebnis - 1) < .02 ? { anteil: .5, notiz: 'Rundungsfehler: halbe Punkte.' } : { anteil: 0 }; }
    return { anteil: null, leer: !norm(ta.value) };
  }) };
  const a = it.a; let anteil = 0, notiz = '', leer = false;
  const zeilen = sel => [...box.querySelectorAll(sel)];
  if (a.y === 'mc') { const s = box.querySelector('.q-opt.on'); leer = !s; anteil = s && a.o[+s.dataset.j][1] ? 1 : 0; zeilen('.q-opt').forEach(o => a.o[+o.dataset.j][1] && o.classList.add('is-ok')); if (s && !anteil) s.classList.add('sel-nok'); }
  else if (a.y === 'mc_multi' || a.y === 'block') { const aus = a.y === 'block' ? a.aussagen : a.o, rows = zeilen('.q-rfz'); leer = rows.some(r => r.dataset.v == null);
    rows.forEach(r => r.classList.add((r.dataset.v === '1') === aus[+r.dataset.j][1] ? 'r-ok' : 'r-nok')); anteil = rows.every(r => r.classList.contains('r-ok')) ? 1 : 0;
    if (!anteil) notiz = 'Alles oder nichts: eine falsche Einschätzung, 0 Punkte.'; }
  else if (a.y === 'zuord' || a.y === 'beschr') { const rows = zeilen('.q-zrow'); leer = rows.every(r => !r.dataset.v);
    const richtig = r => a.y === 'zuord' ? r.dataset.v === a.k[a.e[+r.dataset.j][1]] : r.dataset.v === a.slots[+r.dataset.j];
    rows.forEach(r => r.classList.add(richtig(r) ? 'r-ok' : 'r-nok')); anteil = rows.filter(richtig).length / rows.length; }
  else if (a.y === 'kurz') { const v = box.querySelector('.q-in').value; leer = !norm(v); const t = vergleich(v, a.ok); anteil = t ? 1 : 0; if (t === 'fast') notiz = 'Tippfehler, zählt.'; }
  else if (a.y === 'luecke') { const g = zeilen('.q-gap'); leer = g.every(x => !norm(x.value)); let n = 0; g.forEach(x => { const t = vergleich(x.value, a.l[+x.dataset.n]); if (t) n++; x.classList.add(t ? 'r-ok' : 'r-nok'); }); anteil = n / g.length; }
  else if (a.y === 'num') { const v = num(box.querySelector('.q-in').value); leer = isNaN(v); const tol = a.tol ?? Math.max(.01, Math.abs(a.ans) * .005); anteil = !leer && Math.abs(v - a.ans) <= tol ? 1 : 0;
    if (!leer && !anteil && a.ans && Math.abs(v / a.ans - 1) < .02) { anteil = .5; notiz = 'Rundungsfehler: halbe Punkte.'; } }
  else if (a.y === 'reihe') { const s = it.reihe || []; leer = !s.length; anteil = s.length === a.o.length && s.every((v, j) => v === j) ? 1 : 0; }
  else if (a.y === 'hot') { leer = it.hot == null; anteil = it.hot ? 1 : 0; }
  else if (a.y === 'liste') { const v = listeText(box); leer = !norm(v); it.treffer = listePruefen(v, a.pk); const n = it.treffer.filter(Boolean).length, soll = Math.min(a.n || a.pk.length, a.pk.length);
    anteil = Math.min(1, n / soll); notiz = `${Math.min(n, soll)} von ${soll} Punkten erkannt.`; }
  else if (a.y === 'rev') { const v = box.querySelector('.q-ta').value; leer = !norm(v); if (a.pk && !leer) it.treffer = kernpunkte(v, a.pk); return { selbst: true, leer, anteil: null, notiz: '' }; }
  return { anteil, notiz, leer, selbst: false };
}

function istLeer(it, box) {
  if (it.gross) return [...box.querySelectorAll('input.q-in, textarea:not(.pb-weg)')].every(x => !norm(x.value));
  const y = it.a.y;
  if (y === 'mc') return !box.querySelector('.q-opt.on');
  if (y === 'reihe') return !(it.reihe || []).length;
  if (y === 'hot') return it.hot == null;
  const rows = [...box.querySelectorAll('.q-zrow, .q-rfz')]; if (rows.length) return rows.every(r => r.dataset.v == null);
  return [...box.querySelectorAll('input, textarea')].every(x => !norm(x.value));
}

/* ---------- Der Klausurbogen ---------- */
let PB = null;   // laufender Bogen
function pruefungsBogen(el, items, opt) {
  clearInterval(PB && PB.iv);
  PB = { items, opt, ende: opt.minuten ? Date.now() + opt.minuten * 60000 : 0, iv: 0, abgegeben: false };
  const summe = items.reduce((s, it) => s + it.max, 0);
  const abschnitt = opt.abschnitt || (it => TEIL(it) === 'A' ? 'Teil A · kurze Aufgaben' : 'Teil B · größere Aufgaben');
  el.innerHTML = `<div class="pb-leiste"><span>${items.length} Aufgaben · ${summe} Punkte</span><span class="pb-uhr" ${PB.ende ? '' : 'hidden'}><b class="pb-zeit">–</b> übrig</span><button class="btn btn-main pb-ab">Abgeben</button></div>
    <ol class="pb">${items.map((it, i) => `${i === 0 || abschnitt(items[i - 1]) !== abschnitt(it) ? `<li class="pb-teil">${abschnitt(it)}</li>` : ''}
      <li class="pb-a" data-i="${i}"><div class="pb-kopf"><b>Aufgabe ${i + 1}</b><span>${it.gross ? `${ARTNAME[it.gross.art] || ''} · ${esc(it.gross.titel)}` : `${TYPNAME[it.a.y] || ''} · ${esc(it.t.title)}`}</span><em>${it.max} P</em></div>${it.gross ? grossHTML(it) : `<div class="qz pb-q" data-y="${it.a.y}">${frageHTML(it, i)}</div>`}<div class="pb-fb"></div></li>`).join('')}</ol>
    <div class="pb-unten"><button class="btn btn-main pb-ab">Abgeben</button></div>`;
  items.forEach((it, i) => verdrahte(it, el.querySelector(`.pb-a[data-i="${i}"] .qz`)));
  el.querySelectorAll('.pb-ab').forEach(b => b.onclick = () => abgeben(el, false));
  if (PB.ende) { const tick = () => { const r = Math.max(0, Math.round((PB.ende - Date.now()) / 1000)), z = el.querySelector('.pb-zeit'); if (!z) return clearInterval(PB.iv);
    z.textContent = mmss(r); z.closest('.pb-uhr').classList.toggle('knapp', r < 120); if (!r) abgeben(el, true); }; tick(); PB.iv = setInterval(tick, 1000); }
}
const grossHTML = it => schoen(`<div class="qz pb-q pb-gross" data-y="gross"><div class="ws-ausgang">${it.gross.ausgang}</div><ol class="pb-teile">${it.gross.teile.map((T, j) => `<li data-j="${j}">
  <div class="ws-tk"><span class="ws-tbu">${'abcdefghijklmnopqrstuvwxyz'[j]})</span><div class="ws-p">${T.text}</div><span class="ws-tp">${T.punkte} P</span></div>
  ${T.ergebnis != null ? `<div class="q-numrow"><input class="q-in" inputmode="decimal" placeholder="Ergebnis" aria-label="Ergebnis ${'abcdefghijklmnopqrstuvwxyz'[j]})"><span class="q-unit">${esc(T.einheit || '')}</span></div><textarea class="q-ta pb-weg" rows="2" placeholder="Rechenweg (optional, für dich)" aria-label="Rechenweg"></textarea>`
    : `<textarea class="q-ta" rows="4" placeholder="Deine Antwort …" aria-label="Antwort ${'abcdefghijklmnopqrstuvwxyz'[j]})"></textarea>`}<div class="pb-tfb"></div></li>`).join('')}</ol></div>`);
/* Eingaben ohne Rückmeldung: Auswahl, Chips, Reihenfolge, Antippen */
function verdrahte(it, box) {
  if (it.gross) return;
  const a = it.a;
  if (a.y === 'mc') box.querySelectorAll('.q-opt').forEach(b => b.onclick = () => { box.querySelectorAll('.q-opt').forEach(x => x.classList.toggle('on', x === b)); });
  box.querySelectorAll('.q-zrow, .q-rfz').forEach(r => r.querySelectorAll('.q-chip').forEach(c => c.onclick = () => { r.querySelectorAll('.q-chip').forEach(x => x.classList.remove('on')); c.classList.add('on'); r.dataset.v = r.classList.contains('q-rfz') ? c.dataset.rf : c.dataset.k; }));
  if (a.y === 'reihe') { it.reihe = []; const ol = box.querySelector('.q-seq');
    box.querySelectorAll('.q-opt').forEach(b => b.onclick = () => { it.reihe.push(+b.dataset.j); b.disabled = true; ol.insertAdjacentHTML('beforeend', `<li>${a.o[+b.dataset.j]}</li>`); });
    box.querySelector('.q-hint').insertAdjacentHTML('beforeend', ' <button class="pb-neu">von vorn</button>');
    box.querySelector('.pb-neu').onclick = () => { it.reihe = []; ol.innerHTML = ''; box.querySelectorAll('.q-opt').forEach(b => { b.disabled = false; }); }; }
  if (a.y === 'hot') { const svg = box.querySelector('.q-bild svg'); if (svg) { svg.style.cursor = 'crosshair'; svg.onclick = e => {
    const pt = svg.createSVGPoint(); pt.x = e.clientX; pt.y = e.clientY; const p = pt.matrixTransform(svg.getScreenCTM().inverse()), z = a.z;
    it.hot = z.length === 3 ? Math.hypot(p.x - z[0], p.y - z[1]) <= z[2] + 6 : (p.x >= z[0] - 4 && p.x <= z[0] + z[2] + 4 && p.y >= z[1] - 4 && p.y <= z[1] + z[3] + 4);
    svg.querySelector('.pb-punkt')?.remove(); svg.insertAdjacentHTML('beforeend', `<circle class="pb-punkt" cx="${p.x}" cy="${p.y}" r="9" style="fill:none;stroke:var(--x-acc);stroke-width:3"/>`); }; } }
}
function abgeben(el, zeitUm, trotzdem) {
  if (PB.abgegeben) return;
  const leer = PB.items.filter((it, i) => istLeer(it, el.querySelector(`.pb-a[data-i="${i}"] .qz`))).length;
  if (!zeitUm && !trotzdem && leer) {
    if (el.querySelector('.pb-warn')) return;
    el.querySelector('.pb-leiste').insertAdjacentHTML('afterend', `<div class="pb-warn">${leer} ${leer === 1 ? 'Aufgabe ist' : 'Aufgaben sind'} noch leer. Trotzdem abgeben? <button class="btn btn-main pb-ja">Ja, abgeben</button></div>`);
    el.querySelector('.pb-ja').onclick = () => abgeben(el, false, true); el.querySelector('.pb-warn').scrollIntoView({ block: 'center', behavior: 'smooth' }); return;
  }
  PB.abgegeben = true; clearInterval(PB.iv);
  el.querySelector('.pb-warn')?.remove();
  el.querySelectorAll('.pb-ab').forEach(b => b.remove());
  el.querySelector('.pb-leiste').innerHTML = `<span>${zeitUm ? 'Zeit um. ' : ''}Abgegeben. Erklärfragen und Textteile bewertest du jetzt ehrlich selbst.</span>`;
  PB.items.forEach((it, i) => {
    const li = el.querySelector(`.pb-a[data-i="${i}"]`), box = li.querySelector('.qz'), r = bewerte(it, box);
    box.querySelectorAll('button.q-opt,button.q-chip,input,textarea,.pb-neu').forEach(x => { x.disabled = true; });
    it.erg = r;
    if (r.gross) { it.teilP = r.teile.map((t, j) => t.anteil == null ? null : Math.round(t.anteil * it.gross.teile[j].punkte * 2) / 2); it.p = it.teilP.includes(null) ? null : it.teilP.reduce((s, x) => s + x, 0); }
    else it.p = r.selbst ? null : Math.round(r.anteil * it.max * 2) / 2;
    zeichneErgebnis(el, li, it);
  });
  pruefeFertig(el);
}
function zeichneErgebnis(el, li, it) {
  const fb = li.querySelector('.pb-fb'), r = it.erg;
  if (it.gross) {
    it.gross.teile.forEach((T, j) => {
      const tl = li.querySelector(`.pb-teile > li[data-j="${j}"]`), tp = it.teilP[j], e = r.teile[j];
      tl.classList.toggle('r-ok', tp === T.punkte); tl.classList.toggle('r-nok', tp === 0);
      tl.querySelector('.ws-tp').textContent = tp == null ? `? / ${T.punkte} P` : `${tp} / ${T.punkte} P`;
      tl.querySelector('.pb-tfb').innerHTML = (T.ergebnis == null ? `<div class="pb-selbst"><small>Deine Punkte:</small>${[[1, 'voll'], [.5, 'halb'], [0, 'keine']].map(([v, n]) => `<button class="btn ${tp != null && tp === Math.round(v * T.punkte * 2) / 2 ? 'btn-main' : ''}" data-tselbst="${j}|${v}">${n}</button>`).join('')}</div>` : (e.notiz ? `<div class="q-notiz">${e.notiz}</div>` : ''))
        + `<div class="pb-l">Lösung</div><div class="q-loes">${T.loesung}</div>`;
    });
    li.classList.toggle('pb-voll', it.p === it.max); li.classList.toggle('pb-teil-p', it.p != null && it.p > 0 && it.p < it.max); li.classList.toggle('pb-null', it.p === 0);
    li.querySelector('.pb-kopf em').textContent = it.p == null ? `? / ${it.max} P` : `${it.p} / ${it.max} P`;
    fb.innerHTML = it.p !== it.max ? `<button class="btn q-nach">${IC_LUPE}Im Text nachschlagen</button>` : '';
    fb.querySelector('.q-nach')?.addEventListener('click', () => LT_nachschlagen(it.key, { antwort: txt(it.gross.teile.map(T => T.loesung).join(' ')), frage: it.gross.titel }));
    li.querySelectorAll('[data-tselbst]').forEach(b => b.onclick = () => { const [j, v] = b.dataset.tselbst.split('|'); it.teilP[+j] = Math.round(+v * it.gross.teile[+j].punkte * 2) / 2;
      it.p = it.teilP.includes(null) ? null : it.teilP.reduce((s, x) => s + x, 0); zeichneErgebnis(el, li, it); pruefeFertig(el); });
    return;
  }
  li.classList.toggle('pb-voll', it.p === it.max); li.classList.toggle('pb-teil-p', it.p != null && it.p > 0 && it.p < it.max); li.classList.toggle('pb-null', it.p === 0);
  li.querySelector('.pb-kopf em').textContent = it.p == null ? `? / ${it.max} P` : `${it.p} / ${it.max} P`;
  fb.innerHTML = (r.selbst ? `<div class="q-notiz">${it.treffer ? `${it.treffer.filter(Boolean).length} von ${it.a.pk.length} Kernpunkten in deinem Text erkannt. ` : ''}Vergleiche mit der Lösung und vergib deine Punkte:</div>
      <div class="pb-selbst">${[[1, 'volle Punkte'], [.5, 'halbe'], [0, 'keine']].map(([v, n]) => `<button class="btn ${it.p != null && it.p === Math.round(v * it.max * 2) / 2 ? 'btn-main' : ''}" data-selbst="${v}">${n}</button>`).join('')}</div>` : (r.notiz ? `<div class="q-notiz">${r.notiz}</div>` : ''))
    + '<div class="pb-l">Lösung</div>' + loesungHTML(it) + (it.p !== it.max ? `<button class="btn q-nach">${IC_LUPE}Im Text nachschlagen</button>` : '');
  fb.querySelector('.q-nach')?.addEventListener('click', () => LT_nachschlagen(it.key, suchBegriffe(it.a)));
  fb.querySelectorAll('[data-selbst]').forEach(b => b.onclick = () => { it.p = Math.round(+b.dataset.selbst * it.max * 2) / 2; zeichneErgebnis(el, li, it); pruefeFertig(el); });
}
function pruefeFertig(el) {
  const offen = PB.items.filter(it => it.p == null).length, summe = PB.items.reduce((s, it) => s + it.max, 0), hat = PB.items.reduce((s, it) => s + (it.p || 0), 0);
  el.querySelector('.pb-ergebnis')?.remove();
  el.insertAdjacentHTML('afterbegin', `<div class="pb-ergebnis">${offen ? `<p>Noch ${offen} ${offen === 1 ? 'Aufgabe' : 'Aufgaben'} mit Textantwort selbst bewerten, dann steht dein Ergebnis fest.</p><button class="btn btn-main pb-spring">Zur ersten Selbstbewertung</button>`
    : PB.opt.fertig(PB.items, hat, summe)}</div>`);
  const leiste = el.querySelector('.pb-leiste');
  if (leiste && PB.abgegeben) { leiste.querySelector('.pb-spring')?.remove(); if (offen) leiste.insertAdjacentHTML('beforeend', `<button class="btn btn-main pb-spring">Zur nächsten Selbstbewertung · ${offen} offen</button>`); }
  el.querySelectorAll('.pb-spring').forEach(b => b.onclick = () => springeZuOffen(el));
  if (!offen) el.querySelector('.pb-ergebnis').scrollIntoView({ block: 'start', behavior: 'smooth' });
}

/* Zur nächsten Aufgabe springen, die noch selbst bewertet werden muss (kurz hervorgehoben) */
function springeZuOffen(el) {
  const i = PB.items.findIndex(it => it.p == null); if (i < 0) return;
  const li = el.querySelector(`.pb-a[data-i="${i}"]`), z = li.querySelector('.pb-selbst') || li;
  z.scrollIntoView({ block: 'center', behavior: 'smooth' });
  li.classList.remove('pb-blink'); void li.offsetWidth; li.classList.add('pb-blink');
}
/* ---------- Verbuchen: Prozent, Haltbarkeit, Wackelthemen ---------- */
/* Note nach der Punkte-Noten-Tabelle der DHBW (Studienbereich Wirtschaft, 14.10.2022), 60er-Skala:
   4,0 = genau 50 %, darüber je 1/60 der Punkte 0,1 besser (1,0 ab 59,5 von 60); darunter 4,1 … 4,9, 5,0 ab einem Drittel oder weniger.
   Andere Punktzahlen werden über den Anteil auf 60 umgerechnet (halbe Punkte). */
function note(hat, summe) {
  const p = Math.round(hat / summe * 120) / 2;
  if (p >= 30) return Math.max(1, Math.round((4 - .1 * Math.ceil(p - 30)) * 10) / 10);
  if (p >= 28.5) return 4.1;
  return Math.min(5, Math.round((4.2 + .1 * Math.floor(28 - p)) * 10) / 10);
}
const noteText = n => n.toLocaleString('de-DE', { minimumFractionDigits: 1 });
/* Jede Klausuraufgabe geht ins Gedächtnis: volle Punkte = gekonnt, sonst Stufe 1 (kommt in „Methodisch lernen“) */
function merkeKlausur(items) {
  for (const it of items) {
    if (it.gross) it.gross.teile.forEach((T, j) => it.teilP && it.teilP[j] != null && G.antwort(`a:${it.f.id}:${it.gross.id}:${j}`, it.teilP[j] >= T.punkte, { k: it.key }));
    else if (it.p != null && it.gid) G.antwort(it.gid, it.p >= it.max, { k: it.key, v: it.gv });
  }
}
/* ---------- Probeklausur über die ganze Klausur (Punkte und Zeit wie die echte, Teile nach Gewicht) ---------- */
function probeAufgaben(kl) {
  const ges = kl.punkte || 120, teile = kl.teile.filter(t => F[t[1]]), gsum = teile.reduce((s, t) => s + t[2], 0), out = [];
  teile.forEach((t, ti) => {
    const f = F[t[1]], ziel = Math.round(ges * t[2] / gsum), proK = shuffle(f.kapitel.map(k => klausurAufgaben(f, k)));
    const teil = []; let summe = 0;
    /* höchstens zwei große Aufgaben aus verschiedenen Oberthemen, zusammen höchstens 45 % des Teils */
    for (const g of shuffle(proK.flat().filter(it => it.gross))) {
      if (teil.length >= 2 || summe + g.max > ziel * .45 || teil.some(x => x.k === g.k)) continue;
      teil.push(g); summe += g.max;
    }
    /* dann reihum aus jedem Oberthema eine Aufgabe, bis der Teil seine Punkte hat */
    for (let runde = 0, neu = true; summe < ziel - 1 && neu; runde++) {
      neu = false;
      for (const l of proK) { const it = l.find(x => !x.gross && !x.drin && summe + x.max <= ziel + 1); if (!it) continue; it.drin = 1; teil.push(it); summe += it.max; neu = true; if (summe >= ziel - 1) break; }
    }
    teil.sort((a, b) => (a.gross ? 1 : 0) - (b.gross ? 1 : 0) || a.max - b.max);
    teil.forEach(it => { it.teil = ti; it.teilName = t[4]; });
    out.push(...teil);
  });
  return out;
}
/* Ergebnis verbuchen: Gedächtnis je Aufgabe, Stand je Oberthema (mit vorhandenem Stand gemittelt), Verlauf je Klausur */
function verbucheProbe(kl, items, hat, summe) {
  merkeKlausur(items);
  const proK = {};
  for (const it of items) { const key = it.f.id + '/' + it.k.id, z = proK[key] || (proK[key] = { hat: 0, max: 0, fid: it.f.id, kid: it.k.id }); z.hat += it.p || 0; z.max += it.max; }
  for (const [key, z] of Object.entries(proK)) {
    if (z.max < 4) continue;
    const s = Math.round(z.hat / z.max * 100), vor = stand(z.fid, z.kid), p = S.pruef[key];
    S.pruef[key] = vor ? { ...p, s: Math.round((vor.pct + s) / 2), d: jetzt(), h: haltbarkeit(Math.round((vor.pct + s) / 2)) } : { s, d: jetzt(), h: haltbarkeit(s), falsch: [], ausgelassen: [] };
  }
  S.probe = S.probe || {}; (S.probe[kl.kurz] = S.probe[kl.kurz] || []).push({ d: jetzt(), hat, summe, note: note(hat, summe) });
  save();
}
const haltbarkeit = s => s >= 90 ? 7 : s >= 70 ? 5 : 3;   // Tage, bevor der Stand zu verblassen beginnt
function verbucheKlausur(fid, kid, items, hat, summe) {
  const key = fid + '/' + kid, vorher = stand(fid, kid), s = Math.round(hat / summe * 100);
  const schwach = items.filter(it => it.p < it.max * .5);
  S.pruef[key] = { s, d: jetzt(), h: haltbarkeit(s), falsch: [...new Set(schwach.map(it => it.t.id))], ausgelassen: items.ausgelassen || [] };
  merkeKlausur(items);
  save();
  return { vorher, nachher: stand(fid, kid), schwach, s };
}
function verbucheRefresh(fid, kid, items, hat, summe) {
  const key = fid + '/' + kid, vorher = stand(fid, kid), p = S.pruef[key], quote = hat / summe;
  const schwach = items.filter(it => it.p < it.max * .5);
  if (!p) return { vorher, nachher: null, schwach, gut: false };
  if (quote >= .75) S.pruef[key] = { ...p, d: jetzt(), h: Math.min(32, (p.h || haltbarkeit(p.s)) * 2), falsch: [...new Set(schwach.map(it => it.t.id))] };   // gut: frisch und länger haltbar
  else S.pruef[key] = { ...p, s: vorher.pct ? Math.round(vorher.pct * (.6 + .4 * quote)) : p.s, d: jetzt(), falsch: [...new Set(schwach.map(it => it.t.id))] };   // schlecht: sinkt weiter
  merkeKlausur(items);
  save();
  return { vorher, nachher: stand(fid, kid), schwach, gut: quote >= .75, h: S.pruef[key].h };
}
