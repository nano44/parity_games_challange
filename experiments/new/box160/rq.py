#!/usr/bin/env python3
"""L-NEW box 160, DATA: along a run, R_q(s_t) for every level-0 configuration q (frozen-remainder lengths, box 159) and b_0(q).
Usage: rq.py genome.json ..."""
import sys, os, json, itertools
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box150", "check.py")
ns = {"__file__": P}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]; restrict = ns["restrict"]
for f in sys.argv[1:]:
    G = json.load(open(f)); g = Gen(G); S, _ = g.run(G["start"]); T = len(S) - 1
    L0 = [v for v in range(g.N) if g.lev[v] == 0]
    z = [t for t in range(1, T + 1) if any(S[t][v] != S[t - 1][v] for v in L0)]
    print(os.path.basename(f), "T", T, "level-0 steps", z)
    for q in itertools.product([0, 1], repeat=len(L0)):
        rows = []
        for s in S:
            s2 = list(s)
            for v, b in zip(L0, q): s2[v] = b
            H = restrict(G, L0, s2); SS, _ = Gen(H).run(H["start"]); rows.append(len(SS) - 1)
        k = g.keys(tuple(q) + tuple(S[0][len(L0):])); b0 = int(k[L0[0]] < k[L0[1]])
        print(f"  q {q} b0 {b0} R_q(s_t) = {rows}")
