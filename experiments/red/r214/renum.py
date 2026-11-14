#!/usr/bin/env python3
"""L-RED R214: order-preserving renumbering of gate indices and beta ranks to 0..M-1 (keeps start, keys and Xi-order; lemck needs it).
Usage: renum.py in.json out.json"""
import sys, json
G = json.load(open(sys.argv[1])); N = G["N"]
ids = sorted({o[2] for v in range(N) for o in G["opts"][v]}); rid = {i: q for q, i in enumerate(ids)}
br = [0] * len(ids); bp = [0] * len(ids)
for q, i in enumerate(sorted(ids, key=lambda i: G["br"][i])): br[rid[i]] = q; bp[rid[i]] = G["bp"][i]
G["opts"] = [[[o[0], o[1], rid[o[2]]] for o in G["opts"][v]] for v in range(N)]; G["br"], G["bp"] = br, bp
gs = sorted(x for g in G["gate"] for x in g); gid = {x: q for q, x in enumerate(gs)}; G["gate"] = [[gid[x] for x in g] for g in G["gate"]]
G.pop("deg", None); json.dump(G, open(sys.argv[2], "w"))
