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

## 2. Growth: 4 descents at one context (fall4_n116), 14:0xZ by date -u
- Mechanism found in fall3_n76: its 2 cross edges form a CHAIN down the stack, each from an Even-owned vertex of an upper
  part to an Even-owned vertex of the part just below (35 -> 9, 67 -> 45; the phase is Odd's). Solo fall visits of the
  parts: lex_viol_oink_n20 1->2, lex_viol_inj_n28 and lex_viol_tie_n28 both 2->3; in fall3_n76 the falls are at 1->2,
  2->3, 3->4, so the chain DELAYS one part by one search. ucompose.py CHAIN=1 builds this pattern: 4 of the first 9
  3-part chain unions reach 3 descents (random cross edges: 3 of 224).
- Repeated copies of one gadget do not add (4- and 5-part chains with repeats stay at 3; copies fall in the same search).
  A corpus scan (dtl_rootmono on every corpus file, Oink order) gives gadgets with different solo fall visits:
  h4_def2ctx_n20 0->1; lex_viol_oink_n20, lemmaS_viol_n20, dtl_mviol_n20 1->2; lex_viol_inj_n28, lex_viol_tie_n28,
  cm_viol_oink_n28 (also 2->5), cm_mdrop_*_n28 2->3.
- experiments/red/carry/instances/fall4_n116.pg (n = 116, sha1 9b174a5e337c74b0d83909b678c7bc4bdc1941f1): ucompose.py
  CHAIN=1 seed 81, union 18, parts h4_def2ctx_n20, lex_viol_oink_n20, lemmaS_viol_n20, lex_viol_inj_n28, cm_viol_oink_n28.
  - dtl_rootmono.py UNMODIFIED (l-alg c8df405), DTL_ORDER=oink and =stable, same verdict: "descents of Π_R per context
    (file, max per context, total, transitions, |G'|): (fall4_n116, 4, 10, 4, 113)", one phase. The phase has 4
    transitions, and each is a descent at that context. FALL lines with only old witnesses [12, 18, 23, 25, 27] at visits
    0->1, 1->2, 2->3 (and 0->2). No CLEAN failure, no Ψ-not-monotone, no DOES NOT RISE, no INCOMPLETE.
  - Pinned Oink 8fbf0a7 --dtl --no-single --no-wcwc --no-loops -v: 6 dominions, 82 tangles, 13 iterations, solution
    verified (50 strategies). Pinned in check.sh.

| parts | n | max descents of Π_R at one context, Oink / stable | instance |
| --- | --- | --- | --- |
| 1 | 17-28 | 1 / 1 | the gadgets |
| 2 | 48 | 2 / 2 | f1_twofall_n48, f1_twodef_n48 (R19, R20) |
| 3 | 76 | 3 / 3 | fall3_n76 |
| 5 | 116 | 4 / 4 | fall4_n116 |
Reading (L-RED): descents per context grow with the number of chained parts with distinct fall timing; the limit is the
supply of such timings, not the construction. A family needs gadgets with solo falls at visits 0, 1, 2, ..., k-1 or a
delay gadget; next box.
