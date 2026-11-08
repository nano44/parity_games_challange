# Handover check: L-LOWER successor 11 (2026-11-08 12:15Z, date -u; LANE-RESTART step 3)
Every answer measured from the repository at the time of writing (commands named), not recalled.

## 1. Branch, head, distance to trunk
- Branch `claude/l-lower` (`git branch --show-current`); the local branch was 76 commits behind origin at start and was
  fast-forwarded (`git merge --ff-only origin/claude/l-lower`); clone not shallow (`git rev-parse --is-shallow-repository` = false).
- Head 6b69124bda4e1616582e58bd7841380cb26e08c9 = origin/claude/l-lower (successor 10 HANDOVER).
- Trunk `claude/vibrant-johnson-nxvvxo` at fdc0f1e9cff20275b6e7c2c20b4e61a0ddfcd8a5; merge-base 8cc6ebc6.
- `git rev-list --left-right --count origin/claude/l-lower...origin/claude/vibrant-johnson-nxvvxo` → 45 ahead, 540 behind.
  No trunk merge (not needed for the lane's files).

## 2. Open work and the next step of each (BOX L11, after «go»)
- Item 1 (DECIDE OSC-ROOM on small exact cases, h = 3 and h = 4): formulate «one SHARED helper cascade serves every capped level»
  vs «each level needs its own oscillator» as SAT questions on the exact small targets (base: HS2_d3, the h3d4 capped targets
  DRUP-VERIFIED UNSAT at e198d0b6, the h3d5 Glucose instances (OPEN: 6 TIMEOUT at 1,800 s, 2 never fully run), HIT7's lower
  levels). Every UNSAT with its scope and a DRUP check (Glucose4 proofs via l9/resolve2.py; pysat/CaDiCaL proofs are incomplete);
  every SAT model frozen and replayed (fenc / sim6). Next step: re-read L10 §2e-§3d and the l8/hsat.py, l9/gwhole.py encodings;
  add a «helper reach set» constraint (shared cascade = helpers allowed to serve all levels; per-level = helpers partitioned
  by level) and run the smallest instances first.
- Item 2: state OSC-ROOM as PROVED (lane) for small h, DEAD with the instance, or sharpened, and what it implies for d(h)
  (linear → towers extend, N5 exponential in d; super-linear → T polynomial in d, the tower route stalls).
- No runs of mine in flight (`pgrep -af "push.sh|gwhole|ann "` empty before this push). L-COMP 13's f5-gadget run on the C10 base
  is L-COMP's; any result comes through the Lead.

## 3. docs/GAPS.md rows owned by L-LOWER
None (`grep -c L-LOWER docs/GAPS.md` = 0). The box works against G-N5-TIME (owner L-NEW, open).

## 4. Three owner rulings that most constrain this lane (verbatim, docs/DECISIONS.md; status docs/DECISIONS-INDEX.md)
1. D18 (active, index line 32; DECISIONS.md l. 333): «Focus on N5 and work toward proving it. Explore novel approaches, especially
   by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable
   assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from
   conjectures and open problems.» Constraint: OSC-ROOM's verdict is labelled PROVED (lane) only for the exact scoped instances;
   the d(h) growth law stays CONJECTURE / DATA.
2. D1 (active, index line 5; D001-launch-brief.md l. 25-26, excerpt): «A claimed polynomial algorithm is far more likely to be wrong
   than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.» Constraint: a tower
   stall is not evidence that N5 is polynomial, and an extendable small-h cascade is not an asymptotic lower bound.
3. D14 (active, index line 22; DECISIONS.md l. 246): «You know it can also test prveiously not tested approaches, it can come up
   with it own as well» (typos the owner's). Constraint: the shared-vs-per-level SAT formulation is an own design and goes through
   the same freeze / DRUP / replay discipline as any other result.

## 5. One trap that bit this lane, and the check that prevents it
- Trap: SAT «UNSAT» reported from pysat/CaDiCaL proofs whose final empty clause is not UP-derivable (h3d4 a110, successor 9):
  the DRUP check passed every lemma but the proof was incomplete. Check: proofs from Glucose4 (l9/resolve2.py), checked with
  l8/sat/drup.c, and the verdict «VERIFIED» only when drup reports the final empty clause derived. Also the start trap (stale
  local branch, 76 behind this time): fetch --unshallow, ff-only merge, assert branch and HEAD = origin (both true above).
