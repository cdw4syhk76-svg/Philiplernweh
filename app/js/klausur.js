/* ---------- Klausurbogen: Probeklausur im Aufbau der echten Klausur ----------
   Daten: inhalte/<fach>/klausur.json → f.klausur = { deckblatt, aufgaben: [{ nr, titel, punkte, teile: [{ punkte, varianten: [...] }] }] }
   Variante: { id, unter, text, felder: [{ typ: zahl|menge|ausdruck|matrix|text|rf|wort|sc (o: 4 Optionen, r: Index), label, loesung, p, ... }], loesung, bild? }
   Formeln: \( … \) und \[ … \] werden mit KaTeX gesetzt. */

/* ---------- Formeln setzen ---------- */
function mathe(html) {
  if (!html || typeof katex === 'undefined') return html || '';
  const r = (t, d) => { try { return katex.renderToString(t.replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>'), { throwOnError: false, displayMode: d }); } catch (e) { return t; } };
  return String(html).replace(/\\\[([\s\S]+?)\\\]/g, (_, t) => r(t, true)).replace(/\\\(([\s\S]+?)\\\)/g, (_, t) => r(t, false));
}

/* Schreibweise wie auf Papier: „a ÷ b“ und kurze Formeln wie „K/Y“, „1/x“, „(a+b)/2“ werden echte Brüche,
   \( … \) wird mit KaTeX gesetzt. Gilt für Fragen, Lösungen, Arbeitsblätter, Karten und Klausurbögen aller Fächer. */
const BR_ATOM = String.raw`(?:\((?:[^()]|\([^()]*\))*\)|(?:Ø\s?)?[A-Za-zÄÖÜäöüß0-9.,_′∂ΔπλμσεΣ√₀-₉ⁿ⁻⁺⁰-⁹ᵢⱼₜₙ€%\u0001-\u0004\uE000-\uE0FF]+)`;
const BR_DIV = new RegExp(`(${BR_ATOM})\\s*÷\\s*(${BR_ATOM})`, 'g');
const BR_KURZ = /(^|[\s=(≈→,;:])((?:\([^()<>]{1,40}\))|[A-Za-z∂Δ]{0,2}[A-Za-z0-9₀-₉ⁿ⁻⁰-⁹ᵢⱼₜ′]{1,4})\/((?:\([^()<>]{1,40}\))|[A-Za-z∂Δ]{0,2}[A-Za-z0-9₀-₉ⁿ⁻⁰-⁹ᵢⱼₜ′²³]{1,4})(?=$|[\s)=,.;:·+−])/g;
const brKlammer = s => /^\((?:[^()]|\([^()]*\))*\)$/.test(s) ? s.slice(1, -1) : s;
const brWort = s => /^[A-Za-zÄÖÜäöüß]{3,}$/.test(s);   // „und/oder“, „Ein-/Ausgang“ bleiben Text
const brSpan = (a, b) => `<span class="fr"><span>${brKlammer(a)}</span><span>${brKlammer(b)}</span></span>`;
/* „Zähler ÷ Nenner“ wie auf Papier: der Zähler reicht zurück bis „=“, „(“, Satzzeichen oder Textanfang (Produkte und
   Wortgruppen wie „eigener Absatz · 100“), der Nenner bis zum nächsten „·“, „=“, „+“, „−“ oder Satzzeichen. Zu lange
   Wortgruppen (> 7 Wörter) fallen auf die kurze Form (ein Glied) zurück. Klammern werden übersprungen. */
const BR_LGRENZE = /[=≈:;(\u0001→„“<>\n]/, BR_RGRENZE = /[=≈:;)\u0002→“<>·×÷\n]/;
const BR_ABK = /(^|\s)(kurzfr|langfr|mittelfr|Verb|Ford|inkl|ca|evtl|ggf|Std|Mio|Mrd|Tsd|Nr|Abs|rel|max|min|durchschn)$/;
function brSeite(t, i, schritt) {   // Ende (exklusiv bzw. Anfang) der Seite ab Position i
  let j = i, tiefe = 0;
  const auf = schritt < 0 ? ')' : '(', zu = schritt < 0 ? '(' : ')';
  for (; schritt < 0 ? j > 0 : j < t.length; j += schritt) {
    const c = schritt < 0 ? t[j - 1] : t[j];
    if (c === auf) { tiefe++; continue; }
    if (c === zu) { if (tiefe) { tiefe--; continue; } break; }
    if (tiefe) continue;
    if (schritt < 0 ? BR_LGRENZE.test(c) : BR_RGRENZE.test(c)) break;
    const um = schritt < 0 ? t.slice(Math.max(0, j - 3), j) : t.slice(j, j + 3);
    if (/^ [+−-] $/.test(um)) break;
    const punkt = schritt < 0 ? /^[,.] $/.test(t.slice(j - 2, j)) && j - 2 : /^[,.](\s|$|[“”"»])/.test(t.slice(j, j + 2)) && j;
    if (punkt !== false && !(t[punkt] === '.' && BR_ABK.test(t.slice(0, punkt)))) break;
    if (schritt > 0 && /^ \(/.test(t.slice(j, j + 2)) && t.slice(i, j).trim()) break;   // Erläuterung in Klammern nach dem Nenner
  }
  return j;
}
const BR_STOP = /^(ist|sind|war|wird|werden|heißt|heißen|beträgt|betragen|gilt|ergibt|ergeben|bedeutet|muss|müssen|soll|sollte|kann|also|dann|wenn|als|nur|auch|man|ein|eine|einen|einem|einer|mit|bei|für|durch|und|oder|bzw\.?|wie|Wie|Was|Welche|Welcher|Welches|Die|Der|Das|Ein|Eine|Es|es|nicht|kein|keine|nötig|Rechne|Berechne|Berechnen|rechnet|immer|hier|so|Wer|wer|heute|liegt|liegen|macht|bringt|kostet|jede|jeder|jedes|Bei|Mit|Für|Im|Am|Um|Auf|Über|Unter|Gegen|Ohne|Zum|Zur|Vom|Nach|Aus)$/;
const BR_ART = /^(die|das|den|dem)$/;   // Artikel beenden nur den Zähler; „der“ nicht („Summe der Werte“, „Absatz des größten …“)
function brDivision(t) {
  let i = t.indexOf('÷');
  while (i >= 0) {
    const a0 = brSeite(t, i, -1), b1 = brSeite(t, i + 1, 1);
    let a = t.slice(a0, i), b = t.slice(i + 1, b1);
    const vorn = a.match(/^\s*/)[0], hinten = b.match(/\s*$/)[0];
    a = a.trim(); b = b.trim();
    const oben = ws => { let d = 0; return ws.map(w => { const vor = d; d += (w.match(/\(/g) || []).length - (w.match(/\)/g) || []).length; return vor === 0 && d === 0; }); };   // Wort außerhalb von Klammern?
    const wa = a.split(/\s+/), oa = oben(wa), sa = wa.map((w, k) => oa[k] && (BR_STOP.test(w) || BR_ART.test(w))).lastIndexOf(true);
    if (sa >= 0) a = wa.slice(sa + 1).join(' ');
    const wb = b.split(/\s+/), ob = oben(wb), sb = wb.findIndex((w, k) => ob[k] && BR_STOP.test(w));
    if (sb >= 0) b = wb.slice(0, sb).join(' ');
    const zuLang = x => x.split(/\s+/).length > 7 || x.length > 70;
    if (zuLang(a)) { const m = a.match(new RegExp(`${BR_ATOM}$`)); a = m ? m[0] : ''; }
    if (zuLang(b)) { const m = b.match(new RegExp(`^${BR_ATOM}`)); b = m ? m[0] : ''; }
    if (!a || !b || /^[·×+−-]/.test(a)) { i = t.indexOf('÷', i + 1); continue; }
    const start = t.lastIndexOf(a, i), ende = t.indexOf(b, i) + b.length;
    const neu = brSpan(a, b);
    t = t.slice(0, start) + neu + t.slice(ende);
    i = t.indexOf('÷', start + neu.length);
  }
  return t;
}
const BR_INDEX = /(^|[^A-Za-zÄÖÜäöüß_])([A-Za-zΔσμ]{1,3})_(\{[^{}<>]{1,12}\}|[A-Za-z0-9ÄÖÜäöü]{1,5})(?![A-Za-z0-9_])/g;
function wurzeln(t) {   // √( … ) → Wurzel mit Strich über dem ganzen Ausdruck (Marken \u0001 … \u0002)
  let i = t.indexOf('√(');
  while (i >= 0) {
    let j = i + 2, tiefe = 0;
    for (; j < t.length; j++) { if (t[j] === '(') tiefe++; else if (t[j] === ')') { if (!tiefe) break; tiefe--; } }
    if (j >= t.length) break;
    t = t.slice(0, i) + '√\u0001' + t.slice(i + 2, j) + '\u0002' + t.slice(j + 1);
    i = t.indexOf('√(', i + 2);
  }
  return t;
}
/* Matrizen und Vektoren wie auf Papier: „(1 2 3; 4 5 6)“ (zeilenweise, Zeilen mit „;“) → Matrix in runden Klammern,
   „b = (1; 1; 1)“ → Spaltenvektor, „c = (8 9)“ → Zeilenvektor. Funktionswerte wie „U(7; 9)“ bleiben Text. */
const MX_Z = String.raw`[−-]?\d+(?:[.,]\d+)?(?:\/\d+)?|[a-zα-ω]`;
const MX_RE = new RegExp(String.raw`(^|\bdet|[^A-Za-zÄÖÜäöüß0-9_])\(\s*((?:${MX_Z})(?:[ \t]+(?:${MX_Z}))*(?:\s*;\s*(?:${MX_Z})(?:[ \t]+(?:${MX_Z}))*)*)\s*\)`, 'g');
function matrizen(t) {
  return t.replace(MX_RE, (m, vor, inn, off, str) => {
    const zeilen = inn.split(/\s*;\s*/).map(z => z.trim().split(/[ \t]+/));
    const spalten = zeilen[0].length, vorText = str.slice(Math.max(0, off - 12), off + vor.length);
    if (zeilen.some(z => z.length !== spalten)) return m;
    if (zeilen.length === 1 && vor !== 'det' && (spalten < 2 || !/[=·]\s*$/.test(vorText))) return m;           // Zeilenvektor nur nach „=“ oder „·“
    if (spalten === 1 && (zeilen.length < 2 || !/(=|·|und|für)\s*$/.test(vorText))) return m;   // Spaltenvektor nur nach „=“, „·“
    if (zeilen.every(z => z.every(x => /^[a-zα-ω]$/.test(x)))) return m;                         // nur Buchstaben: eher Text
    const tex = zeilen.map(z => z.map(x => x.replace(/^[−-]/, '-').replace(/,/g, '{,}').replace(/^(-?\d+)\/(\d+)$/, '\\tfrac{$1}{$2}')).join(' & ')).join(' \\\\ ');
    if (vor === 'det') return `\\(\\det\\begin{pmatrix} ${tex} \\end{pmatrix}\\)`;
    return `${vor}\\(\\begin{pmatrix} ${tex} \\end{pmatrix}\\)`;
  });
}
const BR_INLINE = /<\/?(?:sub|sup|i|em)>/g;
function brueche(html) {
  const tags = [];   // <sub>, <sup>, <i>, <em> gehören zur Formel: als Platzhalter durchreichen
  html = String(html).replace(BR_INLINE, m => String.fromCharCode(0xE000 + tags.push(m) - 1));
  return html.split(/(<[^>]+>)/).map(t => t.startsWith('<') ? t : brDivision(wurzeln(t)
    .replace(BR_INDEX, (m, v, a, b) => `${v}${a}\u0003${b.replace(/^\{|\}$/g, '')}\u0004`))
    .replace(BR_KURZ, (m, vor, a, b, off, str) => brWort(a) || brWort(b) || /^\d{3,}$/.test(a) || a === b || /^\d+$/.test(a) && /^\d{4}$/.test(b) || /(Folien?|Seiten?|S\.|Nr\.|SAP)\s*$/.test(str.slice(Math.max(0, off - 8), off + vor.length)) || /^\s*km\b/.test(str.slice(off + m.length)) ? m : vor + brSpan(a, b))
    .replace(/\u0001/g, '<span class="wz">').replace(/\u0002/g, '</span>').replace(/\u0003/g, '<sub>').replace(/\u0004/g, '</sub>')).join('').replace(/[\uE000-\uE0FF]/g, c => tags[c.charCodeAt(0) - 0xE000]);
}
/* Lernseiten-Text: wie schoen(), aber Schaubilder, Skripte, Eingaben und fertige Formeln bleiben unberührt */
const LERN_SCHUTZ = /(<(svg|script|style|textarea|pre|code|math|annotation)\b[\s\S]*?<\/\2>|<span class="katex[\s\S]*?<\/annotation>)/g;
function schoenLern(html) {
  if (!html) return html || '';
  return String(html).split(LERN_SCHUTZ).map((t, i) => i % 3 === 0 ? schoen(t) : i % 3 === 1 ? t : '').join('');
}
/* Rechner-Ausgaben der Schaubilder: Skripte schreiben Texte wie „(700 + 680) ÷ 2“ nach dem Rendern und bei jedem Regler-Zug neu.
   Der Wächter setzt solche Ausgaben wie auf Papier; nur „Blätter“ (Elemente ohne Knöpfe, Eingaben oder SVG darin). */
const FW_MUSTER = /÷|√\(|\b[A-Za-zΔσμ]{1,3}_[A-Za-z0-9]|\((?:[−-]?\d+[ \t]+)+[−-]?\d+;/;
const FW_INLINE = new Set(['B', 'I', 'EM', 'STRONG', 'SUB', 'SUP', 'SPAN', 'SMALL', 'BR']);
function fwSetze(el) {
  if (!el || el.nodeType !== 1 || el.closest('svg,script,style,textarea,.katex,button,select,label') || el.dataset.fwFertig === el.innerHTML) return;
  if ([...el.querySelectorAll('*')].some(k => !FW_INLINE.has(k.tagName) || k.classList.contains('katex'))) return;
  if (!FW_MUSTER.test(el.textContent)) return;
  const neu = schoen(el.innerHTML); if (neu !== el.innerHTML) el.innerHTML = neu;
  el.dataset.fwFertig = el.innerHTML;
}
function formelWaechter(root) {
  if (!root || root.fwBeob) return;
  const kandidaten = r => r.querySelectorAll('li,td,th,p,span,div,b,small,output');
  kandidaten(root).forEach(fwSetze);
  root.fwBeob = new MutationObserver(ms => {
    const ziel = new Set();
    for (const m of ms) { const t = m.type === 'characterData' ? m.target.parentElement : m.target; if (t && t.nodeType === 1) ziel.add(t); }
    for (const t of ziel) { if (t.closest('svg')) continue; fwSetze(t); }
  });
  root.fwBeob.observe(root, { childList: true, characterData: true, subtree: true });
}
function schoen(html) {
  if (html == null || html === '') return html || '';
  html = String(html).split(/(<[^>]+>|\\\([\s\S]+?\\\)|\\\[[\s\S]+?\\\])/).map((t, i) => i % 2 ? t : matrizen(t)).join('');
  const teile = String(html).split(/(\\\([\s\S]+?\\\)|\\\[[\s\S]+?\\\])/);
  return mathe(teile.map((t, i) => i % 2 ? t : brueche(t)).join(''));
}

/* ---------- Mathe-Eingabe: einfache Schreibweise → Baum → LaTeX-Vorschau und Zahlenwert ----------
   Erlaubt: Zahlen (Komma oder Punkt), Variablen (ein Buchstabe, auch x1 / x_1), + − · * / : ^ ( ), sqrt(), ln(), e, π, ∞, ² ³,
   Malpunkt darf fehlen (2x, 3(a+b), x y). */
const MF_FUNK = ['sqrt', 'wurzel', 'ln', 'log', 'exp', 'sin', 'cos'];
function mfTokens(s) {
  s = String(s).replace(/[−–]/g, '-').replace(/[·×*]/g, '*').replace(/:/g, '/').replace(/²/g, '^2').replace(/³/g, '^3').replace(/√/g, 'sqrt').replace(/\s+/g, ' ').trim();
  const t = []; let i = 0;
  while (i < s.length) {
    const c = s[i];
    if (c === ' ') { i++; continue; }
    if (/[0-9]/.test(c) || (c === ',' || c === '.') && /[0-9]/.test(s[i + 1] || '')) {
      let j = i; while (j < s.length && /[0-9.,]/.test(s[j])) j++;
      let z = s.slice(i, j); if (z.includes(',')) z = z.replace(/\.(?=\d{3}(\D|$))/g, '').replace(',', '.');
      t.push({ t: 'n', v: parseFloat(z), s: s.slice(i, j) }); i = j; continue; }
    if (/[a-zA-ZäöüÄÖÜπ∞λ]/.test(c)) {
      const f = MF_FUNK.find(f => s.startsWith(f, i) && !/[a-z]/i.test(s[i + f.length] || '(') || s.startsWith(f + '(', i));
      if (f) { t.push({ t: 'f', v: f === 'wurzel' ? 'sqrt' : f === 'log' ? 'ln' : f }); i += f.length; continue; }
      let v = c, j = i + 1;
      if (s[j] === '_' && /[0-9a-z]/i.test(s[j + 1] || '')) { v += '_' + s[j + 1]; j += 2; }
      else if (/[0-9]/.test(s[j] || '') && /[a-zA-Z]/.test(c) && !/[0-9]/.test(s[j + 1] || '') && (t.length === 0 || t[t.length - 1].t !== 'n')) { v += '_' + s[j]; j++; }   // x1 → x₁
      t.push({ t: 'v', v }); i = j; continue; }
    if ('+-*/^()'.includes(c)) { t.push({ t: c }); i++; continue; }
    throw new Error('Zeichen „' + c + '“ verstehe ich nicht');
  }
  return t;
}
function mfParse(s) {
  const t = mfTokens(s); let i = 0;
  const peek = () => t[i], nimm = typ => { if (!t[i] || t[i].t !== typ) throw new Error(typ === ')' ? 'Klammer fehlt' : 'Ausdruck unvollständig'); return t[i++]; };
  const startTerm = x => x && (x.t === 'n' || x.t === 'v' || x.t === 'f' || x.t === '(');
  function summe() { let a = produkt(); while (peek() && (peek().t === '+' || peek().t === '-')) { const o = t[i++].t; a = { o, a, b: produkt() }; } return a; }
  function produkt() {
    let a = vorz();
    for (;;) {
      const p = peek();
      if (p && (p.t === '*' || p.t === '/')) { i++; a = { o: p.t, a, b: vorz(), punkt: p.t === '*' }; continue; }
      if (startTerm(p)) { a = { o: '*', a, b: potenz() }; continue; }   // Malpunkt weggelassen
      return a;
    }
  }
  function vorz() { if (peek() && peek().t === '-') { i++; return { o: 'neg', a: vorz() }; } if (peek() && peek().t === '+') { i++; return vorz(); } return potenz(); }
  function potenz() { const b = basis(); if (peek() && peek().t === '^') { i++; return { o: '^', a: b, b: vorz() }; } return b; }
  function basis() {
    const x = peek(); if (!x) throw new Error('Ausdruck unvollständig');
    if (x.t === 'n') { i++; return { n: x.v, s: x.s }; }
    if (x.t === 'v') { i++; return { v: x.v }; }
    if (x.t === 'f') { i++; const arg = peek() && peek().t === '(' ? (i++, (() => { const e = summe(); nimm(')'); return e; })()) : potenz(); return { f: x.v, a: arg }; }
    if (x.t === '(') { i++; const e = summe(); nimm(')'); return { k: e }; }
    throw new Error('An dieser Stelle fehlt eine Zahl oder Variable');
  }
  const e = summe(); if (i < t.length) throw new Error(t[i].t === ')' ? 'Eine Klammer zu viel' : 'Ausdruck unvollständig'); return e;
}
function mfLatex(e) {
  const L = mfLatex, ohneK = x => x.k ? L(x.k) : L(x);
  if (e.n != null) return (e.s || String(e.n)).replace('.', '{,}').replace(/,(?!\})/, '{,}');
  if (e.v) return e.v === 'π' ? '\\pi' : e.v === '∞' ? '\\infty' : e.v === 'λ' ? '\\lambda' : e.v.replace(/_(\w)/, '_{$1}');
  if (e.k) return '\\left(' + L(e.k) + '\\right)';
  if (e.f) return e.f === 'sqrt' ? `\\sqrt{${ohneK(e.a)}}` : e.f === 'exp' ? `e^{${ohneK(e.a)}}` : `\\${e.f}\\left(${ohneK(e.a)}\\right)`;
  if (e.o === 'neg') return '-' + L(e.a);
  if (e.o === '/') return `\\frac{${ohneK(e.a)}}{${ohneK(e.b)}}`;
  if (e.o === '^') return `{${L(e.a)}}^{${ohneK(e.b)}}`;
  if (e.o === '*') return L(e.a) + (e.punkt || (e.b.n != null) || (e.a.n == null && !e.a.v) ? ' \\cdot ' : ' ') + L(e.b);
  return L(e.a) + (e.o === '+' ? ' + ' : ' - ') + L(e.b);
}
function mfWert(e, env) {
  const W = x => mfWert(x, env);
  if (e.n != null) return e.n;
  if (e.v) { if (e.v === 'e') return Math.E; if (e.v === 'π') return Math.PI; if (e.v === '∞') return Infinity; if (!(e.v in env)) throw new Error('unbekannt ' + e.v); return env[e.v]; }
  if (e.k) return W(e.k);
  if (e.f) { const a = W(e.a); return e.f === 'sqrt' ? Math.sqrt(a) : e.f === 'ln' ? Math.log(a) : e.f === 'exp' ? Math.exp(a) : e.f === 'sin' ? Math.sin(a) : Math.cos(a); }
  if (e.o === 'neg') return -W(e.a);
  const a = W(e.a), b = W(e.b);
  return e.o === '+' ? a + b : e.o === '-' ? a - b : e.o === '*' ? a * b : e.o === '/' ? a / b : Math.pow(a, b);
}
const mfVars = (e, s = new Set()) => { if (!e || typeof e !== 'object') return s; if (e.v && !['e', 'π', '∞'].includes(e.v)) s.add(e.v); for (const k of ['a', 'b', 'k']) if (e[k]) mfVars(e[k], s); return s; };
/* Sind zwei Ausdrücke gleich? An mehreren zufälligen Stellen auswerten. */
function mfGleich(eingabe, loesung, vars) {
  const a = mfParse(eingabe), b = mfParse(loesung), vs = [...new Set([...(vars || []), ...mfVars(a), ...mfVars(b)])];
  let gut = 0;
  for (let n = 0; n < 8; n++) {
    const env = Object.fromEntries(vs.map((v, j) => [v, 0.6 + ((n * 7 + j * 3) % 11) / 6 + Math.random() * 0.1]));
    const x = mfWert(a, env), y = mfWert(b, env);
    if (!isFinite(y)) continue;
    if (!isFinite(x) || Math.abs(x - y) > 1e-6 * Math.max(1, Math.abs(y))) return false;
    gut++;
  }
  return gut > 0;
}
/* Zahl aus einer Eingabe (auch 11/3, e^0,6, 1.152,38) */
function mfZahl(s) {
  s = String(s).replace(/€|%|kg|Stück|ME|GE|Jahre?/gi, '').trim(); if (!s) return NaN;
  if (/^[−-]?∞$|^[−-]?unendlich$/i.test(s)) return s.includes('-') || s.includes('−') ? -Infinity : Infinity;
  try { return mfWert(mfParse(s), {}); } catch (e) { return NaN; }
}

const MF_TASTEN = [['a/b', '()/()', 1], ['x²', '^2', 0], ['xⁿ', '^()', 2], ['√', 'sqrt()', 1], ['ln', 'ln()', 1], ['eˣ', 'e^()', 1], ['·', '·', 0], ['(', '(', 0], [')', ')', 0], ['∞', '∞', 0]];
function mfHTML(feld, id) {
  const vars = (feld.vars || []).filter(v => v.length <= 3);
  return `<div class="mf" data-mf="${id}"><div class="mf-zeile"><input class="mf-in" data-feld="${id}" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="${esc(feld.platz || 'z. B. h^2/j')}" aria-label="${esc(txt(feld.label || 'Antwort'))}">
    <button type="button" class="mf-tbtn" data-mftast="${id}" aria-label="Mathe-Tastatur" title="Mathe-Tastatur">⌨</button></div>
    <div class="mf-vor" aria-live="polite"></div>
    <div class="mf-tast" hidden>${MF_TASTEN.map(([n, ins, zur]) => `<button type="button" data-ins="${esc(ins)}" data-zur="${zur}">${n}</button>`).join('')}${vars.map(v => `<button type="button" data-ins="${esc(v)}" data-zur="0">${esc(v.replace(/_(\w)/, '$1'))}</button>`).join('')}</div></div>`;
}
document.addEventListener('input', e => {
  const inp = e.target.closest('.mf-in'), mf = inp && inp.closest('.mf'); if (!mf) return;
  const vor = mf.querySelector('.mf-vor'), v = inp.value.trim();
  if (!v) { vor.innerHTML = ''; return; }
  try { vor.innerHTML = katex.renderToString(mfLatex(mfParse(v)), { throwOnError: false }); vor.classList.remove('mf-fehler'); }
  catch (er) { vor.textContent = er.message; vor.classList.add('mf-fehler'); }
});
document.addEventListener('click', e => {
  const t = e.target.closest('[data-mftast]'); if (t) { const tast = t.closest('.mf').querySelector('.mf-tast'); tast.hidden = !tast.hidden; t.classList.toggle('on', !tast.hidden); return; }
  const k = e.target.closest('.mf-tast [data-ins]'); if (!k) return;
  e.preventDefault();
  const inp = k.closest('.mf').querySelector('.mf-in'), a = inp.selectionStart ?? inp.value.length, b = inp.selectionEnd ?? a, ins = k.dataset.ins;
  inp.value = inp.value.slice(0, a) + ins + inp.value.slice(b);
  const pos = a + ins.length - (+k.dataset.zur === 1 && ins.startsWith('()') ? ins.length - 1 : +k.dataset.zur ? 1 : 0);
  inp.focus(); inp.setSelectionRange(pos, pos); inp.dispatchEvent(new Event('input', { bubbles: true }));
});

/* ---------- Bogen ziehen: je Teil eine Variante, möglichst eine länger nicht gesehene ---------- */
function klausurZiehen(kl) {
  S.kbGesehen = S.kbGesehen || {};
  const fs = kl.teile.map(t => F[t[1]]).filter(f => f && f.klausur);
  const aufgaben = [];
  for (const f of fs) for (const A of f.klausur.aufgaben) {
    const teile = A.teile.filter(T => T.varianten.some(v => !v.unter || (TOP[f.id + '/' + v.unter] && !uAus(f.id + '/' + v.unter)))).map((T, j) => {
      const vs = T.varianten.filter(v => !v.unter || (TOP[f.id + '/' + v.unter] && !uAus(f.id + '/' + v.unter)));   // ausgeblendete Unterthemen nicht
      const alt = Math.min(...vs.map(v => S.kbGesehen[f.id + ':' + v.id] || 0));
      const frisch = vs.filter(v => (S.kbGesehen[f.id + ':' + v.id] || 0) === alt), vor = frisch.filter(v => v.vorrang);
      const v = pick(vor.length && Math.random() < .65 ? vor : frisch);   // Klausuraufgaben bevorzugt
      S.kbGesehen[f.id + ':' + v.id] = Date.now();   // schon beim Ziehen merken: die nächste Probeklausur nimmt andere Varianten
      return { buchst: 'abcdefghijklmnopqrstuvwxyz'[j], punkte: T.punkte, v, f };
    });
    if (!teile.length) continue;
    aufgaben.push({ nr: aufgaben.length + 1, titel: A.titel, punkte: teile.length === A.teile.length ? A.punkte : teile.reduce((s, T) => s + T.punkte, 0), intro: A.intro || '', f, teile });
  }
  save();
  return { kl, fs, aufgaben, antworten: {}, selbst: {}, abgegeben: false };
}
const kbSumme = B => B.aufgaben.reduce((s, A) => s + A.punkte, 0);

/* ---------- Zeichnen ---------- */
function kbDeckblatt(B, erreicht) {
  const db = Object.assign({}, ...B.fs.map(f => f.klausur.deckblatt || {})), kl = B.kl;
  const pruefer = [...new Set(B.fs.map(f => (f.klausur.deckblatt || {}).pruefer || f.person).filter(Boolean))].join(', ');
  const zeilen = B.aufgaben.map(A => `<tr><td>${A.nr}</td><td>${A.punkte}</td><td class="kb-grau">${erreicht ? zahl(erreicht[A.nr - 1], 1) : ''}</td></tr>`).join('');
  return `<div class="kb-deck"><div class="kb-dkopf"><b>Klausurdeckblatt</b><span>Probeklausur</span></div>
    <table class="kb-dt"><tr><td colspan="2"><small>Klausur / Fach</small>Probeklausur ${esc(kl.fachProbe ? kl.titel : db.fach || kl.titel || kl.kurz)}</td></tr>
      <tr><td><small>Prüfer/in</small>${esc(pruefer)}</td><td><small>Datum der echten Klausur</small>${datumKurz(kl.beginn)}</td></tr>
      <tr><td><small>Bearbeitungszeit / Minuten</small>${kl.minuten || kbSumme(B)}</td><td><small>Punkte</small>${kbSumme(B)}</td></tr>
      <tr><td colspan="2"><small>Zugelassene Hilfsmittel</small>${esc(db.hilfsmittel || 'keine')}</td></tr>
      ${db.bemerkungen ? `<tr><td colspan="2"><small>Bemerkungen</small>${db.bemerkungen}</td></tr>` : ''}</table>
    <table class="kb-pt"><thead><tr><th>Aufgabe Nr.</th><th>erreichbare Punkte</th><th>erreichte Punkte</th></tr></thead><tbody>${zeilen}
      <tr class="kb-summe"><td>Summe</td><td>${kbSumme(B)}</td><td class="kb-grau">${erreicht ? zahl(erreicht.reduce((s, x) => s + x, 0), 1) : ''}</td></tr></tbody></table></div>`;
}
function feldHTML(feld, id) {
  const lab = feld.label ? `<span class="kb-flab">${mathe(feld.label)}</span>` : '';
  if (feld.typ === 'ausdruck') return `<div class="kb-feld kb-feld-a">${lab}${mfHTML(feld, id)}</div>`;
  if (feld.typ === 'zahl') return `<div class="kb-feld">${lab}<span class="kb-zahl"><input class="mf-in kb-zin" data-feld="${id}" inputmode="decimal" autocomplete="off" placeholder="Ergebnis" aria-label="${esc(txt(feld.label || 'Ergebnis'))}">${feld.einheit ? `<em>${esc(feld.einheit)}</em>` : ''}</span></div>`;
  if (feld.typ === 'menge') return `<div class="kb-feld">${lab}<span class="kb-menge"><i>{</i><input class="kb-min" data-feld="${id}" autocomplete="off" placeholder="z. B. 3, 9" aria-label="${esc(txt(feld.label || 'Menge'))}"><i>}</i></span></div>`;
  if (feld.typ === 'rf') return `<div class="kb-feld kb-rf"><table class="kb-rft"><thead><tr><th>Aussage</th><th>richtig</th><th>falsch</th></tr></thead><tbody>${feld.aussagen.map((a, j) => `<tr><td>${a[0]}</td>${['1', '0'].map(w => `<td class="kb-rfz"><input type="radio" name="${id}:${j}" value="${w}" data-feld="${id}" data-j="${j}" aria-label="${w === '1' ? 'richtig' : 'falsch'}"></td>`).join('')}</tr>`).join('')}</tbody></table><small class="kb-rfh">${feld.abzug ? 'Je richtige Aussage ein Punkt, je falsche ein Punkt Abzug (nicht unter 0); unbeantwortet 0.' : feld.einzeln ? 'Punkte je richtig beantworteter Aussage.' : 'Punkte nur, wenn alle Aussagen des Blocks stimmen.'}</small></div>`;
  if (feld.typ === 'sc') return `<div class="kb-feld kb-sc">${lab}${feld.o.map((o, j) => `<label class="kb-sco"><input type="radio" name="${id}" value="${j}" data-feld="${id}" data-j="${j}"><b>${'abcd'[j]})</b><span>${mathe(o)}</span></label>`).join('')}</div>`;
  if (feld.typ === 'wort') return `<div class="kb-feld">${lab}<input class="kb-wort" data-feld="${id}" autocomplete="off" placeholder="Wort oder Begriff" aria-label="${esc(txt(feld.label || 'Lücke'))}"></div>`;
  if (feld.typ === 'matrix') { const [r, c] = [feld.loesung.length, feld.loesung[0].length];
    return `<div class="kb-feld">${lab}<span class="kb-mat" style="--c:${c}">${Array.from({ length: r * c }, (_, j) => `<input data-feld="${id}" data-j="${j}" inputmode="decimal" autocomplete="off" aria-label="Zeile ${Math.floor(j / c) + 1}, Spalte ${j % c + 1}">`).join('')}</span></div>`; }
  return `<div class="kb-feld kb-feld-t">${lab}<textarea data-feld="${id}" rows="${feld.zeilen || 4}" placeholder="Antwort in Stichworten oder ganzen Sätzen …"></textarea></div>`;
}
const rechnet = T => T.v.felder.some(f => ['zahl', 'ausdruck', 'matrix', 'menge'].includes(f.typ));
function kbAufgabeHTML(B, A) {
  return `<section class="kb-auf" id="kb-a${A.nr}">
    <header class="kb-ah"><b>Aufgabe ${A.nr} [${esc(A.titel)}]</b><b>[${A.punkte} Punkte]</b></header>
    ${A.intro ? `<div class="kb-intro">${schoen(A.intro)}</div>` : ''}
    <ol class="kb-tl">${A.teile.filter(T => T.v.text).map(T => `<li><span class="kb-bu">${T.buchst})</span><div class="kb-tt">${schoen(T.v.text)}</div><span class="kb-pk">[${T.punkte} Punkte]</span></li>`).join('')}</ol>
    <div class="kb-zu">${A.teile.map(T => { const key = A.nr + T.buchst;
      return `<div class="kb-zz" data-kbt="${key}"><div class="kb-zl"><small>Zu ${T.buchst})${T.v.text ? '' : ` · ${T.punkte} Punkte`}</small>${T.v.bild ? `<div class="kb-bild">${T.v.bild}</div>` : ''}
          ${rechnet(T) ? `<textarea class="kb-weg" data-weg="${key}" rows="3" placeholder="Formel und Lösungsweg (wie in der Klausur, Papier geht auch) …"></textarea>` : ''}
          ${T.v.felder.filter(f => f.typ !== 'text').length ? `<div class="kb-erg">${rechnet(T) ? '<small>Ergebnis</small>' : ''}${T.v.felder.map((f, j) => f.typ === 'text' ? '' : feldHTML(f, key + ':' + j)).join('')}</div>` : ''}
          ${T.v.felder.map((f, j) => f.typ === 'text' ? feldHTML(f, key + ':' + j) : '').join('')}
          <div class="kb-loes" hidden></div></div>
        <div class="kb-grau kb-pz" data-pz="${key}"></div></div>`; }).join('')}</div></section>`;
}
function klausurBogenHTML(B) {
  const teilKopf = (A, i) => B.fs.length > 1 && (i === 0 || B.aufgaben[i - 1].f !== A.f) ? `<h2 class="kb-teilh">Teil ${esc(A.f.name)} · ${B.aufgaben.filter(x => x.f === A.f).reduce((s, x) => s + x.punkte, 0)} Punkte</h2>` : '';
  return `<div class="kb">${kbDeckblatt(B)}${B.aufgaben.map((A, i) => teilKopf(A, i) + kbAufgabeHTML(B, A)).join('')}
    <div class="kb-ende"><button class="btn btn-main" data-kb="abgeben">Abgeben</button><small>Danach siehst du die Lösungen. Ergebnisse werden automatisch geprüft, Textantworten bewertest du selbst.</small></div></div>`;
}

/* ---------- Bewerten ---------- */
function feldWert(box, id) { return [...box.querySelectorAll(`[data-feld="${CSS.escape(id)}"]`)]; }
function pruefeFeld(feld, els) {
  const v = els.map(e => e.value.trim());
  if (feld.typ === 'text') return null;
  if (feld.typ === 'sc') { const x = els.find(e => e.checked); return !!x && +x.value === feld.r; }
  if (feld.typ !== 'rf' && !v.some(Boolean)) return false;
  try {
    if (feld.typ === 'zahl') { const x = mfZahl(v[0]), s = +feld.loesung; if (!isFinite(s)) return x === s; return Math.abs(x - s) <= (feld.tol != null ? feld.tol : Math.max(0.011, Math.abs(s) * 0.002)); }
    if (feld.typ === 'ausdruck') return [].concat(feld.loesung).some(l => mfGleich(v[0], l, feld.vars));
    if (feld.typ === 'menge') {
      if (!Array.isArray(feld.loesung)) return /nicht|n\.?\s*b|keine/i.test(v[0]);
      const ist = v[0].replace(/[{}]/g, '').split(/[;,\s]+/).map(x => x.trim().toLowerCase()).filter(Boolean);
      if (!feld.loesung.length) return /^(∅|leer|\{\s*\}|)$/i.test(v[0].trim()) || !ist.length;
      const soll = feld.loesung.map(x => String(x).toLowerCase());
      return ist.length === new Set(ist).size && ist.length === soll.length && soll.every(x => ist.includes(x));
    }
    if (feld.typ === 'rf') { const gew = feld.aussagen.map((a, j) => { const x = els.find(e => +e.dataset.j === j && e.checked); return x ? x.value === '1' : null; });
      if (feld.einzeln) { const n = gew.filter((g, j) => g === !!feld.aussagen[j][1]).length, f = feld.abzug ? gew.filter((g, j) => g !== null && g !== !!feld.aussagen[j][1]).length : 0, w = Math.max(0, n - f); return w === gew.length ? true : w / gew.length; }   // Punkte je Aussage (abzug: falsche Antwort kostet einen Punkt, nicht unter 0)
      return gew.every((g, j) => g === !!feld.aussagen[j][1]); }
    if (feld.typ === 'wort') { const n = s => norm(s).replace(/[^a-z0-9]/g, ''); return [].concat(feld.loesung).some(l => n(v[0]) === n(l) || (n(l).length > 5 && n(v[0]).includes(n(l)))); }
    if (feld.typ === 'matrix') { const soll = feld.loesung.flat(); return soll.every((s, j) => Math.abs(mfZahl(v[j]) - s) <= 0.011 + Math.abs(s) * 0.002); }
  } catch (e) { return false; }
  return false;
}
function kbAbgeben(el, B) {
  B.abgegeben = true; clearInterval(B.uhr);
  for (const A of B.aufgaben) for (const T of A.teile) {
    const key = A.nr + T.buchst, zz = el.querySelector(`[data-kbt="${key}"]`); T.auto = 0; T.selbstMax = 0;
    T.v.felder.forEach((f, j) => { const els = feldWert(zz, key + ':' + j), ok = pruefeFeld(f, els);
      els.forEach(e => { e.disabled = true; e.classList.toggle('kb-ok', ok === true); e.classList.toggle('kb-nein', ok === false); });
      if (ok === true) T.auto += f.p; else if (typeof ok === 'number') T.auto += Math.round(f.p * ok * 2) / 2; if (ok === null) T.selbstMax += f.p;
      if (f.typ === 'rf') zz.querySelectorAll(`[name^="${key}:${j}:"]`).forEach(r => { const z = +r.name.split(':').pop(), tr = r.closest('tr'); tr.classList.toggle('kb-rfja', (f.aussagen[z][1] ? '1' : '0') === (tr.querySelector('input:checked') || {}).value); tr.classList.toggle('kb-rfnein', (f.aussagen[z][1] ? '1' : '0') !== (tr.querySelector('input:checked') || {}).value); });
      if (f.typ === 'sc') els.forEach(e => e.closest('.kb-sco').classList.toggle('kb-scja', +e.value === f.r));
      if (ok === false && f.typ !== 'text') els[0].closest('.kb-feld').insertAdjacentHTML('beforeend', `<span class="kb-soll">richtig: ${mathe(sollText(f))}</span>`); });
    zz.querySelectorAll('textarea').forEach(t => t.readOnly = true);
    const lo = zz.querySelector('.kb-loes'); lo.hidden = false;
    lo.innerHTML = `<b class="kb-lh">Musterlösung</b><button class="q-melde" title="Fehler melden" aria-label="Fehler melden" data-melde="Probeklausur · ${esc(A.titel)} ${T.buchst}) · Variante ${esc(T.v.id)}">⚑</button><div class="kb-lt">${schoen(T.v.loesung || '')}</div>${T.selbstMax ? `<div class="kb-selbst" data-selbst="${key}"><span>Deine Textantwort: wie viele Punkte?</span>${Array.from({ length: T.selbstMax * 2 + 1 }, (_, n) => n / 2).map(n => `<button data-sp="${n}">${zahl(n, 1)}</button>`).join('')}</div>` : ''}`;
  }
  kbPunkteZeigen(el, B);
}
function sollText(f) {
  if (f.zeige) return f.zeige;
  if (f.typ === 'menge') return Array.isArray(f.loesung) ? (f.loesung.length ? '\\(\\{' + f.loesung.join(', ') + '\\}\\)' : '\\(\\emptyset\\)') : 'nicht bestimmbar';
  if (f.typ === 'rf') return f.aussagen.map(a => (a[1] ? 'richtig' : 'falsch')).join(' · ');
  if (f.typ === 'sc') return 'abcd'[f.r] + ') ' + f.o[f.r];
  if (f.typ === 'wort') return [].concat(f.loesung)[0];
  if (f.typ === 'matrix') return '\\(\\begin{pmatrix}' + f.loesung.map(r => r.map(x => zahl(x, 2)).join(' & ')).join(' \\\\ ') + '\\end{pmatrix}\\)';
  if (f.typ === 'ausdruck') { try { return '\\(' + mfLatex(mfParse([].concat(f.loesung)[0])) + '\\)'; } catch (e) { return [].concat(f.loesung)[0]; } }
  return zahl(+f.loesung, 2) + (f.einheit ? ' ' + f.einheit : '');
}
function kbPunkteZeigen(el, B) {
  let hat = 0, offen = 0; const proA = [];
  for (const A of B.aufgaben) { let a = 0;
    for (const T of A.teile) { const key = A.nr + T.buchst, s = B.selbst[key]; if (T.selbstMax && s == null) offen++;
      T.p = T.auto + (s || 0); a += T.p;
      const pz = el.querySelector(`[data-pz="${key}"]`); if (pz) pz.innerHTML = `<b>${zahl(T.p, 1)}</b><small>von ${T.punkte}</small>`; }
    proA.push(a); hat += a; }
  B.hat = hat; B.offen = offen; B.proA = proA;
  const summe = kbSumme(B), n = note(hat, summe), deck = el.querySelector('.kb-deck');
  if (deck) deck.outerHTML = kbDeckblatt(B, proA);
  const ende = el.querySelector('.kb-ende');
  ende.innerHTML = `<div class="kb-res"><span class="kb-note">${offen ? '…' : noteText(n)}</span><div><b>${zahl(hat, 1)} von ${summe} Punkten</b><small>${offen ? `Noch ${offen} ${offen === 1 ? 'Textantwort' : 'Textantworten'} selbst bewerten, dann steht die Note fest.` : `Note ${noteText(n)} · ${n > 4 ? 'nicht bestanden' : 'bestanden'}`}</small></div></div>
    ${offen ? `<button class="btn" data-kb="offen">Zur nächsten Selbstbewertung</button>` : B.gespeichert ? '<small>Gespeichert.</small>' : `<button class="btn btn-main" data-kb="speichern">Ergebnis speichern</button>`}
    <button class="btn" data-act="pr-neu">Neue Probeklausur</button>`;
  // Leiste oben (bleibt beim Scrollen stehen): Note, Punkte, Sprung zur nächsten Selbstbewertung
  let oben = el.querySelector('.kb-oben');
  if (!oben) { oben = document.createElement('div'); oben.className = 'kb-oben'; el.prepend(oben); }
  oben.innerHTML = `<span class="kb-oben-n">${offen ? '…' : noteText(n)}</span><span class="kb-oben-t"><b>${zahl(hat, 1)} / ${summe} P</b><small>${offen ? `${offen} offen` : n > 4 ? 'nicht bestanden' : 'bestanden'}</small></span>
    ${offen ? `<button class="btn" data-kb="offen">Selbst bewerten ↓</button>` : B.gespeichert ? '<small>gespeichert</small>' : `<button class="btn" data-kb="speichern">Speichern</button>`}`;
}
function kbSpeichern(B) {
  const items = [];
  for (const A of B.aufgaben) for (const T of A.teile) {
    const key = T.f.id + '/' + (T.v.unter || ''), x = TOP[key]; if (!x) continue;
    items.push({ f: x.f, k: x.k, t: x.t, key, p: T.p, max: T.punkte });
    S.kbGesehen[T.f.id + ':' + T.v.id] = Date.now();
  }
  verbucheProbe(B.kl, items, B.hat, kbSumme(B)); B.gespeichert = true;
}

/* ---------- Einhängen ---------- */
function klausurBogen(el, B, opt = {}) {
  el.innerHTML = klausurBogenHTML(B);
  if (opt.minuten) {
    const ende = Date.now() + opt.minuten * 60000, leiste = document.createElement('div');
    leiste.className = 'kb-leiste'; el.prepend(leiste);
    const tick = () => { const r = Math.max(0, Math.round((ende - Date.now()) / 1000));
      leiste.innerHTML = B.abgegeben ? '' : `<span>${r ? `noch <b>${Math.floor(r / 60)}:${String(r % 60).padStart(2, '0')}</b> min` : '<b>Zeit ist um</b> – jetzt abgeben'}</span><button class="btn" data-kb="abgeben">Abgeben</button>`;
      if (B.abgegeben) clearInterval(B.uhr); };
    tick(); B.uhr = setInterval(tick, 1000);
  }
  el.onclick = e => {
    const b = e.target.closest('[data-kb]');
    if (b && b.dataset.kb === 'abgeben' && !B.abgegeben) { kbAbgeben(el, B); el.querySelector('.kb-leiste')?.remove(); (el.querySelector('.kb-selbst') || el.querySelector('.kb-ende')).scrollIntoView({ behavior: 'smooth', block: 'center' }); return; }
    if (b && b.dataset.kb === 'offen') { const s = [...el.querySelectorAll('.kb-selbst')].find(x => B.selbst[x.dataset.selbst] == null); s && s.scrollIntoView({ behavior: 'smooth', block: 'center' }); return; }
    if (b && b.dataset.kb === 'speichern') { kbSpeichern(B); kbPunkteZeigen(el, B); hinweis('Ergebnis gespeichert. Der Stand der Oberthemen ist aktualisiert.'); return; }
    const sp = e.target.closest('[data-sp]');
    if (sp && !B.gespeichert) { const box = sp.closest('[data-selbst]'); B.selbst[box.dataset.selbst] = +sp.dataset.sp;
      box.querySelectorAll('[data-sp]').forEach(x => x.classList.toggle('on', x === sp)); kbPunkteZeigen(el, B);
      const n = [...el.querySelectorAll('.kb-selbst')].find(x => B.selbst[x.dataset.selbst] == null); if (n) n.scrollIntoView({ behavior: 'smooth', block: 'center' }); }
  };
}
