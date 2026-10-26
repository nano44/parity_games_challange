# Referee packet P-N5-FRZ: a coarse freeze that survives θ-changes, w-changes and fallbacks, and crossings per fallback-free run (box 34)
L-NEW successor 14 (Opus 5.5, D15/D18). Written 2026-10-25 05:48Z onward by date -u, at the Lead's request (05:40Z). Frozen at this
commit: corrections go in a fixes file, never here.
- Self-contained: definitions, statements, full proofs, the location of every dependency, the data and the scripts that produce it.
- Source text: docs/new/N5-REL-box34.md §1-§5, §7 (box 34 write-up). Where they differ, this packet governs.
- Status: L-NEW successor 14's proofs, unrefereed. All statements are about the candidate N5 on 𝒞^1O (exactly one Odd vertex o with
  out-degree > 1), inside a phase. Labels: PROVED (L-NEW succ. 14), FALSE, DATA, OPEN. Not a running-time bound, not a TARGET.md claim,
  not a step-4 pass. G-N5-TIME stays OPEN.
- Statements to sign: §1 Corollary NL-MF; §2 Fact 0 and Lemma ARENA; §3 Lemma P^c_ℓ and Theorem FREEZE; §4 Corollary RATCHET; §5 Lemma
  BLOCK; §6 Theorem X-RUN; §7 Theorem SUB. §8 is NOT TO SIGN (FBF fails with θ moving; open items). §9: data.

## 0. Objects and dependencies (landed RESULTS only: R15-R30)
- N5, S4a / S4c, gates Iσ_k, gate levels, M_k, valuations x = (c, P, ℓ) with P a set of vertices (P ⊆ vertices more relevant than c),
  u ⊕ x, VJ00's order ⊴ (cycle-node reward, then the most relevant vertex of P Δ P′, then length by the parity of c), lev, COARSE_L,
  (C1)-(C4): as in RESULTS R25 (P-N5-FB §0-§1). Levels: ⊥ < −1 < 0 < 1 < … < ∞. lev(x, y) = ∞ if the cycle nodes differ, else the rank
  of the most relevant vertex of P(x) Δ P(y), else −1 if only lengths differ, else ⊥. COARSE_L(x) = (c, P ∩ V_{>L}) for −1 ≤ L < ∞, where
  V_{>L} = the vertices of rank > L; COARSE_⊥(x) = x. ⊴_L is the induced order on coarse values.
  - (C1) x ⊴ y ⇒ COARSE_L x ⊴_L COARSE_L y.
  - (C2) COARSE_L x = COARSE_L y ⟺ lev(x, y) ≤ L.
  - (C3) ⊴_L is antisymmetric.
  - (C4) COARSE_L(u ⊕ x) is a function of u and COARSE_L(x).
  - (C1s), from (C1) and (C3): COARSE_L x ◁_L COARSE_L y ⇒ x ◁ y.
  - (V2c): if COARSE_L x ⊴_L COARSE_L y, and u lies on neither path (or the cycle nodes differ), then COARSE_L(u ⊕ x) ⊴_L
    COARSE_L(u ⊕ y). Prefixing adds u to both path sets or to neither, and adds 1 to both lengths.
- Elementary facts (proved in P-N5-SN §0, R30): (C5) a ◁ b ⊴ c ⇒ lev(a, b) ≤ lev(a, c); (C6) lev(a, c) ≤ max(lev(a, b), lev(b, c));
  (C7) if π is disjoint from P(x), P(y) and both cycle nodes, then lev(π ⊕ x, π ⊕ y) = lev(x, y), with the same order.
- Ξ_k = honest valuation of σ_k (play value in H_k). W_k = σ_k's valuation in G_τ, the one-player game "Even against τ" (every Odd vertex
  forced; o forced to τ(o)). λ(v) = cycle node of Ξ(v).
- PHASE: a run of transitions with λ_Ξ and τ constant (R27-R30 setting).
  - R_k := {v ≠ o : v's (σ_k, τ)-play reaches o}, R̄_k := R_k ∪ {o}, F_k := V ∖ R̄_k.
  - θ := Ξ(o), w := W(o), c_θ := λ(o) (fixed in the phase), c_w(k) := the cycle node of w_k.
  - H1: o lies on no honest cycle. H2: o lies on no W-cycle (⟺ τ(o) ∈ F). H3: c_θ = c_w. (h) := H1 ∧ H2 ∧ H3.
  - r_k := lev(θ_k, w_k) (< ∞ under H3).
  - SN prefix of a fallback-free run: its states with c_w = c_θ, an initial segment (R30 (c) SN-PREFIX).
- Signed results used, by number:
  - R15 (a): Ξ_k ⊴ Ξ_{k+1} at every transition (fallbacks included).
  - R17 (a): (F1) the optimum of a one-player game dominates every strategy of that game pointwise. R17 (b), (c): Lemma P and Theorem PH,
    whose proof R20 transcribes.
  - R19 (a) Lemma G:
    - off R̄, Ξ = W (no (h) needed);
    - under (h), on R̄: Ξ = π_v ⊕ θ and W = π_v ⊕ w, where π_v is v's route to o, π_v ⊆ R_k;
    - REFEREE's note: the paths of θ and w lie in F ∪ {o}, so no route meets them.
  - R20 (packet P-N5-XA, docs/new/P-N5-XA-box27.md, with fixes docs/new/P-N5-XA-fixes-box28.md):
    - (a) Lemma C;
    - (d) Lemma P^c and Lemma CR, including the case analysis B1 (α)/(β) and B2, the repaired cases XA-3 / XA-4, and N-XA-1 (the
      fallback case is vacuous);
    - (e) Theorem XA;
    - (b) FBL step 1: an in-phase S4c fallback happens only when S4a returned σ_k.
  - R21 (a) XW: Ξ_k ⊴ W_k.
  - R23 (g) WM: inside a phase, W_{k+1} ⊵ W_k at every transition that is not an S4c fallback.
  - R29 (c) Lemma NL.
  - R30 (c) R-STICK and SN-PREFIX, (d) H3H2, (f) ABS-COUNT′.
- VJ00 (BRICS RS-00-48): (V1) prefix equation, x not its own cycle node: Ξ(x) = x ⊕ Ξ(succ x) (and likewise W in G_τ); (P2) at o.
  Both are used as in R17 / R20.

## 1. Corollary NL-MF (PROVED, L-NEW succ. 14)
Statement. Let j → j+1 be an in-phase S4a transition with (h) at j. Let MF_j := the maximal level of a gate (y, z) at j with
z ∈ F_j (MF_j := ⊥ if there is no such gate). If r_j > MF_j, then R_j ⊆ R̄_{j+1} and MF_{j+1} ≤ MF_j.
Proof. Hypothesis (A_j) of R29 Lemma NL holds for L := MF_j by the definition of MF_j, and r_j > L, L < ∞. NL (ii) is the first claim.
NL (iii) is (A_{j+1}) for L, i.e. MF_{j+1} ≤ MF_j. □
Consequence: a vertex leaves R at an (h) S4a step only if some gate into F_j has level ≥ r_j.

## 2. Fact 0 and Lemma ARENA (PROVED, L-NEW succ. 14)
**Fact 0.** At an (h) state k of a phase, every vertex's W-cycle node is λ(v), and λ(v) = c_θ ∈ F_k for v ∈ R̄_k.
Proof.
- v ∈ F_k: W = Ξ (R19 (a)).
- v ∈ R̄_k: v's (σ_k, τ)-play and its H_k-play agree up to o (on 𝒞^1O the two graphs differ only at o). Both then follow o's play, so
  λ(v) = c_θ, and v's W-cycle node is c_w = c_θ by H3.
- c_θ ∈ F_k: by H1, o's honest play does not return to o, so its cycle avoids o. The cycle's vertices have (σ, τ)-plays equal to
  their honest plays, which avoid o (R30 (d), proof of H3H2). □
- So a run of consecutive (h) states of a phase is a λ-phase of G_τ, and an honest cycle node u (λ(u) = u) lies in F_k, with
  W_k(u) = Ξ_k(u) = (u, ∅, 0).
**Lemma ARENA.** Let k → k+1 be an S4a step from an (h) state. The arena {σ_k(y)} ∪ Iσ_k(y) contains every W-improving edge (y, z) of
G_τ except possibly those with y ∈ F_k, z ∈ R̄_k that are not gates (WITHHELD). A withheld edge has lev(W_k(σ_k y), W_k(z)) ≤ r_k.
Proof.
- R → R̄: both frames are π ⊕ (θ or w) with the same π, so they order these edges alike (C7).
- F → F: Ξ = W.
- R → F: W_k(z) ▷ π ⊕ w_k ⊵ π ⊕ θ_k (XW), so the edge is a gate.
- F → R̄, withheld: π_z ⊕ θ_k ⊴ W_k(σ_k y) ◁ π_z ⊕ w_k. By (C5), lev(π_z ⊕ θ_k, W_k σ_k y) ≤ lev(π_z ⊕ θ_k, π_z ⊕ w_k) = r_k (C7). Then
  (C6) gives lev(W_k σ_k y, π_z ⊕ w_k) ≤ r_k. □
- Remark: at θ_k = w_k nothing is withheld and the S4a step is a switch-best step of G_τ (R17).

## 3. Lemma P^c_ℓ and Theorem FREEZE (PROVED, L-NEW succ. 14)
Fix a phase and a level ℓ ∈ {⊥, −1, 0, 1, …} (ℓ < ∞). A WINDOW at ℓ is a run of consecutive states k0, …, k0 + N of the phase, all with
(h) and r_k ≤ ℓ (r = ⊥ counts as ≤ ℓ). Fallback transitions are allowed inside. Write COARSE := COARSE_ℓ, ⪯ := ⊴_ℓ, Ω_k := W_k,
Ω^c_k := COARSE(W_k).
**Step 1 (Lemma C_ℓ, statewise).** At every state k of a window, COARSE(Ξ_k(v)) = COARSE(W_k(v)) for all v.
Proof. On F_k, Ξ = W (R19 (a)). On R̄_k, Ξ_k(v) = π_v ⊕ θ_k and W_k(v) = π_v ⊕ w_k (R19 (a)); π_v is disjoint from both paths and from
the common cycle node (R19 note, Fact 0). So by (C7) lev(Ξ_k v, W_k v) = r_k ≤ ℓ, and (C2) gives the equality. □
- This replaces R20 Lemma C's use of "θ constant on S": R20 used that P(θ) and P(w) agree on V*, the vertices more relevant than u*.
  Here this holds at each state separately, with V* := V_{>ℓ}, because lev(θ_k, w_k) ≤ ℓ.
**Step 2 (monotonicity along a window).** For consecutive window states k, k+1: Ω^c_{k+1} ⪰ Ω^c_k pointwise.
Proof. At an S4a step, WM (R23 (g)) and (C1). At a fallback, Step 1 at k and k+1 and R15 (a) with (C1):
COARSE(W_{k+1}) = COARSE(Ξ_{k+1}) ⪰ COARSE(Ξ_k) = COARSE(W_k). □
- R20 got this from "Lemma C, fallbacks included" (R15 (a) with θ fixed). Here Step 1 at both ends does the same.
**Lemma P^c_ℓ.** Let k0, …, k0 + N be a window at ℓ. For every j ≤ N, every vertex x, and every simple path ρ = (x = p_0, …, p_L = u)
of G_τ with L ≤ j and λ(u) = u: Ω^c_{k0+j}(x) ⪰ COARSE(value(ρ)). Here value(ρ) := (u, {p_i : i < L, p_i more relevant than u}, L)
(R17 §2). Paths may pass o and continue along τ(o).
Proof. This is R20's proof of Lemma P^c, with COARSE := COARSE_ℓ, Lemma C replaced by Step 1, and coarse monotonicity by Step 2.
It is written out so that each use can be checked. Induction on j.
- Base j = 0: ρ = (u). Ω_{k0}(u) = (u, ∅, 0) by Fact 0 (u ∈ F_{k0}).
- Step k := k0 + j → k+1, j < N. Write ρ = x → z → ρ′, with ρ′ simple from z, avoiding x, |ρ′| ≤ j. IH: Ω^c_k(z) ⪰ COARSE(value(ρ′)).
  value(ρ) = x ⊕ value(ρ′). Let s(x) be x's successor under σ_k in G_τ (σ_k(x) for Even x, the unique successor for Odd x).
- Case A: Ω^c_k(z) ⪯ Ω^c_k(s(x)).
  - A1, x ≠ λ(x) (= x's W-cycle node, Fact 0). By (V1) in G_τ, Ω_k(x) = x ⊕ Ω_k(s(x)), and that path avoids x. ρ′ avoids x. So
    (V2c) gives COARSE(value ρ) = COARSE(x ⊕ value ρ′) ⪯ COARSE(x ⊕ Ω_k(s(x))) = Ω^c_k(x), by the IH and Case A. Step 2 gives
    Ω^c_k(x) ⪯ Ω^c_{k+1}(x). (If the cycle nodes of value(ρ′) and Ω_k(s(x)) differ, coarse sees it; (V2c) covers that case too.)
  - A2, x = λ(x). Then Ω_k(x) = (x, ∅, 0), and so is Ω_{k+1}(x) (Fact 0 at k+1).
    - If rew(x) > rew(u): Ω^c_{k+1}(x) ≻ COARSE(value ρ) by cycle node.
    - If rew(x) < rew(u): Ω_k(s(x)) has cycle node x (x is on its own cycle), and value(ρ′) has cycle node u. So
      COARSE(value ρ′) ≻ Ω^c_k(s(x)) ⪰ Ω^c_k(z) ⪰ COARSE(value ρ′), a contradiction.
    - x = u is impossible (ρ is simple with L ≥ 1).
- Case B: Ω^c_k(z) ≻ Ω^c_k(s(x)). Then x is Even: an Odd x ≠ o has one successor, and in G_τ so does o. By Step 1,
  COARSE(Ξ_k z) ≻ COARSE(Ξ_k σ_k x), so Ξ_k(z) ▷ Ξ_k(σ_k x) (C1s): (x, z) ∈ Iσ_k. Also Ω_k(z) ▷ Ω_k(σ_k x) (C1s): the edge is
  W-improving. Let σ̂ := σ_k[x → z], an arena strategy. Let c′ := z's W-cycle node and π := z's σ_k-path to c′.
  - (B-arena) k → k+1 is an S4a step. By (F1) in the arena, Ω_{k+1}(x) ⊵ val_σ̂(x) in G_τ.
    - B1, x ∉ π, x not on c′'s cycle: val_σ̂(x) = x ⊕ Ω_k(z). By (C1), (V2c) (π and ρ′ avoid x) and the IH:
      Ω^c_{k+1}(x) ⪰ COARSE(x ⊕ Ω_k(z)) ⪰ COARSE(x ⊕ value ρ′) = COARSE(value ρ).
    - B1, x ∉ π, x on c′'s cycle. A W-improvement means one of two things.
      - (α) P(π) ≠ ∅ with an even top. Then val_σ̂(x) has a cycle node better than c′ = λ(x), so by (F1) x's W-cycle node at k+1
        differs from λ(x), against Fact 0 at k+1.
      - (β) P(π) = ∅, c′ odd, longer. Then val_σ̂(x) = x ⊕ Ω_k(z), and the first sub-case applies.
      - (P(π) ≠ ∅ with an odd top is not W-improving: Ω_k(z) ◁ Ω_k(s(x)) by that top.)
    - B2, x ∈ π. The σ̂-play from x is the cycle Z = x, z, π[z..x). Put D := P(π[z..x)) ∪ ({x} if x is more relevant than c′).
      - D ≠ ∅ with an odd top: not W-improving.
      - D ≠ ∅ with an even top: val_σ̂(x) has a better cycle node, against Fact 0 at k+1 as in (α).
      - D = ∅: the improvement is in length, so c′ is odd.
        - If x ≠ c′, then top(Z) is less relevant than c′ (D = ∅ and c′ ∉ Z), so rew(top Z) > rew(c′) (c′ odd), and Fact 0 is
          contradicted again.
        - If x = c′: x is its own cycle node, and Ω_k(z) has cycle node x. If rew(x) > rew(u), Ω^c_{k+1}(x) = COARSE(x, ∅, 0) ≻
          COARSE(value ρ). If rew(x) < rew(u), the IH gives Ω^c_k(z) ⪰ COARSE(value ρ′), cycle node x against u: a contradiction.
  - (B-fallback) k → k+1 is an S4c fallback. Then S4a returned σ_k (R20 (b) FBL step 1), so σ_k is an optimum of the arena, and by
    (F1) Ω_k(x) ⊵ val_σ̂(x). In B1 (first sub-case and (β)), val_σ̂(x) = x ⊕ Ω_k(z) ▷ x ⊕ Ω_k(s(x)) = Ω_k(x) by (V2) (VJ00 (5)-(6)),
    a contradiction. In (α) and in B2 with D ≠ ∅ even top, or D = ∅ and x ≠ c′, val_σ̂(x) has a better cycle node than Ω_k(x): a
    contradiction. In B2 with D = ∅ and x = c′, the last sub-case of (B-arena) applies verbatim: it uses only Ω_{k+1}(x) = (x, ∅, 0),
    which holds by Fact 0 at k+1.
  So the fallback case is either contradictory or handled exactly as in R20 (R20's N-XA-1 notes that B-fallback is vacuous for
  ℓ ≥ −1). □
**Theorem FREEZE.** Let k0, …, k0 + n − 1 be a window at ℓ (n states) and F := k0 + n − 1. Let t ≥ F be a state of the same phase, and
suppose some state t2 ≥ t of the phase has H2. Then:
- (a) COARSE_ℓ(Ξ_t(x)) = COARSE_ℓ(Ξ_F(x)) for every x;
- (b) if t has H2: COARSE_ℓ(W_t(x)) = COARSE_ℓ(W_F(x)) = COARSE_ℓ(Ξ_F(x)) for every x.
No hypothesis is made on the states after F: θ, w and R may change, and fallbacks may occur.
Proof.
- Step 3 (upper bound). Let t ≥ F have H2. x's W-play in G_τ under σ_t ends at its W-cycle node c_x. That node is an honest cycle node:
  - if x's play stays in F_t, then c_x = λ(x), because W = Ξ there;
  - otherwise the play reaches o, then τ(o) ∈ F_t (H2), and it stays in F_t. Its cycle lies in F_t, where W = Ξ, so its top c_x
    satisfies λ(c_x) = c_x.
  So W_t(x) = value(ρ_t) for the simple path ρ_t from x to c_x (λ fixed in the phase). ρ_t has ≤ n − 1 edges, so Lemma P^c_ℓ at
  j = n − 1 gives COARSE_ℓ(W_t(x)) ⪯ Ω^c_F(x).
- Step 4 (sandwich). For an H2 state t ≥ F:
  COARSE_ℓ(Ξ_F x) ⪯ COARSE_ℓ(Ξ_t x) [R15 (a), (C1)] ⪯ COARSE_ℓ(W_t x) [XW, (C1)] ⪯ COARSE_ℓ(W_F x) [Step 3] = COARSE_ℓ(Ξ_F x) [Step 1 at F].
  By (C3) all are equal. This is (b), and (a) at H2 states.
- For t without H2 and an H2 state t2 ≥ t: COARSE_ℓ(Ξ_F x) ⪯ COARSE_ℓ(Ξ_t x) ⪯ COARSE_ℓ(Ξ_{t2} x) = COARSE_ℓ(Ξ_F x). □
- Remark (what is new against R20): R20's CR froze coarse values inside a (θ, w)-stretch. Here (i) the window only needs r ≤ ℓ, so
  θ and w may change inside it, and (ii) Steps 3-4 carry the freeze past the window to the end of the phase's H2 states. Steps 3-4 use
  only XW, R15 (a) and paths in G_τ, so they cross fallbacks, w-changes and ¬(h) states.

## 4. Corollary RATCHET (PROVED, L-NEW succ. 14)
Hypothesis: FREEZE's, with F and ℓ. Let T := the H2 states t ≥ F of the phase (in time order).
- (a) At every t ∈ T: COARSE_ℓ(θ_t) = COARSE_ℓ(w_t). Hence c_w = c_θ (H3) and r_t ≤ ℓ; with H1, (h) holds at t.
- (b) Let ℓ ≥ 0. Over the states t ∈ T with H1, COARSE_{ℓ−1}(θ_t) takes at most 2d_o distinct values and changes at most 2d_o − 1
  times. Over all t ∈ T, COARSE_{ℓ−1}(w_t) changes at most once.
- (c) Let ℓ ≥ 0. The states of T with H1 split into at most 2d_o + 1 maximal runs (consecutive in T) on which the pair
  (COARSE_{ℓ−1}θ, COARSE_{ℓ−1}w) is constant. On a run where the two differ, r = ℓ. On a run where they agree, r ≤ ℓ − 1.
Proof.
- (a) FREEZE (a) and (b) at x = o, then (C2). Equal coarse values have equal cycle nodes (ℓ < ∞). With H1, H3H2 (R30 (d)) gives (h).
- (b), θ. Under H1, λ(o) ≠ o and σ̄_t(o)'s honest play avoids o, so θ_t = o ⊕ Ξ_t(σ̄_t(o)) ((P2), (V1)), with σ̄_t(o) ∈ succ(o).
  - By (C4), COARSE_{ℓ−1}(θ_t) = o ⊕_c COARSE_{ℓ−1}(Ξ_t(x)) with x = σ̄_t(o).
  - For each exit x and t ≥ F, COARSE_ℓ(Ξ_t(x)) is constant (FREEZE (a)). COARSE_{ℓ−1} adds the membership of the one vertex of rank
    ℓ, so COARSE_{ℓ−1}(Ξ_t(x)) takes at most 2 values.
  - So COARSE_{ℓ−1}(θ_t) lies in a fixed set of ≤ 2d_o values. θ is non-decreasing (R15 (a)), so by (C1) and (C3) COARSE_{ℓ−1}(θ_t)
    is non-decreasing in t, and it changes at most 2d_o − 1 times.
- (b), w. Under H2, τ(o) ∈ F_t and o's W-play avoids o after o, so w_t = o ⊕ W_t(τ(o)) = o ⊕ Ξ_t(τ(o)) (R19 (a)).
  COARSE_ℓ(Ξ_t(τ o)) is constant and Ξ_t(τ o) is non-decreasing, so COARSE_{ℓ−1}(w_t) takes ≤ 2 values in order.
- (c) The pair changes at most 2d_o times, which gives ≤ 2d_o + 1 runs. The pair differs exactly when lev(θ, w) ≥ ℓ (C2), and with
  (a) that means r = ℓ. □

## 5. Lemma BLOCK (PROVED, L-NEW succ. 14)
Statement. Let ℓ ≥ 0, with FREEZE's hypothesis (F, ℓ). Let I be a set of CONSECUTIVE states of the phase, all t ≥ F, all with (h),
on which (COARSE_{ℓ−1}θ, COARSE_{ℓ−1}w) is constant with the two different (r = ℓ). If v ∈ R_s leaves R at an S4a step s → s+1 with
s, s+1 ∈ I, then v ∉ R_t for every t ∈ I with t > s.
Proof.
- Let u_ℓ be the vertex of rank ℓ. At every t ∈ I, lev(θ_t, w_t) = ℓ, so u_ℓ ∈ P(θ_t) Δ P(w_t), and w_t is the better side there
  (θ_t ◁ w_t by XW). Its membership in P(θ_t) and in P(w_t) is the same at all t ∈ I (the pair is constant). Call θ's membership BAD
  and w's GOOD.
- u_ℓ lies on no route π_v: the paths of θ_t and w_t lie in F_t ∪ {o} (R19 note), o ∉ P(θ) Δ P(w), and π_v ⊆ R_t.
- Put A_v := COARSE_ℓ(W_F(v)) = COARSE_ℓ(Ξ_F(v)). By FREEZE, COARSE_ℓ(Ξ_t v) = COARSE_ℓ(W_t v) = A_v for all t ∈ I.
- For y with COARSE_ℓ(y) = A_v, COARSE_{ℓ−1}(y) is (A_v, BAD) or (A_v, GOOD) (u_ℓ ∈ P(y) or not), with (A_v, BAD) ◁_{ℓ−1} (A_v, GOOD).
- If v ∈ R_t (t ∈ I): Ξ_t(v) = π_v ⊕ θ_t (R19 (a)), so u_ℓ's membership is θ_t's: COARSE_{ℓ−1}(Ξ_t v) = (A_v, BAD).
- At the leave: v ∉ R̄_{s+1}, so Ξ_{s+1}(v) = W_{s+1}(v) (R19 (a)). WM gives W_{s+1}(v) ⊵ W_s(v) = π_v ⊕ w_s, and
  COARSE_{ℓ−1}(π_v ⊕ w_s) = (A_v, GOOD). By (C1), COARSE_{ℓ−1}(Ξ_{s+1} v) ⪰ (A_v, GOOD), hence = (A_v, GOOD).
- A later t ∈ I with v ∈ R_t would give (A_v, BAD) = COARSE_{ℓ−1}(Ξ_t v) ⪰ COARSE_{ℓ−1}(Ξ_{s+1} v) = (A_v, GOOD) (R15 (a), (C1)),
  a contradiction by (C3). □
Consequence: if the transitions inside I are all S4a steps, every vertex crosses R at most twice inside I (at most one entry, then at
most one leave, and none after), so I contains at most 2n crossing transitions, and every exit of o is released inside I at most once.

## 6. Theorem X-RUN (PROVED, L-NEW succ. 14)
Statement. Let Q be a fallback-free run of a phase (consecutive non-fallback transitions), and let P be its SN prefix (R30 (c)). Assume
H1 at every state of P. Then the crossing transitions with both ends in P number at most 13 (d_o + 1) n³. Consequently:
- REL_Q (exits leaving R at transitions of Q) ≤ 13 d_o (d_o + 1) n³. Every leave in Q happens inside P (R30 (c) R-STICK).
- ε_{H1}(Q) ≤ d_o + REL_Q (R30 (f) ABS-COUNT′).
- Q has at most 13 (d_o + 1) n³ + n crossing transitions. At most n − 1 follow P (SN-PREFIX), plus the one leaving P.
Proof.
- All states of P have (h) (H1, H3, and R30 (d)). P is a run of consecutive states without fallbacks. For a level ℓ, let F(ℓ) be the
  least k0 + n − 1 such that k0, …, k0 + n − 1 ∈ P is a window at ℓ (F(ℓ) := ∞ if there is none). F is non-increasing in ℓ.
- Let ℓ_max := max_P r. If P has ≥ n states, F(ℓ_max) = p_0 + n − 1. Before it lie ≤ n − 1 transitions. (If P has < n states, the
  bound is trivial.)
- Levels ℓ ≥ 0, the segment [F(ℓ), F(ℓ − 1)) (states of P in it; F(ℓ−1) may be ∞). By RATCHET (c) at ℓ, it splits into ≤ 2d_o + 1
  runs of constant pair.
  - On a run with r = ℓ, BLOCK gives ≤ 2n crossing transitions inside the run.
  - A run with r ≤ ℓ − 1 is a window at ℓ − 1, so every such run before F(ℓ − 1) has < n states, and the run that creates F(ℓ − 1)
    contributes < n states to the segment. So these runs contribute ≤ (2d_o + 1)(n − 1) transitions.
  - At most 2d_o boundary transitions between runs.
  - In total ≤ (2d_o + 1)(2n + n − 1) + 2d_o ≤ 6(d_o + 1)n crossing transitions per segment. There are ≤ n levels ℓ ≥ 0.
- Level −1, the segment [F(−1), F(⊥)). After F(−1), COARSE_{−1}(Ξ) = (c, P) is frozen. Each Ξ(x) then changes only in its length,
  which takes ≤ n values, in order (R15 (a)).
  - As in RATCHET (b): θ takes ≤ d_o n values and w ≤ n values over the segment, so the pair (θ, w) is constant on ≤ (d_o + 1) n runs.
  - Runs with θ = w (r = ⊥) are windows at ⊥: those before F(⊥) have < n states. Together ≤ (d_o + 1) n (n − 1) transitions, and at
    most n evictions per transition.
  - Runs with θ ≠ w (r = −1): if v leaves at an S4a step s in such a run and re-enters R at a later t, then
    Ξ_t(v) ⊵ Ξ_{s+1}(v) = W_{s+1}(v) ⊵ π_v ⊕ w_s ▷ π_v ⊕ θ_s = Ξ_s(v) (WM, R19 (a), and θ_s ◁ w_s with equal (c, P)).
    That is a strict increase of Ξ(v). Over the segment Ξ(v) takes ≤ n values, so each vertex has ≤ n − 1 such re-entries.
  - Entries of v after leaves in θ = w runs number ≤ the evictions in those runs: ≤ n·(d_o + 1)n(n − 1) in total.
  - So the segment has ≤ (d_o + 1)n(n − 1) + (d_o + 1)n + 2[n + n(n − 1) + n(d_o + 1)n(n − 1)] ≤ 6 (d_o + 1) n³ crossing transitions.
- After F(⊥): FREEZE at ⊥ freezes Ξ and W completely, and by RATCHET (a) θ = w.
  - A non-flat gate (x, z) at an S4a step would give W_{k+1}(x) ▷ W_k(x): case B1 of Lemma P^c, where the cycle cases contradict
    Fact 0. That is impossible.
  - A flat switch (x = λ(x), z in x's region) changes no play into or out of o: x ∈ F, and z ∈ R̄ would move x's W-cycle node to c_w,
    against Fact 0 (if x = c_θ = c_w, o would lie on x's new W-cycle, against H2 at k+1). So it is no crossing.
  - Hence no crossing after F(⊥).
- Sum: (n − 1) + 6(d_o + 1) n² + 6 (d_o + 1) n³ ≤ 13 (d_o + 1) n³. The consequences follow from R-STICK, SN-PREFIX and ABS-COUNT′.
  REL_Q counts exit leaves, ≤ d_o per crossing transition. □
- Per phase (consequence, not a new claim): summing over the f + 1 fallback-free runs, the S4a crossings at SN states of runs with H1
  on their SN prefix number ≤ (f + 1)·13 (d_o + 1) n³. With R28 Corollary OX (f ≤ n_E(2n − 1)(X + 1) + X) this makes f and X
  polynomially equivalent per phase. It bounds neither.

## 7. Theorem SUB (PROVED, L-NEW succ. 14)
Definition. A (w, r)-SUBRUN is a maximal run S of consecutive states of a phase with (h), w and r = lev(θ, w) =: ρ constant (θ may
change). Fallbacks are allowed.
Statement. On a (w, r)-subrun S with ρ ≥ 0, with u* := the vertex of rank ρ and COARSE := COARSE_ρ:
- (i) R20 Lemma C holds on S: COARSE(Ξ_k) = COARSE(W_k) at every state, non-decreasing along S.
- (ii) R20 Lemma CR holds on S: coarse values are constant from k_0 + n − 1 on.
- (iii) R20 Theorem XA holds on S: let x leave R at an S4a step L → L+1 and re-enter R next at E, with L, …, E+1 ∈ S. Then
  COARSE(Ξ_{E+1}(x)) ≻ COARSE(Ξ_L(x)). There are ≤ n(n − 1) such re-entries in S.
For ρ = −1, (i) and (ii) hold (COARSE_{−1} = (c, P)), and a re-entry as in (iii) is a strict increase of Ξ(x).
Proof.
- (i): Step 1 of §3 at each state (ℓ = ρ), and R15 (a).
- (ii): S's first n states form a window at ρ, so FREEZE applies.
- (iii): R20 §6 steps 1-5 verbatim, with θ_{E+1} in step 3. Step 4 needs u* ∈ P(θ_{E+1}) Δ P(w), with w the better side there.
  This holds because lev(θ_{E+1}, w) = ρ = rank u*; and u* lies on no route (R19 note).
- The count is R20's: the intervals (L, E+1] of one vertex are disjoint, each holds a strict coarse increase of x, and by (ii) all
  coarse increases lie in S's first n − 1 transitions, at most one per vertex per transition.
- ρ = −1: R20 §5 remark for (i) and (ii); for (iii), Ξ_{E+1}(x) ⊵ Ξ_{L+1}(x) ⊵ π ⊕ w ▷ π ⊕ θ_L = Ξ_L(x). □

## 8. NOT TO SIGN: refuted forms, data findings, open items
- FALSE (DATA): R20's Lemma FBF ("after a throttled fallback no vertex enters R for the rest of the stretch") does not transfer to
  (w, r)-subruns.
  - FBF's step 2 uses "same path, same θ ⇒ same Ξ".
  - box34/rsubfb.py finds 1,442 entries into R after a subrun's first fallback, over 368 throttled subruns.
  - First instance: experiments/n5-exhaustive/instances/b6_xl2_n32.pg (sha1 909c737192e3…), subrun from state 4, fallback 18, one entry
    after it.
  - What survives is FBF itself on θ-constant stretches: inside a scope run, no vertex enters R after a fallback until θ changes.
    DATA: 1,874 such entries, each preceded by a θ-change; box34/fbenter.py.
- FALSE (DATA): "at most one fallback cluster per level per scope run" (CL1). It fails in 47 scope runs, with up to 9 clusters at one
  level (experiments/new/box28/instances/x48_rt48_final.pg, sha1 cff46249…). The repeated clusters there are drains, with no entry
  between them (N5-REL-box34.md §9).
- OPEN (L1): re-entries after FALLBACK evictions of level < r inside frozen r = ℓ blocks (BLOCK covers S4a leaves only). DATA: up to 95
  in one block at n 56 (b6_xw_n56), up to 4 for one vertex. Equivalent per scope run to the θ-changes after fallbacks (L-SI's open
  "θ per scope run", R29 / P-N5-CLS §7).
- OPEN (L2): interruptions of (h)-runs by ¬(h) states. After a freeze every H1 ∧ H2 state is (h) (RATCHET (a)), so after the first
  freeze only ¬H1 or ¬H2 states can interrupt.
- OPEN: SN states under ¬H1 (329 SN-prefix steps in the library); f per phase; G-N5-TIME.

## 9. Data (DATA, not proof; experiments/new/box34; logs in experiments/new/box34/data/, committed with the box-34 write-up)
- LIB = the 234 files of experiments/new/box34/lib.txt (= box33/lib.txt). Every script asserts exactly one Odd vertex of out-degree > 1.
- relfr.py (NL-MF): data/relfr_lib.txt. 4,084 (h) S4a steps, 1,894 with r > MF, there 0 leaves and 0 MF rises; 46 exit releases, each
  (h) one with a gate into F of level ≥ r with a tail in R.
- snvi.py (ARENA): data/snvi_lib.txt. 469 H1 SN prefixes; 3,186 of 4,247 steps have a withheld edge; the 84 prefixes without one have
  ≤ |U| − 1 W-changing steps.
- freeze.py (FREEZE (a), (b); RATCHET (b) counts; BLOCK on fallback-free intervals): data/freeze_lib.txt. 183 freezes, 3,532 later
  states, 26 intervals, 0 failures. Random 𝒞^1O games give no freezes (n consecutive (h) states are rare), so the data is thin.
- rsub.py, rsubfb.py (SUB (ii), (iii); FBF): data/rsub_lib.txt, data/rsubfb_lib.txt. 794 + 368 throttled subruns, 0 CR failures, 0 XA′
  failures in 123 re-entries; 1,442 entries after fallbacks.
- rerel.py: data/rerel_lib.txt. Maximum 2 releases of one exit per fallback-free run (so_th_n32, 4 cases). Climbs (relclimb.py,
  ≤ 50 min, seed so_th_n32): still 2 per exit, with up to 24 re-releases at n 32.
- fbentry.py, fbclus.py, fbenter.py (§8 items): data/fbentry_lib.txt, data/fbclus_lib.txt, data/fbenter_lib.txt.
