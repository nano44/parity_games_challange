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
