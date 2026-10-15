# L-ALG results (data only, unrefereed; updated 2026-10-15 11:50Z)
| candidate | (a) library (34) | (b) n <= 4 | (c) random n = 5..12 | (d) families | killer |
| --- | --- | --- | --- | --- | --- |
| NE(0) = psolC | 11 partial | 1,380 partial at n = 4 | 4 of 20,000 partial | tc, tc+, counter_symsi, counter_rr: 0 % | psolc_min_n4_m6 (A3) |
| C1 NE(1) | all solved | all solved | all solved | tc N <= 6, counter_symsi N <= 10 solved (others pending) | c1_k1_min_n7_m10 (walk) |
| C1 NE(2) | all | all | all | - | c1_k2_min_n11_m15 (walk) |
| C2 NE'(1) | all solved | all solved | 84,571 Strahler-2 games solved | S_3 (n=10) kills it | cross_h_k1_n10_m16 (Strahler 3) |
| C2 NE'(k) | - | - | - | sibling-trap family S_s: solved iff k >= s-1 (s <= 4) | strfam_S{k+2} |
| C3 ZP (Zielonka + psolC pruning) | == Zielonka, strategies verified | == Zielonka | == Zielonka, 8,000 games, <= 6 calls | all 13 families: <= 5 calls at every size run (tc N<=14, tc+ N<=12, symsi N<=12, rr N<=20, dp/m/core/rob/ortl/qpt/ladder/switch*: 1-2 calls); plain Zielonka exponential on 9 of them; S_s: 2^s-2 calls (linear in n) | DEAD: tiled family T_R (unit zp_ga_K8, step 18, 2 cross edges): 247 / 7,273 / 234,133 calls at n = 32/64/96 (x30 per tile); GA table 129/247/659/1,943/4,173/12,255 at n=24..64 |
Files: out/zp_families_c3_{a,b,c}.csv (per family and size: ZP calls, pruned vertices, time, plain Zielonka calls), instances/zp_ga_K*.pg.
Soundness: no wrong decision by any candidate on any game run (every decided vertex agrees with Zielonka).
Strategies: oracle extraction (the candidate itself) succeeded and verified on every completely solved game where it was run.
Time (Python, 1 core): NE(1) on tc n = 22/42/68/100/138: 0.0/0.2/1.9/7.6/26.9 s; N = 8 (n = 232) > 120 s (growth run pending).

## Oink solvers on the ZP killer family T_R (experiments/alg/out/oink_sweep_tile8.log; work counters at R = 1/2/3/4, n = 32/64/96/128)
| solver | R=1 | R=2 | R=3 | R=4 | reading |
| --- | --- | --- | --- | --- | --- |
| uzlk (plain Zielonka) | 166 | 4,891 | 157,447 | 5,077,039 | x32 per tile (= ZP's growth) |
| fpi | 171 | 4,045 | 104,469 | 2,715,493 | x26 per tile; tc already beats fpi |
| zlkq | 1,803 | 21,174 | 114,154 | 1,182,605 | x6-10; quasi-polynomial by its theorem |
| qpt | 30,323 | 22.9M | 289.6M | timeout 120 s | counter_qpt already beats qpt |
| tspm | 642 | 117,821 | 643,355 | 1,168,960 | tc already beats tspm |
| zlk (Oink, optimised) | 44 | 257 | 1,247 | 5,846 | ~x4.7, polynomial-looking |
| tl / ortl | 1 | 1 | 1 | 1 | one tangle |
| rtl | 1 | 5 | 9 | 14 | linear |
| ptl | 3 | 8 | 13 | 18 | linear |
| dtl, idtl | 4 | 8 | 12 | 16 | linear |
| spptl | 3 | 5 | 7 | 9 | linear |
| psi (major iterations) | 10 | 13 | 16 | 19 | linear |
| pp, dp, rr (promotions) | 3 | 5 | 7 | 9 | linear |
Reading: T_R is hard only for solvers already beaten by published families; tangle learning and priority promotion see through
the sibling-trap compositions that blind psolC.

## C5-DTL (Oink dtl, van Dijk; docs/alg/candidates/C5-DTL.md) correctness and strategies (experiments/alg/dtl_check.py, 13:05Z)
| set | games | dtl | idtl |
| --- | --- | --- | --- |
| library + lane instances | 122 | all regions == reference, strategies verified | same |
| all canonical n = 1, 2, 3 | 4 + 240 + 41,440 | all ok | all ok |
| psolC-partial canonical n = 4 | 1,380 | all ok | all ok |
| random canonical n = 4 | 20,000 (idtl 5,000) | all ok | all ok |
| random n = 5..12 (gen.py mix) | 4,000 | all ok | all ok |
Reference: harness Zielonka (n <= 30) or Oink tl (larger); strategies by harness verify.py (D2 change 5). No wrong region, no
bad strategy, no incomplete answer (dtl's run() can in principle stop with unsolved vertices; never observed).
