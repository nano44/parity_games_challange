# R-N5-NEB: REFEREE report on packet P-N5-NEB (box 38: RISE, HIGH-RISE, NO-ENTRY-A′, CASE-B-LEN′, LOW-RISE′, Theorem BRK, Corollary OUT-1)
Referee: REFEREE (successor 9, session_01VsZYJ8FiTSj5Kazk715ZP7), Opus 5.5 (owner ruling D15, Lead reading L37).
- Routing: the Lead's GO of 14:51Z (Lead's stamp).
- Object: docs/new/P-N5-NEB-box38.md at pinned trunk 314d220, sha1 ba15e51fb02471207b11ecd64e9687a23fe8a744, 297 lines (checked with
  `git show 314d220:docs/new/P-N5-NEB-box38.md | sha1sum`; the working tree at trunk 51bb725 has the same bytes). Author: L-NEW
  successor 17.
- Written 2026-10-25T15:04Z onward by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: I did not read docs/referee-2/R2-N5-NEB.md. D1: each statement was treated as wrong until its proof
  checked line by line.
- I read the lane's post-pin commit 1d934feb (BAND, rises form) only after my own probe had found the BAND violations (§8 below).

## Verdicts
| § | statement | packet label | verdict (Opus 5.5, D15) |
| --- | --- | --- | --- |
| §0 | chain rule for lev; (T1)-(T3); route form; SEP-o; F-values avoid R̄; (iii+) | filled in / used | CHECKED (all correct) |
| §1 | Lemma RISE (any τ(o), cases A and B) | PROVED | SIGNED |
| §2 | Lemma HIGH-RISE (case A, any τ(o), any c_w) | PROVED | SIGNED |
| §3 | Theorem NO-ENTRY-A′ (case A, c_w(a) = o, any τ(o)) | PROVED | SIGNED (remark NEB-R1 = OUT-R1, no gap) |
| §4 | Lemma CASE-B-LEN′ (case B, c_w(a) = o, any τ(o)) | PROVED | SIGNED (remark NEB-R1, no gap) |
| §5 | Lemma LOW-RISE′ (case B, c_w(a) = o, any τ(o)) | PROVED | SIGNED |
| §6 | Theorem BRK (a)-(d) | PROVED | SIGNED (notes NEB-N1 citation, NEB-N2 one missing line, NEB-N3 wording; no gap) |
| §7 | Corollary OUT-1 (τ(o) = o, cases A and B) | PROVED | SIGNED (premises P-N5-OUT EPOCH / NE-COUNT (c), signed by both referees, R39 at CHECKER) |
| §8 | NO-ENTRY-B, NO-ENTRY (c_w ≠ o), dead ends, CONJECTURE BAND, open core | not to sign | not signed. NO-ENTRY-B counterexample re-run (DATA). BAND: FALSE in the rises form, in the gates form at a later state, and in the gates form at the base state (level = rank(c_w)) (NEB-B1) |
- No (P). The label is exact. The one-player facts used are (V1) (R17 (a)), R15 (a), (d), XW (R21 (a)), FBL-N (i)-(iii) (R21 (c)),
  Step (K) (R23 (a)) and ACT (i) (R23 (b)), all landed. None rests on VJ00 Lemma 5.8. P-N5-P1 and P-N5-RL are not used.
- Dependencies: KEY and FB-INT are RESULTS R38 (landed 14:16Z); the packet's "landing (R36)" is stale (note NEB-N4). SPLIT, F-FLAT,
  EPOCH and NE-COUNT (c) are P-N5-OUT, signed by both referees (R-N5-OUT fa086876 + §C a8b8ef3e; R2 dfcaae67 + §C 2a9e8db0), R39 at
  CHECKER C48. So the signatures of §1 (SPLIT (a)), §5 (SPLIT (a)), §6 and §7 hold as stated once R39 lands.
- No gaps.

## 0. Objects and filled-in steps: checked
- Chain rule. For x ◁ y ◁ w with levels l1 = lev(x, y) and l2 = lev(y, w):
  - if l1 ≠ l2, all three agree above the larger level, and at it the pair that differs decides x against w the same way;
  - l1 = l2 at a vertex level u is impossible: y would hold both the membership of u that Even prefers (x ◁ y) and the other one (y ◁ w);
  - at +∞ the rewards increase strictly (so x, w differ in the cycle node); at −1 the lengths move monotonically.
  Correct. My probe checks it on every strict (★) chain (CHAIN, 6 chains, 0 failures).
- (T1)-(T3) for ≡_o (s = rank o) and ≡_B (s = 0): ≡ means the same cycle node and the same P at ranks ≥ s. (T1): the same top difference
  on the same side. (T2): from the chain rule. (T3): ⊕ adds the same vertex on both sides. Correct.
- Route form. π_z ⊆ R and o's honest play after o lies in F (each of its vertices has an o-free (σ, τ)-play, because the honest and
  (σ, τ)-graphs differ only at o). So π_z is disjoint from the cycle, and (V1) gives Ξ(z) = π_z ⊕ θ. Correct.
- SEP-o: θ = o ⊕ Ξ(σ̄ o), with o not a cycle node (H1) and rank o > rank c_θ (case A). F-values avoid R̄: the same suffix argument.
  Correct.
- (iii+): a gate (x, o) with x ∈ F would give x = λ_W(o) ∈ C_W ⊆ R̄ by FBL-N (ii). Correct.

## 1. RISE: checked
- No entry on [a, t+1]: switched edges are gates (R15 (d)); none goes F → R̄ at a..t, so ACT (i) applies. Phase-internal, so τ is unchanged.
- q = σ_{t+1}(y) ∈ F_{t+1}, because y ∈ F_{t+1} is Even.
- (★), y ∈ F_t: (y, z) is not improving at t (no F → R̄ gate, and z ≠ σ_t(y) ∈ F_t), so Ξ_t(z) ⊴ Ξ_t(σ_t y) ⊴ Ξ_t(q) ⊴ Ξ_{t+1}(q)
  (R15 (d), (a)).
- (★), y ∈ R_t: y is evicted, so t → t+1 is not S4a (SPLIT (a)), and it is in-phase, so not S4b. It is an Even fallback.
  - If (y, z) is not improving at t: as above.
  - If it is: y has an improving edge, so S4c moves y to the maximiser q, and Ξ_t(q) ⊵ Ξ_t(z).
- Ξ_{t+1}(q) ◁ Ξ_{t+1}(z), since (y, z) is a gate at t+1. z ≠ o since θ is constant. Correct.
- The hypothesis "a fallback a → a+1 in-phase" is used only to place a in S. Correct as stated.

## 2. HIGH-RISE: checked
- o ∈ P(Ξ_t z) and o ∈ P(Ξ_{t+1} z) (SEP-o, z ∈ R̄ at both), and o ∉ P(Ξ_{t+1} q) (q ∈ F_{t+1}).
- So both comparisons of (★) are strict at levels ≥ rank o: +∞ if the cycle nodes differ, otherwise a P-level ≥ rank o.
- The chain rule gives the maximum. Correct.

## 3. NO-ENTRY-A′: checked in full
- W at a: c_w = o gives w = (o, ∅, 0). XW and c_θ ≠ o give reward(c_θ) < reward(o), and case A then forces Ω(o) even.
- W_a(r) = (o, π_r ∩ V_{>o}, |π_r|): if π_r meets C_W it follows C_W to o, the cycle node. Correct. Probe: the formula holds at every
  state of every base (NOENT_Wform, 0 failures).
- BASE (i): FBL-N (iii) + (iii+) at the S4c state a (τ unchanged). Correct.
- BASE (ii):
  - Both values are π ⊕ θ_a with cycle node c_θ, and the P-difference is D = (π_z Δ π_{σ v}) ∩ V_{>c_θ}. Its top u ≠ o has rank > rank o.
  - The W-difference (π_z Δ π_{σ v}) ∩ V_{>o} has the same top u on the same side (anything higher would be in D). So W_a(z) ▷ W_a(σ_a v).
  - Case 1 (z's route avoids v, v ∉ C_W): z's play and o's W-play are unchanged, and v is in neither route, so v ⊕ preserves the strict
    order. The switch raises W at v.
  - Case 1′ (v = c_i ∈ C_W ∖ {o}): π_{σ v} = c_{i+1} … c_m lies below o, so u ∈ π_z (z's side), and Ω(u) is even.
    - π_z can meet C_W only at some c_j with j > i.
    - After the switch, v's W-play is the cycle v → π_z → o → c_1 … c_{i−1} → v. Its top is u: C_W lies below o, and a higher vertex of
      π_z would be in D. So the cycle node is u, with p′(u) > p′(o) = reward(o).
    - The subcase z = o (π_z = ∅) is vacuous: D ⊆ π_{σ v} lies below o, so ℓ ≥ rank o cannot hold. The packet's wording covers it.
  - Case 2 (π_z = q·v·π_{σ v}): D = (q ∪ {v}) ∩ V_{>c_θ} lies on z's side, so u is even and tops the new cycle v → z → q → v.
  - The three cases are exhaustive (v ≠ o as v ∈ R). Each is a single switch σ_a[v → z] with W-value at v strictly above W_a(v): the
    exact form excluded by Step (K) (P-N5-Z §1: "σ_k[y → z] has W-value at y strictly above W_k(y)"). Correct.
- STEP:
  - No entry: by (i), with R15 (d) and ACT (i).
  - Value claim: by induction on the route length at t+1; a switched z gives an R → R̄ gate at t, which (ii) at t covers; then (T3).
    Uses H1 at t and t+1 (both in S). Correct.
  - (i) at t+1: SEP-o at t+1, (T1), and R15 (a), (d) give (y, z) ∈ Iσ_t with z ∈ R̄_t.
    - y ∈ F_t contradicts (i) at t.
    - y ∈ R_t: (ii) at t and (T2) put Ξ_{t+1}(σ_{t+1} y) in the ≡_o-class of Ξ_t(z), but o separates them. Correct.
  - (ii) at t+1: the value claim, (ii) at t for a switched v, and (T1) give an R → R̄ gate at t of the same level ≥ rank o. Correct.
  - The STEP uses only the honest frame, so τ(o) and later values of c_w do not matter. Correct.
- NEB-R1 (remark, no gap; = OUT-R1 / N-OUT-2 on P-N5-OUT, which the Lead flags for NEB §3/§4).
  - The setting allows a phase-exiting fallback a → a+1 (then b = a), while (K) is stated "at an S4c fallback inside a phase".
  - (K)'s proof uses only FBL-N (i) at a: σ_a is a pointwise arena optimum in G_τ (R21 (c), stated "at an S4c fallback with τ unchanged",
    with no phase condition). It does not look at a+1. So BASE (ii) holds at a phase-exiting fallback too.
  - Data: one such base occurs (red/n5inj/instances/frz24.pg, case A, c_w ≠ o; outside §3's class).
  - Lane text: cite FBL-N (i) + the single-switch form, or require a+1 ∈ S. In every use inside the packet (§6: an eviction is a
    crossing, hence in-phase) a+1 ∈ S holds anyway.

## 4. CASE-B-LEN′: checked
- Case B and c_w = o give w = (o, ∅, 0), reward(o) > reward(c_θ), and Ω(c_θ) odd (an even c_θ above o would beat o).
- If D ≠ ∅, its top u has rank u > rank c_θ > rank o. The W-difference has the same top on the same side. Cases 1, 1′ (π_{σ v} ⊆ C_W
  lies below o < u, so u ∈ π_z and is even) and 2 each give a single-switch W-raise at v, against (K). The new cycle node u has
  p′(u) > p′(o) ≥ reward(o) whatever the parity of o.
- So D = ∅: the same cycle node and P, lev = −1 (strict, so not −∞). With c_θ odd the gate means the longer value: |π_z| > |π_{σ v}|.
  Correct.
- NEB-R1 applies verbatim (the setting is "an HN state at which an Even fallback is taken").

## 5. LOW-RISE′: checked
- INV_B(a): (i) by FBL-N (iii) + (iii+), (ii_B) by §4.
- (a), (b): the §3 STEP with ≡_B. (T3) for ≡_B holds (z ⊕ adds z on both sides or on neither). For (ii_B) at t+1, a gate of level ≥ 0
  at t+1 would transfer by (T1) at threshold 0 to an R → R̄ gate at t of level ≥ 0, against (ii_B) at t. The value claim gives
  ≡_B-freezing.
- (c): t+1 > a lies in S, so a → a+1 is in-phase and §1 applies.
  - (★) and (a) with (T2) give Ξ_{t+1}(q) ≡_B Ξ_{t+1}(z), hence the same P.
  - P(Ξ_{t+1} q) ⊆ F_{t+1} and π_z ⊆ R_{t+1}, so π_z ∩ V_{>c_θ} = ∅ and P(Ξ_{t+1} z) = P(θ).
  - By (a), Ξ_t(z) has the same cycle node and P, so both values lie in C_θ, and they rise strictly by (★). Correct.

## 6. BRK: checked
- The eviction is a crossing, hence in-phase. It is not S4a (SPLIT (a)) and not S4b (τ is constant), so it is an Even fallback. The
  entry needs a gate F → R̄ at k (ACT (i), R15 (d)). j0 ≠ a by F-FLAT.
- The three branches:
  - (a): with θ constant on [a, t+1], §3 (b = t+1) excludes the gate at t+1;
  - (b): §5 (c) gives a low rise at t → t+1 with a ≤ t < k. INV_B on [a, t] holds by (i) up to t (choice of t+1) and §5 (b) inductively;
  - (c): §1, high in case A by §2.
- Disjointness: the next break's eviction state is ≥ k+1, so the intervals [a, k] are disjoint, and each break is charged to its own
  transition. Correct.
- LR_S:
  - On a θ-constant run, C_θ is an ≡_B-class, an interval. Since Ξ only rises, a vertex leaves it at most once (upward), and its length
    moves monotonically inside it.
  - Low rises are at z ∈ R̄ ∖ {o}, and c_θ ∈ F. So ≤ n − 2 vertices, with lengths in [1, n − 1]: ≤ n − 2 strict moves each, hence
    ≤ (n − 2)² transitions per run, and ≤ θ_S + 1 runs. Correct.
- (d) and its special case (o tops its W-cycle at every eviction state ⇒ B^≠ = 0, RW_S = 0; in case A every break has a θ-change).
  Correct.
- NEB-N1 (citation): "SPLIT (b): an S4a step does not evict" should read SPLIT (a). (SPLIT (b) is "an Even fallback does not enter".)
- NEB-N2 (one line missing, no gap): §1 needs "no state of [a, t] has a gate F → R̄", including a itself. §6 defines t+1 as "the first
  state after a with a gate F → R̄" and never says that a has none. It holds by FBL-N (iii) + (iii+) at the S4c state a under ¬H2 (as
  in §3/§5 BASE (i)). Add that line. Probe FBLN0: 0 failures at 117 HN Even-fallback states.
- NEB-N3 (wording): "Values in C_θ belong to vertices z ∉ {o, c_θ}" is false as written (θ itself lies in C_θ). Intended: "low rises
  are at vertices z ∉ {o, c_θ}" (z ≠ o by definition; c_θ ∈ F).

## 7. OUT-1: checked
- With τ(o) = o, C_W = {o}, so c_w = o at every HN state, B^≠ = 0, and B_S ≤ θ_S + (n − 2)²(θ_S + 1) = D(θ_S + 1) − 1.
- EPOCH: X_S ≤ 2(n − 1)D(θ_S + 1). Fallbacks from HN states: in-stretch ones (≤ K(X_S + 1) + X_S) plus ≤ 1 exit per stretch, so
  ≤ (K + 1)(X_S + 1) per stretch.
- Σ_S (X_S + 1) ≤ 2(n − 1)D(θ_ph + N_HN) + N_HN, and N_HN ≤ ⌊T_ph/2⌋ + 1 (NE-COUNT (c)). Both bounds: arithmetic checked.
- The parenthesis "(all out-of-SN fallbacks of the phase)" is P-N5-OUT NE-COUNT (c)'s own wording, not re-proved here.
- θ_ph is a parameter: this is not a running-time bound for N5. G-N5-TIME stays OPEN, as the packet says.
- NEB-N4 (status): KEY / FB-INT are RESULTS R38 (landed), not "landing (R36)".

## 8. NOT TO SIGN: what I checked (DATA)
- NO-ENTRY-B on nebc_cex_n14 (sha1 399119af…; sha1 re-measured): own engine, o = 7, rank 6 < rank(c_θ = 12) = 8, 9 iterations,
  5 fallbacks. The fallback at 1 switches 3 from 7 to 6, so Ξ(3) goes (12, ∅, 3) → (12, ∅, 4). The gate 4 → 3 from F at 2 is followed by
  an entry 2 → 3 with θ = (12, ∅, 2) constant. As §8 states. CASE-B-LEN′ holds at its 4 case-B gates.
- NEB-B1 (for the fixes file): CONJECTURE BAND ("after a c_w ≠ o fallback in case A, R → R̄ gates and R̄-rises have levels below
  rank(c_w)") is FALSE in every form I tested.
  - (1) Rises form, on tauw_A_cex_n24 (sha1 e29908d5…; canonical start). Base a = 4: case A, c_w(4) = 7 of rank 21, rank o 17. The
    θ-constant HN run is [4, 13]: state 13 is in the stretch, and 13 → 14 exits the phase. S4a 12 → 13 raises Ξ(11)
    (18, 4882432, 11) → (18, 13336576, 13) and Ξ(16) (18, 688128, 5) → (18, 9142272, 13), both at level 23 > 21. My engine gives the
    lane's numbers (commit 1d934feb, read after my run).
  - (2) Gates form at a later state (new): on the same run, state 13 has R → R̄ gates 3 → 11 and 7 → 16, at level 23 > 21. The same two
    rises and two gates repeat from base a = 10.
  - (3) Gates form AT the base state (new; the lane wrote "untested"): docs/referee/R-N5-NEB/band_base_cex.pg, sha1
    468edac825a19ef73823a684c288ee01abaad94b.
    - n 24, C^1O, o = 19 (rank 17), τ(o) = 16. Found by my random walk from tauw_A_cex_n24 (scratch/band_find.py, seed 77, 316 steps).
    - Canonical start, 6 iterations, 1 fallback. Oink 8fbf0a7 --zlk solves it and verify accepts the solution.
    - The lane's engine (experiments/new/box38/neb_run.py trace, data cross-check only) gives the same σ, τ(o) and Ξ at all 7 states.
    - Base a = 2 is an in-phase Even fallback at an HN state: case A (rank c_θ 14 < 17), c_w(2) = 2, of rank 19.
    - Its R → R̄ gate 5 → 14 (σ_2(5) = o, Ξ_2(o) = (18, 196608, 2) ◁ Ξ_2(14) = (18, 753664, 8)) has level 19 = rank(c_w(2)). The top
      difference is the vertex c_w = 2 itself.
    - This breaks BAND's strict "below rank(c_w)" at the boundary. A "≤ rank(c_w)" form at the base: no counterexample in a 458,960-step
      search (§9.1).
  - Obstruction, as the lane says for (1): c_w(a) is read at the base, and W-improving R → R̄ gates are not bounded by c_w.

## 9. DATA (DATA, not proof; own code docs/referee/scratch/neb_probe.py on rl_engine, no lane imports; logs docs/referee/R-N5-NEB/)
- C^1O asserted (exactly one Odd vertex of out-degree > 1); non-C^1O files skipped and counted. Every check counts its hypothesis
  occurrences (lesson N-ENT-2).

| check | lib37 (270 C^1O) | lane set (lib37 + box38 instances/*.pg, 275) | named (6, .state starts) | failures |
| --- | --- | --- | --- | --- |
| HN Even-fallback states; FBLN0 (no F → R̄ gate at a) | 106 | 117 | 18 | 0 |
| RISE events (first F → R̄ gate after a on the θ-run) / gates (★) | **0** / 0 | 6 / 7 | 7 / 8 | 0 |
| HIGH-RISE (case A) / chain rule | 0 / 0 | 3 / 6 | 3 / 6 | 0 |
| NO-ENTRY-A′ runs (τ(o) = o / ≠ o) / states | 75 / 9 / 835 | 75 / 9 / 835 | 0 / 4 / 21 | 0 |
| CASE-B-LEN′ R → R̄ gates at case-B c_w = o bases | **0** | 4 | 12 | 0 |
| LOW-RISE′ runs / steps / (c) events | 15 / 52 / **0** | 20 / 63 / 1 | 8 / 14 / 2 | 0 |
| breaks A= / B= / A≠ / B≠ | 8 / 3 / 0 / 0 | 8 / 4 / 2 / 2 | 0 / 2 / 2 / 2 | BRK (a)-(d), LR: 0 |
| breaks charged θ / low / other rise | 11 / 0 / 0 | 11 / 1 / 4 | 0 / 2 / 4 | — |
| OUT-1 τ(o) = o phases (X_HN, f_HN totals) | 83 (144, 90) | 88 (150, 95) | 7 (9, 8) | 0 |

- VACUOUS IN DATA (lesson N-ENT-2): on lib37 alone, the hypotheses of §1/§2, §4 and §5 (c) never occur, and every break is charged to
  a θ-change. §1, §2, §4, §5 (c) and the low / rise charging of §6 are exercised only on the box-38 instances (nebc_cex_n14,
  tauw_A/B_cex_n24, neb_cex_n11 from its .state start). Random C^1O games (4,600, n 6-22, half with a loop at o) give no HN breaks
  at all: no evidence either way.
- Base counts vs packet §9: per file, my in-phase base counts equal the lane's own inv2.py output on all 24 files that have bases
  (lane set). Totals on the lane set: 75 / 9 / 4 / 20 / 8 (A c_w = o τ(o) = o / A c_w = o τ(o) ≠ o / A c_w ≠ o / B τ(o) = o / B c_w ≠ o),
  plus 1 phase-exiting base (frz24), which the lane does not count. The packet's §9 prints 75 / 13 / 6 / 34 / 27
  (data/inv2_all.txt). So that file comes from an input set larger than its "Reproduce" line names (note NEB-N5, data only).
- Climbs: docs/referee/scratch/neb_climb.py (own mutations, C^1O kept), seeds nebc_cex_n14, tauw_A_cex_n24, tauw_B_cex_n24,
  wd16_s2: see §9.1.

### 9.1 Climbs (own code: scratch/neb_climb.py, mutations keep C^1O; logs scratch/neb_logs/climb_1..4.txt; 20 min each, 15:01-15:21Z)
- Score = RISE events + 3 · low-rise (c) events + CASE-B gates + 2 · breaks + 4 · (B≠ breaks). A mutant is kept if its score does not drop.
- Counts are summed over the evaluated mutants. A kept game is re-counted at each evaluation, so these are occurrences, not distinct games.

| seed | mutants tried | RISE (★) events | HIGH / chain | CASE-B gates | low-rise (c) | breaks (B= / A≠ / B≠) | BAND (rise / gate later / gate at base) | FAILS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nebc_cex_n14 | 761,975 | 3,218 | 0 / 6 | 29,415,307 | 3,218 | 3,018 / 0 / 0 | — | 0 |
| tauw_A_cex_n24 | 243,979 | 449,666 | 37,299 / 516,959 | 0 | 0 | 0 / 15,212 / 405,914 | 5,925 / 8,169 / 2,848 | 0 |
| tauw_B_cex_n24 | 272,014 | 420,323 | 17 / 582,582 | 0 | 0 | 0 / 2 / 408,622 | — | 0 |
| wd16_s2 | 2,058,330 | 0 | 0 / 0 | 0 | 0 | 0 | — | 0 |

- Every hypothesis of §1, §2, §4, §5 (c), and the B= / B≠ charging of §6, occurs many times in the climbs: 0 failures.
- Not reached by any climb: case-A breaks with c_w(a) = o (A=: 8 in the library, all θ-charged). The wd16_s2 climb found no improving
  mutant (score 0 throughout).
- The BAND counters of the tauw_A climb are what sent me to search for the base-state instance (NEB-B1 (3)).
- A "≤ rank(c_w)" form at the base: a random walk from tauw_A_cex_n24 (scratch/band_find.py, seed 78, 20 min, 458,960 steps, keeping
  mutants with case-A c_w ≠ o bases) found NO base-state gate of level > rank(c_w) (log scratch/neb_logs/band_find_strict.txt).
  - This is DATA only. The later-state gates of (2) are strictly above rank(c_w), so a "≤" form fails after the base anyway.

## Notes for the lane's fixes file (none is a gap)
- NEB-R1: §3 BASE / §4 cite (K) "inside a phase"; cite FBL-N (i) + the single-switch form, or require a+1 ∈ S.
- NEB-N1: §6 "SPLIT (b)" → "SPLIT (a)" for "an S4a step does not evict".
- NEB-N2: §6: add "a has no gate F → R̄ (FBL-N (iii) + (iii+))", so §1's hypothesis holds on [a, t].
- NEB-N3: §6 LR_S: "low rises are at vertices z ∉ {o, c_θ}", not "values in C_θ belong to …".
- NEB-N4: KEY / FB-INT status → RESULTS R38.
- NEB-N5: §9 base totals are not reproduced by the stated command (75 / 9 / 4 / 20 / 8 on lib37 + instances/*.pg); name the input.
- NEB-B1: BAND FALSE in the rises form (lane), in the gates form at a later state (state 13 of tauw_A_cex_n24, level 23 > 21), and in
  the gates form at the base state (band_base_cex.pg, level 19 = rank(c_w)); see §8 and §9.1 for the "≤" variant.
