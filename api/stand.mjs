/* GET /api/stand          → {daten, version, code, geraete, name}
   PUT /api/stand {patch}  → führt die Änderungen in den gespeicherten Lernstand ein → {daten, version}
   Gleichzeitige Änderungen von zwei Geräten: Versionsprüfung, bei Kollision neu lesen und erneut anwenden. */
import { json, sb, q, sitzung, wendeAn, lies, zeigeCode, loescheCookie } from './_lib.mjs';

async function angemeldet(req) {
  const s = await sitzung(req);
  if (!s) return null;
  const [g] = await sb(`geraete?code=eq.${q(s.c)}&geraet=eq.${q(s.g)}&select=geraet`);
  const [c] = await sb(`codes?code=eq.${q(s.c)}&select=gesperrt`);
  return g && c && !c.gesperrt ? s : null;
}
const raus = () => json({ fehler: 'abgemeldet' }, 401, { 'set-cookie': loescheCookie() });

async function zeile(code) {
  const [z] = await sb(`lernstand?code=eq.${q(code)}&select=daten,version`);
  return z || { daten: {}, version: 0, neu: true };
}

export async function GET(req) {
  try {
    const s = await angemeldet(req); if (!s) return raus();
    const z = await zeile(s.c);
    sb(`geraete?code=eq.${q(s.c)}&geraet=eq.${q(s.g)}`, { method: 'PATCH', body: { zuletzt: new Date().toISOString() } }).catch(() => { });
    const geraete = await sb(`geraete?code=eq.${q(s.c)}&select=geraet,name,zuletzt&order=zuletzt.desc`);
    const [c] = await sb(`codes?code=eq.${q(s.c)}&select=notiz`).catch(() => []);   // Name aus dem Admin-Bereich (Notiz zum Code)
    return json({ daten: z.daten || {}, version: z.version, code: zeigeCode(s.c), geraet: s.g, geraete, name: ((c && c.notiz) || '').trim().slice(0, 60) });
  } catch (e) { console.error(e); return json({ fehler: 'server' }, 500); }
}

export async function PUT(req) {
  try {
    const s = await angemeldet(req); if (!s) return raus();
    const { patch } = await lies(req);
    if (!patch || typeof patch !== 'object') return json({ fehler: 'patch' }, 400);
    if (JSON.stringify(patch).length > 2e6) return json({ fehler: 'zu-gross' }, 413);
    for (let versuch = 0; versuch < 5; versuch++) {
      const z = await zeile(s.c);
      const daten = wendeAn(z.daten, patch), version = z.version + 1, geaendert = new Date().toISOString();
      if (z.neu) {
        const r = await sb('lernstand?on_conflict=code', { method: 'POST', body: { code: s.c, daten, version, geaendert }, prefer: 'return=representation,resolution=ignore-duplicates' });
        if (r && r.length) return json({ daten, version });
      } else {
        const r = await sb(`lernstand?code=eq.${q(s.c)}&version=eq.${z.version}`, { method: 'PATCH', body: { daten, version, geaendert }, prefer: 'return=representation' });
        if (r && r.length) return json({ daten, version });
      }
    }
    return json({ fehler: 'kollision' }, 409);
  } catch (e) { console.error(e); return json({ fehler: 'server' }, 500); }
}
