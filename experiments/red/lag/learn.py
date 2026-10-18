#!/usr/bin/env python3
"""L-RED box 10 (produced on Opus 5.5): per search (player, iteration), the tangles and dominions learned, in input ids,
with the top that learned them; the UNMODIFIED L-ALG model (dtl_stealdepth.run_game). Usage: LALG_DIR=... learn.py G.pg"""
import sys, os
A = os.path.join(os.environ["LALG_DIR"], "experiments", "alg"); sys.path.insert(0, A); sys.path.insert(0, os.path.join(A, "..", "harness"))
for k in ("RM_EXCL", "RM_PREF", "RM_LIGHT"): os.environ.setdefault(k, "1")
os.environ.setdefault("RM_DV", "0")
import pg, dtl_stealdepth as SD
sys.setrecursionlimit(100000)
g = pg.read(sys.argv[1]); d = SD.run_game(g, os.environ.get("DTL_ORDER", "stable")); X = d.idx
ntv = [max([rc["ntv"] for rc in r["recs"]] or [0]) for r in d.trace]
seen = 0
for s, r in enumerate(d.trace):
    nxt = max([rc["ntv"] for rc in d.trace[s + 1]["recs"]] or [len(d.tv)]) if s + 1 < len(d.trace) else len(d.tv)
    new = [t for t in range(seen, nxt)]; seen = max(seen, nxt)
    print(f"search {s} p={r['p']} dom_before={r['dom']} |G|={len(r['G'])} learned:", " ".join("#%d{%s}pr%d esc{%s}" % (t, ",".join(str(X[v]) for v, _ in d.tv[t]), d.tpr[t] if d.tpr[t] >= 0 else -1, ",".join(str(X[e]) for e in d.tout[t])) for t in new))
print("win", "".join(str(w) for w in d.win), "iterations", d.iterations)
