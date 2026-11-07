#!/usr/bin/env python3
"""L-NEW box 115: N5 vs classical switch-all SI on one game, same VJ engine (experiments/si/si.py via box21/n5x.py).
Counts per run: iterations; for N5 also fallbacks (S4c), tau-changing transitions, W-runs (RESULTS R89; count, longest, total); pair
counts for every Even edge (y, z): ENT = entries (y switches to z), FR = fuel re-routes (P-N5-ODD §6 without the W-run clause: y
switches to z at k >= 1, (y, z) not in H_(k-1) = {sigma_(k-1)(y)} u Isigma_(k-1)(y), Xi_(k-1)(z) != Xi_k(z)), FR_W = those with k - 1 and
k in one W-run (N5 only). MAX* = max over pairs (and the argmax pair). Usage: swx.py G.pg [--si] [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
SI = "--si" in sys.argv; args = [a for a in sys.argv[1:] if a != "--si"]
g = load(args[0]); st = readstart(args[1]) if len(args) > 1 else None; n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g))
if SI:
    S = [tuple(E.initial("best"))]
    while True:
        v_ = E.evaluate(S[-1])[0]; I_ = E.improving(S[-1], v_)
        if not I_: break
        S.append(E.rule_switch_all(S[-1], v_, I_, None))
    TAU = [None] * len(S); FB = [0] * (len(S) - 1)
else:
    s, t = start_pair(g, E, Ed, st); S, TAU, FB = [tuple(s)], [tuple(t)], []
    while True:
        r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
        if r is None: break
        S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
XI = {}
def xi(k):
    if k not in XI: vs, _ = E.evaluate(S[k]); XI[k] = (vs, set(E.improving(S[k], vs)))
    return XI[k]
K = len(S) - 1
run_of = [None] * K
if not SI:
    Wc = {}
    def lam(k, tau):
        if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
        return [x[0] for x in Wc[tau].evaluate(S[k])[0]]
    rid = -1
    for k in range(K):
        if TAU[k + 1] != TAU[k] or FB[k] or lam(k, TAU[k]) != lam(k + 1, TAU[k]): continue
        if k == 0 or run_of[k - 1] is None: rid += 1
        run_of[k] = rid
ENT, FR, FRW = {}, {}, {}
for k in range(K):
    for y in range(n):
        if own[y] != 0 or S[k + 1][y] == S[k][y]: continue
        z = S[k + 1][y]; ENT[(y, z)] = ENT.get((y, z), 0) + 1
        if k >= 1 and z != S[k - 1][y] and (y, z) not in xi(k - 1)[1] and xi(k - 1)[0][z] != xi(k)[0][z]:
            FR[(y, z)] = FR.get((y, z), 0) + 1
            if run_of[k] is not None and run_of[k - 1] == run_of[k]:
                key = (run_of[k], y, z); FRW[key] = FRW.get(key, 0) + 1
def mx(d): return max(d.items(), key=lambda a: a[1]) if d else (None, 0)
runs = {}
for k in range(K):
    if run_of[k] is not None: runs[run_of[k]] = runs.get(run_of[k], 0) + 1
out = dict(iters=K, fallbacks=sum(FB), tauchg=sum(1 for k in range(K) if TAU[k] != TAU[k + 1]) if not SI else 0,
           wruns=len(runs), wlongest=max(runs.values() or [0]), wtotal=sum(runs.values()))
me, mf, mw = mx(ENT), mx(FR), mx(FRW)
print(f"SWX {os.path.basename(args[0])} {'SI' if SI else 'N5'} n {n} " + " ".join(f"{a} {b}" for a, b in out.items()) +
      f" MAXENT {me[1]} {me[0]} MAXFR {mf[1]} {mf[0]} MAXFR_W {mw[1]} {mw[0]} SUMFR {sum(FR.values())} SUMFR_W {sum(FRW.values())}")
