#!/usr/bin/env python3
"""L-SI box 29: CANDIDATE RISE-DEPTH in frozen W-phases [a, b] (fwphase.py): if W changes at x at transition a+k-1 -> a+k (k >= 1), then
W_(a+k)(x).length >= k (R17 Lemma P's consequence; it implies FW-BF since lengths are <= n - 1). RD_V counts failures; RDX_V the same for
Xi. Also LMAX: max L/(n-1) per frozen W-phase (L counts W-silent transitions too). Usage: risedepth.py --one GAME [START] | --list FILE"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "root"))
from common import rows, load, readstart, phases
from fwphase import fwphases
C = Counter(); EX = []; MX = [0, None]

def _run(E, g, R, name):
    n = g.n
    for i, j in phases(R):
        for a, b in fwphases(R, i, j):
            D = sum(1 for u in range(n) if g.owner[u] == 1 and R[a]["sb"][u] != R[a]["t"][u])
            if (b - a) / (n - 1) > MX[0]: MX[0] = (b - a) / (n - 1); MX[1] = (name, a, b, D, n)
            for k in range(1, b - a + 1):
                for key, tag in (("W", "RD"), ("vs", "RDX")):
                    for x in range(n):
                        p, q = R[a + k - 1][key][x], R[a + k][key][x]
                        if p != q and q[2] < k:
                            C[tag + "_V"] += 1; C[tag + "_V_D%d" % min(D, 3)] += 1
                            if len([e for e in EX if e[0] == tag]) < 4: EX.append((tag, name, a, b, k, x, p, q, D))

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
                except Exception as e: C["SKIPPED_input"] += 1
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    print("max L/(n-1) = %.3f" % MX[0], MX[1])
    for z in EX: print("EXAMPLE (tag, game, a, b, k, x, before, after, |D|)", z)
    for k in ("RD", "RDX"): print(k, "PASS" if k + "_V" not in C else "FAIL")

if __name__ == "__main__":
    main()
