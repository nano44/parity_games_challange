#!/usr/bin/env python3
"""L-LOWER 15: EXACT KEY-ROOM question (docs/lower/L15-keyroom.md): a private cascade of k pairs (helpers on levels 8..7+k, two per
level) with REAL degree-2 wiring (each option's Xi-target is exit or a helper before it in a free total order: acyclic), distinct ranks
(a free total order on the 4k options) and parities, gate bits, starts; better_y(S) by ENC (R105): the top-ranked option of the
symmetric difference of the two chains decides, toward its side if its parity is even, away if odd. Movement (M3), keys (M4),
o(7)(S_t) = t mod 2. Must separate the clients' lists on rows 0..P. SAT -> decoded cascade written to OUT (then replay with sim15.py).
Usage: ekr.py GENOME TARGET K P CLIENTS OUT"""
import sys, os, subprocess, ast, time
here = os.path.dirname(os.path.abspath(__file__))
gen, tp, K, P, CL, outp = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), [int(c) for c in sys.argv[5].split(',')], sys.argv[6]
lists = {}
for x in CL:
    l = subprocess.run([sys.executable, os.path.join(here, '..', 'l13', 'reqpref.py'), gen, tp, str(x), str(P)], capture_output=True, text=True).stdout
    lists[x] = dict(ast.literal_eval(l[l.index('['):l.index('] |') + 1]))
nv = [0]
def new(): nv[0] += 1; return nv[0]
cl = []
H = 2 * K; NO = 2 * H; T = P
TRUE = new(); cl.append([TRUE])
def xor(a, c, z): cl.extend([[-z, a, c], [-z, -a, -c], [z, -a, c], [z, a, -c]])
def AND(lits):
    z = new()
    for l in lits: cl.append([-z, l])
    cl.append([z] + [-l for l in lits]); return z
def OR(lits):
    z = new()
    for l in lits: cl.append([z, -l])
    cl.append([-z] + list(lits)); return z
s = [[new() for y in range(H)] for t in range(T + 1)]
g = [[new(), new()] for i in range(K)]
o = [[(TRUE if t % 2 else -TRUE)] + [new() for i in range(K)] for t in range(T + 1)]
# mover order (acyclicity) and wiring
ordv = {}
for y in range(H):
    for z in range(y + 1, H): ordv[(y, z)] = new()
def before(z, y): return ordv[(z, y)] if z < y else -ordv[(y, z)]
for a1 in range(H):
    for a2 in range(H):
        for a3 in range(H):
            if len({a1, a2, a3}) == 3: cl.append([-before(a1, a2), -before(a2, a3), before(a1, a3)])
W = {}   # W[(op, z)]: option op = 2y+k points to mover z; at most one; none = exit
for op in range(NO):
    y = op // 2
    for z in range(H):
        if z != y: W[(op, z)] = new(); cl.append([-W[(op, z)], before(z, y)])
    zs = [W[(op, z)] for z in range(H) if z != y]
    for i in range(len(zs)):
        for j in range(i + 1, len(zs)): cl.append([-zs[i], -zs[j]])
# option ranks (strict total order) and parities
rk = {}
for a in range(NO):
    for b in range(a + 1, NO): rk[(a, b)] = new()
def higher(a, b): return rk[(a, b)] if a < b else -rk[(b, a)]   # a ranked above b
for a in range(NO):
    for b in range(NO):
        for c in range(NO):
            if len({a, b, c}) == 3: cl.append([-higher(a, b), -higher(b, c), higher(a, c)])
par = [new() for op in range(NO)]   # True = even (good)
# per row: chain membership cur[z][o] (current chain of mover z), m[op][o] (chain of option op)
bet = [[None] * H for t in range(T + 1)]
for t in range(T + 1):
    m = [[None] * NO for _ in range(NO)]; cur = [[None] * NO for _ in range(H)]
    # chains defined recursively; acyclic by order, so define via fixed point over "depth": encode m[op][o] <-> (o == op) or OR_z (W(op,z) and cur[z][o])
    for op in range(NO):
        for oo in range(NO): m[op][oo] = new()
    for z in range(H):
        for oo in range(NO):
            c = new(); a0, a1 = m[2 * z][oo], m[2 * z + 1][oo]; sz = s[t][z]
            cl.extend([[sz, -c, a0], [sz, c, -a0], [-sz, -c, a1], [-sz, c, -a1]]); cur[z][oo] = c
    for op in range(NO):
        y = op // 2
        for oo in range(NO):
            if oo == op: cl.append([m[op][oo]]); continue
            terms = [AND([W[(op, z)], cur[z][oo]]) for z in range(H) if z != y]
            r = OR(terms); cl.extend([[-m[op][oo], r], [m[op][oo], -r]])
    for y in range(H):
        A, B = 2 * y, 2 * y + 1
        d = []
        for oo in range(NO):
            v = new(); xor(m[A][oo], m[B][oo], v); d.append(v)
        tops = []
        for oo in range(NO):
            tp_ = new(); cl.append([-tp_, d[oo]])
            for o2 in range(NO):
                if o2 != oo: cl.append([-tp_, -d[o2], higher(oo, o2)])
            cl.append([tp_, -d[oo]] + [AND([d[o2], higher(o2, oo)]) for o2 in range(NO) if o2 != oo]); tops.append(tp_)
        # better = 1 iff top in B and even, or top in A and odd
        wins = [AND([tops[oo], m[B][oo], par[oo]]) for oo in range(NO)] + [AND([tops[oo], m[A][oo], -par[oo]]) for oo in range(NO)]
        bet[t][y] = OR(wins)
for t in range(T + 1):
    for i in range(K):
        a, a2, op_, on = s[t][2 * i], s[t][2 * i + 1], o[t][i], o[t][i + 1]
        sp = new(); xor(a, a2, sp); x1 = new(); xor(a, op_, x1)
        cl.extend([[-sp, -on, x1], [-sp, on, -x1]])
        for av, gv in ((0, g[i][0]), (1, g[i][1])):
            lit = a if av else -a; cl.extend([[sp, -lit, -on, gv], [sp, -lit, on, -gv]])
for t in range(T):
    for y in range(H):
        c = o[t + 1][y // 2]
        d1 = new(); xor(bet[t][y], s[t][y], d1); d2 = new(); xor(s[t][y], c, d2)
        mm = new(); cl.extend([[-mm, d1], [-mm, d2], [mm, -d1, -d2]]); xor(s[t][y], mm, s[t + 1][y])
for t in range(T + 1):
    for t2 in range(t + 1, T + 1):
        need = any(t in lists[x] and t2 in lists[x] and lists[x][t] != lists[x][t2] for x in CL)
        if not need: continue
        dz = []
        for z in range(H):
            v = new(); xor(s[t][z], s[t2][z], v); dz.append(v)
        cl.append(dz)
print('EKR K', K, 'P', P, 'clients', CL, 'vars', nv[0], 'clauses', len(cl), flush=True)
from pysat.solvers import Solver
sv = Solver(name='cadical195', bootstrap_with=cl); t0 = time.time(); r = sv.solve()
print(f'RESULT {"SAT" if r else "UNSAT"} {time.time() - t0:.1f}s', flush=True)
if r:
    M = set(l for l in sv.get_model() if l > 0); val = lambda v: (v in M) if v > 0 else (-v not in M)
    xt = []
    for op in range(NO):
        tg = [z for z in range(H) if z != op // 2 and val(W[(op, z)])]; xt.append(tg[0] if tg else -1)
    order = sorted(range(NO), key=lambda a: sum(1 for b in range(NO) if b != a and val(higher(a, b))))  # ascending rank
    rank = [0] * NO
    for i, a in enumerate(order): rank[a] = i
    with open(outp, 'w') as f:
        f.write('k %d\nxt %s\nrank %s\neven %s\ngate %s\nstart %s\n' % (K, ' '.join(map(str, xt)), ' '.join(map(str, rank)),
                ' '.join('1' if val(par[a]) else '0' for a in range(NO)), ' '.join('1' if val(g[i][a]) else '0' for i in range(K) for a in (0, 1)),
                ''.join('1' if val(s[0][y]) else '0' for y in range(H))))
    print('decoded ->', outp)
    for t in range(T + 1): print(t, ''.join('1' if val(s[t][y]) else '0' for y in range(H)))
