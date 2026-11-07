#!/usr/bin/env python3
"""L-RED R199 XISAT: exact Xi-synthesis for a prescribed run as a pure boolean problem (z3): one-hot Xi-targets with an acyclic
order, chain membership in_s[u][f] (face f on the chain of u's current option at state s), a strict total order lt[f][g] on the
faces (rank f < rank g) and parities. A requirement (s, x, bit) (r199/req.py) holds iff the top face of the symmetric difference
of the two option chains of x is GOOD (in the bit-option's chain and even, or in the other chain and odd); encoded as: every BAD
face of the symmetric difference is below some GOOD face of it. UNSAT is an exact obstruction for the prescribed run (given its
W side). Usage: xisat.py target.json out.json   (env TMO seconds; XTALLOW=json {mover: [targets]} optional)"""
import sys, os, json, time
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import z3, req as RQ
def solve(lev, WT, S, req, tmo=None, allow=None, fixxt=None):
    N = len(lev); faces = [(v, k) for v in range(N) for k in (0, 1)]; M = len(faces); fi = {f: i for i, f in enumerate(faces)}
    Z = z3.SolverFor("QF_FD") if os.environ.get("FD") == "1" else z3.Solver()
    if tmo: Z.set("timeout", tmo * 1000)
    T = range(-1, N)
    b = {(f, u): z3.Bool(f"b{fi[f]}_{u}") for f in faces for u in T if u != f[0]}
    before = {(v, w): z3.Bool(f"o{v}_{w}") for v in range(N) for w in range(N) if v != w}   # v strictly before w in the Xi order
    for v in range(N):
        for w in range(N):
            if v < w: Z.add(before[(v, w)] != before[(w, v)])
            for x in range(N):
                if len({v, w, x}) == 3: Z.add(z3.Implies(z3.And(before[(v, w)], before[(w, x)]), before[(v, x)]))
    for f in faces:
        opts = [b[(f, u)] for u in T if u != f[0]]
        Z.add(z3.PbEq([(o, 1) for o in opts], 1))
        for u in range(N):
            if u != f[0]:
                Z.add(z3.Implies(b[(f, u)], before[(f[0], u)]))
                if allow is not None and u not in allow.get(f[0], range(N)): Z.add(z3.Not(b[(f, u)]))
        if fixxt is not None and f in fixxt:
            Z.add(b[(f, fixxt[f])])
    lt = {(i, j): z3.Bool(f"l{i}_{j}") for i in range(M) for j in range(M) if i != j}
    for i in range(M):
        for j in range(i + 1, M): Z.add(lt[(i, j)] != lt[(j, i)])
    for i in range(M):
        for j in range(M):
            for k in range(M):
                if len({i, j, k}) == 3: Z.add(z3.Implies(z3.And(lt[(i, j)], lt[(j, k)]), lt[(i, k)]))
    par = [z3.Bool(f"odd{i}") for i in range(M)]
    need = sorted({s for (s, x) in req}); IN = {}
    for s in need:
        for u in range(N):
            for f in faces: IN[(s, u, f)] = z3.Bool(f"in{s}_{u}_{fi[f]}")
        for u in range(N):
            cf = (u, S[s][u])
            for f in faces:
                if f == cf: Z.add(IN[(s, u, f)]); continue
                Z.add(IN[(s, u, f)] == z3.Or([z3.And(b[(cf, w)], IN[(s, w, f)]) for w in range(N) if w != u]))
    for (s, x), bit in req.items():
        fa, fb = (x, bit), (x, 1 - bit)
        def inopt(fo, f):   # f on the chain of option fo of x at s
            if f == fo: return z3.BoolVal(True)
            if f[0] == x: return z3.BoolVal(False)
            return z3.Or([z3.And(b[(fo, w)], IN[(s, w, f)]) for w in range(N) if w != x])
        dA = {f: z3.And(inopt(fa, f), z3.Not(inopt(fb, f))) for f in faces}; dB = {f: z3.And(inopt(fb, f), z3.Not(inopt(fa, f))) for f in faces}
        good = {f: z3.Or(z3.And(dA[f], z3.Not(par[fi[f]])), z3.And(dB[f], par[fi[f]])) for f in faces}
        bad = {f: z3.Or(z3.And(dA[f], par[fi[f]]), z3.And(dB[f], z3.Not(par[fi[f]]))) for f in faces}
        Z.add(z3.Or([good[f] for f in faces]))
        for g in faces:
            Z.add(z3.Implies(bad[g], z3.Or([z3.And(good[f], lt[(fi[g], fi[f])]) for f in faces if f != g])))
    t0 = time.time(); r = Z.check(); dt = time.time() - t0
    if r != z3.sat: return str(r), dt, None
    m = Z.model(); tv = lambda e: z3.is_true(m.eval(e, model_completion=True))
    xt = {f: next(u for u in T if u != f[0] and tv(b[(f, u)])) for f in faces}
    rank = {f: sum(1 for g in faces if g != f and tv(lt[(fi[g], fi[f])])) for f in faces}
    return "sat", dt, dict(xt=xt, rank=rank, par={f: tv(par[fi[f]]) for f in faces})
if __name__ == "__main__":
    import ideal, xisearch as XS
    T = json.load(open(sys.argv[1])); out = sys.argv[2]
    if "opts" in T:
        lev = T["lev"]; WT = [[o[0] for o in T["opts"][v]] for v in range(T["N"])]; gate = T["gate"]; S, why = ideal.traj(T)
    else:
        lev = [m[0] for m in T["movers"]]; WT = [m[1] for m in T["movers"]]; gate = T["gate"]; S = [tuple(s) for s in T["states"]]
    bad, req = RQ.requirements(lev, WT, gate, S)
    print("XISAT L", len(S) - 1, "N", len(lev), "W-violations", bad, "requirements", len(req), flush=True)
    if bad: sys.exit(1)
    allow = {int(k): v for k, v in json.loads(os.environ["XTALLOW"]).items()} if os.environ.get("XTALLOW") else None
    r, dt, sol = solve(lev, WT, S, req, tmo=int(os.environ["TMO"]) if os.environ.get("TMO") else None, allow=allow)
    print("XISAT", r, f"{dt:.1f} s", flush=True)
    if sol:
        N = len(lev); pos = XS.topo(N, sol["xt"]); G = RQ.genome(lev, WT, gate, S[0], dict(xt=sol["xt"], pos=pos, rank=sol["rank"], par=sol["par"]))
        json.dump(G, open(out, "w")); S2, why = ideal.traj(G)
        print("replay L", len(S2) - 1, why, "prefix matches target:", list(S2[:len(S)]) == list(S), out)
