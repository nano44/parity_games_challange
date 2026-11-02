#!/usr/bin/env python3
"""L-RED R189 DELAY: L-NEW box 142 DELAY-CHARGE on a 2-wide LADDER genome: F_l = flips of L_l (key-smaller of u_l, v_l) along the IDEAL
run; DELAY_l = level-l moves strictly after a flip step of L_(l-1) and before its next flip (moves not at a carry step); checks
F_l <= F_(l-1) + 2 + DELAY_l for l >= 1. Usage: delay.py genome.json ..."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "..", "r187"), os.path.join(H, "..", "..", "r178")]
import ideal
for f in sys.argv[1:]:
    G = json.load(open(f)); S, why = ideal.traj(G); N = G["N"]; lev = G["lev"]; d = max(lev) + 1; O = G["opts"]
    def keys(s):
        key = [None] * N
        for v in sorted(range(N), key=lambda v: lev[v]):
            wt = O[v][s[v]][0]; key[v] = ((G["gate"][v][s[v]],) if wt < 0 else key[wt] + (G["gate"][v][s[v]],))
        return key
    Ls = [[min((2 * l, 2 * l + 1), key=lambda v: K[v]) for l in range(d)] for K in (keys(s) for s in S)]
    F = [sum(Ls[t][l] != Ls[t - 1][l] for t in range(1, len(S))) for l in range(d)]
    D = [0] * d
    for l in range(1, d):
        carry = {t for t in range(1, len(S)) if Ls[t][l - 1] != Ls[t - 1][l - 1]}
        D[l] = sum(1 for t in range(1, len(S)) for v in (2 * l, 2 * l + 1) if S[t][v] != S[t - 1][v] and t not in carry)
    viol = [l for l in range(1, d) if F[l] > F[l - 1] + 2 + D[l]]
    print(f"DELAY {os.path.basename(f)} L {len(S) - 1} F {F} DELAY {D} sumDELAY {sum(D)} viol {viol}")
