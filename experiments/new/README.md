# experiments/new (L-NEW, (c) design lane)
| file | what |
| --- | --- |
| renum.cpp (+ vjfast_copy.cpp) | Box 1 (i): renumbering hill climb for S5 (zadeh) / S6 (cunningham); vjfast_copy.cpp is a verbatim copy of experiments/si/vjfast.cpp (sha1 af4f517) whose main is renamed. `g++ -O2 -std=c++17 -o renum renum.cpp` |
| run_renum.sh | sweep over the bench families; out/renum/summary.csv |
| anneal.cpp | C++ port of N1 (boost cpp_int, shifts for gamma = (2^j-1)/2^j); `g++ -O2 -std=c++17 -o anneal_c anneal.cpp`; xcheck_c.py: equal to anneal.py on 1,000 games (seed 21); rand_c.py: random-game agreement; run_anneal_c.sh: bench sweep; check_sol.py: Zielonka + verify |
| anneal.py | N1 DISC-ANNEAL (docs/new/N1-disc-anneal.md). Run with --nocompress (the candidate); default merges priorities (N1m). --check compares with Zielonka and verifies strategies; --j0 J ablation; --xcheck integer vs Fraction values |
| anneal_random.py | N1 vs Zielonka + strategy check on harness/gen.py corpora |
| anneal_adv.py | adversarial hill climb over small games (objective: N1 iterations or largest phase) |
| run_anneal.sh | N1 bench sweep with baseline (plain VJ switch-all) and ablation; out/anneal/summary.csv |
| delay.py, compress.py | delay transform (candidate N1 killer) and the merging step alone (confound check) |
| instances/ | pinned instances (check.sh) |
Instances for sweeps are generated into out/inst/ (gitignored) from experiments/si/gens.py, hard-families/pgsolver_port.py,
red/gens_red.py, si/gated.py and tools/oink/build generators; see the loops in notes/L-NEW.md.
