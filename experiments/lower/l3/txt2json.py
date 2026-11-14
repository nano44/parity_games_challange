#!/usr/bin/env python3
"""Convert tsearch text genomes (blocks 'd / xt / br / bp / gate / start') to box150 JSON (R110 W-convention).
Usage: txt2json.py in.txt outprefix  -> outprefix_d<d>.json per block"""
import sys, json
def blocks(lines):
    G = None
    for ln in lines:
        w = ln.split()
        if not w: continue
        if w[0] == "d": 
            if G: yield G
            G = {"d": int(w[1])}
        elif G is not None and w[0] in ("xt", "br", "bp", "gate", "start"): G[w[0]] = list(map(int, w[1:]))
    if G: yield G
def tojson(B):
    d = B["d"]; N = 2 * d; opts = []; gate = []
    for x in range(N):
        l = x // 2; o = []
        for k in range(2):
            m = 2 * x + k; o.append([2 * (l - 1) + k if l >= 1 else -1, B["xt"][m], m])
        opts.append(o); gate.append([B["gate"][2 * x], B["gate"][2 * x + 1]])
    return {"N": N, "lev": [x // 2 for x in range(N)], "deg": 2, "opts": opts, "gate": gate, "br": B["br"], "bp": B["bp"],
            "start": B["start"]}
if __name__ == "__main__":
    for B in blocks(open(sys.argv[1])):
        json.dump(tojson(B), open(f"{sys.argv[2]}_d{B['d']}.json", "w"))
