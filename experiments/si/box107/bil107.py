#!/usr/bin/env python3
"""Box 107 (L-SI successor 55): exact SAT on the anti-aligned bi-ladder B_d (docs/si/box107-timing.md §8: levels 0..d-1, two movers per
level, mover (l,i) option o has W-target (l-1,o) and Xi-target (l+1, o ^ x[l][i]); keys and values one bit per level): is there a parameter choice and start with a
run of length >= T?  Usage: bisat.py d T [--full L]  (--full L: both movers of levels 0..L-1 switch 2^(l+1)-1 times instead)"""
import sys, itertools, time
from pysat.formula import IDPool, CNF
from pysat.card import CardEnc, EncType
from pysat.solvers import Solver
def build(d, T, full=None):
    pool = IDPool(); cnf = CNF(); v = pool.id; add = cnf.append
    def XOR(name, a, b):
        x = v(name); add([-x, a, b]); add([-x, -a, -b]); add([x, -a, b]); add([x, a, -b]); return x
    def AND(name, lits):
        x = v(name)
        for l in lits: add([-x, l])
        add([x] + [-l for l in lits]); return x
    X = lambda l, i: v(("X", l, i)); SW = lambda l, u: v(("SW", l, u)); SX = lambda l, u: v(("SX", l, u))
    def EP(q, q2): return v(("EP", q, q2)) if q < q2 else -v(("EP", q2, q))     # eps(q) < eps(q2), level-0 options q = 2i+o
    def BT(q, q2): return v(("BT", q, q2)) if q < q2 else -v(("BT", q2, q))     # beta(q) > beta(q2), top-level options
    for a, b, c in itertools.permutations(range(4), 3):
        if a < b and a < c: add([-EP(a, b), -EP(b, c), EP(a, c)]); add([-BT(a, b), -BT(b, c), BT(a, c)])
    C = lambda t, l, i: v(("C", t, l, i))
    def om(t, l):          # 1 iff mover b of level l has the smaller key in state t
        key = ("OM", t, l)
        if key in pool.obj2id: return pool.obj2id[key]
        x = v(key); a, b = C(t, l, 0), C(t, l, 1)
        if l == 0:
            for ca in (0, 1):
                for cb in (0, 1):
                    pre = [(-a if ca else a), (-b if cb else b)]; e = EP(2 + cb, ca)
                    add(pre + [-x, e]); add(pre + [x, -e])
        else:
            lo = om(t, l - 1)
            add([-a, b, -x, -lo]); add([-a, b, x, lo]); add([a, -b, -x, lo]); add([a, -b, x, -lo])
            for u in (0, 1):
                pre = [(-a if u else a), (-b if u else b)]
                add(pre + [-x, SW(l, u)]); add(pre + [x, -SW(l, u)])
        return x
    def Om(t, l):          # 1 iff mover b of level l has the larger value in state t
        key = ("OMX", t, l)
        if key in pool.obj2id: return pool.obj2id[key]
        x = v(key); a, b = C(t, l, 0), C(t, l, 1)
        if l == d - 1:
            for ca in (0, 1):
                for cb in (0, 1):
                    pre = [(-a if ca else a), (-b if cb else b)]; e = BT(2 + cb, ca)
                    add(pre + [-x, e]); add(pre + [x, -e])
        else:
            hi = Om(t, l + 1); pa = XOR(("PA", t, l), a, X(l, 0)); pb = XOR(("PB", t, l), b, X(l, 1))
            add([-pa, pb, -x, -hi]); add([-pa, pb, x, hi]); add([pa, -pb, -x, hi]); add([pa, -pb, x, -hi])
            for u in (0, 1):
                pre = [(-pa if u else pa), (-pb if u else pb)]
                add(pre + [-x, SX(l, u)]); add(pre + [x, -SX(l, u)])
        return x
    S = {}
    for t in range(T):
        for l in range(d):
            for i in (0, 1):
                cur = C(t, l, i)
                if l == 0: kc = XOR(("KC", t, l, i), EP(2 * i + 1, 2 * i), cur)        # eps(i,1) < eps(i,0) xor cur
                else: kc = XOR(("KC", t, l, i), cur, om(t + 1, l - 1))                 # other == om  <=> cur != om
                if l == d - 1: vc = XOR(("VC", t, l, i), BT(2 * i + 1, 2 * i), cur)   # beta(i,1) > beta(i,0) xor cur
                else:
                    tgt = XOR(("TG", t, l, i), cur, X(l, i))                            # Xi-target of the current option; other = not tgt
                    vc = XOR(("VC", t, l, i), tgt, Om(t, l + 1))                        # other target == Om <=> tgt != Om
                s = AND(("S", t, l, i), [kc, vc]); S[t, l, i] = s
                n = C(t + 1, l, i); add([-n, cur, s]); add([-n, -cur, -s]); add([n, -cur, s]); add([n, cur, -s])
    if full is None:
        for t in range(T): add([S[t, l, i] for l in range(d) for i in (0, 1)])
    else:
        for l in range(full):
            for i in (0, 1):
                need = 2 ** (l + 1) - 1
                if need > T: add([]); continue
                cnf.extend(CardEnc.equals(lits=[S[t, l, i] for t in range(T)], bound=need, vpool=pool, encoding=EncType.seqcounter).clauses)
    return cnf, pool
if __name__ == "__main__":
    a = sys.argv[1:]; d, T = int(a[0]), int(a[1]); full = int(a[a.index("--full") + 1]) if "--full" in a else None
    cnf, pool = build(d, T, full); t0 = time.time()
    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as so:
        r = so.solve()
        print(f"BIL107 d {d} T {T} full {full} vars {pool.top} clauses {len(cnf.clauses)} answer {'SAT' if r else 'UNSAT'}" + ("" if "--notime" in a else f" time {time.time() - t0:.1f}s"), flush=True)
