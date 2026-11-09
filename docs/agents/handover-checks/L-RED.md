# Handover check: L-RED successor 64 (Opus 5.5, D1/D18/D14; LANE-RESTART step 3; written 2026-11-09T09:11Z by date -u)
Every answer is measured from the repository (commands named), not recalled. Predecessor: successor 63, handover =
notes/L-RED.md «Successor 63 HANDOVER» (l. 63) at l-red 4760ba267.

## 1. Branch, head, distance to trunk
- Trap check run first: `git fetch --unshallow origin; git fetch origin claude/l-red claude/vibrant-johnson-nxvvxo;
  git checkout claude/l-red; git merge --ff-only origin/claude/l-red` (local branch was 116 behind; fast-forwarded).
- `git branch --show-current` = claude/l-red; `git rev-parse HEAD origin/claude/l-red` -> both 4760ba2675b6e8f6e8f856331e7107d4c9e580ed.
- Trunk claude/vibrant-johnson-nxvvxo = 98e1c8bee (committed 2026-11-09T07:27:06Z).
  `git rev-list --left-right --count origin/claude/vibrant-johnson-nxvvxo...HEAD` -> 1118 130, i.e. 130 ahead / 1118 behind
  (left = trunk-only); merge-base c2d1e88ee. Trunk not merged in (not needed for this lane's files).

## 2. Open work and the next step of each
- Nothing running: new container (`pgrep -af "push.sh|climb|own.py"`: none); `git worktree list` = main only; scratchpad empty
  (predecessor's lnew / si / new archives lost; rebuild with git archive); tools/oink/build absent (scripts/setup_oink.sh before any Oink route).
- Box R230 (after «go»):
  1. COUNTER SIDE OF B-ONLY ON Γ3 (pads). Next step: rebuild the L-NEW g3 engine tree (git archive l-new fcba92fc, mult91.eng_g3 pattern;
     fvs202 / gflip202 at fa17fdf6), write experiments/red/r230 census: for every Γ3 state of the r229 / r228 instances and climb bests, flag
     a cycle carrying an e-vertex or a mover Λ at/above an e-vertex, split by exact-VJ-tie vs non-tie; then a climb (nclimb229 pattern)
     scoring B-ONLY violations. Any violation: freeze (inst/ + sha1) and message the Lead at once. A B-ONLY-on-Γ3 proof from L-SI 50 (BOX 96)
     preempts: attack premises by R-id, every case.
  2. ADVERSARY on any above-linear point from L-COMP 16 (BOX 37) / L-NEW: waits for routing. Next step: re-measure on two engines
     (cls229 / e93_229 / hgt229 + own.py / L-NEW fvs202), freeze, call genuine growth vs size artefact.
  3. ADVERSARY on L-LOWER 13 BOX L14 sink-cascade lemma: waits for routing. Next step: check its «reaches none» acyclicity step.
- Pending fix rounds to re-read when routed: L-SI 50 (P-N5-GATE G1-G6, R229-box94 Add. A), L-NEW 68 (P-N5-QN G1-G3, R229-box203 Add. B).

## 3. docs/GAPS.md rows I own (trunk 98e1c8bee)
- G-NEST (major, «L-RED (attacks + proof attempts); L-ALG successor if any», open; l. 9).
- L-RED attacks: GAP-A (blocker, open; l. 6), GAP-C (blocker, open; l. 7), G-STR (major, closed; l. 22), G-DOM (major, closed; l. 23).
- R230 works against G-N5-TIME (major, owner «L-NEW (L-LIT T22; referees later)», open; l. 11) under D1/D18.

## 4. Three owner rulings (verbatim; status from trunk docs/DECISIONS-INDEX.md)
- D1 «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own,
  as wrong until it passes the gauntlet below.» (active, index l. 5)
- D18 «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics
  and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and
  proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.» (active, index l. 32)
- D14 «You know it can also test prveiously not tested approaches, it can come up with it own as well» (active, index l. 22)

## 5. One trap that bit this lane, and the check
- Stale local branch at start (this session: 116 behind). Check: trap-check commands above, HEAD == origin/claude/l-red before work.
- Committing while a push runs (successor 61, c482e0d8). Check: `pgrep -af "bash scripts/push.sh"` right before EVERY commit and push.
- Scope trap for R230: R123 B-ONLY is landed for IDEAL-CYC only; any Γ3 claim must not cite it. Check: every Γ3 statement in R230 names
  its class (IDEAL-CYC vs Γ3) and its engine (eng_g3 vs IDEAL-CYC engine).
