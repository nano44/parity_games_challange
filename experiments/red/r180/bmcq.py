#!/usr/bin/env python3
"""L-RED R180 BMC: z3 bounded model check of the IDEAL model (fastabs semantics) on a W-ladder of depth d, width 2, deg 2.
Everything free: Xi-targets (acyclic via positions), beta ranks / parities (one per option), gate indices, start. The run is N5's
deterministic S4a dynamics; asks for L consecutive sigma-changing steps (no fallback). SAT => writes a fastabs genome and replays
it. Usage: bmc.py d L out.json"""
import sys, os, json
import z3
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r177"))
import fastabs as F
d, L, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]; N = 2 * d; lev = [v // 2 for v in range(N)]
faces = [(v, k) for v in range(N) for k in (0, 1)]; M = len(faces)
S = z3.Solver()
rank = {f: z3.Int(f"r{f}") for f in faces}; par = {f: z3.Bool(f"p{f}") for f in faces}
xt = {f: z3.Int(f"x{f}") for f in faces}; pos = [z3.Int(f"pos{v}") for v in range(N)]; gate = {f: z3.Int(f"g{f}") for f in faces}
S.add(z3.Distinct(*rank.values()), z3.Distinct(*gate.values()))
for f in faces:
    S.add(rank[f] >= 0, rank[f] < M, gate[f] >= 0, gate[f] < M, xt[f] >= -1, xt[f] < N, xt[f] != f[0])
    for u in range(N): S.add(z3.Implies(xt[f] == u, pos[u] > pos[f[0]]))
Wt = {f: z3.If(par[f], -1, 1) * z3.Sum([z3.If(rank[f] == r, 2 ** r, 0) for r in range(M)]) for f in faces}
sig = [[z3.Bool(f"s{t}_{v}") for v in range(N)] for t in range(L + 1)]     # True = option 1
def opt(t, v): return z3.If(sig[t][v], 1, 0)
for t in range(L + 1):
    X = [z3.Int(f"X{t}_{u}") for u in range(N)]
    def Fv(v, k): return Wt[(v, k)] + z3.Sum([z3.If(xt[(v, k)] == u, X[u], 0) for u in range(N)])
    for u in range(N): S.add(X[u] == z3.If(sig[t][u], Fv(u, 1), Fv(u, 0)))
    if t == L: break
    # availability at state t
    av = {}
    for v in range(N):
        av[(v, 0)] = z3.Or(z3.Not(sig[t][v]), Fv(v, 0) > Fv(v, 1)); av[(v, 1)] = z3.Or(sig[t][v], Fv(v, 1) > Fv(v, 0))
    # keys in the NEW tree (state t+1): lessv[x][y] for x, y on the same level: key_{t+1}(x) < key_{t+1}(y)
    less = {}
    def g_of(v, b): return z3.If(b, gate[(v, 1)], gate[(v, 0)])
    for l in range(d):
        vs = [v for v in range(N) if lev[v] == l]
        for x in vs:
            for y in vs:
                if x == y: continue
                gx, gy = g_of(x, sig[t + 1][x]), g_of(y, sig[t + 1][y])
                if l == 0: less[(x, y)] = gx < gy
                else:
                    a, b = 2 * (l - 1), 2 * (l - 1) + 1
                    same = sig[t + 1][x] == sig[t + 1][y]
                    tx = sig[t + 1][x]; ty = sig[t + 1][y]
                    lowless = z3.If(tx, less[(b, a)], less[(a, b)])  # targets differ: tx -> b, ty -> a (or reverse)
                    less[(x, y)] = z3.If(same, gx < gy, lowless)
    # option keys of v in the new tree: compare option 0 vs option 1 of v
    for v in range(N):
        if lev[v] == 0: k0less = gate[(v, 0)] < gate[(v, 1)]
        else: k0less = less[(2 * (lev[v] - 1), 2 * (lev[v] - 1) + 1)]
        # chosen = key-least among available
        both = z3.And(av[(v, 0)], av[(v, 1)])
        S.add(sig[t + 1][v] == z3.If(both, z3.Not(k0less), sig[t][v]))
Q = os.environ["Q"]
mv = lambda v: z3.Sum([z3.If(sig[t + 1][v] != sig[t][v], 1, 0) for t in range(L)])
if Q.startswith("moves"):           # moves:v:k  -> can vertex v move >= k times within L steps?
    _, v, k = Q.split(":"); S.add(mv(int(v)) >= int(k))
elif Q.startswith("late"):          # late:v:t   -> can vertex v move at a step >= t?
    _, v, t0 = Q.split(":"); S.add(z3.Or([sig[t + 1][int(v)] != sig[t][int(v)] for t in range(int(t0) - 1, L)]))
elif Q.startswith("total"):         # total:k   -> >= k moves in all
    S.add(z3.Sum([mv(v) for v in range(N)]) >= int(Q.split(":")[1]))
r = S.check(); print("Q", Q, "d", d, "L", L, "->", r, flush=True)
if False:
    m = S.model(); ev = lambda e: m.eval(e, model_completion=True)
    order = sorted(range(N), key=lambda v: ev(pos[v]).as_long())
    G = dict(N=N, lev=lev, deg=2, opts=[[[-1 if lev[v] == 0 else 2 * (lev[v] - 1) + k, ev(xt[(v, k)]).as_long(), 2 * v + k] for k in (0, 1)] for v in range(N)],
             gate=[[ev(gate[(v, k)]).as_long() for k in (0, 1)] for v in range(N)], br=[ev(rank[f]).as_long() for f in faces],
             bp=[1 if z3.is_true(ev(par[f])) else 0 for f in faces], start=[1 if z3.is_true(ev(sig[0][v])) else 0 for v in range(N)], xorder=order)
    json.dump(G, open(out, "w")); print("replay", F.simulate(G))
