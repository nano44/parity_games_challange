# N8d second independent implementation (L-COMP, gauntlet step 2)
Lead GO 2026-10-23 05:41Z (date -u). Candidate N8d-R2 = Koh-Loho strategy iteration (arXiv 2108.13338, Algorithm 1) over the
perfect (n, d/2)-universal tree, one switch per iteration, pivot rule R2 (docs/new/N8d-single.md §0, frozen 03:21Z).

## Independence
Written from two sources only: the paper (arXiv 2108.13338**v5**, LMCS version, e-print sha256 7189eb2f673866257dd887bdfe0d660a
a76ba821dd9ba830d85bb2105a5c816c; sections §2 prelim, §3 strategy iteration (Algorithm 1), §4 label setting (Algorithms 2, 3,
Theorem 4.3)) and N8d-single.md §0. Not read before the freeze commit: experiments/new/kl/*.py (incl. gen_lk.py), N8a-kohloho.md
§1-§2, N8d-single.md §1. Read before the freeze (allowed by the brief): N8d-single.md §0 and §2 (bench table: family sizes and
counts), the harness (experiments/harness/), Oink.

## Files
| file | what |
| --- | --- |
| `kl2.py` | the implementation; `kl2.py GAME [OUT] --rule r1|r2 --seed S [--tau1 first|min] [--check]`; writes a paritysol solution with positional strategies for both players (D2 change 5); prints `pivots_primal P pivots_dual Q time T` on stderr |
| `selfcheck.py` | invariants of Algorithm 1 (mu non-decreasing, feasible in G_tau, no loose arcs in G_tau) and label-setting == naive lifting at every pivot; regions == py Zielonka; strategies pass verify.py; R1, R2 seeds 1-3, both tau_1 options; all 324 games n = 2, P = 2 plus 300 random n <= 9 |
| `bench.py` | family sweeps and corpora: every run checked against Oink zlk @ 8fbf0a7 (tl if zlk aborts, column `ref`) and verify.py |
| `check.sh` | fast self-check for scripts/verify.sh |

## Choices where the paper and §0 are silent (fixed before any comparison with L-NEW's data)
- C1 priorities: input max-parity, priorities p >= 0. The paper needs pi : V -> {1..d}, d even. I use pi' = p + 2 and d = least
  even number >= max pi'. Component xi_1 is never read by a truncation (pi' >= 2), stays 0; no priority compression (D2 change 1).
  Equivalent to "priority 0 allowed, components xi_i for odd i < d0, d0 = max p rounded up to even".
- C2 ell = n, M = {0..n-1} (perfect (n, d/2)-universal tree, §2.1).
- C3 tau_1: each Odd node's first successor in file order (`--tau1 min`: smallest id).
- C4 dual game: owners swapped, priorities p + 1. Odd's strategy = Even's strategy of the dual run; primal and dual regions must
  agree (asserted).
- C5 Even's strategy: a non-violated arc w.r.t. the final mu to the successor with the least label (ties: smallest id).
- Pivot: candidates = Odd nodes with an admissible arc, in increasing id; R1 takes the first; R2 takes
  `random.Random(seed).choice(sorted candidates)` (fresh generator per Algorithm 1 run). Arc: largest Tighten (TOP largest),
  ties smallest successor id (§0).
- Least fixed point mu^{G_tau up}: Algorithm 3 (LabelSetting, §4.1) with line 3 kept (lifts applied in node-id order) and
  Algorithm 2 (Dijkstra, §4) with a lazy binary heap; Phi_p numbers the SCCs of H_p in Tarjan completion order (sink = 1).
  By Thm 4.4 / Cor 4.3 (my count; labels thm:label-setting, cor:dijkstra) the result is unique, so these choices cannot change pivot counts; `--check` compares with naive lifting.

## Results (2026-10-23, date -u; freeze commit c0dc7a21, runs 05:50-08:40Z)
Every run: regions == Oink zlk @ 8fbf0a7 (zlk never aborted; no tl fallback was needed) and strategies of both players
verified by experiments/harness/verify.py. **0 MISMATCH, 0 BADSTRAT, 0 TIMEOUT, 0 ERROR in every file below.**

| bench | runs | result vs L-NEW (experiments/new/kl/results) |
| --- | --- | --- |
| rand10k (`gen.py corpus DIR 10000 20261023 --nmin 1 --nmax 120`, manifest sha1 c2b19244e676 confirmed), R1 + R2 seeds 1-3 | 40,000 | R1: 10,000/10,000 equal per instance (primal and dual); R2 seed 1: 10,000/10,000 equal per instance |
| 17 families at L-NEW's sizes (N8d §2), R1 + R2 seeds 1-10 | 1,155 | R1 equal on every row of every *.r1.csv; R2 seed 1 equal on every row of every *.r2.csv; L-NEW's extra seeds (growing/sbe/switchallexp .r2seeds.csv) equal on all 19 overlapping (family, N, seed) |
| switchallexp R2 extension N = 12..20, seeds 1-10 | 50 | beyond L-NEW's sizes (their seeds 1-5 at N = 12, 14 equal) |
| switchbestexp R2 extension N = 14, 16, seeds 1-10 (kl2.py) | 20 | seeds 1-5 equal L-RED R54 §3 seed for seed; equal to kl2fast on all 20 |

Exact R2 agreement means the R2 draw is the same in both codes; the spec's unpinned candidate-list order was resolved the same
way (increasing node id, `random.Random(seed).choice`). So the distributional comparison of the brief collapses to an exact one.
The choices C1 (priority shift) and C3 (tau_1 = first successor) are consistent with L-NEW's (R1 agrees on all 10,000 + family instances; I did not read their code to confirm).

R2 growth (mean of seeds 1-10, total pivots; tables in results/families.analysis.md): every family's local log-log slope against n
stays <= 3.3 and the mean grows like n^1..n^2 on all families. The two steepest:
- switchallexp (R1 doubles per N: dual 9,291 at N = 10, 33,157 for switchbestexp N = 12): R2 dual mean 212 (n = 91) -> 632 (147)
  -> 952 (203) -> 1,456 (231) -> 1,798 (259) -> 2,007 (287); global slope n = 91..287: 1.96; ratio per 2 steps of N falls
  (1.34, 1.13, 1.53, 1.24, 1.12). No sign of super-polynomial growth.
- switchbestexp: R2 dual mean 584 (n = 160) -> 970 (210) -> 1,435 (260) -> 2,290 (310) -> 2,959 (360) -> 3,827 (410) -> ... -> 13,691 (760, N = 30); see the next section.
rand10k: R2 mean total pivots by n-bin 2.2 (n < 20), 7.3, 12.9, 18.3, 23.1, 29.8 (n 100-120): linear in n.

## kl2fast.py (Lead task 07:41Z: switchbestexp N = 18-22) and the switchbestexp growth
kl2fast.py = kl2.py with the least-fixed-point step (Algorithms 2-3) and the admissible-arc scan + §0 arc choice in C (lfp.c via
ctypes); Algorithm 1's driver, the pivot rules and `random.Random(seed).choice` are kl2.py's Python. ~65x faster. Gate before use,
all passed: selfcheck (C LFP == naive lifting at every pivot, 624 games x 8 runs); exact reproduction of kl2.py on all 1,155 family
rows (`repro.py`, results/ vs results-fast/), on all 40,000 rand10k rows, and on switchbestexp N = 14, 16 seeds 1-10 (20 rows).
Every bench row records `impl` (kl2 | kl2fast).

switchbestexp under R2, seeds 1-10, 190 runs, all verified and = Oink zlk (results-fast/switchbestexp-{big,huge}.kl2fast.csv; N <= 12
from results/switchbestexp.kl2.csv; fit_sbe.py -> results-fast/switchbestexp-fit.txt). Dual pivots (primal = N always):
| N | 14 | 16 | 18 | 20 | 22 | 24 | 26 | 28 | 30 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| n | 360 | 410 | 460 | 510 | 560 | 610 | 660 | 710 | 760 |
| mean (10 seeds) | 2,959 | 3,827 | 5,151 | 5,987 | 6,928 | 9,569 | 8,855 | 13,242 | 13,691 |
| sd | 601 | 1,140 | 1,178 | 865 | 832 | 1,708 | 1,271 | 2,200 | 2,877 |
| mean seeds 1-5 | 3,014 | 4,052 | 5,162 | 5,875 | 6,941 | 9,747 | 8,545 | 14,413 | 12,986 |
Fits on log(mean): Lead series (L-NEW N 6-12, L-RED N 14-16, mine seeds 1-5 N >= 18), N 6..22: n^2.00 (SSR 0.019) vs 1.164^N (SSR
0.180); N 6..30: n^2.03 (SSR 0.106) vs 1.133^N (SSR 0.562). Mine, 10 seeds, N 6..30: n^2.05 (SSR 0.054) vs 1.134^N (SSR 0.550);
N 14..30: n^2.06 (SSR 0.047) vs 1.100^N (SSR 0.066). Ratio per +2N never > 1.6 twice in a row; N = 0 mod 4 sizes run higher than
their neighbours (24, 28 vs 26, 30). Reading: about n^2 on this family. DATA, not a bound.

## Box 2b (Lead 08:34Z): start strategy and tie-breaks, R2 seeds 1-5, kl2fast (results-2b/, box2b.sh, summary.md)
Settings: first = tau_1 first successor (as frozen); last = tau_1 last successor (identical to "edges reversed in file order",
checked on switchbestexp 8: both 0/1282 pivots, because arc ties are by successor id, not file order); rand = tau_1 drawn per Odd
node by random.Random(7), independent of R2's seed; relabel = node ids reversed (v -> n-1-v), which flips every smallest-id
tie-break (§0 arc ties) and keeps tau_1's arcs. Every output verified and = Oink zlk; 0 non-OK rows.
Mean total pivots (primal + dual):
| family | setting | sizes | means | fit |
| --- | --- | --- | --- | --- |
| switchallexp | first / last / rand / relabel | N 8..28 (n 119..399) | 363..3540 / 367..3991 / 434..3867 / 335..3749 | n^1.90 / n^1.99 / n^1.82 / n^1.90, power fits better in all four |
| switchbestexp | first / last / rand | N 10..30 (n 260..760) | 1522..13016 / 1475..11298 / 1412..12948 | n^1.93 / n^1.92 / n^2.14, power better |
| switchbestexp | relabel, 5 seeds | N 10..30 | 1471..13044 | n^2.09 (SSR 0.059) vs 1.118^N (SSR 0.053): tie at 5 seeds |
| switchbestexp | relabel, 15 seeds | N 10..38 (n 260..960) | 1370, 2637, 4281, 6351, 9727, 12637, 17172, 19085 | n^2.08 (SSR 0.012) vs 1.098^N (SSR 0.217): power; +4N ratios track the n^2 prediction |
| rand1k (first 1,000 rand10k games) | first / last / rand / relabel | n 1..120 | 16.67 / 17.07 / 16.29 / 16.99 (max 131 / 126 / 138 / 128) | - |
No setting changes the growth class. Data note (Lead item 3): switchbestexp N = 0 mod 4 runs high (first setting, 10 seeds: N 22 -> 24
+2,641 (z +4.2), 24 -> 26 -714 (z -1.0), 26 -> 28 +4,387 (z +5.2), 28 -> 30 +449 (z +0.4)): the one inversion (24 > 26) is within
1 SE, so variance explains it; the staircase itself (big steps into N = 0 mod 4, flat into N = 2 mod 4) is real at 10 seeds.
