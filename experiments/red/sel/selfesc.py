#!/usr/bin/env python3
"""L-RED successor 23: test (O5) SELF-ESCAPE (docs/red/R96) on N5 runs. At every state of every phase (tau constant), for every gate g
(Odd, sigma-bar(g) = A != tau(g)): follow the play from A under (tau-bar, tau), tau-bar = Even's optimal counterstrategy to tau (Ed.evaluate
on the dual game), and record whether it passes g. (O5) predicts never. Control MUT=1: follow the play from A under (sigma, sigma-bar).
Usage: selfesc.py GAME.pg START [GAME.pg START ...]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import trace as T
MUT = os.environ.get("MUT") == "1"

def through(a, nxt, g):
    v, seen = a, set()
    while v not in seen:
        if v == g: return True
        seen.add(v); v = nxt[v]
    return False

def one(path, st):
    g = T.pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%")))
    states = []
    T.run(g, T.readstart(st), log=lambda *a: None, states=states)
    E, Ed = T.Engine(g), T.Engine(T.dual(g)); n = g.n
    split = selfesc = held = 0; ex = None
    for t, (sigma, tau) in enumerate(states):
        _, sbar = E.evaluate(sigma); _, tbar = Ed.evaluate(tau)
        for u in range(n):
            if g.owner[u] != 1 or sbar[u] == tau[u]: continue
            split += 1
            if MUT: nxt = [sigma[v] if g.owner[v] == 0 else sbar[v] for v in range(n)]
            else: nxt = [tbar[v] if g.owner[v] == 0 else tau[v] for v in range(n)]
            if through(sbar[u], nxt, u):
                selfesc += 1
                vs, _ = E.evaluate(sigma); Is = set(E.improving(sigma, vs))
                v, seen, pend = sbar[u], set(), True
                while v != u and v not in seen:
                    seen.add(v)
                    if g.owner[v] == 0 and nxt[v] != sigma[v] and (v, nxt[v]) in Is: pend = False
                    v = nxt[v]
                if pend:
                    held += 1
                    if ex is None: ex = (t, u, sbar[u])
    print("%s n=%d states=%d split_gate_states=%d self_escapes=%d held(no Isigma edge on route)=%d first_held=%s%s" % (os.path.basename(path), n, len(states), split, selfesc, held, ex, " MUT" if MUT else ""))

if __name__ == "__main__":
    a = sys.argv[1:]
    for i in range(0, len(a), 2): one(a[i], a[i + 1])
