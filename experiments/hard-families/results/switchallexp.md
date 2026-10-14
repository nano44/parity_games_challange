Family switchallexp; generator `python3 pgsolver_port.py switchallexp {N}`; timeout 20s per run; cell = iterations / wall seconds (iterations as reported by the solver; '-' if it reports none).

| N | n | m | d | oink-psi-raw (major iterations) | oink-ssi-raw (major iterations) | oink-zlk-raw (iterations) | oink-tl-raw (iterations) | py-zlk (iterations) |
|---|---|---|---|---|---|---|---|---|
| 1 | 21 | 41 | 21 | 6 / 0.00056 | 1 / 6.7e-05 | 2 / 0.000534 | 1 / 2.6e-05 | 7 / 0.0345 |
| 2 | 35 | 75 | 35 | 8 / 0.000735 | 1 / 5.9e-05 | 2 / 0.000462 | 1 / 2.6e-05 | 7 / 0.0375 |
| 4 | 63 | 143 | 63 | 12 / 0.000492 | 1 / 7.3e-05 | 2 / 0.000524 | 1 / 2.4e-05 | 7 / 0.0315 |
| 8 | 119 | 279 | 119 | 20 / 0.00081 | 1 / 0.000106 | 2 / 0.000451 | 1 / 2.6e-05 | 7 / 0.032 |
| 16 | 231 | 551 | 231 | 36 / 0.00134 | 1 / 0.000236 | 2 / 0.000398 | 1 / 2.7e-05 | 7 / 0.0334 |
| 32 | 455 | 1095 | 455 | 68 / 0.00431 | 1 / 0.000723 | 2 / 0.00046 | 1 / 4.5e-05 | 7 / 0.0359 |
| 64 | 903 | 2183 | 903 | 132 / 0.0243 | 1 / 0.00221 | 2 / 0.000566 | 1 / 6.4e-05 | 7 / 0.0722 |
