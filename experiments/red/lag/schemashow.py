#!/usr/bin/env python3
"""L-RED box 10 (produced on Opus 5.5): print the observed F/X/- table at steps (1, T_j) for the relay tangles t_j of a
schemaclimb/lag3 game (vertex ids from lag3.build(D): helpers are appended after the skeleton), against the R39 schema target. Usage: schemashow.py G.pg D"""
import sys, os
A = os.path.join(os.environ["LALG_DIR"], "experiments", "alg"); sys.path.insert(0, A); sys.path.insert(0, os.path.join(A, "..", "harness"))
for k_, v_ in (("RM_DV", "0"), ("RM_LIGHT", "1"), ("RM_EXCL", "1"), ("RM_PREF", "1")): os.environ[k_] = v_
import pg, dtl_stealdepth as SD, schemaclimb as SC, re
sys.setrecursionlimit(100000)
f, D = sys.argv[1], int(sys.argv[2]); import lag3, lag4; names = dict((lag4 if os.environ.get("SKEL") == "4" else lag3).build(D).ids)   # skeleton ids (helpers come after)
g = pg.read(f); d = SD.run_game(g, os.environ.get("DTL_ORDER", "stable")); inv = {v: i for i, v in enumerate(d.idx)}
ph = SD.FD.phase_rows(d)[0]; rcs = [rc for r in ph for rc in r["recs"] if rc["key"][0] == 0 and len(rc["key"][1]) == len(ph[0]["G"])]
T = SC.target(D, len(rcs))
for j in range(-1, D + 1):
    want = {inv[names[f"{c}{j}"]] for c in ("tau", "w", "y", "v")}; tid = [t for t in range(len(d.tv)) if {v for v, _ in d.tv[t]} == want]
    k = (1, inv[names[f"T{j}"]]); obs = ""
    for x, rc in enumerate(rcs):
        if not tid: obs += "?"; continue
        obs += "F" if tid[0] in rc.get("fired", {}).get(k, ()) else ("X" if tid[0] in rc.get("excl", {}).get(k, ()) else ("." if k in rc.get("pref", {}) else " "))
    print(f"level {j:2d} target {''.join('F' if T[j][x] else 'X' for x in range(len(rcs)))}  observed {obs}  tangle {tid}")
tot = {}; out = []; print("analyze:", SD.analyze(d, "", tot, out)); [print(" ", l[:200]) for l in out[:8]]
