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
- DATA: from S3, N5 is LINEAR in N on both families: friedmannsubexp it = 4N + 3 for N = 2..8 (4 at N = 1); fearnleysubexp
  it ≈ 2.4N + 5. There are no fallbacks and 2-3 phases. N5-SF is linear too (≈ 4.3N), with SBC_σ ≈ 4N on friedmannsubexp and
  ≈ 2N on fearnleysubexp. SBC_τ is 0 everywhere, so τ never moves Even's best reply.
- The box-17 quantities on these runs: max SEG 13, EXC ≤ 0, L-WAVE′ gap ≤ 3, f 0.
- Honest limit: Friedmann's lower bounds hold for the snare-memorising rules from their own initial strategy. Nothing here says
  what N5 does from that start. S3 is N5's specified start.
