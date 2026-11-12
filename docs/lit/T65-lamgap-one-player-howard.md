# T65: Lemma LAM-GAP / SHARP (one-player Howard under the VJ valuation, fixed-Λ window ≤ |Ch|) against the landed fleet results and the one-player Howard literature
L-LIT successor (D18, D1; Lead brief and «go» 2026-11-12 11:04Z). Written 2026-11-12 (date -u in the commit). Working note, unrefereed.
Not a TARGET.md claim; not M3 or M4; G-N5-TIME stays OPEN; N5′-xi stays a CANDIDATE (D1).
Labels for claims: KNOWN (source) / IMPLIED (source + argument) / NEW (searched where) / CONTRADICTS (source). Labels for my own
statements: READING (L-LIT, not to sign) / PROVED-in-source (a theorem of an opened source).

Objects compared (read-only, other lanes):
- LAM-GAP: claude/l-si 23d39400 / 4fda7245, docs/si/box101-lamgap.md §2. «Let a..b be a maximal run of states of a Howard run with
  Λ_t(v) = Λ_a(v) for every vertex v and a ≤ t ≤ b. Then b − a ≤ |Ch| + 1.» (one-player game, VJ valuation, Howard: every v ∈ Ch with
  a strictly better successor moves to a ⊴-best one, any tie resolution).
- SHARP: claude/l-red 0148d73f, docs/red/R234-lamgap.md §3. «In LAM-GAP's setting, b − a ≤ |Ch|.», tight (R234 §6).
- Trunk 071392490: docs/RESULTS.md R17 (l. 730-), R118 (l. 13607-), R125 (l. 15595-); docs/new/P-N5-XICYC.md §4-§5.

## 0. Answers
1. Fleet-internal (F1). LAM-GAP's proof idea is already LANDED twice: RESULTS R118 (c)/(d) (Lemma PATH, Theorem BR-SEG: Howard, movers
   only, two-player form) and R17 (b)/(c) (Lemma P, Theorem PH: arena-optimum rule, one player). LAM-GAP / SHARP are not literally
   implied by either. They add exactly two things: (i) no hypothesis H0 (a choice vertex may be its own cycle node and switch), for
   Howard's greedy rule; (ii) the constant |Ch| (tight) in place of N, n_E or n − 1. §2 has the line-by-line table.
2. What the chain needs (F1, the Lead's question). On Γ3 no mover is ever a cycle node (R125 (e) CN2-3), so (i) is never used there.
   The window-length bound the chain needs is covered by LANDED statements in two ways (§3): globally (R118 (l) with R125 (c):
   T3 ≤ C + R + (C + R + 1)·N), or per SCC through the sub-genome on Reach(C) (R118 (d) + (l), constant N instead of N_C + 1). So the
   chain link can cite RESULTS R118 / R125 plus one short restriction argument; LAM-GAP / SHARP as a new lane lemma is not required
   for the polynomial chain. It is still the cleaner statement for one-player games in general.
3. External novelty. The window bound is KNOWN for additive weights (Cochet-Terrasson–Gaubert 2000, Theorem 2.3: all-switches policy
   iteration for longest paths stops within n − 1 steps, tight) and for mean payoff (Zhong–Ye 2026, proof of Theorem 7.2: «every N
   consecutive updates create a new cycle»; Madani 2002, Fig. 5). For parity games it is STATED without proof: Friedmann's thesis
   (sink parity games, «linear number of iterations») and VJ00 Prop. 7.4 (O(n³) for one-player parity games, which is exactly
   n² Λ-changes × an O(n) window). For one-player 1-sink games LAM-GAP is IMPLIED by the Cochet-Terrasson–Gaubert theorem through a
   weight map (§5). I found no published proof for general one-player VJ games; the fleet's R17 / R118 are such proofs.
4. No CONTRADICTION with any lower bound (§6). Hansen–Zwick (Ω(n²)), Asadi–Chatterjee–de Raaij (Ω(n²), polynomial weights) and
   Zhong–Ye (exp(Ω(N)), a preprint) all count NEW CYCLES (gain changes). Inside one gain they obey the same window bound. Under VJ the
   «gain» is the cycle's top vertex Λ: at most n values per vertex, monotone, so at most n(n − 1) windows.
5. F2. L-SI box 101 §0-§1 says Hansen's conjecture is OPEN. Zhong–Ye, arXiv 2609.40147 v2 (13 Oct 2026, unrefereed preprint), Theorem
   6.1 claims to refute it. Recorded in §4 with quotes. It does not touch LAM-GAP or L1-POLY (§6).

## 1. The statements, verbatim
- LAM-GAP, SHARP: above.
- R118 (c) (trunk RESULTS l. 13686-13688): «DOM «For every mover x, step t and successor y of x: Ω_(t+1)(x) ⊵ ext(x, Ω_t(y)).»; STRICT
  «If σ_(t+1)(x) ≠ σ_t(x), then Ω_(t+1)(x) ▷ Ω_t(x).»; PATH: Ω_t(z_0) ⊵ val(π) along a simple path π of the fixed-σ̄ graph to a fixed
  cycle node, once t − a ≥ μ(π) (Bellman-Ford induction).» μ(π) = the number of movers on π (P-N5-XICYC §4 l. 93-95).
- R118 (d) (l. 13689-13690) [IDEAL-CYC(G), every genome]: «If Λ and σ̄ are constant on the states a, a+1, …, a+j+1 and the step a+j →
  a+j+1 changes σ, then j ≤ N − 1. Hence every maximal run of consecutive p-steps has at most N steps.»
- R118 (i) (l. 13697-13701) [any parity game, Howard from any σ_0, under H0]: «H0: every step t → t+1 switches some Even x with
  Λ_t(x) ≠ x and Λ_(t+1)(x) ≠ x.»; «(a) every maximal run of p-steps has at most n_E steps;».
- R118 (g) ONEP-POLY (l. 13694-13695): «with every gate restricted to its β-face, R = 0 … T ≤ n(2M + 2) + (n(2M + 2) + 1)·N.»
- R118 (l) (l. 13715-13718): «§4 applies on Γ3 (movers priority 0, pads never cycle nodes by PAD (b), non-mover Even vertices frozen in
  standard states, Odd = gates and K2), so «T3 ≤ C + R + (C + R + 1)·N, with C ≤ n3·(2M + 2) and n3 = N + 7M + 10;»».
- R125 (c) REACH3-ALL: «… its mover parts form a run of HOW3(G) … until its first fallback, at iteration T3 + 1.» (REFEREE-2: «removes
  R118 (k)'s condition»). R125 (d): «Facts F1, F3, F4′, F5, F6, DOM, STRICT on HOW3(G) … [every genome]». R125 (e) CN2-3: «For every
  positional pair of Γ3(G) and every vertex v ≠ c_X, the cycle node of v's play has Ω ≥ 3; no mover, gate or pad is ever a cycle node
  or in a set Π.»
- R17 (b) (l. 741-742): «Lemma P (phase progress): in a λ-phase, after k steps every vertex x satisfies Ω_k(x) ⪰ value(r) for every
  simple path r of at most k edges from x to a cycle node of ρ_0 (all four cases, including the cycle-closing cases B1/B2).»
  R17 (c): «Theorem PH: in a λ-phase, after n − 1 steps every further in-phase step is value-flat, and there are fewer than m such
  steps». R17's rule: «switch-best: ρ_{k+1} = an optimal strategy of the arena H_k in which every vertex x may use {ρ_k(x)} ∪ I_k(x)».
  R17 (f): «VJ00 Prop. 7.4's O(n³) holds for the arena-optimum rule; for arbitrary single switches the statement is false (CDAG_n)».

## 2. Where they coincide and where LAM-GAP / SHARP go beyond (READING)
| item | LAM-GAP / SHARP | R118 (c)/(d) BR-SEG | R118 (i) BR-SEG-G | R17 (b)/(c) |
| --- | --- | --- | --- | --- |
| game | any one-player game (Odd and frozen Even vertices have one successor) | Γ(G), non-movers frozen, Odd free at gates; by (l) also Γ3 | any parity game, every Even vertex switches | any one-player game, injective priorities |
| rule | Howard: each v ∈ Ch to a ⊴-best successor, any tie rule | the same, at movers | the same, at Even vertices | arena optimum of {ρ(x)} ∪ I(x) (not Howard's greedy step) |
| window | Λ constant at every vertex | Λ and σ̄ constant at every vertex | the same | no vertex changes its cycle node |
| key lemma | (L): val_(a+k)(v) ⊵ value(P) for every simple path P to a top with ≤ k choice vertices | PATH: the same, with μ(π) = movers on π | PATH-G (fixes l. 48-58) | Lemma P: the same, with k = edges |
| cycle-node switches | allowed (top ℓ ∈ Ch may switch); cost: the «+ 1», removed by SHARP | cannot occur (F6: no mover is a cycle node) | excluded by hypothesis H0 | allowed (cases B1/B2) |
| bound | b − a ≤ \|Ch\| (SHARP, tight) | ≤ N steps | ≤ n_E steps | n − 1 value-changing steps, then < m flat steps |
| status | lane; L-RED R234 SURVIVES; exhaustive n ≤ 4 | landed, two referees | landed, two referees | landed, two referees |

- Same proof: an induction over all simple paths into the fixed cycle nodes, driven by monotonicity (F1 = R15 (a)) and by «Howard's new
  successor is at least as good as every successor under the old values» (DOM). It is a Bellman–Ford domination argument (§4).
- LAM-GAP is not implied verbatim by R118 (i): a step at which only cycle nodes switch violates H0, and such steps occur (R118's DATA:
  H0 fails at 388 of 2,072 steps of its 2,000 random two-player runs). It is not implied by R17: Howard's greedy step need not be an
  arena optimum, and conversely.
- What is NEW inside the fleet: Howard without H0 on one-player games, and the tight constant. Nothing else.

## 3. What box 100's WINDOW needs, and what is landed (READING; three options for the Lead)
WINDOW (box 100 §4, with box 101 §3 and R234's GAP W1) uses one fact: after t0(C), a stretch of HOW3 states with σ̄ constant on C's
gates and Λ constant on Reach(C) contains at most Gap(C) + 1 states at which a mover of C switches.
- H0 on Γ3: automatic. R125 (e) CN2-3 says no mover is ever a cycle node; in HOW3 only movers switch. So the frozen-form theorem
  R118 (d) is the one that applies. BR-SEG-G does NOT apply to HOW3 (it lets β's and K-vertices switch).
- Option A (landed only, global windows). Take the windows of the whole HOW3 run: maximal runs of p-steps. R118 (l) with R125 (c):
  T3 ≤ C + R + (C + R + 1)·N, C ≤ n3(2M + 2). R counts steps at which some gate flips (σ̄(K2) is constant, R125 LOC-K2-3). With box
  100's TWO-CROSS and DEPTH-COUNT3 (lane; D1 fix of R234 §4): R ≤ Σ over ALL gates of flips ≤ polynomial + Deep_c^all, where Deep_c^all
  := the flips of any gate over the whole run that TWO-CROSS charges to a change of depth > c. So
  polynomial T3 ⇐ R118 (l) + R125 (landed) + TWO-CROSS + DEPTH-COUNT3 (lane) + «Deep_c^all polynomial».
  - This needs no SCC-RED, ONE-CROSS3, WINDOW or LAM-GAP. The price: the conjecture is DEEP3 for every gate and the whole run, not only
    internal gates after t0. Box 100 §5.2's counter already measures that quantity («The counter covers EVERY gate over the WHOLE run»).
- Option B′ (landed + a restriction argument, per SCC). Reach(C) is closed under successors (R234 W1). Let G′ := the genome G restricted
  to the movers of Reach(C), with the state at time a as its start. Γ3(G′) is the subgame of Γ3(G) on Reach(C) up to an
  order-preserving renaming of priorities (β's by rank, e's by (level, gate index), core on top), and VJ values depend only on that
  order; pads never matter (R117 PAD). The HOW3 run of Γ3(G), restricted to Reach(C), is a HOW3 run of Γ3(G′). R118 (d) + (l) on G′:
  every stretch with Λ and σ̄ constant has at most N(G′) ≤ N switching steps. So Gap(C) ≤ N. This replaces LAM-GAP in the chain by
  landed statements plus this paragraph (unrefereed; the renaming step is the part to check).
- Option B (new lane lemma). LAM-GAP / SHARP with W1: Gap(C) ≤ N_C. Sharper constant, self-contained, but a new lemma to referee.
- The three options give the same polynomial conclusion. Only the constants and the form of the DEEP conjecture differ.

## 4. External sources (opened 2026-11-12 unless stated; sha256 prefixes in notes/L-LIT.md)
| source | location | quote / content | label for LAM-GAP |
| --- | --- | --- | --- |
| Cochet-Terrasson, Gaubert, «Policy iteration algorithm for shortest path problems» (report; PostScript from Gaubert's page; cited as «Technical report, 2000» by Fearnley [3]) | Algorithm and Theorem 2.3 p.5; Lemma 4.2 p.9; proof p.10; Example 5.1 p.11 | greedy all-switches rule («for i ∈ I_k, π_(k+1)(i) = any element of L_k(i)», L_k = arg max). «Theorem 2.3. The policy iteration algorithm stops at a step k ≤ n − 1. If all the circuits have non-positive weight, then, x^k = x* … Otherwise, G(π_(k+1)) contains a circuit of positive weight.» Lemma 4.2: y^k ≤ z^k ≤ y^(n−1) and z^k < z^(k+1) (the policy-iteration values dominate Bellman's k-th iterate). p.11: «To show that Theorem 2.3 is accurate, we next give an example where the max-plus policy iteration algorithm stops at step n − 1.» | KNOWN (additive weights, one root): statement, proof and tightness |
| Zhong, Ye, arXiv 2609.40147 v2 (preprint, 13 Oct 2026) | Theorem 7.2 p.33; proof p.33-34 | «Suppose N consecutive updates create no new cycle … Thus every N consecutive updates create a new cycle.» (deterministic average-reward MDPs, Howard) | KNOWN (mean payoff; window = no new cycle) |
| Madani, «Polynomial value iteration algorithms for deterministic MDPs», UAI 2002, arXiv 1301.0583 | §5 printed p.316-317 (PDF p.6-7), Fig. 5 | policy iteration viewed in phases: «Apply value iteration until a new cycle is discovered or until n iterations.»; «they all guarantee that the next cycle discovered will have higher mean than the last» | KNOWN (phase structure) |
| Friedmann, PhD thesis (LMU 2011) | Theorem 4.9, printed p.84 (PDF p.96); §4.3 printed p.101 (PDF p.113) | «Theorem 4.9 ([Vög00]). Let G be an one-player parity game. Policy iteration with the SWITCH-ALL rule requires polynomially many iterations in the worst case.»; «In fact, they can be solved in a linear number of iterations in the setting of sink parity games. All the algorithm performs here is acyclic path optimization.» | KNOWN as a statement (no proof given) |
| Vöge, Jurdziński, BRICS RS-00-48 | §7, printed p.27 (PDF p.29) | «Proposition 7.4 The discrete strategy improvement algorithm terminates after O(n³) strategy improvement steps for one-player parity games.» No proof (T22). | KNOWN as a statement: L1-POLY's O(n²·\|Ch\|) is this bound |
| Fearnley, arXiv 1705.02313 | §4, PDF p.9, Lemma 3 | «they proved that the all-switches variant of the algorithm always terminates after at most O(\|V\|\|E\|) steps» (of [3] = Cochet-Terrasson–Gaubert); Lemma 3: one-player strategy improvement finds a best response «after at most O(\|V\|\|E\|) iterations» | KNOWN (sink games, best responses). The cited theorem gives n − 1 iterations and O(n\|A\|) time |
| Hansen, Miltersen, Zwick, arXiv 1008.0530 | §5, PDF p.10, Lemma 5.3 | «T v^(π0) ≥ v^(π1)» (one policy-iteration step dominates one value-iteration step); «well-known and appear, e.g., in Meister and Holzbaur [27] … (They may be folklore.)» | KNOWN (the DOM step, discounted) |
| Post, Ye, arXiv 1208.5083 v2 | p.2; Theorem 3.7 p.9 | simplex with the highest-gain rule on deterministic MDPs: O(n³m²log²n) iterations. «Our results do not extend to policy iteration, and we leave this as a challenging open question.» | no implication: another algorithm (one switch per step), discounted |
| Hansen, Zwick, ISAAC 2010: AUTHORS' SLIDES only | slide pages 13, 14, 19 | «there exists a weighted directed graph with n vertices on which Howard's algorithm performs Ω(n²) iterations»; «Conjecture: The number of iterations performed by Howard's algorithm, when applied to a weighted directed graph, is at most the number of edges in the graph.»; «Madani (2008, personal communication): 2n − O(1) lower bound for deterministic MDPs» | context (§6) |
| Asadi, Chatterjee, de Raaij, arXiv 2506.12254 v1 | §1 p.2; Conjecture 3.1; Theorem 3.2 p.4 | Conjecture 3.1 = «[Hansen, 2012, Conjecture 6.1.1]»; «a better parametric bound of O(n³W) on the number of iterations can be obtained»; Theorem 3.2: (n² + 7n − 6)/2 iterations on 2n vertices with weights O(n²) | context (§6) |
| Zhong, Ye, arXiv 2609.40147 v2 | Theorem 6.1 p.23; p.24; eq. (6.8) p.26 | Theorem 6.1: «a family of deterministic average-reward MDPs with N states and at most four actions per state, on which Howard's policy iteration performs at least exp(Ω(N)) iterations from a specified initial policy»; p.24: «It also refutes the conjecture that Howard's policy iteration terminates within M iterations … (Hansen, 2012, Conjecture 6.1.1; Asadi et al., 2025, Conjecture 3.1).» | context (§6). A CLAIM of an unrefereed preprint; proof not checked here |
| Cochet-Terrasson, Cohen, Gaubert, Mc Gettrick, Quadrat, IFAC SSC 1998 | p.2; Theorem 4.5 p.7 | «We conjecture that the worst case value of the number of iterations N_H is polynomial in E. Examples show that it is at least of order n.»; Theorem 4.5: the number of iterations is «less than the number of policies» | context: the older form of Hansen's conjecture |
| Friedmann, arXiv 1106.0778 v2 (LMCS 2011) | §5, PDF p.8 | «there are only linearly many different values for the first and third component while there are exponentially many for the second» | used in §6 |

NOT OPENED (reported, never paraphrased):
- Hansen, Zwick, ISAAC 2010, the paper (DOI 10.1007/978-3-642-17517-6_37): closed access (Semantic Scholar «CLOSED», OpenAlex «is_oa
  false»; Springer returns an HTML page). Only the slides.
- Hansen, PhD thesis, Aarhus 2012 (Conjecture 6.1.1): cs.au.dk/~tdh/papers/dissertation.pdf is 404. A Wayback snapshot exists
  (archive.org availability API: 20160826003911), but web.archive.org is unreachable from this container (connection reset; the fetch
  tool refuses the host). Conjecture 6.1.1 is quoted only through Asadi et al. and Zhong–Ye.
- Vöge, PhD thesis, RWTH Aachen 2000 ([Vög00]): old.automata.rwth-aachen.de returns 403 (as on 2026-10-19, T22).
- Madani, AAAI 2002 («On policy iteration as a Newton's method …»): aaai.org returns 403. Madani–Thorup–Zwick, TALG 2010. Dasdan 2004.
  Meister–Holzbaur 1986. Melekopoglou–Condon 1994.

## 5. Verdict on LAM-GAP / SHARP
- KNOWN for additive weights with one root: Cochet-Terrasson–Gaubert Theorem 2.3 with Lemma 4.2 (statement, Bellman-domination proof,
  tightness by Example 5.1). KNOWN for mean payoff: Zhong–Ye, proof of Theorem 7.2; Madani Fig. 5.
- KNOWN as an unproved statement for parity games: Friedmann's thesis p.101 (sink parity games, linear) and VJ00 Prop. 7.4 (O(n³)).
  Friedmann attributes a proof for SWITCH-ALL to Vöge's thesis, NOT OPENED.
- IMPLIED for one-player 1-SINK games (every Λ = one sink ℓ without a choice), by Cochet-Terrasson–Gaubert Theorem 2.3 and this weight
  map (READING; the fixed-cycle-node isomorphism of this lane's T56): give a vertex u the weight s(u)·(n + 1)·2^rank(u) + δ if u is more
  relevant than ℓ and δ otherwise, with s(u) = +1 for even priority, −1 for odd, δ = −1 if ℓ is even and +1 if ℓ is odd. Path sums then
  order paths to ℓ exactly as VJ orders (ℓ, Π, len): the signed powers of two compare by the most relevant vertex of the symmetric
  difference, and |Σδ| ≤ n cannot override them. A cycle of positive weight is a cycle whose closing would change Λ. Howard's step is
  the report's policy improvement step. Bound: n − 1 steps for n non-sink vertices.
- General one-player VJ games (several tops, tops with choices): the weight of a vertex depends on the top it is compared against, so
  the reduction above is not a single shortest-path instance. Proofs for this case: RESULTS R17 (arena optimum), R118 (c)/(d)/(i)
  (Howard, under F6 or H0), LAM-GAP (Howard, no H0). In the opened literature: the statement VJ00 Prop. 7.4 only.
- NEW (as far as searched): the exact tight constant b − a ≤ |Ch| for VJ valuations with tops allowed to switch (SHARP). Searched:
  the sources of §4 in full text; arXiv listing and web searches for «one-player parity games strategy improvement polynomial»,
  «Howard minimum mean cycle iterations new cycle», «policy iteration shortest path Bellman»; this lane's T22, T35, T48, T54, T64. Not a
  strong novelty claim: the result is an elementary variant of a 2000 theorem.
- CONTRADICTS: nothing (§6).

## 6. Why the VJ setting escapes the mean-payoff lower bounds (READING, with the sources' own words)
- Every Howard run splits into windows of constant gain. Window LENGTH is small everywhere: ≤ N for mean payoff (Zhong–Ye p.34), ≤ n − 1
  for longest paths (Cochet-Terrasson–Gaubert), ≤ |Ch| under VJ (SHARP). The lower bounds count the NUMBER of windows:
  - Hansen–Zwick: Θ(n²) cycles, weights up to n^(n²) (as described by Asadi et al. p.2: «Howard's policy iteration goes through Θ(n²)
    'good' cycles»).
  - Asadi et al. Theorem 3.2: n cycles found in order, about i iterations for the i-th: windows of length ≤ n, as the bound allows.
  - Zhong–Ye Theorem 6.1: exponentially many cycles, «the encoded cycles have strictly increasing mean rewards, with consecutive
    differences 2^(−d−1)/(6d)» (p.26).
- Under VJ the gain of a play is the most relevant vertex Λ of its cycle, not a cycle mean. Λ(v) takes at most n values and only rises
  in reward (R118 F1, F2; Friedmann LMCS p.8: «only linearly many different values for the first and third component»). So a
  one-player VJ run has at most n(n − 1) + 1 windows, and L1-POLY's O(n²·|Ch|) follows. Two cycles with the same top vertex are the same
  gain for VJ and different gains for mean payoff: that is the whole difference.
- So none of the three constructions is an instance of Howard-VJ on a one-player parity game, and none contradicts LAM-GAP, SHARP,
  L1-POLY, R17 or R118 (g). Conversely LAM-GAP says nothing about Hansen's conjecture or about Howard on mean-payoff deterministic MDPs
  (as box 101 §1 already says).
- Caveat. Howard with mean-payoff valuations on the mean-payoff image of a parity game (weights ±n^priority) is a different algorithm
  from Howard-VJ; nothing here bounds it. Friedmann's thesis p.101 states the equivalence of the two only for sink parity games.
- Where exponential behaviour under VJ does live: in the SECOND component, with two players. Friedmann's G_n keeps one cycle node and
  counts through Odd's best-reply flips (R118 DATA: C = 0, R = 4 … 241 for n = 2 … 7). That is T66's subject.

## DONE / FINDINGS / NEEDS
- DONE: this note; sources re-opened or opened today as listed in §4; notes/L-LIT.md rows.
- FINDINGS:
  1. LAM-GAP = the Howard, no-H0, |Ch| form of landed R118 (c)/(d) and R17 (b)/(c). On Γ3 H0 is automatic (R125 (e)).
  2. The chain link can cite landed results: Option A (R118 (l) + R125, global, with DEEP3 for all gates) or Option B′ (R118 (d) + (l) on
     the sub-genome of Reach(C), Gap(C) ≤ N). LAM-GAP / SHARP stay as an optional sharper lane lemma.
  3. KNOWN outside the fleet in additive and mean-payoff form (Cochet-Terrasson–Gaubert Theorem 2.3; Zhong–Ye Theorem 7.2's proof;
     Madani Fig. 5); STATED without proof for parity games (Friedmann thesis p.101, Theorem 4.9; VJ00 Prop. 7.4). No contradiction.
  4. Hansen's conjecture: claimed refuted by Zhong–Ye Theorem 6.1 (unrefereed preprint). Box 101 §0-§1's «OPEN» should read «open until
     2026-10; a preprint claims a refutation».
- NEEDS: Lead: choose Option A / B′ / B for the chain table. Owner (optional, only if the fleet wants the primary proofs): Vöge's
  thesis (RWTH Aachen 2000), Hansen's thesis (Aarhus 2012), Hansen–Zwick ISAAC 2010.
