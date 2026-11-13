#!/usr/bin/env python3
"""L-COMP box 47: the ENUMERATION DEPTH k(G) (Lead 09:15Z; L-NEW box 217 §5 track A) measured on box 190's n5v (mode spec) run from S3 on
Γ3(G) (replay47.run, optional e-permutation): sw(x) = #steps t < T with s_(t+1)(x) ≠ s_t(x) (states before the first fallback);
|K(x)| = the number of W-paths from x to level 0 (keys = tuples of distinct e-indices, so distinct paths are distinct keys; level-0 mover:
its degree); full(x) iff sw(x) = |K(x)| − 1; k_A6(G) = max over full movers of lev(x) + 1 (0 if none); khalf (Lead 10:03Z, the «half
enumeration» depth) = the largest level l with a level-l mover at sw >= |K|/2 − 1 (|K| >= 2). Also per level: the max sw and |K| of
its movers, and whether a full mover exists. Usage: k47.py G.json ...  (env LNEW)"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import replay47
def kdepth(G, seq):
    N, lev = G["N"], G["lev"]; T = len(seq) - 1
    sw = [sum(1 for t in range(T) if seq[t + 1][x] != seq[t][x]) for x in range(N)]
    P = [0] * N
    for l in range(max(lev) + 1):
        for x in range(N):
            if lev[x] == l: P[x] = sum(1 if l == 0 else P[o[0]] for o in G["opts"][x])
    full = [sw[x] == P[x] - 1 for x in range(N)]; k = max([lev[x] + 1 for x in range(N) if full[x]], default=0)
    khalf = max([lev[x] for x in range(N) if P[x] >= 2 and sw[x] >= P[x] // 2 - 1], default=-1)
    per = []
    for l in range(max(lev) + 1):
        xs = [x for x in range(N) if lev[x] == l]
        per.append("%d:%d/%d%s" % (l, max(sw[x] for x in xs), max(P[x] for x in xs), "F" if any(full[x] for x in xs) else ""))
    return k, T, sw, P, per, khalf
if __name__ == "__main__":
    for fn in sys.argv[1:]:
        G = json.load(open(fn)); G = G if "N" in G else G["genome"]; r = replay47.run(G, "spec")
        k, T, sw, P, per, khalf = kdepth(G, r["seq"])
        print("%s N %d N+M %d d %d T %d k_A6 %d khalf %d | level:max_sw/max_K(F = a full mover) %s" % (os.path.basename(fn), G["N"], G["N"] + sum(len(o) for o in G["opts"]), max(G["lev"]) + 1, T, k, khalf, " ".join(per)), flush=True)
