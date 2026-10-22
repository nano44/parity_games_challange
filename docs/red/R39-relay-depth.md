# R39: an inversion relay driven by a region clock: re-steal depth D on 7D + 22 vertices (L-RED box 10; produced on Opus 5.5)
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

## 6. UNIFORM family: depth = D on n = 7D + 22 (DATA, 03:11Z by date -u; first pushed with the wrong label "03:25Z")
- experiments/red/lag/lagfam.py D is the lag4 skeleton with the fixed control rule T_j -> {x_1, tau_j} and no helpers.
- Why the rule works (READING of the search_rec trace, srtrace.py):
  - At root round 1 the clock tops lie BELOW the relay tops. So T_j's edge x_1 points into a later region: T_j stays open
    and is not absorbed.
  - Once the clock part is in X, x_1 is outside R. The relay context's bv then keeps the T_j and the tau_j (T_j's other edge
    tau_j is in Z), returns 1, and sptl learns every t_j in search 0.
  - The bigger tangle {T_j} + t_j learned in pass 2 escapes only to x_1. At root, x_1's region (bound pr x_1 = 0) cannot
    attract it, so it is inert.
- experiments/red/lag/famsweep.sh: L-ALG dtl_stealdepth.py UNMODIFIED, both order data (identical output), pinned Oink:

  | D | n | sha1 | max depth | max k | Oink iterations | dtl_flipflop vs Oink |
  |---|---|---|---|---|---|---|
  | 2 | 36 | 7d7503055ee4 | 2 | 2 | 10, verified | MATCH |
  | 3 | 43 | 2d2f5386d31d | 3 | 3 | 11, verified | MATCH |
  | 4 | 50 | c8fd86165aba | 4 | 3 | 12, verified | MATCH |
  | 5 | 57 | 53722330f56b | 5 | 4 | 13, verified | MATCH |
  | 6 | 64 | cdf8790a1fae | 6 | 4 | 14, verified | MATCH |
  | 8 | 78 | 46ad828c7901 | 8 | 5 | 16, verified | MATCH |
  | 10 | 92 | 96c73fb8578b | 10 | 6 | 18, verified | MATCH |
  | 12 | 106 | 0dd2899eacfe | 12 | 7 | 20, verified | MATCH |
  | 16 | 134 | a35ddaf9887e | 16 | 9 | 24, verified | MATCH |
  | 20 | 162 | 3afbe4405e3f | 20 | 11 | 28, verified | MATCH |

- Observed: depth = D, max k = floor((D+1)/2) + 1, and iterations = D + 8, for every D tested up to 20.
  The rows for D = 16 and 20 were added at 03:28Z (date -u).
- At D = 2 and D = 3 the observed F/X table at the steps (1, T_j) equals the schema of section 3 cell for cell
  (schemashow.py). The depth-D re-steal sits at level D, pair D + 2, with a single cause: level D - 1 at pair D + 1, of
  depth D - 1.
- Pinned in experiments/red/check.sh:
  - lagfam.py regenerates D = 4, 8, 12 byte for byte (instances/fam_D4_n50, fam_D8_n78, fam_D12_n106);
  - sha1 and dtl_flipflop line for each;
  - in-tree experiments/alg/dtl_stealdepth.py (identical to l-alg e0fc1bb0) gives "max k 3; max depth 4" on fam_D4 in both
    order data.
- Consequences (L-RED reading; the statements are L-ALG's and the Lead's to restate):
  - (STEAL-DEPTH_D) with D CONSTANT is false. That is the premise of the Lemma CHARGE route in RESULTS R12, so the route
    is dead as stated. R37-1 (depth <= V - 3) is not contradicted: the context has D + 6 visits.
  - Re-steals per q are unbounded: max k grows like D/2. Any constant-k form (STEAL-ONCE*-type) fails on this family too.
    STEAL-POLY_sum (R12's main route) is NOT refuted: k <= n here, and the phase is linear.
  - Not a running-time kill: Oink iterations are D + 8.

## 7. The same family breaks (EXIT_c) for constant c; (CTX+) unaffected (DATA, 03:20Z by date -u)
- L-ALG experiments/alg/dtl_prefexits.py UNMODIFIED (RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0), BOTH order data (identical):

  | D | n | max exits per (context, step, vertex) | exit distribution | max total exits per context / abs R |
  |---|---|---|---|---|
  | 2 | 36 | 2 | 1: 17, 2: 4 | |
  | 4 | 50 | 3 | 1: 29, 2: 17, 3: 4 | 1.5 (75 exits, abs R 50, 11 visits) |
  | 6 | 64 | 4 | 1: 41, 2: 29, 3: 17, 4: 4 | |
  | 8 | 78 | 5 | 1: 53, 2: 41, 3: 29, 4: 17, 5: 4 | |
  | 12 | 106 | 7 | | 7.59 (805 exits, abs R 106, 19 visits) |

- Max exits = D/2 + 1 for even D. Re-entries reach the same counts: membership patterns like 0101010000000 are a vertex
  ticking once per toggle of the level above.
- (EXIT_c) with c CONSTANT is false. RESULTS R13's premise (EXIT_c; DATA "c = 2 on all data") fails at fam_D4_n50
  already (c = 3). This is the gadget L-ALG described in §23w-§23x: one vertex's prefix membership ticks like a counter bit.
- Total exits per context grow faster than abs R (75 to 805 for D 4 to 12), but they stay polynomial.
- dtl_rootmono.py UNMODIFIED, both orders: 1 distinct first-difference context per phase (10 / 14 / 18 transitions at
  D = 4 / 8 / 12). Everything happens in the root context, so the family says nothing about (CTX+). The serialized-piece
  question of R38 stays open.

## 8. Totals on the family against n (DATA, 03:35Z by date -u): all polynomial
- Tools, both order data (identical output):
  - Σ_q k_q per (context, phase): experiments/red/lag/sumk.py, a count of dtl_stealdepth.analyze's own events. Only the
    count is mine; the run is the unmodified L-ALG model.
  - #fired⁺(R), D_R and (CHANGE-NEW): L-ALG experiments/alg/dtl_changenew.py UNMODIFIED.
  - Total exits per context: dtl_prefexits.py UNMODIFIED (section 7).
  - Contexts: dtl_rootmono.py UNMODIFIED.
- The maximum is in the root context in every row:

  | D | n | max Σ_q k_q (distinct q) | max #fired⁺(R) | max D_R | total exits per context | S (searches in the phase) | first-difference contexts / transitions |
  |---|---|---|---|---|---|---|---|
  | 2 | 36 | 6 (4) | 12 | 8 | 25 | 9 | |
  | 4 | 50 | 12 (6) | 16 | 10 | 75 | 11 | 1 / 10 |
  | 6 | 64 | 20 (8) | 20 | 12 | 166 | 13 | |
  | 8 | 78 | 30 (10) | 24 | 14 | 310 | 15 | 1 / 14 |
  | 10 | 92 | 42 (12) | 28 | 16 | | 17 | |
  | 12 | 106 | 56 (14) | 32 | 18 | 805 | 19 | 1 / 18 |

  The total-exits entries for D = 2, 6, 8 are the Lead's re-run (03:43Z message); the rest are mine.
- Closed forms on this data:
  - Σ_q k_q = (D/2 + 1)(D/2 + 2), quadratic in n;
  - #fired⁺ = 2D + 8 and D_R = D + 6, both linear;
  - total exits per context: 75 / 310 / 805 at D = 4 / 8 / 12, local exponents 2.0 to 2.4 in D (polynomial; a 03:35Z
    draft said "about cubic", which overstated it). D_R ≤ #fired⁺(R) holds on every row;
  - S = D + 7 searches (Oink: D + 8 iterations);
  - first-difference contexts per transition: 1 / (D + 6), falling.
- (CHANGE-NEW) holds, and N*_R ≤ D_R holds, on every row (dtl_changenew).
- So on this family no total grows super-polynomially. The R12 main route (STEAL-POLY_sum) and the R14 route (FIRED⁺-R)
  are untouched. Only the constant-bound forms die: STEAL-DEPTH_D (section 6) and EXIT_c (section 7).
- Box item (3), long-phase FIRED-R with multi > 0: not reachable with this family. S = D + 7 is below 2 abs R = 14D + 44,
  so the root context never passes the S >= 2 abs R filter.

## 9. Box order (c), first-difference contexts: status at 03:44Z (date -u). Not achieved; what a construction must satisfy
- DATA:
  - lagfam has 1 first-difference context per phase at every D (section 8).
  - Disjoint stacks of two copies with different D (experiments/red/lag/stack.py; D 2+4 and 4+2, n 86) also give 1 context
    in 10 transitions (dtl_rootmono UNMODIFIED, stable).
  - Depth there is 4 (the larger copy). The copies run in lockstep, as R38 found for unions.
- READING:
  - The first difference of a transition is the first tattr log entry whose first four fields differ: caller, depth, Z in,
    Z out (experiments/alg/dtl_fdlcheck.py CK.tattr and reduce_log).
  - So a transition's first difference leaves the root call only if EVERY tattr of the root call returns the same Z.
    This covers the round regions, the bv threshold loop ("bv-thr", consume None) and the root's sptl, dom and -1 entries.
  - In lagfam this fails by design: S's round-1 region grows at every visit.
- Necessary condition for a serialized piece U whose learning sits in a lower context C (depth 0 after a dom, or depth >= 1):
  every tangle U learns between two visits must leave every tattr Z of the earlier calls unchanged.
  - In a round region, its trigger escape must not be popped, or it must be excluded.
  - In the threshold loop (no consume, bound up to the maximum priority), some escape must stay outside Z_t at every
    threshold. So U's tangles need an escape into a part the root's threshold attractor never reaches, or the root must
    return 1 at round 1, before any threshold loop.
  - ctx13_n40 meets this for 16 of its 24 transitions: their first differences are in depth-0 calls of abs R 26-39.
- Not built in this box (context budget). For a successor: a relay unit placed in a context where the root returns 1 at
  round 1, with its clock's tangles escaping only into vertices the root call never attracts.
- Probe (03:49Z date -u), experiments/red/lag/hideclk.py k = 8: every x_j gets an extra edge to an Odd-won vertex o
  (o -> W), so the clock tangles carry an escape the root's threshold attractor can never contain.
  - Result, with o at priority 1 and at priority 2k + 3 alike: tangles are learned in ONE search only. The clock dies, because
    o lies inside the learning context, neither consumed nor in Z.
  - This sharpens the condition above. The hiding escape e must be outside the root's Z_t at every threshold, AND, in the
    learning context C, either consumed by an earlier region of C or outside R_C.
  - Regions and X are Even attractors, so a vertex that Even can never attract in G' meets the second clause only through
    "outside R_C". C must then be a subgame that excludes e: a depth >= 1 recursion of the -1 branch, or a depth-0 call
    after e was consumed in a way the root's threshold loop does not repeat.
  - chainfam learns at depth 0 (its depth-1 subgames are empty in srtrace). So its clock cannot simply be hidden; a hidden
    clock has to learn inside a nonempty -1 subgame.
  - Lead reading needed: whether this is worth a successor box (R38 question, the one premise shared by the live routes).
