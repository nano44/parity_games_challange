#!/usr/bin/env python3
"""box 156: per-step trigger detail (deg <= 2): for each mover z of step t: lev, pi, and X (Xi-triggered: Xi comparison flipped
between s_(t-2), s_(t-1); its movers at t-1 on z's chains) / W (key order flipped between keys of s_(t-1), s_t; lower movers at t)."""
import sys, json
from val import ns
Gen = ns["Gen"]
G = json.load(open(sys.argv[1])); g = Gen(G); N = g.N; S, _ = g.run(G["start"]); T = len(S) - 1; K = [g.keys(s) for s in S]
print("N", N, "T", T, "lev", G["lev"])
for t in range(1, T + 1):
    mv = [v for v in range(N) if S[t][v] != S[t - 1][v]]; out = []
    for z in mv:
        if t == 1: out.append(f"{z}(l{g.lev[z]})"); continue
        o = S[t - 1][z]; p = 1 - o
        xi = (g.face(S[t - 2], z, p) > g.face(S[t - 2], z, o)) != (g.face(S[t - 1], z, p) > g.face(S[t - 1], z, o))
        w = (g.optkey(K[t - 1], z, p) < g.optkey(K[t - 1], z, o)) != (g.optkey(K[t], z, p) < g.optkey(K[t], z, o))
        src = [y for y in set(g.play(S[t - 2], z, o)) | set(g.play(S[t - 2], z, p)) if S[t - 1][y] != S[t - 2][y]]
        out.append(f"{z}(l{g.lev[z]}){'X' + str(sorted(src)) if xi else ''}{'W' if w else ''}")
    print(f"t{t}:", " ".join(out))
