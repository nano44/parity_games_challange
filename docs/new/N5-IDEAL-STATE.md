# N5-IDEAL-STATE: the IDEAL-ACYC question after L-NEW boxes 139-148 and L-RED R187-R191 (synthesis, box 149)
L-NEW successor 49, 2026-11-02 (date -u: see the commit). Lead GO 13:51Z (box 149: synthesis, not new search; mark a packet candidate,
do NOT freeze). Every line is labelled:
- RESULTS-landed: in docs/RESULTS.md on trunk.
- PROVED (lane): proved in a lane file, not refereed.
- DEAD: with the instance that kills it.
- CONJECTURE: with its DATA range.
- READING, DATA.
G-N5-TIME and IDEAL-ACYC-POLY are OPEN. Not a TARGET.md claim. Commits are claude/l-new unless marked l-red.

## 0. The question and where it sits
- IDEAL-ACYC model (R178 §1; P-N5-REALIZE §2).
  - Movers x with options (W-target, Ξ-target, gate, β).
  - One step: every mover takes the key-least option among {current} ∪ {strictly Ξ-better faces}, with keys computed root-first in the
    new state.
  - The Ξ-graph is acyclic; π is a topological order.
  - Run: from a start until no mover moves.
  - The 2-wide ladder: u_l, v_l at level l, degree 2, option k of a level-l mover has W-target the k-th level-(l − 1) mover.
- IDEAL-ACYC-POLY: every IDEAL-ACYC run has poly(n) steps.
- Place in the fleet question (G-N5-TIME), all one-way except where marked:
  - RESULTS-landed R104 (P-N5-REALIZE, Theorem REALIZE / Corollary REAL-IDEAL; l-red packet e609c5d2): every IDEAL-ACYC genome runs,
    state for state, as ONE real N5 FL run (a game of size N + 3M + 6).
    - Hence FL-POLY ⇒ IDEAL-ACYC-POLY.
    - Equivalently, a super-polynomial IDEAL-ACYC family kills FL-POLY.
    - READING (L-NEW): it also kills N5-POLY, since the realised FL run is a stretch of N5's own state sequence on that game, so N5
      makes at least that many iterations there.
  - RESULTS-landed R103 (P-N5-ANCHOR, Corollary FL-GCH; packet ad97ad88): FL-POLY ⟺ GCH-POLY, inside one W-flat run.
  - So (with the READING above) IDEAL-ACYC-POLY is NECESSARY for N5-POLY. It is not known to be sufficient: real FL runs need not be
    Ξ-acyclic.
    - READING: the IDEAL-ACYC question is the cleanest known sub-question whose negative answer kills N5. A positive answer covers only
      the acyclic case.

## 1. Reductions (one line each)
- R1 (PROVED lane, box 144 CHAIN-BACK, d725de98): steps ≤ n_E (1 + U), with U = #unchained steps. So IDEAL-ACYC-POLY ⟺ U-POLY (any
  width, any degree; uses R178 XI-NEW, l-red lane).
- R2 (PROVED lane, box 149 KEYFLIP, this commit, §4): degree 2: moves(x) ≤ 1 + KF_x, with KF_x = #key-preference flips of x.
  - So steps ≤ Σ_x (1 + KF_x), and KF ≤ n · steps. Hence IDEAL-ACYC-POLY ⟺ KF-POLY.
  - On the 2-wide ladder, KF_x for a level-l mover = flips(L_(l−1)) (carries). This is the IDEAL twin of box 137 KCH-GCH (KCH-POLY ⟺
    FL-POLY).
- R3 (PROVED lane, box 142 DELAY-CHARGE, 40708ae9): 2-wide: flips(L_l) ≤ flips(L_(l−1)) + 2 + DELAY_l. So Σ DELAY = O(d) ⇒ O(d²)
  steps.
- R4 (PROVED lane, box 143 STEP-DELAY + C-ELEM + ABSORB, 33f66fca): 2-wide deg 2: steps ≤ 1 + 2d + DELSTEPS. So DELSTEP-LIN ⟺ linear
  runs.
- R5 (PROVED lane, box 139 PATHS / LOG-DEPTH, 3b2078c9): moves(x) ≤ min(VX, VW) − 1 (Ξ-path values, W-path keys). IDEAL-ACYC-POLY holds
  when every mover has logarithmic Ξ-depth or W-level.
- R6 (PROVED lane, box 147 DECREMENT / EXACT-ENERGY, 60286d8c): at every step the max-π mover goes unstable → stable and nothing above
  it changes. So Σ_{unstable} 2^π falls at every step (degree D: Σ c(x) D^π).
- R7 (PROVED lane, box 147 RANK-BOUND): U ≤ Σ_(j ≤ R) C(n, j), with R = the max RANK at unchained steps. So R = O(1) ⇒ U-POLY.
- R8 (PROVED lane, box 148 INTERVAL-RESTRICT / INTERVAL-CHARGE, 5c93eaf8):
  - A TOP_k-constant interval is a prefix of the run of a smaller IDEAL-ACYC genome (the top part at degree 1).
  - #{RANK = r} ≤ (n − r + 1)(1 + #{RANK ≤ r − 1}).
  - Each interval opening is a RELEASE (a key flip of y_t) or a fresh Ξ-WAKE.
  - U*(n) ≤ Σ_(p<n) (U*(p) + 1).
- R9 (PROVED lane, l-red R191 ROT-CAP / ROT-BUDGET, 314dcdda): any width, degree D: moves(x) ≤ (D − 1)(1 + H_x), with H_x = #steps
  at which a Ξ-descendant of x moves. KEY-ALT (width 2) and MERGE-1 are PROVED lane there too.
- R10 (PROVED lane, l-red R189 LAG-RELEASE, 80bfb1d0): a mover that wants an option one step late was released by a Ξ-descendant that
  moved: lags run forward in π.
- Supporting lemmas (PROVED lane): box 140 ALTERNATION, TOWARD-L, L-ACCOUNT, TOP-STATIC (80cd02cc); box 145 VAL-ENERGY, TRI, HALVES
  (632154d0); box 146 SPLIT-CYCLE (767ed19a).

## 2. DEAD routes (instance in brackets)
- Literal NO-LAG (box 142) [lag_min_d2, d 2; also realised lag1 / lag2c_d4 / nest_d3_L4, l-red R189].
- Bounded lag suffices (box 142) [up_d4, UP shape].
- «Face re-rises only after a carry above» (box 143) [R188 exact pin x3_L8, face (0,0) at steps 5, 6].
- Pre-merge cause premise / per-wave charge (box 144) [x3_L8 step 6: re-route off the merge vertex].
- Direct threshold-network cast (box 145) [x3_L8: one-step map not unate; also g4_L12, nest_d3_L4, lag2c_d4, up_d3].
- Split-level energy, all variants, both orientations (box 146) [small_d2 chained rise; realised lag1 unchained non-fall]. Any
  W-side-only energy is excluded by SPLIT-CYCLE.
- Coarse Ξ-statistics (box 147):
  - Ξ-better identity and merge vertices [realised lag1: constant across the unchained step].
  - 37 per-run statistics [best LEX(max π unstable, #unstable): x3_L8 step 3].
  - Any function of B, AGR, KP, MRG, WANT, #unstable, TOP1-3, per-level counts, halves [all-start quotients; up_d3 / up_d4 / up_d5 /
    g4_L12].
- TOP_k, constant k (box 147) [rk_d3: RANK 5 = n − 1]. Ready-only TOP_k [rw_d6_s1: RANKW 6]. (π + 1)^p weights, p ≤ 12 [dc_d12].
- Per-step key-change charge for high-rank unchained steps (box 148) [uc_d6, steps 3-6].
- CASC-M''' on real FL runs (box 139) [stab_d4_n126: D''' cyclic 0 → 2 → 9 → 0]. Pointwise two-sided counting (box 140 TWO-SIDED:
  exponential at the middle, a proved obstruction).
- Doubling schedule NEST(d), d ≥ 3 (l-red R189, degree 2; R191 NEST-DEAD-3, degree ≤ 3; PROVED lane, z3-exact at d 3 for degree 2).
- Ξ-counter inside IDEAL-ACYC (l-red R188): none found. EXACT (z3): max steps 4 at d 2 and 8 at d 3 on LADDERBF's 2-wide ladder.

## 3. Conjectures (DATA range)
- U-LIN: U = O(d) on 2-wide ladders.
  - DATA: U ≈ 2d − 3, climbs to d 10 (box 144: 6 / 9 / 13 / 17 at d 4 / 6 / 8 / 10).
  - l-red R190: (3, 3) ≈ 3.5 per level to d 12, (2, 2) 14 at d 10.
  - l-red R191: degree 3, ≈ 2.7 per level to d 8.
- DELAY-LIN (⇒ linear runs; box 143): Σ DELAY ≈ 5 per level, d 3-12.
- DELSTEP-LIN (⟺ linear runs, R4): DATA d ≤ 12; l-red R190 DELSTEPS linear to d 6.
- UP-LIN (box 141): UP-LADDER runs FL 5 / 7 / 11 / 13 / 16 / 19 at d 3-8 (≈ 2.4 d). Weak.
- No conjecture is made on R (box 147 climbs: R = n − 1) or on RANKW (6 at d 6, 8).

## 4. New in this box: Lemma KEYFLIP (PROVED, lane)
- Statement. Degree 2, any IDEAL-ACYC genome. If x moves at steps t1 < t2 (consecutive moves of x), then KP(x) differs between
  s_(t1) and s_(t2), where KP is the key-preferred option under the keys of that state. Hence moves(x) ≤ 1 + KF_x.
- Proof.
  - At t1, x moves from b to a. With degree 2 the available set is {b, a}.
  - The rule chooses the key-least option under the keys of s_(t1), so KP(x) at s_(t1) is a.
  - At t2, x moves from a to b. Again both options are available, and the rule picks b, so KP(x) at s_(t2) is b.
  - Windows (t1, t2] of consecutive move pairs are disjoint. ∎
- DATA: experiments/new/box149/keyflip.py, 0 violations on 512 movers (46 genomes of boxes 140-148). Example: x3_L8 13 moves vs 10 key
  flips; dc_d12 82 vs 86.

## 5. The remaining open quantity (cleanest form)
- On the 2-wide degree-2 ladder, with F_l := flips(L_l) (carries at level l), everything above reduces to one question:
  - IDEAL-ACYC-POLY ⟺ Σ_l F_l = poly(n).
  - This uses R2 and the ladder identity KF_x = F_(l−1) for every level-l mover x (its two options' keys extend the keys of u_(l−1)
    and v_(l−1)), so KF = 2 Σ_l F_(l−1). The reverse direction holds since F_l ≤ moves at level l.
- What is known about it:
  - DELAY-CHARGE gives F_l ≤ F_(l−1) + 2 + DELAY_l. Here DELAY_l counts the level-l movers released by a carry that move one step
    late.
  - Lags exist (realised, R189). Lags run forward in π (LAG-RELEASE). The known doubling schedules die (NEST-DEAD, NEST-DEAD-3).
- So the open object is: Σ_l DELAY_l, the number of late responses to carries, summed over levels.
  - Equivalently (R8): the number of releases of frozen top movers, counted uniformly in π-rank.
  - Whether one carry can force ω(1) late responses ABOVE it, compounding across levels.
- Any general width / degree: the same with F_l replaced by key-ranking flips R_l (KEY-ALT), and with ROT-CAP's D − 1 factor.

## 6. Packet candidate (NOT frozen; the Lead decides)
- Proposed name: P-IDEAL-RED.
- Claim: «In the IDEAL-ACYC model:
  - (i) steps ≤ n_E (1 + U) (CHAIN-BACK);
  - (ii) at degree 2, steps ≤ Σ_x (1 + KF_x) ≤ n · (1 + steps), so IDEAL-ACYC-POLY ⟺ U-POLY ⟺ KF-POLY (KEYFLIP);
  - (iii) Σ_{unstable} 2^π falls at every step, and U ≤ Σ_(j ≤ R) C(n, j) (DECREMENT, RANK-BOUND);
  - (iv) INTERVAL-RESTRICT and INTERVAL-CHARGE.»
- Each part is a short, self-contained proof inside the R178 §1 model, about 1 page each.
- Premises it needs:
  - R178 Lemma XI-NEW and its consequence (ii) (l-red lane, NOT landed): CHAIN-BACK uses it. Either XI-NEW lands first, or the packet
    carries its proof (I have not re-proved it here). KEYFLIP, DECREMENT, RANK-BOUND and INTERVAL-* do NOT use it.
  - The R178 §1 model statement as in P-N5-REALIZE §2 (landed as R104). No other premise.
- What it would NOT claim:
  - Any polynomial bound.
  - That «frozen-release count polynomial» is equivalent to IDEAL-ACYC-POLY. Only ⇒ is easy (releases ≤ n · steps). The converse is
    not proved: releases are key flips used at one particular moment, while R2 needs ALL key flips.
  - So the honest equivalence is with KF (R2) or with U (R1), not with releases.
- Value (READING): it fixes the reductions in one refereed place. Every later attempt (L-RED R192's freeze/release family, any
  potential) is then scored against U or KF with a referee-signed bound. It is a REDUCTION packet like P-N5-ANCHOR, not M3.
- Risk: (iii) and (iv) are exponential / recursive bounds. Their value is structural (they locate the circularity), so a referee may ask
  for (iii)-(iv) to be cut. A minimal packet is (i) + (ii).

## 7. Status
- OPEN: IDEAL-ACYC-POLY, U-LIN, DELAY-LIN, DELSTEP-LIN, UP-LIN, G-N5-TIME.
- PROVED (lane): §1 R1-R10 and §4 KEYFLIP.
- RESULTS-landed: R103 (FL-POLY ⟺ GCH-POLY), R104 (REALIZE ⇒ FL-POLY ⇒ IDEAL-ACYC-POLY).
