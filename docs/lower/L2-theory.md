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

## 3. Where the 7th gate comes from: owner classes (data, same encoding; cegar_owner.py, 2026-10-15)
Restrict Def. 1.4 to the 4-vertex games whose set of Even vertices is one of a list of masks (programs are vertex-anonymous,
R2, so a class and its relabellings cost the same). CEGAR against all games of the class, no smaller games:
| class of 4-vertex games | k = 5 | k = 6 | certificate |
| --- | --- | --- | --- |
| all vertices Odd (V_E = ∅) | UNSAT (200 games) | SAT, verified on all 810 000 games of the class | result_odd_k{5,6}.log |
| exactly one Even vertex | | UNSAT | core_oneEven_k6.json: 33 games, 132 vertices (minimised, 6 orders) |
| exactly one Odd vertex | | UNSAT | core_oneOdd_k6.json: 37 games, 148 vertices (minimised, 6 orders) |
| all vertices Even (one-player) | UNSAT (L1-report) | SAT (L1-report §3, the 6-gate chain) | min_b1_n4.json |
Reading: both pure classes cost 6 = 2n − 2 at n = 4; the 7th gate is a cost of MIXING ◇-vertices and □-vertices, and one
vertex of the minority owner already forces it. On both class cores the modal depth needed is again 4 (types per depth
3, 20, 106, 128, 129, 129, 129 and 4, 25, 80, 117, 126, 126, 126; W-mixed type pairs first separated at depth 5 or 6: none).
Also (tower.py, 942 s, 6 GB): the subset of 25 593 four-vertex games that realise the W-mixed type pairs first separated at
depths 4, 5, 6 (61 123 + 4 072 + 180 pairs of types) is UNSAT at k = 6 on its own (102 058 nodes, 21.2·10^6 clauses, 222 s).
The DRUP refutation of the 68-game core by Glucose 4 has 114 859 lines (63 298 learned clauses): a human proof cannot follow
the solver's route (§5).

## 4. n = 5: the gap persists (data; cegar5two.py, 2026-10-15)
**Claim C2 (B_2(5) ≥ 9; machine-checked).** No program with 8 Cpre gates outputs W_E on all two-player Büchi games with
≤ 5 vertices. Certificate: experiments/lower/b2_n5_k8.json, a successor-closed subset made of Q_3 (all bisimulation classes
of two-player games with ≤ 3 vertices), the 14 four-vertex games of the n = 4 core and 400 five-vertex games found by CEGAR
against random 5-vertex games (2·10^6 per round, 200 added per round; 3 rounds); 7 220 nodes, 5 708 440 clauses, UNSAT by
CaDiCaL 1.5.3 in 1 733 s (result_b2_n5_k8.log). Second solver: see §6. No full sweep is involved: an UNSAT core is a proof
regardless of how its games were chosen (projection, R6).
So B_2(5) − (2·5 − 2) ≥ 1, as at n = 4. Whether B_2(5) ≥ 10 (gap growing) is the question of the k = 9 run (§6).

## 5. Kill criterion and recommendation
(to be written)

## 6. Status lines
- C1 (B_2(4) = 7; 68-game certificate): data, four solvers; not refereed.
- C2 (B_2(5) ≥ 9; 414-game certificate): data, one solver (CaDiCaL); Glucose 4 re-solve running (result_verify_n5_k8.log).
- k = 9 at n = 5 (would give B_2(5) ≥ 10): running (result_b2_n5_k9.log).
- Lemma 2.1, 2.2: proved above (short); not refereed.
