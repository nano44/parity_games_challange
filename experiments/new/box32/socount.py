#!/usr/bin/env python3
"""Box 32: S_o structure (docs/new/N5-L-box32.md §5 (b)). Per phase: relevant σ̄(o) changes (λ(o) != o) split into THETA (θ = Ξ(o) changes
at the same transition) and TIE (θ unchanged); per (phase, θ-value): TIE moves, and whether the old choice left the minimiser set T
(LEAVE) or stayed in it (TB = a pure tie-break move). Also the cycle-node parity mode (longest-path for even c, BFS for odd c).
Usage: socount.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from mblock import *

if __name__ == "__main__":
    acc = {}
    for f in sys.argv[1:]:
        g = load(f); rows, o = rows_w(g); E = Engine(g); ev = [E.evaluate(tuple(r["s"])) for r in rows]; d_o = len(g.succ[o])
        per = {}
        for k in range(len(rows) - 1):
            if rows[k]["ph"] != rows[k + 1]["ph"]: continue
            X0, X1 = ev[k][0], ev[k + 1][0]; s0, s1 = ev[k][1][o], ev[k + 1][1][o]
            if s0 == s1 or X0[o][0] == o: continue
            if X0[o] != X1[o]: acc["THETA"] = acc.get("THETA", 0) + 1; continue
            mode = "even" if g.prio[X0[o][0]] % 2 == 0 else "odd"
            T1 = [x for x in g.succ[o] if X1[x] == X1[s1]]
            kind = "TB" if s0 in T1 else "LEAVE"
            acc[f"TIE_{kind}_{mode}"] = acc.get(f"TIE_{kind}_{mode}", 0) + 1
            key = (rows[k]["ph"], E.key(X0[o])); per[key] = per.get(key, 0) + 1
            if per[key] > acc.get("max_tie_per_theta", (0,))[0]: acc["max_tie_per_theta"] = (per[key], d_o, os.path.basename(f))
    for k in sorted(acc): print(k, acc[k])
