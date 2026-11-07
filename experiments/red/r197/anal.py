#!/usr/bin/env python3
"""L-RED R197 ANAL: per W-level l of a width-w ladder genome: F_l (flips of the key ranking R_l), moves at level l, delayed moves
(level-l moves at steps where R_(l-1) did not flip), and for LAG moves the W-level offsets of their wakers (waker level - mover level).
Usage: anal.py w genome.json ..."""
import sys, os, json, collections
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import ideal
def run(G, w):
    S, why = ideal.traj(G, cap=20000); N = G["N"]; O = G["opts"]; lev = G["lev"]; d = max(lev) + 1
    def keys(s):
        key = [None] * N
        for v in sorted(range(N), key=lambda v: lev[v]):
            wt = O[v][s[v]][0]; key[v] = ((G["gate"][v][s[v]],) if wt < 0 else key[wt] + (G["gate"][v][s[v]],))
        return key
    K = [keys(s) for s in S]
    R = [[tuple(sorted(range(w * l, w * l + w), key=lambda v: k[v])) for l in range(d)] for k in K]
    desc = []
    for v in range(N):
        seen = set(); st = [v]
        while st:
            x = st.pop()
            for (_, xt, _) in O[x]:
                if xt >= 0 and xt not in seen: seen.add(xt); st.append(xt)
        desc.append(seen)
    def korder(t, x):
        return tuple(sorted(range(len(O[x])), key=lambda k: (G["gate"][x][k],) if O[x][k][0] < 0 else K[t][O[x][k][0]] + (G["gate"][x][k],)))
    mv = [set()] + [{v for v in range(N) if S[t][v] != S[t - 1][v]} for t in range(1, len(S))]
    F = [sum(R[t][l] != R[t - 1][l] for t in range(1, len(S))) for l in range(d)]
    M = [sum(len([v for v in mv[t] if lev[v] == l]) for t in range(1, len(S))) for l in range(d)]
    Dl = [0] * d; off = collections.Counter(); lagn = 0
    for t in range(1, len(S)):
        for v in mv[t]:
            l = lev[v]
            if l >= 1 and R[t][l - 1] == R[t - 1][l - 1]: Dl[l] += 1
            if t >= 2 and v not in mv[t - 1] and korder(t - 1, v) == korder(t, v):
                lagn += 1
                for y in mv[t - 1] & desc[v]: off[lev[y] - l] += 1
    return len(S) - 1, why, F, M, Dl, lagn, off
if __name__ == "__main__":
    w = int(sys.argv[1])
    for f in sys.argv[2:]:
        L, why, F, M, Dl, lagn, off = run(json.load(open(f)), w)
        print(os.path.basename(f), "L", L, why, "F", F, "moves", M, "DELAY", Dl, "LAG", lagn, "waker-level offsets", dict(sorted(off.items())))
