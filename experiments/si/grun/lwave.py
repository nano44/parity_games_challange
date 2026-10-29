#!/usr/bin/env python3
"""L-SI box 25 (successor 21): DATA for CONJECTURE L-WAVE (docs/si/N5-GRUN-box25.md §5). The REL cuts of each run (grun/relseg.py) are split
into L-cuts (sigma-bar changes on RO only at gates whose Xi changes in its length alone) and the rest (P-changes, ties, cycle appearances).
L-WAVE: between two consecutive non-L cuts (or the run's ends) there are <= n - 1 transitions. Prints the number of gaps, max (gap - (n - 1))
(LW_V counts gaps above n - 1) and the max number of non-L cuts per run. PMODE=1 tests L-WAVE' (DEAD L-WAVE refined): events also at every path-set change of Xi at an Odd choice vertex of RO_b.
Usage: lwave.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
for p in (HERE, os.path.join(HERE, "..", "root"), os.path.join(HERE, "..", "runlin"), os.path.join(HERE, "..", "piece")): sys.path.insert(0, p)
from common import rows, load, readstart
from staticdepth import walk
from trace import runs
from pieceh import norm
from relseg import cycof
C = Counter(); EX = []; PMODE = os.environ.get("PMODE") == "1"   # PMODE=1: L-WAVE' events

def maxgap(g, R):
    """max over the runs of R of (gap - (n - 1)) between consecutive non-L cuts (the L-WAVE slack, negated)."""
    global C, EX
    save = (C, EX); C, EX = Counter(), []
    try:
        _run(g, R, "x")
        return C["gap_minus_n1_max_plus1000"] - 1000 if C["gaps"] else -10 ** 6
    finally:
        C, EX = save

def run(g, name, start=None):
    E, R = rows(g, start); _run(g, R, name)

def _run(g, R, name):
    n = g.n; Q = [v for v in range(n) if g.owner[v] == 0 and len(set(g.succ[v])) >= 2]
    CWt = [norm(frozenset(walk(r["wn"], v)[1] for v in range(n))) for r in R]; CHt = [norm(frozenset(walk(r["nxt"], v)[1] for v in range(n))) for r in R]
    for s, e, i, j in runs(R):
        ev = []; b = e
        while b >= s:
            B = R[b]; X, st = set(), list(Q)
            while st:
                x = st.pop()
                if x in X: continue
                X.add(x); st.extend(y for y in sum(walk(B["wn"], x), ()) + sum(walk(B["nxt"], x), ()) if g.owner[y] == 0)
            RO = {y for v in X for y in sum(walk(B["nxt"], v), ()) if g.owner[y] == 1}
            CW = frozenset().union(*[cycof(B["wn"], v) for v in X]) if X else frozenset()
            CH = frozenset().union(*[cycof(B["nxt"], v) for v in X]) if X else frozenset()
            a = b
            while a > s and all(R[a - 1]["sb"][u] == B["sb"][u] for u in RO) and CW <= CWt[a - 1] and CH <= CHt[a - 1]: a -= 1
            if PMODE:                                    # L-WAVE': also every transition inside [a, b] (or into it) at which the path set
                for t in range(max(a, s + 1), b + 1):    # of Xi changes at an Odd vertex of RO_b (b this segment's end)
                    if any(R[t - 1]["vs"][u][1] != R[t]["vs"][u][1] for u in RO if len(set(g.succ[u])) > 1): ev.append(t)
            if a > s:
                ch = [u for u in RO if R[a - 1]["sb"][u] != B["sb"][u]]
                isL = bool(ch) and all(R[a - 1]["vs"][u][1] == R[a]["vs"][u][1] and R[a - 1]["vs"][u] != R[a]["vs"][u] for u in ch)
                if not isL: ev.append(a)
            b = a - 1
        C["nonL_cuts_max"] = max(C["nonL_cuts_max"], len(ev))
        pts = sorted(set([s] + ev + [e]))
        for x, y in zip(pts, pts[1:]):
            C["gaps"] += 1; C["gap_minus_n1_max_plus1000"] = max(C["gap_minus_n1_max_plus1000"], 1000 + (y - x) - (n - 1))
            if y - x > n - 1: C["LW_V"] += 1; EX.append((name, x, y, n))

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if p: run(load(os.path.join(ROOT, p[0])), p[0], readstart(os.path.join(ROOT, p[1])) if len(p) > 1 and os.environ.get("START") == "1" else None)
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for x in EX[:6]: print("EXAMPLE", x)
    print("LWAVE PASS" if "LW_V" not in C else "LWAVE FAIL")

if __name__ == "__main__":
    main()
