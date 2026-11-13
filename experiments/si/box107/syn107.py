#!/usr/bin/env python3
"""Box 107 (L-SI successor 55): SAT synthesis of 2-per-level ladder genomes for L-NEW's one-player model 1P(G) (box 217 §1).
Unknown: the Xi-targets, the beta order and parities, the key bits (level-0 eps order, sigma bits above), the start state.
Query: is there a Xi-acyclic ladder genome with d levels whose key run, within T steps, satisfies the goal?
  goal "full:x,y,.."  : the listed movers switch exactly 2^(lev+1) - 1 times (sw = |K| - 1)
  goal "len"          : every one of the T steps has at least one switch (a run of length >= T)
Ladder: mover 2l + i (i = 0: a_l, 1: b_l), option o has W-target 2(l-1) + o.  Key side as one bit per level (Lemma OMEGA):
om_l = the level-l mover with the smaller key.  Values: sets of options on the Xi-path, compared by the top-rank element of the
symmetric difference (weights +-2^rank), exactly box 217's order (hops never decide: two options of one mover differ).
A model is decoded to a genome in L-NEW's JSON format and must be replayed by replay107.py (their one217.OneP) before it is cited.
CONTROL (--fix G.json): every parameter of the given ladder genome is added as a unit clause; «len T» must then be SAT for T = its
T_key and UNSAT for T_key + 1 (the encoder neither loses nor invents runs on that instance).
Usage: syn107.py d T goal [--solver cadical195] [--out FILE.json] [--fix G.json] [--notime] [--print]"""
import sys, json, itertools, time
from pysat.formula import IDPool, CNF
from pysat.card import CardEnc, EncType
from pysat.solvers import Solver

def build(d, T, goal, extra=(), fix=None):
    N = 2 * d; Q = 2 * N; EXIT = N
    pool = IDPool(); cnf = CNF(); v = pool.id
    add = cnf.append
    def AND(name, lits):           # name <-> AND lits
        x = v(name)
        for l in lits: add([-x, l])
        add([x] + [-l for l in lits]); return x
    def OR(name, lits):
        x = v(name)
        for l in lits: add([x, -l])
        add([-x] + list(lits)); return x
    def XOR(name, a, b):
        x = v(name); add([-x, a, b]); add([-x, -a, -b]); add([x, -a, b]); add([x, a, -b]); return x
    lev = lambda x: x // 2
    # --- parameters
    XT = lambda x, o, y: v(("XT", x, o, y))
    for x in range(N):
        for o in (0, 1):
            add([XT(x, o, y) for y in range(N + 1)])
            for y, y2 in itertools.combinations(range(N + 1), 2): add([-XT(x, o, y), -XT(x, o, y2)])
            add([-XT(x, o, x)])
    ORDge = lambda x, r: v(("ORD", x, r))        # ORD[x] >= r, r = 1..N-1
    for x in range(N):
        for r in range(2, N): add([-ORDge(x, r), ORDge(x, r - 1)])
    for x in range(N):
        for o in (0, 1):
            for y in range(N):
                if y == x: continue
                add([-XT(x, o, y), ORDge(x, 1)])
                for r in range(1, N):
                    if r + 1 <= N - 1: add([-XT(x, o, y), -ORDge(y, r), ORDge(x, r + 1)])
                    else: add([-XT(x, o, y), -ORDge(y, r)])
    def PREC(q, q2):               # option q has the higher rank
        return v(("PR", q, q2)) if q < q2 else -v(("PR", q2, q))
    for a, b, c in itertools.permutations(range(Q), 3):
        if a < b and a < c: add([-PREC(a, b), -PREC(b, c), PREC(a, c)])   # each cyclic triple once per rotation class
    POS = lambda q: v(("POS", q))
    def EP(q, q2):                 # level-0 option q has the smaller eps (q = 2i + o, i in {0,1})
        return v(("EP", q, q2)) if q < q2 else -v(("EP", q2, q))
    for a, b, c in itertools.permutations(range(4), 3):
        if a < b and a < c: add([-EP(a, b), -EP(b, c), EP(a, c)])
    SW = lambda l, u: v(("SW", l, u))             # l >= 1: 1 iff b_l has the smaller key when both point W at (l-1, u)
    C = lambda t, x: v(("C", t, x))
    # --- omega of state t
    def omega(t, l):
        key = ("OM", t, l)
        if key in pool.obj2id: return pool.obj2id[key]
        x = v(key); a, b = C(t, 2 * l), C(t, 2 * l + 1)
        if l == 0:
            for ca in (0, 1):
                for cb in (0, 1):
                    pre = [(-a if ca else a), (-b if cb else b)]     # negated antecedent
                    e = EP(2 + cb, ca)                                # eps(b, cb) < eps(a, ca)
                    add(pre + [-x, e]); add(pre + [x, -e])
        else:
            lo = omega(t, l - 1)
            # a != b: x <-> (b == lo)
            add([-a, b, -x, -lo]); add([-a, b, x, lo])               # a=1,b=0: x <-> not lo ... b==lo means lo=0
            add([a, -b, -x, lo]); add([a, -b, x, -lo])               # a=0,b=1: x <-> lo
            for u in (0, 1):
                pre = [(-a if u else a), (-b if u else b)]
                add(pre + [-x, SW(l, u)]); add(pre + [x, -SW(l, u)])
        return x
    # --- values at states 0..T-1
    SWT = {}
    for t in range(T):
        NX = {}
        for y in range(N):
            for y2 in range(N):
                if y2 == y: continue
                n = v(("NX", t, y, y2)); c = C(t, y)
                add([-n, c, XT(y, 0, y2)]); add([-n, -c, XT(y, 1, y2)])
                add([n, c, -XT(y, 0, y2)]); add([n, -c, -XT(y, 1, y2)])
                NX[y, y2] = n
        PM = lambda y, q: v(("PM", t, y, q))
        for y in range(N):
            for q in range(Q):
                if q // 2 == y:
                    c = C(t, y); add([PM(y, q), (c if q % 2 == 0 else -c)]); add([-PM(y, q), (-c if q % 2 == 0 else c)])
                else:
                    terms = [AND(("NP", t, y, y2, q), [NX[y, y2], PM(y2, q)]) for y2 in range(N) if y2 != y]
                    x_ = PM(y, q)
                    for l_ in terms: add([x_, -l_])
                    add([-x_] + terms)
        for x in range(N):
            PO = {}
            for o in (0, 1):
                for q in range(Q):
                    if q // 2 == x:
                        PO[o, q] = None if q % 2 != o else True
                    else:
                        terms = [AND(("XP", t, x, o, y2, q), [XT(x, o, y2), PM(y2, q)]) for y2 in range(N) if y2 != x]
                        PO[o, q] = OR(("PO", t, x, o, q), terms)
            D = {}; F1 = {}                         # D: in the symmetric difference; F1: in option 1's set
            for q in range(Q):
                if q // 2 == x: D[q] = True; F1[q] = (q % 2 == 1)
                else: D[q] = XOR(("D", t, x, q), PO[0, q], PO[1, q]); F1[q] = PO[1, q]
            TOP = lambda q: v(("TOP", t, x, q)); BET = v(("BET", t, x))
            add([TOP(q) for q in range(Q)])
            for q in range(Q):
                if D[q] is not True: add([-TOP(q), D[q]])
                for q2 in range(Q):
                    if q2 == q: continue
                    add([-TOP(q), PREC(q, q2)] + ([] if D[q2] is True else [-D[q2]]))
                # BET <-> (F1[q] <-> POS[q]) under TOP(q)
                if F1[q] is True: add([-TOP(q), -BET, POS(q)]); add([-TOP(q), BET, -POS(q)])
                elif F1[q] is False: add([-TOP(q), -BET, -POS(q)]); add([-TOP(q), BET, POS(q)])
                else:
                    f = F1[q]
                    add([-TOP(q), -BET, -f, POS(q)]); add([-TOP(q), -BET, f, -POS(q)])
                    add([-TOP(q), BET, -f, -POS(q)]); add([-TOP(q), BET, f, POS(q)])
            cur = C(t, x); XC = XOR(("XC", t, x), BET, cur)          # the other option is strictly better
            if lev(x) == 0:
                dirx = EP(2 * (x % 2) + 1, 2 * (x % 2))               # eps(x, 1) < eps(x, 0)
                KC = XOR(("KC", t, x), dirx, cur)
            else:
                KC = XOR(("KC", t, x), cur, omega(t + 1, lev(x) - 1))
            s = AND(("SWT", t, x), [XC, KC]); SWT[t, x] = s
            n = C(t + 1, x); add([-n, cur, s]); add([-n, -cur, -s]); add([n, -cur, s]); add([n, cur, -s])
    # --- goal
    if goal.startswith("full:"):
        for x in map(int, goal[5:].split(",")):
            need = 2 ** (lev(x) + 1) - 1
            if need > T: add([]); continue
            ce = CardEnc.equals(lits=[SWT[t, x] for t in range(T)], bound=need, vpool=pool, encoding=EncType.seqcounter)
            cnf.extend(ce.clauses)
    elif goal == "len":
        for t in range(T): add([SWT[t, x] for x in range(N)])
    if fix is not None:                              # CONTROL: all parameters of a given ladder genome as unit clauses
        G = fix; assert G["N"] == N
        for x in range(N):
            for o in (0, 1):
                assert G["opts"][x][o][0] == (2 * (x // 2 - 1) + o if x >= 2 else -1), "not a ladder"
                y = G["opts"][x][o][1]; add([XT(x, o, y if y >= 0 else EXIT)])
        for q in range(Q):
            add([POS(q) if G["bp"][q] == 0 else -POS(q)])
            for q2 in range(q + 1, Q): add([PREC(q, q2) if G["br"][q] > G["br"][q2] else -PREC(q, q2)])
        e_ = [G["gate"][0][0], G["gate"][0][1], G["gate"][1][0], G["gate"][1][1]]
        for q, q2 in itertools.combinations(range(4), 2): add([EP(q, q2) if e_[q] < e_[q2] else -EP(q, q2)])
        for l in range(1, d):
            for u in (0, 1): add([SW(l, u) if G["gate"][2 * l + 1][u] < G["gate"][2 * l][u] else -SW(l, u)])
        for x in range(N): add([C(0, x) if G["start"][x] else -C(0, x)])
    for e in extra:                                  # extra constraints: "nosw:x" mover x never switches; "exit:x" both options to the exit
        k, _, a = e.partition(":")
        if k == "nosw":
            for t in range(T): add([-SWT[t, int(a)]])
        elif k == "exit":
            add([XT(int(a), 0, EXIT)]); add([XT(int(a), 1, EXIT)])
    return cnf, pool, SWT

def decode(d, T, model, pool):
    N = 2 * d; Q = 2 * N; val = set(l for l in model if l > 0)
    tv = lambda key: (pool.obj2id.get(key) in val)
    xt = [[next(y for y in range(N + 1) if tv(("XT", x, o, y))) for o in (0, 1)] for x in range(N)]
    def prec(q, q2): return tv(("PR", q, q2)) if q < q2 else not tv(("PR", q2, q))
    rank = [sum(1 for q2 in range(Q) if q2 != q and prec(q, q2)) for q in range(Q)]   # number of options below q
    assert sorted(rank) == list(range(Q)), rank
    pos = [tv(("POS", q)) for q in range(Q)]
    def ep(q, q2): return tv(("EP", q, q2)) if q < q2 else not tv(("EP", q2, q))
    e0 = [sum(1 for q2 in range(4) if q2 != q and ep(q2, q)) for q in range(4)]       # eps rank of level-0 option q (0 = smallest)
    assert sorted(e0) == [0, 1, 2, 3]
    gate = [[e0[0], e0[1]], [e0[2], e0[3]]]
    for l in range(1, d):
        ga, gb = [0, 0], [0, 0]
        for u in (0, 1):
            sw = tv(("SW", l, u))
            ga[u], gb[u] = (1000 * l + 2 * u + 1, 1000 * l + 2 * u) if sw else (1000 * l + 2 * u, 1000 * l + 2 * u + 1)
        gate += [ga, gb]
    start = [int(tv(("C", 0, x))) for x in range(N)]
    states = [[int(tv(("C", t, x))) for x in range(N)] for t in range(T + 1)]
    G = {"N": N, "lev": [x // 2 for x in range(N)], "deg": 2,
         "opts": [[[(2 * (x // 2 - 1) + o) if x >= 2 else -1, (xt[x][o] if xt[x][o] < N else -1), 2 * x + o] for o in (0, 1)] for x in range(N)],
         "gate": gate, "br": rank, "bp": [0 if pos[q] else 1 for q in range(Q)], "start": start}
    return G, states

if __name__ == "__main__":
    a = sys.argv[1:]; d, T, goal = int(a[0]), int(a[1]), a[2]
    solver = a[a.index("--solver") + 1] if "--solver" in a else "cadical195"
    extra = a[a.index("--extra") + 1].split(";") if "--extra" in a else ()
    fix = None
    if "--fix" in a:
        fix = json.load(open(a[a.index("--fix") + 1])); fix = fix.get("genome", fix)
    t0 = time.time(); cnf, pool, SWT = build(d, T, goal, extra, fix)
    NT = "--notime" in a
    print(f"d {d} T {T} goal {goal} extra {list(extra)}" + (" FIXED " + a[a.index("--fix") + 1] if fix else "") + f" vars {pool.top} clauses {len(cnf.clauses)}" + ("" if NT else f" build {time.time() - t0:.1f}s"), flush=True)
    with Solver(name=solver, bootstrap_with=cnf.clauses) as S:
        t1 = time.time(); r = S.solve()
        print(f"SYN107 d {d} T {T} goal {goal} extra {list(extra)}" + (" FIXED " + a[a.index("--fix") + 1] if fix else "") + f" solver {solver} answer {'SAT' if r else 'UNSAT'}" + ("" if NT else f" time {time.time() - t1:.1f}s"), flush=True)
        if r:
            G, states = decode(d, T, S.get_model(), pool)
            out = a[a.index("--out") + 1] if "--out" in a else None
            if out: json.dump({"genome": G, "states": states, "d": d, "T": T, "goal": goal}, open(out, "w"))
            if "--print" in a: print("genome", json.dumps(G))
