#!/usr/bin/env python3
"""Export every page as a self-contained HTML blob to paste into GoHighLevel.

GHL supplies its own <html>/<head>/<body> and injects global styles, so each blob
is: a scoped <style>, the page markup wrapped in .jca, then a <script>. Nothing
depends on load order or on GHL serving .css/.js with the right MIME type.

    python3 tools/build-ghl.py --base https://your-cdn/assets

Outputs dist/ghl/<page>.html plus ASSETS.txt (everything to upload).
"""
import argparse, base64, pathlib, re, shutil, sys

ROOT = pathlib.Path('src/public')
OUT = pathlib.Path('dist/ghl')

ap = argparse.ArgumentParser()
ap.add_argument('--base', default='ASSET_BASE_URL',
                help='absolute URL the uploaded /img, /video and /fonts live under')
ap.add_argument('--external', action='store_true',
                help='reference site.css/site.js by URL instead of inlining them')
ap.add_argument('--link-fonts', action='store_true',
                help='reference the woff2 by URL instead of embedding them (not advised: '
                     'a font that 404s falls back to Georgia and every metric shifts)')
args = ap.parse_args()
BASE = args.base.rstrip('/')

# ---------------------------------------------------------------- CSS
def scope_css(css: str) -> str:
    """Neutralise the four bare element rules so GHL's globals and ours cannot
    collide in either direction. Everything else is already class-scoped."""
    css = css.replace('html{-webkit-text-size-adjust:100%}',
                      '.jca{-webkit-text-size-adjust:100%}')
    css = re.sub(r'(?m)^body\{margin:0;', '.jca{margin:0;', css)
    css = css.replace('img,video{display:block;max-width:100%}',
                      '.jca img,.jca video{display:block;max-width:100%}')
    css = re.sub(r'(?m)^a\{color:inherit\}', '.jca a{color:inherit}', css)
    return css

css = scope_css((ROOT / 'tokens.css').read_text() + '\n' + (ROOT / 'styles.css').read_text())

if args.link_fonts:
    css = css.replace('/fonts/', f'{BASE}/fonts/')
else:
    # Embed the faces. A hosted font that 404s does not degrade gracefully — it
    # falls back to Georgia/Helvetica and every line length, leading and spacing
    # in the page shifts with it. 122 KB of woff2 is worth never debugging that.
    for f in sorted((ROOT / 'fonts').glob('*.woff2')):
        ref = f'/fonts/{f.name}'
        if ref in css:
            uri = 'data:font/woff2;base64,' + base64.b64encode(f.read_bytes()).decode()
            css = css.replace(ref, uri)

css += f'''

/* ---- GHL host adaptation -------------------------------------------------
   GHL wraps custom code in its own constrained containers, which would stop
   full-bleed sections spanning the viewport. The 100vw trick is a no-op when
   the parent is already full width, so it is safe either way; overflow-x:clip
   absorbs the scrollbar-width difference. */
.jca{{position:relative;overflow-x:clip;
  background:var(--paper);color:var(--ink);
  font:400 var(--t-0)/var(--lead-body) var(--font-body)}}
.jca>header,.jca>nav,.jca>main>section,.jca>footer,.jca>main>*{{
  width:100vw;margin-left:calc(50% - 50vw)}}
.jca *,.jca *::before,.jca *::after{{box-sizing:border-box}}
'''

# ---------------------------------------------------------------- JS
main_js = (ROOT / 'main.js').read_text()
results_js = (ROOT / 'results.js').read_text()

# ---------------------------------------------------------------- pages
PAGES = [p for p in sorted(ROOT.rglob('*.html'))
         if not p.name.startswith('_') and 'hero-' not in p.name and '_parked' not in str(p)]

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir(parents=True)

assets = set()
if args.external:
    (OUT / 'site.css').write_text(css)
    (OUT / 'site.js').write_text(main_js + '\n' + results_js)

for p in PAGES:
    s = p.read_text()
    slug = str(p.relative_to(ROOT)).replace('/index.html', '').replace('.html', '')
    if slug == 'index':
        slug = 'home'

    (OUT / slug).parent.mkdir(parents=True, exist_ok=True)
    body = s[s.index('<body>') + len('<body>'):s.rindex('</body>')]

    # keep the JSON-LD, but it belongs in the page's header code, not the blob
    ld = re.findall(r'<script type="application/ld\+json">.*?</script>', body, re.S)
    body = re.sub(r'<script type="application/ld\+json">.*?</script>\s*', '', body, flags=re.S)
    if ld:
        (OUT / f'{slug}.jsonld.html').write_text('\n'.join(ld) + '\n')

    body = re.sub(r'\s*<script src="/[a-z-]+\.js"[^>]*></script>', '', body)

    # split on the delimiters srcset uses, or whole srcset strings get logged as one path
    for m in re.finditer(r'/(?:img|video|fonts)/[^\s"\',]+', body):
        assets.add(m.group(0))
    body = re.sub(r'"(/(?:img|video|fonts)/)', rf'"{BASE}\1', body)
    # srcset carries bare paths too
    body = re.sub(r'(\s)(/(?:img|video)/)', rf'\1{BASE}\2', body)

    js = main_js + ('\n' + results_js if 'results' in slug else '')
    # The hero <source> elements are built at runtime, so those four video paths
    # live in the JS and not in the markup. Scanning and rewriting only the body
    # left them root-relative: they 404 on the GHL domain and the hero silently
    # falls back to the poster. Scan and rewrite the script too. (D-068)
    for m in re.finditer(r'/(?:img|video|fonts)/[^\s"\',)]+', js):
        assets.add(m.group(0))
    js = re.sub(r'([\'"])(/(?:img|video|fonts)/)', rf'\1{BASE}\2', js)
    if args.external:
        headtag = f'<link rel="stylesheet" href="{BASE}/site.css">'
        tail = f'<script src="{BASE}/site.js" defer></script>'
    else:
        headtag = f'<style>\n{css}\n</style>'
        tail = f'<script>\n{js}\n</script>'

    blob = f'''<!-- {slug} — paste into a GoHighLevel Custom Code element.
     Page-level <head> code (SEO/JSON-LD) goes in the page settings, not here. -->
{headtag}
<div class="jca">
{body.strip()}
</div>
{tail}
'''
    (OUT / f'{slug}.html').write_text(blob)
    print(f'  {slug:28s} {len(blob)/1024:7.1f} KB' + ('  +jsonld' if ld else ''))

for a in sorted(assets):
    if not (ROOT / a.lstrip('/')).exists():
        print(f'  ! missing asset referenced: {a}', file=sys.stderr)
(OUT / 'ASSETS.txt').write_text('\n'.join(sorted(assets)) + '\n')
print(f'\n{len(PAGES)} pages -> dist/ghl/   ·   {len(assets)} assets listed in ASSETS.txt')
print(f'asset base: {BASE}')
