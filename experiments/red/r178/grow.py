#!/usr/bin/env python3
"""L-RED R178 GROW: grow a fastabs genome one level at a time (TOP or BOTTOM), keeping the old genome, then climb the whole thing
from there. Usage: grow.py start.json levels_to_add iters mode(top|bottom) seed outprefix"""
import sys, os, json, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r177"))
import fastabs as F

def extend(G, rng, mode):
    H = json.loads(json.dumps(G)); N = H["N"]; deg = H["deg"]; W = sum(1 for l in H["lev"] if l == 0)
    new = list(range(N, N + W)); M = len(H["br"])
    if mode == "top":
        top = max(H["lev"]); H["lev"] += [top + 1] * W; below = [u for u in range(N) if H["lev"][u] == top]
        wts = lambda: rng.choice(below)
    else:
        H["lev"] = [l + 1 for l in H["lev"]] + [0] * W
        for v in range(N):
            if H["lev"][v] == 1:
                for o in H["opts"][v]: o[0] = rng.choice(new)
        wts = lambda: -1
    # xorder: insert new vertices at random positions; their Xi-targets must be later
    xo = H["xorder"]
    for v in new: xo.insert(rng.randrange(len(xo) + 1), v)
    pos = {u: i for i, u in enumerate(xo)}
    b = M
    for v in new:
        o = []
        for k in range(deg):
            later = [u for u in range(N + W) if pos[u] > pos[v]]
            o.append([wts(), rng.choice(later + [-1]) if later else -1, b]); b += 1
        H["opts"].append(o)
    # new betas: random ranks inserted among old ones
    nb = b - M; ranks = H["br"] + [None] * nb; allr = list(range(b))
    newr = rng.sample(allr, nb); old = [r for r in allr if r not in newr]
    H["br"] = [old[r] for r in H["br"]] + newr; H["bp"] += [rng.randint(0, 1) for _ in range(nb)]
    gmax = N * deg; H["gate"] += [[gmax + v2 * deg + k for k in range(deg)] for v2 in range(W)]
    # spread gate indices: random relabel preserving nothing in particular for new ones
    allg = [g for gs in H["gate"] for g in gs]; perm = sorted(range(len(allg)), key=lambda i: allg[i] + (rng.random() * gmax if allg[i] >= gmax else 0))
    H["start"] += [rng.randrange(deg) for _ in range(W)]; H["N"] = N + W
    # keep old xt constraints valid
    for u in range(N + W):
        for o in H["opts"][u]:
            if o[1] >= 0 and pos[o[1]] <= pos[u]: o[1] = -1
    return H

if __name__ == "__main__":
    G = json.load(open(sys.argv[1])); L, iters, mode, seed, outp = int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], int(sys.argv[5]), sys.argv[6]
    rng = random.Random(seed); print("START N", G["N"], "steps", F.simulate(G)[0], flush=True)
    for l in range(L):
        best, bs = None, -1
        for tr in range(8):
            H = extend(G, rng, mode); hs = F.simulate(H)[0]
            if hs > bs: best, bs = H, hs
        G = best
        for it in range(iters):
            H = F.mutate(G, rng); hs = F.simulate(H)[0]
            if hs >= bs: G, bs = H, hs
        json.dump(G, open(f"{outp}_N{G['N']}.json", "w")); print("LEVEL", l + 1, "N", G["N"], "steps", bs, flush=True)
