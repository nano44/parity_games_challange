#!/usr/bin/env python3
"""L-SI box 25 (successor 21): DATA for docs/si/N5-GRUN-box25.md §5. Per fallback-free in-phase run S and vertex v: XR_S(v) (transitions changing
Xi(v)) and PCH_S(v) (transitions changing the path set P of Xi(v); the cycle node is constant in a phase). Within a block of constant (c, P)
only the length moves, strictly monotonically, so XR_S(v) <= PCH_S(v) + (PCH_S(v) + 1)(n - 1) (BLOCK_V counts failures of the per-block
monotonicity). Prints max XR, max PCH over gates and over all vertices, and max PCH/n. Usage: pch.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
for p in (os.path.join(HERE, "..", "root"), os.path.join(HERE, "..", "runlin")): sys.path.insert(0, p)
from common import rows, load, readstart
from trace import runs
C = Counter(); TOP = []

def run(g, name, start=None):
    E, R = rows(g, start); n = g.n
    gates = {u for u in range(n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1}
    for a, b, i, j in runs(R):
        if b <= a: continue
        for v in range(n):
            xr = pch = 0; dirn = None
            for t in range(a, b):
                x, y = R[t]["vs"][v], R[t + 1]["vs"][v]
                if x == y: continue
                xr += 1
                if x[0] != y[0]: C["CN_CHANGE"] += 1
                if x[1] != y[1]: pch += 1; dirn = None
                else:
                    d = (y[2] > x[2])
                    if dirn is not None and d != dirn: C["BLOCK_V"] += 1
                    dirn = d
            k = "gate" if v in gates else "all"
            for kk in ({"all", k}):
                C[f"XR_{kk}_max"] = max(C[f"XR_{kk}_max"], xr); C[f"PCH_{kk}_max"] = max(C[f"PCH_{kk}_max"], pch)
                C[f"PCH_{kk}_over_n_x1000_max"] = max(C[f"PCH_{kk}_over_n_x1000_max"], 1000 * pch // n)
            if v in gates: TOP.append((pch, xr, n, b - a, name, v, a, b))

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if p: run(load(os.path.join(ROOT, p[0])), p[0], readstart(os.path.join(ROOT, p[1])) if len(p) > 1 and os.environ.get("START") == "1" else None)
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for x in sorted(TOP, key=lambda x: -x[0] / x[2])[:8]: print("TOP gate PCH %d XR %d n %d run %d %s u %d [%d,%d]" % x)
    print("PCH PASS" if not any(k in C for k in ("BLOCK_V", "CN_CHANGE")) else "PCH FAIL")

if __name__ == "__main__":
    main()
