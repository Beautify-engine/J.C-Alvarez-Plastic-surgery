/* ============================================================================
   Spec-period access gate.

   Called first from src/worker/index.js, before the consultation route and
   before env.ASSETS. This site deploys as a Worker, not as Pages, so a
   functions/_middleware.js would never execute — that was checked the hard way.

   CLAUDE.md §3: this deployment carries 192 real before-and-after photographs of
   his patients, and the engagement is unsigned. Their consent covers his own
   channels, not a third party republishing them somewhere new. So the preview is
   not allowed to be publicly reachable, and noindex does not achieve that —
   noindex asks search engines not to list the URL. It says nothing to a person
   who has the URL.

   This runs at the edge on EVERY request, before any asset is served, which is
   the part that matters. A password box drawn in JavaScript on the home page
   would leave /procedimientos/rinoplastia and /img/cases/tummy-tuck-01.jpg
   wide open to anyone who typed them.

   One prompt, then a cookie. He enters the password once and browses the whole
   site for SESSION_DAYS.

   SETUP — Cloudflare dashboard → the Worker → Settings → Variables and Secrets:
     SITE_PASSWORD   required, added as a SECRET (encrypted), not a plaintext
                     variable. A plaintext value is readable by anyone with
                     dashboard access and shows in the UI.

   If SITE_PASSWORD is unset the site refuses to serve rather than falling open.
   That is deliberate: a forgotten variable must not publish patient photographs.

   ON LAUNCH DAY, once he has signed and the gallery is cleared for public
   display, delete this file and its two lines in src/worker/index.js, together
   with the noindex header in config/es/_headers and config/es/robots.txt. All
   three exist for the same reason and end together.
   ========================================================================= */

const COOKIE = "jca_preview";
const SESSION_DAYS = 30;

/* HMAC over the expiry, keyed on the password itself. A visitor cannot forge a
   cookie without knowing the password, and changing the password invalidates
   every session that was issued under the old one — which is how you revoke
   someone you have shared it with. */
async function sign(value, secret) {
  const key = await crypto.subtle.importKey(
    "raw", new TextEncoder().encode(secret),
    { name: "HMAC", hash: "SHA-256" }, false, ["sign"]
  );
  const mac = await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(value));
  return [...new Uint8Array(mac)].map(b => b.toString(16).padStart(2, "0")).join("");
}

/* Length-independent comparison. The strings here are hex digests of fixed
   length, but comparing them with === leaks position-of-first-difference through
   timing, and there is no reason to hand that away. */
function safeEqual(a, b) {
  if (typeof a !== "string" || typeof b !== "string" || a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

async function hasValidSession(request, secret) {
  const raw = request.headers.get("Cookie") || "";
  const hit = raw.split(/;\s*/).find(c => c.startsWith(COOKIE + "="));
  if (!hit) return false;
  const [exp, mac] = decodeURIComponent(hit.slice(COOKIE.length + 1)).split(".");
  if (!exp || !mac) return false;
  if (Number(exp) < Date.now()) return false;
  return safeEqual(mac, await sign(exp, secret));
}

function page({ error = false, missing = false } = {}) {
  /* One person will ever read this screen: him. Named at the top so it is
     obviously his, then a plain instruction and nothing else in the way.

     The one line that stays is why it is locked, because that reason is worth
     more than any sentence about care: his patients' photographs are already
     behind a password before he has signed anything. */
  const body = missing
    ? `<h1>Sitio no configurado</h1>
       <p class="n">Falta la variable de entorno <code>SITE_PASSWORD</code>. El sitio no
       se sirve sin ella, a propósito: contiene fotografías de pacientes.</p>`
    : `<p class="k">Para el Dr. Julio Clavijo Alvarez</p>
       <h1>Introduzca su contraseña para ver el sitio.</h1>
       <p class="n">Lleva contraseña porque incluye fotografías de sus pacientes.</p>
       <form method="POST">
         <label for="p">Contraseña</label>
         <input id="p" name="password" type="password" autocomplete="current-password"
                autofocus required aria-describedby="${error ? "err" : "hint"}">
         ${error ? '<p class="e" id="err" role="alert">Contraseña incorrecta.</p>'
                 : '<p class="h" id="hint">Se la pedimos una sola vez en este dispositivo.</p>'}
         <button type="submit">Ver el sitio <span aria-hidden="true">&rarr;</span></button>
       </form>`;

  /* Self-contained: no stylesheet, no font, no image. The gate must not depend on
     an asset the gate itself is blocking. */
  return `<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Una propuesta para el Dr. Julio Clavijo Alvarez</title>
<style>
  :root{--ink:#16232a;--paper:#f7f6f3;--accent:#35606f;--muted:#5b6f77;--line:#d6dfe2}
  *{box-sizing:border-box}
  body{margin:0;min-height:100vh;display:grid;place-items:center;padding:1.5rem;
    background:var(--paper);color:var(--ink);
    font:400 16px/1.55 ui-sans-serif,system-ui,-apple-system,"Helvetica Neue",Arial,sans-serif}
  main{width:100%;max-width:29rem}
  .k{margin:0 0 .75rem;font-size:.75rem;letter-spacing:.1em;text-transform:uppercase;
    color:var(--accent)}
  h1{font:400 1.9rem/1.18 ui-serif,Georgia,"Times New Roman",serif;margin:0 0 .75rem;
    letter-spacing:-.01em}
  .n{color:var(--muted);margin:0 0 2rem;max-width:24rem}
  label{display:block;font-size:.75rem;letter-spacing:.08em;text-transform:uppercase;
    color:var(--muted);margin-bottom:.4rem}
  input{width:100%;padding:.8rem .9rem;font-size:1rem;color:var(--ink);
    background:#fff;border:1px solid var(--line);border-radius:0}
  input:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
  .h,.e{font-size:.8125rem;margin:.5rem 0 0}
  .h{color:var(--muted)}
  .e{color:#8c2f2f;font-weight:500}
  button{margin-top:1.25rem;width:100%;padding:.85rem 1rem;border:0;cursor:pointer;
    background:var(--accent);color:var(--paper);font-size:.8125rem;font-weight:500;
    letter-spacing:.08em;text-transform:uppercase}
  button{display:flex;align-items:center;justify-content:center;gap:.6em}
  button span{transition:transform var(--m,180ms) ease}
  button:hover{background:var(--ink)}
  button:hover span{transform:translateX(3px)}
  @media(prefers-reduced-motion:reduce){button span{transition:none}
    button:hover span{transform:none}}
  button:focus-visible{outline:2px solid var(--ink);outline-offset:2px}
  code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.9em}
  @media(prefers-color-scheme:dark){
    :root{--ink:#eef2f3;--paper:#16232a;--accent:#a5d3de;--muted:#9fb0b7;--line:#2c3f47}
    input{background:#1f2f37}
    button{color:#16232a}
  }
</style></head><body><main>${body}</main></body></html>`;
}

function html(markup, status) {
  return new Response(markup, {
    status,
    headers: {
      "Content-Type": "text/html; charset=utf-8",
      "Cache-Control": "no-store",
      "X-Robots-Tag": "noindex, nofollow",
    },
  });
}

/* Returns a Response to send instead of the site, or null to let the request
   through. Null is the only way past, so a thrown error or a missing branch
   fails closed rather than open. */
export async function gate(request, env) {
  const secret = env.SITE_PASSWORD;

  // Fail closed. An unset variable must never mean "serve the patient gallery".
  if (!secret) return html(page({ missing: true }), 503);

  if (await hasValidSession(request, secret)) return null;

  if (request.method === "POST") {
    const form = await request.formData().catch(() => null);
    const given = form && String(form.get("password") || "");
    if (given && safeEqual(await sign(given, secret), await sign(secret, secret))) {
      const exp = String(Date.now() + SESSION_DAYS * 864e5);
      const value = `${exp}.${await sign(exp, secret)}`;
      return new Response(null, {
        status: 303,
        headers: {
          Location: new URL(request.url).pathname,
          "Cache-Control": "no-store",
          "Set-Cookie": `${COOKIE}=${encodeURIComponent(value)}; Path=/; HttpOnly; Secure;`
            + ` SameSite=Lax; Max-Age=${SESSION_DAYS * 86400}`,
        },
      });
    }
    return html(page({ error: true }), 401);
  }

  return html(page(), 401);
}
