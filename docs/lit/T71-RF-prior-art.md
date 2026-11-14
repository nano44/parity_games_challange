# T71: candidate RF («ROOT-FIRST») against the literature: prior art (item 1) and applicable lower bounds (item 2)
L-LIT successor (design day, D27 / D28 / L61; Lead brief 2026-11-14 14:36Z). Written 2026-11-14 (date -u in the commit). Working note,
unrefereed. Not a TARGET.md claim; not M3 or M4. RF is a CANDIDATE under attack (D1); nothing here says RF is polynomial.

**Status added 2026-11-14 19:06Z (date -u), after this note was written.** RF is reported DEAD by the Lead (messages 15:39Z and
19:05Z, quoted): L-RED-B 8's rule-built family K^s_n (|V| = 3n² + 3n + 1) on which «RF makes exactly 7·2^(n−1) − 2n − 3
iterations for n = 2..15», «confirmed by L-SI's rebuild; its repairs die on decoyed counters». That family is fleet-internal and
not checked by me. In the Lead's words K^s_n uses «one cycle gate per (bit, context), a reader chain for lowest-first order, skip
edges against early refresh», i.e. the missing ingredient named in §4 (b) below (lowest-first re-closing). The Lead also confirmed
my reading of RF against L-SI's engine (switchallexp and switchbestexp rows equal at N = 1..6; frozen statement docs/si/
box109-design.md §4.2 at claude/l-si c236bca94). This note stays as the record of the dead candidate's prior art and of where the
literature said to dig. No second search pass was made (Lead 19:05Z).

Owner rulings, verbatim:
> A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below. (D1)
> SO we have to look for a new algorithm no? Do we have any promising lead or can convert our learning into a new promising algorithm? (D27)

Labels: PROVED-in-source (a theorem of an opened source, quoted); DATA (my runs, one engine, unrefereed); READING (L-LIT interpretation,
not to sign). «NOT RF» / «CLOSE» / «EQUIVALENT» are verdicts on whether a published rule covers RF. Every source below was opened in
this session (by me, or by a literature agent whose download I then read at the quoted lines); sha256 prefixes are in §6 and in
notes/L-LIT.md. The draft barrier statement (item 3) is docs/lit/T72-RF-barrier.md.

## 0. Answers in short
1. **Prior art: RF was NOT FOUND** in about 50 opened sources (searched where: §2, §6). No opened source defines a dependency relation
   between improvable vertices through the plays of the current pair (σ, σ̄), and none switches only the sink components of such a
   relation. «Not found» is a search result, not a proof of novelty (not opened: Hansen's thesis, Hoffmann–Luttenberger ATVA 2013,
   the Gauss–Seidel policy-iteration primaries, Vöge's thesis).
2. **Nearest published relatives**, each different in a way that matters:
   - Melekopoglou–Condon's Topological Policy Improvement (1994): bottom-up by strongly connected component, but of the WHOLE graph,
     fixed once, single-switch, on stochastic one-player games; exponential (their Corollary 2.9), linear on acyclic graphs.
   - Schewe's optimal improvement (CSL 2008): same diagnosis as RF («blind towards the cross effect of different modifications»),
     opposite remedy (the best combination, by a Dijkstra-like sweep); exponential by Friedmann's Theorem 8.4.
   - Fearnley's strategy trees (LPAR 2010): the same play-graph tree, used to classify improving edges as back or cross edges and
     to remember snares; superpolynomial by Friedmann (DAM 2013, Theorem 26).
   - Björklund–Vorobyov §10 (2007): the mirror image of RF (always the switch FARTHEST from the sink) visits all 2^n strategies on
     an acyclic instance that sink-first dynamic programming solves in one pass.
   - Shortest paths: Tarjan's subtree disassembly and Goldberg–Radzik's topological scan (Cherkassky–Goldberg 1999, Lemma 8,
     Theorem 4) are RF's one-player ancestors: do not act on a vertex whose tree ancestor is about to change. Their O(nm) bounds come
     from the FIFO pass structure, which RF does not have.
3. **Applicable lower bounds (item 2).** Only ONE published counter is cancelled by RF's delay: Friedmann's G_n for the locally
   optimizing policy, whose reset is simultaneous with the exit update ([F] Lemma 6.11). In Friedmann's H_n (built for Schewe's rule)
   the reset is built to persist for two iterations, RF does NOT see it, and the reset happens under RF (DATA: bit i's cycle is
   reopened n − i times, n(n − 1)/2 reopenings in all, n = 2..7). Odd's replies also flip repeatedly on PGSolver's switchallexp /
   switchbestexp and on both snare families. RF is polynomial on all of them in DATA (H_n: 7n² + 11n − 13, n = 2..8) for a
   second, independent reason: the reopened bits re-close HIGHEST first (closing order 1 | 2 1 | 3 2 1 | 4 3 2 1 …; a binary
   counter needs 1 | 2 | 1 | 3 | 1 | 2 | 1 …), so no cascade forms.
4. **Where to dig** (§4): a binary counter against RF needs (a) H_n's two-iteration reset (a delay node that keeps the exit update
   invisible for one iteration) and (b) lowest-first re-closing. On H_n RF inverts the order through ONE channel, named by the trace: after a
   reset the exit selector k_i still leads into the reopened gate of bit i + 1, so bit i's cycle nodes wait for bit i + 1.
   (a) is published and works under RF as it stands. (b), cutting that channel, is the open design problem. Single-switch families (Zadeh, Cunningham,
   Bland, Random-Facet) are no guide: on the ports they do not even slow switch-all.
5. **One-player case** (§2.10): arbitrary subsets of improving switches are exponential on one-player games (fleet CDAG_n; BV07
   §10 with trivial Odd vertices; Friedmann–Hansen–Zwick for acyclic shortest paths), so RF's one-player bound is not covered by
   VJ00 Prop. 7.4 (stated for the standard policy, without proof) nor by RESULTS R17 / R118 (other rules). It needs its own proof.
   It does NOT imply the open problem of Howard's rule on deterministic MDPs (there the number of distinct gains is unbounded; under
   the VJ valuation a vertex's cycle node takes at most n values).

## 1. The object
RF, as stated in the Lead's brief (L-SI 57; no RF file was on origin/claude/l-si at 8c062914 when this was written):
«in the play graph of (σ, σ̄), an improvable Even vertex v DEPENDS on an improvable u ≠ v iff u lies on the play from σ(v) or from one
of v's improving targets; switch-best exactly at the improvable vertices in the SINK strongly connected components of the dependency
digraph.» Memoryless, deterministic, one-sided (Even improves, Odd answers with an optimal counterstrategy), VJ valuations.
- In Friedmann's terms RF is an improvement policy: a map σ ↦ σ′ with every edge of σ′ in the improvement arena A_{G,σ} and at least
  one strict improvement ([F] §3, PDF p.5-6: «an improvement policy is a map I_G : S_0(G) → S_0(G) fulfilling the following two
  conditions …»). So RF is INSIDE the class for which [F] proves bounds rule by rule, and inside VJ00's scheme (§2.1).
- My reading as code: docs/lit/T71-rf-trace.py (engine experiments/si/si.py, read-only; «lies on the play» = path and final cycle;
  best successor with the engine's PGSolver tie-break). It reproduces every number of the Lead's brief that I could compare: G_n
  from ι: 5, 9, 12, 15, 18, 21, 24 at n = 1..7; switchallexp 10 at N = 1 and 65 at N = 8; switchbestexp 17 at N = 1 and 106 at
  N = 8. It is NOT the lane's reference implementation; a difference between it and L-SI's engine on any other instance would be
  a finding about my reading.

## 2. Prior art (item 1): one paragraph per rule
### 2.1 Vöge–Jurdziński (CAV 2000; BRICS RS-00-48): any non-empty subset; a linear policy exists
- Rule: «Improve(σ) = Switch_I(σ) for some set I ≠ ∅ of improvements for σ» (BRICS §4.4); the «standard policy» is «switching all
  switchable vertices in every strategy improvement step» (§7, printed p.26-27; T22).
- Proved or stated: Prop. 7.1 «For every initial strategy, there is a strategy improvement policy of length at most n. Moreover,
  there is such a policy switching exactly one edge in every improvement step.»; Prop. 7.4 (O(n³) steps on one-player games, no
  proof; T22: safe reading = the standard policy); Prop. 7.5 (product of out-degrees). Friedmann restates the existence result with
  a proof: [F] Lemma 4.3 «There is an improvement policy I^lin_G s.t. the strategy improvement algorithm requires at most |V| many
  iterations.» The policy uses an optimal strategy σ*, so it is not an algorithm.
- Covers RF? RF is one of the allowed subset choices, so correctness and termination are covered (any subset of improving switches
  is a strict improvement: [F] Theorem 3.2). No step bound for RF follows. NOT RF as a rule (no rule is fixed).

### 2.2 Schewe's optimal improvement (CSL 2008, LNCS 5213; the brief says ICALP 2008) and Friedmann's bound for it; Luttenberger
- Rule: «a novel strategy improvement algorithm … which is guaranteed to select, in each improvement step, an optimal combination
  of local strategy modifications» (abstract). Diagnosis, verbatim: current methods «are completely blind towards the cross effect
  of different modifications: Applying one profitable modification may render all other profitable modifications adversarial»
  (abstract); «the game-based approach allows for fixing an optimal decision for a game position after all of its successors have
  been reevaluated» (§1). Computed by a sweep that «generalizes Dijkstra's single source shortest path algorithm to two player
  games» (§4; Theorem 4: O(m + δ log δ) arithmetic operations per step). In [F]'s words: «strategy improvement with a one-step
  lookahead; it computes the optimal strategy under all possible strategies that can be reached by a single improvement step» (§4).
- Proved: no iteration bound in Schewe's paper. [F] Theorem 8.4: «The Strategy Improvement Algorithm with the I^glo-policy requires
  at least 2^n improvement steps on H_n starting with ι_{H_n}.» Luttenberger (arXiv 0806.2923 v4) reobtains Schewe's step from
  «all profitable switches» on non-deterministic strategies and proves at most 3 · 1.724^|V_0| steps for out-degree two (Theorem 5.4); H_n
  applies to it as to Schewe's rule.
- Covers RF? NOT RF, but the nearest in purpose. Both rules exist because simultaneous switches interfere. Schewe resolves the
  interference inside one step by optimizing over the improvement arena; RF resolves it by postponing every switch whose compared
  plays contain another pending switch. Neither dominates the other: on H_n Schewe's rule is exponential (PROVED-in-source) and RF
  is quadratic (DATA, §3); whether RF is ever worse than Schewe's rule by more than a polynomial is open.
- Lesson carried by [F] p.7 for every «one step optimal» argument about RF: «The reason why this proposition is incorrect lies in
  the intransitivity of optimality of strategy updates.»

### 2.3 Fearnley's non-oblivious strategy improvement (LPAR 2010, arXiv 1003.2976 v1) and its worst case
- Structure: «Definition 10 (Strategy Tree). Given a Max strategy σ and a Min strategy τ we define the tree T^{σ,τ} = (V, E′) where
  E′ = {(v, u) : σ(v) = u or τ(v) = u}.» «T^{σ,τ} is a tree rooted at the sink whose edges are those chosen by σ and τ.» «We call
  this a profitable back edge if u is in Subtree_σ(v), otherwise we call it a profitable cross edge.» (§5; setting: Björklund–
  Vorobyov's mean-payoff algorithm with a sink.) A profitable back edge yields a snare (Definition 11, Proposition 12); the
  algorithm remembers snares and runs FixSnare (Algorithm 1) when that is better than the base (oblivious) policy.
- Proved: Fearnley shows polynomial behaviour on Friedmann's examples (§8). Friedmann, «A Superpolynomial Lower Bound for Strategy
  Iteration based on Snare Memorization» (author preprint of DAM 161 (2013) 1317-1337): Theorem 11 (on [F]'s G_n the snare rule is
  polynomial) and Theorem 26: «The snare memorizing strategy improvement algorithm parameterized with the locally optimizing rule
  requires time exponential in n to solve H_n, no matter which particular snare rule is applied.» (this H_n is the preprint's own
  family: «every cycle looks a bit differently in each iteration, yielding an exponential number of different occurring snares»).
- Covers RF? NOT RF. It is the one parity / mean-payoff source that classifies improving edges by their position in the tree of
  the current pair (σ, σ̄), which is RF's play graph. A back edge (v, u) is the case «v lies on the play from its own improving
  target u»; RF's dependency asks the same question about OTHER improvable vertices. Fearnley uses the classification for memory,
  not for ordering; his base policy still switches everything.
- Bearing on RF: the two published rules that «fix» G_n by structure (snares; Schewe's lookahead) both fell to a modified counter
  within about a year. RF fixes G_n too (§3). That pattern is the base rate. Fearnley's own caveat (§9) applies to RF's DATA word
  for word: «It must be stressed that we are not claiming that simply terminating in polynomial time on Friedmann's examples is a
  major step forward. After all, the randomized switching policies of Björklund and Vorobyov [2] have the same property.»

### 2.4 Björklund–Vorobyov (DAM 155 (2007) 210-229) and Björklund–Sandberg–Vorobyov
- Rule: one attractive (improving) single switch at a time on the longest-shortest-path form of mean payoff games, order by
  Kalai / Matoušek–Sharir–Welzl randomization; 2^O(√(n log n)) expected (abstract).
- On order, verbatim: «The order in which attractive switches are made is crucial for the subexponential complexity bound. Section
  10 gives an example of a poor switching policy with an exponentially long chain of attractive switches.» §10: a (2n + 2)-vertex
  graph with MAX and MIN vertices, sink leftmost; from a designed start the policy that «always makes the rightmost attractive
  single switch … visits all 2^n possible strategies of MAX». And: these instances «are "trivial", because the graphs are acyclic
  and longest shortest distances are easily computable by dynamic programming in polynomial time (in the left-to-right order)».
  §12 (Conclusions): «The remaining major open problem is whether any strategy improvement scheme for the games discussed (or any other) has
  polynomial time complexity.»
- Covers RF? NOT RF; it is the published statement of RF's motivating contrast: farthest-from-sink first is exponential where
  sink-first is one pass, on ACYCLIC instances. No sink-first rule is defined for general graphs. The pseudo-Boolean paper
  (Björklund–Sandberg–Vorobyov, PSI 2003) lists rules on the strategy hypercube only (greedy / random single switch, all profitable
  switches, random multiple switches, Kalai–Ludwig); none reads the graph.

### 2.5 Symmetric strategy improvement (Schewe–Trivedi–Varghese, arXiv 1501.06484) and van Dijk–Loho–Maat's bound
- Rule: both players improve at once; a player takes only improving edges that agree with the other player's optimal
  counterstrategy (vDLM p.7 Algorithm 2; T20 §1 has the quotes).
- Proved: van Dijk–Loho–Maat (arXiv 2309.02223 v1) «Theorem 1. In the worst case, the number of iterations of symmetric strategy
  improvement in parity games, mean payoff games and discounted payoff games is exponential in the number of nodes and edges in the
  graph independently of the improvement rule.» and, on the contrast with the one-sided setting: «This is different from regular
  strategy improvement, where the existence of a (theoretical) improvement rule for which the algorithm terminates in a linear
  number of iterations is guaranteed».
- Covers RF? NOT RF: RF is one-sided, so Theorem 1's «independently of the improvement rule» does not reach it (BARRIERS B11).
  «van Dijk's counters» (Two Counters, GandALF 2019, B6) are built for priority promotion / tangle learning / Zielonka, not for
  strategy improvement; RF on tc / tc+ is a battery question (L-COMP), not a literature one.

### 2.6 Melekopoglou–Condon's Topological Policy Improvement (ORSA J. Comput. 6(2), 1994; author copy) — the nearest rule shape
- Rule, verbatim (§2, p.3 of the author copy): «The vertices are topologically sorted, that is, an integer order is assigned to
  each min vertex, such that if there is a path from vertex i to vertex j, then the order of i is greater or equal to the order of
  j. The graph is in this way divided into components of vertices with the same order. The select procedure selects the largest
  numbered switchable vertex in the component of lowest order that contains switchable vertices. In this way, when a vertex i is
  switched, there is a decrease in the cost of every vertex with larger order from which there is a path to i, according to the
  current policy.»
- Proved (same paragraph): «If a directed graph is divided into k strongly connected components, and the numbers of min vertices
  in them are n_1, n_2, ..., n_k, then, in the worst case the algorithm takes 2^n1 + 2^n2 + . . . + 2^nk steps. … In particular, if
  the graph is acyclic the algorithm makes at most linear number of switches.» Lower bound: Theorem 2.8 (2^n − 1 switches for the
  difference rule on G_n) and «Corollary 2.9. The topological policy improvement algorithm requires exponential time in the worst
  case.» Christ–Yannakakis (arXiv 2212.00083 v1, §2 p.7; Theorem 6) restate the rule («the graph is partitioned into strongly
  connected components and each state is assigned the index of its component in a topological order») and prove the 2^n bound
  robust under perturbation.
- Covers RF? CLOSE in shape, NOT RF. Four differences: (i) the components are those of the whole graph over all actions, computed
  once; RF's are components of a dependency relation recomputed from the current plays; (ii) one switch per step; RF switches a
  whole set; (iii) a Markov decision process with average (random) vertices, one player; (iv) the exponential example is a single
  non-trivial component, where the topological order says nothing.
- Bearing on RF: on a game whose improvable vertices are mutually dependent, RF degenerates to switch-best-everywhere, exactly as
  topological improvement degenerates to the simple rule inside one component. MC94's bound is the published warning that
  «bottom-up by component» alone buys nothing once the adversary puts the counter inside one component. For RF the adversary's
  version of that is §4 (b).

### 2.7 Structured-subset rules for Markov decision processes (batch switching and relatives)
- Mansour–Singh (UAI 1999, arXiv 1301.6718): any `select` returning «a non-empty subset of its argument and at most one action for
  every state»; greedy O(2^n / n); random subsets O(2^0.78n).
- Kalyanakrishnan–Mall–Goyal, Batch-Switching Policy Iteration (IJCAI 2016): «BSPI considers the highest-indexed set in the
  partition that intersects IS(π), and switches all those states in the intersection»; O(1.6479^n). Gupta–Kalyanakrishnan (IJCAI
  2017): switch the states whose improving action is nearest in a fixed binary tree over ACTIONS; k^(0.7207n).
- Covers RF? NOT RF. These are the published «switch only a structured subset» rules; their structure is a fixed index partition
  or an action tree, independent of the policy graph, and their bounds are exponential upper bounds.

### 2.8 Orders on the current policy graph in planning; Gauss–Seidel and asynchronous policy iteration
- Dai–Hansen, «Prioritizing Bellman Backups Without a Priority Queue» (ICAPS 2007), backwards value iteration: «it considers
  states in order of backwards reachability from the goal state. To determine this ordering, it begins from the goal state, and
  performs a simple breadth-first (or depth-first) traversal of the transpose of the policy graph.» This is the one opened source
  that orders work root-first on the CURRENT policy's graph. It orders Bellman backups inside value iteration (no exact evaluation,
  no choice among improvable states, no dependency digraph); no iteration bound read. NOT RF.
- Dai–Mausam–Weld–Goldsmith, Topological Value Iteration (JAIR 2011, arXiv 1401.3910): components of the reachability graph over
  ALL actions, solved «sequentially in topological order». Whole-graph components, value iteration. NOT RF.
- Bertsekas, slides «New Exact and Approximate Policy Iteration Methods» (2011): Gauss–Seidel / asynchronous policy iteration means
  partial or inexact evaluation in a fixed or arbitrary state order («If the policy evaluations are done in Gauss-Seidel cyclic
  fashion (one state at a time), the situation is unclear»). Not a position-based choice among improvable states. NOT RF. The
  primary literature (Williams–Baird 1993, Puterman's book) was NOT OPENED.

### 2.9 RF's one-player ancestors in shortest paths: «scan only vertices with current labels»
Cherkassky–Goldberg, «Negative-cycle detection algorithms» (Math. Program. 85 (1999) 277-311, DOI 10.1007/s10107990053a; copy at
imada.sdu.dk):
- §5: «If the parent graph G_p is a tree, we say that d(v) is current if the distance from s to v in G_p is equal to d(v). If d(v)
  is not current, it must be inexact. This observation is the basis of several heuristic improvements of the Bellman–Ford–Moore
  algorithm».
- §6.7 (Tarjan's subtree disassembly): when a label improves, «all vertices of the subtree except v are removed from the current
  tree and marked as unreached. The SCAN operation does not apply to these vertices until they become labeled.» «Lemma 8. Tarjan's
  algorithm scans only vertices with current distance labels.»
- §5.3 (Goldberg–Radzik): «Apply topological sort to order A so that for every pair of vertices v and w in A such that (v, w) ∈
  G_d, v precedes w and therefore v will be scanned before w.» «Theorem 4 ([15]). The Goldberg–Radzik algorithm runs in O(nm)
  time.» §5.1 Theorem 3: Bellman–Ford–Moore's number of passes «is bounded by the depth of a shortest path tree».
- READING (the map to RF; mine): a label-correcting scan of w that makes x adopt w as parent is the switch x → w. «Do not scan a
  vertex whose tree ancestor's label is about to change» is RF's clause «no improvable u on the play from the improving target»;
  disassembling the subtree is close to RF's clause «no improvable u on the play from σ(v)». Strategy improvement recomputes every
  valuation exactly after each step, so in RF «stale» means «about to change», not «out of date».
- Covers RF? CLOSE as an idea on one-player 1-sink games (no cycle changes), NOT RF, and the bounds do NOT transfer: O(nm) there is
  inherited from the FIFO pass structure (every labeled vertex is scanned once per pass, Theorem 3), and label-correcting orders
  without it are exponential (Shier–Witzgall, T54 §3). RF has no pass structure: a non-sink improvable vertex can wait arbitrarily
  long. A polynomial bound for RF on one-player 1-sink games would have to be proved from the dependency order itself.

### 2.10 Policy iteration on deterministic Markov decision processes and one-player games
- **Howard's rule (all switches) on deterministic MDPs: OPEN, stated as open in every opened source.**
  - Lower bounds: Hansen–Zwick (ISAAC 2010; abstract only opened, paper NOT OPENED): «No polynomial time bound is known on its
    running time. … We provide the first weighted graphs on which Howard's algorithm performs Ω(n²) iterations». Asadi–Chatterjee–
    de Raaij (UAI 2025, arXiv 2506.12254, p.4): Hansen–Zwick's family «performs m − n + 1 iterations»; their Theorem 3.2 reaches
    a quadratic count with polynomial weights; «Conjecture 3.1 ([Hansen, 2012, Conjecture 6.1.1]). The number of iterations
    performed by Howard's algorithm, when applied to a DMDP, is at most the number of edges.» (Hansen's thesis NOT OPENED.)
  - Upper bounds: Post–Ye (arXiv 1208.5083 v2, p.2): «Policy iteration, for instance, is conjectured to run in O(m) iterations on
    deterministic MDPs, but the best upper bounds are exponential, although a lower bound of O(m) is known [HZ10].» Scherrer (arXiv
    1306.0386 v4, p.7): «In the simplest—deterministic—case, the complexity is still an open problem». Mukherjee–Kalyanakrishnan
    (ICAPS 2025, arXiv 2505.00795, p.2): «the best upper bound for HPI on DMDPs remains exponential»; their bounds are
    subexponential or pseudo-polynomial in the reward bit-size.
  - CLAIM (unrefereed preprint, with an AI-use statement): Zhong–Ye arXiv 2609.40147 v2, Theorem 6.1: exp(Ω(N)) iterations of
    Howard's rule on deterministic average-reward MDPs, «refutes the conjecture that Howard's policy iteration terminates within M
    iterations»; Theorem 7.2: O(N³ 2^b) for integer rewards below 2^b, by «Every N consecutive updates before termination create a
    new cycle».
  - Why simultaneous switches are the difficulty there, in Post–Ye's words (§5 p.12): «the multiple simultaneous pivots used in
    policy iteration can interfere with each other in such a way that the algorithm effectively pivots on the smallest improving
    switch rather than the largest. See [HZ10] for such an example.» This is the deterministic one-player statement of the
    interference that RF is designed against.
- **Rules other than Howard's with a polynomial bound in the one-player deterministic setting.**
  - Dantzig's single-switch rule: Post–Ye Theorem 3.7 «The simplex method converges in at most O(n³m² log² n) iterations on
    deterministic MDPs»; improved by Hansen–Kaplan–Zwick (SODA 2014, abstract only) to O(m²n² log² n).
  - Madani, «On Policy Iteration as a Newton's Method and Polynomial Policy Iteration Algorithms» (AAAI 2002; cdn.aaai.org copy):
    «Freezing Policy Iteration» (Fig. 6: «1. Freeze all vertices on a choice of edge 2. Repeat n times 3. Unfreeze a vertex. 4.
    Apply policy iteration until no improvement»); «Theorem 4.5 Policy iteration takes O(mn²) on discounted deterministic adag
    graphs. Freezing policy iteration solves discounted deterministic MDPs in O(mn³)»; «The polynomial bound for freezing policy
    iteration is independent of the order of unfreezing» (proofs deferred to a report NOT OPENED). Also p.277: Lemma 4.1 «holds in
    other variations to the policy improvement step, and in particular if the policy improvement is performed sequentially rather
    than in parallel (such as Gauss-Siedel [Ber95])», and on rolled-out acyclic graphs «by updating the vertex values and edge
    choices in an increasing order, a policy P_h is discovered in O(m) time rather than O(mn)».
  - Shortest paths (one gain, no cycle changes): Cochet-Terrasson–Gaubert (report of October 2000) «Theorem 2.3. The policy
    iteration algorithm stops at a step k ≤ n − 1» for the all-switches rule (the agent's extraction from PostScript; T65 read the
    same theorem); Scherrer Lemma 8: «If the MDP is deterministic, after at most n iterations, either Howard's PI finishes or a new
    cycle appears.»
  - Covers RF? NOT RF. Madani's freezing is the one published multi-switch rule that WITHHOLDS switches and is polynomial on
    deterministic one-player problems; it withholds by a fixed schedule of frozen vertices (any order), runs Howard on the rest,
    and needs the single-bottleneck structure of discounted deterministic problems. It is evidence that withholding can help in
    the one-player case; it is not RF and its proof does not use the policy graph.
- **One-player PARITY games under the VJ valuation.**
  - VJ00 (CAV 2000, p.213): «Proposition 5. The discrete strategy improvement algorithm terminates after O(n³) strategy improvement
    steps for one-player parity games.» (= BRICS Prop. 7.4; no proof in either version; T22: safe reading = the standard policy.)
    Same page: «We say that a strategy improvement step is substantial if in the current valuation the first component of a
    profile of some vertex strictly improves. Observe that there can be at most O(n²) substantial strategy improvement steps. It
    follows that in search for superpolynomial examples one has to manufacture gadgets allowing long sequences of non-substantial
    strategy improvement steps.» That observation holds for every subset rule, RF included.
  - Friedmann's thesis (LMU 2011): «Theorem 4.9 ([Vög00]). Let G be an one-player parity game. Policy iteration with the SWITCH-ALL
    rule requires polynomially many iterations in the worst case.» (no proof; attributed to Vöge's thesis, NOT OPENED); printed
    p.101, a remark: one-player sink parity games «can be solved in a linear number of iterations … All the algorithm performs here
    is acyclic path optimization.» Fleet proofs: RESULTS R17 (arena-optimum rule), R118 (Howard at movers).
- **Arbitrary subsets are exponential on one-player instances**: fleet CDAG_n (2^n − n − 1 single switches, T23); Friedmann–Hansen–
  Zwick arXiv 1410.7530 (Random-Facet and Random-Bland subexponential on acyclic shortest paths); BV07 §10 (§2.4).
- **Covers RF? No, and no collision with the open problem.**
  - RF is neither the standard policy nor an arena optimum, and «any subset» is false, so a bound for RF on one-player games
    (L-SI's climbs: about 3 iterations per vertex) is NEW as a statement and unproved. What is open is exactly VJ00's «long
    sequences of non-substantial steps»: the O(n²) cap on substantial steps is free; the window between two of them is bounded for
    Howard by a Bellman–Ford domination argument (Cochet-Terrasson–Gaubert; Scherrer Lemma 8; R118 PATH) that RF does not satisfy
    (a delayed vertex does not adopt the best successor).
  - RF's one-player bound would NOT settle Howard on deterministic MDPs: T65 §0 item 4 (Hansen–Zwick, Asadi et al. and Zhong–Ye
    count new cycles, i.e. gain changes; under VJ a vertex's cycle node is monotone with at most n values). Conversely nothing
    known about deterministic MDPs bounds RF. So the «warning sign» the brief asks about is absent in this direction: RF's
    one-player claim is weaker than the open problem, not equivalent to it.
  - The warning that does apply: for 25 years the one-player polynomial bound has been stated for the standard policy without a
    printed proof (VJ00, Friedmann's thesis), and the fleet's own proofs needed the domination step. An RF proof cannot cite any of
    them.

### 2.11 Class-wide lower bounds for one-sided strategy improvement
- Disser–Loho–Maat–Mosis (arXiv 2512.16684 v2): «Theorem 1.1 (Informal version) For every deterministic pivot rule that uses
  o(N / log(N)) memory states and bases decisions solely on the ordering of improving edges/variables by global index, the strategy
  improvement and the simplex algorithm take N^ω(1) iterations in the worst-case»; Theorem 1.2 (memoryless rules using index,
  reduced cost and objective improvement: Ω(2^√N) on MDPs). Setting: «we only consider a version of this algorithm that applies a
  single switch in each iteration» (§2).
- Covers RF? No: RF is multi-switch and its decision reads the play graph, which is none of the three rankings. This is the only
  class-wide lower bound for one-sided strategy improvement found; its class is disjoint from RF's by definition (B9).
- Fearnley–Savani (arXiv 1507.04500): PSPACE-completeness of predicting all-switches runs (B12): all-switches only; «devising a
  polynomial-time switching rule is an obvious direction for further study».

### 2.12 Two elementary facts about RF that the comparison with Melekopoglou–Condon suggests (READING; short arguments, unrefereed)
Their topological rule is «at most linear» on acyclic graphs and costs 2^n1 + … + 2^nk on components of sizes n_i (§2.6). RF has
the analogous properties without any preprocessing. Both arguments below are my own wording and unrefereed; neither bounds RF
on a hard instance. ACYC is also a lemma of the design lane (Lead 15:12Z: «§4.4 (Lemma ACYC)» of docs/si/box109-design.md at
claude/l-si c236bca94), which I had not seen when I wrote this; that file is the lane's statement, this is an independent check.
- **ACYC.** On a game that is acyclic apart from the sink's self-loop, RF stops within #(Even vertices with a choice) iterations.
  Argument: let v be improvable with no improvable vertex reachable from v in the GAME graph, and R the set of vertices reachable
  from v. (i) Every play from a successor of v stays in R, so v has no dependency and RF switches it. (ii) R is closed under
  successors, so the valuations on R are those of the subgame on R; σ restricted to R has no improving switch there, hence is
  optimal on R ([F] Theorem 3.3); v moves to a best successor under optimal values, so v's value is optimal and, valuations being
  monotone, v is never improvable again. (iii) In an acyclic game such a v exists whenever σ is improvable. DATA (`acyc`): 5,500
  random acyclic sink games with up to 30 vertices, bound never exceeded and attained, no settled vertex ever switched again.
  This is the general-graph form of Björklund–Vorobyov's remark on their §10 instances (§2.4): RF IS the «left-to-right» dynamic
  programming order there. Consequence for the adversaries: every hard instance for RF has its counter inside cycles of the game
  graph (all Friedmann counters do).
- **SCC-DECOMP.** Steps (i)-(ii) use only «no improvable vertex is reachable from v», so they hold in every game. More
  generally, for a successor-closed vertex set H the valuations on H, the improvable vertices of H and the plays from their
  successors and targets are determined by σ restricted to H. So RF's run on G, restricted to H, IS RF's run on the subgame H
  (followed by idle steps once H is optimal). Take the strongly connected components of the game graph in topological order from
  the sink upward, S_1, …, S_k, and H_j = S_1 ∪ … ∪ S_j. Then H_j is optimal after at most W(S_1) + … + W(S_j) iterations, where
  W(S_j) is RF's worst case on the subgame H_j over the starts that are already optimal on H_{j−1}. Melekopoglou–Condon obtain
  the same shape (2^n1 + … + 2^nk) by freezing everything above the lowest active component; RF does not freeze, but what happens
  above cannot delay what happens below. So RF's worst case lives on strongly connected games with a sink, and decomposition
  into components (which PGSolver's driver does before strategy improvement, T47 §4) neither helps nor hurts it.

## 3. Applicable lower bounds (item 2): what each counter needs, and what RF does to it
DATA below: docs/lit/T71-rf-trace.py (`count`, `flips`, `reopen`, `resets`), own reading of RF, one engine, unrefereed. «Reply
changes of gate e» = the number of iterations at which Odd's optimal reply at the gate vertex changes during the RF run (1 on
G_n: the gate closes once; every reopening adds at least 2, and the reply can also flip while a cycle is open). «Reopenings of bit
i» (`reopen`, G_n and H_n only) = the number of steps at which bit i's closed cycle stops being closed. Start: the paper's ι where
given, else the engine's best-reward start.

| family (source) | built for | the reset step, in the source's words | RF: iterations | RF: resets | verdict |
| --- | --- | --- | --- | --- | --- |
| G_n ([F] = arXiv 1106.0778 v2, Table 4, ι_{G_n}) | locally optimizing policy (switch-all / switch-best per vertex), Thm 6.14 | p.20: «Third, lower closed cycles … have an improving switch to µb (opening them again). Fourth, all lower selector nodes have an improving switch to µb. By performing all these switches, we enter phase four.» (Lemma 6.11 via Lemma 6.2 (4) and (a): h_{i<µb} ≺_σ s) | 5, 9, 12, 15, 18, 21, 24 (n = 1..7) = 3n + 3 for n ≥ 2; switch-all 9·2^n − 10 | none: every e_i changes once | **CANCELLED.** d_i depends on k_i (play d_i → e_i → h_i → k_i); RF switches k_i → g_µb first; then h_i ≻ s and the reset is no longer improving |
| H_n ([F] Table 7, ι_{H_n}; my transcription; Fact 8.1's 21n nodes, 3.5n² + 40.5n − 4 edges and top priority 24n + 6 asserted) | globally optimizing policy (Schewe), Thm 8.4 | §8.1: «the globally optimizing policy refrains from resetting the lane if the resetting event persists for only one iteration … we just alter our construction in such a way that the resetting root will have a better valuation than the default root for two iterations.» §8.3: y_i «will delay the update of g_i to move to the stubborn cycle after closing the cycle by one iteration» | 10, 37, 83, 143, 217, 305, 407, 523 (n = 1..8) = 7n² + 11n − 13 for n ≥ 2; switch-all 2^(n+1) + 1 | **survive**: bit i reopened n − i times (n = 2..7; total n(n − 1)/2); closing order 1, 2 1, 3 2 1, 4 3 2 1, …; reply changes of e_1: 3, 7, 9, 11, 13 (n = 2..6) | **NOT CANCELLED, not exponential.** For one iteration s ≻ h_i while k_i → g_µ is not yet improving; d1_i is a sink of the dependency digraph and resets. Polynomial because reopened bits re-close highest first (§4) |
| PGSolver switchallexp (Friedmann LICS 2009 family; port experiments/hard-families) | switch-all | not re-read here (T66 §5) | 10, 21, 21, 27, 30, 40, 41, 65 (N = 1..8; the Lead's row ends 65 at N = 8); switch-all 10, 30, 70, 150, 310, 630, 1243, 2486 | survive mildly: max 3, 3, 5, 3, 5 changes (N = 2..6) | not cancelled, not exponential in DATA |
| PGSolver switchbestexp (port) | switch-best (Schewe) | as H_n (generator differs from Table 7) | 17, 38, 43, 69, 74, 82, 93, 106 (N = 1..8; the Lead's row ends 106 at N = 8); switch-all 21, 61, 141, 301, 621, 1261, 2541, 5101 | survive: max 3, 5, 9, 9, 11 (N = 2..6) | as H_n |
| friedmannsubexp (PGSolver; Friedmann DAM 2013 preprint, Thm 26) | locally optimizing + snare memory | preprint p.2: «a binary counter again with cycles representing the bits, but here, every cycle looks a bit differently in each iteration» | 8, 21, 43, 50, 85, 132, 149, 189 (N = 1..8; 4.5N² + 10.5N + 5 vertices); switch-all 12, 38, 92, 202, 424 (N = 1..5) | survive: e_0 changes 3, 9, 9, 17, 25, 31, 39 times (N = 2..8); all Odd replies together 9, 36, 88, 215, 411, 622, 976 | not cancelled, not exponential in DATA (N ≤ 8) |
| fearnleysubexp (PGSolver) | Fearnley's snare rule | generator only (T47) | 8, 17, 32, 48, 64, 82, 98, 115, 132 (N = 1..9); switch-all 12, 36, 84, 180, 372, 756 (N = 1..6) | survive: e_0 changes 3, 9, 13, 15, 15, 17, 17, 17 (N = 2..9) | as above; linear in DATA |
| Zadeh (Disser–Friedmann–Hopp arXiv 1911.01074, Thm 6.18; port zadehexp) | least-entered, single switch, with tie-break | order enforced by occurrence records (two cycle centers per level, T37 §2) | 4, 7, 8, 9, 13 (N = 2..6); switch-all 4, 6, 5, 6, 5 | n/a | **does not transfer**: the count lives in the single-switch order; switch-all itself is fast on the port |
| Cunningham (Avis–Friedmann arXiv 1305.3944, Thm 4; port cunninghamexp) | round-robin, single switch | order = the fixed round-robin | 3, 4, 5, 6, 7 (N = 2..6); switch-all 4 | n/a | does not transfer |
| Bland / ranking-based (DLMM arXiv 2512.16684, Fig. 4.1; port dlmm_bland, start «first») | index-based single switch | order = global index | 1 (N = 2..9); switch-all N | n/a | does not transfer |
| Random-Facet (FHZ; port randomfacetsubexp) | randomized single switch | n/a (deterministic RF) | 4, 20, 26, 66, 78 (N = 2..6); switch-all 4, 6, 8, 10, 12 | n/a | does not transfer; note RF is SLOWER than switch-all here (66 vs 10) |
| Symmetric (vDLM arXiv 2309.02223, Thm 1) | symmetric SI, any rule | other algorithm | not run (L-COMP's counter_symsi) | n/a | B11 does not apply to a one-sided rule |
| Fearnley's MDP family (arXiv 1003.3418, Thm 17-18) | Howard on MDPs with random vertices | Propositions 13-16 (same four steps as [F], T37 §2) | no game port; not run | unknown | the G_n mechanism with random vertices; READING: its reset is of G_n's simultaneous kind |
| Fleet kill families (R130 wrapper, Γ3(G_k)) | N5 / N5′-xi | fleet-internal | Lead's rows | n/a | not literature |

READING of the table:
1. **Two kinds of reset.** In G_n the reset of bit i (d_i → s) and the update of its exit (k_i → g_µb) are improving in the SAME
   iteration; the reset is «stale» in the exact sense that it stops being improving once the exit has moved, and RF's first clause
   (no improvable vertex on the play from σ(v)) orders the exit first. In H_n the access to the new bit takes two iterations
   ((3,0) → (3,1) → (3,2) in [F] §8.3), built so that Schewe's one-step lookahead also resets. During the first of the two, the
   exit k_i has no improving switch yet, so nothing on d1_i's plays is improvable and RF resets. H_2, my trace: iteration 15 closes
   cycle 2; 16: s → f_2, y_2 → f_2; 17: d1_1 → s (bit 1 reset) together with g_2 → y_2; 18: k_1 → g_2.
2. **RF's blind spot, stated once.** RF tests the vertices that are improvable NOW on two plays. It does not see a vertex ON the
   play that becomes improvable only after a vertex OFF the play switches in the same iteration (k_i after g_µ). Any counter with a
   one-iteration delay node between «bit µ pays» and «the exits of lower bits can see it» defeats the cancellation. This is not a
   new construction: it is [F] §8.1 / §8.3, published in 2011 against Schewe's rule.
3. **Why RF is still polynomial on H_n (DATA; READING).** After bit µ closes and the bits below it reset, the reopened bits
   re-close HIGHEST first. The cause is the selector chain, not the lane:
   - The lane alone would still order the closings lowest-first under RF. On G_n it does (cycles close in the order 1, 2, …, n,
     at iterations 3, 6, 9, … of the G_3 trace): a cycle node waits only for the improvable lane vertices t_j that lie on the
     plays of its own improving targets a_j, and lower bits have fewer of them.
   - On H_3 after the double reset at iteration 49 the delayed vertices and their blockers are, at iterations 51-58 (trace):
     d2_1 [d1_2, d3_1, g2], d3_1 [d1_2, g2, k1], k1 [d1_2, g2, y2], g2 [d1_2, y2], y2 [d1_2], d1_2 [lane vertices t_j].
     Bit 1's cycle nodes d2_1, d3_1 still point into their cycle, and their play runs e_1 → h_1 → k_1 → g_2 → y_2 → f_2 → e_2 →
     d1_2: through the exit selector k_1 into the reopened gate of bit 2, whose nodes are waiting for the lane. (d1_1, whose play
     does not run through k_1, moves early: iteration 52, d1_1 → a3.) So bit 2 settles first (closes at iteration 62, together
     with k_1 → g_3), then bit 1 (66), and bit 1 is still open when bit 2 closes: no reset of a set bit, no cascade.
   - DATA (`reopen hn 2 7`): bit i is reopened exactly n − i times, n(n − 1)/2 reopenings in all, and the cycles close in the
     order 1, 2 1, 3 2 1, …, n (n − 1) … 1. Quadratic, not exponential.
4. **The single-switch families carry no information about RF.** Their counters are driven by which ONE improving edge the rule
   picks; a multi-switch rule does not follow that order, and switch-all itself needs 4-12 iterations on the ports.
5. **RF is not dominated by switch-all.** randomfacetsubexp N = 5: RF 66, switch-all 10; zadehexp N = 6: 13 vs 5. Delay costs
   iterations; any proof that compares RF with Howard step by step is wrong in that direction.

## 4. Where to dig (for L-RED / L-RED-B; READING, no construction attempted here)
A binary counter of n bits needs, at every increment: the least unset bit µ sets; every lower bit resets; and afterwards the lower
bits set again LOWEST FIRST, so that setting bit 2 finds bit 1 set and resets it. Under RF:
- (a) Reset: available as published. Keep [F] §8.3's delay node y_µ between the access node g_µ and f_µ. RF then resets d1_i for
  every closed i < µ in the iteration after s → f_µ (DATA, H_n). Nothing new is needed for this half.
- (b) Lowest-first re-closing: this is what RF breaks in H_n, and the DATA names the channel (§3 reading 3). (b1) Lane channel:
  an open cycle's node waits for the improvable lane vertices on the plays of its improving targets. This costs iterations but
  keeps the order (G_n closes 1, 2, …, n under RF). (b2) Selector channel: after a reset the exit selector k_i still points to
  g_{i+1}, so the play of bit i's in-cycle nodes runs into bit i + 1's reopened gate, and RF makes bit i wait until bit i + 1 has
  settled. (b2) is what inverts the order. Friedmann's layout has the selector chain ascending by construction (the root's path
  lists the set bits in ascending order, [F] Lemma 6.11-6.12, T37 §2).
- What an RF-specific counter would need (READING; untested, no construction attempted):
  - cut (b2): after a reset, the plays from bit i's in-cycle nodes (through e_i, h_i, k_i) must not pass through any vertex of a
    reopened higher bit that has a pending switch. Either the exit must already bypass the reopened gates when the reset happens,
    or the reopened gate's access nodes (g, y) must settle at once instead of waiting for their cycle node. The monotonicity of
    valuations ([F] Theorem 3.2) constrains every such change: a reset must come with a strict gain elsewhere;
  - keep (b1) honest: a delay supply made of vertices that are NOT improvable while they delay (RF cannot depend on a vertex that
    has no improving switch yet), e.g. chains of [F] §8.3-type delay nodes whose length grows with the bit index.
- A cheap diagnostic for any candidate family: `python3 -I docs/lit/T71-rf-trace.py flips FAMILY NMIN NMAX`. Reply changes per
  gate growing faster than linearly in N is the first sign of a cascade; on every published family it is linear so far.
- The one-player side: L-SI's «about 3 iterations per vertex» has no proof and no published analogue (§2.9, §2.10). A one-player
  superpolynomial run of RF would kill it outright; a proof must replace Howard's domination step (§2.10).

## 5. What I did not do
- I did not run Schewe's rule on H_n (the 2^n there is [F] Theorem 8.4, PROVED-in-source; my switch-all column is Howard, not
  Schewe). I did not diff PGSolver's switchbestexp generator against [F] Table 7.
- I did not re-derive why switchallexp's resets survive mildly (LICS 2009 construction, not re-read).
- Not opened: Hansen's thesis (Aarhus 2012; 404), Hoffmann–Luttenberger ATVA 2013 (paywall; Hoffmann's bachelor thesis opened
  instead), Melekopoglou–Condon's stochastic-games report TR-90-941, Bonet–Geffner HDP, Williams–Baird 1993, Madani's report
  with the freezing proofs, Hansen–Zwick ISAAC 2010 (paper; abstract only), Hansen–Kaplan–Zwick SODA 2014 (abstract only), Vöge's
  thesis (403), the ORSA journal PDF of MC94 (author copy used), DAM 2013 published version (preprint used), Tarjan's 1981 report
  and Goldberg–Radzik 1993 (both through Cherkassky–Goldberg 1999).

## 6. Sources opened for T71 (sha256 prefix of the PDF; downloads in the session scratchpad, lost with the container)
- Friedmann arXiv 1106.0778 v2 = LMCS 7(3:19) 2011 (46c96f44775aa2b0): §3 p.5-6; §4 p.6-7 (Lemma 4.3, Theorem 4.2, p.7
  «intransitivity»); §6.1 Lemma 6.1, 6.2; Table 4; phases p.18-22, Lemma 6.11; §8.1-8.5, Tables 6-7, Lemma 8.1-8.3, Theorem 8.4.
- Fearnley arXiv 1003.2976 v1 (7ac44213b8d8d633): p.1-2; Definitions 10, 11, 13; Proposition 12; Algorithm 1; §8; §9 p.14.
- Friedmann, snare preprint of 13 Feb 2013, oliverfriedmann.com/downloads/papers/fearnley_lower_bound.pdf (8ea13895373a8e9a):
  abstract, p.1-2, Theorem 11 p.9, Theorem 26 p.25.
- Schewe CSL 2008 author copy, finkbeiner.groups.cispa.de/_assets/paper.DJvJAbZR.pdf (cf86d13b3e90fedf): abstract, §1, Fig. 2,
  Theorems 3-5.
- Luttenberger arXiv 0806.2923 v4 (5423346ce997c8ac): abstract, §4 Theorem 4.16, Theorem 5.4.
- Björklund–Vorobyov, DAM 155 (2007), dbai.tuwien.ac.at/staff/vorobyov/dam-2007-mpg-subexp.pdf (95a6b406f01db6b4): abstract, §1,
  §4 p.216-217, §10 p.226, §12 p.227.
- van Dijk–Loho–Maat arXiv 2309.02223 v1 (10e6794d82aba465): Theorem 1 p.2, Theorem 13. Schewe–Trivedi–Varghese arXiv 1501.06484
  (7b68cc69de78bd90): not re-read (T70 Add. A).
- Disser–Loho–Maat–Mosis arXiv 2512.16684 v2 (fa9b42e397e3e434): Theorems 1.1, 1.2 p.2-3; §2 p.7.
- Disser–Friedmann–Hopp arXiv 1911.01074 (ba3242140c0832ac), Avis–Friedmann arXiv 1305.3944 (d1fafb8b5d0b822c), Disser–Mosis
  arXiv 2309.14034 (ab2be221cef25ce6), Fearnley arXiv 1003.3418 (0964f029581ae02e): downloaded, identified by their first lines;
  cited through T37's readings, not re-read today.
- Cherkassky–Goldberg, Math. Program. 85 (1999), imada.sdu.dk/u/jbj/DM817/Negativicyclefinding.pdf (952ee3ba8982a3e1): §5 p.284-286
  (Theorems 3, 4), §6.7 p.290 (Lemma 8).
- Through the literature agent's downloads, quotes re-read by me at the cited places: Melekopoglou–Condon author copy,
  cs.ubc.ca/~condon/papers/9edc2ce55b2d7f5d45cc014a0d2733ed3051.pdf (0a56c141dfbdaf81): §2 p.3-4, Theorem 2.8, Corollary 2.9;
  Dai–Hansen ICAPS 2007, cdn.aaai.org/ICAPS/2007/ICAPS07-015.pdf (8a825dea0de4bffd); Christ–Yannakakis arXiv 2212.00083 v1
  (ab6b525118aadbb3): Theorem 6; VJ00 BRICS RS-00-48 (485a12de432a2a8c): Prop. 7.1, 7.4; BSPI, ijcai.org/Proceedings/16/Papers/
  446.pdf (b9d714b664a005f1).
- Through the second literature agent's downloads, quotes re-read by me at the cited places: Post–Ye arXiv 1208.5083 v2
  (c51876ebf5c3cdb0): p.2, Theorem 3.7, §5 p.12; Scherrer arXiv 1306.0386 v4 (391b6481c8fa903f): Lemma 8 p.6, p.7; Asadi–
  Chatterjee–de Raaij arXiv 2506.12254 (78c4ee071961b89e): p.4; Mukherjee–Kalyanakrishnan arXiv 2505.00795 (7b856cc9010c6c06):
  p.2, App. A; Madani AAAI 2002, cdn.aaai.org/AAAI/2002/AAAI02-042.pdf (2bd187261196bdba): Fig. 6, Theorems 4.4, 4.5, p.277;
  VJ00 CAV 2000 Springer PDF (8e456b741b5b66cc): Propositions 4, 5, p.213; Zhong–Ye arXiv 2609.40147 v2 (dafeb81816af6582):
  Theorems 6.1, 7.2 (headline lines only). Hansen–Zwick ISAAC 2010 and Hansen–Kaplan–Zwick SODA 2014: abstracts only.
- Through the agents only (their quotes, not re-read by me; treat as SECOND-HAND until re-opened): Cochet-Terrasson–Gaubert's
  report (PostScript, hand extraction by the agent; T65 read it earlier), Friedmann thesis Theorem 4.9 and
  §4.2-4.3 (68748f5388a94151; T22 / T23 read the same PDF earlier), Mansour–Singh arXiv 1301.6718 (47e2bb55482e4b33), Gupta–
  Kalyanakrishnan IJCAI 2017 (ec15f9db66664b32), Goenka et al. arXiv 2211.15602 v2 (e62fb2eceb298d98), Dai et al. arXiv 1401.3910
  (5a4b318e745a0341), Bertsekas slides (f12773197992b525), Fearnley thesis, Canavoi–Grädel–Rabinovich arXiv 1210.2459, Fearnley
  arXiv 1705.02313, Fearnley–Savani arXiv 1507.04500, Friedmann–Lange arXiv 1006.1409, van Dijk arXiv 1801.03859, Björklund–
  Sandberg–Vorobyov PSI 2003, Puri's thesis, Hoffmann's bachelor thesis, Koh–Loho arXiv 2108.13338, Maat arXiv 2509.16075, Auger
  et al. arXiv 2102.04922 and 1402.0471, Kalyanakrishnan–Misra–Gopalan AAAI 2016, Grześ–Hoey IJCNN 2013.

## DONE / FINDINGS / NEEDS
- DONE: this note; docs/lit/T71-rf-trace.py; about 50 sources opened (15 by me, the rest by the agent).
- FINDINGS:
  1. RF not found in the opened literature. Nearest: Melekopoglou–Condon topological improvement (whole-graph components,
     single-switch, exponential), Schewe's optimal improvement (exponential, [F] Thm 8.4), Fearnley's strategy trees
     (superpolynomial, Friedmann 2013), Tarjan / Goldberg–Radzik in shortest paths (O(nm) from FIFO passes, not from the order).
  2. RF cancels the reset of exactly one published counter (G_n). H_n's two-iteration reset survives RF (DATA); RF is quadratic
     there because reopened bits re-close highest first.
  3. The adversaries' target is lowest-first re-closing under RF; the reset half is already published.
  4. RF's one-player bound is not covered by any opened source and does not imply the Howard / deterministic-MDP open problem.
- NEEDS: Lead: route §3 reading 2-3 and §4 to L-RED / L-RED-B; decide whether a second search pass (Hansen's thesis, ATVA 2013)
  is wanted before any novelty wording is used. Owner: nothing.
