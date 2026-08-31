#!/usr/bin/env python3
"""List what is still English on a built Spanish page.

The build already applies _common, so this is the exact remaining work for that
page's own map — not the whole source. It reads the BUILT file, so anything the
shared map or a pattern rule already handles never appears here.

    python3 tools/todo-es.py dist-es/procedimientos/aumento-de-gluteos.html
"""
import re, sys, html

# Accents alone are not enough to tell the two apart: plenty of finished Spanish
# lines carry none ("No se trata de", "La faja se coloca antes de que despierte").
# Scoring both vocabularies and comparing is what stops those being reported as
# unfinished work every time.
EN = re.compile(r'\b(the|and|your|you|with|that|before|after|from|what|does|do|did|'
                r'will|would|should|can|could|his|her|for|not|are|this|he|it|of|is|'
                r'on|was|were|been|have|has|had|which|who|whom|whose|they|them|'
                r'their|there|these|those|when|where|why|how|about|into|than|then|'
                r'only|every|most|more|less|other|same|own|both|each|any|all|need|'
                r'as|well|too|first|last|long|much|many|my|me|we|us|our|be|am|so|'
                r'if|but|out|up|down|over|under|again|still|just|like|make|makes|'
                r'take|takes|get|gets|go|goes|say|says|know|see|look|looks|in|at|to|an|'
                r'or|by|its|day|days|week|weeks|month|months|hour|hours|year|'
                r'years|left|right|under|above|through|around|between|without)\b', re.I)
ES = re.compile(r'\b(el|la|los|las|un|una|unos|unas|de|del|al|que|se|con|por|para|'
                r'su|sus|como|pero|cuando|donde|porque|desde|hasta|sobre|entre|'
                r'este|esta|esto|eso|ese|esa|lo|le|les|ya|muy|mas|sin|antes|'
                r'despues|siempre|nunca|cada|todo|toda|todos|todas|usted|no|es|'
                r'son|est\u00e1|est\u00e1n|hay|ser|tiene|puede|va|vuelve)\b', re.I)
ACC = re.compile(r'[\u00e1\u00e9\u00ed\u00f3\u00fa\u00fc\u00f1\u00bf\u00a1\u00ab\u00bb]|'
                 r'&(a|e|i|o|u|n)?(acute|ntilde|eacute|aacute|oacute|iacute|uacute)')


def english(t):
    """Compare vocabularies rather than look for accents. Accents alone miss
    plenty of finished Spanish ("No se trata de"), and short English fragments
    ("Small incisions, hidden in creases", "7 - 10 days") carry none of the long
    function words — which is why the English list reaches down to in/at/to/or
    and to the units a recovery timeline is written in."""
    if ACC.search(t):
        return False
    en = len(EN.findall(t))
    es = len(ES.findall(t))
    return en > es


def main(path):
    s = open(path, encoding="utf-8").read()
    out = []

    for tag, val in re.findall(r'\b(alt|aria-label|title|content|placeholder)="([^"]{6,})"', s):
        if english(val) and val not in out:
            out.append(val)

    body = re.search(r'<main.*?</main>', s, re.S)
    body = re.sub(r'<(script|style|svg)[^>]*>.*?</\1>', '', body.group(0), flags=re.S | re.I)
    for m in re.finditer(r'>([^<>]{3,})<', body):
        t = re.sub(r'\s+', ' ', m.group(1)).strip()
        if t and english(t) and t not in out:
            out.append(t)

    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        for t in re.findall(r'"(?:name|text|description|headline|howPerformed|preparation|followup|bodyLocation)":\s*"([^"]{6,})"', m.group(1)):
            if english(t) and t not in out:
                out.append("[LD] " + t)

    t = re.search(r'<title>([^<]*)</title>', s)
    if t and english(t.group(1)):
        out.insert(0, "[TITLE] " + t.group(1))

    print("%d still English in %s" % (len(out), path))
    for x in out:
        print(repr(x))


main(sys.argv[1])
