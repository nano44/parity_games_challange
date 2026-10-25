# N5 on 𝒞^1O, box 42 (2): W lags Ξ by one step (WLAG); on every fallback-free run of a stretch both frames freeze coarsely (KW-FREEZE), so (K_W) holds given f, and (E) is needed only on U3 / U23 stretches with c_w even and above c_θ
L-NEW successor 21 (Opus 5.5, D15/D18, L37/L40), session_01YJHHx1t8hvqkDnKzMU2Lfa. Working doc (not a packet; the Lead decides any
freeze). Started 20:05Z by date -u, at the Lead's request of 19:48Z (Lead's stamp): "(2) K, meaning (E) and (K_W), via the κ lens.
Repair κ-FREEZE-F's S4a length case, or find a different charging." Version 2, 20:3xZ: the first version (l-new 0c0d439e, sha1
1889d56f…) needed event-free sub-runs; this version proves CSTRICT for every pair of successors, so events are not needed for the
freeze. It supersedes version 1 where they differ.
- Labels (D18/L40): PROVED (L-NEW succ. 21, unrefereed), CONJECTURE, OPEN, DATA, READING.
- Scope: the candidate N5 (SPEC docs/new/N5-ssi-global.md) on 𝒞^1O, inside one phase (λ_Ξ and τ constant). §1 holds on every game.
  Nothing here is a running-time bound for N5, a TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN.
- Answer to the Lead's ask, in one line: κ-FREEZE-F is not repaired. A different charging closes (K_W) given f. RESULTS R20's coarse
  freeze CR is run on G_τ with threshold h := the more relevant of c_θ and c_w. Both frames agree above h on every pair of R-routes,
  because they differ only on the cycles C_Ξ and C_W, which lie at or below h. So W and Ξ freeze coarsely on every fallback-free run
  of a stretch. The events (E) remain needed only on U3 / U23 stretches with c_w even and strictly above c_θ.

## Summary
| item | statement | label |
| --- | --- | --- |
| §1 Lemma WLAG | inside a phase, if k − 1 → k and k → k+1 are S4a steps and W_{k+1} ≠ W_k, then some y has z := σ_{k+1}(y) outside the arena H_{k−1}, and Ξ_k(z) ▷ Ξ_{k−1}(z) | PROVED (every game) |
| §2 Lemma ABOVE-h | on a stretch, for v ∈ R: W(v)'s and Ξ(v)'s path sets above h are π_v ∩ ↑h plus a constant set | PROVED |
| §2 Lemma CSTRICT | on a stretch, for x ∈ R ∖ {o} and successors z, a ∈ R: a COARSE_h-strict W-comparison is an honest strict comparison with the same sign | PROVED |
| §3 Theorem KW-FREEZE | on a fallback-free run ϱ of a stretch: (a) COARSE_h(W) and COARSE_h(Ξ) on R are constant from transition n − 1 of ϱ on; (b) ≤ n + 2n·\|R\| + N_F(ϱ) transitions of ϱ change W on R (N_F(ϱ): transitions of ϱ with a Ξ-change on F; the N_F term only if c_θ ≻ c_w); (c) if c_θ ⪰ c_w, ≤ (n − 1) + 2n·\|R\| change Ξ on R; (d) if c_w ≻ c_θ and c_w is odd, ≤ (n − 1) + 2n(m + n) + #(c_w-switches) change Ξ on R | PROVED |
| §4 Corollary KW | every stretch S has K_S ≤ (f_S + 1)(n + 2n\|R\|) + N_F(S) ≤ 3n²(f_S + 1) + n; so (K_W) per phase ≤ 3n²(f + #stretches) + n(X + 1) | PROVED |
| §4 Corollary NR′ | Ξ-changes on R per stretch, without K_W or E, except U3 / U23 with c_w even and c_w ≻ c_θ | PROVED |
| §4 READING | with Theorem NH (P-N5-NH-box42): O and T per phase ≤ poly(n)·(1 + X + f + E_even) | READING |
| §5 | (E_even): events in U3 / U23 stretches with c_w even, c_w ≻ c_θ | OPEN |
| §6 | DATA | DATA |

## 0. Objects (as in docs/new/P-N5-NH-box42.md §0, frozen; restated where needed)
- Phase, R (o ∈ R), F, crossing, stretch (R, θ, w constant), π_v (v's σ-route before its first visit of o; π_o := ∅), H1, H2,
  c_θ := λ_Ξ(o), c_w := λ_W(o), (V1), ⊵. SPEC S4a: σ_{k+1} := the optimum of the arena H_k = {σ_k(y)} ∪ gate_k(y) in G_τ, with SPEC
  tie-breaks. Gate: (y, z) with Ξ_k(z) ▷ Ξ_k(σ_k(y)) (Iσ_k, SPEC S2; code si.py improving()).
- On a stretch: every vertex of R has W cycle node c_w and honest cycle node c_θ (all R-plays continue with o's play).
  - Under ¬H1, o lies on its honest cycle C_Ξ ⊆ R, whose top is c_θ. Under ¬H2, o lies on its W-cycle C_W ⊆ R, whose top is c_w
    (P-N5-NH-box42 Lemma SW, step 3).
  - Under H1, o's honest play enters F and stays there; under H2, o's W-play does (TC (i)).
- h := the more relevant of c_θ and c_w (h := c_θ if they are equal). ↑h := the vertices strictly more relevant than h.
  COARSE_h(c, P, ℓ) := (c, P ∩ ↑h). With one cycle node c, COARSE_h is order-preserving: if a ⊴ b, then COARSE_h(a) ⪯ COARSE_h(b)
  (the top of P_a Δ P_b decides both orders, or it lies at or below h and COARSE_h ties).
- A RUN of a stretch: a maximal run of consecutive transitions of the stretch with no fallback. Its transitions are S4a steps.
- Classes, for §5: specials S := {c_θ, if ¬H1 and c_θ ≠ o} ∪ {c_w, if ¬H2 and c_w ≠ o}; CLS(v) := S ∩ π_v. An EVENT transition has a
  switching Even y ∈ R ∖ {o} with y ∈ S or CLS(y) changed. On U3 these are RESULTS R26 (c)'s events.
- Signed results used: R15 (a) MONO; R17 (F1) (in G_τ); R19 (d) (SG); R20 (d) Lemma P^c / CR (docs/new/P-N5-XA-box27.md §5, with
  docs/new/P-N5-XA-fixes-box28.md); R23 WM (W never drops at S4a steps; on every game by R25's G-FB-3); R24 (b) Lemma TB (any game);
  R22 (b) TC (i). Lemma SW of docs/new/P-N5-NH-box42.md (in review, sha1 93d19be8…): on a stretch Ξ and W on R are functions of the
  routes and θ, w; a change of Ξ or W on R needs a switch of an Even vertex of R.

## 1. Lemma WLAG (PROVED, every game): W moves one step behind Ξ
Statement. Inside a phase let k − 1 → k and k → k+1 be S4a steps (no fallback) with W_{k+1} ≠ W_k. Then some Even y has
z := σ_{k+1}(y) ∉ H_{k−1}(y), and Ξ_k(z) ▷ Ξ_{k−1}(z). In particular the transition k − 1 → k changes Ξ.
Proof.
1. τ is the same at k − 1, k and k+1. σ_k is the optimum of the arena H_{k−1} in the one-player game G_τ, and σ_{k+1} is that of H_k
   (S4a).
2. If σ_{k+1}(y) ∈ H_{k−1}(y) for every Even y, then σ_{k+1} is a strategy of the arena H_{k−1}, so (F1) gives W_k ⊵ W_{k+1}
   pointwise. WM gives W_{k+1} ⊵ W_k. So W_{k+1} = W_k, against the hypothesis. Hence some y has z := σ_{k+1}(y) ∉ H_{k−1}(y).
3. z ∈ H_k(y). σ_k(y) ∈ H_{k−1}(y) and z ∉ H_{k−1}(y), so z ≠ σ_k(y), and (y, z) is a gate edge at k: Ξ_k(z) ▷ Ξ_k(σ_k(y)).
4. z ∉ H_{k−1}(y): z ≠ σ_{k−1}(y) and Ξ_{k−1}(z) ⊴ Ξ_{k−1}(σ_{k−1}(y)).
   - If σ_k(y) = σ_{k−1}(y) =: a: Ξ_k(z) ▷ Ξ_k(a) ⊵ Ξ_{k−1}(a) ⊵ Ξ_{k−1}(z) (MONO).
   - Otherwise σ_k(y) ∈ H_{k−1}(y) is a gate target at k − 1: Ξ_{k−1}(σ_k(y)) ▷ Ξ_{k−1}(σ_{k−1}(y)) ⊵ Ξ_{k−1}(z), and
     Ξ_k(z) ▷ Ξ_k(σ_k(y)) ⊵ Ξ_{k−1}(σ_k(y)) (MONO).
   Either way Ξ_k(z) ▷ Ξ_{k−1}(z). □
- Consequence. Charge each W-changing S4a step k → k+1 to its predecessor k − 1 → k (an injective map). Per phase:
  #(transitions with W_{k+1} ≠ W_k) ≤ #(Ξ-changing transitions) + 2f + 1. These are the steps that follow a fallback or open the
  phase, and the fallbacks themselves. This explains the cascades (K-chain, docs/new/N5-K-box33.md §11): every W-change needs a fresh
  honest rise one step before. It bounds nothing alone. §3 is the bound.
- DATA (experiments/new/box42/wlag.py): lib41 253 runs, 4,661 W-changing S4a steps after an S4a step, 0 violations (z ∈ R 2,609,
  z ∈ F 2,052); random 𝒞^1O n 6-16 with random starts (seed 4203): 98, 0 violations.

## 2. The two frames agree above h (PROVED)
### Lemma ABOVE-h
Statement. On a stretch there are constant sets K_W, K_Ξ ⊆ ↑h (K_W := P(w) ∩ ↑h under H2, ∅ under ¬H2; K_Ξ := P(θ) ∩ ↑h under H1,
∅ under ¬H1) such that for every v ∈ R:
    P(W(v)) ∩ ↑h = (π_v ∩ ↑h) ⊔ K_W   and   P(Ξ(v)) ∩ ↑h = (π_v ∩ ↑h) ⊔ K_Ξ.
Proof. W frame; the honest frame is the same with θ, c_θ, H1, C_Ξ.
- H2: v's W-play is π_v, then o's W-play, which enters F and never meets π_v. o is not its own W-cycle node, so iterating (V1) gives
  W(v) = π_v ⊕ w. Every vertex of π_v ∩ ↑h is above c_w, so P(W(v)) = (π_v ∩ ↑c_w) ⊔ P(w). Intersect with ↑h (h ⪰ c_w).
- ¬H2, c_w ∉ π_v: v's W-path to c_w is π_v, then o's path to c_w along C_W. The C_W vertices are ⪯ c_w ⪯ h. So
  P(W(v)) ∩ ↑h = π_v ∩ ↑h.
- ¬H2, c_w ∈ π_v: the W-path is the part p of π_v before c_w. The rest of π_v is c_w and then c_w's σ-route to o, an arc of C_W
  (c_w's route follows C_W back to o), all ⪯ c_w ⪯ h. So π_v ∩ ↑h = p ∩ ↑h = P(W(v)) ∩ ↑h.
- v = o: π_o = ∅ and P(w) ∩ ↑h = K_W (under ¬H2, w = (c_w, ∅, d), so P(w) = ∅). □
### Lemma CSTRICT
Statement. At a state of a stretch, let x ∈ R ∖ {o} be Even, a := σ(x), and z ∈ R another successor of x. If COARSE_h(W(z)) ≻
COARSE_h(W(a)), then Ξ(z) ▷ Ξ(a). So (x, z) is a gate edge, and it is W-improving.
Proof.
1. W(z) and W(a) have the same cycle node c_w. By ABOVE-h, P(W(z)) ∩ ↑h and P(W(a)) ∩ ↑h differ exactly by D := (π_z Δ π_a) ∩ ↑h.
   COARSE_h-strictness says D ≠ ∅ and its top t favours z: t ∈ π_z with t even, or t ∈ π_a with t odd.
2. Ξ(z) and Ξ(a) have the same cycle node c_θ. Their path sets differ by a set D′ whose part in ↑h is again D (ABOVE-h). Every vertex
   of D′ ∖ D is ⪯ h ≺ t. So t is the top of D′, and it decides the honest comparison the same way: Ξ(z) ▷ Ξ(a). □
- This is RESULTS R22's (R3) and R24's swapped (R3) without the route-form hypothesis. Outside route form the two frames differ only
  on C_Ξ ∪ C_W, which lies at or below h.

## 3. Theorem KW-FREEZE (PROVED)
Statement. Let ϱ = (k_0 → … → k_0 + L) be a run (no fallback) of a stretch of a phase of N5 on 𝒞^1O. Then:
- (a) for every v ∈ R and every state t ≥ k_0 + n − 1 of ϱ: COARSE_h(W_t(v)) = COARSE_h(W_{k_0+n−1}(v)) and
  COARSE_h(Ξ_t(v)) = COARSE_h(Ξ_{k_0+n−1}(v));
- (b) at most (n − 1) + 2n|R| transitions of ϱ change W at some vertex of R if c_w ⪰ c_θ, and at most n + 2n|R| + N_F(ϱ) if
  c_θ ≻ c_w, where N_F(ϱ) counts the transitions of ϱ with a Ξ-change at some vertex of F;
- (c) if c_θ ⪰ c_w, at most (n − 1) + 2n|R| transitions of ϱ change Ξ at some vertex of R;
- (d) if c_w ≻ c_θ and c_w has odd priority, at most (n − 1) + 2n(m + n) + #(switches of c_w in ϱ) transitions of ϱ change Ξ at some
  vertex of R (m = #edges); under H2 c_w ∈ F does not switch on R's account and the last term is dropped (see the proof).
Proof of (a): R20's CR on G_τ, with COARSE_h and Lemma CSTRICT.
1. CR's setting (P-N5-XA-box27 §5): Ω := W, the valuation of G_τ; Ω^c := COARSE_h(W). W's cycle-node map is constant on ϱ: c_w on R,
   and λ_W = λ_Ξ on F, which is fixed in the phase. Every transition of ϱ is an S4a step, so CR's (B-fallback) case does not arise.
2. Paths. W-TERMINALS: o, with the constant value w, and, under ¬H2 with c_w ≠ o, the vertex c_w, with the constant value (c_w, ∅, 0).
   For x ∈ R ∖ {o}, an ADMISSIBLE path is a simple path r = (x = r_0, …, r_L) of G_τ inside R with r_L a W-terminal and no earlier
   r_i a W-terminal; value(r) := r ⊕ W(r_L), by iterated ⊕ ((V1) algebra). x's current W-play up to its first W-terminal is
   admissible, and W_t(x) = value(that path) (ABOVE-h's case analysis: π_x ⊕ w, or the part before c_w ⊕ (c_w, ∅, 0)).
3. Lemma P^c, restricted to admissible paths: for every j, every x ∈ R ∖ {o} and every admissible r from x with |r| ≤ j and
   k_0 + j ∈ ϱ, Ω^c_{k_0+j}(x) ⪰ COARSE_h(value(r)). The proof is CR's induction on j, step by step:
   - Base: r = (u) with u a W-terminal; W(u) is constant on the stretch.
   - Monotonicity of Ω^c (CR's use of Lemma C): WM and COARSE_h order-preserving (§0).
   - (V1c), (V2c), (Cmono): x ⊕_c is monotone on COARSE_h-values whenever x lies in neither path set above h. If x ⪯ h, x ⊕ does not
     touch the part above h. If x ≻ h, then x ∉ C_Ξ ∪ C_W, so x is not in P(w) or P(θ). x ∉ r′ (r is simple), and x ∉ σ_k(x)'s W-play
     (x is not its own W-cycle node: the only one in R is c_w, a W-terminal).
   - Odd vertices of R ∖ {o} are forced: Ω^c_{k+1}(x) = x ⊕_c Ω^c_{k+1}(z) ⪰ x ⊕_c Ω^c_k(z), then the IH.
   - Case A_c (Ω^c_k(z) ⪯ Ω^c_k(σ_k(x))): CR's A1 verbatim. A2 (x its own W-cycle node) is only x = c_w, a W-terminal (base case).
   - Case B_c (Ω^c_k(z) ≻ Ω^c_k(σ_k(x))): z ∈ R (r lies in R). Lemma CSTRICT replaces CR's (Cstrict): (x, z) is a gate edge and
     W-improving. Then CR's (B-arena) verbatim. σ̂ := σ_k[x → z] is an arena strategy, and (F1) gives Ω_{k+1}(x) ⊵ val_σ̂(x) in G_τ.
     Sub-cases:
     - B1, x not on c_w's cycle: the main case.
     - B1, x on C_W: (α) contradicts the constant W cycle-node map at k+1 (k+1 is a state of the stretch); (β) is the main case.
     - B2, x on z's W-path.
     All three are statements about G_τ and W only.
4. CR's closing step. An admissible path is simple, so it has ≤ n − 1 edges. For t ≥ k_0 + n − 1 in ϱ:
   COARSE_h(value(r_t)) ⪯ Ω^c_{k_0+n−1}(x) ⪯ Ω^c_t(x) = COARSE_h(value(r_t)), where r_t is x's current admissible path. Equality
   throughout. For v = o, W(o) = w is constant.
5. The honest half. By ABOVE-h, COARSE_h(Ξ(v)) = (c_θ, (π_v ∩ ↑h) ⊔ K_Ξ). COARSE_h(W(v)) = (c_w, (π_v ∩ ↑h) ⊔ K_W) determines
   π_v ∩ ↑h, because K_W is constant and disjoint from π_v. So COARSE_h(Ξ(v)) is constant whenever COARSE_h(W(v)) is. □
Proof of (b), (c), (d). Count from state k_0 + n − 1 on; the first n − 1 transitions give the (n − 1) term.
- Length ranges. W(v)'s length is that of v's W-path to c_w: |π_v| + ℓ(w) or |p|. With ℓ(w) ≤ n − 1 constant, it lies in an
  interval of fewer than 2n integers. The same holds for Ξ(v) with ℓ(θ).
- (b) If c_w ⪰ c_θ (h = c_w), every vertex of P(W(v)) is above c_w, so by (a) the whole of P(W(v)) is constant. W(v) is
  ⊵-non-decreasing at S4a steps (WM), so its length moves monotonically: < 2n changes per vertex, ≤ 2n|R| transitions.
  If c_θ ≻ c_w, use Lemma WLAG: every W-changing transition k → k+1 of ϱ other than the first has its predecessor k − 1 → k in ϱ,
  and that predecessor changes Ξ (on R or on F). Distinct W-changing transitions have distinct predecessors. So the W-changing
  transitions number ≤ 1 + #(Ξ-changing transitions of ϱ) ≤ 1 + ((n − 1) + 2n|R|) + N_F(ϱ), by (c).
- (c) If c_θ ⪰ c_w (h = c_θ), every vertex of P(Ξ(v)) is above c_θ, so by (a) P(Ξ(v)) is constant. Ξ(v) is ⊵-non-decreasing (MONO),
  so its length moves monotonically: < 2n changes per vertex. A transition that changes Ξ on R changes it at some vertex:
  ≤ 2n|R| transitions. (Switches of c_θ itself, an own honest cycle node under ¬H1, change no honest value on R: honest paths to
  c_θ never use c_θ's return arc. So they need no count here.)
- (d) c_w ≻ c_θ, c_w odd. Let y ∈ R ∖ {o} be Even with y ≠ c_w; y is not its own W-cycle node (the only one in R is c_w). By R24
  Lemma TB (TB-odd), every switch of y at which W(y) is unchanged lowers σ(y)'s index strictly. W(y) changes < 2n times on ϱ after
  state k_0 + n − 1 ((b)'s argument, h = c_w). Between two changes of W(y), y switches ≤ deg(y) − 1 times. So y switches
  ≤ 2n·deg(y) + 2n times; summed over y, ≤ 2n(m + n) switches. A Ξ-change on R needs a switch of an Even vertex of R (Lemma SW).
  - y = c_w: c_w is its own W-cycle node, so TB does not apply to it. Under ¬H2, c_w ∈ R; its switches keep W(c_w) = (c_w, ∅, 0) and
    re-route C_W's return arc A2 below c_w, which lies on no W-path to c_w, so they change no W-value on R; they can change Ξ on R
    (kind-A routes run through A2). They are counted separately: the term #(switches of c_w in ϱ). Under H2, c_w ∈ F is not in R and
    is not counted. □

## 4. Corollaries (PROVED) and the reduction (READING)
Corollary KW. Let a stretch S have f_S fallback transitions. Then
    K_S ≤ (f_S + 1)(n + 2n|R|) + N_F(S) ≤ 3n²(f_S + 1) + n
non-fallback transitions change W on R (N_F(S): transitions of S with a Ξ-change on F, ≤ |F| − 1 by RESULTS R22 F1°). Per phase:
K_W ≤ 3n²(f + #stretches) + n(X + 1), with #stretches ≤ n²(2X + 2 + f^O) (P-N5-NH-box42 STR-COUNT (d)).
Proof. S has ≤ f_S + 1 runs; apply Theorem KW-FREEZE (b) to each, and sum N_F over the runs of one crossing-free interval (F1°). □
- So (K_W) holds given f and X. Both are polynomial by P-N5-FBPOLY and P-N5-FX (in review).
Corollary NR′. Let S be a stretch with f_S fallbacks, and N_R(S) the transitions of S with a Ξ-change on R.
- If c_θ ⪰ c_w (P3′; U2, U3, U23 with c_θ ⪰ c_w): N_R(S) ≤ f_S + (f_S + 1)((n − 1) + 2n|R|).
- If c_w ≻ c_θ and c_w is odd: N_R(S) ≤ f_S + (f_S + 1)((n − 1) + 2n(m + n)) + #(c_w-switches in S).
  - Under H2 (U1, U2): the last term is 0.
  - Under ¬H2 (U3, U23): c_w-switches are R26 events; their number is OPEN.
- U1: RESULTS R24 Theorem U1 (given f). U2: RESULTS R26 (b), with K_S from Corollary KW.
- Left: U3 and U23 with c_w ≻ c_θ: by RESULTS R26 (d), with K_S from Corollary KW and E_S. E_S is needed when c_w is even; when c_w
  is odd, only the c_w-switches are.
READING (not to sign). Feed Corollaries KW and NR′ into Theorem NH (P-N5-NH-box42 (a): Lemma NR's per-class bounds replaced by NR′
where sharper). Then O and T per phase are ≤ poly(n)·(1 + X + f + E_hi), where E_hi := the event transitions of U3 / U23 stretches
with c_w ≻ c_θ. With P-N5-FX, P-N5-FBPOLY and P-N5-PHI (in review), N5 on 𝒞^1O is polynomial if E_hi is polynomial per phase. For c_w
odd only the c_w-switches count. So along this route the open core of G-N5-TIME on 𝒞^1O is:
- (E_hi): kind changes (across c_w) and c_w-switches in U3 / U23 stretches with c_w ≻ c_θ, for c_w even;
- plus c_w-switches alone, for c_w odd.

## 5. (E_hi) (OPEN)
- Where it lives. U3 / U23 stretches with c_w ≻ c_θ. After the freeze (KW-FREEZE (a)), W moves only through lengths (< 2n|R|
  W-changing transitions per run). What remains are W-flat runs: switches at W-ties.
  - CASC-U3 (RESULTS R26 (c)) bounds a W-flat run between events.
  - Events are W-tie switches across c_w (a kind change at equal W-value: same set above c_w, same length to c_w), or c_w's own
    re-routings of A2.
- What is known. TB-odd kills W-tie cycling at non-cycle-node vertices when c_w is odd. For c_w even (BFS mode, where the K-chain
  lives), TB-even's lexicographic key is the only potential, and it needs W unchanged along the whole old play.
- Next. (i) A W-tie kind change at y keeps W(y) and lowers pk(y) (TB-even), if W is unchanged along y's old play. Is the number of
  kind changes per W-flat run ≤ |R|? (ii) c_w-switches: each re-routes A2 at a W-tie of c_w. Are they bounded by the honest
  rises on A2 (WLAG-type)? (iii) Data: where the library's E* = 34 sits (c_w parity, c_w vs c_θ).

## 6. DATA (experiments/new/box42/; one Odd choice vertex asserted, other files skipped)
- kwfreeze2.py (version 2 statements). It checks:
  - Lemma CSTRICT at every state of every stretch, for every Even x ∈ R ∖ {o} and every pair of successors in R;
  - Theorem KW-FREEZE (a) for W and Ξ, from run index n − 1;
  - (b) on every run;
  - (c) when c_θ ≻ c_w.
  Results:
  - lib41 (253 runs): 424 fallback-free runs, 1,061 COARSE_h-strict cases, all honest-strict. Violations 0. Latest coarse change at
    0.83·(n − 1) into a run (the n − 1 index is nearly reached). Max W-changing transitions in a run: 40.
  - Random 𝒞^1O n 6-16, random starts (seed 4205, 2,561 runs): 480 runs, 923 strict cases. Violations 0.
- kwfreeze.py (version 1, event-free sub-runs; kept). lib41: 5,532 sub-runs, violations 0, max E*_S 34. Random (seed 4204): 7,514
  sub-runs, violations 0.
- wlag.py (Lemma WLAG): §1. kwprof.py: inside OTHER U2 / U3 / U23 stretches, 121 / 121 W-changes after an in-stretch S4a step have
  their new edge inside R, with an honest rise at its head one step earlier.
