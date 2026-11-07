# Box 180 N5-RISES: value rises per option — RISE-EQUIV (max rises ≤ T ≤ 1 + Σ rises), so a «coarse value scale» is G-N5-TIME itself; DATA: on every champion and climb, every option rises at most 2d times (tight at d 4, 5): CONJECTURE RISE-2D, which would give T^R(d) ≤ 8d² + 1
L-NEW successor 56, 2026-11-06 (from 11:05Z by date -u; see the commits). Lead brief BOX 180 (11:07Z): (1) measure R(x, k) = the number
of strict rises of an option's value along a run, against P (#maximal Ξ-paths), depth and d, on the champions; (2) adversarial: one
option with superpolynomially many rises in one run, or the mechanism that stops it. Model: RESULTS R104's IDEAL model; R105 ENC, MONO,
XI-NEW, RISE (landed); 𝓛^R_d = R110's definition. Labels: PROVED (lane, unrefereed) / DATA / CONJECTURE / DEAD. Not a TARGET.md claim.
G-N5-TIME stays OPEN.

## 0. Answer
- PROVED (lane) Lemma RISE-EQUIV (§1). In every IDEAL-ACYC run (any degree, any width): (a) every option value v(x, k) is non-decreasing,
  and R(x, k) = the number of rises of cv(xt(x, k)) (0 if the Ξ-target is X); (b) R(x, k) ≤ T; (c) T ≤ 1 + #{t ≤ T − 1 : some option
  value rises at step t} ≤ 1 + Σ_(x,k) R(x, k). Hence, on any family, max_(x,k) R is polynomial in N + M iff T is, and T ≤ 1 + M·max R.
  On 𝓛^R_d (M = 4d): T ≤ 1 + 4d·max R.
- Consequence for part (2): a genome with one option rising superpolynomially often in a single run IS a superpolynomially long IDEAL
  run (by (b)), i.e. the fleet's open lower-bound question, and conversely. The «coarse value scale» route is not a weaker target than
  G-N5-TIME; it is the same target, in the unit «rises per option».
- DATA (1) (§2, log/rises_champions.txt): 40 runs on the champions (L-RED R212 keep TR_d5_T16, TR_d6_T22, TRL_d6_T22; R207 keep
  TR_d6/d7, T* d 5-10; R208 keep; box152/156/157/160/172 ladders; L-SI inf18_m3), from the stored start and the arg-max start (N ≤ 14).
  max R per run ≤ 15 (Tstar_d10_T46), and max R ≤ 2d in all 40 runs. Equality at dd_d5_F14 (option (4, 0): R 10 = 2·5). Max R is far
  below P − 1 (PATH-RISE): e.g. Tstar_d10: R 15 against P 69; TR_d6_T22: R 8 against P 29. Ratio max R / T between 0.25 and 0.75. No
  value ever falls (0 violations of (a)); (c) holds in all runs.
- DATA (2) (§3): adversarial hill-climbs for ONE option's rises (box180/climbR.py; objective (max R, T); mutations of Ξ-targets, ranks,
  parities, gates, start). Best: d 4 R 8 = 2d (seed max_d4_L13, T 11); d 5 R 9 (seed R212 TR_d5_T16, T 13); d 6 R 11 (seed R212 TR_d6_T22,
  T 19); d 3: R 5 at best (climb seed 33, and corpus iso_d3_6), never 6. Random-seeded climbs stall at T ≤ 7. No run exceeds 2d.
- CONJECTURE RISE-2D (lane; DATA above, tight at d 4 and 5): on 𝓛^R_d every option value rises at most 2d times in every run. With
  RISE-EQUIV (c): T^R(d) ≤ 1 + 4d·2d = 8d² + 1. Kill: one 𝓛^R_d run with an option rising 2d + 1 times. The most promising kill spot is
  d = 3, where T^R(3) = 8 > 2d = 6, so 7 rises are not excluded by T alone. Climbs there: max R 5 (8 climbs, 4 of them all-start).
- Mechanism (READING, why superpolynomial visits stall). A rise of v(x, k) at step t needs a move at step t of some mover on the current
  chain below (x, k): values change only through moves, and a mover moves only to a strictly better option. By KEYFLIP, each move of a
  degree-2 mover y needs a flip of its key preference, and by LOCAL-KP that needs a move below lev(y). So each new path value visited costs
  a fresh key flip below, and the Ξ-DAG's exponential path count (PATH-RISE) can be walked in order only if a clock below flips
  exponentially often. That is exponential T again (box 170: gadgets add moves, not steps; F ≤ T). The diamond / clock constructions of
  boxes 165-170 therefore cannot beat T: rises are capped by steps, by RISE-EQUIV (b).
- Per-option shape (DATA, log/riseshape.txt; 5,796 options over the corpus + champions + climbs): R ≤ 2·dep fails on 10 options and
  R ≤ D + 1 fails on 37 (D = #movers below); worst u4_d8 (a degree-3 file) option (7, 2): R 12, dep 6, D 6. So no per-option bound by
  the Ξ-shape below. The data bound is in d (levels), not in depth: the brake is the key ladder, not the Ξ-DAG.

## 1. Lemma RISE-EQUIV (PROVED, lane)
- (a) By R105 ENC, v_s(x, k) = ε(x, k) + cv_s(xt(x, k)) if xt(x, k) is a mover, and ε(x, k) if it is X. By R105 MONO, cv_s(z) never
  decreases along a run. So v(x, k) never decreases, and it rises at step t iff cv(xt) does.
- (b) Each step changes the state once, so each value rises at most once per step: R(x, k) ≤ T.
- (c) By R105 XI-NEW and RISE: for every t ≥ 2, a least-level mover h_t of step t moves to an option w whose value rose strictly at step
  t − 1 (RISE: «that option's value rose strictly at step t − 1»). So every step t − 1 with t ∈ [2, T] has a rise:
  T − 1 ≤ #{t ∈ [1, T − 1] : some value rises at t} ≤ Σ R. ∎
- Machine check: box180/rises.py counts FALL (a value falls) and REDUCE (T > 1 + #rise-steps): both 0 on all 40 runs.

## 2. Measurement (1): log/rises_champions.txt
- Columns: d (levels), N, T, Σ R, max R (and 2d), the arg-max option, its P and depth, and the largest P of the genome.
- Selected rows: TR_d5_T16 (R212) d 5 T 16 max R 7; TR_d6_T22 (R212) d 6 T 22 max R 8 (P 29); TR_d7_T20 d 7 T 20 max R 5; Tstar_d5..d10:
  max R 7, 8, 10, 11, 12, 15 at T 17, 25, 31, 33, 42, 46; dd_d5_F14 T 14 max R 10 (= 2d); nd2_d5_F12 T 12 max R 9; max_d4_L13 T 13
  max R 6; iso_d4_st9 T 11 max R 5. In the T* runs, max R grows by about 1.5 per level, like T* (linear increments).
- IM-frame realisations (L-RED R212 keep T0_m5_16.txt etc.) are text files in another format: NOT RUN here.

## 3. Adversarial (2): climbs (log/climbR_*.txt, log/climbRall_*.txt; out/climbR_*.json)
- Plain climbs (genome start only), 3,000-6,000 iterations: d 4 seed max_d4_L13: R 8 (T 11); d 5 seed TR_d5_T16: R 9 (T 13); d 6 seed
  TR_d6_T22: R 11 (T 19); random seeds d 4, 5, 6: R 5, 4, 4 (T 7, 5, 6).
- Climbs at d 3: four plain climbs (30,000 iterations, random seeds 31-34): R 4, 4, 5, 4. Four all-start climbs (ALLSTARTS=1: score =
  best over the 64 starts; 4,000 iterations; seeds kf8_d3_t8, kf4_d3_t8, random, kf3_d3_t8): R 4, 4, 3, 3. The corpus max at d 3 is 5
  (iso_d3_6). So max R at d 3 is ≥ 5 (DATA) and, if RISE-2D holds, ≤ 6.
- Why climbs cannot be the whole answer: by RISE-EQUIV (b) a superpolynomial R needs a superpolynomial T, which every L-RED climb since
  R178 has looked for without success (T* increments linear, d 4-10).

## 4. Files (experiments/new/box180/)
- rises.py (R per option, FALL / REDUCE checks, arg-max start for N ≤ 14), riseshape.py (R against dep and D), climbR.py (climb;
  ALLSTARTS=1 for all-start scoring). log/, out/ as above. L-RED tree: `git archive origin/claude/l-red experiments/red` at 49d3fdb0
  (scratch, not committed).

## 5. Next (Lead decides)
- Kill RISE-2D: exact max R on 𝓛^R_3 by SAT (L-RED's T^R(3) encoding plus a rise counter on one option); 7 rises kill it.
- Proof side: RISE-2D would follow from «between two rises of cv(z), each level's pair flips at most twice», a statement in the 8-state
  automaton of ALIGN. To be tested.
