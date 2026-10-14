# switchbestexp

**Verdict:** NOT CONFIRMED: targeted algorithm (PGSolver's switch-best SI) not run, as for switchallexp. Oink psi ~ linear (390 at N = 64); ssi, zlk, tl constant; py-zlk grows mildly (b = 1.47 over N = 2..16, it then timed out on these sizes because of Python recursion cost). Positional strategies were not checked in this sweep (the check was added to sweep.py during it); a re-run with strategy checks is pending.

- Generator source: github.com/tcsprojects/pgsolver @ d3cd624b61cd66739c45aff9554f6bbdcdd05401, src/lib/generators/policyiter/generators/switchbestexp.ml (Python port)
- Command: `python3 experiments/hard-families/pgsolver_port.py switchbestexp N` (N = family parameter)
- What the source says: ident 'switchbestexp'; its description string (line 79) repeats the switch-all text; target presumably PGSolver's 'switchbest' SI (stratimpralgs/switch_globally_best.ml:119)
- Paper: O. Friedmann, strategy-improvement lower bounds (awaiting source)
- Targeted solvers: PGSolver switchbest SI (not run, see README); contrast: oink-psi-raw, oink-ssi-raw, oink-zlk-raw, oink-tl-raw
- Agreement: every solver that finished on an instance gave the same winner on every vertex (py-zlk, the independent Python Zielonka, included while it finished). Run statuses: ok 33, skipped 1, timeout 1.
- Re-run: `experiments/hard-families/run_all.sh switchbestexp` (Oink built by scripts/setup_oink.sh).

## Growth over the last finished sizes
b: fitted base of work ~ b^N; k: fitted exponent of work ~ n^k (n = vertices). An exponential family shows k rising with N and b > 1 stable; a polynomial one shows b -> 1.

| solver | sizes N | b (per +1 in N) | k (in n) | work at largest N |
|---|---|---|---|---|
| py-zlk | 2..16 | 1.470 | 2.83 | 4329 iterations |
| oink-psi-raw | 8..64 | 1.034 | 0.97 | 390 major iterations |
| oink-ssi-raw | 8..64 | 1.000 | 0.00 | 1 major iterations |
| oink-zlk-raw | 8..64 | 1.000 | 0.00 | 2 iterations |
| oink-tl-raw | 8..64 | 1.000 | 0.00 | 1 iterations |

## Sweep table

| N | n | m | d | oink-psi-raw (major iterations) | oink-ssi-raw (major iterations) | oink-zlk-raw (iterations) | oink-tl-raw (iterations) | py-zlk (iterations) |
|---|---|---|---|---|---|---|---|---|
| 1 | 35 | 70 | 34 | 12 / 0.000628 | 1 / 4.8e-05 | 2 / 0.000494 | 1 / 2.8e-05 | 7 / 0.0321 |
| 2 | 60 | 130 | 60 | 18 / 0.000443 | 1 / 6.8e-05 | 2 / 0.000803 | 1 / 2.2e-05 | 18 / 0.0337 |
| 4 | 110 | 250 | 110 | 30 / 0.000601 | 1 / 0.000124 | 2 / 0.000427 | 1 / 3.4e-05 | 51 / 0.0327 |
| 8 | 210 | 490 | 210 | 54 / 0.00156 | 1 / 0.000188 | 2 / 0.000511 | 1 / 2.6e-05 | 253 / 0.0524 |
| 16 | 410 | 970 | 410 | 102 / 0.00608 | 1 / 0.00059 | 2 / 0.000492 | 1 / 4.5e-05 | 4329 / 0.473 |
| 32 | 810 | 1930 | 810 | 198 / 0.0634 | 1 / 0.00274 | 2 / 0.000704 | 1 / 4.3e-05 | timeout |
| 64 | 1610 | 3850 | 1610 | 390 / 0.484 | 1 / 0.0171 | 2 / 0.00108 | 1 / 9e-05 | skipped |

![sweep](sweep.png)
