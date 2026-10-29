#!/usr/bin/env python3
"""L-NEW box 51 (successor 32): cache the N5 run of one game for the VC-PHASE pattern probes. Per state k: sigma, tau, Is (Even's improving
edges, S2), W keys (E.key of the (sigma, tau)-play valuation, larger = better for Even), Xi keys, fb (fallback flag of the transition leaving k),
and the phases (lambda_Xi, tau constant; common.phases). Engine: experiments/si/root/common.rows (n5x, read-only).
Usage: dump.py GAME [START] -> experiments/new/out/box51/<basename>.pkl"""
import sys, os, pickle
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
from common import rows, load, readstart, phases

def dump(path, start=None, save=True):
    g = load(path); E, R = rows(g, readstart(start) if start else None)
    st = []
    for A in R:
        Is = sorted(E.improving(tuple(A["s"]), A["vs"]))
        st.append(dict(s=A["s"], t=A["t"], Is=Is, W=[E.key(x) for x in A["W"]], X=[E.key(x) for x in A["vs"]], fb=A["fb"],
                       Wv=A["W"]))
    out = dict(n=g.n, owner=list(g.owner), prio=list(g.prio), succ=[sorted(set(x)) for x in g.succ], rank=E.rank, st=st,
               ph=list(phases(R)), name=os.path.basename(path))
    if not save: return out
    d = os.path.join(ROOT, "experiments", "new", "out", "box51"); os.makedirs(d, exist_ok=True)
    f = os.path.join(d, os.path.basename(path)[:-3] + ".pkl"); pickle.dump(out, open(f, "wb")); print(f, len(st), "states", out["ph"])

if __name__ == "__main__":
    dump(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
