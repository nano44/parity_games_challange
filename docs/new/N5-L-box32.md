# N5 on 𝒞^1O, box 32: the coarse freeze at the USED level; NO-WAKE (would have merged the open cores) is FALSE in U3
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
| Lemma DF (𝒞^1O) as first stated | FALSE (referees: df_cex.pg n 11 / n 5; own W-cycle nodes) — replaced by DF′ (y not its own W-cycle node), signed by both; P-N5-LP-fixes-box32.md §1 | §3 |
| Lemma BAND (𝒞^1O, both frames in route form): a dormant R-R gate edge has its Ξ-level strictly between rank c_θ and rank c_w | PROVED | §3 |
| (NO-WAKE) "away from fallbacks and crossings, S4a never takes a dormant edge above the previous used level" | FALSE (instances/nowake_cex_n32.pg, a U3 state) | §4 |
| Lemma WAKE: a wake goes R → R (a wake into F is a crossing); in route form it lies in a U1 piece (covered by R24 Theorem U1) | PROVED | §4 |
| Corollary LP′: each phase on 𝒞^1O has O(m·n⁵·(1 + S_o + X + K)) transitions (S_o = relevant σ̄(o) changes, X = crossings, K = wakes), with R25 FB and J1 | PROVED | §4 |
| Lemma TH: θ-changes per phase ≤ (n − 1) + n(X + 1) + X | PROVED | §4b |
| Lemma SO: relevant σ̄(o) changes ≤ d_o(Θ + 1) (with θ fixed, σ̄(o) moves only when its exit stops being a minimiser) | PROVED | §4b |
| Corollary XJ: S_o, J and the fallbacks are O(poly(n)(1 + X)); a phase has O(m n⁷ (1 + X) + m n⁵ K) transitions | PROVED (given R22, R24, R25) | §4b |
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
**Lemma DF** (FALSE as stated: it needs y not its own W-cycle node, i.e. DF′; see docs/new/P-N5-LP-fixes-box32.md §1). On 𝒞^1O, let k → k+1 be an S4a transition (no fallback) inside a phase, and let (y, z) be an edge of the arena H_k that is
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

## 4. Wakes
A WAKE is a relevant Even switch at k′ of level > L_k, where k < k′ are consecutive relevant transitions of one phase (only NU transitions
between) with no fallback in [k, k′] and R constant on [k, k′ + 1]. K := the number of transitions k′ of the phase with a wake.
**(NO-WAKE), K = 0, is FALSE (L-NEW, box 32).** It held on every library step (§6), and climbs on dormant-edge pressure did not break it,
but the climb rrclimb.py (fitness: failures, then dormant R → R edges outside route form) broke it in ~10³ candidates from
u1flat_best_n32: experiments/new/box32/instances/nowake_cex_n32.pg (n 32, sha1 3a56e3fb94f3c84684d01fc87ff3c7e9a8d7eb3f, one Odd choice
vertex o = 27; n5.py 9 iterations, 2 fallbacks; check_sol2.py "zielonka(oink zlk) OK strategies verified").
- Transitions 0 and 1 are S4a steps of one phase with R constant (|R| = 30). The state is U3: the honest frame is in route form with
  c_θ = o (rank 15), and c_w = vertex 13 is the TOP-rank vertex (rank 31).
- L_0 = 26. At transition 1, y = 11 switches 22 → 9 at Ξ-level 30 (> 26). (11, 9) is a gate edge at 0 and at 1 (Lemma HI), so S4a declined
  it at 0.
- Mechanism: with c_w the top vertex every W path set is empty, so W compares LENGTHS only (W(22) = (13, ∅, 7), W(9) = (13, ∅, 9) at 0 and
  1). At transition 1 the same S4a step shortens 9's route (switches at 14 and 15), W(9) becomes (13, ∅, 7) = W(22), and the tie-break takes
  9. The honest frame meanwhile sees the level-30 difference all along. This is the W-blind band of Lemma BAND, pushed to its extreme
  (nothing above c_w), outside route form.
**Lemma WAKE (PROVED, L-NEW).** Let y: a → z be a wake at k′ (definition above; level ℓ > L_k). Then
a ∈ R and z ∈ R.
Proof.
- (y, z) is a gate edge at k′ of level ℓ > L_k. Going back through the NU transitions between k and k′ (Ξ is fixed there and only own
  cycle nodes switch; y is not an own cycle node, since its
  switch is relevant) and through k itself, Lemma HI makes it a gate edge of the same level at every step of [k, k′]; in particular it is
  an edge of the arena H_{k′−1}, and the transition k′ − 1 → k′ is an S4a step. Lemma DF at that step: a = σ_{k′}(y) ∈ R.
- If z ∈ F_{k′} = F_{k′+1} (R is constant), then y's σ_{k′+1}-play enters F and never reaches o, so y ∉ R_{k′+1}. But y ∈ R_{k′} (its
  play passes a ∈ R) and R_{k′} = R_{k′+1}. So z ∈ R. □
- So every wake is an R → R switch at a vertex y ∈ R. (Wakes into F are crossings, counted by X: the one such rise in the library,
  fbref_cex_n32 transition 52, is of this kind.)
- Route form (both frames), by Lemma BAND: a woken R → R edge has level ℓ ∈ (rank c_θ, rank c_w), so the state is in the U1 order, i.e. in
  a U1 piece, and the wake is an R-changing transition of that piece, of which RESULTS R24 Theorem U1 allows O((f + 1)|R|³).
- Outside route form, a wake is an R-changing transition of a U2 / U3 / U23 stretch, i.e. one of the transitions counted by the
  consequences of CASC-U2 / CASC-U3 (N5-U23-box31.md §1-§2: ≤ f + K_W + E + (K_W + f + E + 1)(2|R| − 3) per stretch). So K is bounded
  by the existing open cores (E) and (K_W), and nowake_cex_n32 shows it is not 0.
- DATA (rrdorm.py, LIB): finite dormant R → R edges occur at 40 checked steps: 35 in route form, ALL in the band with c_w above c_θ
  (u1flat_best_n32 and others), 5 in U23 (nr_u23_n32), c_w above c_θ. None is woken in the library.
**Corollary LP′ (PROVED, L-NEW).** On 𝒞^1O, in a phase with f fallbacks, S_o relevant σ̄(o) changes (λ(o) ≠ o), X crossings and K wakes:
- (i) ε ≤ S_o: an Odd-only used level is a relevant Odd change, and every Odd vertex but o has one successor.
- (ii) ρ ≤ 2f + S_o + 2X + K. A rise between consecutive relevant k < k′ has a fallback in [k, k′] (each transition lies in ≤ 2 such
  intervals), or a crossing in [k, k′] (≤ 2X), or its new level comes from σ̄(o) at k′ (≤ S_o), or else it is a wake.
- (iii) With RESULTS R25: f ≤ n_E(2n − 1)(J + 1) + J (Theorem FB) and J ≤ S_o (J1: a non-tame transition switches σ̄(o); a σ̄(o) change at an
  own cycle node o changes no Ξ value, Lemma U, so it cannot be non-tame).
- (iv) Hence T ≤ (m − n + 1)·((n + 1)(2f + S_o + 2X + K + 1)·n(n − 1) + S_o + 1) = O(m·n⁵·(1 + S_o + X + K)).

## 4b. S_o, J and the fallbacks reduce to X (PROVED, L-NEW; 𝒞^1O; unrefereed; written after P-N5-LP was frozen)
Setting: a phase on 𝒞^1O; d_o := |succ(o)|; Θ := the number of transitions of the phase that change θ = Ξ(o); X := crossings.
If λ_Ξ(o) = o, θ = (o, ∅, 0) is constant and no σ̄(o) change is relevant; so assume λ_Ξ(o) ≠ o (fixed in the phase).
**Lemma TH.** Θ ≤ (n − 1) + n(X + 1) + X.
Proof.
- H1 is constant on each crossing-free interval (R22 (b) TC (i)), so a θ-change at a crossing is counted by X. Take a crossing-free θ-change
  k → k+1.
- ¬H1 at k: o lies on its honest cycle, whose top is c_θ, so θ = (c_θ, ∅, d) with d ∈ [0, n − 1] (REFEREE's R-1, P-N5-U23 fixes §6). c_θ is
  fixed in the phase and θ is monotone (R15 (a)), so d moves in one direction: ≤ n − 1 such changes in the whole phase.
- H1 at k: σ̄_k(o) =: x0 is a full Ξ_k-minimiser over succ(o) (λ(o) ≠ o; R25 CAP-1, REFEREE's case split), and θ_k = o ⊕ Ξ_k(x0) (P2).
  x0's honest play never returns to o (H1), so it equals its (σ_k, τ)-play, which therefore never reaches o: x0 ∈ F_k = F_{k+1}. Let
  x1 := σ̄_{k+1}(o). If Ξ_{k+1}(x0) = Ξ_k(x0), then Ξ_{k+1}(x1) ⊴ Ξ_{k+1}(x0) = Ξ_k(x0) ⊴ Ξ_k(x1) ⊴ Ξ_{k+1}(x1) (minimisers; R15 (a)), so
  θ_{k+1} = o ⊕ Ξ_{k+1}(x1) = θ_k. So a θ-change changes Ξ at x0 ∈ F: it is one of the ≤ max(0, |F| − 1) F-changing transitions of its
  crossing-free interval (R22 (a) F1°). There are ≤ X + 1 intervals. □
**Lemma SO.** S_o ≤ Θ + (d_o − 1)(Θ + 1) ≤ d_o(Θ + 1). More precisely: at a relevant σ̄(o) change with θ unchanged, the old choice is no
longer a minimiser.
Proof.
- Fix a maximal run of the phase with θ constant, and μ with o ⊕ μ = θ (⊕ is injective for a fixed cycle node). T_k := {x ∈ succ(o) :
  Ξ_k(x) = μ}, the full minimisers (μ = min, since σ̄_k(o) ∈ T_k by CAP-1). T only shrinks along the run: x ∈ T_{k+1} gives Ξ_k(x) ⊴
  Ξ_{k+1}(x) = μ ⊴ Ξ_k(x).
- The choice inside T. By RESULTS R24 Lemma R, σ̄_k(o) is chosen among the fully optimal successors, i.e. T_k: in the longest-path mode
  (Ω(λ(o)) even) the first in list order, i.e. the smallest index; in the BFS mode (Ω(λ(o)) odd) the first discovered, i.e. the
  lexicographically least root-first index sequence of its BFS-tree path (R24 Lemma TB step 5).
- Keys are frozen on T_k ∩ T_{k+1}. For x ∈ T_k, x ≠ o, and x's H_k-path to c := λ(o) avoids o: if it passed o, then Ξ_k(x) = (path) ⊕ θ,
  and Ξ_k(x) = μ with o ⊕ μ = θ would make μ strictly longer than itself. Every vertex on that path other than o has one successor in the
  graph G_σ of Engine.evaluate (Even: σ; Odd: forced), so the BFS-tree path of x is this path. If some vertex of it switches at k, take the
  first one, p (an Even vertex with λ(p) = c ≠ p): its new successor is a strictly better gate-edge target (R15 (d)), so Ξ_{k+1}(p) ▷ Ξ_k(p)
  (P2, R15 (a), ⊕ keeps strictness), and then Ξ_{k+1}(x) = (the unchanged prefix) ⊕ Ξ_{k+1}(p) ▷ Ξ_k(x), so x ∉ T_{k+1}. Hence for
  x ∈ T_k ∩ T_{k+1} the path, and so the key, is the same at k and k+1. (In the longest-path mode the key is the index anyway.)
- So if σ̄_k(o) =: s0 ∈ T_{k+1}, it is still the key-minimum of T_{k+1} ⊆ T_k (keys of distinct exits differ: they end in the exit), and
  σ̄_{k+1}(o) = s0. A relevant change with θ fixed therefore removes s0 from T: ≤ d_o − 1 per run. There are Θ + 1 runs, and ≤ Θ changes
  at θ-changes. □
**Corollary XJ (PROVED, L-NEW, given RESULTS R22 (a)-(b), R24 Lemma R / TB, R25 CAP-1, FB and J1).** In a phase on 𝒞^1O:
- S_o ≤ d_o·(2n + (n + 1)X) and J ≤ S_o (P-N5-LP §4 step 3), so f ≤ n_E(2n − 1)(J + 1) + J = O(n³(1 + X)) (R25 Theorem FB).
- With P-N5-LP Corollary LP′: T = O(m·n⁷·(1 + X) + m·n⁵·K).
- So (J-poly) (R25's open core), NFB-O and the fallback count all follow from (X); per phase the open cores of o-cyclic 𝒞^1O are now X
  (≡ Z up to a factor n, R23 LV′) and K, the wakes, which live in U1 pieces (R24) and in U2 / U3 / U23 stretches ((E), (K_W)).
- DATA (socheck.py, LIB, 255 phases): 0 failures of Lemma TH (incl. its two cases), Lemma SO (incl. "the old choice leaves T"), and J ≤ S_o.
  Maxima: Θ 51 and S_o 49 at n 32 (lev_l_x, d_o 14, X 21); J 17 ≤ S_o 18 at n 48 (jcl_zcl_cu_n48, d_o 18, X 17).

## 5. What this does to the open cores (READING, L-NEW)
- The hoped-for merge fails. Had NO-WAKE held, Corollary LP′ would have replaced (E), (K_W), NFB-O and J by S_o next to X. With
  nowake_cex_n32 the wakes K stay, and they sit exactly in the U2 / U3 / U23 regime of (E) and (K_W): a wake there is a W-change on R or a
  W-flat switch, decided by W lengths and S4a's tie-break while Ξ sees a high level. So box 32 does not close (E) or (K_W); it locates them
  more sharply: the W-blind band (nothing of the honest difference is visible to W above c_w).
- What box 32 does give:
  - Theorem LP on every game: inside a phase the transitions are polynomial in the number of used-level carries. It is the counter
    picture as an inequality, with no 𝒞^1O assumption.
  - On 𝒞^1O, each carry has one of five named causes: a fallback, a crossing, σ̄(o), a wake in a U1 piece (R24), or a wake in U2 / U3 / U23.
  - The gate-level freeze of R25 is vacuous in U2 / U3 (M = ∞). Any future freeze argument there has to use the used level, or W's own
    order.
- Where to push next (READING):
  - (a) The W-length regime. **Lemma KW-LEN (PROVED, L-NEW).** In a U2 / U3 / U23 stretch with rank c_w > rank v for every v ∈ R \ {c_w},
    the non-fallback transitions with a W-change on R number ≤ (f + 1)·|R|·(n − 1). Proof: w (hence c_w) is constant on the stretch, and for
    v ∈ R, P(W(v)) = P(w) ∪ (π_v ∩ V_{>rank c_w}) = P(w) (kind B and U2), or the part of v's path to c_w above c_w, which is empty (kind A).
    So on R, W varies only in length, in one direction (c_w's parity) at S4a steps, since W_{k+1} ⊵ W_k there (R24 TB step 1). Each vertex
    has ≤ n − 1 length changes per fallback-free segment, and there are ≤ f + 1 segments. □ This covers nowake_cex_n32 (c_w = the top
    vertex). With the CASC-U3 Corollary it leaves only (E) in that regime.
  - DATA (kwlev.py, LIB plus u2flat_n32 and nowake_cex_n32): of the 143 transitions with a W-change on R inside U2 / U3 / U23 stretches, 37
    are length-only W-changes, 101 change a W path set at a level ≤ the used level L_k, and 4 (U2, sc32) at a level above it. So outside the
    length regime W path changes ride on the used level; turning that into a bound on K is OPEN.
  - Wakes per run: the wake-maximising climbs (rrclimb.py; seeds nr_u23_n32, u1flat_best_n32, nowake_cex_n32; ~2·10⁵ candidates) stay at ≤ 2
    wakes per run so far. CONJECTURE-level only; no statement.
  - (b) S_o: DONE in §4b (Lemma TH, Lemma SO, Corollary XJ). The tie-break changes are 0 (keys of tied exits are frozen), and the θ-changes
    are F-changes or crossings (H1) or a monotone length (¬H1). So S_o, J and the fallbacks reduce to X.
- After §4b the per-phase open cores of o-cyclic 𝒞^1O are X (≡ Z up to a factor n, R23 LV′) and K (wakes: OPEN in U2 / U3 / U23, bounded in
  U1 pieces by R24).
- Theorem LP holds on every game; DF, BAND, WAKE and LP′ are 𝒞^1O-specific. On ≥ 2 Odd choice vertices ε counts all of Odd's honest
  changes.

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
- W-gaps of the finite R → F dormant edges (wgap.py, LIB): g = lev(W(z), W(a)) > L_k for 979, ≤ L_k for 180, W(z) = W(a) for 8; W(z) ⊴ W(a)
  always (Lemma DF). (Not needed after Lemma WAKE, which excludes R → F wakes without a crossing outright.)
- Climbs against NO-WAKE (nwclimb.py, fitness (failures, steps with a dormant edge, checked steps); seeds x48_rt48_final, lev_l_x,
  x31_rx32, fbref_cex_n32; 2-4·10⁴ candidates each, stopped): 0 failures; pressure up to 108 of 109 checked steps with a dormant edge
  (rt48 seed), but most of that pressure is level-∞ or R → F dormant edges, which can never wake (NOINF; Lemma WAKE). (nwclimb uses the
  first definition of L, own cycle nodes included; NU transitions are rare, above.)
- rrclimb.py (fitness: NO-WAKE failures, finite dormant R → R edges outside route form, all finite dormant R → R edges): from
  u1flat_best_n32 a failure after ~10³ candidates (nowake_cex_n32, §4); runs from nr_u23_n32, u3ev_n16, oc24_s4 continue (§7 for later
  numbers).
- §0 counterexample to (KW-M): experiments/new/box32/instances/kwm_cex_n24.pg, sha1 c2723e082c93aab617d81e63e821d3199e7cb189, n 24, one
  Odd choice vertex (2); n5.py: 21 iterations, 0 fallbacks; check_sol2.py: "zielonka(oink zlk) OK strategies verified"; mblock.py: a U3
  M-block (M = 21) with 15 KW transitions at |R| = 3 (|R| counts o).
- §0 tables: mblock.py on LIB; usedlev.py first showed the rises (129 of 5,355 with the first definition, fallbacks excluded).

## 7. Stamps and files
- experiments/new/box32: c1o_list.py, mblock.py, mblockclimb.py, usedlev.py, lrun.py, rises.py, nowake.py, nwclimb.py, dormant.py,
  wgap.py, rrdorm.py, lcheck.py (the
  consolidated checker of every lemma of §1-§4). instances/: climb results cited here.
