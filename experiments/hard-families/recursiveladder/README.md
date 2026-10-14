# recursiveladder

**Verdict:** CONFIRMED (on the Python port). Zielonka grows by b = 1.618 per +1 in N in Oink uzlk/zlk/zlkpp-std and in the independent py-zlk (44.8M iterations at N = 34); contrast tl (~linear) and psi (constant) up to N = 38. Re-run 2026-10-14 with positional-strategy checks (harness/verify.py): every finishing solver's strategies verified, no disagreement.

- Generator source: github.com/tcsprojects/pgsolver @ d3cd624b61cd66739c45aff9554f6bbdcdd05401, src/lib/generators/recursiveladder.ml (Python port: pgsolver_port.py)
- Command: `python3 experiments/hard-families/pgsolver_port.py recursiveladder N` (N = family parameter)
- What the source says: PGSolver registers it as 'Recursive Ladder Game' (recursiveladder.ml:48); the repository does not state the target; it is cited in the literature as Friedmann's lower bound for the recursive (Zielonka) algorithm (Lead brief; awaiting source)
- Paper: O. Friedmann, recursive algorithm lower bound (awaiting source)
- Targeted solvers: oink-uzlk-raw, oink-zlk-raw, oink-zlkpp-std-raw; contrast: oink-tl-raw, oink-psi-raw
- Agreement: every solver that finished on an instance gave the same winner on every vertex (py-zlk, the independent Python Zielonka, included while it finished). Run statuses: ok 94, skipped 4, timeout 4.
- Re-run: `experiments/hard-families/run_all.sh recursiveladder` (Oink built by scripts/setup_oink.sh).

## Growth over the last finished sizes
b: fitted base of work ~ b^N; k: fitted exponent of work ~ n^k (n = vertices). An exponential family shows k rising with N and b > 1 stable; a polynomial one shows b -> 1.

| solver | sizes N | b (per +1 in N) | k (in n) | work at largest N |
|---|---|---|---|---|
| py-zlk | 20..26 | 1.618 | 10.99 | 1589049 iterations |
| oink-zlkpp-std-raw | 24..30 | 1.618 | 12.93 | 10695118 iterations |
| oink-uzlk-raw | 26..34 | 1.618 | 14.40 | 44791052 iterations |
| oink-zlk-raw | 26..34 | 1.618 | 14.40 | 44791053 iterations |
| oink-tl-raw | 28..38 | 1.031 | 1.00 | 38 iterations |
| oink-psi-raw | 28..38 | 1.000 | 0.00 | 10 major iterations |

## Sweep table

| N | n | m | d | oink-uzlk-raw (iterations) | oink-zlk-raw (iterations) | oink-zlkpp-std-raw (iterations) | oink-tl-raw (iterations) | oink-psi-raw (major iterations) | py-zlk (iterations) |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 10 | 19 | 8 | 5 / 2.7e-05 | 6 / 0.000819 | 5 / 2.6e-05 | 2 / 2.6e-05 | 4 / 0.000884 | 9 / 0.0413 |
| 4 | 20 | 41 | 14 | 20 / 4.3e-05 | 21 / 0.000498 | 30 / 7e-05 | 4 / 3.1e-05 | 10 / 0.00872 | 34 / 0.0517 |
| 6 | 30 | 63 | 20 | 59 / 3.6e-05 | 60 / 0.000431 | 94 / 0.000122 | 6 / 3.7e-05 | 10 / 0.000528 | 99 / 0.0548 |
| 8 | 40 | 85 | 26 | 161 / 0.000105 | 162 / 0.000589 | 261 / 0.000553 | 8 / 6.7e-05 | 10 / 0.000871 | 269 / 0.0449 |
| 10 | 50 | 107 | 32 | 428 / 9.9e-05 | 429 / 0.00119 | 698 / 0.000525 | 10 / 5.6e-05 | 10 / 0.000724 | 714 / 0.0379 |
| 12 | 60 | 129 | 38 | 1127 / 0.000318 | 1128 / 0.000868 | 1842 / 0.00168 | 12 / 4.7e-05 | 10 / 0.000918 | 1879 / 0.0632 |
| 14 | 70 | 151 | 44 | 2957 / 0.000891 | 2958 / 0.00142 | 4837 / 0.00545 | 14 / 5.1e-05 | 10 / 0.000819 | 4929 / 0.0708 |
| 16 | 80 | 173 | 50 | 7748 / 0.00293 | 7749 / 0.00267 | 12678 / 0.00901 | 16 / 7.6e-05 | 10 / 0.000713 | 12914 / 0.125 |
| 18 | 90 | 195 | 56 | 20291 / 0.00459 | 20292 / 0.00423 | 33206 / 0.0251 | 18 / 6.3e-05 | 10 / 0.00123 | 33819 / 0.253 |
| 20 | 100 | 217 | 62 | 53129 / 0.0125 | 53130 / 0.00872 | 86949 / 0.0797 | 20 / 0.000102 | 10 / 0.000609 | 88549 / 0.562 |
| 22 | 110 | 239 | 68 | 139100 / 0.0289 | 139101 / 0.0254 | 227650 / 0.16 | 22 / 0.000216 | 10 / 0.000868 | 231834 / 1.61 |
| 24 | 120 | 261 | 74 | 364175 / 0.0859 | 364176 / 0.0634 | 596010 / 0.546 | 24 / 8.1e-05 | 10 / 0.00089 | 606959 / 3.86 |
| 26 | 130 | 283 | 80 | 953429 / 0.204 | 953430 / 0.146 | 1560389 / 1.26 | 26 / 9.3e-05 | 10 / 0.000708 | 1589049 / 10 |
| 28 | 140 | 305 | 86 | 2496116 / 0.492 | 2496117 / 0.391 | 4085166 / 3 | 28 / 9.8e-05 | 10 / 0.00081 | timeout |
| 30 | 150 | 327 | 92 | 6534923 / 1.36 | 6534924 / 1.01 | 10695118 / 7.61 | 30 / 0.000215 | 10 / 0.000819 | skipped |
| 34 | 170 | 371 | 104 | 44791052 / 9.86 | 44791053 / 7.28 | timeout | 34 / 0.000126 | 10 / 0.000786 | skipped |
| 38 | 190 | 415 | 116 | timeout | timeout | skipped | 38 / 0.00016 | 10 / 0.000836 | skipped |

![sweep](sweep.png)
