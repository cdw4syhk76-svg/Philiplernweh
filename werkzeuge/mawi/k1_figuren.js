/* Lagerkosten-Rechner: Ø Lagerwert, Lagerkostensatz, Planungsperiode → K_L */
(function () {
  const W = document.getElementById('lkW'); if (!W) return;
  const S = document.getElementById('lkS'), P = document.getElementById('lkT');
  const set = (id, t) => { const e = document.getElementById(id); if (e) e.textContent = t; };
  function draw() {
    const w = +W.value, s = +S.value, m = +P.value, t = m / 12, k = w * 1e6 * t * s / 100;
    set('lkW-o', fmt(w, 1) + ' Mio. €'); set('lkS-o', fmt(s, 0) + ' % pro Jahr'); set('lkT-o', fmt(m, 0) + ' Monate');
    set('lkA', 'T = ' + fmt(t, 2)); set('lkAt', m + ' Monate = ' + fmt(t, 2) + ' Jahre');
    set('lkB', fmt(w, 1) + ' · ' + fmt(t, 2) + ' · ' + fmt(s / 100, 2)); set('lkBt', 'Ø Lagerwert (Mio. €) · T · k_L');
    set('lkC', fmt(k, 0) + ' €'); set('lkCt', 'Kosten der Lagerung in ' + m + ' Monaten');
  }
  [W, S, P].forEach(e => e.addEventListener('input', draw)); draw();
})();
