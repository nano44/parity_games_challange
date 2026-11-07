#!/usr/bin/env python3
"""L-NEW box 143: hill-climb Sum DELAY (box 142 lag.py analyse) on 2-wide deg-2 IDEAL-ACYC ladders (R178 §1 rule; R188 genome format:
W-targets = the two lower movers, Xi-targets = any mover later in a free topological order 'xorder', or T). SCORE = Sum_l DELAY_l
(ties broken by steps). Usage: dclimb.py d iters seed out.json [UP=1: Xi-targets strictly higher level only]"""
import sys, os, json, random
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "..", "box142", "lag.py")).read().split('if sys.argv[1] == "--rand":')[0]
ns = {"__file__": os.path.join(HERE, "..", "box142", "lag.py")}; exec(src, ns); analyse = ns["analyse"]
UP = os.environ.get("UP")
def later(G, v):
    N = G["N"]
    if UP: return [u for u in range(N) if G["lev"][u] > G["lev"][v]] + [-1]
    xo = G["xorder"]; p = xo.index(v); return xo[p + 1:] + [-1]
def fix(G):
    for v in range(G["N"]):
        for k in range(2):
            if G["opts"][v][k][1] not in later(G, v): G["opts"][v][k][1] = random.choice(later(G, v))
def rand(d, rng):
    N = 2 * d; lev = [i // 2 for i in range(N)]; xo = list(range(N)); rng.shuffle(xo)
    if UP: xo = list(range(N))
    G = dict(N=N, lev=lev, deg=2, xorder=xo); opts = []; b = 0
    for v in range(N):
        l = lev[v]; o = []
        for k in range(2): o.append([-1 if l == 0 else 2 * (l - 1) + k, -1, b]); b += 1
        opts.append(o)
    G["opts"] = opts
    for v in range(N):
        for k in range(2): opts[v][k][1] = rng.choice(later(G, v))
    br = list(range(b)); rng.shuffle(br); gates = list(range(b)); rng.shuffle(gates)
    G.update(gate=[gates[2 * v:2 * v + 2] for v in range(N)], br=br, bp=[rng.randint(0, 1) for _ in range(b)], start=[rng.randrange(2) for _ in range(N)])
    return G
def mut(G, rng):
    H = json.loads(json.dumps(G)); N = H["N"]; r = rng.random(); v = rng.randrange(N); k = rng.randrange(2)
    if r < 0.3: H["opts"][v][k][1] = rng.choice(later(H, v))
    elif r < 0.4 and not UP:
        xo = H["xorder"]; i = rng.randrange(N - 1); xo[i], xo[i + 1] = xo[i + 1], xo[i]
        for u in range(N):
            for kk in range(2):
                if H["opts"][u][kk][1] not in later(H, u): H["opts"][u][kk][1] = rng.choice(later(H, u))
    elif r < 0.55: i, j = rng.randrange(len(H["br"])), rng.randrange(len(H["br"])); H["br"][i], H["br"][j] = H["br"][j], H["br"][i]
    elif r < 0.65: i = rng.randrange(len(H["bp"])); H["bp"][i] ^= 1
    elif r < 0.88:
        a, b = rng.randrange(N), rng.randrange(N); ka, kb = rng.randrange(2), rng.randrange(2)
        H["gate"][a][ka], H["gate"][b][kb] = H["gate"][b][kb], H["gate"][a][ka]
    else: H["start"][v] ^= 1
    return H
def score(G):
    T, why, lag, lagmax, double, ex, delay, F, viol = analyse(G); return (sum(delay), T)
if __name__ == "__main__":
    d, iters, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed); random.seed(seed)
    G = rand(d, rng); bs = score(G); best = (bs, G)
    for it in range(iters):
        H = mut(G, rng); hs = score(H)
        if hs >= bs:
            G, bs = H, hs
            if bs > best[0]: best = (bs, G); print("IT", it, "SUMDELAY", bs[0], "STEPS", bs[1], flush=True); json.dump(G, open(out, "w"))
        if it % 4000 == 3999 and bs < best[0]: G, bs = json.loads(json.dumps(best[1])), best[0]
    print("BEST SUMDELAY", best[0][0], "STEPS", best[0][1], flush=True)
