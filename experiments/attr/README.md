# experiments/attr (L-ATTR): attractor and dominion methods, polynomial partial solvers

Task A1 (docs/attr/A1-statement.md, results in docs/attr/A1-results.md): Strahler threshold of psolQ (Huth-Kuo-Piterman,
arXiv 1405.0386v2 Fig. 5) and of Algorithm 1 of arXiv 2511.03752 (experiments/m2/avh.py). Max-parity in/out everywhere.

| file | what |
| --- | --- |
| `psolq.py` | psolQ, faithful to HKP Fig. 5 / Def. 6 (line labels in notes/L-ATTR.md); partial output, witness strategies; exit 3 "UNDECIDED" |
| `psolb.py` | psolB (HKP Fig. 3) and psol (Fig. 2), same conventions; `--psol` for psol |
| `strahler.py` | exact Strahler number of a small game (DJT arXiv 2003.08627 section 2) by DP over subsets, plus brute force over all decompositions (`--brute`) and the d+2 sensitivity check (`--shift 2`) |
| `a1lib.py` | classify one game (psolQ/psolB/psol/Alg1 with soundness and verify.py strategy checks), canonical enumeration (successor orbits x owners x priority patterns), TARGET compression, shrinking |
| `validate.py` | statement section 5 step 3: HKP figures, M2 counterexamples, DP vs brute force, psolQ soundness on random games |
| `exhaustive.py` | statement step 4: every canonical game with n vertices; failures to `out/fail_n{n}.jsonl`, summary to `out/summary_n{n}.txt` (out/ is gitignored; the summaries and sample outputs are copied to `results/`) |
| `hypotheses.py` | predicates PA/PB/PD on attractor decompositions against the solvers' outcomes (section 3 of the results) |
| `instances/` | minimal failing games (PGSolver format) named in the results |
| `check.sh` | the < 1 min regression run by scripts/verify.sh |

Reproduce: `python3 validate.py` (2 min), `python3 exhaustive.py 3 --all-strahler` (seconds), `python3 exhaustive.py 4 --all-strahler --workers 3`
(about 30 min, 27.3 M games), `python3 hypotheses.py 3`, `python3 hypotheses.py 4 --sample 30000 --seed 4`.
