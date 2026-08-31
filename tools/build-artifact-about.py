#!/usr/bin/env python3
"""Inline /about into one self-contained file (Artifact CSP blocks external hosts)."""
import base64, glob, os, pathlib, re

ROOT = pathlib.Path("src/public")
def b64(p, mime):
    return f"data:{mime};base64," + base64.b64encode(pathlib.Path(p).read_bytes()).decode()

html = (ROOT / "about.html").read_text()
css  = (ROOT / "tokens.css").read_text() + "\n" + (ROOT / "styles.css").read_text()

for f in sorted(os.listdir(ROOT / "fonts")):
    if f.endswith(".woff2"):
        css = css.replace(f"/fonts/{f}", b64(ROOT / "fonts" / f, "font/woff2"))

# keep webp where one exists, drop the <source> + srcset and inline a single file
html = re.sub(r'<source type="image/webp"[^>]*>', "", html)
html = re.sub(r'\s*srcset="[^"]*"', "", html)
html = re.sub(r'\s*sizes="[^"]*"', "", html)
for src, real, mime in [
    ("/img/about/jc-panel-760.jpg",  "img/about/jc-panel-760.webp",  "image/webp"),
    ("/img/about/team-700.jpg",      "img/about/team-1100.webp",     "image/webp"),
    ("/img/about/interview-640.jpg", "img/about/interview-960.webp", "image/webp"),
    ("/img/band/consult-1200.jpg",   "img/band/consult-1200.jpg",    "image/jpeg"),
    ("/img/about/book-es-520.jpg",   "img/about/book-es-780.webp",   "image/webp"),
]:
    html = html.replace(src, b64(ROOT / real, mime))

for pat, mime in [("img/about/signature-*.png", "image/png"),
                  ("img/badges/*.png", "image/png"),
                  ("img/brand/*.png", "image/png")]:
    for f in sorted(glob.glob(str(ROOT / pat))):
        n = os.path.basename(f)
        html = html.replace("/" + str(pathlib.Path(pat).parent / n), b64(f, mime))

# strip document scaffolding — the Artifact wrapper supplies it
html = re.sub(r"^.*?<body>", "", html, flags=re.S)
html = html.replace("</body>\n</html>", "").replace("</body></html>", "")
html = re.sub(r'<link rel="(stylesheet|preload)"[^>]*>', "", html)
html = re.sub(r'<script src="/main\.js"[^>]*></script>', "", html)

# unbuilt routes: keep the label, neutralise the click
html = re.sub(r'href="(/(?:book|results|procedures|preparation|contact|privacy|accessibility)'
              r'(?:/[A-Za-z0-9\-]+)?)"', r'href="#" data-route="\1"', html)

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
  n.textContent = a.dataset.route + ' \\u2014 not built yet. This is the About preview.';
  n.hidden = false;
  clearTimeout(window.__t); window.__t = setTimeout(function () { n.hidden = true; }, 2600);
});
"""

# A data: URI cannot go in srcset — the comma in "data:image/jpeg;base64," is the
# srcset candidate separator, so the attribute parses to nothing and the browser
# renders a broken image. Drop every inlined srcset and the <source> elements that
# carry one; the plain src (already inlined) is what should serve. (D-055)
html = re.sub(r'<source[^>]*srcset="data:[^"]*"[^>]*>', '', html)
html = re.sub(r'\s*srcset="data:[^"]*"', '', html)

out = ('<title>About Dr. JC Alvarez</title>\n'
       f"<style>\n{css}\n</style>\n{html}\n<script>\n{js}\n</script>\n")
pathlib.Path("design/artifact-about.html").write_text(out)
print(f"design/artifact-about.html  {len(out)/1024/1024:.2f} MB")
