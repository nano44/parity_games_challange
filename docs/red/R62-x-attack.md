# R62: attack on (X), crossing transitions per joint λ-phase (L-RED successor 14, box 32; GO 2026-10-24 ~18:03Z, date -u)
Target (Lead 18:0xZ): L-NEW box 28 §5c (READING) bounds a joint λ-phase by O(n⁴ (1 + X + O)), with X = crossing transitions (R
changes) and O = OTHER-touching transitions. Tasks:
- (a) the X growth law over n;
- (b) a third counter digit on L-SI's lev_l_sc, and whether its replay is a crossing wave;
- (c) any family with X exponential in a parameter.
Definitions are L-NEW's: R = vertices whose (σ, τ)-play reaches o, o excluded (box28 fbre.reach_o, equal to box25 thtrace.Rset
minus o); phase key = phaseprofile's (λ_Ξ, λ_U, τ(o)).
Labels per L40. No running-time claim. G-N5-TIME stays OPEN.

## 1. (b) The two-digit block on lev_l_sc IS a crossing wave (DATA; experiments/red/xing/wavetrace.py)
lev_l_sc (L-SI, sha1 86c17b07…, n 32), longest phase, states 8-54, 46 transitions, X = 33. Per transition: θ-change level
(VJ rank; L = length only; . = none), +k / −k = R entries / leaves, F = fallback:

    8:19+2 9:30+1 10:19 11:26 12:19 13:31 14:19 15:29 16:19 17:26 18:19+1 19:12+1 20:20+1 21:12+1 22:L+1 23:19+1 24:L+1
    25:L+2 26:17+1 27:14+3 28:16+1 29:13+1 30:L+1 31:.-19F 32:24 33:21+1 34:30+1 35:19 36:29 37:19 38:26 39:19+1 40:12+1
    41:20+1 42:12+1 43:L+2 44:19+1 45:L+1 46:L+2 47:17+1 48:14+3 49:16+1 50:13+1 51:L+2 52:28+4 53:23+4

- Digit 1 (level 19 re-fixed after every higher change, 9-17) changes θ WITHOUT crossings. These transitions add nothing to X.
- Digit 2 (the block replay):
  - wave 1: one-by-one entries at 18-30;
  - one fallback peels all 19 R-vertices at 31;
  - the carry: θ-changes at levels 24 and 21 (32-33);
  - wave 2 (34-51): the same level sequence (30, 19/29/19/26, 19, 12, 20, 12, L, 19, L, L, 17, 14, 16, 13, L) with entries again.
- So X ≈ (number of waves) × (wave size ≤ n): 33 ≈ 2 × 16. Each wave sits behind a fallback peel and a higher carry, the shape
  L-NEW saw on its X-climb bests (box 28 §5c).
- READING, what a third digit needs: under one carry above 24/21, TWO peel-carry-replay cycles of the (24/21)-block, each
  replaying the whole lower wave. X would then be about 4 waves; k digits would give about 2^(k−1) waves.
