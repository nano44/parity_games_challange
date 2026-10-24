#!/usr/bin/env python3
"""Classify every theta-change (theta = Xi(o)) inside joint lambda-phases of N5 runs on one-Odd-choice games.
At transition k -> k+1 with theta changing, e = sbar_k(o), e' = sbar_{k+1}(o):
  INR    : e entered R at k+1 (e's play now reaches o), so o cannot use it;
  SELF   : e' == e and Xi(e) rose;
  OVER   : e' != e, e not in R_{k+1}, Xi(e) rose above Xi(e') (the min moved);
  other  : anything else.
Also: w and u* (top rank of P(theta) xor P(w)) at both states; whether the exit's new value equals its value at the END of the
(w, u*)-run (its 'final' value); and for SELF/OVER the Even vertices on e's sigma-path that switched."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortrace as OT
from stretchret import playval
from collections import Counter
def hstate(g, E, s, o):
    """box 21 (h): o on no cycle of the (sigma, sbar)-play or the (sigma, tau)-play from o, and Xi(o), W(o) share the cycle node."""
    from stretchret import playval
    sig, tau, vs, sbar = s[0], s[1], s[2], s[3]
    for odd in (sbar, tau):
        seen = []; x = o
        while x not in seen:
            seen.append(x); x = sig[x] if g.owner[x] == 0 else odd[x]
        if x == o: return False
    return vs[o][0] == playval(E, sig, tau, o)[0]
def ustar(E, th, w):
    if th[0] != w[0]: return 'C'
    d = th[1] ^ w[1]
    return d.bit_length() - 1 if d else None
def run(path, start=None, verbose=False):
    g, st = OT.load(path, start)
    E, Ed, states, fbf, _ = OT.run_states(g, st)
    n = g.n; o = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1][0]
    def inR(sig, tau, v):
        seen = set(); x = v
        while x not in seen:
            if x == o: return True
            seen.add(x); x = sig[x] if g.owner[x] == 0 else tau[x]
        return False
    cnt = Counter(); rows = []
    for ph in OT.phases(E, Ed, states):
        for t in range(len(ph) - 1):
            k, k1 = ph[t], ph[t + 1]
            s0, s1 = states[k], states[k1]
            th0, th1 = s0[2][o], s1[2][o]
            if th0 == th1: continue
            e, e1 = s0[3][o], s1[3][o]
            w0 = playval(E, s0[0], s0[1], o); w1 = playval(E, s1[0], s1[1], o)
            if inR(s1[0], s1[1], e): c = "INR"
            elif e1 == e: c = "SELF"
            elif E.key(s1[2][e]) > E.key(s0[2][e]): c = "OVER"
            else: c = "other"
            cnt[c] += 1
            rows.append((k, c, e, e1, ustar(E, th0, w0), ustar(E, th1, w1), w0 == w1, fbf[k]))
    return n, o, cnt, rows
if __name__ == "__main__":
    for spec in [a for a in sys.argv[1:] if not a.startswith("--")]:
        p, _, s = spec.partition(":")
        n, o, cnt, rows = run(p, s or None)
        print(f"{os.path.basename(p):22s} n={n:3d} o={o} {dict(cnt)}")
        if "--verbose" in sys.argv:
            for r in rows: print("   k=%d %s exit %s->%s u* %s->%s w-same=%s fb=%d" % r)
