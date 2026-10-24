# Referee packet P-N5-NH: OTHER states inside a joint λ-phase of N5 (box 30)
L-NEW successor 10 (Opus 5.5, D15/D18). Written 2026-10-24 19:32Z onward (date -u), at the Lead's request (19:3xZ).
- Self-contained: definitions, statements, full proofs, and the location of every dependency.
- Source text: docs/new/N5-NH2-box29.md §1-§4 (box 29). Where the two differ, this packet governs.
- Status: L-NEW's proofs, unrefereed. These are lemmas about the candidate N5 on 𝒞^1O. They are not a running-time bound, not a
  TARGET.md claim, and not a step-4 pass. G-N5-TIME stays OPEN.
- Labels per statement: PROVED (L-NEW), READING, CONJECTURE, FALSE, OPEN.
- Statements: F1° (§1), TC (§2), P3′ (§3). The reduction (§4) is READING. Open items and refuted statements: §5.

## 0. Objects and dependencies
- N5, valuations, (V1), (V2), (F1), Ξ, W, θ := Ξ(o), w := W(o), the gate Iσ: as in P-N5-X-box28.md §0 (RESULTS R21).
- A PHASE is a joint λ-phase with τ fixed. R_k is the set of vertices whose (σ_k, τ)-play reaches o, with o ∈ R_k; F_k := V \ R_k.
  - A transition k → k+1 is a CROSSING if R_{k+1} ≠ R_k.
  - A CROSSING-FREE INTERVAL is a maximal run I of consecutive states of a phase with R constant. On I write R, F.
- (h) at k = H1 ∧ H2 ∧ H3 (P-N5-RE §0):
  - H1: the honest play from o does not return to o;
  - H2: the W-play from o does not return to o;
  - H3: Ξ_k(o) and W_k(o) have the same cycle node.
- State types (R21):
  - EQ: Ξ = W;
  - THR: (h) and Ξ ≠ W;
  - OTHER: (h) fails and Ξ ≠ W.
- λ_Ξ, λ_W: the cycle-node maps of Ξ and W. λ_Ξ is constant in a phase. Exits: the successors of o.
- Signed results used:
  - R15 (a) (Ξ non-decreasing) and (d) (≤ 4n(n − 1) consecutive iterations leave Ωσ and Ωτ unchanged).
  - R17: Lemma P, Theorem PH, (F1), any pointwise-optimal arena choice.
  - R18 (c) flat-case analysis; R18 (d) Lemma S (a) (Ξ(o) = min over exits), (c) (S4a returns σ_k iff σ_k is an arena optimum).
  - R19 (a) Lemma G (a) (off R, Ξ = W; no (h)) and (b) (Ξ = π ⊕ θ and W = π ⊕ w on R). The proof of (b) uses only that o's
    continuation in the frame concerned does not return to o.
  - R21 (RESULTS lines 924-973): Lemmas XW, EQ, FBL-N, NF, F1, F2 and Theorem X, with the repairs in
    docs/new/P-N5-X-fixes-box29.md (F1's bound max(0, |F| − 1); NF's EQ line; Lemma TF; step 4 as a re-derivation).
  - R20 (d): Lemma P^c / CR (the coarse freeze) of P-N5-XA §5.

## 1. Lemma F1° (PROVED, L-NEW): F-values on a crossing-free interval, OTHER states included
Statement. On a crossing-free interval I, the transitions at which Ξ changes at some vertex of F number at most max(0, |F| − 1).
Proof. This is R21's Lemma F1 (P-N5-X §5), whose F-intervals exclude OTHER states. Each step is re-checked here at OTHER states.
1. Ξ = W on F at every state (Lemma G (a), no (h)). F is closed under σ_k and contains no vertex with an Odd choice (o ∉ F). Let 𝓕
   be G_τ restricted to F.
2. For x, z ∈ F, (x, z) ∈ Iσ_k iff it is 𝓕-improving at σ_k|F, by step 1 at both endpoints (REFEREE-2's N-X-1: only Lemma G (a) is
   used).
3. S4a steps: there is no crossing, so σ_{k+1} maps F into F. By (F1) in G_τ, σ_{k+1}|F dominates every strategy of 𝓕's arena
   {σ_k(x)} ∪ (𝓕-improving edges); its edges are gate edges by step 2. So σ_{k+1}|F is a pointwise optimum of that arena.
4. S4c steps inside I: Even's, since τ is fixed.
   - Every switched edge from F is flat (FBL-N (ii), no (h)), and it stays in F (no crossing). So the F-values do not change.
   - R-vertices' switches do not affect F, because F-plays avoid R.
   - R17's Lemma P invariant on 𝓕 is a statement about current values, and its step uses only the state it starts from. So it carries
     over with j unchanged.
5. λ on F is λ_Ξ, constant in the phase.
6. R17 Lemma P and Theorem PH on 𝓕 (forced Odd vertices have one successor) give ≤ max(0, |F| − 1) value-changing arena steps. □

## 2. Lemma TC (PROVED, L-NEW): the clauses of (h) on a crossing-free interval
Statement. Let I be a crossing-free interval.
- (i) H1 ⟺ λ_Ξ(o) ∈ F, and H2 ⟺ τ(o) ∈ F. Both are constant on I.
- (ii) If H2 holds on I, then λ_W(o) = λ_Ξ(τ(o)), which is fixed in the phase. So H3 and (h) are constant on I, and either every state
  of I is OTHER or none is.
- (iii) If H1 ∧ ¬H2 holds on I, every state of I is OTHER.
- (iv) If ¬H1 ∧ ¬H2 holds on I, a state of I is EQ iff θ = w, and every transition EQ → OTHER inside I changes w.
Proof.
- (i)
  - Suppose H1 holds. Then e* := σ̄(o) ∈ F: Odd chooses only at o, so if e*'s σ-play reached o, the honest play from o would return
    to o. F is closed, so the honest cycle, and λ_Ξ(o), lies in F.
  - Suppose H1 fails. The honest cycle passes o, and every vertex of it reaches o, so λ_Ξ(o) ∈ R.
  - H2 holds iff o's W-play o → τ(o) → … does not return to o, iff τ(o) ∈ F. (τ(o) = o counts as τ(o) ∈ R.)
  - λ_Ξ(o) is fixed in the phase, τ is fixed, and F is fixed on I. So both clauses are constant on I.
- (ii) Under H2, o is not its own W-cycle node (its W-play does not return), so λ_W(o) = λ_W(τ(o)). Since τ(o) ∈ F and Ξ = W on F,
  λ_W(τ(o)) = λ_Ξ(τ(o)), which is fixed in the phase. Hence H3 ⟺ λ_Ξ(o) = λ_Ξ(τ(o)) is constant, and so is (h), by (i).
  - If (h) fails on I, no state of I is EQ. Ξ(o) = W(o) would need λ_Ξ(o) = λ_W(o) ∈ F, which gives H1 by (i), and also H3, i.e. (h).
  - If (h) holds, no state is OTHER by definition.
- (iii) λ_Ξ(o) ∈ F by (i), while λ_W(o) ∈ R (the W-cycle passes o). So Ξ(o) ≠ W(o) at every state, and (h) fails.
- (iv) Both cycles pass o: C_Ξ = o → e* → π_{e*} → o, and C_W = o → τ(o) → π_{τ(o)} → o.
  - "EQ ⇒ θ = w" is trivial.
  - Conversely, let θ = w. Then c := λ_Ξ(o) = λ_W(o) lies on both cycles, and o's two paths to c (along C_Ξ and along C_W) have the
    same set of vertices above c and the same length.
    - v ∈ F: Ξ(v) = W(v) (Lemma G (a)).
    - v ∈ R with c on v's route π_v (v's σ-path to its first visit of o): both plays coincide until o, so both reach c first. In each
      frame c is v's cycle node (c lies on both cycles), with the same path. So Ξ(v) = W(v).
    - v ∈ R with c not on π_v:
      - In each frame, v's path to c is π_v followed by o's path to c in that frame.
      - That o-path is disjoint from π_v: π_v meets C_Ξ only in a final segment [u..o] with c ∉ [u..o], so o's honest path to c lies
        on C_Ξ \ [u..o]. The same holds for C_W.
      - By (V1) along π_v, Ξ(v) and W(v) differ only through o's two paths to c, which have equal keys. So Ξ(v) = W(v).
  - EQ → OTHER at k → k+1 inside I: θ_k = w_k. If w_{k+1} = w_k, then w_k = θ_k ⊴ θ_{k+1} ⊴ w_{k+1} = w_k (R15 (a), Lemma XW). So
    θ_{k+1} = w_{k+1}, and k+1 is EQ by the converse just proved, a contradiction. □
Consequence. On I the number of maximal OTHER blocks is ≤ 1, except under ¬H1 ∧ ¬H2, where it is ≤ 1 + #(changes of w in I).

## 3. Lemma P3′ (PROVED, L-NEW): two route frames with the honest cycle node higher
Definitions, on a crossing-free interval I.
- The honest frame is in ROUTE FORM if H1 holds or λ_Ξ(o) = o. The W frame is in route form if H2 holds or λ_W(o) = o.
- A (θ, w)-PIECE J ⊆ I is a maximal run on which both frames are in route form and θ, w are constant. c_θ := λ_Ξ(o) and c_w := λ_W(o)
  are then constant on J.
- For v ∈ R, π_v is v's σ-route: the vertices of v's σ-path before its first visit of o.
Facts on a piece J.
- (R1) For v ∈ R: Ξ(v) = π_v ⊕ θ and W(v) = π_v ⊕ w (iterated (V1)).
  - Honest frame under H1: Lemma G (b)'s honest half. Its proof uses only that o's honest continuation does not return to o; that
    continuation lies in F and so avoids π_v.
  - Honest frame with λ_Ξ(o) = o: v's play reaches o along π_v, and o is the cycle node, so v's value is (o, π_v's vertices above o,
    |π_v|) = π_v ⊕ (o, ∅, 0). Here θ = (o, ∅, 0).
  - The W frame is the same, with H2 or λ_W(o) = o.
- (R2) Route orders.
  - Compare ρ ⊕ θ with ρ' ⊕ θ for routes ρ, ρ' ⊆ R \ {o}. They have the same cycle node c_θ, and A_θ(ρ) := ρ's vertices above c_θ
    is disjoint from P(θ): under H1, P(θ) ⊆ {o} ∪ F; if λ_Ξ(o) = o, P(θ) = ∅.
  - So the comparison is decided by the top of A_θ(ρ) Δ A_θ(ρ') (by its parity), and else by |ρ| − |ρ'| (by the parity of c_θ).
  - The same holds for w, with c_w and A_w.
- (R3) Let κ(ρ) := A_θ(ρ), with c_θ strictly more relevant than c_w. If κ(ρ) ≠ κ(ρ'), both orders decide ρ against ρ' the same way.
  - The top t of κ(ρ) Δ κ(ρ') is above c_θ, hence above c_w.
  - Every other vertex of A_w(ρ) Δ A_w(ρ') is in κ(ρ) Δ κ(ρ') or lies between c_w and c_θ, so it is less relevant than t.
  - So t is also the top of A_w(ρ) Δ A_w(ρ'), with the same parity.
- (R4) κ(π_v) is non-decreasing along J in the order of (R2). Ξ(v) is non-decreasing (R15 (a)) and θ is constant, so a change of κ is
  decided by κ and can only go up.
Statement. On a piece J with c_θ strictly more relevant than c_w, the transitions with a Ξ-change at some vertex of R number at most
(n + 1)|R|.
Proof.
1. Coarse freeze: κ(π_v) is constant for all v ∈ R from the |R|-th transition of J on.
   - This is R20 (d) (Lemma P^c and Lemma CR, P-N5-XA §5), run on the route game: the one-player game 𝓡*_w, which is G_τ restricted
     to R with o contracted to a terminal of value w. Its values are W on R by (R1), and S4a's optimum restricted to R is an optimum
     of its arena.
   - The coarse value is κ, and the following replace CR's ingredients:
     - (Cmono) and (Cstrict) by (R3): a κ-strict comparison is strict in both frames, so a κ-strict edge is a gate edge and is
       W-improving;
     - Lemma C (coarse Ξ = coarse W) by (R1)-(R3): on R both frames induce the same κ-order;
     - κ-monotonicity at every transition by (R4). This is all CR uses at S4c steps (REFEREE-2's N-XA-1: the B-fallback case is vacuous).
   - CR's case B2 (x on z's route) uses that W's cycle-node map is constant on J: it is c_w on R, by (R1), and λ_Ξ on F.
   - The squeeze uses x's current route, a simple route of ≤ |R| edges ending at o.
2. After the freeze, κ(π_v) = A_θ(π_v) is constant for every v ∈ R, and so is P(θ). Then Ξ(v) = π_v ⊕ θ changes only through |π_v|
   ∈ [1, n − 1], monotonically by (R4) and R15 (a). So each R-vertex has ≤ n − 2 such changes.
3. Total: ≤ |R| (before the freeze) + (n − 2)|R| + |R| ≤ (n + 1)|R| transitions with a Ξ-change on R. □
Corollaries.
- Under H2 on I, the number of pieces is ≤ max(1, |F|).
  - Under H1, θ = o ⊕ min over exits e ∈ F of Ξ(e) (Lemma TF's argument), and under H2, w = o ⊕ Ξ(τ(o)). Both are F-determined, so
    they change at ≤ max(0, |F| − 1) transitions (F1°).
  - If λ_Ξ(o) = o, then θ = (o, ∅, 0) is constant.
  - The route-form status is constant on I (TC (i); λ_Ξ(o) is fixed in the phase).
- If c_θ = c_w with both frames in route form, the two orders coincide. That is the THR situation, covered by Lemma G (c) and PIECE.
- If c_w is more relevant than c_θ, step 1 holds with κ := the route vertices above c_w, but step 2 fails. The honest order still
  sees the vertices between c_θ and c_w (V_mid); the W order sees only lengths. That is OPEN case U1 (§5).

## 4. The reduction (READING: an assembly of §1-§3 with R21 Theorem X)
Inside one phase, the number of transitions is
    poly(n) · (1 + X + Σ_I (ROI(I) + WC(I))),
summed over the crossing-free intervals I, where:
- X is the number of crossing transitions;
- ROI(I) is the number of transitions in OTHER blocks of I that change values only on R (o included);
- WC(I) is the number of changes of w in I if ¬H1 ∧ ¬H2 holds on I, and 0 otherwise.
Sketch.
- There are ≤ 1 + X crossing-free intervals.
- On each, F-value changes are ≤ max(0, |F| − 1) (F1°), and OTHER blocks are ≤ 1 + WC(I) (TC).
- The parts of I outside OTHER blocks are F-intervals in R21's sense, ≤ 2 + WC(I) of them. Each has ≤ 3n² value-changing
  transitions (Theorem X, steps 2-5, with the fixes).
- Inside OTHER blocks, a value-changing transition changes an F-value (counted above) or is R-only (ROI).
- Value-preserving runs are ≤ 4n(n − 1) (R15 (d)). □
Consequence (READING). With Theorem X, N5 on o-cyclic 𝒞^1O is polynomial if X, ROI and WC are poly(n) per phase. P3′ bounds ROI on
its pieces.

## 5. Open items, conjectures, refuted statements
- OPEN:
  - U1: both frames in route form, c_w more relevant than c_θ (V_mid comparisons at W-ties).
  - U2: honest frame not in route form (¬H1 with λ_Ξ(o) ≠ o).
  - U3: W frame not in route form (¬H2 with λ_W(o) ≠ o).
  - W-CYC: w-changes under ¬H1 ∧ ¬H2.
- CONJECTURE (OB_R): in a crossing-free interval, every OTHER block has ≤ |R| R-only value-changing transitions.
  - DATA: holds on every instance seen. Max ratios: 12/27 (u1_n32, case U1, 3 of them W-flat steps), 16/19 (op20), 7/16 (b5_os_n24),
    10/11 (op16).
- CONJECTURE (OB): every OTHER block has ≤ n − 1 value-changing transitions. DATA: 0 failures (N5-NH2-box29.md §6).
- CONJECTURE (NFB-O): no crossing-free S4c fallback occurs at an OTHER state. DATA: 0 seen.
- FALSE (WF0), "no S4a step leaves W unchanged at every vertex while changing Ξ".
  - Instance: experiments/new/box29/instances/wf0_cex_n16.pg (n 16, sha1 1de2ff5b…, Oink zlk OK, strategies verified). It is in
    case U1.
  - The Lead confirms this is N5 as specified: S4a uses S1's tie-breaks, not "keep current on ties".
- DATA and scripts: N5-NH2-box29.md §6, §8, §9; experiments/new/box29/ (tccheck.py checks every clause of TC: 0 failures;
  p3check.py / rfcheck.py check the freeze of P3′ step 1: 0 failures, but route-form pieces are nearly absent in random runs).
