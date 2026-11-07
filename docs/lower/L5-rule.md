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
  lands, and only in windows of the right key; see §5 for what the Ξ-order can and cannot compute here.
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
- Run B (P = 1, 2, 3; DM/DP 2/4, 3/6, 3/8; 300 restarts): see §7 (running at the time of writing; preliminary best: one doubling level
  (F 1 → 4) and F(l) linear above it).

## 5.-7. (in progress)

## 8. Files
- experiments/lower/l5/: fev.c, revert.py, revert_H5lift_H6.out, fuelsrc.py, fuelsrc.out, utmpl.c, mclimb.c; out/ (gitignored).

## 9. Diff against TARGET.md
No statement mentions a parity game, a winning region, an algorithm's running time or a complexity class; all are about the IDEAL
model's step sequence (R104's definition) on 𝓛^R_d. Not M3, not a gauntlet step.
