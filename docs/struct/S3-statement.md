# S3: the diagonal w^V(n,n) and the fixed-n saturation of weak separators (L-STRUCT, 2026-10-14)

Status 2026-10-14 (Lead 21:59Z): T3 is PARKED as a data-backed conjecture. Statement REFEREE-checked (5b99f2f, findings
[R1]-[R7] applied); novelty NEW (L-LIT T6); T3 + L4 would be M3 (Lead L7). Data: w^V(n,d) = s^V(n,d) on every computed
cell with d ≤ n+1 through (4,5) V (table in §2). Two proof routes tried and dead with instances (docs/struct/T3-proof-
attempt.md; notes/L-STRUCT.md Dead ends): D-A (Lemma A as stated: all-odd cycles), D-C1 (rewire target "next or self"),
D-C2 (any deterministic target rule), D-HB2 (hidden universal tree in A − τ0). What revives it: a diagonal gap at n = 5
(w^V(5,5) < s^V(5,5), L-COMP's successor), which would turn the question towards T3-pos, or a new proof idea for the
size statement. Supporting facts that hold on data: docs/struct/S4-structure-note.md. L4 is signed by the first referee
(9bf5301) and waits for the second referee together with whatever T3 becomes. Vocabulary: docs/struct/S1-statement.md (D1-D5, conventions E/S/V,
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
L4 (needed for any V-barrier): s^V(n, n) is super-polynomial in n. WRITTEN UP for refereeing in docs/struct/L4-proof.md
  (transfer lemma = L-LIT's Claim R, T6; S(n) ≥ (√n/(2 lg n))^{⌊½ lg n⌋ − 2} = n^{Ω(lg n)}). L-LIT T6: no vertex-priority
  lower bound in print; Parys-Wiącek 2305.00308 p.2 state the vertex-splitting conversion as a remark. Lead L7: L4 is a
  supporting lemma; T3 + L4 count as M3.

Data for T3 (all cells with d ≤ n + 1 computed so far; L-STRUCT unrefereed, L-COMP with LRAT-verified UNSAT at
value−1, CryptoMiniSat agreement and re-checked witnesses, claude/l-comp 8d9697b experiments/sat-hard/results/cells.md):
| cell (V) | w | s | source |
| --- | --- | --- | --- |
| (1,1), (1,2) | 1 | 1 | L-STRUCT |
| (2,2), (2,3) | 2, 3 | 2, 3 | both |
| (3,3), (3,4) | 5, 5 | 5, 5 | both |
| (4,4), (4,5) | 7, 10 | 7, 10 | both at (4,4); L-STRUCT at (4,5) (weak k = 9 refuted in 3319 s, k = 10 SAT; strong k = 9 refuted in 1331 s); REFEREE reproduces n ≤ 3 [R6] |
| TARGET alphabet {2..n+2}, n = 2, 3, 4 | 2, 5, 7 | 2, 5, 7 | L-COMP (LRAT; n = 4 strong confirmed 20:32Z); equals w^V(n,n) as S1 Lemma 2(b-V) predicts |
No cell with d ≤ n + 1 violates T3; (4,5) V, the first non-trivial n = 4 cell, gives equality 10 = 10. Also (4,6) V, d = n + 2, gives w = s = 10 (2026-10-22: w ≥ w^V(4,5) = 10 by S1 Lemma 2(a), 10-state weak
witness results/automata/weak_V_n4_d6_k9.json re-verified), so at n = 4 no gap appears even one step above the threshold. Decisive next cells: (5,5) V, (5,6) V. Above the threshold the
equality fails: (2,5), (2,6), (2,7..12), (3,5), (3,6), (3,8), (3,10) (w^V(3,10) ≥ 8 > ... s^V(3,10) open).

n = 5 (2026-10-22 box, experiments/weak-sep/results/n5/): s^V(5,5) ≥ 11 (strong k = 10 UNSAT on 30 maximal even
graphs, 420 s; CaDiCaL 1.7.4 LRAT proof VERIFIED by experiments/sat-hard/lrat_check.py, 3417924 RUP steps, CNF sha256
af340fd5...; agrees with L-COMP's CEGAR k = 10); s^V(5,6) ≥ 11 by S1 Lemma 2(a). w^V(5,5) ≥ 11 (2026-10-22 14:17Z: weak
k = 10 UNSAT by Lemma P, CEGAR on 80 even + 40 odd graphs, 7 rounds, last solve 11913 s, 4004493 clauses;
results/n5/weak_V_n5_d5_k10.json; SOLVER-ONLY: pysat CaDiCaL 1.5.3, no LRAT proof, as re-solving with a proof costs
~3.3 h and a proof of tens of GB); hence w^V(5,6) ≥ 11 as well. So no gap with w ≤ 10 at (5,5). No n = 5 upper bound:
strong (5,5) k = 11 undecided: one solver call ran from 07:58Z 2026-10-22 for at least 8 h 24 min (alive at 16:22Z),
then was lost when the session's container restarted before the 01:30Z cap, with no result (k = 10 took 7 min, so the
cost per extra state is > 70x here), weak (5,5) k = 10 took 4.5 h (UNSAT above),
weak (5,6) k = 14 at ~20 min per CEGAR round after 67 rounds, strong (5,6) k = 13 > 30 min in one round. T3 at n = 5 is
untested. A weak (5,5) separator with 10 states would have certified a gap (w = 10 < 11 ≤ s); it does not exist (solver-only).
A gap now needs s ≥ 12 (strong k = 11 UNSAT) and a weak separator with 11 states.
Observation (DATA, not a conjecture to pursue): every computed strong V value fits s^V(n,2h−1) = s^V(n,2h) =
n + (h−1)(n−1) (n ≤ 4, h ≤ 3), which predicts s^V(5,5) = s^V(5,6) = 13. The formula is polynomial in n at d = n, so
by L4 (s^V(n,n) ≥ n^Ω(lg n)) it must fail for large n: the computable cells are pre-asymptotic for s^V, and the same
caution applies to any equality w = s found there.

Lemma P (padding; 2026-10-22, L-STRUCT, elementary, unrefereed; used by experiments/weak-sep/n5.py to read one
query at k on its own). If a deterministic safety automaton A with k' states, all reachable, is a weak (strong)
(n,d)-separator, then for every k ≥ k' there is one with exactly k states, all reachable. Proof: by induction it is
enough to go from k' to k'+1. Fix a BFS spanning tree of A's transition graph from the initial state. A accepts the
infinite paths of the nonempty even graphs, so A has an infinite run, so its transition graph has a cycle and therefore
a transition p -a-> q that is not a tree edge. Add a copy q' of q with δ(q',b) = δ(q,b) for all b, and redirect
δ(p,a) := q'. Tree edges are unchanged, so every old state stays reachable, and q' is reachable through p. The states q
and q' accept the same words from there on, so the language (the set of accepted infinite words) is unchanged; both the
weak and the strong condition depend only on the language. Consequence: the encoding's BFS symmetry breaking forces all k
states reachable, and still "SAT at k ⟺ value ≤ k", so "UNSAT at k" gives value ≥ k + 1 without the lower k.

## 3. Mechanism: why the gap appears only when d is large against n (structural core; hypotheses, testable)
Fact M0 (elementary, to be written up with S3's proofs). In a word of OddCycles^X_{n,d}, every window of n
  consecutive letters contains a factor whose maximum is odd (n edges visit n + 1 vertices, so one repeats; the closed
  part is a cycle, its maximum is odd); dually every n-window of a word of EvenCycles^X_{n,d} contains a factor with even
  maximum [R7: windows of n letters, not n + 1; only this version gives the n = 2 instance]. For n = 2 this is "no two consecutive odd letters in even words, no two consecutive even letters in odd
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

## 4c. T3's sub-lemma (R2, statement only; Lead's ask 21:35Z) and the probes behind it
Probe data (experiments/weak-sep/probe_oddcycles.py, probe_rewire.py, probe_rule.py, 2026-10-14):
- Weak separators WITH a reachable odd simple cycle exist at d ≤ n+1 in both conventions, at minimum size and above:
  E (2,3) k=3 (= w), (3,3) k=6, (3,4) k=6; V (2,2) k=3, (2,3) k=3 (= w), (3,3) k=5 (= w), (3,4) k=5 (= w), (3,4) k=6,
  (4,4) k=8. None at E (2,2) k ≤ 3, E (3,3) k=5, E (3,4) k=5, E (4,4) k=8, V (2,2) k=2, V (4,4) k=7. So "weak = strong
  as objects" fails at d ≤ n+1 in E as well; T3 is a size statement only (dead ends SL1, SL5, SL5' in the notebook).
- Rewiring (probe_rewire.py: SAT for a STRONG (n,d)-separator with the same k states differing from the weak witness
  in ≤ t transitions): at d ≤ n+1, t = 1 in all nine instances above (eight times a letter-2 transition, once letter 1;
  the new target is a self-loop in four cases, another state in five), even when the witness has 2 or 3 odd simple
  cycles. At the gap cells (2,6) E and (3,6) V no strong separator within t ≤ 6 exists (as w < s there).
- The naive explicit rule "redirect the smallest-even-letter transition of an odd cycle to a self-loop" is NOT the
  mechanism: it removes all odd cycles but breaks (W1) in 7 of 8 instances (probe_rule.py); "redirect to the cycle's
  entry state" loops. The solver's t = 1 rewire is a different transition or target each time. Dead end recorded.

Sub-lemma SL8-t (Hamming form; the working statement, confirmed by the Lead 21:43Z after L-STRUCT's correction). Let
X ∈ {E, S, V}, n ≥ 1, 1 ≤ d ≤ n + 1, and let A be a deterministic weak (n,d)-separator of convention X with state set Q
and initial state q0. Then there is a deterministic strong (n,d)-separator of convention X with the same Q and q0 whose
transition function differs from A's in at most t(n,d) pairs (state, letter), for a bound t(n,d) to be determined;
a constant t is a hypothesis to test, not an assumption (Lead 21:43Z). Observed t_max per cell over ALL enumerated weak
separators (results/sl8/): E (2,2): 1 (k ≤ 4); E (2,3): 3 (k = 4); E (3,3): 1 (k ≤ 6, capped); E (3,4): 1 (k ≤ 6,
capped); V (2,2): 2 (k = 4); V (2,3): 4 (k = 4); V (3,3): 4 (k = 6, capped); V (3,4): 2 (k ≤ 6, capped). At minimum
size k = w: t_max = 1 in E and 2 in V on these cells.
SL8-t ⇒ T3 (w^X(n,d) ≥ s^X(n,d) for d ≤ n+1; the other inequality is S1 F1). Without the Hamming bound the statement
("some strong separator on the same abstract state set") is trivially equivalent to T3 and carries no proof idea; the
bound is what the local-rewiring proof would establish. SL8-1 (t = 1) is FALSE above minimum size: at E (2,3) with k = 4,
one of 1026 weak separators needs 3 changes, and at V (2,3) with k = 4 five of 4550 need 4 (exact; enumerate_weak.py).
Exhaustive test (Lead 21:40Z; results/sl8/, every weak separator with k reachable states up to BFS numbering, least t):
| cell, k | weak separators | t = 0 (strong) | t = 1 | t = 2 | t = 3 | t ≥ 4 |
| --- | --- | --- | --- | --- | --- | --- |
| E (2,2), k = 2 / 3 / 4 | 1 / 22 / 525 | all / all / 507 | - / - / 18 | | | |
| E (2,3), k = 3 / 4 | 11 / 1026 | 8 / 624 | 3 / 372 | - / 29 | - / 1 | |
| E (3,3), k = 5 / 6 | 16 / 4072 | all / 4020 | - / 52 | | | |
| E (3,4), k = 5 / 6 | 20 / ≥ 5000 (capped) | all / 4991 | - / 9 | | | |
| V (2,2), k = 2 / 3 / 4 | 1 / 24 / 609 | all / 22 / 507 | - / 2 / 99 | - / - / 3 | | |
| V (2,3), k = 3 / 4 | 28 / 4550 | 12 / 1075 | 12 / 2272 | 4 / 1059 | - / 139 | - / 5 (all t = 4) |
| V (3,3), k = 5 / 6 | 76 / ≥ 5000 (capped) | 65 / 3432 | 10 / 1356 | 1 / 172 | - / 39 | - / 1 (t_max 4) |
| V (3,4), k = 5 / 6 | 407 / ≥ 5000 (capped) | 365 / 3384 | 36 / 994 | 6 / 622 | | |
Reading: at MINIMUM size (k = w, the only case T3 needs) every weak separator is within t ≤ 2 of a strong one (E: t ≤ 1;
V: t ≤ 2), and most are strong outright. Above minimum size the distance grows (t = 4 at V (2,3) k = 4), so a universal
small t is the wrong form; the T3-relevant statement is SL8-min: for every MINIMAL deterministic weak (n,d)-separator at
d ≤ n+1 there is a strong one on the same states within t = 2 changes. No weak separator without any strong rewire
exists, of course (T3 holds on these cells by the table), so the test cannot refute T3 here; it bounds the mechanism.
Proof plan (statement-level): (1) from the lasso condition (Q3) and Fact M0 with windows of n letters, characterise
the tolerated odd simple cycles at d ≤ n+1: their lasso words are unrealisable with n vertices although every letter
≤ n+1 can occur; identify on such a cycle a transition τ = (q, e, q') with e even whose even-realisable use is
"replaceable"; (2) define the replacement target as the state the even-realisable continuations of q' are also safe
from (candidates: a state already reached by the same even-realisable prefixes with a larger pending odd letter, or q
itself); (3) show (W1) is preserved and every odd cycle through τ is destroyed, and that no new odd cycle appears;
(4) iterate; termination by a potential (number of odd simple cycles). Step (2) is the open core; the next data step
is to list ALL t = 1 rewires per instance (not just one) and read the rule off them, in the E convention first where
the strong side has the universal-tree structure.
Rule data at MINIMUM size (experiments/weak-sep/probe_rules_min.py, results/sl8/rules_min_*.json; every non-strong
minimal weak separator of the cell, all single-transition rewires to a strong separator): E (2,3) k=3: 3 non-strong, all
have a single rewire; V (2,3) k=3: 16 non-strong, 12 have one; V (3,3) k=5: 11, 10 have one; V (3,4) k=5: 42, 36 have one.
Every working single rewire lies on an odd simple cycle of the weak automaton (no exception). In almost all cases the
rewired transition carries the even letter 2 (twice letter 1, once to ⊥), it is the cycle's "return" edge (the
transition that, after the odd maximum p has been read, leads back towards the state where p was read), and the new
target is a state further along the cycle or the source itself (self-loop). The minority with no single rewire need
exactly two changes (SL8-min bound t = 2 holds on all four cells).
First proof step to attempt (SL9, hypothesis read off the data): let A be a minimal deterministic weak (n,d)-separator,
d ≤ n+1, and C a reachable odd simple cycle of A with maximum p (odd); call a transition (q, e, q') of C with e even
an ascent of C if, in the (yet to be defined) level order induced by p on the states of C, q' lies closer to the
state where p is read than q does. SL9: redirecting one ascent of C to the state of C that follows q' (or to q) preserves
(W1) and (W2), destroys C and every odd simple cycle through that transition, creates no new odd simple cycle, and keeps
determinism and the state set; iterating over the odd cycles terminates. What is missing is the definition of the level
order without assuming a tree decomposition (which only strong separators have); the candidate is CDFJLP's resistance
computed in the sub-automaton of letters ≤ p after deleting the ascents themselves, which is finite exactly when the
ascents are the only transitions closing odd cycles. The statement SL9 is where the proof attempt starts. Lead's caution (21:46Z) for the proof: minimality is global, so a
local rewiring argument must use it through a contrapositive of the form "if no strong rewire exists within t changes
at some odd cycle, then two states can be merged or one removed without breaking (W1)/(W2)", contradicting k = w; if the
argument needs only a weaker hypothesis than minimality (e.g. "no two states are equivalent on even-realisable
words"), that weaker form is to be stated instead. L4 is signed by the first referee (referee 9bf5301).
Alternative route if (2) fails: a direct size argument (injective leaf map from a universal-tree-like structure built
from even-realisable words), S3 §4b R2 as before.

## 5. Calibration
- Everything above the diagonal (n = 2, d ≥ 5; n = 3, d ≥ 5) is about letters a TARGET game of that size cannot have.
  The only algorithmically meaningful numbers so far are W(n) = S(n) for n ≤ 4.
- A polynomial W(n) would contradict nothing known (S1 F3, F5 are strong or time-bounded), but no mechanism for it is
  visible in the data: the weak savings so far come from odd cycles whose lasso words need more than n vertices, and
  on the diagonal the solver found none.
- Timestamps in L-STRUCT's earlier messages of this day ran ahead of UTC by up to 90 minutes (clock not consulted);
  the SHAs are authoritative.
