# counter_dp

**Verdict:** CONFIRMED. dp (the target) and pp grow by b = 2.07; zlk by 1.62; contrast tl (~linear) and psi (constant) up to N = 40. Positional strategies were not checked in this sweep (the check was added to sweep.py during it); a re-run with strategy checks is pending.

- Generator source: github.com/trolando/oink @ 8fbf0a7c3e5b0baa254cb4516258c5c42fa99db1, src/tools/counter_dp.cpp
- Command: `tools/oink/build/counter_dp N` (N = family parameter)
- What the source says: Oink README.md:191: 'Counterexample to the DP solver'
- Paper: none given (awaiting source)
- Targeted solvers: oink-dp, oink-pp; contrast: oink-tl, oink-psi, oink-zlk
- Agreement: every solver that finished on an instance gave the same winner on every vertex (py-zlk, the independent Python Zielonka, included while it finished). Run statuses: ok 72, skipped 8, timeout 4.
- Re-run: `experiments/hard-families/run_all.sh counter_dp` (Oink built by scripts/setup_oink.sh).

## Growth over the last finished sizes
b: fitted base of work ~ b^N; k: fitted exponent of work ~ n^k (n = vertices). An exponential family shows k rising with N and b > 1 stable; a polynomial one shows b -> 1.

| solver | sizes N | b (per +1 in N) | k (in n) | work at largest N |
|---|---|---|---|---|
| oink-pp | 16..24 | 2.066 | 15.12 | 65532657 promotions |
| oink-dp | 14..20 | 2.066 | 12.92 | 2434705 promotions |
| py-zlk | 14..20 | 1.839 | 10.85 | 1409972 iterations |
| oink-zlk | 20..32 | 1.618 | 12.74 | 25504082 iterations |
| oink-tl | 24..40 | 1.030 | 0.97 | 42 iterations |
| oink-psi | 24..40 | 1.000 | 0.00 | 6 major iterations |

## Sweep table

| N | n | m | d | oink-dp (promotions) | oink-pp (promotions) | oink-zlk (iterations) | oink-tl (iterations) | oink-psi (major iterations) | py-zlk (iterations) |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 12 | 19 | 6 | 5 / 2.4e-05 | 5 / 2.9e-05 | 11 / 0.000681 | 4 / 2.5e-05 | 6 / 0.000622 | 21 / 0.0415 |
| 4 | 20 | 33 | 8 | 23 / 4.1e-05 | 31 / 3.6e-05 | 32 / 0.000864 | 6 / 4.4e-05 | 6 / 0.000614 | 76 / 0.0327 |
| 6 | 28 | 47 | 10 | 99 / 8.8e-05 | 138 / 0.000103 | 90 / 0.000563 | 8 / 4.1e-05 | 6 / 0.000657 | 273 / 0.0383 |
| 8 | 36 | 61 | 12 | 410 / 0.000216 | 595 / 0.000197 | 242 / 0.000838 | 10 / 5.6e-05 | 6 / 0.000697 | 936 / 0.0344 |
| 10 | 44 | 75 | 14 | 1730 / 0.000674 | 2541 / 0.000591 | 640 / 0.000545 | 12 / 6e-05 | 6 / 0.000474 | 3177 / 0.0398 |
| 12 | 52 | 89 | 16 | 7353 / 0.00273 | 10841 / 0.00224 | 1682 / 0.0013 | 14 / 6.7e-05 | 6 / 0.000565 | 10760 / 0.0921 |
| 14 | 60 | 103 | 18 | 31330 / 0.012 | 46263 / 0.00976 | 4410 / 0.00208 | 16 / 0.000102 | 6 / 0.000586 | 36413 / 0.189 |
| 16 | 68 | 117 | 20 | 133664 / 0.0658 | 197445 / 0.0706 | 11552 / 0.00359 | 18 / 7.7e-05 | 6 / 0.000787 | 123196 / 0.626 |
| 18 | 76 | 131 | 22 | 570435 / 0.244 | 842732 / 0.204 | 30250 / 0.00535 | 20 / 9.3e-05 | 6 / 0.000508 | 416781 / 1.55 |
| 20 | 84 | 145 | 24 | 2434705 / 1.11 | 3597020 / 0.781 | 79202 / 0.0132 | 22 / 0.000151 | 6 / 0.000511 | 1409972 / 5.33 |
| 24 | 100 | 173 | 28 | timeout | 65532657 / 15.5 | 542882 / 0.0906 | 26 / 0.000184 | 6 / 0.000675 | timeout |
| 28 | 116 | 201 | 32 | skipped | timeout | 3720992 / 0.867 | 30 / 0.000228 | 6 / 0.000594 | skipped |
| 32 | 132 | 229 | 36 | skipped | skipped | 25504082 / 4.92 | 34 / 0.000163 | 6 / 0.000591 | skipped |
| 40 | 164 | 285 | 44 | skipped | skipped | timeout | 42 / 0.000217 | 6 / 0.000606 | skipped |

![sweep](sweep.png)
