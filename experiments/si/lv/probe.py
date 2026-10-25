#!/usr/bin/env python3
"""L-SI succ. 7, box 12: print the anatomy of in-scope THR fallbacks (run states): o, t = τ(o), x0 = σ̄(o), c, r, the gates (level,
kind), the W-improving non-gate edges, and the U-play from x0 (U = Even's optimal valuation against τ = Ξτ read in G's order).
Usage: probe.py MAX game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import betasearch as B
from betasearch import *

def show(g, o, a, E, Ed):
    s, t = a["s"], a["t"]; Xi, W, R = a["Xi"], a["W"], a["R"]; Rb = R | {o}
    vt, tb = Ed.evaluate(tuple(t)); U = vt
    x0 = a["sb"][o]; c = Xi[o][0]; r = lev(Xi[o], W[o])
    print(f"  o={o} t={t[o]} x0={x0} c={c} r={r} rank: o<c? {o_rank(g,o) < o_rank(g,c)}  |R|={len(R)} n={g.n}")
    for y, z in a["Is"]:
        l = lev(Xi[s[y]], Xi[z]); kind = ("R" if y in R else "F") + ("R̄" if s[y] in Rb else "F") + "->" + ("R̄" if z in Rb else "F")
        print(f"    gate ({y},{z}) lev {l} {kind}  Wimp={E.key(W[z]) > E.key(W[s[y]])}")
    wi = [(q, e) for q in range(g.n) if g.owner[q] == 0 for e in set(g.succ[q]) if e != s[q] and E.key(W[e]) > E.key(W[s[q]]) and (q, e) not in a["Is"]]
    print(f"    W-improving non-gates: {[(q,e,'q'+('R̄' if q in Rb else 'F')+' e'+('R̄' if e in Rb else 'F')) for q,e in wi]}")
    # U-play from x0 under Even's optimal (tb is dual-Odd's choice = Even's choice) and tau
    nxt = lambda v: tb[v] if g.owner[v] == 0 else t[v]
    p = [x0]; 
    while nxt(p[-1]) not in p: p.append(nxt(p[-1]))
    print(f"    U-play x0: {p} -> {nxt(p[-1])};  U(x0)={U[x0][:1]} U(t)={U[t[o]][:1]}  diff-from-σ at {[v for v in p if g.owner[v]==0 and tb[v]!=s[v]]}")

def o_rank(g, v): return sorted(range(g.n), key=lambda u: (g.prio[u], u)).index(v)

if __name__ == "__main__":
    mx = int(sys.argv[1]); cnt = 0
    for p in sys.argv[2:]:
        g = load(p); o = odd_choice(g)
        if o is None: continue
        E, Ed = n5.Engine(g), n5.Engine(n5.dual(g)); B.E_key = E.key
        try: _, out = states(g)
        except AssertionError: continue
        for i in range(len(out) - 1):
            a = info(g, E, Ed, o, out[i]["s"], out[i]["t"]); 
            if not a["fb"]: continue
            b = info(g, E, Ed, o, out[i + 1]["s"], out[i + 1]["t"]); c = classify(g, o, a, b)
            if not isinstance(c, tuple): continue
            print(p, "state", i, "M", c[1]); show(g, o, a, E, Ed); cnt += 1
            if cnt >= mx: sys.exit()
