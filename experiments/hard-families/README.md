# M1: hard families
One folder per family (`<family>/README.md`: source, claim, targets, growth fit, sweep table, plot `sweep.png`).

| family | source | verdict |
| --- | --- | --- |
| [tc](tc/README.md) | src/tools/tc.cpp | CONFIRMED |
| [tc+](tc+/README.md) | src/tools/tc+.cpp | CONFIRMED |
| [counter_symsi](counter_symsi/README.md) | src/tools/counter_symsi.cpp | CONFIRMED |
| [counter_rr](counter_rr/README.md) | src/tools/counter_rr.cpp | CONFIRMED |
| [counter_dp](counter_dp/README.md) | src/tools/counter_dp.cpp | CONFIRMED |
| [counter_m](counter_m/README.md) | src/tools/counter_m.cpp | CONFIRMED for the priority-promotion family as measured |
| [counter_core](counter_core/README.md) | src/tools/counter_core.cpp | CONFIRMED |
| [counter_rob](counter_rob/README.md) | src/tools/counter_rob.cpp | CONFIRMED |
| [counter_ortl](counter_ortl/README.md) | src/tools/counter_ortl.cpp | CONFIRMED |
| [counter_qpt](counter_qpt/README.md) | src/tools/counter_qpt.cpp | SUPER-POLYNOMIAL JUMPS OBSERVED, CLASS OPEN |
| [recursiveladder](recursiveladder/README.md) | src/lib/generators/recursiveladder.ml (Python port: pgsolver_port.py) | CONFIRMED |
| [switchallexp](switchallexp/README.md) | src/lib/generators/policyiter/generators/switchallexp.ml (Python port) | CONFIRMED against the targeted algorithm, run through Python ports |
| [switchbestexp](switchbestexp/README.md) | src/lib/generators/policyiter/generators/switchbestexp.ml (Python port) | CONFIRMED against the targeted algorithm, run through Python ports |

Tools: `sweep.py` (generate, run with timeouts, check agreement and strategies, table + plot), `run_all.sh` (all
families, sizes, solvers), `pgsolver_port.py` (Python port of PGSolver's generators, line-cited; awaiting the
referee's line-by-line check), `families.py` (sources, claims, paper references: all papers awaiting source),
`verdicts.py`, `make_readmes.py`. Oink: github.com/trolando/oink @ 8fbf0a7; PGSolver: github.com/tcsprojects/pgsolver @ d3cd624.
Raw per-run data: `results/*.csv`.
