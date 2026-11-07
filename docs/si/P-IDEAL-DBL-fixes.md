# P-IDEAL-DBL fixes (the packet docs/si/P-IDEAL-DBL.md stays frozen at f5263d5a, sha1 3573e93b…; every repair is here)

## Entry 1 (fix round 1; L-SI successor 42; Lead 09:20Z: REFEREE 26 d7885be4 DB-Q1, DB-2, DB-3, DB-L1, DB-L2; REFEREE-2 30 7891ba32
W-1, W-2 (a)-(d), W-3, N-1..N-3; Lead rulings 1-5). Strings copied by script: experiments/si/box79/mkfix1.py (this file) and
mkL2.py (line L-2); referee reports byte-copied as experiments/si/box79/ref_d7885be4.md, ref2_7891ba32.md (pinned).

### F-1 (W-1 = DB-Q1; Lead ruling 1): the PATH-RISE premise in §0 is quoted from the landed R113 text
- Old (packet §0): (PATH-RISE) «Then the number of steps at which cv(z) rises is at most P(z) − 1.» [IDEAL-ACYC, any degree, any width]
- New: R113 (trunk docs/RESULTS.md at 97d17f63, «### R113 [refereed-only]», stated «on acyclic Ξ-graphs»): «(PATH-RISE) at any degree, the current value cv(z) of every mover z rises at most P(z) − 1 times in a run», with
  R113's P(z) «the number of maximal Ξ-paths from z». Same content; TOWER-NEED (§4) and FUEL-NEED (§5) use exactly this. No proof changes.

### F-2 (DB-2 + W-2 (d) + N-3; Lead ruling 3): DEAD-REENTRY, reading and levels
- §6 DEAD-REENTRY is to be read as: «the strict Ξ-descendants of the fuel targets U_l lie at levels > l» (static Ξ-graph; U_l as in §0:
  the Ξ-targets of upward options of movers of level ≤ l; strict Ξ-descendants of y: movers reachable from y along Ξ-targets of any
  options, y excluded). The packet's «the movers on the chains of the fuel targets U_l» named no l and no reading (DB-2).
- MEASURED by experiments/si/box79/reentry_levels.py → reentry_levels.out (every l in 0, …, d − 2; reading A = as worded, every y ∈ U_l;
  reading B = only the y ∈ U_l of level > l):
  - REC_d10_tower_mu30.json (sha1 cc94dc9c…, d 10): false for l ∈ {1, 2, 3, 4, 5, 6, 7, 8} (reading A), l ∈ {1, 2, 3, 4, 5, 6, 7, 8} (reading B); true for l = 0.
  - KILL_M2D_d6_mu13.json (sha1 5301c716…, d 6): false for l ∈ {1, 2, 3, 4} (reading A), l ∈ {1, 2, 3} (reading B); true for l = 0.
- The line uses reading A (DB-L2's wording) with these sets and REFEREE-2's witnesses 1 → 11 → 3 (REC_d10_tower_mu30: (1, 0) → 11 of
  level 5, (11, 0) → 3 of level 1) and 2 → 5 → 3 (KILL_M2D_d6_mu13: (2, 1) of level 1 → 5 of level 2, (5, 0) → 3 of level 1); each
  witnesses every l ≥ 1 of its set (the first mover has level ≤ 1 ≤ l, the last has level 1 ≤ l).
- The measured sets differ from both referees' statements: REFEREE 26 «fails for l = 1, …, 4» (tower) / «l = 1» (KILL_M2D) and REFEREE-2
  N-3 «killed at l = 1». Both named only the witness through 11 resp. 5, valid for l ≥ 1. For the tower, 11 of level 5 is in U_l for every l
  (it is the target of a level-0 mover), so with reading A the witness 1 → 11 → 3 works up to l = d − 2 = 8. The «l ≤ 4» bound holds only if
  one also asks lev(11) > l, and reading B then finds other witnesses for l = 5, …, 8 (reentry_levels.out). The DEAD verdicts stand.

### F-3 (DB-3, taken; Lead ruling 4): DBL-EQ proof step (iv)
- Add to (iv): at a doubling level, Φ(s_0) = 2 while Φ(s_(t−1)) = 0 at every l-b-step t (DBL-EQ (a)); so step 1 is not an l-b-step,
  and the l-windows are [1, t_1 − 1], [t_1, t_2 − 1], …, [t_f, T] with t_1 < … < t_f the l-b-steps: exactly F(l − 1) + 1 windows.

### F-4 (DB-L1 + W-3; Lead ruling 2): DATA clause of the line, and why PASS-FREEZE keeps its count
- The line's DATA clause is DB-L1's New text. Every number in it is asserted equal to dblcheck.out / dblcheck_neg2.out by mkL2.py.
  W-3's no-DATA entries that DB-L1 lacks are added in place of «MP-LIN no separate DATA;»: the sufficient condition of PASS-FREEZE and
  DEAD-REENTRY (static; reentry_levels.py) have no separate DATA, and the other three DEAD instances are re-run by dead79.py.
- PASS-FREEZE keeps DB-L1's count (23,317 (run, level) of CORPUS, none in LOWER): it counts the lemma's conclusion F(l + 1) = F(l) on runs
  where the pair above never moves and starts split (counter PF). W-3 asks «no separate DATA» only for the SUFFICIENT CONDITION (both
  options of a member with target X, …), which no counter tests; the line now says exactly that. W-3's own text also carries «23,317 / 0».

### F-5 (N-1, N-2): line premises and wording
- N-1 (and REFEREE 26's optional note): F0 is dropped from the line's premise list (only §5's FUEL (i), not in the line, uses it).
- N-2: the line's U_l now reads «whose Ξ-target has a higher level than that mover» (packet §0 «Upward option»).

### Line L-2 = L-1 with these replacements (mkL2.py; each old string once in L-1, each new once in L-2)
- W-2 (a)
    OLD «(L-RED's dense_d5_l3_H10, start 1100110110: 10 moves against 4)»
    NEW «(experiments/si/box76/inst/dense_d5_l3_H10.json, a byte copy of L-RED's, 𝓛^R_5, start 1100110110: mover 6 of level 3, a Ξ-target, moves 10 times, every mover of levels 0-2 and every strict Ξ-descendant of 6 at most 4 times)»
- W-2 (b)
    OLD «(L-LOWER's REC_d10_tower_mu30: F(0..3) = 2, 6, 14, 30)»
    NEW «(experiments/si/box76/inst/lower/REC_d10_tower_mu30.json, a byte copy of L-LOWER's, 𝓛^R_10, its stored start 00111111010010111010: F(0..3) = 2, 6, 14, 30)»
- W-2 (c)
    OLD «(passfreeze77_d5: F = 2, 2, 2, 6, 6)»
    NEW «(experiments/si/box76/inst/passfreeze77_d5.json, 𝓛^R_5, its stored start 1101111101: F = 2, 2, 2, 6, 6, the top pair never moving)»
- DB-L2 + W-2 (d) + N-3
    OLD ««the chains of the fuel targets U_l stay above level l» (REC_d10_tower_mu30: 11 → 3; KILL_M2D_d6_mu13: 5 → 3)»
    NEW ««the strict Ξ-descendants of the fuel targets U_l lie at levels > l» (static Ξ-graph; measured for every l in 0, …, d − 2 by experiments/si/box79/reentry_levels.py: false for l = 1, …, 8 on experiments/si/box76/inst/lower/REC_d10_tower_mu30.json, a byte copy of L-LOWER's, 𝓛^R_10, witness 1 → 11 → 3 (mover 11 of level 5 is the Ξ-target of mover 1's option 0, and 3 of level 1 is a Ξ-target of an option of 11), and for l = 1, …, 4 on experiments/si/box76/inst/lower/KILL_M2D_d6_mu13.json, a byte copy of L-LOWER's, 𝓛^R_6, witness 2 → 5 → 3 (mover 5 of level 2 is the Ξ-target of an option of mover 2 of level 1, and 3 of level 1 is a Ξ-target of an option of 5); true for l = 0 on both)»
- DB-L1 + W-3
    OLD «(DATA: each statement 0 violations on its own unit over the 63,223 runs of the frozen P-IDEAL-MOVES corpus and the 9 L-LOWER genomes, with controls; FUEL-NEED and FUEL (i), which use L-LOWER's unrefereed FEEDBACK (b), are not stated; no statement bounds T polynomially)»
    NEW «(DATA, experiments/si/box79/dblcheck.py, CORPUS = the 63,223 runs (140,395 steps) of the 208 𝓛^R_d genomes of the frozen P-IDEAL-MOVES corpus (l-new 9995f5a2; every start for N ≤ 10, the stored start otherwise), LOWER = the 9 runs of L-LOWER 3's kill genomes from their stored starts, counts given as CORPUS / LOWER, every genome of degree 2 and width 2 (so HIT and ALT-MIN, stated at any degree, are tested only there): WINDOW-ONCE 0 violations on 577,908 / 1,736 (run, level, window, member); DBL-EQ (a) 0 on 225,647 / 72 (run, level ≥ 1), both directions, with 4,534 / 12 doubling (run, level); (b) 0 on 11,052 / 176 (run, doubling level, window, member); (c) 0 on every doubling (run, level); PASS-FREEZE 0 on the 23,317 (run, level) of CORPUS whose pair above never moves and starts split (none in LOWER); HIT 0 on 1,298,948 / 5,216 (run, mover, step); FUEL-EXACT 0 on 288,870 / 81 (run, level); ALT-MIN 0 on 577,740 / 162 (run, mover), (a) and (d) counted per (run, mover, k); TOWER-NEED's bounds on P and R 0 on 9,068 / 24 (run, doubling level, member), its moves clause through DBL-EQ (b); controls: ALT-MIN's bounds (b) and (c) minus 1 fail on 112,372 / 43 and 7,085 / 13 (run, mover), and with the key-least option taken regardless of availability HIT fails on 238,546 CORPUS (run, mover, step); MP-LIN, the sufficient condition of PASS-FREEZE and DEAD-REENTRY (static Ξ-graph; its level sets measured by experiments/si/box79/reentry_levels.py): no separate DATA; the other three DEAD instances re-run by experiments/si/box79/dead79.py; FUEL-NEED and FUEL (i), which use L-LOWER's unrefereed FEEDBACK (b), are not stated; no statement bounds T polynomially)»
- N-1
    OLD «R113's ALIGN, F0 and PATH-RISE»
    NEW «R113's ALIGN and PATH-RISE»
- N-2
    OLD «whose Ξ-target has a higher level»
    NEW «whose Ξ-target has a higher level than that mover»
- docs/si/P-IDEAL-DBL-line-L2.txt: sha1 1b3dc82544adfaf2cdea0deffbcbd052db9cd371, 5,810 B, 1 line, 97 «(» = 97 «)», 0 «|».
- Not changed: every statement of the packet (all SIGN at both referees); L-1 and the packet stay as frozen.
