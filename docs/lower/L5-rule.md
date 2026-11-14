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
- Premise note (Lead 11:38Z): for a packet, PULSE-NEST (L-SI 42, lane) must be re-proved inside it from landed RESULTS (R104, R105 ENC,
  R110, R113) and DOUBLE-EQ′ (whose proof uses R113 ALIGN only, L4 §3); its proof (induction on k via the nested (j + 1)-window) uses
  only (E3), (E4), so GAP-NEST and PULSE-NEST together need no unlanded premise. DOMINANCE-FREEZE uses R105 ENC and the R104 movement
  rule only; CROSS-ECONOMY adds DOUBLE-EQ′ (E3)-(E5).
- DATA (slack.py → slack7.out; unit = j-window; set = levels 1-5; scope = stored start; target H = 7): violations of PULSE ≥ 7 − j or
  GAP ≥ 7 − j: H6_d24_F126: 87 (level 4: 15 pulses of the types (7, 0), (7, 1); level 5: 63 pulses of all four types + 9 gaps);
  G7_best_d28 (L-LOWER 4's warm start, F(6) = 222): 30 (corrected from «31», L-COMP 10's replay of slack.py, Lead 10:27Z; the parts are
  15 + 14 + 1), all at level 5: 15 pulses and 14 gaps of length 1 in ONE b-step type (9, 1), plus 1 pulse in the first window. The climb H6 → G7_best repaired the pulse/gap deficits type by type; one type is left.
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

- Trigger chains with link types (trig.py → trig_H6_G7.out; unit = j-window; scope = stored start; a link is Ξ if the mover's preference
  flipped one step before its move, K if it waited for its key): H6 level 5, all four types: x₂ ← the b-step mover or a long Ξ-line
  ending in a K-link (PULSE 1). G7_best level 5, types (8, 0), (8, 1), (9, 0): x₂ = 10 ← Ξ 12 (pair 6) ← Ξ 11 (the first mover of pair
  5), i.e. f_5 at u₁, a pair-6 mover at u₁ + 1, x₂ at u₁ + 2 (PULSE 2); type (9, 1): x₂ ← Ξ 15 ← K (PULSE 1). So H6 → G7_best repaired
  three types of level 5 by routing x₂_5's trigger through pair 6 (a RETURN-CHAIN f_j → pair j + 1 → x₂_j), and left the fourth on a
  key-gated trigger.
- RETURN-CHAIN in the records (retchain.py → retchain.out; unit = j-window, j and j + 1 doubling; scope = stored start): «x₂ of the
  nested (j + 1)-window is a trigger of x₂_j» holds in 7 of 15 windows at G7_best j = 3 (exactly the types with member 5), 1 of 7 at G7
  j = 2, 3 of 7 at H6 j = 2 (the types with member 2), 0 elsewhere (H5, DBL4, H6 j = 1, 3, 4); triggers lie 1-24 levels above j. A
  motif, not the rule.
- Targeted score (mclimb.c env SLACK=J:NEED with GUARD; checked against slack.py): G7_best: SLACK=5:2 → 47 good 5-windows of 63 (the
  16 bad = type (9, 1) + the first window); SLACK=4:3 → 31 of 31. H6: SLACK=5:2 → 0, SLACK=4:3 → 16. This is the score proposed for a
  routed climb (a gradient where F(6) has none).

- Pulses and gaps repaired, level 6 still fails: the FUEL obstruction (DATA). A short targeted climb (mclimb.c SLACK=5:2 GUARD=5 LV=6
  ANNEAL=0.02, seed 41, 2.2·10^6 of 2·10^7 steps to the best; a validation run of the score, not a brute climb campaign) from
  G7_best_d28 gives rec/SL41_d28.txt (sha1 c1b46c319fd614e5bcb0909b616a9f2833e0dfee; d 28; T 290; F 2 6 14 30 62 126 222 158 …;
  6 capped; identical T, F under fev, utmpl's exact-order simulator and l3/sim.py; l3/xcheck.py against L-NEW's box150 Gen at claude/l-new
  ae8e185d: SIM-MISMATCH 0, movescheck counters all 0, for SL41_d28 and G7_best_d28):
  slack.py with H = 7 finds 0 violations at levels 1-5 (every PULSE and GAP ≥ 7 − j), yet F(6) = 222 and the same 48 level-6 windows
  fail (now 2 steps long). fuel6.py → fuel6_SL41.out (unit = 6-window; scope = stored start): the first mover of pair 6 is 13
  (key-gated in every window); the second mover 12 is triggered per (parent type, own type): (8,0)/(10,0) ← 22, (8,1)/(10,0) ← 20,
  (9,0)/(10,1) ← 22, (9,0)/(11,1) ← {9, 11, 14}, (8,1)/(11,0) ← {8, 11, …}; in the windows nested under a level-5 window of type
  (9, 1) the needed mover's preference NEVER turns ((9,1)/(11,1): 12 «pref never»; (9,1)/(10,1): 13 «pref never»), and (8,0)/(11,0)
  fails because 13 did not return («already on c»). So the missing piece is fuel for pair 6 in the contexts under one parent type:
  room (PULSE, GAP) is necessary (PULSE-NEST, GAP-NEST) but not sufficient, and at the level being added the fuel supplier depends on
  the parent's type as well as the window's own type (in the capped levels of H6 / G7_best it depends on the own type only, §2).
  This matches L-SI 42's climb snapshot (box 80 §5: pulses met, F(6) = 222).

- Context of the fuel in CAPPED levels (fuel6.py → fuelctx.out; unit = j-window; scope = stored start): in H6 levels 4 and 5 and in
  G7_best level 5 the trigger set of each member of pair j is a function of the window's OWN b-step type, the same under every parent
  type (H6 level 5: own (8, ·) ← {8, 11}, (9, 0) ← {11, 12}, (9, 1) ← {11, 13}, under all four parents; G7_best level 5 likewise, up to
  an extra co-trigger 24 in 4 windows and 43 / 41 in the first windows). So a capped level needs at most four suppliers (one per own
  type), independent of the ancestors; the parent-dependence of SL41's level 6 is a property of a level not yet capped. DATA for
  CONJECTURE L5-TYPE (O(1) suppliers per level), not a proof.

- Lemma DOMINANCE-FREEZE (PROVED, lane; R105 ENC and the movement rule). For a mover x and a state s let dec_s(x) := the β of largest
  rank in the symmetric difference of the chains of (x, 0) and (x, 1) under s (it decides the Ξ-comparison: by ENC the sign of
  v(x, 0) − v(x, 1) is the parity sign of dec_s(x), negated if it lies on the chain of (x, 1)). (a) If dec_s(x) is the same β, on the
  same side, for all states s of a stretch, then x's preference is constant on the stretch. (b) If x is a member of a doubling pair j
  and x moves at t < t′ (consecutive moves of x), then x moves to opposite options (DOUBLE-EQ′ (E4) and the alternation of c_j between
  consecutive j-windows), so its preference under s_(t−1) and under s_(t′−1) differ; hence dec(x) is not one fixed β on one fixed side
  on all of s_(t−1), …, s_(t′−1). Proof: (a) ENC: v(x, 0) − v(x, 1) = Σ ±2^rank over the symmetric difference; the largest term fixes
  the sign. (b) by the movement rule x moves at t only if the other option is strictly better under s_(t−1). ∎
- The SL41 instance (domin.py → domin_SL41.out; unit = 6-window; scope = stored start): pair 6 is CROSS onto (22, 11) (12 → (22, 11),
  13 → (11, 22); L4 §2 DUAL: both members compare the same difference cv(22) − cv(11), with mirror preferences). In all 48 failing
  6-windows the deciding element of 12 and 13 is (rank 87, mover 9, option 1), alone in 16 of them and together with one other in
  32 (the carried-over first state): mover 9 (pair 4) sits on option 1 for the whole level-5 window of type (9, 1), its option-1 β
  (rank 87, odd) lies on 11's chain (11 → 9), and nothing that changes in those windows outranks it, so both members of pair 6
  prefer the 22-side throughout and the member on the 11-side never moves. In no good window is (87, 9, 1) a decider. This is the
  exact missing fuel: a β of rank > 87 on the chain of 22 or of 11 (above 9) that changes inside each window under parent (9, 1),
  or re-routing 11's chain away from 9's option 1. It is FROZEN-WINDOW (L4 §4) realised by rank dominance rather than by a constant
  difference.
- Single edits at the dominator (domfix.py → domfix_SL41.out; unit = genome; set = 111 rank swaps of option (9, 1) + 55 re-targets of
  the link 11:1 → 9; scope = stored start): 56 keep six capped levels, none raises F(6) above 222 (with rank 87 swapped down to 9, F is
  unchanged: another fixed element then decides). So the gap is not one badly ranked β: inside the windows under parent (9, 1) nothing
  on the chains of 22 or 11 changes that could flip the comparison: the fuel supplier for those 48 windows is absent.
- Two-edit fuel splices (fuelsplice.py; unit = genome; 20,000 trials: one option of a mover in the Ξ-closure of pair 6, outside pairs
  0-5, re-targeted to a mover that moves while 9 is parked on option 1, with its rank swapped above 87 and its parity flipped with
  probability 1/2; scope = stored start): no gain (F(6) = 222). The SL41 plateau survives every local repair tried.
- Exhaustive single re-targets (retall.py → retall_SL41.out; unit = genome; set = every option of the 27 movers of pair 6's Ξ-closure
  outside pairs 0-5, re-targeted to every mover and X: 2,970 genomes; scope = stored start): 145 are acyclic and keep six capped
  levels, none has F(6) > 222. Supplier candidate by activity: mover 19 (β of rank 95) moves 23 times while 9 is parked on option 1,
  but no single re-target puts it on the deciding chain without breaking a capped level. The plateau is at least two edits deep.
- Two-edit supplier search (retall2.py → retall2_19.out; unit = genome; set = every closure option re-targeted to mover 19, combined
  with every second closure re-target (any mover or X) or a swap of the first option's rank with any rank > 87: 144,011 genomes; scope
  = stored start): none has F(6) > 222 with six capped levels. The SL41 plateau is deeper than two edits for this supplier.
- Corollary CROSS-ECONOMY (PROVED, lane; DOUBLE-EQ′ (E3)-(E5), the movement rule, ENC). Let pair j be doubling and CROSS onto two
  movers a, b outside pair j: xt(p, k) = A_k, xt(q, k) = A_(1−k) with {A_0, A_1} = {a, b}. Then p prefers k iff q prefers 1 − k (the
  same comparison of ε-shifted cv(a), cv(b), mirrored). In a window with key c and first mover p (E5): p moves to c at u₁, so «A_c's side
  better» under s_(u₁−1); q moves to c at u₂, so «A_(1−c)'s side better» under s_(u₂−1); the next window has key 1 − c and needs «A_(1−c)
  better» at its u₁ − 1, which already holds at u₂ − 1. So (a) the shared comparison changes sign inside every pulse [u₁ − 1, u₂ − 1]
  (F(j − 1) + 1 sign changes in all), and (b) the first mover needs no fuel of its own: it is key-gated whenever the comparison does
  not change between u₂ and the next b-step. ∎ (DATA: SL41 pair 6, 13 «mv<K» in every window, fuel6_SL41.out.) With DOMINANCE-FREEZE:
  a fixed decider over one pulse kills that window; in SL41 the decider (87, 9, 1) is fixed over the 48 failing windows.

## 7. Summary: rule, obstruction, conjecture (labels as stated)
- No inductive rule G_h → G_(h+1) was found. What a rule must do is now specific (PROVED parts: GAP-NEST, PULSE-NEST, DOUBLE-EQ′; DATA:
  §2, §5, §6): for every level j ≤ h − 1 and each of the four b-step types (member of pair j − 1 × direction), the second mover of pair j
  needs a trigger line whose delay grows by one per extension (PULSE and GAP ≥ h − j), so an extension must lengthen Θ(h) lines (the
  zero-slack ones: all four types at j = h − 1, h − 2 in H6). The records realise this type by type (H6 → G7_best: 87 → 30 deficits, one
  type left), never by a uniform local rule (§4), and never without touching every level (§5).
- The obstruction located, in two layers (DATA on G7_best_d28 and SL41_d28; DOMINANCE-FREEZE PROVED): (i) room: in G7_best the type-(9, 1)
  pulses of level 5 are 1 (repaired in SL41); (ii) fuel: in SL41 the crossed pair 6 is decided by the β (87, 9, 1) of a capped pair-4
  mover throughout the windows under parent type (9, 1). A recursive rule must therefore also order ranks: the fuel of a new level must
  outrank the β's of lower tower movers that lie on its chains while those are parked. (i) in detail: a trigger line cannot be lengthened by a mover whose key
  clock is the flip it is supposed to delay; the delay mover must sit at a level whose key flips one step AFTER the first mover of the
  pair, in exactly the windows of one type. The search space of single splices did not contain one (§6).
- READING (not proved; the routing problem behind §3 (b)): in a window with key c, x₂_j must see the trigger as a rise of its option-c
  racer; option values only rise (R105 MONO), a single comparison sees the larger of the two racers' top β's, and the only movers whose
  state equals c in every window are f_j and x₂_j itself. So a per-type trigger must reach x₂_j through f_j's current option, or through a
  copy of f_j, i.e. one more mover with its own racers per type: the per-level cost is O(1) movers per type if keys allow, which would give
  S(h) = O(h) to O(h²).
- CONJECTURE (L5-TYPE): a capped tower of height h + 1 can be obtained from one of height h by adding O(h) movers: one delay mover per
  (zero-slack level, b-step type), at levels whose key clock lags the pair below by one step, plus one fuel supplier per (parent type,
  own type) context of the new level (≤ 16). Evidence: the type-by-type repair H6 →
  G7_best (DATA) and the fuel-type function (§2, DATA on H6, DBL4, RECF4, G7_best). Against: §6 (no single splice found; the fuel gap under parent type (9, 1) in SL41), §4. If the new level's fuel had to
  distinguish the types of all its ancestors, the count would be 4^h, not O(h): that is the alternative to rule out. If true,
  S(h) = O(h²) and T^R is super-polynomial (the R104 / R117 transfer as stated by the Lead; not re-derived here).
- OPEN: a construction of the lagging-clock delay mover; a proof that one exists for every (level, type).

## 8. Files
- experiments/lower/l5/: fev.c, revert.py, revert_H5lift_H6.out, fuelsrc.py, fuelsrc.out, fuelsrc_G7.out, utmpl.c, mclimb.c,
  greedyback.py, greedyback.out, slack.py, slack7.out, fuel6.py, fuel6_SL41.out, fuelctx.out, domin.py, domin_SL41.out, domfix.py, domfix_SL41.out, fuelsplice.py, retall.py, retall_SL41.out, retall2.py, retall2_19.out, rec/SL41_d28.txt, trig.py, trig_H6_G7.out, retchain.py, retchain.out, winfail.py, winfail_G7_l6.out, pulses.py, pulses_G7_l5.out, splice.py; out/ (gitignored).
- mclimb.c (edit-penalised climb from H5_lift, λ = 0.25-2 F-units per edit, 4 seeds): no improvement of F(5) = 94 in the runs before
  they were stopped (penalty too steep for the neutral drift the climb needs); superseded by the greedy walk back (§5).

## 9. Diff against TARGET.md
No statement mentions a parity game, a winning region, an algorithm's running time or a complexity class; all are about the IDEAL
model's step sequence (R104's definition) on 𝓛^R_d. Not M3, not a gauntlet step.
