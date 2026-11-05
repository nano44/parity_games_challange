#!/usr/bin/env python3
"""L-COMP box 27: my own CNF encoding of "some genome + start has a run with T >= L" in the IDEAL model of RESULTS R104 (written
from R104's text; no other lane's encoder used). Degree-2 movers: exactly two per level (u_l = 2l, v_l = 2l+1); optional degree-1
padding movers (any number per level, P="p0,p1,..."); W-targets: R197 wiring (W=R: option k of a level-l >= 1 mover W-points to
mover 2(l-1)+k) or free (W=free: every option of a level-l >= 1 mover, padding included, picks any mover of level l-1).
Xi: every option picks a Xi-target (exit or any mover), acyclic (a strict mover order pi, target later than owner); ranks = a strict
total order on all options; parities free. Comparison = R104's literal rule: the largest-rank beta of the symmetric difference of
the two chains decides (set containing it is better iff even). Keys: lexicographic over W-chains, lowest level first, which for two
movers y, y' of one level reads: different W-targets -> compare the targets; same target -> compare the two gates (gates are
compared only inside a level, as a strict total order per level).
Step t -> t+1: B_t(x) = the other option is strictly better at s_t; s_(t+1)(x) = KP_(t+1)(x) if B_t(x) else s_t(x), KP under the
keys of s_(t+1). T >= L  <=>  s_(t+1) != s_t for t = 0..L-1.
Extra env: FREE0=1 KF=k ISO=1 (level 0 external, b_0 flips <= k, each step moves a level >= 1 mover; T counts those steps)."""
import os, sys, json, itertools, time
from pysat.solvers import Solver
from pysat.card import CardEnc, EncType

class CNF:
    def __init__(s): s.n = 0; s.cl = []
    def var(s): s.n += 1; return s.n
    def add(s, c): s.cl.append(c)
    def AND(s, ls):
        ls = [l for l in ls if l is not True]
        if any(l is False for l in ls): return False
        if not ls: return True
        if len(ls) == 1: return ls[0]
        v = s.var()
        for l in ls: s.add([-v, l])
        s.add([v] + [-l for l in ls]); return v
    def OR(s, ls):
        ls = [l for l in ls if l is not False]
        if any(l is True for l in ls): return True
        if not ls: return False
        if len(ls) == 1: return ls[0]
        v = s.var()
        for l in ls: s.add([v, -l])
        s.add([-v] + ls); return v
    def NOT(s, a): return (not a) if isinstance(a, bool) else -a
    def XOR(s, a, b):
        if isinstance(a, bool): return s.NOT(b) if a else b
        if isinstance(b, bool): return s.NOT(a) if b else a
        v = s.var(); s.add([-v, a, b]); s.add([-v, -a, -b]); s.add([v, -a, b]); s.add([v, a, -b]); return v
    def ITE(s, c, a, b): return s.OR([s.AND([c, a]), s.AND([s.NOT(c), b])])
    def EQ(s, a, b): return s.NOT(s.XOR(a, b))
    def require(s, a):
        if a is True: return
        if a is False: s.add([]); return
        s.add([a])

def order_vars(C, items):
    """strict total order: lt(a,b) literal for a != b, transitive."""
    V = {}
    for i, a in enumerate(items):
        for b in items[i + 1:]:
            v = C.var(); V[(a, b)] = v; V[(b, a)] = -v
    for a, b, c in itertools.permutations(items, 3):
        C.add([-V[(a, b)], -V[(b, c)], V[(a, c)]])
    return V

def build(d, L, P=None, wiring="R"):
    C = CNF(); P = P or [0] * d
    free0 = os.environ.get("FREE0") == "1"; iso = os.environ.get("ISO") == "1" or free0
    movers = []; lev = {}; deg = {}
    for l in range(d):
        for j in range(2): x = 2 * l + j; movers.append(x); lev[x] = l; deg[x] = 2
    nid = 2 * d
    for l in range(d):
        for j in range(P[l]): movers.append(nid); lev[nid] = l; deg[nid] = 1; nid += 1
    opts = [(x, k) for x in movers for k in range(deg[x])]
    atlev = {l: [x for x in movers if lev[x] == l] for l in range(d)}
    # W-targets: Wv[(x,k)][w] literal (or bool)
    Wv = {}
    for (x, k) in opts:
        if lev[x] == 0: Wv[(x, k)] = {}; continue
        cand = atlev[lev[x] - 1]
        if wiring == "R" and deg[x] == 2: Wv[(x, k)] = {w: (w == 2 * (lev[x] - 1) + k) for w in cand}
        else:
            vs = {w: C.var() for w in cand}; C.add(list(vs.values()))
            for a, b in itertools.combinations(cand, 2): C.add([-vs[a], -vs[b]])
            Wv[(x, k)] = vs
    # Xi-targets and acyclicity
    pi = order_vars(C, movers)
    Xv = {}
    for (x, k) in opts:
        cand = [y for y in movers if y != x and not (iso and lev[y] == 0)]
        vs = {y: C.var() for y in cand}; vs[-1] = C.var()
        C.add(list(vs.values()))
        for a, b in itertools.combinations(list(vs), 2): C.add([-vs[a], -vs[b]])
        for y in cand: C.add([-vs[y], pi[(x, y)]])
        Xv[(x, k)] = vs
    rk = order_vars(C, opts)
    par = {o: C.var() for o in opts}
    gord = {l: order_vars(C, [o for o in opts if lev[o[0]] == l]) for l in range(d)}
    # states: S[t][x] = literal "option 1" (degree-2 movers); padding movers have option 0
    S = [{x: (C.var() if deg[x] == 2 else False) for x in movers} for _ in range(L + 1)]
    def st(t, x, k): a = S[t][x]; return a if k == 1 else C.NOT(a)
    def chains(t):
        """cm[(x,k)][o]: option o lies on the chain of option (x,k) under S[t]; mem[y][o]: on the chain of y's current option."""
        mem = {}; cm = {}
        # process movers in a fixed arbitrary order with memo; recursion through Xi-targets is guarded by acyclicity only
        # semantically, so build by "depth" iteration: chain length <= #movers
        # level-by-length: cm_h = chain restricted to the first h hops
        nM = len(movers)
        cmh = {(x, k): {o: (o == (x, k)) for o in opts} for (x, k) in opts}
        for h in range(nM):
            memh = {y: {o: C.OR([C.AND([st(t, y, k), cmh[(y, k)][o]]) for k in range(deg[y])]) for o in opts} for y in movers}
            cmh = {(x, k): {o: C.OR([o == (x, k)] + [C.AND([Xv[(x, k)][y], memh[y][o]]) for y in Xv[(x, k)] if y != -1])
                            for o in opts} for (x, k) in opts}
        return cmh
    def better1(t, x, cm):
        """option 1 of x strictly better than option 0 at S[t]."""
        A, B = cm[(x, 0)], cm[(x, 1)]
        Dl = {o: C.XOR(A[o], B[o]) for o in opts}
        terms = []
        for o in opts:
            if Dl[o] is False: continue
            dec = C.AND([Dl[o]] + [C.OR([C.NOT(Dl[o2]), rk[(o2, o)]]) for o2 in opts if o2 != o and Dl[o2] is not False])
            terms.append(C.AND([dec, C.XOR(B[o], par[o])]))
        return C.OR(terms)
    def keys_lt(t):
        """lt[(y,y')] literal: key(y) < key(y') under S[t], for movers of one level (levels 0..d-2)."""
        lt = {}
        for l in range(d - 1):
            for y, y2 in itertools.permutations(atlev[l], 2):
                terms = []
                for k in range(deg[y]):
                    for k2 in range(deg[y2]):
                        sel = C.AND([st(t, y, k), st(t, y2, k2)])
                        if sel is False: continue
                        if l == 0: cmpv = gord[0][((y, k), (y2, k2))]
                        else:
                            parts = []
                            for w, a in Wv[(y, k)].items():
                                for w2, b in Wv[(y2, k2)].items():
                                    ab = C.AND([a, b])
                                    if ab is False: continue
                                    parts.append(C.AND([ab, lt[(w, w2)] if w != w2 else gord[l][((y, k), (y2, k2))]]))
                            cmpv = C.OR(parts)
                        terms.append(C.AND([sel, cmpv]))
                lt[(y, y2)] = C.OR(terms)
        return lt
    def kp1(t, x, lt):
        """key(x,1) < key(x,0) under S[t] (degree-2 x)."""
        if lev[x] == 0: return gord[0][((x, 1), (x, 0))]
        parts = []
        for w0, a in Wv[(x, 0)].items():
            for w1, b in Wv[(x, 1)].items():
                ab = C.AND([a, b])
                if ab is False: continue
                parts.append(C.AND([ab, lt[(w1, w0)] if w0 != w1 else gord[lev[x]][((x, 1), (x, 0))]]))
        return C.OR(parts)
    D2 = [x for x in movers if deg[x] == 2]
    upper = [x for x in D2 if not (free0 and lev[x] == 0)]
    MV = []
    for t in range(L):
        cm = chains(t); lt = keys_lt(t + 1); mv = []
        for x in upper:
            Bx = C.XOR(better1(t, x, cm), S[t][x])           # other option strictly better
            nx = C.ITE(Bx, kp1(t + 1, x, lt), S[t][x])
            C.require(C.EQ(S[t + 1][x], nx)); mv.append(C.XOR(S[t + 1][x], S[t][x]))
        C.require(C.OR(mv)); MV.append(mv)
    if free0:   # b_0 = [key(u_0) < key(v_0)] at s_t; at most KF changes over s_0..s_L
        def b0(t):
            return C.OR([C.AND([st(t, 0, a), st(t, 1, b), gord[0][((0, a), (1, b))]]) for a in range(2) for b in range(2)])
        B = [b0(t) for t in range(L + 1)]
        fl = [C.XOR(B[t], B[t + 1]) for t in range(L)]
        fl = [f for f in fl if f is not False]
        kf = int(os.environ.get("KF", "0"))
        if kf < len(fl):
            enc = CardEnc.atmost(lits=fl, bound=kf, top_id=C.n, encoding=EncType.seqcounter)
            C.n = max(C.n, enc.nv); C.cl.extend(enc.clauses)
    if os.environ.get("SYM") == "1":   # sound relabelling: the two options of a level-0 mover have no W-role, so swapping their
        for x in (0, 1):                   # labels (with Xi-target, rank, parity, gate) is a symmetry; WLOG s_0(u_0) = s_0(v_0) = 0
            if not (free0 and lev[x] == 0): C.require(C.NOT(S[0][x]))
    for a in [a for a in os.environ.get("CUBE", "").split(",") if a]:   # CUBE=x:b,... fixes start bits s_0(x) = b
        x, b = (int(v) for v in a.split(":")); C.require(S[0][x] if b else C.NOT(S[0][x]))
    for a in [a for a in os.environ.get("XCUBE", "").split(",") if a]:   # XCUBE=j:c,...: option j (in opts order) takes the
        j, c = (int(v) for v in a.split(":")); o = opts[j]               # c-th value of its sorted Xi-target domain
        C.require(Xv[o][sorted(Xv[o].keys())[c]])
    info = dict(d=d, L=L, movers=movers, lev=lev, deg=deg, opts=opts, Wv=Wv, Xv=Xv, rk=rk, par=par, gord=gord, S=S, pi=pi)
    return C, info

def val(model, l):
    if isinstance(l, bool): return l
    return (l > 0) == (model[abs(l) - 1] > 0)

def decode(model, I):
    movers, lev, deg, opts = I["movers"], I["lev"], I["deg"], I["opts"]
    idx = {x: i for i, x in enumerate(movers)}
    oid = {o: i for i, o in enumerate(opts)}
    rank = {o: sum(1 for o2 in opts if o2 != o and val(model, I["rk"][(o2, o)])) for o in opts}
    G = {"N": len(movers), "lev": [lev[x] for x in movers], "opts": [], "gate": [], "br": [rank[o] for o in opts],
         "bp": [int(val(model, I["par"][o])) for o in opts]}
    for x in movers:
        ox, gx = [], []
        for k in range(deg[x]):
            o = (x, k)
            w = -1 if lev[x] == 0 else idx[[w for w, a in I["Wv"][o].items() if val(model, a)][0]]
            y = [y for y, a in I["Xv"][o].items() if val(model, a)][0]
            ox.append([w, -1 if y == -1 else idx[y], oid[o]])
            l = lev[x]; same = [o2 for o2 in opts if lev[o2[0]] == l]
            gx.append(100 * l + sum(1 for o2 in same if o2 != o and val(model, I["gord"][l][(o2, o)])))
        G["opts"].append(ox); G["gate"].append(gx)
    G["states"] = [[int(val(model, I["S"][t][x])) for x in movers] for t in range(I["L"] + 1)]
    G["start"] = G["states"][0]
    return G

if __name__ == "__main__":
    d, L, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    P = [int(v) for v in os.environ.get("P", "").split(",")] if os.environ.get("P") else None
    wiring = os.environ.get("W", "R")
    t0 = time.time(); C, I = build(d, L, P, wiring)
    print(f"build d {d} L {L} P {P} W {wiring} SYM {os.environ.get('SYM')} CUBE {os.environ.get('CUBE')} XCUBE {os.environ.get('XCUBE')} FREE0 {os.environ.get('FREE0')} KF {os.environ.get('KF')} vars {C.n} clauses {len(C.cl)} {time.time() - t0:.1f} s", flush=True)
    s = Solver(name=os.environ.get("SOLVER", "cadical195"), bootstrap_with=C.cl)
    t1 = time.time(); r = s.solve()
    print(f"RESULT d {d} T >= {L} P {P} W {wiring}: {'SAT' if r else 'UNSAT'} {time.time() - t1:.1f} s", flush=True)
    if r:
        G = decode(s.get_model(), I); json.dump(G, open(out, "w")); print("model ->", out, flush=True)
