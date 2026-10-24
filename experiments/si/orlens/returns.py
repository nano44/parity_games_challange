#!/usr/bin/env python3
"""Classify abandonments inside each joint lambda-phase of an N5 run: x leaves z at k (sigma_k(x)=z != sigma_{k+1}(x)).
final = (x,z) never used again in the phase; return = used again.  For returns: slack level of (x,z) w.r.t. the phase
target T (=Xi at the phase end): 'tight' if x+T(z) == T(x) (lev -1), else the level; also whether sigma_end(x) == z.
Also per-vertex max number of returns."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortrace as OT
from collections import Counter
def run(path, start=None, mode="n5"):
    g, st = OT.load(path, start)
    E, Ed, states, fbf, _ = OT.run_states(g, st, mode=mode)
    L = OT.Lex(E); n = g.n
    tot = Counter(); pervx = Counter()
    for ph in OT.phases(E, Ed, states):
        T = states[ph[-1]][2]; send = states[ph[-1]][0]
        sig = [states[k][0] for k in ph]
        for i in range(len(ph) - 1):
            for x in range(n):
                if g.owner[x] != 0 or sig[i][x] == sig[i + 1][x]: continue
                z = sig[i][x]
                if any(sig[j][x] == z for j in range(i + 1, len(ph))):
                    a = L.pre(x, T[z])
                    if a == T[x]: kind = "ret_tight"
                    elif L.le(a, T[x]): kind = "ret_slack"
                    else: kind = "ret_neg"
                    tot[kind] += 1; tot["ret_end" if send[x] == z else "ret_notend"] += 1
                    pervx[(ph[0], x)] += 1
                else:
                    tot["final"] += 1
    return n, tot, max(pervx.values()) if pervx else 0
if __name__ == "__main__":
    mode = 'switchall' if '--switchall' in sys.argv else 'n5'
    for spec in [a for a in sys.argv[1:] if not a.startswith('--')]:
        p, _, s = spec.partition(":")
        n, tot, mx = run(p, s or None, mode)
        print(f"{os.path.basename(p):22s} n={n:3d} {dict(tot)} max returns per vertex per phase={mx}", flush=True)
