#!/usr/bin/env python3
"""Returns of Even vertices inside (theta, w, tau, joint-lambda)-constant stretches of N5 runs on one-Odd-choice games
(box 21 §3.6's stretches): theta = Xi(o) honest, w = W(o) = value of the (sigma, tau)-play from o.
A return = x switches back to an edge it left earlier in the same stretch.  Prints per instance: longest stretch,
returns inside stretches, max per stretch, and the same counts per joint lambda-phase for comparison."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortrace as OT
def playval(E, sig, tau, v):
    seen = {}; path = []; x = v
    while x not in seen:
        seen[x] = len(path); path.append(x)
        x = sig[x] if E.owner[x] == 0 else tau[x]
    cyc = path[seen[x]:]; c = max(cyc, key=lambda u: E.rank[u])
    pre = path[:path.index(c)]
    P = 0
    for u in pre:
        if E.rank[u] > E.rank[c]: P |= E.bit[u]
    return (c, P, len(pre))
def segs(keys):
    out = []; cur = [0]
    for i in range(1, len(keys)):
        if keys[i] == keys[i - 1]: cur.append(i)
        else: out.append(cur); cur = [i]
    out.append(cur); return out
def returns_in(states, idxs, g):
    left = {}; r = 0
    for a, b in zip(idxs, idxs[1:]):
        s0, s1 = states[a][0], states[b][0]
        for x in range(g.n):
            if g.owner[x] == 0 and s0[x] != s1[x]:
                left.setdefault(x, set()).add(s0[x])
                if s1[x] in left[x]: r += 1
    return r
def run(path, start=None):
    g, st = OT.load(path, start)
    E, Ed, states, fbf, (it, fb) = OT.run_states(g, st)
    odd = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1]
    o = odd[0]
    keys = []
    for (sig, tau, vs, sbar, vt, tbar, Is, It) in states:
        lam = (tuple(v[0] for v in vs), tuple(v[0] for v in vt))
        keys.append((tau, vs[o], playval(E, sig, tau, o), lam))
    S = segs(keys)
    rs = [returns_in(states, s, g) for s in S]
    P = segs([k[3] for k in keys]); rp = [returns_in(states, s, g) for s in P]
    return g.n, it, odd, max(len(s) - 1 for s in S), sum(rs), max(rs), sum(rp), max(len(s) - 1 for s in P)
if __name__ == "__main__":
    for spec in sys.argv[1:]:
        p, _, s = spec.partition(":")
        n, it, odd, ls, rs, mrs, rp, lp = run(p, s or None)
        print(f"{os.path.basename(p):22s} n={n:3d} it={it:4d} odd={odd} longest stretch={ls:3d} returns in stretches={rs} (max {mrs}) | longest phase={lp} returns in phases={rp}", flush=True)
