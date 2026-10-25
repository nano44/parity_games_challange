# N5 on o-cyclic 𝒞^1O, box 38 (c): τ(o) ≠ o HN stretches; NO-ENTRY-A and BRK-B whenever o tops its W-cycle (c_w = o); NO-ENTRY FALSE when c_w ≠ o; every break is paid by a θ-change or an R̄-value rise (Lemma RISE)
L-NEW successor 17 (Opus 5.5, D15/D18), session_01ESR6bpU1r4ZjFsMExZtFpq. Box 38 (c), second item (Lead's brief: "τ(o) ≠ o with
threshold c_w"). Written 2026-10-25 13:0xZ onward by date -u.
- Setting: as in docs/new/P-N5-OUT-box37.md §0 (sha1 9f032e61…) and docs/new/N5-NEB-box38.md (sha1 047bfeb5…). N5 is SPEC S1-S5 on
  𝒞^1O; HN := H1 ∧ ¬H2; an HN stretch S is a maximal run of HN states of one phase; B_S counts its breaks and θ_S its θ-changes.
- New notation:
  - At an HN state, o lies on its W-cycle C_W (¬H2). c_w := the most relevant vertex of C_W, so w = W(o) has cycle node c_w.
  - "o TOPS ITS W-CYCLE" means c_w = o. With τ(o) = o this always holds (C_W = {o}).
  - Case A: rank(o) > rank(c_θ). Case B: rank(c_θ) > rank(o).
  - An R̄-RISE at t → t+1 is a vertex z ∈ R̄_t ∩ R̄_{t+1}, z ≠ o, with Ξ_t(z) ◁ Ξ_{t+1}(z).
  - A HIGH RISE has lev(Ξ_t z, Ξ_{t+1} z) ≥ rank(o). A LOW RISE has both values in C_θ = {(c_θ, P(θ), ℓ)} (N5-NEB §2).
- Labels (D18/L40): PROVED (L-NEW succ. 17, unrefereed), CONJECTURE, FALSE, OPEN, DATA. Nothing here is a running-time bound for N5,
  a TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN. Nothing uses (P).

## Summary
1. **Lemma RISE (PROVED; any τ(o), any case).** Let a be an HN fallback state. Inside the HN stretch with θ constant, the first state
   t+1 > a that has a gate from F into R̄ is preceded by an R̄-rise at t → t+1. Hence B_S ≤ θ_S + RR_S, where RR_S counts the
   transitions of S with θ unchanged and an R̄-rise.
2. **Lemma HIGH-RISE (PROVED; case A, any τ(o), any c_w).** In case A that rise is a high rise (lev ≥ rank(o)). The proof uses only
   SEP-o, which is a fact about the honest frame and does not depend on τ(o).
3. **Theorem NO-ENTRY-A′ (PROVED; case A, c_w = o at the fallback, any τ(o)).** P-N5-OUT's NO-ENTRY-A holds verbatim. The new step is
   a W-argument for a switched vertex v on C_W (Case 1′ below).
4. **Theorem BRK-B′ (PROVED; case B, c_w = o at the fallback, any τ(o)).** CASE-B-LEN, LOW-RISE and BRK-B (N5-NEB §2-§3) hold verbatim,
   with the same Case 1′ in the W-argument.
5. **NO-ENTRY is FALSE when c_w ≠ o, in both cases, from the canonical start.**
   - experiments/new/box38/instances/tauw_A_cex_n24.pg (case A), sha1 e29908d546d62e64903b41aa987351c3b3c68a62. n 24.
     n5.py: 16 iterations / 3 fallbacks. Oink zlk OK, strategies verified.
   - experiments/new/box38/instances/tauw_B_cex_n24.pg (case B), sha1 c0ad4f0ca6ce9a35d3c89b377e686eef58dc3845. n 24.
     n5.py: 10 iterations / 4 fallbacks. Oink zlk OK, strategies verified.
6. **Exact obstruction (c_w ≠ o, case A).** The W frame of an R-vertex has threshold c_w. An honest top difference whose rank lies in
   the BAND (rank(o), rank(c_w)) is invisible to W. So Step (K) does not exclude an honest R → R̄ gate at that level at a fallback.
   - Library instance: experiments/new/box35/instances/fbrestart_cex_n24.pg (sha1 a0aacfba…), state 10, with o = 19 (rank 12),
     τ(o) = 9, C_W = 19 → 9 → 7 → 6 → 19, c_w = 7 (rank 21), c_θ = 0.
   - Fallback gates 13 → 2, 23 → 20 and 6 → 20 have their honest top difference at vertex 12, rank 19, inside the band.
   - In tauw_A_cex_n24 the high rise that precedes the entry is at rank 19, inside the band (17, 21).
7. **Corollary BRK-ALL (PROVED).** For every HN stretch S, whatever τ(o) is:
   B_S ≤ θ_S + (n − 2)²(θ_S + 1) + RW_S.
   - RW_S counts the transitions with θ unchanged and an R̄-rise that lie between a break's eviction a and its entry, for the breaks
     whose eviction state has c_w(a) ≠ o.
   - When c_w(a) = o at every eviction state (in particular when τ(o) = o), RW_S = 0, and Corollary OUT-1 (N5-NEB §4) holds for the
     phase.
   - OPEN: R̄-rises after a c_w ≠ o fallback; in case A they are high rises, at levels in the band in the data.

## 1. Lemma RISE (PROVED, L-NEW succ. 17; 𝒞^1O, any τ(o))
Statement. Let S be an HN stretch, a ∈ S a state at which an in-phase Even fallback a → a+1 is taken, and t+1 ∈ S with θ constant on
[a, t+1]. Suppose no state in [a, t] has a gate (y, z) ∈ Iσ with y ∈ F and z ∈ R̄, and state t+1 has one. Then some z ∈ R̄_t ∩ R̄_{t+1},
z ≠ o, has Ξ_t(z) ◁ Ξ_{t+1}(z).
Proof.
- No entry on [a, t+1]: switched edges are gates (R15 (d)), none goes F → R̄ at states a..t, so ACT (i) gives R̄_{s+1} ⊆ R̄_s.
- Let (y, z) be the gate at t+1, with y ∈ F_{t+1}, z ∈ R̄_{t+1} ⊆ R̄_t, and q := σ_{t+1}(y) ∈ F_{t+1}. We show
  (★) Ξ_t(z) ⊴ Ξ_{t+1}(q) ◁ Ξ_{t+1}(z).
  - y ∈ F_t. There is no gate F → R̄ at t, and z ≠ σ_t(y) (σ_t(y) ∈ F_t). So Ξ_t(z) ⊴ Ξ_t(σ_t y) ⊴ Ξ_t(q) ⊴ Ξ_{t+1}(q), by R15 (d)
    (q ∈ {σ_t(y)} ∪ Iσ_t(y)) and R15 (a).
  - y ∈ R_t. By SPLIT (a) an S4a step evicts nothing, so t → t+1 is a fallback. Again Ξ_t(σ_t y) ⊴ Ξ_t(q) ⊴ Ξ_{t+1}(q).
    - If Ξ_t(z) ⊴ Ξ_t(σ_t y), (★) follows.
    - Otherwise (y, z) is a gate at t (z ≠ σ_t(y)), y switches, and S4c gives Ξ_t(q) ⊵ Ξ_t(z). (★) follows.
- So Ξ_t(z) ◁ Ξ_{t+1}(z); z ≠ o since Ξ(o) = θ is constant. □
- Charging (as BRK-B (a), N5-NEB §3). Every break has, in its interval [a, k] (a its eviction, k its entry), either a θ-change at a
  transition in (a, k] (not at a, by F-FLAT) or, by RISE applied at the first gate F → R̄ after a, an R̄-rise at a transition in [a, k).
  These intervals are disjoint. So B_S ≤ θ_S + RR_S.
- Remark. The general count of R̄-rises with θ fixed is a count of route improvements inside R. ROUTE-FROZEN (rfroz_cex_n16) shows that
  such rises occur after fallbacks. No polynomial bound is known in general (OPEN).

## 2. Lemma HIGH-RISE (PROVED, L-NEW succ. 17; case A, any τ(o), any c_w)
Statement. In RISE, if the phase is in case A, the rise can be taken with lev(Ξ_t z, Ξ_{t+1} z) ≥ rank(o).
Proof.
- SEP-o (P-N5-OUT §5) at the H1 states t and t+1 gives o ∈ P(Ξ_t z) and o ∈ P(Ξ_{t+1} z) (z ∈ R̄ at both), and o ∉ P(Ξ_{t+1} q)
  (q ∈ F_{t+1}). SEP-o uses only the honest route form and rank(o) > rank(c_θ); τ(o) does not enter.
- So in (★) both comparisons are at levels ≥ rank(o), and the first is strict: Ξ_t(z) ◁ Ξ_{t+1}(q) ◁ Ξ_{t+1}(z).
- (filled in: lev along a strict chain) If x ◁ y ◁ w, then lev(x, w) = max(lev(x, y), lev(y, w)). If the two levels differ, the larger
  decides x against w. They cannot be equal at a vertex level: x and y would differ in membership of that vertex, and so would y and w,
  so x and w would agree on it. Then y holds the membership Even prefers (x ◁ y) and also the one Even does not prefer (y ◁ w), a
  contradiction.
- So lev(Ξ_t z, Ξ_{t+1} z) ≥ rank(o). □

## 3. Theorem NO-ENTRY-A′ (PROVED, L-NEW succ. 17; case A, c_w(a) = o, any τ(o))
Statement. P-N5-OUT §5's Theorem NO-ENTRY-A, with "τ(o) = o" replaced by "o tops its W-cycle at the fallback state a (c_w(a) = o)".
Proof. P-N5-OUT §5's proof uses τ(o) = o in three places. Only BASE (ii) needs new work.
- (1) XW gives θ ⊴ w. Here w = W(o) = (o, ∅, 0), since o is the cycle node of its own W-play. With c_θ ≠ o (H1), reward(c_θ) < reward(o);
  in case A, Ω(o) is even.
- (2) W-values on R̄_a. For r ∈ R̄_a, r's W-play first reaches o after its route π_r (if π_r meets C_W, it follows C_W to o; c_w = o is the
  cycle node). No vertex of π_r is a cycle node, so W_a(r) = π_r ⊕ (o, ∅, 0) = (o, π_r ∩ V_{>o}, |π_r|).
- (3) BASE (ii). Let (v, z) be an R → R̄ gate at a with ℓ := lev(Ξ_a(σ_a v), Ξ_a(z)) ≥ rank(o), and u the top of
  D := (π_z Δ π_{σ_a v}) ∩ V_{>c_θ}. Then rank(u) > rank(o).
  - Case 1: z's route avoids v, and v ∉ C_W. Switching v changes neither z's play nor o's W-play, so W at v becomes v ⊕ W_a(z). By (2)
    and the shared top u, this is ▷ W_a(v), as in P-N5-OUT §5 Case 1.
  - Case 1′ (new): z's route avoids v, and v ∈ C_W ∖ {o}.
    - Write C_W as o = c_0 → c_1 → … → c_m → o, with v = c_i. Then π_{σ_a v} = c_{i+1} … c_m, all of rank < rank(o) (c_w = o).
    - If π_z meets C_W, it does so at some c_j with j > i (else it would pass v), and then contains c_j … c_m.
    - After the switch, v's W-play is v → z → π_z → o → c_1 → … → c_i = v, a cycle Z.
    - u ∉ π_{σ_a v} (rank(u) > rank(o)), so u ∈ π_z: u is on z's side, and Ω(u) is even (the gate is Even-improving).
    - Top of Z. C_W lies below o. A vertex of π_z of rank > rank(u) would lie above c_θ and outside π_{σ_a v}, so it would be in D,
      against the choice of u. So the top of Z is u, and the new W(v) has cycle node u with reward p′(u) > p′(o) = reward(o).
    - W_a(v) has cycle node o. So the switch raises W at v.
  - Case 2: z's route passes v, π_z = q · v · π_{σ_a v}. As in P-N5-OUT §5: D = (q ∪ {v}) ∩ V_{>c_θ} is on z's side, and the closed cycle
    v → z → q → v has top u, which is even. W at v rises. (If v ∈ C_W, o's W-play also changes; only W at v matters.)
  - In every case an arena edge raises W at v at the fallback, against Step (K) (RESULTS R23 (a)).
- STEP (P-N5-OUT §5) uses only the honest frame (SEP-o, route form, R15 (a), (d), ACT (i), SPLIT), so it holds for every τ(o). □
- Consequence. A break whose eviction state a has c_w(a) = o, in case A, has a θ-change in (a, k] (NE-COUNT (a)).

## 4. Theorem BRK-B′ (PROVED, L-NEW succ. 17; case B, c_w(a) = o, any τ(o))
Statement. CASE-B-LEN (P-N5-OUT §6), LOW-RISE and BRK-B (N5-NEB §2-§3) hold with "τ(o) = o" replaced by "c_w(a) = o at the fallback
state a".
Proof.
- (1) and (2) of §3 hold unchanged. So reward(o) > reward(c_θ), and in case B, Ω(c_θ) is odd.
- CASE-B-LEN′. Its proof is §3 (3) with "rank(u) > rank(c_θ) > rank(o)" in place of "rank(u) > rank(o)". In Case 1′,
  π_{σ_a v} ⊆ C_W lies below o, hence below c_θ, so u ∈ π_z again.
- LOW-RISE and BRK-B use only the honest frame after the base. □
- So for breaks whose eviction state has c_w = o: in case A they are charged to θ-changes, and in case B to θ-changes or low rises
  (≤ (n − 2)² per θ-constant run).

## 5. NO-ENTRY for τ(o) ≠ o is FALSE when c_w ≠ o (DATA, verified)
- tauw_A_cex_n24.pg (case A; canonical start; nebclimb MODE=TAUW seed 3841 from fbrestart_cex_n24).
  - inv2.py: 2 fallback bases with c_w ≠ o and 9 NO-ENTRY violations (entries after a fallback with θ constant, HN, in the phase).
  - At the first INV (i) failure (base a = 4, failure at 5), vertex 3 makes a high rise at rank 19. rank(o) = 17 and rank(c_w) = 21: a
    band rise.
  - n5.py 16 iterations / 3 fallbacks; check_sol2.py "zielonka(oink zlk) OK strategies verified".
- tauw_B_cex_n24.pg (case B; canonical start; MODE=TAU seed 3843).
  - inv2.py: 4 fallback bases with c_w ≠ o, 10 violations, 3 INV (i) failures, none preceded by a LOW rise (LOW-RISE needs c_w = o),
    each preceded by an R̄-rise (RISE).
  - n5.py 10 iterations / 4 fallbacks; check_sol2.py OK, strategies verified.
- So every remaining case of NO-ENTRY is FALSE: case A with c_w ≠ o, and case B whatever c_w is (N5-NEB §1 for c_w = o). The proved
  cases are exactly case A with c_w = o (NO-ENTRY-A′).

## 6. What is OPEN after this box
- RW_S: R̄-rises after a c_w ≠ o fallback.
  - In case A they are high rises (HIGH-RISE); in the data they lie in the band (rank(o), rank(c_w)).
  - CONJECTURE BAND (DATA: the one high rise found; too thin to bound anything): after a c_w ≠ o fallback in case A, R → R̄ gates and
    R̄-rises have levels < rank(c_w).
  - Even if BAND holds, a count of band rises is not polynomial in general: the band can hold Θ(n) vertices, and P-subsets of it are
    exponentially many. A useful bound needs structure (for example, a band-level analogue of the low class).
- θ-changes per HN stretch / phase (θ_S, θ_ph): the residual core, unchanged.
- HN stretches per phase for τ(o) ≠ o (P-N5-OUT §7 (2)), and OTHER states.

## 7. Data and scripts (DATA; experiments/new/box38)
- taunot.py: τ(o) ≠ o HN fallback states by case and c_w = o or not; R → R̄ gate levels against rank(o); whether routes meet C_W.
  Library: case A c_w = o 9 states, 0 gates; case A c_w ≠ o 2 states, 9 gates at lev ≥ rank(o) (8 with a route meeting C_W); case B
  c_w ≠ o 4 states.
- inv2.py: at every HN fallback base (any τ(o)) it checks the following.
  - NO-ENTRY-A′ INV (i), (ii) when c_w = o in case A.
  - (ii_B) and the low rise at the first INV (i) failure when c_w = o in case B.
  - HIGH-RISE in case A.
  - RISE in every case.
  - It also counts NO-ENTRY violations by class.
  - data/inv2_all.txt (library, rfroz_cex_n16, all box-38 instances and climb outputs): 0 failures of RISE, HIGH-RISE, NO-ENTRY-A′,
    (ii_B) or LOW-RISE′.
  - Bases: 75 case-A τ(o) = o; 13 case-A c_w = o with τ(o) ≠ o; 34 case-B τ(o) = o; 6 case-A c_w ≠ o; 27 case-B c_w ≠ o.
  - Violations: 0 in the proved classes; 18 in case A with c_w ≠ o; 60 in case B with c_w ≠ o; 12 in case B with τ(o) = o (charged to
    low rises).
- nebclimb.py MODE=TAU / TAUW (τ(o) ≠ o; TAUW also c_w ≠ o), canonical start, seeds 3841-3843 from fbrestart_cex_n24.
- Instances: tauw_A_cex_n24.pg (e29908d5…), tauw_B_cex_n24.pg (c0ad4f0c…). Climb logs: experiments/new/out/box38/nebclimb
  (gitignored).
