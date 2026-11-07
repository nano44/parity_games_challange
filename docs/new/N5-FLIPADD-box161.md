# Box 161 N5-FLIPADD (interim): proof side of FLIP-ADD on the external-flip model; one flip adds +1 at m = 1, 2 but ≥ +2 at m = 3, T_k(2) grows slowly with k (9 at k = 8); a flip is a swap of the level-1 W-targets (Lemma SWAP); no potential found yet
L-NEW successor 52, 2026-11-05 (date -u: see the commit). Lead GO 03:48Z (BOX 161: proof attempt of FLIP-ADD, T_2(m) ≤ T^R(m) + O(m), on the
external-flip model of box 160; check every candidate potential on T_k(m), m ≤ 3, exactly). Labels: PROVED (lane), EXACT, DATA,
CONJECTURE, READING. Model and notation: docs/new/N5-SLOT-box160.md §0-§1 (T^R, ISO, b_0, W-ONLY, T_k(m)). Not a TARGET.md claim.
No polynomial bound. FLIP-ADD, SLOT-TRADE and G-N5-TIME stay OPEN.

## 0. Answer (interim)
- No proof of FLIP-ADD yet. No candidate potential has been checked exactly yet (the only one tried, §2, was probed on random runs only).
- EXACT data (box160/iso.py FREE0 ISO KF = k; replayed with the schedule forced; table also in box 160 §0):
  - T_k(1) = 2, 3, 3, 3 for k = 0, 1, 2, ≥ 3. The bound for every k is PROVED (lane) (box 160 Lemma FLIP-1).
  - T_k(2) = 4, 5, 7, 8, 8 for k = 0..4, and T_8(2) = 9.
  - T_0(3) = 8: by W-ONLY, the NOL0 maximum at d 4 (exact 8) covers every run with b_0 constant.
  - T_1(3) ≥ 10, and ≥ 11 is running. T_2(3) ≥ 12, from the ISO d 4 witness.
- READING:
  - The increment of one flip over T^R(m) is 1, 1, ≥ 2 for m = 1, 2, 3. So the clean «+1 per flip» pattern of m ≤ 2 does not continue.
  - The increment of two flips is 1, 3, ≥ 4. Both rows are still consistent with FLIP-ADD (O(m) per flip). Nothing kills it.
  - At m = 2, more flips keep helping, slowly: increments 1, 3, 4, 4 for k = 1..4, and 5 at k = 8. A fresh (m)-run per flip would add
    4 per flip.

## 1. PROVED (lane)
- Lemma SWAP (𝓛^R_d, ISO). Let H_c be the genome with level 0 frozen at a configuration with b_0 = c. Let H_c^swap be H_c with the
  W-targets of the two options of each level-1 mover exchanged: option k now points to level-0 mover 1 − k, and its gate, Ξ-target and
  β are unchanged. Then H_(1−c) and H_c^swap take the same step from every state.
  - Proof.
    - Ξ-data, hence A-sets, are unchanged.
    - Two options of a level-1 mover x. In H_c^swap, option k has key (gate of level-0 mover (1 − k)'s frozen option, g(x, k)). So x's
      key order is the reverse of its order in H_c, which is its order in H_(1−c).
    - The two level-1 movers sit at different options. Their keys compare by the level-0 movers they point to, and these are exchanged.
      So the comparison is reversed relative to H_c, as in H_(1−c).
    - The two level-1 movers sit at the same option. Both point to the same level-0 mover, and they compare by their own gates. That
      comparison is the same in all three genomes.
    - Every comparison at level ≥ 2 is decided by comparisons at the level below (box 160 Lemma W-ONLY (ii)). ∎
  - So a run with k external flips is a concatenation of k + 1 runs of two FIXED genomes, H_c and H_c^swap, which differ only in the
    W-targets of level 1. Each piece starts where the previous one stopped.
  - H_c^swap lies in 𝓛_d (any W-targets) but not in the R197 convention 𝓛^R_d. So T^R alone does not cap its pieces; T* over 𝓛_d does
    (F-1 of box 160).
  - Does NOT claim: any bound.

## 2. DATA (weak): potential probe
- box161/psi.py: Ψ(s) := max(R_0(s), R_1(s)), the larger of the two frozen remainders. Measured along random ISO ladders with random
  flip schedules.
- Ψ does not decrease at up to 2 steps per run with ≤ 2 flips. Excess T − Ψ(s_0) is at most 3.
- But random runs are short (max T 4 at d = 3, 4), so this says little. Not an exact check.

## 3. Next (proposal)
- Exact checks of state potentials by SAT. A candidate Φ(s) enters as «Φ(s_t) ≥ Φ(s_(t−1)) at a non-flip step», added to iso.py
  (UNSAT = Φ strictly decreases on every no-flip step in the frame).
- First candidates:
  - (a) the number of armed movers (s(x) ≠ KP(x)) weighted by level;
  - (b) the same plus the number of Ξ-unhappy movers;
  - (c) lexicographic (MONO value vector, armed vector).
- Then bound the jump of Φ at a flip by O(m), using Lemma SWAP (a flip changes KP only at level 1, plus the carry along split levels).
- Files: experiments/new/box161/ext.py (simulator of E_m under a schedule, frozen remainders), xtrace.py (trace), psi.py (probe).
