DONE (all DATA). climb44.py / run44d.sh; band 280 ≤ N + M ≤ 320; 4 restarts × 500 steps per stream, alternating two seeds; score T3 / (N + M)
(T3 = iterations of N5'-xi from S3 on Γ3(G) before the first fallback, [E-LEV]; every proposal on fast37, every new global best re-run on my
text engine lev44.measure = own34 + n5xi44, which also evaluates box 209's must-0 counters). Successor 20's climb state was lost with its
container; successor 21 re-ran both streams from their seeds (the RNG is seeded by (SEED, restart, step), so stream 1's restart 0
repeats successor 20's T3 65 at N + M 285).
| stream (RNG seed) | seeds (T3 at N + M, ratio) | best (frozen) | N, M | T3 / (N + M) | evals |
| --- | --- | --- | --- | --- | --- |
| S1 (4431) | gen37(9) 61 at 290 (0.2103); MWR(10) 66 at 319 (0.2069) | inst/FROZEN44_S1_T65_NM285.json (sha1 bea3c331), from gen37(9), restart 0 | 93, 192 | 65 / 285 = 0.2281 | 1,911 |
| S2 (4432) | gen37(10) 67 at 319 (0.2100); MWR(9) 60 at 290 (0.2069) | inst/FROZEN44_S2_T63_NM281.json (sha1 75a16f72), from MWR(9), restart 1 | 93, 188 | 63 / 281 = 0.2242 | 1,907 |
- Engines: every one of the 24 global bests (out/climb44/BEST_*.json) has the SAME T3 on three engines: fast37 (C), my text engine
  (own34 + n5xi44; «agree True» on every BEST line) and a SECOND, other-lane engine, L-NEW's n5v (claude/l-new 311bbf81
  box208/level208.py --g3, run unchanged with python3 -I; sec44.sh, out/sec44.out): 24 of 24 equal. Box 209's must-0 counters: sum 0 on
  every best (my 47; no ALERT line in either log). Frozen bests and seeds: inst/SHA1SUMS.climb44.
- What the climb found: both bests keep the seed's movers (N = 93) and gain T3 by deleting or rewiring options (S1: M 197 → 192, T3
  61 → 65; S2: M 197 → 188, T3 60 → 63). The best ratio, 0.2281, is 10% above the seed families' slope (MWR(n): T3 = 6n + 6 at
  N + M = 29n + 29, so 6/29 = 0.2069 asymptotically; gen37(n): T3 = 6n + 7 at 29n + 29, box 37).
- Fit: NOT identified. One band (N + M ≈ 300) fixes no growth law; the bests are consistent with the linear T3 ≤ 0.23 (N + M) at this
  size and show nothing faster than linear, but a second band would be needed for an exponent. No alert (nothing faster than polynomial
  within a family; no must-0 counter fired).
