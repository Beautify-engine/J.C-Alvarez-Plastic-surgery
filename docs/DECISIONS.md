# DECISIONS.md

One entry per non-obvious choice: **what**, **why**, **what was rejected**. Raw material
for the pitch narrative (CLAUDE.md §7).

---

## D-001 — Visual direction: light chrome, dark image bands

**What.** Light page frame (`#f7f6f3` warm off-white, alternating to `#e8eced` /
`#d6dfe2`) with **dark full-bleed bands** (`#16232a`) carrying the hero video, the
results gallery, and atmosphere moments.

**Why.** The client asked for "a nice in between" of three references. Screenshotting all
three at 1440 and 390 showed they are *already* the same move: Shafer, MD, and 5C all run
dark full-bleed footage of their people behind light chrome. The in-between is not a
blended hue — it is that band system. Two supporting reasons: his **68 before/afters are
composited on black**, so a dark gallery band lets them sit natively instead of punching
holes in a white page; and long-form reading (his preparation content, the strongest
asset he has) is easier on a light ground.

**Rejected.** *Fully dark (5c.co)* — best for the gallery but punishing for his long-form
preparation content. *Fully light (Shafer/MD)* — forces re-matting all 68 cases or
accepting hard black rectangles. *A blended mid-tone ground* — muddy, and none of the
references actually do it.

## D-002 — Palette verified before adoption, not after

**What.** Every foreground/background pair computed against WCAG 2.2 before entering
`tokens.json`. Table in `design/art-direction.md`.

**Why.** Definition of done requires zero AA violations on every route. Cheaper to
constrain the palette than to retrofit it.

**Rejected.** Shafer's `#5d7a88` as a text colour — fails on their own pale bands.
`muted-on-light` at `#5a6b72` — 4.10 on `paper-3`, below AA; darkened to `#4e5d64`
(min 5.05 across all three light bands).

## D-003 — One accent, two lightnesses

**What.** A single accent hue: `#35606f` on light grounds, `#a5d3de` on dark.

**Why.** §4 requires one accent used sparingly. A band system alternating light and dark
would otherwise need two unrelated accents. Same hue at two lightnesses keeps it one
colour conceptually while clearing contrast on both grounds.

**Rejected.** 5C's `#a5d3de` alone — fails as text on light. Shafer's slate alone — muddy
on dark.

## D-004 — Type: Instrument Serif + Schibsted Grotesk (provisional)

**What.** High-contrast editorial serif for display; neo-grotesque with a true Light for
body. Base size **17px**, not 16px. Self-hosted woff2, metric-matched fallbacks.

**Why.** §4 wants genuine display/body contrast. Both are freely licensable and
self-hostable, so nothing unlicensed ships on a spec pitch.

**Rejected.** *Ivy Ora Display + Alliance No1* (5C) and *Arquitecta* (MD) — commercial,
cannot ship on spec; quoted as a line item if he signs, and swapping is a token change
only. *Playfair Display* (Shafer's actual face) — free, but it is the default "elegant"
serif and reads as template. *Inter* — as a display face it is the loudest AI-default
tell (§ client rules). *Uniform 16px body* — same reason.

## D-005 — Hero video approved with a hard budget

**What.** Video hero, but the **LCP element is a poster image, never the video**. ≤2.5MB
loop, 6–10s, no audio track, `preload="none"`, fixed aspect-ratio box, poster-only under
`prefers-reduced-motion` or Save-Data.

**Why.** Client requirement, and it conflicts with LCP < 2.0s / Performance ≥ 90 / CLS <
0.05. Measured Shafer's implementation: hero 4.6MB, plus 14.3MB and 11.1MB videos, all
`preload="auto"` with **no poster attribute** — roughly 30MB eager on the homepage. We
take the look, not the implementation.

**Rejected.** Autoplaying video as the LCP element. Purchased b-roll of a model — §3 bars
stock people reading as patients, staff, or results, so the loop is him or the facility.

## D-006 — No drop shadows, sparse radii

**What.** `elevation` documents an intentional absence. Radius applies to buttons and
inputs only; cards, images, and bands are square.

**Why.** §4 bars drop shadows and rounded-everything, and the client explicitly barred the
AI-default look. Depth comes from the band system and hairline rules instead.

**Rejected.** Card-with-shadow grids — the single most recognisable template tell.

## D-007 — Playwright installed as project tooling

**What.** `playwright` + Chromium as a dev dependency.

**Why.** §7 requires 390/1440 screenshots of real renders rather than prose descriptions,
and the definition of done requires axe-core on every route. Both need a real browser.
Already used to screenshot the three references into `design/reference-shots/`.

**Rejected.** Describing designs in prose — explicitly barred by §7.

## D-008 — Booking form collects no health data

**What.** Steps: procedure → timing → contact → review. **No** medical history,
medications, weight/BMI, or patient photographs.

**Why.** A consultation request is not an intake form. Health data pulls this into HIPAA
scope and creates a breach surface on a marketing site with no business holding it.

**Rejected.** BMI gating in the form — New Life's funnel does this; we are choosing not
to, and it is worth telling him why.

---

## Open — stack not yet chosen (Phase 3)

Recorded here so the reasoning survives: the teardown settled that a migration off
Elementor is mandatory (avg 144KB HTML, 31 stylesheets, 31 scripts per page, zero WebP,
across all 154 URLs — ≥90 mobile is unreachable). The stack decision itself is Phase 3,
against §6's five criteria.

## D-009 — One image grade, applied to everything, baked at export

**What.** A warm editorial grade — lifted matte blacks, `#f7f6f3` highlights, warm halation
bloom, film grain — in three depths (`air` / `standard` / `deep`) chosen by which band an
image sits on. Implemented as generated 3D LUTs plus an ffmpeg chain: `tools/grade.sh`.

**Why.** §4 requires photography treated consistently — one grade, one crop logic. Assets
arrive from a dozen sources (his stock, his portraits, new photography, generated stills)
and must read as one commission. Generating the LUT *from* `design/tokens.json` means the
grade cannot drift from the palette. Client reference: the Hims/Hers register — warm haze,
grain, glow.

**Rejected.** *A single LUT* — an image graded for a light band reads as a grey rectangle on
`--ink`. *Cool/blue shadows* (the first attempt) — fought `--paper`'s warmth and read
clinical, which is the thing we are moving away from. *CSS `filter:`* — paint cost on every
frame, and it does not survive image export. *Prompt-only AI regrading* — inconsistent
across a set, which defeats the entire purpose; kept as a documented fallback only.
*Grading the before/after cases* — clinical results stay colour-accurate; altering their
tone misrepresents an outcome.

## D-010 — Procedure carousel: three directions, none auto-advancing

**What.** Three full-width treatments on the dark band, all sharing the same eight
`cool-deep`-graded 4:5 images. **A** classic track (competitor parity), **B** index &
stage, **C** expanding panels. Live at `/carousels.html`.

**Why.** Client asked for competitor parity plus original directions. All three are built
on the same data and tokens, so choosing between them is a design decision, not a rebuild.

**Rejected across all three.** *Auto-advance* — fails WCAG 2.2 without a pause control and
moves before people finish reading; definition of done requires zero AA violations.
*A JS carousel library* — native `scroll-snap` is fewer bytes, better touch behaviour, and
survives JS failure. *Dots as the only affordance* — they are tiny targets that convey no
position. *Drop shadows on cards* — barred by §4 and the client's AI-tell list; separation
comes from the band and hairline rules.

Per-option notes:
- **A** — flex track, not grid. `grid-auto-columns: minmax(0, …)` shrinks tracks to fit
  instead of overflowing, which silently collapsed all eight into view.
- **B** — roving tablist. Hover, focus and arrow keys all drive it, so it works by pointer,
  keyboard and screen reader without a separate mode.
- **C** — expanded panel is `flex-grow: 4.2`, not 6, and images use
  `object-position: center 32%`. A 4:5 image in a 16:9 panel over-magnifies; at 6 the crop
  was gratuitous, which is the opposite of the §4 brief.

`[[VERIFY: image-to-procedure mapping is my assignment from the visual content — confirm
before these go near a procedure page. Also confirm rights for MANIFEST: generated,
licensed, or his.]]`

## D-011 — `clean` becomes the default grade; the desaturated look is retired

**What.** New `clean` / `clean-deep` presets are the site default. **Saturation is preserved
(100–108%)**; polish comes from a gentle S-curve, a whisper of black lift, light grain and
a restrained bloom — not from draining colour.

**Why.** Client, on seeing `cool-deep` applied to the procedure set: *"way too unsaturated
and grey looking… I just wanted that clean premium photography feel that looks natural."*
Correct call. The reference look (Hims/Hers, Aesop) is colour-accurate and clean; the
polish is tonal, not chromatic. Measured before/after: `cool-deep` retained **27%** of the
original saturation on the BBL frame; `clean-deep` retains **104%**.

**Root cause of the grey.** The `SPREAD_CLAMP` added in D-009 to fix an orange cast was
compressing any warm colour at |R−B| > 0.085 — which is most skin and every warm
background. It is now **per-preset**: 0.42 for the clean family (catches only extreme
casts), 0.12 for the warm family, 0.20 for cool. Bloom threshold also raised to 0.86/0.88
so bright backgrounds stop washing out.

**Rejected.** *Desaturating for cohesion* — cohesion comes from consistent white balance,
black point and grain, not from removing colour. *A monochromatic tie to the palette* —
photography complements the UI, it does not match it.

## D-012 — Carousel: Option A ships for procedures; Option C is repurposed

**What.** **Option A** (classic track) is the procedures carousel. **Option C** (expanding
panels) is retained as a section pattern for **case studies / patient stories / the team** —
somewhere atmosphere matters more than scanning a list. Option B is parked.

**Why.** Client selection. It is also the right split: A lets a visitor scan eight
procedure names at a glance, which §5.1 wants for a nervous first-timer; C hides seven of
eight names behind vertical text, which is a conversion cost on a navigational section but
an asset on a narrative one.

**Also fixed while wiring it up.** The first four track images were `loading="lazy"`
despite being visible on load — a real LCP bug, not just a capture artefact. And
`tools/serve.py` replaces `python -m http.server`, which is single-threaded and truncates
concurrent responses.

## D-013 — The grade gets character from split toning, not desaturation

**What.** `clean` / `clean-deep` rebuilt with **split toning** — cool slate in the shadows,
warm ivory in the highlights, weighted by luminance so midtones (skin) are untouched. Plus
a real highlight rolloff and visible grain.

**Why.** Client: *"it looks like you completely removed all color grading."* Correct —
measured, D-011's `clean-deep` moved saturation 0.321→0.335 and white point 253.6→245.6.
That is a no-op. The lesson across D-009 → D-011 → D-013: **saturation is the wrong dial in
both directions.** Character comes from where the shadows and highlights sit on the colour
wheel. Now: saturation 90% retained, whites 254→232, blacks 51→60 — a visible, deliberate
look with natural skin.

**Rejected.** Reaching for saturation again in either direction.

## D-014 — About section: research as the origin, healing as the thesis

**What.** Light `--paper` band. Client-supplied cut-out portrait left, copy right, credential
strip beneath. Headline: *"The operation is the middle of the story."* Pull quote is his own
words from the video transcript, verbatim.

**Why.** §5.3 — the surgeon is the product. The Post-Gazette biography gives verified,
specific, unusual detail (four months unpaid at a Harvard lab; following his boss to
Pittsburgh when no one else would), and the transcript gives his own framing: *improving the
quality of your healing.* That thesis ties the PhD, the hyperbaric chamber and the 90-day
preparation content into one argument, and no Miami competitor is making it.

**Rejected.** *A talking-head video as the section's primary element* — 29 seconds, and the
still portrait carries more authority per pixel. The video belongs on the full `/about` page
as a secondary "hear from him," not as the homepage's About. *The site's own "A Legacy of
Excellence" framing* — institutional name-drops with no story. *Re-stating the ABPS badge in
markup* — the supplied portrait already carries the card; doubling it read as clutter.

## D-015 — Copy turns outcome-first; the video does not get its own section

**What.** Hero: *"Refined aesthetics, grounded in science"* → **"Results that look like you."**
About: *"The operation is the middle of the story"* → **"Your result depends on how you heal."**
The 29-second intro video becomes a play affordance on the About portrait, not a section.

**Why.** Client direction: the site is a sales instrument, and I was writing craft-led copy
from the surgeon's point of view. Audited against `docs/conversion-doctrine.md`, all three
headlines were about *him*. The new hero answers the two fears that decide the sale — *will
I look done* and *will I get that result* — in four words. The new About headline makes his
research background matter to **her** rather than reading as a CV.

**On the video.** 29 seconds of "my vision and purpose is to integrate all the knowledge"
is abstract and answers none of the four fears. Standalone video sections also get skipped
— mobile play rates run 10–20%, so a dedicated section spends prime scroll on something
most visitors never start. Its real value is proof-of-person, so it sits inside About as a
small play affordance.

**What would earn a video section:** him answering the actual objections on camera —
*"Will it look done?"*, *"What is recovery really like?"*, *"Am I a candidate?"* Three or
four 45-second answers. That is an hour of filming and would be the highest-converting
video asset on the site. Requested in `assets/ASSET-REQUEST.md`.

**Rejected.** Keeping craft-led headlines because they read well. They do read well — and
they sell nothing.

## D-016 — One HTML file per page

**What.** The homepage is a single `src/public/index.html` carrying every section in
conversion order. Section-preview pages (`about.html`, `carousels.html`) are gone, and
their CSS/JS folded into one `styles.css` and one `main.js`. Each future route — procedure
pages, results, preparation — gets its own single file the same way.

**Why.** Client direction. It is also correct: previewing sections in isolation hid two
real editorial faults that were obvious the moment they sat together —

1. **The About credential strip repeated the hero trust strip** (Certification, Doctorate,
   Practising since, all twice within one scroll). Now the About strip carries only what it
   adds: residency, research, recovery protocol, preparation, facility accreditation.
2. **The procedures headline was still craft-led.** *"Surgery, planned in millimetres"* →
   **"What would you like to change?"** — second person, invites self-identification, which
   is that section's actual job.

Option B and Option C carousels are parked in `src/public/_parked/` for reuse — C is
earmarked for case studies / patient stories / team per D-012.

**Capture note.** `fullPage` screenshots composite `position:fixed` elements at their scroll
offset, which looks like a layout bug. `tools/shootpage.mjs` now hides the sticky CTA for
full-page passes; `tools/viewport.mjs` checks sticky behaviour honestly.

## D-017 — Hero rebuilt: type gets its own column; credentials move above the fold

**What.** The hero is now a split composition — a left-weighted scrim puts the type column on
near-solid `--ink` while the subject stays visible on the right, headline scaled up to
`clamp(3rem, 5.5rem)` at `line-height:.98`, and the credential rail moved from a separate
section onto the hero's bottom edge.

**Why.** Client: *"the hero is weak."* Three causes, all real: the type sat **on top of** the
subject in a busy documentary frame, so neither read; the headline was undersized for a
full-bleed band; and every trust signal was below the fold, so the first screen did
**DESIRE** with no **TRUST** behind it. Credentials on the hero's bottom edge fix the third
and remove a redundant section.

**Bug found doing it.** `.hero` is a column flex container and `.wrap` carries
`margin-inline:auto` — **auto margins on a flex item cancel cross-axis stretch**, so `.wrap`
collapsed to content width and re-centred the type. Fixed with `width:100%`. Caught by
measuring boxes in the browser rather than reading the screenshot, which had me guessing at
the wrong cause twice.

## D-018 — Reviews: a drifting wall of voices, in the register people actually write in

**What.** A held header beside **two columns of quotes counter-drifting** — left rising,
right falling, at different speeds (64s / 78s). Masked to transparent at top and bottom, no
cards, no borders, no arrows, no dots. The motion *is* the interface. Hovering or tabbing
into the section pauses every column so anything can be read.

**Two rounds of client feedback got here.** First attempt was bordered cards in a row —
*"a little too basic."* Second was static newspaper columns — *"the design is weak still…
I want something clean, and animated."* Both were right: on a page whose argument is
restraint, a card row reads as filler, and a section made only of words needs the
typography and the motion to carry it.

**The copy was also wrong, and that mattered more.** *"These are very fake sounding."*
Correct — it was marketing prose: *"He drew what my frame could carry and explained why the
other thing would not age well."* Nobody writes like that. Real reviews are informal,
specific and mundane: *"I asked for something bigger and he said no. Pulled out my
measurements and explained exactly why. I was annoyed lol. He was right."* The placeholder
set now runs in that register — lowercase asides, unfinished thoughts, front-desk details,
one that admits it hurt.

**Honesty preserved without cluttering the design.** Per-card `[[VERIFY]]` badges wrecked
the composition, so it is now one quiet line under the header — *Placeholder copy, real
reviews pending verification* — and the section still ships no testimonial we cannot source.

**Accessibility.** `prefers-reduced-motion` turns the wall into a plain scrollable list with
no animation and no mask; the duplicated loop content sits in the second column, which is
`aria-hidden`, so screen readers hear each quote once.

**Bug caught.** Renaming `.band__head` to `.rev__head` orphaned the heading rules and the h2
silently fell back to the body sans — the classic silent-font-fallback failure. Re-screenshot
after any selector rename.

## D-019 — Reviews set in the body sans, and they name him

**What.** Review text moves from the display serif to `--font-body` at ~1rem/1.6, and
**"Dr. Alvarez" appears in 10 of 12 quotes**, set in medium weight.

**Why (type).** Client: *"the font is a bit too much on the reviews."* Correct — twelve
quotes in an editorial serif is a wall of display type, and it fought the section heading
for the same voice. It was also working against the goal: **a user-written review set in an
elegant serif reads staged.** Sans reads like something a person actually typed, which is
the entire point of the raw register. The serif is now reserved for headings, so the page
has one clear typographic hierarchy instead of two competing ones.

**Why (naming him).** Client: *"we can mention the actual doctor more."* Real reviews name
the surgeon constantly — it is one of the tells that separates genuine ones from written
ones. It also does three jobs at once: reinforces that she is choosing **a person** (§5.3),
puts his name in crawlable body copy on the homepage, and makes the section about him rather
than about the practice. Two quotes deliberately do not name him — uniform naming would read
as scripted.

**Emphasis, not decoration.** His name sits at weight 500 against 400 body text — enough to
register while scanning a drifting column, not enough to look marked up.

## D-020 — The homepage results section is an index, not a wall of before/afters

**What.** Light `--paper` band. Left: headline, the ungated promise, one button into the
gallery. Right: a typographic index — case count per procedure in large tabular display
numerals against hairline rules, each row linking into a filtered gallery view. **No
clinical images on the homepage.**

**Why.** Client raised it directly: his cases are watermarked PowerPoint exports and would
*"ruin the look of the home page."* Investigating confirmed worse than that —

- Layouts are inconsistent: body cases are two clean panels, face cases a 2×2 grid with
  white dividers, so no single crop rule works across 68 files.
- The diagonal watermark sits **on the photographs**, not in the margin; cropping cannot
  remove it.
- They sit on pure `#000` while the band is `#16232a`, so every tile reads as a darker
  rectangle. Keying the black out was tested and **ate the patients' dark garments**.
- Most decisively: they are **explicit clinical images** — bare chests with cover dots,
  full torsos. Shafer and MD both keep these behind a gallery a visitor opts into. That is
  the convention for a reason.

**So the fix is editorial, not technical.** The section still does its **IDENTIFY** job —
*"See whether he has done work like yours"* plus real per-procedure counts is a specific,
checkable claim — and sends her one tap to the gallery, where the documentation aesthetic
belongs and where she has chosen to look.

**"No form. No email. Just the cases."** §5.6 bars gating, and most competitors in this
market gate their galleries behind a lead form. Saying so plainly converts a compliance
rule into a differentiator.

**Rejected.** A homepage grid of watermarked slides. Re-mastering 68 inconsistent exports
by hand for a spec pitch. Keying out the black — destroys garment detail.

`[[VERIFY: per-procedure counts are derived from which slides appear on which procedure
page; 51 unique of 68 mapped, and some appear on more than one page. Confirm before these
numbers ship as fact.]]`

## D-021 — Results: rebuilt pairs on the homepage, lightbox for detail

**What.** Tiles are **composed by us** from before/after halves extracted out of his slides,
in a 4:5 pair with our own hairline divider and caption bar. Clicking opens a lightbox
showing the same clean pair large, with our BEFORE/AFTER labels, keyboard arrows and Esc.
Filters by procedure, 8 shown, batch reveal.

**Why.** Client, twice: the grid of whole slides was ugly, and then — correctly — that
results still belong on the homepage because *"something like this takes a lot of
convincing."* Both are true, and the resolution was neither hiding them nor blurring them.

**The actual diagnosis.** Every export is *already a designed composition* — white frame,
title band, vertical Before/After slabs, centre divider, watermark. Any layout wrapping it
nests one design inside another, which is why the grid read cluttered and why showing it
**larger made it worse** (Option A turned the title band into a billboard). Layout could
never fix a source problem.

**What worked.** Per-image bounding-box detection on each half, then letterboxing into a
fixed 4:5 box rather than force-cropping — the earlier force-crop clipped heads. All 50
pairs extract; the title band, the big labels and the white frame are gone. Body cases come
out clean. **Face cases still catch his labels**, which sit inside the photo area on those
slides, so we add none of our own on the tile and avoid doubling.

**Rejected.** *Blur-to-reveal* — reads as a gate, and §5.6 bars gating; blurring the proof
also defeats the section. *Showing the original slide in the lightbox* — reintroduces the
noise we just removed, so the lightbox shows the clean pair instead. *Bigger tiles* —
amplifies the source noise proportionally.

**Still the best available fix:** unwatermarked originals from him. With clean photos a
drag-to-compare slider becomes trivial, and that is the pattern this vertical is built on.

## D-022 — Results ships as an infinite coverflow; blur carries depth

**What.** Option A selected. One case sharp and centred at 8:5, neighbours rotating away on
the Y axis with scale and depth falloff, **blurred by distance (4/8/12px) rather than
faded**. The index wraps in both directions. Filters are a typographic index. B (case book)
and C (stacked deck) parked in `src/public/_parked/`.

**Two geometry bugs found and fixed:**

1. **Cards were portrait.** A card holding two 4:5 photos side by side must be **8:5
   landscape**; it was portrait, so each half became a narrow sliver and `object-fit:cover`
   chopped the sides off every photo — "can't even see the results on some." Option B never
   had this because its 16:10 spread divides into two exact 4:5 halves. Centring moved from
   `margin-left` into `translateX(-50%)` since width is now derived from aspect-ratio.
2. **Ring duplication.** With a filter applied a set can be small, so the visible span
   clamps to `floor((n-1)/2)` — otherwise the same case appears on both sides of the loop.

**Opacity is not fully removed.** Only the outermost ring fades, and only so cases dissolve
on exit instead of popping. Everything within two of centre holds full opacity.

## D-023 — Two CSS collisions, same root cause

`.nav` (gallery arrows) collided with the site header's `.nav`, inheriting
`background: var(--paper-3)` and painting a pale-blue block behind every control. `.pills`
was a centred capsule row — **on our own banned-tells list** in `design/art-direction.md`
("pill badges", "everything centered") — and shipped anyway.

Both came from adding CSS without checking it against what exists. Every class in the
results section is now scoped `res__`, and `tools/bgprobe.mjs` dumps computed backgrounds
so unexpected fills get caught by measurement rather than by the client spotting them.

## D-024 — Instagram gets weight: 148K, verified, and reframed as authority

**What.** The reel section becomes an **Instagram** band. Headline leads with the number —
*"148,000 people follow him for the answers"* — over a stat row: 148K followers ·
1,143 posts · Verified · 7–18K typical reel reach. Result reels sit beneath it.

**Why.** Client: *"I kinda want to flex more his Instagram, he's pretty big."* He is, and it
is the **largest verified third-party trust signal in the project** — larger than anything
on his website, and checkable in one tap, which is exactly what §3 leaves us in place of
superlatives.

**The bigger find is what the reels contain.** Sampled titles — *why implants harden*,
*what deep vein thrombosis is*, *ponytail facelift: the truth*, *face and neck: together or
separately*, *what men have done* — are **objection-answering content**, which D-015 named
as the highest-value video asset we could ask him to film. He has been making it for years
across 1,143 posts. It also substantiates his own framing from the video transcript
("focused on teaching you about plastic surgery") with evidence rather than assertion.

**Framed as authority, not vanity.** The headline says people follow him *for the answers*,
so the number reads as earned expertise rather than a popularity metric.

**One caution logged in `content/facts.md`.** A third-party overlay in the same screenshot
shows ~409 avg likes and 21 comments across 47 posts — about 0.3% of followers, while reel
views run 7–18K. The stat row therefore carries **post count, verified status and reel
reach** alongside the follower number, so the claim rests on several checkable figures
rather than one that invites arithmetic.

---

## D-025 — Procedure pages ship as one template, not eleven layouts

`src/public/procedure.css` + `procedure.js` are shared; each procedure is one HTML file
(D-016). Eight numbered sections in fixed order: results · what it repairs · the operation
· the rule · candidacy · recovery · risks & cost · questions.

**Why.** Eleven pages is where an agency site either scales or collapses. A shared sheet
means a fix to the recovery timeline fixes it everywhere, and the section index, reveal,
case stage, timeline and video card all come free on page two. Every class is prefixed
`p-`/`.p…` after D-023, where two unscoped names collided mid-build.

**Numbered sections were chosen over titled cards.** A patient reading a facelift page
after a tummy tuck page finds the same information at the same position. Consistency of
structure is what makes a set of pages read as a practice rather than a stack of landing
pages.

**Rejected: a section-per-page CMS-style block system.** Nothing is being handed to an
editor during the spec period, and it would have cost a day.

---

## D-026 — Before/after gets a three-state view control, not a wipe slider

`BEFORE · BOTH · AFTER` collapses one grid column to `0fr` over 380ms. The stage opens on
BOTH at desktop and on AFTER at ≤48rem.

**Why not a drag-to-reveal wipe.** A wipe needs before and after shot on the same axis at
the same crop. His cases are multi-angle composites split into halves, so a wipe would
show two different framings sliding over each other — the interaction would advertise the
inconsistency it is supposed to hide.

**Why the mobile default differs.** Side by side at 390px gives each half about 150px.
Nobody studies a result at 150px. Opening on AFTER and letting one tap reach BEFORE is how
people actually read these, and it costs nothing on desktop where both fit.

**No image reloads on view change** — only the grid track interpolates, so switching is one
composited transition rather than a fetch.

---

## D-027 — Recovery is published as a scrubbable timeline

Eight milestones (Day 1 → Month 6) on one axis, real `tablist` semantics, arrow-key and
Home/End navigation, one panel visible.

**Why.** This is the richest content he already owns. His current page buries a genuinely
detailed recovery chart — shower at day five, drive once off narcotics, desk work at 10–14
days, compression eight weeks then part-time, one litre of lipo maximum, numbness that can
be permanent — under a generic "timeline chart" heading. It is the most specific,
least-marketing thing on his site and it answers the question people actually have.

**Scheduling, not reassurance.** The panel is framed as when-can-I, because "when can I
drive" is the question, not "will I feel better".

**A bug worth recording:** `.ptime__panel{display:grid}` silently overrode the UA
`[hidden]{display:none}` rule and rendered all eight panels at once. `[hidden]` needs an
explicit `display:none` any time a component sets `display` in a class rule.

---

## D-028 — The one-litre cap gets its own section

Florida's legal ceiling on liposuction combined with abdominoplasty — one litre, ~2.2 lb —
is set as a full-width statement between the technique and candidacy sections.

**Why.** §4 asks us to sell with restraint and evidence. Volunteering a limit that
constrains what he can sell you, and naming the reason (blood loss, fluid shifts), does
more for trust than any superlative the current site uses 33 times. It also quietly
disqualifies the competitor who offers to do it all in one sitting, without naming anyone.

---

## D-029 — YouTube is embedded, never re-hosted, and never with his thumbnail

The talks card on a procedure page is a **typographic facade**. On press it injects a
`youtube-nocookie.com` iframe. Nothing is fetched from Google before that — verified: zero
third-party requests on load, eight hosts after the click.

**Why embed rather than download.** Re-hosting his videos would add ~25 minutes of MP4 to
our bandwidth, put us on the wrong side of YouTube's terms, and — the part that matters for
a pitch — strip the views and watch time off his channel. Embedding leaves 202 uploads and
1,510 subscribers earning for him. If he later wants self-hosted files for control, he
exports his own masters from YouTube Studio, which is the same official-export rule §3
already applies to Instagram.

**Why no thumbnail.** His packaged thumbnails are the exact vocabulary §4 rules out — the
2021 tummy tuck one is a bikini stock model with red Impact type and yellow slashes.
Downloading it would put the worst artefact of the old brand on the best page of the new
one. A card built from type on our own ground is on-brand, avoids the question entirely,
and requests zero bytes.

**Why two rows instead of one.** The best tummy tuck talk (6:26, current, a real diagram)
is **Spanish**; the only English-audio one is 25:39 and five years old. A trilingual
practice should show both with the language stated, rather than quietly serving Spanish
audio to an English page. Recorded as an asset ask: one current English recording.

**The find that matters more than the embed.** Cataloguing the channel surfaced
`lfUDnaabfEM` — he *prohibits* compression for the first month after abdominoplasty, which
contradicts his own website copy that our recovery timeline is built from. Two channels,
opposite post-op instructions. Logged in `content/youtube-catalog.md` and
`assets/ASSET-REQUEST.md`; the page is not safe to ship until he says which is current.

## D-025 — Hero rebuilt as a hard split; the scrim was the amateur tell

**What.** The hero is now a two-column grid: a solid `--ink` panel carrying all the type,
a hard 1px edge, and the media held in its own column with no gradient over it. Corner
metadata top (location / certification), proof as a **2×2 grid on a rule** rather than an
inline text list, and a caption pinned to the media's own foot.

**Why.** Client: *"still doesn't have that clean, premium look… I don't want it to look
vibe coded."* The diagnosis was the **scrim**. Washing a diagonal gradient over busy
footage so text becomes legible is the single clearest template tell — it announces that
the image could not carry the frame. Type on a solid panel with a hard edge is the
opposite move: the geometry *is* the design, and nothing has to be hidden.

Second effect: the footage stops having to be a hero. Contained in its own column it reads
as documentary, which is what it is, instead of as a failed cinematic frame.

## D-026 — Motion system

Entry choreography (media settles from 1.06 scale; index, eyebrow, headline lines, lede,
CTA and each proof cell stagger 60–100ms apart), a 26s ambient drift so the frame breathes,
scroll reveals on all 7 major blocks with 70ms child stagger, magnetic CTA on pointer
devices, and an inline-SVG film grain at 0.32 over the dark bands.

Verified in-browser rather than assumed: hero line opacity 0 at 120ms → 1 at 1.7s; 7 of 7
reveal targets fire across a full scroll. All disabled under `prefers-reduced-motion`, and
every element is visible by default if JS never runs.

## D-027 — Regression: the hero rewrite deleted the mobile chrome

Replacing the hero CSS block removed the mobile header rules that lived beside it — the
hidden header CTA, the horizontally-scrolling nav, and the sticky bottom CTA. Mobile came
back with a two-line CTA button in the header and a nav wrapping to two rows.

**Restored, and moved to its own clearly-labelled block at the end of the stylesheet** so a
future section rewrite cannot take the site chrome with it. Third CSS regression of this
build (after `.nav` and `.pills`) — all from editing by position rather than by scope.

---

## D-030 — The template gets four different section shapes, not nine of one

**The problem, seen only at full-page zoom.** Every section had the identical shape:
small numeral, hairline, serif heading left, grey lede right, content below, same
container, same padding — nine times. Individually each section looked fine. Stacked,
the repetition read as a component pasted nine times rather than a designed page. That
is the "template" tell, and no amount of hero work fixes it.

**Four sections were given genuinely different shapes:**

- **Results** — the stage now runs the full container at 1:1 per half, with metadata
  dropped to a rail beneath. It is the page's biggest visual because it is the thing
  that actually sells (§5.2). It was previously a 1.35fr column beside a metadata list,
  which made the conversion driver the *third* largest element in its own section.
- **The operation** — the drawing is pinned and lights up the part being described as
  the steps scroll past. Fills what was an empty column, and lets the diagram carry
  explanation the prose was carrying.
- **The limit** — no numeral chip, no two-column head. One sentence at display scale.
  The page needed a moment that is purely type.
- **Candidacy** — moved to the dark ground, because the bottom third was three
  consecutive light text sections reading as one grey run.

**Word count: 2,215 → ~1,400 visible at rest.** Diagrams took over work the prose was
doing in "what it repairs" (223→144) and "the operation" (256→177), rather than the text
simply being moved elsewhere.

**Two accessibility regressions this pass caused and fixed:**

1. Dimming inactive steps to `opacity:.42` dropped body text to **2.46:1** — a serious
   AA failure. The active step is now *marked* (accent numeral, growing rule) instead of
   the others being faded. Never carry state with opacity on text.
2. `[data-reveal]` renders at `opacity:0` in any full-page screenshot, because
   IntersectionObserver never fires without a real scroll. Every contact sheet taken
   before this was of a half-invisible page. `tools/shootpage.mjs` now forces `.is-in`.

**Still the binding constraint: two photographs on the whole page.** Composition and
typography have been pushed about as far as they go against a single stock hero image
and one case stage. See `design/media-brief.md`.

## D-028 — Four CSS regressions from index-based edits; process changed

Rewriting the hero three times by string offset (`css[:a] + new + css[b:]`) silently deleted
every rule that happened to sit between the markers. Cumulative damage found by audit:
**21 classes referenced in HTML with no CSS rule** — the entire About section, the whole
procedures track, and the shared `.band__head` / `.ctl` / `.creds` / `.pull` helpers.

Symptoms: procedures carousel rendered at **11,231px tall** (flex track fell back to
`display:block`, each 4:5 figure stacking full-width), About at 2,404px.

**Fixed and fenced.** All restored rules now sit in one clearly-marked block at the end of
`styles.css`, alongside the mobile chrome block restored in D-027.

**Process change:** never edit CSS by offset again. Edit by selector, and run the
class-coverage audit (every `class="…"` in HTML checked against defined selectors) after
any structural change — it found all 21 in one pass and would have caught the first
regression immediately.

---

## D-031 — Nine sections become five, and the slide master is deleted

**"It looks like a PowerPoint."** Correct, and specific. Every section was a sealed
full-width band opening with a numeral, an eyebrow and a full-width rule above a heading
at top-left, then content, then a hard colour flip into the next one. That is a slide
master applied nine times. The section *shapes* had been varied in D-030; the *chrome*
and the band-per-topic structure hadn't.

**What changed:**

- **`.p-mark` is gone from every section.** Headings now simply start. Wayfinding was
  already handled by the sticky page index, so the numerals were decoration that happened
  to look exactly like slide furniture.
- **Nine sections became five.** What it repairs + the operation + the one-litre cap +
  his recordings are one continuous argument, so they are one `<section>` separated by
  hairlines rather than four bands. Risks + cost + questions likewise.
- **Eleven colour flips became four.** The hero now runs straight into results on the
  same ground; candidacy runs into recovery on the same ground. A page that changes
  colour every screen reads as a deck no matter what is on it.
- **Internal rhythm now differs from section rhythm.** Sub-blocks are separated by a rule
  and ~60% of the section padding. That difference is most of what separates a page from
  a deck.

**Repetition audit drove the cut, not taste.** Scripted a check for how many sections
each topic appeared in: the one-litre cap **4×**, muscle repair **5×**, "skin below the
navel" **4×**, not-a-weight-loss **3×**, numbness **3×**, compression **3×**. The FAQ was
the worst offender — it re-answered eight of the nine topics the page had already
covered. It went from 12 questions to 6: only what is genuinely unanswered elsewhere.

**2,215 → 1,532 words in the DOM**, roughly 1,050 visible at rest. Page height
13,584px → **11,437px**.

**One real bug found on the way.** `styles.css` applied the homepage hero's staggered
entrance animation to `.hero__corner`, `.hero__lede`, `.hero__cta` and `.hero__proof`
**unscoped**. The procedure hero reuses those class names, so it inherited a 780ms fade
— which axe caught mid-flight as a **1.4:1** contrast failure on the CTA. All of them are
now scoped to `.hero`. Homepage re-audited: still clean.

---

## D-032 — Testimonials ship as labelled placeholders, and the page gets real photography

**Asked for fabricated testimonials. Built labelled placeholders instead.** §2 bars
invented testimonials outright, and §3 D2 says the choice is "signed releases, or ship
none". But the homepage already solved this: placeholder quotes that say so on the page
(D-018). The section now carries three short quotes and the line *"Placeholder copy —
written to build the layout, not by patients."* It breaks up the text exactly as well as
invented copy would, exercises the real layout, and cannot become a regulatory problem if
the preview is ever seen by someone outside the room. Real reviews ship with a source URL
or the section is cut.

**Quotes are deliberately short.** A testimonial wall is still text. Three quotes of ~20
words each add social proof without adding to the density problem this pass was fixing.

**Three real photographs added, from assets we already had:**

- **The surgeon section** — him in the office, plus a press-interview frame as an offset
  inset. Placed straight after the operation section: the reader has just learned what he
  does to them, which is the moment they want to know who he is (§5.3). Links to `/about`.
  Copy is the Post-Gazette material — 180 babies on a Navy base in 1997, four months
  unpaid at a Harvard lab — which is the differentiator no Miami competitor can copy.
- **A full-bleed band** pulled from **frame 11.2s of his own hero footage**. The video
  notes in `ASSET-REQUEST.md` identified 8.9–12.9s as the only dignified window with no
  identifiable patient; this is a still from it. The page needed one moment that touches
  both edges of the screen.

All three graded through `tools/grade.sh` (`clean` for light bands, `clean-deep` for the
band) so they sit in the same treatment as everything else (D-009, D-011).

**2 images → 16.** The text-heavy complaint was never really about word count after
D-031; it was about there being nothing to look at between the words.

---

## D-033 — The surgeon block earns its place or it goes; the biography goes to /about

**Client, correctly:** the surgeon section "is a bit not on point with the rest of the
page… better on the about page." It was. The Navy base, the Harvard lab, the
Post-Gazette quote — that is a biography, and dropping one mid-scroll interrupts someone
who is trying to work out whether they are a candidate for an abdominoplasty.

**Cut, not deleted.** §5.3 still wants the surgeon on the page and §5.4 wants trust above
the fold everywhere, so the block was rewritten around the one verified thing about him
that *is* on-topic for this page: **"the quality of your healing after surgery"** — his
own words, from the transcript in `facts.md`, and the strongest differentiator in the
project. The page already devotes an entire section to recovery; this is the argument for
why that section exists.

**Moved to sit against the recovery timeline** rather than interrupting the operation →
candidacy sequence, and re-grounded to `ink-2` so the light run does not lengthen. Both
photographs stay — losing them would undo the point of adding them. The biography lives
on at `/about` behind "More about him".

## D-034 — Two harness bugs meant the accessibility audit was checking half the page

Both found while fixing D-033, and both invalidate earlier "0 violations" claims.

1. **axe skips invisible nodes.** Every `[data-reveal]` block sits at `opacity:0` until
   IntersectionObserver fires, and axe never scrolls. So the audit had been silently
   ignoring most of the page. Forcing `.is-in` before the run immediately surfaced a real
   **1.78:1** failure: the three-problem cards moved onto the dark ground when D-031
   merged them into the operation section, and their colours did not move with them.
2. **axe sampled colours mid-transition**, reporting a phantom 4.35:1 on the talks card
   while it was still fading in. `tools/axe.mjs` now disables transitions and animations
   before auditing.

**Lesson worth keeping:** a reveal-on-scroll pattern makes a page invisible to any
automated audit that does not scroll. Anything that hides content by default must be
force-shown in the harness, or the harness reports on an empty page. The same bug had
already produced a misleading contact sheet (D-030).

## D-035 — The diagrams are placeholders, and saying so is the useful move

They are hand-authored SVG paths. Anatomically defensible, on-grid, correct colour
behaviour — and visibly not commissioned. Uniform stroke weight, schematic anatomy, and a
front view that cannot show skin overhang (which is the whole point of A1).

Written `design/illustration-brief.md`: the four required states per procedure, the SVG
spec the pinned-plate interaction depends on (`currentColor`, named `data-l` groups,
shared viewBox), the register with references and anti-references, where to hire, and
realistic cost.

**Check first:** the thumbnail on his own "Tummy Tuck Master Class" video contains a real
anatomical diagram. Someone drew it for him. That person is the cheapest path and would
make the site match his video content — worth one question before spending anything.

---

## D-036 — "Three problems" and the step list were the same content twice

**Client:** *"for the steps and the operations in order isn't that kinda repetitive?"*
Yes. The three diagram cards were **Skin / Muscle / Fat**, and steps 3, 4 and 5 were
*skin and fat removed / muscle wall repaired / liposuction*. Same three facts, stated
twice, ten centimetres apart, each with its own illustration.

**The cards are gone.** Each step now carries its own reason in its own sentence — step 2
explains why loose skin does not retract, step 3 explains what diastasis recti is. Six
steps instead of seven (anaesthesia folded into the lede, since it has no visual). One
sequence, one set of marks, no restatement.

## D-037 — Stopped hand-drawing anatomy; drew a mark system instead

Two attempts at anatomical illustration, both abandoned, and the reasoning is worth
keeping because it will come up again on the other ten procedures:

1. **Front-view torso.** The suture rungs read as a corset and the silhouette read as a
   skirt. Worse, a front view **cannot show skin overhang** — which is the single thing
   the first diagram exists to show.
2. **Side profile.** The flattening profile was a genuinely good idea — you *see* the
   belly contour cross-fade flat — but the silhouette read as a trouser leg. Correct
   proportions on a human form is exactly the skill I do not have.

**So the marks stopped being anatomy.** Six purpose-drawn geometric marks on a 48px grid,
one per step, each animating the motion it describes: the incision **draws itself**, the
skin band **lifts away and the gap closes**, two rules **converge and are stitched**, the
flanks **come in**, the navel **travels up its guide**, the line is **stitched closed**.

This is not the icon soup §4 bars. Nothing is borrowed from a library, every mark encodes
its step's action rather than labelling it, and it is precisely what `ASSET-REQUEST.md`
S1 asks for — "custom line, single weight, 24px grid, `currentColor`". Pure geometry is
also something I can execute at real craft, where human anatomy is not.

**Plus a progress meter** in the pinned column — a filling rule and `03 / 06` — so the
sequence has a sense of position. Motion is transform and opacity only, all of it
disabled under `prefers-reduced-motion`, and the page scrolls normally throughout;
nothing is pinned to the wheel.

**The commissioned anatomical set is still worth buying** — `design/illustration-brief.md`
stands. But the page no longer *depends* on it, which was the real problem.

---

## D-038 — The hero "jump" was a cut in the source, and the loop wrap was a second one

Reported as "a weird jump in the last second." Two separate defects, neither where it
looked like it was.

**One: a hard cut inside the footage.** Scene detection on `assets/hero video.mp4` finds
cuts at 2.53 / 5.10 / 6.40 / 8.77 / 10.53 / 13.03 / 15.63 / **17.47**. Our tail clip ran
16.2 → 18.95, so it crossed 17.47 — the wide two-shot snaps to a tight punch-in
mid-clip. Tail now ends at **17.40**, just before it.

That also fixed something the crop was costing us: in the punch-in the top of his head is
outside the frame. §5.3 says the surgeon is the product, so the wide framing where his
face is visible is the one worth keeping regardless.

**Two: the loop wrap.** The clip ended on a bright white studio shot and cut straight back
to a dark clinical one. The tail is now dissolved into the head — `[tail][head]xfade`
before `concat` — so the wrap is continuous.

The two dissolves then had to be **de-conflicted**. The first attempt overlapped the A→B
dissolve with the loop dissolve for 0.4s and triple-exposed three shots at once. With
`lenB = 1.2`, a clean sequence requires `lenB - D >= dur`; A→B is now 0.5 and the loop
crossfade 0.7, so they abut exactly and only one dissolve ever runs.

**Result:** 14.56s → **12.32s**, 1.95MB → 1.67MB mp4. Poster regenerated from the new
first frame so nothing flashes on load. Rebuild with `tools/hero-cut.sh`.

---

## D-039 — Mobile gets its own 9:16 cut, because one object-position cannot serve seven shots

`object-position` was the wrong tool and no value was going to fix it.

A 9:16 container shows about **32% of a 16:9 frame's width**, so the crop column *is* the
composition. And the hero is not one shot — it is **seven**: three marking setups, a white
studio two-shot, a chairside, a desk, and the result. The surgeon sits somewhere different
in each. `22%` centred him at the desk and dropped him out of the marking shots entirely,
leaving a woman's torso in underwear as the opening frame of a surgeon's website. `42%`
fixed the desk and broke the studio. There is no single winner.

So mobile is served a **purpose-built portrait render** (`tools/hero-cut-mobile.sh`) that
crops each shot on its own column — 0.28 / 0.30 / 0.28 / 0.52 / 0.362 / 0.312 / 0.46. The
crop only ever changes on a scene cut, where it is invisible.

Two constraints fell out of testing. The opening shot is also the poster and the LCP
frame, so it is cropped to keep **his profile dominant and no bare torso in it** — pushing
it right made a better picture of the surgery and a worse first impression of the practice.
And `object-fit: cover` still shaves ~7% off each side of the portrait render inside the
section, which clipped his head in the studio shot until that column moved 0.45 → 0.52.

**Delivery:** `media` on `<source>` is only honoured inside `<picture>`, never inside
`<video>`, so the cut is chosen by six lines of inline JS instead. That also means the
unused render is **never downloaded** — mobile pulls 438KB instead of 846KB, on the
connection that can least afford it. The poster uses a real `<picture>` with `media`.
Reduced-motion skips the video entirely and the poster stands.

---

## D-040 — Credential marks: cropped, never recoloured, and not publishable yet

The three supplied PNGs are 1080×1350 with the mark adrift in white space.
`tools/trim-badges.py` finds the content box (ignoring transparent *and* near-white
pixels), adds 3% breathing room, and exports 1x/2x.

**Nothing is recoloured.** Turning certification marks into single-ink silhouettes would
sit better with §4, but ABPS and ASPS both publish usage terms forbidding alteration of
their marks. Restraint has to come from size, spacing and the surrounding whitespace
instead — which is why the strip is three marks and one sentence on paper, nothing else.

The ACS mark is a **photographed bronze medallion**, not a flat logo, so it carries more
visual weight than the two vector marks beside it; it is set slightly larger so the three
read as one row rather than two small logos and a coin.

**These cannot go on a public URL yet.** `facts.md` has ABPS as *asserted, not verified*,
and FACS and ASPS both still `[[VERIFY]]`. A displayed certification mark is a claim
(§2, §3). Gated preview and pitch deck only until the ABPS/ABMS, FACS and ASPS directory
checks come back.

---

## D-041 — White marks, and a marquee that can be stopped

**White is the one alteration the boards generally allow.** D-040 refused to recolour the
certification marks, and that still holds for arbitrary colour — but an all-white
*reverse* version is standard in most brand guidelines, because it is how a mark is meant
to sit on dark ground. `tools/white-badges.py` derives one by taking alpha from how **dark**
each pixel is rather than from its alpha channel, so the internal shapes survive instead
of collapsing into a silhouette — which matters most for the ACS medallion, a photograph
of a bronze relief that a flat silhouette would destroy. Per-mark gamma lifts the ASPS
ring, a mid-tone teal that otherwise washes out next to black text.

**Still request the official reverse artwork before launch.** A derived mark is a
reasonable stand-in for a pitch; it is not what should ship.

**Placement: the foot of the hero.** §5.4 wants trust signals above the fold, and the
bottom edge of the film frame is the only place they fit without competing with the
headline or the CTA. A hairline and a soft gradient seat the strip into the frame rather
than stacking a separate band under it.

**Sizing was the real work.** At 50px the marks were unreadable and the medallion was a
grey smudge — a trust bar nobody can parse is decoration, not a trust signal. They now run
46–70px (medallion 54–80px, since a photographed seal needs more height to hold its own
beside two vector marks).

**SC 2.2.2 required a stop.** Content that moves for more than five seconds needs a
pause mechanism, so the strip carries a small always-present, always-focusable pause
toggle. Hover pauses too, and `prefers-reduced-motion` drops the animation and the edge
masks entirely and shows a static row. Verified: 0 axe violations at 1440 and 390.

Only three marks exist, so the track is duplicated and translated -50% for a seamless
loop; the duplicate set is `aria-hidden` so screen readers hear each credential once.

---

## D-042 — The proof row: no invented number, and the faces come from the one released source

Asked for a stat block above the headline — "over 10,000+ clients helped" — with circular
faces pulled from the reels or YouTube. Built, with two substitutions.

**The number is not invented.** `facts.md` records procedure volume as *"none stated
anywhere on the current site"*; the only floor we have is 68 documented before/after
cases. A patient count on a physician's site is a claim under FTC 16 CFR 255 and Florida
medical-advertising rules, and §2 bars a plausible guess outright. The row therefore runs
the one large number that is **verified** — **148,000** Instagram followers, from the
Linktree/profile capture on 2026-08-20 — phrased as what it actually measures: *people
follow his work*, not people operated on. The moment he supplies a real procedure count
it is a one-line swap.

**The faces are not from the reels.** The reels are almost entirely before/after torsos,
lingerie and surgical fields; there are barely any faces, and the few there are belong to
patients mid-result. Beyond the framing problem there is a consent one: a release covering
a result video does not extend to cropping that patient's face into a social-proof token
beside a number, which is closer to an endorsement. The three avatars are cut from
**`assets/hero video.mp4`**, the one source where the client confirmed signed releases
(2026-08-23), graded `clean` to match everything else.

**It replaces the eyebrow rather than stacking above it.** Two small lines above the
headline is clutter; the byline already carries Miami, and proof earns that slot better
than a location label.

Two bugs found on review: `font-variant-numeric: tabular-nums` gave the comma a full digit
slot and rendered "148,000" as "148 , 000" — tabular figures are for columns, not for one
number inside a sentence. And the narrow mobile strip put the marquee's fade almost on top
of the pause button; the mask now closes at 82%.

---

## D-038 — The talks card kept getting buried; it now lives in the pinned column

Third time of asking. It had its own numbered band (D-029), was demoted to an `<aside>`
when nine sections became five (D-031), and ended up at the tail of the longest section on
the page after the operation rebuild (D-036) — below six steps *and* below the one-litre
statement, with no page-index entry.

It now sits **inside the pinned left column, under the progress meter**. That fixes it
three ways: it is on screen for the entire six-step sequence rather than after it, it
fills the dead space the sticky column had, and on mobile the column is static and appears
*above* the steps, so it arrives early. Restyled compact — no bordered card, just two rows
under a label.

## D-039 — Video testimonial slots ship as honest empty states

**He has no patient video for this procedure.** All 202 uploads searched: the only patient
stories are Katherine Fox (burns reconstruction, 36:33) and Luciana Maldonado (implants,
43:26) — both Spanish, both other procedures, both requiring releases.

So the section carries **three 9:16 slots at the real aspect and the real count**, drawn
as unfilled frames: hairline grid, dashed border, slot number, and the caption that would
sit under each. §3 requires building against placeholders so layout and loading are
genuinely exercised — and an honest empty frame is a clearer ask than a mock-up he has to
decode. A stock face presented as a patient is barred outright, so a fake poster was never
an option.

Each slot carries the question it should answer — *"Why I waited four years", "What the
first week was actually like", "He told me no the first time"* — and the ask is stated on
the page: **three 45-second clips, one afternoon.** Those are the prompts, not a script.

## D-040 — The recovery timeline reads as operable

It was a row of 1rem circles above labels. Nobody could tell it did anything.

It now has a **rail that fills to the current milestone, a draggable handle, and a hint
line** ("Drag the handle, or pick a milestone"). Pointer-drag anywhere on the axis snaps
to the nearest milestone; the handle scales on hover and grip.

**The drag is a layer on top, not a replacement.** Underneath it is still a `tablist`:
arrow keys, Home/End, roving `tabindex`, one visible panel, and every milestone reachable
without a pointer. Drag calls the same `select()` the buttons do. The rail is positioned
from measured tick centres, so it repaints on resize and on the mobile axis scroll.

### D-039 amended — one slot is real

Client: *"you used to have one before."* Correct, and I had dropped it. The page carried a
playable 9:16 Instagram reel in the technique column until D-029 replaced that slot with
the YouTube talks list; the asset was never removed from `src/public/video/reels/` (seven
reels, posters included) — it just stopped being referenced.

**Slot 01 is now that reel**: `tummy-tuck-bbl.mp4`, 11s, self-hosted, poster until clicked,
muted and looping. **Labelled for what it actually is** — *"A result, in motion · From his
Instagram"* — not dressed up as a testimonial, because it isn't one. Slots 02 and 03 stay
as empty asks, and the ask on the page dropped from three clips to two.

Worth noting for the other ten procedures: six more reels are sitting unused
(`bbl-lipo-360`, `skinny-bbl`, `breast-augmentation`, `breast-aug-natural`,
`bbl-breast-lift`, `lipo-breast-aug`). Every one of those pages can open with a real
filled slot the same way.

---

## D-043 — The published hero was 3× the size I signed off on, and my check couldn't see it

Reported as a design failure on desktop: enormous type, broken spacing, an uppercase
byline, a raw underlined link. It was none of those things locally. It was a build bug,
and the check I had written could not have caught it.

`tools/build-artifact-headlines.py` strips the document scaffolding with
`re.sub(r"^.*?<body>", "")`, because the Artifact wrapper supplies its own. But
`hero-headlines.html` kept its headline settings in a `<style>` block **in the head** —
so every publish silently deleted `.h--two`, `.hA__by`, `.hA__more` and `.hA__eye`. The
hero fell back to the base `.hA h1` rule, `clamp(3.2rem, 1rem + 8.4vw, 10.5rem)`, and
shipped at roughly 150px. There was even a line in the builder that *looked* like it
preserved the block — `re.sub(r"<style>.*?</style>", lambda m: m.group(0), html)` — which
substitutes the match with itself. A no-op that reads as a safeguard is worse than no
safeguard.

**Two fixes, one structural.** The page-level CSS moved into `hero-options.css`, where
CLAUDE.md §6 says style values belong. Nothing lives in a document head that a build step
can drop.

**And the check got teeth.** `tools/artchk.mjs` used to assert "no console errors", which
was true the whole time the hero was 150px — a page with no stylesheet throws nothing. It
now loads the built artifact **and** the dev page side by side and diffs computed values:
headline px, line count, byline `text-transform`, the proof row, avatar and mark counts,
the pause control, and the loaded video width. Any drift fails with a non-zero exit.

Confirmed matching at 1440 and 390 — headline 46px / 2 lines desktop, 27px / 2 lines
mobile. **The lesson is the general one: verifying the source and shipping the build are
two different claims, and I reported the first as if it were the second.**

---

## D-041 — Every placeholder removed, by deletion rather than invention

Client: *"remove any placeholders, can't have those there."* Done — and the important part
is **how**. §2 forbids replacing an unverified fact with a plausible guess, so removing a
`[[VERIFY]]` meant deleting the content it was holding open, never filling it in.

| was | now |
|---|---|
| Case metadata `[[VERIFY: months]]` | Row deleted. Two verified rows remain. |
| Recovery Day 5 `[[VERIFY: when drains come out]]` | Row deleted. |
| Candidacy `[[VERIFY: nicotine-free window]]` | Item kept, window dropped — "Nicotine is disqualifying, not discouraged" is true without the number. |
| Risks `[[VERIFY: complication rate]]` | Clause cut; the risk still stands. |
| Risks `[[VERIFY: revision policy]]` | Replaced with a true instruction, not a claim: *"Ask what that costs before you book, not after."* |
| FAQ `[[VERIFY: pain protocol]]` | Clause cut. |
| Cost `[[VERIFY: price band]]` | **No number shown at all.** The block became "what it costs" — the six things every quote is built from, plus advice to ask for it itemised. Every line true, nothing invented. |
| Three placeholder testimonials + note | **Section deleted.** §3 D2 offered "signed releases, or a decision to ship none" — this is shipping none. |
| Two empty video slots | Deleted with the section. |

Verified by reading rendered `innerText` for `VERIFY / Placeholder / Slot / Awaiting` —
**none.**

**The one note deliberately kept** is the private-preview warning over the case gallery.
Not a placeholder — a live constraint, since real unreleased patient images are on the
page. Reworded from an internal reference to site copy: *"Private preview — these cases
are not cleared for public display."* It comes off when releases exist, not before.

## D-042 — Video moved up

The reel was sitting after Recovery, two thirds down. It is a **result**, so it now sits
in the Results section directly under the case filmstrip — second section on the page,
paired with a line about why motion shows what stills cannot. Self-hosted, poster until
clicked, no third-party request.

Three playable videos remain, all above the halfway mark: the reel in Results, and his two
YouTube talks in the operation section's pinned column.

**Cost of the placeholder purge: 1,758 → 1,657 words, 13,342 → 12,201px.** The page lost a
whole section and reads tighter for it.

---

## D-044 — The marquee comes out of the hero; the marks go where they mean something

The rotating strip was the wrong instinct and it looked it. Two reasons it failed, worth
recording so the pattern is not reached for again:

**Three items is not a marquee.** With only three marks the loop repeats every few
seconds, so the eye registers *motion* rather than *credentials* — and the pause control
SC 2.2.2 forces onto any long-running animation put a small piece of UI chrome into a
hero that was otherwise pure film frame.

**And the hero was the wrong argument for them.** The hero's job is the claim; the marks
answer "is he actually qualified", which is the About section's question. Moved into the
existing `.creds` block under a **Certification** label so they sit on the same rhythm as
Residency / Research / Recovery protocol, reading as one more credential rather than three
logos floating in a band. Colour versions here, on paper — the derived white reverses
(D-041) are no longer used anywhere and stay unshipped, which also retires that risk.

**Portrait:** swapped to the transparent cutout, composited onto a flat `--paper-2` panel
at 4:5. Shipping the PNG with its alpha would have cost 2MB; compositing onto a flat token
colour is visually identical and lands at 67KB webp. The previous portrait carried a
printed ABPS badge inside the photograph, which was doing the marks' job less well and is
now redundant.

**The note replaces the pull quote.** First person, per the voice rule in D-0xx — he
speaks, the site supplies the receipts.

> ⚠️ **The note is PROPOSED copy, not a quotation.** It is written in his voice and signed
> with his name, which reads as something he said. It must be read and approved by
> Dr. Alvarez before launch. Flagged in `content/facts.md` and in an HTML comment beside
> the markup.

**No signature was drawn.** There is no signature asset anywhere in the project — I looked.
A fabricated signature on a physician's site is forgery, not decoration, so the slot
carries a literal `[[VERIFY: signature scan]]`, consistent with the
`[[VERIFY: accreditation]]` already sitting in that block. In a pitch this is an asset —
it shows him exactly what we need from him.

Both artifacts now verify against dev with `tools/artchk.mjs` and `tools/homechk.mjs`
(D-043); 0 axe violations at 1440 and 390.

---

## D-043 — One mark language, extended across the page

Client: *"a lot of these can be symbols to add some personality, it's so text heavy."*
The timeline was the obvious place — `MOVEMENT / WASHING / DRIVING / SUPPORT` are exactly
the labels a reader scans rather than reads.

**Fourteen marks, drawn on the same 24px grid as the six operation marks** (D-037), so the
page has one symbol language rather than two. Nothing from an icon library — §4 bars that,
and a borrowed set would not have matched the operation sequence anyway.

Applied to the **recovery fact labels** (23 instances across the eight milestones) and the
**hero fact rail**, which was the other dense text strip. `m-work`, `m-support` and
`m-result` are reused between the two, which is what makes it read as a system.

**Two were redrawn after seeing them at size:** "movement" read as a pin (now a dashed
travelled path with direction) and "intimacy" read as a loading spinner (now two
overlapping circles). "Scar" deliberately echoes the operation set's closing mark — a line
with cross-ticks — so the same idea looks the same in both places.

**Two SVG traps worth recording:**

1. `<use>` needs a `viewBox` on the *referencing* `<svg>`, not just the source. Without it
   every mark rendered clipped to a corner.
2. **CSS cannot style into a `<use>` shadow tree** from a rule scoped to the sprite. The
   marks all rendered as filled black silhouettes until `fill="none" stroke="currentColor"`
   moved onto the source `<g>` elements as *presentation attributes*, which do get copied
   into the shadow tree. `currentColor` still resolves against the `<use>` site, so one
   sprite serves both the cream and the ink grounds.

The sprite sits at the top of `<main>`, not inside the recovery section where it started —
the hero references it, and nothing should depend on a section further down the page
existing.

---

## D-045 — Real quotes replace our copy; the five-point list goes; the marks move again

**The note is now something he actually said.** D-044 shipped a first-person note we had
written and flagged it as needing his approval. That flag is now moot: it is replaced with
his own line from his introduction video — *"I'm integrating all that knowledge that is
going to benefit you — to improve the quality of your healing after cosmetic surgery"* —
attributed on the page as *From his introduction video*. Our words came out.

**A second real quote carries the biography.** The Post-Gazette (2019, PRIMARY) line —
*"They told me I could become a surgeon. I could become a researcher, and maybe a
businessman. … I have become all three"* — sits directly under the paragraph about the
research years, attributed to the paper. It does the researcher-then-surgeon positioning
in his voice instead of ours, which is the whole argument of the section.

Its measure needed scoping: the global `blockquote.pull` is tuned to 26ch for a narrow
column and broke into five stubby lines in About's wide one. Overridden to 36ch above
64rem only.

**The five-point credential list is gone.** Residency / Research / Recovery protocol /
Preparation / Surgical facility restated what the body copy had already said, and one of
the five was a `[[VERIFY]]` placeholder — a row of facts where a fifth of it is an
admission of missing data reads as thin, not thorough.

**The marks moved under the portrait.** They belong to *him*, not to a band at the foot of
the section: hairline, **Certification** label, three marks, directly beneath the photo.
Third placement and the right one — hero (wrong argument), section footer (floating in
whitespace), portrait column (attached to the person they describe).

**Signature: shipped, ink.** Client supplied `assets/signature.png` — a scripted logotype
in orange. Retinted by replacing RGB and preserving the source alpha, so the stroke
antialiasing survives. A teal `--accent-light` variant was built and rejected: on paper it
read as decoration, where the near-black reads as a signature. The `[[VERIFY]]` slot is
retired.

---

## D-044 — Candidacy became a click-through; the mark set reached 23

Client: *"do more symbols… or do fun click throughs on some, just overall make it less
overwhelming. almost there."*

**Candidacy was the densest block left** — two columns, eleven prose items, all on screen
at once. It is now **five checks, one at a time**, each card carrying *both* sides:
"likely a candidate" beside "he'll ask you to wait". The honest turn-them-away content
survives intact; it just stops arriving as eleven paragraphs.

Same tablist contract as the recovery timeline — arrow keys, Home/End, roving `tabindex`,
one visible panel — plus prev/next and a position counter. Reusing the pattern means the
two interactions on the page feel like the same object.

**Nine more marks**, same 24px grid: five for the checks (skin, gap, scale, family,
no-nicotine) and four for the booking steps (form, calendar, mail, check). **23 defined,
43 used** across hero rail, operation steps, recovery labels, candidacy and closing.

**Repeat bug, caught before shipping:** the candidacy cards shipped with `hidden` in the
markup, so with JavaScript off four of five would have been unreachable — exactly the
fault fixed for the timeline in D-027. Cards now ship visible and JS hides them on init.
`tools/rm.mjs` gained a `visibleChecks` assertion so the no-JS state of *both* components
is verified on every run, rather than remembering to check by hand.

Page height 12,201 → **11,986px** despite gaining nine marks and an interaction.

---

## D-046 — The homepage About becomes quote-led; the biography moves to /about

The heading, the lede and the research-years paragraph are now reserved for the full
About page and live in `content/about-page.md`. What is left on the homepage is the thing
the homepage is actually for.

**Why it is better, not just shorter.** The old heading — *"Your result depends on how you
heal"* — was arguing the same case as the hero, which now opens with *"Any surgeon can do
the operation. What happens after is what matters."* Two statements of one thesis, three
scrolls apart, in our voice both times. Cutting the second one costs nothing and lets the
section do a job no other block on the page does: **hand the argument to him.**

So the homepage block is now `In his own words` — portrait, certification marks, two
verbatim quotes, his signature, and a link through to the story. §5.3 says the surgeon is
the product; this is the only place on the page where he speaks.

**The quotes now read as quotes.** Real `\201C`/`\201D` marks, hung into the margin with a
negative `text-indent` so the text edge still aligns optically. The healing quote steps up
to `--t-3` — with the biography gone it is the section's lead element and carries the
weight the heading used to.

**The link changed target.** `/preparation` → `/about`, since that is where the copy went.

`content/about-page.md` also carries what still has to be written for that page — the
Colombia-to-Miami arc, the book, the team — plus two publishable Post-Gazette quotes not
used anywhere yet, so none of it gets lost.

---

## D-047 — Homepage reorder: Instagram was interrupting the argument

`hero → results → instagram → about → procedures → reviews → location`
became
`hero → results → about → procedures → reviews → instagram → location`

**Instagram at #3 was answering a question she had not asked yet.** She has just scrolled
68 before-and-afters. The next thing in her head is *"who did these?"* — and the page
handed her more results, in a second format, before telling her who he is. Reels are
momentum and volume, not a decision input; they belong after she has a reason to care.

**About moves to #3** to take that slot: she has seen the work, now she meets the person
who did it (§5.3). It also breaks a run of three consecutive dark sections — hero, results
and procedures were stacking `--ink` on `--ink` on `--ink`.

**Procedures to #4** — with the surgeon established, *"which one is mine"* is the right
next question, and it is the SEO hub that links out to the per-procedure pages (§5.7).

**Reviews #5**, peers confirming what she has just decided to believe. **Instagram #6** as
proof he does this daily. **Location #7**, practical, nearest the close.

Verified: order asserted in `tools/homechk.mjs`, one `<h1>` and no skipped levels,
no horizontal overflow at 1440, 0 axe violations at 1440 and 390.

---

## D-045 — The page opened with three dark bands, then flipped

Client: *"it starts off super dark then gets light with the background."* The sequence was
**ink · ink · ink-2** · paper · ink-2 · paper · image · paper-2 · ink-2 · ink — a heavy
front-loaded block, then alternation.

**Results moved to the cream ground.** Now: dark · light · dark · light · dark · light ·
image · light · dark · dark. Every band changes.

It also suits the work better. His case composites are **black-backed**, so on cream they
read as framed plates with real edges; on the dark band they dissolved into it. D-022 put
the homepage gallery on dark for exactly that native-fit reason — on a procedure page,
where one case fills the container, the opposite is true.

Cost: about twenty light-ground overrides for `.pcase*`, scoped compound
(`.p-sec--paper2.pcase`) since `.pcase` sits on the section element itself — the same trap
as D-033's `.psurg`.

## D-046 — The page index is now a navigator, not a caption

Client: *"make the category selector more obvious and easy to navigate, so people actually
use them."* Fair — it was 11px uppercase links on `paper-3`, a ground barely distinct from
the sections either side. It read as a label.

- **Numbered** `01`–`06`, so it reads as a contents list with a knowable length
- **Real hit areas** — `--t--1` at full padding instead of `--t-eyebrow`, with a hover
  background so the target is felt before it is clicked
- **Active state that carries** — ink text, accent numeral, 2px accent underline
- **A reading-progress line** across the whole bar, filling with scroll position
- **The CTA became a filled button** rather than a text link at the end of a row

Two bugs on the way. The numerals sat at `--rule-on-light` — **1.48:1**, a serious
failure, since a sequence number is content. And `.pidx a` (0,1,1) out-specified
`.pidx__cta` (0,1,0), so the CTA rendered dark-on-dark and was invisible; it needs
`.pidx a.pidx__cta`. Both are the same lesson as D-033: **an element-plus-class selector
beats a lone class, and lone-class overrides fail silently.**

---

## D-048 — Footer, and /about built from the Post-Gazette record

**Footer.** Four columns — Visit (full NAP), Explore, Procedures, Follow — over a legal
base. Deliberately included:

- **The book, in both languages.** A published patient-education guide is a first-rank
  trust signal and it appears nowhere on his current site.
- **A medical disclaimer.** *"Individual results vary. Nothing on this site is medical
  advice or a guarantee of outcome."* Standard for the vertical, and it is the compliant
  counterweight to a page full of before-and-afters.
- **TikTok omitted.** `facts.md` records two different handles from two sources and cannot
  resolve which is live. A dead social link in a footer is worse than an absent one.
- **Hours as a visible `[[VERIFY]]`.** Not in `facts.md`, so not invented.

The footer is copied verbatim into `/about` rather than retyped, so the NAP cannot drift
between pages — §5.7 depends on it being byte-identical.

One bug on the way in: a blanket `.ft a{color:inherit}` overrode the CTA's own colour and
dropped it to **1.49:1** on the accent fill. Scoped to `:not(.btn)`.

---

## /about

The long-form page the homepage now teases. Built entirely from the **Pittsburgh
Post-Gazette (2019)** profile — named reporter, direct quotes, contemporaneous — which is
the only PRIMARY source in the project and is dramatically better material than anything
on his current site.

**The timeline is the page.** Bogotá → a Colombian Navy base → Madrid → Boston →
Pittsburgh → Miami, dated. The numbering is structural, not decorative: this is a route
with a real sequence, and the dates carry information the reader needs.

Three details do the persuading, and all three are his, not ours: **180 babies delivered**
in the Navy year, **four months unpaid** to hold the Harvard lab position, and the line
*"None of the other lab members wanted to move to Pittsburgh."* Specificity beats
superlatives — and superlatives are barred anyway (§3).

Two Post-Gazette quotes that had never been used anywhere are now placed where they land:
the one about embracing difference sits against the Boston years, and *"I have become all
three"* sits against the residency.

**The unresolved gap is shown, not hidden.** The final timeline row is *Today — Miami,
Florida* followed by a visible `[[VERIFY]]`: nothing documents when or why he left
Pittsburgh. In the pitch that row is useful — it shows him precisely what only he can fill
in.

Two bugs found: `.vh` lived in `hero-options.css`, which /about does not load, so the
section label rendered at 43px — moved to `styles.css` where every page gets it. And the
homepage was marking `/results` as `aria-current="page"`.

Verified: one `<h1>`, no skipped heading levels, no horizontal overflow, artifact matches
dev at 1440 and 390, 0 axe violations on both pages.

---

## D-047 — Procedure hero: deferred, current treatment stands

Four directions were built and reviewed (A editorial plate · B full-bleed photo · C
full-bleed video · D vertical reel). Client: *"I think I'll leave it how it is for now."*

The existing split hero stays. The comparison page is kept at `src/public/_hero-ab.html`
for when this is revisited — now carrying `noindex` and a comment marking it as scratch to
be deleted before any deploy.

**One thing does not stay deferred.** Rendering direction C surfaced that the deployed
homepage hero video contains identifiable patients, contradicting what
`ASSET-REQUEST.md` records. That is a §3 problem, not a design preference, and it is
written up there as a blocker with a verified safe re-cut
(`hero-clean-1920.mp4`) sitting ready. The homepage was **not** changed — approved work,
and the swap is the client's call.

---

## D-049 — Three pictures that were already in the folder

An audit of `src/public/img` against the markup found images processed weeks ago that
nothing referenced. The team photograph is the one that matters.

**The team photo.** `/about` named Liliana Clavijo and Valentina Sanchez and showed
neither, while a photograph of all three of them sat in `assets/Headshots/professionals`
under the filename `imgi_3_about-us-banner-desktop.jpg`. It now carries its own section —
*"You will see the same three people every time"* — which turns practice size from an
apology into the argument it actually is: the person who answers the phone knows your
name, and the surgeon who consulted you is the surgeon who operates.

**The consultation frame** (`consult-1200`) was built for a full-bleed band that no longer
exists and had been orphaned since. It now sits under the *"Ten years in a laboratory"*
heading, where a photograph of him actually consulting is the literal illustration of the
claim.

**The interview shot** was recropped **3:2 from the 1080×1350 original** rather than reusing
the existing 4:5 derivative — portrait stood far too tall beside the timeline heading and
forced a column of dead space. It sits beside *"The route here."*

Two things caught in review. A `<source type="image/webp">` pointed at a **JPEG**, which
only survives because browsers sniff. And I captioned the interview *"Interviewed in Miami,
2025"* — a plausible guess of exactly the kind §2 bars. The caption now states only what
the photograph shows and asks for the rest.

Also: a `.replace()` in the patch silently no-opped because the source text wrapped
mid-sentence, leaving `.ab-arc__top` unclosed — the whole timeline became its second grid
child and collapsed into a narrow column. Asserting on the anchor rather than trusting the
replace would have caught it at write time, not at screenshot time.

**Still unplaced:** `jc-office-*`, a 2048×1365 studio portrait, and a warm interview still.
Logged in `MANIFEST.md` rather than left to be rediscovered.

---

## D-048 — Second procedure page: Brazilian Butt Lift

Built from the tummy tuck template. **What changed is only content**; every component —
case stage, six/five-move sequence, candidacy checks, draggable timeline, talks card,
mark set — carried across untouched. That is the template working.

**Asset coverage is the best of the eleven:** 9 cases, a graded header, 3 reels, and a
deep YouTube shelf.

**The lead talk is `U4MFTb2al-U`, "BBL Proportions: Why Less is More" — 8:36, and
English audio**, which is rare on his channel. It is also exactly the §4 argument: his own
recorded case against volume, on the page that most needs it. The Spanish
"Everything Nobody Tells You About Fat Transfer" (11:01, 3.6K views) sits under it.

**Safety is handled as a question, not a claim.** BBL's defining objection is mortality,
and the honest treatment is that the risk turned on one technical decision: fat placed
above the gluteal muscle, never into it. The page states that, names fat embolism in the
risks, and frames it as *"Ask where the fat goes — it is the first question to put to any
surgeon offering you one."* That is true, useful and verifiable, and requires no
unverified claim about his own technique.

**His blog's "1 in 10,000" fat embolism figure was not carried over** — unsourced, and §2
does not allow publishing a statistic we cannot trace.

**Two positions of his own got promoted to statements**, both from his site and both
unusual enough to be worth the space: *"He will not combine this with a tummy tuck"* and
*"It is not about volume. It is about proportion."* A surgeon publishing what he refuses
to do is the §4 thesis working harder than any superlative.

**Five new step marks** — harvest, purify, place, proportion, compress — animating their
own motion in the established language. The recovery timeline is his own BBL chart, and
the sitting restriction is called out as the thing people underestimate.

**JSON-LD rewritten, not inherited** — `MedicalProcedure`, `Physician`, `BreadcrumbList`
and a `FAQPage` whose six questions match the six on the page exactly. Schema that
disagrees with visible content is worse than none.

Verified: axe 0 at 1440 and 390, no horizontal scroll at 320/390/720, reduced-motion and
no-JS both pass, every interaction smoke-tested, no 404s and no console errors. Tummy tuck
re-audited after the shared-CSS additions: still clean.

---

## D-050 — The book gets a section, not a link

`facts.md` has recorded since 2026-08-20 that a two-language patient-education book is
*"absent from his homepage, his About page, and every procedure page"* — a first-rank trust
signal his own site throws away. It was two text links in a three-up column; now it is a
section with the cover.

**Why it converts.** The subtitle is *"the definitive guide to safe and satisfying plastic
surgery."* That is fear #3 in the conversion doctrine, answered by the surgeon having
literally written the book on it. No competitor in Miami can copy that.

Headline: *"He wrote a book so you would not have to take his word for it."* — the argument
is that he published his reasoning where anyone can check it, which is the same move as
naming the risks out loud.

**Design — rejected once, then rebuilt.** The first attempt was a product listing: the
cover blown up to ~500px so it read as merchandise, a `[[VERIFY]]` chip dropped into the
middle of the layout, and the same image-left/text-right split used by the two sections
directly above it. Three sections running one template is how a page starts feeling
generated.

Rebuilt: **a book is a small object.** The cover now sits at roughly its real size
(19rem max) top-right, with a 1px hairline instead of a drop shadow (§4) and no faked 3-D
mock-up. The section leads with a full-width rule under the eyebrow, gives the display
headline the room to be the biggest thing on screen, and closes with the two editions as a
typographic `<dl>` — language as the term, title as the definition — rather than a stack
of links.

**The `[[VERIFY]]` came off the page.** §2 wants a visible placeholder where we would
otherwise fabricate a claim. The page states no publisher and no date, so there was no
claim to flag — it was an internal to-do sitting in a client-facing layout. It belongs in
`ASSET-REQUEST.md`, and that is where it now lives, along with the English cover artwork.

Both Amazon links were already in `facts.md` from the Linktree capture — ASIN
`B0DMTH25Q5` (ES) and `B0DMWMFVZ4` (EN) — so no new link was needed.

**A fabrication I caught in my own copy.** The rebuilt lede read *"Two hundred pages of the
reasoning most surgeons keep in the consulting room."* I have no page count for this book;
I invented a round number because it scanned well — in the same edit where I removed a
placeholder for being unnecessary. It now reads *"The reasoning most surgeons keep inside
the consulting room, written down where anyone can check it"*, which is the same idea and
asserts nothing I cannot source.

**Team section reworded.** *"You will see the same three people every time"* / *"A small
practice is not a limitation here"* was defensive — it answered an objection nobody had
raised. Now: **"Dr. Alvarez, and the two people behind every result."** Same argument, no
apology in it.

---

## D-049 — Third page: Deep Plane Facelift, the starved procedure

Chosen deliberately as the stress test: **no header photograph, no reel, and the thinnest
asset set of the eleven.** The template held. Everything that changed was content.

**The missing hero image was solved with real footage, not stock.** A 4:5 portrait crop
from **11.6s of his own consultation video** — the window already verified as having no
identifiable patient — graded `clean` and exported at three widths. It is him, at his own
desk, which is more on-thesis for a face page than any stock portrait would have been.

**Both talks are strong and one is English:** `k2Tk83CuNkU` "Face Lift – Neck lift Miami"
(19:42, English audio) over `mYXspQhkLd8` "La Verdad que Nadie te Cuenta" (25:44).

**The statement writes itself on this procedure:** *"People should notice you look rested.
Not that you look operated on."* That is the defining objection for a facelift and it is
also §4's whole thesis. The page earns it by explaining the mechanism — surface tension is
what produces the tell, and a deep plane lift takes no tension at the surface.

**A second statement handles the commonest disappointment:** *"A facelift does not treat
your skin."* Lines, texture and pigment are a separate problem, and expecting one operation
to fix both is why people are unhappy with technically good results.

**Related became a link row, not an image grid.** Eyelid surgery is the only face-adjacent
procedure with photography. Padding the grid with placeholder frames was the alternative,
and placeholders are out (D-041). `.prelrow` is now a reusable component for any procedure
whose neighbours lack imagery; the image grid returns when `PP7` is filled.

### ⚠ The face cases raise the consent stakes

The before/afters on this page are **faces**. Torsos are pseudonymous; a face is the
person. Everything in §3 applies with more force here, and if any single page must stay
behind auth for the whole spec period, it is this one. Worth raising explicitly when the
releases conversation happens (`BA3`, `D2`).

Verified: axe 0 at 1440 and 390, no horizontal scroll at 320/390/720, reduced-motion and
no-JS pass (7 milestones, 5 checks reachable without JS), every interaction smoke-tested,
no 404s, no console errors. BBL and tummy tuck re-audited after the shared-CSS additions:
both still clean.

---

## D-051 — No head-counts. The named staff are not evidence of the staff.

*"Dr. Alvarez, and the two people behind every result"* / *"the same three faces at every
appointment"* both stated a team size. `facts.md` carries **two** staff — Liliana Clavijo
and Valentina Sanchez — because those are the two his own About page names. That is not
evidence the practice has only two; a site's staff page is a marketing artefact, not a
payroll. Surgical assistants, nursing and front-desk staff routinely go unlisted.

It is the same class of error as the invented page count in D-050 and the invented patient
count refused in D-042: a number that reads as a fact but is actually an inference from
incomplete source material. Worse here, because it is trivially falsifiable — a patient who
meets a fourth person at her first appointment now knows the site is guessing.

Now: **"Dr. Alvarez, and the team behind the results."** The named list stays, because
naming who we can source is fine; asserting that the list is complete is not.

`facts.md` carries a standing note against team-size copy, and an HTML comment sits beside
the markup so the next person editing it does not reintroduce a count.

---

## D-050 — The facelift header is licensed stock, on the client's call

The client supplied `assets/Face procedures/Untitled design.jpg` — a face being marked
pre-operatively — and asked for it on the facelift page.

**I flagged it first.** §3: *"Never for a face presented as a patient, a staff member, or
a result."* A marked-up face on a surgery page reads as that surgeon's patient regardless
of caption, and I could not crop it free of the face at header resolution. **The client
confirmed to proceed, so it ships.**

**Mitigations applied, since the risk is the implied claim rather than the image:**

- Alt text is descriptive and asserts nothing — *"Pre-operative facial markings drawn
  before surgery."* Not "a patient", not "his patient", no attribution of the work.
- No caption anywhere claims it is his case. The page's actual evidence is the six
  documented before/afters, which are his.
- `MANIFEST.md` records it as **licensed stock, patient: no (stock model)** so it can
  never be mistaken for patient media by whoever picks this up next.
- Graded `clean`, so it sits in the same treatment as everything else.

**One gate left open, recorded rather than argued:** revisit before public launch. Today
the whole preview is `noindex` and access-controlled, so nothing is publicly presented as
his patient. That changes the day it goes live.

**The usable face-free crop is kept regardless** —
`src/public/img/detail/marking-{600,860}.jpg`, gloved hands and marking pen, no
identifiable face. Soft (≈2× upscale from a corner), so it is a supporting or band image
for the eyelid pages, not a hero.

Also fixed: the hero eyebrow still read "Body · Miami, Florida", inherited from the BBL
page it was built from. Now "Face".

---

## D-052 — /results, and four cases withheld because his own slides mismatch the angles

The gallery §5.2 calls the site's number-one conversion driver. Built as a real page:
**46 cases, filterable, ungated, one tap from the homepage.**

**Filtering is a conversion feature, not UI garnish** (doctrine). It writes `?p=<slug>` into
the URL, so a procedure view can be linked, shared and sent to a specific patient. The
filter bar reuses the typographic index already on the homepage rather than inventing a
second control — and never pills.

**The viewer is a native `<dialog>`.** `showModal()` supplies focus trapping, backdrop and
Esc-to-close for free; no library, nothing counted against the 15kb budget (§6). Without
`<dialog>` support the cards stay inert and the grid still works.

**Cards are 8:5, holding two 4:5 frames.** The source images are exactly 4:5, so each half
matches its frame and nothing is cropped — a portrait card would crop the result out of the
picture, which is the entire point of the card.

### The finding: four pairs compare different angles

Auditing all 50 pairs (`design/case-audit/all-pairs.jpg`) surfaced pairs whose **before and
after are shot from materially different positions** — a straight lateral "before" against a
three-quarter oblique "after", most often on BBL cases.

I checked whether this was our extraction. **It is not.** `split-cases.py` takes the left
half of each slide as before and the right half as after; opening the source slides in
`assets/_raw/cases` shows the mismatch is present in **his original slide layout**. Slide 137
sets a straight lateral before beside a three-quarter after. The splitter is faithful; the
source is inconsistent.

That matters because for a BBL an oblique after exaggerates projection relative to a lateral
before. Comparing across positions is the pattern FTC 16 CFR 255 and state medical-board
advertising rules treat as misleading **regardless of intent** — and it is his licence, not
our byline, that carries the consequence.

**bbl-01, bbl-03, bbl-05 and bbl-08 are withheld**, listed with reasons in
`content/case-rejects.txt`. `gen-results.py` reads that file, excludes them and recounts, so
acting on the rest of the audit is one line per case. The homepage section was recounted to
match — 50 → 46, BBL 9 → 5 — because two pages disagreeing about how many cases exist is
worse than either number.

**This is escalation material, not a decision we own** (§2 — anything touching patient media
or claims). He may have the matching frames in the originals; the fix is his photography
protocol, not our code. The remaining 42 pairs still need the same eyeball.

Also removed while here: the homepage claim *"same protocol, unedited."* Nothing in
`facts.md` supports it, and the audit demonstrates the opposite.

---

## D-051 — Fourth page: High-Definition Liposuction

Built from the BBL page. Assets were in place: 6 cases, graded header, and a reel.

**Rollout order changed on an asset check.** Skinny BBL was next by plan — it has a header
and a reel — but it has **zero cases**, and the results section is the page's main
conversion driver. Same for breast lift and breast lift + augmentation. Three procedures
cannot ship a results section at all, which is a new gap for `ASSET-REQUEST.md`: the 68
slides presumably contain some, they are just not split out.

**The statement is his own position, and it is a disqualifier:** *"It reveals muscle. It
cannot build it."* Taken from his Short "High-definition liposuction isn't for everyone".
This operation uncovers structure that already exists; where there is none, the result is
simply thinner. It is the procedure he turns people away from most often, and saying so on
the page is worth more than any before/after.

**A second statement separates it from what people think they are buying:** *"This is not
a weight operation."* The scales barely move — what changes is where the outline sits.

**`NU7_bN1_K1g` (20:24) is English audio**, so the primary talk is his own walkthrough.
Under it sits `eE3qzFCcw2A` — **21K views, the most-watched video on his channel** — in
Spanish.

**Risk section is contour-led, not volume-led**, because that is where this operation
actually goes wrong: irregularity, fibrosis, skin that will not retract. And the recovery
timeline says the thing nobody warns patients about — *you look bigger at two weeks than
you did before.*

Verified: axe 0 at 1440 and 390, no horizontal scroll at 320/390/720, reduced-motion and
no-JS pass, every interaction smoke-tested, no 404s, no console errors.

---

## D-052 — Talk rows get real thumbnails, which reverses part of D-029

Client: *"I feel like some people will think it's not a video. Show thumbnail. It's good to
have some more pictures on the page anyway."* Both true. A title, a duration and a small
play glyph is a *list*, and a list does not read as playable.

**D-029 refused YouTube thumbnails and that reasoning still holds — for the packaged art.**
Of the eight in use across the four pages, four are bikini stock, Impact type and yellow
slashes. What changed is that **his own face is in the other four**, and a crop can be
taken that keeps him and drops the packaging.

**So each thumbnail is a crop, not the thumbnail.**

- **Four cropped from his own art** where he is in frame: `U4MFTb2al-U`, `KdwyQ45RMc0`,
  `fZx_V94QQU0`, `mYXspQhkLd8`.
- **Four replaced with stills of him** where the art is unusable: two frames from his
  consult footage, two from the office portrait. The talk is his; the picture is him. It
  is not a frame from that specific recording, and nothing on the page claims it is.
- **All eight graded `clean-deep`**, so a set assembled from four sources reads as one.

**Two crops needed a second pass** after seeing them at size — `mYXspQhkLd8` kept the
burned-in subtitle bar until the crop moved below y=360 of 720, and my first estimate of
where the text ended was wrong twice. Measuring the source at full size rather than
guessing from a contact sheet is the faster route.

Rows went from a 2rem glyph to a **7rem 16:9 thumbnail** with a play badge over it, the
image scaling on hover. That is eight more photographs across the four pages, which was
the other half of the ask.

Verified on all four: axe 0 at 1440 and 390, every thumbnail loading, no 404s, no console
errors, no horizontal scroll, reduced-motion and no-JS still passing.

---

## D-053 — The approved hero finally reaches the homepage, and the CSS I deleted by offset

Reported as "the hero is messed up — different headline, a client review eyebrow, and it
looked better on mobile." All three were true, and both causes were mine.

**One: the approved hero was never ported.** It was designed, reviewed and signed off on
`hero-headlines.html`, and I flagged three separate times that `index.html` still ran the
old *"Surgery is one day. Healing is the rest."* — then never did it. The homepage now
carries the agreed hero: the proof row (three patient faces + the verified **148,000**),
*"Any surgeon can do the operation. / What happens after is what matters."*, the
attributed byline, and the secondary link.

Mobile "looked better" for a concrete reason: the comparison page pulled the purpose-built
**9:16 cut** (D-039) and the homepage pulled the 16:9 one. The source picker moved into
`main.js`, inside the existing reduced-motion and `saveData` guards, so the phone gets the
portrait render and the unused cut is still never fetched.

**Two: I deleted the proof row's CSS and did not notice.** Removing the marquee, I sliced
`hero-options.css` between string markers; the "credential strip" slice ran to the next
marker and swallowed the social-proof block sitting between them. Avatars rendered square,
the list rendered with bullets.

This is D-028 verbatim — *never edit CSS by offset* — repeated by me, in the same file. And
it survived because `three.mjs` asserted `!!querySelector('.hA__proof')`: **presence, not
appearance**, which is the same weakness as D-043's "no console errors" passing while the
hero shipped at 150px. Checks now assert computed values — `borderRadius`, `display`,
`list-style` — and the hero CSS lives in `styles.css` as the single definition, with the A
block removed from `hero-options.css` so there is nothing to diverge from.

**Contrast had to be measured, not asserted.** The type sits over twelve seconds of moving
footage and axe cannot evaluate text over video — it reported zero violations the whole
time. `tools/contrast.mjs` hides the copy, screenshots the exact band the headline occupies
at seven points in the loop, and takes the brightest background pixel as worst case. Worst
frame is t=0: **8.22:1** desktop and 7.75:1 mobile for the headline, **3.84 / 3.62** for the
faded second line. At 46px and 27px that is large text, so the AA floor is 3.0 and both
pass — but only after the wash was reweighted toward the band where the copy actually sits
and the faded line went from 52% to 66% white.

Nothing else regressed: 24 testimonials, 46 cases, 15 reels, 8 procedure tiles and the
footer are all present, and the published artifact matches dev at both widths.

---

## D-054 — New hero footage, and every visible placeholder comes off the pages

**New source.** `assets/hero vid.mp4` — 3840×2160, 14.85s — replaces the previous file,
which no longer exists. Scene cuts at 2.70 / 5.10 / 6.87 / 8.83 / 11.43 / 13.30.

**8.83–13.30 is excluded.** Four and a half seconds of it are intraoperative: an open,
draped abdomen with visible incisions. The hero's reader is a nervous first-time patient
and an open surgical field is the fastest way to lose her (§4; doctrine fear #3). Same
call as on the previous footage, and I would make it again — it is a tone judgement, not a
consent one, and he can overrule it.

The loop is **8.92s**: marking → studio two-shot → pre-op → desk → result, with the tail
dissolved back into the head and the two dissolves de-conflicted so neither overlaps.

**Mobile crops follow the subject.** Per the client-side lead: where the body is what the
shot is about, the crop centres the body. So the marking shot frames the marked abdomen and
the gloved hand rather than the surgeon's face, and the closing shot frames the result;
the pre-op and desk shots, which are about him working, still centre him.

**Contrast re-measured on the new footage**, since the frames changed underneath the type:
worst frame t=0, headline **8.00:1** desktop / 9.83:1 mobile, faded line **3.74 / 4.59**.
Large text, so the AA floor is 3.0 — passes on both.

### Placeholders removed

Every visible `[[VERIFY]]` chip is off the pages. The important part is that **the claims
came off with the markers** — deleting a marker and leaving the assertion standing would
invert the whole point of §2:

- **Opening hours** — removed from all three footers and the homepage location block.
  Nothing is shown, because nothing is known.
- **Former President, Greater Pittsburgh Society of Plastic Surgery** — removed from
  /about. Asserted only on his own site, never corroborated. An unverified credential with
  its marker deleted is worse than no credential at all.
- **The interview photograph's provenance** — the caption now says only what the
  photograph shows: "Interviewed on camera."
- The **Today** row on the timeline now states sourced facts (Miami, the practice address,
  the consultation languages) instead of admitting a gap.

All three are logged as launch blockers in `ASSET-REQUEST.md`, and `facts.md` records why
the society line was pulled. The only `[[VERIFY]]` string left in the source is an HTML
comment explaining why the book section does not need one.

---

## D-053 — Fifth page: Breast Augmentation

Full asset set: 8 cases, graded header, two reels. `lm9vgSmG7NI` (30:50) is **English
audio**, so the primary talk is his own walkthrough; `m8iwpolYRY4` sits under it in
Spanish. Its packaged thumbnail was a bikini stock model, so that row uses a graded still
of him instead, per D-052.

**Three statements, because this procedure has three separate misunderstandings** and each
one is a reason people end up unhappy with a technically good operation:

1. **"An implant adds volume. It does not lift."** The single most common
   misunderstanding in breast surgery. A larger implant on a dropped breast makes a
   larger dropped breast. Taken straight from his own copy, which says it plainly and
   then buries it.
2. **"A cup size is not a measurement."** It describes a bra, varies by brand, and is not
   what implants are chosen in. Anyone promising a letter is guessing.
3. **"This is not a one-off operation."** Implants are devices with a lifespan. Someone
   deciding in their thirties is signing up for a future operation, and leaving that out
   is the omission that matters most.

**"Over 20 years of expertise" was not carried over.** `facts.md` records it as a live
conflict — his site says two decades, New Life says fifteen years, and the Post-Gazette
timeline puts plastic surgery training after ~2001. Two sites he is associated with
disagree by five years, so no number ships until one is verified.

**The recovery timeline names the week-two panic explicitly** — implants sit high and firm
before they drop, and almost everyone worries at exactly the same point. Saying so on the
page is worth more than a reassurance in a follow-up call.

Verified: axe 0 at 1440 and 390, no horizontal scroll at 320/390/720, reduced-motion and
no-JS pass, all interactions smoke-tested, thumbnails loading, no 404s, no console errors.

---

## D-054 — Sixth page: Eyelid Surgery

7 cases and a graded header; no reel exists, so that block is omitted rather than faked —
the same call as facelift. `eAwmSwrYHkQ` (17:22) is **English audio** and leads;
`bSgBZxXB9Y0` follows in Spanish. Its packaged art was a stock model, so that row uses a
graded still of him being interviewed — the fourth distinct fallback portrait now in
rotation, which keeps the set from repeating across pages.

**Two statements, both about what the operation cannot do**, because that is where this
procedure disappoints people:

1. **"It fixes tired. It does not fix dark circles."** From his own copy, which states it
   and then buries it. Blepharoplasty does nothing for pigment, crow's feet, or skin
   texture.
2. **"Check the brow before you blame the lid."** A heavy brow pushes skin onto the eyelid
   and looks identical to excess lid skin. Operating on the wrong structure makes the eye
   worse, and it is the classic failure mode here.

**The technique section carries the detail that separates a good result from a gaunt
one:** on the lower lid, modern practice *repositions* fat into the hollow rather than
excising it. Taking too much is what produces the skeletal look, and that is stated on the
page rather than left implied.

**Risks include retrobulbar haemorrhage** — rare, but a genuine emergency because pressure
behind the globe threatens vision. Omitting it from a page about surgery millimetres from
the eye would be the wrong kind of restraint.

Related uses the `.prelrow` link row (D-049), since the face neighbours still have no
imagery.

Verified: axe 0 at 1440 and 390, no horizontal scroll at 320/390/720, reduced-motion and
no-JS pass, all interactions smoke-tested, thumbnails loading, no 404s, no console errors.

---

## D-055 — The artifact check could never have caught a missing inline

Reported as "the video isn't playing and the review pictures aren't filled in." Both were
real, both were in the published artifact only, and the check that was supposed to catch
exactly this could not have.

**Three things were never inlined:** the proof-row avatars, the mobile poster, and — the
big one — **both video files**. The hero's `<source>` elements are created at runtime in
`main.js` (D-053), so the paths live in the JS string, and the builder only ever rewrote
paths in the markup. The artifact shipped fetching `/video/hero-1600.webm`, which does not
exist on claude.ai.

**Why the check passed.** Every artifact check copied the built file into `src/public/`
and served it from there — so any path the builder forgot still resolved against the real
asset tree sitting next to it. The check was structurally incapable of detecting a missed
inline, which is the one failure it existed to detect. `tools/artverify.mjs` now serves the
artifact from a directory containing **nothing else**, so a missed inline 404s exactly as
it would in production, and it asserts `videoWidth`, `!paused` and every avatar's
`naturalWidth`.

**And a real bug that only appeared once it was inlined:** a `data:` URI cannot go in
`srcset`. The comma in `data:image/jpeg;base64,` *is* the srcset candidate separator, so
the mobile poster `<source>` parsed to no candidate and rendered broken. All three builders
now strip inlined `srcset`s and the `<source>` elements carrying them; the plain `src`
serves.

**Two false failures on the way**, both the same shape: images inside horizontally-scrolled
carousels are `loading="lazy"`, so vertical scrolling never triggers them. The verifier now
drives horizontal tracks, and only counts a lazy image as broken when it is actually in the
viewport. A check that cries wolf gets ignored, which is its own kind of broken.

---

## D-056 — The library section: he teaches, therefore he is not selling

Asked for a small library block on the homepage. Placed **light, between two dark
sections**, immediately before the location block — the last beat before the practical
close.

**The job is TRUST, not desire.** A surgeon who publishes forty-two talks explaining what
can go wrong, for free, is visibly not running a sales funnel — and that is the argument
the section makes: *"He would rather you understood it first."* It also pays off his own
positioning, recorded in `facts.md` from his introduction video: his site exists "to teach
you about plastic surgery."

**Spanish is stated, not hidden.** The catalogue is Spanish-language and the copy says so
twice. In Miami that is a reach signal, not a caveat.

Four talks chosen to answer objections rather than to sell procedures — Ozempic before
surgery, what he refuses to do, what nobody says about fat transfer, and breast-lift scars.
Two were swapped during review: a Short, because YouTube pillarboxes Shorts into the same
16:9 thumbnail and it read broken beside the others, and the smoking talk, whose thumbnail
is a graphic necrosis photograph — true to the content, wrong for a homepage.

Cards link to the talk itself; a single ghost button goes to the full library. The button
is deliberately **not** a second primary CTA (§5.5) — "Request a Consultation" stays the
only filled button on the page.

---

## D-055 — The case stage shows whole slides. D-026 is reversed.

Client: *"some of the views aren't even showing it for the result pictures."* Correct, and
there were two faults stacked on each other.

**Fault one, mine.** Every case image is **600×750**, but when the stage went full-width
(D-030) I set the half to `aspect-ratio:1/1`. With `object-fit:cover` that silently
**cropped 20% off the top and bottom of every result on every page** — foreheads and chins
on the face pages. Measured: 80% of each image visible, now 100%.

**Fault two, older and worse.** Fixing the crop revealed that the two halves were never
comparable: different framing, different scale, black gaps. `tools/split-cases.py` cut each
slide into a left/right pair and letterboxed each half *independently*, so the pair stopped
matching. **The stage now shows the whole slide.** They are 1:1, composed as a unit by
whoever made them, at matching scale, with their own Before/After labels burned in. Nothing
to align, nothing to crop.

**This retires the BEFORE / BOTH / AFTER control (D-026).** That interaction existed only
because the halves were split. Each slide carries both states already, so the control was
solving a problem we had created.

### The slide→procedure map was lost, and the slides label themselves

`/tmp/casemap.json` was gone with an old session. Rather than reconstruct it by hand, the
slides turned out to be self-labelling — each carries a burned-in title
("DEEP FACE LIFT", "LIPOSUCTION HD", "BBL - BRAZILIAN BUTT LIFT"). Two contact sheets of
the title bands recovered the whole mapping, now committed to
**`content/case-map.json`** so it cannot be lost again.

**It also found cases nobody was using.** MANIFEST recorded what was *deployed*, not what
exists:

| | was | actually |
|---|---|---|
| breast augmentation | 8 | **15** |
| tummy tuck | 7 | **11** |
| eyelid surgery | 7 | **10** |
| bbl / rhinoplasty / hd lipo / facelift | 9 / 7 / 6 / 6 | unchanged |

**64 cases now live, up from 50.** `tools/build-cases.py` supersedes `split-cases.py`.

### Four self-inflicted bugs on the way, all from careless scripted edits

1. A regex meant to delete one-line rules removed the **first line of a two-line rule**,
   leaving an orphan `}` that broke CSS parsing from that point down.
2. A guard `if '.pcase__bar{' not in s` matched the rule *inside a media query*, so the
   restore silently never ran.
3. Splicing the case-stage JS between two comment markers **deleted the recovery timeline
   and operation blocks entirely**, because they sat between them. Caught only because
   `tools/rm.mjs` asserts one visible panel under reduced motion — the assertion added in
   D-044 for exactly this class of fault.
4. An earlier `s=re.sub=None` typo aborted a script *after* it had mutated the string but
   *before* it wrote, so a "successful" run changed nothing.

**Lesson worth keeping:** scripted CSS/JS surgery by string-splice needs a brace-balance
check and a behavioural assertion afterwards, not just "the script printed ok". The
harness caught what reading the diff would not have.

Verified on all six: axe 0 at 1440 and 390, no horizontal scroll at 320/390/720,
reduced-motion and no-JS pass, every interaction driven, no 404s, no console errors.
Homepage re-audited: clean.

---

## D-057 — All cuts, no dissolves; and the case set was replaced underneath the build

**The fades were an inconsistency, not a style.** The hero played four hard cuts (the
source's own scene changes at 2.70 / 5.10 / 6.87 run straight through) and then two
dissolves — one into the result, one at the loop. Two grammars in one ten-second piece
reads as arbitrary, which is exactly how it was described. It is now **all cuts**.

The loop wrap is a cut too, and that is fine: it jumps between two unrelated scenes (the
result, then the marking room), so it reads as an edit. The "weird jump" D-038 fixed was a
different animal — a jump cut *within a single shot*, wide to tight on the same subject,
which reads as a fault. Cutting between scenes is editing; cutting inside one is a glitch.

10.12s, no crossfades, verified frame-by-frame either side of all five transitions.

### The case images were replaced mid-build

`src/public/img/cases` gained 128 new files during the session: the client swapped the
split before/after halves for **64 whole slide compositions**, 1000×1000, with his own
Before/After labels and procedure title set into the artwork, plus `-t` thumbnails.

**The site was broken and not only in the artifacts** — every case reference on the
homepage and /results pointed at `slug-NN-a.jpg` / `-b.jpg`, which no longer exist. 92
images 404ing on each page. It surfaced only because the new isolated artifact check
(D-055) reported the 404s; the old check would have hidden these too.

Rewired: a case is now **one image, not a pair**. Cards are 1:1 with `object-fit: contain`
so nothing is cropped, and **our Before/After chips were removed** — his slides already
carry them and doubling them looked amateur. A 600px grid copy is generated per case
(`tools/case-audit.py` regenerated for whole slides); the viewer loads his full-size file.
Homepage coverflow and filter counts regenerated the same way: **64 cases**.

**The reject list was cleared, deliberately.** `bbl-01/03/05/08` referred to the *old*
numbering; against the new files those lines would have withheld four unrelated cases. The
underlying finding stands and still needs re-checking against the new set —
`design/case-audit/all-pairs.jpg` now shows all 64, labelled.

Also fixed on the way: the filter counts used `--rule-on-dark`, a hairline colour, as text
— **1.88:1** on ink. Now `--muted-on-dark`. It had been failing since the filters were
built and only tripped axe once the count digits changed.

---

## D-056 — Seventh page: Rhinoplasty

The last of the procedures with a full case set. 7 cases; no header photograph existed, so
one was cut from his own footage as with facelift — this time from the **4K re-supply**,
which is visibly sharper. `xJgHsWVNekI` (23:09) is **English audio** and leads.

**The statement is the one thing everybody underestimates:** *"The nose you see at three
months is not the one you keep."* Residual swelling runs six to nine months and the final
shape lands between nine and twelve. No other procedure on this site takes that long, and
the timeline is labelled **"A year, told honestly"** rather than six months.

**A second statement covers what surgery cannot change:** *"Your skin decides how sharp the
result can be."* Thick skin mutes refinement and holds swelling longer. It is not
adjustable, and raising it after operating is too late.

**And a third, in the risks section, that most sites omit entirely:** *"Roughly one in ten
will want a revision."* Published revision rates for primary rhinoplasty run about 5–15%,
the highest of anything here. Stated as a range attributable to the literature rather than
a precise figure attributed to him, and paired with the useful instruction — ask what a
revision costs before booking the first operation.

**Function is treated as inseparable from shape.** Narrowing a nose narrows an airway, so
the septum and internal valve are assessed in the same operation. A nose that looks better
and breathes worse is a failed operation however it photographs.

Related uses the `.prelrow` link row, since the face neighbours still lack imagery.

Verified: axe 0 at 1440 and 390, no horizontal scroll at 320/390/720, reduced-motion and
no-JS pass, all interactions driven, thumbnails loading, no 404s, no console errors.

---

## D-058 — "Cut off" was an aspect-ratio left over from the old card

Reported after the case set changed: a lot of the cases looked cut off. It was not the
photographs and not `object-fit` — it was **three stale `aspect-ratio: 8/5` rules**.

The old cards held two 4:5 photographs side by side, so 8:5 was correct for them. His new
files are **1:1 slide compositions**. I changed the markup and the image, and left the card
geometry alone — so a square image sat inside an 8:5 window with `overflow: hidden` on the
card, and the top and bottom of every slide was clipped. Three places:
`.res__case`, and the mobile overrides on `.res__flow` and `.res__case`, which is why the
phone stayed wrong even after the desktop card was fixed.

All three are 1/1 now, verified by measuring the computed boxes rather than by eye:
desktop card 368×368, mobile 351×351, image filling the frame exactly.

**Two things I checked before touching anything, both worth recording.** The new files are
**the same slides as `assets/_raw/cases`**, downscaled 1200→1000 — perceptual hashes match
at distance 0 across all 64, so nothing extra was cropped in his export. And the framing
inside the slides (heads cut on some BBLs, tight chins on the tummy tucks, hard seams on
the eyelid cases) is **his own composition**, present in the 1200px originals too. That is
a photography-protocol note for him, not something to fix in CSS.

I also tried cropping his chrome away — title bar, the vertical Before/After columns — to
let the photographs fill more of the card. **Rejected:** the slides are not a uniform
template. Several put the Before/After labels *inside* the photo area rather than in the
side columns, so a fixed crop mangled them. Showing his composition whole is both more
honest and more robust.

---

## D-057 — Rhinoplasty header: client-supplied editorial stock

`Rhino.jpg` — a profile study on a soft white ground, natural light, a hand at the bridge.
It replaces the still I had cut from his consultation footage, and it is better: the
brightness against the ink ground gives that page the strongest hero on the site so far.

**It is also much easier to justify than the marked-face image (D-050).** No surgical
drape, no gloves, no pre-operative marking — it reads as an editorial study of a nose
rather than someone mid-procedure. The §3 line about "a face presented as a patient" is
about implying a clinical relationship, and this image does not.

Same mitigations regardless: descriptive alt (*"Profile view of a nose, assessed in
consultation"*), no caption claiming it is his work, and a MANIFEST row recording it as
licensed stock with `patient: no`.

**Worth noting for the remaining face pages:** this is the register that works. Soft,
editorial, no clinical staging. The facelift page currently carries the marked-face
image — the same treatment applied there would lift it, and the search terms that find
this kind of picture are already in `design/media-brief.md`.

---

## D-058 — Procedures hub, and why it came before an eighth procedure page

Building the next procedure surfaced two things worth acting on ahead of it.

**Breast Lift & Augmentation is not buildable to standard.** No case set — and their own
page carries **the liposuction recovery chart**: "HD Lipo takes 1 to 2 hours", "use your
BBL pillow", "faja for three months", with BBL testimonials underneath. There is no valid
recovery data for that operation anywhere on their site, so the page would ship without
results *and* without a timeline.

**And the primary CTA was broken everywhere.** An audit of internal links across the seven
built pages:

| route | links | was |
|---|---|---|
| `/book` | **35** | 404 |
| `/procedures` | 21 | no page |
| `/about` | 14 | 404 |
| `/results` · `/preparation` · `/contact` | 7 each | 404 |

"Request a Consultation" appears 35 times and every one 404s. §5.5 makes it the one
primary action and the definition of done requires a stranger to find booking in three
seconds. **`/book` is now the single highest-value thing outstanding.**

`/procedures/index.html` closes the 21-link gap: eleven procedures grouped Body / Breast /
Face, each with case count, one-line definition and header image. Unbuilt pages read as
"page in progress" rather than broken. Scarless Eyelid, which has no photograph, gets a
typographic plate — not a placeholder frame (D-041).

## D-059 — Eighth page: Skinny BBL, and an honest cross-reference

Chosen over the other three remaining because its **recovery data legitimately transfers**
— it is the same operation at lower volume, so his BBL chart applies, and the page says so
rather than implying separate data.

**Results are cross-referenced, not fabricated.** No case set is filed for skinny BBL, and
relabelling BBL cases as small-volume transfers would be inventing case metadata. Instead
a `.pxref` block states where the evidence actually is — *"His cases are filed under
Brazilian Butt Lift… which of them were small-volume transfers is not recorded"* — links
to the nine, and carries the real 17-second reel beside it. That is a reusable pattern for
any procedure whose evidence lives under another.

**The statement is the sentence that brings people to this page:** *"You were told you did
not have enough fat."* Taken from his own opening line. It then does the useful thing —
distinguishes not having enough to add volume from not having enough to reshape.

**One claim handled carefully.** His copy attributes graft survival to PRP, exosomes and
hyperbaric oxygen. Those are his protocol and stating he uses them is fine; asserting they
work is a medical claim we cannot source. The FAQ says they are part of his aftercare,
that the evidence is still being established, and to ask him what he expects them to do —
which is true, useful, and claims nothing.

Verified: axe 0 at 1440 and 390 on both new pages, no horizontal scroll at 320/390/720,
reduced-motion and no-JS pass, interactions driven, reel plays, no 404s, no console errors.

---

## D-059 — SUPERSEDED by D-060. Kept for the reasoning, not the outcome.

## D-059 — The results section goes light; the page had to breathe after the hero

Two dark sections back to back — the hero film frame and then the gallery on `--ink` —
made the top of the page one undifferentiated block. Asked to either reorder or go light.

**Went light, kept the order.** §5.2 puts the results gallery within one tap of the top and
it is the single biggest conversion driver on the page; moving it down to win a rhythm
argument would have cost more than it gained. So `.res` is now `--paper`.

It is a better section for it. **The tiles stay black** — his slides are black compositions,
and a black card on paper is far stronger contrast than a black card on ink, where the
tile edges previously dissolved into the background.

**Scoped, not global.** `.res__filters` is shared with `/results`, which is still dark, so
every light override is written under `.res` — a class that only exists on the homepage.
Changing the base rules would have inverted the gallery page.

Two details the change surfaced: the `grain` overlay is tuned for ink and reads as dirt on
paper (dropped from `.32` to `.14` on this section only), and with `.res` and `.about` both
on `--paper` the two ran together as one long section with a hole in the middle — a hairline
on `.about` gives the boundary back.

Order is unchanged: `hero → res → about → band → rev → reel → lib → loc`, now
dark → light → light → dark → dark → dark → light → light.


---

## D-060 — Reordered instead: the surgeon speaks, then the work

D-059 turned the results section light to break the dark-on-dark run under the hero. The
client-side lead preferred that section dark, so the fix moved from colour to sequence:
`.res` is back on `--ink` and **About** takes the slot under the hero.

`hero → about → res → band → lib → rev → reel → loc`

**dark → light → dark → dark → light → dark → dark → light.** No run longer than two, and
the page opens up immediately after the film frame — which was the actual complaint.

**It is a defensible order, not just a rhythmic one.** D-047 put About *after* results on
the argument that "who did these?" is the question a wall of before-and-afters provokes.
That reasoning was written against the old hero. The current hero already answers *who* —
it carries the proof row and a byline naming him and his training — so About now reads as
the expansion of a question the hero has already raised, and the gallery lands immediately
after in the position §5.2 cares about. Results is still one tap from anywhere via the nav.

**The library moved up** from second-to-last to the middle, between procedures and reviews.
It earns the position: after she has seen the work and found her procedure, "he publishes
everything he knows for free" is the trust beat, and it breaks what would otherwise be
four consecutive dark sections.

Both light overrides from D-059 were removed rather than left dormant — `.res` back to
`--ink`, the `grain` opacity back to its tuned value, and the `.about` hairline dropped
since it no longer sits against another paper section.

---

## D-061 — Reverted to the original order

D-059 (results light) and D-060 (reorder) were both attempts at the same complaint — dark
hero running straight into a dark section. Neither was kept. The order is back to what it
was:

`hero → res → about → band → rev → reel → lib → loc`

with `.res` on `--ink`. All of D-059's colour overrides remain removed; nothing dormant is
left in the stylesheet.

Recording the cost, since it is the point of a decision log: the rhythm objection was real
and is now back — **dark, dark** under the hero, and **band / reviews / Instagram** running
three dark sections together in the middle. Two fixes exist and are known to work; if it
comes up again, the reorder (D-060) is the cheaper one because it needs no restyling, and
the library section is the natural light break for the middle run.

---

## D-060 — Ninth page: Breast Lift & Augmentation, and what it refuses to claim

The hardest page so far, because **two of its strongest sections could not be sourced.**

- **No case set.** His documented breast cases are filed as augmentations. A lift is a
  different operation, so showing them here — as skinny BBL shows BBL's — would be
  misleading rather than merely incomplete.
- **No valid recovery data.** His own page carries **the liposuction chart**: "HD Lipo
  takes 1 to 2 hours", "use your BBL pillow", "faja for three months", with BBL
  testimonials beneath it. Publishing that as a breast recovery would be repeating
  somebody else's copy-paste error as fact.

**So the page says so, once, in one block.** "Two things this page does not claim" states
that the cases are augmentations and that the recovery approximates augmentation's with a
longer incision, links to that timeline, and carries the real six-second lift reel beside
it. One honest section beats two apologies, and the recovery section is simply absent
rather than filled with the wrong operation's numbers.

**Three statements, because this procedure is a decision before it is an operation:**

1. **"A lift trades a scar for a shape."** The bargain nobody states plainly. An
   augmentation hides its incision in a fold; a lift cannot.
2. **"Where your nipple sits decides which operation you need."** The objective test —
   above or below the inframammary fold — takes a minute to check and settles the
   argument.
3. **"Doing both at once is a real trade-off."** A lift tightens the envelope, an implant
   pushes against it. They work against each other, staging is legitimate, and the page
   says to ask which he recommends rather than assuming one sitting is just more efficient.

The index renumbers 01–05 with Recovery removed, and "Results" became "Evidence" because
that is what the section honestly is.

Verified: axe 0 at 1440 and 390, no horizontal scroll at 320/390/720, reduced-motion and
no-JS pass, interactions driven, reel plays, thumbnails load, no 404s, no console errors.
Hub updated — two cards left as "page in progress".

---

## D-062 — /preparation: the page indexes his guidance, it does not issue ours

*(Expanded in D-063 — the first pass was under-built.)*

The most-linked missing route on the site (20 references) and the one that carries the
positioning `facts.md` calls "the spine of the brand" — recovery as part of the operation.

**One constraint decided the entire design.** `youtube-catalog.md` records a direct
contradiction between two of his own channels: his website says a binder for the first
month after abdominoplasty; his YouTube video `lfUDnaabfEM` says he *prohibits* the garment
for that first month. When a surgeon's own sources disagree about post-operative
instructions, a third party publishing either one is making a clinical call it has no
standing to make.

So the page **publishes no post-operative instructions at all.** It does three things
instead: states the philosophy and where it comes from, indexes *his own talks* so the
instruction arrives in his voice rather than ours, and says plainly that the plan comes
from him in person. A closing line makes that explicit — "nothing on this page is medical
advice or a set of post-operative instructions."

That turned out to be the stronger page anyway. "Ask him what can go wrong" and "what he
will not tell you: that it will be easy" do more for trust than a timeline would, and they
carry no risk of contradicting him.

**Three talks, chosen for objections not procedures** — Ozempic before surgery, nicotine,
and how to sleep to protect the result. All three had local thumbnails already; I did not
pull more from YouTube for six others I wanted, and picked from what was on disk instead.

Two build details: the signature is ink artwork and needed inverting for the dark section,
and the artifact builder for this page inlines the talk thumbnails, which the About builder
had no reason to handle.

> ⚠ **Still live and still wrong: `/procedures/tummy-tuck` publishes the disputed
> compression instructions in nine places, including inside its JSON-LD.** I have not
> touched them. Removing them is a content decision and choosing between them is a clinical
> one — both are his. This is the single highest-priority item to put in front of him.

---

## D-063 — Tenth page: Breast Lift, built around the disappointment it prevents

The page's whole spine is one sentence: **"A lift makes you perkier, not bigger."** That is
the standing statement in *Before you decide*, it is the first FAQ, and the hero definition
says it before anything else — *"Nothing is added, so nothing gets bigger, and that
surprises people who did not ask."*

That is the commonest post-operative disappointment in this procedure and it is entirely
preventable by being told first. Leading with it costs some enthusiasm on the page and buys
back a consultation that is not spent correcting an expectation. **Rejected:** opening on
"restore a youthful shape," which is what his current site and roughly every competitor
does, and which sells the operation to exactly the people who should be booking an
augmentation instead.

**Five moves, and the second one is the reason the page exists.** *"The nipple is raised on
its own blood supply"* — not detached and re-sited. It makes the nicotine rule mean
something instead of reading as boilerplate, and the risks section and candidacy check 05
both point back at it. The step mark for move 04 was redrawn after review: a wide flat ghost
shape, a narrower taller shape drawn over it, and two arrows pushing inward — *gathered and
narrowed*, which the earlier dome-plus-circle did not say.

**Same refusal as D-060, one line stronger.** No case set is filed for a lift alone, and his
cases are augmentations, so none are shown. On recovery he does publish one figure — one to
two weeks to normal activity — and that is now in the fact rail with the source named
in-page. A full week-by-week timeline is still not sourced, so none is invented; the
augmentation timeline is linked as the nearest real answer.

**A price band exists and is still not published.** His blog post *"Lift alone or lift with
implants"* gives "$4,000–$8,000, add $2,000–$4,000 for implants" — the first pricing figure
found anywhere in his material. It is his, so it traces, but it is an undated blog estimate
rather than a quote from the practice, and every other page ships "what moves the number"
with no figure. Publishing it here alone would make this one page look authoritative about
money in a way the rest of the site is not. Logged as `PP6`, one yes/no from him away.

**Two link bugs fixed while here, both pre-existing.** `breast-lift-aug` and `skinny-bbl`
each carried a *related* card pointing at themselves — a dead end in the one component whose
job is onward travel. And the `prel__n` numerals had drifted out of sync with the hub across
six pages (HD Lipo appeared as 07, BBL as 01, Breast Lift & Aug as 04, against 04/02/07 on
the hub). Swept all of them to the hub numbering, and fixed one card whose `src` and
`srcset` pointed at two different procedures' photographs.

Verified: axe 0 at 1440 and 390 on all four changed pages; no horizontal scroll at 320 or
390; reduced-motion and no-JS both pass (`visibleChecks` 1 with JS, 5 without). Hub is now
one card from complete — only Scarless Eyelid Rejuvenation remains flagged.


---

## D-063 — /preparation, second pass: the media was already on disk

The first version was three sections and two photographs, which was not a page so much as a
statement. The brief was to use more of the media and to be smart about it. Almost
everything it needed already existed and was going unused.

**A full-bleed 21:9 band** carrying his own line — *"Zero pain and zero inflammation don't
exist in a real body"* — over the consultation it describes. It is the title of one of his
own talks, so it is his claim, not ours, and it is the most honest sentence available for
this page. Cut 21:9 rather than 16:9 deliberately: a band should read as a band, not as a
screenshot.

**Four recovery reviews, already written and already on the homepage.** The homepage section
is titled "The part nobody photographs" and contains testimonials specifically about
recovery — the intense prep plan, the rough first week, the 11pm message he answered. They
belong here more than there, and reusing them cost nothing.

**The team photograph earns a second placement** because of what one of those reviews says:
*"His office called me twice to check in."* The caption ties the two together — it is the
same three people every time, which is why that happens at all. Same asset, different
argument.

**The book joins the talks** as a fourth card rather than getting a band of its own. Three
videos and a book is one idea — *here is everything he would want you to know first* — and
it fills the four-up grid the homepage library already uses.

Two layout bugs found by measuring rather than looking: the band's `.wrap` was a flex item
and shrank to its content, centring the quote instead of aligning it to the measure; and the
book cover's `height:100%` could not resolve against an `aspect-ratio` box, so a 2:3 cover
overflowed a 16:9 frame. Absolute centring fits it.

**Still missing, now requested:** `hiperbaric-chamber-equipment.jpg` is catalogued in his
media library and was never downloaded. The page argues the hyperbaric case in words with no
photograph to show for it — the one obvious hole left in it.

---

## D-064 — Marks, a bleed, and no head-count

**No team size, anywhere.** The /preparation caption said "it is the same three people every
time." Same error as D-051: `facts.md` carries two *named* staff because those are the two
his About page names, which is not evidence of the staff. The caption now makes the point
without the arithmetic — "a small practice is why that happens at all, you are not handed
between departments." Grepped every page; that was the last one.

**Three purpose-drawn marks**, on the honest three-up. Following D-037's rule that a mark
must encode its point rather than label it, and §4's ban on icon soup — nothing borrowed
from a library, one stroke weight, `currentColor`, all on a 24 grid:

- *Your plan is yours* — three rules with the last one unfinished, and a dot where it starts
- *The first week is the hard one* — a measured span whose opening stretch carries the weight
- *Ask him what can go wrong* — a question mark reduced to an arc and a dot

The second one took two attempts worth recording. It began as **seven ticks**, one per day,
with the first standing taller — literal and, at 36px, a picket fence. Widening the spacing
did not save it; six strokes five pixels apart is a barcode regardless. The concept had to
change rather than the geometry. **A mark that only works at inspection size does not work.**

**The intro photograph now bleeds off the right edge** rather than sitting as a contained
rectangle in a column — `margin-right: calc(50% - 50vw)` with `overflow-x: clip` on the
section, and the bleed reduced to a gutter pull below 64rem. It is the single change that
does most for the page, and it costs nothing: same asset, better placed.

The honest three-up also stopped being three floating blocks — hairline dividers between the
columns on desktop, stacked rules on mobile, so the marks sit in a system.

---

## D-064 — Eleventh page: Scarless Eyelid, and a hero with no photograph

The last procedure page, and the only one with no header image (`PP7`). The two ways to
fake one were both worse than not having one: borrow the eyelid-surgery photo — which is an
*upper*-lid marking for the exact operation this page exists to distinguish itself from —
or buy a stock face, which §3 forbids outright.

So the figure slot carries the page's argument instead. `.phero--plate` is a bordered panel
holding the eye mark and one sentence: **"There is still an incision. It is on the inside of
the lower lid, where a scar has nothing to show."** A page whose product name is *Scarless*
should say what the word is describing in the first screen, and saying it confidently reads
as authority rather than as a caveat. **Rejected:** an anatomical sagittal diagram — drafted,
rendered, and thrown away. Without labels a cross-section of an orbit reads as abstract arcs;
with labels it needed SVG text and three levels of type it could not carry at 320px.

**The signature component is his own comparison, rebuilt.** His site carries traditional-vs-
scarless as a bare table; here each row is one question put to both columns, so a reader can
stop at whichever row is theirs. It replaces the results slot, which is honest — no case set
is filed for this procedure and his eyelid cases are blepharoplasties, i.e. the other column.
`.pcmp` stays a real `<table>`; the narrow-screen restack needs `display:block`, which strips
the table roles, so the markup re-declares every one of them explicitly.

**This is the best-sourced page on the site.** Every number in the fact rail comes off his own
scarless page — 45–60 minutes, local with sedation, 5–7 days to desk work, three months to
full effect — as do all five candidacy checks and all six FAQ answers. It needed no invention
anywhere, which no other procedure page can say.

**Two statements do the persuading.** *"The smaller operation has a ceiling"* — it takes fat
out and tightens skin, it does not remove skin, so genuine excess needs the other operation.
And *"The laser is the half people underestimate"* — the fat removal is quick, the resurfacing
is what decides your week. Both are conversion arguments, not disclaimers: the reader who
belongs in the other column costs him a consultation slot and a bad review.

**One risk is phrased as a question on purpose.** *"How your skin responds to the laser"* asks
the reader to put it to him directly, rather than us publishing a claim about resurfacing
outcomes across skin types that his own material does not make. In a Miami practice it is the
most useful line on the page and the one we have least standing to answer.

**Four thumbnails were fetched and two were rejected.** `W2I3Qg0GxEo` — "Learn about Scarless
lower eyelid surgery", the single most on-topic video on his channel — has an auto-generated
frame showing **an identifiable patient mid-operation**, so its thumbnail is not going on a
public URL. `uimnyUSJdDI` turned out from its description to be a **patient testimonial**,
which the whole site refuses on `D2` grounds. The pair that shipped is `Ykg14uawacg` (the
three questions he asks) and `j9ljkeXKmmw` (the master class, and the only thumbnail on the
channel carrying a real anatomical diagram — see `illustration-brief.md`).

**Three pre-existing bugs fixed while here.** All eleven procedure pages had `Body` in the
breadcrumb, including the four face procedures and the three breast ones — swept to match the
hub's three sections. `.phero__rail dd` carries `tabular-nums`, which also makes the comma
figure-width, so every rail sub-label rendered as "Full-time , then tapering"; reset on the
`small`. And the hub's flat card is now the eye mark plus the word rather than the word alone.

Verified: axe 0 at 1440 and 390 across all eight changed pages; no horizontal scroll at 320,
390 or 1440; reduced-motion and no-JS pass; FAQ schema matches the visible questions exactly.

**The procedure set is complete — eleven of eleven.**

---

## D-065 — The site was unbrowsable, and every check said it was fine

The user reported the site would not load. It was not a broken page. **Every internal link
on the site is extensionless** — `/procedures/breast-lift`, `/book`, `/about` — which is what
Vercel, Netlify and Cloudflare Pages serve by default. `tools/serve.py` was a plain
`SimpleHTTPRequestHandler`, which resolves only real files, so every one of those links 404'd
in a browser.

**The verification harness never caught it because the harness requested `*.html` directly.**
axe, overflow, rm, sections, shootpage — all of them were pointed at
`/procedures/breast-lift.html`, a URL nothing on the site links to. Eleven procedure pages
were signed off as verified while the site could not be navigated at all. That is the
failure worth remembering: **a check that does not use the same URL a visitor uses is not a
check.**

`serve.py` now resolves clean URLs (`<path>.html`, then `<path>/index.html`, with real files
and directories still winning first) and logs 404s to stderr, because a 404 on a clean URL is
almost always a broken internal link rather than a missing asset.

**Added `tools/crawl.mjs`** — walks every link from `/` outward, reports dead routes with the
list of pages linking to them, plus any failing sub-resource and any page throwing a JS error.
This should have existed from the first page. Run it before calling anything finished.

Its first run found five dead routes. Two were wrong slugs pointing at pages that exist and
are now fixed: `/procedures/brazilian-butt-lift` → `/procedures/bbl` and
`/procedures/deep-facelift` → `/procedures/facelift`, linked from the homepage, `/results`,
`/preparation` and `/about`.

Three remain and need pages built, not links repaired:

| route | linked from | note |
|---|---|---|
| `/contact` | **18 pages** — it is in the primary nav sitewide | The largest hole on the site |
| `/privacy` | 4 | Footer. Also a `D4` prerequisite — the booking form collects personal data |
| `/accessibility` | 4 | Footer |

Current state after the fix: 21 pages crawled, 0 JS errors, 0 failing sub-resources on any
page that exists.

---

## D-066 — /contact, and the third address nobody had noticed

**The page carries no form.** §5.5 allows one primary CTA sitewide and it is "Request a
Consultation"; a second form here would compete with `/book` and split the conversion. So
`/contact` routes instead: three channels, each labelled with what it is *for* — the
consultation form for anything about surgery, the phone for anything with a date attached,
email for anything needing a paper trail. Only the consultation route is marked as primary.

**Investigating the address turned up a live bug on his current site.** He publishes two
practice addresses, split by language:

| where | address |
|---|---|
| English footer, every page | 8400 SW 8th St, Floor 4th, Miami, FL **33146** |
| Spanish footer, every page | 2100 Ponce de Leon, Suite 1010, Miami, FL **33134** |
| Homepage map embed | 8400 SW 8th St |
| **Contact page map embed** | **2100 Ponce de Leon, Coral Gables** |

His own contact page shows a map of Coral Gables above a footer naming an address in
Westchester, seven kilometres away. A Spanish-speaking patient and an English-speaking
patient are sent to different buildings. Both geocode to real places. Confirmed with the
client-side lead: **Westchester is the office**, and this build uses it alone.

**The ZIP is now corroborated by a second independent source.** `facts.md` resolved
33144-over-33146 on the Google Maps place record. OpenStreetMap independently returns
**33144** for 8400 SW 8th St, and so does the building's own `addr:postcode` tag. His site
still prints 33146. *(Proposed `facts.md` amendment flagged separately per §7 — that file is
not edited without raising it first.)*

**The map is generated, not embedded.** `tools/build-map.py` pulls street and building
geometry from the Overpass API and renders it as inline SVG in the site's line register.
A Google Maps iframe is ~700kb of third-party JavaScript, sets cookies — which drags a
consent banner onto the page — and cannot be graded to match anything. This is **12.8kb,
zero runtime requests, and inherits `currentColor`** so one file works on both grounds.
It has to be *inlined*: an external SVG referenced from `<img>` cannot see the page's
`currentColor` and renders black on both. Attribution is rendered visibly, as ODbL requires.

Two wayfinding facts on the page come from OSM way tags rather than memory: SW 8th Street
is **US 41 / Tamiami Trail**, and it is **divided** here — each direction is a separate way,
so overshooting the block is not a U-turn. The cross-streets were computed from the geometry
(SW 87th 433m west, SW 82nd 388m east), not eyeballed.

**Three bugs fixed while here.**

1. **`.visually-hidden` vs `.vh`.** `procedure.css` named the hidden-text class one thing and
   `styles.css` the other, so the contact page's section heading rendered at full size. The
   comment on the `styles.css` rule records this *already happening once* on `/about`. Both
   names are now bound in both files, and the duplicate `.vh` block in `styles.css` is gone.
2. **NAP formatting.** Five pages printed "Floor 4" in the footer against "4th Floor" in
   the body. Normalised sitewide — split formatting costs local ranking (§5.7).
3. **A real AA failure on `/videos`**, pre-existing and unrelated: `.vid__filters .n` used
   `--rule-on-light` — a *hairline* token, **1.49:1** on paper — as a text colour. Now
   `--muted-on-light` at 6.32:1. I probed every other place a rule token is used as text
   across ten routes; nothing else renders, so this was the only one.

Verified: axe 0 at 1440 and 390 on all eight top-level routes; no horizontal scroll at 320,
390, 768 or 1440; crawl clean apart from `/privacy` and `/accessibility`, which still need
pages.

**Still open on this page:** office hours. They appear nowhere in his site, his footer, or
any of his 202 video descriptions. The client-side lead is supplying them; until then the
page ships no hours block rather than a guess.

---

## D-067 — Hours, plainer directions, and a typographic bug on every duration

**Hours are in**, supplied by the client-side lead: Mon–Fri 9:00am–7:00pm, Sat 9:00am–2:00pm.
They sit under the address, which is where people look for them, and they are also in the
`LocalBusiness` node as `openingHoursSpecification` — that is what drives the "Open now"
label in Google's local pack, and it is the first genuinely structured local signal on the
site. *Sunday shows "Closed": inferred from six days being given rather than stated. Worth
one confirmation.*

**The directions copy was rewritten.** The first version read like a gazetteer — a
"Also known as / US 41 · Tamiami Trail" row, a "Neighbourhood" row, a "Floor: Fourth" row.
Correct, and nothing a person would ever say. It now reads as directions someone in the
office would give, with the same facts inside the sentences: *"You will find us on Calle
Ocho, out in Westchester — SW 8th Street, signed as US 41. The street is divided along this
stretch and the building is on the south side… so it saves a loop to pick your direction
before you reach the block."* Dropping the definition list also freed the slot the hours
needed.

**A real typographic bug, found in the hours and traced across the site.** The times were
rendering as `9 : 00am`. Cause: `font-variant-numeric: tabular-nums`. In Schibsted Grotesk
the tabular set gives the **colon, comma and period figure width too** — measured at
**10.16px against 4.48px proportional**, more than double.

That was not just the hours. Every video duration on the site carried it, and on `11:48` the
tabular set is **51% wider** (50.78px vs 33.59px). So did the Instagram post count, `1,143`.
The same bug had already been found and fixed once in isolation on `.phero__rail dd small`
("Full-time , then tapering") without anyone asking where else it applied.

Fixed on `.reel__dur`, `.vid__dur`, `.pvid__dur`, `.pvt__dur`, `.ig__stats b` and
`.ct-hours dd`. **Tabular figures stay everywhere they belong** — pure-numeral counts,
indices, case numbers — because those have no punctuation to widen, and there the column
alignment is the whole point. The rule now written into the CSS comments: *tabular for
numerals, proportional for anything with a separator in it.*

Method note, because the first pass got this wrong: rather than eyeball screenshots, a probe
walked twelve routes collecting every rendered element whose computed
`font-variant-numeric` includes `tabular-nums` **and** whose text contains `:` `,` or `.`.
That produced the exact list, and re-running it after the fix returns clean. The same probe
shape found the earlier `--rule-on-light`-as-text failure.

Verified: axe 0 at 1440 and 390 across ten routes; crawl clean apart from `/privacy` and
`/accessibility`.

---

## D-065 — The deliverable is HTML pasted into GoHighLevel

Confirmed as the delivery route: raw HTML into GHL custom-code elements, and the
client does **not** need to edit it in the builder. That removes the hybrid
approach I had proposed and makes the whole site one export target.

`tools/build-ghl.py` emits `dist/ghl/` — one self-contained blob per page: a scoped
`<style>`, the markup wrapped in `.jca`, then a `<script>`. **Nothing depends on load
order and nothing depends on GHL serving `.css`/`.js` with a correct MIME type**, which
is the usual reason this kind of migration fails. Cost is ~110–165 KB per page
uncompressed, most of it the shared stylesheet; it gzips to a fraction and beats the
fragility of external references. `--external` emits the split version if that changes.

**Two host problems, both solved at export rather than by hand-editing 19 pages.**

*Style bleed, in both directions.* The stylesheet was already almost entirely
class-scoped — 593 rules, **zero `!important`** — with only four bare element rules
(`html`, `body`, `a`, `img,video`). Those are rewritten to `.jca …` on the way out.

*Full bleed.* GHL wraps custom code in a max-width container, which would break every
full-bleed section. Top-level children of `.jca` get `width:100vw` with
`margin-left:calc(50% - 50vw)` — a no-op when the parent is already full width, so it is
safe in both cases — plus `overflow-x:clip` for the scrollbar difference.

**Verified against a simulated host**, not assumed: a page carrying a builder's typical
globals (`*{box-sizing:content-box}`, `body` font, `a` colour, `img` display) with our
blob inside a 1200px container. GHL chrome kept its own font and colour, our sections
measured exactly the viewport at 1440 and 390, no horizontal scroll, the hero picked the
right cut per breakpoint, no broken images and no console errors.

The JSON-LD is stripped out of each blob and written to a `.jsonld.html` sidecar, because
it belongs in the page's head tracking code, not in a body element.

**Two things GHL has to supply**, recorded in `dist/ghl/README.md`: the booking form
becomes a native GHL form so submissions reach the CRM — which is also how the definition
of done's "submissions land somewhere real" finally gets met — and the page slugs have to
match the paths in the markup or the internal navigation breaks.

**One constraint raised early rather than late:** Lighthouse mobile ≥ 90 is in the
definition of done and GHL injects its own runtime on every page. Measure the preview
build and the GHL build separately and report both.

---

## D-066 — The fonts had to be embedded, and my test had proved the wrong thing

Reported that the export's "font is completely messed up and even the spacing."
Correct, and the cause was mine twice over.

**The cause.** The shipped blobs referenced `ASSET_BASE_URL/fonts/*.woff2`, a
placeholder. The faces 404, the browser falls back to Georgia and Helvetica, and
because fallback metrics differ from the real ones, **every line length, leading and
vertical rhythm moves with them**. It presents as "the spacing is off" when the only
fault is one missing file. A hosted webfont has no graceful degradation.

**Why I did not catch it.** I built the export with `--base http://localhost:8787`,
served it, and diffed computed styles against the dev site. Identical, obviously —
the fonts resolved. I then shipped a build with the placeholder base and reported the
earlier result as if it covered it. The check tested a configuration nobody would ever
ship. Same failure as D-043 and D-055: **verifying a convenient variant and reporting
it as the shipped one.**

**The fix.** The four referenced `.woff2` are base64'd into the `<style>` by default.
~163 KB per page, ~155 KB gzipped for the whole homepage blob, and the typography can
no longer depend on a URL being right. `--link-fonts` restores hosted faces.

**The check now matches the deliverable.** `tools/filecheck.mjs` opens the exported
file over `file://` — no server, no asset host, nothing resolvable — and diffs
typeface, size and box metrics against the dev site. Identical at 1440 and 390: h1
848×105 desktop, 342×63 mobile, lede heights matching. If it renders correctly from a
bare file on disk, it will render correctly anywhere.

Images remain external: 26 MB across 345 files cannot be inlined. Until they are
uploaded, pages render with correct type, layout and spacing and empty image frames —
now stated plainly in the README so it is not mistaken for a fault.

---

## D-067 — Real reviews replace the ones I wrote

The homepage, `/results` and `/preparation` now carry twelve verbatim reviews from his
RealSelf profile, attributed to the handle RealSelf shows plus the month, linking back.
`content/reviews.json` is the single source; `tools/inject-reviews.py` places them.

**What they replace matters more than what they are.** `facts.md` had blocked his site's
testimonials — *"under FTC 16 CFR Part 255 a testimonial must reflect a genuine
experience"* — and then I wrote twelve of my own in a convincing patient register. A
`rev__note` labelled them "placeholder copy", which is not a defence: they read as real
because I wrote them to. Fabricated testimonials on a physician's site are precisely the
exposure that rule exists to prevent, and being well written made them worse, not better.

**RealSelf blocks automated access** — 403 on both the profile and the reviews path. I did
not spoof a user agent around it; the client-side lead pasted the content instead. Worth
recording that the block exists, because it is also a signal about their terms.

**Three exclusions, applied at curation and written into the JSON** so they cannot creep
back: prices (from the Pennsylvania practice, not current Miami pricing); a patient's line
calling him *"triple board certified … went to Harvard"* (asserted-not-verified in
`facts.md`, and the Harvard year was a research laboratory, not a clinical post — a patient
repeating it does not make it sourced); and implant volumes and cup sizes, which read as a
promise to the next reader.

**Two things flagged rather than solved.** The republication question — RealSelf owns that
UGC and the aggregate-plus-badge route is the conventional one — was raised and overruled;
it is recorded in `facts.md` with a date. And **most of these reviews are 2018–2022 from
his Pennsylvania practice**, not Miami. His work and his patients, so legitimate, but the
newest is June 2022 and a Miami site whose most recent review is four years old is a
visible gap. Google review export remains the fastest fix.

The `.rev__note` styling was rebuilt on the way: it was a flex row of uppercase small-caps
with a bullet, which was fine for two words and fell apart the moment the note carried a
sentence and an inline link.

---

## D-068 — The map is now a Google embed, and what that costs

Client-supplied embed, swapped in for the generated SVG. `tools/build-map.py` stays in the
repo and regenerates the old map in one command if the tradeoffs below ever bite; the
generated `locator.svg` was deleted rather than left orphaned.

**Four changes to what was pasted, all of them necessary:**

1. **A `title`.** An `<iframe>` with no accessible name is an axe `frame-title` violation.
   Without it this page would have shipped the site's first a11y regression.
2. **The inline `style="border:0"` moved to CSS** (§6 — no hard-coded style values in
   component files).
3. **The fixed `600x450` replaced with an aspect-ratio box.** As pasted it would have
   forced a 600px floor and broken the page at 320px. The `width`/`height` attributes stay
   to give the box its intrinsic ratio.
4. **`!5e1` → `!5e0` — satellite to roadmap.** Aerial tiles of a Miami suburb are orange
   rooftops and parking lots; it was the loudest thing on the page by a wide margin (§4).
   Address, zoom and pin are exactly as supplied, and one digit restores satellite.

**Measured cost, so the number is on the record rather than estimated:** the embed makes
**43 requests across 6 third-party hosts** — `www.google.com`, `maps.gstatic.com`,
`maps.googleapis.com`, `fonts.googleapis.com`, `fonts.gstatic.com`, `places.googleapis.com`.
Byte weight is not readable cross-origin, so the request count is the honest figure. It is
`loading="lazy"` and below the fold, so it should not touch LCP; it will show up in total
byte weight and in third-party blocking time. **Re-run Lighthouse on `/contact` before
signing off the mobile ≥ 90 target** — this is the one page where that number is now at risk.

No cookies were set in a clean context on load. That is *not* a guarantee for real users —
Google sets them on interaction and for signed-in visitors — so if he takes EU patients the
consent question is live. The click-to-load pattern already used for the YouTube embeds
solves it and is one edit away.

**A published claim, verified rather than assumed.** Google drops its pin on the street
centreline, which made the copy's "the building is on the south side" look wrong. Checked
against the OSM geometry: all five SW 8th Street carriageways near the address sit **40–62m
north** of the building footprint. The copy is correct; the pin is just Google's geocode
marker, not the building.

Verified: axe 0 at 1440 and 390; no horizontal scroll at 320, 390, 768 or 1440; crawl clean
apart from `/privacy` and `/accessibility`.

---

## D-069 — /contact hero rewritten: the wrong voice for a utility page

The hero read **"Three ways in, and one of them is the right one."** Flagged by the
client-side lead as sounding unnatural, and they were right: it is a riddle, not a headline.
The reader has to decode it before they learn anything, on the one page where nobody is
browsing — they arrived with a task.

That aphoristic voice is correct on the procedure pages, where the job is persuasion and a
line like *"A lift makes you perkier, not bigger"* earns its keep by reframing a decision.
On a contact page it is just friction. **Plain beats clever wherever the reader has a task
rather than a doubt** — worth holding to on `/privacy` and `/accessibility` too.

Now: **"Get in touch."** — which also pairs with **"Getting here."** further down, so the
page has two plain headings in the same register instead of one epigram and one label.
The lede opens with a question, which is how a receptionist would actually start:
*"Thinking about surgery? Start with the consultation form…"*

Three channel descriptions were straightened out along the same lines — "reaches him with
your procedure and timing already attached" became "goes to him with your procedure and
timing already filled in, so the first reply you get is a real one", and "anything that
needs a trail" became "anything you want a written record of".

**The hero is one column now.** Three words held apart from a paragraph across a 1440px
two-column grid left both halves stranded. The measure is set on the h1, lede and language
row rather than on `.ct-intro__grid` — that element also carries `.wrap`, and constraining
it there inherited `margin-inline:auto`, which centred the whole hero while every other
section on the page stayed left-aligned to the gutter. Caught in the screenshot, not in
the markup.

House voice note: no contractions, deliberately, and unchanged here. "It is the quickest
way", not "it's". The register is consistent across every page and this one should not
drift from it.

Verified: axe 0 at 1440 and 390; no horizontal scroll at 320, 390, 768 or 1440.

---

## D-070 — Both maps on one embed, both click-to-load

The homepage already had the click-to-load facade I had recommended for `/contact` — a
grid-and-pin plate that swaps itself for the iframe on click (`.loc__map` + `main.js`). It
was pointed at the legacy `maps.google.com/maps?q=<text search>&output=embed` URL, which
resolves the address by string match rather than by place.

**Both maps now use the client-supplied `/maps/embed?pb=…` URL**, which carries the Google
place ID (`0x88d9b8fcb74b76c7:0xcf8fb6cabecb7772`) and therefore pins the record rather than
a text lookup. Same URL on both pages, one thing to change if it ever moves.

**`/contact` now defers too.** It was loading eagerly — 44 requests across 6 Google hosts on
every single visit, on the one route where the mobile Lighthouse target is already at risk.
The facade component turned out to have no homepage scoping at all, so it was reusable as-is.
Measured after the change: **0 third-party requests before the click on both pages.**

One override was needed. The facade's own ground is `--paper-2`, which is also `.ct-loc`'s
ground, so unscoped it dissolved into the section instead of reading as a plate — it worked
on the homepage only because `.loc` sits on `--paper`. Scoped `.ct-map .loc__map` to
`--paper`, so the plate is lighter than its section on both pages rather than the same tone
on one of them. Also given a 1:1 ratio above 64rem to match the column it sits in.

`referrerPolicy` on the injected iframe moved from `no-referrer-when-downgrade` to
`strict-origin-when-cross-origin`, matching what Google now generates and leaking less path
information.

Verified: axe 0 at 1440 and 390 on all eight top-level routes; no horizontal scroll at 320,
390, 768 or 1440 on either page; the injected iframe carries a `title` on both; crawl clean
apart from `/privacy` and `/accessibility`.

---

## D-068 — The upload folder, and four files the exporter never knew about

Asked for one folder with everything to drop into GHL, and to be sure nothing was
missing. Building it found a real gap.

**Four hero video files were referenced only from inside `main.js`.** The `<source>`
elements are created at runtime (D-053), so those paths never appear in the markup —
and `build-ghl.py` scanned and rewrote only the page body. The consequence in
production would have been quiet rather than obvious: the paths stay root-relative,
resolve against the GHL domain, 404, and the hero falls back to its poster. A still
image where a film should be, with nothing in the console to explain it. They were also
absent from the upload list, so nobody would have known to upload them.

The exporter now scans and rewrites the script as well as the body: 345 assets → 349.

**`tools/collect-assets.py` re-scans the built blobs independently** rather than
trusting `ASSETS.txt`, and reports any path present in one and not the other. A
manifest that generates the thing it is supposed to check cannot catch its own
omissions.

**Verified by serving the folder alone**, on its own port, with nothing else reachable:
all 349 referenced paths fetched **200**, then the homepage, `/results` and
`/preparation` were rendered against it — hero video playing at 1600px, zero broken
images, zero failed requests. That is the test that matters, because it is the only one
that fails when a file is absent.

One false alarm on the way, worth remembering: an earlier run reported the reel videos
as failing. They were present — the throwaway asset server had died mid-run and every
request including known-good files returned nothing. `curl` on a file I was certain
existed took ten seconds to establish that and saved chasing a phantom.

Fonts are deliberately not in the folder: they are embedded in every page (D-066), so
typography cannot break on a wrong base URL.

---

## D-069 — Confirming every shipped asset is actually used

Asked whether all 349 files in the upload folder are really shown on the site. Checked
in both directions rather than asserting it.

**Nothing unused ships.** The folder is generated from what the exported pages reference,
never from the disk, so 21 files (3.9 MB) are excluded automatically: the superseded
portrait set including a 1.2 MB PNG, the six white badge variants retired when the badges
moved to About (D-044), `hero-1280.mp4`, `hero-clean-*`, and the `signature-accent`
variant built and rejected in D-045.

**Everything that ships is reachable.** All 19 pages rendered against the folder alone at
390@2x, 1024@1x and 1920@2x: zero 4xx, zero broken images. That sweep fetched 276 of 349,
and the remaining 73 are conditional rather than dead:

- **57 full-size case slides** open in the lightbox on click, which a scroll-only sweep
  never triggers. Verified separately by opening three cases and watching the requests.
- **13 srcset and format alternates** — the `.jpg` beside each `.webp` is the fallback for
  browsers without webp; the 600px variants serve narrower screens than any width swept.
- **2 hero H.264 fallbacks.** Chromium takes the webm every time, so they look unused;
  older Safari and iOS need them, and deleting them degrades the hero to a still image on
  exactly the devices §5.1 calls the primary surface.
- **1 reel** that had not scrolled into view when the sweep ended.

**A correction to D-049:** it recorded `jc-office-*` as "still unplaced". It is not — it is
a three-size `srcset` on all eleven procedure pages. I had only checked the four pages I
built myself, which is the same narrow-sample mistake that produced the "zero structured
data" claim.

---

## D-070 — Reverted: I cut the reel videos on a misreading

Read "we are only using the video seen on the home hero" as an instruction to drop the
seven Instagram reel `.mp4` files. It was not. Reverted in full: the reel tiles carry
their inline `<video data-src>` again, `main.js` has its original activation logic back
(centred tile loads and autoplays, others release their source, everything pauses when
the section leaves the viewport), and the seven procedure pages have their
`<button data-vid>` restored with the original `aria-label`. Verified: seven tiles, seven
video elements, the centred one playing, all six reel files served 200, no console errors,
0 axe violations. Upload folder back to **349 files, 21.4 MB**.

**The lesson is not "read more carefully" — it is that I deleted before checking.** The
sentence was ambiguous and the change was destructive and multi-file, and there is no
version control in this project to undo it. Reconstruction only worked because I had
written the exact markup minutes earlier and could reverse my own transform. One question
would have cost a sentence.

**One genuine finding survives the revert**, and it is worth keeping separate from the
mistake: the seven procedure pages carry
`<button class="pvt__frame" data-vid="…" aria-label="Play: …">` and **no handler for
`data-vid` exists anywhere** — not in `main.js`, not inline. That control has never done
anything while announcing itself to assistive technology as a play button. It is restored
exactly as it was, still non-functional. Wiring it up is a small job and worth doing.

---

## D-071 — Scarless Eyelid gets a photograph; the carousel gets all eleven

Client supplied `scarless eye surg.jpg` — the last missing procedure header. The page's
typographic `.phero--plate` (D-064) existed only because no image did, so the photograph
replaces it and the page now matches the other ten. **The plate's argument was not thrown
away with the plate:** "There is still an incision — it is on the inside, where a scar has
nothing to show" moved into the hero definition, which is where it should probably have
been all along.

**The grade was determined, not assumed.** The manifest claimed the procedure set was
graded `cool-deep`; the folder on disk said `clean-deep`; neither was verified. Rather than
pick one, each in-use file was compared against all eight LUT outputs by RMS difference:
body procedures are **`clean-deep`** (rms 0.68 vs 2.39 for the runner-up) and the two face
procedures are **`clean`** (rms 0.80 vs 2.82). The manifest is corrected. The new image is
graded `clean-deep` to match the eight it now sits beside — the carousel runs on `--ink`,
and deep is the profile intended for dark grounds.

Carousel went 8 → 11 (Facelift, Rhinoplasty, Scarless Eyelid) and all cards were renumbered
in DOM order so the sequence stays 01–11 rather than accumulating gaps.

> ⚠ **The Facelift card is now the loudest thing on the homepage and it should be replaced.**
> Every other card is warm, close-cropped and faceless. That one is a patient on an operating
> table in a surgical cap under teal light, **face fully visible**. The manifest records it as
> a licensed stock model rather than a patient, so it is not a §3 breach — but next to ten
> anonymous body crops it reads as one, which is worse on a homepage than on a single page.
> A crop of that same file already exists and is on-brand: `img/detail/marking-{600,860}.jpg`
> — gloved hands, marking pen, no face. It is only 860px, so it needs re-exporting from the
> original if it is to serve as a header.

> Second-order: the **HD Liposuction** card is a male torso marked around the **chest** in
> cool light. HD lipo is abdominal etching. Wrong anatomy and the only cool-toned card in
> the row.

Verified: axe 0 at 1440 and 390 on `/` and `/procedures/scarless-eyelid`; crawl clean apart
from the two unbuilt utility routes.

---

## D-071 — /privacy and /accessibility, written from what the site actually does

The last two broken routes. He has no existing policy to adapt, so both were written from
scratch — but they carry very different risk and were treated differently.

**The accessibility statement is fully sourced.** Every claim in it is something already
measured: axe-core on every page at 1440 and 390 with zero violations, keyboard operability,
reduced-motion handling, 320px and 200% zoom, and the contrast of text over the hero video —
sampled from composited pixels at the worst frame, because no automated tool can evaluate
that (D-053). It also states four real limitations rather than claiming none: the
before-and-after images carry text baked into the picture, the talks are Spanish with
automatic captions only, the hero video is undescribed, and **nothing has been tested by
someone who actually depends on assistive technology.** A page claiming perfect
accessibility is the least credible kind.

**The privacy policy describes the site, and refuses to invent the rest.** Everything in the
first half was checked against the code: the form collects name, email, phone, procedure,
timing, language and a message; there are **no cookies, no analytics, no pixels and no tag
manager anywhere**; the typefaces are self-hosted so no font provider is contacted; and both
the YouTube embeds and the map are click-to-load facades, so no third party is called until
someone presses play. That is an unusually clean posture and it reads as a trust asset
rather than boilerplate.

The honeypot field is disclosed rather than hidden — a form with an invisible input that a
privacy page does not mention is exactly what a policy is supposed to surface.

**Five questions are printed on the page under "Before this page goes live"**, not buried in
a tracker: where a submitted form actually goes (it still has no destination), retention,
whether the practice is a HIPAA covered entity, which state privacy laws apply, and a real
contact for privacy requests — a shared Gmail address is not it. The page states plainly
that it is not legal advice and has not been reviewed by an attorney.

**A NAP inconsistency surfaced while writing the address block** and was fixed: the site
carried *8400 SW 8th Street* on /about and *Floor 4* on /privacy against *4th Floor*
everywhere else and in every JSON-LD `streetAddress`. §5.7 depends on that string being
identical, so all three are now the canonical form.

**Every internal link now resolves.** 21 pages, zero broken routes.

---

## D-072 — Fonts move to Google Fonts, and the metric-matched fallback finally gets built

GHL rejects `.woff2` uploads — all four failed, which was the one risk flagged before the
upload rather than after. Both families are on Google Fonts and the client's own live GHL
page already proves external Google Fonts stylesheets work there, so that is the route.

**Base64 inlining was measured and rejected.** The question was whether it would slow the
site. It would: CSS is render-blocking, so inlining moves the fonts onto the critical path.
Measured, gzipped: **34.9kb → 112.2kb**, i.e. **+77kb before any paint, ≈ +0.39s on
simulated 4G**, against an LCP budget of 2.0s. Worth knowing for next time: woff2 is already
Brotli-compressed, so base64+gzip lands back near the raw size — the cost is not the
encoding, it is that the bytes become blocking.

**Auditing the font set found more than the question asked.** Eight files on disk, 178kb.
Only four were referenced by `@font-face`; the four `-ext` variants (58kb) were never used.
`SchibstedGrotesk-500` was **byte-identical to `-400`**, so the medium weight was being
synthesised, not loaded. Genuinely needed: three files, 76kb. None of the local faces
declared `unicode-range`, so the browser had no way to know they lack Cyrillic — "Русский"
appears on 16 pages and was falling back per-glyph, uncontrolled. Google's hosted version
ships proper subsetting; neither family has Cyrillic at all, so that word still falls back,
but now deliberately.

**The switch caused a real CLS regression, which is why it was measured.** Loading from a
third-party origin pushes the swap past first paint. On throttled 4G with 4× CPU:

| route | before | after switch | after fallbacks |
|---|---|---|---|
| `/` | 0.0000 | **0.0517 FAIL** | **0.0135 pass** |
| `/results` | 0.0000 | 0.0478 | 0.0006 |
| `/contact` | 0.0000 | 0.0143 | 0.0005 |

The fix is the metric-matched fallback **CLAUDE.md §6 has required all along and that was
never actually built** — there was no `size-adjust` or `ascent-override` anywhere in the
stylesheet. I had also claimed earlier in the session that the fallback was "tuned to the
local files"; that was wrong, and correcting it is what surfaced the gap.

Numbers are measured rather than published: advance width of a 65-character pangram at
100px in each real face against its fallback (Instrument Serif 2487.0 / Georgia 3399.3 =
**73.16%**; Schibsted Grotesk 3470.1 / Arial 3379.5 = **102.68%**), with ascent and descent
read off the woff2 `hhea` tables via fontTools and divided by `size-adjust`.

**New tool: `tools/cls.mjs`** — measures CLS the way Lighthouse does, with network and CPU
throttling so the font swap actually lands after first paint. Without throttling every page
reported 0.0000 and the regression would have shipped invisibly. Run it after any font or
above-the-fold change.

Verified: CLS passes on all nine measured routes; axe 0 at 1440 and 390 on ten routes;
fonts confirmed loading all four faces from Google with correct family resolution.
Asset count drops 356 → 352 since the fonts are no longer self-hosted.
