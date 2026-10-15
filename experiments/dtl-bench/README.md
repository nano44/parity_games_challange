# DTL gauntlet step 2 (L-COMP bench, independent of L-ALG / L-RED)
Lead GO 2026-10-15 18:41Z. Subject pinned by docs/DECISIONS.md L22:
A_DTL = `oink --dtl --no-single --no-wcwc --no-loops IN OUT` at Oink 8fbf0a7 (scripts/setup_oink.sh), trace 0 (no `-t`),
exactly this command (no `-w`). A_IDTL = the same with `--idtl`. Every result row records the exact command in column `cmd`.

## Method
- Reference: Oink `uzlk` (Zielonka, default flags) and the independent Python Zielonka `harness/zielonka.py` (py-zlk,
  subprocess with timeout). Exhaustive games: brute force (enumeration of Even's positional strategies) and py-zlk in-process,
  which must agree before DTL is judged.
- Every solution (references included) is checked by `harness/verify.py` (D2 change 5): each winner's positional strategy is
  closed in its region and wins the one-player game left. Oink's own verifier is never used.
- Status per (game, solver): ok | MISMATCH (region differs from reference) | BADSTRAT | timeout | error. Failures are
  printed at once (`!!` lines), listed in `<csv>.bad`, and the game is copied to `failures/` for `experiments/m2/shrink.py`.
- Counters parsed from Oink's log: `found D dominions and T tangles`, `solved in I iterations and P pruning steps`.
- `check.sh` (run by scripts/verify.sh): exhaustive n=2, P=2 through the bench; a planted region flip is reported
  MISMATCH and a planted losing strategy BADSTRAT (`plant.py`). Prints SKIPPED if Oink is not built.

| file | what |
| --- | --- |
| `bench.py` | `files CORPUS...` or `exhaustive n P`; 4 workers; CSV with counters and commands |
| `sweep.py` | one family over sizes; stops after the first size where a pinned solver times out or exceeds `--tmax` |
| `families.txt`, `run_families.sh` | every family, generator, sizes; 3 sweeps in parallel |
| `fit.py` | `results/growth.md` (agreement table, fitted exponents) and `results/plots/<family>.png` |
| `run_step1.sh` | exhaustive tiny games + the 10,000 seeded games |
| `plant.py`, `check.sh` | self-check with planted defects |

## Results
### (1) Exhaustive tiny games and 10,000 seeded random games: 0 MISMATCH, 0 BADSTRAT, 0 error, 0 timeout
| corpus | games | reference | dtl-pin ok | idtl-pin ok | csv |
| --- | --- | --- | --- | --- | --- |
| every game, n=1, priorities 0..1 | 8 | brute force = py-zlk | 8 | 8 | results/exhaustive_n1_P1.csv |
| every game, n=2, priorities 0..2 | 324 | brute force = py-zlk | 324 | 324 | results/exhaustive_n2_P2.csv |
| every game, n=3, priorities 0..3 (TARGET class: priorities 0..n) | 175,616 | brute force = py-zlk | 175,616 | 175,616 | results/exhaustive_n3_P3.csv.gz |
| seeded corpus `gen.py corpus out/g10k 10000 20261015 --nmin 1 --nmax 200` | 10,000 | uzlk and py-zlk (both ok on all) | 10,000 | 10,000 | results/g10k.csv |

Exhaustive games include self-loops (every non-empty successor set), so `--no-loops` is exercised.
g10k: n up to 200, up to 137 distinct priorities; max 186 tangles, max 5 iterations (dtl) / 4 (idtl), max 0.2 s.

### (2) Oink rngame corpus: 0 MISMATCH, 0 BADSTRAT, 0 error
`harness/rngame_corpus.sh out/rn 2000 200` (rngame seeds from std::random_device, so the games are the record:
`results/rngame_corpus.tar.gz`, manifest with sha256 inside). 2,000 games, n up to 200, uzlk and py-zlk ok on all,
dtl-pin and idtl-pin 2,000/2,000 ok with verified strategies (results/rngame.csv). Max 22 tangles, 5 iterations.

### (3)-(4) Hard families and attack instances
Running; see results/growth.md when done.
