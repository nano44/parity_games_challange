# R31: (FALL) — 3 descents of Π_R at one context in one phase on A_DTL, both order data (L-RED box 7, 13:15Z by date -u; produced on Opus 5.5)
Status: DATA, unrefereed. Target (A) of the Lead's 13:04Z message (GAP-A-M §22l/§22m): GAP-A ⇐ (CTX⁺) ∧ (FALL); the known max
was 2 descents per (context, phase), reached only on f1_twodef_n48 / f1_twofall_n48 (R19, R20).

## Instance
experiments/red/carry/instances/fall3_n76.pg (n = 76, 425 edges, sha1 a85133ec886b05beea2582e4a50885eb3795a243).
experiments/red/root/ucompose.py seed 51, union 66 (Oink order): the three 1-descent gadgets lex_viol_oink_n20 (L-ALG
experiments/alg/instances), lex_viol_inj_n28 and lex_viol_tie_n28 (L-RED carry/instances), stacked in random order with
priorities shifted by even amounts, plus random cross edges. The parts have 49 + 187 + 187 = 423 edges, so the union has
2 cross edges.

## Evidence (re-run)
- L-ALG experiments/alg/dtl_rootmono.py UNMODIFIED (l-alg c8df405), DTL_ORDER=oink and =stable, same verdict:
  "descents of Π_R per context (file, max per context, total, transitions, |G'|): (fall3_n76, 3, 3, 5, 76)", one phase,
  player 1. Three "FALL with only old witnesses" lines, visits 1→2, 2→3, 3→4, witnesses [6, 12, 14] each time (k0 20/25/31
  Oink, 21/26/32 stable). RMONO FAILS: vertex 28 round 7→6, vertex 2 8→7, vertex 50 8→7. No CLEAN failure, no
  "Ψ NOT monotone", no "DOES NOT RISE", no INCOMPLETE line.
- Each gadget alone: max descents per context 1, both orders.
- Pinned Oink 8fbf0a7 `oink --dtl --no-single --no-wcwc --no-loops -v`: 3 dominions, 56 tangles, 10 iterations, solution
  verified (35 strategies). Pinned in experiments/red/check.sh (dtl_flipflop n=76 tangles=56 dominions=3 iterations=10).

## Reading (L-RED)
R19 found that plain unions stay at ≤ 2 descents per context, because each part's dominion ends the phase and the parts'
falls merge into one search. Two cross edges break that here: each gadget contributes its own descent at the root context,
in a different search of the same phase. The growth test (unions of k parts, k = 4, 5, 6; descents vs k and n) is running;
a table follows in this file.
