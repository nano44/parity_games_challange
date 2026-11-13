#!/usr/bin/env python3
"""Box 107 (L-SI successor 55): SAT synthesis in the class of UPWARD ladders: a 2-per-level ladder (as syn107.py) in which every
Xi-target lies on a strictly higher W-level (or is the exit) and the beta ranks increase with the W-level (so the Xi-graph is
acyclic by construction and the value of an option is compared at the highest level where the two Xi-paths differ: two different
movers there -> the signed weights of their current options, one mover against none -> its sign; equal paths -> the mover's own two
weights).  Everything else (key bits, rule, goals) as in syn107.py.  Models are decoded to L-NEW genomes; replay107.py must confirm.
Usage: up107.py d T goal [--notime] [--out FILE] [--maxjump J] [--fuelonly h]
  goal: full:x,y,..  |  cap:h (both movers of levels 0..h-1 full)  |  len
  --maxjump J : Xi-targets at most J levels up;   --fuelonly h : movers of levels < h have Xi-targets on levels >= h only
  --upperbil h : movers of levels >= h have both Xi-targets on the next level (top level: the exit)
  --lift FILE [--mid m] [--free L,L]: FILE = a genome with d - 2 levels, embedded with its Xi-targets, weights and key bits: without
                 --mid one level up (new bottom and top levels), with --mid m two new levels m, m + 1 are inserted (old levels >= m go
                 up by 2); --free lists levels of the new ladder whose old wiring is dropped;
                 old: its movers are placed one level up with their Xi-targets, weights and sigma bits
                 (old exits may go to the exit or to the new top level); only the new bottom and top levels, sigma_1 and the start are free
  --hered      : add the constraints implied by box 107's lemmas for the full movers (every lower mover's key changes
                 2^(l+1) - 1 times; ABANDON at the full movers): redundant, they only help the solver
  --dualcap h  : movers of levels l >= h switch exactly 2^(d-l) - 1 times;   --extra sw:x:n,st:x:c : switch counts / start options"""
import sys, json, itertools, time
from pysat.formula import IDPool, CNF
from pysat.card import CardEnc, EncType
from pysat.solvers import Solver
def build(d, T, goal, maxjump=None, fuelonly=None, upperbil=None, dualcap=None, extra=(), lift=None, hered=False):
    N = 2 * d; EXIT = N; pool = IDPool(); cnf = CNF(); v = pool.id; add = cnf.append
    lev = lambda x: x // 2
    def AND(name, lits):
        x = v(name)
        for l in lits: add([-x, l])
        add([x] + [-l for l in lits]); return x
    def OR(name, lits):
        x = v(name)
        for l in lits: add([x, -l])
        add([-x] + list(lits)); return x
    def XOR(name, a, b):
        x = v(name); add([-x, a, b]); add([-x, -a, -b]); add([x, -a, b]); add([x, a, -b]); return x
    def dom(x):
        lo = lev(x) + 1
        if fuelonly is not None and lev(x) < fuelonly: lo = max(lo, fuelonly)
        hi = d - 1 if maxjump is None else min(d - 1, lev(x) + maxjump)
        if upperbil is not None and lev(x) >= upperbil:
            return [EXIT] if lev(x) == d - 1 else [y for y in range(N) if lev(y) == lev(x) + 1]
        return [y for y in range(N) if lo <= lev(y) <= hi] + [EXIT]
    XT = lambda x, o, y: v(("XT", x, o, y))
    for x in range(N):
        for o in (0, 1):
            D = dom(x); add([XT(x, o, y) for y in D])
            for y, y2 in itertools.combinations(D, 2): add([-XT(x, o, y), -XT(x, o, y2)])
    def GT(L, q, q2): return v(("GT", L, q, q2)) if q < q2 else -v(("GT", L, q2, q))     # signed weight of option q of level L is larger
    POS = lambda L, q: v(("POS", L, q))
    for L in range(d):
        for a, b, c in itertools.permutations(range(4), 3):
            if a < b and a < c: add([-GT(L, a, b), -GT(L, b, c), GT(L, a, c)])
        for q, q2 in itertools.permutations(range(4), 2): add([-POS(L, q), POS(L, q2), GT(L, q, q2)])
    if lift is not None:      # lift = (old genome with d - 2 levels, insertion level m, levels of the NEW ladder left free)
        Go, m_, freeL = lift; No = Go["N"]; assert No == N - 4
        fL = lambda Lo: Lo if Lo < m_ else Lo + 2                      # m_ = 0: old movers go one level up... (m_ = 0 means shift by 1)
        if m_ == 0: fL = lambda Lo: Lo + 1
        fx = lambda xo: 2 * fL(xo // 2) + xo % 2
        newlevels = [L for L in range(d) if L not in [fL(Lo) for Lo in range(No // 2)]]
        pro = lambda b: 6 + 2 * Go["br"][b] + Go["bp"][b]
        for xo in range(No):
            x = fx(xo)
            if lev(x) in freeL: continue
            for o in (0, 1):
                yo = Go["opts"][xo][o][1]
                if yo >= 0: add([XT(x, o, fx(yo))])
                else: add([XT(x, o, y) for y in [EXIT] + [yy for yy in range(N) if lev(yy) in newlevels and lev(yy) > lev(x)]])
        for Lo in range(No // 2):
            L = fL(Lo); w = []
            if L in freeL: continue
            for q in range(4):
                b = 2 * (2 * Lo + q // 2) + q % 2; p_ = pro(b); w.append((1 if p_ % 2 == 0 else -1) * (2 ** Go["br"][b]))
                add([POS(L, q) if p_ % 2 == 0 else -POS(L, q)])
            for q, q2 in itertools.combinations(range(4), 2): add([GT(L, q, q2) if w[q] > w[q2] else -GT(L, q, q2)])
    def EP(q, q2): return v(("EP", q, q2)) if q < q2 else -v(("EP", q2, q))
    for a, b, c in itertools.permutations(range(4), 3):
        if a < b and a < c: add([-EP(a, b), -EP(b, c), EP(a, c)])
    SW = lambda l, u: v(("SW", l, u)); C = lambda t, x: v(("C", t, x))
    if lift is not None:
        Go, m_, freeL = lift
        for lo in range(1, Go["N"] // 2):
            L = (lo + 1) if m_ == 0 else (lo if lo < m_ else lo + 2)
            if L in freeL or (m_ > 0 and lo == m_): continue          # the level just above the insertion reads a new pair: its sigma is free
            for u in (0, 1):
                g = Go["gate"]; add([SW(L, u) if g[2 * lo + 1][u] < g[2 * lo][u] else -SW(L, u)])
        if m_ > 0:                                                     # level 0 is old: keep its eps order
            g = Go["gate"]; e_ = [g[0][0], g[0][1], g[1][0], g[1][1]]
            for q, q2 in itertools.combinations(range(4), 2): add([EP(q, q2) if e_[q] < e_[q2] else -EP(q, q2)])
    def omega(t, l):
        key = ("OM", t, l)
        if key in pool.obj2id: return pool.obj2id[key]
        x = v(key); a, b = C(t, 2 * l), C(t, 2 * l + 1)
        if l == 0:
            for ca in (0, 1):
                for cb in (0, 1):
                    pre = [(-a if ca else a), (-b if cb else b)]; e = EP(2 + cb, ca)
                    add(pre + [-x, e]); add(pre + [x, -e])
        else:
            lo = omega(t, l - 1)
            add([-a, b, -x, -lo]); add([-a, b, x, lo]); add([a, -b, -x, lo]); add([a, -b, x, -lo])
            for u in (0, 1):
                pre = [(-a if u else a), (-b if u else b)]
                add(pre + [-x, SW(l, u)]); add(pre + [x, -SW(l, u)])
        return x
    SWT = {}
    for t in range(T):
        # current Xi-target of y, and which mover of each higher level y's path visits
        VIS = {}
        for y in range(N - 1, -1, -1):
            c = C(t, y); NX = {}
            for y1 in dom(y):
                if y1 == EXIT: continue
                n = v(("NX", t, y, y1)); NX[y1] = n
                add([-n, c, XT(y, 0, y1)]); add([-n, -c, XT(y, 1, y1)]); add([n, c, -XT(y, 0, y1)]); add([n, -c, -XT(y, 1, y1)])
            for m in range(2 * (lev(y) + 1), N):
                terms = []
                for y1, n in NX.items():
                    if y1 == m: terms.append(n)
                    elif lev(y1) < lev(m): terms.append(AND(("NV", t, y, y1, m), [n, VIS[y1, m]]))
                VIS[y, m] = OR(("VIS", t, y, m), terms) if terms else None
        for x in range(N):
            VO = {}
            for o in (0, 1):
                for m in range(2 * (lev(x) + 1), N):
                    terms = []
                    for y1 in dom(x):
                        if y1 == EXIT: continue
                        if y1 == m: terms.append(XT(x, o, y1))
                        elif lev(y1) < lev(m) and VIS[y1, m] is not None: terms.append(AND(("XV", t, x, o, y1, m), [XT(x, o, y1), VIS[y1, m]]))
                    VO[o, m] = OR(("VO", t, x, o, m), terms) if terms else None
            BET = v(("BET", t, x)); undecided = []          # literals: «no difference at any level above L»
            own = GT(lev(x), 2 * (x % 2) + 1, 2 * (x % 2))
            for L in range(d - 1, lev(x), -1):
                a, b = 2 * L, 2 * L + 1
                def lit(o, m): return VO[o, m]
                ds = []
                for m in (a, b):
                    l0, l1 = lit(0, m), lit(1, m)
                    if l0 is None and l1 is None: continue
                    if l0 is None: ds.append(l1)
                    elif l1 is None: ds.append(l0)
                    else: ds.append(XOR(("DX", t, x, m), l0, l1))
                if not ds: continue
                DIFF = OR(("DIFF", t, x, L), ds)
                pre = [-DIFF] + [u for u in undecided]        # clause prefix: DIFF here and no DIFF above
                # cases: (m0, m1) = which mover each option's path visits at level L (None = no mover)
                for m0 in (a, b, None):
                    for m1 in (a, b, None):
                        if m0 == m1: continue
                        cond = []; ok = True
                        for o, mm in ((0, m0), (1, m1)):
                            for m in (a, b):
                                l_ = lit(o, m)
                                if mm == m:
                                    if l_ is None: ok = False
                                    else: cond.append(-l_)
                                elif l_ is not None: cond.append(l_)
                        if not ok: continue
                        if m1 is None:      # option 0 has the extra element (m0, c): better iff positive
                            for cc in (0, 1):
                                g = [(-C(t, m0) if cc else C(t, m0))]; p_ = POS(L, 2 * (m0 % 2) + cc)
                                add(pre + cond + g + [-BET, -p_]); add(pre + cond + g + [BET, p_])
                        elif m0 is None:
                            for cc in (0, 1):
                                g = [(-C(t, m1) if cc else C(t, m1))]; p_ = POS(L, 2 * (m1 % 2) + cc)
                                add(pre + cond + g + [-BET, p_]); add(pre + cond + g + [BET, -p_])
                        else:
                            for c0 in (0, 1):
                                for c1 in (0, 1):
                                    g = [(-C(t, m0) if c0 else C(t, m0)), (-C(t, m1) if c1 else C(t, m1))]
                                    e = GT(L, 2 * (m1 % 2) + c1, 2 * (m0 % 2) + c0)
                                    add(pre + cond + g + [-BET, e]); add(pre + cond + g + [BET, -e])
                undecided.append(DIFF)
            add([u for u in undecided] + [-BET, own]); add([u for u in undecided] + [BET, -own])
            cur = C(t, x); XC = XOR(("XC", t, x), BET, cur)
            if lev(x) == 0: KC = XOR(("KC", t, x), EP(2 * (x % 2) + 1, 2 * (x % 2)), cur)
            else: KC = XOR(("KC", t, x), cur, omega(t + 1, lev(x) - 1))
            s = AND(("SWT", t, x), [XC, KC]); SWT[t, x] = s
            n = C(t + 1, x); add([-n, cur, s]); add([-n, -cur, -s]); add([n, -cur, s]); add([n, cur, -s])
    fulls = []
    if goal.startswith("full:"): fulls = list(map(int, goal[5:].split(",")))
    elif goal.startswith("cap:"): fulls = list(range(2 * int(goal[4:])))
    elif goal == "len":
        for t in range(T): add([SWT[t, x] for x in range(N)])
    if fulls and hered:      # implied by the lemmas of box 107 (HEREDITY + FULL-ORDER + ABANDON): redundant constraints for the solver
        KCH = {}
        for t in range(T):
            for x in range(N):
                if lev(x) == 0: KCH[t, x] = SWT[t, x]
                else:
                    c = C(t, x); ta, tb = KCH[t, 2 * (lev(x) - 1)], KCH[t, 2 * (lev(x) - 1) + 1]
                    KCH[t, x] = OR(("KCH", t, x), [SWT[t, x], AND(("KA", t, x), [-c, ta]), AND(("KB", t, x), [c, tb])])
        top = max(lev(x) for x in fulls)
        for x in range(N):
            if lev(x) < top and x not in fulls:
                cnf.extend(CardEnc.equals(lits=[KCH[t, x] for t in range(T)], bound=2 ** (lev(x) + 1) - 1, vpool=pool, encoding=EncType.seqcounter).clauses)
        for x in fulls:
            if lev(x) == 0: continue
            for t in range(T):
                add([C(t, x), -KCH[t, 2 * (lev(x) - 1)]]); add([-C(t, x), -KCH[t, 2 * (lev(x) - 1) + 1]])
    if dualcap is not None:
        for x in range(2 * dualcap, N):
            need = 2 ** (d - lev(x)) - 1
            if need > T: add([]); continue
            cnf.extend(CardEnc.equals(lits=[SWT[t, x] for t in range(T)], bound=need, vpool=pool, encoding=EncType.seqcounter).clauses)
    for e in extra:                      # "sw:x:n" mover x switches exactly n times; "st:x:c" start option
        k_, a_, b_ = e.split(":")
        if k_ == "sw": cnf.extend(CardEnc.equals(lits=[SWT[t, int(a_)] for t in range(T)], bound=int(b_), vpool=pool, encoding=EncType.seqcounter).clauses)
        elif k_ == "st": add([C(0, int(a_)) if int(b_) else -C(0, int(a_))])
    for x in fulls:
        need = 2 ** (lev(x) + 1) - 1
        if need > T: add([]); continue
        cnf.extend(CardEnc.equals(lits=[SWT[t, x] for t in range(T)], bound=need, vpool=pool, encoding=EncType.seqcounter).clauses)
    return cnf, pool
def decode(d, T, model, pool):
    N = 2 * d; val = set(l for l in model if l > 0); tv = lambda k: pool.obj2id.get(k) in val
    xt = [[next((y for y in range(N) if tv(("XT", x, o, y))), -1) for o in (0, 1)] for x in range(N)]
    br = [0] * (2 * N); bp = [0] * (2 * N)
    for L in range(d):
        gt = lambda q, q2: tv(("GT", L, q, q2)) if q < q2 else not tv(("GT", L, q2, q))
        order = sorted(range(4), key=lambda q: sum(1 for q2 in range(4) if q2 != q and gt(q, q2)))   # increasing signed weight
        pos = [tv(("POS", L, q)) for q in range(4)]
        neg = [q for q in order if not pos[q]]; ps = [q for q in order if pos[q]]
        mags = list(reversed(neg)) + ps                    # increasing magnitude: negatives (least negative first), then positives
        for r, q in enumerate(mags): br[4 * L + q] = 4 * L + r; bp[4 * L + q] = 0 if pos[q] else 1
    ep = lambda q, q2: tv(("EP", q, q2)) if q < q2 else not tv(("EP", q2, q))
    e0 = [sum(1 for q2 in range(4) if q2 != q and ep(q2, q)) for q in range(4)]
    gate = [[e0[0], e0[1]], [e0[2], e0[3]]]
    for l in range(1, d):
        ga, gb = [0, 0], [0, 0]
        for u in (0, 1):
            ga[u], gb[u] = (1000 * l + 2 * u + 1, 1000 * l + 2 * u) if tv(("SW", l, u)) else (1000 * l + 2 * u, 1000 * l + 2 * u + 1)
        gate += [ga, gb]
    G = {"N": N, "lev": [x // 2 for x in range(N)], "deg": 2,
         "opts": [[[(2 * (x // 2 - 1) + o) if x >= 2 else -1, xt[x][o], 2 * x + o] for o in (0, 1)] for x in range(N)],
         "gate": gate, "br": br, "bp": bp, "start": [int(tv(("C", 0, x))) for x in range(N)]}
    return G, [[int(tv(("C", t, x))) for x in range(N)] for t in range(T + 1)]
if __name__ == "__main__":
    a = sys.argv[1:]; d, T, goal = int(a[0]), int(a[1]), a[2]
    mj = int(a[a.index("--maxjump") + 1]) if "--maxjump" in a else None
    fo = int(a[a.index("--fuelonly") + 1]) if "--fuelonly" in a else None
    ub = int(a[a.index("--upperbil") + 1]) if "--upperbil" in a else None
    dc = int(a[a.index("--dualcap") + 1]) if "--dualcap" in a else None
    ex = a[a.index("--extra") + 1].split(",") if "--extra" in a else ()
    lf = None
    if "--lift" in a:
        lf = json.load(open(a[a.index("--lift") + 1])); lf = lf.get("genome", lf)
        m_ = int(a[a.index("--mid") + 1]) if "--mid" in a else 0
        fr = [int(z) for z in a[a.index("--free") + 1].split(",")] if "--free" in a else []
        lf = (lf, m_, fr)
    t0 = time.time(); cnf, pool = build(d, T, goal, mj, fo, ub, dc, ex, lf, "--hered" in a)
    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as S:
        r = S.solve()
        print(f"UP107 d {d} T {T} goal {goal} maxjump {mj} fuelonly {fo}" + (f" upperbil {ub} dualcap {dc} extra {list(ex)}" if (ub is not None or dc is not None or ex) else "") + f" vars {pool.top} clauses {len(cnf.clauses)} answer {'SAT' if r else 'UNSAT'}" + ("" if "--notime" in a else f" time {time.time() - t0:.1f}s"), flush=True)
        if r and "--out" in a:
            G, states = decode(d, T, S.get_model(), pool)
            json.dump({"genome": G, "states": states, "d": d, "T": T, "goal": goal}, open(a[a.index("--out") + 1], "w"))
