#!/usr/bin/env python3
"""L-SI box 74: realise a frame «flips» model as a real ISO R197 genome. Keeps the model's Xi-graph, climbs ENC data (box 71 realise.py
moves) to maximise F = key-order flips of the top pair (movers 2m, 2m+1) along a flip-free run (K = 0) of the real IDEAL engine
(box 64 flipdp.Ext.step, XSIM-checked). ord_s = [key_s(A_m, s(A_m)) < key_s(B_m, s(B_m))], keys = R104 keys under s (level 0 forced to q_b).
Usage: realflip.py "<xt>" m target seed iters out.json      (score: max over starts u and bits b of F along the b-run from u)
Env K = max external-bit changes (default 0): score = max F over runs with <= K changes (DP over (state, bit, changes left); a change
counts only at a step that moves; ord of s_t is read with the bit of the step that produced s_t, as frame.py mode flips)."""
import sys, os, json, random, ast, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box73")); sys.path.insert(0, os.path.join(HERE, "..", "box64"))
from flipdp import Ext
xt_up = ast.literal_eval(sys.argv[1]); m, target, seed, iters = (int(a) for a in sys.argv[2:6]); out = sys.argv[6]
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
def keys(E, st):
    key = [None] * E.N
    for v in E.byl:
        wt = E.opts[v][st[v]][0]; key[v] = (E.gate[v][st[v]],) if wt < 0 else key[wt] + (E.gate[v][st[v]],)
    return key
def ordtop(E, up, b):
    k = keys(E, E.full(up, b)); return k[2 * m] < k[2 * m + 1]
KF = int(os.environ.get("K", "0"))
def scoreK(E):
    from functools import lru_cache
    @lru_cache(None)
    def V(u, pb, left):
        best = (0, ())
        for nb in ([pb, 1 - pb] if left > 0 else [pb]):
            n = E.step(u, nb)
            if n == u: continue
            f, path = V(n, nb, left - (nb != pb)); f += int(ordtop(E, u, pb) != ordtop(E, n, nb))
            if f > best[0]: best = (f, (nb,) + path)
        return best
    best, arg = -1, None
    for u in itertools.product((0, 1), repeat=len(E.UP)):
        for b in (0, 1):
            f, path = V(u, b, KF)
            if f > best: best, arg = f, (list(u), b, len(path), list(path))
    return best, arg
def score(G):
    try: E = Ext(G)
    except AssertionError: return -1000, None
    if KF: return scoreK(E)
    best, arg = -1, None
    for u in itertools.product((0, 1), repeat=len(E.UP)):
        for b in (0, 1):
            seq = [u]
            while len(seq) < 100:
                n = E.step(seq[-1], b)
                if n == seq[-1]: break
                seq.append(n)
            o = [ordtop(E, x, b) for x in seq]; F = sum(1 for i in range(len(o) - 1) if o[i] != o[i + 1])
            if F > best: best, arg = F, (list(u), b, len(seq) - 1)
    return best, arg
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
    if cs > best and carg is not None:
        best = cs; G = build(*cur); G["flip_witness"] = {"start_up": carg[0], "bit": carg[1], "T": carg[2], "F": cs, "K": KF, "bits": carg[3] if len(carg) > 3 else None}
        json.dump(G, open(out, "w")); print("it", it, "F", best, "witness", carg, flush=True)
        if best >= target: break
print("FINAL best", best, "target", target)
