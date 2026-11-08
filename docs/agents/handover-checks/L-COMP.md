# Handover check: L-COMP (successor 13, Opus 5.5; written 2026-11-08, date -u 07:46Z)
Every answer measured from the repository at the time of writing. Successor of L-COMP 12 (handover «HANDOVER -- successor 12 ... PARKS»,
notes/L-COMP.md, park commit 989df5a0). This OVERWRITES successor 12's answers (in git history).

## 1. Branch, head, distance to trunk
- Container started on a stale local branch: local claude/l-comp was 1527 commits behind origin. `git fetch --unshallow` + `git fetch origin
  claude/l-comp claude/vibrant-johnson-nxvvxo` + `git checkout claude/l-comp` + `git merge --ff-only origin/claude/l-comp` -> fast-forward.
- Branch `claude/l-comp` (`git branch --show-current`), HEAD = origin/claude/l-comp = 989df5a0 (rev-parse, 07:46Z).
- Trunk origin/claude/vibrant-johnson-nxvvxo = 36c183f8 («Lead: L-LOWER 10 roster/restart row; log 06:17Z-06:45Z ...»).
  `git rev-list --left-right --count HEAD...trunk` = 78 ahead / 142 behind; merge-base ebf59a34; 989df5a0 is NOT an ancestor of trunk.
  +1 ahead after this file's commit.
- Container: 4 cores, 15 GB RAM, 30 GB disk free; Oink missing -> scripts/setup_oink.sh running (tracked). No job of mine runs.

## 2. Open work and the next step of each (all DATA; nothing runs)
- BOX 32 item 1 (after «go»): an independent EXACT encoding (SAT / CP-SAT) of «a d 32 genome whose run realizes core8_HIT7 exactly»
  (target claude/l-lower experiments/lower/l10/out/core8_HIT7.txt sha1 c6e19673; stretched target out/target_HIT7_H8.txt). Next: read
  R104 / IDEAL model + L-LOWER's constraint generator (l7/ranksolve.constraints, l7/clamp.runclamp) for the semantics only, write my own
  encoding in experiments/comp/box32/, validate (accept HIT7's own run vs its 7-level target; reject 20 mutants; 0 mismatches vs
  fenc / sim6 / replay30), send validation + code sha1 to the Lead, then solve in resumable cubes.
- BOX 32 item 2: replay any L-LOWER 10 candidate (fenc + sim6 + replay30) and run N5 end to end on its Γ3 (n5b + n5v spec + Oink zlk
  --verify) vs L + 3. Waits for a candidate.
- Box 31 level-7 climbs (L7a-d, L7br, L7cr): ENDED by successor 12 (plateau T 466 < 510); not to be relaunched unless the Lead asks.
- Second N5 engine on HIT7 (n5v = 302 = n5b = L + 3, Oink OK): DONE by successor 12.

## 3. docs/GAPS.md rows owned by L-COMP
None open (trunk docs/GAPS.md). Only mention: G-N5-TERM («L-NEW (L-COMP checks runs)», l.16), closed. Box 32 is DATA for G-N5-TIME
(l.11, owned by L-NEW), which stays OPEN.

## 4. Three owner rulings that most constrain this lane (verbatim; status from trunk docs/DECISIONS-INDEX.md)
1. D18 (active, DECISIONS-INDEX.md:32): «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas
   from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state
   them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.»
2. D1 (active, DECISIONS-INDEX.md:5; excerpt): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such
   claim, including the fleet's own, as wrong until it passes the gauntlet below.»
3. D20 (active, DECISIONS-INDEX.md:42): «We have reset the weekly usage, so we can again work faster no?» (Lead reading L48, l.43: full
   pace; stop on paid overage. Brief of this box: seven-day usage warning, ≤ 2 CPU-heavy jobs.)

## 5. One trap that bit this lane, and the check that now prevents it
Trap: stale container (this start: 1527 commits behind; successor 12: 1516); and an unfaithful engine at large d: L-LOWER's l5/fev.c
overflows at d ≥ 32 (successor 12 notebook). Checks: fetch --unshallow + ff-only + `git branch --show-current` + HEAD == origin before
any edit; at d 32 use only fenc (exact d ≤ 64), sim6 and replay30, and require all three to agree on every decoded genome.
Also: kill only by PID files; before every push `pgrep -f "bash scripts/push.sh"` empty; push as a tracked task, output to a file.
