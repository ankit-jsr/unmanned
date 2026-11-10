Run the three review gates on the current branch.

1. **Gate 1:** `python3 scripts/check_content.py`. Fix anything it reports.
2. **Gate 2:** run the `reviewer` subagent on every changed file
   (`git diff --name-only main...HEAD`). Fix every BLOCKING item and re-run until PASS.
3. **Gate 3:** for posts, skills and landing pages, run
   `python3 scripts/cross_review.py <file> --type post|skill|decision`.
   Fix blocking items. If `REVIEWER_API_KEY` is missing, note "gate 3 skipped: no key"
   in the PR and do not publish outside the repo.
4. Push and open the PR with `gh pr create`, pasting the gate 2 and gate 3 verdicts into the body.
