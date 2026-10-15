# R2: adversary report on L-SI's S1 Random-Action-Removal (original Random-Facet), the fleet's M4-R candidate

L-RED, 2026-10-15 (Lead brief 12:22Z). Target: docs/si/candidates/S1.md at claude/l-si 95d37d3 (rule `rar`, Zwick arXiv
2607.06334 Appendix D Fig. 1, fresh randomness at every call; valuations VJ; start best-reward). Code: experiments/red/fhz.py.

## Verdict: KILLED, by transfer of a published theorem (needs a referee for the transfer lemma)
Friedmann-Hansen-Zwick, "Random-Facet and Random-Bland require subexponential time even for shortest paths", arXiv 1410.7530,
Theorem 6.3 (p.22): on the weighted acyclic graphs G_{n,r,s,t} with r = Theta(log n), s = Theta(sqrt(n) log n), t = Theta(log n),
from the initial tree B0, the expected number of switches of the ORIGINAL Random-Facet algorithm is at least
e^Omega(sqrt n) = e^Omega(M^{1/3} / log M), M = Theta(n^{3/2} log^3 n) the number of edges. (The errata 1410.7871 p.2 names this,
together with Hansen's thesis, as the surviving Random-Facet bound; the SODA 2011 parity-game bound is for Random-Facet* only.)
Transfer lemma (below): there is a sink parity game P_{n,r,s,t} with Theta(M) vertices and edges, priorities O(nrs) (compressed
to {0..n} as TARGET section 1 allows), on which Random-Action-Removal from the best-reward start performs, switch for switch,
a run with the same distribution as Random-Facet on G_{n,r,s,t} from B0. Hence S1 needs e^Omega(sqrt n) expected switches
(each costing at least one valuation) on parity games of size Theta(n^{3/2} log^3 n): not polynomial expected time, not M4-R.
This closes the gap docs/lit/RANKING.md section 4 names ("construct sink parity games ... on which ORIGINAL Random-Facet
needs 2^(N^Omega(1)) expected iterations"): the answer is FHZ's own construction, re-encoded.

## The transfer
### G_{n,r,s,t} (1410.7530 section 5, Table 1 p.14; eps = 1/(rs))
Levels i = 1..n with vertices u_i, w_i, chains a_{i,j,k} (j in [r], k in [s]) and b_{i,j} (j in [rs]); target t = u_{n+1} = w_{n+1}.
Edges: a_{i,j,k} -> a_{i,j,k+1} (cost 0; a_{i,j,s} -> b_{i,1}) and -> u_{i+1} (2^{2i+1} + (k-1) eps, t copies); b_{i,j} -> b_{i,j+1}
(0; b_{i,rs} -> w_{i+1}) and -> u_{i+1} (2^{2i+1} + 1 + (j-1) eps, t copies); u_i -> b_{i,1} (0, t copies), u_i -> u_{i+1} (2^{2i},
t copies); w_i -> a_{i,j,1} (0, t copies each), w_i -> w_{i+1} (2^{2i}, t copies). B0 = any tree of "zero-edges" (the bit-0
edges a0, b0, u0, w0, i.e. the costly ones; p.14). Random-Facet (errata section 2, Zwick Fig. 1): RF(F, B): pick e uniformly
from F \ B; B' = RF(F \ {e}, B); if e is a strictly improving switch for B' then RF(F, B'[e]) else B'.

### P_{n,r,s,t} (fhz.py build(): the parity encoding)
- sink 0: Odd, priority 1, self-loop. Every other vertex is Even (one player; Odd has no choice anywhere).
- every vertex of G: priority 0 (below the sink, so never in a path set; it counts in the length only);
- every edge copy x -> y of G becomes x -> m (priority 0, one relay per copy) -> [class vertex] -> y, so copies of a
  multi-edge give equal valuations and equal lengths;
- level-i band base_i = 2 + (i-1)(4rs+2). Class A, the 0-cost chain exit b_{i,rs} -> w_{i+1}: shared EVEN vertex g_i, priority
  base_i + 4rs. Class B (u_i -> u_{i+1}, w_i -> w_{i+1}, cost 2^{2i}): no class vertex. Class C, an escape to u_{i+1} with
  offset d = (k-1) for a-escapes, rs + (j-1) for b-escapes (so d in [0, 2rs), cost 2^{2i+1} + d eps): shared ODD vertex
  o_{i,d}, priority base_i + 1 + 2d. All other 0-cost edges: relay only.
- edge ids are shared between G and P; a tree B of G is the strategy sigma_B of P that takes the relay of B's edge at every
  vertex of G. The best-reward start of si.py/vj.py on P is a zero-edge tree (all successors of a vertex of G are priority-0
  relays, reward 0; the tie-break takes the highest index, and the costly copies are added last), hence a valid B0: it takes
  the LAST copy of each zero-edge, while fhz.py's own driver starts from the FIRST copy; FHZ allow any zero-edge tree and the
  copies of a multi-edge are interchangeable (equal cost, equal set and length), so the two runs have the same distribution.
  (REFEREE-2 F2(c).)
Size: |V(P)| = |V(G)| + |E(G)| + n(2rs + 1), |E(P)| = 2|E(G)| + n(2rs + 1): Theta(nrst) = Theta(M).

### Transfer Lemma (L-RED, unrefereed)
For every tree B subseteq E(G) and every e in E(G) \ B: e is a strictly improving switch for B in G iff the relay edge of e is
an improving edge for sigma_B in P (VJ valuation, Friedmann 1106.0778 section 3). (The test depends on (B, e) only, so no
restriction to FHZ's functional F (Def. 5.2) is needed; Random-Facet's recursion also visits non-functional F. REFEREE-2 F2(b).) Consequently RF on G from B0 and RAR on P from
sigma_{B0} are the same random process (same random choices, same tests, same pivots), and FHZ Theorem 6.3 holds for P.

Proof. Write y_B(x) for the tree distance in G. For e = (x, y): e improves B iff c(e) + y_B(y) < y_B(x); in P, Xi(relay of e)
beats Xi(sigma_B(x)) iff the path x e-path is better than the tree path in the (set, length) order (sink odd: lexicographic set
order first, then longer is better). Both paths run from x to t; they differ on a prefix and coincide from their merge vertex on.
(1) Level accounting. A path from level i visits levels i, i+1, ..., n and pays at each level j exactly one class cost: A = 0
(reaching w_{j+1} through the chains), B = 2^{2j} (u0_j or w0_j), or C = 2^{2j+1} + delta (an escape to u_{j+1}), with
0 <= delta < 2. The sum of the costs below level j is < 2^{2j+1}(1/3) + 2(j-1)... precisely <= sum_{j'<j}(2^{2j'+1} + 2) =
(2/3)(4^j - 4) + 2(j-1) < 4^j - 2, while two different classes at level j differ by at least 4^j (B - A = 4^j, C - B = 4^j + delta). (REFEREE-2 F2(a).)
Hence for two paths pi, pi' from x whose class sequences differ, the cost order is decided by the class at the highest level j*
where the classes differ, EXCEPT that the levels above j* may contribute one within-level difference (see (3)).
(2) Equal class sequences. The two paths leave x by different edges. If x is a chain vertex a_{i,j,k} or b_{i,j}, either both
edges are escape copies (the chain edge is unique): same offset, equal cost, and in P equal set and equal length; or one is the
chain edge and the other an escape copy, and the chain path escapes later at the same level (class C on both; if the chain
path reached w_{i+1} the classes would differ and case (3) applies): the offsets are k-1 < k''-1 (or rs+j-1 < rs+j''-1, or an
a-chain offset < s <= rs <= a b-chain offset), G orders by the offset, and in P the only difference is the later escape's
o_{i,.} with the larger odd priority on the chain path, so both prefer the immediate escape. (Sub-case added for REFEREE-2 F1.) If x = u_i: both u1 copies or both
u0 copies: equal cost, equal set, equal length. If x = w_i: both w0 copies (equal), or both chain entries w_i -> a_{i,j,1},
a_{i,j',1}: class A on both (merge at b_{i,1}: equal cost; in P no class vertex before the merge and equal lengths s + s relays),
or class C on both with offsets k-1 and k'-1 (merge at u_{i+1}): the cost order is the offset order and in P the only
difference is o_{i,k-1} vs o_{i,k'-1}, both odd, the larger (= larger offset) being worse. So equal class sequences give the
same verdict in G and P, ties included.
(3) Different class sequences. Let j* be the highest level with different classes. Above j* the classes agree; a level j > j*
can still carry a cost difference only if both paths take class C there with different offsets, and then they merge at u_{j+1};
below j the classes agree and are A or B (another class-C level would be an earlier merge), so there is at most one such j, and
below j* everything is bounded as in (1). Entering level j: the two paths come from different vertices of level j (they merged
only at u_{j+1}), one from w_j (a-chain escape, offset < s) and one from u_j (b-chain escape, offset >= rs > offset of the other),
because entering at the same vertex would mean an earlier merge, and a w_j path through b_{j,1} would meet the u_j path there.
Now walk down from j to j*: at each level between, the classes agree, and the path that entered level j at w_j entered level j'
at w_{j'} as well (class A leads to w, class B from w leads to w), while the other stayed on the u side (class B from u, or C);
at j* the w-side path has class A or B and the u-side path has class B or C, with a strict difference, so the w-side path is
cheaper at j* by at least 4^{j*} - 2 > (the sum below j*) + (the offset difference at j, < 2). So in G the w-side path wins. In
P the maximum of the symmetric difference is the pair o_{j,.} at level j (band j is the highest differing band), and the u-side
path holds the larger offset, i.e. the larger odd priority: the w-side path wins. If no such j exists, the symmetric difference
tops at level j* where A carries the even g_{j*} and C the odd o_{j*,.} and B nothing, ordered A > B > C in P exactly as the costs
0 < 2^{2j*} < 2^{2j*+1} + delta in G. In all cases the verdicts agree, and ties (equal cost) occur only in case (2) where P also
ties (equal set and equal length, so neither direction is improving). The run equivalence follows because Random-Facet's
behaviour is a function of the sequence of answers to exactly these tests (Zwick Fig. 1: the test "(c -> b) in H" is
"VAL_b prec VAL_c", i.e. the improving test at the vertex of the removed action). QED.

### Evidence (experiments/red/fhz.py; all on claude/l-red)
- `lockstep n r s t seeds`: one Random-Facet driver feeds the same random edge choices to the weighted model and the parity
  model and asserts that every improving test agrees. Agreed on every test: (3,1,1,1) 5 seeds; (5,2,2,2) 3 seeds (up to 190
  switches, 7,589 tests); (6,1,3,2) 3 seeds; (7,2,3,3) 2 seeds (769 switches, 72,296 tests, |V(P)| = 610).
- `lockstep3`: a third model, the exported .pg evaluated by the generic VJ engine experiments/red/vj.py (validated by brute
  force over Odd's counterstrategies this morning), agrees on every test: (3,1,1,1) 3 seeds, (4,2,1,2) 2 seeds.
- `relation n r s t samples`: random functional F and random tree B in F, arbitrary (not only reachable): the SETS of improving
  edges in G and P coincide on 300 + 300 + 200 samples for (4,2,2,2), (6,1,2,1), (5,3,2,2); and on 400 + 1500 + 300 further samples for (8,2,3,2),
  (10,1,1,1), (6,3,3,3): 2,200 of 2,200 identical.
- L-SI's engine: `si.py rar` on the exported instances/fhz_n3_r1s1t1.pg, fhz_n4_r1s1t1.pg (best-reward start): mean switches
  19.1 and 26.3 over 30 seeds, against 18.9 and 29.9 of my driver over 200 seeds; strategies pass harness/verify.py and the
  regions equal Zielonka's (every vertex is Odd's, as in every sink game).

## (b) Measured growth (my Random-Facet driver on P, = on G by the lemma; mean switches over seeds, best-reward start)
| n | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| r=s=t=1: \|V(P)\| | 31 | 46 | 61 | 76 | 91 | 106 | 121 | 136 | 151 | 166 | 181 |
| mean (200 seeds) | 10.7 | 18.9 | 29.9 | 42.4 | 56.9 | 68.7 | 86.5 | 102.9 | 125.2 | 142.0 | 159.4 |
| max | 16 | 36 | 58 | 88 | 148 | 156 | 200 | 214 | 296 | 330 | 362 |
| r=s=t=2: \|V(P)\| | 103 | 154 | 205 | 256 | 307 | 358 | 409 | | | | |
| mean (60 seeds) | 27.1 | 52.1 | 89.2 | 133.8 | 197.4 | 262.8 | 354.6 | | | | |
| r=2,s=3,t=3: \|V(P)\| | 175 | 262 | 349 | 436 | 523 | 610 | | | | | |
| mean (30 seeds) | 40.8 | 88.0 | 152.5 | 232.7 | 355.9 | 526.5 | | | | | |

Log-log slopes in n over the last four sizes: about 1.5 (r=s=t=1), 1.9 (r=s=t=2), 2.1 (r=2,s=3,t=3): polynomial-looking at
these sizes, like L-SI's n^1.8 on randomfacetsubexp. This is expected: Theorem 6.3 is asymptotic and its parameters r, s, t grow
with n (the gadgets make the random counter's bit order hold with high probability only for large n); the tables are
consistency data, not the kill. The kill is the theorem plus the lemma.

## Why FHZ did not state the parity-game consequence themselves (the Lead's referee question)
Both texts were searched for every mention of parity games, MDPs and the reason for the shortest-path setting.
- 1410.7530 abstract (p.1): "We previously showed that Random-Facet performs an expected number of 2^Omega~(m^{1/3}) pivoting
  steps on some LPs with m inequalities that correspond to m-action Markov Decision Processes (MDPs). ... Here we show that the
  same results can be obtained using LPs that correspond to instances of the classical shortest paths problem. This shows that
  the stochasticity of the MDPs, which is essential for obtaining lower bounds for Random-Edge, is not needed in order to obtain
  lower bounds for Random-Facet."
- 1410.7530 section 1 (p.2): "The lower bound given in [17] is for parity games, a class of deterministic 2-player games. The lower
  bounds given in [18, 23] are for LPs that correspond to Markov Decision Processes (MDPs), a class of stochastic 1-player games.
  ... Here, we obtain subexponential lower bounds for the running times of Random-Facet, Random-Facet1P and Random-Bland on LPs
  that correspond to standard acyclic shortest paths problems, the simplest form of deterministic 1-player games." and "It is
  interesting, and perhaps surprising, that Random-Facet, the fastest known pivoting rule for general linear programs, requires a
  subexponential number of pivoting steps even for acyclic shortest paths problems which can be easily solved in linear time."
- 1410.7530 section 3 (p.7): "we show that such lower bounds ... can be obtained using linear programs that correspond to the purely
  combinatorial problem of finding shortest paths in directed graphs. The graphs we use are even acyclic and all their edge weights
  are non-negative."
- errata 1410.7871 (p.2): "The proof in [5] was presented for Markov decision processes. In [3] we transfer the lower bound
  construction to the setting of shortest paths"; and, about the RF versus RF* examples only: "It is not difficult to obtain
  similar examples for parity games."
Nothing in either text says that the shortest-path instances cannot be, or are not, parity games, and nothing restricts the
result to LPs for a stated reason. The papers move in one direction only, from games to ever simpler LPs ("the simplest form of
deterministic 1-player games"), because their audience is the simplex/LP one and the point made is that stochasticity is not
needed. The step back to parity games needs the observation of the Transfer Lemma (the costs of G_{n,r,s,t} are a lexicographic
set order, so the VJ valuation of a sink game reproduces every improving test, ties included); it is not a general reduction from
shortest paths to parity games, which does not exist for arbitrary additive costs (the Lead reading of this report). So: no
remark found; the omission is explained by direction and audience, not by an obstacle they name.

Referee status: REFEREE-2 first read docs/referee-2/R2-TL.md (referee-2 995cfd3): "OK with fixes", F1 and F2 applied above;
its independent exhaustive check (every tree and every edge for four small parameter settings, 435,584 tests) found 0 disagreements.

## What this does not say
- The bound is e^Omega(sqrt n) in the number of bits, 2^Omega~(M^{1/3}) in the size; it rules out polynomial expected time, not
  the subexponential upper bound of Zwick Thm 8.2.
- The transfer lemma is unrefereed. The weakest step is (3), the entry argument; the random-relation checks on arbitrary
  trees are its empirical cover.
- The lemma is specific to G_{n,r,s,t}'s cost structure (one class per level, offsets below 2, class gaps >= 4^j). It does not
  claim that every shortest-path instance is a sink parity game.

## DONE / FINDINGS / NEEDS
- DONE: this report; experiments/red/fhz.py (+ instances/fhz_*.pg); notebook; check.sh pins lockstep3 (3,1,1,1) and relation (4,2,2,2).
- FINDINGS: S1 killed by FHZ Thm 6.3 + transfer lemma; measured growth tables; si.py rar consistent with an independent driver.
- NEEDS: REFEREE on the transfer lemma (section "Transfer Lemma"); Lead: record in docs/si/DEAD.md and RANKING section 4.
