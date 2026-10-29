# T32: cross-field techniques for the current N5 frontier (L-LIT, 2026-10-29)

Asked by the Lead at 09:59Z (date -u), under owner ruling D18 (docs/DECISIONS.md, verbatim):
> Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and
> computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed
> without asking me questions. Clearly distinguish proven results from conjectures and open problems.

- **Scope.** No N5 runs, no contact. One brute-force self-check of an elementary lemma (§E6, docs/lit/T32-match-check.py).
- **N5 objects, as stated by the lanes (read, not re-derived).**
  - (O1) A maximal REL-admissible segment [a, b] of a fallback-free run: two frames (W, honest), frame-wise settled sets S^W_t, S^H_t,
    sinks, the deadlock broken by an INTERMEDIATE switch (claude/l-si docs/si/N5-LAY-box27.md §1-§6). CONJECTURE SEG-COUNT:
    b − a ≤ number of Even vertices that switch in [a, b]. DEAD there: SEG-LAST, W-GROW, H-GROW, SINK-GROW, PSI-DROP.
  - (O2) SEG(S), the number of maximal REL segments of a run S. RESULTS R83: SEG(S) − 1 ≤ G(S) + CF(S); GATE-RISE bounds G by the
    gates' Ξ-changes XR plus TIE/CYC/THRU cases. CONJECTURE SEG-RUN: SEG = O(n) (claude/l-si docs/si/N5-GRUN-box25.md §4-§5).
  - (O3) P-changes of a vertex v in a phase: P_t := P(Ξ_t v) ⊆ ranks above rank(λ(v)), ordered by the signed weight
    weight(A) = Σ_{r ∈ A} s(r)2^r. RESULTS R84: the top changes ≤ n − 1 times; the P-changes under a fixed top are NOT bounded
    (71 in one phase at n = 41; L-RED R104: "RESET 133 of PCH 157").
- **Not repeated from T28** (docs/lit/T28-n5-techniques.md): path-vector routing (Daggitt-Griffin), Post-Ye flux, parametric shortest
  paths, USO face sinks, GKK/AESL, tropical arrangements, Davenport-Schinzel, Tarski / EPRY. Cross-referenced where they bear on O1-O3.
- **Labels.**
  - **PROVED (source)**: a theorem of the opened source, for the source's own objects.
  - **PROVED (L-LIT, unrefereed)**: an elementary argument written here; needs a referee before anyone relies on it.
  - **CONJECTURE**: any statement about N5 that is not proved; every transfer below is one.
  - **READING**: L-LIT interpretation. **ASSUMPTION**: stated in one line where used.
- Pages: PDF pages unless marked. sha256 of every PDF in notes/L-LIT.md "Sources opened" (2026-10-29 rows).

## 0. Summary for the Lead

| # | technique (field) | source opened | N5 object | verdict |
| --- | --- | --- | --- | --- |
| E1 | Full Reversal as a min-plus linear system; work vectors Lipschitz along edges (distributed routing / max-plus algebra) | arXiv 1111.4600 v1 §8.3 | O1 per-vertex switch counts; O2 | BLOCKED by the fixed min-plus law; one cheap test |
| E2 | least action principle for abelian networks (chip-firing / automata networks) | arXiv 1309.3445 v3 Lemma 4.3, Thm 4.9 | O1 | BLOCKED by local abelianness (killed by seglast_kill_n29) |
| E3 | alternating fixpoint for the well-founded semantics, progressive operator template (W1)-(W2) (logic programming) | arXiv cs/0101014 v1 Alg. 1, Thm 3.1, (W1)-(W2) | O1 | BLOCKED by (W2); explains why SINK-GROW died |
| E4 | composition: R83 + GATE-RISE + GRUN's XR ≤ PCH·n bound + E6 | (fleet results) | O2 → O3 | REDUCTION: SEG-RUN follows from a bound on non-matched P-changes |
| E5 | 1-1 exchange decomposition and rank-replacement potential; the 1-2-exchange counter (algorithmic game theory: matroid congestion games) | ECCC TR06-067 Thm 3, Lemma 4, Thm 7, Def. 8, Lemmas 9-10 | O3 | **PROMISING** (as a reduction + a measurement) |
| E6 | the transfer of E5 to signed path sets (Lemma MATCH-Φ) | — | O3 | PROVED (L-LIT, unrefereed); a REDUCTION, not a bound |
| E7 | shadow paths on 0/1 polytopes: auxiliary-objective monotonicity and nested faces (LP / polyhedral combinatorics) | arXiv 2111.14050 v1 Cor. 1, Thm 5, Lemma 5 | O3 | **PROMISING** as two testable hypotheses (HAM-MONO, NEST-FACE) |
| E8 | link-reversal work bounds (Busch-Tirthapura), Gawlitza-Seidl min/max strategy iteration (abstract interpretation), Van Gelder JCSS 1993, Schurr-Szabó | not opened (§8) | O1, O2 | none |

**Headline (READING).** For O3 the cross-field literature has a sharp dichotomy that matches R84's "binary counter below the top":
in matroid congestion games (ARV, E5) an improving move that decomposes into pairwise non-worsening 1-1 exchanges raises a
polynomial potential (Lemma 4), and every non-matroid structure admits a 1-2 exchange from which ARV build an exponential binary
counter (Def. 8, Lemma 10). N5's signed weight is decided by the largest rank of the symmetric difference (R84 Fact DELTA), which is
exactly a "one element outweighs many" (1-k) exchange. E6 proves the positive half for N5: P-changes that admit a non-worsening
1-1 matching raise Φ(P) = Σ ±pos(r) by ≥ 1, so a vertex has at most (K(K+1)/2)(NM + 1) + NM P-changes in a phase, NM the
non-matchable ("carry") changes, K ≤ n − 1. Via E4 this turns SEG-RUN into one count: carries per (vertex, phase). That count is
OPEN and is where an exponential example would have to live.

## 1. E1: Full Reversal routing as a min-plus linear dynamical system (O1, O2)
**Source.** Charron-Bost, Függer, Nowak, "On the Transience of Linear Max-Plus Dynamical Systems", arXiv 1111.4600 v1 (20 Nov 2011),
§8.3 (PDF pp.31-32), restating Charron-Bost, Függer, Welch, Widder (SIROCCO 2011; TALG 11(3) 2015, not opened).
- **Exact statements (PROVED, source).**
  - Full Reversal: "Each sink reverses all its (incoming) edges"; the greedy execution reverses all sinks of G_t at once. W_i(t) :=
    "the number of reversals of node i until iteration t".
  - "the sequence of work vectors can be described as a min-plus linear dynamical system": W(0) = 0 and
    −W(t + 1) = (−A) ⊗ (−W(t)), with A_{i,j} = 0 if (j, i) is an edge of G_0, 1 if (i, j) is an edge of G_0, +∞ otherwise; i.e.
    W_i(t + 1) = min( min_{(j,i) ∈ G_0} W_j(t), min_{(i,j) ∈ G_0} W_j(t) + 1 ).
  - Routing case (destinations carry self-loops, G_0 minus loops weakly connected and acyclic): "an upper bound on the termination
    time of Full Reversal routing starting from initial graph G_0, for N ≥ 3, is θ(G_0) ≤ (N − 1)²"; on trees θ(G_0) ≤ 2(N − 1).
- **Mechanism (READING).** Destinations have W ≡ 0, and the recursion makes W 1-Lipschitz along every edge at every time, so a node's
  count is at most its distance to a destination; the quadratic time bound is a transience bound of a fixed min-plus matrix.
- **N5 object.** Destinations ↔ vertices settled in their frame (T, and S^W_t / S^H_t); edges ↔ the chain maps jW, jH of LAY §1;
  W_i(t) ↔ the switches of an Even vertex of E_b in [a, t]. LAY §6 already notes per-vertex switch counts in one segment are NOT
  bounded by a constant (one vertex switches 48 times in red/ul/ladderd0_k48_n156), so a per-vertex bound must be a distance-type
  bound like Full Reversal's, not a constant.
- **Hypotheses.**
  - (a) A FIXED min-plus law W(t + 1) = A ⊗′ W(t): **fails** for N5. S4a is a joint optimum over the arena of state t, and which
    neighbours constrain a vertex changes with t (the sinks of LAY §1 are defined by the moving sets U^W_t, U^H_t).
  - (b) The time-uniform Lipschitz inequality SW_{[a,t]}(v) ≤ SW_{[a,t]}(w) + 1 for w = jW(v) or jH(v): not proved for N5;
    CONJECTURE LIP. LAY §6's ladder (an H-sink making 11 intermediate switches "while a both-sink snake 12, 11, 10, … finalizes one
    vertex per step") is the first test: if the snake is the H-sink's chain, LIP is DEAD there. Not measured by L-LIT.
- **Verdict.** BLOCKED by (a). Test for L-SI/L-COMP: LIP on ladderd0_k12_n48 [0, 13] and on seglast_kill_n29.

## 2. E2: least action principle for abelian networks (O1)
**Source.** Bond, Levine, "Abelian networks I. Foundations and examples", arXiv 1309.3445 v3 (12 Feb 2016), §4.
- **Exact statements (PROVED, source).**
  - Lemma 4.3 (Least Action Principle, p.14): "If w is legal for x.q and w′ is complete for x.q, then |w|_a ≤ |w′|_a for all a ∈ A."
  - Lemma 4.4 (Halting Dichotomy, p.15): if a finite complete execution exists, "Every legal execution for x.q is finite, there exists
    a complete legal execution for x.q, and any two complete legal executions w, w′ for x.q satisfy |w| = |w′|."
  - Thm 4.9 (p.17): "If N halts on input x.q, then u = [x.q] is the unique minimizer of (5)" (a monotone integer program).
  - The hypothesis carried by every processor: abelian, i.e. the processed letters commute (Lemma 4.2's proof: "Since t_a and t_b
    commute for all a, b ∈ A").
- **N5 object.** A REL segment as an execution; letters = Even switches; "complete" = reaching σ_b. If N5's in-segment dynamics were
  abelian, Lemma 4.3 with w′ = "each switcher jumps once to its target" would give ≤ 1 switch per vertex, hence SEG-LAST and
  SEG-COUNT at once.
- **Hypothesis.** Local abelianness: **fails** for N5, and the fleet's own kill instance is the witness. seglast_kill_n29 (LAY §4): at
  t = 2 the only switch is vertex 1's 9 → 23, an intermediate switch, and vertex 1 switches again at t = 3 (1 → 19); the direct one-jump execution is
  not reachable in the order S4a takes. Per-vertex counts up to 48 in one segment (LAY §6) contradict the abelian bound outright.
- **Verdict.** BLOCKED by local abelianness. READING: the intermediate switch is exactly a non-commuting pair (the H-sink's move
  changes which arena edges are improving for the W-sink).

## 3. E3: the alternating fixpoint and the progressive-operator template (O1)
**Source.** Lonc, Truszczyński, "On the problem of computing the well-founded semantics", arXiv cs/0101014 v1 (TPLP), §2-§3.
Van Gelder's own paper (JCSS 47, 1993; DOI 10.1016/0022-0000(93)90024-Q) was NOT opened (§8); the statements below are Lonc-
Truszczyński's.
- **Exact statements (PROVED, source).**
  - p.4: "It is well known that GL is antimonotone. Consequently, GL² = GL ∘ GL is monotone"; T_wfs = lfp(GL²), F_wfs = lfp(A),
    A(M) = complement of GL(complement of GL(M)).
  - Algorithm 1 (Van Gelder), p.5: alternate T := GL(F), F := A-step "until no change in F".
  - Thm 3.1 (p.5-6): the operator B is monotone, A(F) ⊆ B(F), B(F) ⊆ F_wfs for F ⊆ F_wfs, lfp(B) = F_wfs, and B(F) ⊇ F.
  - Template (p.7): any increment operator Δ_w with "(W1) Δ_w(F, Q) ⊆ F̄ \ LM(Q)" and "(W2) Δ_w(F, Q) = ∅ if and only if
    F̄ \ LM(Q) = ∅" gives a correct algorithm; every iteration adds ≥ 1 atom, hence ≤ |At(P)| iterations and the
    "O(|At(P)| × size(P)) running-time estimate for the alternating-fixpoint algorithm" (p.9).
- **N5 object.** The two frames are the two interleaved fixpoints (W-frame ↔ the true/under-estimate, honest frame ↔ the
  false/over-estimate); W-GROW / H-GROW / SINK-GROW are exactly "(W2): every step grows S^W or S^H when not finished".
- **Hypothesis.** (W2): **fails** for N5. LAY §4: seglast_kill_n110 / n29 have a step at which neither S^W nor S^H grows (the
  deadlock) although the segment is not finished; SINK-GROW is DEAD for that reason. In the alternating fixpoint (W2) holds because
  each half-step runs its own frame to a fixpoint (LM(Q) is a full least model); N5's S4a step does not.
- **Verdict.** BLOCKED by (W2). READING: the template says what a SEG-COUNT proof must supply in place of (W2): a charge from each
  step with empty increment to a later step with a surplus increment. That is L-SI's Corollary JOINT plus the missing injectivity
  (LAY §6 (b)); nothing in the logic-programming literature opened here supplies it.

## 4. E4: SEG-RUN reduces to a count of P-change "carries" (O2 → O3)
Composition of fleet results with E6. No new source.
- RESULTS R83 (refereed): SEG(S) − 1 ≤ G(S) + CF(S), and G(S) ≤ Σ_u (XR_S(u) + TIE_S(u) + CYC_S(u) + THRU_S(u)) over Odd u of
  out-degree ≥ 2 (GATE-RISE).
- GRUN §5, "Elementary (PROVED, lane)": XR_S(v) ≤ PCH_S(v) + (PCH_S(v) + 1)(n − 1), PCH_S(v) the P-changes of Ξ(v) in S.
- E6 below (PROVED, L-LIT, unrefereed): PCH_P(v) ≤ (K(K+1)/2)(NM_P(v) + 1) + NM_P(v) on a phase P, K ≤ n − 1.
- **Consequence (PROVED as a composition, conditional on E6 being refereed).** On a run S inside one phase,
  SEG(S) ≤ 1 + CF(S) + Σ_u (TIE + CYC + THRU)_S(u) + Σ_u n·[(n²/2)(NM(u) + 1) + NM(u) + 1].
  So CONJECTURE SEG-RUN (even in the weaker form SEG = poly(n)) follows from three counts: CF (cycle appearances; T28 rank 2's
  Post-Ye cycle-creation lemma is the cross-field analogue there), the TIE/CYC/THRU cases, and **NM(u), the non-matchable
  P-changes of each gate u per phase**. This is weaker than SEG = O(n), and it does not touch (H4′_rel) or GEN_W.
- **Verdict.** A REDUCTION, not a bound. It moves O2 onto O3's open part.

## 5. E5: 1-1 exchanges, rank replacement, and the 1-2-exchange counter (O3)
**Source.** Ackermann, Röglin, Vöcking, "On the impact of combinatorial structure on congestion games", ECCC TR06-067 (2006; J. ACM
55(6) 2008, not opened in the journal form).
- **Exact statements (PROVED, source).**
  - Thm 3 (p.5): "Let Γ be a matroid congestion game. Then players reach a Nash equilibrium after at most n²·m·rk(Γ) best
    responses."
  - Lemma 4 (p.5), the engine: with d̃_r(n_r) := the RANK of the delay d_r(n_r) in the sorted list of all delays, "a best response of
    player i to S w.r.t. delays d_r which strictly decreases the delay of i ... strictly decreases the delay of player i w.r.t. the
    delays d̃_r". Proof: a perfect matching between S*_i \ S_i and S_i \ S*_i (Schrijver) in which every matched exchange is
    individually non-worsening, one strictly.
  - p.5: "Theorem 3 is independent of the delay functions. In particular, we do not assume monotonicity or that all delays have the
    same sign."
  - p.7: "The key insight for proving Theorem 3 is that best responses in matroids can be decomposed into sequences of pairwise
    exchanges of resources such that each of these exchanges does not increase the delay of the corresponding player."
  - Def. 8 (1-2-exchange property), Lemma 9 (every inclusion-free non-matroid has it), Lemma 10 / Thm 7: from a 1-2 exchange
    ("If d(a) < d(b) + d(c) ... a ∈ I and b, c ∉ I") they build "a binary counter" with exponentially long best-response sequences.
- **N5 object.** A P-change P_t → P_{t+1} of one vertex; resources ↔ ranks; delays ↔ signed weights s(r)2^r. Fact DELTA (R84) makes
  the comparison of sets lexicographic: the largest rank of the symmetric difference decides. A carry (one higher even rank in, several
  lower even ranks out, or the odd dual) is a 1-k exchange, the analogue of ARV's 1-2 exchange: one element outweighs the sum of the
  others (2^d > Σ_{r<d} 2^r).
- **Hypotheses.** (a) Matroid structure of the strategy sets: path sets of simple paths into a fixed cycle node are not matroid bases,
  so ARV's Theorem 3 does not apply as stated, and their Theorem 7 says structure alone cannot exclude counters. (b) The rank-replacement
  step needs only (c) below, not (a): E6. (c) Each move decomposes into non-worsening 1-1 exchanges: NOT known for N5; this is the
  measurable hypothesis.
- **Verdict.** PROMISING, as a reduction plus a measurement: the P-changes split into MATCH and carries (E6), and the lane data
  (L-RED R104: RESET 133 of PCH 157) do not yet say which RESETs are carries. A reset that removes one lower even rank while adding one
  higher even rank is a MATCH; only multi-element resets without a matching are carries.

## 6. E6: Lemma MATCH-Φ (PROVED, L-LIT, unrefereed; elementary)
**Setting.** RESULTS R84's: a vertex v, a phase P, c := λ(v) constant on P, P_t := P(Ξ_t v), a set of ranks above rank(c). Let
r_1 < … < r_K be those ranks (K ≤ n − 1), pos(r_k) := k, and w(r) := +pos(r) if r is even (Ω of its vertex even), −pos(r) if r is odd.
Φ(A) := Σ_{r ∈ A} w(r).
- **Definition.** A P-change A := P_t → B := P_{t+1} is MATCHED if there is a matching M between some outgoing ranks (A ∖ B) and some
  incoming ranks (B ∖ A) such that every pair (o, i) ∈ M has w(i) > w(o), every unmatched incoming rank is even and every unmatched
  outgoing rank is odd. Otherwise it is a CARRY. NM_P(v) := the carries of v in P.
- **Fact 1.** For distinct ranks o, i: w(i) > w(o) iff the one-element exchange {o} → {i} raises the signed weight (Fact DELTA on the
  pair: if i > o the exchange is better iff i is even, and then w(i) = pos(i) > |w(o)|; if o > i it is better iff o is odd, and then
  w(o) = −pos(o) < w(i)); adding an even rank or removing an odd rank raises both. So MATCHED = "decomposes into individually improving
  1-1 exchanges, additions of even ranks and removals of odd ranks" (ARV's Lemma 4 condition).
- **Lemma.** At a MATCHED P-change, Φ(B) − Φ(A) ≥ 1. Proof: Φ(B) − Φ(A) = Σ_{(o,i) ∈ M} (w(i) − w(o)) + Σ_{unmatched i} pos(i) +
  Σ_{unmatched o} pos(o); every term is a positive integer (w(i) ≠ w(o) as i ≠ o, and |w| ≥ 1), and the sum is non-empty as A ≠ B. □
- **Corollary.** Φ takes values in [−Σ_{odd} pos, Σ_{even} pos], an interval of width ≤ K(K+1)/2, and a carry changes Φ by at most
  that width, so on P: PCH_P(v) ≤ (K(K+1)/2)·(NM_P(v) + 1) + NM_P(v) ≤ (n²/2)(NM_P(v) + 1) + NM_P(v).
- **What it uses.** Only the definition of MATCHED and that ranks are distinct; not (MON). (MON) and Fact DELTA enter only in the
  READING that a MATCHED change is an improvement decomposed into improvements (Fact 1), and in R84's guarantee that every P-change
  of a phase is a strict improvement.
- **Self-check.** docs/lit/T32-match-check.py: all ordered pairs of subsets of K = 6 ranks with weight(B) > weight(A), 40 random parity
  patterns: 80,640 improving pairs, 0 MATCHED pairs with Φ rise < 1, 32,534 carries; the carry {0, 1} → {2} (all even) has Φ 3 → 3.
- **Honest limits.** (i) This is a REDUCTION: NM_P(v) may be exponential; a binary counter on P under a fixed top is made of carries.
  (ii) It bounds P-changes, not ℓ-changes (Ξ = (c, P, ℓ)); GRUN §5 handles ℓ per P-block. (iii) Not refereed; the fleet's REFEREE
  should check Fact 1 against SPEC S1's rank and sign convention before anyone cites it. (iv) R84's TOP-SHAPE is a special case in
  spirit (a top change is a 1-1 or 0-1 move at the top) but is not implied by this lemma.
- **NEEDS (measurement, for L-COMP or L-SI).** For every (vertex, phase) in the library and the kill pins: PCH, NM (a bipartite
  matching test per P-change), max NM/n, and on l121reader_n41 (71 P-changes of one vertex) and pl130_n40 (R104) the split of the
  RESETs into MATCHED and carries. If NM per (vertex, phase) stays ≤ c·n with small c, E4 gives a polynomial CONJECTURE for SEG-RUN
  that is far easier to attack than SEG = O(n).

## 7. E7: shadow paths on 0/1 polytopes (O3)
**Source.** Black, De Loera, Kafer, Sanità, "On the Simplex method for 0/1 polytopes", arXiv 2111.14050 v1 (28 Nov 2021; Math. Oper.
Res. 50(2) 2025, not opened in that form).
- **Exact statements (PROVED, source).**
  - Cor. 1 (p.15): "for any objective function c, the c-coherent v-monotone path from a c-maximum of F to a c-maximum of Q is of
    length at most |{v^T u : u ∈ V}| − 1."
  - Def. 4 + Thm 5 (p.15-16): with v = 1 − 2x⁰ (Hamming distance from the start), "the Slim Shadow rule reaches an optimal solution by
    performing at most n steps."
  - Lemma 5 (p.17), nested faces: with f(u) := the largest coordinate where u differs from x⁰ and F_k := {x ∈ P : f(x) ≤ k}, the path
    that moves to the c-best among the f-minimal improving neighbours visits c-maxima of a strictly increasing chain of faces, so "The
    length of the path Γ constructed in this way is at most d."
  - Context, p.4: Klee-Minty and all popular pivot rules have exponential examples; p.1: no polynomial pivot rule was known for 0/1-LPs.
- **N5 object.** P_t ∈ {0, 1}^K (the incidence vector of a path set) and the objective c_r = s(r)2^r: the P-sequence of a vertex in a
  phase is a strictly c-monotone sequence of 0/1 points (R84). Its steps are not polytope edges in general.
- **Two hypotheses this suggests (CONJECTURES, untested).**
  - HAM-MONO: in a phase, |P_t Δ P_{a}| strictly increases at every P-change (P_a the phase's first path set). By Cor. 1's counting
    (only the values of v^T x matter, not the edges) this alone gives PCH ≤ K. It is the 0/1 form of "no rank enters and leaves
    again", so R104's abundant RESETs probably kill it as stated; a weaker version with a different auxiliary vector v of few values
    (e.g. counting ranks of one parity) is the real question.
  - NEST-FACE: at every P-change t → t + 1 with k := the largest rank in P_{t+1} Δ P_a, P_{t+1} is Ξ-best among the path sets
    REALIZABLE at t + 1 that agree with P_a above k, and k does not decrease. Lemma 5's argument (faces strictly growing) then
    gives PCH ≤ K. A binary counter violates it: a carry lands on a set that is not the best of its face.
- **Hypotheses of the source that N5 lacks.** (a) A fixed polytope: N5's realizable path sets change with the state (σ̄, τ fixed per
  phase, but σ moves). (b) Moves along edges chosen by the rule: N5's P-steps are induced by S4a, not chosen. So the source gives the
  counting device, not the dynamics.
- **Verdict.** PROMISING only as a source of testable invariants (HAM-MONO weak forms, NEST-FACE). Both are falsifiable on the
  existing pins (l121reader_n41, long121_n40, pl130_n40) without new runs of N5, from logged P-sequences.

## 8. Not opened (and why)
- Busch, Tirthapura, "Analysis of link reversal routing algorithms", SIAM J. Comput. 35(2) 2005 (DOI 10.1137/S0097539704443598):
  author copy www.ece.iastate.edu/snt/files/2015/10/sicomp05.pdf fails TLS verification through the proxy; web.archive.org reset
  twice; SIAM paywall. Its per-node reversal bounds are NOT cited above; E1 rests on arXiv 1111.4600 only.
- Charron-Bost, Függer, Welch, Widder, "Full reversal routing as a linear dynamical system" (SIROCCO 2011) / TALG 2015: no open copy
  found; cited only through arXiv 1111.4600 §8.3.
- Van Gelder, "The alternating fixpoint of logic programs with negation", JCSS 47 (1993) and PODS 1989: epub.ub.uni-muenchen.de/8502
  is the PODS'89 proceedings file; its table of contents lists the paper on p.1 but the extracted text is not that paper. E3 cites
  Lonc-Truszczyński only.
- Gawlitza, Seidl, "Precise fixpoint computation through strategy iteration" (ESOP 2007) and "Precise interval analysis vs. parity
  games" (FM 2008): Springer, no open copy found. Planned for O2 (min-strategy changes inside max-strategy iteration); dropped.
- Schurr-Szabó IPCO 2005 (jumps on USOs; notebook: "extraction garbled"): not re-opened; see BARRIERS B14 and T28 rank 4.
- Tardos, "Polynomial bound for a chip firing game on graphs", SIAM J. Discrete Math. 1(3) 1988: not attempted (SIAM paywall);
  Bond-Levine (E2) covers the least-action side.

## DONE / FINDINGS / NEEDS
- DONE: this note; docs/lit/T32-match-check.py (self-check of E6); notebook rows for 7 opened sources.
- FINDINGS:
  1. (E5/E6) O3's obstruction has a precise cross-field name: ARV's 1-2-exchange (one resource outweighs two) is what builds binary
     counters in congestion games, and the matched 1-1 case is polynomial. Lemma MATCH-Φ (PROVED, L-LIT, unrefereed): matched
     P-changes raise Φ = Σ ±pos(r) by ≥ 1, so PCH ≤ (n²/2)(NM + 1) + NM per vertex per phase, NM = carries.
  2. (E4) With R83, GATE-RISE and GRUN's XR bound, SEG-RUN in polynomial form reduces to bounding CF, TIE/CYC/THRU and the gates'
     carries NM. A REDUCTION; NM is OPEN.
  3. (E2, E3) The O1 deadlock is exactly a failure of local abelianness (least action) and of (W2) (alternating fixpoint); both
     literatures prove their bounds from the property N5 lacks, so neither gives SEG-COUNT.
  4. (E1) Full Reversal's quadratic bound comes from a fixed min-plus law with 1-Lipschitz work vectors; N5 has no fixed law;
     CONJECTURE LIP is a cheap test.
  5. (E7) Two testable invariants for O3 from 0/1-polytope shadow paths: HAM-MONO (weak forms) and NEST-FACE.
- NEEDS: none from the owner. For the Lead to route: (a) the NM measurement of §6 (L-COMP or L-SI, from logged P-sequences);
  (b) LIP, HAM-MONO, NEST-FACE checks on the existing pins; (c) a referee read of Lemma MATCH-Φ if (a) shows NM small.
