#!/usr/bin/env python3
"""L-RED box 10 (produced on Opus 5.5): per phase and best_vertices context, each visit's steps (round, top) with the tangles
fired (F) and excluded (X) there, as the UNMODIFIED L-ALG model records them (dtl_stealdepth.run_game: RM with RM_EXCL=1
RM_PREF=1). Ids are input ids; a tangle prints as #id{vertices}. VT_MAXR = max |R| shown (default all); VT_PH = phase index.
Usage: LALG_DIR=... DTL_ORDER=stable|oink vtrace.py G.pg"""
import sys, os
A = os.path.join(os.environ["LALG_DIR"], "experiments", "alg"); sys.path.insert(0, A); sys.path.insert(0, os.path.join(A, "..", "harness"))
os.environ.setdefault("RM_EXCL", "1"); os.environ.setdefault("RM_PREF", "1"); os.environ.setdefault("RM_LIGHT", "1"); os.environ.setdefault("RM_DV", "0")
import pg, dtl_stealdepth as SD
sys.setrecursionlimit(100000)
g = pg.read(sys.argv[1]); d = SD.run_game(g, os.environ.get("DTL_ORDER", "stable")); X = d.idx
tn = lambda t: "#%d{%s}" % (t, ",".join(str(X[v]) for v, _ in d.tv[t]))
for phn, ph in enumerate(SD.FD.phase_rows(d)):
    if "VT_PH" in os.environ and int(os.environ["VT_PH"]) != phn: continue
    print(f"== phase {phn} p={ph[0]['p']} searches {len(ph)} tangles learned per search {[r.get('t1', 0) - r.get('t0', 0) for r in ph]}")
    vis = {}
    for s, r_ in enumerate(ph):
        for rc in r_["recs"]: vis.setdefault(rc["key"], []).append((s, rc))
    for key, rcs in vis.items():
        if len(key[1]) > int(os.environ.get("VT_MAXR", 10 ** 9)): continue
        print(f"-- context depth {key[0]} |R| {len(key[1])} visits {len(rcs)}")
        for i, (s, rc) in enumerate(rcs):
            steps = sorted(set(rc.get("fired", {})) | set(rc.get("excl", {})), key=lambda k: (k[0], -k[1]))
            row = []
            for k in steps:
                F = rc.get("fired", {}).get(k, ()); E = rc.get("excl", {}).get(k, ())
                if F or E: row.append(f"(r{k[0]},{X[k[1]]})" + (" F" + " ".join(tn(t) for t in sorted(F)) if F else "") + (" X" + " ".join(tn(t) for t in sorted(E)) if E else ""))
            print(f"  visit {i} (search {s}) ntv {rc['ntv']}: " + " | ".join(row))
