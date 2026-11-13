# L19: exact questions on box 217's one-player model 1P(G) by SAT (BOX L19; L-LOWER successor 16)
Labels: DATA (solver only) / DATA (DRUP-verified) / PROVED (lane). Lead briefs 09:08Z, 09:12Z (plan approved), 09:15Z (k-objective),
12:13Z (classes), 13:51Z (close: the question is settled from another side by L-RED-B's family G_k, packet P-N5-EXP, claude/l-red-b
350d84eb). Model: claude/l-new a32a588d, docs/new/N5-QUIETKEY-box217.md §1, experiments/new/box217/one217.py (key rule, ε = gate index,
= R104's IDEAL model per the Lead's 12:13Z note). Tools experiments/lower/l19/ (README). Every SAT below was decoded and replayed with
one217 (and N5 itself on Γ3 where marked «N5-checked»); every UNSAT is «solver only» unless marked DRUP-verified. All degree 2.

## 0. What the box asked and what a result means
- T(N): the largest key-run length over Ξ-acyclic degree-2 genomes with N movers (exact via «s_L ≠ s_(L−1)» SAT / UNSAT).
- ENUM (Lead 09:15Z): the smallest d at which some level-(k−1) mover makes |K| − 1 = 2^k − 1 switches (degree 2), per k.
- Scope: DATA about 1P(G) on the stated level profiles / classes; not a bound for N5; growth readings are READINGS.

## 1. Encoder (enc19.py) and its checks
- Symbolic genome on a fixed level-width profile W: W-targets (one-hot, level − 1), Ξ-targets (one-hot, exit or a mover; acyclic via
  the exact longest-path depth), β priorities (v2, default: pairwise rank order + sign per β; v1: rank-position permutation), per-level
  gate orders, start. One key step (one217.OneP.step) as a circuit; L steps unrolled; the step is total (a stopped run stays).
- Symmetry breaks (sound): s_0 = option 0 everywhere (option labels are arbitrary); Ξ-depth exact (one model per Ξ-graph).
- Checker validation (val19.py): random genomes fixed by unit clauses: SAT with exactly one217's states; a flipped state bit UNSAT.
  v1: 160 genomes on 5 profiles, v2: 90 genomes on 3 profiles: bad 0. L-RED-B's G_3 (experiments/red-b/data/b6b/G/G_3.json @ 350d84eb,
  N 11, W 2,2,3,4): checker SAT, states = one217's, T_key 6 (moving at L 6, stopped at L 7).
- v1 → v2: v1 could not find known SATs (k 3 at W 2,2,2,2,2 L 16: no answer 3,000 s); v2 made the N 4 UNSAT 18× faster (55 → 3.1 s).

## 2. Exact points
| question | profile / class | result | label |
| --- | --- | --- | --- |
| T(4) | all 8 compositions of 4 | T_max = 4 on every profile (L 4 SAT, replayed; L 5 UNSAT ≤ 3.1 s) | W 2,2: DRUP-verified (cnf eaac86cf, 109,408 lemmas); other 7: solver only |
| T(5), T(6) | — | not run (stopped for the job limit, then the box closed) | — |
| ENUM k = 2 | W 2,2 (N 4, d 2) | SAT: level-1 mover 3/3 switches, T 4, max_sw 3; N5-checked (n5 4, mism 0) | minimal: d ≥ 2 and two level-0 movers are forced (box 217 A3) |
| ENUM k = 3 | W 2,2,2 (N 6, d 3), general | UNSAT within L 8 (198 s) and within L 12 (596 s), v1 | solver only; horizon L 12 |
| ENUM k = 3 | W 2,2,2,2 (N 8), W 3,3,3 (N 9), W 2,2,2,2,2 (N 10) general | no answer (1,800-3,000 s caps, v1 and v2) | — |
| bi-ladder T, d 4 | LADDER, Ξ exactly one level up, top to exit, W 2,2,2,2 | T ≥ 7 SAT (one217 7, N5-checked n5 7 mism 0); L 8 UNSAT 71 s, L 9 UNSAT 79 s | SAT replayed; UNSAT solver only. Settles the 6-vs-7 discrepancy for 7 (L-SI's «exactly 6» is too low) |
| ENUM k = 3 upward ladder | LADDER, Ξ strictly higher or exit, d 5 (± β ranks by level) | UNSAT within L 12 (668 s; 31.5 s with BRANK) | solver only; horizon L 12 (T_max of the class at d 5 not computed) |
| ENUM k = 3 upward ladder | same, d 6 (N 12, M 24) | SAT both: T_key 8, k(G) 3, max_sw 7; N5-checked (n5 8, mism 0) | replayed; agrees with L-SI 55's independent encoder |
| ENUM k = 4 upward ladder | d 7, BRANK, L 20 | no answer 3,000 s; d 8 stopped (Lead 13:51Z) | — |
Instances frozen in experiments/lower/l19/inst/ (SHA1SUMS; replay.txt = rep19 with N5): E_K2_W22_L4 (k 2), ro22_L4 (T 4 at W 2,2),
bi4_L7 (bi-ladder d 4, T 7), U3d6 and U3d6b (upward ladder d 6, k 3, T 8); every line n5 = key, mism 0.

## 3. Readings (not claims)
- In the classes measured, full enumeration of depth k = 3 needs d 6 at width 2 (upward ladders), k = 2 needs d 2: the two points match
  L-SI's «k = d / 2». The Lead's 13:51Z note: L-RED-B's G_k (L(G_k) = 2^k − 2 at N = 9k − 16, proof by induction, N5 2^k + 1 iterations
  at k = 3..11) answers the box's underlying question from another side; L19 adds an independent exact replay of G_3 (§1).

## 9. Diff against TARGET.md
No statement here is about parity games' solvability or an algorithm's running time; all are about the key run of 1P(G) on degree-2
genomes and fixed level profiles. Not M3/M4, not a gauntlet pass.
