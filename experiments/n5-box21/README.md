# Box 21: PGSolver friedmannsubexp / fearnleysubexp under N5, N5-SF and Oink (L-COMP successor 7)
Lead brief 2026-10-29 15:40Z (D18). All numbers are DATA. Start = SPEC S3 (best reward) throughout: PGSolver's stratimprgen generators
define no initial strategy, and Friedmann's papers' specified starts were not opened in this box.

## Port (independent; NOT yet byte-checked)
- hard-families/pgsolver_port.py `friedmannsubexp N`, `fearnleysubexp N` (`fearnleysubexp-nogadget N` = its -nogadget option).
  Transcribed line by line from github.com/tcsprojects/pgsolver d3cd624,
  src/lib/generators/policyiter/generators/friedmannsubexp.ml (90 lines) and fearnleysubexp.ml (86 lines). The symbolic numbering and
  output format are the existing SymbolicPG port, byte-identical to the d3cd624 binaries on switchallexp / switchbestexp
  (hard-families/pgsolver-binary-diff.md).
- Byte-for-byte check against the original binary: NOT RUN. Building PGSolver in this session was refused by the permission classifier
  ("Code from External"), as on 2026-10-14. Against L-LIT's T47-gen-*.py: NOT RUN, because T47 is not on claude/l-lit yet (b6111905).
  It runs as soon as T47 lands.
- Sanity (DATA): every vertex has priority ≥ 0 and ≥ 1 successor. Sizes match the .ml's node counts: fearnleysubexp
  n = 9N + 5 + 6N + 3·N(N−1)/2 (20, 38, 59, ...), and friedmannsubexp adds 6·N(N−1)/2 (20, 44, 77, ...). Oink zlk solves all 16.

## Runs (run21.py; results/run21_S3.log; check.sh gates the sha1s and two n5b counts)
| game | n | sha1 | N5 it | N5 fb | N5 phases | longest phase | N5-SF it | SF fb | SBC_σ | SBC_τ | SF LAM | SF SEG |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| friedmannsubexp_1 | 20 | aaf6175a | 4 | 0 | 2 | 2 | 4 | 0 | 1 | 0 | 0 | 2 |
| friedmannsubexp_2 | 44 | 13d55b1d | 10 | 0 | 3 | 5 | 8 | 0 | 5 | 0 | 0 | 6 |
| friedmannsubexp_3 | 77 | 90773868 | 15 | 0 | 3 | 7 | 11 | 0 | 9 | 0 | 0 | 10 |
| friedmannsubexp_4 | 119 | 280e5e7c | 19 | 0 | 3 | 9 | 14 | 0 | 12 | 0 | 0 | 13 |
| friedmannsubexp_5 | 170 | 52f345dd | 23 | 0 | 3 | 11 | 18 | 0 | 16 | 0 | 0 | 17 |
| friedmannsubexp_6 | 230 | 67408669 | 27 | 0 | 3 | 13 | 23 | 0 | 20 | 0 | 0 | 21 |
| friedmannsubexp_7 | 299 | 086ba814 | 31 | 0 | 3 | 15 | 28 | 0 | 26 | 0 | 0 | 27 |
| friedmannsubexp_8 | 377 | 42ad644b | 35 | 0 | 3 | 17 | 33 | 0 | 32 | 0 | 0 | 33 |
| fearnleysubexp_1 | 20 | 05a19c05 | 4 | 0 | 2 | 2 | 4 | 0 | 1 | 0 | 0 | 2 |
| fearnleysubexp_2 | 38 | 77cfde64 | 8 | 0 | 2 | 5 | 6 | 0 | 3 | 0 | 0 | 4 |
| fearnleysubexp_3 | 59 | 0e46c8e5 | 12 | 0 | 2 | 8 | 9 | 0 | 5 | 0 | 0 | 6 |
| fearnleysubexp_4 | 83 | ad297bca | 14 | 0 | 2 | 10 | 12 | 0 | 6 | 0 | 0 | 7 |
| fearnleysubexp_5 | 110 | 5350cad3 | 16 | 0 | 2 | 12 | 15 | 0 | 9 | 0 | 0 | 10 |
| fearnleysubexp_6 | 140 | 2a67e2d7 | 18 | 0 | 2 | 14 | 18 | 0 | 10 | 0 | 0 | 11 |
| fearnleysubexp_7 | 173 | 052aad65 | 21 | 0 | 2 | 17 | 21 | 0 | 13 | 0 | 0 | 14 |
| fearnleysubexp_8 | 209 | 8e259baa | 24 | 0 | 2 | 20 | 24 | 0 | 16 | 0 | 0 | 17 |
- Checks, all instances: n5b state sequence = n5x's; N5 regions = Oink zlk @ 8fbf0a7; N5 strategies pass verify.py. N5-SF does not
  cycle, its regions = Oink, and its final σ has no improving edge.
- DATA: from S3, N5 is LINEAR in N on both families: friedmannsubexp it = 4N + 3 for N = 3..8 (4, 10 at N = 1, 2); fearnleysubexp
  it 4, 8, 12, 14, 16, 18, 21, 24 (steps of 2-4). There are no fallbacks and 2-3 phases. N5-SF is linear too (≈ 4.3N), with SBC_σ ≈ 4N on friedmannsubexp and
  ≈ 2N on fearnleysubexp. SBC_τ is 0 everywhere, so τ never moves Even's best reply.
- The box-17 quantities on these runs: max SEG 13, EXC ≤ 0, L-WAVE′ gap ≤ 3, f 0.
- Honest limit: Friedmann's lower bounds hold for the snare-memorising rules from their own initial strategy. Nothing here says
  what N5 does from that start. S3 is N5's specified start.

## Byte check (Lead 16:03Z / 16:10Z): PASS against L-LIT T47
- docs/lit/T47-gen-pgsolver-snare.py (l-lit 02034f74; written independently of this port) vs hard-families/pgsolver_port.py, cmp of the
  full .pg: IDENTICAL for friedmannsubexp, fearnleysubexp and fearnleysubexp-nogadget at N = 1..12 (36 pairs), and the N = 1..5 sha1
  prefixes in the Lead's 16:03Z message match. Two independent transcriptions agree byte for byte. A PGSolver binary diff is still NOT RUN.
- Start (T47 §4): the generators define none, and PGSolver's snare solver starts from initial_strategy_by_best_reward (= SPEC S3 for
  Even), so the S3 runs above are the intended start. T47 and T46 name no designed (ι-type) start. Extra start run here: "lastedge"
  (PGSolver initial_strategy_by_last_edge for Even, S3 dual for Odd; run21.py --start lastedge).

## Both starts, N = 1..12 (results/run21_S3.log, results/run21_lastedge.log). Every row passes all checks: n5b = n5x states, N5 regions
## = Oink zlk, verify.py OK; N5-SF no cycle, regions = Oink, no improving edge left. "LE" = lastedge start (Even), S3 dual (Odd).
| N | friedmann n | N5 it S3 / LE | N5-SF it S3 / LE | SBC_σ S3 / LE | fearnley n | N5 it S3 / LE | N5-SF it S3 / LE | SBC_σ S3 / LE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 20 | 4 / 1 | 4 / 1 | 1 / 0 | 20 | 4 / 1 | 4 / 1 | 1 / 0 |
| 2 | 44 | 10 / 6 | 8 / 3 | 5 / 2 | 38 | 8 / 6 | 6 / 3 | 3 / 2 |
| 3 | 77 | 15 / 9 | 11 / 13 | 9 / 11 | 59 | 12 / 10 | 9 / 4 | 5 / 4 |
| 4 | 119 | 19 / 24 | 14 / 17 | 12 / 15 | 83 | 14 / 14 | 12 / 6 | 6 / 6 |
| 5 | 170 | 23 / 31 | 18 / 25 | 16 / 21 | 110 | 16 / 16 | 15 / 11 | 9 / 7 |
| 6 | 230 | 27 / 37 | 23 / 32 | 20 / 28 | 140 | 18 / 18 | 18 / 12 | 10 / 10 |
| 7 | 299 | 31 / 41 | 28 / 39 | 26 / 37 | 173 | 21 / 20 | 21 / 15 | 13 / 11 |
| 8 | 377 | 35 / 45 | 33 / 46 | 32 / 44 | 209 | 24 / 22 | 24 / 19 | 16 / 18 |
| 9 | 464 | 39 / 49 | 41 / 52 | 36 / 48 | 248 | 27 / 24 | 27 / 24 | 20 / 20 |
| 10 | 560 | 43 / 53 | 49 / 59 | 44 / 56 | 290 | 30 / 26 | 30 / 27 | 22 / 23 |
| 11 | 665 | 47 / 57 | 53 / 62 | 51 / 60 | 335 | 33 / 28 | 33 / 29 | 26 / 26 |
| 12 | 779 | 51 / 61 | 68 / 81 | 62 / 79 | 383 | 36 / 30 | 36 / 36 | 28 / 32 |
- SBC_τ = 0 and N5 fallbacks = 0 in every run. N5 phases: friedmann 3 (LE: 0, 1, 1, then 3); fearnley 2 (LE: 0, then 1).
- N5 stays linear in N for both starts: friedmann 4N + 3 (S3, N ≥ 3) and 4N + 13 (LE, N ≥ 6); fearnley 3N (S3, N ≥ 7) and 2N + 6 (LE, N ≥ 4).
- N5-SF's SBC on friedmannsubexp grows FASTER than linearly in N at the top of the range. S3 increments by N: 4, 4, 3, 4, 4, 6, 6, 4, 8, 7, 11.
  LE increments: …, 7, 9, 7, 4, 8, 4, 19. So SBC/N = 4.0 (N 8), 4.4 (N 10), 5.2 (N 12) from S3, and 5.5, 5.6, 6.6 from LE.
  In the game size n (≈ 4.5N² + 10.5N + 5), SBC/n FALLS (S3: 0.085 at N 8, 0.080 at N 12). This is DATA on N ≤ 12 only; the trend could be
  N log N, quadratic in N (= linear in n), or noise. fearnleysubexp SBC stays ≈ 2.3-2.7 N.

## N5-SF anatomy on friedmannsubexp, N = 1..20, both starts (Lead 16:46Z; sbcanat.py; results/sbcanat.log)
N = 13..20 instances are byte-identical to T47's generator. Every run: no cycle, regions = Oink zlk. Per N (S3 / LE): SF it, SBC_σ, DSB
(distinct σ̄ values), SBC/n.
| N | n | SF it | SBC_σ | DSB | SBC/n |
| --- | --- | --- | --- | --- | --- |
| 8 | 377 | 33 / 46 | 32 / 44 | 33 / 45 | 0.085 / 0.117 |
| 10 | 560 | 49 / 59 | 44 / 56 | 45 / 57 | 0.079 / 0.100 |
| 12 | 779 | 68 / 81 | 62 / 79 | 63 / 80 | 0.080 / 0.101 |
| 14 | 1,034 | 100 / 94 | 97 / 92 | 98 / 93 | 0.094 / 0.089 |
| 16 | 1,325 | 111 / 107 | 108 / 104 | 109 / 105 | 0.082 / 0.078 |
| 17 | 1,484 | 120 / 124 | 118 / 121 | 119 / 122 | 0.080 / 0.082 |
| 18 | 1,652 | 148 / 130 | 141 / 129 | 142 / 130 | 0.085 / 0.078 |
| 19 | 1,829 | 170 / 146 | 167 / 145 | 168 / 146 | 0.091 / 0.079 |
| 20 | 2,015 | 162 / 159 | 158 / 158 | 159 / 159 | 0.078 / 0.078 |
(all N in the log.)
- SBC/n does NOT rise. S3: 0.077-0.094 for N = 8..20, no trend (bumps at N 14, 19). LE: falls from 0.14 (N 3) to 0.078 (N 20).
- Least-squares fits of SBC_σ on N = 3..20 (RSS; residuals at N = 17..20):
  - S3: 9.43N − 38.2 (RSS 2,303; −4, 9, 26, 8); 2.82 N ln N − 12.6 (RSS 1,326; −5, 7, 22, 1); 0.410N² + 5.0 (RSS 535; −6, 3, 14, −11).
  - LE: 8.43N − 23.3 (RSS 625; 1, 1, 8, 13); 2.51 N ln N + 0.0 (RSS 262; 0, −2, 5, 8); 0.361N² + 16.2 (RSS 385; 1, −4, −1, −3).
  - N² fits best from S3, N ln N from LE. Both are consistent with SBC = Θ(n) (n ≈ 4.5N²), i.e. SBC ≈ 0.08n, and the fit cannot
    separate N ln N from N² on N ≤ 20. DATA only.
- DSB = SBC_σ + 1 in every run: σ̄ never returns to an earlier value. Every σ̄ change is to a NEW best reply.
- Where σ̄ changes (counted as (transition, vertex) pairs): only at the classes e (cycle centres), v and w (bad-entry selectors), on
  both starts. At N = 20 S3: e 358, v 1,406, w 1,720. Several vertices change per SBC transition (≈ 22 at N 20).
- Cycle-centre word (bit i = σ̄(e_i) = d(i,1)): NO binary counter. From S3 it starts at 2^N − 1 (all closed) and moves through
  e_words_count distinct values: 132 at N 20, far below 2^N. Consecutive words are never consecutive integers (e_binary_counter
  false for every N ≥ 2, both starts). From S3 at N 8 the words run 255, 254, 252, 249, 248, 242, 241, 228, …, 3, 1, 3, 0, 1, 0. They
  mostly fall, with a few re-openings at the end, so no counter completes.
- N5 at N = 13..16 (run21.py, all checks pass; n5b = n5x): S3 55, 59, 63, 67 = 4N + 3; LE 65, 69, 73, 77 = 4N + 13; 0 fallbacks. N5 stays
  exactly linear in N (so ~√n in the game size) up to n = 1,325, while N5-SF's SBC grows ~0.08n. The run21.py SF counts at N 13..16 equal
  sbcanat.py's (two scripts, same engine).
