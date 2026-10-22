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
