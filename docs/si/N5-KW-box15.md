# N5 on 𝒞^1O, box 15: a coarse freeze on every stretch, W-ONCE, and kind monotonicity. (K_W), (E) and K are polynomial per stretch, and the per-phase count closes given f
L-SI successor 10 (Opus 5.5; D18, L40), session_01PBqfsNWMhTPn7yNJ8C18HP. Written 2026-10-25 by date -u (stamp in the commit). Lane
note, not a packet. Lead request 19:23Z (Lead's stamp), item (1): K, i.e. (E) and (K_W).
- Labels: PROVED (L-SI 10, UNREFEREED) / LANDED Rnn / IN REVIEW / CONJECTURE / OPEN / DATA / READING.
- D1: treat every statement below as wrong until a referee has checked its proof. A one-lane proof is not a result (CLAUDE.md).
- Scope: N5 (SPEC, docs/new/N5-ssi-global.md) on 𝒞^1O, inside one phase. This is NOT a TARGET.md claim. 𝒞^1O is polynomial by other
  means, and nothing here touches games with two or more Odd choice vertices.
- Summary.
  - Lemma W-ONCE (§2, any game): after an S4a step that leaves Ξ unchanged, the next S4a step leaves W unchanged.
  - Lemma FRZ-U (§3): on EVERY stretch (route form or not), the route vertices above m* := the more relevant of c_θ, c_w freeze after
    |R| − 1 fallback-free transitions.
  - Corollary LEN (§4): after the freeze, the frame whose cycle node is m* changes on R only through lengths.
  - When c_w is more relevant than c_θ and the W frame is not in route form (U3 / U23), three more facts:
    - KIND-MONO (§5): each vertex changes kind at most once;
    - CW-INT (§5): c_w switches ≤ deg(c_w) − 1 times between kind-B moves;
    - CASC-B (§5): R26's kind-B cascade does not need c_w to be static.
  - Theorem RUN (§6): every fallback-free run of a stretch has O(Δ·|R|⁴) transitions with a Ξ-change on R.
    - So (K_W) and (E) are polynomial per stretch (§7). Both are open in RESULTS R26 limit (ii).
    - So is K, which ledger v2 calls the single open count.
  - Corollary PHASE (§8): with Theorem LP (R27 (d)), the transitions per phase are polynomial GIVEN f per phase. f is FB-POLY's bound,
    IN REVIEW (P-N5-FBPOLY).
  - Assembly (§8, READING): N5 on 𝒞^1O makes polynomially many iterations if P-N5-FBPOLY, P-N5-PHI and this note's lemmas are signed.
    G-N5-TIME stays OPEN until then.

## 1. Setting and notation
- 𝒞^1O: o is the only Odd vertex of out-degree > 1. A PHASE is a maximal run of states with λ_Ξ and τ constant (RESULTS R27 setting;
  = joint λ-phase by R38 KEY). Inside a phase every transition is an S4a step or an Even S4c fallback (SPEC S4: τ is constant, and if S4a
  does not move σ the fallback is Even's because Iσ ≠ ∅; FIX 3).
- R = R_k := {v : v's (σ_k, τ_k)-play reaches o}, o ∈ R (R19 / R24 / R26 convention); r := |R|; F := V \ R. π_v := v's (σ, τ)-path
  before its first visit of o (π_o = ∅).
- θ := Ξ(o), w := W(o), c_θ := λ_Ξ(o), c_w := the cycle node of w.
  - H1: o's honest play does not return to o. H2: o's W-play does not return to o, i.e. τ(o) ∈ F.
  - Route form: honest frame if H1 or c_θ = o; W frame if H2 or c_w = o (P-N5-NH §3).
- STRETCH: a maximal run of states of a phase with R, θ, w constant (R26 setting).
- RUN S: a maximal run of consecutive NON-fallback transitions inside a stretch. States k0, …, kT; every transition is an S4a step with the
  same τ, R, θ, w.
- m* := the more relevant of c_θ and c_w (c_θ if equal). For a vertex set ρ, κ(ρ) := ρ ∩ V_{>m*} (vertices of rank > rank m*).
- κ-ORDER on subsets of V_{>m*}: A ⪯ B iff A = B, or the top t of A Δ B lies in B with Ω(t) even or in A with Ω(t) odd. This is the
  path-set order of SPEC S1 (Q1 there). If C is disjoint from A ∪ B, then A ⪯ B ⟺ A ∪ C ⪯ B ∪ C.
- Valuations, lev, COARSE_L, (V1), (V2), (F1), (C1)-(C4): as in R25 / P-N5-LP §0.
- Landed results used:
  - R15 (a) Ξ_{k+1} ⊵ Ξ_k;
  - R15 (d): a switched Even vertex moves to a gate target;
  - R17 (F1): the S4a result is the pointwise optimum of its arena;
  - R19 (a) Lemma G (a): off R, Ξ = W, with no (h) needed;
  - R19 (d) (SG);
  - R22 (a) F1° and (b) TC;
  - R23 (g) WM: W_{k+1} ⊵ W_k at non-fallback in-phase transitions;
  - R24 (b) TB, (c) CASC, (e) WC;
  - R26 (a)-(d) CASC-U2, CASC-U3;
  - R27 (a) Lemma U, (d) Theorem LP, (g) TH, SO;
  - R30 (c) SN-PREFIX;
  - R34 (e), (f).

## 2. Lemma W-ONCE (PROVED, L-SI 10; any game)
Statement. Let k → k+1 → k+2 be two consecutive S4a transitions (no fallback) of one phase, with Ξ_{k+1} = Ξ_k at every vertex. Then
W_{k+2} = W_{k+1} at every vertex.
Proof.
1. Arenas (SPEC S4a): A_j(v) := {σ_j(v)} ∪ {z : Ξ_j(z) ▷ Ξ_j(σ_j v)} for Even v; Odd v keeps τ(v) (τ is the same at k, k+1).
2. A_{k+1}(v) ⊆ A_k(v) for every Even v.
   - σ_{k+1}(v) ∈ A_k(v), so Ξ_k(σ_{k+1} v) ⊵ Ξ_k(σ_k v).
   - If z ∈ A_{k+1}(v) and z ≠ σ_{k+1}(v), then Ξ_k(z) = Ξ_{k+1}(z) ▷ Ξ_{k+1}(σ_{k+1} v) = Ξ_k(σ_{k+1} v) ⊵ Ξ_k(σ_k v). So z ∈ A_k(v).
3. W_{k+1} is the pointwise optimum over the strategies of H_k, and W_{k+2} is the pointwise optimum over those of H_{k+1} ((F1), R17).
   - σ_{k+1} is a strategy of H_{k+1}, so W_{k+2} ⊵ W_{k+1}.
   - H_{k+1}'s strategies are strategies of H_k (step 2), so W_{k+2} = val(σ_{k+2}) ⊴ W_{k+1}. □
Corollary W-ONCE′. In a phase, an S4a transition that changes W follows a fallback, or a Ξ-changing transition, or is the phase's first
transition. By Lemma U (R27 (a)), a Ξ-changing transition is relevant. So the W-changing S4a transitions of a phase number at most
1 + f + #(Ξ-changing transitions).
- Contrast: Lemma NU (R27 (c)) says Ξ is frozen on NU runs. W-ONCE says W is frozen one step later on Ξ-flat runs. So between two
  Ξ-changes, S4a only re-breaks ties (TB).

## 3. Lemma FRZ-U (PROVED, L-SI 10): the κ-freeze holds on every stretch
Fact A (coarse values on R are route functions; PROVED). On a stretch, for v ∈ R:
- (A-Ξ) P(Ξ(v)) ∩ V_{>m*} = κ(π_v) ∪ C_Ξ and λ_Ξ(v) = c_θ, where C_Ξ := P(θ) ∩ V_{>m*} under H1 and C_Ξ := ∅ otherwise. C_Ξ is
  constant on the stretch and disjoint from π_v.
- (A-W) P(W(v)) ∩ V_{>m*} = κ(π_v) ∪ C_W and the W cycle node of v is c_w, where C_W := P(w) ∩ V_{>m*} under H2 and C_W := ∅ otherwise.
Proof.
- H1 (honest route form): Ξ(v) = π_v ⊕ θ (P-N5-NH (R1); R19 (a) Lemma G (b), honest half). P(θ) ⊆ F ∪ {o} is disjoint from π_v, and
  π_v ⊕ θ has path set (π_v ∩ V_{>c_θ}) ∪ P(θ). Intersect with V_{>m*} ⊆ V_{>c_θ}.
- c_θ = o: Ξ(v) = (o, π_v ∩ V_{>o}, |π_v|).
- ¬H1, c_θ ≠ o. o's honest play is a cycle C_Θ through o with top c_θ (θ = (c_θ, ∅, d), R26 R-1). Every Odd vertex but o is forced, so
  v's honest play follows π_v.
  - If c_θ ∈ π_v, it stops there.
  - Otherwise it reaches o and follows C_Θ's segment o → … → c_θ. That segment avoids π_v: if π_v met C_Θ at q ≠ o, it would follow
    C_Θ from q to o, and c_θ ∉ π_v puts q after c_θ on C_Θ.
  - Vertices after c_θ on π_v, and the segment, lie on C_Θ, so they are less relevant than c_θ.
  - Either way P(Ξ(v)) = π_v ∩ V_{>c_θ}, and λ_Ξ(v) = c_θ.
- W frame: H2 gives W(v) = π_v ⊕ w (P-N5-NH (R1), W half), with P(w) ⊆ F ∪ {o}.
- W frame, ¬H2 (C_W = ∅). o lies on its W-cycle C_W = o → A1 → c_w → A2 → o, with top c_w and w = (c_w, ∅, d) (R24 (e) step 1; R26 (c)
  setting).
  - Kind B (c_w ∉ π_v): v's W-play is π_v, o, A1, c_w.
  - Kind A: v's W-play is π_v up to c_w, and the rest of π_v lies on A2.
  - A1, A2 ⊆ C_W are less relevant than c_w. So P(W(v)) = π_v ∩ V_{>c_w} in both kinds. If c_w = o, this is π_v ⊕ (o, ∅, 0).
  - Every R-vertex's W-play ends in C_W, so its W cycle node is c_w.
- m* ⪰ c_θ and m* ⪰ c_w. □
Fact B (agreement; PROVED). For y, z ∈ R at one state of a stretch: if κ(π_y) ≠ κ(π_z), then Ξ(y) ◁ Ξ(z) ⟺ W(y) ◁ W(z) ⟺
κ(π_y) ≺ κ(π_z).
Proof.
- The cycle nodes agree within each frame (Fact A).
- The path sets differ in (π_y Δ π_z) ∩ V_{>c} for the frame's cycle node c: the constants C_Ξ and C_W are common and disjoint.
- Its top is the top t of κ(π_y) Δ κ(π_z), which lies above m* ⪰ c. Every other differing vertex is in the κ-difference or ranked at
  most m*, so it is below t.
- So both frames decide by t's membership and parity. That is the κ-order. □
Lemma FRZ-U. Let S be a run (states k0, …, kT) of a stretch, and t ≥ k0 + r − 1 a state of S. Then κ(π_v^t) = κ(π_v^{k0+r−1}) for every
v ∈ R.
Proof. Write κ_k(x) := κ(π_x^k). Claim P^c: for k = k0 + j ∈ S, every x ∈ R and every simple path ρ = (x = ρ_0, …, ρ_L = o) of G_τ
with all vertices in R, no inner vertex equal to o, and L ≤ j: κ_k(x) ⪰ κ(ρ) := κ({ρ_0, …, ρ_{L−1}}).
(This is R20 (d) Lemma P^c in the route game with terminal o, transcribed. The transcription replaces Lemma C by Fact B and argues the
cycle cases from "the W cycle node of every R-vertex is c_w, and w is constant".)
- Monotonicity used in every case: κ_k(x) ⪯ κ_{k+1}(x) for x ∈ R. By WM (R23 (g)) W_{k+1}(x) ⊵ W_k(x). Both have cycle node c_w, so (C1)
  and (A-W) give κ_k(x) ∪ C_W ⪯ κ_{k+1}(x) ∪ C_W.
- Base j = 0: only x = o, with ρ = (o) and κ(ρ) = ∅ = κ_k(o).
- Step k → k+1 (k = k0 + j). If x = o, the claim is trivial. Otherwise ρ = x → z → ρ′, with z ∈ R, ρ′ a simple path from z avoiding x,
  |ρ′| ≤ j. Induction hypothesis: κ_k(z) ⪰ κ(ρ′). Write a := σ_k(x) ∈ R for Even x, and a := x's unique successor = z for Odd x ≠ o.
  - Case A: κ_k(z) ⪯ κ_k(a).
    - κ(ρ) = ({x} ∩ V_{>m*}) ∪ κ(ρ′) ⪯ ({x} ∩ V_{>m*}) ∪ κ_k(a) = κ_k(x) ⪯ κ_{k+1}(x).
    - Adding x is order-preserving, since x ∉ ρ′ and x ∉ π_a (π_x = x·π_a is simple).
  - Case B: κ_k(z) ≻ κ_k(a). Then x is Even.
    - By Fact B, Ξ_k(z) ▷ Ξ_k(a) and W_k(z) ▷ W_k(a). So (x, z) ∈ Iσ_k, and σ̂ := σ_k[x ↦ z] is a strategy of the arena H_k.
    - By (F1) (R17), W_{k+1}(x) ⊵ val_σ̂(x), where val_σ̂ is the play value of (σ̂, τ).
    - B1: x ∉ π_z^k and x ∉ C_W (or H2). z's (σ_k, τ)-play does not pass x: it is π_z, then o and o's W-continuation, which lies in C_W
      (¬H2) or in F (H2). So val_σ̂(x) = x ⊕ W_k(z) by (V1).
      - Taking COARSE_{m*} ((C1), (C4), (A-W)): κ_{k+1}(x) ⪰ ({x} ∩ V_{>m*}) ∪ κ_k(z) ⪰ ({x} ∩ V_{>m*}) ∪ κ(ρ′) = κ(ρ).
      - x ∉ π_z and x ∉ ρ′. x ∈ R_{k+1} (R is constant on S), so κ_{k+1}(x) is read from (A-W).
    - B2: x ∈ π_z^k. The σ̂-play from x is a cycle Z = x, z, …, (back to x) inside R, avoiding o.
      - π_z = (z … x)·π_x = (z … x)·x·π_a. So κ(π_z) = κ(Z) ∪ κ(π_a), disjoint, and κ_k(z) ≻ κ_k(a) says κ(Z) ≠ ∅ with even top t.
      - top(Z) = t, since t ∈ V_{>m*} and every vertex of Z above m* is in κ(Z).
      - reward(t) > reward(c_w): t is even and ranked above c_w.
      - So val_σ̂(x) has a cycle node better than c_w. By (F1), W_{k+1}(x)'s cycle node has reward ≥ reward(t) > reward(c_w).
      - But x ∈ R_{k+1}, whose W cycle node is c_w (Fact A; w is constant). Contradiction: B2 does not occur.
    - B3: ¬H2, x ∈ C_W, x ∉ π_z^k (x ≠ o, since x is Even).
      - x ∈ C_W gives π_x ⊆ C_W, so κ_k(a) = ∅ and κ(π_z) ≻ ∅ has an even top t above m*.
      - The σ̂-play from o follows C_W (unchanged except at x) to x, then z, π_z, o. So the new W-cycle through x contains t.
      - Contradiction as in B2. □
- Final step. Every state t ≥ k0 + r − 1 of S has π_x^t ⊆ R, a simple path with ≤ r − 1 edges ending at o. So κ_{k0+r−1}(x) ⪰
  κ_t(x) ⪰ κ_{k0+r−1}(x) (monotonicity). Equal. □
- Remarks.
  - FRZ-U needs no route form, no (h), and no hypothesis on c_θ, c_w beyond their being constant. It covers U1 (that is R24's κ_w-freeze,
    m* = c_w), P3′ pieces (R22 (c) step 1, m* = c_θ), and U2, U3, U23 alike.
  - R26 limit (ii) ("R24's κ_w-freeze does not transfer") is about the freeze above c_w when c_θ is more relevant. FRZ-U freezes above
    m*, which is the more relevant one.

## 4. Corollary LEN (PROVED, L-SI 10): after the freeze, one frame moves only by lengths
Let S be a run of a stretch and f0 := k0 + r − 1. On states t ≥ f0 of S:
- (LEN-Ξ) If m* = c_θ, then P(Ξ_t(v)) is constant for every v ∈ R. Ξ_t(v) moves only by its length, monotonically.
  - Proof: by (A-Ξ), P(Ξ(v)) = κ(π_v) ∪ C_Ξ when m* = c_θ (under H1 the full path set is A_θ(π_v) ∪ P(θ) with A_θ = κ). The cycle node is
    c_θ, and Ξ is non-decreasing (R15 (a)).
  - The length is |π_v| + ℓ(θ) (H1), or |π_v| (c_θ = o), or the honest distance from v to c_θ inside R (¬H1). For v ∉ {o, c_θ} it lies
    in [1, r − 1] + const. So each v has ≤ r − 2 Ξ-changes on S after f0.
- (LEN-W) If m* = c_w ≻ c_θ, then P(W_t(v)) is constant for every v ∈ R. W_t(v) moves only by its length, monotonically.
  - Proof: (A-W) and WM. The W-length is the distance to c_w inside R (¬H2), or |π_v| + ℓ(w) (H2). Each v ∉ {o, c_w} has ≤ r − 2
    W-changes on S after f0.
- Counts per run S (r = |R|):
  - m* = c_θ: the transitions of S with a Ξ-change on R number ≤ (r − 1) + (r − 1)(r − 2) = (r − 1)².
  - m* = c_w ≻ c_θ: the transitions of S with a W-change on R number ≤ (r − 1)². So the post-freeze part of S splits into
    ≤ (r − 1)(r − 2) + 1 W-flat segments.

## 5. c_w ≻ c_θ with the W frame not in route form (U3, U23; ¬H2, c_w ≠ o)
Kinds as in R26 (c): v ∈ R \ {o} is of KIND A if c_w ∈ π_v, else KIND B. A KIND-B SWITCH is a σ-change at an Even kind-B vertex.
- Lemma KIND-MONO (PROVED, L-SI 10). On the post-freeze part (states ≥ f0) of a run S with c_w ≻ c_θ, ¬H2, c_w ≠ o, each v ∈ R \ {o}
  changes kind at most once. The direction is fixed: B → A if Ω(c_w) is even, A → B if odd.
  Proof.
  - c_w ∈ R is ranked above c_θ, so by (A-Ξ)'s computation, c_w ∈ P(Ξ(v)) ⟺ c_w ∈ π_v ⟺ v is kind A. (c_w ≠ o and c_w ∉ P(θ) ⊆ F ∪ {o}.)
  - P(Ξ(v)) ∩ V_{>c_w} = κ(π_v) ∪ C_Ξ is constant after f0 (FRZ-U).
  - If v's kind differs between consecutive states, c_w is the top of the path-set difference of Ξ(v). Ξ(v) is non-decreasing (R15 (a)),
    with cycle node c_θ fixed. So the new path set contains c_w iff Ω(c_w) is even. □
- Lemma CASC-B (PROVED, L-SI 10; a variant of R26 (c) (i)). In a W-flat segment of a U3 / U23 stretch, take a sub-run in which no vertex
  changes kind (c_w and kind-A vertices may switch). A kind-B vertex v switches there only at sub-run steps ≤ |π_v| − 2.
  Proof. R26 (c) proof step 2, verbatim. Kind-B values and keys do not depend on c_w's or kind-A vertices' choices:
  - A kind-B route consists of kind-B vertices.
  - Ξ of a kind-B vertex depends only on σ along its route and on θ (Fact A).
  - Its W-length |π_v| + d is constant on the W-flat segment.
  - Its tied kind-B candidates and their Ξ-values depend only on kind-B σ's at lower levels.
  - TB's keys of kind-B candidates share the prefix (A1 reversed, o) (TB-even), or are indices (TB-odd).
  - A tied kind-A candidate would be a kind change, excluded.
  - Step 1's "kinds constant" is the hypothesis. R26's event-freeness is used only through it, and through c_w's static choice in the
    kind-A half (step 3), which is not used here. □
- Lemma CW-INT (PROVED, L-SI 10). Let t1 < t2 be states of a run S of a U3 / U23 stretch such that no transition in [t1, t2) has a kind
  change or a kind-B switch. Then c_w switches at ≤ deg(c_w) − 1 transitions of [t1, t2).
  Proof.
  - σ(c_w) is kind B at every state: a kind-A successor's route passes c_w, so c_w's play would cycle avoiding o, and c_w ∈ R is constant.
  - Over [t1, t2], Ξ of every kind-B vertex is constant: its route consists of kind-B vertices, none of which switches, and θ is constant.
  - Each switch of c_w goes to a gate target (R15 (d)): Ξ(σ_{t+1} c_w) ▷ Ξ(σ_t c_w), with all these values constant.
  - So c_w's successors along [t1, t2] have strictly increasing, fixed values: ≤ deg(c_w) distinct successors. □
- Proposition E-SEG (PROVED, L-SI 10, from the three lemmas + R26 (c) (ii), (iii)). Let Q be a post-freeze W-flat segment of a U3 / U23
  run with c_w ≻ c_θ, and e(Q) its transitions with a kind change. Then:
  - N_B(Q) ≤ (e(Q) + 1)(r − 2) (kind-B switch transitions; CASC-B per kind-stable sub-run);
  - the c_w switches satisfy E_cw(Q) ≤ N_cut + (deg(c_w) − 1)(N_cut + 1), with N_cut := e(Q) + N_B(Q) (CW-INT on the gaps between cuts);
  - the events (R26's E) satisfy E(Q) ≤ e(Q) + E_cw(Q);
  - the R-changing transitions of Q number ≤ E(Q) + (E(Q) + 1)(2r − 4) (R26 (c) (iii) per event-free sub-run).
  - Σ_Q e(Q) ≤ r − 2 over the post-freeze part of S (KIND-MONO; o and c_w never change kind).

## 6. Theorem RUN (PROVED, L-SI 10, from §2-§5 and landed results)
Let S be a run of a stretch of a phase on 𝒞^1O, with r = |R| and Δ := max out-degree. The transitions of S with a Ξ-change at some vertex
of R number at most B(r, Δ) = O(Δ·r⁴). By case:
- m* = c_θ (c_θ ⪰ c_w): ≤ (r − 1)² (LEN-Ξ).
- m* = c_w ≻ c_θ, W frame in route form (U1, or U2 with H2 or c_w = o): ≤ (r − 1)² + ((r − 1)(r − 2) + 1)(r − 2).
  - LEN-W counts the W-changes. Each W-flat segment has ≤ r − 2 transitions with a switch on R: R24 (c) CASC (U1) or R26 (a) CASC-U2 (U2).
  - A Ξ-change on R needs a switch on R: Ξ on R is a function of σ on R and of the constant θ (Fact A).
- m* = c_w ≻ c_θ, U3 / U23: ≤ (r − 1)² + Σ_Q RC(Q), over ≤ (r − 1)(r − 2) + 1 segments Q, with RC(Q) from E-SEG.
  - Summing with Σ e(Q) ≤ r − 2 gives O(Δ·r⁴).
- Proof of the case split: c_w ≻ c_θ with W in route form is U1 (both frames in route form) or U2. With W not in route form (¬H2, c_w ≠ o),
  it is U3 (honest in route form) or U23. □

## 7. What this does to the open items of RESULTS R26 / R27 and ledger v2
- (K_W) per stretch (non-fallback W-changes on R), all cases: ≤ (f_st + 1)·n².
  - m* = c_w: LEN-W.
  - m* = c_θ: W-ONCE′ with LEN-Ξ and F1°. The run's W-changing transitions are ≤ 1 + its Ξ-changing transitions ≤ 1 + (r − 1)² +
    (|F| − 1).
  - PROVED (L-SI 10).
- (E) per W-flat run of a U3 / U23 stretch: polynomial, from KIND-MONO, CW-INT, CASC-B (E-SEG) when c_w ≻ c_θ. PROVED (L-SI 10).
  - When c_θ ⪰ c_w, (E) is not needed: LEN-Ξ bounds the Ξ-changes on R directly.
- K (wakes) per phase: every wake is a relevant transition, so K ≤ T_rel, which §8 bounds. The wake mechanism needs no separate treatment.
  - Lemma WAKE's DF-based picture is still right: a wake at k′ ≥ k + 2 is a W-tie, by W-ONCE at k′ − 1.
- R26's reading "(NH′) ⇐ (X), NFB-O, (E), (K_W)": (E) and (K_W) are now PROVED here (L-SI 10, unrefereed). (X) and NFB-O are given by
  FB-POLY (IN REVIEW).

## 8. Corollary PHASE (PROVED, L-SI 10, given the premises named) and the assembly (READING)
Statement. Let a phase on 𝒞^1O have f fallback transitions, X crossings, Θ θ-changes and W_ch w-changes; N_st := 1 + X + Θ + W_ch
stretches. Then
- the Ξ-changing transitions number N_Ξ ≤ f + N_st + (X + 1)(n − 1) + (N_st + f)·B(n, Δ);
- the relevant transitions number T_rel ≤ N_Ξ + S_o;
- T ≤ (m − n + 1)(T_rel + 1).
Proof.
- A relevant transition has a relevant Odd change (≤ S_o of these), or a relevant Even switch y: a → z. In the second case
  Ξ_{k+1}(y) ▷ Ξ_k(y) by (SG) (R19 (d)), so the transition is Ξ-changing.
- The Ξ-changing transitions split into:
  - fallbacks (≤ f);
  - stretch boundaries (≤ N_st − 1);
  - transitions inside runs with a Ξ-change on F: ≤ |F| − 1 per crossing-free interval (F1°, R22 (a)), and ≤ X + 1 intervals;
  - transitions inside runs with a Ξ-change on R: ≤ B per run (Theorem RUN), and ≤ N_st + f runs.
- T ≤ (m − n + 1)(T_rel + 1) is Theorem LP (R27 (d)). □
Premises for "polynomial per phase" (each with its status):
| quantity | bound | status |
| --- | --- | --- |
| f | ≤ 1 + (n − 2)(2n − 1) | FB-POLY (P-N5-FBPOLY, IN REVIEW); FB-PHASE second proof (L-SI 9, lane) |
| X | ≤ (f + 1)(n − 1) + f + X_SN, X_SN ≤ 13(d_o + 1)n³(f + 1 + T) + T, T ≤ n² + 2n − 1 | LANDED R30 (c), R34 (e), (f) (given f) |
| Θ | ≤ (n − 1) + n(X + 1) + X if λ_Ξ(o) ≠ o; 0 if λ_Ξ(o) = o | LANDED R27 (g) TH |
| S_o | ≤ d_o(Θ + 1) | LANDED R27 (g) SO |
| W_ch | ¬H2: ≤ (f_I + 1)(|R|² − 1) + f_I per crossing-free interval I; H2: w = o ⊕ Ξ(τ(o)) with τ(o) ∈ F, so ≤ |F| − 1 per I (F1°, R19 (a), (V1)); c_w = o: 0 | LANDED R24 (e), R22 (a), (b) |
| B(n, Δ) | O(Δ n⁴) | Theorem RUN (PROVED here, unrefereed) |
- So T per phase = poly(n, m) given f (Corollary PHASE).
- Assembly (READING). The phases number ≤ n(n − 1) + d (P-N5-PHI, IN REVIEW). Each iteration costs poly(n, m) bit operations (SPEC, cost
  section). So N5 on 𝒞^1O runs in polynomial time IF:
  - P-N5-FBPOLY (or FB-PHASE) and P-N5-PHI are signed;
  - this note's Lemmas W-ONCE (needed only for (K_W)), FRZ-U, LEN, KIND-MONO, CASC-B, CW-INT and Theorem RUN are signed;
  - CHECKER confirms the assembly.
  - Until then: NO polynomial bound for N5 is proved, and G-N5-TIME stays OPEN.
- Crude size: X = O(d_o·n⁵) ⊆ O(n⁶) (from f = O(n²)), Θ = O(n⁷), W_ch = O(n²(f + X)) = O(n⁸), N_st = O(n⁸). So N_Ξ = O(Δ·n¹²) and
  T = O(m·Δ·n¹²) per phase. The bound is loose and unoptimised.

## 9. Where a referee should push (my own list of the weakest points)
1. FRZ-U Case B3 and B2 use "x ∈ R_{k+1} has W cycle node c_w". This holds because R and w are constant on the stretch and every
   R-vertex's W-play ends in C_W (¬H2) or at c_w in F (H2).
2. Fact A under ¬H1: the honest play of v ∈ R is π_v up to c_θ, or π_v then o → … → c_θ along C_Θ. This uses "every Odd vertex but o is
   forced" (𝒞^1O).
3. CASC-B claims R26 (c) step 2 never uses c_w's static choice. Check the TB-even key: pk(z) is read from c_w back to z. For kind-B z the
   prefix (A1 reversed, o) is common at each step, and A1 can change between steps.
4. CW-INT needs every c_w switch to be strict in Ξ (R15 (d): S4a moves only to arena edges, and a moved edge is a gate edge).
5. Corollary PHASE counts stretch boundaries and fallbacks as Ξ-changing (crude). Runs are maximal non-fallback runs INSIDE one stretch,
   so every transition of a phase is a run transition, a fallback, or a stretch boundary.
6. LEN's length ranges: ¬H2 W-length is the distance to c_w along the W-play, inside R, so ≤ r − 1. ¬H1 honest length is likewise ≤ r − 1.

## 10. DATA (experiments/si/kw15/; REFEREE-2's SPEC-mode tracer read only; every game asserted 𝒞^1O; DATA, not proof)
- Scripts:
  - kwcheck.py checks, per trace: WONCE, AGREE (Fact A's formulas for both frames above m*), FRZ (freeze from k0 + |R| − 1), LEN, KIND
    (≤ 1 change per vertex and the direction) and CWINT.
  - kwclimb.py: random o-cyclic 𝒞^1O games (RC.rand_game) and hill-climbs (FCL mutations).
- Corpus 1: every .pg file in experiments/ and docs/ (1,101 files; 500 𝒞^1O, 600 not 𝒞^1O, 1 unparsable; S3 start + 2 random starts). Logs: logs/all_r2_c0..3.txt.
  - 1,502 runs, 6,151 AGREE states, 1,334 FRZ state checks: 0 failures.
  - Largest actual freeze delay: 1 transition (bound |R| − 1).
- Corpus 2: 3,000 random games, n 6-40 (logs/random_3000.txt): 0 failures. Nearly vacuous: runs of ≤ 4 transitions.
- Climbs (seconds 2400 / 1500; logs/climb_*.txt), totals over all evaluated games:
  - ≈ 8.6M AGREE states and ≈ 2.6M FRZ state checks: 0 failures.
  - WONCE: 849k checks over 1.5M Ξ-flat S4a transitions (wonce2 climbs): 0 failures.
  - KIND / CWINT: 481k post-freeze runs with c_w ≻ c_θ and ¬H2 (kind2 climbs): 0 failures.
- VACUITY (honest):
  - No post-freeze kind change and no post-freeze c_w switch was observed anywhere. So KIND-MONO's direction claim and CW-INT have NO
    data support; they rest on their proofs.
  - Longest post-freeze part of a run: 23 transitions (library). Max Ξ-changes on R in one run: 40 (library); in climbs 25 at n 29.
- Not run: an independent tracer (all traces are REFEREE-2's SPEC mode), and a check of Theorem RUN's numeric bound per run. The bound
  is far above the observed maxima, so such a check would be vacuous.
