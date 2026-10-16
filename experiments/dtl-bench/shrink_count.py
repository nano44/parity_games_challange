#!/usr/bin/env python3
"""Shrink a game on which dtl_py.py (--order oink) and Oink's pinned dtl/idtl differ in (tangles, dominions, iterations)
or in regions. Greedy: delete vertices, delete edges, merge priorities, flip owners; keep a change iff the divergence persists.
Usage: shrink_count.py IN.pg OUT.pg [--idtl]"""
import sys, os, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_py, compare, bench

IDTL = "--idtl" in sys.argv
TD = tempfile.mkdtemp()


def sig(g):
    gp = os.path.join(TD, "g.pg"); pg.write(g, gp)
    st, text, *_ , log = compare.run(bench.PIN["idtl-pin" if IDTL else "dtl-pin"], gp, 60)
    if st != "ok":
        return None
    c = bench.counters(log)
    W, S, d = dtl_py.solve_game(g, IDTL, "oink")
    o = (int(c["tangles"]), int(c["dominions"]), int(c["iterations"]), tuple(pg.read_sol(text, g.n)))
    p = (d.tangles, d.dominions, d.iterations, tuple(W))
    return o, p


def fails(g):
    s = sig(g)
    return s is not None and s[0] != s[1]


def rebuild(g, keep):
    idx = {v: i for i, v in enumerate(keep)}
    ns = [[idx[w] for w in g.succ[v] if w in idx] for v in keep]
    if any(not s for s in ns):
        return None
    return pg.Game([g.prio[v] for v in keep], [g.owner[v] for v in keep], ns)


def shrink(g):
    changed = True
    while changed:
        changed = False
        for v in range(g.n):
            h = rebuild(g, [u for u in range(g.n) if u != v])
            if h and h.n and fails(h):
                g, changed = h, True; break
        if changed:
            continue
        for v in range(g.n):
            for w in list(dict.fromkeys(g.succ[v])):
                if len(g.succ[v]) <= 1:
                    break
                succ = [list(s) for s in g.succ]; succ[v] = [x for x in succ[v] if x != w]
                h = pg.Game(g.prio, g.owner, succ)
                if fails(h):
                    g, changed = h, True; break
            if changed:
                break
        if changed:
            continue
        ps = sorted(set(g.prio))
        for a, b in zip(ps, ps[1:]):          # merge priority b into a (same parity only) or lower b by 2
            for nb in ([a] if a % 2 == b % 2 else []) + ([b - 2] if b >= 2 else []):
                h = pg.Game([nb if x == b else x for x in g.prio], g.owner, g.succ)
                if fails(h):
                    g, changed = h, True; break
            if changed:
                break
    return g


g = pg.read(sys.argv[1])
assert fails(g), "no divergence on input"
h = shrink(g)
pg.write(h, sys.argv[2])
print(f"shrunk {g.n} -> {h.n} vertices, {h.m} edges; oink vs py: {sig(h)[0][:3]} vs {sig(h)[1][:3]}")
