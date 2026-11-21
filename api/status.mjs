/* GET /api/status – Selbsttest der Einrichtung (zeigt nur, OB etwas eingetragen ist, nie die Werte). */
import { json, sb, supabaseUrl } from './_lib.mjs';

export async function GET() {
  const e = k => ((globalThis.process && process.env[k]) || '').trim();
  const url = e('SUPABASE_URL'), key = e('SUPABASE_SERVICE_KEY');
  const r = {
    SUPABASE_URL: url ? (/^https:\/\/[a-z0-9-]+\.supabase\.co\/?$/.test(url) ? 'ok' : 'ok (verwendet: ' + supabaseUrl() + ')') : 'fehlt',
    SUPABASE_SERVICE_KEY: key ? (key.startsWith('sb_publishable') ? 'falscher Schlüssel (publishable statt secret)' : 'ok') : 'fehlt',
    SITZUNG_GEHEIMNIS: !e('SITZUNG_GEHEIMNIS') ? 'fehlt' : e('SITZUNG_GEHEIMNIS').length < 20 ? 'zu kurz (mind. 20 Zeichen)' : 'ok',
    ADMIN_PASSWORT: !e('ADMIN_PASSWORT') ? 'fehlt' : e('ADMIN_PASSWORT').length < 10 ? 'zu kurz (mind. 10 Zeichen)' : 'ok',
    datenbank: 'nicht geprüft',
  };
  if (url && key) {
    try { await sb('codes?select=code&limit=1'); r.datenbank = 'ok'; }
    catch (x) { r.datenbank = 'Fehler: ' + String(x.message || x).slice(0, 160); }
  }
  return json(r);
}
