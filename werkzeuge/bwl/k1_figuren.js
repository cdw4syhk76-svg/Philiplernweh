/* ABWL: gemeinsame Zeichenhilfen für die Rechner (Theme-Farben, Schrift ≥ 12) */
const BW = {
  t: (x, y, s, o = {}) => `<text x="${x}" y="${y}" font-size="${o.size || 13}" font-weight="${o.w || 600}" text-anchor="${o.a || 'middle'}" style="fill:${o.f || 'var(--ink)'};paint-order:stroke;stroke:var(--card);stroke-width:${o.halo === 0 ? 0 : 3}px;stroke-linejoin:round">${s}</text>`,
  l: (x1, y1, x2, y2, f = 'var(--axis)', w = 1.4, dash = false) => `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" style="stroke:${f}" stroke-width="${w}"${dash ? ' stroke-dasharray="5 4"' : ''}/>`,
  pl: (pts, f = 'var(--primary)', w = 2.5, dash = false) => `<polyline points="${pts.map(p => p[0].toFixed(1) + ',' + p[1].toFixed(1)).join(' ')}" style="fill:none;stroke:${f}" stroke-width="${w}"${dash ? ' stroke-dasharray="6 4"' : ''}/>`,
  dot: (x, y, f = 'var(--primary)', r = 5.5) => `<circle cx="${x}" cy="${y}" r="${r}" style="fill:${f}"/>`,
  kurve: (fn, a, b, X, Y, f, w = 2.5, n = 80) => { const p = []; for (let i = 0; i <= n; i++) { const x = a + (b - a) * i / n; p.push([X(x), Y(fn(x))]); } return BW.pl(p, f, w); },
  achsen: (x0, y0, x1, y1, xl, yl) => BW.l(x0, y0, x1, y0) + BW.l(x0, y0, x0, y1) + `<path d="M${x1} ${y0}l-7 -4v8z M${x0} ${y1}l-4 7h8z" style="fill:var(--axis)"/>`
    + (xl ? BW.t(x1 - 4, y0 - 10, xl, { a: 'end', f: 'var(--muted)', size: 12 }) : '') + (yl ? BW.t(x0 + 6, y1 + 4, yl, { a: 'start', f: 'var(--muted)', size: 12 }) : ''),
  setz: (id, v) => { const e = document.getElementById(id); if (e) e.innerHTML = v; },
  eur: n => fmt(n, 2) + ' €',
  ganz: n => fmt(n, 0)
};
