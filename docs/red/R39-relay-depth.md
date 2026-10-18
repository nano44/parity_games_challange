# R39: an inversion relay driven by a region clock gives re-steal depth 2 (L-RED box 10; produced on Opus 5.5)
Status: DATA plus READING, unrefereed. Target: Lead box-10 item (1), the lag / serialized-piece gadget (R37 addendum, R38).
All measurements use L-ALG's tools UNMODIFIED (detached checkout of claude/l-alg at e0fc1bb0). Started 2026-10-18 02:10Z (date -u).

## 1. Result
- experiments/red/lag/instances/depth2_n39.pg (sha1 6200e5869e8f), n = 39, Even's phase of 9 searches.
- L-ALG experiments/alg/dtl_stealdepth.py, RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0, the SAME output in both order data:
  - `RE-STEAL |R| 39 pair 3 step (r1, top 14) t 2 k 2 depth 1 | previous 1 | causes: [(2, (1, 13), 3, 0)]`
  - `RE-STEAL |R| 39 pair 4 step (r1, top 15) t 1 k 2 depth 2 | previous 2 | causes: [(3, (1, 14), 2, 1)]`
  - `max k 2; max depth 2`.
- Every re-steal found before had depth 1 (R37: about 3,000 variants and climbs, both orders).
- Pinned Oink `oink --dtl --no-single --no-wcwc --no-loops -v`: 10 iterations, solution verified.
  experiments/red/dtl/dtl_flipflop.py --oink: dominions 1, tangles 15, iterations 10, MATCH.

## 2. The construction (section 3 explains why it works)
- Clock: L-ALG's dtl_chainfam UP chain (a, b, z, x_1..x_k) with an added root top S (Odd-owned, edge to an Odd sink W) and an
  added edge a -> S. Then S's round-1 region in the root context gains x_m from visit m. experiments/red/lag/clockcheck.py on
  cl2.py k = 6 prints region sizes 2, 3, ..., 9 over the 8 visits, in both order data.
- Levels j = -1..D (here D = 2). Tangle t_j = {tau_j, w_j, y_j, v_j}:
  - tau_j: top, Odd-owned, edges w_j and v_j;
  - w_j: Even, edge y_j;
  - y_j: Odd, edges v_j and T_j (the escape);
  - v_j: Even, edge tau_j.
  t_j fires at the Odd top T_j, with T_{-1} > T_0 > ... (earlier steps for lower j).
- Hold: edge w_j -> y_{j-1}. When t_{j-1} fires at T_{j-1}, w_j joins that region, so t_j is excluded at T_j.
- Freeze: edge w_j -> f_j, where f_j is Odd with edges x_{j+3} and S. From visit j + 3, S's region takes f_j and then w_j.
- Only w_j is ever pulled into an earlier region. tau_j is Odd and needs both w_j and v_j, so it stays out. y_j is then not
  re-attracted at T_j, because its other successor v_j is neither consumed nor in Z.
- Control wiring: the out-edges of T_j plus three helpers, found by experiments/red/lag/schemaclimb.py (seed 221, about
  150 steps). The climb was given only the schema-match score of section 3; the cycles, holds, freezes and clock were fixed.

## 3. Why: the relay schema (READING plus an abstract check)
- F_j(x) means t_j fires at visit x. With holds and freezes as above:
  F_j(x) = avail(x) and not (F_{j-1}(x) or x >= j + OFF).
  Each level is the inverse of the level above until its freeze arrives. The freezes reach the levels one search apart,
  from the top level down.
- experiments/red/lag/relaymodel.py scores this F/X table with dtl_stealdepth's own depth rule, re-implemented for prediction
  only. Max depth = D for levels -1..D, in a phase of D + OFF + 3 visits. At D = 2 the predicted table is exactly the observed
  one (schemashow.py, steps (1, T_j)):

  | level | predicted (visits 0..8) | observed |
  |---|---|---|
  | -1 | XFXXXXXXX | .FXXXXXXX |
  | 0 | XXFXXXXXX | .XFXXXXXX |
  | 1 | XFXFXXXXX | .FXFXXXXX |
  | 2 | XXFXFXXXX | .XFXFXXXX |

  At visit 0 no tangle is known yet, so it is printed ".".
- The plan in the R37 addendum was a 2-search lag between copies. It is not needed. What is needed is a staggered freeze
  clock: monotone learning that excludes one level per search, top level first. The inversion holds then make every level
  above the freeze front toggle at every visit.

## 4. Traps found on the way (READING of dtl_pyref, the reference model)
- (T1) Within a search, sptl repeats to a fixpoint on a fixed V, and a bv call's attractors are transitive. So a dependency
  "learn A, then B" collapses into ONE search unless it passes through a new bv call (V or context) or through W. The
  chainfam clock gets its one-search delay from the shrinking context R after the -1 branch, not from region steps.
  Its signal reaches root regions only through an added top (S above).
- (T2) An opponent vertex counts a successor in an EARLIER region as satisfied (attractVertices skips only successors in Gx
  outside Z). So when a stolen tangle loses one vertex, the rest of it usually re-enters the same region by plain attraction,
  and the release never reaches the levels below.
  - DATA, stealonce_viol_n76: the vertices of its depth-1 re-stolen tangle t7 lie in every lower prefix of round 4 at all
    visits 1-8.
  - experiments/red/lag/l2predict.py (every step x vertex pair, both orders) finds no added level with depth >= 2 on
    stealonce_viol_n76 or stealonce_core_n76.
  - A first freeze through v_j failed for the same reason (y_j was re-attracted).
- (T3) Odd tops that point into the clock are pruned in bv. The level tangles must still be learned at search 0. The
  climbed control wiring solves this; a hand rule for it is not yet written.

## 5. Depth grows with the number of levels (DATA, 03:00Z by date -u)
- The same skeleton (lag4.build(D) plus 3 helpers) was climbed separately for each D with schemaclimb.py (seeds 303 and 304,
  about 200 steps each). Every row below was checked with L-ALG's dtl_stealdepth.py UNMODIFIED, both order data, and with
  pinned Oink:

  | D | file (sha1) | n | max depth (stable / oink) | max k | Oink iterations | dtl_flipflop vs Oink |
  |---|---|---|---|---|---|---|
  | 2 | depth2_n39.pg (6200e5869e8f) | 39 | 2 / 2 | 2 | 10, verified | MATCH |
  | 3 | depth3_n46.pg (54cc8526238e) | 46 | 3 / 3 | 2 | 11, verified | MATCH |
  | 4 | depth4_n53.pg (40dacf0e4b6f) | 53 | 4 / 4 | 3 | 12, verified | MATCH |

- Depth = D on n = 7D + 25 vertices, and max k reaches 3. Iterations grow by one per level.
- So (STEAL-DEPTH_D) with D constant (RESULTS R12, Lemma CHARGE) fails on this sequence if the sequence continues.
- What this is NOT:
  - It is not a uniform family yet. The control wiring was climbed separately for each D.
  - It is not a running-time kill: iterations are linear.
- Next: climbs at D = 5 and 6 (running), and a hand rule for the control wiring (T3) that makes the family uniform.
