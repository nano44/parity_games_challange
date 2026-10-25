# N5 on 𝒞^1O, box 41 (b): with FB-POLY, crossings in OUT stretches are polynomial (Lemma X-OUT), and the f ↔ X loop of RESULTS R34 is broken (READING)
L-NEW successor 20 (Opus 5.5, D15/D18), session_018pjn8Y8JRES3YuFDUCAJgM. Working doc (not a packet), written 2026-10-25 18:4xZ (date -u).
Companion to docs/new/N5-FBPOLY-box41.md (Theorem FB-POLY, lane PROVED, unrefereed; l-new d65e43af).
- Labels (D18/L40): PROVED (L-NEW succ. 20, unrefereed), READING (how results combine; not a proof of a running-time bound), OPEN.
- Scope: N5 on 𝒞^1O, one phase. G-N5-TIME stays OPEN.

## 1. Lemma X-OUT (PROVED, given Q-SPLIT (b) for the Q case)
Setting. An OUT state is an in-phase state with H1 and c_w ≠ c_θ (an HN state, or a Q state H1 ∧ H2 ∧ ¬H3). An OUT STRETCH is a maximal
run of consecutive OUT states of one phase (box 37's outsn.py name). For an OUT stretch S: f_S := its in-phase Even fallbacks with both
ends in S, X_S := its crossings with both ends in S.
Statement. X_S ≤ (|U| − 2)(f_S + 1) + f_S.
Proof.
- Under H1, R_t ⊆ U ∖ {o, c_θ} for t ∈ S: R̄_t ⊆ U by the route form ((HP), P-N5-RHO §0), o ∉ R_t by definition, and c_θ ∈ F_t (its
  honest play is its cycle, which avoids o under H1). So 0 ≤ |R_t| ≤ |U| − 2.
- A transition k → k+1 with both ends in S is, inside the phase (τ constant), an S4a step or an Even S4c fallback.
  - S4a step: R_k ⊆ R_{k+1} (Q-SPLIT (a), docs/new/N5-Q-box40.md §2: H1 at k and c_w(k) ≠ c_θ; for HN states it is SPLIT (a), RESULTS
    R39 (a), LANDED). So an S4a crossing is an entry and raises |R| by ≥ 1.
  - Fallback: R̄_{k+1} ⊆ R̄_k (HN at k: SPLIT (a), RESULTS R39 (a), LANDED; Q at k with H1 at k+1: Q-SPLIT (b), lane PROVED, unrefereed).
    So a fallback crossing is an eviction and lowers |R| by between 1 and |U| − 2.
- |R| starts ≥ 0 and stays ≤ |U| − 2, so (#entries) ≤ (|U| − 2) + (total decrease) ≤ (|U| − 2)(1 + f_S). Add the ≤ f_S evictions. □
- In a phase with an HN state there is no Q state (H3-IN-HN, P-N5-NHN §6), so an OUT stretch is an HN stretch or a Q-run, never mixed.

## 2. Corollary X-OUT-PHASE (PROVED, given the counts cited)
Let N_OUT be the number of OUT stretches of the phase and f its in-phase Even fallbacks. Crossings with both ends OUT number
≤ (|U| − 2)(f + N_OUT) + f (sum of §1 over the stretches). N_OUT is polynomial:
- τ(o) = o: no Q state (¬H2 everywhere), N_OUT = N_HN ≤ ⌊T/2⌋ + 1 (NE-COUNT (c), RESULTS R39 (f), LANDED), T ≤ n² + 2n − 1 (TOGGLE-COUNT,
  RESULTS R34 (e), LANDED).
- τ(o) ≠ o, phase with an HN state: N_OUT = N_HN ≤ ⌈T/2⌉ + 2|U| − 3 (NHN-BOUND, P-N5-NHN §5; pinned 0bb175d, in review).
- τ(o) ≠ o, phase with a Q state: every state is Q or ¬H1 (P-N5-NHN §6), so Q-runs are separated by H1-toggles: N_OUT ≤ ⌈T/2⌉ + 1.
With FB-POLY (f ≤ 1 + (n − 2)(2n − 1)) this is polynomial in n.

## 3. READING: what FB-POLY changes in the G-N5-TIME accounting (not a proof; every item names its premises)
- f per phase: FB-POLY (lane) replaces the per-class fallback bounds (FB-INT R38 (d), NH1-FB R38 (e), PL-S″ R40, LV-PL R41, OUT-1 R42,
  NE-COUNT R39 (f), BRK-POLY / HN-POLY lane). So REL(S), the level −1 count, NJB's straddle and θ_ph are no longer needed FOR f.
- X_SN per phase ≤ 13(d_o + 1)n³(f + 1 + T) + T (X-SN-PHASE, RESULTS R34 (f), LANDED): polynomial once f is (FB-POLY). This is the
  "f ↔ X loop" of R34's open list: the loop is broken in the direction f first.
- Crossings in OUT stretches: §2 above.
- Scope runs per phase ≤ (1 + T + f) + (n − 2)(X + 1) + X (SCOPE-COUNT, RESULTS R38 (c)): polynomial once X is.
- Still OPEN for a full per-phase bound, as far as this lane can see (the Lead's map governs): crossings at transitions with an end that
  is neither SN-prefix nor OUT (¬H1 states outside SN prefixes, and the boundary transitions between classes, which number ≤ 2 per
  stretch/run plus the toggles); O (OTHER-touching transitions, Theorem X, RESULTS R21 (g)); then Theorem X's transition bound
  O(n⁴(1 + X + O)) per phase; the number of phases (Lemma Φ, box 21, lane PROVED, unrefereed).

## 4. DATA (DATA, not proof; experiments/new/box41/xout.py, 2026-10-25 18:5xZ by date -u)
- Checks per OUT stretch: S4a crossings are entries, fallback crossings are evictions, X_S ≤ (|U| − 2)(f_S + 1) + f_S. 0 failures.
- (L) experiments/new/box41/lib41.txt (253 𝒞^1O files, canonical start): 271 OUT stretches, 253 crossings, 108 fallbacks inside
  stretches; max X_S = 31 with f_S = 0 at |U| = 48 (experiments/red/so/instances/post31_n48.pg; bound 46); max f_S = 9 (b5_os_n40, X_S 16).
- (R) `xout.py --rand 3000 6 20 4102 3`: 10,048 runs, 2,836 OUT stretches, 11 crossings, 2 fallbacks; max X_S 2.
