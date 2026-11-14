# THE BATTERY (L-COMP): gauntlet step 2 for any candidate engine
Everything here is DATA. A growth line is a READING of data, never a claim (D1; TARGET.md section 5 step 2; D2 change 5).
A BATTERY PASS with «polynomial-looking» on every family is compatible with an exponential candidate: RF (L-SI 57) passed all
five sets (record/rf_lred247_*: 10,499 answered instances, 17 families) and is dead on L-RED-B 8's family K^s_n
(7·2^(n−1) − 2n − 3 iterations on 3n² + 3n + 1 vertices). The fixed sets are families hard for OTHER rules; they cannot find a
candidate's own worst case. Standing rule (Lead 15:47Z): every kill family of the fleet goes into the battery when it exists.
Needs: python3, g++, Oink built (`scripts/setup_oink.sh`), and from this repo `experiments/battery` + `experiments/harness`
(the N5 self-test engines also read `experiments/comp/box44`, `experiments/n5-second`, `experiments/hard-families`).

## Engine interface
An engine is a command; the battery appends the path of a parity game in PGSolver format (vertex ids 0..n-1, max-parity,
owner 0 = Even) and reads the LAST non-empty line of stdout, one JSON object:
`{"winner": [0|1 for every vertex id], "strategy": {"<vertex id>": successor id, for every vertex OWNED by its winner},
"iterations": int or null, "steps": int or null}` (strategy may also be a list of length n with null / -1 for no move).
Worked example (2 vertices; Even owns both; 0 has priority 1 and edges to 0 and 1; 1 has priority 2 and a self-loop):
```
$ printf 'parity 2;\n0 1 0 0,1;\n1 2 0 1;\n' > /tmp/g.pg ; python3 engines/zielonka.py /tmp/g.pg
{"winner": [0, 0], "strategy": {"0": 1, "1": 1}, "iterations": 1, "steps": 3}
```
Engines here: `engines/oink_zlk.py` (reference: Oink zlk wrapped), `engines/zielonka.py` (recursive algorithm, self-contained),
`engines/n5.py --mode spec|xi` (N5 and N5'-xi, both dead, kept for their KNOWN rows), `engines/control.py` (wrong on purpose),
`engines/sol_adapter.py [--iter REGEX] [--steps REGEX] '<solver command with {in} {out}>'` (any solver that writes an Oink /
PGSolver solution file `v winner [strategy];` becomes an engine; the regex pulls the count out of the solver's output),
`engines/rf_lred247.py [--rule rf|howard]` (candidate RF of L-SI 57 through L-RED's implementation, claude/l-red 821d63e3
experiments/red/r247, unmodified, from an archive named by env LRED; NOT the designer's own engine).

## Run
`experiments/battery/run_battery.sh '<engine command>' [set ...]` (sets: a b c d e; default all). Never pipe it (exit code).
For every instance: timeout; winner against Oink zlk (pinned 8fbf0a7, run with -v; the manifest names `tl` / `psi` where zlk
aborts or blows up: counter_m 41, 42 and large sizes of the families built against it); strategy
checked by `experiments/harness/verify.py`; iterations, steps, wall seconds. Per family: a table (param, n, m, d, iterations,
steps, seconds, status) and a growth line for the measure y (iterations, else steps, else seconds): the ratios y(next size) /
y(size) over the last three steps; power-law fits y = c0 + a x^b in x = n and in x = the size parameter (exponent b);
exponential fits y = c0 + a g^x in n and in the parameter (factor per size step); each with its err (sum of squared relative
errors; c0 is free from 7 answered sizes on, else 0). Reading: «too few points» (under 4 answered sizes); «exponential-looking»
(the better exponential fit beats the better power law AND y at least doubles from the first to the last size); else
«polynomial-looking». Limits measured on synthetic sequences (battery.py growth): with 7 or more sizes only slow exponentials
(1.2^k over 7 sizes) were misread; with 4 to 6 sizes a polynomial with a large additive constant can read exponential-looking
and 2^k + k^3 can read polynomial-looking. Read the table and the ratios, not only the word.
Exit 0 pass (timeouts listed) | 1 wrong winner or bad strategy (instance printed) | 2 engine error or no answer | 3 battery broken.
Environment: BATTERY_TIMEOUT (60 s), BATTERY_JOBS (2), BATTERY_OUT (directory for report.txt, rows.tsv, summary.json),
BATTERY_MAXPARAM, BATTERY_FAMILY (comma-separated), BATTERY_LIMIT_E, BATTERY_NOSKIP=1 (a family stops at its first timeout
otherwise), BATTERY_CACHE, BATTERY_OINK (path of the oink binary), BATTERY_WINNER_ONLY=1 (prototype without strategies:
winners compared, strategies NOT verified, last line says so; not a step-2 pass).

## Instance sets (each `sets/<set>/MANIFEST.tsv` pins every file by sha1; a mismatch is exit 3)
| set | content | source (copied byte for byte; not regenerated) |
| --- | --- | --- |
| a | Γ3(G_k), k = 3..13, n = 135k − 230 | claude/l-red-b 10dfedb6 experiments/red-b/data/b6b/pg/ |
| b | wrapper family of R130: WL_1..4 = W(G_n, ι); W_2..8 = W(switchallexp_n); F_2..8 | claude/l-si 8c062914 experiments/si/box104/inst |
| e | 10,000 seeded random games, n 8..500, agreement only | `sets/e_random/rngame_seeded.cpp` = Oink rngame.cpp @ 8fbf0a7 + a seed argument (Oink's rngame seeds from std::random_device); arguments and seed per game in the manifest |
| d | harness instances: the 300 tiny games of selftest.py step 2 (brute-force checked there), 5 regressions, 3 hkp bench games; agreement only | experiments/harness (this lane); `sets/d_harness/mk_set.py` |
| c | the 13 M1 hard families at the sizes of experiments/hard-families/run_all.sh (173 instances) + counter_m 41, 42 | generated at run time by Oink's generators (8fbf0a7) and experiments/hard-families/pgsolver_port.py, each output sha1-pinned (`sets/c_hard/mk_manifest.py`); M1 never froze them as files |

## Self-test (rows that must come out as known; if one does not, the battery is wrong)
`python3 -B selftest.py quick` (1 minute; run by check.sh) or `full OUTDIR`. Known rows and sources: selftest.py's header. Records: record/ (experiments/*/out/ is gitignored, so nothing of record lives in out/);
record/selftest_full* is the full run of the battery at commit dd9ba4ac (19 checks), record/zielonka_c the Zielonka engine on set c,
record/n5spec_e and record/n5spec_c N5 (SPEC) on sets e (10,000 of 10,000 OK) and c (161 OK, 4 timeouts at 60 s, 8 skipped),
record/rf_lred247_ab, rf_lred247_cde RF by L-RED's engine (l-red 821d63e3) on all five sets, record/howard_lred247_abc Howard
(same engine) on a, b, c: exponential-looking on switchallexp (10, 30, 150, 2486 at N = 1, 2, 4, 8).
