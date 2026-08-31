# IA — current state (extracted 2026-08-20)

Not a proposal. This is what exists today, so the Phase 2 rebuild has a baseline.
Proposed IA lands in Phase 2.

## Scale

| | EN | ES | RU | total |
|---|---|---|---|---|
| Pages | 37 | 29 | 25 | 91 |
| Posts | 50 | 3 | 0 | 53 |
| **Total URLs** | | | | **144** |

No `hreflang` on any of the 154 URLs — the three language trees are unlinked and compete
in search.
RU pages use percent-encoded Cyrillic slugs
(`/ru-%d0%bb%d1%83%d1%87%d1%88%d0%b5%d0%b5-…`), which are unreadable, unshareable, and
truncate badly in SERPs.

## Current navigation (mega-menu, ~35 items, 5 groups)

```
Home
About ─┬─ Board Certification
       ├─ Choosing your Surgeon
       ├─ Plastic Surgery Cost
       ├─ Why Miami?
       ├─ Why Dr. JC Alvarez?
       └─ Miami's Top Plastic Surgeons
Prepare ┬─ 90 days preparation      ← the differentiated content, buried here
        ├─ Gluteal Muscle Training
        ├─ Nutrition
        ├─ Pain Management
        └─ Supplements
Procedures ┬─ Brazilian Butt Lift
           ├─ Skinny BBL
           ├─ Breast Aug
           ├─ Breast Lift Aug
           ├─ Eyelid Surgery
           ├─ Scarless Eyelid Rejuvenation
           ├─ FaceLift Surgery
           ├─ Face Rejuvenation Blueprint
           ├─ Liposuction HD
           ├─ Rhinoplasty
           └─ Tummy tuck
SPA Services ┬─ Hyperbaric Oxygen Therapy
             ├─ Hair Smart Regrowth
             └─ Skin rejuvenation
Gallery · Blog · Contact · FAQ · Videos · Language (Espanol / Русский)
```

## Structural problems

1. **Gallery is one nav item and shows none of his results.** He has 68 patient
   before/afters; `/gallery/` displays 17 stock spa photos and zero of them. The 44
   deployed cases are buried 6–9 at a time inside procedure pages, so no visitor can
   browse results across procedures. §5.2's primary conversion driver exists as assets
   and not as a destination. See `docs/competitive-teardown.md`.
2. **Three overlapping top-level buckets** — `/services/`, `/procedures/`, and
   "SPA Services" — with unclear boundaries. `/services/` has 307 words; `/procedures/`
   has 896. Neither is a real hub.
3. **"Prepare" is the best content and the worst-placed.** It should be a visible pillar,
   not a dropdown.
4. **"About" is a content farm, not a bio.** Four of its six children ("Plastic Surgery
   Cost", "Why Miami?", "Miami's Top Plastic Surgeons", "Choosing your Surgeon") are SEO
   landing pages, not information about him. The actual bio is at `/about-2/` — a slug
   that means the original `/about/` was lost and never redirected.
5. **Blog cannibalizes procedure pages.** 53 posts, many "101 course" explainers, target
   the same queries as the money pages.
6. **Language switching is last in the nav**, after FAQ and Videos. In a trilingual
   Miami market that is backwards.
7. **A published `/404-2/` page** sits in the sitemap as a real indexable URL.
8. **Trust signals are stranded.** ABPS, American College of Surgeons, ASPS, and
   RealSelf Top Doctor logos appear on exactly one page of 154 — not the homepage, not
   any procedure page. §5.4 wants them above the fold everywhere.

## Redirect debt to carry into the rebuild

Any migration must map: `/about-2/` → new about; the `TOP …` procedure slugs → clean
procedure slugs; percent-encoded RU slugs → readable `/ru/…` paths; `/404-2/` → removed
from sitemap. Full mapping is a Phase 3 deliverable.

---
---

# PART 2 — PROPOSED IA (Phase 2)

Everything above is the current site. Everything below is the rebuild.

Governing constraints: gallery is the #1 driver and never more than one tap from home
(§5.2) · the surgeon is the product (§5.3) · trust signals above the fold on every page
(§5.4) · exactly one primary CTA, "Request a Consultation" (§5.5) · nothing gated (§5.6)
· mobile is the design surface (§5.1).

## Route map

```
/                          Home
/results                   ★ Gallery — filterable by procedure, ungated
/procedures                Hub
/procedures/[slug]         11 procedure pages, unique title/meta/H1
/about                     The surgeon — the Post-Gazette story
/preparation               Hub — his differentiator, promoted out of a dropdown
/preparation/[slug]        90-day prep · nutrition · supplements · pain · training · risks
/book                      ★ Multi-step consultation request
/contact                   NAP, map, hours
/es/… /ru/…                Full mirrors, hreflang + x-default
```

Down from 154 URLs to roughly 30 per language. The 53 thin "101 course" blog posts fold
into the procedure and preparation pages they cannibalise.

**Nav: 5 items.** Results · Procedures · Preparation · About · Contact — plus a persistent
"Request a Consultation" and a language switcher **promoted to the header**, not buried
after FAQ. Five items, no mega-menu, no fifth-level dropdown.

## Homepage — section by section, in mobile order

| # | section | why it exists |
|---|---|---|
| 1 | **Hero** — his real portrait, name + credential line, one CTA, city | §5.3. Replaces a stock photo of a woman getting a facial with the actual product: him. |
| 2 | **Trust strip** — board certification, years practising, documented cases, book, languages spoken | §5.4, above the fold. Every value pulled from `facts.md`; anything unverified does not render. |
| 3 | **Results** — 8 cases, procedure-filtered, "See all 68" | §5.2. High, because it is the thing that sells. One tap to the full gallery. |
| 4 | **"I need help with…"** — goal-based entry | Borrowed from 5C. A first-timer knows "my stomach after two kids," not "abdominoplasty." Routes to procedures. |
| 5 | **The surgeon** — condensed Post-Gazette story + portrait, link to /about | 180 babies in a war zone; four months unpaid at a Harvard lab. This is the differentiator no Miami competitor can copy. |
| 6 | **Procedures** — restrained grid, 11 items | Navigation, not sales. Sales already happened in §3 and §5. |
| 7 | **Preparation** — "how we prepare you," 3 entry points | His genuine clinical substance, currently buried. Maps to §4's "restraint and evidence." |
| 8 | **The book** — *Behind the Mirror* / *Detrás del Espejo*, both editions | First-rank trust signal (§5.4) currently on zero pages. |
| 9 | **Reviews** — `[[BLOCKED]]` pending verification | Renders only if real numbers clear `facts.md`. Ships absent rather than fabricated. |
| 10 | **Closing CTA + NAP + footer** | `Physician` + `MedicalBusiness` + `LocalBusiness` JSON-LD lands here (§5.7). |

Sections 9 and 10 are the only ones that may collapse. If reviews stay unverified the
page ends at 8 and loses nothing.

## Procedure page template

Above the fold: H1, one-line plain-language definition, **his cases for this procedure**,
trust strip, CTA. Then: what it addresses · his technique and why · candidacy (honest,
including who is *not* a candidate) · recovery timeline linked to the preparation
content · risks stated plainly · cost guidance · FAQ · CTA.

Risks and non-candidacy stated openly is the §4 "restraint and evidence" thesis doing
conversion work — it reads as a surgeon, not a marketer. Zero superlatives; the 33
instances of "best" and the "TOP" prefixes do not survive.

## Gallery — the priority build

Filterable by procedure, ungated, lazy-loaded below the fold, keyboard-operable, real
`alt` text per case. Built against **1200×1200 placeholders at true case counts** so
layout, filtering and loading are all genuinely exercised; real cases appear only in the
access-controlled preview (§3). Presented on the dark ground so his black-background
composites sit natively.

## Booking flow — /book

Multi-step, one question per screen on mobile, progress visible, back always available,
no dead ends. Steps: **procedure of interest → preferred timing → contact details →
review and submit.** Validated inline, honeypot + rate limiting + a captcha that does not
require solving puzzles, submissions to a real endpoint with an email receipt.

> **Deliberately NOT collected: medical history, current medications, weight/BMI, or
> patient photographs.** A consultation request is not an intake form. Collecting health
> data drags this into HIPAA scope and adds a breach surface for a site that has no
> business holding it. Clinical detail belongs in the consult, not a marketing form.
> Flagged for him: New Life's funnel gates on BMI; we are choosing not to.

## Trilingual

Full EN/ES/RU mirrors, reciprocal `hreflang` plus `x-default`, readable Latin-transliterated
RU slugs replacing the percent-encoded Cyrillic, language switcher in the header
preserving the current route. Fixes a 154-URL sitewide defect and it is a real Miami
advantage — currently implemented as three sites competing with each other.

## What this fixes, measured

| defect (current) | after |
|---|---|
| 0/154 meta descriptions | unique per route |
| 0/154 JSON-LD | Physician + MedicalBusiness + LocalBusiness |
| 0/154 hreflang | reciprocal + x-default |
| 85/154 missing `<h1>` | exactly one per page |
| 2,804 images `alt=""` | real alt, `alt=""` only when decorative |
| 610 images without dimensions | every image space-reserved |
| gallery with 0 of his 68 cases | all 68, filterable, one tap from home |
| trust logos on 1 of 154 pages | trust strip on every route |
| 4 competing CTA phrasings | one, everywhere |
| booking sent to New Life's funnel | his own endpoint |
