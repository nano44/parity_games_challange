Family switchbestexp; generator `python3 pgsolver_port.py switchbestexp {N}`; timeout 20s per run; cell = iterations / wall seconds (iterations as reported by the solver; '-' if it reports none).

| N | n | m | d | oink-psi-raw (major iterations) | oink-ssi-raw (major iterations) | oink-zlk-raw (iterations) | oink-tl-raw (iterations) | py-zlk (iterations) |
|---|---|---|---|---|---|---|---|---|
| 1 | 35 | 70 | 34 | 12 / 0.00058 | 1 / 5.5e-05 | 2 / 0.000384 | 1 / 2e-05 | 7 / 0.0319 |
| 2 | 60 | 130 | 60 | 18 / 0.000658 | 1 / 6.1e-05 | 2 / 0.0005 | 1 / 2.3e-05 | 18 / 0.0342 |
| 4 | 110 | 250 | 110 | 30 / 0.000969 | 1 / 0.000162 | 2 / 0.000637 | 1 / 2.4e-05 | 51 / 0.0346 |
| 8 | 210 | 490 | 210 | 54 / 0.00149 | 1 / 0.000196 | 2 / 0.000514 | 1 / 2.7e-05 | 253 / 0.0482 |
| 16 | 410 | 970 | 410 | 102 / 0.00753 | 1 / 0.000601 | 2 / 0.0006 | 1 / 5.6e-05 | 4329 / 0.883 |
| 32 | 810 | 1930 | 810 | 198 / 0.0735 | 1 / 0.00302 | 2 / 0.00108 | 1 / 4.6e-05 | timeout |
| 64 | 1610 | 3850 | 1610 | 390 / 0.392 | 1 / 0.0113 | 2 / 0.000598 | 1 / 7e-05 | skipped |
