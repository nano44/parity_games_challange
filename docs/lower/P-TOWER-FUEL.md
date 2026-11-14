# P-TOWER-FUEL: room and fuel for a further doubling level on 2-wide ladders (L-LOWER successor 5) — FROZEN

Status: FROZEN 2026-11-07 (date -u, at the commit that adds this file). Lead ruling 12:36Z (BOX L5 sub-box (b)). For REFEREE and
REFEREE-2. Author's lane notes: docs/lower/L5-rule.md (history, not part of the packet). Labels: PROVED (the statements of §2, proofs
below, premises §1 only) / DATA (§4, §5, each with its counter) / READING. Nothing here bounds T polynomially; G-N5-TIME stays OPEN;
not a TARGET.md claim (§7). Line L-1: docs/lower/P-TOWER-FUEL-line-L1.txt. Check block: experiments/lower/l5/p_tower_check.py (run by
experiments/lower/check.sh).

## 1. Premises (LANDED RESULTS only) and notation
- RESULTS R104: its definition of the IDEAL model only (A-sets under the old state; new options level by level, lowest first, the
  key-least option of the A-set under the new state; the run stops when nothing changes). No theorem of R104 is used.
- RESULTS R105: ENC only («the Ξ-order of β-sets is the order of the integers Σ ±2^rank (+ for even parity), so … the value of option
  (x, k) is ε(x, k) plus the current value of its Ξ-target»; ranks are distinct).
- RESULTS R110: its definition of 𝓛^R_d only (movers 2l, 2l + 1 on level l = 0, …, d − 1, degree 2, option k of a mover of level l ≥ 1
  W-points to mover 2(l − 1) + k).
- RESULTS R113: ALIGN only, with its notation c_l(s), γ_l(j), flip, F(l) («on 𝓛^R_d, for 1 ≤ l ≤ d − 1 and every state s of a run,
  both movers 2l and 2l + 1 have KP_s = c_l(s), each of them that moves at step t moves to option c_l(s_t), and the order of their keys
  under s is [s(2l) = c_l(s)] if s(2l) ≠ s(2l + 1) and γ_l(j) if both are on option j»), on acyclic Ξ-graphs.
- Not used: R116 (listed by the Lead as available; not needed), any «signed, not landed» item, R119 / P-IDEAL-DBL (DBL-EQ, WINDOW-ONCE),
  L-SI's PULSE-NEST and L-LOWER's DOUBLE-EQ′ / FROZEN-WINDOW (lane): what is needed of them is re-proved here (Lemmas 1, 2).
- Notation. A run s_0, …, s_T (G ∈ 𝓛^R_d, Ξ-acyclic, any start). o_l(s) ∈ {0, 1} := the index of the key-smaller member of pair l
  (2l, 2l + 1) under s, so c_(l+1)(s) = o_l(s) (R113's definition of c). For 1 ≤ j ≤ d − 1: a j-b-step is a step t with c_j(s_t) ≠
  c_j(s_(t−1)) (equivalently a flip of pair j − 1); a j-window is a maximal set of consecutive steps of [1, T] containing no j-b-step
  except possibly its first (the j-windows partition [1, T]; c_j(s_t) is constant on each). Level j is DOUBLING if F(j) = 2F(j − 1) + 2.
  For a doubling level j and a j-window W in which each member of pair j moves exactly once (Lemma 1 (E4)): u₁(W) < u₂(W) the two move
  steps, f(W), x₂(W) the movers, PULSE(W) := u₂(W) − u₁(W); for consecutive such windows W, W⁺: GAP(W) := u₁(W⁺) − u₂(W).
  cv_s(z) := the value of z's current option (ENC); v_s(x, k) := ε(x, k) + cv_s(xt(x, k)) (cv of the exit X is 0); π_s(x) := the option
  of x of larger value under s. chain_s(x, k) := the set of options on the Ξ-path from (x, k) under s (each at most once: acyclic).

## 2. Statements (PROVED, from §1)
- Lemma 0 (MOVE). On 𝓛^R_d, a mover x of level l ≥ 1 moves at step t iff its other option is strictly better under s_(t−1) and c_l(s_t)
  ≠ s_(t−1)(x); it then moves to c_l(s_t).
- Lemma 1 (DOUBLE-EQ, re-proved from ALIGN). If level j (1 ≤ j ≤ d − 1) is doubling, with Φ(t) := #{x ∈ pair j : s_t(x) ≠ c_j(s_t)}:
  (E1) Φ(0) = 2, Φ(T) = 0; (E2) Φ(t − 1) = 0 at every j-b-step t; (E3) no step moves both members, and pair j flips exactly at the steps
  that move a member; (E4) in every j-window each member moves exactly once; (E5) if F(j − 1) ≥ 1, the first mover f is the same member
  in every j-window (and γ_j(0) = γ_j(1)).
- Lemma 2 (PULSE-NEST, re-proved; first proved in L-SI 42's lane). If levels j, j + 1, …, j + k are doubling (k ≥ 0, j + k ≤ d − 1),
  every j-window has PULSE ≥ k + 1.
- Lemma 3 (GAP-NEST). If levels j, …, j + k are doubling with k ≥ 1, then GAP(W) ≥ k + 1 for consecutive j-windows W, W⁺. Hence with
  levels 0, …, h − 1 capped (F(l) = 2^(l+2) − 2), PULSE and GAP of every j-window are ≥ h − j for 1 ≤ j ≤ h − 2.
- Lemma 4 (DOMINANCE-FREEZE). For a mover x and a state s let dec_s(x) := (m, k), where m is the option of largest rank in chain_s(x, 0)
  △ chain_s(x, 1) and k ∈ {0, 1} the side containing it. (a) π_s(x) is determined by dec_s(x) (π = k if m has even parity, 1 − k if
  odd); so if dec is constant on a set of states, so is π. (b) If x is a member of pair j, level j doubling, and t < t′ are consecutive
  moves of x, then dec(x) is not constant on s_(t−1), …, s_(t′−1).
- Lemma 5 (CROSS-ECONOMY). Let level j be doubling and pair j CROSS onto two movers A_0 ≠ A_1 outside pair j: xt(2j, k) = A_k = xt(2j +
  1, 1 − k). Put D_s := cv_s(A_0) − cv_s(A_1), θ_(2j) := ε(2j, 1) − ε(2j, 0), θ_(2j+1) := ε(2j + 1, 0) − ε(2j + 1, 1). (i) π_s(2j) = 0 iff
  D_s > θ_(2j); π_s(2j + 1) = 1 iff D_s > θ_(2j+1) (each member prefers its A_0-side iff D_s exceeds its threshold). (ii) In every
  j-window: [D(s_(u₁−1)) > θ_f] ≠ [D(s_(u₂−1)) > θ_(x₂)]. (iii) If at s_(u₁−1) and at s_(u₂−1) the largest rank in chain(A_0) △ chain(A_1)
  exceeds the ranks of the four options of pair j (RANK hypothesis), then D changes sign between s_(u₁−1) and s_(u₂−1): the shared
  comparison must change sign inside every pulse, and nothing else is required of it there.

## 3. Proofs
- Lemma 0. Degree 2: A_(s_(t−1))(x) is {s_(t−1)(x)} or both options (the other one iff strictly better under s_(t−1), R104). The new option
  is the key-least option of the A-set under s_t; by ALIGN the key-least option of x under s_t is c_l(s_t). So if the A-set has both
  options the new option is c_l(s_t), otherwise s_(t−1)(x). ∎
- Lemma 1. Write c_t := c_j(s_t) and ord_t := the key order of pair j under s_t, which ALIGN gives as a function of s_t(2j), s_t(2j + 1),
  c_t and γ_j; a flip at t is ord_t ≠ ord_(t−1). Movers land on c_t (Lemma 0). At a non-b-step (c_t = c_(t−1)) a flip needs a mover (the
  ALIGN expression then changes only through the pair's states), and every mover lowers Φ by 1; so flip_t ≤ Φ(t − 1) − Φ(t), with equality
  iff no mover, or exactly one mover and a flip. At a b-step with a := Φ(t − 1) and r movers (movers were not on c_t; non-movers toggle
  alignment): Φ(t) = 2 − a − r, and the case analysis of the ALIGN expression gives flip_t − (Φ(t − 1) − Φ(t)) = h(a, r) with h(0, 0) = 2
  (both on c_(t−1) before and after: order γ_j(c_(t−1)) unchanged, no flip), h(0, 1) ≤ 2, h(0, 2) ≤ 1, h(1, 0) = 1, h(1, 1) ≤ 0, h(2, 0) = −2
  (no flip). Summing over t: F(j) ≤ Φ(0) − Φ(T) + Σ_(b-steps) h ≤ 2 + 2F(j − 1) (F(j − 1) b-steps, h ≤ 2). Equality (doubling) forces
  Φ(0) = 2, Φ(T) = 0 (E1), equality at every non-b-step, and h = 2 at every b-step, i.e. a = 0 there (E2) and r ≤ 1, with a flip if r = 1.
  (E3): a b-step with a = 0, r = 0 has no flip; with r = 1 it has one; a
  non-b-step flips iff exactly one member moves; two simultaneous movers at a non-b-step would give flip ≤ 1 < 2 = Φ-drop, violating
  equality; at a b-step a = 0 forces r ≤ 1 (h(0, 2) ≤ 1 < 2). (E4): inside a window c is constant; right after its opening b-step Φ = 2
  (r = 0) or 1 (r = 1), and Φ(0) = 2 for the first window; Φ must be 0 before the next b-step and at T (E1, E2); each move lowers Φ by 1,
  and a member that has moved is on c and cannot move again while c is constant (Lemma 0). (E5): in a window with value c′, before its
  first move the pair is together on w = 1 − c′ (Φ = 2 there, using (E2) at the opening b-step); the first move must flip (E3): the order
  goes from γ_j(w) to [first mover is 2j]; the second move must flip: [first is 2j] → γ_j(c′). So [first is 2j] = ¬γ_j(w) and γ_j(c′) =
  γ_j(w). Consecutive windows have different c′; if F(j − 1) ≥ 1 there are two windows, so γ_j(0) = γ_j(1) and the first mover is the
  same member in every window. ∎ (This is the proof of L-LOWER 4's DOUBLE-EQ′, docs/lower/L4-tower.md §3, from ALIGN only.)
- Lemma 2. Induction on k. k = 0: (E4) and (E3) give two moves at distinct steps. k ≥ 1: by (E3) at level j the (j + 1)-b-steps are
  exactly the steps that move a member of pair j, i.e. the steps u₁(V), u₂(V) over all j-windows V. Hence W′ := [u₁(W), u₂(W) − 1] is a
  (j + 1)-window. Levels j + 1, …, j + k are doubling, so by the induction hypothesis (k − 1, base j + 1) its two pair-(j + 1) moves are ≥ k
  steps apart and lie in W′, so PULSE(W) = |W′| ≥ k + 1. ∎
- Lemma 3. By (E3) at level j, [u₂(W), u₁(W⁺) − 1] is a (j + 1)-window (it starts at a move of pair j, and the next move of pair j is
  u₁(W⁺)). Levels j + 1, …, j + k are doubling, so by Lemma 2 (base j + 1, k − 1) its two pair-(j + 1) moves are ≥ k steps apart and lie
  in it; its length u₁(W⁺) − u₂(W) is ≥ k + 1. For h capped levels take k = h − 1 − j. ∎
- Lemma 4. (a) ENC: v_s(x, 0) − v_s(x, 1) = Σ_(m ∈ chain(x,0) \ chain(x,1)) ε(m) − Σ_(m ∈ chain(x,1) \ chain(x,0)) ε(m), ε(m) = ±2^rank(m)
  with distinct ranks, so the sign is that of the term of largest rank, i.e. fixed by dec_s(x). (b) By (E4) x moves exactly once in each
  j-window, so consecutive moves t < t′ lie in consecutive j-windows, whose values c_j differ (a window boundary is a change of c_j).
  By Lemma 0 x moves to c_j(s_t) at t and to c_j(s_(t′)) = 1 − c_j(s_t) at t′, and at each move the new option is strictly better under
  the previous state: π_(s_(t−1))(x) = s_t(x) ≠ s_(t′)(x) = π_(s_(t′−1))(x). By (a), dec cannot be constant on s_(t−1), …, s_(t′−1). ∎
- Lemma 5. (i) ENC: v_s(2j, 0) − v_s(2j, 1) = ε(2j, 0) − ε(2j, 1) + D_s and v_s(2j + 1, 1) − v_s(2j + 1, 0) = ε(2j + 1, 1) − ε(2j + 1, 0) +
  D_s. (ii) In a window with key c: by Lemma 0, π_(s_(u₁−1))(f) = c and π_(s_(u₂−1))(x₂) = c. Member 2j's option c is its A_c-side,
  member 2j + 1's option c is its A_(1−c)-side; f and x₂ are the two different members, so at u₁ − 1 the first prefers the A_c-side and
  at u₂ − 1 the second prefers the A_(1−c)-side; with (i): [D(s_(u₁−1)) > θ_f] = [c = 0] ≠ [c = 1] = [D(s_(u₂−1)) > θ_(x₂)] (for f = 2j;
  the case f = 2j + 1 is symmetric). (iii) Under the RANK hypothesis at s, |D_s| ≥ 2^(rank of the top element) > 2·max(|θ_(2j)|, |θ_(2j+1)|)
  (each θ is a difference of two terms of rank below it), so [D_s > θ_(2j)] = [D_s > θ_(2j+1)] = [D_s > 0]; with (ii) the signs of D at
  s_(u₁−1) and s_(u₂−1) differ. ∎

## 4. The two obstruction instances (DATA; genomes in the R110 text format d / xt / br / bp / gate / start; stored start; checked by
## p_tower_check.py §(2))
- I-ROOM: experiments/lower/l4/rec/G7_best_d28.txt (sha1 b995fff21c1f8558eb3e1868ec5ce59a3d4ccfb3; L-LOWER 4's seventh-level warm
  start; d 28; start 11110011110011000111100110010001000101011001000100001100). T 270, F = 2 6 14 30 62 126 222 158 …: levels 0-5
  capped, level 6 not doubling (222 < 254). Against the conditions of Lemmas 2, 3 for SEVEN capped levels (PULSE, GAP ≥ 7 − j, j = 1..5):
  0 violations at levels 1-4; 30 at level 5: 15 pulses and 14 gaps of length 1 in the 5-windows opened by mover 9 moving to option 1,
  plus 1 pulse of the first 5-window (unit = 5-window; set = all 63 5-windows; scope = stored start). Level 6: 48 of its 127 6-windows do
  not have one move of each member of pair 6. So by Lemmas 2, 3, seven capped levels need a run that differs from this one at level
  5 in those windows (room); the instance is DATA, the conditions are Lemmas 2, 3.
- I-FUEL: experiments/lower/l5/rec/SL41_d28.txt (sha1 c1b46c319fd614e5bcb0909b616a9f2833e0dfee; from I-ROOM by a climb scoring the
  Lemma 2/3 conditions, L5-rule §6; d 28; start 11110011110011000111110111010110001111111000010111100110). T 290, F = 2 6 14 30 62 126 222 158 …:
  levels 0-5 capped; 0 violations of PULSE, GAP ≥ 7 − j at levels 1-5 (unit = j-window; set = all windows of levels 1-5; scope =
  stored start); still 48 of 127 6-windows fail. Pair 6 is CROSS onto (22, 11) (12 → (22, 11), 13 → (11, 22)), so Lemma 5 applies to it
  as soon as level 6 doubles. In all 48 failing 6-windows the deciding element (Lemma 4) of 12 or 13 is option 19 = (mover 9, option 1),
  rank 87, odd parity, on 11's chain (11 → 9), and in none of the 79 other 6-windows (unit = 6-window; set = all 127; scope = stored
  start). So the room conditions are met and the missing piece is fuel: Lemma 4 (b) is violated in exactly those windows by a parked
  β of the capped pair 4.
- Not claimed: that the plateau F(6) = 222 is a cap (lane DATA, L5-rule §6: 166 single edits at the dominator, 2,970 single re-targets in
  pair 6's Ξ-closure, 144,011 two-edit genomes; none above 222 with six capped levels); any statement about T^R(d) or S(h).

## 5. DATA for §2 (p_tower_check.py §(3); unit and set per counter; scope = stored start of 24 runs: experiments/lower/l3/kill/*.json
## (15), experiments/lower/l4/rec/*.json (7), I-ROOM, I-FUEL; 62 doubling levels, 757 j-windows)
- Lemma 0: no separate DATA (it is how the simulator moves). Lemma 1: E3 0 violations (unit = step × doubling level), E4 0 (unit =
  j-window, 757), E5 0 (unit = doubling level, 62). Lemma 2: 0 violations on 757 j-windows (k = number of further doubling levels), bound
  attained on 215. Lemma 3: 0 violations on 260 (window, next window) pairs with k ≥ 1, attained on 12. Lemma 4 (a): 0 violations on
  65,885 (consecutive-state, mover) pairs with equal deciders; (b): 0 on 1,390 (member, consecutive-move pair) units. Lemma 5: 4 CROSS
  doubling pairs in the corpus (REC_d10_tower_mu30 level 3, REC_d12_mu42 level 6, REC_d9_mu29 level 6, RECF4_d20_F60 level 3), (ii) 0
  violations on their 65 windows, (iii) RANK hypothesis at both states in 43 of them, 0 violations.
- Simulators: l3/sim.py (the check), fev.c (experiments/lower/l5, core of l4/rclimb.c), utmpl.c's exact-order simulator: identical T
  and F on I-ROOM and I-FUEL; L-NEW's box150 Gen (claude/l-new ae8e185d) via l3/xcheck.py: SIM-MISMATCH 0, movescheck counters 0 on both.

## 6. Machine check
- experiments/lower/l5/p_tower_check.py (< 5 s): pins the two instance sha1s and the line file, re-derives every count of §4 and every
  counter of §5 and asserts them exactly; prints «P-TOWER-FUEL CHECK PASS». Run by experiments/lower/check.sh (scripts/verify.sh).

## 7. Diff against TARGET.md
No statement mentions a parity game, a winning region, an algorithm's running time or a complexity class; all are about the IDEAL
model's step sequence (R104's definition) on 𝓛^R_d. Not M3, not a gauntlet step; G-N5-TIME stays OPEN.
