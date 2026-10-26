# P-N5-RUND-box17: offsets, aligned blocks and the per-edge schedule of Lemma P inside a fallback-free in-phase run of N5 (packet)
Authors: L-SI successor 12 (session_01HYh7NTpb8ZcvdYpgAJiDgy; §2-§4) and successor 13 (session_018EgSbDTYEVHqL882sCoX7u; §5, §6, assembly).
Opus 5.5; D15, D18, L37, L40. Frozen at the Lead's word (08:32Z: "Freeze it at the earlier of (i) the end of your (FS) box … (ii) your
handover"); the (FS) box ended with (FS) not proved, so it is §7 (OPEN). Source: lane note docs/si/N5-RUND-box17.md §4, §5, §11, §14, §16
(not frozen). Labels (D18 / L40): PROVED (by the lane, unrefereed until signed) / CONJECTURE / OPEN / READING / DATA / DEAD.
D1: "A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as
wrong until it passes the gauntlet below." Nothing here bounds N5's running time on any class. Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. What to sign
Every item is structural, on EVERY game, inside one fallback-free run S of N5 inside one phase. Items:
- §2 Lemma CR-REL.
- §3 Lemma OFFSET (a)-(c), Lemma MERGE-B, Theorem TWIN-GAP (i)-(iii) and its Corollary (under (h3_D) on S).
- §4 Lemma PIECE_D (a), (b), Corollary SPLIT-RED.
- §5 Lemma P^c_sch, Corollary FRZ-SCH, Corollary CHARGE (hypothesis (ii) only).
- §6 Fact FZ, Lemma UNF, Corollary CHARGE-U (hypothesis (ii) only; FZ under the standing SPEC premise named there).
Not to sign: §7 (CONJECTURES FS, UF-ONCE, LC2, PAIR-OC; OPEN items), §8 (DEAD statements, for the record), §9 (DATA), every READING.

## 1. Setting and cited text
- RESULTS R55 / R62 setting, quoted from R62: "state k = (σ_k, τ_k); σ̄_k; Ξ_k; G_τ; W_k; λ_Ξ, λ_W; D_k; u(v); R_D, F_D; π_v; (h_D); (h3_D);
  lev, COARSE_L, (C2), (C4) of RESULTS R25; M_D, ⊥ if D_k = ∅ … A run S: consecutive states k_0, …, k_1 inside one phase, all of whose
  transitions are S4a steps (no fallback); Ω_k := W_k, the valuation of σ_k in the fixed one-player game G_τ; COARSE := COARSE_L for a
  level −1 ≤ L < ∞." Here σ̄_k is SPEC S1's optimal Odd counterstrategy to σ_k, Ξ_k(v) the value of the (σ_k, σ̄_k)-play from v, W_k(v)
  the value of the (σ_k, τ_k)-play, D_k := {Odd u : σ̄_k(u) ≠ τ_k(u)}, u(v) the first vertex of D_k on v's W-play, R_D := {v : u(v) exists},
  F_D := V ∖ R_D.
- RESULTS R62 (d) WM-G: "for every transition k → k+1 of a run S, Ω_{k+1} ⊵ Ω_k pointwise." Its proof: SPEC S4a takes σ_{k+1} := Even's
  pointwise optimum in the arena H_k of G_τ, in which Even's v may use {σ_k(v)} ∪ Iσ_k(v), with Iσ_k := {(x, z) : Ξ_k(z) ▷ Ξ_k(σ_k x)}
  (SPEC S2); (F1). (MON) := WM-G with (C1): Ω^c_{k+1} ⪰ Ω^c_k, where Ω^c_k := COARSE(Ω_k).
- RESULTS R62 (e) Lemma P^c_L and Lemma CR-D, quoted: "if at every state of S (i) COARSE(Ξ_k(v)) = COARSE(W_k(v)) for every v and (ii) the
  map v ↦ λ_W(v) is the same, then COARSE(Ω_t) = COARSE(Ω_{k_0+n−1}) for every t ∈ S with t ≥ k_0 + n − 1 (Lemma P^c_L: for every j with
  k_0 + j ∈ S and every simple path r of G_τ from x to a W-cycle node u with at most j edges, Ω^c_{k_0+j}(x) ⪰ COARSE(value(r)))." The proof
  is in docs/si/P-N5-H3-box16.md §5 (sha1 680e4528…), with R62's added sentence for Case B1 (H3-N2). value(r) := (u, P(r), m) for
  r = (r_0, …, r_m), P(r) := {r_i : i < m, rank(r_i) > rank(u)}.
- RESULTS R62 (f) FRZ-U_H3: "on a run S inside one phase with (h3_D) at every state, for max_S M_D ≤ L < ∞, L ≥ −1, COARSE_L(W) = COARSE_L(Ξ)
  on V at every state of S, and it is constant on S FROM STATE k_0 + n − 1 ON."
- RESULTS R62 (b) TC-CLASS and (c) C2-H3 (with its proof's factorisation P_F(v) = (π_v ∩ V_{>c}) ⊔ P_F(u) for c := λ(v) ∉ π_v, both frames).
- RESULTS R55 (a): "for every state k and every v ∈ F_D, Ξ_k(v) = W_k(v)."
- RESULTS R19 (d), the (SG) step: "Ξ_{L+1}(z) ⊵ Ξ_L(z) at any N5 transition (on all games)".
- RESULTS R17 (a) (F1): "the optimum of a one-player game dominates every strategy of that game pointwise"; R17 (c) Theorem PH (a λ-phase of
  switch-best on a one-player game has fewer than n + m steps) and (d) (for every pointwise-optimal choice). Game-general per R55's premises.
- (C1)-(C4), lev, COARSE_L: RESULTS R25 setting (docs/si/P-N5-FB-box7.md §1). (Cstrict): COARSE_L a ≺_L COARSE_L b ⇒ a ◁ b.
- The FORBIDDEN predicate (new here). At state k and level L, an Even edge (x, z) is FORBIDDEN AT k if z ≠ a := σ_k(x),
  COARSE_L(W_k(z)) ≻_L COARSE_L(W_k(a)) and not Ξ_k(z) ▷ Ξ_k(a).

## 2. Lemma CR-REL (PROVED, every game; L-SI 12)
Statement. CR-D holds with hypothesis (i) replaced by EDGE ORDER TRANSFER at L, at every state k of S:
- (i_rel) for every Even x, every z ∈ succ(x) and a := σ_k(x): COARSE_L(W_k(z)) ≻_L COARSE_L(W_k(a)) ⇒ Ξ_k(z) ▷ Ξ_k(a).
Then, under (i_rel) and (ii), COARSE_L(W) is constant on S from state k_0 + n − 1 on.
Proof. P^c_L's proof uses (i) only in Case B, to turn Ω^c_k(z) ≻ Ω^c_k(a) into Ξ_k(z) ▷ Ξ_k(σ_k x), so that (x, z) ∈ Iσ_k. (i_rel) is that
step. Nothing else in P^c_L or in CR-D's proof reads Ξ. □
- (i) ⇒ (i_rel), by (C2) and (Cstrict). (i_rel) at L says: no Even edge is forbidden at L. §5 refines this to one state per edge.

## 3. Offsets (PROVED, every game, under (h3_D) at every state of S; L-SI 12)
Setting. L* := max(max_S M_D, −1), with M_D := −1 when D_k = ∅. w(P) := Σ_{x ∈ P} ε(x)·2^{rank x}, ε(x) = +1 for even x and −1 for odd x
(S1's signed path weight; injective on sets, P-N5-FB-box7 §1 (C3)). s^Ξ_k(v) := w(P(Ξ_k(v))), s^W_k(v) := w(P(W_k(v))), the OFFSET
Δ_k(v) := s^W_k(v) − s^Ξ_k(v), and for u ∈ D_k: δ_k(u) := w(P(W_k(u))) − w(P(Ξ_k(u))).
### Lemma OFFSET
- (a) λ_Ξ(v) = λ_W(v) for every v, constant on S. s^Ξ_k(v) and s^W_k(v) are non-decreasing along S.
- (b) Δ_k(v) = 0 if v ∈ F_D, or if v ∈ R_D and λ(v) ∈ π_v. Otherwise Δ_k(v) = δ_k(u(v)).
- (c) Every δ_k(u) is a sum of terms ±2^r with r ∈ P(Ξ_k(u)) Δ P(W_k(u)), a set of ranks in [ℓ_S, L*], where ℓ_S is the least rank in
  U_S := ∪_{k ∈ S, u ∈ D_k} (P(Ξ_k(u)) Δ P(W_k(u))). So every offset on S is a multiple of 2^{ℓ_S}; if U_S = ∅, every offset is 0.
Proof.
- (a) The first sentence is P-N5-H3 §6's proof of (ii) (R55 (a) on F_D; TC-CLASS and (h3_D) on R_D; λ_Ξ is constant on a phase).
  Ξ_{k+1}(v) ⊵ Ξ_k(v) ((SG)) and W_{k+1}(v) ⊵ W_k(v) (WM-G). With the cycle node fixed, S1's order compares path sets first, and on sets that
  order is the order of w. So s^Ξ and s^W do not decrease.
- (b) On F_D, Ξ = W (R55 (a)). For v ∈ R_D with c := λ(v), u := u(v): if c ∈ π_v, both plays follow π_v to c (σ̄ = τ off D_k), so the path
  sets are equal; if c ∉ π_v, C2-H3's proof gives P_F(v) = (π_v ∩ V_{>c}) ⊔ P_F(u) in both frames F = Ξ, W. w is additive over disjoint
  unions, so Δ_k(v) = w(P_W(u)) − w(P_Ξ(u)) = δ_k(u).
- (c) δ_k(u) = Σ_{r ∈ P_W(u) ∖ P_Ξ(u)} ε 2^r − Σ_{r ∈ P_Ξ(u) ∖ P_W(u)} ε 2^r. Under (h3_D) the two values share the cycle node, so
  top(P_Ξ(u) Δ P_W(u)) = lev(Ξ_k(u), W_k(u)) ≤ M_D ≤ L*. □
### Lemma MERGE-B
At a state of S, if λ(y) = λ(z) and Δ(y) = Δ(z), then s^Ξ(y) − s^Ξ(z) = s^W(y) − s^W(z), so the two frames order the path sets of y and z the
same way. (Immediate from the definition of Δ.) Inside one OFFSET CLASS (common cycle node, common offset) the frames agree on every
path-set comparison: RESULTS R50's Fact B with "same terminal" replaced by "same offset".
### Theorem TWIN-GAP
Let N_v be the number of transitions of S at which Δ(v) changes, and B := L* − ℓ_S + 1 (N_v = 0 if U_S = ∅). Then:
- (i) at each such transition, with d := Δ_{k+1}(v) − Δ_k(v) ≠ 0: s^W(v) rises by ≥ d if d > 0, and s^Ξ(v) rises by ≥ −d if d < 0;
- (ii) at most (2^{L*+2} − 2) / 2^{ℓ_S} < 2^{B+1} of them lie at states ≥ k_0 + n − 1;
- (iii) N_v ≤ (n − 1) + 2^{B+1}.
Proof.
- (i): s^W_{k+1} − s^W_k = (s^Ξ_{k+1} − s^Ξ_k) + d, and both rises are ≥ 0 by OFFSET (a).
- (ii): from state k_0 + n − 1 on, FRZ-U_H3 at L* keeps COARSE_{L*}(W(v)) = COARSE_{L*}(Ξ(v)) constant, so P ∩ V_{>L*} is constant in both
  frames. Each score then moves by a difference of w over sets of ranks ≤ L*; each rank r contributes at most 2^r, so each score rises by
  ≤ 2^{L*+1} − 1 in all (it is monotone), and s^W(v) + s^Ξ(v) by ≤ 2^{L*+2} − 2. By (i) and OFFSET (c), each change consumes ≥ |d| ≥ 2^{ℓ_S}.
  If L* = −1, then U_S = ∅ and there is nothing to count.
- (iii): at most n − 1 transitions lie before k_0 + n − 1. □
- Corollary: under (h3_D) on S, the terminal changes of v at which its offset changes are ≤ N_v ≤ (n − 1) + 2^{B+1}.
- READING: polynomial only when the band is narrow (B = O(log n)); in data B reaches 39 at n ≤ 48 (note §7).

## 4. Lemma PIECE_D and Corollary SPLIT-RED (PROVED, every game; L-SI 12)
Definitions. At k ∈ S an Even edge (x, z), z ≠ a := σ_k(x), is SPLIT if [Ξ_k(z) ▷ Ξ_k(a)] ≠ [W_k(z) ▷ W_k(a)]. State k is ALIGNED if it has no
split edge. N_split(S) := the number of transitions of S whose source is not aligned.
### Lemma PIECE_D
- (a) At an aligned state k, Iσ_k equals the improving set of σ_k in the one-player game G_τ, and the S4a step k → k+1 is a switch-best step
  of G_τ from σ_k (R17's rule, for SPEC's pointwise-optimal choice).
- (b) If every transition of a block B of consecutive transitions of S has an aligned source and λ_W is constant on B, then B has fewer
  than n + m transitions (m := the number of edges).
Proof.
- (a) SPEC S2 gives Iσ_k = {(x, z) : Ξ_k(z) ▷ Ξ_k(σ_k x)}. In G_τ every Odd vertex has out-degree 1, so S1's valuation of σ_k on G_τ is the
  play valuation W_k, and G_τ's improving set is {(x, z) : W_k(z) ▷ W_k(σ_k x)} (R17's setting). Alignment makes the two sets equal. S4a
  takes Even's pointwise optimum in H_k, which is then R17's switch-best arena on G_τ; R17 (d) holds for every pointwise-optimal choice.
- (b) By (a), B is a run of switch-best on G_τ started at its first state. λ_W is G_τ's cycle-node map, so B lies in one λ-phase of that run.
  R17 (c) bounds |B|. □
### Corollary SPLIT-RED
Under (h3_D) at every state of S: |S| ≤ N_split(S) + (N_split(S) + 1)·(n + m − 1).
Proof. λ_W is constant on S (P-N5-H3 §6, (ii)). The maximal blocks of transitions with aligned sources number ≤ N_split + 1, each with
< n + m transitions by PIECE_D (b); the other transitions number N_split. □
- A forbidden edge (§1) at L = −1 is a split edge; the converse fails (EXTRA edges, improving in Ξ only, are split but not forbidden).
- CORRECTION to the source note's §11 READING ("x ∈ R_D with a := σ(x) ∈ R_D and z ∈ F_D … W prefers z and Ξ does not"): that pattern
  cannot be forbidden, by Fact FZ (§6). In data the forbidden pairs have σ(x) ∈ F_D and z gated (§6). The READING is withdrawn; no
  PROVED item used it.

## 5. The restricted Lemma P with an exact per-edge schedule (PROVED, every game; L-SI 13)
Hypotheses: S as in §1 (one phase, no fallback) and (ii) (λ_W constant on S). Not (i), not (h3_D). Level −1 ≤ L < ∞.
- Observation (READING of P^c_L's proof): in the step from k to k + 1, hypothesis (i) is used once, in Case B, on the FIRST edge (x, z)
  of r, at state k; the suffix r′ enters only through the IH at state k. Unrolled, edge q of a path used at state k is looked at only
  at state k − 1 − q.
- SCHEDULE. For a simple path r = (r_0, …, r_m) of G_τ ending at a W-cycle node and a state k ∈ S: the schedule of r at k is CLEAN if
  k − m ≥ k_0 and, for every q < m with r_q Even, the edge (r_q, r_{q+1}) is not forbidden at state k − 1 − q.
### Lemma P^c_sch
If the schedule of r at k is clean, then Ω^c_k(r_0) ⪰ COARSE(value(r)).
Proof. Induction on m, for all k at once.
- m = 0: r = (u) and Ω_k(u) = (u, ∅, 0) by (ii) (u is a W-cycle node at every state of S).
- m ≥ 1: r = x → z → r′, r′ simple, avoiding x, with m − 1 edges. The schedule of r′ at k − 1 is clean: (k − 1) − (m − 1) = k − m ≥ k_0,
  and edge q′ of r′ is edge q′ + 1 of r, looked at in both at state (k − 1) − 1 − q′. The IH gives Ω^c_{k−1}(z) ⪰ COARSE(value(r′)).
- P^c_L's step from k − 1 to k, verbatim (Cases A1, A2, B1, B2, with R62's B1 sentence), with k − 1 in the role of its k:
  - Cases A1, A2 use the IH, (V2c), (MON) and (ii) only.
  - Case B (x Even, Ω^c_{k−1}(z) ≻ Ω^c_{k−1}(a), a := σ_{k−1}(x)): P^c_L uses (i) to get Ξ_{k−1}(z) ▷ Ξ_{k−1}(a). Here z ≠ a (their coarse
    values differ), so if that failed, (x, z) would be forbidden at k − 1 − 0, against cleanness. The rest of Case B (B1, B2) uses (F1) on
    the arena H_{k−1}, the IH, (C4), (V2c) and (ii) only. □
### Corollary FRZ-SCH
For s ≤ t in S and any x, let r_t be x's W-play prefix at t (to λ_W(x)), with m edges. If the schedule of r_t at s is clean, then
COARSE(W(x)) is constant on [s, t].
Proof. Ω_t(x) = value(r_t): λ_W(x) is a W-cycle node at every state, by (ii) (CR-D's proof). P^c_sch at s gives Ω^c_s(x) ⪰ Ω^c_t(x). (MON)
gives Ω^c_t(x) ⪰ Ω^c_{s′}(x) ⪰ Ω^c_s(x) for s ≤ s′ ≤ t. (C3). □
- It contains CR-D (under (i) nothing is forbidden; a clean schedule at every s ≥ k_0 + m) and CR-REL, and starts the freeze of x at
  k_0 + m, m = the length of x's own play prefix, instead of k_0 + n − 1.
### Corollary CHARGE
Every change of COARSE(W(x)) at a transition s − 1 → s of S (s − 1 ≥ k_0) is one of:
- a WINDOW change: s − 1 − m < k_0, m := the length of x's W-play prefix at s (so s ≤ k_0 + n − 1; at most n − 1 per x per run); or
- a CHARGED change: x's W-play prefix r at s has an Even edge (r_q, r_{q+1}) that is forbidden at state s − 2 − q (≥ k_0).
Proof. FRZ-SCH at (s − 1, s): if the schedule of r at s − 1 were clean, COARSE(W(x)) would be constant on [s − 1, s]. □
- Consequence: changes of COARSE(W(x)) on S ≤ (n − 1) + (n − 1)·|K_F(S)|, K_F(S) := the states of S at which some Even edge is forbidden
  (a charged state lies in [s − 1 − m, s − 2], so each forbidden state serves ≤ n − 1 values of s). In data |K_F| is close to |S| (§9), so
  this form is weak; §6 sharpens it.

## 6. Charging switches (PROVED, every game; L-SI 13)
### Fact FZ (premise: σ̄_k is Odd's pointwise-optimal strategy in the one-player game G_{σ_k}, the standing SPEC S1 premise, as 1E-N3 in R57)
If (x, z) is forbidden at k (any L ≥ −1), then Ξ_k(z) ◁ W_k(z); so z's W-play meets D_k.
Proof. (F1) in G_{σ_k} (Odd's one-player game; τ_k is one of its strategies) gives Ξ_k ⊴ W_k pointwise. With a := σ_k(x):
Ξ_k(z) ⊴ Ξ_k(a) (forbidden; ⊴ is total) ⊴ W_k(a) ◁ W_k(z) (COARSE W(z) ≻ COARSE W(a) and (Cstrict)). If z's W-play met no vertex of D_k,
the (σ_k, σ̄_k)-play from z would be the same play (σ̄_k = τ_k off D_k), so Ξ_k(z) = W_k(z). □
### Lemma UNF
Let a change of COARSE W(x) at s − 1 → s be charged (§5) to (q, e = (r_q, r_{q+1}), f := s − 2 − q). Then r_q SWITCHES INTO r_{q+1} at an S4a
transition k′ → k′ + 1 with f < k′ ≤ s − 1 ≤ f + n − 1, and e is not forbidden at k′.
Proof. σ_s(r_q) = r_{q+1} (r is x's W-play at s, r_q Even), and r_{q+1} ≠ σ_f(r_q) (forbidden at f). Let k′ be the largest k ∈ [f, s − 1]
with σ_k(r_q) ≠ r_{q+1}; then σ_{k′+1}(r_q) = r_{q+1}. By S4a, σ_{k′+1}(r_q) ∈ {σ_{k′}(r_q)} ∪ Iσ_{k′}(r_q), so e ∈ Iσ_{k′}: Ξ_{k′}(r_{q+1}) ▷
Ξ_{k′}(σ_{k′}(r_q)), and e is not forbidden at k′; so k′ ≠ f. Finally s − 1 − f = q + 1 ≤ m ≤ n − 1. □
### Corollary CHARGE-U
Let U(S) := the S4a switch events (k′, e) of S (e = (y, z), σ_{k′}(y) ≠ z = σ_{k′+1}(y)) such that e is forbidden at some state in
[k′ − n + 1, k′ − 1] ∩ S (UNFORBID-SWITCHES). Then for every x, the changes of COARSE_L(W(x)) on S number ≤ (n − 1)·(1 + |U(S)|).
Proof. ≤ n − 1 window changes (§5). A charged change at s gets (k′, e) ∈ U(S) by UNF (f ≥ k′ − n + 1 since k′ − f ≤ s − 1 − f ≤ n − 1), with
k′ + 1 ≤ s and s − 1 − k′ < s − 1 − f ≤ n − 1; so one event serves ≤ n − 1 values of s. □
- An edge that is forbidden and never switched into afterwards is never charged.

## 7. Not to sign: CONJECTURES and OPEN items
- CONJECTURE FS (the Lead's form, 08:32Z): if an Even edge is forbidden at k (L = −1), it is forbidden at no state ≥ k + n. DATA: 0
  violations (§9); max span 28 at n = 32. Not needed by §6 (persistent edges are never charged), and it would fail on any run that keeps
  one edge statically forbidden for ≥ n more states while other vertices move; no such run is known. OPEN.
- CONJECTURE UF-ONCE: in every run S, each Even vertex makes at most one unforbid-switch. Then |U(S)| ≤ n_E and, by CHARGE-U, every vertex's
  COARSE_{−1}(W) changes ≤ (n − 1)(n_E + 1) times per run. DATA: 0 violations in 101 U events (§9); thin. OPEN; the target of the next box.
- CONJECTURES LC2 (|OC(v)| ≤ |SL(v)|, the (score, level) pairs of v's rises; ≤ 2n) and PAIR-OC (no (score, level) at two offset changes of v
  in one stretch_D segment), after the death of LEVEL-COUNT's count form (§8): DATA only (note §15), thin. L-RED holds the kill pattern
  (one score rising at a, b, a, b > a, at three offset changes).
- OPEN (named in note §6): (R1) offset-preserving terminal changes (a port of R50's per-class chain to an offset class); (R2) offset changes
  per vertex per stretch_D (≥ Θ(√n) by mkalt, ≤ (n − 1) + 2^{B+1} by TWIN-GAP); (R3) ¬(h3_D) runs; (R4) epochs and stretch_D boundaries.
  Runs per phase (cut by fallbacks and λ_W changes) are not counted here.

## 8. DEAD (for the record; docs/si/DEAD.md box 17, 17b, 17c, 17d; all pinned in experiments/si/check.sh)
- Strict-raise lemma ("every twin change raises COARSE_L(W(v))"): a length-only W change; experiments/si/rund/instances/lenonly_n8.pg (sha1
  725c2766…).
- OFFSET-ONCE: a delay chain on the old route makes it better again; offret_n23.pg (sha1 8fdfc38d…); family mkalt.py K: K − 1 offset changes
  of one vertex in one stretch_D at n = Θ(K²).
- INC (rise levels at offset changes increase): a return paid by removing a high odd vertex; incdown_n23.pg (sha1 18a5d000…), levels [20, 19].
- LEVEL-COUNT, count form |OC(v)| ≤ |RL(v)| (L-RED's kill, reproduced by L-SI 13): a W-then-Ξ lag at one level;
  experiments/red/h3/instances/lcount_n23.pg (sha1 f86125a08f0e3b0caf3d825cb48e6dcdc0ee3b04), v = 1, OC 3, RL {18, 21}; lcount2_n23.pg
  (sha1 dd9847c6b19cb9f44af73bcc23de7ca2aca9a14c).

## 9. DATA (not proof; experiments/si/rund/, own scripts; N5 via experiments/new/box21/n5x.py step, read-only)
- §2-§4 (L-SI 12): rel.py, gap.py, piece.py; tables in note §4, §7, §11 (0 violations: lib41 / lib2o with random starts, random 𝒞^2O and
  𝒞^kO 6,000 each, the long runs; mutation controls gap.py MUT=1, rel.py MUT=2, piece.py MUT=1 bite).
- §5 (sched.py; logs/sched_long.txt, sched_lib41_rs2.txt): 0 violations of FRZ-SCH over all pairs s ≤ t (frz1_n24, frz3_n24, pftheta34_n32,
  lib41 S3 + 2 random starts: 2,693 / 2,661 / 7,784 / 31,636 clean pairs, most with content); every change classified as window or charged
  (0 unclassified). Controls: MUT=1 (schedule shifted by one state) and MUT=2 (forbidden-ness ignored) FAIL on all three long runs.
  |K_F|: 16, 17, 33 on runs of 24, 24, 34 transitions.
- §6 (sched.py with NOGEN=1; logs/fs_*.txt): FZ_EQ_V, UNF_V, SWITCH_INTO_FORB_V all 0. Ξ and W tuples checked to be in the same format (Ξ = W
  on 163 of 163 ungated vertex-states of frz1_n24, Ξ ⊴ W on all 288), so FZ_EQ_V is a real check.

| set | runs | states | S4a switches | |U| | max |U| per run | max U events per vertex per run | FS violations |
| --- | --- | --- | --- | --- | --- | --- | --- |
| frz1 / frz2 / frz3 (n 24, their .start) | 2 / 1 / 1 | 30 / 24 / 25 | 44 / 36 / 38 | 7 / 5 / 6 | 7 / 5 / 6 | 1 | 0 |
| pftheta34_n32 (S3) | 1 | 35 | 74 | 7 | 7 | 1 | 0 |
| lib41, S3 + 4 random starts | 243 | 1,230 | 1,514 | 63 | 6 | 1 | 0 |
| lib2o, S3 + 4 random starts | 121 | 828 | 956 | 30 | 3 | 1 | 0 |
| random 𝒞^2O 6,000 (seed 62) / 𝒞^kO 6,000 (seed 63) / 𝒞^kO 2,000 n 15-24 (seed 64) | 927 / 737 / 641 | 1,923 / 1,530 / 1,367 | 1,288 / 1,009 / 1,150 | 0 / 0 / 1 | 0 / 0 / 1 | 1 | 0 |
| lcount_n23, lcount2_n23, offret_n23, incdown_n23, offalt_K10 | 1 each | 4-25 | 10-177 | 0 | 0 | – | 0 |

- Forbidden (pair, state)s by gate class: long runs 304 of 304 with σ(x) ∈ F_D and z gated; lib41 RS4 2,652 of 2,946 so, 293 on different
  gates, 1 on the same gate.
- Reproduce (from experiments/si): `python3 -I rund/sched.py --one ../n5-exhaustive/instances/frz3_n24.pg ../n5-exhaustive/instances/frz3_n24.start`
  (SCHED PASS; with MUT=1, SCHED FAIL; both pinned in check.sh); `NOGEN=1 RS=4 python3 -I rund/sched.py --list ../new/box41/lib41.txt 2`;
  `NOGEN=1 K=2 python3 -I rund/sched.py --rand 6000 5 14 62`.
