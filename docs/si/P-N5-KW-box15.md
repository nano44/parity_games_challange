# Referee packet P-N5-KW: on 𝒞^1O, inside a phase, the Ξ-changes on R of every fallback-free run of a stretch are O(Δ·|R|⁴); so (K_W), (E) and K are polynomial per stretch, and the transitions per phase are polynomial GIVEN f
Author: L-SI successor 10 (Opus 5.5; D15, D18, L37, L40), session_01PBqfsNWMhTPn7yNJ8C18HP. Packet written at the Lead's request of
21:22Z (Lead's stamp), from docs/si/N5-KW-box15.md (sha1 5ebbb3b6, frozen) with the six additions the Lead listed from L-NEW 21's cross-read.
Stamp: in the commit (date -u). FROZEN once its sha1 is reported; repairs go to a NEW fixes file.
- Scope: the candidate N5 (SPEC docs/new/N5-ssi-global.md) on 𝒞^1O, inside one phase. Not a TARGET.md claim, not a step-4 pass.
  𝒞^1O is polynomial by other means. Nothing here touches games with two or more Odd choice vertices. G-N5-TIME stays OPEN.
- D1: every statement below is wrong until a referee has checked its proof.

## 0. What to sign, what not to sign, and the dependencies
| § | statement | label | to sign |
| --- | --- | --- | --- |
| §2 | Lemma W-ONCE (every game) | PROVED | yes |
| §3 | Fact A (coarse and full values on R), Fact B (agreement above m*) | PROVED | yes |
| §3 | Lemma FRZ-U (κ-freeze on every fallback-free run of every stretch) | PROVED | yes |
| §4 | Corollary LEN | PROVED | yes |
| §5 | Lemma PAR (L-NEW 21), Lemma H-PATH, Lemma KIND-MONO, Lemma CASC-B, Lemma CW-INT, Proposition E-SEG | PROVED | yes |
| §6 | Theorem RUN | PROVED | yes |
| §7 | Corollary KW-S ((K_W), (E), K per stretch) | PROVED | yes |
| §8 | Corollary PHASE: T per phase ≤ an explicit polynomial in (n, m, f), CONDITIONAL ON f ONLY | PROVED (conditional on f) | yes |
| §8 | how FB-POLY's bound plugs in; the 𝒞^1O assembly with the phase count | READING | no |
| §9 | weak points | READING | no |
| §10 | data | DATA | no |
| §11 | the two lane notes | not to sign | no |

Dependencies (every one is LANDED, except the two marked IN REVIEW, which only the READINGs of §8 use):
| item | where | status |
| --- | --- | --- |
| (V1), (V2), (C1), (C4), lev, COARSE_L, the valuation order | RESULTS R25 setting; docs/new/P-N5-LP-box32.md §0 | LANDED |
| Ξ_{k+1} ⊵ Ξ_k; a switched Even vertex moves to a gate target (σ_{k+1}(y) ∈ {σ_k(y)} ∪ Iσ_k(y)) | R15 (a), (d) | LANDED |
| (F1): the S4a result is the pointwise optimum of its one-player arena in G_τ | R17 (F1) | LANDED |
| Lemma G (a): off R, Ξ = W, with no (h) needed | R19 (a) | LANDED |
| (SG): a switched Even y with λ(y) ≠ y has Ξ_{k+1}(y) ▷ Ξ_k(y) | R19 (d) | LANDED |
| Lemma XW: Ξ_k ⊴ W_k pointwise | R21 (a) | LANDED |
| F1°: on a crossing-free interval I, Ξ changes on F at ≤ max(0, |F| − 1) transitions; TC (i) | R22 (a), (b) | LANDED |
| WM: W_{k+1} ⊵ W_k at in-phase non-fallback transitions | R23 (g) | LANDED |
| Lemma R; Lemma TB; CASC; WC | R24 (a), (b), (c), (e) | LANDED |
| CASC-U2; CASC-U3 (ii), (iii) | R26 (a), (c) | LANDED |
| Lemma U; Theorem LP; TH; SO | R27 (a), (d), (g) | LANDED |
| SN-PREFIX | R30 (c) | LANDED |
| TOGGLE-COUNT, X-SN-PHASE | R34 (e), (f) | LANDED |
| KEY: (λ_Ξ, τ)-phases are the joint λ-phases | R38 (a) | LANDED |
| f per phase ≤ 1 + (n − 2)(2n − 1) (FB-POLY) | P-N5-FBPOLY | IN REVIEW (READING of §8 only) |
| #phases ≤ n(n − 1) + d (Corollary Φ-1O) | P-N5-PHI (+ fixes 29936b3d) | IN REVIEW, at CHECKER as R47 (READING of §8 only) |
R20 (d) Lemma P^c / CR is the model of FRZ-U's proof. FRZ-U is proved in full below and does not cite it.

## 1. Setting and notation
- 𝒞^1O: o is the only Odd vertex of out-degree > 1. PHASE: a maximal run of states with λ_Ξ and τ constant (R27 setting; joint λ-phase
  by R38 KEY). τ is constant in a phase. If S4a leaves σ unchanged and S4b leaves τ unchanged, the S4c fallback is Even's, because
  Iσ ≠ ∅ (otherwise the fallback would be Odd's, changing τ: SPEC S4c, FIX 3). So every in-phase transition is an S4a step or an Even
  S4c fallback.
- R = R_k := {v : v's (σ_k, τ_k)-play reaches o}, o ∈ R; r := |R|; F := V \ R. π_v := v's (σ, τ)-path before its first visit of o
  (π_o = ∅). A CROSSING changes R; a crossing-free interval is a maximal run of states of a phase with R constant.
- θ := Ξ(o), w := W(o) (W_k := the play value of (σ_k, τ_k)), c_θ := λ_Ξ(o), c_w := the cycle node of w.
  - H1: o's honest play (σ, σ̄) does not return to o. H2: o's W-play does not return to o, i.e. τ(o) ∈ F.
  - Route form (P-N5-NH §3, as in R22-R26): the honest frame is in route form if H1 or c_θ = o; the W frame if H2 or c_w = o.
  - Under ¬H1 o lies on its honest cycle C_Θ ⊆ R with top c_θ, and θ = (c_θ, ∅, d_θ). Under ¬H2 o lies on its W-cycle C_W ⊆ R with top
    c_w, and w = (c_w, ∅, d). Write C_W = o → A1 → c_w → A2 → o: A1 holds the vertices strictly between o and c_w on o's W-path, A2 those
    strictly between c_w and o (R24 (e) step 1; R26 (c) setting).
- STRETCH: a maximal run of states of a phase with R, θ, w constant (R26 setting). A stretch lies in one crossing-free interval.
- RUN S of a stretch: a maximal run of consecutive NON-fallback transitions of the stretch. States k0, …, kT; all its transitions are
  S4a steps with the same τ, R, θ, w.
- m* := the more relevant of c_θ and c_w (c_θ if they are equal). V_{>m*}: the vertices of rank > rank(m*). κ(ρ) := ρ ∩ V_{>m*} for a
  vertex set ρ. κ_k(v) := κ(π_v^k).
- κ-ORDER on subsets of V_{>m*}: A ⪯ B iff A = B, or the top t of A Δ B lies in B with Ω(t) even, or in A with Ω(t) odd. This is
  SPEC S1's path-set order (Q1 there). If C is disjoint from A ∪ B, then A ⪯ B ⟺ A ∪ C ⪯ B ∪ C. Adding one element x ∉ A ∪ B to both
  sides preserves ⪯.
- Kinds (R26 (c)), under ¬H2 with c_w ≠ o: v ∈ R \ {o} is of KIND A if c_w ∈ π_v, else KIND B. c_w is kind A, and A2's vertices are
  kind B. A KIND-B SWITCH is a σ-change at an Even kind-B vertex.
- W-FLAT SEGMENT: a run of consecutive non-fallback transitions of a stretch at each of which W is unchanged at every vertex of R. It is a
  contiguous part of one of R24 / R26's W-flat runs.
- Δ := the maximum out-degree; d_o := |succ(o)|; m := #edges; n := |V|.

## 2. Lemma W-ONCE (PROVED; every game)
Statement. Let k → k+1 → k+2 be two consecutive S4a transitions (no fallback) of one phase, with Ξ_{k+1} = Ξ_k at every vertex. Then
W_{k+2} = W_{k+1} at every vertex.
Proof.
1. The arenas (SPEC S4a): for Even v, A_j(v) := {σ_j(v)} ∪ {z : Ξ_j(z) ▷ Ξ_j(σ_j v)}; an Odd v keeps only τ(v), and τ is the same at
   k, k+1, k+2.
2. A_{k+1}(v) ⊆ A_k(v) for every Even v.
   - σ_{k+1}(v) ∈ A_k(v), so Ξ_k(σ_{k+1} v) ⊵ Ξ_k(σ_k v).
   - If z ∈ A_{k+1}(v) and z ≠ σ_{k+1}(v), then Ξ_k(z) = Ξ_{k+1}(z) ▷ Ξ_{k+1}(σ_{k+1} v) = Ξ_k(σ_{k+1} v) ⊵ Ξ_k(σ_k v). So z ≠ σ_k(v) and
     z ∈ A_k(v).
3. By (F1), W_{k+1} is the pointwise optimum over the strategies of the arena H_k, and W_{k+2} that over H_{k+1}.
   - σ_{k+1} is a strategy of H_{k+1}, so W_{k+2} ⊵ W_{k+1}.
   - Every strategy of H_{k+1} is one of H_k (step 2), so W_{k+2} ⊴ W_{k+1}. □
Corollary W-ONCE′. In a phase, an S4a transition that changes W is the phase's first transition, or follows a fallback, or follows a
Ξ-changing transition.
- L-NEW 21's Lemma WLAG (docs/new/N5-KW-box42.md §1) is a slightly stronger form, found independently.

## 3. The coarse freeze on every stretch
**Fact A0 (full values on R; PROVED).** On a stretch, for v ∈ R \ {o}:
- (Ξ) Ξ(v) = (v's σ-path up to its first vertex in {o, c_θ}) ⊕ T_Ξ, by iterated (V1). The terminal value T_Ξ is θ at o and
  (c_θ, ∅, 0) at c_θ (the latter only under ¬H1). That σ-path is a prefix of π_v.
  - So Ξ(v) depends only on σ at the vertices of π_v (forced Odd vertices never move), and on the stretch constants θ, c_θ.
  - In particular λ_Ξ(v) = c_θ.
- (W) W(v) = (v's σ-path up to its first vertex in {o, c_w}) ⊕ T_W, with T_W = w at o and (c_w, ∅, 0) at c_w (the latter only under
  ¬H2). That path is again a prefix of π_v; W(v) depends only on σ at π_v and on w, c_w; the W cycle node of v is c_w.
Proof.
- Every Odd vertex other than o is forced, so v's honest play and its W-play both follow σ along π_v until they first meet o, or a
  vertex where they stop because it is their cycle node.
- Honest frame:
  - H1: o's honest continuation enters F and never returns to o. It avoids π_v: a vertex of π_v would lead back to o. So Ξ(v) = π_v ⊕ θ
    (iterated (V1); P-N5-NH (R1), R19 (a) Lemma G (b), honest half). c_θ ∈ F is not on π_v.
  - c_θ = o: v's play reaches o, which is the cycle node, so Ξ(v) = π_v ⊕ (o, ∅, 0) = π_v ⊕ θ.
  - ¬H1, c_θ ≠ o: if c_θ ∈ π_v, v's honest play stops at c_θ. Otherwise it reaches o and follows C_Θ's arc o → … → c_θ.
    - That arc avoids π_v. If π_v met C_Θ at q ≠ o, then π_v would follow C_Θ's σ-edges from q to o. Since c_θ ∉ π_v, q lies on the
      arc c_θ → … → o, which is disjoint from the arc o → … → c_θ.
    - So in both cases (V1) iterates along the prefix of π_v up to the first of o, c_θ, with terminal θ or (c_θ, ∅, 0).
    - (θ = o ⊕ … ⊕ (c_θ, ∅, 0) along the arc o → c_θ; both terminals are constants of the stretch.)
- W frame: the same, with H2, c_w, C_W, w. □
**Fact A (coarse values on R; PROVED).** On a stretch, for v ∈ R:
- (A-Ξ) P(Ξ(v)) ∩ V_{>m*} = κ(π_v) ⊔ C_Ξ, where C_Ξ := P(θ) ∩ V_{>m*} under H1 and C_Ξ := ∅ otherwise;
- (A-W) P(W(v)) ∩ V_{>m*} = κ(π_v) ⊔ C_W, where C_W := P(w) ∩ V_{>m*} under H2 and C_W := ∅ otherwise.
- C_Ξ and C_W are constant on the stretch and disjoint from π_v.
Proof.
- H1: Ξ(v) = π_v ⊕ θ, with path set (π_v ∩ V_{>c_θ}) ⊔ P(θ), and P(θ) ⊆ F ∪ {o}. Intersect with V_{>m*} ⊆ V_{>c_θ}.
- c_θ = o: the path set is π_v ∩ V_{>o}.
- ¬H1, c_θ ≠ o: by A0, the path is a prefix of π_v up to c_θ, or π_v followed by C_Θ's arc o → c_θ. Vertices of π_v after c_θ, and
  the arc, lie on C_Θ, so they are below c_θ. So P(Ξ(v)) = π_v ∩ V_{>c_θ}.
- W frame: the same (H2: P(w) ⊆ F ∪ {o}; ¬H2: P(W(v)) = π_v ∩ V_{>c_w}).
- m* ⪰ c_θ and m* ⪰ c_w. □
**Fact B (agreement above m*; PROVED).** At a state of a stretch, let y, z ∈ R with κ(π_y) ≠ κ(π_z). Then
Ξ(y) ◁ Ξ(z) ⟺ W(y) ◁ W(z) ⟺ κ(π_y) ≺ κ(π_z).
Proof.
- Within each frame the cycle nodes agree (A0).
- The path sets differ, in the frame with cycle node c, by (π_y Δ π_z) ∩ V_{>c} (the constant parts are common and disjoint).
- Its top is the top t of κ(π_y) Δ κ(π_z): t ∈ V_{>m*}, and every other differing vertex is in the κ-difference or ranked ≤ m*.
- Both frames decide by t's membership and parity, which is the κ-order. □
- L-NEW 21's Lemmas ABOVE-h and CSTRICT (docs/new/N5-KW-box42.md §2) are the same facts, found independently.

**Lemma FRZ-U (PROVED).** Let S be a run of a stretch (states k0, …, kT). Then for every state t ≥ k0 + r − 1 of S and every v ∈ R:
κ_t(v) = κ_{k0+r−1}(v).
Proof. Claim P^c: for every k = k0 + j in S, every x ∈ R, and every simple path ρ = (x = ρ_0, …, ρ_L = o) of G_τ with all vertices in
R and ρ_i ≠ o for i < L, with L ≤ j: κ_k(x) ⪰ κ(ρ) := κ({ρ_0, …, ρ_{L−1}}).
- (MON) For x ∈ R and consecutive states k, k+1 of S: κ_k(x) ⪯ κ_{k+1}(x).
  - WM (R23 (g)) gives W_{k+1}(x) ⊵ W_k(x), and both have cycle node c_w (A0).
  - By (C1), COARSE_{m*} is order-preserving. By (A-W), κ_k(x) ⊔ C_W ⪯ κ_{k+1}(x) ⊔ C_W, and C_W is common.
- Base j = 0: only x = o, ρ = (o), κ(ρ) = ∅ = κ_k(o).
- Step from k = k0 + j to k + 1. If x = o, there is nothing to prove. Otherwise ρ = x → z → ρ′, where z ∈ R and ρ′ is a simple path from
  z to o avoiding x with |ρ′| ≤ j. Induction hypothesis (IH): κ_k(z) ⪰ κ(ρ′). Let a := σ_k(x) if x is Even. If x is Odd (x ≠ o, so
  x is forced), a := its only successor, which is z.
  - Case A: κ_k(z) ⪯ κ_k(a).
    - κ(ρ′) ⪯ κ_k(z) ⪯ κ_k(a), by (IH) and Case A.
    - x ∉ ρ′ (ρ is simple) and x ∉ π_a^k (π_x = x·π_a is simple). So adding x to both sides preserves ⪯:
      κ(ρ) = κ({x}) ⊔ κ(ρ′) ⪯ κ({x}) ⊔ κ_k(a) = κ_k(x) ⪯ κ_{k+1}(x), the last step by (MON).
  - Case B: κ_k(z) ≻ κ_k(a). Then x is Even.
    - By Fact B, Ξ_k(z) ▷ Ξ_k(a) and W_k(z) ▷ W_k(a). So (x, z) ∈ Iσ_k, and σ̂ := σ_k[x ↦ z] is a strategy of the arena H_k.
    - By (F1), W_{k+1}(x) ⊵ val_σ̂(x), where val_σ̂ is the value of the (σ̂, τ)-play.
    - B1: x ∉ π_z^k, and (H2 or x ∉ C_W).
      - z's (σ_k, τ)-play is π_z, then o, then o's W-continuation: in F (H2), or C_W (¬H2). It does not pass x.
      - So val_σ̂(x) = x ⊕ W_k(z) by (V1). Taking COARSE_{m*} ((C1), (C4), (A-W)) gives
        κ_{k+1}(x) ⪰ κ({x}) ⊔ κ_k(z) ⪰ κ({x}) ⊔ κ(ρ′) = κ(ρ), since x ∉ π_z and x ∉ ρ′.
      - x ∈ R_{k+1} (R is constant on S), so κ_{k+1}(x) is read through (A-W) at k + 1.
    - B2: x ∈ π_z^k. Then π_z = (z, …, x)·π_x = (z, …, x)·x·π_a, so the σ̂-play from x is the cycle Z := x → z → … → x inside R,
      avoiding o.
      - κ(π_z) = κ(Z) ⊔ κ(π_a), so κ_k(z) ≻ κ_k(a) says κ(Z) ≠ ∅, with an even top t.
      - top(Z) = t: every vertex of Z above m* is in κ(Z).
      - t is even and ranked above c_w, so reward(t) > reward(c_w).
      - So val_σ̂(x) has cycle node t. By (F1) the cycle node of W_{k+1}(x) has reward ≥ reward(t) > reward(c_w).
      - But x ∈ R_{k+1}, so its W cycle node is c_w (A0; w is constant on the stretch). Contradiction: B2 does not occur.
    - B3: ¬H2, x ∈ C_W \ {o} (x is Even, so x ≠ o), and x ∉ π_z^k.
      - π_x follows C_W from x to o, so κ_k(a) = ∅. Every vertex of C_W is ⪯ c_w ⪯ m*.
      - So κ_k(z) ≻ ∅: κ(π_z) ≠ ∅, with an even top t ∈ V_{>m*}.
      - The σ̂-play from x is x → π_z → o, then o's σ̂-play. Every edge of C_W except x's is unchanged, and o's W-play runs along C_W
        and reaches x:
        - x ∈ A1 ∪ {c_w}: o → τ(o) → … along A1 → x. The σ̂-play from x is the cycle Z = x · π_z · (C_W from o up to, not including, x).
        - x ∈ A2: o → A1 → c_w → (A2 up to x). Z = x · π_z · (o → A1 → c_w → A2 up to, not including, x).
      - Z is simple. π_z avoids the C_W-arc from o to x: if π_z met that arc at q, it would follow the arc's σ-edges from q to x, so
        x ∈ π_z, against B3.
      - top(Z) = t: the vertices of Z above m* are those of κ(π_z), with top t; the arc lies on C_W, ⪯ c_w.
      - Contradiction exactly as in B2. B3 does not occur. □
- Closing step. For every state t ≥ k0 + r − 1 of S, π_x^t ∪ {o} ⊆ R_t = R is a simple path from x to o with ≤ r − 1 edges. So
  κ_{k0+r−1}(x) ⪰ κ_t(x) (Claim P^c) ⪰ κ_{k0+r−1}(x) (MON, iterated). Equal. □
- Remarks.
  - FRZ-U uses no route form, no (h), and nothing about c_θ, c_w except that they are constant. R24's κ_w-freeze (U1) and P3′ step 1
    (R22 (c)) are the route-form special cases.
  - R26 limit (ii) noted that the freeze above c_w does not transfer when c_θ is the more relevant. FRZ-U freezes above m*.
  - L-NEW 21's Theorem KW-FREEZE (a) is the same freeze, with paths to the W-terminals o and c_w and index n − 1 ≥ r − 1.

## 4. Corollary LEN (PROVED)
Let S be a run of a stretch and f0 := k0 + r − 1. On states t ≥ f0 of S:
- (LEN-Ξ) If m* = c_θ (c_θ ⪰ c_w), then P(Ξ_t(v)) = P(Ξ_{f0}(v)) for every v ∈ R. Ξ_t(v) moves only by its length, monotonically.
  - Proof: when m* = c_θ, (A-Ξ) and its proof show that the whole path set of Ξ(v) is κ(π_v) ⊔ C_Ξ (under H1: P(θ) ⊆ V_{>c_θ}). It is
    frozen by FRZ-U. The cycle node is c_θ, and Ξ is ⊵-non-decreasing (R15 (a)).
  - The length is that of the path in A0(Ξ): ≤ r − 1 for v ∉ {o, c_θ}, plus the constant terminal length; Ξ(o) = θ and Ξ(c_θ) are
    constant. So each v has ≤ r − 2 Ξ-changes on S after f0.
- (LEN-W) If m* = c_w ≻ c_θ, then P(W_t(v)) = P(W_{f0}(v)) for every v ∈ R. W_t(v) moves only by its length, monotonically (WM).
  - Each v ∉ {o, c_w} has ≤ r − 2 W-changes on S after f0.
- Counts per run S:
  - m* = c_θ: the transitions of S with a Ξ-change on R number ≤ (r − 1) + (r − 1)(r − 2) = (r − 1)².
  - m* = c_w ≻ c_θ: the transitions of S with a W-change on R number ≤ (r − 1)². The part of S after f0 splits into
    ≤ (r − 1)(r − 2) + 1 W-flat segments.

## 5. c_w ≻ c_θ (PAR, kinds, c_w's switches)
**Lemma PAR (PROVED; L-NEW 21, docs/new/N5-KW-box42.md v3.2 §5, l-new 31776c5c).** At every state of a phase on 𝒞^1O: if c_w ≻ c_θ,
then Ω(c_w) is even.
Proof.
- R21 (a) XW gives θ = Ξ(o) ⊴ W(o) = w. The cycle nodes differ, and valuations compare the rewards of their cycle nodes first, so
  reward(c_θ) < reward(c_w) (rewards are injective, SPEC S1).
- If c_w were odd, reward(c_w) = −p′(c_w) < 0. If c_θ is even, then reward(c_θ) > 0. If c_θ is odd, then reward(c_θ) = −p′(c_θ) >
  −p′(c_w), because c_w ≻ c_θ.
- Both contradict reward(c_θ) < reward(c_w). □

**Lemma H-PATH (PROVED; L-NEW 21's statement).** On a stretch with ¬H2, c_w ≠ o and c_w ≻ c_θ: for v ∈ R \ {o}, c_w ∈ P(Ξ(v)) iff v
is of kind A.
Proof.
- c_w ∉ C_Θ under ¬H1: c_θ tops C_Θ and c_w ≻ c_θ. Under H1, c_θ ∈ F; under c_θ = o, the honest path is π_v.
- So, under ¬H1, if c_w ∈ π_v then c_w precedes c_θ on π_v. After c_θ, π_v runs along C_Θ, which avoids c_w.
- By A0 / (A-Ξ), the honest path is the prefix of π_v up to the first of o, c_θ, followed (if c_θ ∉ π_v) by part of C_Θ, or by o's
  honest continuation in F under H1.
- So c_w lies on the honest path iff c_w ∈ π_v. c_w ≻ c_θ puts it in the path set. Also c_w ∉ P(θ), since P(θ) ⊆ F ∪ {o} and c_w ≠ o
  is in R. □

**Lemma KIND-MONO (PROVED).** In a run S of a stretch with ¬H2, c_w ≠ o and c_w ≻ c_θ, after f0 = k0 + r − 1 every v ∈ R \ {o} changes
kind at most once, and only from B to A.
Proof.
- After f0, P(Ξ(v)) ∩ V_{>c_w} = κ(π_v) ⊔ C_Ξ is constant (FRZ-U; m* = c_w).
- If v's kind differs at consecutive states t, t+1, then by H-PATH c_w is in exactly one of the two path sets, and it is their top
  difference.
- Ξ_{t+1}(v) ⊵ Ξ_t(v) (R15 (a)), with cycle node c_θ at both states. So the new path set contains c_w iff Ω(c_w) is even.
- By PAR, Ω(c_w) is even. So the change is B → A, and a kind-A vertex never becomes kind B again on S after f0. □

**Lemma CASC-B (PROVED; a variant of R26 (c) (i)).** Let Γ be a W-flat segment of a U3 / U23 stretch (¬H2, c_w ≠ o) with no kind
change at any of its transitions; c_w and kind-A vertices may switch. Number Γ's transitions 0, 1, …. A kind-B vertex v switches in Γ
only at steps ≤ |π_v| − 2.
Proof. This is R26 (c)'s proof, step 2 (kind B), which runs the induction of R26 (a)'s step 4 (= R24 (c) CASC step 3).
- That step uses R26's "event-free" hypothesis only through its step 1 (kinds constant), which is Γ's hypothesis here.
- c_w's switches enter R26's proof only in step 3 (kind A, through Ξ(c_w)), which is not used.
- Written out:
1. Levels. For kind-B v, A0 gives W(v) = π_v ⊕ w (the W-path reaches o before c_w), of length |π_v| + d. W is unchanged on Γ, so
   ℓ(v) := |π_v| is constant on Γ.
2. The choice rule. Let v be an Even kind-B vertex that switches at step j. v is not its own W cycle node (that is c_w, which is kind A),
   and W′ = W at every vertex of R.
   - By R24 (b) TB, proof steps 2-5, with R24 (a) Lemma R (as used in R24 (c) step 1 and R26 (a) step 3): σ_{j+1}(v) is the
     key-minimum among the arena edges of v that are TIED (W(z) ⊕ v = W(v)).
   - A tied successor in F would make v leave R, which is impossible inside the stretch.
   - A tied successor of kind A would change v's kind, which is excluded.
   - So the candidates are tied kind-B vertices z with |π_z| = ℓ(v) − 1, and o if ℓ(v) = 1.
3. Honest values of kind-B candidates. A kind-B route consists of kind-B vertices. By A0, Ξ(z) depends only on σ at the vertices of π_z
   (all of lower level) and on constants.
4. Keys of kind-B candidates.
   - TB-odd mode (c_w odd; vacuous here by PAR when c_w ≻ c_θ, kept for c_θ ⪰ c_w): the key is the vertex index.
   - TB-even mode: pk(z) is the root-first index sequence of z's σ_{j+1}-play from c_w (excluded) back to z. For kind-B z that play is
     π_z, o, A1, c_w, so pk(z) = (A1 reversed, o) followed by π_z reversed.
   - At a fixed step j, the prefix (A1 at state j+1, reversed, then o) is the SAME for every kind-B candidate. So comparing keys of two
     kind-B candidates at step j compares their route parts only, which depend only on σ_{j+1} along π_z.
   - A1 can change from step to step (kind-A re-routings); that changes the common prefix only, never the order among kind-B
     candidates.
5. Induction (R26 (a) step 4 verbatim). Let S_ℓ be the first step of Γ from which no kind-B vertex of level ≤ ℓ switches.
   - S_1 = 0: a level-1 kind-B vertex has o as its only tied kind-B candidate.
   - Let j := S_{ℓ−1}, v of kind B and level ℓ, and z1 := σ_{j+1}(v), the key-minimum at step j. Take a step j′ > j with σ_{j′}(v) = z1,
     and any tied kind-B arena candidate z ≠ z1 at j′.
   - z's route lies at levels ≤ ℓ − 1, which are fixed from step j on. So Ξ_{j′}(z) = Ξ_j(z), z is tied at j, and its route part of the
     key is unchanged.
   - Ξ_j(z) = Ξ_{j′}(z) ▷ Ξ_{j′}(z1) = Ξ_j(z1) ⊵ Ξ_j(σ_j v) (z1 was in the arena at j). So z ≠ σ_j(v), and z was a tied arena candidate
     at j. Hence key(z) > key(z1) there, and so at j′.
   - So v keeps z1 at j′, and S_ℓ ≤ S_{ℓ−1} + 1 ≤ ℓ − 1. □
- L-NEW 21's Lemma CASC-B (docs/new/N5-KW-box42.md §5) is the same lemma, found independently.

**Lemma CW-INT (PROVED).** In a run S of a stretch with ¬H2, c_w ≠ o, let t1 < t2 be states of S such that no transition in [t1, t2)
has a kind change or a kind-B switch. Then c_w switches at ≤ deg(c_w) − 1 transitions of [t1, t2).
Proof.
1. At every state, σ(c_w) is kind B. A kind-A successor's route passes c_w, so c_w's play would cycle without o, and c_w would leave R.
   R is constant.
2. Ξ is constant on kind-B vertices over the states t1, …, t2. A kind-B route consists of kind-B vertices, none of which switches in
   [t1, t2), and the kind-B set is constant there (no kind change). So by A0 Ξ(z) is constant for every kind-B z.
3. At each switch of c_w at a transition t ∈ [t1, t2), the new successor is a gate target (R15 (d)): Ξ_t(σ_{t+1} c_w) ▷ Ξ_t(σ_t c_w).
   - Both successors are kind B at t, since there is no kind change at t (step 1 at t and at t+1), and their values are the constant ones.
4. So c_w's successors along [t1, t2] have strictly increasing fixed values, hence they are distinct: ≤ deg(c_w) − 1 switches. □
- L-NEW 21's Lemma CW (v3.2, corrected at cc2de675) is the same argument.

**Proposition E-SEG (PROVED).** Let S be a run of a stretch with ¬H2, c_w ≠ o, c_w ≻ c_θ, and Q a W-flat segment of S after f0. Let e(Q)
be the transitions of Q with a kind change. Then:
- (i) N_B(Q) ≤ (e(Q) + 1)(r − 2), where N_B(Q) counts the transitions of Q with a kind-B switch. Apply CASC-B on each of the ≤ e(Q) + 1
  kind-change-free parts; levels are ≤ r − 1, so switches fall at steps 0, …, r − 3.
- (ii) Let N_cut(Q) := e(Q) + N_B(Q) ≤ (e(Q) + 1)(r − 1). Then c_w switches at ≤ N_cut(Q) + (deg(c_w) − 1)(N_cut(Q) + 1)
  ≤ Δ·(N_cut(Q) + 1) transitions of Q. CW-INT applies on each of the ≤ N_cut(Q) + 1 gaps between cut transitions; the cut transitions
  themselves are counted once each.
- (iii) Let E(Q) count the transitions of Q with an EVENT (R26 (c): a switch of an Even R-vertex that changes its kind, or a switch of
  c_w). Then E(Q) ≤ e(Q) + Δ(N_cut(Q) + 1) ≤ (e(Q) + 1)(Δ·r + 1) − 1.
- (iv) The transitions of Q with a switch on R number ≤ E(Q) + (E(Q) + 1)(2r − 4) ≤ (E(Q) + 1)(2r − 3).
  - Use R26 (c) (iii) on each event-free part: no R-vertex switches at a step ≥ 2r − 4 of the maximal event-free sub-run containing it.
    So an event-free part of Q has ≤ 2r − 4 transitions with a switch.
- (v) Σ_Q e(Q) ≤ r − 2 over the W-flat segments of S after f0. By KIND-MONO each vertex of R \ {o, c_w} changes kind at most once there,
  and o, c_w never change kind. □

## 6. Theorem RUN (PROVED)
Statement. Let S be a run of a stretch of a phase on 𝒞^1O, r = |R|. The transitions of S with a Ξ-change at some vertex of R number at
most B(r) ≤ 3Δ·r⁴. By case:
- (a) m* = c_θ (c_θ ⪰ c_w): ≤ (r − 1)² (LEN-Ξ).
- (b) m* = c_w ≻ c_θ, W frame in route form (H2, or c_w = o): ≤ (r − 1)² + ((r − 1)(r − 2) + 1)(r − 2) ≤ r³.
- (c) m* = c_w ≻ c_θ, ¬H2, c_w ≠ o (U3 or U23): ≤ (r − 1)² + Σ_Q (e(Q) + 1)(Δr + 1)(2r − 3) ≤ (r − 1)² + (Δr + 1)(2r − 3)·r² ≤ 3Δ·r⁴.
Proof.
- (S1) A Ξ-change on R needs a switch on R. By A0, Ξ on R \ {o} is a function of σ at the vertices of the routes and of θ, c_θ, which
  are constant on the stretch. Ξ(o) = θ. Forced vertices and τ never move. The same holds for W, with w, c_w. (This is the fact that
  P-N5-NH-box42's Lemma SW (b), in review, states; it is not cited.)
- Before f0: ≤ r − 1 transitions.
- (a) LEN-Ξ.
- (b) LEN-W counts the W-changing transitions after f0: ≤ (r − 1)(r − 2). They leave ≤ (r − 1)(r − 2) + 1 W-flat segments. Each has
  ≤ r − 2 transitions with a switch on R:
  - A ROUTE-FORM STRETCH LIES IN ONE PIECE. On a stretch, R, θ, w are constant and c_θ is constant in the phase. By TC (i) (R22 (b)),
    H1 ⟺ λ_Ξ(o) ∈ F and H2 ⟺ τ(o) ∈ F, both constant on a crossing-free interval. c_w = o is decided by w. So the route form of each frame
    is constant on the stretch. With θ, w constant, a stretch with both frames in route form lies in one piece (R24 setting).
  - So a W-flat segment of it is part of a W-flat run of a piece, and R24 (c) CASC applies: no R-vertex switches at a run step ≥ r − 2,
    so ≤ r − 2 transitions with a switch.
  - With the honest frame not in route form, the stretch is a U2 stretch (¬H1, c_θ ≠ o, W in route form; R26 setting), and R26 (a)
    CASC-U2 gives the same.
  - With (S1), the Ξ-changing transitions on R are ≤ (r − 1) + (r − 1)(r − 2) + ((r − 1)(r − 2) + 1)(r − 2).
- (c) The same split. W-flat segments: ≤ (r − 1)(r − 2) + 1, each with ≤ (e(Q) + 1)(Δr + 1)(2r − 3) transitions with a switch on R
  (E-SEG (iii), (iv)).
  - Summing with Σ e(Q) ≤ r − 2 (E-SEG (v)): Σ_Q (e(Q) + 1) ≤ (r − 2) + (r − 1)(r − 2) + 1 ≤ r².
  - (Δr + 1)(2r − 3) ≤ 2Δr² for Δ ≥ 1. So the total is ≤ (r − 1)² + 2Δr⁴ ≤ 3Δr⁴.
- The case split is exhaustive: with c_w ≻ c_θ, the W frame is in route form (b) or not (c). □

## 7. Corollary KW-S (PROVED): (K_W), (E) and K per stretch
Let a stretch have f_st fallback transitions; it has ≤ f_st + 1 runs.
- (K_W) Its non-fallback transitions with a W-change on R number ≤ (f_st + 1)·(1 + (r − 1)² + (|F| − 1)) ≤ (f_st + 1)·n².
  - m* = c_w: LEN-W gives ≤ (r − 1)² per run.
  - m* = c_θ: by W-ONCE′, a W-changing transition of a run other than its first follows a Ξ-changing transition of the same run.
    Those are ≤ (r − 1)² on R (Theorem RUN (a)) plus ≤ |F| − 1 on F (F1°, on the crossing-free interval that contains the stretch).
- (E) Per W-flat run of a U3 / U23 stretch with c_w ≻ c_θ: polynomial, by E-SEG and KIND-MONO. When c_θ ⪰ c_w, (E) is not needed, since
  Theorem RUN (a) bounds the Ξ-changes on R directly.
- K (wakes, R27 (e)): every wake is a relevant transition, so K ≤ T_rel, which §8 bounds.
- R26's open items (E), (K_W) (limit (ii)) and ledger v2's K are therefore bounded given f (this packet; unrefereed until signed).

## 8. Corollary PHASE (PROVED, CONDITIONAL ON f ONLY) and the readings
Statement. Let a phase on 𝒞^1O have f fallback transitions. Then its transitions number T ≤ (m − n + 1)(T_rel + 1), where
- T_rel ≤ S_o + N_Ξ;
- N_Ξ ≤ f + (N_st − 1) + (X + 1)(n − 1) + (N_st + f)·3Δn⁴;
- N_st ≤ 1 + X + Θ + W_ch;
and, by landed results:
- X ≤ (f + 1)(n − 1) + f + X_SN, with X_SN ≤ 13(d_o + 1)n³(f + 1 + T_H) + T_H and T_H := n² + 2n − 1 (R30 (c) SN-PREFIX; R34 (e), (f));
- Θ ≤ (n − 1) + n(X + 1) + X if c_θ ≠ o, and Θ = 0 if c_θ = o (R27 (g) TH);
- S_o ≤ d_o(Θ + 1) (R27 (g) SO);
- W_ch ≤ (f + X + 1)·n² (per crossing-free interval I, by TC (i) one of three cases holds, and there are ≤ X + 1 intervals):
  - ¬H2, c_w ≠ o: ≤ (f_I + 1)(|R|² − 1) + f_I (R24 (e) WC);
  - H2: τ(o) ∈ F and w = o ⊕ W(τ(o)) = o ⊕ Ξ(τ(o)) (R19 (a), (V1)), so ≤ |F| − 1 w-changes (F1°);
  - c_w = o under ¬H2: w = (o, ∅, 0) is constant.
So T is bounded by an explicit polynomial in n, m and f. Writing it with f free:
- X = O(d_o·n³(f + n²));
- Θ = O(n·X);
- W_ch = O(n²(f + X));
- N_st = O(n²(f + X));
- N_Ξ = O(Δ·n⁶(f + X));
- T = O(m·Δ·n⁶·(f + X)) = O(m·Δ·d_o·n⁹·(f + n²)).
Proof.
1. Theorem LP (R27 (d)): T ≤ (m − n + 1)(T_rel + 1).
2. A relevant transition (R27 (a) setting) has a relevant Odd change of σ̄(o) (counted in S_o), or a relevant Even switch y: a → z.
   - In the second case λ(y) ≠ y, so Ξ_{k+1}(y) ▷ Ξ_k(y) by (SG) (R19 (d)), and the transition is Ξ-changing.
   - So T_rel ≤ S_o + N_Ξ.
3. Every transition of the phase is exactly one of: a fallback (≤ f), a stretch boundary (≤ N_st − 1), or a transition of a run of a
   stretch. Runs number ≤ N_st + f.
4. A Ξ-changing run transition changes Ξ on F, or on R.
   - On F: ≤ |F| − 1 per crossing-free interval (F1°), and there are ≤ X + 1 intervals.
   - On R: ≤ 3Δn⁴ per run (Theorem RUN).
5. Stretch boundaries change R, θ or w: N_st − 1 ≤ X + Θ + W_ch. The bounds on X, Θ, S_o, W_ch are the cited landed results. □
READING (not to sign).
- With FB-POLY (P-N5-FBPOLY, in review: f ≤ 1 + (n − 2)(2n − 1) per phase):
  - X = O(d_o·n⁵), N_st = O(d_o·n⁷), N_Ξ = O(Δ·d_o·n¹¹), T = O(m·Δ·d_o·n¹¹) per phase.
- With Corollary Φ-1O (P-N5-PHI, at CHECKER as R47: ≤ n(n − 1) + d phases) and SPEC's poly(n, m) bit cost per iteration, N5 on 𝒞^1O
  would make polynomially many iterations. This needs this packet, P-N5-FBPOLY and P-N5-PHI signed and landed.
- Until then NO polynomial bound for N5 is proved, and G-N5-TIME stays OPEN. The exponents are loose.

## 9. Weak points (READING; where a referee should push)
1. FRZ-U B2 / B3 use "x ∈ R_{k+1} has W cycle node c_w". This holds because R and w are constant on the stretch and A0 (W).
2. A0 under ¬H1 rests on "every Odd vertex but o is forced" and on C_Θ's two arcs being disjoint.
3. CASC-B's key step 4: pk is read from c_w backwards (R24 (b) TB-even), so the kind-B prefix is (A1 reversed, o) at each step.
4. CW-INT step 3: a c_w switch is strict in Ξ because S4a moves only along arena edges (R15 (d)).
5. Theorem RUN (b): "a route-form stretch lies in one piece" uses TC (i) on the crossing-free interval that contains the stretch.
6. Corollary PHASE step 3: runs are maximal non-fallback runs inside one stretch, so every transition is a run transition, a fallback,
   or a stretch boundary.
7. PAR makes the "c_w odd" branches of KIND-MONO and E-SEG vacuous. They are stated only in the B → A form.

## 10. DATA (DATA, not proof; experiments/si/kw15/kwcheck.py, kwclimb.py; REFEREE-2's SPEC-mode tracer read only; 𝒞^1O asserted)
- kwcheck checks per trace:
  - WONCE;
  - AGREE: Fact A's formulas above m*, both frames, at every state of every stretch;
  - FRZ: the freeze from k0 + |R| − 1;
  - LEN;
  - KIND: post-freeze, ≤ 1 change per vertex, direction B → A;
  - CWINT.
- Corpora, all with 0 failures:
  - every .pg in experiments/ and docs/ (500 𝒞^1O files, S3 + 2 random starts);
  - 3,000 random o-cyclic 𝒞^1O games, n 6-40;
  - 11 hill-climbs (fitness: long runs, Ξ-flat pairs, c_w ≻ c_θ ¬H2 runs; 4 seeded from L-NEW 21's 10 qualifying games);
  - L-NEW's 10 qualifying games × 150 random starts.
- Totals:
  - ≈ 13M AGREE states;
  - ≈ 4.7M freeze state checks (the largest observed freeze delay is 1 transition);
  - ≈ 0.85M W-ONCE checks;
  - ≈ 0.73M post-freeze runs with c_w ≻ c_θ, ¬H2, c_w ≠ o.
- VACUOUS IN DATA (the statements rest on their proofs):
  - KIND-MONO and CW-INT after the freeze: no post-freeze kind change and no post-freeze c_w switch was ever observed.
    - L-NEW 21's data (docs/new/N5-KW-box42.md §7: 820 kind-change transitions, 6 c_w switches) exercise DIR / CW BEFORE this packet's
      freeze index.
    - Pre-freeze transitions are counted wholesale (≤ r − 1 per run), so this packet does not need them.
  - Every c_w-odd branch: no state with c_w ≻ c_θ and c_w odd exists (PAR).
- Logs: experiments/si/kw15/logs/all_r2_c*.txt, random_3000.txt, climb_*.txt, qual10_r150.txt.

## 11. Independent lane proofs (referees may consult; neither is to sign)
- docs/si/N5-KW-box15.md (L-SI 10, sha1 5ebbb3b6): this packet's source.
- docs/new/N5-KW-box42.md v3.2 (L-NEW 21, l-new 31776c5c, sha1 349d553c): WLAG, ABOVE-h, CSTRICT, KW-FREEZE, Corollary KW, NR′, PAR,
  H-PATH, DIR, KC, CASC-B, CW, E-HI.
  - It reaches the same per-stretch conclusions by a different count of kinds (DIR + KC, no freeze).
  - Its per-phase assembly goes through P-N5-NH-box42 (in review).
- Cross-reads: notes/L-SI.md (l-si c6d70acf, c8186200) and L-NEW's notes/L-NEW.md (l-new 669624b2). Neither found a doubt of substance.
