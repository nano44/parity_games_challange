# R29: (K-in), (K-low), (TW) and (S-LOW, tight form) are FALSE on A_DTL, both order data; the run stays complete (L-RED box 6, 11:02Z by date -u; produced on Opus 5.5)
Status: DATA, unrefereed. Instance experiments/red/carry/instances/kin_viol_n29.pg (n = 29, sha1 50987098027ec0a014a8974af89f40bb856b35c1),
found by experiments/red/k4b/umix.py seed 18, union 9922 (interacting union of 2-3 corpus games + random cross edges).

## Evidence
- Pinned Oink 8fbf0a7 `oink --dtl --no-single --no-wcwc --no-loops -v`: 2 dominions, 15 tangles, 8 iterations (4 even, 4 odd),
  solution verified (13 strategies). Pinned in experiments/red/check.sh (dtl_flipflop n=29 tangles=15 dominions=2 iterations=8).
- L-ALG's dtl_kin.py, unmodified (l-alg ae7e1d3), DTL_ORDER=oink and =stable, same counts: 'K-in VIOLATION': 1 (p 0, |G'| 29,
  |W_p| 9); new tangles in such searches {'inside': 11, 'meets': 1, 'avoids': 3}.
- L-ALG's dtl_loww.py, both orders: 'LOW-W VIOLATION': 1.
- L-ALG's dtl_step5stats.py, both orders: "KTHR broken by S VIOLATION (barren, nothing learned inside D before)": 1,
  "KT broken by S VIOLATION (barren, ...)": 1, "S-STEP ... VIOLATION barren": 1, "S-LOC ... VIOLATION": 1, "LASTD piece S
  VIOLATION": 1; its loose S-LOW line says "learns": 2.
- carry/slow.py, both orders: loose 0, TIGHT 1 (qual 2): the first-pass lowest top of the KT-breaking S piece learns only
  outside D (L-ALG d8a377c: "no case fails tight while passing loose" on its data; this is one).

## Anatomy (experiments/red/k4b/pieces.py, original ids, Oink order), search 0 (Even; W_0(G') = {0..8}; no dominion)
1. DOM-1, prevV {18}: removes {11, 13, 17, 18, 21, 23} (no W_0 vertex).
2. THR t = 21: removes {19, 25}.
3. STABLE, V* = {4, 5, 8, 10, 12, 14, 15, 22, 24, 26} (MIX: W_0 tops 4, 5, 8): removes all of W_0 with opponent vertices and
   learns OUT {10, 12}, OUT {14} and the STRADDLING tangle {0, 4, 6, 10, 12, 16, 20, 26, 27} (W_0 vertices 0, 4, 6). Nothing
   inside W_0.
4. THR t = 37: removes {9, 28}.
Search 1 learns IN {0, 1, 2, 4} at depth 1; search 2 finds the Even dominion. The run recovers.

## What dies
(K-in) "a W_p search with no dominion learns a tangle inside W_p"; (K-low)/(LOW-W); (TW) "learned tangles never straddle
W_p"; (S-LOW) in the tight form (inside D); (KT-STEP-first) at an S piece. What still holds here: L-ALG's loose S-LOW test
(the lowest top learns SOMETHING), and completeness. A weaker completeness statement is needed, e.g. "a W_p search learns a
tangle MEETING W_p (or a dominion), or a later search learns inside W_p".
