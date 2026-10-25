# Referee packet P-N5-LP: the used-level freeze and a carry bound for a phase of N5 (box 32)
L-NEW successor 12 (Opus 5.5, D15/D18). Written 2026-10-25 00:4xZ by date -u, at the Lead's request (00:24Z). Frozen at this commit:
corrections go in a fixes file, never here.
- Self-contained: definitions, statements, full proofs, the location of every dependency, and the data with the scripts that produce it.
- Source text: docs/new/N5-L-box32.md §1-§4 (box 32 write-up). Where the two differ, this packet governs.
- Status: L-NEW's proofs, unrefereed. §1-§2 hold on EVERY parity game inside a phase. §3-§4 are on 𝒞^1O (exactly one Odd vertex o with
  out-degree > 1). Lemmas about the candidate N5 (SPEC tie-breaks). Not a running-time bound, not a TARGET.md claim, not a step-4 pass.
  G-N5-TIME stays OPEN.
- Labels per statement: PROVED (L-NEW), FALSE, OPEN, DATA, READING.
- Statements: §1 Lemma U, Lemma HI, Lemma UL, Lemma GR, Lemma NU; §2 Theorem LP; §3 Lemma DF, Lemma BAND, Lemma WAKE; §4 Corollary LP′.
  §5 refuted forms and open items (not to sign). §6 data.

## 0. Objects and dependencies
- N5 and its SPEC: docs/new/N5-ssi-global.md (S1 valuations and Engine.evaluate, S2 improving edges, S4a / S4b / S4c, FIX 2-4); code
  experiments/new/n5.py, experiments/si/si.py l.78-205.
- Valuations, as RESULTS R25 / docs/si/P-N5-FB-box7.md §0-§1 (signed): x = (c, P, ℓ), cycle node c, P = the path vertices of rank > rank c,
  ℓ = the path length; ⊴ = Even's order; u ⊕ x one more step; lev(x, y) := ∞ if the cycle nodes differ, else the top rank of P(x) Δ P(y),
  else −1 if only the lengths differ, ⊥ if x = y; COARSE_L(x) := (c, P ∩ V_{>L}) for −1 ≤ L < ∞, COARSE_⊥ := identity; facts
  (C1) x ⊴ y ⇒ COARSE_L x ⊴_L COARSE_L y, (C2) COARSE_L x = COARSE_L y ⟺ lev(x, y) ≤ L, (C3) ⊴_L antisymmetric, (C4) COARSE_L(u ⊕ x) is a
  function of u and COARSE_L(x) (and keeps x's cycle node).
- Ξ_k = Θ_{H_k}, the honest valuation of σ_k = the play value in H_k := the (σ_k, σ̄_k)-graph (ENG-1, R25 (a); SPEC's σ̄ = VJ00's procedure).
  λ_k(v) := the cycle node of Ξ_k(v). W_k := the play value of (σ_k, τ_k). Gate (improving) edge at k: (y, z) with z ≠ σ_k(y) and
  Ξ_k(z) ▷ Ξ_k(σ_k y) (SPEC S2); its level lev(Ξ_k(σ_k y), Ξ_k(z)) ≥ −1.
- VJ00 = Jurdziński & Vöge, BRICS RS-00-48 (pdf sha256 485a12de432a2a8c…, opened by L-NEW succ. 12 on 2026-10-25 00:35Z from
  www.brics.dk/RS/00/48/BRICS-RS-00-48.pdf; the same file as R25):
  - p. 14-15, Prog(Ξ, (v, w)): (P1) Λ(v) = Λ(w); (P2) if Λ(v) ≠ v then Π(v) = Π(w) ⊕ v; (P3) if Λ(v) = v then Π(v) = (∅, 0).
  - p. 15, Lemma 5.2: Ξ is locally progressive for σ and τ iff Ξ = Θ_{στ}; in its proof the cycle node is the max≤ vertex of the play's
    cycle.
  - p. 16, (11): Ω_σ = Θ_{σσ̄}, "hence … Θ_{σσ̄} ⊴ Θ_{στ}, for all strategies τ". Used as (XW): Ξ_k ⊴ W_k.
  - p. 19-21, Lemma 5.8, directions 2 ⇒ 3 ⇒ 1 (proved there from Lemma 5.7 and Lemma 5.2): if σ has an improvement, σ is not a maximum
    element of (Strategies, ⊑). Used only in Lemma DF, on a one-player arena.
- Signed results used: R15 (a) Ξ_k ⊴ Ξ_{k+1}; R15 (d) every switched Even vertex moves to a gate-edge target of the current state
  (σ_{k+1}(y) ∈ {σ_k(y)} ∪ Iσ_k(y)); every N5 iteration changes σ or τ (SPEC S4: if S4a and S4b change nothing, the S4c fallback switches
  at least one vertex, since Iσ ∪ Iτ ≠ ∅); R17 (F1) the S4a result is a one-player optimum of its arena
  (dominates every strategy of the arena pointwise); R19 (a) Lemma G (a): on 𝒞^1O, off R, Ξ = W; R22 / R24 (R1): on a piece in route form,
  Ξ(v) = π_v ⊕ θ and W(v) = π_v ⊕ w for v ∈ R; R24 Theorem U1; R25 (d) Theorem FB and (e) J1.
- PHASE: a run of transitions with λ_Ξ and τ constant (R21 / R25 setting; only these two are used). On 𝒞^1O: R_k := {o} ∪ {v : v's
  (σ_k, τ_k)-play reaches o}, F_k := V \ R_k; a CROSSING is a transition with R_k ≠ R_{k+1}; c_θ := λ_Ξ(o), c_w := the cycle node of W(o).
- v is its OWN CYCLE NODE at k if λ_k(v) = v.

## 1. The used level (PROVED, L-NEW; any game, inside a phase)
Definitions.
- RELEVANT CHANGES at k → k+1: an Even y with σ_{k+1}(y) ≠ σ_k(y) and λ_k(y) ≠ y; an Odd u with σ̄_{k+1}(u) ≠ σ̄_k(u) and λ_k(u) ≠ u.
- USED LEVEL L_k := the max of lev(Ξ_k(old successor), Ξ_k(new successor)) over the relevant changes; ⊥ if there is none or all of them
  are ⊥. A transition is NU if L_k = ⊥ and RELEVANT otherwise.
- For ℓ ≥ 0, u_ℓ is the vertex of rank ℓ. A valuation x with rank(c(x)) < ℓ is ℓ-GOOD if (u_ℓ ∈ P(x)) ⟺ (Ω(u_ℓ) even).
  G_ℓ(k) := {v : rank λ(v) < ℓ, Ξ_k(v) ℓ-good} (λ is fixed in the phase).
- Comparison: R25's M_k is the max level over ALL gate edges; Even's part of L_k is ≤ M_k (switches go to gate edges, R15 (d)).

**Lemma U (used-level freeze).** For every transition k → k+1 of a phase: L_k < ∞, and COARSE_{L_k}(Ξ_{k+1}(v)) = COARSE_{L_k}(Ξ_k(v)) for
every v. In particular an NU transition leaves Ξ unchanged.
Proof.
1. L_k < ∞. Let y be a relevant Even vertex. By (P1) on the H_k-edge (y, σ_k y), λ_k(σ_k y) = λ_k(y). By (P1) at k+1 and the phase,
   λ_k(σ_{k+1} y) = λ_{k+1}(σ_{k+1} y) = λ_{k+1}(y) = λ_k(y). So the two valuations have the same cycle node and their lev is finite. The
   same for a relevant Odd vertex.
2. Fix v and c := λ_k(v) = λ_{k+1}(v). c is the top of the cycle of v's plays, so λ_k(c) = λ_{k+1}(c) = c and Ξ_k(c) = Ξ_{k+1}(c) = (c, ∅, 0)
   by (P3) (Lemma 5.2 for H_k and H_{k+1}). Let p_0 = v, …, p_s = c be v's H_{k+1}-path up to its first visit of c.
3. For i < s: λ_{k+1}(p_i) = c by (P1) along H_{k+1}-edges, so p_i ≠ c is not its own cycle node (λ is the same at k). Hence if p_i's successor
   in H_{k+1} differs from its successor in H_k, the change is relevant, of level ≤ L_k, and COARSE_{L_k}(Ξ_k(p_{i+1})) =
   COARSE_{L_k}(Ξ_k(succ_{H_k} p_i)) by (C2). (If L_k = ⊥: equality of the values.)
4. Downward induction on i, from i = s (step 2). For i < s: Ξ_{k+1}(p_i) = p_i ⊕ Ξ_{k+1}(p_{i+1}) by (P2). By (C4) its COARSE_{L_k} is a
   function of p_i and COARSE_{L_k}(Ξ_{k+1}(p_{i+1})) = COARSE_{L_k}(Ξ_k(p_{i+1})) (induction) = COARSE_{L_k}(Ξ_k(succ_{H_k} p_i)) (step 3).
   By (C4) and (P2) at k this is COARSE_{L_k}(Ξ_k(p_i)). Take i = 0. □
- Relation to R25: this is Lemma TAME (proof of COARSE-SI (b) via Claim (T)) with M_k replaced by L_k. TAME uses M_k only as an upper bound
  on the levels of the changed edges, and changes at own cycle nodes can be dropped because no path before a first visit of c contains one.

**Lemma HI (high gate edges are frozen).** Let k → k+1 be a transition of a phase with L := L_k ≠ ⊥, and let y be an Even vertex that is not
an own cycle node switched at k. For every z and every ℓ > L: (y, z) is a gate edge of level ℓ at k iff it is a gate edge of level ℓ at k+1.
Proof.
- COARSE_L(Ξ_{k+1}(x)) = COARSE_L(Ξ_k(x)) for every x (Lemma U). COARSE_L(Ξ_k(σ_{k+1} y)) = COARSE_L(Ξ_k(σ_k y)): y is unswitched, or its
  switch is relevant of level ≤ L ((C2)). So the COARSE_L values of both ends of (y, z), relative to y's current successor, are the same at
  k and k+1.
- By (C2), lev > L iff the COARSE_L values differ. Then the level (∞, or the top rank of the path sets restricted to V_{>L}) and the
  direction (reward of the cycle node if they differ, else the parity of that top vertex) are functions of the two COARSE_L values.
- z = σ_k(y) at k+1 and z = σ_{k+1}(y) at k have level ≤ L, so they are not in either set. □
- Consequence: M_{k+1} = M_k if M_k > L_k, and M_{k+1} ≤ L_k if M_k = L_k. (R25 MONO is the tame case.)

**Lemma UL.** Inside a phase, L_k = ℓ ≥ 0 is never attained by a relevant switch of the Even vertex u_ℓ.
Proof. Let y = u_ℓ switch from a = σ_k(y) to z with lev(Ξ_k(a), Ξ_k(z)) = ℓ, and c := λ(y); rank c < ℓ because P ⊆ V_{>rank c}. z is a
gate-edge target (R15 (d)), so Ξ_k(z) ▷ Ξ_k(a), and their path sets differ first at y.
- Ω(y) odd: the better one, z, lacks y, so y ∈ P(Ξ_k(a)): a's H_k-path passes y and then returns to σ_k(y) = a. So a lies on an H_k-cycle
  through y. Its top has rank ≥ ℓ > rank c, and the cycle node of a vertex on a cycle is that cycle's top (Lemma 5.2's proof). So
  λ_k(a) ≠ c = λ_k(y), against (P1).
- Ω(y) even: y ∈ P(Ξ_k(z)). By Lemma U, Ξ_{k+1}(z) agrees with Ξ_k(z) above ℓ, and Ξ_{k+1}(z) ⊵ Ξ_k(z) (R15 (a)), so Ξ_{k+1}(z) is not worse at
  bit ℓ: y ∈ P(Ξ_{k+1}(z)). So z's H_{k+1}-path passes y, and with σ_{k+1}(y) = z, z lies on an H_{k+1}-cycle through y of top rank ≥ ℓ.
  So λ_{k+1}(z) ≠ c = λ_k(z), against the phase. □

**Lemma GR (ℓ-goodness).** Inside a phase, fix ℓ ≥ 0.
- (a) If L_k = ⊥ or L_k ≤ ℓ, then G_ℓ(k) ⊆ G_ℓ(k+1).
- (b) If L_k = ℓ is attained by a relevant Even switch y: a → z, then y ∉ G_ℓ(k) and y ∈ G_ℓ(k+1).
Proof.
- (a) COARSE_ℓ is a function of COARSE_{L_k}, so COARSE_ℓ(Ξ_{k+1}(v)) = COARSE_ℓ(Ξ_k(v)) (Lemma U). Let rank λ(v) < ℓ. If bit ℓ of the
  path sets differs, it is the top difference, so the comparison is decided by Ω(u_ℓ), and Ξ_{k+1}(v) ⊵ Ξ_k(v) (R15 (a)) makes Ξ_{k+1}(v)
  the ℓ-good one.
- (b) y ≠ u_ℓ (Lemma UL). Ξ_k(z) ▷ Ξ_k(a) (gate edge, R15 (d)) with top difference at ℓ, so Ξ_k(z) is ℓ-good and Ξ_k(a) is ℓ-bad, and
  rank λ(y) < ℓ. y ⊕ x has the same bit ℓ as x (rank y ≠ ℓ). So Ξ_k(y) = y ⊕ Ξ_k(a) (P2) is ℓ-bad, and Ξ_{k+1}(y) = y ⊕ Ξ_{k+1}(z) (P2 at
  k+1) is ℓ-good, since Ξ_{k+1}(z) is ℓ-good by (a). □

**Lemma NU.** Inside a phase, a run of consecutive NU transitions has at most Σ_{y Even}(deg(y) − 1) ≤ m − n transitions.
Proof.
- Ξ is constant on the run (Lemma U).
- Every transition of a phase changes σ: τ is constant and every N5 iteration changes σ or τ (§0).
- At an NU transition every switched Even y is an own cycle node: otherwise the switch is relevant, of level ≥ −1 (its new successor is a
  gate-edge target, strictly better).
- Each such switch moves to a gate-edge target: Ξ(σ_{k+1} y) ▷ Ξ(σ_k y) with Ξ fixed. So Ξ(σ(y)) strictly increases along the run, and y
  switches at most deg(y) − 1 times. □

## 2. Theorem LP (PROVED, L-NEW; any game)
Statement. Let a phase have T transitions, T_rel of them relevant. Let ρ be the number of RISES (consecutive relevant transitions k < k′,
only NU transitions between, with L_{k′} > L_k), and ε the number of relevant transitions whose used level is attained only by Odd
changes. Then
    T ≤ (m − n + 1)(T_rel + 1)   and   T_rel ≤ (n + 1)(ρ + 1)·n(n − 1) + ε   (n ≥ 2).
Proof.
1. NU runs: ≤ T_rel + 1 of them, each with ≤ m − n transitions (Lemma NU). This gives the first bound.
2. L-RUNS: maximal blocks of consecutive relevant transitions (NU transitions between them ignored) with equal used level. Between two rises
   the run values strictly decrease and lie in {−1, 0, …, n − 1}. So there are ≤ (n + 1)(ρ + 1) runs.
3. A run of value ℓ ≥ 0: each of its transitions not counted in ε has L = ℓ attained by a relevant Even switch, which adds that vertex to G_ℓ
   (Lemma GR (b)). G_ℓ loses no vertex during the run, NU transitions included (Lemma GR (a)). So the run has ≤ n such transitions.
4. A run of value −1: COARSE_{−1}(Ξ) (cycle node and full path set) is constant on the run (Lemma U), so only lengths change. Each transition
   not in ε has a relevant Even switch y: a → z with Ξ_{k+1}(y) = y ⊕ Ξ_{k+1}(z) ⊵ y ⊕ Ξ_k(z) ▷ y ⊕ Ξ_k(a) = Ξ_k(y) (R15 (a), (P2); y ⊕ keeps
   order and strictness between values of one cycle node). So some vertex's length changes strictly. Each vertex's length lies in
   [0, n − 1] and moves in one direction (fixed by the parity of its fixed cycle node). So ≤ n(n − 1) such transitions.
5. Sum over the runs, with max(n, n(n − 1)) = n(n − 1). □
- Reading (not to sign): inside a phase the value vector is a counter whose digit ℓ (the set G_ℓ) only fills while the used level stays at
  ℓ. Theorem LP says: transitions ≤ poly(n, m)·(1 + carries + ε). It bounds nothing by itself; it moves the count to the carries.

## 3. Dormant edges and wakes on 𝒞^1O (PROVED, L-NEW)
**Lemma DF.** On 𝒞^1O, let k → k+1 be an S4a transition (no fallback) of a phase, and let (y, z) be an edge of the arena H_k that is a gate
edge at k+1. Then a := σ_{k+1}(y) ∈ R_{k+1}.
Proof.
- σ_{k+1} is a maximum strategy of the one-player arena H_k against τ (SPEC S4a; R17 (F1)), whose valuation is W_{k+1} (Odd's moves are
  fixed). By VJ00 Lemma 5.8 (2 ⇒ 3 ⇒ 1) a maximum has no improvement in its arena. So W_{k+1}(z) ⊴ W_{k+1}(a).
- If a ∈ F_{k+1}: Ξ_{k+1}(a) = W_{k+1}(a) (R19 (a)), so Ξ_{k+1}(z) ⊴ W_{k+1}(z) ((XW)) ⊴ W_{k+1}(a) = Ξ_{k+1}(a), against (y, z) being a gate
  edge at k+1. □
**Lemma BAND.** On 𝒞^1O, at a state with both frames in route form ((R1) on R) and c_θ ≠ c_w, let (y, z) be a gate edge of level ℓ ≥ 0 with
a := σ(y) ∈ R and z ∈ R, and W(z) ⊴ W(a). Then rank c_θ < ℓ < rank c_w, and P(W(z)) = P(W(a)).
Proof.
- π_x and θ's path are disjoint: under H1, o lies on no honest cycle; if λ_Ξ(o) = o, θ's path is empty. So P(Ξ(z)) Δ P(Ξ(a)) =
  (π_z Δ π_a) ∩ V_{>rank c_θ}; likewise P(W(z)) Δ P(W(a)) = (π_z Δ π_a) ∩ V_{>rank c_w} (the same argument for w; under H2 o is on no W-cycle,
  and if λ_W(o) = o then w's path is empty).
- ℓ ≥ 0 is the rank of the top t of (π_z Δ π_a) ∩ V_{>rank c_θ}, so ℓ > rank c_θ. If rank t > rank c_w, W's top difference is the same t
  with the same verdict, so W(z) ▷ W(a): excluded. t ≠ c_w, because in route form c_w ∈ F ∪ {o} and routes stop before o. So ℓ < rank c_w,
  and every vertex of π_z Δ π_a has rank ≤ ℓ < rank c_w: the W path sets agree. □
Definition. Let k < k′ be consecutive relevant transitions of a phase (only NU transitions between) with no fallback in [k, k′] and
R constant on [k, k′ + 1]. A WAKE at k′ is a relevant Even switch y: a → z at k′ of level > L_k. K := the number of transitions with a wake.
**Lemma WAKE.** On 𝒞^1O, a wake y: a → z has a ∈ R and z ∈ R. If the state at k′ has both frames in route form, it is in a U1 piece
(c_w more relevant than c_θ).
Proof.
- (y, z) is a gate edge at k′ of level ℓ > L_k. y is not an own cycle node (its switch is relevant), so it does not switch at the NU
  transitions between k and k′ (only own cycle nodes do, Lemma NU's proof), and Ξ is fixed there; so y's gate edges are unchanged there. Lemma
  HI at k carries the gate edge back to k. So (y, z) is a gate edge at every step of [k, k′], in particular an edge of the arena H_{k′−1};
  and k′ − 1 → k′ is an S4a step. Lemma DF at that step: a = σ_{k′}(y) ∈ R.
- If z ∈ F_{k′} = F_{k′+1} (R is constant), y's σ_{k′+1}-play enters F and never reaches o, so y ∉ R_{k′+1}. But y ∈ R_{k′} (its play
  passes a) and R_{k′} = R_{k′+1}. So z ∈ R.
- Route form: at k′, W_{k′}(z) ⊴ W_{k′}(a) (Lemma DF's first step at k′ − 1 → k′) and (y, z) is a gate edge with a, z ∈ R, so Lemma BAND
  gives rank c_θ < ℓ < rank c_w. □

## 4. Corollary LP′ (PROVED, L-NEW; 𝒞^1O)
Statement. In a phase on 𝒞^1O with f fallback transitions, S_o transitions with a relevant change of σ̄(o) (λ(o) ≠ o), X crossings and K
wakes,
    T ≤ (m − n + 1)·((n + 1)(2f + S_o + 2X + K + 1)·n(n − 1) + S_o + 1),   with   f ≤ n_E(2n − 1)(S_o + 1) + S_o,
so T = O(m·n⁵·(1 + S_o + X + K)).
Proof.
1. ε ≤ S_o: an Odd-only used level comes from a relevant Odd change, and every Odd vertex but o has one successor.
2. ρ ≤ 2f + S_o + 2X + K. Take a rise k < k′. If [k, k′] contains a fallback or a crossing: each transition lies in at most two intervals
   [k, k′] of consecutive relevant transitions, so ≤ 2f + 2X such rises. Otherwise, if every relevant Even level at k′ is ≤ L_k, the level
   L_{k′} > L_k is attained by a relevant Odd change at k′, i.e. by σ̄(o) (≤ S_o rises); else k′ has a wake (≤ K rises).
3. Theorem FB (R25 (d)): f ≤ n_E(2n − 1)(J + 1) + J, J = the non-tame transitions. J ≤ S_o: by J1 (R25 (e)) a non-tame transition switches
   σ̄(o) at a level above M_k; if λ(o) = o that change is not relevant, so L_k ≤ M_k (Even switches are gate edges) and Lemma U gives
   COARSE_{M_k}(Ξ) unchanged, i.e. the transition is tame. So the change is relevant.
4. Theorem LP with steps 1-3. □
- Every wake is a σ-change at a vertex of R, i.e. an R-changing transition: of a U1 piece in route form (Lemma WAKE; R24 Theorem U1 bounds
  them by O((f + 1)|R|³) per piece), or of a U2 / U3 / U23 stretch (bounded by the CASC-U2 / CASC-U3 corollaries in terms of the open (E)
  and (K_W); P-N5-U23 with its fixes file).

## 5. Refuted forms and open items (not to sign)
- (NO-WAKE) "K = 0": FALSE. experiments/new/box32/instances/nowake_cex_n32.pg (n 32, sha1 3a56e3fb94f3c84684d01fc87ff3c7e9a8d7eb3f, one
  Odd choice vertex o = 27; n5.py 9 iterations, 2 fallbacks; check_sol2.py "zielonka(oink zlk) OK strategies verified"). Transitions 0, 1
  are S4a steps of one phase, R constant (|R| 30), state U3 (c_θ = o of rank 15; c_w = vertex 13, the top-rank vertex). L_0 = 26; at
  transition 1, y = 11 switches 22 → 9 at level 30. Mechanism: c_w is the top vertex, so W compares lengths only; the same S4a step shortens
  9's route to a W-tie (13, ∅, 7) with 22, and the tie-break takes 9.
- The coarse freeze at R25's gate level M is vacuous for most residual transitions of (NH') (M_k = ∞ at 52 of 69 U2 / U3 KW transitions and
  at both U3 events in the 220-file library); (KW-M) "≤ |R| KW transitions per M-block" FALSE (instances/kwm_cex_n24.pg, sha1 c2723e08…, a
  U3 M-block with 15 KW at |R| 3; Lead re-run). DATA / FALSE, docs/new/N5-L-box32.md §0.
- OPEN: S_o per phase; X per phase; K per phase in U2 / U3 / U23 states (the regime of (E) and (K_W)).

## 6. Data (DATA, not proof; experiments/new/box32)
- LIB = the 220 files listed by c1o_list.py 64 (every experiments/**/*.pg in 𝒞^1O with n ≤ 64; 5,355 phase transitions). RAND =
  lcheck.py --rand 3000 8 24 3203 (1,375 phase transitions). The traces are box31/u23check.py's rows (box29/otherx.py step); (iterations,
  fallbacks) equal experiments/new/n5.py run() on every 11th LIB file (20 of 20).
- lcheck.py (checks every statement of §1, §2 and §4 (i)-(ii) at every transition of every phase): 0 failures on LIB and RAND of Lemma U
  (incl. NU), HI, UL, GR (a) and (b), Theorem LP (both inequalities), ε ≤ S_o, ρ ≤ 2f + S_o + 2X + K. NU transitions: 15 LIB, 194 RAND,
  never more than 1 per phase.
- Rises (LIB, 413): 284 with a fallback, 128 from σ̄(o), 1 with a crossing (fbref_cex_n32, transitions 51-52), 0 wakes.
- Per-phase maxima (LIB): T 110 at n 48 (x48_rt48: f 21, S_o 2, X 70, ρ 11, ε 1); ρ 14 (fbp48_rt48, n 48); S_o 49 (lev_l_x, n 32);
  X 84 (b6_xl_n48). Constant-level runs ≤ 55 at n 64; level −1 runs ≤ 8.
- Dormant edges (dormant.py, LIB, 1,637 steps of wake type; o counted in R): finite level R → F 1,167, R → R 40; level ∞ 644; F → F 0 and
  F → R 0 (Lemma DF). rrdorm.py: the 40 R → R steps are 35 route-form steps, all in the band of Lemma BAND (c_w above c_θ), and 5 U23 steps.
- Wakes: 0 in LIB and RAND; nowake_cex_n32 from rrclimb.py (seed u1flat_best_n32); the wake-maximising climb (rrclimb.py, seed nr_u23_n32)
  reached 2 wakes in one run after ~3·10⁴ candidates.
- S_o structure (socount.py, LIB): of the relevant σ̄(o) changes, 1,229 change θ at the same transition and 4 do not (each one an exit
  leaving the minimiser set; no pure tie-break move).
