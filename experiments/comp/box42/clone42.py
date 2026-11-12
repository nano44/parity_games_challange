#!/usr/bin/env python3
"""L-COMP box 42 item 1: the C6G8-line FAMILY CL(k) (Lead 11:54Z: «find the family's growth rule by trace … build it at >= 4 sizes»).
Trace (box41 per-gate census of C6G8_n54 -> grown 281 -> D300b best 79f3cd11): the deep internal flips (depth 4-5) occur at a few
steps, each deep change fanning out to the internal gates of several level-1 movers whose face plays pass the changing vertex; mover 10
carries the most (gate (10, 0): 3 deep flips; its options' targets 17, 1, 20, 7, 50 and Ξ-targets 18, 17, 83, 57, 3 lie in the giant SCC;
its only in-edge is option (18, 0), Ξ-target 10). GROWTH RULE (the family): CL(k) := the D300b best plus k CLONES of mover X (= 10): clone
i is a new level-lev(X) mover with copies of X's options (same W- and Ξ-targets, bp, start; gate index and β rank placed just after the
original's: original + i/(k+1) before re-ranking) and one copy of each in-edge option of X (an option with Ξ- or W-target X), retargeted to
the clone (same placement rule). Each clone adds 1 mover and deg(X) + #in-edges options (here 1 + 5 + 1 = 7 to N + M). The clones stay in
the giant SCC (in-edge from 18, out-edges into it). No search: CL(k) is deterministic.
Usage: clone42.py BASE.json X K OUT.json"""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "box39")]
from mut39 import flat, unflat, canon


def clone(G, X, K):
    G = canon(G); N, lev = G["N"], list(G["lev"]); O = flat(G)
    base = [o for o in O if o["x"] == X]; ins = [o for o in O if o["x"] != X and (o["xt"] == X or o["wt"] == X)]
    for i in range(1, K + 1):
        l = lev[X]; p = max(y + 1 for y in range(N) if lev[y] <= l)
        sh = lambda y: y + (y >= p) if y >= 0 else y
        for o in O: o["x"] = sh(o["x"]); o["wt"] = sh(o["wt"]); o["xt"] = sh(o["xt"])
        lev = lev[:p] + [l] + lev[p:]; N += 1
        eps = i / (K + 1)
        for o in base: O.append(dict(x=p, wt=o["wt"], xt=o["xt"], gate=o["gate"] + eps, br=o["br"] + eps, bp=o["bp"], st=o["st"]))
        for o in ins:
            c = dict(o); c["gate"] = o["gate"] + eps; c["br"] = o["br"] + eps; c["st"] = False
            if o["xt"] == base[0]["x"]: c["xt"] = p
            if o["wt"] == base[0]["x"]: c["wt"] = p
            O.append(c)
    return unflat(N, lev, O)


if __name__ == "__main__":
    G = json.load(open(sys.argv[1])); X, K = int(sys.argv[2]), int(sys.argv[3])
    C = clone(G, X, K); json.dump(C, open(sys.argv[4], "w"), sort_keys=True)
    print(sys.argv[4], "N", C["N"], "N+M", C["N"] + sum(map(len, C["opts"])))
