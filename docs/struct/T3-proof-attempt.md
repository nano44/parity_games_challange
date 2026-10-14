# T3 proof attempt via SL8-min (L-STRUCT, 2026-10-14): status = OBSTRUCTED at Lemma C (reported, not switched)

Lead's requirements (21:50Z): (1) every step a proof or a numbered gap; (2) every lemma tested on the enumerated automata
before use, failures to Dead ends with the instance; (3) stop and report if Lemma C's minimality step fails; no E-only
switch without the Lead. Data: experiments/weak-sep/test_lemmas.py over all non-strong minimal weak separators stored in
results/sl8/rules_min_*.json (E (2,3) k=3: 3; V (2,3) k=3: 16; V (3,3) k=5: 11; V (3,4) k=5: 42; 106 odd simple cycles,
64 working single rewires); output results/sl8/lemma_tests.json. Vocabulary: S1, S3 (D6, SL8-min, SL9).

## 0. Statement attempted
SL8-min. Let X ∈ {E, S, V}, n ≥ 1, 1 ≤ d ≤ n+1, and A a deterministic weak (n,d)-separator of convention X with k = w^X(n,d)
states (minimal). Then there is a deterministic strong (n,d)-separator of convention X on the same states and initial
state differing from A in at most 2 transitions. SL8-min ⇒ T3 (w ≥ s at d ≤ n+1).

## 1. Lemma A (return edges): as first stated, FALSE on data; restated as A'
A (as sketched 22:35Z): every reachable odd simple cycle C with maximum p contains an even-letter transition τ = (q, e, q'),
e < p, such that A − τ restricted to letters ≤ p has no cycle through a p-transition of C.
Data: holds for 104 of 106 odd simple cycles. Fails for the two cycles consisting of a single odd self-loop (V (2,3) k=3,
δ(2,1) = 2 in two automata): no even letter at all. Dead end D-A (notebook). The working rewires there change the odd
letter itself (δ(2,1): 2 → 1, i.e. letter 1 leaves the loop).
A' (restated, holds on all 106 data cycles; proof = GAP 1): every reachable odd simple cycle C with maximum p either (i)
contains an even-letter transition τ with letter e < p whose removal breaks every cycle through C's p-transitions inside
the ≤ p sub-automaton, or (ii) consists of odd letters only; in case (ii) C is a single odd self-loop or an all-odd cycle,
and the working rewire moves one of its odd transitions.
Why (i) should hold at d ≤ n+1 (sketch, GAP 1): C^ω's lasso words are unrealisable by odd graphs with ≤ n vertices
(S1 Q3). If C had no even letter below p that "returns" to the p-reading region, C's word would be p followed by letters
that an n-vertex odd graph can realise as a cycle (all letters ≤ n+1 available, M0 with n-windows), contradiction. The
step "the only way to be unrealisable is an even return below p" is unproved; it is exactly what the two all-odd
instances violate at the level of the statement, so A' needs its own argument for case (ii).

## 2. Lemma B (tree-likeness after deleting return edges): holds on data except the all-odd case; proof = GAP 2
B: there is a set R of even-letter transitions lying on odd simple cycles such that A − R has no reachable odd simple
cycle; then, by CDFJLP's Lemma 5.2 argument applied to A − R (its proof uses only "no odd cycle in A_{e,2i+1}"), A − R
admits a tree-decomposition (Conditions 1-3 of CDFJLP §5.1), i.e. the quasi-orders ≤_{2i+1} exist on all states, with
Conditions 1-2 holding for every transition of A except those in R.
Data: least |R| = 1 for all 71 of 72 automata (even those with 2 or 4 odd simple cycles: one deleted even transition kills
them all); the remaining automaton is an all-odd-cycle case (|R| undefined, case (ii) of A'). Proof of existence of R in
case (i): A' gives one τ per cycle; that the SAME τ serves all cycles (|R| = 1 on data) is unexplained (GAP 2a); that the
deletion leaves no odd cycle anywhere (not only through C's p-transitions) is GAP 2b.

## 3. Lemma C (the rewire): target rule FALSE on data; minimality step NOT REACHED
C (as sketched): redirect the return edge τ = (q, e, q') to the next state of C after q' or to q; (W2) preserved because
the new target is deeper in the ≤_p order; (W1) preserved or minimality violated.
Data on the 64 working single rewires: new target = source q (self-loop) 16 times, = successor of q' on the cycle 6
times, = some OTHER state 42 times (e.g. the predecessor of q on the cycle, or a state off the cycle); the rewired letter
is the smallest even letter of the cycle 57 times. So the target rule "next or self" is wrong in two thirds of the
instances. Dead end D-C1 (notebook). What the data support instead: C' (GAP 3): for the return edge τ there EXISTS a
target q'' with q'' ≥_p q' in the order of Lemma B (not shallower) such that the redirected automaton still satisfies
(W1); the choice of q'' is instance-specific.
Minimality step (requirement 3): to prove C' one needs: if no such q'' exists then A is not minimal (two states mergeable
or one removable). I could not formulate this contradiction: the candidates q'' are distinguished from q' by even-
realisable words, and a minimal automaton may legitimately have pairwise even-inequivalent states; nothing forces a
redundant state. The step is therefore NOT PROVED and NOT REFUTED: it is unformulated. Per requirement (3) this is the
stop point. I did not switch to an E-only argument.

## 4. What stands, what is dead, what is next (for the Lead and the two referees)
- Stands (data-backed, unproved): SL8-min with t = 2 on all 8 enumerated cells; A' (i)/(ii); B with |R| = 1.
- Dead (with instances, notebook): Lemma A as stated (all-odd self-loop, V (2,3) k=3, δ = [[1,0,1],[⊥,2,⊥],[2,2,⊥]]);
  Lemma C's target rule (42 of 64 rewires use another target; e.g. V (3,3) k=5, δ = [[1,0,1],[2,3,2],[⊥,3,⊥],[4,3,⊥],[2,0,⊥]],
  rewire δ(4,2): 0 → 3, the predecessor of 4 on the cycle).
- GAPS: 1 (A' proof), 2a/2b (B), 3 (C' existence and the minimality contradiction).
- Possible next moves (Lead's call): (a) find the target rule from the 64 rewires by expressing q'' in the Lemma-B order
  (compute the quasi-orders of A − R for each instance and locate q'' relative to q, q'); (b) replace minimality by a
  concrete structural hypothesis that the data satisfy (e.g. "A − R is a tree-like automaton whose D-tree is
  (n, ⌈d/2⌉)-universal", which is where CFGO/CDFJLP structure would re-enter and which L-COMP's cells could test);
  (c) park T3 and return to the computational frontier ((5,5), (5,6) V).

## 5. Outcome of the Lead's move (a) (21:53Z, time-boxed): necessary rule found, no sufficient rule → outcome (ii)
Method (experiments/weak-sep/target_rule.py, target_rule2.py): for each non-strong minimal weak separator with a single
even-letter deletion R killing all odd cycles (71 of 72; the all-odd case excluded), CDFJLP's resistance quasi-orders
were computed on A − R exactly as in their Lemma 5.2 (per odd letter p from the top, within each class of the coarser
order, resistance = maximal number of p-letters on paths of the ≤ p sub-automaton; SCC-based, finite since A − R has no
odd cycle); rank(s) = the tuple of resistances, lexicographic, smaller = deeper (fewer p's still readable). Every working
single rewire (q, e, old → new) with e even and new ≠ ⊥ (57 (q,e)-groups, 58 rewires) was located in this order.
Results:
- NECESSARY RULE NR (holds on all 57 groups, no exception): rank(q) ≤ rank(new) < rank(old), or new = q. In words: the
  return edge's target is moved strictly deeper than the old target but never deeper than the source; the rewired edge
  stops ascending above its source yet still points at or above the source's level. Relative to old, new is deeper in
  49 of 58 rewires and equal in 8 (the 8 "equal" are exactly the groups with an empty interval, where new = q).
- NO SUFFICIENT RULE: the interval I(q,e) = {x : rank(old) > rank(x) ≥ rank(q)} contains non-working states in 41 of 49
  non-empty cases (working ⊇ I in 16 only); the shallowest state of I works in 40 of 49, the deepest in 8 of 41, the
  source q in 16 of 57. Example where only one interval state works: V (3,3) k=5, δ = [[1,0,1],[2,3,2],[⊥,3,⊥],[4,3,⊥],
  [2,0,⊥]], return edge (4, 2, 0), ranks 0:(2,0) 1:(1,0) 2:(0,0) 3:(0,2) 4:(0,1); interval {1, 3, 4}; only 3 works.
- GAP 2a: the rewired transition is the Lemma-B deletion in 29 of 58 rewires only; "one deletion suffices" is not
  explained by the rewire choice.
Conclusion: (ii). NR turns GAP 3 into a precise existence statement — C'' : for the return edge τ = (q, e, old) there is
x with rank(q) ≤ rank(x) < rank(old) or x = q such that redirecting τ to x preserves (W1) — but it does not say which x,
and the minimality contradiction for "no such x" is still unformulated. Dead end D-C2 (no deterministic target rule
among: shallowest / deepest interval state, source, successor, predecessor).

## 6. (b) Structural hypothesis replacing minimality, with a test plan (not proved, per the Lead's instruction)
H-B (precise). Let X ∈ {E, S, V}, d ≤ n+1, and A a minimal deterministic weak (n,d)-separator of convention X. Then:
 (1) there is a single even-letter transition τ_0 on an odd simple cycle such that A − τ_0 has no reachable odd simple
     cycle (hence A − τ_0 is tree-like, CDFJLP §5.1, by their Lemma 5.2 argument);
 (2) with D the tree-decomposition of A − τ_0 by resistance, the D-tree of A − τ_0 is (n, ⌈d/2⌉)-universal in the sense
     of CDFJLP (every ordered tree with ≤ n leaves and height ⌈d/2⌉ embeds), hence |A| ≥ s^E(n, d) for X = E and, for
     X = V, |A| ≥ the least size of a tree-like V-separator with a universal D-tree;
 (3) (the rewiring form) for τ_0 = (q, e, old) some x with rank(q) ≤ rank(x) < rank(old) or x = q makes A with τ_0
     redirected to x a strong separator.
H-B(2) is the content: it says minimal weak separators carry the universal-tree structure in their even part despite the
odd cycle, which is why w = s at d ≤ n+1. If (2) holds, T3 for X = E follows from CDFJLP Lemma 5.3's universality
argument applied to A − τ_0 (the words α_t used there are even-realisable and their runs avoid τ_0?: GAP 4, to test) and
for X = V from the V analogue of Lemma 5.1 (open, but L4.1-type transfer gives the n/d-loss form).
Test plan (cheap, on existing data first, then L-COMP's cells): (T1) for each stored minimal non-strong weak separator,
compute A − τ_0 for the τ_0 of Lemma B, its D-tree (classes of the resistance orders), and test (n, ⌈d/2⌉)-universality
by brute-force embedding of all trees with ≤ n leaves (wsep/utrees.py embeds); record failures with instances. (T2) check
whether the runs of CDFJLP's words α_t (built from the trees with n leaves) avoid τ_0 in A, which is what GAP 4 needs.
(T3) at (4,5) V and (4,4) V, run T1 on every minimal weak witness the solver returns (enumeration with blocking clauses,
k = 10 and 7). (T4) at the gap cells (2,6), (3,6) V, run T1: H-B(2) must FAIL there (w < s), which calibrates the test.
A failure of T1 at any d ≤ n+1 cell kills H-B(2) and with it this route; a pass on all cells makes H-B(2) the statement
to prove, with the proof route "the even-realisable words of CDFJLP's G_t force the universal tree even in a weak
separator, because at d ≤ n+1 their runs never use the return edge".
