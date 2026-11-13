#!/usr/bin/env python3
"""Box 107 (L-SI successor 55): PAIR NETWORKS (docs/si/box107-timing.md §8).  P pairs of movers; pair p has a W-parent pair (an earlier pair or none) and a Xi-parent pair (any other
pair, acyclic, or the exit).  Mover (p,i), option o: W-target = member o of the W-parent, Xi-target = member o ^ x[p][i] of the
Xi-parent.  Keys root-first along the W-forest, values root-first along the Xi-forest (ranks of a Xi-parent's options above those of
its children), so both sides are one bit per pair:  om_p = the member with the smaller key, Om_p = the member with the larger value.
A mover switches iff its other option points W at om' (new state) of its W-parent and Xi at Om (old state) of its Xi-parent.
Query: a run of length >= T (default) or --full "p:i,..." (those movers switch 2^(Wdepth+1)-1 times; needs --chain).
Usage: pnsat.py P T [--chain] [--xchain] [--out FILE]   (--chain: W-parent of p is p-1)"""
import sys, itertools, time, json
from pysat.formula import IDPool, CNF
from pysat.card import CardEnc, EncType
from pysat.solvers import Solver
def build(P, T, chain=False, full=None, noexit2=False):
    pool = IDPool(); cnf = CNF(); v = pool.id; add = cnf.append
    def XOR(name, a, b):
        x = v(name); add([-x, a, b]); add([-x, -a, -b]); add([x, -a, b]); add([x, a, -b]); return x
    def AND(name, lits):
        x = v(name)
        for l in lits: add([-x, l])
        add([x] + [-l for l in lits]); return x
    NONE = -1
    WPs = lambda p: ([NONE] if p == 0 else ([p - 1] if chain else [NONE] + list(range(p))))
    XPs = lambda p: [NONE] + [q for q in range(P) if q != p]
    WP = lambda p, q: v(("WP", p, q)); XP = lambda p, q: v(("XP", p, q))
    for p in range(P):
        for dom, f in ((WPs(p), WP), (XPs(p), XP)):
            add([f(p, q) for q in dom])
            for q, q2 in itertools.combinations(dom, 2): add([-f(p, q), -f(p, q2)])
    OG = lambda p, r: v(("OG", p, r))                      # ORDX[p] >= r, r = 1..P-1
    for p in range(P):
        for r in range(2, P): add([-OG(p, r), OG(p, r - 1)])
        for q in range(P):
            if q == p: continue
            if P > 1: add([-XP(p, q), OG(p, 1)])
            for r in range(1, P):
                if r + 1 <= P - 1: add([-XP(p, q), -OG(q, r), OG(p, r + 1)])
                else: add([-XP(p, q), -OG(q, r)])
    X = lambda p, i: v(("X", p, i)); SW = lambda p, u: v(("SW", p, u)); SX = lambda p, u: v(("SX", p, u))
    def EP(p, q, q2): return v(("EP", p, q, q2)) if q < q2 else -v(("EP", p, q2, q))
    def BT(p, q, q2): return v(("BT", p, q, q2)) if q < q2 else -v(("BT", p, q2, q))
    for p in range(P):
        for a, b, c in itertools.permutations(range(4), 3):
            if a < b and a < c: add([-EP(p, a, b), -EP(p, b, c), EP(p, a, c)]); add([-BT(p, a, b), -BT(p, b, c), BT(p, a, c)])
    C = lambda t, p, i: v(("C", t, p, i))
    def mux(name, sel, dom, f):                             # name == f(q) for the selected q in dom (q != NONE)
        x = v(name)
        for q in dom:
            if q == NONE: continue
            y = f(q); add([-sel(q), -x, y]); add([-sel(q), x, -y])
        return x
    def om(t, p):
        key = ("OM", t, p)
        if key in pool.obj2id: return pool.obj2id[key]
        x = v(key); a, b = C(t, p, 0), C(t, p, 1); none = WP(p, NONE) if NONE in WPs(p) else None
        if none is not None:
            for ca in (0, 1):
                for cb in (0, 1):
                    pre = [-none, (-a if ca else a), (-b if cb else b)]; e = EP(p, 2 + cb, ca)
                    add(pre + [-x, e]); add(pre + [x, -e])
        if any(q != NONE for q in WPs(p)):
            lo = mux(("OMW", t, p), lambda q: WP(p, q), WPs(p), lambda q: om(t, q)); g = [] if none is None else [none]
            add(g + [-a, b, -x, -lo]); add(g + [-a, b, x, lo]); add(g + [a, -b, -x, lo]); add(g + [a, -b, x, -lo])
            for u in (0, 1):
                pre = g + [(-a if u else a), (-b if u else b)]
                add(pre + [-x, SW(p, u)]); add(pre + [x, -SW(p, u)])
        return x
    def Om(t, p):
        key = ("OMX", t, p)
        if key in pool.obj2id: return pool.obj2id[key]
        x = v(key); a, b = C(t, p, 0), C(t, p, 1); none = XP(p, NONE)
        for ca in (0, 1):
            for cb in (0, 1):
                pre = [-none, (-a if ca else a), (-b if cb else b)]; e = BT(p, 2 + cb, ca)
                add(pre + [-x, e]); add(pre + [x, -e])
        if P > 1:
            hi = mux(("OMXP", t, p), lambda q: XP(p, q), XPs(p), lambda q: Om(t, q)); g = [none]
            pa = XOR(("PA", t, p), a, X(p, 0)); pb = XOR(("PB", t, p), b, X(p, 1))
            add(g + [-pa, pb, -x, -hi]); add(g + [-pa, pb, x, hi]); add(g + [pa, -pb, -x, hi]); add(g + [pa, -pb, x, -hi])
            for u in (0, 1):
                pre = g + [(-pa if u else pa), (-pb if u else pb)]
                add(pre + [-x, SX(p, u)]); add(pre + [x, -SX(p, u)])
        return x
    S = {}
    for t in range(T):
        for p in range(P):
            for i in (0, 1):
                cur = C(t, p, i); kc = v(("KC", t, p, i)); vc = v(("VC", t, p, i))
                if NONE in WPs(p):
                    e = EP(p, 2 * i + 1, 2 * i); n_ = WP(p, NONE)       # kc <-> e xor cur
                    add([-n_, -kc, e, cur]); add([-n_, -kc, -e, -cur]); add([-n_, kc, -e, cur]); add([-n_, kc, e, -cur])
                if any(q != NONE for q in WPs(p)):
                    om(t + 1, p); lo = pool.obj2id[("OMW", t + 1, p)]; g = [WP(p, NONE)] if NONE in WPs(p) else []
                    add(g + [-kc, lo, cur]); add(g + [-kc, -lo, -cur]); add(g + [kc, -lo, cur]); add(g + [kc, lo, -cur])
                e = BT(p, 2 * i + 1, 2 * i); n_ = XP(p, NONE)
                add([-n_, -vc, e, cur]); add([-n_, -vc, -e, -cur]); add([-n_, vc, -e, cur]); add([-n_, vc, e, -cur])
                if P > 1:
                    Om(t, p); hi = pool.obj2id[("OMXP", t, p)]; tg = XOR(("TG", t, p, i), cur, X(p, i))
                    add([n_, -vc, hi, tg]); add([n_, -vc, -hi, -tg]); add([n_, vc, -hi, tg]); add([n_, vc, hi, -tg])
                s = AND(("S", t, p, i), [kc, vc]); S[t, p, i] = s
                n = C(t + 1, p, i); add([-n, cur, s]); add([-n, -cur, -s]); add([n, -cur, s]); add([n, cur, -s])
    if full:
        for p, i in full:
            need = 2 ** (p + 1) - 1
            if need > T: add([]); continue
            cnf.extend(CardEnc.equals(lits=[S[t, p, i] for t in range(T)], bound=need, vpool=pool, encoding=EncType.seqcounter).clauses)
    else:
        for t in range(T): add([S[t, p, i] for p in range(P) for i in (0, 1)])
    return cnf, pool
def decode(P, T, model, pool, chain):
    val = set(l for l in model if l > 0); tv = lambda k: pool.obj2id.get(k) in val
    NONE = -1
    wp = [next((q for q in [NONE] + list(range(p)) if tv(("WP", p, q))), NONE) for p in range(P)]
    xp = [next((q for q in [NONE] + [q for q in range(P) if q != p] if tv(("XP", p, q))), NONE) for p in range(P)]
    def order(tag, p, less):   # rank of the 4 options under the order relation (count of options it beats)
        f = lambda q, q2: tv((tag, p, q, q2)) if q < q2 else not tv((tag, p, q2, q))
        return [sum(1 for q2 in range(4) if q2 != q and f(q, q2)) for q in range(4)]
    D = {"P": P, "wp": wp, "xp": xp, "x": [[int(tv(("X", p, i))) for i in (0, 1)] for p in range(P)],
         "sW": [[int(tv(("SW", p, u))) for u in (0, 1)] for p in range(P)], "sX": [[int(tv(("SX", p, u))) for u in (0, 1)] for p in range(P)],
         "epsless": [order("EP", p, 0) for p in range(P)], "betagreater": [order("BT", p, 0) for p in range(P)],
         "start": [[int(tv(("C", 0, p, i))) for i in (0, 1)] for p in range(P)],
         "states": [[[int(tv(("C", t, p, i))) for i in (0, 1)] for p in range(P)] for t in range(T + 1)]}
    return D
if __name__ == "__main__":
    a = sys.argv[1:]; P, T = int(a[0]), int(a[1]); chain = "--chain" in a
    full = [tuple(map(int, s.split(":"))) for s in a[a.index("--full") + 1].split(",")] if "--full" in a else None
    cnf, pool = build(P, T, chain, full); t0 = time.time()
    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as so:
        r = so.solve()
        print(f"PN107 P {P} T {T} chain {int(chain)} full {full} vars {pool.top} clauses {len(cnf.clauses)} answer {'SAT' if r else 'UNSAT'}" + ("" if "--notime" in a else f" time {time.time() - t0:.1f}s"), flush=True)
        if r:
            D = decode(P, T, so.get_model(), pool, chain)
            if "--print" in a: print(" wp", D["wp"], "xp", D["xp"], "x", D["x"], "start", D["start"])
            if "--out" in a: json.dump(D, open(a[a.index("--out") + 1], "w"))
