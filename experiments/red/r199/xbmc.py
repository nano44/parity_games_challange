#!/usr/bin/env python3
"""L-RED R199 XBMC: exact boolean synthesis of an IDEAL-ACYC genome (degree 2) in which the MAIN movers follow a prescribed run and
AUXILIARY movers (W-leaves: nobody W-points at them; level >= 1, W-targets = the two main movers of the level below, either
orientation) are free. Exact RESULTS R104 semantics: chains of current options, top face of the symmetric difference decides
(strict total order lt on faces, parities). Main movers: the C-element requirements of r199/req.py. Aux movers: their states are
variables obeying the C-element rule s_t = (KP_t == C_(t-1)) ? KP_t : s_(t-1) (r199/req.py, PROVED there), KP_t known (it depends on
main states only). UNSAT = no genome with these movers realises the main run (exact). Usage: xbmc.py target.json naux_spec out.json
naux_spec: comma list of aux levels with orientation, e.g. "4+,4-,3+" (+: option 0 -> u_(l-1), -: option 0 -> v_(l-1)).
env TMO (s), STARTAUX free by default."""
import sys, os, json, time
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import z3, req as RQ
def main():
    T = json.load(open(sys.argv[1])); aux = [a for a in sys.argv[2].split(",") if a]; out = sys.argv[3]
    lev0 = [m[0] for m in T["movers"]]; WT0 = [m[1] for m in T["movers"]]; gate0 = T["gate"]; S0 = [tuple(s) for s in T["states"]]
    N0 = len(lev0); L = len(S0) - 1
    lev = list(lev0); WT = [list(w) for w in WT0]; m0 = max(lev0) + 1; E = 0
    for a in aux:
        if a[0] == "E": E = int(a[1:])
    for j in range(E):   # extra full ladder levels m0 .. m0+E-1 (movers 2l, 2l+1 must follow the main ones)
        l = m0 + j; lev += [l, l]; WT += [[2 * (l - 1), 2 * (l - 1) + 1]] * 2
    assert N0 == 2 * m0, "main movers must be exactly the ladder pairs of levels 0..m0-1"
    for a in aux:
        if a[0] == "E": continue
        l = int(a[:-1]); o = a[-1]; lev.append(l); WT.append([2 * (l - 1), 2 * (l - 1) + 1] if o == "+" else [2 * (l - 1) + 1, 2 * (l - 1)])
    N = len(lev); gate = [list(g) for g in gate0] + [[1000 + 2 * i, 1001 + 2 * i] for i in range(N - N0)]
    dtop = m0 + E
    bad, req = RQ.requirements(lev0, WT0, gate0, S0)
    if bad: print("W-side violations", bad); sys.exit(1)
    faces = [(v, k) for v in range(N) for k in (0, 1)]; M = len(faces); fi = {f: i for i, f in enumerate(faces)}
    Z = z3.Solver()
    if os.environ.get("TMO"): Z.set("timeout", int(os.environ["TMO"]) * 1000)
    Tg = range(-1, N)
    b = {(f, u): z3.Bool(f"b{fi[f]}_{u}") for f in faces for u in Tg if u != f[0]}
    before = {(v, w): z3.Bool(f"o{v}_{w}") for v in range(N) for w in range(N) if v != w}
    for v in range(N):
        for w in range(N):
            if v < w: Z.add(before[(v, w)] != before[(w, v)])
            for x in range(N):
                if len({v, w, x}) == 3: Z.add(z3.Implies(z3.And(before[(v, w)], before[(w, x)]), before[(v, x)]))
    for f in faces:
        Z.add(z3.PbEq([(b[(f, u)], 1) for u in Tg if u != f[0]], 1))
        for u in range(N):
            if u != f[0]: Z.add(z3.Implies(b[(f, u)], before[(f[0], u)]))
    lt = {(i, j): z3.Bool(f"l{i}_{j}") for i in range(M) for j in range(M) if i != j}
    for i in range(M):
        for j in range(i + 1, M): Z.add(lt[(i, j)] != lt[(j, i)])
        for j in range(M):
            for k in range(M):
                if len({i, j, k}) == 3: Z.add(z3.Implies(z3.And(lt[(i, j)], lt[(j, k)]), lt[(i, k)]))
    par = [z3.Bool(f"odd{i}") for i in range(M)]
    st = {}
    for t in range(L + 1):
        for v in range(N): st[(t, v)] = z3.BoolVal(bool(S0[t][v])) if v < N0 else z3.Bool(f"s{t}_{v}")
    # key rankings: main levels known; extra levels symbolic (Lemma K3 of R198: same option -> gate bit, else R of the level below)
    Gb = {(l, k): z3.Bool(f"G{l}_{k}") for l in range(m0, dtop) for k in (0, 1)}
    Rk = {}
    for t in range(L + 1):
        key = RQ.keys(lev0, WT0, gate0, S0[t])
        for l in range(m0): Rk[(t, l)] = z3.BoolVal(key[2 * l] < key[2 * l + 1])
        for l in range(m0, dtop):
            a, c = st[(t, 2 * l)], st[(t, 2 * l + 1)]
            Rk[(t, l)] = z3.If(a == c, z3.If(a, Gb[(l, 1)], Gb[(l, 0)]), z3.If(z3.Not(a), Rk[(t, l - 1)], z3.Not(Rk[(t, l - 1)])))
    def KPb(t, a):   # z3 bool: KP of mover a at state t is option 1
        x, y = WT[a]; l = lev[a] - 1
        rx = Rk[(t, l)] if x == 2 * l else z3.Not(Rk[(t, l)])   # True iff W-target x has the smaller key
        return z3.Not(rx)
    IN = {}
    for t in range(L + 1):
        for u in range(N):
            for f in faces: IN[(t, u, f)] = z3.Bool(f"in{t}_{u}_{fi[f]}")
        for u in range(N):
            for f in faces:
                terms = []
                for k in (0, 1):
                    on = st[(t, u)] if k == 1 else z3.Not(st[(t, u)])
                    if f == (u, k): terms.append(on)
                    elif f[0] != u: terms.append(z3.And(on, z3.Or([z3.And(b[((u, k), w)], IN[(t, w, f)]) for w in range(N) if w != u])))
                Z.add(IN[(t, u, f)] == z3.Or(terms) if terms else z3.Not(IN[(t, u, f)]))
    def better1(t, x):
        """z3 bool: option 1 of x strictly better at state t (exact semantics)"""
        def inopt(k, f):
            if f == (x, k): return z3.BoolVal(True)
            if f[0] == x: return z3.BoolVal(False)
            return z3.Or([z3.And(b[((x, k), w)], IN[(t, w, f)]) for w in range(N) if w != x])
        i1 = {f: inopt(1, f) for f in faces}; i0 = {f: inopt(0, f) for f in faces}
        f1 = {f: z3.Or(z3.And(i1[f], z3.Not(i0[f]), z3.Not(par[fi[f]])), z3.And(i0[f], z3.Not(i1[f]), par[fi[f]])) for f in faces}
        f0 = {f: z3.Or(z3.And(i0[f], z3.Not(i1[f]), z3.Not(par[fi[f]])), z3.And(i1[f], z3.Not(i0[f]), par[fi[f]])) for f in faces}
        c = z3.Bool(f"c{t}_{x}")
        Z.add(z3.Implies(c, z3.And(z3.Or(list(f1.values())), *[z3.Implies(f0[g], z3.Or([z3.And(f1[f], lt[(fi[g], fi[f])]) for f in faces if f != g])) for g in faces])))
        Z.add(z3.Implies(z3.Not(c), z3.And(z3.Or(list(f0.values())), *[z3.Implies(f1[g], z3.Or([z3.And(f0[f], lt[(fi[g], fi[f])]) for f in faces if f != g])) for g in faces])))
        return c
    if os.environ.get("LEM", "1") == "1":
        # redundant lane-lemma clauses (sound on every IDEAL-ACYC run, degree 2): reach = Xi-reachability;
        # R189 RE-REVERSAL: between consecutive moves of x at a < b some Xi-descendant moves at a step in [a, b-1];
        # R189 Corollary LAG: a move of x at t with no move at t-1 and the same KP at t-1 and t has a descendant moving at t-1
        reach = {(x, y): z3.Bool(f"re{x}_{y}") for x in range(N) for y in range(N)}
        for x in range(N):
            Z.add(z3.Not(reach[(x, x)]))
            for y in range(N):
                if x != y: Z.add(reach[(x, y)] == z3.Or([z3.And(b[((x, k), w)], z3.Or(z3.BoolVal(w == y), reach[(w, y)])) for k in (0, 1) for w in range(N) if w != x]))
        mv = {(t, v): (st[(t, v)] != st[(t - 1, v)]) for t in range(1, L + 1) for v in range(N)}
        def kpb(t, v):
            if v < N0:
                key = RQ.keys(lev0, WT0, gate0, S0[t]); return z3.BoolVal(RQ.kp(lev0, WT0, gate0, key, v) == 1)
            return KPb(t, v)
        for x in range(N):
            for a in range(1, L + 1):
                for c in range(a + 1, L + 1):
                    gap = z3.And(mv[(a, x)], mv[(c, x)], *[z3.Not(mv[(e, x)]) for e in range(a + 1, c)])
                    gap = z3.simplify(gap)
                    if z3.is_false(gap): continue
                    Z.add(z3.Implies(gap, z3.Or([z3.And(reach[(x, y)], z3.Or([mv[(e, y)] for e in range(a, c)])) for y in range(N) if y != x])))
            for t in range(2, L + 1):
                cond = z3.simplify(z3.And(mv[(t, x)], z3.Not(mv[(t - 1, x)]), kpb(t, x) == kpb(t - 1, x)))
                if z3.is_false(cond): continue
                Z.add(z3.Implies(cond, z3.Or([z3.And(reach[(x, y)], mv[(t - 1, y)]) for y in range(N) if y != x])))
    for (s, x), bit in req.items():
        c = better1(s, x); Z.add(c if bit == 1 else z3.Not(c))
    for a in range(N0, N):
        for t in range(1, L + 1):
            c = better1(t - 1, a); kp = KPb(t, a)
            Z.add(st[(t, a)] == z3.If(c == kp, kp, st[(t - 1, a)]))
    for item in [x for x in os.environ.get("FX", "").split(",") if x]:
        l, k = map(int, item.split(":")); Z.add(z3.PbGe([(Rk[(t, l)] != Rk[(t - 1, l)], 1) for t in range(1, L + 1)], k))
    if os.environ.get("AUXMOVE") == "1":   # every aux mover must move at least once (avoid idle aux)
        for a in range(N0, N): Z.add(z3.Or([st[(t, a)] != st[(t - 1, a)] for t in range(1, L + 1)]))
    print("XBMC main N", N0, "aux", aux, "L", L, "requirements", len(req), "faces", M, flush=True)
    t0 = time.time(); r = Z.check(); print("XBMC ->", r, f"{time.time() - t0:.1f} s", flush=True)
    if r == z3.sat:
        m = Z.model(); tv = lambda e: z3.is_true(m.eval(e, model_completion=True))
        xt = {f: next(u for u in Tg if u != f[0] and tv(b[(f, u)])) for f in faces}
        rank = {f: sum(1 for g in faces if g != f and tv(lt[(fi[g], fi[f])])) for f in faces}
        import xisearch as XS, ideal
        start = [S0[0][v] if v < N0 else (1 if tv(st[(0, v)]) else 0) for v in range(N)]
        for l in range(m0, dtop):
            for k in (0, 1):
                lo, hi = 2000 + 4 * l + 2 * k, 2001 + 4 * l + 2 * k
                gate[2 * l][k], gate[2 * l + 1][k] = (lo, hi) if tv(Gb[(l, k)]) else (hi, lo)
        G = RQ.genome(lev, WT, gate, start, dict(xt=xt, pos=XS.topo(N, xt), rank=rank, par={f: tv(par[fi[f]]) for f in faces}))
        json.dump(G, open(out, "w")); S2, why = ideal.traj(G)
        okk = all(tuple(S2[t][:N0]) == S0[t] for t in range(min(len(S2), L + 1))) and len(S2) > L
        print("replay L", len(S2) - 1, why, "main prefix matches target:", okk, out)
        print("aux moves", {a: [t for t in range(1, L + 1) if S2[t][a] != S2[t - 1][a]] for a in range(N0, N)} if len(S2) > L else None)
main()
