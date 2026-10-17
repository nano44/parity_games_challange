# experiments/lower: straight-line symbolic programs (L-LOWER, task L1)

Model: docs/lower/L1-statement.md. Report: docs/lower/L1-report.md. Fast regression: `check.sh` (run by scripts/verify.sh).
Needs numpy and python-sat (`pip install python-sat`); the harness (../harness) supplies pg.py and zielonka.py.

| file | what |
| --- | --- |
| `slp.py` | program representation, evaluator on pg.Game (bitmasks) and on a Struct (numpy); builders `buchi_unfold(n)` (Lemma 2.3) and `anp_symmetric(n, d)` (ANP ‖F‖_{U,V} with S_{n,h} trees, Transfer 2.4) |
| `games.py` | enumeration of all games with n vertices (priorities / owners given), packing into one Struct |
| `check_vs_zielonka.py` | both builders against the harness Zielonka on all games with n ≤ 4 (sampled where > 10^6) |
| `quotient.py` | bisimulation quotient Q_n of all pointed games with ≤ n vertices (partition refinement, vectorized); W via Zielonka on representatives |
| `satsearch.py` | exact B_1(n) by SAT on Q_n with CEGAR (successor-closed subsets); witness decoded and verified on all of Q_n |
| `bfssearch.py` | independent BFS over partitions (exact, doubly exponential; n ≤ 3) |
| `restricted.py` | minima under restrictions: window-w chains, monotone programs |
| `depthneeded.py` | minimal modal depth (W constant on depth-D types) |
| `fooling.py` | deepest fooling pairs (winning vs losing classes with equal depth-(2n−3) types) |
| `show.py` | prints a program as a chain of modal formulas with minimised Boolean arguments |
| `vec5.py` | vectorized evaluation on ALL k-vertex one-player Büchi games (packed masks); independent reference W by transitive closure, checked against Zielonka for k ≤ 4 |
| `cegar5.py` | n = 5: SAT candidates on Q_3 + counterexample games, verified on Q_4 and on all 916·10^6 five-vertex games |
| `cegar5b.py` | faster n = 5 variant: truth tables evaluated directly on all 5-vertex games (one lookup per gate), all 32 patterns per round, checkpoints `cegar5_<tag>.subset.json` (resumable) |
| `vec2.py` | two-player Büchi: all k-vertex games (k ≤ 4) vectorized, reference W = Lemma 2.3 unfolding (checked against Zielonka), table evaluation with inputs (P_2, V_E, s_j) |
| `sat2.py` | two-player: `exact n kmax` (SAT on Q_n) and `cegar4 k` (CEGAR against all 12 960 000 four-vertex games) |
| `depth2.py` | two-player minimal modal depth for n ≤ 4 (partition refinement over all (game, vertex) pairs) |
| `bits.py` | which gate outputs of a chain program determine W (minimal determining subsets) |
| `min_*.json`, `result_*.log`, `cegar5_*.json`, `b2_*.json` | witnesses, UNSAT cores and logs of the runs reported in docs/lower/L1-report.md and docs/lower/L2-data.md |
| `coremin.py`, `coremin2.py`, `coremin3.py`, `coremin_class.py` | T-L2 (docs/lower/L2-theory.md): UNSAT-core minimisation (greedy; assumption-based over Q_3 classes + games; over whole games under several deletion orders; for class cores) |
| `levels.py` | depth-j types of a core's vertices, W-mixed type pairs first separated at depth j (M_j), last-gate constraint |
| `tower.py` | depth-j types of ALL ≤ 4-vertex two-player games (as depth2.py), the M_j type pairs on the full class, SAT on the games realising M_jmin..M_6 (~16 min, 6 GB) |
| `prooftree.py`, `prooftree2.py`, `prooftree3.py`, `chainbfs.py` | case-tree enumerations of realisable profile partitions (general gates / window-1 chains) with refinement or exact pruning; used to measure the size of an enumerated proof |
| `towerproof.py` | type-form SAT (over-approximation: a set per type, not per profile) and DRUP proof-size measurement |
| `cegar_owner.py`, `sat_shape.py` | 4-vertex owner/priority/degree classes (`FILTER` env): CEGAR against all games of the class; exact SAT on a whole class with a prescribed gate reading shape |
| `cegar5two.py`, `verify_core.py` | n = 5 two-player: CEGAR at k gates against random 5-vertex games (an UNSAT core is a proof, a SAT candidate is not); re-solve a core with other solvers |
| `cegar_class5.py` | n = 5 localised class K_5 (one Even vertex of priority 1, Odd vertices, two priority patterns, out-degree 2): exact CEGAR against all 200 000 games of the class |
| `b2_n4_k6_core3.json` (68 games), `core_exact_k6.json` (28 games), `core_oneEven_k6.json`, `core_oneOdd_k6.json`, `core_d2221_k6.json`, `core_p13_k6.json`, `b2_n5_k8.json` (414 games, n = 5) | the UNSAT cores of L2-theory |

Reproduce: `python3 -I check_vs_zielonka.py`; `python3 -I satsearch.py 4`; `python3 -I restricted.py 4 8`;
`python3 -I depthneeded.py`; `python3 -I fooling.py`; `python3 -I cegar5b.py 8 0 12` (hours; caches W per priority pattern in $W5_CACHE);
`python3 -I sat2.py exact 3 8`; `python3 -I sat2.py cegar4 7 400` (minutes); `python3 -I depth2.py 4` (~15 min, ~6 GB).
T-L2: `python3 -I coremin2.py 6 b2_n4_k6_core_min.json x.json && python3 -I coremin3.py 6 x.json y.json 12` (< 10 min; 68 games);
`python3 -I cegar_owner.py 6 8 200 1,3` (one Even vertex, P_2 = {v0} or {v0, v1}: UNSAT); with
`FILTER="(deg(3)==2)&(deg(0)==2)&(deg(1)==2)&(deg(2)==2)"` the 2 592-game class whose 28-game core is core_exact_k6.json
(`python3 -I coremin_class.py 6 b2_n4_k6_ve8_p21-3_all2_exact.json core_exact_k6.json 8`); `python3 -I cegar5two.py 8 2000000 200 0`
(B_2(5) ≥ 9, ~35 min); `python3 -I verify_core.py b2_n5_k8.json 8 Glucose4`.
