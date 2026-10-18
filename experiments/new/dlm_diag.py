#!/usr/bin/env python3
"""Box 5: the condition "N5's Even step = SSI's Even step iff τ̄ ⊆ A_σ" (τ̄ = Even's best reply to τ; A_σ(v) = {σ(v)} ∪ Iσ(v)),
dually σ̄ ⊆ A_τ for Odd. Runs SSI (n5.py mode ssi = 2309.02223 Alg. 2 with switch-all) or N5 (mode n5) with n5.py's own step
(copied loop, counts asserted equal to n5.run) and prints, per iteration, the vertices where the condition FAILS.
Usage: dlm_diag.py game.pg ssi|n5 [startfile]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import n5
from n5 import pg, Engine, dual
from n5_lock import step
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); mode = sys.argv[2]
st = None
if len(sys.argv) > 3:
    L = [l for l in open(sys.argv[3]) if l.split() and l.split()[0] in ("SIGMA0", "TAU0")]
    st = tuple(dict(map(int, t.split(":")) for t in L[j].split()[1:]) for j in (0, 1))
E, Ed = Engine(g), Engine(dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best"))
if st:
    for v, w in st[0].items(): s[v] = w
    for v, w in st[1].items(): t[v] = w
it = fb = 0; tot_e = tot_o = 0
while True:
    vs, sbar = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs); vt, tbar = Ed.evaluate(tuple(t)); It = Ed.improving(tuple(t), vt)
    if not Is and not It: break
    A = {v: {s[v]} | {w for x, w in Is if x == v} for v in range(g.n) if g.owner[v] == 0}
    B = {v: {t[v]} | {w for x, w in It if x == v} for v in range(g.n) if g.owner[v] == 1}
    fe = [v for v in A if tbar[v] not in A[v]]; fo = [v for v in B if sbar[v] not in B[v]]
    tot_e += len(fe); tot_o += len(fo); it += 1
    print(f"it {it}: |Is|={len(Is)} |It|={len(It)} Even: tbar outside A_sigma at {fe}; Odd: sbar outside A_tau at {fo}")
    if mode == "ssi":
        ns, nt = list(s), list(t)
        for v, w in Is:
            if tbar[v] == w: ns[v] = w
        for v, w in It:
            if sbar[v] == w: nt[v] = w
        s, t = ns, nt
    else:
        r = step(g, E, Ed, s, t); fb += r[2]; s, t = r[0], r[1]
ri, rf, *_ = n5.run(g, mode, st)
assert (ri, rf) == (it, fb), (ri, rf, it, fb)
print(f"TOTAL {mode} iterations={it} fallback={fb} (= n5.run); condition failures: Even {tot_e}, Odd {tot_o}")
