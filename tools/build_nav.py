# -*- coding: utf-8 -*-
"""Stamp the shared top bar and footer into every root page.

The top bar lives in assets/nav.html and the footer (name, email, credit) in
assets/footer.html. Each page carries the marker pairs <!-- nav:start -->,
<!-- nav:end --> and <!-- footer:start -->, <!-- footer:end -->; this script
replaces what lies between them and marks the current page in the top bar.

    python tools/build_nav.py           # write
    python tools/build_nav.py --check   # change nothing, exit 1 if out of date

To change the email or name on every page: edit assets/footer.html, then run
this script.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAV = ROOT / "assets" / "nav.html"
FOOTER = ROOT / "assets" / "footer.html"
# PAGES = ["index.html", "syllabus.html", "schedule.html", "literature.html",
#          "setup.html", "downloads.html", "exam_info.html"]
PAGES = ["index.html", "syllabus.html",
         "setup.html", "downloads.html", "resources.html", "exam_info.html"]


def nav_for(page):
    nav = NAV.read_text(encoding="utf-8").rstrip("\n")
    # The brand link also points at index.html, so only mark the list entry.
    return nav.replace(f'<li><a href="{page}">',
                       f'<li><a href="{page}" aria-current="page">')


def replace_between(text, name, block, page):
    start = f"  <!-- {name}:start -->"
    end = f"  <!-- {name}:end -->"
    if start not in text or end not in text:
        raise SystemExit(f"{page}: markers for {name} missing")
    head, rest = text.split(start, 1)
    _, tail = rest.split(end, 1)
    return head + start + "\n  " + block + "\n" + end + tail


def stamped(page):
    old = (ROOT / page).read_text(encoding="utf-8")
    new = replace_between(old, "nav", nav_for(page), page)
    new = replace_between(new, "footer",
                          FOOTER.read_text(encoding="utf-8").rstrip("\n"), page)
    return old, new


def main():
    check = "--check" in sys.argv
    stale = []
    for page in PAGES:
        old, new = stamped(page)
        if new != old:
            stale.append(page)
            if not check:
                (ROOT / page).write_text(new, encoding="utf-8", newline="\n")
    if check:
        if stale:
            print("nav or footer out of date in: " + ", ".join(stale))
            return 1
        print("nav and footer up to date")
        return 0
    print(f"nav and footer stamped into {len(PAGES)} pages ({len(stale)} changed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
