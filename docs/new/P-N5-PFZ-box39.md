# Referee packet P-N5-PFZ: fallbacks are Bellman-Ford rounds on U = λ^{-1}(c_θ); the path sets freeze after |U| − 1 fallbacks of a θ-run; breaks per HN stretch are polynomial in θ_S (FB-ROUND, P-FREEZE, LEN-TAIL, NO-CROSS-A, RISE′, BRK-POLY) (box 39)
L-NEW successor 18 (Opus 5.5, D15/D18, L37/L40), session_01BhkSHzG2cPM2Rdbj5Y2NJV. Written 2026-10-25 15:2xZ by date -u, at the Lead's
request of 15:11Z (Lead's stamp): "route P-N5-PFZ ... a new frozen file, self-contained in the same style as P-N5-OUT". Frozen at this
commit: corrections go in a fixes file, never here.
- Source: docs/new/N5-RW-box39.md §11 (working doc, l-new a29bd8ac / b1439f57). This packet re-states and re-proves everything it signs.
  Where the packet and the source differ, the packet governs.
- Names. FB-ROUND is the lemma that the Lead's message calls "FBF". It was renamed in the working doc because box 27's "Lemma FBF"
  (P-N5-XA; RESULTS R20 setting) already uses that name. The block lemma "BF" of the working doc is now BF-RW (it clashed with
  P-N5-ENT's BF). BF-RW is not in this packet.
- Labels (D18/L40): PROVED (L-NEW succ. 18, unrefereed), CONJECTURE, OPEN, DATA.
- Scope. Every statement is about the candidate N5 (SPEC S1-S5, docs/new/N5-ssi-global.md) on 𝒞^1O, inside one phase. Nothing here is a
  running-time bound for N5, a TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN. θ-changes are a PARAMETER (θ_S); no bound on
  them is claimed.

## To sign, and what is not to sign
| § | statement | label | uses (P) | uses P-N5-NEB (in review, pinned 314d220) |
| --- | --- | --- | --- | --- |
| §1 | Lemma FB-ROUND (every in-phase Even fallback is a Bellman-Ford round on U) | PROVED | no | no |
| §2 | Theorem P-FREEZE (a), (b) | PROVED | no | no |
| §3 | Corollary LEN-TAIL | PROVED | no | no |
| §4 | Corollary NO-CROSS-A (case A) | PROVED | no | no |
| §5 | Lemma RISE′ (P-N5-NEB's RISE, re-proved here in the form BRK-POLY needs) | PROVED | no | no: re-proved in full |
| §6 | Theorem BRK-POLY (any τ(o), any c_w; case-A refinement) | PROVED | no | no |
- (P) (R18's one-player premise) is used nowhere. The one-player facts used are R17 (a) (V1) and R15; nothing from R18 (d) or R36.
- P-N5-NEB (pinned 314d220, in review) is NOT a premise. Its Lemma RISE is re-proved here as RISE′ (§5) from landed results only.
- §7 is NOT TO SIGN: the P-epoch extension (P-FREEZE′, θ-LEN, BRK-POLY′, lane PROVED in the working doc §12, offered for a later
  packet); W-TIE steps (OPEN); the block lemmas of the working doc (BF-RW, FREEZE-M, FREEZE-X, ROUTE-LEN, W-POT, CW-COUNT); what stays
  OPEN. §8 is data.

## 0. Objects, notation and dependencies
- N5 is SPEC S1-S5 of docs/new/N5-ssi-global.md, as in P-N5-OUT §0 (RESULTS R39).
  - S4a is Even's arena step. S4c is the fallback: if Iσ ≠ ∅, every Even v with an improving edge sets σ(v) to the w with
    (v, w) ∈ Iσ maximising (Ξσ(w), w), ties to the larger index; τ unchanged.
  - Iσ_k := {(y, z) : y Even, z ≠ σ_k(y), Ξ_k(z) ▷ Ξ_k(σ_k y)} (gates).
- Valuations x = (c, P, ℓ), Even's order ⊴ / ◁, rank, p′, reward: VJ00's, as in P-N5-OUT §0. The order compares:
  - first reward(c);
  - then P by the signed weight Σ_{u∈P} sgn(u)·2^rank(u), with sgn(u) = +1 for Ω(u) even and −1 for odd (lexicographic: the top vertex
    of P(x) Δ P(y) decides);
  - then ℓ (shorter is better for Even iff Ω(c) is even).
  P(x) consists of vertices of rank > rank(c), and the cycle node's own value is (c, ∅, 0).
- Honest frame: Ξ_k := Ξ_{σ_k} (against Odd's optimal counterstrategy σ̄_k). λ_k(v) := the cycle node of Ξ_k(v). next_k(v) := σ_k(v)
  for Even v, σ̄_k(v) for Odd v.
- 𝒞^1O: exactly one Odd vertex o has out-degree > 1; every other Odd vertex is forced.
- θ := Ξ(o); c_θ := λ(o). R_k := {v ≠ o : v's (σ_k, τ)-play reaches o}; R̄_k := R_k ∪ {o}; F_k := V ∖ R̄_k; routes π_z (z's
  (σ_k, τ)-path to its first visit of o, o excluded). H1: o lies on no honest cycle. H2: o lies on no W-cycle. HN := H1 ∧ ¬H2.
- PHASE: a maximal run of consecutive states with λ_Ξ and τ constant (RESULTS R38 (a): it is a joint λ-phase). Its transitions have
  both ends in it. A θ-RUN is a maximal run of consecutive states of one phase with θ constant. An HN STRETCH is a maximal run of
  consecutive HN states of one phase. A CROSSING is an in-phase transition with R_{k+1} ≠ R_k; an ENTRY has R_k ⊊ R_{k+1}, an EVICTION
  has R̄_{k+1} ⊊ R̄_k. A BREAK of S is an entry of S preceded in S by an eviction with no entry in between. B_S, θ_S := the numbers of
  breaks and of θ-changes (transitions with θ_{k+1} ≠ θ_k) of S. CASE A: rank(o) > rank(c_θ).
- New notation (this packet).
  - U := λ^{-1}(c_θ). It is constant on a phase (λ is), and o, c_θ ∈ U. The TERMINALS are o and c_θ.
  - M_t(z) := Σ_{u∈P(Ξ_t z)} sgn(u)·2^rank(u), the signed weight of the whole path set, for z ∈ U.
  - wt(v) := sgn(v)·2^rank(v) if rank(v) > rank(c_θ), else 0; wt(A) := Σ_{v∈A} wt(v).
  - G_U is the graph on U in which every Even v ∈ U ∖ {c_θ} keeps all its edges into U, every Odd v ∈ U ∖ {o, c_θ} keeps its forced
    edge, and o and c_θ are sinks. For a θ-run Θ: M_Θ(o) := wt(P(θ)) (constant on Θ) and M_Θ(c_θ) := 0. For z ∈ U,
    Mopt_Θ(z) := max{wt(p ∖ {end}) + M_Θ(end) : p a simple path in G_U from z to a terminal}.
  - A U-RISE at t → t+1 is a z ∈ U with Ξ_t(z) ◁ Ξ_{t+1}(z). An R̄-RISE is a z ∈ R̄_t ∩ R̄_{t+1}, z ≠ o, with Ξ_t(z) ◁ Ξ_{t+1}(z).

### Dependencies (statement used / where it lives / status)
| tag | statement used | location | status |
| --- | --- | --- | --- |
| (V1) | if λ(v) ≠ v, the value of v is v ⊕ (the value of next(v)): add v to P iff rank(v) > rank(cycle node), length + 1 | VJ00 BRICS RS-00-48 §4.2; RESULTS R17 (a) | LANDED |
| R15 (a) | Ξ_k ⊴ Ξ_{k+1} pointwise at every transition, fallbacks included | RESULTS R15 (a) | LANDED |
| R15 (d) | σ_{k+1}(v) ∈ {σ_k(v)} ∪ Iσ_k(v) | RESULTS R15 (d) | LANDED |
| KEY | a (λ_Ξ, τ)-phase is a joint λ-phase | RESULTS R38 (a) | LANDED (used only to name the setting) |
| FBL-N (ii), (iii) | at an S4c fallback with τ unchanged: every gate (x, z) with x ∈ F_k has x = λ_W(x) and λ_W(z) = x; under ¬H2 no gate goes from F_k to R_k | RESULTS R21 (c) | LANDED |
| ACT (i) | at a transition with τ unchanged, if R̄ gains a vertex, some switched Even s ∈ F_k with σ_{k+1}(s) ∈ R̄_k enters | RESULTS R23 (b) | LANDED |
| SPLIT | at an in-phase transition with H1 ∧ ¬H2 at k: a non-fallback has R_k ⊆ R_{k+1}; an Even S4c fallback has R̄_{k+1} ⊆ R̄_k | RESULTS R39 (a) | LANDED |
| F-FLAT | at an in-phase Even fallback with H1 ∧ ¬H2 at k, θ_{k+1} = θ_k | RESULTS R39 (c) | LANDED |
- Re-proved here, so that nothing rests on a proof step of a landed entry: the route form at H1 states and SEP-o (§4), the target-o step
  of "no F → R̄ gate at an HN fallback state" (§5), and RISE (§5).
- Item → dependencies:
  | item | depends on |
  | --- | --- |
  | §1 FB-ROUND | (V1), R15 (a), S4c (SPEC) |
  | §2 P-FREEZE | FB-ROUND, (V1), R15 (a), 𝒞^1O |
  | §3 LEN-TAIL | P-FREEZE, R15 (a) |
  | §4 NO-CROSS-A | P-FREEZE, (V1) |
  | §5 RISE′ | R15 (a), (d), ACT (i), SPLIT (a), FBL-N (ii)-(iii), S4c |
  | §6 BRK-POLY | RISE′, P-FREEZE, LEN-TAIL, NO-CROSS-A, SPLIT (b), F-FLAT |

## 1. Lemma FB-ROUND (PROVED, L-NEW succ. 18; 𝒞^1O)
Facts first (used throughout; each from (V1) and R15 (a)).
- (A) Additivity. For every state t and z ∈ U ∖ {c_θ}: next_t(z) ∈ U and M_t(z) = wt(z) + M_t(next_t z).
  Proof: λ_t(z) = c_θ ≠ z, so (V1) gives Ξ_t(z) = z ⊕ Ξ_t(next_t z) with the same cycle node c_θ; hence next_t(z) ∈ U. ⊕ adds z to P iff
  rank(z) > rank(c_θ).
  - (filled in) No double count: if z already lies in P(Ξ_t next_t z), then z lies on the play of next_t(z). So z lies on its own
    play's cycle, whose top is c_θ, and rank(z) < rank(c_θ): wt(z) = 0, and z is not in either P.
- (M1′) For y, z ∈ U at one state t: Ξ_t(y) ⊴ Ξ_t(z) ⇒ M_t(y) ≤ M_t(z). (Same cycle node; the order compares the signed weights next.)
- (M2′) For z ∈ U and every in-phase transition t → t+1: M_{t+1}(z) ≥ M_t(z). (R15 (a), and the same cycle node c_θ at both states.)
Statement. Let k → k+1 be an in-phase Even S4c fallback. Then for every Even v ∈ U ∖ {c_θ} and every successor x ∈ U of v:
M_{k+1}(v) ≥ wt(v) + M_k(x).
Proof.
- Case 1: Ξ_k(x) ⊴ Ξ_k(σ_k v). By (M1′), (A) at k, and (M2′):
  wt(v) + M_k(x) ≤ wt(v) + M_k(σ_k v) = M_k(v) ≤ M_{k+1}(v).
- Case 2: Ξ_k(x) ▷ Ξ_k(σ_k v), so (v, x) ∈ Iσ_k. v has an improving edge, so S4c sets σ_{k+1}(v) = x* with Ξ_k(x*) ⊵ Ξ_k(x).
  - The transition is in the phase, so λ_{k+1}(v) = c_θ ≠ v. (A) at k+1 gives x* ∈ U and M_{k+1}(v) = wt(v) + M_{k+1}(x*).
  - By (M2′) and (M1′): M_{k+1}(x*) ≥ M_k(x*) ≥ M_k(x). □
- Remarks.
  - The proof does not use θ, H1, H2, c_w, τ(o) or 𝒞^1O. It is the observation that S4c switches EVERY improving vertex to its best
    edge, i.e. a Howard (switch-all-to-best) round, and that values never fall (R15 (a)).
  - S4a steps are not rounds. They enter the later proofs only through (M2′).

## 2. Theorem P-FREEZE (PROVED, L-NEW succ. 18; 𝒞^1O)
Statement. Let Θ = [a, b] be a θ-run, and let f_1 < f_2 < … be the transitions of Θ that are Even S4c fallbacks (f_j → f_j + 1, both
ends in Θ).
- (a) For every j ≥ 0, every state t ∈ Θ with t > f_j (t ≥ a when j = 0), every z ∈ U and every simple path p in G_U from z to a
  terminal with ≤ j edges: M_t(z) ≥ wt(p ∖ {end}) + M_Θ(end).
- (b) (UB) M_t(z) ≤ Mopt_Θ(z) for every t ∈ Θ and z ∈ U.
- (c) For every state t ∈ Θ with t > f_{|U|−1}: M_t = Mopt_Θ on U, and P(Ξ_t z) = P(Ξ_{t′} z) for all such t, t′ and all z ∈ U.
  (If |U| = 1, U = {o} = {c_θ} and there is nothing to prove.)
Proof.
- (b) Let p be z's honest play up to its first visit of a terminal. It reaches one: the play ends on the cycle of c_θ, so it visits c_θ.
  - Before o, the honest play is a path of G_U. At Even vertices it follows σ_t; at Odd vertices other than o it follows the forced
    edge (𝒞^1O); its vertices are in U by (A). It is simple: c_θ lies on the cycle, so the play visits c_θ before any repetition.
  - By (A) along p, M_t(z) = wt(p ∖ {end}) + M_t(end). Here M_t(o) = wt(P(θ)) = M_Θ(o) and M_t(c_θ) = 0 (P(c_θ) = ∅). So
    M_t(z) ≤ Mopt_Θ(z).
- (a) By induction on j.
  - j = 0: p has 0 edges, so z is a terminal, and M_t(z) = M_Θ(z) as just noted.
  - j − 1 → j. Write p = z · p′ with z not a terminal, p′ a simple path from x with ≤ j − 1 edges.
    - z Odd: x is its forced successor, x = next_t(z). (A) and the hypothesis at t (t > f_j > f_{j−1}) give
      M_t(z) = wt(z) + M_t(x) ≥ wt(z) + wt(p′ ∖ {end}) + M_Θ(end).
    - z Even: let k := f_j < t. The hypothesis at the state k (k > f_{j−1}, or k ≥ a when j = 1) gives
      M_k(x) ≥ wt(p′ ∖ {end}) + M_Θ(end). FB-ROUND at k gives M_{k+1}(z) ≥ wt(z) + M_k(x). (M2′) from k+1 to t gives M_t(z) ≥ M_{k+1}(z).
- (c) A simple path in G_U has ≤ |U| − 1 edges, so (a) with j = |U| − 1 and (b) give M_t = Mopt_Θ. The signed weight is injective on
  sets of vertices of rank > rank(c_θ) (distinct powers of 2), and P(Ξ_t z) is such a set, so P(Ξ_t z) is determined by M_t(z). □
- Remark (no positive-cycle issue). (a) quantifies over simple paths only, so cycles of positive weight in G_U do not matter.

## 3. Corollary LEN-TAIL (PROVED, L-NEW succ. 18)
Statement. In a θ-run Θ, at most |U|(|U| − 1) transitions t → t+1 with t > f_{|U|−1} carry a U-rise, and every such U-rise is a length
rise (P(Ξ_t z) = P(Ξ_{t+1} z)).
Proof.
- For t > f_{|U|−1}, P is constant on U (P-FREEZE (c)). A U-rise at t → t+1 has the same cycle node and the same P, so it is a length
  rise.
- Put s_θ := +1 if Ω(c_θ) is odd (longer is better for Even), −1 if even, and Ψ_t := Σ_{z∈U} s_θ·ℓ(Ξ_t z).
- R15 (a) makes each term non-decreasing on t > f_{|U|−1}, and a U-rise raises Ψ by ≥ 1.
- ℓ(Ξ_t z) is the length of z's honest play to c_θ, a simple path in U, so it lies in [0, |U| − 1]. So Ψ ranges over an interval of
  length ≤ |U|(|U| − 1). □

## 4. Corollary NO-CROSS-A (PROVED, L-NEW succ. 18; case A)
Statement. In case A (rank(o) > rank(c_θ)), let Θ be a θ-run and t → t+1 a transition of Θ with t > f_{|U|−1} and H1 at t and at t+1.
Then R̄_{t+1} = R̄_t: the transition is not a crossing.
Proof. At an H1 state s, R̄_s = {z ∈ U : o ∈ P(Ξ_s z)}. Then P-FREEZE (c) gives the claim.
- (filled in, route form) Let s be an H1 state and z ∈ R_s. z's honest play agrees with its (σ_s, τ)-play up to o (on 𝒞^1O the two
  graphs differ only at o), so it is π_z followed by o's honest play. Under H1 that play never returns to o. So it never meets π_z
  either: from a vertex of π_z the play runs to o. So no vertex of π_z is a cycle node, (V1) along π_z gives
  Ξ_s(z) = π_z ⊕ θ_s, and λ_s(z) = c_θ, i.e. z ∈ U.
- (filled in, SEP-o) o ∈ P(θ_s): θ_s = o ⊕ Ξ_s(σ̄_s o) by (V1) (o is not a cycle node under H1), and rank(o) > rank(c_θ). Hence
  o ∈ P(Ξ_s z) for every z ∈ R̄_s (P(π_z ⊕ θ_s) ⊇ P(θ_s)). For z ∈ U ∩ F_s, z's honest play avoids o (a play through o would reach o
  along the (σ_s, τ)-graph), and P consists of vertices of the play, so o ∉ P(Ξ_s z). □

## 5. Lemma RISE′ (PROVED, L-NEW succ. 18; re-proof of P-N5-NEB / N5-TAUW §1 RISE from landed results)
Statement. Let S be an HN stretch and a ∈ S a state at which an in-phase Even fallback a → a+1 is taken. Let k > a with k → k+1 an entry
in S, and suppose no transition of [a, k) is an entry. Then either θ changes at some transition t → t+1 with a + 1 ≤ t ≤ k, or some
transition t → t+1 with a ≤ t < k, θ constant on [a, t+1] and t+1 ∈ S, carries an R̄-rise.
Proof.
- Step 0 (no F → R̄ gate at a).
  - FBL-N (iii) (R21 (c)): under ¬H2 there is no gate (x, z) at a with x ∈ F_a, z ∈ R_a.
  - (filled in, target o) If z = o, FBL-N (ii) gives x = λ_W(o). Under ¬H2, λ_W(o) lies on o's W-cycle, which is contained in R̄_a
    (every vertex of it reaches o). So x ∈ R̄_a, a contradiction.
- Step 1 (a gate F → R̄ by state k). By ACT (i) (R23 (b)), the entry k → k+1 has a switched Even s ∈ F_k with σ_{k+1}(s) ∈ R̄_k. By R15
  (d), (s, σ_{k+1}(s)) ∈ Iσ_k: a gate from F_k into R̄_k.
- Let t+1 be the least state in (a, k] with a gate (y, z), y ∈ F_{t+1}, z ∈ R̄_{t+1}. If θ changes at a transition of [a, t], that
  transition is not a → a+1 (F-FLAT, R39 (c)), so it lies in [a+1, t] ⊆ [a+1, k], and we are done. Otherwise θ is constant on [a, t+1].
- Step 2 (R̄ does not grow on [a, t+1]). For s ∈ [a, t] there is no gate F → R̄ at s (Step 0 and the choice of t+1). An entry at s → s+1
  would need one (ACT (i) and R15 (d), as in Step 1). So R̄_{s+1} ⊆ R̄_s, and z ∈ R̄_{t+1} ⊆ R̄_t.
- Step 3. Let q := σ_{t+1}(y). Since y ∈ F_{t+1}, q ∈ F_{t+1} (otherwise y's play would reach o). We show
  (★) Ξ_t(z) ⊴ Ξ_{t+1}(q) ◁ Ξ_{t+1}(z).
  - The second inequality is the gate at t+1.
  - y ∈ F_t.
    - z ≠ σ_t(y), since σ_t(y) ∈ F_t. There is no gate F → R̄ at t, so Ξ_t(z) ⊴ Ξ_t(σ_t y).
    - R15 (d) gives q ∈ {σ_t(y)} ∪ Iσ_t(y), so Ξ_t(σ_t y) ⊴ Ξ_t(q). R15 (a) gives Ξ_t(q) ⊴ Ξ_{t+1}(q).
  - y ∈ R_t. Then y ∈ R_t ∖ R_{t+1}. By SPLIT (a) (R39 (a)), t → t+1 is not a non-fallback, so it is a fallback (in-phase; Even, since
    τ is constant).
    - Again Ξ_t(σ_t y) ⊴ Ξ_t(q) ⊴ Ξ_{t+1}(q).
    - If Ξ_t(z) ⊴ Ξ_t(σ_t y), (★) follows.
    - Otherwise (y, z) ∈ Iσ_t. So y has an improving edge, S4c's choice q maximises Ξ_t over y's improving edges, and
      Ξ_t(q) ⊵ Ξ_t(z). (★) follows.
- So Ξ_t(z) ◁ Ξ_{t+1}(z), with z ∈ R̄_t ∩ R̄_{t+1}; z ≠ o, since Ξ(o) = θ is constant on [t, t+1]. t ∈ [a, k): t + 1 ≤ k. □

## 6. Theorem BRK-POLY (PROVED, L-NEW succ. 18; 𝒞^1O)
Statement. For every HN stretch S of a phase, for any τ(o) and any c_w:
- (i) B_S ≤ θ_S + (θ_S + 1)·(|U| − 1 + |U|(|U| − 1)) ≤ θ_S + (θ_S + 1)(n² − 1);
- (ii) in case A, B_S ≤ θ_S + (θ_S + 1)(|U| − 1).
Proof.
- Every break of S has a WINDOW [a, k]: a → a+1 is the last eviction before its entry k → k+1, so no transition of (a, k) is an entry.
  - By SPLIT (R39 (a)), the eviction a → a+1 is an Even S4c fallback.
  - Windows of distinct breaks are disjoint: between two breaks there is an entry, and a window contains no entry before its last
    transition.
- Apply RISE′ to each break. Kind 1: θ changes at a transition t → t+1 with a + 1 ≤ t ≤ k. Kind 2: θ is constant on [a, t+1] and
  t → t+1 carries an R̄-rise, a ≤ t < k.
  - Kind 1: the windows are disjoint, so distinct breaks use distinct θ-changes. ≤ θ_S.
  - Kind 2: a, …, t+1 lie in one θ-run Θ, and a → a+1 is a fallback transition of Θ, say f_j.
    - Breaks with j ≤ |U| − 1: distinct breaks have distinct evictions, so ≤ |U| − 1 per θ-run.
    - Breaks with j ≥ |U|: then t ≥ a = f_j > f_{|U|−1}. The R̄-rise at t → t+1 is a U-rise (R̄ ⊆ U under H1, §4 route form), so by
      LEN-TAIL it is one of ≤ |U|(|U| − 1) transitions. Distinct breaks give distinct t (disjoint windows).
    - In case A there are no breaks with j ≥ |U|. Their eviction a → a+1 would be a crossing between two H1 states with a > f_{|U|−1},
      against NO-CROSS-A.
  - S meets at most θ_S + 1 θ-runs. Summing gives (i) and (ii); |U| ≤ n. □
- Consequences (PROVED with RESULTS R39 (b) EPOCH):
  - X_S ≤ 2(n − 1)(B_S + 1) and f_S ≤ K(X_S + 1) + X_S. So crossings and fallbacks per HN stretch are O(n³·K·(θ_S + 1)), for every
    τ(o) and every c_w.
  - Compared with R39 (f) NE-COUNT (τ(o) = o, case A: B ≤ θ_S): BRK-POLY (ii) is weaker by the factor |U| − 1 but has no hypothesis on
    τ(o) or c_w. BRK-POLY (i) covers case B and c_w ≠ o, where NO-ENTRY is FALSE (R39 not-signed list: nebc_cex_n14, tauw_A_cex_n24,
    tauw_B_cex_n24).

## 7. Not to sign
- The P-epoch extension (working doc §12; lane PROVED, not in this packet by the Lead's instruction):
  - P-FREEZE′: §2 with "θ-run" replaced by "maximal run with P(θ) constant";
  - θ-LEN: ≤ |U| − 2 θ-changes per P-epoch;
  - BRK-POLY′: B_S ≤ (ρ_S + 1)(2n² − 1), with ρ_S the number of P(θ)-changes.
- W-TIE steps (working doc §4): S4a transitions with W unchanged on R̄ and an R̄-rise. OPEN.
- Block lemmas of the working doc (BF-RW, FREEZE-M, FREEZE-X, ROUTE-LEN, W-POT, CW-COUNT): lane PROVED, not routed.
- OPEN, unchanged:
  - θ_S / θ_ph (θ-changes; after §7's extension, P(θ)-changes);
  - HN stretches per phase for τ(o) ≠ o;
  - OTHER states;
  - S4a steps between fallbacks: P-FREEZE says nothing about S4a-only runs, so it is not an iteration bound.

## 8. Data (DATA; which hypotheses occur — lesson N-ENT-2)
Scripts in experiments/new/box39: pfreeze.py (FB-ROUND, the freeze, crossings/breaks after it; env PFZ_KEY=P for P-epochs), pfzdata.py
(branch counts below), pfzclimb.py (climb against P-FREEZE). Instances: the library experiments/new/box37/lib37.txt without out/
directories (270 𝒞^1O files; 159 non-𝒞^1O files skipped and counted), experiments/new/box37/instances/*.pg,
experiments/new/box38/instances/*.pg, and box-39 climb outputs. Canonical start (SPEC S3). One Odd vertex of out-degree > 1, checked
per file.
- FB-ROUND: checked at every in-phase fallback for every Even v ∈ U ∖ {c_θ} and every successor x ∈ U (pfzdata.py):
  - Case 1: 69,178 instances (27,601 with equality);
  - Case 2: 1,939 instances (1,617 with equality);
  - failures 0.
  - pfreeze.py: 714 θ-runs, 674 fallbacks, failures 0.
- P-FREEZE (a): checked directly against the exact best simple path with ≤ j edges (DFS), for every j ≤ |U| − 1, every state after
  f_j and every z ∈ U, in θ-runs with |U| ≤ 18: 3,865 checks, failures 0 (230 θ-runs with fallbacks skipped for |U| > 18).
- P-FREEZE (c), LEN-TAIL, NO-CROSS-A: the hypothesis "t > f_{|U|−1}" is RARE in data.
  - Only 10 θ-runs reach |U| − 1 fallbacks, all with |U| = 1 (47 transitions after the freeze point). So (c), LEN-TAIL and NO-CROSS-A
    are exercised only trivially by the library.
  - The library's θ-runs end long before |U| − 1 fallbacks. Max fallbacks in one θ-run: 25, at |U| = 48 (njb_reabs65_n48.pg).
  - P-changes after many fallbacks do occur: up to 25 at n = 48, 23 at n = 32 (fb32_inr2_final.pg), 7 at n = 12 (wd12_s1.pg).
    Always ≤ |U| − 1: FAIL_PFZ 0. Post-freeze crossings 0, breaks 0.
  - pfzclimb.py with PFZ_SCORE=excess (pushes a θ-run with |U| ≥ 3 past |U| − 1 fallbacks): results in the fixes file or the working
    doc, not here (the climb is running at the freeze of this packet).
- RISE′ (pfzdata.py, every HN in-phase fallback state a and the first later state with an F → R̄ gate, θ constant): 6 events. The tail y
  is in F_t in 3 and in R_t in 3 (both branches of Step 3 occur); the transition t → t+1 is a fallback in all 6. Failures 0.
- BRK-POLY (pfzdata.py): 36 HN stretches, 15 breaks (max 2 in one stretch, tauw_A_cex_n24.pg). Charging: 10 kind 1 (θ-change), 5 kind 2
  with an early eviction (j ≤ |U| − 1), 0 kind 2 with j ≥ |U|. No eviction that is not a fallback (0).
- Random 𝒞^1O games (rwclass.py --rand, 20,110 games, n 6..16): no HN state with a fallback is reached, as box 37 found. All evidence
  is library and climb material.
