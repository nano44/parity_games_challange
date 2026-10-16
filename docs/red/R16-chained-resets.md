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

## 4. Side datum: disjoint unions do not inflate c_i (12:54Z by date -u)
experiments/red/union/union.py builds disjoint unions with stacked, interleaved or equal priorities. Stacking k copies of
phi_idx_flat_n20 gives max c_i = 3 for k = 1..6 (5 searches throughout). Stacking k copies of nest_nest_s81 gives
3, 3, 5, 5 for k = 1..4. Unions of three different games give 7, not the product 27. The copies' pieces synchronise. This
is moot since c_i is circular (L-ALG 14), but it shows that unions are not a cheap way to inflate depth-0 contexts.

## 5. FINDING: Lemma S fails on A_DTL when the later run has a deficit (12:59Z by date -u)
Instance: experiments/red/carry/instances/lemmaS_viol_n20.pg (n = 20, sha1 5abc51bd…). It came from the lemmas climb,
seed 183, from dtl_mviol_n20, with the fitness rewarding leader drops (L-ALG c0aaa02's hint). Pinned Oink: 1 dominion,
18 tangles, 8 iterations, solution verified. Pinned in check.sh.
- Odd phase, searches 5 -> 6. It is a Dom(prevV) piece in the SAME context: my tracer's depth-0 call 4 (|R| = 16);
  dtl_pyref numbers it search 5 -> 6, piece 2 (|R| = 18, recorded at call entry). Both results are -1.
- M = 7 both times. The return set SHRINKS from {7, 14, 15} to {7} (original ids). Rounds (original ids):
  * s5: {1,5,6,7,8,12,13,14,15,18,19}, {1,5,6,7,13,14,15,18,19}, {5,6,7,13,14,15,18,19}, {5,6,7,14,15,18,19},
    {5,7,14,15,18}, {7,14,15,18}, {7,14,15}, {}
  * s6: the same through round 3, then {5,7,14,15,18,19}, {7,14,18,19}, {7}, {}
  Leaders 15 and 14 die at rounds 5 and 6 instead of 7. That is S2 ("at equal M the return set only grows") violated.
- L-ALG's dtl_deficit.py, unmodified: both calls are DEFICIT calls. The ideal (C6) result is STABLE in both searches
  (V = {1,5,6,7,8,12,13,14,15,18,19}). Pieces 0 and 1 of the same searches are deficit calls too.
- READING: this is consistent with L-ALG's statement that Lemma S is proved for A_DTL only under Theorem M-cond (no
  deficit in the later run). It is not a hole in the C6 proof. It does show that A_DTL's own staircases are NOT monotone
  under deficits. A deficit drops leaders, as L-ALG predicted. So the n(n+1)(n+1) child-context bound per fixed context
  needs (H4), a bound on deficit steps, before it applies to A_DTL. Here the deficit staircase sits where the ideal rule
  would already be stable.
- Second instance, with the round count DROPPING (13:06Z by date -u): experiments/red/carry/instances/lemmaS_Mdrop_n20.pg
  (n = 20, sha1 4793c740…; the same climb, 1,809 steps on). Pinned Oink: 1 dominion, 15 tangles, 7 iterations, solution
  verified. Pinned in check.sh. Odd searches 4 -> 5, both pieces in the same context and -1:
  * piece 0 (the full context, |R| = 20): M drops 10 -> 9, with the return set {9} unchanged (an S1 violation);
  * piece 1 (|R| = 19): M drops 9 -> 8, and the return set RE-TARGETS {0} -> {13} (S1 again; a DEF -1 -> -1 re-target
    with M going down).
  dtl_deficit.py, unmodified: all four calls are DEFICIT calls, and the ideal result is stable throughout. So under
  deficits A_DTL's round count M is not monotone at a fixed context either, and (H4)'s re-targets can come with
  decreasing M.
