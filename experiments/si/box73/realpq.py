#!/usr/bin/env python3
"""L-SI box 73: realise a frame pq model (one-flip run, flip after PRE steps) as a real ISO R197 genome. Same climb as box71/realise.py
(Xi-graph kept from the model, ENC data = rank order, parities, gate orders climbed) but the score is
  pq(G) = max over starts u, bits b, flip times t >= PRE on the flip-free b-run from u of  t + (flip-free (1-b)-run length from s_t),
the real engine being box 64 flipdp.Ext.step (XSIM-checked against L-NEW's Gen in box 64). Usage: realpq.py "<xt>" m PRE target seed iters out.json"""
import sys, os, json, random, ast, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box64"))
from flipdp import Ext
xt_up = ast.literal_eval(sys.argv[1]); m, PRE, target, seed, iters = (int(a) for a in sys.argv[2:7]); out = sys.argv[7]
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
    order = []; seen = set()
    def dfs(z):
        if z in seen: return
        seen.add(z)
        for o in opts[z]:
            if o[1] >= 0: dfs(o[1])
        order.append(z)
    for z in range(N): dfs(z)
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": bp, "start": [0] * N, "xorder": order[::-1]}
def runlen(E, u, b, memo):
    if (u, b) in memo: return memo[(u, b)]
    seq = [u]
    while True:
        n = E.step(seq[-1], b)
        if n == seq[-1] or len(seq) > 200: break
        seq.append(n)
    memo[(u, b)] = seq; return seq
def score(G):
    try: E = Ext(G)
    except AssertionError: return -1000, None
    memo = {}; best = -1; arg = None; nU = len(E.UP); mr = 0
    for u in itertools.product((0, 1), repeat=nU):
        for b in (0, 1):
            seq = runlen(E, u, b, memo); mr = max(mr, len(seq) - 1)
            for t in range(PRE, len(seq)):
                v = t + len(runlen(E, seq[t], 1 - b, memo)) - 1
                if v > best: best, arg = v, (list(u), b, t)
    return (best if best >= 0 else min(mr, PRE) - 100), arg   # climb toward a b-run of PRE steps first
br = list(range(M)); rng.shuffle(br); bp = [rng.randint(0, 1) for _ in range(M)]
g = list(range(M)); rng.shuffle(g); gate = [[g[2 * x], g[2 * x + 1]] for x in range(N)]
cur = (br, bp, gate); cs, carg = score(build(*cur)); best = cs
for it in range(iters):
    br2, bp2, gate2 = list(cur[0]), list(cur[1]), [list(x) for x in cur[2]]; r = rng.random()
    if r < 0.4: i, j = rng.randrange(M), rng.randrange(M); br2[i], br2[j] = br2[j], br2[i]
    elif r < 0.6: bp2[rng.randrange(M)] ^= 1
    else:
        a, b = (rng.randrange(N), rng.randrange(2)), (rng.randrange(N), rng.randrange(2)); gate2[a[0]][a[1]], gate2[b[0]][b[1]] = gate2[b[0]][b[1]], gate2[a[0]][a[1]]
    s, arg = score(build(br2, bp2, gate2))
    if s >= cs: cur, cs, carg = (br2, bp2, gate2), s, arg
    if cs > best:
        best = cs
        if carg is not None:
            G = build(*cur); G["pq_witness"] = {"start_up": carg[0], "bit": carg[1], "flip_after": carg[2], "total": cs}
            json.dump(G, open(out, "w")); print("it", it, "score", best, "witness", carg, flush=True)
        if best >= target: break
print("FINAL best", best, "target", target)
