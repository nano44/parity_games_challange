#!/usr/bin/env python3
"""Shrink a game on which avh.py disagrees with the reference (brute force for n <= 12, else py Zielonka), or on
which its strategy fails verify.py. Greedy: delete vertices, delete edges, compress priorities, flip owners only
if the failure persists; repeat to a fixpoint.
Usage: shrink.py in.pg out.pg [--kind region|strategy]"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pg, zielonka, verify, avh


def ref(g):
    return zielonka.brute_force(g) if sum(1 for v in range(g.n) if g.owner[v] == 0) <= 12 and g.n <= 14 else zielonka.solve(g)


def fails(g, kind):
    try:
        win, strat = avh.Solver(g).solve()
    except avh.Stuck:
        return kind == "region"
    if kind == "region":
        return win != ref(g)
    return win == ref(g) and bool(verify.check(g, win, strat))


def rebuild(prio, owner, succ, keep):
    idx = {v: i for i, v in enumerate(keep)}
    ns = [[idx[w] for w in succ[v] if w in idx] for v in keep]
    if any(not s for s in ns):
        return None
    return pg.Game([prio[v] for v in keep], [owner[v] for v in keep], ns)


def compress(g):
    ps = sorted(set(g.prio)); m, cur = {}, -1
    for p in ps:
        cur += 1
        if cur % 2 != p % 2:
            cur += 1
        m[p] = cur
    return pg.Game([m[p] for p in g.prio], g.owner, g.succ)


def shrink(g, kind):
    changed = True
    while changed:
        changed = False
        for v in range(g.n):
            h = rebuild(g.prio, g.owner, g.succ, [u for u in range(g.n) if u != v])
            if h and h.n and fails(h, kind):
                g, changed = h, True; break
        if changed:
            continue
        for v in range(g.n):
            for w in list(set(g.succ[v])):
                if len(set(g.succ[v])) <= 1:
                    break
                succ = [list(s) for s in g.succ]; succ[v] = [x for x in succ[v] if x != w]
                h = pg.Game(g.prio, g.owner, succ)
                if fails(h, kind):
                    g, changed = h, True; break
            if changed:
                break
        if changed:
            continue
        h = compress(g)
        if h.prio != g.prio and fails(h, kind):
            g, changed = h, True; continue
        for v in range(g.n):  # lower single priorities by 2 (keeps parity)
            if g.prio[v] >= 2:
                pr = list(g.prio); pr[v] -= 2
                h = pg.Game(pr, g.owner, g.succ)
                if fails(h, kind):
                    g, changed = h, True; break
    return g


if __name__ == "__main__":
    kind = "strategy" if "strategy" in sys.argv else "region"
    g = pg.read(sys.argv[1])
    assert fails(g, kind), "input does not fail"
    h = shrink(g, kind)
    pg.write(h, sys.argv[2])
    print(f"shrunk {g.n} -> {h.n} vertices ({kind})")
    print(pg.dumps(h))
    w, s = avh.Solver(h).solve()
    print("avh:", w, "strategy:", s)
    print("ref:", ref(h))
