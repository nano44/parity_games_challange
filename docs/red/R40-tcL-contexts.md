# R40: a one-edge-class perturbation of Two Counters, tcL(N): first-difference contexts = S − 3 per phase (L-RED box 11; produced on Opus 5.5)
Status: DATA plus READING, unrefereed. No kill, no super-polynomial family, no incorrect run. Targets: Lead box-11 item (1)
((CTX⁺) serialized contexts), the R38 question, and the Lead's side check on L-ALG's TC-6 (GAP-A-M §25a).
Started 2026-10-18 09:16Z (date -u). Tools: L-ALG's tools from a detached claude/l-alg checkout at 11d89e20 (LALG_DIR), imported
UNMODIFIED; pinned Oink tools/oink/build/oink @ 8fbf0a7 (scripts/setup_oink.sh), `--dtl --no-single --no-wcwc --no-loops -v`.

## 0. Summary (11:32Z by date -u)
Three uniform perturbations of Oink's Two Counters generator, all solved correctly by pinned Oink at every size tried:
- leanT(N) (§9), n = 8N: Even phase S = N, and EVERY transition has its own first-difference context (C_bv = S − 1 = n/8 − 1;
  N 6..32, both order data). The strongest (CTX⁺) data: no slack at all between (CTX⁺) and the phase length.
- tcL(N) (§1-3), n ≈ 3.4N²: C_bv = S − 3 = N − 4, through a "staircase" of depth-0 calls (§3).
- tcR4(N) (§8): first differences at search_rec DEPTH 1 with the root call identical (13 of 25 transitions at N 8), the
  R39 §9 condition met on a uniform family.
Everything is linear in n; nothing refutes (CTX⁺) or GAP-A. Side results: TC-6 is fragile under one edge class (§4); (DEEP-STAB)
data (§5); other totals trivial on these families (§6); perturbation climbs give at most about 0.13·n searches (§7); GAP-C
probe: 60,000 perturbed hard-family / tc games, all verified (§10).

## 1. Result (tcL)
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
- Structured games (11:52-12:33Z by date -u; experiments/red/ctxp/lemmatc.py): 10,000 random tcpert rule sets (cut / loop
  included) on tc(4) (1,500 stable + 1,500 Oink order), tc(5) (4,000 stable), tc(6) (3,000 Oink order): 286 games learn tangles
  at depth >= 1 (1,113 births), 0 (DEEP-STAB) violations. tcR4 N 5..8, both orders: 0 violations (§8).
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

## 9. leanT(N): every transition of the phase has its own first-difference context; n = 8N (DATA, 11:12-11:14Z by date -u)
- lean base (experiments/red/tcpert/lean.py): tc(N) with every S/A/B vertex deleted (an edge into X-i-S-j is redirected to
  X-i-Z, other edges into deleted vertices are dropped). n = 8N. On the base alone pinned Oink needs 3 iterations at every N.
- leanT(N) := lean base + edges Even-i-T -> Even-(i+1)-L (`tcpert.py`'s rule "leanT"; `lean.py N OUT.pg leanT`; found by
  tcclimb.py on the lean base, seed 13, step 2). Instances leanT_N6/8/12/16/24/32 (sha1 f037844a, 5b5ab3ee, 604b3497, 341f92ce,
  739b03f4, c66aea08).
- Pinned Oink, verified: iterations N + 2 at N 6, 8, 12, 16, 24 (8, 10, 14, 18, 26); tangles 27 / 44 / 90 at N 6 / 8 / 12
  (dtl_flipflop: the same).
- First differences, Even phase 0 (S = N), both order data, identical:

  | N | n | S | transitions | distinct contexts | tool |
  |---|---|---|---|---|---|
  | 6 | 48 | 6 | 5 | 5 | ctxfit (full sets) and ctxlight |
  | 8 | 64 | 8 | 7 | 7 | ctxfit and ctxlight |
  | 12 | 96 | 12 | 11 | 11 | ctxlight |
  | 16 | 128 | 16 | 15 | 15 | ctxlight |
  | 24 | 192 | 24 | 23 | 23 | ctxlight (11:30Z) |
  | 32 | 256 | 32 | 31 | 31 | ctxlight (11:30Z); pinned Oink 34 iterations, verified |

  N 12 sequence: depth-0 bv-thr contexts with |R| 56, 60, 64, ..., 92, 96: the arena grows by 4 (half a bit) per transition, the
  last one is the root.
- So distinct first-difference contexts per phase = S − 1 = n/8 − 1: linear in n, one new context for EVERY transition. This is
  the extreme case of the R38 question: (CTX⁺) is exactly as hard as bounding the phase length on this family.

## 10. GAP-C probe (DATA, 10:42-11:10Z by date -u)
- experiments/red/tcpert/hfpert.py seed 2: 40,000 random games, each one of Oink's hard-family generators (counter_core, _dp, _m,
  _ortl, _qpt, _rob, _rr, _symsi, tc, tc+; sizes 1-4) with 1-4 random changes (add an edge, flip an owner, shift a priority):
  pinned Oink DTL with -v, all 40,000 "solution verified".
- tcpert.py seed 2 with cut / self-loop rules (TCP_EXT=1): 20,000 rule draws on tc(N), N 3..6: no unverified run. Earlier
  seeds (0, 1) and all climbs: no unverified run either.

## 11. L-ALG's live checkers on the new instances (DATA, 11:31-11:34Z by date -u; in-tree = l-alg 11d89e20, unmodified)
- Instances leanT_N6, leanT_N8, tcL_N4, tcL_N6, tcR4_N4, tcR4_N5, deep1_n13; both order data; RM_DV=0.
- dtl_fdlcheck.py (First-Difference Lemma): 0 violations on every instance (rc 0).
- dtl_rootmono.py (RM_EXCL=1 RM_PREF=1, ideal checks on): the only FAILS lines are statements already dead: CTX-ROOT (RESULTS
  DE17) on leanT 6/8 and tcR4 5; CHAIN (DE16) at depth 0 on tcR4 4/5 and at depth > 0 on tcR4 5; ABS-pw (dead, not a hit) on
  tcL 4/6 and tcR4 4/5.
- dtl_changenew.py, dtl_defsplit.py, dtl_quietlin.py: no failure line. No live lemma is broken by these families.
- Repeated 11:39-11:48Z on leanT_N12, leanT_N16, tcR4_N6, both orders: FDL 0 violations (11 / 15 / 15 transitions); again only
  CTX-ROOT, CHAIN and ABS-pw fail.

## 12. Item (2), long phase: NOT achieved; what was tried (DATA, 11:45-13:10Z by date -u)
- Learned-TANGLE climbs (C5 §4: A_DTL is polynomial iff the number of learned tangles is). tcclimb.py with TCC_METRIC=tangles on
  the lean base, seed 15, from leanT: best rule gives tangles 48 / 93 / 156 / 234 / 436 / 706 at N 12 / 16 / 20 / 24 / 32 / 40
  (n = 8N; searches N − 2): about 0.44 N², quadratic. leanT itself: 27 / 44 / 90 at N 6 / 8 / 12 (quadratic).
- Shape of every structured family found: nested chains. On leanT search k learns tangles extending a chain by bit k
  (lag/learn.py on leanT(3): {E0}, {E1}, {E1, E0}, then {E2}, {E2, E1}, {E2, E1, E0}). A counter needs a rung RE-learned with a
  new tangle after a higher rung advances; none of these families does that.
- Width is NOT an obstruction (experiments/red/ctxp/width.py, tangles learned per phase, largest ⊆-antichain): leanT N 8 / 16:
  width 8 / 16 = S; lagfam D 12: 32 tangles, width 32 (pairwise incomparable); ctx13_n40 Odd phase: 87 tangles, width 15.
- Products of staircases (experiments/red/tcpert/prodclimb.py): disjoint union of leanT(a) and leanT(b), copy 2 shifted up,
  climbing ≤ 8 individual cross edges on pinned-Oink iterations (all verified). The union alone runs in lockstep (6 / 8 / 10
  iterations at a = b = 4 / 6 / 8). Best with cross edges: 19 (a = b = 4, n 64), 24 (6, 6; n 96), 29 (8, 8; n 128; climb ended by its
  2000 s timeout at 13:22Z). Above a + b + 2, but growing slowly with the size, not like a product (a·b = 16 / 36 / 64). Every
  run verified.

- Compounding (Lead 12:11Z / L-ALG §29 (b)) on leanT: it cannot carry, and the trace shows why (ctxp/d0calls.py on leanT_N8):
  ```
  search 0: 64:-1 63:-1 61:-1 ... 40:-1 39:-1 37:-1 36:1 33:-1 32:-1 24:-1 21:-1 ... 3:-1 0:0
  search 1: 64:-1 ... 41:-1 40:1 32:-1 24:-1 ... 3:-1 0:0
  ...
  search 6: 64:-1 63:-1 61:-1 60:1 32:-1 24:-1 ... 0:0
  search 7: 64:1 32:-1 24:-1 ... 0:0
  ```
  The −1 prefix above the rising rung is identical in every search. The stable (learning) call rises one rung per search
  (|R| 36, 40, 44, ..., 64). Its Dom then swallows EVERY lower rung in one piece: the next depth-0 call is always |R| 32. The
  tail below 32 is the Odd side, identical in every search, and it learns nothing in Even's phase. So no rung below the rise
  point is ever re-cut and re-visited as a fresh context. The state of the lower rungs survives as a SUB-CHAIN of the new
  tangle ({E_j, ..., E_0} contains {E_(j−1), ..., E_0}), not as something reset. Condition (b) fails: nothing is learned in a
  fresh tail below j after the rise, so nothing can fire high later. Each rung rises exactly once (−1 -> 1).
  What a counter needs is the opposite: after the rise at j, Dom(stable piece at j) must NOT contain the rungs below j, so they
  remain a separate tail that is re-cut and must re-learn. Not built in this box.

## 14. Wall time on the seed-8 rule (Lead 11:04Z / 12:17Z; DATA 13:41-13:50Z by date -u)
- tcS8(N) = tc(N) + the §7 seed-8 rule (`tcpert.py tcS8 N OUT.pg`). Instances tcS8_N6..N11: sha1 d0424940f2d6, c10237a75021,
  1a7ba80f5dc4, 6b5f47892aa0, 60eaa4e79e6a, 0df9ed4cf315.
- Pinned Oink WITHOUT -v (no verification, no tracing): wall 0.16 / 1.33 / 6.55 / 29.5 / 102.9 s at N 6..10 (n 138 / 182 /
  232 / 288 / 350); iterations 6 / 9 / 11 / 14 / 16; tangles 32 / 62 / 91 / 135 / 176. Per-N ratios 8.2, 4.9, 4.5, 3.5: FALLING.
  N 11 not run (estimated > 5 min).
- Counters in the reference model (experiments/red/ctxp/d2count.py, dtl_pyref unmodified via hooks, Oink order; the model's
  searches and tangles equal Oink's):

  | N | n | search_rec calls | max depth | best_vertices calls | sptl calls | tattr calls | vertex pops | attractTangle calls | tangle-vertex scans | dup-key comparisons |
  |---|---|---|---|---|---|---|---|---|---|---|
  | 6 | 138 | 43 | 2 | 131 | 39 | 21,837 | 846,259 | 1,884,445 | 90,113,014 | 528 |
  | 7 | 182 | 69 | 2 | 224 | 72 | 62,904 | 2,693,901 | 13,337,907 | 917,770,088 | 1,953 |
  | 8 | 232 | 91 | 2 | 317 | 103 | 117,282 | 6,554,366 | 52,883,955 | 4,785,387,135 | 4,186 |
  | 9 | 288 | 122 | 2 | 445 | 150 | 212,454 | 14,607,811 | 185,711,021 | 21,488,041,025 | 9,180 |

  Ratios N 8->9 (box 12, 14:35Z): search_rec 1.34, bv 1.40, tattr 1.81, pops 2.23, attractTangle 3.51, scans 4.49.
  Peak RSS of pinned Oink (getrusage of the child, no -v): 11.2 MB at N 6, 11.3 MB at N 7..10; wall 0.2 / 1.4 / 7.2 / 33.2 /
  105.3 s at N 6..10 in that run. Ratios N 6->7 / 7->8: search_rec 1.6 / 1.3; best_vertices 1.7 / 1.4; tattr 2.9 / 1.9; pops 3.2 / 2.4; attractTangle calls
  7.1 / 4.0; tangle-vertex scans 10.2 / 5.2. Every ratio falls.
- The term that carries the wall time is the tangle-attractor scan: attractTangle calls (one per tangle having the popped
  vertex as an escape) times the tangle's size. With |T| = 32..91 tangles of size up to about n, this is at most
  pops × |T| × n, inside D2's per-iteration form O((n + |T|)(m + Σ|t|) d). Local exponent in n: about 8.4, then 6.8. It is a
  high-degree polynomial, not an exponential, and not an Oink artefact (the model shows the same growth). No D2 counter grows
  exponentially on this data.
- tcL N ≥ 14 and tcR4 N ≥ 9 need a lighter context tool (ctxlight peaks above 5 GB at n ≈ 490).
- (DEEP-STAB): close the tangle-split gap (§5) or find a counterexample.
- Item (2): a staircase whose rungs are RE-learned with new tangles after a higher rung advances (§12).
