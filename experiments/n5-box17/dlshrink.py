#!/usr/bin/env python3
"""Box 17 (Lead 10:36Z item 1): an upper bound on the least n with a DL-RUN deadlock (a deadlock step t > r0 of a REL segment,
box17.analyse 'dl' = L-SI chg/dlock.py DLRUN). Greedy shrink of GAME + START keeping dl > 0 (from the shrunk start pair):
moves = delete a vertex (its in-edges dropped; a start choice into it is re-pointed to the first remaining successor; refused if a
vertex loses all successors), delete an edge (not a start choice; out-degree stays >= 1); first improving move taken, repeat to a fixpoint.
Writes OUT.pg / OUT.start. Usage: dlshrink.py GAME START OUT"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "n5-box18"))
import box17 as B, nm, pg


def dl(prio, owner, succ, st):
    g = pg.Game(prio, owner, succ); e = B.Eng(g)
    try:
        return B.analyse(e, B.trajectory(e, st))["dl"]
    except Exception:  # noqa: BLE001
        return 0


def delvertex(prio, owner, succ, st, x):
    n = len(prio); m = [v for v in range(n) if v != x]; idx = {v: k for k, v in enumerate(m)}
    s2 = [[idx[w] for w in succ[v] if w != x] for v in m]
    if any(not s for s in s2): return None
    s0, t0 = [], []
    for k, v in enumerate(m):
        c = (st[0] if owner[v] == 0 else st[1])[v]; c = idx[c] if c != x else s2[k][0]
        s0.append(c if owner[v] == 0 else -1); t0.append(c if owner[v] == 1 else -1)
    return [prio[v] for v in m], [owner[v] for v in m], s2, (tuple(s0), tuple(t0))


def main():
    g = nm.load(sys.argv[1]); e = B.Eng(g); st = nm.startof(g, e, sys.argv[2])
    cur = (list(g.prio), list(g.owner), [sorted(set(s)) for s in g.succ], st); assert dl(*cur) > 0
    changed = True
    while changed:
        changed = False
        for x in range(len(cur[0]) - 1, -1, -1):
            c = delvertex(*cur, x)
            if c and dl(*c) > 0:
                cur = c; changed = True; print("n", len(cur[0]), flush=True); break
        if changed: continue
        for v in range(len(cur[0])):
            ch = (cur[3][0] if cur[1][v] == 0 else cur[3][1])[v]
            for w in list(cur[2][v]):
                if w == ch or len(cur[2][v]) == 1: continue
                s2 = [list(s) for s in cur[2]]; s2[v].remove(w); c = (cur[0], cur[1], s2, cur[3])
                if dl(*c) > 0:
                    cur = c; changed = True; break
            if changed: break
    prio, owner, succ, (s0, t0) = cur; g2 = pg.Game(prio, owner, succ); pg.write(g2, sys.argv[3] + ".pg")
    with open(sys.argv[3] + ".start", "w") as f:
        f.write("SIGMA0 " + " ".join(f"{v}:{s0[v]}" for v in range(g2.n) if owner[v] == 0) + "\n")
        f.write("TAU0 " + " ".join(f"{v}:{t0[v]}" for v in range(g2.n) if owner[v] == 1) + "\n")
    e2 = B.Eng(g2); a = B.analyse(e2, B.trajectory(e2, (s0, t0)))
    print("SHRUNK n", g2.n, "m", g2.m, "dl", a["dl"], "at", a["dl_at"], "exc", a["exc"])


if __name__ == "__main__":
    main()
