#!/usr/bin/env python3
"""L-RED 56 R221: Lemma B-ONLY check. At every state of own.py's IDEAL-CYC run and every vertex v other than c_W and the e-vertices whose
W-target is c_W: Lambda_t(v) is less relevant than every e-vertex (a beta, K1, K2 or cX). Counts (t, v) pairs and violations; also gate ties.
Usage: bonly221.py G.json ..."""
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import own
tp = tv = tt = 0
for f in sys.argv[1:]:
    try: G = json.load(open(f))
    except Exception: continue
    if not (isinstance(G, dict) and "opts" in G): continue
    out, V, O, o_ = own.run(G); n, prio, _, succ, _, _ = own.build(G); rk = own.VJ(prio).rk
    evs = [V[("e", q)] for q in O]; emin = min(rk[e] for e in evs); cW = V["cW"]
    skip = {cW} | {V[("e", q)] for q in O if G["opts"][q[0]][q[1]][0] < 0}
    p = v_ = ties = 0
    for s, vals, tau in out:
        for v in range(n):
            if v in skip: continue
            p += 1; v_ += rk[vals[v][0]] >= emin
        ties += sum(1 for q in O if vals[V[("e", q)]] == vals[V[("b", q)]])
    tp += p; tv += v_; tt += ties
    if v_ or ties: print("VIOLATION", f, v_, ties, flush=True)
print(f"runs {len(sys.argv) - 1} (t, v) pairs {tp} Lambda >= some e: {tv}; gate ties {tt}", flush=True)
