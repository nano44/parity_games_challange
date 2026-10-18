# R40: a one-edge-class perturbation of Two Counters, tcL(N): first-difference contexts = S − 3 per phase (L-RED box 11; produced on Opus 5.5)
Status: DATA plus READING, unrefereed. No kill, no super-polynomial family, no incorrect run. Targets: Lead box-11 item (1)
((CTX⁺) serialized contexts), the R38 question, and the Lead's side check on L-ALG's TC-6 (GAP-A-M §25a).
Started 2026-10-18 09:16Z (date -u). Tools: L-ALG's tools from a detached claude/l-alg checkout at 11d89e20 (LALG_DIR), imported
UNMODIFIED; pinned Oink tools/oink/build/oink @ 8fbf0a7 (scripts/setup_oink.sh), `--dtl --no-single --no-wcwc --no-loops -v`.

## 1. Result
- tcL(N) := Oink's tc(N) (tools/oink/build/tc N, pinned) plus, for every i ≥ 1, an edge from the vertex labelled Even-i-L to
  the vertex labelled Even-(i−1)-H. Generator: `experiments/red/tcpert/tcpert.py tcL N OUT.pg` (calls the pinned tc binary).
  The rule is uniform in N; it adds N − 1 edges. n(tcL(N)) = n(tc(N)).
- Pinned Oink, every N tried, solution verified:

  | N | n | iterations (Even + Odd) | tangles | dominions | tc(N) iterations / tangles |
  |---|---|---|---|---|---|
  | 3 | 42 | 6 (4 + 2) | 7 | 2 | 6 / 7 |
  | 4 | 68 | 6 (4 + 2) | 10 | 2 | 6 / 9 |
  | 5 | 100 | 7 (5 + 2) | 13 | 2 | 6 / 11 |
  | 6 | 138 | 8 (6 + 2) | 16 | 2 | 6 / 13 |
  | 8 | 232 | 10 (8 + 2) | 22 | 2 | 6 / 17 |
  | 10 | 350 | 12 (10 + 2) | 28 | 2 | 6 / 21 |
  | 12 | 492 | 14 (12 + 2) | 34 | 2 | 6 / 25 |

  Iterations N + 2 also at N = 7, 9, 11, 13, 14, 16 (verified; files not kept). So tcL has 3N − 2 tangles and N + 2 searches
  for N ≥ 4: linear, not constant. The reference model (experiments/red/dtl/dtl_flipflop.py) gives the same counts at N 4, 6, 8.
- First-difference contexts (C_bv, the dtl_rootmono / root/ctxtrace.py rule), Even phase 0:

  | N | S (phase 0) | transitions | distinct contexts | stable | Oink order | tool |
  |---|---|---|---|---|---|---|
  | 4 | 3 | 2 | 1 | yes | yes | ctxfit (full sets) |
  | 6 | 5 | 4 | 2 | yes | yes | ctxfit |
  | 8 | 7 | 6 | 4 | yes | yes | ctxfit |
  | 10 | 9 | 8 | 6 | yes | yes | ctxlight |
  | 12 | 11 | 10 | 8 | yes | yes | ctxlight |

  Sequence at N = 12 (depth / |R| / context id / caller): 0/492/C0/bv-thr, 0/492/C0, then 0/369/C1, 0/387/C2, 0/404/C3,
  0/420/C4, 0/435/C5, 0/449/C6, 0/472/C7, then 0/492/C0. Every middle transition has its first difference in a NEW depth-0
  best_vertices call whose arena grows by 12-23 vertices per search. All callers are bv-thr; no e* at depth ≥ 1.
- So on tcL, distinct first-difference contexts per phase = S − 3 = N − 4 (N ≥ 6): contexts per transition (N − 4)/(N − 2) → 1.
  This answers the R38 question on a uniform family: the ratio is NOT bounded away from 1, let alone from 0, so (CTX⁺) has
  no bound independent of S. Proving (CTX⁺) on a family is as hard as bounding its phase length. It does not refute (CTX⁺):
  everything here is linear.

## 2. Tools and how they were checked
- experiments/red/ctxp/ctxfit.py: the root/ctxtrace.py rule as a function (L-ALG dtl_rootmono.RM, dtl_fdlcheck.reduce_log
  imported unmodified; first log entry differing on its first 4 fields; context = the best_vertices record holding it).
- experiments/red/ctxp/ctxlight.py: the same run with each tattr log entry storing hashes of its input and output sets. Needed
  because ctxfit (full frozensets per entry) is OOM-killed at N = 10 (about 6 GB; 09:36Z with two runs at once, 09:47Z alone). Validated: identical output
  to ctxfit on tcL N = 4, 6, 8. A hash collision could only hide a difference.
- Both orders: DTL_ORDER=stable and DTL_ORDER=oink (the L-ALG order emulation of pinned Oink).

## 3. Reading (L-RED): where the contexts come from
- The Even counter of tcL(N) is learned top bits first, then one lower bit per search (experiments/red/lag/learn.py on tcL_N6:
  search 0 learns tangles on the Even-5/4 bits, search 1 the Even-3 cycle, search 2 the Even-2 cycle, search 3 Even-0). In tc(N)
  the bits are learned in 3 Even searches for every N; the added edges Even-i-L -> Even-(i−1)-H serialize them. (This is a
  reading of one trace, not a proof.)
- Each search s ≥ 2 first differs in the depth-0 best_vertices call that follows the Dom of the bits learned so far, so its
  arena is G' minus a different, growing set. This is the "serialized pieces" shape R37/R38/R39 §9 asked for: the root call and
  the earlier depth-0 calls stay identical while a lower piece learns. It is obtained through the Dom sequence at depth 0, not
  through a −1 subgame.

- DATA (11:12Z by date -u; experiments/red/ctxp/d0calls.py, the reference model via a subclass hook): the depth-0
  best_vertices calls of each search on tcL(8), as |R|:result:
  ```
  search 0: 232:-1 224:1 115:-1 0:0
  search 1: 232:-1 231:-1 229:-1 221:1 217:-1 216:-1 207:-1 201:-1 200:-1 196:-1 191:-1 190:-1 184:-1 180:-1 179:-1 171:-1 168:1 116:-1 115:-1 0:0
  search 2: 232:-1 231:-1 228:-1 216:-1 215:-1 207:-1 201:-1 200:-1 196:-1 191:-1 190:-1 184:-1 180:1 116:-1 115:-1 0:0
  search 3: 232:-1 231:-1 228:-1 216:-1 215:-1 207:-1 201:-1 200:-1 196:-1 191:1 116:-1 115:-1 0:0
  search 4: 232:-1 231:-1 228:-1 216:-1 215:-1 207:-1 201:1 116:-1 115:-1 0:0
  search 5: 232:-1 231:-1 228:-1 216:1 116:-1 115:-1 0:0
  search 6: 232:1 116:-1 115:-1 0:0
  search 7: 116:-1 115:-1 0:0   (then the Odd searches)
  ```
  A staircase: each search walks a chain of depth-0 calls that return −1 (each followed by a Dom or a −1 recursion), and the
  first call that returns 1 (where sptl learns) moves up one rung per search: |R| 180, 191, 201, 216, 232. The first difference
  of transition s → s+1 is at the rung where search s+1 learns: the call that returned −1 in search s returns 1 in s+1, because of
  the tangle that s learned one rung lower (contexts |R| 191, 201, 216 in §1's N = 8 row; 232 is the root, C0). The number of
  rungs, and so of contexts, is the number of serialized bits.

## 4. Side check for the Lead: TC-6 is fragile
- L-ALG's TC-6 (GAP-A-M §25a) is about tc(N) itself, and nothing here contradicts it (pinned Oink: tc(N) 6 iterations, 2N+1
  tangles, N = 3..12, table above).
- But one uniform edge class added to tc(N) makes the search count N + 2. tcpert.py searched 3,000 one- or two-part label rules
  (owner flips, edge classes with index offset −1/0/+1, priority shifts ±2) at N = 3..6 (seed 1): no rule was unverified;
  growth is common; the fastest found was 1.5N + O(1) (rule prio Even-Z −2 plus edges Odd-i-S -> Odd-(i+1)-T: 5, 6, 8, 9, 11, 12,
  14, ... at N = 2..14). Nothing super-linear.
- Consequence for a TC-6 proof: it must use that tc(N) has no edge from a lower counter bit's L vertex to the next bit's H vertex;
  a trace argument that does not see that edge class would also "prove" 6 searches on tcL, which is false.

## 5. Depth >= 1 learning (Lead box item (1), first step; R39 §9)
- experiments/red/ctxp/instances/deep1_n13.pg (sha1 fa65aa1c971b): a tangle is born inside a search_rec call of depth 1 (search
  1: depth-1 call on 9 vertices; a −1, a Dom, a −1, then best_vertices returns 1 and sptl learns), in both order data
  (experiments/red/ctxp/depthscan.py, the reference model via subclass hooks). Pinned Oink: 4 iterations, 4 tangles, verified.
  deep1_n21.pg (398c2ecd) is a stable-order example. Found by random search (rsearch.py): 2 hits in about 400,000 random games (seeds 11, 12).
- The learned tangle is visible to the root: both transitions of that phase first differ in the root threshold loop (bv-thr).
- (DEEP-STAB), DATA: the FIRST best_vertices call of a −1 subcall never returned 1 in 700,000 random games (n 6-18, both orders;
  34,661 nonempty subcalls; lemmacheck.py seeds 21 and 22); later calls in a subcall returned 1 27 times.
- READING, two facts behind it:
  - (ODD-CLOSED), from search_rec's −1 branch (C5 §2; dtl_pyref search_rec): every opponent vertex w of the subgame Z_s has
    succ(w) ∩ R_P ⊆ Z_s, where R_P is the parent's arena. Reason: w was p-attracted (all successors in Z or outside R), and the
    opponent attractor to the threshold vertices removed every opponent vertex with a successor among the vertices moved to X.
  - So in Z_s the opponent has the same moves as in R_P, and p has fewer. If best_vertices' region union were monotone in the
    arena and in V, a set S of p-vertices that is stable in Z_s would never be pruned in R_P, contradicting the parent's −1.
    GAP in this argument: the union is NOT monotone in V in general, because a higher region can take part of a tangle, and a
    later region then cannot attract that tangle (dtl_pyref attractTangle rejects a tangle with a vertex outside CurR). So
    (DEEP-STAB) is DATA plus a proof sketch with this gap, not a lemma.
- Consequence for a hidden clock (R39 §9): its learning context at depth ≥ 1 cannot be the first call of the subgame; it needs a
  Dom inside the subgame and a later call. tcL shows that serialized contexts do not need depth ≥ 1 at all.

## 6. Other totals on tcL (DATA, 10:09-10:16Z by date -u; L-ALG tools unmodified, in-tree = l-alg 11d89e20; both orders identical)
| N | max k / depth (dtl_stealdepth) | max Σ_q k_q (red/lag/sumk.py) | max #fired⁺(R), D_R (dtl_changenew) | max exits (dtl_prefexits) |
|---|---|---|---|---|
| 4 | 0 / 0 | 0 | 4, 2 | none |
| 6 | 0 / 0 | 0 | 8, 3 | none |
| 8 | 0 / 0 | 0 | 12, 3 | none |
- No steal, no exit; #fired⁺(R) = 2N − 4 (linear); (CHANGE-NEW) and D_R ≤ #fired⁺(R) hold on every row. So tcL stresses only
  (CTX⁺): every other total is trivial or linear there.

## 7. Faster-growing perturbations of tc(N) (DATA, 10:17-10:20Z by date -u; pinned Oink, every solution verified)
- experiments/red/tcpert/tcclimb.py (hill climb over rule sets, fitness = iterations(N=7) − iterations(N=4)), seed 3:
  r4 = {edges Even-i-A -> Even-i-T; Even-S priority −2; Even-Z priority −2; edges Even-i-B -> Even-(i−1)-L}:
  iterations 7, 10, 15, 18, 25, 29, 37, 45, 59, 67 at N = 3..12 (tangles 10 ... 139). About N²/2, and since n ≈ 3.4N², about
  0.13 n: linear in n. The 3-part r3 (without the B -> L edges): 7, 9, 12, 14, 18, 19, 20, 24, 27, 29, 29, 32 at N = 3..14.
- tcclimb seeds 7 and 8, fitness min(it(8)/it(5), it(7)/it(4)), up to 6 rule parts incl. cut / self-loop rules (10:21-10:40Z):
  best ratios 2.0 and 4.0 come from small bases (2, 2, 3, 6, 9, 12 at N 3..8). The seed-8 rule {Odd-i-L -> Even-i-T, Odd-L owner
  flip, Even-B -> Odd-S, Odd-i-B -> Odd-(i−1)-T, Odd-T -> Odd-B, Even-B -> Odd-A} gives 3, 3, 4, 6, 9, 11, 14, 16 iterations at
  N 3..10: linear. Its pinned-Oink WALL TIME grows about 4x per N (0.14 / 1.3 / 7.0 / 29.6 s at N 6..9, n 138..288; tangles
  32 / 62 / 91 / 135). That is per-search cost (polynomial by C5 §2), not search count, so it is not a gauntlet failure; noted
  for the step-5 timing record only.
- Nothing super-polynomial in n. A climb for iterations EXPONENTIAL in N (which would be super-polynomial in n, since n is
  quadratic in N) is running (fitness iterations(8)/iterations(5), with cut and self-loop rules).

## 8. tcR4(N): first differences INSIDE −1 subgames (depth 1) while the root call is identical (DATA, 10:43-10:50Z by date -u)
- tcR4(N) := tc(N) with the four rules of §7's r4 (`tcpert.py tcR4 N OUT.pg`; instances tcR4_N4..N8, sha1 4e69bfd2,
  665e657a, 167e1e85, 887a3eb2, 6591768a). Pinned Oink, verified: iterations 10 / 15 / 18 / 25 / 29 at N 4..8 (Even 8 / 13 /
  16 / 23 / 27), tangles 17 / 27 / 35 / 49 / 59. dtl_flipflop at N 5: 27 tangles, 15 iterations (= Oink).
- First differences, Even phase 0 (ctxlight; at N 5 also ctxfit with full sets, identical):

  | N | n | S | transitions | distinct contexts | e* at depth 1 | order |
  |---|---|---|---|---|---|---|
  | 5 | 100 | 12 | 11 | 7 | 3 | stable = Oink order |
  | 6 | 138 | 15 | 14 | 10 | 6 | stable and Oink order (same counts, slightly different sequences) |
  | 7 | 182 | 22 | 21 | 14 | 10 | Oink order |
  | 7 | 182 | 20 | 19 | 13 | 8 | stable |
  | 8 | 232 | 26 | 25 | 18 | 13 | Oink order |
  | 8 | 232 | 25 | 24 | 18 | 13 | stable |

  N 8, Oink order: C0, then depth-1 contexts |R| 97, 113, 126, 136, then depth-0 |R| 225, then depth-1 112, 128, 172, 105, 123,
  140, 172, back to depth 0 225, depth-1 198, 198, then depth 0 225, 225, 232, then five new depth-0 contexts |R| 222..230, C0.
- So the R39 §9 condition is met on a uniform family: in 13 of 25 transitions (N 8) the root call and every depth-0 call are
  identical and the first difference lies in a best_vertices call at search_rec depth 1. depthscan at N 5, both orders:
  10 tangles born at depth ≥ 1, best_vertices returned 1 at depth ≥ 1 five times, (DEEP-STAB) held (FIRST-BV-1 0).
- Counts grow linearly in N (contexts 7, 10, 14, 18), so about sqrt(n), like tcL. Nothing super-polynomial.

## 9. Open, in this box
- N = 14 needs a lighter tool (ctxlight peaks above 5 GB at N = 12).
- The other totals on tcL (Σk, #fired⁺(R), D_R, exits) are not yet measured.
