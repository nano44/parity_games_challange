#!/usr/bin/env python3
"""L-NEW box 50 (successor 31): phase VC dsig(P) against |D| (Lead 12:22Z). Per phase P (lambda_Xi, tau constant): dsig(P) = VC of
{sigma_t^E : t in P} (vcrun.vc), len(P), Dmax = max over states of P of |D_t|, D_t = Odd vertices with sigma-bar_t != tau (common.Dset), n.
Usage: phvc.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE)
for p in ("root", "runlin"): sys.path.insert(0, os.path.join(ROOT, "experiments", "si", p))
from common import rows, load, readstart, phases, Dset
from vcrun import vc
C = Counter(); TOP = []

def one(g, name, start=None):
    E, R = rows(g, start); n = g.n; ev = [v for v in range(n) if g.owner[v] == 0 and len(set(g.succ[v])) >= 2]
    for i, j in phases(R):
        if j <= i: continue
        d, m, nf, w = vc([frozenset((v, R[k]["s"][v]) for v in ev) for k in range(i, j + 1)])
        D = max(len(Dset(g, R[k])) for k in range(i, j + 1)); C["phases"] += 1
        C["dsigP_max"] = max(C["dsigP_max"], d); C["Dmax"] = max(C["Dmax"], D)
        C["dsigP_max_D1"] = max(C["dsigP_max_D1"], d if D == 1 else 0)
        TOP.append((d, D, j - i, n, m, name, i, j))

def main():
    a = sys.argv[1:]
    if a[0] == "--one": one(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if p:
                X = lambda q: os.path.join(ROOT, "experiments", q)
                try: one(load(X(p[0])), p[0], readstart(X(p[1])) if len(p) > 1 and os.environ.get("START") == "1" else None)
                except Exception as ex: C["ERR"] += 1; print("ERR", p[0], repr(ex)[:80])
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for x in sorted(TOP, key=lambda x: (-x[1], -x[2]))[:6]: print("TOP-D dsig(P) %d |D| %d len %d n %d m %d %s [%d,%d]" % x)
    for x in sorted(TOP, key=lambda x: (-x[2], -x[0]))[:6]: print("TOP-LEN dsig(P) %d |D| %d len %d n %d m %d %s [%d,%d]" % x)
    for x in sorted(TOP, key=lambda x: (-x[0], -x[2]))[:4]: print("TOP-VC dsig(P) %d |D| %d len %d n %d m %d %s [%d,%d]" % x)

if __name__ == "__main__":
    main()
