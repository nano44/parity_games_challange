#!/usr/bin/env python3
"""L-SI box 28 (docs/si/N5-CHG-box28.md §12): where a CARRY of a vertex y at t comes from. x := the first vertex at which y's honest plays
at t and t + 1 diverge (the play prefix up to x is shared; x is Even with sigma_t(x) != sigma_(t+1)(x), or Odd with a changed sigma-bar).
Lemma INHERIT (note §12): y's P-change is a CARRY iff x's own P-change at t is a CARRY (same cycle node, shared prefix outside both sets).
Counters: INH_V (inheritance fails), src_even / src_odd (carry sources by owner), srcs (distinct (t, x) source carries per phase, max),
carries (all). Usage: carrysrc.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "root")); sys.path.insert(0, os.path.join(HERE, "..", "lwp"))
from common import rows, load, readstart, phases
from compose import matched, bits
from staticdepth import walk
C = Counter(); EX = []

def _run(E, g, R, name):
    n = g.n; rk2v = {E.rank[v]: v for v in range(n)}; odd = lambda r: E.par[rk2v[r]] == 1
    for i, j in phases(R):
        srcs = set(); per = Counter()
        for t in range(i, j):
            A, B = R[t], R[t + 1]
            def carry(x):
                a, b = A["vs"][x], B["vs"][x]
                if a[1] == b[1] or a[0] != b[0]: return None
                rc = E.rank[a[0]]; w = lambda r: (r - rc) if not odd(r) else -(r - rc)
                return not matched(bits(a[1]), bits(b[1]), w, odd)
            for y in range(n):
                cy = carry(y)
                if not cy: continue
                C["carries"] += 1; per[y] += 1
                p0 = list(walk(A["nxt"], y)[0]) + list(walk(A["nxt"], y)[1]); x = None
                for u in p0:
                    if A["nxt"][u] != B["nxt"][u]: x = u; break
                if x is None: C["NOSRC"] += 1; continue
                if carry(x) is not True: C["INH_V"] += 1; EX.append(("INH", name, i, j, t, y, x))
                C["src_even" if g.owner[x] == 0 else "src_odd"] += 1; srcs.add((t, x))
        C["srcs_max_per_phase"] = max(C["srcs_max_per_phase"], len(srcs)); C["nm_max"] = max(C["nm_max"], max(per.values(), default=0))
        C["phases"] += 1

def run(g, name, start=None):
    E, R = rows(g, start, cap=20000); _run(E, g, R, name)

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if p:
                f = os.path.join(ROOT, p[0]) if os.path.exists(os.path.join(ROOT, p[0])) else os.path.join(ROOT, "experiments", p[0])
                s = None
                if len(p) > 1 and os.environ.get("START") == "1":
                    s = os.path.join(ROOT, p[1]) if os.path.exists(os.path.join(ROOT, p[1])) else os.path.join(ROOT, "experiments", p[1])
                try: run(load(f), p[0], readstart(s) if s else None)
                except Exception: C["SKIPPED_input"] += 1
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for z in EX[:6]: print("EXAMPLE", z)
    print("INH", "PASS" if "INH_V" not in C else "FAIL")

if __name__ == "__main__":
    main()
