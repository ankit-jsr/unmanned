# Free skills

Free Claude skills published by Unmanned under the MIT licence. Each one ships with its eval
cases and latest results, so you can see how well it works before you install it.

| Skill | For | Pass rate | Status |
| --- | --- | --- | --- |
| [grant-fit-screener](grant-fit-screener/) | Nonprofit grant writers | 31/31 checks (2026-11-11) | Published |
| [reviewer-response](reviewer-response/) | Academic researchers | 33/33 checks (2026-11-11) | Published; being re-evaluated (see below) |
| [newsletter-issue-planner](newsletter-issue-planner/) | Newsletter operators | 32/32 checks (2026-11-11) | Published |

**Known issue, reviewer-response:** in eval case c1, the skill added methods details the
author never supplied (matching tolerances, a supplementary table), and the grader passed it.
The skill is being tightened to use placeholders for anything the author hasn't given, and
the eval will be re-run. Until then, check every specific in its output against what you
actually changed.

To install a skill, copy its folder into your project's `.claude/skills/` directory.

Start a new one from [`_template/`](_template/).
