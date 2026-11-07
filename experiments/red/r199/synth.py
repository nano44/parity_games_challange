#!/usr/bin/env python3
"""L-RED R199 SYNTH: z3 synthesis of an IDEAL-ACYC genome (RESULTS R104 model; degree 2; any width) with a PRESCRIBED (partial)
move schedule. Generalises r197/bmcfork.py: movers are listed with levels and the W-targets of their two options (main ladder
movers u_l = 2l, v_l = 2l + 1; extra «helper» movers after them, W-leaves). Free: Xi-targets (acyclic by positions; per spec may be
fixed), gates (distinct), weights (REL=1: distinct nonzero integers, a relaxation; default exact: +-2^rank, distinct ranks), start
(unless fixed). Constraints: L consecutive IDEAL steps, each with a move (as bmcfork), plus
  sched[v] = list of steps (1..L) at which v moves (exactly those), for every v with a schedule;
  ftot = {l: k}: R_l (key order of u_l, v_l) flips at >= k of the steps 1..L (TOTAL count, step 1 included);
  fexact = {l: [steps]}: R_l flips exactly at those steps.
Spec JSON: {"d":, "L":, "movers": [[lev, [W0, W1]], ...] (W = -1 at level 0), "sched": {v: [...]}, "start": {v: 0/1},
"xt": {"v,k": target}, "ftot": {...}, "fexact": {...}, "xtallow": {v: [allowed targets]}}. Usage: synth.py spec.json out.json
Writes a genome (exact mode) in the r187/ideal.py format, or a FIX structure (REL mode). Exact SAT is checked by replaying with
r187/ideal.py (the replay must reproduce the schedule)."""
import sys, os, json
import z3
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
spec = json.load(open(sys.argv[1])); out = sys.argv[2]
d, L = spec["d"], spec["L"]; MV = spec["movers"]; N = len(MV); lev = [m[0] for m in MV]; WT = [m[1] for m in MV]
faces = [(v, k) for v in range(N) for k in (0, 1)]; M = len(faces)
REL = os.environ.get("REL") == "1"; FIX = os.environ.get("FIX")
S = z3.Solver()
if os.environ.get("TMO"): S.set("timeout", int(os.environ["TMO"]) * 1000)
xt = {f: z3.Int(f"x{f}") for f in faces}; pos = [z3.Int(f"pos{v}") for v in range(N)]; gate = {f: z3.Int(f"g{f}") for f in faces}
S.add(z3.Distinct(*gate.values()))
allow = {int(k): v for k, v in spec.get("xtallow", {}).items()}
for f in faces:
    S.add(gate[f] >= 0, gate[f] < M, xt[f] >= -1, xt[f] < N, xt[f] != f[0])
    if f[0] in allow: S.add(z3.Or([xt[f] == a for a in allow[f[0]]]))
    for u in range(N): S.add(z3.Implies(xt[f] == u, pos[u] > pos[f[0]]))
for key, val in spec.get("xt", {}).items():
    v, k = map(int, key.split(",")); S.add(xt[(v, k)] == val)
for v in range(N):
    if lev[v] == 0: S.add(gate[(v, 0)] < gate[(v, 1)])   # level-0 options are symmetric (bmc3 symmetry (i))
if FIX:
    R = json.load(open(FIX))
    for v, k in faces: S.add(xt[(v, k)] == R["xt"][f"{v},{k}"], gate[(v, k)] == R["gate"][f"{v},{k}"])
if REL:
    Wt = {f: z3.Int(f"w{f}") for f in faces}; S.add(z3.Distinct(*Wt.values())); S.add(*[Wt[f] != 0 for f in faces])
else:
    rank = {f: z3.Int(f"r{f}") for f in faces}; par = {f: z3.Bool(f"p{f}") for f in faces}
    S.add(z3.Distinct(*rank.values())); S.add(*[z3.And(rank[f] >= 0, rank[f] < M) for f in faces])
    Wt = {f: z3.If(par[f], -1, 1) * z3.Sum([z3.If(rank[f] == r, 2 ** r, 0) for r in range(M)]) for f in faces}
sig = [[z3.Bool(f"s{t}_{v}") for v in range(N)] for t in range(L + 1)]
sched = {int(k): set(v) for k, v in spec.get("sched", {}).items()}
for v, st in sched.items():
    for t in range(1, L + 1): S.add((sig[t][v] != sig[t - 1][v]) == (t in st))
for k, b in spec.get("start", {}).items(): S.add(sig[0][int(k)] == bool(b))
if FIX:
    for v in range(N): S.add(sig[0][v] == bool(R["start"][v]))
keyed = sorted({w for v in range(N) for w in WT[v] if w >= 0} | set(range(2 * d)))
LS = []
for t in range(L + 1):
    X = [z3.Int(f"X{t}_{u}") for u in range(N)]
    def Fv(v, k, X=X): return Wt[(v, k)] + z3.Sum([z3.If(xt[(v, k)] == u, X[u], 0) for u in range(N)])
    for u in range(N): S.add(X[u] == z3.If(sig[t][u], Fv(u, 1), Fv(u, 0)))
    # keys of state t: less[(x, y)] for keyed x, y of the same level
    less = {}
    def g_of(v, b): return z3.If(b, gate[(v, 1)], gate[(v, 0)])
    for l in range(d):
        vs = [v for v in keyed if lev[v] == l]
        for x in vs:
            for y in vs:
                if x == y: continue
                if l == 0: less[(x, y)] = g_of(x, sig[t][x]) < g_of(y, sig[t][y]); continue
                def cmp(kx, ky):
                    a, b = WT[x][kx], WT[y][ky]
                    return (gate[(x, kx)] < gate[(y, ky)]) if a == b else less[(a, b)]
                sx, sy = sig[t][x], sig[t][y]
                less[(x, y)] = z3.If(sx, z3.If(sy, cmp(1, 1), cmp(1, 0)), z3.If(sy, cmp(0, 1), cmp(0, 0)))
    def k0less(v):
        if lev[v] == 0: return gate[(v, 0)] < gate[(v, 1)]
        a, b = WT[v]
        return (gate[(v, 0)] < gate[(v, 1)]) if a == b else less[(a, b)]
    LS.append(dict(R=[less[(2 * l, 2 * l + 1)] for l in range(d)], K=[k0less(v) for v in range(N)], X=X, Fv=Fv))
for t in range(L):
    A, B = LS[t], LS[t + 1]
    for v in range(N):
        both = z3.And(z3.Or(z3.Not(sig[t][v]), A["Fv"](v, 0) > A["Fv"](v, 1)), z3.Or(sig[t][v], A["Fv"](v, 1) > A["Fv"](v, 0)))
        S.add(sig[t + 1][v] == z3.If(both, z3.Not(B["K"][v]), sig[t][v]))
    S.add(z3.Or([sig[t + 1][v] != sig[t][v] for v in range(N)]))
for l, k in spec.get("ftot", {}).items():
    l = int(l); S.add(z3.Sum([z3.If(LS[t]["R"][l] != LS[t + 1]["R"][l], 1, 0) for t in range(L)]) >= k)
for l, st in spec.get("fexact", {}).items():
    l = int(l); st = set(st)
    for t in range(L): S.add((LS[t]["R"][l] != LS[t + 1]["R"][l]) == ((t + 1) in st))
BLOCK = os.environ.get("BLOCK")
if BLOCK and os.path.exists(BLOCK):
    for Bk in json.load(open(BLOCK)):
        S.add(z3.Not(z3.And(*[xt[(v, k)] == Bk["xt"][f"{v},{k}"] for v, k in faces], *[gate[(v, k)] == Bk["gate"][f"{v},{k}"] for v, k in faces],
                             *[sig[0][v] == bool(Bk["start"][v]) for v in range(N)])))
r = S.check(); print("SYNTH", sys.argv[1], "N", N, "d", d, "L", L, "REL", int(REL), "FIX", int(bool(FIX)), "->", r, flush=True)
if r == z3.sat:
    m = S.model(); ev = lambda e: m.eval(e, model_completion=True)
    if REL:
        json.dump(dict(xt={f"{v},{k}": ev(xt[(v, k)]).as_long() for v, k in faces}, gate={f"{v},{k}": ev(gate[(v, k)]).as_long() for v, k in faces},
                       start=[1 if z3.is_true(ev(sig[0][v])) else 0 for v in range(N)]), open(out, "w")); print("REL model written", out)
    else:
        import ideal
        order = sorted(range(N), key=lambda v: ev(pos[v]).as_long())
        G = dict(N=N, lev=lev, deg=2, opts=[[[WT[v][k], ev(xt[(v, k)]).as_long(), 2 * v + k] for k in (0, 1)] for v in range(N)],
                 gate=[[ev(gate[(v, k)]).as_long() for k in (0, 1)] for v in range(N)], br=[ev(rank[f]).as_long() for f in faces],
                 bp=[1 if z3.is_true(ev(par[f])) else 0 for f in faces], start=[1 if z3.is_true(ev(sig[0][v])) else 0 for v in range(N)], xorder=order)
        json.dump(G, open(out, "w")); Sx, why = ideal.traj(G, cap=100000)
        ok = all(tuple(1 if z3.is_true(ev(sig[t][v])) else 0 for v in range(N)) == Sx[t] for t in range(min(L + 1, len(Sx))))
        print("replay L", len(Sx) - 1, why, "matches model prefix:", ok, "genome", out)
