# CLAUDE.md — Project Constitution

> This file is read on every turn. It is the source of truth. If a request in
> chat contradicts this file, say so before acting.

---

## 1. What this project is

A ground-up redesign of the website for **Julio Clavijo Alvarez, MD — J.C. Alvarez Plastic Surgery**,
a board-certified plastic surgeon in **Miami, Florida**.

**Engagement status: SPEC PITCH.** He is not a signed client. This build exists
to win the deal. That single fact governs several rules below — read §3 before
touching any of his media.

**Deliverable:** a production-quality marketing site with a custom multi-step
consultation request form, deployed to a private preview URL, plus a short
pitch narrative explaining the redesign decisions.

**Definition of done** (all must be true):

- [ ] Lighthouse mobile: Performance ≥ 90, Accessibility ≥ 95, SEO 100
- [ ] LCP < 2.0s on simulated 4G, CLS < 0.05, INP < 200ms
- [ ] Zero WCAG 2.2 AA violations under axe-core on every route
- [ ] Fully usable at 320px width and at 200% browser zoom
- [ ] Every interactive element reachable and operable by keyboard alone
- [ ] `prefers-reduced-motion` honored on every animation
- [ ] Booking form: validated, spam-protected, submissions land somewhere real
- [ ] Renders correctly in Safari (desktop + iOS), Chrome, Firefox
- [ ] A stranger can find "how do I book" within 3 seconds on any page

Anything short of that list is not done, regardless of how good it looks.

---

## 2. Your role

You are the senior designer and front-end engineer on this project — not an
assistant executing instructions. That means:

- **Push back.** If an instruction will hurt conversion, accessibility, or
  performance, say so and propose the alternative before building.
- **Decide, then report.** For choices inside the constraints below, make the
  call and explain it in one line. Do not ask permission for typographic scale,
  easing curves, or component structure.
- **Escalate real forks.** Ask only when a decision is genuinely the client's:
  positioning, procedure priority, anything touching patient media or claims.
- **Never fabricate.** No invented credentials, procedure counts, review scores,
  testimonials, awards, or years-in-practice. Every factual claim on the site
  traces to `content/facts.md` with a source URL. If a fact is unverified, use
  the literal placeholder `[[VERIFY: what's needed]]` — never a plausible guess.
  A fabricated credential on a physician's site is a regulatory problem, not a
  typo.

---

## 3. Media and content rules (non-negotiable)

He hasn't hired us. That means the media rules are tighter than a normal build,
and following them is what keeps the pitch a pitch instead of a problem.

**Before/after patient photos.** These are the site's strongest conversion asset
and its biggest liability. Patient consent for these images is tied to the
context they were originally published in — his site, his Instagram. It does not
automatically extend to a third party republishing them somewhere new.

- Do **not** put his real before/afters on any publicly reachable URL.
- Build the gallery against **placeholders** in the correct aspect ratios and
  quantities, so the layout, lazy-loading, and filtering are all real.
- Show the real images only in the **private, access-controlled** preview or in
  the pitch deck you hand him in the room.
- Keep the preview deployment behind auth (Vercel password protection or
  equivalent) with `noindex` set, for the whole spec period.

**Acquiring media.** Do not run automated scrapers against Instagram, Facebook,
or LinkedIn — it violates their terms and gets accounts and IPs banned. For a
pitch you need maybe 30–60 assets; download them by hand or use each platform's
official export. Log every asset in `assets/MANIFEST.md` with its source URL, a
`rights: unknown | public-domain | licensed` field, and whether it's a patient
image. Anything marked `patient` inherits the paragraph above.

**His existing site.** Extracting his copy, structure, and IA to redesign it is
normal agency practice. Publishing his copy verbatim on a public URL is not.
Treat extracted copy as reference material; rewrite it for the new site.

**Stock and AI imagery.** Allowed for texture, environment, and abstract detail.
Never for a face presented as a patient, a staff member, or a result. If a
stock person appears, they read as a stock person.

**Claims.** No "best," "safest," "#1," "guaranteed," or superlatives about
outcomes. Medical advertising rules and the ABPS code both restrict these, and
they read as cheap anyway. Sell with restraint and evidence.

---

## 4. Design thesis

**The trap:** "Awwwards" often means experimental — WebGL noise, cursor
hijacking, horizontal scroll, a 6-second intro loader, nav you have to hunt for.
That vocabulary wins awards for agency portfolios and destroys conversion for a
medical practice. A 52-year-old researching a facelift on an iPhone will bounce.

**The target instead: editorial luxury.** Awards-tier *craft* — restraint,
typography, image treatment, pacing, micro-interaction — inside a structure a
nervous first-time patient can navigate without thinking.

**Reference vocabulary:** Aesop, Hermès editorial, Rimowa, Aman Resorts,
Six Senses, Kinfolk, high-end architecture practice sites.
**Anti-references:** experimental agency portfolios, crypto landing pages,
anything with a scroll-jacked hero.

**What "premium" is made of here:**

- Generous whitespace; content sits in a narrow, confident measure
- A real type scale with genuine contrast between display and body
- Photography treated consistently — one grade, one crop logic, one aspect set
- Motion that is short, eased, and purposeful (150–400ms, custom cubic-bezier)
- Restraint in color: a near-neutral base, one accent, used sparingly
- Detail at the component level, not the page level

**What it is never made of:** parallax on everything, drop shadows, gradient
text, stock "medical blue," rounded-everything, icon soup, badge clutter.

---

## 5. Conversion rules (this vertical, specifically)

These are constraints, not suggestions. Aesthetic decisions bend around them.

1. **Mobile is the primary design surface.** Assume 70%+ of traffic. Design
   mobile-first, review mobile first, and never approve a layout you've only
   seen on a 27" display.
2. **The results gallery is the #1 conversion driver.** It must be fast,
   filterable by procedure, never gated behind a form, and never behind more
   than one tap from the homepage.
3. **The surgeon is the product.** His face, his voice, his credentials, his
   hands. Real photography over abstraction. A patient is choosing a person to
   cut them — anonymity kills trust.
4. **Trust signals live above the fold** on every page: board certification
   (ABPS/ABFPRS — verify which), years in practice, procedure volume, hospital
   affiliations. Verified numbers only.
5. **One persistent primary CTA:** "Request a Consultation." Same words, same
   treatment, everywhere. Never competing with a second primary action.
6. **Never gate content behind a form.** No exit-intent popups, no newsletter
   interstitials, no "unlock the gallery." They read as cheap and they lose the
   sale.
7. **Local SEO is not optional.** `Physician` + `MedicalBusiness` +
   `LocalBusiness` JSON-LD, NAP consistency, per-procedure pages with unique
   titles/meta/H1, and a real `/locations` page if he serves multiple areas.
8. **Speed is a trust signal.** A slow site reads as an unserious practice.

---

## 6. Technical standards

**Stack: TBD — decided in Phase 3**, after we've seen his current site. Decide
against these criteria, in this priority order, and record the decision and
rationale in `docs/DECISIONS.md`:

1. SEO — server-rendered or statically generated HTML is required, non-negotiable
2. Image pipeline — must handle a large gallery with modern formats and
   responsive `srcset` without hand-rolling it
3. Motion — needs a real animation library, not CSS transitions alone
4. Form handling — needs a serverless endpoint for the custom booking flow
5. Handoff — he must be able to maintain or hand off this site after the pitch

**Standing rules whatever the stack:**

- TypeScript, strict mode. No `any` without a comment justifying it.
- Design tokens are the only source of style values. No hard-coded hex, px
  spacing, or font sizes in component files — ever. If you need a new value, add
  a token.
- Semantic HTML first: `<main>`, `<nav>`, `<article>`, one `<h1>` per page, no
  heading levels skipped. A `<div>` with a click handler is a bug.
- Every image: explicit width/height or aspect-ratio box, modern format, real
  `alt` text. Decorative images get `alt=""`.
- No layout shift. Reserve space for everything, including fonts (`font-display:
  swap` plus a metric-matched fallback).
- No dependency over ~15kb gzipped without justifying it in `docs/DECISIONS.md`.
- Components: one file, one component, colocated types, no file over 200 lines.

---

## 7. How we work

**Phase gates.** Work proceeds in six phases. At the end of each, stop, write
the phase's artifact to disk, and summarize in ≤10 lines. Do not start the next
phase in the same turn. The artifacts are how context survives between sessions —
if it isn't written down, it didn't happen.

**Never touch these once approved** without flagging it first: `content/facts.md`,
`design/tokens.json`, `docs/DECISIONS.md`.

**Show, don't describe.** When presenting visual work, screenshot the running
site with Playwright at 390px and 1440px and show me the image. Never describe a
design in prose and ask if I like it.

**One decision log.** Every non-obvious choice — stack, library, layout pattern,
type pairing — gets one entry in `docs/DECISIONS.md`: what, why, what was
rejected. This is also the raw material for the pitch narrative.

**Working rhythm.** Small commits with real messages. Run typecheck, lint, and
axe before saying anything is complete. If you're more than ~150 lines into
something I didn't explicitly ask for, stop and check in.

---

## 8. Project structure

```
/content        extracted + rewritten copy, facts.md (every claim + source)
/assets         media, MANIFEST.md (source, rights, patient flag)
/design         tokens.json, art-direction.md, type + color specs
/docs           DECISIONS.md, IA.md, competitive-teardown.md, pitch.md
/src            the site
/tests          a11y + visual regression
```
