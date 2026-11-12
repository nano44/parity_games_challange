#!/usr/bin/env python3
"""L-LOWER 16: kr2 = l15/kr.py + env EXT=core movers (e.g. 0-11) whose states (fixed by the TARGET rows) every helper and the client
may also read: a pair of rows differing on EXT satisfies the better-consistency and separation clauses at once. EXT movers are
fixed inputs below every helper (no cycle). EXT empty = kr.py exactly.
L-LOWER 15: relaxed KEY-ROOM question K (docs/lower/L15-keyroom.md §1). A private cascade of k pairs (helpers on levels 8..7+k,
two per level, Xi-edges only inside), driven by o(7)(S_t) = t mod 2; better_y = SOME function of the states of the movers before y in
a free total order (acyclic closure); movement R104 (M3), keys (M4) with free gate bits. Must SEPARATE the required-preference lists
of the given clients on rows 0..P (S_t != S_t' on the cascade whenever the client's required values differ).
UNSAT => no private cascade of k pairs serves these clients (sound relaxation). SAT is a relaxed model only (prints the trajectory).
Usage: kr.py GENOME(core gates) TARGET K P CLIENTS(e.g. 8,11) [CNF=path env writes DIMACS instead of solving]"""
import sys, os, subprocess, ast, time, hashlib
here = os.path.dirname(os.path.abspath(__file__))
gen, tp, K, P, CL = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), [int(c) for c in sys.argv[5].split(',')]
lists = {}
for x in CL:
    l = subprocess.run([sys.executable, os.path.join(here, '..', 'l13', 'reqpref.py'), gen, tp, str(x), str(P)], capture_output=True, text=True).stdout
    lists[x] = ast.literal_eval(l[l.index('['):l.index('] |') + 1])
EXT = []
for part in os.environ.get('EXT', '').split(','):
    if '-' in part: a_, b_ = map(int, part.split('-')); EXT += list(range(a_, b_ + 1))
    elif part: EXT.append(int(part))
TR = open(tp).read().split(); ROWS = [TR[2 + i] for i in range(P + 1)]
def extdiff(t, t2): return any(ROWS[t][e] != ROWS[t2][e] for e in EXT)
nv = [0]
def new(): nv[0] += 1; return nv[0]
cl = []
H = 2 * K; T = P
s = [[new() for y in range(H)] for t in range(T + 1)]
b = [[new() for y in range(H)] for t in range(T + 1)]
g = [[new(), new()] for i in range(K)]
TRUE = new(); cl.append([TRUE])
o = [[(TRUE if t % 2 else -TRUE)] + [new() for i in range(K)] for t in range(T + 1)]   # o[t][i] = o(7+i)(S_t)
def xor(a, c, z):  # z <-> a xor c
    cl.extend([[-z, a, c], [-z, -a, -c], [z, -a, c], [z, a, -c]])
def eq(a, c, z):   # z <-> (a == c)
    xor(a, c, -z)
for t in range(T + 1):
    for i in range(K):
        a, a2, op, on = s[t][2 * i], s[t][2 * i + 1], o[t][i], o[t][i + 1]
        sp = new(); xor(a, a2, sp)                     # split
        x1 = new(); xor(a, op, x1)
        cl.extend([[-sp, -on, x1], [-sp, on, -x1]])    # split: on = a xor o_prev
        for av, gv in ((0, g[i][0]), (1, g[i][1])):   # joined with a = av: on = gate bit
            lit = a if av else -a
            cl.extend([[sp, -lit, -on, gv], [sp, -lit, on, -gv]])
# movement
for t in range(T):
    for y in range(H):
        i = y // 2; c = o[t + 1][i]
        d1 = new(); xor(b[t][y], s[t][y], d1)        # av
        d2 = new(); xor(s[t][y], c, d2)              # free
        m = new(); cl.extend([[-m, d1], [-m, d2], [m, -d1, -d2]])
        xor(s[t][y], m, s[t + 1][y])
# order (strict total, transitive)
ordv = {}
for y in range(H):
    for z in range(H):
        if y < z: ordv[(y, z)] = new()
def before(z, y): return ordv[(z, y)] if z < y else -ordv[(y, z)]
for a1 in range(H):
    for a2 in range(H):
        for a3 in range(H):
            if len({a1, a2, a3}) == 3: cl.append([-before(a1, a2), -before(a2, a3), before(a1, a3)])
# consistency of better functions: b[t][y] != b[t'][y] -> exists z before y with s differing
for t in range(T + 1):
    for t2 in range(t + 1, T + 1):
        if extdiff(t, t2): continue
        dz = {}
        for z in range(H):
            v = new(); xor(s[t][z], s[t2][z], v); dz[z] = v
        for y in range(H):
            db = new(); xor(b[t][y], b[t2][y], db)
            ws = []
            for z in range(H):
                if z == y: continue
                w = new(); cl.extend([[-w, before(z, y)], [-w, dz[z]]]); ws.append(w)
            cl.append([-db] + ws)
        # separation (uses dz)
        for x in CL:
            pass
        dzs = dz
        for x in CL:
            Lx = dict(lists[x])
            if t in Lx and t2 in Lx and Lx[t] != Lx[t2]: cl.append([dzs[z] for z in range(H)])
info = {x: (len(lists[x]), sum(1 for k in range(1, len(lists[x])) if lists[x][k][1] != lists[x][k - 1][1])) for x in CL}
print('KR2 EXT', EXT, 'K', K, 'P', P, 'clients', CL, '(free pre-states, changes R)', info, 'vars', nv[0], 'clauses', len(cl), flush=True)
cnfp = os.environ.get('CNF')
if cnfp:
    with open(cnfp, 'w') as f:
        f.write(f'p cnf {nv[0]} {len(cl)}\n')
        for c in cl: f.write(' '.join(map(str, c)) + ' 0\n')
    print('CNF ->', cnfp, hashlib.sha1(open(cnfp, 'rb').read()).hexdigest()); sys.exit()
from pysat.solvers import Solver
sv = Solver(name='cadical195', bootstrap_with=cl); t0 = time.time(); r = sv.solve()
print(f'RESULT {"SAT" if r else "UNSAT"} {time.time() - t0:.1f}s', flush=True)
if r:
    M = set(l for l in sv.get_model() if l > 0)
    print('trajectory (rows 0..P, helper states, o(7..7+K)):')
    for t in range(T + 1): print(t, ''.join('1' if s[t][y] in M else '0' for y in range(H)), ''.join('1' if (o[t][i] in M if o[t][i] > 0 else -o[t][i] not in M) else '0' for i in range(K + 1)))
