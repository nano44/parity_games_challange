#!/usr/bin/env python3
"""L-NEW box 177: per-mover move bounds and their slack on real runs (stored start; degree <= 2 genomes).
 KF   : 1 + KF_x                            (R105 KEYFLIP; = 1 + flips of x's W-target pair by PAIR-KF)
 RET  : 1 + R(x,0) + R(x,1)                 (P-IDEAL-KEYS RETURN-COUNT; R = #rises of cv(Xi-target))
 PATH : 1 + (P(xt0) - 1) + (P(xt1) - 1)     (box 177 PATH-RISE: rises of cv(z) <= P(z) - 1, P(z) = #maximal Xi-paths from z; P(X) = 1)
 JOINT: 1 + #consecutive-move windows ... = moves (exact), printed with the number of windows that contain a KP flip AND a rise
 Per level l (two-option movers 2l, 2l+1 when the file is 2-wide in that convention): F(l) = flips of (2l, 2l+1).
Usage: slack.py files..."""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P, "__name__": "lib"}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
def paths(G):
    N = G["N"]; memo = {}
    def p(z):
        if z < 0: return 1
        if z not in memo: memo[z] = sum(p(o[1]) for o in G["opts"][z])
        return memo[z]
    return p
for f in sys.argv[1:]:
    G = json.load(open(f)); N = G["N"]; g = Gen(G); S, _ = g.run(G["start"]); T = len(S) - 1; pp = paths(G)
    K = [g.keys(s) for s in S]
    kp = [[min(range(len(G["opts"][x])), key=lambda k: g.optkey(K[t], x, k)) for x in range(N)] for t in range(T + 1)]
    cv = [[g.face(S[t], z, S[t][z]) for z in range(N)] for t in range(T + 1)]
    print("== %s N %d T %d" % (os.path.basename(f), N, T))
    two = [x for x in range(N) if len(G["opts"][x]) == 2]; levs = sorted(set(G["lev"][x] for x in two))
    viol = 0; rows = []
    for x in two:
        mv = [t for t in range(1, T + 1) if S[t][x] != S[t - 1][x]]; KF = sum(1 for t in range(1, T + 1) if kp[t][x] != kp[t - 1][x])
        R = []; Pb = []
        for k in (0, 1):
            z = G["opts"][x][k][1]
            R.append(0 if z < 0 else sum(1 for t in range(1, T + 1) if cv[t][z] > cv[t - 1][z])); Pb.append(pp(z) - 1)
            if z >= 0 and R[-1] > pp(z) - 1: viol += 1
        both = sum(1 for i in range(1, len(mv)) if any(kp[t][x] != kp[t - 1][x] for t in range(mv[i - 1] + 1, mv[i] + 1))
                   and any(cv[t][G["opts"][x][kk][1]] > cv[t - 1][G["opts"][x][kk][1]] for kk in (0, 1) if G["opts"][x][kk][1] >= 0
                           for t in range(mv[i - 1], mv[i])))
        rows.append((G["lev"][x], x, len(mv), 1 + KF, 1 + sum(R), 1 + sum(Pb), both))
    for r in sorted(rows): print("  lev %d x %2d moves %2d | KF-bound %2d RET-bound %2d PATH-bound %4d | windows with flip+rise %d" % r)
    if all(G["lev"][2 * l] == l and G["lev"][2 * l + 1] == l for l in levs if 2 * l + 1 < N):
        F = [sum(1 for t in range(1, T + 1) if (K[t][2 * l] < K[t][2 * l + 1]) != (K[t - 1][2 * l] < K[t - 1][2 * l + 1])) for l in levs]
        print("  F(l) by level", F)
    print("  PATH-RISE violations", viol)
