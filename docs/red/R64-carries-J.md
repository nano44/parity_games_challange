# R64: nested carries, (CL), and J (L-RED successor 14, box 34; GO 2026-10-24 21:07Z, date -u)
Targets (Lead 21:07Z, refined 21:1xZ and 21:5xZ):
- (C) per phase: '+−' reversals at fallbacks, a drain counting once (docs/si/P-N5-Z-fixes-box5.md §2);
- L-SI's CONJECTURE (CL): carry level non-increasing while w is constant;
- then J = non-tame transitions per joint λ-phase (L-SI box 7, Theorem FB, PROVED by the lane: fallbacks ≤ n_E(2n−1)(J+1) + J; open
  core (J-poly)).
Reference counters, all L-SI's and unmodified: experiments/si/xing/{zcount,revpay,carries,clclimb}.py (trunk) and
experiments/si/coarse/tame.py (l-si 25d16cc8). Labels per L40. G-N5-TIME stays OPEN.

## 1. (C) and (CL) (DATA)
- (C) over all pinned in-class instances (revpay.py: '+−' reversals with a fallback as the reversing transition):

  | instance | n | (C) | Z |
  | --- | --- | --- | --- |
  | zcl_fb2_n32 | 32 | 8 | 18 |
  | zcl_rx_n32 | 32 | 7 | 14 |
  | zcl_fb1_n32 | 32 | 6 | 11 |
  | x32_waves32 | 32 | 5 | 10 |
  | others | 16-64 | 0-3 | |

  At n 48 / 64, (C) is 0-2. The ccl_* W-lowering bests have 23-33 W-lowerings but (C) = 1: one drain.
- Climbs:
  - L-SI's clclimb.py, unmodified (fitness: CL violations, W-lowerings), from four seeds. Stopped after about 8 minutes once the Lead
    pointed out that W-lowerings are drain-inflated: 18-26 W-lowerings, 0 (CL) violations.
  - experiments/red/xing/ccclimb.py (fitness: (CL) violations, (C) per phase, Z; L-SI's counters unmodified), 2,400 s each from
    zcl_fb2 / zcl_rx / zcl_fb1 / x32_waves32. (C) stays 8 / 7, and goes 6 → 7 and 5 → 6. **0 (CL) violations.**
- READING: (C) ≤ 8 everywhere, with no growth in n or under climbing. (CL) is not refuted.
