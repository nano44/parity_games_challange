# Box 98: how CHAIN3's bound depends on U(G), and a stress test along U (design side, D18)
L-SI successor 50 (Opus 5.5), D18 / D14 / D1; Lead 2026-11-11 22:12Z (BOX 98 (1)-(3)). Labels: PROVED (L-SI lane, unrefereed) /
CONJECTURE / DATA (unit, set, scope, counter) / DEAD / READING. Not a TARGET.md claim; not M3 or M4; not a gauntlet step; G-N5-TIME stays
OPEN. L-RED 64 attacks what is claimed here.

## 0. Answer
- (1) READING: CHAIN3's bound is T3 + 3 ≤ (1 + n3·((2M + 3)·F′_(U(G))(M) − 1))·(L3 + 1) + 3 with F′_B of degree 5·2^B − 3 in M (RESULTS
  R121). So the dependence on U is n^{O(2^U)}: DOUBLY exponential in U inside the exponent. It is neither n^{O(U)} nor 2^{O(U)}·poly(n);
  it is polynomial only for U = O(1), and not even quasi-polynomial for U ≈ log log n. [E-LEV] is used in exactly one place, UP-JUMP3
  (an ascent of seq_t(v) needs an upward Ξ-edge), hence UP-B3 (ascents ≤ U(G)). It does not fix anything else; without it the ascent
  count is not bounded by U (R121: NOUP fails under the reversed e-order; L-RED NOUPC_1-3 have U = 0 and 2-4 ascents).
- (2) DATA: U is NOT the axis that binds. On every frozen family U(G) is already linear in N (U ≈ N/3, up to 99 on MW32_2) while T3 stays
  linear; the quantity the proof uses, the number of ASCENTS per e-sequence, stays at most 5 on 19 frozen instances and at most 2 on the
  seven climb bests; a high ascent count does not make runs long (WC16_2: 16 ascents, T3 = 4, Dmax 3). A hill-climb maximising T3 at seven
  shapes (N 4-25, U up to 16) finds T3 ≤ N + 4 (two engines). No family with super-polynomial, or even super-linear, T3 was found.
- (3) CONJECTURE U-FREE (stated with its strongest DATA, §4): T3 ≤ N + M + 4 for every genome, independent of U(G) (and so polynomial);
  the weaker form «T3 ≤ poly(N + M), independent of U» is the mover-phase part of what G-N5-TIME asks, for N5′-xi. No obstruction lemma is
  claimed; §3 names the one mechanism that could break it and why Howard's greed blocks it on the families measured.

## 1. (1) The reading, clause by clause (P-N5-CHAIN at claude/l-new 93531b03; fixes 1-4 and line L-5 at claude/l-new)
- §8 Theorem CHAIN3: «T3 + 3 ≤ (1 + n3·((2M + 3)·F′_(U(G))(M) − 1))·(L3 + 1) + 3», n3 = N + 7M + 10, L3 = (M + 1)(2M + 1)(N + 1) +
  N(n3 − 1). Its proof: T-QUIET3 gives T3 ≤ (1 + Σ_v (D^tot_E(v) − 1))(L3 + 1); UP-B3 with HUB-ASC-G3 gives D^tot_E(v) ≤ (2M + 3)·
  F′_(U(G))(M). So U enters ONLY through B := U(G) in F′_B, as an upper bound on the ascents of every seq_t(v).
- F′_B: F′_0(M) = 1 + M(M + 1)/2, F′_B(M) = (M² + 3M + 1)(1 + M·F′_(B−1)(M)²) (P-N5-CHAIN l. 76-77; RESULTS R121), «a polynomial of
  degree 5·2^B − 3 for fixed B» (RESULTS R121). The squaring in the recursion is what doubles the degree per ascent.
- §7 UP-JUMP3 / UP-B3 «(under [E-LEV])»: the only place [E-LEV] appears (header table l. 34-35; L-5: «HYPOTHESIS [E-LEV] for UP-JUMP3,
  UP-B3 and CHAIN3 only»). [E-LEV] makes the e-priorities increase with level, so a step to a more relevant e-vertex must climb in level,
  and the only level-raising edges are Ξ-edges to a higher level.
- Fixes 1-4 and L-5 change no bound: they rename CHAIN3's premises to the landed RESULTS R121 and R124 (fixes l. 108-113) and keep
  «CONDITIONAL» (l. 102). L-5 states the same formula and the same restriction: «a polynomial in N + M for U(G) ≤ B, B fixed».
- READING on looseness: the proof only ever uses the number of ascents B_v := max_t ascents of seq_t(v), not U. The same proof gives
  D^tot_E(v) ≤ (2M + 3)·F′_(B_v)(M) with B_v ≤ U. Separately, the abstract HUB-ASC data (R121: B = 1 max 16 at M = 4, 29 at M = 5) are far
  below F′_1; the 2^B exponent comes from the proof's squaring, and no instance is known that needs it.

## 2. (2) DATA (experiments/si/box98; engines: own = L-RED R221 own.py on IDEAL-CYC, g3 = L-NEW's Γ3 N5′-xi from S3, pins as box91)
- asc98.py (unit: (state, vertex) for ascents and upfail; vertex for D^tot_E; genome for U, T): seq_t(v) := the e-vertices of P_t(v)
  more relevant than Λ_t(v) in play order; maxasc = max ascents; Dmax = max_v D^tot_E(v) (distinct (Λ, E) pairs); upfail = (t, v) with
  ascents > U (UP-B / UP-B3, must be 0 under [E-LEV]; gamma3 orders e-priorities by (lev, gate), so [E-LEV] holds on every instance).
- Frozen set (box 91's 11 + box 93's 8; out/asc98_own.out, asc98_g3.out): U, T, maxasc, Dmax IDENTICAL on the two engines (sumD differs:
  g3 also counts the pads). upfail 0. U from 1 (k1fail_202) to 99 (MW32_2); maxasc ≤ 5 (DHIB26_2804; 4 on WC4_2, 16 on WC16_2 with T = 4,
  Dmax 3); T and Dmax largest on MW32_2 (T 199, Dmax 131, maxasc 2) and MWR16_2 (T 102, Dmax 34). Every row has T ≤ N + M.
- Climb (climb98.py, seed 9801, 600 iterations per shape, score T3 on g3; out/climb98.out; bests frozen in inst/ with SHA1SUMS by
  freeze98.sh): best T3 = 8, 8, 12, 12, 16, 19, 15 at (d, w, D) = (2,2,3), (2,3,3), (3,3,3), (3,4,3), (4,4,3), (4,5,3), (5,5,3), i.e. N =
  4, 6, 9, 12, 16, 20, 25, M = 10, 14, 22, 29, 40, 52, 59, U = 4, 3, 6, 9, 15, 12, 16. On the bests (out/ascC98_*.out, two engines, rows
  identical in U, T, maxasc, Dmax): maxasc ≤ 2, Dmax ≤ 14, upfail 0. T3 ≤ N + 4 at every shape.
- What was NOT done: no instance without [E-LEV] (gamma3 fixes the (lev, gate) e-order; a reversed-order builder is not in the pinned
  tools); no climb on N5′-xi's total after the first fallback; climbs are small (N ≤ 25).

## 3. (2) The design reading: what a super-polynomial family would need (READING, no claim)
- With B ascents, seq_t(v) is B + 1 descending segments, each more relevant than the last; lex order is decided by the most relevant
  segment. So a hub's e-set could behave like an ODOMETER: a lower segment may «reset» when a higher one rises. Each item's own chain is
  lex-nondecreasing (E-MON3), so a reset must route through a DIFFERENT item; counting items per band gives at most about M^{O(B)} hub
  values: n^{O(U)}, far below CHAIN3's n^{O(2^U)}, and quasi-polynomial if B ≈ log M were realised.
- Why the measured runs do not realise it: a Howard step moves each mover at once to its best option, so an intermediate odometer state
  is visited only if its improvement is revealed one step at a time. In Friedmann's exponential lower bounds for switch-all policy
  iteration this is the job of delay gadgets (cycles that Odd holds open); in Γ3(G) Odd's only choices are the gates' two faces, and the
  e-face of a gate tracks one mover (E-FACE-PAYS (b), PROVISO / PROVISO3: S(p_e) = S(D)). Whether genomes can host such delays is the open
  question; the families and climbs measured do not.
- So the stress axis is not U and not the ascent count, but the number of distinct e-sets of a hub (Dmax), which is bounded by T + 1
  and has stayed linear in N everywhere (§2).

## 4. (3) CONJECTURE U-FREE (with its strongest DATA)
- Statement: for every genome G, N5′-xi from S3 on Γ3(G) has T3 ≤ N + M + 4 (and T_CYC ≤ N + M + 4 on IDEAL-CYC), independent of U(G).
  Weaker form (the one that matters): T3 ≤ poly(N + M) independent of U, i.e. the mover-phase part of G-N5-TIME's question for
  N5′-xi on Γ3(G) (G-N5-TIME itself is about N5; nothing here is about the iterations after the first fallback).
- Strongest DATA: T ≤ N + M on 19 frozen instances (U up to 99, two engines identical in T); climb bests T3 ≤ N + 4 at N ≤ 25 (U up to 16);
  the fleet's k = 1 climb records are linear in N + M (Lead 22:12Z: «The k = 1 records are all linear in N + M»; not re-run here). Max T / (N + M) over all of these: 0.57 at
  C98_2_2_3 (N 4, M 10, T3 8); over N ≥ 20: 0.26 (C98_4_5_3, 19 / 72).
- What would refute it: a genome family with T3 ≥ (N + M)^(1 + ε); a family with Dmax super-linear in N would be the first sign.
- Status: CONJECTURE, not a lemma. No obstruction is proved; §3 is a reading.

## 5. Sources opened (this box)
- claude/l-new 93531b03 docs/new/P-N5-CHAIN.md §2, §7-§8 (l. 256-310); claude/l-new docs/new/P-N5-CHAIN-fixes.md (l. 9-14, 102-113) and
  P-N5-CHAIN-line-L5.txt; trunk docs/RESULTS.md R121 (F′_B degree, HUB-ASC data, NOUP control), R123.
