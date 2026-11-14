# Box 66 N5-FRONT: exact one-flip (pre, post) frontier at m = 1, 2. At m = 2 it is the full trade-off line pre + post = T^R(2) + 1; at m = 3 the excess is at least 2 (kf1_d4_t10 attains (5, 5))
L-SI successor 39, 2026-11-05 (date -u: see the commit). Lead GO 12:31Z (BOX 66): for every 𝓛^R_2 genome and start with ONE
external flip, the Pareto frontier of (pre-flip length, post-flip length); test pre + post ≤ T^R(2) + c and the trade-off shape; m = 3
by climbs (lower bounds only).
Model: E_m of L-NEW box 160 §0 (R197 2-wide degree-2 ladders, ISO, level 0 external, b_0 flipped once).
Labels:
- EXACT: exhaustive enumeration (C, machine-checked, not Lean).
- DATA (climbs: lower bounds only), READING, CONJECTURE.

Not a TARGET.md claim. No polynomial bound. FLIP-ADD, SLOT-TRADE and G-N5-TIME stay OPEN.

## 0. Answer
- **Definitions.** For a start (u, level-0 configuration c, bit b = b_0(c)) and a flip time t on the flip-free b-run u = s_0, s_1, …:
  - pre := t;
  - post := L_(1−b)(s_t), the flip-free run with the other bit from s_t (max over level-0 configurations of that bit; by W-ONLY all of
    them give the same run above level 0);
  - STUCK: the flip is at the end of the b-run (t = L_b(u)); MID: before the end.
  - max (pre + post) over everything is T_1(m) (one flip, flip-free afterwards).
- **EXACT m = 1** (bff.c, all 7 ISO Ξ-graphs and every rank order, parity, gate order and start):
  - attained pairs: (0, 0..2), (1, 0..2), (2, 0);
  - frontier: (1, 2), (2, 0); max pre + post = 3 = T^R(1) + 1;
  - (2, 1) is NOT attained: a full pre-flip run of 2 leaves no post-flip step.
- **EXACT m = 2** (bff.c, all 5,941 ISO Ξ-graphs in 4 parts; every rank order, parity vector, in-level gate order and start):
  - attained pairs: exactly {(pre, post): post ≤ 4, pre + post ≤ 5}, i.e. (0, 0..4), (1, 0..4), (2, 0..3), (3, 0..2), (4, 0..1).
  - Frontier: (0, 4), (1, 4), (2, 3), (3, 2), (4, 1). Max pre + post = 5 = T^R(2) + 1, attained at EVERY pre = 1..4.
  - So the trade-off line is exact: **post ≤ min(T^R(2), T^R(2) + 1 − pre)**. Every frontier point with pre ≥ 1 is a STUCK flip.
  - The same runs reproduce T_0(2) = 4, T_1(2) = 5 and g*(2) = 4 (L-COMP 557b045b; box 65).
  - Witnesses (L-COMP bfk.c genome format: xt, rank, par, gate, start = full state incl. level 0; out/bff_m2_p*.txt):
    - (1, 4) STUCK: xt -1 4 -1 -1 -1 3 -1 2 rank 0 1 2 7 3 4 5 6 par 0 0 0 0 1 1 0 1 gate 0 2 1 3 16 18 19 17 32 33 34 35 start 4.
    - (2, 3) STUCK: xt -1 3 -1 -1 5 3 3 2 rank 0 1 4 7 5 6 2 3 par 0 0 1 0 0 1 0 1 gate 0 2 1 3 17 18 16 19 32 33 34 35 start 20.
    - (3, 2) STUCK: xt -1 -1 2 -1 5 2 3 2 rank 0 7 1 2 3 4 6 5 par 0 1 0 1 0 0 1 1 gate 0 2 1 3 16 17 18 19 32 33 34 35 start 53.
    - (4, 1) STUCK: xt -1 5 4 -1 -1 -1 4 3 rank 0 1 2 3 4 7 6 5 par 0 0 0 0 0 1 0 0 gate 0 2 1 3 16 17 18 19 32 33 34 35 start 17.
    - (0, 4) MID: xt -1 3 -1 4 -1 -1 4 2 rank 0 1 2 3 6 7 4 5 par 0 0 1 0 0 1 0 0 gate 0 2 1 3 16 18 19 17 32 33 34 35 start 16.
  - Cross-check: front.py (Python, box 64 simulator, XSIM-checked against L-NEW Gen) on 2,000 random m = 2 ISO ladders finds 14 of
    the 19 pairs and none outside the exact set.
- **m = 3 (DATA, lower bounds):** see §1.
  - (5, 5) is attained (kf1_d4_t10, L-NEW): pre + post = 10 = T^R(3) + 2. T^R(3) = 8 is EXACT (L-RED R197, L-COMP 27).
  - So the excess c(m) := T_1(m) − T^R(m) is 1, 1, ≥ 2 for m = 1, 2, 3. This is L-NEW box 160's one-flip increment row; L-NEW had
    T_1(3) ≥ 10, with ≥ 11 still running at its push.
- **READING.**
  - At m = 2 the one-flip budget is exactly «one more than a flip-free run, shared between the segments». Every split of T^R(2) + 1
    is attained, so the trade-off is tight at every pre: no constant smaller than 1 works for any split.
  - At m = 3 the halves are not shared: (5, 5) has both halves a full run of its own genome (T_0(G) = 5), with sum 10 > 8 + 1. The
    m = 2 line «pre + post ≤ T^R + 1» does not lift to m = 3. The best available form is pre + post ≤ T^R(m) + c(m) with
    c(3) ≥ 2.
  - The climbs (§1) give the m = 3 frontier lower bounds. Whether c(m) stays O(m) is FLIP-ADD at k = 1 and stays OPEN.
  - Mechanism at m = 3 (kf1_d4_t10, box 65 §2): the genome's two flip-free runs (b = 0 and b = 1) are each 5 long and chain at a
    common stuck state. A genome reaching T^R(3) = 8 under one bit has not been found to chain like this (max post after pre ≥ 6 is
    2 on the climbs).

## 1. m = 3 climbs (front.py --climb 3 p; max post subject to pre ≥ p; lower bounds; frozen copies in pin/)
- Champions are frozen in experiments/si/box66/pin/ (sha1 in pin/pins.sha1). The live climb outputs are in live/, gitignored.
- Each point used below was replayed with L-NEW's box 150 Gen (an independent step rule; replay inline in check66.sh).
- Combined lower bound: max post over pre ≥ p, on climbs, L-NEW witnesses and the box 65 pins.
  | pre ≥ p | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | max post | 8 | 7 | 7 | 5 | 5 | 5 | 3 | 1 | 0 |
  | point | (0, 8) | (1, 7) | (2, 7) | (5, 5) | (5, 5) | (5, 5) | (6, 3) | (7, 1) | (8, 0) |
  | pre + post | 8 | 8 | 9 | 10 | 10 | 10 | 9 | 8 | 8 |
  - Sources: (0, 8), (7, 1) and (8, 0) from pin/f_m3_p4_s1.json; (1, 7) from pin/f_m3_p2_s1.json; (2, 7) from box65/pin/j1_m3_s1.json;
    (5, 5) from L-NEW kf1_d4_t10; (6, 3) from pin/f_m3_p6_s1.json.
- Frontiers of single genomes:
  - pin/f_m3_p4_s1: (0, 8), (1, 7), (2, 6), (4, 5), (5, 3), (6, 2), (7, 1), (8, 0). This genome reaches T^R(3) = 8 under EACH
    bit separately, yet pre + post ≤ 9 = T^R(3) + 1 everywhere: the m = 2 line, one higher in the middle.
  - pin/f_m3_p2_s1: max sum 8. pin/f_m3_p6_s1: (0, 6), (1, 5), (6, 3), max sum 9.
  - kf1_d4_t10: the single point (5, 5), sum 10. Its own T_0(G) = 5, so both halves are full runs of a SHORT genome.
- READING (DATA only, m = 3):
  - At the ends (pre ≤ 1 or pre ≥ 7) the data obeys pre + post ≤ T^R(3) = 8.
  - The excess appears only in the middle, and the largest sum (10) is reached by a genome whose flip-free maximum is 5, not 8.
  - CONJECTURE BULGE (lane, DATA): pre + post ≤ T^R(m) + c(m) with the maximum taken at pre ≈ post. If the
    excess comes from «two half-length runs chained», then FLIP-ADD at k = 1 asks how long two flip-free runs of opposite bits
    can be when they chain at a common stuck state. That is a question about pairs of runs, not about one long run.
  - Not exact. An exhaustive m = 3 enumeration is out of reach for bff.c, since its rank-order loop is 12! per Ξ-graph.
    L-NEW's SAT frame with a pre / post side condition is the exact tool.

## 2. Process note
- Commit 35599262 (pushed) contained a check66.sh that fails: a for-loop's last test returned 1 inside $(...) under set -e. The
  same shell command stopped before wiring it into experiments/si/check.sh, so verify passed without running it.
- The exact m = 2 output files in that commit are unaffected.
- Fixed in the next commit: if/then in the loop; wired into check.sh; a negative control (expected set mutated to pre + post ≤ 4)
  makes the check fail as it should.
