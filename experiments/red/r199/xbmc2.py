#!/usr/bin/env python3
"""L-RED R199 XBMC2: exact boolean bounded model check of IDEAL-ACYC runs (degree 2) on a width-2 ladder of depth d plus optional
W-leaf helpers, in the EXACT RESULTS R104 semantics (no integer weights): Xi-targets one-hot with an acyclic order, a strict total
order on faces, parities; every mover obeys the C-ELEMENT rule (r199/req.py) s_t = (KP_t == C_(t-1)) ? KP_t : s_(t-1), with KP from
symbolic key rankings (R198 Lemma K3: level l >= 1: same option -> gate bit, else R_(l-1) or its negation; level 0: 4 gate-order bits,
KP of level 0 = option 0 by the symmetry gate(v,0) < gate(v,1)). Each of the L steps has a move. Redundant lane-lemma clauses
(LEM=1): RE-REVERSAL and LAG over Xi-reach (R189), as in r199/xbmc.py.
Constraints: FX="l:k,..." R_l flips at >= k of the steps 1..L (TOTAL); FIX=json {"t,v": bit} fixed states; SCHED=json {v: [steps]}
exact move steps of v; WIN=json {v: [[lo, hi], ...]} v moves exactly once in each window. Usage: xbmc2.py d L out.json [helpers]
(helpers "l+,l-": W-leaf movers at level l with option 0 -> u_(l-1) (+) or v_(l-1) (-))."""
import sys, os, json, time
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import z3
def main():
    d, L, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]; hel = [a for a in (sys.argv[4] if len(sys.argv) > 4 else "").split(",") if a]
    lev = [v // 2 for v in range(2 * d)]; WT = [[-1, -1] if v < 2 else [2 * (v // 2 - 1), 2 * (v // 2 - 1) + 1] for v in range(2 * d)]
    for a in hel:
        l = int(a[:-1]); lev.append(l); WT.append([2 * (l - 1), 2 * (l - 1) + 1] if a[-1] == "+" else [2 * (l - 1) + 1, 2 * (l - 1)])
    N = len(lev); faces = [(v, k) for v in range(N) for k in (0, 1)]; M = len(faces); fi = {f: i for i, f in enumerate(faces)}
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
    st = {(t, v): z3.Bool(f"s{t}_{v}") for t in range(L + 1) for v in range(N)}
    # gate bits: level 0: B[a][c] = g(u0, a) < g(v0, c), with g(x,0) < g(x,1) (monotone); level l >= 1: G[l][k] = g(u_l,k) < g(v_l,k)
    B0 = {(a, c): z3.Bool(f"B{a}{c}") for a in (0, 1) for c in (0, 1)}
    Z.add(z3.Implies(B0[(0, 0)], B0[(0, 1)]), z3.Implies(B0[(1, 0)], B0[(1, 1)]), z3.Implies(B0[(1, 0)], B0[(0, 0)]), z3.Implies(B0[(1, 1)], B0[(0, 1)]))
    Gb = {(l, k): z3.Bool(f"G{l}_{k}") for l in range(1, d) for k in (0, 1)}
    Rk = {}
    for t in range(L + 1):
        a, c = st[(t, 0)], st[(t, 1)]
        Rk[(t, 0)] = z3.If(a, z3.If(c, B0[(1, 1)], B0[(1, 0)]), z3.If(c, B0[(0, 1)], B0[(0, 0)]))
        for l in range(1, d):
            a, c = st[(t, 2 * l)], st[(t, 2 * l + 1)]
            Rk[(t, l)] = z3.If(a == c, z3.If(a, Gb[(l, 1)], Gb[(l, 0)]), z3.If(z3.Not(a), Rk[(t, l - 1)], z3.Not(Rk[(t, l - 1)])))
    def KPb(t, v):   # True iff KP of v at state t is option 1
        if lev[v] == 0: return z3.BoolVal(False)
        x, y = WT[v]; l = lev[v] - 1
        return z3.Not(Rk[(t, l)] if x == 2 * l else z3.Not(Rk[(t, l)]))
    IN = {}
    for t in range(L):
        for u in range(N):
            for f in faces: IN[(t, u, f)] = z3.Bool(f"in{t}_{u}_{fi[f]}")
        for u in range(N):
            for f in faces:
                terms = []
                for k in (0, 1):
                    on = st[(t, u)] if k == 1 else z3.Not(st[(t, u)])
                    if f == (u, k): terms.append(on)
                    elif f[0] != u: terms.append(z3.And(on, z3.Or([z3.And(b[((u, k), w)], IN[(t, w, f)]) for w in range(N) if w != u])))
                Z.add(IN[(t, u, f)] == z3.Or(terms))
    def better1(t, x):
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
    for t in range(1, L + 1):
        for v in range(N):
            c = better1(t - 1, v); kp = KPb(t, v); Z.add(st[(t, v)] == z3.If(c == kp, kp, st[(t - 1, v)]))
        Z.add(z3.Or([st[(t, v)] != st[(t - 1, v)] for v in range(N)]))
    mv = {(t, v): (st[(t, v)] != st[(t - 1, v)]) for t in range(1, L + 1) for v in range(N)}
    if os.environ.get("LEM", "1") == "1":
        reach = {(x, y): z3.Bool(f"re{x}_{y}") for x in range(N) for y in range(N)}
        for x in range(N):
            Z.add(z3.Not(reach[(x, x)]))
            for y in range(N):
                if x != y: Z.add(reach[(x, y)] == z3.Or([z3.And(b[((x, k), w)], z3.Or(z3.BoolVal(w == y), reach[(w, y)])) for k in (0, 1) for w in range(N) if w != x]))
        for x in range(N):
            for a in range(1, L + 1):
                for c in range(a + 1, L + 1):
                    gap = z3.And(mv[(a, x)], mv[(c, x)], *[z3.Not(mv[(e, x)]) for e in range(a + 1, c)])
                    Z.add(z3.Implies(gap, z3.Or([z3.And(reach[(x, y)], z3.Or([mv[(e, y)] for e in range(a, c)])) for y in range(N) if y != x])))
            for t in range(2, L + 1):
                if lev[x] == 0: continue
                Z.add(z3.Implies(z3.And(mv[(t, x)], z3.Not(mv[(t - 1, x)]), KPb(t, x) == KPb(t - 1, x)), z3.Or([z3.And(reach[(x, y)], mv[(t - 1, y)]) for y in range(N) if y != x])))
    for item in [x for x in os.environ.get("FX", "").split(",") if x]:
        l, k = map(int, item.split(":")); Z.add(z3.PbGe([(Rk[(t, l)] != Rk[(t - 1, l)], 1) for t in range(1, L + 1)], k))
    for key, bit in (json.loads(os.environ["FIX"]).items() if os.environ.get("FIX") else []):
        t, v = map(int, key.split(",")); Z.add(st[(t, v)] == bool(bit))
    for v, steps in (json.loads(os.environ["SCHED"]).items() if os.environ.get("SCHED") else []):
        v = int(v)
        for t in range(1, L + 1): Z.add(mv[(t, v)] == (t in steps))
    for v, wins in (json.loads(os.environ["WIN"]).items() if os.environ.get("WIN") else []):
        v = int(v); inside = set()
        for lo, hi in wins:
            Z.add(z3.PbEq([(mv[(t, v)], 1) for t in range(lo, hi + 1)], 1)); inside |= set(range(lo, hi + 1))
        for t in range(1, L + 1):
            if t not in inside: Z.add(z3.Not(mv[(t, v)]))
    print("XBMC2 d", d, "L", L, "helpers", hel, "FX", os.environ.get("FX"), "N", N, flush=True)
    t0 = time.time(); r = Z.check(); print("XBMC2 ->", r, f"{time.time() - t0:.1f} s", flush=True)
    if r == z3.sat:
        m = Z.model(); tv = lambda e: z3.is_true(m.eval(e, model_completion=True))
        xt = {f: next(u for u in Tg if u != f[0] and tv(b[(f, u)])) for f in faces}
        rank = {f: sum(1 for g in faces if g != f and tv(lt[(fi[g], fi[f])])) for f in faces}
        gate = [[0, 0] for _ in range(N)]
        # level 0: realise the 4 order bits
        import itertools
        for p in itertools.permutations(range(4)):
            g = {(0, 0): p[0], (0, 1): p[1], (1, 0): p[2], (1, 1): p[3]}
            if g[(0, 0)] < g[(0, 1)] and g[(1, 0)] < g[(1, 1)] and all((g[(0, a)] < g[(1, c)]) == tv(B0[(a, c)]) for a in (0, 1) for c in (0, 1)):
                gate[0] = [g[(0, 0)], g[(0, 1)]]; gate[1] = [g[(1, 0)], g[(1, 1)]]; break
        nx = 4
        for l in range(1, d):
            for k in (0, 1):
                lo, hi = nx, nx + 1; nx += 2
                gate[2 * l][k], gate[2 * l + 1][k] = (lo, hi) if tv(Gb[(l, k)]) else (hi, lo)
        for v in range(2 * d, N): gate[v] = [nx, nx + 1]; nx += 2
        import req as RQ, xisearch as XS, ideal
        start = [1 if tv(st[(0, v)]) else 0 for v in range(N)]
        G = RQ.genome(lev, WT, gate, start, dict(xt=xt, pos=XS.topo(N, xt), rank=rank, par={f: tv(par[fi[f]]) for f in faces}))
        json.dump(G, open(out, "w")); S2, why = ideal.traj(G)
        okk = all(tuple(1 if tv(st[(t, v)]) else 0 for v in range(N)) == S2[t] for t in range(min(len(S2), L + 1))) and len(S2) > L
        print("replay L", len(S2) - 1, why, "matches model:", okk, out, flush=True)
main()
