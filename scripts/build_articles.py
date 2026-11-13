#!/usr/bin/env python3
"""Build site/articles/ from content/articles/*.md.

Supports the markdown the articles use: front matter, #/## headings, paragraphs, - and 1. lists,
> blockquotes, | tables |, **bold**, *italic*, `code` and [links](url). No dependencies.

Usage: python3 scripts/build_articles.py          # write the HTML
       python3 scripts/build_articles.py --check  # fail if the HTML is out of date (CI)
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "content" / "articles"
OUT = ROOT / "site" / "articles"


def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![*\w])\*([^*]+)\*(?![*\w])", r"<em>\1</em>", text)
    return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lambda m: f'<a href="{html.escape(m.group(2))}">{m.group(1)}</a>', text)


def blocks(md):
    out, lines, i = [], md.splitlines(), 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("## "):
            out.append(f"<h2>{inline(line[3:])}</h2>"); i += 1; continue
        if line.startswith("# "):
            i += 1; continue  # title comes from front matter
        if line.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(lines[i][1:].strip()); i += 1
            out.append("<blockquote>" + blocks("\n".join(buf)) + "</blockquote>"); continue
        if line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            head = "".join(f"<th>{inline(c)}</th>" for c in rows[0])
            body = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows[1:])
            out.append(f'<div class="table"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'); continue
        m = re.match(r"(\s*)(-|\d+\.)\s+", line)
        if m:
            tag = "ol" if m.group(2)[0].isdigit() else "ul"
            items = []
            while i < len(lines) and (re.match(r"\s*(-|\d+\.)\s+", lines[i]) or (lines[i].startswith("   ") and items)):
                mm = re.match(r"\s*(-|\d+\.)\s+(.*)", lines[i])
                if mm:
                    items.append(mm.group(2))
                else:
                    items[-1] += " " + lines[i].strip()
                i += 1
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>"); continue
        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(r"(#|>|\||\s*(-|\d+\.)\s)", lines[i]):
            buf.append(lines[i].strip()); i += 1
        out.append(f"<p>{inline(' '.join(buf))}</p>")
    return "\n".join(out)


def parse(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    meta = dict(l.split(": ", 1) for l in m.group(1).splitlines())
    return meta, text[m.end():]


PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Unmanned</title>
  <meta name="description" content="{description}">
  <link rel="stylesheet" href="{up}assets/article.css">
</head>
<body>
<nav><div class="container"><a class="logo" href="{up}">Unmanned <span>by Claude</span></a><a class="navlink" href="{up}articles/">Articles</a></div></nav>
<main class="container">
{body}
</main>
<footer><div class="container">Written and maintained by Claude, an AI (Anthropic). Not edited by a human. <a href="https://github.com/ankit-jsr/unmanned">Source</a></div></footer>
</body>
</html>
"""


def render():
    pages, items = {}, []
    for src in sorted(SRC.glob("*.md")):
        meta, md = parse(src)
        slug = src.stem
        body = (f'<article><p class="meta">{html.escape(meta["date"])}</p><h1>{inline(meta["title"])}</h1>\n'
                + blocks(md) + "</article>")
        pages[OUT / slug / "index.html"] = PAGE.format(title=html.escape(meta["title"]), description=html.escape(meta["description"]), up="../../", body=body)
        items.append((meta["date"], slug, meta))
    lis = "".join(
        f'<li><a href="{slug}/"><strong>{inline(m["title"])}</strong></a><br><span>{html.escape(m["description"])}</span></li>'
        for _, slug, m in sorted(items, reverse=True))
    pages[OUT / "index.html"] = PAGE.format(title="Articles", description="Practical guides from Unmanned, written by Claude.", up="../",
                                            body=f'<h1>Articles</h1><p>Practical guides for the professions we build Claude skills for.</p><ul class="list">{lis}</ul>')
    return pages


def main():
    pages = render()
    if "--check" in sys.argv:
        stale = [str(p.relative_to(ROOT)) for p, t in pages.items() if not p.exists() or p.read_text(encoding="utf-8") != t]
        if stale:
            print("Articles out of date; run python3 scripts/build_articles.py:", *stale, sep="\n  ")
            return 1
        print("Articles: up to date")
        return 0
    for p, t in pages.items():
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(t, encoding="utf-8")
    print(f"built {len(pages)} pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
