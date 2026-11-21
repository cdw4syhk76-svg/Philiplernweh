/* POST /api/admin  {passwort, aktion, ...}   nur für den Betreiber (ADMIN_PASSWORT)
   aktion: liste · auswertung (mit Namen) · geist {nr} (Lernstand einer Person nur ansehen) · erzeugen {anzahl, notiz} · notiz {code, notiz} · sperren {code, gesperrt} · geraete-weg {code} */
import { json, sb, q, normCode, neuerCode, zeigeCode, lies, signiere } from './_lib.mjs';
import { auswerten, geistDaten } from './_auswertung.mjs';

function gleich(a, b) {   // Vergleich ohne frühes Abbrechen
  a = String(a); b = String(b); let d = a.length ^ b.length;
  for (let i = 0; i < Math.max(a.length, b.length); i++) d |= (a.charCodeAt(i) || 0) ^ (b.charCodeAt(i) || 0);
  return d === 0;
}

export async function POST(req) {
  const b = await lies(req), pw = ((globalThis.process && process.env.ADMIN_PASSWORT) || '').trim();
  if (pw.length < 10) return json({ fehler: 'einrichtung', text: 'ADMIN_PASSWORT ist in Vercel nicht eingetragen oder kürzer als 10 Zeichen (Prüfen: /api/status).' }, 500);
  if (!gleich(String(b.passwort || '').trim(), pw)) { await new Promise(r => setTimeout(r, 800)); return json({ fehler: 'passwort' }, 401); }
  try {
    if (b.aktion === 'erzeugen') {
      const n = Math.min(Math.max(+b.anzahl || 1, 1), 100), notiz = String(b.notiz || '').slice(0, 200);
      const zeilen = Array.from({ length: n }, () => ({ code: neuerCode(), notiz }));
      await sb('codes', { method: 'POST', body: zeilen });
      return json({ codes: zeilen.map(z => zeigeCode(z.code)) });
    }
    if (b.aktion === 'auswertung') {
      const codes = await sb('codes?select=code,erstellt,gesperrt,notiz');
      const staende = await sb('lernstand?select=code,daten,geaendert');
      const geraete = await sb('geraete?select=code,zuletzt').catch(() => []);
      return json(auswerten(codes, staende, geraete));
    }
    if (b.aktion === 'geist') {   // Lernstand von „Person nr“ zum Ansehen + Cookie, das 2 Stunden die App öffnet (nur lesen, kein Konto)
      const codes = await sb('codes?select=code,erstellt,notiz');
      const code = geistDaten(codes, +b.nr); if (!code) return json({ fehler: 'person' }, 404);
      const [z] = await sb(`lernstand?code=eq.${q(code)}&select=daten`);
      const bis = Date.now() + 2 * 3600e3, cookie = await signiere({ geist: 1, bis });
      const d = z ? z.daten : {}, c = codes.find(x => x.code === code) || {};
      const person = String((d && d.einst && d.einst.name) || '').trim() || String(c.notiz || '').trim() || 'Person ' + (+b.nr);
      return json({ person, daten: d }, 200,
        { 'set-cookie': `lt_geist=${encodeURIComponent(cookie)}; Path=/; Max-Age=7200; HttpOnly; Secure; SameSite=Lax` });
    }
    const code = normCode(b.code);
    if (b.aktion === 'notiz') { await sb(`codes?code=eq.${q(code)}`, { method: 'PATCH', body: { notiz: String(b.notiz || '').slice(0, 200) } }); return json({ ok: true }); }
    if (b.aktion === 'sperren') { await sb(`codes?code=eq.${q(code)}`, { method: 'PATCH', body: { gesperrt: !!b.gesperrt } }); return json({ ok: true }); }
    if (b.aktion === 'geraete-weg') { await sb(`geraete?code=eq.${q(code)}`, { method: 'DELETE' }); return json({ ok: true }); }
    const codes = await sb('codes?select=code,notiz,gesperrt,erstellt&order=erstellt.desc');
    const geraete = await sb('geraete?select=code,name,zuletzt');
    const staende = await sb('lernstand?select=code,geaendert');
    const g = {}, st = {};
    for (const x of geraete) (g[x.code] = g[x.code] || []).push(x);
    for (const x of staende) st[x.code] = x.geaendert;
    return json({ codes: codes.map(c => ({ ...c, anzeige: zeigeCode(c.code), geraete: g[c.code] || [], geaendert: st[c.code] || null })) });
  } catch (e) { console.error(e); return json({ fehler: 'server', text: String(e.message || e) }, 500); }
}
