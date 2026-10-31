#!/usr/bin/env python3
"""REFEREE-2 succ. 25: print one boundary instance (transition K leaving a W-run). Usage: bnd.py game.pg game.start K y z"""
import sys, os
D = "/home/user/parity_games_challange/docs/referee-2"
sys.path.insert(0, D + "/R2-N5-LATEP"); sys.path.insert(0, D + "/R2-N5-WRUN")
import latep_check as L, wrun_check as WR
pgf, stf, K, y, z = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
g = L.pg.read(pgf); s, t, ok = WR.read_start(g, stf)
states, fbs = L.DC.Runner(g).run(list(s), list(t), cap=5000)
E = L.Engine(g); n = g.n
def W(k):
    sg, tu = states[k]; nx = [sg[v] if g.owner[v] == 0 else tu[v] for v in range(n)]
    return [L.pval(E, nx, v) for v in range(n)]
def XI(k):
    sg = states[k][0]; xe, sb = E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n))); return [tuple(x) for x in xe], set(E.improving(tuple(sg), xe))
print("start ok", ok, "fallback at K", fbs[K], "tau same", states[K][1] == states[K+1][1], "fb at K-1", fbs[K-1])
for k in (K-1, K, K+1):
    w = W(k); print(k, "sigma(y)", states[k][0][y], "W(y)", w[y], "W(z)", w[z], "lamW same as K-1", [x[0] for x in w] == [x[0] for x in W(K-1)])
xi, Is = XI(K-1); print("in H_(K-1):", z == states[K-1][0][y] or (y, z) in Is)
