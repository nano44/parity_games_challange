# R38: (CTX⁺) against n: best first-difference context counts found (L-RED box 9, 2026-10-18 01:48Z by date -u; produced on Opus 5.5)
Status: DATA, unrefereed. No kill and no super-polynomial family. Target: Lead box-9 item (1), the n-trend of (CTX⁺) (RESULTS R9 (c)).

## What is measured
- L-ALG experiments/alg/dtl_rootmono.py UNMODIFIED (l-alg 9b621aa2), RM_DV=0, line "distinct first-difference contexts per phase
  (file, contexts, transitions, |G'|)". It counts C_bv only, the best_vertices contexts that hold a first difference. C_T and C_Dom
  are NOT in this count.
- Each transition has exactly one first difference, so per phase C_bv ≤ transitions ≤ S − 1. A super-polynomial C_bv needs a
  super-polynomial S. The quantity with content is contexts per transition: a ratio bounded away from 0 as n grows would mean
  (CTX⁺) has no S-free bound.

## Best found per n (climbs with ROOTFIT=ctx = root/rootfit.py, which runs dtl_rootmono unmodified)
| n | file (sha1) | stable: contexts / transitions | Oink: contexts / transitions | pinned Oink |
|---|---|---|---|---|
| 20 | ctx6_n20.pg (2e1f2279b152) | 6 / 13 | 6 / 12 | 14 iterations, verified |
| 30 | ctx7_n30.pg (8e6bfc479008) | 7 / 15 | 5 / 12 | 14 iterations, verified |
| 40 | ctx13_n40.pg (box 7) | 13 / 24 | 13 / 24 | verified (C11) |
| 56 | ctx6_n56.pg (b7057c69db7d) | 6 / 12 | 5 / 10 | 15 iterations, verified |
- Seeds: spp_final_n20 (L-ALG), spp19_stable_n30 (L-RED), ctx13_n40 grown by 16 random vertices (best of 20) for n = 56.
  Climb lengths: n 20: 11,000 steps; n 30: 4,600; n 56: 300 (about 10 s per evaluation); an Oink-order climb from
  ctx13_n40 ran 100 steps (about 40 s per evaluation) without passing 13.
- Every best is about half its transitions: 0.46, 0.47, 0.54, 0.50. The absolute count does not grow with n, because the
  climbs' phases stay at 12-24 transitions.

## Structure (root/ctxtrace.py, the dtl_rootmono first-difference rule)
- ctx13_n40, phase 1, 24 transitions: the 13 contexts are all depth-0 pieces (|R| 26-40), with the first difference in the
  threshold loop. The full root context takes 8 of the 24.
- L-ALG's dtl_chainfam UP (S = n − 1): 1 context; every first difference is in the root threshold loop.
- fall3_n76 / fall4_n116: 1 context. 2-part CHAIN unions of the ctx instances (n 80): 12-13 contexts on the same 24-transition
  phase, because the phase ends at one part's dominion and the parts evolve in parallel.
- A finer count printed by the same tool, "distinct first-difference tattr inputs", is 12 / 12 on ctx6_n20 in both orders:
  every transition has a new tattr input.

## Reading (L-RED)
- On this data (CTX⁺) runs at about half a context per transition at every n tried. That neither bounds it independently of S
  nor shows growth.
- A union's highest changing piece always takes the first difference. A family whose context count grows with S therefore
  needs serialized pieces: the root call identical while a lower piece learns. This is the same lag problem as the depth
  construction (R37 addendum), and it is the open constructive route for both.
