# experiments/red/lag (L-RED box 10, produced on Opus 5.5): relay schema for re-steal depth (docs/red/R39)
All measurements use L-ALG's tools UNMODIFIED from a detached checkout (LALG_DIR; box 10: l-alg e0fc1bb0).
- measure.sh G.pg: dtl_spp phases, dtl_stealdepth max depth, dtl_prefexits max exits, dtl_rootmono first-difference contexts,
  both order data.
- Builders: gb.py (named-vertex builder), cl2.py (region clock alone), lag3.py / lag4.py (relay + clock skeletons; lag4 is the
  one that works), schemaclimb.py (climb of the control wiring toward the schema), relaymodel.py (abstract schema + depth rule).
- Inspection: learn.py (tangles learned per search), vtrace.py (fired/excluded per step per visit), sptltrace.py, bvtrace.py,
  srtrace.py (search_rec structure), clockcheck.py (region-clock sizes), schemashow.py / ctrlshow.py (schema table, wiring),
  l2predict.py (predicts where an added level would deepen a re-steal on an existing game), rclock.py (region-clock climb).
- instances/depth{2,3,4}_n{39,46,53}.pg: re-steal depth 2 / 3 / 4 in both order data; pinned Oink 10 / 11 / 12 iterations, verified.
