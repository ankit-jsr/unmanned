# Session log

## 2026-11-10: Day 0
- **Objective:** bootstrap the company.
- **Shipped:** repo structure, CLAUDE.md, three-gate review system, strategy, decisions 001 to 006,
  market scan, Substack post 1 draft.
- **Blocked:** payments provider and reviewer API key, both with the investor.

## 2026-11-10: Day 0, setup
- **Objective:** Wire up personal-account repo, fix infrastructure, review post 001.
- **Shipped:** Decision 007 (personal account supersedes org), facts.csv repo_url updated, pre-commit hook installed locally, decisions 005+007 rubric-compliant, post 001 passes gates 1 and 2 (gate 3 pending).
- **Blocked:** `gh` CLI not authenticated — cannot create `needs-investor` label/issues, branch protection, or push unmanned-kits. Gate 3 skipped (no `REVIEWER_API_KEY`). Both need the investor.

## 2026-11-10: Day 0, housekeeping
- **Objective:** remove the investor's personal name from the repo's files, at his request.
  Earlier commits still contain it; he chose to keep the history.
- **Shipped:** "the investor" replaces the name in every file (it remains in the repo URL); label renamed to `needs-investor`.
  `repo_url` now points at the repo's real home; decision 003 states the correct check count.
- **Blocked:** label, first two issues and branch protection still need setting up on GitHub.

## 2026-11-11: Day 1
- **Objective:** Complete repo setup and ship three free skills for the vertical sprint.
- **Shipped:** gh auth; `needs-investor` label; issues #1 (reviewer key) + #2 (payments); branch protection on main; pre-commit hook; unmanned-kits pushed; three free skills merged (grant-fit-screener, reviewer-response, newsletter-issue-planner) — all 100% evals, gates 1+2 PASS (PRs #3, #5).
- **Blocked:** Gate 3 skipped (no `REVIEWER_API_KEY`, issue #1). Pre-order page blocked on payments provider (issue #2).

## 2026-11-11: Day 1, landing pages
- **Objective:** make the landing pages correct and deployable, and make the investor's asks
  work exactly as written.
- **Shipped:** decision 008 (GitHub Pages via Actions, Tally waitlists); Pages deploy workflow;
  relative links (root links would 404 under the site's subpath); Tally embed with an
  "opens soon" fallback; removed unsourced statistics and promises the strategy doesn't make;
  Gate 1 now checks links in `site/`. Corrected issue #6 (Pages source) and issue #1 (provider name).
  Gate 2 on the pages found that the reviewer-response skill invented methods details in its own
  eval. PR #8 fixed the skill to use placeholders and re-ran its eval honestly: 39/40, down from
  a wrong 33/33.
- **Blocked:** Tally form IDs and turning Pages on (issue #6); pre-order link (issue #2);
  gate 3 (issue #1).
- **Next:** reviewer-response revision 2 (no changes written as made inside conditional
  branches), then a fresh eval run; recheck the other two skills' evals for the same blind spot.

## 2026-11-13: Day 3, ship
- **Objective:** publish. The investor flagged that a parallel business had a site, three articles
  and daily LinkedIn posts while we had published nothing. Money made is the measure.
- **Shipped:** decision 009 (publish on gates 1 and 2; gate 3 stops blocking; gate 2 is one
  round). Three articles, one per profession, built from `content/articles/` by
  `scripts/build_articles.py` (CI checks the build is current). Articles index, links from the
  home and profession pages. Pages deploys on every merge again. LinkedIn week 1 drafted in
  `content/linkedin/week-1.md` for a company page.
- **Lesson:** five review rounds on landing-page copy and three eval re-runs cost two days with
  nothing published. Catching the invented skill output was worth it; polishing the copy wasn't.
- **Blocked:** Pages toggle, Tally IDs, payments, Substack (investor, in progress).
