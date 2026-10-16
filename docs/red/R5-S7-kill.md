# R5: S7 "most-improved" KILLED, and Question DF answered (L-RED, 2026-10-15, box on Question DF)

Target: docs/si/candidates/S7.md (claude/l-si 4719161): switch the improving edge maximising the number of vertices whose
valuation strictly improves; ties by the largest new valuation at v, then by index. Engines: L-SI's vjfast most-improved;
my experiments/red/vj.py most-improved (validated against vjfast in R3). Family: experiments/red/gens_red.py fhz_padded.

## Verdict: KILLED (instances experiments/red/instances/fhz_padded_n4.pg, fhz_padded_n6.pg)
| n | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vertices | 64 | 112 | 171 | 241 | 322 | 414 | 518 | 632 | 757 |
| S7 iterations (vjfast) | 16 | 44 | 104 | 228 | 480 | 988 | 2008 | 4052 | 8144 |
| S7 iterations (vj.py) | 16 | 44 | 104 | | | | | | |
| unpadded P_{n,1,1,1} (vjfast) | 8 | 14 | 22 | 32 | 44 | 58 | | | |
i(n) = 2 i(n-1) + 4n exactly on the table (n <= 10), so i(n) = 8 * 2^n - 4n - 8: exponential in n on a family of size Theta(n^2).
Start: best-reward (= FHZ's zero-edge tree B0; every Even choice leads to a priority-0 relay and the costly relay is the
last). Final regions equal Zielonka's and the strategies pass harness/verify.py (n = 3, 4 checked with vj.py). No index
tie-break fired. Every switch is non-cycle-creating (one-player acyclic game).

## The family
P_{n,1,1,1}: the sink-parity encoding (R2, fhz.py build) of Friedmann-Hansen-Zwick's one-player acyclic graph G_{n,1,1,1}
(arXiv 1410.7530 Fig. 3 p.9 and Table 1 p.14 with r = s = t = 1): levels i = 1..n with u_i, w_i, a_i (= a_{i,1,1}), b_i
(= b_{i,1}); u_i -> b_i (cost 0) or u_{i+1} (2^{2i}); w_i -> a_i (0) or w_{i+1} (2^{2i}); a_i -> b_i (0) or u_{i+1}
(2^{2i+1}); b_i -> w_{i+1} (0) or u_{i+1} (2^{2i+1} + 1); target t = u_{n+1} = w_{n+1}. The encoding gives every vertex of
G priority 0, every edge a priority-0 relay, class A (b_i -> w_{i+1}) an even vertex g_i, class B nothing, class C an odd
vertex per offset; all Even except the sink. Pads: on x_i (x in u, w, a, b) hang W_x (n + 1 - i) dangling Even vertices of
priority 0 with the single edge to x_i, W = (W_u, W_w, W_a, W_b) = (3, 4, 3, 1). Total pads 11 n(n+1)/2.
Other pad schemes (vjfast, n = 2..7): W = (1,1,1,1) linear: 10, 24, 44, 70, 102, 140 (second difference 4, 6, 6, 6: still
superlinear, slower); quadratic (n+1-i)^2 with W = (3,4,3,1): 16, 44, 104, 228, 480, 988 (same run); geometric 2^{n-i}
(exponential size): same 16, 44, 104, 228, 480; pads growing with the level, or none: polynomial (unpadded 8..58).

## Why (Lead reading; the reduction of R3 3c completed)
1. Question DF (Lead 14:00Z): YES. The longest downstream-first (DF) single-switch run on G_{n,1,1,1}, computed exactly by
   DP over all 2^{4n} trees (experiments/red/df_fhz.py), is 5, 20, 53, 124, 269 for n = 1..5 (unrestricted longest run
   7, 30, 85, 204, 451). The DF run is the FHZ counter's own increment sequence (set bit i, reset the lower bits, count
   up): in FHZ's graph the lower levels route through the higher levels, but a bit is set only when the levels above it
   are quiet, and the resets of the lower levels are produced by the switch at the higher level while that level stays
   quiet. (This is what Friedmann's gate counter could not do, R3 3b/3c: there the reopened higher gate becomes
   improving again before the lower bits move.)
2. S7 is downstream-first (Lemma D) and picks, among the improving vertices that are not downstream of one another, the
   one with the largest count = traffic + pads. In G_{n,1,1,1} the edges go only upward, so a level-i vertex has no traffic
   from other levels except through its own level: its count is its pads plus O(1). Pads decreasing with the level make
   "lower level first" the rule among route-incomparable candidates, which is the counter's order; the higher level is
   switched when it is the only improving one or when it is downstream of nothing improving. The run is then an
   exponential DF run of the counter.
3. The longest DF runs themselves are not S7 runs: an exact LP over the pad values (experiments/red/df_lp.py: one
   constraint per step and per route-incomparable improving competitor) is infeasible for every one of 300 sampled longest
   runs at n = 3, because they switch w_1 while u_1 is improving and later u_1 while w_1 is improving, and level-1 vertices
   carry no traffic that could flip the order; at n = 2 the LP is feasible and vjfast reproduces the full 20-switch run
   with the LP's pads. S7 follows a different DF run of the counter (16 of 20, 44 of 53, 104 of 124 switches), which is
   still exponential: i(n) = 2 i(n-1) + 4n.

## Evidence (commands)
```
python3 experiments/red/gens_red.py fhz_padded 6 > /tmp/f6.pg && <vjfast> most-improved /tmp/f6.pg      # 480
python3 experiments/red/vj.py most-improved experiments/red/instances/fhz_padded_n4.pg > /tmp/f4.sol     # 104
python3 experiments/harness/zielonka.py experiments/red/instances/fhz_padded_n4.pg | cut -d' ' -f1,2 | diff - <(cut -d' ' -f1,2 /tmp/f4.sol)
python3 experiments/red/df_fhz.py 4 1 1 1          # longest DF run 124, unrestricted 204
python3 experiments/red/pad_scheme.py <vjfast> -1 3 4 3 1 2 7   # 16 44 104 228 480 988
python3 experiments/red/df_lp.py <vjfast> 2        # LP feasible, vjfast reproduces the 20-switch DF run
```

## What this says about the fleet's SI programme
- S7 was the last defended single-switch rule; it dies on a ONE-PLAYER acyclic family, so its defence (iii) "padding
  must beat the upstream structure" fails whenever the base counter's bit switches carry no cross-level traffic, which
  FHZ's Random-Facet counter provides and Friedmann's and DLMM's counters do not.
- R3 3c stands corrected on one point: DF runs of exponential length exist (in one-player DAGs); the impossibility there
  is for Friedmann-spine gate counters only. The positive statement for L-SI ("downstream first") does not bound S7.
- Any single-switch rule that is downstream-first and orders route-incomparable candidates by a static per-vertex weight
  (pads) dies on this family; a rule that is DF and chooses by something pads cannot set (e.g. valuation content among
  incomparable candidates) would need a separate construction.

## DONE / FINDINGS / NEEDS
- DONE: fhz_padded family, instances n = 4, 6, both engines, Zielonka + verify.py, df_fhz.py (exact DF runs), df_lp.py
  (pad-feasibility LP), pad_scheme.py (schemes), df_search.py / df_fast.py (random small-game searches: DF longest runs
  grow slowly there, 6..18 for n = 5..9, which is why the structured family was needed).
- FINDINGS: S7 killed (exponential on Theta(n^2) vertices); Question DF answered YES with exact numbers on FHZ's graph.
- NEEDS: REFEREE: the growth is measured (two engines) and the recurrence i(n) = 2 i(n-1) + 4n is observed for n <= 9, not
  proved; a proof would follow FHZ's counter analysis for the S7 order (not attempted).
