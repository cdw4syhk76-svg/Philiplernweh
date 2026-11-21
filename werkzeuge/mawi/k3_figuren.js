/* Lagerkennzahlen-Rechner und Andler-Rechner */
(function () {
  const set = (id, t) => { const e = document.getElementById(id); if (e) e.textContent = t; };
  const A = document.getElementById('kzA');
  if (A) {
    const E = document.getElementById('kzE'), V = document.getElementById('kzV'), P = document.getElementById('kzP');
    const draw = () => {
      const a = +A.value, e = +E.value, v = +V.value, p = +P.value, d = (a + e) / 2;
      set('kzA-o', fmt(a, 0) + ' Stück'); set('kzE-o', fmt(e, 0) + ' Stück'); set('kzV-o', fmt(v, 0) + ' Stück'); set('kzP-o', fmt(p, 0) + ' €');
      set('kz1', fmt(d, 0)); set('kz1t', '(' + fmt(a, 0) + ' + ' + fmt(e, 0) + ') / 2');
      if (d <= 0) { set('kz2', '–'); set('kz2t', 'kein Bestand'); set('kz3', '–'); set('kz3t', ''); set('kz4', '0 €'); set('kz4t', ''); return; }
      set('kz2', fmt(v / d, 1) + '-mal'); set('kz2t', 'Jahresverbrauch / Ø Bestand');
      set('kz3', fmt(d * 365 / v, 1) + ' Tage'); set('kz3t', 'Ø Bestand · 365 / Jahresverbrauch');
      set('kz4', fmt(d * p, 0) + ' €'); set('kz4t', 'Ø Bestand · Einkaufspreis');
    };
    [A, E, V, P].forEach(x => x.addEventListener('input', draw)); draw();
  }
  const M = document.getElementById('anM');
  if (M) {
    const K = document.getElementById('anK'), W = document.getElementById('anW'), I = document.getElementById('anI');
    const draw = () => {
      const m = +M.value, kb = +K.value, w = +W.value, i = +I.value / 100;
      set('anM-o', fmt(m, 0) + ' t'); set('anK-o', fmt(kb, 0) + ' €'); set('anW-o', fmt(w, 0) + ' €/t'); set('anI-o', fmt(i * 100, 0) + ' %');
      const x = Math.sqrt(2 * m * kb / (w * i)), kost = q => m / q * kb + q / 2 * w * i;
      set('an1', fmt(x, 2) + ' t'); set('an1t', '√(2 · ' + fmt(m, 0) + ' · ' + fmt(kb, 0) + ' / (' + fmt(w, 0) + ' · ' + fmt(i, 2) + '))');
      const lo = Math.max(1, Math.floor(x)), hi = lo + 1, kl = kost(lo), kh = kost(hi), best = kl <= kh ? lo : hi;
      set('an2', fmt(best, 0) + ' t'); set('an2t', 'K(' + lo + ') = ' + fmt(kl, 2) + ' € · K(' + hi + ') = ' + fmt(kh, 2) + ' €');
      set('an3', fmt(m / best, 2) + '-mal'); set('an3t', 'm / x = ' + fmt(m, 0) + ' / ' + fmt(best, 0) + ' (exakt mit x_opt: ' + fmt(m / x, 2) + ')');
    };
    [M, K, W, I].forEach(x => x.addEventListener('input', draw)); draw();
  }
})();
