# Referee packet P-N5-RHO: θ's path set changes at most deg(o) times after |U| − 2 fallbacks of a phase, at most |U| + deg(o) − 3 times in a fallback-free HN run, so P(θ)-changes over the HN states of a phase are polynomial in n and N_HN (Y-FORM, HAT-FREEZE, RHO-TAIL, BF-F, FREEZE-F, RHO-HN, Corollary HN-POLY) (box 40)
L-NEW successor 19 (Opus 5.5, D15/D18, L37/L40), session_011reTXakSJCcwLhC4i9ZpkB. Written 2026-10-25 16:42Z by date -u, at the Lead's
request of 16:05Z (Lead's stamp): "Packet P-N5-RHO: yes, write it. File docs/new/P-N5-RHO-box40.md, new, frozen, self-contained."
Frozen at this commit: corrections go in a fixes file, never here.
- Source: docs/new/N5-RHO-box39.md §1-§4 (working doc, L-NEW successor 18, l-new 1b6239fb). This packet re-states and re-proves
  everything it signs. Where the packet and the source differ, the packet governs. Differences from the source (none changes a
  statement): (i) "F1" in BF-F is (F1) of RESULTS R17 (a), not Lemma F1 of RESULTS R21 (e); (ii) Lemma S (a) is cited together with
  RESULTS R21 (a), because R18 signs Lemma S with gaps; (iii) the ¬H1 half of Y-FORM is proved from the valuation's definition;
  (iv) (A0) (additivity at c_θ) is stated and used where a play may pass c_θ; (v) RHO-TAIL counts transitions t → t+1 with
  t > g_{|U|−2}, and the run count in RHO-HN is spelled out; (vi) HN-POLY uses BRK-POLY′ (i) only in the weak form (i′) (REFEREE's
  GAP PFZ-1 on P-N5-PFZ-ext, relayed by the Lead 16:23Z), so the θ-term of HN-POLY is ρ_HN + (ρ_HN + N_HN)·max(|U| − 2, 0).
- Labels (D18/L40): PROVED (L-NEW succ. 18, re-checked and filled in by L-NEW succ. 19; unrefereed), OPEN, DATA.
- Scope. Every statement is about the candidate N5 (SPEC S1-S5, docs/new/N5-ssi-global.md) on 𝒞^1O, inside one phase. Nothing here is a
  running-time bound for N5, a TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN. N_HN (HN stretches per phase) is a PARAMETER;
  no bound on it is claimed here (for τ(o) ≠ o see §7).

## To sign, and what is not to sign
| § | statement | label | uses (P) | uses P-N5-PFZ / -ext (pinned 283bcb67 / c61ecc4e, in review) |
| --- | --- | --- | --- | --- |
| §1 | Lemma Y-FORM (θ's signed weight at H1 states; P(θ) = ∅ at ¬H1 states) | PROVED | no | (A) only |
| §2 | Lemma HAT-FREEZE (a)-(c) (M frozen on F ∩ U after |U| − 2 fallbacks of a phase; θ free) | PROVED | no | (A), (M2′), FB-ROUND |
| §3 | Theorem RHO-TAIL (≤ deg(o) P(θ)-changes after g_{|U|−2}) | PROVED | no | (A), (M2′), FB-ROUND (via §2) |
| §4 | Lemma BF-F (an S4a step between HN states is a Bellman-Ford round on F ∩ U) | PROVED | no | (A), (M1′), (M2′) |
| §5 | Theorem FREEZE-F (a)-(c) (fallback-free HN runs) | PROVED | no | (A), (M2′) |
| §6 | Theorem RHO-HN (ρ_HN ≤ (N_HN + |U| − 2)(|U| + deg(o) − 3) + deg(o)) | PROVED | no | (A), (M2′), FB-ROUND |
| §6 | Corollary HN-POLY (HN breaks, crossings, fallbacks, θ-changes per phase ≤ poly(n, N_HN)) | PROVED | no | also BRK-POLY′ (i′), (ii) (ext §3) |
- (P) (R18's one-player premise) is used nowhere. Lemma S (a) of R18 (d) is not (P): it is VJ00 (11) on G (R18 (d) text); RESULTS R21 (a)
  gives the same fact as a second source.
- P-N5-PFZ and P-N5-PFZ-ext are pinned and in review. The facts (A), (M1′), (M2′) and Lemma FB-ROUND are restated in §0 with their
  short proofs, so that a referee can check this packet alone; the signature of FB-ROUND itself belongs to P-N5-PFZ. Corollary HN-POLY
  depends on BRK-POLY′ (P-N5-PFZ-ext §3) and is conditional on that packet's signature.
- §7 is NOT TO SIGN (OPEN items and the lane's N_HN result for τ(o) ≠ o, offered separately). §8 is data.

## 0. Objects, notation and dependencies
- N5, valuations x = (c, P, ℓ), Even's order ⊴ / ◁, rank, reward, Iσ_k, the honest frame Ξ_k (against Odd's optimal counterstrategy σ̄_k),
  λ_k, next_k, 𝒞^1O, θ, c_θ, R_k, R̄_k, F_k, routes π_z, H1, H2, HN, PHASE, HN STRETCH, CROSSING, BREAK: exactly as in P-N5-PFZ §0
  (= RESULTS R39's setting). Summary of the order: first reward(c), then the signed weight Σ_{u∈P} sgn(u)·2^rank(u) (sgn(u) = +1 for
  Ω(u) even, −1 for odd), then ℓ (shorter is better for Even iff Ω(c) is even). P(x) consists of vertices of rank > rank(c); the cycle
  node's own value is (c, ∅, 0). W_k := the valuation of the (σ_k, τ)-play; w := W(o); c_w := λ_W(o).
- In a phase, every transition has τ unchanged, so it is an S4a step (σ_{k+1} = Even's arena optimum against τ, SPEC S4a; S4b leaves τ
  unchanged) or an Even S4c fallback (an Odd fallback changes τ, SPEC S4c and FIX 3).
- U := λ^{-1}(c_θ), constant on a phase; o, c_θ ∈ U. Û := U ∖ {o}. M_t(z) := Σ_{u∈P(Ξ_t z)} sgn(u)·2^rank(u) for z ∈ U.
  wt(v) := sgn(v)·2^rank(v) if rank(v) > rank(c_θ), else 0; wt(A) := Σ_{v∈A} wt(v). s_θ := +1 if Ω(c_θ) is odd, −1 if even.
- G_Û: the graph on Û in which every Even v ∈ Û ∖ {c_θ} keeps its edges into Û, every Odd v ∈ Û ∖ {c_θ} keeps its forced edge if it
  lies in Û, and c_θ is a sink. MoptÛ(z) := max{wt(p ∖ {c_θ}) : p a simple path in G_Û from z to c_θ} (undefined if there is none).
  For A ⊆ U ∖ {o} with c_θ ∈ A, G[A] is defined in the same way on A.
- g_1 < g_2 < … are the in-phase Even S4c fallback transitions of the phase (g_j → g_j + 1, both ends in the phase). "t > g_j" is about
  states; "t > g_0" means every state of the phase.
- deg(o) := the out-degree of o (≥ 2 on 𝒞^1O). Y_t := succ(o) ∩ U ∩ F_t. N_HN := the number of HN stretches of the phase. ρ_HN := the
  number of transitions of the phase with both ends HN at which P(θ) changes; ρ_S := the same inside the HN stretch S.

### Facts used throughout (restated from P-N5-PFZ §1, with proofs)
- (A) For every state t and z ∈ U ∖ {c_θ}: next_t(z) ∈ U and M_t(z) = wt(z) + M_t(next_t z); also ℓ(Ξ_t z) = 1 + ℓ(Ξ_t next_t z).
  Proof: λ_t(z) = c_θ ≠ z, so (V1) (RESULTS R17 (a)) gives Ξ_t(z) = z ⊕ Ξ_t(next_t z) with the same cycle node; ⊕ adds z to P iff
  rank(z) > rank(c_θ) and adds 1 to ℓ. No double count: if z ∈ P(Ξ_t next_t z), z lies on its own play's cycle, whose top is c_θ, so
  rank(z) < rank(c_θ), wt(z) = 0 and z is in neither P.
- (A0) (filled in) The equation M_t(z) = wt(z) + M_t(next_t z) also holds at z = c_θ: wt(c_θ) = 0, and next_t(c_θ) lies on c_θ's own
  cycle, whose top is c_θ, so P(Ξ_t next_t c_θ) = ∅ and both sides are 0.
- (M1′) For valuations x, x′ with cycle node c_θ: x ⊴ x′ ⇔ (wt(P(x)), s_θ·ℓ(x)) ≤ (wt(P(x′)), s_θ·ℓ(x′)) lexicographically (same
  reward; then the signed weight of P, whose vertices all have rank > rank(c_θ); then the length in the direction s_θ). In particular,
  for y, z ∈ U at states t, t′ of one phase, Ξ_t(y) ⊴ Ξ_{t′}(z) ⇒ M_t(y) ≤ M_{t′}(z).
- (M2′) For z ∈ U and every in-phase transition t → t+1: M_{t+1}(z) ≥ M_t(z). (R15 (a): Ξ_t ⊴ Ξ_{t+1}; then (M1′).)
- (INJ) For z ∈ U, P(Ξ_t z) is a set of vertices of rank > rank(c_θ), and the signed weight is injective on such sets (distinct powers of
  2). So P(Ξ_t z) = P(Ξ_{t′} z) ⇔ M_t(z) = M_{t′}(z). In particular P(θ) changes at t → t+1 iff M(o) does.
- Lemma FB-ROUND (P-N5-PFZ §1; signed there, restated): at an in-phase Even S4c fallback k → k+1, for every Even v ∈ U ∖ {c_θ} and every
  successor x ∈ U of v: M_{k+1}(v) ≥ wt(v) + M_k(x). Proof: if Ξ_k(x) ⊴ Ξ_k(σ_k v), (M1′), (A) and (M2′) give wt(v) + M_k(x) ≤
  M_k(v) ≤ M_{k+1}(v). Otherwise (v, x) ∈ Iσ_k, so S4c sets σ_{k+1}(v) = x* with Ξ_k(x*) ⊵ Ξ_k(x); λ_{k+1}(v) = c_θ ≠ v, so (A) at
  k+1 gives x* ∈ U and M_{k+1}(v) = wt(v) + M_{k+1}(x*) ≥ wt(v) + M_k(x*) ≥ wt(v) + M_k(x) ((M2′), (M1′)).
- (HP) (filled in; honest plays at H1) On 𝒞^1O the honest play (σ_t, σ̄_t) and the (σ_t, τ)-play from any vertex agree until their first
  visit of o (they differ only at o). Hence: z ∈ F_t ⇒ z's honest play avoids o. Under H1, c_θ ∈ F_t (c_θ's honest play is its
  cycle, which avoids o), and for z ∈ R_t the honest play is π_z followed by o's honest play, which never returns to o and never meets
  π_z; so λ_t(z) = c_θ, i.e. R̄_t ⊆ U (the route form, re-proved in P-N5-PFZ §4).
- (SP) (filled in) For z ∈ U ∖ {c_θ}, the honest play of z up to its first visit of c_θ is a simple path in U, so 1 ≤ ℓ(Ξ_t z) ≤ |U| − 1.
  (The play ends on c_θ's cycle; it visits c_θ before any repetition; its vertices are in U by (A).)

### Dependencies (statement used / where it lives / status)
| tag | statement used | location | status |
| --- | --- | --- | --- |
| (V1) | if λ(v) ≠ v, the value of v is v ⊕ (value of next(v)) | VJ00 BRICS RS-00-48 §4.2; RESULTS R17 (a) | LANDED |
| (F1) | the optimum of a one-player game dominates every strategy of that game pointwise (applied to S4a's arena H_k with τ fixed) | RESULTS R17 (a) (as R39 (e) cites it) | LANDED |
| R15 (a), (d) | Ξ_k ⊴ Ξ_{k+1} pointwise; σ_{k+1}(v) ∈ {σ_k(v)} ∪ Iσ_k(v) | RESULTS R15 | LANDED |
| Lemma S (a) | Ξ_σ is the pointwise minimum of V_{σ,τ′} over Odd's strategies τ′ (VJ00 (11) on G; no (P)) | RESULTS R18 (d) | LANDED (signed with gaps S1, S2, G-1OA-6) |
| XW | Ξ_k ⊴ W_k pointwise (Odd's best reply σ̄_k is pointwise optimal in G_{σ_k}) | RESULTS R21 (a) | LANDED |
| G (a) | off R, Ξ = W (no (h) needed) | RESULTS R19 (a) | LANDED |
| KEY | a (λ_Ξ, τ)-phase is a joint λ-phase | RESULTS R38 (a) | LANDED (names the setting only) |
| SPLIT | at an in-phase transition with H1 ∧ ¬H2 at k, a non-fallback has R_k ⊆ R_{k+1} | RESULTS R39 (a) | LANDED |
| F-FLAT | at an in-phase Even fallback with H1 ∧ ¬H2 at k, θ_{k+1} = θ_k | RESULTS R39 (c) | LANDED |
| EPOCH | X_S ≤ 2(n − 1)(B_S + 1), f_S ≤ K(X_S + 1) + X_S, K := n_E(2n − 1) (premise FB-INT, RESULTS R38 (d)) | RESULTS R39 (b) | LANDED |
| NE-COUNT (c) | τ(o) = o: N_HN ≤ ⌊T_ph/2⌋ + 1 ≤ ⌊T*/2⌋ + 1 (TOGGLE-COUNT, RESULTS R34 (e)) | RESULTS R39 (f) | LANDED |
| (A), (M1′), (M2′), FB-ROUND | as above | P-N5-PFZ §1 | in review (pinned 283bcb67); SIGNED by REFEREE 9 (R-N5-PFZ 8595343) and REFEREE-2 9 (R2-N5-PFZ 37e55fd), per the Lead's 16:23Z relay; not landed |
| BRK-POLY′ (i′), (ii) | θ_S ≤ ρ_S + (ρ_S + 1)·max(|U| − 2, 0) (the weak form, see below); B_S ≤ (ρ_S + 1)(2n² − 1) | P-N5-PFZ-ext §3 | in review (pinned c61ecc4e); REFEREE R-N5-PFZ 8595343: SIGNED except GAP PFZ-1 on (i) |
- Not used: WCH (RESULTS R38 (b)), NE-COUNT (a)/(b), RESULTS R36, P-N5-NEB, P-N5-LV, P-N5-LV2.
- Item → dependencies:
  | item | depends on |
  | --- | --- |
  | §1 Y-FORM | (A), (HP), Lemma S (a) / XW |
  | §2 HAT-FREEZE | (A), (A0), (M2′), FB-ROUND, (HP), (SP) |
  | §3 RHO-TAIL | Y-FORM, HAT-FREEZE, (M2′), (INJ) |
  | §4 BF-F | (A), (A0), (M1′), (M2′), SPLIT, (F1), G (a), XW, (HP) |
  | §5 FREEZE-F | BF-F, (A), (M2′), SPLIT, Y-FORM, (HP), (SP) |
  | §6 RHO-HN | F-FLAT, RHO-TAIL, FREEZE-F |
  | §6 HN-POLY | RHO-HN, BRK-POLY′, EPOCH, NE-COUNT (c) |

## 1. Lemma Y-FORM (PROVED)
Statement. Let t be a state of a phase.
- (a) If H1 holds at t: σ̄_t(o) ∈ Y_t and M_t(o) = wt(o) + min_{y∈Y_t} M_t(y).
- (b) If H1 fails at t: P(θ_t) = ∅, so M_t(o) = 0.
Proof.
- (a) Under H1, o is not on its honest cycle, so λ_t(o) = c_θ ≠ o and (A) gives σ̄_t(o) ∈ U and M_t(o) = wt(o) + M_t(σ̄_t o).
  σ̄_t(o)'s honest play is the rest of o's honest play, which never returns to o; by (HP) its (σ_t, τ)-play does not reach o either, so
  σ̄_t(o) ∈ F_t. So σ̄_t(o) ∈ Y_t and M_t(o) ≥ wt(o) + min_{y∈Y_t} M_t(y).
  - For y ∈ Y_t, let τ′ be Odd's strategy with τ′(o) = y (all other Odd vertices are forced). y ∈ F_t, so y's (σ_t, τ)-play avoids o,
    and so does its (σ_t, τ′)-play (the same play). Hence V_{σ_t,τ′}(y) = W_t(y) = Ξ_t(y) (G (a)), with cycle node c_θ (y ∈ U), and
    o's (σ_t, τ′)-play is o · (y's play), which does not return to o: V_{σ_t,τ′}(o) = o ⊕ Ξ_t(y).
  - Lemma S (a) (equivalently XW's reason, RESULTS R21 (a): σ̄_t is pointwise optimal for Odd in G_{σ_t}) gives
    Ξ_t(o) ⊴ o ⊕ Ξ_t(y). Both have cycle node c_θ, and o ∉ P(Ξ_t y) (y's play avoids o), so by (M1′) M_t(o) ≤ wt(o) + M_t(y). □
- (b) o lies on its honest cycle, whose top is the cycle node λ_t(o) = c_θ. P(θ_t) consists of the vertices of o's honest path to c_θ
  of rank > rank(c_θ); they all lie on that cycle, so there are none. (If o = c_θ, θ = (o, ∅, 0).) The same is RESULTS R34 (a) Fact (F).
  □

## 2. Lemma HAT-FREEZE (PROVED)
Statement. In a phase:
- (a) For every j ≥ 0, every state t > g_j, every z ∈ Û and every simple path p in G_Û from z to c_θ with ≤ j edges:
  M_t(z) ≥ wt(p ∖ {c_θ}).
- (b) For every state t and z ∈ F_t ∩ U: MoptÛ(z) is defined and M_t(z) ≤ MoptÛ(z).
- (c) If |U| ≥ 2: M_t(y) = MoptÛ(y) for every state t > g_{|U|−2} and every y ∈ F_t ∩ U.
θ may change anywhere in the phase; nothing about θ, H1, H2, τ(o) or c_w is assumed.
Proof.
- (a) Induction on j. j = 0: p has no edge, z = c_θ, and M_t(c_θ) = 0 = wt(∅). Step j − 1 → j: write p = z · p′, z ≠ c_θ, p′ a simple
  path of G_Û from x with ≤ j − 1 edges.
  - z Odd: x is z's forced successor, so x = next_t(z), and (A) and the hypothesis at t (t > g_j > g_{j−1}) give
    M_t(z) = wt(z) + M_t(x) ≥ wt(z) + wt(p′ ∖ {c_θ}).
  - z Even: let k := g_j < t. The hypothesis at the state k (k > g_{j−1}; every state if j = 1) gives M_k(x) ≥ wt(p′ ∖ {c_θ}).
    FB-ROUND at k (z ∈ U ∖ {c_θ} Even, x ∈ U) gives M_{k+1}(z) ≥ wt(z) + M_k(x). (M2′) from k+1 to t gives M_t(z) ≥ M_{k+1}(z).
  - The induction never uses o's value or θ: o is not a vertex of G_Û, and an Odd vertex whose forced successor is o has no edge in G_Û.
- (b) If z = c_θ, both sides are 0. Otherwise z's honest play avoids o ((HP)), and up to c_θ it is a simple path in U ((SP)), hence in
  Û. At Even vertices it follows σ_t (an edge into Û), at Odd vertices the forced edge (into Û). So it is a simple path p of G_Û, and
  (A), (A0) along p give M_t(z) = wt(p ∖ {c_θ}) ≤ MoptÛ(z).
- (c) Simple paths in G_Û have ≤ |Û| − 1 = |U| − 2 edges. (a) with j = |U| − 2 and (b). (For |U| = 2, Û = {c_θ} and both sides are 0.) □

## 3. Theorem RHO-TAIL (PROVED)
Statement. In a phase with |U| ≥ 2, at most deg(o) transitions t → t+1 with t > g_{|U|−2} change P(θ). (If |U| = 1, o = c_θ and θ is
constant.)
Proof.
- At an H1 state t > g_{|U|−2}: by Y-FORM (a), M_t(o) = wt(o) + min_{y∈Y_t} M_t(y), and by HAT-FREEZE (c), M_t(y) = MoptÛ(y) for y ∈
  Y_t ⊆ F_t ∩ U. So M_t(o) ∈ {wt(o) + MoptÛ(y) : y ∈ succ(o) ∩ U, MoptÛ(y) defined}, a set of ≤ deg(o) numbers.
- At a ¬H1 state, M_t(o) = 0 (Y-FORM (b)).
- So on the states t > g_{|U|−2}, M(o) takes values in a set of ≤ deg(o) + 1 numbers, and it is non-decreasing ((M2′) at o). It changes
  at ≤ deg(o) transitions, and by (INJ) these are exactly the transitions that change P(θ). □

## 4. Lemma BF-F (PROVED)
Statement. Let k → k+1 be an in-phase S4a transition with H1 ∧ ¬H2 at k and at k+1. For every Even v ∈ U ∩ F_{k+1}, v ≠ c_θ, and every
successor x ∈ U of v: M_{k+1}(v) ≥ wt(v) + M_k(x).
(The proof uses H1 ∧ ¬H2 only at k.)
Proof.
- v ∈ F_k: by SPLIT (RESULTS R39 (a)) R_k ⊆ R_{k+1}, so F_{k+1} ⊆ F_k (o ∈ R̄ at both).
- Case 1: M_k(x) ≤ M_k(σ_k v). Then wt(v) + M_k(x) ≤ wt(v) + M_k(σ_k v) = M_k(v) ≤ M_{k+1}(v), by (A) and (M2′).
- Case 2: M_k(x) > M_k(σ_k v). By (M1′), Ξ_k(x) ▷ Ξ_k(σ_k v), so (v, x) ∈ Iσ_k and x ∈ A_k(v) (SPEC S4a). Let σ″ := σ_k with v ↦ x;
  it is a strategy of S4a's arena H_k. σ_{k+1} is Even's optimum of H_k against τ (SPEC S4a), so (F1) (RESULTS R17 (a)) gives
  W_{k+1} ⊵ W_{σ″} pointwise, where W_{σ″} is the valuation of the (σ″, τ)-play. By G (a) (RESULTS R19 (a)), W_{k+1}(v) = Ξ_{k+1}(v),
  which has cycle node c_θ (v ∈ U ∩ F_{k+1}). Three sub-cases:
  - x ∈ R̄_k. ¬H2 at k: o lies on its W-cycle C_W, every vertex of which reaches o, so C_W ⊆ R̄_k. x's (σ_k, τ)-play is π_x followed by
    C_W; it lies in R̄_k and avoids v ∈ F_k, so it is also x's (σ″, τ)-play. So W_{σ″}(v) has cycle node c_w (the top of C_W). By
    (HP), c_θ ∈ F_k, so c_θ ≠ c_w, and XW at o (θ_k ⊴ w_k, RESULTS R21 (a)) with distinct cycle nodes gives
    reward(c_θ) < reward(c_w). So W_{σ″}(v) ▷ W_{k+1}(v), against (F1). Impossible.
  - x ∈ F_k, and x's (σ_k, τ)-play passes v. Write it q · v · (v's play), with v ∉ q. It avoids o, so it is x's honest play ((HP)),
    and (A), (A0) along q · v give M_k(x) = wt(q) + wt(v) + M_k(σ_k v). So wt(q ∪ {v}) > 0. Under σ″, v's play is v → x → q → v: the
    cycle C := q ∪ {v}, which avoids o.
    - Let A := {u ∈ C : rank(u) > rank(c_θ)}. wt(C) = wt(A) > 0, so A ≠ ∅ and its vertex u of largest rank is even (it dominates the
      signed sum). Every vertex of C ∖ A has rank ≤ rank(c_θ) < rank(u), so u is the top of C.
    - u even with rank(u) > rank(c_θ) gives reward(u) > reward(c_θ). So W_{σ″}(v) (cycle node u) ▷ W_{k+1}(v) (cycle node c_θ),
      against (F1). Impossible.
  - x ∈ F_k, and x's (σ_k, τ)-play avoids v. It is also x's (σ″, τ)-play, so W_{σ″}(v) = v ⊕ W_k(x) = v ⊕ Ξ_k(x) (G (a)), with cycle
    node c_θ (x ∈ U), and v ∉ P(Ξ_k x) (P lies on x's play). (F1): Ξ_{k+1}(v) ⊵ v ⊕ Ξ_k(x); by (M1′), M_{k+1}(v) ≥ wt(v) + M_k(x). □
- Remark. BF-F is FB-ROUND's analogue for S4a steps, restricted to vertices that stay in F. A vertex entering R follows W's preference
  (c_w beats c_θ), not the honest weight; this is why the S4a analogue is stated on F only.

## 5. Theorem FREEZE-F (PROVED)
Statement. Let [s, e] be a run of consecutive HN states of one phase, no transition of which is a fallback.
- (a) For t ∈ [s, e], z ∈ F_t ∩ U, and every simple path p in G[F_t ∩ U] from z to c_θ with ≤ t − s edges: M_t(z) ≥ wt(p ∖ {c_θ}).
- (b) For t ≤ t′ in [s + |U| − 2, e] and z ∈ F_{t′} ∩ U: M_{t′}(z) = M_t(z).
- (c) At most max(|U| − 2, 0) + deg(o) − 1 transitions of [s, e] change P(θ).
Proof.
- Every transition of [s, e] is S4a (§0), so F_{t+1} ⊆ F_t (SPLIT); c_θ ∈ F_t for all t ∈ [s, e] ((HP)). So G[F_t ∩ U] is defined, and a
  path of G[F_{t+1} ∩ U] is a path of G[F_t ∩ U].
- (a) Induction on t − s. t = s: p has no edge; M_s(c_θ) = 0. Step t → t+1: p = z · p′ in G[F_{t+1} ∩ U], p′ from x with ≤ t − s edges;
  p′ is a path of G[F_t ∩ U], so M_t(x) ≥ wt(p′ ∖ {c_θ}).
  - z Even: BF-F at t → t+1 gives M_{t+1}(z) ≥ wt(z) + M_t(x).
  - z Odd: x = next_{t+1}(z) (forced), so (A) and (M2′) give M_{t+1}(z) = wt(z) + M_{t+1}(x) ≥ wt(z) + M_t(x).
- (b) A simple path of G[F_t ∩ U] has ≤ |F_t ∩ U| − 1 ≤ |U| − 2 edges (o ∉ F_t). The honest play of z ∈ F_t ∩ U, z ≠ c_θ, up to c_θ, is
  such a path ((HP), (SP); its vertices are in F_t because their plays are suffixes of z's). So, with MoptF_t(z) := the best simple
  path of G[F_t ∩ U] from z to c_θ, (a) and (A), (A0) give M_t = MoptF_t on F_t ∩ U for t ≥ s + |U| − 2. Then for t ≤ t′ and
  z ∈ F_{t′} ∩ U ⊆ F_t ∩ U: M_{t′}(z) = MoptF_{t′}(z) ≤ MoptF_t(z) = M_t(z) ≤ M_{t′}(z) (fewer paths; (M2′)).
- (c) Transitions t → t+1 with t < s + |U| − 2: at most max(|U| − 2, 0). For the states t ≥ t* := s + max(|U| − 2, 0): H1 holds, so by
  Y-FORM M_t(o) = wt(o) + min_{y∈Y_t} M_t(y); by (b), M_t(y) = M_{t*}(y) for y ∈ Y_t; and Y_t = succ(o) ∩ U ∩ F_t only shrinks. A min of
  fixed numbers over a shrinking non-empty set (σ̄_t(o) ∈ Y_t) takes ≤ |Y_{t*}| ≤ deg(o) values in order, so M(o) changes at ≤ deg(o) − 1
  of these transitions; by (INJ) so does P(θ). □

## 6. Theorem RHO-HN and Corollary HN-POLY (PROVED)
Statement (RHO-HN). For one phase with |U| ≥ 2: ρ_HN ≤ (N_HN + |U| − 2)(|U| + deg(o) − 3) + deg(o).
Proof. Classify the transitions t → t+1 with both ends HN that change P(θ).
- Fallback transitions: none, by F-FLAT (RESULTS R39 (c)): θ_{t+1} = θ_t.
- t > g_{|U|−2}: at most deg(o) (RHO-TAIL).
- The rest are S4a transitions with t < g_{|U|−2} (all S4a HN → HN transitions if the phase has fewer than |U| − 2 fallbacks). Each lies
  in a maximal run [s, e] of consecutive HN states with no fallback transition, with s ≤ t < g_{|U|−2}. Such a run starts at the start of
  an HN stretch, or at g_j + 1 for a fallback g_j with HN at g_j and g_j + 1; in the second case g_j + 1 ≤ t < g_{|U|−2}, so j ≤ |U| − 3.
  Hence there are ≤ N_HN + |U| − 3 such runs. None contains g_{|U|−2} as a transition. Each has ≤ |U| + deg(o) − 3 changes
  (FREEZE-F (c)).
- Sum: ≤ (N_HN + |U| − 3)(|U| + deg(o) − 3) + deg(o), which is at most the stated bound. □
Corollary HN-POLY (PROVED; conditional on P-N5-PFZ-ext BRK-POLY′, in review). For one phase:
- Σ_S (ρ_S + 1) ≤ ρ_HN + N_HN over the HN stretches S (a transition of S has both ends HN in the phase).
- BRK-POLY′ in the weak form (i′): θ_S ≤ ρ_S + (ρ_S + 1)·max(|U| − 2, 0). (Reason: θ-LEN bounds the θ-changes INSIDE each P-epoch;
  the ρ_S transitions that change P(θ) are θ-changes too. This is the form that P-N5-PFZ-ext's proof gives as written; REFEREE's
  GAP PFZ-1 on (i) and its repair (θ_S ≤ (ρ_S + 1)(|U| − 2)) are not needed here.) With it, B_S ≤ θ_S + (ρ_S + 1)(|U|² − 1) ≤
  (ρ_S + 1)(|U|² + |U| − 2) ≤ (ρ_S + 1)(2n² − 1), so (ii)'s final bound holds as stated. Summing: Σ_S θ_S ≤ ρ_HN + (ρ_HN + N_HN)·
  max(|U| − 2, 0) and Σ_S B_S ≤ (ρ_HN + N_HN)(2n² − 1).
- EPOCH (RESULTS R39 (b)): Σ_S X_S ≤ 2(n − 1)(Σ_S B_S + N_HN), Σ_S f_S ≤ K(Σ_S X_S + N_HN) + Σ_S X_S, K = n_E(2n − 1). An in-phase
  fallback from an HN state either lies in a stretch or is its stretch's last transition, so the phase's fallbacks at HN states number
  ≤ Σ_S f_S + N_HN.
- With RHO-HN and |U|, deg(o) ≤ n: all of these are ≤ poly(n, N_HN) (Σ_S B_S = O(n⁴·N_HN), Σ_S X_S = O(n⁵·N_HN),
  fallbacks at HN states O(n⁷·N_HN)).
- For τ(o) = o: N_HN ≤ ⌊T*/2⌋ + 1 with T* ≤ n² + 2n − 1 (RESULTS R39 (f) (c)), so all of these are polynomial in n.
- Not covered: N_HN for τ(o) ≠ o (§7), the non-HN states, and S4a steps that change none of the counted quantities (iterations).

## 7. Not to sign
- N_HN for τ(o) ≠ o. Lane result (L-NEW succ. 19, PROVED, unrefereed, after this packet's statements; docs/new/N5-NHN-box40.md): in a
  phase with τ(o) ≠ o, every HN-stretch end that keeps H1 is a fallback evicting τ(o), with a strict rise of Ξ(τ(o)); after g_{|U|−2}
  that rise is length-only (HAT-FREEZE pins M(τ(o))), so N_HN ≤ ⌈T/2⌉ + 2|U| − 3. NOT part of this packet; offered to the Lead as a
  separate packet. With it, HN-POLY would hold for every τ(o).
- OPEN, unchanged: the non-HN states (SN, OTHER, ¬H1); S4a steps between fallbacks that change none of the counted quantities (this
  packet is not an iteration bound); whether the bounds of §3, §5, §6 are approached.
- W-TIE steps and the block lemmas of docs/new/N5-RW-box39.md: not routed.

## 8. Data (DATA; which hypotheses occur — lesson N-ENT-2)
Scripts in experiments/new/box40 (l-new 04fe8979 and this commit): rhodata.py (every statement's hypothesis and conclusion, with branch
counts), rhoclimb.py (climb into the post-freeze regime), and box39/rho.py (successor 18's checker, re-run). Instances: (L) the 412-file
list = experiments/new/box37/lib37.txt without out/ paths (existing files) + experiments/new/box37/instances/*.pg +
experiments/new/box38/instances/*.pg; 253 of them are 𝒞^1O (one Odd vertex of out-degree > 1, checked per file), 159 skipped and
counted. (C) the box-40 climb outputs experiments/new/box40/out/rhc_*.pg (5 files, sha1 cc459f93…, 77cc31b1…, 2a68bea3…, 25d15aac…,
98ba660a…) and nhc_fbrestart_cex_n12_11.pg (2344518c…). Canonical start (SPEC S3). Failures: 0 of every check on (L) and on (C).
- (L), 990 phases, 106 with HN states:
  - Y-FORM (a): checked at EVERY H1 state of every phase (not only after the freeze): 6,335 checks. Y-FORM (b): 651 ¬H1 states.
  - HAT-FREEZE (a): checked directly against the exact best simple path of G_Û with ≤ j edges, for j ≤ min(|U| − 2, #fallbacks),
    every state after g_j and every z ∈ Û with such a path, in phases with 3 ≤ |U| ≤ 14: 1,127 checks (109 phases with fallbacks
    skipped for |U| > 14).
  - HAT-FREEZE (c), RHO-TAIL: the hypothesis "t > g_{|U|−2}" with |U| ≥ 3 NEVER occurs in (L) (rhoclimb.py survey: the largest value of
    #fallbacks − (|U| − 2) over phases with |U| ≥ 3 and an H1 state is −1). It occurs only with |U| = 2, where Û = {c_θ} and (c) is
    trivial: 29 phases, 22 with an H1 state after the freeze, 38 checks; RHO-TAIL max 0 changes there.
  - BF-F (S4a HN → HN transitions, Even v ∈ U ∩ F_{k+1}, v ≠ c_θ, x ∈ U): 28,394 checks. Case 1: 27,932. Case 2 with x ∈ F_k avoiding v
    (the only possible sub-case): 462. Case 2 with x ∈ R̄_k: 0; with x's play passing v: 0 (both proved impossible).
  - FREEZE-F (a): 91 maximal fallback-free HN runs with > 1 state; direct checks against the best simple path of G[F_t ∩ U] with
    ≤ min(t − s, |U| − 2) edges (|U| ≤ 14): 250. FREEZE-F (b): VACUOUS (0 states satisfy t ≥ s + |U| − 2: no fallback-free HN run is
    longer than |U| − 2 transitions). FREEZE-F (c): max 13 P(θ)-changes in one run (experiments/red/so/instances/epsseg_cex_n48.pg,
    n 48, |U| 48, deg(o) 17; bound 62).
  - RHO-HN: ρ_HN 87 in total over the 106 phases with HN states; max 13 (epsseg_cex_n48.pg, N_HN 1; bound 2,931).
  - box39/rho.py re-run on (L): the same counts as successor 18's §7 (990 phases, BF-F 28,394, 91 runs, max 13, ρ_HN 87).
- (C), climb outputs (rhoclimb.py, score (failures, H1 states past the hat freeze at |U| ≥ 3, #fallbacks − (|U| − 2)); seeds
  experiments/new/box21/instances/oneodd_c16.pg, experiments/red/n5inj/instances/block_bk20.pg, experiments/new/box22/instances/pure_22.pg,
  about 30 CPU-minutes; then RHC_SCORE=bigU for |U| ≥ 4, about 70 CPU-minutes, no improvement past |U| = 3):
  - 5 phases past the hat freeze with |U| = 3 and an H1 state after it; HAT-FREEZE (c) 10 checks against exact MoptÛ, RHO-TAIL max 0
    changes; Y-FORM 25, HAT-FREEZE (a) 22, BF-F 10, FREEZE-F (a) 2 checks.
  - The post-freeze regime at |U| ≥ 4 was NOT reached (best: #fallbacks − (|U| − 2) = −2 for |U| ≥ 4).
- Honest caveats (the referees should count these; lesson N-ENT-2):
  - HAT-FREEZE (c) and RHO-TAIL after the freeze are exercised only at |U| ≤ 3: trivially at |U| = 2 in (L), and on 5 climb phases at
    |U| = 3 in (C). Successor 18 reported 40 HAT-FREEZE (c) / Y-FORM checks after the freeze on its box-39 climb outputs
    (experiments/new/out/box39, gitignored, lost with its container); those files are not available to re-check.
  - FREEZE-F (b) is VACUOUS in data. FREEZE-F (c)'s second term (after s + |U| − 2) is therefore never exercised; the 13 changes above
    all fall in the first term.
  - Random 𝒞^1O games reach no HN fallback state (box 37, box 39 rwclass.py --rand): all evidence is library and climb material.
