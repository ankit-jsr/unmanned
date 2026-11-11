# Free skills

Free Claude skills published by Unmanned under the MIT licence. Each one ships with its eval
cases and latest results, so you can see how well it works before you install it.

| Skill | For | Pass rate | Status |
| --- | --- | --- | --- |
| [grant-fit-screener](grant-fit-screener/) | Nonprofit grant writers | 31/31 checks (2026-11-11) | Published |
| [reviewer-response](reviewer-response/) | Academic researchers | 39/40 checks (2026-11-11, re-run) | Published (see note) |
| [newsletter-issue-planner](newsletter-issue-planner/) | Newsletter operators | 32/32 checks (2026-11-11) | Published |

**Note, reviewer-response:** the first eval run scored 33/33, but one case passed an output that
invented methods details the author never supplied. The skill is now instructed to write any decision or
detail you haven't given as a `[placeholder]`. In the re-run it scored 39/40; its one failure was
writing a change as already made inside a conditional branch, recorded in the results file. Still check every specific in its output against what you actually changed.

To install a skill, copy its folder into your project's `.claude/skills/` directory.

Start a new one from [`_template/`](_template/).
