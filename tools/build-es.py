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

# The origin this build will be served from, used for rel="canonical" and og:url.
# Set it when the domain is settled:
#
#     SITE=https://jcalvarez.pages.dev python3 tools/build-es.py
#
# Left empty the build emits no canonical and says so, which is the right default:
# a canonical pointing at a URL this site is not served from is worse than none —
# it hands every page's ranking to a URL that may not exist. The JSON-LD in the
# English source still declares jcalvarezplasticsurgery.com, his current live site,
# which is exactly why this cannot be guessed here.
SITE = os.environ.get("SITE", "").rstrip("/")

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
        # Absolute URLs inside JSON-LD (@id, breadcrumb item, canonical, og:url).
        # These are not hrefs, so the rule above never saw them: the Spanish pages
        # were declaring breadcrumbs and canonicals pointing at English routes that
        # do not exist on this site. A broken breadcrumb item is a structured-data
        # error, and a canonical to a non-existent URL is worse than none.
        html = re.sub(r'(https?://[^"\s]*?)%s(?=["#?])' % re.escape(en),
                      lambda m: m.group(1) + es, html)
    return html


LD_RE = re.compile(r'<script type="application/ld\+json">.*?</script>', re.S)

# The English pages are inconsistent about entities: about.html writes a literal
# em dash where the procedure pages write &mdash;, and both are correct HTML. A
# map key written one way silently failed to match markup written the other, and
# a silent failure here looks exactly like a finished page. Each of these matches
# either spelling.
_EQ = {}
for _ent, _ch in (("&mdash;", "\u2014"), ("&ndash;", "\u2013"), ("&rsquo;", "\u2019"),
                  ("&lsquo;", "\u2018"), ("&hellip;", "\u2026"), ("&nbsp;", "\u00a0"),
                  ("&middot;", "\u00b7"), ("&times;", "\u00d7")):
    _alt = "(?:%s|%s)" % (_ent, _ch)
    _EQ[_ent] = _alt
    _EQ[_ch] = _alt
_EQ_RE = re.compile("|".join(re.escape(k) for k in sorted(_EQ, key=len, reverse=True)))


UNUSED = []


def flex_of(src):
    """A whitespace-tolerant, entity-tolerant pattern for one map key.

    The equivalences have to be spliced in around re.escape rather than run over
    its output: re.escape also escapes "&", so substituting into the escaped word
    left the backslash stranded in front of the alternation and the pattern would
    not compile."""
    def word(w):
        out, last = [], 0
        for m in _EQ_RE.finditer(w):
            out.append(re.escape(w[last:m.start()]))
            out.append(_EQ[m.group(0)])
            last = m.end()
        out.append(re.escape(w[last:]))
        return "".join(out)
    return r"\s+".join(word(w) for w in src.split())


def apply_copy(html, T):
    """Replace text nodes, the handful of attributes that carry visible or
    announced copy, and the string values inside JSON-LD. Longest first, so a
    short string that is a substring of a longer one cannot corrupt it.

    JSON-LD is pulled out before the text pass and put back after. Its strings sit
    inside a <script>, so the >text< pattern never reached them: every procedure
    page was shipping a Spanish FAQ on the page and an English FAQPage in the
    structured data. Google reads that as a mismatch between markup and content,
    and it is the one part of the page written purely for a search engine — the
    one place a language slip goes unnoticed until it costs rankings."""
    del UNUSED[:]
    lds = LD_RE.findall(html)
    for i, block in enumerate(lds):
        html = html.replace(block, "\x00LD%d\x00" % i, 1)
    hits = misses = 0
    for src in sorted(T, key=len, reverse=True):
        dst = T[src]
        if dst is None or dst == src:
            # None means verbatim. dst == src is the same intent written the other
            # way — a proper noun, an address, a brand — and neither is a miss.
            continue
        before, before_lds = html, list(lds)
        # A text node is rarely flush against its tags. It usually carries leading or
        # trailing whitespace, and is often followed by a nested <span> (an arrow, a
        # count) rather than a closing tag. Matching only ">src<" silently missed the
        # nav CTA, the hero credit line and the proof row. Allow the whitespace and
        # let the node end at either a closing tag or the next element.
        # The map keys are whitespace-normalised (one line), but the HTML wraps its
        # paragraphs across several. re.escape alone therefore matched only the
        # single-line strings — most of the body copy silently passed through. Let any
        # run of whitespace in the key match any run in the markup.
        pat = r'(>)(\s*)%s(\s*)(?=<)' % flex_of(src)
        html = re.sub(pat, lambda m: m.group(1) + m.group(2) + dst + m.group(3), html)
        for attr in ("alt", "aria-label", "title", "content"):
            html = html.replace('%s="%s"' % (attr, src), '%s="%s"' % (attr, dst))
            # Video buttons label themselves "Play: <title>". Whole-value matching
            # never reached the title, so every reel on a Spanish page announced
            # itself in English to a screen reader.
            html = html.replace('%s="Play: %s"' % (attr, src),
                                '%s="Reproducir: %s"' % (attr, dst))
        html = html.replace("<title>%s</title>" % src, "<title>%s</title>" % dst)
        # JSON-LD carries plain text, not entities, so a key written with &mdash;
        # will not match here. Those get their own plain-text entries in the map.
        lds = [b.replace('"%s"' % src, '"%s"' % dst) for b in lds]
        if html != before or lds != before_lds:
            hits += 1
        else:
            misses += 1
            UNUSED.append(src)
    for i, block in enumerate(lds):
        html = html.replace("\x00LD%d\x00" % i, block, 1)
    return apply_patterns(html, T), hits, misses


def apply_patterns(html, T):
    """Template alt text that carries a number. There are 84 of these across the
    eleven procedure pages and they change with every case added, so they belong
    in a rule rather than in a copy map somebody has to remember to update."""
    html = re.sub(r'Case (\d+) of (\d+), before and after',
                  r'Caso \1 de \2, antes y despu&eacute;s', html)
    html = re.sub(r'([A-Z][A-Za-z\- ]{2,40}), case (\d+): before and after',
                  lambda m: "%s, caso %s: antes y despu&eacute;s"
                            % (T.get(m.group(1), m.group(1)), m.group(2)), html)
    # The gallery's 64 open-larger buttons.
    html = re.sub(r'([A-Z][A-Za-z\- ]{2,40}), case (\d+) (?:&mdash;|—) open larger',
                  lambda m: "%s, caso %s \u2014 ver m&aacute;s grande"
                            % (T.get(m.group(1), m.group(1)), m.group(2)), html)
    # The case counter, "01 of 09". Numeric, so it cannot be a map key.
    html = re.sub(r'>(\d{2}) of (\d{2})<', r'>\1 de \2<', html)
    # Any remaining "Play:" prefix — the title after it is a real YouTube title and
    # stays exactly as he published it.
    html = html.replace('aria-label="Play: ', 'aria-label="Reproducir: ')
    return html


def route_of(out):
    """The clean URL a built file is served at, matching Cloudflare's
    html_handling: auto-trailing-slash. index.html is the root of its directory."""
    r = "/" + out[:-len(".html")] if out.endswith(".html") else "/" + out
    if r.endswith("/index"):
        r = r[:-len("/index")]
    return r or "/"


def add_canonical(html, out):
    """Self-referencing canonical plus og:url. Every page shipped without either —
    on a site that also answers to a .pages.dev preview domain and to whatever
    custom domain gets attached, that is how the same page ends up indexed twice."""
    if not SITE:
        return html
    url = SITE + route_of(out)
    tags = '<link rel="canonical" href="%s">\n  <meta property="og:url" content="%s">\n  ' % (url, url)
    return html.replace("</head>", tags + "</head>", 1) if "</head>" in html else html


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
    # JavaScript writes copy at runtime — the gallery count, the booking form's
    # step announcements, the map's iframe title. None of it is in the built HTML,
    # so it stayed English on the Spanish site with nothing to catch it.
    JS_EDITS = {}
    if os.path.exists("content/es/_js.py"):
        spec = importlib.util.spec_from_file_location("es_js", "content/es/_js.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        JS_EDITS = mod.EDITS

    for f in (glob.glob("src/public/*.css") + glob.glob("src/public/*.js")):
        base = os.path.basename(f)
        if base == "hero-options.css":
            continue
        os.makedirs(OUT, exist_ok=True)
        if base in JS_EDITS:
            src_js = open(f, encoding="utf-8").read()
            for old_s, new_s in JS_EDITS[base]:
                if src_js.count(old_s) != 1:
                    raise SystemExit(
                        "content/es/_js.py: %s — this no longer matches the English "
                        "source exactly once (found %d):\n  %s"
                        % (base, src_js.count(old_s), old_s.strip()[:90]))
                src_js = src_js.replace(old_s, new_s)
            open(os.path.join(OUT, base), "w", encoding="utf-8").write(src_js)
        else:
            shutil.copy2(f, os.path.join(OUT, base))

    COMMON = load_map("_common") if os.path.exists("content/es/_common.py") else {}
    done, todo = [], []
    for name, (src, out) in PAGES.items():
        if not os.path.exists(src):
            todo.append((name, "SOURCE MISSING")); continue
        html = open(src, encoding="utf-8").read()
        html = html.replace('<html lang="en">', '<html lang="es">', 1)

        # _common carries everything that repeats across 8+ pages — the template's
        # section headings, the recovery timeline, the surgeon strip, the booking
        # summary. It is applied to every page first; the page's own map is applied
        # after and therefore wins on any string both define.
        combined = dict(COMMON)
        mapfile = "content/es/%s.py" % name
        if os.path.exists(mapfile):
            combined.update(load_map(name))
        html, hits, _ = apply_copy(html, combined)
        # A key that matches nothing is almost always a typo against the English
        # source, and it fails silently — the page just stays English in that one
        # spot. Only reported for pages that have their own map; the shared map is
        # deliberately larger than any single page needs.
        page_keys = set(load_map(name)) if os.path.exists(mapfile) else set()
        stale = sorted(k for k in UNUSED if k in page_keys)
        if os.path.exists(mapfile):
            done.append((name, hits, stale))
        else:
            todo.append((name, "%d shared strings only" % hits))

        html = swap_links(html)
        html = html.replace('"@context": "https://schema.org",',
                            '"@context": "https://schema.org",\n  "inLanguage": "es",', 1)
        html = add_canonical(html, out)
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
    if SITE:
        print("  canonical + og:url on every page, rooted at %s" % SITE)
    else:
        print("  NO canonical, NO og:url — set SITE=https://... to emit them")
    print()
    print("  TRANSLATED (%d):" % len(done))
    for n, h, stale in done:
        print("     %-18s %d strings%s" % (n, h, "" if not stale else
              "   \u2014 %d KEY(S) MATCHED NOTHING" % len(stale)))
        for k in stale:
            print("        no match: %s" % (k[:88] + ("\u2026" if len(k) > 88 else "")))
    print("  STILL ENGLISH (%d) — routing and slugs are correct, copy is not:" % len(todo))
    for n, why in todo:
        print("     %-18s %s" % (n, why))


if __name__ == "__main__":
    main()
