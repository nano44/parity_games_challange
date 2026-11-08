#!/usr/bin/env python3
"""L-COMP box 32 (successor 13): EXACT CNF encoding of «a genome whose run realizes a given core trajectory exactly».
Written from the R104 / IDEAL rules as l6/sim6.py and l9/fenc.c state them (ENC preference, R105); no code of ann.c / gsolve.py.

Model (one step s -> ns): movers x = 0..N-1, N = 2d, level l = x // 2; option m = 2x + k, target xt[m] (mover or -1), rank br[m]
(distinct), sign bp[m] (1 = negative). chain(x, k) at s = m = 2x+k, then y = xt[m], option 2y + s[y], ... until xt = -1.
pref_x(s) = 1 iff the top-rank option of chain(x,0) xor chain(x,1) is (in chain(x,1) and positive) or (in chain(x,0) and negative).
ns is built level by level, c = o(l-1) of ns: level 0: x flips iff pref_x != s[x] and gate[2x+1-s[x]] < gate[2x+s[x]];
level l >= 1: ns[x] = pref_x if s[x] != c (free) else s[x]. o(0) = gate[ns0] > gate[2+ns1]; o(l) = (a != b) ? (a != c) : G_l[a],
G_l[a] = gate[4l+a] > gate[4l+2+a] (a = ns[2l], b = ns[2l+1]). The run stops when ns == s.
REALIZES(genome, target S*[0..T] on core movers 0..2h-1): the run's core states equal S* at t = 0..T, the run makes a change at
every t < T, and S_T is a fixed point (ns == s), i.e. the run's T equals the target's T.

Unknowns (free unless fixed by an option): strict total order of ranks over the options in scope, signs, gate bits G_l[0], G_l[1]
of helper levels l >= h, helper start bits, helper states at every step. FIXED always: wiring xt (W0 scope), core gates (levels
0..h-1, taken from the genome file), core start (= target row 0).
Relevant movers: core + every mover statically reachable from a relevant mover's options + every mover of a level below a relevant
helper's level (o(l-1) reads all pairs 0..l-1); fixpoint. Movers outside are never read by a relevant mover; they are dropped (their
states never affect the core; the decoded genome is re-checked by replay, so T is re-measured there).

Preference encoding at (t, x): U = options statically reachable from 2x or 2x+1; inA_e, inB_e (chain membership literals at S_t),
d_e = inA_e xor inB_e; one-hot-ish top selector tau_e (at least one; tau_e -> d_e; tau_e & d_f -> ord(e,f) for f != e);
tau_e & inB_e -> (P <-> pos_e); tau_e & inA_e -> (P <-> !pos_e). ord(e,f) = rank e > rank f, transitive, total (asym by sign).

Usage: enc32.py GENOME TARGET H [--fix all|ranks,signs,gates,starts] [--solve cadical|glucose] [--cnf out.cnf] [--out decoded.txt]
       [--lazy] [--relax]
--relax: helper transitions dropped (helper states free per step); a sound relaxation: its UNSAT implies the full UNSAT.
TARGET: first line "rows ncore", then one bit string per step (t = 0..T) for movers 0..ncore-1 (ncore = 2H)."""
import sys, os, argparse, time, hashlib
SKIPCORE = set(int(v) for v in os.environ.get('SKIPCORE', '').split(',') if v)   # diagnostics only

class Enc:
    def __init__(s, sink=None):
        s.nv = 0; s.cl = []; s.ncl = 0; s.empty = False; s.sink = sink   # sink(clause): stream instead of storing
    def new(s):
        s.nv += 1; return s.nv
    def add(s, c):
        out = []
        for l in c:
            if l is True: return
            if l is False: continue
            out.append(l)
        s.ncl += 1
        if not out: s.empty = True
        if s.sink is not None:
            if out: s.sink(out)
        else: s.cl.append(out)
    # constant-folding gates (literals: int or True/False)
    def neg(s, a):
        return (not a) if isinstance(a, bool) else -a
    def AND(s, a, b):
        if a is False or b is False: return False
        if a is True: return b
        if b is True: return a
        if a == b: return a
        if a == -b: return False
        v = s.new(); s.add([-v, a]); s.add([-v, b]); s.add([v, -a, -b]); return v
    def OR(s, a, b):
        return s.neg(s.AND(s.neg(a), s.neg(b)))
    def XOR(s, a, b):
        if isinstance(a, bool) and isinstance(b, bool): return a != b
        if a is False: return b
        if b is False: return a
        if a is True: return s.neg(b)
        if b is True: return s.neg(a)
        if a == b: return False
        if a == -b: return True
        v = s.new()
        s.add([-v, a, b]); s.add([-v, -a, -b]); s.add([v, -a, b]); s.add([v, a, -b]); return v
    def MUX(s, c, a1, a0):   # c ? a1 : a0
        if c is True: return a1
        if c is False: return a0
        if a1 == a0: return a1
        if a1 is True and a0 is False: return c
        if a1 is False and a0 is True: return s.neg(c)
        return s.OR(s.AND(c, a1), s.AND(s.neg(c), a0))
    def EQ(s, a, b):   # assert a == b
        if isinstance(a, bool) and isinstance(b, bool):
            if a != b: s.add([])
            return
        s.add([s.neg(a), b]); s.add([a, s.neg(b)])

def rdgen(p):
    D = {}
    for ln in open(p):
        w = ln.split()
        if w and w[0] == 'd': D['d'] = int(w[1])
        elif w and w[0] in ('xt', 'br', 'bp', 'gate', 'start'): D[w[0]] = list(map(int, w[1:]))
    return D

def wrgen(D, p):
    with open(p, 'w') as f:
        f.write(f"d {D['d']}\n")
        for k in ('xt', 'br', 'bp', 'gate', 'start'): f.write(k + ' ' + ' '.join(map(str, D[k])) + '\n')

def rdtarget(p):
    L = open(p).read().split()
    rows, nc = int(L[0]), int(L[1]); S = [[int(ch) for ch in L[2 + i]] for i in range(rows)]
    assert all(len(r) == nc for r in S); return S, nc

def build(D, S, H, fix=(), lazy=False, sink=None, relax=False, thresh=False, fixpoint=True, freeopts=(), freerank=(), cand_in=None):
    d = D['d']; N = 2 * d; xt = D['xt']; g = D['gate']; T = len(S) - 1; NC = 2 * H
    assert len(S[0]) == NC
    freeopts = set(freeopts); freerank = set(freerank)
    # W1: free targets of the options in freeopts (one owner mover); candidates = -1 and every mover z != owner that does not
    # reach the owner through FIXED edges (so every choice is acyclic: the owner's options are its only free edges)
    cand = {}
    if cand_in:   # explicit candidate lists (caller guarantees acyclicity; re-checked below for every choice by order)
        cand = {m: list(v) for m, v in cand_in.items()}; freeopts = set(cand)
    elif freeopts:
        owners = {m // 2 for m in freeopts}; assert len(owners) == 1, 'W1: free options of one mover only'
        x0 = owners.pop(); reach_x0 = {x0}; ch = True
        while ch:
            ch = False
            for m in range(2 * N):
                if m in freeopts: continue
                if xt[m] in reach_x0 and m // 2 not in reach_x0: reach_x0.add(m // 2); ch = True
        for m in freeopts: cand[m] = [-1] + [z for z in range(N) if z not in reach_x0]
    # static reach (options) from option m
    memo = {}
    def ro(m):
        if m in memo: return memo[m]
        r = {m}
        for y in (cand[m] if m in cand else [xt[m]]):
            if y >= 0: r |= ro(2 * y) | ro(2 * y + 1)
        memo[m] = frozenset(r); return memo[m]
    # acyclic check
    sys.setrecursionlimit(100000)
    vis = [0] * N
    def dfs(x):
        if vis[x] == 2: return True
        if vis[x] == 1: return False
        vis[x] = 1
        for k in (0, 1):
            if 2 * x + k in cand: continue
            y = xt[2 * x + k]
            if y >= 0 and not dfs(y): return False
        vis[x] = 2; return True
    for x in range(N):
        if not dfs(x): raise SystemExit('CYCLIC wiring')
    # relevant movers
    rel = set(range(NC))
    while True:
        new = set(rel)
        for x in rel:
            for m in ro(2 * x) | ro(2 * x + 1): new.add(m // 2)
        top = max(new) // 2
        new |= set(range(2 * top + 2))   # all movers of levels <= top (o(l-1) reads pairs 0..l-1; pair partner kept)
        if new == rel: break
        rel = new
    R = sorted(rel); Lmax = max(R) // 2
    assert R == list(range(2 * Lmax + 2))
    opts = sorted(m for x in R for m in (2 * x, 2 * x + 1))
    E = Enc(sink)
    fixed = set(fix)
    # ranks: ord(e,f) literal = rank e > rank f
    ordv = {}
    fr_u = {}; fr_w = {}
    fixed_sorted = sorted((m for m in range(2 * N) if m not in freerank), key=lambda m: D['br'][m])
    fidx = {m: i for i, m in enumerate(fixed_sorted)}
    def ordl(e, f):
        if 'ranks' in fixed and (e in freerank or f in freerank):
            if e in freerank and f in freerank: return fr_w[(e, f)] if (e, f) in fr_w else -fr_w[(f, e)]
            if e in freerank: return fr_u[e][fidx[f]]          # e above fixed f
            return -fr_u[f][fidx[e]]
        if 'ranks' in fixed: return D['br'][e] > D['br'][f]
        if e < f: return ordv[(e, f)]
        return -ordv[(f, e)]
    if freerank:   # FREERANK: insert positions of these options into the fixed order (unary; u[k] = above the k-th fixed)
        assert 'ranks' in fixed
        for e in freerank:
            fr_u[e] = [E.new() for _ in fixed_sorted]
            for k in range(len(fixed_sorted) - 1): E.add([-fr_u[e][k + 1], fr_u[e][k]])
        fl = sorted(freerank)
        for i, e in enumerate(fl):
            for f in fl[i + 1:]:
                w = E.new(); fr_w[(e, f)] = w
                for k in range(len(fixed_sorted)):
                    E.add([-fr_u[e][k], fr_u[f][k], w]); E.add([fr_u[e][k], -fr_u[f][k], -w])
    K = max(1, (len(opts) - 1).bit_length()); rb = {}
    if thresh and 'ranks' not in fixed:
        # THRESHOLD mode: rank = K-bit integer per option, all different; per site a threshold theta with
        # d_f -> r_f <= theta and tau_e -> r_e == theta (linear in |U| per site instead of |U|^2)
        for e in opts: rb[e] = [E.new() for _ in range(K)]          # MSB first
        for i, e in enumerate(opts):
            for f in opts[i + 1:]:
                ds = []
                for k in range(K):
                    ds.append(E.XOR(rb[e][k], rb[f][k]))
                E.add(ds)
    if 'ranks' not in fixed and not thresh:
        for i, e in enumerate(opts):
            for f in opts[i + 1:]: ordv[(e, f)] = E.new()
        n = len(opts)           # a tournament with no 3-cycle is a strict total order: forbid both 3-cycles of each triple
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    a, b, c = opts[i], opts[j], opts[k]
                    E.add([-ordl(a, b), -ordl(b, c), -ordl(c, a)]); E.add([-ordl(a, c), -ordl(c, b), -ordl(b, a)])
    pos = {m: ((D['bp'][m] == 0) if 'signs' in fixed else E.new()) for m in opts}
    Wv = {}
    for m in cand:   # one-hot target choice
        for z in cand[m]: Wv[(m, z)] = E.new()
        E.add([Wv[(m, z)] for z in cand[m]])
        cl = cand[m]
        for i in range(len(cl)):
            for j in range(i + 1, len(cl)): E.add([-Wv[(m, cl[i])], -Wv[(m, cl[j])]])
    # helper gate bits
    Gb = {}
    for l in range(H, Lmax + 1):
        for a in (0, 1):
            Gb[(l, a)] = (g[4 * l + a] > g[4 * l + 2 + a]) if 'gates' in fixed else E.new()
    # states
    st = [[None] * N for _ in range(T + 2)]
    for x in R:
        st[0][x] = bool(S[0][x]) if x < NC else ((D['start'][x] == 1) if 'starts' in fixed else E.new())
    for t in range(1, T + 1):
        for x in R: st[t][x] = bool(S[t][x]) if x < NC else E.new()
    for x in R: st[T + 1][x] = st[T][x] if x >= NC else bool(S[T][x])   # fixed point at T
    nP = 0; nquad = 0; lazyc = []
    def okeys(row):
        o = [None] * (Lmax + 1); c = None
        for l in range(Lmax + 1):
            a, b = row[2 * l], row[2 * l + 1]
            if l == 0: ol = g[0 + int(a)] > g[2 + int(b)]
            elif l < H:
                ol = (a != c) if a != b else (g[4 * l + int(a)] > g[4 * l + 2 + int(a)])
                assert isinstance(ol, bool)
            else:
                ga = E.MUX(a, Gb[(l, 1)], Gb[(l, 0)])
                ol = E.MUX(E.XOR(a, b), E.XOR(a, c), ga)
            o[l] = ol; c = ol
        return o
    O = [okeys(st[t]) for t in range(T + 2)]
    for t in range(T + 1 if fixpoint else T):   # transition S_t -> S_(t+1) (t = T: fixed point, unless a prefix run)
        s = st[t]; ns = st[t + 1]; on = O[t + 1]
        # chain membership at s: Q[y][e] = option e on chain starting at mover y (using s[y])
        Q = {}
        def q(y, e):
            if (y, e) in Q: return Q[(y, e)]
            v = E.MUX(s[y], inopt(2 * y + 1, e), inopt(2 * y, e)); Q[(y, e)] = v; return v
        def inopt(m, e):
            if m == e: return True
            if m in cand:
                acc = False
                for z in cand[m]:
                    if z < 0 or e not in (ro(2 * z) | ro(2 * z + 1)): continue
                    acc = E.OR(acc, E.AND(Wv[(m, z)], q(z, e)))
                return acc
            z = xt[m]
            if z < 0 or e not in (ro(2 * z) | ro(2 * z + 1)): return False
            return q(z, e)
        anych = []
        for x in R:
            l = x // 2
            if l == 0:
                free = g[2 * x + 1 - int(s[x])] < g[2 * x + int(s[x])]
            else:
                free = E.XOR(s[x], on[l - 1])
            if x < NC:
                assert isinstance(free, bool)
                if not free:
                    if s[x] != ns[x]: raise SystemExit(f'target moves blocked mover {x} at t {t + 1}')
                    continue
                if x in SKIPCORE: continue   # diagnostics only: drop this core mover's preference constraints
                # level 0 rule: flips iff pref != s: ns = pref when free; same for level >= 1
            if relax and x >= NC: continue   # RELAX: helper states free at every step (sound relaxation: UNSAT -> UNSAT)
            if free is False:
                E.EQ(ns[x], s[x]); continue
            U = sorted(ro(2 * x) | ro(2 * x + 1))
            inA = {e: inopt(2 * x, e) for e in U}; inB = {e: inopt(2 * x + 1, e) for e in U}
            dl = {e: E.XOR(inA[e], inB[e]) for e in U}
            Uc = [e for e in U if dl[e] is not False]
            P = E.new(); nP += 1
            tau = {e: E.new() for e in Uc}
            E.add([tau[e] for e in Uc])
            for e in Uc:
                E.add([-tau[e], dl[e]])
                E.add([-tau[e], E.neg(inB[e]), E.neg(pos[e]), P]); E.add([-tau[e], E.neg(inB[e]), pos[e], -P])
                E.add([-tau[e], E.neg(inA[e]), pos[e], P]); E.add([-tau[e], E.neg(inA[e]), E.neg(pos[e]), -P])
                if lazy and 'ranks' not in fixed: continue
                if thresh and 'ranks' not in fixed: continue
                for f in Uc:
                    if f == e: continue
                    E.add([-tau[e], E.neg(dl[f]), ordl(e, f)]); nquad += 1
            if thresh and 'ranks' not in fixed:
                th = [E.new() for _ in range(K)]
                for e in Uc:
                    for k in range(K):
                        E.add([-tau[e], -rb[e][k], th[k]]); E.add([-tau[e], rb[e][k], -th[k]])
                for f in Uc:   # d_f -> r_f <= th : forbid the first differing bit being r=1, th=0
                    prev = dl[f]
                    for k in range(K):
                        E.add([E.neg(prev), -rb[f][k], th[k]])
                        if k == K - 1: break
                        pk = E.new()   # pk forced true when prev and bit k equal
                        E.add([E.neg(prev), -rb[f][k], -th[k], pk]); E.add([E.neg(prev), rb[f][k], th[k], pk])
                        prev = pk
                    nquad += 1
            if lazy and 'ranks' not in fixed: lazyc.append((tau, dl))   # CEGAR: order clauses added when a model violates them
            # ns = free ? P : s
            if free is True: E.EQ(ns[x], P)
            else: E.EQ(ns[x], E.MUX(free, P, s[x]))
        if t < T and S[t] == S[t + 1]:   # core unchanged: some helper must change
            E.add([E.XOR(s[x], ns[x]) for x in R if x >= NC])
    info = dict(d=d, H=H, T=T, relevant=len(R), Lmax=Lmax, options=len(opts), vars=E.nv, clauses=E.ncl, empty=E.empty, nP=nP, quad=nquad,
                lazy=len(lazyc))
    return E, info, dict(Wv=Wv, cand=cand, freerank=freerank, fr_u=fr_u, fixed_sorted=fixed_sorted, rb=rb, R=R, opts=opts, ordl=ordl, pos=pos, Gb=Gb, st=st, Lmax=Lmax, lazyc=lazyc)

def decode(D, M, ctx, H):
    """model (set of true literals) -> genome text dict. Dropped movers: xt kept, ranks below all scoped, starts as in D."""
    val = lambda l: (l if isinstance(l, bool) else ((l in M) if l > 0 else (-l not in M)))
    E = dict(D); E = {k: (list(v) if isinstance(v, list) else v) for k, v in D.items()}
    opts = ctx['opts']; d = D['d']; N = 2 * d
    # ranks: sort scoped options by number of options they beat
    if ctx['cand']:
        E['xt'] = list(D['xt'])
        for m, cl in ctx['cand'].items():
            ch = [z for z in cl if val(ctx['Wv'][(m, z)])]; assert len(ch) == 1; E['xt'][m] = ch[0]
    if ctx['freerank']:
        fs = ctx['fixed_sorted']; slots = {}
        for e in ctx['freerank']: slots[e] = sum(1 for u in ctx['fr_u'][e] if val(u))   # number of fixed below e
        seq = []
        for i in range(len(fs) + 1):
            here = [e for e in ctx['freerank'] if slots[e] == i]
            here.sort(key=lambda e: sum(1 for f in ctx['freerank'] if f != e and val(ctx['ordl'](e, f))))
            seq += here
            if i < len(fs): seq.append(fs[i])
        E['br'] = [0] * (2 * N)
        for r_, m in enumerate(seq): E['br'][m] = r_
        E['bp'] = [(0 if val(ctx['pos'][m]) else 1) if m in ctx['pos'] else D['bp'][m] for m in range(2 * N)]
        wins = None
    elif ctx['rb']:
        wins = {e: sum(int(val(b)) << (len(ctx['rb'][e]) - 1 - k) for k, b in enumerate(ctx['rb'][e])) for e in opts}
    else:
        wins = {e: sum(1 for f in opts if f != e and val(ctx['ordl'](e, f))) for e in opts}
    if wins is not None:
        order = sorted(opts, key=lambda e: wins[e])           # ascending
        assert len(set(wins.values())) == len(opts), 'order not total/strict'
        rest = [m for m in range(2 * N) if m not in set(opts)]
        br = [0] * (2 * N)
        for i, m in enumerate(rest): br[m] = i
        for i, m in enumerate(order): br[m] = len(rest) + i
        E['br'] = br
        E['bp'] = [(0 if val(ctx['pos'][m]) else 1) if m in ctx['pos'] else D['bp'][m] for m in range(2 * N)]
    gt = list(D['gate'])
    for (l, a), lit in ctx['Gb'].items():
        hi, lo = (4 * l + a, 4 * l + 2 + a) if val(lit) else (4 * l + 2 + a, 4 * l + a)
        pair = sorted([gt[hi], gt[lo]]); gt[hi], gt[lo] = pair[1], pair[0]
    E['gate'] = gt
    E['start'] = [int(val(ctx['st'][0][x])) if x in set(ctx['R']) else D['start'][x] for x in range(N)]
    return E

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('genome'); ap.add_argument('target'); ap.add_argument('H', type=int)
    ap.add_argument('--fix', default=''); ap.add_argument('--solve', default='')
    ap.add_argument('--cnf'); ap.add_argument('--out'); ap.add_argument('--lazy', action='store_true'); ap.add_argument('--relax', action='store_true'); ap.add_argument('--lazy2', action='store_true'); ap.add_argument('--thresh', action='store_true'); ap.add_argument('--prefix', type=int, default=-1); ap.add_argument('--freeopts', default=''); ap.add_argument('--freerank', default=''); ap.add_argument('--only', default='')
    a = ap.parse_args()
    if a.lazy2: a.lazy = True
    if a.only: SKIPCORE.update(set(range(2 * a.H)) - set(int(v) for v in a.only.split(',')))   # keep only these core movers' constraints (sub-problem)
    fix = set() if not a.fix else ({'ranks', 'signs', 'gates', 'starts'} if a.fix == 'all' else set(a.fix.split(',')))
    D = rdgen(a.genome); S, nc = rdtarget(a.target); assert nc == 2 * a.H
    if a.prefix >= 0: S = S[:a.prefix + 1]   # PREFIX: core rows t = 0..prefix only, no fixed point at the end
    sinks = []; sv = None; body = None
    if a.solve:
        from pysat.solvers import Solver
        sv = Solver(name={'cadical': 'cadical195', 'glucose': 'glucose4'}[a.solve]); sinks.append(sv.add_clause)
    if a.cnf:
        body = open(a.cnf + '.body', 'w'); sinks.append(lambda c: body.write(' '.join(map(str, c)) + ' 0\n'))
    def sink(c):
        for f in sinks: f(c)
    t0 = time.time(); E, info, ctx = build(D, S, a.H, fix, a.lazy, sink, a.relax, a.thresh, a.prefix < 0, [int(v) for v in a.freeopts.split(',') if v], [int(v) for v in a.freerank.split(',') if v])
    info['build_s'] = round(time.time() - t0, 1); print('INFO', info, flush=True)
    if a.cnf:
        body.close(); nstored = sum(1 for _ in open(a.cnf + '.body'))
        with open(a.cnf, 'w') as f:
            f.write(f'p cnf {E.nv} {nstored + (1 if E.empty else 0)}\n')
            if E.empty: f.write('0\n')
            for ln in open(a.cnf + '.body'): f.write(ln)
        os.remove(a.cnf + '.body'); print('CNF ->', a.cnf, flush=True)
    if a.solve:
        if E.empty: print('RESULT UNSAT (empty clause at build)'); return
        lz = ctx['lazyc']; it = 0; done = set()
        while True:
            t1 = time.time(); r = sv.solve(); it += 1
            print(f'SOLVE it {it} -> {"SAT" if r else "UNSAT"} {time.time() - t1:.1f}s', flush=True)
            if not r: print('RESULT UNSAT'); return
            M = set(l for l in sv.get_model() if l > 0)
            if not lz: break
            val = lambda l: (l if isinstance(l, bool) else ((l in M) if l > 0 else (-l not in M)))
            ordl = ctx['ordl']; nadd = 0
            for tau, dl in lz:
                on = [e for e in tau if val(tau[e])]; D_ = [f for f in dl if val(dl[f])]
                bad = any(f != e and not val(ordl(e, f)) for e in on for f in D_)
                if not bad: continue
                for e in (D_ if a.lazy2 else on):   # lazy2: the whole block over the realized difference set
                    for f in D_:
                        if f != e and (a.lazy2 or not val(ordl(e, f))):
                            key = (tau[e], f)
                            if key in done: continue
                            done.add(key)
                            c = [-tau[e], -dl[f] if not isinstance(dl[f], bool) else None, ordl(e, f)]
                            sv.add_clause([l for l in c if l is not None and not isinstance(l, bool)]); nadd += 1
            if not nadd: break
            print(f'  lazy: added {nadd}', flush=True)
        G = decode(D, M, ctx, a.H)
        print('RESULT SAT')
        if a.out: wrgen(G, a.out); print('decoded ->', a.out, hashlib.sha1(open(a.out, 'rb').read()).hexdigest())

if __name__ == '__main__':
    main()
