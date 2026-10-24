# N5 on o-cyclic 𝒞^1O, box 29: OTHER states (NH'), by clause pattern
L-NEW successor 10 (Opus 5.5, D15/D18). Lead GO 2026-10-24 18:1xZ, about 3 h. Written from 18:30Z (date -u).
- Labels (L40): PROVED (L-NEW, unrefereed unless stated), READING, CONJECTURE, OPEN, DATA.
- Scope: N5 on 𝒞^1O, inside one joint λ-phase with τ fixed (a PHASE), notation of P-N5-X-box28.md §0. These are lemmas about the
  candidate. They are not a running-time bound, not a TARGET.md claim, and not a step-4 pass. G-N5-TIME stays OPEN.
- The pinned packet P-N5-X (trunk afc88b0) is not edited.
- Code: experiments/new/box29/. It imports box28/fbre.py, box28/nhprof.py and box25/common.py.
- OTHER := (h) fails and Ξ ≠ W. A crossing-free interval I is a maximal run of states of a phase with R constant. F := V \ R, with
  o ∈ R.

## 0. Results in short
- PROVED (L-NEW): Lemma F1° (§1). Lemma F1 of P-N5-X holds on every crossing-free interval, OTHER states included: the values on F
  change at ≤ |F| − 1 transitions.
- PROVED (L-NEW): Lemma TC (§2). On a crossing-free interval:
  - H1 ⟺ λ_Ξ(o) ∈ F, and H2 ⟺ τ(o) ∈ F, so both are constant;
  - under H2, H3 is constant too, and the interval is OTHER at every state or at none;
  - under H1 ∧ ¬H2 it is OTHER at every state;
  - under ¬H1 ∧ ¬H2, EQ ⟺ θ = w, and each EQ → OTHER switch changes w.
  So OTHER blocks are few, and they cannot alternate with EQ / THR except through changes of w in the case ¬H1 ∧ ¬H2.
- PROVED (L-NEW): Lemma P3′ (§3, the route-form, honest-higher case). When both frames are in ROUTE FORM and the honest cycle node
  c_θ = λ_Ξ(o) is more relevant than c_w = λ_W(o), there are ≤ (n + 1)|R| R-value changes per (θ, w)-piece.
  - The proof is a coarse freeze above c_θ (Lemma CR's argument), after which only route LENGTHS move, monotonically.
  - Route form covers patterns "3" (H1 ∧ H2 ∧ ¬H3) and "13" with λ_Ξ(o) = o (the most frequent OTHER configuration in random runs).
- READING (§4): with Theorem X, (NH') reduces to two residual counts per crossing-free interval:
  - (R-ONLY) value changes on R inside OTHER blocks;
  - (W-CYC) changes of w under ¬H1 ∧ ¬H2.
  P3′ bounds (R-ONLY) in its case. The uncovered cases are listed exactly in §5.
- DATA (§6): every R-only count seen is ≤ |R|. The climbs' large O′ counts are mostly F-changes, which F1° already bounds.
  - The best O′ climb at n 32 (26 O′ transitions) has |R| = 1.
  - The n 16 climb has 20 O′ = 10 F-changes + 10 R-only, split by 2 crossings.
- READING (§7), the outside views asked for in GO (c): the hitting-time view is exactly what makes P3′ work. Discounted limits and
  well-quasi-orders give termination only.

## 1. Lemma F1° (PROVED, L-NEW): F-values on a crossing-free interval, OTHER states included
Statement. On a crossing-free interval I of a phase, the transitions at which Ξ changes at some vertex of F number at most |F| − 1.
Proof. This is P-N5-X §5 (Lemma F1) with two steps re-checked for OTHER states.
- Step 2 (the gate on F). For x, z ∈ F, (x, z) ∈ Iσ_k iff it is W-improving. Reason: Ξ = W on F at EVERY state (Lemma G (a), which
  needs no (h)).
- Step 4 (fallbacks). An S4c step inside I is Even's (τ fixed).
  - Its switched edges from F are flat F-edges (FBL-N (ii), no (h)). An edge from F into R would be a crossing.
  - So the F-vertices switch only flat F → F edges, and the F-values do not change.
  - Switches of R-vertices do not affect F, because F-plays avoid R.
  - So Lemma P's invariant on 𝓕 carries over with j unchanged.
- Steps 1, 3, 5 and 6 are unchanged: F is closed and has no Odd choice; S4a's optimum restricted to F is an 𝓕-arena optimum; λ on F
  is λ_Ξ, fixed in the phase; R17 on 𝓕. □

## 2. Lemma TC (PROVED, L-NEW): the clauses of (h) on a crossing-free interval
Statement. Let I be a crossing-free interval of a phase.
- (i) H1 ⟺ λ_Ξ(o) ∈ F, and H2 ⟺ τ(o) ∈ F. Both are constant on I.
- (ii) If H2 holds on I, then λ_W(o) = λ_Ξ(τ(o)) is fixed in the phase. So H3 and (h) are constant on I, and either every state of I
  is OTHER or none is.
- (iii) If H1 ∧ ¬H2 holds on I, every state of I is OTHER.
- (iv) If ¬H1 ∧ ¬H2 holds on I: a state is EQ iff θ = w, and at every transition EQ → OTHER inside I, w changes.
Proof.
- (i)
  - H1 holds iff the honest play from o does not return to o. Then e* := σ̄(o) ∈ F: if e*'s σ-play reached o, the honest play
    would return to o, since Odd chooses only at o. F is closed, so the honest cycle, and λ_Ξ(o), lies in F.
  - If H1 fails, the honest cycle passes o. Every vertex of it reaches o, so the cycle lies in R and λ_Ξ(o) ∈ R.
  - H2: the same with τ(o) in place of e*. τ(o) = o counts as "in R".
  - λ_Ξ(o) is fixed in the phase, τ is fixed, and F is fixed on I. So both clauses are constant.
- (ii) Under H2, o's W-play does not return to o, so o is not its own W-cycle node. Then λ_W(o) = λ_W(τ(o)) = λ_Ξ(τ(o)) (Ξ = W on
  F, τ(o) ∈ F), which is fixed in the phase.
  - So H3 (λ_Ξ(o) = λ_W(o)) is constant, and with (i) so is (h).
  - If (h) fails on I, no state of I is EQ: Ξ(o) = W(o) needs λ_Ξ(o) = λ_W(o) ∈ F, which gives H1 by (i) and H3, i.e. (h). So
    every state is OTHER.
  - If (h) holds, no state is OTHER by definition.
- (iii) λ_Ξ(o) ∈ F and λ_W(o) ∈ R (the W-cycle passes o). These differ, so Ξ(o) ≠ W(o), and (h) fails: every state is OTHER.
- (iv) Both cycles pass o: C_Ξ = o → e* → π_{e*} → o, and C_W = o → τ(o) → π_{τ(o)} → o.
  - "EQ ⇒ θ = w" is trivial. Conversely, let θ = w. Then c := λ_Ξ(o) = λ_W(o) lies on both cycles, and o's two paths to c have the
    same path set above c and the same length.
  - v ∈ F: Ξ(v) = W(v) (Lemma G (a)).
  - v ∈ R, c on v's route π_v: both plays coincide until o, so both reach c first. In both frames v's cycle node is c (c lies on
    both cycles), with the same path. So Ξ(v) = W(v).
  - v ∈ R, c not on π_v:
    - In each frame, v's path to c is π_v followed by o's path to c in that frame.
    - That o-path is disjoint from π_v: π_v meets C_Ξ in a final segment [u..o], and c ∉ [u..o]; the same holds for C_W.
    - By (V1) along π_v, Ξ(v) and W(v) differ only through o's two paths to c, which have equal keys. So Ξ(v) = W(v).
  - So θ = w ⇒ Ξ = W.
  - EQ → OTHER at k → k+1: θ_k = w_k. If w_{k+1} = w_k, then θ_{k+1} = w_{k+1} (XW3 of P-N5-X), so k+1 is EQ, a contradiction. □
- Consequence. On I the number of maximal OTHER blocks is ≤ 1, except under ¬H1 ∧ ¬H2, where it is ≤ 1 + #(changes of w in I).
- DATA (tccheck.py): every clause of (i)-(iv) checked; 0 failures.
  - Named instances: op20, op32, op16, oc24_s4_final, wd16_s2, x32_sc32_final.
  - Random runs: seeds 2951/2952, 5,624 runs, 1,133 crossing-free in-phase transitions, 5,710 state checks for (v).

## 3. Lemma P3′ (PROVED, L-NEW): route form with the honest cycle node higher
Definitions on a crossing-free interval I.
- The honest frame is in ROUTE FORM if H1 holds or λ_Ξ(o) = o.
  - Then for every v ∈ R, Ξ(v) = π_v ⊕ θ: under H1 by Lemma G (b)'s honest half (it uses only H1); if λ_Ξ(o) = o, v's honest path to
    its cycle node o is π_v.
  - θ is F-determined under H1 (θ = o ⊕ min over exits e ∈ F of Ξ(e), since σ̄(o) ∈ F attains the minimum). If λ_Ξ(o) = o,
    θ = (o, ∅, 0) is constant.
- The W frame is in route form if H2 holds or λ_W(o) = o.
  - Then W(v) = π_v ⊕ w on R.
  - w is F-determined under H2 (w = o ⊕ Ξ(τ(o)), as in P-N5-X Lemma F2), and constant while λ_W(o) = o.
- A (θ, w)-PIECE of I: a maximal sub-interval on which both frames are in route form and θ, w are constant.
  - c_θ := λ_Ξ(o) and c_w := λ_W(o) are then constant.
  - Under H2 on I, I has ≤ |F| pieces: θ and w change only with F-values (F1°), and the route-form status is constant (TC (i),
    and λ_Ξ(o) is fixed in the phase).
Statement. On a (θ, w)-piece J with c_θ strictly more relevant than c_w, the transitions with a Ξ-change at some vertex of R number
at most (n + 1)|R|.
Proof.
1. Routes and orders. Every R-vertex's value is a function of its route π_v (path to o): Ξ(v) = π_v ⊕ θ and W(v) = π_v ⊕ w.
   - The honest order on routes compares A_θ(π) := route vertices above c_θ (top of the symmetric difference, by its parity), then
     the length (parity of c_θ).
   - The W order does the same with c_w.
   - Let κ(π) := A_θ(π), the route vertices above c_θ. c_θ is the more relevant node, so every vertex above c_θ is above c_w. Hence a
     κ-strict comparison is decided the same way in both orders.
2. Coarse freeze (Lemma CR's argument, P-N5-XA §5, run on the route game with terminal o): κ(π_v) is constant for all v ∈ R from
   the |R|-th transition of J on.
   - Lemma P^κ: for every simple route r of ≤ j edges from x to o, κ(π_x) at state k_0 + j is ⪰ κ(r).
   - Base: r = (o).
   - Case A (no κ-strict improvement from x): (V2) on κ and κ-monotonicity of Ξ (R15 (a)).
   - Case B (κ-strict edge (x, z)):
     - The edge is honest-improving, so it is a gate edge, and it is W-improving (step 1). The S4a optimum dominates σ_k[x → z]
       ((F1) in G_τ).
     - If x lies on π_z, the case analysis is B2 of CR. W's cycle-node map is constant on J: c_w on R, λ_Ξ on F.
     - At S4c steps only κ-monotonicity is used (R15 (a)).
   - Squeeze with the current route (a simple route of ≤ |R| edges).
3. After the freeze, A_θ(π_v) is constant for every v ∈ R. So Ξ(v) = π_v ⊕ θ changes only through |π_v| ∈ [1, n − 1], monotonically
   (Ξ is non-decreasing; the direction is the parity of c_θ). Each R-vertex has ≤ n − 1 such changes.
4. Total: ≤ |R| (before the freeze) + (n − 1)|R| + |R| ≤ (n + 1)|R| transitions with an R-value change. □
- Remarks.
  - c_θ = c_w with both frames in route form: the two orders coincide. That is the THR situation, where Lemma G (c) and PIECE give
    ≤ |R| − 1.
  - c_w more relevant: step 2 still holds with κ := route vertices above c_w, but after the freeze the honest order still sees the
    vertices between c_θ and c_w (V_mid), while the W order sees only lengths. Step 3 fails. This is OPEN case (U1) in §5.
- DATA (p3check.py, rfcheck.py):
  - Pattern-3 pieces with transitions are nearly absent in random runs (2 pieces in 10,000 runs). Freeze checks: 0 failures.
  - The O′ climb best at n 32 is pattern 13 with c_θ = o and c_w HIGHER, case (U1). Its activity is in F (|R| = 1), so F1° bounds it.

## 4. The reduction (READING: an assembly of §1-§3 with Theorem X, P-N5-X §7)
Per phase, the transitions are poly(n) · (1 + X + Σ over crossing-free intervals I of (ROI(I) + WC(I))), where:
- X is the number of crossing transitions (Theorem X);
- ROI(I) is the number of transitions in OTHER blocks of I that change values on R ∪ {o} only (R-ONLY);
- WC(I) is the number of changes of w in I when ¬H1 ∧ ¬H2 holds on I (W-CYC), and 0 otherwise.
Sketch.
- On I, F-value changes are ≤ |F| − 1 (F1°).
- OTHER blocks are ≤ 1 + WC(I) (TC).
- Between OTHER blocks, the EQ / THR parts of I are F-intervals in P-N5-X's sense: ≤ 3n² value changes each (Theorem X, steps
  2-5).
- Inside an OTHER block, a value-changing transition changes an F-value (≤ |F| − 1 in all) or is R-only (ROI).
- Value-preserving runs are ≤ 4n(n − 1) (R15 (d)). □
- P3′ bounds ROI on its pieces. The rest is §5.

## 5. What is left of (NH'), exactly (OPEN)
- (U1) Route form in both frames with c_w more relevant than c_θ. After the coarse freeze, the honest order compares the route
  vertices between c_θ and c_w (V_mid); the W order compares only lengths. A bound needs either:
  - "no crossing-free fallback at OTHER states" (DATA: 0 seen, §6) together with a bound on W-tie switches; or
  - a V_mid potential.
- (U2) Honest frame not in route form: ¬H1 with λ_Ξ(o) ≠ o (patterns 13, 123, 12 with the honest cycle node elsewhere on the
  honest cycle). Honest values are then paths to c_θ in the graph with o fixed to σ̄(o). Vertices reaching c_θ before o and those
  reaching o first are valued differently.
- (U3) W frame not in route form: ¬H2 with λ_W(o) ≠ o (patterns 23, 123, 12). W is the valuation of the closed one-player subgame
  on R, with o's W-cycle inside R.
- (W-CYC) Under ¬H1 ∧ ¬H2, w is a cycle value inside R. It is monotone at arena steps (Lemma W); its changes are not otherwise
  bounded.
- CONJECTURE (OB_R): in a crossing-free interval, each OTHER block has ≤ |R| R-only value-changing transitions.
  - DATA: max R-only = |R| − 3 (op20: 16 with |R| = 19) and |R| − 1 (op16: 10 with |R| = 11). orclimb.py is the attack (§6).
- Unified view behind (U1)-(U3), READING. In each frame, the value of v ∈ R is v's path to that frame's cycle node, in the graph
  where o is fixed to that frame's exit (σ̄(o) or τ(o)). So N5 on R is a "two-target route game": the honest target gates, the W
  target selects. P3′ is the case where both targets are reached through o and the honest target is the more relevant.

## 6. Data (DATA; experiments/new/box29/; every cited best checked with n5.py + check_sol2.py: Oink zlk OK, strategies verified)
- otherx.py: OTHER-touching transitions split into crossing ones (charged to X) and O′ (non-crossing).
  - Named: wd16_s2, 12 OTHER-touching transitions, all crossings, so O′ = 0. oc16_s2: 16, of them 13 O′. oc24_s4_final: 19, all O′.
  - Every O′ transition seen is an arena step: 0 crossing-free fallbacks at OTHER states in all runs (seeds 2931/2932, 6,913 runs,
    and all named).
- dstat.py: the disagreement set D = {v : Ξ(v) ≠ W(v)} at OTHER states. In random runs D = {o} is the most frequent (patterns 13
  with c_θ = o, 3, 23); the climbed instances have |D| > 2.
- throttle.py / odep.py: at OTHER states, throttled edges (W-improving, not in the gate) occur in about half the states. Many are
  GENUINE (neither into o nor out of a vertex pointing to o), and o-dependent vertices are common. So OTHER blocks are NOT Lemma-EQ
  runs in disguise.
- oblock.py, CONJECTURE (OB), "each OTHER block in a crossing-free interval has ≤ n − 1 value changes": 0 failures; max excess −3.
  - Random runs: seeds 2911/2912, 5,296 runs, 2,553 blocks. Named: op16 / op20 / op32 / oc24 / wd16.
- rsplit.py (F-changing vs R-only O′):
  | instance | n | phase O′ | F-changing | R-only | |R| |
  | --- | --- | --- | --- | --- | --- |
  | op32_r climb best | 32 | 26 | 26 | 0 | 1 |
  | op20_r climb best | 20 | 16 | 0 | 16 | 19 |
  | op16 (seeded from oc16_s2) | 16 | 20 | 10 | 10 | 11 |
- Climbs: opclimb.py (O′ per phase) and orclimb.py (R-only O′). Final numbers are in §8 at the end of the box.

## 7. Outside viewpoints (Lead GO (c)) (READING)
- Hitting times on the play graph. With positional strategies the play graph is a functional graph, and |π_v| is the hitting time
  of o from v. P3′'s step 3 is exactly a hitting-time argument: once the coarse level above the deciding cycle node is frozen,
  values are decided by hitting times, which lie in [1, n − 1] and move monotonically. So a polynomial-height potential exists
  wherever the deciding comparison reduces to a hitting time. The obstruction (U1) is the opposite: the deciding comparison is a
  SET comparison over V_mid, which has no polynomial-height monotone measure by itself. This is why OTHER blocks are short in the
  data: in every instance seen, they live in the hitting-time regime (single-vertex arena steps building one path).
- Discounted or mean-payoff limits. VJ00 valuations are the lexicographic limit of discounted values with rewards of size n^{O(d)}
  (the reduction recorded in this notebook's sources, Friedmann arXiv 1106.0778 §9). The clauses H1 / H2 of Lemma TC are
  recurrence of o in each frame's play. A discounted potential Σ_v Ξ_γ(v) increases at every value-changing step, but its gap is
  only exponentially small in n. So this view gives termination (as R15 does), not a polynomial bound.
- Well-quasi-orders. A wqo argument on states would also prove only termination. It yields no polynomial height of the state
  sequence, so it cannot address G-N5-TIME by itself.
