# R23: GAP-beta realised on A_DTL: an orphan and a duplicate-check hit, both orders; run complete (L-RED box 5, 02:02Z by date -u; produced on Opus 5.5)
Targets (L-ALG docs/alg/GAP-C.md §2-§6a, relayed by the Lead 01:40Z-02:01Z): (NO-ORPHAN) at no best_vertices call is there a
stored p-tangle t inside the context R with all escapes outside R; GAP-beta: a duplicate-check hit (dtl.cpp 385-424);
Lemma K / completeness.

## 1. Tools
experiments/red/carry/dupcheck.py: L-ALG's dtl_pyref through dtl_deficit.build (read-only, LALG_DIR = l-alg 57e2256), order
from DTL_ORDER; counts hits of pyref's duplicate check (`if key in self.tkeys: continue`, the transcription of dtl.cpp
385-424) by wrapping tkeys (wrapper verified by a forced lookup); counts orphans at every best_vertices call (any depth);
checks completeness (no vertex left in G) and winners against Zielonka (experiments/harness/zielonka.py).
carry/gapb.py adds L-ALG's dtl_nearorphan2.py (unmodified, subprocess, l-alg 1335713) for the graded near-orphan level.
Climb: dtl_search --fitness dupchk, stable order, seed 8020, from L-ALG's spp_final_n20, ~2,500 steps.

## 2. FINDING (experiments/red/carry/instances/gapb_dup_n20.pg)
n = 20, sha1 2f433a31. Pinned Oink: 1 dominion, 26 tangles, 14 iterations, solution verified (11 strategies).
- L-ALG's dtl_orphan.py, unmodified (l-alg 1335713): DTL_ORDER=oink {'calls': 96, 'stable calls': 15, 'calls with orphan': 1,
  'stable calls with orphan': 1, 'orphan top in V*': 1, 'near-orphans': 19}; stable {'calls': 107, ..., 'calls with orphan': 1,
  'stable calls with orphan': 1, 'orphan top in V*': 1, 'near-orphans': 24}.
- dupcheck.py, both orders: 1 duplicate-check hit, 1 orphan, 0 unsolved, 0 wrong (vs Zielonka).
- Anatomy (original ids, identical in both orders): Even's phase, search index 2. The orphan is the Even tangle {3, 4}
  (vertex 4: priority 12, Odd-owned, self-loop; vertex 3: priority 1, Odd-owned), tangle priority 12, 14 escapes
  {0,1,2,5,6,7,8,9,10,12,13,14,16,17}. At a DEPTH-1 best_vertices call whose context is exactly {3, 4}, every escape is
  outside the context; the top re-finds {3, 4} as a closed region and extractTangles hits the duplicate key [3, 4].
- The run nevertheless ends COMPLETE and CORRECT (Oink verified; pyref winners = Zielonka's).
So (NO-ORPHAN) is FALSE on A_DTL and the GAP-beta duplicate is reachable; Lemma K / completeness is not refuted.

## 3. Pinned Oink prints the hit itself
CHECK_UNIQUE is compiled in release too (dtl.cpp:23 "#define CHECK_UNIQUE (1 or !NDEBUG)") and logs "duplicate tangle" at
trace >= 1 (dtl.cpp:407-409). tools/oink/build/oink --dtl --no-single --no-wcwc --no-loops -t -t on gapb_dup_n20.pg:
iteration 1-even ... "new tangle 10 (5) (depth 0) 13/10 ...", "new tangle 6 (6) ...", "new tangle 6 (7) ... 8/6 ...",
"best vertices: 12/8 (stable)", "duplicate tangle", then "iteration 2-even" (labels are Oink's reindexed id/priority).
So Oink's own duplicate branch (tangle.clear(); continue) runs on this game; the search had already learned three new
tangles at depth 0, so it still returns true and the run proceeds (14 iterations, solution verified).

## 4. Open
An incomplete run: the duplicate must happen in a search that learns nothing else (L-ALG's sketch: "nothing else in
search 2 is productive"). Climbs --fitness gapb from this instance, both orders, in progress.

## 5. W_p filter (Lead 02:15Z, L-ALG (NO-ORPHAN-W))
dupcheck.py now computes W_p(G') with Zielonka (experiments/harness/zielonka.solve_sub on the unsolved set at each search)
and counts orphans / duplicates whose tangle lies inside W_p. gapb_dup_n20: dupW = 0, orphW = 0 in both orders (the
duplicate is in Even's search 1 with W_0(G') empty, as L-ALG found). (NO-ORPHAN-W) is not refuted. Climbs (fitness gapb:
incomplete/wrong >> dupW >> orphW >> barren >> dup >> orphan >> near-orphan) continue.
