#!/usr/bin/env python3
"""L-NEW box 165: hill-climb degree-2 IDEAL-ACYC genomes (levels 0..d-1, width w per level, W-targets any mover one level down,
Xi-targets any later mover in a hidden topological order, arbitrary ranks/parities/gates/start) to maximize
excess := max_x (moves(x) - (deg(x)-1)(1 + desc(x))), tie-break T. CONJECTURE PM (per-mover): excess <= 0. Prints KILL if excess > 0.
Usage: kill1.py d w iters restarts seed [LR]   (LR: R197 ladder W-targets, w = 2)"""
import os, sys, json, random, copy
H = os.path.dirname(os.path.abspath(__file__)); exec(open(os.path.join(H, "permover.py")).read().split("\nif __name__")[0])

def gen(d, w, rng, lr):
    N = d * w; lev = [v // w for v in range(N)]; order = list(range(N)); rng.shuffle(order); opts = []; M = 0
    for x in range(N):
        o = []
        for k in range(2):
            if lev[x] == 0: wt = -1
            elif lr: wt = w * (lev[x] - 1) + k
            else: wt = rng.randrange(w * (lev[x] - 1), w * lev[x])
            o.append([wt, -1, M]); M += 1
        opts.append(o)
    G = {"N": N, "lev": lev, "opts": opts, "gate": None, "br": list(range(M)), "bp": [rng.randint(0, 1) for _ in range(M)],
         "start": [rng.randint(0, 1) for _ in range(N)], "xorder": order, "deg": [2] * N}
    g = list(range(M)); rng.shuffle(g); G["gate"] = [[g[2 * x], g[2 * x + 1]] for x in range(N)]; rng.shuffle(G["br"])
    for x in range(N):
        for k in range(2): G["opts"][x][k][1] = pick(G, x, rng)
    return G

def pick(G, x, rng):
    pos = {v: i for i, v in enumerate(G["xorder"])}; later = [v for v in range(G["N"]) if pos[v] > pos[x]]
    return rng.choice(later) if later and rng.random() < 0.85 else -1

def mutate(G, rng, lr):
    G = copy.deepcopy(G); N = G["N"]; M = 2 * N; r = rng.random()
    if r < 0.25: i, j = rng.sample(range(M), 2); G["br"][i], G["br"][j] = G["br"][j], G["br"][i]
    elif r < 0.37: G["bp"][rng.randrange(M)] ^= 1
    elif r < 0.52:
        a, b = rng.randrange(N), rng.randrange(N); ka, kb = rng.randrange(2), rng.randrange(2)
        G["gate"][a][ka], G["gate"][b][kb] = G["gate"][b][kb], G["gate"][a][ka]
    elif r < 0.6: G["start"][rng.randrange(N)] ^= 1
    elif r < 0.68 and not lr:
        x = rng.randrange(N); l = G["lev"][x]
        if l > 0:
            w = sum(1 for v in range(N) if G["lev"][v] == 0); G["opts"][x][rng.randrange(2)][0] = rng.randrange(w * (l - 1), w * l)
    else:
        x = rng.randrange(N); G["opts"][x][rng.randrange(2)][1] = pick(G, x, rng)
    return G

def score(G):
    try: r = measure(G)
    except RuntimeError: return (-99, 0)
    return (max(r["mv"][x] - (len(G["opts"][x]) - 1) * (1 + r["desc"][x]) for x in range(G["N"])), r["T"])

if __name__ == "__main__":
    d, w, iters, restarts, seed = map(int, sys.argv[1:6]); lr = len(sys.argv) > 6; rng = random.Random(seed); best = None
    for rs in range(restarts):
        G = gen(d, w, rng, lr); s = score(G)
        for it in range(iters):
            G2 = mutate(G, rng, lr); s2 = score(G2)
            if s2 >= s:
                G, s = G2, s2
                if s[0] > 0:
                    json.dump(G, open(os.path.join(H, "out", "KILL_PM_d%d_w%d_s%d.json" % (d, w, seed)), "w")); print("KILL", s, flush=True); break
        if best is None or s > best: best = s; json.dump(G, open(os.path.join(H, "out", "pm_d%d_w%d_s%d.json" % (d, w, seed)), "w"))
        print("restart %d (excess, T) %s best %s" % (rs, s, best), flush=True)
        if s[0] > 0: break
