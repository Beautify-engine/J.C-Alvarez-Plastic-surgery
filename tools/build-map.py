#!/usr/bin/env python3
"""Render a locator map as clean SVG from OpenStreetMap geometry.

Why not a Google Maps iframe: it is ~700kb of third-party JavaScript, it sets cookies
(so it drags a consent banner onto the page), it cannot be graded to match the site, and
it is the single heaviest thing that could land on a page whose Lighthouse budget is
already spent. This draws the same streets as paths in the site's line register, weighs
about 20kb, makes zero network requests at runtime, and inherits currentColor so one file
works on the ink ground and the paper ground.

Input:  /tmp/osm.json — an Overpass `out geom;` response. Refetch with:

    curl -s -H 'User-Agent: jc-alvarez-site-build/1.0' \
      --data-urlencode 'data=[out:json][timeout:60];
        ( way(around:520,LAT,LON)["highway"~"^(motorway|trunk|primary|secondary|tertiary|residential|unclassified|motorway_link|trunk_link|primary_link)$"];
          way(around:200,LAT,LON)["building"]; );
        out geom;' https://overpass-api.de/api/interpreter -o /tmp/osm.json

Output: src/public/img/map/locator.svg

Data © OpenStreetMap contributors, ODbL. Attribution is required and is rendered as
visible text on the page, not just in this comment.
"""
import json, math, os, sys

LAT, LON = 25.7616349, -80.3318236      # 8400 SW 8th St, Miami FL 33144
RADIUS_M = 430                           # drawn extent; fetch a little wider than this
SIZE = 960                               # viewBox units, square
OUT = "src/public/img/map/locator.svg"

# stroke weight by road class — a hierarchy you can read at a glance without labels
WEIGHT = {
    "motorway": 5.0, "trunk": 5.0, "primary": 4.2, "secondary": 3.2,
    "tertiary": 2.4, "residential": 1.3, "unclassified": 1.3,
    "motorway_link": 2.4, "trunk_link": 2.4, "primary_link": 2.4,
}
OPACITY = {
    "motorway": .95, "trunk": .95, "primary": .9, "secondary": .7,
    "tertiary": .6, "residential": .42, "unclassified": .42,
    "motorway_link": .55, "trunk_link": .55, "primary_link": .55,
}

M_PER_DEG_LAT = 111320.0
M_PER_DEG_LON = 111320.0 * math.cos(math.radians(LAT))
SCALE = (SIZE / 2) / RADIUS_M           # viewBox units per metre


def project(lat, lon):
    """Equirectangular about the centre. At a 430m radius the error is far below a pixel."""
    return (SIZE / 2 + (lon - LON) * M_PER_DEG_LON * SCALE,
            SIZE / 2 - (lat - LAT) * M_PER_DEG_LAT * SCALE)


def clip(points):
    """Split a way into runs that stay inside the frame, so nothing dangles off-canvas."""
    pad = 12
    runs, cur = [], []
    for x, y in points:
        if -pad <= x <= SIZE + pad and -pad <= y <= SIZE + pad:
            cur.append((x, y))
        else:
            if len(cur) > 1:
                runs.append(cur)
            cur = []
    if len(cur) > 1:
        runs.append(cur)
    return runs


def path_d(points, close=False):
    d = "M%.1f,%.1f" % points[0] + "".join("L%.1f,%.1f" % p for p in points[1:])
    return d + "Z" if close else d


def main():
    if not os.path.exists("/tmp/osm.json"):
        sys.exit("no /tmp/osm.json — refetch from Overpass, see the docstring")
    els = json.load(open("/tmp/osm.json"))["elements"]

    roads, buildings, practice = [], [], None
    for e in els:
        t = e.get("tags", {})
        g = e.get("geometry") or []
        if len(g) < 2:
            continue
        pts = [project(p["lat"], p["lon"]) for p in g]
        if "highway" in t:
            roads.append((t["highway"], t.get("name", ""), pts))
        elif "building" in t:
            cy = sum(p["lat"] for p in g) / len(g)
            cx = sum(p["lon"] for p in g) / len(g)
            dist = math.hypot((cy - LAT) * M_PER_DEG_LAT, (cx - LON) * M_PER_DEG_LON)
            if dist <= 12 and practice is None:
                practice = pts
            else:
                buildings.append(pts)

    layers = []

    # buildings — texture only, never competing with the streets
    b = [path_d(r, True) for pts in buildings for r in clip(pts)]
    if b:
        layers.append('  <g opacity=".22" stroke-width="1"><path d="%s"/></g>' % " ".join(b))

    # roads, light classes first so the arterials draw over them
    order = sorted(roads, key=lambda r: WEIGHT.get(r[0], 1))
    by_class = {}
    for cls, _name, pts in order:
        for run in clip(pts):
            by_class.setdefault(cls, []).append(path_d(run))
    for cls in sorted(by_class, key=lambda c: WEIGHT.get(c, 1)):
        layers.append('  <g stroke-width="%.1f" opacity="%.2f"><path d="%s"/></g>'
                      % (WEIGHT.get(cls, 1.3), OPACITY.get(cls, .3), " ".join(by_class[cls])))

    # the building itself, then the mark on it
    if practice:
        for run in clip(practice):
            layers.append('  <path d="%s" stroke-width="1.6" opacity=".9"/>' % path_d(run, True))
    c = SIZE / 2
    layers.append(
        '  <g class="locator__pin">\n'
        '    <circle cx="%.0f" cy="%.0f" r="34" stroke-width="1.2" opacity=".45"/>\n'
        '    <circle cx="%.0f" cy="%.0f" r="7" stroke-width="2.4"/>\n'
        '    <path d="M%.0f,%.0f L%.0f,%.0f M%.0f,%.0f L%.0f,%.0f" stroke-width="1.2" opacity=".55"/>\n'
        '  </g>' % (c, c, c, c, c, c - 52, c, c - 22, c, c + 22, c, c + 52))

    # The arterial gets a label, seated just above its own carriageways rather than at a
    # guessed fraction of the frame — the first version floated mid-block and read as
    # labelling a side street. Offset left so it clears the pin ring. Everything else is
    # oriented by the compass and by the cross-streets named in the copy beside the map.
    ARTERIAL_OFFSET_N = 47          # metres from the practice to the SW 8th St centreline
    road_y = SIZE / 2 - ARTERIAL_OFFSET_N * SCALE
    layers.append(
        '  <g class="locator__lbl" stroke="none" fill="currentColor">\n'
        '    <text x="%d" y="%d" text-anchor="middle">SW 8TH ST &#183; US 41</text>\n'
        '  </g>' % (int(SIZE * 0.29), int(road_y - 16)))
    layers.append(
        '  <g class="locator__n" opacity=".6">\n'
        '    <path d="M%d,%d L%d,%d M%d,%d L%d,%d L%d,%d" stroke-width="1.6"/>\n'
        '    <text class="locator__lbl" stroke="none" fill="currentColor" '
        'x="%d" y="%d" text-anchor="middle">N</text>\n'
        '  </g>' % (SIZE - 84, SIZE - 52, SIZE - 84, SIZE - 92,
                    SIZE - 90, SIZE - 86, SIZE - 84, SIZE - 94, SIZE - 78, SIZE - 86,
                    SIZE - 84, SIZE - 104))

    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" fill="none"\n'
        '     stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"\n'
        '     role="img" aria-label="Street map of the block around 8400 SW 8th Street, Miami">\n'
        '%s\n</svg>\n' % (SIZE, SIZE, "\n".join(layers))
    )
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(svg)
    print("%s  %.1f kb  roads=%d buildings=%d practice=%s"
          % (OUT, len(svg) / 1024, len(roads), len(buildings), bool(practice)))


if __name__ == "__main__":
    main()
