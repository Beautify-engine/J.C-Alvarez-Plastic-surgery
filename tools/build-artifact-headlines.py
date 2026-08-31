#!/usr/bin/env python3
"""Inline the hero-headline comparison into one self-contained file.

The Artifact CSP blocks every external host, so fonts, images and both video
cuts are embedded as data: URIs.
"""
import base64, glob, os, pathlib, re

ROOT = pathlib.Path("src/public")

def b64(p, mime):
    return f"data:{mime};base64," + base64.b64encode(pathlib.Path(p).read_bytes()).decode()

html = (ROOT / "hero-headlines.html").read_text()
css = "\n".join((ROOT / f).read_text() for f in
                ("tokens.css", "styles.css", "hero-options.css"))

# fonts
for f in sorted(os.listdir(ROOT / "fonts")):
    if f.endswith(".woff2"):
        css = css.replace(f"/fonts/{f}", b64(ROOT / "fonts" / f, "font/woff2"))

# posters, badges, logo
for path, mime in [("/img/hero-poster.jpg", "image/jpeg"),
                   ("/img/hero-poster-m.jpg", "image/jpeg")]:
    html = html.replace(path, b64(ROOT / path.lstrip("/"), mime))
for f in sorted(glob.glob(str(ROOT / "img/badges/*.png"))):
    n = os.path.basename(f)
    html = html.replace(f"/img/badges/{n}", b64(f, "image/png"))
for f in sorted(glob.glob(str(ROOT / "img/avatars/*.jpg"))):
    n = os.path.basename(f)
    html = html.replace(f"/img/avatars/{n}", b64(f, "image/jpeg"))
for f in sorted(glob.glob(str(ROOT / "img/brand/*.png"))):
    n = os.path.basename(f)
    html = html.replace(f"/img/brand/{n}", b64(f, "image/png"))

# Both cuts go in, so the mobile render is still what a phone gets. webm only —
# VP9 covers Chrome, Firefox and Safari 16+, and carrying the mp4 as well would
# nearly double the payload for no added reach.
D = b64(ROOT / "video/hero-1600.webm", "video/webm")
M = b64(ROOT / "video/hero-m-608.webm", "video/webm")
html = html.replace(
    "[['/video/hero-m-608.webm', 'video/webm'], ['/video/hero-m-608.mp4', 'video/mp4']]",
    f"[['{M}', 'video/webm']]")
html = html.replace(
    "[['/video/hero-1600.webm',  'video/webm'], ['/video/hero-1920.mp4',  'video/mp4']]",
    f"[['{D}', 'video/webm']]")

# strip document scaffolding — the Artifact wrapper supplies it
html = re.sub(r"^.*?<body>", "", html, flags=re.S)
html = html.replace("</body></html>", "").replace("</body>\n</html>", "")
html = re.sub(r'<link rel="stylesheet"[^>]*>', "", html)
html = re.sub(r"<style>.*?</style>", lambda m: m.group(0), html, flags=re.S)  # keep page <style>

# unbuilt routes: keep the label, neutralise the click
html = re.sub(r'href="(/(?:book|results|procedures|preparation|about|contact|videos)'
              r'(?:/[A-Za-z0-9\-]+)?)"', r'href="#" data-route="\1"', html)
html = html.replace('href="#recovery"', 'href="#" data-route="#recovery (not built yet)"')

css += """
#previewNote{position:fixed;left:50%;bottom:1.25rem;transform:translateX(-50%);z-index:60;
  background:var(--ink);color:var(--paper);font:400 var(--t--1)/1.35 var(--font-body);
  padding:.85em 1.25em;border-radius:var(--r-pill);max-width:90vw;text-align:center}
"""
html += '\n<p id="previewNote" role="status" hidden></p>\n'

js = """
document.addEventListener('click', function (e) {
  var a = e.target.closest && e.target.closest('a[data-route]');
  if (!a) return;
  e.preventDefault();
  var n = document.getElementById('previewNote');
  n.textContent = a.dataset.route + ' \\u2014 not built yet. This is the hero comparison.';
  n.hidden = false;
  clearTimeout(window.__t); window.__t = setTimeout(function () { n.hidden = true; }, 2600);
});
"""

out = ('<title>Alvarez Hero Headlines</title>\n'
       f"<style>\n{css}\n</style>\n{html}\n<script>\n{js}\n</script>\n")
pathlib.Path("design/artifact-headlines.html").write_text(out)
print(f"design/artifact-headlines.html  {len(out)/1024/1024:.2f} MB")
