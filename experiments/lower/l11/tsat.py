#!/usr/bin/env python3
"""L-LOWER 11 (BOX L11): exact SAT for a CLAMPED core target with free helper pairs (hsat.py's encoding, l8, generalised).
Core = pairs 0..h-1, states fixed to a target file (tight.py output: 'gate' line with 4h core gate values, then one state row per
step). Helpers = pairs h..d-1: any trajectory allowed by the R104 movement rule, any start; helper gates (levels h..d-2) are SAT
VARIABLES (joined value for a = 0, 1), so one instance covers every gate case of hsat.py. Unknowns as in hsat.py: wiring (one-hot
per option: exit or another mover), a strict order on movers (acyclic), helper states and keys, a strict total order on options
(ranks), signs. Per step t >= 1 and free mover x: the top-rank option of chain(x,0) xor chain(x,1) at s_(t-1) decides, s_t(x) = pref.
Sharing constraints (BOX L11): HR(x, y) = «x reaches helper y by a path whose inner movers are helpers»; client(j, y) = OR over the
two movers x of core pair j of HR(x, y). Mode 'disj': no helper is a client of two different core levels (each level owns its
helpers). Mode 'shared:J1,J2': every helper read by level J2 is also read by level J1 (one shared cascade). Mode 'none'.
Env PREFIX=T0: only rows 0..T0 of the target. Also 'noread:X:Y1+Y2' (mover X must not reach movers Y.. in the full wiring, any path).
CLI: tsat.py TARGET d MODE solver(g4|c195) tlimit_s OUTPREFIX  -> appends a result line to OUTPREFIX.res; UNSAT: CNF + proof
(Glucose4) written to OUTPREFIX.cnf / .proof; SAT: decoded genome (sim6-replayed) to OUTPREFIX.genome."""
import sys, os, itertools, time, threading
H = os.path.dirname(os.path.abspath(__file__))
for p in ('../l6', '../l7', '../l8'): sys.path.insert(0, os.path.join(H, p))
from sim6 import okeys, run, Fprof, caps, wr
from hsat import CNF, lit_true
def rdtarget(p):
    g = None; LS = []
    for ln in open(p):
        if ln.startswith('#'): continue
        w = ln.split()
        if not w: continue
        if w[0] == 'gate': g = list(map(int, w[1:])); continue
        LS.append(tuple(map(int, w)))
    return LS, g
def build(LS, cg, d, mode='none'):
    h = len(cg) // 4; N = 2 * d; M = 2 * N; T = len(LS) - 1
    gate = list(cg) + [v for l in range(h, d) for v in (4 * l + 1000, 4 * l + 1001, 4 * l + 1002, 4 * l + 1003)]
    c = CNF()
    JV = {l: (c.v(), c.v()) for l in range(h, d - 1)}   # joined value of helper level l for a = 0, a = 1
    E = {}
    for m in range(M):
        ys = [-1] + [y for y in range(N) if y != m // 2]; vs = []
        for y in ys: E[m, y] = c.v(); vs.append(E[m, y])
        c.add(vs)
        for a, b in itertools.combinations(vs, 2): c.add([-a, -b])
    P = {}
    for x in range(N):
        for y in range(N):
            if x < y: P[x, y] = c.v()
    def prec(x, y): return P[x, y] if x < y else -P[y, x]
    for x, y, z in itertools.permutations(range(N), 3): c.add([-prec(x, y), -prec(y, z), prec(x, z)])
    for m in range(M):
        for y in range(N):
            if y != m // 2: c.add([-E[m, y], prec(m // 2, y)])
    R = {}
    for i in range(M):
        for j in range(i + 1, M): R[i, j] = c.v()
    def above(i, j): return R[i, j] if i < j else -R[j, i]
    for i, j, k in itertools.permutations(range(M), 3): c.add([-above(i, j), -above(j, k), above(i, k)])
    SG = [c.v() for _ in range(M)]
    St = [[bool(LS[t][x]) if x < 2 * h else c.v() for x in range(N)] for t in range(T + 1)]
    def neg(a): return (not a) if isinstance(a, bool) else -a
    def neq(a, b):
        if isinstance(a, bool) and isinstance(b, bool): return a != b
        if isinstance(a, bool): return c.EQ(b, not a)
        return c.EQ(a, neg(b))
    def ite(cond, a, b):  # z = cond ? a : b (literals or bools)
        if isinstance(cond, bool): return a if cond else b
        z = c.v()
        for val, br in ((cond, a), (neg(cond), b)):
            if isinstance(br, bool): c.add([-val, z if br else -z])
            else: c.add([-val, -z, br]); c.add([-val, z, -br])
        return z
    K = [[None] * (d + 1) for _ in range(T + 1)]
    for t in range(T + 1):
        o = okeys({'d': h, 'gate': gate}, list(LS[t]))
        for l in range(1, h + 1): K[t][l] = bool(o[l - 1])
        for l in range(h, d - 1):
            a, b, cc = St[t][2 * l], St[t][2 * l + 1], K[t][l]
            ne = neq(a, b); anc = neq(a, cc); jz = ite(a, JV[l][1], JV[l][0])
            K[t][l + 1] = ite(ne, anc, jz)
    nconds = 0
    for t in range(1, T + 1):
        for x in range(N):
            l = x // 2; a, b = St[t - 1][x], St[t][x]
            if x >= 2 * h:
                cc = K[t][l]
                if isinstance(cc, bool):
                    if cc: c.add([-a, b])
                    else: c.add([-b, a])
                else: c.add([-b, a, cc]); c.add([b, -a, -cc])
                free = neq(a, cc)
            elif l == 0: free = gate[2 * x + 1 - LS[t - 1][x]] < gate[2 * x + LS[t - 1][x]]
            else: free = (LS[t - 1][x] != int(K[t][l]))
            if free is False: continue
            on = {}
            for k in (0, 1):
                ok = {m: False for m in range(M)}; ok[2 * x + k] = True; vis = {}
                for y in range(N):
                    if y != x: vis[y] = c.v()
                for y in range(N):
                    if y == x: continue
                    for j in (0, 1):
                        sy = St[t - 1][y]
                        sj = (sy == bool(j)) if isinstance(sy, bool) else (sy if j == 1 else -sy)
                        ok[2 * y + j] = c.AND(vis[y], sj)
                for y in range(N):
                    if y == x: continue
                    terms = []
                    for m in range(M):
                        if m // 2 == y or ok[m] is False: continue
                        tm = c.AND(ok[m], E[m, y])
                        if tm is False: continue
                        if tm is True: terms.append(True); continue
                        terms.append(tm); c.add([-tm, vis[y]])
                    if True in terms: c.add([vis[y]])
                    else: c.add([-vis[y]] + terms)
                on[k] = ok
            pref = c.v(); nconds += 1
            for m in range(M):
                o0, o1 = on[0][m], on[1][m]
                if o0 is False and o1 is False: continue
                dl = neq(o0, o1)
                if dl is False: continue
                fav = c.EQ(o1, SG[m]) if not isinstance(o1, bool) else (SG[m] if o1 else -SG[m])
                bt = c.v(); ws = []
                for m2 in range(M):
                    if m2 == m: continue
                    p0, p1 = on[0][m2], on[1][m2]
                    if p0 is False and p1 is False: continue
                    d2 = neq(p0, p1)
                    if d2 is False: continue
                    w = c.v(); ws.append(w)
                    if d2 is not True: c.add([-w, d2])
                    c.add([-w, above(m2, m)])
                c.add([-bt] + ws)
                e = c.EQ(pref, fav); cl = [bt, e]
                if dl is not True: cl = [-dl] + cl
                c.add(cl)
            e = c.EQ(pref, b)
            if free is True: lit_true(c, e)
            else: c.add([-free, e])
    # sharing constraints
    hel = list(range(2 * h, N))
    for md in mode.split(';'):
        if md in ('none', ''): continue
        if md == 'disj' or md.startswith('shared:'):
            HR = {(x, y): c.v() for x in range(N) for y in hel if x != y}
            for x in range(N):
                for y in hel:
                    if x == y: continue
                    for k in (0, 1):
                        m = 2 * x + k; c.add([-E[m, y], HR[x, y]])
                        for z in hel:
                            if z != x and z != y: c.add([-E[m, z], -HR[z, y], HR[x, y]])
            CL = {}
            for j in range(h):
                for y in hel:
                    v = c.v(); CL[j, y] = v; c.add([-HR[2 * j, y], v]); c.add([-HR[2 * j + 1, y], v])
                    c.add([-v, HR[2 * j, y], HR[2 * j + 1, y]])
            if md == 'disj':
                for y in hel:
                    for j1, j2 in itertools.combinations(range(h), 2): c.add([-CL[j1, y], -CL[j2, y]])
            else:
                j1, j2 = map(int, md.split(':')[1].split(','))
                for y in hel: c.add([-CL[j2, y], CL[j1, y]])
        elif md.startswith('noread:'):
            _, X, Ys = md.split(':'); X = int(X); Ys = list(map(int, Ys.split('+')))
            RR = {(u, y): c.v() for u in range(N) for y in Ys if u != y}
            for u in range(N):
                for y in Ys:
                    if u == y: continue
                    for k in (0, 1):
                        m = 2 * u + k; c.add([-E[m, y], RR[u, y]])
                        for z in range(N):
                            if z != u and z != y and (z, y) in RR: c.add([-E[m, z], -RR[z, y], RR[u, y]])
            for y in Ys:
                if (X, y) in RR: c.add([-RR[X, y]])
        else: raise SystemExit('bad mode ' + md)
    return dict(c=c, E=E, SG=SG, R=R, St=St, gate=gate, JV=JV, T=T, N=N, M=M, d=d, h=h, nconds=nconds)
def decode(model, B):
    val = set(l for l in model if l > 0); E, R, SG, St, N, M, T = B['E'], B['R'], B['SG'], B['St'], B['N'], B['M'], B['T']
    xt = [next(y for y in [-1] + list(range(N)) if (m, y) in E and E[m, y] in val) for m in range(M)]
    ab = lambda i, j: (R[i, j] in val) if i < j else not (R[j, i] in val)
    order = sorted(range(M), key=lambda i: -sum(ab(i, j) for j in range(M) if j != i))
    br = [0] * M
    for r, i in enumerate(order): br[i] = M - 1 - r
    bp = [0 if SG[m] in val else 1 for m in range(M)]
    gate = list(B['gate'])
    for l, (v0, v1) in B['JV'].items():
        b0, b1 = int(v0 in val), int(v1 in val)
        gate[4 * l + 0], gate[4 * l + 2] = (5, 3) if b0 else (3, 5)
        gate[4 * l + 1], gate[4 * l + 3] = (5, 3) if b1 else (3, 5)
    st = lambda v: int(v) if isinstance(v, bool) else int(v in val)
    S = [tuple(st(St[t][x]) for x in range(N)) for t in range(T + 1)]
    return {'d': B['d'], 'xt': xt, 'br': br, 'bp': bp, 'gate': gate, 'start': list(S[0])}, S
if __name__ == '__main__':
    tgt, d, mode, sv, tl, outp = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4], float(sys.argv[5]), sys.argv[6]
    LS, cg = rdtarget(tgt)
    if os.environ.get('PREFIX'): LS = LS[:int(os.environ['PREFIX']) + 1]
    t0 = time.time(); B = build(LS, cg, d, mode); c = B['c']
    print('target', tgt, 'h', B['h'], 'd', d, 'mode', mode, 'T', B['T'], 'vars', c.n, 'clauses', len(c.cl), f'build {time.time()-t0:.0f}s', flush=True)
    if sv == 'g4':
        from pysat.solvers import Glucose4; s = Glucose4(bootstrap_with=c.cl, with_proof=True)
    else:
        from pysat.solvers import Cadical195; s = Cadical195(bootstrap_with=c.cl)
    tm = threading.Timer(tl, s.interrupt); tm.start(); t1 = time.time(); r = s.solve_limited(expect_interrupt=True); tm.cancel(); dt = time.time() - t1
    st = 'SAT' if r is True else 'UNSAT' if r is False else 'TIMEOUT'
    line = f"{os.path.basename(tgt)} d {d} mode {mode} solver {sv} {st} {dt:.0f}s {time.strftime('%H:%MZ', time.gmtime())} vars {c.n} clauses {len(c.cl)}"
    print(line, flush=True)
    with open(outp + '.res', 'a') as f: f.write(line + '\n')
    if st == 'UNSAT' and sv == 'g4':
        with open(outp + '.cnf', 'w') as f:
            f.write(f'p cnf {c.n} {len(c.cl)}\n'); f.writelines(' '.join(map(str, cl)) + ' 0\n' for cl in c.cl)
        with open(outp + '.proof', 'w') as f: f.writelines(l + '\n' for l in s.get_proof())
    if st == 'SAT':
        D, S = decode(s.get_model(), B); S2, O2 = run(D); Fv = Fprof(D, O2) if S2 else None
        ok = S2 is not None and [x[:2 * B['h']] for x in S2] == [tuple(x) for x in LS]
        msg = f"replay sim6: T {len(S2) - 1 if S2 else None} F {Fv} caps {caps(Fv) if Fv else None} core = target {ok}"
        print(msg, flush=True); wr(D, outp + '.genome')
        with open(outp + '.res', 'a') as f: f.write(msg + '\n')
