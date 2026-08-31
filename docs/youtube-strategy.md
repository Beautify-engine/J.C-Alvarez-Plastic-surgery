# YouTube — use it as a content library, not as a trust badge

Channel: `youtube.com/@drjcalvarez` · id `UC06qDqPc2gjuv38lvsX2LRw`
Feed pulled 2026-08-22 via the public RSS endpoint (no scraping).

## What is actually there

**Cadence is genuinely impressive.** 15 videos published between 8 and 22 August — close to
daily. His channel description: *"I share expert tips, patient journeys, and everything you
need to know about achieving natural, beautiful results."*

**But the audience is not.** Views on those 15: **11, 28, 34, 35, 41, 49, 58, 66, 69, 74,
102, 125, 147, 187, 197.**

| | Instagram | YouTube |
|---|---|---|
| Audience | 148,000 followers | small |
| Per-post reach | 7,000–18,000 | **11–197** |

**So: do not put YouTube subscriber or view counts on the site.** Beside "148K followers"
they read as weakness, and a visitor who clicks through sees the gap immediately. The
Instagram numbers are the trust asset. YouTube is something else.

**Every video is in Spanish.** All 15. Relevant for the EN/ES/RU split — these are ready
for the Spanish site and need subtitles or English re-records for the English one.

## Why the content is still valuable — very

Every title is **a patient question he answers on camera**:

- *¿Cuándo puedo volver a trabajar después de un facelift?* — when can I return to work
- *¿Qué pasa con el pubis después de un tummy tuck?*
- *¿El gym borra los resultados de un BBL?* — does the gym undo a BBL
- *¿Levantamiento de seno antes o después de los hijos?* — breast lift before or after children
- *Cómo se corrige una lipo que no quedó como esperabas* — correcting a lipo that went wrong
- *¿Qué se opera primero después de una pérdida masiva de weight?*

That is **fear #4 (recovery and downtime) and fear #1 (will it look right) answered in his
own voice**, dozens of times over. `docs/conversion-doctrine.md` says naming the fear out
loud builds more trust than avoiding it. He has been doing exactly that, daily, to an
audience of forty people.

**The channel is under-performing content, not weak content. The site is where it should
have been living all along.**

## How to use it

| # | use | value |
|---|---|---|
| 1 | **Patient story videos → the reviews problem.** Client says some videos are patient reviews. A real patient on camera outperforms any text testimonial and sidesteps the fabricated-testimonial block in `content/facts.md`. **Highest value — needs signed releases.** |
| 2 | **Video titles become the FAQ.** Each title is already a real patient question. Pair question + his video + a short written answer → `FAQPage` + `VideoObject` schema on one page. |
| 3 | **Per-procedure embeds.** His explainer for that procedure on that procedure page. Deepens thin pages, raises dwell time, gives Google indexable video. |
| 4 | **The recovery section.** "When can I return to work" is the single most-asked pre-op question and he has already answered it. |
| 5 | **A real `/videos` library.** His current site has a Videos nav item; rebuild it filterable by procedure and topic. |

## Technical rules

- **Never a standard YouTube iframe on load** — ~900KB plus cookies, and it alone would put
  ≥90 mobile Performance out of reach. Use the same **facade** pattern as the map: a
  self-hosted thumbnail and a play control, player mounts on click.
- **`youtube-nocookie.com`** as the embed origin.
- **Self-host thumbnails.** `i.ytimg.com` is a third-party request on every card.
- **`VideoObject` JSON-LD** per embedded video — name, description, thumbnail, uploadDate,
  duration, embedUrl. This is how video wins SERP real estate (§5.7).
- Pull the catalogue through the **YouTube Data API** (free, needs a key) or the RSS feed,
  never by scraping the channel page.

## What we still need

- `[[VERIFY]]` Which videos are **patient stories** vs educational — and whether those
  patients signed releases covering web use.
- `[[VERIFY]]` Any **English-language** videos, or budget for subtitling.
- Total video count and channel age (RSS returns only the latest 15).
