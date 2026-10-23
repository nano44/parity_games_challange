## switchallexp: mean total pivots (primal + dual), R2 seeds 1-5
| setting | N 8 (n 119) | N 12 (n 175) | N 16 (n 231) | N 20 (n 287) | N 24 (n 343) | N 28 (n 399) | power exp. | exp. base | better |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| first | 363 | 789 | 1352 | 1973 | 2922 | 3540 | n^1.90 (SSR 0.006) | 1.119^N (SSR 0.153) | power |
| last | 367 | 904 | 1454 | 2340 | 3328 | 3991 | n^1.99 (SSR 0.019) | 1.124^N (SSR 0.213) | power |
| rand | 434 | 830 | 1456 | 2257 | 2873 | 3867 | n^1.82 (SSR 0.006) | 1.114^N (SSR 0.115) | power |
| relabel | 335 | 864 | 1202 | 2015 | 2413 | 3749 | n^1.90 (SSR 0.045) | 1.118^N (SSR 0.186) | power |

## switchbestexp: mean total pivots (primal + dual), R2 seeds 1-5
| setting | N 10 (n 260) | N 14 (n 360) | N 18 (n 460) | N 22 (n 560) | N 26 (n 660) | N 30 (n 760) | power exp. | exp. base | better |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| first | 1522 | 3028 | 5180 | 6963 | 8571 | 13016 | n^1.93 (SSR 0.022) | 1.106^N (SSR 0.118) | power |
| last | 1475 | 2680 | 4400 | 6123 | 9219 | 11298 | n^1.92 (SSR 0.005) | 1.107^N (SSR 0.069) | power |
| rand | 1412 | 2590 | 5982 | 6687 | 11443 | 12948 | n^2.14 (SSR 0.081) | 1.118^N (SSR 0.223) | power |
| relabel | 1471 | 2721 | 3709 | 6488 | 10779 | 13044 | n^2.09 (SSR 0.059) | 1.118^N (SSR 0.053) | exp |

## rand1k (first 1,000 rand10k games), R2 seeds 1-5: mean total pivots
- first: 5000 runs, mean 16.67, max 131
- last: 5000 runs, mean 17.07, max 126
- rand: 5000 runs, mean 16.29, max 138
- relabel: 5000 runs, mean 16.99, max 128

non-OK rows: 0
