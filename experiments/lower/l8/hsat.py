#!/usr/bin/env python3
"""L-LOWER 8 (BOX L8 item 1, Lead 23:48Z (b)): the sequential schedule with FREE helper pairs as one SAT instance (my own encoding).
Same question as hsched.py / hsched2.py (no ordering restriction): lower pairs 0..h-1 follow l7/sched.py's target (alpha given),
helper pairs h..d-1 follow any trajectory allowed by the R104 movement rule, any start bit; one gate pattern of the helper levels
h..d-2 per instance (2 bits per level: joined value for a = 0, 1); level 0 gates 0 2 1 3. Unknowns: wiring (one-hot target per
option, exit or another mover), a strict order on movers (every edge goes forward: acyclic), helper states, helper keys, a strict
total order on options (ranks) and signs. Constraint per step t >= 1 and mover x free at t (level 0: gate allows the switch; level >= 1:
s_(t-1)[x] != c_x(t), keys at the NEW state): the top-rank option of chain(x,0) △ chain(x,1) at s_(t-1) decides, and x's state at t
equals that preference (ENC; Δ always contains x's own two options, so it is never empty). Chains are unrolled exactly:
on(m) for x's own options; visit(y) <-> OR_m (on(m) & E[m][y]); on(2y + j) <-> visit(y) & (s_y = j) (well-founded since acyclic).
CLI: hsat.py h d alpha gatecase [proof_file]  -> SAT (prints the decoded genome; checked by sim6) or UNSAT (optionally a DRUP proof)."""
import sys, os, itertools, time
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..', 'l6')); sys.path.insert(0, os.path.join(H, '..', 'l7'))
from sim6 import okeys, run, Fprof, caps
from sched import schedule
from pysat.solvers import Cadical153
class CNF:
    def __init__(s): s.n = 0; s.cl = []
    def v(s): s.n += 1; return s.n
    def add(s, c): s.cl.append(c)
    def AND(s, a, b):
        if a is True: return b
        if b is True: return a
        if a is False or b is False: return False
        z = s.v(); s.add([-z, a]); s.add([-z, b]); s.add([z, -a, -b]); return z
    def EQ(s, a, b):  # a <-> b, literals or bools
        if isinstance(a, bool): a, b = b, a
        if isinstance(b, bool):
            if isinstance(a, bool): return a == b
            return a if b else -a
        z = s.v(); s.add([-z, -a, b]); s.add([-z, a, -b]); s.add([z, a, b]); s.add([z, -a, -b]); return z
def lit_true(c, a):
    if a is True: return
    if a is False: c.add([]); return
    c.add([a])
def build(h, d, al, gp):
    N = 2 * d; M = 2 * N; _, LS = schedule(h, alpha=al); LS = [tuple(s[:2 * h]) for s in LS]; T = len(LS) - 1
    gate = [0, 2, 1, 3] + [v for l in range(1, d) for v in (4 * l + 1000, 4 * l + 1001, 4 * l + 1002, 4 * l + 1003)]
    jv = {}
    for i, l in enumerate(range(h, d - 1)):
        b0, b1 = gp[i] & 1, gp[i] >> 1; jv[l] = (b0, b1)
        gate[4 * l + 0], gate[4 * l + 2] = (5, 3) if b0 else (3, 5)
        gate[4 * l + 1], gate[4 * l + 3] = (5, 3) if b1 else (3, 5)
    c = CNF()
    # wiring
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
    # ranks (strict total order on options) and signs
    R = {}
    for i in range(M):
        for j in range(i + 1, M): R[i, j] = c.v()
    def above(i, j): return R[i, j] if i < j else -R[j, i]
    for i, j, k in itertools.permutations(range(M), 3): c.add([-above(i, j), -above(j, k), above(i, k)])
    SG = [c.v() for _ in range(M)]   # true = positive
    # states
    St = [[None] * N for _ in range(T + 1)]
    for t in range(T + 1):
        for x in range(N):
            St[t][x] = bool(LS[t][x]) if x < 2 * h else (c.v())
    # keys: K[t][l] = c_l(t) = o(l-1) at state t, for l >= 1. Lower levels from LS (constants).
    K = [[None] * (d + 1) for _ in range(T + 1)]
    for t in range(T + 1):
        o = okeys({'d': h, 'gate': gate}, list(LS[t]))
        for l in range(1, h + 1): K[t][l] = bool(o[l - 1])
        for l in range(h, d):               # o(l) for helper level l -> K[t][l+1]
            a, b, cc = St[t][2 * l], St[t][2 * l + 1], K[t][l]
            if l == d - 1: break
            z = c.v(); b0, b1 = jv[l]
            # z = (a != b) ? (a != cc) : (a ? b1 : b0)
            ne = c.EQ(a, -b if not isinstance(b, bool) else (not b))   # a != b
            anc = c.EQ(a, -cc if not isinstance(cc, bool) else (not cc))
            # ne -> z == anc ; !ne -> z == joined(a)
            jz = (a if (b0 == 0 and b1 == 1) else (-a if (b0 == 1 and b1 == 0) else (b1 == 1)))
            for zz, cond in ((anc, ne), (jz, -ne if not isinstance(ne, bool) else (not ne))):
                e = c.EQ(z, zz)
                if isinstance(cond, bool):
                    if cond: lit_true(c, e)
                else:
                    if e is True: pass
                    elif e is False: c.add([-cond])
                    else: c.add([-cond, e])
            K[t][l + 1] = z
    # movement rule for helpers and freedom
    def neq(a, b):
        if isinstance(a, bool) and isinstance(b, bool): return a != b
        return c.EQ(a, -b if not isinstance(b, bool) else (not b)) if not isinstance(a, bool) else c.EQ(b, not a)
    nconds = 0
    for t in range(1, T + 1):
        for x in range(N):
            l = x // 2; a, b = St[t - 1][x], St[t][x]
            if x >= 2 * h:   # b in {a, c}
                cc = K[t][l]
                if isinstance(cc, bool):      # constant key: b in {a, cc}
                    if cc: c.add([-a, b])         # a = 1 -> b = 1
                    else: c.add([-b, a])          # b = 1 -> a = 1
                else:
                    c.add([-b, a, cc]); c.add([b, -a, -cc])
                free = neq(a, cc)
            elif l == 0: free = gate[2 * x + 1 - LS[t - 1][x]] < gate[2 * x + LS[t - 1][x]]
            else: free = (LS[t - 1][x] != int(K[t][l]))
            if free is False: continue
            # chains at pre-state t-1
            on = {}
            for k in (0, 1):
                ok = {m: False for m in range(M)}; ok[2 * x + k] = True
                vis = {}
                # visit(y) <-> OR_m on(m) & E[m][y]; on(2y+j) <-> visit(y) & s_y == j  (y != x)
                for y in range(N):
                    if y == x: continue
                    vis[y] = c.v()
                for y in range(N):
                    if y == x: continue
                    for j in (0, 1):
                        sy = St[t - 1][y]; sj = (sy if j == 1 else (-sy if not isinstance(sy, bool) else (not sy))) if not isinstance(sy, bool) else (sy == bool(j))
                        ok[2 * y + j] = c.AND(vis[y], sj)
                for y in range(N):
                    if y == x: continue
                    terms = []
                    for m in range(M):
                        if m // 2 == y: continue
                        tm = c.AND(ok[m], E[m, y]) if ok[m] is not False else False
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
                # favor1(m) = on1(m) <-> sign positive
                fav = c.EQ(o1, SG[m]) if not isinstance(o1, bool) else (SG[m] if o1 else -SG[m])
                # beaten(m): some m' in Δ above m. w(m,m') -> dl(m') & above(m', m); beaten -> OR w
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
                # dl & !bt -> pref == fav
                e = c.EQ(pref, fav)
                cl = [bt, e]
                if dl is not True: cl = [-dl] + cl
                c.add(cl)
            # state at t equals pref (free)
            e = c.EQ(pref, b)
            if free is True: lit_true(c, e)
            else: c.add([-free, e])
    return c, E, SG, R, St, gate, T, N, M, LS, nconds
def decode(model, E, SG, R, St, gate, T, N, M, d):
    val = set(l for l in model if l > 0)
    xt = [next(y for y in [-1] + list(range(N)) if (m, y) in E and E[m, y] in val) for m in range(M)]
    above = lambda i, j: (R[i, j] in val) if i < j else not (R[j, i] in val)
    order = sorted(range(M), key=lambda i: -sum(above(i, j) for j in range(M) if j != i))
    br = [0] * M
    for r, i in enumerate(order): br[i] = M - 1 - r
    bp = [0 if SG[m] in val else 1 for m in range(M)]
    st = lambda v: v if isinstance(v, bool) else (v in val)
    S = [tuple(int(st(St[t][x])) for x in range(N)) for t in range(T + 1)]
    return {'d': d, 'xt': xt, 'br': br, 'bp': bp, 'gate': gate, 'start': list(S[0])}, S
if __name__ == '__main__':
    h, d = int(sys.argv[1]), int(sys.argv[2]); al = list(map(int, sys.argv[3].split(','))); gp = tuple(map(int, sys.argv[4].split(','))) if len(sys.argv) > 4 and sys.argv[4] != '-' else ()
    proof = sys.argv[5] if len(sys.argv) > 5 else None
    t0 = time.time(); c, E, SG, R, St, gate, T, N, M, LS, nc = build(h, d, al, gp)
    print('h', h, 'd', d, 'alpha', al, 'gate case', gp, 'T', T, 'vars', c.n, 'clauses', len(c.cl), 'conditions', nc, f'build {time.time() - t0:.1f}s', flush=True)
    if proof:
        with open(proof.replace('.proof', '.cnf'), 'w') as f:
            f.write(f'p cnf {c.n} {len(c.cl)}\n'); f.writelines(' '.join(map(str, cl)) + ' 0\n' for cl in c.cl)
    s = Cadical153(bootstrap_with=c.cl, with_proof=bool(proof)); r = s.solve()
    print('RESULT', 'SAT' if r else 'UNSAT', f'{time.time() - t0:.1f}s', flush=True)
    if r:
        D, S = decode(s.get_model(), E, SG, R, St, gate, T, N, M, d); S2, O2 = run(D); F = Fprof(D, O2)
        print('decoded genome: sim6 T', len(S2) - 1, 'F', F, 'caps', caps(F), 'prefix = target', S2[:len(S)] == S)
        for k in ('d', 'xt', 'br', 'bp', 'gate', 'start'): print('GENOME', k, D[k] if k == 'd' else ' '.join(map(str, D[k])))
    elif proof:
        with open(proof, 'w') as f: f.writelines(l + '\n' for l in s.get_proof())
        print('proof lines', len(s.get_proof()))
