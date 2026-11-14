### Table 1: engine check and RF on the named families (out/engine.out; unit: iterations = applied switch sets)
- Howard on Friedmann's G_n from iota, n = 1..6: 8, 26, 62, 134, 278, 566; 9 * 2^n - 10 = 8, 26, 62, 134, 278, 566
- RF on Friedmann's G_n from iota, n = 1..7: 5, 9, 12, 15, 18, 21, 24
- RF on Gamma3(G_k) from S3, k = 3..8: 6, 6, 8, 8, 10, 10
- RF on Gamma3^top(G_k) from S3, k = 3..8: 10, 12, 14, 16, 18, 20; Howard there, k = 3..6: 4, 5, 5, 5

### Table 2: where RF leaves Howard's run on Friedmann's G_n (out/viol.out)
- friedmann_G2: howard iterations 26 steps with a blocked vertex 10 of 26
- friedmann_G3: howard iterations 62 steps with a blocked vertex 24 of 62
  - G_3 pairs: blocked t by t 105
  - G_3 pairs: blocked d by t 75
  - G_3 pairs: blocked t by c 49
  - G_3 pairs: blocked t by r 42
  - G_3 pairs: blocked t by k 24
  - G_3 pairs: blocked c by r 7
  - G_3 pairs: blocked d by k 6
  - G_3 pairs: blocked d by r 5
  - G_3 pairs: blocked d by c 5
  - G_3 pairs: blocked r by k 4
  - G_3 pairs: blocked c by k 4
  - G_3 pairs: blocked g by d 4
  - G_3 pairs: blocked k by k 1
- friedmann_G4: howard iterations 134 steps with a blocked vertex 52 of 134

### Table 3: decoy k_i -> z_i -> d_i on Friedmann's G_n (out/decoy.out)
- DECOY247 friedmann_G2 decoy none n 24 rule howard iterations 26 even_wins 0
- DECOY247 friedmann_G2 decoy none n 24 rule rf iterations 9 even_wins 0
- DECOY247 friedmann_G2 decoy all n 26 rule howard iterations 8 even_wins 25
- DECOY247 friedmann_G2 decoy all n 26 rule rf iterations 11 even_wins 25
- DECOY247 friedmann_G2 decoy 1 n 25 rule howard iterations 5 even_wins 19
- DECOY247 friedmann_G2 decoy 1 n 25 rule rf iterations 6 even_wins 19
- DECOY247 friedmann_G3 decoy none n 34 rule howard iterations 62 even_wins 0
- DECOY247 friedmann_G3 decoy none n 34 rule rf iterations 12 even_wins 0
- DECOY247 friedmann_G3 decoy all n 37 rule howard iterations 10 even_wins 36
- DECOY247 friedmann_G3 decoy all n 37 rule rf iterations 15 even_wins 36
- DECOY247 friedmann_G3 decoy 1 n 35 rule howard iterations 6 even_wins 24
- DECOY247 friedmann_G3 decoy 1 n 35 rule rf iterations 7 even_wins 24
- DECOY247 friedmann_G4 decoy none n 44 rule howard iterations 134 even_wins 0
- DECOY247 friedmann_G4 decoy none n 44 rule rf iterations 15 even_wins 0
- DECOY247 friedmann_G4 decoy all n 48 rule howard iterations 12 even_wins 47
- DECOY247 friedmann_G4 decoy all n 48 rule rf iterations 19 even_wins 47
- DECOY247 friedmann_G4 decoy 1 n 45 rule howard iterations 8 even_wins 29
- DECOY247 friedmann_G4 decoy 1 n 45 rule rf iterations 9 even_wins 29

### Table 4: delay patches of G_n (out/patch.out; rf / howard iterations)
- [none] n = 1..5: RF 5, 9, 12, 15, 18; Howard 8, 26, 62, 134, 278
- [buf=1] n = 1..5: RF 5, 9, 12, 15, 18; Howard 8, 26, 62, 134, 278
- [buf=2] n = 1..5: RF 5, 9, 12, 15, 18; Howard 8, 26, 62, 134, 278
- [noCS] n = 1..5: RF 5, 9, 12, 15, 18; Howard 7, 23, 55, 119, 247
- [buf=2 noCS] n = 1..5: RF 5, 9, 12, 15, 18; Howard 7, 23, 55, 119, 247

### Table 5: PGSolver families from S3 (out/pgs.out; generators = trunk experiments/hard-families/pgsolver_port.py)
- switchallexp howard: N 1 (n 21): 10, N 2 (n 35): 30, N 3 (n 49): 70, N 4 (n 63): 150, N 5 (n 77): 310, N 6 (n 91): 630
- switchallexp rf: N 1 (n 21): 10, N 2 (n 35): 21, N 3 (n 49): 21, N 4 (n 63): 27, N 5 (n 77): 30, N 6 (n 91): 40, N 7 (n 105): 41, N 8 (n 119): 65, N 9 (n 133): 71, N 10 (n 147): 71, N 12 (n 175): 73, N 14 (n 203): 76, N 16 (n 231): 79
- switchbestexp howard: N 1 (n 35): 21, N 2 (n 60): 61, N 3 (n 85): 141, N 4 (n 110): 301, N 5 (n 135): 621, N 6 (n 160): 1261
- switchbestexp rf: N 1 (n 35): 17, N 2 (n 60): 38, N 3 (n 85): 43, N 4 (n 110): 69, N 5 (n 135): 74, N 6 (n 160): 82, N 7 (n 185): 93, N 8 (n 210): 106, N 9 (n 235): 117, N 10 (n 260): 132, N 12 (n 310): 158, N 14 (n 360): 184, N 16 (n 410): 210

### Table 6: exhaustive maxima (out/exh_*.out)
- EXH247 n 2 D 2 mode two rule rf part 0/1 games 27 runs 40 max_its 1 attained_by 13 howard_its_on_witness 1 secs 0
- EXH247 histogram of per-game maxima: 0:16 1:11
- EXH247 witness: parity 1; 0 0 0 0; 1 1 0 0,1; % start 0:0 1:1
- EXH247 n 3 D 3 mode two rule rf part 0/1 games 2401 runs 6516 max_its 4 attained_by 1 howard_its_on_witness 3 secs 0
- EXH247 histogram of per-game maxima: 0:661 1:1320 2:387 3:32 4:1
- EXH247 witness: parity 2; 0 0 0 0,1; 1 1 0 0,1,2; 2 2 0 0,1,2; % start 0:0 1:1 2:1
- EXH247 n 4 D 3 mode two rule rf part 0/1 games 576240 runs 3073280 max_its 8 attained_by 79 howard_its_on_witness 5 secs 137
- EXH247 histogram of per-game maxima: 0:74892 1:245980 2:177867 3:60410 4:12738 5:3268 6:838 7:223 8:24
- EXH247 witness: parity 3; 0 0 0 0,3; 1 1 0 0,1,2; 2 2 0 0,1,3; 3 3 0 0,1; % start 0:3 1:0 2:3 3:0
- EXH247 n 4 D 4 mode one rule rf part 0/1 games 50625 runs 1048576 max_its 8 attained_by 234 howard_its_on_witness 5 secs 66
- EXH247 histogram of per-game maxima: 0:295 1:5002 2:15658 3:16523 4:8216 5:3405 6:1060 7:396 8:70
- EXH247 witness: parity 3; 0 0 0 0,3; 1 1 0 0,1,2; 2 2 0 0,1,3; 3 3 0 0,1; % start 0:3 1:0 2:3 3:0

### Table 7: climbs (out/climbs/*.log; last BEST line and END line)
- climb_a4.log: BEST evals 234 n 4 m 12 rf_its 8 switches 11 howard_its 3 secs 0 | END evals 987384 best (8, 11) n 4 secs 150
- climb_a5.log: BEST evals 449432 n 5 m 15 rf_its 11 switches 12 howard_its 3 secs 93 | END evals 730132 best (11, 12) n 5 secs 150
- climb_a6.log: BEST evals 409762 n 6 m 18 rf_its 16 switches 21 howard_its 6 secs 136 | END evals 450907 best (16, 21) n 6 secs 150
- climb_a7.log: BEST evals 82161 n 7 m 20 rf_its 18 switches 19 howard_its 8 secs 32 | END evals 385263 best (18, 19) n 7 secs 150
- climb_a8.log: BEST evals 232204 n 8 m 23 rf_its 21 switches 27 howard_its 5 secs 124 | END evals 282138 best (21, 27) n 8 secs 150
- climb_a9.log: BEST evals 70996 n 9 m 27 rf_its 22 switches 29 howard_its 7 secs 44 | END evals 239844 best (22, 29) n 9 secs 150
- climb_r8.log: BEST evals 79215 n 8 m 23 score ret rf (6, 21, 13) howard (6, 21, 9) secs 33 | END evals 99051 best (6, 21, 13) n 8 secs 40
- climb_a10.log: BEST evals 24358 n 10 m 30 rf_its 29 switches 37 howard_its 5 secs 20 | END evals 193149 best (29, 37) n 10 secs 150
- climb_b12.log: BEST evals 149118 n 12 m 36 rf_its 31 switches 49 howard_its 9 secs 140 | END evals 310013 best (31, 49) n 12 secs 300
- climb_b14.log: BEST evals 81654 n 14 m 42 rf_its 33 switches 59 howard_its 11 secs 108 | END evals 247916 best (33, 59) n 14 secs 300
- climb_b16.log: BEST evals 169303 n 16 m 48 rf_its 35 switches 55 howard_its 5 secs 253 | END evals 196384 best (35, 55) n 16 secs 300
- climb_b20.log: BEST evals 36234 n 20 m 59 rf_its 46 switches 85 howard_its 9 secs 82 | END evals 137114 best (46, 85) n 20 secs 300
- climb_fg2.log: BEST evals 125463 n 26 m 202 rf_its 99 switches 213 howard_its 6 secs 900 | END evals 125486 best (99, 213) n 26 secs 900
