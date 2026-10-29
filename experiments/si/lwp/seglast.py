#!/usr/bin/env python3
"""L-SI box 26: DATA for the candidate SEG-LAST (docs/si/N5-LWP-box26.md): inside each maximal REL-admissible segment [a, b] of a run
(grun/relseg.py's cutting), every transition t -> t+1 (a <= t < b) contains the last switch in [a, b] of some Even vertex. It would give
b - a <= the number of Even vertices switching in [a, b]. MODE=piece: the same on sigma-bar-constant pieces; MODE=run: on whole runs
(control: must fail). Also DMONO_V / DSTRICT_V: segments where D_t = {v : sigma_t(v) != sigma_b(v)} fails to shrink / to shrink
strictly at every transition (DSTRICT would give the bound with |D_a|). SS_V: transitions where no switcher becomes W- and H-settled
(play-level, both frames) from t + 1 (SET-STEP, which implies SEG-LAST). Usage: seglast.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import gaps
from common import rows, load, readstart
from staticdepth import walk
from trace import runs
from relseg import cycof
from pieceh import norm
from staticdepth import walk
C = Counter(); EX = []; MODE = os.environ.get("MODE", "seg")

def segs(g, R):
    n = g.n; Q = [v for v in range(n) if g.owner[v] == 0 and len(set(g.succ[v])) >= 2]
    CWt = [norm(frozenset(walk(r["wn"], v)[1] for v in range(n))) for r in R]; CHt = [norm(frozenset(walk(r["nxt"], v)[1] for v in range(n))) for r in R]
    for s, e, i, j in runs(R):
        if MODE == "run": yield s, e; continue
        b = e
        while b >= s:
            B = R[b]
            if MODE == "piece":
                a = b
                while a > s and R[a - 1]["sb"] == B["sb"]: a -= 1
            else:
                X, st = set(), list(Q)
                while st:
                    x = st.pop()
                    if x in X: continue
                    X.add(x); st.extend(y for y in sum(walk(B["wn"], x), ()) + sum(walk(B["nxt"], x), ()) if g.owner[y] == 0)
                RO = {y for v in X for y in sum(walk(B["nxt"], v), ()) if g.owner[y] == 1}
                CW = frozenset().union(*[cycof(B["wn"], v) for v in X]) if X else frozenset()
                CH = frozenset().union(*[cycof(B["nxt"], v) for v in X]) if X else frozenset()
                a = b
                while a > s and all(R[a - 1]["sb"][u] == B["sb"][u] for u in RO) and CW <= CWt[a - 1] and CH <= CHt[a - 1]: a -= 1
            yield a, b; b = a - 1

def slscore(g, R):
    """(number of SEG-LAST failures, max over segments of (length - switching Even vertices)) for the climb lwp/xclimb.py OBJ=SL."""
    global C, EX
    save = (C, EX); C, EX = Counter(), []
    try: _run(g, R, "x"); return C["SL_V"], C.get("ex_max_plus1000", 1000 - 10 ** 6) - 1000
    finally: C, EX = save

def run(g, name, start=None):
    E, R = rows(g, start); _run(g, R, name)

def _run(g, R, name):
    for a, b in segs(g, R):
        if b <= a: continue
        C["segs"] += 1; C["trans"] += b - a; last = {}
        for t in range(a, b):
            for v in range(g.n):
                if g.owner[v] == 0 and R[t]["s"][v] != R[t + 1]["s"][v]: last[v] = t
        D = [frozenset(v for v in range(g.n) if g.owner[v] == 0 and R[t]["s"][v] != R[b]["s"][v]) for t in range(a, b + 1)]
        if any(not D[k + 1] <= D[k] for k in range(b - a)): C["DMONO_V"] += 1     # D_t = {v : sigma_t(v) != sigma_b(v)} shrinks?
        if any(not D[k + 1] < D[k] for k in range(b - a)): C["DSTRICT_V"] += 1
        C["ex_max_plus1000"] = max(C.get("ex_max_plus1000", 0), 1000 + (b - a) - len(last))
        # SET-STEP: some switcher of t is W- and H-settled from t + 1 (plays at every s in [t+1, b] equal its plays at b)
        for t in range(a, b):
            sw = [v for v in range(g.n) if g.owner[v] == 0 and R[t]["s"][v] != R[t + 1]["s"][v]]
            if not any(all(walk(R[u]["wn"], v) == walk(R[b]["wn"], v) and walk(R[u]["nxt"], v) == walk(R[b]["nxt"], v) for u in range(t + 1, b + 1)) for v in sw):
                C["SS_V"] += 1; EX.append(("SS", name, a, b, t))
        lt = set(last.values()); bad = [t for t in range(a, b) if t not in lt]
        if bad: C["SL_V"] += len(bad); EX.append((name, a, b, bad[:4], b - a, len(last), g.n))

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if p: run(load(os.path.join(ROOT, p[0])), p[0], readstart(os.path.join(ROOT, p[1])) if len(p) > 1 and os.environ.get("START") == "1" else None)
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for z in EX[:8]: print("EXAMPLE", z)
    print("SEGLAST PASS" if "SL_V" not in C else "SEGLAST FAIL")

if __name__ == "__main__":
    main()
