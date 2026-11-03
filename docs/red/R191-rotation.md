# R191 The degree-3 RE-REVERSAL escape from NEST-DEAD: the extra option buys exactly ONE key-alone move per Ξ-help (Lemma ROT-CAP, PROVED, lane, any width / degree: in a Ξ-descendant-free window a mover makes ≤ D − 1 moves, so ≤ D − 2 key-alone moves in a row; tight at D 3 / 4 / 5); the rotation k1 → k2 → k3 by key alone needs D ≥ 4; at degree 3 NEST(d) gets past R189's step-5 kill (realised prefix 6, pin) but dies at step 7 for every d ≥ 3 (Proposition NEST-DEAD-3, PROVED, lane); U stays LINEAR at d 3-8 (L-RED successor 46)
Started 2026-11-02 11:52Z (Lead brief STEP 1, date -u). Brief: «R191: the degree-3 RE-REVERSAL escape from NEST-DEAD (R190 §2). NEST-DEAD's
proof uses degree 2 in RE-REVERSAL. At degree ≥ 3 a mover can go k1 → k2 → k3 without returning. Build an acyclic IDEAL ladder of degree 3,
width 2, where that freedom lets each level respond to more than one lower carry without a re-reversal. Score U against d, at d = 3-8. If
you find compounding, realise it with REALIZE and pin it … If it stays linear, state the exact point where the extra option fails to
help, as a lemma, ideally proved.»
Labels: PROVED (lane), EXACT (z3, machine-checked, not Lean), DATA, READING, OPEN. Model: IDEAL-ACYC (P-N5-REALIZE §2; RESULTS R104 makes
every acyclic IDEAL genome a real N5 FL run from a given start pair); ladder of width 2, degree D, option k of a level-l ≥ 1 mover has
W-target 2(l − 1) + (k mod 2) (r190/delclimb format; at D = 3 options 0, 2 point at u_(l−1), option 1 at v_(l−1)). Premises used: R178
Lemma XI-NEW / consequence (ii) («Ξ is monotone»), box 144 Lemma CHAIN-BACK (score U), R189 Corollary LAG / Proposition NEST-DEAD, all
lane results quoted from their files; RESULTS R104 for realisation. Not a TARGET.md claim. G-N5-TIME OPEN. No kill.

## 0. Answer
- No compounding. The rotation the brief asks for (k1 → k2 → k3 by key alone, each move answering one lower carry) does NOT exist at
  degree 3: it needs FOUR options. Lemma ROT-CAP (§1, PROVED, lane, any IDEAL-ACYC genome, any width, any degree D): if a mover x moves
  at t_0 < t_1 < … < t_k (consecutive moves of x) and no Ξ-descendant of x moves at any step in [t_0, t_k − 1], then k ≤ D − 2. The
  option x left at t_0 counts: all k + 2 options are compared under ONE value state, s_(t_0 − 1) = … = s_(t_k − 1) on desc(x).
  - D = 2: k = 0, i.e. R189 Corollary RE-REVERSAL (every two consecutive moves need a descendant move in between).
  - D = 3: k ≤ 1. Between two Ξ-helps a mover answers at most ONE lower carry by key alone. This is the exact point where the extra
    option stops helping: it turns «a help per move» into «a help per two moves», a constant factor, not a compounding.
  - Corollary ROT-BUDGET: moves(x) ≤ (D − 1)(1 + H_x), H_x := #steps at which some Ξ-descendant of x moves.
  - Tight (DATA, r191/rotclimb.py maximising the longest key-alone run): max run 1 / 2 / 3 at D = 3 / 4 / 5 (d 3, w 2); every climbed
    or pinned degree-3 genome has max run ≤ 1 (r191/altck.py, 0 violations of ROT-CAP and of Lemma KEY-ALT on 25 genomes).
- Lemma KEY-ALT (§1, PROVED, lane, width 2, any degree): a key-alone move (no Ξ-descendant move since the previous move) happens at a
  step where R_(l−1) (the key ranking of the two level-(l − 1) movers) flips, switches the W-target of x, and lands on the key-smaller
  lower mover L_(l−1). At D = 3 a key-alone pair is (0 or 2) → 1 or 1 → (2 or 0).
- NEST(d) at degree 3 (§2). R189's step-5 contradiction is gone: the climb realises NEST(3)'s first SIX steps exactly at degree 3
  (pin nest3_D3_p6_n84; degree 2: 4, as z3 (R189)). Lemma NEST-PI (PROVED, lane, d ≥ 3; (iii) needs degree ≤ 3): a NEST(d) prefix of 7 steps forces
  π(v_j) < π(q) for every j ≤ d − 2, π(q) < π(p) and π(p) < π(u_(d−2)) (q = v_(d−1), p = u_(d−1)).
- Proposition NEST-DEAD-3 (§2, PROVED, lane): for every d ≥ 3 and degree ≤ 3, no width-2 IDEAL-ACYC ladder realises NEST(d)'s first
  SEVEN steps. Proof by Lemma MERGE-1 (a step that moves a single mover y changes a comparison of two faces only if exactly one of
  their chains contains y, and that one gains): b = v_(d−2)'s two moves (steps 3, 7) are both woken by q alone, so the chain of b's
  middle option must contain q at state 1 and not at state 5; the only mover that can re-route it is c = v_(d−3) (moving at 5), and
  c's own move at 5, woken by q alone at 4, needs the chain of c's OLD option to avoid q, which it does not. Degree enters only through
  NEST-PI (iii) (π(p) < π(u_(d−2)), from ROT-CAP); at degree ≥ 4 the proof does not close (OPEN). z3 (relaxation and exact) did not
  decide prefix 7 within 3600 s; the proof replaces it. MERGE-1 checked on 41 runs (U champions, NEST climbs, pins, R188 / R189
  genomes): 0 violations (r191/mergeck.py).
- U against d (§3, DATA, climbs scoring box 144's U, 100k mutations, 3 seeds): best U 6 / 9 / 16 / 16 / 22 / 21 at d = 3 / 4 / 5 / 6 /
  7 / 8 (width 2, degree 3); ≈ 2.7 per level; width 2 / degree 2 (R190): 10 at d 6, 14 at d 10. Linear (DATA). Champion u_d8_D3 (U 21,
  L 24) realised and pinned.

## 1. ROT-CAP, ROT-BUDGET, KEY-ALT (PROVED, lane)
Notation. s_t = state after step t (s_0 = start). desc(x) = movers Ξ-reachable from x over all options. V_t(x) = the values of x's faces
under s_t; they depend only on s_t restricted to desc(x) (a face's chain is (x, k), (xt, s(xt)), …, all in desc(x)). x moves at step t to
the key_t-least option of A_(t−1)(x) := {s_(t−1)(x)} ∪ {k : face(x, k) ▷ face(x, s_(t−1)(x)) under V_(t−1)} (the IDEAL rule, r187/ideal.py:
availability read at state t − 1, keys at state t).
- Lemma ROT-CAP. Let x move at t_0 < t_1 < … < t_k, with no move of x strictly between, and suppose no mover of desc(x) moves at any step
  in [t_0, t_k − 1]. Then k ≤ D − 2, D := deg(x).
  - Proof. No desc(x) move at steps t_0, …, t_k − 1 gives V_(t_0 − 1) = V_(t_0) = … = V_(t_k − 1) =: V. Let o_(−1) := s_(t_0 − 1)(x) and
    o_i := s_(t_i)(x). At step t_i, x moves from o_(i−1) to o_i ∈ A_(t_i − 1)(x), o_i ≠ o_(i−1), so o_i ▷_V o_(i−1) (availability is a
    strict improvement under V_(t_i − 1) = V). Hence o_(−1) ◁ o_0 ◁ … ◁ o_k under the single order ▷_V (values are distinct sets, no
    ties), so these k + 2 options are distinct and k + 2 ≤ D. ∎
  - Remark. The point is the opening move: its target o_0 already beats o_(−1) under V, so the window starts one option «up». At D = 2
    this is R189 RE-REVERSAL; R190 §1 counted D − 1 key-alone moves because it left o_(−1) out.
- Corollary ROT-BUDGET. moves(x) ≤ (D − 1)(1 + H_x). Proof: cut x's move sequence between t_i and t_(i+1) whenever some desc(x) mover
  moves in [t_i, t_(i+1) − 1]; distinct cuts use distinct steps (the windows [t_i, t_(i+1) − 1] are disjoint), so there are ≤ H_x cuts,
  and each piece has ≤ D − 1 moves by ROT-CAP. ∎ (Exponential in the π-depth in general: the last mover in π moves ≤ D − 1 times, the
  bound may multiply by ~D per π-position. It is a budget, not a polynomial bound.)
- Lemma KEY-ALT (width 2). Let x (level l ≥ 1) move at t_1 < t_2 (consecutive moves) with no desc(x) move in [t_1, t_2 − 1]. Then
  (a) R_(l−1)(s_(t_2)) ≠ R_(l−1)(s_(t_2 − 1)) (the key ranking of u_(l−1), v_(l−1) flips AT step t_2), (b) the W-targets of s_(t_1)(x)
  and s_(t_2)(x) differ, (c) the new W-target is L_(l−1)(s_(t_2)) (the key-smaller one).
  - Proof. Let o = s_(t_1)(x), n = s_(t_2)(x), V as in ROT-CAP. For t ∈ (t_1, t_2], A_(t−1)(x) = {o} ∪ {k ▷_V o} =: A′, and
    A′ ⊆ A_(t_1 − 1)(x) (o ▷_V s_(t_1 − 1)(x)). The key order on x's options is: options pointing at L_(l−1) first, each W-class
    ordered by the fixed gates (key(x, k) = key(W-target) · gate, and key(u_(l−1)) ≠ key(v_(l−1))). At step t_2 − 1 (if t_2 − 1 > t_1;
    else at t_1, over the superset A_(t_1 − 1)) x chose o as key-least of a superset of A′ ∋ n; at t_2 it chooses n ≠ o from A′. So
    the key order of o, n differs between s_(t_2 − 1) (resp. s_(t_1)) and s_(t_2). Within one W-class the order is fixed, so o, n are
    in different classes (b), the class order flipped (a), and n's class is first at s_(t_2) (c). (In the case t_2 = t_1 + 1 the flip is
    between s_(t_1) and s_(t_2) = s_(t_1 + 1): again at step t_2.) ∎
  - So a key-alone move answers a flip of R_(l−1) at the same step, and needs a mover of level ≤ l − 1 to move at that step.
  - At D = 3 (classes {0, 2} → u_(l−1), {1} → v_(l−1)): consecutive key-alone moves would alternate classes and climb in ▷_V; by
    ROT-CAP there is at most one, so a degree-3 «rotation» is a helped move followed by one key-alone move: (0|2) → 1 or 1 → (0|2).
- Checks (DATA): r191/altck.py tests (a)-(c) and ROT-CAP on every pair of consecutive moves without a descendant move in between:
  0 violations on the 18 U-climb champions (d 3-8), 4 NEST climbs, the 3 pins, R188 x3_L8 / g4_L12, R189 lag1 / lag1u / lag2c_d4 /
  nest_d3_L4. r191/pathck.py checks Ξ-monotonicity (every face value non-decreasing, step by step) and the path-count consequence
  moves(x) ≤ V(x) − 1 ≤ P(x) − 1 (V(x) := number of distinct values of x's current face, P(x) := Ξ-paths from x to the exit counted
  over options; V(x) ≤ Σ_k V(xt(x, k)) since x's current value is β(x, k) ⊕ the current value of xt(x, k)): 0 violations; far from
  tight (u_d8_D3: 52 moves against Σ(P − 1) = 2906), so the path count does not bound runs polynomially by itself.

## 2. NEST(d) at degree 3
- Schedule NEST(d) as R189 §2 (r189/lag/schedbmc.nest; at d 3: [0,2,4], [5], [3,4], [5], [1,2,4], [5], [3,4], [5]). u_l moves at the
  steps t ≡ 1 mod 2^(d−l), v_l at t ≡ 1 + 2^(d−l−1) mod 2^(d−l); so every even step moves q = v_(d−1) alone, p = u_(d−1) moves at every
  odd step, and no level below l moves when v_l moves.
- R189 NEST-DEAD step (3) (p moves at 3 and 5 with no descendant move in [3, 4]) is no contradiction at D = 3: the pair (3, 5) is one
  key-alone move (KEY-ALT: R_(d−2) flips at 5 when u_(d−2) moves). Realised (DATA, r191/nestclimb.py, score = longest matched prefix):
  degree 3 matches 6 of NEST(3)'s 8 steps (4 seeds; one more seed with π forced as below: 6); degree 2 matches 4 (2 seeds), as z3
  (R189: prefix 5 UNSAT). Pin nest3_D3_p6_n84 (genome r191/lag/nest3_D3_p6.json): p visits 0 → 1 → 2 at steps 3, 5 (key-alone at 5);
  q visits 1 → 0 → 1 → 2.
- Lemma NEST-PI (PROVED, lane; d ≥ 3; (i), (ii) any degree, (iii) degree ≤ 3; a run whose first 7 steps move exactly NEST(d)'s sets).
  - (i) π(v_j) < π(q) for every j ≤ d − 2. v_j moves at a step t with no lower-level move at t (so its key order is that of t − 1) and
    did not move at t − 1, so A_(t−1)(v_j) ≠ A_(t−2)(v_j): a desc(v_j) mover moved at t − 1 (Corollary LAG). t − 1 is even, and only q
    moves at even steps. (For the first 7 steps: v_(d−2) at 3, v_(d−3) at 5.)
  - (ii) π(q) < π(p): R189 NEST-DEAD step (2) (degree-free: Corollary LAG).
  - (iii) π(p) < π(u_(d−2)). p moves at 3, 5, 7. Steps 3, 4 move only v_(d−2), p, q, none in desc(p) by (i), (ii); so (3, 5) is
    descendant-free and by ROT-CAP (D ≤ 3: k ≤ 1) some desc(p) mover moves at step 5 or 6. Step 6 moves only q; step 5 moves v_(d−3),
    u_(d−2), p (d ≥ 4; at d 3: v_0, u_1, p), and v_(d−3) ∉ desc(p) by (i). So u_(d−2) ∈ desc(p). ∎ (iii) uses D ≤ 3; (i), (ii) do not.
  - Not forced: the order of u_(d−2) against lower u_j (u_1 moves only twice in NEST(d)), nor u_0's position at d 3.
- Lemma MERGE-1 (PROVED, lane; the one-mover case of box 144's merge observation). If exactly one mover y moves at step t, then for any
  mover x and options k, k′ the comparison of face(x, k) and face(x, k′) differs between V_(t−1) and V_t only if exactly one of the two
  chains under s_(t−1) contains y, and then the face whose chain contains y is the one that gains.
  - Proof. Chains under s_(t−1) and s_t agree up to y (no other mover moves). A chain without y keeps its value. A chain with y is
    P ∪ C(y) with P its part before y (movers π-before y) and C(y) the chain of y's current face (movers π-after y), so its value is
    w(P) + w(C(y)) in the translation-invariant order (signed weight, then −length). If both contain y, the difference w(P) − w(P′) does
    not change. If one does, it changes by cur_t(y) − cur_(t−1)(y) ▷ 0 (y moves to a face that is strictly better under s_(t−1), and Ξ
    is monotone, R178 (ii)). ∎
- Proposition NEST-DEAD-3 (PROVED, lane). For every d ≥ 3 and degree D ≤ 3, no width-2 IDEAL-ACYC ladder has a run whose steps 1-7
  move exactly NEST(d)'s sets. Write b = v_(d−2), q = v_(d−1), p = u_(d−1), a = u_(d−2), c = v_(d−3). NEST(d)'s steps 1-7 are
  {u_0, …, u_(d−1)}, {q}, {b, p}, {q}, {c, a, p}, {q}, {b, p}.
  - Proof. By NEST-PI (ii), (iii) (D ≤ 3 enters here, through ROT-CAP): π(q) < π(p) < π(a).
    - (1) b moves at 3 (c₀ → n) and at 7 (n → m) and not at 4-6. Levels < d − 2 do not move at steps 2-4 or 6-7, so b's key order is the
      same at s_1, s_2, s_3 and at s_5, s_6, s_7. As in Corollary LAG: n ∈ A_2(b) \ A_1(b) and m ∈ A_6(b) \ A_5(b). Only q moves at
      steps 2 and 6, so by MERGE-1 the chain of (b, n) contains q under s_1 and does NOT contain q under s_5 (at step 6 the gaining face is
      (b, m), so (b, m) contains q and (b, n) does not).
    - (2) So some mover on the s_1-chain of (b, n) strictly before q moved during steps 2-5 (else the s_5-chain follows the same prefix
      to q). Such a mover has π strictly between π(b) and π(q). The movers of steps 2-5 are q, b, p, c, a; p and a are π-after q, and the
      chain starts at b with b's option fixed. So it is c, and c lies on the s_1-chain of (b, n) before q. Let c_old := s_4(c) (c moves at
      5 only). The part of that chain from c to q is c's current chain under s_1, so the chain of (c, c_old) contains q under s_1; its
      movers between c and q are π-between c and q, and none of them moves at steps 2-3 (those are q, b, p; b is π-before c), so the chain
      of (c, c_old) contains q under s_3 too.
    - (3) c moves at 5 (c_old → c′) and not at 4; levels < d − 3 do not move at steps 4-5, so c's key order is the same at s_4 and s_5,
      and c′ ∈ A_4(c) \ A_3(c). Only q moves at step 4, so by MERGE-1 the chain of (c, c′) contains q under s_3 and the chain of
      (c, c_old) does not. This contradicts (2). ∎
  - Degree enters only through NEST-PI (iii) (π(p) < π(a)), which excludes a = u_(d−2) (it moves at 5) from the prefix in (2). At D ≥ 4
    ROT-CAP allows p's moves at 3, 5, 7 in one descendant-free window, (iii) is not forced, and the proof does not close.
  - It is the second NEST-DEAD: R189's kills NEST(d) at step 5 for D = 2; this one at step 7 for D = 3. Consistent with the data
    (climbs: 6 at D 3, 4 at D 2) and with z3 (table).
- Exact status of step 7 (z3, r191/nestbmc.py = r190/clockbmc.py + PIFIX, which adds exactly (i)-(iii); REL = free distinct integer
  weights, a relaxation: its UNSAT is an upper bound):

| d 3, w 2, D 3 | prefix 6 | prefix 7 | full 8 |
| --- | --- | --- | --- |
| REL, π free | SAT (fast) | timeout 3600 s | (stopped) |
| REL, PIFIX | — | timeout 3600 s | timeout 3600 s |
| exact, PIFIX | — | timeout 5400 s | — |
| exact, PIFIX + LEM (lemma clauses) | SAT, 223 s | timeout 5000 s | — |
- So the prefix-7 question is settled by the proof, not by z3 (UNSAT expected by NEST-DEAD-3; any SAT answer would be a bug in one of
  them and is to be reported).
- Consistent with the climbs: they reach p's 4th move at step 7 but never b's (seed 2: step 7 moves {u_0, p}); 9 seeds stop at ≤ 6.
- Degree 4 (DATA, not covered by the proof): nestclimb d 3 D 4, 3 seeds × 300,000 mutations: 6 / 6 / 6, also stuck at step 7.

## 3. DATA: U against d (r190/delclimb.py SCORE=U; width 2, degree 3; 100,000 mutations; seeds 1-3)

| d | U (seed 1 / 2 / 3) | L (seed 1 / 2 / 3) | best U |
| --- | --- | --- | --- |
| 3 | 6 / 6 / 6 | 7 / 7 / 8 | 6 |
| 4 | 7 / 8 / 9 | 10 / 11 / 11 | 9 |
| 5 | 14 / 11 / 16 | 16 / 13 / 19 | 16 |
| 6 | 15 / 14 / 16 | 16 / 15 / 24 | 16 |
| 7 | 17 / 22 / 18 | 20 / 25 / 20 | 22 |
| 8 | 20 / 21 / 18 | 23 / 24 / 21 | 21 |
- Reading: additive, ≈ 2.7 per level (width 2 / degree 2, R190: U 10 at d 6, 14 at d 10; width 3 / degree 3: 22 at d 6, 34 at d 10).
  Degree 3 at width 2 sits between. No doubling of U or L at any level (per-level U ≤ 5 everywhere).
- Key-alone moves are rare in U-champions: 1-6 per run, against 4-30 helped consecutive pairs (altck): the climbs win U with helped
  (Ξ-woken) moves, as box 144 says.
- Pins (r191/instances, pins.sha1; built by r187/stab.py PAD 1; each: lemck 0 violations, startck, Oink --zlk + verify, --tl + verify,
  xeng):

| pin | genome | n | L_FL | what |
| --- | --- | --- | --- | --- |
| nest3_D3_p6_n84 | r191/lag/nest3_D3_p6.json | 84 | 6 | NEST(3) prefix 6 at degree 3 (past NEST-DEAD's step 5) |
| rot_d3_D4_n108 | r191/lag/rot_d3_D4.json | 108 | 8 | degree 4: a key-alone run of 2 (ROT-CAP tight at D 4) |
| u_d8_D3_n214 | r191/lag/u_d8_D3.json | 214 | 24 | U champion d 8 (U 21) |

## 4. READING / OPEN
- Where the degree-3 freedom goes: each Ξ-help now buys two moves instead of one (ROT-BUDGET with D − 1 = 2), so every bound of the
  form «moves ≤ c · (helps)» doubles its constant. A counter needs the helps themselves to double per level, which is the Ξ side
  (box 144's U), not the key side. The key side is capped by ROT-CAP at every degree: k ≤ D − 2 key answers per help.
- For degree D growing with n, ROT-CAP allows D − 2 key-alone answers per help; a counter that answers 2^l lower carries by key would
  need D ≥ 2^l + 1 at level l, i.e. exponential degree (READING; the ladder's degree is part of the instance size).
- OPEN: NEST(d) at degree ≥ 4 (NEST-DEAD-3's step (2) needs π(p) < π(u_(d−2))); other doubling schedules at degree 3 (NEST-DEAD-3
  kills one schedule, like R189); a proof of U-LIN (box 144 CONJECTURE) at width 2 and fixed degree.

## 5. Files (experiments/red/r191/)
- altck.py (KEY-ALT / ROT-CAP checker), mergeck.py (MERGE-1 checker), pathck.py (monotonicity + path-count checker), rotclimb.py (longest key-alone run),
  nestclimb.py (NEST prefix climb; PI=nest forces an order stronger than NEST-PI, used for one seed only, DATA), nestbmc.py (z3, copy of
  r190/clockbmc.py with PIFIX = NEST-PI), lag/*.json (genomes), instances/ (3 pins + pins.sha1). Outputs in r191/out are container-local
  (gitignored). check.sh block «R191».
