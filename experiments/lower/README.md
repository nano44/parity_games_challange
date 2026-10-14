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
| `min_*.json`, `*.log` | witnesses and logs of the runs reported in docs/lower/L1-report.md |

Reproduce: `python3 -I check_vs_zielonka.py`; `python3 -I satsearch.py 4`; `python3 -I restricted.py 4 8`;
`python3 -I depthneeded.py`; `python3 -I fooling.py`; `python3 -I cegar5.py 8 1` (hours; caches W per priority pattern).
