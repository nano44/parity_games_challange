# Box 147 N5-COARSE: no coarse Ξ-statistic found. Every candidate the Lead named and 34 more are DEAD (per run and as «any function of the feature», all-start graphs). The Ξ-better-face vector and the merge vertices do not change across R189's realised unchained step (lag1, d 3). PROVED (lane): Lemma DECREMENT: at every step the highest-π mover becomes stable and no unstable bit above it changes. So the unstable set, read as a binary number in π order, falls at EVERY step. That is the exact (exponential) energy, and its poly truncations need unbounded depth
L-NEW successor 49, 2026-11-02 (date -u: see the commit). Lead brief 11:47Z (box 147: a COARSE Ξ-statistic with polynomially many levels
that falls at every unchained step and never rises at a chained one; test every candidate on every genome; else state the minimal
distinguishing information). Labels: PROVED (lane), DATA, DEAD, READING, CONJECTURE. U-LIN, IDEAL-ACYC-POLY and G-N5-TIME stay OPEN.
Not a TARGET.md claim.

Model: as box 144/146 (R178 §1 IDEAL rule, acyclic Ξ-graph, 2-wide deg-2 ladders in the R188 genome format unless said otherwise).
- π: a topological order of the Ξ-graph (Ξ-edges go forward; the genome's xorder).
- fv(x, k): the value of face (x, k) under state s (fastcyc_r178).
- B(x): the Ξ-better option.
- UNST(x) = [B(x) ≠ s(x)]: x is unstable, i.e. it has a strictly better face.
- KP(x): the key-preferred option under the keys of s.
- AGR(x) = [B(x) = KP(x)].
- MRG(x): the π-position of the merge vertex of x's two Ξ-plays (n if they meet only at T).
- Chained / unchained: box 144 ALL form; U = number of unchained steps.
- Premise routes: only landed RESULTS R103 / R104 (Theorem REALIZE: every IDEAL-ACYC genome is one real FL run), and lane-PROVED
  statements of boxes 142-146.

## 0. Answer
- No coarse statistic works. Best candidates per run (DOWN orientation, total violations over 37 genomes):
  - LEX(max π of an unstable mover, #unstable): 59. First counterexample: R188 exact pin x3_L8, step 3, unchained, (5, 3) → (5, 3).
  - Σ_{x unstable} (π(x) + 1): 65. First counterexample: x3_L8, step 4, chained, 9 → 10.
- The Lead's named candidates are DEAD, on R189's realised pin lag1 (lag1_n48: Oink --zlk / --tl verified, n5b identical, re-run here).
  At its unchained step 2, state (1,0,0,1,0,0) → (1,0,0,0,1,0):
  - Identity of the Ξ-better face: B = [1,0,0,0,1,0] before and after. Any function of B is constant, so it cannot fall.
    lag_min_d2 (d 2) is the same.
  - Merge vertex of the two Ξ-plays: MRG = all 6 (the plays meet only at T) before and after. Any function of MRG is constant.
  - «Face order agrees with key order» per level: LVL_AGR rises 2 → 3 and NAGR rises 5 → 6 (DOWN dies). UP dies on x3_L8 step 3
    (1 → 1) and step 5 (4 → 2).
  - π-position of the deepest mover whose Ξ-play changed: 3 → 3 (both orientations die).
- Stronger kills, all-start (§2): over every one of the 2^n starts (each is a valid IDEAL-ACYC genome), NO function at all of
  B, AGR, KP, MRG, «ready» (UNST with KP = B), #unstable, TOP1-3, per-level unstable counts, or the upper / lower half of the unstable
  set falls at every unchained step and never rises at a chained one. Each fails on some genome; instances are in §2.
- PROVED (lane), Lemma DECREMENT (§1, any IDEAL-ACYC genome).
  - At each step t let y_t be the mover with the largest π. Then y_t is unstable at s_(t−1) and stable at s_t, and no UNST bit at a
    position π > π(y_t) changes.
  - Corollary EXACT-ENERGY: E(s) = Σ_{x unstable} 2^π(x) falls strictly at EVERY step. So the unstable set alone suffices, but only
    through an exponential order (it is box 145 VAL-ENERGY at bit resolution).
  - Corollary TOP-MONO / RANK-BOUND: TOP_k(s), the k largest π-positions of unstable movers sorted downward and compared
    lexicographically, never rises. It falls at step t iff RANK_t ≤ k, where RANK_t = 1 + #(unstable movers above y_t).
    So #{t : RANK_t ≤ k} ≤ Σ_{j ≤ k} C(n, j), and U ≤ Σ_{j ≤ R} C(n, j) with R = the maximum RANK over unchained steps.
  - Hence «R = O(1) at unchained steps» would give U = n^O(1), and IDEAL-ACYC-POLY via CHAIN-BACK.
- DEAD: R = O(1).
  - Climbs on R (§3) give 5 / 7 / 11 / 15 / 18 at d 3 / 4 / 6 / 8 / 10, i.e. R = n − 1 (n − 2 at d 10), already with U = 1. The padding is unstable
    movers that are key-blocked for the rest of the run (the run stops «stuck» with them).
  - Counting only key-ready movers above y_t (RANKW) gives ≤ 2 on all 37 corpus genomes. But climbs reach 6 at d 6 and d 8
    (rw_d6_s1: one level-0 carry at step 2 freezes the five ready movers above y in the same step).
  - Polynomial weights: Σ_{x unstable} (π(x) + 1)^p needs p > 8 on dc_d10 (n 20) and p > 12 on dc_d12 (n 24). So no fixed degree
    works: DEAD for p ≤ 12 by dc_d12; the degree needed grows with n (DATA).
- READING (information): what tells an unchained step apart is the full unstable set in π order, and that is an exponential counter.
  - Every coarsening tested loses the decrement structure, and so does every Ξ-identity feature (B, MRG, AGR). W-side features are
    already dead by SPLIT-CYCLE.
  - A polynomial statistic would have to bound how often a lower W-side carry turns ready movers into frozen ones and back
    (RANKW: Θ(n) in one step). That is a key-change count again (box 137 KCH-GCH ⟺ FL-POLY), so in this form the target is circular.
  - A linear potential in the unstable bits with per-genome weights IS LP-feasible on every all-start graph with n ≤ 14
    (Σ|w| ≤ 169). The weights grow fast along π (uc_d4: 1,1,0,2,3,2,5,8). Fixed structural rules fail (1, π + 1, n − π, #desc + 1,
    height + 1); only 2^π (DECREMENT) works on every genome.

## 1. Proofs (PROVED, lane)
- Lemma DECREMENT. Any IDEAL-ACYC genome, deg 2, run s_0, s_1, …; t ≥ 1 with s_t ≠ s_(t−1); y_t := the max-π mover of step t.
  - (i) Under the R178 §1 rule a mover moves only to an available option, i.e. one with a strictly better face under s_(t−1). With
    deg 2 that option is B(y_t), so UNST(y_t) = 1 at s_(t−1).
  - (ii) The face (x, k) is the value of the functional Ξ-play gate (x, k) → β (x, k) → xt → gate (xt, s(xt)) → … → T. Every
    mover on it after x is a Ξ-descendant of x, so it has larger π (acyclic, π topological).
  - Every Ξ-descendant of y_t has π > π(y_t), so none of them moved at t. So y_t's faces are equal under s_(t−1) and s_t. y_t now
    sits on the strictly better one, so UNST(y_t) = 0 at s_t.
  - (iii) For π(x) > π(y_t): x did not move, and its descendants (π > π(x)) did not move. So its faces and its option are
    unchanged, and so is UNST(x). ∎
- Corollary EXACT-ENERGY.
  - By DECREMENT the highest changed bit of the word (UNST(x))_x, read with π as bit significance, goes 1 → 0, so E falls.
  - The quotient of the step graph by the unstable set is therefore acyclic, so some function of the unstable set is monotone with
    strict falls everywhere. This is why UNST (and every feature containing it) passes the all-start test in §2.
  - Degree D: replace UNST(x) by c(x) := #options with a strictly better face than s(x) ∈ {0, …, D − 1}. A move to a strictly better
    option strictly lowers c(y_t), since the options better than the new one are a subset of those better than the old one, minus
    the new one. The word Σ c(x) D^π(x) falls. Not checked on deg-3 data here.
- Corollary TOP-MONO / RANK-BOUND.
  - Positions above π(y_t) are unchanged, y_t leaves the set, and only positions below π(y_t) can enter.
  - If y_t is among the top k (RANK_t ≤ k), the first changed entry of the sorted tuple drops from π(y_t) to something smaller (or
    the tuple shortens): a strict fall. Otherwise the top k are unchanged.
  - TOP_k takes at most Σ_{j ≤ k} C(n, j) values. ∎

## 2. DATA
Tools (experiments/new/box147/):
- stat.py: 37 statistics and step quantities, both orientations; per-run quotient test.
- allstart.py: all 2^n starts, quotient / SCC test for any feature map, and the LP for linear potentials (scipy HiGHS).
- rank.py: RANK, YSTAB, ABOVE.
- rclimb.py: climbs on RANK; RW=1 climbs on RANKW.
- polyw.py: (π + 1)^p weights.
- weights.py: LP weights against structure.
- trace.py: per-step trace in π order.
Corpus: 32 genomes of boxes 140-146 (incl. R188 x3_L8 / g4_L12 and R189 lag1 / lag1u / lag2c_d4 / nest_d3_L4), plus box147/out
climbs.
- DECREMENT check (rank.py): YSTAB 0, ABOVE 0 on all 37 genomes and all steps.
- Per run (stat.py, run1.txt): every statistic is violated somewhere. The full list with totals is in run1.txt. The lowest DOWN
  totals are LEX_MAXPI_NU 59, SUMPI_U 65, Q_MAXPI_MV 79, MAXPI_WANT 83.
- All starts (allstart2.txt, n ≤ 14; «BAD» = genomes where some unchained edge lies on a cycle of the quotient):

| feature F (any function g(F)) | first BAD genome (n) | BAD genomes (of 27 run) |
| --- | --- | --- |
| B (Ξ-better identity) | up_d3 (6), lag1 (6, realised) | 23 |
| AGR, KP | up_d3 (6) | 22, 23 |
| MRG (per-run quotient, stat.py) | up_d3 (6) | 21 of 32 |
| WANT (ready set), NUNST, TOP1 | up_d4 / up_d3 / up_d3 | 14, 18, 20 |
| TOP2, TOP3 | up_d5 (10) | 18, 14 |
| LVCNT (per-level unstable counts) | g4_L12 (8, R188) | 8 |
| UNST upper half, lower half | up_d3 (6) | 20, 22 |
| WANT + #unstable | up_d6 (12) | 11 |
| UNST, UNST+KP, B+UNST, state | none (EXACT-ENERGY) | 0 |

- RANK on the corpus: max over unchained steps ≤ 6 (dc_d10). Histogram of unchained RANK: 1: 67, 2: 43, 3: 27, 4: 14, 5: 7, 6: 1.
  RANKW (ready movers only) ≤ 2 on the corpus.
- LP (allstart1.txt): a linear UNST potential is feasible on all 24 genomes with n ≤ 14. A linear potential in the option bits alone
  (S) is INFEASIBLE on 16 of them. Polynomial structural weights fail (weights.py).
- Pins: no new pins (box147/out climbs are IDEAL genomes, realisable by R104 Theorem REALIZE but not built).
  - Re-run in this container: box143/pincheck.sh and box144/pincheck.sh. Oink 8fbf0a7 --zlk and --tl: solution verified on all six
    pins; pinwin AGREE; n5b identical state sequences.
  - Output identical to the stored pincheck.txt files (box147/pincheck.txt).

## 3. DATA: climbs (box147/out; 3000 mutations for RANK, 6000 for RANKW; seeds 1-2)

| d | max unchained RANK (U) | max unchained RANKW, seed 1 / 2 (U) |
| --- | --- | --- |
| 3 | 5 (1) | 3 (3) / 3 (2) |
| 4 | 7 (1) | 2 (4) / 3 (1) |
| 6 | 11 (1) | 6 (4) / 6 (4) |
| 8 | 15 (1) | 5 (7) / 6 (1) |
| 10 | 18 (1) | not run |

RANKW over all steps (ALL=1, d 6): 7.

## 4. Status
- DEAD: every coarse candidate tested.
  - The Lead's four, on realised lag1 (B and MRG constant across an unchained step).
  - 37 per-run statistics; all-start functions of B, AGR, KP, MRG, WANT, NUNST, TOP1-3, LVCNT, halves.
  - TOP_k for constant k (rk climbs); ready-TOP_k for constant k (rw climbs); fixed-degree polynomial weights up to p 12 (dc_d12).
- PROVED (lane): DECREMENT, EXACT-ENERGY (also at degree D), TOP-MONO / RANK-BOUND (U ≤ Σ_{j ≤ R} C(n, j)).
- READING: minimal distinguishing information = the unstable set in π order (an exponential counter). A polynomial statistic must
  also control W-side freeze / release of ready movers, which is the key-change count again.
- OPEN: U-LIN, IDEAL-ACYC-POLY, G-N5-TIME.
- Suggested next (Lead decides): bound #{unchained t : RANK_t > k} by key changes below the frozen movers above y_t. That makes
  U ≤ n^k + (frozen-release events) explicit, and asks L-RED for a family where those events are super-polynomial.
