#!/usr/bin/env python3
"""L-RED R142: exhaustive static-rho BIP on box 82's Odd-gated ladder ogl_k (l-new 163342eb experiments/new/box82/inst/ogl_k.pg):
tau = honest at every gate (first successor, u(j, c)); rho ranges over ALL static routings (each gate: honest or routed); sigma0 over all
Even starts (or a sample). Prints the max BIP length and the max number of distinct W(T) = val(sigma, tau)(T) values along a run.
Usage: oglx.py OGL.pg [SAMPLES]"""
import sys, os, itertools, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import bip
n5b = bip.n5b
g = n5b.pg.read(sys.argv[1]); n = g.n
gates = [v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) == 2]
ch = [v for v in range(n) if g.owner[v] == 0 and len(g.succ[v]) > 1]
T = max(ch, key=lambda v: (g.prio[v] == 3, v)) if any(g.prio[v] == 3 for v in ch) else ch[-1]
tau = [g.succ[v][0] if g.owner[v] == 1 else -1 for v in range(n)]
Gt = n5b.SpecSI(n5b.pg.Game(list(g.prio), list(g.owner), [[tau[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(n)]))
def tvals(rho, s0):
    # replay BIP, recording W(T)
    N = n5b.N5(g); N.mode = "spec"
    Grho = n5b.SpecSI(n5b.pg.Game(list(g.prio), list(g.owner), [[rho[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(n)]))
    sig = list(s0); vals = [Gt.evaluate(sig)[T]]; it = 0
    while it < 5000:
        vr = Grho.evaluate(sig); I = N.improving(Grho, sig, vr)
        if not I: break
        allow = [([sig[v]] + I.get(v, [])) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
        _, c2 = N.opt(n5b.SpecSI(n5b.dual(n5b.restrict(g, allow))), [tau[v] if g.owner[v] == 1 else -1 for v in range(n)])
        ns = [c2[v] if g.owner[v] == 0 else -1 for v in range(n)]
        if ns == sig: break
        sig = ns; it += 1; w = Gt.evaluate(sig)[T]
        if w != vals[-1]: vals.append(w)
    return it, len(vals)
best = (0, 0, None)
rhos = list(itertools.product((0, 1), repeat=len(gates))); starts = list(itertools.product(*[range(len(g.succ[v])) for v in ch]))
pairs = [(r, s) for r in rhos for s in starts]
if len(sys.argv) > 2: random.seed(1); pairs = random.sample(pairs, min(int(sys.argv[2]), len(pairs)))
for r, s in pairs:
    rho = list(tau)
    for gv, b in zip(gates, r): rho[gv] = g.succ[gv][b]
    s0 = [-1] * n
    for v in range(n):
        if g.owner[v] == 0: s0[v] = g.succ[v][0]
    for v, i in zip(ch, s): s0[v] = g.succ[v][i]
    it, tv = tvals(rho, s0)
    if (tv, it) > best[:2]: best = (tv, it, (r, s))
print(f"OGLX {os.path.basename(sys.argv[1])} n {n} gates {len(gates)} pairs {len(pairs)} max W(T)-values {best[0]} (steps {best[1]}) at {best[2]}")
