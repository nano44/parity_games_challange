#!/usr/bin/env python3
"""L-RED successor 27: carries per vertex per lambda-RUN (NM*) and per JOINT lambda-run, with L-COMP's nm.py functions imported
unchanged (nm.matched, nm.wmap, box17 trajectory). nm.py itself cuts by its key r38 = (lambda_Xi, tau), i.e. per phase; this wrapper only
changes the grouping: lambda-run = lambda_Xi constant (tau free); joint = (lambda_Xi, lambda of Xi_tau on G^d) constant.
For the Odd side (NM*^U) run it on G^d with the swapped start (ctl/dualize.py): N5 on G^d mirrors N5 on G (R111), and G^d's Xi is G's U.
Usage: nmrun.py GAME START|S3"""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(EXP, "n5-box18")); sys.path.insert(0, os.path.join(EXP, "n5-box17"))
import nm, box17 as B


def blocks(keys):
    i = 0
    while i < len(keys):
        j = i
        while j + 1 < len(keys) and keys[j + 1] == keys[i]:
            j += 1
        yield i, j
        i = j + 1


def measure(gp, sp):
    g = nm.load(gp); e = B.Eng(g); st = nm.startof(g, e, sp) if sp not in (None, "S3") else None
    R = B.trajectory(e, st or e.start()); w = nm.wmap(g)
    lam = [r["key"][0] for r in R]
    lamU = [tuple(x[0] for x in e.N.SD.evaluate(list(r["t"]))) for r in R]
    out = {}
    for name, keys in (("phase_r38", [r["key"] for r in R]), ("lambda_run", lam), ("joint_run", list(zip(lam, lamU)))):
        best = dict(nm=0, pch=0, v=None, run=None)
        for i, j in blocks(keys):
            for v in range(g.n):
                pch = nmc = 0
                for t in range(i, j):
                    A, Bs = R[t]["xi"][v][1], R[t + 1]["xi"][v][1]
                    if A != Bs:
                        pch += 1; nmc += not nm.matched(A, Bs, w)
                if (nmc, pch) > (best["nm"], best["pch"]):
                    best = dict(nm=nmc, pch=pch, v=v, run=(i, j))
        out[name] = best
    return g, R, out


if __name__ == "__main__":
    g, R, out = measure(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "S3")
    print("n", g.n, "states", len(R), json.dumps(out))
