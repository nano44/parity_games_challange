# Handover check: L-LOWER successor 15 (2026-11-12 09:47Z, date -u; LANE-RESTART step 3)
Every answer measured from the repository at the time of writing (commands named), not recalled.

## 1. Branch, head, distance to trunk
- Branch `claude/l-lower` (`git branch --show-current`). The local branch was 9,555 commits behind origin at start and was
  fast-forwarded (`git merge --ff-only origin/claude/l-lower`) after `git fetch --unshallow`; `git rev-parse --is-shallow-repository` = false.
- Head 5d8b4b102f142ff34a2f021a6b0c41de9401c1d7 = origin/claude/l-lower (successor 14 HANDOVER).
- Trunk `claude/vibrant-johnson-nxvvxo` at 071392490dcea36bfa952288aa6170d45fadf874; merge-base 8cc6ebc6.
- `git rev-list --left-right --count origin/claude/vibrant-johnson-nxvvxo...HEAD` → 113 ahead, 843 behind.
  No trunk merge (not needed for the lane's files).

## 2. Open work and the next step of each (BOX L17, after «go»)
- BOX L17 (Lead 07:37Z): build the base AROUND the frozen f6 pair (ekr2_f6_k1_P510, 4fee0495). Milestone: rows 0..18 realized,
  replayed sim6 = fenc; stretch P 32. Stop rule: three consecutive capped runs with no answer at the same P → write the obstruction.
- A1: DEAD start (ann3 re-solves all ranks; f6 broken; pgad3 UNSAT at prefix 2, solver only). Recorded in L17 §2. Nothing open.
- A2 (l17/run/A2.txt d9aa4f7e, best 161 violated constraints; SHA1SUMS checked OK): next step: `l14/rsolve.py` → A2_solved.txt,
  `l16/f6check.py` on rows 0..64, then ascending exact prefix sweep 2..18 (`l13/sweep1.sh`, pgad3, XS 8, G {63}, 600 s per prefix
  question, task cap 2,900 s), every SAT prefix replayed sim6 = fenc and frozen with SHA1SUMS.
- A3 (only if A2 stops before P 18): one design in a frame that KEEPS the design's ranks (pin the 6 design options' relative ranks
  in ann3/gsolve, or pgad5 on A2_solved with FIXC 16,17 and XS 8,11,12,14,15 and an XORD consistent with the base). Then the box
  result in L17: the P 18 design or the exact obstruction with its instance; DRUP every cited UNSAT first.
- No runs in flight (`pgrep -af "pgad|ann3|ekr2|push.sh"` empty before this commit). Binaries (fenc, drup, ann3) to rebuild in the
  scratchpad before «go»; no long job before «go».

## 3. docs/GAPS.md rows owned by L-LOWER
None. `grep -c L-LOWER docs/GAPS.md` = 0 on this branch; on trunk 1 matching line (line 11, G-N5-TIME, owner L-NEW, open): it
cites L-LOWER's instances in its text, not as owner. The box works against G-N5-TIME.

## 4. Three owner rulings that most constrain this lane (verbatim; status from trunk docs/DECISIONS-INDEX.md)
1. D18 (active, index line 32; docs/DECISIONS.md l. 333): «Focus on N5 and work toward proving it. Explore novel approaches,
   especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make
   reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven
   results from conjectures and open problems.» Constraint: each L17 statement carries PROVED (lane) / CONJECTURE / DATA / DEAD;
   a long realized prefix is DATA, not a lower bound (L17 §0).
2. D1 (active, index line 5; docs/decisions/D001-launch-brief.md l. 25, excerpt): «A claimed polynomial algorithm is far more
   likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet
   below.» Constraint: a design that fails in one frame is not evidence that N5 is polynomial; a P 18 design is not a
   super-polynomial family; scope every claim to its instance.
3. D14 (active, index line 22; docs/DECISIONS.md l. 246): «You know it can also test prveiously not tested approaches, it can
   come up with it own as well» (typos the owner's). Constraint: A2 / A3 are own designs and go through the same freeze / replay /
   DRUP discipline as any other candidate.

## 5. One trap that bit this lane, and the check that prevents it
- Trap (successor 14, twice): a bare «&» (one ekr2 loop; one push.sh killed in verify). Check: every long command, push included,
  goes through a tracked background task with output redirected to a file and «echo exit $?»; completion is read from that file's
  exit marker, never by a pgrep wait loop (which matches its own command line, successor 13).
- Start trap (again this time, 9,555 behind): fetch --unshallow, ff-only merge, assert branch and HEAD = origin (both true above).
