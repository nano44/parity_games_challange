#!/usr/bin/env python3
"""L-SI box 24 (successor 20): greedy shrink for RUN-LIN. Repeatedly (1) delete an Even edge if the longest fallback-free run does not drop,
(2) delete a non-choice vertex if the run drops by < 2 (so run - 2n rises). Odd choice vertices are kept. Usage: shrink.py G.pg G.start OUT"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from growclimb import runlen, mkst, save, odd_choices
from common import load, readstart
import pg

def delete(g, st, v):
    keep = [x for x in range(g.n) if x != v]; idx = {x: i for i, x in enumerate(keep)}; ns = []
    for x in keep:
        s = sorted({idx[w] for w in g.succ[x] if w != v})
        if not s: return None
        ns.append(s)
    st2 = []
    for i, x in enumerate(keep):
        y = st[x]; st2.append(idx[y] if y != v else ns[i][0])
    return pg.Game([g.prio[x] for x in keep], [g.owner[x] for x in keep], ns), st2

g = load(sys.argv[1]); s, t = readstart(sys.argv[2]); st = [s.get(v, t.get(v)) for v in range(g.n)]; out = sys.argv[3]
O = set(odd_choices(g)); cur = runlen(g, mkst(g, st)); print("start run", cur, "n", g.n, flush=True)
changed = True
while changed:
    changed = False
    for v in range(g.n):
        if g.owner[v] != 0: continue
        for w in list(g.succ[v]):
            if len(g.succ[v]) < 2 or w == st[v]: continue
            succ = [list(x) for x in g.succ]; succ[v] = [x for x in succ[v] if x != w]
            h = pg.Game(list(g.prio), list(g.owner), succ); r = runlen(h, mkst(h, st))
            if r is not None and r >= cur: g, cur, changed = h, r, True
    v = 0
    while v < g.n:
        if v in O or (g.owner[v] == 1 and len(g.succ[v]) > 1): v += 1; continue
        res = delete(g, st, v)
        if res:
            h, st2 = res
            if len(odd_choices(h)) == len(O):
                r = runlen(h, mkst(h, st2))
                if r is not None and r - 2 * h.n > cur - 2 * g.n:
                    O = set(odd_choices(h)); g, st, cur, changed = h, st2, r, True
                    print("deleted -> run", cur, "n", g.n, "run-2n", cur - 2 * g.n, flush=True); continue
        v += 1
save(out, g, st); print("final run", cur, "n", g.n, "ratio %.3f" % (cur / g.n))
