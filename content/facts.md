# facts.md — every factual claim, with source and verification status

**Rule (CLAUDE.md §2):** nothing ships to the site unless it appears here with a
source. Unverified items carry `[[VERIFY: …]]` and must NOT be published as fact.

Source key — `CLIENT-SITE` = claim made on jcalvarezplasticsurgery.com (a *claim*,
not a verification). `PRIMARY` = independent authoritative source. A claim is only
publishable when it has a PRIMARY source.

Extracted 2026-08-20 from https://www.jcalvarezplasticsurgery.com/

---

## Identity / NAP

| Field | Value | Source | Status |
|---|---|---|---|
| Legal name | Julio Clavijo Alvarez, MD | CLIENT-SITE /about-2/ | confirmed by user |
| Display name used on site | "Dr. JC Alvarez" | CLIENT-SITE | confirmed |
| Practice name | J.C. Alvarez Plastic Surgery | CLIENT-SITE | confirmed |
| Street | 8400 SW 8th St, 4th Floor, Miami, FL | CLIENT-SITE | **CONFLICT — see below** |
| ZIP | **33144** | **RESOLVED 2026-08-22** — Google Maps place record for 8400 SW 8th St returns 33144 | confirmed |
| Phone | 786-795-2113 / +17867952113 | CLIENT-SITE | confirmed, consistent |
| Email | drjcalvarez.plasticsurgery@gmail.com | CLIENT-SITE | confirmed (see teardown — not a branded domain) |

> **RESOLVED — use 33144.** His site published both `33144` and `33146`. The Google Maps
> place record supplied by the client-side lead on 2026-08-22
> (`maps/place/8400+SW+8th+St,+Miami,+FL+33144`) returns **33144**, and Google's own record
> is what drives local-pack ranking. The site now uses 33144 throughout.
>
> `[[VERIFY: 33146 still appears on his live site and the client-side lead quoted it again
> on 2026-08-22. Confirm against the Google Business Profile and correct every remaining
> listing — a split NAP across directories costs local ranking (§5.7).]]`

## Credentials — ALL require primary-source verification

| Claim | Source | Status |
|---|---|---|
| Board-certified plastic surgeon — **ABPS named** | CLIENT-SITE + New Life + **PRIMARY (PG 2019)** + client-supplied portrait | Asserted by three sources incl. a newspaper. **Board now named:** the client-supplied portrait (`assets/about pic.png`, 2026-08-20) shows him in a coat embroidered *"JC Alvarez MD — Board Certified Plastic Surgeon"* beside a card reading *"Certified by The American Board of Plastic Surgery Inc."* That is him asserting ABPS specifically, which the website never did. Still `[[VERIFY: confirm active status in the ABPS/ABMS directory before publishing — an asserted badge is not a verified one.]]` |
| Fellow, American College of Surgeons (FACS) | CLIENT-SITE /about-2/ | `[[VERIFY: facs.org member directory]]` |
| Ph.D. / doctorate in general surgery, cancer focus, earned in **Spain** | CLIENT-SITE + **PRIMARY (Post-Gazette 2019)** | **CORROBORATED.** PG: "earned a doctoral degree in general surgery focused on cancer treatment" in Spain. Institution (Univ. Autónoma de Madrid) still `[[VERIFY]]`. **New Life Cosmetic wrongly calls this a stem-cell PhD** — stem cells were his Pittsburgh work, not the doctorate. |
| Plastic Surgery Residency, University of Pittsburgh | CLIENT-SITE + **PRIMARY (PG 2019)** | **CORROBORATED** — his own quote: "I was able to pass my boards and start my plastic surgery residency." Dates `[[VERIFY]]`. |
| **Harvard — RESOLVED, and not what his site implies** | **PRIMARY (PG 2019)** | From his own account: arrived Boston **2000 on a student visa** to work at a **research laboratory at Harvard University**, spoke little English, **worked four months unpaid** to prove himself; **assistant → lab manager**. That is *Harvard University*, in a research lab — **not Harvard Medical School**, not a clinical fellowship. His site's "journey spans … Harvard Medical School" and New Life's "earned a position at Harvard University" both overstate it. **Describe accurately or omit (§2).** The true version — unpaid for four months to earn the place — is the better story. |
| University of Pittsburgh — research lab, then plastic surgery | **PRIMARY (PG 2019)** | **CORROBORATED.** Moved ~2001 when his lab head relocated; rose to **laboratory manager**; research in **stem cells, limb transplantation, cell culturing**; won funding in trauma surgery, critical care, limb transplantation. |
| Former President, Greater Pittsburgh Society of Plastic Surgery (2018–2020) | CLIENT-SITE /about-2/ | `[[VERIFY]]` — **pulled off /about 2026-08-25.** Visible placeholders were removed from the pages; rather than publish an unverified credential with its marker deleted, the line came out. Restore once corroborated. |
| Years in practice | **CONFLICT — do not publish either number** | His site: "over two decades" / "over 20 years." **New Life Cosmetic: "over 15 years."** Two live sites he is associated with disagree by five years. PG fixes **MD 1996**; plastic surgery residency began only after ~2001. `[[VERIFY: residency completion year + FL license issue date, then state one defensible fact — "practicing plastic surgery since [YEAR]" beats a round decade claim.]]` |
| Medical Director & Founder, Ai Gaia Med Spa and Ai Hair Transplant Miami | CLIENT-SITE /about-2/ | `[[VERIFY]]` |
| FL medical license number + status | — | `[[VERIFY: flhealthsource.gov license lookup — REQUIRED before launch]]` |
| Hospital affiliations | — | `[[VERIFY: §5.4 wants these above the fold; site names none]]` |
| ASPS membership | CLIENT-SITE (logo, /top-board-certified…/) | `[[VERIFY: plasticsurgery.org member lookup]]` |
| RealSelf "Top Doctor" badge | CLIENT-SITE (logo, same page) | `[[VERIFY: RealSelf profile — badge is year-scoped and expires; confirm current status before displaying]]` |
| Procedure volume | — | `[[VERIFY: none stated anywhere on current site. 68 documented before/after cases exist in his media library — a floor, not a total.]]` **Asked on 2026-08-24 to run "over 10,000+ clients helped" in the hero. Refused — see D-042.** The hero proof row runs the verified 148,000 follower count instead, phrased as *people follow his work*. Swap in a real number the moment he supplies one, with a source. |
| Accredited surgical facility (AAAASF/QUAD A/JCAHO) | — | `[[VERIFY: his own content argues accreditation matters; he never states his own]]` |

## Copy written in his voice — needs his sign-off

| item | where | status |
|---|---|---|
| About-section note — *"I'm integrating all that knowledge that is going to benefit you — to improve the quality of your healing after cosmetic surgery."* | `src/public/index.html`, `.note` | **RESOLVED 2026-08-24 — his own words.** Replaced the copy we had drafted. Source: client-supplied transcript of his introduction video, recorded below. Attributed on the page as *From his introduction video*. |
| About biography quote — *"They told me I could become a surgeon… I have become all three."* | `src/public/index.html`, `.pull` | **PRIMARY.** Pittsburgh Post-Gazette, 2019-11-04. Attributed on the page. |
| Hero headline + byline | `src/public/hero-headlines.html` | Third-person byline is factual and sourced. The headline is our copy, not attributed speech — no sign-off needed, but he should approve the positioning. |

**Signature — RESOLVED 2026-08-24.** Client supplied `assets/signature.png` (a scripted
"Dr. JC Alvarez" logotype). Retinted to `--ink` and shipped; the placeholder is gone.
Note it is a brand script, not a handwritten scan — if he wants a true autograph on the
page, that is still an ask.

## Team

| Name | Role | Source | Status |
|---|---|---|---|
| Liliana Clavijo | CFO and Aesthetician | CLIENT-SITE /about-2/ | `[[VERIFY: aesthetician licensure if the title ships]]` |
| Valentina Sanchez | Patient Concierge Specialist | CLIENT-SITE /about-2/ | as claimed |

> **Do not state a team size.** These are the two staff his own site names; that is not
> evidence the practice has only two. Any copy that counts heads — "the two people behind
> every result", "the same three faces" — is an inference, not a fact. `[[VERIFY: full
> staff list, roles and whether any surgical or nursing staff are unlisted.]]`

## Testimonials — RESOLVED 2026-08-26

**Real reviews are now live**, sourced from his RealSelf profile at the client-side lead's
direction and pasted by them (RealSelf returns 403 to automated requests, so nothing was
scraped). Twelve are curated in `content/reviews.json` and injected by
`tools/inject-reviews.py` into the homepage, `/results` and `/preparation`. Verbatim, cuts
marked with an ellipsis, each attributed to the handle RealSelf shows plus the month, with
a link back to the profile.

**This replaces twelve testimonials we wrote ourselves.** They were labelled "placeholder
copy" in a small line under the heading, but they were written in a convincing patient
register and read as real. Fabricated testimonials on a physician's site are the exact
thing FTC 16 CFR 255 exists to prevent, and ours were more believable than the vendor copy
this file had already rejected. They are gone.

Three things deliberately left out of the quotes, recorded so nobody re-adds them:

- **Prices.** One review names a figure; it is from the Pennsylvania practice and is not
  current Miami pricing.
- **"Triple board certified … went to Harvard."** A patient repeating a credential this
  file has as *asserted, not verified* — and the Harvard year was a research laboratory,
  not a clinical post. Republishing a patient's version of it makes it our claim.
- **Implant volumes and cup sizes.** Specific to that patient; on a marketing page they
  read as a promise to the next one.

`[[VERIFY: two things for him.` **(1)** Most of these reviews are from **2018–2022 and from
his Pennsylvania practice (ReNova / Wexford)**, not Miami — his work and his patients, so
legitimate to publish, but the newest is June 2022 and a Miami practice showing nothing
more recent is a visible gap. **(2)** Ask whether RealSelf's terms permit republishing the
text, or whether the aggregate-plus-badge route is safer. Raised and overruled; recorded
here so the decision has a date on it.`]]`

## Superseded — the original finding on his site's testimonials

Current site carries attributed testimonials: "Maria L", "Julia C", "Mark R",
"Samantha L" — e.g. *"My waist is snatched, and my curves are perfect. Worth every
penny!"*, *"Dr. Alvarez's expertise is unmatched!"*

> **[[VERIFY: are these real patients with signed release?]]** They read as template
> copy. Under FTC 16 CFR Part 255 a testimonial must reflect a genuine experience;
> fabricated ones are an enforcement matter, and republishing them under our redesign
> transfers that exposure to work with our name on it. **Blocked from the rebuild
> until he produces signed releases.** If he cannot, we ship no testimonials and use
> verified third-party review counts instead.

## Procedures offered (safe to carry over — service list, not a claim)

Brazilian Butt Lift · Skinny BBL · Breast Augmentation · Breast Lift + Augmentation ·
Eyelid Surgery (Blepharoplasty) · Scarless Eyelid Rejuvenation · Deep Facelift ·
Face Rejuvenation · High-Definition Liposuction · Rhinoplasty · Tummy Tuck
(Abdominoplasty)
Adjacent/spa: Hyperbaric Oxygen Therapy · Hair Smart Regrowth · Skin Rejuvenation ·
CO2 Laser Resurfacing

## Claims that CANNOT carry over (CLAUDE.md §3 "Claims")

Current site uses restricted superlatives heavily — **33 instances of "best"**, plus
"TOP" in nearly every page title and URL slug, "unmatched", "flawless", "perfect",
"renowned", "world-class". Also "Free Consultation" framed as a **"Special Offer"**.
All barred by §3 and by ABPS/state medical advertising norms. Rewrite from scratch.

---

## Verified biography (PRIMARY: Pittsburgh Post-Gazette, 2019-11-04)

Full text: `content/_extracted/external/post-gazette-2019.md`. Named reporter, direct
quotes, contemporaneous — the most reliable source we have. **This is publishable
material**, and it is dramatically better than anything on his current site.

| year | fact |
|---|---|
| — | Medical school, Bogotá, Colombia. At 19, ran a campus business baking brownies; later sold slide-making services for medical lectures. |
| **1996** | Graduated medical school. |
| **1997–98** | Colombian Navy base on the Pacific coast during the guerrilla conflict — treated soldiers wounded in combat, and **delivered 180 babies in that year**. |
| **1998** | Moved to Spain. Struggled with the board exams there ("very technical"; his training had been hands-on). |
| — | Earned his **doctorate in general surgery, cancer focus**, in Spain. |
| **2000** | Moved to Boston on a student visa for a **Harvard University research laboratory**. Spoke little English. **Worked four months unpaid.** |
| **~2001** | Followed his lab head to the **University of Pittsburgh** — "None of the other lab members wanted to move to Pittsburgh." Rose from assistant to **laboratory manager**. |
| — | Research in **stem cells, limb transplantation, cell culturing**; funded work in trauma surgery and critical care. |
| — | Passed boards, began **plastic surgery residency**. |
| **2015** | Opened **ReNova Plastic Surgery and Medical Spa** in Pine, PA — financed by a Pittsburgh lender he persuaded. |
| **~2018** | Moved ReNova to a **3,300 sq ft** space in Fairmont Plaza, Marshall, PA. Three employees. |
| **2019** | Living in Pine, PA. Two children, ages 12 and 10. |
| — | `[[VERIFY: when and why he relocated to Miami — the gap between 2019 Pittsburgh and today is undocumented.]]` |

**Also from his site, not yet verified:** Former President, Greater Pittsburgh Society
of Plastic Surgery (2018–2020) — consistent with the PG timeline. `[[VERIFY]]`

### Publishable quotes (attribute to Post-Gazette, 2019)

> "They told me, 'Hey, you have this skill to do many things. Why don't you go to
> America to fulfill this dream?' They told me I could become a surgeon. I could become
> a researcher, and maybe a businessman. … I have become all three."

> "The discrimination I have faced in my time has taught me that, even if you are
> different, you have to embrace your difference."

> "Invest in how to be better. Hard work is the No. 1 resource. But smart hard work is
> what gives you more tools toward success."

---

## He is a published author — and his site barely says so

| item | source | status |
|---|---|---|
| **"Behind the Mirror: The ultimate guide to safe and satisfying plastic surgery"** | Linktree → Amazon **ASIN B0DMWMFVZ4** | Listing confirmed. `[[VERIFY: publisher, publication date, format, review count. ASIN prefix B0DM suggests a late-2024 KDP release.]]` |
| **"Detrás del Espejo: La Guía Definitiva para una Cirugía Plástica Segura y Satisfactoria"** | Linktree → Amazon **ASIN B0DMTH25Q5** | Spanish edition. Same `[[VERIFY]]`. |
| Cover art in his media library (`behind-the-mirror.png`, `Detras-del-espejo.png`) | CLIENT-SITE | confirmed |

A published patient-education book in two languages is a first-rank trust signal
(§5.4) and it is **absent from his homepage, his About page, and every procedure page.**

## Julux Institute

| claim | source | status |
|---|---|---|
| "Founder of Julux Institute" | Linktree bio | `[[VERIFY: what it is, whether it is live, and whether it belongs in this site's story at all — it appears NOWHERE on jcalvarezplasticsurgery.com]]` |

## Digital ecosystem (Linktree, retrieved 2026-08-20)

Bio reads: *"Board-certified plastic surgeon / Regenerative medicine & longevity /
Founder of Julux Institute / Miami, FL"*

| channel | URL |
|---|---|
| Instagram | instagram.com/drjcalvarez_plasticsurgery — **148K followers · 1,143 posts · verified badge** |
| YouTube | youtube.com/@drjcalvarez |
| TikTok | tiktok.com/@drjcalvarez_plasticsurgeon `[[VERIFY: Linktree's own social block lists @jcalvarez_plasticsurgeon — two different handles; confirm which is live]]` |
| Amazon storefront | amazon.com/shop/drjcalvarez_plasticsurgery |
| **Booking** | **info.newlifecosmetic.com/organic-dr-jc-alvarez** |
| His own site | jcalvarezplasticsurgery.com — labelled *"LEARN about your procedure"* |

> **The single most important structural finding in this project.** His own Linktree
> routes **booking to New Life Cosmetic's funnel**, and casts his own website as a
> *learning* resource. Today the funnel is **Instagram → Linktree → New Life's form.**
> His site is a brochure that does not convert. Making it the conversion endpoint is
> the entire job (CLAUDE.md §5.5, and the definition of done's "submissions land
> somewhere real").

## Employment / affiliation — needs a decision, not just verification

| fact | source | status |
|---|---|---|
| Listed surgeon at **New Life Plastic Surgery** (newlifecosmetic.com), one of 6 | newlifecosmetic.com/surgeon/dr-julio-clavijo-alvarez/ (page live, modified 2025-07-10) | confirmed |
| New Life markets on price — "HOLIDAYS SPECIAL", "aesthetic surgery in Miami at incredible prices", financing, BMI-max-36 gating | same | confirmed |
| His 8400 SW 8th St address vs New Life's locations | — | `[[VERIFY: is his listed address his own practice, or a New Life facility?]]` |
| Prior practice: **ReNova Plastic Surgery & Medical Spa**, Marshall PA | PRIMARY (PG 2019) | `[[VERIFY: still operating? still his?]]` |
| Also claims Medical Director & Founder, **Ai Gaia Med Spa** and **Ai Hair Transplant Miami** | CLIENT-SITE /about-2/ | `[[VERIFY]]` |

**Escalation (§2 — client's call, not ours):** he is attached to at least four brands —
his own name, New Life, Ai Gaia / Ai Hair Transplant, and Julux Institute — plus a
former Pittsburgh practice. The §4 editorial-luxury positioning is in direct tension
with New Life's discount-volume marketing. **Which brand is this site for, and does it
compete with New Life or feed it?** Everything downstream — positioning, CTA
destination, pricing language — depends on the answer.

---

## His own words (video transcript, supplied 2026-08-20)

Source: client-supplied transcript of a short introduction video. **Usable as his voice**,
unlike the site's vendor-written copy.

> "JC Alvarez Plastic Surgery is a website that is focused on teaching you about plastic
> surgery. My vision and purpose is to integrate all the knowledge that I have acquired
> throughout the time to put it in the service of my patients. I have a good background in
> cellular biology. I had a PhD. I did hyperbaric oxygen therapies. I studied plastic
> surgery. And at the end I'm integrating all that knowledge that is going to benefit you
> to improve the quality of your healing after cosmetic surgery."

**What this establishes:**

| claim | status |
|---|---|
| Background in cellular biology | consistent with the PG-verified Pittsburgh lab work (stem cells, cell culturing) |
| PhD | corroborated — PG confirms a doctorate earned in Spain |
| Hyperbaric oxygen therapy practice | his own statement; equipment photographed in his media library |
| **Positioning: "the quality of your healing"** | **his own framing, and the strongest differentiator we have** |

> **This is the spine of the brand.** He is not selling a procedure, he is selling *recovery
> as part of the operation.* It ties the PhD, the hyperbaric chamber, and the 90-day
> preparation content into one argument no Miami competitor is making. Used verbatim as the
> pull quote in the About section.

---

## Instagram — the largest verified asset he has (captured 2026-08-22)

Source: profile screenshots supplied by client-side lead.

| metric | value | note |
|---|---|---|
| Followers | **148,000** | **the single biggest third-party trust signal in the project** |
| Posts | 1,143 | proves the "educator" positioning is real, not claimed |
| Verified | yes, blue check | platform-verified identity |
| Reel views (sampled) | 6,694 · 7,018 · 9,316 · 10,400 · 13,600 · 17,600 | healthy per-reel reach |
| Highlights | Before/After · Eyelid Surgery · Demo Videos · Transformations · Lips | already organised by procedure |
| Bio CTA | `info.newlifecosmetic.com/organic-dr-jc-alvarez` | **confirms the funnel finding — his own bio books into New Life** |

### His reels are objection-answering content, and that is the high-value asset

Sampled titles, all him to camera, mostly Spanish:

- *¿Por qué se endurecen los implantes?* — why implants harden (capsular contracture)
- *¿Qué es la trombosis venosa profunda?* — what DVT is
- *Ponytail facelift: la verdad*
- *¿Cara y cuello: juntos o separados?* — face and neck, together or separately
- *¿Qué se hacen los hombres?* — what men have done
- *Por qué escribí el libro y qué hay dentro* — why he wrote the book

`docs/DECISIONS.md` D-015 asked him to film objection answers as the highest-value video
ask. **He has been making them for years.** They map directly onto the four fears in
`docs/conversion-doctrine.md` — safety (DVT), naturalness (ponytail facelift "truth"),
candidacy (what men have done). Sourcing and subtitling these beats commissioning new film.

### One caveat before the follower count ships as a headline

`[[VERIFY: engagement]]` A third-party analytics overlay in the same screenshot reports
**avg 409 likes and 21 comments per post across 47 posts** — roughly 0.3% of followers.
Reel *views* (7K–17.6K) look healthier than post likes. Mixed signals like this are worth
understanding before we print "148K" as a trust headline, because a competitor or a
sceptical patient can run the same arithmetic. Recommend leading with **reel reach** or
**verified + post count**, which are unambiguous, and using the follower number as support.
