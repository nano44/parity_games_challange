#!/usr/bin/env python3
"""L-RED box 11 (produced on Opus 5.5): lean Two Counters. From tc(N) (pinned generator) delete every S/A/B vertex; an edge into
X-i-S-j is redirected to X-i-Z (the chain end), other edges into deleted vertices are dropped; then apply a tcpert rule set
(default tcL). Prints n and pinned-Oink iterations; writes OUT.pg. Usage: lean.py N OUT.pg [RULENAME]"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tcpert as T
def lean(N, rule):
    V = T.gen(N); L = [T.lab(v[3]) for v in V]
    keep = [k for k, l in enumerate(L) if l[2] not in ("S", "A", "B")]; new = {k: i for i, k in enumerate(keep)}
    zof = {(l[0], l[1]): k for k, l in enumerate(L) if l[2] == "Z"}
    W = []
    for k in keep:
        a, b, su, nm = V[k]; out = []
        for w in su:
            if w in new: out.append(new[w])
            elif L[w][2] == "S": out.append(new[zof[(L[w][0], L[w][1])]])
        W.append([a, b, sorted(set(out)) or [new[k]], nm])
    return T.apply(W, rule)
if __name__ == "__main__":
    N = int(sys.argv[1]); V = lean(N, T.RULES.get(sys.argv[3], ()) if len(sys.argv) > 3 else T.TCL)
    print(N, len(V), T.solve(V, sys.argv[2]))   # solve() also writes V to OUT.pg
