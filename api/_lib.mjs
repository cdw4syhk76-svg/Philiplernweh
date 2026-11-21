/* Gemeinsame Helfer für die Online-Version (Vercel-Funktionen + Middleware).
   Umgebungsvariablen (in Vercel eintragen, nie ins Repo):
     SUPABASE_URL           https://xxxx.supabase.co
     SUPABASE_SERVICE_KEY   „service_role“-Schlüssel (geheim, nur auf dem Server)
     SITZUNG_GEHEIMNIS      langer Zufallstext zum Signieren der Anmelde-Cookies
     ADMIN_PASSWORT         Passwort für /admin.html (Codes erzeugen und verwalten) */

export const MAX_GERAETE = 3;
export const COOKIE = 'lt_sitzung';
const JAHR = 365 * 24 * 3600;
const env = k => ((globalThis.process && process.env[k]) || '').trim();

/* ---------- Antworten ---------- */
export const json = (daten, status = 200, kopf = {}) =>
  new Response(JSON.stringify(daten), { status, headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store', ...kopf } });

/* ---------- Codes: 10 Zeichen ohne verwechselbare (0/O, 1/I/L), angezeigt als XXXXX-XXXXX ---------- */
const ZEICHEN = 'ABCDEFGHJKMNPQRSTUVWXYZ23456789';
export const normCode = s => String(s || '').toUpperCase().replace(/[^A-Z0-9]/g, '');
export const zeigeCode = c => c.slice(0, 5) + '-' + c.slice(5);
export function neuerCode() {
  const b = crypto.getRandomValues(new Uint8Array(10));
  return Array.from(b, x => ZEICHEN[x % ZEICHEN.length]).join('');   // 31^10 ≈ 8·10^14 Möglichkeiten
}
export const gueltigesFormat = c => /^[A-Z0-9]{10}$/.test(c);

/* ---------- Sitzungs-Cookie: base64url(JSON).Signatur (HMAC-SHA256) ---------- */
const b64 = buf => btoa(String.fromCharCode(...new Uint8Array(buf))).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
const unb64 = s => Uint8Array.from(atob(s.replace(/-/g, '+').replace(/_/g, '/')), c => c.charCodeAt(0));
async function schluessel() {
  const g = env('SITZUNG_GEHEIMNIS');
  if (g.length < 20) throw new Error('SITZUNG_GEHEIMNIS fehlt oder ist zu kurz');
  return crypto.subtle.importKey('raw', new TextEncoder().encode(g), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign', 'verify']);
}
export async function signiere(inhalt) {
  const teil = b64(new TextEncoder().encode(JSON.stringify(inhalt)));
  const sig = await crypto.subtle.sign('HMAC', await schluessel(), new TextEncoder().encode(teil));
  return teil + '.' + b64(sig);
}
export async function pruefe(token) {
  try {
    const [teil, sig] = String(token || '').split('.');
    if (!teil || !sig) return null;
    const ok = await crypto.subtle.verify('HMAC', await schluessel(), unb64(sig), new TextEncoder().encode(teil));
    if (!ok) return null;
    const x = JSON.parse(new TextDecoder().decode(unb64(teil)));
    return x && x.c && x.g ? x : null;
  } catch (e) { return null; }
}
export function leseCookie(req, name = COOKIE) {
  const m = (req.headers.get('cookie') || '').match(new RegExp('(?:^|;\\s*)' + name + '=([^;]+)'));
  return m ? decodeURIComponent(m[1]) : '';
}
export const setzeCookie = wert => `${COOKIE}=${encodeURIComponent(wert)}; Path=/; Max-Age=${JAHR}; HttpOnly; Secure; SameSite=Lax`;
export const loescheCookie = () => `${COOKIE}=; Path=/; Max-Age=0; HttpOnly; Secure; SameSite=Lax`;
export async function sitzung(req) { return pruefe(leseCookie(req)); }

/* Projekt-Adresse aus dem, was eingetragen wurde: https://xxxx.supabase.co, auch mit /rest/v1/… dahinter
   oder als Dashboard-Link (supabase.com/dashboard/project/xxxx) */
export function supabaseUrl() {
  const v = env('SUPABASE_URL');
  const d = v.match(/supabase\.com\/dashboard\/project\/([a-z0-9]+)/i);
  if (d) return `https://${d[1]}.supabase.co`;
  try { return new URL(/^https?:\/\//.test(v) ? v : 'https://' + v).origin; } catch (e) { return ''; }
}

/* ---------- Supabase (PostgREST) mit dem Service-Schlüssel; alle Tabellen haben RLS ohne Regeln ---------- */
export async function sb(pfad, { method = 'GET', body, prefer } = {}) {
  const url = supabaseUrl(), key = env('SUPABASE_SERVICE_KEY');
  if (!url || !key) throw new Error('SUPABASE_URL oder SUPABASE_SERVICE_KEY fehlt');
  const r = await fetch(`${url}/rest/v1/${pfad}`, {
    method, body: body === undefined ? undefined : JSON.stringify(body),
    headers: { apikey: key, ...(key.startsWith('eyJ') ? { authorization: `Bearer ${key}` } : {}), 'content-type': 'application/json', ...(prefer ? { prefer } : {}) },   // neue Schlüssel (sb_secret_…) nur im apikey-Kopf
  });
  const text = await r.text();
  if (!r.ok) throw new Error(`Supabase ${method} ${pfad.split('?')[0]}: ${r.status} ${text.slice(0, 200)}`);
  return text ? JSON.parse(text) : null;
}
export const q = encodeURIComponent;

/* ---------- Lernstand zusammenführen: Patch {pfad: wert|null}, Pfad „abschnitt“ oder „abschnitt/schlüssel“ ---------- */
export function wendeAn(daten, patch) {
  const d = daten && typeof daten === 'object' ? daten : {};
  for (const [pfad, wert] of Object.entries(patch || {})) {
    const i = pfad.indexOf('/');
    if (i < 0) { if (wert === null) delete d[pfad]; else d[pfad] = wert; continue; }
    const a = pfad.slice(0, i), k = pfad.slice(i + 1);
    if (!d[a] || typeof d[a] !== 'object' || Array.isArray(d[a])) d[a] = {};
    if (wert === null) delete d[a][k]; else d[a][k] = wert;
  }
  return d;
}

export async function lies(req) { try { return await req.json(); } catch (e) { return {}; } }
