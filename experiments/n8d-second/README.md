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
  By Theorem 4.3 the result is unique, so these choices cannot change pivot counts; `--check` compares with naive lifting.

## Results
(filled after the freeze commit; see notes/L-COMP.md)
