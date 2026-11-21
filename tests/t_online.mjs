/* Online-Version: API-Funktionen gegen ein nachgebautes Supabase (im Speicher) + Abgleich zweier Geräte im Browser-Code. */
import fs from 'node:fs';
import vm from 'node:vm';

let fehler = 0;
const ok = (b, t) => { if (!b) { fehler++; console.log('FEHLER: ' + t); } };

process.env.SUPABASE_URL = 'https://test.supabase.co';
process.env.SUPABASE_SERVICE_KEY = 'service';
process.env.SITZUNG_GEHEIMNIS = 'ein-sehr-langes-testgeheimnis-123456';
process.env.ADMIN_PASSWORT = 'admin-passwort-1';
process.env.LOGIN = 'an';   // dieser Test prüft die Variante mit Login-Codes

/* ---------- Mini-PostgREST ---------- */
const DB = { codes: [], geraete: [], lernstand: [] };
const PK = { codes: ['code'], geraete: ['code', 'geraet'], lernstand: ['code'] };
globalThis.fetch = async (url, opt = {}) => {
  const u = new URL(url), tab = u.pathname.split('/').pop(), m = opt.method || 'GET';
  ok(opt.headers.apikey === 'service', 'Service-Schlüssel wird mitgeschickt');
  const filter = [...u.searchParams].filter(([k]) => !['select', 'order', 'on_conflict'].includes(k));
  const passt = z => filter.every(([k, v]) => String(z[k]) === decodeURIComponent(v.replace(/^eq\./, '')));
  const body = opt.body ? JSON.parse(opt.body) : null, prefer = opt.headers.prefer || '';
  const antw = (x, s = 200) => new Response(x === undefined ? null : JSON.stringify(x), { status: s });
  const zeilen = DB[tab];
  if (m === 'GET') {
    let r = zeilen.filter(passt).map(z => ({ ...z }));
    const o = u.searchParams.get('order'); if (o) { const [f, d] = o.split('.'); r.sort((a, b) => (a[f] < b[f] ? -1 : 1) * (d === 'desc' ? -1 : 1)); }
    return antw(r);
  }
  if (m === 'POST') {
    const neu = [];
    for (const z of [].concat(body)) {
      const dup = zeilen.find(x => PK[tab].every(k => x[k] === z[k]));
      if (dup) { if (prefer.includes('ignore-duplicates')) continue; return antw({ message: 'duplicate' }, 409); }
      const v = { erstellt: new Date().toISOString(), gesperrt: false, notiz: '', ...z }; zeilen.push(v); neu.push(v);
    }
    return prefer.includes('return=representation') ? antw(neu, 201) : antw(undefined, 201);
  }
  if (m === 'PATCH') { const r = zeilen.filter(passt); r.forEach(z => Object.assign(z, body)); return prefer.includes('return=representation') ? antw(r) : antw(undefined, 204); }
  if (m === 'DELETE') { DB[tab] = zeilen.filter(z => !passt(z)); return antw(undefined, 204); }
};

const login = await import('../api/login.mjs'), stand = await import('../api/stand.mjs'), admin = await import('../api/admin.mjs'), logout = await import('../api/logout.mjs');
const lib = await import('../api/_lib.mjs');
const anfrage = (pfad, method, body, cookie) => new Request('https://lern.test' + pfad, { method, body: body ? JSON.stringify(body) : undefined, headers: { 'content-type': 'application/json', ...(cookie ? { cookie } : {}) } });
const keks = r => (r.headers.get('set-cookie') || '').split(';')[0];

/* Verwaltung */
ok((await admin.POST(anfrage('/api/admin', 'POST', { passwort: 'falsch', aktion: 'liste' }))).status === 401, 'falsches Admin-Passwort abgelehnt');
const erz = await (await admin.POST(anfrage('/api/admin', 'POST', { passwort: 'admin-passwort-1', aktion: 'erzeugen', anzahl: 2, notiz: 'Lena' }))).json();
ok(erz.codes.length === 2 && /^[A-Z0-9]{5}-[A-Z0-9]{5}$/.test(erz.codes[0]), 'zwei Codes im Format XXXXX-XXXXX');
ok(!/[01OIL]/.test(erz.codes.join('')), 'keine verwechselbaren Zeichen');
const CODE = erz.codes[0];

/* Anmeldung */
ok((await login.POST(anfrage('/api/login', 'POST', { code: 'ABCDE-FGHJK', geraet: 'geraet-aaaa1' }))).status === 401, 'unbekannter Code abgelehnt');
const r1 = await login.POST(anfrage('/api/login', 'POST', { code: CODE.toLowerCase(), geraet: 'geraet-laptop', name: 'Mac · Safari' }));
ok(r1.status === 200 && keks(r1).startsWith('lt_sitzung='), 'Anmeldung (auch klein geschrieben) setzt Cookie');
ok(/HttpOnly/.test(r1.headers.get('set-cookie')) && /Secure/.test(r1.headers.get('set-cookie')), 'Cookie HttpOnly und Secure');
const K1 = keks(r1);
const K2 = keks(await login.POST(anfrage('/api/login', 'POST', { code: CODE, geraet: 'geraet-handy', name: 'iPhone · Safari' })));
await login.POST(anfrage('/api/login', 'POST', { code: CODE, geraet: 'geraet-ipad1', name: 'iPad · Safari' }));
const voll = await login.POST(anfrage('/api/login', 'POST', { code: CODE, geraet: 'geraet-viertes', name: 'Windows · Edge' }));
const vj = await voll.json();
ok(voll.status === 409 && vj.fehler === 'voll' && vj.geraete.length === 3, 'viertes Gerät: Liste der drei Geräte');
ok((await login.POST(anfrage('/api/login', 'POST', { code: CODE, geraet: 'geraet-viertes', name: 'Windows · Edge', entfernen: 'geraet-ipad1' }))).status === 200, 'altes Gerät abmelden, dann geht es');

/* Middleware-Logik und Fälschungen */
ok(!!(await lib.sitzung(anfrage('/', 'GET', null, K1))), 'gültiges Cookie erkannt');
const gefaelscht = K1.replace(/\.[^.]+$/, '.AAAA');
ok(!(await lib.sitzung(anfrage('/', 'GET', null, gefaelscht))), 'gefälschte Signatur abgelehnt');
const mw = (await import('../middleware.js')).default;
ok((await mw(anfrage('/daten/ling.js', 'GET'))).status === 302, 'ohne Anmeldung: Umleitung zur Anmeldeseite');
ok((await mw(anfrage('/daten/ling.js', 'GET', null, K1))) === undefined, 'mit Anmeldung: Datei wird ausgeliefert');

/* Lernstand */
const g0 = await (await stand.GET(anfrage('/api/stand', 'GET', null, K1))).json();
ok(g0.version === 0 && g0.code === CODE && g0.geraete.length === 3, 'leerer Lernstand, Code und Geräte');
let p = await (await stand.PUT(anfrage('/api/stand', 'PUT', { patch: { 'g/q:a:mc': { s: 2 }, 'mark/logistik/x': [{ id: 1 }] } }, K1))).json();
ok(p.version === 1 && p.daten.g['q:a:mc'].s === 2, 'erste Änderung gespeichert');
p = await (await stand.PUT(anfrage('/api/stand', 'PUT', { patch: { 'g/q:b:mc': { s: 4 }, 'mark/logistik/x': null } }, K2))).json();
ok(p.version === 2 && p.daten.g['q:a:mc'].s === 2 && p.daten.g['q:b:mc'].s === 4 && !p.daten.mark.logistik_x && !('logistik/x' in p.daten.mark), 'zweites Gerät: beide Änderungen erhalten, Löschung wirkt');
await logout.POST(anfrage('/api/logout', 'POST', { geraet: 'geraet-handy' }, K1));
ok((await stand.GET(anfrage('/api/stand', 'GET', null, K2))).status === 401, 'abgemeldetes Gerät kommt nicht mehr an den Lernstand');
await admin.POST(anfrage('/api/admin', 'POST', { passwort: 'admin-passwort-1', aktion: 'sperren', code: CODE, gesperrt: true }));
ok((await stand.GET(anfrage('/api/stand', 'GET', null, K1))).status === 401, 'gesperrter Code kommt nicht an den Lernstand');
const li = await (await admin.POST(anfrage('/api/admin', 'POST', { passwort: 'admin-passwort-1', aktion: 'liste' }))).json();
ok(li.codes.length === 2 && li.codes.some(c => c.gesperrt && c.geraete.length >= 1 && c.geaendert), 'Liste mit Geräten, Sperre und letzter Änderung');

/* ---------- Browser-Abgleich: zwei Geräte arbeiten offline und gleichen dann ab ---------- */
function geraet(server) {
  const ls = {};
  const ctx = { console, JSON, Object, Date, setTimeout: () => 0, clearTimeout: () => { }, confirm: () => true,
    localStorage: { getItem: k => ls[k] ?? null, setItem: (k, v) => { ls[k] = v; }, removeItem: k => { delete ls[k]; } },
    location: { protocol: 'file:', hostname: '', pathname: '/x' }, document: { addEventListener() { } }, window: { addEventListener() { } },
    esc: s => s, render: () => { ctx.gezeichnet++; }, gezeichnet: 0 };
  ctx.fetch = async (url, opt = {}) => {
    if (opt.method === 'PUT') { server.daten = JSON.parse(JSON.stringify(server.daten)); const pt = JSON.parse(opt.body).patch; server.daten = lib.wendeAn(server.daten, pt); server.version++; }
    return { status: 200, ok: true, json: async () => ({ daten: JSON.parse(JSON.stringify(server.daten)), version: server.version, code: 'X', geraet: 'g', geraete: [] }) };
  };
  vm.createContext(ctx);
  vm.runInContext(`const KEY = 'lerntool-v1'; let S = { v: 1, pruef: {}, wackel: {}, zuletztF: {}, einst: { theme: 'dark' }, mark: {}, notiz: {}, g: {}, ks: {}, uhr: { rest: 5 } }; const V = { screen: 'dash' };`
    + fs.readFileSync(new URL('../app/js/sync.js', import.meta.url), 'utf8') + `;this.S = S; this.SYNC = SYNC; this.syncHolen = syncHolen; this.syncSenden = syncSenden;`, ctx);
  return ctx;
}
const SERVER = { daten: {}, version: 0 };
const A = geraet(SERVER), B = geraet(SERVER);
A.S.g['q:1'] = { s: 4 }; A.S.notiz['logistik/a'] = 'Notiz A';
await A.syncHolen(true); await A.syncSenden();
ok(SERVER.daten.g['q:1'].s === 4 && SERVER.daten.notiz['logistik/a'] === 'Notiz A', 'Gerät A: alter lokaler Stand wandert beim ersten Abgleich auf den Server');
ok(!('uhr' in SERVER.daten) && !('theme' in (SERVER.daten.einst || {})), 'Timer und Farbschema bleiben auf dem Gerät');
B.S.g['q:2'] = { s: 1 };
await B.syncHolen(true); await B.syncSenden();
ok(B.S.g['q:1'].s === 4 && B.S.g['q:2'].s === 1 && B.S.notiz['logistik/a'] === 'Notiz A', 'Gerät B: bekommt Stand von A und behält eigenen');
ok(B.S.einst.theme === 'dark' && B.S.uhr.rest === 5, 'Gerät B: eigene Geräteeinstellungen bleiben');
A.S.g['q:1'] = { s: 2 }; delete A.S.notiz['logistik/a'];
B.S.g['q:3'] = { s: 3 };
await A.syncSenden(); await B.syncSenden();
await A.syncHolen(true);
ok(B.S.g['q:1'].s === 2 && !B.S.notiz['logistik/a'] && B.S.g['q:3'].s === 3, 'gleichzeitige Änderungen: B übernimmt A (Stufe, gelöschte Notiz) und behält q:3');
ok(A.S.g['q:3'].s === 3 && A.S.g['q:2'].s === 1, 'A sieht nach dem Holen die Änderungen von B');
ok(A.gezeichnet > 0, 'nach dem Holen wird neu gezeichnet');

console.log(fehler ? `Online-Test: ${fehler} Fehler` : 'Online-Test ok: 0 Fehler');
process.exit(fehler ? 1 : 0);
