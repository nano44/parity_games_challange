#!/usr/bin/env python3
"""L-RED R171: hill-climb for many S4c fallbacks inside ONE TWO-FIX window (score = (max FB over windows, its L)). Seeded from a game +
start (SEED_PG / SEED_START), or random (climb170's generator with KO Odd choice vertices). Mutations as climb170 (n fixed).
Usage: climb171.py SEED ITERS OUT_PREFIX [SEED_PG SEED_START|-]   (random seed game: env N, KO)
Prints improvements and a BEST line; writes OUT_PREFIX.pg / .start."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "r170"))
from fbscore import windows_fb
from climb170 import rand_game, mutate, write
from n5x import load, readstart, start_pair, Engine, dual
import pg

def score(G):
    g = pg.Game(G["prio"], G["own"], G["succ"])
    try: W, K = windows_fb(g, G["s"], G["t"], cap=3000)
    except Exception: return (-1, 0), None
    if not W: return (0, 0), None
    w = max(W, key=lambda w: (w["FB"], w["L"])); return (w["FB"], w["L"]), w

def load_genome(p, sp):
    g = load(p); st = readstart(sp) if sp != "-" else None
    s, t = start_pair(g, Engine(g), Engine(dual(g)), st)
    return {"prio": list(g.prio), "own": list(g.owner), "succ": [sorted(set(x)) for x in g.succ],
            "ch": [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1],
            "s": [s[v] if g.owner[v] == 0 else -1 for v in range(g.n)], "t": [t[v] if g.owner[v] == 1 else -1 for v in range(g.n)]}

def main():
    seed, iters, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]; rng = random.Random(seed)
    if len(sys.argv) > 5: G = load_genome(sys.argv[4], sys.argv[5])
    else: n = int(os.environ.get("N", "24")); G = rand_game(n, int(os.environ.get("KO", "1")), n // 6, rng)
    sc, w = score(G); print(f"start FB {sc[0]} L {sc[1]} {w}", flush=True)
    for i in range(iters):
        H = mutate(G, rng)
        if H is None: continue
        H["ch"] = [v for v in range(len(H["prio"])) if H["own"][v] == 1 and len(H["succ"][v]) > 1]
        s2, w2 = score(H)
        if s2 >= sc:
            if s2 > sc: print(f"it {i} FB {s2[0]} L {s2[1]} {w2}", flush=True)
            G, sc, w = H, s2, w2
    write(G, out); print(f"BEST n {len(G['prio'])} FB {sc[0]} L {sc[1]} {w}")

if __name__ == "__main__":
    main()
