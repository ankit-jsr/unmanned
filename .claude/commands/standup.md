Run the Monday standup.

1. Follow the session-start protocol in CLAUDE.md.
2. Pull the week's numbers into `company/metrics.csv` (Substack subscribers, GitHub stars,
   waitlist signups, pre-orders, revenue, spend). Use `gh` for stars; ask the investor via a
   `needs-investor` issue only for numbers you cannot fetch.
3. Write `company/board/YYYY-Www.md`:
   - Score: each kill criterion from `company/strategy.md`, with the number and on track / off track.
   - What shipped last week, with links to commits or PRs.
   - Decisions made, with links.
   - This week's plan: at most three objectives.
   - Asks: open `needs-investor` issues, each with the time it takes.
4. If a kill criterion is breached, write the decision file the same session.
5. Commit and push on a branch, open a PR, run `/review`, merge if it passes.
