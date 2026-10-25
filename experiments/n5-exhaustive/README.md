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

## Box 4 (Lead 16:10Z, D18; docs/new/N5-xing-box27.md §8): (CYC'), (NH), reentry.py classes (box4.py; runs 16:10-17:35Z)
Definitions exactly as experiments/new/box25/phaseprofile.py, applied to every phase (key (lambda_sigma, lambda_tau, tau(o))):
cyc = theta-changes + w-changes per phase; noh = non-(h) transitions per phase; nohlen = longest phase containing a non-(h)
transition; re-entry classes from reentry.py (ROUTE / WRISE / THETA / OTHER). box4.measure equals phaseprofile.py on fts_best16,
theta_tp32, theta_thc24, sc32 (sc32: 43 / 0 / 0 in the long phase; one non-(h) transition in a 1-iteration phase, which phaseprofile
does not print).
| table (results/box4_*.json) | games / runs | max cyc (theta, w) | max noh | longest phase with noh > 0 | longest phase | re-entries ROUTE / WRISE / THETA / OTHER |
| --- | --- | --- | --- | --- | --- | --- |
| n 4 canonical (full canonical subset) | 4,828,736 | 2 (1, 1) | 2 | 2 | 2 | 0 / 0 / 0 / 0 |
| n 4 all starts (no forced, Even out-deg <= 2) | 704,000 / 7,340,032 | 3 (2, 1) | 3 | 3 | 3 | 192 / 0 / 0 / 0 |
| n 5 canonical subset (as box 3), 44 of 160 slices | 18,910,320 | 2 (1, 1) | 3 | 3 | 3 | 390 / 0 / 0 / 390 |
| random all starts n 5..9 (6,000 games) | 1,826,258 | 4 (3, 2) | 4 | 4 | 4 | 161 / 6 / 5 / 0 |
| random n 8..16, canonical + 1 random start (970,000 games) | 1,940,000 | 6 (3, 3) | 5 | 5 | 6 | 470 / 72 / 4 / 119 |
cyc histograms: n 4 canonical {0: 4,826,000, 2: 2,736}; n 4 all starts {0: 7,271,012, 1: 23,594, 2: 45,322, 3: 104}.

Checked instances (instances/, check_instance.py OK: n5b states equal, Oink zlk, verify.py):
- nh_n8 (n 8, m 13, start pair, shrunk with shrink.py --prop noh): a 4-iteration phase with 4 non-(h) transitions, theta and w constant;
  (h) fails because o lies on the play cycle (o 5 -> 7 -> 6 -> ... -> o) at every state. Could not shrink below n 8.
- b4_nohlen5_0 (n 11, start pair): a 5-iteration phase with 5 non-(h) transitions (phaseprofile.py confirms).
- b4_cyc6_0 / _1 (n 11 / n 12; _1 from the CANONICAL start): cyc 6 in one phase (_1: 3 theta + 3 w changes in a 4-iteration phase).
- b4_n4all_cyc3_0 (n 4, start pair): cyc 3.
- b4_theta_n7 (n 7, start pair): 5 THETA-class re-entries (pure throttle release, reentry.py -v), 1 ROUTE.
- b4_n5_other_0 (n 5, CANONICAL start): 2 OTHER-class re-entries (reentry.py).
Readings (DATA; CONJECTURE = exhaustive in the stated subset):
- (CYC'): max theta+w changes per phase = 2 at n 4 canonical, 3 at n 4 all starts (CONJECTURE, exhaustive in the subsets); 2 on the
  n 5 canonical subset (44/160 slices); random lower bounds 4 (n <= 9), 6 (n 11-12). Small n sits far below n; the low end of the law
  does not decide "faster than n" (sc32: 43 at n 32).
- (NH): non-(h) transitions per phase reach the phase length at small n: max 2 / 3 (n 4 canonical / all starts), 3 (n 5 subset); a
  long phase made entirely of non-(h) transitions occurs at n 8 (nh_n8, 4 iterations) and n 11 (5 iterations), from start pairs. Every
  such long phase seen has o on the play cycle and theta, w constant.
- reentry.py classes: ROUTE dominates; THETA occurs (n 7, start pair); OTHER occurs already at n 5 from the canonical start.
- Not done (Lead 17:1xZ, would need new runs): the X (crossing transitions) and O (OTHER-state transitions) columns; handed to box 5.

## Box 5 (Lead GO 17:5xZ, D18; L-NEW box 28 §5c (X) and (NH')): X and O per joint lambda-phase (runs 17:52-19:56Z)
Labels (L40): everything here is DATA (exact = exhaustive in the stated class), CONJECTURE (data behind it named) or OPEN; nothing is
PROVED. Phase key (lambda_sigma, lambda_tau, tau(o)) as box25 phaseprofile.py (not exh.py's maxph key).
- X = crossing transitions of a phase (R changes; R = vertices whose (sigma, tau)-play reaches o, box28 fbre.reach_o / thtrace.Rset);
  O = transitions of the phase with an OTHER endpoint ((h) fails and Xi != W at some vertex). Columns max X, max O per run, with the
  length of the phase attaining it (Xplen / Oplen) and X - n (Xmn). box4.py --no-reentry skips reentry.py (box 4 has those columns).
- Definition check (xo_validate.py): box4.measure_ph's per-phase (first, last, X, O) and trace_fb's states equal L-NEW's
  box28 xcount.phases_x on 33 instances: sc32 (X 30), theta_tp32 (22), fts_best16 (14), fbref_cex_n32 (28; sha1 901674dc), x32_sc32
  (X 37 > n 32), oc16_s2 (O 16), box28/out/*, instances/*. ALL EQUAL.
- O split (xo_split.py, from docs/new/N5-NH2-box29.md §0, §4-§5, l-new 670a63b): crossing-free interval = maximal run of states of a
  phase with R constant; each OTHER-touching transition is CROSS, or FCH (Xi/W change on F = V \ R), RONLY (changes on R only) or
  FLAT; WC = w-changes under not H1 and not H2; RONLY per OTHER block. Per-phase sums equal box29 rsplit.py / otherx.py.

| table (results/box5/) | games / runs | max X per phase (phase length) | max O per phase (phase length) | X hist | O hist |
| --- | --- | --- | --- | --- | --- |
| n 4 canonical (full canonical subset) | 4,828,736 | 2 (2) | 1 (1) | 0: 4,773,310, 1: 55,330, 2: 96 | 0: 4,826,000, 1: 2,736 |
| n 4 all starts (no forced, Even out-deg <= 2) | 704,000 / 7,340,032 | 3 (3) | 2 (2) | 0: 7,021,260, 1: 297,578, 2: 21,102, 3: 92 | 0: 7,323,452, 1: 16,576, 2: 4 |
| n 5 canonical subset (as box 3: no forced, Even out-deg <= 2, o out-deg 2, o-cyclic; all 160 slices) | 68,764,800 | 2 (2) | 1 (1) | 0: 66,711,412, 1: 2,036,230, 2: 17,158 | 0: 68,703,572, 1: 61,228 |
| random, canonical + 1 random start, 20,000 games per n, n 6..16 (box4_rnd_n_n_s5nn.json) | 16,888-18,358 games per n (2 runs each) | 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4 (n 6..16) | 1, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2 | | |

Climbs (climb5.py; canonical start; mutation box21 climb_fix.mutate; one seed, 120 s per n unless stated; logs gitignored):
- X from random starts: X = 3, 4, 4, 6, 7, 8, 9, 10, 11, 12, 13 at n 6..16 (= n - 3 from n 9 on; every witness has X = its phase
  length). Never X > n (L-NEW's x32_sc32 has X 37 > n 32 by a targeted climb).
- O from random starts: 2, 3, 4, 5, 11, 7, 8, 10, 10, 11, 12 at n 6..16 (noisy; two 300 s climbs at n 10 reached only 6).
- O seeded chain (each n seeded with the previous best padded with Even self-loops; 240 s, 300 s from n 28): every instance is ONE
  long phase in which every transition is OTHER-touching, pattern 23 (H1, not H2: o on the (sigma, tau)-play cycle, Xi(o) and W(o)
  with different cycle nodes) at every state, tau constant, theta 1-2 changes, w none. All passed check_instance.py.

| n | instance (sha1) | O = phase length | O/n | CROSS = X | FCH | RONLY | FLAT, WC | intervals | max FCH in an I (|F| - 1) | max RONLY in an I (|R| without o) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | b5_o11 (db4fe55a) | 11 | 1.10 | 4 | 7 | 0 | 0, 0 | 4 | 4 (7) | 0 |
| 12 | b5_os_n12 (7f626c27) | 16 | 1.33 | 6 | 10 | 0 | 0, 0 | 4 | 5 (8) | 0 |
| 14 | b5_os_n14 (74e10e25) | 20 | 1.43 | 7 | 12 | 1 | 0, 0 | 5 | 7 (10) | 1 (6) |
| 16 | b5_os_n16 (6297686b, vertex-minimal at O 24) | 24 | 1.50 | 9 | 13 | 2 | 0, 0 | 5 | 8 (11) | 2 (8) |
| 20 | b5_os_n20 (655e787b, vertex-minimal at O 32) | 32 | 1.60 | 9 | 21 | 2 | 0, 0 | 8 | 10 (15) | 2 (11) |
| 24 | b5_os_n24 (3aca1103) | 49 | 2.04 | 8 | 34 | 7 | 0, 0 | 8 | 14 (19) | 7 (16) |
| 28 | b5_os_n28 (ea287f50) | 60 | 2.14 | 11 | 42 | 7 | 0, 0 | 10 | 13 (23) | 6 (19) |
| 32 | b5_os_n32 (09b22134) | 67 | 2.09 | 9 | 50 | 8 | 0, 0 | 9 | 14 (27) | 8 (24) |
| 40 | b5_os_n40 (00fc4562) | 77 | 1.93 | 16 | 55 | 6 | 0, 0 | 12 | 17 (35) | 2 (31) |
(intervals = crossing-free intervals with at least one transition; the per-interval RONLY of a block equals that of its interval
here: one OTHER block per interval.)

Readings:
- DATA (exact, in the subsets): max X per phase 2 / 3 / 2 and max O per phase 1 / 2 / 1 at n 4 canonical / n 4 all starts / n 5
  subset; the maximum is always
  attained by a phase of exactly that length (every transition crossing / OTHER-touching).
- CONJECTURE (data: the tables, climbs n 6-16): X <= n - 3 for n >= 9 is NOT claimed (climb budget); X <= n seen everywhere except
  L-NEW's targeted x32_sc32 (37 > 32). (X) stays OPEN.
- DATA: O > n from n 10 on, O/n rising to about 2.1 at n 28 and falling to 1.93 at n 40 on the seeded chain: consistent with O ~ 2n
  (linear), superlinear not seen; climb budget shrinks with n (iterations 86k at n 12, 5.7k at n 40), so this is a lower bound only.
- DATA, against box 29: on every chain instance O = CROSS + FCH + RONLY (FLAT = WC = 0); FCH <= |F| - 1 per interval (Lemma F1°,
  PROVED by L-NEW) and RONLY <= |R| per interval (CONJECTURE (OB_R), not refuted; max ratio 8/24). The growth of O is F-changes
  times the number of crossing-free intervals (about X + 1), i.e. the (NH') <= (X) + F1° + (OB_R) shape; (NH') stays OPEN.
- Box 4 column completed by the full n 5 subset (DATA, exact): max (CYC') = 4 (theta 2, w 2) in a phase of 2 iterations (theta and w both change at each transition; instances/b5_n5_cyc4_0.pg, canonical start, sha1 f42767ef, check_instance OK) (box 4's
  44-slice partial had 2); max non-(h) per phase 3; longest phase 3; cyc hist {0: 68,612,254, 1: 11,954, 2: 140,572, 4: 20}.

## Box 6 (Lead GO 20:0xZ, D18): exact checks of referee packet P-N5-NH (c7981ee) and a seeded X chain (runs 20:10-23:00Z)
Labels (L40): DATA (exact = every run of the stated class) / CONJECTURE / OPEN. The statements checked are L-NEW's (PROVED by the
lane, unrefereed: F1°, TC) and a CONJECTURE ((OB_R)); a 0-violation table is evidence for the referees, not a proof.
box6.py checks per crossing-free interval I (definitions of P-N5-NH §0-§2):
- F1° : transitions of I with a Xi-change on F <= max(0, |F| - 1);
- TC (i): H1 <=> lambda_Xi(o) in F, H2 <=> tau(o) in F, both constant on I; (ii) under H2: lambda_W(o) = lambda_Xi(tau(o)), H3, (h)
  and "OTHER" constant on I; (iii) H1 and not H2: every state OTHER; (iv) not H1 and not H2: EQ <=> theta = w, EQ -> OTHER changes w;
- (OB_R): per OTHER block, R-only value-changing OTHER-touching transitions <= |R \ {o}| (OBRincl: <= |R| with o).

| table (results/box6/) | runs | crossing-free intervals | TC2 / TC3 / TC4 intervals | OTHER blocks | violations | max slack F1°, OB_R |
| --- | --- | --- | --- | --- | --- | --- |
| n 4 canonical | 4,828,736 | 6,678,702 | 2,624,262 / 141,252 / 3,913,188 | 0 (every OTHER-touching transition is a crossing) | 0 | 0, - |
| n 4 all starts (no forced, Even out-deg <= 2) | 7,340,032 | 15,176,360 | 6,018,598 / 930,240 / 8,227,522 | 2,800 | 0 | 0, 0 |
| n 5 subset, quarter 1 (game index = 0 mod 4) | 17,193,152 | 25,293,336 | 9,979,196 / 622,840 / 14,691,300 | 926 | 0 | 0, 0 |
| n 5 subset, quarter 2 (= 1 mod 4) | 17,191,424 | 25,000,542 | 9,876,682 / 531,362 / 14,592,498 | 774 | 0 | 0, 0 |
| n 5 subset, quarter 3 (= 2 mod 4) | 17,189,248 | 25,293,682 | 9,975,532 / 622,652 / 14,695,498 | 886 | 0 | 0, 0 |
| n 5 subset, quarter 4 (= 3 mod 4) | 17,190,976 | 24,999,572 | 9,872,944 / 530,338 / 14,596,290 | 846 | 0 | 0, 0 |
| n 5 subset, all four quarters = EXHAUSTIVE (68,764,800 runs, as box 5) | 68,764,800 | 100,587,132 | 39,704,354 / 2,307,192 / 58,575,586 | 3,432 | 0 | 0, 0 |
Max slack 0 = the bound is attained somewhere and never exceeded.

X chains (climb5.py X, raw X = crossing transitions per phase; canonical start; every instance check_instance OK):
| chain | n: X |
| --- | --- |
| one-wave, seed instances X_n16 (box 5, X 13), 300 s | 20: 17, 24: 21, 28: 25, 32: 29, 40: 36, 48: 37 (0.77-0.91n, 0 fallbacks) |
| waves, seed L-RED x32_waves32 (sha1 a0565c6e, X 65), 360 s | 32: 67, 36: 67, 40: 69, 48: 73, 56: 74, 64: 74 (bests reuse the seed's run) |
| waves, 1,500 s, seed b6_xw_n32 | 32: 75 (2.34n, b6_xl_n32, sha1 610a2da2), 40: 79 (1.98n), 48: 84 (1.75n) |
| waves, 2,400 s, seed b6_xl_n32 | 32: 77 (2.41n, b6_xl2_n32, sha1 909c7371) |
Readings (DATA): at fixed n, X rises with climb budget (n 32: 67 -> 75), so per-n maxima are budget-bound lower bounds and the n-trend
of the wave chain is not readable from them. Max X/n seen 2.41 (n 32: 67 at 360 s, 75 at 1,500 s, 77 at 2,400 s); no super-linear signal; (X) stays OPEN.

## Box 7 (Lead GO 23:2xZ, D18; amended 00:28Z, 00:33Z): exact checks of R23-R25 lemmas, J, K, S_o, and P-N5-U23 (runs 23:3xZ-)
Labels (L40): DATA (exact = every run of the stated class). Statements checked are refereed (R23, R24), in review (R25: FB, MONO) or
lane data quantities (J, K, S_o, E, K_W); 0 violations is evidence, not proof.
- box7.py: the lanes' checkers called unmodified: box31 casccheck.analyse (CASC, Theorem U1) and tbcheck.check_run (TB) with the
  start pair; L-SI coarse/tame.py scan_t's body with the start pair (J = non-tame transitions per phase; Mup_tame = MONO); xing
  zcount.zsigns (Z). Own: WM (W_{k+1} >= W_k pointwise at in-phase non-fallback transitions), LV' (X <= (n-1)(Z+1)+Z; LVr: '±'
  also resets the pure-sign run), FB (fallbacks per phase <= n_E(2n-1)(J+1)+J). Equal to tame.py / casccheck.py / zcount.py on
  jcl_lev_l_sc, jcl_x31_cu32i, u1t_cex2_n32, p3long_n14.
- box7w.py: K = wakes per phase (box32 nowake.census's NOWAKE_FAIL condition; NO-WAKE itself is FALSE, nowake_cex_n32), S_o per
  phase (census's formula; both checked against census on every run), used-level rises by cause (fallback > sigma_bar(o) > crossing
  > wake > other), and L-RED's u23x.analyse (P-N5-U23 exactly as frozen: CASC-U2, CASC-U3 (i)-(iii), corollaries; E per sub-run,
  K_W per stretch). Both reference modules start from the canonical pair; box7w rebinds start_pair in their modules (files unchanged;
  state sequences equal trace_fb on 3 start-pair instances). Equal to nowake.py on nowake_cex_n32 and u23x.py on u3ev_n16.
- box7e.py (u23check-based (E)) is superseded by box7w's u23x (Lead 00:28Z: u23check tests less than the packet); not run.

| box7 table (results/box7/) | runs | WM / LV' / FB-MONO tested | W-flat runs, R-switches | TB even / odd | U1 pieces | violations | max J | max Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| n 4 canonical | 4,828,736 | 107,596 / 188,320 / 1,974,244 | 7,984, 0 | 0 / 0 | 0 | 0 | 1 | 0 |
| n 4 all starts | 7,340,032 | 694,116 / 939,808 / 8,337,228 | 140,668, 0 | 17,068 / 576 | 100 | 0 (LV' tight) | 1 | 1 |
| n 5 subset quarter 1 (index = 0 mod 4) | 17,193,152 | 1,055,200 / 1,299,248 / 8,817,118 | 135,610, 0 | 6,604 / 42 | 92 | 0 | 1 | 1 |
| n 5 subset quarter 2 (index = 1 mod 4) | 17,191,424 | 1,131,306 / 1,396,338 / 8,592,786 | 143,352, 0 | 6,948 / 124 | 98 | 0 | 1 | 1 |
| n 5 subset quarter 3 (index = 2 mod 4) | 17,189,248 | 1,053,568 / 1,297,684 / 8,821,224 | 135,696, 0 | 6,608 / 42 | 52 | 0 | 1 | 1 |
| n 5 subset quarter 4 (index = 3 mod 4) | 17,190,976 | 1,132,668 / 1,397,614 / 8,593,598 | 144,150, 0 | 6,934 / 126 | 100 | 0 | 1 | 1 |
| n 5 subset, all 4 quarters | 68,764,800 | 4,372,742 / 5,390,884 / 34,824,726 | 558,808, 0 | 27,094 / 334 | 342 | 0 | 1 | 1 |

| box7w table | runs | max K | max S_o | rises fallback / sigma_bar(o) / crossing / wake / other | U2 / U3 / U23 stretches, switches | violations | max E | max K_W |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| n 4 canonical | 4,828,736 | 0 | 1 | none | 0 / 0 / 70,454, 576 | 0 | 1 | 1 |
| n 4 all starts | 7,340,032 | 0 | 2 | 4 / 0 / 0 / 0 / 0 | 848 / 0 / 145,098, 832 | 0 | 1 | 2 |
| n 5 subset quarter 1 (index = 0 mod 4) | 17,193,152 | 0 | 1 | none | 4 / 0 / 308,550, 10,240 | 0 | 1 | 2 |
| n 5 subset quarter 2 (index = 1 mod 4) | 17,191,424 | 0 | 1 | 0 / 4 / 0 / 0 / 0 | 6 / 0 / 365,930, 13,902 | 0 | 1 | 2 |
| n 5 subset quarter 3 (index = 2 mod 4) | 17,189,248 | 0 | 1 | none | 6 / 0 / 308,472, 10,210 | 0 | 1 | 2 |
| n 5 subset quarter 4 (index = 3 mod 4) | 17,190,976 | 0 | 1 | 0 / 12 / 0 / 0 / 0 | 4 / 0 / 365,956, 13,932 | 0 | 1 | 2 |
| n 5 subset, all 4 quarters | 68,764,800 | 0 | 1 | 0 / 16 / 0 / 0 / 0 | 20 / 0 / 1,348,908, 48,284 | 0 | 1 | 2 |
Readings (DATA, exact on these classes): CASC is vacuous through n 5 (no R-switch inside a W-flat run); J <= 1, K = 0 (no wake at all),
S_o <= 2, E <= 1, K_W <= 2 at n 4 and on the WHOLE n 5 subset (S_o <= 1 there); 0 violations of every box 7 check on all of it (box 7 complete).

## Box 8 (Lead GO 04:56Z / order 05:18Z, D18): R28 (OE, OX), R29 (CLS), R30 in landing (SN + fixes §2b) on the exact small-n classes
Labels (L40): DATA (exact = every run of the stated class); 0 violations is evidence, not proof. box8.py calls the referees' checkers
UNMODIFIED: REFEREE-2 oe_check / cls_check / sn_check / h1_check.check_run with the run's start pair (all rows), REFEREE oe_probe /
cls_probe / sn_probe.run (canonical start only: their trace has no start argument; reported in their own rows, Lead 05:18Z). Own code:
per-phase maxima read as deltas of the checkers' counters (J, K, X, eps, rho, T, X_SN); REL recomputed with sn_check's formula.
Phase key = the checkers' (lambda_Xi, tau). Validated on epsseg_cex_n48 (= sn_check inst mode: X_SN 5, crossings after prefix 13; REL 1).

| box8 (start-pair rows: REFEREE-2 checkers) | runs | violations | max J | max K | max X | max eps | max rho | max T | max X_SN | max REL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| n 4 canonical | 4,828,736 | 0 | 1 | 0 | 2 | 1 | 0 | 2 | 1 | 3 |
| n 4 all starts (even max-deg 2, no forced) | 7,340,032 | 0 | 1 | 0 | 3 | 1 | 1 | 3 | 2 | 3 |
| n 5 subset quarter 1 (box 7 class, index = 0 mod 4) | 17,193,152 | 0 | 1 | 0 | 2 | 1 | 0 | 3 | 2 | 2 |
| n 5 subset quarter 2 (index = 1 mod 4) | 17,191,424 | 0 | 1 | 0 | 2 | 1 | 1 | 3 | 2 | 2 |
BOX8ROW

| box8 (REFEREE probes, canonical start only) | runs | FAIL counters | max J | max K | max X | max eps | max rho | max T |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| n 4 canonical | 4,828,736 | 0 | 1 | 0 | 2 | 1 | 0 | 2 |
| n 5 subset quarter 1 | 17,193,152 | 0 (OGP_viol 1,476 = the refuted OG', counted by cls_probe, not a failure) | 1 | 0 | 2 | 1 | 0 | 3 |
| n 5 subset quarter 2 | 17,191,424 | 0 (OGP_viol 1,186, info) | 1 | 0 | 2 | 1 | 1 | 3 |
BOX8PROW

Teeth (n 4 canonical, REFEREE-2 counters): U-loc 780,352 checks; OE 139,566 off-crossing transitions (16 crossings with O > E); OX 188,320
phases (16 non-tame, all crossings, J = X); CN 120,082; TRANSFER 4,752; H3H2 6,818,268 states; LEAVE (H1) 17,344; CHOICE 80,027;
H1-DROP 6,752 (all P(theta_k) empty); OR / ABS-COUNT' 16 eps-transitions (all H1, all ABS-COUNT' tight). VACUOUS at n 4 canonical (no
instance of the hypothesis): R-STICK (no checks), NL (34,624 S4a (h) transitions, none with an admissible L), CLS1 / FBL / CLU (scope
fallbacks all theta = w, none with r >= 0), WK, ABS-L, crossings after an SN prefix (0).
Teeth (n 4 all starts): U-loc 4,018,288; OE 663,958 off-crossing (15,604 relevant sigma-bar(o) changes; 2,508 level-BOT tie moves, info);
S2 39,484 / S3 36,680 / S4 2,804; OX 939,808 phases (1,536 non-tame, all crossings; rho total 4); CN 449,502; TRANSFER 28,746; OFFGATE
18,560; NL 25,732 (j, L) checks on 9,780 transitions; R-STICK 3,288; LEAVE (H1) 47,698 (72 tight); crossings after an SN prefix 900
(max 1 per run); H1-DROP 152,650; OR / ABS-COUNT' 1,536 (828 tight). Still VACUOUS: CLS1 / FBL / CLU (all 79,112 scope fallbacks have
theta = w), WK (K = 0: no wake), ABS-L.
Teeth (n 5 quarter 1): U-loc 6,728,090; OE 844,468 off-crossing; OX 1,299,248 phases (520 non-tame, all crossings); CN 552,198;
TRANSFER 26,370; OFFGATE 12,132; NL 1,948 (j, L) checks; R-STICK 178; LEAVE (H1) 202,370; crossings after an SN prefix 312 (max 1 per run);
H1-DROP 39,852; OR / ABS-COUNT' 520 (all tight). Still VACUOUS: CLS1 / FBL / CLU (60,430 scope fallbacks, all theta = w), WK (K = 0), ABS-L.
Examples: X_SN 2 at prio [0,2,4,5,7] owner [1,0,0,0,0] succ [[2,4],[1],[0,3],[1,2],[1]] (canonical start); REL 2 at prio [0,2,4,6,8]
owner [1,0,0,0,0] succ [[2,4],[0],[4],[0],[2,3]] (canonical start).
Teeth (n 5 quarter 2): U-loc 7,234,290; OE 912,022; non-tame 952 (all crossings); CN 595,048; TRANSFER 28,326; OFFGATE 11,980; NL 2,072;
R-STICK 232; LEAVE 235,934; crossings after prefix 398; ABS-COUNT' 952 (all tight). Still VACUOUS: CLS1 / FBL / CLU (62,100 scope
fallbacks, all theta = w), WK, ABS-L.
