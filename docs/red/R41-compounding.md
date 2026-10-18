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

## 4. Scaling (running)
