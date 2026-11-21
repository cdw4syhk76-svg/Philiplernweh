/* Vercel-Middleware: Ohne gültiges Anmelde-Cookie gibt es nur die Anmeldeseite (und die Verwaltungsseite).
   So sind alle Inhalte (daten/*.js, Skripte) erst nach Eingabe eines Codes erreichbar.
   Bewusst ohne Importe (läuft in der Edge-Umgebung); Signatur wie signiere() in api/_lib.mjs. */

export const config = { matcher: ['/((?!api/|login\\.html|admin\\.html|favicon\\.ico).*)'] };

function unb64(s) { return Uint8Array.from(atob(s.replace(/-/g, '+').replace(/_/g, '/')), c => c.charCodeAt(0)); }

async function signiertOk(request, name) {
  const m = (request.headers.get('cookie') || '').match(new RegExp('(?:^|;\\s*)' + name + '=([^;]+)'));
  if (!m) return null;
  const [teil, sig] = decodeURIComponent(m[1]).split('.');
  const geheim = (typeof process !== 'undefined' && process.env && process.env.SITZUNG_GEHEIMNIS) || '';
  if (!teil || !sig || geheim.length < 20) return null;
  const key = await crypto.subtle.importKey('raw', new TextEncoder().encode(geheim), { name: 'HMAC', hash: 'SHA-256' }, false, ['verify']);
  if (!await crypto.subtle.verify('HMAC', key, unb64(sig), new TextEncoder().encode(teil))) return null;
  try { return JSON.parse(new TextDecoder().decode(unb64(teil))); } catch (e) { return {}; }
}
/* Gültig: Anmelde-Cookie eines Codes – oder das Geist-Cookie aus dem Admin-Bereich (nur ansehen, läuft nach 2 Stunden ab) */
async function gueltig(request) {
  if (await signiertOk(request, 'lt_sitzung')) return true;
  const g = await signiertOk(request, 'lt_geist');
  return !!(g && g.geist && g.bis > Date.now());
}

export default async function middleware(request) {
  // Login nur, wenn in Vercel die Umgebungsvariable LOGIN=an gesetzt ist; sonst ist die Website offen (ohne Codes).
  if (((typeof process !== 'undefined' && process.env && process.env.LOGIN) || '') !== 'an') return;
  let ok = false;
  try { ok = await gueltig(request); } catch (e) { ok = false; }
  if (ok) return;   // weiter zur gewünschten Datei
  return new Response(null, { status: 302, headers: { location: new URL('/login.html', request.url).toString(), 'cache-control': 'no-store' } });
}
