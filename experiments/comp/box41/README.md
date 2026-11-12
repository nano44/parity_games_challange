# L-COMP BOX 41 (successor 18; Lead 10:23Z 2026-11-12): DEEP3 counter, Deep_3 climbs, size-floor SCC-LIN climb, fit. All DATA.
Nothing here is a TARGET.md claim. CONJECTURE DEEP3 (L-SI box 100 §5.2) stays OPEN; SCC-LIN, U-FREE, G-N5-TIME stay OPEN; N5′-xi stays a
CANDIDATE (D1).

## Item 1 COUNTER: deep41.py (MY Γ3 engine box34/own34.py; σ̄_t = Odd's optimal counterstrategy, n5b; relevance (priority, index))
- From box 100's TEXT (claude/l-si 23d39400, docs/si/box100-scclin.md §2 TWO-CROSS, §3 depth, §4 Deep_c / internal / t0, §5.2 counter;
  quoted in the script header), not cross100.py. Depth: −1 if Λ changes; else #Π_t above z (z = most relevant element of Π_t Δ Π_(t+1));
  |Π_t| for a length-only change. The «D1 note» (L-RED 66, docs/red/R234-lamgap.md, not on origin when read): Lead 10:38Z confirms it is
  this rule (a length-only change is shallow iff |Π_t| <= c); nothing else applied.
- Counters (unit; scope): whole run, every gate, states 0..T3 (= box 100's): deep [flip charged to depth > 3], dmax [max charged depth],
  unm [flip with Ω(a) unchanged: must be 0], qflip, qint, gates, multi, maxfl. Box 100 §4's own quantity: DeepInt = Σ_C Deep_3(C) [flip at
  an INTERNAL gate (both targets in its mover's SCC) at a step t >= t0(C) = box 99's e(C), charged to depth > 3]; DeepBig (largest SCC);
  dmaxInt.
- Cross-check (xcheck41.sh; out/deep41_inst26.out, out/xcheck41.log) on the 26 frozen (box40/inst = L-RED r232 SHA1SUMS) vs L-SI
  out/cross100_inst.out: T3, deep, dmax, qflip, qint, gates, unm, multi, maxfl: **0 mismatching genomes**. Totals deep 79, dmax 6 (MW8 8,
  MW32 32, DHIB26 24, DWT20 9, C6G8 3, DHIB18 2, Kprev_8 1). Control CTRL=1 (charge to the face Odd moves TO) fires: unm MWR4_2 13, C6G8 51,
  DHIB26 98 (out/deep41_ctrl.out).
- **Split (Lead 10:38Z: «the useful number»)**: DEEP3 proper, Σ_C Deep_3(C) = **38** on the 26 (C6G8 3, DWT20 9, DHIB26 24, DHIB18 2, all
  in the largest SCC). MW8 / MW32 / Kprev_8's 41 deep flips are all at NON-internal gates (Deep_3 = 0): the whole-run «deep» overcounts
  DEEP3 by n on MW(n).

## Item 2 CLIMB: climb41.py, band41.sh (score (Σ_C Deep_3(C), dmaxInt, whole-run deep); 1 restart x 200 proposals per stream; no k constraint)
- Second engine on every new best: L-SI cross100.py (worktree claude/l-si 23d39400) on L-RED how3_232 (worktree claude/l-red 59daaef2),
  LNEW = archive of l-new fcba92fc, CMAX 3: T3, deep, dmax, qflip, qint, gates, unm equal: **11 / 11 bests agree**. (cross100 has no
  internal/after-t0 split; on every best here the whole-run deep it confirms equals or bounds my DeepInt: D300b: DeepInt 10 = deep 10.)
- Seeds (Lead reading, approved 10:38Z): DHIB26 / DHIB18 (N + M 400) and RWX (328) lie above both bands and the moves cannot shrink.
  | stream | seed (Deep_3, dmax) | best Deep_3 | dmaxInt | whole-run deep | N + M | sha1 |
  | --- | --- | --- | --- | --- | --- | --- |
  | D150a | MW4 (0, −; whole-run deep 4 external) | 2 | 4 | 2 | 160 | 9faa99eab0bb |
  | D150b | C98_4_5_3 grown to 140 (0, 2) | 0 (no gain) | 2 | 0 | 140 | 5c5a0868309e |
  | D300a | MW9 (0, −; deep 9 external) | 0 (whole-run deep 9 -> 15, all external) | − | 15 | 298 | 9094d162457 |
  | D300b | C6G8 grown to 281 (5, 5) | **10** | 5 | 10 | 285 | 79f3cd1167d1 (out/climb41/BEST_D300b_D10_dm5_W10_NM285_79f3cd11.json) |
  Growth step: C6G8 (Deep_3 3 at 204) grew to Deep_3 5 at 281 under growth-only moves (sha1 203a3c81).

## Item 3 (budget left): size-floor SCC-LIN climb (SCORE=sccfloor, C_max >= 40 movers, score loc/M_C; band 300; 1 x 200; second engine
L-SI scc99.py as box 40)
- F300 from MWR9 (0.314, C_max 89 movers): best **0.427** (loc 58 / M_C 136, C_max 68 movers, N + M 299, T3 59, sha1 edefe11f95be);
  7 / 7 bests agree with scc99; no ALERT (loc > M_C or ratio > 1: none). So with the floor, the giant-SCC ratio does rise above MWR's
  0.31, to 0.43, by trimming options of the giant SCC while keeping loc ~ T3.

## Item 4 FIT: fit41.py, out/fit41.out
- Envelope (max Σ_C Deep_3(C) per size): (160, 2) D150a, (204, 3) C6G8_n54, (285, 10) D300b, (364, 9) DWT20_2803, (400, 24) DHIB26_2804:
  log-log exponent **2.45 +- 0.46**; climb maxima alone (2 points) 2.79.
- Verdict: **NOT identified** as a growth law. Reasons: the five points are five different families (MW-derived, C6G8, DWT, DHIB) over a
  size range of only 2.5x; search effort is unequal (D300b's seed already had Deep_3 5, D150's seeds had 0; DHIB26 and DWT20 are older
  climb bests of other lanes); no family is measured at >= 3 sizes. Within the one family measured at several sizes (MW(n), n 4-32),
  Deep_3 = 0 and dmax = 4 flat. dmax over everything: 4 (150 band), 5 (300 band), 6 (DHIB26 at 400): no family where dmax grows with n.
- Flag (READING): the numbers are compatible with super-linear growth across families (Deep_3 / (N + M) rises 0.0125 -> 0.035 -> 0.06),
  so the next measurement should hold the family fixed (C6G8- or DHIB-type genomes grown at 3+ sizes, same effort per size).

## Files
deep41.py, xcheck41.sh, climb41.py (+ box39/mut39.py, box40/scc40.py), band41.sh, fit41.py; inst/ (seeds; SHA1SUMS; L-SI's
cross100_inst.out copy); out/.
