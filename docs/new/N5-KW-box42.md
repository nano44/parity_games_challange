# N5 on 𝒞^1O, box 42 (2): W lags Ξ by one step (WLAG), and between events W freezes coarsely (KW-FREEZE), so (K_W) ⇐ (E*)
L-NEW successor 21 (Opus 5.5, D15/D18, L37/L40), session_01YJHHx1t8hvqkDnKzMU2Lfa. Working doc (not a packet; the Lead decides any
freeze). Started 20:05Z by date -u, at the Lead's request of 19:48Z (Lead's stamp): "(2) K, meaning (E) and (K_W), via the κ lens.
Repair κ-FREEZE-F's S4a length case, or find a different charging."
- Labels (D18/L40): PROVED (L-NEW succ. 21, unrefereed), CONJECTURE, OPEN, DATA, READING.
- Scope: the candidate N5 (SPEC docs/new/N5-ssi-global.md) on 𝒞^1O, inside one phase (λ_Ξ and τ constant). §1 holds on every game.
  Nothing here is a running-time bound for N5, a TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN.
- Answer to the Lead's ask, in one line: I did not repair κ-FREEZE-F. I found a different charging: R20's coarse freeze CR, run on
  G_τ with the two W-terminals o and c_w and restricted to class-respecting paths, freezes W coarsely on every event-free,
  fallback-free sub-run of ANY stretch. That bounds the W-changes on R by the events and fallbacks: (K_W) ⇐ (E*), where E* adds the
  honest-frame events (switches across c_θ) to R26's (E). The open core is now the events alone.

## Summary
| item | statement | label |
| --- | --- | --- |
| §1 Lemma WLAG | inside a phase, if k − 1 → k and k → k+1 are S4a steps and W_{k+1} ≠ W_k, then some y has z := σ_{k+1}(y) outside the arena H_{k−1}, and Ξ_k(z) ▷ Ξ_{k−1}(z) | PROVED (every game) |
| §2 Lemma CLS-CONST | on a sub-run (no fallback, no event) every class CLS(v) is constant | PROVED |
| §2 Lemma CSTRICT | same-class successors: a COARSE_h-strict W-comparison is an honest strict comparison with the same sign | PROVED |
| §3 Theorem KW-FREEZE | on a sub-run Σ: (a) COARSE_h(W) on R is constant from transition n − 1 of Σ on; (b) if c_θ ≻ c_w, the path set of Ξ on R is constant from there too; (c) Σ has ≤ n² − 1 transitions with a W-change on R | PROVED |
| §4 Corollary KW-E | a stretch S has K_S ≤ E*_S + (E*_S + f_S + 1)(n² − 1) | PROVED |
| §4 READING | with Theorem NH (P-N5-NH-box42): T per phase ≤ poly(n)·(1 + X + f + E*) | READING |
| §5 | (E*) per phase | OPEN |
| §6 | DATA | DATA |

## 0. Objects (as in docs/new/P-N5-NH-box42.md §0, which is frozen; restated where needed)
- Phase, R (o ∈ R), F, crossing, stretch (R, θ, w constant), π_v (v's σ-route before its first visit of o), H1, H2, c_θ := λ_Ξ(o),
  c_w := λ_W(o), (V1), ⊵, SPEC S4a (σ_{k+1} := the optimum of the arena H_k = {σ_k(y)} ∪ gate_k(y) in G_τ, SPEC tie-breaks), S4c, gate:
  (y, z) with Ξ_k(z) ▷ Ξ_k(σ_k(y)) (Iσ_k, SPEC S2; code si.py improving()).
- SPECIALS of a stretch: S := {c_θ, if ¬H1 and c_θ ≠ o} ∪ {c_w, if ¬H2 and c_w ≠ o}. These are the tops, inside R ∖ {o}, of the
  frames that are not in route form (Lemma SW step 3 of P-N5-NH-box42: under ¬H1 the honest cycle C_Ξ ⊆ R has top c_θ; under ¬H2,
  C_W ⊆ R has top c_w). S = ∅ on route-form pieces; S = {c_θ} on U2, {c_w} on U3, {c_θ, c_w} on U23 (possibly one vertex, U3-3).
- CLASS of v ∈ R ∖ {o}: CLS(v) := S ∩ π_v. On U3 this is R26's kind (A iff c_w ∈ CLS(v)).
- EVENT transition (of a stretch): some Even y ∈ R ∖ {o} switches (σ_{k+1}(y) ≠ σ_k(y)) and either y ∈ S or CLS_{k+1}(y) ≠ CLS_k(y).
  On U3 these are exactly R26 (c)'s events (a kind change of the switcher, or a switch of c_w). E*_S := #transitions of S containing an
  event; E* := Σ over the stretches of the phase.
- SUB-RUN: a maximal run of consecutive transitions of a stretch with no fallback and no event.
- W-TERMINAL of v ∈ R ∖ {o}: t(v) := c_w if c_w ∈ CLS(v), else o. Honest terminal: c_θ if c_θ ∈ CLS(v), else o.
- h := the more relevant of c_θ and c_w (they differ unless S is the single vertex c_θ = c_w of U3-3; then h := c_w).
  COARSE_h(c, P, ℓ) := (c, P ∩ ↑h), with ↑h the vertices strictly more relevant than h. COARSE_h is order-preserving on valuations with
  one cycle node: if a ⊴ b then COARSE_h(a) ⪯ COARSE_h(b) (the top of P_a Δ P_b decides both, or lies below h and COARSE_h ties).
- Signed results used: R15 (a) MONO; R17 (F1) (in G_τ); R19 (d) (SG); R20 (d) Lemma P^c / CR (P-N5-XA-box27.md §5, with
  P-N5-XA-fixes-box28.md); R23 WM (W never drops at S4a steps; on every game by R25's G-FB-3); RESULTS R22 (b) TC (i); and Lemma SW of
  docs/new/P-N5-NH-box42.md (in review: P-N5-NH-box42 sha1 93d19be8…; its proof is short and restated in §2 where used).

## 1. Lemma WLAG (PROVED, every game): W moves one step behind Ξ
Statement. Inside a phase let k − 1 → k and k → k+1 be S4a steps (no fallback) with W_{k+1} ≠ W_k. Then some Even y has
z := σ_{k+1}(y) ∉ H_{k−1}(y), and Ξ_k(z) ▷ Ξ_{k−1}(z). In particular Ξ_k ≠ Ξ_{k−1}: the transition k − 1 → k changes Ξ.
Proof.
1. τ is the same at k − 1, k, k+1. σ_k is the optimum of the arena H_{k−1} in the one-player game G_τ, and σ_{k+1} that of H_k (S4a).
2. If σ_{k+1}(y) ∈ H_{k−1}(y) for every Even y, then σ_{k+1} is a strategy of the arena H_{k−1}, so (F1) gives W_k ⊵ W_{k+1}
   pointwise. WM gives W_{k+1} ⊵ W_k. So W_{k+1} = W_k, against the hypothesis. Hence some y has z := σ_{k+1}(y) ∉ H_{k−1}(y).
3. z ∈ H_k(y) and z ≠ σ_{k−1}(y), z not a gate target of y at k − 1. Since σ_k(y) ∈ H_{k−1}(y) ∌ z, also z ≠ σ_k(y), so (y, z) is a
   gate edge at k: Ξ_k(z) ▷ Ξ_k(σ_k(y)).
4. Not a gate at k − 1: Ξ_{k−1}(z) ⊴ Ξ_{k−1}(σ_{k−1}(y)).
   - If σ_k(y) = σ_{k−1}(y) =: a: Ξ_k(z) ▷ Ξ_k(a) ⊵ Ξ_{k−1}(a) ⊵ Ξ_{k−1}(z) (MONO).
   - If σ_k(y) ≠ σ_{k−1}(y): σ_k(y) ∈ H_{k−1}(y) is then a gate target at k − 1, so Ξ_{k−1}(σ_k(y)) ▷ Ξ_{k−1}(σ_{k−1}(y)) ⊵ Ξ_{k−1}(z),
     and Ξ_k(z) ▷ Ξ_k(σ_k(y)) ⊵ Ξ_{k−1}(σ_k(y)) (MONO).
   Either way Ξ_k(z) ▷ Ξ_{k−1}(z). □
- Consequences.
  - On 𝒞^1O inside a stretch: z ∈ R if y ∈ R (R is constant), and z ∈ F if y ∈ F; in the second case k − 1 → k is an F-change, at most
    |F| − 1 of them per crossing-free interval (RESULTS R22 F1°).
  - Charging each W-changing S4a step k → k+1 to its predecessor k − 1 → k (an injective map): per phase, #(transitions with
    W_{k+1} ≠ W_k) ≤ #(Ξ-changing transitions) + 2f + 1 (the steps that follow a fallback or open the phase, and the fallbacks
    themselves). It explains the cascades (K-chain, box 33 §11): every W-change needs a fresh honest rise one step before. It bounds
    nothing alone: the honest rise can itself come from the W-change before it.
- DATA (experiments/new/box42/wlag.py): lib41 253 runs, 4,661 W-changing S4a steps after an S4a step, 0 violations (z ∈ R 2,609,
  z ∈ F 2,052); random 𝒞^1O n 6-16 with random starts (seed 4203): 98, 0 violations. kwprof.py: inside OTHER U2 / U3 / U23 stretches,
  121 / 121 such new edges have y, z ∈ R.

## 2. Classes on a sub-run (PROVED)
### Lemma CLS-CONST
Statement. On a sub-run Σ of a stretch, CLS(v) is constant for every v ∈ R ∖ {o}, and so is the W-terminal t(v).
Proof. Induction along Σ. At a transition k → k+1 of Σ let v ∈ R ∖ {o}. If no vertex of π_v^k switches, π_v^{k+1} = π_v^k. Otherwise
let y be the first vertex of π_v^k that switches. y ∉ S (no event), so π_v^{k+1} = (the part of π_v^k before y) · π_y^{k+1}, and
CLS_{k+1}(y) = CLS_k(y) (no event). The part before y is unchanged and contains the same specials. So CLS_{k+1}(v) = CLS_k(v). (R26's
U3-2, written for every class.) □
- Hence on Σ: CLS(σ(v)) = CLS(v) ∖ {v} for every Even v ∈ R ∖ {o} and every state of Σ.
### Values on a stretch (restating P-N5-NH-box42 Lemma SW, with the classes)
For v ∈ R ∖ {o} at a state of a stretch:
- W(v) = (c_w, P_w(p), |p|) if c_w ∈ CLS(v), where p is the part of π_v before c_w and P_w(p) its vertices more relevant than c_w;
  W(v) = π_v ⊕ w otherwise, and P(w) is disjoint from π_v (under H2, P(w) ⊆ {o} ∪ F; under ¬H2, P(w) = ∅).
- Ξ(v) = (c_θ, A_θ(p′), |p′|) if c_θ ∈ CLS(v), where p′ is the part of π_v before c_θ; Ξ(v) = π_v ⊕ θ otherwise (P(θ) ⊆ {o} ∪ F under
  H1, P(θ) = ∅ under ¬H1).
- Terminal values are constant on the stretch: W(o) = w, W(c_w) = (c_w, ∅, 0) (c_w ∈ S tops C_W ⊆ R), θ, (c_θ, ∅, 0).
### Lemma CSTRICT
Statement. Let k be a state of a sub-run, x an Even vertex of R ∖ {o} with x not a W-terminal, a := σ_k(x), and z ∈ R a successor of x
with CLS(z) = CLS(a) (z = t(x) allowed when a's class is empty and t(x) = o, or when z = c_w = t(x)). If COARSE_h(W_k(z)) ≻
COARSE_h(W_k(a)), then Ξ_k(z) ▷ Ξ_k(a): (x, z) is a gate edge at k.
Proof.
1. Same class: the routes π_z and π_a contain the same specials. If the class is empty, both end at o. Otherwise let s be the first
   special on π_z. Then s is also the first special on π_a: if the other special s′ came first on π_a, then s′ ∈ π_s and s ∈ π_{s′}
   would make the σ-routes of s and s′ a cycle avoiding o, which routes do not have. After s both routes are π_s.
2. Write q_z, q_a for the parts of π_z, π_a before s (the whole routes if the class is empty). The two routes are simple, so q_z, q_a
   are disjoint from the common rest. In each frame the two values have the same cycle node and terminal, and they differ only through
   q_z vs q_a: W through the vertices of q_z Δ q_a more relevant than c_w and through |q_z| − |q_a|; Ξ through those more relevant
   than c_θ and through the same length difference. (The terminal parts and P(w), P(θ) are common and disjoint from q_z ∪ q_a.)
3. COARSE_h-strict means: the top t of the W-difference (q_z Δ q_a) ∩ ↑c_w lies above h, and favours z (t ∈ q_z even, or t ∈ q_a odd).
   t ≻ h ⪰ c_θ, so t is in the honest difference. Any vertex u of the honest difference with u ≻ t is above h ⪰ c_w, so it is in the
   W-difference, against t being its top. So t also tops the honest difference and decides it the same way: Ξ_k(z) ▷ Ξ_k(a). □

## 3. Theorem KW-FREEZE (PROVED)
Statement. Let Σ = (k_0 → … → k_0 + L) be a sub-run of a stretch of a phase of N5 on 𝒞^1O. Then:
- (a) COARSE_h(W_t(v)) = COARSE_h(W_{k_0+n−1}(v)) for every v ∈ R and every state t of Σ with t ≥ k_0 + n − 1;
- (b) if c_θ ≻ c_w, then also the path set of Ξ_t(v) is constant on R for t ≥ k_0 + n − 1;
- (c) at most n² − 1 transitions of Σ change W at some vertex of R; precisely ≤ (n − 1) + |R|(n − 1) if c_w ≻ c_θ and
  ≤ (n − 1) + |R|(|R| − 2) if c_θ ≻ c_w.
Proof of (a): R20's CR on G_τ, on class-respecting paths.
1. Setting of CR (P-N5-XA §5): Ω := W (the valuation of G_τ), Ω^c := COARSE_h(W). On the stretch W's cycle node is c_w at every vertex
   of R (all R-plays end in o's W-play), and λ_Ξ = λ_W on F is fixed in the phase: W's cycle-node map is constant on Σ (CR's §1 fact).
   Every transition of Σ is an S4a step (no fallback), so CR's (B-fallback) case is not needed.
2. Class-respecting paths: for x ∈ R ∖ {o}, a simple path r = (x = r_0, …, r_L) of G_τ inside R with r_L = t(x), no earlier r_i a
   W-terminal, and CLS(r_{i+1}) = CLS(r_i) ∖ {r_i} for i < L. value(r) := r ⊕ W(t(x)) (the terminal value is constant on the stretch).
   Every current route (to its W-terminal) is class-respecting (Lemma CLS-CONST), and W_t(x) = value(current route).
3. Lemma P^c restricted to class-respecting r: for every j and every x, r with |r| ≤ j and k_0 + j ∈ Σ:
   Ω^c_{k_0+j}(x) ⪰ COARSE_h(value(r)). The proof is CR's, step by step:
   - Base (j = 0, r = (u), u a W-terminal): W(u) is constant (above).
   - Monotonicity of Ω^c (CR's "Lemma C" use): W is ⊵-non-decreasing at S4a steps (WM) and COARSE_h is order-preserving with one
     cycle node (§0). (V1c), (V2c), (Cmono) are properties of ⊕ and COARSE_h; r′ and σ_k(x)'s W-path avoid x.
   - Odd vertices of R ∖ {o} are forced: Ω^c_{k+1}(x) = x ⊕_c Ω^c_{k+1}(z) ⪰ x ⊕_c Ω^c_k(z), and the IH.
   - Case A_c (Ω^c_k(z) ⪯ Ω^c_k(σ_k(x))): CR's A1 verbatim. A2 (x its own W-cycle node) happens only for x = c_w, a W-terminal (base).
   - Case B_c (Ω^c_k(z) ≻ Ω^c_k(σ_k(x))): r is class-respecting, so CLS(z) = CLS(x) ∖ {x} = CLS(σ_k(x)) (Lemma CLS-CONST). Lemma CSTRICT
     replaces CR's (Cstrict): (x, z) is a gate edge, and it is W-improving. Then CR's (B-arena) verbatim: σ̂ := σ_k[x → z] is an arena
     strategy, (F1) gives Ω_{k+1}(x) ⊵ val_σ̂(x) in G_τ, and the sub-cases B1 (x ∉ π, off or on c_w's cycle C_W: (α) contradicts the
     constant W cycle-node map at k+1, which lies in Σ's stretch; (β) is the main case) and B2 (x ∈ π) are statements about G_τ and W
     only.
4. CR's closing step: every class-respecting r has ≤ n − 1 edges (simple). For t ≥ k_0 + n − 1 in Σ, W_t(x) = value(r_t) for x's
   current route r_t, so COARSE_h(value(r_t)) ⪯ Ω^c_{k_0+n−1}(x) ⪯ Ω^c_t(x) = COARSE_h(value(r_t)). Equality throughout. □
Proof of (b) (c_θ ≻ c_w, so h = c_θ). Induction on |CLS(v)|, using (a) for every vertex.
- CLS(v) = ∅: W(v) = π_v ⊕ w and Ξ(v) = π_v ⊕ θ. COARSE_h(W(v)) = (A_θ(π_v)) ⊔ (P(w) ∩ ↑c_θ), the second part constant. So A_θ(π_v),
  the honest path set minus the constant P(θ), is constant.
- c_θ ∈ CLS(v), c_θ first special on π_v (or the only one): Ξ(v)'s path set is A_θ(p′) with p′ the part before c_θ. W(v)'s path set
  restricted to ↑c_θ is A_θ(p′) ⊔ (W(c_θ)'s path set ∩ ↑c_θ) (π_v = p′ · π_{c_θ} up to the W-terminal, which is common). Both W-parts
  are frozen by (a), so A_θ(p′) is.
- c_w ∈ CLS(v), c_w first: the honest path continues past c_w. Its set is A_θ(p) ∪ ({c_w} ∩ ↑c_θ = ∅) ∪ (the honest path set of
  σ(c_w)) with p the part before c_w. A_θ(p) = COARSE_h part of W(v) (frozen by (a)); σ(c_w) is constant on Σ (c_w ∈ S does not
  switch) and |CLS(σ(c_w))| < |CLS(v)|: frozen by induction. □
Proof of (c).
- Transitions before k_0 + n − 1: at most n − 1.
- c_w ≻ c_θ (h = c_w): after k_0 + n − 1, COARSE_h(W(v)) = (c_w, P(W(v))) (every vertex of a path set is above the cycle node), so
  W(v) moves only through its length, ⊵-monotonically (WM). That length is |p| (c_w ∈ CLS(v)) or |π_v| + ℓ(w) with ℓ(w) constant, and
  |p|, |π_v| ∈ [1, |R| − 1]: at most |R| − 2 ≤ n − 1 changes per vertex. So ≤ |R|(n − 1) transitions with a W-change on R.
- c_θ ≻ c_w (h = c_θ): after k_0 + n − 1, a transition with a W-change on R has a switch of some Even y ∈ R ∖ {o} (Lemma SW (b),
  P-N5-NH-box42). y's honest value is (c_θ, frozen set by (b), length of y's honest path to its honest terminal, plus a constant).
  λ_Ξ(y) = c_θ ≠ y, so (SG) makes Ξ(y) rise strictly at each switch of y; with the set frozen and the terminal value constant, Ξ(y)
  then moves only through that length, monotonically in the direction fixed by c_θ's parity (MONO). The length lies in [1, |R| − 1]:
  ≤ |R| − 2 switches of y. So ≤ |R|(|R| − 2) such transitions.
- Both are ≤ (n − 1) + n(n − 1) = n² − 1. □

## 4. Corollary KW-E (PROVED) and the reduction (READING)
Corollary KW-E. A stretch S with f_S fallback transitions and E*_S event transitions has
    K_S ≤ E*_S + (E*_S + f_S + 1)(n² − 1)
non-fallback transitions with a W-change on R.
Proof. The fallback and event transitions cut S into ≤ E*_S + f_S + 1 sub-runs. A non-fallback W-changing transition is an event
transition (≤ E*_S) or lies in a sub-run (Theorem KW-FREEZE (c)). □
- Remark. On route-form pieces S = ∅, there are no events, and KW-E gives K ≤ (f + 1)(n² − 1): a second proof of the order of R24
  Theorem U1's K (which is ≤ (f + 1)(|R| − 1)(|R| − 2) there).
READING (not to sign). Theorem NH (P-N5-NH-box42 (b), (c)) with K_W ≤ Σ_S K_S ≤ E* + (E* + f + #stretches)(n² − 1) and E ≤ E* (R26's
events are E*-events: on U3 / U23, c_w ∈ S) gives, per phase,
    O and T ≤ poly(n)·(1 + X + f + E*),
using #stretches ≤ N ≤ n²(2X + 2 + f^O) (P-N5-NH-box42 STR-COUNT). With P-N5-FX and P-N5-FBPOLY (in review), X and f are polynomial,
so on 𝒞^1O: T per phase is polynomial if (E*) is. With P-N5-PHI (in review) the phase count is polynomial. So along this route the
whole open core of G-N5-TIME on 𝒞^1O is (E*): event transitions per phase.

## 5. (E*) (OPEN)
- (E*) := the number of transitions per phase containing an event: a switch of a special vertex (c_θ under ¬H1, c_w under ¬H2, when
  they are not o), or a switch that moves the switching vertex's route across a special (CLS changes).
- What is known: R26 left (E) open; nothing bounds E* yet. K-chain (box 33 §11) has K linear in n with few events.
- First observations (DATA, §6): E* per stretch ≤ 34 on the library, ≤ 2 on random runs.
- Plan (next): (i) characterise events with WLAG / KW-FREEZE: an event at a sub-run's end is an S4a switch whose new target is of
  another class, so it is a gate edge whose W-value beats the current one; does COARSE_h(W) rise strictly at an event (so events are
  charged to coarse rises, which are monotone between fallbacks)? (ii) data on the instance with E* = 34; (iii) climbs for E*.

## 6. DATA (experiments/new/box42/; one Odd choice vertex asserted, other files skipped)
- kwfreeze.py checks Lemma CLS-CONST, Theorem KW-FREEZE (a), (b), (c) and Corollary KW-E on every stretch of every phase:
  - lib41 (253 runs): 5,058 stretches with S = ∅, 293 with |S| = 1, 40 with |S| = 2; 5,532 sub-runs; violations 0; latest coarse
    change at sub-run index 20; max W-changing transitions in a sub-run 21; max E*_S 34; ΣK_S 498, ΣE* 130.
  - random 𝒞^1O n 6-16, random starts (seed 4204, 2,605 runs): 7,514 sub-runs, violations 0 (max E*_S 2).
- wlag.py (Lemma WLAG): see §1. kwprof.py: profile of K_W transitions in OTHER stretches (§1).
