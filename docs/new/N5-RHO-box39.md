# N5 on 𝒞^1O, box 39 (2): P(θ)-changes per phase. After |U| − 2 fallbacks of a phase, P(θ) changes at most deg(o) more times; inside a fallback-free HN run at most |U| + deg(o) − 3 times; so over the HN states of a phase ρ_HN is polynomial in n and N_HN (Y-FORM, HAT-FREEZE, RHO-TAIL, BF-F, FREEZE-F, RHO-HN)
L-NEW successor 18 (Opus 5.5, D15/D18), session_01BhkSHzG2cPM2Rdbj5Y2NJV. Working doc (not a packet). Written 2026-10-25 15:3xZ by date -u.
- Setting, notation and facts (A), (M1′), (M2′), FB-ROUND: docs/new/P-N5-PFZ-box39.md §0-§1 (sha1 3c617e06…). P-epochs, ρ: docs/new/
  P-N5-PFZ-ext-box39.md (sha1 b3702b1b…). Û := U ∖ {o}. G_Û := G_U restricted to Û, with c_θ the only terminal (o removed).
  MoptÛ(z) := the max weight wt(p ∖ {c_θ}) of a simple path p in G_Û from z to c_θ. deg(o) := the out-degree of o. Y_t :=
  succ(o) ∩ U ∩ F_t. N_HN := the number of HN stretches of the phase.
- Labels: PROVED (L-NEW succ. 18, unrefereed), OPEN, DATA. Not a running-time bound; G-N5-TIME stays OPEN. No (P).

## Summary
1. **Lemma Y-FORM (PROVED).** At every H1 state t of a phase, M_t(o) = wt(o) + min_{y ∈ Y_t} M_t(y).
   At a ¬H1 state, P(θ) = ∅.
2. **Lemma HAT-FREEZE (PROVED).** After the (|U| − 2)-th in-phase fallback of a phase, M_t(y) = MoptÛ(y) for every y ∈ F_t ∩ U, at
   every later state t of the phase. Here θ is allowed to change.
3. **Theorem RHO-TAIL (PROVED).** After the (|U| − 2)-th in-phase fallback of a phase, P(θ) changes at most deg(o) more times in the
   phase.
4. **Lemma BF-F (PROVED).** At an S4a transition k → k+1 between two HN states of a phase, every Even v ∈ U ∩ F_{k+1}, v ≠ c_θ, and
   every successor x ∈ U satisfy M_{k+1}(v) ≥ wt(v) + M_k(x).
5. **Theorem FREEZE-F (PROVED).** In a run of consecutive HN states of a phase with no fallback transition, P(θ) changes at at most
   (|U| − 2) + (deg(o) − 1) transitions.
6. **Theorem RHO-HN (PROVED).** Over the transitions with both ends HN in one phase:
   ρ_HN ≤ (N_HN + |U| − 2)(|U| + deg(o) − 3) + deg(o).
   With P-N5-PFZ-ext BRK-POLY′ and R39 (b) EPOCH, the HN breaks, crossings, fallbacks and θ-changes of a phase are polynomial in n and
   N_HN. For τ(o) = o phases, R39 (f) (N_HN ≤ ⌊T*/2⌋ + 1, T* ≤ n² + 2n − 1) makes them polynomial in n.
7. **OPEN.** N_HN for τ(o) ≠ o; the non-HN states (SN, OTHER); S4a steps that change nothing counted here (iterations); whether the
   bounds of 3 and 6 are ever approached.
8. **DATA (rho.py).** 0 failures of every check. BF-F (33,503 checks) and FREEZE-F (c) (112 runs) are exercised. HAT-FREEZE / Y-FORM
   after the freeze are exercised only on climb outputs (40 checks). FREEZE-F (b) is vacuous in data (§7).

## 1. Lemma Y-FORM (PROVED)
Statement. At an H1 state t of a phase: σ̄_t(o) ∈ Y_t and M_t(o) = wt(o) + min_{y∈Y_t} M_t(y). At a ¬H1 state: P(θ_t) = ∅, M_t(o) = 0.
Proof.
- H1. o's honest play never returns to o, so σ̄_t(o)'s honest play avoids o. On 𝒞^1O the honest and (σ_t, τ)-plays agree off o, so
  σ̄_t(o) ∈ F_t, and σ̄_t(o) ∈ U by (A). So σ̄_t(o) ∈ Y_t, and (A) gives M_t(o) = wt(o) + M_t(σ̄_t o).
- For y ∈ Y_t, let τ′ be Odd's strategy with τ′(o) = y (the other Odd vertices are forced).
  - y's play under (σ_t, τ′) is its honest play (it avoids o), so V_{σ_t,τ′}(o) = o ⊕ Ξ_t(y), with cycle node c_θ.
  - Lemma S (a) (RESULTS R18 (d): Ξ_σ is the pointwise minimum of V_{σ,τ′} over Odd's strategies; no (P)) gives
    Ξ_t(o) ⊴ o ⊕ Ξ_t(y). With the same cycle node, M_t(o) ≤ wt(o) + M_t(y).
- ¬H1: o lies on its honest cycle, whose top is c_θ. If o = c_θ, θ = (o, ∅, 0). Otherwise RESULTS R34 (a) (F) gives
  θ = (c_θ, ∅, dist). □

## 2. Lemma HAT-FREEZE and Theorem RHO-TAIL (PROVED)
Statement (HAT-FREEZE). Let g_1 < g_2 < … be the in-phase Even S4c fallback transitions of a phase.
- (a) For every j, every state t > g_j of the phase, every z ∈ Û and every simple path p in G_Û from z to c_θ with ≤ j edges:
  M_t(z) ≥ wt(p ∖ {c_θ}).
- (b) For z ∈ F_t ∩ U: M_t(z) ≤ MoptÛ(z).
- (c) Hence M_t(y) = MoptÛ(y) for every y ∈ F_t ∩ U and every state t > g_{|U|−2} (every t, if |U| = 2).
Proof.
- (a) As P-N5-PFZ §2 (a) with the single terminal c_θ. The induction never uses o, so θ may change.
  - FB-ROUND at g_j holds for every in-phase Even fallback; it does not use θ.
  - (M2′) holds on the whole phase (c_θ is a phase constant).
  - Odd vertices of Û other than c_θ are forced. An Odd vertex whose forced successor is o has no edge in G_Û.
- (b) z ∈ F_t: its honest play avoids o and stays in F_t ∩ U, so its prefix to c_θ is a simple path of G_Û. Then (A).
- (c) Simple paths in G_Û have ≤ |Û| − 1 = |U| − 2 edges. □
Statement (RHO-TAIL). After g_{|U|−2}, P(θ) changes at ≤ deg(o) transitions of the phase.
Proof.
- By Y-FORM and HAT-FREEZE (c), at every H1 state t > g_{|U|−2}, M_t(o) = wt(o) + min_{y∈Y_t} MoptÛ(y). This is one of the
  ≤ deg(o) numbers {wt(o) + MoptÛ(y) : y ∈ succ(o) ∩ U}.
- At ¬H1 states, M_t(o) = 0.
- M(o) is non-decreasing on the phase (R15 (a) at o, with c_θ fixed). So it takes ≤ deg(o) + 1 values in order: ≤ deg(o) changes.
- P(θ) is determined by M(o) (injectivity). □

## 3. Lemma BF-F and Theorem FREEZE-F (PROVED)
Statement (BF-F). Let k → k+1 be an in-phase S4a transition with HN at k and at k+1. For every Even v ∈ U ∩ F_{k+1}, v ≠ c_θ, and every
successor x ∈ U of v: M_{k+1}(v) ≥ wt(v) + M_k(x).
Proof.
- v ∈ F_k (SPLIT (a), R39 (a): R_k ⊆ R_{k+1}).
- Case 1: M_k(x) ≤ M_k(σ_k v). Then wt(v) + M_k(x) ≤ M_k(v) ≤ M_{k+1}(v), by (A) and (M2′).
- Case 2: M_k(x) > M_k(σ_k v). By (M1′), (v, x) ∈ Iσ_k, so x ∈ A_k(v), and σ″ := σ_k with v ↦ x is a strategy of the S4a arena. By F1
  (RESULTS R17 (a)), W_{k+1} ⊵ W_{σ″}. By G (a) (RESULTS R19 (a)), W_{k+1}(v) = Ξ_{k+1}(v), with cycle node c_θ (v ∈ U ∩ F_{k+1}).
  - x ∈ R̄_k: x's (σ″, τ)-play is its route, then o's W-cycle C_W ⊆ R̄_k, which avoids v ∈ F_k. So W_{σ″}(v) has cycle node c_w.
    At an HN state c_w ∈ R̄ and c_θ ∈ F, so XW (RESULTS R21 (a), θ ⊴ w) gives reward(c_θ) < reward(c_w). So W_{σ″}(v) ▷ W_{k+1}(v),
    against F1. Impossible.
  - x ∈ F_k, and x's play passes v. Then x's play is q · v · (v's play), q ∪ {v} avoids o, and by (A),
    M_k(x) = wt(q) + wt(v) + M_k(σ_k v). So wt(q ∪ {v}) > 0. Under σ″, v closes the cycle v → x → q → v; it avoids o, so it is the
    same for W.
    - Its top u is even and has rank > rank(c_θ). (The weight is positive, so the top of its part above c_θ is even, and it is the top
      of the cycle.)
    - So reward(u) > reward(c_θ), W_{σ″}(v) ▷ W_{k+1}(v), against F1. Impossible.
  - x ∈ F_k, and x's play avoids v. Then W_{σ″}(v) = v ⊕ W_k(x) = v ⊕ Ξ_k(x) (G (a)), with cycle node c_θ. F1 gives
    Ξ_{k+1}(v) ⊵ v ⊕ Ξ_k(x), so M_{k+1}(v) ≥ wt(v) + M_k(x). □
Statement (FREEZE-F). Let [s, e] be a run of consecutive HN states of one phase with no fallback transition.
- (a) For t ∈ [s, e], z ∈ F_t ∩ U, and every simple path p in G[F_t ∩ U] from z to c_θ with ≤ t − s edges: M_t(z) ≥ wt(p ∖ {c_θ}).
- (b) For t ≥ s + |U| − 2: M is constant on F_t ∩ U from t on, within [s, e].
- (c) At most (|U| − 2) + (deg(o) − 1) transitions of [s, e] change P(θ).
Proof.
- (a) Every transition is S4a, so F_{t+1} ⊆ F_t (SPLIT (a)), and c_θ ∈ F_t (under H1 its play is its own cycle, which avoids o).
  Induction on t − s as in P-N5-PFZ §2 (a): a path of G[F_{t+1} ∩ U] is one of G[F_t ∩ U]. Use BF-F for Even z, and (A) + (M2′) for
  Odd z.
- (b) A path in G[F_t ∩ U] has ≤ |U| − 2 edges, and honest plays of z ∈ F_t ∩ U are such paths. So M_t = MoptF_t on F_t ∩ U, where
  MoptF_t is the best simple path in G[F_t ∩ U]. MoptF_t can only fall as F shrinks, and M can only rise, so both are constant.
- (c) In the first |U| − 2 transitions, ≤ |U| − 2 changes. Afterwards, by Y-FORM, M_t(o) = wt(o) + min_{y ∈ Y_t} M_t(y). The values
  M_t(y) are constant by (b), and Y_t = succ(o) ∩ U ∩ F_t only shrinks. So the min takes ≤ |Y| ≤ deg(o) values: ≤ deg(o) − 1
  changes. □

## 4. Theorem RHO-HN (PROVED)
Statement. For one phase, ρ_HN (the transitions with both ends HN at which P(θ) changes) satisfies
ρ_HN ≤ (N_HN + |U| − 2)(|U| + deg(o) − 3) + deg(o).
Proof.
- Fallback transitions with HN at the start do not change θ (F-FLAT, RESULTS R39 (c)).
- Transitions after g_{|U|−2}: ≤ deg(o) changes (RHO-TAIL).
- Every other counted transition lies in a maximal run of consecutive HN states without fallback transitions that meets the part of the
  phase before g_{|U|−2}. These runs are cut only at HN-stretch boundaries and at fallbacks. There are ≤ N_HN + (|U| − 2) of them, each
  with ≤ |U| + deg(o) − 3 changes (FREEZE-F (c)). □
- Corollary HN-POLY (PROVED).
  - Summing P-N5-PFZ-ext BRK-POLY′ over the HN stretches S of a phase (Σ_S (ρ_S + 1) ≤ ρ_HN + 2N_HN, counting transitions at stretch
    ends) gives Σ_S B_S, Σ_S θ_S ≤ poly(n, N_HN). EPOCH (R39 (b)) then gives the HN crossings and HN fallbacks of the phase ≤
    poly(n, N_HN, K).
  - For τ(o) = o, N_HN ≤ ⌊T*/2⌋ + 1 with T* ≤ n² + 2n − 1 (R39 (f)), so all of these are polynomial in n.
  - Not covered: N_HN for τ(o) ≠ o, non-HN states, and S4a steps that change none of the counted quantities.

## 5. Dependencies
| tag | location | status |
| --- | --- | --- |
| (A), (M1′), (M2′), FB-ROUND | P-N5-PFZ §1 | in review (pin pending) |
| Lemma S (a) | RESULTS R18 (d) | LANDED, no (P) |
| F1 | RESULTS R17 (a) | LANDED |
| G (a) | RESULTS R19 (a) | LANDED |
| XW | RESULTS R21 (a) | LANDED |
| (F) | RESULTS R34 (a) | LANDED |
| SPLIT, F-FLAT, EPOCH, NE-COUNT (c) | RESULTS R39 (a), (c), (b), (f) | LANDED |
| BRK-POLY′ | P-N5-PFZ-ext §3 | in review (pin pending) |

## 6. To do next (for the next session)
- A frozen packet for §1-§4 (P-N5-RHO), if the Lead routes it.
- An adversarial climb against FREEZE-F (c) and RHO-TAIL. Also push phases past g_{|U|−2} with H1 states: the library never gets
  there.
- N_HN for τ(o) ≠ o: HN stretches end at H1-toggles or H2-changes. TOGGLE-COUNT (R34 (e)) bounds H1-toggles per phase for all τ;
  H2-changes are w-changes (WCH, R38). Check whether N_HN ≤ (H1-toggles) + (H2-changes) + 1 is already polynomial by R34 (e) +
  R38 WCH. If so, HN-POLY holds for every τ(o).

## 7. DATA (rho.py; library 270 𝒞^1O files + box-37/38 instances; canonical start)
- 990 phases, 106 with HN states.
- BF-F: 28,394 checks, 0 failures.
- FREEZE-F: 91 fallback-free HN runs (with > 1 state). Max P(θ)-changes in one run: 13 (experiments/red/so/instances/epsseg_cex_n48.pg,
  n 48, |U| 48, deg(o) 17; bound 62). 0 failures of (c). M-constancy (b) is VACUOUS: no fallback-free HN run is longer than |U| − 2.
- RHO-TAIL / Y-FORM after the freeze, library only: 29 phases pass g_{|U|−2}, none with an H1 state after it (vacuous).
  With the box-39 climb outputs (experiments/new/out/box39/*.pg, gitignored) added: 1,038 phases, 33 past g_{|U|−2}. Y-FORM there:
  40 checks; HAT-FREEZE (c) against exact MoptÛ: 40 checks; 0 failures. RHO-TAIL max 0 changes. BF-F 33,503 checks, 0 failures.
- ρ_HN: 87 in total over 106 phases; max 13 (epsseg_cex_n48, 1 HN stretch; bound 2,931). 0 failures.
