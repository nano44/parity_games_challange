# Box 74 N5-FLIPS: top-pair key-order flips F in the IM frame. F ≤ |W| is FALSE at m = 3 for real genomes (a 7-step flip-free run whose top pair flips at every step); F ≤ 2|W| holds at m ≤ 3 only because F ≤ T; the m = 4 frame is out of reach
L-SI successor 40, 2026-11-06 (date -u: see the commit). Lead brief BOX 74 (02:46Z): feed CONJECTURE PAIR-LIN (key-order flips of a
same-level pair ≤ c·|W-closure|):
- compute the EXACT max top-pair flips F in the frame at m = 2, 3, then 4 if feasible, with T and |W|;
- decide whether F ≤ 2|W| (or another linear form) is UNSAT-provable at m = 3;
- put every SAT model with large F through a realiser.

Labels:
- PROVED (lane): proved here, not refereed.
- EXACT-SAT: CaDiCaL 1.5.3 via python-sat, one solver, proof unchecked. Every UNSAT is in experiments/si/UNSAT-LIST.txt (DIMACS sha1 and
  exact regeneration command; L-COMP 9 certifies them).
- DATA, READING.

Not a TARGET.md claim. PAIR-LIN, FLIP-ADD and G-N5-TIME stay OPEN.

## 0. Answer
- **Definitions.**
  - The top pair is (A_m, B_m).
  - Its key order under a state s is the BIT-CHAIN bit b_m(s) (box 64 BIT-CHAIN; P-IDEAL-KEYS §0 ord_s(A_m, B_m)).
  - F counts the steps t ∈ [1, T] with b_m(s_t) ≠ b_m(s_(t−1)). The bit of s_t is read with the external bit of the step that produced
    s_t, and a change is counted only at a step that moves.
  - |W| = |W(A_m) ∪ W(B_m)| = 2m: every mover below the top, level 0 included.
- **Frame maxima (EXACT-SAT; K = number of external-bit changes):**
  | m | |W| | K = 0 | K = 1 | K = 2 | K unlimited |
  | --- | --- | --- | --- | --- | --- |
  | 2 | 4 | 4 (= T_0 4) | 5 (= T_1 5) | 6 (T_2 7; F ≥ 7 UNSAT) | 7 (T_∞ 9; F ≥ 8 UNSAT) |
  | 3 | 6 | 7 (T_0 8; F ≥ 8 UNSAT 81 s) | 8 (T_1 10; F ≥ 9 UNSAT 964 s) | 10 (T_2 12; F ≥ 11 UNSAT 2,364 s) | not run |
- **Realised by real ISO R197 genomes (replayed with L-NEW's box 150 Gen, replayflip.py):**
  - m 3, K = 0, F = 7 (out/fl7_m3_s2..s4.json; s1 is a first climb that reached F 4 only): a 7-step flip-free run in which the top pair flips at every step (ord 01010101).
  - m 3, K = 2, F = 10 (out/fl10_K2_m3_s1..s3.json): a 10-step run with 2 external-bit changes and a flip at every step.
  - The lane's earlier real genomes (45 pins of boxes 64-73, tuned for T, not F) reach only F ≤ 5 at m 3 (fscan.out).
- **Consequences.**
  - **F ≤ |W| is FALSE at m = 3 for real genomes:** 7 > 6 flip-free.
  - **F ≤ 2|W| holds at m ≤ 3, but only through F ≤ T:** a flip needs a step, and T_k(3) ≤ 12 = 2|W| for k ≤ 2. It is therefore
    not a structural fact. The UNSAT answers above are the exact maxima, not a proof of a linear form.
  - The frame maximum equals T at K ≤ 1 and stays 1-2 below T at K ≥ 2.
  - K ≤ 2 is a RELAXATION of the (m+1)-level ladder 𝓛^R_(m+1): its level-0 pair flips at most twice (P-IDEAL-KEYS PAIR-MOVES: each
    level-0 mover of degree 2 moves at most once). So the m 3, K 2 value 10 bounds the top-pair flips of 𝓛^R_4, |W| = 6.
    - READING: whether a real level-0 pair can produce the realised 2-change schedule is not checked.
- **m = 4: not answered (DEAD as a method at this budget).**
  - Monolithic: F ≥ 10 (T ≤ 13) ran 5 h 46 min without an answer; killed, log kept as log/fl_K0_m4_T13_F10.killed.
  - The cube drivers were tried on the higher-priority query T_1(4) ≥ 15 (box 72 (2)):
    - cube74.py: Ξ-target split, 2 h, 78 leaves, 4 UNSAT;
    - cube74b.py: key bits, then start state, then Ξ-targets; 1 h 35 min, 80 leaves, none solved; cubes with 9 of 14 binary
      variables fixed still exceed 25 min.
  - READING: the m 4 frame encoding (an IM table over all 256 states per mover × 15 steps) is the bottleneck, not restart safety.
  - The Lead stopped the m 4 frame queries (14:13Z). Summaries: cubes_t1_m4_15.summary, cubes_t1_m4_15b.summary.

## 1. Frame mode flips (experiments/si/box70/frame.py)
- Mode `flips` m T F with env K. One run of ≤ T steps; idle steps are allowed only at the end (once idle, idle for good).
- b_m(s_t) is built by the BIT-CHAIN recursion from s_t. The level-m key bits c(m, k) are free.
- F_t = [b_m(s_t) ≠ b_m(s_(t+1))] ∧ (step t moves). The constraint is Σ F_t ≥ F (sequential counter).
- m 2 controls in check74.sh: F_max 4 (K 0), 6 (K 2), 7 (K unlimited).

## 2. Realisation
- realflip.py keeps the frame model's Ξ-graph and climbs the ENC data (ranks, parities, gates). Its score is the real F, max over
  starts, bits and (env K) external-bit schedules with ≤ K changes.
  - ord is computed from the R104 keys written out from the definition. Steps come from box 64 flipdp.Ext.step, which is XSIM-checked.
- replayflip.py replays a witness with L-NEW's box 150 Gen (read-only copy box64/ref), following the stored bit schedule. Exit 1 on
  any mismatch.

## 3. Also done in this box's time (box 72 remainder; logs experiments/si/box72/log/)
- m 3 frame: T_∞ ≥ 19 UNSAT (9,732 s) and T_3 ≥ 15 UNSAT (11,474 s). With the box 71 pins: T_∞(3) = 18 and T_3(3) = 14 EXACT-SAT;
  T_0..T_3 = 8, 10, 12, 14.
- SUM_2 at m 3 = 18 EXACT-SAT. Frame: (8, 10) SAT, (6, 12) SAT; (8, 11), (7, 11), (7, 12) UNSAT. The real genome
  box72/out/sum2_18_m3_s1.json has T_0 = 8, T_1 = 8, T_2 = 10 (flipdp bad 0; Gen replay k 2: 10 steps, 2 changes).
  So SUM_2(3) = 18 > 2T^R(3) + 1 = 17.
- m 4 T_0 ≥ 14 was dropped: L-RED R212 FROZEN-EMBED (C1) gives T_0(m) ≤ T^R(m) = 13 at m 4.

## 4. Files
- experiments/si/box74/: realflip.py, replayflip.py, fscan.py (+ fscan.out), run74.sh, cube74.py, cube74b.py, check74.sh (wired),
  pins.sha1, out/*.json, log/*.log, cubes_*.summary, cubes_t1_m4_15b.log.txt.
- experiments/si/box70/frame.py: modes flips, pq, bits; env NOPROOF, DUMPONLY, XCUBE.
- experiments/si/UNSAT-LIST.txt, experiments/si/unsat_regen.sh (23 of 23 sha1 OK).
- experiments/si/box72/: realsum.py, out/sum2_18_m3_s*.json, unsat/*.cnf.gz, log/.
