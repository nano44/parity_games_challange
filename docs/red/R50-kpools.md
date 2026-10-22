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

## 3. Union-only steps (no climb): NEST* and maximum learning positions (FIT=pool score; NEST*, max positions per search, searches with ≥ 2)
- k = 3, base nest5_n49 (NEST* 5, max 2 positions), stable order. Third part × placement → (NEST*, max positions, searches with ≥ 2):
  - nest3_n24: above (4, 3, 17); below (5, 3, 17); inter (5, 3, 17).
  - near4_n26: above (4, 3, 17); below (4, 3, 17); inter (4, 3, 17).
  - oseg_n26: above (5, 3, 15); below (5, 3, 15); inter (5, 3, 15).
  - onep_fdkey_n20: above (5, 3, 5); below (5, 3, 5); inter (5, 3, 5).
  - nest3_n20: above (4, 3, 10); below (4, 3, 10); inter (4, 3, 10).
- k = 4, base nest6_n75 (NEST* 6, max 3 positions), oink order:
  - oseg_n26: above (6, 4, 15); below (5, 4, 15).
  - nest3_n24: above (4, 4, 17); below (5, 4, 17).
  - onep_fdkey_n20: above (6, 4, 9); below (6, 4, 9).
- So every added part adds one simultaneous learning position (max positions = k). But a union alone never raised NEST* beyond the
  base, except 3 → 4 at k = 2 (R49 §5), and it often lowered it (masking). Each further level (4 → 5, 5 → 6) came from a graded
  climb on a union seed.

## 4. What the climbs change (Lead 00:21Z: "record exactly what the climb changes")
Tools: experiments/red/nest16/gdiff.py (diff), shrinkdiff.py (greedy revert toward the seed, keeping NEST* ≥ target in stable order),
subsets.py (all subsets of the remaining changes, NEST* in both orders).
- 5 → 6 (k = 3). Seed nest5_n49 ⊎ oseg_n26 (above) (parts: 0-48 nest5_n49, 49-74 oseg_n26); result nest6_n75.
  - The climb changed 5 owners, 23 vertices' successor sets, and the priority order (116 inversions).
  - The shrink reverted all owner changes and 20 of the successor sets, leaving instances/nest6min_n75.pg
    (sha1 e2c0d57f0b29e379a33dbcd9cc4f30fb28736563). It still has NEST* 6 in both orders: S 25, Oink 25 even iterations, verified.
  - Four vertices really move in the priority order (24 +32 ranks, 28 +19, 50 −33, 73 −27); the rest are knock-on ±1-3 shifts.
  - subsets.py over the 4 moves × 3 edge changes (128 subsets). NEST* 6 in both orders exactly when the edges 23→73, 55→27, 64→15
    are added AND vertex 73 is moved. Every other subset gives ≤ 5.
  - So the minimal 5 → 6 step is three CROSS-PART edges plus one priority move:
    - 23 → 73: a nest5 C-vertex to an oseg vertex.
    - 55 → 27: an oseg C-vertex to a chainfail-part vertex.
    - 64 → 15: an oseg C-vertex to a near4-part vertex.
    - 73 (oseg) moves 27 ranks down, into nest5's priority band.
- 4 → 5 (k = 2). Seed nest4u_n46 (parts 0-25 near4, 26-45 chainfail); result nest5_n49 (3 added vertices).
  - The greedy shrink keeps: 3 added vertices, 5 owner changes, about 15 successor-set changes, and 345 order inversions.
  - Many of the kept edges cross the part boundary (2→39, 44; 25→30, 33; 27→5; 30→9; 36→2, 3, 9, 13, 17; 44→11, 25). Not reduced further.
- Reading: after a union, the next level comes from coupling the parts directly: C-edges between parts plus interleaved
  priorities, on top of the coupling through mixed pieces. This is the clue for a recipe. A restricted climb that only adds
  cross-part edges and moves single priorities (experiments/red/nest16/crossclimb.py) is running on the k = 4 seed.

## 5. Is the minimal step a recipe? Mirror test on k = 4 (negative)
- Seed nest6_n75 ⊎ oseg_n26 (above): k = 4, n 101, NEST* 6. Its new oseg copy is vertices 75-100.
- Mirror of the §4 step (oseg vertex i ↦ 75 + i): add 81→27, 90→15 and 23→99, then move 99 down 0 / 27 / 40 ranks.
  NEST* (stable, oink): [3, 3], [4, 4] and [4, 4].
- Variant "into the previous oseg copy" (81→53, 90→64, 23→99), shift 0: [3, 3]. The remaining variants were lost to a container
  restart (01:2xZ).
- So the minimal step does not transfer by index mirroring: the extra edges collapse the phase instead of adding a level. The step is
  specific to the instance's dynamics, not a structural recipe.
