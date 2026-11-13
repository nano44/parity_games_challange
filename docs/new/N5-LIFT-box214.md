# Box 214 (D18) Step A: prior tower-lift record and block alignment of H5 / H6 / HIT7 — no repeating block, no lift rule (DATA; a negative result for the «block lifting» construction route; no kill, no bound; G-N5-TIME stays OPEN)
L-NEW successor 75 (session_01V5yGRWimvjsi2nZhjaevtK), D1 / D14 / D18 / D21. Written 2026-11-13 04:27Z (date -u). Lead 04:25Z: «FIRST a short
record of what these attempts established (by quote and commit) … THEN your block-alignment analysis ONLY on what is not already covered.»
Labels: READING (what other lanes' files say; quotes checked by git grep at the heads named), DATA. Not M3, not M4.

## 1. The decisive question (Lead 04:25Z, restated)
A family G_k (one genome per k, N + M polynomial in k) on which one mover switches 2^k − 1 times before N5's first fallback on Γ3(G_k)
would make N5 exponential (RESULTS R124 EXACT-L: L(G) + 3 iterations on IDEAL-ACYC): a gauntlet kill. Known instances: DBL4 (k 4, d 20,
N 40), H5 (5, 20, 40), H6 (6, 24, 48), HIT7 (7, 28, 56); box 213 kcount213: one mover switches 15, 31, 63, 127 times on them.

## 2. Prior attempts (READING; heads read: l-lower 3e83685a, l-si 047f0725, l-red 50fe432a, l-new 3bcd7b62)
- L-LOWER, TOP-ADD then climb (how H5, H6, HIT7 were made): inert top levels added (l3/lift.py, l9/lift.py), then a fresh annealed climb or
  SAT search per level. H5 → H6: docs/lower/L4-tower.md l. 172 «the diff gives no rule» (Ξ-targets changed 89 of 96, longest common
  subsequence 17 of 96). H6 → HIT7: not measured as an operation (L8). No family; stopped at k = 7.
- L-LOWER, uniform level templates (docs/lower/L5-rule.md l. 79, d 6-12): «never two consecutive doubling levels»; CANDIDATE-DEAD; reading:
  a working rule must be non-uniform in the level. CONJECTURE L5-TYPE (O(h) added movers) open, no construction.
- L-LOWER, level 8 (k = 8) from HIT7_lift_d32 (L9-L12, L18): the stretched target core8 (rows 0..510); docs/lower/L12-slack.md l. 129 «Every
  base dies at t ≤ 7», l. 101 «Depth did not buy room»; in progress as BOX L18: docs/lower/L18-horizon.md l. 11 «NOT the level-8 tower»
  (P = 13 of the 510 rows realised; P = 14 UNSAT in the neighbourhoods tried, per L-LOWER's notes).
- L-SI pair84 «MIRROR» hub towers (h 2-8) and L-NEW box 197 (two85 family, h 2-8): IDEAL-CYC hub counters, not 𝓛^R_d doubling towers; T
  linear, maxalt ≤ 5 (docs/new/N5-CORE-box197.md l. 169 «maxalt does not grow past 5 on this family up to height 8»). L-RED's HP6x / HP7x
  extrapolation: docs/red/R226-core197.md l. 81 «may not be faithful towers», superseded by L-SI's faithful HP6b-HP8b (maxalt 4).
- So no lift or generator has kept F(l) doubling beyond k = 7, and the only ladder «lifts» are inert padding plus a new search per level.

## 3. Step A: block alignment (DATA; experiments/new/box214/align214.py, mirror214.py; outputs out/, pinned in out/SHA1SUMS)
Not covered by §2: a level-by-level comparison of the parameters of H5, H6, HIT7 up to a shift of the level axis. Per level l (movers 2l,
2l + 1, two options each): the W-target pattern (which mover of level l − 1, or c_W), the Ξ-target pattern (level offset lev(xt) − l and side,
or the exit X), the β priority and the start bit.
- W-target patterns: equal at every level and shift (the ladder 𝓛^R_d itself; no information).
- Ξ-target patterns: **0 matching levels at every shift**, H5 → H6 (shifts 0-4), H6 → HIT7 (0-4), H5 → HIT7 (0-8). No level of one tower
  reappears, even with level-relative offsets, in the next; so no block of 4 ladder levels repeats, and «HIT7 = H6 + one block» is false at
  the level of Ξ-targets.
- The visible «low levels point up, high levels point down» shape is not structure: mean |lev(xt) − (d − 1 − l)| equals a shuffled baseline
  (HIT7 8.32 vs 8.78 ± 0.50; H6 8.47 vs 7.89 ± 0.49; H5 7.18 vs 6.47 ± 0.45; DBL4, RECF4 likewise) and corr(l, lev(xt)) ∈ [−0.10, 0.17].
- Conclusion (DATA): the towers are unrelated search results at the level of their Ξ-targets; the «block lifting» route of my 04:23Z
  proposal has no starting point. Step B (extrapolation to k = 8-10) is NOT run: there is nothing to extrapolate. What would still be new:
  an invariant-level description (what the doubling needs from the Ξ-structure, e.g. per-level Ξ-reachability or priority-rank patterns),
  not a parameter copy; L-LOWER's L18 is the active construction attempt at k = 8.
