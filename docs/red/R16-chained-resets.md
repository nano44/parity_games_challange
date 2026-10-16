# R16: chained resets, the non-circular counter target (L-RED, 12:20Z by date -u; produced on Opus 5.5)
Target (Lead 11:59Z and 12:04Z; L-ALG GAP-A-M sections 14-15, l-alg ded46a5 / 8707f2c): c_i is circular (c_i is at most
the number of searches in the phase). A counter needs CHAINED resets: each change of piece i must re-enable a full cycle
of changes at deeper pieces, again and again.
Status words: DATA / READING.

## 1. Score (experiments/red/carry/phi_full.py replay_blocks; dtl_search.py fitnesses replay2 and phaselen)
- Per phase, F lists the first-difference depth-0 index of each consecutive search pair. Pieces are compared by
  (context, kind, V). If the depth-0 pieces are identical, the change is deeper ("D", inside a cut's recursion).
- A block at level i is a change at i plus the deeper changes that follow it, up to the next change at <= i.
- Score = max over (phase, i) with >= 2 blocks of the sum over blocks of (deeper changes - 1)^+. A K x K two-level counter
  scores about K(K - 1).
- Corpus (134 files): score histogram 0:119, 1:4, 2:5, 3:5, 4:4, 7:1. The longest phase is 16 searches at n = 32.

## 2. The best corpus instance is context TOGGLING, not a reset (L-ALG's dtl_searches15_n24, n = 24, score 7)
F = 0, 5, 2, 2, 2, 0, 2, D, D, D, D (Even phase, searches 0-11). Depth-0 pieces (original ids):
- Piece 0 (Dom(prevV), the full context |R| = 24): the return set toggles {12, 21} (s0) -> {12} (s1-s5) -> {12, 21}
  (s6-s11).
- So index 2 alternates between two contexts. Context A (|R| = 13) holds while 21 is in piece 0's return set (s0, s6-);
  context B (|R| = 14) holds in s1-s5.
- In B, index 2 changes in s1 -> s4 (the death of 5 goes 3, 3, 5, 7) and is stable at s5.
- Back in A at s6, index 2 does not restart. It goes from -1 (s0) straight to stable, with a larger V. A's progress was
  KEPT, and the later changes are deeper.
READING: the second "child cycle" runs in a second context with its own memory. It is not a replay of the first. By
Lemma F (same-context deaths only rise between carries) each context's changes are bounded by about n(n+2), so this shape
is counted by the per-context bound. A counter needs a child context to be FRESH at each parent change (a parent state
not seen before), and the child must replay a full cycle there, rather than finish at once with the tangles it already
learned. L-ALG's section 15 resets (child deaths drop at a new context) give the first half; the replay is the open half.

## 3. Staircases (L-ALG GAP-A-M 16 (a)) and their nesting, on A_DTL (12:46Z by date -u)
Tools in phi_full.py:
- staircases: the -1 Dom(prevV) calls at one (phase, depth-0 index, context) over consecutive searches, with their round
  counts M and the M-rises that bring NEW leaders (a return set not seen before in that staircase).
- nest2: (parent rises) x (child staircases at deeper depth-0 indices).
- nest2deep: the same, but with the children INSIDE cut recursions (depth >= 1). Approximation: the piece kind is not
  checked at depth >= 1.
- lemma_s: L-ALG's Lemma S on A_DTL.
DATA (134-139 files: the corpus, both h4 instances, tc+ 3-5):
- Lemma S on A_DTL: 604 fixed-context Dom(prevV) -1 pairs, 0 violations. This includes h4_disjoint_n20 and
  h4_notweaker_n20, whose later searches have deficits. In those games M rises (6 -> 8) or stays equal with the return
  set growing or unchanged. So R15's freedom changes WHICH set is returned, but not Lemma S on this data.
- New-leader M-rises per depth-0 staircase: histogram 0:129, 1:103, 2:8, 3:1, 4:1. The max is dtl_searches20_n32,
  piece 0: M = 4,4,4,4,5,6,6,6,6,7,7,7,7,8,8,8, with rises at s4, s5, s9, s13.
- nest2 (children at depth-0 indices): corpus max 3.
- nest2deep: 137 files score 0, 4 score 1, and dtl_searches20_n32 scores 16. That is 4 parent rises x 4 depth-1 child
  staircases, in contexts |R| = 19, 18, 18' and 17, each with ONE new-leader rise.
READING: dtl_searches20_n32 (L-ALG's F9/F10, "a one-digit instance") is a k=2 skeleton. The parent digit is the depth-0
piece-0 staircase. Each parent rise moves the depth-1 recursion under piece 1's cut to a fresh context. There the child
makes one new-leader rise (K_child = 1-2) before the next parent rise. A counter needs K_child to grow with n AND a third
level. The climbs nest2deep seeds 171-174 (two from dtl_searches20_n32, one from nest_nest_s83, one from
phi_flat_alive_n32) aim at K_child at n = 32. Results will follow in the next section.
