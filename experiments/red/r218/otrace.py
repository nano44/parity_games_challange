#!/usr/bin/env python3
"""L-RED 55 R218: named trace of the own.py IDEAL-CYC Howard run. Per state: each multi-option mover's option label, faces (e/b) of
the level-1 gates of the named movers. Usage: otrace.py G.json names.json [mover ...]  (labels from <G>.labels.json if present)"""
import sys, json, os
import own
G = json.load(open(sys.argv[1])); nm = json.load(open(sys.argv[2])); inv = {v: k for k, v in nm.items()}
lp = sys.argv[1][:-5] + ".labels.json"; lab = json.load(open(lp)) if os.path.exists(lp) else None
out, V, O, ow = own.run(G); inv_g = {V[("g", q)]: q for q in O}
show = sys.argv[3:] or [inv[x] for x in range(G["N"]) if len(G["opts"][x]) > 1]
for t, (s, vals, tau) in enumerate(out):
    row = []
    for m in show:
        x = nm[m]; k = inv_g[s[x]][1]; L = lab[m][k] if lab else str(k)
        if G["lev"][x] == 1:
            q = (x, k); L += "." + ("e" if tau[V[("g", q)]] == V[("e", q)] else "b")
        row.append(f"{m}:{L}")
    print(t, " ".join(row))
