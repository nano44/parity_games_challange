# Referee packet P-N5-NC: on every game, the D-factorisation and coarse agreement of RESULTS R55 need only "no disagreement vertex lies on its own cycle" (Lemma G_D-NC), and coarse values freeze after n − 1 arena steps of a run under that hypothesis (Lemma CR-D, Corollary FRZ-U_D)
Author: L-SI successor 11 (Opus 5.5; D15, D18, L37, L40), session_01FchPxfEZ9Fo56WrCZTvnXS. Written at the Lead's request of 05:05Z (Lead's
stamp). FROZEN at its commit (date -u); repairs go to a NEW fixes file.
- Sources:
  - docs/si/N5-2O-T-box16.md §6 (this lane, l-si b92f84d4): G_D-NC, FRZ-U_D.
  - docs/si/N5-FRONTIER-box15.md §2 (L-SI successor 10, l-si 0bd6fb23, file sha1 06cd6c9e…): Lemma CR-D, stated there with a proof by
    citation. This packet writes CR-D's proof out in full.
  - This packet governs where they differ.
- Labels (D18 / L40): PROVED (L-SI 11; CR-D's statement L-SI 10) / READING / DATA. D1: wrong until checked.
- Scope: structural lemmas for the candidate N5 (SPEC S1-S5 with FIX 1-4, docs/new/N5-ssi-global.md) on EVERY game. Nothing here bounds
  N5's running time on any class. Not a TARGET.md claim, not a gauntlet pass. G-N5-TIME stays OPEN.

## 0. What to sign
| § | statement | label | to sign |
| --- | --- | --- | --- |
| §2 | Lemma G_D-NC (b′): under (NC), R55's G_D (b) factorisation and avoidance | PROVED | yes |
| §2 | Lemma G_D-NC (c1′), (c2′): under (NC) ∧ (h3_D), R55's G_D (c1), (c2) | PROVED | yes |
| §3 | Lemma WM-G: W never drops at an in-phase S4a step (every game) | PROVED | yes |
| §3 | Lemma P^c_L and Lemma CR-D: under (i) coarse agreement and (ii) a constant W-cycle-node map, COARSE_L(W) freezes after n − 1 arena steps | PROVED | yes |
| §4 | Corollary FRZ-U_D: (NC) ∧ (h3_D) on a fallback-free run ⇒ COARSE_L(W) = COARSE_L(Ξ) frozen from the run's (n − 1)-th state, for L ≥ max M_D | PROVED | yes |
| §5 | what is not covered: (¬h-cyc), ¬(h3_D), LEN below L, Wo_D | READING | no |
| §6 | DATA (experiments/si/fb2o/gdnc.py) | DATA | no |

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
- New hypothesis. (NC) at k: no vertex of D_k lies on its own honest cycle, and no vertex of D_k lies on its own W-cycle. (h_D) implies
  (NC): a vertex on its own cycle visits itself, a vertex of D_k, after leaving itself.

## 2. Lemma G_D-NC (PROVED, every game)
Statement.
- (b′) Under (NC) at k: for v ∈ R_D with u := u(v), Ξ_k(v) = π_v ⊕ Ξ_k(u) and W_k(v) = π_v ⊕ W_k(u), and the honest and the W-play from u
  avoid π_v.
- (c1′), (c2′) Under (NC) and (h3_D) at k: R55 (c1) and (c2) hold as quoted in §1.
Proof.
- (b′): R55's proof, quoted in §1, with its one use of (h_D) replaced.
  - Its only use of (h_D) is "it would then follow x's play back to u ∈ D_k, against (h_D) at u".
  - A play is positional, so its sequence of vertices is a lasso. If u's play in a frame returns to u, u lies on the cycle of its own
    play in that frame. (NC) forbids exactly this, in both frames.
  - Visits of the play to other vertices of D_k are never used. So the proof holds under (NC).
- (c1′): R55's proof of (c1) (packet §1) uses (h_D) only through "A_v ∩ P(T) = ∅ (G_D (b): T's play avoids π_v)". (b′) supplies it, and
  (h3_D) supplies the common cycle node, as in R55.
- (c2′): R55's proof of (c2) uses (h_D) only through "by G_D (b), Ξ_k(v) = π_v ⊕ Ξ_k(u) and W_k(v) = π_v ⊕ W_k(u)" and "both plays from u
  avoid π_v". (b′) supplies both. The rest ((C2), (C4), lev(Ξ_k(u), W_k(u)) ≤ M_D ≤ L, and G_D (a) on F_D) is unchanged. □
- Under (NC), one vertex of D_k may route through another in either frame: (h_D) fails, (NC) holds. This is the case the lemma adds.

## 3. Lemma WM-G, Lemma P^c_L, Lemma CR-D (PROVED, every game)
Setting. S is a run of consecutive states k_0, …, k_1 inside one phase, all of whose transitions are S4a steps (no fallback). τ is
constant on S, so G_τ is one fixed one-player game. Ω_k := W_k, the valuation of σ_k in G_τ. L is a level with −1 ≤ L < ∞, and
COARSE := COARSE_L.
### Lemma WM-G
Statement. For every transition k → k+1 of S: Ω_{k+1} ⊵ Ω_k pointwise.
Proof.
- SPEC S4a: σ_{k+1} is Even's pointwise optimum in the arena H_k of G_τ, in which Even's v may use {σ_k(v)} ∪ Iσ_k(v).
- σ_k is a strategy of H_k. By (F1) on the one-player game H_k, Ω_{k+1} ⊵ Ω_k pointwise. □
(This is RESULTS R23 (g) WM; its proof is (F1) in G_τ, which holds on every game. It is written out to avoid citing a 𝒞^1O-labelled statement.)
### Lemma CR-D (statement: L-SI successor 10, docs/si/N5-FRONTIER-box15.md §2)
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

## 4. Corollary FRZ-U_D (PROVED, every game)
Statement. Let S be a run of consecutive S4a transitions inside one phase of N5 on any game, with (NC) and (h3_D) at every state of S,
and let L satisfy max_S M_D ≤ L < ∞, with L ≥ −1. Then COARSE_L(W) = COARSE_L(Ξ) on V at every state of S, and it is constant on S from
state k_0 + n − 1 on.
Proof. Lemma CR-D's hypotheses, at every state of S:
- (i) is G_D-NC (c2′), since M_D ≤ L at each state. (M_D < ∞ by (h3_D).)
- (ii): on F_D, λ_W = λ_Ξ by R55 (a). On R_D, (b′) gives λ_W(v) = λ_W(u(v)) and λ_Ξ(v) = λ_Ξ(u(v)), and λ_W(u(v)) = λ_Ξ(u(v)) by (h3_D).
  So λ_W = λ_Ξ on V. λ_Ξ is constant on the phase, so (ii) holds. □
- Scope, exactly:
  - every game and any number of disagreement vertices;
  - every fallback-free run inside a phase on which (NC) and (h3_D) hold at every state;
  - the coarse levels L ≥ max_S M_D.
- Relation to successor 10's Corollary CR-D′ (docs/si/N5-FRONTIER-box15.md §2): the same conclusion under (h_D) ∧ (h3_D). This replaces
  (h_D) by the weaker (NC).

## 5. Not to sign (READING)
- (¬h-cyc): a disagreement vertex on its own honest or W-cycle, where (NC) fails. On 𝒞^1O this is ¬H1 / ¬H2, which RESULTS R50 handles
  with kinds (KIND-MONO, CASC-B, CW-INT). Not covered here; the next lane item.
- ¬(h3_D): the cycle nodes of a disagreement vertex differ between the frames. M_D = ∞, and nothing coarse is claimed.
- Below L: the fine order of routes to different disagreement vertices (Δ-RT, R55 Remark). On 𝒞^1O this is LEN. FRZ-U_D says nothing
  there; it is the first failing link of the R50 chain beyond one Odd choice vertex (docs/si/N5-2O-T-box16.md §1).
- R55's Wo_D is not ported. Its proof uses (h_D) to put τ(u) ∈ F_D, and under routing the W-play from τ(u) can meet another disagreement
  vertex.

## 6. DATA (DATA, not proof): experiments/si/fb2o/gdnc.py (own checker; logs experiments/si/fb2o/logs/gdnc_*.txt)
At every state it checks (b′) (both equations and both avoidances) when (NC) holds, and (c2′) at L = max(M_D, −1) when (NC) and (h3_D)
hold. On every fallback-free run inside a phase with (NC) ∧ (h3_D) at every state, it checks FRZ-U_D's freeze from the (n − 1)-th state.
| set | states | (h_D) | (NC) | (NC) ∧ ¬(h_D) | (b′) checks / viol. | (c2′) checks / viol. | freeze runs / checks / viol. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| lib2o.txt (43 games with two Odd choice vertices) | 374 | 235 | 325 | 90 | 1,718 / 0 | 7,934 / 0 | 37 / 0 / 0 |
| lib41.txt games with ≥ 2 Odd choice vertices (93) | 1,039 | 389 | 603 | 214 | 3,229 / 0 | 17,604 / 0 | 57 / 0 / 0 |
| random 𝒞^2O, 40,000 games, n 5-12, half from random start pairs (seed 31) | 95,928 | 68,803 | 69,849 | 1,046 | 8,126 / 0 | 573,433 / 0 | 4,721 / 0 / 0 |
| random 𝒞^kO (k 2-4), 20,000 games, n 5-14 (seed 32) | 50,804 | 33,900 | 34,836 | 936 | 5,710 / 0 | 319,671 / 0 | 2,356 / 0 / 0 |
- Mutation control (MUT=1: (b′) checked without (NC)): fails on experiments/red/carry/instances/absmono_viol_n44.pg, 3 violations
  (logs/gdnc_mut_lib41.txt).
- Thin, stated plainly: the freeze is VACUOUS in all data. No fallback-free run under the hypotheses lasts n − 1 transitions, so Lemma CR-D
  and FRZ-U_D rest on their proofs. (b′) and (c2′) are exercised widely.
- Reproduce (from experiments/si/fb2o):
  - `python3 -I gdnc.py --list lib2o.txt`;
  - `python3 -I gdnc.py --list ../../new/box41/lib41.txt 2`;
  - `K=2 python3 -I gdnc.py --rand 40000 5 12 31`;
  - `python3 -I gdnc.py --rand 20000 5 14 32`.
  About 30 s in all. Each prints "GDNC PASS".
