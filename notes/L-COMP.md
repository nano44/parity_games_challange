# L-COMP notebook
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point
2026-10-14: branch claude/l-comp (from trunk claude/vibrant-johnson-nxvvxo). Oink 8fbf0a7 built by scripts/setup_oink.sh.
Task 2 (harness, experiments/harness/) done: py Zielonka + brute-force oracle, seeded generator, rngame corpus,
compare.py, check.sh (in verify.sh). Validation: experiments/harness/validation.md.
Task 3 (M1, experiments/hard-families/) in progress: sweep.py driver; PGSolver generators ported to
pgsolver_port.py (PGSolver binaries could not be run here, see Things only I know).
Task 4 (M2, arXiv 2511.03752): BLOCKED until the Lead says arXiv is reachable. Nothing implemented.

## Queue
1. M1 sweeps: tc, tc+, counter_symsi, counter_{rr,dp,m,core,rob,ortl,qpt}, recursiveladder, switchallexp, switchbestexp.
2. SI families target PGSolver's strategy-improvement variants, not Oink psi/ssi: port PGSolver's stratimprovement
   (switch-all / switch-best) from src/lib/solvers/stratimpralgs* to confirm the blow-up in the targeted algorithm.
3. M2 when unblocked.

## Things only I know
- PGSolver (tcsprojects/pgsolver d3cd624) builds with apt OCaml 4.14 + dune 3.14 after two local edits
  ((lang dune 3.18)->3.14, drop maintenance_intent) in a dune workspace with tcslib 6778419,
  ocaml-sat-solvers 0264291, c-cube/ocaml-minisat aeb7776 (all cloned under experiments/hard-families/out/pgsolver,
  gitignored). Running the built generator.exe was refused by this session's permission classifier ("code from
  external"), so the generators are ported to Python instead; the owner can allow running it, then the port can
  be diffed against the original output.
- Oink rngame is seeded from std::random_device: not reproducible; keep the files, not the parameters.
- Oink mspm (8fbf0a7) is unsound: logic error at mspm.cpp:486 on 3 rngame games, and on one game a wrong answer
  that Oink's own verifier rejects ("loser can escape"). Instances: experiments/harness/regressions/mspm_*.pg.
  Exclude mspm from any "all solvers agree" claim.
- Oink's work counters are solver-specific (iterations, promotions, lifts, major iterations); compare across sizes
  of one solver, never across solvers.

## Sources opened
| source (arXiv id / DOI) | result used (theorem / section) | opened on | note |
| --- | --- | --- | --- |
| github.com/trolando/oink @ 8fbf0a7 | solver list (README), generators src/tools/*.cpp, solution format src/game.cpp:459 | 2026-10-14 | code, not a paper |
| github.com/tcsprojects/pgsolver @ d3cd624 | generators recursiveladder.ml, policyiter/generators/*.ml; paritygame.ml conventions | 2026-10-14 | code, not a paper; papers awaiting source |

## Dead ends
(none)
