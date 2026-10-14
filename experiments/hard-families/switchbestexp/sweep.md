Family switchbestexp; generator `python3 pgsolver_port.py switchbestexp {N}`; timeout 20s per run; cell = iterations / wall seconds (iterations as reported by the solver; '-' if it reports none).

| N | n | m | d | oink-psi-raw (major iterations) | oink-ssi-raw (major iterations) | oink-zlk-raw (iterations) | oink-tl-raw (iterations) | py-zlk (iterations) |
|---|---|---|---|---|---|---|---|---|
| 1 | 35 | 70 | 34 | 12 / 0.000628 | 1 / 4.8e-05 | 2 / 0.000494 | 1 / 2.8e-05 | 7 / 0.0321 |
| 2 | 60 | 130 | 60 | 18 / 0.000443 | 1 / 6.8e-05 | 2 / 0.000803 | 1 / 2.2e-05 | 18 / 0.0337 |
| 4 | 110 | 250 | 110 | 30 / 0.000601 | 1 / 0.000124 | 2 / 0.000427 | 1 / 3.4e-05 | 51 / 0.0327 |
| 8 | 210 | 490 | 210 | 54 / 0.00156 | 1 / 0.000188 | 2 / 0.000511 | 1 / 2.6e-05 | 253 / 0.0524 |
| 16 | 410 | 970 | 410 | 102 / 0.00608 | 1 / 0.00059 | 2 / 0.000492 | 1 / 4.5e-05 | 4329 / 0.473 |
| 32 | 810 | 1930 | 810 | 198 / 0.0634 | 1 / 0.00274 | 2 / 0.000704 | 1 / 4.3e-05 | timeout |
| 64 | 1610 | 3850 | 1610 | 390 / 0.484 | 1 / 0.0171 | 2 / 0.00108 | 1 / 9e-05 | skipped |
