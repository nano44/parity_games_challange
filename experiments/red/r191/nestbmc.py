#!/usr/bin/env python3
"""L-RED R191 NESTBMC (copy of r190/clockbmc.py; PIFIX=1 adds the forced pi of R191 §3: every v_j (j <= d-2) < v_(d-1) < u_(d-1) < u_(d-2);
sound to add for d >= 3 by R191 Lemma NEST-PI; LEM=1 adds the redundant lemma clauses). R190 CLOCKBMC: z3 bounded model of the IDEAL-ACYC model (fastabs semantics: acyclic Xi via positions, face value = signed
2^rank sum along the chain; REL=1: free distinct integer weights instead, a relaxation) on a W-ladder of depth d, width w, degree D:
movers w*l + i at level l; option k of a level-l >= 1 mover has W-target w*(l-1) + (k mod w); level 0 -> c_W. Keys: TB lex-min
(key(target) . gate); step = keep-or-improve availability (state t), key-least choice (state t+1).
Schedule: u_l := w*l, v_l := w*l + 1 must move EXACTLY as in NEST(d) (r189/lag/schedbmc.py); the other movers (clocks) are free.
Usage: clockbmc.py d w D [L] out.json"""
import sys, os, json
import z3
d, w, D = map(int, sys.argv[1:4]); out = sys.argv[-1]; N = w * d; lev = [v // w for v in range(N)]
def nest(d):
    ev = {}
    def R(l, t):
        if l == d: return 0
        ev.setdefault(t, set()).add(w * l); Dd = R(l + 1, t) or 1
        ev.setdefault(t + Dd, set()).add(w * l + 1); R(l + 1, t + Dd); return 2 * Dd
    R(0, 1); T = max(ev); return [sorted(ev.get(t, [])) for t in range(1, T + 1)]
sched = json.loads(os.environ["SCHED"]) if os.environ.get("SCHED") else nest(d)
L = int(sys.argv[4]) if len(sys.argv) > 5 else len(sched); sched = sched[:L]
UV = {w * l for l in range(d)} | {w * l + 1 for l in range(d)}
print("schedule (u/v only)", sched, flush=True)
tgt = lambda v, k: -1 if lev[v] == 0 else w * (lev[v] - 1) + (k % w)
faces = [(v, k) for v in range(N) for k in range(D)]; M = len(faces)
S = z3.Solver(); REL = os.environ.get("REL") == "1"
gate = {f: z3.Int(f"g{f}") for f in faces}; xt = {f: z3.Int(f"x{f}") for f in faces}; pos = [z3.Int(f"pos{v}") for v in range(N)]
S.add(z3.Distinct(*gate.values()))
if REL:
    Wt = {f: z3.Int(f"w{f}") for f in faces}; S.add(z3.Distinct(*Wt.values()))
    for f in faces: S.add(Wt[f] != 0)
else:
    rank = {f: z3.Int(f"r{f}") for f in faces}; par = {f: z3.Bool(f"p{f}") for f in faces}; S.add(z3.Distinct(*rank.values()))
    for f in faces: S.add(rank[f] >= 0, rank[f] < M)
    Wt = {f: z3.If(par[f], -1, 1) * z3.Sum([z3.If(rank[f] == r, 2 ** r, 0) for r in range(M)]) for f in faces}
for f in faces:
    S.add(gate[f] >= 0, gate[f] < M, xt[f] >= -1, xt[f] < N, xt[f] != f[0])
    for u in range(N): S.add(z3.Implies(xt[f] == u, pos[u] > pos[f[0]]))
if os.environ.get("PIFIX") == "1":
    S.add(*[pos[w * l + 1] < pos[w * (d - 1) + 1] for l in range(d - 1)]); S.add(pos[w * (d - 1) + 1] < pos[w * (d - 1)])
    S.add(pos[w * (d - 1)] < pos[w * (d - 2)])
c = [[z3.Int(f"c{t}_{v}") for v in range(N)] for t in range(L + 1)]
for t in range(L + 1):
    for v in range(N): S.add(c[t][v] >= 0, c[t][v] < D)
def optless(v, k, k2, less):
    if lev[v] == 0 or tgt(v, k) == tgt(v, k2): return gate[(v, k)] < gate[(v, k2)]
    return less[(tgt(v, k), tgt(v, k2))]
for t in range(L + 1):
    X = [z3.Int(f"X{t}_{u}") for u in range(N)]
    def Fv(v, k): return Wt[(v, k)] + z3.Sum([z3.If(xt[(v, k)] == u, X[u], 0) for u in range(N)])
    for u in range(N): S.add(X[u] == z3.Sum([z3.If(c[t][u] == k, Fv(u, k), 0) for k in range(D)]))
    if t == L: break
    av = {(v, k): z3.Or(c[t][v] == k, Fv(v, k) > X[v]) for v in range(N) for k in range(D)}
    less = {}
    for l in range(d):
        vs = [v for v in range(N) if lev[v] == l]
        for x in vs:
            for y in vs:
                if x == y: continue
                cases = []
                for kx in range(D):
                    for ky in range(D):
                        if l == 0 or tgt(x, kx) == tgt(y, ky): cond = gate[(x, kx)] < gate[(y, ky)]
                        else: cond = less[(tgt(x, kx), tgt(y, ky))]
                        cases.append(z3.And(c[t + 1][x] == kx, c[t + 1][y] == ky, cond))
                less[(x, y)] = z3.Or(cases)
    for v in range(N):
        for k in range(D):
            S.add(z3.Implies(c[t + 1][v] == k, z3.And(av[(v, k)], *[z3.Implies(av[(v, k2)], optless(v, k, k2, less)) for k2 in range(D) if k2 != k])))
        if v in UV: S.add((c[t + 1][v] != c[t][v]) == (v in sched[t]))
    S.add(z3.Or([c[t + 1][v] != c[t][v] for v in range(N)]))
if os.environ.get("LEM") == "1":
    # redundant clauses from proved lane lemmas (R191): reach = Xi-reachability; ROT-CAP (D consecutive moves of x need a desc(x) move
    # in [first, last - 1]); XI-NEW (a least-level mover of step >= 2 has a desc that moved one step earlier)
    reach = [[z3.Bool(f"re{x}_{y}") for y in range(N)] for x in range(N)]
    for x in range(N):
        for y in range(N):
            S.add(reach[x][y] == z3.Or([z3.Or(xt[(x, k)] == y, z3.Or([z3.And(xt[(x, k)] == z, reach[z][y]) for z in range(N) if z != x])) for k in range(D)]))
        S.add(z3.Not(reach[x][x]))
    mvd = [[c[t + 1][v] != c[t][v] for v in range(N)] for t in range(L)]
    import itertools
    for x in range(N):
        for ts in itertools.combinations(range(L), D):
            a0, b0 = ts[0], ts[-1]
            cons = z3.And(*[mvd[q][x] for q in ts], *[z3.Not(mvd[q][x]) for q in range(a0, b0 + 1) if q not in ts])
            S.add(z3.Implies(cons, z3.Or([z3.And(reach[x][y], z3.Or([mvd[q][y] for q in range(a0, b0)])) for y in range(N) if y != x])))
    for t in range(1, L):
        for x in range(N):
            S.add(z3.Implies(z3.And(mvd[t][x], *[z3.Not(mvd[t][u]) for u in range(N) if lev[u] < lev[x]]), z3.Or([z3.And(reach[x][y], mvd[t - 1][y]) for y in range(N) if y != x])))
r = S.check(); print(f"CLOCKBMC d {d} w {w} D {D} L {L} REL {int(REL)} -> {r}", flush=True)
if r == z3.sat:
    m = S.model(); ev = lambda e: m.eval(e, model_completion=True).as_long()
    S2 = [[ev(c[t][v]) for v in range(N)] for t in range(L + 1)]
    print("moves", [sorted(v for v in range(N) if S2[t][v] != S2[t - 1][v]) for t in range(1, L + 1)])
    if not REL:
        G = dict(N=N, lev=lev, deg=D, opts=[[[tgt(v, k), ev(xt[(v, k)]), D * v + k] for k in range(D)] for v in range(N)],
                 gate=[[ev(gate[(v, k)]) for k in range(D)] for v in range(N)], br=[ev(rank[f]) for f in faces],
                 bp=[1 if z3.is_true(m.eval(par[f], model_completion=True)) else 0 for f in faces], start=S2[0])
        json.dump(G, open(out, "w"))
    else: json.dump(dict(xt={f"{v},{k}": ev(xt[(v, k)]) for v, k in faces}, gate={f"{v},{k}": ev(gate[(v, k)]) for v, k in faces}, start=S2[0]), open(out, "w"))
