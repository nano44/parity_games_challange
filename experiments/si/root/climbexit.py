#!/usr/bin/env python3
"""L-SI box 22 (successor 18): hill-climb for growth of EXIT_x at FIXED k (docs/si/N5-EXIT-box22.md). Score (lexicographic):
(max EXIT_x over phases, classes and x; EXIT_sum; longest phase), from exitx.py's counters. The game keeps exactly K Odd choice vertices
(Odd vertices with >= 2 distinct successors) and its size n. Mutations as climbmig.py (one priority, redirect / add / drop one edge).
Start: a random C^kO game of size n (new/box43 multi.rand_ckO) or a given game. DATA tool.
Usage: climbexit.py SEED STEPS N K [START.pg [START.start]]. Writes the best game (and its start, N5's default) to root/instances/."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
import exitx
from common import load, readstart
import pg

def score(g, start=None):
    exitx.C.clear(); exitx.LINES.clear(); exitx.VIOL.clear()
    try: exitx.run(g, "climb", start)
    except Exception: return None
    if exitx.VIOL: print("VIOLATION in climb:", exitx.VIOL[:3]); write(g, "viol"); sys.exit(2)
    C = exitx.C
    return (C["EXIT_max"], C["EXIT_sum"], C["len_max"])

def kq(g): return sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2)

def mutate(rng, g, k):
    prio, owner, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]
    n = g.n; v = rng.randrange(n); r = rng.random()
    if r < 0.25: prio[v] = rng.randrange(2 * n + 3)
    elif r < 0.6: succ[v][rng.randrange(len(succ[v]))] = rng.randrange(n)
    elif r < 0.8: succ[v].append(rng.randrange(n))
    elif len(succ[v]) > 1: succ[v].pop(rng.randrange(len(succ[v])))
    if len(set(prio)) < n: return None                     # SPEC S1: rewards injective
    h = pg.Game(prio, owner, [sorted(set(s)) for s in succ])
    return h if kq(h) == k else None

def write(g, tag):
    os.makedirs(os.path.join(HERE, "instances"), exist_ok=True)
    out = os.path.join(HERE, "instances", f"exit_{tag}.pg")
    with open(out, "w") as f:
        f.write(f"parity {g.n - 1};\n")
        for v in range(g.n): f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")
    return out

def main():
    seed, steps, n, k = map(int, sys.argv[1:5]); rng = random.Random(seed)
    if len(sys.argv) > 5: g = load(sys.argv[5]); st = readstart(sys.argv[6]) if len(sys.argv) > 6 else None
    else:
        sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box43")); from multi import rand_ckO
        g = None
        while g is None or g.n != n or kq(g) != k: g = rand_ckO(rng, n, n, k)
        g = pg.Game(rng.sample(range(2 * n + 3), n), list(g.owner), [list(s) for s in g.succ])   # injective priorities (SPEC S1)
        st = None
    sc = score(g, st); first = sc
    for it in range(steps):
        h = mutate(rng, g, k)
        if h is None: continue
        s2 = score(h)
        if s2 is not None and s2 >= sc:
            if s2 > sc: print(f"step {it} score {s2}", flush=True)
            g, sc, st = h, s2, None
    out = write(g, f"s{seed}_n{g.n}_k{k}_{sc[0]}_{sc[1]}")
    print(f"seed {seed} n {g.n} k {k}: start score {first} -> best {sc} -> {out}")

if __name__ == "__main__":
    main()
