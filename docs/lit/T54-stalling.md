# T54: network-simplex stalling, fixed-gain policy iteration, label-correcting orders, and what SPEC S1's tie-break does on a W-tight subgame G_I, against [P-INT] and BIP-POLY
L-LIT successor T54 (Opus 5.5), D18. Lead's brief 2026-10-30 ~14:08Z (T54 (a)-(c), routed from L-SI 33 box 51b, l-si f2765662,
docs/si/N5-GATE-box51b.md) and the 14:34Z addendum (d) (L-NEW 38 box 88, l-new e975c729, docs/new/N5-ONEP-box88.md). Written 2026-10-30
14:10Z-15:00Z (date -u). Working note, unrefereed, not a TARGET.md claim. G-N5-TIME, [P-INT], INT-LIN and BIP-POLY stay OPEN.
Labels: PROVED-in-source (opened) / SECONDARY (seen only through another opened text, named) / PROVED (L-LIT, elementary, unrefereed) /
READING / DATA / OPEN. "Opened" = full text downloaded and the cited page read; sha256 prefixes here, scratchpad paths in notes/L-LIT.md.
Symbols as in box 51b: a W-run F (τ fixed), a W-constant interval I, G_I := G_W (Even restricted to OPT_W, Odd keeps all edges),
INTERVAL-SI (inside I, N5 is VJ strategy improvement on G_I and S4a's choice is a pure tie-break of SPEC S1's procedure).

## Summary
- (a) Network simplex. Strongly feasible trees make the method FINITE for every entering rule, through a monotone potential. They do not
  make degenerate runs polynomial. Cunningham 1979 shows exponentially long runs of consecutive degenerate pivots ("stalling") under
  Bland's rule, even on shortest-path problems (SECONDARY, Orlin CWI 1985 p. 6). All polynomial bounds on consecutive degenerate pivots
  that I could open use an extra ingredient that N5's S1 tie-break lacks: a history (cyclic) entering rule, an alternating dual tree
  (Muramatsu 2000, Lemma 5: < 2n), an oracle improving direction (Kukharenko-Sanità, Thm 1: ≤ n − m − 1) or monotone distance labels
  (Goldfarb-Hao, max flow only). Without that ingredient the count is pseudo-polynomial (O(n²C)-type, integer costs).
- (b) Fixed-gain / bias-only phases. Polynomial bounds exist only for specific rules: Dantzig single switch (Zhong-Ye 2026 eq. (7.6),
  preprint; Post-Ye Lemma 3.4) or Howard switch-all (Scherrer Lemma 8), and only for ONE player. For arbitrary improving rules the best
  opened bound is exponential (Goenka et al. Cor. 1), and lower bounds hold with a single fixed sink (FHZ 1410.7530; Björklund-Vorobyov
  §10; Friedmann's 1-sink games, two players).
- (§4, new, the main finding for [P-INT]) Inside I, S1's tie-break splits by the parity of the W-cycle node c = λ_W(v):
  - ODD branch (Ω(c) odd). The choice is the SMALLEST-INDEX tight arena edge, so index(σ(v)) never rises inside I. This gives ≤ m − n
    transitions with an ODD-branch switch per interval (Lemma IDX-MONO, PROVED modulo Claim RG). DATA: 0 such switches in the corpus.
  - EVEN branch (Ω(c) even). The choice is a LEXICOGRAPHIC BFS tree (Lemma LEX-BFS, PROVED modulo Claim RG). DATA: 168/168 switches in
    the corpus. Its keys fall monotonically (LEX-MONO), the analogue of the strongly-feasible-tree potential.
  - In the abstract model where an adversary picks the arenas, the lex-BFS choice STALLS EXPONENTIALLY: longest runs 2, 8, 22, 52, 114 =
    2^(L+1) − 2L − 2 at n = 2L + 1 (DATA, exhaustive, L ≤ 6). This is Cunningham's picture: no cycling, but stalling.
  - So [P-INT] ⇐ CN-POLY ∧ EVEN-POLY, and EVEN-POLY must use WHICH edges S2 offers (Ξ-improvement). Monotonicity of the keys is not enough.
- (d) Label-correcting. Exponential orders: LIFO and the Pape deque with nonnegative arcs of length ~2^n (Shier-Witzgall 1981 Results 5,
  6), and Dijkstra's order with negative arcs (Result 7; Johnson 1973 SECONDARY). Polynomial orders: FIFO, O(n³) arc examinations (Result
  8), and pass-based Bellman-Ford with ANY order inside a pass, O(nm). Generic arbitrary order: pseudo-polynomial O(n²C) for integer data.
- Cross-cutting (READING). Parity valuations order path sets by Σ ±2^rank. That is exactly the exponential-weight regime of the classical
  stalling and label-correcting examples. So every pseudo-polynomial bound above (O(n²C), Cunningham + integers, Björklund-Vorobyov
  O(n²|E|W)) gives only 2^O(n) for N5. A polynomial bound must be combinatorial in the sense of §1.6-§1.7, Muramatsu or Kukharenko-Sanità.

## 1. (a) Network-simplex stalling and anti-stalling
Notation of those papers: a spanning-tree basis T; node potentials π; reduced costs; a pivot is DEGENERATE if the flow (primal value)
does not change. L-SI's reading maps W ↔ the primal objective (frozen inside I) and Ξ ↔ the potentials (they move, strictly, at
switched vertices). I checked this against the definitions below: the mapping is consistent. The entering edges are Ξ-improving (non-zero
"reduced cost" w.r.t. Ξ) and W-tight (the objective does not move), exactly as for a degenerate pivot. (READING)

### 1.1 Cunningham 1976, "A network simplex method", Math. Prog. 11:105-116, doi 10.1007/BF01580379: NOT OPENED (closed access)
- SECONDARY, definition (Muramatsu 2000, Def. 3, p. 154, opened): «A primal feasible spanning tree is called strongly feasible if there is
  a node t such that any arc of the spanning tree whose flow is zero has the direction towards t.» Leaving rule (p. 154): «The leaving
  arc is the last blocking arc encountered in traversing the cycle W along its orientation starting from [the apex]» (keeps strong
  feasibility; Muramatsu's Lemma 4, citing AMO p. 421).
- SECONDARY, mechanism (Holzhauser-Krumke-Thielen arXiv 1607.02284 pp. 9-10, opened, following AMO pp. 424-425): in a degenerate pivot
  only the potentials of the cut-off subtree change, all in the same direction, so Σπ strictly decreases. No tree repeats, whatever the
  entering rule. The count «π_v are integers in {−nC, …, nC}» gives a PSEUDO-polynomial bound (integer costs).
- (c) N5 on G_I: the finiteness part holds with no new lemma: Ξ strictly rises (R15 (c), (d)), and the lex keys of §4 also fall
  (LEX-MONO). The counting part needs integer potentials of size C. The N5 analogue of C is 2^n (path-set weights). (d) For [P-INT]:
  2^O(n), useless.

### 1.2 Cunningham 1979, "Theoretical properties of the network simplex method", Math. Oper. Res. 4(2):196-208, doi 10.1287/moor.4.2.196: NOT OPENED (INFORMS 403)
- SECONDARY, stalling (Orlin, CWI Report OS-R8504, 1985, p. 6, opened, sha256 7013d22e…): «Cunningham (1979) showed that Bland's primal
  simplex pivot rule takes an exponentially long sequence of consecutive degenerate pivots in the worst case. Indeed, Cunningham's example
  (a modification of an example of Edmonds (1970)) shows that Bland's rule takes an exponentially large number of pivots in the worst case
  even when specialized to the shortest path problem.»
- SECONDARY, anti-stalling (same page): Cunningham «also provided some "good news" … by developing a primal network simplex pivot rule
  that avoids "stalling", i.e., the number of consecutive degenerate pivots is polynomially bounded.» The rule is the least recently
  considered (round-robin) entering rule (Avis-Friedmann, opened, pp. 1-2). The exact bound (search snippets say nm, or m² under LRS) is
  UNCONFIRMED.
- Hypotheses: (H1) a strongly feasible tree with the last-blocking-arc leaving rule; (H2) ONE entering arc per pivot; (H3) a fixed cyclic
  order on the arcs (or nodes) and a memory of the last entering arc (history-based).
- (c) N5 on G_I: (H1) has an analogue (the lex keys of §4, READING). (H2) fails: S4a switches a set. (H3) fails: S1 has no memory, and
  its EVEN-branch order is lexicographic in the current tree, not cyclic. Missing: a history rule. That would be a CHANGE of N5, as is
  R93's N5-LZC, which already has FL = 0. (d) For plain N5: no bound. Cunningham's stalling result is the warning: a strongly feasible
  (lexicographic) structure plus a non-history rule can stall exponentially, and §4.4 reproduces this for S1's EVEN branch in the
  abstract model.

### 1.3 Avis-Friedmann, "An exponential lower bound for Cunningham's rule", arXiv 1305.3944v1 (Math. Prog. 161, 2017): OPENED (sha256 d1fafb8b…)
- PROVED-in-source, Theorem 4 (p. 10): on the parity games G_n of size O(n), the round-robin (least recently considered) improvement rule
  with ordering (1) makes at least 2^n switches. Theorem 7 (p. 30): on LP_n «the pivot path … has length at least 2^n. The objective
  function strictly increases with each pivot.» Theorem 3 (p. 11): from any σ_0 there are ≤ n distinct improving switches leading to an
  optimal strategy, «Since all switches are different in the sequence … there is always a way to select an ordering that results in a
  linear number of pivoting steps». Open problem (p. 31): «extend our results to network LPs».
- (c) The anti-stalling rule bounds only CONSECUTIVE DEGENERATE pivots. Its total count is exponential even on parity games, and the
  pivots there are non-degenerate. Theorem 3 applies to G_I verbatim (G_I is a parity game). So inside I a run of ≤ n − 1 single
  improving switches (Ξ-improving, all W-tight) always EXISTS. [P-INT] is purely about S1's choice among them. (d) Existence of a short
  run only.

### 1.4 Muramatsu, J. Oper. Res. Soc. Japan 43(1) (2000) 149-161 (network simplex with the primal-dual symmetric pivot rule; orsj.org Vol.43_01_149.pdf): OPENED (sha256 c0d592ed…, pp. 153-155)
- PROVED-in-source, Lemma 5 (p. 154): «There are no 2n consecutive degenerate primal pivots.» Hypotheses: the Chen-Pardalos-Saunders
  primal-dual symmetric pivot rule (primal and dual pivots alternate), a strongly feasible primal tree, the last-blocking-arc leaving
  rule. Mechanism (p. 155): the cut (U, V) of the dual tree is fixed during the degenerate run. Each degenerate primal pivot keeps the root
  t on its side and lowers |U| by ≥ 1, so there are fewer than n − 1 per case. Combinatorial. Total (Theorem 6): ≤ 2n²·max b_i primal
  pivots, pseudo-polynomial.
- (c) N5 inside a W-run has no dual pivots: τ is FIXED (that is the definition of a W-run). The nearest analogue of the dual tree is σ̄
  / the deviation set D_k = {o : σ̄_k(o) ≠ τ(o)}. L-SI box 51b §3 shows D, the gate map and λ_Ξ CONSTANT over all 8 flat transitions of
  u23sw64_n32. So the obvious analogue of the shrinking cut does not move. Missing lemma: a set that shrinks at every flat transition.
  (d) None.

### 1.5 Kukharenko-Sanità, arXiv 2311.15799v4: OPENED (sha256 ed8b82ac…, pp. 1-7)
- PROVED-in-source, Theorem 1 (p. 3): for min{cᵀx : Ax = b, x ≥ 0}, A ∈ ℝ^{m×n}, «there exists a pivot rule that limits the number of
  consecutive degenerate simplex pivots at any non-optimal extreme solution to at most n − m − 1.» Hypothesis: an improving feasible
  DIRECTION at the current vertex is given, and the rule is built from it. Each degenerate pivot shrinks that direction's support outside
  the basis, or lowers its dimension. Combinatorial. It extends Kabadi-Punnen (≤ m in the totally unimodular case; SECONDARY via p. 2).
- (c) N5's S1 has no direction oracle. The analogue would be "steer the tie-break toward a fixed Ξ-better strategy of G_I", as in
  Avis-Friedmann Thm 3. (d) Existence only (an oracle rule with |I| ≤ n − 1 exists); nothing for S1.

### 1.6 Tarjan, "Efficiency of the primal network simplex algorithm for the minimum-cost circulation problem", MOR 16 (1991) 272-291: OPENED as Princeton CS-TR-187-88 (sha256 e77c6f6c…, scanned, pp. 1-18)
- PROVED-in-source: the rule blocks a minimum-mean pseudo-residual cycle Γ, pivoting only on arcs of Γ (§4, p. 11). Lemma 4.3 (p. 12):
  «A sequence of m/2 − 2n + 2 ≤ m cycle blockings reduces ε*(f) to at most (1 − 1/n)ε.» Theorem 4.6 (p. 14): «For arbitrary real-valued
  arc costs, the cycle blocking algorithm terminates after O(nm² log n) cycle blockings.» Theorem 4.10 (p. 18): «The cycle-blocking
  algorithm blocks Γ in at most n^{(log n)/2} pivots.» Degenerate pivots are included in the count.
- Mechanism of 4.10: a signature α_i = |Γ_i − T_i| over condensed graphs falls lexicographically (Lemma 4.8), with α_i ≤ n/2^(i−1)
  (Lemma 4.9). A lexicographic potential of length O(log n) gives n^O(log n).
- (c) The lesson for §4: S1's EVEN-branch lex keys have length up to n with entries up to n. Tarjan's counting needs geometrically
  shrinking entries, and no such shrinkage is known for the keys (OPEN). (d) None.
- Tarjan, "Dynamic trees as search trees via Euler tours…", Math. Prog. 78 (1997) 169-177: NOT OPENED (closed). Its subject is
  per-pivot running time (SECONDARY, citation contexts).

### 1.7 Goldfarb-Hao, "A primal simplex algorithm that solves the maximum flow problem in at most nm pivots …", Math. Prog. 47 (1990) 353-365: NOT OPENED (closed)
- SECONDARY (Goldberg-Grigoriadis-Tarjan, Princeton CS-TR-193-88, p. 4-5, opened, sha256 da51e931…): «Goldfarb and Hao proposed a pivot
  rule such that at most nm pivots occur»: the smallest-label rule, d(v) = fewest pseudoresidual arcs from s; «vertex labels can never
  decrease … once a pseudoresidual arc (v,w) becomes a saturated nontree arc, it cannot become pseudoresidual again until at least one of
  d(v) and d(w) increases». Labels stay < n. Combinatorial; max flow only. GGT p. 4: with only an anti-cycling rule such as Cunningham's,
  «at most n²U pivots» (pseudo-polynomial).
- (c) This is the closest pattern to a usable lemma: bounded integer labels that never decrease, plus an edge that can be re-used only
  after a label rises. The N5 analogue inside I would be an "arc re-entry" lemma: an Even edge left inside I re-enters only after some
  bounded label rises. LEX-MONO gives falling keys, but they are unbounded in number (§4.4). (d) None yet. This is the lemma shape to look
  for (§5).
- NOT OPENED (closed or 403/429): Goldfarb-Hao-Kai, Networks 20 (1990) 79-91 (anti-stalling rules; SECONDARY via Kukharenko-Sanità p. 2:
  bounds «introduced in [Cunningham 1979] and further developed in [AOSS 2002, GHK, Roohy-Laleh 1981]», no bound quoted); Goldfarb-Hao,
  Algorithmica 8 (1992); Orlin 1985, MP Study 24 (snippet: O(|V|²|E| log|V|) consecutive degenerate pivots, unverified); Orlin 1997, MP 78
  (DSpace 1721.1/2584 answered 429 six times); Ahuja-Orlin-Sharma-Sokkalingam, ORL 30 (2002) («O(n) consecutive degenerate pivots»,
  title only); AMO ch. 11.

## 2. (b) Strategy improvement / policy iteration while the gain or cycle is fixed
### 2.1 Zhong-Ye, "Policy iteration is not strongly polynomial for deterministic MDPs: the price of algorithmic anarchy", arXiv 2609.40147v2 (13 Oct 2026, preprint): OPENED (sha256 dafeb818…, §5 pp. 22-23, §7.1 pp. 31-33)
- PROVED-in-source (preprint): one player, deterministic, average reward. Rule (5.3) (Dantzig: ONE state-action pair maximising (J(f(s,a))
  − J(s), Q(s,a) − V(s)) lexicographically). Eq. (7.6), p. 32: «#{consecutive bias updates with unchanged cycles} = O(N²M log(2N)).»
  p. 31: «For a bias update that creates no cycle … J^{πt+1}(s) = J^{πt}(s) for every s», and bias updates continue «until a new cycle is
  created or the algorithm terminates». Theorem 7.1: O(N³M² log²(2N)) in all. Theorem 6.1 (p. 23): Howard (5.2) needs exp(Ω(N)) iterations
  «before any state attains its optimal gain» (a gain-phase lower bound).
- Mechanism: Σ_s(V^{πT} − V^{πt}) ≤ N²·(max residual) (needs Dantzig), so it contracts by (1 − 1/N²) per step. After 2N² log N steps an
  action is eliminated for good (Post-Ye). Numeric, but strongly polynomial.
- (c) G_I is TWO-player (Odd keeps all edges). S4a switches a set. S1's choice is not the max residual (L-SI box 51b §3: XNGRD 46, LAZY 64).
  So the hypotheses fail three times over. In the one-player case (Ξ = W) box 88's NO-DEV already gives FL = 0. (d) None for N5. It
  confirms that the bias-only phase is polynomial for a residual-greedy rule.

### 2.2 Post-Ye, arXiv 1208.5083 (Math. Oper. Res. 2015): OPENED (sha256 c51876eb…, pp. 4-9)
- PROVED-in-source: discounted DMDP, single switch, highest gain. Lemma 3.4 (p. 8): «Either the algorithm finishes or a new cycle is
  created after O(n²m log n) iterations.» Theorem 3.7: O(n³m² log²n). (c), (d): as 2.1, discounted.

### 2.3 Scherrer, arXiv 1306.0386v4: OPENED (sha256 391b6481…, pp. 6, 17)
- PROVED-in-source, Lemma 8: «If the MDP is deterministic, after at most n iterations, either Howard's PI finishes or a new cycle
  appears.» Discounted, Howard (switch-all to the best action). Mechanism: depth n (the Bellman-Ford analogue).
- (c) Needs switch-all-best. S1 is neither greedy nor switch-all (box 51b §3 DEAD: the Bellman-Ford route in G_I). (d) None.
  (Agent inference, NOT checked: the same argument gives ≤ n Howard bias iterations per gain-fixed phase in average reward.)

### 2.4 Goenka-Gupta-Khyalia-Agarwal-Wajid-Kalyanakrishnan, arXiv 2211.15602v2 (Math. Oper. Res.): OPENED (sha256 e62fb2ec…, pp. 5-7, 19-22)
- PROVED-in-source, Corollary 1 (p. 21): «Any run of a PI algorithm with arbitrary action selection on an n-state, k-action DMDP terminates
  in at most 5n³k²α(k)^(n−1) = O(n³kα(k)^n) steps.» Discounted; combinatorial (each new policy has a new path-cycle). p. 6 (SECONDARY):
  Ashutosh et al. build a DMDP whose PI-DAG has a path of length Ω(k^(n/2)).
- (c) "Arbitrary improving subset" is the only hypothesis S1 meets for free, and the bound is exponential. (d) 2^O(n log k).

### 2.5 Friedmann-Hansen-Zwick, arXiv 1410.7530: OPENED (sha256 c337feb6…)
- PROVED-in-source, Theorems 6.3, 8.1: Random-Facet and Random-Bland need e^Ω(√n) expected switches on acyclic shortest-path instances
  with nonnegative weights (one target). p. 2: Random-Edge is polynomial on shortest paths («not difficult to show», no proof there).
- (c) A single fixed sink, one player, is not enough for polynomial bounds under general improving rules. (d) None.

### 2.6 Friedmann, "An exponential lower bound for the latest deterministic strategy iteration algorithms", LMCS 7(3:19) 2011, arXiv 1106.0778: OPENED (sha256 46c96f44…, pp. 8-9, 23, 33)
- PROVED-in-source: the lower-bound games are 1-sink games. (2) «Sink Seeking: for each player 0 strategy σ … the cycle component of
  Ξ_σ(w) equals v*.» p. 8: «the strategy iteration algorithm is just improving the paths leading to the cycle node.» Theorem 6.14:
  switch-all needs ≥ 2^n improvements; Theorem 8.4: the same for the globally optimal rule.
- (c) A fixed cycle node with two players is still exponential. These games are NOT W-tight subgames: against a fixed τ, different Even
  strategies have different values. Whether some long SI run can be embedded as one G_I is L-SI's kill target (box 51b §5, R1-R3).
  Literature gives no answer either way. (d) None.

### 2.7 Björklund-Vorobyov, "A combinatorial strongly subexponential strategy improvement algorithm for mean payoff games", DAM 155 (2007) 210-229: OPENED (author PDF, sha256 95a6b406…, pp. 213-215, 218-226)
- PROVED-in-source: longest-shortest paths (MAX chooses edges, MIN replies with shortest paths to a fixed sink). Theorem 5.1: any
  attractive switch gives an admissible, better strategy. §8: «any combination of attractive switches improves the strategy value.»
  Theorem 7.1: min(O(n²|E|W), 2^O(√(n log n))). §10 (p. 226): with «the rightmost attractive single switch, it visits all 2^n possible
  strategies of MAX» on acyclic instances, and «we are unaware of any LSP instances that require superpolynomially many steps of the
  single random, multiple random, or all profitable … algorithms.»
- (c) This is the closest model to G_I: two players, fixed sink, only the potential part improves. A STATIC-ORDER single-switch rule is
  exponential there. S1's ODD branch is static-order too, but it is applied among W-TIGHT arena edges that include σ(v). That is why it
  is monotone per vertex (§4.2) while "rightmost attractive" is not. (d) Pseudo-polynomial O(n²|E|W) only; W ~ 2^n for parity.
- Also opened, not needed: Asadi-Chatterjee-de Raaij arXiv 2506.12254 (Howard on mean-payoff DMDP, gain phase); Disser-Mosis (stochastic
  MDPs). NOT OPENED: Hansen-Kaplan-Zwick SODA 2014 (SIAM 403), Hansen-Zwick ISAAC 2010 (429), Madani-Thorup-Zwick TALG 2010 (403),
  Veinott 1969 (bot wall), Puterman.
- OPEN in the literature as far as opened: no bound on bias-only phases for arbitrary or index-type rules in two-player games, and none
  for a player who is INDIFFERENT against a fixed opponent strategy (the W-tightness of G_I).

## 3. (d) Label-correcting shortest paths: which orders are exponential, which polynomial
### 3.1 Shier-Witzgall, "Properties of labeling methods for determining shortest path trees", J. Res. NBS 86(3) (1981) 317-330, doi 10.6028/jres.086.013: OPENED (nvlpubs.nist.gov, sha256 d6f521ad…, pp. 317-318, 326-329)
- Setting: one root; a sequence list; branching out from a node scans its forward star; no negative closed paths. Effort = «the number
  of arcs examined (i.e., used in branching out)» (p. 326).
- PROVED-in-source, Result 5 (p. 326): «Under LIFO/MOVE or LIFO/NO MOVE sequence disciplines, a labeling method has exponential
  computational complexity.» On the networks V_n (2n + 1 nodes, 3n arcs): E(n + 1) = 3 + 2E(n), «E(n) = 3(2^n − 1)». Arc lengths are
  NONNEGATIVE integers growing by a factor F = 2 per segment (V_n = G_n with a = 1, b = 0, c = 2, F = 2; Lemma 3: «If F ≥ 2, c > a + b,
  and c > a then LIFO is exponential on the networks G_n»).
- Result 6 (p. 329): «Under PAPE/MOVE or PAPE/NO MOVE sequence disciplines, a labeling method has exponential computational complexity»
  (root arcs of length M > 2^(n+1); Pape then reproduces LIFO on V_n).
- Result 7 (p. 329): «Under the DIJKSTRA sequence discipline, a labeling method has exponential computational complexity if arcs of
  negative lengths are admitted.» «This result has been previously obtained by Johnson [9]» (Johnson, JACM 20(3) 1973: NOT OPENED, ACM 403).
- Result 8 (p. 329): «Under FIFO/MOVE or FIFO/NO MOVE sequence disciplines, a labeling method has computational complexity O(n³)». Round t
  only holds labels of paths with ≤ t arcs. Conclusion: «only FIFO has polynomial complexity».
### 3.2 Textbook statements (opened)
- Orlin, MIT OCW 15.082J (2010) lecture 7 (sha256 446b0a03…): slide 9, «Theorem. Suppose all data are integral, and that there are no
  negative cost cycles …» the generic algorithm (ANY order) ends, «nC ≥ d(j) ≥ d*(j) > −nC … So, the number of iterations is O(n²C).»
  Slide 12: passes, «arcs to be scanned in any order», «at most n−1 passes. The running time is O(nm).» Slide 20: LIFO «bad in the worst
  case»; FIFO O(nm).
- Bertsekas, Network Optimization: Continuous and Discrete Models (1998), full-book PDF (sha256 9b4a0d6b…): Prop. 2.2 (d), pp. 59-60,
  finiteness iff there is no negative cycle reachable (real lengths; no count bound for arbitrary order). §2.4.1, pp. 73-74: Bellman-Ford,
  after cycle k «d_i … is less or equal to d_i^k», so O(NA). §2.4.2, p. 75: D'Esopo-Pape, «the number of entrances of some nodes in the
  candidate list V is not polynomial» (Kershenbaum 1981, Networks 11: NOT OPENED, Wiley 403; Shier-Witzgall). Also Bertsekas, Linear
  Network Optimization (1991) §1.3.3 pp. 75-76 (sha256 ac86b2c0…) and «A simple and fast label correcting algorithm», Networks 23 (1993)
  §1 (sha256 cee42f9a…): Pape «exponential in the worst case».
- AMO §5.4 (generic O(n²C), FIFO O(nm)): NOT OPENED; SECONDARY via Lehigh IE411 lecture 11 slides (sha256 380cfe8d…).
### 3.3 The exact order classes (answer to the Lead)
| order class | weights | count | bound | source |
| --- | --- | --- | --- | --- |
| generic, arbitrary order | integer, \|c\| ≤ C | label updates | O(n²C) (pseudo-polynomial) | Orlin OCW l.7 slide 9 |
| generic, arbitrary order | real | — | finite iff no negative cycle; no count | Bertsekas 1998 Prop. 2.2 |
| LIFO (MOVE / NO MOVE) | nonnegative integer, ~2^n | arcs examined | 3(2^n − 1), exponential | S-W Result 5, Lemma 3 |
| Pape deque (D'Esopo-Pape) | nonnegative integer, ~2^n | arcs examined | exponential | S-W Result 6; Bertsekas p. 75 |
| Dijkstra order | negative arcs allowed | arcs examined | exponential | S-W Result 7 (Johnson 1973 SECONDARY) |
| Dijkstra order | nonnegative | node scans | each node once | Bertsekas §2.3 (agent reading) |
| FIFO (MOVE / NO MOVE) | real | arcs examined | O(n³) | S-W Result 8 |
| passes (Bellman-Ford), any order inside a pass | real | arc scans | ≤ n − 1 passes, O(nm) | OCW slide 12; Bertsekas §2.4.1 |
- So: arbitrary order includes LIFO and is exponential (with nonnegative weights, exponentially large but of polynomial bit length). The
  polynomial class is defined by the PASS property: every arc whose label test fails at the start of a pass is examined before the pass
  ends.
### 3.4 Against BIP(ρ, τ) (box 88) (READING; nothing proved)
- BIP is not literally label-correcting. Its labels val(σ_t, ρ) are recomputed EXACTLY after every step, so there are no stale labels
  (the S-W effort counts exams caused by stale labels). BIP is the network-simplex / PI form of shortest paths in G_ρ, where a switch
  re-labels the whole subtree. The order is not adversarial either: it is the τ-optimum of σ_t ∪ offers.
- Transfer of the LOWER bounds needs a game in which the τ-optimum realises a LIFO / Pape-like order. Not done. The weights are no
  obstacle: S-W's lengths ~2^n are exactly the path-set weights 2^rank of parity valuations, so the pseudo-polynomial O(n²C) gives 2^O(n)
  for BIP.
- Transfer of the UPPER bound (passes) needs a missing lemma. PASS-BIP: an offer (y, z) that stays ρ-improving is taken by the τ-optimum
  within p(n) steps, or some bounded label rises. In N5 terms a refused but still-offered edge is a BLOCKED edge (box 86 GAP-DEV; R88's
  R*), so PASS-BIP is a per-release-epoch form of R*-POLY. Box 88's GP* already bounds each release-to-release epoch by n − 1. The open
  part is the number of epochs, exactly as box 88 says.

## 4. What SPEC S1's tie-break is inside a W-constant interval (new; lane-level)
Setting: a W-flat transition k → k+1 inside I. S4a builds the arena H_k (Even v keeps {σ_k(v)} ∪ Iσ_k(v); Odd keeps τ) and runs S1's
procedure on the DUAL of H_k (priorities + 1, owners swapped; experiments/new/box21/n5x.py step(), si.py Engine.evaluate). Inside I the
arena optimum against τ equals W (flat), and σ_k ⊆ H_k is W-tight (INTERVAL-SI (i)). In the dual, G-Even is the minimiser. A cycle node c
with Ω(c) odd is dual-even, so S1 (iv) takes the LONGEST path by recursion, «first strict maximum wins». A cycle node with Ω(c) even is
dual-odd, so S1 (iv) runs BFS over predecessors, «first discovery sets Odd's choice». Lists are in increasing index order. A cycle node
itself is set by S1 (v), a stack-based DFS (si.py l. 177-189).
- Claim RG (READING, from the correctness invariant of VJ's procedure; SPEC S1 (iii); not re-proved here). In c's round, the successors y
  of x that remain after the deletions of (iii) and satisfy dist(y) = dist(x) − 1 are exactly the W-tight arena edges of x (path set and
  length both optimal, and the computed values are W because the interval is flat). DATA: consistent with all 168 EVEN-branch switches
  (PLEX_OK 168, PLEX_BAD 0) and NT = 0 (no switch to a non-tight edge).
### 4.1 Lemma IDX-MONO (ODD branch) (PROVED, L-LIT, elementary, modulo Claim RG)
- Statement. If Even v ≠ c := λ_W(v) and Ω(c) is odd, then σ_{k+1}(v) = the smallest-index W-tight edge of {σ_k(v)} ∪ Iσ_k(v). Hence
  index(σ_{k+1}(v)) ≤ index(σ_k(v)), with equality iff v does not switch. Inside I, v switches at most |OPT_W(v)| − 1 times, and at most
  Σ_v (deg(v) − 1) ≤ m − n transitions of I switch an ODD-branch vertex.
- Proof. The recursion «for y in hs[x]: if d > best» over the sorted remaining successors returns the first maximum. By Claim RG these
  are the tight arena edges, all of maximal length. σ_k(v) is one of them (σ_k ⊆ H_k, tight). □
- DATA: the corpus has NO ODD-branch flat switch (0 of 179). So the branch is provably cheap and empirically empty.
### 4.2 Lemma LEX-BFS and LEX-MONO (EVEN branch) (PROVED, L-LIT, elementary, modulo Claim RG)
- Key. For a strategy σ in G_I and x with λ_W(x) = c, key_σ(x) := (x_{ℓ−1}, …, x_1, x_0), where x = x_0 → x_1 → … → x_ℓ = c is the (σ, τ)
  path (ℓ = W-length of x, fixed in I). Keys are compared lexicographically.
- LEX-BFS. If Ω(c) is even and v ≠ c is Even, then σ_{k+1}(v) = argmin over the W-tight arena edges y of key_{σ_{k+1}}(y).
  - Proof: BFS layer j+1 is built by scanning layer j in queue order and appending undiscovered predecessors in increasing index. By
    induction on j, queue order within a layer is lexicographic order of keys: same parent → by own index (last coordinate); different
    parents → by the parents' order (prefix). A vertex is discovered from the first queued tight successor, i.e. the lex-least one
    (Claim RG). □
- LEX-MONO. key_{σ_{k+1}}(x) ≤ key_{σ_k}(x) for every such x, strictly if x switches.
  - Proof: σ_k ⊆ H_k is a tight tree, and the BFS tree is the pointwise lex-min tree of H_k's tight edges. The min is unique because
    keys of distinct vertices differ in the last coordinate. □
- DATA: EVEN-branch flat switches 168 of 179. PLEX_OK 168 / 168, LEX_DN 168 / 168. Index order is NOT monotone here (DOWN 110, UP 58).
### 4.3 CN branch (v its own W-cycle node): no rule found (DATA)
- 11 switches in the corpus: DOWN 3, UP 8, smallest-index 1/11, largest-index 5/11. The LIFO DFS depends on the whole arena. CN-POLY is OPEN.
### 4.4 The lex keys alone cannot bound I: exponential stalling in the abstract model (DATA)
- Model LEX-ARENA: a layered tight DAG of width 2 (root c, layers 1..L, each vertex of layer j ≥ 2 has tight edges to both vertices of
  layer j − 1). Each step an adversary gives each Even v an arena ⊇ {σ(v)}, and σ becomes the lex-BFS choice. This is exactly S1's EVEN
  branch with an adversarial S2.
- Exhaustive longest run (docs/lit/T54-lexarena.py): L = 2, 3, 4, 5, 6 (n = 5 … 13) give 2, 8, 22, 52, 114 = 2^(L+1) − 2L − 2.
  Exponential. Width 3, L = 3: 15.
- READING: this is Cunningham's stalling picture inside N5. The lex structure (the analogue of strongly feasible trees) excludes cycling
  but allows exponentially long degenerate runs. Any proof of [P-INT] for the EVEN branch must use the constraint that the arena edges are
  exactly the Ξ-IMPROVING ones (S2), i.e. the coupling to σ̄, the Odd reply in G_I. This is the same place where box 88 locates the
  break of the one-player picture (poison, σ̄ ≠ τ).
- It is also a concrete template for L-RED's [P-INT] kill target (box 51b §5): realise the width-2 counter's adversarial arena schedule
  by Ξ-improvement in a G_I. Not attempted.
### 4.5 DATA summary (docs/lit/T54-tiebreak-check.py over box 50b/51b's corpus: sbcg 719 + alt 413 runs, 300 s each, all finished; latew_K16_m32, fx_K8_m32)
| list | flat transitions | intervals with ≥ 1 | ODD sw. | EVEN sw. (PLEX ok / LEX down) | CN sw. (down / up) | NT | FLI max | SWV max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sbcg (719) | 39 | 17 | 0 | 167 (167 / 167) | 11 (3 / 8) | 0 | 8 (u23sw64_n32) | 6 (u23sw64_n32) |
| alt (413) | 40 | 18 | 0 | 168 (168 / 168) | 11 (3 / 8) | 0 | 8 (u23sw64_n32) | 6 |
| latew, fx | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
- The two lists overlap (box 51b counts 79 = 39 + 40 per list). Distinct switches are the alt line (179).

## 5. Per-source verdict for [P-INT] (the brief's (c))
| source (opened unless marked) | hypothesis | does N5's S1 on G_I satisfy it? | missing lemma | bound for [P-INT] |
| --- | --- | --- | --- | --- |
| Cunningham 1976 (SECONDARY) | strongly feasible tree, any entering rule | analogue yes (Ξ ↑, LEX-MONO) | none for finiteness | finite; O(n²C)-type = 2^O(n) |
| Cunningham 1979 stalling (SECONDARY) | Bland's rule | — (warning) | — | exponential consecutive degenerate runs exist |
| Cunningham 1979 anti-stalling (SECONDARY, bound unconfirmed) | single entering arc, cyclic order, memory | no (set switches, no memory) | a history rule = a change of N5 | none for plain N5 |
| Avis-Friedmann Thm 3, 4, 7 | parity SI, round-robin | Thm 3 applies to G_I | — | a run of ≤ n − 1 switches EXISTS; LRC total is 2^n |
| Muramatsu Lemma 5 | alternating primal-dual pivots | no (τ fixed; no dual pivot inside a W-run) | a cut shrinking per flat step (D, gates are constant: box 51b §3) | none |
| Kukharenko-Sanità Thm 1 | an improving direction is known | no oracle | — | existence: n − m − 1 with an oracle |
| Tarjan 1991 Thm 4.6, 4.10 | min-mean cycle blocking | no | geometric shrinkage of a lex signature | none |
| Goldfarb-Hao (SECONDARY via GGT) | smallest label, max flow | no | ARC RE-ENTRY: re-use needs a bounded label to rise | none yet (the shape to look for) |
| Zhong-Ye (7.6) (preprint), Post-Ye 3.4 | one player, Dantzig single switch | no (two players, set, not greedy) | one-player reduction (NO-DEV gives FL = 0 there anyway) | none |
| Scherrer Lemma 8 | Howard switch-all-best, one player | no (box 51b §3: not greedy, not switch-all) | — | none |
| Goenka et al. Cor. 1 | any improving rule (DMDP) | yes | — | O(n³kα(k)^n), exponential |
| FHZ 1410.7530; Friedmann 1106.0778 | fixed sink / 1-sink, two players | partly (fixed cycle node) | W-tightness not in their games | lower bounds, not transferred |
| Björklund-Vorobyov DAM 2007 | LSP, fixed sink, attractive switches | close model | per-vertex monotone rule (§4.1 gives it for the ODD branch only) | O(n²\|E\|W) = 2^O(n) |
| S1 itself (§4) | — | — | CN-POLY, EVEN-POLY (must use S2's Ξ-offers; §4.4) | ODD part ≤ m − n per interval (IDX-MONO) |
- Reduction (PROVED modulo Claim RG): |I| ≤ (m − n) + CN_I + EV_I, where CN_I counts the transitions of I that switch a CN-branch vertex
  and EV_I those that switch only EVEN-branch vertices. So [P-INT] ⇐ CN-POLY ∧ EVEN-POLY. INT-LIN (|I| ≤ n − 1) stays a CONJECTURE.

## DONE / FINDINGS / NEEDS
- DONE: this note; docs/lit/T54-tiebreak-check.py (corpus check), docs/lit/T54-lexarena.py (abstract model); notes/L-LIT.md.
- FINDINGS:
  1. (a) Strong feasibility gives finiteness only. Stalling is exponential under Bland's rule (Cunningham 1979, SECONDARY). Polynomial
     degenerate-run bounds all need history, alternation, an oracle or bounded labels, and S1 has none of these.
  2. (b) Bias-only phases are polynomial only for specific one-player rules (Dantzig: Zhong-Ye (7.6) preprint, Post-Ye; Howard:
     Scherrer L8). For arbitrary rules the bound is exponential (Goenka). Lower bounds hold with a fixed sink (FHZ, BV §10, Friedmann).
  3. (d) Exponential: LIFO and Pape (nonnegative, ~2^n), and Dijkstra with negative arcs (Shier-Witzgall R5-R7). Polynomial: FIFO O(n³)
     (R8) and Bellman-Ford passes O(nm). Generic arbitrary order: O(n²C) only.
  4. READING: parity's path-set order IS the 2^n-weight regime, so every pseudo-polynomial bound is 2^O(n) for N5.
  5. PROVED (modulo Claim RG): IDX-MONO (ODD branch: smallest index, ≤ m − n transitions per interval) and LEX-BFS / LEX-MONO (EVEN
     branch: lex-min BFS tree, keys fall). DATA 168/168, 0 ODD switches.
  6. DATA: the abstract LEX-ARENA stalls exponentially (2^(L+1) − 2L − 2, L ≤ 6). EVEN-POLY must use S2's Ξ-offers.
  7. Reduction: [P-INT] ⇐ CN-POLY ∧ EVEN-POLY. BIP side: PASS-BIP ⇔ a per-epoch R*-type bound (READING).
- NEEDS: none from the owner for this note. Optional (owner, library access): Cunningham 1979 MOR, Goldfarb-Hao-Kai 1990, Orlin 1997,
  Johnson 1973, Kershenbaum 1981, AMO ch. 5 and 11, for exact statements now SECONDARY.
