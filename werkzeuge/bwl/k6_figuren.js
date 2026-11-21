/* Nutzenfunktion: zwei Alternativen, Gewicht Umsatz/Gewinn; drei Rechenwege nebeneinander */
(function () {
  const W = document.getElementById('nfW'); if (!W) return;
  function draw() {
    const g1 = +W.value / 100, g2 = 1 - g1, U = [800000, 600000], G = [7000, 8000];
    const m1 = U.map((u, i) => g1 * u + g2 * G[i]);
    const e = U.map((u, i) => g1 * (u === Math.max(...U) ? 1 : 0) + g2 * (G[i] === Math.max(...G) ? 1 : 0));
    const n = U.map((u, i) => g1 * u / Math.max(...U) + g2 * G[i] / Math.max(...G));
    const reihen = [['Multiplikation', m1, Math.max(...m1)], ['einf. Normierung', e, 1], ['Normierung', n, 1]];
    let s = '';
    reihen.forEach(([name, w, mx], r) => {
      const y0 = 16 + r * 76; s += BW.t(4, y0 + 10, name, { a: 'start', w: 800, size: 13 });
      w.forEach((v, i) => {
        const y = y0 + 20 + i * 24, len = mx > 0 ? v / mx * 220 : 0, best = v === Math.max(...w);
        s += BW.t(30, y + 14, 'a' + (i + 1), { a: 'end', w: 700, size: 13 });
        s += `<rect x="38" y="${y}" width="${Math.max(2, len)}" height="18" rx="4" style="fill:${best ? 'var(--primary)' : 'var(--axis2)'}"/>`;
        s += BW.t(44 + Math.max(2, len), y + 14, (r === 0 ? fmt(v, 0) : fmt(v, 3)) + (best ? '  ✓' : ''), { a: 'start', size: 13, w: best ? 800 : 500 });
      });
    });
    document.getElementById('figNF').innerHTML = s;
    const sieger = w => w[0] === w[1] ? 'gleich' : (w[0] > w[1] ? 'a1' : 'a2');
    BW.setz('nfR1', sieger(m1)); BW.setz('nfT1', `a1: ${fmt(m1[0], 0)} · a2: ${fmt(m1[1], 0)}. Die großen Umsatzzahlen dominieren.`);
    BW.setz('nfR2', sieger(e)); BW.setz('nfT2', `a1: ${fmt(e[0], 3)} · a2: ${fmt(e[1], 3)}. Bester Wert = 1, schlechtester = 0.`);
    BW.setz('nfR3', sieger(n)); BW.setz('nfT3', `a1: ${fmt(n[0], 3)} · a2: ${fmt(n[1], 3)}. Jeder Wert ÷ höchster Wert.`);
  }
  W.addEventListener('input', draw); draw();
})();
