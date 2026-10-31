#!/usr/bin/env python3
"""L-NEW box 116b: test of the coupling target CARRY-ODD on one N5 run. Per Even pair (y, z): FR(y, z) = fuel re-routes (box115/swx.py
definition, whole run) and RE(y, z) = max(FR - 1, 0), the re-entries. Run quantities: ORET (Odd returns), TCH (tau-changing transitions),
FB (fallbacks), ES (R97 source events on W-run transitions, desc.py's src()), WCH(z) (transitions of W-runs changing W(z), W under the
run's tau). Variants: V1 = 1 + ORET + ES; V2 = 1 + TCH + FB + ES; V3(y, z) = V1 + WCH(z). Prints max RE, and max of RE/V for each variant
(argmax pair). Usage: carry.py G.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); S, TAU, FB = [tuple(s)], [tuple(t)], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
K = len(S) - 1; XI = {}
def xi(k):
    if k not in XI: vs, sb = E.evaluate(S[k]); XI[k] = (vs, set(E.improving(S[k], vs)), sb)
    return XI[k]
Wc = {}
def Wraw(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
inrun = [TAU[k + 1] == TAU[k] and not FB[k] and [x[0] for x in Wraw(k, TAU[k])] == [x[0] for x in Wraw(k + 1, TAU[k])] for k in range(K)]
ES = 0; WCH = {}
for k in range(K):
    if not inrun[k]: continue
    tau = TAU[k]; A, B = Wraw(k, tau), Wraw(k + 1, tau)
    for v in range(n):
        if A[v] != B[v]: WCH[v] = WCH.get(v, 0) + 1
    X0, sb0 = xi(k)[0], xi(k)[2]; X1, sb1 = xi(k + 1)[0], xi(k + 1)[2]; C = {x for x in range(n) if A[x][0] == x}
    Sk = {o for o in range(n) if own[o] == 1 and (sb0[o] != tau[o] or sb1[o] != tau[o])} | C
    ES += any(X0[x] != X1[x] for x in Sk)
held = {o: {TAU[0][o]} for o in range(n) if own[o] == 1}; ORET = TCH = 0
for k in range(K):
    if TAU[k + 1] != TAU[k]:
        TCH += 1
        for o in held:
            if TAU[k + 1][o] != TAU[k][o]: ORET += TAU[k + 1][o] in held[o]; held[o].add(TAU[k + 1][o])
FR = {}
for k in range(1, K):
    for y in range(n):
        if own[y] != 0 or S[k + 1][y] == S[k][y]: continue
        z = S[k + 1][y]
        if z != S[k - 1][y] and (y, z) not in xi(k - 1)[1] and xi(k - 1)[0][z] != xi(k)[0][z]: FR[(y, z)] = FR.get((y, z), 0) + 1
V1 = 1 + ORET + ES; V2 = 1 + TCH + sum(FB) + ES
RE = {p: c - 1 for p, c in FR.items() if c > 1}
mr = max(RE.values() or [0])
r1 = max(((c / V1, p) for p, c in RE.items()), default=(0, None)); r2 = max(((c / V2, p) for p, c in RE.items()), default=(0, None))
r3 = max(((c / (V1 + WCH.get(p[1], 0)), p) for p, c in RE.items()), default=(0, None))
print(f"CARRY {os.path.basename(sys.argv[1])} n {n} iters {K} maxRE {mr} ORET {ORET} TCH {TCH} FB {sum(FB)} ES {ES} V1 {V1} V2 {V2} "
      f"R1 {r1[0]:.3f} {r1[1]} R2 {r2[0]:.3f} {r2[1]} R3 {r3[0]:.3f} {r3[1]} V1VIOL {int(r1[0] > 1)} V2VIOL {int(r2[0] > 1)} V3VIOL {int(r3[0] > 1)}")
