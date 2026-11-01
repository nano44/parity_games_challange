#!/usr/bin/env python3
"""L-RED R177 DCHECK: Lemma CASC-G on the abstract model. Runs abs177.simulate on a genome (json), records the dependency digraph D
on Even vertices (v -> u iff u is on the W-play prefix or the Xi-play of some W-tight option of v at some state of the run, u != the
terminal), and prints D acyclic?, height(D), run length, and whether run length <= height + 1 (CASC-G) when D is acyclic.
Usage: dcheck.py genome.json"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import abs177 as A, pg
from si import Engine

def walk(succ, x, stop):
    seq = []; seen = set(); v = x
    while v not in seen and v not in stop:
        seen.add(v); seq.append(v); v = succ[v][0] if len(succ[v]) == 1 else None
        if v is None: break
    return seq

def main(path):
    gen = json.load(open(path)); n, prio, owner, sW, sX, idx = A.build(gen)
    steps, fl, why, hist = A.simulate(gen)
    # replay to collect states
    GX = pg.Game(prio, owner, sX); EX = Engine(GX); N = len(gen["levels"])
    sig = [-1] * n
    for i in range(N): sig[idx[("x", i)]] = idx[("g", i, gen["start"][i])]
    for v in range(n):
        if owner[v] == 0 and sig[v] == -1: sig[v] = sX[v][0]
    states = [list(sig)]
    import n5
    for _ in range(steps):
        vx, _ = EX.evaluate(tuple(sig)); Is = EX.improving(tuple(sig), vx)
        opt = {v: {sig[v]} for v in range(n) if owner[v] == 0}
        for v, w in Is: opt[v].add(w)
        succ = [sorted(opt[v]) if owner[v] == 0 else list(sW[v]) for v in range(n)]
        Er = Engine(n5.dual(pg.Game(prio, owner, succ)))
        _, best = Er.evaluate(tuple(sW[v][0] if owner[v] == 1 else -1 for v in range(n)))
        sig = [best[v] if owner[v] == 0 else -1 for v in range(n)]; states.append(list(sig))
    assert len(states) == steps + 1
    evens = [idx[("x", i)] for i in range(N)]; D = {v: set() for v in evens}
    term = {n - 1, n - 2}
    for s in states:
        s1W = [[s[v]] if owner[v] == 0 else sW[v] for v in range(n)]; s1X = [[s[v]] if owner[v] == 0 else sX[v] for v in range(n)]
        for v in evens:
            for z in sW[v]:
                for u in walk(s1W, z, term) + walk(s1X, z, term):
                    if u in D and u != v or u == v and owner[u] == 0 and u in D: D[v].add(u)
    # height / acyclicity
    color = {}; h = {}
    def dfs(v):
        color[v] = 1; best = 0
        for u in D[v]:
            if color.get(u) == 1: raise ValueError("cycle")
            if color.get(u) != 2: dfs(u)
            best = max(best, 1 + h[u])
        color[v] = 2; h[v] = best
    try:
        for v in evens:
            if v not in color: dfs(v)
        H = max(h.values()); print(f"DCHECK {os.path.basename(path)} acyclic 1 height {H} run {steps} casc_ok {int(steps <= H + 1)}")
    except ValueError:
        print(f"DCHECK {os.path.basename(path)} acyclic 0 run {steps}")

if __name__ == "__main__":
    for p in sys.argv[1:]: main(p)
