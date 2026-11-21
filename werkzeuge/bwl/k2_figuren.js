/* Break-even-Rechner: Preis, variable Kosten, Fixkosten → Ertrags- und Aufwandsgerade */
(function () {
  const P = document.getElementById('beP'); if (!P) return;
  const V = document.getElementById('beV'), F = document.getElementById('beF');
  function draw() {
    const p = +P.value, v = +V.value, f = +F.value, d = p - v, xbe = f / d;
    const XM = 3000, YM = 120000, X = x => 52 + x / XM * 290, Y = y => 222 - y / YM * 200;
    let g = BW.achsen(52, 222, 350, 12, '', '€') + BW.t(350, 212, 'Stück', { a: 'end', f: 'var(--muted)', size: 12 });
    [1000, 2000].forEach(k => { g += BW.l(X(k), 222, X(k), 227) + BW.t(X(k), 242, BW.ganz(k), { size: 12, w: 400 }); });
    [40000, 80000, 120000].forEach(k => { g += BW.l(47, Y(k), 52, Y(k)) + BW.t(44, Y(k) + 4, fmt(k / 1000, 0) + 'T', { size: 12, w: 400, a: 'end' }); });
    if (xbe <= XM) g += `<polygon points="${X(xbe)},${Y(p * xbe)} ${X(XM)},${Y(p * XM)} ${X(XM)},${Y(v * XM + f)}" style="fill:var(--pos);opacity:.18"/>`;
    g += `<polygon points="${X(0)},${Y(0)} ${X(0)},${Y(f)} ${X(Math.min(xbe, XM))},${Y(v * Math.min(xbe, XM) + f)} ${X(Math.min(xbe, XM))},${Y(p * Math.min(xbe, XM))}" style="fill:var(--neg);opacity:.14"/>`;
    g += BW.l(X(0), Y(f), X(XM), Y(f), 'var(--axis)', 1.2, true) + BW.t(X(XM) - 2, Y(f) - 6, 'Fixkosten', { size: 12, a: 'end', f: 'var(--muted)' });
    g += BW.pl([[X(0), Y(f)], [X(XM), Y(v * XM + f)]], 'var(--c3)') + BW.pl([[X(0), Y(0)], [X(Math.min(XM, YM / p)), Y(p * Math.min(XM, YM / p))]], 'var(--c2)');
    g += BW.t(X(Math.min(XM, YM / p)) - 4, Y(p * Math.min(XM, YM / p)) + 16, 'E(x)', { a: 'end', f: 'var(--c2)', w: 800 }) + BW.t(X(XM) - 2, Y(v * XM + f) + 18, 'A(x)', { a: 'end', f: 'var(--c3)', w: 800 });
    if (xbe <= XM) {
      g += BW.l(X(xbe), Y(p * xbe), X(xbe), 222, 'var(--primary)', 1.4, true) + BW.dot(X(xbe), Y(p * xbe), 'var(--primary)', 6.5);
      g += BW.t(X(xbe) + 12, Y(p * xbe) + 22, 'Break-even', { a: 'start', f: 'var(--primary)', w: 800 });
      g += BW.t(X(xbe), 258, fmt(xbe, 0) + ' Stück', { f: 'var(--primary)', w: 800, size: 12 });
    } else g += BW.t(200, 40, 'Break-even liegt außerhalb des Bildes', { f: 'var(--neg)' });
    g += BW.t(X(400), Y(4000) - 4, 'Verlust', { size: 12, f: 'var(--neg)', w: 700, a: 'start' });
    if (xbe < 2400) g += BW.t(X(2900), Y((p * 2900 + v * 2900 + f) / 2) + 4, 'Gewinn', { size: 12, f: 'var(--pos)', w: 700, a: 'end' });
    document.getElementById('figBE').innerHTML = g;
    BW.setz('beR1', BW.eur(d)); BW.setz('beT1', `Preis − variable Kosten: ${fmt(p, 0)} − ${fmt(v, 0)}. So viel trägt jedes Stück zu den Fixkosten bei.`);
    BW.setz('beR2', `G(x) = ${fmt(d, 0)}x − ${BW.ganz(f)}`); BW.setz('beT2', `E(x) = ${fmt(p, 0)}x minus A(x) = ${fmt(v, 0)}x + ${BW.ganz(f)}`);
    BW.setz('beR3', (Number.isInteger(xbe) ? fmt(xbe, 0) : fmt(xbe, 2)) + ' Stück'); BW.setz('beT3', `G(x) = 0: ${BW.ganz(f)} ÷ ${fmt(d, 0)}. Ertrag dort: ${BW.ganz(Math.round(xbe * p))} €.`);
  }
  [P, V, F].forEach(x => x.addEventListener('input', draw)); draw();
})();

/* Rentabilitätsrechner: Gewinn und Kapital → Prozent */
(function () {
  const G = document.getElementById('rtG'); if (!G) return;
  const K = document.getElementById('rtK');
  function draw() {
    const g = +G.value, k = +K.value, r = g / k * 100;
    BW.setz('rtR1', '<span style="font-size:.8em">Gewinn ÷ Kapital · 100 %</span>'); BW.setz('rtT1', 'Erfolgsgröße oben, Basisgröße unten');
    BW.setz('rtR2', `${BW.ganz(g)} ÷ ${BW.ganz(k)}`); BW.setz('rtT2', `= ${fmt(g / k, 4)}; mal 100 für Prozent`);
    BW.setz('rtR3', fmt(r, 2) + ' %'); BW.setz('rtT3', `Mit jedem eingesetzten Euro ${fmt(r, 2)} Cent Gewinn. Umgekehrt: Kapital = ${BW.ganz(g)} ÷ ${fmt(r / 100, 4)} = ${BW.ganz(k)} €.`);
  }
  [G, K].forEach(x => x.addEventListener('input', draw)); draw();
})();

/* Gewinnmaximum: p(x) = a − x/2, Kosten v·x + F → E, A, G; Hochpunkt und Gewinnschwellen */
(function () {
  const A = document.getElementById('gmA'); if (!A) return;
  const V = document.getElementById('gmV'), F = document.getElementById('gmF');
  function draw() {
    const a = +A.value, v = +V.value, f = +F.value, b = a - v;
    const E = x => a * x - x * x / 2, K = x => v * x + f, Gf = x => E(x) - K(x);
    const xs = b, gs = b * b / 2 - f, disk = b * b - 2 * f;
    const XM = 2 * a, YT = 55, YB = -14, X = x => 44 + x / XM * 300, Y = y => 20 + (YT - y) / (YT - YB) * 210;
    let g = BW.achsen(44, Y(0), 350, 12, 'x', '€') + BW.l(44, Y(0), 44, Y(YB));
    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20].filter(k => k < XM).forEach(k => { g += BW.l(X(k), Y(0) - 3, X(k), Y(0) + 3) + (k % 4 === 0 || XM <= 12 ? BW.t(X(k), Y(0) + 17, k, { size: 12, w: 400 }) : ''); });
    [20, 40].forEach(k => { g += BW.l(40, Y(k), 44, Y(k)) + BW.t(38, Y(k) + 4, k, { size: 12, w: 400, a: 'end' }); });
    g += BW.kurve(E, 0, XM, X, Y, 'var(--c2)') + BW.kurve(K, 0, Math.min(XM, (YT - f) / Math.max(v, .01)), X, Y, 'var(--c3)');
    const dd = b * b - 2 * (f + YB), ga = dd > 0 ? Math.max(0, b - Math.sqrt(dd)) : 0, gb = dd > 0 ? Math.min(XM, b + Math.sqrt(dd)) : XM;
    g += BW.kurve(Gf, ga, gb, X, Y, 'var(--primary)', 3);
    g += BW.t(X(a * .45) - 6, Y(E(a * .45)) - 8, 'E(x)', { f: 'var(--c2)', w: 800, a: 'end' }) + BW.t(X(XM) - 4, Y(Math.min(YT, K(XM))) + 18, 'K(x)', { f: 'var(--c3)', w: 800, a: 'end' });
    const xl = xs + .7 * (gb - xs); g += BW.t(X(xl) + 10, Y(Gf(xl)) + 4, 'G(x)', { f: 'var(--primary)', w: 800, a: 'start' });
    if (disk >= 0) { const x1 = b - Math.sqrt(disk), x2 = b + Math.sqrt(disk); [x1, x2].forEach(x => { if (x > 0) g += BW.dot(X(x), Y(0), 'var(--c3)', 4.5); }); }
    g += BW.l(X(xs), Y(gs), X(xs), Y(0), 'var(--primary)', 1.3, true) + BW.dot(X(xs), Y(gs), 'var(--primary)', 6.5);
    g += BW.t(X(xs), Y(gs) - 12, 'max. Gewinn', { f: 'var(--primary)', w: 800 });
    document.getElementById('figGM').innerHTML = g;
    const s = n => (n < 0 ? '− ' : '+ ') + fmt(Math.abs(n), 2);
    BW.setz('gmR1', `<span style="font-size:.78em">G(x) = −½x² ${s(b)}x ${s(-f)}</span>`); BW.setz('gmT1', `E(x) = (${fmt(a, 2)} − x/2)·x minus K(x) = ${fmt(v, 2)}x + ${fmt(f, 0)}`);
    BW.setz('gmR2', `x = ${fmt(xs, 2)}`); BW.setz('gmT2', `G'(x) = −x ${s(b)} = 0. G''(x) = −1 < 0: Hochpunkt.`);
    BW.setz('gmR3', BW.eur(gs)); BW.setz('gmT3', (gs < 0 ? 'Selbst im Maximum Verlust: Das lohnt sich nie. ' : '') + `Preis p = ${fmt(a - xs / 2, 2)} €, Umsatz E = ${BW.eur(E(xs))}` + (disk >= 0 && gs >= 0 ? `. Gewinnschwellen bei x = ${fmt(b - Math.sqrt(disk), 2)} und ${fmt(b + Math.sqrt(disk), 2)}.` : '.'));
  }
  [A, V, F].forEach(x => x.addEventListener('input', draw)); draw();
})();
