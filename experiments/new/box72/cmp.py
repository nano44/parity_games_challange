#!/usr/bin/env python3
"""L-NEW box 72: compare gxc.py runs of N5 (gxc_*.txt) and N5-LZ (gxclz_*.txt): iterations, fallbacks, GXC categories, per-n ratios."""
import re, ast, sys
from collections import Counter
def rd(fs):
    D = {}
    for f in fs:
        for l in open(f):
            key = " ".join(l.split(" GXC ")[0].split()[1:]) + "|" + f.split("_")[-1]
            g = dict(n=int(re.search(r" n (\d+)", l).group(1)), it=int(re.search(r"iters (\d+)", l).group(1)),
                     fb=int(re.search(r"fallbacks (\d+)", l).group(1)) if "fallbacks" in l else None,
                     ev=int(re.search(r"events (\d+)", l).group(1)), run=int(re.search(r" run (\d+)", l).group(1)),
                     cat=Counter(ast.literal_eval(re.search(r"cat (\{.*?\}) s4a", l).group(1))),
                     fbo=int(re.search(r"fbopen (\d+)", l).group(1)), fbop=int(re.search(r"fbopen-per-phase (\d+)", l).group(1)),
                     cv=int(re.search(r"close_viol (\d+)", l).group(1)), tb=int(re.search(r"tie_bad (\d+)", l).group(1)))
            D[key] = g
    return D
X = sys.argv[1] if len(sys.argv) > 1 else "gxclz"
A = rd(["gxc_sbcg.txt", "gxc_alt.txt"]); B = rd([X + "_sbcg.txt", X + "_alt.txt"])
assert A.keys() == B.keys(), (len(A), len(B))
for name, D in (("N5", A), ("N5-LZ", B)):
    cat = sum((d["cat"] for d in D.values()), Counter())
    print(name, "runs", len(D), "iters", sum(d["it"] for d in D.values()), "fallbacks", sum(d["fb"] or 0 for d in D.values()),
          "GXC", sum(d["ev"] for d in D.values()), "maxGXC/run", max(d["run"] for d in D.values()), "fbopen", sum(d["fbo"] for d in D.values()),
          "max fbopen/phase", max(d["fbop"] for d in D.values()), "close_viol", sum(d["cv"] for d in D.values()), "tie_bad", sum(d["tb"] for d in D.values()))
    print("   cats", dict(cat))
    print("   max iters/n", max((d["it"] / d["n"], k) for k, d in D.items()))
w = sorted(((B[k]["it"] - A[k]["it"], k, A[k]["it"], B[k]["it"]) for k in A))
print("LZ longer in", sum(1 for x in w if x[0] > 0), "shorter in", sum(1 for x in w if x[0] < 0), "same", sum(1 for x in w if x[0] == 0))
print("worst LZ - N5:", w[-5:]); print("best:", w[:3])
