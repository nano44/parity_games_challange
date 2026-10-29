#!/usr/bin/env python3
"""L-SI box 25 (successor 21): DATA for docs/si/N5-GRUN-box25.md §5. For every REL cut a_i - 1 -> a_i of every run (grun/relseg.py's segments):
SB if sigma-bar changes there at a vertex of RO_(b_i), else CY (a cycle of CW/CH_(b_i) appears). For SB cuts, per changing gate u in RO: P if
the path set of Xi(u) changes at the cut, L if only its length changes, 0 if Xi(u) is unchanged (tie / cycle / pass-through cases of
GATE-RISE). Counts per corpus and max per run of SB cuts with a P-change at some gate. Usage: cutkind.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
for p in (HERE, os.path.join(HERE, "..", "root"), os.path.join(HERE, "..", "runlin"), os.path.join(HERE, "..", "piece")): sys.path.insert(0, p)
from common import rows, load, readstart
from staticdepth import walk
from trace import runs
from pieceh import norm
from relseg import cycof
C = Counter(); TOP = []

def run(g, name, start=None):
    E, R = rows(g, start); n = g.n; Q = [v for v in range(n) if g.owner[v] == 0 and len(set(g.succ[v])) >= 2]
    CWt = [norm(frozenset(walk(r["wn"], v)[1] for v in range(n))) for r in R]; CHt = [norm(frozenset(walk(r["nxt"], v)[1] for v in range(n))) for r in R]
    for s, e, i, j in runs(R):
        b = e; pc = lc = 0
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
            if a > s:
                ch = [u for u in RO if R[a - 1]["sb"][u] != B["sb"][u]]
                if ch:
                    C["cut_SB"] += 1; kinds = set()
                    for u in ch:
                        x, y = R[a - 1]["vs"][u], R[a]["vs"][u]
                        kinds.add("P" if x[1] != y[1] else ("L" if x != y else "0"))
                    k = "P" if "P" in kinds else ("L" if "L" in kinds else "0"); C["cut_SB_" + k] += 1
                    pc += k == "P"; lc += k == "L"
                else: C["cut_CY"] += 1
            b = a - 1
        C["run_P_cuts_max"] = max(C["run_P_cuts_max"], pc); C["run_L_cuts_max"] = max(C["run_L_cuts_max"], lc)
        TOP.append((pc, lc, n, e - s, name))

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if p: run(load(os.path.join(ROOT, p[0])), p[0], readstart(os.path.join(ROOT, p[1])) if len(p) > 1 and os.environ.get("START") == "1" else None)
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for x in sorted(TOP, key=lambda x: -(x[0] + x[1]))[:8]: print("TOP Pcuts %d Lcuts %d n %d run %d %s" % x)

if __name__ == "__main__":
    main()
