
/* Eingabe-Beschriftungen zusammenhalten, damit z. B. K<sub>L</sub> nicht als „K L“ zerfällt */
$$('.ctrl label').forEach(l => {
  const ns = [...l.childNodes].filter(n => !(n.nodeType === 1 && /^(INPUT|SELECT)$/.test(n.tagName)));
  if (ns.length < 2) return; const sp = document.createElement('span'); l.insertBefore(sp, ns[0]); ns.forEach(n => sp.appendChild(n));
});
/* Schmale Bildschirme: Schaubilder nur so weit verkleinern, dass die kleinste Schrift lesbar bleibt (sonst seitlich wischen) */
function fitSvgs(){
  $$('.figure svg').forEach(svg => {
    if (svg.closest('.zoomed')) return;
    const vb = svg.viewBox && svg.viewBox.baseVal; if (!vb || !vb.width) return;
    let fs = 99; $$('text', svg).forEach(t => { const f = parseFloat(t.getAttribute('font-size') || getComputedStyle(t).fontSize); if (f && t.textContent.trim() && f < fs) fs = f; });
    if (fs === 99) return;
    if (!svg.dataset.mw) svg.dataset.mw = parseFloat(svg.style.minWidth) || 0;
    const need = Math.min(vb.width, vb.width * (document.body.classList.contains('ruhig') ? 7.6 : 8.5) / fs);
    svg.style.minWidth = Math.max(+svg.dataset.mw, need) + 'px';
    if (!svg.parentNode.classList.contains('svgscroll')) { const w = document.createElement('div'); w.className = 'svgscroll'; svg.parentNode.insertBefore(w, svg); w.appendChild(svg); const h = document.createElement('div'); h.className = 'swipe'; h.textContent = svg.closest('.mfig-body,#fmB') ? '↔ Seitlich wischen' : '↔ Seitlich wischen oder „Vergrößern“ antippen'; w.after(h); }
    const w = svg.parentNode; w.nextElementSibling.hidden = w.scrollWidth <= w.clientWidth + 2;
  });
}
fitSvgs(); window.addEventListener('resize', fitSvgs);
const topicTitle = t => $('.t-title', t).childNodes[0].textContent.trim();
const escH = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
/* Zu einem Thema springen (aus Kompakt, Suche oder Erklär-Fenster) */
function goTopic(id, full){
  const t = document.getElementById(id); if (!t) return;
  $$('#viewSeg button').forEach(x => x.classList.toggle('on', x.dataset.view === 'v-over'));
  $$('.view').forEach(v => v.classList.toggle('on', v.id === 'v-over'));
  t.classList.add('open'); if (full) t.classList.add('full');
  t.scrollIntoView({ behavior: 'smooth', block: 'start' });
}
/* Sprungziele nicht unter der klebenden Leiste verstecken */
const setBarH = () => document.documentElement.style.setProperty('--barh', ($('.bar') ? $('.bar').offsetHeight : 60) + 'px');
setBarH(); window.addEventListener('resize', setBarH);

/* Klausur-Kompakt: sammelt Merksatz, Formeln, Klausurfrage und Fallen aus jedem klausurrelevanten Thema */
$$('.chap').forEach(ch => {
  const ts = $$('.topic', ch).filter(t => $('.box.excl', t)); if (!ts.length) return;
  const grp = document.createElement('section'); grp.className = 'kgrp'; $('#kList').appendChild(grp);
  const h = document.createElement('h2'); h.className = 'kchap'; h.textContent = ch.dataset.title; grp.appendChild(h);
  ts.forEach(t => {
    const c = document.createElement('div'); c.className = 'kc'; c.dataset.t = t.id;
    const b = document.createElement('button'); b.type = 'button'; b.textContent = topicTitle(t); b.onclick = () => goTopic(t.id); c.appendChild(b);
    const m = $('.merk', t); if (m) c.appendChild(m.cloneNode(true));
    const fx = $$('.fx', t);
    if (fx.length) { c.classList.add('has-fx'); const r = document.createElement('div'); r.className = 'fx-row'; fx.forEach(f => { const k = f.cloneNode(true); $$('.fx-z,.fx-why', k).forEach(z => z.remove()); r.appendChild(k); }); c.appendChild(r); }
    const ml = $('.mliste', t); if (ml) { c.classList.add('has-ml'); c.appendChild(ml.cloneNode(true)); }
    if ($('.t-title .badge:not(.alt)', t)) c.classList.add('stern');
    const x = $('.box.excl', t);
    if (x) { c.classList.add('has-exam'); const d = document.createElement('div'); d.className = 'kx'; d.innerHTML = x.innerHTML; c.appendChild(d); }
    const f = $$('.box.fall li', t);
    if (f.length) { c.classList.add('has-fall'); const d = document.createElement('div'); d.className = 'kf'; d.innerHTML = '<b>Typische Fallen</b><ul></ul>'; f.forEach(li => $('ul', d).appendChild(li.cloneNode(true))); c.appendChild(d); }
    grp.appendChild(c);
  });
});
$$('#kompSeg button').forEach(b => b.onclick = () => { $$('#kompSeg button').forEach(x => x.classList.toggle('on', x === b)); $('#kList').dataset.f = b.dataset.f; $$('.kgrp').forEach(g => g.hidden = false); $$('.kgrp').forEach(g => g.hidden = !$$('.kc', g).some(c => c.offsetParent)); });
if ($('#printBtn')) $('#printBtn').onclick = () => window.print();
/* Drucken immer hell, sonst landet ein dunkler Hintergrund auf dem Papier */
let themeBeforePrint = null;
window.addEventListener('beforeprint', () => { themeBeforePrint = document.documentElement.getAttribute('data-theme'); document.documentElement.setAttribute('data-theme', 'light'); });
window.addEventListener('afterprint', () => { if (themeBeforePrint) document.documentElement.setAttribute('data-theme', themeBeforePrint); });

/* Suche über alle Themen und Begriffe */
const fold = s => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
const plainTxt = el => {
  if (!el) return '';
  const c = el.cloneNode(true); $$('div,p,li,h3,h4,td,th,br,.box-h', c).forEach(x => x.after(' '));  // Blöcke nicht zusammenkleben
  return c.textContent.replace(/\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]/g, ' ').replace(/\s+/g, ' ').trim();
};
const SIDX = $$('.topic').map(t => {
  const e = { id: t.id, title: topicTitle(t), chap: t.closest('.chap').dataset.title, kern: plainTxt($('.t-kern', t)) };
  e.top = plainTxt($('.lv1', t)) + ' ' + plainTxt($('.merk', t));
  const art = $('.article', t).cloneNode(true); $$('.toc,.relline', art).forEach(x => x.remove());
  e.body = plainTxt(art);
  e.f = [e.title, e.kern, e.top, e.body].map(fold);
  return e;
});
function hl(raw, words){
  const f = fold(raw), rx = new RegExp(words.map(w => w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|'), 'g');
  let out = '', i = 0;
  for (const m of f.matchAll(rx)) { if (!m[0]) break; out += escH(raw.slice(i, m.index)) + '<mark>' + escH(raw.slice(m.index, m.index + m[0].length)) + '</mark>'; i = m.index + m[0].length; }
  return out + escH(raw.slice(i));
}
function snip(raw, w){
  const p = fold(raw).indexOf(w); if (p < 0) return raw.slice(0, 140);
  const a = Math.max(0, raw.lastIndexOf(' ', Math.max(0, p - 50)));
  return (a > 0 ? '… ' : '') + raw.slice(a, p + 110).trim() + (p + 110 < raw.length ? ' …' : '');
}
const SM = document.createElement('div'); SM.className = 'modal smodal'; SM.id = 'srchModal';
SM.innerHTML = '<div class="mbox sbox" role="dialog" aria-modal="true" aria-label="Suche"><div class="sin"><span aria-hidden="true">⌕</span><input id="sIn" type="search" placeholder="Begriff oder Thema, z. B. Leverage" autocomplete="off" aria-label="Suchbegriff"><button type="button" id="sX">Schließen</button></div><div id="sRes"></div></div>';
document.body.appendChild(SM);
let sHits = [], sCur = 0;
function runSearch(){
  const words = fold($('#sIn').value).split(/\s+/).filter(w => w.length > 1), box = $('#sRes');
  if (!words.length) { sHits = []; box.innerHTML = '<div class="sempty">Tippe einen Begriff oder ein Thema ein, zum Beispiel „Barwert“, „Haftung“ oder „Maslow“.</div>'; return; }
  const terms = GLO.map((g, i) => ({ g, i, f: fold(g[0]) })).filter(x => words.every(w => x.f.includes(w)))
    .sort((a, b) => (b.f.startsWith(words[0]) - a.f.startsWith(words[0])) || a.f.length - b.f.length).slice(0, 3);
  const tops = SIDX.map(e => {
    let s = 0;
    for (const w of words) { const k = e.f.findIndex(f => f.includes(w)); if (k < 0) return null; s += [12, 5, 3, 1][k]; }
    return { e, s, deep: !words.some(w => e.f[0].includes(w) || e.f[1].includes(w) || e.f[2].includes(w)) };
  }).filter(Boolean).sort((a, b) => b.s - a.s).slice(0, 12);
  sHits = [...terms.map(x => ({ term: x.g })), ...tops]; sCur = 0;
  if (!sHits.length) { box.innerHTML = '<div class="sempty">Nichts gefunden. Versuch ein anderes Wort oder eine kürzere Schreibweise.</div>'; return; }
  box.innerHTML = sHits.map((h, i) => h.term
    ? `<button class="sr term" data-i="${i}" type="button"><small>Begriff</small><b>${hl(h.term[0], words)}</b><span>${escH(h.term[3])} <u>→ ${escH(h.term[4])}</u></span></button>`
    : `<button class="sr" data-i="${i}" type="button"><small>${escH(h.e.chap)}</small><b>${hl(h.e.title, words)}</b><span>${hl(h.deep ? snip(h.e.body, words[0]) : h.e.kern, words)}</span></button>`).join('');
  $$('.sr', box).forEach(b => b.onclick = () => pickSearch(+b.dataset.i));
  paintCur();
}
function paintCur(){ $$('#sRes .sr').forEach((b, i) => b.classList.toggle('cur', i === sCur)); const c = $('#sRes .sr.cur'); if (c) c.scrollIntoView({ block: 'nearest' }); }
function pickSearch(i){ const h = sHits[i]; if (!h) return; closeSearch(); h.term ? goTopic(h.term[2]) : goTopic(h.e.id, h.deep); }
function openSearch(){ hideGlo(); SM.classList.add('on'); document.body.classList.add('nozoomscroll'); $('#sIn').value = ''; runSearch(); $('#sIn').focus(); }
function closeSearch(){ SM.classList.remove('on'); document.body.classList.remove('nozoomscroll'); }
$('#sIn').oninput = runSearch;
$('#sIn').onkeydown = e => {
  if (e.key === 'ArrowDown') { e.preventDefault(); sCur = Math.min(sCur + 1, sHits.length - 1); paintCur(); }
  else if (e.key === 'ArrowUp') { e.preventDefault(); sCur = Math.max(sCur - 1, 0); paintCur(); }
  else if (e.key === 'Enter') { e.preventDefault(); pickSearch(sCur); }
};
$('#sX').onclick = closeSearch; SM.onclick = e => { if (e.target === SM) closeSearch(); };
if ($('#srchBtn')) $('#srchBtn').onclick = openSearch;
document.addEventListener('keydown', e => {
  if (e.key === 'Escape' && SM.classList.contains('on')) { closeSearch(); return; }
  if (e.key === 'Escape') hideGlo();
  const typing = /INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName);
  if (!typing && (e.key === '/' || ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k'))) { e.preventDefault(); openSearch(); }
});

/* Erklär-Fenster: Fachbegriffe im Text antippen */
const GP = document.createElement('div'); GP.id = 'gloPop'; GP.setAttribute('role', 'dialog'); document.body.appendChild(GP);
let gpEl = null;
function showGlo(el){
  const g = GLO[+el.dataset.g]; hideGlo(); gpEl = el; el.classList.add('on');
  GP.innerHTML = `<b>${escH(g[0])}</b>${escH(g[3])}<br><button type="button">Mehr im Thema „${escH(g[4])}“ →</button>`;
  $('button', GP).onclick = () => { hideGlo(); goTopic(g[2]); };
  GP.classList.add('on');
  const r = el.getBoundingClientRect(), w = GP.offsetWidth, h = GP.offsetHeight;
  let y = r.bottom + 6; if (y + h > innerHeight - 10) y = Math.max(10, r.top - h - 6);
  GP.style.left = Math.min(Math.max(16, r.left), innerWidth - w - 16) + 'px'; GP.style.top = y + 'px';
}
function hideGlo(){ GP.classList.remove('on'); if (gpEl) gpEl.classList.remove('on'); gpEl = null; }
document.addEventListener('click', e => {
  const g = e.target.closest && e.target.closest('.glo');
  if (g) { g === gpEl ? hideGlo() : showGlo(g); return; }
  if (!e.target.closest || !e.target.closest('#gloPop')) hideGlo();
});
document.addEventListener('keydown', e => { if (e.key === 'Enter' && document.activeElement.classList.contains('glo')) showGlo(document.activeElement); });
window.addEventListener('scroll', () => { if (gpEl) hideGlo(); }, { passive: true });
function markTerms(){
  // pro Thema nur das erste Vorkommen, nie im Heimat-Thema, nicht in Schaubildern, Formeln, Überschriften oder Übungen
  const SKIP = 'svg,.katex,.figure,button,a,h3,h4,.sec-h,.box-h,.fx,.quizsrc,.q,.toc,.relline,.glo,input,label,.merk>b,.actions';
  const L = 'A-Za-zÄÖÜäöüß';
  const all = GLO.map((g, i) => ({ i, home: g[2], rx: new RegExp(`(^|[^${L}0-9-])(${g[1]})(?![${L}])`) })).filter(x => GLO[x.i][5]);
  $$('#v-over .topic').forEach(t => {
    let todo = all.filter(x => x.home !== t.id);  // noch zu markieren; 'all' dient zum Erkennen längerer Begriffe
    const w = document.createTreeWalker($('.t-body', t), NodeFilter.SHOW_TEXT, { acceptNode: n => n.parentElement.closest(SKIP) ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT });
    const nodes = []; while (w.nextNode()) nodes.push(w.currentNode);
    for (let n of nodes) {
      while (n && todo.length && n.data) {
        let best = null;
        for (const x of all) { const m = x.rx.exec(n.data); if (!m) continue; const at = m.index + m[1].length; if (!best || at < best.at || (at === best.at && m[2].length > best.len)) best = { x, at, len: m[2].length }; }
        if (!best) break;
        const mid = n.splitText(best.at), rest = mid.splitText(best.len);
        if (!todo.includes(best.x)) { n = rest; continue; }  // längerer Begriff schon erklärt oder im Heimat-Thema: Stelle überspringen
        const s = document.createElement('span'); s.className = 'glo'; s.tabIndex = 0; s.setAttribute('role', 'button'); s.dataset.g = best.x.i;
        mid.replaceWith(s); s.appendChild(mid);
        todo = todo.filter(x => x !== best.x); n = rest;
      }
    }
  });
}

window.addEventListener('load', () => {
  try {
    if (window.renderMathInElement) renderMathInElement(document.body, {
      delimiters: [{ left: '\\[', right: '\\]', display: true }, { left: '\\(', right: '\\)', display: false }],
      throwOnError: false,
      trust: c => c.command === '\\htmlClass', strict: c => c === 'htmlExtension' ? 'ignore' : 'warn'  // \htmlClass für Farbmarken in fxkette()
    });
  } finally { markTerms(); setBarH(); wideFx(); }
});
/* Passt eine Formel nicht in ihre Kachel, stehen alle Formeln der Zeile untereinander (gleich breit, ruhiges Raster) */
function wideFx(){
  const probe = document.createElement('div'); probe.style.cssText = 'position:absolute;left:-9999px;top:0;visibility:hidden;white-space:nowrap'; document.body.appendChild(probe);
  $$('.fx-row').forEach(row => {
    const n = row.children.length; if (n < 2) return;
    const max = n === 4 ? 420 : n === 2 ? 420 : 290;
    for (const fx of row.children) { const k = $('.katex-display', fx); if (!k) continue; const c = k.cloneNode(true); probe.appendChild(c); const w = c.scrollWidth; probe.removeChild(c); if (w > max) { row.classList.add('stack'); break; } }
  });
  probe.remove();
}
/* Schieberegler: Wert neben der Beschriftung mitführen */
$$('.rg input[type=range]').forEach(r => { const o = document.getElementById(r.id + '-o'); if (!o || o.hasAttribute('data-own')) return; const u = o.dataset.u || '';
  const show = () => { o.textContent = (+r.value).toLocaleString('de-DE') + u; }; r.addEventListener('input', show); show(); });
