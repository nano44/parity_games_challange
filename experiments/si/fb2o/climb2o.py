#!/usr/bin/env python3
"""L-SI box 16: hill-climb on games with exactly two Odd choice vertices, maximising the most in-phase fallbacks of one phase of N5
(ties: more states in that phase). Mutations: redirect one edge, add / drop an edge (Odd non-choice vertices keep one successor, the two
Odd choice vertices keep >= 2), change one priority. Writes the best game to instances/. DATA tool.
Usage: climb2o.py SEED STEPS N [START.pg]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import fb2o, pg

def score(g):
    E, rows = fb2o.trace(g, cap=600)
    best, a = (0, 0), 0
    for k in range(1, len(rows) + 1):
        if k == len(rows) or (rows[k]["lam"], rows[k]["t"]) != (rows[a]["lam"], rows[a]["t"]):
            f = sum(rows[i]["fb"] for i in range(a, k - 1)); best = max(best, (f, k - a)); a = k
    return best

OBJ = os.environ.get("OBJ", "f")   # f: most fallbacks in one phase; hyp: DIR + SAT hypothesis hits (fb2o counters), then f

def score_hyp(g):
    for k in fb2o.C: fb2o.C[k] = 0
    fb2o.VIOL.clear(); fb2o.check(g, "climb")
    if fb2o.VIOL: raise SystemExit(f"VIOLATION during climb: {fb2o.VIOL[:3]}")
    return (fb2o.C["DIR_n"] + fb2o.C["SAT_n"], fb2o.C["FMAX"])

def k2(g): return sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) == 2

def mutate(rng, g):
    prio, owner, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]
    n = g.n; v = rng.randrange(n); r = rng.random()
    if r < 0.25: prio[v] = rng.randrange(n + 3)
    elif r < 0.6: succ[v][rng.randrange(len(succ[v]))] = rng.randrange(n)
    elif r < 0.8: succ[v].append(rng.randrange(n))
    elif len(succ[v]) > 1: succ[v].pop(rng.randrange(len(succ[v])))
    succ = [sorted(set(s)) for s in succ]
    h = pg.Game(prio, owner, succ)
    return h if k2(h) else None

def main():
    seed, steps, n = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed)
    g = fb2o.load(sys.argv[4]) if len(sys.argv) > 4 else fb2o.randgame(rng, n, n, 2)
    sc_f = score_hyp if OBJ == "hyp" else score
    sc = sc_f(g)
    for i in range(steps):
        h = mutate(rng, g)
        if h is None: continue
        s2 = sc_f(h)
        if s2 >= sc: g, sc = h, s2
    os.makedirs(os.path.join(HERE, "instances"), exist_ok=True)
    out = os.path.join(HERE, "instances", f"climb_s{seed}_n{g.n}_{OBJ}{sc[0]}.pg")
    with open(out, "w") as f:
        f.write(f"parity {g.n - 1};\n")
        for v in range(g.n): f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")
    print(f"seed {seed} n {g.n}: best ({OBJ} objective) = {sc} -> {out}")

if __name__ == "__main__":
    main()
