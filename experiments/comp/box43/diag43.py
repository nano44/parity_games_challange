#!/usr/bin/env python3
"""L-COMP box 43 item 1 (b): the first failure of the lifted box 208 counters, in values. For a game (lmcs N | switchall N), a state t,
a mover x and its successor y: prints Ω_t(y), Ω_t(σ_t(x)), Ω_(t+1)(x) (cycle node, Π by decreasing relevance with priorities, length),
the escapes W, and z := the most relevant vertex of Π_t(y) Δ Π_t(σ_t(x)) with its parity, owner and whether it is an escape: (K2) COARSE
(box 208 §2) needs z to be an e-vertex («by E-DOM z is an e-vertex, c_W, K0 or K3»); here it is not.
Usage: diag43.py lmcs|switchall N t x y"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lev43
kind, N, t, xn, yn = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], sys.argv[5]
g, st, names = (lev43.lmcs if kind == "lmcs" else lev43.switchall)(N); Hs = lev43.howard(g, st); W = lev43.escapes(g)
idx = {nm: i for i, nm in enumerate(names)}; x, y = idx[xn], idx[yn]; rk = lambda v: (g.prio[v], v)
def show(tag, val):
    print("%s: Λ %s, Π [%s], len %d" % (tag, names[val[0]], " ".join("%s:%d%s" % (names[u], g.prio[u], "*" if u in W else "") for u in sorted(val[1], key=rk, reverse=True)), val[2]))
cur = Hs[t][2][x]
print("%s N %d, state %d; escapes W (marked *): %s" % (kind, N, t, " ".join("%s:%d" % (names[u], g.prio[u]) for u in sorted(W, key=rk))))
show("Ω_t(%s) [successor y of %s]" % (yn, xn), Hs[t][0][y]); show("Ω_t(%s) [σ_t(%s)]" % (names[cur], xn), Hs[t][0][cur])
show("Ω_(t+1)(%s), σ_(t+1)(%s) = %s" % (xn, xn, names[Hs[t + 1][2][x]]), Hs[t + 1][0][x])
D = set(Hs[t][0][y][1]) ^ set(Hs[t][0][cur][1]); z = max(D, key=rk)
print("z = %s: priority %d (%s), owner %d, escape %s, in Π_t(%s): %s" % (names[z], g.prio[z], "even" if g.prio[z] % 2 == 0 else "ODD", g.owner[z], z in W, yn, z in Hs[t][0][y][1]))
lowesc = min(W, key=rk); print("vertices above the least relevant escape %s that are not escapes: %s" % (names[lowesc], " ".join("%s:%d" % (names[u], g.prio[u]) for u in sorted(range(g.n), key=rk) if rk(u) > rk(lowesc) and u not in W)))
