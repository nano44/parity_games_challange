# L-ALG results (data only, unrefereed; updated 2026-10-15 12:40Z)
| candidate | (a) library (34) | (b) n <= 4 | (c) random n = 5..12 | (d) families | killer |
| --- | --- | --- | --- | --- | --- |
| NE(0) = psolC | 11 partial | 1,380 partial at n = 4 | 4 of 20,000 partial | tc, tc+, counter_symsi, counter_rr: 0 % | psolc_min_n4_m6 (A3) |
| C1 NE(1) | all solved | all solved | all solved | tc N <= 6, counter_symsi N <= 10 solved (others pending) | c1_k1_min_n7_m10 (walk) |
| C1 NE(2) | all | all | all | - | c1_k2_min_n11_m15 (walk) |
| C2 NE'(1) | all solved | all solved | (running) | (pending) | none found yet (walks to n = 20, crossover) |
Soundness: no wrong decision by any candidate on any game run (every decided vertex agrees with Zielonka).
Strategies: oracle extraction (the candidate itself) succeeded and verified on every completely solved game where it was run.
Time (Python, 1 core): NE(1) on tc n = 22/42/68/100/138: 0.0/0.2/1.9/7.6/26.9 s; N = 8 (n = 232) > 120 s (growth run pending).
