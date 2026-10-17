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
- Searches so far (stable unless noted, root/depthfit.py = dtl_stealdepth.analyze unmodified): one-edge neighbourhood of
  stealonce_viol_n76 at 8 vertices (235 variants: max k 2, max depth 1); stealk climbs (both orders, ~1 h: k 2 stable, 1 Oink);
  depth climbs from stealonce_core_n76 and stealonce_viol_n76 (both orders) and a one-edge depth scan of the core: running.

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
