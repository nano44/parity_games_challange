#!/usr/bin/env python3
"""L-NEW box 115 ablations of N5 on one game (same VJ engine, si.py via box21/n5x.py). Variants:
  SI    classical switch-all SI: sigma <- rule_switch_all against Odd's optimal counterstrategy sigma-bar (no tau).
  ARSB  S4a's step with sigma-bar for tau: sigma <- pointwise optimum of the arena {sigma(v)} u Isigma(v) with Odd fixed to sigma-bar_k.
  SAT   symmetric loop with Even switch-all and Odd's S4b (tau <- Odd's pointwise optimum of {tau(o)} u Itau(o) against the OLD sigma);
        S4c-style fallback for tau when sigma is optimal and tau unchanged.
  TBR   S4a against tau_k as in N5, but Odd's update is its full best reply: tau_(k+1) := sigma-bar_k (Odd's optimal counterstrategy to
        the OLD sigma_k), instead of S4b's arena-restricted optimum. Stops when Isigma and Itau are empty.
  N5    n5x.step (SPEC S1-S5).
Prints iterations, Even switches, max entries of one Even pair (y, z), max fuel re-routes of one pair (as box115/swx.py), and for
loops with tau the W-runs. Usage: abl.py G.pg VARIANT [cap]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, Engine, dual
import pg
g = load(sys.argv[1]); VAR = sys.argv[2]; cap = int(sys.argv[3]) if len(sys.argv) > 3 else 100000; n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g))
def even_opt(sig, odd, Is):
    opt = {v: {sig[v]} for v in range(n) if own[v] == 0}
    for v, w in Is: opt[v].add(w)
    succ = [sorted(opt[v]) if own[v] == 0 else [odd[v]] for v in range(n)]
    Er = Engine(dual(pg.Game(list(g.prio), list(own), succ)))
    _, best = Er.evaluate(tuple(odd[v] if own[v] == 1 else -1 for v in range(n)))
    return tuple(best[v] if own[v] == 0 else sig[v] for v in range(n))
def odd_opt(tau, sig, It):
    opt = {v: {tau[v]} for v in range(n) if own[v] == 1}
    for v, w in It: opt[v].add(w)
    succ = [sorted(opt[v]) if own[v] == 1 else [sig[v]] for v in range(n)]
    Er = Engine(pg.Game(list(g.prio), list(own), succ))
    _, best = Er.evaluate(tuple(sig[v] if own[v] == 0 else -1 for v in range(n)))
    return tuple(best[v] if own[v] == 1 else tau[v] for v in range(n))
s0, t0 = start_pair(g, E, Ed, None); S, T = [tuple(s0)], [tuple(t0)]
while len(S) <= cap:
    sig, tau = S[-1], T[-1]
    vs, sb = E.evaluate(sig); Is = E.improving(sig, vs)
    if VAR == "SI":
        if not Is: break
        S.append(E.rule_switch_all(sig, vs, Is, None)); T.append(tau)
    elif VAR == "ARSB":
        if not Is: break
        S.append(even_opt(sig, sb, Is)); T.append(tau)
    elif VAR == "SAT":
        vt, tb = Ed.evaluate(tau); It = Ed.improving(tau, vt)
        if not Is and not It: break
        ns = E.rule_switch_all(sig, vs, Is, None) if Is else sig
        nt = odd_opt(tau, sig, It) if It else tau
        if ns == sig and nt == tau:
            nt = list(tau)
            for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
            nt = tuple(nt)
        S.append(ns); T.append(nt)
    elif VAR == "TBR":
        vt, tb = Ed.evaluate(tau); It = Ed.improving(tau, vt)
        if not Is and not It: break
        ns = even_opt(sig, tau, Is) if Is else sig
        nt = tuple(sb[v] if own[v] == 1 else tau[v] for v in range(n))
        if ns == sig and nt == tau: break
        S.append(ns); T.append(nt)
    elif VAR == "N5":
        r = step(g, E, Ed, list(sig), list(tau))
        if r is None: break
        S.append(tuple(r[0])); T.append(tuple(r[1]))
K = len(S) - 1
XI = {}
def xi(k):
    if k not in XI: vs, _ = E.evaluate(S[k]); XI[k] = (vs, set(E.improving(S[k], vs)))
    return XI[k]
ENT, FR = {}, {}; SW = 0
for k in range(K):
    for y in range(n):
        if own[y] != 0 or S[k + 1][y] == S[k][y]: continue
        z = S[k + 1][y]; SW += 1; ENT[(y, z)] = ENT.get((y, z), 0) + 1
        if k >= 1 and z != S[k - 1][y] and (y, z) not in xi(k - 1)[1] and xi(k - 1)[0][z] != xi(k)[0][z]: FR[(y, z)] = FR.get((y, z), 0) + 1
mx = lambda d: max(d.items(), key=lambda a: a[1]) if d else (None, 0)
win = E.regions(S[-1]) if VAR in ("SI", "ARSB") else None
print(f"ABL {os.path.basename(sys.argv[1])} {VAR} n {n} iters {K}{' CAPPED' if K >= cap else ''} evenswitches {SW} taumoves {sum(1 for k in range(K) if T[k] != T[k+1])} MAXENT {mx(ENT)[1]} {mx(ENT)[0]} MAXFR {mx(FR)[1]} {mx(FR)[0]}")
