#!/usr/bin/env python3
"""L-RED R200 XCNF: the r199/xbmc.py model (exact RESULTS R104 IDEAL-ACYC semantics, degree 2; MAIN movers follow a prescribed run,
E extra full ladder levels free) compiled to plain CNF by hand (Tseitin, constant folding) and solved with a CDCL solver from pysat
(default CaDiCaL 1.9.5; env SOLVER=kissat404 etc.). Same constraints as xbmc.py, clause for clause:
  Xi-targets one-hot over {X} + movers, an acyclic order 'before' (tournament + transitivity), b[f,u] -> before[f0,u];
  strict total order lt on faces (one var per pair + transitivity), parities;
  IN[t,u,f] = face f on the chain of u's current option at state t (recursive definition, unique by acyclicity);
  c[t,x] = option 1 of x strictly Xi-better at t: c -> (some face favours 1, and every face favouring 0 lies below a face favouring 1),
  not c -> the mirror (exact: the symmetric difference is never empty at degree 2);
  main requirements (r199/req.py C-ELEMENT form) c[s,x] = bit; extra movers: s_t = (c_(t-1) == KP_t) ? KP_t : s_(t-1) with KP_t from
  the R198 K3 key-rank recursion (gate bits G[l,k] free);
  LEM (env LEM=1 default): reach = Xi-reachability, R189 RE-REVERSAL, R189 Corollary LAG (redundant, sound on IDEAL-ACYC runs).
SAT models are replayed under r187/ideal.py (the reference simulator); a SAT claim needs that replay to match.
Usage: xcnf.py target.json E out.json     (env SOLVER, SEED, FIXALL=1: all movers are main (pure Xi problem, E must be 0),
      DIMACS=path: also write the CNF; LEM=0/1)"""
import sys, os, json, time
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r199"), os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import req as RQ

class CNF:
    def __init__(s): s.n = 0; s.cl = []; s.empty = False
    def new(s): s.n += 1; return s.n
    def add(s, c):
        if any(l is True for l in c): return
        c = [l for l in c if l is not False]
        if not c: s.empty = True
        s.cl.append(c)
    def AND(s, ls):
        if any(l is False for l in ls): return False
        ls = [l for l in ls if l is not True]
        if not ls: return True
        if len(ls) == 1: return ls[0]
        v = s.new()
        for l in ls: s.cl.append([-v, l])
        s.cl.append([v] + [-l for l in ls]); return v
    def OR(s, ls):
        r = s.AND([neg(l) for l in ls]); return neg(r)
    def EQ(s, a, b):   # a <-> b, returns literal
        if a is True: return b
        if a is False: return neg(b)
        if b is True: return a
        if b is False: return neg(a)
        v = s.new(); s.cl += [[-v, -a, b], [-v, a, -b], [v, a, b], [v, -a, -b]]; return v
    def ITE(s, c, a, b):
        if c is True: return a
        if c is False: return b
        if a is b: return a
        return s.OR([s.AND([c, a]), s.AND([neg(c), b])])
    def imp(s, a, b): s.add([neg(a), b])
def neg(l): return (not l) if isinstance(l, bool) else -l

def build(T, E, fixall=False, lem=True):
    lev0 = [m[0] for m in T["movers"]]; WT0 = [m[1] for m in T["movers"]]; gate0 = T["gate"]; S0 = [tuple(s) for s in T["states"]]
    N0 = len(lev0); L = len(S0) - 1
    lev = list(lev0); WT = [list(w) for w in WT0]; m0 = max(lev0) + 1
    for j in range(E):
        l = m0 + j; lev += [l, l]; WT += [[2 * (l - 1), 2 * (l - 1) + 1]] * 2
    if E: assert N0 == 2 * m0 and not fixall
    N = len(lev); dtop = m0 + E
    bad, req = RQ.requirements(lev0, WT0, gate0, S0)
    if bad: raise SystemExit(f"W-side violations {bad}")
    faces = [(v, k) for v in range(N) for k in (0, 1)]; M = len(faces); fi = {f: i for i, f in enumerate(faces)}
    C = CNF(); Tg = range(-1, N)
    b = {(f, u): C.new() for f in faces for u in Tg if u != f[0]}
    bv = {}
    for v in range(N):
        for w in range(v + 1, N): bv[(v, w)] = C.new()
    before = lambda v, w: bv[(v, w)] if v < w else -bv[(w, v)]
    for v in range(N):
        for w in range(N):
            for x in range(N):
                if len({v, w, x}) == 3: C.add([-before(v, w), -before(w, x), before(v, x)])
    for f in faces:
        ops = [b[(f, u)] for u in Tg if u != f[0]]; C.add(ops)
        for i in range(len(ops)):
            for j in range(i + 1, len(ops)): C.add([-ops[i], -ops[j]])
        for u in range(N):
            if u != f[0]: C.imp(b[(f, u)], before(f[0], u))
    lv = {}
    for i in range(M):
        for j in range(i + 1, M): lv[(i, j)] = C.new()
    lt = lambda i, j: lv[(i, j)] if i < j else -lv[(j, i)]
    for i in range(M):
        for j in range(M):
            if j == i: continue
            for k in range(M):
                if k != i and k != j: C.add([-lt(i, j), -lt(j, k), lt(i, k)])
    par = [C.new() for _ in range(M)]
    st = {}
    for t in range(L + 1):
        for v in range(N): st[(t, v)] = bool(S0[t][v]) if v < N0 else C.new()
    Gb = {(l, k): C.new() for l in range(m0, dtop) for k in (0, 1)}
    Rk = {}
    for t in range(L + 1):
        key = RQ.keys(lev0, WT0, gate0, S0[t])
        for l in range(m0): Rk[(t, l)] = key[2 * l] < key[2 * l + 1]
        for l in range(m0, dtop):
            a, c = st[(t, 2 * l)], st[(t, 2 * l + 1)]
            Rk[(t, l)] = C.ITE(C.EQ(a, c), C.ITE(a, Gb[(l, 1)], Gb[(l, 0)]), C.ITE(neg(a), Rk[(t, l - 1)], neg(Rk[(t, l - 1)])))
    def KPb(t, a):
        if a < N0:
            key = RQ.keys(lev0, WT0, gate0, S0[t]); return RQ.kp(lev0, WT0, gate0, key, a) == 1
        x, y = WT[a]; l = lev[a] - 1
        rx = Rk[(t, l)] if x == 2 * l else neg(Rk[(t, l)])
        return neg(rx)
    need_t = set(s for (s, x) in req) | (set(range(L)) if N > N0 else set())
    IN = {}
    # topological evaluation is not available (order is symbolic): define IN by equations
    for t in sorted(need_t):
        for u in range(N):
            for f in faces: IN[(t, u, f)] = C.new()
    for t in sorted(need_t):
        for u in range(N):
            for f in faces:
                terms = []
                for k in (0, 1):
                    on = st[(t, u)] if k == 1 else neg(st[(t, u)])
                    if f == (u, k): terms.append(on)
                    elif f[0] != u: terms.append(C.AND([on, C.OR([C.AND([b[((u, k), w)], IN[(t, w, f)]]) for w in range(N) if w != u])]))
                e = C.OR(terms) if terms else False
                v = IN[(t, u, f)]
                if e is False: C.add([-v])
                elif e is True: C.add([v])
                else: C.add([-v, e]); C.add([v, -e])
    cvar = {}
    def better1(t, x):
        if (t, x) in cvar: return cvar[(t, x)]
        def inopt(k, f):
            if f == (x, k): return True
            if f[0] == x: return False
            return C.OR([C.AND([b[((x, k), w)], IN[(t, w, f)]]) for w in range(N) if w != x])
        i1 = {f: inopt(1, f) for f in faces}; i0 = {f: inopt(0, f) for f in faces}
        f1 = {f: C.OR([C.AND([i1[f], neg(i0[f]), -par[fi[f]]]), C.AND([i0[f], neg(i1[f]), par[fi[f]]])]) for f in faces}
        f0 = {f: C.OR([C.AND([i0[f], neg(i1[f]), -par[fi[f]]]), C.AND([i1[f], neg(i0[f]), par[fi[f]]])]) for f in faces}
        c = C.new()
        for (pos, fa, fb) in ((c, f1, f0), (-c, f0, f1)):
            C.add([-pos] + [fa[f] for f in faces])
            for g in faces:
                if fb[g] is False: continue
                C.add([-pos, neg(fb[g])] + [C.AND([fa[f], lt(fi[g], fi[f])]) for f in faces if f != g])
        cvar[(t, x)] = c; return c
    mv = {(t, v): neg(C.EQ(st[(t, v)], st[(t - 1, v)])) for t in range(1, L + 1) for v in range(N)}
    if lem:
        reach = {}
        for x in range(N):
            for y in range(N):
                if x != y: reach[(x, y)] = C.new()
        for x in range(N):
            for y in range(N):
                if x == y: continue
                e = C.OR([C.AND([b[((x, k), w)], True if w == y else reach[(w, y)]]) for k in (0, 1) for w in range(N) if w != x])
                C.add([-reach[(x, y)], e]); C.add([reach[(x, y)], neg(e)])
        for x in range(N):
            for a in range(1, L + 1):
                for c2 in range(a + 1, L + 1):
                    gap = [mv[(a, x)], mv[(c2, x)]] + [neg(mv[(e, x)]) for e in range(a + 1, c2)]
                    if any(g is False for g in gap): continue
                    C.add([neg(g) for g in gap if g is not True] + [C.AND([reach[(x, y)], C.OR([mv[(e, y)] for e in range(a, c2)])]) for y in range(N) if y != x])
            for t in range(2, L + 1):
                cond = [mv[(t, x)], neg(mv[(t - 1, x)]), C.EQ(KPb(t, x), KPb(t - 1, x))]
                if any(g is False for g in cond): continue
                C.add([neg(g) for g in cond if g is not True] + [C.AND([reach[(x, y)], mv[(t - 1, y)]]) for y in range(N) if y != x])
    for (s, x), bit in req.items():
        c = better1(s, x); C.add([c if bit == 1 else -c])
    for a in range(N0, N):
        for t in range(1, L + 1):
            c = better1(t - 1, a); kp = KPb(t, a)
            C.add([C.EQ(st[(t, a)], C.ITE(C.EQ(c, kp), kp, st[(t - 1, a)]))])
    info = dict(N=N, N0=N0, L=L, lev=lev, WT=WT, gate0=gate0, S0=S0, m0=m0, dtop=dtop, faces=faces, b=b, lt=lt, par=par, st=st, Gb=Gb, req=req, fi=fi)
    return C, info

def decode(model, I):
    ms = set(l for l in model if l > 0); tv = lambda l: l if isinstance(l, bool) else ((l in ms) if l > 0 else (-l not in ms))
    N, N0, L, faces, fi = I["N"], I["N0"], I["L"], I["faces"], I["fi"]
    xt = {f: next(u for u in range(-1, N) if u != f[0] and tv(I["b"][(f, u)])) for f in faces}
    rank = {f: sum(1 for g in faces if g != f and tv(I["lt"](fi[g], fi[f]))) for f in faces}
    gate = [list(g) for g in I["gate0"]] + [[0, 0] for _ in range(N - N0)]
    for l in range(I["m0"], I["dtop"]):
        for k in (0, 1):
            lo, hi = 2000 + 4 * l + 2 * k, 2001 + 4 * l + 2 * k
            gate[2 * l][k], gate[2 * l + 1][k] = (lo, hi) if tv(I["Gb"][(l, k)]) else (hi, lo)
    start = [I["S0"][0][v] if v < N0 else (1 if tv(I["st"][(0, v)]) else 0) for v in range(N)]
    import xisearch as XS
    G = RQ.genome(I["lev"], I["WT"], gate, start, dict(xt=xt, pos=XS.topo(N, xt), rank=rank, par={f: tv(I["par"][fi[f]]) for f in faces}))
    return G

def solve(C, name=None, seed=None):
    from pysat.solvers import Solver
    name = name or os.environ.get("SOLVER", "cadical195")
    if C.empty: return False, None
    with Solver(name=name, bootstrap_with=C.cl) as S:
        r = S.solve(); return r, (S.get_model() if r else None)

if __name__ == "__main__":
    import ideal
    T = json.load(open(sys.argv[1])); E = int(sys.argv[2]); out = sys.argv[3]
    t0 = time.time(); C, I = build(T, E, lem=os.environ.get("LEM", "1") == "1")
    print(f"XCNF target {sys.argv[1]} E {E} N {I['N']} L {I['L']} requirements {len(I['req'])} vars {C.n} clauses {len(C.cl)} build {time.time() - t0:.1f} s", flush=True)
    if os.environ.get("DIMACS"):
        with open(os.environ["DIMACS"], "w") as fh:
            fh.write(f"p cnf {C.n} {len(C.cl)}\n"); fh.writelines(" ".join(map(str, c)) + " 0\n" for c in C.cl)
    if os.environ.get("CUBEVARS"):   # cube-and-conquer: assumptions over extra-level gate bits (G) and/or extra-mover start bits (S0)
        from pysat.solvers import Solver
        cv = []
        for kind in os.environ["CUBEVARS"].split(","):
            if kind == "G": cv += [I["Gb"][k] for k in sorted(I["Gb"])]
            if kind == "S0": cv += [I["st"][(0, v)] for v in range(I["N0"], I["N"])]
        part, P = map(int, os.environ.get("CUBEPART", "0/1").split("/")); r = False; model = None
        with Solver(name=os.environ.get("SOLVER", "cadical195"), bootstrap_with=C.cl) as SS:
            for ci in range(2 ** len(cv)):
                if ci % P != part: continue
                asm = [v if (ci >> j) & 1 else -v for j, v in enumerate(cv)]; t1 = time.time(); rr = SS.solve(assumptions=asm)
                print(f"CUBE {ci} {'SAT' if rr else 'UNSAT'} {time.time() - t1:.1f} s", flush=True)
                if rr: r = True; model = SS.get_model(); break
        print(f"XCNF CUBES part {part}/{P} -> {'SAT' if r else 'UNSAT (all cubes of this part)'}", flush=True)
        t1 = time.time()
    else:
        t1 = time.time(); r, model = solve(C)
    print(f"XCNF -> {'SAT' if r else 'UNSAT'} {time.time() - t1:.1f} s solver {os.environ.get('SOLVER', 'cadical195')}", flush=True)
    if r:
        G = decode(model, I); json.dump(G, open(out, "w")); S2, why = ideal.traj(G); L, N0, S0 = I["L"], I["N0"], I["S0"]
        ok = len(S2) > L and all(tuple(S2[t][:N0]) == S0[t] for t in range(L + 1))
        print("replay L", len(S2) - 1, why, "main prefix matches target:", ok, out, flush=True)
        if len(S2) > L: print("extra moves", {a: [t for t in range(1, L + 1) if S2[t][a] != S2[t - 1][a]] for a in range(N0, I["N"])})
