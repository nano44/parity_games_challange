#!/usr/bin/env python3
"""Print states k, k+1 of the SPEC run of a C^1O game (R, theta, w, (h), which vertices change Xi / W). Usage: dump_tf.py game.pg k"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2-N5-RE"))
import re_check as rc
g = rc.parse(open(sys.argv[1]).read()); k = int(sys.argv[2])
o = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1][0]
def br(v, dual):
    def rr(w_):
        p = g.prio[w_] + (1 if dual else 0); r_ = p if p % 2 == 0 else -p
        return (r_, w_ if r_ % 2 == 0 else -w_)
    return max(g.succ[v], key=rr)
s = [br(v, False) for v in range(g.n)]; t = [br(v, True) for v in range(g.n)]
states, fbs = rc.n5_spec(g, o, s, t)
A0, A1 = rc.analyse(g, o, *states[k]), rc.analyse(g, o, *states[k + 1])
fmt = lambda v: (v[0], sorted(v[1]), v[2])
print("o =", o, "tau(o) =", states[k][1][o], "->", states[k + 1][1][o], "fallback at k:", fbs[k])
for S, j in ((A0, k), (A1, k + 1)):
    print(f"k={j} h={S.h} R={sorted(S.R)} theta={fmt(S.theta)} w={fmt(S.w)} sbar(o)={S.sbar} lamX==? ")
print("same lambda maps:", A0.lamX == A1.lamX and A0.lamU == A1.lamU)
print("Xi changes:", [v for v in range(g.n) if A0.Xi[v] != A1.Xi[v]])
print("W changes:", [v for v in range(g.n) if A0.W[v] != A1.W[v]])
print("switched Even:", [(v, A0.f[v], A1.f[v]) for v in range(g.n) if A0.f[v] != A1.f[v]])
