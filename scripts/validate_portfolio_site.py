#!/usr/bin/env python3
"""Dependency-free structural checks for the static portfolio landing page."""
from html.parser import HTMLParser
from pathlib import Path
import re
import sys

SITE = Path("index.html")

class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.fragments = []
        self.external_links = []
        self.buttons = 0
        self.main_count = 0
        self.title_seen = False
        self.script_count = 0
        self.errors = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            if attrs["id"] in self.ids:
                self.errors.append("duplicate id: " + attrs["id"])
            self.ids.add(attrs["id"])
        if tag == "a":
            href = attrs.get("href", "")
            if href.startswith("#"):
                self.fragments.append(href[1:])
            elif href.startswith("https://"):
                self.external_links.append(href)
            elif href and not href.startswith(("mailto:", "tel:")):
                self.errors.append("unsupported link target: " + href)
        if tag == "button":
            self.buttons += 1
        if tag == "main":
            self.main_count += 1
        if tag == "script":
            self.script_count += 1

    def handle_endtag(self, tag):
        pass

def main():
    if not SITE.is_file():
        raise SystemExit("FAIL: index.html not found")
    source = SITE.read_text(encoding="utf-8")
    parser = SiteParser()
    parser.feed(source)
    parser.close()
    checks = {
        "HTML5 doctype": source.lstrip().lower().startswith("<!doctype html>"),
        "English document language": bool(re.search(r'<html[^>]+lang="en"', source)),
        "responsive viewport": 'name="viewport"' in source,
        "page title": bool(re.search(r"<title>[^<]+</title>", source)),
        "one main landmark": parser.main_count == 1,
        "skip link": bool(re.search(r'class="[^"]*\\bskip\\b[^"]*"[^>]*href="#main"', source)),
        "keyboard focus styling": ":focus-visible" in source,
        "reduced-motion support": "prefers-reduced-motion" in source,
        "interactive demo controls": parser.buttons >= 3,
        "live feedback region": 'aria-live="polite"' in source,
        "local fragment targets exist": all(fragment in parser.ids for fragment in parser.fragments),
        "no duplicate element IDs": not any("duplicate id" in e for e in parser.errors),
        "synthetic-data disclosure": "All practice datasets are clearly identified as synthetic" in source,
        "repository evidence links": "github.com/jaackdoe35-sudo/ai-data-evaluation-portfolio" in source,
        "visible candidate email": "tobepatrickjnr@gmail.com" in source and "mailto:tobepatrickjnr@gmail.com" in source,
        "no placeholder contact copy": "can be added once confirmed" not in source,
    }
    for label, passed in checks.items():
        print(("PASS" if passed else "FAIL") + "  " + label)
    for error in parser.errors:
        print("FAIL  " + error)
    print(f"\n{sum(checks.values())}/{len(checks)} checks passed; {len(parser.external_links)} HTTPS links; {parser.buttons} buttons.")
    if not all(checks.values()) or parser.errors:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
