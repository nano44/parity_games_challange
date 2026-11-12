#!/usr/bin/env python3
"""L-RED 66 R234: cross-check of box 101's DATA with L-RED 66's independent engine lg234.py.
Regenerates the exact game sequence of lamgap101.py SEED COUNT NMAX (claude/l-si 23d39400; file path in env LSI, its engine in env RED)
by executing its source without the final main() call and replaying its rng consumption; then, per game, (1) relabels vertices by
own.VJ's relevance rank (prio, index) and compares every vertex value of lg234 against own.VJ on the strategies of both of box 101's
runs (must-0: valdiff), (2) runs lg234's ALL-tie-resolution search from those runs' start strategies (must-0: gapfail, sharpfail).
Usage: xlg234.py SEED COUNT NMAX"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lg234
src = open(os.environ["LSI"]).read().rsplit("\nmain()", 1)[0]
ns = {"__name__": "lamgap101", "__file__": os.environ["LSI"]}; exec(compile(src, "lamgap101", "exec"), ns)
seed, cnt, nmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
rng = random.Random(seed); tot = dict(games=0, valchecked=0, valdiff=0, runs=0, gapfail=0, sharpfail=0, eqCh=0, tight=0, capped=0, maxT=0, maxwin={})
for i in range(cnt):
    n = rng.randint(2, nmax); prio, succ = ns["game"](rng, n)
    if rng.random() < 0.3:
        for v in range(n - 1):
            if v + 1 not in succ[v]: succ[v] = sorted(succ[v] + [v + 1])
    order = sorted(range(n), key=lambda v: (prio[v], v)); rk = {v: r for r, v in enumerate(order)}
    par = tuple(prio[order[r]] % 2 for r in range(n)); succ2 = [sorted(rk[w] for w in succ[order[r]]) for r in range(n)]
    starts = []
    for rule in ("rnd", "idx"):
        out, vj = ns["run"](prio, succ, rng, rule)
        starts.append([rk[out[0][0][order[r]]] for r in range(n)])
        for sig, vals in out:
            s2 = [rk[sig[order[r]]] for r in range(n)]
            for r in range(n):
                a = lg234.val(r, s2, par); b = vals[order[r]]; tot["valchecked"] += 1
                if (a[0], a[1], a[2]) != (rk[b[0]], frozenset(rk[u] for u in b[1]), b[2]): tot["valdiff"] += 1
    tot["games"] += 1; lg234.check(succ2, par, starts, tot)
print("TOTAL", tot, flush=True)
