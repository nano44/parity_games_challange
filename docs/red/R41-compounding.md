# R41: compounding tail resets on staircase products (L-RED box 12; produced on Opus 5.5)
Status: DATA plus READING, unrefereed. Target: Lead box-12 item 2 (L-ALG GAP-A-M §28f/§29: a counter needs a position j whose
context rises ≥ 2 times, each rise enabled by a tangle born in the tail below j, with the tail re-rising ≥ 2 times between).
Started 2026-10-18 14:05Z (date -u). L-ALG tools unmodified (fixd_fdpos.py, fixd_outcome.py, fixd_enable.py; l-alg 50e66d32 =
in-tree copies); pinned Oink @ 8fbf0a7 verifies every instance.

## 1. Measures
- fixd_fdpos.py: per phase, the depth-0 chain position of each transition's first difference ("positions").
- NEST (experiments/red/tcpert/carryclimb.py, nest()): 1 for any transition; for a position p with ≥ 2 transitions,
  1 + max over the gaps between consecutive transitions at p of NEST(gap restricted to positions > p). A binary counter over
  k positions scores k; leanT (positions strictly falling) scores 1; a root rise interleaved with a falling staircase scores 2.
  (L-ALG's "reset-depth proxy" overcounts staircases: leanT(8) has proxy 7 but never compounds.)

## 2. Why leanT cannot carry (box 11, R40 §12)
Every rise is −1 -> stable (fixd_outcome on leanT(8): {-1->ST: 7}); the stable piece's Dom swallows all lower rungs; the tail
below is the Odd side, identical every search. The lower rungs' state survives as a sub-chain of the new tangle, never as a
re-cut tail. fixd_enable: no enabling tangle fires at R_j in any transition.

## 3. Staircase products (DATA)
- Base: disjoint union leanT(a) + leanT(b), copy 2's priorities shifted up by an even amount (prodclimb.py / carryclimb.py).
- With climbed individual cross edges, fixd_outcome (stable): products a = b = 6 / 8 (19-29 searches) have PV-SHRINK rises
  (the §27d reset) 3 / 6 times; leanT has 0; ctx13_n40 has 13.
- nest4_n80.pg (sha1 31c02e548d82; experiments/red/tcpert/instances/prod/): leanT(5) + leanT(5) + 11 cross edges
  (carryclimb.py seed 4, about 380 steps). Pinned Oink: 14 iterations, 35 tangles, verified; dtl_flipflop the same.
  fixd_fdpos, both order data identical: positions [6, 6, 15, 15, 14, 9, 0, 3, 6, 9, 6, 3, 0]. After the rise at position 0 the
  tail RE-RISES (3, 6, 9, 6, 3) before position 0 rises again: positions 3, 6 and 9 each rise twice, the second time after a
  reset. NEST = 4 (0 ⊃ 3 ⊃ 6 ⊃ 9). fixd_outcome: -1->ST 4, PV-SHRINK 2, PV-GROW 2, CTX 3, SAME 2. fixd_enable: 3 enabling
  births, all '>j' at depth 0 (tail-born, condition (b)).
- Greedy shrink keeps NEST 4 with 8 of the 11 edges: 1:Even-3-T -> 2:Even-1-L, 2:Even-0-T -> 1:Even-2-Z,
  1:Odd-4-T -> 2:Odd-1-Z, 2:Odd-0-L -> 1:Even-3-Z, 1:Even-2-H -> 2:Odd-2-L, 2:Even-0-Z -> 1:Odd-0-Z,
  2:Even-4-H -> 1:Odd-1-T, 2:Odd-3-H -> 1:Odd-0-T. No uniform pattern is visible yet.
- Caveat: one climbed instance, not a family. Each position re-rises at most twice here; a counter needs this recursively.

## 4. Scaling (DATA, 14:40-15:35Z by date -u): the climbs plateau
- carryclimb.py NEST climbs (stable order), each started from the nest4 edges or from scratch, ≤ 1 h each:
  2 copies a = b = 5 (n 80): NEST 4 (S 15-17); a = b = 6 (n 96): 3; a = b = 7 (n 112): 3;
  3 copies 4,4,4 (n 96): 3; 4 copies 3,3,3,3 (n 96): 3. No growth with the size or the number of copies in this time.
- Individual random cross edges do not scale; a uniform cross-edge RULE was not found (the shrunk 8-edge set of §3 has no
  visible pattern).

## 5. Reading: what a staircase product's tangles can be, and the obstruction for two copies
- DATA (lag/learn.py on nest4_n80): all 35 learned tangles are, per copy and per player, contiguous ranges of bit indices
  (35 of 35); 5 of them span both copies (an interval of copy 1 united with an interval of copy 2).
- Reading. If every learned tangle of a k-copy staircase product is a union of one bit interval per copy (and player), then the
  number of distinct tangles is at most prod_i O(b_i^2), and each search learns at least one new tangle, so
  S ≤ prod_i O(b_i^2). For k = 2 this is polynomial (O(a^2 b^2) ⊆ O(n^4)): two staircases cannot make a super-polynomial phase,
  whatever the cross edges, as long as the interval shape holds. For k copies the bound is about (n/k)^(2k), so with
  k ≈ log n copies interval-product tangles leave room for n^(Θ(log n)) distinct tangles. That is the only place where this
  substrate leaves room for a counter: carries must be CROSS-COPY tangles (one interval per copy), learned low and firing high.
- The interval shape itself is DATA (one instance), not proved.
- Why each rung re-rises only once in nest4 (READING): a re-rise at a rung needs a NEW tangle firing there (CHANGE-NEW, R14);
  at a rung of copy 2 the new tangles available are the intervals of copy 2 ending at that rung, extended by intervals of copy 1.
  In nest4 the second rise uses the cross tangle that the root rise of copy 1 created; copy 1 then has no further rise below
  the root to supply another extension. A deeper counter would need copy 1's own tail to re-rise between the re-rises of
  copy 2, which is the same problem one level down (k copies, one per counter bit).

## 6. What keeps ctx13_n40's tail alive (Lead 14:03Z question; DATA 15:44Z by date -u)
- ctxp/d0calls.py on ctx13_n40, Odd phase (S 25): every search is a long chain of depth-0 calls that return −1, and the
  SINGLE stable call is the last one (its Dom ends the search: the next call is |R| 0 or 1). For example:
  `40:-1 39:-1 38:-1 37:-1 35:-1 33:-1 30:-1 28:-1 23:-1 20:-1 14:-1 13:-1 10:-1 9:1 1:0`, next search
  `40:-1 39:-1 38:-1 37:-1 35:-1 33:-1 30:-1 27:-1 25:-1 20:-1 19:-1 18:-1 14:-1 10:1 0:0`.
- So the counter positions of ctx13 are the −1 calls ABOVE the stable call, i.e. distraction pieces removed by Dom(prevV)
  without learning. Its resets (fixd_outcome: PV-SHRINK 13, PV-GROW 9, −1→ST 2) change the SIZE of a −1 piece, which re-cuts
  every −1 piece below it. The lower part stays out of Dom because a −1 call removes only the regions of its prevV, not the
  rest of R. leanT is the opposite: its rungs turn STABLE (−1→ST every time), and a stable piece's Dom takes everything below.
- Design consequence (READING): a compounding counter should keep its rungs as −1 pieces whose prevV shrinks (a later
  emptying round, §27d), with learning only at the bottom stable call; the tangle learned at the bottom must then make a −1
  piece HIGHER up shrink (fire high), and the pieces below that one restart from a low state. In ctx13 only 4 of 26
  transitions have an enabling tangle firing at R_j (all tail-born); the rest change R_j through a different context (CTX) or
  a deeper attractor.
- NEST (§1) on the library and on this box's instances (fixd_fdpos, stable order; the Oink order was identical where run):
  ctx13_n40 Odd phase 3; tcR4_N6 3; nest4_n80 4; leanT_N8 1; onep_lagdist_D8 1; onep_chainfail_n20 1. nest4_n80 is the
  highest NEST seen.

## 7. L-ALG's NEW-KEY potentials (b12_pot.py, l-alg e2132aec, run UNMODIFIED; DATA 16:12-16:25Z by date -u)
- On 11 box-11/12 instances (nest4_n80, products a6/a8, leanT_N8, tcL_N6, tcR4_N5/N6, deep1_n13, tcS8_N6, ctx13_n40,
  fam_D8_n78; 148 transitions, 23 with an identical depth-0 chain), both orders identical: K-v-rs, K-v-rV, K-v-rjV, K-v-all:
  0 violations. K-jRrV 1 and K-v-rj 3 (tcR4_N5), K-v-r 13, K-Rset 8.
- Two-player kill of (VR-NEW_s) (key (v, rank, |R_j|) = K-v-rs): vrs_viol_n100.pg (sha1 b4bbe7f0fdc0;
  experiments/red/tcpert/instances/prod/), found by keyclimb.py (seed 2, from tcR4_N5, 32 steps). Pinned Oink 7 iterations, 13
  tangles, verified; dtl_flipflop the same. b12_pot: stable 6 transitions, K-v-rs 2 violations; Oink order 5 transitions, K-v-rs
  1 violation. K-v-rV, K-v-rjV, K-v-all: 0 (both orders). Not in 𝒞^1P (two-player), so it does not touch the class claim.
- Two-player kills of (VR-NEW_V) (key K-v-rV = (v, rank, |V_j|)), keyclimb.py, both orders (DATA 16:59Z by date -u):
  vrV_viol_n80.pg (sha1 f77f0d34d13f; from nest4_n80, seed 1): stable 5 transitions, K-v-rs 2, K-v-rV 1, K-v-rjV 1;
  Oink order 4 transitions, K-v-rs 1, K-v-rV 1, K-v-rjV 1. vrV_viol_n40.pg (sha1 8cf415ec9267; from ctx13_n40, seed 3):
  27 transitions in both orders, K-v-rV 1 (K-v-rs 0, K-v-rjV 0). K-v-all: 0 on both, both orders. So in two-player games only
  (VR-NEW_all) survives among the vertex keys; (VR-NEW_s), (VR-NEW_V) and (v, rank, j, |V_j|) are false there.

## 8. Box 13: (VR-NEW_all) and (FD-WITNESS_all) (DATA from 17:30Z by date -u; l-alg 7fc4681b, tools unmodified)
- b12_fdwit.py on vrV_viol_n80, vrV_viol_n40, vrs_viol_n100, nest4_n80, ctx13_n40, tcR4_N6 (two-player): stable 74 / Oink order
  72 chain-changing transitions. Transitions with no new-key vertex in the piece at j*: K-v-rV 26 / 26, K-v-rs 17 / 15,
  K-v-all 2 / 2; nor at j* − 1: K-v-rV 21 / 21, K-v-rs 12 / 10, K-v-all 0 / 0. So (FD-WITNESS_all) holds on all of them
  (2 transitions need the j* − 1 clause), while the rV and rs forms fail often in two-player games.
- marginclimb.py (b12_pot.vr_score, MARGIN=1, key K-v-all; every accepted game verified by pinned Oink): the margin (fewest
  vertices supplying a new key at one chain-changing transition) reaches 1 quickly from vrV_viol_n80 (stable) and from L-ALG's
  onep_fdkey_n20 (Oink order; mutations leave the class), and stays at 1 (by 18:09Z: 9 and 17 chain-changing transitions, about
  40,000 steps on the n = 20 seed). MC_TIGHT=1 (also maximising the number of margin-1 transitions) stays at one such transition.
- Margin-1 anatomy (experiments/red/ctxp/newkeys.py over b12_pot.run/chain/keys/sig, unmodified): on the three climb bests
  (instances ctxp/instances/margin1_n20.pg from onep_fdkey_n20, Oink order; margin1_mc1.pg from vrV_viol_n80 and margin1_mc5.pg
  from lagfam fam_D4_n50, stable order) the single new-key vertex is, every time, a vertex changing its RANK CLASS for the first
  time in the phase: stable -> −1 (margin1_n20: vertex 18, earlier keys all rank n+2, new key rank 4 at position 5 or 7;
  margin1_mc5: vertex 34, rank n+2 -> 5) or outside -> stable (margin1_mc1: vertex 73, rank 0 -> n+2). lagfam itself has margin 2
  at every D (fam_D4/D8, depth2_n39; both orders).
- READING (the obstruction as it shows in the data): every chain change found so far moves some vertex into a rank class
  (stable / −1 at an emptying round e / 0) and position it never held in the phase. A kill of (VR-NEW_all) needs a transition
  where EVERY vertex of the changed pieces returns to an exact earlier (rank, j, |R_j|, |V_j|); in particular a vertex that left
  a −1 piece for a stable one must come back to the same −1 piece with the same emptying round and the same |R_j|, |V_j|. The
  climbs never produced such a re-crossing: whenever a vertex re-enters a −1 class, the piece's |R_j| or |V_j| or round differs.
