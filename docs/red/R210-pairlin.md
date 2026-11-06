# R210 (the Lead's «R209 re-aimed», 02:46Z) Adversarial search on CONJECTURE PAIR-LIN: best pair flips F against |W| per level and d (L-RED successor 50)
Started 2026-11-06 03:1xZ (date -u). Target: CONJECTURE PAIR-LIN, flips(p, q) ≤ c·|{p, q} ∪ W(p) ∪ W(q)| for same-level pairs. The
search maximises F / |W| and F − 2|W| over co-designed genomes (no fixed base). A kill would be F growing superlinearly in |W|;
otherwise the result is a stable ratio (DATA for c).
Model: IDEAL-ACYC (RESULTS R104), degree 2. Labels: DATA, PROVED (lane; here only L-NEW's, quoted). Not a TARGET.md claim. G-N5-TIME
stays OPEN.

## 0. Answers
- No kill. On every file the best pair has F ≤ 2|W|, i.e. F − 2|W| ≤ 0. Equality holds only at |W| 6 (F 12; c4x_d5_F12 and its
  co-designed relatives at d 6, 7). The ratio does not grow: it falls to 1.75 at |W| 8 and to 1.5 at |W| 10.
- On ladders the structure is per level, not per d.
  - L-NEW's Corollary LADDER (P-IDEAL-KEYS §4, PROVED lane, quoted): «F(l) ≤ 2 + 3 F(l − 1) and F(l) ≤ 3^(l+1) − 1; and F(l) ≤ T for
    every l».
  - This bound does not depend on d, so adding levels above cannot raise F(l) past 3^(l+1) − 1.
  - In the climbs, adding levels does not raise F(l) at all once a clock is in place: F(2) = 12 at d 5, 6, 7 and F(3) = 14 at
    d 5, 6, 7, 8.
- Best pair flips found per level (ladders 𝓛^R_d; |W| = 2(l + 1); DATA lower bounds unless marked EXACT):

  | level l | |W| | best F | F − 2|W| | F / |W| | file (d, T) | LADDER cap 3^(l+1) − 1 |
  | --- | --- | --- | --- | --- | --- | --- |
  | 0 | 2 | 2 (EXACT: level-0 movers move ≤ 1) | −2 | 1.00 | any | 2 |
  | 1 | 4 | 6 | −2 | 1.50 | dbl_d3_F6 (3, 8); EXACT carry max (R197) | 8 |
  | 2 | 6 | 12 | 0 | 2.00 | c4x_d5_F12 (5, 12); f2_d6 (6, 13); f2_d7 (7, 16) | 26 |
  | 3 | 8 | 14 | −2 | 1.75 | dd_d5_F14 (5, 14); f3_d6 (6, 18); f3_d7 (7, 22); f4_d8 (8, 23) | 80 |
  | 4 | 10 | 15 | −5 | 1.50 | f4_d8 (8, 23) | 242 |
  | 5 | 12 | 14 | −10 | 1.17 | f4_d8 (8, 23) | 728 |

- Per d (best pair anywhere, with |W| and T):

  | d | best F (|W|) | T | file |
  | --- | --- | --- | --- |
  | 4 | 10 (6) | 10 | dbl_d4_F10 (R197, EXACT carry max at d 4) |
  | 5 | 14 (8); 12 (6) | 14; 12 | dd_d5_F14; c4x_d5_F12 |
  | 6 | 14 (8); 12 (6) | 18; 13 | f3_d6; f2_d6 |
  | 7 | 14 (8 and 10); 12 (6) | 21; 16 | f4_d7; f2_d7 |
  | 8 | 15 (10); 14 (8, 12) | 23 | f4_d8 |

- Increments of the best F per level: 2, 6, 12, 14, 15 (+4, +6, +2, +1). The best F flattens.
  - This is consistent with F ≤ T (CASCADE, L-NEW) and with T growing only linearly in d (R207).
  - Reading: the observed limit is the step count, not the cascade. LADDER's cascade could allow 3^(l+1) − 1 flips, but no run has
    the steps for it.
- With helpers (AUX 2, free W): mc6A (d 6) reaches F 12 at |W| 6 again. The helper pairs at levels 4-5 have F 4 at |W| 11-13.
  Helpers did not help the margin.
- The top pair specifically (FTW climbs, d 4 / 6, ft4R / ft6R): F 8 at |W| 8 and F 6 at |W| 12. Top pairs flip less than middle
  pairs, because the run ends before a top clock can cycle.

## 1. Verification
- Every kept file (r210/keep/: f2_d6, f2_d7, f3_d6, f3_d7, f4_d7, f4_d8, mc6A, ft4R, ft6R) was replayed:
  - r187/ideal.py;
  - L-NEW box166 verify_kill: well-formed, acyclic;
  - box150 check.py: XSIM 0, VIOL 0;
  - r189/lemck.py: 0 violations on every check (real FL runs of N5 «from the stated start pairs»).
- Pair flips were computed by my diag.py and by L-NEW's box168/pairflips.py; the two agree on every file.
- Seeds: c4x_d5_F12, dd_d5_F14, dbl_d4_F10 (R197 / R198 pins).

## 2. Tools
- r207/gclimb.py SCORE=MARGIN (max over same-level pairs of F − 2|W|), FTW (top pair), FLEV with PL=l (the level-l pair's F, then T).
- Climb logs: r210/out/ (not committed).
