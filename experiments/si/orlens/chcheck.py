#!/usr/bin/env python3
"""Check Lemma CH (box 3 §2): at a theta-change with e = sbar_k(o) outside R at k and k+1 ((h) at both), lev(theta_k, theta_{k+1})
<= lev(Xi_k(e), Xi_{k+1}(e)).  Also Lemma LEN: max run of consecutive length-only theta-changes in a phase."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortrace as OT
from thclass import hstate
def run(path, start=None):
    g, st = OT.load(path, start)
    E, Ed, states, fbf, _ = OT.run_states(g, st); L = OT.Lex(E)
    n = g.n; o = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1][0]
    def inR(sig, tau, v):
        seen = set(); x = v
        while x not in seen:
            if x == o: return True
            seen.add(x); x = sig[x] if g.owner[x] == 0 else tau[x]
        return False
    chk = viol = 0; lenrun = 0
    for ph in OT.phases(E, Ed, states):
        cur = 0
        for t in range(len(ph) - 1):
            s0, s1 = states[ph[t]], states[ph[t + 1]]
            a, b = s0[2][o], s1[2][o]
            if a == b: continue
            if a[1] == b[1]: cur += 1; lenrun = max(lenrun, cur)
            else: cur = 0
            if not (hstate(g, E, s0, o) and hstate(g, E, s1, o)): continue
            e = s0[3][o]
            if inR(s0[0], s0[1], e) or inR(s1[0], s1[1], e): continue
            chk += 1
            if L.lev(a, b) > L.lev(s0[2][e], s1[2][e]): viol += 1
    return n, chk, viol, lenrun
if __name__ == "__main__":
    for spec in sys.argv[1:]:
        p, _, s = spec.partition(":")
        print(os.path.basename(p), run(p, s or None), flush=True)
