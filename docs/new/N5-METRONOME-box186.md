# Box 186 N5-METRONOME: the segment lemma «a metronome is at most 2 × its lower pair's moves + O(1)» is DEAD as stated (pass_d4_D4: a level-3 mover moves at 4 consecutive steps while the lower pair never moves; every key flip is passed through from below and its Ξ-targets are movers 0 and 2). PROVED (lane) SEG-WINDOW: a metronome segment of length D at level l forces D − 1 flips of the pair below inside it, so D ≤ 3 + 2·F_seg(l − 2) and D ≤ 1 + #(segment steps moving some mover below l). Iterated, these give 2^l (LEVEL-PRODUCT), not O(l), and the exact d 4 maximum is a halving tower (7 / 4 + 3 / 2 + 1 / 1 + 1 moves), which the key side allows at every level. No brake stated without T.
L-NEW successor 57, 2026-11-06 (from 19:5xZ by date -u; see the commits). Lead brief BOX 186 (19:52Z): a brake on metronomes not stated
through T. (1) Bound a metronome segment by the lower pair's own moves, e.g. segment ≤ 2·(moves of the lower pair in the segment) +
O(1); (2) iterate down the levels: O(l) or LEVEL-PRODUCT? Prove the segment lemma lane-level, or give the instance where a metronome
outruns its lower pair. Tools: L-RED R208 TOP-SPLIT (lane), RESULTS R111, R113. Premises: R104 definition, R105 ENC / MONO / LOCAL,
R110 definition of 𝓛^R_d, R111 CASCADE, R113 ALIGN; box 185 AND-GATE (lane). Labels: PROVED (lane, unrefereed) / DATA / CONJECTURE /
DEAD / READING. Not a TARGET.md claim. G-N5-TIME stays OPEN.

Notation (𝓛^R_d, level l ≥ 1): x a mover of level l; u := 2l − 2, w := 2l − 1 (the lower pair); a METRONOME SEGMENT of x is a set
[a, b] of consecutive steps each of which moves x, D := b − a + 1; for a set W of steps and a level j, F_W(j) := #{t ∈ W : the pair
(2j, 2j + 1) flips at t}; LM := Σ_(t ∈ [a, b]) #(Mv_t ∩ {u, w}) (the lower pair's moves in the segment), LS := #{t ∈ [a, b] : Mv_t ∩ {u, w}
≠ ∅}.

## 0. Answer
- (1) DEAD as stated: «D ≤ 2·LM + O(1)» fails, and the excess grows with d in the data.
  - pass_d3_D3 (experiments/new/box186/out/pass_d3_D3.json, sha1 8bca9764…; text form pass_d3_D3.txt): d 3, start 110100, mover 5
    (level 2) moves at steps 1, 2, 3 (D 3) and the lower pair (2, 3) never moves (LM 0). Ξ-targets of 5: (5, 0) → 4 (its partner),
    (5, 1) → 0 (level 0). Its key flips come from the level-0 moves at steps 2 and 3, passed through level 1.
  - pass_d4_D4 (out/pass_d4_D4.json, sha1 3bf6a4a4…; pass_d4_D4.txt): d 4, start 01010111, mover 7 (level 3) moves at steps 1-4 (D 4),
    and the lower pair (4, 5) never moves (LM 0, LS 0; moves per mover 1 1 1 2 0 0 1 4; F = 1, 3, 3, 0). The pair (4, 5) flips at steps 2,
    3, 4, all pass-throughs (it sits in a D-state, Φ = 1, while (2, 3) flips below it). The Ξ-preference flips are fed by movers 0, 6, 2 on
    the chains of 7's options (Ξ-targets 0 and 2: no option of 7 points into the lower pair).
  - Both are verified on L-NEW's own simulator (box150/check.py Gen, via box185/trace.py and flips.py) and on dense.c. DATA, max of D −
    2·LM over all starts: corpus (214 genomes, d 1-8) ≤ 3; climbs on D − 2·LM: d 3: 3, d 4: 4, d 5: 5 (out/pass_d5_D5.txt: mover 9,
    level 4, D 5, LM 0), d 6: 5 (climb stopped). So far the excess equals d: a pure pass-through metronome of length d at the top (§3).
  - So a metronome does not need its lower pair: its two inputs (a key flip and a Ξ-preference flip at every step) can both come from
    any level below, through pass-through on the key side and through chains on the Ξ side.
- (1′) PROVED (lane) Lemma SEG-WINDOW, the corrected segment lemma (§1). For a metronome segment [a, b] of x at level l ≥ 1:
  - (a) the pair (u, w) flips at every step of [a + 1, b], so D − 1 ≤ F_[a+1,b](l − 1);
  - (b) D ≤ 1 + LS + PT ≤ 1 + #{t ∈ [a + 1, b] : some mover of level < l moves at t}, with PT the pass-through steps (the pair (u, w)
    flips with no move of u or w; there the pair l − 2 flips and Φ = 1);
  - (c) for l ≥ 2: D ≤ 3 + 2·F_[a+1,b](l − 2) (R113's PAIR-DOUBLE argument on a window);
  - (d) BURST-2: on any window in which the pair l − 2 does not flip, the pair l − 1 flips at most twice. So a segment contains a flip of
    the pair two levels down in every 3 consecutive inner steps but at most 2.
  - (e) the Ξ side: at every step t ∈ [a, b − 1] the Ξ-preference of x flips, and some mover on the chain under s_(t−1) of the option x
    takes at t + 1 moves at t (R105 LOCAL: a value changes only through a move on its chain).
- NEW RECORD for MOVES at d 5 (ADDENDUM, 2026-11-06 ~21:0xZ): out/dense_d5_D9.json (sha1 5619d2bd…; text dense_d5_D9.txt), start
  0101111000: mover 9 (level 4, a Ξ-target) moves at EVERY step 1-9 of a 9-step run (moves 9; L-RED's previous best at d 5: 8; 2d = 10;
  a kill needs 11). Cross-wired (xt(9, 0) = 7, xt(9, 1) = 6); per-mover moves 1 1 1 2 2 1 4 5 1 9; F = 1, 2, 4, 9, 3: a halving tower
  (9 / 4 + 5 / 2 + 1 / 1 + 2 / 1 + 1). Found by dense.c SCORE=D from box185/out/h_d5_L4_ld6.txt; checked on box150 Gen (trace.py,
  flips.py). Seed for R214's DENSE(5, 4, 11).
- (2) Iterating gives LEVEL-PRODUCT, not O(l). With (c), D_l ≤ 3 + 2·F(l − 2) and F(j) ≤ 2F(j − 1) + 2: the iterate is 2^l-type, the
  key-side bound already known (R113 MOVES). The segment lemma, even in the Lead's form, only moves the question to the lower pair's
  moves inside the segment, and in the exact maxima those are half-dense themselves:
  - DATA, the exact d 4 maximum m4_z6_r7 (L-RED R213, start 01110010) is a HALVING TOWER: per-level moves 1 + 1 (level 0), 1 + 2
    (level 1), 4 + 3 (level 2: they alternate, each moving every other step), 7 (level 3: every step). So level l − k moves about D / 2^k
    times per mover, the binary-counter profile that PAIR-DOUBLE allows at full tightness.
  - A halving tower of height d at d 5 would have a top metronome of length 15 > 2d: that is the DENSE(5, l, 11) query now at L-RED R214.
    Nothing on the key side forbids it (PAIR-DOUBLE is tight with every level doubling). So if MOVES-2D is true, its brake is a Ξ-side
    cap on how dense a whole tower can be, and it has to say why the Ξ-preference flips of all the tower's movers cannot all be fed. I
    have no statement of that brake that avoids T.
- READING (TOP-SPLIT). L-RED R208's TOP-SPLIT splits a run at the top moves: between two top moves the lower part is a run of a (d −
  1)-level genome. For a metronome at the top every step is a top move, so every segment of TOP-SPLIT is one step long and the lemma is
  vacuous; it measures re-arming between top moves, the opposite regime.

## 1. Lemma SEG-WINDOW (PROVED, lane)
- Hypotheses: G ∈ 𝓛^R_d (R110); x of level l ≥ 1; a run; [a, b] a metronome segment of x (x ∈ Mv_t for every t ∈ [a, b]).
- (a) For t ∈ [a + 1, b], x moves at t − 1 and at t. By box 185 AND-GATE (b), KP(x) changes at step t (its window [t − 1 + 1, t] is the single
  step t). By R113 ALIGN (a), KP_s(x) = c_l(s), which changes exactly when the pair (u, w) flips. So (u, w) flips at every t ∈ [a + 1, b],
  and D − 1 ≤ F_[a+1,b](l − 1).
- (b) R113 §4 («Claim: if (p, q) flips at step t and Mv_t ∩ {p, q} = ∅, then t is a b-step and Φ(t − 1) = 1», applied at level l − 1 for
  l ≥ 2; at l = 1 the pair (0, 1) flips only at a step moving 0 or 1, R113 F0's proof): each flip of (u, w) is at a step moving u or w or at a
  pass-through step. A pass-through step has a flip of the pair l − 2 at the same step; by R111 CASCADE (its root move lies at a level
  below) or directly by induction on this claim down to level 0, every such step moves some mover of level < l − 1. So D − 1 ≤ LS + PT ≤
  #{t ∈ [a + 1, b] : some mover of level < l moves at t}.
- (c) R113 PAIR-DOUBLE's proof is a sum over steps of Φ(t) − Φ(t − 1); summed over the window [a + 1, b] instead of [1, T], with Φ(a) ≤ 2 and
  Φ(b) ≥ 0, it gives F_[a+1,b](l − 1) ≤ 2 + 2·F_[a+1,b](l − 2) (for l − 1 ≥ 1). With (a): D ≤ 3 + 2·F_[a+1,b](l − 2).
- (d) If the pair l − 2 does not flip on a window W, then c_(l−1) is constant on W, so Φ (for the pair l − 1) never increases on W, every
  flip of the pair l − 1 on W is at a step moving it (claim of (b)), and each such step lowers Φ by at least 1; Φ ≤ 2. ∎
- (e) By AND-GATE (b) the Ξ-preference changes at the single step t of the window [t, t + 1 − 1], and by AND-GATE (c) the value of the
  newly preferred option rises strictly at t; by R105 LOCAL it depends only on the states on its chain, so a mover on that chain (under
  s_(t−1)) moves at t. ∎
- Does NOT claim: any bound on D polynomial in l; that the movers of (b) or (e) are the lower pair.

## 2. What (2) would need (READING)
- In the d 4 halving tower every level's pair flips at nearly every step and every level's movers are Ξ-renewed at their own period.
  A brake must count Ξ-renewals of a whole tower: each move of a level-j mover needs a value rise on its chain (AND-GATE (c)), and those
  rises come from moves of movers on chains, which are themselves tower movers. In the d 4 tower the chains point UP as well as down
  (m4_z6_r7, Ξ-targets of options 0 and 1 per mover: 0 → 6, 1; 1 → 5, 4; 2 → 7, X; 3 → X, 7; 4 → 3, 2; 5 → 2, 3; 6 → 5, 4; 7 → X, X), so the top metronome renews the lower levels and the lower
  levels renew the top. A brake would have to exclude such a two-way renewal loop of length 2^l; acyclicity of the Ξ-graph is the only
  constraint on it in the model, and the loop above is acyclic.

## 3. DATA and tools (experiments/new/box186/)
- dense.c (from box185/mv.c): per start and mover, the longest metronome segment from the start, LM and LS inside it; reports max D −
  2·LM, the D and D − 2·LS of that segment, and max D over Ξ-targets; climbs with score D − 2·LM (default) or D (SCORE=D).
- log/corpus_dense.txt: 214 corpus genomes, every start: max D − 2·LM by d: 1 (d 2), 2 (d 3-7), 3 (d 8, seedpm_rk_D2_k2_d8_s1).
- Climbs (log/x_m*.txt; m = d − 1): d 3: 3 (pass_d3_D3), d 4: 4 (pass_d4_D4), d 5: 5 (pass_d5_D5), d 6: 5 (stopped); SCORE=D at d 5 from
  box185/out/h_d5_L4_ld6.txt (start value 7): 9 (dense_d5_D9, log/D_d5_seed.txt).
