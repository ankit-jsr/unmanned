# 008: Landing pages on GitHub Pages, waitlists on Tally

**Status:** Decided, 2026-11-11

## Context
The vertical sprint needs one landing page per profession, each with a waitlist, live before
the first kill gate on 2026-12-01. The strategy left hosting and the waitlist tool open. A
static page can't store signups on its own, and the domain stays unbought until a vertical wins.

## Options
| Need | Option | For | Against |
| --- | --- | --- | --- |
| Hosting | GitHub Pages, deployed by Actions from `site/` | Free; no new account; every change goes through the same PR and gates | Lives on a subpath until the domain is bought, so links must be relative |
| Hosting | Netlify or Vercel | Root domain, previews | Another account for the investor; nothing we need yet |
| Waitlist | Tally, one form per profession, embedded | Free; signups counted per profession, which the kill criterion needs | Needs JavaScript; another account |
| Waitlist | Substack signup | One list we already need | Can't tell which profession a signup came from |
| Waitlist | Google Forms | Free | Looks untrustworthy embedded; clumsy styling |

## Decision
- `site/` is published by `.github/workflows/pages.yml` to `https://ankit-jsr.github.io/unmanned/`.
- Each profession page embeds its own Tally form. The three form IDs live in one place,
  `site/assets/waitlist.js`. Until an ID is set, the page says the waitlist opens soon.
- Gate 1 now fails on root-relative or broken links in `site/`.
- The pages promise one email when the paid kit opens for pre-order, and nothing else.
- The $29 pre-order link is added once the payments provider is chosen (issue #2).

## Kill criteria
- If a test signup on any form doesn't arrive in Tally, replace that embed before sending
  traffic to it.
- If Tally's free tier blocks signups or per-profession counts before 2026-12-01, switch the
  waitlist tool in a new decision; signup counts decide the first kill gate.
- When the domain is bought (after a vertical wins the sprint), revisit hosting in a new decision.
