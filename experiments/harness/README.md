# Harness: reference solvers, random games, compare tool (gauntlet step 2 bench)

Solver-agnostic. A **solver** is any command that reads a PGSolver `.pg` file and writes a solution in
`paritysol` format (`v winner [strategy];`, winner 0 = Even, 1 = Odd) to `{out}` (or to stdout).
Convention: max-parity, owner 0 = Even, priorities any naturals (TARGET.md v1.0 allows 0..n; same as Oink and PGSolver).
compare.py checks, for every solver and game: regions equal the reference's, and every winner's positional strategy
passes verify.py (status BADSTRAT otherwise; the reference's own strategies are checked too).

| file | what |
| --- | --- |
| `pg.py` | parse/write `.pg`, read/write solutions |
| `zielonka.py` | independent recursive Zielonka in Python (`py-zlk`), plus `brute_force` (enumerates Even's positional strategies; tiny games only) |
| `gen.py` | seeded random games: `gen.py n d dmin dmax seed [--peven P] [--no-self-loops]`; `gen.py corpus DIR COUNT SEED [--nmin --nmax]` draws varied n, #priorities, degree, owner mix, self-loops; every game file name records its parameters and seed; `manifest.csv` lists them. Own splitmix64 PRNG, so games are identical across Python versions |
| `rngame_corpus.sh` | Oink `rngame` corpus. rngame seeds from `std::random_device`: not reproducible, so the files are the record (manifest has sha256 prefixes) |
| `solvers.py` | registry: `py-zlk`, `oink-<s>` for every Oink solver (`-w 1`), `oink-<s>-raw` (no single-parity / winner-controlled-cycle preprocessing) |
| `compare.py` | run solvers on a corpus, check winning regions against the reference (default `oink-uzlk`), CSV of status/time/iterations; extra solvers via `--solver NAME='CMD {in} {out}'` |
| `verify.py` | independent positional-strategy verifier (D2 change 5): closure of each winner's strategy in its region, and no opponent-parity dominant cycle in the one-player graph (recursive SCC decomposition) |
| `xverify.py` | cross-checks verify.py against Oink's `verify` tool on correct and mutated solutions |
| `selftest.py`, `check.sh` | the <2 min deterministic self-test run by `scripts/verify.sh` |

## Self-test (check.sh)
1. generator determinism: the 200-game corpus (master seed 2026, n in 1..40) hashes to a pinned sha256;
2. brute force == py Zielonka on 300 tiny games (n <= 7): an oracle with no attractor code;
3. py Zielonka == Oink `uzlk` == Oink `zlk` on the 200 games (skipped with a NOT RUN line if Oink is not built);
4. compare.py reports a region-wrong solver that writes the reference's strategies as exactly MISMATCH on 5/5 games;
5. verify.py hand-built unit cases, no Oink: 3 accepted; rejected for leaving the region, in-region losing cycle,
   missing strategy, non-edge strategy, opponent escape;
6. verify.py agrees with Oink's `verify` on 300 correct/mutated solutions. `mutation_check.sh` shows that steps 4 and 5
   fail when compare.py's region check or verify.py's cycle test / closure checks are planted out.

## Re-run the validation
```
python3 gen.py corpus out/own 2000 11 --nmax 150
./rngame_corpus.sh out/rn 1000 120
python3 compare.py out/rn out/own -s py-zlk oink-zlk oink-tl ... --timeout 30 --csv out/res.csv
```
For the gauntlet's 10,000 games: `python3 gen.py corpus out/g10k 10000 <seed> --nmax 200`, then `compare.py out/g10k --solver NEW='...'`.

## Generic bench families (L-LIT ranked list, claude/l-lit a6c530f docs/lit/2511.03752-position.md)
- rank 1, `exhaustive.py`: every game with n vertices and priorities 0..P (file corpus with `--stride`, or `iter_games`
  in-process). Checked: py-zlk == brute force with verified strategies on all 74088 games with n = 3, P = 2;
  py-zlk == Oink zlk == uzlk on all 324 games with n = 2, P = 2.
- rank 2, `bench/hkp_fig4a.pg`, `hkp_fig4b.pg`, `hkp_fig6.pg`: Huth-Kuo-Piterman (arXiv 1405.0386v2) incompleteness
  witnesses, encoded from the figures' tikz source by `bench/make_hkp.py` (min-parity converted to max-parity).
  Brute force: Even wins every vertex of all three (Fig. 6 agrees with L-LIT's hand check).

## Results
See `validation.md`.
