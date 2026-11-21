// Klicktest: jede Ansicht und jedes Werkzeug einmal bedienen, auf Desktop und Handy. Läuft mit `python3 bau.py --test`.
const { chromium } = require('playwright');
const path = require('path');
const URL = 'file://' + path.resolve(__dirname, '..', 'dist', 'index.html');

// Beantwortet die gerade sichtbare Frage irgendwie (richtig oder falsch ist egal, es geht um den Ablauf)
async function antworte(p, sel) {
  return p.evaluate(sel => {
    const q = document.querySelector(sel + ' .qz'); if (!q) return false;
    const n = q.querySelector('.q-next'); if (n) { n.click(); return true; }
    if (['mc', 'reihe'].includes(q.dataset.y)) { const o = q.querySelector('button.q-opt:not(:disabled)'); if (o) { o.click(); return true; } }
    q.querySelectorAll('.q-zrow, .q-rfz').forEach(r => r.querySelector('.q-chip').click());
    q.querySelectorAll('input.q-in,input.q-gap,input.q-li,textarea.q-ta').forEach(x => { x.value = '1'; });
    const s = q.querySelector('.q-show'); if (s) { s.click(); q.querySelector('.q-self')?.click(); return true; }
    if (q.dataset.y === 'hot') { q.querySelector('svg')?.dispatchEvent(new MouseEvent('click', { clientX: 5, clientY: 5, bubbles: true })); return true; }
    q.querySelector('.q-check')?.click(); return true;
  }, sel);
}

(async () => {
  const b = await chromium.launch(), fehler = [];
  const pruefe = (ok, was) => { if (!ok) fehler.push(was); };
  for (const [w, h, tag] of [[1360, 900, 'Desktop'], [390, 844, 'Handy']]) {
    const p = await b.newPage({ viewport: { width: w, height: h } });
    p.on('pageerror', e => fehler.push(`${tag}: ${e.message}`));
    await p.goto(URL + '#heute'); await p.evaluate(() => localStorage.clear()); await p.reload(); await p.waitForTimeout(400);
    if (tag === 'Desktop') {  // Inhalts-Check: alle Fächer laden, jede Rechenaufgabe mit Zufallszahlen erzeugen
      const r = await p.evaluate(async () => { await LT.lade(D.faecher.map(f => f.id)); let n = 0, bad = [];
        for (const x of Object.values(TOP)) for (const fam of x.t.fragen) for (const a of fam.a) if (a.y === 'num') { n++; const q = inst(a); if (isNaN(q.ans) || /\{/.test(q.w)) bad.push(x.t.id); }
        const ohneText = Object.values(TOP).filter(x => !x.t.html).length;
        return { n, bad, ohneText, themen: Object.keys(TOP).length }; });
      pruefe(r.bad.length === 0, `Rechenaufgaben fehlerhaft: ${r.bad.join(', ')}`);
      pruefe(r.ohneText === 0 && r.themen >= 9, `Unterthemen ohne Text: ${r.ohneText} von ${r.themen}`);
      console.log(`Inhalte: ${r.themen} Unterthemen, ${r.n} Rechenaufgaben erzeugt`);
    }
    const ueberlauf = async was => { const o = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth); pruefe(o <= 0, `${tag} ${was}: ${o}px Überlauf`); };

    // Heute: Karte drehen, Oberthema öffnen
    await p.click('.fk[data-f="ling"] .fk-vorn'); await p.waitForTimeout(800);
    pruefe(await p.$eval('.fk[data-f="ling"]', e => e.classList.contains('gedreht')), `${tag}: Karte dreht nicht`);
    await p.click('.fk[data-f="ling"] .fk-liste li:nth-child(2) button'); await p.waitForTimeout(1200);
    pruefe((await p.evaluate(() => location.hash)).startsWith('#lernen--ling--k2'), `${tag}: Oberthema von der Karte öffnet nicht`);
    await ueberlauf('Lernen');

    // Lernen: Verdecken, Karten, Suche, Wackel, Mini-Quiz, Weiter
    await p.click('[data-act="blur"]'); pruefe(await p.$('.inhalt.blurmode') !== null, `${tag}: Verdecken`); await p.click('[data-act="blur"]');
    await p.click('[data-act="karten"]'); pruefe(await p.$('#ov .sw-card') !== null, `${tag}: Karteikarten`); await p.keyboard.press('Escape');
    await p.click('[data-act="suche"]'); await p.fill('.pal-in', 'Saussure'); await p.waitForTimeout(1500);
    pruefe((await p.$$('.pal-it')).length > 0, `${tag}: Suche findet nichts`); await p.keyboard.press('Escape');
    await p.click('[data-act="wackel"]'); await p.waitForTimeout(200);
    pruefe(await p.evaluate(() => G.farbe(V.fid + '/' + V.tid) === 1 && G.itemsVon(V.fid + '/' + V.tid).every(i => G.stufe(i) === 1)), `${tag}: Unsicher setzt nicht alle Aufgaben auf 1`);
    pruefe(await p.$('.lt-hinweis button') !== null, `${tag}: Rückgängig fehlt`);
    await p.click('[data-act="quiz"]');
    for (let i = 0; i < 25; i++) { if (!(await antworte(p, '[data-mount="mini"]'))) break; await p.waitForTimeout(60); }
    pruefe(/richtig/.test(await p.$eval('[data-mount="mini"]', e => e.innerText)), `${tag}: Mini-Quiz endet nicht`);
    await p.click('.pg-next'); await p.waitForTimeout(400);
    pruefe(await p.evaluate(() => V.tid !== 'dichotomies' && location.hash.includes('lernen--ling--k2')), `${tag}: Weiter-Knopf`);

    // Markieren: Text auswählen → Leiste → Grün; dann Rot → Wackel; Panel; Neuladen behält Markierung
    const waehle = async () => { await p.evaluate(() => { const w = document.createTreeWalker(document.querySelector('.bl-card .inhalt .kurz'), NodeFilter.SHOW_TEXT); let t; while ((t = w.nextNode()) && t.nodeValue.trim().length < 25);
      t.parentElement.scrollIntoView({ block: 'center' }); const r = document.createRange(); r.setStart(t, 2); r.setEnd(t, 18); const s = getSelection(); s.removeAllRanges(); s.addRange(r); }); await p.waitForTimeout(400); };
    await waehle(); pruefe(await p.$('.mk-leiste') !== null, `${tag}: Markier-Leiste erscheint nicht`);
    if (await p.$('.mk-leiste')) {
      await p.click('[data-mkneu="gruen"]'); await p.waitForTimeout(300);
      pruefe(await p.$('mark.mk-gruen') !== null, `${tag}: grüne Markierung fehlt im Text`);
      pruefe(await p.evaluate(() => kartenFuer([{ key: V.fid + '/' + V.tid, f: cur().f, k: cur().k, t: cur().t }]).some(c => c.eigen)), `${tag}: grüne Markierung wird keine Karte`);
      await p.click('mark.mk-gruen'); await p.waitForTimeout(150); await p.click('[data-mkfarbe="rot"]'); await p.fill('.mk-pop textarea', 'Warum genau?'); await p.click('[data-mkok]'); await p.waitForTimeout(300);
      pruefe(await p.evaluate(() => G.farbe(V.fid + '/' + V.tid) !== 1), `${tag}: rote Markierung verändert das Unterthema`);
      pruefe(await p.$('.mk-notiz') !== null, `${tag}: Notiz-Zeichen am Text fehlt`);
      await p.reload(); await p.waitForTimeout(1300);
      pruefe(await p.$('mark.mk-rot') !== null, `${tag}: Markierung nach Neuladen weg`);
      await p.click('[data-act="markiert"]'); await p.waitForTimeout(200);
      pruefe((await p.$$('.mk-it')).length >= 1, `${tag}: Panel „Markiert“ leer`);
      await p.click('[data-mkbereich="fach"]'); await p.keyboard.press('Escape');
      // Übersicht aller Markierungen von der Startseite
      await p.evaluate(() => { document.getElementById('ov')?.remove(); location.hash = '#heute'; }); await p.waitForTimeout(500);
      pruefe(await p.$('.b7-mk') !== null, `${tag}: Startseite zeigt keine Markierungen`);
      if (await p.$('.b7-mk')) { await p.click('.b7-mk'); await p.waitForTimeout(250);
        pruefe(await p.evaluate(() => V_MK.bereich === 'alle' && document.querySelectorAll('#ov .mk-it').length >= 1 && /Linguistics/.test(document.querySelector('#ov .mk-it small')?.innerText || '')), `${tag}: Übersicht „alle Fächer“ fehlt`);
        await p.click('#ov .mk-it'); await p.waitForTimeout(900);
        pruefe(await p.evaluate(() => V.screen === 'lern' && !document.getElementById('ov')), `${tag}: Sprung aus der Übersicht`); }
    }
    // Erklärfenster
    if (await p.$('.glo >> visible=true')) { await p.click('.glo >> visible=true'); pruefe(await p.$('#glo-pop') !== null, `${tag}: Erklärfenster öffnet nicht`); await p.mouse.click(5, 5); }
    else fehler.push(`${tag}: keine Begriffe im Text markiert`);

    // Fach wechseln über den Umschalter
    const zweites = await p.evaluate(() => (D.faecher.find(f => f.id !== V.fid) || {}).id);
    if (zweites) { await p.click('[data-fw]'); await p.click(`.fw-f[data-go="lernf|${zweites}"]`); await p.waitForTimeout(1200);
      pruefe(await p.evaluate(z => V.fid === z, zweites), `${tag}: Fachwechsel`); }
    await p.evaluate(() => go('lern|ling|k2|linguistic-sign')); await p.waitForTimeout(1200);
    pruefe(await p.evaluate(() => !!document.querySelector('.inhalt svg')), `${tag}: Schaubild fehlt`);
    await ueberlauf('Schaubild');

    // Sandbox: Oberthemen aufklappen, eins wählen, Prüf-Knopf, alle Werkzeuge
    await p.evaluate(() => go('sb|ling')); await p.waitForTimeout(800);
    await p.click('[data-auf="ling"]'); await p.click('[data-sbk="ling/k2"]'); await p.waitForTimeout(200);
    pruefe(await p.$('.sx-pruef:not(.aus)') !== null, `${tag}: Prüf-Knopf erscheint nicht`);
    // Timer: Dauer wählen (Hover-Menü), starten
    await p.hover('.uhr'); await p.waitForTimeout(150); await p.click('.uhr [data-timer-min="10"]');
    pruefe(await p.$eval('[data-timer]', e => e.textContent) === '10:00', `${tag}: Timer-Dauer`);
    await p.click('.uhr [data-act="timer"]'); await p.waitForTimeout(1300);
    pruefe(await p.evaluate(() => !!S.uhr.ende && uhrRest() < 600), `${tag}: Timer läuft nicht`);
    await p.click('.uhr [data-act="timer"]');
    // Nachschlagen aus dem Endlos-Quiz: absichtlich falsch antworten, dann Fenster mit hervorgehobener Stelle
    await p.click('.m-tool[data-v="quiz"]'); await p.waitForTimeout(300);
    await p.evaluate(() => { const x = TOP['ling/structuralism'], el = document.querySelector('[data-mount="sb"]');
      quiz(el, { next: i => i ? null : { a: { y: 'mc', p: 'Who founded structuralism?', o: [['Saussure', true], ['Chomsky', false]] }, key: 'ling/structuralism', f: x.f, k: x.k, t: x.t } }); });
    await p.click('[data-mount="sb"] .q-opt[data-j="1"]'); await p.waitForTimeout(200);
    if (await p.$('.q-nach')) { await p.click('.q-nach'); await p.waitForTimeout(1300);
      pruefe(await p.$('#ov.ov-nach .inhalt') !== null, `${tag}: Nachschlagen-Fenster fehlt`);
      pruefe(await p.$('#ov .fund') !== null, `${tag}: Nachschlagen findet keine Stelle`); await p.keyboard.press('Escape'); }
    else fehler.push(`${tag}: kein „Nachschlagen“ nach falscher Antwort`);
    for (const t of ['drill', 'swipe', 'quiz', 'blatt']) {
      if (!(await p.$(`.m-tool[data-v="${t}"]`))) { await p.click('.zurueck'); await p.waitForTimeout(300); }   // eigene Seite je Werkzeug: erst zurück zur Übersicht
      await p.click(`.m-tool[data-v="${t}"]`); await p.waitForTimeout(400);
      pruefe(await p.$('.w-kopf .ziel') !== null, `${tag}: Werkzeugseite ${t} ohne Lernziel`);
      if (t === 'swipe') {   // Auswahl-Menü: aufklappen, Fach dazu, Oberthema wählen, Seite bleibt an ihrem Platz
        const y0 = await p.$eval('.w-buehne', e => e.getBoundingClientRect().top);
        await p.click('[data-act="sb-auswahl"]'); await p.waitForTimeout(300);
        pruefe(await p.$('.w-pop') !== null, `${tag}: Auswahl-Menü geht nicht auf`);
        if (await p.$('.w-pop')) {
          const fk = '.wp-f:not(.on) [data-act="sb-f"]';
          if (await p.$(fk)) {
          const fv = await p.$eval(fk, e => e.dataset.v), vor = await p.evaluate(() => V.sb.f.length); await p.click(fk); await p.waitForTimeout(300);
          pruefe(await p.evaluate(() => V.sb.f.length) !== vor, `${tag}: Fach im Auswahl-Menü lässt sich nicht wählen`);
          pruefe(Math.abs(await p.$eval('.w-buehne', e => e.getBoundingClientRect().top) - y0) < 2, `${tag}: Auswahl-Menü verschiebt die Seite`);
          await p.click(`[data-act="sb-f"][data-v="${fv}"]`); await p.waitForTimeout(200); }   // nur mit einem zweiten Fach
          await p.click('.w-pop-bg', { position: { x: 5, y: 600 } }); await p.waitForTimeout(200);
        }
      }
      if (t === 'swipe') {   // eigene Karte anlegen, sie zählt für das Unterthema und erscheint in den Karten
        await p.click('[data-act="eigen-neu"]'); await p.waitForTimeout(250);
        pruefe(await p.$('#ov .ek-form') !== null, `${tag}: Formular „Eigene Karte“ fehlt`);
        if (await p.$('#ov .ek-form')) {
          await p.fill('#ov textarea[name="v"]', 'Testfrage eigene Karte'); await p.fill('#ov textarea[name="r"]', 'Zeile 1\nZeile 2');
          await p.click('#ov .ek-form [type="submit"]'); await p.waitForTimeout(300);
          pruefe(await p.evaluate(() => { const [id, c] = Object.entries(S.eigen)[0] || []; const x = c && TOP[c.k]; return !!x && kartenFuer([{ key: c.k, f: x.f, k: x.k, t: x.t }]).some(k => k.id === 'e:' + id); }), `${tag}: eigene Karte nicht gespeichert`);
          pruefe((await p.$$('#ov .ek-it')).length === 1, `${tag}: Liste der eigenen Karten`);
          await p.click('#ov .ek-weg'); await p.waitForTimeout(150); await p.click('#ov .ek-weg'); await p.waitForTimeout(300);
          pruefe(await p.evaluate(() => Object.keys(S.eigen).length === 0 && !document.querySelector('#ov .ek-it')), `${tag}: eigene Karte lässt sich nicht löschen`);
          await p.evaluate(() => document.getElementById('ov')?.remove());
        }
      }
      if (t === 'drill') { await p.click('[data-act="sb-dmodus"][data-v="schreiben"]'); await p.waitForTimeout(300);
        pruefe(await p.$('[data-mount="sb"] .qz[data-y="rev"] textarea') !== null, `${tag}: Drill „Selbst schreiben“ ohne Schreibfeld`); }
      pruefe(await p.evaluate(() => document.querySelector('[data-mount="sb"]').innerText.trim().length > 10), `${tag}: Werkzeug ${t} leer`);
      await ueberlauf('Sandbox ' + t);
    }
    await p.click('.ring[data-r="3"]'); pruefe(await p.$('.ws-out[data-o="3"]:not([hidden])') !== null, `${tag}: Lösungsweg klappt nicht auf`);

    // Übungsklausur: Bogen ausfüllen, abgeben, Erklärfragen selbst bewerten, Ergebnis
    await p.click('.zurueck'); await p.waitForTimeout(300);
    await p.click('.sx-pruef'); await p.waitForTimeout(300);
    pruefe(await p.$('.pr-fakten') !== null, `${tag}: Übungsklausur-Intro fehlt`);
    await p.click('[data-act="pr-start"]'); await p.waitForTimeout(300);
    pruefe(await p.evaluate(() => [...document.querySelectorAll('.pb-a .pb-kopf em')].map(e => parseInt(e.textContent)).every((v, i, a) => !i || v >= a[i - 1])), `${tag}: Aufgaben nicht von klein nach groß`);
    await p.evaluate(() => document.querySelectorAll('.pb-a .qz').forEach(q => {
      q.querySelector('.q-opt:not(:disabled)')?.click(); q.querySelectorAll('.q-zrow, .q-rfz').forEach(r => r.querySelector('.q-chip').click());
      q.querySelectorAll('input.q-in,input.q-gap,textarea.q-ta').forEach(x => { x.value = 'Menge'; });
      if (q.dataset.y === 'reihe') q.querySelectorAll('.q-opt').forEach(o => o.click());
      if (q.dataset.y === 'hot') q.querySelector('svg')?.dispatchEvent(new MouseEvent('click', { clientX: 5, clientY: 5, bubbles: true })); }));
    await p.click('.pb-leiste .pb-ab'); await p.waitForTimeout(300);
    if (await p.$('.pb-ja')) await p.click('.pb-ja');
    await p.evaluate(() => document.querySelectorAll('.pb-a').forEach(li => li.querySelector('[data-selbst="0.5"]')?.click()));
    for (let i = 0; i < 6; i++) await p.evaluate(() => [...document.querySelectorAll('.pb-teile > li')].forEach(tl => tl.querySelector('[data-tselbst$="|0.5"]:not(.btn-main)')?.click()));
    await p.waitForTimeout(300);
    pruefe(await p.$('.erg-zahl') !== null, `${tag}: Übungsklausur ohne Ergebnis`);
    pruefe(await p.evaluate(() => !!S.pruef['ling/k2']), `${tag}: Prüfungsstand nicht gespeichert`);

    // Einstellungen: Dunkel, Testdatum → verblasst, zurück auf Gerät
    await p.evaluate(() => { const x = S.pruef['ling/k2']; if (x && !(x.s > 0)) x.s = 60; });   // Zufallsantworten können 0 % ergeben; 0 % kann nicht verfallen
    await p.evaluate(() => go('einst')); await p.click('[data-act="theme"][data-v="dark"]');
    pruefe(await p.evaluate(() => document.documentElement.dataset.theme === 'dark'), `${tag}: Dunkelmodus`);
    await p.fill('[data-act="testtage"]', '20'); await p.dispatchEvent('[data-act="testtage"]', 'change'); await p.waitForTimeout(200);
    await p.evaluate(() => go('dash')); await p.waitForTimeout(300);
    pruefe(await p.evaluate(() => faelligListe().length >= 1), `${tag}: Verfall mit Testdatum`);
    await p.evaluate(() => { S.einst.testTage = 0; setzeTheme('system'); });
    await ueberlauf('Heute');

    // Adresse: Neuladen landet wieder auf derselben Ansicht
    await p.evaluate(() => go('lern|ling|k1|')); await p.waitForTimeout(1000); await p.reload(); await p.waitForTimeout(1200);
    pruefe(await p.evaluate(() => V.screen === 'lern' && V.fid === 'ling' && V.kid === 'k1'), `${tag}: Adresse nach Neuladen`);
    // Probeklausur: Knopf auf der Training-Seite öffnet das Deckblatt mit Teilen
    await p.goto(URL + '#sandbox'); await p.waitForTimeout(500);
    await p.click('.pk-fz'); await p.waitForTimeout(250); await p.click('.pk-oks button'); await p.waitForTimeout(600);
    pruefe(await p.$('.pr-fakten') !== null, `${tag}: „Jetzt abprüfen“ → Oberthema startet keine Übungsklausur`);
    await p.goto(URL + '#sandbox'); await p.waitForTimeout(500);
    await p.click('.pk-probe[data-go^="probe|"]'); await p.waitForTimeout(1200);
    pruefe(await p.$('.kb-deck') !== null, `${tag}: Probeklausur-Deckblatt fehlt`);
    await p.click('[data-act="pr-start"]'); await p.waitForTimeout(700);
    pruefe(await p.evaluate(() => kbSumme(V.pr.bogen) === 17 && document.querySelectorAll('.kb-auf').length === 4), `${tag}: Probeklausur nicht 17 Punkte / 4 Aufgaben`);
    await p.click('.kb-ende [data-kb="abgeben"]'); await p.waitForTimeout(500);
    pruefe(await p.evaluate(() => document.querySelectorAll('.kb-loes:not([hidden])').length >= 4), `${tag}: Abgeben zeigt keine Lösungen`);
    // Methodisch lernen: fällige Aufgaben (aus „Unsicher“ oben) erscheinen im Originalformat; Schalter „Frei · Methodisch“
    await p.goto(URL + '#heute'); await p.waitForTimeout(500);
    pruefe(/fällig/.test(await p.$eval('.m-wackel', e => e.innerText)), `${tag}: Start zeigt „Methodisch lernen“ nicht`);
    await p.click('.m-wackel'); await p.waitForTimeout(1500);
    pruefe(await p.$('[data-mount="sb"] .qz') !== null, `${tag}: Methodisch lernen zeigt keine Aufgabe`);
    for (let i = 0; i < 6; i++) { if (!(await antworte(p, '[data-mount="sb"]'))) break; await p.waitForTimeout(80); }
    await p.click('.zurueck'); await p.waitForTimeout(300);
    await p.click('[data-act="sb-tool"][data-v="quiz"]'); await p.waitForTimeout(300); await p.click('[data-act="sb-modus"][data-v="methodisch"]'); await p.waitForTimeout(1200);
    pruefe(await p.evaluate(() => { const q = document.querySelector('[data-mount="sb"] .qz'); return !q || !['karte', 'teil'].includes(q.dataset.y); }), `${tag}: Endlos-Quiz methodisch zeigt Nicht-Quizaufgaben`);
    await p.close();
  }
  await b.close();
  console.log(fehler.length ? fehler.join('\n') + `\n${fehler.length} Fehler` : 'Klicktest ok: 0 Fehler');
  process.exit(fehler.length ? 1 : 0);
})();
