#!/usr/bin/env python3
"""REFEREE adversarial climb against Lemma CASC / Theorem U1 (P-N5-U1). Fitness = max over W-flat switches in route-form pieces of
(run step - level + 2) (CASC violated iff > 0), then total W-flat switches, then max R-changing transitions of a U1 piece minus |R|.
Mutations keep C^1O (assert in u1_probe.run). Every candidate is fully checked by u1_probe (any *_FAIL counter is printed and saved).
Usage: casc_climb.py seed.pg steps rngseed outdir"""
import sys, os, random, copy
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u1_probe as U, pg

class Rec(Counter): pass

def fitness(g):
    c = Counter(); margin = [-99]
    orig = U.piece
    def piece(g_, E, o, J, R, cnt, name):
        T = len(J) - 1; Rl = [v for v in R if v != o]
        flat = [not J[i]["fb"] and all(J[i]["W"][v] == J[i + 1]["W"][v] for v in R) for i in range(T)]
        i = 0
        while i < T:
            if not flat[i]: i += 1; continue
            j = i
            while j < T and flat[j]: j += 1
            for st in range(i, j):
                for v in Rl:
                    if g_.owner[v] == 0 and J[st]["s"][v] != J[st + 1]["s"][v]:
                        lv = len(U.play_to(J[st]["nx"], v, o)); margin[0] = max(margin[0], (st - i) - lv + 2)
            i = j
        orig(g_, E, o, J, R, cnt, name)
    U.piece = piece
    try: U.run(g, c)
    finally: U.piece = orig
    return (margin[0], c["CASC_switches"], c["U1_max_changes"]), c

def mutate(g, rng):
    h = pg.Game(list(g.prio), list(g.owner), [list(s) for s in g.succ]); n = h.n
    o = [v for v in range(n) if h.owner[v] == 1 and len(set(h.succ[v])) > 1][0]
    r = rng.random()
    if r < 0.5:
        v = rng.randrange(n); 
        if h.owner[v] == 1 and v != o: h.succ[v] = [rng.randrange(n)]
        else:
            s = h.succ[v]; s[rng.randrange(len(s))] = rng.randrange(n); h.succ[v] = sorted(set(s))
            if v == o and len(h.succ[v]) < 2: return None
    elif r < 0.8:
        a, b = rng.randrange(n), rng.randrange(n); h.prio[a], h.prio[b] = h.prio[b], h.prio[a]
    else:
        v = rng.randrange(n)
        if h.owner[v] == 0 and len(h.succ[v]) < 4: h.succ[v] = sorted(set(h.succ[v] + [rng.randrange(n)]))
        else: return None
    return h

if __name__ == "__main__":
    seedf, steps, rs, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    os.makedirs(out, exist_ok=True); rng = random.Random(rs); g = U.load(seedf); best, c = fitness(g); allc = Counter()
    print("seed", best, flush=True)
    for it in range(steps):
        h = mutate(g, rng)
        if h is None: continue
        try: f, c = fitness(h)
        except AssertionError: continue
        allc["cands"] += 1; allc.update({k: v for k, v in c.items() if "FAIL" in k})
        if any("FAIL" in k for k in c):
            p = os.path.join(out, "fail_%d.pg" % it); pg.write(h, p); print("FAIL", it, c, flush=True)
        if f >= best:
            if f > best: print(it, f, flush=True)
            best, g = f, h
    print("final", best, dict(allc), flush=True)
    with open(os.path.join(out, "best.pg"), "w") as fh:
        fh.write("parity %d;\n" % (g.n - 1))
        for v in range(g.n): fh.write("%d %d %d %s;\n" % (v, g.prio[v], g.owner[v], ",".join(map(str, g.succ[v]))))
