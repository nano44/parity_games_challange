# Referee packet P-N5-H3: on every game, the honest and W-valuations agree in coarse form above M_D under (h3_D) alone, terminals change only inside an honest class, and coarse values freeze after n − 1 arena steps of every run with (h3_D) (Lemmas G_D-NC (b′), TC-CLASS, C2-H3, WM-G, P^c_L, CR-D; Corollary FRZ-U_H3)
Author: L-SI successor 11 (Opus 5.5; D15, D18, L37, L40), session_01FchPxfEZ9Fo56WrCZTvnXS. Written at the Lead's decision (2) of 05:30Z
(Lead's stamp). FROZEN at its commit (date -u); repairs go to a NEW fixes file.
- SUPERSEDES P-N5-NC (docs/si/P-N5-NC-box16.md, sha1 2036e7c8a8c177ad842fc2e0dbc2899de2b8495f, l-si eeb08be7), WITHDRAWN UNREVIEWED (Lead
  05:30Z, option (A)). Its (c2′) and FRZ-U_D are the special cases "(NC) ∧ (h3_D)" of C2-H3 and FRZ-U_H3 below. Its (b′), WM-G, P^c_L and
  CR-D are carried over unchanged. Its (c1′) is not carried over.
- Sources:
  - docs/si/N5-2O-T-box16.md §6 (l-si b92f84d4) and §7 (l-si 3e526214), this lane;
  - docs/si/N5-FRONTIER-box15.md §2 (L-SI successor 10, l-si 0bd6fb23, file sha1 06cd6c9e…), the statement of Lemma CR-D.
  This packet governs where they differ.
- Labels (D18 / L40): PROVED (L-SI 11; CR-D's statement L-SI 10) / READING / DATA. D1: wrong until checked.
- Scope: structural lemmas for the candidate N5 (SPEC S1-S5 with FIX 1-4, docs/new/N5-ssi-global.md) on EVERY game, with any number of
  Odd choice vertices. Nothing here bounds N5's running time on any class. Not a TARGET.md claim, not a gauntlet pass. G-N5-TIME stays
  OPEN.

## 0. What to sign
| § | statement | hypothesis | label | to sign |
| --- | --- | --- | --- | --- |
| §2 | Lemma G_D-NC (b′): R55's factorisation Ξ_k(v) = π_v ⊕ Ξ_k(u(v)), W_k(v) = π_v ⊕ W_k(u(v)), with both plays from u(v) avoiding π_v | (NC) at k | PROVED | yes |
| §3 | Lemma TC-CLASS: λ_Ξ(v) = λ_Ξ(u(v)), λ_W(v) = λ_W(u(v)); inside a phase a terminal change stays inside one honest class | none | PROVED | yes |
| §4 | Lemma C2-H3: COARSE_L(Ξ_k) = COARSE_L(W_k) on V for every M_D ≤ L < ∞, L ≥ −1 | (h3_D) at k | PROVED | yes |
| §5 | Lemma WM-G: W never drops at an in-phase S4a step | none | PROVED | yes |
| §5 | Lemma P^c_L, Lemma CR-D: under (i) coarse agreement and (ii) a constant W-cycle-node map on a fallback-free run, COARSE_L(W) freezes after n − 1 steps | (i), (ii) on the run | PROVED | yes |
| §6 | Corollary FRZ-U_H3: on a fallback-free run inside a phase, COARSE_L(W) = COARSE_L(Ξ), constant from the run's (n − 1)-th state on, for max M_D ≤ L < ∞ | (h3_D) at every state of the run | PROVED | yes |
| §7 | what is not covered | — | READING | no |
| §8 | DATA | — | DATA | no |

## 1. Setting and cited text
- RESULTS R55 setting, quoted (every game): "state k = (σ_k, τ_k); σ̄_k := SPEC S1's optimal Odd counterstrategy to σ_k; Ξ_k(v) := the value of
  the (σ_k, σ̄_k)-play from v; G_τ := G with every Odd vertex fixed to τ_k; W_k(v) := the value of the (σ_k, τ_k)-play from v; λ_Ξ, λ_W the
  cycle-node maps; … D_k := {Odd u : σ̄_k(u) ≠ τ_k(u)}; u(v) := the first vertex of D_k on v's (σ_k, τ_k)-play (v included), if any;
  R_D := {v : u(v) exists}, F_D := V ∖ R_D; π_v := the (σ_k, τ_k)-path from v to u(v), u(v) excluded. (h_D) at k: for every u ∈ D_k,
  neither the honest play nor the W-play from u visits D_k after leaving u. (h3_D) at k: λ_Ξ(u) = λ_W(u) for every u ∈ D_k. lev, COARSE_L,
  (C2), (C4) as in RESULTS R25; M_D := max over u ∈ D_k of lev(Ξ_k(u), W_k(u)), ⊥ if D_k = ∅."
- R55 (a), quoted: "Lemma G_D (a) (no hypothesis): for every state k and every v ∈ F_D, Ξ_k(v) = W_k(v)."
- R55 (b), quoted: "Lemma G_D (b) (under (h_D) at k): for v ∈ R_D with u := u(v), Ξ_k(v) = π_v ⊕ Ξ_k(u) and W_k(v) = π_v ⊕ W_k(u), and
  the honest and the W-play from u avoid π_v."
- R55 (c), quoted: "(c1) if y, z ∈ R_D and u(y) = u(z) = u, then π_y ⊕ Ξ_k(u) ⊴ π_z ⊕ Ξ_k(u) iff π_y ⊕ W_k(u) ⊴ π_z ⊕ W_k(u); (c2) for
  every L with M_D ≤ L < ∞ (L = ⊥ allowed when M_D = ⊥) and every v ∈ V, COARSE_L(Ξ_k(v)) = COARSE_L(W_k(v))".
- R55's proof of (b) (docs/new/P-N5-GD-box43.md §1, sha1 b898ff82…), quoted:
  - "Both plays from v follow π_v to u: the Odd vertices of π_v are outside D_k (u is the first vertex of D_k), so σ̄_k = τ_k there (HP_D).
    Continuation avoids π_v. Let x ∈ π_v. x's (σ_k, τ_k)-play is the suffix of π_v from x, then u; it meets D_k first at u, so by (HP_D)
    x's honest play is the same path to u. If u's honest play (resp. W-play) met x after leaving u, it would then follow x's play back to
    u ∈ D_k, against (h_D) at u. So each play from v is π_v followed by u's play, whose cycle lies off π_v; (V1) along π_v gives both
    equations."
- lev, COARSE_L and (C1)-(C4) (RESULTS R25 setting; docs/si/P-N5-FB-box7.md §1), quoted:
  - "lev(x, y) := ∞ if the cycle nodes differ; else the top rank of P(x) Δ P(y); else −1 if only the lengths differ; ⊥ if x = y";
  - "COARSE_L(x) := (c, P ∩ V_{>L}) for −1 ≤ L < ∞ … ⊴_L compares coarse values by reward(c) and then by the restricted path set";
  - "(C1) x ⊴ y ⇒ COARSE_L x ⊴_L COARSE_L y. (C2) COARSE_L x = COARSE_L y ⟺ lev(x, y) ≤ L. (C3) ⊴_L is antisymmetric on coarse values.
    (C4) COARSE_L(u ⊕ x) is a function of u and COARSE_L(x): it is (c, (P ∩ V_{>L}) ∪ ({u} if rank u > max(rank c, L)))".
  - Two consequences are used: (Cmono) is (C1); (Cstrict) COARSE_L a ≺_L COARSE_L b ⇒ a ◁ b, by (C1) and (C3) (if a ⊵ b then
    COARSE_L a ⪰_L COARSE_L b).
- RESULTS R17 (a): (V1) prefix equation, (V2) prefix monotonicity, (F1) "the optimum of a one-player game dominates every strategy of that
  game pointwise". Signed under a 𝒞^1O line; both referees of R55 confirmed them game-general ("one-player statements, applied to G_τ, its
  arenas …, which are one-player on every game", R55 premises).
- Phase: a maximal run of states with (λ_Ξ, τ) constant (R38 (a) KEY). Inside a phase every transition is an S4a step or an Even S4c
  fallback (an Odd fallback changes τ).
- Hypotheses named in this packet. (NC) at k: no vertex of D_k lies on its own honest cycle, and no vertex of D_k lies on its own W-cycle. (h_D) implies
  (NC): a vertex on its own cycle visits itself, a vertex of D_k, after leaving itself.
- Lasso fact (used in §4): a positional play is a lasso, and every vertex of its cycle is visited before its first repetition.
  So the prefix of a play up to its first visit of any vertex of its cycle, in particular its cycle node, repeats no vertex.

## 2. Lemma G_D-NC (b′) (PROVED, every game)
Statement. Under (NC) at k: for v ∈ R_D with u := u(v), Ξ_k(v) = π_v ⊕ Ξ_k(u) and W_k(v) = π_v ⊕ W_k(u), and the honest and the W-play from
u avoid π_v.
Proof. R55's proof, quoted in §1, with its one use of (h_D) replaced.
- Its only use of (h_D) is "it would then follow x's play back to u ∈ D_k, against (h_D) at u".
- A play is positional, so it is a lasso. If u's play in a frame returns to u, then u lies on the cycle of its own play in that frame.
  (NC) forbids exactly this, in both frames.
- Visits of the play to other vertices of D_k are never used. So the proof holds under (NC). □
- (NC) allows one vertex of D_k to route through another in either frame, where (h_D) fails. (b′) is not needed for §4-§6. It is the
  exact (not coarse) factorisation, kept for later use.

## 3. Lemma TC-CLASS (PROVED, every game)
Statement. At every state k and for every v ∈ R_D: λ_Ξ(v) = λ_Ξ(u(v)) and λ_W(v) = λ_W(u(v)). Hence, inside a phase, if v ∈ R_D at k and at
k + 1 and u_k(v) ≠ u_{k+1}(v), then λ_Ξ(u_k(v)) = λ_Ξ(v) = λ_Ξ(u_{k+1}(v)).
Proof.
- Both plays from v follow π_v to u(v). The Odd vertices of π_v are outside D_k, so σ̄_k = τ_k there (HP_D), and the Even vertices use σ_k
  in both plays.
- Plays are positional, so from u(v) on each play is u(v)'s play in its frame. So v's play and u(v)'s play end in the same cycle, in each
  frame, and have the same cycle node.
- λ_Ξ is constant on a phase. So λ_Ξ(u_k(v)) = λ_Ξ_k(v) = λ_Ξ_{k+1}(v) = λ_Ξ(u_{k+1}(v)). □
- Reading: a vertex can move only between disagreement vertices of the same honest class U_c = λ_Ξ^{-1}(c). Disagreement vertices in
  different honest classes never exchange vertices.

## 4. Lemma C2-H3 (PROVED, every game)
Statement. Let (h3_D) hold at k, and let L satisfy M_D ≤ L < ∞ and L ≥ −1 (L = −1 when M_D = ⊥). Then COARSE_L(Ξ_k(v)) = COARSE_L(W_k(v))
for every v ∈ V. No (h_D) and no (NC) is assumed.
Proof.
- v ∈ F_D: Ξ_k(v) = W_k(v), by R55 (a).
- v ∈ R_D:
  - Let u := u(v) and c := λ_Ξ(u) = λ_W(u), by (h3_D). By TC-CLASS, c is v's cycle node in both frames.
  - For a frame F (honest or W), let P_F(v) be the vertices of v's F-play before its first visit of c that are ranked above c. This is
    the path set of v's F-value.
  - Case c ∈ π_v: both plays follow π_v up to c, so P_Ξ(v) = P_W(v). COARSE_L ignores lengths, so the coarse values are equal.
  - Case c ∉ π_v:
    - v's F-play is π_v followed by u's F-play, and c is first visited inside u's F-play.
    - So the prefix before c is π_v followed by Q_F, the prefix of u's F-play before c.
    - Q_F ∩ π_v = ∅: a common vertex would be repeated before the first visit of c, against the lasso fact (§1).
    - Hence P_F(v) = (π_v ∩ V_{>c}) ⊔ (Q_F ∩ V_{>c}) = (π_v ∩ V_{>c}) ⊔ P_F(u).
  - Coarse agreement:
    - lev(Ξ_k(u), W_k(u)) ≤ M_D ≤ L. By (C2), COARSE_L(Ξ_k(u)) = COARSE_L(W_k(u)): both have cycle node c, and
      P_Ξ(u) ∩ V_{>L} = P_W(u) ∩ V_{>L}.
    - So COARSE_L(Ξ_k(v)) = (c, ((π_v ∩ V_{>c}) ⊔ P_Ξ(u)) ∩ V_{>L}) = (c, ((π_v ∩ V_{>c}) ⊔ P_W(u)) ∩ V_{>L}) = COARSE_L(W_k(v)).
□
- Relation to R55: R55 (c2) is this statement under the stronger (h_D) ∧ (h3_D). R55's proof goes through the exact factorisation (b),
  which needs (h_D) or (NC). The coarse statement needs only the path set above c, which factors through u(v) whatever the play does
  after c.

## 5. Lemma WM-G, Lemma P^c_L, Lemma CR-D (PROVED, every game)
Setting. S is a run of consecutive states k_0, …, k_1 inside one phase, all of whose transitions are S4a steps (no fallback). τ is
constant on S, so G_τ is one fixed one-player game. Ω_k := W_k, the valuation of σ_k in G_τ. L is a level with −1 ≤ L < ∞, and
COARSE := COARSE_L.
### Lemma WM-G
Statement. For every transition k → k+1 of S: Ω_{k+1} ⊵ Ω_k pointwise.
Proof.
- SPEC S4a: σ_{k+1} is Even's pointwise optimum in the arena H_k of G_τ, in which Even's v may use {σ_k(v)} ∪ Iσ_k(v).
- σ_k is a strategy of H_k. By (F1) on the one-player game H_k, Ω_{k+1} ⊵ Ω_k pointwise. □
(This is RESULTS R23 (g) WM; its proof is (F1) in G_τ, which holds on every game. It is written out to avoid citing a 𝒞^1O-labelled statement.)
### Lemma CR-D (statement: L-SI successor 10, docs/si/N5-FRONTIER-box15.md §2, l-si 0bd6fb23, sha1 06cd6c9e…)
Statement. Suppose that at every state of S:
- (i) COARSE(Ξ_k(v)) = COARSE(W_k(v)) for every v ∈ V;
- (ii) the W-cycle-node map v ↦ λ_W(v) is the same at every state of S.
Then COARSE(Ω_t) = COARSE(Ω_{k_0+n−1}) for every t ∈ S with t ≥ k_0 + n − 1.
Notation.
- For a simple path r = (r_0, …, r_m) of G_τ ending at a vertex u with λ_W(u) = u, let value(r) := (u, P(r), m), where P(r) := {r_i : i < m,
  rank(r_i) > rank(u)}. This is the S1 value of a play that follows r and then stays on u's W-cycle.
- Ω^c_k := COARSE(Ω_k).
- (MON): Ω^c_{k+1} ⪰ Ω^c_k on S, by WM-G and (Cmono).
- (V2c): if COARSE(p) ⪯ COARSE(q) and x lies in neither path set, then COARSE(x ⊕ p) ⪯ COARSE(x ⊕ q). Proof: if the cycle nodes differ,
  x ⊕ keeps them. If they agree, (C4) adds x to both coarse path sets or to neither.
- By (ii), every W-cycle node u at k_0 has Ω_k(u) = (u, ∅, 0) at every k ∈ S.
### Lemma P^c_L
Statement. For every j with k_0 + j ∈ S, every vertex x, and every simple path r of G_τ from x to a vertex u with λ_W(u) = u, with at most
j edges: Ω^c_{k_0+j}(x) ⪰ COARSE(value(r)).
Proof. Induction on j. This is R20 (d)'s Lemma P^c (docs/new/P-N5-XA-box27.md §5, with its fixes XA-3, XA-4, N-XA-1), transcribed:
- R20's Lemma C is replaced by (i) and (MON).
- R20's §1 "W's cycle-node map is constant on S" is replaced by (ii).
- R20's case B-fallback is absent, since S has no fallback.
- Base j = 0: r = (u), x = u, and Ω_{k_0}(u) = (u, ∅, 0) = value(r).
- Step from k := k_0 + j to k + 1 (k + 1 ∈ S):
  - Let r be a path with ≤ j + 1 edges. If r has no edge, x = u and Ω_{k+1}(u) = (u, ∅, 0).
  - Otherwise r = x → z → r′, with r′ simple from z, avoiding x, with ≤ j edges. IH: Ω^c_k(z) ⪰ COARSE(value(r′)).
  - Let a := σ_k(x) if x is Even. If x is Odd, a := τ(x), its only edge in G_τ, so z = a (XA-4).
- Case A: Ω^c_k(z) ⪯ Ω^c_k(a). (This covers every Odd x.)
  - A1, x ≠ λ_W(x): (V1) gives Ω_k(x) = x ⊕ Ω_k(a).
    - x ∉ P(value(r′)), since r′ avoids x.
    - x ∉ P(Ω_k(a)): if a's W-play passes x, then x lies on its own W-cycle but is not its cycle node, so it is ranked below that cycle
      node and is in no path set.
    - value(r) = x ⊕ value(r′), since both have cycle node u and x ∉ r′.
    - So COARSE(value(r)) ⪯ x ⊕_c Ω^c_k(a) = Ω^c_k(x) ⪯ Ω^c_{k+1}(x), by the IH, Case A, (V2c) and (MON).
  - A2, x = λ_W(x): Ω_k(x) = (x, ∅, 0). x ≠ u, since r is simple and has an edge.
    - reward(x) > reward(u): the cycle node decides, Ω^c_k(x) ≻ COARSE(value(r)), and (MON) carries this to k + 1.
    - reward(x) < reward(u): a lies on x's W-cycle, so Ω_k(a) has cycle node x, while value(r′) has cycle node u. Then
      COARSE(value(r′)) ≻ Ω^c_k(a) ⪰ Ω^c_k(z) ⪰ COARSE(value(r′)), a contradiction. Rewards are injective, so there is no tie.
- Case B: Ω^c_k(z) ≻ Ω^c_k(a). Then x is Even (an Odd x has z = a).
  - By (i), COARSE(Ξ_k(z)) ≻ COARSE(Ξ_k(a)), so Ξ_k(z) ▷ Ξ_k(σ_k x) by (Cstrict). So (x, z) ∈ Iσ_k, and σ̂ := σ_k[x ↦ z] is a strategy
    of the arena H_k.
  - The transition is an S4a step, so (F1) gives Ω_{k+1}(x) ⊵ val_σ̂(x), the value of x's (σ̂, τ)-play.
  - Let c′ := λ_W(z), and let π be z's W-path from z to c′, both included. P(π) := the vertices of π more relevant than c′.
  - B1, x ∉ π:
    - x not on c′'s W-cycle: x's σ̂-play is x followed by z's W-play, which does not pass x. So val_σ̂(x) = x ⊕ Ω_k(z), and
      Ω^c_{k+1}(x) ⪰ x ⊕_c Ω^c_k(z) ⪰ x ⊕_c COARSE(value(r′)) = COARSE(value(r)), by (Cmono), (C4), the IH and (V2c) (x ∉ π ∪ r′).
    - x on c′'s W-cycle (so λ_W(x) = c′, and a is x's successor on that cycle, with P(Ω_k(a)) = ∅). Ω^c_k(z) ≻ Ω^c_k(a) with the same
      cycle node c′ means P(π) ≠ ∅ with an even top t. (Coarse values ignore length, so R20's length cases (β), (γ) are coarse ties
      and cannot occur here.) Then x's σ̂-play closes the cycle x → z → π → c′ → (the old arc) → x, whose top is t. So val_σ̂(x) has cycle
      node t, with reward(t) > reward(c′). By (F1), λ_W(x) at k + 1 has reward ≥ reward(t), so it differs from c′, against (ii).
  - B2, x ∈ π: then λ_W(x) = c′ (x's W-play is the rest of π). x's σ̂-play is the cycle Z := x, z, π[z..x). Let D := the vertices of Z more
    relevant than c′.
    - Ω_k(z) = π[z..x) ⊕ Ω_k(x) and Ω_k(x) = x ⊕ Ω_k(a) or, if x = c′, Ω_k(x) = (c′, ∅, 0).
    - So COARSE(Ω_k(z)) and COARSE(Ω_k(a)) differ exactly by the vertices of D above L. Ω^c_k(z) ≻ Ω^c_k(a) means D has a vertex above
      L and the top t of D is even.
    - Every vertex of Z outside D is ranked at most c′, so t = top(Z), and val_σ̂(x) has cycle node t with reward(t) > reward(c′). By
      (F1), λ_W(x) changes at k + 1, against (ii).
    - (R20's sub-case "D = ∅" is a coarse tie here, so it is excluded by Case B.) □
### Proof of Lemma CR-D
- Let t ∈ S with t ≥ k_0 + n − 1, and x ∈ V. x's W-play at t follows a simple path r_t of G_τ to λ_W(x), and λ_W(x) is a W-cycle node at
  every state of S, by (ii). So Ω_t(x) = value(r_t), and r_t has ≤ n − 1 edges.
- By P^c_L at j = n − 1, Ω^c_{k_0+n−1}(x) ⪰ COARSE(value(r_t)) = Ω^c_t(x).
- By (MON) iterated from k_0 + n − 1 to t, Ω^c_t(x) ⪰ Ω^c_{k_0+n−1}(x).
- By (C3) the two coarse values are equal. □

## 6. Corollary FRZ-U_H3 (PROVED, every game)
Statement. Let S be a run of consecutive S4a transitions (no fallback) inside one phase of N5 on any game, with (h3_D) at every state of S.
Let L satisfy max_S M_D ≤ L < ∞ and L ≥ −1. Then COARSE_L(W) = COARSE_L(Ξ) on V at every state of S, and it is constant on S from state
k_0 + n − 1 on.
Proof. Lemma CR-D's hypotheses, at every state of S:
- (i) is C2-H3, since M_D ≤ L at each state. (M_D < ∞ by (h3_D).)
- (ii):
  - on F_D, λ_W = λ_Ξ by R55 (a);
  - on R_D, TC-CLASS gives λ_W(v) = λ_W(u(v)) and λ_Ξ(v) = λ_Ξ(u(v)), and λ_W(u(v)) = λ_Ξ(u(v)) by (h3_D).
  So λ_W = λ_Ξ on V. λ_Ξ is constant on the phase, so (ii) holds.
Lemma CR-D gives the freeze. □
- Scope, exactly:
  - every game, and any number and any cycle configuration of the disagreement vertices: a vertex of D_k on its own honest or W-cycle
    (¬h-cyc), and one routing through another (¬h-route), are both allowed;
  - every fallback-free run inside one phase on which (h3_D) holds at every state;
  - the coarse levels L with max_S M_D ≤ L < ∞.
- Special cases: successor 10's Corollary CR-D′ ((h_D) ∧ (h3_D)) and the withdrawn P-N5-NC's FRZ-U_D ((NC) ∧ (h3_D)).

## 7. Not to sign (READING)
- ¬(h3_D): a disagreement vertex u with λ_Ξ(u) ≠ λ_W(u). Then M_D = ∞, and nothing coarse is claimed.
  - On 𝒞^1O this is ¬H3, the case (c_w ≻ c_θ) in which RESULTS R50 uses kinds (H-PATH, KIND-MONO, CASC-B, CW-INT) and its full κ-freeze
    above m*.
  - The port to two or more disagreement vertices is the next lane item.
- Below L: the fine order of routes inside one honest class with two or more disagreement vertices (Δ-RT, R55 Remark). On 𝒞^1O this is
  R50's LEN, the first failing link of its chain beyond one Odd choice vertex (docs/si/N5-2O-T-box16.md §1, §5). By TC-CLASS, this is
  the only place where vertices can change terminal.
- R55's Wo_D is not ported. Its proof uses (h_D) to put τ(u) ∈ F_D.

## 8. DATA (DATA, not proof): experiments/si/fb2o/ (own checkers; logs/gdnc_*.txt, gdnc_h3_*.txt, tcdir_*.txt, hcyc_*.txt)
- gdnc.py checks (b′) at every (NC) state. With H3ONLY=1 it checks C2-H3 at every (h3_D) state at L = max(M_D, −1). It also checks
  FRZ-U's freeze on fallback-free runs.
- tcdir.py counts terminal changes across honest classes (TCCLASS_V).
| set | states | (h3_D) | (h3_D) ∧ ¬(NC) | C2-H3 checks / viol. | (b′) checks / viol. |
| --- | --- | --- | --- | --- | --- |
| lib2o.txt (43 games with two Odd choice vertices) | 374 | 314 | 3 | 7,972 / 0 | 1,718 / 0 |
| lib41.txt games with ≥ 2 Odd choice vertices (93) | 1,039 | 526 | 23 | 18,323 / 0 | 3,229 / 0 |
| random 𝒞^2O, 40,000 games, n 5-12, half from random start pairs (seed 31) | 95,928 | 72,780 | 7,658 | 637,911 / 0 | 8,126 / 0 |
| random 𝒞^kO (k 2-4), 20,000 games, n 5-14 (seed 32) | 50,804 | 36,271 | 4,124 | 358,424 / 0 | 5,710 / 0 |
- Of the C2-H3 checks, 104,000 lie at states where (NC) fails (38; 719; 64,478; 38,753 by row). C2-H3 is exercised outside P-N5-NC's
  hypothesis.
- Mutation controls, both failing as required:
  - MUTL=1 (C2-H3 one level below M_D) on lib41: 2,504 violations;
  - MUT=1 ((b′) without (NC)) on lib41: 3 violations, on absmono_viol_n44.pg.
- TC-CLASS: 0 cross-class terminal changes (tcdir.py: 150,000 random 𝒞^2O from random start pairs; lib41).
- Independent check (L-COMP, l-comp 27d38816, as relayed by the Lead 05:30Z): G_D-NC 0 violations on 100,000 random 𝒞^kO runs.
- Thin, stated plainly:
  - The freeze of CR-D / FRZ-U_H3 is vacuous in this lane's data: no fallback-free run under the hypotheses lasts n − 1 transitions.
    L-COMP reports the first non-vacuous run (frz1_n24.pg, n 24), in the (h_D) regime.
  - CR-D and FRZ-U_H3 rest on their proofs.
- Reproduce (from experiments/si/fb2o):
  - `H3ONLY=1 python3 -I gdnc.py --list lib2o.txt`;
  - `H3ONLY=1 python3 -I gdnc.py --list ../../new/box41/lib41.txt 2`;
  - `H3ONLY=1 K=2 python3 -I gdnc.py --rand 40000 5 12 31`;
  - `H3ONLY=1 python3 -I gdnc.py --rand 20000 5 14 32`.
  Each prints "GDNC PASS". MUTL=1 or MUT=1 make it print "GDNC FAIL".
