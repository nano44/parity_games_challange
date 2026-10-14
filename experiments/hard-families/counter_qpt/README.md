# counter_qpt

**Verdict:** SUPER-POLYNOMIAL JUMPS OBSERVED, CLASS OPEN. With preprocessing off, qpt's lifts jump at N = 8 (x15 over N = 6) and N = 16 (x31 over N = 14), growing only ~N^3..N^4 in between (13.8M lifts at N = 28; timeout at N = 32, the next power of two). The jumps at powers of two fit a counter over log N bits, i.e. quasi-polynomial-type growth, but the data cannot fix the class. Contrast zlk, tl constant; sspm ~ n^2. Oink with default preprocessing solves the family outright. Re-run 2026-10-14 with positional-strategy checks (harness/verify.py): every finishing solver's strategies verified, no disagreement.

- Generator source: github.com/trolando/oink @ 8fbf0a7c3e5b0baa254cb4516258c5c42fa99db1, src/tools/counter_qpt.cpp
- Command: `tools/oink/build/counter_qpt N` (N = family parameter)
- What the source says: Oink README.md:193: 'Counterexample of Fearnley et al, An ordered approach to solving parity games in quasi polynomial time and quasi linear space'
- Paper: Fearnley, Jain, Schewe, Stephan, Wojtczak, SPIN 2017, doi:10.1145/3092282.3092286 (awaiting source)
- Targeted solvers: oink-qpt-raw, oink-sspm-raw; contrast: oink-zlk-raw, oink-tl-raw
- Agreement: every solver that finished on an instance gave the same winner on every vertex (py-zlk, the independent Python Zielonka, included while it finished). Run statuses: ok 82, skipped 2, timeout 1.
- Re-run: `experiments/hard-families/run_all.sh counter_qpt` (Oink built by scripts/setup_oink.sh).

## Growth over the last finished sizes
b: fitted base of work ~ b^N; k: fitted exponent of work ~ n^k (n = vertices). An exponential family shows k rising with N and b > 1 stable; a polynomial one shows b -> 1.

| solver | sizes N | b (per +1 in N) | k (in n) | work at largest N |
|---|---|---|---|---|
| oink-qpt-raw | 22..28 | 1.212 | 4.78 | 13815989 lifts |
| oink-sspm-raw | 28..128 | 1.030 | 2.00 | 16384 lifts |
| oink-zlk-raw | 28..128 | 1.000 | 0.00 | 2 iterations |
| oink-tl-raw | 28..128 | 1.000 | 0.00 | 1 iterations |
| py-zlk | 28..128 | 1.000 | 0.00 | 2 iterations |

## Sweep table

| N | n | m | d | oink-qpt-raw (lifts) | oink-sspm-raw (lifts) | oink-zlk-raw (iterations) | oink-tl-raw (iterations) | py-zlk (iterations) |
|---|---|---|---|---|---|---|---|---|
| 2 | 4 | 5 | 4 | 21 / 9.9e-05 | 4 / 4.9e-05 | 2 / 0.000453 | 1 / 1.7e-05 | 2 / 0.0306 |
| 4 | 8 | 11 | 8 | 113 / 6.4e-05 | 16 / 5.1e-05 | 2 / 0.000515 | 1 / 1.8e-05 | 2 / 0.0302 |
| 6 | 12 | 17 | 12 | 278 / 0.00025 | 36 / 6.1e-05 | 2 / 0.000479 | 1 / 1.9e-05 | 2 / 0.0363 |
| 8 | 16 | 23 | 16 | 4187 / 0.000814 | 64 / 6.5e-05 | 2 / 0.000648 | 1 / 1.8e-05 | 2 / 0.0352 |
| 10 | 20 | 29 | 20 | 9167 / 0.00173 | 100 / 7.7e-05 | 2 / 0.000446 | 1 / 2.1e-05 | 2 / 0.031 |
| 12 | 24 | 35 | 24 | 18004 / 0.00381 | 144 / 9e-05 | 2 / 0.000499 | 1 / 2.3e-05 | 2 / 0.0381 |
| 14 | 28 | 41 | 28 | 31364 / 0.0063 | 196 / 0.000102 | 2 / 0.000455 | 1 / 2e-05 | 2 / 0.0298 |
| 16 | 32 | 47 | 32 | 975553 / 0.245 | 256 / 0.000123 | 2 / 0.000714 | 1 / 1.9e-05 | 2 / 0.0321 |
| 18 | 36 | 53 | 36 | 1691882 / 0.483 | 324 / 0.000241 | 2 / 0.000535 | 1 / 3e-05 | 2 / 0.0324 |
| 20 | 40 | 59 | 40 | 2777523 / 0.783 | 400 / 0.000169 | 2 / 0.000487 | 1 / 1.9e-05 | 2 / 0.0485 |
| 22 | 44 | 65 | 44 | 4356444 / 1.45 | 484 / 0.000198 | 2 / 0.000385 | 1 / 2.2e-05 | 2 / 0.0562 |
| 24 | 48 | 71 | 48 | 6640131 / 1.9 | 576 / 0.00039 | 2 / 0.000395 | 1 / 2.7e-05 | 2 / 0.0419 |
| 26 | 52 | 77 | 52 | 9707208 / 2.88 | 676 / 0.000314 | 2 / 0.000632 | 1 / 2.7e-05 | 2 / 0.0334 |
| 28 | 56 | 83 | 56 | 13815989 / 4.26 | 784 / 0.000362 | 2 / 0.000463 | 1 / 2.1e-05 | 2 / 0.0323 |
| 32 | 64 | 95 | 64 | timeout | 1024 / 0.000385 | 2 / 0.000762 | 1 / 2.3e-05 | 2 / 0.0607 |
| 64 | 128 | 191 | 128 | skipped | 4096 / 0.00268 | 2 / 0.000863 | 1 / 3.9e-05 | 2 / 0.0366 |
| 128 | 256 | 383 | 256 | skipped | 16384 / 0.0149 | 2 / 0.000959 | 1 / 4.1e-05 | 2 / 0.0361 |

![sweep](sweep.png)
