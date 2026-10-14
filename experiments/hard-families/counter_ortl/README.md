# counter_ortl

**Verdict:** CONFIRMED. ortl (the target) grows by b = 2.00 (2048 iterations at N = 12, then timeout); contrast rtl, tl (2 iterations) and psi (6) constant up to N = 40. Positional strategies were not checked in this sweep (the check was added to sweep.py during it); a re-run with strategy checks is pending.

- Generator source: github.com/trolando/oink @ 8fbf0a7c3e5b0baa254cb4516258c5c42fa99db1, src/tools/counter_ortl.cpp
- Command: `tools/oink/build/counter_ortl N` (N = family parameter)
- What the source says: Oink README.md:197: 'Counterexample to the ORTL solver'
- Paper: none given (awaiting source)
- Targeted solvers: oink-ortl; contrast: oink-rtl, oink-tl, oink-psi
- Agreement: every solver that finished on an instance gave the same winner on every vertex (py-zlk, the independent Python Zielonka, included while it finished). Run statuses: ok 56, skipped 12, timeout 2.
- Re-run: `experiments/hard-families/run_all.sh counter_ortl` (Oink built by scripts/setup_oink.sh).

## Growth over the last finished sizes
b: fitted base of work ~ b^N; k: fitted exponent of work ~ n^k (n = vertices). An exponential family shows k rising with N and b > 1 stable; a polynomial one shows b -> 1.

| solver | sizes N | b (per +1 in N) | k (in n) | work at largest N |
|---|---|---|---|---|
| py-zlk | 10..16 | 2.184 | 10.10 | 2580476 iterations |
| oink-ortl | 6..12 | 2.000 | 6.10 | 2048 iterations |
| oink-rtl | 24..40 | 1.000 | 0.00 | 2 iterations |
| oink-tl | 24..40 | 1.000 | 0.00 | 2 iterations |
| oink-psi | 24..40 | 1.000 | 0.00 | 6 major iterations |

## Sweep table

| N | n | m | d | oink-ortl (iterations) | oink-rtl (iterations) | oink-tl (iterations) | oink-psi (major iterations) | py-zlk (iterations) |
|---|---|---|---|---|---|---|---|---|
| 2 | 11 | 17 | 8 | 2 / 2.8e-05 | 2 / 2.9e-05 | 2 / 3e-05 | 6 / 0.000528 | 31 / 0.035 |
| 4 | 21 | 33 | 14 | 8 / 4.9e-05 | 2 / 3.6e-05 | 2 / 2.8e-05 | 6 / 0.000427 | 182 / 0.0312 |
| 6 | 31 | 49 | 20 | 32 / 0.000203 | 2 / 5.4e-05 | 2 / 2.9e-05 | 6 / 0.000586 | 956 / 0.0343 |
| 8 | 41 | 65 | 26 | 128 / 0.00257 | 2 / 4.5e-05 | 2 / 3.2e-05 | 6 / 0.000535 | 4828 / 0.0568 |
| 10 | 51 | 81 | 32 | 512 / 0.0622 | 2 / 0.000112 | 2 / 4.8e-05 | 6 / 0.000734 | 23804 / 0.155 |
| 12 | 61 | 97 | 38 | 2048 / 1.71 | 2 / 6.3e-05 | 2 / 4.1e-05 | 6 / 0.000598 | 115196 / 0.512 |
| 14 | 71 | 113 | 44 | timeout | 2 / 0.000144 | 2 / 3.1e-05 | 6 / 0.000585 | 548860 / 2.6 |
| 16 | 81 | 129 | 50 | skipped | 2 / 8.1e-05 | 2 / 3.5e-05 | 6 / 0.00052 | 2580476 / 10.9 |
| 18 | 91 | 145 | 56 | skipped | 2 / 9.8e-05 | 2 / 3.7e-05 | 6 / 0.00061 | timeout |
| 20 | 101 | 161 | 62 | skipped | 2 / 0.000143 | 2 / 3.7e-05 | 6 / 0.00059 | skipped |
| 24 | 121 | 193 | 74 | skipped | 2 / 0.00013 | 2 / 5.5e-05 | 6 / 0.00053 | skipped |
| 28 | 141 | 225 | 86 | skipped | 2 / 0.000167 | 2 / 4.3e-05 | 6 / 0.00059 | skipped |
| 32 | 161 | 257 | 98 | skipped | 2 / 0.000204 | 2 / 3.6e-05 | 6 / 0.000526 | skipped |
| 40 | 201 | 321 | 122 | skipped | 2 / 0.000408 | 2 / 9.4e-05 | 6 / 0.000871 | skipped |

![sweep](sweep.png)
