# R198 CARRY+4 is FALSE (EXACT, d 5): F = [2, 6, 12, 9, 2] (F_2 = F_1 + 6, pin c4x_d5_F12_n96) and F = [2, 3, 6, 14, 7] (two consecutive doubling levels, level 3 at the full ceiling 2F_2 + 2, pin dd_d5_F14_n96); the proof route reduces CARRY+4 exactly to DBL − ZERO ≤ 3 (Lemma INTERVAL, FLIP-COUNT, AUTOMATON: PROVED, lane), refuted by DBL − ZERO = 5 and 7; levels ABOVE a level raise its carries (L-RED successor 47)
Started 2026-11-03 02:02Z (Lead UN-PARK 02:03Z, date -u): «CARRY+4 at d 5 (exact), plus a PROOF attempt of F_l ≤ F_(l−1) + 4 by interval
nesting (R197 §4) … Label it carefully: it is a proof for the 2-wide degree-2 ladder model only, not N5 … Write the proof attempt so it
could become a referee packet: every step justified by landed RESULTS or by lane lemmas named with commits.» Labels: PROVED (lane),
EXACT (z3), DATA, OPEN. NOT a TARGET.md claim; NOT an N5 statement (RESULTS R104 is one-way: IDEAL-ACYC runs are N5 runs, not
conversely). G-N5-TIME OPEN.

## 0. Answer
- CARRY+4 is FALSE. EXACT (z3, r197/liftloop.py with KEYFLIP + LAG lane-lemma clauses, FMIN 2:11 at L 12; REL 3634 s, FIX 505 s):
  a d 5 ladder run with F = [2, 6, 12, 9, 2] (all steps counted), L 12. Level 2: F_2 = 12 = F_1 + 6, per-interval flips [2, 2, 2, 1, 1,
  2, 2] (DBL 5, ZERO 0). Genome r197/lag/c4x_d5_F12.json; realised and pinned c4x_d5_F12_n96 (n 96; sha1 .pg 6213e350…, .start
  eb383fec…): lemck L 12, 0 violations (one real FL run of length 12); startck, Oink 8fbf0a7 --zlk + verify, --tl + verify, xeng: PIN OK.
- Against R197 §2b (d 4: F_2 ≤ 10 on EVERY run, exact): adding two levels above level 2 raises its exact maximum from 10 to ≥ 12. The
  extra levels take part in the late wakes (3 of the 5 delayed level-2 moves have a level-3 or level-4 waker, u4 or v3; trace in §4). This is
  the direction the R197 §4 reading called «delay lines through higher levels». The ceiling 2F_1 + 2 = 14 is not yet reached.
- Second exact d 5 witness (FMIN 3:13 at L 14; REL 14063 s, FIX 18 s): r197/lag/dd_d5_F14.json, L 14, F = [2, 3, 6, 14, 7].
  Level 2 doubles (F_2 = 6 = 2F_1; DBL 3, ZERO 1) and level 3 reaches the KEYFLIP ceiling F_3 = 2F_2 + 2 = 14 (per-interval [2, 2,
  2, 2, 2, 2, 2]; R_3 flips at every one of the 14 steps). Mechanism: level-2 carries come every 2 steps (t3, t5, …, t13); at each,
  v3 moves at once and u3 (Ξ-fork [v3, v2]) is woken by v3 one step later: spacing 2 below plus a partner wake of delay 1 gives a full
  doubling. This realises the R197 §4 nesting picture for two levels (delays 2, then 1). Pinned dd_d5_F14_n96 (n 96; sha1 .pg
  ab093e8c…, .start 9e88d7a0…): lemck L 14, 0 violations; startck, Oink zlk / tl + verify, xeng: PIN OK. Max run at d 5 ≥ 14.
- READING (not a claim): doubling stacks over k consecutive levels only if delays shrink by ≥ 1 per level (R197 §4), so the bottom
  delay must be ≥ k and must be carried by delay lines through levels above. If delay-δ lines exist for growing δ with O(δ) extra
  levels, carries grow like 2^(Θ(d)) on this ladder class; if not, the excess per level stays bounded. Both witnesses have run
  length ≤ 14: no long run yet.
- Proved (lane, §2), self-contained apart from the model: on a 2-wide degree-2 ladder (each level-l ≥ 1 mover's two options have the
  two level-(l − 1) movers as W-targets) (i) every move goes to the key-preferred option; (ii) a mover moves at most once between two
  consecutive carries of the level below; (iii) R_l is a fixed function of the two level-l options and of R_(l−1); (iv) Lemma INTERVAL:
  every interval between consecutive carries of level l − 1 (and the initial stretch) contains at most 2 flips of R_l, and a 2-flip
  interval (a DOUBLE) contains a delayed level-l move; (v) the identity F_l = F_(l−1) + 1 + DBL_l − ZERO_l; (vi) the AUTOMATON of the
  pair state (n = 0 forces an empty interval; S-doubles have a gate-determined fixed leader).
- So CARRY+4 ⟺ DBL_l − ZERO_l ≤ 3 at every level, and the d 5 witnesses have DBL − ZERO = 5 (level 2) and 7 (level 3). The proof route is dead as stated. What
  survives: the identity (v) makes F_l − F_(l−1) − 1 = DBL_l − ZERO_l the exact quantity to bound, and every double costs one delayed
  move of the level, woken from Ξ-descendants (R197 WAKE-CHAIN). Whether DBL − ZERO stays bounded per level (F linear, with a larger
  constant) or grows with the number of levels above (F super-linear) is OPEN; d 5 runs in flight (§4).
- Scope: 2-wide degree-2 IDEAL-ACYC ladders. RESULTS R104 makes the pin a real N5 FL run; a growth result here would be a real N5
  statement only through R104 (one-way). Not a TARGET.md claim. No family yet: one instance at d 5.

## 1. Model and notation (RESULTS R104 statement; R191 ladder)
- IDEAL step (RESULTS R104, the model of L-RED R178 §1): every mover x goes to the key-least option of A_(t−1)(x) := {s_(t−1)(x)} ∪
  {options whose Ξ-face is strictly better than the current one under s_(t−1)}, keys read in the NEW state s_t; key of option (x, k) =
  key of its W-target followed by the gate index g(x, k) (lexicographic, gates distinct); level-0 W-targets are the exit, so a level-0
  key is the gate alone.
- 2-wide ladder: levels 0..d − 1, movers u_l, v_l; degree 2; for l ≥ 1 the two options of a level-l mover have the two level-(l − 1)
  movers as W-targets (one each; which is which may differ per mover). R_l(s) := whether key_s(u_l) < key_s(v_l); a carry of level l
  at step t means R_l(s_(t−1)) ≠ R_l(s_t); F_l := number of carries of level l.
- small_t(l − 1) := the R_(l−1)-smaller level-(l − 1) mover at s_t. KP_t(x) := the option of x with the smaller key at s_t.

## 2. Proofs (PROVED, lane)
- Lemma K0 (keys). For l ≥ 1 and x of level l, KP_t(x) is the option whose W-target is small_t(l − 1). For x of level 0, KP_t(x) is
  constant. Proof: key(x, k) = key(W(x, k)) · g(x, k); the two W-targets are distinct movers of level l − 1 whose keys are distinct
  tuples of equal length (their last entries are distinct gates), so the prefix decides. Level 0: keys are the fixed gates. ∎
- Lemma K1 (moves go to KP). If x moves at step t, s_t(x) = KP_t(x). Proof: s_(t−1)(x) ∈ A_(t−1)(x) and x takes the key_t-least
  element; it moved, so key_t(s_t(x)) < key_t(s_(t−1)(x)); with two options this is KP_t(x). ∎
- Lemma K2 (one move per interval; = L-NEW box 149 KEYFLIP in this setting, re-proved). If x (level l ≥ 1) moves at t_1 < t_2 with no
  move in between, some step in (t_1, t_2] is a carry of level l − 1. Level-0 movers move at most once. Proof: by K1, s_(t_1)(x) =
  KP_(t_1)(x) and s_(t_2)(x) = KP_(t_2)(x) ≠ s_(t_2 − 1)(x) = s_(t_1)(x); so KP changes in (t_1, t_2], and by K0 that needs
  small(l − 1) to change, i.e. a carry of level l − 1. Level 0: KP constant, and a second move would return to a non-KP option. ∎
- Lemma K3 (R_l formula). If u_l, v_l have the same W-target at s_t, R_l(s_t) is the order of their current gates; otherwise the mover
  whose W-target is small_t(l − 1) is first. Proof: as K0. ∎
- Lemma INTERVAL. Let l ≥ 1, let c_1 < c_2 < … < c_m be the carries of level l − 1, I_0 := steps 1..c_1 − 1 and
  I_i := steps c_i..c_(i+1) − 1 (with c_(m+1) − 1 := L). Then (a) each of u_l, v_l moves at most once at steps of I_i; (b) R_l flips at most
  twice at steps of I_i; (c) if R_l flips twice at steps of I_i, i ≥ 1, some level-l mover moves at a step t ∈ I_i, t > c_i, and did not
  move at t − 1 (a delayed move; its option was then not available at s_(t−2) and is at s_(t−1), so a Ξ-descendant moved at t − 1).
  - Proof. (a) K2 (no carry of level l − 1 at steps c_i + 1..c_(i+1) − 1). (b) small(l − 1) is constant on s_(c_i), …, s_(c_(i+1) − 1);
    by K3, R_l can change at a step of I_i only at c_i or at a step where u_l or v_l moves. Case S (u_l, v_l share their W-target at
    s_(c_i − 1)): with no move at c_i the shared target and the gates are unchanged, so R_l does not flip at c_i; at most two later
    moves remain (a): ≤ 2 flips. With a move at c_i: that step plus ≤ 1 later move: ≤ 2. Case D (different W-targets at s_(c_i − 1)):
    after the carry exactly one of them, o, has W-target small_(c_i)(l − 1); by K1 o cannot move during I_i (it is on KP_(c_i), and KP
    is constant on I_i); so at most c_i and one move of the other: ≤ 2. I_0: KP constant, ≤ one move each: ≤ 2.
    (c) Two flips in I_i, i ≥ 1. In case S without a move at c_i both flips are at moves after c_i; in case S with a move at c_i and in
    case D, one flip is at a move after c_i. Let t > c_i be such a move of x. t is not a carry of level l − 1 (t ∈ I_i), so KP_(t−1)(x)
    = KP_t(x) and the key order of x's options is the same at s_(t−1) and s_t. x did not move at t − 1 (if t − 1 > c_i by (a); if
    t − 1 = c_i, a move at c_i and at t would contradict (a)). Then s_(t−2)(x) = s_(t−1)(x) =: o and the new option w = KP_t(x) =
    KP_(t−1)(x). If w ∈ A_(t−2)(x), then at step t − 1 the key-least element of A_(t−2)(x) ⊆ {o, w} under key_(t−1) would be w, so x
    would have moved at t − 1. So w ∉ A_(t−2)(x) and w ∈ A_(t−1)(x): a face value of x changed between s_(t−2) and s_(t−1); faces of x
    depend only on the states of its Ξ-descendants, so one of them moved at t − 1 (this is R189 Corollary LAG, 8192e194, re-proved). ∎
- Corollary FLIP-COUNT. There are F_(l−1) + 1 intervals I_0..I_m, each with 0, 1 or 2 flips, so F_l = (F_(l−1) + 1) − ZERO_l + DBL_l.
  Hence F_l ≤ F_(l−1) + 4 ⟺ DBL_l − ZERO_l ≤ 3, and F_l ≤ 2F_(l−1) + 2 always. ∎
- Shape of a double (by the case analysis above, PROVED): in case S, the mover that moves first (at c_i or later) must lose the gate
  comparison on BOTH shared targets (old and new small); in case D, the mover m on the old small target must not move at c_i, must move
  later (delayed), and must win the gate comparison on the new small target. In both, one mover is delayed past the carry.

- Corollary AUTOMATON (PROVED, from K1-K3 and the case analysis). Let n_i ∈ {0, 1, 2} be the number of level-l movers on their KP option
  at s_(c_i − 1) (the last state before the carry that opens I_i, i ≥ 1). Then: n_i = 0 ⇒ I_i has 0 flips and n_(i+1) = 2 (after
  the carry both are on KP, so neither can move); n_i = 2 ⇒ only the two movers' own moves can flip R_l in I_i, a double needs both
  to move, and n_(i+1) = number of movers that moved; n_i = 1 ⇒ R_l flips at c_i unless the off-KP mover moves exactly at c_i, and a
  double needs that mover to move strictly later. A double always ends with n_(i+1) = 2. In an S-double (n_i = 2) the first mover is
  the gate-loser on BOTH shared W-targets, so it is the same mover in every S-double of the level (if the two gate comparisons have
  different losers, S-doubles are impossible at that level). So a level with many doubles runs a fixed «leader moves, follower is
  late» pattern, and every double pays a delayed move of the follower (or of the off-KP mover).
- DATA for the automaton (r197/ivl.py checks G: n = 0 ⇒ ZERO, H: the double shapes): 0 violations on the 10 committed in-class genomes
  (the R189 lag1 / lag1u genomes are outside the class: one of their movers has both options on the same W-target).

## 3. What DBL-3 needs (OPEN) and why the interval argument stops there
- Every double costs one delayed move (§2 (c)), so DBL_l ≤ #delayed level-l moves (= box 142 DELAY_l up to the I_0 term): this is box
  142's DELAY-CHARGE again, now with the exact bookkeeping. A bound DBL_l ≤ ZERO_l + 3 must show that a level cannot be late in many
  intervals unless it is also idle in about as many. Nothing in K0-K3 forbids that; the obstruction, if it exists, is on the Ξ side
  (each delayed move needs a fresh Ξ-wake, R197 WAKE-CHAIN) and on the alternation of the late mover's options (each move of x
  needs a flip of x's Ξ-comparison, R189 RE-REVERSAL).
- The R197 §4 nesting picture is the timing half: a double at level l + 1 inside a level-l interval needs room there. It does not by
  itself bound DBL, because intervals can be long when levels above keep moving.
- Data on doubles (r197/ivl.py): dbl_d3_F6 level 1 [2, 2, 2] (DBL 3, ZERO 0: the maximum 3 at the first level, since F_0 ≤ 2);
  dbl_d4_F10 level 2 [0, 2, 2, 1, 1, 2, 2] (DBL 4, ZERO 1); f2_d5_L12 level 3 [1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 2] (DBL 1, ZERO 5).
- Climbs maximising max_l (F_l − F_(l−1)) (r197/forkclimb.py SCORE=JUMP, free ladders, 100k-300k mutations) stop at exactly 4
  at d 6, 8, 12: the d 5 exact witness (6) was not found by climbing.

## 4. d 5 (EXACT, r197/liftloop.py, KF + LAG lemma clauses, FMIN = flips over steps 2..L)
| query (d 5) | meaning | result |
| --- | --- | --- |
| FMIN 2:10 at L 11 | F_2 ≥ 10 over steps 2..11 | SAT (R197 §2b; witness total F_2 = 10) |
| FMIN 2:11 at L 12 | F_2 ≥ 11 over steps 2..12 | SAT: c4x_d5_F12, total F_2 = 12 (CARRY+4 false) |
| FMIN 2:13 at L 14 | total F_2 ≥ 13 | running at the push (REL > 2.5 h) |
| FMIN 3:13 at L 14 | F_3 ≥ 13 over steps 2..14 | SAT: dd_d5_F14, F_3 = 14 = 2F_2 + 2 |
| FMIN 3:15 at L 16 | F_3 ≥ 15 over steps 2..16 | UNSAT (REL, 11503 s) |
| FMIN 3:15 at L 18 | F_3 ≥ 15 over steps 2..18 | running at the push |
- Trace of the witness (r197/trace.py): level 2 moves at t1 (v2), t2 (u2 LAG<u4, v2>), t3 (v2), t4 (u2 LAG<v1, v2, v3>), t5 (v2), t6
  (u2 LAG<u4, v2>), t7 (v2), t10 (u2 LAG<v1>), t11 (v2), t12 (u2 LAG<v2>): v2 answers carries of level 1 at once, u2 one step later,
  woken by v2 and by the levels above (u4, v3).

## 5. Files
r197/ivl.py (checks K1, K3, INTERVAL (a)-(c), FLIP-COUNT; profiles), r197/liftloop.py, r197/bmcfork.py, r197/forkclimb.py SCORE=JUMP.
check.sh block «R198».
