#!/usr/bin/env python3
"""L-NEW box 160, DATA: classify each level-0 step of a 2-wide ladder run by its W-effect (does b_0 = key order of the two level-0
movers flip?) and report JUMP_t = R(s_t) - R(s_(t-1)) + 1 (box 159 R-IDENTITY). ALL=1: every start. Usage: jumpkind.py genome.json ..."""
import sys, os, json, itertools
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box150", "check.py")
ns = {"__file__": P}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]; restrict = ns["restrict"]
def R(G, s):
    keep = [v for v in range(G["N"]) if G["lev"][v] == 0]; H = restrict(G, keep, list(s)); S, _ = Gen(H).run(H["start"]); return len(S) - 1
agg = {"flip": [], "noflip": []}; mx = {"flip": (-99, None), "noflip": (-99, None)}
for f in sys.argv[1:]:
    G = json.load(open(f)); g = Gen(G)
    if any(len(o) != 2 for o in G["opts"]): continue
    L0 = [v for v in range(g.N) if g.lev[v] == 0]
    if len(L0) != 2: continue
    starts = [G["start"]] if not os.environ.get("ALL") else [list(x) for x in itertools.product([0, 1], repeat=g.N)]
    for st in starts:
        S, _ = g.run(st); T = len(S) - 1
        for t in range(1, T + 1):
            if any(S[t][v] != S[t - 1][v] for v in L0):
                k0, k1 = g.keys(S[t - 1]), g.keys(S[t])
                fl = (k0[L0[0]] < k0[L0[1]]) != (k1[L0[0]] < k1[L0[1]])
                j = R(G, S[t]) - R(G, S[t - 1]) + 1; kind = "flip" if fl else "noflip"
                agg[kind].append(j)
                if j > mx[kind][0]: mx[kind] = (j, (os.path.basename(f), st, t, T))
for k in agg:
    a = agg[k]; print(k, "count", len(a), "max", mx[k], "hist", {v: a.count(v) for v in sorted(set(a))})
