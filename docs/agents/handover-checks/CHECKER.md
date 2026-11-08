# Handover check: CHECKER successor 22 (Opus 5.5), written 2026-11-08 09:42Z (date -u)
Predecessor: successor 21 (Resume point 09:22Z and HANDOVER 03:51Z at the top of notes/CHECKER.md, pushed in c8a2bc05). This file is
overwritten per the brief; earlier successors' checks are in git history of this path and in notes/CHECKER.md. Every answer is
measured from the repository (commands named), not recalled.

### 1. Branch, head, ahead/behind trunk
- Branch claude/checker (`git branch --show-current`). HEAD = local ref = origin/claude/checker = `git ls-remote origin claude/checker`
  = c8a2bc05. Trap check run first (fetch --unshallow, fetch both branches, checkout, merge --ff-only): already up to date, no stale ref.
- Against trunk claude/vibrant-johnson-nxvvxo @ 3906d411 (`git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo`):
  3 ahead (0942e8be C135 main, fa8add12 handover, c8a2bc05 resume point), 839 behind (238 first-parent); merge-base d38a2194.

### 2. Open work and the next step of each
- C135 = R121 (P-N5-ASC, L-NEW): main 0942e8be FAIL E-1..E-4 (L-3 0012d671, UPDATE f545cba7). The THIRD fill is on trunk:
  3906d411:docs/agents/R121-draft.md sha1 1fa73568e67187c08ede98afcc2d31eeb16c2e39 (measured); line L-5 at claude/l-new e28e962d,
  docs/new/P-N5-ASC-line-L5.txt, sha1 fe4d3f902b6afde93384ebf625fa9bebcea0e1d0, 5,192 B (measured). e28e962d is NOT an ancestor of
  trunk 3906d411 (`git merge-base --is-ancestor`): to be named in Add. 1 as a merge landing needs, unless the Lead merges it first.
  NEXT: C135 Add. 1 = predecessor's to-do (1)-(5): premise ancestry; cmp L-3 with §5, then L-3 → L-4 → L-5 in meaning (R5, R-A, R-I)
  with the referees' byte tests (REFEREE 29 §F 52e6e77b / §F add. 1 055758ba / §G d17b305e; REFEREE-2 33 Add. 5 05eb5181 / Add. 6
  388530af); rule N-H (HUB-ASC(B): «hub», «value», «forest», «chain» undefined in the line; C135 E-4 rule) and N-S (C134 N-S); title,
  block, UPDATE by token diff, word diff vs the second fill, stale phrases, box 193 blocks from git archive, quote sweep, landing
  simulation after R120. Then Add. 2 (rebuild from parent + checked block; Add. 1 premise commits ancestors of the landing) + CI.
- Next: C136 = R122 (P-ACYC, second fill docs/agents/R122-draft.md sha1 2cd7cfd0 on L-4 85bb221f; flags G-4, N-S). Later R123
  (P-N5-QUIET), P-N5-END, P-N5-CHAIN.

### 3. GAPS rows owned
None. `git show origin/claude/vibrant-johnson-nxvvxo:docs/GAPS.md | grep -n -i checker`: l. 6 (GAP-A, owner L-ALG), l. 11 (G-N5-TIME,
owner L-NEW), l. 16 (G-N5-TERM, owner L-NEW, closed); CHECKER appears only as landing checker / re-runner in other lanes' rows.

### 4. Three owner rulings, verbatim, with status (trunk docs/DECISIONS-INDEX.md)
- D1 (DECISIONS.md l. 7-8; index l. 5 «active»): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every
  such claim, including the fleet's own, as wrong until it passes the gauntlet below.» and «Never downgrade the referee to save money.»
- D18 (DECISIONS.md l. 333; index l. 32 «active»): «Focus on N5 and work toward proving it. Explore novel approaches, especially by
  connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions
  where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and
  open problems.»
- D20 (index l. 42 «active»): «We have reset the weekly usage, so we can again work faster no?» (Lead reading L48: full pace.)

### 5. One trap and the check that prevents it
Stale / shallow clone with a stale local branch ref (bit successors 19-21; not this time). Check: fetch --unshallow, fetch both
branches, checkout + ff-only, then compare `git branch --show-current`, HEAD and `git ls-remote origin claude/checker` before any work
and again before push.sh; `git cat-file -e` on every SHA a brief cites (e28e962d needed `git fetch origin claude/l-new` first). Also:
Oink is not built in a fresh container: scripts/setup_oink.sh started 09:42Z, before the first push.sh, or the smoke step is NOT RUN.
