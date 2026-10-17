# R27: (P-K) and (K-STEP-first) are FALSE on A_DTL, both order data; the run stays complete (L-RED box 6, 05:50Z by date -u; produced on Opus 5.5)
Targets (Lead 05:48Z; L-ALG succ. 6, GAP-C.md §18 at l-alg 9000121): for a search of p with D = W_p(G') ≠ ∅, K(R) holds
iff (D ∩ R) minus the p-attractor (inside D ∩ R) of the vertices with an edge into X = G' \ R still has a nonempty p-winning
region. (P-K): a depth-0 P piece (Dom(prevV), Q empty, dtl.cpp 961-991) never breaks K. (K-STEP-first): the first depth-0
piece after which K fails learns a tangle inside D or finds a dominion. Lemma K0 (proved there) plus (K-STEP-first) would
give completeness. Status of this note: DATA, unrefereed.

## 1. FINDING (experiments/red/carry/instances/pk_viol_n20.pg)
n = 20, sha1 942bd778a1d6689af58632229800c5426e14de52. Found by dtl_search --fitness pk (carry/pk.py), seed 9502, stable
order, from gapbW_dup_n20, step 1,182.
- Pinned Oink 8fbf0a7 `oink --dtl --no-single --no-wcwc --no-loops -v`: 1 dominion, 4 tangles, 2 iterations (both even),
  solution verified (11 strategies). Even wins all 20 vertices.
- L-ALG's dtl_step5stats.py, unmodified, l-alg 9000121, identical under DTL_ORDER=stable and =oink:
  "K FIRST break by P VIOLATION (barren, nothing learned inside D before)": 1; "K broken by P (barren)": 1;
  "ATTR VIOLATION": 1; "HYB broken by P VIOLATION (barren)": 1.
- L-ALG's dtl_pnl.py, both orders: "PNL* depth 0 holds": 1; "YZ depth 0 Y_0 = Z_f": 1; "PNL* depth 0 greatest p-closed
  subset of Y_0 nonempty, no p-priority vertex": 1. So (PNL*) holds here.
- Pinned in experiments/red/check.sh (dtl_flipflop: n=20 tangles=4 dominions=1 iterations=2, = Oink).

## 2. Anatomy (experiments/red/k4b/pieces.py, original ids, stable order)
Search 0 (Even, D = G', no dominion):
1. DOM-1, prevV = {8, 11, 12, 13}: Dom(prevV) removes 14 of the 20 D-vertices {0,1,2,4,8,9,10,11,12,13,14,16,18,19};
   nothing learned. K fails after it.
2. THR-1 at t = 15: removes 7.
3. STABLE, V* = {3, 5, 6, 17}: learns {3, 5, 6} inside D.
Search 1 finds the dominion. So (K-in) and (K-low) hold: the search learns inside D only after K is false. The completeness
route through K needs another statement; what this instance still satisfies is (K-low)/(K-in) and (PNL*).

## 3. Next
pk climbs continue (target (i): a P piece after which every remaining D-vertex is p-attracted to X; and a (K-in)
violation from this instance).
