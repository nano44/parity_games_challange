# Handover check: L-LOWER successor 12 (2026-11-08 23:23Z, date -u; LANE-RESTART step 3)
Every answer measured from the repository at the time of writing (commands named), not recalled.

## 1. Branch, head, distance to trunk
- Branch `claude/l-lower` (`git branch --show-current`). The local branch was 90 commits behind origin at start and was
  fast-forwarded (`git merge --ff-only origin/claude/l-lower`); clone not shallow (`git rev-parse --is-shallow-repository` = false).
- Head ecdba818a54de723f5dd47fbad92a6136c7b40d7 = origin/claude/l-lower (successor 11 HANDOVER).
- Trunk `claude/vibrant-johnson-nxvvxo` at 72278533e555e0bcf43aecd28227889507c3e621; merge-base 8cc6ebc6.
- `git rev-list --left-right --count origin/claude/vibrant-johnson-nxvvxo...HEAD` → 59 ahead, 712 behind.
  No trunk merge (not needed for the lane's files).

## 2. Open work and the next step of each (BOX L13, after «go»)
- Item 1, EXACT PREFIX GADGET: encode «a genome with FREE wiring on a small helper set (ranks fixed elsewhere, L-COMP's fixed-rank
  method, enc32 copy l12/enc32_lcomp.py sha1 a8c4f5e3) realizes rows 0-20 of the common target (core8 c6e19673 = S8_R2 fd5b112c
  there)». Grow the helper set 1, 2, 3, … on a base (seed / C10 / SEED_R2); per size SAT (decode, replay fenc + sim6 + replay30,
  freeze) or UNSAT (first infeasible step, culprit; DRUP-checked, proof deleted after the check, CNF sha1 + command kept).
  Next step: read enc32_lcomp.py to see how wiring is fixed (W0-R) and add free-wiring variables for a chosen helper set.
- Item 2: if a gadget exists, splice it into a base and rerun C10-style fixed-rank questions on the FULL core8 and S8_R2: the first
  exact comparison of the two targets; a full-length SAT model is a HIT (decode, replay, freeze, Lead at once, then N5 Γ3 check).
- Item 3: if none exists at small helper counts, state the obstruction exactly (start-up hold, rule of L10 §2f / §3d), as a lemma
  if possible, instances frozen (evidence for CONJECTURE OSC-ROOM″).
- No runs in flight (`pgrep -f "bash scripts/push.sh"` and `pgrep -f enc32` empty before this commit).

## 3. docs/GAPS.md rows owned by L-LOWER
None (`grep -c L-LOWER docs/GAPS.md` = 0). The box works against G-N5-TIME (owner L-NEW, open).

## 4. Three owner rulings that most constrain this lane (verbatim, docs/DECISIONS.md; status docs/DECISIONS-INDEX.md)
1. D18 (active, index line 32; DECISIONS.md l. 333): «Focus on N5 and work toward proving it. Explore novel approaches, especially
   by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable
   assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from
   conjectures and open problems.» Constraint: a prefix-gadget UNSAT is PROVED (lane) only within its encoding scope (fixed ranks,
   named helper set); the d(h) law stays CONJECTURE / DATA.
2. D1 (active, index line 5; D001-launch-brief.md l. 25-26, excerpt): «A claimed polynomial algorithm is far more likely to be wrong
   than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.» Constraint: no
   level-8 gadget is not evidence that N5 is polynomial; a HIT is a lower-bound datum only after replay and the end-to-end N5 check.
3. D14 (active, index line 22; DECISIONS.md l. 246): «You know it can also test prveiously not tested approaches, it can come up
   with it own as well» (typos the owner's). Constraint: the free-wiring prefix encoding is an own design and goes through the same
   freeze / DRUP / replay discipline.

## 5. One trap that bit this lane, and the check that prevents it
- Trap: pysat Glucose4 with_proof writes its proof to a temp file (~5 MB/s); an hour-long run filled the disk allowance (successor
  11, TT3 d 5, ENOSPC). Check: proofs only for short re-solves of cited UNSATs (l12/drupcheck.py), deleted after drup.c, with CNF
  sha1 + regenerate command kept; long searches run without proofs. Also the start trap (stale local branch, 90 behind this time):
  fetch --unshallow, ff-only merge, assert branch and HEAD = origin (both true above).
