#!/usr/bin/env python3
"""L-RED R189 SCHEDBMC: does an IDEAL-ACYC 2-wide deg-2 LADDER (R188 bmc3 encoding, fastabs semantics: acyclic Xi via positions,
value = signed 2^rank sum along the chain) realise a GIVEN move schedule exactly (the set of movers that move at each step)?
Schedule NEST(d) (the doubling counter, docs/red/R189-lag.md): R_l(t) = u_l moves at t, then R_(l+1)(t), then v_l moves at
t + D_(l+1), then R_(l+1)(t + D_(l+1)); D_d = 1, D_l = 2 D_(l+1); level 0: u_0 at 1, R_1(1), v_0 at 1 + D_1, R_1(1 + D_1). L = 2^d.
Usage: schedbmc.py d [L] out.json   (L < 2^d asks for the prefix of length L).  Env SCHED=custom json list of mover lists;\nCOUNT=l:K (with L given) drops the schedule and asks for >= K moves at level l in a fallback-free run of L steps."""
import sys, os, json
import z3
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "r177"))
import fastabs as F
d = int(sys.argv[1]); out = sys.argv[-1]; N = 2 * d; lev = [v // 2 for v in range(N)]
def nest(d):
    ev = {}
    def R(l, t):
        if l == d: return 0
        ev.setdefault(t, set()).add(2 * l); D = R(l + 1, t) or 1
        ev.setdefault(t + D, set()).add(2 * l + 1); R(l + 1, t + D); return 2 * D
    R(0, 1); T = max(ev); return [sorted(ev.get(t, [])) for t in range(1, T + 1)]
COUNT = os.environ.get("COUNT")    # "l:K": no schedule; at least K moves at level l, every step changes sigma
sched = json.loads(os.environ["SCHED"]) if os.environ.get("SCHED") else nest(d)
L = int(sys.argv[2]) if len(sys.argv) > 3 else len(sched); sched = sched[:L] if not COUNT else None
print("schedule", sched, flush=True)
faces = [(v, k) for v in range(N) for k in (0, 1)]; M = len(faces)
S = z3.Solver()
rank = {f: z3.Int(f"r{f}") for f in faces}; par = {f: z3.Bool(f"p{f}") for f in faces}
xt = {f: z3.Int(f"x{f}") for f in faces}; pos = [z3.Int(f"pos{v}") for v in range(N)]; gate = {f: z3.Int(f"g{f}") for f in faces}
S.add(z3.Distinct(*rank.values()), z3.Distinct(*gate.values()))
for f in faces:
    S.add(rank[f] >= 0, rank[f] < M, gate[f] >= 0, gate[f] < M, xt[f] >= -1, xt[f] < N, xt[f] != f[0])
    for u in range(N): S.add(z3.Implies(xt[f] == u, pos[u] > pos[f[0]]))
Wt = {f: z3.If(par[f], -1, 1) * z3.Sum([z3.If(rank[f] == r, 2 ** r, 0) for r in range(M)]) for f in faces}
sig = [[z3.Bool(f"s{t}_{v}") for v in range(N)] for t in range(L + 1)]
for t in range(L + 1):
    X = [z3.Int(f"X{t}_{u}") for u in range(N)]
    def Fv(v, k): return Wt[(v, k)] + z3.Sum([z3.If(xt[(v, k)] == u, X[u], 0) for u in range(N)])
    for u in range(N): S.add(X[u] == z3.If(sig[t][u], Fv(u, 1), Fv(u, 0)))
    if t == L: break
    av = {}
    for v in range(N):
        av[(v, 0)] = z3.Or(z3.Not(sig[t][v]), Fv(v, 0) > Fv(v, 1)); av[(v, 1)] = z3.Or(sig[t][v], Fv(v, 1) > Fv(v, 0))
    less = {}
    def g_of(v, b): return z3.If(b, gate[(v, 1)], gate[(v, 0)])
    for l in range(d):
        vs = [2 * l, 2 * l + 1]
        for x in vs:
            for y in vs:
                if x == y: continue
                gx, gy = g_of(x, sig[t + 1][x]), g_of(y, sig[t + 1][y])
                if l == 0: less[(x, y)] = gx < gy
                else:
                    a, b = 2 * (l - 1), 2 * (l - 1) + 1
                    same = sig[t + 1][x] == sig[t + 1][y]
                    lowless = z3.If(sig[t + 1][x], less[(b, a)], less[(a, b)])
                    less[(x, y)] = z3.If(same, gx < gy, lowless)
    for v in range(N):
        k0less = gate[(v, 0)] < gate[(v, 1)] if lev[v] == 0 else less[(2 * (lev[v] - 1), 2 * (lev[v] - 1) + 1)]
        both = z3.And(av[(v, 0)], av[(v, 1)])
        S.add(sig[t + 1][v] == z3.If(both, z3.Not(k0less), sig[t][v]))
        if sched is not None: S.add((sig[t + 1][v] != sig[t][v]) == (v in sched[t]))
    if sched is None: S.add(z3.Or([sig[t + 1][v] != sig[t][v] for v in range(N)]))
if COUNT:
    cl, cK = map(int, COUNT.split(":"))
    S.add(z3.Sum([z3.If(sig[t + 1][v] != sig[t][v], 1, 0) for t in range(L) for v in (2 * cl, 2 * cl + 1)]) >= cK)
r = S.check(); print("SCHEDBMC d", d, "L", L, "->", r, flush=True)
if r == z3.sat:
    m = S.model(); ev = lambda e: m.eval(e, model_completion=True)
    G = dict(N=N, lev=lev, deg=2, opts=[[[-1 if lev[v] == 0 else 2 * (lev[v] - 1) + k, ev(xt[(v, k)]).as_long(), 2 * v + k] for k in (0, 1)] for v in range(N)],
             gate=[[ev(gate[(v, k)]).as_long() for k in (0, 1)] for v in range(N)], br=[ev(rank[f]).as_long() for f in faces],
             bp=[1 if z3.is_true(ev(par[f])) else 0 for f in faces], start=[1 if z3.is_true(ev(sig[0][v])) else 0 for v in range(N)])
    json.dump(G, open(out, "w")); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "r187")); import ideal; S2, why = ideal.traj(G); print("replay L", len(S2) - 1, why, "moves", [sorted(v for v in range(N) if S2[j][v] != S2[j - 1][v]) for j in range(1, len(S2))])
