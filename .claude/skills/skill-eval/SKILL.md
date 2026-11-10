---
name: skill-eval
description: How to build and test a free or paid Claude skill for Unmanned, including its eval cases. Use whenever creating or changing anything in products/ or in the unmanned-kits repo, or when asked whether a skill is ready to publish or sell.
---

# Building and evaluating a skill

## Structure

Copy `products/_template/`. A skill folder holds `SKILL.md`, `evals/cases.json`, and
`evals/results-YYYY-MM-DD.json`.

## Eval cases

- At least 5 cases, at least 2 of them hard or adversarial (missing input, messy input,
  a request the skill should refuse or redirect).
- Each case: `id`, `prompt`, `input_files` (optional), and `checks`: a list of plain-language
  assertions an independent grader can mark true or false.

## Running evals

For each case, run a fresh subagent with only the skill and the prompt. Then run a second,
separate subagent as the grader, giving it the output and the checks. Never grade your own run.
Record pass/fail per check in `evals/results-YYYY-MM-DD.json` with a summary pass rate.

## Ready to ship

- Free skill: pass rate at least 90%, gate 2 PASS.
- Paid kit: pass rate at least 90% on Claude and on the gate 3 model, gate 2 and gate 3 PASS.
