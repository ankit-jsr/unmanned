# 007: Repos on personal account, not an organisation

**Status:** Decided, 2026-11-10
**Supersedes:** [005](2026-11-10-005-public-repo-two-repos.md)

## Context

Decision 005 placed both repos under a GitHub organisation (`unmanned-hq`) on the assumption
that keeping company assets separate from the investor's personal identity was worth the extra
setup cost. In practice, the investor's personal GitHub account was already set up and
ready; creating and managing an organisation adds friction with no near-term benefit for a
pre-revenue company.

## Options

| Option | Pros | Cons |
| --- | --- | --- |
| Investor's personal account | Zero extra setup; works immediately; free | Company identity tied to investor identity; migration needed if sold |
| GitHub organisation | Cleaner separation; easier to transfer ownership | Extra setup; no meaningful benefit pre-revenue |

## Decision

- Both `unmanned` (public) and `unmanned-kits` (private) live under the investor's personal GitHub account, not an org.
- URLs updated: `https://github.com/ankit-jsr/unmanned` and `https://github.com/ankit-jsr/unmanned-kits`.
- If the company reaches revenue and the investor wants to separate identities, a migration to
  an organisation is straightforward: a GitHub org transfer preserves all issues, PRs, and history.
- `company/facts.csv` key `repo_url` updated accordingly.

## Kill criteria

Migrate to an org if the investor explicitly requests it, or if a paying customer objects to
the personal-account URL.
