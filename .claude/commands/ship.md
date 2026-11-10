Ship this week's work.

1. Follow the session-start protocol in CLAUDE.md.
2. Pick the highest-value unfinished objective from the latest board memo and build it on a branch.
3. If something real happened this week, draft the Substack post in `content/log/NNN-slug.md`
   from the decision log and board memo. Use `{{fact:key}}` for every number.
4. Run `/review` on the branch.
5. If all gates pass, merge with `gh pr merge --squash`.
6. If a post merged, run `python3 scripts/render_post.py content/log/<file>` and open a
   `needs-investor` issue: "Paste content/rendered/<file> into Substack (5 min)".
7. Follow the session-end protocol.
