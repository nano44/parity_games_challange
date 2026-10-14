Family switchallexp; generator `python3 pgsolver_port.py switchallexp {N}`; timeout 20s per run; cell = iterations / wall seconds (iterations as reported by the solver; '-' if it reports none).

| N | n | m | d | oink-psi-raw (major iterations) | oink-ssi-raw (major iterations) | oink-zlk-raw (iterations) | oink-tl-raw (iterations) | py-zlk (iterations) |
|---|---|---|---|---|---|---|---|---|
| 1 | 21 | 41 | 21 | 6 / 0.000691 | 1 / 5e-05 | 2 / 0.000611 | 1 / 3.5e-05 | 7 / 0.0314 |
| 2 | 35 | 75 | 35 | 8 / 0.000515 | 1 / 6.2e-05 | 2 / 0.000777 | 1 / 2.6e-05 | 7 / 0.0312 |
| 4 | 63 | 143 | 63 | 12 / 0.000547 | 1 / 6.6e-05 | 2 / 0.00298 | 1 / 3.3e-05 | 7 / 0.0364 |
| 8 | 119 | 279 | 119 | 20 / 0.00114 | 1 / 0.000123 | 2 / 0.000634 | 1 / 0.000108 | 7 / 0.0325 |
| 16 | 231 | 551 | 231 | 36 / 0.00168 | 1 / 0.000195 | 2 / 0.000513 | 1 / 2.9e-05 | 7 / 0.0392 |
| 32 | 455 | 1095 | 455 | 68 / 0.00566 | 1 / 0.000563 | 2 / 0.000509 | 1 / 3.9e-05 | 7 / 0.0415 |
| 64 | 903 | 2183 | 903 | 132 / 0.0285 | 1 / 0.00199 | 2 / 0.000514 | 1 / 5.6e-05 | 7 / 0.0562 |
