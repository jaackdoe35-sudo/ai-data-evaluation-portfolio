#!/usr/bin/env python3
"""Dependency-free structural checks for the recruiter-facing static portfolio."""
from html.parser import HTMLParser
from pathlib import Path
import re

class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.fragments = []
        self.https_links = []
        self.buttons = 0
        self.main_count = 0
        self.errors = []
        self.skip_link = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        ident = attrs.get("id")
        if ident:
            if ident in self.ids:
                self.errors.append("duplicate id: " + ident)
            self.ids.add(ident)
        if tag == "a":
            href = attrs.get("href", "")
            if href.startswith("#"):
                self.fragments.append(href[1:])
            elif href.startswith("https://"):
                self.https_links.append(href)
            elif href and not href.startswith(("mailto:", "tel:")):
                self.errors.append("unsupported link target: " + href)
            if "skip" in attrs.get("class", "").split() and href == "#main":
                self.skip_link = True
        if tag == "button":
            self.buttons += 1
        if tag == "main":
            self.main_count += 1

def main():
    path = Path("index.html")
    if not path.is_file():
        raise SystemExit("FAIL: index.html not found")
    source = path.read_text(encoding="utf-8")
    parser = SiteParser()
    parser.feed(source)
    parser.close()
    checks = {
        "HTML5 doctype": source.lstrip().lower().startswith("<!doctype html>"),
        "English document language": bool(re.search(r'<html[^>]+lang="en"', source)),
        "responsive viewport": 'name="viewport"' in source,
        "descriptive title": bool(re.search(r"<title>[^<]+</title>", source)),
        "one main landmark": parser.main_count == 1,
        "skip link targets main": parser.skip_link and "main" in parser.ids,
        "keyboard focus styling": ":focus-visible" in source,
        "reduced-motion support": "prefers-reduced-motion" in source,
        "three interactive demo choices": parser.buttons >= 3,
        "live feedback region": 'aria-live="polite"' in source,
        "all local fragment links resolve": all(x in parser.ids for x in parser.fragments),
        "no duplicate IDs": not any("duplicate id" in e for e in parser.errors),
        "synthetic practice disclosure": "synthetic" in source.lower() and "self-directed" in source.lower(),
        "repository evidence links": "github.com/jaackdoe35-sudo/ai-data-evaluation-portfolio" in source,
        "visible candidate email": "tobepatrickjnr@gmail.com" in source and "mailto:tobepatrickjnr@gmail.com" in source,
        "no placeholder contact copy": "can be added once confirmed" not in source,
    }
    for label, passed in checks.items():
        print(("PASS" if passed else "FAIL") + "  " + label)
    for error in parser.errors:
        print("FAIL  " + error)
    print(f"\\n{sum(checks.values())}/{len(checks)} checks passed; {len(parser.https_links)} HTTPS links; {parser.buttons} buttons.")
    if not all(checks.values()) or parser.errors:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
