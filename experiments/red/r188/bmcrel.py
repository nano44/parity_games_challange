#!/usr/bin/env python3
"""L-RED R188 BMCREL: RELAXATION of bmc3 (every beta weight a free integer instead of +-2^rank; ranks/parities unused). Every IDEAL-ACYC
ladder instance is an instance of this model, so UNSAT here is an upper bound for IDEAL-ACYC; SAT needs a replay check. Based on: BMC3 = R180 bmc.py + symmetry breaking (valid symmetries of the 2-wide ladder): (i) at level 0 the two options of a vertex
are interchangeable (both W-faces go to c_W): gate(v,0) < gate(v,1); (ii) swapping the two vertices of level l together with options 0/1 of
every level-(l+1) vertex is a symmetry: pos(2l) <= pos(2l+1) (pos = acyclic Xi-order). Original R180 text: L-RED R180 BMC: z3 bounded model check of the IDEAL model (fastabs semantics) on a W-ladder of depth d, width 2, deg 2.
Everything free: Xi-targets (acyclic via positions), beta ranks / parities (one per option), gate indices, start. The run is N5's
deterministic S4a dynamics; asks for L consecutive sigma-changing steps (no fallback). SAT => writes a fastabs genome and replays
it. Usage: bmc.py d L out.json"""
import sys, os, json
import z3
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r177"))
SYM = os.environ.get("SYM", "1") == "1"
import fastabs as F
d, L, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]; N = 2 * d; lev = [v // 2 for v in range(N)]
faces = [(v, k) for v in range(N) for k in (0, 1)]; M = len(faces)
S = z3.Solver()
rank = {f: z3.Int(f"r{f}") for f in faces}; par = {f: z3.Bool(f"p{f}") for f in faces}
xt = {f: z3.Int(f"x{f}") for f in faces}; pos = [z3.Int(f"pos{v}") for v in range(N)]; gate = {f: z3.Int(f"g{f}") for f in faces}
S.add(z3.Distinct(*gate.values()))
for f in faces:
    S.add(gate[f] >= 0, gate[f] < M, xt[f] >= -1, xt[f] < N, xt[f] != f[0])
    for u in range(N): S.add(z3.Implies(xt[f] == u, pos[u] > pos[f[0]]))
if SYM:
    for v in range(N):
        if lev[v] == 0: S.add(gate[(v, 0)] < gate[(v, 1)])
    for l in range(d): S.add(pos[2 * l] <= pos[2 * l + 1])
Wt = {f: z3.Int(f'w{f}') for f in faces}
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
    S.add(z3.Or([sig[t + 1][v] != sig[t][v] for v in range(N)]))
r = S.check(); print("BMCREL d", d, "L", L, "->", r, flush=True)
if r == z3.sat:
    m = S.model(); ev = lambda e: m.eval(e, model_completion=True)
    R = dict(d=d, L=L, xt={f"{v},{k}": ev(xt[(v, k)]).as_long() for v, k in faces}, gate={f"{v},{k}": ev(gate[(v, k)]).as_long() for v, k in faces},
             w={f"{v},{k}": ev(Wt[(v, k)]).as_long() for v, k in faces}, start=[1 if z3.is_true(ev(sig[0][v])) else 0 for v in range(N)],
             sig=[[1 if z3.is_true(ev(sig[t][v])) else 0 for v in range(N)] for t in range(L + 1)])
    json.dump(R, open(out, "w")); print(R)
