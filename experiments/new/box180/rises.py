#!/usr/bin/env python3
"""L-NEW box 180: VALUE RISES. For a run of an IDEAL genome (box150 simulator), R(x, k) := #steps t with v_(s_t)(x, k) > v_(s_(t-1))(x, k)
(option values never fall: v(x, k) = eps + cv(xt) and cv is monotone by R105 MONO; checked here: FALL counts any fall).
P(x, k) := #maximal Xi-paths from option (x, k); dep(x, k) := longest Xi-path length (movers) below it. Also checks the reduction
REDUCE: T <= 1 + #steps t <= T - 1 at which some option value rises (R105 XI-NEW/RISE), hence max R <= T <= 1 + sum R.
Runs from the stored start and from the arg-max start over all starts when N <= 14. Usage: rises.py files..."""
import os, sys, json, itertools
H = os.path.dirname(os.path.abspath(__file__)); P0 = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P0, "__name__": "lib"}; exec(open(P0).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
def paths(G, x, k, memo):
    if (x, k) in memo: return memo[(x, k)]
    xt = G["opts"][x][k][1]
    r = (1, 0) if xt < 0 else (sum(paths(G, xt, j, memo)[0] for j in range(len(G["opts"][xt]))),
                              1 + max(paths(G, xt, j, memo)[1] for j in range(len(G["opts"][xt]))))
    memo[(x, k)] = r; return r
TOT = dict(runs=0, FALL=0, REDUCE=0)
def one(G, start, tag):
    g = Gen(G); S, _ = g.run(start); T = len(S) - 1; N = G["N"]; memo = {}
    opts = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]
    val = [[g.face(s, x, k) for (x, k) in opts] for s in S]
    R = [0] * len(opts); risesteps = 0
    for t in range(1, T + 1):
        any_r = False
        for i in range(len(opts)):
            if val[t][i] > val[t - 1][i]: R[i] += 1; any_r = True
            elif val[t][i] < val[t - 1][i]: TOT["FALL"] += 1
        risesteps += any_r and t <= T - 1
    if T > 1 + risesteps: TOT["REDUCE"] += 1
    TOT["runs"] += 1
    i = max(range(len(opts)), key=lambda i: (R[i], -paths(G, *opts[i], memo)[0]))
    Pm, dm = paths(G, *opts[i], memo)
    dd = max(G["lev"]) + 1; TOT["maxR>2d"] = TOT.get("maxR>2d", 0) + (R[i] > 2 * dd)
    print("%-28s d %2d N %2d T %3d sumR %4d maxR %2d (2d %2d) at %s P %d dep %d  maxP %d" % (tag, dd, N, T, sum(R), R[i], 2 * dd, opts[i], Pm, dm,
          max(paths(G, x, k, memo)[0] for x, k in opts)))
    return T, R[i]
for f in sys.argv[1:]:
    try: G = json.load(open(f)); assert isinstance(G, dict) and "opts" in G
    except Exception: continue
    b = os.path.basename(f)
    try:
        one(G, tuple(G["start"]), b)
        if G["N"] <= 14:
            g = Gen(G); best = max(itertools.product((0, 1) if all(len(o) == 2 for o in G["opts"]) else [0], repeat=G["N"]),
                                   key=lambda s: len(g.run(s)[0])) if all(len(o) == 2 for o in G["opts"]) else None
            if best is not None and tuple(best) != tuple(G["start"]): one(G, best, b + "@max")
    except RuntimeError as e: print(b, "skip", e)
print(" ".join("%s %d" % kv for kv in TOT.items()))
