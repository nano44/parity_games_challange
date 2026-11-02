# Box 146 N5-SPLITE: the box 145 candidate energy (split-level count weighted by π-position) is DEAD in every variant and both orientations; smallest counterexample d 2, 4 movers, a 2-step run (chained step, split bit 0 → 1); on R189's realised pin lag1 an unchained step leaves the count unchanged and raises every weighted form. Reason: a released pair makes its level split, then same, inside one carry period, whichever kind of step does it
L-NEW successor 48, 2026-11-02 (date -u: see the commit). Lead GO 06:27Z (box 146, last before parking: test the candidate energy of box 145
§0, its strict fall at every unchained step and no rise at chained steps). Labels: PROVED (lane), DATA, DEAD, READING. U-LIN,
IDEAL-ACYC-POLY and G-N5-TIME stay OPEN. Not a TARGET.md claim.

## 0. Answer
- The candidate made precise, as functions of the current state s only (experiments/new/box146/energy.py):
  - split_l(s) = 1 iff l ≥ 1 and u_l, v_l point at different lower movers (box 143 ABSORB);
  - π = the genome's xorder, or a Kahn topological order of the Ξ-graph;
  - pmin_l / pmax_l = the min / max π-position of u_l, v_l.
  - V0 = Σ split_l; V1 = Σ split_l (1 + pmin_l); V2 = Σ split_l (1 + pmax_l); V3 = Σ split_l (l + 1); VLEX = the split bits ordered by
    pmin, compared lexicographically.
  - Steps are chained / unchained as in box 144 (ALL form).
  - Tested in both orientations:
    - DOWN: strict fall at unchained steps, no rise at chained steps;
    - UP: strict rise at unchained steps, no fall at chained steps.
- DEAD, all 10 (variant, orientation) pairs. Totals over 31 genomes (boxes 140-144, R188 x3_L8 / g4_L12, R189 lag1 / lag1u / lag2c_d4 /
  nest_d3_L4, the d 12 champion):
  - DOWN: V0 143, V1 145, V2 142, V3 154, VLEX 113 violations.
  - UP: 173, 155, 160, 147, 188.
- Smallest counterexample, DOWN (as briefed): small_d2.json (box146/small.py, random search, d = 2, trial 17).
  - 4 movers, run of 2 steps from the start (0,1,1,0). The violating pair is state 1 = (0,1,0,0) → state 2 = (0,0,0,1).
  - Step 2 is chained: least mover 1 (level 0); h_1 = mover 2 lies on its new face's Ξ-play.
  - split_1 goes 0 → 1, so every variant RISES at a chained step.
  - It is an IDEAL genome only (not realised as a real game, like box 142's lag_min_d2).
- On a realised pin: R189 lag1 (lag1_n48: Oink verified, n5b identical; box 144).
  - Step 2 is UNCHAINED: (1,0,0,1,0,0) → (1,0,0,0,1,0).
  - V0 stays 1 (no strict fall); V1 3 → 4, V2 5 → 6, V3 2 → 3 rise. Only VLEX-DOWN survives on lag1, and it dies on x3_L8 step 5 and
    up_d3 step 2.
- The UP orientation dies on lag_min_d2 (d 2, unchained step 2) and on x3_L8 step 3.
- Why (PROVED, lane), Lemma SPLIT-CYCLE.
  - Take a level l ≥ 1 in the SAME state (both movers point at the same lower mover y), and let a carry of level l − 1 release both.
  - If they move at different steps (a delay or lag, box 142), split_l goes 0 → 1 at the first move and 1 → 0 at the second.
  - If they move together, split_l stays 0. If only one moves before the next carry, split_l stays 1.
  - So every level's split bit can rise and fall inside one carry period. Whether the rise falls on a chained or an unchained step is
    decided by Ξ-reads, not by the split pattern.
  - So no function of the split bits alone can be monotone along CHAIN-BACK's classes. The instances above realise both kinds.
- READING: an energy for U must read Ξ-information, i.e. where along π the waiting movers' faces stand. The split pattern is W-side
  only, and W-side-only data cannot see the chained / unchained distinction. Box 145 showed the full Ξ-value vector has exponentially
  many levels. The open question is a COARSE Ξ-statistic with polynomially many levels that still falls at every unchained step.

## 1. Proof of SPLIT-CYCLE (PROVED, lane)
- Same state at level l with target y = L_(l−1)(s − 1). A carry at s makes y the H-mover, so both u_l and v_l are released (box 142).
- By C-ELEM each moves at most once before the next carry, and only to the new L_(l−1).
- After the first move only, they point at different lower movers (split_l = 1). After both, they point at the same one (split_l = 0).
- The three cases follow. ∎

## 2. DATA
- energy.py on every genome: per variant and orientation, the violation counts and the first violating (state t − 1, state t) pair
  (VERB=1).
- small.py: d = 2 random search, 20,000 trials, seed 7; first hit at trial 17, kept as box146/small_d2.json.

## 3. Status
- DEAD: the split-level energy V0-V3, VLEX, both orientations. Smallest instance small_d2 (d 2, chained rise); realised instance lag1
  (unchained non-fall).
- PROVED (lane): SPLIT-CYCLE.
- OPEN: U-LIN, IDEAL-ACYC-POLY, G-N5-TIME.
