# N8d: Koh-Loho tree strategy iteration (perfect tree) with a SINGLE-SWITCH pivot rule (L-NEW successor 5, Opus 5.5; box 15)
Lead 03:16Z 2026-10-23 (date -u). Machinery: experiments/new/kl/kl.py unchanged (its §0 fidelity table in N8a-kohloho.md applies to every
function reused); new code experiments/new/kl/kl_single.py (only the pivot rule is new; map in §1).

## 0. Rules (FROZEN at 2026-10-23 03:21Z by date -u, before any N8d run; changes only in new sections)
Algorithm 1 of Koh-Loho (arXiv 2108.13338 §3) with line 5 "Pivot to a strategy τ′ by selecting admissible arc(s)" restricted to ONE arc:
- R1 (lowest index): among the Odd nodes that have at least one admissible arc (an Odd arc violated w.r.t. µ, §3), take the one with the
  smallest node id; switch it to its admissible arc with the LARGEST Tighten(µ, vw) (⊤ largest; ties: smallest successor id).
- R2 (random node): the same, but the node is drawn uniformly at random among the Odd nodes with an admissible arc, by
  random.Random(seed) created at the start of each Algorithm 1 run (primal and dual runs each start a fresh generator with the same seed);
  seed 1 for the bench, seeds 2-3 as robustness checks. The arc is again the largest-Tighten admissible arc.
Both rules switch exactly one arc per iteration, so Algorithm 1's invariants (no loose arcs in G_τ; µ feasible in G_τ after the least-
fixed-point step) hold as in §3 of the paper, and Theorem 3.1 (correctness, termination ≤ n·|L(T)| iterations) applies unchanged.
Why tree labels might differ from the VJ/discounted single-switch lower bounds (Friedmann LMCS 2011, B8; Avis-Friedmann 1305.3944,
single-switch round-robin; DLMM 2512.16684, index rules, B9): those constructions are for valuations that are a FUNCTION of the current
strategy, so a run is a walk in the strategy order. Koh-Loho's µ is the least fixed point ABOVE the previous µ: it depends on the history,
strategies may recur (§3), and the progress measure is µ, not the strategy. R53 §6 (L-RED) observed that on the H_k family one switch
closes the odd cycle and the least fixed point then jumps to ⊤, whereas switch-all keeps the cycle open while counting. That is the only
reason to expect a difference; there is no argument that single-switch avoids the crawl (a crawl needs only that SOME sequence of single
admissible switches keeps an odd cycle open, and the rule chooses which).
Measure: Algorithm 1 iterations (pivots), primal and dual; against n per family; fitted exponent where it grows.

## 1. Code ↔ paper (new functions only)
| kl_single.py | paper | note |
| --- | --- | --- |
| `rule_r1`, `rule_r2` | Algorithm 1 line 5 (pivot rule) | admissible arc = violated arc of an Odd node (§3); Tighten as in kl.py (§2.2) |
| `strategy_iteration` | Algorithm 1 | copy of kl.strategy_iteration with the rule passed as a function; τ_1 = first successor as in kl.py |
| `solve` | Thm 2.3 + dual game | identical to kl.solve |

## 2. Bench
Runs 03:22-03:42Z (date -u); experiments/new/kl/results/<family>.<rule>.csv; famF/G/H = R53's F_k/G_k/H_k (experiments/red/kl/famgen.py),
famL = L_k (gen_lk.py, N8a §6).
| family | rule | N: n / primal / dual pivots | outputs |
| --- | --- | --- | --- |
| famF | r1 | 0: 16/7/15; 1: 18/7/15; 2: 20/7/15; 3: 22/7/15; 4: 24/7/15 | all verified, = Oink zlk |
| famF | r2 (seed 1) | 0: 16/9/13; 1: 18/9/13; 2: 20/9/13; 3: 22/9/13; 4: 24/9/13 | all verified, = Oink zlk |
| famG | r1 | 0: 16/11/26; 1: 18/11/26; 2: 20/11/26; 3: 22/11/26; 4: 24/11/26 | all verified, = Oink zlk |
| famG | r2 (seed 1) | 0: 16/9/53; 1: 18/9/53; 2: 20/9/53; 3: 22/9/53; 4: 24/9/53 | all verified, = Oink zlk |
| famH | r1 | 0: 13/0/9; 1: 15/0/9; 2: 17/0/9; 3: 19/0/9; 4: 21/0/9; 5: 23/0/9 | all verified, = Oink zlk |
| famH | r2 (seed 1) | 0: 13/0/5; 1: 15/0/5; 2: 17/0/5; 3: 19/0/5; 4: 21/0/5; 5: 23/0/5 | all verified, = Oink zlk |
| famL | r1 | 0: 15/7/0; 2: 17/7/0; 3: 18/7/0; 4: 19/7/0; 5: 20/7/0; 6: 21/7/0 | all verified, = Oink zlk |
| famL | r2 (seed 1) | 0: 15/47/0; 2: 17/47/0; 3: 18/47/0; 4: 19/47/0; 5: 20/47/0; 6: 21/47/0 | all verified, = Oink zlk |
| tc | r1 | 1: 8/0/0; 2: 22/4/4; 4: 68/29/23; 6: 138/68/68; 8: 232/131/157; 10: 350/208/308; 12: 492/339/401; 14: 658/722/488 | all verified, = Oink zlk |
| tc | r2 (seed 1) | 1: 8/0/0; 2: 22/4/4; 4: 68/25/23; 6: 138/60/56; 8: 232/95/107; 10: 350/180/146; 12: 492/279/297; 14: 658/344/370 | all verified, = Oink zlk |
| tc+ | r1 | 1: 8/0/0; 2: 24/3/3; 3: 54/10/10; 4: 104/22/22; 5: 180/40/40; 6: 288/65/65 | all verified, = Oink zlk |
| tc+ | r2 (seed 1) | 1: 8/0/0; 2: 24/3/3; 3: 54/11/11; 4: 104/25/25; 5: 180/49/49; 6: 288/83/83 | all verified, = Oink zlk |
| switchallexp | r1 | 1: 21/1/14; 2: 35/2/39; 3: 49/3/84; 4: 63/4/165; 5: 77/5/318; 6: 91/6/615; 7: 105/7/1200; 8: 119/8/2361; 9: 133/9/4674; 10: 147/10/9291 | all verified, = Oink zlk |
| switchallexp | r2 (seed 1) | 1: 21/1/19; 2: 35/2/34; 3: 49/3/49; 4: 63/4/100; 5: 77/5/187; 6: 91/6/142 | all verified, = Oink zlk |
| switchbestexp | r1 | 1: 35/1/28; 2: 60/2/71; 3: 85/3/136; 4: 110/4/237; 5: 135/5/398; 6: 160/6/691; 7: 185/7/1236; 8: 210/8/2297 | all verified, = Oink zlk |
| switchbestexp | r2 (seed 1) | 1: 35/1/44; 2: 60/2/99; 3: 85/3/180; 4: 110/4/264; 5: 135/5/514; 6: 160/6/830 | all verified, = Oink zlk |
| counter_qpt | r1 | 2: 4/0/0; 4: 8/0/0; 8: 16/0/0; 12: 24/0/0; 16: 32/0/0; 20: 40/0/0 | all verified, = Oink zlk |
| counter_qpt | r2 (seed 1) | 2: 4/0/0; 4: 8/0/0; 8: 16/0/0; 12: 24/0/0; 16: 32/0/0; 20: 40/0/0 | all verified, = Oink zlk |
| counter_m | r1 | 2: 9/2/2; 4: 15/4/4; 8: 27/8/8; 12: 39/12/12; 16: 51/16/16; 20: 63/20/20 | all verified, = Oink zlk |
| counter_m | r2 (seed 1) | 2: 9/2/2; 4: 15/3/3; 8: 27/7/7; 12: 39/8/8; 16: 51/11/11; 20: 63/15/15 | all verified, = Oink zlk |
| counter_rr | r1 | 2: 8/0/2; 4: 16/2/4; 8: 32/6/8; 12: 48/10/12; 16: 64/14/16; 20: 80/18/20 | all verified, = Oink zlk |
| counter_rr | r2 (seed 1) | 2: 8/0/2; 4: 16/2/4; 8: 32/6/8; 12: 48/10/12; 16: 64/14/16; 20: 80/18/20 | all verified, = Oink zlk |
| counter_dp | r1 | 2: 12/2/1; 4: 20/6/4; 8: 36/20/16; 12: 52/42/36; 16: 68/72/64; 20: 84/110/100 | all verified, = Oink zlk |
| counter_dp | r2 (seed 1) | 2: 12/2/1; 4: 20/6/4; 8: 36/12/8; 12: 52/20/10; 16: 68/30/22; 20: 84/40/22 | all verified, = Oink zlk |
| counter_core | r1 | 2: 15/6/4; 4: 27/20/16; 6: 39/42/36; 8: 51/72/64; 10: 63/110/100 | all verified, = Oink zlk |
| counter_core | r2 (seed 1) | 2: 15/6/4; 4: 27/12/8; 6: 39/20/10; 8: 51/30/22; 10: 63/40/22 | all verified, = Oink zlk |
| counter_ortl | r1 | 2: 11/0/2; 4: 21/0/4; 6: 31/0/6; 8: 41/0/8; 10: 51/0/10 | all verified, = Oink zlk |
| counter_ortl | r2 (seed 1) | 2: 11/0/2; 4: 21/0/4; 6: 31/0/6; 8: 41/0/8; 10: 51/0/10 | all verified, = Oink zlk |
| counter_rob | r1 | 1: 14/5/5; 2: 31/17/16; 3: 54/44/42; 4: 83/102/101; 5: 118/223/229 | all verified, = Oink zlk |
| counter_rob | r2 (seed 1) | 1: 14/5/5; 2: 31/15/12; 3: 54/30/28; 4: 83/52/63; 5: 118/69/70 | all verified, = Oink zlk |
| counter_symsi | r1 | 1: 12/2/3; 2: 22/7/7; 3: 32/13/20; 4: 42/24/42; 6: 62/90/174 | all verified, = Oink zlk |
| counter_symsi | r2 (seed 1) | 1: 12/2/3; 2: 22/5/5; 3: 32/20/12; 4: 42/26/24; 6: 62/36/33 | all verified, = Oink zlk |
| recursiveladder | r1 | 2: 10/4/0; 4: 20/8/4; 6: 30/12/8; 8: 40/16/12; 10: 50/20/16 | all verified, = Oink zlk |
| recursiveladder | r2 (seed 1) | 2: 10/3/0; 4: 20/9/3; 6: 30/14/11; 8: 40/16/14; 10: 50/22/18 | all verified, = Oink zlk |

## 3. R1 is DEAD (2026-10-23 03:42Z by date -u)
switchallexp (Friedmann's switch-all family, experiments/hard-families/pgsolver_port.py), R1, dual pivots: 14, 39, 84, 165, 318, 615, 1,200,
2,361, 4,674, 9,291 for N = 1..10 (n = 14N + 7 = 21..147); from N = 5 on the ratio is 1.93-1.99 per step of N, i.e. ≈ 9·2^N = 2^{Θ(n)}.
Every output: verify.py OK and regions = Oink zlk (results/switchallexp.r1.csv; instances regenerable, sha1 in the CSV).
switchbestexp under R1: dual 28, 71, 136, 237, 398, 691, 1,236, 2,297 for N = 1..8 (×1.8 per N at the top). So the single-switch
lowest-index rule falls to Friedmann's families exactly as single-switch rules do on VJ valuations (B8): the tree labels do not help here.


## 4. R2 (random node, seeded) — polynomial-looking so far (2026-10-23 ~04:20Z by date -u; DATA under D1, not a claim)
- Crawl families (R53 F_k / G_k / H_k, N8a L_k): constant in k (seed 1: 13, 53, 5, 47 pivots), all verified (§2 table).
- Random corpus (rand10k, gen.py corpus seed 20261023, n 1-120): 10,000 / 10,000 verified (verify.py) and = Oink zlk; max 82 primal, 95 dual
  (results/rand10k.r2.csv). R1 for comparison: 10,000 / 10,000, max 71 / 79 (rand10k.r1.csv).
- Hard bench, seed 1: §2 table; all 13 families verified, = Oink zlk.
- Multi-seed on the growing families (dual pivots, every output verified, = Oink zlk; results/switchallexp.r2seeds.csv, growing.r2seeds.csv,
  sbe.r2seeds.csv):
| family | N (n) | seeds | dual pivots | mean |
| --- | --- | --- | --- | --- |
| switchallexp | 2 (35) / 4 (63) / 6 (91) / 8 (119) | 1-5 | | ≈ 37 / 100 / 168 / 374 |
| switchallexp | 10 (147) | 1-5 | 500, 458, 650, 533, 632 | 555 |
| switchallexp | 12 (175) | 1-5 | 689, 651, 1085, 836, 624 | 777 |
| switchallexp | 14 (203) | 1-5 | 440, 701, 1009, 1016, 1318 | 897 |
| switchbestexp | 6 (160) / 8 (210) / 10 (260) | 1-3 | 830, 406, 626 / 879, 994, 970 / 1714, 1729, 1207 | 621 / 948 / 1550 |
| switchbestexp | 12 (310) | 1-2 (3 running) | 1980, 2054 | ≈ 2017 |
| tc | 14 (658) | 1-3 | 370, 374, 520 (primal 344, 414, 450) | 421 |
- Fitted log-log slopes against n (means): switchallexp 91 → 203: 1.9; switchbestexp 160 → 310: 1.8 (local slopes 1.6, 2.3, 1.5).
  Compare R1 on switchallexp: ×2 per N (§3).
- Pending at this writing: tc N = 18, 22; counter_rob N = 7, 9; counter_symsi N = 8, 10 (3 seeds each); switchbestexp N = 12 seed 3.
- Caveat (stated now): R2 is a Random-Edge-type rule; on VJ valuations Random-Edge is exponential in expectation (Friedmann thesis Thm
  4.76, BARRIERS B10) on games of size O(n^4); those games are not in this bench. A Random-Edge family is the obvious first attack.

## 5. Runtime growth per hard family, R2 (recorded 05:26Z by date -u; generated by experiments/new/kl/growth_table.py from results/*.csv)
Pivots = primal + dual Algorithm 1 iterations (the measure). Seconds = wall time of kl_single.py on one core (Python, linear-scan Dijkstra,
per iteration about O(d·(n² + m·d)); see N8a §0), so seconds grow faster than pivots by the per-iteration cost. Slopes are
d(log y)/d(log n) over the last two sizes / over the whole range. Multi-seed means: seeds 1-5 (switchallexp) or 1-3 (others); every
multi-seed output verified (verify.py) and = Oink zlk (results/*r2seeds.csv).
| family | seed-1 bench: n → pivots (primal+dual), seconds | slope last / whole (pivots) | slope last / whole (seconds) | multi-seed means (n: mean primal+dual) |
| --- | --- | --- | --- | --- |
| tc | 8: 0 (0.05 s); 22: 8 (0.05 s); 68: 48 (0.1 s); 138: 116 (0.8 s); 232: 202 (3.4 s); 350: 326 (13 s); 492: 576 (44.3 s); 658: 714 (100.7 s) | 0.74 / 1.32 | 2.82 / 1.73 | 658: 824 (k=3); 1062: 1383 (k=3); 1562: 2439 (k=3) |
| tc+ | 8: 0 (0.05 s); 24: 6 (0.05 s); 54: 22 (0.05 s); 104: 50 (0.2 s); 180: 98 (1.1 s); 288: 166 (4.1 s) | 1.12 / 1.34 | 2.80 / 1.23 | - |
| switchallexp | 21: 20 (0.05 s); 35: 36 (0.1 s); 49: 52 (0.2 s); 63: 104 (0.5 s); 77: 192 (1.6 s); 91: 148 (1.7 s) | -1.56 / 1.36 | 0.36 / 2.40 | 147: 565 (k=5); 175: 789 (k=5); 203: 911 (k=5) |
| switchbestexp | 35: 45 (0.1 s); 60: 101 (0.5 s); 85: 183 (2 s); 110: 268 (5.4 s); 135: 519 (16.3 s); 160: 836 (38.8 s) | 2.81 / 1.92 | 5.10 / 3.92 | 160: 627 (k=3); 210: 956 (k=3); 260: 1560 (k=3); 310: 2081 (k=3) |
| counter_qpt | 4: 0 (0.05 s); 8: 0 (0.05 s); 16: 0 (0.05 s); 24: 0 (0.05 s); 32: 0 (0.05 s); 40: 0 (0.05 s) | - / - | 0.00 / 0.00 | - |
| counter_m | 9: 4 (0.05 s); 15: 6 (0.05 s); 27: 14 (0.05 s); 39: 16 (0.05 s); 51: 22 (0.05 s); 63: 30 (0.1 s) | 1.47 / 1.04 | 3.28 / 0.36 | - |
| counter_rr | 8: 2 (0.05 s); 16: 6 (0.05 s); 32: 14 (0.05 s); 48: 22 (0.05 s); 64: 30 (0.1 s); 80: 38 (0.1 s) | 1.06 / 1.28 | 0.00 / 0.30 | - |
| counter_dp | 12: 3 (0.05 s); 20: 10 (0.05 s); 36: 20 (0.05 s); 52: 30 (0.05 s); 68: 52 (0.1 s); 84: 62 (0.2 s) | 0.83 / 1.56 | 3.28 / 0.71 | - |
| counter_core | 15: 10 (0.05 s); 27: 20 (0.05 s); 39: 30 (0.05 s); 51: 52 (0.1 s); 63: 62 (0.2 s) | 0.83 / 1.27 | 3.28 / 0.97 | - |
| counter_ortl | 11: 2 (0.05 s); 21: 4 (0.05 s); 31: 6 (0.05 s); 41: 8 (0.05 s); 51: 10 (0.05 s) | 1.02 / 1.05 | 0.00 / 0.00 | - |
| counter_rob | 14: 10 (0.05 s); 31: 27 (0.05 s); 54: 58 (0.1 s); 83: 115 (0.4 s); 118: 139 (1 s) | 0.54 / 1.23 | 2.60 / 1.41 | 118: 137 (k=3); 206: 313 (k=3); 318: 575 (k=3) |
| counter_symsi | 12: 5 (0.05 s); 22: 10 (0.05 s); 32: 32 (0.05 s); 42: 50 (0.1 s); 62: 69 (0.4 s) | 0.83 / 1.60 | 3.56 / 1.27 | 62: 46 (k=3); 82: 119 (k=3); 102: 166 (k=3) |
| recursiveladder | 10: 3 (0.05 s); 20: 12 (0.05 s); 30: 25 (0.05 s); 40: 30 (0.05 s); 50: 40 (0.1 s) | 1.29 / 1.61 | 3.11 / 0.43 | - |
Completion of the §4 pending runs: tc N = 18 (n 1,062): primal 766, 708, 760 / dual 614, 696, 604; tc N = 22 (n 1,562): primal 1,114, 1,160,
1,204 / dual 1,308, 1,246, 1,284 (about 2,200 s each); counter_rob N = 7, 9 and counter_symsi N = 8, 10 in growing2.r2seeds.csv; all verified.
Reading: on every family the R2 pivot count grows like n^1 to n^2 over the sizes reached (largest whole-range slope: switchbestexp 1.9);
no family shows the per-N doubling that killed R1. This is DATA under D1; L-RED attacks R2 next (Lead 04:26Z; B10 is the prior).
