/* Brutto-Netto-Rechner und exponentielle Glättung */
(function () {
  const set = (id, t) => { const e = document.getElementById(id); if (e) e.textContent = t; };
  const S = document.getElementById('bnS');
  if (S) {
    const Z = document.getElementById('bnZ'), L = document.getElementById('bnL'), B = document.getElementById('bnB'), R = document.getElementById('bnR');
    const draw = () => {
      const s = +S.value, z = +Z.value, l = +L.value, b = +B.value, r = +R.value;
      set('bnS-o', fmt(s, 0) + ' Stück'); set('bnZ-o', fmt(z, 0) + ' %'); set('bnL-o', fmt(l, 0) + ' Stück'); set('bnB-o', fmt(b, 0) + ' Stück'); set('bnR-o', fmt(r, 0) + ' Stück');
      const zb = Math.round(s * z / 100), br = s + zb, v = l + b - r, n = br - v;
      set('bnA', fmt(br, 0)); set('bnAt', fmt(s, 0) + ' + ' + fmt(zb, 0) + ' Zusatzbedarf (' + z + ' %)');
      set('bnV', fmt(v, 0)); set('bnVt', 'Lager ' + fmt(l, 0) + ' + bestellt ' + fmt(b, 0) + ' − reserviert ' + fmt(r, 0));
      set('bnN', n > 0 ? fmt(n, 0) + ' Stück' : '0 Stück'); set('bnNt', n > 0 ? 'Bruttobedarf − verfügbare Menge: so viel muss beschafft werden' : 'kein Beschaffungsbedarf, verfügbare Menge reicht (Überdeckung ' + fmt(-n, 0) + ')');
    };
    [S, Z, L, B, R].forEach(e => e.addEventListener('input', draw)); draw();
  }
  const A = document.getElementById('egA');
  if (A) {
    const V = document.getElementById('egV'), T = document.getElementById('egT');
    const draw = () => {
      const a = +A.value, v = +V.value, t = +T.value, d = t - v, k = a * d;
      set('egA-o', fmt(a, 1)); set('egV-o', fmt(v, 0) + ' Stück'); set('egT-o', fmt(t, 0) + ' Stück');
      set('egD', (d >= 0 ? '+' : '−') + fmt(Math.abs(d), 0)); set('egDt', 'T_i − V_alt = ' + fmt(t, 0) + ' − ' + fmt(v, 0));
      set('egK', (k >= 0 ? '+' : '−') + fmt(Math.abs(k), 1)); set('egKt', 'α · Abweichung = ' + fmt(a, 1) + ' · ' + fmt(d, 0));
      set('egN', fmt(v + k, 1)); set('egNt', a <= 0.3 ? 'kleines α: starke Glättung, die Prognose reagiert träge' : (a >= 0.6 ? 'großes α: folgt dem letzten Wert stark, wenig Glättung' : 'mittleres α'));
    };
    [A, V, T].forEach(e => e.addEventListener('input', draw)); draw();
  }
})();
