#!/usr/bin/env python3
"""L-NEW box 64: hill-climb for a ONE-PLAYER game (every Odd vertex has out-degree 1, so tau never changes and
N5 = switch-best, RESULTS R17 (e)) on which N5 makes >= n + m iterations from a chosen sigma_0. Such a game kills
CONJECTURE FRAME-STRETCH (whole run is one tau-stretch). Engine: box21/n5x.trace (plain N5).
Usage: climb1p.py N SEED ITERS [OUT.pg]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import trace
import pg

def score(G, s0):
    st, _ = trace(G, start=(s0, {}), check=False)
    return len(st) - 1

def build(prio, owner, succ): return pg.Game(prio, owner, succ)

def rand_game(rng, n):
    prio = rng.sample(range(n * 2), n)
    owner = [0 if rng.random() < 0.6 else 1 for _ in range(n)]
    succ = [sorted(set(rng.sample(range(n), 1 if owner[v] else rng.choice([2, 2, 3])))) for v in range(n)]
    return prio, owner, succ

def mutate(rng, n, prio, owner, succ):
    prio, owner, succ = list(prio), list(owner), [list(s) for s in succ]
    k = rng.randrange(4); v = rng.randrange(n)
    if k == 0:
        u = rng.randrange(n); prio[v], prio[u] = prio[u], prio[v]
    elif k == 1:
        free = [p for p in range(2 * n + 2) if p not in prio]; prio[v] = rng.choice(free)
    elif k == 2:
        if owner[v] == 1: succ[v] = [rng.randrange(n)]
        else:
            s = set(succ[v]); s.discard(rng.choice(succ[v])) if len(s) > 1 and rng.random() < 0.4 else s.add(rng.randrange(n))
            succ[v] = sorted(s)
    else:
        owner[v] = 1 - owner[v]
        if owner[v] == 1: succ[v] = [rng.choice(succ[v])]
    return prio, owner, succ

def main():
    n, seed, iters = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    rng = random.Random(seed)
    cur = rand_game(rng, n); s0 = {}
    def val(c, s0):
        G = build(*c)
        s0 = {v: w for v, w in s0.items() if G.owner[v] == 0 and w in G.succ[v]}
        return score(G, s0) / (G.n + G.m), G, s0
    best, G, s0 = val(cur, s0)
    for it in range(iters):
        cand = mutate(rng, n, *cur); ns0 = dict(s0)
        if rng.random() < 0.3:
            v = rng.randrange(n)
            if cand[1][v] == 0: ns0[v] = rng.choice(cand[2][v])
        r, H, ns0 = val(cand, ns0)
        if r >= best:
            cur, best, G, s0 = cand, r, H, ns0
    it = score(G, s0)
    print(f"n {G.n} m {G.m} iters {it} ratio {best:.3f} start {s0}")
    if len(sys.argv) > 4:
        with open(sys.argv[4], "w") as f:
            f.write(f"parity {G.n - 1};\n")
            for v in range(G.n): f.write(f"{v} {G.prio[v]} {G.owner[v]} {','.join(map(str, G.succ[v]))};\n")
        with open(sys.argv[4] + ".start", "w") as f:
            f.write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in sorted(s0.items())) + "\nTAU0\n")

main()
