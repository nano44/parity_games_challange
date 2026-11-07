#!/usr/bin/env python3
"""L-SI box 64: hill-climb over ISO R197 ladders (levels 0..m) for large T_k / T_inf of the external-flip model (flipdp.py).
DATA only (lower bounds; every reported witness is re-checked by flipdp.py, which also cross-checks against L-NEW box 150).
Usage: climb.py m objective seed iters outdir     objective in {inf, k0, k1, k2, ..., inc1 (T_1 - T_0), inc2 (T_2 - T_0)}"""
import sys, os, json, random, copy
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from flipdp import analyse

def rand_iso(d, rng):  # = L-NEW box161/ext.py rand_iso (levels 0..d-1), re-typed
    N = 2 * d; lev = [v // 2 for v in range(N)]
    order = list(range(N)); rng.shuffle(order); pos = {v: i for i, v in enumerate(order)}
    opts, M = [], 0
    for x in range(N):
        o = []
        for k in range(2):
            wt = 2 * (lev[x] - 1) + k if lev[x] > 0 else -1
            later = [v for v in range(N) if pos[v] > pos[x] and lev[v] > 0]
            xt = rng.choice(later) if later and rng.random() < 0.8 else -1
            o.append([wt, xt, M]); M += 1
        opts.append(o)
    g = list(range(M)); rng.shuffle(g); it = iter(g); gate = [[next(it), next(it)] for _ in range(N)]
    br = list(range(M)); rng.shuffle(br); bp = [rng.randint(0, 1) for _ in range(M)]
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": bp, "start": [0] * N, "xorder": order}

def mutate(G, rng):
    H = copy.deepcopy(G); N = H["N"]; M = len(H["br"]); r = rng.random(); pos = {v: i for i, v in enumerate(H["xorder"])}
    if r < 0.3:
        x = rng.randrange(2, N); k = rng.randrange(2)
        later = [v for v in range(N) if pos[v] > pos[x] and H["lev"][v] > 0]
        H["opts"][x][k][1] = rng.choice(later + [-1]) if later else -1
    elif r < 0.5:
        i, j = rng.randrange(M), rng.randrange(M); H["br"][i], H["br"][j] = H["br"][j], H["br"][i]
    elif r < 0.6:
        i = rng.randrange(M); H["bp"][i] ^= 1
    elif r < 0.85:
        a, b = (rng.randrange(N), rng.randrange(2)), (rng.randrange(N), rng.randrange(2))
        H["gate"][a[0]][a[1]], H["gate"][b[0]][b[1]] = H["gate"][b[0]][b[1]], H["gate"][a[0]][a[1]]
    else:  # move a mover in the topological order (keep Xi-targets consistent: drop targets that become invalid)
        o = H["xorder"]; i, j = rng.randrange(N), rng.randrange(N); v = o.pop(i); o.insert(j, v)
        pos = {v: i for i, v in enumerate(o)}
        for x in range(N):
            for k in range(2):
                t = H["opts"][x][k][1]
                if t >= 0 and pos[t] < pos[x]: H["opts"][x][k][1] = -1
    return H

def score(G, obj):
    try: r = analyse(G, K=2 if obj in ("inf",) else int(obj[-1]) if obj[-1].isdigit() else 2, check=False)
    except AssertionError: return None, None
    T = r["T"]
    if obj == "inf": return (r["Tinf"], T[0]), r
    if obj.startswith("k"): return (T[int(obj[1:])], -T[0]), r
    if obj.startswith("inc"): k = int(obj[3:]); return (T[k] - T[0], T[k]), r
    raise SystemExit("objective")

if __name__ == "__main__":
    m, obj, seed, iters, out = int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    rng = random.Random(seed); os.makedirs(out, exist_ok=True)
    best, bs = None, None
    while best is None:
        G = rand_iso(m + 1, rng); s, _ = score(G, obj)
        if s is not None: best, bs = G, s
    restarts = 0; cur, cs = best, bs; stale = 0
    for it in range(iters):
        H = mutate(cur, rng); s, r = score(H, obj)
        if s is None: continue
        if s >= cs:
            if s > cs: stale = 0
            cur, cs = H, s
        else: stale += 1
        if cs > bs:
            best, bs = cur, cs
            json.dump(best, open(os.path.join(out, "%s_m%d_s%d.json" % (obj, m, seed)), "w"))
            print("it", it, "best", bs, "T", r["T"], "Tinf", r["Tinf"], "LP", r["LP"], flush=True)
        if stale > 3000:
            G = rand_iso(m + 1, rng); s, _ = score(G, obj)
            if s is not None: cur, cs = G, s; stale = 0; restarts += 1
    print("FINAL", obj, "m", m, "seed", seed, "best", bs, "restarts", restarts)
