# Handover check: L-RED (successor 3, Opus 5.5 per owner D8; LANE-RESTART step 3; written 2026-10-16 15:57Z by date -u)
Every answer measured from the repository at the time of writing (commands named), not recalled. Predecessor:
session_01PxvcUhsSEhfjURzmBDBeoN (Opus 5.5, PARKED 15:20Z end of CARRY box, notebook head 5a30e98 -> trunk fe8cb18).
The previous version of this file (successor 2's check) is replaced.

## 1. Branch, head, distance to trunk
- Branch `claude/l-red`. Container head before step 0: 5a30e98 (stale local ref, clean tree); after the fetch,
  origin/claude/l-red = 6b52858 (predecessor's PARKED notebook), already on trunk, so the trunk merge contains it
  (`git merge-base --is-ancestor 6b52858 origin/claude/vibrant-johnson-nxvvxo` true). This file pushed as 053255c
  (fast-forward 6b52858..053255c, VERIFY PASS; Oink smoke NOT RUN: Oink not built yet in this container).
- Step 0: `git fetch origin && git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` -> merge commit e11de1d
  (trunk at b16716d "RESULTS DE10; NOW: L-ALG end of box, parked").
- `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` -> 1 ahead (the merge commit), 0
  behind, before this file's commit (2 ahead after it). `git merge-base` = b16716d (trunk head).

## 2. Open work and the next step of each
No climbs in flight (notebook IN FLIGHT: none; this container has no scratchpad from the predecessor, so oink-det,
oink-debug and the LALG_DIR checkout must be rebuilt). Queue from the Lead brief = notebook Resume point:
- (1) (CM) attack: L-ALG GAP-A-M §13h candidate "child M never drops across a parent DEF step into an IDEAL-STABLE child
  context" (DATA only, 0/123 in §13h, 0/129 per NOW). My R15 §13 check used the UNFILTERED phi_full.child_m_drops (3 and 2
  drops on h4_compound2x2_n44 / h4_compound_n44, all into ideal -1 contexts: outside the premise). Next step: build a
  filtered fitness (ideal stability from dtl_deficit, DEF tag on the parent step, M per index from dtl_regvec, Oink
  order and stable order both labelled) by reading L-ALG's experiments/alg/dtl_childM.py read-only, reproduce its
  0/123 on the same files, then climb from h4_compound2x2_n44, h4_nested7_oink_n44, h4_def9/10_oink_n28 (the only games
  with child-death drops).
- (2) Scale the compounding: h4_compound2x2_n44 (R15 §12: K_parent >= 3 x K_child = 2, block score 4). Next step: climb
  with a fitness = K_child at fresh ideal-stable child contexts (and a third level), n = 44 -> 60 -> 76; report the
  growth curve with order labels.
- (3) r0 dips at one ideal-stable context WITH a DEF filter (the old r0dips fitness lacks it). Next step after (1)-(2).
Any super-polynomially growing count -> immediate report to the Lead. Every instance relied on: Oink-verified, committed,
pinned in experiments/red/check.sh.

## 3. docs/GAPS.md rows I own
- None. Trunk docs/GAPS.md (b16716d): the open table is empty; the closed table holds only G1 (owner L-STRUCT).
  GAP-A / GAP-C / (H4) are L-ALG's proof gaps (docs/alg/DTL-proof.md, GAP-A-M.md), which L-RED attacks, not owns.

## 4. The three owner rulings that most constrain me (verbatim), with their DECISIONS-INDEX status
1. D1 (docs/decisions/D001-launch-brief.md lines 25-26, 96; index row D1 "active"):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.
2. D7 (docs/DECISIONS.md#d7; index row D7 "active"):
   > a
   (Q9 option (a): "Continue at the current rate. We pause automatically if the cap is hit and stop at once on overage.")
   With D1 line 62 "On paid overage, stop the fleet and tell me.": no detached climbs outliving my box.
3. D8 (docs/DECISIONS.md#d8; index row D8 "active"):
   > I think it is okay if we switch to opus 5.5 until the weekly limit is reset no? They produce very similiar results on the benchmarks
   Lead reading L27: Opus work labelled as such; referees wait, so anything I find stays DATA until refereed.
   Binding Lead reading (not an owner ruling): L26, the frozen DTL statement covers EVERY order datum, so a family under
   any order refutes A_DTL; every count is labelled with its order.

## 5. One trap that bit this lane, and the check that now prevents it
- Trap: `out=$(python3 ... | head -1)` in experiments/red/check.sh under set -euo pipefail: head exits early, Python gets
  EPIPE (exit 120), pipefail kills the gate; verify FAILED transiently (14:30Z, 14:42Z). Check now: every pin uses
  `| sed -n 1p` (reads all input); `grep -c "| head" experiments/red/check.sh` must be 0 before a push.
- Push trap (piped gate, 7e2efb8 / 6a60655 / c204679): pushes only via `scripts/push.sh > file 2>&1; echo $?`, never piped.
- Kill trap: `pkill -f PAT` kills my own shell when PAT is in the same command; kill by PID in a separate call.
