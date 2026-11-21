/* Robinson Crusoe: 12 Stunden zwischen Jagd und Wasser verteilen; Fortschritt (Falle) dreht die Grenze */
(function () {
  const H = document.getElementById('robH'); if (!H) return;
  const Fo = document.getElementById('robF');
  function draw() {
    const h = +H.value, s = +Fo.value, w = 10, schw = s * h / 12, wass = w * (12 - h) / 12;
    const X = l => 50 + l / 10 * 290, Y = k => 214 - k / 10 * 190;
    let g = BW.achsen(50, 214, 352, 12, '', 'Wildschweine') + BW.t(352, 250, 'Wasser (Liter)', { a: 'end', f: 'var(--muted)', size: 12 });
    [2, 4, 6, 8, 10].forEach(k => { g += BW.l(X(k), 214, X(k), 218) + BW.t(X(k), 232, k, { size: 12, w: 400 }) + BW.l(46, Y(k), 50, Y(k)) + BW.t(42, Y(k) + 4, k, { size: 12, w: 400, a: 'end' }); });
    if (s > 5) g += BW.pl([[X(0), Y(5)], [X(10), Y(0)]], 'var(--axis)', 2, true) + BW.t(X(3.2), Y(3.4) + 18, 'vorher', { size: 12, f: 'var(--muted)', a: 'end' });
    g += `<polygon points="${X(0)},${Y(0)} ${X(0)},${Y(s)} ${X(10)},${Y(0)}" style="fill:var(--pale);opacity:.9"/>`;
    g += BW.pl([[X(0), Y(s)], [X(10), Y(0)]], 'var(--primary)', 3);
    g += BW.t(X(1.4), Y(.8), 'möglich', { size: 13, w: 700, f: 'var(--muted)' }) + BW.t(X(8.2), Y(8.6), 'unmöglich', { size: 13, w: 700, f: 'var(--neg)' });
    g += BW.l(X(wass), Y(schw), X(wass), 214, 'var(--c3)', 1.2, true) + BW.l(50, Y(schw), X(wass), Y(schw), 'var(--c3)', 1.2, true) + BW.dot(X(wass), Y(schw), 'var(--c3)', 7);
    g += BW.t(X(wass) + 12, Y(schw) - 14, `${fmt(schw, 1)} Schweine · ${fmt(wass, 1)} l`, { a: wass > 5 ? 'end' : 'start', f: 'var(--c3)', w: 800 });
    document.getElementById('figROB').innerHTML = g;
    BW.setz('robR1', fmt(schw, 2) + ' Wildschweine'); BW.setz('robT1', `${h} h · ${s} ÷ 12 h`);
    BW.setz('robR2', fmt(wass, 2) + ' Liter'); BW.setz('robT2', `${12 - h} h · 10 ÷ 12 h`);
    BW.setz('robR3', `1 Schwein = ${fmt(10 / s, 2)} l`); BW.setz('robT3', `1 Liter Wasser = ${fmt(s / 10, 2)} Wildschweine. ` + (s > 5 ? 'Mit der Falle ist ein Schwein „billiger“ geworden.' : 'Wer jagt, verzichtet auf Wasser.'));
  }
  [H, Fo].forEach(x => x.addEventListener('input', draw)); draw();
})();
