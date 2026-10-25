#!/usr/bin/env python3
"""Box 43 greedy shrink of a C^kO game keeping a property of the N5 run from the best-reward start (or the given .start):
  TX   T > sum_i (deg(o_i) - 1)   (tau changes exceed the per-vertex C^1O count, Corollary Phi-1O (a) summed over Odd choice vertices)
  RET  some tau(o_i) returns to an earlier value; RETN: the same by a switch with o_i not its own lambda^U cycle node
  TJ>=m  at least m tau-changing transitions inside one joint lambda-run
Moves: delete a vertex (its in-edges dropped; a vertex left without successors gets a self-loop), delete an edge, lower a priority.
Usage: shrink.py in.pg out.pg PROP [m]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from multi import run, measure, odd_choices, pg
from climb import returns, returns_n, save
from n5x import load

def prop(g, P, m):
    O = odd_choices(g)
    if not O: return False
    try: states, lam, lamU, fbs = run(g, None, cap=5000)
    except RecursionError: return False
    M = measure(g, states, lam, lamU, fbs)
    if P == "TX": return M["T"] > sum(len(g.succ[o]) - 1 for o in O)
    if P == "RET": return returns(g, states) > 0
    if P == "RETN": return returns_n(g, states, lamU) > 0
    if P == "TJ": return M["TJ"] >= m

def cands(g):
    n = g.n
    for v in range(n):
        keep = [x for x in range(n) if x != v]; idx = {x: i for i, x in enumerate(keep)}
        yield pg.Game([g.prio[x] for x in keep], [g.owner[x] for x in keep],
                      [sorted({idx[w] for w in g.succ[x] if w != v}) or [idx[x]] for x in keep])
    for v in range(n):
        if len(g.succ[v]) > 1:
            for w in g.succ[v]:
                yield pg.Game(list(g.prio), list(g.owner), [[y for y in s if not (x == v and y == w)] for x, s in enumerate(g.succ)])
    for v in range(n):
        for p in range(g.prio[v]):
            yield pg.Game([p if x == v else q for x, q in enumerate(g.prio)], list(g.owner), [list(s) for s in g.succ])

if __name__ == "__main__":
    g = load(sys.argv[1]); P = sys.argv[3]; m = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    assert prop(g, P, m), "property fails on the input"
    k = len(odd_choices(g)); changed = True
    while changed:
        changed = False
        for h in cands(g):
            if len(odd_choices(h)) == k and prop(h, P, m):
                g = h; changed = True; break
    save(sys.argv[2], g, None, None); print("n =", g.n, "m =", sum(map(len, g.succ)))
