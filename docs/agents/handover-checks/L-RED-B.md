# Handover check: L-RED-B successor 7 (second adversary lane, the AUTHOR lane of the dead-end packet P-N5-EXP; model and effort as in the Lead's brief and roster; D1 / D18 / D22 / D24 / D25 / D26; written 2026-11-13T19:10Z by date -u)
Every answer is measured from the repository (commands named), not recalled. Predecessor: successor 6
(session_01V5yGRYvwUZTkQxfvG8iXBu), handover 69ab92f7905434db7dc22eeb7f07c848220adc0b (notes/L-RED-B.md, «SUCCESSOR 6 HANDOVER»), on
top of 0c8fdf9eaf370cbd2d18d13eb55d91dad3ca905f (fixes entry 6). This session: session_01V5yGRVmUNMkUXGRuVH63B8 (get_session:
model and effort_level as the brief names them; parent session_014FBi6o334DvwT5Uw2kDfoN).
Trap check on entry (17:05Z): `git fetch --unshallow`, fetch, `git merge --ff-only origin/claude/l-red-b` (the clone was 37 commits
behind); `git branch --show-current` -> claude/l-red-b; HEAD = origin = 24f4d436a0fea1f62ae736f20f78ff9e84333a90. Clock skew against
the Date header of a raw.githubusercontent.com response: 0 s (header «Fri, 13 Nov 2026 17:05:02 GMT», local date -u 17:05:02).
Pins at 24f4d436: packet sha1 c0449b17193f19619f33b366096762dfde27d542, fixes file 9dc9179fb08063cd59de25c5d3e16b0f8c693fbd (829
lines), L-1 59c5309377eda882ba436ffe7eb03fbff598c7c8 (5,585 bytes): the brief's values.
EARLY START (Lead's brief): `git ls-remote origin claude/l-red-b` printed 24f4d436 at every check from 17:05Z to 17:31:04Z and
0c8fdf9eaf370cbd2d18d13eb55d91dad3ca905f at 17:32:34Z (a background loop's own line: «l-red-b moved to
0c8fdf9eaf370cbd2d18d13eb55d91dad3ca905f at 2026-11-13T17:33:25Z»); then `git merge --ff-only`. Nothing was committed before
that; drafts lived in the session scratchpad. The fleet's 5-hour limit stopped this session's turn from about 17:37Z to 19:04Z (Lead
19:03Z, reading L52: a pause); on waking, origin was at 69ab92f7 (successor 6's handover note) and was fast-forwarded again.
rate_limit_info (get_session, 17:05Z and 19:10Z): isUsingOverage false, rateLimitType seven_day, status allowed_warning, resetsAt
1795035600. Context at 19:10Z: 442,891 tokens (the park line is about 450k).

## 1. Branch, head, distance to trunk
- `git branch --show-current` -> claude/l-red-b. Before this session's commit: `git rev-parse HEAD origin/claude/l-red-b` -> both
  69ab92f7905434db7dc22eeb7f07c848220adc0b.
- Trunk: `git rev-parse origin/claude/vibrant-johnson-nxvvxo` -> 31d94df061ebe98525b47a67a5771488cdac9c50 (fetched 19:04Z).
  `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` -> 43 ahead, 197 behind; merge-base
  471aba45214c9b4009332ef1d498dd5dbc42f3cb. Trunk is not merged into this branch; other lanes' files are read with `git show`.
- Read-only refs fetched: claude/referee 78515253a74a353a829b435d53f4987a8552989a (R-P-N5-EXP.md with stage 4, sha1 0ec7d605…, 542
  lines), claude/referee-2 f17a2708de653b306eaedf878f6120d2d0b31e06 (Addendum 2; file sha1 7128d83e…, 549 lines) and e643672d
  (Addendum 3), trunk docs/RESULTS.md (sha1 eecbd798b81ad431d1b753f5a7f92f3c63e56da1; R117's title line is its l. 13362).
- Files I own: docs/red-b/, experiments/red-b/, notes/L-RED-B.md, this file.

## 2. Open work and the next step of each
- The packet P-N5-EXP is FROZEN (docs/red-b/P-N5-EXP.md at 350d84eb): never edited; changes are append-only entries of
  docs/red-b/P-N5-EXP-fixes.md (entries 1-6 on origin at 0c8fdf9e, 881 lines, sha1 43a941eb6249f0278e342438f92293b7f7a4449e).
- WORK 1, line L-2 (this commit): docs/red-b/P-N5-EXP-line-L2.txt = L-1 with five named replacements by experiments/red-b/b6line.py
  (L-a the units' shape, L-b R117's premises in its title line's words, L-c the L41 scope tail with both referees' signature
  sentences, L-d N5 at k = 13 from entry 6); nothing else changed. Next step: the Lead diffs it; a line item comes back as L-3,
  again by script.
- WORK 2, fixes entry 7 (this commit): REFEREE-2 42's F-1 (range of (R3): t − 1 ≤ τ < last, with a direct test), F-2 (which frozen
  lines stay in force), F-3 (5.1's parenthesis), F-4 (run_b6fix.sh repaired and tested; eleven outputs byte-equal), F-5 (label);
  REFEREE 36's stage 4 has no new item. Guards in check.sh. Next step: wait; referee or CHECKER items on L-2 or entry 7 come
  through the Lead and are answered in an entry 8, append-only. No new experiments.
- Nothing runs: `pgrep -af "push.sh|verify.sh"` -> nothing before this commit's push.

## 3. docs/GAPS.md rows
- Owned: none. Trunk 31d94df0 docs/GAPS.md: `grep -c L-RED-B` -> 1 (line 11, row G-N5-TIME, owner «L-NEW (L-LIT T22; referees
  later)», status open; its text cites this lane, the owner column does not name it).
- Worked against: G-N5-TIME. Corollary EXP-N5 answers it NO for N5 from S3, PROVED-CONDITIONAL on R117's Theorem REACH3 as landed;
  the row is the Lead's to change after both signatures and CHECKER.

## 4. Owner rulings, verbatim (trunk 31d94df0 docs/DECISIONS.md; status from docs/DECISIONS-INDEX.md at the same commit)
- D1 (DECISIONS.md line 7; index line 5, status **active**):
  > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
  A kill of the fleet's candidate is itself a claim held to that standard: two referee signatures and CHECKER before it lands.
- D18 (DECISIONS.md line 333; index line 32, status **active**):
  > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
- D25 (DECISIONS.md line 541; index line 57, status **active**): «So put everything into trying solving it today»
- Also binding: D22 (line 491; index line 47, active): owner (verbatim) «yes» to the L-RED-B lane; D24 (line 538; index line 56,
  active) «do xhigh»; D26 (line 567; index line 60, active) «I hit my usage limit while you were working, but it has reset now.
  Please continue from where you left off.» Lead readings used today: L41 (index line 34, active: a referee-originated proof needs
  its author's signature and the other referee's independent one, both quoted, the scope tail says so) and L43 (index line 36,
  active: «DEAD» needs a refereed proof or an instance beyond an explicit bound; every measured run here is below n²).

## 5. One trap that bit this lane, and the check that prevents it
- Trap (found today by REFEREE-2 42, its F-4, and worse than reported): a runner that exits 0 when its stage fails.
  run_b6fix.sh at 24f4d436 printed «done», exited 0 and left an EMPTY output file under a failing python3; the two-line repair
  used for run_b6b.sh (an ERR trap and `exit $fail`) still leaves the empty file and, in a stage whose commands share one subshell,
  misses a failing command that is not the last (exit 0, a short output file). Check: every stage command is tested where it runs
  and writes through a temporary file; experiments/red-b/b6fixtest.sh tests seven failure paths and three controls and compares
  the eleven outputs with their pins; check.sh runs one stage with a failing interpreter (exit 1, no file left) on every verify.
  The comparison of record is of FILES against pins, never of an exit code.
- Second trap (successors 2-7): a commit made, or a SHA quoted, before the previous push is on origin. Check: `git ls-remote origin
  claude/l-red-b` before any commit after an EARLY START and after every push (a 503 can hide behind exit 0); pushes are tracked
  tasks with a 2-hour timeout, output redirected, exit code echoed, `pgrep -f "bash scripts/push.sh"` first; never a commit while
  a push runs.
