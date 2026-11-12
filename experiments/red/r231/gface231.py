#!/usr/bin/env python3
"""L-RED 65 R231 item (b): on a gated re-arm genome (gate231.py), own engine: Odd's face at the y gates (e = exit to z0, b = follow R)
per state, and how many carry choosers c_k hold the re-arm option, per state. Usage: gface231.py G.json CW_N"""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r221q"))
import own
G = json.load(open(sys.argv[1])); n0 = int(sys.argv[2]); out, V, O, ow = own.run(G); N = G["N"]; z0 = n0
ys = [x for x in range(N) if G["opts"][x] and G["opts"][x][0][0] == z0]
cks = [x for x in range(N) if any(o[1] in ys for o in G["opts"][x])]
for t, (s, vals, tau) in enumerate(out):
    f = "".join("e" if tau[V[("g", (y, 0))]] == V[("e", (y, 0))] else "b" for y in ys)
    hold = sum(1 for c in cks if G["opts"][c][[V[("g", (c, j))] for j in range(len(G["opts"][c]))].index(s[c])][1] in ys)
    print(f"t {t}: y faces {f}  c_k on re-arm {hold}/{len(cks)}")
