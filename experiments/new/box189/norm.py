#!/usr/bin/env python3
"""Normalise a box150-format genome (gate indices / beta ranks distinct but not 0..M-1) to R104's packet format by ORDER-PRESERVING
relabelling (keys compare gate indices lexicographically and Xi-values compare by beta rank: both invariant). Lib + CLI: norm.py IN OUT."""
import json, sys
def norm(G):
    G = dict(G); N = G["N"]
    gl = sorted(G["gate"][x][k] for x in range(N) for k in range(len(G["opts"][x]))); assert len(set(gl)) == len(gl)
    G["gate"] = [[gl.index(G["gate"][x][k]) for k in range(len(G["opts"][x]))] for x in range(N)]
    br = G["br"]; assert len(set(br)) == len(br); srt = sorted(br); G["br"] = [srt.index(b) for b in br]
    M = sum(len(o) for o in G["opts"]); assert len(br) == M and sorted(o[2] for x in range(N) for o in G["opts"][x]) == list(range(M))
    return G
if __name__ == "__main__":
    json.dump(norm(json.load(open(sys.argv[1]))), open(sys.argv[2], "w"))
