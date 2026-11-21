/* Mittelwertmethode: zwei Punkte (p1, M1) und (p2, M2) */
(function () {
  const P1 = document.getElementById('mwP1'); if (!P1) return;
  const P2 = document.getElementById('mwP2'), M1 = document.getElementById('mwM1'), M2 = document.getElementById('mwM2');
  function draw() {
    const p1 = +P1.value, p2 = +P2.value, m1 = +M1.value, m2 = +M2.value;
    const X = m => 48 + m / 200 * 296, Y = p => 196 - p / 20 * 176;
    let g = BW.achsen(48, 196, 350, 12, 'Menge', 'Preis');
    [50, 100, 150].forEach(k => { g += BW.l(X(k), 196, X(k), 200) + BW.t(X(k), 214, k, { size: 12, w: 400 }); });
    [5, 10, 15].forEach(k => { g += BW.l(44, Y(k), 48, Y(k)) + BW.t(40, Y(k) + 4, k, { size: 12, w: 400, a: 'end' }); });
    g += BW.pl([[X(m1), Y(p1)], [X(m2), Y(p2)]], 'var(--primary)', 2.5, true);
    g += BW.l(X(m1), Y(p1), X(m1), 196, 'var(--axis)', 1, true) + BW.l(48, Y(p1), X(m1), Y(p1), 'var(--axis)', 1, true);
    g += BW.l(X(m2), Y(p2), X(m2), 196, 'var(--axis)', 1, true) + BW.l(48, Y(p2), X(m2), Y(p2), 'var(--axis)', 1, true);
    g += BW.dot(X(m1), Y(p1), 'var(--c3)', 6.5) + BW.dot(X(m2), Y(p2), 'var(--primary)', 6.5);
    g += BW.t(X(m1) + 9, Y(p1) - 9, 'vorher', { a: 'start', f: 'var(--c3)', w: 800 }) + BW.t(X(m2) + 9, Y(p2) + 18, 'nachher', { a: 'start', f: 'var(--primary)', w: 800 });
    document.getElementById('figMW').innerHTML = g;
    const dm = (m2 - m1) / ((m2 + m1) / 2), dp = (p2 - p1) / ((p2 + p1) / 2);
    BW.setz('mwR1', fmt(dm * 100, 2) + ' %'); BW.setz('mwT1', `(${fmt(m2, 0)} − ${fmt(m1, 0)}) ÷ ${fmt((m1 + m2) / 2, 1)}`);
    BW.setz('mwR2', fmt(dp * 100, 2) + ' %'); BW.setz('mwT2', `(${fmt(p2, 2)} − ${fmt(p1, 2)}) ÷ ${fmt((p1 + p2) / 2, 2)}`);
    if (Math.abs(dp) < 1e-9) { BW.setz('mwR3', '–'); BW.setz('mwT3', 'Der Preis hat sich nicht geändert.'); return; }
    const e = Math.abs(dm / dp), art = Math.abs(e - 1) < .005 ? 'einheitselastisch' : e > 1 ? 'elastisch' : 'unelastisch';
    BW.setz('mwR3', 'ε = ' + fmt(e, 2)); BW.setz('mwT3', `${art}: Ändert sich der Preis um 1 %, ändert sich die Nachfrage um ${fmt(e, 2)} %.`);
  }
  [P1, P2, M1, M2].forEach(x => x.addEventListener('input', draw)); draw();
})();

/* Punktelastizität auf der Nachfragegeraden D(p) = a − b·p */
(function () {
  const A = document.getElementById('peA'); if (!A) return;
  const B = document.getElementById('peB'), P = document.getElementById('peP');
  function draw() {
    const a = +A.value, b = +B.value, pmax = a / b; if (+P.max !== Math.floor(pmax * 2) / 2 - .5) P.max = Math.max(1, Math.floor(pmax * 2) / 2 - .5);
    const p = Math.min(+P.value, +P.max), q = a - b * p, e = b * p / q;
    BW.setz('peP-o', fmt(p, 2) + ' €');
    const X = m => 48 + m / 200 * 296, Y = pr => 206 - pr / 40 * 186;
    let g = BW.achsen(48, 206, 350, 12, 'Menge Q', 'Preis p');
    [50, 100, 150].forEach(k => { g += BW.l(X(k), 206, X(k), 210) + BW.t(X(k), 224, k, { size: 12, w: 400 }); });
    [10, 20, 30].forEach(k => { g += BW.l(44, Y(k), 48, Y(k)) + BW.t(40, Y(k) + 4, k, { size: 12, w: 400, a: 'end' }); });
    const pm = pmax / 2;
    const pt = Math.min(pmax, 40); g += BW.pl([[X(a - b * pt), Y(pt)], [X(a), Y(0)]], 'var(--primary)', 3);
    if (pm < 40) g += BW.dot(X(a - b * pm), Y(pm), 'var(--axis)', 4) + BW.t(X(a - b * pm) + 8, Y(pm) - 8, 'ε = 1', { a: 'start', size: 12, f: 'var(--muted)' });
    g += BW.l(X(q), Y(p), X(q), 206, 'var(--c3)', 1.2, true) + BW.l(48, Y(p), X(q), Y(p), 'var(--c3)', 1.2, true) + BW.dot(X(q), Y(p), 'var(--c3)', 7);
    g += BW.t(X(q) + 10, Y(p) + 4, `(${fmt(q, 1)} | ${fmt(p, 2)})`, { a: 'start', f: 'var(--c3)', w: 800 });
    g += BW.t(200, 246, e > 1.005 ? 'oberer Teil: elastisch' : e < .995 ? 'unterer Teil: unelastisch' : 'Mitte: einheitselastisch', { size: 13, w: 700, f: 'var(--muted)' });
    document.getElementById('figPE').innerHTML = g;
    BW.setz('peR1', `D'(p) = −${fmt(b, 2)}`); BW.setz('peT1', `D(p) = ${fmt(a, 0)} − ${fmt(b, 2)}p, nach p abgeleitet`);
    BW.setz('peR2', `Q = ${fmt(q, 2)}`); BW.setz('peT2', `${fmt(a, 0)} − ${fmt(b, 2)} · ${fmt(p, 2)}`);
    BW.setz('peR3', 'ε = ' + fmt(e, 2)); BW.setz('peT3', `|−${fmt(b, 2)} · ${fmt(p, 2)} ÷ ${fmt(q, 2)}|: ${e > 1.005 ? 'elastisch' : e < .995 ? 'unelastisch' : 'einheitselastisch'}. Preis +1 % → Nachfrage −${fmt(e, 2)} %.`);
  }
  [A, B, P].forEach(x => x.addEventListener('input', draw)); draw();
})();

/* Preis-, Mengen-, Gesamteffekt mit D(p) = 1000 − 200p (Folienbeispiel) */
(function () {
  const P1 = document.getElementById('efP1'); if (!P1) return;
  const P2 = document.getElementById('efP2');
  function draw() {
    const pa = +P1.value, pn = +P2.value, D = p => 1000 - 200 * p, ma = D(pa), mn = D(pn);
    const X = m => 48 + m / 800 * 296, Y = p => 214 - p / 6 * 196;
    let g = BW.achsen(48, 214, 350, 12, 'Menge', 'Preis');
    [200, 400, 600].forEach(k => { g += BW.l(X(k), 214, X(k), 218) + BW.t(X(k), 232, k, { size: 12, w: 400 }); });
    [2, 4].forEach(k => { g += BW.l(44, Y(k), 48, Y(k)) + BW.t(40, Y(k) + 4, k, { size: 12, w: 400, a: 'end' }); });
    const lo = Math.min(pa, pn), hi = Math.max(pa, pn);
    // Preiseffekt: Streifen zwischen den Preisen über der alten Menge
    g += `<rect x="${X(0)}" y="${Y(hi)}" width="${X(ma) - X(0)}" height="${Y(lo) - Y(hi)}" style="fill:${pn < pa ? 'var(--neg)' : 'var(--pos)'};opacity:.35"/>`;
    // Mengeneffekt: zwischen alter und neuer Menge, Höhe neuer Preis
    g += `<rect x="${X(Math.min(ma, mn))}" y="${Y(pn)}" width="${Math.abs(X(mn) - X(ma))}" height="${214 - Y(pn)}" style="fill:${mn > ma ? 'var(--pos)' : 'var(--neg)'};opacity:.35"/>`;
    g += BW.pl([[X(0), Y(5)], [X(800), Y(1)]], 'var(--primary)', 2.5) + BW.t(X(780), Y(1.1) - 10, 'NF', { a: 'end', f: 'var(--primary)', w: 800 });
    g += BW.dot(X(ma), Y(pa), 'var(--c3)', 6) + BW.dot(X(mn), Y(pn), 'var(--primary)', 6);
    g += BW.t(X(ma) + 8, Y(pa) - 8, 'alt', { a: 'start', f: 'var(--c3)', w: 800 }) + BW.t(X(mn) + 8, Y(pn) - 8, 'neu', { a: 'start', f: 'var(--primary)', w: 800 });
    g += BW.t(X(ma / 2), (Y(lo) + Y(hi)) / 2 + 5, 'PE', { w: 800 }) + BW.t((X(ma) + X(mn)) / 2, (Y(pn) + 214) / 2, 'ME', { w: 800 });
    const ME = (mn - ma) * pn, PE = (pn - pa) * ma, GE = pn * mn - pa * ma, e = Math.abs(((mn - ma) / ((mn + ma) / 2)) / ((pn - pa) / ((pn + pa) / 2) || 1e-9));
    g += BW.t(200, 258, pa === pn ? 'Preis unverändert' : `ε = ${fmt(e, 2)}: ${e > 1 ? 'elastisch' : e < 1 ? 'unelastisch' : 'einheitselastisch'}`, { size: 13, w: 700, f: 'var(--muted)' });
    document.getElementById('figEF').innerHTML = g;
    BW.setz('efR1', (ME >= 0 ? '+' : '−') + BW.eur(Math.abs(ME))); BW.setz('efT1', `(${fmt(mn, 0)} − ${fmt(ma, 0)}) · ${fmt(pn, 2)} €`);
    BW.setz('efR2', (PE >= 0 ? '+' : '−') + BW.eur(Math.abs(PE))); BW.setz('efT2', `(${fmt(pn, 2)} − ${fmt(pa, 2)}) · ${fmt(ma, 0)}`);
    BW.setz('efR3', (GE >= 0 ? '+' : '−') + BW.eur(Math.abs(GE))); BW.setz('efT3', `Erlös ${BW.eur(pn * mn)} statt ${BW.eur(pa * ma)}. ` + (GE > 0 ? 'Der Erlös steigt.' : GE < 0 ? 'Der Erlös sinkt.' : 'Der Erlös bleibt gleich.'));
  }
  [P1, P2].forEach(x => x.addEventListener('input', draw)); draw();
})();
