#!/usr/bin/env python3
"""L-RED R213: per-option value rises R(x, k) along IDEAL runs (L-NEW box 180 definition: R(x, k) = #strict rises of cv(xt(x, k)),
0 for target X). Own implementation: cv_s(z) = sum of +-2^rank along z's current Xi-chain under s (R105 ENC), run by r187/ideal.py.
Also counts FALL (cv falls; must be 0 by R105 MONO). Usage: rises.py genome.json [--all]  (--all: max over all starts)"""
import sys, os, json, itertools
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187")]
import ideal
def cv(G, s, z):
    t = 0
    while True:
        o = G["opts"][z][s[z]]; m = o[2]; t += (1 if G["bp"][m] == 0 else -1) * (1 << G["br"][m])
        if o[1] < 0: return t
        z = o[1]
def rises(G, start=None):
    if start is not None: G = dict(G, start=list(start))
    S, _ = ideal.traj(G); N = G["N"]; R = {}; fall = 0
    vals = [[cv(G, s, z) for z in range(N)] for s in S]
    rz = [sum(1 for t in range(1, len(S)) if vals[t][z] > vals[t - 1][z]) for z in range(N)]
    fall = sum(1 for t in range(1, len(S)) for z in range(N) if vals[t][z] < vals[t - 1][z])
    for x in range(N):
        for k, o in enumerate(G["opts"][x]): R[(x, k)] = rz[o[1]] if o[1] >= 0 else 0
    best = max(R, key=lambda q: R[q])
    return len(S) - 1, R[best], best, rz, fall
if __name__ == "__main__":
    G = json.load(open(sys.argv[1]))
    if "--all" in sys.argv:
        res = max((rises(G, u) + (u,) for u in itertools.product(range(2), repeat=G["N"])), key=lambda r: (r[1], r[0]))
        T, r, opt, rz, fall, u = res; print(f"RISES {os.path.basename(sys.argv[1])} all-starts maxR {r} option {opt} T {T} start {''.join(map(str, u))} FALL {fall}")
    else:
        T, r, opt, rz, fall = rises(G); print(f"RISES {os.path.basename(sys.argv[1])} T {T} maxR {r} option {opt} per-mover {rz} FALL {fall}")
