/* Lernweh · Gruß mit Namen und Gedanken des Tages, Rundgang durch alle Bereiche, Hell-Erkennung für die Glas-Akzente.
   Name und „Rundgang gesehen“ stehen in S.einst (werden mit dem Login-Code abgeglichen). */

/* Gedanken: kurz, ruhig, eher nachdenklich als antreibend; täglich ein anderer, Antippen zeigt den nächsten */
const GEDANKEN = [
  'Lernen ist Fernweh nach dem, was du noch nicht weißt.',
  'Jeder Gedanke, den du heute verstehst, macht den nächsten leichter.',
  'Was du dir selbst erklären kannst, gehört dir für immer.',
  'Verstehen ist kein Ort, an dem man ankommt. Es ist eine Richtung.',
  'Zweifel ist kein Rückschritt. Er ist der Anfang jedes Verstehens.',
  'Neugier ist der kürzeste Weg zwischen dir und dem nächsten Aha.',
  'Wer Fragen stellt, ist schon unterwegs.',
  'Heute ist ein guter Tag, etwas zum ersten Mal wirklich zu begreifen.',
  'Wissen wächst leise. Man merkt es erst, wenn man zurückschaut.',
  'Jede schwierige Seite ist eine, die du bald erklären kannst.'];
let gedankeI = Math.floor(Date.now() / 864e5) % GEDANKEN.length;
/* Name: selbst eingetragen (S.einst.name) oder der Vorname aus der Notiz zum Login-Code im Admin-Bereich */
const lwName = () => S.einst.name || ((typeof SYNC !== 'undefined' && SYNC.name) || '').split(/\s+/)[0];
function nameAuffrischen() { document.querySelectorAll('.lw-name').forEach(n => { if (document.activeElement !== n) n.textContent = lwName(); }); }
function grussHTML() {
  const h = new Date().getHours(), anrede = h < 11 ? 'Guten Morgen' : h >= 18 ? 'Guten Abend' : 'Hallo';
  return `<div class="lw-gruss"><b>${anrede} <span class="lw-name" contenteditable="true" spellcheck="false" data-ph="dein Name" title="Antippen, um deinen Namen einzutragen">${esc(lwName())}</span>,</b>
    <p class="lw-gedanke" title="Antippen für einen neuen Gedanken">${GEDANKEN[gedankeI]}</p></div>`;
}
document.addEventListener('click', e => {
  const p = e.target.closest('.lw-gedanke'); if (!p) return;
  p.classList.add('weg'); setTimeout(() => { gedankeI = (gedankeI + 1) % GEDANKEN.length; p.textContent = GEDANKEN[gedankeI]; p.classList.remove('weg'); }, 280);
});
document.addEventListener('keydown', e => { if (e.target.matches && e.target.matches('.lw-name') && e.key === 'Enter') { e.preventDefault(); e.target.blur(); } });
document.addEventListener('focusout', e => {
  if (!e.target.matches || !e.target.matches('.lw-name')) return;
  const v = e.target.textContent.trim().slice(0, 24); S.einst.name = v; save(); e.target.textContent = lwName();
});

/* hell oder dunkel? Die Glas- und Farbakzente gelten nur im hellen Modus, der Dunkelmodus bleibt unverändert */
(function () {
  const R = document.documentElement, mq = matchMedia('(prefers-color-scheme: dark)');
  const hell = () => { const t = R.getAttribute('data-theme'); R.classList.toggle('lw-hell', t ? t === 'light' : !mq.matches); };
  mq.addEventListener('change', hell); new MutationObserver(hell).observe(R, { attributes: true, attributeFilter: ['data-theme'] }); hell();
})();

/* Rundgang je Bereich: Start, Lernseite, Training. Jeder startet beim ersten Besuch des Bereichs von selbst, „?“ zeigt den des aktuellen Bereichs.
   Während des Rundgangs ist der Bildschirm gesperrt (kein eigenes Scrollen, keine Klicks auf die Seite). */
const STAND_BILD = `<span class="lw-weg"><span><b>Lesen</b><small>Lernseite</small></span><i>→</i><span><b>Mini-Quiz</b><small>zählt nicht</small></span><i>→</i><span class="an"><b>Übungsklausur</b><small>je Oberthema</small></span><i>→</i><span><b>% des Oberthemas</b><small>Ø aller = Ring</small></span></span>`;
const RUNDGAENGE = {
  start: [
    ['.lw-gruss', 'Willkommen bei Lernweh', 'Lernweh ist ein Werkzeug, kein Lernplan: Du entscheidest, was du lernst. Tippe oben auf den Namen und trag deinen ein. Jeden Tag wartet hier ein neuer Gedanke.'],
    ['.m-deck', 'Deine Fächer', 'Jede Karte ist ein Fach mit seinem Klausurtermin. Antippen dreht die Karte um: Dann siehst du alle Oberthemen und wie weit du bei jedem bist.'],
    ['.m-deck', 'So entsteht dein Lernstand', `${STAND_BILD}<br>Lesen und Mini-Quiz helfen beim Verstehen, ändern aber noch keine Prozente. Erst wenn du ein Oberthema mit seiner Übungsklausur abprüfst, bekommt es einen Prozentwert. Der Ring auf der Karte ist der Durchschnitt aller Oberthemen des Fachs. 0 % heißt also nur: noch nichts abgeprüft.`],
    ['.m-weiter', 'Weiterlernen', 'Ein Tipp, und du bist genau dort, wo du aufgehört hast.'],
    ['.m-blass', 'Verblassen und Auffrischen', 'Ein abgeprüfter Stand hält nicht ewig. Nach einiger Zeit verblasst er und erscheint hier. Ein Refresh von 5 Minuten bringt ihn zurück.'],
    ['.m-wackel', 'Methodisch lernen', 'Was du irgendwo nicht konntest, kommt hier zum richtigen Zeitpunkt zurück.'],
    ['.tabbar', 'Lernen und Training', 'Unten wechselst du die Bereiche. Lernen und Training zeigen dir beim ersten Öffnen kurz, was sie können. Das „?“ oben rechts erklärt immer die Seite, auf der du gerade bist.']],
  lernen: [
    ['.bl-hero', 'Die Lernseite', 'Fach, Oberthema, Unterthema. Oben steht das Oberthema; über die Auswahl springst du zu jedem anderen.'],
    ['.bl-rail', 'Unterthemen', 'Die Unterthemen dieses Oberthemas, der Reihe nach. Die Punkte zeigen, wie sicher du schon bist.'],
    ['.inhalt', 'Erklärungen und Schaubilder', 'Kurz erklärt, Formeln mit „In Worten“ und Beispiel, Schaubilder zum Antippen und Rechner zum Ausprobieren.'],
    ['.a-dock-in', 'Deine Werkzeuge', 'Text verdecken zum Abfragen, markieren, als unsicher merken, suchen und Karteikarten aus diesem Thema.'],
    ['.bl-mini', 'Mini-Quiz', 'Fünf schnelle Fragen nach dem ersten Lesen. Sie zeigen, ob du es verstanden hast, zählen aber noch nicht für den Lernstand.'],
    ['.mi-stand', 'Oberthema abprüfen', `${STAND_BILD}<br>Hast du alle Unterthemen gelernt, startest du hier die Übungsklausur. Ihr Ergebnis wird der Prozentwert dieses Oberthemas und fließt in den Ring des Fachs. Nur so steigt dein Lernstand.`]],
  training: [
    ['.sx-was', 'Was üben?', 'Wähle ein oder mehrere Fächer. Über „Oberthemen“ grenzt du bis auf einzelne Oberthemen ein.'],
    ['.sx-werk', 'Wie üben?', 'Quiz, Definitions-Drill, Karteikarten und Arbeitsblatt. Nach jeder Lösung sagst du, ob du es konntest: „Nein“ und „Teilweise“ kommen später unter Methodisch lernen zurück.'],
    ['.sx-pruefen', 'Abprüfen', `${STAND_BILD}<br>Hier prüfst du ohne Hilfen, mit Zeit und Note: ein einzelnes Oberthema, ein ganzes Fach oder die komplette Klausur. Jede Übungsklausur zu einem Oberthema setzt dessen Prozentwert.`]]};
function bereich() { const h = location.hash.slice(1); return !h || h === 'heute' ? 'start' : h.startsWith('lernen--') ? 'lernen' : h === 'sandbox' ? 'training' : null; }
(function () {
  let ti = 0, liste = [], name = 'start', tour, spot, blase;
  const R = document.documentElement, $ = s => document.querySelector(s);
  const gesehen = () => (S.einst.rundgang && typeof S.einst.rundgang === 'object') ? S.einst.rundgang : (S.einst.rundgang = S.einst.rundgang ? { start: 1 } : {});
  const sperre = e => { if (tour && tour.classList.contains('on') && !e.target.closest('.lw-tour-blase')) e.preventDefault(); };
  const tasten = e => {
    if (!tour || !tour.classList.contains('on')) return;
    if (e.key === 'ArrowRight' || e.key === 'Enter') { e.preventDefault(); weiter(); } else if (e.key === 'ArrowLeft') { e.preventDefault(); zurueck(); }
    else if (e.key === 'Escape') ende(); else if ([' ', 'ArrowUp', 'ArrowDown', 'PageUp', 'PageDown', 'Home', 'End'].includes(e.key)) e.preventDefault();
  };
  function warte(sel, fn, n = 0) { const el = $(sel); if (el && el.getBoundingClientRect().height) fn(el); else if (n < 50) setTimeout(() => warte(sel, fn, n + 1), 60); else fn(null); }
  function zeige() {
    const [sel, t, x] = liste[ti];
    blase.querySelector('small').textContent = `${{ start: 'START', lernen: 'LERNSEITE', training: 'TRAINING' }[name]} · ${ti + 1} VON ${liste.length}`;
    blase.querySelector('h3').textContent = t; blase.querySelector('p').innerHTML = x;
    blase.querySelector('.lw-w').textContent = ti === liste.length - 1 ? 'Fertig' : 'Weiter';
    blase.querySelector('.lw-z').style.visibility = ti ? 'visible' : 'hidden';
    blase.querySelector('.lw-tour-punkte').innerHTML = liste.map((_, i) => `<i class="${i === ti ? 'on' : ''}"></i>`).join('');
    blase.style.opacity = '0';
    warte(sel, el => {
      if (!el) { if (ti < liste.length - 1) { ti++; zeige(); } else ende(); return; }
      if (sel !== '.tabbar') { const r = el.getBoundingClientRect(), y = scrollY + r.top - (r.height > innerHeight * .55 ? 90 : (innerHeight - r.height) / 2 - 60); scrollTo({ top: Math.max(0, y), behavior: 'instant' }); }
      requestAnimationFrame(() => { platz(); blase.style.opacity = '1'; setTimeout(platz, 250); });
    });
  }
  function platz() {
    if (!tour || !tour.classList.contains('on')) return; const el = $(liste[ti][0]); if (!el) return;
    const r = el.getBoundingClientRect(), p = 8, oben = Math.max(6, r.top - p), unten = Math.min(r.bottom + p, innerHeight - 6);
    Object.assign(spot.style, { left: Math.max(6, r.left - p) + 'px', top: oben + 'px', width: Math.min(r.width + 2 * p, innerWidth - 12) + 'px', height: Math.max(40, unten - oben) + 'px' });
    const bh = blase.offsetHeight, bw = blase.offsetWidth;
    let by = unten + 12 + bh < innerHeight - 8 ? unten + 12 : oben - bh - 12; if (by < 8) by = innerHeight - bh - 16;
    blase.style.top = by + 'px'; blase.style.left = Math.min(Math.max(16, r.left), innerWidth - bw - 16) + 'px';
  }
  const weiter = () => { if (ti < liste.length - 1) { ti++; zeige(); } else ende(); };
  const zurueck = () => { if (ti) { ti--; zeige(); } };
  function ende() { tour.classList.remove('on'); R.classList.remove('lw-gesperrt'); gesehen()[name] = 1; save(); }
  function starte(b) { name = b || bereich() || 'start'; if (name === 'start' && bereich() !== 'start') location.hash = 'heute'; liste = RUNDGAENGE[name]; if (!tour) baue(); ti = 0; tour.classList.add('on'); R.classList.add('lw-gesperrt'); zeige(); }
  function baue() {
    tour = document.createElement('div'); tour.className = 'lw-tour'; tour.setAttribute('role', 'dialog'); tour.setAttribute('aria-modal', 'true'); tour.setAttribute('aria-label', 'Rundgang');
    tour.innerHTML = `<div class="lw-tour-spot"></div><div class="lw-tour-blase"><small></small><h3></h3><p></p>
      <div class="lw-tour-zeile"><span class="lw-tour-punkte"></span><span><button class="lw-e">Beenden</button><button class="lw-z">Zurück</button><button class="lw-w">Weiter</button></span></div></div>`;
    document.body.appendChild(tour); spot = tour.querySelector('.lw-tour-spot'); blase = tour.querySelector('.lw-tour-blase');
    blase.querySelector('.lw-w').onclick = weiter; blase.querySelector('.lw-z').onclick = zurueck; blase.querySelector('.lw-e').onclick = ende;
    tour.addEventListener('click', e => { if (!e.target.closest('.lw-tour-blase')) e.stopPropagation(); });
    addEventListener('resize', platz); addEventListener('scroll', () => requestAnimationFrame(platz), { passive: true });
    addEventListener('wheel', sperre, { passive: false }); addEventListener('touchmove', sperre, { passive: false }); addEventListener('keydown', tasten, true);
  }
  /* erster Besuch eines Bereichs: dessen Rundgang zeigen */
  function pruefe() {
    if (navigator.webdriver || GEIST || (tour && tour.classList.contains('on'))) return;
    const b = bereich(); if (b && !gesehen()[b]) setTimeout(() => { if (bereich() === b && !gesehen()[b] && !(tour && tour.classList.contains('on'))) starte(b); }, 1100);
  }
  /* Zurück-Pfeil auf Seiten ohne eigenen Rückweg (Prüfung, Probeklausur, Einstellungen) */
  function pfeil() {
    let z = document.querySelector('.lw-zurueck');
    const zeigen = /^#(pruefung|probeklausur|fachprobe|einstellungen|folien)/.test(location.hash);
    if (!z) { z = document.createElement('button'); z.className = 'lw-zurueck'; z.setAttribute('aria-label', 'Zurück'); z.innerHTML = '<svg viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7"/></svg><span>Zurück</span>';
      z.onclick = () => { if (history.length > 1) history.back(); else location.hash = /^#(einstellungen|folien)/.test(location.hash) ? 'heute' : 'sandbox'; }; document.body.appendChild(z); }
    z.hidden = !zeigen; document.documentElement.classList.toggle('lw-mit-zurueck', zeigen);
  }
  function knopf() {
    if (document.querySelector('.lw-tour-knopf')) return;
    const k = document.createElement('button'); k.className = 'lw-tour-knopf'; k.textContent = '?'; k.title = 'Was kann diese Seite?'; k.setAttribute('aria-label', 'Rundgang für diese Seite');
    k.onclick = () => starte(); document.body.appendChild(k);
    addEventListener('hashchange', () => { pruefe(); pfeil(); }); pruefe(); pfeil();
  }
  window.rundgangStarten = starte;
  if (document.body) knopf(); else document.addEventListener('DOMContentLoaded', knopf);
})();
