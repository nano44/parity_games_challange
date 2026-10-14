# counter_core

**Verdict:** CONFIRMED. The Zielonka variants blow up: uzlk b = 3.64, zlkpp-std 2.85, zlk 2.62, py-zlk 3.66. Contrast tl (~linear) and psi (constant) up to N = 40. Positional strategies were not checked in this sweep (the check was added to sweep.py during it); a re-run with strategy checks is pending.

- Generator source: github.com/trolando/oink @ 8fbf0a7c3e5b0baa254cb4516258c5c42fa99db1, src/tools/counter_core.cpp
- Command: `tools/oink/build/counter_core N` (N = family parameter)
- What the source says: Oink README.md:194: 'Counterexample of Benerecetti, Dell'Erba, Mogavero, Robust Exponential Worst Cases for Divide-et-Impera Algorithms for Parity Games'
- Paper: Benerecetti, Dell'Erba, Mogavero, GandALF 2017, doi:10.4204/EPTCS.256.9 (awaiting source)
- Targeted solvers: oink-uzlk, oink-zlk, oink-zlkpp-std; contrast: oink-tl, oink-psi
- Agreement: every solver that finished on an instance gave the same winner on every vertex (py-zlk, the independent Python Zielonka, included while it finished). Run statuses: ok 54, skipped 26, timeout 4.
- Re-run: `experiments/hard-families/run_all.sh counter_core` (Oink built by scripts/setup_oink.sh).

## Growth over the last finished sizes
b: fitted base of work ~ b^N; k: fitted exponent of work ~ n^k (n = vertices). An exponential family shows k rising with N and b > 1 stable; a polynomial one shows b -> 1.

| solver | sizes N | b (per +1 in N) | k (in n) | work at largest N |
|---|---|---|---|---|
| py-zlk | 4..10 | 3.663 | 9.10 | 3353460 iterations |
| oink-uzlk | 6..12 | 3.636 | 11.77 | 17923881 iterations |
| oink-zlkpp-std | 8..14 | 2.850 | 11.72 | 40388068 iterations |
| oink-zlk | 10..16 | 2.618 | 12.74 | 21979505 iterations |
| oink-tl | 24..40 | 1.031 | 0.98 | 82 iterations |
| oink-psi | 24..40 | 1.000 | 0.00 | 6 major iterations |

## Sweep table

| N | n | m | d | oink-uzlk (iterations) | oink-zlk (iterations) | oink-zlkpp-std (iterations) | oink-tl (iterations) | oink-psi (major iterations) | py-zlk (iterations) |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 15 | 28 | 10 | 39 / 2.8e-05 | 28 / 0.00059 | 76 / 6.5e-05 | 6 / 3.8e-05 | 6 / 0.000517 | 92 / 0.0319 |
| 4 | 27 | 52 | 18 | 574 / 0.000114 | 209 / 0.000568 | 888 / 0.000416 | 10 / 4.4e-05 | 6 / 0.000482 | 1386 / 0.0441 |
| 6 | 39 | 76 | 26 | 7751 / 0.00239 | 1450 / 0.00338 | 8538 / 0.00379 | 14 / 5.7e-05 | 6 / 0.000901 | 18986 / 0.126 |
| 8 | 51 | 100 | 34 | 102914 / 0.0236 | 9956 / 0.00368 | 75256 / 0.0343 | 18 / 6.9e-05 | 6 / 0.000443 | 253419 / 0.808 |
| 10 | 63 | 124 | 42 | 1359342 / 0.216 | 68257 / 0.0121 | 630452 / 0.275 | 22 / 8.5e-05 | 6 / 0.000962 | 3353460 / 10.7 |
| 12 | 75 | 148 | 50 | 17923881 / 2.93 | 467858 / 0.0902 | 5106866 / 2.04 | 26 / 7e-05 | 6 / 0.000504 | timeout |
| 14 | 87 | 172 | 58 | timeout | 3206764 / 0.584 | 40388068 / 15.9 | 30 / 0.000109 | 6 / 0.000508 | skipped |
| 16 | 99 | 196 | 66 | skipped | 21979505 / 4.28 | timeout | 34 / 9.6e-05 | 6 / 0.000619 | skipped |
| 18 | 111 | 220 | 74 | skipped | timeout | skipped | 38 / 0.000103 | 6 / 0.000649 | skipped |
| 20 | 123 | 244 | 82 | skipped | skipped | skipped | 42 / 0.000112 | 6 / 0.000574 | skipped |
| 24 | 147 | 292 | 98 | skipped | skipped | skipped | 50 / 0.000149 | 6 / 0.000839 | skipped |
| 28 | 171 | 340 | 114 | skipped | skipped | skipped | 58 / 0.000295 | 6 / 0.00082 | skipped |
| 32 | 195 | 388 | 130 | skipped | skipped | skipped | 66 / 0.000236 | 6 / 0.000694 | skipped |
| 40 | 243 | 484 | 162 | skipped | skipped | skipped | 82 / 0.000413 | 6 / 0.00211 | skipped |

![sweep](sweep.png)
