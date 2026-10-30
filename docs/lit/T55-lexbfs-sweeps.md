# T55: LexBFS, LBFS+ multi-sweep convergence and graph-search orders, against S1's EVEN-branch BFS inside a W-constant interval (EV_I, LAYER-RESET)
L-LIT successor T54/T55 (Opus 5.5), D18. Lead's brief 2026-10-30 14:58Z (T55, graph algorithms × SI). Inputs: docs/lit/T54-stalling.md §4
(LEX-BFS, LEX-MONO), L-SI 33 dbc51c07 docs/si/N5-GATE-box51b.md §8 (CONJECTURE LAYER-RESET, counter reading). Written 2026-10-30
15:00Z-15:30Z (date -u). Working note, unrefereed, not a TARGET.md claim. G-N5-TIME, [P-INT], EVEN-POLY, INT-LIN stay OPEN.
Labels as in T54: PROVED-in-source / SECONDARY / PROVED (L-LIT, elementary, unrefereed, modulo Claim RG of T54 §4) / READING / DATA / OPEN.

## Summary
- S1's EVEN-branch choice is a plain BFS first-in tree of the reverse W-tight arena graph, with siblings in FIXED index order (T54
  LEX-BFS). It is NOT a LexBFS (Rose-Tarjan-Lueker) and its successive sweeps are NOT LBFS+ sweeps. DATA on the 1,132-run corpus:
  - the plain-BFS model predicts 828 / 828 Even choices at EVEN-branch flat transitions;
  - LexBFS would choose differently at 25 of them (15 of 40 transitions);
  - the "+" rule (ties by the previous sweep, last first) would choose differently at 180 (29 transitions).
  - Witnesses: u23sw64_n32 (§3).
- Structural difference. LBFS+ multi-sweeps run on a FIXED undirected graph, and the previous ORDER enters as the tie-break. In N5 the
  graph changes at every step (the arena H_k = σ_k ∪ S2's offers). The previous sweep enters only as EDGES (σ_k ⊆ H_k). Its tie-break is a
  static index order. On a fixed arena one S1 sweep is a fixed point (the same tree again), whereas LBFS+ never has a fixed point
  (LexCycle ≥ 2). So multi-sweep convergence theorems have nothing to act on: the whole dynamics of I is S2's arena change.
- Literature verdict (§1-§2): every multi-sweep bound is for undirected graphs in special classes. Dusart-Habib (n sweeps, cocomparability)
  is SECONDARY. LexCycle = 2 is proved only for subclasses. In general graphs LBFS+ cycles have length ≥ 3, and «we don't know in general
  any non-trivial bound on when the cycle will be reached» (Charbit-Habib-Mouatadid-Naserasr p. 3). No LexBFS theory for directed graphs
  was found beyond a remark. Bound for EV_I from this literature: none.
- New (PROVED, §4): from LEX-MONO,
  - (i) a weak LAYER-RESET: a return of a layer-d vertex needs a switch at some layer < d on the tree path of the target it returns to;
  - (ii) Lemma LAYER-WINDOW: between two transitions that switch lower-layer vertices, a layer-d vertex switches ≤ |OPT(x)| − 1 times.
  - So L-SI's mixed-radix counter bound EV-part ≤ Π_d (1 + m_d) now holds UNCONDITIONALLY (modulo Claim RG). It is polynomial when the
    switching depth D is O(1), and exponential in general.
  - T54's abstract LEX-ARENA run (2^(L+1) − 2L − 2) shows this counter can be filled without Ξ. INT-LIN needs S2.

## 1. Sources: LexBFS, four-point conditions, search trees
### 1.1 Rose-Tarjan-Lueker, SIAM J. Comput. 5(2) (1976) 266-283, doi 10.1137/0205021: NOT OPENED (SIAM 403)
- SECONDARY, definition (Charbit-Habib-Mouatadid-Naserasr arXiv 1702.02133, Algorithm 1, p. 6, opened): «pick an unnumbered vertex v with
  lexicographically largest label … foreach unnumbered vertex w adjacent to v do append(n − i) to label(w)». The label of w is the list
  of the visit times of ALL already-visited neighbours.
- SECONDARY (Beisegel et al. arXiv 1811.09249 p. 2): «a perfect elimination order of a chordal graph can be found by reversing an LBFS
  order on that graph». RTL's theorem number is unverified.
### 1.2 Corneil-Dusart-Habib-Mamcarz-de Montgolfier, "A tie-break model for graph search", arXiv 1501.06148v1: OPENED (sha256 12a502cc…, pp. 1-12)
- PROVED-in-source, four-point conditions for an order σ, a <σ b <σ c (condition (2) attributed there to Corneil-Krueger 2008, NOT OPENED):
  - BFS (Theorem 4.4, p. 8; label order A ≺ B iff umin(A) > umin(B)): «a ∈ N(c) − N(b), there exists d such that d ∈ N(b) and d <σ a».
  - LBFS (Theorem 4.6, p. 9; A ≺ B iff umin(B − A) < umin(A − B)): «a ∈ N(c) − N(b), there exists d <σ a, d ∈ N(b) − N(c)».
  - So BFS compares two vertices by their FIRST visited neighbour only. LBFS compares the whole visited neighbourhoods (symmetric
    difference). On a tie of first neighbours, LBFS decides by the next one, and BFS leaves it to the tie-break.
- Theorem 3.7 (p. 6): σ is producible by the search with some tie-break iff σ = TBLS(G, ≺, σ). LBFS+ in this formalism (p. 4): «τ is
  set to be the reverse of the previous LBFS ordering». Directed graphs (pp. 2-3): TBLS «may be performed on directed graphs without any
  modifications» (a remark; no theorem).
### 1.3 Beisegel et al., "Recognizing graph search trees", arXiv 1811.09249v2: OPENED (sha256 e2f99ac3…, pp. 1-4, 8, 11)
- Def. 3 (p. 8): the first-in tree (F-tree) of σ joins each vertex to its LEFTMOST neighbour in σ. Table 1 / Thm 8: F-trees of BFS are
  recognisable in linear time (Manber 1990, SECONDARY). F-trees of LBFS are «NP-complete on weakly chordal graphs» (3-SAT). Undirected.
- (c) S1's σ_{k+1} restricted to an even component is exactly the F-tree of the BFS order of the reverse tight arena graph with index
  tie-break (T54 LEX-BFS). (d) No count; recognition only.
### 1.4 Scheffler, arXiv 2206.14556v1 (partial search orders): OPENED (sha256 25f8e303…, pp. 1-5, 11)
- Problem 3 (p. 5): extend a partial order π to an A-ordering. NP-complete for BFS, DFS, LBFS, LDFS, MCS, MNS. Generic search O(n + m + |π|)
  (Thm 6). Undirected; no dynamics. Not used further.
### 1.5 Beisegel et al., "On the end-vertex problem of graph searches", arXiv 1810.12253v5: OPENED (abstract and introduction only)
- End-vertex problems NP-complete for LBFS on weakly chordal graphs and for BFS (SECONDARY there). Not used.

## 2. Sources: LBFS+ multi-sweep convergence
### 2.1 Charbit-Habib-Mouatadid-Naserasr, "A new graph parameter to measure linearity", arXiv 1702.02133: OPENED (sha256 5081bcef…, pp. 1-9, 13-14, 18-21, 24-28)
- Definition (p. 2): «Simon defines LexBFS+(G, σ) as the (unique) LexBFS ordering … obtained by breaking ties by always picking the right
  most vertex with respect to σ (for instance, LexBFS+(G, σ) starts with the last vertex of σ).» Multi-sweep: σ_i = LexBFS+(G, σ_{i−1}).
- Def. 2.1 (p. 6): «LexCycle(G) [is] the maximum length of a cycle of vertex orderings obtained via a sequence of LexBFS+ sweeps». No
  fixed points for n ≥ 2, since «the last vertex of an order is always the first vertex of the next order» (p. 3).
- PROVED-in-source:
  - LexCycle is even on cocomparability graphs (Cor. 3.6).
  - LexCycle = 2 on domino-free cocomparability graphs (Thm 4.1, which includes interval, cograph and cobipartite graphs).
  - Interval graphs (Thm 4.2): σ1 = σ3 from a LexBFS cocomparability start.
  - Proper interval graphs (Thm 4.5): «G is a proper interval graph if and only if the third LexBFS+ sweep on G is a PI-ordering».
  - Cobipartite graphs (Cor. 4.11): cycle reached «in fewer than 3n LexBFS+ sweeps».
- General graphs (pp. 6, 13): a 9-vertex graph with LexCycle 3. Starjoin (Prop. 2.4) gives LexCycle ≥ lcm of the parts' cycles. «suggests
  (but does not yet prove)» that LexCycle is not polynomially bounded. p. 3: «we don't know in general any non-trivial bound on when the
  cycle will be reached». CONJECTURED (§5): LexCycle = 2 for AT-free graphs, split graphs, trees.
- Dusart-Habib, DAM 216 (2017) 149-161: NOT OPENED (Elsevier, not fetched; HAL record without file). SECONDARY via this paper, p. 3,
  Theorem 1.1: «If G is a cocomparability graph on n vertices, and σ0 an arbitrary ordering … Then σn is a cocomparability ordering.»
  Conjecture 1.2 (p. 3): «for i sufficiently large, we have σi = σi+2» on cocomparability graphs. OPEN.
### 2.2 Gao-Xu, "The LexCycle on P2∪P3-free cocomparability graphs", DMTCS 22:4 (2020) #13, arXiv 1904.08076v5: OPENED (sha256 77afbca5…, pp. 1-5, 9)
- Thm 3.2 (p. 9): LexCycle = 2 on P2∪P3-free cocomparability graphs. Lemma 2.2 (p. 5): «G is a cocomparability graph if and only if O(n)
  LBFS+ sweeps compute a cocomparability ordering.» Flipping Lemma (Corneil-Dusart-Habib-Köhler 2016, SECONDARY via Lemma 2.3).
### 2.3 Dusart-Habib-Corneil, arXiv 1611.02002v1: OPENED (sha256 b5200cea…, introduction and §3 only)
- p. 3: «O(|V(G)|) LBFSs must be used in order to guarantee these results.» Not used further.
### 2.4 NOT OPENED
Corneil, "Lexicographic breadth first search – a survey", WG 2004 (Springer 429; author page gone); Corneil-Krueger, SIDMA 2008 (no open
copy; the DOI I tried gave 404); Corneil-Dalton-Habib, SICOMP 2013 (SIAM 403); Corneil-Olariu-Stewart, SIDMA 2009 (no open copy;
5 + 1 sweeps for interval graphs, SECONDARY via 1811.09249 p. 3); Corneil-Dusart-Habib-Köhler, SIDMA 2016 (HAL without file).

## 3. Is S1's EVEN branch a LexBFS, and are its re-sweeps "+" sweeps? (DATA, docs/lit/T55-sweep-check.py)
- Model, per W-flat transition k → k+1 and even W-cycle node c with a switched Even vertex. T_k = the W-tight arena graph on {λ_W = c}:
  Even x keeps the tight edges of {σ_k(x)} ∪ Iσ_k(x), and Odd x keeps τ(x). The searches run from c over reverse edges. choice(x) := the
  tight arena successor of x that comes first in the search order. Three searches:
  - S1: BFS with siblings by increasing index.
  - LEX: LexBFS (labels = visit positions of the already-visited tight successors; equal labels by index).
  - PLUS: BFS with siblings by decreasing position in the previous sweep. The previous sweep is S1's order on σ_k's tight tree.
- Corpus (box 50b/51b lists: sbcg 719, alt 413; 300 s per game; all finished; 21 games have flat transitions; latew_K16_m32, fx_K8_m32
  have none):

| list | flat tr. | Even choices checked | S1 model wrong | LexBFS differs (transitions) | "+" differs (transitions) |
| --- | --- | --- | --- | --- | --- |
| sbcg | 39 | 814 | 0 | 25 (15) | 179 (28) |
| alt | 40 | 828 | 0 | 25 (15) | 180 (29) |

- Witness, not LexBFS. u23sw64_n32 (experiments/red/xing/instances/u23sw64_n32.pg, start = best-reward), first flat transition, c = 13.
  - x = 3 (layer 7) has tight arena successors {17, 22} (layer 6). 17's are {9}; 22's are {9, 26}. 9 precedes 26 in the search.
  - S1 discovers 17 and 22 as siblings of 9 and orders them by index: 17 first, so σ_{k+1}(3) = 17 (the run's actual choice).
  - LexBFS ranks 22 above 17, because its label (pos 9, pos 26) extends 17's (pos 9). So it would choose 22.
  - This is exactly the BFS / LBFS four-point gap (§1.2): the witness d = 26 ∈ N(22) − N(17).
- Witness, not "+". Same instance and transition, x = 2, tight arena {6, 31}: S1 takes 31 (index ties), and the "+" order takes 6.
- How the re-sweeps differ from LBFS+, exactly:
  - (1) the graph is not fixed (H_k changes by S2's offers);
  - (2) the previous sweep is inherited as edges σ_k ⊆ H_k, not as a tie-break order;
  - (3) ties are by a static index;
  - (4) the graph is a directed layered DAG with a root (the cycle node), not an undirected graph of a special class;
  - (5) the search is plain BFS, not LexBFS.
  - Consequence of (1)-(3): with H fixed, S1 is idempotent (one sweep = fixed point), the opposite of LexCycle ≥ 2.

## 4. What does carry over: the counter bound, now unconditional (PROVED, L-LIT, elementary, modulo Claim RG)
Setting: an even component inside I; layer(x) := the W-length of x (fixed on I); key_k(x) as in T54 §4.2 (LEX-MONO: keys never rise and
strictly fall at a switched vertex; key(x) = key(σ(x))·x).
- Lemma RETURN-ANCESTOR (weak LAYER-RESET).
  - Statement. If Even x of layer d leaves y at k1 (σ_{k1}(x) = y ≠ σ_{k1+1}(x)) and returns, σ_{k2+1}(x) = y with k2 > k1, then
    key(y) strictly falls between k1 + 1 and k2 + 1. So some vertex on y's tree path (y or an ancestor, all of layer ≤ d − 1) switches
    in [k1 + 1, k2].
  - Proof. Let y′ := σ_{k1+1}(x). By LEX-BFS, key_{k1+1}(y′) < key_{k1+1}(y) (y ∈ H_{k1}(x)). By LEX-MONO for x,
    key_{k2+1}(y)·x = key_{k2+1}(x) ≤ key_{k1+1}(x) = key_{k1+1}(y′)·x < key_{k1+1}(y)·x. A key changes only if a vertex on its tree path
    switches. □
  - L-SI's CONJECTURE LAYER-RESET asks for a switch at layer exactly d − 1. That is stronger and stays CONJECTURE (DATA RET 78, UNX 0).
- Lemma LAYER-WINDOW. In a window of consecutive transitions of I in which no vertex of layer < d switches, each Even x of layer d
  switches at most |OPT_W(x)| − 1 times.
  - Proof. The keys of layer d − 1 are constant on the window. Each switch of x strictly lowers key(x) = key(σ(x))·x (LEX-MONO), so x
    moves through its tight successors in strictly increasing key order, without repetition. □
- Corollary COUNTER (unconditional form of box 51b §8's bound). With S_d := switches of layer-d vertices in I and m_d :=
  Σ_{layer(x) = d} (|OPT_W(x)| − 1): S_d ≤ (1 + Σ_{d′<d} S_{d′})·m_d.
  - So the EVEN-branch switch count is ≤ Π_{d=1}^{D} (1 + m_d) − 1 ≤ (1 + m)^D, with D := the deepest layer that switches in I.
  - That is POLYNOMIAL when D = O(1) and exponential in general. DATA: D up to 11 (u1t_cex_n32, box 51b §8).
- READING: T54 §4.4's LEX-ARENA run shows that COUNTER is nearly tight without Ξ: 2^(L+1) − 2L − 2 against Π (1 + 2) over L − 1 layers.
  Any proof of EVEN-POLY or INT-LIN must forbid carries with S2's Ξ-improvement condition, as L-SI says.

## 5. Per-source verdict (the brief's three questions)
| source | hypothesis (graph class, tie-break) | are N5's re-sweeps of that type? | bound for EV_I |
| --- | --- | --- | --- |
| RTL 1976 (SECONDARY) | undirected; LexBFS; chordal for the PEO theorem | no: plain BFS, not LexBFS (§3 witness x = 3) | none |
| Corneil et al. 1501.06148 Thm 4.4 / 4.6 | any undirected graph; 4-point conditions | S1's order satisfies the BFS condition with an index tie-break; not LBFS | none (characterisation only) |
| Beisegel et al. 1811.09249 | undirected; F-trees of BFS / LBFS | σ_{k+1} is a BFS F-tree of the reverse tight arena (directed) | none (recognition only) |
| Dusart-Habib 2017 (SECONDARY) | cocomparability; LBFS+ (ties: last of previous) | no (§3: dynamic graph, static ties) | none; n sweeps there |
| Charbit et al. 1702.02133; Gao-Xu 1904.08076 | domino-free / P2∪P3-free cocomparability, interval, proper interval, cobipartite; LBFS+ | no | none; general graphs: no known bound before cycling |
| Corneil-Olariu-Stewart 2009 (SECONDARY) | interval; 5 LBFS + 1 modified | no | none |
| this note §4 | S1 itself (LEX-MONO) | — | EV-part ≤ Π_d (1 + m_d) − 1, polynomial iff the switching depth is O(1) |

## DONE / FINDINGS / NEEDS
- DONE: this note; docs/lit/T55-sweep-check.py (corpus run in the scratchpad, outputs summarised in §3); notes/L-LIT.md.
- FINDINGS:
  1. S1's EVEN branch is a plain BFS (first-in tree, static index ties) on a changing directed layered arena, not LexBFS and not LBFS+.
     DATA: 828/828 choices match the model; LexBFS differs at 25 and "+" at 180. Witness u23sw64_n32 first flat transition, x = 3
     (LexBFS) and x = 2 ("+").
  2. Multi-sweep theory: bounds exist only for undirected special classes. Cycles of length ≥ 3 occur in general, with no general bound
     before cycling. Nothing applies to N5: on a fixed arena one S1 sweep is a fixed point, and the dynamics is S2's arena change.
  3. PROVED (modulo Claim RG): RETURN-ANCESTOR (weak LAYER-RESET), LAYER-WINDOW and Corollary COUNTER. L-SI's counter bound holds
     unconditionally; it is polynomial for bounded switching depth only.
  4. READING: INT-LIN / EVEN-POLY must use S2's Ξ-offers to forbid carries. Graph-search literature cannot supply this.
- NEEDS: none from the owner. Optional (owner, library access): Corneil 2004 survey, RTL 1976, Corneil-Krueger 2008, Dusart-Habib 2017,
  Corneil-Olariu-Stewart 2009.
