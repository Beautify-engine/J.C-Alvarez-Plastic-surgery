/* ============================================================================
   The consultation endpoint.

   Everything the site serves is static; this is the one piece of server-side
   code, and it exists for a single route. Every other request falls straight
   through to the static assets binding.

   Two mails go out per request: the brief to his office, reply-to the patient,
   and a confirmation to the patient. Delivery is Resend, chosen because
   MailChannels withdrew its free Workers integration in 2024 and there is no
   longer a no-account path off a Worker.

   Secrets (wrangler secret put NAME):
     RESEND_API_KEY   required, or the endpoint returns 503 and the form tells
                      her to call instead — it never reports a request as sent
                      when nothing was delivered.
     OFFICE_TO        where requests land. Comma-separate for several.
     MAIL_FROM        a verified sender on his domain, e.g.
                      "J.C. Alvarez Plastic Surgery <consultations@…>"
   ========================================================================= */

const ROUTE = '/api/consultation';
const LIMIT = 8 * 1024;      /* a request this size is not a person */
const MIN_SECONDS = 3;       /* nobody fills four questions faster */

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === ROUTE) return consultation(request, env, url);
    return env.ASSETS.fetch(request);
  },
};

async function consultation(request, env, url) {
  if (request.method !== 'POST') return json({ error: 'method' }, 405);

  /* Same-origin only. Does not stop a scripted POST, but it stops the form
     being embedded and submitted from somewhere else. */
  const origin = request.headers.get('Origin');
  if (origin && new URL(origin).host !== url.host) return json({ error: 'origin' }, 403);

  let body;
  try {
    const raw = await request.text();
    if (raw.length > LIMIT) return json({ error: 'size' }, 413);
    body = JSON.parse(raw);
  } catch {
    return json({ error: 'json' }, 400);
  }

  /* Spam gates, repeated here because the client-side ones protect the form,
     not the endpoint. A bot posting straight at this route never sees either.
     TODO before this is public: add a Cloudflare Turnstile token check here —
     the honeypot and the timer are the floor, not the ceiling. */
  if (body.company) return json({ ok: true }, 200);            /* honeypot: silent */
  if (Number(body.elapsed) < MIN_SECONDS) return json({ ok: true }, 200);

  const v = clean(body);
  if (!v.name || !v.email || !v.procedure.length || !v.timing) {
    return json({ error: 'incomplete' }, 422);
  }

  if (!env.RESEND_API_KEY || !env.OFFICE_TO || !env.MAIL_FROM) {
    return json({ error: 'unconfigured' }, 503);
  }

  const office = await mail(env, {
    to: env.OFFICE_TO.split(',').map((s) => s.trim()),
    reply_to: v.email,
    subject: `Consultation request — ${v.name} — ${v.procedure.join(', ')}`,
    text: officeText(v),
  });
  if (!office.ok) return json({ error: 'delivery' }, 502);

  /* Her confirmation must never fail the request: his office already has it. */
  await mail(env, {
    to: [v.email],
    subject: 'Your consultation request — J.C. Alvarez Plastic Surgery',
    text: patientText(v),
  }).catch(() => {});

  return json({ ok: true }, 200);
}

/* Trim, cap, and drop anything the form did not ask for. Nothing from the
   request body is trusted into an email except as plain text. */
function clean(b) {
  const s = (x, n) => (typeof x === 'string' ? x.trim().slice(0, n) : '');
  const list = (x, n) => (Array.isArray(x) ? x.slice(0, 12).map((i) => s(i, n)).filter(Boolean) : []);
  return {
    name: s(b.name, 120),
    email: s(b.email, 200),
    phone: s(b.phone, 40),
    language: s(b.language, 40),
    note: s(b.note, 2000),
    timing: s(b.timing, 80),
    procedure: list(b.procedure, 80),
    elapsed: Number(b.elapsed) || 0,
    source: b.source && typeof b.source === 'object' ? b.source : {},
  };
}

function officeText(v) {
  const src = Object.entries(v.source)
    .map(([k, x]) => `  ${k}: ${String(x).slice(0, 200)}`).join('\n');
  return [
    `${v.name}`,
    `${v.email}${v.phone ? '  ·  ' + v.phone : ''}`,
    `Prefers ${v.language || 'English'}`,
    '',
    `Considering:  ${v.procedure.join(', ')}`,
    `Timing:       ${v.timing}`,
    '',
    v.note ? `In her words:\n${v.note}\n` : '',
    '— — —',
    `Spent ${v.elapsed}s on the form.`,
    src ? `Came from:\n${src}` : 'Came from: direct, no campaign tags.',
    '',
    'Reply to this email and it goes straight to her.',
  ].filter((l) => l !== '').join('\n');
}

function patientText(v) {
  return [
    `${v.name},`,
    '',
    'Your consultation request has arrived. His office reads every one and',
    'replies, usually within a working day.',
    '',
    `You asked about: ${v.procedure.join(', ')}`,
    `Timing: ${v.timing}`,
    '',
    'Nothing is booked and nothing is committed. If it is urgent, or you would',
    'rather just talk, call 786 795 2113.',
    '',
    'J.C. Alvarez Plastic Surgery · 8400 SW 8th St, 4th Floor, Miami FL 33144',
  ].join('\n');
}

async function mail(env, msg) {
  const r = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${env.RESEND_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ from: env.MAIL_FROM, ...msg }),
  });
  return { ok: r.ok };
}

function json(obj, status) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' },
  });
}
