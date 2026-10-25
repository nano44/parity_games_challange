# N5 on 𝒞^1O, box 40 (4): a proof route for L-RED's CONJECTURE FB-CAP (in-phase Even fallbacks per phase ≤ max(1, |U| − 2)) via a Bellman-Ford freeze of the full valuation key κ = (M, s_θ·ℓ)
L-NEW successor 19 (Opus 5.5, D15/D18), session_011reTXakSJCcwLhC4i9ZpkB. Working doc (not a packet), written 2026-10-25 17:4xZ by date -u,
after the Lead's 17:34Z relay of FB-CAP (L-RED 17, l-red 1b00610, experiments/red/frz/). For successor 20's queue.
- Notation: docs/new/P-N5-RHO-box40.md §0, docs/new/P-N5-NHN-box40.md §0 (κ_t(z) := (M_t(z), s_θ·ℓ(Ξ_t z)), lexicographic).
- Labels: PROVED (L-NEW succ. 19, unrefereed; short proofs below), ROUTE (a plan, not a proof), OPEN, DATA.

## 0. Why |U| − 2 is suggestive
- FB-CAP's threshold is HAT-FREEZE's threshold g_{|U|−2} (P-N5-RHO §2): simple paths of G_Û have ≤ |U| − 2 edges.
- DATA consistent with FB-CAP: rhoclimb.py survey (P-N5-RHO §8) found max (#fallbacks − (|U| − 2)) = −1 over library phases with |U| ≥ 3
  and an H1 state; the box-40 climbs reached exactly 0 (|U| = 3) and never > 0; RHO's post-freeze regime (t > g_{|U|−2} at |U| ≥ 4) was
  never reached. If FB-CAP holds, HAT-FREEZE (c) and RHO-TAIL are about the LAST state(s) of a phase only.

## 1. κ-FB-ROUND and κ-HAT-FREEZE (PROVED; same proofs as FB-ROUND / HAT-FREEZE, with κ for M)
- (A_κ) For z ∈ U ∖ {c_θ}: κ_t(z) = (wt(z), s_θ) + κ_t(next_t z) ((A) for M and (V1) for ℓ). (M1′): Ξ_t(y) ⊴ Ξ_{t′}(z) ⇔ κ_t(y) ≤ κ_{t′}(z)
  for y, z ∈ U. (M2′_κ): κ non-decreasing on U along the phase (R15 (a)).
- κ-FB-ROUND: at an in-phase Even fallback k → k+1, for Even v ∈ U ∖ {c_θ} and x ∈ U a successor: κ_{k+1}(v) ≥ (wt(v), s_θ) + κ_k(x).
  Proof: FB-ROUND's two cases verbatim with κ (case 1 by (M1′) and (M2′_κ); case 2: x* with Ξ_k(x*) ⊵ Ξ_k(x), (A_κ) at k+1). □
- κ-HAT-FREEZE: (a) for t > g_j, z ∈ Û, and a simple path p of G_Û from z to c_θ with ≤ j edges: κ_t(z) ≥ κwt(p) := Σ_{u ∈ p ∖ {c_θ}}
  (wt(u), s_θ); (b) z ∈ F_t ∩ U ⇒ κ_t(z) = κwt(z's honest path to c_θ) ≤ κoptÛ(z) := max over simple paths; (c) for t > g_{|U|−2} and
  z ∈ F_t ∩ U: κ_t(z) = κoptÛ(z), i.e. Ξ is FROZEN on F_t ∩ U (cycle node, P and length). Proof: as P-N5-RHO §2. □

## 2. ROUTE: no switch of a U-vertex at an in-phase fallback after g_{|U|−2} (pieces PROVED, gaps marked)
Let k = g_j, j ≥ |U| − 1, an in-phase Even fallback with H1 at k (an HN or a Q state), and v ∈ U an Even vertex that switches, to x*
(S4c: the Ξ-best gate target). In-phase ⇒ λ_{k+1}(v) = c_θ, so x* ∈ U and v's new play does not close a cycle through v (else λ(v) would
become that cycle's top ≠ c_θ, or c_θ would be on it with v ... — CHECK this case: a closed cycle through v with top c_θ is possible only
if c_θ is on it; then c_θ's own play changes, so c_θ = v or c_θ's successor chain passes v: re-check).
- (i) v ∈ F_k, x* ∈ F_k ∩ U (PROVED modulo the cycle case): x*'s honest play avoids v (else the switch closes a cycle through v), so
  v · (x*'s path) is a simple path of G_Û and κoptÛ(v) ≥ (wt(v), s_θ) + κoptÛ(x*). By κ-HAT-FREEZE (c) at k (k > g_{|U|−2}):
  κ_k(v) = κoptÛ(v) ≥ (wt(v), s_θ) + κ_k(x*), against the gate κ_k(x*) > κ_k(σ_k v) = κ_k(v) − (wt(v), s_θ). Impossible.
- (ii) v ∈ F_k, x* ∈ R̄_k: at an HN state FBL-N (iii) + (iii+) exclude F → R̄ gates; at a Q state FBL-N (ii) leaves only gates from
  c′ = λ(t0) ∉ U (docs/new/N5-Q-box40.md §2). Impossible for v ∈ U.
- (iii) v ∈ R_k, x* ∈ F_k ∩ U (an eviction; PROVED): x*'s honest play avoids o and hence v (v reaches o). κ-HAT-FREEZE (a) with j = |U| − 2
  gives κ_k(v) ≥ κoptÛ(v) ≥ (wt(v), s_θ) + κoptÛ(x*) = (wt(v), s_θ) + κ_k(x*) (κ-HAT-FREEZE (c) at x* ∈ F_k ∩ U). Gate: κ_k(x*) >
  κ_k(σ_k v) = κ_k(v) − (wt(v), s_θ). Impossible. So NO EVICTION at an in-phase fallback after g_{|U|−2}.
  - (iii) uses no hypothesis on H1/H2 (κ-HAT-FREEZE (a), (c) need none). Consequence for P-N5-NHN (frozen; for a later packet): an EV2
    end after g_{|U|−2} is an eviction of t0 at an in-phase fallback, so it CANNOT occur; NHN-BOUND (a) tightens to ≤ |U| − 2 EV2 ends and
    N_HN ≤ 1 + ⌈T/2⌉ + |U| − 2, and T0-PIN's branch is empty (matches DATA: 0 post-freeze EV2 ends).
- Correction to (i): the cycle case is real. If v lies on c_θ's own cycle, switching v to x* can close a NEW cycle through v that still
  contains c_θ (and has top c_θ), so λ is unchanged and the transition stays in-phase. There v ∈ F ∩ U has wt(v) = 0 and the gate is a
  length gain around c_θ's cycle (cf. CN-LAST, RESULTS R38 (f): cycle-node length switches). (i) is PROVED only when x*'s path avoids v.
- (iv) v ∈ R_k, x* ∈ R̄_k (a route change inside R̄): OPEN. κ-HAT-FREEZE removes o; route values carry θ. Plan: the θ-run version
  (P-FREEZE for κ with terminal o valued κ(θ)) freezes κ on U after |U| − 1 fallbacks of a θ-RUN; F-FLAT keeps θ at HN fallbacks; at Q
  fallbacks θ? (CHECK: F-FLAT is for HN; a Q analogue is needed.) Also Y-FORM ties θ to min over Y of frozen values after g_{|U|−2}.
- (v) Even vertices OUTSIDE U (other λ-classes U″ = λ^{-1}(c″)): OPEN. FB-ROUND holds in each class (terminal c″ only, if o ∉ U″), so
  each class freezes after |U″| − 1 fallbacks; FB-CAP's max(1, |U| − 2) suggests the o-class dominates, or the other classes are already
  frozen (CHECK in data: switches outside U at in-phase fallbacks).
- (vi) ¬H1 states: FBL-N / route form need H1; NH1-FB (RESULTS R38 (e)) bounds those fallbacks separately.
- If (iv)-(vi) close: after g_{|U|−2} an in-phase fallback switches no vertex, i.e. it is not a fallback (S4c with Iσ ≠ ∅ switches
  every improving vertex). That is FB-CAP's "≤ |U| − 2" (for |U| ≥ 3), up to the max(1, ·) case.

## 3. DATA to run first (successor 20)
- At every in-phase fallback g_j, classify the switched vertices: in U (F→F, R→F, R→R̄, F→R̄) / outside U; and whether j ≥ |U| − 1 ever
  occurs (FB-CAP says no). L-RED's experiments/red/frz/ has the counters; read l-red 1b00610 first.
- κ-HAT-FREEZE (c) directly (it is stronger than HAT-FREEZE (c): lengths too).
