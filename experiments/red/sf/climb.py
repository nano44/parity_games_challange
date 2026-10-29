#!/usr/bin/env python3
"""L-RED: hill-climb (random restarts + single mutations) over parity games of n vertices maximising N5-SF's objective
(OBJ=sbc: SBC_sigma + SBC_tau; OBJ=it: iterations) from the SPEC S3 start, engine sf2.py. Mutations: re-target an edge, add/remove
an edge (out-degree 1..D), swap two priorities, flip an owner. Ties accepted (plateau walk). Writes the best game to OUT.pg after each
improvement. Usage: climb.py n D SEED STEPS OUT.pg"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sf2, pg, n5b
OBJ = os.environ.get("OBJ", "sbc")


def score(g):
    s = sf2.SF(g, mode="spec"); rec = []
    try:
        s.run_sf(rec=rec, max_iter=5000)
    except Exception:
        return -1, None
    sc, sbc, tc, tbc, lam = sf2.stats(rec)
    return (sbc + tbc if OBJ == "sbc" else len(rec) - 1), (len(rec) - 1, sbc, tbc)


def rand_game(n, D, R):
    prio = list(range(n)); R.shuffle(prio)
    own = [R.randint(0, 1) for _ in range(n)]
    succ = [sorted(set(R.sample(range(n), R.randint(1, D)))) for _ in range(n)]
    return pg.Game(prio, own, succ)


def mutate(g, D, R):
    n = g.n; prio, own, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]
    k = R.randint(0, 3); v = R.randrange(n)
    if k == 0:
        i = R.randrange(len(succ[v])); succ[v][i] = R.randrange(n)
    elif k == 1:
        if len(succ[v]) < D: succ[v].append(R.randrange(n))
        elif len(succ[v]) > 1: succ[v].pop(R.randrange(len(succ[v])))
    elif k == 2:
        w = R.randrange(n); prio[v], prio[w] = prio[w], prio[v]
    else:
        own[v] = 1 - own[v]
    return pg.Game(prio, own, [sorted(set(s)) for s in succ])


def write(g, path):
    with open(path, "w") as f:
        f.write(f"parity {g.n - 1};\n")
        for v in range(g.n): f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")


if __name__ == "__main__":
    n, D, seed, steps, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    R = random.Random(seed); g = rand_game(n, D, R); best, info = score(g)
    for t in range(steps):
        h = mutate(g, D, R); s, inf = score(h)
        if s >= best:
            if s > best:
                write(h, out); print(f"step {t} obj {s} (it, SBC_s, SBC_t) {inf}", flush=True)
            g, best, info = h, s, inf
    print("final", best, info)
