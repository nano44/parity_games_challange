#!/usr/bin/env python3
"""L-SI box 24 (successor 20): growth climb for CONJECTURE RUN-LIN (docs/si/N5-RUNLIN-box24.md).
Objective: the longest fallback-free in-phase run R; score = R - C*n (env C, default 1.25), so a vertex is kept only if it adds > C steps.
Mutations: experiments/new/box43/climb.mutate (Odd choice set fixed) plus CLONE: copy an Even vertex v (same priority + 0/1, same successors,
the copy also gets the edge to v or v gets the edge to the copy) and give a random predecessor of v an edge to the copy.
Usage: growclimb.py SEED.pg SEED.start|- STEPS RNGSEED NMAX OUTPREFIX"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(HERE, "..", "root")); sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box43")); sys.path.insert(0, HERE)
from common import rows, load, readstart
import climb, pg
climb.DEG2 = False
from multi import odd_choices
from trace import runs
C = float(os.environ.get("C", "1.25"))

def runlen(g, st):
    try: E, R = rows(g, st, cap=1500)
    except (RecursionError, RuntimeError): return None
    if len(R) > 1500: return None
    rr = list(runs(R))
    return max((b - a for a, b, i, j in rr), default=0)

def mkst(g, st):
    if not st: return None
    return ({v: st[v] for v in range(g.n) if g.owner[v] == 0}, {v: st[v] for v in range(g.n) if g.owner[v] == 1})

def clone(rng, g, O, nmax, st):
    n = g.n
    if n >= nmax: return None
    ev = [v for v in range(n) if g.owner[v] == 0]
    v = rng.choice(ev); prio, owner, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]
    prio.append(max(0, prio[v] + rng.choice([-1, 0, 0, 1]))); owner.append(0)
    s = set(succ[v]) - {v}
    if rng.random() < 0.5: s.add(v)
    else: succ[v] = sorted(set(succ[v]) | {n})
    succ.append(sorted(s) or [v])
    preds = [u for u in range(n) if v in succ[u] and (owner[u] == 0 or u in O)]
    if preds:
        u = rng.choice(preds); succ[u] = sorted(set(succ[u]) | {n})
    st2 = list(st) + [succ[n][0]] if st else None
    h = pg.Game(prio, owner, succ)
    if len(odd_choices(h)) != len(O): return None
    return h, O, st2

def save(out, g, st):
    with open(out + ".pg", "w") as f:
        f.write("parity %d;\n" % (g.n - 1))
        for v in range(g.n): f.write("%d %d %d %s;\n" % (v, g.prio[v], g.owner[v], ",".join(map(str, g.succ[v]))))
    if st:
        with open(out + ".start", "w") as f:
            f.write("SIGMA0 " + " ".join("%d:%d" % (v, st[v]) for v in range(g.n) if g.owner[v] == 0) + "\n")
            f.write("TAU0 " + " ".join("%d:%d" % (v, st[v]) for v in range(g.n) if g.owner[v] == 1) + "\n")

def main():
    gp, sp, steps, seed, nmax, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
    rng = random.Random(seed); g = load(gp); O = sorted(odd_choices(g)); st = None
    if sp != "-":
        s, t = readstart(sp); st = [s.get(v, t.get(v)) for v in range(g.n)]
    r = runlen(g, mkst(g, st)); cur = r - C * g.n; bestr = (r, g.n)
    print("seed run", r, "n", g.n, flush=True)
    for it in range(steps):
        res = clone(rng, g, O, nmax, st) if rng.random() < 0.25 else climb.mutate(rng, g, O, nmax, st)
        if res is None: continue
        g2, O2, st2 = res
        r2 = runlen(g2, mkst(g2, st2))
        if r2 is None: continue
        sc = r2 - C * g2.n
        if sc >= cur:
            if sc > cur: print("step", it, "run", r2, "n", g2.n, "ratio %.3f" % (r2 / g2.n), flush=True)
            if r2 / g2.n > bestr[0] / bestr[1]: bestr = (r2, g2.n); save(out, g2, st2)
            g, O, st, cur = g2, O2, st2, sc
    print("final best run/n", bestr, "%.3f" % (bestr[0] / bestr[1]))

if __name__ == "__main__":
    main()
