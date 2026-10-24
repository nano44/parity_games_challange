#!/usr/bin/env python3
"""Box 26: greedy shrinker (canonical start) keeping a pure throttle-release re-entry (reentry.py class THETA, with (h) at leave
and re-entry) inside one (τ, joint-λ)-phase of an o-cyclic C^1O game. Removes edges, then vertices (with reindexing), then
lowers priorities toward a compact range. Usage: shrink_theta.py in.pg out.pg"""
from common import *
from reentry import run
from collections import Counter
def ok(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return False
    g = pg.Game(*G)
    if not any(w in split(g, odd[0]) for w in G[2][odd[0]]): return False
    c = Counter()
    try: run(g, None, c)
    except Exception: return False
    return c["THETA"] - c["THETA_noh"] > 0
if __name__ == "__main__":
    g = load(sys.argv[1]); G = [list(g.prio), list(g.owner), [list(s) for s in g.succ]]; assert ok(G)
    changed = True
    while changed:
        changed = False
        for v in range(len(G[0])):
            for w in list(G[2][v]):
                if len(G[2][v]) < 2: break
                H = [G[0], G[1], [list(s) for s in G[2]]]; H[2][v].remove(w)
                if ok(H): G = H; changed = True
        for x in range(len(G[0]) - 1, -1, -1):
            keep = [v for v in range(len(G[0])) if v != x]; idx = {v: i for i, v in enumerate(keep)}
            s2 = [[idx[w] for w in G[2][v] if w != x] for v in keep]
            if any(not s for s in s2): continue
            H = [[G[0][v] for v in keep], [G[1][v] for v in keep], s2]
            if ok(H): G = H; changed = True; break
        if changed: continue
        for x in range(len(G[0]) - 1, -1, -1):            # contraction: x with one successor y; edges into x go to y
            if len(G[2][x]) != 1 or G[2][x][0] == x: continue
            y = G[2][x][0]; keep = [v for v in range(len(G[0])) if v != x]; idx = {v: i for i, v in enumerate(keep)}
            s2 = [sorted({idx[y] if w == x else idx[w] for w in G[2][v]}) for v in keep]
            H = [[G[0][v] for v in keep], [G[1][v] for v in keep], s2]
            if ok(H): G = H; changed = True; break
        if changed: continue
        for v in range(len(G[0])):                          # priority compaction: try lowering each priority
            for p in range(G[0][v]):
                H = [list(G[0]), G[1], G[2]]; H[0][v] = p
                if ok(H): G = H; changed = True; break
    n = len(G[0])
    open(sys.argv[2], "w").write(f"parity {n-1};\n" + "".join(f"{v} {G[0][v]} {G[1][v]} {','.join(map(str, G[2][v]))};\n" for v in range(n)))
    print("n", n, "edges", sum(len(s) for s in G[2]))
