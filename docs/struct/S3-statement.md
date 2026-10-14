# S3: the diagonal w^V(n,n) and the fixed-n saturation of weak separators (L-STRUCT, 2026-10-14)

Status: statement, REFEREE-checked with CHANGES (docs/referee/2026-10-14-S3-statement-check.md, referee 5b99f2f);
all six findings applied below (marked [R1]-[R6]). Awaiting L-LIT T6 (novelty; L4 sources) before proof work. Vocabulary: docs/struct/S1-statement.md (D1-D5, conventions E/S/V,
Lemmas 1-3 refereed). Lead's framing (20:09Z): the algorithmic question is the diagonal, because a TARGET game with n
vertices has priorities in {0..n}, which after the shift by 2 and S1 Lemma 2(b) means the automaton must be a weak
(n, n)-separator of convention V (REFEREE S2 finding 3). Fixed-n growth in d is algorithmically irrelevant; it is kept
here only as the mechanism that produced the weak < strong cells.

## 1. The quantity that matters
D6. The diagonal: W(n) := w^V(n, n) and S(n) := s^V(n, n) (S1 D5 minima; letters = TARGET priorities, 0 removed by
S1 Lemma 2(b-V), the vertex-labelled version with the contraction proof [R1]). An algorithm of the product class ((i)-(iii) of S2 §1 as fixed by the REFEREE) correct on all TARGET
games with ≤ n vertices has |A| ≥ W(n) and running time ≥ n·W(n). Conversely (S1 Lemma 1, refereed, plus linear-time
safety-game solving) a deterministic weak (n,n)-separator A of convention V, computable in time t(n), solves every
TARGET game with n vertices and m edges in time O(t(n) + (n + m)·|A|) and outputs the regions. Positional strategies
do NOT come from the product strategy (it has memory |A|); they come from the region oracle with polynomially many
calls (TARGET §3), as the gauntlet requires [R2].

Data (L-STRUCT, SAT + checker, unrefereed except C1; experiments/weak-sep/results/table.md):
| n | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| W(n) = w^V(n,n) | 1 | 2 | 5 | 7 | open (L-COMP) |
| S(n) = s^V(n,n) | 1 | 2 | 5 | 7 | open |
| s^E(n,n) (for comparison) | 1 | 2 | 5 | 8 | open |
On the diagonal weak and strong coincide on every computed cell. The weak < strong cells all lie above the diagonal
(d ≥ n + 3): (2,5), (2,6), (2,7..12), (3,5), (3,6), (3,8).

## 2. Target T3 (Lead's framing 20:23Z, option (ii) with the explicit f the data allow; (i) is the case d ≤ n)
T3 and T3-pos below exclude each other only under L4 [R3]: if S(n) were polynomial, W = S and W polynomial would both
hold, and strong V-separators would already give a product algorithm.
T3. For all n ≥ 1 and all d with 1 ≤ d ≤ n + 1:   w^V(n, d) = s^V(n, d).
  In words: on and just above the TARGET range, deterministic weak separators of convention V are no smaller than
  strong ones. The case d ≤ n (TARGET alphabet after S1 Lemma 2(b)) is the Lead's option (i); f(n) = n + 1 is the
  largest threshold consistent with the data (gaps at (2,5) = n+3 and (3,5) = n+2; equality at (2,4) = n+2 and at
  every cell with d ≤ n+1). Consequence: W(n) = S(n); the product class (i)-(iii) of S2 §1 gains nothing from
  weakening, and every known quasi-polynomial product algorithm's size bound is tight for its class exactly where
  algorithms live. The quasi-polynomial reading needs L4. M3 status if proved and refereed: extends the separation
  barrier (B1) to deterministic weak separators on the algorithmic range; Lead to rule, L-LIT to check novelty.
T3-pos (the opposite, M4 route; stated so the refutation of T3 has a name). There are a polynomial p and a
  deterministic algorithm that on input n outputs in time p(n) a deterministic weak (n, n)-separator of convention V
  with ≤ p(n) states. Consequence: by §1 an algorithm meeting TARGET §2, then the gauntlet (TARGET §5). A single cell
  with w^V(n,d) < s^V(n,d) and d ≤ n + 1 refutes T3 and is the first evidence for T3-pos.
L4 (needed for any V-barrier; open): s^V(n, n) is super-polynomial in n. CDFJLP Thm 5.1 covers E only; s^V ≤ s^E and
  s^V < s^E already at (4,4) (7 vs 8) and (4,6) (10 vs 13). The Parys-Wiącek remark that the necessity proof "does not
  apply" for vertex priorities (docs/lit/BARRIERS.md B1 fine print) is the obstacle; L-LIT to check for any source.

Data for T3 (all cells with d ≤ n + 1 computed so far; L-STRUCT unrefereed, L-COMP with LRAT-verified UNSAT at
value−1, CryptoMiniSat agreement and re-checked witnesses, claude/l-comp 8d9697b experiments/sat-hard/results/cells.md):
| cell (V) | w | s | source |
| --- | --- | --- | --- |
| (1,1), (1,2) | 1 | 1 | L-STRUCT |
| (2,2), (2,3) | 2, 3 | 2, 3 | both |
| (3,3), (3,4) | 5, 5 | 5, 5 | both |
| (4,4), (4,5) | 7, open | 7, open | both at (4,4); REFEREE reproduces n ≤ 3 [R6] |
| TARGET alphabet {2..n+2}, n = 2, 3, 4 | 2, 5, 7 | 2, 5, 7 | L-COMP (LRAT; n = 4 strong confirmed 20:32Z); equals w^V(n,n) as S1 Lemma 2(b-V) predicts |
No cell with d ≤ n + 1 violates T3. Decisive next cells: (4,5) V (both), (5,5) V, (5,6) V. Above the threshold the
equality fails: (2,5), (2,6), (2,7..12), (3,5), (3,6), (3,8), (3,10) (w^V(3,10) ≥ 8 > ... s^V(3,10) open).

## 3. Mechanism: why the gap appears only when d is large against n (structural core; hypotheses, testable)
Fact M0 (elementary, to be written up with S3's proofs). In a word of OddCycles^X_{n,d}, every window of n + 1
  consecutive letters contains a factor whose maximum is odd (n + 1 edges visit a repeated vertex, the closed part is a
  cycle, its maximum is odd); dually every (n+1)-window of a word of EvenCycles^X_{n,d} contains a factor with even
  maximum. For n = 2 this is "no two consecutive odd letters in even words, no two consecutive even letters in odd
  words" (verified on the maximal graphs). These are local constraints, independent of d.
Fact M1 (refereed lasso condition, S1 Q3). A weak separator may keep a reachable odd simple cycle C exactly when the
  lasso words π(P)·π(C)^ω are unrealisable by odd graphs with ≤ n vertices; the cheap filter is |P| + |C| > n.
Hypothesis H2 (where the saving comes from). The strong minimum pays one universal-tree level per odd letter
  (s^E(2,2h) = h + 1 by the universal tree; in V verified for h ≤ 4 only [R4]; in general the (n, d/2)-universal tree). A weak separator can merge the levels of the odd letters
  that an n-vertex graph cannot "count" against each other: with ≤ n vertices a graph realises at most n distinct
  letters per cycle structure (V: at most n letters in the whole word), so for d ≫ n most letters are, for every
  single graph, either absent or interchangeable, and the separator exploits this with odd cycles of the kind M1
  allows (all witnesses: cycles through high even letters, e.g. (5 4 4)^ω, (9 4 8)^ω, (7 2 4 2)^ω). For d ≤ n + 1 every
  letter can occur with every other inside one n-vertex graph, so nothing can be merged: this is T3's content.
  Test of H2: minimal weak witnesses at gap cells should have odd simple cycles only through letters ≥ some threshold
  that grows with n; refuted if a gap cell has a minimal witness whose odd cycles all lie below n + 1.
Hypothesis H1 (saturation in d; non-algorithmic). For every n there is D(n) with w^V(n, d) = w^V(n, D(n)) for all
  d ≥ D(n). Evidence: w^V(2, d) = 2, 2, 3, 3, 3, 4, 4, 4, 4 for d = 2, 3, 4, 5, 6, 7, 8, 9, 10 and 4 at d = 12 (d = 11
  not run), against s^V(2, 2h) = h + 1 for h ≤ 4 (SAT) and s^E(2, 2h) = h + 1 for all h (universal tree) [R4]; E:
  w^E(2, 8) = w^E(2,10) = w^E(2,12) = 4. At n = 3: w^V(3,6) = 6, w^V(3,8) = 7, w^V(3,10) ≥ 8 (k = 7 refuted), so H1 is not yet visible at n = 3;
  L-COMP's w(2,d) to d = 20 and my w^V(3,d) for d = 10..14 test it. H1 says nothing about the diagonal.

## 4. Decisive data (L-COMP's cells, in order of value)
1. (4,5) V, then (5,5) V and (5,6) V: any strict inequality refutes T3 (and names the first algorithmic gap).
2. w^V(3, d), d = 10, 12, 14 (mine, cheap, capped): tests H1 and, with the odd-cycle probe, H2.
3. (6,6) V if feasible.
A refutation of T3-pos is not available from finite data; its support can only come from a construction.

## 4b. First target and proof route (≤ 1 page; Lead's ask 20:32Z; L-STRUCT's call, reasons given)
Choice: L4 first, T3 second. Reasons. (a) L4 is needed for any barrier reading of T3 and of the whole weak-separator
line, so it is on every path. (b) L4 has a visible route that reuses CDFJLP's proof with one new construction, while
T3 has no route yet: the obvious sub-lemma for T3 ("a weak separator's even-used transitions contain no odd cycle, so it
prunes to a strong one of the same size") is already dead at (3,3) V, where d = n: the committed 5-state minimal weak
witness weak_V_n3_d3.json has an odd cycle inside its even-used part (wsep/analyze.py: live_has_no_odd_cycle = False)
although w^V(3,3) = s^V(3,3) = 5. So T3, if true, is an inequality of sizes between different objects, which needs
the extraction argument below, not pruning. (c) The Lead's reading (T3 first) is noted; if the Lead prefers it, route
R2 is the plan.

Route R1 for L4 (s^V(n, d) is super-polynomial on the diagonal). CDFJLP Lemma 5.1 extracts an (n, d/2)-universal tree
from any strong (n,d)-separator using the even graphs G_t (one vertex per leaf of a tree t with n leaves, edges
v_i → v_j with the even common-ancestor priority and v_j → v_i with that priority minus one, even self-loops) and the
words α_t they realise. G_t is edge-labelled with many distinct out-labels per vertex. Step 1: build a vertex-labelled
even graph G'_t with c·n vertices realising α_t (or a word with the same repetitive structure): candidate is to split
v_i into one copy per out-priority it uses on the path α_t, and to show α_t visits each v_i with O(1) distinct
out-priorities between resets, giving c = O(1); fallback c = O(d), which still yields a super-polynomial bound at
d = Θ(n / lg n) but not at d = n. Step 2: re-run Lemma 5.1's argument (the tree-decomposition of the states by
resistance; Lemma 5.2 holds verbatim since the separator is strong) with G'_t in place of G_t: s^V(c·n, d) ≥
C(⌊lg n⌋ + d/2 − 1, ⌊lg n⌋), i.e. s^V(n, d) ≥ C(⌊lg(n/c)⌋ + d/2 − 1, ⌊lg(n/c)⌋). Step 3: check against the table
(s^V(4,4) = 7, s^V(4,6) = 10, s^V(3,6) = 7) that the bound is consistent, and against Parys-Wiącek 2305.00308 §4 (to
be opened) that it does not contradict their "⌊n/2⌋-universal trees suffice". Deliverable: a theorem statement in
TARGET vocabulary with the exact c, then the REFEREE.

Route R2 for T3 (W(n) = S(n), or w^V(n,d) ≥ s^V(n,d) for d ≤ n+1), to be attempted after L4 or on the Lead's word.
Replace Lemma 5.2's hypothesis (no reachable odd cycle) by the lasso condition M1 and the window fact M0: for d ≤ n+1
show that every reachable odd simple cycle C of a deterministic weak V-separator with any path P from q0 has a lasso
word realisable by an odd V-graph with ≤ n vertices after folding (the folding must create only odd cycles; this is
where d ≤ n+1 should enter, since a V-graph on ≤ n vertices with ≥ n+1... letters cannot exist, the folding is forced
to reuse vertices with equal labels). If that sub-lemma (call it L5') holds, Lemma 5.2 goes through and Lemma 5.1
gives the universal tree, hence w^V(n,d) ≥ s^E-type bound; the equality with s^V then needs the V version of Lemma
5.1 from R1 anyway. DATA STEP DONE (experiments/weak-sep/lasso_analysis.py, results/lasso_analysis.md): for every committed minimal
weak V-witness with n ≤ 3 (d ≤ 6) and (4,4), all reachable odd simple cycles, all simple paths P from q0 into them,
and the least odd V-graph realising each lasso word (exact DFS). Result: L5' is FALSE. At (3,3) V (d = n) the minimal
5-state weak witness has one reachable odd simple cycle whose lasso words need 4 > 3 vertices, so it is weak, not
strong, with w = s = 5; at d ≤ n+1 weak separators therefore need not be strong, and R2 cannot go through Lemma 5.2
"no odd cycle". Across all witnesses the least odd graph for a tolerated lasso word has exactly n+1 vertices except
(3,6) V (n+2): the tolerated cycles sit exactly at W2's edge. Dead end recorded in notes/L-STRUCT.md.
What remains of R2: a pure size argument, i.e. an injective map from the leaves of an (n, ·)-universal-tree-like
structure into the states of any deterministic weak V-separator with d ≤ n+1, built from even-realisable words only
(the quasi-orders of CDFJLP Lemma 5.1 defined through paths that are prefixes of EvenCycles^V_n words) and using the
tolerated odd cycles' position at W2's edge. No sub-lemma for this is formulated yet; it is the open core of T3.

## 5. Calibration
- Everything above the diagonal (n = 2, d ≥ 5; n = 3, d ≥ 5) is about letters a TARGET game of that size cannot have.
  The only algorithmically meaningful numbers so far are W(n) = S(n) for n ≤ 4.
- A polynomial W(n) would contradict nothing known (S1 F3, F5 are strong or time-bounded), but no mechanism for it is
  visible in the data: the weak savings so far come from odd cycles whose lasso words need more than n vertices, and
  on the diagonal the solver found none.
- Timestamps in L-STRUCT's earlier messages of this day ran ahead of UTC by up to 90 minutes (clock not consulted);
  the SHAs are authoritative.
