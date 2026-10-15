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
| every game, n=1, priorities 0..1 | 4 | brute force = py-zlk | 4 | 4 | results/exhaustive_n1_P1.csv |
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
  5,121; tc+ 4,448 (dtl; extension below); tc 3,232; red_counter_odftl 3,080; red_counter_dftl 2,056; red_chain 2,048; switchbestexp
  1,610; counter_m 1,539; counter_symsi 1,282; recursiveladder 1,280; switchallexp 903; counter_qpt 512 (all sizes solved < 0.1 s).

### tc+ extension (solo run, timeout 1800 s; results/fam_tc+_ext.csv)
`sweep.py tc+_ext --gen "tools/oink/build/tc+ {N}" --sizes 14 16 18 20 24 --timeout 1800 --tmax 1500 --ref-timeout 300`.
| N | n | uzlk | dtl wall s | dtl tangles | dtl iterations | idtl wall s | idtl tangles | idtl iterations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | 624 | agree | 1.6 | 94 | 18 | 4.1 | 118 | 17 |
| 12 | 1944 | agree | 42.5 | 190 | 26 | 137.6 | 239 | 25 |
| 14 | 3024 | agree | 168.4 | 250 | 30 | 556.8 | 317 | 29 |
| 16 | 4448 | agree | 565.2 | 318 | 34 | timeout (1800) | - | - |
(N = 8, 12 from fam_tc+.csv, run with 3 sweeps in parallel.) On tc+ the dtl iteration count is 2N+2 for N = 8..16 and the
tangle count ~1.24 N^2 (L-ALG's ~1.2N^2 reproduced); dtl wall time local exponent in n ~3.2 (N=14 -> 16). idtl is 3-4x slower
than dtl on tc+ and is the only pinned run that did not finish at N = 16 within 1800 s. All finished runs: verified strategies,
regions equal to uzlk.

## Second independent implementation (gauntlet step 2, Lead 21:20Z)
`dtl_py.py`: DTL and IDTL in Python, written from docs/alg/candidates/C5-DTL.md @ ccff864 ONLY (dtl.cpp not read while
writing). Output: regions + positional strategies; prints Oink-style counters. `xcheck.py` compares it with Oink's pinned
dtl / idtl per game: regions, strategies (harness/verify.py), tangles, dominions, iterations. `shrink_count.py` shrinks a
count or region divergence. Choices C5 leaves open are listed in dtl_py.py's docstring (CH1-CH6).

Two modes:
- default = C5-literal choices (equal priorities stable by input position; ins ascending; SCC vertices in Tarjan pop order).
- `--order oink` = the four orders Oink actually uses, each identified from a shrunk divergence and only then read in
  Oink's source: CH1' step-0 std::sort (game.cpp:478-505; `stdsort.py` emulates libstdc++ introsort incl. heap fallback),
  CH2' in-edge lists in decreasing index (game.cpp:868-906), CH3' tangle vertex lists sorted ascending (dtl.cpp ~385),
  CH3'' SCC vertex order = Pearce emission order (root first) and dominion queue only for vertices not yet in S
  (dtl.cpp 222-299, ~370). Plus CH6: the idtl iteration counter (dtl.cpp run() 1123-1138; C5 does not define it).

### Divergences found (all reported to the Lead at once; shrunk instances in failures/)
| # | what | shrunk instance | classification |
| --- | --- | --- | --- |
| 1 | idtl iteration count (one per search call vs one per round + 1) | idtl_itercount_n2.pg (2 vertices) | C5 omission (counter not defined); computation identical |
| 2 | tangle/dominion/iteration counts on 878/10,000 seeded games | count_r06005_min.pg (17 vertices) | C5 omissions: equal-priority order (C5 allows any), in-edge order, stored tangle vertex order |
| 3 | dominion/iteration counts on 3 games after #2 | count3_min.pg (23 vertices, sorted input) | C5 omission: SCC vertex order = dominion solve-queue order; the dominion-extension attractor deletes tangles as vertices are solved, so its result depends on queue order |
No region or strategy divergence in either mode, on any game. No pseudocode error and no Oink deviation from C5 found.

### Results
| corpus | games | `--order oink`: all five equal (regions, strategies, tangles, dominions, iterations) | C5-literal: regions + strategies equal | C5-literal: count differences |
| --- | --- | --- | --- | --- |
| exhaustive n<=3 (priorities 0..n) | 175,944 | 175,944 x {dtl, idtl} | all | 0 (n <= 16: step-0 sort is stable) |
| seeded g10k (n <= 200) | 10,000 | 10,000 x 2 | all | 878 games (tangles differ by up to 8, iterations by up to 2) |
| rngame | 2,000 | 2,000 x 2 | all | 296 games |
| seeded small50k (n 4..10) | 50,000 | 50,000 x 2 | all | 72 games |
| family instances (Oink idtl <= 5 s) | 127 | see results/xcheck_families.csv | - | - |
CSV: results/xcheck_*.csv(.gz); `_orderstable` = C5-literal mode.
