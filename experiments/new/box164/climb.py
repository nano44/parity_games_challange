#!/usr/bin/env python3
"""L-NEW box 164: hill-climb on R197 2-wide ladders (ISO) for long real IDEAL runs / high record multiplicity.
Score = (mult, T) with mult = max multiplicity of the record kind (A or V, see rec.py). Usage: climb.py d kind iters restarts seed"""
import os, sys, json, random, copy
H = os.path.dirname(os.path.abspath(__file__)); sys.argv0 = sys.argv[:]
exec(open(os.path.join(H, "rec.py")).read().split("\nif __name__")[0])

def mutate(G, rng, iso=True):
    G = copy.deepcopy(G); N = G["N"]; M = sum(len(o) for o in G["opts"]); r = rng.random()
    if r < 0.25: i, j = rng.sample(range(M), 2); G["br"][i], G["br"][j] = G["br"][j], G["br"][i]
    elif r < 0.4: i = rng.randrange(M); G["bp"][i] ^= 1
    elif r < 0.55:
        a, b = rng.randrange(N), rng.randrange(N); ka, kb = rng.randrange(2), rng.randrange(2)
        G["gate"][a][ka], G["gate"][b][kb] = G["gate"][b][kb], G["gate"][a][ka]
    elif r < 0.65: i = rng.randrange(N); G["start"][i] ^= 1
    else:
        pos = {v: i for i, v in enumerate(G["xorder"])}; x = rng.randrange(N); k = rng.randrange(2)
        later = [v for v in range(N) if pos[v] > pos[x] and (G["lev"][v] > 0 or not iso)]
        G["opts"][x][k][1] = rng.choice(later + [-1]) if later else -1
        if rng.random() < 0.1:
            i, j = rng.sample(range(N), 2); o = G["xorder"]; 
            G2 = copy.deepcopy(G); o2 = G2["xorder"]; o2[i], o2[j] = o2[j], o2[i]
            p2 = {v: i for i, v in enumerate(o2)}
            if all(oo[1] < 0 or p2[oo[1]] > p2[v] for v in range(N) for oo in G2["opts"][v]): G = G2
    return G

def score(G, kind):
    try: r = records(G)
    except RuntimeError: return (-1, -1), None
    return (r["mult" + kind], r["T"]), r

if __name__ == "__main__":
    d, kind, iters, restarts, seed = int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    rng = random.Random(seed); best = ((0, 0), None)
    for rs in range(restarts):
        G = rand_lr(d, rng, iso=True); s, r = score(G, kind)
        for it in range(iters):
            G2 = mutate(G, rng); s2, r2 = score(G2, kind)
            if s2 >= s: G, s, r = G2, s2, r2
        if s > best[0]:
            best = (s, G); json.dump(G, open(os.path.join(H, "out", "climb_%s_d%d_m%d_T%d.json" % (kind, d, s[0], s[1])), "w"))
        print("restart %d score mult %d T %d  best mult %d T %d" % (rs, s[0], s[1], best[0][0], best[0][1]), flush=True)
