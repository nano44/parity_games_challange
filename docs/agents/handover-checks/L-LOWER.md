# Handover check: L-LOWER successor 13 (2026-11-09 08:08Z, date -u; LANE-RESTART step 3)
Every answer measured from the repository at the time of writing (commands named), not recalled.

## 1. Branch, head, distance to trunk
- Branch `claude/l-lower` (`git branch --show-current`). The local branch was 112 commits behind origin at start and was
  fast-forwarded (`git merge --ff-only origin/claude/l-lower`); clone not shallow (`git rev-parse --is-shallow-repository` = false).
- Head 8fc703354ae26bdcfff90d934182dfdf5f442a62 = origin/claude/l-lower (successor 12 HANDOVER).
- Trunk `claude/vibrant-johnson-nxvvxo` at 547985a10fad4739611ba46aeaebaec3dc9899ab; merge-base 8cc6ebc6.
- `git rev-list --left-right --count origin/claude/vibrant-johnson-nxvvxo...HEAD` → 81 ahead, 728 behind.
  No trunk merge (not needed for the lane's files).

## 2. Open work and the next step of each (BOX L14, after «go»)
- Item 1, LEMMA (D18, main): on the level-8 fixed-rank bases (C10 / C11 family; the class to be stated exactly in docs/lower/L14),
  prove that the gadget for a sink at level j needs a helper cascade reaching no core mover of level ≤ j, of size ≥ c·j.
  PREF-FUEL (L13 §2) gives |closure| ≥ j + 1; the open part is «reaches none». Next step: read L13 §2-§4 and §9 and the
  required-preference lists (l13/reqpref.py, isol.py) of the C10 sink f5 and the C11 sink q4, and try to show that a helper
  reached from a lower core mover inherits that mover's fixed preference and so cannot carry the sink's change. If it does not
  close: the exact failing step and the smallest configuration.
- Item 2, FALSIFIER: C12 = C11 + cut «pairs 0-3 reach none of 8, 11, 13, 14, 15» (L10 ann.c, that order); freeze (sha1);
  48 single-helper runs (pgad3.py), global sink and first infeasible row, DRUP on every cited UNSAT. Prediction: sink q3,
  wall < 14; a wall ≥ 14 refutes the READING.
- No runs in flight (`pgrep -f "bash scripts/push.sh"`, `pgrep -f pgad` empty before this commit).

## 3. docs/GAPS.md rows owned by L-LOWER
None (`grep -c L-LOWER docs/GAPS.md` = 0). The box works against G-N5-TIME (owner L-NEW, open; GAPS line 11).

## 4. Three owner rulings that most constrain this lane (verbatim, docs/DECISIONS.md; status docs/DECISIONS-INDEX.md)
1. D18 (active, index line 32; DECISIONS.md l. 333): «Focus on N5 and work toward proving it. Explore novel approaches, especially
   by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable
   assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from
   conjectures and open problems.» Constraint: the L14 lemma is PROVED (lane) only on the stated base class; the sink recursion
   stays a READING / DATA until then.
2. D1 (active, index line 5; D001-launch-brief.md l. 25, excerpt): «A claimed polynomial algorithm is far more likely to be wrong
   than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.» Constraint: a
   level-8 obstruction on one base class is not evidence that N5 is polynomial; the lemma's scope must say what it does not exclude.
3. D14 (active, index line 22; DECISIONS.md l. 246): «You know it can also test prveiously not tested approaches, it can come up
   with it own as well» (typos the owner's). Constraint: the C12 cut is an own design and goes through the same freeze / DRUP /
   replay discipline.

## 5. One trap that bit this lane, and the check that prevents it
- Trap: enc32 --freerank has no transitivity within an insertion slot, so a SAT model can carry a cyclic order (successor 12,
  C4 k 1 prefix 10: SAT, decoded genome rejected by enc32 --fix all at prefix 3). Check: use pgad3.py (3-cycle bans) and replay
  every SAT (decoded genome through the CHECK mode / fenc + sim6) before citing it. Also the start trap (stale local branch, 112
  behind this time): fetch --unshallow, ff-only merge, assert branch and HEAD = origin (both true above).
