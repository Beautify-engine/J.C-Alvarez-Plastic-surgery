# Art direction — J.C. Alvarez Plastic Surgery

References approved 2026-08-20. All three extracted from source, not eyeballed.
Anti-references remain CLAUDE.md §4's, plus the banned-tells list below.

| site | ground | display / body type | accent | notes |
|---|---|---|---|---|
| **5c.co** — cosmetic + regenerative, Coeur d'Alene | **dark** `#19252a` | Ivy Ora Display / Alliance No1 | `#a5d3de` soft cyan | Webflow. The most genuinely editorial of the three. |
| **mdplasticsurgery.com** — Phoenix/Scottsdale | **warm light** `#eeeadd` bone | Arquitecta (commercial) | `#1d4354` deep teal + `#4b403a` warm brown | WordPress. Warm neutral instead of medical white — the most distinctive palette. |
| **shaferplasticsurgery.com** — NYC | **cool light** white/black | Playfair Display / Open Sans | `#d6dfe2` pale blue, `#5d7a88` slate | WordPress + Salient. Has the hero video. Type pairing is the most conventional. |

**What the three actually share** — and what the client is responding to: generous
whitespace, a serif display against a clean sans body, a restrained near-neutral palette
with one accent, photography at large scale, and calm pacing. Not a specific hue.

---

## Client rules (stated 2026-08-20) — binding

> "Never fall back on Claude's standard interface. Avoid anything and everything that
> looks AI-generated or vibe-coded."

An abstract rule is unenforceable, so here are the specific tells. **None of these ship.**

**Banned — the AI-default visual vocabulary**
- Tailwind-default look: `rounded-lg`, `shadow-md`, `bg-gray-50/100`, indigo/violet accents
- Inter (or system-ui) as the display face — the single loudest tell
- Emoji used as icons; Lucide/Heroicons icon soup
- Equal-height card grids with drop shadows, three-across
- Gradient text, glassmorphism, blurred colour blobs, mesh gradients
- Everything centered; everything rounded
- The template rhythm: hero → three feature cards → testimonial strip → CTA banner → footer
- Generic abstract 3D/illustration filler
- Purple, indigo, or "SaaS blue" anywhere
- Pill badges with a dot; "✨" anywhere
- Body copy at a uniform 16px with no measure control

**Required instead**
- A real type scale with genuine display/body contrast, set in a licensed editorial face
- Asymmetry — content that sits off-axis on purpose, not a centered column
- Photography carrying the page, not components
- Detail at the component level: rules, letterspaced eyebrows, considered numerals
- A narrow measure (60–72ch) for body copy
- Motion that is short, eased, and purposeful — never decorative

## Resolved direction — light chrome, dark image bands

Client call 2026-08-20: **"a nice in between,"** pointing at Shafer. Screenshots of all
three at 1440 and 390 (`design/reference-shots/`) show the in-between already exists —
all three run **dark full-bleed footage of their people behind light chrome.** Shafer's
page alternates white → pale blue-gray → white → dark photographic band. MD does the same
with warmer tones. 5C runs the same rhythm inverted.

So the system is not a blended hue. It is a **band system**:

| band | token | carries |
|---|---|---|
| Light primary | `paper` `#f7f6f3` | reading sections — about, preparation, procedure copy |
| Light alt | `paper-2` `#e8eced` | alternating sections, rhythm without ornament |
| Light deep | `paper-3` `#d6dfe2` | nav bar, footer top (Shafer's move) |
| **Dark** | `ink` `#16232a` | **hero video · results gallery · facility/atmosphere** |
| Dark alt | `ink-2` `#1f2f37` | second dark band where two sit adjacent |

**Why the gallery gets a dark band specifically:** his 68 before/afters are composited on
black with a burned-in watermark. On a light ground each one punches a hard black
rectangle into the page. On the dark band they sit natively and read as a considered
gallery. The biggest constraint in his asset library becomes the thing that looks most
deliberate — see `docs/DECISIONS.md` D-001.

**What each reference contributes:**

| from | take |
|---|---|
| **Shafer** | The band rhythm. Full-bleed hero video *of the surgeon himself*, not stock. Serif display in white over a scrim, letterspaced caps subtitle, persistent pill CTA bottom-right. |
| **MD** | Warm neutral instead of sterile white — `paper` is `#f7f6f3`, not `#ffffff`. Letterspaced caps beneath a large display line. |
| **5C** | The dark ground values and the single soft-cyan accent. Alternating band discipline. The "I need help with…" goal-based entry. |

**Rejected from the references:** 5C's rotating-word H1 (animated H1 hurts LCP, reads
gimmicky). Shafer's `preload="auto"` video handling (see the video budget below) and its
Playfair/Open Sans pairing (the default "elegant" choice). MD's announcement ticker bar.
Any aggregate-rating block until `content/facts.md` clears.

## Typography — licensing

Ivy Ora Display (Ivy Foundry / Type Network) and Alliance No1 (Degarism) are **commercial
licenses**. We do not ship unlicensed fonts on a spec pitch.

- **Spec build:** free analogues, self-hosted, metric-matched fallbacks, `font-display: swap`.
  - Display candidate: a high-contrast editorial serif with true italics and a light weight.
  - Body candidate: a neutral neo-grotesque with a genuine Light.
  - Final pairing chosen in the type pass and logged in `docs/DECISIONS.md`.
- **Post-signature:** quote the real licenses as a line item. Swap is a token change only,
  which is the point of §6's token rule.

## Rules this inherits from CLAUDE.md

- Tokens are the only source of style values (§6). Every value above lands in
  `design/tokens.json` before any component uses it.
- One accent, used sparingly (§4). The cyan is for the CTA and focus rings, not decoration.
- Contrast — **measured, not assumed** (computed 2026-08-20):

  | foreground | on `#19252a` | on `#202c30` |
  |---|---|---|
  | `#b0bcbf` body text | **8.06 — AAA** | **7.37 — AAA** |
  | `#ffffff` | 15.68 — AAA | 14.34 — AAA |
  | `#a5d3de` accent | 9.69 — AAA | 8.86 — AAA |
  | `#80b8c5` cyan-dark | 7.15 — AAA | 6.54 — AA |
  | `#3b5057` charcoal-blue | 1.84 — **FAIL** | 1.69 — **FAIL** |

  The palette clears AAA for body copy with room to spare. **`#3b5057` is a
  border/divider value only — never text, never an icon that carries meaning.** Any UI
  component boundary that must be perceivable needs 3:1, so `#3b5057` is for decorative
  rules; functional borders step up to `#80b8c5` or lighter.
- Dark ground does **not** mean low contrast. Test at 200% zoom and 320px.
- `prefers-reduced-motion` honored on every transition (§6).

---

## Hero video — approved, with an engineering budget

Client requirement 2026-08-20: **video background on the hero.** Adopted.

This is in direct tension with the definition of done (LCP < 2.0s on simulated 4G,
Performance ≥ 90 mobile, CLS < 0.05). It is winnable, but only with a budget — and
**Shafer is the example of how not to do it:**

| Shafer's homepage | measured |
|---|---|
| `1730320918-shafer-home-hero-1.mp4` | **4.6 MB** |
| `background-video.mp4` | **14.3 MB** |
| `high.mp4` | **11.1 MB** |
| all five `<video>` tags | `preload="auto"`, **no `poster` attribute** |

That is ~30 MB pulled eagerly on load, with no poster frame, so the hero paints late and
the LCP element is whatever the video eventually resolves to. It looks expensive and
performs like a brochure CD-ROM. We take the look, not the implementation.

**Our budget and technique:**

- **The LCP element is a poster image, never the video.** A real `poster` frame, AVIF/WebP,
  responsive `srcset`, preloaded. The video fades in over it once it can play. LCP is
  therefore an image, and stays well under 2.0s.
- **≤ 2.5 MB for the hero loop**, 6–10 seconds, seamless. AV1/WebM with an H.264 MP4
  fallback. No audio track at all — not muted, *absent* (it saves bytes and removes an
  autoplay failure mode).
- `preload="none"` + `autoplay muted playsinline loop`. Load deferred until after first
  paint.
- **Fixed aspect-ratio box.** Zero CLS — the space is reserved before anything loads.
- **`prefers-reduced-motion: reduce` → poster only, video never fetched.** Non-negotiable (§6).
- **Save-Data / 2G / slow connection → poster only.** A 52-year-old on hotel wifi gets a
  sharp still, not a stall.
- Never the sole carrier of meaning: the H1, credential line, and CTA are real DOM text
  over the video, legible against a scrim, and pass contrast with the video removed.

**Content of the loop matters more than the technique.** Per §3, no stock person may read
as a patient, staff member, or result. So the loop is *him* — in consult, in the OR,
hands working — or the facility. That is also §5.3 doing its job. If we do not have
usable footage, the hero ships as a still portrait until we do; we do not fill it with
purchased b-roll of a smiling model.

`[[VERIFY: does he have video footage? Linktree lists a YouTube channel —
youtube.com/@drjcalvarez — which may hold usable material, subject to §3.]]`
