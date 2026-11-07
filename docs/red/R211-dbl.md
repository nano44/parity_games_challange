# R211 DBL-O(1): three consecutive doubling levels F(l) = 2F(l − 1) + 2 — not realised; the obstruction is the step count (F ≤ T), exact at d 4 and for runs ≤ 16 steps at d 5 from F(0) = 0 (L-RED successor 50)
Started 2026-11-06 04:5xZ (date -u). Lead R211 (03:24Z / 04:37Z): L-NEW box 177 PAIR-DOUBLE (F(l) ≤ 2F(l − 1) + 2 on 𝓛^R_d; equality
needs a γ-equal pair renewed after every lower flip). Task: realise doubling at THREE consecutive levels (2 → 6 → 14 → 30), or name the
exact obstruction at the third level. Model: IDEAL-ACYC (RESULTS R104), 𝓛^R_d (R197 ladders). Labels: EXACT (CaDiCaL via r200/xcnf.py,
replayed), UNKNOWN, DATA, READING. Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Answers
- No instance. Two consecutive doubling levels are realised:
  - F = 2, 6 at levels 0-1: c4x_d5_F12, dbl_d4_F10, the d 4 witness below.
  - F = 0, 2, 6 at levels 0-2: d 3 witness r200/out/r211/v_c3 (replayed: F = [0, 2, 6], T 6).
  A third consecutive doubling is not realised anywhere.
- EXACT results. Engine: r200/xcnf.py with the new FMIN / FMAX options, which count flips of the level-l pair order Rk over the
  transitions of the run. TMIN = 0 and horizon H, so an UNSAT covers every run of at most H steps.

  | query | d | H | result | time | scope |
  | --- | --- | --- | --- | --- | --- |
  | F(0) ≥ 2, F(1) ≥ 6 (validation) | 3 | 8 = T*(3) | SAT, replay F [2, 6, …] | 3.7 s | all runs |
  | F(0) ≥ 2, F(1) ≥ 6, F(2) ≥ 10 (validation) | 4 | 13 = T^R(4) | SAT, replay F [2, 6, 10, 3] | 208 s | all runs |
  | F(0) ≥ 2, F(1) ≥ 6, F(2) ≥ 11 | 4 | 13 | UNSAT (reproduces R197's exact F_2 ≤ 10) | 112 s | all d 4 runs |
  | F(0) = 0, F(1) ≥ 2, F(2) ≥ 6, F(3) ≥ 14 (third doubling from 0) | 5 | 16 | UNSAT | 853 s | runs ≤ 16 steps |
  | F(0) ≥ 2, F(1) ≥ 6, F(2) ≥ 14 (A: third doubling from 2) | 5 | 16 | UNKNOWN (2 h cap) | — | — |
  | F(2) ≥ 13 (B) | 5 | 16 | UNKNOWN (2 h cap) | — | — |

  - PAIR-DOUBLE gives F(l) ≤ 2F(l − 1) + 2. So the lower bounds with FMAX 0:0 force EXACT equality: F = 0, 2, 6, 14.
- The obstruction at the third level is the STEP COUNT, not a missing renewal:
  - (i) F(l) ≤ T (CASCADE, L-NEW). Doubling from F(l − 1) needs T ≥ 2F(l − 1) + 2 steps. The chain from F(0) = 2 needs T ≥ 14
    for three doublings and T ≥ 30 for four.
  - (ii) d 4: T^R(4) = 13 < 14, so three consecutive doublings from F(0) = 2 are impossible (EXACT; the max is F(2) = 10). The
    chain from F(0) = 0 needs F(3) = 14 > 13, also impossible.
  - (iii) d 5, the closest instance: c4x_d5_F12, F = [2, 6, 12, 9, 2], T 12.
    - The level-2 pair (movers 4, 5) is γ-equal: both gates of 4 are below both gates of 5, (4, 14) vs (11, 17).
    - It flips at EVERY step 1-12. Mover 4 moves at 2, 4, 6, 10, 12; mover 5 at 1, 3, 5, 7, 11; level-1 flips are at 3, 5, 7, 8,
      9, 11.
    - So the pair is saturated (F(2) = T = 12). The doubling to 14 fails only because the run stops (stuck) after step 12.
    - Neither mover is un-renewed. There is no step left for them.
  - (iv) d 5 from F(0) = 0: UNSAT within 16 steps (EXACT for runs ≤ 16; whether any d 5 ladder run has ≥ 16 steps is the open
    MAIN cube question, conditional run cubes/d5c_t16).
- READING: «doubling for k consecutive levels» needs T ≥ 2^(k+2) − 2 steps on one ladder, while the best T found grows linearly in d
  (R207: T^R ≥ 18 / 20 at d 6 / 7). So in the data, DBL-O(1) holds for the same reason as SLOT-TRADE: steps saturate before
  doubling can repeat. That reduces DBL-O(1) to T^R(d) = poly(d). It is not an independent bound, and it is not proved.

## 1. Files
- r200/xcnf.py: FMIN "l:k" (≥ k flips of the level-l pair over the run's transitions) and FMAX "l:k" (≤ k), sequential counters.
- r200/out/r211/ (not committed; gitignored): logs and witnesses.
  - Relaunch lines: TMIN=0 SYMB=1 FMIN=<…> [FMAX=<…>] python3 xmax.py d H out.json.
  - The validation witnesses replay under r207/diag.py: v_4: F [2, 6, 10, 3]; v_c3: F [0, 2, 6].
