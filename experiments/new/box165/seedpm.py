#!/usr/bin/env python3
"""climb from a seed genome (any degree, any widths) to kill CONJECTURE PM: objective (excess, moves of the argmax mover, T),
excess = max_x moves(x) - (deg(x)-1)(1+desc(x)). Mutations keep the degrees, levels and acyclicity (topological order computed if
absent). Usage: seedpm.py seed.json iters seed"""
import os, sys, json, random, copy
H = os.path.dirname(os.path.abspath(__file__)); exec(open(os.path.join(H, "permover.py")).read().split("\nif __name__")[0])

def topo(G):
    N = G["N"]; R = reach(G); return sorted(range(N), key=lambda x: -len(R[x]))  # descendants have fewer descendants: valid topo order

def mutate(G, rng):
    G = copy.deepcopy(G); N = G["N"]; opts = G["opts"]; allo = [(x, k) for x in range(N) for k in range(len(opts[x]))]; r = rng.random()
    if r < 0.25:
        (a, i), (b, j) = rng.sample(allo, 2); ma, mb = opts[a][i][2], opts[b][j][2]; G["br"][ma], G["br"][mb] = G["br"][mb], G["br"][ma]
    elif r < 0.37: x, k = rng.choice(allo); G["bp"][opts[x][k][2]] ^= 1
    elif r < 0.52:
        (a, i), (b, j) = rng.sample(allo, 2); G["gate"][a][i], G["gate"][b][j] = G["gate"][b][j], G["gate"][a][i]
    elif r < 0.6: x = rng.randrange(N); G["start"][x] = rng.randrange(len(opts[x]))
    elif r < 0.7:
        x, k = rng.choice(allo); l = G["lev"][x]
        if l > 0: opts[x][k][0] = rng.choice([v for v in range(N) if G["lev"][v] == l - 1])
    else:
        pos = {v: i for i, v in enumerate(G["xorder"])}; x, k = rng.choice(allo)
        later = [v for v in range(N) if pos[v] > pos[x]]; opts[x][k][1] = rng.choice(later + [-1]) if later else -1
    return G

def score(G):
    try: r = measure(G)
    except RuntimeError: return (-99, 0, 0)
    ex = [r["mv"][x] - (len(G["opts"][x]) - 1) * (1 + r["desc"][x]) for x in range(G["N"])]; m = max(ex)
    return (m, max(r["mv"][x] for x in range(G["N"]) if ex[x] == m), r["T"])

if __name__ == "__main__":
    f, iters, seed = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); G = json.load(open(f))
    G["xorder"] = topo(G); s = score(G); best = s; print("seed", os.path.basename(f), s, flush=True)
    for it in range(iters):
        G2 = mutate(G, rng); s2 = score(G2)
        if s2 >= s:
            G, s = G2, s2
            if s > best:
                best = s; print("it", it, s, flush=True)
                json.dump(G, open(os.path.join(H, "out", "seedpm_%s_s%d.json" % (os.path.basename(f)[:-5], seed)), "w"))
                if s[0] > 0: print("KILL", flush=True); json.dump(G, open(os.path.join(H, "out", "KILL_PM_%s_s%d.json" % (os.path.basename(f)[:-5], seed)), "w")); break
    print("FINAL", best)
