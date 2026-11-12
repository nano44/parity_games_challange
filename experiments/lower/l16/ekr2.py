#!/usr/bin/env python3
"""L-LOWER 16: ekr2 = l15/ekr.py (EXACT private cascade: degree-2 wiring, option ranks, parities, ENC, movement M3, keys M4,
o(7)(S_t) = t mod 2) + EXTERNAL inputs. Cascade options and the CLIENT's two options may also point to EXT movers (core movers of the
base genome). The chain of an EXT mover e at row t is the FIXED option set chain(e, S_t) of the base genome's clamped run (core
forced to TARGET, l7/clamp), with the base's ranks and signs; cascade / client options get free ranks (a total order over cascade +
client + fixed options, the fixed ones kept in base order). The CLIENT x is modelled exactly too: its options point to cascade
movers, EXT movers or exit; better_x by ENC must equal x's required value at each free pre-state t <= P (not mere separation).
EXT movers must not reach x in the base (asserted). SAT -> decoded design (OUT); UNSAT -> no such cascade (scope above).
env LEVEL=L (default 8): the cascade sits on levels L..L+K-1 (movers 2L..), its clock is the base's o(L-1) on the clamped run;
EXT movers must not reach those slots. env KEEPR=1: every mover whose base chain (at some row < P) enters the client or a cascade slot keeps its base better value
on rows 0..P-1 (its chain = the fixed base prefix + the design's chain from the hook); sufficient for an unchanged run elsewhere.
env KEEPO=1: o(7+K) of the cascade must equal the base genome's o(7+K) on the clamped run (keys above the graft unchanged).
env CNF=path: write DIMACS instead of solving (for edrup.py).
Usage: ekr2.py GENOME TARGET K P CLIENT EXT(e.g. 0-11) OUT [TLIM]"""
import sys, os, subprocess, ast, time
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(here, '..', 'l6')); sys.path.insert(0, os.path.join(here, '..', 'l7'))
import sim6, clamp
gen, tp, K, P, X, outp = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[7]
TL = float(sys.argv[8]) if len(sys.argv) > 8 else 2900
EXT = []
for part in sys.argv[6].split(','):
    if '-' in part: a_, b_ = map(int, part.split('-')); EXT += list(range(a_, b_ + 1))
    elif part: EXT.append(int(part))
D = sim6.rd(gen); xt0 = D['xt']
TR = open(tp).read().split(); tg = [[int(c) for c in TR[2 + i]] for i in range(P + 1)]
tgt = [r + (D['start'][16:] if t == 0 else [0] * 48) for t, r in enumerate(tg)]
SB = clamp.runclamp(D, tgt, set(range(16)))
def reach(b):
    out = {b}; st = [b]
    while st:
        y = st.pop()
        for k in (0, 1):
            z = xt0[2 * y + k]
            if z >= 0 and z not in out: out.add(z); st.append(z)
    return out
LEV0 = int(os.environ.get('LEVEL', '8')); SLOTS = set(range(2 * LEV0, 2 * LEV0 + 2 * K))
for e in EXT: assert X not in reach(e) and not (reach(e) & SLOTS), ('EXT mover reaches the client or a cascade slot', e)
def chainset(e, s):
    out = []
    while e >= 0:
        m = 2 * e + s[e]; out.append(m); e = xt0[m]
    return out
CH = {(e, t): chainset(e, SB[t]) for e in EXT for t in range(P + 1)}
KEEPR = os.environ.get('KEEPR') == '1'
LEVR = int(os.environ.get('LEVEL', '8')); SLOTSR = set(range(2 * LEVR, 2 * LEVR + 2 * K)); HOOK = SLOTSR | {X}
def hookwalk(m, s):   # from option m on base state s: fixed prefix options until an option whose target is a HOOK mover
    pre = []
    while True:
        pre.append(m); z = xt0[m]
        if z < 0: return pre, None
        if z in HOOK: return pre, z
        m = 2 * z + s[z]
RSKIP = set(int(c) for c in os.environ.get('KEEPRSKIP', '').split(',') if c)
RONLY = set(int(c) for c in os.environ.get("KEEPRONLY", "").split(",") if c)
RD = {}   # (r, t, k) -> (prefix, hook mover or None)
if KEEPR:
    for r in range(64):
        if r in HOOK or r in RSKIP or (RONLY and r not in RONLY): continue
        for t in range(P):
            pr = [hookwalk(2 * r + k, SB[t]) for k in (0, 1)]
            if any(h is not None for _, h in pr):
                for k in (0, 1): RD[(r, t, k)] = pr[k]
FX = sorted(set(m for v in CH.values() for m in v) | set(m for v in RD.values() for m in v[0]), key=lambda m: D['br'][m])   # fixed options, ascending base rank
l = subprocess.run([sys.executable, os.path.join(here, '..', 'l13', 'reqpref.py'), gen, tp, str(X), str(P)], capture_output=True, text=True).stdout
req = dict(ast.literal_eval(l[l.index('['):l.index('] |') + 1]))
nv = [0]
def new(): nv[0] += 1; return nv[0]
cl = []
H = 2 * K; NC = 2 * H        # cascade options 0..NC-1; client options NC, NC+1
NO = NC + 2
TRUE = new(); cl.append([TRUE])
def xor(a, c, z): cl.extend([[-z, a, c], [-z, -a, -c], [z, -a, c], [z, a, -c]])
def AND(lits):
    z = new()
    for q in lits: cl.append([-z, q])
    cl.append([z] + [-q for q in lits]); return z
def OR(lits):
    lits = [q for q in lits if q is not None]
    if not lits: return -TRUE
    z = new()
    for q in lits: cl.append([z, -q])
    cl.append([-z] + list(lits)); return z
s = [[new() for y in range(H)] for t in range(P + 1)]
g = [[new(), new()] for i in range(K)]
LEV = int(os.environ.get('LEVEL', '8'))   # cascade on levels LEV..LEV+K-1, clock = the base's o(LEV-1) on the clamped run
def ob(t, l): return sim6.okeys(D, list(SB[t]))[l]
o = [[(TRUE if ob(t, LEV - 1) else -TRUE)] + [new() for i in range(K)] for t in range(P + 1)]
if LEV == 8: assert all(ob(t, 7) == t % 2 for t in range(P + 1))
# acyclic order among cascade movers (client is above all: it may read any cascade mover)
ordv = {}
for y in range(H):
    for z in range(y + 1, H): ordv[(y, z)] = new()
def before(z, y): return ordv[(z, y)] if z < y else -ordv[(y, z)]
for a1 in range(H):
    for a2 in range(H):
        for a3 in range(H):
            if len({a1, a2, a3}) == 3: cl.append([-before(a1, a2), -before(a2, a3), before(a1, a3)])
TG = list(range(H)) + ['e%d' % e for e in EXT]   # targets
W = {}
for op in range(NO):
    y = op // 2 if op < NC else None
    opts_ = []
    for z in TG:
        if z == y: continue
        v = new(); W[(op, z)] = v; opts_.append(v)
        if y is not None and isinstance(z, int): cl.append([-v, before(z, y)])
    for i in range(len(opts_)):
        for j in range(i + 1, len(opts_)): cl.append([-opts_[i], -opts_[j]])
# ranks: total order over free options (cascade + client) and fixed options; fixed among themselves by base rank
ALL = list(range(NO)) + ['f%d' % m for m in FX]
rk = {}
def higher(a, b):
    if isinstance(a, str) and isinstance(b, str): return TRUE if D['br'][int(a[1:])] > D['br'][int(b[1:])] else -TRUE
    key = (a, b) if str(a) < str(b) else (b, a)
    if key not in rk: rk[key] = new()
    return rk[key] if key == (a, b) else -rk[key]
for a in ALL:
    for b in ALL:
        if a == b: continue
        for c in ALL:
            if c in (a, b): continue
            if isinstance(a, str) and isinstance(b, str) and isinstance(c, str): continue
            cl.append([-higher(a, b), -higher(b, c), higher(a, c)])
par = [new() for op in range(NO)]
def fpar(m): return TRUE if D['bp'][m] == 0 else -TRUE
def better_from(A, B, U):
    """A, B: dict element -> membership literal (chain of option side 0 / side 1); returns literal better = 1."""
    d = {}
    for e in U:
        a, b = A.get(e, -TRUE), B.get(e, -TRUE); v = new(); xor(a, b, v); d[e] = v
    tops = []
    for e in U:
        tp_ = new(); cl.append([-tp_, d[e]])
        for e2 in U:
            if e2 != e: cl.append([-tp_, -d[e2], higher(e, e2)])
        cl.append([tp_, -d[e]] + [AND([d[e2], higher(e2, e)]) for e2 in U if e2 != e]); tops.append((e, tp_))
    wins = []
    for e, tp_ in tops:
        pe = par[e] if isinstance(e, int) else fpar(int(e[1:]))
        wins.append(AND([tp_, B.get(e, -TRUE), pe])); wins.append(AND([tp_, A.get(e, -TRUE), -pe]))
    return OR(wins)
bet = [[None] * H for t in range(P + 1)]; xbet = [None] * (P + 1); SEL = {}
for t in range(P + 1):
    m = {}; cur = {}
    for op in range(NC):
        for e in ALL: m[(op, e)] = new()
    for z in range(H):
        for e in ALL:
            c = new(); a0, a1 = m[(2 * z, e)], m[(2 * z + 1, e)]; sz = s[t][z]
            cl.extend([[sz, -c, a0], [sz, c, -a0], [-sz, -c, a1], [-sz, c, -a1]]); cur[(z, e)] = c
    def memb(op, e):   # membership literal of element e in the chain starting at option op (op may be a client option)
        if e == op: return TRUE
        terms = []
        for z in TG:
            if (op, z) not in W: continue
            if isinstance(z, int): terms.append(AND([W[(op, z)], cur[(z, e)]]))
            elif isinstance(e, str) and int(e[1:]) in CH[(int(z[1:]), t)]: terms.append(W[(op, z)])
        return OR(terms)
    for op in range(NC):
        for e in ALL:
            r = memb(op, e); cl.extend([[-m[(op, e)], r], [m[(op, e)], -r]])
    for y in range(H):
        A = {e: m[(2 * y, e)] for e in ALL}; B = {e: m[(2 * y + 1, e)] for e in ALL}
        bet[t][y] = better_from(A, B, ALL)
    if KEEPR and t < P:
        order_ = sim6.topo(D); vb = sim6.values(D, list(SB[t]), order_)
        for r in sorted({r_ for (r_, t_, k_) in RD if t_ == t}):
            sides = []
            for k in (0, 1):
                pre, hk = RD[(r, t, k)]; mm = {('f%d' % q): TRUE for q in pre}
                if hk is not None:
                    if hk == X:   # the client's current option (its state at row t is the target's) and that option's chain
                        cop = NC + SB[t][X]
                        for e in ALL:
                            if isinstance(e, str) and e in mm: continue
                            mm[e] = memb(cop, e)
                    else:         # a cascade mover: its current option's chain = cur[(z, e)]
                        z = hk - 2 * LEVR
                        for e in ALL:
                            if isinstance(e, str) and e in mm: continue
                            mm[e] = cur[(z, e)]
                sides.append(mm)
            m1 = 2 * r + 1 - SB[t][r]; y1 = xt0[m1]; ov = sim6.bv(D, m1) + (vb[y1] if y1 >= 0 else 0)
            want = (ov > vb[r]) != bool(SB[t][r])   # base better_r = 1 iff option 1 has the larger value
            want = int(SB[t][r]) if not (ov > vb[r]) else 1 - int(SB[t][r])
            rb = better_from(sides[0], sides[1], ALL)
            if os.environ.get('DEBUGCORE') == '1':
                sel = new(); SEL[sel] = (r, t); cl.append([-sel, rb] if want else [-sel, -rb])
            else: cl.append([rb] if want else [-rb])
    if t in req:
        A = {e: memb(NC, e) for e in ALL}; B = {e: memb(NC + 1, e) for e in ALL}
        xb = better_from(A, B, ALL); cl.append([xb] if req[t] else [-xb])
for t in range(P + 1):
    for i in range(K):
        a, a2, op_, on = s[t][2 * i], s[t][2 * i + 1], o[t][i], o[t][i + 1]
        sp = new(); xor(a, a2, sp); x1 = new(); xor(a, op_, x1)
        cl.extend([[-sp, -on, x1], [-sp, on, -x1]])
        for av, gv in ((0, g[i][0]), (1, g[i][1])):
            lit = a if av else -a; cl.extend([[sp, -lit, -on, gv], [sp, -lit, on, -gv]])
for t in range(P):
    for y in range(H):
        c = o[t + 1][y // 2]
        d1 = new(); xor(bet[t][y], s[t][y], d1); d2 = new(); xor(s[t][y], c, d2)
        mm = new(); cl.extend([[-mm, d1], [-mm, d2], [mm, -d1, -d2]]); xor(s[t][y], mm, s[t + 1][y])
if os.environ.get('KEEPO') == '1':   # the cascade's top key o(7+K) must equal the base's (clamped run) on rows 0..P
    for t in range(P + 1):
        v_ = ob(t, LEV - 1 + K); cl.append([o[t][K]] if v_ else [-o[t][K]])
if os.environ.get('FORCEBASE') == '1':   # debug: the client's options exactly as in the base genome
    for k in (0, 1):
        z = xt0[2 * X + k]; key = (NC + k, ('e%d' % z) if z >= 0 else None)
        for zz in TG:
            if (NC + k, zz) in W: cl.append([W[(NC + k, zz)]] if zz == key[1] else [-W[(NC + k, zz)]])
        cl.append([par[NC + k]] if D['bp'][2 * X + k] == 0 else [-par[NC + k]])
        for f in FX: cl.append([higher(NC + k, 'f%d' % f)] if D['br'][2 * X + k] > D['br'][f] else [-higher(NC + k, 'f%d' % f)])
    cl.append([higher(NC + 1, NC)] if D['br'][2 * X + 1] > D['br'][2 * X] else [-higher(NC + 1, NC)])
print('EKR2 LEVEL', os.environ.get('LEVEL', '8'), 'KEEPO', os.environ.get('KEEPO', '0'), 'K', K, 'P', P, 'client', X, 'EXT', EXT, 'fixed options', len(FX), 'kept readers', sorted({r for (r, t, k) in RD}), 'vars', nv[0], 'clauses', len(cl), flush=True)
cnfp = os.environ.get('CNF')
if cnfp:
    import hashlib
    with open(cnfp, 'w') as f:
        f.write(f'p cnf {nv[0]} {len(cl)}\n')
        for c in cl: f.write(' '.join(map(str, c)) + ' 0\n')
    print('CNF ->', cnfp, hashlib.sha1(open(cnfp, 'rb').read()).hexdigest()); sys.exit()
from pysat.solvers import Solver
import threading
sv = Solver(name='glucose4', bootstrap_with=cl); t0 = time.time()
timer = threading.Timer(TL, lambda: sv.interrupt()); timer.start()
r = sv.solve_limited(assumptions=list(SEL), expect_interrupt=True); timer.cancel()
if r is False and SEL: print('CORE', sorted(SEL[q] for q in (sv.get_core() or []) if q in SEL))
print(f'RESULT {"SAT" if r else ("UNSAT" if r is False else "NO_ANSWER")} {time.time() - t0:.1f}s', flush=True)
if r:
    M = set(q for q in sv.get_model() if q > 0); val = lambda v: (v in M) if v > 0 else (-v not in M)
    with open(outp, 'w') as f:
        for op in range(NO):
            tg_ = [z for z in TG if (op, z) in W and val(W[(op, z)])]
            f.write('opt %d -> %s even %d\n' % (op, tg_[0] if tg_ else 'exit', val(par[op])))
        order = sorted(ALL, key=lambda a: sum(1 for b in ALL if b != a and val(higher(a, b))))
        f.write('rank_order_ascending ' + ' '.join(map(str, order)) + '\n')
        f.write('gate ' + ' '.join('1' if val(g[i][a]) else '0' for i in range(K) for a in (0, 1)) + '\n')
        f.write('start ' + ''.join('1' if val(s[0][y]) else '0' for y in range(H)) + '\n')
        for t in range(P + 1): f.write('row %d %s\n' % (t, ''.join('1' if val(s[t][y]) else '0' for y in range(H))))
    print('decoded ->', outp)
