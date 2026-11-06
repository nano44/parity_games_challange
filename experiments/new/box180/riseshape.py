#!/usr/bin/env python3
"""L-NEW box 180: per-option shape of value rises. For every option (x, k) of every run: R(x, k) against dep(x, k) (movers on the longest
Xi-path below the option), the number D(x, k) of distinct movers reachable below it, and the level count d. Prints the largest R - dep,
R / dep, R - D, and counts of R > 2 dep and R > D + 1. Usage: riseshape.py files..."""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__)); P0 = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P0, "__name__": "lib"}; exec(open(P0).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
st = dict(options=0, R_gt_2dep=0, R_gt_D1=0); ex = {}
def below(G, x, k):
    seen, todo = set(), [G["opts"][x][k][1]]
    while todo:
        v = todo.pop()
        if v < 0 or v in seen: continue
        seen.add(v); todo += [o[1] for o in G["opts"][v]]
    return seen
def dep(G, x, k, memo):
    if (x, k) not in memo:
        xt = G["opts"][x][k][1]; memo[(x, k)] = 0 if xt < 0 else 1 + max(dep(G, xt, j, memo) for j in range(len(G["opts"][xt])))
    return memo[(x, k)]
for f in sys.argv[1:]:
    try: G = json.load(open(f)); g = Gen(G); S, _ = g.run(G["start"], cap=5000)
    except Exception: continue
    memo = {}; T = len(S) - 1
    for x in range(G["N"]):
        for k in range(len(G["opts"][x])):
            v = [g.face(s, x, k) for s in S]; R = sum(1 for t in range(1, T + 1) if v[t] > v[t - 1]); dp = dep(G, x, k, memo); D = len(below(G, x, k))
            st["options"] += 1; st["R_gt_2dep"] += R > 2 * dp; st["R_gt_D1"] += R > D + 1
            for key, val in (("R-dep", R - dp), ("R-D", R - D)):
                if val > ex.get(key, (-99,))[0]: ex[key] = (val, os.path.basename(f), (x, k), R, dp, D)
print(" ".join("%s %d" % kv for kv in st.items()))
for k, v in ex.items(): print("max %s = %d at %s option %s (R %d dep %d D %d)" % ((k,) + v))
