#!/usr/bin/env python3
"""L-NEW box 141: trace of an UP-LADDER IDEAL run: per state, each level's pair (option of u_l, option of v_l), L_l (u or v), the movers
of the step into the state, and per level whether each mover's face order favours option 0 or 1. Usage: trace.py genome.json"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box139"))
import fastcyc_r178 as fc
src = open(os.path.join(HERE, "..", "box139", "paths.py")).read().split("def vx(G):")[0]
ns = {"__file__": os.path.join(HERE, "..", "box139", "paths.py")}; exec(src, ns); run = ns["run"]
G = json.load(open(sys.argv[1])); S, CUR, KEY, why = run(G); N, opts = G["N"], G["opts"]; d = N // 2
for t, s in enumerate(S):
    val, idx, _, M = fc.values(G, list(s))
    fav = ["".join(str(int(val(N + idx[(x, 1)]) > val(N + idx[(x, 0)]))) for x in (2 * l, 2 * l + 1)) for l in range(d)]
    K = KEY[t] if t < len(KEY) else None
    L = ["u" if K and K[2 * l] < K[2 * l + 1] else "v" for l in range(d)] if K else ["?"] * d
    mv = [x for x in range(N) if t > 0 and S[t][x] != S[t - 1][x]]
    print(f"t{t:2d} " + " | ".join(f"L{l}:{s[2*l]}{s[2*l+1]} {L[l]} f{fav[l]}" for l in range(d)) + f"   movers {mv}")
print("stop", why)
