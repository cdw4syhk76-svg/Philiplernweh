/* LernWeh · Originalfolien: alle Unterlagen eines Fachs, wie sie im PDF stehen, Seite für Seite.
   Neben jeder Seite steht, auf welcher Lernseite der Stoff ist (Stand: steht dort · teilweise · kaum · ohne Lernstoff),
   bei Übungsblättern zusätzlich, ob die Aufgabe als Aufgabe in LernWeh eingebaut ist (antippen öffnet sie).
   Daten: dist/folien/<fach>.js (aus werkzeuge/originalfolien.py), PDFs dist/folien/<fach>/<deck>.pdf, Anzeige mit pdf.js (dist/pdfjs/).
   Adresse: #folien--<fach>--<deck>--<seite>. Einstiege: Knopf oben rechts, Einstellungen, „Quelle“ auf jeder Lernseite. */
'use strict';

const FO = { daten: {}, warte: {}, laden: {}, pdf: {}, bild: new Map(), schlange: [], laeuft: 0, beob: null };
const FO_STAND = {
  voll: ['Steht auf der Lernseite', 'Der Inhalt dieser Seite ist auf der genannten Lernseite erklärt.'],
  teil: ['Großteils auf der Lernseite', 'Das Wesentliche steht dort, einzelne Stichworte oder Beispiele vielleicht nicht. Kurz selbst vergleichen.'],
  offen: ['Kaum auf einer Lernseite', 'Diese Seite findet sich kaum in LernWeh wieder. Bitte selbst prüfen und gern melden.'],
  titel: ['Gliederung oder Organisatorisches', 'Titel-, Gliederungs- und Agenda-Folien, Literatur, Organisatorisches: kein eigener Lernstoff, darum nicht verglichen.'],
  weg: ['Bewusst weggelassen', 'In der Vorlesung gestrichen oder nicht prüfungsrelevant.'],
};
const FO_AUFG = { drin: 'Als Aufgabe in LernWeh', aehnlich: 'Ähnliche Aufgabe in LernWeh', keine: 'Nicht als eigene Aufgabe' };
const foV = () => (window.LT_V || {});
const foUrl = p => p + (foV()[p.replace(/\.js$/, '')] || foV()[p] ? '?v=' + (foV()[p.replace(/\.js$/, '')] || foV()[p]) : '');
const foFaecher = () => D.faecher.filter(f => f.folien);

/* ---------- Laden ---------- */
window.LT_folienGeladen = (fid, d) => { FO.daten[fid] = d; const w = FO.warte[fid]; delete FO.warte[fid]; if (w) w(); };
/* Eine Ladung je Fach; schlägt sie fehl (Netz, abgelaufene Anmeldung, Datei fehlt), wird sie verworfen, damit „Erneut versuchen“ wirklich neu lädt.
   Kommt statt der Daten etwas anderes (z. B. eine HTML-Seite), meldet onload das, statt ewig „Lade …“ zu zeigen. */
function foLade(fid) {
  if (FO.daten[fid]) return Promise.resolve(FO.daten[fid]);
  if (FO.laden[fid]) return FO.laden[fid];
  const s = document.createElement('script');
  let uhr = 0;
  return FO.laden[fid] = new Promise((ok, nein) => {
    FO.warte[fid] = () => ok(FO.daten[fid]);
    s.onerror = () => nein(new Error('Die Datei mit den Unterlagen konnte nicht geladen werden.'));
    s.onload = () => setTimeout(() => { if (!FO.daten[fid]) nein(new Error('Die Unterlagen kamen nicht an. Bitte neu anmelden oder die Seite neu laden.')); }, 50);
    uhr = setTimeout(() => nein(new Error('Das Laden dauert zu lange. Bitte die Internetverbindung prüfen.')), 30000);
    s.src = foUrl('folien/' + fid + '.js'); document.head.appendChild(s);
  }).then(d => { clearTimeout(uhr); delete FO.laden[fid]; return d; },
          e => { clearTimeout(uhr); delete FO.laden[fid]; delete FO.warte[fid]; s.remove(); throw e; });
}
let foPdfjs = null;
function foPdfjsLade() {
  if (foPdfjs) return foPdfjs;
  foPdfjs = new Promise((ok, nein) => {
    if (window.pdfjsLib) return ok(window.pdfjsLib);
    const s = document.createElement('script'); s.src = foUrl('pdfjs/pdf.min.js');
    s.onload = () => { try { pdfjsLib.GlobalWorkerOptions.workerSrc = foUrl('pdfjs/pdf.worker.min.js'); ok(pdfjsLib); } catch (e) { nein(e); } };
    s.onerror = () => { foPdfjs = null; nein(new Error('PDF-Anzeige konnte nicht geladen werden')); }; document.head.appendChild(s);
  });
  return foPdfjs;
}
function foDok(fid, deck) {
  const k = fid + '/' + deck.id;
  if (!FO.pdf[k]) FO.pdf[k] = foPdfjsLade().then(lib => lib.getDocument({ url: deck.datei, disableAutoFetch: true, isEvalSupported: false }).promise).catch(e => { delete FO.pdf[k]; throw e; });
  return FO.pdf[k];
}

/* ---------- Zustand und Adresse ---------- */
function foZustand() {
  if (!V.fo) V.fo = { fid: (S.einst.foFach && F[S.einst.foFach] && F[S.einst.foFach].folien) ? S.einst.foFach : (foFaecher()[0] || D.faecher[0]).id, deck: '', seite: 0, filter: 'alle', suche: '', thema: '' };
  return V.fo;
}
/* Wo steht ein Unterthema in den Unterlagen? [{deck, seiten:[n…]}] */
function foStellen(fid, tid) {
  const d = FO.daten[fid]; if (!d) return [];
  return d.decks.map(k => ({ deck: k, seiten: d.seiten[k.id].filter(s => s.t.includes(tid) || (s.a || []).some(a => a.t.includes(tid))).map(s => s.n) })).filter(x => x.seiten.length);
}
const foBereich = l => { const out = []; let a = null, b = null; for (const n of l) { if (b !== null && n === b + 1) b = n; else { if (a !== null) out.push(a === b ? a : a + '–' + b); a = b = n; } } if (a !== null) out.push(a === b ? a : a + '–' + b); return out.join(', '); };

/* Öffnen von außen: foOeffnen(fid, {tid}) springt zur ersten Seite des Unterthemas, sonst zur gemerkten Stelle */
function foOeffnen(fid, opt = {}) {
  const z = foZustand();
  if (fid && F[fid] && F[fid].folien) { if (z.fid !== fid) Object.assign(z, { fid, deck: '', seite: 0 }); }
  z.thema = opt.tid || ''; z.filter = 'alle'; z.suche = '';
  if (V.screen !== 'folien') try { history.pushState(null, '', '#folien'); } catch (e) { }   // „Zurück“ führt wieder zur Lernseite
  V.screen = 'folien';
  if (opt.tid) foLade(z.fid).then(() => { const st = foStellen(z.fid, opt.tid); if (st.length) { z.deck = st[0].deck.id; z.seite = st[0].seiten[0]; } render(true); }).catch(() => render(true));
  else render(true);
}

/* ---------- Ansicht ---------- */
function folienAnsicht() {
  const z = foZustand(), f = F[z.fid];
  return rahmen(`<div class="fo" style="--fach:${f ? f.farbe : 'var(--x-acc)'}">
    <header class="b7-top fo-top"><h1>Originalfolien</h1><div class="b7-stats"><span>Alle Unterlagen, wie sie im PDF stehen · daneben, wo der Stoff in LernWeh steht</span></div></header>
    <nav class="fo-faecher" aria-label="Fach wählen">${foFaecher().map(x => `<button class="${x.id === z.fid ? 'on' : ''}" style="--fach:${x.farbe}" data-fo-fach="${x.id}" aria-pressed="${x.id === z.fid}"><i></i><b>${esc(x.name)}</b><small>${x.folien.u} ${x.folien.u === 1 ? 'Unterlage' : 'Unterlagen'} · ${x.folien.s} Seiten</small></button>`).join('')}</nav>
    <div data-mount="folien"><div class="laden" role="status">Lade die Unterlagen …</div></div></div>`);
}
function foMontiere(el) {
  const z = foZustand();
  foLade(z.fid).then(d => { if (!el.isConnected) return; foZeichne(el, d); }).catch(e => { if (!el.isConnected) return;
    el.innerHTML = leer('Unterlagen konnten nicht geladen werden', esc(e.message)) + '<p class="fo-nochmal"><button class="btn" type="button">Erneut versuchen</button></p>';
    el.querySelector('.fo-nochmal button').addEventListener('click', () => { el.innerHTML = '<div class="laden" role="status">Lade die Unterlagen …</div>'; foMontiere(el); }); });
}
function foZaehle(d, deck) {
  const c = { voll: 0, teil: 0, offen: 0, titel: 0, weg: 0, drin: 0, aehnlich: 0, keine: 0 };
  c.pr = 0;
  for (const s of d.seiten[deck.id]) { c[s.z]++; if (s.z === 'offen' || (s.f || []).some(x => (x[2] || 'fehlt') === 'fehlt')) c.pr++; for (const a of s.a || []) if (!a.f) c[a.a.some(x => x.st === 'drin') ? 'drin' : a.a.length ? 'aehnlich' : 'keine']++; }
  return c;
}
function foZeichne(el, d) {
  const z = foZustand(), f = F[z.fid];
  if (!d.decks.some(k => k.id === z.deck)) { z.deck = d.decks[0].id; z.seite = 0; }
  const deck = d.decks.find(k => k.id === z.deck), gruppen = [...new Set(d.decks.map(k => k.gruppe))];
  const pruefen = s => s.z === 'offen' || (s.f || []).some(x => (x[2] || 'fehlt') === 'fehlt') || (s.a || []).some(a => !a.f && !a.a.some(x => x.st === 'drin'));
  const thema = z.thema && TOP[z.fid + '/' + z.thema] ? TOP[z.fid + '/' + z.thema] : null;
  let seiten = d.seiten[deck.id];
  if (z.filter === 'pruefen') seiten = seiten.filter(pruefen);
  if (z.filter === 'aufg') seiten = seiten.filter(s => (s.a || []).some(a => !a.f));
  const c = foZaehle(d, deck), uebung = deck.art === 'uebung';
  const stellen = thema ? foStellen(z.fid, z.thema) : [];
  const i = d.decks.indexOf(deck), naechstes = d.decks[i + 1];
  el.innerHTML = `<div class="fo-wrap">
    <aside class="fo-seitel" aria-label="Unterlagen">
      <label class="fo-suche">${IC.suche}<input type="search" placeholder="In allen Unterlagen suchen" value="${esc(z.suche)}" data-fo-suche aria-label="In den Unterlagen von ${esc(f.name)} suchen"></label>
      <div class="fo-treffer" data-fo-treffer hidden></div>
      <select class="fo-deckwahl" data-fo-deckwahl aria-label="Unterlage wählen">${gruppen.map(g => `<optgroup label="${esc(g)}">${d.decks.filter(k => k.gruppe === g).map(k => `<option value="${k.id}" ${k === deck ? 'selected' : ''}>${esc(k.titel)} (${k.n} S.)</option>`).join('')}</optgroup>`).join('')}</select>
      <div class="fo-decks">${gruppen.map(g => `<h3>${esc(g)}</h3>${d.decks.filter(k => k.gruppe === g).map(k => { const cc = foZaehle(d, k), offen = cc.pr + (k.art === 'uebung' ? cc.keine : 0);
        return `<button class="fo-deck ${k === deck ? 'on' : ''}" data-fo-deck="${k.id}" aria-pressed="${k === deck}"><b>${esc(k.titel)}</b><small>${k.n} Seiten${offen ? ` · <em>${offen} zum Prüfen</em>` : ''}</small></button>`; }).join('')}`).join('')}</div>
      <div class="fo-legende"><h3>So liest du die Zuordnung</h3>${['voll', 'teil', 'offen', 'titel'].map(k => `<p><span class="fo-pk fo-${k}"></span><span><b>${FO_STAND[k][0]}</b>${FO_STAND[k][1]}</span></p>`).join('')}
        <p class="fo-hw">Die Zuordnung entsteht automatisch aus dem Text der Seiten und den Quellenangaben der Lernseiten. Fehlt etwas oder stimmt eine Zuordnung nicht: „⚑ Melden“ an der Seite.</p></div>
    </aside>
    <section class="fo-haupt">
      ${thema ? `<div class="fo-thema" role="note"><span><small>Folien zum Unterthema</small><b>${esc(thema.t.title)}</b>${stellen.length ? `<span class="fo-thema-st">${stellen.map(s => `<button data-fo-spring="${s.deck.id}|${s.seiten[0]}">${esc(s.deck.titel)} · S. ${foBereich(s.seiten)}</button>`).join('')}</span>` : '<em>Keine Seite eindeutig zugeordnet.</em>'}</span>
        <button class="btn" ${goLern(z.fid, thema.k.id, thema.t.id)}>Zur Lernseite</button><button class="fo-x" data-fo-thema-weg aria-label="Hinweis schließen">✕</button></div>` : ''}
      <header class="fo-dkopf"><div><small>${esc(deck.gruppe)} · ${esc(f.name)}</small><h2>${esc(deck.titel)}</h2>
        <p>${deck.n} Seiten${c.voll + c.teil ? ` · ${c.voll + c.teil} mit Stoff auf einer Lernseite` : ''}${c.offen ? ` · <em>${c.offen} kaum zu finden</em>` : ''}${uebung ? ` · Aufgaben: ${c.drin} eingebaut${c.aehnlich ? `, ${c.aehnlich} ähnlich` : ''}${c.keine ? `, ${c.keine} nicht als eigene Aufgabe` : ''}` : ''}</p></div>
        <a class="btn fo-pdf" href="${esc(deck.datei)}" target="_blank" rel="noopener" download>PDF ↓</a></header>
      <div class="fo-hinweis" role="note"><b>„Fehlt vielleicht auf der Lernseite“</b> neben einer Folie ist ein automatischer Wortvergleich mit allen Lernseiten, kein sicherer Befund:
        <ul><li>Ist etwas <b>mit anderen Worten erklärt</b> (z. B. „Hierarchie der Bedürfnisse“ statt „Bedürfnishierarchie“), steht es trotzdem dort.</li>
          <li><b>Namen, Firmen, Beispiele und Quellen</b> der Folie müssen nicht auf der Lernseite stehen.</li>
          <li>Was nur im <b>Bild oder Schaubild</b> steht, wird nicht erkannt.</li></ul>
        Kurz auf der Lernseite nachsehen. Fehlt dort wirklich etwas Inhaltliches: „⚑ Zuordnung falsch oder Stoff fehlt“.${foAdmin() ? '<p class="fo-adm-hw"><b>Admin:</b> Kästchen ankreuzen = „auf der Lernseite ergänzen“. Das geht als Meldung mit Vorrang an Claude.</p>' : ''}</div>
      <div class="seg fo-filter" role="group" aria-label="Seiten filtern">${[['alle', 'Alle Seiten'], ['pruefen', 'Nur zum Prüfen'], ...(uebung ? [['aufg', 'Nur Aufgaben']] : [])].map(([v, n]) => `<button class="${z.filter === v ? 'on' : ''}" data-fo-filter="${v}" aria-pressed="${z.filter === v}">${n}</button>`).join('')}</div>
      <ol class="fo-liste ${deck.art === 'skript' || uebung || deck.art === 'formeln' ? 'fo-hoch' : ''}">${seiten.map(s => foSeiteHTML(z.fid, deck, s, thema)).join('') || `<li class="fo-leer">${leer('Nichts zu prüfen', 'Alle Seiten dieser Unterlage sind einer Lernseite zugeordnet.')}</li>`}</ol>
      ${naechstes ? `<button class="tile fo-weiter" data-fo-deck="${naechstes.id}"><small>Weiter mit</small><b>${esc(naechstes.titel)}</b>${IC.pfeil}</button>` : ''}
    </section></div>`;
  foVerdrahte(el, d, deck);
}
function foThemaLink(fid, tid, haupt) {
  const x = TOP[fid + '/' + tid]; if (!x) return '';
  return `<li><button class="fo-lk${haupt ? '' : ' fo-lk2'}" ${goLern(fid, x.k.id, tid)}><small>Oberthema ${x.f.kapitel.indexOf(x.k) + 1} · ${esc(x.k.title)}</small><b>${esc(x.t.title)}</b>${IC.pfeil}</button></li>`;
}
function foSeiteHTML(fid, deck, s, thema) {
  s._k = `${fid}/${deck.id}/${s.n}`;
  const st = FO_STAND[s.z] || FO_STAND.teil, an = thema && (s.t.includes(thema.t.id) || (s.a || []).some(a => a.t.includes(thema.t.id)));
  const aufg = (s.a || []).map(a => {
    const best = a.a.find(x => x.st === 'drin') || a.a[0], art = best ? best.st : 'keine';
    return `<li class="fo-a fo-a-${art}${a.f ? ' fo-a-forts' : ''}"><div class="fo-a-kopf"><span class="fo-a-l">${a.f ? (a.l ? 'Fortsetzung · ' + esc(a.l) : 'Fortsetzung') : esc(a.l || 'Aufgabe')}</span><span class="fo-a-st">${art === 'drin' ? '✓ ' : art === 'aehnlich' ? '≈ ' : '– '}${FO_AUFG[art]}</span></div>
      ${a.a.length ? `<div class="fo-a-knoepfe">${a.a.slice(0, 2).map(x => `<button class="fo-a-auf" data-fo-aufgabe="${esc(x.id)}" title="Diese Aufgabe in LernWeh öffnen"><b>${esc(x.titel)}</b><small>${x.id.startsWith('k:') ? 'aus dem Probeklausur-Bogen' : x.id.startsWith('l:') ? 'durchgerechnet auf der Lernseite' : 'Aufgabe im Arbeitsblatt'} · öffnen</small></button>`).join('')}</div>` : ''}
      ${a.t.length ? `<p class="fo-a-stoff">Stoff dazu: ${a.t.map(t => { const x = TOP[fid + '/' + t]; return x ? `<button class="fo-a-lk" ${goLern(fid, x.k.id, t)}>${esc(x.t.title)}</button>` : ''; }).join(' · ')}</p>` : ''}</li>`;
  }).join('');
  return `<li class="fo-s${an ? ' fo-an' : ''}" id="fo-${deck.id}-${s.n}" data-n="${s.n}">
    <div class="fo-bild" data-fo-bild="${deck.id}|${s.n}"><span class="fo-nr">Seite ${s.n}</span><div class="fo-ph" aria-hidden="true"></div></div>
    <div class="fo-info">
      ${s.nk ? `<p class="fo-nk" title="${esc(s.nk)}">Nicht klausurrelevant <small>${esc(s.nk)}</small></p>` : ''}
      <p class="fo-st fo-${s.z}" title="${esc(st[1])}"><span class="fo-pk fo-${s.z}"></span>${st[0]}</p>
      ${s.t.length ? `<ul class="fo-lks">${s.t.map((t, i) => foThemaLink(fid, t, i === 0)).join('')}</ul>` : s.z === 'offen' ? '<p class="fo-dim">Keiner Lernseite eindeutig zugeordnet.</p>' : ''}
      ${foFehltHTML(s)}
      ${aufg ? `<div class="fo-aufg"><h4>Aufgaben auf dieser Seite</h4><ul>${aufg}</ul></div>` : ''}
      ${foAdmin() && ['voll', 'teil', 'offen'].includes(s.z) ? `<label class="fo-mk fo-mk-seite${foMarkiert(s._k + '/seite') ? ' an' : ''}"><input type="checkbox" data-fo-mark="${esc(s._k + '/seite')}" ${foMarkiert(s._k + '/seite') ? 'checked' : ''}><span><b>Admin:</b> Inhalt dieser Seite auf der Lernseite ergänzen${foMarkiert(s._k + '/seite') ? '<em>vermerkt · wird ergänzt</em>' : ''}</span></label>` : ''}
      <button class="melde fo-melde" data-melde="Originalfolien · ${esc(F[fid].name)} · ${esc(deck.titel)} · Seite ${s.n}">⚑ Zuordnung falsch oder Stoff fehlt</button>
    </div></li>`;
}

/* Was auf der Lernseite fehlt: Aussagen der Seite mit Fachbegriffen, die nirgends in LernWeh vorkommen (Begriffe fett) */
function foFehltHTML(s) {
  if (!['voll', 'teil', 'offen'].includes(s.z)) return '';
  if (!s.f) return s.z === 'offen' ? '' : '<p class="fo-fehlt-nix">✓ Kein Fachbegriff dieser Seite fehlt.</p>';
  const fett = (t, ws) => ws.reduce((h, w) => h.replace(new RegExp('(^|[^\\wÄÖÜäöüß])(' + w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')(?=$|[^\\wÄÖÜäöüß])', 'g'), '$1<b>$2</b>'), esc(t));
  /* Stand je Stichpunkt (werkzeuge/originalfolien_ergaenzungen.py): nichts wird still entfernt, jeder Punkt sagt, was mit ihm ist */
  const STAND = { fehlt: ['fehlt', ''], erg: ['ergänzt', 'steht jetzt im Text der Lernseite'], anders: ['mit anderen Worten erklärt', 'steht auf der Lernseite, nur anders formuliert'], kein: ['kein Lernstoff', 'Literatur, Weblink, Lebenslauf oder Bildquelle'] };
  const offen = s.f.filter(x => (x[2] || 'fehlt') === 'fehlt');
  const punkt = ([t, ws, st = 'fehlt']) => {
    const k = s._k + '/' + foHash(t), m = foMarkiert(k), lab = st === 'fehlt' ? '' : `<em class="fo-fs fo-fs-${st}" title="${esc(STAND[st][1])}">✓ ${STAND[st][0]}</em>`;
    const txt = st === 'fehlt' ? fett(t, ws) : esc(t);
    return foAdmin() && st === 'fehlt' ? `<li><label class="fo-mk${m ? ' an' : ''}"><input type="checkbox" data-fo-mark="${esc(k)}" ${m ? 'checked' : ''}><span>${txt}${m ? '<em>vermerkt · wird ergänzt</em>' : ''}</span></label></li>`
      : `<li class="fo-f-${st}"><span>${txt}</span>${lab}</li>`;
  };
  return `<div class="fo-fehlt${offen.length ? '' : ' fo-fehlt-ok'}"><h4>${offen.length ? 'Fehlt vielleicht auf der Lernseite' : 'Abgleich mit der Lernseite: alles geprüft'}</h4>
    <ul class="fo-fehlt-l${foAdmin() ? ' fo-adm' : ''}">${[...offen, ...s.f.filter(x => (x[2] || 'fehlt') !== 'fehlt')].map(punkt).join('')}</ul></div>`;
}

/* ---------- Admins: Fehlstellen ankreuzen → Meldung mit Vorrang (prio 1) im Lernstand, die Claude mit /meldungen-pruefen zuerst bearbeitet.
   Schlüssel <fach>/<deck>/<seite>/<nr|seite>; S.foMark merkt, was angekreuzt ist (Abwählen nimmt die Meldung wieder heraus). ---------- */
const foHash = t => [...t].reduce((h, c) => (h * 31 + c.charCodeAt(0)) | 0, 7).toString(36).replace('-', 'm');   // Stichpunkt bleibt erkennbar, auch wenn andere wegfallen
const foAdmin = () => typeof LW_ADMIN !== 'undefined' && LW_ADMIN;
const foMarkiert = k => !!(S.foMark && S.foMark[k]);
function foMarkSetzen(k, an) {
  const [fid, dk, n, nr] = k.split('/'), d = FO.daten[fid], deck = d && d.decks.find(x => x.id === dk), seite = d && d.seiten[dk].find(x => x.n === +n);
  if (!deck || !seite) return;
  S.foMark = S.foMark || {}; S.meldungen = S.meldungen || [];
  S.meldungen = S.meldungen.filter(m => m.ziel !== 'originalfolie:' + k);
  if (an) {
    const punkt = nr === 'seite' ? null : (seite.f || []).find(p => foHash(p[0]) === nr);
    const themen = seite.t.map(t => TOP[fid + '/' + t]).filter(Boolean).map(x => x.t.title).join(', ');
    S.meldungen.push({ d: new Date().toISOString(), ort: `Admin · Originalfolien · ${F[fid].name} · ${deck.titel} · Seite ${n}${themen ? ' → Lernseite ' + themen : ''}`,
      sel: punkt ? punkt[0].slice(0, 300) : seite.x.slice(0, 300), text: punkt ? `Auf der Lernseite ergänzen (fehlende Begriffe: ${punkt[1].join(', ')})` : 'Inhalt dieser Folie auf der Lernseite ergänzen',
      prio: 1, ziel: 'originalfolie:' + k });
    S.foMark[k] = new Date().toISOString().slice(0, 10);
  } else delete S.foMark[k];
  save();
}
document.addEventListener('change', e => {
  const c = e.target.closest('[data-fo-mark]'); if (!c || !foAdmin()) return;
  foMarkSetzen(c.dataset.foMark, c.checked);
  const l = c.closest('.fo-mk'); l.classList.toggle('an', c.checked);
  l.querySelector('em')?.remove(); if (c.checked) l.querySelector('span').insertAdjacentHTML('beforeend', '<em>vermerkt · wird ergänzt</em>');
  if (typeof hinweis === 'function') hinweis(c.checked ? 'Vermerkt: geht als Meldung mit Vorrang an Claude.' : 'Vermerk entfernt.');
});

/* ---------- Bilder der Seiten: erst wenn sie in die Nähe kommen, eins nach dem anderen, als JPEG (wenig Speicher) ---------- */
function foBildRendern(fid, deck, box) {
  const n = +box.dataset.foBild.split('|')[1], key = `${fid}/${deck.id}/${n}`;
  if (box.dataset.fertig) return;
  box.dataset.fertig = '1';
  const zeige = url => { const img = new Image(); img.alt = `${deck.titel}, Seite ${n}`; img.decoding = 'async'; img.src = url; img.onload = () => { box.querySelector('.fo-ph')?.remove(); box.classList.add('da'); }; box.appendChild(img); img.onclick = () => foGross(fid, deck, n); };
  if (FO.bild.has(key)) return zeige(FO.bild.get(key));
  if (deck.bilder && !FO.ohneBild) {   // vorab gerendertes Bild (schnell); fehlt es, aus dem PDF zeichnen
    const img = new Image(); img.alt = `${deck.titel}, Seite ${n}`; img.decoding = 'async';
    img.onload = () => { box.querySelector('.fo-ph')?.remove(); box.classList.add('da'); };
    img.onerror = () => { img.remove(); FO.ohneBild = true; box.dataset.fertig = ''; foBildRendern(fid, deck, box); };
    img.onclick = () => foGross(fid, deck, n); img.src = deck.bilder + n + '.webp'; box.appendChild(img);
    return;
  }
  FO.schlange.push(async () => {
    try {
      const doc = await foDok(fid, deck), page = await doc.getPage(n);
      const breite = Math.min(1400, Math.max(600, box.clientWidth * Math.min(2, window.devicePixelRatio || 1)));
      /* Quer gedruckte Folien auf Hochformat-Seiten: Textrichtung messen und aufrecht drehen */
      let rot = page.rotate || 0;
      try { const tc = await page.getTextContent(); let senk = 0, waag = 0;
        for (const it of tc.items) { const [a, bb] = it.transform, l = (it.str || '').trim().length; if (Math.abs(bb) > Math.abs(a)) senk += l * Math.sign(bb); else waag += l; }
        if (Math.abs(senk) > waag) rot = (rot + (senk > 0 ? 90 : 270)) % 360; } catch (e) { }
      const vp0 = page.getViewport({ scale: 1, rotation: rot }), vp = page.getViewport({ scale: breite / vp0.width, rotation: rot });
      const cv = document.createElement('canvas'); cv.width = Math.round(vp.width); cv.height = Math.round(vp.height);
      const ctx = cv.getContext('2d'); ctx.fillStyle = '#fff'; ctx.fillRect(0, 0, cv.width, cv.height);
      await page.render({ canvasContext: ctx, viewport: vp }).promise;
      const url = await new Promise(ok => cv.toBlob(b => ok(b ? URL.createObjectURL(b) : cv.toDataURL('image/jpeg', .82)), 'image/jpeg', .82));
      cv.width = cv.height = 0; page.cleanup();
      FO.bild.set(key, url); if (box.isConnected) zeige(url);
    } catch (e) { box.dataset.fertig = ''; box.classList.add('fehler'); box.querySelector('.fo-ph')?.replaceWith(Object.assign(document.createElement('p'), { className: 'fo-fehler', textContent: 'Seite konnte nicht angezeigt werden. „PDF ↓“ öffnet die Datei.' })); }
  });
  foWeiter();
}
function foWeiter() {
  while (FO.laeuft < 2 && FO.schlange.length) { FO.laeuft++; FO.schlange.shift()().finally(() => { FO.laeuft--; foWeiter(); }); }
}
function foGross(fid, deck, n) {
  document.getElementById('ov')?.remove();
  const url = FO.bild.get(`${fid}/${deck.id}/${n}`) || (deck.bilder && !FO.ohneBild ? deck.bilder + n + '.webp' : ''); if (!url) return;
  document.body.insertAdjacentHTML('beforeend', `<div id="ov" class="ov ov-seite fo-ov" role="dialog" aria-modal="true" aria-label="${esc(deck.titel)}, Seite ${n}"><div class="ov-box">
    <div class="ov-kopf"><b>${esc(deck.titel)}</b><span>Seite ${n} von ${deck.n}</span><button class="btn" data-act="ov-zu">Schließen</button></div><img class="fo-gross" src="${url}" alt="${esc(deck.titel)}, Seite ${n}"></div></div>`);
  const ov = document.getElementById('ov'); ov.onclick = e => { if (e.target === ov) ov.remove(); };
  if (!FO.bild.has(`${fid}/${deck.id}/${n}`)) foScharf(fid, deck, n).then(u => { const im = ov.querySelector('.fo-gross'); if (u && im && ov.isConnected) im.src = u; }).catch(() => { });
}
/* Großansicht: das kleine Vorschaubild sofort zeigen, dann scharf aus dem PDF nachzeichnen (nur diese eine Seite) */
async function foScharf(fid, deck, n) {
  const k = `${fid}/${deck.id}/${n}/gross`; if (FO.bild.has(k)) return FO.bild.get(k);
  const doc = await foDok(fid, deck), page = await doc.getPage(n);
  const img = new Image(); img.src = deck.bilder + n + '.webp'; await img.decode().catch(() => { });
  const quer = img.naturalWidth && img.naturalHeight && (img.naturalWidth > img.naturalHeight) !== (page.getViewport({ scale: 1 }).width > page.getViewport({ scale: 1 }).height);
  if (quer) return null;   // aufrecht gedrehte Seiten: beim Vorschaubild bleiben
  const rot = page.rotate || 0;
  const vp0 = page.getViewport({ scale: 1, rotation: rot }), vp = page.getViewport({ scale: Math.min(1800, window.innerWidth * (window.devicePixelRatio || 1)) / vp0.width, rotation: rot });
  const cv = document.createElement('canvas'); cv.width = Math.round(vp.width); cv.height = Math.round(vp.height);
  const ctx = cv.getContext('2d'); ctx.fillStyle = '#fff'; ctx.fillRect(0, 0, cv.width, cv.height);
  await page.render({ canvasContext: ctx, viewport: vp }).promise;
  const url = await new Promise(ok => cv.toBlob(b => ok(b ? URL.createObjectURL(b) : cv.toDataURL('image/jpeg', .85)), 'image/jpeg', .85));
  cv.width = cv.height = 0; page.cleanup(); FO.bild.set(k, url); return url;
}

/* ---------- Aufgabe aus LernWeh direkt öffnen (eigene Aufgabe oder Teil des Probeklausur-Bogens) ---------- */
function foAufgabe(fid, id) {
  document.getElementById('ov')?.remove();
  if (id.startsWith('l:')) { const x = TOP[fid + '/' + id.slice(2)]; if (x) go(`lern|${fid}|${x.k.id}|${x.t.id}`); return; }   // Beispiel auf der Lernseite
  document.body.insertAdjacentHTML('beforeend', `<div id="ov" class="ov ov-seite" role="dialog" aria-modal="true" aria-label="Aufgabe"><div class="ov-box">
    <div class="ov-kopf"><b>Aufgabe in LernWeh</b><span>${esc(F[fid].name)} · zum Vergleich mit dem Original</span><button class="btn" data-act="ov-zu">Schließen</button></div><div class="ov-body" data-fo-ab><div class="laden">Lade …</div></div></div></div>`);
  const ov = document.getElementById('ov'); ov.onclick = e => { if (e.target === ov) ov.remove(); };
  LT.lade([fid]).then(() => {
    const f = F[fid], body = ov.querySelector('[data-fo-ab]'); let A = null;
    if (id.startsWith('a:')) { const roh = (f.aufgaben || []).find(x => x.id === id.slice(2)); if (roh) A = ausAufgabe(f, roh); }
    else if (id.startsWith('k:') && f.klausur) for (const K of f.klausur.aufgaben) for (const T of K.teile) for (const v of T.varianten) if (v.id === id.slice(2)) A = ausVariante(f, K, T, v);
    if (!A) { body.innerHTML = leer('Aufgabe nicht gefunden', 'Sie wurde vielleicht umbenannt. Bitte melden.'); return; }
    blatt(body, [], { nur: [A], kopf: false });
    if (A.key) { const x = TOP[A.key]; body.insertAdjacentHTML('beforeend', `<p class="fo-ab-fuss">Stoff dazu: <button class="fo-a-lk" ${goLern(fid, x.k.id, x.t.id)}>${esc(x.t.title)}</button></p>`); }
  }).catch(() => { ov.querySelector('[data-fo-ab]').innerHTML = leer('Laden fehlgeschlagen', 'Bitte die Seite neu laden.'); });
}

/* ---------- Bedienung ---------- */
function foSpring(deckId, n) {
  const z = foZustand(); z.seite = n;
  if (z.deck !== deckId || z.filter !== 'alle') { z.deck = deckId; z.filter = 'alle'; render(); return; }
  foZiel();
}
function foZiel() {
  const z = foZustand(), el = z.seite && document.getElementById(`fo-${z.deck}-${z.seite}`);
  if (el) { el.scrollIntoView({ block: 'start' }); el.classList.remove('fo-blink'); void el.offsetWidth; el.classList.add('fo-blink'); }
}
function foVerdrahte(el, d, deck) {
  const z = foZustand(), fid = z.fid;
  FO.beob?.disconnect(); FO.schlange.length = 0;
  FO.beob = 'IntersectionObserver' in window ? new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { foBildRendern(fid, deck, e.target); FO.beob.unobserve(e.target); } }), { rootMargin: '900px 0px' }) : null;
  el.querySelectorAll('[data-fo-bild]').forEach(b => FO.beob ? FO.beob.observe(b) : foBildRendern(fid, deck, b));
  /* Adresse folgt der Seite, die gerade oben steht (zum Teilen und für „Zurück“) */
  const sicht = 'IntersectionObserver' in window ? new IntersectionObserver(es => { for (const e of es) if (e.isIntersecting) { z.seite = +e.target.dataset.n; const a = '#' + adresse(); if (location.hash !== a) history.replaceState(null, '', a); } }, { rootMargin: '-45% 0px -50% 0px' }) : null;
  if (sicht) el.querySelectorAll('.fo-s').forEach(s => sicht.observe(s));
  el.onclick = e => {
    const t = e.target.closest('[data-fo-deck],[data-fo-filter],[data-fo-spring],[data-fo-aufgabe],[data-fo-thema-weg],[data-fo-treffer-n]'); if (!t) return;
    if (t.dataset.foDeck) { z.deck = t.dataset.foDeck; z.seite = 0; z.filter = 'alle'; render(true); }
    else if (t.dataset.foFilter) { z.filter = t.dataset.foFilter; z.seite = 0; render(); el.querySelector('.fo-dkopf')?.scrollIntoView({ block: 'start' }); }
    else if (t.dataset.foSpring) { const [dk, n] = t.dataset.foSpring.split('|'); foSpring(dk, +n); }
    else if (t.dataset.foTrefferN) { const [dk, n] = t.dataset.foTrefferN.split('|'); z.suche = ''; foSpring(dk, +n); }
    else if (t.dataset.foAufgabe) foAufgabe(fid, t.dataset.foAufgabe);
    else if ('foThemaWeg' in t.dataset) { z.thema = ''; t.closest('.fo-thema').remove(); el.querySelectorAll('.fo-an').forEach(x => x.classList.remove('fo-an')); }
  };
  const wahl = el.querySelector('[data-fo-deckwahl]'); if (wahl) wahl.onchange = () => { z.deck = wahl.value; z.seite = 0; z.filter = 'alle'; render(true); };
  const inp = el.querySelector('[data-fo-suche]'), box = el.querySelector('[data-fo-treffer]');
  const suche = () => {
    z.suche = inp.value; const q = foNorm(inp.value).trim();
    if (q.length < 3) { box.hidden = true; box.innerHTML = ''; return; }
    const w = q.split(/\s+/).filter(Boolean), tr = [];
    for (const k of d.decks) for (const s of d.seiten[k.id]) { const x = foNorm(s.x); if (w.every(v => x.includes(v))) tr.push({ k, s, i: x.indexOf(w[0]) }); }
    box.hidden = false;
    box.innerHTML = tr.length ? `<small>${tr.length} ${tr.length === 1 ? 'Seite' : 'Seiten'}</small>` + tr.slice(0, 40).map(({ k, s, i }) => `<button data-fo-treffer-n="${k.id}|${s.n}"><b>${esc(k.titel)} · S. ${s.n}</b><span>${esc(s.x.slice(Math.max(0, i - 40), i + 90))}</span></button>`).join('') : '<small>Nichts gefunden.</small>';
  };
  if (inp) { inp.oninput = suche; if (z.suche) suche(); }
  if (z.seite) requestAnimationFrame(foZiel);
}
function foNorm(s) { return String(s || "").toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/ß/g, "ss"); }
document.addEventListener('click', e => {
  const b = e.target.closest('[data-fo-fach]'); if (!b) return;
  const z = foZustand(); z.fid = b.dataset.foFach; z.deck = ''; z.seite = 0; z.thema = ''; z.filter = 'alle'; z.suche = ''; S.einst.foFach = z.fid; save(); render(true);
});

/* ---------- Einstiege ---------- */
/* Knopf oben rechts (unter „?“ und Lerntipps): auf einer Lernseite direkt zu deren Folien */
(function knopf() {
  if (!document.body) return document.addEventListener('DOMContentLoaded', knopf);
  if (!foFaecher().length || document.querySelector('.lw-folien-knopf')) return;
  const k = document.createElement('button'); k.className = 'lw-folien-knopf'; k.title = 'Originalfolien: alle Unterlagen, wie sie im PDF stehen'; k.setAttribute('aria-label', 'Originalfolien');
  k.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="14" height="10" rx="1.5"/><path d="M7 18h10a2 2 0 0 0 2-2V8M10 21h10a2 2 0 0 0 2-2v-8"/></svg>';
  k.onclick = () => { if (V.screen === 'folien') return; if (V.screen === 'lern' && F[V.fid] && F[V.fid].folien) foOeffnen(V.fid, { tid: V.tid }); else foOeffnen(V.screen === 'sb' && V.sb.f.length === 1 ? V.sb.f[0] : null); };
  document.body.appendChild(k);
  const zeig = () => k.classList.toggle('on', V.screen === 'folien'); addEventListener('hashchange', zeig); zeig();
})();
/* „Quelle: …“ auf der Lernseite wird zum Sprung in die Originalfolien */
document.addEventListener('click', e => {
  const b = e.target.closest('[data-fo-quelle]'); if (!b) return;
  const [fid, tid] = b.dataset.foQuelle.split('|'); foOeffnen(fid, { tid });
});
function foQuelleHTML(x) {
  return '';   // kein Abgleich-Abzeichen mehr (aufgeräumt, 17.11.2026)
  if (!x.f.folien) return '';
  return `<span class="fo-abgl" title="Jede Folie zu diesem Unterthema wurde mit der Lernseite verglichen. Was dabei gefehlt hat, steht jetzt im Text.">✓ Mit den Folien abgeglichen</span>`;
}
/* ---------- Folienfenster zur Lernseite (Knopf „Folien“ in der Werkzeugleiste, „↗ Folie“ an Definitionen und Ergänzungen) ----------
   Alle Seiten der Unterlagen zu diesem Unterthema (auch Übungen und Fallstudien; passt eine Folie zu zwei Unterthemen, steht sie bei beiden).
   Laptop: rechts angedockt (Splitscreen, Breite am linken Rand ziehen) oder gelöst als kleines Fenster (verschieben, Größe ändern).
   Handy: kleines Fenster, das man verschieben kann. Wischen oder ‹ › blättert, Antippen vergrößert. Wechselt das Unterthema, wechseln die Folien mit.
   Lage und Breite merkt sich nur dieses Gerät (localStorage lw-fo-panel). */
const FP = { fid: '', tid: '', liste: [], i: 0 };
const fpLies = () => { try { return JSON.parse(localStorage.getItem('lw-fo-panel') || '{}'); } catch (e) { return {}; } };
const fpMerke = o => { try { localStorage.setItem('lw-fo-panel', JSON.stringify(Object.assign(fpLies(), o))); } catch (e) { } };
const fpHandy = () => matchMedia('(max-width:760px)').matches;
function fpDock() { document.querySelectorAll('[data-fo-panel]').forEach(b => b.classList.toggle('on', !!document.getElementById('fo-panel'))); }
function fpZu() { document.getElementById('fo-panel')?.remove(); document.body.classList.remove('fo-split'); document.body.style.removeProperty('--fo-b'); FP.tid = ''; fpDock(); }
function fpLage(el) {
  const m = fpLies(), frei = fpHandy() || m.frei;
  el.classList.toggle('fo-frei', !!frei); document.body.classList.toggle('fo-split', !frei);
  if (!frei) { document.body.style.setProperty('--fo-b', Math.min(Math.max(m.b || 440, 320), innerWidth * .6) + 'px'); el.style.cssText = ''; return; }
  document.body.style.removeProperty('--fo-b');
  const w = Math.min(m.w || (fpHandy() ? innerWidth - 24 : 460), innerWidth - 16), h = Math.min(m.h || (fpHandy() ? innerHeight * .42 : 380), innerHeight - 80);
  const x = Math.min(Math.max(m.x ?? innerWidth - w - 12, 8), innerWidth - w - 8), y = Math.min(Math.max(m.y ?? (fpHandy() ? 70 : innerHeight - h - 24), 8), innerHeight - h - 8);
  Object.assign(el.style, { left: x + 'px', top: y + 'px', width: w + 'px', height: h + 'px' });
}
function fpOeffne(fid, tid, ziel) {
  let el = document.getElementById('fo-panel');
  if (!el) {
    document.body.insertAdjacentHTML('beforeend', `<aside id="fo-panel" class="fo-panel" role="dialog" aria-label="Folien zu diesem Thema" tabindex="-1">
      <div class="fo-p-rand" title="Breite ziehen"></div>
      <div class="fo-p-kopf"><b>Folien zu diesem Thema</b><span class="fo-p-z"></span>
        <button class="fo-p-k" data-fp="frei" title="Lösen oder andocken">⧉</button><button class="fo-p-k" data-fp="zu" title="Schließen" aria-label="Schließen">✕</button></div>
      <p class="fo-p-deck"></p><div class="fo-p-band"></div>
      <div class="fo-p-fuss"><button class="fo-p-k" data-fp="zurueck" aria-label="Vorige Folie">‹</button><button class="fo-p-k" data-fp="vor" aria-label="Nächste Folie">›</button>
        <button class="btn fo-p-alle" data-fp="alle">Alle Originalfolien</button></div></aside>`);
    el = document.getElementById('fo-panel'); fpLage(el); fpZiehen(el);
  }
  fpDock();
  if (FP.fid === fid && FP.tid === tid && FP.liste.length) return fpGehe(ziel ? Math.max(0, FP.liste.findIndex(x => x.dk === ziel.dk && x.n === ziel.n)) : FP.i, true);
  Object.assign(FP, { fid, tid, liste: [], i: 0 });
  el.querySelector('.fo-p-band').innerHTML = '<p class="fo-dim">Folien werden geladen …</p>';
  foLade(fid).then(d => {
    if (FP.tid !== tid) return;
    const liste = foStellen(fid, tid).flatMap(x => x.seiten.map(n => ({ deck: x.deck, dk: x.deck.id, n })));
    if (ziel && !liste.some(x => x.dk === ziel.dk && x.n === ziel.n)) { const deck = d.decks.find(k => k.id === ziel.dk); if (deck) liste.unshift({ deck, dk: deck.id, n: ziel.n }); }
    FP.liste = liste;
    const band = el.querySelector('.fo-p-band');
    if (!liste.length) { band.innerHTML = '<p class="fo-dim">Zu diesem Unterthema gibt es keine eigene Folie.</p>'; el.querySelector('.fo-p-z').textContent = ''; return; }
    band.innerHTML = liste.map((x, i) => `<div class="fo-p-s" data-i="${i}"><div class="fo-bild" data-fo-bild="${esc(x.dk)}|${x.n}"><span class="fo-nr">Seite ${x.n}</span><div class="fo-ph" aria-hidden="true"></div></div></div>`).join('');
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { const x = FP.liste[+e.target.dataset.i]; if (x) foBildRendern(fid, x.deck, e.target.querySelector('.fo-bild')); } }), { root: band, rootMargin: '0px 100% 0px 100%' });
    band.querySelectorAll('.fo-p-s').forEach(s_ => io.observe(s_));
    band.onscroll = () => { const i = Math.round(band.scrollLeft / Math.max(1, band.clientWidth)); if (i !== FP.i) { FP.i = i; fpText(); } };
    fpGehe(ziel ? Math.max(0, liste.findIndex(x => x.dk === ziel.dk && x.n === ziel.n)) : 0, false);
  }).catch(() => { el.querySelector('.fo-p-band').innerHTML = '<p class="fo-dim">Folien konnten nicht geladen werden.</p>'; });
}
function fpText() {
  const el = document.getElementById('fo-panel'), x = FP.liste[FP.i]; if (!el || !x) return;
  el.querySelector('.fo-p-z').textContent = `${FP.i + 1} / ${FP.liste.length}`;
  el.querySelector('.fo-p-deck').textContent = `${x.deck.titel}${x.deck.art === 'uebung' ? ' (Übung / Fallstudie)' : ''} · Seite ${x.n}`;
}
function fpGehe(i, weich) {
  const band = document.querySelector('#fo-panel .fo-p-band'); if (!band || !FP.liste.length) return;
  FP.i = Math.min(Math.max(i, 0), FP.liste.length - 1); fpText();
  band.scrollTo({ left: FP.i * band.clientWidth, behavior: weich ? 'smooth' : 'auto' });
}
/* Verschieben (am Kopf, gelöst) und Breite ändern (linker Rand, angedockt); die Größe des gelösten Fensters ändert die Ecke unten rechts */
function fpZiehen(el) {
  const kopf = el.querySelector('.fo-p-kopf'), rand = el.querySelector('.fo-p-rand');
  kopf.addEventListener('pointerdown', e => {
    if (!el.classList.contains('fo-frei') || e.target.closest('button')) return;
    const r = el.getBoundingClientRect(), dx = e.clientX - r.left, dy = e.clientY - r.top; kopf.setPointerCapture(e.pointerId);
    const mv = ev => { el.style.left = Math.min(Math.max(ev.clientX - dx, 0), innerWidth - 60) + 'px'; el.style.top = Math.min(Math.max(ev.clientY - dy, 0), innerHeight - 40) + 'px'; };
    const up = () => { kopf.removeEventListener('pointermove', mv); fpMerke({ x: parseFloat(el.style.left), y: parseFloat(el.style.top) }); };
    kopf.addEventListener('pointermove', mv); kopf.addEventListener('pointerup', up, { once: true });
  });
  rand.addEventListener('pointerdown', e => {
    if (el.classList.contains('fo-frei')) return; rand.setPointerCapture(e.pointerId);
    const mv = ev => document.body.style.setProperty('--fo-b', Math.min(Math.max(innerWidth - ev.clientX, 320), innerWidth * .6) + 'px');
    const up = () => { rand.removeEventListener('pointermove', mv); fpMerke({ b: parseFloat(document.body.style.getPropertyValue('--fo-b')) }); fpGehe(FP.i); };
    rand.addEventListener('pointermove', mv); rand.addEventListener('pointerup', up, { once: true });
  });
  new ResizeObserver(() => { if (el.classList.contains('fo-frei') && el.isConnected && el.style.width) { fpMerke({ w: el.offsetWidth, h: el.offsetHeight }); } }).observe(el);
  el.addEventListener('keydown', e => { if (e.key === 'ArrowRight') fpGehe(FP.i + 1, true); else if (e.key === 'ArrowLeft') fpGehe(FP.i - 1, true); else if (e.key === 'Escape') fpZu(); });
}
document.addEventListener('click', e => {
  const k = e.target.closest('[data-fo-panel]');
  if (k) { const [fid, tid] = k.dataset.foPanel.split('|'); if (document.getElementById('fo-panel') && FP.tid === tid) fpZu(); else fpOeffne(fid, tid); return; }
  const b = e.target.closest('[data-fo-folie]');   // „↗ Folie“: Fenster an genau dieser Folie
  if (b) { e.preventDefault(); const [fid, dk, n] = b.dataset.foFolie.split('|'); fpOeffne(fid, V.screen === 'lern' && V.fid === fid ? V.tid : '', { dk, n: +n }); return; }
  const a = e.target.closest('#fo-panel [data-fp]'); if (!a) return;
  const was = a.dataset.fp;
  if (was === 'zu') fpZu();
  else if (was === 'vor') fpGehe(FP.i + 1, true);
  else if (was === 'zurueck') fpGehe(FP.i - 1, true);
  else if (was === 'frei') { fpMerke({ frei: !fpLies().frei }); fpLage(document.getElementById('fo-panel')); setTimeout(() => fpGehe(FP.i), 50); }
  else if (was === 'alle') { const x = FP.liste[FP.i], fid = FP.fid; fpZu(); const z = foZustand(); Object.assign(z, { fid, deck: x ? x.dk : '', seite: x ? x.n : 0, filter: 'alle', thema: '' }); if (V.screen !== 'folien') try { history.pushState(null, '', '#folien'); } catch (er) { } V.screen = 'folien'; render(true); }
});
document.addEventListener('click', e => {   // Antippen einer Folie im Fenster: groß
  const s_ = e.target.closest('#fo-panel .fo-p-s'); if (!s_) return; const x = FP.liste[+s_.dataset.i]; if (x) foGross(FP.fid, x.deck, x.n);
}, true);
/* Unterthema gewechselt: Folien wechseln mit; Lernseite verlassen: Fenster schließt */
addEventListener('hashchange', () => setTimeout(() => {
  if (!document.getElementById('fo-panel')) return;
  if (V.screen !== 'lern') return fpZu();
  if (V.tid !== FP.tid && F[V.fid] && F[V.fid].folien) fpOeffne(V.fid, V.tid); else fpDock();
}, 60));
addEventListener('resize', () => { const el = document.getElementById('fo-panel'); if (el) { fpLage(el); fpGehe(FP.i); } });

/* folien.js lädt nach ansichten.js: steht man schon auf #folien, jetzt zeichnen */
if (typeof V !== 'undefined' && V.screen === 'folien') render();
