# Box 185 N5-MOVES: MOVES-2D is a quadratic bound on T^R in disguise — PROVED (lane) REDUCE-XI: on every IDEAL-ACYC run, every step but the last moves a Ξ-target mover, so T ≤ 1 + Σ_(Ξ-targets z) moves(z) (non-Ξ-target movers need no bound), hence MOVES-2D ⇒ T^R(d) ≤ 4d² − 4d + 3, and conversely max moves ≤ T; so MOVES-poly ⇔ T^R-poly and no lemma weaker than a polynomial bound on T^R gives MOVES-2D. DATA: the exact maxima are «metronomes» (one mover moving at every step of a SHORT run, Ξ-cross-wired onto the pair below); long runs spread their moves (TRL_d7_T26: ≤ 6 moves per mover in 26 steps). No proof of MOVES-2D, no kill.
L-NEW successor 57, 2026-11-06 (from 18:3xZ by date -u; see the commits). Lead brief BOX 185: (1) settle the reduction «MOVES-2D for
all movers ⇒ T^R(d) ≤ Σ_x moves(x) = O(d²)», including whether non-Ξ-target movers need a separate bound; (2) proof attempt of MOVES-2D
or a level-wise form, or the failing configuration as a kill seed for L-RED (R214 attacks MOVES-2D in parallel). Premises: RESULTS R104
(definition of the IDEAL model), R105 RISE / XI-NEW / MONO / ENC (landed, «at any degree», any width), R110 (definition of 𝓛^R_d),
R113 (P-IDEAL-ALIGN: ALIGN, F0, PAIR-DOUBLE, MOVES; landed). Labels: PROVED (lane, unrefereed) / DATA / CONJECTURE / READING. Not a
TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Answer
- (1) Settled, in a sharper form than asked. PROVED (lane) Lemma REDUCE-XI (§1): on every run of every IDEAL-ACYC genome (any degree,
  any width), with Z := {z : z = xt(x, k) for some option (x, k)} (the Ξ-target movers), every step t − 1 with 2 ≤ t ≤ T moves a member
  of Z. Hence T ≤ 1 + #{t ∈ [1, T − 1] : Mv_t ∩ Z ≠ ∅} ≤ 1 + Σ_(z ∈ Z) moves(z). The movers outside Z need NO bound: they never carry
  a step other than the last one alone.
  - Corollary (𝓛^R_d). 𝓛^R_d has 2d movers (levels 0, …, d − 1; the brief's «N = 2(d + 1)» is L-RED's top-level index m = d − 1 read as
    d). With R113 F0 (level-0 movers move ≤ 1 time): T ≤ 3 + Σ_(z ∈ Z, lev(z) ≥ 1) moves(z). So MOVES-2D (every z ∈ Z moves ≤ 2d times)
    ⇒ T^R(d) ≤ 3 + (2d − 2)·2d = 4d² − 4d + 3. A level-wise form moves(z) ≤ c·(lev(z) + 1) gives T^R(d) ≤ 3 + c·d(d + 1) − 2c.
  - Converse (trivial): moves(z) ≤ T. So, for any f, «max_(z ∈ Z) moves(z) ≤ f(d) on 𝓛^R_d» and «T^R(d) ≤ 3 + (2d − 2) f(d)» are
    equivalent up to the factor 2d − 2: MOVES-poly ⇔ T^R polynomial. READING: MOVES-2D is not a local statement that could be proved
    below G-N5-TIME on 𝓛^R; any proof of it is a proof of T^R(d) = O(d²). MOVE-RISE / RISE-EQUIV are not needed for (1).
  - DATA: REDUCE-XI holds with 0 violations over every start of all 214 distinct in-tree 𝓛^R genomes (d 1-8, 2^(2d) starts each; L-NEW
    box150-184 files + L-RED r212 / r213 files), and is TIGHT: T = 1 + #{Z-moving steps before the last} on some run of 210 of the 214
    genomes (log/corpus_eval.txt, «minslack 0»).
- (2) No proof of MOVES-2D (by (1), it would be a quadratic bound on T^R). What is proved and what the data show:
  - PROVED (lane) Lemma AND-GATE (§2), the exact move rule of a degree-2 mover: x moves at step t iff its Ξ-preferred option under s_(t−1)
    is not its current option AND is its key-preferred option under s_t. So between two consecutive moves BOTH the Ξ-preference (PF) and
    the key preference (KF) change: moves(x) ≤ 1 + min(KF_x, PF_x), and each Ξ-preference flip needs a strict rise of the value of the
    newly preferred option (MONO + ENC).
  - DATA (§3) level-wise maxima of moves of Ξ-target movers (exact = L-RED R213 SAT; others: every start of every corpus genome + my
    climbs): d 3: 1, 3, 4 (exact); d 4: 1, 3, 7, 7-8 (exact); d 5: 1, 3, 6, 7, 8; d 6: 1, 3, 4, 6, 5, 5; d 7: 1, 3, 4, 6, 5, 5, 5;
    d 8: 1, 2, 4, 4, 3, 4, 3, 4. Every value ≤ 2d. Level-wise «moves ≤ 2(l + 1)» is FALSE at d 4, l 2 (L-RED exact witness m4_z4_r7:
    7 > 6); «moves ≤ 2l + 3» fits all data (DATA only).
  - DATA (§3, the mechanism of the maxima). The exact witnesses are METRONOMES: m3_z4_r4 (d 3, level 2) moves at 4 of 4 steps;
    m4_z6_r7 (d 4, level 3) at 7 of 7; m4_z4_r7 (d 4, level 2) at 7 of 8. In each, the mover's two options are Ξ-CROSS-WIRED onto the
    pair below (option k, which W-points to 2(l − 1) + k, has Ξ-target 2(l − 1) + 1 − k), the lower pair moves alternately, and the
    Ξ-preference and the key preference flip TOGETHER at every step (trace.py). These runs are SHORT (T 4, 7, 8 against T^R = 8, 13).
    Long runs spread their moves: the longest corpus runs have max moves 7/14 (dd_d5_F14), 6/16 (rise_d6_R14), 6/26 (TRL_d7_T26),
    4/17 (d 8). So high move counts appear only in dense short runs, and long runs need many movers each moving O(1)-ish times.
  - The brake (READING). By AND-GATE + PAIR-DOUBLE's tightness conditions, a key-tight mover (moves = 1 + F(l − 1)) needs the pair
    below to flip at every step of a long stretch, i.e. a dense lower pair, and density costs steps below at the same rate (the
    PAIR-DOUBLE tightness argument forces consecutive lower flips ≥ 2 steps apart, and k consecutive tight levels force spacing ≈ 2^k
    at the bottom: F ≤ T again). So the data's linear cap is the same phenomenon as T^R's linear increments; I found no brake that is
    stated without T.
  - No kill. Best found: d 5 level 4: 8 (climb from a bottom-lift of m4_z6_r7; = L-RED's best); d 5 level 3: 7 (bottom-lift of
    m4_z4_r7 keeps its 7; climbs do not raise it); exhaustive re-wiring of one mover's options on dd_d5_F14 (Ξ-targets, ranks,
    parities): mover 8 at most 3, mover 9 at most 2 (the cross-wiring onto (6, 7) is cyclic there: 5 → 8).
- Kill seed for L-RED R214 (a much smaller SAT query than max-moves): DENSE(d, l, r) := «some Ξ-target mover of level l moves at
  EACH of the steps 1, …, r». The exact maxima at d 3 / d 4 level 3 are dense (r = 4, 7). DENSE(5, l, 11) SAT for any l kills
  MOVES-2D at d 5 (11 > 10); the metronome needs the lower pair to flip at every step 2, …, 11. Seeds (experiments/new/box185/out/):
  ld4_1.txt (d 5, level 3, 7 moves, the bottom-lift of m4_z4_r7), h_d5_L4_ld6.txt (d 5, level 4, 8 moves).

## 1. Lemma REDUCE-XI (PROVED, lane)
- Hypotheses: G IDEAL-ACYC (RESULTS R104's model, acyclic Ξ-graph), any degree, any number of movers per level; any run, T its number of
  steps, Mv_t := {x : s_t(x) ≠ s_(t−1)(x)}; Z := {xt(x, k) : (x, k) an option, xt(x, k) ≠ X}.
- Statement: for every t with 2 ≤ t ≤ T, Mv_(t−1) ∩ Z ≠ ∅. Hence T ≤ 1 + #{t ∈ [1, T − 1] : Mv_t ∩ Z ≠ ∅} ≤ 1 + Σ_(z ∈ Z) moves(z).
- Proof. Let 2 ≤ t ≤ T. Mv_t ≠ ∅ (R104: a step changes the state), so a least-level mover h of step t exists. R105 (RISE), «at any
  degree»: «that option's value rose strictly at step t − 1, and some strict Ξ-descendant of h on its chain under s_(t−2) moved at step
  t − 1». A strict Ξ-descendant y of h on the chain (h, w), (y_1, s(y_1)), (y_2, s(y_2)), … is some y_j with j ≥ 1, and y_j =
  xt(y_(j−1), ·) (y_0 := h) is the Ξ-target of an option, so y ∈ Z, and y ∈ Mv_(t−1). The map t ↦ t − 1 is injective from [2, T] into
  [1, T − 1], so T − 1 ≤ #{t ∈ [1, T − 1] : Mv_t ∩ Z ≠ ∅}, and each such t is counted by moves(z) for some z ∈ Z. ∎
- Corollary 𝓛^R. On 𝓛^R_d (2d movers; R113 F0: moves(0), moves(1) ≤ 1): T ≤ 3 + Σ_(z ∈ Z, lev ≥ 1) moves(z); MOVES-2D ⇒ T^R(d) ≤
  4d² − 4d + 3; conversely max_(z ∈ Z) moves(z) ≤ T ≤ T^R(d).
- Does NOT claim: any bound on moves; that Z-moves are the least-level movers; anything about Ξ-cyclic genomes.

## 2. Lemma AND-GATE (PROVED, lane; R104 definition; the last clause uses R105 ENC + MONO)
- Hypotheses: G IDEAL-ACYC; x a mover with deg(x) = 2; any run. π_s(x) := the option of x whose Ξ-value under s is the better one
  (well defined: the two chains of x differ in x's own β, so their β-sets differ and are strictly ordered).
- (a) x ∈ Mv_t ⟺ s_(t−1)(x) ≠ π_(s_(t−1))(x) and π_(s_(t−1))(x) = KP_(s_t)(x).
- (b) If x moves at t < t′ consecutively, then π(x) changes at some step of [t, t′ − 1] and KP(x) at some step of [t + 1, t′]; so
  moves(x) ≤ 1 + min(KF_x, PF_x), PF_x := #{t ∈ [1, T] : π_(s_t)(x) ≠ π_(s_(t−1))(x)}.
- (c) At a step t with π_(s_t)(x) = b ≠ a = π_(s_(t−1))(x), the value v(x, b) rises strictly at t (so PF_x ≤ R(x, 0) + R(x, 1), R(x, k) the
  number of strict rises of v(x, k)).
- Proof. (a) A_(s_(t−1))(x) = {s_(t−1)(x)} if π = s_(t−1)(x), and both options otherwise; the step gives x the option of A with the least
  key under s_t (R104). So x moves iff |A| = 2 and the key-least option under s_t, KP_(s_t)(x), is the other one, i.e. = π. (b) By (a),
  s_t(x) = π_(s_(t−1))(x) = KP_(s_t)(x) and s_(t′)(x) = π_(s_(t′−1))(x) = KP_(s_(t′))(x), and s_(t′)(x) ≠ s_t(x) (deg 2, consecutive moves
  alternate). The windows of consecutive moves are disjoint. (c) By ENC + MONO, v(x, a) is non-decreasing; v_(t)(x, b) > v_(t)(x, a) ≥
  v_(t−1)(x, a) > v_(t−1)(x, b). ∎
- Does NOT claim: a bound on PF or KF (on 𝓛^R, KF_x = F(l − 1) by R113 MOVES, exponential in the worst case of PAIR-DOUBLE).

## 3. DATA (experiments/new/box185/)
- Tool mv.c (C; step function copied from L-RED R212 fl.c, stepL, with credit): `mv eval m` (per-level max moves of Ξ-targets,
  of all movers, the longest stretch of consecutive moves, REDUCE-XI check, all 2^N starts), `mv climb m LEV seed iters out [seed]`
  (env ANNEAL, ANYZ, FAM), `mv opt m x` (exhaustive re-wiring of one mover's two options). Cross-check xval.py against L-NEW's own
  simulator box150/check.py Gen: 46 genomes (d 1-5), every start, Tmax, per-level max moves and REDUCE counts: 0 mismatches
  (log/xval.txt). trace.py (per-step position, Ξ-preference, key preference of one mover), flips.py (F, moves, PF per run), lift.py
  (add a top level), liftdown.py (add a level below).
- Corpus (log/corpus_eval.txt): 214 distinct 𝓛^R genomes, d 1-8, from experiments/new/box150-184 and L-RED claude/l-red
  experiments/red/r212, r213 (read-only copies in my scratch). Per level, (max moves of a Ξ-target, longest consecutive-move stretch):
  d 3: (1,1) (3,3) (4,4); d 4: (1,1) (3,3) (7,4) (7,7); d 5: (1,1) (3,3) (6,3) (7,3) (5,3); d 6: (1,1) (3,2) (4,2) (6,2) (5,2) (5,2);
  d 7: (1,1) (3,2) (4,2) (6,2) (5,3) (5,2) (5,2); d 8: (1,1) (2,2) (4,3) (4,3) (3,2) (4,2) (3,3) (4,1). REDUCE-XI: 0 violations.
- Exact witnesses (L-RED R213 SAT models, claude/l-red experiments/red/r213/out/m3_z4_r4.json, m4_z4_r7.json, m4_z6_r7.json),
  traced (trace.py, flips.py): m3_z4_r4 start 100100, z 4: T 4, moves 4, F = [2, 4, 4]; m4_z6_r7 start 01110010, z 6: T 7, moves 7,
  F = [2, 3, 7, 6]; m4_z4_r7 start 10111010, z 4: T 8, moves 7 = 1 + F(1), F = [2, 6, 5, 4] (level 1 PAIR-DOUBLE-tight, z key-tight).
  dd_d5_F14 start 1101111110, z 6: moves 7 = 1 + F(2) at steps 2, 4, …, 14 (period 2; Ξ-targets 7 (its partner) and 5).
- Climbs (log/): random-seeded climbs are weak (d 4 level 2: 4-5 against the exact 7); seeded: d 5 level 4: 7 from dd_d5_F14, 8 from a
  bottom-lift of m4_z6_r7 (out/h_d5_L4_ld6.txt; start 0100110010, T 11, z 8 moves at 8 of 11 steps, Ξ-cross-wired onto (6, 7): xt(8, 0) = 7,
  xt(8, 1) = 6; F = [2, 4, 5, 9, 7]); d 5 level 3: 7 (bottom-lift of m4_z4_r7, out/ld4_1.txt; climbs stay at 7).

## 4. Next (Lead decides)
- L-RED: DENSE(5, l, 11) by SAT (one mover moving at each of steps 1-11); SAT kills MOVES-2D at d 5, UNSAT at every l says that
  metronomes are capped (not a proof of MOVES-2D: period-2 movers like dd_d5_F14's z 6 are not dense).
- Proof side: by REDUCE-XI any proof of MOVES-2D is a proof of T^R(d) = O(d²); the per-mover form adds nothing over T. The only
  route I see is a global one (a potential over all levels whose drop per step is ≥ 1 and whose range is polynomial), which box 179
  (LP potentials) found DEAD for level-local linear potentials.
