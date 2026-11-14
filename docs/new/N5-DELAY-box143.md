# Box 143 N5-DELAY: DELAY-LIN not proved; Lemma STEP-DELAY (PROVED, lane) sharpens box 142's chain to steps ≤ 1 + 2d + DELSTEPS, so DELAY-LIN would give LINEAR runs on the 2-wide ladder; C-ELEM normal form PROVED; the briefed charging (a face re-rises only after a carry above) is DEAD on R188's exact pin x3_L8; delays stay about 5 per level up to d 12 (DATA)
L-NEW successor 48, 2026-11-02 (date -u: see the commit). Lead brief 03:07Z (box 143: prove DELAY-LIN on the 2-wide IDEAL-ACYC ladder,
or find its exact obstruction). Labels: PROVED (lane), CONJECTURE, READING, DATA, DEAD. G-N5-TIME, IDEAL-ACYC-POLY, UP-LIN and
DELAY-LIN stay OPEN. Not a TARGET.md claim.
Model: R178 §1 IDEAL model on the 2-wide deg-2 ladder in the R188 genome format. Levels 0..d−1, movers u_l = 2l, v_l = 2l + 1.
At level l ≥ 1, option k has W-target 2(l−1) + k; at level 0 the W-target is c_W. Ξ-targets are any later mover in a topological
order «xorder», or T. Notation follows box 142: L_l, carry, released, DELAY.

## 0. Answer
- DELAY-LIN is NOT proved. No obstruction to it was found either.
- PROVED (lane), §1: three lemmas.
  - Lemma C-ELEM: every mover is a Muller C-element. x moves to option k at step t exactly when two conditions hold:
    - A_x(t) = k ≠ σ_(t−1)(x), where A_x(t) is the option toward L_(l−1)(t) (same step);
    - B_x(t−1) = k, where B_x is the strictly Ξ-better face (one step late).
    - So between two moves of x both A_x and B_x flip, and moves(x) ≤ 1 + min(F_(l−1), flips(B_x)). Each delay of x is one B_x flip.
  - Lemma STEP-DELAY: the least-level mover of every step t ≥ 2 is either DELAYED (a box 142 delay event) or PRE (its level has had no
    carry yet, or it is at level 0). Hence steps ≤ 1 + 2d + DELSTEPS ≤ 1 + 2d + Σ DELAY, where DELSTEPS = steps whose least mover is
    delayed.
    - This replaces box 142's 2 + 2d + 2d² + 2dD. So DELAY-LIN implies LINEAR runs, not only O(d²).
    - Conversely Σ DELAY ≤ moves ≤ 2d · steps. So IDEAL-ACYC-POLY on the 2-wide ladder ⟺ DELSTEPS polynomial ⟺ Σ DELAY
      polynomial.
  - Lemma ABSORB: if u_l and v_l point at the same lower mover before and after a step without a level-l move, then L_l is unchanged,
    even when L_(l−1) flips. A carry crosses a level in the same step only when that level is split.
- DEAD: the briefed charging route, read literally: «a face that rose cannot rise again until a carry passes above it (at a level ≥ the
  face owner's)».
  - Instance: R188's exact pin x3_L8 (d 3, steps 8). Face (mover 0, option 0) reads the top mover 4. It rises at steps 5 and 6, and no
    L_m changes at step 6 at any level: mover 4's move at step 6 is a top-level delay.
  - x3_L8 has 4 such pairs (5 with the open interval). The d 12 champion has 26 of 196; up_d8_s8 (UP shape) has 3 of 56.
  - Face rises grow with d: up to 13 rises of one face at d 12. B flips and moves per mover do not grow that fast (§2).
  - READING: a charging argument must count CROSSINGS of a mover's two faces (B flips), not rises of one face.
- DATA (§2), from climbs that maximise Σ DELAY directly (ANY acyclic Ξ, 60-80k mutations):
  - Σ DELAY = 5 / 10 / 15 / 22 / 24 / 40 / 38 / 63 at d = 3 / 4 / 5 / 6 / 7 / 8 / 10 / 12, i.e. about 5 per level (ratio 1.7 → 5.3,
    climbs noisy).
  - steps = 6 … 26, about 2.2d; DELSTEPS ≤ 23.
  - Max delays into one option ≤ 3; max delays of one mover ≤ 5.
  - Max moves of ONE mover is not constant: a climb on that score gives 3 / 5 / 7 at d = 4 / 6 / 8 (ANY), and 4 at d 8 (UP).
    - Most of those moves are CAR moves (at carry steps), not delays. mc_d4 has 3 steps, 1 delay and a mover with 3 moves.
- CONJECTURE DELAY-LIN (DATA d ≤ 12; unchanged). The weaker CONJECTURE DELSTEP-LIN (DELSTEPS = O(d)) is equivalent to linear runs by
  STEP-DELAY.
- CONJECTURE MOVE-CONST (O(1) moves per mover) is NOT made: 7 moves at d 8.

## 1. Proofs (PROVED, lane; R178 §1 rule, R188 ladder format)
- Lemma C-ELEM.
  - The deg-2 availability set is A_(t−1)(x) = {σ_(t−1)(x)} ∪ {k : face_(t−1)(x,k) ▷ face_(t−1)(x,σ)}. So the other option k is
    available iff B_x(t−1) = k.
  - The new choice is the key-least available option under the step-t keys of the lower level (bottom-up, R178 §1).
    - At level l ≥ 1 the two options' keys are key_t(u_(l−1)) + gate and key_t(v_(l−1)) + gate.
    - These two lower keys are distinct tuples of equal length l, so the order is decided before the gate entry: the least is the
      option toward L_(l−1)(t) = A_x(t).
    - At level 0 both W-targets are c_W, so A_x is the gate-smaller option, constant.
  - Hence x moves to k iff k ≠ σ_(t−1)(x), k is available (B_x(t−1) = k) and k is key-least (A_x(t) = k).
  - A move to k needs A = B = k. The previous move (to k̄), or the start state, needed A = B = k̄, unless x had not moved yet. So
    between consecutive moves A_x flips (one carry of level l − 1) and B_x flips (one crossing of x's two faces). ∎
  - Corollaries.
    - (a) Level-0 movers and movers before the first carry of level l − 1 move at most once.
    - (b) A delay of x (box 142) is a move of x whose B_x flip happened at step t − 1, after the carry. This is DELAY-CAUSE again.
    - (c) A mover whose two faces have the same Ξ-target (or both T) has a static B, so it moves ≤ 1 time. Its faces differ by the
      β-weights and the lengths only.
- Lemma STEP-DELAY. Let t ≥ 2, M_t ≠ ∅ the movers of step t, h ∈ M_t of least level l.
  - (i) No carry of level l − 1 happens at step t.
    - By L-ACCOUNT (box 140), L_(l−1) changes at t only if a level-(l−1) mover moves at t or L_(l−2) changes at t.
    - By induction down to level 0 (whose keys change only by level-0 moves), some mover of level < l moves at t. This contradicts
      the minimality of l.
  - (ii) Suppose l = 0, or no carry of level l − 1 happens before t. Then h is PRE, and by C-ELEM (a) each mover has at most one PRE
    move. So at most 2d steps have a PRE least mover.
  - (iii) Otherwise let s < t be the last carry of level l − 1; A_h is constant on [s, t].
    - If h moved at some u ∈ [s, t), then σ(h) = A_h from u on, and h cannot move at t (C-ELEM). So h did not move in [s, t), and
      σ_(s−1)(h) = σ_(t−1)(h) ≠ A_h(t) = A_h(s).
    - So h is released by s, does not move at s, and moves at t, before the next carry: a delay event (box 142 definition).
  - Distinct steps give distinct (h, t) events. Hence steps ≤ 1 + 2d + DELSTEPS. ∎
  - Checked: «OTHER» least movers = 0 on all genomes of §2 (cause.py LEAST).
- Lemma ABSORB. Suppose σ(u_l) and σ(v_l) both target the same lower mover y at states t − 1 and t (no level-l move at t).
  - Then key_t(u_l) and key_t(v_l) share the prefix key_t(y), and the gate entries decide.
  - Those gate entries are the same as at t − 1. So L_l(t) = L_l(t − 1).
  - In the split state (different targets), L_l is the mover pointing at L_(l−1). So a carry propagates through a split level and is
    absorbed by a same level. ∎

## 2. DATA
Tools in experiments/new/box143/:
- cause.py: C-ELEM check, least-mover classes, STEP-DELAY bound, and per delay the cause movers on the toward face's Ξ-play one step
  earlier with their class and level offset.
- perx.py: per option / per mover delays and moves.
- rerise.py: the literal re-rise hint.
- dclimb.py / mclimb.py: climbs on Σ DELAY / on max moves of one mover.
- trace.py: run printer.
- pincheck.sh: pins.

| genome | d | steps | Σ DELAY | DELSTEPS | max delays per option / per mover | max moves per mover | re-rise viol. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| x3_L8 (R188 exact, d 3) | 3 | 8 | 5 | 4 | 2 / 3 | 4 | 4 |
| g4_L12 (R188, d 4) | 4 | 12 | 7 | 6 | 2 / 3 | 4 | 3 |
| dc_d3 / d4 / d5 / d6 | 3-6 | 6 / 8 / 9 / 12 | 5 / 10 / 15 / 22 | 4 / 6 / 7 / 10 | ≤ 2 / ≤ 3 | ≤ 3 | 0 / 1 / 3 / 0 |
| dc_d7 / d8 | 7, 8 | 13 / 23 | 24 / 40 | 10 / 19 | 2 / 3, 3 / 5 | 4 / 5 | 14 / 22 |
| dc_d10 / d12 | 10, 12 | 21 / 26 | 38 / 63 | 18 / 23 | 2 / 4, 3 / 5 | 4 / 5 | 5 / 26 |
| mc_d4 / d6 / d8 (max-moves climbs) | 4-8 | 3 / 7 / 14 | 1 / 5 / 21 | 1 / 3 / 11 | ≤ 3 / ≤ 3 | 3 / 5 / 7 | not run |
- C-ELEM violations 0, least-mover OTHER 0, NOCAUSE 0 on every genome above and on up_d3 … up_d8_s8 and lag_min_d2.
- The cause of a delay can be a LOWER-level mover in the ANY shape (dc_d12 offsets −10 … +7). Only in the UP shape is it always higher.
- dc_d8 replays a 3-step block (steps 3-5 = 16-18, the same movers). The replay does not recurse.
- Pins: R188's x3_L8_n48 and g4_L12_n62 were copied read-only from claude/l-red ce1d19e9 into box143/inst (sha1 158ca15d…,
  658f4e23…; starts f07be770…, 9f3e1f92…).
  - Oink 8fbf0a7 --zlk and --tl: solution verified on both.
  - pinwin AGREE; n5b identical state sequences (12 / 16 states, 1 fallback each); box143/pincheck.txt.
  - The IDEAL genomes x3_L8.json / g4_L12.json replay to 8 / 12 steps, matching R188.

## 3. Status and next
- PROVED (lane): C-ELEM (+ corollaries), STEP-DELAY (steps ≤ 1 + 2d + DELSTEPS), ABSORB.
- DEAD: the literal re-rise charging (x3_L8).
- CONJECTURE: DELAY-LIN, DELSTEP-LIN (the latter ⟺ linear 2-wide runs).
- OPEN: IDEAL-ACYC-POLY, G-N5-TIME.
- READING (what a proof must do): bound the crossings of the two monotone face sequences of each mover, summed over least movers. Face
  RISES are too many (13 at d 12).
  - A crossing needs a move on a PRE-MERGE segment of the two Ξ-plays (box 135 MERGE), since moves on the common suffix cancel.
  - Next candidate: charge each DELSTEP to a (pre-merge segment, carry wave) pair, and show that a carry wave crossing a segment
    flips the order of at most O(1) least movers below it.
- For L-RED 45: a counter must make DELSTEPS super-linear. By STEP-DELAY that is necessary and sufficient for super-linear runs on the
  2-wide ladder. Many delays per step (dc_d12: 63 delays in 26 steps) do not help.
