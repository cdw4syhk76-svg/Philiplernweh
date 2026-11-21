
/* ===== Mathe: gemeinsamer Plot-Helfer für alle Kapitel ===== */
const MP = {
  plot(id, o){
    const svg = document.getElementById(id); if (!svg) return null;
    const A = svgAxes(Object.assign({ L: 52, R: 625, T: 16, B: 222 }, o));
    let s = A.s, X = A.X, Y = A.Y;
    const cl = v => Math.max(o.ymin, Math.min(o.ymax, v));
    (o.fill || []).forEach(f => { const p = []; for (let k = 0; k <= 120; k++) { const x = f.a + (f.b - f.a) * k / 120; p.push(`${X(x)},${Y(cl(f.f(x)))}`); } s += `<polygon points="${X(f.a)},${Y(cl(f.base || 0))} ${p.join(' ')} ${X(f.b)},${Y(cl(f.base || 0))}" style="fill:var(${f.c || '--c1'});opacity:${f.op || .18}"/>`; });
    (o.hl || []).forEach(h => { s += `<line x1="${X(o.xmin)}" x2="${X(o.xmax)}" y1="${Y(h.y)}" y2="${Y(h.y)}" style="stroke:var(${h.c || '--axis2'})" stroke-dasharray="5 4"/>` + (h.t ? `<text x="${X(o.xmax) - 4}" y="${Y(h.y) - 5}" font-size="${o.fs || 11}" text-anchor="end" style="fill:var(${h.c || '--muted'})">${h.t}</text>` : ''); });
    (o.vl || []).forEach(h => { s += `<line x1="${X(h.x)}" x2="${X(h.x)}" y1="${o.T || 16}" y2="${o.B || 222}" style="stroke:var(${h.c || '--axis2'})" stroke-dasharray="5 4"/>` + (h.t ? `<text x="${X(h.x) + 4}" y="${(o.T || 16) + 12}" font-size="${o.fs || 11}" style="fill:var(${h.c || '--muted'})">${h.t}</text>` : ''); });
    (o.f || []).forEach(f => { let d = '', pen = false; const a = f.a ?? o.xmin, b = f.b ?? o.xmax; for (let k = 0; k <= 240; k++) { const x = a + (b - a) * k / 240, y = f.f(x); if (!isFinite(y) || y < o.ymin - 1e-9 || y > o.ymax + 1e-9) { pen = false; continue; } d += (pen ? 'L' : 'M') + X(x).toFixed(1) + ' ' + Y(cl(y)).toFixed(1); pen = true; }
      s += `<path d="${d}" style="fill:none;stroke:var(${f.c || '--primary'})" stroke-width="${f.w || 2.6}"${f.dash ? ' stroke-dasharray="6 4"' : ''}/>`; if (f.t) { const xt = f.tx ?? b; s += `<text x="${X(xt) - 4}" y="${Y(cl(f.f(xt))) - 7}" font-size="12" text-anchor="end" font-weight="700" style="fill:var(${f.c || '--primary'})">${f.t}</text>`; } });
    (o.p || []).forEach(q => { s += `<circle cx="${X(q.x)}" cy="${Y(cl(q.y))}" r="${q.r || 5.5}" style="fill:var(${q.c || '--mid'})"/>` + (q.t ? `<text x="${X(q.x) + (q.dx ?? 8)}" y="${Y(cl(q.y)) + (q.dy ?? -8)}" font-size="12" font-weight="700" text-anchor="${q.anchor || 'start'}" style="fill:var(${q.c || '--mid'})">${q.t}</text>` : ''); });
    svg.innerHTML = s + (o.extra ? o.extra(X, Y) : ''); return { X, Y };
  },
  set(id, v, t){ const e = document.getElementById(id); if (e) e.innerHTML = v; const f = document.getElementById(id + 't'); if (f && t != null) f.innerHTML = t; },
  on(ids, fn){ ids.forEach(i => { const e = document.getElementById(i); if (e) e.addEventListener('input', fn); }); NEU.push(fn); fn(); },
  v: id => +document.getElementById(id).value
};


/* Mathe-Helfer für alle Schaubilder */
const phi = x => Math.exp(-x * x / 2) / Math.sqrt(2 * Math.PI);
const Phi = x => { const t = 1 / (1 + 0.2316419 * Math.abs(x)), d = phi(x), p = d * t * (0.31938153 + t * (-0.356563782 + t * (1.781477937 + t * (-1.821255978 + t * 1.330274429)))); return x >= 0 ? 1 - p : p; };
const binom = (n, p) => { const r = []; let c = Math.pow(1 - p, n); r.push(c); for (let k = 1; k <= n; k++) { c = c * (n - k + 1) / k * p / (1 - p); r.push(c); } return r; };
/* Umschalter-Knöpfe (<div class="rules" id=…> mit <button data-k>): fn(k) beim Klick und einmal am Anfang */
function UM(id, fn){ const bs = document.querySelectorAll('#' + id + ' button'); const set = b => { bs.forEach(x => x.classList.toggle('on', x === b)); fn(+b.dataset.k); }; bs.forEach(b => b.addEventListener('click', () => set(b))); const on = document.querySelector('#' + id + ' button.on') || bs[0]; if (on) { set(on); NEU.push(() => set(document.querySelector('#' + id + ' button.on') || bs[0])); } }
/* Sprache: LG(en, de) wählt den Text; NEU = Zeichenfunktionen, die beim Sprachwechsel neu laufen */
const NEU = [];
function LG(en, de){ return (window.LANG && window.LANG() === 'de') ? de : en; }
const ZWS = (en, de) => en + ' · ' + de;

/* Sortier-Schaubilder */
document.querySelectorAll('.sortier').forEach(root => {
  const tiles = [...root.querySelectorAll('.so-t')], bas = [...root.querySelectorAll('.so-k .so-in')], out = root.querySelector('.so-out');
  const lege = t => { if (t.classList.contains('done')) return; t.classList.add('done'); const c = document.createElement('div'); c.className = 'so-chip'; c.textContent = t.textContent; bas[+t.dataset.k].appendChild(c); };
  const zeige = t => { tiles.forEach(x => x.classList.toggle('cur', x === t)); out.innerHTML = t.dataset.why; };
  tiles.forEach(t => t.addEventListener('click', () => { lege(t); zeige(t); }));
  root.querySelector('[data-all]').onclick = () => { tiles.forEach(lege); out.innerHTML = 'Alle einsortiert · all sorted.'; };
  root.querySelector('[data-reset]').onclick = () => { tiles.forEach(t => t.classList.remove('done', 'cur')); bas.forEach(b => b.innerHTML = ''); out.innerHTML = out.dataset.start; };
});

/* SVG-Bausteine für Schaubilder, die das JS zeichnet (Gegenstücke zu box/matrix2 in Python) */
function KS(x, y, w, h, t, s, o = {}){
  const f = o.fill || (o.on ? 'var(--primary)' : 'var(--pale)'), ink = o.on ? 'var(--on-primary)' : 'var(--ink)', sub = o.on ? 'var(--on-primary)' : 'var(--muted)';
  const sp = (txt, n) => { if (!txt || txt.length <= n || txt.indexOf(' ') < 0) return [txt || '']; let b = 0, d = 1e9; for (let i = 0; i < txt.length; i++) if (txt[i] === ' ' && Math.abs(i - txt.length / 2) < d) { d = Math.abs(i - txt.length / 2); b = i; } return [txt.slice(0, b), txt.slice(b + 1)]; };
  const L = sp(t, Math.max(10, w / 7.6 | 0)).map(z => [z, o.size || 13, 700, ink]).concat(s ? sp(s, Math.max(12, w / 6.2 | 0)).map(z => [z, o.sub || 11, 400, sub]) : []);
  let yy = y + (h - L.reduce((a, l) => a + l[1] + 3, 0)) / 2 + 11, g = `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="9" style="fill:${f};stroke:${o.stroke || 'var(--primary-2)'}" stroke-width="1.2"${o.dash ? ' stroke-dasharray="5 4"' : ''}/>`;
  L.forEach(l => { g += `<text x="${x + w / 2}" y="${yy}" font-size="${l[1]}" font-weight="${l[2]}" text-anchor="middle" style="fill:${l[3]}">${l[0]}</text>`; yy += l[1] + 3; });
  return g;
}
const TXS = (x, y, t, size = 12, w = 400, fill = 'var(--ink)', anchor = 'middle') => `<text x="${x}" y="${y}" font-size="${size}" font-weight="${w}" text-anchor="${anchor}" style="fill:${fill}">${t}</text>`;
const ARDEFS = id => '<defs>' + ['c1', 'c3', 'axis2', 'primary', 'neg', 'pos', 'mid', 'ink'].map(c => `<marker id="${id}-${c}" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8z" style="fill:var(--${c})"/></marker>`).join('') + '</defs>';
const ARS = (id, x1, y1, x2, y2, c = 'axis2', w = 1.8, dash = false) => `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" style="stroke:var(--${c})" stroke-width="${w}"${dash ? ' stroke-dasharray="5 4"' : ''} marker-end="url(#${id}-${c})"/>`;
function M2S(xlab, ylab, xt, yt, cells, hl = [], W = 640, H = 300){
  const L = 100, T = 14, cw = (W - 130) / 2, ch = (H - 70) / 2;
  const pos = [[L, T], [L + cw, T], [L, T + ch], [L + cw, T + ch]];
  let o = '';
  cells.forEach((c, i) => { o += KS(pos[i][0] + 4, pos[i][1] + 4, cw - 8, ch - 8, c[0], c[1], { on: hl.includes(i), size: 14, fill: c[2] }); });
  o += `<path d="M${L} ${T}V${T + 2 * ch}H${L + 2 * cw + 8}" style="fill:none;stroke:var(--axis)" stroke-width="1.6"/>`;
  o += TXS(L + cw / 2, T + 2 * ch + 18, xt[0], 12, 600, 'var(--muted)') + TXS(L + 1.5 * cw, T + 2 * ch + 18, xt[1], 12, 600, 'var(--muted)') + TXS(L + cw, T + 2 * ch + 38, xlab, 13, 700);
  o += TXS(L - 10, T + 1.5 * ch + 4, yt[0], 12, 600, 'var(--muted)', 'end') + TXS(L - 10, T + ch / 2 + 4, yt[1], 12, 600, 'var(--muted)', 'end');
  o += `<text x="18" y="${T + ch}" font-size="13" font-weight="700" text-anchor="middle" transform="rotate(-90 18 ${T + ch})" style="fill:var(--ink)">${ylab}</text>`;
  return o;
}
