#!/usr/bin/env python3
"""L-COMP box 32: OSC sub-problem (Lead 10:58Z, from L-LOWER 10 §3c): can pairs 0-5 follow the core8 target on a prefix t = 0..T0
when they and their helpers never read pairs 6-7 (movers 12-15)?
Model (R104 rules as in enc32.py): movers M = pairs 0-5 (0..11) + K helpers (movers 16..16+K-1, levels 8..). Pairs 6-7 (12..15)
follow the target rows (clamped). Every option of a mover in M points to -1 or to a mover of M (never 12-15); the wiring is FREE
(one-hot), acyclic (W(m,z) -> before(owner(m), z), «before» a strict total order over M). Ranks free over the options of M (strict
total order, tournament without 3-cycles), signs free, helper gate bits free, helper starts free, helper states free per step.
Constraints: at each t < T0 every pair 0-5 mover that is free at S_t moves exactly as the target says (P = target next state);
helpers follow the R104 rule. Core gates (levels 0-7) from the base genome (o(7) is read from the clamped rows).
Movers outside M ∪ {12..15} are not modelled: nothing in M reads them, and they sit above M's levels except 12-15, so they never
change o(l) for a level of M (o(l) reads pairs 0..l only) -- except levels 8.. read o(7), which the clamp fixes.
Generalized (--H, default 8): lower pairs 0..H-3 constrained, pairs H-2, H-1 clamped, helpers 2H..2H+K-1.
Usage: osc.py BASE TARGET K T0 OUTPREFIX [--cnf F] [--H H]   (BASE: genome whose core gates are used; TARGET core8 rows)"""
import sys, os, time, hashlib, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from enc32 import Enc, rdgen, wrgen, rdtarget
ap = argparse.ArgumentParser(); ap.add_argument('base'); ap.add_argument('target'); ap.add_argument('K', type=int)
ap.add_argument('T0', type=int); ap.add_argument('out'); ap.add_argument('--cnf'); ap.add_argument('--H', type=int, default=8); a = ap.parse_args()
D = rdgen(a.base); S, NC = rdtarget(a.target); g = D['gate']; d = D['d']; N = 2 * d; K = a.K; T0 = a.T0; H = a.H
LOW = 2 * H - 4                      # movers of the lower pairs 0..H-3 (constrained); pairs H-2, H-1 clamped; helpers from 2H
assert NC == 2 * H and K % 2 == 0 and 2 * H + K <= N and H >= 3
M = list(range(LOW)) + list(range(2 * H, 2 * H + K)); Ms = set(M); OP = [2 * x + k for x in M for k in (0, 1)]
Lmax = (2 * H + K - 1) // 2
sinks = []; body = None
from pysat.solvers import Solver
sv = Solver(name='cadical195'); sinks.append(sv.add_clause)
if a.cnf:
    body = open(a.cnf + '.body', 'w'); sinks.append(lambda c: body.write(' '.join(map(str, c)) + ' 0\n'))
def sink(c):
    for f in sinks: f(c)
E = Enc(sink); t0 = time.time()
# wiring
W = {}
for m in OP:
    W[m] = {z: E.new() for z in [-1] + [z for z in M if z != m // 2]}
    E.add(list(W[m].values())); L = list(W[m].values())
    for i in range(len(L)):
        for j in range(i + 1, len(L)): E.add([-L[i], -L[j]])
bef = {}
def befl(x, z): return bef[(x, z)] if x < z else -bef[(z, x)]
for i, x in enumerate(M):
    for z in M[i + 1:]: bef[(x, z)] = E.new()
for i in range(len(M)):
    for j in range(i + 1, len(M)):
        for k in range(j + 1, len(M)):
            x, y, z = M[i], M[j], M[k]
            E.add([-befl(x, y), -befl(y, z), -befl(z, x)]); E.add([-befl(x, z), -befl(z, y), -befl(y, x)])
for m in OP:
    for z, v in W[m].items():
        if z >= 0: E.add([-v, befl(m // 2, z)])
# ranks, signs
ordv = {}
def ordl(e, f): return ordv[(e, f)] if e < f else -ordv[(f, e)]
for i, e in enumerate(OP):
    for f in OP[i + 1:]: ordv[(e, f)] = E.new()
for i in range(len(OP)):
    for j in range(i + 1, len(OP)):
        for k in range(j + 1, len(OP)):
            x, y, z = OP[i], OP[j], OP[k]
            E.add([-ordl(x, y), -ordl(y, z), -ordl(z, x)]); E.add([-ordl(x, z), -ordl(z, y), -ordl(y, x)])
pos = {m: E.new() for m in OP}
Gb = {(l, b): E.new() for l in range(H, Lmax + 1) for b in (0, 1)}
# states
st = []
for t in range(T0 + 1):
    row = {}
    for x in range(NC): row[x] = bool(S[t][x])
    for x in M[LOW:]: row[x] = E.new()
    st.append(row)
def okeys(row):
    o = {}; c = None
    for l in range(Lmax + 1):
        a_, b_ = row[2 * l], row[2 * l + 1]
        if l == 0: ol = g[0 + int(a_)] > g[2 + int(b_)]
        elif l < H: ol = (a_ != c) if a_ != b_ else (g[4 * l + int(a_)] > g[4 * l + 2 + int(a_)])
        else: ol = E.MUX(E.XOR(a_, b_), E.XOR(a_, c), E.MUX(a_, Gb[(l, 1)], Gb[(l, 0)]))
        o[l] = ol; c = ol
    return o
O = [okeys(st[t]) for t in range(T0 + 1)]
def ITE(c, a1, a0):
    return E.MUX(c, a1, a0)
nsites = 0
for t in range(T0):
    s = st[t]; ns = st[t + 1]; on = O[t + 1]
    # chain membership: R[m][e] = option e on the chain that starts at option m (at state s); Q[y][e] = from mover y
    R = {m: {e: (True if e == m else E.new()) for e in OP} for m in OP}
    Q = {y: {e: ITE(s[y], R[2 * y + 1][e], R[2 * y][e]) for e in OP} for y in M}
    for m in OP:
        for e in OP:
            if e == m: continue
            # R[m][e] <-> OR_z (W[m][z] & Q[z][e])
            terms = []
            for z, v in W[m].items():
                if z < 0: continue
                terms.append(E.AND(v, Q[z][e]))
            r = R[m][e]
            E.add([-r] + terms)
            for tm in terms: E.add([E.neg(tm), r])
    for x in M:
        l = x // 2
        free = (g[2 * x + 1 - int(s[x])] < g[2 * x + int(s[x])]) if l == 0 else E.XOR(s[x], on[l - 1])
        if x < LOW:
            if not free:
                if s[x] != ns[x]: raise SystemExit(f'target moves blocked mover {x} at t {t + 1}')
                continue
        if free is False: E.EQ(ns[x], s[x]); continue
        inA = {e: R[2 * x][e] for e in OP}; inB = {e: R[2 * x + 1][e] for e in OP}
        dl = {e: E.XOR(inA[e], inB[e]) for e in OP}; Uc = [e for e in OP if dl[e] is not False]
        P = E.new(); tau = {e: E.new() for e in Uc}; E.add([tau[e] for e in Uc]); nsites += 1
        for e in Uc:
            E.add([-tau[e], dl[e]])
            E.add([-tau[e], E.neg(inB[e]), -pos[e], P]); E.add([-tau[e], E.neg(inB[e]), pos[e], -P])
            E.add([-tau[e], E.neg(inA[e]), pos[e], P]); E.add([-tau[e], E.neg(inA[e]), -pos[e], -P])
            for f in Uc:
                if f != e: E.add([-tau[e], E.neg(dl[f]), ordl(e, f)])
        if free is True: E.EQ(ns[x], P)
        else: E.EQ(ns[x], E.MUX(free, P, s[x]))
info = dict(K=K, T0=T0, movers=len(M), options=len(OP), vars=E.nv, clauses=E.ncl, sites=nsites, build_s=round(time.time() - t0, 1))
print('OSC base', os.path.basename(a.base), hashlib.sha1(open(a.base, 'rb').read()).hexdigest()[:8], 'INFO', info, flush=True)
if a.cnf:
    body.close(); n = sum(1 for _ in open(a.cnf + '.body'))
    with open(a.cnf, 'w') as f:
        f.write(f'p cnf {E.nv} {n + (1 if E.empty else 0)}\n')
        if E.empty: f.write('0\n')
        for ln in open(a.cnf + '.body'): f.write(ln)
    os.remove(a.cnf + '.body'); print('CNF ->', a.cnf, flush=True)
if E.empty: print('RESULT UNSAT (empty clause at build)'); sys.exit()
t1 = time.time(); r = sv.solve(); print(f'SOLVE -> {"SAT" if r else "UNSAT"} {time.time() - t1:.1f}s', flush=True)
if not r: print('RESULT UNSAT'); sys.exit()
Mo = set(l for l in sv.get_model() if l > 0); val = lambda l: l if isinstance(l, bool) else ((l in Mo) if l > 0 else (-l not in Mo))
G = {k: (list(v) if isinstance(v, list) else v) for k, v in D.items()}
for m in range(2 * N):
    if m // 2 in Ms:
        ch = [z for z, v in W[m].items() if val(v)]; assert len(ch) == 1; G['xt'][m] = ch[0]
    elif m // 2 >= 2 * H: G['xt'][m] = -1                      # unmodelled helpers: exits, unread
wins = {e: sum(1 for f in OP if f != e and val(ordl(e, f))) for e in OP}; assert len(set(wins.values())) == len(OP)
rest = [m for m in range(2 * N) if m not in set(OP)]
G['br'] = [0] * (2 * N)
for i, m in enumerate(rest): G['br'][m] = i
for i, m in enumerate(sorted(OP, key=lambda e: wins[e])): G['br'][m] = len(rest) + i
G['bp'] = [(0 if val(pos[m]) else 1) if m in pos else D['bp'][m] for m in range(2 * N)]
gt = list(g)
for (l, b), lit in Gb.items():
    hi, lo = (4 * l + b, 4 * l + 2 + b) if val(lit) else (4 * l + 2 + b, 4 * l + b)
    pr = sorted([gt[hi], gt[lo]]); gt[hi], gt[lo] = pr[1], pr[0]
G['gate'] = gt
G['start'] = [int(S[0][x]) if x < NC else (int(val(st[0][x])) if x in Ms else D['start'][x]) for x in range(N)]
wrgen(G, a.out + '_dec.txt'); print('RESULT SAT decoded ->', a.out + '_dec.txt', hashlib.sha1(open(a.out + '_dec.txt', 'rb').read()).hexdigest())
