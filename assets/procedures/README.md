# Drop procedure images here

Put the **original, ungraded** files in `_originals/`. Any format — jpg, png, webp, heic,
tif. Original filenames are fine; if you can, name them by procedure (`bbl-01.jpg`,
`tummy-tuck-02.jpg`) and I'll wire them straight into the carousel.

Then I run:

```bash
./tools/grade.sh assets/procedures/_originals cool-deep
```

Output lands in `_originals/graded-cool-deep/`. Originals are never modified.

## Which preset

| preset | look |
|---|---|
| `cool` | cool cast, lifted matte blacks, soft haze, moderate contrast |
| **`cool-deep`** | **same but deeper blacks and more contrast — for the dark band. Default for procedure imagery.** |

Warm family (`air` / `standard` / `deep` / `band`) is for portraits, team and facility.

## Before you upload — two checks

1. **No faces**, per CLAUDE.md §3 and `design/procedure-photography.md`. Cropped bodies,
   hands, instruments, markings — yes. Identifiable faces — no.
2. **Nothing that reads as a result.** Pre-op and in-progress only. The 68 real cases do
   the results job, in the gallery.

Anything that arrives with a face or reads as an outcome, I'll flag rather than grade.

## Logging

Every file gets a row in `assets/MANIFEST.md` with `rights:` (`ai-generated` | `licensed` |
`client-owned`) and `patient:` (`yes` | `no`). Tell me the source when you upload and I'll
fill it in.
