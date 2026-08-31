#!/usr/bin/env python3
"""List what is still English on a built Spanish page.

    python3 tools/todo-es.py procedimientos/abdominoplastia
    python3 tools/todo-es.py --all

NOT A LANGUAGE HEURISTIC. Guessing the language by vocabulary kept missing things
in both directions: finished Spanish with no accents read as English, and short
English like "Request a consultation." — an H1 — scored zero in both lists and
read as done.

This compares the built page against the English source it was built from. A
string in the build that is byte-identical to a string in the source has not been
touched, which is exact rather than probable. Deliberate pass-throughs — proper
nouns, the address, RealSelf usernames — are identical by design, so anything
declared verbatim in a map (value None, or value == key) is excluded.
"""
import importlib.util, os, re, sys

ARGS = [a for a in sys.argv[1:] if a != "--all"]

spec = importlib.util.spec_from_file_location("b", "tools/build-es.py")
B = importlib.util.module_from_spec(spec)
sys.argv = sys.argv[:1]          # build-es reads argv; keep it out of this
spec.loader.exec_module(B)

TEXT = re.compile(r'>([^<>]{3,})<')
STRIP = re.compile(r'<(script|style|svg)[^>]*>.*?</\1>', re.S | re.I)
ATTR = re.compile(r'\b(alt|aria-label|title|content|placeholder)="([^"]{3,})"')


def strings(html):
    """Every visible or announced string, plus JSON-LD values."""
    out = []
    for _, v in ATTR.findall(html):
        out.append(v)
    for m in TEXT.finditer(STRIP.sub("", html)):
        out.append(re.sub(r"\s+", " ", m.group(1)).strip())
    for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        out += re.findall(r'"(?:name|text|description|headline|howPerformed|'
                          r'preparation|followup|bodyLocation)":\s*"([^"]{3,})"', blk)
    return [s for s in out if s]


def verbatim_keys(name):
    """Strings a map deliberately leaves alone: value None, or value == key."""
    keep = set()
    for m in ("_common", name):
        p = "content/es/%s.py" % m
        if not os.path.exists(p):
            continue
        T = B.load_map(m)
        keep |= {k for k, v in T.items() if v is None or v == k}
        keep |= {str(v) for v in T.values() if v is not None}
    return keep


# Strings that are identical in both languages by nature rather than by decision:
# entities, numbers, phone numbers, and the two meta values that are not prose.
# A string that already carries Spanish orthography is Spanish in the source too
# — his own video titles, the book title, quotes he published in Spanish. Those
# are identical in both builds by nature, not by omission.
ALREADY_ES = re.compile(r'[\u00e1\u00e9\u00ed\u00f3\u00fa\u00fc\u00f1\u00bf\u00a1]|'
                        r'&(aacute|eacute|iacute|oacute|uacute|ntilde|uuml);', re.I)

NOISE = re.compile(r'^(&[a-z]+;|[\s\d.,:+()&#;/-]+|width=device-width.*|noindex.*|'
                   r'[\d\s\u2009,]+)$')


def report(name, src, out):
    built_p = os.path.join(B.OUT, out)
    if not os.path.exists(built_p) or not os.path.exists(src):
        return None
    built = strings(open(built_p, encoding="utf-8").read())
    source = set(strings(open(src, encoding="utf-8").read()))
    keep = verbatim_keys(name)
    left, seen = [], set()
    for s in built:
        if s in source and s not in keep and s not in seen and not NOISE.match(s) \
           and not ALREADY_ES.search(s):
            seen.add(s)
            left.append(s)
    return left


def main():
    args = ARGS or None
    todo = {}
    for name, (src, out) in B.PAGES.items():
        if args and name not in args:
            continue
        r = report(name, src, out)
        if r is not None:
            todo[name] = r
    for name in sorted(todo, key=lambda n: -len(todo[n])):
        left = todo[name]
        print("%-18s %d still English" % (name, len(left)))
        if args or len(todo) == 1:
            for s in left:
                print("   %s" % s)


main()
