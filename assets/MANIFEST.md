# assets/MANIFEST.md

Every asset used in this project gets a row. Required by CLAUDE.md §3.

`rights`: `unknown` | `public-domain` | `licensed` | `client-owned`
`patient`: `yes` | `no` — anything `yes` may appear ONLY in the access-controlled
preview or the pitch deck. **Never on a publicly reachable URL.**

Inventory taken 2026-08-20 from his WordPress media library (414 items) via the public
REST API. Nothing has been bulk-downloaded; the table records what exists and its
classification. Sample files pulled for verification live in `assets/_raw/` (gitignored).

---

## Category inventory

| category | count | rights | patient | notes |
|---|---|---|---|---|
| **Patient before/after composites** (`Slide*.jpg` / `Slide*.png`, 1200×1200) | **68** | client-owned | **yes** | Slide exports. Black bg, burned-in "Dr. JC Alvarez – Plastic Surgery" watermark, before/after labels, multi-angle. **54 deployed** across EN/ES/RU procedure pages; **14 never displayed** (Slide48/50–55/78/79/85/102.jpg, Slide19/136/143.png). |
| Envato Elements stock (`*-YYYY-MM-DD-HH-MM-SS-utc*`) | 136 | licensed (to him) | no | His licence, not ours. Do not carry into the rebuild — §4 bars this vocabulary anyway. |
| Dr. Alvarez studio portraits | 4 | client-owned | no | `jc-alvarez-md-plasticsurgeon.png` 800×1120 · `JC-alvarez-black-jacket.png` 994×1166 · `JC-alvarez-light-brown-jacket.png` 555×544 · `Dr-JCAlvarez-contact.jpg` 500×500 |
| Team / staff photography | 4 | client-owned | no | `about-us-banner-desktop.jpg` 1500×1734 (group) · `Lili-Clavijo.png` · `Valentina-Sanchez.png` · `maria-velasquez-foto.jpg` 1365×1365 |
| Facility & equipment | ~6 | client-owned | no | `hiperbaric-chamber-equipment.jpg` 1300×1300 · `venus-viva.png` · `Ellacor.jpg` · `exosomes.jpg` · `zo-antiaging.jpg` |
| Credential / affiliation logos | 8 | third-party marks | no | ABPS (`abps_logotm_stacked-logo`, `logo-american-board-plastic-surgeons`) · American College of Surgeons · ASPS · **RealSelf Top Doctor** |
| Brand marks | 3 | client-owned | no | `logo-Dr-JC-Alvarez.png` 800×185 · `logo.png` |
| Programme artwork | 2 | client-owned | no | `behind-the-mirror.png` · `Detras-del-espejo.png` — his show/podcast |
| Procedure banner photography | 5 | unknown | **likely yes** | `2021-01-05-Blepharoplasty.jpg` · `2021-05-24-HD-Liposuction-Miami-Butt-Lift.png` · `Abdominoplasty-scaled.jpg` · `Breast-aug-lift-.jpg` · `Rhinoplasty.jpg` — all 2000×1125. `[[VERIFY: confirm whether these are patients]]` |
| UI graphics / icons / section headers | ~180 | mixed | no | `2000×1400` PNG headers, procedure icon sets, floral elements. All replaced in rebuild. |

## Before/after cases by procedure (deployed)

| procedure | cases live | file range |
|---|---|---|
| Brazilian Butt Lift | 9 | Slide144–152.png |
| Breast Augmentation | 8 | Slide41–49.jpg |
| Rhinoplasty | 7 | Slide32–39.jpg |
| Deep Facelift | 7 | Slide20–26.png |
| Tummy Tuck | 7 | Slide73–88.jpg |
| HD Liposuction | 6 | Slide137–142.png |
| Eyelid Surgery / Scarless Eyelid | 7 | (verified site-wide crawl) |
| **total deployed** | **54 of 68** | 14 cases never shown on any page |

## Rules that follow from this

1. **The 68 before/afters never reach a public URL.** Gallery ships against 1200×1200
   placeholders at true case counts (7 BBL, 8 breast aug, …) so layout, filtering, and
   lazy-loading are exercised for real. Swap to real cases only in the gated preview.
2. **Do not re-host the watermarked slide exports in the final design.** Watermark,
   black background and slide framing are a PowerPoint aesthetic, not editorial (§4).
   Re-mastering requires his originals — a signed-client conversation.
3. **Credential logos are third-party marks.** ABPS/ACS/ASPS/RealSelf usage is governed
   by each body's brand rules and is contingent on `content/facts.md` verification
   clearing. Do not display a badge we have not verified he holds.
4. **His Envato licence does not transfer to us.** Any stock we use is licensed fresh,
   and per §3 never as a face presented as patient, staff, or result.

## Procedure carousel imagery (added 2026-08-20)

8 files, 1080×1350 (4:5), supplied by client-side lead. Originals in
`assets/procedures/Body procedures/`, graded copies in `graded-clean-deep/`, web derivatives in
`src/public/img/procedures/` at 600/900/1200w.

| file | assigned procedure | patient | rights |
|---|---|---|---|
| 13.jpg | Brazilian Butt Lift | no (faceless) | `[[VERIFY]]` |
| 7.jpg | Skinny BBL | no (faceless) | `[[VERIFY]]` |
| 9.jpg | Breast Augmentation | no (faceless) | `[[VERIFY]]` |
| 8.jpg | Breast Lift & Augmentation | no (faceless) | `[[VERIFY]]` |
| 10.jpg | Breast Lift | no (faceless) | `[[VERIFY]]` |
| 12.jpg | Tummy Tuck | no (faceless) | `[[VERIFY]]` |
| 14.jpg | High-Definition Liposuction | no (face not shown) | `[[VERIFY]]` |
| 11.jpg | Eyelid Surgery | no (eye only, not identifiable) | `[[VERIFY]]` |

All eight comply with the no-faces rule in `design/procedure-photography.md`. None reads
as a result. **`[[VERIFY: rights — generated, licensed, or client-owned? Needed before
any public deployment.]]`**

## Instagram-sourced cases (flagged 2026-08-20)

Client-side lead obtained before/after cases from his Instagram by scraping. Recorded here
because provenance has to survive the project.

| field | value |
|---|---|
| source | instagram.com/drjcalvarez_plasticsurgery |
| method | automated scrape — **contrary to CLAUDE.md §3**, logged for the record |
| rights | `unknown` |
| patient | **yes** |
| deployable publicly | **no** — gated preview and pitch deck only |

Consent for these attaches to Instagram, not to a new domain. Same constraint as the 68
website slides. Public build uses placeholders at matching aspect ratios and counts.
Post-signature: replace with originals plus signed releases.

`[[VERIFY: procedure breakdown, case count, whether faces are identifiable, watermark state]]`

## Still outstanding

- `[[VERIFY]]` Whether the 5 procedure banner photos are patient images.
- **Original, unwatermarked before/after files** — request from him. Would lift the
  gallery from "usable" to genuinely premium.
- **Photography of the operating facility / consultation rooms** — none found.
- **Signed patient releases** covering web use of the 68 cases — must exist before any
  public deployment post-signature.

## YouTube — indexed, not downloaded (2026-08-22)

| category | count | rights | patient | notes |
|---|---|---|---|---|
| `@drjcalvarez` uploads | **202** (67 long-form + 135 Shorts) | client-owned, **stays on his channel** | no | Indexed in `content/youtube-catalog.md`. **No file was downloaded.** Procedure pages embed via `youtube-nocookie.com`, click-to-load (D-029). Two thumbnails were pulled during evaluation and **deleted** — off-brand per §4. |

## Imported into the build 2026-08-23 (procedure template)

| file in `src/public` | source | rights | patient | notes |
|---|---|---|---|---|
| `img/about/jc-office-{600,900,1200}.jpg` | `assets/Headshots/professionals/123424497_…n.jpg` | client-owned | no | Him in the office, suit. Graded `clean`. Used in the surgeon section. |
| `img/about/jc-interview-{600,900}.jpg` | `assets/Headshots/professionals/707886696_…n.jpg` | client-owned | no | Press interview. Graded `clean`. Inset frame in the surgeon section. |
| `img/band/consult-{1200,1800}.jpg` | frame at **11.2s** of `assets/hero video.mp4` | client-owned | **no — verified** | The one window in that reel with no identifiable patient (back of head only), per the video notes in `ASSET-REQUEST.md`. Graded `clean-deep`. Full-bleed band. |

Two YouTube thumbnails were pulled during evaluation and **deleted** — off-brand per §4 (D-029).

## Credential marks, supplied 2026-08-24

| file in `src/public` | source | rights | patient | notes |
|---|---|---|---|---|
| `img/badges/abps{,@2x}.png` | `assets/Badges/17.png` (1080×1350) | client-supplied | no | ABPS certification mark. Content-box cropped, not recoloured (D-040). **Display blocked** until active status is confirmed in the ABPS/ABMS directory — `facts.md` has this as asserted, not verified. |
| `img/badges/asps{,@2x}.png` | `assets/Badges/16.png` (1080×1350) | client-supplied | no | ASPS member mark. Same treatment. **Display blocked** pending plasticsurgery.org member lookup. |
| `img/badges/acs{,@2x}.png` | `assets/Badges/Untitled design (1).png` (1080×1350) | client-supplied | no | American College of Surgeons medallion — a photograph, not a flat logo. **Display blocked** pending facs.org directory check. |
| `img/badges/{abps,asps,acs}-w{,@2x}.png` | derived from the three marks above | client-supplied, **derived** | no | White reverse versions for the dark hero strip (D-041). Alpha taken from pixel darkness so internal shapes survive. **Request the official reverse artwork from each board before launch** — a derived mark is a pitch stand-in, not shippable. Same display block as the colour originals. |

## Hero video renders, rebuilt 2026-08-24

| file in `src/public` | source | rights | patient | notes |
|---|---|---|---|---|
| `video/hero-{1920.mp4,1600.webm,1280.mp4}` | `assets/hero video.mp4` | client-owned | **yes — releases confirmed by client 2026-08-23** | 12.32s. Tail cut at 17.40 to drop a jump cut in the source; tail dissolved back into the head for a seamless loop (D-038). Built by `tools/hero-cut.sh`. |
| `video/hero-m-608.{mp4,webm}` | `assets/hero video.mp4` | client-owned | **yes — as above** | 608×1080 portrait cut, each of the seven shots cropped on its own column (D-039). Built by `tools/hero-cut-mobile.sh`. |
| `img/hero-poster.jpg`, `img/hero-poster-m.jpg` | frame 0 of each render above | client-owned | no | Marking shot, surgeon's profile — no identifiable patient in frame. |

## Hero proof-row avatars, cut 2026-08-24

| file in `src/public` | source | rights | patient | notes |
|---|---|---|---|---|
| `img/avatars/p{1,2,3}{,@2x}.jpg` | `assets/hero video.mp4` at 7.0s, 9.9s, 17.0s | client-owned | **yes — releases confirmed by client 2026-08-23** | Square face crops, graded `clean`. **Deliberately not taken from the reels** (D-042): a release covering a result video does not extend to using that patient's face as a social-proof token. Gated preview only. |

## Signature, supplied 2026-08-24

| file in `src/public` | source | rights | patient | notes |
|---|---|---|---|---|
| `img/about/signature-ink{,@2x}.png` | `assets/signature.png` (672×196, orange on transparent) | client-supplied | no | Cropped to content, retinted to `--ink` by replacing RGB and keeping the source alpha, so the antialiasing survives. An `accent` (#35606f) variant was generated and rejected — it read decorative rather than signed. Used in the About note (D-045). |

## Imported 2026-08-24 — pictures that were sitting unused

| file in `src/public` | source | rights | patient | notes |
|---|---|---|---|---|
| `img/about/team-{700,1100}.{jpg,webp}` | `assets/Headshots/professionals/imgi_3_about-us-banner-desktop.jpg` (1500×1734) | client-owned | no | **The team photograph** — him with Liliana Clavijo and Valentina Sanchez. Cropped 5:4 from y=150 so nobody loses their shoulders, graded `clean`. Was in the folder unused since 2026-08-20; the /about team block named both women and showed neither. |
| `img/about/interview-{640,960}.{jpg,webp}` | `assets/Headshots/professionals/707886696_…n.jpg` (1080×1350) | client-owned | no | Press interview. Recropped **3:2 landscape** from the original rather than reusing the 4:5 `jc-interview-*` derivative, which stood too tall beside the timeline heading. Graded `clean`. Caption carries `[[VERIFY: outlet, interviewer and date]]`. |
| `img/band/consult-{1200,1800}.jpg` | frame at 11.2s of `assets/hero video.mp4` | client-owned | **no — verified** | Already existed but was **orphaned** — nothing referenced it. Now carries the "why it matters" section on /about. Back of head only; no identifiable patient. |

**Still unused and worth a home:** `jc-office-*` (him in a suit, framed before/afters behind —
good for /contact), `183858725_…jpg` (2048×1365 studio portrait on white), and
`assets/Instagram videos/Profile picture.jpg` (warm interview still).

| `img/about/book-es-{520,780}.{jpg,webp}` | `assets/Book.png` (768×1205, supplied 2026-08-25) | client-owned | no | Cover of *Detrás del Espejo*. Shown flat on `--ink` in the /about book section (D-050). **Only the Spanish cover has been supplied** — the English *Behind the Mirror* artwork is still an ask, and is flagged on the page. |

## Licensed stock — face procedures (added by client 2026-08-25)

| file | source | rights | patient | notes |
|---|---|---|---|---|
| `assets/Face procedures/Untitled design.jpg` (1080×1350) → `src/public/img/procedures/facelift-{600,900,1200}.jpg` | client-supplied, **licensed stock** | licensed | **no — stock model, NOT a patient** | **In use as the Deep Plane Facelift header, on the client's explicit instruction (2026-08-25).** Graded `clean`. I flagged §3 first — *"Never for a face presented as a patient, a staff member, or a result"* — and the client confirmed to proceed. **Mitigations applied:** alt text is descriptive (*"Pre-operative facial markings drawn before surgery"*) and never asserts a patient relationship; no caption claims it is his work; it is recorded here as stock so it can never be mistaken for patient media. **Open gate: revisit before any public launch** — the whole preview is `noindex` and access-controlled today, so nothing is publicly presented as his patient. |
| `src/public/img/detail/marking-{600,860}.jpg` | crop of the above | licensed | no | **The usable part.** Gloved hands, marking pen, surgical cap, no identifiable face — "abstract detail", which §3 permits. Graded `clean`. Upscaled ~2× from a corner of the frame, so it is **soft: use as a supporting or band image, not as a hero.** |

## Hero source replaced 2026-08-25

| file in `src/public` | source | rights | patient | notes |
|---|---|---|---|---|
| `video/hero-{1920.mp4,1600.webm,1280.mp4}` · `img/hero-poster.jpg` | **`assets/hero vid.mp4`** (3840×2160, 14.85s, 30fps) — supplied 2026-08-25, replaces `assets/hero video.mp4` | client-owned | **yes — releases confirmed by client 2026-08-23** | 8.92s loop. **8.83–13.30s of the source is intraoperative** (open draped abdomen, visible incisions) and is excluded — a tone call, not a consent one. Seamless loop: tail dissolved into head. Built by `tools/hero-cut.sh`. |
| `video/hero-m-608.{mp4,webm}` · `img/hero-poster-m.jpg` | same | client-owned | **yes — as above** | 608×1080 portrait cut, each shot cropped on its own column. Where the **body is the subject** (the marking, the result) the crop centres the body; where he is working it centres him. `tools/hero-cut-mobile.sh`. |

> **Note:** `assets/hero video.mp4` no longer exists — it was replaced, not kept. The hero
> avatars (`img/avatars/p{1,2,3}.jpg`) and `img/band/consult-1200.jpg` were derived from it
> and remain valid files, but cannot be re-derived from the current source.


## Procedure headers supplied by client 2026-08-25

| file | source | rights | patient | notes |
|---|---|---|---|---|
| `assets/procedures/Face procedures/Rhino.jpg` (1080×1350) → `img/procedures/rhinoplasty-{600,900,1200}.jpg` | client-supplied stock | licensed | **no — stock model** | **In use as the Rhinoplasty header.** Editorial profile on a soft white ground, natural light, no surgical staging — considerably closer to the §4 register than the marked-face image, and much easier to justify under §3 because it reads as an editorial study of a nose rather than a patient mid-procedure. Graded `clean`. Alt text descriptive only: *"Profile view of a nose, assessed in consultation."* |

**It replaced a still cut from his own consultation footage** (8.2s of `hero vid.mp4`),
which is retained in the raw exports should the stock image need withdrawing.


## Scarless Eyelid header supplied by client 2026-08-27

| file | source | rights | patient | notes |
|---|---|---|---|---|
| `assets/procedures/Face procedures/scarless eye surg.jpg` (1350×1688) → `img/procedures/scarless-eyelid-{600,900,1200}.jpg` | client-supplied stock | `[[VERIFY: licence source]]` | **no — stock model, face not identifiable in the published crop** | **In use as the Scarless Eyelid header and as carousel card 11.** Gloved hand steadying the brow above a closed eye. Cover-cropped to 4:5, graded `clean-deep`. It replaced the typographic `.phero--plate` (D-064), which is now unused by any page — the plate's argument moved into the hero definition rather than being lost. |

**Grade profiles, established by matching each in-use file against every LUT rather than
from memory** — the manifest had recorded the wrong one:

| set | grade | evidence |
|---|---|---|
| Body procedures (8) | `clean-deep` | `13.jpg` → `bbl-1200.jpg` rms **0.68**; next nearest `clean` 2.39 |
| Face procedures — facelift, rhinoplasty | `clean` | `face lift.jpg` → `facelift-1200.jpg` rms **0.80**; `clean-deep` 2.82 |
| Scarless Eyelid (new) | `clean-deep` | matched to the eight it now sits beside in the carousel, which runs on `--ink` |

> The face pair being `clean` and everything else `clean-deep` is a real inconsistency,
> not a decision. It is imperceptible at card size; regrading those two to `clean-deep`
> is a two-minute job whenever it is wanted.
