
const fmt = (n, d = 2) => (Math.abs(n) < 1e-12 ? 0 : n).toLocaleString('de-DE', { maximumFractionDigits: d });
const eur = n => (Math.abs(n) < 1e-12 ? 0 : n).toLocaleString('de-DE', { minimumFractionDigits: 2, maximumFractionDigits: 2 });  // Geldbeträge immer mit 2 Nachkommastellen
const store = {
  get(k){ try { return JSON.parse(localStorage.getItem(k)); } catch(e){ return null; } },
  set(k,v){ try { localStorage.setItem(k, JSON.stringify(v)); } catch(e){} }
};
const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];

/* Ansicht */
$$('#viewSeg button').forEach(b => b.onclick = () => {
  $$('#viewSeg button').forEach(x => x.classList.toggle('on', x === b));
  $$('.view').forEach(v => v.classList.toggle('on', v.id === b.dataset.view));
  window.scrollTo({ top: 0 });
});

/* Hell / Dunkel */
const sysDark = window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches;
function setTheme(t, merken){
  document.documentElement.setAttribute('data-theme', t);
  const b = $('#themeBtn'); if (b) b.innerHTML = t === 'dark' ? '☀<span class="lbl"> Hell</span>' : '☾<span class="lbl"> Dunkel</span>';
  if (merken) store.set('lp-theme', t);
}
if ($('#themeBtn')) $('#themeBtn').onclick = () => setTheme(document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark', true);

/* Kurzer Hinweis oben, einmal wegklickbar */
if ($('#hint')) { if (store.get(FACH + '-hint-off')) $('#hint').remove(); else $('#hint button').onclick = () => { $('#hint').remove(); store.set(FACH + '-hint-off', true); }; }
setTheme(store.get('lp-theme') || (sysDark ? 'dark' : 'light'));

/* Kapitel ein- und ausklappen */
const shut = new Set(store.get(FACH + '-shut') || []);
function setShut(ch, on){
  ch.classList.toggle('shut', on); $('.chap-head', ch).setAttribute('aria-expanded', !on);
  on ? shut.add(ch.id) : shut.delete(ch.id); store.set(FACH + '-shut', [...shut]); paintCall();
}
function paintCall(){ const b = $('#callBtn'); if (!b) return; const all = $$('.chap').every(c => c.classList.contains('shut')); b.textContent = all ? '▾ Kapitel auf' : '▸ Kapitel zu'; }
$$('.chap').forEach(ch => {
  const h = $('.chap-head', ch);
  h.onclick = () => setShut(ch, !ch.classList.contains('shut'));
  h.onkeydown = e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); h.onclick(); } };
  if (shut.has(ch.id)) setShut(ch, true);
});
if ($('#callBtn')) $('#callBtn').onclick = () => { const all = $$('.chap').every(c => c.classList.contains('shut')); $$('.chap').forEach(c => setShut(c, !all)); };
paintCall();
/* Wer zu einem Thema springt (Querverweis, Vergleichsknopf …), klappt dessen Kapitel automatisch auf */
const _siv = Element.prototype.scrollIntoView;
Element.prototype.scrollIntoView = function(o){ const ch = this.closest && this.closest('.chap.shut'); if (ch && !this.classList.contains('chap')) setShut(ch, false); return _siv.call(this, o); };
/* Fortschritt */
const learned = new Set(store.get(FACH + '-learned') || []);
function paintProgress(){
  $$('.chap').forEach(ch => {
    const ts = $$('.topic', ch), done = ts.filter(t => learned.has(t.dataset.id)).length;
    $('.chap-prog i', ch).style.width = (done / ts.length * 100) + '%';
    $('.chap-prog small', ch).textContent = `${done} von ${ts.length} Themen gelernt`;
  });
}
$$('.topic').forEach(t => {
  const id = t.dataset.id;
  $('.t-head', t).onclick = () => { t.classList.toggle('open'); if (t.classList.contains('open')) store.set(FACH + '-last', t.id); };
  const qb = $('.qbtn', t); if (qb) qb.onclick = () => $('.quiz', t).classList.toggle('on');
  const lb = $('.learned', t);
  const paint = () => { const on = learned.has(id); t.classList.toggle('done', on); lb.classList.toggle('ok', on); lb.textContent = on ? '✓ Gelernt' : 'Als gelernt markieren'; };
  lb.onclick = () => { learned.has(id) ? learned.delete(id) : learned.add(id); store.set(FACH + '-learned', [...learned]); paint(); paintProgress(); };
  paint();
});
paintProgress();
/* Querverweise öffnen das Zielthema */
$$('.links a').forEach(a => a.onclick = e => {
  const t = document.getElementById(a.getAttribute('href').slice(1));
  if (!t) return; e.preventDefault(); t.classList.add('open'); t.scrollIntoView({ behavior: 'smooth' });
});
/* Sprung aus dem Portal: #themen-id öffnet dieses Thema */
/* #kompakt öffnet Klausur-Kompakt, #thema~ueben öffnet das Thema mit den Übungen (Sprünge aus dem Lernplan) */
function springe(){ let h = decodeURIComponent(location.hash.slice(1));
  if (h === 'kompakt' || h === 'kompakt-wackel') { const b = $('#viewSeg button[data-view="v-komp"]'); if (b) setTimeout(() => { b.click(); if (h === 'kompakt-wackel') { const w = $('[data-wackel]'); if (w && w.getAttribute('aria-pressed') !== 'true') w.click(); } }, 50); return; }
  const ueben = h.endsWith('~ueben'); if (ueben) h = h.slice(0, -6);
  const t = h && document.getElementById(h);
  if (t && t.classList.contains('topic')) {
    const v = t.closest('.view'), ov = $('#viewSeg button[data-view="v-over"]');
    if (v && !v.classList.contains('on') && ov) ov.click();  // aus Klausur-Kompakt zurück in die Übersicht
    t.classList.add('open'); store.set(FACH + '-last', t.id);
    setTimeout(() => { t.scrollIntoView({ block: 'start' });
      if (ueben) { const q = $('.quizbtn', t) || $('.qbtn', t) || $('.sbtn[data-p="quiz"]', t); if (q) q.click(); } }, 80); } }
springe(); window.addEventListener('hashchange', springe);


/* Vorlage A: Abschnitts-Knöpfe */
$$('.topic.v2').forEach(t => {
  $$('.sbtn', t).forEach(btn => btn.onclick = () => {
    const p = $(`.panel[data-p="${btn.dataset.p}"]`, t), on = !p.classList.contains('on');
    p.classList.toggle('on', on); btn.classList.toggle('on', on);
  });
  const erkl = $('.panel[data-p="erkl"] .erkl', t), toc = $('.panel[data-p="erkl"] .toc', t);
  if (erkl && toc) $$('h4', erkl).forEach((h, i) => {
    h.id = t.id + '-h' + i; const a = document.createElement('a'); a.href = '#' + h.id; a.textContent = h.textContent;
    a.onclick = e => { e.preventDefault(); h.scrollIntoView({ behavior: 'smooth', block: 'center' }); }; toc.appendChild(a);
  });
});
function setXall(on){ document.body.classList.toggle('xall', on); const b = $('#xallBtn'); if (b) { b.classList.toggle('on', on); b.innerHTML = on ? 'Alle <span class="lbl">ganz </span>erklärt' : 'Alle <span class="lbl">ganz </span>erklären'; } store.set(FACH + '-xall', on); }
if ($('#xallBtn')) { $('#xallBtn').onclick = () => setXall(!document.body.classList.contains('xall')); setXall(!!store.get(FACH + '-xall')); }


/* v3: Ganz erklären, Inhaltsverzeichnis, Vergrößern, Üben-Popup */
$$('.topic.v3').forEach(t => {
  $('.gobtn', t).onclick = () => { t.classList.toggle('full'); if (t.classList.contains('full')) $('.article', t).scrollIntoView({ behavior: 'smooth', block: 'start' }); };
  const art = $('.article', t), toc = $('.toc', art);
  const hs = $$('h3', art), n1 = hs.filter(h => !h.closest('.l-de')).length; if (n1 < 4) toc.remove();  // Inhaltsverzeichnis nur bei längeren Texten (zweisprachig: je Sprache zählen)
  hs.forEach((h, i) => { h.id = t.id + '-s' + i; if (n1 < 4) return; const a = document.createElement('a'); a.href = '#' + h.id; a.textContent = h.textContent; const sp = h.closest('.l-de, .l-en'); if (sp) a.className = sp.classList.contains('l-de') ? 'l-de' : 'l-en'; a.onclick = e => { e.preventDefault(); h.scrollIntoView({ behavior: 'smooth' }); }; toc.appendChild(a); });
});
$$('.zoom').forEach(z => z.onclick = () => { const f = z.closest('.figure'), on = !f.classList.contains('zoomed'); f.classList.toggle('zoomed', on); document.body.classList.toggle('nozoomscroll', on); z.textContent = on ? '✕ Schließen' : '⤢ Vergrößern'; });
document.addEventListener('keydown', e => { if (e.key === 'Escape') { const f = $('.figure.zoomed'); if (f) $('.zoom', f).click(); if ($('#quizModal.on')) closeQuiz(); } });
const QM = document.createElement('div'); QM.className = 'modal'; QM.id = 'quizModal';
QM.innerHTML = '<div class="mbox" role="dialog" aria-modal="true"><div class="mhead"><b id="qmT"></b><button class="qmclose" type="button">✕</button></div><div class="mprog"><i id="qmP"></i></div><div class="mbody" id="qmB"></div><div class="mnav"><button class="btn" id="qmPrev" type="button">← Zurück</button><span id="qmC" style="align-self:center;font-size:.85rem;color:var(--muted)"></span><button class="btn primary" id="qmNext" type="button">Weiter →</button></div></div>';
document.body.appendChild(QM);
let qmSrc = null, qmI = 0;
function qmShow(){ const qs = $$('.q', $('#qmB')); $('.mnav', QM).style.display = qs.length ? '' : 'none'; $('.mprog', QM).style.display = qs.length ? '' : 'none'; if (!qs.length) return; qs.forEach((q, i) => q.classList.toggle('cur', i === qmI)); $('#qmC').textContent = `Frage ${qmI + 1} von ${qs.length}`; $('#qmP').style.width = ((qmI + 1) / qs.length * 100) + '%'; $('#qmPrev').disabled = qmI === 0; $('#qmNext').textContent = qmI === qs.length - 1 ? 'Fertig ✓' : 'Weiter →'; }
function openQuiz(t){ qmSrc = $('.quizsrc', t); while (qmSrc.firstChild) $('#qmB').appendChild(qmSrc.firstChild); $('#qmT').textContent = 'Üben: ' + $('.t-title', t).childNodes[0].textContent; qmI = 0; qmShow(); QM.classList.add('on'); document.body.classList.add('nozoomscroll'); }
function closeQuiz(){ while ($('#qmB').firstChild) qmSrc.appendChild($('#qmB').firstChild); QM.classList.remove('on'); document.body.classList.remove('nozoomscroll'); }
$('.qmclose', QM).onclick = closeQuiz; QM.onclick = e => { if (e.target === QM) closeQuiz(); };
$('#qmPrev').onclick = () => { if (qmI > 0) { qmI--; qmShow(); } };
$('#qmNext').onclick = () => { const n = $$('.q', $('#qmB')).length; if (qmI < n - 1) { qmI++; qmShow(); } else closeQuiz(); };
$$('.topic.v3 .quizbtn').forEach(b => b.onclick = () => openQuiz(b.closest('.topic')));
/* Mini-Schaubilder: Vorschau ist eine stumme Kopie, das Original wandert ins Fenster und zurück */
const FM = document.createElement('div'); FM.className = 'modal'; FM.id = 'figModal';
FM.innerHTML = '<div class="mbox" role="dialog" aria-modal="true"><div class="mhead"><b id="fmT"></b><button class="qmclose" type="button">✕</button></div><div id="fmB"></div></div>';
document.body.appendChild(FM);
let fmSrc = null;
function closeFig(){ if (!fmSrc) return; while ($('#fmB').firstChild) fmSrc.appendChild($('#fmB').firstChild); FM.classList.remove('on'); document.body.classList.remove('nozoomscroll'); fmSrc = null; }
$$('.mfig').forEach(m => {
  const body = $('.mfig-body', m), svg = $('svg', body);
  if (svg) setTimeout(() => { const c = svg.cloneNode(true); c.removeAttribute('id'); c.style.minWidth = ''; $$('[id]', c).forEach(x => x.removeAttribute('id')); $('.mfig-prev', m).appendChild(c); }, 0);  // erst nach dem Zeichnen kopieren
  $('.mfig-btn', m).onclick = () => { fmSrc = body; $('#fmT').textContent = $('.mfig-t', body).textContent; $$('.mfig-t', body).forEach(t => t.hidden = true); while (body.firstChild) $('#fmB').appendChild(body.firstChild); FM.classList.add('on'); document.body.classList.add('nozoomscroll'); fitSvgs(); };
});
const tipAn = t => { const box = t.closest('#fmB, .figure, .mfig-body'); const root = t.closest('#fmB') || t.closest('.mfig-body') || box; const out = root && $('.mtip', root); if (!out) return; $$('.tp.on', root).forEach(x => x.classList.remove('on')); t.classList.add('on'); out.innerHTML = t.dataset.tip; out.scrollIntoView({block: 'nearest', behavior: 'smooth'}); };
document.addEventListener('click', e => { const t = e.target.closest('.tp'); if (t) tipAn(t); });
document.addEventListener('keydown', e => { const t = e.target.closest && e.target.closest('.tp'); if (t && (e.key === 'Enter' || e.key === ' ')) { e.preventDefault(); tipAn(t); } });
$('.qmclose', FM).onclick = closeFig; FM.onclick = e => { if (e.target === FM) closeFig(); };
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeFig(); });

/* Vertiefen-Reiter */
$$('.deep').forEach(d => {
  const btns = $$('.dtabs button', d), panes = $$('.pane', d);
  btns.forEach((b, i) => b.onclick = () => { btns.forEach(x => x.classList.toggle('on', x === b)); panes.forEach((p, j) => p.classList.toggle('on', i === j)); });
});

/* Üben */
$$('.q .rev').forEach(b => b.onclick = () => b.closest('.q').classList.toggle('show'));
/* Zahleneingabe: 1.234,5 · 1234,5 · 1234.5 · −300 · 30 % */
function parseNum(raw){
  let x = raw.trim().replace(/[−–]/g, '-').replace(/[%€\s]/g, '');
  if (x.includes(',')) x = x.replace(/\./g, '').replace(',', '.');
  else if (/^-?\d{1,3}(\.\d{3})+$/.test(x)) x = x.replace(/\./g, '');  // Punkt als Tausendertrenner
  return parseFloat(x);
}
$$('.q .chk').forEach(b => b.onclick = () => {
  const q = b.closest('.q'), v = parseNum($('input', q).value), a = parseFloat(q.dataset.ans);
  const tol = Math.max(parseFloat(q.dataset.tol || '0.05'), Math.abs(a) * 0.001), fb = $('.fb', q), u = q.dataset.unit || '';
  const ok = Math.abs(v - a) <= tol || (u.trim() === '%' && Math.abs(v * 100 - a) <= tol);  // 30 % darf auch als 0,3 kommen
  fb.className = 'fb ' + (ok ? 'r' : 'w');
  fb.innerHTML = ok ? '✓ Richtig!' + (q.dataset.why ? ' ' + q.dataset.why : '') : `✗ Nicht ganz. Richtig ist ${fmt(a)}${u}. ${q.dataset.why || ''}`;
});
$$('.q.mc').forEach(q => {
  const opts = $$('.opt', q), fb = $('.fb', q);
  opts.forEach((o, i) => o.onclick = () => {
    opts.forEach(x => x.classList.remove('right', 'wrong'));
    const ok = o.hasAttribute('data-ok');
    o.classList.add(ok ? 'right' : 'wrong');
    fb.className = 'fb ' + (ok ? 'r' : 'w');
    fb.innerHTML = (ok ? '✓ Richtig! ' : '✗ Leider nicht. ') + (q.dataset.why || '');
  });
});

/* Antippbare Schaubilder */
function bindHot(root){
  $$('.hot', root).forEach(g => g.addEventListener('click', () => {
    const f = g.closest('.figure'), tip = f && $('.tip', f); if (tip) tip.innerHTML = g.dataset.tip;
    if (f) $$('.hot.sel', f).forEach(x => x.classList.remove('sel')); g.classList.add('sel');  // angetippt bleibt markiert
  }));
}
bindHot(document);

/* Baum-/Kasten-Diagramme aus Daten: nodes {id,x,y,w,h,t,s,tip,k}, edges [[von,nach,label?],...] */
function drawTree(id, nodes, edges, opt = {}){
  const svg = document.getElementById(id); if (!svg) return;
  const N = {}; nodes.forEach(n => { n.w = n.w || 140; n.h = n.h || (n.s ? 44 : 32); N[n.id] = n; });
  let s = `<defs><marker id="${id}-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10z" style="fill:var(--axis)"/></marker></defs>`;
  edges.forEach(e => {
    const a = N[e[0]], b = N[e[1]], o = e[3] || {};
    let d;
    if (o.side) { // waagrecht: rechte Kante -> linke Kante
      const y1 = a.y + a.h / 2, y2 = b.y + b.h / 2, x1 = a.x + a.w / 2, x2 = b.x - b.w / 2, xm = (x1 + x2) / 2;
      d = `M${x1} ${y1} H${xm} V${y2} H${x2}`;
    } else {
      const x1 = a.x, y1 = a.y + a.h, x2 = b.x, y2 = b.y, ym = y1 + (y2 - y1) / 2;
      d = `M${x1} ${y1} V${ym} H${x2} V${y2}`;
    }
    s += `<path d="${d}" style="fill:none;stroke:var(--axis)" stroke-width="1.3"${opt.arrows || o.arrow ? ` marker-end="url(#${id}-a)"` : ''}${o.dash ? ' stroke-dasharray="4 3"' : ''}/>`;
    if (e[2]) { const mx = (a.x + b.x) / 2, my = (a.y + a.h + b.y) / 2; s += `<text x="${mx + 4}" y="${my - 3}" font-size="10" style="fill:var(--muted)">${e[2]}</text>`; }
  });
  nodes.forEach(n => {
    const k = n.k || '', x = n.x - n.w / 2;
    const fill = k === 'hl' ? 'var(--primary)' : k === 'soft' ? 'var(--pale)' : k === 'pos' ? 'var(--pos-bg)' : k === 'neg' ? 'var(--neg-bg)' : k === 'mid' ? 'var(--mid-bg)' : 'var(--card)';
    const stroke = k === 'hl' ? 'var(--primary)' : k === 'pos' ? 'var(--pos)' : k === 'neg' ? 'var(--neg)' : k === 'mid' ? 'var(--mid)' : 'var(--axis2)';
    const tc = k === 'hl' ? 'var(--on-primary)' : 'var(--ink)', sc = k === 'hl' ? 'var(--on-primary)' : 'var(--muted)';
    const lines = String(n.t).split('|');
    const lh = 15, total = lines.length * lh + (n.s ? 13 : 0);
    let ty = n.y + n.h / 2 - total / 2 + 11;
    let txt = lines.map((l, i) => `<text x="${n.x}" y="${ty + i * lh}" text-anchor="middle" font-size="${n.fs || 13}" font-weight="700" style="fill:${tc}">${l}</text>`).join('');
    if (n.s) txt += `<text x="${n.x}" y="${ty + lines.length * lh}" text-anchor="middle" font-size="10.5" style="fill:${sc}">${n.s}</text>`;
    s += `<g${n.tip ? ` class="hot" data-tip="${n.tip.replace(/"/g, '&quot;')}"` : ''}><rect x="${x}" y="${n.y}" width="${n.w}" height="${n.h}" rx="9" style="fill:${fill};stroke:${stroke}"${n.dash ? ' stroke-dasharray="4 3"' : ''}/>${txt}</g>`;
  });
  svg.innerHTML = s + (opt.extra || '');
  bindHot(svg);
}

/* kleine SVG-Hilfe */
function svgAxes(o){
  // o: {L,R,T,B,xmin,xmax,ymin,ymax,xt:[...],yt:[...],xl,yl,xf,yf}
  const X = v => o.L + (v - o.xmin) / (o.xmax - o.xmin) * (o.R - o.L);
  const Y = v => o.B - (v - o.ymin) / (o.ymax - o.ymin) * (o.B - o.T);
  let s = '';
  (o.yt || []).forEach(v => { s += `<line x1="${o.L}" x2="${o.R}" y1="${Y(v)}" y2="${Y(v)}" style="stroke:var(${v === 0 ? '--axis' : '--grid'})"/><text x="${o.L - 6}" y="${Y(v) + 4}" font-size="${o.fs || 10}" text-anchor="end" style="fill:var(--muted)">${o.yf ? o.yf(v) : fmt(v)}</text>`; });
  (o.xt || []).forEach(v => { s += `<text x="${X(v)}" y="${o.B + 15}" font-size="${o.fs || 10}" text-anchor="middle" style="fill:var(--muted)">${o.xf ? o.xf(v) : fmt(v)}</text>`; });
  s += `<line x1="${o.L}" y1="${o.B}" x2="${o.R}" y2="${o.B}" style="stroke:var(--axis)"/><line x1="${o.L}" y1="${o.T}" x2="${o.L}" y2="${o.B}" style="stroke:var(--axis)"/>`;
  if (o.xl) s += `<text x="${o.R}" y="${o.B + 30}" font-size="${o.fs || 10.5}" text-anchor="end" style="fill:var(--muted)">${o.xl}</text>`;
  if (o.yl) s += `<text x="${o.L - 4}" y="${o.T - 6}" font-size="${o.fs || 10.5}" style="fill:var(--muted)">${o.yl}</text>`;
  return { s, X, Y };
}
