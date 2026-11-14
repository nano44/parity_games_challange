#!/usr/bin/env python3
"""B-bit key model: each mover x reads KP_t(x) = b_t[i(x)] XOR sgn(x), or a constant; the bit vector b_t in {0,1}^B is free at every
step (unlimited flips). Dynamics as onebit.py. B >= N gives FREE-KP (= key-free subset dynamics). Exact max of moves(x0) over
assignments (bit indices canonical up to renaming), starts and bit sequences. Usage: bbit.py vfile x0 B"""
import os, sys, json, itertools
H = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(H, "..", "box165", "permover.py")).read().split("\nif __name__")[0])
sys.setrecursionlimit(100000)
V = json.load(open(sys.argv[1])); x0 = int(sys.argv[2]); B = int(sys.argv[3])
g = Gen(V); N = V["N"]; states = list(itertools.product((0, 1), repeat=N)); unh = {s: [x for x in range(N) if len(g.avail(s, x)) == 2] for s in states}
bits = list(itertools.product((0, 1), repeat=B))
def canon(a):  # bit indices in order of first use
    seen = {}; 
    for v in a:
        if v[0] == "b" and v[1] not in seen: seen[v[1]] = len(seen)
    return all(seen.get(i, -1) == j for j, i in enumerate(sorted(seen, key=lambda i: [k for k, v in enumerate(a) if v[0] == "b" and v[1] == i][0]))) and sorted(seen) == list(range(len(seen)))
choices = [("c", 0), ("c", 1)] + [("b", i, sg) for i in range(B) for sg in (0, 1)]
best = (0, None); cnt = 0
for a in itertools.product(choices, repeat=N):
    if not canon(a): continue
    cnt += 1; memo = {}
    def f(s):
        if s in memo: return memo[s]
        memo[s] = 0; v = 0
        for bv in bits:
            t = list(s)
            for x in unh[s]: t[x] = a[x][1] if a[x][0] == "c" else bv[a[x][1]] ^ a[x][2]
            t = tuple(t)
            if t != s: v = max(v, (t[x0] != s[x0]) + f(t))
        memo[s] = v; return v
    m = max(f(s) for s in states)
    if m > best[0]: best = (m, a)
R = reach(V)
print("BBIT", os.path.basename(sys.argv[1]), "x0", x0, "desc", len(R[x0]), "B", B, "assignments", cnt, "max moves(x0)", best[0], "bound", 1 + len(R[x0]), "assignment", best[1])
