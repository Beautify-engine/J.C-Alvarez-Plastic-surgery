#!/usr/bin/env python3
"""Inline /results into one self-contained file (Artifact CSP blocks external hosts)."""
import base64, glob, os, pathlib, re

ROOT = pathlib.Path("src/public")
def b64(p, mime):
    return f"data:{mime};base64," + base64.b64encode(pathlib.Path(p).read_bytes()).decode()

html = (ROOT / "results.html").read_text()
css  = (ROOT / "tokens.css").read_text() + "\n" + (ROOT / "styles.css").read_text()
js   = (ROOT / "results.js").read_text()

for f in sorted(os.listdir(ROOT / "fonts")):
    if f.endswith(".woff2"):
        css = css.replace(f"/fonts/{f}", b64(ROOT / "fonts" / f, "font/woff2"))

# only the cases actually on the page — the reject list keeps four out
# grid uses the 600px copies; the viewer's full-size slide is swapped to the same
# file so the artifact does not carry both (64 x 1000px would double the payload)
html = html.replace('data-full="/img/cases/', 'data-full="__F__/img/cases/')
html = re.sub(r'data-full="__F__/img/cases/([a-z0-9\-]+)\.jpg"',
              r'data-full="/img/cases/\1-600.jpg"', html)
used = set(re.findall(r'/img/cases/([a-z0-9\-]+\.jpg)', html))
for n in sorted(used):
    html = html.replace(f"/img/cases/{n}", b64(ROOT / "img/cases" / n, "image/jpeg"))
for f in sorted(glob.glob(str(ROOT / "img/brand/*.png"))):
    n = os.path.basename(f)
    html = html.replace(f"/img/brand/{n}", b64(f, "image/png"))

html = re.sub(r"^.*?<body>", "", html, flags=re.S)
html = html.replace("</body>\n</html>", "").replace("</body></html>", "")
html = re.sub(r'<link rel="(stylesheet|preload)"[^>]*>', "", html)
html = re.sub(r'<script src="/(main|results)\.js"[^>]*></script>', "", html)

html = re.sub(r'href="(/(?:book|procedures|preparation|contact|about|videos|privacy|accessibility)'
              r'(?:/[A-Za-z0-9\-]+)?)"', r'href="#" data-route="\1"', html)

css += """
#previewNote{position:fixed;left:50%;bottom:1.25rem;transform:translateX(-50%);z-index:80;
  background:var(--paper);color:var(--ink);font:400 var(--t--1)/1.35 var(--font-body);
  padding:.85em 1.25em;border-radius:var(--r-pill);max-width:90vw;text-align:center}
"""
html += '\n<p id="previewNote" role="status" hidden></p>\n'
js += """
document.addEventListener('click', function (e) {
  var a = e.target.closest && e.target.closest('a[data-route]');
  if (!a) return;
  e.preventDefault();
  var n = document.getElementById('previewNote');
  n.textContent = a.dataset.route + ' \\u2014 not built yet. This is the results preview.';
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

out = ('<title>Results — Dr. JC Alvarez</title>\n'
       f"<style>\n{css}\n</style>\n{html}\n<script>\n{js}\n</script>\n")
pathlib.Path("design/artifact-results.html").write_text(out)
print(f"design/artifact-results.html  {len(out)/1024/1024:.2f} MB  ({len(used)} case images inlined)")
