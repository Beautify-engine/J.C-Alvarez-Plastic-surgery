#!/usr/bin/env python3
"""Inline the homepage into one self-contained file (Artifact CSP blocks external hosts)."""
import base64, re, os, pathlib
ROOT = pathlib.Path("src/public")
def b64(p, mime):
    return f"data:{mime};base64," + base64.b64encode(pathlib.Path(p).read_bytes()).decode()

html = (ROOT/"videos.html").read_text()
css  = (ROOT/"tokens.css").read_text() + "\n" + (ROOT/"styles.css").read_text()
js   = (ROOT/"videos.js").read_text()

# fonts -> data URIs
for f in sorted(os.listdir(ROOT/"fonts")):
    if f.endswith(".woff2"):
        css = css.replace(f"/fonts/{f}", b64(ROOT/"fonts"/f, "font/woff2"))

# hero poster + video
css_html_pairs = [("/img/hero-poster.jpg","image/jpeg"), ("/video/hero-1600.webm","video/webm")]
for path, mime in css_html_pairs:
    html = html.replace(path, b64(ROOT/path.lstrip("/"), mime))

# drop the mp4 fallback (webm covers Chrome/Firefox/Safari 16+) to keep the payload down
html = re.sub(r'\s*<source src="/video/hero-1920\.mp4" type="video/mp4">', '', html)

# procedure images: collapse srcset to one inlined size
for slug in ["bbl","skinny-bbl","breast-augmentation","breast-lift-aug","breast-lift",
             "tummy-tuck","hd-liposuction","eyelid-surgery"]:
    uri = b64(ROOT/f"img/procedures/{slug}-900.jpg", "image/jpeg")
    html = re.sub(rf'srcset="[^"]*{re.escape(slug)}-600[^"]*"\s*', '', html)
    html = html.replace(f"/img/procedures/{slug}-900.jpg", uri)

# case tiles: inline the 560w only and drop srcset, or the payload doubles
import glob, os as _os
for f in sorted(glob.glob(str(ROOT/"img/cases/*-[ba].jpg"))):
    name = _os.path.basename(f)
    html = html.replace(f"/img/cases/{name}", b64(f, "image/jpeg"))

for f in sorted(glob.glob(str(ROOT/"img/brand/*.png"))):
    n=_os.path.basename(f); html = html.replace(f"/img/brand/{n}", b64(f,"image/png"))
for f in sorted(glob.glob(str(ROOT/"img/yt/*.jpg"))):
    n=_os.path.basename(f); html = html.replace(f"/img/yt/{n}", b64(f,"image/jpeg"))
for f in sorted(glob.glob(str(ROOT/"img/ig/*.jpg"))):
    n=_os.path.basename(f); html = html.replace(f"/img/ig/{n}", b64(f,"image/jpeg"))

# reels: inline posters + the mp4s (data: URIs work as <video src>)
for f in sorted(glob.glob(str(ROOT/"img/reels/*.jpg"))):
    n=_os.path.basename(f); html = html.replace(f"/img/reels/{n}", b64(f,"image/jpeg"))
for f in sorted(glob.glob(str(ROOT/"video/reels/*.mp4"))):
    n=_os.path.basename(f); html = html.replace(f"/video/reels/{n}", b64(f,"video/mp4"))

# portrait: keep webp (alpha), drop the png fallback + srcset
html = re.sub(r'<source type="image/webp"[^>]*>', '', html)
html = html.replace("/img/about/portrait-700.png", b64(ROOT/"img/about/portrait-700.webp","image/webp"))

# strip document scaffolding — the Artifact wrapper supplies it
html = re.sub(r'^.*?<body>', '', html, flags=re.S)
html = html.replace("</body>\n</html>", "").replace("</body></html>","")
html = re.sub(r'<link rel="stylesheet"[^>]*>', '', html)
html = re.sub(r'<link rel="preload"[^>]*>', '', html)
html = re.sub(r'<script src="/(?:main|videos)\.js"[^>]*></script>', '', html)

# routes that don't exist yet: keep the label, neutralise the click so the preview
# doesn't navigate away from itself
html = re.sub(r'href="(/(?:book|results|procedures|preparation|about|contact|videos)(?:/[A-Za-z0-9\-]+)?)"',
              r'href="#" data-route="\1"', html)
js += '''
// homepage-only preview: explain unbuilt routes instead of dead-ending
document.addEventListener('click', function(e){
  var a = e.target.closest && e.target.closest('a[data-route]');
  if(!a) return;
  e.preventDefault();
  var n = document.getElementById('previewNote');
  n.textContent = a.dataset.route + ' — not built yet. This is the homepage preview.';
  n.hidden = false;
  clearTimeout(window.__t); window.__t = setTimeout(function(){ n.hidden = true; }, 2600);
});
'''
css += '''
#previewNote{position:fixed;left:50%;bottom:1.25rem;transform:translateX(-50%);z-index:60;
  background:var(--ink);color:var(--paper);font:400 var(--t--1)/1 var(--font-body);
  padding:.85em 1.25em;border-radius:var(--r-pill);box-shadow:none;max-width:90vw;text-align:center}
'''
html += '\n<p id="previewNote" role="status" hidden></p>\n'

js += '''
(function(){
  document.addEventListener('click',function(e){
    var b=e.target.closest('.vid__play'); if(!b) return;
    e.preventDefault(); e.stopImmediatePropagation();
    var id=b.closest('.vid__frame').dataset.id;
    window.open('https://www.youtube.com/watch?v='+id,'_blank','noopener');
  },true);
})();
'''

# The artifact CSP blocks maps.google.com, so the facade opens Google Maps in a new
# tab instead of trying (and silently failing) to inline an iframe.
js += '''
(function(){
  var btn=document.getElementById('locLoad'); if(!btn) return;
  var a=document.createElement('a');
  a.className=btn.className; a.href='https://www.google.com/maps/place/8400+SW+8th+St,+Miami,+FL+33144';
  a.target='_blank'; a.rel='noopener'; a.innerHTML=btn.innerHTML;
  a.querySelector('.s').textContent='Open in Google Maps \\u2192';
  btn.replaceWith(a);
})();
'''

out = ('<title>Clavijo Alvarez Video Library</title>\n'
       f'<style>\n{css}\n</style>\n'
       f'{html}\n'
       f'<script>\n{js}\n</script>\n')
pathlib.Path("design/artifact-videos.html").write_text(out)
print(f"design/artifact-videos.html  {len(out)/1024/1024:.2f} MB")
