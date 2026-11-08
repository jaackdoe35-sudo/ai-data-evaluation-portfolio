#!/usr/bin/env python3
"""Dependency-free structural checks for the static portfolio site."""
from html.parser import HTMLParser
from pathlib import Path
import re

class Parser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids=set(); self.fragments=[]; self.main=0; self.buttons=0; self.skip=False; self.errors=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs); ident=a.get("id")
        if ident:
            if ident in self.ids: self.errors.append("duplicate id: "+ident)
            self.ids.add(ident)
        if tag=="main": self.main+=1
        if tag=="button": self.buttons+=1
        if tag=="a":
            href=a.get("href","")
            if href.startswith("#"): self.fragments.append(href[1:])
            if "skip" in a.get("class","").split() and href=="#main": self.skip=True

def main():
    path=Path("index.html")
    if not path.is_file(): raise SystemExit("FAIL: index.html missing")
    source=path.read_text(encoding="utf-8")
    p=Parser(); p.feed(source); p.close()
    checks={
      "HTML5 doctype":source.lstrip().lower().startswith("<!doctype html>"),
      "English language":bool(re.search(r'<html[^>]+lang="en"',source)),
      "responsive viewport":'name="viewport"' in source,
      "descriptive title":bool(re.search(r"<title>[^<]+</title>",source)),
      "one main landmark":p.main==1,
      "skip link targets main":p.skip and "main" in p.ids,
      "keyboard focus style":":focus-visible" in source,
      "reduced motion support":"prefers-reduced-motion" in source,
      "interactive evaluation choices":p.buttons>=3,
      "live feedback region":'aria-live="polite"' in source,
      "local links resolve":all(x in p.ids for x in p.fragments),
      "no duplicate IDs":not p.errors,
      "synthetic practice disclosed":"synthetic" in source.lower() and "self-directed" in source.lower(),
      "governance project linked":"21-ai-governance-and-assurance" in source,
      "security project linked":"20-llm-security-evaluation" in source,
      "email contact visible":"tobepatrickjnr@gmail.com" in source,
      "GitHub source linked":"github.com/jaackdoe35-sudo/ai-data-evaluation-portfolio" in source,
    }
    for name,ok in checks.items(): print(("PASS" if ok else "FAIL")+" "+name)
    for error in p.errors: print("FAIL "+error)
    print(f"{sum(checks.values())}/{len(checks)} checks passed")
    if not all(checks.values()) or p.errors: raise SystemExit(1)
if __name__=="__main__": main()
