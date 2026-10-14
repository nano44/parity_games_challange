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

## 3. What the failures have in common; the class psolB solves (T-A1, proof in docs/attr/TA1-proof.md, not refereed)
Mechanism (read off the minimal instance and HKP Fig. 6). A fatal (layered) attractor certifies a region by "from every
target the owner forces a return to the target set through colours of the current layer". An attractor decomposition
(D1) has a second way to win: the opponent is TRAPPED in a sub-dominion S_i of lower top priority and never returns. The
solvers see a trap only if the owner can still force a return from it. In the minimal instance Odd's dominion is
A = {v1} (top priority 3) with the sub-trap S_1 = {v0} (self-loop, priority 1): from v1 Odd cannot force a return to v1
(Even can stay on the loop), and from v0 Odd cannot force a return to v0 through the layer of colour(v0) (the path v0 v1 v2 v0
crosses priority 2, excluded from that layer). Each piece needs the other: a mutual escape between the top attractor and a
sub-trap. HKP Fig. 6 is the same shape one level up (A = {v0,v5,v6,v7}, S_1 = {v2,v3,v4}, escapes v0 -> v1 -> ... -> S_1 and
v4 -> v5 -> A).

Three predicates on the two winning regions, in increasing strength (exact definitions: hypotheses.py, peeling.py, TA1-proof.md
section 1; "trap for the opponent in R" = DJT's trap: the opponent's vertices keep all R-edges inside, the owner's keep one):
- PA (closed traps): a DJT decomposition in which every S_i, at every level, is a trap for the opponent in the level's whole
  subgame R (the definition only asks for a trap in the remainder G_i).
- PA* (peeling): traps are peeled BEFORE the level's top attractor: S_1 a trap in R, A_1 = Attr(S_1), S_2 a trap in R \ A_1, ...,
  and finally the rest R_l equals its own attractor to the top priority. S_i may escape into earlier pieces only.
- PA** (mixed order, "peelable"): at each level, repeatedly remove either a self-returning top set (a non-empty X of top
  priority d from which the owner forces a revisit of X seeing only priorities <= d, with its monotone attractor and
  attractor) or the attractor of a closed sub-trap (a trap for the opponent, priorities <= d-2) that is itself peelable.
Data (hypotheses.py, peeling.py, pastar_fails.py, pa2_fails.py; outputs in experiments/attr/results/):
| implication | n = 3 (all 41,440) | n = 4 | n = 5 |
| --- | --- | --- | --- |
| PA => psolQ, psolB solve | holds | holds (30,000 random; PA false on all 75,856 psolQ failures of the 27.3 M enumeration) | holds (4,500 random) and n = 6 (600) |
| PA* => psolQ, psolB solve | holds | holds (20,000 random; PA* false on all 75,856 failures) | - |
| PA** => psolQ, psolB solve | holds | holds (2 x 20,000 random; PA** false on all 75,856 failures) | holds (1,500 + 3,000 random) |
| psolB solves => PA** | holds | holds (2 x 20,000) | holds (1,500 + 3,000) |
| psolQ solves => PA** | fails (3,016) | fails | fails |
| PA => PA* => PA** | holds | holds | holds |
| Büchi, deterministic ⊆ PA* | holds (7,840 / 4,144 games) | holds (sample) | - |
| SCC-constant ⊆ PA* | FAILS (708 of 11,872) | fails | - |
| Büchi, SCC-constant, deterministic ⊆ PA** | holds | holds | holds |
| canonical rules decide PA*, PA** | greedy sound, incomplete (4,266 misses) ; greedy2 sound, incomplete (48) | same | same |
Correction (L-LIT T8, docs/lit/T8-TA1.md): the first version of this section said PA "should contain" HKP's Thm 7 and Thm 8
classes; it does not. L-LIT's witness instances/llit_witness_buchi_n3.pg (v pr1 -> v; x pr2 Odd -> v; w pr1 Even -> w,x) is
Büchi and SCC-constant, solved by all three HKP solvers, and PA is false on it (checked; PA* and PA** are true on it).
The SCC-constant witness against PA* is "0 3 0 0; 1 1 0 0; 2 1 0 0,2" (all Even; Odd wins all): psolB decides the top
attractor {v0,v1} first and the sub-trap {v2} after, the order PA* forbids.

Theorem T-A1 (statement in TA1-proof.md section 2; proof there, both directions; gaps G1-G8 listed):
  psolB solves G completely  <=>  PA**(G);  and PA**(G) => psolQ solves G completely (strict: HKP Fig. 4(a)).
Corollaries: HKP Thm 7, Thm 8, Lemma 5 are the special cases where the certificate is found by HKP's own arguments (they
follow from the "only if" direction); PA**-membership is decidable in O(|V|^2 |E|) by the theorem; PA ⊊ PA* ⊊ PA**.
What T-A1 says about the failures: a game is left undecided by psolB exactly when some level of every decomposition of some
winning region has no piece that can go first: no top set that returns to itself and no closed sub-trap. That is the
"mutual escape" of the minimal instances, now as a theorem rather than a reading.
Exact class of psolQ: not attempted (its analogue of PA** with layered attractors in clause (a) would be definitional).
Dead variants: PB, PD (section 5); the greedy canonical rules for PA* and PA** (sound, not complete; instances in results/).

## 4. Position (TARGET section 4, L-LIT T7 part (c))
- Nothing here is M4 or M4-R. T-A1 is an exact characterisation of psolB's complete class (HKP's class Solved, Def. 8, which
  HKP call semantic but do not characterise; Ah-Fat-Huth 2016 name 2-player completeness classes as open, docs/lit/T8-TA1.md).
  Under ruling L8 (docs/DECISIONS.md): PA** is a structural condition on attractor decompositions, and its membership is
  decidable in polynomial time, but only via the theorem itself (run psolB); whether that counts as "a new polynomial
  class" or "a tighter analysis of a known algorithm" is the Lead's/owner's call. The value is that it names exactly what
  fatal attractors cannot do, and it gives HKP's three classes one common reason.
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
