# counter_rr

**Verdict:** CONFIRMED. rr (the target) grows by b = 1.618 (Fibonacci-like), as does zlk; rrdp grows slowly (b = 1.06); contrast tl and psi are constant (2 and 6) up to N = 40. Positional strategies were not checked in this sweep (the check was added to sweep.py during it); a re-run with strategy checks is pending.

- Generator source: github.com/trolando/oink @ 8fbf0a7c3e5b0baa254cb4516258c5c42fa99db1, src/tools/counter_rr.cpp
- Command: `tools/oink/build/counter_rr N` (N = family parameter)
- What the source says: Oink README.md:190: 'Counterexample to the RR solver'
- Paper: none given (awaiting source)
- Targeted solvers: oink-rr, oink-rrdp; contrast: oink-tl, oink-psi, oink-zlk
- Agreement: every solver that finished on an instance gave the same winner on every vertex (py-zlk, the independent Python Zielonka, included while it finished). Run statuses: ok 78, skipped 3, timeout 3.
- Re-run: `experiments/hard-families/run_all.sh counter_rr` (Oink built by scripts/setup_oink.sh).

## Growth over the last finished sizes
b: fitted base of work ~ b^N; k: fitted exponent of work ~ n^k (n = vertices). An exponential family shows k rising with N and b > 1 stable; a polynomial one shows b -> 1.

| solver | sizes N | b (per +1 in N) | k (in n) | work at largest N |
|---|---|---|---|---|
| py-zlk | 14..20 | 1.907 | 10.84 | 1294985 iterations |
| oink-zlk | 20..32 | 1.618 | 12.25 | 12752024 iterations |
| oink-rr | 20..32 | 1.618 | 12.25 | 7881194 promotions |
| oink-rrdp | 24..40 | 1.063 | 1.94 | 629 promotions |
| oink-tl | 24..40 | 1.000 | 0.00 | 2 iterations |
| oink-psi | 24..40 | 1.000 | 0.00 | 6 major iterations |

## Sweep table

| N | n | m | d | oink-rr (promotions) | oink-rrdp (promotions) | oink-zlk (iterations) | oink-tl (iterations) | oink-psi (major iterations) | py-zlk (iterations) |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 8 | 16 | 4 | 2 / 2.9e-05 | 2 / 2.8e-05 | 3 / 0.000492 | 2 / 2.2e-05 | 6 / 0.000486 | 8 / 0.0304 |
| 4 | 16 | 32 | 8 | 9 / 2.2e-05 | 8 / 3.4e-05 | 13 / 0.000533 | 2 / 2.7e-05 | 6 / 0.000653 | 36 / 0.0327 |
| 6 | 24 | 48 | 12 | 27 / 3.4e-05 | 17 / 4.4e-05 | 41 / 0.000484 | 2 / 2.4e-05 | 6 / 0.000402 | 143 / 0.0355 |
| 8 | 32 | 64 | 16 | 74 / 6.6e-05 | 29 / 7.1e-05 | 116 / 0.000631 | 2 / 4e-05 | 6 / 0.000557 | 542 / 0.0309 |
| 10 | 40 | 80 | 20 | 197 / 0.000108 | 44 / 4.5e-05 | 314 / 0.000494 | 2 / 5e-05 | 6 / 0.000589 | 2010 / 0.0554 |
| 12 | 48 | 96 | 24 | 519 / 0.000137 | 62 / 6.3e-05 | 834 / 0.000774 | 2 / 3.1e-05 | 6 / 0.000514 | 7376 / 0.0865 |
| 14 | 56 | 112 | 28 | 1362 / 0.000523 | 83 / 7.7e-05 | 2197 / 0.000911 | 2 / 3.3e-05 | 6 / 0.000517 | 26927 / 0.113 |
| 16 | 64 | 128 | 32 | 3569 / 0.000731 | 107 / 0.00018 | 5767 / 0.00155 | 2 / 3.8e-05 | 6 / 0.000482 | 98039 / 0.385 |
| 18 | 72 | 144 | 36 | 9347 / 0.00186 | 134 / 0.000125 | 15115 / 0.00307 | 2 / 3.8e-05 | 6 / 0.000744 | 356449 / 1.22 |
| 20 | 80 | 160 | 40 | 24474 / 0.0074 | 164 / 0.000255 | 39590 / 0.00817 | 2 / 4e-05 | 6 / 0.000508 | 1294985 / 4.08 |
| 24 | 96 | 192 | 48 | 167759 / 0.0337 | 233 / 0.000204 | 271428 / 0.062 | 2 / 6.6e-05 | 6 / 0.000561 | timeout |
| 28 | 112 | 224 | 56 | 1149849 / 0.259 | 314 / 0.000375 | 1860481 / 0.375 | 2 / 8.3e-05 | 6 / 0.000465 | skipped |
| 32 | 128 | 256 | 64 | 7881194 / 1.75 | 407 / 0.000382 | 12752024 / 3.23 | 2 / 4.1e-05 | 6 / 0.00059 | skipped |
| 40 | 160 | 320 | 80 | timeout | 629 / 0.00148 | timeout | 2 / 4.8e-05 | 6 / 0.000822 | skipped |

![sweep](sweep.png)
