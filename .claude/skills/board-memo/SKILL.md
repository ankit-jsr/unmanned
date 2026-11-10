---
name: board-memo
description: How to write Unmanned's weekly board memo. Use every Monday, whenever /standup runs, or whenever writing anything in company/board/, even if only a partial update.
---

# Board memo

The memo is a public, honest scorecard. Its reader is a sceptical investor with five minutes.

## Format

File: `company/board/YYYY-Www.md` (ISO week).

1. **One-line verdict**: on track, off track, or killed, with the single number that decides it.
2. **Kill criteria table**: criterion | target | actual | status. Actuals from `company/metrics.csv`.
3. **Shipped**: bullets, each linking a commit or PR.
4. **Decisions**: links to `company/decisions/` files made this week.
5. **Next week**: at most three objectives, each with a measurable done-condition.
6. **Asks**: links to open `needs-investor` issues, each with the minutes it takes.

## Rules

- Zeros are written as zeros. No "early signs", no "momentum".
- If a kill criterion is breached, the memo says so in the first line and links the kill or pivot decision.
- Under 400 words.
