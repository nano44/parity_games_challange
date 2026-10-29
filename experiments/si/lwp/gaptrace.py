#!/usr/bin/env python3
"""L-SI box 26: anatomy of the largest L-WAVE' gap of a game (docs/si/N5-LWP-box26.md). Per transition t -> t+1 of the gap: Even switches,
sigma-bar changes, and the vertices whose Xi changes, split into P-changes (path set) and length-only changes, Odd (o) / Even (e).
Usage: gaptrace.py GAME [START]"""
import sys, os
os.environ["PMODE"] = "1"
HERE = os.path.dirname(os.path.abspath(__file__))
for p in (os.path.join(HERE, "..", "grun"), os.path.join(HERE, "..", "root"), os.path.join(HERE, "..", "runlin"), os.path.join(HERE, "..", "piece")): sys.path.insert(0, p)
from common import rows, load, readstart
import lwave

def main():
    g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; E, R = rows(g, st)
    lwave.C.clear(); del lwave.EX[:]
    lwave._run(g, R, "x")
    # recompute gaps with positions
    best = None
    for x, y in GAPS(g, R):
        if best is None or y - x > best[1] - best[0]: best = (x, y)
    x, y = best; print("n", g.n, "gap", x, y, "len", y - x)
    for t in range(x, y):
        A, B = R[t], R[t + 1]
        sw = ["%d:%d>%d" % (v, A["s"][v], B["s"][v]) for v in range(g.n) if g.owner[v] == 0 and A["s"][v] != B["s"][v]]
        sb = ["%d:%d>%d" % (v, A["sb"][v], B["sb"][v]) for v in range(g.n) if g.owner[v] == 1 and A["sb"][v] != B["sb"][v]]
        P = ["%s%d" % ("eo"[g.owner[v]], v) for v in range(g.n) if A["vs"][v][1] != B["vs"][v][1] or A["vs"][v][0] != B["vs"][v][0]]
        L = ["%s%d" % ("eo"[g.owner[v]], v) for v in range(g.n) if A["vs"][v][:2] == B["vs"][v][:2] and A["vs"][v] != B["vs"][v]]
        print(t, "sw", " ".join(sw), "| sb", " ".join(sb), "| P", " ".join(P), "| L", " ".join(L))

def GAPS(g, R):
    import lwave as LW
    out = []
    old = LW.C, LW.EX
    LW.C, LW.EX = __import__("collections").Counter(), []
    # monkeypatch: capture pts via EX by making n-1 huge negative
    class G2: pass
    g2 = G2(); g2.__dict__.update(g.__dict__); g2.n = g.n
    LW._run_pts = []
    src = LW._run
    return _pts(g, R)

def _pts(g, R):
    import lwave as LW
    from staticdepth import walk
    from trace import runs
    from relseg import cycof
    from pieceh import norm
    n = g.n; Q = [v for v in range(n) if g.owner[v] == 0 and len(set(g.succ[v])) >= 2]
    CWt = [norm(frozenset(walk(r["wn"], v)[1] for v in range(n))) for r in R]; CHt = [norm(frozenset(walk(r["nxt"], v)[1] for v in range(n))) for r in R]
    out = []
    for s, e, i, j in runs(R):
        ev = []; b = e
        while b >= s:
            B = R[b]; X, stk = set(), list(Q)
            while stk:
                x = stk.pop()
                if x in X: continue
                X.add(x); stk.extend(y for y in sum(walk(B["wn"], x), ()) + sum(walk(B["nxt"], x), ()) if g.owner[y] == 0)
            RO = {y for v in X for y in sum(walk(B["nxt"], v), ()) if g.owner[y] == 1}
            CW = frozenset().union(*[cycof(B["wn"], v) for v in X]) if X else frozenset()
            CH = frozenset().union(*[cycof(B["nxt"], v) for v in X]) if X else frozenset()
            a = b
            while a > s and all(R[a - 1]["sb"][u] == B["sb"][u] for u in RO) and CW <= CWt[a - 1] and CH <= CHt[a - 1]: a -= 1
            for t in range(max(a, s + 1), b + 1):
                if any(R[t - 1]["vs"][u][1] != R[t]["vs"][u][1] for u in RO if len(set(g.succ[u])) > 1): ev.append(t)
            if a > s:
                ch = [u for u in RO if R[a - 1]["sb"][u] != B["sb"][u]]
                isL = bool(ch) and all(R[a - 1]["vs"][u][1] == R[a]["vs"][u][1] and R[a - 1]["vs"][u] != R[a]["vs"][u] for u in ch)
                if not isL: ev.append(a)
                else: print("Lcut", a, "gates", ch)
            b = a - 1
        pts = sorted(set([s] + ev + [e])); out += list(zip(pts, pts[1:]))
    return out

if __name__ == "__main__":
    main()
