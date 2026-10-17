# R26: (K-in)/(K-low) attack on A_DTL, first pass: no violation (L-RED box 6, 05:50Z by date -u; produced on Opus 5.5)
Target (Lead 04:55Z, L-ALG GAP-C.md §14-§17 at l-alg 39f6111): (K-in) a search of p with W_p(G') ≠ ∅ finds a dominion or
learns a tangle inside W_p; (K-low) some stable piece's lowest region is productive inside W_p. Fitness order: incomplete/
wrong > K-in > K-low > TW straddle > dupW > orphW > barren > dup > orphan. Status: DATA, unrefereed. No violation found.

## 1. Tools (experiments/red)
- k4b/pieces.py: piece tracer on L-ALG's dtl_kin.KI (unmodified, LALG5_DIR): per search the depth-0/deeper pieces
  STABLE / DOM-1 (−1, Q empty, Dom(prevV)) / THR-1 (−1 threshold piece; logged set = threshold vertices + opponent
  attractor, the recursed rest is traced at depth + 1), removed sets with their W_p part, new tangles IN/MEET/OUT, and
  duplicate-check hits (wrapper on pyref's tkeys, the transcription of dtl.cpp 385-424).
- carry/klow.py (dtl_search --fitness klow): per W_p search without dominion, prod = stable pieces learning inside W_p
  (prod 0 = a (K-in) violation), dupmin = duplicate hits inside W_p at the least-prod search, eaten = share of p-priority
  W_p vertices removed by −1 pieces before the first productive piece.
- k4b/graft.py, graft3.py, rgraft.py, nbhd.py: exhaustive small grafts, random grafts, one-step neighbourhood ascent.

## 2. Runs (both order data unless noted; all scored with klow.py)
| run | games | qualifying W_p searches | result |
| --- | --- | --- | --- |
| graft.py on c1_k1_min_n7_m10 (tangle {τ,y}, y -> 1-2 base vertices, optional base -> τ) | 3,500 | not counted | min prod 1 |
| graft.py GR_S=1 GR_NOINTO=1 on gapbW_dup_n20 | 2,200 | not counted | min prod 1 |
| graft3.py on c1_k1_min (x -> y -> x, z; z -> base; optional y -> base) | 14,000 | not counted | min prod 1, best eaten 714 per mille |
| rgraft.py, 1-6 random vertices on 5 bases (c1_k1_min, gapbW_dup_n20, kfirst_viol_union, firstw_viol_cross, kfirst_viol_n13) | 20,000 | 29,064 | min prod histogram 1: 27,652; 2: 1,282; 3: 114; 4: 12; 5: 4 |
| nbhd.py steepest ascent from gapbW_dup_n20, 20 steps x ~1,250 neighbours | ~25,000 | not counted | plateau: prod 1, 1 duplicate inside W_p, eaten 666 |
| dtl_search --fitness klow climbs 9301-9306, 9311-9314, 9321-9323 | about 300,000 steps in total | not counted | plateau prod 1 (best 81888010: 1 duplicate in W_p, eaten 888) |

## 3. What the hand analysis says (reading, not proved)
- The near miss is real: gapbW_dup_n20 search 1 (Even) re-finds the stored tangle {3,17} as a duplicate at its last piece,
  and its only productive piece is {5,13}. That search would be a (K-in) violation if search 0 had learned only
  "replayable" tangles. Search 0 also learned {12} and {13}, and those change search 1's earlier pieces.
- Replay route (what a barren search needs): every tangle T that search s learns has its escapes removed before T's
  piece, and in search s+1 no attractor that pops an escape of T may run at a threshold >= pr(T). Two things block it.
  (i) THE RESCUE: while T's top τ must be pruned, the good-path test (threshold t < pr(τ)) attracts T's opponent vertex y
  as soon as y's escape lies in the union of regions; so the escape must lie in no pruning-round region and must not be
  rescuable below pr(τ). (ii) The escape vertices that satisfy (i) in c1_k1_min (vertex 4, removed by a threshold piece)
  lie in the region of a higher top (6) in earlier rounds, so in search s+1 the stored T is attracted there by the
  tangle attractor, and the replay breaks.
- The last p-won remnant: once the other p-won vertices are in X, the region attractor ignores the remnant's escapes
  into X, so its region closes and it is learned (c1_k1_min's vertex 0; every graft3 variant). A violation needs that
  remnant to be a duplicate (route above) or open through an unregioned p-won vertex that nothing removes first.

## 4. Next
Climbs continue on klow; the SPP spare-cycle climbs (queue item 3) run on n = 40 from spp22_oink_n40.
