# Handover check: L-COMP (successor 14, Opus 5.5; written 2026-11-08, date -u 16:29Z)
Every answer measured from the repository at the time of writing. Successor of L-COMP 13 (handover «HANDOVER -- successor 13 ... PARKS
2026-11-08 16:03Z», notes/L-COMP.md, park commit b63119fc). This OVERWRITES successor 13's answers (in git history).

## 1. Branch, head, distance to trunk
- Container started on a stale local branch (local claude/l-comp 1551 commits behind origin). `git fetch --unshallow` + `git fetch origin
  claude/l-comp claude/vibrant-johnson-nxvvxo` + `git checkout claude/l-comp` + `git merge --ff-only origin/claude/l-comp` -> fast-forward.
- Branch `claude/l-comp` (`git branch --show-current`), HEAD = origin/claude/l-comp = b63119fc (rev-parse, 16:28Z).
- Trunk origin/claude/vibrant-johnson-nxvvxo = fcbc75d5 («Lead: log 14:06Z-14:51Z (R121 landed; C135 Add. 3 + C136 sent; ...)»).
  `git rev-list --left-right --count HEAD...trunk` = 102 ahead / 270 behind; merge-base ebf59a34. +1 ahead after this file's commit.
- Container: 4 cores, 15 GB RAM; Oink not built yet (tools/oink/build missing; scripts/setup_oink.sh before verify). No job of mine runs.

## 2. Open work and the next step of each (all DATA; nothing runs)
- BOX 34 item 1: finish N 2 / M 4 [E-LEV] shards 0/2 and 1/2 from the committed checkpoints experiments/comp/box33/out/N2M4_s{0,1}.txt.ck
  (engine L-NEW asc197.run @ claude/l-new b61c2029; needs a worktree of that commit: `git fetch origin claude/l-new` first, the object is
  not in this clone yet). Then N 2 / M 4 --noelev (both shards). Freeze every new argmax file with sha1.
- BOX 34 item 2: N = 3 by sample (enum33.py --sample S --seed R); state sampler, S, R as scope; A and T3 histograms with and without E-LEV.
- BOX 34 item 3: own N5'-xi-on-Γ3 engine from the SPEC text and R118 (not asc197's code; asc197 read only for its input format);
  cross-check T3 and maxalt on every frozen argmax file and ≥ 1,000 random genomes per measured (N, M); report every mismatch.
- BOX 34 item 4: if A_max grows with (N, M), send the smallest argmax instance to the Lead at once (for L-RED 61, L-NEW 65).
- BOX 32 (exact CNF, tower route): all jobs stopped, every verdict reported; nothing open unless the Lead reopens it.

## 3. docs/GAPS.md rows owned by L-COMP
None open (trunk docs/GAPS.md). Only mention: G-N5-TERM («L-NEW (L-COMP checks runs)», l.16), closed. Boxes 33/34 are DATA for
G-N5-TIME (l.11, owned by L-NEW), which stays open.

## 4. Three owner rulings that most constrain this lane (verbatim; status from trunk docs/DECISIONS-INDEX.md)
1. D18 (active, DECISIONS-INDEX.md:32): «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas
   from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state
   them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.»
2. D1 (active, DECISIONS-INDEX.md:5; excerpt): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such
   claim, including the fleet's own, as wrong until it passes the gauntlet below.»
3. D20 (active, DECISIONS-INDEX.md:42): «We have reset the weekly usage, so we can again work faster no?» (Lead reading L48, l.43: full
   pace; stop on paid overage. Brief of this box: seven-day usage warning (resets 2026-11-11 21:00Z), ≤ 2 CPU-heavy jobs.)

## 5. One trap that bit this lane, and the check that now prevents it
Trap: stale container (this start: 1551 commits behind; successor 13: 1527), and a single non-independent engine: BOX 33's table rests
on L-NEW's asc197 alone. Checks: fetch --unshallow + ff-only + `git branch --show-current` + HEAD == origin before any edit; BOX 34 item 3
(own engine from SPEC/R118, 0 mismatches required) before BOX 33's numbers are called two-engine DATA. Also: before every push
`pgrep -f "bash scripts/push.sh"` empty; push as a tracked task, output to a file, exit code echoed (no pipes).
