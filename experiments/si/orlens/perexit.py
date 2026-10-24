#!/usr/bin/env python3
"""Per (w, u*)-run and per exit e of o: RISE(e) = number of theta-changes at which e = sbar_k(o), e stays out of R, and Xi(e)
strictly rises (classes SELF and OVER of thclass.py); INR(e) = INR events of e.  Prints max RISE(e), max INR(e), max over runs of
theta-changes, and the max of (theta-changes in a run) / d."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortrace as OT
from stretchret import playval
from thclass import ustar, hstate
from collections import Counter
def run(path, start=None):
    g, st = OT.load(path, start)
    return run_g(g, st)
def run_g(g, st=None, cap=10 ** 5):
    E, Ed, states, fbf, _ = OT.run_states(g, st, cap=cap)
    n = g.n; o = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1][0]; d = len(set(g.succ[o]))
    def inR(sig, tau, v):
        seen = set(); x = v
        while x not in seen:
            if x == o: return True
            seen.add(x); x = sig[x] if g.owner[x] == 0 else tau[x]
        return False
    mr = mi = mt = 0; other = 0; ex = None
    for ph in OT.phases(E, Ed, states):
        key = []
        for k in ph:
            s = states[k]; w = playval(E, s[0], s[1], o); th = s[2][o]
            key.append((s[1], w, ustar(E, th, w)) if (th != w and hstate(g, E, s, o)) else None)
        t = 0
        while t < len(ph):
            if key[t] is None: t += 1; continue
            u = t
            while u + 1 < len(ph) and key[u + 1] == key[t]: u += 1
            rise = Counter(); inr = Counter(); tc = 0
            for j in range(t, u):
                s0, s1 = states[ph[j]], states[ph[j + 1]]
                if s0[2][o] == s1[2][o]: continue
                tc += 1; e = s0[3][o]
                if inR(s1[0], s1[1], e): inr[e] += 1
                elif E.key(s1[2][e]) > E.key(s0[2][e]): rise[e] += 1
                else: other += 1
            if rise and max(rise.values()) > mr: mr = max(rise.values()); ex = (ph[t], ph[u], rise.most_common(1))
            mi = max(mi, max(inr.values(), default=0)); mt = max(mt, tc)
            t = u + 1
    return n, d, mr, mi, mt, other, ex
if __name__ == "__main__":
    for spec in sys.argv[1:]:
        p, _, s = spec.partition(":")
        n, d, mr, mi, mt, other, ex = run(p, s or None)
        print(f"{os.path.basename(p):22s} n={n:3d} d={d:2d} max RISE per exit per run={mr} max INR per exit per run={mi} max theta-changes per run={mt} other={other} {ex}", flush=True)
