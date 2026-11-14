# Box 142 N5-LAG: NO-LAG is false (smallest leapfrog: d 2, 4 movers, via a sibling Ξ-read); bounded lag cannot suffice; the right quantity is DELAY, and Lemma DELAY-CHARGE gives flips(L_l) ≤ flips(L_(l−1)) + 2 + DELAY_l, so O(d) total delays ⇒ O(d²) steps on the 2-wide ladder
L-NEW successor 47, 2026-11-02 (date -u: see the commit). Lead GO 02:35Z (box 142: NO-LAG or LAG ≤ O(1) per carry; last box before
parking). Labels: PROVED (lane), CONJECTURE, READING, DATA, DEAD. G-N5-TIME, IDEAL-ACYC-POLY and UP-LIN stay OPEN. Not a TARGET.md claim.
Model: the 2-wide deg-2 IDEAL ladder (box 140 «LADDER»), any acyclic Ξ-graph unless said otherwise; R178 §1 rule. Notation: L_l = the
key-smaller of u_l, v_l at a state; a CARRY at level l − 1 is a step s with L_(l−1)(s) ≠ L_(l−1)(s − 1). The level-l movers RELEASED by
it are those whose option at state s − 1 does not target L_(l−1)(s). F_l := the number of steps at which L_l changes.

## 0. Answer
- DEAD: NO-LAG. «Two same-level vertices released by one lower key flip move at the same step» fails.
  - Smallest instance: lag_min_d2 (box142/lag_min_d2.json), d = 2 with 4 movers, a 2-step run.
    - Step 1: mover 1 (level 0) moves, so L_0 changes and both level-1 movers 2 and 3 are released.
    - Mover 3 moves at step 1.
    - Mover 2 moves only at step 2. Its option toward L_0 has Ξ-target mover 3, its own sibling, so its face rises only after 3 has
      moved.
  - In the UP shape (Ξ-targets strictly higher), lag needs a move from above. up_d4 (box 140): a level-1 carry at step 4, released
    movers 2 and 3 move at steps 6 and 4 (lag 2).
  - Lag events: 6 of 8 UP-LADDER champions, lag ≤ 2. No UP-LADDER lag at d = 2 in 200,000 random trials, as forced by TOP-STATIC.
- «LAG ≤ O(1) per carry» does not suffice, and NO-LAG alone does not either (PROVED, lane, §1):
  - L_l can change at most once per step. With lag 1, one carry already yields 2 changes of L_l, i.e. doubling per level.
  - Even with no lag, a SPLIT level whose released mover moves after the carry step yields 2 changes: the propagation at the carry
    step and the merge later.
  - The quantity that decides is DELAY, i.e. a released mover that does not move at the carry step but moves later, before the next
    carry. Lag is a special case: the later of two lagging movers is delayed.
- PROVED (lane):
  - Lemma DELAY-CHARGE: F_l ≤ F_(l−1) + 2 + DELAY_l on every 2-wide ladder.
  - Lemma DELAY-CAUSE: each delay at step s′ needs a strict face rise at step s′ − 1, caused by a move on the delayed mover's option's
    Ξ-play at step s′ − 1.
- The chain asked for (PROVED, lane, §1): if Σ_l DELAY_l ≤ D, then F_l ≤ 2(l + 1) + D, moves at level l ≤ 2(1 + F_(l−1)), and the run has
  ≤ 2 + 2d + 2d² + 2dD steps. So D = O(d) gives O(d²) on the 2-wide ladder.
  - Linear (UP-LIN) would need a finer count. DELAY-CHARGE is tight in the data's shape: levels near the bottom add 2-3 flips per level.
- The d = 3 exact maximum 8 (moves per level 2, 4, 7) is allowed: the chain gives moves_1 ≤ 6 and moves_2 ≤ 2(5 + DELAY_1).
- DATA (§2): DELAY-CHARGE holds on all 9 ladder genomes (0 violations). DELAY per level ≤ 4; Σ DELAY = 11 at d = 7 and 14 at d = 8
  (up_d8_s8: 0, 3, 3, 4, 2, 1, 1, 0).
- CONJECTURE DELAY-LIN (DATA only): Σ_l DELAY_l = O(d) on 2-wide IDEAL-ACYC ladders. With DELAY-CHARGE it implies O(d²) runs, i.e. the
  2-wide case of IDEAL-ACYC-POLY. Proving it means counting Ξ-events one step before each delay (DELAY-CAUSE), the same circular object
  as before, now localised to «released and waiting» movers.

## 1. Proofs (PROVED, lane)
- One change per step: F_l counts steps, by definition.
- Lemma DELAY-CHARGE.
  - L_l changes only at a step where L_(l−1) changes or a level-l mover moves (box 140 L-ACCOUNT).
  - Before the first carry at level l − 1, each level-l mover moves at most once (box 140 TOWARD-L: after a move it targets L_(l−1),
    which has not changed). So there are ≤ 2 change steps there.
  - Take a carry s and the next carry s* (or the end).
    - In [s, s*), a non-released mover already targets L_(l−1) and cannot move (TOWARD-L).
    - A released mover moves at most once in [s, s*) (afterwards it targets L_(l−1)).
    - So the change steps of L_l in [s, s*) are among {s} and the steps in (s, s*) at which a released mover moves. Those are exactly
      the DELAY events of this carry.
    - Hence ≤ 1 + (delays of this carry).
  - Summing over the F_(l−1) carries gives F_l ≤ 2 + F_(l−1) + DELAY_l. ∎
- Lemma DELAY-CAUSE. Let x be released by the carry s, not move at s, and move at s′ ∈ (s, s*).
  - L_(l−1) is constant on [s, s*), so x's key order (= the order of L_(l−1), TOWARD-L proof) is constant.
  - At step s′ − 1 (≥ s), x did not move with the same key order, so its option toward L_(l−1) was not available:
    face_(s′−2)(toward) ⊴ face_(s′−2)(current).
  - At step s′ it is available: face_(s′−1)(toward) ▷ face_(s′−1)(current) ⊵ face_(s′−2)(current) (VAL-MONO, box 139; x's current option
    is unchanged).
  - So face(toward) rose strictly at step s′ − 1, and some mover on that option's Ξ-play moved at step s′ − 1. In an UP-LADDER that mover
    is of higher level; in lag_min_d2 it is the sibling. ∎
- The chain.
  - F_0 ≤ 2 (level-0 keys are static gates; each level-0 mover moves ≤ 1 time).
  - DELAY-CHARGE: F_l ≤ 2(l + 1) + Σ_(j≤l) DELAY_j ≤ 2(l + 1) + D.
  - TOWARD-L: moves at level l ≤ 2(1 + F_(l−1)).
  - Summing: moves ≤ 2 (level 0) + Σ_(l=1)^(d−1) 2(1 + 2l + D) ≤ 2 + 2d + 2d² + 2dD. Every non-stuck step has a mover, so steps ≤
    moves. ∎
- Why bounded lag is not enough: with lag 1 at every carry and no other delay, DELAY_l = F_(l−1) and DELAY-CHARGE becomes F_l ≤ 2F_(l−1)
  + 2, which is exponential. The data's lags are rare (≤ 3 lag events per run), not short.

## 2. DATA
Tool: experiments/new/box142/lag.py (LAG events, LAGMAX, DOUBLE, DELAY per level, L-flips per level, DELVIOL = levels violating
DELAY-CHARGE; `--rand d trials seed` searches random UP-LADDERs, ANY=1 allows any acyclic Ξ-graph).

| genome | d | steps | lag events (max lag) | DELAY per level | L-flips per level | DELVIOL |
| --- | --- | --- | --- | --- | --- | --- |
| lag_min_d2 (smallest leapfrog) | 2 | 2 | 1 (1) | 0, 1 | 1, 1 | 0 |
| up_d3 | 3 | 5 | 0 | 0, 1, 0 | 1, 2, 3 | 0 |
| up_d4 | 4 | 7 | 1 (2) | 0, 1, 1, 0 | 1, 2, 2, 3 | 0 |
| up_d5 / up_d5_s15 | 5 | 11 / 10 | 3 (2) / 0 | 0, 2, 3, 0, 0 / 0, 1, 2, 1, 0 | 2, 5, 5, 3, 2 / 2, 3, 4, 4, 3 | 0 / 0 |
| up_d6 / up_d6_s16 | 6 | 13 / 13 | 3 (1) / 2 (1) | 0, 1, 3, 2, 1, 0 / 0, 2, 1, 2, 1, 0 | 2, 3, 7, 6, 6, 5 / 2, 5, 4, 3, 3, 4 | 0 / 0 |
| up_d7_s7 | 7 | 16 | 2 (1) | 0, 4, 3, 2, 2, 0, 0 | 2, 6, 6, 5, 4, 2, 1 | 0 |
| up_d8_s8 | 8 | 19 | 2 (1) | 0, 3, 3, 4, 2, 1, 1, 0 | 2, 6, 8, 9, 7, 6, 6, 5 | 0 |
- Random search: UP shape, d = 2, 200,000 trials (seed 1): no lag. ANY acyclic, d = 2, 200,000 trials (seed 2): lag found at trial 420
  (the minimal genome above, kept as box142/lag_min_d2.json).
- Not tested: R188's exact d = 3 pin x3_L8_n48. Its IDEAL genome was not copied into this lane. The chain's bound allows its moves 2 / 4 / 7.

## 3. Status
- DEAD: NO-LAG (lag_min_d2; in the UP shape up_d4).
- PROVED (lane): one change per step; DELAY-CHARGE; DELAY-CAUSE; the chain Σ DELAY = O(d) ⇒ O(d²) steps; bounded lag ⇏ polynomial.
- CONJECTURE DELAY-LIN (DATA only, d ≤ 8). OPEN: UP-LIN, IDEAL-ACYC-POLY (2-wide and general).
- READING: a counter needs Θ(F_(l−1)) delays at many levels, i.e. a Ξ-event one step before a constant fraction of all carries. L-RED's
  LAG reading (R188) is the lag special case of this.
