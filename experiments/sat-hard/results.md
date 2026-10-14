# Results (in progress)

## Reproduction of L-STRUCT at 42dbbc2 (independent run, 2026-10-14)
- `experiments/weak-sep/check.sh`: ALL PASS (5 s).
- `bruteforce_k2.py`: no 2-state weak separator for n = 2, d in {5,6}, conventions E and V (59049 / 531441 automata
  each; 3 s, 37 s, 8 s, 108 s). Confirms w(2,5), w(2,6) >= 3 in E and V.
- Own encoder + checker (this folder) reproduce w(2,6)=3, w(3,6)=7, w(4,4)=8, and (4,4) k=7 UNSAT with a verified LRAT
  proof; (4,5) k=8 UNSAT in 84 s (L-STRUCT: 118 s).

## T1 REFUTED at (2,10): w(2,10) = 4 < 5 = s(2,8), in conventions E, S and V (2026-10-14 ~20:30Z)
T1 (L-STRUCT, as stated by the Lead): w(n,d) >= s(n,d-2). At n = 2, d = 10:
- **w(2,10) <= 4**: the 4-state weak (2,10)-separator `results/weak_E_n2_d10_k4.json` (found by search.py 2 10 4,
  delta[q][p-1], None = bottom, state 0 initial):
  ```
  delta(0,.) = [1, 0, 2, 0, 2, 0, 2, 0, 3, 0]
  delta(1,.) = [3, 2, 3, 2, _, 2, _, 0, _, 0]
  delta(2,.) = [1, 2, 3, 2, 3, 2, _, 0, _, 0]
  delta(3,.) = [_, 3, _, 1, _, 2, _, 2, _, 0]
  ```
  Verified three ways: (1) verify2.py, exhaustive and progress-measure-free: ALL inclusion-maximal even / odd E-graphs
  on <= 2 vertices (a 2-vertex graph is even iff all loops are even and max(a,b) is even for every 0->1 label a and
  1->0 label b), 11 even + 12 odd, no violation; (2) check.py against graphs.family(2,10) (5 even, 6 odd); (3)
  L-STRUCT's own checker (5e94874 wsep.automata.check_separator on its maximal_graphs for n = 1, 2): no violation.
  As S- and V-graphs are E-graphs, it is also an S and a V separator (checked: graphs.family_S / family_V, n = 1, 2).
- **s(2,8) >= 5** in E, S and V: strong k = 4 UNSAT (search.py 2 8 4 --strong [--conv S|V]); CaDiCaL LRAT proofs
  verified by lrat_check.py (2257 / 2441 / 3681 RUP steps) and CryptoMiniSat UNSAT on each CNF
  (results/sX_n2_d8_k4.cnf; E sha256 f453e181bdde3fe9...). k = 5 is SAT, so s(2,8) = 5 (E: = least leaves of a
  (2,4)-universal tree, CFGO, per L-STRUCT's table pattern h+1 for n = 2).
- Also w(2,10) >= w(2,8) >= 4 (monotone in d; (2,8) weak k = 3 UNSAT in E, S, V with verified LRAT proofs and
  CryptoMiniSat agreement, results/wX_n2_d8_k3.cnf): so w(2,10) = 4 exactly. And s(2,10) = 6 (k=5 UNSAT, k=6 SAT; no proof yet).
- (2,8): w(2,8) >= 4 = s(2,6) in E, S, V, consistent with T1 there.
Re-run: `python3 search.py 2 10 4` (SAT, < 1 s), `python3 search.py 2 8 4 --strong --cnf-out F.cnf`, then
`cadical --lrat=true --binary=false F.cnf F.lrat && python3 lrat_check.py F.cnf F.lrat`; `python3 verify2.py results/weak_E_n2_d10_k4.json`.

## New bounds (convention E, weak)
| cell | bound | evidence |
| --- | --- | --- |
| w(4,6) | >= 8 (no weak (4,6) E-separator with <= 7 states; supports L-STRUCT's T1 at (4,6): w >= s(4,4) = 8) | k=7 UNSAT: search.py 4 6 7 --cnf-out (12 graphs: 9 even + 3 odd; 11809 vars, 127565 clauses, 6 s); CaDiCaL LRAT proof (16 MB) verified by lrat_check.py (91568 RUP steps); CryptoMiniSat 5.11.15 UNSAT on the same CNF (10 s); L-STRUCT's encoder (5e94874) UNSAT at k=7 (11 s). CNF sha256 57c88533ff3b7949... Monotonicity in k covers k < 7. Elementary second route: a weak (4,6)-separator is a weak (4,4)-separator, so w(4,6) >= w(4,4) = 8, and (4,4) k=7 is UNSAT with a verified LRAT proof (this folder). |
| w(5,4) | >= 10 (so w(5,4) in {10, 11}, as s(5,4) <= 11 by CFGO's f recursion, L-STRUCT table) | k=9 UNSAT: search.py 5 4 9 --cnf-out (CEGAR, 12 even + 3 odd graphs, 18936 vars, 246419 clauses, 57 s); CaDiCaL 1.7.3 LRAT proof (162 MB, 76 s) verified by lrat_check.py (377764 RUP steps, 44 s). CNF sha256 493cd346a13eb259... |

Running: (4,5) k=9, (4,6) k=9 (UNSAT side), (4,6) k=12 (SAT probe), (5,4) k=10.

## Independent check of L-STRUCT's w^V(4,6) <= 11 (claude/l-struct 616cf77, weak_V_n4_d6_k11.json)
graphs.family_V (own generator: every tree with n leaves x every vertex labelling, brute-force parity check; covers all
V-graphs on n vertices up to subgraphs) for n = 1..4, d = 6: the 11-state automaton has NO violation (n = 4: 5007 even,
7752 odd graphs). It is not an E-separator (48 violated (4,6) E-graphs), as expected. Copy: out/ (not committed).

## Dead ends
- Pairwise-inconsistent words (clique.py): the inconsistency graph is EMPTY for every (n,d) tried ((2,5), (2,6),
  (3,5), (3,6), (4,3), (4,4)). Obstruction: u.y and v.y share the tail y, so their limsup parities agree; y cannot be an
  infinite path label of an even graph after u and of an odd graph after v. Pairwise prefix arguments can never
  separate states of a weak separator; lower bounds need joint (multi-word / n-bounded) reasoning.
- Simulated annealing (anneal.py) on the violated-graph count: stuck at 16 violations for (3,6), k = 7 (a 7-state
  separator exists). The landscape is too rugged; not usable for upper bounds.
- Pure lasso CEGAR (search.py --w2 lasso): instead of product ranks, each violated odd graph contributes only the
  constraint "A rejects u.v^w" for one lasso of the product (run simulated |u| + k|v| letters, must end in bottom).
  Valid, but each constraint removes few automata: no convergence within 120 s even for (2,6), k = 2.
- Binary ranks (search.py --w2 binary, lexicographic comparator, shared successor-rank bits): correct (reproduces
  w(2,6), w(3,6), w(4,4)) but UNSAT ~8x slower than unary: (3,6) k=6 13.7 s vs 1.7 s; (4,4) k=7 13.7 s vs 2.3 s.
  Unary (thermometer) ranks propagate a product cycle into a conflict directly; binary comparators do not.
- State merging (merge.py): no 2-state merge of the 4-state strong (2,6) separator is a weak separator although a
  3-state weak one exists, so the small weak separators are not quotients of strong ones; dropped.
