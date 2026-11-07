# Box 144 N5-CHAIN: the briefed pre-merge charge is DEAD (a B-flip can be caused only on the common suffix, when the other play re-routes off the merge vertex; R188 pin x3_L8); Lemma CHAIN-BACK (PROVED, lane, any IDEAL-ACYC genome): steps ≤ n_E (1 + U), where U counts steps whose least mover was NOT woken by the previous step's least mover; U-climbs give U ≈ 2d (DATA), so U is the open object
L-NEW successor 48, 2026-11-02 (date -u: see the commit). Lead GO 04:33Z (box 144: charge each DELSTEP to a (pre-merge segment, carry
wave) pair via box 135 MERGE; O(1) per wave or O(n) in total ⇒ DELSTEPS polynomial). Labels: PROVED (lane), CONJECTURE, READING,
DATA, DEAD. G-N5-TIME, IDEAL-ACYC-POLY, DELAY-LIN and DELSTEP-LIN stay OPEN. Not a TARGET.md claim.
Model: as box 143 (R178 §1 IDEAL rule; 2-wide deg-2 ladder in the R188 genome format unless said otherwise). h_t := the least-level
mover of step t, smallest index on a tie. π := any topological order of the Ξ-graph: Ξ-edges go forward. n_E := number of movers (2d
on the ladder).

## 0. Answer
- The briefed charge does not close.
  - DEAD (the premise): «a delayed least mover's B-flip is caused by a move on the PRE-MERGE segment of its toward-face's Ξ-play».
  - Instance: R188's exact pin x3_L8 (d 3), step t = 6, h_6 = mover 4 (level 2), new option k = 1.
    - At state 4, face (4, 1) reads mover 1 directly, so its pre-merge segment is empty and the merge vertex is 1.
    - Face (4, 0) reads 5 → 1 → …, so its pre-merge segment is [5].
    - Step 5 moves exactly 1 (the merge vertex) and 5. Mover 5 switches from option 0 (Ξ-target 1) to option 1 (Ξ-target 3), so the
      k̄-play leaves the merge vertex.
    - The rise of Ξ(1) then no longer cancels between the two faces, and face 1 overtakes face 0. The cause is on the COMMON SUFFIX.
  - MERGE (box 135) needs a fixed merge vertex; a move on the other segment can re-route it.
  - The same happens once on g4_L12, nest_d3_L4 (R189), dc_d6 and dc_d12, and twice on mc_d8 (merge.py NOPRE).
  - Repaired cause set: movers on the WHOLE toward-play that moved one step earlier. It is never empty (box 142 DELAY-CAUSE / R178
    XI-NEW): NOCAUSE 0 everywhere.
  - Data on per-segment charging (pairs (x, c), with c the first cause on the play): ≤ 3 DELSTEPS per pair, per (x, k) and per cause
    mover. No pattern of «O(1) per wave»: each step is one wave, so per-wave charging is trivially 1 and gives nothing.
- PROVED (lane), §1, Lemma CHAIN-BACK, valid for ANY IDEAL-ACYC genome (any width, any degree), not only the 2-wide ladder.
  - Call a step t ≥ 2 CHAINED if h_(t−1) lies on the Ξ-play (state t − 2) of the option that h_t takes at t. Then π(h_t) < π(h_(t−1)).
  - A maximal block of consecutive chained steps has length ≤ n_E. Hence steps ≤ n_E (1 + U), with U = #{t ≥ 2 unchained}.
  - So IDEAL-ACYC-POLY ⟺ U polynomial (U ≤ steps).
  - In the UP shape (Ξ-targets strictly higher) π can be the level, so blocks have length ≤ d and steps ≤ d (1 + U).
  - This is the backward twin of R189's LAG-RELEASE («lags run forward in π»): along a chain the woken least mover is a Ξ-ANCESTOR of
    the previous one.
- What wakes an unchained step (DATA): a non-least mover of the previous step.
  - On the ladder it is a CAR move (carried up from h_(t−1) through split levels, box 143 ABSORB) or a parallel delay higher up.
  - up_d8_s8: all 7 unchained DELSTEPS are woken by CAR moves above h_t; h_(t−1) is below h_t in 6 of them and at the same level
    in 1 (t 17).
- DATA (§2):
  - Blocks are short: MAXBLOCK ≤ 7, and = n_E = 6 on dc_d3, so the bound is tight there.
  - Climbs that maximise U (40k mutations): U = 6 / 9 / 13 / 17 at d = 4 / 6 / 8 / 10 (steps 7 / 13 / 16 / 22). U ≈ 2d − 3, linear.
  - So in the worst observed runs nearly every step is unchained, and CHAIN-BACK moves the open object without shrinking it.
- CONJECTURE U-LIN (DATA d ≤ 10): U = O(d) on 2-wide IDEAL-ACYC ladders.
  - With CHAIN-BACK it gives O(d²) steps; linear runs imply it (U ≤ steps).
  - DELSTEP-LIN is equivalent to linear runs (box 143 STEP-DELAY); DELAY-LIN implies them.
  - Any polynomial bound on U gives the 2-wide case of IDEAL-ACYC-POLY.
- Beyond width 2 (Lead's question): CHAIN-BACK and its bound hold for every IDEAL-ACYC genome, which is the part that extends.
  - C-ELEM, STEP-DELAY and ABSORB are 2-wide deg-2 statements. With w > 2 lower movers a mover can move twice between carries (it moves
    to the key-least AVAILABLE option, and a key-smaller one can become available later), so STEP-DELAY's «≤ 1 move per carry» fails.
  - XI-NEW (R178) replaces it, and CHAIN-BACK uses only XI-NEW.
  - For L-RED R190 (3-wide clock): the score that matters is U. A clock must wake least movers from the non-root part of the previous
    wave super-linearly often.

## 1. Proof (PROVED, lane)
- Lemma CHAIN-BACK. IDEAL-ACYC genome, fallback-free run with steps 1..T.
  - (a) Cause sets. For t ≥ 2, let w be h_t's new option.
    - By R178 Lemma XI-NEW, w ∉ A_(t−2)(h_t), and by its consequence (ii) the face (h_t, w) rose strictly at step t − 1. So some mover
      on its Ξ-play (state t − 2) moved at step t − 1.
    - Let Z_t ≠ ∅ be the set of those movers.
    - Every mover on that play is Ξ-reachable from h_t, so π(h_t) < π(z) for z ∈ Z_t (acyclic Ξ-graph).
  - (b) Blocks. Take a maximal interval [a, b] of steps with h_(t−1) ∈ Z_t for every t ∈ (a, b].
    - Then π(h_a) > π(h_(a+1)) > … > π(h_b), so the h_t are distinct and b − a + 1 ≤ n_E.
    - Every block starts at a = 1 or at an unchained step. So T ≤ n_E · (1 + U). ∎
  - On the ladder XI-NEW is box 142 DELAY-CAUSE for delayed least movers and C-ELEM's B-flip for PRE least movers. Checked: NOCAUSE 0,
    PIVIOL 0 (chain.py) on every genome of §2.
- Why the pre-merge premise fails, in general.
  - The comparison of faces k and k̄ equals the comparison of their pre-merge segments plus the gates' β, but only while the merge
    vertex m is fixed.
  - A move on the k̄ segment that re-routes the k̄-play away from m makes the old common suffix part of the difference.
  - A move at m (or beyond) then raises face k alone, as on x3_L8 above.
- What would close U-LIN (READING): a potential over waves.
  - An unchained step t is woken by a non-root mover c of wave t − 1. On the ladder c is CAR (its carry is caused in the same step by
    h_(t−1) through split levels) or a parallel delay.
  - A proof has to charge such c to something that wave t − 1 consumes, e.g. a split level that closes (ABSORB) or an L_l flip, and
    show that this resource refills O(1) times per lower carry.
  - That is the doubling question again (box 142 DELAY-CHARGE), so U-LIN is not easier than DELSTEP-LIN in this form.

## 2. DATA
Tools in experiments/new/box144/:
- merge.py: the briefed pre-merge charge: NOPRE, per-pair maxima, cause classes.
- chain.py: CHAIN-BACK on DELSTEPS and on ALL steps ≥ 2: UNCH = U, NOCAUSE, PIVIOL, MAXBLOCK, BOUND n_E (1 + U).
- uclimb.py: climbs on U.
- pincheck.sh: pins.

| genome | d | steps | NOPRE | U (all steps) | MAXBLOCK | n_E (1 + U) |
| --- | --- | --- | --- | --- | --- | --- |
| x3_L8 (R188 exact) | 3 | 8 | 1 | 3 | 3 | 24 |
| g4_L12 (R188) | 4 | 12 | 1 | 3 | 5 | 32 |
| lag1 / lag1u (R189) | 3 | 2 / 2 | 0 / 0 | 1 / 1 | 1 / 1 | 12 / 12 |
| lag2c_d4 (R189) | 4 | 9 | 0 | 3 | 4 | 32 |
| nest_d3_L4 (R189) | 3 | 4 | 1 | 1 | 3 | 12 |
| dc_d3 / dc_d8 / dc_d12 (box 143) | 3 / 8 / 12 | 6 / 23 / 26 | 0 / 0 / 1 | 0 / 9 / 14 | 6 / 6 / 7 | 6 / 160 / 360 |
| up_d8_s8 (box 141) | 8 | 19 | 0 | 10 | 3 | 176 |
| uc_d4 / d6 / d8 / d10 (U climbs) | 4-10 | 7 / 13 / 16 / 22 | not run | 6 / 9 / 13 / 17 | 1 / 3 / 2 / 3 | 56 / 120 / 224 / 360 |
- NOCAUSE 0, PIVIOL 0 and BOUND OK on all of the above and on all box 140-143 genomes (up_d3 … up_d8_s8, dc_*, mc_*, lag_min_d2).
- Pins: R189's lag1_n48, lag1u_n48, lag2c_d4_n62 and nest_d3_L4_n48 were copied read-only from claude/l-red 80bfb1d0 into box144/inst.
  - The sha1s equal its pins.sha1 (aed8620b…, 4db88f5b…, c3a530fd…, af8c37c9…). The IDEAL genomes lag1 / lag1u / lag2c_d4 /
    nest_d3_L4 .json come from r189/lag.
  - Oink 8fbf0a7 --zlk and --tl: solution verified on all four.
  - pinwin AGREE; n5b identical state sequences (6 / 6 / 13 / 8 states, 1 fallback each); box144/pincheck.txt.

## 3. Status
- DEAD: the pre-merge cause premise (x3_L8, step 6), and with it the briefed (pre-merge segment, carry wave) charge as stated.
- PROVED (lane): CHAIN-BACK (any IDEAL-ACYC genome): steps ≤ n_E (1 + U); UP shape: ≤ d (1 + U).
- CONJECTURE: U-LIN (⇒ O(d²) steps), DELSTEP-LIN (⟺ linear runs), DELAY-LIN (⇒ linear runs); DATA to d 10-12.
- OPEN: IDEAL-ACYC-POLY, G-N5-TIME.
- READING: the remaining object is the rate at which non-root wave members (carried moves) wake least movers below them.
