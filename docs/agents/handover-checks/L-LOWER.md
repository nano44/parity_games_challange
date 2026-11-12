# Handover check: L-LOWER successor 16 (2026-11-12T22:46Z, date -u; LANE-RESTART step 3)
Every answer measured from the repository at the time of writing (commands named), not recalled.

## 1. Branch, head, distance to trunk
- Branch `claude/l-lower` (`git branch --show-current`). Start trap again: the local branch was 9,573 commits behind origin; fixed by
  `git fetch --unshallow` + `git merge --ff-only origin/claude/l-lower`; `git rev-parse --is-shallow-repository` = false.
- Head e6aa1e7b65e7f2ae1647afdb1f9724cfbb5c81fc = origin/claude/l-lower (successor 15 handover pointer) before this commit.
- Trunk `claude/vibrant-johnson-nxvvxo` at 21b87e70f15832e5c53ec7acb6c4db209e1bda02; merge-base 8cc6ebc6.
  `git rev-list --left-right --count origin/claude/vibrant-johnson-nxvvxo...HEAD` → 131 ahead, 872 behind. No trunk merge (lane files only).
- Clock: date -u 22:45:45Z vs raw.githubusercontent.com Date header 22:45:45 GMT: skew 0 s.

## 2. Open work and next step (BOX L18 continued, frame L18b = L18 + q5 free; after «go»)
- Target: largest P with f6 correct on ALL 129 free pre-states (f6check rows 0..510). Now 10 (L18b_N10a_dec, l18/run/SHA1SUMS d3b6e342),
  chain L18b_H7 → N510 (P 8) → N9a (P 9) → N10a (P 10); solve times 929 / 1,443 / 2,514 s.
- Next: P 11 on base L18b_N10a with l18/n.sh (base-neighbourhood question, R 510): XS 15 alone first (diag row 11 names only mover 15, f7),
  then XS 15 with 12, then 15 with 14 (XORD from the design's reach order). Cap per question up to 6,000 s inside one tracked task (Lead cap
  ruling); report the cap per question. Every SAT: decode, replay sim6 = fenc, f6check rows 0..510, inframe.py, freeze with SHA1SUMS; then
  diag the next failing row and climb. Stop: 3 consecutive capped / neighbourhood-UNSAT attempts at one P. Every cited UNSAT DRUP-checked.
- Nothing in flight (`pgrep -af "pgad|ann3|ekr2|push.sh|cadical"` empty). Binaries (fenc, drup) to rebuild in this session's scratchpad.
  Machine: 4 cores, 15 GB RAM: one R 510 job (5-8 GB) at a time while verify/push runs; at most 2 heavy jobs.

## 3. docs/GAPS.md rows owned by L-LOWER
None. `git show origin/claude/vibrant-johnson-nxvvxo:docs/GAPS.md | grep -n L-LOWER` → only line 11, G-N5-TIME (owner L-NEW, open),
which names L-LOWER instances in its text, not as owner. BOX L18 works against G-N5-TIME (a hard family would be a dead end for N5).

## 4. Three owner rulings that most constrain this lane (verbatim; status from trunk docs/DECISIONS-INDEX.md)
1. D18 (active, index line 32; docs/DECISIONS.md l. 333): «Focus on N5 and work toward proving it. Explore novel approaches, especially by
   connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where
   needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.»
   Constraint: every L18 result is labelled DATA (not a lower bound); negatives «no answer» or «this neighbourhood only».
2. D1 (active, index line 5; docs/decisions/D001-launch-brief.md l. 25, excerpt): «A claimed polynomial algorithm is far more likely to be wrong
   than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.» Constraint: a realized prefix
   is not a super-polynomial family, and a failed neighbourhood is not evidence for N5.
3. D21 (active, index line 46; docs/DECISIONS.md l. 451-454), relayed verbatim: «Okay, I want maximum effort. I want to use 200% usage in 3
   days. There is fable 5.2 as well, use that too in dpeth everywhere where it seems fitting, use fable 5.2 at hard or xhigh. SO yes, 200% uage
   under 2 days.» (typos the owner's). Lead readings L51/L53: maximum effort until 2026-11-14 10:05Z; Fable rejected until 2026-11-18 21:00Z,
   so this successor runs on Opus 5.5 high. Constraint: keep the machine busy (up to 2 heavy jobs), longer caps (6,000 s) allowed.

## 5. One trap that bit this lane, and the check that prevents it
- Trap (successors 14 and 15): a bare «&» launch (ekr2 loop; push.sh twice) and 3 heavy jobs overlapping. Check: every long command,
  push included, is a tracked background task (run_in_background) with output redirected to a file and «echo exit $?»; completion read
  from the exit marker in that file; `pgrep -af` job count before every launch (max 2 heavy, R 510 jobs one at a time beside verify).
- Start trap (again, 9,573 behind): fetch --unshallow, ff-only merge, assert branch and HEAD = origin (both true above).
