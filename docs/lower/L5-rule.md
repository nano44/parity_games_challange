# L5: the inductive rule G_h → G_(h+1), or the obstruction to one (L-LOWER successor 5, BOX L5)

Box: Lead brief (L-LOWER successor 5, D1 / D14 / D18), BOX L5 «find the INDUCTIVE RULE, or the obstruction to one»; GO 2026-11-07
09:42Z. Written from 09:50Z (date -u). Labels: PROVED (lane, unrefereed) / CONJECTURE / DATA / DEAD / READING. Every DATA clause names
its counter (unit, set, scope). Nothing here is a result in the sense of CLAUDE.md; G-N5-TIME stays OPEN. Not a TARGET.md claim (§9).

## 0. Premises, notation, tools
- Premises as in docs/lower/L4-tower.md §0 (landed: R104 definition, R105 ENC / MONO, R110 definition of 𝓛^R_d, R113 ALIGN, F0,
  PAIR-DOUBLE; lane: DOUBLE-EQ′, FROZEN-WINDOW, LATE-PREF / FUEL-PER-WINDOW). L-SI 42's lane lemmas PULSE-NEST, CAP-PULSE, ZONE,
  INSERT-PASS, STRETCH-NEED (claude/l-si 9b51f2cb docs/si/N5-TOWER-box80.md §1-§3) and TOWER-NEED / FUEL-NEED / PASS-FREEZE
  (docs/si/N5-TROPICAL-box76.md §8-§10) are used only as constraints for the design and are named where used (lane, unrefereed).
- Capped: level l has F(l) = 2^(l+2) − 2 (R113 T-BOUND's per-level cap); «h capped» = levels 0, …, h − 1 capped. Doubling: F(l) =
  2F(l − 1) + 2. j-window, u₁ < u₂, x₂, f (first mover), PULSE as in L4 §3 / L-SI box 80 §0.
- Tools (experiments/lower/l5/): fev.c (batch evaluator; simulator core copied verbatim from l4/rclimb.c), revert.py (unit reverts),
  fuelsrc.py (fuel source per window vs b-step type), utmpl.c (uniform level templates; its own exact-order simulator, GENOME= self-check
  mode), mclimb.c (rclimb.c + edit-distance penalty). Cross-check (DATA; unit = genome; set = H5_lift, H6, G7_best_d28 and the 270
  revert genomes of §1; scope = stored start): utmpl's exact-order simulator = fev (__int128) on all 273, T and F identical.

## 1. Step 1: H5 → H6 dissected
- Not an operation under the ladder symmetries (DATA; unit = level; set = levels 0-23 of rec/H5_lift_d24.txt vs rec/H6_d24_F126.txt):
  the multiset of target levels of the four options differs at 23 of 24 levels (per-level table: revert.py companion, §8). A relabelling
  (swap of the two members of a pair, with the induced option swap one level up), a substitution or a block insertion would preserve
  these multisets up to a shift; none does. L4 §5: Ξ-targets changed 89 of 96, rank-order LCS 17 of 96.
- Forced vs drift (DATA, revert.py → revert_H5lift_H6.out; unit = one changed part of H6 set back to its H5_lift value, all else H6;
  set = all 246 changed single parts: Ξ-target / parity / rank (by a swap inside the rank permutation) per option, gate order and start per
  mover, plus 24 whole-level blocks; scope = stored start):
  | revert of | neutral (6 capped kept) | cyclic | < 3 capped, but ≥ 3 consecutive doubling levels survive | collapse (neither) | 3-5 capped |
  | --- | --- | --- | --- | --- | --- |
  | Ξ-target (89) | 16 | 30 | 20 | 22 | 1 |
  | rank (96) | 52 | 0 | 11 | 32 | 1 |
  | parity (42) | 29 | 0 | 2 | 11 | 0 |
  | start (19) | 10 | 0 | 1 | 8 | 0 |
  | level block (24) | 0 | 17 | 3 | 4 | 0 |
  So about 43 % of the single-part differences (107 of 246; 52 of the 96 rank changes) are drift in this one-at-a-time sense, and 73 % of the Ξ-target
  changes that keep the graph acyclic are forced (43 of 59). A frequent failure is not a top-level loss but «bottom fails»: F(0) = 0 and
  a tower 2, 6, 14, 30, 62 restarts one level higher (e.g. x0's Ξ-target revert: F 0 2 6 14 30 62 47 17). The level-0 key source of H6
  is fed by the top of the genome (0 → 42 (level 21), 1 → 39 (level 19)): a closed loop, as ZONE / RE-ENTRY say (L-SI 42: every Z_j is
  the whole genome).
- Minimal-edit climb (§6; running): least edits from H5_lift to six capped levels.

## 2. The fuel schedule: a function of the opening b-step (DATA) — not a ruler sequence (DEAD)
- DEAD (as a description of the records): «the fuel source of the j-window number i is a function of v₂(i) (ruler / Towers-of-Hanoi
  sequence)». Instances: H5_d20_F62 j = 3 (v₂ = 0 windows fed by {18, 19} and {19}); H6_d24_F126 j = 3 (v₂ = 0 windows fed by 23 and
  by 24). Counter: ruler.py-type test (unit = j-window; set = doubling levels j with j + 1 doubling; scope = stored start of H5, H6, DBL4,
  RECF4_d20_F60).
- DATA (fuelsrc.py → fuelsrc.out; same unit / set / scope): the feeder set of a j-window (movers on x₂'s chains that move at u₂ − 1, the
  lpaudit.py rule) is a FUNCTION of the TYPE of the window's opening b-step := (the member of pair j − 1 that moved, its new option): at
  every doubling level of H6 (j = 1-4), DBL4 (j = 1-3) and RECF4_d20_F60 (j = 1, 2), and at H5 j = 1, 2; H5 j = 3 fails in one window
  (type (5, 0): feeders 14 in three windows, 35 in one). x₂'s new option is itself a function of the moving member (it alternates).
  Hence: the parity alternation (pre-go DATA) = the alternation of the two members of pair j − 1 at the b-steps (DOUBLE-EQ′ (E3)-(E5));
  the period-4 pattern at H6 j = 3 = the four types (member × direction): b-steps of member 4 to 0 → feeder 23, to 1 → feeder 24;
  of member 5 (either direction) → feeder 19. A new feeder is spliced in by splitting one type by its direction.
- READING: the fuel is triggered by the b-step itself (L-SI 42's delay lines: «x₂ ← z ← … ← member of pair j − 1»), so a recursive rule
  must provide, per level, one delay line per b-step type, of length ≥ PULSE_j − 1 ≥ h − j − 1 (CAP-PULSE).

## 3. Step 2: structures from neighbouring fields (what each needs; the cheapest tested)
- (a) Ruler / Hanoi fuel schedule: needs the fuel source to be indexed by v₂(window). Tested first (cheapest, on existing records):
  DEAD as a description (§2). The time structure of a capped run IS the Hanoi recursion (PULSE-NEST: each j-pulse contains a whole
  (j + 1)-window; the run is a depth-first traversal of a complete binary tree), but the fuel identity follows the b-step type, i.e. the
  parent's last move, not the depth v₂.
- (b) Call/return (visibly pushdown) reading of PULSE-NEST: the f-move of pair j «calls» level j + 1, the x₂-move of pair j «returns»;
  a tight tower (PULSE_j = h − j) returns level j one step after level j + 1 returns. Needs x₂_j's preference to flip exactly when x₂_(j+1)
  lands, and only in windows of the right key (§7 READING: the Ξ-order cannot route one trigger to two racers by window parity
  without a mover that copies f_j).
- (c) Uniform templates = substitution systems of period P (a 1-dimensional cellular «L-system» on the level axis): the same local
  wiring, ranks, parities, gates and start at every level (mod P). Needs only O(1) parameters per level: S(h) = O(h) if it works.
  Tested (§4).
- (d) Friedmann's binary-counter games (strategy iteration lower bounds): NOT opened in this box; no statement uses them.

## 4. Uniform level templates (DATA; the search is over rules, not genomes)
- utmpl.c: for every level l ≥ 1 (mod P), member q, option k: Ξ-target X or 2(l + δ) + q′ with δ ∈ [−DM, DP] (out of range → X); parity;
  rank key l·S·8 + off (S = ±1, so ranks increase or decrease with the level, interleaved by the offsets); gate order per member; start
  bit per member (alternating with the level parity or not); level 0 separately. G_d := the template on d levels. Score: Σ over d ∈ {6, 8,
  10, 12} of 1000·(capped levels) (run A) or 1000·(longest run of doubling levels) (run B) + partial credit.
- Run A (P = 1; DM/DP = 1/2, 2/3, 2/6, 3/8; 100,000 hill-climb steps × 200 restarts each; unit = template; scope = stored start): best
  F = 0 2 4 6 … 2(d − 1) for every d (T = 2d − 2): linear, no doubling level beyond l = 1, no capped level (F(0) = 0).
- Run B (P = 1, 2, 3; DM/DP 2/4, 3/6, 3/8; 100,000 steps × 300 restarts, all six configurations completed; unit = template; scope =
  stored start; logs out/r_p*): best score 4,659 of a possible ≥ 8,000, i.e. ONE doubling level per d
  (e.g. P = 2: F = 0 1 4 3 4 5 8 7 8 9 12 11 at d 12; P = 3: F = 0 1 2 6 3 6 4 1 2 6 3 5): never two consecutive doubling levels, while
  non-uniform genomes have 2-3 consecutive doubling levels already at d ≤ 10 (REC_d10_tower, L4 §5). DATA, not a proof: a heuristic
  search over a restricted rule space (rank keys monotone in the level, radius ≤ 8). READING: a local periodic rule does not even
  produce two consecutive doubling levels; with STRETCH-NEED (pulses must grow like h − j at fixed j) and §2 (fuel triggered per b-step
  type), a working rule must be non-uniform in the level (pulse length depends on the distance to the top). DEAD as stated for this
  space: «a uniform period-≤3, radius-≤8 template with level-monotone ranks gives ≥ 2 consecutive doubling levels at d ≤ 12» (none found
  in the searched sample; CANDIDATE-DEAD until an exhaustive check, which is out of reach at ~10^10 templates).

## 5. Lemma GAP-NEST (PROVED, lane; DOUBLE-EQ′ (E3), (E4) and L-SI 42's PULSE-NEST) and the forced part of H5 → H6
- Hypotheses: G ∈ 𝓛^R_d, any run, j ≥ 1, k ≥ 1, j + k ≤ d − 1, levels j, …, j + k doubling; W, W⁺ consecutive j-windows.
- Claim: GAP(W) := u₁(W⁺) − u₂(W) ≥ k + 1 (and PULSE(W) := u₂(W) − u₁(W) ≥ k + 1 by PULSE-NEST), so u₁(W⁺) − u₁(W) ≥ 2(k + 1). With h
  capped levels: PULSE and GAP of every j-window (1 ≤ j ≤ h − 2) are ≥ h − j.
- Proof. By (E3) at level j the (j + 1)-b-steps are exactly the moves of pair j, so [u₂(W), u₁(W⁺) − 1] is a (j + 1)-window (it starts
  at a move of pair j, and the next move of pair j is u₁(W⁺)). Levels j + 1, …, j + k are doubling, so by PULSE-NEST (base j + 1, with
  k − 1 further doubling levels) its two pair-(j + 1) moves are ≥ k steps apart, and both lie in the window, so its length u₁(W⁺) − u₂(W)
  is ≥ k + 1. Sum with PULSE. ∎
- DATA (slack.py → slack7.out; unit = j-window; set = levels 1-5; scope = stored start; target H = 7): violations of PULSE ≥ 7 − j or
  GAP ≥ 7 − j: H6_d24_F126: 87 (level 4: 15 pulses of the types (7, 0), (7, 1); level 5: 63 pulses of all four types + 9 gaps);
  G7_best_d28 (L-LOWER 4's warm start, F(6) = 222): 31, all at level 5, all in ONE b-step type (9, 1) (15 pulses and 14 gaps of length
  1, plus the first window). The climb H6 → G7_best repaired the pulse/gap deficits type by type; one type is left.
- Greedy walk back (greedyback.py → greedyback.out; unit = single changed part; set = the 249 differences H6 vs H5_lift; 4 random
  orders; a revert is kept iff 6 capped levels survive): 118-122 reverts kept, 127-131 differences remain in every order, among them 70-72
  Ξ-targets, the same set up to 2 elements in all four orders, touching every level 0-23 (e.g. 0:0 25→42, 0:1 10→3, 2:0 23→40, 4:0 16→6,
  9:0 6→14, 10:0 8→11). So about half of the H5 → H6 difference is drift; the other half is locally forced and global (no level is
  untouched), as ZONE / STRETCH-NEED predict (L-SI 42: every Z_j of H5, H6 is the whole genome).

## 6. The obstruction instance for the seventh level: one delay line (DATA; the exact place)
- G7_best_d28 (rec/G7_best_d28.txt, L-LOWER 4; levels 0-5 capped, F(6) = 222 < 254): level 6 has 127 windows; 79 have the two moves
  DOUBLE-EQ′ needs, 48 fail (winfail_G7_l6.out; unit = 6-window; scope = stored start), periodically: in every block of 8 windows the
  three windows opened by the pair-5 moves after a level-5 window of type (9, 1) (types (11, 1): 1 step, only q moves; (10, 1): 1-2
  steps, no move; (11, 0): only p moves).
- Cause (pulses_G7_l5.out; unit = 5-window; scope = stored start): pair 5's PULSE is 2 in the 47 windows of the types (8, 0), (8, 1),
  (9, 0) and 1 in the 15 windows of type (9, 1) (+ the first window); in type (9, 1) the second mover 10 is triggered by mover 15 alone
  (10 → 30 → 15), and 15 is KEY-GATED by the same flip: in the window at steps 20-22 (9 → 1 at 20), 15 prefers its other option from
  step 19 but moves only at 21, when c_7 = o_6 changes: at 21 the first mover of pair 6 (13) moves, in the same step as the first mover
  of pair 5 (11); 10 follows at 22. The trigger is keyed by the FIRST move of pair 6, which comes at u₁ itself, so the line has length 1.
  READING (self-consistency): a trigger keyed by pair 6's SECOND move would give u₂ ≥ u₂(6-window) + 1, but the 6-window [u₁, u₂ − 1]
  has length 1, so pair 6 cannot make its second move there; the failure of level 6 and the short level-5 pulse sustain each other,
  which is consistent with the plateau (no single change improves F(6)).
- What the seventh level needs here (from PULSE-NEST, GAP-NEST, DOUBLE-EQ′; exact): a trigger for 10 in the type-(9, 1) windows that
  fires at u₁ + 1 or later (pulse ≥ 2) and a gap ≥ 2 after it, without shortening the other three types below 2. Every other pulse/gap
  condition for 7 capped levels already holds in G7_best (slack7.out, levels 1-4: 0 violations).
- Splice search (splice.py; unit = genome; 4,000 + 3 × 30,000 random single-mover splices: the option (30, 0) → 15 or (10, 1) → 30
  re-pointed through one re-initialised mover w (new top movers or idle movers 28, 29, 32, 45, 50, 55-59 of the d 30 lift), w's other
  data random; scope = stored start): no splice raises F(6) above 222 while keeping 6 capped levels. DATA (negative), not a cap: the
  splice mover needs a key clock that lags the first mover of pair 5 by one step in exactly the type-(9, 1) windows.

## 7. Summary: rule, obstruction, conjecture (labels as stated)
- No inductive rule G_h → G_(h+1) was found. What a rule must do is now specific (PROVED parts: GAP-NEST, PULSE-NEST, DOUBLE-EQ′; DATA:
  §2, §5, §6): for every level j ≤ h − 1 and each of the four b-step types (member of pair j − 1 × direction), the second mover of pair j
  needs a trigger line whose delay grows by one per extension (PULSE and GAP ≥ h − j), so an extension must lengthen Θ(h) lines (the
  zero-slack ones: all four types at j = h − 1, h − 2 in H6). The records realise this type by type (H6 → G7_best: 87 → 31 deficits, one
  type left), never by a uniform local rule (§4), and never without touching every level (§5).
- The obstruction located (DATA, instance G7_best_d28, type (9, 1) at level 5): a trigger line cannot be lengthened by a mover whose key
  clock is the flip it is supposed to delay; the delay mover must sit at a level whose key flips one step AFTER the first mover of the
  pair, in exactly the windows of one type. The search space of single splices did not contain one (§6).
- READING (not proved; the routing problem behind §3 (b)): in a window with key c, x₂_j must see the trigger as a rise of its option-c
  racer; option values only rise (R105 MONO), a single comparison sees the larger of the two racers' top β's, and the only movers whose
  state equals c in every window are f_j and x₂_j itself. So a per-type trigger must reach x₂_j through f_j's current option, or through a
  copy of f_j, i.e. one more mover with its own racers per type: the per-level cost is O(1) movers per type if keys allow, which would give
  S(h) = O(h) to O(h²).
- CONJECTURE (L5-TYPE): a capped tower of height h + 1 can be obtained from one of height h by adding O(h) movers, one delay mover per
  (zero-slack level, b-step type), at levels whose key clock lags the pair below by one step. Evidence: the type-by-type repair H6 →
  G7_best (DATA) and the fuel-type function (§2, DATA on H6, DBL4, RECF4, G7_best). Against: §6 (no single splice found), §4. If true,
  S(h) = O(h²) and T^R is super-polynomial (the R104 / R117 transfer as stated by the Lead; not re-derived here).
- OPEN: a construction of the lagging-clock delay mover; a proof that one exists for every (level, type).

## 8. Files
- experiments/lower/l5/: fev.c, revert.py, revert_H5lift_H6.out, fuelsrc.py, fuelsrc.out, fuelsrc_G7.out, utmpl.c, mclimb.c,
  greedyback.py, greedyback.out, slack.py, slack7.out, winfail.py, winfail_G7_l6.out, pulses.py, pulses_G7_l5.out, splice.py; out/ (gitignored).
- mclimb.c (edit-penalised climb from H5_lift, λ = 0.25-2 F-units per edit, 4 seeds): no improvement of F(5) = 94 in the runs before
  they were stopped (penalty too steep for the neutral drift the climb needs); superseded by the greedy walk back (§5).

## 9. Diff against TARGET.md
No statement mentions a parity game, a winning region, an algorithm's running time or a complexity class; all are about the IDEAL
model's step sequence (R104's definition) on 𝓛^R_d. Not M3, not a gauntlet step.
