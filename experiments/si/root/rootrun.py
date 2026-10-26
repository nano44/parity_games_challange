#!/usr/bin/env python3
"""L-SI box 20 (successor 16): DATA for note §29 (Corollary ROOT-RUN). For the phase and Odd choice vertex r with the most rho events (as
rootdyn.py), class c, U := lambda^-1(c), A_t := F_D(t) cap U. The phase is cut at fallback transitions and at S4a transitions with
A_t+1 not a subset of A_t (A-gains; each is tagged DLEAVE if every entering vertex's first D-vertex left D, else SWITCH). On each piece
[s, e] (A non-increasing, no fallback) count the transitions with r D-direct (sigma-bar(r) in A) at both ends and M(r) changing (rhoP) and
with Xi(r) changing (rho), against FREEZE-A (c)'s bound B := (|A_s| - 1) + (deg(r) - 1) for rhoP (ROOTRUN_V counts pieces over B).
Control MUT=1: bound 2 in place of B (must bite on nep90).
Usage: rootrun.py GAME [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from common import *


def main():
    g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None
    E, R = rows(g, st); Q = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]
    best = None
    for i, j in phases(R):
        for q in Q:
            rq = sum(E.key(R[k]["vs"][q]) != E.key(R[k + 1]["vs"][q]) for k in range(i, j))
            if best is None or rq > best[0]: best = (rq, i, j, q)
    rq, i, j, r = best; c = R[i]["vs"][r][0]; U = {v for v in range(g.n) if R[i]["vs"][v][0] == c}
    A = {k: avoid(R[k]["wn"], Dset(g, R[k]), g.n) & U for k in range(i, j + 1)}
    cuts = []
    for k in range(i, j):
        if R[k]["fb"]: cuts.append((k, "fb"))
        elif not A[k + 1] <= A[k]:
            D1 = Dset(g, R[k + 1]); D0 = Dset(g, R[k])
            tag = "DLEAVE" if all(first_D(R[k]["wn"], z, D0) not in D1 for z in A[k + 1] - A[k]) else "SWITCH"
            cuts.append((k, tag))
    pieces, s = [], i
    for k, tag in cuts + [(j, "end")]:
        pieces.append((s, k, tag)); s = k + 1
    viol = 0; tot = 0
    print(f"phase@{i} len={j - i} r={r} c={c} |U|={len(U)} deg(r)={len(set(g.succ[r]))} rho_r={rq} cuts={len(cuts)} "
          f"(fb {sum(1 for _, t in cuts if t == 'fb')}, DLEAVE {sum(1 for _, t in cuts if t == 'DLEAVE')}, SWITCH {sum(1 for _, t in cuts if t == 'SWITCH')})")
    for s, e, tag in pieces:
        if e <= s: continue
        dd = lambda k: R[k]["sb"][r] in A[k]
        rp = sum(1 for k in range(s, e) if dd(k) and dd(k + 1) and M(E, R[k]["vs"][r]) != M(E, R[k + 1]["vs"][r]))
        rh = sum(1 for k in range(s, e) if E.key(R[k]["vs"][r]) != E.key(R[k + 1]["vs"][r]))
        B = (len(A[s]) - 1) + (len(set(g.succ[r])) - 1)
        if os.environ.get("MUT") == "1": B = 2
        viol += rp > B; tot += rh
        print(f"  piece [{s - i},{e - i}] len={e - s} ended_by={tag} |A_s|={len(A[s])} rhoP_r={rp} rho_r={rh} bound={B}")
    print(f"ROOTRUN_V={viol} rho_in_pieces={tot}")

if __name__ == "__main__":
    main()
