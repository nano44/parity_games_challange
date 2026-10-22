# R50: k learning pools on 𝒞^1P (box 17; L-RED successor 10; produced on Opus 5.5)
Status: DATA plus readings, unrefereed. Started 2026-10-21 23:49Z (date -u), on the Lead's GO of 23:47Z. Target: R49 §9 (k parts /
k pools by union plus graded climb; NEST* against k and n).
Object and tools as in R49: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, both order data. Chains come from L-ALG's
unmodified b12_pot / b12_core (through ../xctx/xscore.py). Instance checks use experiments/red/nest16/kcheck.sh and table.py.

## 1. Learning positions, and the refined law (G-NEXT-1P)
- A learning position of a search is a depth-0 position where sptl extracts a tangle in that search (experiments/red/nest16/learnpos.py,
  a hook on ../xctx/tlog.py's sptl, L-ALG code unmodified).
- Per-search maxima: nest3_n24 2 (search 0 only), near4_n26 1, nest4u_n46 2 (searches 0-3), nest4uu_n51 3 (2 in searches 1-16),
  nest5_n49 2 (search 2 only).
- Correction to R49 §6 (frozen; corrected here): "every library phase has a single learning pool" is too strong. nest3_n24 learns at
  2 positions in search 0, and the library has 19 G-transitions whose own search learned at ≥ 2 positions.
- (G-NEXT-1P): let a G-transition at b (search i → i+1) be followed by a transition at c. If search i learned at only one
  position, then c ≤ b.
  - experiments/red/nest16/gnext1p.py on the 956-phase library (b12_topchain.classgames, DIST=1), identical in stable and oink order:
    - 345 cases with a 1-position search: all have c ≤ b.
    - 19 cases with a ≥ 2-position search: 16 have c ≤ b and 3 have c > b.
    - 0 violations.
  - The three c > b cases are exactly R49 §8's counterexamples (nest4u_n46 search 3, nest4uu_n51 search 16, nest5_n49 search 2).
    In each, search i learns at two positions. Reading: one feeds the G at b, and one lies deeper and feeds the next transition. The following search learns only at the deeper one (11, 7 and 10).

## 2. NEST* 6 on 𝒞^1P (2026-10-22 00:14Z, date -u): three-part union plus graded climb
- Seed (k = 3 parts): nest5_n49 ⊎ oseg_n26 with oseg's priorities above, built as in R49 §5. It has n 75 and score (5, 3, 15, 81, 20)
  under FIT=pool. nest5_n49 itself descends from near4_n26 ⊎ onep_chainfail_n20.
- Climb: experiments/red/nest16/starclimb.py, FIT=pool, oink order, seed 181, GROW 0.05, NMAX 90. NEST* 6 at step 103.
- instances/nest6_n75.pg: sha1 dc8b04cc7c16574d22b3a8bc4612ced2d83c6268, n 75, C = 1, in 𝒞^1P by L-ALG's fixd_oneplayer.inclass, all
  priorities distinct.
  - Both orders identical (L-ALG's unmodified b12_pot / b12_core): S 25, |P| 24, I 0,
    P = 0,1,6,9,7,4,9,3,8,16,17,17,16,1,8,7,16,13,1,12,12,7,0,6, NEST* 6.
  - Witness (experiments/red/nest16/witness.py): 0 (idx 0, 22) ⊃ 1 (1, 18) ⊃ 7 (4, 15) ⊃ 8 (8, 14) ⊃ 16 (9, 12) ⊃ the 17-pair (10, 11).
  - Pinned Oink 8fbf0a7 -v: 25 even iterations (= S), 1 odd, solution verified (64 strategies).
- Learning positions per search (oink order): 2,2,3,2,2,2,2,2,2, then 1 from search 9 on.
- (G-NEXT) violations: search 2→3 (G at 6, next at 9) and search 8→9 (G at 8, next at 16). Their own searches learn at 3 and 2
  positions, consistent with (G-NEXT-1P).
