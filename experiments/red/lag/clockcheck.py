#!/usr/bin/env python3
"""L-RED box 10 (produced on Opus 5.5): region-clock check. For the root context (depth 0, R = G') of the longest phase, print per
visit the size of the round-1 region of top TOPID (input id), i.e. |P(next step)| - |P(this step)|, by the UNMODIFIED L-ALG model
(dtl_stealdepth.run_game, RM_PREF=1). Usage: DTL_ORDER=stable|oink clockcheck.py G.pg TOPID"""
import sys, os
A = os.path.join(os.environ["LALG_DIR"], "experiments", "alg"); sys.path.insert(0, A); sys.path.insert(0, os.path.join(A, "..", "harness"))
for k_, v_ in (("RM_DV", "0"), ("RM_LIGHT", "1"), ("RM_EXCL", "1"), ("RM_PREF", "1")): os.environ[k_] = v_
import pg, dtl_stealdepth as SD
sys.setrecursionlimit(100000)
d = SD.run_game(pg.read(sys.argv[1]), os.environ.get("DTL_ORDER", "stable")); X = d.idx; top = int(sys.argv[2])
ph = max(SD.FD.phase_rows(d), key=len); rcs = [rc for r in ph for rc in r["recs"] if rc["key"][0] == 0 and len(rc["key"][1]) == len(ph[0]["G"])]
out = []
for rc in rcs:
    ks = sorted([k for k in rc.get("pref", {}) if k[0] == 1], key=lambda k: -k[1]); i = [X[k[1]] for k in ks].index(top)
    out.append(len(rc["pref"][ks[i + 1]]) - len(rc["pref"][ks[i]]) if i + 1 < len(ks) else None)
print(os.environ.get("DTL_ORDER", "stable"), "phase searches", len(ph), "region sizes of top", top, "per visit:", out)
