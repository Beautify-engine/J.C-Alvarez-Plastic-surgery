# Illustration brief — hand this to an illustrator

The diagrams currently on `/procedures/tummy-tuck` are **placeholders I drew in raw SVG
paths**. They are correct and they sit on the grid, but they are not commissioned craft —
the line has no weight variation, the anatomy is schematic, and every procedure would
inherit the same limitation. This is the brief to replace them.

---

## What to commission

### Set A — anatomical diagrams · 4 per procedure · **the priority**

Per procedure, four states of the same figure. Tummy tuck shown as the example:

| # | shows | must read as |
|---|---|---|
| A1 | Skin laxity | The overhang that will not retract. **Best in ¾ or profile view** — my front view cannot show it, which is the clearest weakness in the current set |
| A2 | Diastasis recti | Two rectus bands with a measurable gap; arrows indicating closure |
| A3 | Localised fat | Flank volume outside the waist line |
| A4 | The operation | Incision at the bikini line, the zone removed, the navel repositioned |

Across 11 procedures that is ~44 diagrams. **Start with 3 procedures** (tummy tuck, BBL,
breast augmentation) and see how the first set lands before commissioning the rest.

### Set B — procedure marks · 11 · lower priority

One mark per procedure for the hub and nav. Currently `❌ S1` in `ASSET-REQUEST.md`.
Single weight, 24px grid, must survive at 24px.

---

## Specification — non-negotiable, this is what makes them work in the build

- **Format: clean SVG.** Paths only. No embedded raster, no clipping masks, no text.
- **`fill="none"`, `stroke="currentColor"`.** The colour is set by CSS so one file works on
  the cream ground and the dark ground. **A file with baked-in colour is unusable.**
- **`stroke-width` in the 1–2.5 range**, with the base outline lighter than the marked
  feature. Weight variation between the body outline and the annotated part is exactly
  what my versions lack.
- **`stroke-linecap="round"`, `stroke-linejoin="round"`.**
- **Consistent viewBox across the set** so the figures do not jump between states.
  Current build uses `0 0 180 212`; the illustrator may propose another, but all four
  states of a procedure must share it and the figure must sit identically in each.
- **Layer the marks in named groups** — `<g data-l="incision">`, `data-l="skin"`,
  `data-l="muscle"`, `data-l="lipo"`, `data-l="navel"`. The build fades these
  independently as the reader scrolls the steps. **Without the groups the pinned-plate
  interaction does not work.**
- Optimised: run through SVGO, no editor metadata, no `<style>` blocks.

## Register

**Reference:** Aesop product diagrams · Kinfolk · high-end architecture drawings ·
technical patent illustration. Restrained, confident, editorial.

**Not:** clinical textbook rendering, 3D medical render, cross-hatched shading, anything
with a gradient, and nothing resembling a stock anatomy icon set. §4 of the project
constitution bars icon soup; these must read as diagrams that carry information, not as
decoration.

**No faces, no identifiable individuals, no skin texture.** The figure is a form, not a
person.

---

## Where to find someone

| source | notes |
|---|---|
| **ami.org** — Association of Medical Illustrators, "Find an Artist" | The right specialism. Ask specifically for editorial/line work, not clinical rendering, or you get textbook plates |
| **Behance / Dribbble** — search `editorial line illustration`, `medical line art`, `technical illustration` | Widest range. Filter hard for line-only portfolios |
| **Folio / Handsome Frank / Levy Creative** (illustration agencies) | Pricier, but they art-direct for you |

**Budget:** roughly $150–400 per spot from an independent illustrator. A first set of
12 diagrams (3 procedures × 4 states) lands around **$2–4k**. Agencies run 2–3×.

**Ask for:** two sample states of one procedure before committing to the full set.

---

## Before commissioning anything — check he already has someone

The thumbnail on his **"Tummy Tuck Master Class"** video (`fZx_V94QQU0`, 2 months old)
contains a genuine anatomical diagram of an abdomen with marked planes. **Somebody drew
that for him.**

If that person exists and is reachable, they are the cheapest and most consistent path:
the diagrams on the site would then match the diagrams in his own video content, which is
worth more than a stylistic upgrade. Worth one question before spending anything.
