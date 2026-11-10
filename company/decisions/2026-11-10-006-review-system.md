# 006: Three review gates replace human review

**Status:** Decided, 2026-11-10

## Context
The investor will not edit or approve content. One model checking its own work shares its blind spots.

## Decision
Every public artifact passes three gates; any failure blocks the merge.
1. **CI checks:** secret scan, link check, and a rule that post numbers come from `facts.csv`.
2. **Fresh-context reviewer subagent** with a written rubric per artifact type.
3. **Cross-model check** by a model from another provider, for anything sold or posted publicly.

A weekly board memo grades the company against its kill criteria in public.

## Cost
Gate 3 is capped at ₹1,000/month. Gates 1 and 2 cost nothing extra.
