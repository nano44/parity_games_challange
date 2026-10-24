# N5 exhaustive small-game searches (L-COMP box 3, 2026-10-24)
Lead brief 13:08Z (box 3) with addenda 13:20Z (theta-changes, D18), 13:42Z (T28 (b), SEG-1O), 14:00Z (ELIM window, E per stretch),
14:10Z (ELIM = noelimrun_both, thetaelim). All quantities are DATA; "CONJECTURE (exhaustive to n <= k)" means only what the table says.

## Tools
| file | what |
| --- | --- |
| `exh.py` | exhaustive enumeration of C^1O games (exactly one Odd vertex o with out-degree > 1) in a stated canonical subset, N5 from the canonical start or from every start pair; per-game measures (below); JSON per table in out/ (gitignored; copies in results/) |
| `rnd.py` | random o-cyclic C^1O games (box25 `rand_c1o`), canonical start + one random start pair, or every start pair (`--all-starts`) |
| `analyse()` in exh.py | the measures, validated against L-RED `retcheck.py` (re-entry classes), box21 `phases.py` (phase lengths), L-SI `elim.py` / `thetaelim.py` (ELIM windows, theta in windows) on returns_rt48, returns_ph64, theta_thf16, fts_best16 (`validate.py`) |
| `check_instance.py` | per reported instance: n5x.trace(check=True) (= n5.run counts), n5b.py SPEC full state sequence equal, regions = Oink zlk @ 8fbf0a7, verify.py; saves instances/NAME.pg (+ .start) |
| `shrink.py` | greedy shrink (delete vertex / edge, lower priority) keeping a theta-driven re-entry (from a start pair, or from the canonical start with `--prop canonA`) |

Canonical subset of exh.py: distinct priorities with vertex ids in increasing priority order (minimal values for the parity
pattern). L-SI's Engine ranks by (priority, id), so every C^1O game is Engine-equivalent to one game of this form up to relabelling;
relabelled copies can differ only through N5's id tie-breaks. Self-loops allowed. Options restrict further (stated per table).

## Measures (per run; maxima over runs in the tables)
- maxph: longest joint lambda-phase in iterations (phases.py convention).
- thch: max theta-changes (theta = Xi_sigma(o)) inside one joint lambda-phase ((CYC)).
- trust: max trust events per (tau, joint-lambda)-phase (box25 trustcount.count).
- re-entries into R inside every phase, retcheck classes: A = theta at re-entry > w at the last leave ("theta-driven"), B = route
  improvement; raw leave / entry counts. (L-NEW's reentry.py classifier was not on claude/l-new during this box.)
- SEG-1O: longest run of transitions inside a joint lambda-phase without a theta change, minus (n - 1).
- (b) trust-route growth (T28): for z in the box25 trust set T_k that stays in R inside one (tau(o), joint-lambda)-phase, is its
  route length to o + 1 at the next state?
- ELIM window (L-SI (ELIM-n)): elim.py noelimrun_both (sigma edge or Odd best-reply edge abandoned for good in the phase), minus
  (n - 1); also sigma-only and sigma-or-tau variants; thetaelim (theta-changes inside a non-eliminating window).
- E (L-LIT (H-E)): per fallback-free (theta, w, tau, lambda)-stretch, changes of admitted status of R-entering Even arcs; reported
  with the longest stretch and the excess of stretch length over (E + 1)(n - 1).

## Results (2026-10-24, runs 13:05-15:50Z; every listed instance passed check_instance.py: n5b states equal, Oink zlk, verify.py)
### Exhaustive tables (results/*.json)
| table | games / runs | max it | max in-phase | max theta-ch./phase | max trust/phase | re-entries A / B | SEG-1O excess | (b) holds / violated | ELIM window both (sigma; sigma-or-tau) | max theta-ch. in non-elim window | max E / longest stretch | H-E excess |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| n 2, canonical | 40 | 0 | 0 | 0 | 0 | 0 / 0 | <= 0 | 0 / 0 | 0 | 0 | 0 / 0 | <= 0 |
| n 3, canonical | 9,600 | 1 | 1 | 0 | 1 | 0 / 0 | <= 0 | 0 / 0 | - | - | - | <= 0 |
| n 3, ALL start pairs | 9,600 / 48,600 | 3 | 3 | 1 | 1 | 0 / 0 | <= 0 | 0 / 0 | 1 (1; 0) | 0 | 2 / 1 | <= 0 |
| n 4, canonical (full canonical subset) | 4,828,736 | 3 | 2 | 1 | 2 | 0 / 0 | <= 0 | 0 / 0 | 1 (1; 0) | 0 | 2 / 1 | <= 0 |
| n 4, ALL start pairs, no forced Odd, Even out-deg <= 2 | 704,000 / 7,340,032 | 5 | 4 | 2 | 2 | 0 / 0 | <= 0 | 320 / 248 | 1 (1; 0) | 0 | 4 / 3 | <= 0 |
| n 5, canonical, no forced, Even out-deg <= 2, o out-deg 2, o-cyclic: 57 of 160 (o, parity) slices, each slice complete | 24,497,460 | 4 | 3 | 1 | 3 | 0 / 0 | <= 0 | 0 / 80 | 1 (1; 0) | 0 | 4 / 2 | <= 0 |
(n 2 and n 3 canonical tables were produced before the ELIM / E columns existed; their phases have <= 1 transition, so ELIM <= 1 and
E-stretches <= 1 trivially.) "<= 0" = no excess (exh.py flags any positive excess at once; none was flagged).

Phase-length histograms (runs by longest phase): n 4 canonical {0: 2,991,460, 1: 1,779,128, 2: 58,148}; n 4 all starts {0: 755,272,
1: 5,955,086, 2: 611,706, 3: 17,814, 4: 154}; n 5 subset (partial) {0: 10,599,029, 1: 9,289,546, 2: 308,658, 3: 2,427}.

### Random all-starts stream (results/rnd_5_8_all_s51.json; rand_c1o, no forced Odd vertices, every start pair; 18,299 games)
| n | runs | max in-phase | max theta-ch./phase | ELIM window both | theta-ch. in non-elim window | SEG excess | H-E excess | max E | re-entries A / B | (b) holds / violated |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 233,021 | 4 | 2 | 2 | 0 | 0 (tight: run of n-1 = 4) | -1 | 6 | 0 / 0 | 18 / 71 |
| 6 | 455,638 | 5 | 3 | 2 | 0 | -1 | -2 | 7 | 1 / 0 | 16 / 330 |
| 7 | 903,945 | 6 | 3 | 2 | 0 | -2 | -2 | 8 | 0 / 0 | 85 / 1,246 |
| 8 | 1,775,235 | 5 | 3 | 2 | 0 | -3 | -3 | 8 | 6 / 2 | 194 / 2,722 |

### Theta-driven re-entries (class A, retcheck definition) - EXIST (instances/)
| instance | n | m | start | Odd vertices | note |
| --- | --- | --- | --- | --- | --- |
| thetaA_n17 | 17 | - | random pair | o + 2 forced | first hit (rnd n 12..20) |
| thetaA_n9 | 9 | 13 | same start, shrunk | o only | |
| thetaA_canon_n8 | 8 | 12 | CANONICAL | o + 1 forced | shrunk from canonA_1 (n 15); canonA_0/1, thetaA_canon_n12 also saved |
| thetaA_n7 | 7 | 11 | random pair | o only | shrunk from an n 8 hit |
| thetaA_n6 | 6 | 10 | random pair | o only | shrunk from an n 7 hit; rnd also hit n 6 directly |
Mechanism in every case: inside one joint lambda-phase (tau fixed) Even vertices leave R; an Even vertex on o's continuation (outside
R) switches and theta = Xi_sigma(o) rises; a vertex that left re-enters R with theta_now > w_at_leave.
None at n <= 4 (exhaustive tables, any start in the n 3 / n 4 tables) and none at n 5 (random all-starts, 233k runs; n 5 canonical
subset, 24.5M games).

### Named instances (Lead 13:42Z / 14:00Z / 14:10Z)
| instance | n | maxph | thch | seg (n-1) | (b) ok / bad | ELIM both | theta in window | max E / stretch |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fts_best16 | 16 | 27 | 8 | 10 (15) | 0 / 19 | - | - | - |
| theta_thf16 | 16 | 19 | 13 | 2 (15) | 0 / 5 | 3 | 3 | 4 / 2 |
| returns_rt48 | 48 | 79 | 3 | 40 (47) | 0 / 122 | 11 | 0 | 21 / 11 |
| returns_ph64 | 64 | 104 | 3 | 56 (63) | 0 / 191 | 15 | - | 21 / 11 |

### Readings (DATA; CONJECTURE labels as the Lead asked)
- (a) theta-driven re-entries exist, from the canonical start too; smallest found n = 6 (start pair), n = 8 (canonical). None at n <= 4
  in the exhaustive tables.
- Max in-phase length, canonical start: 0, 1, 2 for n = 2, 3, 4 (exhaustive in the canonical subset), 3 at n = 5 (subset, 57/160
  slices): CONJECTURE max = n - 2 for n <= 4 (n 5 consistent). All starts: 3 at n = 3 (exhaustive), 4 at n = 4 (subset); random n 5..7:
  4, 5, 6.
- (b) trust-route growth: COUNTEREXAMPLE (as stated; smallest instances/n4all_tgbad_0, n 4, from a start pair).
- SEG-1O: holds on every run (CONJECTURE exhaustive to n <= 4 in the stated subsets); attained with equality at n = 5 (random).
- ELIM-n (noelimrun_both <= n - 1): holds everywhere; the window never exceeded 2 on random n <= 8 and 1 exhaustively at n <= 4;
  CONJECTURE exhaustive to n <= 4 (subsets as stated).
- CYC-ELIM: theta-changes inside a non-eliminating window: 0 in every exhaustive table and random run; 3 on theta_thf16.
- H-E: stretch length <= (E + 1)(n - 1) on every run (no excess).
