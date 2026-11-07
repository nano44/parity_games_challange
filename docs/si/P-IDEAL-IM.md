# Packet P-IDEAL-IM (box 75): improvement monotonicity (IM) in the IDEAL model; the BIT-CHAIN form of R110's c-step (KEY-DIR); value monotonicity across bit changes (VALUE-MONO); COMPOSE; the IM frame and the theorem that every ISO genome of 𝓛^R_(m+1) maps into it (FRAME); MACHINE: T_1(3) = 10
L-SI successors 39-40, frozen 2026-11-06 (date -u: see the commit). Lead brief BOX 75 (2026-11-06 14:13Z). Sources: docs/si/N5-MECH-box69.md
§1 (Lemma IM), docs/si/N5-FLIPOR-box64.md §2 (BIT-CHAIN, FLIP-PATH), docs/si/N5-REFUTE-box68.md §1 (COMPOSE), docs/si/N5-FRAME-box70.md
§0-§1 (the frame), docs/si/N5-SUM1-box73.md §1 (KEY-DIR). Every proof is written out in full HERE, and this packet governs.

Not a TARGET.md claim. No polynomial bound. G-N5-TIME, FLIP-ADD, PAIR-LIN and SUM_1 stay OPEN.

## Summary of items
| § | Item | Status | Hypotheses |
| --- | --- | --- | --- |
| §1 | Lemma IM | PROVED | IDEAL-ACYC, the two movers of degree 2 |
| §2 | Lemma BIT-CHAIN and Corollary KEY-DIR | PROVED | 𝓛^R_(m+1), R110's c-step |
| §3 | Lemma VALUE-MONO and Corollary NO-REPEAT | PROVED | 𝓛^R_(m+1), ISO, any bit sequence |
| §4 | Lemma COMPOSE and Corollary COMPOSE-LB | PROVED | ISO genomes of 𝓛^R |
| §5 | Theorem FRAME (every ISO genome of 𝓛^R_(m+1) maps into the IM frame; T_k(m) ≤ T^Φ_k(m)) | PROVED | ISO, 𝓛^R_(m+1) |
| §6 | MACHINE: T^Φ_1(3) ≤ 10, hence T_1(3) = 10 | MACHINE | §5 + one solver UNSAT + a drup.c-checked proof |
| §7 | DATA | DATA | scoped per statement |

## Premises (landed RESULTS only, quoted verbatim)
- RESULTS R104: its DEFINITION of the IDEAL model and of the Ξ-graph only. No theorem of R104 is used.
- RESULTS R105:
  - (ENC) «the Ξ-order of β-sets is the order of the integers Σ ±2^rank (+ for even parity), so, with ε(x, k) := ±2^rank(x, k) (+ for
    even parity), the value of option (x, k) is ε(x, k) plus the current value of its Ξ-target (ε(x, k) alone if the Ξ-target is the
    exit X)»;
  - (LOCAL) «an option's value depends only on the states on its chain, a key only on the states below its level».
- RESULTS R110: its definitions of 𝓦_d, 𝓛^R_d, T^R(d), ISO, b_0(s), the c-step and T_k(m), quoted in §0; and (W-ONLY) «on 𝓦_d every
  step of a run equals, on the levels ≥ 1, the c-step with c = b_0 of the new state», used in Corollary COMPOSE-LB only.
- Not used: any other item of R104-R112, any other RESULTS entry, docs/lit, any other lane file, any outside source. §6 rests in addition
  on two machine premises, named there.

## 0. Model and notation
- The model (RESULTS R104's definition, as restated in RESULTS R105's entry):
  - A genome has movers x with levels lev(x) and options (x, k). Each option has a W-target of level lev(x) − 1 (none at level 0), a
    Ξ-target (a mover or the exit X), a β with a rank (distinct) and a parity, and a gate index (distinct).
  - IDEAL-ACYC: the Ξ-graph (an edge x → Ξ-target of each option whose target is a mover) is acyclic.
  - Under a state s the chain of (x, k) is (x, k), (y_1, s(y_1)), (y_2, s(y_2)), … with y_1 the Ξ-target of (x, k) and y_(j+1) the
    Ξ-target of (y_j, s(y_j)), up to the first option whose Ξ-target is X. A_s(x) := {s(x)} ∪ the options of x strictly Ξ-better than
    s(x) under s.
  - Keys under s are the gate indices along the W-target chain, lowest level first. A step moves every mover to the key-least option of
    its A-set under the OLD state, keys read under the NEW state, root-first.
- R110 (quoted): «𝓦_d the genomes with levels 0, …, d − 1 whose level-0 movers are exactly two movers named 0 and 1, 𝓛^R_d ⊆ 𝓦_d the
  2-wide degree-2 ladders in L-RED's R197 convention (movers 2l and 2l + 1 on level l, all of degree 2, no other movers, option k of a
  mover of level l ≥ 1 W-pointing to mover 2(l − 1) + k), T^R(d) the largest number of steps over 𝓛^R_d and all starts», «ISO the
  property that no option has Ξ-target 0 or 1, b_0(s) = 1 iff g(0, s(0)) < g(1, s(1)), for c ∈ {0, 1} the c-step the step rule on the
  movers of level ≥ 1 (A-sets under the old state, keys under the new state, movers 0 and 1 kept) with every level-1 option W-pointing to
  mover w keyed by (κ^c_w, its own gate), κ^c_0 = 1 − c, κ^c_1 = c, and T_k(m) the supremum, over the ISO genomes of 𝓛^R_(m+1), their
  starts u_0 and the bit sequences c_1, …, c_L with at most k changes, of the number of t with u_t ≠ u_(t−1) on the levels ≥ 1, where
  u_t is the c_t-step of u_(t−1)».
- Notation of this packet:
  - On 𝓛^R_(m+1) write A_l := mover 2l and B_l := mover 2l + 1 (l = 0..m). The UPPER movers are those of level ≥ 1. T_∞(m) is T_k(m)
    with no bound on the changes.
  - g(x, k) is the gate index of (x, k). v_s(x, k) is the integer value of (x, k) under s (R105 ENC); cv_s(x) := v_s(x, s(x)), and
    cv_s(X) := 0.
  - ch_k(z, s) is the set of movers on the chain of (z, k) under s, (z, k) itself excluded.
  - For a degree-2 mover z and a state s, C_z(s) is the option of z with the larger value under s (well defined: Fact 0).
  - z is HAPPY at s iff s(z) = C_z(s), and UNHAPPY otherwise.
  - s ⊕ e_y is s with y's option switched.
- **Fact 0.** On an acyclic genome, for a mover z of degree 2 and any state s: v_s(z, 0) ≠ v_s(z, 1).
  - The β of (z, 0) lies on the chain of (z, 0). It does not lie on the chain of (z, 1): that chain consists of (z, 1) and options of
    strict Ξ-descendants of z, never of z itself (acyclic), and each β belongs to exactly one option.
  - So the two β-sets differ, and by R105 ENC (an order of the integers that is the order of the sets) their integers differ, since the
    map from distinct sets to Σ ±2^rank with distinct ranks is injective. ∎
  - Hence A_s(z) = {s(z)} if z is happy at s, and {0, 1} otherwise.

## 1. Lemma IM (PROVED)
- **Statement.** IDEAL-ACYC. Let z ≠ y be movers of degree 2, s a state with y unhappy at s, and s′ := s ⊕ e_y.
  - (a) If y ∉ ch_0(z, s) ∪ ch_1(z, s), then C_z(s′) = C_z(s).
  - (b) If y ∈ ch_0(z, s) ∩ ch_1(z, s), then C_z(s′) = C_z(s).
  - (c) If y lies in ch_k(z, s) and not in ch_(1−k)(z, s), then C_z(s′) ∈ {C_z(s), k}.
- **Proof.**
  - (a) The chains of (z, 0) and (z, 1) under s do not pass y. The movers on them have the same options under s and s′, so they are the
    same chains under s′ and carry the same values (R105 LOCAL). So C_z is unchanged.
  - Rise at y. y is unhappy at s, so s′(y) = C_y(s), and by Fact 0 v_s(y, s′(y)) > v_s(y, s(y)) = cv_s(y).
    - The chain of (y, s′(y)) passes only Ξ-descendants of y, not y (acyclic); their options are the same under s and s′.
    - So v_(s′)(y, s′(y)) = v_s(y, s′(y)) (R105 LOCAL), and δ := cv_(s′)(y) − cv_s(y) > 0.
  - Chains through y. Let y ∈ ch_k(z, s). The part of the chain of (z, k) before y visits movers ≠ y, with the same options under s and
    s′, so under s′ the chain also reaches y.
    - By R105 ENC, applied along that part, v_r(z, k) = Σ (the ε's of the options before y) + cv_r(y) for r ∈ {s, s′}.
    - So v_(s′)(z, k) − v_s(z, k) = δ.
  - (b) Both values rise by δ. Their difference, and hence C_z, is unchanged.
  - (c) The value of (z, k) rises by δ > 0. The chain of (z, 1 − k) does not pass y, so (as in (a)) its value is unchanged.
    - If C_z(s) = k, then C_z(s′) = k.
    - Otherwise C_z(s′) is C_z(s) or k. ∎
- **Reading (OR).** This is the policy-iteration monotonicity lemma for the deterministic acyclic total-reward MDP with rewards ε (R105
  ENC): an improving switch never lowers a value, and it raises exactly the values of the chains through the switching mover.
- **Does NOT claim:**
  - anything for movers of degree ≥ 3;
  - anything for a simultaneous switch of several movers (a step of the model can move several; each is improving at the OLD state,
    not at the intermediate states of a decomposition);
  - any bound on the number of steps.

## 2. Lemma BIT-CHAIN and Corollary KEY-DIR (PROVED)
- **Setting.** G ∈ 𝓛^R_(m+1), m ≥ 1, c ∈ {0, 1}, and keys as in R110's c-step:
  - a level-1 option W-pointing to mover w is keyed (κ^c_w, its own gate);
  - an option of level l ≥ 2 is keyed by the key of its W-target's option under the state, followed by its own gate.
  - key_s(x) denotes the key of x's option s(x).
- **Statement (BIT-CHAIN).** For a state s define b_0 := c and, for l = 1..m:
  - b_l := b_(l−1) if (s(A_l), s(B_l)) = (0, 1);
  - b_l := 1 − b_(l−1) if it is (1, 0);
  - b_l := c_l(k) := [g(A_l, k) < g(B_l, k)] if s(A_l) = s(B_l) = k.
  Then:
  - (i) for l = 1..m, b_l = [key_s(A_l) < key_s(B_l)];
  - (ii) for l = 1..m, a mover x of level l prefers by key its option 0 (key of (x, 0) < key of (x, 1) under s) iff b_(l−1) = 1.
- **Proof.** Induction on l.
  - (ii) at l = 1: (x, 0) W-points to mover 0 and is keyed (1 − c, g(x, 0)); (x, 1) is keyed (c, g(x, 1)). They compare at the first
    entry (1 − c ≠ c): option 0 is smaller iff c = 1, i.e. iff b_0 = 1.
  - (ii) at level l ≥ 2: (x, 0) has key key_s(A_(l−1)) followed by g(x, 0), and (x, 1) has key key_s(B_(l−1)) followed by g(x, 1). The
    two prefixes are keys of the options s(A_(l−1)) and s(B_(l−1)) of two distinct movers of one level.
    - At level ≥ 2 such keys are tuples of the same length ending in distinct gates, so they differ.
    - At level 1 they are pairs ending in distinct gates.
    - So the tuples compare at the prefix: option 0 is smaller iff key_s(A_(l−1)) < key_s(B_(l−1)), i.e. iff b_(l−1) = 1 by (i) at
      l − 1.
  - (i) at level l: key_s(A_l) = (prefix of the option s(A_l)) followed by g(A_l, s(A_l)), and likewise for B_l. The prefix of option k
    of a level-l mover is the key of A_(l−1)'s option if k = 0 and of B_(l−1)'s if k = 1 (at l = 1: the entry κ^c_k).
    - If (s(A_l), s(B_l)) = (0, 1), the prefixes are those of A_(l−1) and B_(l−1) in this order, they differ, and A_l is smaller iff
      b_(l−1) = 1 (by (i) at l − 1, or at l = 1 since κ^c_0 = 1 − c < c = κ^c_1 iff c = 1).
    - If (1, 0), the order is reversed: A_l is smaller iff b_(l−1) = 0.
    - If both equal k, the prefixes are equal and the own gates decide: A_l is smaller iff g(A_l, k) < g(B_l, k). ∎
- **Corollary KEY-DIR.** For a state u, let u′ be its c-step and b_l the bits of u′ (BIT-CHAIN with s = u′). A mover x of level l ≥ 1
  moves (u′(x) ≠ u(x)) iff u(x) = b_(l−1) and C_x(u) ≠ b_(l−1).
  - Proof. By Fact 0, A_u(x) = {u(x)} if x is happy at u, and {0, 1} otherwise.
    - x takes the key-least option of A_u(x), keys under u′; its own key preference is decided by the options of level l − 1 under u′
      (keys go down the W-chain), which the c-step has already fixed (lowest level first).
    - By (ii), x moves iff it is unhappy at u and its key-preferred option is the other one, i.e. 1 − u(x) = 1 − b_(l−1), and then
      C_x(u) = 1 − u(x) = 1 − b_(l−1). ∎
  - Consequence (the BIT-CHAIN step): the c-step above level 0 depends on the gates only through c and the 2(m − 1) bits c_l(k),
    l = 1..m − 1. (c_m(k) enters only b_m, which no mover reads.)
- **Does NOT claim:** anything outside 𝓛^R; anything for the IDEAL step of a genome whose level 0 moves, except through R110 W-ONLY
  (not used here).

## 3. Lemma VALUE-MONO and Corollary NO-REPEAT (PROVED)
- **Statement.** G ∈ 𝓛^R_(m+1) with ISO, u a state, c ∈ {0, 1}, u′ the c-step of u. For every upper mover x:
  cv_(u′)(x) ≥ cv_u(x), with strict inequality if u′(x) ≠ u(x).
- **Proof.** Induction along a topological order of the Ξ-graph, Ξ-targets first.
  - By ISO, every option of an upper mover has an upper mover or X as Ξ-target. Let t := the Ξ-target of (x, u′(x)).
  - By R105 ENC, cv_(u′)(x) = ε(x, u′(x)) + cv_(u′)(t).
  - By induction (t is a strict Ξ-descendant of x, or X with cv 0), cv_(u′)(t) ≥ cv_u(t).
  - So cv_(u′)(x) ≥ ε(x, u′(x)) + cv_u(t) = v_u(x, u′(x)) (R105 ENC).
  - If u′(x) = u(x), this is cv_u(x).
  - Otherwise u′(x) ∈ A_u(x) \ {u(x)} (the c-step takes an option of the A-set under the old state), so v_u(x, u′(x)) > cv_u(x). ∎
- **Corollary NO-REPEAT.** In every c_t-step sequence of an ISO genome of 𝓛^R_(m+1) (any number of changes of c), the vector
  (cv(x))_x of the upper movers never decreases, and it strictly increases at every t with u_t ≠ u_(t−1). Hence no state repeats among
  the states with u_t ≠ u_(t−1), and T_k(m) ≤ T_∞(m) ≤ 2^(2m) − 1.
  - Proof: a strictly increasing sequence of vectors (componentwise ≥, ≠) has distinct terms; there are 2^(2m) upper states. ∎
- **Does NOT claim:** any polynomial bound (2^(2m) − 1 is exponential), or that T_∞(m) is attained.

## 4. Lemma COMPOSE and Corollary COMPOSE-LB (PROVED)
- **Setting.**
  - K ∈ 𝓛^R_(m′+1) and G ∈ 𝓛^R_(m+1), both ISO, m′, m ≥ 1.
  - The composite H ∈ 𝓛^R_(m′+m+1):
    - its levels 0..m′ are K;
    - G's mover of level l ≥ 1 becomes H's mover of level m′ + l (renamed 2(m′ + l) + i for G's 2l + i), keeping its Ξ-targets (renamed;
      inside G's part), β's and gates;
    - G's level-0 movers are dropped;
    - the β ranks of G's options are raised above all of K's, and its gate indices above all of K's (orders inside each part kept);
    - H's R197 wiring makes option k of a level-(m′ + 1) mover W-point to mover 2m′ + k.
  - H is in 𝓛^R_(m′+m+1) (two degree-2 movers per level, R197 W-wiring, distinct ranks and gates), and its Ξ-graph is acyclic (the
    disjoint union of K's and G's, upper parts) and ISO.
- **Statement.** For c ∈ {0, 1} and any state u of H, let u′ be H's c-step of u.
  - (i) On K's upper movers, u′ is K's c-step of u restricted to K.
  - (ii) On G's movers, u′ is G's c_*-step of u restricted to G, where c_* := b_(m′) of u′ computed in K (BIT-CHAIN in K).
- **Proof.**
  - A-sets: every chain of an option of K's (resp. G's) movers stays in K's (resp. G's) part, so its value depends only on that part's
    states (R105 LOCAL), and the ranks keep the order inside each part. Since ranks are compared within one chain's set, and both sets
    of one comparison lie in one part, the A-sets are those of K (resp. G).
  - Keys: H's keys at levels ≤ m′ are K's keys (keys go down the W-chain), so (i) holds.
  - For a mover of H-level m′ + l, BIT-CHAIN (ii) in H says its key preference is decided by H's bit b_(m′ + l − 1) of u′.
  - By BIT-CHAIN in H, H's bits at levels ≤ m′ are K's bits b_0..b_(m′) (c the same).
  - H's bits at levels m′ + 1.. are computed from the states of G's levels, starting from b_(m′), by the same recursion as G's bits
    starting from b_0 := c_*. The bits c_l(k) are G's, since the gate order inside G's part is kept.
  - So every G-mover takes the same option as in G's c_*-step (KEY-DIR in both genomes, same A-sets). ∎
- **Corollary COMPOSE-LB.** For every flip-free c-step sequence of K and the bit sequence c_*(t) := b_(m′) of K's part of u_t that it
  produces, the number of steps of G's c_*(t)-step sequence (from any start) is at most T^R(m′ + m + 1).
  - Proof. Give H's level-0 movers both options with Ξ-target X, and choose the start so that each takes its better option (Fact 0 at
    level 0: each has its own constant values). Then they are happy forever: their values never change, since no chain passes them by
    ISO.
  - By R110 W-ONLY, every step of H's IDEAL run equals on the levels ≥ 1 the c-step with c = b_0 of the new state, which is constant
    since level 0 never moves.
  - By (i)-(ii) H's run counts every step of G's c_*-sequence (and K's steps). Its length is at most T^R(m′ + m + 1) by R110's
    definition of T^R. ∎
- **Does NOT claim:** any bound in the other direction; that the bit sequences a flip-free K can produce include every schedule (they do
  not in general: the cost of timing flips is the open part).

## 5. Theorem FRAME (PROVED)
- **The IM frame Φ_m (m ≥ 1).** A frame system Σ consists of:
  - the 2m upper movers A_l, B_l (l = 1..m), each with two options (z, k);
  - a Ξ-target for each option, an upper mover ≠ z or X, with an acyclic Ξ-graph;
  - a table C: (z, s) ↦ C_z(s) ∈ {0, 1} for every upper state s ∈ {0, 1}^(2m);
  - bits c_l(k) ∈ {0, 1} for l = 1..m − 1, k ∈ {0, 1}.
  It satisfies:
  - (Φ1) C_z(s) does not depend on s(z);
  - (Φ2) LOCAL: if y ∉ ch_0(z, s) ∪ ch_1(z, s) then C_z(s ⊕ e_y) = C_z(s);
  - (Φ3) IM: for y ≠ z unhappy at s (s(y) ≠ C_y(s)), clauses (b) and (c) of Lemma IM hold with this C.
  The frame step from s with bit c: b_0 := c; for l = 1..m, every level-l mover x with C_x(s) ≠ s(x) and C_x(s) = 1 − b_(l−1)
  switches, and then b_l is computed from the NEW level-l states by the BIT-CHAIN recursion with the c_l(k) (l < m).
  T^Φ_k(m) := the largest T such that some frame system, start s_0 and bits c_1, …, c_T with at most k changes have
  s_t := the frame step of s_(t−1) with c_t, and s_t ≠ s_(t−1) for t = 1..T (T^Φ_∞ without a bound on the changes).
- **Statement.**
  - (i) For every ISO genome G of 𝓛^R_(m+1), the system Σ(G) satisfies (Φ1)-(Φ3), and its frame step with bit c equals G's c-step
    (on the levels ≥ 1) at every state. Here Σ(G) consists of the Ξ-targets of G's upper options, the table C_z(s) of Fact 0, and the
    bits c_l(k) := [g(A_l, k) < g(B_l, k)].
  - (ii) Hence T_k(m) ≤ T^Φ_k(m) for every k ≥ 0, and T_∞(m) ≤ T^Φ_∞(m).
- **Proof.**
  - (i) Ξ-targets: by ISO every Ξ-target of an upper option is an upper mover or X; acyclic by IDEAL-ACYC.
    - C is well defined by Fact 0.
    - (Φ1): z is not on its own chains (acyclic), so by R105 LOCAL its option values, hence C_z, do not depend on s(z).
    - (Φ2) is Lemma IM (a); (Φ3) is Lemma IM (b), (c).
    - The step: by KEY-DIR, x moves in G's c-step iff u(x) = b_(l−1) and C_x(u) ≠ b_(l−1), with b_(l−1) from the new state, which is the
      frame's rule (C_x(s) ≠ s(x) and C_x(s) = 1 − b_(l−1) say the same). The frame's b_l recursion is BIT-CHAIN's.
  - (ii) Take G, a start u_0 and bits c_1..c_L with at most k changes, and let T be the number of t with u_t ≠ u_(t−1).
    - Delete every t with u_t = u_(t−1): the remaining states still form a step sequence, because u_t = u_(t−1) means the step is the
      identity.
    - Deleting a term of the bit sequence does not increase its number of changes, since [a ≠ c] + [c ≠ b] ≥ [a ≠ b].
    - By (i) the result is a frame run of Σ(G) of length T with at most k changes. ∎
- **Consequence.** Every frame query «T^Φ_k(m) ≥ L» that is UNSAT gives T_k(m) ≤ L − 1. A SAT model is a frame system, not a genome;
  lower bounds need genomes (§6).
- **Does NOT claim:** that T^Φ_k(m) = T_k(m) in general (the frame is a relaxation; no converse is proved); anything outside ISO or
  𝓛^R_(m+1).

## 6. MACHINE: T^Φ_1(3) ≤ 10, hence T_1(3) = 10
- **Statement.** T^Φ_1(3) ≤ 10. With Theorem FRAME (ii): T_1(3) ≤ 10. With the witness below: T_1(3) = 10.
- **What rests on what:**
  - (M1) Encoder (a premise, not machine-checked). experiments/si/box75/frame_P-IDEAL-IM.py (frozen copy, sha1 c3b3a232…), run as
    `DUMP=<dir> DUMPONLY=1 python3 frame_P-IDEAL-IM.py 3 t1 11`, writes a CNF that is satisfiable iff some frame system of Φ_3 has a frame
    run of 11 steps with at most 1 change. Clause groups (line numbers of the frozen copy):
    | lines | frame object |
    | --- | --- |
    | 38-43 | exactly one Ξ-target per option: X or an upper mover ≠ z |
    | 44-49 | acyclicity: a transitive, asymmetric relation R containing every Ξ-edge (it exists iff the Ξ-graph is acyclic) |
    | 51-61 | on(z, k, s, y) ↔ y ∈ ch_k(z, s), by the fixpoint equation of the chain (unique on an acyclic graph) |
    | 63-65 | (Φ1) |
    | 66-69 | (Φ2) |
    | 71-74 | (Φ3): line 72 Lemma IM (b); line 73 (c) with k = 1; line 74 (c) with k = 0; u = «y unhappy at s» |
    | 75 | the bits c_l(k), l = 1..m − 1 |
    | 77-110 | the run: states S_t; external bit B ⊕ F_(t+1) for step t; F monotone (one change at most, line 81); the frame step (lines 99-107: key-preferred index 1 − b_(l−1), BIT-CHAIN recursion from the new states); every step moves (line 108) |
  - (M2) Solver 1: CaDiCaL 1.5.3 via python-sat reported UNSAT (1,282 s; L-SI box 70, experiments/si/box70/log/3_t1_11.log). No proof.
  - (M3) Solver 2 + checker: Glucose 4 reported UNSAT on the CNF with sha1 7e611c8bdf53a70a398e9e1ec3b220a1b79e2507 (96,580 clauses), and
    its DRUP proof (2,388,304,251 bytes, sha1 32be84e4…) was accepted by drup.c (sha1 2d4b8eab…, the checker of RESULTS R112):
    «s VERIFIED (6531220 lemmas RUP-checked)». L-COMP successor 9, claude/l-comp experiments/comp/box27/log/lsi_q1_cert.txt (branch
    head fb9682a1 when read).
  - (M4) Identity of the CNF: the frozen encoder regenerates sha1 7e611c8b… (checked in this box; experiments/si/unsat_regen.sh line
    «m 3 t1 11 (box 70)»). L-COMP generated it from its read-only copy of the same encoder at claude/l-si 7523970f.
  - drup.c's correctness is a premise (as in R112). No drat-trim, no Lean.
- **Witness T_1(3) ≥ 10.** L-NEW's ISO genome kf1_d4_t10 of 𝓛^R_4: claude/l-new experiments/new/box160/out/kf1_d4_t10.json, sha1
  1c0dc8cc5a8dd382e028d199f96f783f995b9a5a; read-only copy experiments/si/box64/wit/kf1_d4_t10.json, same sha1.
  - Replayed by two simulators: box 64 flipdp.py (T_0, T_1 = 5, 10; XSIM 0) and L-NEW's box 150 Gen through box71/replayk.py (10
    steps, bits 0000011111, 1 change).
- **Does NOT claim:** T_k(3) for k ≥ 2 (the frame UNSATs for k = 2, 3, ∞ are single-solver, without a checked proof; listed in
  experiments/si/UNSAT-LIST.txt, not part of this packet).

## 7. DATA (each count names the statement it covers)
- experiments/si/box75/imcheck.py (own c-step from R110's text; random ISO genomes of 𝓛^R_2, 𝓛^R_3, 𝓛^R_4 with acyclic Ξ-data, every
  start, both c, plus 4 real m 3 pins of boxes 72-74). Run `imcheck.py 400 75`: 404 genomes. Output in experiments/si/box75/imcheck.out.
  | statement | checks | violations | negative control (fires) |
  | --- | --- | --- | --- |
  | Lemma IM (b), (c) (y unhappy, on a chain) | 31,208 | 0 | direction reversed: 6,284 |
  | (Φ2) = Lemma IM (a) | 250,248 | 0 | — |
  | (Φ1) | 66,520 | 0 | — |
  | BIT-CHAIN (i) | 66,520 | 0 | bit negated: 66,520 |
  | KEY-DIR | 133,040 | 0 | condition u(x) ≠ b_(l−1): 67,100 |
  | VALUE-MONO | 133,040 | 0 | «a moved mover's value falls»: 33,586 |
  | FRAME step = c-step | 24,184 | 0 | other bit: 20,486 |
  | own c-step = flipdp step (level 0 forced to a configuration with b_0 = c) | 18,944 | 0 | — |
- COMPOSE: experiments/si/box68/compose.py (box 68): 200 random pairs (m′, m) ∈ {1, 2}², all starts, both c: 0 disagreements on K's and
  G's parts; negative control (schedule negated) fires 6,786 and 16,853 times. COMPOSE-LB: no separate DATA.
- §6: the CNF sha1 regenerated (above); the witness replays. For the encoder (M1) only these cross-checks at m = 2 are claimed:
  - mode t1 gives T_1 ≥ 5 SAT and T_1 ≥ 6 UNSAT (experiments/si/box70/check70.sh);
  - mode tk with K = 1 gives T ≥ 6 UNSAT with a drup.c-verified proof (experiments/si/box71/check71.sh);
  - both equal L-COMP's exhaustive T_1(2) = 5 over all ISO genomes of 𝓛^R_3 (L-COMP box 27 bfk.c, as quoted in
    docs/si/N5-FRAME-box70.md §0).
- Not covered by DATA: NO-REPEAT beyond VALUE-MONO; Fact 0 (used by every check).

## 8. Files
- docs/si/P-IDEAL-IM.md (this file), docs/si/P-IDEAL-IM-line-L1.txt (draft RESULTS line).
- experiments/si/box75/{imcheck.py, imcheck.out, frame_P-IDEAL-IM.py, check75.sh}.
- experiments/si/box68/compose.py; experiments/si/box64/{flipdp.py, wit/kf1_d4_t10.json}; experiments/si/box71/replayk.py;
  experiments/si/unsat_regen.sh, experiments/si/UNSAT-LIST.txt.
- Read only, other branches: claude/l-comp experiments/comp/box27/log/lsi_q1_cert.txt, experiments/comp/box27/drup.c; claude/l-new
  experiments/new/box160/out/kf1_d4_t10.json.
