#!/usr/bin/env python3
"""L-RED R199 XWAKE: WAKE-ORDER relaxation of a prescribed ladder run (main levels fixed, E extra ladder levels free on top, optional
W-leaf helpers). Variables: states of the extra movers, gate bits of the extra levels, and an arbitrary STRICT PARTIAL ORDER «x reaches y»
(transitive, irreflexive) standing for Xi-reachability. Constraints, each valid on every IDEAL-ACYC run at degree 2:
  (K) every move goes to KP_t (r199/req.py C-ELEMENT; R198 K1);
  (RR) R189 RE-REVERSAL: between consecutive moves of x at a < b some y reached by x moves at a step in [a, b-1];
  (LAG) R189 Corollary LAG: a move of x at t >= 2 with no move of x at t-1 and the same KP at t-1 and t has a reached y moving at t-1;
  every step has a move.
Xi-reachability of an acyclic genome is a strict partial order, so UNSAT here is an EXACT obstruction for the prescribed main run with
that many extra levels (no Xi-values are modelled; nothing else is relaxed away that could make a real run fail these clauses).
Usage: xwake.py target.json E out.json [helpers "l+,l-"]   (env TMO seconds)"""
import sys, os, json, time
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H]
import z3, req as RQ
T = json.load(open(sys.argv[1])); E = int(sys.argv[2]); out = sys.argv[3]; hel = [a for a in (sys.argv[4] if len(sys.argv) > 4 else "").split(",") if a]
lev0 = [m[0] for m in T["movers"]]; WT0 = [m[1] for m in T["movers"]]; gate0 = T["gate"]; S0 = [tuple(s) for s in T["states"]]
N0 = len(lev0); L = len(S0) - 1; m0 = max(lev0) + 1; assert N0 == 2 * m0
lev = list(lev0); WT = [list(w) for w in WT0]
for j in range(E): l = m0 + j; lev += [l, l]; WT += [[2 * (l - 1), 2 * (l - 1) + 1]] * 2
for a in hel: l = int(a[:-1]); lev.append(l); WT.append([2 * (l - 1), 2 * (l - 1) + 1] if a[-1] == "+" else [2 * (l - 1) + 1, 2 * (l - 1)])
N = len(lev); dtop = m0 + E
Z = z3.Solver()
if os.environ.get("TMO"): Z.set("timeout", int(os.environ["TMO"]) * 1000)
st = {(t, v): (z3.BoolVal(bool(S0[t][v])) if v < N0 else z3.Bool(f"s{t}_{v}")) for t in range(L + 1) for v in range(N)}
Gb = {(l, k): z3.Bool(f"G{l}_{k}") for l in range(m0, dtop) for k in (0, 1)}
Rk = {}
FREEKP = os.environ.get("FREEKP") == "1"
for t in range(L + 1):
    key = RQ.keys(lev0, WT0, gate0, S0[t])
    for l in range(m0): Rk[(t, l)] = z3.Bool(f"R{t}_{l}") if FREEKP else z3.BoolVal(key[2 * l] < key[2 * l + 1])
    for l in range(m0, dtop):
        a, c = st[(t, 2 * l)], st[(t, 2 * l + 1)]
        Rk[(t, l)] = z3.If(a == c, z3.If(a, Gb[(l, 1)], Gb[(l, 0)]), z3.If(z3.Not(a), Rk[(t, l - 1)], z3.Not(Rk[(t, l - 1)])))
if FREEKP:
    # gate-free relaxation: the key order R_l of the two main level-l movers is free, except that it cannot change at a step where
    # no mover of level <= l moves (keys of level l read only states of levels <= l: P-IDEAL-RED LOCAL (c))
    for t in range(1, L + 1):
        for l in range(m0):
            if not any(S0[t][v] != S0[t - 1][v] for v in range(N0) if lev0[v] <= l): Z.add(Rk[(t, l)] == Rk[(t - 1, l)])
def KP(t, v):
    if lev[v] == 0: return z3.Bool(f"K0_{v}") if (FREEKP and v < N0) else z3.BoolVal(False)
    x, y = WT[v]; l = lev[v] - 1
    if v < N0 and not FREEKP:
        key = RQ.keys(lev0, WT0, gate0, S0[t]); return z3.BoolVal(RQ.kp(lev0, WT0, gate0, key, v) == 1)
    if v < N0 and x == y: return z3.Bool(f"K{t}_{v}")  # both options on one W-target: gate order, constant (checked below)
    return z3.Not(Rk[(t, l)] if x == 2 * l else z3.Not(Rk[(t, l)]))
re = {(x, y): z3.Bool(f"re{x}_{y}") for x in range(N) for y in range(N)}
ed = {(x, y): z3.Bool(f"e{x}_{y}") for x in range(N) for y in range(N) if x != y}   # Xi-edges: out-degree <= 2 (degree 2)
XT = os.environ.get("XT") == "1"
if XT:
    # per-option Xi-targets (each option: at most one mover target, else X); reach = transitive closure of these edges
    eo = {(x, k, y): z3.Bool(f"eo{x}_{k}_{y}") for x in range(N) for k in (0, 1) for y in range(N) if x != y}
    for x in range(N):
        for k in (0, 1): Z.add(z3.PbLe([(eo[(x, k, y)], 1) for y in range(N) if y != x], 1))
        for y in range(N):
            if x != y: Z.add(z3.Implies(z3.Or(eo[(x, 0, y)], eo[(x, 1, y)]), re[(x, y)]))
    for x in range(N):
        for y in range(N):
            if x != y:
                Z.add(re[(x, y)] == z3.Or(eo[(x, 0, y)], eo[(x, 1, y)], *[z3.And(z3.Or(eo[(x, 0, w)], eo[(x, 1, w)]), re[(w, y)]) for w in range(N) if w not in (x, y)]))
for x in range(N):
    Z.add(z3.Not(re[(x, x)]))
    if os.environ.get("ANTI") == "1":
        for y in range(x + 1, N): Z.add(z3.Not(z3.And(re[(x, y)], re[(y, x)])))
    if XT: pass
    elif os.environ.get("DEG", "1") == "1":
        Z.add(z3.PbLe([(ed[(x, y)], 1) for y in range(N) if y != x], 2))
        for y in range(N):
            if x != y: Z.add(re[(x, y)] == z3.Or(ed[(x, y)], *[z3.And(ed[(x, w)], re[(w, y)]) for w in range(N) if w not in (x, y)]))
    else:
        for y in range(N):
            for w in range(N):
                if len({x, y, w}) == 3: Z.add(z3.Implies(z3.And(re[(x, y)], re[(y, w)]), re[(x, w)]))
mv = {(t, v): z3.simplify(st[(t, v)] != st[(t - 1, v)]) for t in range(1, L + 1) for v in range(N)}
for t in range(1, L + 1):
    Z.add(z3.Or([mv[(t, v)] for v in range(N)]))
    for v in (range(N) if FREEKP else range(N0, N)): Z.add(z3.Implies(mv[(t, v)], st[(t, v)] == KP(t, v)))
for x in range(N):
    for a in range(1, L + 1):
        for c in range(a + 1, L + 1):
            gap = z3.simplify(z3.And(mv[(a, x)], mv[(c, x)], *[z3.Not(mv[(e, x)]) for e in range(a + 1, c)]))
            if z3.is_false(gap): continue
            Z.add(z3.Implies(gap, z3.Or([z3.And(re[(x, y)], z3.Or([mv[(e, y)] for e in range(a, c)])) for y in range(N) if y != x])))
    if lev[x] == 0: continue
    for t in range(2, L + 1):
        cond = z3.simplify(z3.And(mv[(t, x)], z3.Not(mv[(t - 1, x)]), KP(t, x) == KP(t - 1, x)))
        if z3.is_false(cond): continue
        Z.add(z3.Implies(cond, z3.Or([z3.And(re[(x, y)], mv[(t - 1, y)]) for y in range(N) if y != x])))
if os.environ.get("CBIT", "1") == "1":
    # comparison bits: C_t(v) = strictly better option of v at state t; C-ELEMENT rule exactly (r199/req.py) for every mover;
    # C is a function of the states of the movers v reaches, so C_t != C_(t-1) needs a reached mover moving at step t
    C = {(t, v): z3.Bool(f"c{t}_{v}") for t in range(L) for v in range(N)}
    for v in range(N):
        for t in range(1, L + 1):
            kp = KP(t, v); Z.add(st[(t, v)] == z3.If(C[(t - 1, v)] == kp, kp, st[(t - 1, v)]))
        for t in range(1, L):
            Z.add(z3.Implies(C[(t, v)] != C[(t - 1, v)], z3.Or([z3.And(re[(v, y)], mv[(t, y)]) for y in range(N) if y != v])))
if os.environ.get("SDIFF") == "1":
    # STATE-DIFF (P-IDEAL-RED LOCAL (b) across ANY two states): C_s(v) != C_s'(v) needs a mover reached by v whose option differs
    # between s and s' (CBIT is the case s' = s + 1 with «moved» in place of «differs»)
    for v in range(N):
        for a in range(L):
            for b in range(a + 2, L):
                Z.add(z3.Implies(C[(a, v)] != C[(b, v)], z3.Or([z3.And(re[(v, y)], st[(a, y)] != st[(b, y)]) for y in range(N) if y != v])))
if XT and os.environ.get("PMDIFF") == "1":
    # PRE-MERGE DIFF (Lemma PREMERGE): C_s(x) is a function of the two pre-merge segments of x's face chains at s, and the pre-merge
    # movers are exactly the movers on ONE of the two chains. So C_s(x) != C_s'(x) needs a mover on exactly one face chain of x at s
    # whose option differs between s and s'. on[(s, x, k, y)]: y lies on the chain of option (x, k) under state s.
    on = {(t, x, k, y): z3.Bool(f"on{t}_{x}_{k}_{y}") for t in range(L) for x in range(N) for k in (0, 1) for y in range(N) if y != x}
    for t in range(L):
        for x in range(N):
            for k in (0, 1):
                for y in range(N):
                    if y == x: continue
                    via = [z3.And(eo[(x, k, z)], z3.If(st[(t, z)], on[(t, z, 1, y)], on[(t, z, 0, y)])) for z in range(N) if z not in (x, y)]
                    Z.add(on[(t, x, k, y)] == z3.Or(eo[(x, k, y)], *via))
    for x in range(N):
        for a in range(L):
            for b in range(a + 1, L):
                Z.add(z3.Implies(C[(a, x)] != C[(b, x)], z3.Or([z3.And(on[(a, x, 0, y)] != on[(a, x, 1, y)], st[(a, y)] != st[(b, y)]) for y in range(N) if y != x])))
if XT and os.environ.get("PMDIFF") == "1" and os.environ.get("STABPATH") == "1":
    # STABLE-PATH (box 152): at state a, let P / Q be the pre-merge parts of x's face chains b / 1-b (movers on exactly one chain),
    # merging at m. If C_a(x) = b, every Q-mover keeps its option at state c, and every P-mover keeps its option or is STABLE at c
    # (C_c(y) = s_c(y)), then face_c(x, b) >= sum(P) + cv_c(m) > sum(Q) + cv_c(m) = face_c(x, 1-b), so C_c(x) = b.
    for x in range(N):
        for a in range(L):
            for c in range(L):
                if c == a: continue
                for b in (0, 1):
                    onb = lambda y: z3.And(on[(a, x, b, y)], z3.Not(on[(a, x, 1 - b, y)]))
                    onq = lambda y: z3.And(on[(a, x, 1 - b, y)], z3.Not(on[(a, x, b, y)]))
                    cond = [C[(a, x)] == z3.BoolVal(b == 1)]
                    for y in range(N):
                        if y == x: continue
                        cond.append(z3.Implies(onq(y), st[(a, y)] == st[(c, y)]))
                        cond.append(z3.Implies(onb(y), z3.Or(st[(a, y)] == st[(c, y)], C[(c, y)] == st[(c, y)])))
                    Z.add(z3.Implies(z3.And(cond), C[(c, x)] == z3.BoolVal(b == 1)))
if XT and os.environ.get("VAL") == "1":
    # REL value model (a relaxation of +-2^rank): distinct nonzero integer weight per option; cv_t(y) = w(y, s_t(y)) + cv_t(xt(y, s_t(y)));
    # the comparison bit is the value comparison: C_t(v) = [face(v,1) > face(v,0)] at state t (requires CBIT=1)
    wv = {(x, k): z3.Int(f"w{x}_{k}") for x in range(N) for k in (0, 1)}
    Z.add(z3.Distinct(*wv.values()), *[wv[f] != 0 for f in wv])
    cv = {(t, y): z3.Int(f"cv{t}_{y}") for t in range(L + 1) for y in range(N)}
    def face(t, y, k): return wv[(y, k)] + z3.Sum([z3.If(eo[(y, k, z)], cv[(t, z)], 0) for z in range(N) if z != y])
    for t in range(L + 1):
        for y in range(N):
            Z.add(cv[(t, y)] == z3.If(st[(t, y)], face(t, y, 1), face(t, y, 0)))
            if t < L: Z.add(C[(t, y)] == (face(t, y, 1) > face(t, y, 0)))
# level-0 movers: KP constant (option 0), so a level-0 mover moves at most once (R197 §2 ceiling); main level 0 is fixed anyway
for B in (json.load(open(os.environ["BLOCKS"])) if os.environ.get("BLOCKS") and os.path.exists(os.environ["BLOCKS"]) else []):
    Z.add(z3.Not(z3.And([mv[(t, int(v))] == (t in set(ts)) for v, ts in B.items() for t in range(1, L + 1)])))
if XT and os.environ.get("NOGOODS") and os.path.exists(os.environ["NOGOODS"]):
    # CEGAR nogoods from box152/cegar.py: each is a list of literals that a value check (REL, fixed targets) refuted together
    for ng in json.load(open(os.environ["NOGOODS"])):
        lits = []
        for l in ng:
            if l[0] == "eo": x, k, y = l[1:4]; lits.append(eo[(x, k, y)] if y >= 0 else z3.Not(z3.Or([eo[(x, k, z)] for z in range(N) if z != x])))
            elif l[0] == "st": t, v, b = l[1:]; lits.append(st[(t, v)] == z3.BoolVal(bool(b)))
            elif l[0] == "C": t, v, b = l[1:]; lits.append(C[(t, v)] == z3.BoolVal(bool(b)))
        Z.add(z3.Not(z3.And(lits)))
t0 = time.time(); r = Z.check(); print("XWAKE", sys.argv[1], "E", E, "helpers", hel, "N", N, "L", L, "->", r, f"{time.time() - t0:.1f} s", flush=True)
if r == z3.sat:
    m = Z.model(); tv = lambda e: z3.is_true(m.eval(e, model_completion=True))
    sol = dict(moves={v: [t for t in range(1, L + 1) if tv(mv[(t, v)])] for v in range(N0, N)}, reach=[[x, y] for x in range(N) for y in range(N) if tv(re[(x, y)])],
               start={v: (1 if tv(st[(0, v)]) else 0) for v in range(N0, N)}, G={f"{l},{k}": tv(Gb[(l, k)]) for (l, k) in Gb},
               movers=[[lev[v], WT[v]] for v in range(N)])
    sol["states"] = [[int(tv(st[(t, v)])) for v in range(N)] for t in range(L + 1)]
    sol["KP"] = [[None] + [int(tv(KP(t, v))) for v in range(N)] for t in range(1, L + 1)]
    sol["KP"] = [[int(tv(KP(t, v))) for v in range(N)] for t in range(L + 1)]
    sol["lev"] = lev
    if XT and os.environ.get("VAL") == "1": sol["w"] = {f"{x},{k}": m.eval(wv[(x, k)], model_completion=True).as_long() for x in range(N) for k in (0, 1)}
    if XT: sol["xt"] = {f"{x},{k}": next((y for y in range(N) if y != x and tv(eo[(x, k, y)])), -1) for x in range(N) for k in (0, 1)}
    if FREEKP: sol["R_main"] = [[int(tv(Rk[(t, l)])) for l in range(m0)] for t in range(L + 1)]; sol["KP0"] = {v: int(tv(KP(0, v))) for v in range(N0) if lev[v] == 0}
    json.dump(sol, open(out, "w"))
