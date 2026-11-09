# R229 item 6: the min-face class-height climb (Lead 05:51Z; guided by L-RED's CLASS-PAYS / GATE-FLIP-MIN) (L-RED successor 63)
Written 2026-11-09 (date -u in the commit). Labels: PROVED (lane, unrefereed) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD /
READING. Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1).
Target (Lead): a family where m(g) := min(cc(e_g), cc(β_g)) grows super-linearly in N + M at some gate g. Here cc(v) := #steps at which
class(v) = (Λ, E) changes, which is D^tot(v) − 1. GATE-FLIP-MIN gives flips(g) ≤ 2·m(g) + 1 (R229-box203 §3).
Tools: experiments/red/r229/nclimb229.py ORDER=MINH (score (max_g m(g), flips at that gate, C, −size); IDEAL-CYC, own engine, cap 600 steps
in the climb), hgt229.py (class heights), cls229.py (must-be-0 counters); out/minh229.out, out/ncMINH_*.log / .json.

## 0. Answer
- **No super-linear growth.** Best m(g) is 15 at N + M 200 and 39 at N + M 400. The ratio m/(N + M) is ≈ 0.07-0.10, the same scale as
  MW(n) (2n + 1 ≈ 0.068·(N + M)) and MWR(n) (n ≈ 0.033·(N + M) on the flipping gate, 2n + 1 at its β-face).
- **PROVED (trivial, lane): m(g) ≤ cc(v) ≤ T for every vertex.** A class changes at most once per step. So a super-linear m(g) needs a
  super-linear run, and m(g) is not an easier target than T itself. The climbs show it: at cap 400 the best m(g) is 39 with T = 44.
- The score is lexicographic in m first, so the climbs drifted to gates that DO NOT flip. The best at cap 400 from K1C16 has m = 39 at a
  gate with 0 flips; its max-flip gate has m = 24 and 32 flips. The climbs also gave up k = 1 (they did not filter on k; k ≥ 5 at the bests).
- All must-be-0 counters (GATE-CLASS, GATE-FLIP, CLASS-PAYS, B-ONLY, QUIET-N) are 0 on every climb best.

## 1. DATA (hgt229.py, own engine, cap 3000; unit: genome; maxcc = per-vertex MAXIMUM of cc; minh = max over gates of m(g); minhf = the same
## over gates with ≥ 1 flip, with the flips there; maxflip = per-gate MAXIMUM; out/minh229.out)
| instance | N + M | T | maxcc | minh | minhf (flips there) | maxflip | k |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MW26_2 | 783 | 163 | 106 | 53 | 53 (106) | 106 | 2 |
| MWR16_2 | 493 | 102 | 33 | 33 | 16 (33) | 33 | 1 |
| LC32_a13d9661 (L-COMP 15, claude/l-comp 0eb92268) | 275 | 49 | 33 | 18 | 17 (32) | 32 | 1 |
| K1C16_n400 | 400 | 51 | 36 | 36 | 21 (31) | 31 | 1 |
| ncMINH_200_2905 (seed MWR4_2, 2500 iterations) | 200 | 17 | 15 | 15 | 15 (10) | 10 | 5 |
| ncMINH_400_2906 (seed K1C16, 1500 iterations) | 400 | 44 | 39 | 39 | 24 (32) | 32 | 5-6 |
| ncMINH_400_2907 (seed LC32, 1200 iterations) | 393 | 36 | 30 | 27 | 27 (8) | 25 | 6-12 |
- Γ3 cross-check (L-NEW's fvs202 / gflip202 at fa17fdf6) on ncMINH_200_2905: T3 17, max flips 10 at the same gate; k 5.
- LC32 on GATE-FLIP-MIN: the max-flip gate has (cc(e), cc(β)) = (17, 33) and 32 flips; the bound is 2·17 + 1 = 35 (slack 3; cls229).
- READING: per unit of size, LC32 has the most flips at one gate (32 / 275 ≈ 0.12, against MW's 0.135 and MWR's 0.067). Every best stays
  on the line m(g), flips(g) ≤ T, with T ≤ 0.25·(N + M).
