#!/usr/bin/env python3
"""Build the Spanish site from the English source plus a per-page copy map.

The English tree in src/public stays the reviewable source of truth — the client-side
lead reads English and approves there. Spanish is generated into src/es, page by page,
from a hand-authored map in content/es/<page>.py.

The maps are transcreations, not translations. Where an English line trades on English
rhythm it is rewritten as a Spanish line that does the same job, so this cannot be a
machine-translation step and the map files are the deliverable a native reviewer reads.

    python3 tools/build-es.py home

WHAT IS DELIBERATELY NOT TRANSLATED
Patient reviews. They are quoted verbatim from real people on RealSelf; translating a
quotation and still presenting it as that person's words is the same class of problem as
inventing one. They stay in their original language and the page labels them. A map entry
whose value is None means "leave exactly as written" and is used for these.
"""
import glob, importlib.util, json, os, re, shutil, sys

SLUGS = {
    "/": "/",
    "/results": "/resultados",
    "/procedures": "/procedimientos",
    "/preparation": "/preparacion",
    "/videos": "/videos",
    "/about": "/sobre-el-dr-alvarez",
    "/contact": "/contacto",
    "/book": "/consulta",
    "/privacy": "/privacidad",
    "/accessibility": "/accesibilidad",
    "/procedures/tummy-tuck": "/procedimientos/abdominoplastia",
    "/procedures/bbl": "/procedimientos/aumento-de-gluteos",
    "/procedures/skinny-bbl": "/procedimientos/skinny-bbl",
    "/procedures/hd-liposuction": "/procedimientos/liposuccion-alta-definicion",
    "/procedures/breast-augmentation": "/procedimientos/aumento-de-senos",
    "/procedures/breast-lift": "/procedimientos/levantamiento-de-senos",
    "/procedures/breast-lift-aug": "/procedimientos/levantamiento-y-aumento-de-senos",
    "/procedures/facelift": "/procedimientos/levantamiento-facial-profundo",
    "/procedures/rhinoplasty": "/procedimientos/rinoplastia",
    "/procedures/eyelid-surgery": "/procedimientos/blefaroplastia",
    "/procedures/scarless-eyelid": "/procedimientos/parpados-sin-cicatrices",
}

# Source page -> output path inside the Spanish tree.
#
# CLOUDFLARE PAGES ROUTING, which is what decides these filenames:
#   about.html                     is served at /about
#   procedimientos/index.html      is served at /procedimientos
#   procedimientos/rinoplastia.html is served at /procedimientos/rinoplastia
# So a section with children uses a directory + index.html, and everything else is
# a flat <slug>.html. Do NOT have both procedimientos.html and a procedimientos/
# directory — the two compete for the same route.
PAGES = {
 "home":            ("src/public/index.html",                            "index.html"),
 "resultados":      ("src/public/results.html",                          "resultados.html"),
 "procedimientos":  ("src/public/procedures/index.html",                 "procedimientos/index.html"),
 "preparacion":     ("src/public/preparation.html",                      "preparacion.html"),
 "videos":          ("src/public/videos.html",                           "videos.html"),
 "sobre":           ("src/public/about.html",                            "sobre-el-dr-alvarez.html"),
 "contacto":        ("src/public/contact.html",                          "contacto.html"),
 "consulta":        ("src/public/book/index.html",                       "consulta.html"),
 "privacidad":      ("src/public/privacy.html",                          "privacidad.html"),
 "accesibilidad":   ("src/public/accessibility.html",                    "accesibilidad.html"),
 "abdominoplastia": ("src/public/procedures/tummy-tuck.html",            "procedimientos/abdominoplastia.html"),
 "gluteos":         ("src/public/procedures/bbl.html",                   "procedimientos/aumento-de-gluteos.html"),
 "skinny-bbl":      ("src/public/procedures/skinny-bbl.html",            "procedimientos/skinny-bbl.html"),
 "lipo-hd":         ("src/public/procedures/hd-liposuction.html",        "procedimientos/liposuccion-alta-definicion.html"),
 "aumento-senos":   ("src/public/procedures/breast-augmentation.html",   "procedimientos/aumento-de-senos.html"),
 "lev-senos":       ("src/public/procedures/breast-lift.html",           "procedimientos/levantamiento-de-senos.html"),
 "lev-aum-senos":   ("src/public/procedures/breast-lift-aug.html",       "procedimientos/levantamiento-y-aumento-de-senos.html"),
 "facial":          ("src/public/procedures/facelift.html",              "procedimientos/levantamiento-facial-profundo.html"),
 "rinoplastia":     ("src/public/procedures/rhinoplasty.html",           "procedimientos/rinoplastia.html"),
 "blefaroplastia":  ("src/public/procedures/eyelid-surgery.html",        "procedimientos/blefaroplastia.html"),
 "parpados":        ("src/public/procedures/scarless-eyelid.html",       "procedimientos/parpados-sin-cicatrices.html"),
 # Cloudflare Pages serves /404.html for any unmatched route automatically.
 "404":             ("src/public/_404-src.html",                          "404.html"),
}
OUT = "dist-es"


def load_map(name):
    p = "content/es/%s.py" % name
    spec = importlib.util.spec_from_file_location("m", p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.T


def swap_links(html):
    """Rewrite internal hrefs, longest route first so /procedures is not eaten
    before /procedures/bbl. Any ?query is preserved."""
    for en in sorted(SLUGS, key=len, reverse=True):
        es = SLUGS[en]
        if en == es:
            continue
        # Keep whatever follows the route: ?query AND #fragment. Handling only the
        # query left breadcrumb links like /procedures#body pointing at the English
        # tree, which 404s on the Spanish site.
        html = re.sub(r'href="%s([?#][^"]*)?"' % re.escape(en),
                      lambda m: 'href="%s%s"' % (es, m.group(1) or ""), html)
    return html


def apply_copy(html, T):
    """Replace text nodes and the handful of attributes that carry visible or
    announced copy. Longest first, so a short string that is a substring of a
    longer one cannot corrupt it."""
    hits = misses = 0
    for src in sorted(T, key=len, reverse=True):
        dst = T[src]
        if dst is None:                      # verbatim: leave untouched
            continue
        before = html
        # A text node is rarely flush against its tags. It usually carries leading or
        # trailing whitespace, and is often followed by a nested <span> (an arrow, a
        # count) rather than a closing tag. Matching only ">src<" silently missed the
        # nav CTA, the hero credit line and the proof row. Allow the whitespace and
        # let the node end at either a closing tag or the next element.
        # The map keys are whitespace-normalised (one line), but the HTML wraps its
        # paragraphs across several. re.escape alone therefore matched only the
        # single-line strings — most of the body copy silently passed through. Let any
        # run of whitespace in the key match any run in the markup.
        flex = r'\s+'.join(re.escape(w) for w in src.split())
        pat = r'(>)(\s*)%s(\s*)(?=<)' % flex
        html = re.sub(pat, lambda m: m.group(1) + m.group(2) + dst + m.group(3), html)
        for attr in ("alt", "aria-label", "title", "content"):
            html = html.replace('%s="%s"' % (attr, src), '%s="%s"' % (attr, dst))
        html = html.replace("<title>%s</title>" % src, "<title>%s</title>" % dst)
        hits += (html != before)
        misses += (html == before)
    return html, hits, misses


def main():
    """Build the whole Spanish tree. A page with no copy map yet is still emitted —
    with Spanish slugs, Spanish links and lang="es" — so routing can be deployed and
    tested before every page is translated. Those pages are listed as UNTRANSLATED so
    nobody mistakes them for finished."""
    import glob
    shutil.rmtree(OUT, ignore_errors=True)

    # assets and stylesheets ride along unchanged
    # NOT "fonts": since the move to Google Fonts (D-072) nothing references the
    # local woff2 files. They were still shipping — 196kb of dead weight — because
    # the copy list had never been revisited.
    for sub in ("img", "video"):
        if os.path.isdir(os.path.join("src/public", sub)):
            shutil.copytree(os.path.join("src/public", sub), os.path.join(OUT, sub))
    # hero-options.css is a parked exploration, referenced only in comments.
    for f in (glob.glob("src/public/*.css") + glob.glob("src/public/*.js")):
        if os.path.basename(f) == "hero-options.css":
            continue
        os.makedirs(OUT, exist_ok=True)
        shutil.copy2(f, os.path.join(OUT, os.path.basename(f)))

    done, todo = [], []
    for name, (src, out) in PAGES.items():
        if not os.path.exists(src):
            todo.append((name, "SOURCE MISSING")); continue
        html = open(src, encoding="utf-8").read()
        html = html.replace('<html lang="en">', '<html lang="es">', 1)

        mapfile = "content/es/%s.py" % name
        if os.path.exists(mapfile):
            html, hits, _ = apply_copy(html, load_map(name))
            done.append((name, hits))
        else:
            todo.append((name, "no content/es/%s.py yet" % name))

        html = swap_links(html)
        html = html.replace('"@context": "https://schema.org",',
                            '"@context": "https://schema.org",\n  "inLanguage": "es",', 1)
        dst = os.path.join(OUT, out)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        open(dst, "w", encoding="utf-8").write(html)

    # _headers and _redirects are authored for the Spanish tree and kept in
    # config/es/ so a rebuild never overwrites them with the English versions.
    for f in ("_headers", "_redirects", "robots.txt", "llms.txt"):
        src_f = os.path.join("config/es", f)
        if os.path.exists(src_f):
            shutil.copy2(src_f, os.path.join(OUT, f))

    print("built %s — %d pages" % (OUT, len(PAGES)))
    print()
    print("  TRANSLATED (%d):" % len(done))
    for n, h in done:
        print("     %-18s %d strings" % (n, h))
    print("  STILL ENGLISH (%d) — routing and slugs are correct, copy is not:" % len(todo))
    for n, why in todo:
        print("     %-18s %s" % (n, why))


if __name__ == "__main__":
    main()
