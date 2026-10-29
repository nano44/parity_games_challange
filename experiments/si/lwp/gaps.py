#!/usr/bin/env python3
"""L-SI box 26: the L-WAVE' gaps of a game as (run, x, y) (same cut / event rules as grun/lwave.py PMODE=1). Imported by lwp/*.py."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
for p in (os.path.join(HERE, "..", "grun"), os.path.join(HERE, "..", "root"), os.path.join(HERE, "..", "runlin"), os.path.join(HERE, "..", "piece")): sys.path.insert(0, p)

LCUTS = []   # the L-cut states a (transition a - 1 -> a) of the last _pts call
EVENTS = set()   # the event states (L-WAVE' events) of the last _pts call

def _pts(g, R):
    del LCUTS[:]; EVENTS.clear()
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
                else: LCUTS.append(a)
            b = a - 1
        EVENTS.update(ev); pts = sorted(set([s] + ev + [e])); out += [(s, e, x, y) for x, y in zip(pts, pts[1:])]
    return out

