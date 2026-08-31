#!/usr/bin/env python3
"""Bundle the static site into paste-ready blocks for GoHighLevel.

GHL builds a page out of "custom code" elements holding raw HTML, with CSS inline
in <style> and images re-hosted on its own CDN. That is verified behaviour, not a
guess — goapluscredit.com/case-study serves 12 custom-code blocks, 15 inline <style>
blocks, images on assets.cdn.filesafe.space, and its body text is present in the
server HTML (so GHL is server-rendering, which is what §6 rule 1 requires).

    python3 tools/bundle-ghl.py                  # build, leave /img/... paths alone
    python3 tools/bundle-ghl.py --map assets.csv # build and rewrite paths to GHL CDN
    python3 tools/bundle-ghl.py --links links.csv # rewrite internal links to GHL URLs
    python3 tools/bundle-ghl.py --only tummy-tuck

INTERNAL LINKS
There are 525 internal link instances in the build (93 of them to /book alone). If the
GHL page paths are set to match ours exactly — /procedures/breast-lift, not
/breast-lift — every one of those keeps working untouched and --links is unnecessary.
Use --links only for pages GHL forces onto a different path. links.csv is
route,ghl_url and the rewrite preserves any ?query string on the link.

Output lands in out/ghl/:

    _sitewide.css   paste ONCE into GHL Settings > Custom CSS
    _sitewide.js    paste ONCE into GHL Settings > Tracking Code (header)
    assets.csv      314 rows; fill the ghl_url column after bulk-uploading media
    pages/<slug>/block.html    paste into the page's custom-code element
    pages/<slug>/meta.txt      title + description for the SEO tab
    pages/<slug>/schema.json   JSON-LD for the Schema Generator (GHL's code widget
                               strips ld+json, so it cannot ride along in block.html)

WHY THE CSS IS SCOPED
Our class names collide with GHL's own in 11 places that we actually use in markup —
.btn .nav .wrap .topbar .ft .ft__col .ft__top .ft__brand .hero__cta .d .dot — and
GHL's rules would otherwise reassign our buttons, nav and page gutters. So every
selector is rewritten under .jca and each block is wrapped in <div class="jca">.
@font-face and @keyframes are left alone (scoping them breaks them), and :root
becomes .jca — custom properties inherit, so the tokens still reach everything.
"""
import argparse, csv, json, os, re, shutil, sys

SRC = "src/public"
OUT = "out/ghl"
SCOPE = "jca"                      # wrapper class; must not collide with GHL's
CSS_FILES = ["tokens.css", "styles.css", "procedure.css"]
JS_FILES = ["main.js", "procedure.js", "results.js", "videos.js", "book.js"]
SKIP = ("_parked", "_hero-ab", "hero-options", "hero-headlines")

# NOT anchored on a preceding quote or paren. srcset packs several URLs into one
# attribute separated by ", " — a lookbehind for ["'(] matches only the first, silently
# leaving every 900w/1200w candidate pointing at a path that will not exist on the host.
# Found by diffing the site's asset list against what was actually uploaded: 18 files
# were "in the media library but unused", and all 18 were later srcset entries.
ASSET_RE = re.compile(r'(?<![\w.\-/])(/(?:img|video|fonts)/[^"\'()\s,]+)')


# ---------------------------------------------------------------- CSS scoping

def scope_css(css, scope):
    """Prefix every selector with .scope. Leaves at-rules that must stay global."""
    out, i, n = [], 0, len(css)
    while i < n:
        # Consume whitespace BEFORE dispatching. Without this, "}\n@media{...}"
        # arrives with i on the newline, the @-branch never fires, and the whole
        # at-rule is treated as a selector — yielding ".jca @media (...)" with an
        # unscoped body. Two silent ways to unstyle the page from one missing strip.
        if css[i].isspace():
            j = i
            while j < n and css[j].isspace():
                j += 1
            out.append(css[i:j]); i = j; continue

        # comments pass through untouched
        if css.startswith("/*", i):
            j = css.find("*/", i + 2)
            j = n if j == -1 else j + 2
            out.append(css[i:j]); i = j; continue

        # at-rules: @media/@supports recurse into their body, the rest pass through
        if css[i] == "@":
            brace = css.find("{", i)
            semi = css.find(";", i)
            if semi != -1 and (brace == -1 or semi < brace):
                out.append(css[i:semi + 1]); i = semi + 1; continue
            prelude = css[i:brace]
            depth, j = 1, brace + 1
            while j < n and depth:
                if css[j] == "{": depth += 1
                elif css[j] == "}": depth -= 1
                j += 1
            body = css[brace + 1:j - 1]
            name = prelude.split()[0].lower()
            if name in ("@media", "@supports", "@layer", "@container"):
                body = scope_css(body, scope)          # conditional group: recurse
            # @font-face, @keyframes, @property, @charset: body is not selectors
            out.append(prelude + "{" + body + "}")
            i = j; continue

        # a normal rule
        brace = css.find("{", i)
        if brace == -1:
            out.append(css[i:]); break
        depth, j = 1, brace + 1
        while j < n and depth:
            if css[j] == "{": depth += 1
            elif css[j] == "}": depth -= 1
            j += 1
        sel, body = css[i:brace], css[brace + 1:j - 1]
        # A comment can sit inside the selector run (the usual "/* why */\n.thing{"
        # shape). Left in place it becomes part of the selector and yields
        # ".jca /* why */ .thing", a descendant selector that matches nothing —
        # which silently unstyles the page. Lift comments out, scope what remains.
        comments = re.findall(r"/\*.*?\*/", sel, re.S)
        sel = re.sub(r"/\*.*?\*/", "", sel, flags=re.S)
        if not sel.strip():
            out.append("".join(comments)); i = j; continue
        out.append("".join(comments) + scope_selector(sel, scope) + "{" + body + "}")
        i = j
    return "".join(out)


def scope_selector(sel, scope):
    lead = sel[:len(sel) - len(sel.lstrip())]
    parts = []
    for one in sel.strip().split(","):
        s = one.strip()
        if not s:
            continue
        # :root holds the design tokens. Custom properties inherit, so moving them
        # onto the wrapper still reaches every descendant.
        if s in (":root", "html", "body", ":root,html", "*"):
            parts.append("." + scope if s != "*" else ".%s *" % scope)
            continue
        if s.startswith(":root"):
            parts.append("." + scope + s[len(":root"):])
            continue
        if s.startswith(("html ", "body ")):
            parts.append(".%s %s" % (scope, s.split(None, 1)[1]))
            continue
        if s.startswith("." + scope):
            parts.append(s)
            continue
        parts.append(".%s %s" % (scope, s))
    return lead + ",".join(parts)


# ---------------------------------------------------------------- page parsing

def routes():
    found = []
    for dp, _dn, fn in os.walk(SRC):
        if any(s in dp for s in SKIP):
            continue
        for f in sorted(fn):
            if not f.endswith(".html") or any(f.startswith(s) for s in SKIP):
                continue
            rel = os.path.relpath(os.path.join(dp, f), SRC)
            route = "/" + rel[:-5]
            route = route.replace("/index", "") or "/"
            found.append((route, os.path.join(dp, f)))
    return sorted(found, key=lambda r: (r[0].count("/"), r[0]))


def slug(route):
    return "home" if route == "/" else route.strip("/").replace("/", "-")


def split_page(html):
    """Return (body_inner, title, description, [json-ld blocks], [inline styles])."""
    title = re.search(r"<title>(.*?)</title>", html, re.S)
    desc = re.search(r'<meta name="description" content="(.*?)">', html, re.S)
    ld = re.findall(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', html, re.S)

    body = re.search(r"<body[^>]*>(.*)</body>", html, re.S)
    body = body.group(1) if body else html

    # page-local <style> blocks ride along with the block, scoped like the rest
    inline = re.findall(r"<style[^>]*>(.*?)</style>", body, re.S)
    body = re.sub(r"<style[^>]*>.*?</style>", "", body, flags=re.S)

    # strip what GHL supplies or rejects: our own script tags, ld+json, and the
    # skip link (GHL pages have their own landmark structure)
    body = re.sub(r'<script[^>]*application/ld\+json[^>]*>.*?</script>', "", body, flags=re.S)
    body = re.sub(r'<script[^>]*src="/[^"]*"[^>]*>\s*</script>', "", body)

    clean = lambda m: re.sub(r"\s+", " ", m.group(1)).strip() if m else ""
    return body.strip(), clean(title), clean(desc), [b.strip() for b in ld], inline


def rewrite_links(html, link_map):
    """Swap href="/route" for the mapped GHL URL, keeping any ?query intact.
    Longest route first, so /procedures/bbl is not eaten by /procedures."""
    for route in sorted(link_map, key=len, reverse=True):
        target = link_map[route]
        html = re.sub(r'href="%s(\?[^"]*)?"' % re.escape(route),
                      lambda m: 'href="%s%s"' % (target, m.group(1) or ""), html)
    return html


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--map", help="CSV with local_path,ghl_url to rewrite asset paths")
    ap.add_argument("--asset-prefix", help="Prefix every /img|/video|/fonts path with this "
                    "origin, e.g. https://cdn.example.com . Far cheaper than --map: one "
                    "value instead of 328 hand-collected CDN URLs.")
    ap.add_argument("--links", help="CSV with route,ghl_url to rewrite internal links")
    ap.add_argument("--only", help="build one route, matched as a substring")
    ap.add_argument("--scope", default=SCOPE)
    args = ap.parse_args()

    if not os.path.isdir(SRC):
        sys.exit("run from the project root")

    prefix = (args.asset_prefix or "").rstrip("/")
    url_map = {}
    if args.map:
        with open(args.map, newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                if row.get("ghl_url", "").strip():
                    url_map[row["local_path"]] = row["ghl_url"].strip()
        print("asset map: %d of them filled in" % len(url_map))

    link_map = {}
    if args.links:
        with open(args.links, newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                if row.get("ghl_url", "").strip():
                    link_map[row["route"].strip()] = row["ghl_url"].strip()
        print("link map: %d routes redirected" % len(link_map))

    shutil.rmtree(OUT, ignore_errors=True)
    os.makedirs(OUT + "/pages", exist_ok=True)

    # ---- sitewide CSS and JS, concatenated once ----
    css = "\n".join(
        "/* ===== %s ===== */\n%s" % (f, open(os.path.join(SRC, f), encoding="utf-8").read())
        for f in CSS_FILES)
    css = scope_css(css, args.scope)
    js = "\n".join(
        "/* ===== %s ===== */\n%s" % (f, open(os.path.join(SRC, f), encoding="utf-8").read())
        for f in JS_FILES)

    assets = set(ASSET_RE.findall(css)) | set(ASSET_RE.findall(js))

    pages, skipped = [], []
    for route, path in routes():
        if args.only and args.only not in route:
            continue
        html = open(path, encoding="utf-8").read()
        body, title, desc, ld, inline = split_page(html)
        for s in inline:
            css += "\n/* ===== inline: %s ===== */\n%s" % (route, scope_css(s, args.scope))
        assets.update(ASSET_RE.findall(body))

        d = os.path.join(OUT, "pages", slug(route))
        os.makedirs(d, exist_ok=True)
        block = '<div class="%s">\n%s\n</div>\n' % (args.scope, body)
        if url_map or prefix:
            block = ASSET_RE.sub(
                lambda m: url_map.get(m.group(1), prefix + m.group(1) if prefix else m.group(1)),
                block)
        if link_map:
            block = rewrite_links(block, link_map)
        open(os.path.join(d, "block.html"), "w", encoding="utf-8").write(block)
        open(os.path.join(d, "meta.txt"), "w", encoding="utf-8").write(
            "PATH\n%s\n\nTITLE\n%s\n\nMETA DESCRIPTION\n%s\n\nROBOTS\nnoindex,nofollow"
            "   <- keep until the spec period ends (CLAUDE.md §3)\n" % (route, title, desc))
        if ld:
            open(os.path.join(d, "schema.json"), "w", encoding="utf-8").write(
                ",\n".join(ld) if len(ld) > 1 else ld[0])
        pages.append((route, slug(route), len(block), len(ld), bool(title), bool(desc)))

    if url_map or prefix:
        sub = lambda m: url_map.get(m.group(1), prefix + m.group(1) if prefix else m.group(1))
        css = ASSET_RE.sub(sub, css)
        js = ASSET_RE.sub(sub, js)

    open(OUT + "/_sitewide.css", "w", encoding="utf-8").write(css)
    open(OUT + "/_sitewide.js", "w", encoding="utf-8").write(js)

    # a links.csv stub, pre-filled with every route so it is just a paste-in job
    with open(OUT + "/links.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["route", "ghl_url"])
        for route, _s, _sz, _n, _t, _d in pages:
            w.writerow([route, ""])
        for route in ("/privacy", "/accessibility"):
            w.writerow([route, ""])

    with open(OUT + "/assets.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["local_path", "bytes", "exists", "ghl_url"])
        for a in sorted(assets):
            p = SRC + a
            w.writerow([a, os.path.getsize(p) if os.path.exists(p) else 0,
                        "yes" if os.path.exists(p) else "MISSING", ""])

    total = sum(os.path.getsize(SRC + a) for a in assets if os.path.exists(SRC + a))
    missing = [a for a in assets if not os.path.exists(SRC + a)]

    print("\n%-32s %8s %7s %5s" % ("route", "block", "schema", "meta"))
    print("-" * 56)
    for route, _s, size, nld, t, d in pages:
        print("%-32s %7.1fk %7s %5s" % (route, size / 1024, nld or "-",
                                        "ok" if t and d else "CHECK"))
    print("-" * 56)
    print("%d pages   sitewide css %.0fk   js %.0fk" %
          (len(pages), len(css) / 1024, len(js) / 1024))
    print("%d assets, %.1f MB%s" % (len(assets), total / 1024 / 1024,
                                    "" if not missing else "   MISSING: %d" % len(missing)))
    for a in missing:
        print("   missing", a)
    if prefix:
        print("\nasset paths rewritten to %s/img/..., %s/video/..., %s/fonts/..."
              % (prefix, prefix, prefix))
    elif not url_map:
        print("\nasset paths left as /img/... — either serve the asset folders from an "
              "origin that keeps the paths and re-run with --asset-prefix, or fill "
              "ghl_url in %s/assets.csv and re-run with --map" % OUT)


if __name__ == "__main__":
    main()
