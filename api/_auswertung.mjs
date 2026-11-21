/* Auswertung aller Lernstände für den Admin-Bereich (ohne Codes).
   Name je Person: in der App eingetragener Name, sonst Notiz zum Code, sonst „Person n“ (n = Reihenfolge nach Erstellung des Codes). */
const TAG = 864e5;
/* Tage nach deutscher Ortszeit (wie in der App), nicht UTC */
const ortTag = ts => new Date(ts).toLocaleDateString('sv-SE', { timeZone: 'Europe/Berlin' });
const heute = () => ortTag(Date.now());
const tagMinus = n => ortTag(Date.now() - n * TAG);
/* Lernzeit aus Zeitstempeln schätzen (auch für Zeit vor der Minutenzählung): Aktionen mit höchstens 10 Minuten Abstand
   gehören zu einer Sitzung; jede Aktion zählt mindestens 1 Minute. Ergebnis je Tag: {m: Minuten, a: Aktionen} */
function ausStempeln(d) {
  const ts = [];
  const nimm = t => { const x = typeof t === 'number' ? t : Date.parse(t); if (x > 1.6e12 && x < Date.now() + TAG) ts.push(x); };
  for (const e of Object.values(d.g || {})) if (e && e.t) nimm(e.t);
  for (const p of Object.values(d.pruef || {})) if (p && p.d) nimm(p.d);
  for (const u of Object.values(d.unsicher || {})) if (u && u.t) nimm(u.t);
  for (const m of Array.isArray(d.meldungen) ? d.meldungen : []) if (m && m.d) nimm(m.d);
  ts.sort((a, b) => a - b);
  const tage = {};
  for (let i = 0; i < ts.length; i++) {
    const t = tage[ortTag(ts[i])] || (tage[ortTag(ts[i])] = { m: 0, a: 0 }); t.a++;
    const luecke = i ? ts[i] - ts[i - 1] : Infinity;
    t.m += luecke <= 10 * 6e4 ? luecke / 6e4 : 1;
  }
  for (const t of Object.values(tage)) t.m = Math.round(t.m);
  return tage;
}

export function auswerten(codes, staende, geraete = []) {
  const kontakt = {}; for (const g of geraete) if (g.zuletzt && String(g.zuletzt) > String(kontakt[g.code] || '')) kontakt[g.code] = g.zuletzt;
  const reihenfolge = [...codes].sort((a, b) => String(a.erstellt).localeCompare(String(b.erstellt)));
  const nr = new Map(reihenfolge.map((c, i) => [c.code, i + 1])), notiz = new Map(codes.map(c => [c.code, String(c.notiz || '').trim()]));
  const verlauf = {}, themen = {}, familien = {}, pruef = {}, meldungen = [], personen = [];
  for (let i = 0; i < 30; i++) verlauf[tagMinus(i)] = { personen: 0, minuten: 0, antworten: 0, richtig: 0, besuche: 0 };
  for (const z of staende) {
    const d = z.daten || {}, g = d.g || {}, appName = String((d.einst && d.einst.name) || '').trim().slice(0, 60), nz = notiz.get(z.code) || '',
      name = appName || nz || 'Person ' + (nr.get(z.code) || '?');
    /* Nutzung je Tag: Zählung der App (S.nutzung) und Schätzung aus Zeitstempeln, jeweils das Größere */
    const n = {}, st = ausStempeln(d);
    for (const [tag, t] of Object.entries(d.nutzung || {})) if (t && typeof t === 'object') n[tag] = { ...t };
    for (const [tag, s] of Object.entries(st)) { const t = n[tag] || (n[tag] = { b: 1, m: 0, a: 0, r: 0 }); t.m = Math.max(t.m || 0, s.m); t.a = Math.max(t.a || 0, s.a); t.b = Math.max(t.b || 0, 1); }
    const online = [z.geaendert, kontakt[z.code]].filter(Boolean).map(x => new Date(x).getTime()).reduce((a, b) => Math.max(a, b), 0) || null;
    if (online) { const t = n[ortTag(online)] || (n[ortTag(online)] = { b: 1, m: 0, a: 0, r: 0 }); t.m = Math.max(t.m || 0, 1); }
    let min = 0, bes = 0, ant = 0, ri = 0, tage = 0, letzter = '';
    const werkzeug = {};
    for (const [tag, t] of Object.entries(n)) {
      if (!t || typeof t !== 'object') continue;
      min += t.m || 0; bes += t.b || 0; ant += t.a || 0; ri += t.r || 0;
      if ((t.m || 0) + (t.a || 0) > 0) { tage++; if (tag > letzter) letzter = tag; }
      for (const [w, c] of Object.entries(t.w || {})) werkzeug[w] = (werkzeug[w] || 0) + c;
      const v = verlauf[tag]; if (v && (t.m || t.a)) { v.personen++; v.minuten += t.m || 0; v.antworten += t.a || 0; v.richtig += t.r || 0; v.besuche += t.b || 0; }
    }
    /* Stufen je Unterthema: Anteil „nicht gekonnt“ (Stufe 1) */
    const jeThema = {};
    for (const [id, e] of Object.entries(g)) {
      if (!e || !e.k || !e.s) continue;
      const t = jeThema[e.k] || (jeThema[e.k] = { n: 0, sum: 0, eins: 0 }); t.n++; t.sum += e.s; if (e.s === 1) t.eins++;
      if (id.startsWith('q:') && e.s === 1) { const fam = id.slice(2, id.lastIndexOf(':')); const f = familien[fam] || (familien[fam] = { k: e.k, personen: 0, faelle: 0 }); f.faelle++; f._p = f._p || new Set(); f._p.add(name); }
    }
    let rot = 0;
    for (const [k, t] of Object.entries(jeThema)) {
      const T = themen[k] || (themen[k] = { personen: 0, aufgaben: 0, nichtGekonnt: 0, stufenSumme: 0, rotBei: 0 });
      T.personen++; T.aufgaben += t.n; T.nichtGekonnt += t.eins; T.stufenSumme += t.sum;
      if (t.n >= 5 && t.sum / t.n < 1.5) { T.rotBei++; rot++; }
    }
    let gepr = 0, pSum = 0;
    for (const [k, p] of Object.entries(d.pruef || {})) {
      if (!p || typeof p.s !== 'number') continue; gepr++; pSum += p.s;
      const P = pruef[k] || (pruef[k] = { personen: 0, summe: 0 }); P.personen++; P.summe += p.s;
    }
    for (const m of Array.isArray(d.meldungen) ? d.meldungen : []) meldungen.push({ person: name, d: m.d, ort: m.ort, sel: m.sel || '', text: m.text });
    const pv = {}; for (let i = 0; i < 60; i++) { const t = tagMinus(i), x = n[t]; if (x && (x.m || x.a)) pv[t] = { m: x.m || 0, a: x.a || 0, r: x.r || 0, b: x.b || 0 }; }
    const pth = {}; for (const [k, t] of Object.entries(jeThema)) pth[k] = [t.n, t.sum, t.eins];
    const ppr = {}; for (const [k, p] of Object.entries(d.pruef || {})) if (p && typeof p.s === 'number') ppr[k] = { s: p.s, d: p.d || null, h: p.h || 4 };
    personen.push({ person: name, appName, notiz: nz, nr: nr.get(z.code) || 0, richtig: ri, verlauf: pv, themen: pth, pruefStand: ppr,
      meldungen: (Array.isArray(d.meldungen) ? d.meldungen : []).map(m => ({ d: m.d, ort: m.ort, sel: m.sel || '', text: m.text })), letzterTag: letzter || null, tageAktiv: tage, minuten: min, besuche: bes, antworten: ant,
      quote: ant ? Math.round(ri / ant * 100) : null, minutenJeTag: tage ? Math.round(min / tage) : 0, aufgabenBearbeitet: Object.keys(g).length,
      roteThemen: rot, geprueft: gepr, pruefSchnitt: gepr ? Math.round(pSum / gepr) : null, werkzeug, zuletztGespeichert: z.geaendert,
      zuletztOnline: online });
  }
  personen.sort((a, b) => a.nr - b.nr);
  const aktivSeit = t => personen.filter(p => p.letzterTag && p.letzterTag >= t).length;
  const schwer = Object.entries(themen).map(([k, t]) => ({ k, ...t, anteil: t.aufgaben ? Math.round(t.nichtGekonnt / t.aufgaben * 100) : 0, schnitt: t.aufgaben ? +(t.stufenSumme / t.aufgaben).toFixed(2) : 0 }))
    .filter(t => t.aufgaben >= 5).sort((a, b) => b.anteil - a.anteil || b.personen - a.personen).slice(0, 25);
  const famTop = Object.entries(familien).map(([id, f]) => ({ id, k: f.k, personen: f._p.size, faelle: f.faelle }))
    .sort((a, b) => b.personen - a.personen || b.faelle - a.faelle).slice(0, 25);
  meldungen.sort((a, b) => String(b.d).localeCompare(String(a.d)));
  const nutzer = personen.filter(p => p.aufgabenBearbeitet || p.minuten).length;
  return {
    stand: new Date().toISOString(),
    gesamt: { codes: codes.length, mitLernstand: staende.length, nutzer, aktivHeute: aktivSeit(heute()), aktiv7: aktivSeit(tagMinus(6)), aktiv30: aktivSeit(tagMinus(29)),
      minuten: personen.reduce((s, p) => s + p.minuten, 0), antworten: personen.reduce((s, p) => s + p.antworten, 0),
      quote: (() => { const a = personen.reduce((s, p) => s + p.antworten, 0); const r = personen.reduce((s, p) => s + (p.quote != null ? p.quote * p.antworten / 100 : 0), 0); return a ? Math.round(r / a * 100) : null; })(),
      meldungen: meldungen.length },
    verlauf: Object.entries(verlauf).sort((a, b) => a[0].localeCompare(b[0])).map(([tag, v]) => ({ tag, ...v })),
    personen, schwer, familien: famTop,
    pruef: Object.entries(pruef).map(([k, p]) => ({ k, personen: p.personen, schnitt: Math.round(p.summe / p.personen) })).sort((a, b) => a.schnitt - b.schnitt),
    meldungen: meldungen.slice(0, 300),
  };
}

/* Geist-Ansicht: Code der Person n (Reihenfolge nach Erstellung) */
export function geistDaten(codes, nrWunsch) {
  const reihenfolge = [...codes].sort((a, b) => String(a.erstellt).localeCompare(String(b.erstellt)));
  return reihenfolge[nrWunsch - 1] ? reihenfolge[nrWunsch - 1].code : null;
}
