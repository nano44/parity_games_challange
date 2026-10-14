# tc

**Verdict:** CONFIRMED. Exponential for the targets: tl, zlk, uzlk, rr, dp grow by b = 2.00 per +1 in N (fpi 1.92, tspm 2.74, zlkq 2.23 over shorter ranges; zlkq is claimed quasi-polynomial by Oink, which our range cannot separate from exponential). Contrast rtl and psi stay polynomial (b = 1.04, work ~ n^0.5) up to N = 32 (3232 vertices). Positional strategies were not checked in this sweep (the check was added to sweep.py during it); a re-run with strategy checks is pending.

- Generator source: github.com/trolando/oink @ 8fbf0a7c3e5b0baa254cb4516258c5c42fa99db1, src/tools/tc.cpp
- Command: `tools/oink/build/tc N` (N = family parameter)
- What the source says: Oink README.md:199-219: 'Two binary counters ... exponential lower bound for many algorithms' (TL, FPI/FPJ/FPJG, NPP/PP/PPP/DP/RRDP, ZLK/UZLK/ZLKPP-STD, TSPM/SPM/MSPM); quasi-polynomial for ZLKQ/ZLKPP-WAW/ZLKPP-LIV/SSPM/QPT; polynomial for RTL/ORTL/PTL/SPPTL/DTL/IDTL/PSI
- Paper: T. van Dijk, A Parity Game Tale of Two Counters, GandALF 2019, doi:10.4204/EPTCS.305.8 (awaiting source)
- Targeted solvers: oink-tl, oink-zlk, oink-uzlk, oink-rr, oink-dp, oink-fpi, oink-tspm, oink-zlkq; contrast: oink-rtl, oink-psi
- Agreement: every solver that finished on an instance gave the same winner on every vertex (py-zlk, the independent Python Zielonka, included while it finished). Run statuses: ok 97, skipped 36, timeout 9.
- Re-run: `experiments/hard-families/run_all.sh tc` (Oink built by scripts/setup_oink.sh).

## Growth over the last finished sizes
b: fitted base of work ~ b^N; k: fitted exponent of work ~ n^k (n = vertices). An exponential family shows k rising with N and b > 1 stable; a polynomial one shows b -> 1.

| solver | sizes N | b (per +1 in N) | k (in n) | work at largest N |
|---|---|---|---|---|
| oink-tspm | 6..12 | 2.742 | 4.74 | 25938757 lifts |
| oink-zlkq | 6..12 | 2.231 | 3.78 | 13025476 iterations |
| oink-dp | 12..18 | 2.001 | 5.40 | 982882 promotions |
| oink-rr | 14..20 | 2.000 | 6.10 | 2097150 promotions |
| oink-tl | 6..12 | 2.000 | 3.25 | 8192 iterations |
| oink-zlk | 14..20 | 2.000 | 6.10 | 8388641 iterations |
| oink-uzlk | 14..20 | 1.996 | 6.08 | 5769223 iterations |
| py-zlk | 8..14 | 1.939 | 3.79 | 140699 iterations |
| oink-fpi | 8..14 | 1.922 | 3.80 | 2000320 iterations |
| oink-psi | 20..32 | 1.038 | 0.49 | 93 major iterations |
| oink-rtl | 20..32 | 1.037 | 0.48 | 34 iterations |

## Sweep table

| N | n | m | d | oink-tl (iterations) | oink-zlk (iterations) | oink-uzlk (iterations) | oink-rr (promotions) | oink-dp (promotions) | oink-fpi (iterations) | oink-tspm (lifts) | oink-zlkq (iterations) | oink-rtl (iterations) | oink-psi (major iterations) | py-zlk (iterations) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 22 | 36 | 11 | 8 / 3.6e-05 | 29 / 0.00302 | 43 / 2.7e-05 | 6 / 2.7e-05 | 9 / 3e-05 | 36 / 0.000268 | 221 / 5.5e-05 | 496 / 9.3e-05 | 4 / 3.8e-05 | 7 / 0.0173 | 65 / 0.0342 |
| 4 | 68 | 128 | 19 | 32 / 0.000135 | 129 / 0.000507 | 175 / 0.000141 | 30 / 7.1e-05 | 49 / 0.000171 | 787 / 0.000588 | 5449 / 0.000837 | 11571 / 0.00185 | 6 / 6.7e-05 | 13 / 0.000588 | 261 / 0.0323 |
| 6 | 138 | 276 | 27 | 128 / 0.000742 | 517 / 0.000746 | 545 / 0.000384 | 126 / 0.000269 | 220 / 0.00058 | 4284 / 0.00214 | 60768 / 0.0135 | 125167 / 0.0315 | 8 / 0.000138 | 17 / 0.000814 | 819 / 0.0473 |
| 8 | 232 | 480 | 35 | 512 / 0.0113 | 2057 / 0.0018 | 1747 / 0.00136 | 510 / 0.00112 | 927 / 0.00472 | 32220 / 0.0148 | 524557 / 0.118 | 520204 / 0.226 | 10 / 0.000253 | 23 / 0.00114 | 2657 / 0.088 |
| 10 | 350 | 740 | 43 | 2048 / 0.119 | 8205 / 0.00814 | 6157 / 0.00544 | 2046 / 0.00483 | 3790 / 0.0148 | 300449 / 0.174 | 3882653 / 1.03 | 4290402 / 3.04 | 12 / 0.000479 | 29 / 0.00208 | 9447 / 0.331 |
| 12 | 492 | 1056 | 51 | 8192 / 2.15 | 32785 / 0.0323 | 23279 / 0.025 | 8190 / 0.0274 | 15289 / 0.0795 | 591355 / 0.696 | 25938757 / 7.6 | 13025476 / 11.8 | 14 / 0.000874 | 35 / 0.00378 | 35877 / 1.29 |
| 14 | 658 | 1428 | 59 | timeout | 131093 / 0.145 | 91129 / 0.109 | 32766 / 0.152 | 61344 / 0.472 | 2000320 / 3.17 | timeout | timeout | 16 / 0.0013 | 41 / 0.00774 | 140699 / 6.85 |
| 16 | 848 | 1856 | 67 | skipped | 524313 / 0.827 | 361771 / 0.685 | 131070 / 0.514 | 245635 / 1.94 | timeout | skipped | skipped | 18 / 0.0034 | 47 / 0.00841 | timeout |
| 18 | 1062 | 2340 | 75 | skipped | 2097181 / 3.9 | 1443461 / 2.65 | 524286 / 2.55 | 982882 / 8.71 | skipped | skipped | skipped | 20 / 0.00317 | 53 / 0.021 | skipped |
| 20 | 1300 | 2880 | 83 | skipped | 8388641 / 16.9 | 5769223 / 11.1 | 2097150 / 11.7 | timeout | skipped | skipped | skipped | 22 / 0.00602 | 59 / 0.0186 | skipped |
| 24 | 1848 | 4128 | 99 | skipped | timeout | timeout | timeout | skipped | skipped | skipped | skipped | 26 / 0.00992 | 71 / 0.0644 | skipped |
| 28 | 2492 | 5600 | 115 | skipped | skipped | skipped | skipped | skipped | skipped | skipped | skipped | 30 / 0.028 | 81 / 0.0993 | skipped |
| 32 | 3232 | 7296 | 131 | skipped | skipped | skipped | skipped | skipped | skipped | skipped | skipped | 34 / 0.031 | 93 / 0.145 |  |

![sweep](sweep.png)
