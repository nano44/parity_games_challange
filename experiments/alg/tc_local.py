#!/usr/bin/env python3
"""Local search around the Two Counters game for DTL (Oink dtl) tangle growth: start from tc N (Oink generator), mutate
(add/remove edge, change priority by +-1/+-2, flip owner, split an edge with a new vertex of low priority), accept when the
dtl tangle count does not drop (and with prob 0.05 anyway); keep the best per size. Fitness: oink_fit.work(g, 'dtl').
Usage: tc_local.py N STEPS SEED [--nmax 90] [--solver dtl]"""
import sys, os, json, random, subprocess, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, oink_fit, alglib, zielonka
O = os.path.join(HERE, "..", "..", "tools", "oink", "build")


def mutate(g, rnd, nmax):
    prio, owner, succ = list(g.prio), list(g.owner), [sorted(set(s)) for s in g.succ]
    n = len(prio); r = rnd.random()
    if r < 0.25:
        v, w = rnd.randrange(n), rnd.randrange(n)
        if w not in succ[v]: succ[v] = sorted(succ[v] + [w])
    elif r < 0.45:
        v = rnd.randrange(n)
        if len(succ[v]) > 1: succ[v].remove(rnd.choice(succ[v]))
    elif r < 0.7:
        v = rnd.randrange(n); prio[v] = max(0, prio[v] + rnd.choice([-2, -1, 1, 2]))
    elif r < 0.8:
        v = rnd.randrange(n); owner[v] ^= 1
    elif n < nmax:                      # split an edge v->w with a new vertex x (low priority, owner random)
        v = rnd.randrange(n); w = rnd.choice(succ[v])
        prio.append(rnd.choice([0, 1, 2])); owner.append(rnd.randrange(2)); succ.append([w])
        succ[v] = sorted((set(succ[v]) - {w}) | {n})
    return pg.Game(prio, owner, succ)


def main():
    N, steps, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    opt = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
    nmax = int(opt("--nmax", 90)); solver = opt("--solver", "dtl")
    rnd = random.Random(seed)
    g = pg.parse(subprocess.run([f"{O}/tc", str(N)], capture_output=True, text=True).stdout)
    fit = lambda h: oink_fit.work(h, solver, raw=True, timeout=30)
    sc = fit(g); best = (sc, g); t0 = time.time()
    print(f"tc {N}: n={g.n} {solver} work {sc}", flush=True)
    for step in range(steps):
        h = mutate(g, rnd, nmax); sh = fit(h)
        if sh < 0: continue
        if sh >= sc or rnd.random() < 0.05:
            g, sc = h, sh
            if sc > best[0]:
                best = (sc, g); print(f"  step {step}: {solver} work {sc} (n={g.n}, m={g.m})", flush=True)
                pg.write(g, os.path.join(HERE, "out", f"tc_local_{solver}_N{N}_s{seed}_best.pg"))
        if step % 2000 == 0:
            print(f"  step {step}, {time.time()-t0:.0f}s, current {sc}, best {best[0]}", flush=True)
    print(f"done: best {solver} work {best[0]} at n={best[1].n}")


if __name__ == "__main__":
    main()
