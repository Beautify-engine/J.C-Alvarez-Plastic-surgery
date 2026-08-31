# Teardown — jcalvarezplasticsurgery.com (as of 2026-08-20)

Method: robots-respecting crawl of the public site + WordPress REST API. No auth
bypass. Raw output in `content/_extracted/` (gitignored, never deployed, CLAUDE.md §3).

**Platform:** WordPress, self-hosted on Apache, built with **Elementor + ElementsKit**
page builder. No SEO plugin installed (no Yoast, no Rank Math). Not a locked vendor
platform — he owns the install, so he can be migrated.

**Scale:** **154 indexable URLs** — 91 pages + 53 posts + 10 category archives + 1 author
archive, minus one slug collision (below). Trilingual: 87 EN, 32 ES, 25 RU.
414 media library items (136 Envato stock, 68 patient before/afters, real portrait/team/facility
photography, credential logos, and ~200 UI graphics). Posts stopped 2025-05-15.
Pages edited as recently as 2026-08-11.

---

## The headline finding: he has the results, and the site hides them

**Corrected 2026-08-20** — an earlier pass of this teardown sampled only the first
100 of 414 media items and wrongly concluded the library was entirely stock. The full
library tells a much better story.

**68 patient before/after composites exist** (`Slide*.jpg` / `Slide*.png`, 1200×1200).
Verified by inspection: black background, baked-in "Dr. JC Alvarez – Plastic Surgery"
watermark, before/after labels, multiple angles per case — PowerPoint or Keynote
exports of his case library.

**Real photography of him and his team exists too:** studio portraits
(`jc-alvarez-md-plasticsurgeon.png` 800×1120, `JC-alvarez-black-jacket.png` 994×1166,
`JC-alvarez-light-brown-jacket.png`), a team group shot (`about-us-banner-desktop.jpg`
1500×1734), and individual staff headshots (Lili Clavijo, Valentina Sanchez,
Maria Velasquez 1365×1365). Plus real facility/equipment photography — hyperbaric
chamber, Venus Viva, Ellacor.

**And the credential logos exist:** ABPS, American College of Surgeons, ASPS, and a
RealSelf Top Doctor badge.

So the asset problem is not scarcity. It is deployment:

| Asset | Reality |
|---|---|
| 68 before/after cases | **54 are used**, scattered 6–9 per procedure page across EN/ES/RU. **14 are never displayed at all.** |
| `/gallery/` — the one nav item a patient clicks to see results | **Contains zero of them.** 17 generic stock spa images: `cosmetologist-inspecting-skin`, `flowers-and-eucaaliptus-composition`, `massaging-back-with-body-massager`. |
| Credential logos (ABPS, ACS, ASPS, RealSelf) | Appear on **exactly one page** of 154. Absent from the homepage and every procedure page. |
| Doctor + team photography | Confined to `/about-2/` and `/contact/`. Absent from the homepage hero and every procedure page. |

Meanwhile the BBL page tells visitors to *"See real before-and-after results"* — and
links toward a gallery that has none.

Per CLAUDE.md §5.2 the gallery is the #1 conversion driver, and §5.4 puts trust signals
above the fold on every page. He already owns everything both rules require. **The
pitch is not "you need new assets" — it is "you are sitting on the assets and the site
buries them."** That is a far stronger room than a shoot proposal, and it is cheap to
prove: a filterable 68-case gallery, built from media he already has.

### What this means for §3 (patient media)

The 68 before/afters **are** patient images, so the §3 rule now binds hard and is no
longer hypothetical:

- Build the gallery against **placeholders** in 1200×1200, ~7 per procedure across 6+
  procedures, so layout, filtering, and lazy-loading are all real.
- Real cases appear only in the **access-controlled preview** and the pitch deck.
- The watermark, black background, and slide-export framing all have to go for the
  rebuild — they are a PowerPoint aesthetic, not an editorial one (§4). Re-mastering
  needs his originals, which is a signed-client conversation, not a spec one.

### Quality caveat

These are slide exports, not photographs. Lighting, background, crop, and camera
distance are inconsistent case to case, and the source resolution is capped at
1200×1200 with a watermark burned in. §4 requires one grade, one crop logic, one
aspect set. Deliverable for the pitch: a gallery that *looks* systematic using what
exists. Deliverable post-signature: re-master from originals, or standardise his
photography protocol going forward.

## SEO: broken at the foundation

**Measured across all 154 URLs** (complete crawl, not a sample):

| check | result |
|---|---|
| Meta descriptions | **0 of 154 — 100% missing.** Google is inventing every snippet on the site. |
| JSON-LD structured data | **0 of 154.** No `Physician`, `MedicalBusiness`, or `LocalBusiness` anywhere. §5.7 violated outright. |
| `hreflang` | **0 of 154**, on a trilingual site. The EN/ES/RU trees are unlinked and compete with one another. |
| `<h1>` | **85 of 154 (55%) have none.** 2 more have several. |
| Modern image formats | **0 of 154 reference WebP or AVIF.** Entire library is JPG/PNG. |
| Image `alt` | **2,804 of 3,287 images (85%) are `alt=""`.** SEO and WCAG failure together. |
| Explicit `width`+`height` | only 2,677 of 3,287 — **610 images can shift layout** (§6 forbids it). |
| Canonical tag | missing on 11 URLs. |
| Duplicate `<title>` | none — the one thing that is clean. |

Title and slug strategy is keyword stuffing:
`top-breast-augmentation-in-miami-fl-dr-jc-alvarez`, `TOP Deep FaceLift Surgery in
Miami FL – Dr. JC Alvarez – J.C. Alvarez Plastic Surgeon`. Almost every title
front-loads "TOP" — a restricted superlative (§3) burning the pixels that should carry
the value proposition. The homepage title is just `J.C. Alvarez Plastic Surgeon`: no
city, no procedure, no differentiator.

**Slug collision on the most important trust page.**
`/top-board-certified-plastic-surgeon-in-miami-fl-dr-jc-alvarez/` is published in **both**
the page sitemap and the post sitemap — two WordPress objects competing for one URL.
WordPress resolves to one; the other is orphaned but still submitted to Google. Of every
URL on the site to break this way, it is the board-certification page — the one §5.4
treats as the primary trust signal.

Other structural defects: NAP publishes **two conflicting ZIPs** (33144 / 33146) for one
address; the contact address is `@gmail.com`, not a branded domain; a published
`/404-2/` page sits in the sitemap as a real indexable URL; and the RU tree uses
percent-encoded Cyrillic slugs that are unreadable and unshareable.

## Performance: the Elementor tax

Across all 154 pages: **average 144 KB of raw HTML, 31 stylesheets, and 31 script tags
per page** — peaking at 289 KB, 45 stylesheets, and 41 scripts on the procedure pages.
Media is **JPG/PNG only, no WebP or AVIF anywhere**, including a 5.9 MB PNG and a 9.9 MB
PNG in the library.

Thirty-one render-blocking stylesheets on a mobile connection is not a tuning problem,
it's an architecture problem. CLAUDE.md §6 requires ≥90 mobile Performance and LCP
< 2.0s; that is unreachable on this stack, which settles the Phase 3 question — a
migration off Elementor is mandatory, not preferential.

## Conversion and positioning

- **CTA language is inconsistent** — "Get Free Consultation With Our Experts",
  "Make an Appointment", "Consult With Doctor", "Contact us", "Book your consultation"
  all appear, often on the same page. §5.5 requires exactly one, everywhere.
- **"Special Offer / Free Consultation"** frames the practice on discount. Free
  consults are standard in this market; presenting one as a limited offer reads cheap
  and undercuts the premium positioning in §4.
- **Navigation is a mega-menu with 5 sub-levels and ~35 items.** A nervous first-time
  patient cannot parse it. Language switching is buried at the end of the nav.
- **Trust signals are absent above the fold** — no board name, no years, no volume,
  no facility accreditation, no hospital affiliation (§5.4).
- **Testimonials appear fabricated** — see `content/facts.md`. Blocked from reuse.
- **A blog that stopped 15 months ago** (last post 2025-05-15) signals a dormant
  practice; 53 posts of thin "101 course" content compete with his own procedure pages.

## The funnel: his site is not the conversion endpoint

From his own Linktree (`linktr.ee/dr_jcalvarez_plasticsurgery`, the link in his
Instagram bio):

- **"BOOK your CONSULTATION with Dr. JC Alvarez"** → `info.newlifecosmetic.com/organic-dr-jc-alvarez`
- **"LEARN about your procedure"** → `jcalvarezplasticsurgery.com`

He routes booking to **New Life Cosmetic's** funnel and casts his own site as a
*learning* resource. The live path is **Instagram → Linktree → New Life's form.** His
website is a brochure that does not convert — which is why an empty gallery, missing
trust signals, and four competing CTA phrasings have gone unnoticed. Nothing on that
site was ever measured against a booking.

That is this project in one sentence: **make his site the conversion endpoint.**

## The brand tangle (needs his decision — §2)

He is attached to at least four active brands plus a former practice:

| brand | role | positioning |
|---|---|---|
| **jcalvarezplasticsurgery.com** | his own name | education / brochure |
| **New Life Plastic Surgery** | one of 6 listed surgeons | **discount volume** — "HOLIDAYS SPECIAL", "aesthetic surgery in Miami at incredible prices", financing, BMI-max-36 gating |
| **Ai Gaia Med Spa** / **Ai Hair Transplant Miami** | claims Medical Director & Founder | med-spa |
| **Julux Institute** | "Founder" (Linktree bio) | appears **nowhere** on his website |
| ReNova Plastic Surgery, Marshall PA | owner from 2015 | prior Pittsburgh practice |

New Life's price-led marketing is in direct tension with the §4 editorial-luxury thesis.
**Which brand is this site for, and does it compete with New Life or feed it?** We
cannot resolve that; he must.

Note a live contradiction while we wait: **New Life says "over 15 years of experience";
his own site says "over two decades."** Two sites carrying his name disagree by five
years. Logged in `content/facts.md` — neither number ships until verified.

## The story his site refuses to tell

The Pittsburgh Post-Gazette profiled him in 2019 (full text in
`content/_extracted/external/post-gazette-2019.md`). The verified biography:

Bogotá medical school, where at 19 he sold brownies to classmates, then bought a camera
and a computer and sold slide-making to residents — *"while doing the slides, I was
learning the topics and making money at the same time."* Graduated 1996. Spent 1997–98
at a Colombian Navy base on the Pacific coast during the guerrilla conflict, treating
soldiers wounded in combat — **and delivering 180 babies that year.** Moved to Spain in
1998 and earned a doctorate in general surgery. Came to Boston in 2000 on a student visa
with little English and **worked four months unpaid** in a Harvard research lab to prove
he was worth hiring. Followed his boss to Pittsburgh when none of the other lab members
would go. Assistant → lab manager → stem cell and limb-transplantation research →
plastic surgery residency → his own practice, financed by a lender he talked into it.

His current About page renders all of that as *"A Legacy of Excellence"* over a bulleted
list of institution names.

**§5.3 says the surgeon is the product.** He has an extraordinary story, a published
book in two languages, and 68 documented cases — and the site leads with a stock photo
of a woman receiving a facial. Correcting that is most of the redesign.

**One correction we must make while doing it:** the site's "his journey spans … Harvard
Medical School" overstates what the Post-Gazette documents — a research laboratory at
Harvard *University*, not Harvard Medical School, and not a clinical fellowship. Per §2
we describe it accurately. The true version is better anyway.

## What is genuinely good and should survive

1. **The pre-op content is a real differentiator.** 90-day preparation, nutrition,
   supplements, pain management, gluteal muscle training, and the frank
   marijuana/tobacco/cocaine risk articles. No competitor in Miami is publishing
   surgical-preparation content at this depth. It is *substance*, not marketing, and
   it maps directly onto the §4 "restraint and evidence" thesis. Currently buried
   under a "Prepare" nav item.
2. **Trilingual reach** is a real asset in Miami — it is merely implemented wrong.
3. **The regenerative-medicine angle** (hyperbaric oxygen, stem cell research, PhD)
   is a defensible, non-superlative differentiator that his competitors cannot claim.
4. **He owns his WordPress install** — no vendor lock-in blocking a migration.
5. **He is a published author.** *Behind the Mirror* / *Detrás del Espejo*, on Amazon in
   English and Spanish. A first-rank trust signal (§5.4), and it appears on neither his
   homepage, his About page, nor any procedure page. The cover art is sitting unused in
   his media library.
6. **A real audience.** Instagram, YouTube, TikTok, and an Amazon storefront — traffic
   that currently flows past his site to someone else's booking form.

## The pitch narrative in one line

He is a Ph.D.-credentialed surgeon who delivered 180 babies in a war zone, worked four
months unpaid to get into a Harvard lab, wrote the book on safe plastic surgery in two
languages, and holds 68 documented cases — presented through a stock-photo med-spa
template with an empty gallery, no structured data, no `<h1>`s, a page weight no phone
can love, and a booking button that sends his patients to a competitor's funnel.
**We are not redesigning a website; we are making the surgeon visible — and pointing
the funnel back at him.**
