# 009: Publish on gates 1 and 2; gate 3 stops blocking

**Status:** Decided, 2026-11-13, on the investor's instruction. Amends [006](2026-11-10-006-review-system.md).

## Context
After three days the company had published nothing and earned nothing. A parallel business run
by another model had a website, three articles and daily LinkedIn posts. The investor said the
measure is money made, and told me to publish without waiting for approvals. Two things slowed us
down. Gate 3 blocks publishing until an API key exists. And gate 2 ran for up to five rounds on
copy wording.

## Options
1. Keep all three gates blocking and wait for the key.
2. Publish on gates 1 and 2; run gate 3 after the fact once the key exists.
3. Drop review entirely.

## Decision
Option 2.
- **Gate 1 (CI)** still blocks every merge. It costs nothing and catches broken links, secrets,
  raw currency in posts and stale article builds.
- **Gate 2 (reviewer subagent)** runs one round. It blocks only on false claims about the company
  or a product, invented data, personal data, or safety issues. Style and wording notes don't block.
- **Gate 3 (cross-model)** runs on everything already published once the key exists. Anything it
  finds gets fixed in place.
- The site deploys on every merge to `main`.

What stays non-negotiable: no fabricated numbers or traction, AI authorship disclosed, no
personal data, nothing posted under the investor's identity.

`CLAUDE.md` section 4 still describes the old blocking gates. This decision overrides it until
the investor updates that file.

## Kill criteria
If a published claim turns out false, return to blocking gate 2 for that kind of content.
