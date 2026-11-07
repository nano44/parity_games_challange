# Box 71 N5-FRAMEK: the frame as the exact engine for flip data. CONJECTURE INF-2 is DEAD at m = 3: a real ISO ladder with T_∞ = 18 > 2T^R(3) + 1 = 17, found by realising a frame SAT model
L-SI successor 39, 2026-11-05 (date -u: see the commit). Lead brief BOX 71 (19:24Z; item (0) inserted 19:36Z and dropped 19:48Z):
- (1) m = 3: exact T_2, T_3, T_∞ and SUM_2;
- (2) m = 4: T_0, T_1 ≥ 15, T_2 ≥ 16;
- (3) DIMACS + sha1 and DRUP proofs for every UNSAT.

Labels:
- PROVED (lane): proved here or in boxes 64-70, not refereed.
- EXACT-SAT: CaDiCaL 1.5.3 via python-sat. A DRUP proof is RUP-checked with L-COMP's drup.c (a read-only copy in ref/) where stated.
- DATA, CONJECTURE, READING.

Not a TARGET.md claim. No polynomial bound. FLIP-ADD and G-N5-TIME stay OPEN.

## 0. Answer
- **CONJECTURE INF-2 (L-NEW box 163: T_∞(m) ≤ 2T^R(m) + 1) is DEAD at m = 3.**
  - Kill: pin/inf18_m3.json (sha1 2af7d941…), an ISO R197 ladder with levels 0-3.
  - T_∞ = 18 > 2·8 + 1 = 17 (T^R(3) = 8 EXACT: L-RED R197, L-COMP 27).
  - Computed by flipdp.py (box 64; all self-checks 0; XSIM against L-NEW's Gen): T_0..T_3 = 3, 5, 6, 8; T_∞ 18; LP 23.
  - Replayed step by step with L-NEW's box 150 Gen: start (0,0,1,0,1,0) above level 0, bit sequence 001010110101001010, 18
    steps, 14 bit changes.
  - How it was found:
    - the frame query «m 3, unlimited flips, T ≥ 18» came back SAT (1,118 s; DIMACS sha1 d0f2a0d4…);
    - its Ξ-graph was kept: upper options' targets [2, 3, 3, 2, 5, 4, 4, 5, X, X, 4, X], i.e. A1 → {A2, B2}, B1 → {B2, A2},
      A2 → {B3, A3}, B2 → {A3, B3}, A3 → X, B3 → {A3, X};
    - a hill-climb over real ENC data (ranks, parities, gates) on that graph reached T_∞ = 18 in 1,329 iterations (realise.py).
- **READING:**
  - INF-2 was multiplicative (T_∞ ≤ 2T^R + 1) and is false already at m = 3.
  - The kill uses many flips (14). So it says nothing about FLIP-ADD at fixed k, and nothing against SUM_1 (exact at m ≤ 3, box 70).
  - It shows unlimited flips can beat the «two runs» budget at m = 3.
- **Method (new, a lane tool): frame SAT → real genome.**
  - Fix the model's Ξ-graph and climb over ENC data with the exact engine.
  - It turned a frame SAT answer into a real kill in seconds. Every later frame SAT answer gets the same treatment.
- Items (1)-(2): §1 (as the solvers finish). Item (3): §2.
- Item (0), PM (dropped by the Lead after L-NEW's box 166 kill): frame DATA kept in pmlog/README.txt.

## 1. Results
| query | answer | time | DRUP | real lower bound |
| --- | --- | --- | --- | --- |
| m 3, T_∞ ≥ 18 | SAT | 1,118 s | — | REALISED: pin/inf18_m3.json (T_∞ 18; INF-2 kill) |
| m 3, T_2 ≥ 13 | UNSAT | 6,173 s | 5.7 GB, sha1 f02fab2a…; RUP check NOT finished (two runs of ~1.5 h, one cut by a container restart) | T_2(3) = 12 EXACT-SAT (unchecked proof), witness L-NEW ISO_1_d4_t12 |
| m 3, T_3 ≥ 14 | SAT | 3,697 s | — | REALISED: pin/t3_14_m3.json (sha1 bced21a8…; T_0..T_3 = 4, 8, 12, 14; Gen replay 14 steps, 3 changes) |
| m 3, T_∞ ≥ 19 | OPEN at park (~1.5 h, relaunched after the restart) | — | — | — |
| m 3, T_3 ≥ 15 | OPEN at park | — | — | — |
| m 4, T_1 ≥ 15 | OPEN at park (no proof logging) | — | — | — |
- Exact values at m = 3 now: T_0 = 8 (box 70), T_1 = 10 (box 70), T_2 = 12 (this box), T_3 ≥ 14, T_∞ ≥ 18. So the k-flip excess
  over T^R(3) = 8 is 2, 4 for k = 1, 2, i.e. +2 per flip so far. SUM_2 lower bound 17 (three genomes); its splits are queued.
- Relaunch lines, DIMACS sha1s and the proof state: experiments/si/box71/OPEN-QUERIES.txt.

## 2. Proof files (item 3)
- Every PROOF job writes dump/<tag>.cnf (gzipped and committed) and dump/<tag>.drup. On UNSAT the proof is RUP-checked in place by
  L-COMP's drup.c (copy in ref/), and its sha1 and size are logged. Proofs are gitignored. A gzipped proof > 50 MB is deleted after the
  check.
- m = 2 positive control: m2 T_1 ≥ 6, 52,447 lemmas, «s VERIFIED» (check71.sh).
- m 3 T_2 ≥ 13: 5.7 GB proof; the check did not finish before parking. That UNSAT is EXACT-SAT with an unchecked proof.
