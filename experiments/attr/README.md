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
| `peeling.py` | PA* (peeling decompositions, exact + greedy) and PA** (mixed order, exact + canonical rule): `peeling.py n` and `peeling.py --pa2 n [--sample K --seed S]` |
| `pastar_fails.py`, `pa2_fails.py` | PA*/PA** on every psolQ failure of `out/fail_n{n}.jsonl` |
| `pa_sample.py` | PA alone on random games (PD is slow from n = 5) |
| `classes_n4.py` | class containment check (superseded by T-A1's corollary; left for reference) |
| `instances/` | minimal failing games (PGSolver format) named in the results |
| `check.sh` | the < 1 min regression run by scripts/verify.sh |

Reproduce: `python3 validate.py` (2 min), `python3 exhaustive.py 3 --all-strahler` (seconds), `python3 exhaustive.py 4 --all-strahler --workers 3`
(about 30 min, 27.3 M games), `python3 hypotheses.py 3`, `python3 hypotheses.py 4 --sample 30000 --seed 4`.

## Regenerating the n = 4 data (not committed: 51 MB)
```
cd experiments/attr && python3 exhaustive.py 4 --workers 3 --all-strahler     # 27,331,200 games, 1632 s on 3 workers
```
Deterministic output (orbit, owner and pattern order are fixed): `out/fail_n4.jsonl` has 361,420 lines, sha256
728e7cda1757ff598db74c7b3c980c8fa23efb7de9fa383f894a8d2c907fb63c; `out/summary_n4.txt` sha256
c1e29137c7104280983f9cbc3d600be38c20d452f5125dc03169941fc2f6283f (committed copy: results/summary_n4.txt).
Note: the summary's time line differs between runs, so its hash is for the 2026-10-14 run only; compare the count lines.
