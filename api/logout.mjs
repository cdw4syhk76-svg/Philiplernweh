/* POST /api/logout  {geraet?}  meldet dieses (oder ein anderes eigenes) Gerät ab. */
import { json, sb, q, sitzung, loescheCookie, lies } from './_lib.mjs';

export async function POST(req) {
  const s = await sitzung(req);
  if (!s) return json({ ok: true }, 200, { 'set-cookie': loescheCookie() });
  const b = await lies(req), ziel = String(b.geraet || s.g);
  try { await sb(`geraete?code=eq.${q(s.c)}&geraet=eq.${q(ziel)}`, { method: 'DELETE' }); } catch (e) { console.error(e); }
  return ziel === s.g ? json({ ok: true }, 200, { 'set-cookie': loescheCookie() }) : json({ ok: true });
}
