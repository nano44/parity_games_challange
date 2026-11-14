#!/usr/bin/env python3
"""control: in the key-free single-switch improvement graph on all 2^N states of a degree-2 genome (edge s -> s with one Xi-unhappy
mover switched; acyclic by MONO-FLIP), the largest number of moves of each mover x on one improving path, against desc(x).
Usage: keylessmv.py file.json ..."""
import os, sys, json, itertools
H = os.path.dirname(os.path.abspath(__file__)); exec(open(os.path.join(H, "permover.py")).read().split("\nif __name__")[0])
sys.setrecursionlimit(100000)
for f in sys.argv[1:]:
    G = json.load(open(f)); g = Gen(G); N = g.N; R = reach(G); states = list(itertools.product((0, 1), repeat=N))
    succ = {s: [s[:x] + (1 - s[x],) + s[x + 1:] for x in range(N) if len(g.avail(s, x)) == 2] for s in states}
    out = []
    for x in range(N):
        memo = {}
        def fm(s):
            if s not in memo: memo[s] = max([(t[x] != s[x]) + fm(t) for t in succ[s]], default=0)
            return memo[s]
        out.append((len(R[x]), max(fm(s) for s in states)))
    print(os.path.basename(f), "desc:maxmoves", " ".join("%d:%d" % o for o in sorted(out)), " PM-excess", max(m - 1 - d for d, m in out))
