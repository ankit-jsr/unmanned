#!/usr/bin/env python3
"""Gate 1 content checks. No network, no model.

1. Posts in content/log/ may not contain raw currency amounts; numbers come from
   {{fact:key}} placeholders resolved against company/facts.csv.
2. Every {{fact:key}} placeholder must exist in company/facts.csv.
3. Every relative markdown link in the repo must point to a file or folder that exists.
4. company/ledger.csv and company/metrics.csv must parse with the expected headers.
5. Links in site/ HTML must be relative and point to files that exist. The site is served
   from a subpath (ankit-jsr.github.io/unmanned/), so a link starting with "/" would 404.

Exit code 0 = pass, 1 = fail.
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLACEHOLDER = re.compile(r"\{\{fact:([a-z0-9_]+)\}\}")
CURRENCY = re.compile(r"(₹|\bRs\.?\s?|\bINR\s?|\$)\s?\d")
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
SKIP_DIRS = {".git", "node_modules", ".venv", "content/rendered", "content/articles"}  # articles: links checked in the built site/ HTML

LEDGER_HEADER = ["date", "type", "category", "description", "amount_inr", "counterparty", "evidence"]
METRICS_HEADER = ["week", "date", "substack_subscribers", "github_stars", "waitlist_signups",
                  "preorders", "revenue_inr", "spend_inr"]
FACTS_HEADER = ["key", "value", "source"]


def load_facts(errors):
    path = ROOT / "company" / "facts.csv"
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    if not rows or rows[0] != FACTS_HEADER:
        errors.append(f"company/facts.csv: header must be {FACTS_HEADER}")
        return {}
    return {r[0]: r[1] for r in rows[1:] if r}


def check_csv(rel, header, errors):
    path = ROOT / rel
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    if not rows or rows[0] != header:
        errors.append(f"{rel}: header must be {header}")
        return
    for i, row in enumerate(rows[1:], start=2):
        if row and len(row) != len(header):
            errors.append(f"{rel}:{i}: expected {len(header)} columns, got {len(row)}")


def strip_code(text):
    return re.sub(r"```.*?```", "", text, flags=re.S)


def check_posts(facts, errors):
    for post in sorted((ROOT / "content" / "log").glob("*.md")):
        rel = post.relative_to(ROOT)
        text = strip_code(post.read_text(encoding="utf-8"))
        for key in PLACEHOLDER.findall(text):
            if key not in facts:
                errors.append(f"{rel}: unknown placeholder {{{{fact:{key}}}}}")
        bare = PLACEHOLDER.sub("", text)
        for n, line in enumerate(bare.splitlines(), start=1):
            if CURRENCY.search(line):
                errors.append(f"{rel}:{n}: raw currency amount; use a {{{{fact:key}}}} placeholder")


def skipped(path):
    rel = path.relative_to(ROOT).as_posix()
    return any(rel == d or rel.startswith(d + "/") for d in SKIP_DIRS)


def check_links(errors):
    for md in ROOT.rglob("*.md"):
        if skipped(md):
            continue
        text = strip_code(md.read_text(encoding="utf-8"))
        for target in LINK.findall(text):
            if re.match(r"^(https?:|mailto:|#|\{\{)", target):
                continue
            target = target.split("#")[0]
            if target and not (md.parent / target).exists():
                errors.append(f"{md.relative_to(ROOT)}: broken link -> {target}")


HTML_REF = re.compile(r"""(?:href|src)\s*=\s*["']([^"']+)["']""")


def check_site_links(errors):
    site = ROOT / "site"
    for page in sorted(site.rglob("*.html")):
        rel = page.relative_to(ROOT)
        for target in HTML_REF.findall(page.read_text(encoding="utf-8")):
            if re.match(r"^(https?:|mailto:|#|data:|javascript:)", target):
                continue
            if target.startswith("/"):
                errors.append(f"{rel}: root-relative link {target} breaks under the site's subpath; use a relative link")
                continue
            path = (page.parent / target.split("#")[0].split("?")[0]).resolve()
            if site.resolve() not in path.parents and path != site.resolve():
                errors.append(f"{rel}: link {target} points outside site/, which isn't published")
                continue
            if path.is_dir():
                path = path / "index.html"
            if not path.exists():
                errors.append(f"{rel}: broken link -> {target}")


def main():
    errors = []
    facts = load_facts(errors)
    check_csv("company/ledger.csv", LEDGER_HEADER, errors)
    check_csv("company/metrics.csv", METRICS_HEADER, errors)
    check_posts(facts, errors)
    check_links(errors)
    check_site_links(errors)
    if errors:
        print("Gate 1: FAIL")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("Gate 1: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
