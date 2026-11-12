# T69: Dijkstra-type potentials against policy iteration. Is box 208's argument (Lemma LEVEL, Statement ABS, Lemma PLATEAU, the fixed-k bounds) known? The two-player Dijkstra ALGORITHM is known; a polynomial bound on Howard's STEPS by a lowest-lagging-value potential was not found
L-LIT successor (D18, D1; Lead brief, «go» 2026-11-12 13:10Z). Written 2026-11-12 (date -u in the commit). Working note, unrefereed.
Not a TARGET.md claim; not M3 or M4; G-N5-TIME stays OPEN; every statement of box 208 stays a CANDIDATE (D1); N5′-xi stays a CANDIDATE.
Labels for claims: KNOWN (source) / IMPLIED (source + argument) / NEW (searched where) / CONTRADICTS (source). Labels for my own
statements: READING (L-LIT, not to sign) / PROVED-in-source (a theorem of an opened source). «NEW» means «not found in the opened
sources and searches listed in §6»; it is a search result, not a theorem, and never a priority claim.

Object compared (read-only, another lane): claude/l-new 8db300fe3fd8e868e61851a9bff76673146d2f10, docs/new/N5-LEVEL-box208.md
(sha1 55e6538110d379fc695f1f06efbd1d7b3df97494, 502 lines): §3 Lemma LEVEL, §5 Theorem WIN, §6 R-HEIGHT / K1-TCYC / FVS-TCYC, §10
Statement ABS, Addendum A Lemma PLATEAU and Theorem ALL-TCYC. One-page summary: docs/lit/T69-summary.md.

## 0. Answers
1. The ALGORITHM is KNOWN. Dijkstra's algorithm extends to two-player shortest-path games with non-negative weights: Khachiyan et al.
   (DIMACS TR 2007-02, Theorem 1); Fijalkow (ed.), Games on Graphs, Theorem 5.14; Bertsekas, arXiv 1608.01670, §5.3 (Prop. 5.1-5.3);
   Hansen–Ibsen-Jensen–Miltersen, arXiv 1201.3498, Fig. 3 (ExtendedDijkstra). Its greedy invariant («the lowest unsettled label is
   final») is the invariant LEVEL uses.
2. STRATEGY ITERATION on exactly this class is KNOWN as an algorithm, with FINITE termination only: Hansen–Ibsen-Jensen–Miltersen §2
   (Theorem 2.5: «there are only finitely many strategies»); Bertsekas §5.2 («a finite number of iterations», and p.30: «unclear how
   the Dijkstra-like algorithm compares with … PI»); Guillot–Stauffer («a finite number of steps»). Björklund–Vorobyov (the maximiser
   improves, the minimiser takes shortest paths; signed weights) give a pseudopolynomial bound.
3. A POLYNOMIAL bound on Howard's steps on such games, proved by a Dijkstra-type lowest-lagging-value potential (box 208 §10,
   Statement ABS: ≤ (edges of Max vertices)·(vertices) steps): NOT FOUND. Label NEW (searched: §6), weakly: the proof is elementary and
   every ingredient is classical. For ONE player it is KNOWN in Bellman–Ford form (Cochet-Terrasson–Gaubert Theorem 2.3: ≤ n − 1 steps).
4. Lemma PLATEAU's abstract content (a stretch on which the lowest class is frozen is a one-player Howard run with fixed cycle nodes)
   uses the one-player window bound: KNOWN for additive weights and mean payoff, landed in the fleet for VJ (T65; RESULTS R118 (i)).
5. Fixed k. Published fixed-parameter results for parity games are about SOLVING, by other algorithms: Gajarský et al. Theorem 3
   (directed feedback vertex set) and Theorem 4 (k vertices of one player), Mnich–Röglin–Rösner Theorem 1, Berwanger et al. Theorem 4.5
   (DAG-width), Fearnley–Schewe (treewidth, DAG-width). None bounds HOWARD's steps. The one published step bound of this kind is for
   simple stochastic games: Auger–Coucheney–Strozecki Lemma 5 (MAX-acyclic: ≤ 2·n_M steps), the analogue of k = 0 (RESULTS R122). So
   WIN / FVS-TCYC (T_CYC ≤ (P + N)(P + 1)^k) is NEW as a statement (searched: §6). The Ξ-feedback number is not the directed feedback
   vertex number of Γ(G), so Gajarský et al. Theorem 3 does not apply to it as it stands (§4).
6. CONTRADICTION check (§5). No opened lower bound contradicts Statement ABS or ALL-TCYC as stated. Two hypotheses of the abstract form
   are exactly where the known exponential families sit:
   - Friedmann's G_n (and every E-DOM-violating sink game): the step that breaks is «Odd's choices are decided at class level, with
     non-negative weights» = box 208 (K2) COARSE + (K3) (d), from E-DOM; it is used in (L3), in (P4) and in QUIET-N.
   - Zhong–Ye / Hansen–Zwick / Asadi et al. (one-player mean payoff): the step that breaks is (L5) through (L3) case (β): «the class
     of a cycle lying in the front takes at most M values». Under VJ a cycle's class is its top vertex; for mean payoff it is the
     cycle mean, and Zhong–Ye's cycles have «strictly increasing mean rewards».
7. For D18 (cross-field): the «iterate a two-player Dijkstra potential» family (GKK, Dorfman–Kaplan–Zwick, Schewe's OSI, QDPM, unified
   as PPI by Cadilhac–Casares–Ohlmann) has NO known superpolynomial lower bound as of that paper (their Question 19); §7.

## 1. What box 208 claims (verbatim), and its abstract form (READING)
- Statement ABS (box 208 §10, l. 376-381): «a SHORTEST-PATH GAME: a finite graph, every vertex owned by Max or Min, a target, an
  integer weight ≥ 0 on every edge, and no cycle of total weight 0. … HOWARD: every Max vertex moves to an edge (z, y) of largest
  w(z, y) + d_s(y), keeping its edge if that is one of them.» «From every positional start, Howard makes at most (number of edges of
  Max vertices)·(number of vertices) steps, and every step before the last one raises d at a vertex of the lowest lagging value.»
- Lemma LEVEL (§0, l. 22-25): «Φ never falls. At a step it stays equal exactly when no vertex of FRONT_t changes class (a STALL), and
  a stall forces FRONT_t to contain a whole cycle of the functional graph Ξ_(σ_b)»; «m_t takes at most 2M values».
- Theorem FVS-TCYC (§0, l. 35): «Ξ-feedback number k: T_CYC ≤ (P + N)·(P + 1)^k.» Lemma PLATEAU (Addendum A0): «every maximal
  interval [u, v] of states of constant Φ (reference b): v − u ≤ N + 2M + 5.» Theorem ALL-TCYC: «T_CYC ≤ P·(N + 2M + 6) + N».
- The abstract form, as I read §2-§4, §10 and A2 (my wording; the letters are used in §5):
  - (A1) a class map into a total order, pointwise non-decreasing along the run [(K1)];
  - (A2) along a play the class is constant, except at «cost» vertices where it strictly rises; the responder's choice is the face
    of lower class [(K3), (K4), with (K2) COARSE: the value order refines the class order]: non-negative weights at class level;
  - (A3) Howard's new value dominates every successor's old class [(K5), from DOM];
  - (A4) the lowest lagging class m_t takes polynomially many values [(L5)]: by (L3) it is the final class of a successor of an
    improver's vertex (one value per edge), or (case β) the class of a play cycle lying inside the front;
  - (A5) on a plateau the responder does not move on the part of class ≤ m [(P4)], so the run there is a one-player Howard run with
    fixed cycle nodes, bounded by a window bound [(P7), R118 (i) BR-SEG-G]; the tail after the last lag is bounded the same way
    [(C4), QUIET-N].
  ABS is (A1)-(A4) with no zero-weight cycle (no stall, no case β). ALL-TCYC adds (A5) for the zero-weight part.

## 2. Sources (opened 2026-11-12; sha256 prefixes and URLs in notes/L-LIT.md)
| source | location | quote / content | bears on |
| --- | --- | --- | --- |
| Khachiyan, Boros, Borys, Elbassioni, Gurvich, Rudolf, Zhao, «On short paths interdiction problems: total and node-wise limited interdiction», DIMACS TR 2007-02 (journal: Theory Comput. Syst. 43, 2008, DOI 10.1007/s00224-007-9025-6, not opened) | abstract PDF p.2; Theorem 1, PDF p.6; §2.2 | «MASPNLAI can be solved in strongly polynomial time by a natural extension of Dijkstra's algorithm.» Theorem 1: «a non-negative weight function w : A → R+» … «for blocking systems B2 the problem can be solved in O(\|A\| + \|V\| log \|V\|) time» | two-player Dijkstra: KNOWN (algorithm) |
| Fijalkow (ed.), Games on Graphs, arXiv 2305.10546 v2 (29 Jul 2025), ch. 5 (Fijalkow, Monmege) | Theorem 5.14, PDF p.199-201; notes PDF p.202 | «There exists an algorithm for computing the values in shortest path games with non-negative weights running in time O(m + n log(n)).» Invariant 2: «min {µ_i(u) : u ∈ S_i} ≥ max {val_G(u) : u ∉ S_i}» … «generalises the greedy property of Dijkstra's algorithm». Notes: «this has been proved by Khachiyan and coauthors [223]. No polynomial solution is known for the general case.»; «divergent shortest path games [88] in which the arena does not contain any cycle with total weight 0 … the value iteration algorithm converges in polynomial time» | KNOWN (algorithm); ABS's hypothesis «no cycle of weight 0» = «divergent» |
| the same book, ch. 5 | Theorem 5.6, PDF p.179; PDF p.183 | «There exists a strategy improvement algorithm for solving energy games in exponential time.» «There are lower bounds showing that the sequence can be of exponential length» | signed weights: exponential |
| Hansen, Ibsen-Jensen, Miltersen, «A faster algorithm for solving one-clock priced timed games», arXiv 1201.3498 v3 | §2, PDF p.4-9: priced games; Fig. 3; Lemma 2.3; Corollary 2.4; Fig. 4; Theorem 2.5 | priced game: «Each action j ∈ A has an associated non-negative cost» … «a single source shortest path problem from the point of view of Player 1, with the exception that an adversary, Player 2, controls some of the decisions». «Strategy iteration algorithm. We shall present a different algorithm for solving priced games, following the general strategy iteration pattern [11].» Valuation «ν(k, σ) = (u(k, σ), ℓ(k, σ))»; «The inclusion of the length in the definition of an improving switch is crucial» (zero-cost self-loops). Termination: «it ensures that each strategy is only encountered once, and the number of strategies is finite.» | strategy iteration on ABS's class: KNOWN as an algorithm; bound: finite only. The improver is the MINIMISER (mirror of ABS) |
| Bertsekas, «Robust shortest path planning and semicontractive dynamic programming», arXiv 1608.01670 v1 | §5.2 PDF p.23; §5.3 PDF p.25-30; Assumption 5.1; Prop. 5.1, 5.2 | §5.2: «the sequence {J_µk} is nonincreasing. It then follows that J_µk converges to J* in a finite number of iterations.» Assumption 5.1 (b): «For every improper policy µ, all cycles in the subgraph of arcs A_µ have positive length.» Prop. 5.2: «The Dijkstra-like algorithm will terminate after exactly N + 1 iterations». p.30: «It is also unclear how the Dijkstra-like algorithm compares with the finitely terminating VI algorithm and other asynchronous VI and PI algorithms» | PI bound: finite only; the comparison Dijkstra vs PI is stated as unclear |
| Guillot, Stauffer, «The stochastic shortest path problem: a polyhedral combinatorics perspective», arXiv 1702.03186 | abstract; §4.2 PDF p.9 | «(c) Value Iteration and Policy Iteration converge, and (d) we can extend Dijkstra's algorithm»; «Howard's policy iteration algorithm converges in a finite number of steps» | one player, stochastic: finite only |
| Björklund, Vorobyov, «A combinatorial strongly subexponential strategy improvement algorithm for mean payoff games», DAM 155 (2007) 210-229, author copy | §3.1 p.213-214; §5 p.219; §6 p.222; §10 p.226 | LSP: «a positional strategy that maximizes the shortest paths from all vertices to the distinguished sink». p.219: «The number of iterations will be at most pseudopolynomial, because distances increase in integral steps». p.222: «we can use a faster … implementation of Dijkstra's algorithm (requires nonnegative weights) … Nonnegative edge weights can be ensured by … potential transformations». p.226: «Currently we are unaware of any LSP instances that require superpolynomially many steps of the single random, multiple random, or all profitable (attractive) switches algorithms.» | ABS's orientation (the maximiser improves), signed weights: pseudopolynomial bound only; the lower bounds came later (Friedmann) |
| Cochet-Terrasson, Gaubert, «Policy iteration algorithm for shortest path problems» (report, PostScript from Gaubert's page) | abstract; Theorem 2.3 | «the worst case execution time of policy iteration is O(nm)»; «Theorem 2.3. The policy iteration algorithm stops at a step k ≤ n − 1.» (T65 §4 has the proof location.) | one player: KNOWN, Bellman–Ford form |
| Cadilhac, Casares, Ohlmann, «Fast value iteration: a uniform approach to efficient algorithms for energy games», arXiv 2110.07346 v3 (12 Feb 2025) | §1 PDF p.3; §4.1 PDF p.10; §6 PDF p.17 | «the core algorithmic idea underlying these two algorithms [OSI, QDPM] … is a natural adaptation of Dijkstra's algorithm to the two-player setting»; «Khachiyan, Gurvich and Zhao [24] solved the same problem earlier and in a different context (with an algorithm similar to Schewe's)»; p.17: «Currently, we lack any family of examples in which PPI takes more than a linear number of iterations, although we expect that it should admit exponential lower bounds.» «Question 19. Can one design superpolynomial lower bounds on the number of iterations for PPI?» | §7 |
| Luttenberger, arXiv 0806.2923 v4 | Prop. 4.19 | «VI_σ can be calculated using Dijkstra's algorithm» | Dijkstra inside one strategy-improvement step: KNOWN |
| Hansen, Miltersen, Zwick, arXiv 1008.0530 v1 | §1 PDF p.3; §7 PDF p.11 | «The policy/strategy iteration algorithms are strongly polynomial for a fixed discount factor, but exponential for non-discounted problems, or when the discount factor is part of the input.» | another proof technique (contraction), no front potential |
| Post, Ye, arXiv 1208.5083 v2 | p.2 | «Our results do not extend to policy iteration, and we leave this as a challenging open question.» | single-switch simplex only |
| Hansen, Kaplan, Zwick, SODA 2014, DOI 10.1137/1.9781611973402.63 | bibliographic page only | the PAPER is NOT OPENED (§6) | – |
| Gajarský, Lampis, Makino, Mitsou, Ordyniak, «Parameterized algorithms for parity games», MFCS 2015 (DOI 10.1007/978-3-662-48054-0_28), author copy | §1 PDF p.2-3; Theorem 3, Theorem 4, PDF p.9; Corollary 3 PDF p.17 | «Theorem 3. Given an instance of parity games G(V, E) and a directed feedback vertex set S, \|S\| ≤ k of G, there exists an algorithm which decides the problem in time O*(p^(log k) 4^k).» «Theorem 4. There exists an algorithm which given an instance of parity games G(V, E) such that \|V_1\| = k decides the problem in time O*(4^k p^(log k)).» p.2-3: treewidth «p^(O(k)) [25]»; «entanglement, DAG-width and kelly-width, algorithms running in n^(O(k)) time are known»; «this problem is not known to be FPT when the number of priorities is not part of the parameter for any non-trivial graph width» | fixed k, SOLVING: KNOWN |
| Mnich, Röglin, Rösner, «New deterministic algorithms for solving parity games», arXiv 1512.03246 v1 | abstract; Theorem 1 | «parity games in which one of the two players controls only a small number k of nodes» … «a fixed-parameter algorithm that solves bipartite parity games in time k^(O(√k))·O(n³), and general parity games in time (p + k)^(O(√k))·O(pnm)» | fixed k, SOLVING: KNOWN |
| Berwanger, Dawar, Hunter, Kreutzer, «DAG-width and parity games», full version (author copy; journal JCTB 102 (2012), DOI 10.1016/j.jctb.2012.04.004, not opened) | p.2; Theorem 4.5, PDF p.22 | «Theorem 4.5. For each k, there is a polynomial p and an algorithm running in time O(p(n)) which determines the winner of parity games on all graphs with DAG-width at most k.» p.2: bounded tree-width by Courcelle; «Obdržàlek [11] exhibited a particular such algorithm» | fixed k, SOLVING: KNOWN |
| Fearnley, Schewe, arXiv 1112.0221 (LMCS 9(2:06) 2013) | abstract | «parity games with bounded DAG width can be solved in O(n^(k+3)·k^(k+2)·(d + 1)^(3k+2)) time» … «bounded treewidth can be solved in O(n·k^(k+5)·(d + 1)^(3k+5)) time» | fixed k, SOLVING: KNOWN |
| Auger, Coucheney, Strozecki, «Finding optimal strategies of almost acyclic simple stochastic games», arXiv 1402.0471 v1 | p.2-3; Definition 5 PDF p.8; Lemma 5 PDF p.9; Theorem 5 PDF p.11; Theorem 8 PDF p.18 | Definition 5: «MAX-acyclic … if from any MAX vertex x …, for all outgoing arcs a but one, all plays going through a never reach x again.» «Lemma 5. Let G be a strongly connected, MAX-acyclic SSG, where all MAX vertices have degree 2. Then the Hoffman-Karp algorithm, starting from any strategy σ_0, halts in at most 2n_M steps.» «Theorem 8. There is an algorithm which solves any stopping SSG in time O(n^(k+1)) where n is the number of vertices and k the size of the minimal feedback vertex set.» p.2: «in the simpler case of parity games the best algorithms for DAG-width and clique-width are polynomials but not even FPT» | a published STEP bound for strategy iteration in an acyclic-type class (k = 0 analogue); fixed k by another algorithm |
| Friedmann, arXiv 1106.0778 v2 (LMCS 7(3:19) 2011) | §5 PDF p.8; Table 4 PDF p.15; Lemma 6.6 PDF p.14; Theorem 6.14 PDF p.23 | re-used from T66 §1, §3 (quotes there) | §5.1 |
| Zhong, Ye, arXiv 2609.40147 v2 (13 Oct 2026; unrefereed preprint) | Theorem 6.1 PDF p.23; p.26; Theorem 7.2 and the text after it, PDF p.33 | Theorem 6.1: «at least exp(Ω(N)) iterations from a specified initial policy before any state attains its optimal gain». p.26: «the encoded cycles have strictly increasing mean rewards, with consecutive differences 2^(−d−1)/(6d)». p.33: «Every N consecutive updates before termination create a new cycle, and each update creating a cycle increases the sum of state gains by at least 1/N. This sum is nondecreasing and smaller than N·2^b.» | §5.2. A CLAIM of an unrefereed preprint; proofs not checked here |
| Fearnley, Savani, arXiv 1507.04500 (LMCS 14(4:9) 2018) | abstract | «We show PSPACE-completeness of the edge switch problem and optimal strategy problem for … Parity games with the discrete strategy improvement algorithm of Vöge and Jurdziński» (all-switches) | §5.1: no step bound can hold for Howard on all VJ games |

## 3. Verdicts on the pieces
| piece of box 208 | label | by what |
| --- | --- | --- |
| the class of games of ABS (two-player shortest paths, weights ≥ 0) | KNOWN | «priced games» (Hansen–Ibsen-Jensen–Miltersen §2), «shortest path games with non-negative weights» (Games on Graphs §5.4), «robust shortest path» (Bertsekas), MASPNLAI (Khachiyan et al.) |
| ABS's hypothesis «no cycle of total weight 0» | KNOWN as a named condition | «divergent» (Games on Graphs p.202); Bertsekas Assumption 5.1 (b) |
| solving that class by a Dijkstra pass (settle the lowest label) | KNOWN | Khachiyan et al. Theorem 1; Games on Graphs Theorem 5.14; Bertsekas Prop. 5.1-5.3 |
| strategy iteration on that class, as an algorithm | KNOWN | Hansen–Ibsen-Jensen–Miltersen Fig. 4, Theorem 2.5; Bertsekas §5.2; with signed weights Björklund–Vorobyov §3-§5 |
| Howard's steps there ≤ (edges of Max)·(vertices), by the potential (lowest lagging value, −front size) | NEW (searched: §6), weakly | the three sources that present policy iteration next to a Dijkstra algorithm prove finiteness only; Bertsekas calls the comparison «unclear» |
| the same for ONE player (longest / shortest paths) | KNOWN, in Bellman–Ford form | Cochet-Terrasson–Gaubert Theorem 2.3 (≤ n − 1 steps; tight by their Example 5.1) |
| a second valuation component for zero-weight cycles | KNOWN | Hansen–Ibsen-Jensen–Miltersen p.7: the pair (cost, length), the length being «crucial»; VJ's (Π, k) plays this role in box 208 |
| Lemma LEVEL on Γ(G): (K1)-(K5), the stall ⇒ Ξ-cycle step | NEW (fleet-internal; nothing to compare outside) | the genome class is the fleet's own (R104); the mechanism is ABS's |
| Lemma PLATEAU: plateau = one-player Howard run with fixed cycle nodes, ≤ n_E steps | the reduction: NEW (fleet-internal). The bound it calls: landed R118 (i); KNOWN outside for additive weights and mean payoff | T65 §4-§5: Cochet-Terrasson–Gaubert Theorem 2.3; Zhong–Ye Theorem 7.2's proof («Every N consecutive updates … create a new cycle») |
| WIN / K1-TCYC / FVS-TCYC: Howard's steps polynomial for fixed Ξ-feedback number k | NEW as a statement (searched: §6) | no fixed-parameter bound on strategy-improvement STEPS in the opened sources, except Auger–Coucheney–Strozecki Lemma 5 (the k = 0 analogue) |
| parity games are solvable in polynomial time for fixed k (feedback vertex set, k vertices of one player, DAG-width, treewidth) | KNOWN, by other algorithms | Gajarský et al. Theorems 3, 4; Mnich–Röglin–Rösner Theorem 1; Berwanger et al. Theorem 4.5; Fearnley–Schewe |
- Why «weakly» (READING). ABS's proof is Dijkstra's exchange argument applied to the vertices that have not reached their final
  value. A reader who knows Khachiyan et al.'s algorithm and Howard's domination property (one policy-iteration step dominates one
  Bellman step: Hansen–Miltersen–Zwick Lemma 5.3, quoted in T65 §4) can rebuild it. It is still not a corollary of «Howard dominates
  value iteration»: synchronous value iteration from below is only pseudopolynomial on these games (a Max vertex on a positive cycle
  climbs by the cycle weight per round), and the proof uses that Howard's values are exact at the Min vertices ((K3′), (K4′)).
- Orientation (READING). In ABS the MAXIMISER improves and the minimiser answers with shortest paths: Björklund–Vorobyov's LSP. In
  Hansen–Ibsen-Jensen–Miltersen's outer loop and in Bertsekas §5.2 the MINIMISER improves. A citation of either as «the same
  algorithm» would be wrong without this remark.

## 4. Fixed k: what the parameterized literature gives and does not give (READING)
- It gives polynomial-time SOLVING for fixed k, by recursion on dominion hitters (Gajarský et al.) or dynamic programming over a
  decomposition (Berwanger et al., Fearnley–Schewe, Obdržálek [CAV 2003, NOT OPENED; cited through the two papers above]).
- It gives no bound on Howard's steps. I found no statement «strategy improvement makes polynomially many steps on parity games of
  bounded treewidth / DAG-width / feedback vertex number».
- The trivial fixed-k bound for a player with k choice vertices (enumerate that player's ≤ n^k positional strategies, solve n^k
  one-player games) is folklore; Gajarský et al. Theorem 4 and Mnich–Röglin–Rösner Theorem 1 improve it to FPT. Inside the fleet:
  RESULTS R51 / R57 (N5 on 𝒞^1O, 𝒞^1E), R61 (f = O(n^(k+1)) per phase on 𝒞^kO).
- The Ξ-feedback number (box 208 §1, from R126: «the minimum size of a set of movers meeting every cycle … of the Ξ-graph on the
  movers») counts cycles of Ξ-edges only. Γ(G) also has the W-edges e → W-target, and a cycle of Γ(G) may use them. So k is not the
  directed feedback vertex number of Γ(G), and Gajarský et al. Theorem 3 is not a statement about k. (Solving Γ(G) is not the question
  in any case: T_CYC counts Howard's steps.)
- Nearest published statement to WIN: Auger–Coucheney–Strozecki Lemma 5. Its proof is a «closed once» argument (PDF p.9: «if a MAX
  vertex is closed it cannot be opened and closed again, and if it is open it can only be closed once»), the same shape as landed
  R122 (Ξ-acyclic ⇒ T_CYC ≤ N). Their step from k = 0 to k > 0 is NOT a step bound for one strategy-iteration run: Theorem 5 enumerates
  the 2^(k_p) local choices at fork vertices and runs Hoffman–Karp on each acyclic subgame; Theorem 8 eliminates feedback vertices
  by a binary search on values. So the mechanism of FVS-TCYC (freeze one more feedback vertex per nested plateau, a factor P + 1
  each) has no counterpart there.

## 5. Contradiction check against the known lower bounds (READING, with the sources' own words)
### 5.1 Friedmann's G_n ([F09] Theorem 8, [F11] Theorem 6.14; Howard = I^loc; T66)
- Not an instance of ABS or of ALL-TCYC: G_n is not a genome game (T66 §3: E-DOM fails; [F11] Table 4 has the odd f_j, k_j above the
  exits h_i for i < j).
- Where the abstract form breaks on G_n. G_n is a 1-sink game: Λ = x for every vertex at every state (T66 §5.1: C = 0).
  - With the coarsest class map (class = Λ) no vertex ever lags. (A1)-(A4) hold trivially and say nothing. The whole run is «after
    the last lag», and (A5) fails: Odd's gates flip while no class changes (T66 §5.1, DATA N ≤ 8, two engines: 502 flips at N = 8,
    fit 2^(N+1) − N − 2). So (P4) / QUIET-N is false there.
  - With the finest class map (class = the whole value Ω) Odd's choice is decided at class level, and (A2) fails: an odd vertex has
    a LOWER value than its successor on the play, so the class is not non-increasing along a play. The class-level game is a
    shortest-path game with weights of both signs, i.e. Björklund–Vorobyov's LSP, where only the pseudopolynomial bound is
    available (p.219).
  - For every class map at least one of (A1)-(A5) must fail on G_n; otherwise the abstract argument would bound a run that [F11]
    Theorem 6.14 proves exponential. The two extreme maps show the two ways. I did not analyse intermediate maps.
- So the genome-only step is: «Odd's choices are decided at class level AND the class-level weights are non-negative». In box 208
  this is (K2) COARSE with (K3) (d) and (K4); it enters (L3) (the play of a front vertex stays at class ≤ m), (P4) (Odd frozen on a
  plateau) and QUIET-N (the tail). Its source is E-DOM (R121: «Every vertex more relevant than some e-vertex is an e-vertex, c_W, K0
  or K3») together with NO-TIE / LOC-GATE (R123). This agrees with box 208 A5's own sentence («Odd's choices are decided at class
  level (K2, K4, (P4)), where only e-vertices count and they count for Even») and with T66 §6.
- Fearnley–Savani (PSPACE-completeness of predicting all-switches strategy improvement on parity games, by one-sink constructions)
  says the same from the complexity side: no argument of this shape can hold for Howard on all VJ games.
### 5.2 One-player mean-payoff lower bounds (Hansen–Zwick Ω(n²); Asadi et al. Theorem 3.2; Zhong–Ye Theorem 6.1, a preprint's CLAIM)
- Not instances of ABS (no target; every play ends in a cycle) and not genome games.
- Transfer of the abstract form with class := gain (one player, so (A2) and (A5)'s «responder frozen» are empty): (A1) gains never
  fall; (A3) Howard's gain step dominates; plateaus are bias-only stretches without a new cycle, at most N steps (Zhong–Ye p.33).
  All of this HOLDS. What fails is (A4): in (L3) case (β) the lowest lagging class is the gain of a current cycle whose vertices all
  lag, and that gain is a cycle MEAN. Zhong–Ye's family runs through exponentially many cycles with «strictly increasing mean
  rewards» «before any state attains its optimal gain»: every state lags the whole time, so every step is in case (β).
- Under VJ the class of a cycle is its top vertex, (c, ∅): at most M values on Γ(G) (box 208 (L5)), at most n on any game. This is
  T65 §6's sentence («Two cycles with the same top vertex are the same gain for VJ and different gains for mean payoff») seen from
  box 208. Zhong–Ye state the same criterion themselves: the bound of Theorem 7.2 is the number of possible gain increments.
- Hansen–Zwick's and Asadi et al.'s Ω(n²) are below every bound of box 208; no conflict in any reading.
### 5.3 Shortest-path lower bounds
- Cochet-Terrasson–Gaubert Example 5.1 (n − 1 steps, one player): inside ABS's bound.
- Hansen–Kaplan–Zwick's Ω(n²) for Dantzig's rule on shortest paths (from the bibliographic summary only; paper NOT OPENED): another
  rule (one switch per step), and below ABS's bound.
- I found no lower bound for strategy iteration on two-player shortest-path games with non-negative weights.
### 5.4 Result
CONTRADICTS: nothing. The two hypotheses that carry the weight are (A2) [E-DOM: non-negative class-level weights with Odd decided
at class level] against the two-player exponential families, and (A4) [VJ: few classes of cycles] against the mean-payoff ones.
A referee of box 208 should press on exactly these: (K2) with (K3) (d) and NO-TIE, and (L3) case (β) with (L5).

## 6. Searched where; not opened; limits
- Full text opened and searched (grep for Dijkstra, policy / strategy iteration, iterations, polynomial, feedback): the sources of §2.
- Web searches (2026-11-12): «strategy improvement shortest path games non-negative weights polynomial iterations Dijkstra»;
  «strategy iteration priced games / reachability-price games / min-cost reachability non-negative Dijkstra»; «policy iteration
  deterministic shortest path nonnegative arc lengths at most n iterations Dijkstra»; «Howard policy iteration Dijkstra potential
  shortest path game / reachability game / stopping game» (extended mode); «strategy improvement feedback vertex set / treewidth number
  of iterations»; the Gajarský, Khachiyan and Hansen–Kaplan–Zwick titles. This lane's T48, T54, T58, T63, T64, T65 (DMDP and
  elimination literature) contain no such bound either.
- NOT OPENED (reported, never paraphrased): Hansen–Kaplan–Zwick SODA 2014 (epubs.siam.org returns an HTML wall; three author URLs
  404; only a bibliographic page); Khachiyan–Gurvich–Zhao CSR 2006 (Springer; the DIMACS report of the journal version was opened
  instead); the journal versions of Khachiyan et al. and Berwanger et al.; Obdržálek CAV 2003; Schewe CSL 2008 (OSI; read through
  Cadilhac–Casares–Ohlmann and Luttenberger); Rutkowski QAPL 2011; Gimbert–Horn 2008 and Ibsen-Jensen–Miltersen 2012 (few random
  vertices); Bertsekas's DP book §3.4.1 («consistently improving policies»); Vladimirsky 2008.
- Limits. «NEW» rests on about thirty sources and six searches in one session. A statement of ABS could sit in a textbook exercise
  or in the priced-timed-games literature that I did not open. I did not check any proof of box 208 or of the preprints.
  The abstract form (A1)-(A5) is my wording, not L-NEW's.

## 7. Cross-field notes for the designers (D18; READING)
- Cadilhac–Casares–Ohlmann's PPI («Positive Path Iteration») is «iterate the two-player Dijkstra potential En+ until a fixpoint».
  It is their «reinterpretation of OSI and QDPM». They report that it solves Friedmann's families «in linear time» and that no family with more
  than linearly many iterations is known (p.17, Question 19; they «expect» exponential lower bounds). Box 208's reading («at class
  level the game is a shortest-path game with non-negative weights») is the same decomposition: non-negative part by Dijkstra, the
  rest by iteration. If the fleet wants a second candidate outside N5, PPI is a published one with an open lower-bound question.
  It is NOT a polynomial-time claim: they cite Friedmann's thesis («[17, Sect. 4.6.2]», not re-opened by me today) for an
  exponential family for OSI, and report only experiments for PPI.
- Hansen–Ibsen-Jensen–Miltersen analyse one-clock priced timed games by running strategy iteration on priced games («our analysis
  of the running time will use this strategy iteration algorithm in non-trivial ways», PDF p.7). Their bound on the number L(G) of
  event points is exponential, and «L(G) ≤ p(n) for some polynomial p» is their Conjecture 5.1 (PDF p.27). The priced-game core has
  no step bound there; ABS, if it survives the referees, would be one, in the mirrored orientation.
- Björklund–Vorobyov's remark that DAG instances of LSP are solvable by dynamic programming (p.214) is the k = 0 case of every
  feedback parameterization; nothing between «DAG» and «general» is treated there.

## DONE / FINDINGS / NEEDS
- DONE: this note; docs/lit/T69-summary.md; T66 Addendum C (T68 item 3); notes/L-LIT.md rows.
- FINDINGS:
  1. Two-player Dijkstra for non-negative weights: KNOWN (Khachiyan et al. Theorem 1; Games on Graphs Theorem 5.14; Bertsekas §5.3).
  2. Strategy iteration on that class: KNOWN as an algorithm; only finite termination is proved (Hansen–Ibsen-Jensen–Miltersen
     Theorem 2.5; Bertsekas §5.2; Guillot–Stauffer §4.2). A polynomial step bound by a lowest-lagging-value potential: NEW (searched),
     weakly. One player: KNOWN (Cochet-Terrasson–Gaubert Theorem 2.3).
  3. Fixed k: SOLVING is KNOWN (Gajarský et al. Theorems 3, 4; Mnich–Röglin–Rösner; DAG-width; treewidth); a step bound for Howard
     at fixed feedback number: NEW as a statement; nearest: Auger–Coucheney–Strozecki Lemma 5 (k = 0 analogue, simple stochastic games).
  4. No CONTRADICTION. Break points of the abstract form: (K2) + (K3) (d) + NO-TIE (E-DOM) against Friedmann; (L3) (β) / (L5) (few
     classes of cycles, VJ) against Zhong–Ye / Hansen–Zwick.
  5. PPI (Cadilhac–Casares–Ohlmann, Question 19): a published Dijkstra-potential iteration with no known superpolynomial lower bound.
- NEEDS: Lead: relay §5.4 to the referees of box 208 (the two steps to press) and §3's orientation remark to L-NEW (any citation of
  Hansen–Ibsen-Jensen–Miltersen or Bertsekas must say that the minimiser improves there). Owner: nothing (optional library:
  Hansen–Kaplan–Zwick SODA 2014; Schewe CSL 2008; Obdržálek CAV 2003).
