// Screenshots aller Ansichten (Desktop, Handy, Dunkel) + Prüfung auf seitlichen Überlauf und JS-Fehler.
// Aufruf: node tests/screenshots.js [Zielordner]   (wird von bau.py --test nicht automatisch gestartet: Datei beginnt nicht mit t_)
const { chromium } = require('playwright');
const path = require('path');
const DIST = 'file://' + path.resolve(__dirname, '..', 'dist', 'index.html');
const OUT = process.argv[2] || path.resolve(__dirname, '..', 'tests', 'bilder');
const SEITEN = [['heute', 'heute'], ['dicho', 'lernen--ling--k1--form-function'], ['zeichen', 'lernen--ling--k2--linguistic-sign'], ['chomsky', 'lernen--ling--k2--formalism-chomsky'],
  ['sb', 'sandbox'], ['pruef', 'pruefung--ling--k2--end'], ['einst', 'einstellungen']];
(async () => {
  require('fs').mkdirSync(OUT, { recursive: true });
  const b = await chromium.launch(), fehler = [];
  for (const [w, h, tag, dunkel] of [[1360, 900, 'd', false], [390, 844, 'm', false], [1360, 900, 'dd', true], [390, 844, 'md', true]]) {
    const ctx = await b.newContext({ viewport: { width: w, height: h }, colorScheme: dunkel ? 'dark' : 'light' });
    const p = await ctx.newPage();
    p.on('pageerror', e => fehler.push(`${tag} ${e.message}`));
    p.on('console', m => { if (m.type() === 'error') fehler.push(`${tag} console ${m.text()}`); });
    await p.goto(DIST + '#heute'); await p.waitForTimeout(500);
    for (const [n, h] of SEITEN) {
      await p.evaluate(x => { location.hash = x; }, h); await p.waitForTimeout(900);
      const ov = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth);
      if (ov > 0) fehler.push(`${tag} ${n}: ${ov}px seitlicher Überlauf`);
      await p.screenshot({ path: `${OUT}/${tag}-${n}.png` });
    }
    await ctx.close();
  }
  await b.close();
  console.log(fehler.join('\n') || 'Screenshots ok: keine Fehler, kein Überlauf');
  process.exit(fehler.length ? 1 : 0);
})();
