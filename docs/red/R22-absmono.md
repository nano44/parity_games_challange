# R22: (ABS-mono) and (ABS-mono-pw) are FALSE on A_DTL, both orders (L-RED box 5, 01:37Z by date -u; produced on Opus 5.5)
Targets (L-ALG GAP-A-M §21j, l-alg 57e2256 / f060d6a, relayed by the Lead 01:00Z and 01:10Z):
(ABS-mono) PHI0 = sum over v in G' of idx0(v) (index of the depth-0 piece that removes v, dtl_idx0.py) never RISES at a
transition whose first piece-level difference (dtl_piecediff.classify) is not a RES at a depth-0 piece.
(ABS-mono-pw) at every such transition, no single vertex moves to a LATER depth-0 piece.

## 1. Tools
experiments/red/carry/abspw.py: my loop on L-ALG's modules (read-only, LALG_DIR = l-alg 57e2256): dtl_settle build,
dtl_piecediff.classify, dtl_idx0.idx0; same transition classes as dtl_dvctx.py. Reproduces dtl_dvctx's non-RES-d0
counts on the seeds (spp_final_n20 14, spp19_stable_n30 12, f1_twodef_n48 2). carry/absmono.py runs L-ALG's
dtl_dvctx.py DVC_PHI=1 unmodified and parses its class table. Climb: dtl_search --fitness abspw, seed 7202, STABLE
order, from h4_compound2x2_n44, ~9,600 steps.

## 2. FINDING (experiments/red/carry/instances/absmono_viol_n44.pg)
n = 44, sha1 0d570670. Pinned Oink: 1 dominion, 34 tangles, 5 iterations, solution verified (12 strategies).
L-ALG's dtl_dvctx.py DVC_PHI=1, unmodified, DTL_ORDER=stable: "1 ('SHRINK', 'd0', 'DEF', 'PHI0 RISES')" (plus 2
('SHRINK', 'd0', 'DEF', 'PHI0 falls')). abspw.py gives the same in BOTH orders: 1 pointwise violation, 7 vertices later.
Even's phase, search 0 -> 1 (pyref numbering, original ids):
- depth-0 piece sizes s0: 44 43 40 37 33 28 26 25 22 20 19 16 15 13 12 9 8 7 1 (19 pieces; piece 14 stable, 17 stable);
  s1: 44 43 40 37 33 28 26 25 22 20 19 16 15 13 11 9 8 7 6 1 (20 pieces; piece 14 stable, 17 and 18 now -1).
- First difference: SHRINK at depth-0 piece 14 (context 12 -> 11): an absorption.
- Later, piece 17 (context size 7 in both) changes its actual result from STABLE to -1 with the larger tangle set, and
  the tail splits into one more piece. Vertices moved later (id: piece before -> after): 43: 18->19, 16: 16->17,
  9, 22, 41, 18, 35: 17->18. Two vertices move earlier. PHI0 374 -> 379.
Mechanism: exactly the weak point L-ALG named: after the first difference, a later depth-0 piece runs with a larger
tangle set, and best_vertices is not monotone in T (a stable result turns -1), which pushes vertices later.

## 3. Consequence (reading)
The budget "S - 1 <= (#RES_d0 + 1)(n^2 + 1) + #deeper" built on (ABS-mono) (GAP-A-M §21j) loses its premise: PHI0 can
rise at an absorption step, by later-piece non-monotonicity. One instance, rise of 5; no growth shown.
