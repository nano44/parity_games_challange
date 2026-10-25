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

## 2. J per phase (DATA; experiments/red/xing/jclimb.py, L-SI's coarse/tame.py at l-si 25d16cc8 unmodified)
- Baseline: max J per phase over 25 pinned in-class instances = 3 (zcl_cu_n48), in line with L-SI's "J ≤ 3 on 53".
- Climbs (fitness: max J per phase, total J, transitions), 2,400-2,700 s each, two rounds, 21:57-23:23Z:

| best (sha1) | n | J in one phase | phase length | seed | N5 it. / fb (n5 = n5b) |
| --- | --- | --- | --- | --- | --- |
| j5_n16 (9ae9df5e…) | 16 | 5 | 24 | x31_cu16 (J 1) | 30 / 4 |
| **j10_n24** (a3325093…) | 24 | **10** | 24 | x31_cu24 (J 0) | 25 / 1 |
| j7_n32 (78ec52e8…) | 32 | 7 | 48 | x31_rx32 (J 2) | 50 / 1 |
| j8_n32 (b6f2b87c…) | 32 | 8 | 52 | continuation of j7_n32 | 54 / 2 |
| j4_n40 (d1503d9c…) | 40 | 4 | 103 | x32_nest40 (J 2) | 106 / 4 |
| j7_n48 (c593e43c…) | 48 | 7 | 77 | zcl_cu_n48 (J 3) | 78 / 7 |
| j8_n48 (b50e6dd3…) | 48 | 8 | 85 | continuation of j7_n48 | 86 / 8 |

- All verified: Oink zlk OK, strategies verified, and n5b agrees.
- L-SI's mono.py on j5/j10/j8/j8: viol_coarse = viol_M = viol_conv = 0 (Lemma MONO holds).
- On every best, every non-tame transition is an NC failure with a θ-change above M_k (J_nc = J_thhigh = J), as Step 1 / J1 require.
  J_eq is at most 1 per phase, so most non-tame transitions do not land at θ = w.
- READING:
  - J rose from 3 to 10, but per n it stays at most about 0.42n (10 at n 24, inside a 24-transition phase: almost every second
    transition is non-tame).
  - At n 32 / 48 the climbs are budget-limited at 8.
  - A linear J is consistent with the data; a super-linear law is not visible. Theorem FB then gives O(n³) fallbacks per phase on
    these instances.
- CONJECTURE (data only): J = O(n) per joint λ-phase on o-cyclic 𝒞^1O. (J-poly) is neither refuted nor proved.

## 3. Verdict (labels per L40)
- (C) per phase ≤ 8 and (CL) holds with 0 violations: DATA, no growth.
- J per phase: new maximum 10 at n 24 (previously 3). Linear-looking at most. No kill. G-N5-TIME stays OPEN.
