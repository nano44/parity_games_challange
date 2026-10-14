# tc+

**Verdict:** CONFIRMED. rtl (the target) and tl grow by b = 1.98, zlk by 2.00; contrast ortl (b = 1.10) and psi (1.08) stay polynomial (psi times out only at N = 32, 33984 vertices). Positional strategies were not checked in this sweep (the check was added to sweep.py during it); a re-run with strategy checks is pending.

- Generator source: github.com/trolando/oink @ 8fbf0a7c3e5b0baa254cb4516258c5c42fa99db1, src/tools/tc+.cpp
- Command: `tools/oink/build/tc+ N` (N = family parameter)
- What the source says: Oink README.md:200: 'TC modified to defeat the RTL solver'
- Paper: none given in the repository (awaiting source)
- Targeted solvers: oink-rtl, oink-tl, oink-zlk; contrast: oink-ortl, oink-psi
- Agreement: every solver that finished on an instance gave the same winner on every vertex (py-zlk, the independent Python Zielonka, included while it finished). Run statuses: ok 47, skipped 19, timeout 5.
- Re-run: `experiments/hard-families/run_all.sh tc+` (Oink built by scripts/setup_oink.sh).

## Growth over the last finished sizes
b: fitted base of work ~ b^N; k: fitted exponent of work ~ n^k (n = vertices). An exponential family shows k rising with N and b > 1 stable; a polynomial one shows b -> 1.

| solver | sizes N | b (per +1 in N) | k (in n) | work at largest N |
|---|---|---|---|---|
| oink-zlk | 12..18 | 2.000 | 3.55 | 2621464 iterations |
| oink-rtl | 4..10 | 1.981 | 1.68 | 1025 iterations |
| oink-tl | 4..10 | 1.981 | 1.68 | 1025 iterations |
| py-zlk | 6..12 | 1.943 | 2.07 | 95779 iterations |
| oink-ortl | 14..20 | 1.102 | 0.56 | 143 iterations |
| oink-psi | 18..28 | 1.084 | 0.62 | 251 major iterations |

## Sweep table

| N | n | m | d | oink-rtl (iterations) | oink-tl (iterations) | oink-zlk (iterations) | oink-ortl (iterations) | oink-psi (major iterations) | py-zlk (iterations) |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 24 | 38 | 15 | 5 / 3.9e-05 | 5 / 3.1e-05 | 32 / 0.000468 | 8 / 4.2e-05 | 6 / 0.000461 | 85 / 0.0321 |
| 4 | 104 | 196 | 27 | 17 / 0.000284 | 17 / 0.000129 | 156 / 0.00045 | 15 / 0.000177 | 12 / 0.000545 | 455 / 0.035 |
| 6 | 288 | 570 | 39 | 65 / 0.00341 | 65 / 0.0012 | 640 / 0.00153 | 24 / 0.000984 | 18 / 0.0013 | 1777 / 0.067 |
| 8 | 624 | 1256 | 51 | 257 / 0.0679 | 257 / 0.0174 | 2564 / 0.00355 | 35 / 0.00467 | 27 / 0.00337 | 6565 / 0.24 |
| 10 | 1160 | 2350 | 63 | 1025 / 1.62 | 1025 / 0.443 | 10248 / 0.0172 | 48 / 0.0202 | 36 / 0.0124 | 24731 / 0.915 |
| 12 | 1944 | 3948 | 75 | timeout | timeout | 40972 / 0.0888 | 63 / 0.0738 | 50 / 0.0274 | 95779 / 5.14 |
| 14 | 3024 | 6146 | 87 | skipped | skipped | 163856 / 0.523 | 80 / 0.227 | 69 / 0.0895 |  |
| 16 | 4448 | 9040 | 99 | skipped | skipped | 655380 / 3 | 99 / 0.799 | 96 / 0.165 |  |
| 18 | 6264 | 12726 | 111 | skipped | skipped | 2621464 / 12.5 | 120 / 1.89 | 112 / 0.299 |  |
| 20 | 8520 | 17300 | 123 | skipped | skipped | timeout | 143 / 4.46 | 141 / 0.589 |  |
| 24 | 14544 | 29496 | 147 | skipped | skipped | skipped | timeout | 200 / 3.98 |  |
| 28 | 22904 | 46396 | 171 | skipped | skipped | skipped | skipped | 251 / 11.2 |  |
| 32 | 33984 | 68768 | 195 | skipped | skipped | skipped | skipped | timeout |  |

![sweep](sweep.png)
