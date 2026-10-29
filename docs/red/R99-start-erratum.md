# R99: erratum. Three invalid or partial start files under experiments/red/n3/instances, repaired; every reported count reproduces
L-RED successor 23 (Opus 5.5). Lead 2026-10-29 00:10Z, relaying both CORE-N5 referees. Written 2026-10-29 00:2xZ (date -u). Label: DATA.

## 1. What was wrong (checked with a scan of every experiments/red/*/instances/*.start against its game: 51 files, 2 invalid, 1 partial)
| instance | game sha1 (unchanged) | old .start sha1 | defect | reported in |
| --- | --- | --- | --- | --- |
| comp54_n80 | 16c64008… | 35dee2db… | forced vertex 11 is given 11→51, which is not an edge | R88 §5 (pin, T = 54), R89 (longest run 12) |
| n3cov_lean | bcf8dbf6… | 9d3ab487… | written for another owner assignment: Odd 47 in SIGMA0, Even 7 and 19 in TAU0; also partial | R87 §1 (coverage pin), experiments/red/check.sh l. 237-238 |
| n3cov_phi | 50d416db… | 0ee71ae7… | PARTIAL (entries valid, many vertices absent); n5.py fills the rest from S3, while n5b needs a full start | R87 §1 (coverage pin) |
- n5.py sets the given moves without checking them, so the old comp54 / n3cov_lean runs started from a state with a non-edge or a
  wrong-owner entry. Those runs were not faithful N5 runs.
- Also: R87 §1's pin table has the two sizes swapped. n3cov_lean is n = 48 and n3cov_phi is n = 32; the sha1s in that table are right.
- All other 48 start files under experiments/red/*/instances are full and valid.

## 2. Repair (the old files are kept, as their sha1s are cited)
- New files: experiments/red/n3/instances/comp54_n80_fixed.start (d2afc58f…), n3cov_lean_fixed.start (b116c3e2…),
  n3cov_phi_fixed.start (53dabe31…).
  - Each is S3 (SPEC FIX 1), overridden by every valid entry of the old file; invalid entries are dropped.
  - Written by experiments/red/sel/fullstart2.py.
- Re-run with experiments/red/ul/vrun.sh (n5.py = n5b --mode spec, Oink zlk "OK strategies verified" for both) and phsw.py:

| instance | iterations / fallbacks (n5 = n5b) | reported | PL | longest fallback-free run |
| --- | --- | --- | --- | --- |
| comp54_n80 | 55 / 6 | R88: T 54 (phase), R89: run 12 | 54 | 12 |
| n3cov_lean | 35 / 1 | R87: 35 / 1 | 30 | 30 |
| n3cov_phi | 31 / 3 | R87: 31 / 3 | 25 | 9 |
- Every reported count reproduces, so no conclusion of R87, R88 or R89 changes.
- experiments/red/check.sh now uses n3cov_lean_fixed.start. n3x PASS and the MUT=1 strict-control FAIL are both unchanged.
