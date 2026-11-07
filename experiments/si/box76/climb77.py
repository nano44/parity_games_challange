#!/usr/bin/env python3
"""L-SI box 77: hill climb from a seed genome toward a tower of consecutive doubling levels (F(l) = 2F(l-1) + 2 for l = 1..h).
Moves: re-target the Xi-target of one option (a mover or X; Xi-acyclicity kept), swap two beta ranks, swap two gates, flip a parity,
flip one start bit. Score: (h = number of consecutive doubling levels from level 1, F(h+1), T). Deterministic for a seed.
Usage: climb77.py SEED.json SEED_INT ITERS OUT.json"""
import sys, os, json, random, copy
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
from tw import Sim, analyse, is_lr
def acyclic(G):
    N = G["N"]; col = [0] * N
    def dfs(v):
        col[v] = 1
        for k in range(2):
            u = G["opts"][v][k][1]
            if u >= 0:
                if col[u] == 1 or (col[u] == 0 and not dfs(u)): return False
        col[v] = 2; return True
    return all(col[v] or dfs(v) for v in range(N))
def score(G):
    try:
        S = Sim(G).run(tuple(G["start"]), cap=5000)
    except RuntimeError:
        return None
    sim = Sim(G); a = analyse(sim, S); T = a["T"]; d = G["N"] // 2
    F = [sum(1 for t in range(1, T + 1) if a["flip"][t][j]) for j in range(d)]
    h = 0
    while h + 1 < d and F[h + 1] == 2 * F[h] + 2: h += 1
    nxt = F[h + 1] if h + 1 < d else 0
    return (h, nxt, T), F
def main():
    G = json.load(open(sys.argv[1])); rnd = random.Random(int(sys.argv[2])); iters = int(sys.argv[3]); out = sys.argv[4]
    N = G["N"]; best, F = score(G); print("seed", best, F, flush=True)
    for it in range(iters):
        H2 = copy.deepcopy(G); r = rnd.random()
        if r < 0.4:
            x = rnd.randrange(N); k = rnd.randrange(2); H2["opts"][x][k][1] = rnd.choice([-1] + [y for y in range(N) if y != x])
            if not acyclic(H2): continue
        elif r < 0.6:
            i, j = rnd.sample(range(len(H2["br"])), 2); H2["br"][i], H2["br"][j] = H2["br"][j], H2["br"][i]
        elif r < 0.75:
            x, y = rnd.randrange(N), rnd.randrange(N); k, l = rnd.randrange(2), rnd.randrange(2)
            H2["gate"][x][k], H2["gate"][y][l] = H2["gate"][y][l], H2["gate"][x][k]
        elif r < 0.9:
            i = rnd.randrange(len(H2["bp"])); H2["bp"][i] ^= 1
        else:
            x = rnd.randrange(N); H2["start"][x] ^= 1
        sc = score(H2)
        if sc is None: continue
        if sc[0] >= best:
            if sc[0] > best: print("it", it, sc[0], sc[1], flush=True)
            G, best = H2, sc[0]
    json.dump(G, open(out, "w")); print("final", best, score(G)[1])
if __name__ == "__main__":
    main()
