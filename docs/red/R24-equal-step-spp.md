# R24: equal-step searches-per-phase climbs, n = 20/30/40/60 x 3 seeds x both orders (L-RED box 5, 04:17Z by date -u; produced on Opus 5.5)
Queue item (1) of box 5 (Lead 23:20Z). Target: (SPP) S <= |G'| (S = searches in one phase, G' = unsolved game at the phase
start), (SPP-sharp) S <= max(1, |G'| - 1); growth of max S/|G'| with n at equal steps.
Tool: experiments/red/carry/spp.py (L-ALG dtl_phasestats read-only, l-alg b9b3b2b); climb dtl_search --fitness spp
(1000 x max S/|G'| over phases with >= 3 searches + max S + searches/1000), heartbeat every 100 steps. Seeds: L-ALG
spp_final_n{20,30,40,60} (l-alg b9b3b2b); n = 30 seed 3 from my spp19_stable_n30. Seed values 5000 + 10n + s.
BUDGET: planned 1500 steps; the 1500-step runs were too slow on 4 shared cores, so the common budget was cut to 500 steps
at 02:58Z. n = 60 (all but stable s3) ran 1500 steps; oink n40 s1/s2 were stopped at step 600, stable n60 s3 at 1100,
oink n40 s3 at 500; the rest ran 500. fit@k = best climb fitness at step k (heartbeat); the last four columns measure
the run's saved best game with spp.py in the run's own order. "sharp" = max over phases with |G'| >= 2 of S - |G'| + 1.

| order | n | seed | done | fit@0 | fit@500 | fit@1000 | fit@end | best S | |G'| | S/|G'| | sharp |
|---|---|---|---|---|---|---|---|---|---|---|---|
| oink | 20 | 1 | yes | 969.022 |  |  | 969.022 | 19 | 20 | 0.950 | 0 |
| oink | 20 | 2 | yes | 969.022 |  |  | 969.022 | 19 | 20 | 0.950 | 0 |
| oink | 20 | 3 | yes | 969.022 |  |  | 969.022 | 19 | 20 | 0.950 | 0 |
| oink | 30 | 1 | yes | 652.355 |  |  | 652.355 | 19 | 30 | 0.633 | -10 |
| oink | 30 | 2 | yes | 652.355 |  |  | 652.355 | 19 | 30 | 0.633 | -10 |
| oink | 30 | 3 | yes | 652.356 |  |  | 652.356 | 19 | 30 | 0.633 | -2 |
| oink | 40 | 1 | step 600 | 494.026 | 532.846 |  |  | 20 | 39 | 0.513 | -18 |
| oink | 40 | 2 | step 600 | 494.026 | 573.658 |  |  | 22 | 38 | 0.579 | -15 |
| oink | 40 | 3 | step 500 | 494.026 | 519.024 |  |  | 19 | 38 | 0.500 | -18 |
| oink | 60 | 1 | yes | 247.349 | 247.349 | 283.849 | 283.849 | 13 | 48 | 0.271 | -34 |
| oink | 60 | 2 | yes | 247.349 | 247.349 | 267.917 | 278.322 | 13 | 49 | 0.265 | -35 |
| oink | 60 | 3 | yes | 247.349 | 247.349 | 265.017 | 315.018 | 15 | 50 | 0.300 | -34 |
| stable | 20 | 1 | yes | 561.014 |  |  | 918.021 | 18 | 20 | 0.900 | 0 |
| stable | 20 | 2 | yes | 561.014 |  |  | 765.018 | 15 | 20 | 0.750 | 0 |
| stable | 20 | 3 | yes | 561.014 |  |  | 867.02 | 17 | 20 | 0.850 | 0 |
| stable | 30 | 1 | yes | 652.355 |  |  | 652.355 | 19 | 30 | 0.633 | -10 |
| stable | 30 | 2 | yes | 652.355 |  |  | 652.355 | 19 | 30 | 0.633 | -10 |
| stable | 30 | 3 | yes | 652.356 |  |  | 652.356 | 19 | 30 | 0.633 | -2 |
| stable | 40 | 1 | yes | 442.024 |  |  | 479.562 | 18 | 39 | 0.462 | -20 |
| stable | 40 | 2 | yes | 442.024 |  |  | 491.708 | 18 | 38 | 0.474 | -19 |
| stable | 40 | 3 | yes | 442.024 |  |  | 491.707 | 18 | 38 | 0.474 | -19 |
| stable | 60 | 1 | yes | 247.349 | 247.349 | 273.016 | 283.849 | 13 | 48 | 0.271 | -34 |
| stable | 60 | 2 | yes | 247.349 | 247.349 | 267.917 | 278.322 | 13 | 49 | 0.265 | -35 |
| stable | 60 | 3 | step 1100 | 247.349 | 247.349 | 265.017 |  | 15 | 60 | 0.250 | -44 |

## Reading
- No phase with S > |G'| and no SPP-sharp violation (sharp <= 0 everywhere; 0 = tight, at n = 20 only).
- Best S/|G'| by n (both orders): 0.95 (n = 20, unchanged from L-ALG's seed), 0.633 (n = 30), 0.579 (n = 40), 0.30 (n = 60).
  At equal (and larger) step budgets the max ratio FALLS with n; max S is 19, 19, 22, 15. No growth signal.
- New best at n = 40: experiments/red/carry/instances/spp22_oink_n40.pg (sha1 79b25b73): 22 searches in one phase at |G'| = 38
  in BOTH orders (L-ALG's spp_final_n40: 19). Pinned Oink: 3 dominions, 41 tangles, 28 iterations, solution verified.
- n = 60 climbs barely move in 1500 steps (eval ~2-4 s); the n = 60 numbers are the least converged.
