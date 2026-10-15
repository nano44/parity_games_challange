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

| extra: seeded small games `gen.py corpus out/small50k 50000 20261016 --nmin 4 --nmax 10` | 50,000 | uzlk and py-zlk (both ok on all) | 50,000 | 50,000 | results/small50k.csv.gz |

Exhaustive games include self-loops (every non-empty successor set), so `--no-loops` is exercised.
g10k: n up to 200, up to 137 distinct priorities; max 186 tangles, max 5 iterations (dtl) / 4 (idtl), max 0.2 s.

### (2) Oink rngame corpus: 0 MISMATCH, 0 BADSTRAT, 0 error
`harness/rngame_corpus.sh out/rn 2000 200` (rngame seeds from std::random_device, so the games are the record:
`results/rngame_corpus.tar.gz`, manifest with sha256 inside). 2,000 games, n up to 200, uzlk and py-zlk ok on all,
dtl-pin and idtl-pin 2,000/2,000 ok with verified strategies (results/rngame.csv). Max 22 tangles, 5 iterations.

### (3)-(4) Hard families and attack instances: 0 MISMATCH, 0 BADSTRAT, 0 error
`run_families.sh` (families.txt; tmax 200 s, timeout 400 s, reference timeout 120 s; 3 sweeps share 4 cores, so wall times
compare sizes within one family only). 18 families: the 13 M1 families (Oink tc, tc+, counter_symsi, counter_rr, counter_dp,
counter_m, counter_core, counter_rob, counter_ortl, counter_qpt; PGSolver ports recursiveladder, switchallexp, switchbestexp)
and L-RED's experiments/red/dtl/gens_dtl.py chain, ladder, counter_dftl, counter_odftl, n5. Each sweep stops after the first
size where dtl or idtl times out or exceeds tmax; the largest finished size is the "largest that finishes" at these limits.
Every finished DTL/IDTL run has verified strategies; Zielonka (uzlk and/or py-zlk) finished and agreed on the smaller sizes of
every family and on all sizes of counter_qpt, red_chain, red_counter_dftl, red_ladder, switchallexp, switchbestexp, tc+
(table "Agreement" in results/growth.md). Where Zielonka timed out, the regions are certified by the two verified strategies.
L-ALG's step-4 instances experiments/alg/instances/dtl_proof_c1..c4.pg: 4/4 ok for both (results/dtl_proof_c.csv).

Growth (results/growth.md, plots results/plots/<family>.png; exponent k of y ~ n^k over the largest 4 finished sizes):
- tangles: linear in n on every family that has tangles (k = 0.99-1.03), ~n^0.5 (= linear in N) on tc, ~n^0.6-0.7 on tc+;
  0 or 1 tangle on counter_qpt, switchallexp, switchbestexp. Matches L-RED's 2N+3 on counter_dftl/odftl (1027 at N = 512).
- iterations: constant (1-6) on every family except tc+, where they grow (5, 10, 18, 26 at n = 24, 104, 624, 1944; k ~0.35).
- wall time: polynomial-looking, local exponent 2.0-4.0 in n (largest: counter_ortl 3.99, recursiveladder 3.94,
  red_counter_dftl 3.93, switchallexp 3.91); power law fits better than exponential on the last 4 sizes everywhere it is
  measurable. So the cost per tangle grows like n^2..n^3 on these families: data for the running-time side (DTL-proof.md
  section 3 bounds the work by O(|T|^2 n^6 + |T| n^7 + n^8 + ...), far above what is measured).
- Largest finished n: counter_rob 50,179; counter_dp 8,196; counter_rr 8,192; red_ladder 6,150; counter_core 6,147; counter_ortl
  5,121; tc 3,232; red_counter_odftl 3,080; red_counter_dftl 2,056; red_chain 2,048; tc+ 1,944 (extension running); switchbestexp
  1,610; counter_m 1,539; counter_symsi 1,282; recursiveladder 1,280; switchallexp 903; counter_qpt 512 (all sizes solved < 0.1 s).
