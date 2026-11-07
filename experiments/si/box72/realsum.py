#!/usr/bin/env python3
"""L-SI box 72 (copy of box71/realise.py, score T_0 + T_2): try to REALISE a frame SAT model as a real ISO R197 genome: keep the model's Xi-graph (xt over upper options), hill-climb
ENC data (rank order, parities, all gate orders) to maximise T_k (box 64 flipdp.py, XSIM-checked engine). A realised genome with the
model's T is a real lower bound; failure proves nothing. Usage: realise.py "<xt list>" m K target seed iters out.json"""
import sys, os, json, random, ast
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box64"))
from flipdp import analyse
xt_up = ast.literal_eval(sys.argv[1]); m, K, target, seed, iters, out = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), sys.argv[7]
rng = random.Random(seed); N = 2 * (m + 1); M = 2 * N
def build(br, bp, gate):
    lev = [v // 2 for v in range(N)]; opts = []
    for x in range(N):
        o = []
        for k in range(2):
            wt = 2 * (lev[x] - 1) + k if lev[x] > 0 else -1
            xt = -1 if lev[x] == 0 else (-1 if xt_up[2 * (x - 2) + k] < 0 else xt_up[2 * (x - 2) + k] + 2)
            o.append([wt, xt, 2 * x + k])
        opts.append(o)
    # topological order of the Xi-graph (targets later)
    order = []; seen = set()
    def dfs(z):
        if z in seen: return
        seen.add(z)
        for o in opts[z]:
            if o[1] >= 0: dfs(o[1])
        order.append(z)
    for z in range(N): dfs(z)
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": bp, "start": [0] * N, "xorder": order[::-1]}
def score(G):
    k = K if K >= 0 else 2 * target
    try: r = analyse(G, K=min(k, 3), check=False)
    except AssertionError: return -1
    return r["T"][0] + r["T"][2] if os.environ.get("SUM") == "2" else (r["Tinf"] if K < 0 else r["T"][min(K, 3)])
br = list(range(M)); rng.shuffle(br); bp = [rng.randint(0, 1) for _ in range(M)]
g = list(range(M)); rng.shuffle(g); gate = [[g[2 * x], g[2 * x + 1]] for x in range(N)]
cur = (br, bp, gate); cs = score(build(*cur)); best = cs
for it in range(iters):
    br2, bp2, gate2 = list(cur[0]), list(cur[1]), [list(x) for x in cur[2]]; r = rng.random()
    if r < 0.4: i, j = rng.randrange(M), rng.randrange(M); br2[i], br2[j] = br2[j], br2[i]
    elif r < 0.6: bp2[rng.randrange(M)] ^= 1
    else:
        a, b = (rng.randrange(N), rng.randrange(2)), (rng.randrange(N), rng.randrange(2)); gate2[a[0]][a[1]], gate2[b[0]][b[1]] = gate2[b[0]][b[1]], gate2[a[0]][a[1]]
    s = score(build(br2, bp2, gate2))
    if s >= cs: cur, cs = (br2, bp2, gate2), s
    if cs > best:
        best = cs; json.dump(build(*cur), open(out, "w")); print("it", it, "score", best, flush=True)
        if best >= target: break
print("FINAL best", best, "target", target)
