# S5: weak versus strong separators, where the strong lower bound breaks and three bridges tested (L-STRUCT, 2026-10-22)

Theory box after the n = 5 box (Lead GO 13:25Z, notebook queue 2). Status labels: PROVED (proof here, unrefereed),
DATA (computed, reproducible, no proof), DEAD (refuted, instance named), READING (my interpretation of a source).
Conventions and names: S1 (definitions D1-D5, Lemma 2), S3 (T3, Lemma P), S4 (facts F1-F11). A weak separator is
deterministic throughout. "Cycle" means a cycle of the reachable transition graph through non-rejecting states.

## 0. The question and its status in the literature
Can deterministic weak separators beat L4 (s^V(n,n) ≥ n^Ω(lg n), RESULTS R1)? This is the open question CDFJLP ask
(arXiv 1807.10546v2 §6, verbatim): "We leave open the question whether a stronger version of our main technical result
holds, namely whether every safety automaton separating EvenCycles_n from OddCycles_n has at least quasi-polynomial
number of states. Our argument cannot be directly extended to that setting, as already the proof of Lemma 5.2 crucially
relies on that fact that no word from LimsupOdd is accepted." L-LIT T4 (docs/lit/T4-weak-separators.md) found it open.

## 1. Where strongness enters the CDFJLP proof (READING of 1807.10546v2 §5, opened 2026-10-22, pdftotext)
Thm 5.1 follows from Lemma 5.1, proved by Lemma 5.2 (every accessible strong separator has a tree decomposition D:
quasi-orders ⪯_1 ⊆ ⪯_3 ⊆ ... ⊆ ⪯_{d+1} with Conditions 1-3) and Lemma 5.3 (for every D, the D-tree is
(n, d/2)-universal). Strongness is used at one point only, in Lemma 5.2: "there cannot be any odd cycle in A_{e,2i+1} ...
Notice that this is exactly the point in the proof of Lemma 5.2 where we need the assumption about rejecting all the
words from LimsupOdd_d. Rejecting all the words from OddCycles_{n,d} would not be sufficient". The proof of Lemma 5.3
(Claim 5.1) uses only (i) a non-rejecting run of A on α_t, a path word of the even graph G_t with n vertices, and
(ii) Conditions 1-2 of D on the transitions of that run.

## 2. Tree decompositions are exactly strongness (PROVED)
Lemma TD. An accessible deterministic safety automaton A over Σ_d (d even) has a tree decomposition iff no cycle of A
has odd maximum (equivalently, iff A rejects every word of LimsupOdd_d).
Proof. (⇐) is Lemma 5.2 (its proof uses exactly "no cycle with odd maximum inside A_{e,2i+1}"). (⇒) Let C be a cycle
with odd maximum p. Every transition (s, a, s') of C has a ≤ p. If a < p, Condition 1 with 2i+1 = p (a < p ≤ d+1) gives
s ⪰_p s'; if a = p, Condition 2 with 2i+1 = p gives s ≻_p s'. C contains a transition with letter p, so going around C
gives s ≻_p s for some s, a contradiction. The equivalence with LimsupOdd: an accepted word with odd limsup p has a run
whose infinitely visited part contains a closed walk with maximum p, hence a cycle with odd maximum, and conversely a
reachable cycle with odd maximum p yields the accepted lasso word π(P)·π(C)^ω, whose limsup is p. ∎
Consequence. Any transfer of Thm 5.1 to a weak separator W must run Lemma 5.3 on a sub-automaton B of W that contains
the runs on all words α_t (one B, one D for all trees t: the D-tree must contain every t), and by Lemma TD B must have
no cycle with odd maximum.

## 3. Bridge 1: the CDFJLP words avoid the tolerated odd cycles (Prop. W PROVED; hypothesis UG DEAD)
Let U_G(W) be the set of transitions W takes on paths (from any vertex) of the graphs G_t of CDFJLP §5.2, t an ordered
tree with exactly n leaves, all at depth d/2 (convention E, d even).
Prop. W. If W is a weak (n,d)-separator in convention E and U_G(W) has no cycle with odd maximum, then
|W| ≥ C(⌊lg n⌋ + d/2 − 1, ⌊lg n⌋).
Proof. Let B be W restricted to the transitions U_G(W) (all others to ⊥), on the states they reach from q0. B accepts
every path word of every G_t: W does (W1, G_t is even with n vertices) and the run uses only U_G(W). B is accessible
(its states are reached by such runs). By Lemma TD, B has a tree decomposition D. CDFJLP's proof of Lemma 5.3 applies
verbatim to B and D: it uses a non-rejecting run on α_t (exponent |A| replaced by |W| ≥ |B|, which only lengthens the
blocks; "at most |A| − 1 decreases" holds with |B| ≤ |W|) and Conditions 1-2 on that run. So tree_D(B) is
(n, d/2)-universal and its leaves inject into B's states (CDFJLP §5.2), giving the bound of Thm 5.1 for |B| ≤ |W|. ∎
Hypothesis UG ("U_G(W) has no cycle with odd maximum" for minimal, or all, weak separators; tested below and at
the T3 cell (3,4), d = n+1) — DEAD on data
(experiments/weak-sep/ug_test.py, results/partition/UG_E_*.json; every strong separator passes, as Lemma TD says):
| cell (E) | k | weak | non-strong | UG holds on non-strong |
| --- | --- | --- | --- | --- |
| (2,4) | 3 (= w) | 13 | 3 | 0 |
| (2,4) | 4 (capped 5000) | 5000 | 1867 | 99 |
| (2,6) | 3 (= w) | 2 | 2 | 0 |
| (3,4) | 5 (= w) | 20 | 0 | - |
| (3,4) | 6 (capped 5000) | 5000 | 9 | 0 |
Instance: E (2,4) k = 3, δ = [[1,0,1,0],[⊥,2,⊥,0],[1,0,⊥,0]] (rows = states, columns = letters 1..4). Control: the
4-state weak (2,10) E separator (results/external/lcomp_weak_E_n2_d10_k4.json) is below the Prop. W bound
C(1+5−1, 1) = 5, so UG must fail on it; it does. Obstruction: the paths of the G_t already drive a minimal weak
separator around its tolerated odd cycles; the odd cycle is traversed by an even word whose graph path is not closed.

## 4. Bridge 2: same partition of the even prefixes (DEAD)
For automata A, B let R(A,B) = {(δ_A(u), δ_B(u)) : u a finite word read along a path of an even graph with ≤ n vertices}.
Hypothesis: for every minimal weak W at d ≤ n+1 there is a minimal strong S with R(W,S) a bijection (W and S split the
even prefixes identically; W would be S with only its odd behaviour changed). DEAD
(experiments/weak-sep/prefix_partition.py, results/partition/{V,E}_*.json; all minimal weak and strong separators
enumerated, complete):
| cell | k = w = s | weak | non-strong | strong | non-strong W with a bijective S |
| --- | --- | --- | --- | --- | --- |
| V (2,3) | 3 | 28 | 16 | 12 | 1 |
| E (2,3) | 3 | 11 | 3 | 8 | 0 |
| V (3,3) | 5 | 76 | 11 | 65 | 1 |
| V (3,4) | 5 | 407 | 42 | 365 | 2 |
| E (3,3) | 5 | 16 | 0 | 16 | - |
Instance: V (2,3), W = [[1,1,1],[2,1,⊥],[⊥,0,⊥]]: |R(W,S)| ≥ 5 > 3 for all 12 minimal strong S. With S4 F7 (a strong
separator within Hamming distance ≤ 2 on the same states always exists), the picture is: minimal weak and strong
separators are close as transition tables but induce different partitions of the even prefixes, so a
state-counting argument that reads only even runs does not see which one it is counting.

## 5. Bridge 3: short lassos force strongness (PROVED; elementary, cf. S1 Q3 / S4 F3)
Lemma SL. In conventions E and V, if W is an accessible weak (n,d)-separator and C is a reachable cycle with odd maximum
reached by a simple path P disjoint from C except its end, then |P| + |C| ≥ n + 1. Hence a weak separator with at most
n states is strong.
Proof. The lasso graph (a path of |P| vertices into a cycle of |C| vertices, labels copied from the run; in V each
vertex carries the letter read when leaving it) has one cycle, whose maximum is odd: it is an odd graph with |P| + |C|
vertices, and its infinite path from the first vertex reads π(P)·π(C)^ω, which W accepts. If |P| + |C| ≤ n this
contradicts (W2). A cycle with odd maximum contains a simple one with the same maximum, and with k ≤ n states
|P| + |C| ≤ k ≤ n. ∎ This is the cheap filter of S4 F3/M1 written as a lemma; it only reaches k ≤ n, far below w.

## 6. The s^V formula (DATA conjecture with its range, and why it must fail)
Observation S^V. On every computed cell, s^V(n, 2h−1) = s^V(n, 2h) = n + (h−1)(n−1).
Range (experiments/weak-sep/results/table.md, convention V, all exact): n = 1 (d = 1..4): 1; n = 2: d = 1..6 and d = 8
(2, 3, 4, 5 for h = 1..4); n = 3: d = 1..6 (3, 5, 7); n = 4: d = 1..6 (4, 7, 10). At n = 5 only s^V(5,5) ≥ 11 is known
(prediction 13). Not checked: any n ≥ 5 value, n = 3 or 4 with h ≥ 4, d = 7 at n = 2.
Why it fails asymptotically (PROVED from L4). At d = n the formula gives n + (⌈n/2⌉ − 1)(n − 1) < n². L4 (L4-proof.md,
RESULTS R1; Corollary L4.3, last inequality) gives s^V(n,n) ≥ B(n) := (√n/(2 lg n))^{⌊½ lg n⌋ − 2} for n ≥ 64. The formula at d = n is at most (n² + 1)/2.
For n ≥ N1 = 2 240 573: lg n ≥ 21, so the exponent is ≥ 8 and the base is ≥ 1, hence B(n) ≥ n^4/(256 lg^8 n); this
exceeds (n² + 1)/2 at N1 and the ratio n^4/(256 lg^8 n) : (n² + 1)/2 increases for n ≥ e^4. The value n = 2 240 572 is
checked directly (B = 2.51008057·10^12 > formula 2.51008032·10^12); at n = 2 240 571 the bound does not yet exceed the formula. (experiments/weak-sep/l4_vs_formula.py.) So the formula is false for every n ≥ 2 240 572 at d = n: the computed cells are pre-asymptotic. The same caution applies to
weak values: equality w = s on small cells says nothing about the growth of w.

## 7. What is left, stated as targets
- T5 (weak transfer of Thm 5.1): find a sub-automaton B of every weak (n,d)-separator W that accepts a family of even
  words rich enough for Lemma 5.3 (a universal family of trees) and has no cycle with odd maximum. §3 shows the CDFJLP
  family itself is too rich (B = U_G(W) has odd cycles); a thinner family must keep universality while avoiding the
  tolerated odd cycles, whose lassos are all longer than n (Lemma SL).
- T6 (fooling sets for safety automata): a lower bound by pairwise distinguishable even prefixes u_i, with the right
  notion for weak separators: for i ≠ j some y with u_j·y ∈ OddCycles_{n,d} and every finite prefix of u_i·y extendable
  to a word of EvenCycles_{n,d} (L-COMP's version required u_i·y ∈ EvenCycles itself, which is impossible because both
  words share the tail's limsup: notes/L-COMP.md 2026-10-14). Not computed.
Neither target is in reach of the data tools at n ≥ 5 (S3 §2: n = 5 queries take hours per k).
