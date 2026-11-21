/* ---------- Online-Abgleich des Lernstands (nur in der Online-Version mit /api; im Artifact und lokal inaktiv) ----------
   Prinzip: „basis“ ist der zuletzt vom Server bekannte Stand (flach: „abschnitt/schlüssel“ → JSON).
   Lokale Änderungen = Unterschied zwischen S und basis; sie gehen als Patch an den Server, der sie in seinen Stand
   einfügt. Geänderte Einträge gewinnen also je Schlüssel – zwei Geräte überschreiben sich nicht gegenseitig. */
const SYNC = { an: false, basis: null, timer: 0, laeuft: false, nochmal: false, code: '', geraet: '', geraete: [], zuletzt: 0, fehler: '' };
const SYNC_KEY = 'lerntool-sync';
const SYNC_GERAET = new Set(['uhr', 'einst/testTage', 'einst/theme']);   // bleibt auf dem Gerät
const SYNC_GANZ = new Set(['zuletzt', 'v']);                                // wird als Ganzes übernommen

function syncFlach(o) {
  const m = {};
  for (const [a, v] of Object.entries(o || {})) {
    if (SYNC_GERAET.has(a)) continue;
    if (v && typeof v === 'object' && !Array.isArray(v) && !SYNC_GANZ.has(a)) {
      for (const [k, w] of Object.entries(v)) if (!SYNC_GERAET.has(a + '/' + k) && w !== undefined) m[a + '/' + k] = JSON.stringify(w);
    } else if (v !== undefined) m[a] = JSON.stringify(v);
  }
  return m;
}
function syncDiff(jetzt, ref) {
  const p = {};
  for (const [k, v] of Object.entries(jetzt)) if (ref[k] !== v) p[k] = JSON.parse(v);
  for (const k of Object.keys(ref)) if (!(k in jetzt)) p[k] = null;
  return p;
}
function syncAnwenden(daten, patch) {   // wie wendeAn auf dem Server
  const d = JSON.parse(JSON.stringify(daten || {}));
  for (const [pfad, wert] of Object.entries(patch)) {
    const i = pfad.indexOf('/');
    if (i < 0) { if (wert === null) delete d[pfad]; else d[pfad] = wert; continue; }
    const a = pfad.slice(0, i), k = pfad.slice(i + 1);
    if (!d[a] || typeof d[a] !== 'object' || Array.isArray(d[a])) d[a] = {};
    if (wert === null) delete d[a][k]; else d[a][k] = wert;
  }
  return d;
}
function syncMerkeBasis(flach) {
  SYNC.basis = flach;
  try { localStorage.setItem(SYNC_KEY, JSON.stringify({ basis: flach })); } catch (e) { }
}
/* Serverstand übernehmen, lokale (noch nicht gesendete) Änderungen gegenüber ref obendrauf */
function syncUebernehme(server, ref) {
  const vorher = JSON.stringify(S), lokal = syncDiff(syncFlach(S), ref);
  const neu = syncAnwenden(server, lokal);
  const bleibt = { uhr: S.uhr, testTage: S.einst && S.einst.testTage, theme: S.einst && S.einst.theme };
  for (const k of Object.keys(S)) delete S[k];
  Object.assign(S, neu);
  S.v = 1;
  for (const k of ['pruef', 'wackel', 'zuletztF', 'einst', 'mark', 'notiz', 'g', 'ks', 'eigen', 'unsicher', 'nutzung', 'uaus']) S[k] = S[k] && typeof S[k] === 'object' ? S[k] : {};
  if (bleibt.uhr) S.uhr = bleibt.uhr;
  if (bleibt.testTage != null) S.einst.testTage = bleibt.testTage;
  if (bleibt.theme != null) S.einst.theme = bleibt.theme;
  syncMerkeBasis(syncFlach(server));
  try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) { }
  return { geaendert: JSON.stringify(S) !== vorher, offen: Object.keys(lokal).length > 0 };
}

async function syncAbruf(url, opt = {}) {
  const r = await fetch(url, { credentials: 'same-origin', cache: 'no-store', ...opt, headers: { 'content-type': 'application/json', ...(opt.headers || {}) } });
  if (r.status === 401) { SYNC.an = false; location.href = '/login.html?abgemeldet=1'; throw new Error('abgemeldet'); }
  const j = await r.json().catch(() => ({}));
  if (!r.ok) throw new Error(j.fehler || 'http ' + r.status);
  return j;
}

async function syncHolen(neuZeichnen) {
  const j = await syncAbruf('/api/stand');
  SYNC.an = true; SYNC.code = j.code; SYNC.geraet = j.geraet; SYNC.geraete = j.geraete || [];
  if (j.name && j.name !== SYNC.name) { SYNC.name = j.name; if (typeof nameAuffrischen === 'function') nameAuffrischen(); }
  const e = syncUebernehme(j.daten || {}, SYNC.basis || {});
  SYNC.zuletzt = Date.now(); SYNC.fehler = '';
  if (e.offen) syncPlan(200);
  if (e.geaendert && neuZeichnen && typeof render === 'function') render();
}

async function syncSenden() {
  if (!SYNC.an) return;
  if (SYNC.laeuft) { SYNC.nochmal = true; return; }
  const gesendet = syncFlach(S), patch = syncDiff(gesendet, SYNC.basis || {});
  if (!Object.keys(patch).length) return;
  SYNC.laeuft = true;
  try {
    const j = await syncAbruf('/api/stand', { method: 'PUT', body: JSON.stringify({ patch }), keepalive: JSON.stringify(patch).length < 60000 });
    syncUebernehme(j.daten || {}, gesendet);
    SYNC.zuletzt = Date.now(); SYNC.fehler = '';
  } catch (e) {
    SYNC.fehler = 'Gerade offline – wird später gespeichert.';
    syncPlan(30000);
  } finally {
    SYNC.laeuft = false;
    if (SYNC.nochmal) { SYNC.nochmal = false; syncPlan(500); }
  }
}
function syncPlan(ms = 2500) {
  if (!SYNC.an) return;
  clearTimeout(SYNC.timer);
  SYNC.timer = setTimeout(syncSenden, ms);
}
/* Tab wird verlassen: offene Änderungen (z. B. Lernminuten) sofort senden */
document.addEventListener('visibilitychange', () => { if (document.visibilityState === 'hidden' && SYNC.an) syncSenden(); });
/* wird von save() in kern.js aufgerufen */
function syncNachSpeichern() { syncPlan(); }

function syncEinstHTML() {
  if (!SYNC.an) return '';
  const zeit = t => t ? new Date(t).toLocaleDateString('de-DE', { day: 'numeric', month: 'short' }) : '';
  return `<section class="tile"><h2>Konto</h2>
    <p class="dim3">Dein Lernstand wird online gespeichert und erscheint auf jedem Gerät, auf dem du diesen Code eingibst (höchstens 3).${SYNC.fehler ? ' ' + esc(SYNC.fehler) : ''}</p>
    <p class="ein-zeile">Dein Code <b>${esc(SYNC.code)}</b></p>
    <ul class="sync-geraete">${SYNC.geraete.map(g => `<li><span>${esc(g.name)}${g.geraet === SYNC.geraet ? ' <em>(dieses Gerät)</em>' : ''}</span><small>${zeit(g.zuletzt)}</small>${g.geraet === SYNC.geraet ? '' : `<button class="btn" data-sync="weg" data-v="${esc(g.geraet)}">Abmelden</button>`}</li>`).join('')}</ul>
    <button class="btn" data-sync="raus">Auf diesem Gerät abmelden</button></section>`;
}

document.addEventListener('click', async ev => {
  const b = ev.target.closest('[data-sync]'); if (!b) return;
  ev.preventDefault();
  if (b.dataset.sync === 'weg') {
    await syncAbruf('/api/logout', { method: 'POST', body: JSON.stringify({ geraet: b.dataset.v }) }).catch(() => { });
    await syncHolen(false).catch(() => { }); render();
  }
  if (b.dataset.sync === 'raus') {
    if (!b.dataset.sicher) { b.dataset.sicher = '1'; b.textContent = 'Wirklich abmelden? Dein Lernstand bleibt online.'; return; }
    await syncSenden();
    await fetch('/api/logout', { method: 'POST', credentials: 'same-origin' }).catch(() => { });
    try { localStorage.removeItem(SYNC_KEY); localStorage.removeItem(KEY); } catch (e) { }
    location.href = '/login.html';
  }
});

/* Start: nur wenn die Seite über http(s) von unserer Online-Version kommt */
(function syncStart() {
  if (window.LT_INDEX && LT_INDEX.semester && LT_INDEX.semester.login === false) return;   // Website ohne Login-Codes: Lernstand bleibt im Browser
  if (typeof GEIST !== 'undefined' && GEIST) return;   // Geist-Ansicht: kein Abgleich
  if (!/^https?:$/.test(location.protocol) || /claude|usercontent/.test(location.hostname) || !location.pathname.match(/^\/(index\.html)?$/)) return;
  try { SYNC.basis = (JSON.parse(localStorage.getItem(SYNC_KEY)) || {}).basis || null; } catch (e) { }
  syncHolen(true).catch(() => { });
  document.addEventListener('visibilitychange', () => {
    if (!SYNC.an) return;
    if (document.visibilityState === 'hidden') syncSenden();
    else if (Date.now() - SYNC.zuletzt > 60000) syncHolen(V.screen === 'dash' || V.screen === 'einst').catch(() => { });
  });
  window.addEventListener('pagehide', () => { if (SYNC.an) syncSenden(); });
})();
