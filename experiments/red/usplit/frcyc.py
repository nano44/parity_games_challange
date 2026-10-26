#!/usr/bin/env python3
"""Box 52 (L-RED successor 20): Friedmann's simple cycles (LMCS 7(3:19) 2011, arXiv 1106.0778 §6.1, Table 1: Even d_i → {e_i} ∪ D_i,
Odd e_i → {d_i, h_i}) under N5 (o1_19.trace, SPEC S1-S5). Per state and cycle: closed (σ(d) = e); for open cycles whether (d, e) is
Ξ-improving (in S4a's arena) and whether W prefers e (W(e) ≻ W(σ(d)), W = valuation against τ). Counts closings, openings, and
'hidden' states (open, (d, e) Ξ-improving, not closed at the next state). Usage: frcyc.py game.pg"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "o1")); sys.path.insert(0, os.path.join(HERE, "..", "rec0"))
import o1_19 as O, pg, rec0_20 as R0
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); n = g.n
cyc = [(d, e) for e in range(n) if g.owner[e] == 1 and len(set(g.succ[e])) == 2 for d in set(g.succ[e]) if g.owner[d] == 0 and e in g.succ[d]]
S, FB, E = O.trace(g, None); K = E.key
r = dict(n=n, cycles=len(cyc), ITER=len(FB), FB=sum(1 for f in FB if f), closings=0, openings=0, hidden=0, open_xi_impr=0, open_not_impr=0, w_tempted_blocked=0)
for k in range(len(S)):
    s, t = S[k]; X, SB = E.evaluate(s); W = [R0.playval(g, E, s, t, x) for x in range(n)]
    for d, e in cyc:
        if s[d] == e:
            if k + 1 < len(S) and S[k + 1][0][d] != e: r["openings"] += 1
            continue
        if k + 1 < len(S) and S[k + 1][0][d] == e: r["closings"] += 1
        impr = K(X[e]) > K(X[s[d]])
        r["open_xi_impr" if impr else "open_not_impr"] += 1
        if impr and k + 1 < len(S) and S[k + 1][0][d] != e: r["hidden"] += 1
        if not impr and K(W[e]) > K(W[s[d]]): r["w_tempted_blocked"] += 1
print(json.dumps(r))
