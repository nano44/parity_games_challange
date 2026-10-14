# A1 results: Strahler threshold of psolQ and of arXiv 2511.03752 Algorithm 1 (L-ATTR)
Statement: docs/attr/A1-statement.md (definitions D1-D4, questions Q1-Q3; definitions unchanged since 22:15Z 2026-10-14). Code and
data: experiments/attr/ (README there). Every solver output below was checked for soundness against harness Zielonka and
for positional strategies with experiments/harness/verify.py (restricted to the decided region for partial outputs).
Status: data + one theorem candidate with a proof sketch; NOT a result (no referee yet; TARGET section 5 step 4 pending).

## 1. Answers
- Q1: k(psolQ) = 0. Q2: k(Alg1) = 0. Both solvers fail on games of Strahler number 1, the minimum possible value
  (D2a: Str(G) >= 1 for every game). So "psolQ is complete exactly for Strahler <= k" is false for every k >= 1, and the
  same for Algorithm 1; the Strahler number does not measure what these solvers miss (section 4).
- Q3, psolQ: the minimal failing game has n = 3, m = 4 (exhaustive: every canonical game with n <= 2 is solved; the 8
  canonical failures with n = 3, m = 4 are one game up to the player swap and the owners of two irrelevant vertices).
  experiments/attr/instances/psolq_min_n3_m4.pg (TARGET priorities):
  ```
  0 1 0 0,1;    v0: priority 1, Even, edges to v0 (self-loop) and v1
  1 3 0 2;      v1: priority 3, Even, edge to v2
  2 2 0 0;      v2: priority 2, Even, edge to v0
  ```
  Odd wins every vertex (both cycles, v0v0 and v0v1v2, have odd top priority); Str = 1 (Odd tree <<>>: A = Attr_O({v1}) = {v1},
  S_1 = {v0}, A_1 = {v0, v2}). psolQ, psolB and psol decide nothing (HKP's three solvers); Algorithm 1 solves it.
- Q3, Alg1 (regions): no failure with n <= 3 (exhaustive, 41,440 canonical games, Zielonka-equal regions on all of them);
  minimal failure at n = 4 with m = 5 (exhaustive n = 4: every game with m = 4 is solved; 160 canonical games with m = 5 are
  WRONG, one successor shape with all 16 owner vectors and 10 priority patterns, all Str 1; the algorithm never gets STUCK
  on any n <= 4 game, its failures are always wrong regions). experiments/attr/instances/alg1_min_n4_m5.pg (TARGET priorities):
  ```
  0 1 0 1;      v0: priority 1, Even, edge to v1
  1 1 0 0,2;    v1: priority 1, Even, edges to v0 and v2
  2 3 0 3;      v2: priority 3, Even, edge to v3
  3 2 0 0;      v3: priority 2, Even, edge to v0
  ```
  Odd wins every vertex (cycles v0v1 and v0v1v2v3 both have odd top priority); Algorithm 1 gives all four to Even in one
  round (A(G,2) = V as an Even dominion: the Theorem 2 obstruction of M2); Str = 1 (Odd tree <<>>: A = {v2}, S_1 = {v0, v1}).
  psolQ and psolB leave it undecided; psol solves it (edge removal, HKP Lemma 1). The M2 counterexample ce1_4v.pg is another
  member of the m = 5 class.
- Alg1 versus psolQ at n = 4: all 10,428 wrong answers of Algorithm 1 are on games psolQ leaves undecided (no game is
  psolQ-solved and Alg1-WRONG), and all are at Strahler number 1. L-ATTR reading: Algorithm 1 is a psolQ-type solver that,
  where psolQ stops, declares a region instead of stopping.
- Reference games: HKP Fig. 6 (n = 8, "modified by neither psol, psolB nor psolQ") has Str = 1 (Even tree <<>>); the three
  M2 counterexamples (ce1, cex1, cex2; Alg1 WRONG) have Str = 1 and are left entirely undecided by psolQ, psolB and psol.

## 2. Data (experiments/attr/out/summary_n*.txt; failing games in out/fail_n*.jsonl, regenerable)
Canonical enumeration: successor structures up to isomorphism x all owner vectors x all priority patterns up to
order-and-parity equivalence (a1lib.py); both solvers and the Strahler number depend on priorities only through order and parity.
| n | games | psolQ undecided | psolB undecided | psol undecided | Alg1 WRONG / stuck | Alg1 BADSTRAT (L-COMP strategies S1-S2) | Strahler histogram |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 240 | 0 | 0 | 0 | 0 / 0 | 0 | all 1 |
| 3 | 41,440 | 44 (all Str 1) | 3,060 | 3,336 | 0 / 0 | 144 | 1: 41,062; 2: 378 |
| 4 | 27,331,200 | 75,856 (73,588 at Str 1, 2,268 at Str 2) | - | - | 10,428 / 0 (all Str 1) | 288,294 | 1: 26,632,540; 2: 698,660 |
(psolB/psol counted at n = 3 by hypotheses.py; n = 4 row filled from summary_n4.txt.)
Inclusions at n = 3 (all 41,440 games): psolQ solves every game that psolB or psol solves (no game is psolQ-undecided and
psolB- or psol-solved); psolB and psol are incomparable (152 games psol-only, 428 psolB-only), as HKP Example 5 says.

Validation (validate.py, full run 2026-10-14 22:22Z, PASS): HKP Fig. 6 untouched by psolQ, Fig. 4(a) and 4(b) decided by
psolQ, psolB/psol on Fig. 4 as HKP Example 5 states; Strahler DP = brute force over all decompositions on 600 random games
(n <= 6; brute n <= 5), DJT Prop. 3-4 bounds respected, D2a's d versus d+2: identical on all 600; psolQ sound with verified
strategies on 2,000 seeded random games with n <= 40 (undecided on 9 of them; Alg1 WRONG on 16, BADSTRAT on 94).

## 3. What the failures have in common; a sufficient condition (theorem candidate, proof sketch, not refereed)
Mechanism (read off the minimal instance and HKP Fig. 6). A fatal (layered) attractor certifies a region by "from every
target the owner forces a return to the target set through colours of the current layer". An attractor decomposition
(D1) has a second way to win: the opponent is TRAPPED in a sub-dominion S_i of lower top priority and never returns. The
solvers see a trap only if the owner can still force a return from it. In the minimal instance Odd's dominion is
A = {v1} (top priority 3) with the sub-trap S_1 = {v0} (self-loop, priority 1): from v1 Odd cannot force a return to v1
(Even can stay on the loop), and from v0 Odd cannot force a return to v0 through the layer of colour(v0) (the path v0 v1 v2 v0
crosses priority 2, excluded from that layer). Each piece needs the other: a mutual escape between the top attractor and a
sub-trap. HKP Fig. 6 is the same shape one level up (A = {v0,v5,v6,v7}, S_1 = {v2,v3,v4}, escapes v0 -> v1 -> ... -> S_1 and
v4 -> v5 -> A).
Predicates tested (hypotheses.py; "trap for the opponent in R" = DJT's trap: the opponent's vertices keep all R-edges inside,
the owner's keep one):
- PA: both winning regions have a decomposition in which every S_i, at every level, is a trap for the opponent in the
  level's whole subgame R (not only in the remainder G_i where the definition requires it).
- PB: as PA with "trap in R \ A". PD: a decomposition whose escape graph between the level's pieces A, A_1..A_l is acyclic.
| implication | n = 3 (all 41,440) | n = 4 (30,000 random canonical games) | n = 5 (4,500 random games, pa_sample.py, 2,954 PA-true) and n = 6 (600, 368 PA-true) |
| --- | --- | --- | --- |
| PA => psolQ solves completely | holds | holds; and PA is false on all 75,856 psolQ failures of the full enumeration, so it holds on all 27.3 M games | holds |
| PA => psolB solves completely | holds | holds | holds |
| PA => psol solves completely | fails (400) | fails (243) | - |
| PB => psolQ solves | fails (44) | fails (85) | - |
| PD => psolQ solves | fails (8) | fails (11) | - |
| psolQ solves => PA | fails (6,914) | fails (7,813) | - |
Theorem candidate T-A1 (sufficient condition; new as far as L-ATTR can tell, to be checked by L-LIT against HKP Thm 7
(Büchi), Thm 8 (SCC-constant colour), Lemma 5 (deterministic), which it should contain):
  "psolB, and psolQ, completely solve every parity game G such that each of W_E(G) and W_O(G) admits an attractor
  decomposition (D1) in which every trap S_i, at every level, is a trap for the opponent in the subgame being decomposed
  at that level."
Proof sketch (four lemmas). (L1, leaf) Let S be an innermost piece of such a decomposition for player p (its own
decomposition has l = 0, so S = Attr_p^S(P_q ∩ S) for its top priority q, pr(S) <= q), and S a trap for 1-p in the game
(by PA, inductively through the levels: a trap in R that is inside a trap in the parent is a trap in the parent). Then
X_0 = P_q ∩ S satisfies X_0 ⊆ MAttr_p(X_0, q) (HKP Def. 3; attraction through priorities <= q inside S), i.e. a fatal
attractor exists. (L2, monotonicity) MAttr and layeredAttr are monotone in the target set, so the greatest fixpoint of
psolB at colour q (resp. psolQ at the bound of colour q) started from X ⊇ X_0 never drops X_0: the solver decides a
non-empty set containing S. (L3, preservation) Removing the p-attractor of a p-won set keeps PA: the opponent loses
edges, p's vertices outside the removed set lose none, so the restricted decomposition stays valid and closed; the
other player's region is untouched. (L4) Induction on |V|. Gaps to referee: the precise statement of L3 (the restricted
chain S_i ∩ W' after larger attractors), and that the tree may change (irrelevant for completeness).
What PA is not: it is sufficient only (thousands of PA-false games are solved: the escape goes into a region decided
earlier, which the predicate does not see). An exact characterisation of psolQ's class is not attempted; PB and PD are
dead ends (section 5).

## 4. Position (TARGET section 4, L-LIT T7 part (c))
- Nothing here is M4 or M4-R. T-A1 would be an M3-type "characterisation of a partial solver" (L-LIT: low-medium value);
  the class PA is not a known parameter class, and its membership is as hard to decide as it looks (it quantifies over
  decompositions); the value is that it names exactly what fatal attractors cannot do.
- The negative answers are the rank-3 deliverable in its negative form: the Strahler number (branching of attractor
  decompositions, the parameter of the quasi-polynomial bounds, DJT Thm 32) is orthogonal to the failure of the fatal-attractor
  family: the family fails on chains (Strahler 1), on 1-player games (HKP Fig. 6; and the minimal instance is 1-player for Even),
  on dull games. 2511.03752's Algorithm 1 fails on Strahler-1 games with 4 vertices, i.e. its obstruction is the same
  trap-versus-return confusion (REFEREE's obstruction in docs/decisions/M2-arxiv-2511.03752.md: "the player avoids A' by never
  returning to U"), now placed in the family: the three M2 counterexamples are all psolQ-undecided.
- Side finding for L-COMP (not a finding against the paper, whose Algorithm 1 gives no strategies): avh.py's own strategy
  construction S1-S2 fails verify.py on 144 of the 41,440 canonical 3-vertex games although the regions are right;
  smallest: experiments/attr/instances/avh_badstrat_n3_m4.pg (v1 is sent to v0, closing the odd cycle v0 v1 instead of
  going to v2 of priority 4).

## 5. Dead ends (notes/L-ATTR.md has the instances)
- "Strahler threshold k >= 1" for psolQ or Alg1: dead (k = 0; instances section 1).
- PB and PD as the completeness condition: dead (counterexamples at n = 3: instances/psolq_min_n3_m4.pg satisfies PB and is
  undecided; instances/psolq_pd_n3_m4.pg (v1 owned by Odd) satisfies PD and is undecided).
- Strahler-2 failures exist from n = 4 on (2,268 of them); smallest: instances/psolq_str2_n4_m6.pg (Odd tree <<>,<>>: the minimal
  Strahler-1 instance with a second self-loop trap v3). They add nothing to the mechanism.

## 6. Gauntlet position (TARGET section 5)
Not an algorithm claim. For T-A1: step 1 (pseudocode of psolB/psolQ in notes/L-ATTR.md, implementation here) done; step 2
not applicable (partial solvers; soundness checked on 10^4+ games); step 3 L-LIT novelty check of T-A1; step 4 a written proof
of L1-L4 and a referee; Lean not required (not M4).
