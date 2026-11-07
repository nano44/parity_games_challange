# Handover check: L-LOWER successor 5 (2026-11-07 09:2xZ, date -u; LANE-RESTART step 3)
Every answer measured from the repository at the time of writing (commands named), not recalled.

## 1. Branch, head, distance to trunk
- Branch `claude/l-lower` (`git branch --show-current`), tracking origin, working tree clean; clone not shallow
  (`git rev-parse --is-shallow-repository` = false after `fetch --unshallow`); `merge --ff-only origin/claude/l-lower`: already up to date.
- Head af9a73d8bb9c551af7eac8efd24b0072eed074f5 = origin/claude/l-lower = `git ls-remote` («L-LOWER 4 PARKED: handover …»).
- Trunk `claude/vibrant-johnson-nxvvxo` at 137b5e18d1494f47222054e2ebf7f1aa1471bd67 (ls-remote = local origin ref); merge-base f55b98e3.
- `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` → 3 ahead, 340 behind. No trunk merge (not needed for BOX L5).

## 2. Open work and the next step of each
- BOX L5 (after «go»): the inductive rule G_h → G_(h+1) or its obstruction. Next step: dissect rec/H5_lift_d24.txt (H5 + 4 TOP-ADD
  levels, the climb seed) vs rec/H6_d24_F126.txt level by level (Ξ-options, ranks, fuel targets via lpaudit.py), then revert each changed
  part and record F; then the cheapest neighbouring-field structure (Gray code / Hanoi fuel schedule) as a designed tower.
- Seventh level (F(6) = 254): NOT mine to brute-climb (L-COMP 10 box 30 runs it). Predecessor's runs died with its container
  (`pgrep -f rclimb` empty here). Warm-start genome rec/G7_best_d28.txt (F 2 6 14 30 62 126 222 …) stays as the hand-off.
- DUTY P-M2D-DEAD fix round 2 (afc85c57, line L-3): waiting for the referees' byte tests; answer by script if an item arrives, never
  edit the frozen packet.

## 3. docs/GAPS.md rows owned by L-LOWER
None (`grep -c L-LOWER docs/GAPS.md` = 0). The box works against G-N5-TIME (major, owner L-NEW, open; GAPS.md line 11).

## 4. Three owner rulings that most constrain this lane (verbatim, docs/DECISIONS.md; status docs/DECISIONS-INDEX.md)
1. D18 (active, index line 32; DECISIONS.md l. 333): «Focus on N5 and work toward proving it. Explore novel approaches, especially by
   connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions
   where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and
   open problems.» Constraint: every statement labelled PROVED (lane) / CONJECTURE / DATA / DEAD; step 2 of the box imports a structure.
2. D1 (active, index line 5; DECISIONS.md l. 7): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every
   such claim, including the fleet's own, as wrong until it passes the gauntlet below.» Constraint: a recursive family is a lower-bound
   CANDIDATE only; N5's super-polynomiality needs R104/R117 plus a proof that every level doubles, not data to h = 7.
3. D14 (active, index line 22; DECISIONS.md l. 246): «You know it can also test prveiously not tested approaches, it can come up with it
   own as well» (typos the owner's). Constraint: own designs are allowed, but go through the same CANDIDATE → replay path.

## 5. One trap that bit this lane, and the check that now prevents it
Trap: the stale / shallow clone (predecessors started with the local branch behind origin; pushes then fail or a merge misreads its
base). Check, run first this session: `fetch --unshallow`, `checkout claude/l-lower`, `merge --ff-only`, then compare
`git rev-parse HEAD`, `origin/claude/l-lower` and `git ls-remote` (all af9a73d8 here). Second trap: rclimb.c's __int128 values
overflow at d ≥ 32 (ranks ≥ 127); any run at d ≥ 32 uses L-COMP's rclimb30.c, and every L5 record will state its d.
