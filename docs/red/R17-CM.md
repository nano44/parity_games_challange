# R17: filtered attack on L-ALG's (CM) (GAP-A-M 13h) (L-RED successor 3, 16:05Z by date -u; produced on Opus 5.5)
Target (L-ALG, GAP-A-M 13h, DATA only, 0/123 there): "across a parent DEF step, an ideal-stable child's actual round
count M does not decrease". A_DTL = oink --dtl --no-single --no-wcwc --no-loops @ 8fbf0a7; every count labelled with its
order datum (L26).

## 1. Tool (premise copied from L-ALG's own checker)
experiments/red/carry/cmf.py imports L-ALG's dtl_regvec.py read-only (LALG_DIR = a detached checkout of claude/l-alg
d2ae597) and repeats the premise of experiments/alg/dtl_childM.py line for line: consecutive searches a, b of one phase
(same player, no dominion between); depth-0 piece j >= 1 whose context changes; piece j-1 at the SAME context with the
SAME ideal (C6) result and a DIFFERENT actual result (a DEF step); piece j's ideal result STABLE in a and in b; M = the
number of nonempty actual pruning rounds at piece j. It adds one tag: "clean" = the parent's actual result is -1 in both
searches (the parent's staircase continues; it does not finish). Reproduction before the climb: L-ALG's dtl_childM.py on
its instances/h4_*.pg plus my h4_*/lemmaS_* gives M_drop 0 (Oink order 51 cases, stable order 42 cases).
Fitness dtl_search.py --fitness cmf: 2000 x clean drops + 300 x largest clean drop + 1000 x drops + 100 x death drops
+ 10 x equal-M cases + cases. Climbs from L-ALG's h4_def9_oink_n28 / h4_def10_oink_n28 (the only games with child death
drops), both orders.

## 2. FINDING: (CM) is FALSE on A_DTL, in BOTH orders (instance experiments/red/carry/instances/cm_mdrop_both_n28.pg)
n = 28, sha1 4c52c32f. Pinned Oink: 1 dominion, 24 tangles, 9 iterations, solution verified (10 strategies); dtl_pyref
9 searches. Checked with L-ALG's UNMODIFIED dtl_childM.py: DTL_ORDER=oink M_drop 1, DTL_ORDER=stable M_drop 1.
Player 1 (Odd) phase, search s5 -> s6 (pyref numbering), original ids:
| piece | context | actual s5 -> s6 | ideal s5 = s6 |
|---|---|---|---|
| 0 (parent) | 28 -> 28 (same) | -1 {6,23} -> -1 {6,23,27} (DEF) | stable, 23 vertices, unchanged |
| 1 (child) | 26 -> 25 (loses 27) | -1 {2} -> -1 {1,2,7,10,19,25} | stable in both |
Child rounds |V|: s5 21,19,17,15,13,8,3,1 (M = 8, last {2}); s6 20,18,16,15,14,12,6 (M = 7). Death drops on common
vertices (round a -> b): 2: 8 -> 7, 13: 7 -> 6, 14: 7 -> 5, 26: 6 -> 4. The parent stays -1 (clean). The parent's return
set GREW by 27, so the child's context lost 27, and the child's actual pruning ended a round earlier while its ideal
result stayed stable. Earlier and later steps of the same staircase: s4 -> s5 M 5 -> 8, s6 -> s7 M 7 -> 9.

## 3. A larger drop, Oink order only (experiments/red/carry/instances/cm_mdrop_oink_n28.pg)
n = 28, sha1 f298f8f5. Pinned Oink: 1 dominion, 12 tangles, 7 iterations, verified. dtl_childM.py: Oink order M_drop 1,
stable order M_drop 0 (the case does not arise there). s6 -> s7: the parent (piece 0, context 28, ideal stable
unchanged) goes actual -1 {5} -> STABLE {1,5,7,12,18,20}; the child's context shrinks 27 -> 8 and its M goes 13 -> 1 (its
ideal is stable in both). This is the "parent finishes" form (not clean): it fits L-ALG's premise as written, but a
restated (CM) restricted to parent steps -1 -> -1 is not killed by it. Section 2 kills that restatement too.

## 4. Reading (L-RED)
- (CM) as stated: DEAD (both orders). Restricted to clean parent steps: DEAD (section 2, both orders).
- Mechanism: a parent DEF step that ENLARGES the parent's -1 return set shrinks the child's context; vertices that
  supported the child's slow deaths leave, so the child's deaths come earlier and M drops, with the child's ideal stable.
  The drop of 1 is the smallest; climbs for larger clean drops continue (section 5 when they end).
- What this does NOT show: no growth of any count with n, no re-climb chain. It removes (CM) as a brake on nesting.

## 5. Climbs (in progress at the time of writing)
Seeds 301-304, dtl_search --fitness cmf; scores and any larger clean drop go here at box end.
