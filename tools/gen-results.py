#!/usr/bin/env python3
"""Generate /results — the full case gallery. 50 cases, filterable, ungated (§5.2)."""
import os, re, collections, pathlib

CASES_DIR = pathlib.Path('src/public/img/cases')
LABEL = {'bbl': 'Brazilian Butt Lift', 'breast-augmentation': 'Breast Augmentation',
         'tummy-tuck': 'Tummy Tuck', 'rhinoplasty': 'Rhinoplasty',
         'eyelid-surgery': 'Eyelid Surgery', 'facelift': 'Deep Facelift',
         'hd-liposuction': 'HD Liposuction'}
ORDER = ['bbl', 'breast-augmentation', 'tummy-tuck', 'rhinoplasty',
         'eyelid-surgery', 'facelift', 'hd-liposuction']

# cases withheld for angle mismatch — see content/case-rejects.txt
rejects = set()
rp = pathlib.Path('content/case-rejects.txt')
if rp.exists():
    for line in rp.read_text().splitlines():
        line = line.split('#')[0].strip()
        if line:
            rejects.add(line)

# The client replaced the split before/after halves with whole slide compositions
# on 2026-08-25: one 1000x1000 square per case, with his own Before/After labels
# and title bar baked in. A case is now ONE image, not a pair. (D-057)
found = collections.defaultdict(set)
for f in os.listdir(CASES_DIR):
    m = re.match(r'(.+)-(\d+)\.jpg$', f)
    if m and not m.group(1).endswith(('-t', '-600')) and f'{m.group(1)}-{m.group(2)}' not in rejects:
        found[m.group(1)].add(m.group(2))
for slug in ORDER:
    assert slug in found, f'no cases for {slug}'

# interleave procedures so the unfiltered grid does not open with nine of one thing
buckets = {s: sorted(found[s]) for s in ORDER}
sequence = []
while any(buckets.values()):
    for s in ORDER:
        if buckets[s]:
            sequence.append((s, buckets[s].pop(0)))
total = len(sequence)

filters = ['        <button type="button" data-filter="all" aria-pressed="true">'
           f'All<span class="n">{total}</span></button>']
for s in ORDER:
    filters.append(f'        <button type="button" data-filter="{s}" aria-pressed="false">'
                   f'{LABEL[s]}<span class="n">{len(found[s])}</span></button>')

cards = []
for i, (slug, num) in enumerate(sequence):
    label, n = LABEL[slug], str(int(num))
    eager = i < 6
    loading = '' if eager else ' loading="lazy"'
    prio = ' fetchpriority="high"' if i < 2 else ''
    cards.append(f'''        <li class="gal__i" data-procedure="{slug}">
          <button class="gal__c" type="button" data-full="/img/cases/{slug}-{num}.jpg"
                  aria-label="{label}, case {n} — open larger">
            <span class="gal__frame">
              <img src="/img/cases/{slug}-{num}-600.jpg" width="600" height="600"
                   decoding="async"{loading}{prio} alt="{label}, case {n}: before and after">
            </span>
            <span class="gal__meta"><span class="gal__proc">{label}</span><span class="gal__n">{n:0>2}</span></span>
          </button>
        </li>''')

HEAD = pathlib.Path('src/public/about.html').read_text()
head = HEAD[:HEAD.index('<main id="main">')]
head = head.replace('<title>About Julio Clavijo Alvarez, MD — Plastic Surgeon in Miami</title>',
                    '<title>Before &amp; After Results — Julio Clavijo Alvarez, MD, Miami</title>')
head = head.replace('<meta name="description" content="A doctorate in surgical research before a career in plastic surgery. The story behind the way Dr. Julio Clavijo Alvarez plans surgery and recovery in Miami.">',
                    f'<meta name="description" content="{total} documented before-and-after cases from Dr. Julio Clavijo Alvarez in Miami, filed by procedure. No form, no email — the cases are open.">')
head = head.replace('<li><a href="/about" aria-current="page">About</a></li>',
                    '<li><a href="/about">About</a></li>')
head = head.replace('<li><a href="/results">Results</a></li>',
                    '<li><a href="/results" aria-current="page">Results</a></li>')

FOOT = pathlib.Path('src/public/about.html').read_text()
foot = FOOT[FOOT.index('<footer class="ft">'):FOOT.index('</footer>') + len('</footer>')]

nl = '\n'
page = f'''{head}<main id="main">

  <section class="gal" aria-labelledby="gal-h">
    <div class="wrap">

      <div class="gal__head">
        <p class="eyebrow">Results</p>
        <h1 id="gal-h">Look for someone built like you.</h1>
        <p class="gal__lede">{total} documented cases, filed by procedure &mdash; his own
          before-and-after records, published as he keeps them.</p>
        <p class="gal__ungated">No form. No email. Nothing to unlock.</p>
      </div>

      <div class="res__filters gal__filters" role="group" aria-label="Filter cases by procedure">
{nl.join(filters)}
      </div>

      <p class="gal__count" role="status" aria-live="polite">Showing all {total} cases</p>

      <ul class="gal__grid" id="galGrid">
{nl.join(cards)}
      </ul>

      <p class="gal__note">Every case is Dr. Alvarez&rsquo;s own patient. Results vary
        between people; these are individual outcomes, not a promise of yours.</p>

    </div>
  </section>

  <section class="ab-cta" aria-labelledby="gcta-h">
    <div class="wrap ab-cta__in">
      <div>
        <h2 id="gcta-h">Bring the one that looks like you.</h2>
        <p>Screenshot the case you keep coming back to and bring it. It is the fastest way
          to a straight answer about what your own body will do.</p>
      </div>
      <a class="btn btn--on-dark" href="/book">Request a Consultation
        <span class="arw" aria-hidden="true">&rarr;</span></a>
    </div>
  </section>

  <dialog class="lb" id="lb" aria-label="Case viewer">
    <button class="lb__x" type="button" data-lb-close aria-label="Close">&times;</button>
    <figure class="lb__fig">
      <div class="lb__one"><img id="lbImg" src="" alt=""></div>
      <figcaption class="lb__cap">
        <span id="lbTitle"></span>
        <a class="btn btn--on-dark" href="/book">Request a Consultation
          <span class="arw" aria-hidden="true">&rarr;</span></a>
      </figcaption>
    </figure>
  </dialog>

</main>

{foot}

<script src="/main.js" defer></script>
<script src="/results.js" defer></script>
</body>
</html>
'''
pathlib.Path('src/public/results.html').write_text(page)
print(f'results.html — {total} cases, {len(ORDER)} filters')
