#!/usr/bin/env python3
"""list every B=2 assignment (bbit.py model) with max moves(x0) > 1 + desc(x0) for the violator; writes out/patterns2.json.
Usage: patterns.py vfile x0"""
import os, sys, json, itertools
H = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(H, "..", "box165", "permover.py")).read().split("\nif __name__")[0])
sys.setrecursionlimit(100000)
V = json.load(open(sys.argv[1])); x0 = int(sys.argv[2]); g = Gen(V); N = V["N"]; R = reach(V); bound = 1 + len(R[x0])
states = list(itertools.product((0, 1), repeat=N)); unh = {s: [x for x in range(N) if len(g.avail(s, x)) == 2] for s in states}
choices = [("c", 0), ("c", 1)] + [("b", i, sg) for i in range(2) for sg in (0, 1)]; out = []
for a in itertools.product(choices, repeat=N):
    used = [v[1] for v in a if v[0] == "b"]
    if 1 in used and (0 not in used or used.index(0) > used.index(1)): continue
    memo = {}
    def f(s):
        if s in memo: return memo[s]
        memo[s] = 0; v = 0
        for bv in itertools.product((0, 1), repeat=2):
            t = list(s)
            for x in unh[s]: t[x] = a[x][1] if a[x][0] == "c" else bv[a[x][1]] ^ a[x][2]
            t = tuple(t)
            if t != s: v = max(v, (t[x0] != s[x0]) + f(t))
        memo[s] = v; return v
    m = max(f(s) for s in states)
    if m > bound: out.append([list(v) for v in a])
json.dump(out, open(os.path.join(H, "out", "patterns2.json"), "w")); print("winning 2-bit patterns", len(out)); print(out[:5])
