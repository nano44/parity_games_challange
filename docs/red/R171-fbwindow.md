# R171 fallbacks per TWO-FIX window: nothing above n − O(1); the size-indexed record is R100's lvl1 template (FB = n − 7, XO 1); seeded and random climbs do not raise FB; FB-XO not killed (L-RED successor 40)
Started 2026-11-01 04:38Z (Lead GO, date -u), written ~05:0xZ. Lead brief (R171): FB-per-window scaling from farrise25_n32 (FB 28) and
rise_fb38_n48 (L-NEW box 123: 34 fallbacks); target a size-indexed family with FB per window growing faster than n. L-NEW's CONJECTURE
FB-XO (FB ≤ (XO + 1)·n) means such a family needs XO growing, or it kills FB-XO. Score FB, XO, L, n, ODIFF.
Labels: DATA, READING, OPEN. Not a TARGET.md claim. G-N5-TIME stays OPEN. Engine: n5x.step (SPEC S1-S5); windows as L-NEW box 121;
XO as box 123 (window transitions changing Ξ at a vertex of O).

## 0. Answer
- No family with FB per window growing faster than n was found, and FB-XO is NOT killed.
- The only size-indexed family with FB ≈ n is R100's level-1 template, fb/lvl1.py (gate q1, source s1, chain c_1..c_m). Its fallback
  wave lies inside ONE TWO-FIX window with ODIFF 1 and XO 1, and FB = m = n − 7:

| m | n | K | FB | XO | L | ODIFF | FB / n |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | 15 | 10 | 8 | 1 | 9 | 1 | 0.53 |
| 16 | 23 | 18 | 16 | 1 | 17 | 1 | 0.70 |
| 32 | 39 | 34 | 32 | 1 | 33 | 1 | 0.82 |
| 64 | 71 | 66 | 64 | 1 | 65 | 1 | 0.90 |
| 128 | 135 | 130 | 128 | 1 | 129 | 1 | 0.95 |

  - FB / ((XO + 1)·n) tends to 1/2, so lvl1 sits inside FB-XO with room. (lvl1fb.py; for m ≥ 64 the gadget base B is raised to 2m + 10,
    which keeps the chain's odd priorities below the gadget. m ≤ 32 uses R100's B = 100.)
- The seeds, re-measured (fbscore.py, default S3 starts):

| instance | n | FB | XO | L | ODIFF | FB / n | FB / ((XO + 1)n) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| farrise25_n32 | 32 | 28 | 2 | 33 | 1 | 0.88 | 0.29 |
| rise_fb38_n48 | 48 | 34 | 0 | 35 | 1 | 0.71 | 0.71 |
| b5_os_n40 | 40 | 9 | 2 | 77 | 1 | 0.23 | 0.08 |
| returns_ph64 | 64 | 15 | 4 | 93 | 1 | 0.23 | 0.05 |
| runquad K 8 (R170) | 198 | 0 | — | 279 | 32 | 0 | 0 |

- Climbs (climb171.py: score = max FB in one window, then L; 6,000 mutations at fixed n; stopped before the push, best-so-far logged):
  - from farrise25 (2 seeds): FB stays 28, while L grows to 64 and XO to 3;
  - from rise_fb38: FB stays 34 (L 37);
  - random n 32 with 1 or 2 Odd choice vertices: FB 1.
  - Single mutations do not create a second wave. The seeds are local maxima of FB.

## 1. Why FB ≫ n is hard here (READING, not to sign)
- A fallback-only stretch of a window is Howard-style all-switch on the one-player game G_σ̄: S4c switches each improving vertex to
  its Ξ-best successor. T64 (Lead 03:45Z) reports that Howard is the one rule with known exponential lower bounds on deterministic
  one-player games, so a window made of fallbacks alone, on a Howard-hard G_σ̄, would be the strongest attack.
- It is blocked by FB-DISJ (box 123): at every fallback, S4a's G_τ arena optimum must be σ_j itself, so no Ξ-improving edge may be
  W-improving.
  - Pending ladder edges cannot exist. In runquad the pivot's higher levels are always Ξ-improving, and a fallback would take h's Ξ-best
    level C_K and destroy the gating. That is why runquad's S4a waves cannot simply be turned into fallback waves.
  - If W does not depend on σ along G_τ's plays from the switched vertices, each fallback moves a vertex to a successor of strictly
    smaller W, so a vertex falls back at most deg − 1 times and FB ≤ Σ (deg − 1) ≤ m. FB ≫ m needs W to be re-armed, and W rises only at
    S4a steps (box 122 W-MON-RUN).
  - Re-arming between waves is R100 §3's second-wave problem (designs O-A … O-D, each a sign contradiction on one prefix). It is unchanged.
- So a kill of FB-XO would need many waves without a Ξ-change on O, re-armed by S4a W-rises alone. FB ≫ n with XO growing would need the
  lvl1 wave repeated with a Ξ(o)-rise per wave, which is the runquad pattern with fallback waves. Neither was built. OPEN.

## 2. FREEZE's (NT) and P-N5-S4B (the Lead's 04:38Z question)
- Corollary S4B-KEEP (signed by both referees; Lead reading L45) gives, at every τ-stretch transition with I_τ ≠ ∅, that τ_k is Odd's
  pointwise optimum of H′_k. That is the VALUE half of FREEZE's S4b step (R170 §1), which R170 drew from R57's premise; it now also has a
  signed lemma behind it.
- It does NOT give the OUTPUT half. When another successor of an ODIFF vertex o ties with τ(o) in H′_F, S1's procedure may output it, so
  (NT) stays as a tie-break hypothesis only. A one-word change for R170 §1, to be done at the next edit of that note: «(NT), the
  tie-break part; optimality of τ in H′ is S4B-KEEP».

## 3. Tools (experiments/red/r171/)
- fbscore.py G START: per window L, FB, XO, ODIFF, FFSEG; BEST line.
- lvl1fb.py m...: lvl1 template scaling (out/lvl1.txt for m 64, 128).
- climb171.py, runclimb.sh: FB climbs (out/fbc_*.txt).

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/red/r171/*; notebook. SHAs in the push / message.
- FINDINGS:
  - No FB ≫ n family: the size-indexed record is lvl1, with FB = n − 7, XO 1, ODIFF 1 (m 128: FB 128 at n 135).
  - farrise25 and rise_fb38 are FB local maxima under climbing (28 / 34).
  - FB-XO holds on every instance here (max FB / ((XO + 1)n) = 0.71).
  - READING: fallback-only stretches are Howard on G_σ̄, but FB-DISJ forbids pending Ξ-improving edges. With W static, FB ≤ m.
  - S4B-KEEP covers FREEZE's value step; (NT) stays as a tie-break.
- NEEDS: Lead: redirect, or GO for (ii) (a TF-PH counterexample with D ≠ ∅). Context ~400k; I can do one more short box before
  parking at ~550k.
