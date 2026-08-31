#!/usr/bin/env python3
"""Put the RealSelf reviews into the homepage, /results and /preparation.

content/reviews.json is the single source. Verbatim text, attributed to the
handle RealSelf shows, with the date and a link back to the profile.
"""
import html as H, json, pathlib, re

D = json.loads(pathlib.Path('content/reviews.json').read_text())
REVIEWS = D['reviews']
PROFILE = 'https://www.realself.com/dr/julio-clavijo-alvarez-miami-fl'
MONTHS = ['January','February','March','April','May','June','July','August',
          'September','October','November','December']

def when(d):
    y, m, _ = d.split('-')
    return f'{MONTHS[int(m)-1]} {y}'

def esc(t):
    return H.escape(t, quote=False).replace('&lt;', '<').replace('&gt;', '>')

def card(r, cls='rev__q'):
    lang = f' lang="{r["lang"]}"' if r.get('lang') else ''
    return (f'<blockquote class="{cls}"><p{lang}>{esc(r["quote"])}</p>'
            f'<footer><span>{esc(r["procedure"])}</span>'
            f'<span>{r["id"]}</span><span>{when(r["date"])}</span></footer></blockquote>')

# ---------------------------------------------------------------- homepage
p = pathlib.Path('src/public/index.html'); s = p.read_text()
run = '\n          '.join(card(r) for r in REVIEWS)
s = re.sub(r'(<div class="rev__run">\s*)(?:<blockquote class="rev__q">.*?</blockquote>\s*)+(</div>)',
           lambda m: m.group(1) + run + '\n          ' + m.group(2), s, flags=re.S)
s = s.replace('<p class="rev__note">Placeholder copy &mdash; real reviews pending verification</p>',
              f'<p class="rev__note">Verbatim from <a href="{PROFILE}" rel="noopener" target="_blank">'
              f'his RealSelf profile</a> &mdash; {len(REVIEWS)} of them, oldest first published 2018.</p>')
p.write_text(s)
print('homepage:', s.count('rev__q'), 'quotes')

# ---------------------------------------------------------------- /preparation
p = pathlib.Path('src/public/preparation.html'); s = p.read_text()
PICK = ['jaileen23', 'torijudd', 'KM46', 'the dashing olive']   # recovery-specific
by = {r['id']: r for r in REVIEWS}
items = '\n'.join(
    f'''        <li class="pr-v">
          <blockquote><p{' lang="'+by[i]["lang"]+'"' if by[i].get("lang") else ''}>{esc(by[i]["quote"])}</p></blockquote>
          <p class="pr-v__who"><span>{esc(by[i]["procedure"])}</span><span>{i}</span><span>{when(by[i]["date"])}</span></p>
        </li>''' for i in PICK)
s = re.sub(r'(<ul class="pr-v__list">\s*)(?:<li class="pr-v">.*?</li>\s*)+(\s*</ul>)',
           lambda m: m.group(1) + items + '\n        ' + m.group(2), s, flags=re.S)
s = s.replace('<h2 id="voices-h">Nobody photographs week one.</h2>',
              '<h2 id="voices-h">Nobody photographs week one.</h2>\n        '
              f'<p class="pr-note">Verbatim from <a href="{PROFILE}" rel="noopener" target="_blank">'
              'his RealSelf profile</a>.</p>')
p.write_text(s)
print('preparation:', s.count('class="pr-v"'), 'quotes')

# ---------------------------------------------------------------- /results
p = pathlib.Path('src/public/results.html'); s = p.read_text()
if 'rev__q' not in s:
    six = '\n          '.join(card(r) for r in REVIEWS[:6])
    block = f'''
  <section class="rev" aria-labelledby="rres-h">
    <div class="wrap">
      <div class="rev__layout">
        <div class="rev__head">
          <p class="eyebrow">In their words</p>
          <h2 id="rres-h">A case can&rsquo;t tell you what he was like.</h2>
          <p>The photographs show the result. They can&rsquo;t show you whether he listened,
            what recovery actually felt like, or whether he talked someone out of something.</p>
          <p class="rev__note">Verbatim from <a href="{PROFILE}" rel="noopener" target="_blank">his RealSelf profile</a>.</p>
        </div>
        <div class="rev__col rev__col--a">
          <div class="rev__run">
          {six}
          </div>
        </div>
        <div class="rev__col rev__col--b" aria-hidden="true">
          <div class="rev__run">
          {six}
          </div>
        </div>
      </div>
    </div>
  </section>
'''
    s = s.replace('  <section class="ab-cta"', block + '\n  <section class="ab-cta"')
    p.write_text(s)
print('results:', s.count('rev__q'), 'quotes')
