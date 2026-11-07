#!/usr/bin/env python3
"""L-RED R187 IDEAL trajectory: r178/fastcyc.simulate, returning the state sequence (option index per mover) and, per step, the
movers. Same rule (TB lex-min key over the gate indices, availability = current or strictly Xi-better face). Lib only."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r178"))
import fastcyc
def traj(G, cap=100000):
    N, lev, opts, gate = G["N"], G["lev"], G["opts"], G["gate"]
    order = sorted(range(N), key=lambda v: lev[v]); s = list(G["start"]); S = [tuple(s)]
    while len(S) - 1 < cap:
        val, idx, _, M = fastcyc.values(G, s)
        face = lambda v, k: val(N + idx[(v, k)])
        cur = [face(v, s[v]) for v in range(N)]
        avail = [[k for k in range(len(opts[v])) if k == s[v] or face(v, k) > cur[v]] for v in range(N)]
        if all(len(a) == 1 for a in avail): return S, "opt"
        key = [None] * N; ns = list(s)
        for v in order:
            best = None
            for k in avail[v]:
                wt = opts[v][k][0]; kk = ((gate[v][k],) if wt < 0 else key[wt] + (gate[v][k],))
                if best is None or kk < best[0]: best = (kk, k)
            key[v] = best[0]; ns[v] = best[1]
        if ns == s: return S, "stuck"
        s = ns; S.append(tuple(s))
    return S, "cap"
