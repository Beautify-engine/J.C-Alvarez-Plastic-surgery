# Asset request — what we need to collect

Derived from his existing site architecture, simplified per `docs/IA.md` Part 2.
Status as of 2026-08-20. **✅ have · ⚠️ have but not usable as-is · ❌ need**

Every acquired asset gets a row in `MANIFEST.md` with source, rights, and patient flag.
Anything flagged `patient: yes` is preview-only — never a public URL (CLAUDE.md §3).

---

## 1 · Video

| # | asset | spec | status |
|---|---|---|---|
| V1 | **Hero loop** | 6–10s, 1920×1080, no audio, seamless | ⚠️ **have footage, needs a proper cut** — see §Video notes |
| V2 | Hero poster frame | 1920×1080 still, matches loop frame 0 | ✅ derived |
| V3 | Facility / atmosphere loop | 6–8s — exterior, reception, OR, recovery | ❌ |
| V4 | 3–6 procedure explainer clips | 30–90s, for procedure pages | ✅ **RESOLVED 2026-08-22 — 202 uploads catalogued in `content/youtube-catalog.md`.** All 11 procedures covered, plus 26 prep/recovery clips. Embedded, not re-hosted. ⚠️ most recent audio is Spanish-only |
| V5 | Surgeon-to-camera intro | 45–60s, subtitled EN/ES/RU | ✅ **have** — 29s clip, transcript in `content/facts.md` |
| **V6** | **Objection-answer videos — HIGHEST-VALUE VIDEO ASK** | 3–4 clips, 45s each, him to camera: *"Will it look done?"* · *"What is recovery really like?"* · *"Am I a candidate?"* · *"What happens at the consultation?"* | ❌ **one hour of filming; would be the best-converting video on the site** |

## 2 · Photography — the surgeon

| # | asset | spec | status |
|---|---|---|---|
| P1 | Primary portrait, environmental | ≥3000px, in scrubs or OR | ✅ 4 exist (`jc-alvarez-md-plasticsurgeon.png` 800×1120 etc.) — ⚠️ **too small**, need originals |
| P2 | Secondary portrait, formal | ≥3000px | ⚠️ same |
| P3 | Him working — hands, marking, consulting | 6–10 frames, ≥2400px | ❌ (video frames could stand in) |
| P4 | Him teaching / with the book | 2–3 frames | ❌ |

## 3 · Photography — team & facility

| # | asset | spec | status |
|---|---|---|---|
| T1 | Team group | ≥3000px | ✅ `about-us-banner-desktop.jpg` 1500×1734 — ⚠️ small |
| T2 | Individual headshots, consistent treatment | 3–5 people, ≥2000px square | ⚠️ exist at 2000×1400, inconsistent |
| F1 | Exterior / building & signage | ≥3000px | ❌ |
| F2 | Reception & waiting area | 2–3 frames | ❌ |
| F3 | Consultation room | 2 frames | ❌ |
| F4 | Operating room | 2–3 frames | ❌ |
| F5 | Recovery / hyperbaric chamber | 2 frames | ✅ `hiperbaric-chamber-equipment.jpg` 1300×1300 |

## 4 · Before / after — the conversion driver

| # | asset | spec | status |
|---|---|---|---|
| BA1 | **Unwatermarked originals of all 68 cases** | full res, consistent angles | ❌ **highest-value ask** |
| BA2 | Per-case metadata | procedure, age band, time post-op, technique | ❌ |
| BA3 | Signed patient releases covering web use | — | ❌ **blocks public deployment** |
| — | *Fallback* | the 68 existing 1200×1200 watermarked slides | ✅ usable for the gated preview |

Current coverage: BBL 9 · Breast aug 8 · Rhinoplasty 7 · Facelift 7 · Tummy tuck 7 ·
Eyelid 7 · HD lipo 6 · **14 never displayed**. Target ≥8 per procedure.

## 5 · Brand

| # | asset | spec | status |
|---|---|---|---|
| B1 | Logo — vector | **SVG**, horizontal + stacked | ❌ only `logo-Dr-JC-Alvarez.png` 800×185 raster |
| B2 | Logo — reversed for dark bands | SVG | ❌ |
| B3 | Monogram / favicon mark | SVG, legible at 16px | ❌ |
| B4 | Favicon set + touch icon | 32/180/512 + `site.webmanifest` | ❌ |
| B5 | OG / social share image | 1200×630 | ❌ |
| B6 | Brand colour + font spec, if one exists | — | `[[VERIFY: does he have brand guidelines?]]` |

## 6 · Credentials & trust

| # | asset | spec | status |
|---|---|---|---|
| C1 | ABPS mark | SVG or ≥1000px | ✅ raster only — ⚠️ need vector + usage rights |
| C2 | American College of Surgeons (FACS) | same | ✅ raster |
| C3 | ASPS | same | ✅ raster |
| C4 | RealSelf Top Doctor | same | ⚠️ **year-scoped, expires** — confirm current |
| C5 | Facility accreditation (AAAASF / QUAD A / JCAHO) | — | ❌ `[[VERIFY: which, if any]]` |
| C6 | Hospital affiliation marks | — | ❌ |
| C7 | Press / featured-in logos | SVG | ❌ Post-Gazette at minimum |
| C8 | Book covers — both editions | ≥2000px | ✅ `behind-the-mirror.png`, `Detras-del-espejo.png` |

## 7 · Symbols & section assets

Kept deliberately minimal — icon soup is barred (§4), and the banned-tells list rules out
Lucide/Heroicons and emoji.

| # | asset | spec | status |
|---|---|---|---|
| S1 | **Procedure marks** — 11, custom line, single weight | SVG, 24px grid, `currentColor` | ❌ **commission or draw** |
| S2 | UI glyphs — arrow, chevron, close, filter, play, globe, phone, pin | SVG sprite, one weight | ❌ draw (8 only) |
| S3 | Hairline rule / divider motif | CSS, no asset | ✅ tokenised |
| S4 | Gallery placeholder set | 1200×1200 ×68, correct aspect | ❌ generate |
| S5 | Procedure page header images | 11 × ≥2400px wide | ⚠️ 5 exist (`Rhinoplasty.jpg` etc.) — `[[VERIFY: are these patients?]]` |
| S6 | Preparation section imagery | 6 × ≥2000px — nutrition, movement, recovery | ⚠️ currently Envato stock; **his licence, not ours** — relicense or reshoot |
| S7 | Map / location still | static, no third-party embed on first load | ❌ |

## 8 · Copy & documents

| # | asset | status |
|---|---|---|
| D1 | Verified credential documents (board cert, licence, FACS, PhD) | ❌ **blocks the trust strip** |
| D2 | Signed testimonial releases, or a decision to ship none | ❌ **currently blocked** |
| D3 | Procedure pricing bands, if he'll publish them | ⚠️ **one figure found — see PP6** |
| D4 | Real consultation destination — inbox or CRM | ❌ **blocks definition of done** |
| D5 | ES + RU translation sign-off by a native speaker | ❌ |

---

## Video notes — the footage supplied 2026-08-20

`assets/hero video.mp4` — 1920×1080, H.264, **19.05s, 20.8MB, 8.5 Mbps, with an audio
track, `moov` atom at the end** (so a browser must download all 20.8MB before the first
frame). Transcoded to `src/public/video/` at **719KB / 295KB / 291KB** with faststart,
audio stripped.

**Shot map (1fps):**

| time | content | usable in an autoplay hero? |
|---|---|---|
| 0–5s | marking a patient's abdomen, patient in underwear | **no** — identifiable patient, and it sets a body-contouring-volume tone |
| 6–8s | him seated with a patient, clothed | no — patient's face is identifiable |
| **9–10s** | **him in scrubs with a colour chart, patient not identifiable** | **yes** |
| **11–12s** | **him at the desk, consulting, patient back-of-head only** | **yes — the strongest frames in the reel** |
| 13–16s | intraoperative abdomen on surgical drape, incision visible | **no** — graphic for an autoplaying homepage |
| 17–19s | him with a patient in a green dress, result reveal | no — identifiable patient |

**The current cut uses 8.9–12.9s** — the dignified window. It is only 4 seconds, which is
short for a loop.

**Three things to resolve:**

1. **Consent (§3).** Every clip contains real patients. Consent for an Instagram reel does
   not extend to a third party republishing on a new domain — the same rule as the 68
   before/afters. The current cut minimises this (no identifiable patient), but footage
   with faces stays preview-only until releases exist.
2. **Tone.** Autoplaying surgical incisions and underwear body-marking is a bounce risk
   for the demographic §4 targets, and it is New Life's volume-BBL vocabulary rather than
   editorial luxury.
3. **Length.** 4 usable seconds. **Ask: 20–30s of B-roll of him consulting, gowning,
   marking (cropped above the shoulders), and the facility.** That is one hour with a
   camera and it upgrades the hero permanently.

---

## 9 · Procedure pages — what the template needs, per procedure

Added 2026-08-22 after building the tummy tuck template
(`src/public/procedures/tummy-tuck.html`). Every slot below is real in the build; the
ones marked ❌ currently render a `[[VERIFY: …]]` placeholder in the page.

| # | asset | why the template needs it | status |
|---|---|---|---|
| **PP1** | **Case → procedure map + per-case metadata**: `filename · procedure · age band · months post-op · combined procedures` | Fills the case chart and every `alt` string. 14 of the 68 slides were never displayed anywhere, so we cannot infer them. | ❌ **highest-value 20 minutes he can spend** |
| **PP2** | **Re-cropped case pairs from the unwatermarked originals** | The current `/img/cases/*-b|-a.jpg` are split halves of composite slides: the two angles are misaligned and the watermark is visible mid-frame. Legible at 150px, poor at full stage width. | ⚠️ usable, visibly imperfect |
| **PP3a** | **Two videos on his own channel are unusable as published** | `W2I3Qg0GxEo` ("Learn about Scarless lower eyelid surgery") has an auto-generated thumbnail frame showing **an identifiable patient mid-operation** — YouTube picks that frame, he did not, and it is what appears wherever the video is shared. `uimnyUSJdDI` is a **patient testimonial** filmed with the patient on camera. Both were rejected for the scarless page. Worth him knowing regardless of this project. | ❌ **flag for the pitch meeting** |
| **PP3b** | **Stale contact details in the back catalogue** | At least two video descriptions still carry **(412) 638-2391** and *renova-plasticsurgery* — his former Pittsburgh practice. Confirmed on `uimnyUSJdDI` and `KmqoQzP1awo`. A scripted pass over all 202 descriptions found no others, so this is cleanup, not a pattern. | ❌ small, 10 minutes |
| **PP3c** | **184 of 202 video descriptions carry no contact details at all** | Only 17 mention the Miami number or the site. That is 202 assets ranking on YouTube search with nowhere to send anyone — the cheapest local-SEO win available to him (§5.7), and entirely his to make. | ❌ **recommendation, not a blocker** |
| **PP3** | Procedure explainer video | ✅ **found on YouTube** — the slot now embeds `OnmNtCUuglI` (25:39, English) + `fZx_V94QQU0` (6:26, Español). See `content/youtube-catalog.md`. | ⚠️ **need one English-audio recording newer than 2021** — everything current is Spanish |
| **PP4** | Recovery specifics he will sign off on | Drains out at ?, nicotine-free window, pain protocol. Everything else in the timeline came off his current site. | ❌ 3 unknowns on this page |
| **PP5** | Complication rate and revision policy | The risks section names both and shows a placeholder rather than a guess. | ❌ |
| **PP6** | Price band per procedure | The cost slot ships or gets cut; a fabricated range is worse than silence. **First figure found anywhere:** his own blog post *"Lift alone or lift with implants"* publishes **"Lift averages $4,000–$8,000; add $2,000–$4,000 for implants."** It is sourced — but it is a blog estimate, not a quote from his practice, and it is undated. **Not published on any page.** One yes/no from him turns the cost block on for two procedures. | ⚠️ **one ask away** |
| **PP7** | Header photography for **Scarless Eyelid Rejuvenation** | Down to one. Facelift and Rhinoplasty were supplied. Scarless Eyelid now ships a typographic plate instead of a photo (D-064) — it works, but a real lower-lid or laser image would be better. **Do not send a stock face.** | ⚠️ 1 of 11 |
| **PP8** | Confirmation that the 5 existing procedure banners are not patients | `Rhinoplasty.jpg`, `Abdominoplasty-scaled.jpg`, `2021-01-05-Blepharoplasty.jpg`, `Breast-aug-lift-.jpg`, `2021-05-24-HD-Liposuction…png` | ❌ `[[VERIFY]]` |
| **PP9** | Reviews, per procedure, with source URLs | His old template had a reviews block on every procedure page. Ours ships the section absent rather than fabricated. | ❌ **blocked** |

### Sourcing note for `content/facts.md`

The tummy tuck page publishes clinical specifics — operating time, shower at day 5, desk
work 10–14 days, compression 8 weeks then part-time 4–6, Florida's 1-litre cap, possible
permanent numbness. **All of it is his own published copy**, from
`https://www.jcalvarezplasticsurgery.com/top-tummy-tuck-abdominoplasty-in-miami-fl-dr-jc-alvarez/`
(captured 2026-08-20, full text in `content/_extracted/full/`).

Per CLAUDE.md §2 every claim on the site traces to `facts.md` with a source URL, and per §7
`facts.md` is not edited without flagging first. **Flagged: it needs a "Procedure clinical
specifics" section keyed by procedure, with that URL as the source.** Say the word and it
goes in.

### ⚠ Conflict surfaced by the YouTube catalog — blocks the recovery section

`content/youtube-catalog.md` turned up **`lfUDnaabfEM` — "Why I prohibit the compression
garment for the first month after a tummy tuck."** His website says the opposite: binder
on before you wake up, full-time, for the first month, then a faja for two more.

Our recovery timeline currently publishes the **website** version, because that was the
only source we had. Two of his channels give opposite post-operative instructions.

**Ask him which is current.** Until he answers, the compression rows on
`/procedures/tummy-tuck` are the one thing on that page I would not put in front of a
patient. Everything else on it traces cleanly to a single source.

### Also worth 20 minutes of his time

The Shorts library is 135 clips of him answering exactly the objections
`docs/conversion-doctrine.md` names — Ozempic before surgery, why fat is lost after a BBL,
fibrosis, fainting post-op, smoking. D-015 asked him to *film* objection answers. He has
been filming them for two years. Sourcing and subtitling beats commissioning.

## Added 2026-08-24

- **Signature scan** — his handwritten signature on white, photographed or scanned, ideally
  300dpi+. Needed for the About-section note. There is no substitute: a drawn or generated
  signature on a physician's site is forgery, so the slot ships as a visible
  `[[VERIFY: signature scan]]` placeholder until he supplies one.
- **Official reverse (white) artwork** for the ABPS, ASPS and ACS marks, if he ever wants
  them on a dark ground. Not currently needed — the marks now sit on paper in About (D-044).
- **Approval on the About note** — it is written in his voice and signed with his name.

---

## ⚠ BLOCKER — the deployed hero video shows identifiable patients

Found 2026-08-24 while rendering the hero options. **The §Video notes above are wrong**
and should be read with this correction.

Those notes record that the deployed cut uses **8.9–12.9s** of `assets/hero video.mp4` —
"the dignified window", "no identifiable patient". The file actually deployed at
`src/public/video/hero-1920.mp4` is **12.32s** and contains:

| in the deployed file | content |
|---|---|
| 0–3s | body marking, patient in underwear, identifiable |
| ~6s | a patient standing beside him, **face fully visible** |
| ~9s | a patient in a chair, **face visible** |

**This is on the homepage hero, autoplaying.** Under §3 the consent covering his own
Instagram does not extend to a third party republishing on a new domain — these are
precisely the images the rule exists for. Nothing is publicly reachable today (localhost,
`noindex` on every page), so there is no live exposure, but **it must not reach the
preview URL in this state.**

**The original was also more limited than the notes claim.** At 9–10s the patient's face
is fully visible. The genuinely clean window is **11.0–12.85s — under two seconds.**

**A safe cut already exists**, ready to swap in:
`src/public/video/hero-clean-1920.mp4` — 11.0–12.85s, slowed 2×, 3.7s, 553KB, faststart,
audio stripped, poster at `src/public/img/hero-clean-poster.jpg`. Every frame verified:
him at the desk, patient back-of-head only.

**The homepage has not been changed** — that is approved work and the swap needs a
decision. Two options:

1. Point the homepage hero at the clean clip. 3.7s is a short loop but it is safe today.
2. Drop to the poster still until better footage exists.

Either way this reinforces **V1/V6**: 20–30s of B-roll of him gowning, marking (cropped
above the shoulders), consulting and walking the facility. One hour with a camera and the
hero stops being a compliance question.
- **English cover artwork** for *Behind the Mirror*. Only the Spanish *Detrás del Espejo*
  cover has been supplied (`assets/Book.png`, 2026-08-25), so the /about book section shows
  one cover where it should show two.
- **Imprint details for the book** — publisher, publication date, page count, ISBN. Not
  currently stated anywhere on the site, so nothing is unverified on the page; but the
  section would be stronger with a real date on it.

## Pulled OFF the pages 2026-08-25 — needed before launch

Visible `[[VERIFY]]` chips were removed from all pages at the client-side lead's request.
Nothing unverified was left standing in their place; the claims came off with the markers.
These are now asks, not page furniture:

- **Opening hours.** Removed from the footer on all three pages and from the homepage
  location block. Not in `facts.md`, so nothing is shown at all.
- **Former President, Greater Pittsburgh Society of Plastic Surgery (2018–2020).** Removed
  from /about entirely. Asserted only on his own site, never corroborated — and an
  unverified credential with its marker deleted is worse than no credential.
- **The interview photograph's provenance** — outlet, interviewer, date. The caption now
  says only what the photograph shows: "Interviewed on camera."


### Hero footage re-supplied 2026-08-25 — same reel, now 4K

`assets/hero video.mp4` was replaced by **`assets/hero vid.mp4`** — 3840×2160, 14.85s,
29MB. **It is the same footage, re-exported at 4K**, not new material.

- **The §3 blocker above stands unchanged.** Frames sampled across the clip still show
  body marking with an identifiable patient (0–2s), patients with faces visible (4s, 6s,
  12–14s) and intraoperative abdomen (10–12s).
- **The clean window is 7.0–9.2s** in the new file &mdash; him at the consulting desk,
  patient back-of-head only. About two seconds, same as before.
- `src/public/video/hero-clean-1920.mp4` has been **re-cut from the 4K source**
  (7.0–9.1s, slowed 1.8×, 3.8s, 690KB, faststart, audio stripped) and is sharper than the
  1080p version it replaces.
- The 4K source also produced a much cleaner still for the **rhinoplasty header**
  (`img/procedures/rhinoplasty-*.jpg`), cropped from 8.2s.

**Still outstanding, and the reason this keeps recurring: V1/V6.** 20–30s of B-roll of him
gowning, marking cropped above the shoulders, consulting and walking the facility. One
hour with a camera retires this problem permanently.
- **`hiperbaric-chamber-equipment.jpg`** (1300×1300) — catalogued in his WordPress media
  library but never downloaded. The /preparation page argues the hyperbaric case in words
  and has no photograph of the chamber to show for it. Also worth pulling from the same
  library: `exosomes.jpg`, and any photograph of the accredited surgical facility.
