# L2-data: two-player Büchi in the SLP model (L-LOWER, 2026-10-15; unrefereed)

Task from the Lead (07:50Z): measure B_2(n) (Def. 1.4 of docs/lower/L1-statement.md, restrictions R1-R6) for n ≤ 4 and
compare with B_1(n) = 2n − 2 (n ≤ 5, docs/lower/L1-report.md). Code: experiments/lower/vec2.py, sat2.py, depth2.py.

## 1. What CDHL prove for two-player Büchi games, and what it means for T-L2
- CDHL SODA 2018 (arXiv 1711.09148 v1, opened): no statement about two-player games at all. All objectives (§1 p.2-3, §3, §4)
  are defined on graphs ("Given a graph G = (V, E) and a starting vertex s ∈ V, let P_s be the set of infinite paths in G starting
  from s"); the word "game" occurs once, in the grant line (p.21). Theorem 3.10 (1), p.8: Ω(n) one-step operations for Büchi(T)
  on graphs; §4.2 p.10: Büchi(T) on graphs in O(min(SCC + D, |T|·D)) symbolic operations.
- CDHL CSL 2017 (arXiv 1706.04889 v1, opened 2026-10-15): the adaptive set-based model for PARITY GAMES (§2.2). Upper bounds:
  Theorem 20 (App. D.1, verbatim): "Algorithm ClassicParity computes the winning sets of parity games; ... as set-based
  symbolic algorithm it requires O(n^c) symbolic one step and set operations, and O(c) many sets"; Lemma 27 (App. D, verbatim):
  the big-step algorithm takes "O(n^2) symbolic one-step and set operations for c = 2". No lower bound for games is stated.
- Consequence in the anonymous model of Def. 1.3: for two-player Büchi (c = 2) the adaptive model has Ω(n) (one-player games
  are a subclass, Theorem 3.10 transfers as in L1 Transfer 2.2) and O(n^2) (CSL'17 Lemma 27), while the SLP model has
  2n − 2 ≤ B_2(n) ≤ n^2 (L1 Lemma 2.1', Lemma 2.3). T-L2 (B_2(n) = Ω(n^2/polylog n)) is neither implied nor excluded by
  CDHL: their two-player upper bound is the same n^2 as the SLP unfolding, and they have no two-player lower bound. Unlike the
  one-player case, where the adaptive model is O(n) and an SLP bound of ω(n) would separate the models, for two players the
  adaptive model itself is not known to be o(n^2); a quadratic SLP lower bound would be the first super-linear symbolic bound
  for Büchi games in any model, and would leave open whether adaptivity (vertex naming, Post) helps.

## 2. Measured values (exact; quotient-plus-SAT, W from the harness Zielonka; witnesses verified on all games of the size)
| n | B_1(n) (one-player) | B_2(n) (two-player) | minimal depth, two-player | method for B_2 |
| --- | --- | --- | --- | --- |
| 1 | 0 | 0 | 0 | SAT on Q_1 (4 classes) |
| 2 | 2 | 2 | 2 | SAT on Q_2 (76 classes): UNSAT at 1 |
| 3 | 4 | 4 | 4 | SAT on Q_3 (5164 classes): UNSAT at 3; witness verified on Q_3 |
| 4 | 6 | **7** | **6** (depth2.py on all 51 906 148 (game, vertex) pairs with ≤ 4 vertices: 1 120 780 depth-6 types, W constant on each; 90 mixed depth-5 types) | CEGAR: UNSAT at k = 6 on 400 games (result_b2_n4_k6.log); k = 7 SAT, verified on ALL 12 960 000 four-vertex games (vec2 reference = Lemma 2.3's unfolding, checked against Zielonka on all games with ≤ 3 vertices and 300 000 random 4-vertex games) and re-checked gate by gate against the harness Zielonka on 100 000 random games (result_b2_n4_k7.log, b2_n4_k7.json) |
| 5 | 8 | ≥ 8 (Lemma 2.1') | | not attempted (6.9·10^9 games; a sweep is ~ 1 h per candidate) |
Reading: two-player Büchi first exceeds the one-player minimum at n = 4, by one gate (7 versus 6 = 2n − 2), and this is NOT a
depth phenomenon: the minimal depth is 6 for two players as for one, so B_2(4) = 7 is the first exact data point where the
Büchi SLP cost strictly exceeds the depth lower bound. The obstruction family is the UNSAT core of k = 6: 400 four-vertex games
(b2_n4_k6.json) on which no 6-gate program is correct. Caveat on the pair B_1 = 2n − 2 (n ≤ 5) versus B_2(4) = 7: a single
point above the line; whether B_2(n) − B_1(n) grows is exactly T-L2's question, and n = 5 is out of reach for the present
sweep method (2.9·10^10 five-vertex two-player games; the one-player 9.2·10^8 took 7 min per sweep).

## 3. Status lines
- T-L1 (one-player, B_1(n) = ω(n)): data AGAINST (B_1 = 2n − 2 for n ≤ 5, exact), open, PARKED (Lead, 07:50Z).
- T-L2 (two-player, B_2(n) = Ω(n^2/polylog n)): data: B_2(1..4) = 0, 2, 4, 7 with minimal depth 0, 2, 4, 6; B_2(4) = 7 > depth = 6 =
  B_1(4); open. One point above the line is not a trend; n = 5 (B_2(5) ≥ 8) is not measurable by sweeping (2.9·10^10 games).
