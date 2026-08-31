#!/usr/bin/env python3
"""Threaded static server. python -m http.server is single-threaded and truncates
concurrent responses, which silently corrupts images in a gallery/carousel.

It also resolves CLEAN URLs — /procedures/breast-lift serves procedures/breast-lift.html.
Every internal link on this site is extensionless, which is what Vercel, Netlify and
Cloudflare Pages all do by default. Without this the whole site 404s in a browser while
every automated check still passes, because the tools were requesting *.html directly.
Add a route here only if the host will also serve it that way in production.
"""
import sys, os, posixpath
from urllib.parse import urlsplit
from http.server import SimpleHTTPRequestHandler
from socketserver import ThreadingTCPServer

ROOT = sys.argv[2] if len(sys.argv) > 2 else "src/public"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8787


class H(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)

    def translate_path(self, path):
        p = super().translate_path(path)
        # only extensionless paths are candidates; a real file or directory wins first
        url_path = urlsplit(path).path
        if os.path.exists(p) or posixpath.splitext(url_path)[1]:
            return p
        for candidate in (p + ".html", os.path.join(p, "index.html")):
            if os.path.isfile(candidate):
                return candidate
        return p

    def send_error(self, code, message=None, explain=None):
        # a 404 on a clean URL is almost always a broken internal link, so name it
        if code == 404:
            sys.stderr.write("404  %s\n" % self.path)
        super().send_error(code, message, explain)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def log_message(self, *a):
        pass


ThreadingTCPServer.allow_reuse_address = True
ThreadingTCPServer.daemon_threads = True
print(f"serving {ROOT} on http://localhost:{PORT}  (clean URLs on)")
ThreadingTCPServer(("", PORT), H).serve_forever()
