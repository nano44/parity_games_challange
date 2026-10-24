#!/usr/bin/env python3
"""theta-changes grouped by (w, u*)-run (box 27 §8b) on one-Odd-choice games.  A run = maximal sequence of consecutive states in
one joint lambda-phase with tau, w and u* constant and theta != w (throttled).  Per run: theta-changes by class (thclass.py),
INR events whose exit already had an INR event earlier in the same run ('repeat INR'), d, and the number of distinct exits used."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortrace as OT
from stretchret import playval
from thclass import ustar, hstate
from collections import Counter
def run(path, start=None):
    g, st = OT.load(path, start)
    E, Ed, states, fbf, _ = OT.run_states(g, st)
    n = g.n; o = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1][0]; d = len(set(g.succ[o]))
    def inR(sig, tau, v):
        seen = set(); x = v
        while x not in seen:
            if x == o: return True
            seen.add(x); x = sig[x] if g.owner[x] == 0 else tau[x]
        return False
    out = []
    for ph in OT.phases(E, Ed, states):
        key = []
        for k in ph:
            s = states[k]; w = playval(E, s[0], s[1], o); th = s[2][o]
            key.append((s[1], w, ustar(E, th, w)) if (th != w and hstate(g, E, s, o)) else None)
        t = 0
        while t < len(ph) - 1:
            if key[t] is None: t += 1; continue
            u = t
            while u + 1 < len(ph) and key[u + 1] == key[t]: u += 1
            # transitions t..u-1 inside the run; also count the transition leaving the run if theta changes there
            c = Counter(); inr_ex = []; rep = 0
            for j in range(t, min(u + 1, len(ph) - 1)):
                s0, s1 = states[ph[j]], states[ph[j + 1]]
                if s0[2][o] == s1[2][o]: continue
                e, e1 = s0[3][o], s1[3][o]
                if inR(s1[0], s1[1], e):
                    c["INR"] += 1
                    if e in inr_ex: rep += 1
                    inr_ex.append(e)
                elif e1 == e: c["SELF"] += 1
                else: c["OVER"] += 1
            out.append(dict(states=(ph[t], ph[u]), ustar=key[t][2], tc=sum(c.values()), cls=dict(c), repINR=rep))
            t = u + 1
    return n, d, out
if __name__ == "__main__":
    for spec in sys.argv[1:]:
        p, _, s = spec.partition(":")
        n, d, out = run(p, s or None)
        tot = sum(r["tc"] for r in out); mx = max((r["tc"] for r in out), default=0); rep = sum(r["repINR"] for r in out)
        print(f"{os.path.basename(p):22s} n={n:3d} d={d} runs={len(out)} theta-changes in runs={tot} max per run={mx} repeat-INR={rep}")
        for r in out:
            if r["tc"] >= 3: print("    ", r)
