# R37: what a re-steal chain of depth D needs (L-RED box 8; produced on Opus 5.5)
Status: READING (proof by reading the definitions; unrefereed) plus DATA. It is written for L-ALG and the Lead, Lead 21:33Z:
"write it up as a precise statement, whichever way it goes". Target: (STEAL-DEPTH_D), D constant (RESULTS R12, GAP-A-M §23g).

## Definitions used (exactly those of L-ALG's experiments/alg/dtl_stealdepth.py, l-alg 931fc221, analyze())
- One context key = (depth, R) and one phase. Visits x_0, x_1, ... are the context's best_vertices calls in call order. Pair i
  is (x_i, x_{i+1}).
- An EVENT e = (i, k, t) sits at pair i, step k = (round, top), tangle t. Conditions: t ∈ F_k(x_i) (it fired at k), t was not
  excluded at k in x_i, and t is excluded at k in x_{i+1} (met but not contained by P_{x_{i+1}}(k)). Here q(e) = (k, t).
- The first event of q has depth 0. Take a later event e = (i, k, t) of q whose previous event of q is at pair j < i.
  - Its CAUSES are the events c = (m, k', t') with j < m < i, k' strictly earlier than k, and t ∩ P(k) losing a vertex at
    pair m.
  - depth(e) = 1 + min depth over its causes. With no cause the tool prints "no cause" and gives no depth.

## Statement R37-1 (chain): a depth-D event needs D + 3 visits and D + 1 strictly ordered steps
Let e_D be an event of depth D ≥ 1. Then there are events e_0, e_1, ..., e_D = (i_j, k_j, t_j) with:
- (a) i_0 < i_1 < ... < i_D;
- (b) k_0 ≺ k_1 ≺ ... ≺ k_D, strictly earlier steps (rounds ascending, tops descending), so D + 1 distinct steps;
- (c) depth(e_j) = j, and every e_j with j ≥ 1 is a re-steal of q_j = (k_j, t_j). The previous event of q_j is at a pair
  p_j < i_{j−1}, so i_0 ≥ 1 and i_D ≥ D + 1. Hence the context has at least D + 3 visits in the phase.
Proof (reading). depth(e_j) = 1 + min over the causes of e_j, so some cause e_{j−1} has depth j − 1. By the cause
definition, p_j < i_{j−1} < i_j and k_{j−1} ≺ k_j. Induct down to depth 0. Then i_0 > p_1 ≥ 0 and i_j ≥ i_0 + j.
- (d) Tightness of the count (combinatorial only, not a construction). The pattern "every q_j (j ≥ 1) first stolen at pair 0;
  e_0 at pair 1; the stealing vertices of q_j leave P(k_j) at pair j (by e_{j−1}); q_j stolen again at pair j + 1" meets
  (a)-(c) with exactly D + 3 visits. Each level must be RE-STOLEN one pair after its cause: at visit i_{j−1} + 1, t_j is
  disjoint from P(k_j) and fires at k_j again; at visit i_{j−1} + 2 it is met again.

## Statement R37-2 (learning): every event pair needs a tangle learned in between
Reading. Within a phase the context's best_vertices call is a function of R, the searching player and the stored tangle
list. Consecutive visits with no new tangle between them record identical regions, fired sets and exclusions, so the pair
carries no event. Hence the D + 1 pairs i_0..i_D, and the pairs p_j, are each separated by at least one learned tangle.
- Gap: this uses the fleet's determinacy reading. Same arena and same tangle list give the same best_vertices records;
  0 exceptions in DATA, and STR-DET (RESULTS R11) covers the extracted SCCs. It is NOT proved here for the record fields
  pref/excl/fired.

## Consequence for the (STEAL-DEPTH) route (L-RED reading)
- depth ≤ V − 3, where V is the largest number of visits of one context in one phase. If every context were visited at most
  once per search, this would give depth ≤ S − 3 ≤ |G'| − 3 under the DATA statement (SPP) S ≤ |G'| (GAP-A-M §21a).
  Contexts can, however, be visited several times in one search: search_rec calls best_vertices again with the same R after
  each res = 1 round (dtl_pyref 260-296), so V is not bounded by S.
- So R37 gives a LINEAR bound on depth, not a constant one. A constant D needs an argument that a context's visits in which
  a NEW level becomes active are boundedly many. Equivalently: why can the pairs i_0 < ... < i_D not all lie at strictly
  ordered steps?
- What the attack must build for depth D: D + 1 nested steps in ONE context and ONE phase, and a cascade that moves down
  one step per visit pair. Level j's stealing vertices leave P(k_j) exactly when level j − 1 is re-stolen, and level j is
  re-stolen at the next pair. Each pair needs a new tangle (R37-2), so the phase must keep learning for D + 1 consecutive
  visits while the context stays the same.

## DATA behind the reading (all stable unless noted; L-ALG tools unmodified)
- Every re-steal found so far has depth 1, and its cause is a depth-0 steal at the next higher step. Instances:
  - stealonce_viol_n76 (R35): 1 re-steal, phase 9 searches;
  - stealonce_core_n76 (R36 §1): 2 re-steals, phase 4 searches;
  - stealonce_both_n45 (R36 §5): 2 re-steals in both orders, phase 4 searches.
- Searches, 19:47Z-22:00Z (date -u), max depth 1:
  - about 2,000 one-edge variants (R35 game, core, 45-vertex core);
  - stealk/depth hill climbs in both orders.
- In these instances the cascade has exactly two active levels. The phases (4-9 searches) learn their last tangle that
  touches the context by search 6 at the latest, so (R37-1 (c)) leaves no room for depth 2 inside them.
