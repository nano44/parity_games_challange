# N5 on 𝒞^1O, box 41: in-phase Even fallbacks per phase are polynomial, ≤ 1 + (|U| − 2)(deg_U(o) + |U|), with no hypothesis on H1, H2, H3, τ(o), c_w, θ or N_HN (Theorem FB-POLY); FB-CAP holds at |U| ≤ 2
L-NEW successor 20 (Opus 5.5, D15/D18), session_018pjn8Y8JRES3YuFDUCAJgM. Working doc (not a packet), written 2026-10-25 18:2xZ-18:4xZ
(date -u), box 41 item (1) (Lead GO 18:15Z, Lead's stamp: "FB-CAP proof, as in your notebook ... If it fails, record the exact
obstruction"). Source of the route: docs/new/N5-FBCAP-route-box40.md (successor 19). This doc supersedes its §2 (i)-(vi) case split.
- Labels (D18/L40): PROVED (L-NEW succ. 20, unrefereed; full proofs below), CONJECTURE, OPEN, DATA.
- Scope: the candidate N5 (SPEC S1-S5, docs/new/N5-ssi-global.md) on 𝒞^1O, inside one phase. Nothing here is a running-time bound for
  N5, a TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN (crossings X, θ-changes before the freeze, S4a steps, phases remain).
- Result in one line: FB-CAP's bound max(1, |U| − 2) is NOT proved for |U| ≥ 3 (it stays L-RED's CONJECTURE); a polynomial bound with
  the same mechanism IS proved, and FB-CAP itself is proved for |U| ≤ 2.

## 0. Notation and the facts used
- Objects as in docs/new/P-N5-RHO-box40.md §0 (= P-N5-PFZ §0 = RESULTS R39's setting): phase, θ = Ξ(o), c_θ, U := λ^{-1}(c_θ),
  Û := U ∖ {o}, R_k, R̄_k, F_k, wt, s_θ, G_Û, honest frame Ξ_k (against σ̄_k), next_k, g_1 < g_2 < … the in-phase Even S4c fallbacks of
  the phase, θ-run. NEW: T := {o, c_θ} (the terminals); deg_U(o) := |succ(o) ∩ U|; for an in-phase Even fallback k → k+1, S_k := the
  set of Even vertices that switch, x*_v := σ_{k+1}(v) for v ∈ S_k, and S_U := S_k ∩ (U ∖ T).
- κ_t(z) := (M_t(z), s_θ·ℓ(Ξ_t z)) for z ∈ U, ordered lexicographically; κwt(v) := (wt(v), s_θ); κwt(A) := Σ_{v∈A} κwt(v) (componentwise).
  For a path p, κwt(p ∖ {end}) sums over its vertices except the last.
- G_U^o: the graph on U ∖ {c_θ} in which Even v ≠ o keeps its edges into U ∖ {c_θ}, Odd v ≠ o keeps its forced edge if it lies in
  U ∖ {c_θ}, and o is a sink. (So G_Û handles paths to c_θ avoiding o, G_U^o paths to o avoiding c_θ.)
- Facts (landed or restated with proofs in P-N5-PFZ §1 / P-N5-RHO §0; the κ forms follow with the same proofs):
  - (A_κ) for z ∈ U ∖ {c_θ}: next_t(z) ∈ U and κ_t(z) = κwt(z) + κ_t(next_t z). ((A) of P-N5-PFZ §1 for M; (V1) adds 1 to ℓ.)
    κ_t(c_θ) = (0, 0) (cycle node value (c_θ, ∅, 0)).
  - (M1κ) for valuations x, x′ with cycle node c_θ: x ⊴ x′ ⇔ κ(x) ≤ κ(x′) (S1's order: reward(c_θ) equal, then the signed weight of P,
    then ℓ in the direction s_θ). (M2κ) κ_t(z) ≤ κ_{t+1}(z) for z ∈ U at every in-phase transition (RESULTS R15 (a) + (M1κ)).
  - (INJ) the signed weight is injective on vertex sets (distinct powers of 2); in particular M_t(z) = 0 ⇔ P(Ξ_t z) = ∅.
  - (HP) on 𝒞^1O the honest play and the (σ_t, τ)-play from any vertex agree until their first visit of o. Hence a vertex whose honest
    play never visits o lies in F_t, and a vertex whose honest play visits o has λ_t = λ_t(o) = c_θ.
  - (SP′) for z ∈ U ∖ {c_θ}, the honest play at t from z stays in U and visits c_θ; its prefix up to its first visit of T is a simple
    path. Proof: it stays in U by (A_κ); it ends in a cycle whose cycle node is c_θ, so the cycle contains c_θ; a play is a lasso whose
    vertices are distinct up to the first repetition, which happens only after the whole cycle, hence after visiting c_θ ∈ T. □
  - In-phase: λ_{k+1} = λ_k pointwise (a phase has λ_Ξ constant; RESULTS R38 (a)). S4c (SPEC, FIX 3): at an Even fallback τ is
    unchanged, every Even v with a gate switches to x*_v, the gate target maximising (Ξ_k(w), w), and no other vertex changes.
  - FBL-N (ii) (RESULTS R21 (c)): at an S4c fallback with τ unchanged, every gate (x, z) with x ∈ F_k has x = λ_W(x) and λ_W(z) = x.
    G (a) (RESULTS R19 (a)): off R, Ξ = W.
  - Y-FORM (b) (P-N5-RHO §1; same fact as RESULTS R34 (a) (F)): at a ¬H1 state P(θ) = ∅. Lemma S (a) (RESULTS R18 (d); XW, R21 (a)).
  - CN-LAST (RESULTS R38 (f), every game): if at an S4c fallback k → k+1 with Iσ_k ≠ ∅ every gate (y, z) has λ_k(y) = y and
    lev(Ξ_k(σ_k y), Ξ_k(z)) = −1 (same cycle node, same P, different length), then Ξ_{k+1} = Ξ_k, Iσ_{k+1} = ∅, and k + 1 is the last
    state of its phase.

## 1. Bellman-Ford with the full key κ (PROVED; the proofs of P-N5-PFZ §1-§2 and P-N5-RHO §2 with κ for M)
- Lemma κ-FB-ROUND. At an in-phase Even fallback k → k+1, for every Even v ∈ U ∖ {c_θ} and every successor x ∈ U of v:
  κ_{k+1}(v) ≥ κwt(v) + κ_k(x).
  Proof. If Ξ_k(x) ⊴ Ξ_k(σ_k v): κ_k(x) ≤ κ_k(σ_k v) (M1κ), so κwt(v) + κ_k(x) ≤ κ_k(v) ≤ κ_{k+1}(v) ((A_κ), (M2κ)). Otherwise
  (v, x) is a gate, v switches to x* with Ξ_k(x*) ⊵ Ξ_k(x); λ_{k+1}(v) = c_θ ≠ v, so (A_κ) at k+1 gives x* ∈ U and
  κ_{k+1}(v) = κwt(v) + κ_{k+1}(x*) ≥ κwt(v) + κ_k(x*) ≥ κwt(v) + κ_k(x) ((M2κ), (M1κ)). □
- Lemma κ-HAT-FREEZE. (a) For j ≥ 0, every state t > g_j, z ∈ Û, and every simple path p of G_Û from z to c_θ with ≤ j edges:
  κ_t(z) ≥ κwt(p ∖ {c_θ}). (b) For z ∈ F_t ∩ U: κ_t(z) = κwt(q ∖ {c_θ}) for z's honest path q to c_θ, a simple path of G_Û.
  (c) For |U| ≥ 2, t > g_{|U|−2} and y ∈ F_t ∩ U: κ_t(y) = κoptÛ(y) := max{κwt(p ∖ {c_θ}) : p a simple path of G_Û from y to c_θ}.
  Proof. (a) Induction on j; j = 0: z = c_θ, κ_t(c_θ) = (0, 0). Step: p = z·p′ from x. z Odd: x = next_t(z) (forced), (A_κ) and the
  hypothesis at t. z Even: k := g_j < t; hypothesis at k (k > g_{j−1}) for x; κ-FB-ROUND at k; (M2κ) from k+1 to t. (b) (HP), (SP′),
  (A_κ) along q. (c) simple paths of G_Û have ≤ |U| − 2 edges; (a) and (b). □
- Lemma κ-PFZ (the θ-run version, terminal o). Let Θ be a θ-run of the phase with o ≠ c_θ, f^Θ_1 < f^Θ_2 < … its in-phase Even
  fallbacks (transitions k → k+1 with k ∈ Θ). For j ≥ 0, every t ∈ Θ with t > f^Θ_j, z ∈ U ∖ {c_θ} and every simple path p of G_U^o
  from z to o with ≤ j edges: κ_t(z) ≥ κwt(p ∖ {o}) + κ_t(o). (κ_t(o) = κ(θ_Θ) is constant on Θ.)
  Proof. Induction on j; j = 0: z = o. Step: p = z·p′, z ≠ o, p′ from x. z Odd: (A_κ) at t, x forced, hypothesis at t. z Even:
  k := f^Θ_j < t, k ∈ Θ and k > f^Θ_{j−1}; hypothesis at k: κ_k(x) ≥ κwt(p′ ∖ {o}) + κ(θ_Θ); κ-FB-ROUND at k; (M2κ) from k+1 to t
  (k+1 ≤ t, so k+1 ∈ Θ). □ (This is P-N5-PFZ's P-FREEZE lower bound with κ, restricted to paths that avoid c_θ.)
- Lemma κ-Y-FORM (a). At an H1 state t: κ_t(o) = κwt(o) + min_{y∈Y_t} κ_t(y), Y_t := succ(o) ∩ U ∩ F_t.
  Proof. Y-FORM (a)'s proof (P-N5-RHO §1) with κ: σ̄_t(o) ∈ Y_t and (A_κ) give "≥"; Lemma S (a) gives Ξ_t(o) ⊴ o ⊕ Ξ_t(y) for y ∈ Y_t,
  and κ(o ⊕ Ξ_t y) = κwt(o) + κ_t(y) (o ∉ P(Ξ_t y), length + 1), so (M1κ) gives "≤". □

## 2. Lemma EXIT-SWITCH (PROVED; every in-phase Even fallback, no hypothesis on H1/H2/H3/τ(o))
Statement. Let k → k+1 be an in-phase Even fallback with S_U ≠ ∅. Then some u ∈ S_U has this property: the honest play at k from x*_u
visits T before it visits u. For such u, let e ∈ T be the first terminal visited and p_u := u · (that play up to e). Then p_u is a simple
path from u to e, it lies in G_Û if e = c_θ and in G_U^o if e = o, and κ_k(x*_u) = κwt(p_u ∖ {u, e}) + κ_k(e).
Proof.
- For w ∈ U ∖ T: if w ∉ S_k then next_{k+1}(w) = next_k(w) (Even: σ unchanged; Odd w ≠ o: forced). If w ∈ S_U then next_{k+1}(w) = x*_w,
  and x*_w ∈ U ((A_κ) at k+1, as λ_{k+1}(w) = λ_k(w) = c_θ ≠ w).
- Suppose, for a contradiction, that for every u ∈ S_U the honest play at k from x*_u visits u before T. Take v ∈ S_U. By (SP′) at k+1
  (λ_{k+1}(v) = c_θ), the honest play at k+1 from v visits c_θ ∈ T. But by induction it never visits T: whenever it stands at some
  u ∈ S_U, it moves to x*_u; from there the k-play visits u before T, and every vertex it visits before its first vertex of S_U ∪ T lies
  in U ∖ (S_U ∪ T) (the play stays in U, (A_κ)), where the k+1-play and the k-play take the same step. So the k+1-play follows the k-play
  until a vertex u′ ∈ S_U, with no terminal in between. (Vertices of S_k outside U are never visited: the play stays in U.) Contradiction.
- For u as in the statement: the k-play from x*_u up to e is simple (SP′; if x*_u ∈ T it is the single vertex e) and avoids u, so p_u is
  simple. Its edges: u → x*_u (u Even, x*_u ∈ U), then σ_k-edges at Even vertices and forced edges at Odd vertices ≠ o, all inside U.
  Before e it avoids T, so p_u lies in G_Û (e = c_θ) or in G_U^o (e = o). (A_κ) along the play from x*_u to e gives the value. □

## 3. Lemma FREEZE-EXIT (PROVED)
Statement. Let o ≠ c_θ, and let k = g_j be an in-phase Even fallback that is the i-th fallback of its θ-run Θ. If j ≥ |U| − 1 and
i ≥ |U| − 1, then S_U = ∅.
Proof. If S_U ≠ ∅, take u and p_u from EXIT-SWITCH. p_u avoids the other terminal, so it has ≤ |U| − 2 edges (G_Û and G_U^o have
|U| − 1 vertices each). The switch is through a gate: Ξ_k(x*_u) ▷ Ξ_k(σ_k u), both with cycle node c_θ, so κ_k(x*_u) > κ_k(σ_k u) (M1κ).
- e = c_θ: κ-HAT-FREEZE (a) at k > g_{|U|−2} gives κ_k(u) ≥ κwt(p_u ∖ {c_θ}) = κwt(u) + κ_k(x*_u).
- e = o: κ-PFZ at k ∈ Θ, k > f^Θ_{|U|−2}, gives κ_k(u) ≥ κwt(p_u ∖ {o}) + κ_k(o) = κwt(u) + κ_k(x*_u).
In both cases (A_κ) at u gives κ_k(σ_k u) = κ_k(u) − κwt(u) ≥ κ_k(x*_u), a contradiction. □

## 4. Lemma CN-ONLY (PROVED; every in-phase Even fallback)
Statement. If k → k+1 is an in-phase Even fallback with S_U = ∅, then every gate (y, z) ∈ Iσ_k has λ_k(y) = y and
lev(Ξ_k(σ_k y), Ξ_k(z)) = −1; hence (CN-LAST) k + 1 is the last state of the phase. So a phase has at most one such fallback.
Proof.
- Every switched y is a cycle node of Ξ_k. y ∈ U ∖ T is excluded; o is Odd; y = c_θ is one. If y ∉ U, y's honest play never visits o
  ((HP): else λ_k(y) = c_θ), so y ∈ F_k; FBL-N (ii) gives y = λ_W(y), and λ_W(y) = λ_k(y) by G (a). The gate sources are exactly the
  switched vertices (S4c switches every Even vertex with a gate).
- For a switched y: λ_{k+1}(y) = λ_k(y) = y, so y lies on its own honest cycle at k+1, x*_y is on that cycle and λ_k(x*_y) =
  λ_{k+1}(x*_y) = y. Claim: P(Ξ_k x*_y) = ∅ and P(Ξ_k σ_k y) = ∅.
  - P(Ξ_k σ_k y) = ∅: σ_k(y) lies on y's honest cycle at k, whose most relevant vertex is y.
  - y ≠ c_θ: the k-play from x*_y stays in λ_k^{-1}(y) ⊆ F_k ∖ U until it reaches y. Its vertices other than y are not cycle nodes, so
    they have no gate (first bullet) and do not switch; its Odd vertices are not o (o ∈ U), so they are forced. So the k+1-play from
    x*_y is the same path, and y's cycle at k+1 is y · (that path). Its most relevant vertex is y, so every vertex of the path has
    p′ < p′(y): P(Ξ_k x*_y) = ∅.
  - y = c_θ, and the k-play from x*_y reaches c_θ before o: its vertices before c_θ are in U ∖ T, not switched (S_U = ∅), so as above
    c_θ's cycle at k+1 is c_θ · (that path) and P(Ξ_k x*_y) = ∅.
  - y = c_θ, and the k-play from x*_y reaches o first (possibly x*_y = o), along a path π: π is unchanged at k+1 (same reason), so the
    k+1-play from c_θ is c_θ · π · o · …, and it returns to c_θ. So o and π lie on c_θ's honest cycle at k+1: ¬H1 at k+1, M_{k+1}(o) = 0
    (Y-FORM (b)), and every vertex of π has rank < rank(c_θ), wt = 0. By (A_κ) along π and (M2κ) at o: M_k(x*_y) = M_k(o) ≤ M_{k+1}(o) = 0.
    The gate Ξ_k(x*_y) ▷ Ξ_k(σ_k c_θ), with M_k(σ_k c_θ) = 0 ((A0) of P-N5-RHO §0) and (M1κ), gives M_k(x*_y) ≥ 0. So M_k(x*_y) = 0 and
    P(Ξ_k x*_y) = ∅ (INJ).
- Every gate (y, z): Ξ_k(σ_k y) ◁ Ξ_k(z) ⊴ Ξ_k(x*_y) (x*_y maximises (Ξ_k(w), w) over the gates of y). The two ends are (y, ∅, ℓ_0) and
  (y, ∅, ℓ*). S1 compares the reward first and the reward is injective (p′ is), so Ξ_k(z) has cycle node y; then the signed weight lies
  between 0 and 0, so P(Ξ_k z) = ∅ (INJ). So Ξ_k(z) differs from Ξ_k(σ_k y) only in length: lev = −1. CN-LAST applies. □

## 5. Lemma THETA-AFTER (PROVED)
Statement. Let o ≠ c_θ and |U| ≥ 2. At most deg_U(o) + |U| − 2 transitions t → t+1 of the phase with t > g_{|U|−2} change θ. Hence at most
deg_U(o) + |U| − 1 θ-runs of the phase contain a state t > g_{|U|−2}. (If the phase has fewer than |U| − 2 fallbacks, this is vacuous.)
Proof. θ has cycle node c_θ throughout, so θ is determined by κ(o) (INJ), and κ(o) is non-decreasing (M2κ). For t > g_{|U|−2}:
- H1 at t: κ_t(o) = κwt(o) + min_{y∈Y_t} κ_t(y) (κ-Y-FORM) and κ_t(y) = κoptÛ(y) for y ∈ Y_t ⊆ F_t ∩ U (κ-HAT-FREEZE (c)). So κ_t(o) lies
  in V_H := {κwt(o) + κoptÛ(y) : y ∈ succ(o) ∩ U, κoptÛ(y) defined}, |V_H| ≤ deg_U(o).
- ¬H1 at t: P(θ_t) = ∅ (Y-FORM (b)) and 1 ≤ ℓ(θ_t) ≤ |U| − 1 ((SP′) at o, o ≠ c_θ). So κ_t(o) ∈ V_N := {(0, s_θ·ℓ) : 1 ≤ ℓ ≤ |U| − 1}.
A non-decreasing sequence with values in V_H ∪ V_N changes at most |V_H ∪ V_N| − 1 ≤ deg_U(o) + |U| − 2 times. □
- This is the κ form of RHO-TAIL (P-N5-RHO §3). RHO-TAIL counts only P(θ)-changes, because HAT-FREEZE froze only M; κ-HAT-FREEZE also
  freezes lengths, and that is what bounds θ-changes (length changes included) after the freeze.

## 6. Theorem FB-POLY (PROVED; 𝒞^1O, one phase, no hypothesis on H1/H2/H3/τ(o)/c_w/θ/N_HN)
Statement. Let f be the number of in-phase Even S4c fallbacks of a phase.
- (a) If o ≠ c_θ and |U| ≥ 2: f ≤ 1 + (|U| − 2)·(deg_U(o) + |U|) ≤ 1 + (n − 2)(2n − 1).
- (b) If |U| = 2: f ≤ 1, i.e. L-RED's FB-CAP (f ≤ max(1, |U| − 2)) HOLDS for |U| = 2.
- (c) If o = c_θ: f ≤ |U|.
- (d) In every case, all but at most one of the fallbacks switch a vertex of U ∖ T, and the exceptional one (if any) ends the phase.
Proof.
- (d) is CN-ONLY.
- (a) Fallbacks with S_U = ∅: ≤ 1 (CN-ONLY). Fallbacks g_j with S_U ≠ ∅: those with j ≤ |U| − 2 number ≤ |U| − 2. Those with
  j ≥ |U| − 1 lie (FREEZE-EXIT) among the first |U| − 2 fallbacks of their θ-run, and their θ-run contains the state g_j > g_{|U|−2};
  by THETA-AFTER there are ≤ deg_U(o) + |U| − 1 such θ-runs. Total ≤ 1 + (|U| − 2) + (|U| − 2)(deg_U(o) + |U| − 1).
- (b) U = {o, c_θ}, so U ∖ T = ∅ and every fallback has S_U = ∅: ≤ 1 by CN-ONLY.
- (c) o = c_θ: T = {o}, θ = (o, ∅, 0) at every state, so the phase is one θ-run. EXIT-SWITCH holds verbatim with T = {o} (its proof uses
  only "the k+1-play from v visits a terminal"). κ-PFZ holds verbatim in the graph G_U of P-N5-PFZ §0 (o = c_θ its only sink; κ(θ) = (0, 0)),
  and p_u is a simple path of G_U with ≤ |U| − 1 edges; so at the i-th fallback with i ≥ |U|, S_U = ∅ (FREEZE-EXIT's proof). Hence ≤ |U| − 1 fallbacks with S_U ≠ ∅, plus ≤ 1. □
- Remarks.
  - Odd fallbacks change τ and end the phase (SPEC S4c, FIX 3), so they are not in-phase; f counts every fallback a phase can hold
    except the one at its end.
  - What FB-POLY replaces. Known per-phase fallback bounds were polynomial only given other counts: FB-INT (R38 (d), per
    crossing-free run), NH1-FB (R38 (e), ¬H1 fallbacks, given T), EPOCH (R39 (b), given B_S and X_S), BRK-POLY / HN-POLY (lane, given
    ρ, N_HN). FB-POLY needs none of them. With it, SCOPE-COUNT's f term (R38 (c)) and EPOCH's f_S are ≤ 1 + (n − 2)(2n − 1) per phase.
  - What FB-POLY does NOT give: crossings X per phase, θ-changes BEFORE g_{|U|−2} (θ_ph), S4a steps, the number of phases. G-N5-TIME
    stays OPEN.
  - The route of N5-FBCAP-route-box40.md §2 is superseded: its cases (i)-(ii) (F ∩ U switches) are empty by FBL-N (ii) except at c_θ,
    its (iii) and (iv) are both FREEZE-EXIT (terminal c_θ, resp. o, with the θ-run count of THETA-AFTER), its (v) (outside U) and the
    c_θ-cycle exception are CN-ONLY, and its (vi) (¬H1 states) needs nothing: no step above assumes H1.

## 7. What stays open, and the obstruction to FB-CAP for |U| ≥ 3
- CONJECTURE FB-CAP (L-RED succ. 17, R71 draft): f ≤ max(1, |U| − 2). OPEN for |U| ≥ 3. The proof above gives |U| − 2 Bellman-Ford rounds
  for paths to c_θ (one freeze per phase), but the rounds for paths to o restart at every θ-change: κ-PFZ's bound uses κ(o) at the
  state of the relaxation, and after θ rises, a route that was relaxed against the old κ(o) is a strict lower bound again. THETA-AFTER
  bounds the restarts by deg_U(o) + |U| − 2, each costing ≤ |U| − 2 rounds. Closing FB-CAP needs one of:
  - (FB-CAP-1) after g_{|U|−2}, no fallback switches toward o (every e = o switch happens before the hat freeze); or
  - (FB-CAP-2) a θ-change after g_{|U|−2} leaves the route relaxations valid (e.g. it is caused by c_θ-side values only).
  Neither is proved; no instance against either is known (the post-freeze regime is never reached in data, §8).
- OPEN (structural, not needed): EXIT-SWITCH's "loop" branch (x*_u's play passes u: the switch closes a κ-positive cycle through u that
  another switch must break) never occurs in data (0 of 1,537 + 7 switched U ∖ T vertices, §8).

## 8. DATA (DATA, not proof; experiments/new/box41/fbpoly.py, run 2026-10-25 18:2xZ by date -u)
- Checks per in-phase Even fallback: CN-ONLY (CNa every switched vertex a cycle node; CNb every gate lev −1; CNc k + 1 the last state of
  the phase); EXIT-SWITCH (GS) and the kind of every switched U ∖ T vertex (loop / ct / o); FREEZE-EXIT's two halves separately (HF:
  kind ct only at g_j with j ≤ |U| − 2; PF: kind o only at the first |U| − 2 fallbacks of the θ-run); UT-POS; THETA-AFTER; the FB-POLY
  bound. Direct checks of κ-HAT-FREEZE (a) (KH) and κ-PFZ (KP) against exact best κ-paths with ≤ j edges (3 ≤ |U| ≤ 12).
- Instances: (L) experiments/new/box41/lib41.txt (412 files, the P-N5-RHO §8 (L) list; 253 𝒞^1O, 159 skipped), canonical start (S3);
  (R) `fbpoly.py --rand 4000 6 20 4101 3` (random 𝒞^1O, o-cyclic, n 6-20, canonical start + 3 random Even start strategies each).
- Results: 0 failures of every check, on (L) and (R).
  | set | runs | phases | fallbacks | CN-ONLY (all last of phase) | with S_U ≠ ∅ | switched U ∖ T: ct / o / loop | KH | KP | max f per phase (|U|) |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | (L) | 253 | 990 | 660 | 21 | 639 | 1,509 / 28 / 0 | 531 | 395 | 33 (48, ccl_w48_n48) |
  | (R) | 13,364 | 33,017 | 615 | 610 | 5 | 7 / 0 / 0 | 731 | 629 | 2 (17) |
- Honest caveats (lesson N-ENT-2): FREEZE-EXIT's and THETA-AFTER's hypotheses (j ≥ |U| − 1 at |U| ≥ 3) NEVER occur in (L) or (R)
  (as in L-RED R71 §2 and P-N5-RHO §8): those two lemmas, and the (a) bound beyond FB-CAP, are untested by data; only the lemmas they rest
  on (KH, KP, GS, CN-ONLY) are tested where their hypotheses hold. FB-CAP (max f − max(1, |U| − 2) = 0) holds in all data, as L-RED found.
