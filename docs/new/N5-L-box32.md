# N5 on 𝒞^1O, box 32: the coarse freeze at the USED level, and one conjecture (NO-WAKE) that would merge the open cores
L-NEW successor 12 (Opus 5.5, D15/D18). GO 2026-10-24 23:50Z (Lead); first version pushed 2026-10-25 00:1xZ by date -u (container clock
  runs slow; stamps only from date -u).
Labels (L40): PROVED (by whom), READING, CONJECTURE, FALSE, OPEN, DATA. Every PROVED here is L-NEW's, unrefereed.
- Scope: lemmas about the candidate N5 (SPEC docs/new/N5-ssi-global.md). §1-§3 hold on EVERY parity game, inside a phase. §4-§5 are on
  𝒞^1O (exactly one Odd vertex o of out-degree > 1). Not a running-time bound, not a TARGET.md claim. G-N5-TIME stays OPEN.
- Task (Lead GO 23:50Z): the open cores (E) and (K_W) of (NH') (docs/new/N5-U23-box31.md §3) via a coarse freeze at L-SI's gate level M
  (RESULTS R25) instead of at c_w (successor 11's READING, N5-U23 §5).

## Summary
| item | label | where |
| --- | --- | --- |
| The freeze at the gate level M is vacuous for most residual transitions: M_k = ∞ at 52 of 69 U2/U3 KW transitions and at both events | DATA | §0 |
| (KW-M) "≤ \|R\| W-changing transitions per M-block" | FALSE (climb) | §0 |
| Lemma U: COARSE_{L_k}(Ξ) is unchanged, L_k = the USED level (max level of the Ξ-relevant changes actually made); always finite | PROVED | §1 |
| Lemma HI: the gate edges of level > L_k are the same, with the same levels, before and after the transition | PROVED | §1 |
| Lemma UL: the used level is never set by a switch of the vertex of that rank | PROVED | §1 |
| Lemma GR: a transition whose used level ℓ ≥ 0 is set by an Even switch makes that vertex ℓ-good; nobody loses ℓ-goodness at used level ≤ ℓ | PROVED | §1 |
| Lemma NU: a run of transitions with no relevant change has ≤ m − n transitions and leaves Ξ fixed | PROVED | §1 |
| Theorem LP: a phase has T ≤ (m − n + 1)(T_rel + 1) transitions, T_rel ≤ (n + 1)(ρ + 1)·n(n − 1) + ε (ρ = rises of the used level, ε = Odd-only levels) | PROVED | §2 |
| Lemma DF (𝒞^1O): after an S4a step a dormant gate edge (y, z) has σ(y) ∈ R (never F → F, never F → R) | PROVED | §3 |
| Lemma BAND (𝒞^1O, both frames in route form): a dormant R-R gate edge has its Ξ-level strictly between rank c_θ and rank c_w | PROVED | §3 |
| CONJECTURE NO-WAKE: away from fallbacks and crossings, S4a never takes a dormant edge above the previous used level | CONJECTURE (DATA: 0 failures) | §4 |
| Corollary: NO-WAKE ⇒ each phase on 𝒞^1O has O(m·n⁵·(1 + S_o + X)) transitions (S_o = σ̄(o) changes, X = crossings), with R25 FB and J1 | PROVED given NO-WAKE | §4 |
| What this does to (NH'), (E), (K_W), J, NFB-O | READING | §5 |

## 0. The gate-level freeze is vacuous where it is needed (DATA)
- Tools: experiments/new/box32/mblock.py (classes KW / EV / FLAT of N5-U23 §5, M_k and tameness read from experiments/si/coarse/mono.py).
  Instance set: every experiments/**/*.pg in 𝒞^1O with n ≤ 64 (experiments/new/box32/c1o_list.py 64: 220 files).
- Every residual transition is tame (successor 11's 78/78 reproduced on the larger set: 0 non-tame among 152 KW / EV / FLAT).
- But M_k = ∞ (some gate edge points to a better cycle node; COARSE_∞ is constant, so tameness says nothing):

| class | transitions | M_k = ∞ | M_k finite |
| --- | --- | --- | --- |
| U2 KW | 32 | 27 | 5 (all M = −1) |
| U3 KW | 37 | 25 | 12 (M 15, 23) |
| U23 KW | 74 | 0 | 74 (M −1, 19, 22, 23) |
| U3 EV (events) | 2 | 2 | 0 |
| U23 FLAT | 7 | 7 | 0 |

- So the READING "coarse freeze at level M" gives nothing for most of U2 / U3 and for every event seen. The ∞-gate edges are never taken
  inside a phase (R25 NOINF), so they are DORMANT: improving for Ξ, not chosen by S4a against τ. That is the two-frame gap again.
- (KW-M), "the KW transitions of one M-block number ≤ |R| − 1", is FALSE: the climb experiments/new/box32/mblockclimb.py from oc24_s4
  reached a U3 M-block (M = 21) with 15 KW transitions at |R| = 3 (instances/kwm_cex_n24.pg, §6). It held on all 220 library files
  (max 16 at |R| 24).
- W-changes above M exist (oc12_s1, transition 1, U2: W at level 11 with M = −1): there c_θ is the top-rank vertex, so Ξ sees only lengths.
- Repair: freeze at the level actually USED by the step, not at the highest level AVAILABLE. §1-§2.

## 1. The used level (PROVED, L-NEW; any game)
Notation as RESULTS R25 / docs/si/P-N5-FB-box7.md §0-§1: valuations (c, P, ℓ) with ranks; lev(x, y) (∞ if cycle nodes differ, else the
top rank of P(x) Δ P(y), else −1 if only lengths differ, ⊥ if x = y); COARSE_L; (C1)-(C4); Ξ_k = Θ_{H_k} (ENG-1), H_k = the
(σ_k, σ̄_k)-graph, λ_k = cycle nodes; VJ00 Lemma 5.2 with (P1)-(P3); R15 (a), (d). A PHASE is a run of transitions with λ_Ξ and τ constant
(R21 / R25 setting; only these two are used). A vertex v is its own cycle node if λ(v) = v.
- RELEVANT CHANGES at k → k+1: an Even y with σ_{k+1}(y) ≠ σ_k(y) and λ_k(y) ≠ y; an Odd u with σ̄_{k+1}(u) ≠ σ̄_k(u) and λ_k(u) ≠ u.
- The USED LEVEL L_k := max of lev(Ξ_k(old successor), Ξ_k(new successor)) over the relevant changes; L_k := ⊥ if there is none
  (an NU transition). Compare M_k = the max level over ALL gate edges (R25): Even's part of L_k is ≤ M_k, but L_k can be far below M_k.
- For ℓ ≥ 0 let u_ℓ be the vertex of rank ℓ. A valuation x with rank(c(x)) < ℓ is ℓ-GOOD if (u_ℓ ∈ P(x)) ⟺ (Ω(u_ℓ) even). At a fixed
  phase, G_ℓ(k) := {v : rank λ(v) < ℓ, Ξ_k(v) ℓ-good}.

**Lemma U (used-level freeze).** Let k → k+1 be a transition inside a phase. Then L_k < ∞, and COARSE_{L_k}(Ξ_{k+1}(v)) =
COARSE_{L_k}(Ξ_k(v)) for every v (with COARSE_⊥ = identity: an NU transition leaves Ξ unchanged).
Proof.
1. L_k < ∞. For a relevant Even y: λ_k(σ_k y) = λ_k(y) by (P1) on the H_k-edge; λ_k(σ_{k+1} y) = λ_{k+1}(σ_{k+1} y) = λ_{k+1}(y) = λ_k(y)
   by the phase and (P1) at k+1. So both valuations have cycle node λ_k(y). The same for a relevant Odd u.
2. Fix v and c := λ_k(v) = λ_{k+1}(v). Let p_0 = v, p_1, …, p_s = c be v's H_{k+1}-path up to its first visit of c. By (P1) along H_{k+1}
   edges, λ_{k+1}(p_i) = c for all i, so p_i ≠ c is not its own cycle node for i < s. Hence if p_i's successor differs in H_k and H_{k+1},
   that change is relevant and has level ≤ L_k, so COARSE_{L_k}(Ξ_k(p_{i+1})) = COARSE_{L_k}(Ξ_k(succ_{H_k} p_i)) by (C2).
3. Downward induction on i. i = s: Ξ_k(c) = Ξ_{k+1}(c) = (c, ∅, 0) by (P3) (c is a cycle node at k and k+1).
   i < s: Ξ_{k+1}(p_i) = p_i ⊕ Ξ_{k+1}(p_{i+1}) by (P2). By (C4), its COARSE_{L_k} is a function of p_i and COARSE_{L_k}(Ξ_{k+1}(p_{i+1})),
   which equals COARSE_{L_k}(Ξ_k(p_{i+1})) by induction, which equals COARSE_{L_k}(Ξ_k(succ_{H_k} p_i)) by step 2. By (C4) and (P2) at k,
   that is COARSE_{L_k}(Ξ_k(p_i)). Take i = 0. □
- This is R25's Lemma TAME (proof of COARSE-SI (b) through Claim (T)) with M_k replaced by L_k: TAME uses M_k only as an upper bound on
  the levels of the changed edges, and the own-cycle-node changes can be dropped because no path before a first visit of c passes one.

**Lemma HI (high gate edges are frozen).** In the setting of Lemma U, let L := L_k ≠ ⊥ and let y be an Even vertex that is not an own
cycle node switched at k. For every z: (y, z) is a gate edge of level ℓ > L at k iff it is one of level ℓ at k+1.
Proof. COARSE_L(Ξ_{k+1}(x)) = COARSE_L(Ξ_k(x)) for every x (Lemma U), and COARSE_L(Ξ_k(σ_{k+1} y)) = COARSE_L(Ξ_k(σ_k y)) (y unswitched, or
its switch is relevant of level ≤ L; (C2)). By (C2), lev(·,·) > L iff the COARSE_L values differ, and then the level (the top rank of
the restricted path sets, or ∞) and the direction (reward of the cycle node, else the parity of that top vertex) are functions of the two
COARSE_L values. The endpoints σ_k(y), σ_{k+1}(y) themselves give levels ≤ L at both times. □
- Consequence: M_{k+1} = M_k whenever M_k > L_k, and M_{k+1} ≤ L_k when M_k = L_k. So M is non-increasing at every phase transition at which
  Even sets the used level (R25 MONO is the tame case). M can exceed L for a long time: those top edges are the dormant ones.

**Lemma UL.** Inside a phase, L_k = ℓ ≥ 0 is never attained by a relevant switch of the Even vertex u_ℓ.
Proof. Let y = u_ℓ switch from a = σ_k(y) to z with lev(Ξ_k(a), Ξ_k(z)) = ℓ, c := λ(y), so rank c < ℓ. z is a gate edge target (R15 (d)),
so Ξ_k(z) ▷ Ξ_k(a) and they differ first at y's bit.
- If Ω(y) is odd, the better one, z, lacks y, so y ∈ P(Ξ_k(a)): a's H_k-path to c passes y, and from y it returns to a. Then a lies on an
  H_k-cycle through y whose top has rank ≥ ℓ > rank c, so λ_k(a) ≠ c = λ_k(y), against (P1).
- If Ω(y) is even, y ∈ P(Ξ_k(z)). By Lemma U and Ξ_{k+1} ⊵ Ξ_k (R15 (a)), Ξ_{k+1}(z) agrees with Ξ_k(z) above ℓ and is not worse at ℓ, so
  y ∈ P(Ξ_{k+1}(z)): z's H_{k+1}-path passes y. With σ_{k+1}(y) = z, y lies on an H_{k+1}-cycle of top rank ≥ ℓ > rank c, so λ_{k+1}(y) ≠ c,
  against the phase. □

**Lemma GR (ℓ-goodness).** Inside a phase, fix ℓ ≥ 0.
- (a) If L_k ≤ ℓ or L_k = ⊥, then G_ℓ(k) ⊆ G_ℓ(k+1).
- (b) If L_k = ℓ is attained by a relevant Even switch y: a → z, then y ∉ G_ℓ(k) and y ∈ G_ℓ(k+1).
Proof. (a) COARSE_ℓ(Ξ_{k+1}(v)) = COARSE_ℓ(Ξ_k(v)) (Lemma U; COARSE_ℓ is a function of COARSE_{L_k}). If bit ℓ differs it is then the top
difference, decided by Ω(u_ℓ); Ξ_{k+1}(v) ⊵ Ξ_k(v) (R15 (a)) forces the later one to be the ℓ-good one.
(b) y ≠ u_ℓ (Lemma UL). Ξ_k(z) ▷ Ξ_k(a) (gate edge, R15 (d)) with top difference at ℓ, so Ξ_k(z) is ℓ-good and Ξ_k(a) is not. y ⊕ x has the
same bit ℓ as x (rank y ≠ ℓ). So Ξ_k(y) = y ⊕ Ξ_k(a) (P2) is ℓ-bad, and Ξ_{k+1}(y) = y ⊕ Ξ_{k+1}(z) is ℓ-good because Ξ_{k+1}(z) is (part (a)
applied to z). □

**Lemma NU.** Inside a phase, a run of consecutive NU transitions has at most Σ_{y Even}(deg y − 1) ≤ m − n transitions.
Proof. Ξ is constant on the run (Lemma U). Every transition of a phase changes σ (τ is constant and each N5 iteration changes σ or τ,
R15 (d) / SPEC S4). The switched Even vertices are own cycle nodes (else the change is relevant), and each moves to a gate edge target:
Ξ(σ_{k+1} y) ▷ Ξ(σ_k y) with Ξ fixed. So along the run Ξ(σ(y)) strictly increases for each y: at most deg(y) − 1 switches of y. □

## 2. Theorem LP: a phase is long only if the used level rises often (PROVED, L-NEW; any game)
Statement. Let a phase have T transitions, T_rel of them relevant (L_k ≠ ⊥). Let ρ be the number of RISES (consecutive relevant transitions
k < k′, only NU transitions between, with L_{k′} > L_k) and ε the number of relevant transitions whose used level is attained only by Odd
changes. Then
    T ≤ (m − n + 1)(T_rel + 1)   and   T_rel ≤ (n + 1)(ρ + 1)·n(n − 1) + ε.
Proof.
1. NU runs: there are ≤ T_rel + 1 of them, each with ≤ m − n transitions (Lemma NU). This gives the first bound.
2. Split the relevant transitions into maximal L-RUNS (consecutive relevant transitions with equal L). Between two rises the run values
   strictly decrease and lie in {−1, 0, …, n − 1}, so there are ≤ (n + 1)(ρ + 1) runs.
3. A run with value ℓ ≥ 0: each of its transitions that is not counted in ε has L = ℓ attained by a relevant Even switch, which adds a vertex
   to G_ℓ (Lemma GR (b)); G_ℓ never loses a vertex during the run, NU transitions included (Lemma GR (a)). So ≤ n such transitions.
4. A run with value −1: COARSE_{−1}(Ξ) (cycle node and full path set) is constant on the run (Lemma U), so only lengths change. Each such
   transition not in ε has a relevant Even switch y: a → z, and Ξ_{k+1}(y) = y ⊕ Ξ_{k+1}(z) ⊵ y ⊕ Ξ_k(z) ▷ y ⊕ Ξ_k(a) = Ξ_k(y), a strict
   length change. Each vertex's length moves in one direction (fixed by the parity of its fixed cycle node) inside [0, n − 1]. So
   ≤ n(n − 1) such transitions.
5. Sum: T_rel ≤ (n + 1)(ρ + 1)·max(n, n(n − 1)) + ε. □
- Reading of the theorem: inside a phase the value vector is a counter whose digit ℓ (the sets G_ℓ) only fills up while the used level
  stays at ℓ; a long phase needs CARRIES, i.e. rises of the used level. Theorem LP says exactly: transitions ≤ poly(n, m)·(1 + carries + ε).
  It is the binary-counter picture made into an inequality; it does not by itself bound anything, since Friedmann-type lower bounds for
  other rules must have exponentially many carries. Its use is §4: for N5 the carries seem to have only three causes.

## 3. Where dormant edges live on 𝒞^1O (PROVED, L-NEW)
A gate edge (y, z) at k+1 of level > L_k is DORMANT: by Lemma HI it was a gate edge at k, with z ≠ σ_k(y), so z ∈ A_k(y), and S4a did not
take it.
**Lemma DF.** On 𝒞^1O, let k → k+1 be an S4a transition (no fallback) inside a phase, and let (y, z) be an edge of the arena H_k that is
a gate edge at k+1 (every dormant edge is one, by Lemma HI). Then a := σ_{k+1}(y) ∈ R_{k+1} (o counts as a vertex of R).
Proof.
- σ_{k+1} is Even's optimum of the one-player arena H_k against τ (SPEC S4a), so no edge of H_k improves W_{k+1}: an improving switch of a
  one-player strategy gives a strictly better strategy at that vertex (R15 (a) on the arena), while the optimum dominates every strategy
  of the arena (R17 (F1)). So W_{k+1}(z) ⊴ W_{k+1}(a), and Ξ_{k+1}(z) ▷ Ξ_{k+1}(a) (gate edge).
- Off R, Ξ = W (RESULTS R19 (a), Lemma G (a)), and Ξ ⊴ W everywhere (VJ00 (11), p. 16: Θ_{σσ̄} ⊴ Θ_{στ} for every τ; as cited in R25).
- If a ∈ F: Ξ(z) ⊴ W(z) ⊴ W(a) = Ξ(a), against Ξ(z) ▷ Ξ(a). □
- So dormant edges are of two kinds: R → F (Ξ(a) ◁ Ξ(z) = W(z) ⊴ W(a): the honest value of a sits below W(a) by more than the gap) and
  R → R.
**Lemma BAND.** On 𝒞^1O, at a state with both frames in route form ((R1): Ξ(v) = π_v ⊕ θ, W(v) = π_v ⊕ w on R) and c_θ ≠ c_w, let (y, z)
be a gate edge at level ℓ ≥ 0 with a := σ(y) ∈ R and z ∈ R, and W(z) ⊴ W(a). Then rank c_θ < ℓ < rank c_w, and P(W(z)) = P(W(a)).
Proof.
- π_x and θ's path are disjoint (under H1 o is on no honest cycle; under λ_Ξ(o) = o, θ's path is empty). So P(Ξ(z)) Δ P(Ξ(a)) =
  (π_z Δ π_a) ∩ V_{>c_θ}, and likewise P(W(z)) Δ P(W(a)) = (π_z Δ π_a) ∩ V_{>c_w}.
- ℓ ≥ 0 is the rank of the top t of (π_z Δ π_a) ∩ V_{>c_θ}. If rank t > rank c_w, W's top difference is the same t, with the same verdict,
  so W(z) ▷ W(a): excluded. t ≠ c_w, because c_w ∈ F ∪ {o} in route form and routes stop before o. So ℓ < rank c_w. Then every vertex of
  (π_z Δ π_a) has rank ≤ ℓ < rank c_w, so the W path sets agree. □
- So in route form a dormant R-R edge needs the U1 order (c_w more relevant than c_θ) and lies in the band between them. In P3′ pieces
  (c_θ more relevant) there is none. This is the two-frame band of box 26 §7.3, now localised on edges.

## 4. CONJECTURE NO-WAKE and its consequence
**CONJECTURE NO-WAKE (L-NEW).** On 𝒞^1O, let k < k′ be consecutive relevant transitions of one phase (only NU transitions between) with no
fallback in [k, k′] and R constant on [k, k′ + 1]. Then every relevant Even switch at k′ has level ≤ L_k.
- In words: away from fallbacks and crossings, S4a never wakes a dormant edge. A rise of the used level then comes only from σ̄(o).
- DATA: §6 (0 failures on every checked step of the 220-file library, 3,000 random 𝒞^1O runs and the climbs of §6).
- Why it might be true (READING). Waking (y, z) at k′ needs W*(z) to overtake W*(σ_{k′}(y)) in the new arena. By Lemma HI every edge that
  enters the arena between k and k′ has Ξ-level ≤ L_k. Lemma DF puts the dormant edge on R; Lemma BAND (route form) puts it in the band
  (c_θ, c_w) with equal W path sets, where W compares lengths only; and in the U1 order every R-route difference visible to W is visible to
  Ξ at the same level, so new edges of Ξ-level ≤ L_k change W only at levels ≤ L_k or in length. A proof needs a coarse one-player optimality
  lemma (no edge W-improving above L ⇒ the arena optimum keeps COARSE_L(W)) and the mixed cases (one of a, z in F; U2 / U3 / U23). OPEN.
**Corollary (PROVED given NO-WAKE, L-NEW).** On 𝒞^1O, in a phase with f fallbacks, S_o transitions that change σ̄(o) and X crossings:
- (i) ε ≤ S_o: an Odd-only used level is a relevant Odd change, and every Odd vertex but o has one successor.
- (ii) ρ ≤ 2f + S_o + 2X. A rise between consecutive relevant k < k′ has a fallback in [k, k′] (each transition lies in ≤ 2 such intervals),
  or a crossing in [k, k′] (≤ 2X), or else, by NO-WAKE, its new level comes from σ̄(o) at k′ (≤ S_o).
- (iii) With RESULTS R25: f ≤ n_E(2n − 1)(J + 1) + J (Theorem FB) and J ≤ S_o (J1: a non-tame transition switches σ̄(o)).
- (iv) Hence T ≤ (m − n + 1)·((n + 1)(2f + S_o + 2X + 1)·n(n − 1) + S_o + 1) = O(m·n⁵·(1 + S_o + X)).

## 5. What this does to the open cores (READING, L-NEW)
- R21 bounds a phase by O(n⁴(1 + X + O)); (NH') splits O into (E), (K_W), NFB-O and J (N5-U23 §3, R24, R25). Under NO-WAKE, Theorem LP
  replaces all of them by ONE quantity, S_o, the number of σ̄(o) changes per phase, next to X. (E) events, W-changes on R, fallbacks and J
  are no longer separate cores: they are bounded through the used level.
- What remains for o-cyclic 𝒞^1O, per phase: (1) NO-WAKE (CONJECTURE); (2) S_o (OPEN; DATA: up to 49 at n 32, §6); (3) X (OPEN; ≡ Z up to
  a factor n by R23 LV′).
- S_o has structure of its own. At a relevant change (λ(o) ≠ o) σ̄(o) is a full Ξ-minimiser over succ(o) (R25 CAP-1, REFEREE's case split);
  while θ = Ξ(o) stands still, the set of exits attaining the minimum only shrinks (Ξ is monotone). So S_o ≤ (d_o + tie-break changes)·(θ-
  changes + 1), and the θ-changes are the TRUST/THETA quantity of boxes 22-25. Bounding the tie-break changes is the analogue of R24 Lemma TB
  for the honest frame. OPEN.
- Theorem LP holds on every game; NO-WAKE and DF / BAND are the only 𝒞^1O-specific parts. On ≥ 2 Odd choice vertices ε counts all of
  Odd's honest changes.

## 6. DATA (experiments/new/box32; 𝒞^1O asserted on every file; the traces are box31/u23check.py's rows (box29/otherx.py step);
  (iterations, fallbacks) equal experiments/new/n5.py run() on every 11th LIB file, 20 of 20)
- Sets. LIB = the 220 files of c1o_list.py 64 (5,355 phase transitions). RAND = lcheck.py --rand 3000 8 24 3203 (1,375 phase transitions;
  random o-cyclic 𝒞^1O phases are short).
- lcheck.py on LIB and RAND: 0 failures of Lemma U (incl. NU: Ξ unchanged), HI, UL, GR (a) and (b), Theorem LP (both inequalities),
  ε ≤ S_o^rel, ρ ≤ 2f + S_o^rel + 2X, and NO-WAKE (1,731 checked steps: 811 + 825 LIB, 95 RAND). NU transitions: 15 LIB, 194 RAND; never
  more than 1 per phase.
- Rises of the used level (LIB, 413): 284 at a fallback (S4c switches every improving vertex to its best edge), 128 set by σ̄(o), 1 at a
  crossing (fbref_cex_n32, transitions 51-52, |R| 0 → 2 → 25), 0 other.
- Per-phase maxima (LIB): T = 110 at n 48 (x48_rt48 and x48_rt48_final: f 21, S_o 2, X 70, ρ 11, ε 1); ρ = 14 at n 48 (fbp48_rt48: T 77,
  f 16, X 18); S_o^rel = 49 at n 32 (lev_l_x: T 55, X 21, ρ 3); X = 84 at n 48 (b6_xl_n48, T 94). Constant-level runs: ≤ 55 transitions at
  n 64 (x32_rand64); level −1 runs ≤ 8 (frz24). In every phase T/(1 + f + S_o + X) ≤ 26 (op32_r, n 32: a phase with f = S_o = X = 0).
- Dormant edges (dormant.py, LIB, the 1,637 NO-WAKE-type steps; o counted in R): finite level R → F 1,167, R → R 40; level ∞ R → F 644;
  F → F 0, F → R 0 (Lemma DF). 572 steps carry a finite dormant edge. None is ever woken.
- Climbs against NO-WAKE (nwclimb.py, fitness (failures, steps with a dormant edge, checked steps); seeds x48_rt48_final, lev_l_x,
  x31_rx32, fbref_cex_n32; ~10⁴-2·10⁴ candidates each at this writing, still running): 0 failures; pressure up to 86 of 87 checked steps
  with a dormant edge (rt48 seed). (nwclimb uses the first definition of L, own cycle nodes included; NU transitions are rare, above.)
- §0 counterexample to (KW-M): experiments/new/box32/instances/kwm_cex_n24.pg, sha1 c2723e082c93aab617d81e63e821d3199e7cb189, n 24, one
  Odd choice vertex (2); n5.py: 21 iterations, 0 fallbacks; check_sol2.py: "zielonka(oink zlk) OK strategies verified"; mblock.py: a U3
  M-block (M = 21) with 15 KW transitions at |R| = 3 (|R| counts o).
- §0 tables: mblock.py on LIB; usedlev.py first showed the rises (129 of 5,355 with the first definition, fallbacks excluded).

## 7. Stamps and files
- experiments/new/box32: c1o_list.py, mblock.py, mblockclimb.py, usedlev.py, lrun.py, rises.py, nowake.py, nwclimb.py, lcheck.py (the
  consolidated checker of every lemma of §1-§4). instances/: climb results cited here.
