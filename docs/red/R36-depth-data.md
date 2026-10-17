# R36: box-8 data after R35: the R35 core, re-steal depth, per-step fired counts (L-RED box 8, 20:31Z by date -u; produced on Opus 5.5)
Status: DATA, unrefereed. No kill in this note. Every count is from an UNMODIFIED L-ALG tool, and every instance is pinned
in experiments/red/check.sh and verified by pinned Oink 8fbf0a7 (`--dtl --no-single --no-wcwc --no-loops -v`).

## 1. stealonce_core_n76: the edge-minimised R35 mechanism
- File experiments/red/carry/instances/stealonce_core_n76.pg (n 76, 101 edges, sha1 4e017c28a6c8980e9c112413b5be67d4abd0f565).
  root/shrink.py deletes edges greedily from stealonce_viol_n76 (R35, 450 edges) while keeping permgap max k ≥ 2 and a
  STOLEN-PERM hit (stable). Pinned Oink: 5 dominions, 15 tangles, 4 iterations, verified (33 strategies).
- dtl_rootmono.py (l-alg 931fc221), RM_EXCL=1 RM_PREF=1 RM_DV=0, stable: STOLEN-PERM FAILS 2 / holds 4; NO-REFIRE "REFIRES
  later | prefix later unmeets t" 2. Oink order: no relevant steal.
- dtl_stealdepth.py (l-alg 931fc221), stable: max k 2, max depth 1, 2 re-steals of depth 1, both in one context (|R| 64), at
  steps (r5, top 18) and (r6, top 18), with cause the depth-0 steal at (5, 66) / (6, 66) of tangle 4. Oink: max k 0.
- stealonce_viol_n76 itself: max k 2, max depth 1, 1 re-steal (stable); Oink max k 1, depth 0.

## 2. Depth ≥ 2: not found yet
- Shape needed (Lemma CHARGE, GAP-A-M §23g): the cause of a re-steal must itself be a re-steal, a three-level toggle
  T0 < A < B < C. Here the steal at A's step is by B, then C steals B's tangle so that A refires, and B steals A's new tangle.
- Searches, 20:20Z-21:09Z by date -u (stable unless noted; root/depthfit.py = dtl_stealdepth.analyze unmodified, l-alg 931fc221):
  - one-edge neighbourhood of stealonce_viol_n76 at 8 vertices (235 variants, permgap): max k 2;
  - one-edge neighbourhood of stealonce_core_n76 at 10 vertices (764 variants, depthfit): max k 2, max depth 1;
  - stealk climbs (both orders, ~1 h): k 2 stable, k 1 Oink;
  - depth climbs, 40 min each: from the core (stable, 820 steps), from stealonce_viol_n76 (stable 250 steps, Oink 500 steps).
    Best: max depth 1, max k 2; the core climb reached 26 re-steals of depth 1.
- The re-steals in a climbed core (sha1 7cbcf835, 13 of them at that point) are ONE event repeated in 8 nested depth-0
  contexts (|R| 70, 69, 65, 63, 62, 60, 59, 58), each with the same cause (step (5, 66), tangle 5, depth 0). That is
  replication across contexts, at most 2 per context; it is not branching inside a context.
- Reading (L-RED): depth ≥ 2 needs the cause of a re-steal to be a re-steal. Then the phase must hold ≥ 2 more toggles
  before the base re-steal. The R35 phase has 9 searches and the core's has 4, which leaves no room. A depth-D chain
  needs a phase of about 2D + 2 searches with every level active, so phase length is the resource to build next.

## 3. (FIRED-STEP) per-step counts (GAP-A-M §23d candidate: bounded by a constant c)
- File experiments/red/carry/instances/firedstep13_n76.pg (sha1 68df1c0d23fa2e91401338d325f4b873b2a0b815), found by a
  permgap PERMFIT=firedstep climb (seed 26001) from stealonce_viol_n76. Pinned Oink: 5 dominions, 38 tangles, 4 iterations,
  verified (36 strategies).
- dtl_firedlong2.py (l-alg 9b621aa2) FL_ALL=1, RM_EXCL=1 RM_LIGHT=1 RM_DV=0: stable "max distinct tangles fired at one step
  (round, top) in a phase: 13", NO-RETURN holds 17. Oink order: 2. The §23d corpus max was 3; R35 had 4; an earlier snapshot
  of the same climb (sha1 9a886c61) had 8 (Oink 3).
- Reading (L-RED): one region step can fire many tangles in a single tattr, so a constant c cannot hold once a top's region
  can absorb many independent tangles. The count that matters for (FIRED-R) is its growth with n, which this one instance
  does not measure.

## 4. Long-phase (FIRED-R) (Lead item 2): best ratio 0.667 in both orders (was 0.455, unpinned)
Judge: root/firedlong.py, which counts a context when it is visited ≥ 2 times in a phase of S ≥ 2|R| searches. Climbs from the
SPP seeds use FLGRAD=1, a gradient when no context is counted yet; the measure printed by the judge is unchanged.
| file (sha1) | n | stable: fired / \|R\| / S | Oink: fired / \|R\| / S | pinned Oink |
|---|---|---|---|---|
| firedlong667_n43.pg (7f15d7ba4a72) | 43 | 4 / 6 / 14 (0.667) | 4 / 6 / 14 (0.667) | 2 dominions, 22 tangles, 16 iterations, verified |
| firedlong667_n20.pg (2f9da571a7a1) | 20 | 4 / 6 / 12 (0.667) | 4 / 6 / 12 (0.667) | 1 dominion, 26 tangles, 14 iterations, verified |
| (unpinned) l21014 (96e4f9e67cdf) | 30 | 3 / 5 / 12 (0.6) | 2 / 5 / 12 (0.4) | 2 dominions, 33 tangles, 14 iterations, verified |
- L-ALG experiments/alg/dtl_firedlong2.py UNMODIFIED (l-alg 931fc221; default long-phase filter) agrees on both pinned files
  in both orders: max ratio 0.667, max fired 4, per-step max 4, NO-RETURN holds, no INCOMPLETE.
- Seeds: spp_chain_up_n43 (L-ALG; its phase is 42 searches long but no context is visited twice in it), spp_n20 (L-ALG),
  spp19_stable_n30 (L-RED). The climbs shortened the phases from 42/18/19 to 14/12/12 searches and found contexts of size 5-6.
- Reading (L-RED): 4 fired at |R| 6. These are single instances with small contexts, so they show no trend of fired/|R|
  with phase length. The climbs keep running.
