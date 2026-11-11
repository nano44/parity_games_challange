# Handover check: CHECKER successor 23 (Opus 5.5), written 2026-11-08 23:12Z (date -u)
Predecessor: successor 22 (HANDOVER 22:45Z at the top of notes/CHECKER.md, pushed in 873ed3ae). This file is overwritten per the brief;
earlier successors' checks are in git history of this path. Every answer is measured from the repository (commands named), not recalled.

### 1. Branch, head, ahead/behind trunk
- Branch claude/checker (`git branch --show-current`). Trap check run first (fetch --unshallow, fetch both branches, checkout,
  merge --ff-only): the local ref was STALE at c8a2bc05 (17 behind) and fast-forwarded; now HEAD = origin/claude/checker =
  `git ls-remote origin claude/checker` = 873ed3ae.
- Against trunk claude/vibrant-johnson-nxvvxo @ 72278533 (`git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo`):
  3 ahead (a15377c7 C136 Add. 2, 3479ecb0 C137 main, 873ed3ae handover), 998 behind (264 first-parent); merge-base bdfb2d07.

### 2. Open work and the next step of each
- C136 = R122 (P-ACYC): landed aaf52291, Add. 2 a15377c7 PASS (byte-equal). CI run #7155 on aaf52291 cancelled (superseded). Run
  42531410624 (#7164) on 72278533 (aaf52291 an ancestor, `merge-base --is-ancestor`; `git diff aaf52291 72278533 -- docs/RESULTS.md
  docs/GAPS.md` empty) is in_progress (GitHub actions get_workflow_run, measured now). NEXT: on green, one CI line in C136 and
  «C136 CLOSED» (C113 / R102 rule). a15377c7 is not yet an ancestor of trunk: the Lead's next merge of claude/checker carries it.
- C137 = R123 (P-N5-QUIET): main PASS 3479ecb0 on the second fill 72278533:docs/agents/R123-draft.md (sha1 a1ab70ef…, 921 lines,
  re-hashed now: match). R123 not yet landed (trunk head 72278533 is the second fill). 3479ecb0 is NOT an ancestor of trunk: the Lead
  must merge claude/checker (873ed3ae or later) first. NEXT: Add. 1 on the landing = rebuild from the parent RESULTS + d[467:761] with
  «checker PENDING)» → «checker 3479ecb0)», inserted before the LINE-START «**Erratum E-1** (not a result» heading; GAPS l. 11 + UPDATE
  d[774] filled; byte-compare; 3479ecb0 an ancestor of the landing; then close on the landing's green CI (or a descendant's with
  RESULTS/GAPS unchanged).
- Coming: R124 (P-N5-END, first fill on L-3) = C138; R125 (P-N5-CHAIN, first fill on L-4) = C139, when the Lead sends them.

### 3. GAPS rows owned
None. `git show origin/claude/vibrant-johnson-nxvvxo:docs/GAPS.md | grep -n -i checker`: l. 6 (GAP-A, owner L-ALG), l. 11 (G-N5-TIME,
owner L-NEW), l. 16 (G-N5-TERM, owner L-NEW, closed); CHECKER appears there only as landing checker / re-runner of other lanes' rows.

### 4. Three owner rulings, verbatim, with status (trunk docs/DECISIONS-INDEX.md)
- D1 (DECISIONS.md l. 7-8; index l. 5 «active»): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every
  such claim, including the fleet's own, as wrong until it passes the gauntlet below.» and «Never downgrade the referee to save money.»
- D18 (DECISIONS.md l. 333; index l. 32 «active»): «Focus on N5 and work toward proving it. Explore novel approaches, especially by
  connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions
  where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and
  open problems.»
- D20 (index l. 42 «active»): «We have reset the weekly usage, so we can again work faster no?» (Lead reading L48: full pace.)

### 5. One trap and the check that prevents it
Stale local branch ref: it bit this start (local claude/checker at c8a2bc05, 17 behind origin 873ed3ae); a commit there would have
diverged and push.sh would fail. Check: fetch --unshallow, fetch both branches, checkout + merge --ff-only, then compare
`git branch --show-current`, HEAD and `git ls-remote origin claude/checker` before any work and again before push.sh. Second trap
(predecessor's): stamps typed ahead of date -u; every stamp in this file comes from $(date -u) in the heredoc. Oink is not built in a
fresh container: scripts/setup_oink.sh was started before the first push.sh, else the smoke step is NOT RUN.
