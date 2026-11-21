/* ===== Gemeinsame Lernseiten-Bausteine für alle Fächer: Zuordnungsspiel und Umschalt-Tafeln ===== */
/* Zuordnungsspiel (wie Materialarten in Logistik): <div class="p-spiel" data-spiel='{"f":[en,de],"k":[[en,de]…],"c":[[en,de,k,warum_en,warum_de]…]}'> */
(function(){
  document.querySelectorAll('.p-spiel').forEach(box => {
    if (box.dataset.bereit) return; box.dataset.bereit = '1';
    const D = JSON.parse(box.dataset.spiel); let i = 0, ok = 0, fertig = false;
    const reihe = D.c.map((c, j) => j).sort(() => Math.random() - .5);
    function zeig(){
      if (i >= reihe.length) {
        box.innerHTML = `<div class="sp-ende"><b>${ok} ${LG('of', 'von')} ${reihe.length} ${LG('correct', 'richtig')}.</b> ${ok === reihe.length ? LG('Everything sorted!', 'Alles richtig eingeordnet!') : LG('Read the explanations again and play once more.', 'Lies die Erklärungen noch einmal und spiel eine zweite Runde.')}</div><button type="button" class="btn sp-neu">${LG('Play again', 'Noch einmal')}</button>`;
        box.querySelector('.sp-neu').onclick = () => { i = 0; ok = 0; reihe.sort(() => Math.random() - .5); zeig(); }; return;
      }
      const c = D.c[reihe[i]]; fertig = false;
      box.innerHTML = `<div class="sp-kopf"><span>${LG(...D.f)}</span><small>${i + 1} / ${reihe.length}</small></div><p class="sp-karte">${LG(c[0], c[1])}</p>`
        + `<div class="rules sp-wahl">${D.k.map((k, j) => `<button type="button" data-j="${j}">${LG(...k)}</button>`).join('')}</div><div class="sp-aus"></div>`;
      box.querySelectorAll('.sp-wahl button').forEach(b => b.onclick = () => {
        if (fertig) return; fertig = true;
        const j = +b.dataset.j, r = j === c[2]; if (r) ok++;
        b.classList.add('on'); if (!r) box.querySelector(`.sp-wahl [data-j="${c[2]}"]`).classList.add('sp-richtig');
        box.querySelector('.sp-aus').innerHTML = (r ? `<b class="sp-ok">✓ ${LG('Correct.', 'Richtig.')}</b> ` : `<b class="sp-nok">✗ ${LG('Not quite', 'Nicht ganz')}:</b> ${LG('correct is', 'richtig ist')} <b>${LG(...D.k[c[2]])}</b>. `)
          + LG(c[3], c[4]) + ` <button type="button" class="btn sp-weiter">${LG('Next', 'Weiter')} →</button>`;
        box.querySelector('.sp-weiter').onclick = () => { i++; zeig(); };
      });
    }
    zeig(); NEU.push(() => zeig());
  });
})();

/* Umschalt-Tafeln: <div class="rules" data-tafeln> + <div class="umpanel" data-for=… data-k=…> */
(function(){
  document.querySelectorAll('.rules[data-tafeln]').forEach(r => {
    if (r.dataset.bereit) return; r.dataset.bereit = '1';
    const scope = r.closest('.figure, .mfig-body, .article, .t-body') || document;
    UM(r.id, k => scope.querySelectorAll('.umpanel[data-for="' + r.id + '"]').forEach(p => p.hidden = +p.dataset.k !== k));
  });
})();
