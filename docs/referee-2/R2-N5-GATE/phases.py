import sys, os
D = "/home/user/parity_games_challange/docs/referee-2"
sys.path.insert(0, D + "/R2-N5-LATEP"); sys.path.insert(0, D + "/R2-N5-WRUN")
import latep_check as L, wrun_check as WR
g = L.pg.read(sys.argv[1]); s, t, ok = WR.read_start(g, sys.argv[2]); n = g.n; E = L.Engine(g)
states, fbs = L.DC.Runner(g).run(list(s), list(t), cap=5000)
W = []; lam = []
for sg, tu in states:
    nx = [sg[v] if g.owner[v] == 0 else tu[v] for v in range(n)]; w = [L.pval(E, nx, v) for v in range(n)]; W.append(w); lam.append(tuple(x[0] for x in w))
K = len(states) - 1
kept = [states[k][1] == states[k + 1][1] for k in range(K)]
print("K", K, "fallbacks at", [k for k in range(K) if fbs[k]], "tau changes at", [k for k in range(K) if not kept[k]])
print("lamW changes at", [k for k in range(K) if lam[k] != lam[k + 1]])
print("W-unchanged transitions", [k for k in range(K) if W[k] == W[k + 1]])
