#!/usr/bin/env python3
"""N8a: delta-debug a crawl instance to a small core. Deleting node v = removing every arc into v (rejected if some node would lose its
last successor), then dropping v and compacting ids. Kept iff the padding growth of degree `order` stays >= frac of the original
(order 2: P(2K) - 2P(K) + P(0); order 1: P(K) - P(0); P = primal + dual pivots, rule global). Usage: shrink.py in.pg order K out.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import kl, pg
src, order, K, dst = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
frac = 0.9
g = pg.parse("".join(l for l in open(src) if not l.lstrip().startswith("%")))
prio, owner, succ = list(g.prio), list(g.owner), [list(dict.fromkeys(s)) for s in g.succ]


def P(prio, owner, succ, k):
    gg = pg.Game(list(prio) + [0] * k, list(owner) + [0] * k, [list(s) for s in succ] + [[len(prio) + i] for i in range(k)])
    r = kl.solve(gg, "global"); return r["it"] + r["it_dual"]


def fit(prio, owner, succ):
    if order == 1: return P(prio, owner, succ, K) - P(prio, owner, succ, 0)
    return P(prio, owner, succ, 2 * K) - 2 * P(prio, owner, succ, K) + P(prio, owner, succ, 0)


def delete(prio, owner, succ, v):
    S = [[w for w in s if w != v] for s in succ]
    if any(not S[u] for u in range(len(S)) if u != v): return None
    keep = [u for u in range(len(prio)) if u != v]; idx = {u: i for i, u in enumerate(keep)}
    return [prio[u] for u in keep], [owner[u] for u in keep], [[idx[w] for w in S[u]] for u in keep]


base = fit(prio, owner, succ); print("start n", len(prio), "fitness", base, flush=True)
changed = True
while changed:
    changed = False
    for v in reversed(range(len(prio))):
        r = delete(prio, owner, succ, v)
        if r is None: continue
        try: f = fit(*r)
        except Exception: continue
        if f >= frac * base:
            prio, owner, succ = r; changed = True; print("deleted, n", len(prio), "fitness", f, flush=True)
            break
pg.write(pg.Game(prio, owner, succ), dst); print("final n", len(prio), "fitness", fit(prio, owner, succ))
