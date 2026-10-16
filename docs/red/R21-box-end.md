# R21: end of the successor-3 box: replay depth, searches per phase, open targets (L-RED, 23:04Z by date -u; produced on Opus 5.5)
Box: Lead "go" 16:03Z (Lead clock) to ~00:05Z. Kills this box: R17 (CM), R18 (LEX)+(NR), R19 (F1), R20 DEF-(F1). This file
records the measurements that produced no kill.

## 1. Searches per phase (Lead 20:45Z target: a phase with more than n searches)
Tool experiments/red/carry/replay.py (spp = longest run of consecutive searches with the same player and no dominion
between; A_DTL, Oink order with DTL_ORDER=oink, else stable). It reproduces L-ALG's spp_n20/30/40/60 = 16/18/11/14 in BOTH
orders. Climbs (dtl_search --fitness phase, ~2.5 h, 4 cores):
| start | order | n | best spp | instance |
|---|---|---|---|---|
| L-ALG spp_n30 | oink | 30 | 19 (stable order: 16) | carry/instances/spp19_oink_n30.pg (Oink 21 it., verified; sha1 5c050c1d) |
| L-ALG spp_n30 | stable | 30 | 19 (Oink order: 19) | carry/instances/spp19_stable_n30.pg (Oink 23 it., verified; sha1 f5d23845) |
| L-ALG spp_n20 | oink / stable | 20 | 16 (no gain) | - |
| L-ALG spp_n40 | oink | 40 | 11 (no gain) | - |
| random | oink | 12 / 16 | 7 / 8 | - |
| replay4 padded | oink | 48 / 64 | 13 / 13 | - |
No phase with more than n searches anywhere; spp/n at most 0.8 (L-ALG n = 20) and 0.63 here (n = 30).

## 2. Replay depth (Lead 18:30Z target)
Depth 4 at n = 32 (R20, replay4_n32). Climbs from the n = 48 / 64 depth-4 padded copies stayed at 4; climbs from L-ALG's
c6_replay3_n48 and a padded n = 64 copy stayed at 3. R20 section 3: the depth changes with inert padding at equal
searches, so it is a noisy signal.

## 3. Other measurements this box (no kill)
- (U-MONO_DTL) (L-ALG): 0 U-shrinks, 0 S-shrinks over 575 (Oink) / 596 (stable) carry rounds on my corpus; 100,000-step
  climb seeded from L-ALG's dtl_lexcounter gadget (n = 18): 0 shrinks. In no DTL run does a vertex of U move to a
  LOWER-top region, although tangle splits by steals happen at every carry of h4_compound2x2_n44 (carry/umono.py).
- (NR) depth >= 2: never seen. All falls are one event per context, or one per component of a disjoint union; "a vertex
  falls twice at one context" (fitness refall): never seen in ~40 min of climbs from lex_viol_inj_n28 / f1_twodef_n48.
- Nested DEF blocks (queue item 2): T3 = 4 at n = 44 (3-level nesting, Oink order only), 8 DEF per phase: no growth.
- r0 dips at one ideal-stable context, DEF-filtered (queue item 3): 2 (n = 28); not pursued after the Lead's re-targets.
- Tool caveat (R18 section 4): dtl_regvec / dtl_crm / my r0d.py pad a shorter STABLE round list with the empty set.

## 4. Open targets for the next box
(a) a phase with more than n searches (from spp19_*_n30 and L-ALG spp_*); (b) one vertex falling twice at one context
(renewable reset); (c) a U-shrink in an actual DTL run: needs a split-tangle remainder whose tops were never stable best
vertices before the steal (L-RED reading, R18/§3 above).
