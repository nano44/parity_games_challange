#!/usr/bin/env python3
"""L-RED 60 R226: generalized type-II census (R225-leap §3 READING) at EVERY mover with >= 2 options (own.py IDEAL-CYC, [E-LEV]).
Switch at mover x, step t -> t+1: sigma_(t+1)(x) = g_new != g_old = sigma_t(x). At step t (the deciding values):
  E_new, E_old = Pi-e-sets of the values of g_new, g_old at t (vals[g][1] restricted to e-vertices); z = max(E_new ^ E_old) (relevance);
  shared heads Hh = {e in E_new & E_old : e more relevant than z}; type II iff Hh nonempty (decided BELOW a shared head); head = min(Hh).
  Switches with Lambda(g_new) != Lambda(g_old) at t are 'reward' switches (not counted as type I/II).
Per (x, maximal interval with Lambda(x) constant): #type-II switches, depth = #distinct heads.
Prints totals: T, sw, rew, typeI, typeII, max typeII per (x, I), max depth, sum typeII. Usage: nest226.py G.json ..."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r221")]
import own
def nest(G, cap=3000):
    N = G["N"]; out, V, O, ow = own.run(G, cap); n, prio, o_, succ, _, _ = own.build(G); rk = own.VJ(prio).rk
    evs = {V[("e", q)] for q in O}; tot = dict(T=len(out) - 1, sw=0, rew=0, typeI=0, typeII=0, maxII=0, maxdepth=0)
    for x in range(N):
        if len(G["opts"][x]) < 2: continue
        t = 0
        while t < len(out):
            u = t
            while u + 1 < len(out) and out[u + 1][1][x][0] == out[t][1][x][0]: u += 1
            kII = 0; heads = set()
            for i in range(t, min(u, len(out) - 1)):
                go, gn = out[i][0][x], out[i + 1][0][x]
                if go == gn: continue
                tot["sw"] += 1; vo, vn = out[i][1][go], out[i][1][gn]
                if vo[0] != vn[0]: tot["rew"] += 1; continue
                Eo = {e for e in vo[1] if e in evs}; En = {e for e in vn[1] if e in evs}; d = Eo ^ En
                if not d: tot["typeI"] += 1; continue
                z = max(d, key=lambda e: rk[e]); Hh = [e for e in Eo & En if rk[e] > rk[z]]
                if Hh: kII += 1; heads.add(min(Hh, key=lambda e: rk[e]))
                else: tot["typeI"] += 1
            tot["typeII"] += kII; tot["maxII"] = max(tot["maxII"], kII); tot["maxdepth"] = max(tot["maxdepth"], len(heads)); t = u + 1
    return tot
if __name__ == "__main__":
    for f in sys.argv[1:]: print(os.path.basename(f), nest(json.load(open(f))), flush=True)
