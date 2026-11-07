# Box 167 N5-PMPRIME: the corrected per-mover form PM′ = moves(x) ≤ (deg(x) − 1)(1 + desc(x) + κ(x)) — with a DYNAMIC κ (key flips reaching x through W) it is PROVED but empty (κ reaches T); with a STATIC κ (the W-closure size) it holds on all 263 files with slack ≥ 2, but summing it gives no recursion, and it would die by composition if T^R grows superlinearly
L-NEW successor 54, 2026-11-05 (date -u: see the commit). Lead brief BOX 167 (19:48Z). Labels: PROVED (lane, unrefereed) / DATA /
CONJECTURE / DEAD (instance) / READING. Model: RESULTS R104 (P-IDEAL-FLIP §0); R105 (LOCAL, KEYFLIP) as landed. Box 166 kill:
box166/out/KILL_PM_compose_dd_d5_F14.json (c025a4b6). Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Answer
- Definitions (W-side, from R104). W(x) := the movers reachable from x along W-targets of any option, transitively (the W-closure
  below x). Under s, key_s(x, k) is built only from the options s(y), y ∈ W(x) along the W-path, and the gates. Four κ's, by
  decreasing size of the information they carry:
  - κ_K(x) := KF_x, the key flips of x (R105 KEYFLIP);
  - κ_E(x) := WE_x := #{t : some mover of W(x) moves at step t};
  - κ_M(x) := WM_x := #{y ∈ W(x) : y moves at least once};
  - κ_S(x) := |W(x)| (static).
- (1) Screen (experiments/new/box167/pmprime.py): 263 file paths (all L-RED JSON genomes at 002f7cd1 + every L-NEW box 160-166 genome,
  incl. the box 166 kill), every mover. PM′ with κ_K, κ_E, κ_M, κ_S: 0 violations each. The chain KF_x ≤ WE_x: 0 violations.
  - The kill's mover 12 has moves 6, desc 4, KF 14, WE 14, WM 8, |W| 8. So κ_S, κ_M give bound 13, κ_E, κ_K give 19.
  - Smallest κ that makes the kill consistent: any κ(12) ≥ 1. The natural choice is κ_S = |W| = 8.
- PROVED (lane):
  - LOCAL-KP. KP_(s_t)(x) depends only on the options s_t(y), y ∈ W(x). So KF_x ≤ WE_x, and at degree 2 moves(x) ≤ 1 + KF_x ≤
    1 + WE_x (R105 KEYFLIP). Hence PM′ with κ_K or κ_E holds for every genome; desc is not even needed.
- (2) The recursion question:
  - Dynamic κ (κ_K, κ_E): summing gives T ≤ Σ_x (1 + desc(x) + KF_x). This is R105's T ≤ N + KF up to the desc term, and KF_x can
    equal T. Instance: dd_d5_F14 (claude/l-red r197/lag, sha1 06f0e501), movers 8 and 9 (level 4) have KF = WE = 14 = T, so the sum
    is ≥ T for trivial reasons. To bound κ_E one uses WE_x ≤ Σ_(y ∈ W(x)) moves(y). Per level, with w movers per level and M_l the
    largest moves at level l: M_l ≤ 1 + D + w·Σ_(j<l) M_j, so M_l ≤ (D + 1)(w + 1)^l: 3^l at w = 2. This is LEVEL-PRODUCT again.
    DEAD as a polynomial route.
  - Static κ (κ_S or κ_M): summing needs no recursion. T ≤ Σ_x (deg − 1)(1 + desc(x) + |W(x)|) ≤ (D − 1)(N + N(N − 1)) =
    (D − 1)N². This is a CONJECTURE of polynomial strength, CONJECTURE PM′_S. Data: 0 violations on 263 files. Every mover with
    desc + |W| ≥ 3 has slack ≥ 2; the best ratio T / Σ-bound is 0.31 (iso_d2_4).
  - READING (why PM′_S is fragile; not a kill). The box 166 composition gives a reader x of a clock pair up to ≈ KF(pair) moves at
    Ξ-cost desc ≈ 2 log_2(moves) (diamond violators: key-free 2^(desc/2+1) − 1 moves), provided the bits are realizable. So PM′_S
    survives composition only if some pair's flips stay ≤ |W(reader)| + O(log T) on every clock.
    - dd_d5_F14's top pair: 14 flips at |W| = 8 (ratio 1.75), so the margin is already thin.
    - On 𝓛^R a top-level mover has |W| = 2d − 2, and its pair's flips are at most T. They can be as large as T on some clocks
      (dd_d5_F14: 14 = T); whether they are on the T^R(d) maxima is not checked. If they are and T^R(d) grows faster than
      2d + O(log d), the composition kills PM′_S at some d. The exact data T^R = 2, 4, 8, 13 (d 1-4) against 2d − 2 = 0, 2, 4, 6
      already lies above.
    - The kill needs: (i) a pair flipping ≈ T^R(d) times (on dd_d5_F14 the top pair flips at every step), (ii) a violator using
      ≈ all flips (box 166 used 6 of 14), (iii) 2-3 such independent pairs. Open.
- So: dynamic PM′ is TRUE but carries no information beyond R105 KEYFLIP. Static PM′_S is polynomial but probably false at scale;
  its kill is a composition question (NEEDS).

## 1. Tightness data (box167/tight.py)
- Closest movers to PM′_S among desc + |W| ≥ 3: excess −2 (moves 3, desc 2, |W| 2) on nd2_like_g2_E2, nd2_d5_F12, iso_d3_6/7,
  dbl_d3_F6, and the box 166 kill's mover 14. No mover is within 1 of the bound.
- Per-mover detail of the kill (pmprime.py -v): level-4 movers 8, 9, 12, 13 all have KF = WE = 14 = T and |W| = 8; level-3 movers
  6, 7 have moves 7, KF 6, WE 9, |W| 6.

## 2. Next (Lead decides)
- Kill side for PM′_S: the box 166 composition scaled up. A clock with a pair whose flip count exceeds |W| + 2 log_2 (flips) + 2
  (L-RED's longest ladders; does the top pair of T^R(d) maxima flip at every step, as on dd_d5_F14?), plus a diamond violator (n = 4:
  desc 6, key-free 15) through the B-bit test (bbit.py) and compose2.py. I can run it if routed. The diamond n = 4 B-bit enumeration
  is heavier (8 movers) and needs a smarter search than full enumeration.
