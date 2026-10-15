# L2-theory: why two-player Büchi on 4 vertices needs a 7th gate (L-LOWER, T-L2 theory box, 2026-10-15; unrefereed)

Model: docs/lower/L1-statement.md (Def. 1.3, R1-R6; B_2(n) of Def. 1.4). Data: docs/lower/L2-data.md (B_2(1..4) = 0, 2, 4, 7;
minimal modal depth 0, 2, 4, 6). Code: experiments/lower/ (README). Nothing here is a result in the sense of CLAUDE.md; every
"Theorem" below has a proof in this file, every data claim a SHA and a command. Status lines are in §6.

## 1. The certificate (data; what the SAT solver proves)
**Claim C1 (B_2(4) ≥ 7; machine-checked).** No program with 6 Cpre gates (any DAG of gates, Def. 1.3) outputs W_E on all of the
68 two-player Büchi games listed in experiments/lower/b2_n4_k6_core3.json (14 games with 4 vertices, 53 with 3, 1 with 2;
217 vertices in all). Since the 68 games are whole games (a successor-closed set), every program correct on all games with ≤ 4
vertices is correct on them (projection), so B_2(4) ≥ 7; with the 7-gate witness of L2-data (verified on all 12 960 000
four-vertex games) B_2(4) = 7.
- Encoding (experiments/lower/sat2.py `encode2`): gate i has a truth table over (P_2, V_E, s_1, ..., s_{i−1}) (this is the
  full model: Boolean gates are free, so the argument of the i-th Cpre is an arbitrary Boolean function of the base sets and
  the earlier Cpre gates); s_i(v) = OR (v ∈ V_E) / AND (v ∈ V_O) over the successors; the output is a truth table over
  (P_2, V_E, s_1, ..., s_6) and must equal W_E (from the harness Zielonka) at every vertex. 45 172 clauses, 3 112 variables.
- UNSAT by four solvers (CaDiCaL 1.5.3, Glucose 4, MapleChrono, Lingeling; 3-13 s each; python-sat 1.9.dev15).
- Provenance: the 400-game CEGAR core of L2-data (d00349a) → 100 games by chunked deletion (f0e5e8f) → with Q_3 (all
  two-player bisimulation classes with ≤ 3 vertices) as a side condition, assumption-based minimisation (coremin2.py:
  14 four-vertex games + 130 classes, fresh re-solve UNSAT) → classes replaced by their representative games and minimised
  again over whole games under 12 deletion orders (coremin3.py): 68 games every time (217 or 218 vertices).
  Reproduce (< 1 min): `python3 -I coremin2.py 6 b2_n4_k6_core_min.json x.json && python3 -I coremin3.py 6 x.json y.json 12`.
  The plain greedy deletion with Q_3 kept (coremin.py, 35 min, result_coremin_greedy.log) also ends at 14 four-vertex games.

**What the certificate looks like (measured, levels.py / the script in §1 of notes).**
- No game of the core is one-player: every one of the 68 games has an Odd vertex (4-vertex games by number of Odd vertices:
  1: 1, 2: 5, 3: 7, 4: 1; 3-vertex games: 1: 17, 2: 30, 3: 6). One-player Büchi on ≤ 4 vertices is solved by 6 gates
  (L1-report §3), and the one-player part of any core is satisfiable at 6; the 7th gate is forced by Odd vertices only.
- All 14 four-vertex games are uniform: W_E = V or W_E = ∅ on each of them.
- The modal depth needed on the core is 4, not 6: the depth-j bisimulation types of the 217 vertices number 4, 43, 153, 180,
  181, 181, 181 for j = 0..6, and W_E is constant on depth-4 types. Of the W-mixed pairs of types first separated at depth
  j there are 253, 197, 17, 1, 0, 0 for j = 1..6. So on the core a program of depth 4 (with many gates) exists, and the
  obstruction is NOT depth: it is the width of the model, one bit per Cpre gate.

## 2. Two lemmas about the shape of a 6-gate program (proved here)
Notation: for a program P and a vertex v, the i-profile π_i(v) = (P_2(v), V_E(v), s_1(v), ..., s_i(v)) ∈ {0,1}^{i+2}.

**Lemma 2.1 (one bit per gate).** s_i(v) is determined by the owner of v and the SET of (i−1)-profiles of the successors of
v: s_i(v) = [∃ w ∈ E(v): π_{i−1}(w) ∈ F_i] if v ∈ V_E and [∀ w ∈ E(v): π_{i−1}(w) ∈ F_i] if v ∈ V_O, where F_i ⊆ {0,1}^{i+1}
is the set of profiles on which the Boolean argument of the i-th Cpre is true. Proof: the argument of Cpre_E(X_j) is a
Boolean combination of base sets and earlier Cpre gates, i.e. a function of π_{i−1}; Def. 1.2. ∎
Consequently P is determined, on any class of games, by the sequence F_1, ..., F_k and the output function, and two
programs with the same i-profile PARTITION of the vertices of a game class have the same options from level i on.

**Lemma 2.2 (tower).** If P has k Cpre gates and depth k, then its Cpre gates can be ordered so that gate i has depth
exactly i and its argument depends on s_{i−1}. If moreover W_E is not constant on the depth-(k−1) types of some game
class, every k-gate program correct on that class has depth k (L1 Lemma 1.6), hence is such a tower. ∎
For n = 4 two-player Büchi the minimal depth is 6 (L2-data; depth2.py; 90 W-mixed depth-5 types among all 51 906 148
(game, vertex) pairs), so every 6-gate program correct on all games with ≤ 4 vertices is a tower, and its LAST gate alone
must separate every one of the 90 mixed depth-5 types (all earlier gates are constant on a depth-5 type).
Caution: Lemma 2.2 is about the full class. On the 68-game core alone depth 4 suffices (§1), so a 6-gate program correct on
the core need not be a tower; Claim C1 is nevertheless about all DAGs (the encoding is general).

## 3. Where the 7th gate comes from: localisation to a 2 592-game class (data; cegar_owner.py, sat_shape.py, 2026-10-15)
Restrict Def. 1.4 to a class of 4-vertex games (programs are vertex-anonymous, R2, so a class and its relabellings cost
the same; a class needing 7 gates is a lower bound for every superclass, a class solved by 6 says nothing about superclasses).
Each line below is one CEGAR run against ALL games of the class (no smaller games), log result_*.log, core b2_n4_k6_*.json.
Notation: e = the Even vertex, a, b, c = the Odd vertices; "pattern {a}" means P_2 = {a}.
| class of 4-vertex games | games | 6 gates | note |
| --- | --- | --- | --- |
| all vertices Odd | 810 000 | SAT (5: UNSAT) | pure □; like the pure-◇ one-player class (L1-report: 6) |
| exactly one Even vertex (any priorities, any edges) | 3 240 000 | UNSAT | core_oneEven_k6.json: 33 games, 132 vertices |
| exactly one Odd vertex | 3 240 000 | UNSAT | core_oneOdd_k6.json: 37 games, 148 vertices |
| one Even vertex e, ONE priority pattern (each of {a}, {e}, {a,b}, {a,e}, {a,b,c}, {a,b,e}, {a,b,c,e} separately) | 50 625 each | SAT | every single pattern is solved by 6 |
| one Even vertex, all patterns with |P_2| = 1; all with |P_2| = 2 | 202 500; 303 750 | SAT; SAT | |
| one Even vertex, patterns {a} and {a,b} (e ∉ P_2) | 101 250 | UNSAT | two patterns suffice; also {a} and {b,c} |
| one Even vertex, patterns {e}, {a,b}, {a,c}, {b,c}; patterns {a}, {b}, {c}, {a,e}, {b,e}, {c,e} | 202 500; 303 750 | SAT; SAT | e ∈ P_2 in some of the patterns: 6 suffice |
| patterns {a}, {a,b}; every out-degree ≤ 2, e of out-degree 2 | 12 000 | UNSAT | |
| patterns {a}, {a,b}, any out-degrees, no self-loop anywhere | 4 802 | SAT | loops are needed |
| the bounded-degree class above with no loop at e; no loop at a; no loops at b, c | 6 000; 7 200; 4 320 | SAT | loops at e, at a and at b or c are all needed |
| **K**: patterns {a}, {a,b}; EVERY vertex has out-degree exactly 2 | 2 592 | UNSAT | core_exact_k6.json: 28 games, 112 vertices |
| K with out-degree of c = 1 instead (a, b, e of out-degree 2) | 1 728 | UNSAT | core_d2221_k6.json: 32 games |
| out-degrees (e, a, b, c) = (2, 2, 1, 1); K with a loop at e in every game | 1 152; 1 296 | SAT | |
**The count of priority-2 vertices (all 16 owner patterns allowed; cegar_owner.py with all masks; result_all_*.log).**
| 4-vertex games by |P_2| (any owners, any edges) | games | 6 gates |
| --- | --- | --- |
| |P_2| = 1 | 3 240 000 | SAT (5: UNSAT) |
| |P_2| = 2 | 4 860 000 | SAT |
| |P_2| = 3; |P_2| ≤ 1; |P_2| ∈ {0, 3} | 3 240 000; 4 050 000; 4 050 000 | SAT |
| |P_2| ∈ {1, 3}; {2, 3}; {1, 4}; {2, 4}; {3, 4} | 6 480 000; 8 100 000; 4 050 000; 5 670 000; 4 050 000 | SAT |
| |P_2| ∈ {1, 2} | 8 100 000 | UNSAT (contains K) |
Reading: of all pairs of counts, ONLY {1, 2} forces the 7th gate. A vertex-anonymous program cannot count P_2 (R2); for
every class with a single count, or with any pair of counts other than {1, 2}, 6 gates suffice; serving |P_2| = 1 and
|P_2| = 2 by one program costs the 7th. (Why {1, 2} and not {2, 3} is not understood.)
Reading (data, no theorem): both pure classes cost 6 = 2n − 2; the 7th gate is a cost of MIXING ◇-vertices and
□-vertices, one minority vertex is enough, and it needs two priority patterns at once (a program for a fixed pattern exists
with 6 gates, but no single 6-gate program serves {a} and {a,b} together), self-loops, and branching (out-degree 2) at
every vertex. On the class K a 7-gate WINDOW-1 CHAIN exists (sat_shape.py: `chain` shape, k = 7: SAT; 6: UNSAT), so the
7 gates can be a tower s_i = Cpre_E(f_i(P_2, V_E, s_{i−1})) of depth 7, with W_E a function of (P_2, V_E, s_1, ..., s_7).
On K the modal depth needed is 4 (types per depth 3, 15, 195, 1451, 2591, 2827, 2827, 2827; W-mixed type pairs first
separated at depth 5, 6, 7: none); on its 28-game core also 4.
Smallest certificates found: 28 whole games (112 vertices); 97 bisimulation classes (qmin.py: quotient of K, 2 827
classes, assumption-based minimisation over classes with successor closure, 8 orders, fresh re-solve UNSAT:
qcore_exact_k6.json); on that 97-vertex structure the smallest set of (winning, losing) vertex pairs that 6 gates cannot
separate simultaneously has 53 pairs (pairmin.py, 6 orders, all 53).

## 3b. The obstruction to a human-readable proof (what was tried; the honest state of goal (a))
A proof "read out of the core" must refute every 6-gate program on the certificate. Three mechanical routes were measured:
1. The solver's own refutation: DRUP proof of the 68-game core by Glucose 4: 114 859 lines, 63 298 learned clauses.
2. Enumeration of realisable profile partitions level by level (prooftree2.py; Lemma 2.1 makes the partition the only
   state), with the sound "r rounds of refinement must separate W" pruning: 15 partitions after gate 1, 2 555 after gate 2,
   none dead; the tree explodes at level 3. With exact pruning (prooftree3.py, remaining gates decided by SAT) the tree is
   trivial (the root is already dead) and the leaf reasons are SAT calls, i.e. nothing is explained.
3. The same enumeration restricted to window-1 chains on the 28-game core K (chainbfs.py): live partitions per level
   7, 132, 2 177, 8 561, 486, 0 (choices examined: 8, 166, 10 030, 296 477, 1 696 465, 111 232). The chain-only refutation
   alone needs thousands of cases, and the theorem is about all DAGs.
Also measured: the depth-forcing subset (tower.py; the 25 593 four-vertex games realising the W-mixed type pairs first
separated at depth 4, 5, 6) is UNSAT at 6 on its own (102 058 nodes, 21.2·10^6 clauses, 222 s), so a proof that starts
from Lemma 2.2's tower structure on the full class and forces the sets F_6, F_5, ... top-down has a certificate; but the
forcing is not unit propagation: on the 68-game core the last gate alone has > 1000 admissible F_6 (levels.py), the
constraints bind only jointly across levels.
Conclusion for goal (a): the certificate is minimal in three senses (68 games with 12 deletion orders; 28 games of the
class K; 97 bisimulation classes; 53 pairs) and verified by four solvers, and the mechanism is LOCALISED (§3: mixing of
owners, two priority patterns, loops, branching), but no proof short enough to be read by a human was found. What a human
can check by hand is §2 (Lemmas 2.1, 2.2) and the class table of §3; the refutation itself remains a SAT certificate.
This is recorded as the obstruction to (a), not as a theorem.

## 4. n = 5: the gap persists (data; cegar5two.py, 2026-10-15)
**Claim C2 (B_2(5) ≥ 9; machine-checked, two solvers).** No program with 8 Cpre gates outputs W_E on all two-player Büchi
games with ≤ 5 vertices. Certificate: experiments/lower/b2_n5_k8.json, a successor-closed subset made of Q_3 (all
bisimulation classes of two-player games with ≤ 3 vertices), the 14 four-vertex games of the n = 4 core and 400 five-vertex
games found by CEGAR against random 5-vertex games (2·10^6 per round, 200 added per round, 3 rounds); 7 220 nodes,
5 708 440 clauses; UNSAT by CaDiCaL 1.5.3 in 1 733 s (result_b2_n5_k8.log) and by Glucose 4 in 3 009 s
(result_verify_n5_k8.log; `python3 -I verify_core.py b2_n5_k8.json 8 Glucose4`). No full sweep is involved: an UNSAT core
is a proof whatever the origin of its games (projection, R6). The core is not minimised (one UNSAT call costs ~30 min).
**Claim C2' (the count mechanism persists at n = 5; machine-checked, one solver).** Restricted to games with |P_2| ∈ {1, 2}
(any owners, ≤ 5 vertices), 8 gates still do not suffice: cegar5two.py with P2SIZES=1,2 (subset: Q_1, the four-vertex core
games with |P_2| ∈ {1, 2}, and 5-vertex games with |P_2| ∈ {1, 2} sampled at random), UNSAT at round 4 on 612 games
(3 052 nodes, 2 422 688 clauses, 2 036 s; result_b2_n5_k8_p2sz1-2.log, b2_n5_k8_p2sz1-2.json).
**Claim C3 (single count costs exactly 2n − 2 at n = 5; machine-checked).** The class of two-player Büchi games with ≤ 5
vertices and exactly ONE priority-2 vertex is solved by 8 Cpre gates: the CEGAR candidate b2_n5_k8_p2sz1_candidate.json
(19 rounds, 3 415 games) was verified on ALL 4 580 664 160 five-vertex games of the class (sweep_p2.py: 5 priority masks ×
32 owner masks × 31^5 successor assignments, 0 failing, 5 738 s, result_sweep_p2sz1_k8.log), on all 3 248 306 games of the
class with ≤ 4 vertices (0 failing), and gate by gate against the harness Zielonka on 20 000 random 5-vertex games of the
class (0 mismatches; decoded program: cost 8, depth 8, 13 815 Boolean gates). The lower bound 8 is Lemma 2.1' (its lasso pair
has one priority-2 vertex). So at n = 5, as at n = 4: one count of priority-2 vertices costs 2n − 2, the two counts {1, 2}
together cost ≥ 2n − 1.
So B_2(5) − (2·5 − 2) ≥ 1, as at n = 4: the gap does not close. Whether it GROWS (B_2(5) ≥ 10) is the k = 9 run (§6).

## 5. Goal (b): a family, and what is and is not known about growth
**The family K_n (parametrised; from the localisation of §3).** Vertices e, a, b, c_1, ..., c_{n−3}; e ∈ V_E with
priority 1, all other vertices Odd; pr(a) = 2, pr(b) ∈ {1, 2} (two patterns), pr(c_i) = 1; every vertex has exactly two
successors. |K_4| = 2 592 and K_4 needs 7 gates (§3). |K_5| = 200 000 and **K_5 needs ≥ 9 gates**: cegar_class5.py (exact
CEGAR against the whole class, no sampling), UNSAT at k = 8 on 1 000 games of K_5 (5 000 nodes, 3 950 000 clauses, 1 625 s;
result_k5_deg2_k8.log, k5_deg2_k8.json; one solver). So the family's cost exceeds 2n − 2 at n = 4 and n = 5 (by ≥ 1
each); K_5 at k = 9 is in §6. Lower bounds on K_n are lower bounds on B_2(n) (R6).
**What is known.** B_2(n) − (2n − 2) ≥ 1 for n = 4 (exact: = 1) and n = 5 (C2). The mechanism is the same at both sizes
(§3 count table at n = 4; C2', C3 at n = 5): a single count of priority-2 vertices costs exactly 2n − 2, the counts 1 and 2
together cost ≥ 2n − 1. Programs are vertex-anonymous (R2) and cannot count; the extra gate pays for not knowing |P_2|. The depth lower bound 2n − 2 (Lemma
2.1') is attained by the modal depth on the full class for n ≤ 4; on the hard classes of §3 the depth needed is only 4, so
the extra gate is a WIDTH cost: one Cpre gate carries one bit about the set of successor profiles (Lemma 2.1), and the
games of K force two incompatible one-bit tests at the same level (data: a single priority pattern is solved by 6 gates,
two patterns are not).
**What is not known (the obstruction to (b)).** No argument that the gap is unbounded was found, and none that it is
bounded. A proof of growth needs, for each n, a reason why Θ(n) levels of the tower each need a second bit, or why some
level needs n^ε bits; the n = 4 reason itself has no short proof (§3b), so there is nothing to parametrise. The natural
candidate measure (the number of W-mixed pairs that one gate must separate at a level, divided by what one bit can do) does
not give a bound: the last gate alone always has many admissible choices (levels.py: > 1000 on the 68-game core); the
constraints bind only jointly. Data that would decide the direction cheaply: B_2(5) ≥ 10 (k = 9, running) would make the
gap 1, ≥ 2 at n = 4, 5; a SAT answer at 9 with a full sweep (2.9·10^10 games, ~1 h per candidate) would make B_2(5) = 9
and the gap constant on the data, i.e. T-L2 (quadratic) would then stand against two points, not one.

## 5b. Kill criterion (notes/L-LOWER.md, verbatim: "if by hour 6 the n=4 argument is not written (step 2) or the family at
n=5 gives no bound above 2n-2 = 8 for two-player (i.e. SAT finds 8-gate programs for every hand-built family), stop, record
the dead end with the instances, and recommend parking the lane") and recommendation
- First clause: FIRES. The n = 4 human-readable argument is not written; the obstruction is recorded in §3b with the
  instances (b2_n4_k6_core3.json, core_exact_k6.json, qcore_exact_k6.json, qcore_exact_k6_pairs_k6.json).
- Second clause: does NOT fire. n = 5 gives B_2(5) ≥ 9 > 8 on the general class (C2, two solvers), not by a hand-built
  family but by CEGAR against random games; the hand-built family K_5 is in §6.
- Recommendation (L-LOWER): park the theory goal (a human proof of B_2(4) = 7) as a dead end of this method; keep T-L2 as
  an open data question with one cheap decisive experiment (k = 9 at n = 5) and one expensive one (full sweep of a 9-gate
  candidate). Do not spend referee time: nothing here is a theorem beyond Lemmas 2.1, 2.2, and the data claims C1, C2 are
  SAT certificates (CHECKER-reproducible: C1 in seconds, C2 in ~1 h).

## 6. Status lines
- C1 (B_2(4) = 7; 68-game certificate, 28-game class certificate): data, four solvers; not refereed.
- C2 (B_2(5) ≥ 9; 414-game certificate): data, two solvers (CaDiCaL, Glucose); not refereed.
- k = 9 at n = 5 (would give B_2(5) ≥ 10): RUNNING at the time of writing (result_b2_n5_k9.log; seeded with the k = 8 core).
- K_5 at k = 8: UNSAT (K_5 needs ≥ 9; §5). K_5 at k = 9: RUNNING at the time of writing (result_k5_deg2_k9.log).
- C3 (|P_2| = 1 at n = 5 costs exactly 8): data, full sweep of the class (4.58·10^9 games) plus all smaller games; not refereed.
- Lemma 2.1, 2.2: proved above (short); not refereed.
- Goal (a) human-readable proof: NOT achieved; obstruction in §3b. Goal (b) growth argument: NOT achieved; §5.
