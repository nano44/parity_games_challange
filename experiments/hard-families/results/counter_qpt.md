Family counter_qpt; generator `../../tools/oink/build/counter_qpt {N}`; timeout 20s per run; cell = iterations / wall seconds (iterations as reported by the solver; '-' if it reports none).

| N | n | m | d | oink-qpt-raw (lifts) | oink-sspm-raw (lifts) | oink-zlk-raw (iterations) | oink-tl-raw (iterations) | py-zlk (iterations) |
|---|---|---|---|---|---|---|---|---|
| 2 | 4 | 5 | 4 | 21 / 5e-05 | 4 / 5e-05 | 2 / 0.000654 | 1 / 2e-05 | 2 / 0.0319 |
| 4 | 8 | 11 | 8 | 113 / 6.5e-05 | 16 / 6.3e-05 | 2 / 0.000522 | 1 / 3e-05 | 2 / 0.0342 |
| 8 | 16 | 23 | 16 | 4187 / 0.00094 | 64 / 7.2e-05 | 2 / 0.000606 | 1 / 3.2e-05 | 2 / 0.0303 |
| 16 | 32 | 47 | 32 | 975553 / 0.238 | 256 / 0.00012 | 2 / 0.000612 | 1 / 1.9e-05 | 2 / 0.0297 |
| 32 | 64 | 95 | 64 | timeout | 1024 / 0.00062 | 2 / 0.00115 | 1 / 3e-05 | 2 / 0.0556 |
| 64 | 128 | 191 | 128 | skipped | 4096 / 0.00234 | 2 / 0.000518 | 1 / 3.2e-05 | 2 / 0.0385 |
| 128 | 256 | 383 | 256 | skipped | 16384 / 0.00613 | 2 / 0.000515 | 1 / 4.3e-05 | 2 / 0.0474 |
| 256 | 512 | 767 | 512 | skipped | 65536 / 0.0328 | 2 / 0.000886 | 1 / 3.7e-05 | 2 / 0.047 |
| 512 | 1024 | 1535 | 1024 | skipped | 262144 / 0.128 | 2 / 0.000634 | 1 / 8.6e-05 | 2 / 0.0499 |
