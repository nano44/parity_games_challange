# R19: two fall steps at one context on A_DTL (attack on (F1)) (L-RED successor 3, 18:49Z by date -u; produced on Opus 5.5)
(F1) (my DATA line of 18:27Z, relayed by the Lead 18:46Z as an L-ALG target): at a fixed (phase, context), at most ONE
step between consecutive best_vertices calls has a FALL (some p-vertex's actual death round decreases). Tool:
experiments/red/carry/lex.py (L-ALG dtl_regvec read-only, l-alg c7fc7cb; deaths as in R18).

## 1. FINDING: (F1) is FALSE on A_DTL, both orders (experiments/red/carry/instances/f1_twofall_n48.pg)
n = 48, sha1 6af4ef5c, injective priorities (carry/injective.py, Oink's tie order). It is the DISJOINT UNION of L-ALG's
lex_viol_oink_n20 (ids 0-19) and my lex_viol_inj_n28 (ids 20-47, priorities shifted above). Pinned Oink: 2 dominions,
32 tangles, 8 iterations, solution verified (22 strategies). lex.py, DTL_ORDER=oink and stable alike: player 1, context
R = G (|R| 48), fall steps:
- s4 -> s5 (ideal MOVED, an LRN step): 13 vertices fall, all in the n20 component (e.g. 1: 15->14, 16: 14->13).
- s5 -> s6 (ideal SAME, a DEF step): 9 vertices fall, all in the n28 component (22: 8->7, the top changed vertex, as in
  R18; 46: 6->4; 34: 7->5).
So two steps with falls at one context. Each component falls once; they fall at different searches because the n20
gadget falls one search earlier in the union.

## 2. Limits of the finding
- Only ONE of the two fall steps is a DEF step (ideal unchanged). (F1) restricted to DEF steps survives this instance.
  Climb running: fitness fallsdef (2 DEF fall steps at one context), from this instance, Oink order.
- Plain unions do not scale: unions of 3, 4 and 6 gadgets with distinct solo fall searches (4, 5, 6, 7, 8, 9) give at most
  2 fall steps at one context in either order. Each component's dominion ends the phase, and the components' falls merge
  into the same search (scratchpad k3a/k3b/k4/k6, not committed).
- No nesting: (NR) level 0 in this instance; the second fall is in a disjoint component.
