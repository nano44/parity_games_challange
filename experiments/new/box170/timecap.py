#!/usr/bin/env python3
"""key-free SUBSET dynamics (= FREE-KP, box 166): at each step any nonempty subset of the Xi-unhappy movers switches. Exact max of
moves(top) within at most k steps, over all starts, k = 1..K. An upper bound for every keyed realization that must fit into k steps
(no keyed run can do better than free key preferences). Usage: timecap.py gadget.json K"""
import os, sys, json, itertools
H = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(H, "..", "box165", "permover.py")).read().split("\nif __name__")[0])
V = json.load(open(sys.argv[1])); K = int(sys.argv[2]); g = Gen(V); N = V["N"]; R = reach(V); top = max(range(N), key=lambda x: len(R[x]))
states = list(itertools.product((0, 1), repeat=N)); unh = {s: [x for x in range(N) if len(g.avail(s, x)) == 2] for s in states}
succ = {}
for s in states:
    out = set()
    for r in range(1, len(unh[s]) + 1):
        for sub in itertools.combinations(unh[s], r):
            t = list(s)
            for x in sub: t[x] ^= 1
            out.add(tuple(t))
    succ[s] = list(out)
f = {s: 0 for s in states}
res = []
for k in range(1, K + 1):
    f = {s: max([(t[top] != s[top]) + f[t] for t in succ[s]], default=0) for s in states}
    res.append(max(f.values()))
print(os.path.basename(sys.argv[1]), "top", top, "desc", len(R[top]), "max moves(top) within k steps, k = 1..%d:" % K, res)
