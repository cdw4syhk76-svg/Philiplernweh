/* POST /api/login  {code, geraet, name, entfernen?}
   Prüft den Code, meldet dieses Gerät an (höchstens MAX_GERAETE je Code) und setzt das Sitzungs-Cookie.
   Sind schon alle Plätze belegt, kommt die Geräteliste zurück; mit „entfernen“ wird ein altes Gerät abgemeldet. */
import { json, normCode, gueltigesFormat, sb, q, signiere, setzeCookie, MAX_GERAETE, lies } from './_lib.mjs';

export async function POST(req) {
  const b = await lies(req);
  const code = normCode(b.code), geraet = String(b.geraet || '').slice(0, 64), name = String(b.name || 'Gerät').slice(0, 60);
  if (!gueltigesFormat(code)) return json({ fehler: 'format', text: 'Der Code hat 10 Zeichen, z. B. ABCDE-FGH23.' }, 400);
  if (!/^[a-z0-9-]{8,64}$/i.test(geraet)) return json({ fehler: 'geraet', text: 'Gerätekennung fehlt. Bitte Seite neu laden.' }, 400);
  try {
    const [c] = await sb(`codes?code=eq.${q(code)}&select=code,gesperrt`);
    if (!c) { await new Promise(r => setTimeout(r, 600)); return json({ fehler: 'unbekannt', text: 'Diesen Code gibt es nicht. Bitte genau abtippen.' }, 401); }
    if (c.gesperrt) return json({ fehler: 'gesperrt', text: 'Dieser Code ist gesperrt.' }, 403);
    if (b.entfernen) await sb(`geraete?code=eq.${q(code)}&geraet=eq.${q(String(b.entfernen))}`, { method: 'DELETE' });
    const liste = await sb(`geraete?code=eq.${q(code)}&select=geraet,name,zuletzt&order=zuletzt.desc`);
    const jetzt = new Date().toISOString();
    if (!liste.some(g => g.geraet === geraet)) {
      if (liste.length >= MAX_GERAETE)
        return json({ fehler: 'voll', text: `Dieser Code ist schon auf ${MAX_GERAETE} Geräten angemeldet. Melde eins davon ab, um hier weiterzumachen.`, geraete: liste }, 409);
      await sb('geraete', { method: 'POST', body: { code, geraet, name, zuletzt: jetzt } });
    } else await sb(`geraete?code=eq.${q(code)}&geraet=eq.${q(geraet)}`, { method: 'PATCH', body: { name, zuletzt: jetzt } });
    const token = await signiere({ c: code, g: geraet, t: Date.now() });
    return json({ ok: true }, 200, { 'set-cookie': setzeCookie(token) });
  } catch (e) {
    console.error(e);
    return json({ fehler: 'server', text: 'Anmeldung gerade nicht möglich. Bitte später noch einmal.' }, 500);
  }
}
