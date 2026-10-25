# N5 on o-cyclic 𝒞^1O, box 38 (c): NO-ENTRY-B is FALSE; breaks in case B are paid by low-class length rises (Lemma LOW-RISE, Theorem BRK-B)
L-NEW successor 17 (Opus 5.5, D15/D18), session_01ESR6bpU1r4ZjFsMExZtFpq. Box 38 GO by the Lead 12:00Z (Lead's stamp). Written
2026-10-25 12:4xZ onward by date -u.
- Setting and notation: as in docs/new/P-N5-OUT-box37.md §0 (sha1 9f032e61…, l-new b1a43578). N5 is SPEC S1-S5 on 𝒞^1O; a phase has
  λ_Ξ and τ constant; HN := H1 ∧ ¬H2; an HN stretch S is a maximal run of HN states of one phase; θ_S := θ-changes at transitions of S.
  Case A: rank(o) > rank(c_θ); case B: rank(c_θ) > rank(o) (then Ω(c_θ) is odd, P-N5-OUT §5 Setting).
- Labels (D18/L40): PROVED (L-NEW succ. 17, unrefereed), CONJECTURE, FALSE, OPEN, DATA. Nothing here is a running-time bound for N5,
  a TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN.

## Summary
1. **CONJECTURE NO-ENTRY-B is FALSE** (τ(o) = o, case B), from the canonical start.
   - Instance experiments/new/box38/instances/nebc_cex_n14.pg, sha1 399119afb8741f3689081389e70729891937df7b, n 14, o = 7,
     succ(o) = {2, 3, 7}. n5.py: 9 iterations / 5 fallbacks. check_sol2.py: "zielonka(oink zlk) OK strategies verified".
   - Also from a start pair (SPEC S3): neb_cex_n11.pg (+ .state), sha1 232b8951…, n 11.
   - So NO-ENTRY (P-N5-OUT §7) is FALSE as a general statement. It holds in case A with τ(o) = o (Theorem NO-ENTRY-A).
2. **Exact obstruction.** In case B, an R → R̄ gate at a fallback is length-only (CASE-B-LEN). When the fallback takes one, it raises an
   R̄-value by length alone. If that value is in the LOW CLASS C_θ := {(c_θ, P(θ), ℓ)}, it can overtake an F-value with the same cycle
   node and the same path set. The next S4a step then takes the new gate from F into R̄: an entry, with θ unchanged.
3. **Lemma LOW-RISE (PROVED).** In case B with τ(o) = o, starting at an HN fallback state a and with θ constant, the invariant INV_B
   ("no gate F → R̄"; "every R → R̄ gate is length-only") can first fail at a state t+1 only if some z ∈ R̄_t ∩ R̄_{t+1} makes a strict
   length rise inside C_θ at t → t+1.
4. **Theorem BRK-B (PROVED).** For every HN stretch S of a τ(o) = o phase (case A or B), the number of breaks is
   B_S ≤ θ_S + (n − 2)²(θ_S + 1). In case A, B_S ≤ θ_S (P-N5-OUT NE-COUNT (a)).
5. **Corollary OUT-1 (PROVED).** For a τ(o) = o phase with θ_ph θ-changes and T_ph H1-toggles, the out-of-SN fallbacks satisfy
   f_HN ≤ (K + 1)(2(n − 1)·D·(θ_ph + N_HN) + N_HN), where D := (n − 2)² + 1, K := n_E(2n − 1) and N_HN ≤ ⌊T_ph/2⌋ + 1.
   - This replaces the use of NO-ENTRY-B. Out-of-SN fallbacks and crossings of a τ(o) = o phase are poly(n)·(1 + θ_ph + T_ph), in both
     cases.
   - θ_ph stays OPEN.
6. **Dead ends** (intermediate CONJECTURES of this box, each killed):
   - NO-RR-B: "at a case-B τ(o) = o HN fallback state there is no R → R̄ gate";
   - NO-RISE-B: "a case-B fallback never raises an R̄-value";
   - the INV route for case B ("INV_B (i) propagates").
   All three die on nebc_cex_n14 (state 1: the fallback switches 3 from 7 to 6, an R → R̄ length-only switch; state 2 has the gate
   4 → 3 from F into R̄). §5 gives details.

## 1. The counterexample to NO-ENTRY-B (DATA, verified)
- nebc_cex_n14.pg (canonical start). rank(o) = 6 < rank(c_θ) = rank(12) = 8: case B. τ(o) = o from state 1 on (the phase starts at 1).
  θ = (12, ∅, 2) at states 1-3, all HN, all in one phase.
  - State 1: an Even fallback. Gates: (3, 6), (4, 3), (4, 11), (9, 0). The fallback evicts 4 and 9 (R = {1, 3, 4, 5, 6, 9, 10} →
    {1, 3, 5, 6, 10}). Vertex 3 ∈ R switches 7 → 6, a length-only R → R̄ gate: Ξ(3) = (12, ∅, 3) → (12, ∅, 4). This is a low rise
    (P = ∅ = P(θ)).
  - State 2: 4 ∈ F_2 with σ(4) = 11, Ξ_2(11) = (12, ∅, 3) ◁ Ξ_2(3) = (12, ∅, 4). The gate (4, 3) goes from F into R̄: INV (i) fails.
  - Transition 2 → 3 (S4a, in the phase, θ constant): 4 switches to 3 and enters R. This is a NO-ENTRY-B violation.
- neb_cex_n11.pg + neb_cex_n11.pg.state (start pair σ0 given, τ0(o) = o = 0). n5.py --start: 6 iterations / 2 fallbacks; check_sol2.py
  OK with strategies verified. rank(o) = 5 < rank(c_θ = 4) = 9.
  - Fallback at 0 → 1 evicts 2 and 7; vertex 3 rises by length alone, (4, {5}, 4) → (4, {5}, 5), with P(θ) = {5}.
  - At state 1 the gate (8, 3) appears (Ξ(σ 8) = Ξ(9) = (4, {5}, 4)). 1 → 2 is an S4a entry of 7 and 8; θ = (4, {5}, 3) is constant.
- How they were found (DATA): statesamp.py (state-level samples; §5), neb_aug.py (an added vertex y and a chain to x0 that copy an
  R̄-value's P and length), nebclimb.py (hill climb on (game, start)). Start-pair climbs (seeds 3831-3833, from the augmented state
  norise_state_n8) reached a violation within 30-1,700 mutations. The canonical climb (seed 3835, from
  experiments/n5-exhaustive/instances/b5_os_n14.pg) reached one after 26,758 mutations.

## 2. Lemma LOW-RISE (PROVED, L-NEW succ. 17; 𝒞^1O, τ(o) = o, case B)
Notation.
- x ≡_B y: lev(x, y) ≤ −1, i.e. the same cycle node and the same P (only the length may differ).
- Facts (as (T1)-(T3) of P-N5-OUT §5, with the level 0 in place of rank(o)):
  - (T1_B) if lev(x, y) ≥ 0, x′ ≡_B x and y′ ≡_B y, then lev(x′, y′) = lev(x, y) with the same verdict;
  - (T2_B) ≡_B-classes are intervals of ⊴;
  - (T3_B) z ⊕ · respects ≡_B.
- C_θ := {(c_θ, P(θ), ℓ) : ℓ ≥ 0}, the LOW CLASS. A LOW RISE at t → t+1 is a vertex z with Ξ_t(z), Ξ_{t+1}(z) ∈ C_θ and
  Ξ_t(z) ◁ Ξ_{t+1}(z).
- INV_B(t):
  - (i) no gate (y, z) ∈ Iσ_t with y ∈ F_t and z ∈ R̄_t;
  - (ii_B) every gate (v, z) ∈ Iσ_t with v ∈ R_t, z ∈ R̄_t has lev(Ξ_t(σ_t v), Ξ_t(z)) = −1.
Statement. Let S be an HN stretch of a τ(o) = o phase in case B, a ∈ S a state at which an Even fallback a → a+1 is taken, and t+1 ∈ S
with θ constant on [a, t+1] and INV_B(s) for all s ∈ [a, t]. Then:
- (a) no transition of [a, t+1] is an entry, and Ξ_{t+1}(z) ≡_B Ξ_t(z) for z ∈ R̄_{t+1};
- (b) (ii_B) holds at t+1;
- (c) if (i) fails at t+1, there is a low rise at some z ∈ R̄_t ∩ R̄_{t+1}, z ≠ o, at t → t+1.
Also INV_B(a) holds. So INV_B holds from a until the first state at which (i) fails, and that failure follows a low rise.
Proof.
- INV_B(a): (i) is FBL-N (iii) together with target o (P-N5-OUT §1 (b)); (ii_B) is CASE-B-LEN (P-N5-OUT §6).
- (a) As in P-N5-OUT §5 STEP, with ≡_B in place of ≡ and (ii_B) in place of (ii):
  - switched edges are gates (R15 (d)); by (i) at t none goes F_t → R̄_t, so there is no entry (ACT (i)) and R̄_{t+1} ⊆ R̄_t;
  - route form at the H1 states t and t+1 ((V1)), induction along the route at t+1: a forced or unswitched z keeps next_t(z); a switched
    z ∈ R_{t+1} ⊆ R_t took an R → R̄ gate (z, z′) at t (z′ ∈ R̄_{t+1} ⊆ R̄_t), so Ξ_t(z′) ≡_B Ξ_t(σ_t z) by (ii_B); (T3_B).
- (b) An R → R̄ gate (v, z) at t+1 with lev ≥ 0 transfers, by (a), (ii_B) at t if v switched, and (T1_B), to an R → R̄ gate at t with
  lev ≥ 0, against (ii_B) at t.
- (c) Let y ∈ F_{t+1} be Even, z ∈ R̄_{t+1}, with Ξ_{t+1}(z) ▷ Ξ_{t+1}(σ_{t+1} y). Write q := σ_{t+1}(y) ∈ F_{t+1}. In each case we show
  (★) Ξ_t(z) ⊴ Ξ_{t+1}(q) ◁ Ξ_{t+1}(z) and Ξ_t(z) ◁ Ξ_{t+1}(z).
  - y ∈ F_t. By (i) at t and z ≠ σ_t(y) (σ_t(y) ∈ F_t, z ∈ R̄_t), Ξ_t(z) ⊴ Ξ_t(σ_t y) ⊴ Ξ_t(q) ⊴ Ξ_{t+1}(q) (R15 (d): q ∈ {σ_t(y)} ∪ Iσ_t(y); R15 (a)).
    (★) follows.
  - y ∈ R_t, evicted at t → t+1. By SPLIT (a) an S4a step evicts nothing, so t → t+1 is a fallback, at which every Even vertex with a
    gate switches, to the gate target of largest Ξ_t (S4c). In all cases q ∈ {σ_t(y)} ∪ Iσ_t(y), so Ξ_t(σ_t y) ⊴ Ξ_t(q) ⊴ Ξ_{t+1}(q).
    - If Ξ_t(z) ⊴ Ξ_t(σ_t y), (★) follows.
    - If Ξ_t(z) ▷ Ξ_t(σ_t y), then z ≠ σ_t(y), so (y, z) is a gate at t. Then y switches, and Ξ_t(q) ⊵ Ξ_t(z) by the S4c rule. So
      Ξ_t(z) ⊴ Ξ_t(q) ⊴ Ξ_{t+1}(q) ◁ Ξ_{t+1}(z), and (★) follows.
  - From (★), (a) and (T2_B): Ξ_{t+1}(q) ≡_B Ξ_t(z) ≡_B Ξ_{t+1}(z). So P(Ξ_{t+1} z) = P(Ξ_{t+1} q).
  - q's honest play avoids o, so every vertex on it lies in F_{t+1}, and P(Ξ_{t+1} q) ⊆ F_{t+1}. On the other side,
    P(Ξ_{t+1} z) = (π_z ∩ V_{>c_θ}) ∪ P(θ) with π_z ⊆ R_{t+1}. Hence π_z ∩ V_{>c_θ} = ∅ and P(Ξ_{t+1} z) = P(θ) = P(Ξ_t z).
  - So Ξ_t(z), Ξ_{t+1}(z) ∈ C_θ and Ξ_t(z) ◁ Ξ_{t+1}(z): a low rise. z ≠ o, because Ξ(o) = θ does not change.
  - z ∈ R̄_t, since R̄_{t+1} ⊆ R̄_t. □

## 3. Theorem BRK-B (PROVED, L-NEW succ. 17; 𝒞^1O, τ(o) = o)
Statement. Let S be an HN stretch of a τ(o) = o phase, with B_S breaks and θ_S θ-changes.
- (a) Case B: B_S ≤ θ_S + LR_S, where LR_S counts the transitions of S with θ unchanged and a low rise.
- (b) LR_S ≤ (n − 2)²(θ_S + 1).
- (c) Hence B_S ≤ θ_S + (n − 2)²(θ_S + 1) = D(θ_S + 1) − 1 with D := (n − 2)² + 1. In case A, B_S ≤ θ_S (NE-COUNT (a)).
Proof.
- (a) Take a break with entry k → k+1. Let a → a+1 be the first eviction after the previous entry of S (or after the start of S). It
  is a fallback (SPLIT), and a < k.
  - By ACT (i) the entry needs a switched s ∈ F_k with σ_{k+1}(s) ∈ R̄_k, a gate, so INV_B (i) fails at k.
  - Let j0 be the first transition in [a, k] at which θ changes, if there is one. j0 ≠ a by F-FLAT.
  - Let t+1 ∈ (a, k] be the first state at which INV_B fails. If there is no θ-change in [a, t], LOW-RISE applies (INV_B holds on
    [a, t]: (ii_B) by (b) of the lemma) and gives a low rise at t → t+1, a transition in [a, k). Otherwise j0 ∈ (a, k] is a θ-change.
  - Charge the break to that transition. The intervals [a, k] of distinct breaks are disjoint (the next break's eviction comes after
    this entry). So B_S ≤ θ_S + LR_S.
- (b) Fix a maximal θ-constant run of S; P(θ) and c_θ are fixed on it, so C_θ is fixed.
  - Values only rise (R15 (a)), so a vertex that leaves C_θ upward never comes back, and inside C_θ its length can only increase
    (Ω(c_θ) odd: the longer one is better).
  - A value in C_θ belongs to a vertex z ∉ {o, c_θ} (Ξ(o) = θ, Ξ(c_θ) = (c_θ, ∅, 0) has length 0 and is not raised in the phase) and
    has length in [1, n − 1]. So each of the ≤ n − 2 vertices rises inside C_θ at most n − 2 times.
  - So the run has ≤ (n − 2)² transitions with a low rise. S has ≤ θ_S + 1 such runs. □
- Remark. Case A has no analogue of the low class: SEP-o separates every R̄-value from every F-value at the level rank(o)
  (P-N5-OUT §5), so (i) never fails, and B_S ≤ θ_S.

## 4. Corollary OUT-1 (PROVED, L-NEW succ. 17; 𝒞^1O, τ(o) = o, both cases)
Statement. For a phase with τ(o) = o, with θ_ph θ-changes and T_ph H1-toggles, and N_HN ≤ ⌊T_ph/2⌋ + 1 HN stretches (P-N5-OUT
NE-COUNT (c)):
- X_HN ≤ 2(n − 1)·D·(θ_ph + N_HN);
- f_HN ≤ (K + 1)(2(n − 1)·D·(θ_ph + N_HN) + N_HN).
Here X_HN counts the crossings with both ends in an HN stretch, and f_HN the in-phase fallbacks from HN states. In a τ(o) = o phase,
f_HN is all of its out-of-SN fallbacks, since every H1 state is HN.
Proof. EPOCH (P-N5-OUT §2) gives X_S ≤ 2(n − 1)(B_S + 1) ≤ 2(n − 1)·D(θ_S + 1) by BRK-B (c), and f_S + [exit fallback] ≤
(K + 1)(X_S + 1). Sum over the stretches, with Σ_S θ_S ≤ θ_ph. □
- Status: this replaces "given NO-ENTRY" in P-N5-OUT §7 for τ(o) = o, in both cases. θ_ph (θ-changes per phase) stays OPEN (the residual
  core). T_ph ≤ T* (RESULTS R34 (e)). Dependencies: those of P-N5-OUT (§0 table; FB-INT and KEY in review), plus LOW-RISE and BRK-B.
  Nothing uses (P).

## 5. Dead ends of this box (exact obstruction and instance)
- NO-RR-B (my CONJECTURE, 12:3xZ): "at a case-B τ(o) = o HN fallback state there is no R → R̄ gate". Library DATA supported it (0 gates
  in 15 such states; rrgate.py).
  - FALSE at state level: statesamp.py (seeds 3812-3814: 150,000 games each, n 4-10; seeds 3815-3817: 300,000 each, n 4-11; 6 random σ
    per game): 39 of 616 sampled case-B fallback states have one, every one length-only (lev −1, as CASE-B-LEN says).
  - FALSE on a canonical run: nebc_cex_n14 state 1 (gates (3, 6) and (4, 3) with 3, 4 ∈ R_1, 6 ∈ R̄_1).
- NO-RISE-B (my CONJECTURE): "a case-B fallback never raises an R̄-value (no R → R̄ switch that stays in R)". If true it would give
  NO-ENTRY-B through FREEZE-STEP / TAIL from a+1.
  - Rare at state level: 1 real rise in 413 case-B fallback states (seeds 3821-3823; many apparent R → R̄ switches evict their target
    in the same fallback). Instance experiments/new/box38/instances/norise_state_n8.pg + .state, sha1 c7462ba5….
  - FALSE on a canonical run: nebc_cex_n14 state 1 → 2 (3 rises from length 3 to 4 and stays in R).
- INV route for case B ("INV_B (i) propagates along a θ-constant run after a fallback"): FALSE, same instance, state 2 (gate (4, 3)).
  - Exact obstruction: a low rise at the fallback (LOW-RISE (c)).
  - Repair: charge breaks to low rises (BRK-B).
- Pitfall (method): statesamp.py first counted "R → R̄ switches" whose target the same fallback evicts. Those are evictions, not rises.
  The fixed version requires z ∈ R̄_a ∩ R̄_{a+1} with Ξ changed.

## 6. What is OPEN after this box
- θ-changes per HN stretch / per phase (θ_S, θ_ph): the residual core, unchanged.
- τ(o) ≠ o HN stretches: is there an analogue of NO-ENTRY-A / BRK-B with threshold c_w? Next item of box 38 (c).
- CONJECTURE (DATA, unexplored): the low rises of a θ-constant run are far fewer than (n − 2)². DATA: at most 2 per HN stretch in the
  library and climbs (lowrise.py).

## 7. Data and scripts (DATA; experiments/new/box38)
- Every script asserts exactly one Odd vertex of out-degree > 1 per game, and skips and counts non-𝒞^1O files.
- fbsplit.py (box 38 (a), P-N5-OUT §8). rrgate.py: R → R̄ gates at HN fallback states by case (library: case B τ(o) = o 15 states, 0
  gates; case A τ(o) = o 75 states, 1 with gates).
- statesamp.py: state-level samples (random 𝒞^1O game with o → o, τ(o) = o, random σ; keeps in-phase H1 fallback states).
- neb_aug.py: adds y and a chain to a state with a low rise. neb_run.py: NO-ENTRY check on runs (canonical or start pair).
  nebclimb.py: hill climb; score (violations, INV (i) failures, rises, case-B fallbacks); "-" as the state file means the canonical
  start.
- lowrise.py: checks LOW-RISE (c) at the first INV_B (i) failure, (ii_B), the charging of every break (θ-change or low rise in [a, k)),
  and B_S ≤ θ_S + n(n − 1)(θ_S + 1).
  - data/lowrise_lib.txt (library, rfroz_cex_n16, both counterexamples, all climb outputs): 75 case-A and 32 case-B fallback bases;
    7 case-B INV (i) failures, each with a low rise; 8 case-A and 9 case-B breaks, all charged; max 2 low rises per stretch; 0 failures.
- Instances (experiments/new/box38/instances): nebc_cex_n14.pg (399119af…), neb_cex_n11.pg (232b8951…) + .state (7b79ecd5…),
  norise_state_n8.pg (c7462ba5…) + .state (612b749c…). Climb logs: experiments/new/out/box38/nebclimb (gitignored).
