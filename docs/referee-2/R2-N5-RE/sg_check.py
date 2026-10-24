#!/usr/bin/env python3
"""REFEREE-2 check of the uniform strict-gain step that replaces (NC) (R2-N5-RE §4):
  (SG) at ANY N5 transition k -> k+1, every Even vertex y with sigma_{k+1}(y) != sigma_k(y) and lambda_k(y) != y
       has Xi_{k+1}(y) strictly better than Xi_k(y).  No (h), no phase, no tau condition.
Also (SG-cyc): the same at switched y with lambda_k(y) = y (own cycle node) is NOT claimed; counted as a control (flat switches).
Usage: sg_check.py N nmin nmax seed [own|spec] [cyc|any]"""
import sys, random
from collections import Counter
import re_check as rc

def main():
    N, nmin, nmax, seed = map(int, sys.argv[1:5])
    mode = sys.argv[5] if len(sys.argv) > 5 else "own"
    cyc = (sys.argv[6] if len(sys.argv) > 6 else "cyc") == "cyc"
    rng = random.Random(seed); c = Counter(); bad = []
    for i in range(N):
        g, o = rc.rand_game(rng, rng.randint(nmin, nmax), cyc)
        s, t = rc.rand_start(rng, g)
        states, fbs = rc.n5_spec(g, o, s, t) if mode == "spec" else rc.n5_own(g, o, s, t, rng)
        A = [rc.analyse(g, o, *x) for x in states]
        for k in range(len(states) - 1):
            for y in range(g.n):
                if g.owner[y] != 0 or A[k].f[y] == A[k + 1].f[y]: continue
                gain = g.cmp(A[k + 1].Xi[y], A[k].Xi[y])
                if A[k].lamX[y] != y:
                    c["SG_checks"] += 1
                    c["SG_checks_fallback" if fbs[k] else "SG_checks_arena"] += 1
                    if A[k].lamX[y] == A[k + 1].lamX[y]: c["SG_checks_same_lambda"] += 1
                    if gain <= 0:
                        c["SG_VIOLATIONS"] += 1
                        if len(bad) < 10: bad.append(f"seed{seed}#{i} k={k} y={y}")
                else:
                    c["control_own_cycle_node_switches"] += 1
                    if gain == 0: c["control_own_cycle_node_flat"] += 1
    for k in sorted(c): print(f"{k}: {c[k]}")
    for b in bad: print("VIOLATION", b)
    print("RESULT", "FAIL" if c["SG_VIOLATIONS"] else "OK", f"violations={c['SG_VIOLATIONS']}")

if __name__ == "__main__":
    main()
