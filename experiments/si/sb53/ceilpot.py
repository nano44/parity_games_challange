#!/usr/bin/env python3
"""L-SI box 53c: candidate global potentials against the W-ceiling (Fact CEILING, note §7: Xi <= W pointwise) inside W-runs (as
treestab.py). Per transition of a W-run: Z := |{v : Xi(v) != W(v)}| (gap set size); A := sum_v lcp(CS(Xi(v)), CS(W(v))) (agreement with
the ceiling, R93 coordinate sequences). Counts rises / falls / flats of each, and the transitions at which BOTH are flat (FLAT2).
AINC: the total increase of A over W-run transitions; ANDN: W-run transitions at which A does not strictly fall; AMAX: max A. AUPZ: rises of A at which the gap set does not shrink. Per W-run maxima: MAXWR (length), MAXAUP, MAXANDN.
So the W-run transitions number <= AMAX + AINC + ANDN (A >= 0). SRC: W-run transitions that are SOURCE EVENTS (R97: Xi changes at a vertex of S_k = D_k u D_(k+1) u C); AUPSF / ANDNSF / AEQSF:
rises / non-falls / flats of A at source-free transitions; AEQ0SF / AEQMAXSF: source-free flats at the floor A = 0 / the ceiling
A = n(n+2) (Xi = W); AMIDSF: source-free non-falls with A strictly inside (0, n(n+2)) at both states. Usage: ceilpot.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); S, TAU, FB = [tuple(s)], [tuple(t)], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
def cs(v):
    c, m, l = v
    return (E.rew[c],) + tuple(((1 if E.rankpar[r] == 0 else -1) if (m >> r) & 1 else 0) for r in range(n - 1, -1, -1)) + ((l if E.par[c] == 1 else -l),)
def lcp(a, b):
    i = 0
    while i < len(a) and a[i] == b[i]: i += 1
    return i
cur = None; per = []
c = dict(WT=0, ZUP=0, ZDN=0, ZEQ=0, AUP=0, ADN=0, AEQ=0, FLAT2=0, AINC=0, ANDN=0, AMAX=0, AUPZ=0, WRUNS=0, MAXWR=0, MAXAUP=0, MAXANDN=0, SRC=0, AUPSF=0, ANDNSF=0, AEQSF=0, AEQ0SF=0, AEQMAXSF=0, AMIDSF=0)
for k in range(len(S) - 1):
    if TAU[k + 1] != TAU[k] or FB[k] or [x[0] for x in Wv(k, TAU[k])] != [x[0] for x in Wv(k + 1, TAU[k])]: continue
    if cur is None or cur[0] != k - 1: cur = [k, 0, 0, 0]; per.append(cur)
    cur[0] = k; cur[1] += 1
    c['WT'] += 1; P = []
    for q in (k, k + 1):
        X = E.evaluate(S[q])[0]; W = Wv(q, TAU[k])
        P.append((sum(1 for v in range(n) if X[v] != W[v]), sum(lcp(cs(X[v]), cs(W[v])) for v in range(n))))
    (z0, a0), (z1, a1) = P
    X0, sb0 = E.evaluate(S[k]); X1, sb1 = E.evaluate(S[k + 1]); tau = TAU[k]
    Wk = Wv(k, tau); C = {v for v in range(n) if Wk[v][0] == v}
    Sk = {o for o in range(n) if own[o] == 1 and (sb0[o] != tau[o] or sb1[o] != tau[o])} | C
    src = any(X0[v] != X1[v] for v in Sk); c['SRC'] += src
    if not src: c['AUPSF'] += a1 > a0; c['ANDNSF'] += a1 >= a0; c['AEQSF'] += a1 == a0
    if not src and a1 == a0: c['AEQ0SF'] += a0 == 0; c['AEQMAXSF'] += a0 == n * (n + 2)
    if not src and a1 >= a0 and 0 < a0 < n * (n + 2) and 0 < a1 < n * (n + 2): c['AMIDSF'] += 1
    c['ZUP' if z1 > z0 else 'ZDN' if z1 < z0 else 'ZEQ'] += 1; c['AUP' if a1 > a0 else 'ADN' if a1 < a0 else 'AEQ'] += 1
    c['FLAT2'] += z1 == z0 and a1 == a0
    c['AUPZ'] += a1 > a0 and z1 >= z0; cur[2] += a1 > a0; cur[3] += a1 >= a0
    c['AINC'] += max(0, a1 - a0); c['ANDN'] += a1 >= a0; c['AMAX'] = max(c['AMAX'], a0, a1)
c['WRUNS'] = len(per); c['MAXWR'] = max([x[1] for x in per] or [0]); c['MAXAUP'] = max([x[2] for x in per] or [0]); c['MAXANDN'] = max([x[3] for x in per] or [0])
print(f"CEILPOT {os.path.basename(sys.argv[1])} n {n} " + " ".join(f"{a} {b}" for a, b in c.items()))
