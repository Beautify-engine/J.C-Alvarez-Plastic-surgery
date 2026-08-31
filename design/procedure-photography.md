# Procedure media list — "the moment before"

**Concept:** the craft *before* the outcome — pre-operative marking, gloved hands,
instruments, materials. Never the result; the 68 real cases do that job, in the gallery,
where a patient expects it.

Register set by the client reference (two implants held in open palms, warm window light,
no face): **editorial, tactile, cropped, faceless.**

## The three rules that keep this compliant

1. **No faces. Ever.** §3 bars AI imagery for "a face presented as a patient, a staff
   member, or a result." Every frame below crops above or below the face, or shows only
   hands. If a face appears, the image is out.
2. **Never framed as an outcome.** These are pre-op and in-progress. No "after" language,
   no before/after framing, no smooth-result hero shots. Alt text describes the *action*
   ("a surgeon marking contour lines"), never a result.
3. **Never confusable with the gallery.** Real cases are the evidence. These are
   atmosphere. Different treatment, different placement, different crop language.

Log every generated file in `assets/MANIFEST.md` with `rights: ai-generated`.

---

## The session recipe — prefix EVERY prompt with this

```
Editorial clinical photography. Soft directional window light from camera-left, large and
diffused, warm in temperature. Background: warm neutral — bone, oatmeal, pale plaster or
pale wood — softly out of focus. Shallow depth of field, 85mm at f/2.8, focus on the
point of contact. Natural skin tones, no gloss, no retouching sheen. Muted warm palette:
cream, sand, soft clay, surgical violet as the only saturated accent. Calm, quiet,
expensive. Fine film grain, gentle highlight bloom, lifted matte shadows, low contrast.
No face visible. No text, no logos, no watermarks. Aspect ratio 4:5 portrait.
```

Fix one seed and reuse across all fifteen; use image 1 as style reference for 2–15.
Generate at ≥2400px on the long edge, then run `./tools/grade.sh <folder> deep`.

---

## The fifteen

### Body

| # | procedure | subject |
|---|---|---|
| 1 | **Brazilian Butt Lift** | Gloved hands drawing concentric contour lines with a violet surgical marker across the lower back and hip of a standing patient. Cropped mid-back to upper thigh. The marker tip in sharp focus, the lines reading like topographic contours. |
| 2 | **Skinny BBL** | Brass calipers held against a marked hip, measuring proportion. Finer, more restrained marking than #1 — a few precise lines rather than full contours. Cropped waist to thigh. |
| 3 | **Breast Augmentation** | Two silicone implants resting in open upturned palms — one smooth, one textured — held toward soft window light so the edges glow and the translucency reads. Warm background, hands in white cuffs. *(the client's reference frame)* |
| 4 | **Breast Lift + Augmentation** | A flexible measuring tape and violet marker resting across folded surgical drape, a gloved hand steadying the tape. Sterile, precise, no skin — measurement as the subject. |
| 5 | **High-Definition Liposuction** | A torso marked with the classic HD cross-hatch grid, raking light across it so the markings and the underlying muscle topography both read. Cropped ribs to hips. No face, no chest. |
| 6 | **Tummy Tuck** | A single clean horizontal line drawn low across the abdomen, a gloved hand smoothing the skin flat beside it. Cropped tight — navel to hipline. The one line is the subject. |

### Face

| # | procedure | subject |
|---|---|---|
| 7 | **Rhinoplasty** | Gloved fingertips steadying the bridge of a nose while a fine marker places two dots. Cropped hard — nose, one cheek, nothing above the bridge. Eyes out of frame. |
| 8 | **Deep Facelift** | A gloved finger tracing the pre-auricular line from temple down past the ear to the jaw. Cropped ear-to-chin, profile, eyes out of frame. |
| 9 | **Face Rejuvenation** | A gloved hand holding a blunt cannula against soft light, the other hand's fingertips resting at a cheekbone. Extreme shallow focus on the cannula tip. |
| 10 | **Eyelid Surgery** | Macro: fine curved iris scissors and Castroviejo forceps held in gloved fingers over a folded drape, tips crossing a millimetre rule so the scale reads. Instruments only. |
| 11 | **Scarless Eyelid Rejuvenation** | A fibre-optic light source held in a gloved hand, glowing warm through translucent surgical drape — light arriving from behind and within. Abstract, no anatomy. |

### Adjacent services

| # | service | subject |
|---|---|---|
| 12 | **Hyperbaric Oxygen** | A hand resting on the steel locking wheel of a hyperbaric chamber door, thick porthole glass beside it lit cool from within, warm room light on the steel. |
| 13 | **Hair Smart Regrowth** | Gloved fingers parting hair at the crown, a fine follicular punch held just above the scalp. Cropped to scalp and hair only. |
| 14 | **Skin Rejuvenation** | A treatment handpiece held in a gloved hand at an angle to soft light, its glass tip catching a highlight. Background warm and out of focus. |
| 15 | **CO2 Laser Resurfacing** | The articulated arm and handpiece of a CO2 laser against a warm wall, a single thin red aiming beam grazing the lens edge, dust visible in the beam. |

---

## Shoot these six instead of generating them

**3, 4, 10, 12, 14, 15** are objects he already owns — implants, marker and tape,
instruments, the chamber, the handpieces. One hour, one window, a sheet of warm card, and
you get the real thing at higher quality than any generator, and it is genuinely his
practice. The recipe above works unchanged as a photographic brief.

The nine involving skin and markings are the ones worth generating — real versions would
require a consenting patient and a release, which is a signed-client conversation.

## Delivery

4:5, ≥2400px, graded with `./tools/grade.sh <folder> deep` (the carousel tiles sit on the
dark band), exported AVIF + WebP with JPEG fallback and `srcset` at 480/800/1200/2400.
