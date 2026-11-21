/* Hurwicz: Φ = λ·Max + (1 − λ)·Min für die Folienmatrix */
(function () {
  const L = document.getElementById('huL'); if (!L) return;
  const M = [['a1', [60, 30, 50, 60]], ['a2', [10, 10, 10, 140]], ['a3', [-30, 100, 120, 130]]];
  function draw() {
    const l = +L.value, phi = M.map(([, w]) => l * Math.max(...w) + (1 - l) * Math.min(...w)), best = phi.indexOf(Math.max(...phi));
    const X = v => 110 + v * 1.5;
    let s = BW.l(X(0), 14, X(0), 170, 'var(--axis)', 1.4) + BW.t(X(0), 188, '0', { size: 12, w: 400 });
    [-40, 40, 80, 120].forEach(k => { s += BW.l(X(k), 166, X(k), 172, 'var(--axis)') + BW.t(X(k), 188, k, { size: 12, w: 400 }); });
    M.forEach(([n, w], i) => {
      const y = 22 + i * 50, mn = Math.min(...w), mx = Math.max(...w), v = phi[i];
      s += BW.t(6, y + 22, n, { w: 800, a: 'start' });
      s += BW.l(X(mn), y + 18, X(mx), y + 18, 'var(--axis2)', 8);
      s += BW.t(X(mn) - 8, y + 22, String(mn).replace('-', '−'), { size: 12, w: 600, f: 'var(--muted)', a: 'end' }) + BW.t(X(mx) + 8, y + 22, mx, { size: 12, w: 600, f: 'var(--muted)', a: 'start' });
      s += BW.dot(X(v), y + 18, i === best ? 'var(--primary)' : 'var(--c3)', 8);
      s += BW.t(X(v), y + 40, 'Φ = ' + fmt(v, 1), { w: 800, f: i === best ? 'var(--primary)' : 'var(--ink)', size: 13 });
    });
    document.getElementById('figHU').innerHTML = s;
    BW.setz('huR1', 'Φ = ' + fmt(phi[0], 2)); BW.setz('huT1', `${fmt(l, 1)} · 60 + ${fmt(1 - l, 1)} · 30`);
    BW.setz('huR2', fmt(phi[1], 2) + ' | ' + fmt(phi[2], 2)); BW.setz('huT2', `a2: ${fmt(l, 1)} · 140 + ${fmt(1 - l, 1)} · 10 · a3: ${fmt(l, 1)} · 130 + ${fmt(1 - l, 1)} · (−30)`);
    BW.setz('huR3', M[best][0]); BW.setz('huT3', l === 0 ? 'λ = 0: wie die Maximin-Regel' : l === 1 ? 'λ = 1: wie die Maximax-Regel' : `größtes Φ. λ = ${fmt(l, 1)}: ${l < .5 ? 'eher vorsichtig' : 'eher optimistisch'}`);
  }
  L.addEventListener('input', draw); draw();
})();
