// Engine-Test: Bewertungsregeln und Stufen. Läuft mit `python3 bau.py --test`.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch(), p = await b.newPage();
  await p.goto('file://' + path.resolve(__dirname, '..', 'dist', 'index.html') + '#heute'); await p.waitForTimeout(300);
  const r = await p.evaluate(async () => {
    const f = [], ok = (b, was) => { if (!b) f.push(was); };
    // Tippfehler-Toleranz
    ok(vergleich('Materialwirtschaft', ['Materialwirtschaft']) === 'exakt', 'exakt');
    ok(vergleich('Materialwirtschat', ['Materialwirtschaft']) === 'fast', 'ein Tippfehler zählt');
    ok(vergleich('Matrialwirtshaft', ['Materialwirtschaft']) === 'fast', 'zwei Tippfehler bei langem Wort zählen');
    ok(vergleich('Logistik', ['Lagerung']) === '', 'anderes Wort zählt nicht');
    ok(vergleich('Zeit', ['Zeil']) === '', 'kurze Wörter müssen exakt stimmen');
    // Liste
    const pk = [['Teil', 'Material'], ['Zeitpunkt', 'Zeit'], ['Qualität'], ['Menge'], ['Ort'], ['Preis', 'Kosten']];
    const t = listePruefen('richtige Menge\nrichtiger Ort\nrichtiger Preis\nQualitaet\nrichtige Zeit', pk);
    ok(t.filter(Boolean).length === 5 && !t[0], 'Liste: 5 von 6 erkannt, Teil fehlt (' + t + ')');
    ok(listePruefen('Menge, Ort, Preis', pk).filter(Boolean).length === 3, 'Liste mit Kommas');
    // Kernpunkte
    const kp = kernpunkte('Die Logistik umfasst den ganzen Weg vom Lieferanten bis zum Kunden, die Materialwirtschaft ist ein Teil davon.', ['Logistik: ganzer Weg vom Lieferanten bis zum Kunden', 'Materialwirtschaft = Teil der Logistik', 'Informationsfluss gehört dazu']);
    ok(kp[0] && kp[1] && !kp[2], 'Kernpunkte erkannt (' + kp + ')');
    // Stufen: auf „Klausur“ und „Schwer“ fast keine Einstiegsfragen, wo es schwerere Varianten gibt
    await LT.lade(['ling']);
    const fams = Object.values(TOP).filter(x => x.f.id === 'ling').flatMap(x => x.t.fragen);
    const anteil = (w, bed, nur = a => (a.lvl || 1) >= 2) => { let n = 0, m = 0; for (const fam of fams) { if (!fam.a.some(nur)) continue; for (let i = 0; i < 4; i++) { m++; if (bed(variante(fam, w))) n++; } } return n / m; };
    const l1k = anteil('klausur', a => (a.lvl || 1) === 1), l3s = anteil('schwer', a => (a.lvl || 1) === 3 || a.klausur, a => (a.lvl || 1) >= 3 || a.klausur), l1g = anteil('grund', a => (a.lvl || 1) <= 2, a => (a.lvl || 1) <= 2);
    ok(l1k === 0, `Klausur-Stufe zieht Stufe-1-Fragen (${(l1k * 100).toFixed(0)} %)`);
    ok(l3s > .6, `Schwer-Stufe zu leicht (${(l3s * 100).toFixed(0)} % Stufe 3/Klausur)`);
    ok(l1g === 1, 'Grundlagen-Stufe zieht Stufe-3-Fragen');
    // Endlos-Quiz: Niveau je Unterthema; 3 richtige in Folge im selben Unterthema → schwerer; im freien Modus keine Wiederholung
    { const x = TOP['ling/structuralism'], pool = [{ key: 'ling/structuralism', f: x.f, k: x.k, t: x.t }], e = endlos(pool), res = [];
      let it = e.next(0, res), hoch = false;
      for (let i = 1; i <= 3; i++) { res.push({ ok: true, item: it }); it = e.next(i, res); hoch = hoch || e.schwerer; }
      ok(hoch, 'Endlos: nach 3 richtigen im selben Unterthema nicht schwerer');
      res.push({ ok: false, item: it }); let nochmal = false;
      for (let i = 5; i < 12; i++) { it = e.next(i, res); res.push({ ok: true, item: it }); if (it.nochmal) nochmal = true; }
      ok(!nochmal, 'Endlos (frei): Falsches darf nicht automatisch wiederkommen'); }
    // Übungsklausur: jedes Unterthema, von klein nach groß, Punktzahl im Rahmen
    for (const fid of D.faecher.map(f => f.id)) {
      await LT.lade([fid]);
      for (const k of F[fid].kapitel) {
        const its = klausurAufgaben(F[fid], k), mitFragen = klausurThemen(k).filter(t => t.fragen.length).length, summe = its.reduce((s, x) => s + x.max, 0);
        ok(new Set(its.map(x => x.t.id)).size + its.ausgelassen.length === mitFragen, `${fid}/${k.id}: Unterthemen fehlen ohne Hinweis`);
        ok(its.every((x, i) => !i || x.max >= its[i - 1].max), `${fid}/${k.id}: nicht von klein nach groß`);
        ok(summe >= Math.min(18, mitFragen * 2) && summe <= 45, `${fid}/${k.id}: Punktzahl ${summe}`);
      }
    }
    // Arbeitsblatt „Klausurmäßig“: erst kurze, dann große; eigene große Aufgaben werden genutzt
    await LT.lade(['ling']);
    const pool2 = themen({ f: ['ling'], k: ['ling/k1', 'ling/k2'] });
    const mitAufg = F.ling.aufgaben.length > 0;
    const zt = blattZiehen(pool2, { stufe: 'klausurmaessig' }), z = zt.length > 1 ? { teilA: zt[0].liste, teilB: zt[1].liste } : { teilA: [], teilB: zt[0].liste };
    ok(zt[zt.length - 1].reserve.length > 0, 'Arbeitsblatt: keine Reserve zum Tauschen');
    ok(zt.length === 1 || (z.teilA.length >= 2 && z.teilA.every(A => A.punkte <= 3)), 'Klausurmäßig: Teil A nicht kurz');
    ok([...z.teilA, ...z.teilB].every(A => A.klausur), 'Klausurniveau: nur Klausuraufgaben');
    ok(z.teilB.some(A => (A.gross && A.teile.length === 4) || A.kv), 'Klausurmäßig: große Aufgabe (a–d oder Klausuraufgabe) fehlt');
    ok(Math.min(...z.teilB.map(A => A.punkte)) >= 4, 'Klausurmäßig: Teil B nicht groß');
    const sz = [...z.teilA, ...z.teilB].reduce((s, A) => s + A.punkte, 0); ok(sz <= 45, 'Klausurmäßig: zu lang (' + sz + ' P)');
    const r2 = blattZiehen(pool2, { stufe: 'klausur', arten: ['zeichnen'] })[0].liste;
    ok(r2.every(A => A.art === 'zeichnen'), 'Arbeitsblatt: Aufgabenart-Filter');
    const kl4 = klausurAufgaben(F.ling, F.ling.kapitel.find(k => k.id === 'k2'));
    if (mitAufg) ok(kl4.some(it => it.gross) && kl4[kl4.length - 1].gross, 'Übungsklausur l4: große Aufgabe fehlt oder steht nicht am Ende');
    ok(kl4.reduce((s, x) => s + x.max, 0) <= 45, 'Übungsklausur k2: zu lang');
    // Verfall: Haltbarkeit h, danach 2,4 % pro Tag; gelungener Refresh verdoppelt h
    S.pruef['ling/k1'] = { s: 100, d: jetzt() - 8 * DAY, h: 7 };
    ok(stand('ling', 'k1').pct === 98 && stand('ling', 'k1').faellt, 'Verfall nach Haltbarkeit');
    const its = [{ max: 2, p: 2, t: { id: 'dichotomies' }, key: 'ling/dichotomies' }, { max: 2, p: 2, t: { id: 'structuralism' }, key: 'ling/structuralism' }];
    verbucheRefresh('ling', 'k1', its, 4, 4);
    ok(S.pruef['ling/k1'].h === 14 && stand('ling', 'k1').pct === 100, 'Refresh macht frisch und verdoppelt die Haltbarkeit');
    delete S.pruef['ling/k1'];
    // Gedächtnis (Stufen-System): Regeln mit verschobenem Datum prüfen
    {
      const alt = S.einst.testTage; S.g = {}; G.cache = null;
      const tag = n => { S.einst.testTage = n; };
      const key = Object.keys(TOP).find(k => k.startsWith('ling/')), id = 'q:test:mc', st = () => G.stufe(id);
      tag(0); G.antwort(id, true, { k: key }); ok(st() === 4, 'neu und richtig → 4');
      G.antwort(id, false, { k: key }); ok(st() === 1 && G.faellig(id) && G.frisch(id), 'falsch → 1, sofort fällig');
      G.antwort(id, true, { k: key }); ok(st() === 1 && !G.frisch(id), 'am selben Tag richtig: nur nachgelernt, kein Aufstieg');
      ok(!G.faellig(id) && G.termin(id) === G.tag() + 1, 'nachgelernt → morgen wieder');
      G.antwort(id, true, { k: key }); G.antwort(id, true, { k: key }); ok(st() === 1, 'mehrmals am Tag richtig: kein Aufstieg');
      tag(1); ok(G.faellig(id), 'am nächsten Tag fällig'); G.antwort(id, true, { k: key }); ok(st() === 2, 'nächster Tag richtig → 2');
      G.antwort(id, true, { k: key }); ok(st() === 2, 'höchstens +1 pro Tag');
      tag(2); G.antwort(id, true, { k: key }); ok(st() === 3, '→ 3');
      tag(5); G.antwort(id, true, { k: key }); ok(st() === 4 && !S.g[id].b, '→ 4 (noch nicht bestätigt)');
      tag(12); G.antwort(id, true, { k: key }); ok(st() === 4 && S.g[id].b, '4 an einem späteren Tag → bestätigt');
      // Karteikarten-Runden: neue Karten bekommen die Stufe ihrer Runde
      tag(20); const k1 = 'k:test:a', k2 = 'k:test:b', k3 = 'k:test:c';
      G.antwort(k1, true, { k: key, runde: 1 }); G.antwort(k2, false, { k: key, runde: 1 }); G.antwort(k3, false, { k: key, runde: 1 });
      G.antwort(k2, true, { k: key, runde: 2 }); G.antwort(k3, false, { k: key, runde: 2 }); G.antwort(k3, false, { k: key, runde: 3 }); G.antwort(k3, true, { k: key, runde: 4 });
      ok(G.stufe(k1) === 4 && G.stufe(k2) === 3 && G.stufe(k3) === 2, `Runden 1/2/4 → 4/3/2 (${G.stufe(k1)}/${G.stufe(k2)}/${G.stufe(k3)})`);
      ok(G.termin(k2) === G.tag() + 1 && G.termin(k3) === G.tag() + 1, 'heute neu gelernt (2 und 3) → morgen');
      ok(G.termin(k1) === G.tag() + 3 || G.termin(k1) < G.tag() + 3, 'heute neu und sofort gewusst → nach 3 Tagen');
      // Unterthema: Farbe aus dem Durchschnitt, „unsicher“ setzt alle auf 1, Rückgängig
      tag(0); S.g = {}; G.cache = null;
      const l = G.itemsVon(key); ok(l && l.length >= 5, 'Unterthema hat Aufgaben-IDs');
      ok(G.farbe(key) === 0, 'unbearbeitet = grau');
      const zur = G.unsicher(key); ok(G.farbe(key) === 1 && istWackel(key), 'unsicher → rot (Wackelthema)');
      zur(); ok(G.farbe(key) === 0, 'Rückgängig');
      l.slice(0, 5).forEach(i => G.antwort(i, true, { k: key })); ok(G.farbe(key) === 4, '5 sofort gewusst → grün');
      G.antwort(l[0], false, { k: key }); G.antwort(l[1], false, { k: key }); ok(G.farbe(key) === 3, 'Ø 2,8 → hellgrün (' + G.thema(key).avg + ')');
      ok(G.faelligListe()[0].frisch, 'frische Fehler stehen vorn');
      S.g = {}; G.cache = null; S.einst.testTage = alt;
    }
    // Probeklausur: Punkte wie die echte Klausur, Teile nach Gewicht, keine Aufgabe doppelt
    await LT.lade(D.faecher.map(f => f.id));
    for (const kl of D.klausuren.filter(k => k.faecher.some(f => F[f]) && k.faecher.filter(f => F[f]).every(f => Object.keys(F[f].fragen || {}).length))) {   // Fächer im Aufbau (noch ohne Fragen) überspringen
      const it = probeAufgaben(kl), sum = it.reduce((s, x) => s + x.max, 0), ges = kl.punkte || 120;
      ok(sum >= ges - 8 && sum <= ges + 3, `Probeklausur ${kl.kurz}: ${sum} statt ${ges} Punkte`);
      ok(new Set(it).size === it.length, `Probeklausur ${kl.kurz}: Aufgabe doppelt`);
      const teile = kl.teile.filter(t => F[t[1]]), g = teile.reduce((s, t) => s + t[2], 0);
      teile.forEach((t, i) => { const p = it.filter(x => x.teil === i).reduce((s, x) => s + x.max, 0), soll = ges * t[2] / g; ok(Math.abs(p - soll) <= 6, `Probeklausur ${kl.kurz}, Teil ${t[4]}: ${p} statt ${soll} P`); });
    }
    // Potenzen in Zufallsaufgaben: ^ ist Potenz (nicht Bit-Operator)
    ok(ev('2^(M+N-K)', { M: 3, N: 5, K: 4 }) === 16, 'Potenz: 2^4 muss 16 sein');
    ok(ev('A*Q^(N-1)', { A: 3, Q: 3, N: 5 }) === 243, 'Potenz: 3·3^4 muss 243 sein');
    ok(Math.abs(ev('Z/(1+I/100)^T', { Z: 1000, I: 10, T: 2 }) - 826.446) < .01, 'Potenz: Barwert');
    ok(hoch('e^(2x²)') === 'e<sup>2x²</sup>' && hoch('a_7') === 'a<sub>7</sub>', 'Hoch-/Tiefzeichen werden gesetzt');
    { const pk = ['Planung, Steuerung und Kontrolle des Materialflusses', 'vom Lieferanten bis zum Kunden'];
      const t = kernpunkte('Man plant, lenkt und überwacht den Materialfluss vom Zulieferer zum Abnehmer.', pk);
      ok(t[0] && t[1], 'Kernpunkte: Synonyme werden erkannt');
      ok(!kernpunkte('Etwas ganz anderes über Werbung.', pk).some(Boolean), 'Kernpunkte: falscher Text trifft nicht');
      const tp = defTipps('Planung, Steuerung und Kontrolle des Materialflusses vom Lieferanten bis zum Kunden.', pk);
      ok(tp.length === 2 && /Planung/.test(tp[0]) && /Lieferanten/.test(tp[1]), 'Definitions-Tipps'); }
    if (typeof mfGleich === 'function') {
      ok(mfGleich('h^2/j', 'h^2*j^(-1)') && mfGleich('h²/j', 'h^2/j') && mfGleich('3ln(z)+3', '3*ln(z)+3'), 'Mathe-Feld: gleichwertige Terme');
      ok(!mfGleich('h/j', 'h^2/j') && !mfGleich('2x', 'x^2'), 'Mathe-Feld: verschiedene Terme');
      ok(mfGleich('2e^y(1+y)', '2*e^y+2y*e^y') && mfGleich('(1+2x)e^(x+x^2)', '(1+2x)*e^(x+x^2)'), 'Mathe-Feld: Malpunkt darf fehlen');
      ok(Math.abs(mfZahl('1.152,38') - 1152.38) < 1e-9 && Math.abs(mfZahl('11/3') - 11 / 3) < 1e-9 && Math.abs(mfZahl('e^0,6') - Math.exp(.6)) < 1e-9 && mfZahl('4,13') === 4.13, 'Mathe-Feld: Zahlen mit Komma, Bruch, e');
      ok(/\\frac/.test(mfLatex(mfParse('(a+b)^2/(2x)'))) && /\\cdot/.test(mfLatex(mfParse('3*x'))), 'Mathe-Feld: LaTeX-Vorschau');
      { const fr = x => (brueche(x).match(/class="fr"/g) || []).length;
        ok(fr('Ø Bestand = (AB + EB) ÷ 2') === 1 && /<span>AB \+ EB<\/span>/.test(brueche('(AB + EB) ÷ 2')), 'Bruch aus ÷ mit Klammer');
        ok(fr('ε = ∂Y/∂K · K/Y') === 2 && fr('Umsatz ÷ Gesamtkapital') === 1 && fr('f(x) = 1/x') === 1, 'kurze Brüche');
        ok(fr('und/oder') === 0 && fr('Preis in €/kWh') === 0 && fr('Ein-/Ausgang') === 0 && fr('<a href="x/y">a</a>') === 0 && fr('Stück/Tag') === 0, 'Text mit Schrägstrich bleibt Text');
        { const z = x => (brueche(x).match(/<span class="fr"><span>(.*?)<\/span><span>(.*?)<\/span><\/span>/) || []).slice(1).join(' | ');
          ok(z('LS = Lagerkosten · 100 ÷ Ø Lagerwert') === 'Lagerkosten · 100 | Ø Lagerwert', 'Bruch: Produkt im Zähler, Ø im Nenner (' + z('LS = Lagerkosten · 100 ÷ Ø Lagerwert') + ')');
          ok(z('ppm = fehlerhafte Teile ÷ gelieferte Teile · 1.000.000') === 'fehlerhafte Teile | gelieferte Teile', 'Bruch: Wortgruppen');
          ok(z('Die Umsatzrentabilität ist Gewinn ÷ Umsatz.') === 'Gewinn | Umsatz', 'Bruch: Satz bleibt Text');
          ok(z('Zinsen = Betrag · Zins ÷ 2 · Tage') === 'Betrag · Zins | 2' && fr('a + b ÷ c') === 1 && z('a + b ÷ c') === 'b | c', 'Bruch: Punkt vor Strich');
          ok(/r<sub>EK<\/sub>/.test(brueche('r_EK = 5')) && /class="wz"/.test(brueche('x = √(2 · M)')) && !/sub/.test(brueche('Ein-/Ausgang mc_multi_x')), 'Index und Wurzel');
          ok(z('v = (r<sub>EK</sub> − r<sub>GK</sub>) ÷ (r<sub>GK</sub> − i)') === 'r<sub>EK</sub> − r<sub>GK</sub> | r<sub>GK</sub> − i', 'Bruch über Index-Tags'); }
        ok(/katex/.test(schoen('Es gilt \\(\\frac{a}{b}\\) und a ÷ b')) && /class="fr"/.test(schoen('Es gilt \\(x\\) und a ÷ b')), 'schoen: Formeln und Brüche'); }
      ok(pruefeFeld({ typ: 'menge', loesung: [3, 9] }, [{ value: '{9, 3}' }]) && !pruefeFeld({ typ: 'menge', loesung: [3, 9] }, [{ value: '3' }]) && pruefeFeld({ typ: 'menge', loesung: null }, [{ value: 'nicht bestimmbar' }]), 'Mengen-Feld');
    }
    // Note nach DHBW-Tabelle (60 Punkte)
    for (const [h, n] of [[60, 1], [59.5, 1], [59, 1.1], [31, 3.9], [30.5, 3.9], [30, 4], [29.5, 4.1], [28.5, 4.1], [28, 4.2], [27, 4.3], [21, 4.9], [20.5, 4.9], [20, 5], [0, 5]]) ok(note(h, 60) === n, `Note ${h}/60 = ${note(h, 60)}, erwartet ${n}`);
    ok(note(90, 120) === note(45, 60), 'Note über Anteil umgerechnet');
    // Endlos: keine Wiederholung derselben Frage, solange die Auswahl noch offene Fragen hat (nur „nochmal“ nach Fehler)
    await LT.lade(['ling']);
    for (const richtig of [true, false]) {
      const pool = Object.values(TOP).filter(x => x.f.id === 'ling'), e = endlos(pool), res = [], seen = new Set();
      let wdh = 0;
      for (let i = 0; i < 80; i++) { const it = e.next(i, res); const k = it.fam.id + '#' + it.fam.a.indexOf(it.orig); if (!it.nochmal) { if (seen.has(k)) wdh++; seen.add(k); } res.push({ item: it, ok: richtig }); }
      if (wdh) f.push('Endlos: ' + wdh + ' Wiederholungen in 80 Fragen (' + (richtig ? 'richtig' : 'falsch') + ')');
    }
    return f;
  });
  await b.close();
  console.log(r.length ? r.join('\n') + `\n${r.length} Fehler` : 'Engine-Test ok: 0 Fehler');
  process.exit(r.length ? 1 : 0);
})();
