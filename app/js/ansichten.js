/* LernTool · Ansichten: Router (Adresse je Ansicht), Heute, Lernen, Sandbox, Prüfung, Einstellungen.
   Logik und Werkzeuge kommen aus kern.js; Schaubilder laufen über laufzeit.js (LT_nachRender). */
'use strict';

/* ---------- Konstanten ---------- */
const IC = {
  blur: '<svg viewBox="0 0 24 24"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/><path d="M4 20 20 4"/></svg>',
  karten: '<svg viewBox="0 0 24 24"><rect x="3" y="6" width="14" height="14" rx="2"/><path d="M7 3h12a2 2 0 0 1 2 2v12"/></svg>',
  quiz: '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6V14"/><circle cx="12" cy="17.3" r=".6"/></svg>',
  wackel: '<svg viewBox="0 0 24 24"><path d="M5 21V4h11l-2 4 2 4H5"/></svg>',
  uaus: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 3l18 18M10.6 6.2A9.8 9.8 0 0 1 12 6c5 0 8.5 4 9.5 6-.4.9-1.3 2.2-2.6 3.4M6.3 7.7C4.4 9 3.1 10.8 2.5 12c1 2 4.5 6 9.5 6 1.3 0 2.5-.3 3.6-.7M9.9 9.9a3 3 0 0 0 4.2 4.2"/></svg>',
  sandbox: '<svg viewBox="0 0 24 24"><path d="M4 20h16M6 20l2-8h8l2 8M9 12V6l3-2 3 2v6"/></svg>',
  home: '<svg viewBox="0 0 24 24"><path d="M3 11 12 4l9 7v9H3z"/></svg>',
  lern: '<svg viewBox="0 0 24 24"><path d="M4 5h7a2 2 0 0 1 2 2v13a2 2 0 0 0-2-2H4zM20 5h-7"/><path d="M13 7a2 2 0 0 1 2-2h5v13h-5a2 2 0 0 0-2 2"/></svg>',
  pfeil: '<svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
  markiert: '<svg viewBox="0 0 24 24"><path d="M4 20h6M14.5 4.5l5 5L10 19H5v-5z"/></svg>',
  suche: '<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/></svg>',
  einst: '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1 7 17M17 7l2.1-2.1"/></svg>',
};
const TOOLS = [['drill', 'Definitions-Drill', 'Begriffe und Definitionen, bis sie sitzen'], ['swipe', 'Karteikarten', 'umdrehen, gewusst oder nicht, wie bei Quizlet'],
  ['quiz', 'Endlos-Quiz', 'einfache Fragen schnell hintereinander'], ['blatt', 'Arbeitsblatt', 'Aufgaben wie in der Klausur, mit Rettungsringen']];
/* Training nach Lernziel: Verstehen · Merken · Können (Konzept 06.11.) */
const ZIELE = [['v', 'Verstehen', 'Schnell hintereinander, bis es klar ist.', ['quiz']], ['m', 'Merken', 'Auswendig können. Es wird gemerkt, was sitzt.', ['drill', 'swipe']], ['k', 'Können', 'Aufgaben wie in der Klausur, mit Hilfen.', ['blatt']]];
const ZIEL_VON = { quiz: 'v', drill: 'm', swipe: 'm', blatt: 'k' };
const WAS_DRIN = { quiz: 'Auswahl, richtig/falsch, Zuordnen, Reihenfolge, Schaubild beschriften, Nennen, Kopfrechnen. Erklären und Definieren sind im Drill, lange Aufgaben im Arbeitsblatt.',
  drill: 'Definieren und Erklären. „Auswählen“: Welcher Begriff passt? „Selbst schreiben“: Definition oder Erklärung in eigenen Worten, die Kernpunkte werden erkannt. Aufzählungen und Formeln sind bei den Karteikarten.',
  swipe: 'Begriffe, Merksätze und deine grün markierten Stellen. Was du nicht wusstest, kommt in der nächsten Runde wieder, bis alles sitzt.',
  blatt: 'Rechnen, Anwenden, Transfer, Zeichnen bis zu großen Aufgaben a–d. Rettungsring 1 und 2, dann die Lösung. Prozent gibt es nur in der Übungsklausur.',
  methodisch: 'Alles, was du irgendwo nicht auf Anhieb konntest, im Originalformat. Zuerst frische Fehler, dann was am ehesten vergessen ist. Jederzeit aufhören.' };
const SEITEN_SB = ['drill', 'swipe', 'quiz', 'blatt', 'methodisch'];
const TOOL_IC = {
  drill: '<svg viewBox="0 0 24 24"><path d="M13 2 4 14h7l-1 8 9-12h-7z"/></svg>',
  swipe: '<svg viewBox="0 0 24 24"><rect x="7" y="4" width="10" height="15" rx="2"/><path d="M3 9 1 11.5 3 14M21 9l2 2.5-2 2.5"/></svg>',
  quiz: '<svg viewBox="0 0 24 24"><path d="M6.5 8.5c-2 0-3.5 1.6-3.5 3.5s1.5 3.5 3.5 3.5c3.5 0 7.5-7 11-7 2 0 3.5 1.6 3.5 3.5s-1.5 3.5-3.5 3.5c-3.5 0-7.5-7-11-7z"/></svg>',
  blatt: '<svg viewBox="0 0 24 24"><path d="M6 3h9l4 4v14H6z"/><path d="M15 3v4h4M9 11h7M9 15h7M9 19h4"/></svg>',
};
const BUNT = ['#ffd23f', '#ff9ec7', '#8fd3ff', '#b8f28b', '#ffb38a', '#c7b6ff'];
const SPRUECHE = [
  'Fehler beim Üben sind kostenlos. In der Klausur nicht.', 'Ein Unterthema reicht für jetzt. Der Rest wartet.',
  'Verstehen hält länger als Auswendiglernen.', 'Fünf Minuten zählen. Fang einfach an.',
  'Was wackelt, ist nicht verloren, nur noch nicht fertig.', 'Erklär es so, dass es dein Mitbewohner versteht.',
  'Jeden Tag ein bisschen schlägt eine Nacht vor der Klausur.', 'Formel hinschreiben, einsetzen, Einheit dran. Das gibt Punkte.',
  'Wer verdeckt und trotzdem weiß, weiß es wirklich.', 'Pausen gehören zum Lernen dazu.',
];
let spruchI = Math.floor(Math.random() * SPRUECHE.length);

/* ---------- Ansichts-Zustand ---------- */
const V = { screen: 'dash', fid: D.faecher[0].id, kid: D.faecher[0].kapitel[0].id, tid: D.faecher[0].kapitel[0].topics[0].id,
  lang: 'en', blur: false, quizOffen: false, flip: {}, sbAuf: {}, sb: { f: [], k: [], wackel: false, tool: 'drill', modus: 'frei', seite: null }, pr: null };
if (S.zuletzt && TOP[S.zuletzt.fid + '/' + S.zuletzt.tid]) Object.assign(V, { fid: S.zuletzt.fid, kid: S.zuletzt.kid, tid: S.zuletzt.tid });
V.sb.f = [V.fid]; V.sb.wichtig = !!S.einst.wichtig; V.sb.stufe = S.einst.stufe || 'klausur'; V.sb.arten = S.einst.arten || ARTEN.map(a => a[0]);

/* ---------- Helfer ---------- */
const cur = () => TOP[V.fid + '/' + V.tid];
const goLern = (fid, kid, tid) => `data-go="lern|${fid}|${kid}|${tid || ''}"`;
function nachbarn() { const x = cur(), ts = x.k.topics, i = ts.indexOf(x.t), da = t => !uAus(x.f.id + '/' + t.id), next = ts.slice(i + 1).find(da);
  return { i, n: ts.length, prev: ts.slice(0, i).reverse().find(da) || ts[i - 1], next, letztes: !next }; }   // ausgeblendete Unterthemen überspringen
const kapWackel = (f, k) => k.topics.filter(t => istWackel(f.id + '/' + t.id)).length;
function ober(fid, k) {
  const st = stand(fid, k.id), w = kapWackel(F[fid], k);
  const cls = !st ? 'neu' : st.faellt ? 'blass' : st.s < 100 ? 'teil' : 'frisch';
  return { st, w, cls, fertig: kapFertig(F[fid], k), aus: kapAusZahl(F[fid], k), txt: !st ? 'ungeprüft' : st.faellt ? `verblasst · ${st.pct} %` : `${st.pct} %` };
}
/* Häkchen „Oberthema fertig“: alle eingeblendeten Unterthemen grün; ausgeblendete zählen nicht mit */
const fertigMarke = o => o.fertig ? `<span class="k-fertig" title="Oberthema fertig: alle eingeblendeten Unterthemen sind grün${o.aus ? ` (${o.aus} ausgeblendet)` : ''}">✓</span>` : '';
function faelligListe() {
  const out = [];
  for (const f of D.faecher) for (const k of f.kapitel) { const st = stand(f.id, k.id); if (st && st.refresh) out.push({ f, k, st }); }
  return out.sort((a, b) => a.st.pct - b.st.pct);
}
function zuletztIn(fid) { const z = S.zuletztF[fid], x = z && TOP[fid + '/' + z.tid]; return x || { f: F[fid], k: F[fid].kapitel[0], t: F[fid].kapitel[0].topics[0] }; }
function zuletzt() { const z = S.zuletzt && TOP[S.zuletzt.fid + '/' + S.zuletzt.tid]; return z || null; }
function klausurInfo(fid) { const k = klausurVon(fid); return k ? { k, tage: tageBis(k.beginn), datum: datumKurz(k.beginn), uhr: uhr(k.beginn), gew: gewichte(k) } : null; }
const badges = t => (t.aus ? '<span class="bdg bdg-aus">Kommt nicht dran</span>' : t.w || t.star ? '<span class="bdg bdg-star">★ Wichtig!</span>' : '');
function segRing(f, size = 168, sw = 14) {
  const n = f.kapitel.length, r = 70, c = 90, gap = n > 10 ? 2.2 : 4;
  const arc = (a0, a1) => { const p = a => [c + r * Math.sin(a * Math.PI / 180), c - r * Math.cos(a * Math.PI / 180)]; const [x0, y0] = p(a0), [x1, y1] = p(a1); return `M${x0.toFixed(2)} ${y0.toFixed(2)}A${r} ${r} 0 ${a1 - a0 > 180 ? 1 : 0} 1 ${x1.toFixed(2)} ${y1.toFixed(2)}`; };
  return `<svg class="segring" viewBox="0 0 180 180" width="${size}" height="${size}" role="img" aria-label="Prüfungsstand je Oberthema">${f.kapitel.map((k, i) => {
    const o = ober(f.id, k), a0 = i * 360 / n + gap / 2, a1 = (i + 1) * 360 / n - gap / 2;
    return `<path d="${arc(a0, a1)}" style="fill:none;stroke:currentColor;stroke-opacity:${o.st ? (.25 + .75 * o.st.pct / 100).toFixed(2) : .14}" stroke-width="${sw}"><title>${esc(k.title)}: ${o.txt}</title></path>`;
  }).join('')}</svg>`;
}
/* fällige Aufgaben in der aktuellen Auswahl (für Band und Schalter) */
function mmZahl(w) { const keys = new Set(sbPool().map(x => x.key)); return G.faelligListe({ w, keys }).length; }
function sbPool() { return themen({ f: V.sb.f, k: V.sb.k, wackel: V.sb.wackel, wichtig: V.sb.wichtig }); }
const wichtigZahl = () => themen({ f: V.sb.f, k: V.sb.k, wichtig: true }).length;
const poolZahl = () => { const p = sbPool(); return `${p.length} Unterthemen · ${p.reduce((s, x) => s + (x.t.nf || 0), 0)} Fragen-Familien`; };
function sbZusammenfassung() {
  const fs = V.sb.f.map(id => F[id].name).join(', ') || 'kein Fach';
  const ks = V.sb.k.length ? V.sb.k.map(x => { const [f, k] = x.split('/'); return F[f].kapitel.find(y => y.id === k).title; }).join(', ') : 'alle Oberthemen';
  return `${fs} · ${ks}${V.sb.wackel ? ' · nur rote Unterthemen' : ''}${V.sb.wichtig ? ' · nur Wichtiges' : ''}`;
}
const timerPresets = (mins = [5, 15, 25, 45]) => mins.map(m => `<button class="tmin" data-act="tmin" data-timer-min="${m}">${m}</button>`).join('');
const toolTiles = (fid = '') => `<div class="b-tools">${TOOLS.map(([id, n, s], i) => `<button class="b-tool" style="--c:${BUNT[i]}" data-go="sbt|${id}|${fid}"><b>${n}</b><small>${s}</small></button>`).join('')}</div>`;
/* Kurzer Hinweis unten, optional mit „Rückgängig“ (5 Sekunden) */
function hinweis(text, rueck) {
  document.getElementById('lt-hinweis')?.remove();
  const d = document.createElement('div'); d.id = 'lt-hinweis'; d.className = 'lt-hinweis'; d.setAttribute('role', 'status');
  d.innerHTML = `<span>${esc(text)}</span>${rueck ? '<button>Rückgängig</button>' : ''}`;
  document.body.appendChild(d);
  if (rueck) d.querySelector('button').onclick = () => { rueck(); d.remove(); };
  setTimeout(() => d.remove(), 5000);
}
/* Kurzer Schlüssel für eine Auswahl (Karteikarten-Sitzung zum Weitermachen) */
const sitzungVon = pool => 'k' + [...pool.map(x => x.key).sort().join('|')].reduce((h, c) => (h * 31 + c.charCodeAt(0)) | 0, 7).toString(36);
const leer = (titel, text) => `<div class="leer-z"><b>${titel}</b><span>${text}</span></div>`;

/* ---------- Adressen: #heute · #lernen--fach--ober--unter · #sandbox · #pruefung--fach--ober--modus · #einstellungen ---------- */
function adresse() {
  if (V.screen === 'lern') return `lernen--${V.fid}--${V.kid}--${V.tid}`;
  if (V.screen === 'sb') return 'sandbox' + (V.sb.seite ? '--' + V.sb.seite : '');
  if (V.screen === 'pruef' && V.pr && V.pr.probe) return V.pr.probe.startsWith('fach:') ? `fachprobe--${V.pr.probe.slice(5)}` : `probeklausur--${D.klausuren.findIndex(k => k.kurz === V.pr.probe)}`;
  if (V.screen === 'pruef' && V.pr) return `pruefung--${V.pr.fid}--${V.pr.kid}--${V.pr.modus}`;
  if (V.screen === 'einst') return 'einstellungen';
  if (V.screen === 'folien' && V.fo) return ['folien', V.fo.fid, V.fo.deck, V.fo.seite || ''].filter(Boolean).join('--');
  if (V.screen === 'folien') return 'folien';
  return 'heute';
}
function ausAdresse(h) {
  const [s, a, b, c] = (h || '').replace(/^#/, '').split('--');
  if (s === 'lernen' && TOP[a + '/' + c]) Object.assign(V, { screen: 'lern', fid: a, kid: b, tid: c });
  else if (s === 'sandbox') { V.screen = 'sb'; V.sb.seite = SEITEN_SB.includes(a) ? a : null; if (V.sb.seite && V.sb.seite !== 'methodisch') V.sb.tool = a; if (V.sb.seite && !V.sb.f.length) V.sb.f = D.faecher.map(f => f.id); }
  else if (s === 'pruefung' && F[a] && F[a].kapitel.some(k => k.id === b)) { V.screen = 'pruef'; V.pr = { fid: a, kid: b, modus: c === 'refresh' ? 'refresh' : 'end', laeuft: false }; }
  else if (s === 'probeklausur' && D.klausuren[+a]) { V.screen = 'pruef'; V.pr = { probe: D.klausuren[+a].kurz, laeuft: false }; }
  else if (s === 'fachprobe' && probeKl('fach:' + a)) { V.screen = 'pruef'; V.pr = { probe: 'fach:' + a, laeuft: false }; }
  else if (s === 'einstellungen') V.screen = 'einst';
  else if (s === 'folien') { V.screen = 'folien'; if (a && F[a] && F[a].folien) V.fo = Object.assign(V.fo || { filter: 'alle', suche: '', thema: '' }, { fid: a, deck: b || '', seite: +c || 0 }); }
  else V.screen = 'dash';
}
window.addEventListener('hashchange', () => { if (location.hash.slice(1) !== adresse()) { V.sb.prOffen = null; V.sb.auswahlAuf = false; ausAdresse(location.hash); render(true); } });

/* ---------- Navigation (data-go) ---------- */
function go(ziel) {
  const [s, a, b, c] = ziel.split('|');
  V.sb.prOffen = null; V.sb.auswahlAuf = false;   // Aufklapp-Menüs schließen beim Seitenwechsel
  if (s === 'dash') V.screen = 'dash';
  if (s === 'lern') { V.screen = 'lern'; V.fid = a; V.kid = b; V.tid = c || F[a].kapitel.find(k => k.id === b).topics[0].id; V.quizOffen = false; }
  if (s === 'lernf') { const x = zuletztIn(a); return go(`lern|${a}|${x.k.id}|${x.t.id}`); }
  if (s === 'sb') { V.screen = 'sb'; if (a) { V.sb.f = [a]; V.sb.k = b ? [a + '/' + b] : []; V.sb.wackel = false; if (b) V.sbAuf[a] = true; } }
  if (s === 'sb') V.sb.seite = null;
  if (s === 'sb-seite') V.screen = 'sb';
  if (s === 'sbw') { V.screen = 'sb'; V.sb.f = a ? [a] : D.faecher.map(f => f.id); V.sb.k = b ? [a + '/' + b] : []; V.sb.wackel = true; V.sb.tool = 'quiz'; V.sb.seite = 'quiz'; V.sb.modus = 'frei'; }
  if (s === 'sbm') { V.screen = 'sb'; V.sb.seite = 'methodisch'; V.sb.f = D.faecher.map(f => f.id); V.sb.k = []; V.sb.wackel = false; }
  if (s === 'sbt') { V.screen = 'sb'; V.sb.tool = a; V.sb.seite = a; if (b) { V.sb.f = [b]; V.sb.k = []; } if (!V.sb.f.length) V.sb.f = D.faecher.map(f => f.id); }
  if (s === 'probe') { V.screen = 'pruef'; V.pr = { probe: a, laeuft: false, items: null }; }
  if (s === 'pruef') { V.screen = 'pruef'; V.pr = { fid: a, kid: b, modus: c === 'refresh' ? 'refresh' : 'end', laeuft: false, items: null }; }
  if (s === 'einst') V.screen = 'einst';
  if (s === 'folien') { if (typeof foOeffnen === 'function') return foOeffnen(a || null, { tid: b }); V.screen = 'folien'; }
  if (V.screen === 'lern') { S.zuletzt = { fid: V.fid, kid: V.kid, tid: V.tid }; S.zuletztF[V.fid] = { kid: V.kid, tid: V.tid }; save(); }
  render(true);
}
function act(name, el) {
  const x = cur(), key = x && (x.f.id + '/' + x.t.id);
  if (name === 'blur') { V.blur = !V.blur; document.querySelectorAll('.inhalt').forEach(e => { e.classList.toggle('blurmode', V.blur); if (V.blur && typeof vdMarkiere === 'function') vdMarkiere(e); }); document.querySelectorAll('[data-act="blur"]').forEach(b => b.classList.toggle('on', V.blur)); return; }
  if (name === 'wackel') {
    if (G.istUnsicher(key)) { G.sicher(key); render(); hinweis('„Unsicher“ aufgehoben: Alle Aufgaben haben wieder ihren Stand von vorher.'); return; }
    const zurueck = G.unsicher(key); render(); hinweis('Alle Aufgaben dieses Unterthemas stehen jetzt auf Stufe 1 und kommen in „Methodisch lernen“. Nochmal tippen hebt es wieder auf.', () => { zurueck(); render(); }); return; }
  if (name === 'uaus') {
    const an = !uAus(key); uSetze(key, an); render();
    hinweis(an ? '„' + x.t.title + '“ ist ausgeblendet: Die Fragen kommen nicht mehr in Training, Übungs- und Probeklausur. Lesen kannst du es weiter.' : '„' + x.t.title + '“ ist wieder eingeblendet.' + (x.t.ag ? ' Laut Prüfungsausgrenzung ist es für die Klausur nicht notwendig.' : ''), () => { uSetze(key, !an); render(); }); return; }
  if (name === 'melde-kopie') { const t = (S.meldungen || []).map(x => `[${x.d.slice(0, 16).replace('T', ' ')}] ${x.ort}${x.sel ? `\n  Stelle: „${x.sel}“` : ''}\n  ${x.text}`).join('\n\n');
    (navigator.clipboard ? navigator.clipboard.writeText(t) : Promise.reject()).then(() => hinweis('Meldungen kopiert.'), () => { const ta = document.createElement('textarea'); ta.value = t; document.body.appendChild(ta); ta.select(); document.execCommand('copy'); ta.remove(); hinweis('Meldungen kopiert.'); }); return; }
  if (name === 'melde-loesch') { if (confirm('Alle Meldungen löschen?')) { S.meldungen = []; save(); render(); } return; }
  if (name === 'lang') { V.lang = V.lang === 'en' ? 'de' : 'en'; render(); return; }
  if (name === 'karten') { const eig = [{ key, f: x.f, k: x.k, t: x.t }]; karteOverlay(kartenFuer(eig).length >= 3 ? eig : x.k.topics.map(t => ({ key: x.f.id + '/' + t.id, f: x.f, k: x.k, t }))); return; }
  if (name === 'quiz') { V.quizOffen = true; const m = document.querySelector('[data-mount="mini"]'); if (m) { miniQuiz(m); m.scrollIntoView({ behavior: 'smooth', block: 'center' }); } return; }
  if (name === 'suche') { sucheOverlay(); return; }
  if (name === 'feed') { feedKlappe(false); feedOverlay(); return; }
  if (name === 'nach') { nacharbeiten(); return; }
  if (name === 'test-an' || name === 'test-aus') { testSetzen(name === 'test-an'); return; }
  if (name === 'feed-auf') { feedKlappe(!document.querySelector('.lw-neu').classList.contains('auf')); return; }
  if (name === 'markiert') { V_MK.bereich = V.screen === 'lern' ? (V_MK.bereich === 'alle' ? 'unter' : V_MK.bereich) : 'alle'; markiertPanel(); return; }
  if (name === 'tmin-frei') { timerSet(el.value); return; }
  if (name === 'sb-f') { const v = el.dataset.v, f = V.sb.f; V.sb.f = f.includes(v) ? f.filter(y => y !== v) : [...f, v]; V.sb.k = V.sb.k.filter(k => V.sb.f.includes(k.split('/')[0])); render(); return; }
  if (name === 'sb-w') { V.sb.wackel = !V.sb.wackel; render(); return; }
  if (name === 'sb-wi') { V.sb.wichtig = S.einst.wichtig = !V.sb.wichtig; save(); render(); return; }
  if (name === 'sb-tool') { V.sb.tool = V.sb.seite = el.dataset.v; if (!V.sb.f.length) V.sb.f = D.faecher.map(f => f.id); go('sb-seite'); return; }
  if (name === 'sb-modus') { V.sb.modus = el.dataset.v; render(); return; }
  if (name === 'sb-alle') { V.sb.seite = 'methodisch'; if (!V.sb.f.length) V.sb.f = D.faecher.map(f => f.id); go('sb-seite'); return; }
  if (name === 'sb-auswahl') { V.sb.auswahlAuf = !V.sb.auswahlAuf; render(); return; }
  if (name === 'sb-stapel') { V.sb.stapel = el.dataset.v || null; render(); return; }
  if (name === 'sb-stapel-weg') { delete S.ks[el.dataset.v]; save(); if (V.sb.stapel === el.dataset.v) V.sb.stapel = null; render(); return; }
  if (name === 'sb-prkl') { const a = V.sb.prAuf || (V.sb.prAuf = {}); a[el.dataset.v] = !a[el.dataset.v]; render(); return; }
  if (name === 'sb-zurueck') { V.sb.seite = null; go('sb-seite'); return; }
  if (name === 'sb-art') { const v = el.dataset.v, a = V.sb.arten; V.sb.arten = S.einst.arten = a.includes(v) ? (a.length > 1 ? a.filter(x => x !== v) : a) : [...a, v]; save(); render(); return; }
  if (name === 'sb-dmodus') { V.sb.dmodus = el.dataset.v; render(); return; }
  if (name === 'sb-stufe') { V.sb.stufe = S.einst.stufe = el.dataset.v; save(); render(); return; }
  if (name === 'sb-neu') { render(); return; }
  if (name === 'timer') { timerToggle(); return; }
  if (name === 'tmin') { timerSet(+el.dataset.timerMin); return; }
  if (name === 'pr-start') { V.pr.laeuft = true; render(); return; }
  if (name === 'pr-zeit') { V.pr.zeit = el.checked; S.einst.zeitlimit = el.checked; save(); render(); return; }
  if (name === 'pr-neu') { if (V.pr.bogen) clearInterval(V.pr.bogen.uhr); V.pr = { ...V.pr, items: null, bogen: null, laeuft: false }; render(true); return; }
  if (name === 'eigen-neu') { eigenFenster(null); return; }
  if (name === 'eigen-liste') { eigenFenster(); return; }
  if (name === 'eigen-auf') { eigenFenster(el.dataset.v); return; }
  if (name === 'ov-zu') { document.getElementById('ov')?.remove(); return; }
  if (name === 'neu-start') { neuStart(el); return; }
  if (name === 'theme') { setzeTheme(el.dataset.v); render(); return; }
  if (name === 'testtage') { S.einst.testTage = +el.value || 0; save(); render(); return; }
}
document.addEventListener('click', e => {
  if (V.blur) { const b = e.target.closest('.blurmode .vd, .blurmode .fx-leg dd, .blurmode b, .blurmode strong, .blurmode .merk, .blurmode td, .blurmode .kernsatz, .blurmode .glo, .blurmode mark.mk'); if (b && !b.closest('.nv') && !e.target.closest('button,a,input,label')) { b.classList.toggle('rev'); e.stopPropagation(); return; } }
  const fl = e.target.closest('[data-flip]');
  if (fl && !e.target.closest('[data-go]')) { const c = fl.closest('.fk'); c.classList.toggle('gedreht'); V.flip[c.dataset.f] = c.classList.contains('gedreht'); return; }
  if (e.target.closest('[data-spruch]')) { naechsterSpruch(); return; }
  if (e.target.closest('[data-fw]')) { document.querySelector('.fw-pop')?.classList.toggle('offen'); return; }
  if (!e.target.closest('.fw-pop')) document.querySelector('.fw-pop.offen')?.classList.remove('offen');
  const auf = e.target.closest('[data-auf]'); if (auf) { V.sbAuf[auf.dataset.auf] = !V.sbAuf[auf.dataset.auf]; render(); return; }
  const ok = e.target.closest('[data-sbk]'); if (ok) { const v = ok.dataset.sbk, f = v.split('/')[0]; V.sb.k = V.sb.k.includes(v) ? V.sb.k.filter(x => x !== v) : [...V.sb.k, v]; if (!V.sb.f.includes(f)) V.sb.f = [...V.sb.f, f]; render(); return; }
  const gp = e.target.closest('[data-geprueft]'); if (gp && !gp.disabled) { const f = F[gp.dataset.geprueft]; V.sb.k = f.kapitel.filter(k => stand(f.id, k.id)).map(k => f.id + '/' + k.id); render(); return; }
  const g = e.target.closest('[data-go]'); if (g) { e.preventDefault(); go(g.dataset.go); return; }
  const a = e.target.closest('[data-act]'); if (a && a.tagName !== 'INPUT') { e.preventDefault(); act(a.dataset.act, a); }
});
document.addEventListener('change', e => { const a = e.target.closest('[data-act]'); if (a && a.tagName === 'INPUT') act(a.dataset.act, a); });
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') { document.getElementById('ov')?.remove(); document.querySelector('.fw-pop.offen')?.classList.remove('offen'); }
  if ((e.ctrlKey || e.metaKey) && e.key === 'k') { e.preventDefault(); sucheOverlay(); }
  if ((e.key === 'Enter' || e.key === ' ') && e.target.matches('.fk-vorn')) { e.preventDefault(); e.target.click(); }
});
function naechsterSpruch() {
  const el = document.querySelector('[data-spruch] p'); if (!el) return;
  spruchI = (spruchI + 1) % SPRUECHE.length;
  el.classList.add('weg'); setTimeout(() => { el.textContent = SPRUECHE[spruchI]; el.classList.remove('weg'); }, 250);
}
setInterval(() => { if (document.querySelector('[data-spruch]') && !document.hidden) naechsterSpruch(); }, 12000);

/* ---------- Hell / Dunkel ---------- */
function setzeTheme(t) {
  S.einst.theme = t; save();
  try { if (t === 'system') localStorage.removeItem('lt-theme'); else localStorage.setItem('lt-theme', t); } catch (e) { }
  if (t === 'system') document.documentElement.removeAttribute('data-theme'); else document.documentElement.setAttribute('data-theme', t);
}

/* ---------- Rahmen ---------- */
const tabbar = () => `<nav class="tabbar" aria-label="Bereiche">
  <button class="${V.screen === 'dash' ? 'on' : ''}" data-go="dash">${IC.home}<span>Start</span></button>
  <button class="${V.screen === 'lern' ? 'on' : ''}" ${goLern(V.fid, V.kid, V.tid)}>${IC.lern}<span>Lernen</span></button>
  <button class="${V.screen === 'sb' ? 'on' : ''}" data-go="sb">${IC.sandbox}<span>Training</span></button>
  <button class="tb-klein ${V.screen === 'einst' ? 'on' : ''}" data-go="einst" aria-label="Einstellungen" title="Einstellungen">${IC.einst}</button></nav>`;
const rahmen = inner => `<div class="seite">${inner}</div>${tabbar()}`;

/* ---------- Heute: Wende-Karten + drei Kacheln ---------- */
function wendeKarte(f) {
  const fs = fachStand(f), ki = klausurInfo(f.id), blass = f.kapitel.filter(k => ober(f.id, k).cls === 'blass').length, z = zuletztIn(f.id);
  return `<div class="fk ${V.flip[f.id] ? 'gedreht' : ''}" data-f="${f.id}" style="--fach:${f.farbe}"><div class="fk-in">
    <div class="fk-seite fk-vorn" data-flip role="button" tabindex="0" aria-label="${esc(f.name)}: Oberthemen zeigen">
      <span class="b7-ring">${segRing(f, 150, 16)}<span class="b7-rz"><b>${fs.gesamt}</b><small>% prüfungsreif</small></span></span>
      <span class="b7-cn">${esc(f.name)}</span><span class="b7-cp">${esc(f.person)}</span>
      <span class="fk-abd">${fs.geprueft} von ${fs.von} Oberthemen geprüft</span>
      ${ki ? `<span class="b7-cc"><b>${ki.tage}</b> Tage · ${esc(ki.k.kurz)}</span>` : ''}<span class="fk-dreh">umdrehen ↻</span></div>
    <div class="fk-seite fk-hinten" data-flip>
      <div class="fk-kopf"><b>${esc(f.name)}</b><span>${fs.geprueft}/${fs.von} geprüft${blass ? ` · <em>${blass} verblasst</em>` : ''}</span></div>
      <ol class="fk-liste">${f.kapitel.map((k, i) => { const o = ober(f.id, k);
        return `<li class="o-${o.cls}"><button ${goLern(f.id, k.id)} title="${esc(k.title)}: ${o.txt}"><i>${i + 1}</i><span class="fk-t">${esc(k.title)}${fertigMarke(o)}</span>
          <span class="fk-bar"><u style="width:${o.st ? o.st.s : 0}%"></u><s style="width:${o.st ? o.st.pct : 0}%"></s></span><em>${o.st ? o.st.pct : '–'}</em></button></li>`; }).join('')}</ol>
      <div class="fk-fuss"><button ${goLern(f.id, z.k.id, z.t.id)}>Lernen</button><button data-go="sb|${f.id}">Training</button><span class="fk-zu" aria-hidden="true">↻</span></div></div>
  </div></div>`;
}
function dash() {
  const fl = faelligListe(), wl = wackelListe(), mm = G.faelligListe(), z = zuletzt(), ks = klausurenSortiert(), k0 = ks[0];
  const weiter = z ? (() => { const zi = z.k.topics.indexOf(z.t);
    return `<button class="tile m-weiter" style="--fach:${z.f.farbe}" ${goLern(z.f.id, z.k.id, z.t.id)}><small>Hier hast du aufgehört</small>
      <b>${esc(z.t.title)}</b><span class="m-wm">${esc(z.f.name)} · ${esc(z.k.title)}</span>
      <span class="b6-dots">${z.k.topics.map((t, i) => `<i class="${i < zi ? 'd' : i === zi ? 'on' : ''}"></i>`).join('')}</span>
      <span class="m-cta">Weiterlesen ${IC.pfeil}</span></button>`; })()
    : `<button class="tile m-weiter" style="--fach:${D.faecher[0].farbe}" data-go="lernf|${D.faecher[0].id}"><small>Noch nichts gelesen</small><b>Fang mit einem Fach an</b>
      <span class="m-wm">Karte oben umdrehen und ein Oberthema wählen, oder hier mit ${esc(D.faecher[0].name)} beginnen.</span><span class="m-cta">Loslegen ${IC.pfeil}</span></button>`;
  return rahmen(`<div class="lw-kopf">${grussHTML()}${feedHTML()}</div><header class="b7-top"><h1>Deine Fächer</h1>
      <div class="b7-stats">${k0 ? `<span><b>${tageBis(k0.beginn)}</b> Tage bis ${esc(k0.kurz)}</span>` : ''}<span><b>${fl.length}</b> verblasst</span><span><b>${mm.length}</b> fällig</span>${(() => { const n = Object.values(S.mark).reduce((s, l) => s + l.length, 0) + Object.keys(S.notiz).length; return n ? `<button class="b7-mk" data-act="markiert">${IC.markiert}<b>${n}</b> markiert</button>` : ''; })()}</div></header>
    <div class="m-deck">${D.faecher.map(wendeKarte).join('')}</div>
    <div class="m-drei">${weiter}
      <section class="tile m-blass"><small>Verblasst · wiederholen</small><h2>${fl.length ? fl.length + ' Oberthemen' : 'Nichts verblasst'}</h2>
        ${fl.length ? `<ul>${fl.slice(0, 4).map(d => `<li><button data-go="pruef|${d.f.id}|${d.k.id}|refresh"><span class="m-bt"><b>${esc(d.k.title)}</b><small>${esc(d.f.name)} · ${d.st.s} % → ${d.st.pct} %</small></span>
          <span class="b6-fall"><i style="width:${d.st.s}%"></i><i class="jetzt" style="width:${d.st.pct}%"></i></span><span class="m-go">5 Min</span></button></li>`).join('')}</ul>${fl.length > 4 ? `<small class="m-mehr">und ${fl.length - 4} weitere</small>` : ''}`
          : `<p class="m-leer">Hier erscheinen Oberthemen, deren Übungsklausur schon eine Weile her ist. Ein kurzer Refresh bringt sie wieder nach oben.</p>`}</section>
      <button class="tile m-wackel" data-go="sbm"><small>Methodisch lernen</small>${mm.length ? `<div class="big">${mm.length}<span class="m-big-s">fällig</span></div>` : '<div class="big leer">Nichts fällig</div>'}
        <span class="m-mm">${mm.length ? `${mm.filter(z => z.frisch).length} frische Fehler · ${wl.length} ${wl.length === 1 ? 'rotes Unterthema' : 'rote Unterthemen'}` : 'Was du irgendwo nicht auf Anhieb konntest, kommt hier zum richtigen Zeitpunkt wieder.'}</span>
        <span class="m-rote">${wl.slice(0, 3).map(w => `<span>${G.punkt(w.key)}${esc(w.t.title)}</span>`).join('')}</span>
        <span class="m-cta">Starten ${IC.pfeil}</span></button>
    </div>`);
}

/* ---------- Lernen ---------- */
function lernKontext() {
  const x = cur(), nb = nachbarn(), key = x.f.id + '/' + x.t.id, ki = klausurInfo(x.f.id);
  const anteil = ki ? (ki.gew.find(g => g.fid === x.f.id) || { pct: 100 }).pct : 100;
  return { x, nb, key, ki, w: istWackel(key), anteil, karten: kartenFuer([{ key, f: x.f, k: x.k, t: x.t }]).length };
}
/* Formeln wie auf Papier auch im Lerntext (Production bleibt bis zur Überarbeitung unverändert); je Thema einmal berechnet */
const LERN_CACHE = new Map();
function lernText(x, h) {
  if (!h) return h || '';
  const k = x.key + '|' + h.length + '|' + h.slice(0, 40);
  if (!LERN_CACHE.has(k)) LERN_CACHE.set(k, schoenLern(h));
  return LERN_CACHE.get(k);
}
/* Gold: eingearbeiteter Folienstoff, den diese Person beim ersten Besuch noch nicht hatte (S.kannte, gedaechtnis.js) */
function neuGold(x) {
  const key = x.f.id + '/' + x.t.id, nz = (TOP[key] && TOP[key].t.nz) || [];
  if (!(key in S.kannte)) { S.kannte[key] = nz.slice(); save(); }
  return nz.filter(b => !S.kannte[key].includes(b));
}
function inhaltHTML(x) {
  const t = x.t; neuGold(x);   // merkt nur, welche Überarbeitungen beim ersten Besuch schon da waren (Pflicht-Hinweis, Nacharbeiten)
  const h = lernText(x, t.html);   // Folienstoff steht als normaler Text (keine Gold-Markierung mehr, 16.11.2026)
  return `<div class="inhalt${V.blur ? ' blurmode' : ''}" data-lang="${x.f.englisch ? V.lang : 'de'}">
    ${t.kern ? `<p class="kernsatz">${lernText(x, t.kern)}</p>` : ''}${h}${t.src ? `<p class="quelle">Quelle: ${esc(t.src)}${typeof foQuelleHTML === 'function' ? foQuelleHTML(x) : ''}</p>` : (typeof foQuelleHTML === 'function' && x.f.folien ? `<p class="quelle">${foQuelleHTML(x)}</p>` : '')}<button class="melde" data-melde="Lernseite · ${esc(x.f.name)} · ${esc(txt(x.t.title))}">⚑ Fehler oder Unklarheit melden</button></div>`;
}
const miniTile = () => `<section class="tile bl-card bl-mini"><div class="mq-kopf"><span class="mq-ic">${IC.quiz}</span><div><b>Mini-Quiz</b><small>5 Fragen · grobes Verständnis nach dem ersten Lesen</small></div></div>
  <div data-mount="mini">${V.quizOffen ? '' : '<button class="btn btn-main" data-act="quiz">Los</button>'}</div></section>`;
function lern() {
  const c = lernKontext(), { x, nb } = c, o = ober(x.f.id, x.k);
  const wahl = `<div class="fw"><button class="fw-knopf" data-fw style="--fach:${x.f.farbe}" aria-haspopup="true"><i></i><span><small>Fach</small><b>${esc(x.f.name)}</b></span><span class="fw-pfeil">▾</span></button>
    <div class="fw-pop"><small>Fach wechseln · du landest dort, wo du zuletzt warst</small>${D.faecher.map(f => { const zz = zuletztIn(f.id), fs = fachStand(f);
      return `<button class="fw-f ${f === x.f ? 'on' : ''}" style="--fach:${f.farbe}" data-go="lernf|${f.id}"><span class="fw-ring" style="--p:${fs.gesamt}"><b>${fs.gesamt}</b></span><span><b>${esc(f.name)}</b><small>${esc(zz.t.title)}</small></span>${(() => { const n = Object.keys(S.mark).concat(Object.keys(S.notiz)).filter(k => k.startsWith(f.id + '/')).length; return n ? `<em class="fw-mk">${n} markiert</em>` : ''; })()}</button>`; }).join('')}</div></div>`;
  { const mo = document.querySelector('.lt-modale'); if (mo) mo.style.setProperty('--x-acc', x.f.farbe); }   // Schaubild-Fenster in Fachfarbe
  return rahmen(`<div class="m-lern" style="--fach:${x.f.farbe}"><div class="m-col">${wahl}
    <header class="bl-hero"><div class="bl-hl"><small>Oberthema ${kapNr(x.f, x.k)} von ${x.f.kapitel.length} · ${esc(x.f.name)}</small><h2>${esc(x.k.title)}</h2>
        <select class="k3" aria-label="Oberthema wählen" onchange="go(this.value)">${x.f.kapitel.map((k, i) => `<option value="lern|${x.f.id}|${k.id}|" ${k === x.k ? 'selected' : ''}>${i + 1}. ${esc(k.title)}</option>`).join('')}</select></div>
      <div class="bl-ring">${segRing(x.f, 132, 18)}<span><b>${kapNr(x.f, x.k)}</b><small>von ${x.f.kapitel.length}</small></span></div></header>
    <nav class="bl-rail" aria-label="Unterthemen">${x.k.topics.map((t, i) => { const ua = !t.aus && uAus(x.f.id + '/' + t.id); return `<button class="${t === x.t ? 'on' : ''} ${t.aus ? 'aus' : ''}${ua ? ' u-aus' : ''}" ${t.aus ? 'title="Kommt nicht dran"' : ua ? `title="${t.ag ? 'Nicht in der Klausur notwendig (Prüfungsausgrenzung): ausgeblendet' : 'Ausgeblendet: kommt nicht in Training und Klausuren'}"` : ''} ${goLern(x.f.id, x.k.id, t.id)}><i>${i + 1}</i>${ua ? `<span class="u-aus-ic">${IC.uaus}</span>` : G.punkt(x.f.id + '/' + t.id)}<span>${esc(t.title)}</span>${markPunkte(x.f.id + '/' + t.id)}</button>`; }).join('')}
      ${o.fertig ? `<span class="bl-rail-fertig" title="Alle eingeblendeten Unterthemen sind grün">✓ Oberthema fertig${o.aus ? ` <small>${o.aus} ausgeblendet</small>` : ''}</span>` : ''}<button class="bl-rail-sb" data-go="sb|${x.f.id}|${x.k.id}"><i>${IC.sandbox}</i><span>Training</span></button></nav>
    <div class="m-info">
      <div class="tile mi mi-stand"><small>Prüfungsstand Oberthema</small><div class="mi-z"><b>${o.st ? o.st.pct : '–'}</b>${o.st ? '<span>%</span>' : ''}</div>
        <span class="b7-bar"><i style="width:${o.st ? o.st.s : 0}%"></i><i class="jetzt" style="width:${o.st ? o.st.pct : 0}%"></i></span>
        ${o.st && o.st.refresh ? `<button class="mi-btn hi" data-go="pruef|${x.f.id}|${x.k.id}|refresh">5-Min-Refresh</button>` : `<button class="mi-btn" data-go="pruef|${x.f.id}|${x.k.id}|end">${o.st ? 'Nochmal prüfen' : 'Übungsklausur'}</button>`}</div>
      <div class="tile mi mi-kl"><small>Klausur</small>${c.ki ? `<div class="mi-z"><b>${c.ki.tage}</b><span>Tage</span></div><p>${esc(c.ki.k.kurz)} · ${c.ki.datum}${c.anteil < 100 ? ` · ${esc(x.f.name)} zählt ${c.anteil} %` : ''}</p>` : '<p>kein Termin</p>'}</div>
      <button class="tile mi mi-spruch" data-spruch title="Nächster Spruch"><small>Kurz durchatmen</small><p>${SPRUECHE[spruchI]}</p></button></div>
    <article class="tile bl-card"><div class="bdgs">${badges(x.t)}${x.t.aus ? '' : `<span class="bdg bdg-st st-b${G.farbe(c.key)}" title="Stufe der Aufgaben in diesem Unterthema">${G.punkt(c.key)}${esc(G.text(c.key))}</span>`}${S.notiz[c.key] ? '<button class="bdg bdg-notiz" data-act="markiert">Deine Notiz</button>' : ''}${!x.t.aus && uAus(c.key) ? `<button class="bdg bdg-uaus" data-act="uaus" title="Wieder einblenden">${x.t.ag ? 'Nicht in der Klausur notwendig · ausgeblendet' : 'Ausgeblendet · nicht in Training und Klausuren'}</button>` : ''}</div><h1>${esc(x.t.title)}</h1>${inhaltHTML(x)}</article>
    ${x.f.rechnen ? `<section class="tile bl-card"><h2>Direkt üben <small>einfach, mit Rettungsringen</small></h2><div data-mount="ueben"></div></section>` : ''}
    ${x.t.aus ? '' : miniTile()}
    <nav class="bl-pager">${nb.prev ? `<button class="tile pg-prev" ${goLern(x.f.id, x.k.id, nb.prev.id)}><small>zurück</small><b>${esc(nb.prev.title)}</b></button>` : '<span></span>'}
      ${nb.next ? `<button class="tile pg-next" ${goLern(x.f.id, x.k.id, nb.next.id)}><small>weiter · Thema ${nb.i + 2}</small><b>${esc(nb.next.title)}</b>${IC.pfeil}</button>` : ''}</nav>
    ${nb.letztes ? `<section class="bl-ende"><button class="tile e-sb" data-go="sb|${x.f.id}|${x.k.id}"><small>Oberthema durch</small><b>Jetzt in der Sandbox trainieren</b><span>vorgefiltert auf „${esc(x.k.title)}“</span>${IC.pfeil}</button>
      <button class="tile e-pr" data-go="pruef|${x.f.id}|${x.k.id}|end"><small>Klausurniveau, ohne Hilfen</small><b>Übungsklausur</b><span>${o.txt}</span></button></section>` : ''}</div>
    <aside class="a-dock m-dock" aria-label="Werkzeuge"><div class="a-dock-in">
      <button class="${V.blur ? 'on' : ''}" data-act="blur">${IC.blur}<span>Verdecken</span></button>
      <button data-act="karten">${IC.karten}<span>Karten <small>${c.karten}</small></span></button>
      <button data-act="markiert">${IC.markiert}<span>Markiert${markZahl(c.key) ? ` <small>${markZahl(c.key)}</small>` : ''}</span></button>
      <button data-act="suche">${IC.suche}<span>Suche</span></button>
      ${x.f.folien ? `<button data-fo-panel="${x.f.id}|${x.t.id}" title="Folien zu diesem Thema neben der Lernseite"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="14" height="10" rx="1.5"/><path d="M7 18h10a2 2 0 0 0 2-2V8"/></svg><span>Folien</span></button>` : ''}
      <button class="${G.istUnsicher(c.key) ? 'on w' : ''}" data-act="wackel" aria-pressed="${G.istUnsicher(c.key)}" title="${G.istUnsicher(c.key) ? 'Unsicher aufheben: Stand von vorher wiederherstellen' : 'Alle Aufgaben dieses Unterthemas auf Stufe 1 setzen'}">${IC.wackel}<span>Unsicher</span></button>
      ${x.t.aus ? '' : `<button class="${uAus(c.key) ? 'on' : ''}" data-act="uaus" aria-pressed="${uAus(c.key)}" title="${uAus(c.key) ? 'Wieder einblenden: Fragen kommen wieder in Training und Klausuren' : 'Unterthema ausblenden: Fragen kommen nicht mehr in Training, Übungs- und Probeklausur'}">${IC.uaus}<span>${uAus(c.key) ? 'Einblenden' : 'Ausblenden'}</span></button>`}
      ${x.f.englisch ? `<button data-act="lang"><b class="ic-txt">${V.lang === 'en' ? 'DE' : 'EN'}</b><span>${V.lang === 'en' ? 'Deutsch' : 'English'}</span></button>` : ''}
      <button data-go="sb|${x.f.id}|${x.k.id}">${IC.sandbox}<span>Training</span></button></div></aside></div>`);
}

/* ---------- Sandbox ---------- */
function sb() {
  return V.sb.seite ? sbSeite() : sbStart();
}
const zielChip = z => { const Z = ZIELE.find(x => x[0] === z); return `<span class="ziel z-${z}">${Z[1]}</span>`; };
/* Kurzer Stand je Werkzeug für die Kacheln */
function sbVorschau(id) {
  const pool = sbPool(), keys = new Set(pool.map(x => x.key));
  if (!pool.length) return '';
  const art = WERKZEUG_ART[id], faellig = G.faelligListe({ w: art, keys }).length;
  return `<span class="m-tstand">${faellig ? `<b>${faellig}</b> fällig` : 'nichts fällig'}</span>`;
}
function sbWasHTML() {
  return `<aside class="sx-was"><div class="sx-h"><span class="a-sn">1</span><b>Was üben?</b><small>Fach antippen zum Auswählen, „Oberthemen ▾“ zum Eingrenzen</small></div>
        ${D.faecher.map(f => { const on = V.sb.f.includes(f.id), auf = !!V.sbAuf[f.id], gew = f.kapitel.filter(k => V.sb.k.includes(f.id + '/' + k.id));
          const geprueft = f.kapitel.filter(k => stand(f.id, k.id)), allein = on && V.sb.f.length === 1, eins = gew.length === 1 ? gew[0] : null, st1 = eins && stand(f.id, eins.id);
          return `<div class="sx-fach ${on ? 'on' : ''} ${auf ? 'auf' : ''}" style="--fach:${f.farbe}">
            <div class="sx-zeile"><button class="sx-fk" data-act="sb-f" data-v="${f.id}" aria-pressed="${on}"><i class="bs-check"></i><span><b>${esc(f.name)}</b><small>${on ? (gew.length ? `${gew.length} von ${f.kapitel.length} Oberthemen` : `alle ${f.kapitel.length} Oberthemen`) : `${fachStand(f).geprueft}/${f.kapitel.length} Oberthemen geprüft`}</small></span></button>
              <button class="sx-auf" data-auf="${f.id}" aria-expanded="${auf}"><span>Oberthemen</span><b>${auf ? '▴' : '▾'}</b></button></div>
            ${auf ? `<div class="sx-block">
              <div class="sx-tools"><button class="sx-gp" data-geprueft="${f.id}" ${allein && geprueft.length ? '' : 'disabled'}>Nur geprüfte <small>${geprueft.length}</small></button>
                <span class="sx-tipp">${!geprueft.length ? 'noch nichts geprüft' : allein ? 'wählt alle mit Prüfungsstand' : 'geht nur, wenn nur dieses Fach gewählt ist'}</span></div>
              ${eins ? `<button class="sx-pruef" data-go="pruef|${f.id}|${eins.id}|${st1 && st1.refresh ? 'refresh' : 'end'}"><span><small>${st1 && st1.refresh ? '5-Minuten-Refresh' : 'Übungsklausur'}</small><b>${esc(eins.title)}</b></span>${TOOL_IC.blatt}</button>`
                : `<div class="sx-pruef aus"><span><small>Prüfung</small><b>${gew.length ? 'Für die Prüfung genau ein Oberthema wählen' : 'Ein Oberthema wählen, dann geht es direkt in die Übungsklausur'}</b></span></div>`}
              <div class="sx-ober">${f.kapitel.map((k, i) => { const oo = ober(f.id, k), sel = V.sb.k.includes(f.id + '/' + k.id);
                return `<button class="sx-ok ${sel ? 'on' : ''}" data-sbk="${f.id}/${k.id}" aria-pressed="${sel}"><i>${i + 1}</i><span>${esc(k.title)}${fertigMarke(oo)}${G.balken(f, k)}</span><em class="o-${oo.cls}">${oo.st ? oo.st.pct : '–'}</em></button>`; }).join('')}</div></div>` : ''}</div>`; }).join('')}
        <button class="sw-toggle ${V.sb.wackel ? 'on' : ''}" data-act="sb-w" aria-pressed="${V.sb.wackel}"><i></i>Nur rote Unterthemen <small>${wackelListe().length}</small></button>
        <button class="sw-toggle sw-wi ${V.sb.wichtig ? 'on' : ''}" data-act="sb-wi" aria-pressed="${V.sb.wichtig}"><i></i>Nur Wichtiges <small>${wichtigZahl()}</small></button></aside>`;
}
/* Karteikarten: nur angefangene Stapel, zum Weitermachen oder Löschen (Stufen der Karten bleiben dabei, wie sie sind) */
function stapelOffen() {
  return Object.entries(S.ks).filter(([, z]) => z && (z.stapel.length + z.nicht.length) && (z.runde > 1 || z.erste.g + z.erste.n > 0));
}
function stapelHTML() {
  const offen = stapelOffen();
  return `<aside class="w-stapel"><h3>Angefangene Stapel</h3>
    <button class="deck ${!V.sb.stapel ? 'on' : ''}" data-act="sb-stapel" data-v=""><b>Aktuelle Auswahl</b><small>${esc(sbZusammenfassung())}</small></button>
    ${offen.length ? offen.map(([sk, z]) => { const rest = z.stapel.length + z.nicht.length, ges = rest + z.erste.g + (z.runde > 1 ? 0 : 0);
      return `<div class="deck deck-o ${V.sb.stapel === sk ? 'on' : ''}"><button class="deck-auf" data-act="sb-stapel" data-v="${sk}"><b>${esc(z.name || 'Stapel')}</b><small>Runde ${z.runde} · noch ${rest} ${rest === 1 ? 'Karte' : 'Karten'}</small></button>
        <button class="deck-weg" data-act="sb-stapel-weg" data-v="${sk}" title="Stapel löschen (deine Stufen bleiben)" aria-label="Stapel löschen">✕</button></div>`; }).join('')
      : '<p class="dim3">Hier erscheinen Stapel, sobald du angefangen hast. Brichst du ab, machst du hier weiter.</p>'}
    <h3 class="w-eh">Deine Karten</h3>
    <div class="deck deck-e"><button class="deck-auf" data-act="eigen-liste"><b>${Object.keys(S.eigen).length ? Object.keys(S.eigen).length + ' eigene ' + (Object.keys(S.eigen).length === 1 ? 'Karte' : 'Karten') : 'Noch keine eigenen Karten'}</b><small>ansehen, ändern, löschen</small></button>
      <button class="deck-neu" data-act="eigen-neu" title="Eigene Karte anlegen" aria-label="Eigene Karte anlegen">+</button></div></aside>`;
}
/* Eigene Karteikarten: anlegen, ändern, löschen. Sie hängen an einem Unterthema und zählen wie alle Karten für die Stufen. */
function eigenFenster(id) {
  document.getElementById('ov')?.remove();
  const c = id ? S.eigen[id] : null, alle = Object.entries(S.eigen).sort((a, b) => b[1].t - a[1].t);
  const vorschlag = c ? c.k : (S.einst.eigenK && TOP[S.einst.eigenK] && V.sb.f.includes(TOP[S.einst.eigenK].f.id) ? S.einst.eigenK : (() => { const f = F[V.sb.f[0]] || D.faecher[0], k = f.kapitel.find(k => V.sb.k.includes(f.id + '/' + k.id)) || f.kapitel[0]; return f.id + '/' + k.topics[0].id; })());
  const auswahl = D.faecher.map(f => f.kapitel.map((k, i) => `<optgroup label="${esc(f.name)} · ${i + 1} ${esc(k.title)}">${k.topics.map(t => { const key = f.id + '/' + t.id; return `<option value="${key}" ${key === vorschlag ? 'selected' : ''}>${esc(t.title)}</option>`; }).join('')}</optgroup>`).join('')).join('');
  const formular = id !== undefined;
  document.body.insertAdjacentHTML('beforeend', `<div id="ov" class="ov ov-seite" role="dialog" aria-modal="true" aria-label="Deine Karteikarten"><div class="ov-box">
    <div class="ov-kopf"><b>${formular ? (c ? 'Karte ändern' : 'Neue Karte') : 'Deine Karten'}</b><span></span><button class="btn" data-act="ov-zu">Schließen</button></div>
    ${formular ? `<form class="ek-form" data-eigen="${id || ''}">
      <label><small>Unterthema</small><select name="k">${auswahl}</select></label>
      <label><small>Vorderseite (Frage oder Begriff)</small><textarea name="v" rows="2" required maxlength="300" placeholder="z. B. Die 6 R der Materialwirtschaft">${esc(c ? c.v : '')}</textarea></label>
      <label><small>Rückseite (Antwort; jede Zeile wird ein Punkt)</small><textarea name="r" rows="5" required maxlength="1500" placeholder="Antwort …">${esc(c ? c.r : '')}</textarea></label>
      <div class="ek-knoepfe"><button class="btn btn-main" type="submit">Speichern</button>${c ? `<button class="btn" type="button" data-eweg="${id}">Löschen</button>` : ''}<button class="btn" type="button" data-act="eigen-liste">Alle Karten</button></div></form>`
    : `<button class="btn btn-main ek-neu" data-act="eigen-neu">+ Neue Karte</button>
      ${alle.length ? `<ul class="mk-liste">${alle.map(([eid, e]) => { const tt = TOP[e.k]; return `<li class="ek-zeile"><button class="mk-it ek-it" data-act="eigen-auf" data-v="${eid}"><span><q>${esc(e.v)}</q><em>${esc(e.r.slice(0, 120))}</em><small>${tt ? esc(tt.f.name) + ' · ' + esc(tt.t.title) : ''}</small></span></button><button class="ek-weg" data-eweg="${eid}" title="Karte löschen" aria-label="Karte löschen">✕</button></li>`; }).join('')}</ul>`
      : '<p class="dim3">Lege Karten für alles an, was du dir merken willst. Sie kommen in den Karteikarten-Stapeln und in „Methodisch lernen“ wie alle anderen Karten.</p>'}`}</div></div>`);
  const ov = document.getElementById('ov');
  ov.addEventListener('click', e => { if (e.target === ov) ov.remove(); const w = e.target.closest('[data-eweg]');
    if (!w) return; e.stopPropagation();
    if (!w.dataset.sicher) { w.dataset.sicher = '1'; w.classList.add('ek-sicher'); w.textContent = 'Wirklich löschen?'; return; }
    delete S.eigen[w.dataset.eweg]; delete S.g['e:' + w.dataset.eweg]; save(); hinweis('Karte gelöscht.'); eigenFenster(); render(); });
  const fo = ov.querySelector('.ek-form');
  if (fo) { fo.querySelector('textarea[name="v"]').focus();
    fo.addEventListener('submit', e => { e.preventDefault(); const d = new FormData(fo), v = String(d.get('v')).trim(), r = String(d.get('r')).trim(), k = String(d.get('k'));
      if (!v || !r || !TOP[k]) return;
      const eid = fo.dataset.eigen || Date.now().toString(36) + Math.random().toString(36).slice(2, 6);
      S.eigen[eid] = { k, v, r, t: Date.now() }; S.einst.eigenK = k; save();
      hinweis(fo.dataset.eigen ? 'Karte geändert.' : 'Karte gespeichert. Sie kommt beim nächsten Stapel dran.'); eigenFenster(); render(); }); }
}
/* Probeklausur: echte Klausur (Kurzname) oder nur ein Fach daraus („fach:<id>“, Punkte und Zeit anteilig nach Gewicht) */
function probeKl(name) {
  if (!name || !name.startsWith('fach:')) {   // Teile ohne gebautes Fach (noch keine Unterlagen) zählen nicht: Punkte und Zeit anteilig
    const kl = D.klausuren.find(k => k.kurz === name); if (!kl || !kl.teile) return kl;
    const alle = kl.teile.reduce((s, t) => s + (t[2] || 0), 0), da = kl.teile.filter(t => F[t[1]]).reduce((s, t) => s + (t[2] || 0), 0);
    return da > 0 && da < alle ? { ...kl, punkte: Math.round((kl.punkte || 120) * da / alle), minuten: Math.round((kl.minuten || 120) * da / alle) } : kl;
  }
  const fid = name.slice(5), kl = D.klausuren.find(k => k.faecher.includes(fid)); if (!kl || !F[fid]) return null;
  const teile = kl.teile.filter(t => F[t[1]]), gsum = teile.reduce((s, t) => s + t[2], 0) || 1, mein = teile.filter(t => t[1] === fid), anteil = mein.reduce((s, t) => s + t[2], 0) / gsum;
  return { ...kl, kurz: name, titel: F[fid].lang || F[fid].name, fachProbe: true, teile: mein, faecher: [fid], punkte: Math.round((kl.punkte || 120) * anteil), minuten: Math.round((kl.minuten || 120) * anteil) };
}
/* Prüfen: Übungsklausur je Oberthema oder ganze Klausur */
function pruefHTML() {
  const auf = V.sb.prAuf || (V.sb.prAuf = {});
  return `<div class="pk-liste">${klausurenSortiert().filter(kl => kl.faecher.some(fid => F[fid])).map((kl, n) => { const fs = [...new Set(kl.faecher)].filter(fid => F[fid]), tage = tageBis(kl.beginn);
    const v = (S.probe || {})[kl.kurz] || [], l = v[v.length - 1];
    return `<section class="pk-kl"><header class="pk-klh"><span class="pk-tage"><b>${tage}</b><small>${tage === 1 ? 'Tag' : 'Tage'}</small></span>
        <div class="pk-kt"><small>Klausur ${n + 1} · ${datumKurz(kl.beginn)}</small><h3>${esc(kl.kurz)}</h3></div>
        <button class="pk-probe" data-go="probe|${esc(kl.kurz)}"><b>Ganze Klausur prüfen</b><small>Probeklausur · ${l ? `zuletzt Note ${noteText(l.note)}` : `${kl.punkte || 120} P · ${kl.minuten || 120} min`}</small></button></header>
      ${fs.map(fid => { const f = F[fid], key = kl.kurz + ':' + fid, fa = !!auf[key], fst = fachStand(f);
        return `<div class="pk-fach ${fa ? 'auf' : ''}" style="--fach:${f.farbe}"><button class="pk-fz" data-act="sb-prkl" data-v="${esc(key)}" aria-expanded="${fa}">
            <span class="pk-fn"><b>${esc(f.name)}</b><small>${fst.geprueft} von ${fst.von} Oberthemen geprüft · ${fst.gesamt} % prüfungsreif</small></span>
            <span class="pk-fa">${fa ? 'zuklappen ▴' : 'Oberthema prüfen ▾'}</span></button>
          ${fa && fs.length > 1 ? (() => { const fk = probeKl('fach:' + fid), vv = (S.probe || {})['fach:' + fid] || [], ll = vv[vv.length - 1]; return `<button class="pk-fprobe" data-go="probe|fach:${fid}"><b>Nur ${esc(f.name)} prüfen</b><small>Probeklausur nur für dieses Fach · ${ll ? `zuletzt Note ${noteText(ll.note)}` : `${fk.punkte} P · ${fk.minuten} min`}</small></button>`; })() : ''}
          ${fa ? `<div class="pk-oks">${f.kapitel.map((k, i) => { const st = stand(fid, k.id);
            return `<button data-go="pruef|${fid}|${k.id}|end"><i>${i + 1}</i><span>${esc(k.title)}</span><em>${st ? st.pct + ' %' : 'noch nicht geprüft'}</em><b>Übungsklausur →</b></button>`; }).join('')}</div>` : ''}</div>`; }).join('')}</section>`; }).join('')}</div>`;
}
/* Kleine Auswahl im Aufklapp-Menü der Werkzeugseiten: Fach an/aus, Oberthemen eingrenzen, nur rote Unterthemen */
function auswahlKlein() {
  return `${D.faecher.map(f => { const on = V.sb.f.includes(f.id), auf = !!V.sbAuf[f.id], gew = f.kapitel.filter(k => V.sb.k.includes(f.id + '/' + k.id)).length;
    return `<div class="wp-f ${on ? 'on' : ''}" style="--fach:${f.farbe}"><div class="wp-z"><button class="wp-fk" data-act="sb-f" data-v="${f.id}" aria-pressed="${on}"><i class="wp-c"></i><b>${esc(f.name)}</b><small>${on ? (gew ? `${gew} von ${f.kapitel.length}` : 'alle') : ''}</small></button>
      <button class="wp-auf" data-auf="${f.id}" aria-expanded="${auf}" aria-label="Oberthemen ${esc(f.name)}">${auf ? '▴' : '▾'}</button></div>
      ${auf ? `<div class="wp-ok">${f.kapitel.map((k, i) => { const sel = V.sb.k.includes(f.id + '/' + k.id); return `<button class="${sel ? 'on' : ''}" data-sbk="${f.id}/${k.id}" aria-pressed="${sel}"><span class="wp-dot"></span><i>${i + 1}</i><span>${esc(k.title)}</span></button>`; }).join('')}</div>` : ''}</div>`; }).join('')}
    <button class="sw-toggle wp-rot ${V.sb.wackel ? 'on' : ''}" data-act="sb-w" aria-pressed="${V.sb.wackel}"><i></i>Nur rote Unterthemen <small>${wackelListe().length}</small></button>
    <button class="sw-toggle sw-wi ${V.sb.wichtig ? 'on' : ''}" data-act="sb-wi" aria-pressed="${V.sb.wichtig}"><i></i>Nur Wichtiges <small>${wichtigZahl()}</small></button>`;
}
function sbStart() {
  return rahmen(`<header class="b7-top"><h1>Training</h1><div class="b7-stats"><span>${poolZahl()}</span>${uhrHTML()}</div></header>
    <div class="sx">
${sbWasHTML()}
      <section class="sx-wie"><div class="sx-werk"><div class="sx-h hell"><span class="a-sn">2</span><b>Wie üben?</b></div>
          <button class="mm-band" data-act="sb-alle"><span><small>Alle Werkzeuge gemischt</small><b>Methodisch lernen</b></span><em>${mmZahl()} fällig</em></button>
          ${nachBand()}
          <div class="m-ziele">${ZIELE.map(([z, name, satz, ids]) => `<div class="m-ziel z-${z}"><div class="m-zkopf">${zielChip(z)}<small>${satz}</small></div>
            <div class="m-tools">${ids.map(id => { const i = TOOLS.findIndex(t => t[0] === id), [, n, sub] = TOOLS[i];
              return `<button class="m-tool" style="--c:${BUNT[i]}" data-act="sb-tool" data-v="${id}"><span class="m-tic">${TOOL_IC[id]}</span><b>${n}</b><small>${sub}</small>${sbVorschau(id)}</button>`; }).join('')}</div></div>`).join('')}</div>
          <p class="m-woanders">Nicht hier: <b>Mini-Quiz</b> (5 Fragen am Ende jedes Unterthemas) · Prüfen mit Note und Prozent: unten bei <b>3 · Jetzt abprüfen</b>.</p></div>
        <div class="sx-pruefen"><div class="sx-h"><span class="a-sn">3</span><b>Jetzt abprüfen</b><small>Wie in der Klausur: ohne Hilfen, mit Zeit und Note. Fach aufklappen und ein Oberthema als Übungsklausur prüfen, oder die ganze Klausur als Probeklausur.</small></div>
          ${pruefHTML()}</div>
      </section></div>`);
}
function sbSeite() {
  const id = V.sb.seite, mm = id === 'methodisch', ti = TOOLS.findIndex(t => t[0] === id), tool = TOOLS[ti];
  const niveau = id === 'blatt' ? BLATT_NIVEAU : STUFEN;
  return rahmen(`<header class="w-kopf"><button class="zurueck" data-act="sb-zurueck" aria-label="Zurück zum Training">${IC.pfeil}</button>
      <div class="w-titel">${mm ? '<span class="ziel z-a">Alle Werkzeuge</span>' : zielChip(ZIEL_VON[id])}<h1>${mm ? 'Methodisch lernen' : tool[1]}</h1><p>${WAS_DRIN[id]}</p></div>
      <div class="b7-stats">${uhrHTML()}</div></header>
    <div class="w-leiste">
      <div class="w-awrap"><button class="w-auswahl ${V.sb.auswahlAuf ? 'on' : ''}" data-act="sb-auswahl" aria-expanded="${!!V.sb.auswahlAuf}" title="Auswahl ändern"><small>Auswahl</small><b>${esc(sbZusammenfassung())}</b><em>${V.sb.auswahlAuf ? '▴' : '▾'}</em></button>
        ${V.sb.auswahlAuf ? `<div class="w-pop-bg" data-act="sb-auswahl"></div><div class="w-pop" role="dialog" aria-label="Auswahl">${auswahlKlein()}</div>` : ''}</div>
      ${mm ? `<span class="w-info"><b>${mmZahl()}</b> fällig</span>` : `<div class="seg mm-seg" role="group" aria-label="Modus"><button class="${V.sb.modus === 'frei' ? 'on' : ''}" data-act="sb-modus" data-v="frei" aria-pressed="${V.sb.modus === 'frei'}">Frei</button><button class="${V.sb.modus === 'methodisch' ? 'on' : ''}" data-act="sb-modus" data-v="methodisch" aria-pressed="${V.sb.modus === 'methodisch'}">Methodisch <small>${mmZahl(WERKZEUG_ART[id])}</small></button></div>`}
      ${!mm && V.sb.modus === 'frei' && id === 'drill' ? `<div class="w-niveau"><span>Modus</span><div class="seg">${[['waehlen', 'Auswählen'], ['schreiben', 'Selbst schreiben']].map(([v, n]) => `<button class="${(V.sb.dmodus || 'waehlen') === v ? 'on' : ''}" data-act="sb-dmodus" data-v="${v}">${n}</button>`).join('')}</div></div>` : ''}
      ${!mm && V.sb.modus === 'frei' && id === 'blatt' ? `<div class="w-niveau"><span>Niveau</span><div class="seg">${niveau.map(([v, n]) => { const on = (id === 'blatt' ? blattNiveau(V.sb.stufe) : V.sb.stufe) === v; return `<button class="${on ? 'on' : ''}" data-act="sb-stufe" data-v="${v}" aria-pressed="${on}">${n}</button>`; }).join('')}</div></div>` : ''}
      ${!mm && V.sb.modus === 'frei' && id === 'blatt' ? `<div class="arten"><span>Aufgabenarten</span>${ARTEN.map(([v, n]) => `<button class="${V.sb.arten.includes(v) ? 'on' : ''}" data-act="sb-art" data-v="${v}" aria-pressed="${V.sb.arten.includes(v)}">${n}</button>`).join('')}</div>` : ''}
      <button class="a-neu" data-act="sb-neu" title="Neu mischen" aria-label="Neu mischen">↻</button></div>
    ${id === 'swipe' && V.sb.modus === 'frei' ? `<div class="w-zwei"><div class="w-zwei-l">` : ''}
    <section class="m-work w-buehne" style="--c:${mm ? 'var(--st-3)' : BUNT[ti]}"><div class="m-wbody"><div data-mount="sb"></div></div></section>
    ${id === 'swipe' && V.sb.modus === 'frei' ? `</div>${stapelHTML()}</div>` : ''}`);
}

/* ---------- Prüfung: Übungsklausur je Oberthema / Refresh-Sprint (Bogen und Auswertung in pruefung.js) ---------- */
const verfallText = st => !st ? 'noch nicht geprüft' : st.faellt ? `vor ${st.tage} Tagen ${st.s} %, jetzt ${st.pct} % · verblasst` : `${st.pct} % · hält noch ${st.haeltNoch} ${st.haeltNoch === 1 ? 'Tag' : 'Tage'}`;
/* Probeklausur: Deckblatt wie die echte Klausur, dann der Bogen mit Teilen je Fach */
function probe() {
  const kl = probeKl(V.pr.probe);
  if (kl.teile.filter(t => F[t[1]]).every(t => F[t[1]].klausur)) return probeBogen(kl);
  if (!V.pr.items) V.pr.items = probeAufgaben(kl);
  const it = V.pr.items, summe = it.reduce((s, x) => s + x.max, 0), fs = kl.teile.filter(t => F[t[1]]);
  if (V.pr.zeit == null) V.pr.zeit = S.einst.zeitlimit !== false;
  const verlauf = (S.probe || {})[kl.kurz] || [], letzt = verlauf[verlauf.length - 1];
  return rahmen(`<div class="cpr"><header class="tile cpr-h pk-deck" style="--c:var(--x-sun)"><small>Probeklausur · echte Klausur am ${datumKurz(kl.beginn)}, in ${tageBis(kl.beginn)} Tagen</small><h1>${esc(kl.titel || kl.kurz)}</h1><h2>${esc(kl.kurz)}</h2></header>
    <section class="tile cpr-b">${V.pr.laeuft || V.pr.fertig ? '' : `
      <div class="pk-blatt"><div class="pk-zeile"><span>Bearbeitungszeit</span><b>${V.pr.zeit ? (kl.minuten || summe) + ' Minuten' : 'ohne Zeitlimit'}</b></div>
        <div class="pk-zeile"><span>Punkte</span><b>${summe}</b></div>
        ${fs.map((t, i) => { const f = F[t[1]], n = it.filter(x => x.teil === i); return `<div class="pk-zeile" style="--fach:${f.farbe}"><span>Teil ${i + 1} · ${esc(f.name)}</span><b>${n.reduce((s, x) => s + x.max, 0)} P · ${n.length} Aufgaben</b></div>`; }).join('')}
        <div class="pk-zeile"><span>Bewertung</span><b>Note nach der DHBW-Tabelle</b><small>Auswahl, Zahlen, Zuordnen werden automatisch bewertet, Textantworten bewertest du nach dem Abgeben selbst.</small></div></div>
      ${letzt ? `<p class="dim3">Letzte Probeklausur: ${zahl(letzt.hat, 1)} von ${letzt.summe} Punkten, Note ${noteText(letzt.note)}.</p>` : ''}
      <label class="pr-zeit"><input type="checkbox" data-act="pr-zeit" ${V.pr.zeit ? 'checked' : ''}> mit Zeitlimit wie in der echten Klausur</label>
      <div><button class="btn btn-main" data-act="pr-start">Beginnen</button><button class="btn" data-go="sb">Zurück zum Training</button></div>`}
      <div data-mount="pruef"></div></section></div>`);
}
/* Probeklausur als Bogen wie die echte Klausur (Deckblatt, Aufgaben mit a) b) c), „Zu a)“-Feldern) */
function probeBogen(kl) {
  if (!V.pr.bogen) V.pr.bogen = klausurZiehen(kl);
  const B = V.pr.bogen, verlauf = (S.probe || {})[kl.kurz] || [], letzt = verlauf[verlauf.length - 1];
  if (V.pr.zeit == null) V.pr.zeit = S.einst.zeitlimit !== false;
  return rahmen(`<div class="cpr"><header class="tile cpr-h pk-deck" style="--c:var(--x-sun)"><small>Probeklausur · echte Klausur am ${datumKurz(kl.beginn)}, in ${tageBis(kl.beginn)} Tagen</small><h1>${esc(kl.titel || kl.kurz)}</h1><h2>Aufbau, Punkte und Zeit wie in der echten Klausur</h2></header>
    ${V.pr.laeuft ? '' : `<section class="tile cpr-b">${kbDeckblatt(B)}
      <p class="dim3">Jede Probeklausur wird neu zusammengestellt: je Teilaufgabe eine passende Aufgabe aus dem Stoff, bevorzugt eine, die du länger nicht hattest. Zahlen, Mengen, Terme und Matrizen werden automatisch geprüft (Terme gelten, wenn sie gleichwertig sind). Textantworten bewertest du nach dem Abgeben selbst.</p>
      ${letzt ? `<p class="dim3">Letzte Probeklausur: ${zahl(letzt.hat, 1)} von ${letzt.summe} Punkten, Note ${noteText(letzt.note)}.</p>` : ''}
      <label class="pr-zeit"><input type="checkbox" data-act="pr-zeit" ${V.pr.zeit ? 'checked' : ''}> mit Zeitlimit wie in der echten Klausur (${kl.minuten || kbSumme(B)} Minuten)</label>
      <div><button class="btn btn-main" data-act="pr-start">Beginnen</button><button class="btn" data-go="sb">Zurück zum Training</button></div></section>`}
    ${V.pr.laeuft ? '<div data-mount="kbogen"></div>' : ''}</div>`);
}
function probeErgebnisHTML(kl, items, hat, summe) {
  verbucheProbe(kl, items, hat, summe);
  const n = note(hat, summe), teile = kl.teile.filter(t => F[t[1]]);
  const w = [...new Map(items.filter(it => it.p < it.max * .5).map(it => [it.key, it.t])).values()];
  return `<div class="erg"><div class="erg-zahl"><span>${noteText(n)}</span><small>Note</small></div>
    <p class="erg-note"><b>${zahl(hat, 1)} von ${summe} Punkten · ${Math.round(hat / summe * 100)} %</b>${n > 4 ? '<small>nicht bestanden</small>' : '<small>bestanden</small>'}</p>
    <div class="pk-teile">${teile.map((t, i) => { const its = items.filter(x => x.teil === i), h = its.reduce((s, x) => s + (x.p || 0), 0), m = its.reduce((s, x) => s + x.max, 0);
      return `<div style="--fach:${F[t[1]].farbe}"><span>${esc(F[t[1]].name)}</span><b>${zahl(h, 1)} / ${m} P</b><span class="pk-bar"><i style="width:${m ? h / m * 100 : 0}%"></i></span></div>`; }).join('')}</div>
    ${w.length ? `<div class="erg-w"><b>Hier hat es gehakt</b><ul>${w.slice(0, 8).map(t => `<li>${esc(t.title)}</li>`).join('')}</ul><small>Die falschen Aufgaben liegen jetzt in „Methodisch lernen“. Der Stand der geprüften Oberthemen ist aktualisiert.</small></div>` : ''}
    <div class="erg-act"><button class="btn btn-main" data-go="sb">Zum Training</button><button class="btn" data-go="sbm">Methodisch lernen</button><button class="btn" data-act="pr-neu">Neue Probeklausur</button></div>
    <p class="dim3">Unten siehst du jede Aufgabe mit Lösung.</p></div>`;
}
function pruef() {
  if (V.pr.probe) return probe();
  const f = F[V.pr.fid], k = f.kapitel.find(y => y.id === V.pr.kid), st = stand(f.id, k.id), end = V.pr.modus === 'end';
  const kl = klausurVon(f.id), j = Math.max(0, klausurenSortiert().indexOf(kl));
  if (!V.pr.items) V.pr.items = end ? klausurAufgaben(f, k) : refreshAufgaben(f, k);
  const it = V.pr.items, summe = it.reduce((s, x) => s + x.max, 0), nA = it.filter(x => TEIL(x) === 'A').length;
  if (V.pr.zeit == null) V.pr.zeit = S.einst.zeitlimit !== false;
  return rahmen(`<div class="cpr"><header class="tile cpr-h" style="--c:${BUNT[j]}"><small>${esc(f.name)}${kl ? ` · zählt für ${esc(kl.kurz)} in ${tageBis(kl.beginn)} Tagen` : ''}</small><h1>${end ? 'Übungsklausur' : '5-Minuten-Refresh'}</h1><h2>${esc(k.title)}</h2></header>
    <section class="tile cpr-b">${V.pr.laeuft || V.pr.fertig ? '' : `
      <div class="pr-fakten"><span><b>${it.length}</b> Aufgaben</span><span><b>${summe}</b> Punkte</span><span><b>${V.pr.zeit ? summe + ' min' : 'ohne'}</b> Zeit</span><span>Stand: ${verfallText(st)}</span></div>
      <p>${end ? `Aufgebaut wie die Klausur: zuerst ${nA} kurze Aufgaben (Teil A), dann ${it.length - nA} größere (Teil B). ${it.ausgelassen && it.ausgelassen.length ? `Diesmal ${k.topics.length - it.ausgelassen.length} von ${k.topics.length} Unterthemen, damit es bei 45 Minuten bleibt; die übrigen kommen beim nächsten Mal zuerst.` : 'Jedes Unterthema kommt mindestens einmal dran.'} Keine Tipps, keine Lösung zwischendurch, abgerechnet wird nach der Abgabe. Erklärfragen bewertest du danach ehrlich selbst anhand der Lösung. Unterthemen mit weniger als der Hälfte der Punkte werden zu Wackelthemen.`
        : `${it.length} kurze Fragen${(S.pruef[f.id + '/' + k.id] || {}).falsch?.length ? ', zuerst aus Unterthemen, die zuletzt nicht saßen' : ''}. Mindestens 75 %: Der Stand ist wieder frisch und hält danach doppelt so lange. Darunter sinkt er weiter.`}</p>
      <label class="pr-zeit"><input type="checkbox" data-act="pr-zeit" ${V.pr.zeit ? 'checked' : ''}> mit Zeitlimit (1 Punkt ≈ 1 Minute, wie in der Klausur)</label>
      <div><button class="btn btn-main" data-act="pr-start">Beginnen</button><button class="btn" ${goLern(f.id, k.id)}>Zurück zum Oberthema</button></div>`}
      <div data-mount="pruef"></div></section></div>`);
}
function ergebnisHTML(fid, kid, modus, items, hat, summe) {
  const e = modus === 'end' ? verbucheKlausur(fid, kid, items, hat, summe) : verbucheRefresh(fid, kid, items, hat, summe);
  const w = [...new Map(e.schwach.map(it => [it.key, it.t])).values()];
  const txtE = modus === 'end' ? `${zahl(hat, 1)} von ${summe} Punkten.${e.vorher ? ` Vorher ${e.vorher.pct} %.` : ''} Der Stand hält ${haltbarkeit(e.s)} Tage, danach verblasst er langsam.`
    : !e.nachher ? 'Für dieses Oberthema gibt es noch keine Übungsklausur.' : e.gut ? `${hat} von ${summe} Punkten. Wieder frisch, hält jetzt ${e.h} Tage.` : `${hat} von ${summe} Punkten. Unter 75 %: Der Stand sinkt auf ${e.nachher.pct} %.`;
  const n = note(hat, summe);
  return `<div class="erg"><div class="erg-zahl"><span>${e.nachher ? e.nachher.pct : Math.round(hat / summe * 100)}</span><small>%</small></div>
    <p class="erg-note"><b>entspricht Note ${noteText(n)}</b>${n > 4 ? ' · nicht bestanden' : ''}<small>nach der DHBW-Notentabelle, umgerechnet auf 60 Punkte</small></p><p class="erg-txt">${txtE}</p>
    ${w.length ? `<div class="erg-w"><b>Hier hat es gehakt</b><ul>${w.map(t => `<li>${esc(t.title)}</li>`).join('')}</ul><small>Die falschen Aufgaben liegen jetzt in „Methodisch lernen“.</small></div>` : '<p class="erg-txt">Alles gut gegangen.</p>'}
    <div class="erg-act"><button class="btn btn-main" data-go="dash">Zur Übersicht</button>${w.length ? `<button class="btn" data-go="sbw|${fid}|${kid}">Rote Unterthemen trainieren</button>` : ''}<button class="btn" data-act="pr-neu">Neue Übungsklausur</button></div>
    <p class="dim3">Unten siehst du jede Aufgabe mit Lösung. „Im Text nachschlagen“ führt zur passenden Stelle.</p></div>`;
}

/* ---------- Einstellungen ---------- */
/* ---------- Fehler melden: Meldungen werden im Lernstand gesammelt (S.meldungen) und in den Einstellungen gezeigt ---------- */
function meldeDialog(ort) {
  document.querySelector('.melde-dlg')?.remove();
  const sel = String(getSelection ? getSelection() : '').trim().slice(0, 300);
  const d = document.createElement('div'); d.className = 'melde-dlg';
  d.innerHTML = `<div class="melde-box" role="dialog" aria-label="Fehler melden"><b>Fehler oder Unklarheit melden</b><small>${esc(ort)}</small>
    ${sel ? `<blockquote>${esc(sel)}</blockquote>` : ''}<textarea rows="4" placeholder="Was stimmt nicht oder ist unklar? (z. B. falsche Lösung, Tippfehler, schwer verständlich)"></textarea>
    <div class="melde-act"><button class="btn btn-main" data-m="ok">Absenden</button><button class="btn" data-m="weg">Abbrechen</button></div></div>`;
  document.body.appendChild(d); const ta = d.querySelector('textarea'); ta.focus();
  d.addEventListener('click', e => {
    const m = e.target.dataset && e.target.dataset.m; if (e.target === d || m === 'weg') return d.remove(); if (m !== 'ok') return;
    if (!ta.value.trim()) { ta.focus(); return; }
    (S.meldungen = S.meldungen || []).push({ d: new Date().toISOString(), ort, sel, text: ta.value.trim() }); save(); d.remove();
    hinweis(typeof SYNC === 'object' && SYNC && SYNC.an ? 'Danke! Die Meldung ist abgeschickt und unter Einstellungen → Meldungen gespeichert.' : 'Danke! Die Meldung ist gespeichert (Einstellungen → Meldungen).');
  });
}
document.addEventListener('click', e => { const b = e.target.closest && e.target.closest('[data-melde]'); if (b) { e.preventDefault(); e.stopPropagation(); meldeDialog(b.dataset.melde); } }, true);
/* ---------- Neu anfangen: Lernstand auf null setzen (auswählbar; zweimal bestätigen). Meldungen und Einstellungen bleiben. ---------- */
const NEU_TEILE = [['fort', 'Lernfortschritt', 'Abdeckung, Stufen, Wiederholungen, Prüfungs- und Probeklausur-Ergebnisse, „unsicher“, Nutzungszeiten',
  ['g', 'pruef', 'probe', 'ks', 'wackel', 'unsicher', 'zuletzt', 'zuletztF', 'kbGesehen', 'wserie', 'nutzung', 'nutzZuletzt']],
  ['mark', 'Markierungen und Notizen', 'alle farbigen Stellen, Unterstreichungen und Notizen', ['mark', 'notiz']],
  ['eigen', 'Eigene Karteikarten', 'selbst angelegte Karten', ['eigen']]];
function neuStartHTML() {
  return `<section class="tile neu-start"><h2>Neu anfangen</h2><p class="dim3">Setzt Lernweh auf null, für einen frischen Durchlauf. Wähle, was gelöscht wird. Meldungen und Einstellungen bleiben.</p>
    ${NEU_TEILE.map(([k, n, w]) => `<label class="neu-z"><input type="checkbox" data-neu="${k}" ${k === 'fort' ? 'checked' : ''}><span><b>${n}</b><small>${w}</small></span></label>`).join('')}
    <div class="melde-act"><button class="btn" data-act="neu-start">Ausgewähltes löschen …</button></div></section>`;
}
function neuStart(b) {
  const wahl = [...document.querySelectorAll('[data-neu]:checked')].map(x => x.dataset.neu); if (!wahl.length) { hinweis('Bitte zuerst auswählen, was gelöscht werden soll.'); return; }
  if (!b.dataset.sicher) { b.dataset.sicher = '1'; b.classList.add('btn-main'); b.textContent = 'Wirklich löschen? Das lässt sich nicht rückgängig machen.'; return; }
  for (const [k, , , felder] of NEU_TEILE) if (wahl.includes(k)) for (const f of felder) { if (S[f] && typeof S[f] === 'object' && !Array.isArray(S[f])) S[f] = {}; else delete S[f]; }
  save(); b.disabled = true; b.textContent = 'Gelöscht. Lernweh startet neu …';
  const neu = () => location.reload();
  if (typeof SYNC === 'object' && SYNC.an && typeof syncSenden === 'function') syncSenden().finally(neu); else setTimeout(neu, 400);
}
function meldungenHTML() {
  const m = S.meldungen || [];
  return `<section class="tile"><h2>Meldungen</h2><p class="dim3">Fehler und Unklarheiten, die du über „⚑ Fehler melden“ gespeichert hast. Kopieren und an die Betreuung des LernTools schicken; danach kannst du sie löschen.</p>
    ${m.length ? `<ol class="melde-liste">${m.map(x => `<li><small>${esc(x.d.slice(0, 10))} · ${esc(x.ort)}</small>${x.sel ? `<q>${esc(x.sel)}</q>` : ''}<span>${esc(x.text)}</span></li>`).join('')}</ol>
    <div class="melde-act"><button class="btn btn-main" data-act="melde-kopie">Alle kopieren (${m.length})</button><button class="btn" data-act="melde-loesch">Alle löschen</button></div>` : '<p class="dim3">Noch keine Meldungen.</p>'}</section>`;
}
function einst() {
  const th = S.einst.theme || 'system';
  return rahmen(`<header class="b7-top"><h1>Einstellungen</h1></header>
    <div class="ein">
      ${D.faecher.some(f => f.folien) ? `<section class="tile ein-fo"><h2>Originalfolien</h2><p class="dim3">Alle Folien, Skripte und Übungsblätter, wie sie im PDF stehen. Neben jeder Seite steht, auf welcher Lernseite der Stoff erklärt ist und ob die Aufgaben als Aufgabe eingebaut sind. So prüfst du selbst, was drin ist.</p>
        <div class="ein-fo-l">${D.faecher.filter(f => f.folien).map(f => `<button class="btn" style="--fach:${f.farbe}" data-go="folien|${f.id}"><i class="ein-fo-p"></i>${esc(f.name)} <small>${f.folien.s} S.</small></button>`).join('')}</div></section>` : ''}
      <section class="tile"><h2>Darstellung</h2><div class="seg">${[['system', 'Wie das Gerät'], ['light', 'Hell'], ['dark', 'Dunkel']].map(([v, n]) => `<button class="${th === v ? 'on' : ''}" data-act="theme" data-v="${v}" aria-pressed="${th === v}">${n}</button>`).join('')}</div></section>
      <section class="tile"><h2>Testdatum</h2><p class="dim3">Verschiebt „heute“, um Verfall und Countdown auszuprobieren. Für normales Lernen auf 0 lassen.</p>
        <label class="ein-zeile">Tage in die Zukunft <input type="number" min="0" max="120" value="${S.einst.testTage || 0}" data-act="testtage"></label></section>
      ${testHTML()}
      ${meldungenHTML()}
      ${neuStartHTML()}
      ${(typeof syncEinstHTML === 'function' && syncEinstHTML()) || '<section class="tile"><h2>Lernstand</h2><p class="dim3">Prüfungsstände, Stufen je Aufgabe, Karteikarten-Sitzungen und „Weiterlesen“ speichert dieser Browser auf diesem Gerät.</p></section>'}
    </div>`);
}

/* ---------- Vorschau (nur im Artifact und lokal, nie online): so tun, als hätte man alles schon vor der Überarbeitung bearbeitet ----------
   Setzt Testdaten: alle überarbeiteten Unterthemen als „schon gekannt“ (gold), alle angepassten Fragen als „schon gekonnt“ (Nacharbeiten),
   Pflicht-Hinweis wieder offen. Der Lernstand von vorher wird gesichert und lässt sich wiederherstellen. */
const VORSCHAU = location.protocol === 'file:' || /claude|usercontent|localhost|127\.0\.0\.1/.test(location.hostname);
const TEST_KEY = 'lw-test-vorher';
function testHTML() {
  if (!VORSCHAU) return '';
  let aktiv = false; try { aktiv = !!localStorage.getItem(TEST_KEY); } catch (e) { }
  return `<section class="tile"><h2>Vorschau: Überarbeitung ausprobieren</h2><p class="dim3">Nur in dieser Vorschau. Tut so, als hättest du alle überarbeiteten Unterthemen und die angepassten Fragen schon vorher bearbeitet: Dann siehst du den gelben Pflicht-Hinweis und im Training „Nacharbeiten“.</p>
    <div class="ein-fo-l"><button class="btn btn-main" data-act="test-an">${aktiv ? 'Testdaten neu setzen' : 'Testdaten setzen'}</button>${aktiv ? '<button class="btn" data-act="test-aus">Testdaten entfernen</button>' : ''}</div></section>`;
}
function testSetzen(an) {
  try {
    if (!an) { const alt = localStorage.getItem(TEST_KEY); if (alt) { for (const k of Object.keys(S)) delete S[k]; Object.assign(S, JSON.parse(alt)); save(); localStorage.removeItem(TEST_KEY); } location.reload(); return; }
    if (!localStorage.getItem(TEST_KEY)) localStorage.setItem(TEST_KEY, JSON.stringify(S));
  } catch (e) { }
  S.kannte = S.kannte || {}; S.nach = []; S.einst.dringend = {};
  for (const [key, x] of Object.entries(TOP)) if ((x.t.nz || []).length) S.kannte[key] = [];
  for (const f of D.faecher) for (const l of Object.values(f.nach || {})) for (const [fam, i, y, tid] of l) {
    const id = `q:${fam}:${y}`; S.g[id] = S.g[id] || { s: 4, e: G.tag() - 30, d: G.tag() - 30, t: Date.now() - 30 * DAY, k: f.id + '/' + tid };
    S.nach.push(`${f.id}|${fam}|${i}|${y}|${tid}`);
  }
  for (const f of D.faecher) for (const [fam, i, y, tid] of f.nachNz || []) S.nach.push(`${f.id}|${fam}|${i}|${y}|${tid}`);
  save(); G.cache = null; go('dash');
}
/* ---------- Nacharbeiten: nur sichtbar, solange es überarbeitete Fragen gibt, die man vor der Überarbeitung schon bearbeitet hatte (S.nach, gedaechtnis.js) ---------- */
function nachBand() {   // nur für Lernende, die wirklich etwas nachzuarbeiten haben
  const n = (S.nach || []).length; if (!n) return '';
  return `<button class="mm-band nach-band" data-act="nach"><span><small>Überarbeitete Fragen und neuer Stoff in Unterthemen, die du schon kanntest</small><b>Nacharbeiten</b></span><em><b>${n}</b> ${n === 1 ? 'Frage' : 'Fragen'}</em></button>`;
}
function nacharbeiten() {
  /* Läuft wie das Endlos-Quiz: so lange, bis alles sitzt oder man schließt. Falsch Beantwortetes kommt später in derselben Sitzung wieder. */
  document.getElementById('ov')?.remove();
  if (!(S.nach || []).length) return;
  document.body.insertAdjacentHTML('beforeend', `<div id="ov" class="ov app" role="dialog" aria-modal="true"><div class="ov-box"><div class="ov-kopf"><b>Nacharbeiten</b><span>Fragen zu neuem oder überarbeitetem Stoff in Unterthemen, die du schon kanntest. Richtig beantwortet ist eine Frage erledigt; was nicht sitzt, kommt in „Methodisch lernen“.</span><button class="btn" data-act="ov-zu">Schließen</button></div><div class="ov-body"><p class="leer">Wird geladen …</p></div></div></div>`);
  const body = document.querySelector('#ov .ov-body'), zu = () => { if (V.screen === 'sb') render(); };
  document.querySelector('#ov [data-act="ov-zu"]').addEventListener('click', zu);
  const item = k => { const [fid, fam, i, y, tid] = k.split('|'), x = TOP[fid + '/' + tid], q = x && (x.t.fragen || []).find(f => f.id === fam);
    if (y === 'def') {   // Nachschärf-Karte: bekannte Fassung → Folien-Definition (Kernpunkte fett), selbst bewerten
      const d = x && (x.f.defs || {})[fam]; if (!q || !d) return null;
      return { a: { y: 'karte', fach: 'Definition nachschärfen · ' + x.f.name, p: `„${d.b}“ – so kennst du es: ${txt(d.e)} · Wie sagt es die Folie genau?`,
          l: `<div class="def-nach"><p class="def-folie">${d.w}</p><small>Gold = die Kernpunkte der Folie. „Gewusst“, wenn du sie inhaltlich drin hattest.</small></div>` },
        key: fid + '/' + tid, f: x.f, k: x.k, t: x.t, fam: q, x: { key: fid + '/' + tid, f: x.f, k: x.k, t: x.t }, gid: `q:${fam}:rev`, gv: { i: -1 }, def: true };
    }
    return q && q.a[+i] && q.a[+i].y === y ? frageItem({ key: fid + '/' + tid, f: x.f, k: x.k, t: x.t }, q, q.a[+i]) : null; };
  LT.lade(S.nach.map(k => k.split('|')[0])).then(() => {
    S.nach = S.nach.filter(k => !!item(k)); save();   // nicht mehr vorhandene Fragen fallen weg
    if (!S.nach.length) { body.innerHTML = '<p class="leer">Alles nachgearbeitet.</p>'; return; }
    /* Ohne Zehnerrunden: alles Offene nacheinander. Jede Frage kommt hier genau einmal: richtig = erledigt,
       falsch = raus aus „Nacharbeiten“ und wie gewohnt in „Methodisch lernen“ (die Antwort verbucht G.antwort). */
    let reihe = S.nach.slice(), zuletzt = '', beantwortet = 0;
    quiz(body, {
      next: (i, res) => {
        if (zuletzt && res.length > beantwortet) {
          const l = res[res.length - 1];
          if (l && l.item.def && l.ok) for (const y of ['rev', 'luecke']) {   // nachgeschärft: Definitionsfrage gilt als „fast sicher“, nicht von vorn
            const id = `q:${l.item.fam.id}:${y}`, e = S.g[id] || (S.g[id] = { e: G.tag() }); e.s = Math.max(Math.min(e.s || 0, 3), 3); e.d = G.tag(); e.t = Date.now(); e.k = l.item.key; }
          S.nach = S.nach.filter(k => k !== zuletzt); beantwortet = res.length; save(); }
        reihe = reihe.filter(k => S.nach.includes(k));
        while (reihe.length) { const k = reihe.shift(), it = item(k); if (it) { zuletzt = k; return it; } }
        zuletzt = ''; return null;
      },
      kopf: (i, res, it) => `<span class="q-zaehl">Noch ${S.nach.length} offen · ${esc(it.f.name)} · ${esc(it.t.title)}</span>`,
      onEnd: (res, box) => { const ok = res.filter(r => r.ok).length;
        box.innerHTML = `<div class="mini-end"><b>Alles nachgearbeitet.</b> ${ok} von ${res.length} richtig.${ok < res.length ? ' Was nicht saß, kommt in „Methodisch lernen“ wieder.' : ''}</div>`; } });
  }).catch(() => { body.innerHTML = '<p class="leer">Konnte nicht geladen werden.</p>'; });
}
/* ---------- Werkzeuge einhängen ---------- */
function miniQuiz(el) {
  const x = cur(), key = x.f.id + '/' + x.t.id;
  const items = ziehFragen([{ key, f: x.f, k: x.k, t: x.t }], 5, 'leicht');
  if (!items.length) { el.innerHTML = '<div class="leer">Zu diesem Unterthema gibt es noch keine Fragen.</div>'; return; }
  quiz(el, { next: i => items[i] || null, kopf: i => `<span class="q-zaehl">Frage ${i + 1} von ${items.length}</span>`,
    onEnd: (res, box) => {
      const ok = res.filter(r => r.ok).length;
      box.innerHTML = `<div class="mini-end"><b>${ok} von ${res.length} richtig.</b> ${ok < res.length ? 'Was nicht saß, kommt in „Methodisch lernen“ wieder.' : 'Grob verstanden. Weiter zum nächsten Unterthema.'}
        <button class="btn" data-act="quiz">Nochmal</button></div>`;
      document.querySelectorAll('.bl-rail button.on .st, .bdg-st .st').forEach(e => e.outerHTML = G.punkt(key));
    } });
}
function karteOverlay(pool) {
  document.getElementById('ov')?.remove();
  document.body.insertAdjacentHTML('beforeend', `<div id="ov" class="ov app" role="dialog" aria-modal="true"><div class="ov-box"><div class="ov-kopf"><b>Karteikarten</b><span>${esc(pool[0].k.title)}</span><button class="btn" data-act="ov-zu">Schließen</button></div><div class="ov-body"></div></div></div>`);
  const body = document.querySelector('#ov .ov-body'); swipe(body, kartenFuer(pool), { sitzung: sitzungVon(pool) }); body.focus();
  document.getElementById('ov').onclick = e => { if (e.target.id === 'ov') e.target.remove(); };
}
/* gleichbedeutende Suchwörter (in beide Richtungen) */
const SUCH_SYN = (() => { const g = [['Determinanten', 'Bestimmungsgrößen', 'Einflussfaktoren', 'Einflussgrößen'], ['Kriterien', 'Merkmale'], ['Ziele', 'Zielsetzungen'],
  ['Vorteile', 'Stärken'], ['Nachteile', 'Schwächen'], ['Arten', 'Formen', 'Typen'], ['Funktionen', 'Aufgaben']], m = {};
  for (const l of g) for (const w of l) m[norm(w)] = l.filter(v => v !== w); return m; })();
function sucheOverlay() {
  document.getElementById('ov')?.remove();
  document.body.insertAdjacentHTML('beforeend', `<div id="ov" class="ov app ov-pal" role="dialog" aria-modal="true" aria-label="Suche"><div class="ov-box"><input class="pal-in" placeholder="Unterthema, Begriff oder Notiz suchen …" aria-label="Suchbegriff"><div class="pal-list"></div></div></div>`);
  const inp = document.querySelector('.pal-in'), list = document.querySelector('.pal-list');
  const zeig = () => {
    const q = norm(inp.value), hits = [];
    for (const [k, x] of Object.entries(TOP)) if (!q || norm(x.t.title + x.k.title + x.f.name).includes(q)) hits.push(`<button class="pal-it" data-go="lern|${x.f.id}|${x.k.id}|${x.t.id}"><span>${esc(x.t.title)}</span><small>${esc(x.f.name)} · ${esc(x.k.title)}</small></button>`);
    if (q.length > 2) for (const [key, ms] of Object.entries(S.mark)) for (const m of ms) if (TOP[key] && norm(m.text + ' ' + m.notiz).includes(q)) { const x = TOP[key];
      hits.unshift(`<button class="pal-it" data-go="lern|${x.f.id}|${x.k.id}|${x.t.id}"><span>${esc(m.notiz || m.text.slice(0, 80))} <em>markiert</em></span><small>${esc(x.f.name)} · ${esc(x.t.title)}</small></button>`); }
    if (q.length > 2) for (const [key, n] of Object.entries(S.notiz)) if (TOP[key] && norm(n).includes(q)) { const x = TOP[key];
      hits.unshift(`<button class="pal-it" data-go="lern|${x.f.id}|${x.k.id}|${x.t.id}"><span>${esc(n.slice(0, 90))} <em>Notiz</em></span><small>${esc(x.f.name)} · ${esc(x.t.title)}</small></button>`); }
    if (q.length > 2) for (const f of D.faecher) for (const g of (f.glossar || [])) if (norm(g.b).includes(q) && TOP[f.id + '/' + g.t]) { const x = TOP[f.id + '/' + g.t];
      hits.push(`<button class="pal-it" data-go="lern|${f.id}|${x.k.id}|${x.t.id}"><span>${esc(g.b)} <em>Begriff</em></span><small>${esc(g.e.slice(0, 110))}</small></button>`); }
    if (q.length > 3) {   // Volltext: Erklärungen, Merksätze, Kernsätze aller geladenen Lernseiten (mit gleichbedeutenden Wörtern)
      const roh = inp.value.trim(), worte = [roh, ...(SUCH_SYN[norm(roh)] || [])], qs = worte.map(norm); let n = 0;
      for (const x of Object.values(TOP)) {
        if (n >= 10 || !x.t.html) continue;
        const text = x.t.html + ' ' + (x.t.merk || '') + ' ' + (x.t.kern || ''), tn = norm(text);
        if (!qs.some(w => tn.includes(w)) || hits.some(h => h.includes(`|${x.t.id}"`))) continue;
        const klar = text.replace(/<(script|style)[^>]*>[\s\S]*?<\/\1>/g, ' ').replace(/<[^>]+>/g, ' ').replace(/&amp;/g, '&').replace(/&[a-z]+;/g, ' ').replace(/\s+/g, ' '), kl = klar.toLowerCase();
        const w = worte.find(v => kl.includes(v.toLowerCase())) || roh, i = Math.max(0, kl.indexOf(w.toLowerCase()));
        const aus = (i > 40 ? '… ' : '') + klar.slice(Math.max(0, i - 40), i + 90) + ' …';
        hits.push(`<button class="pal-it" data-go="lern|${x.f.id}|${x.k.id}|${x.t.id}"><span>${esc(x.t.title)} <em>im Text</em></span><small>${esc(aus)}</small></button>`); n++;
      }
    }
    list.innerHTML = hits.slice(0, 20).join('') || '<p class="dim3">Nichts gefunden.</p>';
  };
  inp.oninput = zeig; zeig(); inp.focus();
  LT.lade(D.faecher.map(f => f.id)).then(zeig).catch(() => {});   // Begriffe aller Fächer nachladen
  list.addEventListener('click', () => document.getElementById('ov')?.remove());
  document.getElementById('ov').onclick = e => { if (e.target.id === 'ov') e.target.remove(); };
}
function montiere() {
  const fm = document.querySelector('[data-mount="folien"]'); if (fm && typeof foMontiere === 'function') foMontiere(fm);
  const m = document.querySelector('[data-mount="mini"]'); if (m && V.quizOffen) miniQuiz(m);
  const b = document.querySelector('[data-mount="ueben"]'); if (b) { const x = cur(); blatt(b, [{ key: V.fid + '/' + V.tid, f: x.f, k: x.k, t: x.t }], { n: 3, stufe: 'grund', kopf: false }); }
  const s = document.querySelector('[data-mount="sb"]');
  if (s) {
    const pool = sbPool();
    if (!pool.length) s.innerHTML = leer(V.sb.wackel ? 'Keine roten Unterthemen' : 'Kein Fach gewählt', V.sb.wackel ? 'In dieser Auswahl wackelt nichts. Schön.' : 'Links mindestens ein Fach antippen.');
    else if (V.sb.seite === 'methodisch') methodisch(s, { keys: new Set(pool.map(x => x.key)) });
    else if (V.sb.modus === 'methodisch') methodisch(s, { w: WERKZEUG_ART[V.sb.tool], keys: new Set(pool.map(x => x.key)) });
    else if (V.sb.tool === 'swipe') { const z = V.sb.stapel && S.ks[V.sb.stapel], dp = z && z.keys.length ? z.keys.filter(k => TOP[k]).map(k => ({ key: k, ...TOP[k] })) : pool;
      swipe(s, kartenFuer(dp), { sitzung: z ? V.sb.stapel : sitzungVon(dp), name: z ? z.name : sbZusammenfassung(), keys: dp.map(x => x.key) }); }
    else if (V.sb.tool === 'drill' && V.sb.dmodus === 'schreiben') drillSchreiben(s, pool, (st, best, res) => `<span class="drill-streak">Serie <b>${st}</b></span><span class="drill-best">Rekord ${best} · ${res.length} gespielt</span>`);
    else if (V.sb.tool === 'drill') drill(s, pool, (st, best, res) => `<span class="drill-streak">Serie <b>${st}</b></span><span class="drill-best">Rekord ${best} · ${res.length} gespielt${st >= 5 ? ' · jetzt eintippen' : ''}</span>`, 'klausur');
    else if (V.sb.tool === 'quiz') { const e = endlos(pool);
      quiz(s, { next: (i, res) => e.next(i, res), kopf: (i, res, it) => `${e.schwerer ? '<span class="q-hoch">jetzt schwerer</span>' : ''}<span class="q-zaehl">Serie ${e.serie} · ${res.filter(r => r.ok).length} / ${res.length} richtig</span>` }); }
    else blatt(s, pool, { n: 5, stufe: V.sb.stufe, arten: V.sb.arten, titel: sbZusammenfassung() });
  }
  const kb = document.querySelector('[data-mount="kbogen"]');
  if (kb && V.pr && V.pr.bogen) { const kl = V.pr.bogen.kl; if (V.pr.bogen.el !== kb) { V.pr.bogen.el = kb; klausurBogen(kb, V.pr.bogen, { minuten: V.pr.zeit ? (kl.minuten || kbSumme(V.pr.bogen)) : 0 }); } }
  const p = document.querySelector('[data-mount="pruef"]');
  if (p && V.pr && V.pr.laeuft) {
    if (V.pr.probe) { const kl = probeKl(V.pr.probe), items = V.pr.items, summe = items.reduce((s, x) => s + x.max, 0);
      pruefungsBogen(p, items, { minuten: V.pr.zeit ? (kl.minuten || summe) : 0, abschnitt: it => `Teil ${it.teil + 1} · ${esc(it.teilName)}`,
        fertig: (its, hat, sum) => { V.pr.laeuft = false; V.pr.fertig = true; return probeErgebnisHTML(kl, its, hat, sum); } });
      timerUpd(); return; }
    const { fid, kid, modus, items } = V.pr, summe = items.reduce((s, x) => s + x.max, 0);
    pruefungsBogen(p, items, { minuten: V.pr.zeit ? (modus === 'end' ? summe : Math.max(5, summe)) : 0,
      fertig: (its, hat, sum) => { V.pr.laeuft = false; V.pr.fertig = true; return ergebnisHTML(fid, kid, modus, its, hat, sum); } });
  }
  timerUpd();
}

/* ---------- Zeichnen ---------- */
/* Originalfolien: Inhalt aus folien.js (lädt nach) */
function folien() { return typeof folienAnsicht === 'function' ? folienAnsicht() : rahmen(`<h1>Originalfolien</h1><div data-mount="folien"></div>`); }
const ANSICHT = { dash, lern, sb, pruef, einst, folien };
function brauchtFaecher() {
  if (V.screen === 'lern') return [V.fid];
  if (V.screen === 'sb') return V.sb.wackel ? D.faecher.map(f => f.id) : V.sb.seite === 'methodisch' || V.sb.modus === 'methodisch' ? [...new Set(G.faelligListe().map(z => z.e.k.split('/')[0]))].filter(f => V.sb.f.includes(f)) : V.sb.f;
  if (V.screen === 'pruef' && V.pr && V.pr.probe) return (probeKl(V.pr.probe) || { faecher: [] }).faecher.filter(f => F[f]);
  if (V.screen === 'pruef' && V.pr) return [V.pr.fid];
  return [];
}
let renderNr = 0;
function render(nachOben) {
  const nr = ++renderNr, app = document.getElementById('app'), fids = brauchtFaecher();
  document.getElementById('glo-pop')?.remove(); document.querySelector('.mk-leiste')?.remove();
  if (location.hash.slice(1) !== adresse()) history.replaceState(null, '', '#' + adresse());
  if (!geladen(fids)) {
    app.innerHTML = rahmen(`<div class="laden" role="status">Lade ${fids.filter(f => !F[f].geladen).map(f => esc(F[f].name)).join(', ')} …</div>`);
    LT.lade(fids).then(() => { if (nr === renderNr) render(nachOben); })
      .catch(e => { app.innerHTML = rahmen(leer('Laden fehlgeschlagen', esc(e.message) + '. Bitte die Seite neu laden.')); });
    return;
  }
  const popY = document.querySelector('.w-pop')?.scrollTop;   // Aufklapp-Menü behält beim Ankreuzen seine Scrollposition
  app.innerHTML = ANSICHT[V.screen]();
  if (popY) document.querySelector('.w-pop')?.scrollTo(0, popY);
  montiere();
  if (V.screen === 'dash') feedAuto();
  dringendPruefen();
  if (V.screen === 'lern' && F[V.fid] && F[V.fid].englisch) document.documentElement.dataset.lang = V.lang; else delete document.documentElement.dataset.lang;   // Sprache auch für aufgeklappte Schaubilder (außerhalb .inhalt)
  if (V.screen === 'lern') { if (window.LT_nachRender) { window.LANG = () => (F[V.fid] && F[V.fid].englisch ? V.lang : 'de'); window.LT_nachRender(V.fid); } nachLernRender(); }
  if (nachOben) window.scrollTo(0, 0);
}
if (S.einst.theme && S.einst.theme !== 'system') document.documentElement.setAttribute('data-theme', S.einst.theme);
ausAdresse(location.hash);
render();

/* ---------- Feed „Neu in Lernweh“ (inhalte/neuigkeiten.json): kleine Kachel oben rechts auf der Startseite.
   Klappt kurz auf (neuester Eintrag), wenn es etwas Ungelesenes gibt oder die Sitzung gerade beginnt; danach wieder zu. Alles im Overlay. ---------- */
function feedUngelesen() { return (D.neu || []).filter(e => e.id > (S.einst.neuGelesen || '')).length; }
function feedArt(a) { return ({ neu: 'Neu', besser: 'Verbessert', behoben: 'Behoben', wichtig: 'Wichtig' })[a] || 'Neu'; }
function feedHTML() {
  const l = D.neu || []; if (!l.length) return '';
  const n = feedUngelesen(), e = l[0];
  return `<div class="lw-neu${n ? ' ungelesen' : ''}"><button class="lw-neu-k" data-act="feed-auf" aria-expanded="false" aria-label="Neuigkeiten">${n ? '<i></i>' : ''}Neu</button>
    <div class="lw-neu-pop" role="status"><div class="lw-neu-kopf"><span class="feed-art feed-${esc(e.art || 'neu')}">${feedArt(e.art)}</span><small>${datumKurz(e.datum)}</small></div>
      <b>${esc(e.titel)}</b><p>${e.text}</p><button class="lw-neu-alle" data-act="feed">Alle Neuigkeiten${l.length > 1 ? ` (${l.length})` : ''} ${IC.pfeil}</button></div></div>`;
}
/* auf-/zuklappen; beim Aufklappen gilt der neueste Eintrag als gelesen */
function feedKlappe(auf, auto) {
  const w = document.querySelector('.lw-neu'); if (!w) return;
  clearTimeout(feedKlappe.t); w.classList.toggle('auf', auf); w.querySelector('.lw-neu-k').setAttribute('aria-expanded', auf);
  if (!auf) return;
  const l = D.neu || []; if (l.length && l[0].id > (S.einst.neuGelesen || '')) { S.einst.neuGelesen = l[0].id; save(); }
  if (auto) feedKlappe.t = setTimeout(() => { if (!w.matches(':hover') && !w.contains(document.activeElement)) feedKlappe(false); }, 6000);
}
/* Pflicht-Hinweis (Neuigkeit mit dringend + nz): Wer eins der überarbeiteten Unterthemen schon kannte, bekommt einmal ein Fenster mit genau
   diesen Unterthemen; erst „Verstanden“ schließt es dauerhaft (S.einst.dringend). Wer sie noch nicht kannte, sieht nur den normalen Eintrag. */
function dringendPruefen() {
  if (document.getElementById('ov') || navigator.webdriver) return;
  const ok = S.einst.dringend || {};
  const e = (D.neu || []).find(n => n.dringend && n.themen && !ok[n.id]); if (!e) return;
  const meine = e.themen.filter(k => TOP[k] && k in S.kannte && !S.kannte[k].includes(e.nz)); if (!meine.length) return;
  const nachFach = {}; for (const k of meine) (nachFach[TOP[k].f.id] = nachFach[TOP[k].f.id] || []).push(TOP[k]);
  document.body.insertAdjacentHTML('beforeend', `<div id="ov" class="ov ov-feed ov-dringend" role="dialog" aria-modal="true" aria-label="${esc(e.titel)}"><div class="ov-box">
    <div class="ov-kopf"><b>${esc(e.titel)}</b><span>${datumKurz(e.datum)}</span></div>
    <p>${e.text}</p><p><b>Betroffen sind diese Unterthemen, die du schon bearbeitet hast:</b></p>
    ${Object.values(nachFach).map(l => `<h4>${esc(l[0].f.name)}</h4><ul class="dr-liste">${l.map(x => `<li><button class="dr-lk" ${goLern(x.f.id, x.k.id, x.t.id)}>${esc(x.t.title)}</button></li>`).join('')}</ul>`).join('')}
    <p class="dr-fuss"><button class="btn btn-main" data-dr-ok>Verstanden</button></p></div></div>`);
  const ov = document.getElementById('ov'), fertig = () => { S.einst.dringend = { ...(S.einst.dringend || {}), [e.id]: 1 }; save(); ov.remove(); };
  ov.querySelector('[data-dr-ok]').onclick = fertig;
  ov.querySelectorAll('.dr-lk').forEach(b => b.addEventListener('click', () => { S.einst.dringend = { ...(S.einst.dringend || {}), [e.id]: 1 }; save(); ov.remove(); }));
}
function feedAuto() {
  const w = document.querySelector('.lw-neu'); if (!w || navigator.webdriver) return;
  let neuSitzung = false; try { neuSitzung = !sessionStorage.getItem('lw-neu-s'); sessionStorage.setItem('lw-neu-s', '1'); } catch (e) { }
  if (feedUngelesen() || neuSitzung) setTimeout(() => feedKlappe(true, true), 500);
}
document.addEventListener('pointerdown', e => { const w = document.querySelector('.lw-neu.auf'); if (w && !w.contains(e.target)) feedKlappe(false); });
function feedOverlay() {
  const l = D.neu || [], gel = S.einst.neuGelesen || '';
  document.getElementById('ov')?.remove();
  document.body.insertAdjacentHTML('beforeend', `<div id="ov" class="ov ov-feed" role="dialog" aria-modal="true" aria-label="Neu in Lernweh"><div class="ov-box">
    <div class="ov-kopf"><b>Neu in Lernweh</b><span>Was sich zuletzt geändert hat</span><button class="btn" data-act="ov-zu">Schließen</button></div>
    <ol class="feed-liste">${l.map(e => `<li class="${e.id > gel ? 'ungelesen' : ''}"><div class="feed-kopf"><span class="feed-art feed-${esc(e.art || 'neu')}">${feedArt(e.art)}</span><small>${datumKurz(e.datum)}</small></div>
      <b>${esc(e.titel)}</b><p>${e.text}</p></li>`).join('')}</ol></div></div>`);
  const ov = document.getElementById('ov'); ov.onclick = ev => { if (ev.target === ov) ov.remove(); };
  if (l.length && l[0].id > gel) { S.einst.neuGelesen = l[0].id; save(); }
}
