# R25: (K-first) and (K4-B) are FALSE on A_DTL, both order data; the run stays complete (L-RED box 6, 05:00Z by date -u; produced on Opus 5.5)
Target: L-ALG docs/alg/GAP-C.md §13 (l-alg 31fdd98): (K-first) "in every search of p with W_p(G') ≠ ∅ and no dominion, the
FIRST stable piece is good"; (K4-B) "at that first stable piece, V* and the union of the final-round regions lie inside
W_p(G')". Both DATA there (483/483 Oink order, 464/464 stable). GAP-K' = (K4-B) + (α) + (β-1). Status of this note: DATA,
unrefereed.

## 1. FINDING (experiments/red/carry/instances/kfirst_viol_n13.pg)
n = 13, sha1 a9075c8b2182277b7afd71e256ae66b55ff10f85. Disjoint union of the hand gadget chain2 (vertices 0-5,
experiments/red/k4b/gen_chain.py 2) and L-ALG's experiments/alg/instances/walk_s2_k1_n7_m11_8.pg (vertices 6-12).
- Pinned Oink 8fbf0a7, `oink --dtl --no-single --no-wcwc --no-loops -v`: 2 dominions, 6 tangles, 5 iterations (4 even,
  1 odd), solution verified. Even wins 6-12, Odd wins 0-5. Iteration 0-even has no dominion; its first "(stable)" line
  learns "new tangle 4 (0)" (the Odd-won region {e, u}); its second stable piece learns inside W_0.
- L-ALG's tools, unmodified, at l-alg 31fdd98, identical under DTL_ORDER=oink and DTL_ORDER=stable:
  dtl_whichpiece.py: {'searches': 2, "mixed (W_p != G')": 2, 'FIRST': 1, 'FIRST in mixed': 1, 'FIRST-W': 2, 'LAST': 2,
  'ANY': 2}, "FIRST fails ... pieces 2 good [False, True]";
  dtl_k4b.py: 1 ('mixed', 'V* meets W_{1-p}', 'regions meet W_{1-p}'), 1 ('mixed', 'V* inside W_p', 'regions inside W_p');
  dtl_kin.py: 'K-in VIOLATION': 0; dtl_loww.py: 'LOW-W VIOLATION': 0.
- Pinned in experiments/red/check.sh (dtl_flipflop: n=13 tangles=6 dominions=2 iterations=5, = Oink).
- Same result with the walk game placed first (vertices shifted), both orders.

## 2. The gadget (chain_k; k = 2 here)
u (3, Odd) -> e, b'; e (4, Even) -> u; a_1 (6, Even) -> e, c; a_i (4+2i, Even) -> a_{i-1}, c; b' (2k+5, Even) -> a_k;
c (2k+7, Odd) -> c. Everything is Odd-won (c is an Odd self-loop; the cycle u b' a_k .. a_1 e has top b', odd).
Even's first search, depth 0:
1. Piece 1 (-1). Round 1: e's region is {e} (u has its edge to b' in CurR); e is a candidate and is not rescued below
   pr(e) = 4, because u needs b' and pr(b') = 9 > 4. a_i has an edge into Z (a_{i-1} is a top) so it stays. Round i+1
   prunes a_i. With the walk part pruned by then too, V empties with prevV = {a_k}: Dom(prevV) puts a_k into X.
2. Piece 2 (-1). The threshold step takes the lowest level with a vertex that attracts into X: b' (its only edge goes to
   a_k). b' is a threshold vertex, so it goes to X; the recursion is on the empty set.
3. Piece 3 (stable). u's edge to b' now lies outside R and is ignored by attractVertices (escapes judged in CurR), so u
   joins e's region, which is closed (e -> u). The first stable piece holds the region {e, u} ⊆ W_1, and e is the lowest
   top. Its sptl extracts the tangle {e, u} with escape b' (outside W_0).
Why each choice (DATA from the derivation, checked on the built games): pr(b') > pr(a_k) keeps b' out of a_k's region;
pr(b') > pr(e) prevents the rescue of e through u in the round that prunes e (with b' in Z, u is attracted at t = pr(u)
and e survives); the chain lets the gadget prune LAST, so a_k is in prevV when the other component has emptied. Alone
(W_0 = ∅) the gadget does the same, but no statement applies; the union supplies W_0 ≠ ∅ with no dominion.

## 3. What fails in the proof route, and what survives
- Theorem A's K4 step needs X p-won. Here X holds W_{1-p} vertices before the first stable piece: a_k from a Dom(prevV)
  piece, and b' from a THRESHOLD piece built on it. An opponent vertex u of the next region has its only escape into
  X ∩ W_{1-p}; the region attractor ignores that edge. So (K4-B) cannot be proved as stated, and the first stable piece
  can be barren for W_p.
- Survives on this instance: (K-in), (LOW-W), FIRST-W (the first stable piece having a top in W_p is good, 2/2).
- My own failed routes (derivation notes): with X built only from Dom(prevV) pieces of the same best_vertices loop, the
  rescue step blocked every attempt in which u's escape target lay in the union of regions of the round that pruned e;
  the threshold piece supplies a target (b') that lies in no region of any pruning round.
- Corpus sweep: gadget ∪ each of 256 repo games (both arrangements, both orders): gad5 (no chain) 0 violations in 604
  checked searches (the other component makes piece 1 stable first); chain2 ∪ walk_s2_k1_n7_m11_8 is the hit
  (experiments/red/k4b/union_corpus.py).

## 4. Next
Make the W_p part's own learning wait for more gadget pieces, aiming at a (K-in) violation (a search with W_p ≠ ∅ that
learns only outside W_p), then at an incomplete run.
