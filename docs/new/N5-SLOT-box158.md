# Box 158 N5-SLOT: the «linear first segments» route is circular. Lemma LIFT puts a whole (d−1)-level run into the first segment of a d-level ladder (lift_max_d4_L13: d 5, first segment 13); Lemma SHIFT + SEG cap every segment by T*(d−1); so T*(d−1) ≤ T*(d) ≤ 3 T*(d−1) + 2, and «T*(d) ≤ T*(d−1) + O(d)» is a trade-off statement between segments, not a per-segment one
L-NEW successor 51, 2026-11-04 (date -u: see the commit). Lead brief BOX 158 (12:23Z; proof twin of L-RED R203). Labels: PROVED (lane),
DATA, DEAD (route), CONJECTURE, READING. Model: RESULTS R104's definition; notation of P-IDEAL-SEG §0. Not a TARGET.md claim.
No polynomial bound. IDEAL-ACYC-POLY and G-N5-TIME stay OPEN.

## 0. Answer
- Class 𝓛_d: IDEAL-ACYC genomes with levels 0, …, d − 1 and exactly two degree-2 movers on every level. Any number of degree-1 movers is
  allowed at any level (padding). T*(d) := sup of T over 𝓛_d and all starts (finite: LEVEL-PRODUCT gives ≤ 3^d − 1).
- Segments of a run, cut at its level-0 steps (at most 2, by SEG-ONCE):
  - seg1 := the steps before the first level-0 step;
  - mid := the non-level-0 steps between the first and the last level-0 step;
  - tail := the steps after the last one.
  - T = seg1 + mid + tail + (number of level-0 steps).
- PROVED (lane), §1:
  - Lemma SHIFT: if every level-0 mover has degree 1, the genome is run-equivalent to one with a level fewer.
  - Corollary SEG-CAP (SEG + SHIFT): on 𝓛_d, each of seg1, mid and tail is at most T*(d − 1).
  - Lemma LIFT: every run of a d-level genome reappears, with the same length, as the run of a (d + 1)-level genome whose two new
    level-0 movers never move. So 𝓛_(d−1) runs embed into 𝓛_d with seg1 = T.
  - Corollary: T*(d − 1) ≤ T*(d) ≤ 3 T*(d − 1) + 2, and max seg1 over 𝓛_d equals T*(d − 1).
- DEAD (route): «bound the first two segments linearly in d, then T(d) ≤ T(d − 1) + O(d)» (Lead brief box 158).
  - By LIFT, max seg1 over 𝓛_d is T*(d − 1). A linear bound on seg1 is therefore the linear bound on T* itself, so the route is
    circular.
  - Instance: box158/lift_max_d4_L13.json (L-RED R197's max_d4_L13 lifted). A 5-level 2-wide ladder with T 13, no level-0 step, so
    seg1 = 13. Every other d = 5 run in the data has seg1 ≤ 6 (table below).
  - Likewise lift_max_d5_L15 (d 6, seg1 15) and lift_dd_d5_F14 (d 6, seg1 14).
- What survives: the statement the route was aiming at is a TRADE-OFF.
  - CONJECTURE SLOT-TRADE (lane): T*(d) ≤ T*(d − 1) + c·d for a constant c, i.e. seg1 + mid + tail ≤ T*(d − 1) + O(d). The segments can
    each be long, but not all at once.
  - It is equivalent to «T* is O(d²)» given LIFT / SEG-CAP. No proof.
  - DATA on exact pure-ladder maxima (L-RED; no padding): T(d) − T(d − 1) = 4, 5, ≥ 2 for d = 3, 4, 5 (4, 8, 13, ≥ 15).
  - Tails are well below T(d − 1) in every champion: max_d5_L15 tail 7 ≤ 13; max_d4_L13 tail 5 ≤ 8; x3_L8 tail 3 ≤ 4.
- DATA (box158/three.py), segments of every corpus / champion run (genome start). Largest values seen:
  | d | best T | seg1 / mid / tail of the best T | max seg1 (any run) | max tail (any run) |
  | --- | --- | --- | --- | --- |
  | 3 | 8 (x3_L8, dbl_d3_F6) | 3 / 0 / 3 and 3 / 1 / 2 | 3 | 3 |
  | 4 | 13 (max_d4_L13) | 5 / 1 / 5 | 5 | 5 |
  | 5 | 15 (max_d5_L15) | 6 / 0 / 7 | 6 | 7 |
  | 6 | 13 (uc_d6, up_d6, up_d6_s16) | 0 / 3 / 8, 7 / 0 / 4, 9 / 1 / 1 | 9 | 10 |
  | 8 | 23 (dc_d8) | 5 / 1 / 15 | 10 | 15 |
  | 10 | 22 (uc_d10) | 0 / 12 / 8 | 0 | 10 |
  | 12 | 26 (dc_d12) | 1 / 8 / 15 | 1 | 15 |
- READING:
  - The champions spend about a third of T in each segment, and none comes close to filling two segments with a full (d − 1)-run.
  - SLOT-TRADE asks exactly why. It needs an argument that a level-0 step «uses up» the room that a long seg1 used, i.e. some
    potential above level 0 that seg1 spends and the level-0 step does not refill.
  - EXACT-ENERGY (RESULTS R105) is such a potential, but it is refilled by the level-0 move (c of level-0 movers drops, everything above
    may reset). That is the 3^d room again.

## 1. Proofs
- Lemma SHIFT (IDEAL-ACYC, any degree, any width).
  - Setting. Let G have every level-0 mover of degree 1. Build G↓:
    - every mover of level ≥ 1 goes one level down, and the level-0 movers stay at level 0;
    - every option of a former level-1 mover loses its W-target, and its gate becomes g′(x, k) := g(w, k_w)·Γ + g(x, k), where w is
      its old W-target, k_w the only option of w, and Γ is larger than every gate of G;
    - every other field, and the start, is unchanged.
  - Claim: G↓ is an IDEAL-ACYC genome, and from every start its run equals G's state for state.
  - Proof.
    - Validity. Gates stay distinct: if g(w, k_w) ≥ 1 the new gates are ≥ Γ, above every old gate, and pairwise distinct; if
      g(w, k_w) = 0, then g′ = g(x, k), already distinct. W-targets still lie one level down. Ξ-data and the Ξ-graph are unchanged.
    - Values. The Ξ-values are those of G (same Ξ-data, same states).
    - Keys. For an option at old level l ≥ 1, G's key under s is (g(w_0), g(w_1), g(w_2), …, g(x, k)), with w_0 the level-0 option on its
      W-chain (fixed, since level-0 movers have one option) and w_1 the level-1 option. G↓'s key is (g′(w_1), g(w_2), …, g(x, k)).
    - g′ orders the pairs (g(w_0), g(w_1)) lexicographically, because Γ exceeds every gate. So the two keys compare the same way for
      any two options of the same mover.
    - Hence every step chooses the same options, and the stop rules agree. ∎
- Corollary SEG-CAP (𝓛_d, d ≥ 2). For every run, seg1, mid and tail are each ≤ T*(d − 1).
  - Proof. Each is (the steps of) a maximal interval without a level-0 step. By P-IDEAL-SEG Lemma SEG with l = 0, it is a prefix of the
    run of H (level-0 movers frozen, degree 1) from a state. By SHIFT, H is run-equivalent to H↓, which has levels 0, …, d − 2:
    - new level 0: the two former level-1 movers (degree 2) and the frozen former level-0 movers (degree 1);
    - new level l ≥ 1: the former level l + 1.
    - So H↓ ∈ 𝓛_(d−1), and the prefix has length ≤ T*(d − 1). (mid is a union of at most one interval, since there are ≤ 2 level-0
      steps.) ∎
- Lemma LIFT (IDEAL-ACYC, any degree, any width). Given G with levels 0, …, d − 1, build G^:
  - every mover goes one level up;
  - two new level-0 movers A, B of degree 2 are added, whose options have Ξ-target X, new distinct top ranks with even parity, the
    larger rank on option 0, start at option 0, and new top gates;
  - every option of a former level-0 mover gets W-target A.
  - Then G^ is IDEAL-ACYC, and from (start of G, A and B at 0) its run equals G's run on the old movers; A and B never move.
  - Proof.
    - A and B: each option's Ξ-value is its own β (target X). Option 0 has the larger rank and even parity, so it is strictly better.
      At option 0, A_s = {0}, so they never move. No option has A or B as Ξ-target, so every old chain and Ξ-value is unchanged.
    - Keys: every old option's key in G^ is (g(A, 0)) followed by its key in G, because its W-chain now ends at A's option 0. A common
      first entry does not change any comparison.
    - So every step chooses the same options at the old movers, and the stop rules agree. If G is a d-level 2-wide ladder (with
      padding), G^ ∈ 𝓛_(d+1). ∎
- Corollary. T*(d − 1) ≤ T*(d) ≤ 3 T*(d − 1) + 2 (lower: LIFT; upper: SEG-CAP and SEG-ONCE's ≤ 2 level-0 steps). max over 𝓛_d of
  seg1 = T*(d − 1) (≥ by LIFT, whose lifted run has no level-0 step; ≤ by SEG-CAP).
- Does NOT claim: any polynomial bound; SLOT-TRADE.

## 2. Files and status
- experiments/new/box158/:
  - three.py: segment lengths;
  - lift.py: the LIFT construction, with a run comparison (SAME);
  - lift_*.json: lifted champions.
- PROVED (lane): SHIFT, SEG-CAP, LIFT, and the corollary. DEAD (route): «linear first segments». CONJECTURE: SLOT-TRADE. OPEN:
  IDEAL-ACYC-POLY, G-N5-TIME.
