# -*- coding: utf-8 -*-
"""Check the site before a push.

    python tools/check_site.py

1. The nav in every root page is up to date (tools/build_nav.py --check).
2. Every session_NN/session_NN.qmd has a rendered session_NN.html next to it.
3. Every local href and src in the root pages and the rendered decks resolves
   to a file in the repository.

External links (http, https, mailto) are not tested.
"""
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.found = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name in ("href", "src") and value:
                self.found.append(value)


def local_targets(html_path):
    parser = Links()
    parser.feed(html_path.read_text(encoding="utf-8", errors="replace"))
    for value in parser.found:
        parts = urlparse(value)
        if parts.scheme or parts.netloc or not parts.path:
            continue
        yield value, (html_path.parent / unquote(parts.path)).resolve()


def main():
    problems = []

    nav = subprocess.run([sys.executable, str(ROOT / "tools" / "build_nav.py"), "--check"],
                         capture_output=True, text=True)
    if nav.returncode != 0:
        problems.append(nav.stdout.strip())

    pages = sorted(ROOT.glob("*.html"))
    for qmd in sorted(ROOT.glob("session_*/session_*.qmd")):
        html = qmd.with_suffix(".html")
        if not html.exists():
            problems.append(f"{qmd.relative_to(ROOT)}: not rendered")
        else:
            pages.append(html)

    checked = 0
    for page in pages:
        for value, target in local_targets(page):
            checked += 1
            if not target.exists():
                problems.append(f"{page.relative_to(ROOT)}: broken link {value}")

    for problem in problems:
        print(problem)
    print(f"{len(pages)} pages, {checked} local links checked, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
