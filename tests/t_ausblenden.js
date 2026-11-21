// Unterthemen ausblenden (S.uaus): kein Training, keine Übungs-/Refresh-/Probeklausur, Oberthema „fertig“ ohne die ausgeblendeten.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch(), p = await b.newPage(), fehler = [];
  p.on('pageerror', e => fehler.push('pageerror: ' + e.message));
  await p.goto('file://' + path.resolve(__dirname, '..', 'dist', 'index.html') + '#heute'); await p.waitForTimeout(300);
  const r = await p.evaluate(async () => {
    const f = [], ok = (b, was) => { if (!b) f.push(was); };
    await LT.lade(['ling']);
    const fach = F.ling, k = fach.kapitel.find(k => k.topics.filter(t => (t.fragen || []).length).length >= 3);
    const [a, ...rest] = k.topics.filter(t => (t.fragen || []).length), key = 'ling/' + a.id;
    uSetze(key, true);
    ok(uAus(key), 'uSetze/uAus');
    ok(!themen({ f: ['ling'] }).some(x => x.key === key), 'Training-Pool enthält ausgeblendetes Unterthema');
    ok(!klausurThemen(k, fach).includes(a) && !klausurThemen(k).includes(a), 'Übungsklausur enthält ausgeblendetes Unterthema');
    for (let i = 0; i < 5; i++) ok(!klausurAufgaben(fach, k).some(it => it.t === a), 'Übungsklausur zieht Frage aus ausgeblendetem Unterthema');
    const kl = (D.klausuren || []).find(x => (x.teile || []).some(t => t[1] === 'ling'));
    ok(!!kl, 'keine Klausur mit Linguistics gefunden');
    if (kl) for (let i = 0; i < 3; i++) ok(!probeAufgaben(kl).some(it => it.t === a), 'Probeklausur zieht Frage aus ausgeblendetem Unterthema');
    // fällig: Aufgabe aus dem ausgeblendeten Thema ist nie fällig
    S.g['q:test:mc'] = { s: 1, k: key, d: 0, e: 0, t: 0 }; G.cache = null;
    ok(!G.faelligListe().some(x => x.e.k === key), 'fällige Liste enthält ausgeblendetes Unterthema');
    delete S.g['q:test:mc'];
    // fertig: alle eingeblendeten grün → Oberthema fertig, auch wenn das ausgeblendete fehlt
    const echtFarbe = G.farbe; G.farbe = kk => kk === key ? 0 : 4;
    ok(kapFertig(fach, k), 'Oberthema nicht fertig, obwohl nur das ausgeblendete fehlt');
    uSetze(key, false);
    ok(!kapFertig(fach, k), 'Oberthema fertig, obwohl ein eingeblendetes Unterthema fehlt');
    G.farbe = echtFarbe;
    ok(themen({ f: ['ling'] }).some(x => x.key === key), 'Einblenden holt Unterthema nicht zurück');
    // Oberfläche: Knopf im Dock schaltet um
    go(`lern|ling|${k.id}|${a.id}`); await new Promise(r => setTimeout(r, 200));
    const knopf = document.querySelector('[data-act="uaus"]'); ok(!!knopf, 'Knopf „Ausblenden“ fehlt'); knopf && knopf.click();
    await new Promise(r => setTimeout(r, 100));
    ok(uAus(key) && document.querySelector('.bl-rail button.u-aus'), 'Knopf blendet nicht aus oder Leiste zeigt es nicht');
    uSetze(key, false);
    // Prüfungsausgrenzung (ag): von Haus aus ausgeblendet, Einblenden speichert 0, Ausblenden löscht den Eintrag wieder
    const agT = Object.keys(TOP).filter(kk => TOP[kk].t.ag);
    // seit 17.11.2026 wird Ausgegrenztes gar nicht mehr gebaut (inhalte/<fach>/ausgeblendet.json); ag-Unterthemen gibt es dann keine mehr
    for (const kk of agT) ok(uAus(kk) && !themen({ f: [kk.split('/')[0]] }).some(x => x.key === kk), 'ag-Unterthema nicht von Haus aus ausgeblendet: ' + kk);
    if (agT[0]) { uSetze(agT[0], false); ok(!uAus(agT[0]) && S.uaus[agT[0]] === 0, 'ag-Unterthema lässt sich nicht einblenden'); uSetze(agT[0], true); ok(uAus(agT[0]) && !(agT[0] in S.uaus), 'ag-Unterthema lässt sich nicht wieder ausblenden'); }
    const mk = F.ling; if (mk && mk.klausur) for (let i = 0; i < 3; i++) { const B = klausurZiehen((D.klausuren || []).find(x => (x.teile || []).some(t => t[1] === 'ling')));
      ok(!B.aufgaben.some(A => A.teile.some(T => T.v.unter && uAus('ling/' + T.v.unter))), 'Probeklausur-Bogen zieht Variante aus ausgeblendetem Unterthema'); }
    return f;
  });
  await b.close();
  const alle = [...fehler, ...r];
  if (alle.length) { console.log('FEHLER:\n' + alle.join('\n')); process.exit(1); }
  console.log('Ausblenden OK: Training, Übungs- und Probeklausur, Bogen, fällige Aufgaben, Oberthema fertig, Knopf, Prüfungsausgrenzung');
})().catch(e => { console.log('FEHLER: ' + e.message); process.exit(1); });
