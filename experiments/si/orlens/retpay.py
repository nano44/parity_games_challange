#!/usr/bin/env python3
"""Is every return paid by a gap-level drop?  Inside each joint lambda-phase (target T = Xi at the phase end, g as in gaps.py):
a RETURN = x leaves z at k (sigma_k(x)=z != sigma_{k+1}(x)) and next uses z again at j+1 (sigma_{j+1}(x)=z).
Counts returns for which g(z) drops somewhere in [k, j+1] ('paid_z'), g(x) drops there ('paid_x'), either ('paid_any'),
and lists unpaid ones.  Usage: retpay.py [--switchall] game.pg[:start] ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortrace as OT
def run(path, start=None, mode="n5", show=3):
    g, st = OT.load(path, start)
    E, Ed, states, fbf, _ = OT.run_states(g, st, mode=mode)
    L = OT.Lex(E); n = g.n; ev = [x for x in range(n) if g.owner[x] == 0]
    tot = dict(returns=0, paid_z=0, paid_x=0, paid_any=0); unpaid = []
    for ph in OT.phases(E, Ed, states):
        T = states[ph[-1]][2]
        G = [[L.lev(T[v], states[k][2][v]) for v in range(n)] for k in ph]
        sig = [states[k][0] for k in ph]
        for x in ev:
            for i in range(len(ph) - 1):
                if sig[i][x] == sig[i + 1][x]: continue
                z = sig[i][x]
                j = next((j for j in range(i + 1, len(ph)) if sig[j][x] == z), None)
                if j is None: continue
                tot["returns"] += 1
                dz = any(G[t + 1][z] < G[t][z] for t in range(i, j))
                dx = any(G[t + 1][x] < G[t][x] for t in range(i, j))
                tot["paid_z"] += dz; tot["paid_x"] += dx; tot["paid_any"] += (dz or dx)
                if not (dz or dx) and len(unpaid) < show: unpaid.append((ph[i], ph[j], x, z, sig[i + 1][x], G[i][z], G[i][x]))
    return n, tot, unpaid
if __name__ == "__main__":
    mode = 'switchall' if '--switchall' in sys.argv else 'n5'
    for spec in [a for a in sys.argv[1:] if not a.startswith('--')]:
        p, _, s = spec.partition(":")
        n, tot, unpaid = run(p, s or None, mode)
        print(f"{mode:9s} {os.path.basename(p):22s} n={n:3d} {tot} unpaid examples (k, j, x, z, z', g(z), g(x)): {unpaid}", flush=True)
