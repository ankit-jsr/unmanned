#!/usr/bin/env python3
"""Render a post for Substack: resolve {{fact:key}} placeholders from company/facts.csv
and strip the front-matter block. Output goes to content/rendered/<same name>.

Usage: python3 scripts/render_post.py content/log/001-slug.md
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLACEHOLDER = re.compile(r"\{\{fact:([a-z0-9_]+)\}\}")


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    src = Path(sys.argv[1]).resolve()
    with (ROOT / "company" / "facts.csv").open(newline="", encoding="utf-8") as f:
        facts = {r["key"]: r["value"] for r in csv.DictReader(f)}
    text = src.read_text(encoding="utf-8")
    text = re.sub(r"\A---\n.*?\n---\n+", "", text, flags=re.S)

    def resolve(m):
        key = m.group(1)
        if key not in facts:
            raise SystemExit(f"unknown placeholder: {key}")
        return facts[key]

    out = PLACEHOLDER.sub(resolve, text)
    dest = ROOT / "content" / "rendered" / src.name
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(out, encoding="utf-8")
    print(f"rendered -> {dest.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
