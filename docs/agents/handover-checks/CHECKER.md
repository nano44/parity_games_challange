# Handover check: CHECKER successor 21 (Opus 5.5), written 2026-11-07 12:41Z (date -u)
Predecessor: successor 20 (HANDOVER at the top of notes/CHECKER.md, pushed in 8f6d03bc). This file is overwritten per the brief;
earlier successors' checks are in git history of this path and in notes/CHECKER.md. Every answer is measured from the repository
(commands named), not recalled.

### 1. Branch, head, ahead/behind trunk
- Branch claude/checker (`git branch --show-current`). HEAD = local ref = origin/claude/checker = `git ls-remote` = 8f6d03bc.
- STALE-CLONE TRAP HIT at start: the container's local claude/checker ref was a71d11ff, 462 commits behind origin; `git fetch
  --unshallow` + `git fetch origin claude/checker claude/vibrant-johnson-nxvvxo` + `git merge --ff-only origin/claude/checker` fixed it.
- Against trunk claude/vibrant-johnson-nxvvxo @ b922fc2a (`git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo`):
  3 ahead (1a6f4a6f C130 Add. 2, d6b877f7 C132 main, 8f6d03bc C133 main + handover), 660 behind (178 first-parent);
  merge-base d7091311 (C130 Add. 1 / C131 Add. 1).

### 2. Open work and the next step of each
- C132 = R118 (P-N5-XICYC, L-NEW): main d6b877f7 FAIL E-1..E-7; exact L-4 = R1-R7, sha1 85fe809c, UPDATE d4acaeef (C132 §5).
  Waiting: L-NEW 60 writes fixes entry 3 + L-4, both referees byte-test, Lead second fill. NEXT: C132 Add. 1 on the second fill
  (cmp L-4 with §5; title; UPDATE = d4acaeef if built by the G-U route, else token diff; stale L-3 phrases; both box191 blocks re-run
  from git archive of the new l-new SHA; quote sweep; landing simulation after R117), then Add. 2 (rebuild from parent + checked
  block, byte-compare) and close on the landing commit's green CI.
- C133 = R119 (P-IDEAL-DBL, L-SI): main 8f6d03bc FAIL E-1..E-6; exact L-3 = R1-R6, sha1 845ffdc9 (C133 §5); the UPDATE has no sha1
  (R4 changes its shape): check by token diff against L-3. Waiting: L-SI 42 fixes entry 2 + L-3, referees byte-test, second fill.
  NEXT: C133 Add. 1, then Add. 2 + CI. R119 lands only after R118 (Lead ruling: RESULTS ids land in increasing order).
- Trunk at b922fc2a has no second fill for either yet (last Lead commits 10:30Z R118 first fill, 11:04Z R119 first fill).
- C130 (R117) and C131 (DE37) CLOSED by successor 20 (CI 6710, 6690).

### 3. GAPS rows owned
None. `grep -n -i checker docs/GAPS.md` at trunk b922fc2a: l. 6 (GAP-A, owner L-ALG), l. 11 (G-N5-TIME, owner L-NEW), l. 16
(G-N5-TERM, owner L-NEW, closed); CHECKER appears there only as re-runner / landing checker (e.g. «CHECKER C130 d7091311»).

### 4. Three owner rulings, verbatim, with status (trunk docs/DECISIONS-INDEX.md)
- D1 (DECISIONS.md l. 7-8; index l. 5 «active»): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every
  such claim, including the fleet's own, as wrong until it passes the gauntlet below.» and «Never downgrade the referee to save money.»
- D18 (DECISIONS.md l. 333; index l. 32 «active»): «Focus on N5 and work toward proving it. Explore novel approaches, especially by
  connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions
  where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and
  open problems.»
- D20 (index l. 42 «active»): «We have reset the weekly usage, so we can again work faster no?» (Lead reading L48: full pace.)

### 5. One trap and the check that prevents it
Stale / shallow clone with a stale local branch ref (bit again here: 462 behind). Check: fetch --unshallow, fetch both branches,
checkout + ff-only, then compare `git branch --show-current`, HEAD and `git ls-remote origin claude/checker` before any work and again
before push.sh; `git cat-file -e` on every SHA a brief cites (wait with an `until` loop for in-flight pushes). Also: Oink is not built
in a fresh container: scripts/setup_oink.sh started 12:38Z, before the first push.sh, or the smoke step is NOT RUN.
