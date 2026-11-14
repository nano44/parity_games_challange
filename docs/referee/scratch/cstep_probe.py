#!/usr/bin/env python3
"""REFEREE successor 24: own c-step from RESULTS R110's text (P-IDEAL-IM review). c-step: movers 0, 1 kept; every mover of level >= 1
takes the key-least option of its A-set under the OLD state (my t3r_sim value / better, R104 set order), keys under the NEW state, lowest
level first; a level-1 option W-pointing to mover w is keyed (kappa^c_w, its own gate), kappa^c_0 = 1 - c, kappa^c_1 = c; a level-l >= 2
option is keyed by the key of its W-target's option under the new state followed by its own gate.
T_1 of a genome from a start: max over c1, c2 and the switch time of the number of upper-changing steps (<= 1 bit change).
Usage: python3 -I cstep_probe.py genome.json"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t3r_sim as R

def cstep(G, u, c):
    N = G["N"]; new = list(u); keys = {}
    def key(x, k):
        w = G["opts"][x][k][0]
        if G["lev"][x] == 1: return ((1 - c) if w == 0 else c, G["gate"][x][k])
        return keys[w] + (G["gate"][x][k],)
    for l in sorted(set(G["lev"])):
        if l == 0: continue
        for x in [y for y in range(N) if G["lev"][y] == l]:
            cur = R.value(G, u, x, u[x])
            A = [k for k in range(len(G["opts"][x])) if k == u[x] or R.better(G, R.value(G, u, x, k), cur)]
            new[x] = min(A, key=lambda k: key(x, k))
        for x in [y for y in range(N) if G["lev"][y] == l]:
            keys[x] = key(x, new[x])
    return tuple(new)

def fix_run(G, u, c, cap=10000):
    seq = [u]
    while True:
        n = cstep(G, seq[-1], c)
        if n == seq[-1] or len(seq) > cap: return seq
        seq.append(n)

if __name__ == "__main__":
    G = json.load(open(sys.argv[1])); s0 = tuple(G["start"])
    iso = all(o[1] not in (0, 1) for x in range(G["N"]) for o in G["opts"][x])
    print("N", G["N"], "inLR", R.in_LR(G, G["N"] // 2), "ISO", iso)
    best = (0, None)
    for c1 in (0, 1):
        A = fix_run(G, s0, c1)
        for tau in range(len(A)):                 # switch after tau changing steps of c1
            for c2 in (0, 1):
                B = fix_run(G, A[tau], c2)
                tot = tau + len(B) - 1
                if tot > best[0]: best = (tot, (c1, tau, c2))
    print("T_1 from stored start (my c-step):", best)
    for c in (0, 1): print("T_0 with c =", c, ":", len(fix_run(G, s0, c)) - 1)
