# Referee packet P-N5-NEB: breaks after HN fallbacks are paid by θ-changes or R̄-rises (Lemma RISE, HIGH-RISE), NO-ENTRY-A′ and the case-B low-class bound when o tops its W-cycle (CASE-B-LEN′, LOW-RISE′, Theorem BRK), and the τ(o) = o out-of-SN fallback bound (Corollary OUT-1) (box 38)
L-NEW successor 17 (Opus 5.5, D15/D18), session_01ESR6bpU1r4ZjFsMExZtFpq. Written 2026-10-25 13:2xZ onward by date -u, after the Lead's
decision of 12:54Z (Lead's stamp: "one packet covers both", τ(o) = o and τ(o) ≠ o). Frozen at its commit: corrections go in a fixes file.
- Self-contained: definitions, statements, full proofs, the location and status of every dependency, the data, and the scripts.
- Source texts (working docs, superseded by this packet where they differ): docs/new/N5-NEB-box38.md (sha1 047bfeb5…) and
  docs/new/N5-TAUW-box38.md (sha1 e194ffe4…).
- Labels (D18/L40): PROVED (L-NEW succ. 17, unrefereed), CONJECTURE, FALSE, OPEN, DATA. Scope: the candidate N5, inside a phase, on
  𝒞^1O. Nothing here is a running-time bound for N5, a TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN. θ-changes are a
  PARAMETER (θ_S, θ_ph); no bound on them is claimed.

## To sign, and what is not to sign
| § | statement | label | uses (P) | uses P-N5-OUT (pinned 719ce66, in review) | uses P-N5-SCOPE (signed, landing) |
| --- | --- | --- | --- | --- | --- |
| §1 | Lemma RISE (any τ(o), cases A and B) | PROVED | no | SPLIT (a), F-FLAT | KEY |
| §2 | Lemma HIGH-RISE (case A, any τ(o), any c_w) | PROVED | no | SEP-o (restated in §0) | KEY |
| §3 | Theorem NO-ENTRY-A′ (case A, c_w(a) = o, any τ(o)) | PROVED | no | FBL-N target-o step (restated) | KEY |
| §4 | Lemma CASE-B-LEN′ (case B, c_w(a) = o, any τ(o)) | PROVED | no | none beyond §0 | KEY |
| §5 | Lemma LOW-RISE′ (case B, c_w(a) = o, any τ(o)) | PROVED | no | SPLIT (a) | KEY |
| §6 | Theorem BRK (break count per HN stretch) | PROVED | no | SPLIT, F-FLAT | KEY |
| §7 | Corollary OUT-1 (τ(o) = o, both cases) | PROVED | no | EPOCH (corrected form), NE-COUNT (c)'s stretch count | KEY, FB-INT |
- (P) is used nowhere. The W-arguments use Step (K) (RESULTS R23 (a)), which rests on FBL-N (i) (R21 (c)) and F1 (R17 (a)), all signed
  without (P). P-N5-P1 and P-N5-RL are not used.
- With τ(o) = o, §3 is P-N5-OUT's Theorem NO-ENTRY-A and §4 is P-N5-OUT's CASE-B-LEN (c_w = o always holds there). This packet re-proves
  both in the general form, so it does not depend on those two items of P-N5-OUT.
- §8 is NOT TO SIGN:
  - FALSE: NO-ENTRY-B (nebc_cex_n14), and NO-ENTRY when c_w ≠ o (tauw_A_cex_n24, tauw_B_cex_n24);
  - DEAD ENDS: NO-RR-B, NO-RISE-B, the INV_B propagation route;
  - CONJECTURE BAND;
  - OPEN: the residual core.
- §9 is data.

## 0. Objects, notation and dependencies
- N5 is SPEC S1-S5 of docs/new/N5-ssi-global.md.
  - S4a is Even's arena step and S4b Odd's.
  - S4c is the fallback: if Iσ ≠ ∅, every Even v with an improving edge sets σ(v) to the w with (v, w) ∈ Iσ that maximises (Ξσ(w), w),
    and τ is unchanged.
- Valuations x = (c, P, ℓ) and Even's order ⊴ / ◁ are VJ00's (SPEC S1).
  - rank is the relevance order; p′(u) = 2·rank(u) + (Ω(u) mod 2); reward(c) = p′(c) if Ω(c) is even, −p′(c) if odd.
  - The order compares the cycle-node reward, then P lexicographically by its top differing vertex (in Even's favour on the side where
    it is even), then the length (shorter better if Ω(c) is even, longer if odd).
- lev(x, y): +∞ if the cycle nodes differ; rank(top of P(x) Δ P(y)) if the P differ; −1 if only the lengths differ; −∞ if x = y.
  - (filled in) For a strict chain x ◁ y ◁ w: lev(x, w) = max(lev(x, y), lev(y, w)).
  - Proof. Above the larger level all three agree, and the larger level decides x against w, unless the two levels are equal.
  - They are never equal at a vertex level: x and y would differ in that vertex's membership, and so would y and w. Then y would hold
    both the membership Even prefers (x ◁ y) and the one it does not (y ◁ w). At +∞ the rewards increase strictly, and at −1 the
    lengths are monotone.
- Honest frame: Ξ_k := Ξ_{σ_k} (Even's valuation of σ_k against Odd's optimal counterstrategy σ̄_k); λ_k(v) := the cycle node of Ξ_k(v);
  next_k(v) := σ_k(v) for Even v, σ̄_k(v) for Odd v.
- 𝒞^1O: exactly one Odd vertex o has out-degree > 1, and every other Odd vertex is forced. So τ is τ(o), and the honest graph and the
  (σ_k, τ)-graph differ at most at o.
  - W_k := the valuation of the (σ_k, τ)-play in the one-player game G_τ.
  - θ := Ξ(o), w := W(o); c_θ := λ(o).
- Sets: R_k := {v ≠ o : v's (σ_k, τ)-play reaches o}; R̄_k := R_k ∪ {o}; F_k := V ∖ R̄_k. For z ∈ R̄_k, the ROUTE π_z is the
  (σ_k, τ)-path from z to its first visit of o, with o excluded (π_o = ∅).
- PHASE: a maximal run of states with λ_Ξ and τ constant; by Remark KEY (P-N5-SCOPE §1) a joint λ-phase. "In-phase" means both ends are in
  it. c_θ is a phase constant.
- H1: o lies on no honest cycle. H2: o lies on no W-cycle. HN := H1 ∧ ¬H2.
  - An HN STRETCH S is a maximal run of HN states of one phase. θ_S counts its θ-changes at transitions with both ends in S.
  - At an HN state, C_W := o's W-cycle (it contains o), and c_w := its most relevant vertex. "o TOPS ITS W-CYCLE" means c_w = o; with
    τ(o) = o this always holds (C_W = {o}).
- CASE A: rank(o) > rank(c_θ). CASE B: rank(c_θ) > rank(o). Both are phase constants.
- Crossings:
  - a CROSSING is an in-phase transition with R_{k+1} ≠ R_k;
  - an ENTRY has R_k ⊊ R_{k+1}, an EVICTION has R̄_{k+1} ⊊ R̄_k;
  - a BREAK of S is an entry preceded in S by an eviction with no entry in between; B_S counts the breaks of S.
- Rises:
  - an R̄-RISE at t → t+1 is some z ∈ R̄_t ∩ R̄_{t+1}, z ≠ o, with Ξ_t(z) ◁ Ξ_{t+1}(z);
  - a HIGH RISE has lev(Ξ_t z, Ξ_{t+1} z) ≥ rank(o);
  - the LOW CLASS is C_θ := {(c_θ, P(θ), ℓ) : ℓ ≥ 0}, and a LOW RISE has Ξ_t(z), Ξ_{t+1}(z) ∈ C_θ.
- Equivalences: x ≡_o y iff lev(x, y) < rank(o); x ≡_B y iff lev(x, y) ≤ −1.
  - (T1) if lev(x, y) ≥ s, x′ ≡ x and y′ ≡ y (≡ at threshold s), then lev(x′, y′) = lev(x, y) with the same verdict;
  - (T2) ≡-classes are intervals of ⊴;
  - (T3) z ⊕ · respects ≡ (z ⊕ (c, P, ℓ) = (c, P ∪ ({z} if rank(z) > rank(c)), ℓ + 1)).
  These hold for ≡_o (s = rank(o)) and for ≡_B (s = 0): above the threshold, the same cycle node and P-part give the same top difference
  on the same side.
- Route form (H1). At an H1 state, for z ∈ R̄, z's honest play is π_z followed by o's honest play, which never returns to o. No vertex of
  π_z is its own cycle node, so by (V1) Ξ(z) = π_z ⊕ θ.
- SEP-o (case A, H1). Every z ∈ R̄ has o ∈ P(Ξ z): Ξ(z) = π_z ⊕ θ, θ = o ⊕ Ξ(σ̄ o) with o not a cycle node, and rank(o) > rank(c_θ). Every
  f ∈ F has o ∉ P(Ξ f), since its honest play avoids o. SEP-o does not involve τ(o).
- F-values avoid R̄. For f ∈ F_k, every vertex on f's honest play has a (σ_k, τ)-play avoiding o (a suffix), so it lies in F_k. Hence
  P(Ξ_k f) ⊆ F_k.

### Dependencies (statement used / location / status)
| tag | statement used | location | status |
| --- | --- | --- | --- |
| (V1) | if λ(v) ≠ v, the value of v is v ⊕ (value of its successor on the play) | VJ00 §4.2; RESULTS R17 (a) | LANDED |
| R15 (a), (d) | Ξ_k ⊴ Ξ_{k+1} pointwise at every transition; σ_{k+1}(v) ∈ {σ_k(v)} ∪ Iσ_k(v) | RESULTS R15 | LANDED |
| XW | Ξ_k ⊴ W_k pointwise | RESULTS R21 (a) | LANDED |
| FBL-N | at an S4c fallback with τ unchanged: (i) Even's, σ_k a pointwise arena optimum in G_τ; (ii) a gate (x, z) with x ∈ F_k has x = λ_W(x), λ_W(z) = x; (iii) under ¬H2, no gate from F_k to R_k | RESULTS R21 (c); proof docs/new/P-N5-X-box28.md §3 | LANDED |
| (K) | at an S4c fallback inside a phase, no arena edge (y, z) raises W at y | RESULTS R23 (a) | LANDED |
| ACT (i) | at a transition with τ unchanged, if R̄ gains a vertex, some switched Even s ∈ F_k with σ_{k+1}(s) ∈ R̄_k enters | RESULTS R23 (b) | LANDED |
| KEY | a (λ_Ξ, τ)-phase is a joint λ-phase | P-N5-SCOPE §1 (c3f5ed37, pin 8998ee6) | signed by both referees; landing (R36) |
| FB-INT | a crossing-free run of a phase has ≤ K := n_E(2n − 1) fallbacks | P-N5-SCOPE §4 | signed by both referees; landing (R36) |
| SPLIT | at an in-phase transition from an HN state: (a) an S4a step has R_k ⊆ R_{k+1}; (b) an Even fallback has R̄_{k+1} ⊆ R̄_k | P-N5-OUT §1 (sha1 9f032e61, pin 719ce66) | IN REVIEW |
| F-FLAT | an in-phase Even fallback from an HN state leaves θ unchanged | P-N5-OUT §3 | IN REVIEW |
| EPOCH | per HN stretch: X_S ≤ 2(n − 1)(B_S + 1), f_S ≤ K(X_S + 1) + X_S | P-N5-OUT §2 | IN REVIEW |
| NE-COUNT (c) | in a τ(o) = o phase the HN stretches are the H1-runs: N_HN ≤ ⌊T_ph/2⌋ + 1 ≤ ⌊T*/2⌋ + 1; a fallback from an HN state has both ends in a stretch or is its exit transition (≤ 1 per stretch) | P-N5-OUT §5 (counting part only) | IN REVIEW |
| TOGGLE-COUNT | T_ph ≤ T* := |U|(n + 1) + n − 1 | RESULTS R34 (e) | LANDED |
- One step of FBL-N (iii) is filled in and used below as (iii+). Under ¬H2, there is also no gate from F_k to o.
  - Proof: a gate (x, o) with x ∈ F_k has x = λ_W(o) by (ii).
  - λ_W(o) lies on C_W, and every vertex of C_W reaches o, so x ∈ R̄_k, a contradiction. (P-N5-OUT §1 (b), filled in.)

## 1. Lemma RISE (PROVED, L-NEW succ. 17; 𝒞^1O, any τ(o), cases A and B)
Statement. Let S be an HN stretch, a ∈ S a state at which an in-phase Even fallback a → a+1 is taken, and t+1 ∈ S with θ constant on
[a, t+1]. Suppose no state of [a, t] has a gate (y, z) ∈ Iσ with y ∈ F and z ∈ R̄, and state t+1 has one. Then there is an R̄-rise at
t → t+1.
Proof.
- No entry on [a, t+1]. Switched edges are gates (R15 (d)), and no gate goes F → R̄ at a..t, so ACT (i) gives R̄_{s+1} ⊆ R̄_s for
  a ≤ s ≤ t.
- Let (y, z) be the gate at t+1, with y ∈ F_{t+1}, z ∈ R̄_{t+1} ⊆ R̄_t, and q := σ_{t+1}(y) ∈ F_{t+1}. We show
  (★) Ξ_t(z) ⊴ Ξ_{t+1}(q) ◁ Ξ_{t+1}(z).
  - y ∈ F_t. No gate F → R̄ at t, and z ≠ σ_t(y) (σ_t(y) ∈ F_t), so Ξ_t(z) ⊴ Ξ_t(σ_t y). Then Ξ_t(σ_t y) ⊴ Ξ_t(q) by R15 (d) (q is
    σ_t(y) or a gate target), and Ξ_t(q) ⊴ Ξ_{t+1}(q) by R15 (a).
  - y ∈ R_t. An S4a step evicts nothing (SPLIT (a)), so t → t+1 is a fallback. As above, Ξ_t(σ_t y) ⊴ Ξ_t(q) ⊴ Ξ_{t+1}(q).
    - If Ξ_t(z) ⊴ Ξ_t(σ_t y), (★) follows.
    - Otherwise (y, z) is a gate at t (z ≠ σ_t(y)), so y switches at the fallback. S4c gives Ξ_t(q) ⊵ Ξ_t(z), and (★) follows.
- So Ξ_t(z) ◁ Ξ_{t+1}(z), and z ≠ o because Ξ(o) = θ is constant. □

## 2. Lemma HIGH-RISE (PROVED, L-NEW succ. 17; case A, any τ(o), any c_w)
Statement. In §1, if the phase is in case A, the rise at z satisfies lev(Ξ_t z, Ξ_{t+1} z) ≥ rank(o).
Proof.
- SEP-o at the H1 states t and t+1: o ∈ P(Ξ_t z) (z ∈ R̄_t) and o ∉ P(Ξ_{t+1} q) (q ∈ F_{t+1}). So the first comparison of (★) is
  strict, at a level ≥ rank(o).
- Likewise o ∈ P(Ξ_{t+1} z), so the second comparison is at a level ≥ rank(o).
- By the chain rule of §0, lev(Ξ_t z, Ξ_{t+1} z) is the larger of the two, which is ≥ rank(o). □

## 3. Theorem NO-ENTRY-A′ (PROVED, L-NEW succ. 17; case A, c_w(a) = o, any τ(o))
Setting. A phase in case A. S is an HN stretch of it, a ∈ S a state at which an Even fallback a → a+1 is taken, and o tops its W-cycle
at a. θ is constant on a run of states [a, b] ⊆ S.
Invariant INV(t):
- (i) no gate (y, z) ∈ Iσ_t with y ∈ F_t and z ∈ R̄_t;
- (ii) every gate (v, z) ∈ Iσ_t with v ∈ R_t and z ∈ R̄_t has lev(Ξ_t(σ_t v), Ξ_t(z)) < rank(o).
Statement. INV(t) holds for every t ∈ [a, b]. No transition of [a, b] is an entry, R̄ only shrinks on [a, b], and Ξ_t(z) ≡_o Ξ_a(z)
for z ∈ R̄_t. In particular, no R̄-rise on [a, b] is high.
Proof.
- W at a. w = W(o) = (o, ∅, 0), because o is the cycle node of its own W-play (c_w = o).
  - XW gives θ ⊴ w. c_θ ≠ o (H1), so reward(c_θ) < reward(o). In case A this forces Ω(o) even: an odd o more relevant than c_θ would
    have reward(o) = −p′(o) < reward(c_θ).
  - For r ∈ R̄_a, r's W-play first reaches o after π_r: if π_r meets C_W, it follows C_W to o, and o is C_W's cycle node. No vertex of
    π_r is a cycle node, so W_a(r) = π_r ⊕ (o, ∅, 0) = (o, π_r ∩ V_{>o}, |π_r|).
- BASE (i): FBL-N (iii) with (iii+).
- BASE (ii). Let (v, z) be a gate at a with v ∈ R_a, z ∈ R̄_a, and ℓ := lev(Ξ_a(σ_a v), Ξ_a(z)) ≥ rank(o). σ_a(v) ∈ R̄_a.
  - Both values are π ⊕ θ_a with cycle node c_θ. Routes lie in R, and θ's path set in {o} ∪ F, so
    P(Ξ_a z) Δ P(Ξ_a σ_a v) = D := (π_z Δ π_{σ_a v}) ∩ V_{>c_θ}. Its top u has rank ℓ, and u ≠ o (o is in no route), so rank(u) > rank(o).
  - The W path sets are π ∩ V_{>o}. Their difference contains u, and an element above u would lie above c_θ and in D. So the W
    difference has the same top u on the same side, and W_a(z) ▷ W_a(σ_a v).
  - Case 1: z's route avoids v, and v ∉ C_W. The switch v → z changes neither z's play nor o's W-play. So W at v becomes
    v ⊕ W_a(z) ▷ v ⊕ W_a(σ_a v) = W_a(v), since v is in neither route and v ⊕ preserves the strict order.
  - Case 1′: z's route avoids v, and v ∈ C_W ∖ {o}.
    - Write C_W as o = c_0 → c_1 → … → c_m → o with v = c_i; then π_{σ_a v} = c_{i+1} … c_m, all of rank < rank(o) (c_w = o).
    - If π_z meets C_W, it does so at some c_j with j > i (else it would pass v).
    - After the switch, v's W-play is v → z → π_z → o → c_1 → … → c_i = v, a cycle Z.
    - u ∉ π_{σ_a v} (rank(u) > rank(o)), so u ∈ π_z: u is on z's side, and Ω(u) is even, since the gate is Even-improving and decided
      at u.
    - Top of Z. Vertices of C_W are below o. A vertex of π_z above u would be above c_θ and outside π_{σ_a v}, hence in D, against the
      choice of u. So the top of Z is u.
    - The new W(v) has cycle node u with reward p′(u) > p′(o) = reward(o), and W_a(v) has cycle node o. So W at v rises.
  - Case 2: z's route passes v, π_z = q · v · π_{σ_a v}. Then D = (q ∪ {v}) ∩ V_{>c_θ}, all on z's side, so u is on z's side and even.
    The switched play from v closes the cycle v → z → q → v, whose top is u. The new W(v) has cycle node u with reward > reward(o).
  - In every case the arena edge (v, z) raises W at v at the fallback a, against Step (K). So (ii) holds.
- STEP: INV(t) ⇒ INV(t+1), for t, t+1 ∈ [a, b].
  - No entry: switched edges are gates (R15 (d)), none goes F_t → R̄_t by (i), so ACT (i) gives R̄_{t+1} ⊆ R̄_t.
  - Value claim, Ξ_{t+1}(z) ≡_o Ξ_t(z) for z ∈ R̄_{t+1}, by induction on the route length d of z at t+1.
    - d = 0: Ξ(o) = θ is constant.
    - d ≥ 1: z′ := next_{t+1}(z) ∈ R̄_{t+1}, and Ξ_{t+1}(z) = z ⊕ Ξ_{t+1}(z′) (route form, H1 at t+1).
      - If z is forced or not switched, next_t(z) = z′.
      - If z is switched, then z ∈ R_t, z′ ∈ R̄_t, and (z, z′) was an R → R̄ gate at t, so Ξ_t(z′) ≡_o Ξ_t(σ_t z) by (ii).
      - (T3) and the induction hypothesis give Ξ_{t+1}(z) ≡_o z ⊕ Ξ_t(next_t z) = Ξ_t(z).
  - (i) at t+1. Let y ∈ F_{t+1} be Even, z ∈ R̄_{t+1}, and Ξ_{t+1}(z) ▷ Ξ_{t+1}(σ_{t+1} y).
    - By SEP-o at t+1 the level is ≥ rank(o). By (T1) with Ξ_t(z) ≡_o Ξ_{t+1}(z), Ξ_t(z) ▷ Ξ_{t+1}(σ_{t+1} y) ⊵ Ξ_t(σ_{t+1} y) ⊵
      Ξ_t(σ_t y) (R15 (a), (d)). So z ≠ σ_t(y) and (y, z) ∈ Iσ_t, with z ∈ R̄_t.
    - y ∈ F_t contradicts (i) at t.
    - y ∈ R_t: (y, z) is an R → R̄ gate at t, so Ξ_t(z) ≡_o Ξ_t(σ_t y) by (ii). With Ξ_t(σ_t y) ⊴ Ξ_{t+1}(σ_{t+1} y) ◁ Ξ_t(z), (T2) gives
      Ξ_{t+1}(σ_{t+1} y) ≡_o Ξ_t(z). But o ∉ P(Ξ_{t+1}(σ_{t+1} y)) (an F_{t+1}-value) and o ∈ P(Ξ_t z) (SEP-o): a contradiction.
  - (ii) at t+1. Let (v, z) be an R → R̄ gate at t+1 with lev ≥ rank(o).
    - v ∈ R_{t+1} ⊆ R_t. By the value claim, and (ii) at t if v switched, Ξ_{t+1}(σ_{t+1} v) ≡_o Ξ_t(σ_{t+1} v) ≡_o Ξ_t(σ_t v), and
      Ξ_{t+1}(z) ≡_o Ξ_t(z).
    - By (T1), (v, z) is an R → R̄ gate at t at the same level ≥ rank(o) (z ≠ σ_t v, since the values differ), against (ii) at t. □
- STEP uses only the honest frame, so τ(o) and c_w after a do not matter.

## 4. Lemma CASE-B-LEN′ (PROVED, L-NEW succ. 17; case B, c_w(a) = o, any τ(o))
Statement. In a phase in case B, let a be an HN state at which an Even fallback is taken, and let o top its W-cycle at a. Then every
R → R̄ gate (v, z) at a has lev(Ξ_a(σ_a v), Ξ_a(z)) = −1, and z's route is longer than σ_a(v)'s.
Proof.
- As in §3, w = (o, ∅, 0), reward(o) > reward(c_θ), and W_a(r) = (o, π_r ∩ V_{>o}, |π_r|) on R̄_a. In case B, Ω(c_θ) is odd: an even
  c_θ more relevant than o would have reward(c_θ) = p′(c_θ) > p′(o) ≥ reward(o).
- Suppose D := (π_z Δ π_{σ_a v}) ∩ V_{>c_θ} is non-empty, with top u. Then rank(u) > rank(c_θ) > rank(o).
- The W difference has the same top u on the same side, as in §3. Cases 1, 1′ and 2 of §3 apply verbatim:
  - in Case 1′, π_{σ_a v} ⊆ C_W lies below o, hence below u, so u ∈ π_z and is even;
  - in Case 2, D lies on z's side.
  Each case gives a W-raise at v, against Step (K).
- So D = ∅: the cycle nodes and P coincide, and lev = −1. Since Ω(c_θ) is odd, the gate means the longer value: |π_z| > |π_{σ_a v}|. □

## 5. Lemma LOW-RISE′ (PROVED, L-NEW succ. 17; case B, c_w(a) = o, any τ(o))
Setting as §4, with S the HN stretch of a.
INV_B(t):
- (i) no gate (y, z) ∈ Iσ_t with y ∈ F_t, z ∈ R̄_t;
- (ii_B) every gate (v, z) ∈ Iσ_t with v ∈ R_t, z ∈ R̄_t has lev(Ξ_t(σ_t v), Ξ_t(z)) = −1.
Statement. INV_B(a) holds. Let t+1 ∈ S, with θ constant on [a, t+1] and INV_B(s) for all s ∈ [a, t]. Then:
- (a) no transition of [a, t+1] is an entry, and Ξ_{t+1}(z) ≡_B Ξ_t(z) for z ∈ R̄_{t+1};
- (b) (ii_B) holds at t+1;
- (c) if (i) fails at t+1, there is a LOW rise at some z ∈ R̄_t ∩ R̄_{t+1} at t → t+1.
Proof.
- INV_B(a): (i) is FBL-N (iii) + (iii+); (ii_B) is §4.
- (a), (b): the STEP of §3 with ≡_B, (ii_B), and (T1)-(T3) at threshold 0. It uses only the honest frame.
- (c) By §1, (★) holds for some y, z, q. By (a) and (T2): Ξ_{t+1}(q) ≡_B Ξ_t(z) ≡_B Ξ_{t+1}(z), so P(Ξ_{t+1} z) = P(Ξ_{t+1} q) ⊆ F_{t+1}
  (F-values avoid R̄).
  - P(Ξ_{t+1} z) = (π_z ∩ V_{>c_θ}) ∪ P(θ) with π_z ⊆ R_{t+1}, so π_z ∩ V_{>c_θ} = ∅ and P(Ξ_{t+1} z) = P(θ) = P(Ξ_t z).
  - So both values are in C_θ, and Ξ_t(z) ◁ Ξ_{t+1}(z) by (★). □

## 6. Theorem BRK (PROVED, L-NEW succ. 17; 𝒞^1O, any τ(o))
Statement. Let S be an HN stretch.
- For a break of S, let a be its EVICTION STATE: the state of the first eviction after the previous entry of S (or after S's start).
- B_S^{=} counts the breaks whose eviction state has c_w = o, and B_S^{≠} the others.
Then:
- (a) Case A: every break counted in B_S^{=} has a θ-change at a transition of (a, k], where k → k+1 is its entry.
- (b) Case B: every break counted in B_S^{=} has a θ-change at a transition of (a, k] or a LOW rise at a transition of [a, k) with θ
  unchanged.
- (c) Every break has a θ-change at a transition of (a, k] or an R̄-rise at a transition of [a, k) with θ unchanged; in case A a HIGH one.
- (d) Hence B_S ≤ θ_S + LR_S + RW_S, where:
  - LR_S counts the transitions of S with θ unchanged and a low rise, and LR_S ≤ (n − 2)²(θ_S + 1);
  - RW_S counts the transitions with θ unchanged and an R̄-rise that lie in [a, k) for a break counted in B_S^{≠}.
  - In particular, if o tops its W-cycle at every eviction state of S (always when τ(o) = o), then B_S ≤ θ_S + (n − 2)²(θ_S + 1), and in
    case A, B_S ≤ θ_S.
Proof.
- The eviction a → a+1 is a fallback (SPLIT (b): an S4a step does not evict), and a < k. The entry k → k+1 needs a switched s ∈ F_k with
  σ_{k+1}(s) ∈ R̄_k (ACT (i)), a gate, so a gate F → R̄ exists at k.
- Let j0 be the first θ-change at a transition of [a, k], if any; j0 ≠ a by F-FLAT.
- Let t+1 ∈ (a, k] be the first state after a with a gate F → R̄.
  - If no θ-change occurs at a..t, the run [a, t+1] has θ constant.
    - Case A with c_w(a) = o: §3 excludes such a gate, so this cannot happen; hence j0 ∈ (a, k] exists. This is (a).
    - Case B with c_w(a) = o: §5 (c) gives a low rise at t → t+1, with a ≤ t < k. This is (b).
    - Otherwise §1 gives an R̄-rise at t → t+1, high in case A by §2. This is (c).
  - Else j0 ≤ t, a θ-change in (a, k].
- Disjointness. The next break's eviction comes after this entry, so the intervals [a, k] of distinct breaks are disjoint. Charging each
  break to its θ-change or rise gives (d)'s first inequality.
- LR_S. Fix a maximal θ-constant run of S, on which C_θ is fixed.
  - Ξ only rises (R15 (a)). So a vertex that leaves C_θ upward never returns, and inside C_θ its length moves in one direction.
  - Values in C_θ belong to vertices z ∉ {o, c_θ}, with lengths in [1, n − 1]. So each of the ≤ n − 2 vertices has ≤ n − 2 low rises
    per run, and the run has ≤ (n − 2)² transitions with one.
  - S has ≤ θ_S + 1 such runs. □

## 7. Corollary OUT-1 (PROVED, L-NEW succ. 17; τ(o) = o, cases A and B)
Statement. For a phase with τ(o) = o, let θ_ph be its number of θ-changes, T_ph its number of H1-toggles, N_HN ≤ ⌊T_ph/2⌋ + 1 its number
of HN stretches, D := (n − 2)² + 1 and K := n_E(2n − 1). Let X_HN count the crossings with both ends in an HN stretch, and f_HN the
in-phase fallbacks from HN states (all out-of-SN fallbacks of the phase). Then:
- X_HN ≤ 2(n − 1)·D·(θ_ph + N_HN);
- f_HN ≤ (K + 1)(2(n − 1)·D·(θ_ph + N_HN) + N_HN).
Proof.
- With τ(o) = o, o tops its W-cycle at every state, so §6 (d) gives B_S ≤ D(θ_S + 1) − 1.
- EPOCH: X_S ≤ 2(n − 1)(B_S + 1) ≤ 2(n − 1)·D·(θ_S + 1), and f_S ≤ K(X_S + 1) + X_S.
- A fallback from an HN state has both ends in one stretch, or is the exit transition of its stretch (≤ 1 per stretch; NE-COUNT (c)).
  So f_HN ≤ Σ_S (K + 1)(X_S + 1).
- Σ_S θ_S ≤ θ_ph, and N_HN ≤ ⌊T_ph/2⌋ + 1 (NE-COUNT (c)). Summing gives both bounds. □
- With T_ph ≤ T* ≤ n² + 2n − 1 (R34 (e)), out-of-SN fallbacks and crossings of a τ(o) = o phase are poly(n)·(1 + θ_ph). θ_ph is OPEN.

## 8. NOT TO SIGN
- FALSE: NO-ENTRY-B (τ(o) = o, case B), canonical start.
  - Instance experiments/new/box38/instances/nebc_cex_n14.pg, sha1 399119afb8741f3689081389e70729891937df7b. n 14, o = 7, rank(o) 6 <
    rank(c_θ = 12) 8. n5 9 iterations / 5 fallbacks; Oink zlk OK, strategies verified (Lead re-run 12:54Z).
  - The fallback at 1 evicts 4 and 9 and switches 3 from 7 to 6, a length-only R → R̄ switch: Ξ(3) (12, ∅, 3) → (12, ∅, 4), a low rise.
    At 2 there is a gate 4 → 3 from F; S4a 2 → 3 enters 4, with θ = (12, ∅, 2) constant.
  - Also from a start pair: neb_cex_n11.pg + .state (sha1 232b8951…, 7b79ecd5…).
- FALSE: NO-ENTRY when c_w ≠ o (both cases), canonical start.
  - experiments/new/box38/instances/tauw_A_cex_n24.pg (case A), sha1 e29908d546d62e64903b41aa987351c3b3c68a62. n5 16 iterations /
    3 fallbacks; Oink OK. The first INV failure (a = 4, at 5) follows a high rise of vertex 3 at rank 19 ∈ (rank(o), rank(c_w)) = (17, 21).
  - experiments/new/box38/instances/tauw_B_cex_n24.pg (case B), sha1 c0ad4f0ca6ce9a35d3c89b377e686eef58dc3845. n5 10 iterations /
    4 fallbacks; Oink OK.
  - Exact obstruction: W's threshold is c_w, so an honest R → R̄ gate at a level in the band (rank(o), rank(c_w)) survives Step (K).
    Library: experiments/new/box35/instances/fbrestart_cex_n24.pg state 10 (o = 19, rank 12; C_W = 19 → 9 → 7 → 6; c_w = 7, rank 21):
    fallback gates 13 → 2, 23 → 20 and 6 → 20 at vertex 12 (rank 19).
- Summary of NO-ENTRY: PROVED exactly for case A with c_w = o at the fallback (§3); FALSE in every other class.
- DEAD ENDS (intermediate CONJECTURES of box 38, all killed on nebc_cex_n14):
  - NO-RR-B, "no R → R̄ gate at a case-B τ(o) = o HN fallback state": FALSE at state 1;
  - NO-RISE-B, "no R̄-value rise at such a fallback": FALSE at 1 → 2;
  - "INV_B (i) propagates": FALSE at state 2. Obstruction: §5 (c), a low rise.
  - State-level samples (statesamp.py): 39 / 616 case-B fallback states have such gates, all length-only; 1 / 413 has a real rise
    (norise_state_n8.pg + .state, sha1 c7462ba5…, 612b749c…).
- CONJECTURE BAND (DATA thin: one high rise found): after a c_w ≠ o fallback in case A, R → R̄ gates and R̄-rises have levels below
  rank(c_w). Even if it holds, band rises are not obviously polynomial (the band can hold Θ(n) vertices).
- OPEN: RW_S (rises after c_w ≠ o evictions); θ_S / θ_ph (the residual core); HN stretches per phase for τ(o) ≠ o; OTHER states.

## 9. Data and scripts (DATA, not proof; experiments/new/box38)
- Every script asserts exactly one Odd vertex of out-degree > 1, and skips and counts non-𝒞^1O files.
- Library: experiments/new/box37/lib37.txt (429 paths, 270 in 𝒞^1O) plus rfroz_cex_n16 and the box-38 instances.
- lowrise.py (τ(o) = o): checks §5 (c) at the first INV_B (i) failure, (ii_B), the charging of every break, and the bound.
  data/lowrise_lib.txt: 75 case-A and 32 case-B fallback bases; 7 INV failures, each with a low rise; 17 breaks, all charged; 0 failures.
- inv2.py (any τ(o)): checks §3 INV (i), (ii) when c_w = o in case A; (ii_B) and the low rise (§5) when c_w = o in case B; §2 in case A;
  §1 always.
  - data/inv2_all.txt: 0 failures.
  - Bases by class: 75 + 13 (case A, c_w = o; τ(o) = o / ≠ o); 34 (case B, τ(o) = o); 6 (case A, c_w ≠ o); 27 (case B, c_w ≠ o).
  - Violations: 0 in the proved class; 18 in case A with c_w ≠ o; 60 in case B with c_w ≠ o; 12 in case B with τ(o) = o, all charged.
- fbsplit.py (P-N5-OUT §8): all 107 in-stretch HN fallbacks of the library are crossings.
- Search tools: rrgate.py, taunot.py, statesamp.py, neb_aug.py, neb_run.py, nebclimb.py (MODE = B | TAU | TAUW; "-" for the canonical
  start). Climb logs: experiments/new/out/box38/nebclimb (gitignored).
- Reproduce: `python3 experiments/new/box38/inv2.py $(cat experiments/new/box37/lib37.txt) experiments/new/box38/instances/*.pg`, and
  `python3 experiments/new/n5.py n5 G sol; python3 experiments/new/check_sol2.py G sol` for each instance.
