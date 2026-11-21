/* LernTool · Lese-Werkzeuge: Nachschlagen, Markieren & Notizen, Erklärfenster für Begriffe, Uhr mit Dauerwahl.
   Wird vor ansichten.js geladen; die Funktionen greifen erst beim Aufruf auf den Ansichts-Zustand V zu. */
'use strict';

/* ---------- Uhr: Dauer beim Drüberfahren (Handy: Antippen) wählen ---------- */
const uhrHTML = () => `<span class="uhr${S.uhr.ende ? ' laeuft' : ''}" tabindex="0" aria-label="Fokus-Timer, Dauer wählen">
  <b data-timer>${mmss(uhrRest())}</b><button data-act="timer" data-timer-btn>${S.uhr.ende ? 'Pause' : 'Start'}</button>
  <span class="uhr-pop" role="group" aria-label="Dauer wählen"><small>Dauer in Minuten</small>
    <span class="uhr-min">${[5, 10, 15, 25, 45, 60, 90].map(m => `<button data-act="tmin" data-timer-min="${m}" class="${m * 60 === S.uhr.len ? 'on' : ''}">${m}</button>`).join('')}</span>
    <label class="uhr-frei">eigene Dauer <input type="number" min="1" max="180" value="${Math.round(S.uhr.len / 60)}" data-act="tmin-frei" aria-label="Minuten"> min</label></span></span>`;

/* ---------- Textkarte: alle lesbaren Textknoten eines Bereichs mit Position (ohne Schaubilder, Formeln, Knöpfe) ---------- */
const NICHT_TEXT = 'svg,.katex,script,style,.fig-top,button,select,.mk-notiz,input,textarea';
function textKarte(root) {
  const nodes = [], teile = []; let pos = 0;
  const w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, { acceptNode: n => n.parentElement && !n.parentElement.closest(NICHT_TEXT) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT });
  let n; while ((n = w.nextNode())) { nodes.push({ n, a: pos }); pos += n.nodeValue.length; teile.push(n.nodeValue); }
  return { nodes, text: teile.join('') };
}
/* Bereich [a, b) der Textkarte in <mark>-Stücke einpacken (über Element-Grenzen hinweg) */
function umhuelle(root, a, b, mache) {
  const { nodes } = textKarte(root), stuecke = [];
  for (const { n, a: s0 } of nodes) {
    const s1 = s0 + n.nodeValue.length; if (s1 <= a || s0 >= b) continue;
    let node = n; const von = Math.max(0, a - s0), bis = Math.min(n.nodeValue.length, b - s0);
    if (von > 0) node = node.splitText(von);
    if (bis - von < node.nodeValue.length) node.splitText(bis - von);
    const m = mache(); node.parentNode.insertBefore(m, node); m.appendChild(node); stuecke.push(m);
  }
  return stuecke;
}

/* ---------- Nachschlagen: passende Stelle im Text finden und hervorheben ---------- */
const STOP = new Set('aber alle allem auch beim beide damit dann dass dein deine denn dessen diese dieser dieses durch eine einem einen einer eines erst etwa gibt habe haben hast hier immer jede jeder jedes kann kein keine machen mehr muss nach nicht noch oder ohne seine sich sind sowie über unter viel vom wann warum was welche welcher welches wenn werden wird wieso wird wurde zwei drei vier zwischen eines ihre ihrer their with that this from which what when have will into than then they there these about'.split(' '));
const woerter = s => [...new Set(norm2(s).split(' ').filter(w => w.length >= 4 && !STOP.has(w)))];
const norm2 = s => String(s).toLowerCase().replace(/<[^>]+>/g, ' ').replace(/[^a-zäöüß0-9]+/g, ' ').trim();
function zeigeStelle(root, beg) {
  if (!root) return;
  root.querySelectorAll('.fund').forEach(e => e.classList.remove('fund'));
  const A = woerter(beg.antwort), Q = woerter(beg.frage);
  const bl = [...root.querySelectorAll('p, li, td, .merk, .kernsatz, h3, .kurz, .box')].filter(e => !e.closest('svg') && (!e.querySelector('p, li') || e.matches('.merk, .kernsatz')));
  let best = null, bs = 0;
  for (const e of bl) { const t = norm2(e.textContent); const s = A.filter(w => t.includes(w)).length * 3 + Q.filter(w => t.includes(w)).length; if (s > bs) { bs = s; best = e; } }
  if (!best) { root.scrollIntoView({ block: 'start', behavior: 'smooth' }); return; }
  const top = best.closest('.topic'); if (best.closest('.article') && top) top.classList.add('full');
  best.classList.add('fund');
  if (window.lwOeffne) window.lwOeffne(best);   // zugeklappten Abschnitt öffnen
  setTimeout(() => best.scrollIntoView({ block: 'center', behavior: 'smooth' }), 60);
}
window.LT_nachschlagen = (key, beg) => {
  const x = TOP[key]; if (!x) return;
  if (V.screen === 'lern' && V.fid + '/' + V.tid === key) { zeigeStelle(document.querySelector('.bl-card .inhalt'), beg); return; }
  document.getElementById('ov')?.remove();
  const blur = V.blur; V.blur = false;
  document.body.insertAdjacentHTML('beforeend', `<div id="ov" class="ov ov-nach" role="dialog" aria-modal="true" aria-label="Nachschlagen" style="--fach:${x.f.farbe}"><div class="ov-box">
    <div class="ov-kopf"><b>Nachschlagen</b><span>${esc(x.f.name)} · ${esc(x.k.title)}</span><button class="btn btn-main" ${goLern(x.f.id, x.k.id, x.t.id)}>Zur Lernseite</button><button class="btn" data-act="ov-zu">Schließen</button></div>
    <h2 class="nach-t">${esc(x.t.title)}</h2>${inhaltHTML(x)}</div></div>`);
  V.blur = blur;
  const ov = document.getElementById('ov');
  ov.onclick = e => { if (e.target === ov || e.target.closest('[data-go]')) ov.remove(); };
  if (window.LT_nachRender) window.LT_nachRender(x.f.id);
  wendeMarkierungen(ov.querySelector('.inhalt'), key, false);
  zeigeStelle(ov.querySelector('.inhalt'), beg);
};

/* ---------- Markieren & Notizen ---------- */
/* Farben: die ersten drei haben eine Bedeutung (Grün wird zur Karteikarte), die übrigen frei wählbar. Jede Markierung kann
   statt farbig hinterlegt auch unterstrichen sein (m.stil = 'u'). Farbwerte: Tokens --mk-* in app.css */
const FARBEN = { gelb: 'Wichtig', gruen: 'Lernen', rot: 'Unklar', blau: 'Blau', lila: 'Lila', orange: 'Orange', pink: 'Pink', tuerkis: 'Türkis' };
const FARB_BEDEUTUNG = ['gelb', 'gruen', 'rot'];
const mkKlasse = m => 'mk mk-' + m.farbe + (m.stil === 'u' ? ' mk-u' : '');
const markeVon = (key, id) => (S.mark[key] || []).find(m => m.id === id);
function anker(text, m) {   // beste Fundstelle des Zitats: Vor- und Nachtext vergleichen
  let best = -1, bs = -1, i = text.indexOf(m.text);
  while (i >= 0) {
    const v = text.slice(Math.max(0, i - m.vor.length), i), n = text.slice(i + m.text.length, i + m.text.length + m.nach.length);
    let s = 0; for (let k = 1; k <= v.length && v[v.length - k] === m.vor[m.vor.length - k]; k++) s++;
    for (let k = 0; k < n.length && n[k] === m.nach[k]; k++) s++;
    if (s > bs) { bs = s; best = i; } i = text.indexOf(m.text, i + 1);
  }
  return best;
}
function wendeMarkierungen(root, key, klickbar = true) {
  if (!root) return 0;
  let fehlt = 0;
  for (const m of (S.mark[key] || [])) {
    const a = anker(textKarte(root).text, m); if (a < 0) { m.verloren = true; fehlt++; continue; } m.verloren = false;
    const st = umhuelle(root, a, a + m.text.length, () => { const e = document.createElement('mark'); e.className = mkKlasse(m); e.dataset.mk = m.id; return e; });
    if (m.notiz && st.length && klickbar) st[st.length - 1].insertAdjacentHTML('afterend', `<button class="mk-notiz" data-mk="${m.id}" aria-label="Notiz ansehen" title="${esc(m.notiz)}"></button>`);
  }
  return fehlt;
}
function speichereMarke(farbe, stil) {
  const sel = getSelection(); if (!sel.rangeCount || sel.isCollapsed) return null;
  const r = sel.getRangeAt(0), root = document.querySelector('.bl-card .inhalt'); if (!root || !root.contains(r.commonAncestorContainer)) return null;
  const { nodes, text } = textKarte(root);
  /* Anfang und Ende als Textposition. Die Auswahl kann an einer Element-Grenze liegen (ganzer Listenpunkt, Absatz, Karte,
     Doppel-/Dreifachtipp am Handy): dann zählt der erste bzw. letzte Textknoten, den die Auswahl berührt. */
  const drin = nodes.filter(x => { try { return r.intersectsNode(x.n); } catch (e) { return false; } });
  if (!drin.length) return null;
  const erst = drin[0], letzt = drin[drin.length - 1];
  let a = erst.a + (erst.n === r.startContainer ? r.startOffset : 0);
  let b = letzt.a + (letzt.n === r.endContainer ? r.endOffset : letzt.n.nodeValue.length);
  if (b <= a) return null;
  while (a < b && /\s/.test(text[a])) a++; while (b > a && /\s/.test(text[b - 1])) b--;
  const wz = c => /[0-9A-Za-zÄÖÜäöüß\-]/.test(c || '');   // auf ganze Wörter erweitern
  const grenze = new Set(nodes.map(x => x.a));   // nie über die Grenze eines Textknotens hinaus
  while (a > 0 && !grenze.has(a) && wz(text[a - 1]) && wz(text[a])) a--; while (b < text.length && !grenze.has(b) && wz(text[b]) && wz(text[b - 1])) b++;
  if (b - a < 2) return null;
  const block = r.startContainer.parentElement.closest('p, li, td, .merk, .kurz, h3, div');
  const m = { id: Date.now().toString(36), farbe, text: text.slice(a, b).slice(0, 600), vor: text.slice(Math.max(0, a - 30), a), nach: text.slice(b, b + 30),
    satz: block ? block.textContent.replace(/\s+/g, ' ').trim().slice(0, 400) : '', notiz: '', d: jetzt(), ...(stil === 'u' ? { stil: 'u' } : {}) };
  const key = V.fid + '/' + V.tid;
  (S.mark[key] = S.mark[key] || []).push(m);
  save(); sel.removeAllRanges();
  return m;
}
function loescheMarke(key, id) {
  S.mark[key] = (S.mark[key] || []).filter(m => m.id !== id);
  if (!S.mark[key].length) delete S.mark[key];
  save();
}
/* Leiste über einer Auswahl im Lerntext */
function leisteZeigen() {
  document.querySelector('.mk-leiste')?.remove();
  const sel = getSelection(); if (!sel.rangeCount || sel.isCollapsed || V.screen !== 'lern') return;
  const r = sel.getRangeAt(0), root = document.querySelector('.bl-card .inhalt');
  if (!root || !root.contains(r.commonAncestorContainer) || r.toString().trim().length < 2) return;
  const box = r.getBoundingClientRect();
  const mehr = Object.keys(FARBEN).filter(f => !FARB_BEDEUTUNG.includes(f));
  document.body.insertAdjacentHTML('beforeend', `<div class="mk-leiste" role="toolbar" aria-label="Markieren">${FARB_BEDEUTUNG.map(f => `<button data-mkneu="${f}" class="mkb-${f}"><i></i>${FARBEN[f]}</button>`).join('')}<span class="mk-mehr">${mehr.map(f => `<button data-mkneu="${f}" class="mkb-${f}" aria-label="${FARBEN[f]}" title="${FARBEN[f]}"><i></i></button>`).join('')}</span><button data-mkneu="unter" class="mk-ub" title="Unterstreichen" aria-label="Unterstreichen"><u>U</u></button><button data-mkneu="notiz">Notiz</button><button data-mkneu="melden" class="mk-melde" title="Fehler an dieser Stelle melden">⚑ Melden</button></div>`);
  const l = document.querySelector('.mk-leiste'), w = l.offsetWidth;
  l.style.left = Math.max(8, Math.min(innerWidth - w - 8, box.left + box.width / 2 - w / 2)) + 'px';
  l.style.top = Math.max(8, Math.min(innerHeight - l.offsetHeight - 90, box.top > 70 ? box.top - l.offsetHeight - 8 : box.bottom + 8)) + 'px';
}
let leisteT = 0;
document.addEventListener('selectionchange', () => { clearTimeout(leisteT); leisteT = setTimeout(leisteZeigen, 180); });
['mousedown', 'pointerdown', 'touchstart'].forEach(t => document.addEventListener(t, e => { if (e.target.closest && e.target.closest('.mk-leiste')) e.preventDefault(); }, { passive: false }));   // Auswahl beim Klick auf die Leiste behalten
function markePopup(key, id, anchorEl) {
  document.querySelector('.mk-pop')?.remove();
  const m = markeVon(key, id); if (!m) return;
  document.body.insertAdjacentHTML('beforeend', `<div class="mk-pop" role="dialog" aria-label="Markierung"><div class="mk-pop-f">${Object.entries(FARBEN).map(([f, n]) => `<button data-mkfarbe="${f}" class="mkb-${f} ${m.farbe === f ? 'on' : ''}"${FARB_BEDEUTUNG.includes(f) ? '' : ` aria-label="${n}" title="${n}"`}><i></i>${FARB_BEDEUTUNG.includes(f) ? n : ''}</button>`).join('')}</div>
    <div class="seg mk-stil"><button data-mkstil="" class="${m.stil === 'u' ? '' : 'on'}">Hinterlegt</button><button data-mkstil="u" class="${m.stil === 'u' ? 'on' : ''}"><u>Unterstrichen</u></button></div>
    <textarea rows="3" placeholder="Notiz zu dieser Stelle …" aria-label="Notiz">${esc(m.notiz)}</textarea>
    <div class="mk-pop-a"><button class="btn" data-mkweg>Entfernen</button><button class="btn btn-main" data-mkok>Fertig</button></div></div>`);
  const p = document.querySelector('.mk-pop'); p.dataset.key = key; p.dataset.id = id;
  const b = anchorEl.getBoundingClientRect(), w = p.offsetWidth;
  p.style.left = Math.max(8, Math.min(innerWidth - w - 8, b.left)) + 'px';
  p.style.top = Math.min(innerHeight - p.offsetHeight - 8, b.bottom + 8) + 'px';
  if (!m.notiz && anchorEl.dataset.fokus) p.querySelector('textarea').focus();
}
document.addEventListener('click', e => {
  const neu = e.target.closest('[data-mkneu]');
  if (neu) {
    e.stopPropagation();
    if (neu.dataset.mkneu === 'melden') { document.querySelector('.mk-leiste')?.remove(); const x = cur();   // Fehler an der ausgewählten Stelle melden
      if (typeof meldeDialog === 'function') meldeDialog(`Lernseite · ${x.f.name} · ${txt(x.t.title)}`); return; }
    const f = neu.dataset.mkneu, m = speichereMarke(f === 'notiz' ? 'gelb' : f === 'unter' ? (S.einst.mkUnter || 'blau') : f, f === 'unter' ? 'u' : ''); document.querySelector('.mk-leiste')?.remove();
    if (m) { render(); const el = document.querySelector(`mark[data-mk="${m.id}"]`); if (el && f === 'notiz') { el.dataset.fokus = 1; markePopup(V.fid + '/' + V.tid, m.id, el); } }
    return;
  }
  const pop = e.target.closest('.mk-pop');
  if (pop) {
    e.stopPropagation();
    const key = pop.dataset.key, m = markeVon(key, pop.dataset.id); if (!m) return;
    const fb = e.target.closest('[data-mkfarbe]');
    if (fb) { m.farbe = fb.dataset.mkfarbe; save(); pop.querySelectorAll('[data-mkfarbe]').forEach(x => x.classList.toggle('on', x === fb)); }
    const st = e.target.closest('[data-mkstil]');
    if (st) { if (st.dataset.mkstil === 'u') { m.stil = 'u'; S.einst.mkUnter = m.farbe; } else delete m.stil; save(); pop.querySelectorAll('[data-mkstil]').forEach(x => x.classList.toggle('on', x === st)); }
    if (e.target.closest('[data-mkweg]')) { loescheMarke(key, m.id); pop.remove(); render(); }
    if (e.target.closest('[data-mkok]')) { m.notiz = pop.querySelector('textarea').value.trim(); save(); pop.remove(); render(); }
    return;
  }
  if (document.querySelector('.mk-pop')) { e.stopPropagation(); const p = document.querySelector('.mk-pop'), m = markeVon(p.dataset.key, p.dataset.id); if (m) { m.notiz = p.querySelector('textarea').value.trim(); save(); } p.remove(); render(); return; }
  const mk = e.target.closest('mark.mk[data-mk], .mk-notiz');
  if (mk && !V.blur && V.screen === 'lern' && !e.target.closest('#ov')) { e.stopPropagation(); markePopup(V.fid + '/' + V.tid, mk.dataset.mk, mk); return; }
  const glo = e.target.closest('.glo'); if (glo && !V.blur) { e.stopPropagation(); erklaere(glo); return; }
  if (!e.target.closest('#glo-pop')) document.getElementById('glo-pop')?.remove();
}, true);

/* Seitenleiste „Markiert“: alle Markierungen und Notizen, wahlweise Unterthema · Oberthema · Fach */
const V_MK = { bereich: 'unter', farbe: '' };
function markeListe() {
  const x = cur(), out = [];
  if (V_MK.bereich === 'alle') {   // alle Fächer: jede Stelle mit Markierung oder Notiz
    for (const key of new Set([...Object.keys(S.mark), ...Object.keys(S.notiz)])) { const tt = TOP[key]; if (!tt) continue;
      for (const m of (S.mark[key] || [])) if (!V_MK.farbe || m.farbe === V_MK.farbe) out.push({ m, key, tt });
      if (S.notiz[key] && !V_MK.farbe) out.push({ frei: S.notiz[key], key, tt }); }
    const pos = k => { const tt = TOP[k]; return D.faecher.indexOf(tt.f) * 1e4 + kapNr(tt.f, tt.k) * 100 + tt.k.topics.indexOf(tt.t); };
    return out.sort((a, b) => pos(a.key) - pos(b.key));
  }
  const ts = V_MK.bereich === 'unter' ? [x.t] : V_MK.bereich === 'ober' ? x.k.topics : x.f.kapitel.flatMap(k => k.topics);
  for (const t of ts) { const key = x.f.id + '/' + t.id, tt = TOP[key];
    for (const m of (S.mark[key] || [])) if (!V_MK.farbe || m.farbe === V_MK.farbe) out.push({ m, key, tt });
    if (S.notiz[key] && !V_MK.farbe && t !== x.t) out.push({ frei: S.notiz[key], key, tt }); }
  return out;
}
function markiertPanel() {
  document.getElementById('ov')?.remove();
  const x = cur(), key = x.f.id + '/' + x.t.id, l = markeListe();
  document.body.insertAdjacentHTML('beforeend', `<div id="ov" class="ov ov-seite" role="dialog" aria-modal="true" aria-label="Markiert und Notizen" style="--fach:${x.f.farbe}"><div class="ov-box">
    <div class="ov-kopf"><b>Markiert & Notizen</b><span></span><button class="btn" data-act="ov-zu">Schließen</button></div>
    <div class="seg mk-seg">${[['unter', 'Unterthema'], ['ober', 'Oberthema'], ['fach', 'Fach'], ['alle', 'Alle Fächer']].map(([v, n]) => `<button class="${V_MK.bereich === v ? 'on' : ''}" data-mkbereich="${v}">${n}</button>`).join('')}</div>
    <div class="mk-filter">${[['', 'Alle'], ...Object.entries(FARBEN)].map(([f, n]) => `<button class="mkb-${f || 'alle'} ${V_MK.farbe === f ? 'on' : ''}" data-mkfilter="${f}"><i></i>${n}</button>`).join('')}</div>
    ${V_MK.bereich === 'unter' ? `<label class="mk-frei"><small>Notiz zu „${esc(x.t.title)}“</small><textarea rows="3" data-freinotiz="${key}" placeholder="Was du dir zu diesem Unterthema merken willst …">${esc(S.notiz[key] || '')}</textarea></label>` : ''}
    <ul class="mk-liste">${l.map(e => e.m ? `<li><button data-mkspring="${e.key}|${e.m.id}" class="mk-it mkb-${e.m.farbe}"><i></i><span><q>${esc(e.m.text.slice(0, 220))}</q>${e.m.notiz ? `<em>${esc(e.m.notiz)}</em>` : ''}${V_MK.bereich !== 'unter' ? `<small>${V_MK.bereich === 'alle' ? esc(e.tt.f.name) + ' · ' : ''}${esc(e.tt.t.title)}</small>` : ''}${e.m.verloren ? '<small>Stelle im Text nicht mehr gefunden</small>' : ''}</span></button></li>`
      : `<li><button data-mkspring="${e.key}|" class="mk-it mkb-notiz"><i></i><span><em>${esc(e.frei)}</em><small>Notiz · ${V_MK.bereich === 'alle' ? esc(e.tt.f.name) + ' · ' : ''}${esc(e.tt.t.title)}</small></span></button></li>`).join('')}</ul>
    ${l.length ? '' : `<p class="dim3">Noch nichts markiert. Text auswählen, dann eine Farbe wählen: <b>Gelb</b> wichtig, <b>Grün</b> wird zur Karteikarte, <b>Rot</b> heißt: verstehe ich noch nicht.</p>`}</div></div>`);
  const ov = document.getElementById('ov');
  ov.onclick = e => {
    if (e.target === ov) return ov.remove();
    const b = e.target.closest('[data-mkbereich]'); if (b) { V_MK.bereich = b.dataset.mkbereich; return markiertPanel(); }
    const f = e.target.closest('[data-mkfilter]'); if (f) { V_MK.farbe = f.dataset.mkfilter; return markiertPanel(); }
    const s = e.target.closest('[data-mkspring]'); if (s) { const [key, id] = s.dataset.mkspring.split('|'), [fid, tid] = key.split('/'); ov.remove();
      V.springMarke = id; go(`lern|${fid}|${TOP[key].k.id}|${tid}`); }
  };
  const ta = ov.querySelector('[data-freinotiz]');
  if (ta) ta.oninput = () => { const k = ta.dataset.freinotiz, v = ta.value.trim(); if (v) S.notiz[k] = v; else delete S.notiz[k]; save(); };
}
const markZahl = key => (S.mark[key] || []).length + (S.notiz[key] ? 1 : 0);
const markPunkte = key => { const fs = new Set((S.mark[key] || []).map(m => m.farbe)); if (S.notiz[key]) fs.add('notiz'); return fs.size ? `<span class="mk-punkte">${[...fs].map(f => `<i class="mkp-${f}"></i>`).join('')}</span>` : ''; };

/* ---------- Erklärfenster: Fachbegriffe im Text antippen ---------- */
function markiereBegriffe(root, x) {
  if (!root || !x.f.glossar) return;
  const nm = new Set(x.f.nichtMarkieren || []);
  x.f.glossar.forEach((g, i) => {
    if (g.t === x.t.id || nm.has(g.b)) return;
    let rx; try { rx = new RegExp('(^|[^0-9A-Za-zÄÖÜäöüß])(' + g.muster + ')(?![0-9A-Za-zÄÖÜäöüß])'); } catch (e) { return; }
    const w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, { acceptNode: n => n.parentElement && !n.parentElement.closest(NICHT_TEXT + ',h1,h2,h3,a,.glo,mark,.fig-cap,label') ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT });
    let n; while ((n = w.nextNode())) {
      const m = rx.exec(n.nodeValue); if (!m) continue;
      const s = m.index + m[1].length, rest = n.splitText(s); rest.splitText(m[2].length);
      const sp = document.createElement('span'); sp.className = 'glo'; sp.tabIndex = 0; sp.dataset.g = i; sp.setAttribute('role', 'button');
      rest.parentNode.insertBefore(sp, rest); sp.appendChild(rest); break;
    }
  });
}
function erklaere(el) {
  document.getElementById('glo-pop')?.remove();
  const x = cur(), g = x && x.f.glossar[+el.dataset.g]; if (!g) return;
  const h = TOP[x.f.id + '/' + g.t];
  document.body.insertAdjacentHTML('beforeend', `<div id="glo-pop" role="dialog" aria-label="${esc(g.b)}"><b>${esc(g.b)}</b><p>${esc(g.e)}</p>${h ? `<button data-go="lern|${x.f.id}|${h.k.id}|${h.t.id}">Mehr dazu: ${esc(h.t.title)} →</button>` : ''}</div>`);
  const p = document.getElementById('glo-pop'), b = el.getBoundingClientRect(), w = p.offsetWidth;
  p.style.left = Math.max(8, Math.min(innerWidth - w - 8, b.left)) + 'px';
  p.style.top = (b.bottom + p.offsetHeight + 12 < innerHeight ? b.bottom + 6 : b.top - p.offsetHeight - 6) + 'px';
}
document.addEventListener('keydown', e => { if (e.key === 'Enter' && document.activeElement && document.activeElement.classList.contains('glo')) erklaere(document.activeElement); });
window.addEventListener('scroll', () => { document.getElementById('glo-pop')?.remove(); document.querySelector('.mk-leiste') && leisteZeigen(); }, { passive: true });

/* ---------- Verdecken: Fachbegriffe im Text, Aufzählungspunkte und Begriffe in Schaubildern (nie das ganze Bild) ----------
   Text: <b>, <strong>, Fachbegriffe (.glo), Merksatz, Tabellenzellen – per CSS. Hier zusätzlich markiert (.vd):
   · Aufzählungspunkte ohne fett gesetzten Begriff (sonst wird nur der Begriff verdeckt)
   · Beschriftungen in Schaubildern (SVG-Text mit Buchstaben; reine Zahlen, Achsen-Ticks und Einheiten bleiben sichtbar)
   Bereiche mit class="nv" werden nie verdeckt (z. B. eine Ablaufkette als Orientierung). Schaubilder zeichnen sich nach jedem
   Regler neu; ein Beobachter markiert neue Beschriftungen nach. */
const VD_WORT = /[A-Za-zÄÖÜäöüß]{3,}/, VD_EINHEIT = /^\s*[\d.,%€\s+−\-–·×:/()]*(Stück|Stk\.?|Tage?n?|Wochen?|Monate?n?|Jahre?n?|Std\.?|Min\.?|kg|t|m|km|ME|GE|ZE)?\s*$/;
function vdMarkiere(root) {
  if (!root) return;
  root.querySelectorAll('li').forEach(li => {
    if (li.closest('.nv, .q-liste, .seg, nav, button') || li.querySelector('b, strong, .glo, ul, ol')) return;
    if (VD_WORT.test(li.textContent)) li.classList.add('vd');
  });
  root.querySelectorAll('svg text').forEach(t => {
    if (t.closest('.nv')) return;
    const s = t.textContent.trim();
    if (VD_WORT.test(s) && !VD_EINHEIT.test(s)) t.classList.add('vd');
  });
  if (!root._vdBeob && typeof MutationObserver === 'function') {   // neu gezeichnete Schaubilder nachmarkieren
    let warte = 0;
    root._vdBeob = new MutationObserver(() => { if (!V.blur || warte) return; warte = requestAnimationFrame(() => { warte = 0; vdMarkiere(root); }); });
    root._vdBeob.observe(root, { childList: true, subtree: true });
  }
}

/* Nach dem Zeichnen einer Lernseite: Begriffe, Markierungen, Sprung zu einer Markierung */
function nachLernRender() {
  const x = cur(), root = document.querySelector('.bl-card .inhalt'); if (!root) return;
  if (typeof formelWaechter === 'function') formelWaechter(root);   // Rechner-Ausgaben der Schaubilder wie auf Papier
  markiereBegriffe(root, x);
  wendeMarkierungen(root, x.f.id + '/' + x.t.id);
  if (V.blur) vdMarkiere(root);
  if (V.springMarke) { const el = root.querySelector(`mark[data-mk="${V.springMarke}"]`); V.springMarke = null;
    if (el && window.lwOeffne) window.lwOeffne(el);
    if (el) { const top = el.closest('.topic'); if (el.closest('.article') && top) top.classList.add('full'); el.classList.add('fund'); setTimeout(() => el.scrollIntoView({ block: 'center', behavior: 'smooth' }), 80); } }
}
