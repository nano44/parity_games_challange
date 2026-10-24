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

## 2. (a) X over n, one seed family (DATA)
- Family: for each n, the first random o-cyclic 𝒞^1O game from L-NEW's rand_c1o (forced 0, Random(1000 + n)) that xclimb.fit
  accepts (experiments/red/xing/xseed.py).
- Climb: L-NEW's experiments/new/box28/xclimb.py at l-new 07614f6e, UNMODIFIED. Fitness = max over phases of (X − O, phase length).
  3,600 s each, 4 in parallel, 18:05-19:05Z.

| n | best (sha1) | X − O | O | peels (≥ 3 leave at once) | N5 iterations / fallbacks (n5 = n5b) | X / n |
| --- | --- | --- | --- | --- | --- | --- |
| 16 | x32_rand16 (978dcd05…) | 13 | 0 | 0 | 15 / 1 | 0.81 |
| 24 | x32_rand24 (730a0df9…) | 20 | 0 | 0 | 20 / 0 | 0.83 |
| 32 | x32_rand32 (33f2e1fe…) | 29 | 0 | 0 | 29 / 0 | 0.91 |
| 48 | x32_rand48 (86532180…) | 44 | 0 | 0 | 44 / 0 | 0.92 |
| 64 | x32_rand64 (e8142aed…; 3,000 s) | 55 | 0 | 0 | 56 / 1 | 0.86 |

- All verified: Oink zlk OK, strategies verified, and n5b (SPEC) agrees.
- Fit: X ≈ n − 3 to n − 9. Log-log slope 16 → 64: log(55/13)/log 4 = 1.04; X/n stays in 0.81-0.92. No super-linear law is visible.
- Shape: every best is ONE wave. Each iteration adds vertices to R, there are no peels, and X equals the whole run length. From
  random seeds the climb finds only the trivial linear shape within an hour.
- The multi-wave shape (X ≈ waves × wave size) appears only from structured seeds. L-NEW's bests (my count agrees: x32_sc32_final
  X 54 with 3 peels, x48_rt48_final X 70 with 8 peels) and the wave climbs of §3 test it.

## 3. Structured seeds: more waves (DATA; xclimb.py --target waves, 3,000 s each, 19:05-19:55Z)
| climb | n | seed | best (sha1) | X (mine = L-NEW xcount.py) | phase length | peels (≥ 3 leave) | θ-changes | N5 it. / fb (n5 = n5b) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| waves | 32 | L-NEW x32_sc32_final (X 54) | x32_waves32 (a0565c6e…) | **65** (2.0n) | 77 | 9 | 16 | 81 / 9 |
| waves | 48 | L-NEW x48_rt48_final (X 70) | x32_waves48 (4188f3e9…) | **78** (1.6n) | 85 | 19 | 3 | 89 / 19 |
| nest | 40 | lev_l_sc padded to 40 | x32_nest40 (2abed4ab…) | 51 (1.3n) | 53 | — | 19 | 58 / 2 |

- All verified: Oink zlk OK, strategies verified, and n5b agrees. O = 0 and w-changes = 0 on all three.
- x32_waves32 is the largest X per phase known at n 32 (L-NEW's box-28 best was 54). It is still about 2n.
- Anatomy (wavetrace.py):
  - waves32: waves of one-by-one entries, cut by fallback peels of −21, −25, −8 and −3 (×4), each followed by a θ-change
    (levels 30/31, 30, 28, 23/24/27/26). About 4 real waves, the later ones short.
  - waves48: one wave of ~29 entries, then about 10 consecutive fallbacks dismantling R in chunks of 3-6, then θ-change 46; a second
    wave of ~27 entries, again about 10 chunked fallbacks, then θ 45, 47 (+36 at once). The 19 "peels" are 3 waves, each R dismantled
    in pieces, not 19 waves.
- READING: X ≈ (carries + 1) × (wave size ≤ n). The climbs trade wave count against wave size: more peels came with smaller waves,
  and X stays at 1.3-2.0n.
- nest40 (counter target): m_r = 1, 2, 2, 3, 1, 1, 1, 6 top-down (levels 39 … 23). That is still one low digit (level 23 with 6)
  under single-use higher levels. No third digit.

## 4. (c) Exponential X: none found
No family or climb gives X beyond about 2n per phase (max 65 at n 32, 78 at n 48), and no X > n². G-N5-TIME stays OPEN.

## 5. Verdict (labels per L40)
- (X) over one random seed family: DATA, X ≈ 0.8-0.9n, one wave, slope 1.04 over n 16-64.
- Structured: X ≤ 2.0n (65 at n 32). Waves ≤ about 4 per phase on every best.
- CONJECTURE (data only): max X per joint λ-phase is O(n) on o-cyclic 𝒞^1O, i.e. waves per phase stay O(1). No super-linear law is
  visible.
- (b) A third digit is NOT achieved by climbing (nest40), and a hand-built k-digit counter is OPEN. The two-digit replay is a crossing
  wave (§1), so a k-digit construction would give X ≈ 2^(k−1)·n. That remains the design target.
- Tools: xseed.py, wavetrace.py, xclimb.py --target waves / nest (experiments/red/xing/).
