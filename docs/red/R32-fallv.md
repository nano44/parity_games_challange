# R32: (FALL-V) is FALSE on A_DTL, both order data; the run stays complete (L-RED box 7, 14:36Z by date -u; produced on Opus 5.5)
Status: DATA, unrefereed. Target: L-ALG's (FALL-V), relayed by the Lead at 14:22Z: "along a phase, each vertex's RV at a
fixed context R falls AT MOST ONCE" (would give F_R <= n and GAP-A <= (CTX+) alone).

## Instance
experiments/red/carry/instances/fallv_viol_n28.pg (n = 28, sha1 21b235f4e680e1bf599c6623774fad0a05d41350). Found by
dtl_search.py --fitness fallv (root/fallv.py), seed 17001, DTL_ORDER=oink, from carry/instances/lex_viol_inj_n28.pg, about
2,900 steps.

## Evidence (re-run)
- root/fallv.py: a read-only wrapper; it runs L-ALG's dtl_rootmono.RM UNMODIFIED (l-alg 94067096, imported as a module)
  and compares consecutive visits of every context key as dtl_rootmono's "descents of Π_R" block does. DTL_ORDER=oink and
  =stable, same result: hit 8 (context, vertex) pairs, maxfalls 2, run complete.
- Phase 1, player 1, 5 searches, |G'| = 28. Root context key (depth 0, R = all 28 vertices), one visit per search.
  RV(vertex 14, priority 27) over searches 0..4: 4, 6, 5, 4, 4: a rise (4 -> 6), then falls 6 -> 5 (search 1 -> 2) and
  5 -> 4 (search 2 -> 3). The same vertex falls twice at 7 more contexts (|R| 16..22).
- dtl_rootmono.py UNMODIFIED, both orders: "RMONO FAILS ... p=1 root threshold loop, round 3 vertex 14 pr 27 round 5 -> 4"
  (the second fall); "descents of Π_R per context: (fallv_viol_n28, 2, 17, 4, 28)"; no CLEAN failure, no Ψ-not-monotone,
  no DOES NOT RISE, no INCOMPLETE.
- Pinned Oink 8fbf0a7 --dtl --no-single --no-wcwc --no-loops -v: 1 dominion, 17 tangles, 7 iterations, solution verified
  (14 strategies). Pinned in experiments/red/check.sh.

## Shape and consequence (L-RED reading)
Rise, fall, fall (not fall / restore / fall): a new tangle raises the vertex's RV, then two later steals lower it in two
steps. "Each vertex falls at most once per context" is dead; F_R <= n does not follow from it. Per-vertex falls are still
bounded by its rises plus the RV range, which needs its own potential.
