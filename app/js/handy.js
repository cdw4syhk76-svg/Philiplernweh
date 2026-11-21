/* Lernweh · Abschnitte auf- und zuklappen (alle Geräte).
   - „Ganz erklären“: jeder Abschnitt mit Zwischenüberschrift (h3) bekommt einen Pfeil. Am Laptop ist anfangs alles offen,
     am Handy der erste Abschnitt.
   - „Alle auf · Alle zu“ oben im Text; was man selbst auf- oder zuklappt, merkt sich die App je Unterthema (nur auf diesem Gerät).
   - Sprünge (Inhaltsverzeichnis, Suche, „Im Text nachschlagen“) öffnen den Abschnitt, in dem das Ziel liegt. */
(function () {
  const mq = matchMedia('(max-width:600px)');
  const SPEICHER = 'lw-klapp';
  const lies = () => { try { return JSON.parse(localStorage.getItem(SPEICHER) || '{}'); } catch (e) { return {}; } };
  const merke = (k, offen) => { try { const m = lies(); m[k] = offen ? 1 : 0; localStorage.setItem(SPEICHER, JSON.stringify(m)); } catch (e) { } };
  const thema = el => { const c = el.closest('[data-tid]'); return (location.hash.split('--')[1] || '') + '/' + (c ? c.dataset.tid : ''); };
  function kopfMachen(h, box, offen, key) {
    h.classList.add('lw-kopf'); h.setAttribute('role', 'button'); h.tabIndex = 0; h.dataset.klapp = key;
    if (!h.querySelector('.lw-pfeil')) h.insertAdjacentHTML('beforeend', '<span class="lw-pfeil" aria-hidden="true"></span>');
    box.hidden = !offen; h.setAttribute('aria-expanded', String(offen));
  }
  function klappe() {
    const gemerkt = lies();
    document.querySelectorAll('.inhalt .article:not([data-lw-klapp])').forEach(art => {
      const koepfe = [...art.children].filter(e => e.tagName === 'H3');
      art.dataset.lwKlapp = '1';
      const t = thema(art);
      koepfe.forEach((h, i) => {
        const box = document.createElement('div'); box.className = 'lw-abs';
        let n = h.nextElementSibling;
        while (n && n.tagName !== 'H3') { const w = n.nextElementSibling; box.appendChild(n); n = w; }
        h.after(box);
        const key = t + '#' + i, start = mq.matches ? i === 0 : true;
        kopfMachen(h, box, key in gemerkt ? !!gemerkt[key] : start, key);
      });
      const erg = null, viele = art.querySelectorAll('.lw-kopf').length >= 2;
      if ((viele || erg) && !art.querySelector('.lw-alle'))
        art.insertAdjacentHTML('afterbegin', '<div class="lw-alle">' + (viele ? '<button type="button" data-lw-alle="1">Alle auf</button><span aria-hidden="true">·</span><button type="button" data-lw-alle="0">Alle zu</button>' : '')
          + (erg ? (viele ? '<span aria-hidden="true">·</span>' : '') + '<button type="button" class="lw-nur" data-lw-nur aria-pressed="false" title="Zeigt vorübergehend nur die Stellen mit Stoff aus den Folien (gold)">Nur Folienstoff</button>' : '') + '</div>');
    });
  }
  /* „Nur Folienstoff“: vorübergehend nur die Absätze, Listen und Tabellen zeigen, in denen Stoff aus den Folien steht (gold); nichts wird gemerkt */
  const ERG = '[data-an], .fo-wl';   // gold: Stoff aus den Folien im Wortlaut (ansichten.js inhaltHTML, bau.py definitionen_gold)
  function nurErg(art, an) {
    art.classList.toggle('lw-nur-erg', an); art.querySelector('[data-lw-nur]')?.setAttribute('aria-pressed', String(an));
    art.querySelectorAll('.lw-kopf').forEach(h => { const box = h.nextElementSibling; if (!box || !box.classList.contains('lw-abs')) return;
      const hat = !!box.querySelector(ERG) || h.matches(ERG); h.classList.toggle('lw-ohne-erg', an && !hat);
      if (an) { h.dataset.vorher = h.getAttribute('aria-expanded'); if (hat) setze(h, true, false); }
      else if (h.dataset.vorher) { setze(h, h.dataset.vorher === 'true', false); delete h.dataset.vorher; } });
  }
  const setze = (h, offen, merken) => { const box = h.nextElementSibling; if (!box || !box.classList.contains('lw-abs')) return; box.hidden = !offen; h.setAttribute('aria-expanded', String(offen)); if (merken) merke(h.dataset.klapp, offen);
    if (offen && typeof formelnEinpassen === 'function') requestAnimationFrame(() => formelnEinpassen(box)); };   // aufgeklappt: Formeln jetzt einpassen
  const umschalten = h => setze(h, h.getAttribute('aria-expanded') !== 'true', true);
  /* Ein Element sichtbar machen: alle zugeklappten Abschnitte darüber öffnen (für Suche, Nachschlagen, Sprünge) */
  window.lwOeffne = el => { let n = el; while (n && n !== document.body) { if (n.classList && n.classList.contains('lw-abs') && n.hidden) setze(n.previousElementSibling, true, false); n = n.parentElement; } };
  document.addEventListener('click', e => {
    const alle = e.target.closest('[data-lw-alle]');
    if (alle) { const art = alle.closest('.article'); art.querySelectorAll('.lw-kopf').forEach(h => setze(h, alle.dataset.lwAlle === '1', true)); return; }
    const nur = e.target.closest('[data-lw-nur]');
    if (nur) { const art = nur.closest('.article'); nurErg(art, !art.classList.contains('lw-nur-erg')); return; }
    const h = e.target.closest('.lw-kopf'); if (h) { umschalten(h); return; }
    const a = e.target.closest('.inhalt .toc a[href^="#"]');   // Sprung aus dem Inhaltsverzeichnis: Abschnitt öffnen
    if (a) { const z = document.getElementById(a.getAttribute('href').slice(1)); if (z) { if (z.classList.contains('lw-kopf')) setze(z, true, false); window.lwOeffne(z); } }
  }, true);
  document.addEventListener('keydown', e => { const h = e.target.closest && e.target.closest('.lw-kopf'); if (h && (e.key === 'Enter' || e.key === ' ')) { e.preventDefault(); umschalten(h); } });
  const start = () => { new MutationObserver(() => { klappe(); }).observe(document.body, { childList: true, subtree: true }); klappe(); };
  if (document.body) start(); else document.addEventListener('DOMContentLoaded', start);
})();
