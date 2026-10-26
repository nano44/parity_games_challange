# N5 iterations on 𝒞^1O against n (DATA, not proof; L-SI succ. 10, 2026-10-26 00:54Z by date -u; Lead 00:51Z item (2))
Purpose: show how loose P-N5-1O's bound (Theorem 1O-POLY: O(m·Δ·d_o·n¹³) ⊆ O(n¹⁸)) is in observed runs. Nothing here is a growth law.
Script: iters.py. It runs experiments/new/n5.py run() (SPEC, read-only) from SPEC S3's start plus K random start pairs, and fits a
least-squares line to log(ITER) against log n.
| corpus | runs | n range | max ITER (at n) | max ITER / n | fitted exponent, max ITER per n | fitted exponent, all runs |
| --- | --- | --- | --- | --- | --- | --- |
| lib41 (experiments/new/box41/lib41.txt, 𝒞^1O files), S3 + 3 random starts (seed 2601); log lib41_k3.txt | 1,012 | ≤ 64 | 115 (n 48) | 2.75 (66 at n 24) | 1.16 | 1.25 |
| random o-cyclic 𝒞^1O (REFEREE-2's rand_game), n 6-40, S3 + 2 random starts (seed 2602); log rand_6_40.txt | 1,800 | 6-40 | 6 | 0.43 | 0.48 | 0.45 |
| random o-cyclic 𝒞^1O, n 41-100, S3 + 1 random start (seed 2603); log rand_41_100.txt | 300 | 41-100 | 9 (n 98) | 0.14 | 0.49 | 0.39 |
Reading (not a claim):
- lib41 contains the fleet's adversarial climbs (L-NEW, L-RED, L-SI, referees), aimed at long phases, fallbacks, crossings and wakes. On
  it, the maximum iteration count grows about linearly in n (exponent ≈ 1.2, at most 2.75·n).
- Random 𝒞^1O games stay below n/2, with a sublinear fit.
- Against the proved O(n¹⁸) the gap is ~16 orders in the exponent. The proof bound is a worst-case product of independent counts (phases ×
  fallbacks × crossings × stretches × per-run bounds); the data never come close to any of the factors (see R47-R50 data).
- Caveats: Python engine, n ≤ 100. lib41's largest games are n 64. Climbs maximise other targets, not ITER itself; no ITER-climb was run.
