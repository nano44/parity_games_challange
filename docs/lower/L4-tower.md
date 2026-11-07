# L4: the fifth doubling level, the driven-block relaxation, and why stacked doubling stops (L-LOWER successor 4, BOX L4)

Box: Lead BRIEF (L-LOWER successor 4, D1/D14/D18/D20), BOX L4 «the fifth doubling level, i.e. S(h)», angle «EXPLICIT RECURSIVE
design, with proofs». Written 2026-11-07 from 04:20Z (date -u). Labels: PROVED (lane, unrefereed) / CANDIDATE / DEAD (instance) /
DATA / READING. Nothing here is a result in the sense of CLAUDE.md. Nothing here bounds T polynomially; G-N5-TIME stays OPEN. Not a
TARGET.md claim (diff in §8).

## 0. Premises and notation
- Landed only: RESULTS R104 (l. 9864) — its definition of the IDEAL model only; RESULTS R105 (l. 10155) — ENC («the Ξ-order of β-sets
  is the order of the integers Σ ±2^rank (+ for even parity), so … the value of option (x, k) is ε(x, k) plus the current value of its
  Ξ-target») and MONO; RESULTS R110 — its definition of 𝓛^R_d only; RESULTS R113 (l. 12152) — ALIGN (b), (c), F0, PAIR-DOUBLE and its
  notation (F(l), c_l(s), γ_l(j), b-steps). No «signed, not landed» item and no lane lemma of another lane is a premise of §1-§4.
- Notation as in docs/lower/L3-families.md §0. For a pair l: p := 2l, q := 2l + 1. cv_s(x) := the integer value of x's current option
  (ENC). D_l(s) := cv_s(2l) − cv_s(2l + 1). Level l ≥ 1 is DOUBLING in a run if F(l) = 2F(l − 1) + 2 (equality in PAIR-DOUBLE). An
  l-b-step is a step t with c_l(s_t) ≠ c_l(s_(t−1)); an l-window is a maximal set of consecutive steps containing no l-b-step except
  possibly its first (the windows partition [1, T]; the first window starts at step 1). Φ_l(t) := #{x ∈ {p, q} : s_t(x) ≠ c_l(s_t)}.
- Movement rule used throughout (R104 definition + ALIGN (b)): a mover x of level l ≥ 1 moves at step t iff its other option is strictly
  better than its current one under s_(t−1) and c_l(s_t) is that other option; it then moves to c_l(s_t).

## 1. Lemma DRV-RELAX (PROVED, lane) and what it shows
- The DRIVEN BLOCK of G ∈ 𝓛^R_d: the movers of levels 1, …, d − 1 with their options, β's, Ξ-targets and gate orders γ, and an
  exogenous bit e(t) in place of c_1. Its transition from s with input e: values on s (ENC); level by level, lowest first, c := e for
  level 1; a mover moves to c iff its other option is strictly better under s and equals c; then c_(l+1) := [s′(p) ≠ c] if s′(p) ≠
  s′(q), γ-order if together (R113 ALIGN (c)). Implementations: experiments/lower/l4/drv.c (exact longest paths, climbs) and
  drvpath.py (written separately, Python).
- Claim. If no option of G Ξ-targets a level-0 mover, then for every run of G the sequence (s_t restricted to levels ≥ 1) is a walk of
  the driven block with e(t) := c_1(s_t), and e changes at most twice. Hence T(G) ≤ 2 + LP₂(block) and F_G(l) ≤ 2 + Fmax₂(block, l)
  for l ≥ 1, where LP₂ is the longest walk with moving steps and Fmax₂(·, l) the largest number of changes of the order of pair l
  along such walks, both over inputs with ≤ 2 changes (and from the stored start when the start is fixed).
- Proof. Chains of options of movers of level ≥ 1 never visit level 0 (no level-0 Ξ-target), so their values under s depend only on s
  at levels ≥ 1 (ENC). The movement rule (§0) and ALIGN (c) for the order of each pair give exactly the block transition with c_1(s_t)
  as input. c_1(s) is the order of pair 0, which changes F(0) ≤ 2 times (R113 F0). A step moving only level-0 movers leaves the block
  state unchanged; there are at most 2 (each level-0 mover moves at most once, F0); each such step can change the order of a pair once
  without a block move, which is the «+2». ∎
- DATA (exact DP, drv.c STARTONLY, from the stored start; blk.py export; replay state-identical to l3/sim.py, l4check.py):
  | genome | real T | block LP, e free | real F(3), F(4) | Fmax₂ F(3), F(4) |
  | --- | --- | --- | --- | --- |
  | REC_d10_tower_mu30 (cc94dc9c…) | 35 | 39 (40 over all starts) | 30, 23 | 30, 23 |
  | REC_d10_tower + 4 TOP-ADD levels (d 14) | 35 | — | 30, 23 | 30, 23 |
  | RECT_d13_T99 (8946c0ff…) | 99 | 101 | — | — |
  | RECT_d11_T59 | 59 | 59 | — | — |
  Reading: an unrestricted key source at the bottom buys ≤ 4 steps on these records, and with ≤ 2 key changes (what F0 allows) the
  tower block's F(4) cap is exactly its real 23. So R113 F0 (the weak key source at level 0) is not what stops the fifth doubling level.
- DEAD (method): with e unrestricted, a climb reaches «F(4)» 63 at m 13 (out/rf4_s2.gen) only by 57 e-changes relayed up through split
  pairs; F0 forbids this. Every relaxed search here therefore uses ≤ 2 e-changes (env EB=2).

## 2. Lemma DUAL (PROVED, lane; ENC and the definitions)
- Call pair l SPLIT-FROZEN if xt(p, a) = xt(q, 1 − a) for a = 0, 1 (CROSS; e.g. p → (2l − 2, 2l − 1), q → (2l − 1, 2l − 2)) and
  JOINT-FROZEN if xt(p, a) = xt(q, a) for a = 0, 1 (PARALLEL). In general call a state (a, b) of pair l FROZEN if xt(p, a) = xt(q, b).
- Claim. If (s(p), s(q)) = (a, b) is frozen, D_l(s) = ε(p, a) − ε(q, b) (a constant of the pair's state). For a CROSS pair: split states
  are frozen, and in a together state on j, D_l = ε(p, j) − ε(q, j) ± D_(l−1)-type difference of the two distinct targets; the order of
  the pair (ALIGN (c)) relays c_l in split states and is the constant γ_l(j) in together states. For a PARALLEL pair: together states are
  frozen, split states relay both. Proof: ENC: cv(p) = ε(p, a) + cv(y), cv(q) = ε(q, b) + cv(y) with y the common target (0 if X). ∎
- Reading: a CROSS pair relays keys and blocks Ξ-differences when split, relays Ξ-differences and blocks keys when together.

## 3. Lemma DOUBLE-EQ′ (PROVED, lane; R113 ALIGN (b), (c) and PAIR-DOUBLE's accounting, re-derived)
- Hypotheses: G ∈ 𝓛^R_d, 1 ≤ j ≤ d − 1, any run, level j doubling.
- Claim. (E1) Φ_j(0) = 2 and Φ_j(T) = 0; (E2) Φ_j(t − 1) = 0 at every j-b-step t; (E3) no step moves both p and q, and the order of
  pair j changes exactly at the steps moving p or q; (E4) in every j-window each of p, q moves exactly once; (E5) γ_j(0) = γ_j(1) =: γ
  and the first of p, q to move in every j-window is p iff γ = 0; hence, if F(j − 1) ≥ 1, all four states of pair j occur in the run.
- Proof. Write c_t := c_j(s_t), ord_t the order of pair j under s_t (ALIGN (c): [s(p) = c] if split, γ(i) if together on i). Movers land
  aligned (movement rule). At a non-b-step a flip needs a mover and every mover lowers Φ by 1, so flip_t ≤ Φ(t − 1) − Φ(t), with equality
  iff no mover, or exactly one mover and a flip. At a b-step with a := Φ(t − 1) and r movers (movers are aligned with c_(t−1), i.e. not
  with c_t; non-movers toggle alignment): Φ(t) = 2 − a − r, and the cases give flip_t − (Φ(t − 1) − Φ(t)) = h(a, r) with h(0, 0) = 2
  (together on c_(t−1) before and after the toggle: order γ(c_(t−1)) unchanged, flip 0), h(0, 1) ≤ 2, h(0, 2) ≤ 1, h(1, 0) = 1, h(1, 1) ≤
  0, h(2, 0) = −2 (no flip). Summing: F(j) ≤ Φ(0) − Φ(T) + Σ_b h ≤ 2 + 2F(j − 1), and equality forces (E1), a = 0 and r ≤ 1 at every
  b-step with a flip when r = 1 (E2), and equality at every non-b-step (E3, first part); a b-step with a = 0, r = 0 has no flip, so the
  flips are exactly the moving steps (E3). (E4): inside a window c is constant; Φ starts at 2 (r = 0) or 1 (r = 1) right after the
  opening b-step (or Φ(0) = 2 for the first window) and must be 0 before the next b-step and at T (E1, E2); each move lowers Φ by 1 and a
  member that has moved is aligned and cannot move again while c is constant. (E5): in a window with value c′, the pair is together on
  w = 1 − c′ before its first move (Φ = 2 there, or a = 0 at the opening b-step); the first move must flip: γ(w) → [first mover is p];
  the second move must flip: [first is p] → γ(c′). So [first is p] = ¬γ(w) and γ(c′) = γ(w); consecutive windows have different c′, so
  γ(0) = γ(1) if F(j − 1) ≥ 1, and the first mover is the same member f in every window. Then the split state of a window with value c′
  is (f on c′, the other on 1 − c′): both orientations occur, and both together states occur (Φ = 0 at the end of each window). ∎
- Note: L-SI 41's lane lemma DBL-EQ (claude/l-si, docs/si/N5-TROPICAL-box76.md §7) states (E1)-(E5) from WINDOW-DOUBLE («signed, not
  landed»); this proof uses only ALIGN, so DOUBLE-EQ′ is a premise-light version of it (for the referees: compare, do not merge).
- DATA (fwcheck.py): 0 violations on 124,705 all-start runs of the 240 𝓛^R genomes under L-NEW's box150-199 (claude/l-new 73b3d1fd,
  9,650 doubling levels), on 964,608 all-start runs of 1,500 random hypothesis-rich genomes (8,079 doubling levels), and on the
  l3/kill/ and l4/rec/ records. FROZEN-WINDOW (a)'s hypothesis (levels l, l + 1 doubling, pair l + 1 targeting pair l) holds once in
  the corpus (REC_d10_tower, l = 2; counter dd_tg); (b)'s hypothesis never (fw_hyp 0 on 1.28M runs of d 3 genomes as well): (b) is a
  theorem without a machine instance, as expected if it is the obstruction.

## 4. Lemma FROZEN-WINDOW (PROVED, lane; §2, §3, the movement rule) and its corollaries
- Hypotheses: G ∈ 𝓛^R_d, 1 ≤ l, any run; levels l and l + 1 doubling; each member x of pair l + 1 has {xt(x, 0), xt(x, 1)} = {2l, 2l + 1}.
- Claim. (a) D_l is not constant on the states s_0, …, s_(t₁−1) before the first move of pair l. (b) If also l + 2 ≤ d − 1 and level
  l + 2 is doubling: for every stretch of states s_t, …, s_(t′−1) between consecutive moves t < t′ of pair l (and the final stretch
  s_t, …, s_T), D_l is not constant on it. In particular no state of the run is a frozen state of pair l.
- Proof. If D_l is constant on a stretch, then for x in pair l + 1 the value difference of its two options, ±D_l + ε(x, 0) − ε(x, 1), is
  constant there, so «the other option is strictly better» has one truth value on the whole stretch. By (E3) at level l the (l + 1)-b-
  steps are exactly the moves of pair l, so a stretch s_t … s_(t′−1) is an (l + 1)-window [t, t′ − 1] (resp. [1, t₁ − 1]). If x moves at a
  step u of the window other than its first step, it did not move earlier in the window (E4), its other option is strictly better under
  s_(u−1), hence under the first state of the stretch, and c_(l+1) is constant on the window: so x already moves at the first step after
  the stretch begins (step t + 1, resp. step 1). (a): Φ_(l+1)(0) = 2 and Φ_(l+1)(t₁ − 1) = 0 (E1, E2), so both members move in
  [1, t₁ − 1] (t₁ ≥ 2, since Φ(0) = 2 ≠ 0), both at step 1, against (E3). (b): both members move in the window (E4), at most one at the
  b-step t, so one moves at t and the other at t + 1 (t + 1 < t′, else both move at t, against (E3)). By (E3) at level l + 1 the
  (l + 2)-b-steps include t and t + 1, so [t, t] is an (l + 2)-window with one step, in which both members of pair l + 2 must move (E4)
  at distinct steps (E3): impossible. ∎
- Corollary NO-CROSS / NO-PARALLEL (PROVED, lane). Under the hypotheses of (b), pair l is neither CROSS nor PARALLEL (a split and a
  together state occur in every doubling run: (E1)-(E4)). If moreover F(l − 1) ≥ 1, all four states occur (E5), so no state is frozen:
  {xt(p, 0), xt(p, 1)} ∩ {xt(q, 0), xt(q, 1)} = ∅ (X counted as an element), and since a member whose two options share a Ξ-target
  has a constant preference and moves at most once (F(l − 1) + 1 ≥ 2 moves are needed, E4), pair l uses four distinct Ξ-targets, at
  most one of them X: at least one Ξ-target of pair l lies outside pair l − 1.
- What it kills (DEAD as a design, by the theorem; instances in §5): the explicit recursion «G_h := G_(h−1) plus one level crossed onto
  the top pair» (the TOWER-NEED-natural choice: L-SI 41, docs/si/N5-TROPICAL-box76.md §8, lane): a fully crossed tower has at most two
  consecutive doubling levels above any CROSS pair that the next pair targets. In REC_d10_tower the pair 3 is CROSS and mover 8
  targets it: the lemma says levels 3, 4, 5 cannot all double there (and level 4 does not: F(4) = 23). Every further doubling level
  of a targeted tower needs a pair whose two members keep Ξ-differences alive inside every window: a D-event (a rise of a current
  Ξ-target of pair l) at a step that moves no member of pair l, in every (l + 1)-window.
- Does NOT claim: that towers stop (the lemma allows towers whose pairs have four distinct targets); any bound on S(h) or T.

## 5. DATA: searches for the fifth doubling level (h = 5: F = 2, 6, 14, 30, 62 on levels 0-4)
- Real model (rclimb.c, own simulator, same rules as l3/sim.py; records re-run by l3/sim.py and L-NEW's box150 Gen via l3/xcheck.py:
  SIM-MISMATCH 0, movescheck counters 0):
  - unconstrained climb from REC_d10_tower + 4 TOP-ADD levels (d 14): F(4) = 52 (T 73, F 2 5 12 26 52 39 21 8 6 2 2 2 3 0;
    rec/RECF4_d14_F52.json, sha1 1e0b0a58…); after 2 more TOP-ADD levels (d 16): F(4) = 53 (T 73, F 2 5 12 26 53 40 25 18 16 2 3 3 4 3
    4 3; rec/RECF4_d16_F53.json, sha1 9b08c289…). CANDIDATE records (previous best F(4) = 46, RECT_d14_F46). Levels 2 and 3 are
    doubling (12 = 2·5 + 2, 26 = 2·12 + 2), level 4 is one short (53 = 2·26 + 1), level 1 is one short (5 = 2·2 + 1). Their tower pairs
    are not CROSS: pair 2 = (4: 26, 16; 5: 19, 12), pair 3 = (6: 14, 4; 7: 10, 11), pair 4 = (8: 6, 7; 9: 7, 8) — the shape §4 permits.
  - forced crossed pair 4 (9 → (6, 7), 4's option re-pointed; NOMUT 6-9; three annealing schedules, 2·10^8 proposals): F(4) ≤ 34.
  - forced CROSS pair 2 under a targeting pair 3 (seedCR2): F 2 4 10 20 …: level 3 stays below doubling (CR2_d10.json).
- Relaxation (drv.c, EB = 2, block of the d 14 tower): climbs reach Fmax₂ F(4) = 30 (below the real 52 found by the real climb; the
  relaxed climb is a weaker search, not a cap).
- Fully crossed driven blocks, e free (exact LP over all starts): uniform period-1 templates (all 12,288 per m, tmpl.c): LP 5, 9, 12,
  16, 20, 25, 30 for m = 2..8 (≈ 4 per level); climbs: 14, 18, 26, 31, 34 for m = 4..8. One active mover per level with frozen partner
  (KM-type fuel chain, HALF): LP 5, 7, 10, 12 for m = 3..6. Free single improving switches (no keys; climbed acyclic genomes): 10, 26, 60 for
  4, 6, 8 movers. Reading: the exponential capacity of the Ξ-side is cut to linear by the key coupling, even with a free key source.

## 6. The obstruction for the explicit recursion, and what S(5) needs (READING, with the proved parts named)
- PROVED parts: F0 is not binding (§1 DATA on the records; DRV-RELAX); a targeted CROSS or PARALLEL pair cannot sit under two more
  doubling levels (§4); every pair of a targeted doubling tower (except the top two) needs four distinct Ξ-targets and a fresh Ξ-event
  inside every window of the level above (§4 (b)).
- So the constraint that kills «add one crossed level per step» is not R113 F0 / PAIR-DOUBLE (both allow it), nor R110 ISO / W-ONLY
  (not used), but the AND-gate timing at three consecutive doubling levels: a frozen Ξ-difference forces the second follower one step
  after the first (§4 proof), and a one-step window cannot be doubled. Instance of the failure: REC_d10_tower levels 3-4 (CROSS pair 3,
  F(4) = 23); the forced-cross climbs (F(4) ≤ 34).
- What a recursive G_h must have instead: each tower pair l ≤ h − 2 with four distinct Ξ-targets, one of them outside pair l − 1 (§4),
  whose value rises at steps that move no member of pair l, once per (l + 1)-window, i.e. ≈ F(l) ≈ 2^(l+2) such rises. Those rises are
  the «fuel» of FUEL-NEED (L-SI, lane), now located per window. The records RECF4_d14_F52 / d16_F53 have this shape (pairs 2, 3 with
  four distinct targets) and get to 52-53, short of 62.
- OPEN: whether a fuel target outside pair l − 1 can rise once per window for h levels with O(h) or O(h²) extra movers (polynomial S(h),
  exponential T^R) or needs a block that itself is a tower (compounding, polynomial T^R). No conjecture added.

## 7. Files (experiments/lower/l4/; outputs in out/, gitignored; records in rec/)
- drv.c (driven block: exact LP / Fmax with EB, all starts or STARTONLY, climbs; CROSS, HALF, ACYC, FREE modes), drvpy.py, drvpath.py
  (Python twins), blk.py (𝓛^R_d JSON → block), tmpl.c (uniform crossed templates), rclimb.c (structured real-model climb: FIX, NOMUT,
  LV, ANNEAL), j2t.py, fwcheck.py (DOUBLE-EQ′, FROZEN-WINDOW, STEP-ADJ counters), l4check.py (fast regression, run by
  experiments/lower/check.sh).
- Commands: `gcc -O2 -o $SP/drv drv.c -lm`; `EB=2 OBJL=3 STARTONLY=1 SEED=x.gen $SP/drv 0 0 1` (Fmax₂ F(4) of a block);
  `gcc -O2 -o $SP/rclimb rclimb.c -lm`; `LV=4 ANNEAL=0.15 OUT=o.txt $SP/rclimb in.txt SEED ITERS`; `$SP/tmpl 2 8`.

## 8. Diff against TARGET.md
No statement mentions a parity game, a winning region, an algorithm's running time or a complexity class; each is about the IDEAL
model's step sequence (R104's definition) on 𝓛^R_d. §1 bounds T by another exponential-size quantity; §3-§4 constrain doubling runs;
nothing is polynomial. Not M3, not a gauntlet step. G-N5-TIME stays OPEN; MOVES-2D stays OPEN (its constant 2d is DEAD, L3 §9).
