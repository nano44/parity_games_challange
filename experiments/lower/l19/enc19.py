#!/usr/bin/env python3
"""L-LOWER 19 (successor 16): SAT encoding of N5's KEY run on box 217's one-player model 1P(G) (claude/l-new a32a588d,
docs/new/N5-QUIETKEY-box217.md §1, experiments/new/box217/one217.py), degree 2, a fixed level-width profile.

Symbolic genome (everything one217.py reads, free except the level profile):
  movers x = 0..N-1, lev(x) fixed by the profile W = (w_0, ..., w_(d-1)) (movers numbered level by level);
  option o = (x, k), k in {0, 1}, o = 2x + k;
  wt(x, k): one-hot over the level lev(x)-1 movers (absent at level 0);
  xt(x, k): one-hot over {exit} + movers, with a free strict order TO (pairwise vars + transitivity) and xt = y => TO(y, x)
            (= the Xi-graph is acyclic; every acyclic Xi-graph has such an order);
  beta of option o: rank position P[o][r] (permutation matrix M x M) and a sign SG[r] per rank position (+ = even priority);
            any (rank permutation, signs) is realised by br = rank, bp = 1 - sign (priority 6 + 2 br + bp);
  gate order: GO(o1, o2) = «gate(o1) < gate(o2)» for options of movers of the same level (transitive per level); keys compare
            gates of the same level only, and any per-level orders are realised by one global gate permutation (decode sorts by level);
  start s_0: free bit per mover.
One step s -> s' (one217.OneP.step, rule key), per mover x with options 0, 1 and current option c = s(x):
  value sets: Bo[x][k] = R(beta(x, k)) OR Bm[xt(x, k)] (bit-vector over rank positions; exit = empty), Bm[x] = Bo[x][c];
  better: Bo[x][1] > Bo[x][0] iff at the highest rank position r where they differ, Bo[x][1][r] == SG[r] (distinct powers of two,
            signed; the two option sets always differ (distinct first betas), so hops never decide);
  imp(x) = the other option is strictly better; A_s(x) = {c} + {other if imp};
  key: key'(x) = key'(wt(x, s'(x))) ++ (gate(x, s'(x))), all keys of one level distinct; KO'(y1, y2) = «key'(y1) < key'(y2)» for movers
            of one level, built level by level from KO' of the level below; s'(x) = other iff imp(x) and key(x, other) < key(x, c).
  A fixed point (no imp anywhere, or s' = s) repeats: the step function is total and a stopped run stays stopped.
Questions (pgad-style, pysat cadical195 or CNF out):
  ENUM: designated mover X (first mover of level K-1): at least 2^K - 1 switches of X among steps 0..L-1 (|K(X)| = 2^K at degree 2).
  LEN: s_L != s_(L-1) (the run is still moving at step L, T_key >= L).
Usage: enc19.py W L MODE [K] [OUT_PREFIX]      W = widths like 2,2,2,2   MODE = enum | len | check:GENOME.json
  env CNF=path: write DIMACS instead of solving. env SOLVER (default cadical195). env FIXG=genome.json: fix the genome (checker mode).
Prints RESULT SAT/UNSAT; on SAT writes OUT_PREFIX.json (one217 genome) and the encoder's state sequence."""
import sys, os, json, time, itertools
from pysat.formula import IDPool
from pysat.card import CardEnc, EncType

class Enc:
    def __init__(s):
        s.pool = IDPool(); s.cl = []; s.TRUE = s.new(); s.cl.append([s.TRUE])
    def new(s): return s.pool._next()
    def add(s, c): s.cl.append(c)
    def AND(s, *a):
        a = [x for x in a if x != s.TRUE]
        if any(x == -s.TRUE for x in a): return -s.TRUE
        if not a: return s.TRUE
        if len(a) == 1: return a[0]
        v = s.new()
        for x in a: s.add([-v, x])
        s.add([v] + [-x for x in a]); return v
    def OR(s, *a): return -s.AND(*[-x for x in a])
    def XOR(s, a, b):
        v = s.new(); s.add([-v, a, b]); s.add([-v, -a, -b]); s.add([v, -a, b]); s.add([v, a, -b]); return v
    def MUX(s, c, a, b):   # c ? a : b
        if a == b: return a
        return s.OR(s.AND(c, a), s.AND(-c, b))
    def onehot(s, vs):
        s.add(list(vs))
        for i in range(len(vs)):
            for j in range(i + 1, len(vs)): s.add([-vs[i], -vs[j]])

def build(W, L, mode, K=None, fixg=None):
    E = Enc(); T = E.TRUE
    lev = [l for l, w in enumerate(W) for _ in range(w)]; N = len(lev); M = 2 * N
    bylev = [[x for x in range(N) if lev[x] == l] for l in range(len(W))]
    # genome
    WT = {}
    for x in range(N):
        if lev[x] > 0:
            for k in (0, 1):
                cand = bylev[lev[x] - 1]; vs = [E.new() for _ in cand]; E.onehot(vs); WT[(x, k)] = dict(zip(cand, vs))
    TO = {}
    for a in range(N):
        for b in range(a + 1, N): v = E.new(); TO[(a, b)] = v; TO[(b, a)] = -v
    for a, b, c in itertools.permutations(range(N), 3):
        E.add([-TO[(a, b)], -TO[(b, c)], TO[(a, c)]])
    XT = {}
    for x in range(N):
        for k in (0, 1):
            ex = E.new(); vs = {y: E.new() for y in range(N) if y != x}; E.onehot([ex] + list(vs.values()))
            for y, v in vs.items(): E.add([-v, TO[(y, x)]])
            XT[(x, k)] = (ex, vs)
    P = [[E.new() for r in range(M)] for o in range(M)]
    for o in range(M): E.onehot(P[o])
    for r in range(M): E.onehot([P[o][r] for o in range(M)])
    SG = [E.new() for r in range(M)]
    GO = {}
    for l in range(len(W)):
        os_ = [2 * x + k for x in bylev[l] for k in (0, 1)]
        for i, a in enumerate(os_):
            for b in os_[i + 1:]: v = E.new(); GO[(a, b)] = v; GO[(b, a)] = -v
        for a, b, c in itertools.permutations(os_, 3): E.add([-GO[(a, b)], -GO[(b, c)], GO[(a, c)]])
    S = [[E.new() for x in range(N)]]   # s_t(x): option index (0/1)
    def gt(A, B):   # A > B as signed rank-weight sets (A != B assumed for the use made of it)
        res = -T; eq = T   # scan from the top rank down: res = decided greater, eq = all equal so far
        for r in reversed(range(M)):
            d = E.XOR(A[r], B[r]); here = E.AND(eq, d, -E.XOR(A[r], SG[r]))
            res = E.OR(res, here); eq = E.AND(eq, -d)
        return res
    def gsel(x1, c1, x2, c2):   # gate(x1, c1) < gate(x2, c2), c symbolic option bits, same level, (x1 != x2 or c differ)
        out = []
        for a in (0, 1):
            for b in (0, 1):
                o1, o2 = 2 * x1 + a, 2 * x2 + b
                if o1 == o2: continue
                out.append(E.AND(c1 if a else -c1, c2 if b else -c2, GO[(o1, o2)]))
        return E.OR(*out)
    switches = []
    for t in range(L):
        s = S[t]
        Bm = {}; Bo = {}
        # topological evaluation is symbolic: compute Bm in a fixed number of rounds is not needed: Bo uses Bm of Xi-targets,
        # which are defined by equations; acyclicity (TO) makes the equation system have the unique solution = path sets.
        for x in range(N): Bm[x] = [E.new() for r in range(M)]
        for x in range(N):
            for k in (0, 1):
                ex, vs = XT[(x, k)]; o = 2 * x + k
                Bo[(x, k)] = [E.OR(P[o][r], *[E.AND(v, Bm[y][r]) for y, v in vs.items()]) for r in range(M)]
            for r in range(M):
                m = E.MUX(s[x], Bo[(x, 1)][r], Bo[(x, 0)][r]); E.add([-Bm[x][r], m]); E.add([Bm[x][r], -m])
        imp = {}
        for x in range(N):
            g10 = gt(Bo[(x, 1)], Bo[(x, 0)]); imp[x] = E.MUX(s[x], -g10, g10)
        ns = [None] * N; KO = {}
        for l in range(len(W)):
            for x in bylev[l]:
                # c10 = key(x, 1) < key(x, 0)
                if l == 0: c10 = GO[(2 * x + 1, 2 * x)]
                else:
                    terms = []
                    for a, va in WT[(x, 0)].items():
                        for b, vb in WT[(x, 1)].items():
                            terms.append(E.AND(va, vb, GO[(2 * x + 1, 2 * x)] if a == b else KO[(b, a)]))
                    c10 = E.OR(*terms)
                kless = E.MUX(s[x], -c10, c10)
                ns[x] = E.XOR(s[x], E.AND(imp[x], kless))
            # KO' at level l (new keys)
            for i, y1 in enumerate(bylev[l]):
                for y2 in bylev[l][i + 1:]:
                    if l == 0: v = gsel(y1, ns[y1], y2, ns[y2])
                    else:
                        terms = []
                        for c1 in (0, 1):
                            for c2 in (0, 1):
                                sel = E.AND(ns[y1] if c1 else -ns[y1], ns[y2] if c2 else -ns[y2])
                                for a, va in WT[(y1, c1)].items():
                                    for b, vb in WT[(y2, c2)].items():
                                        terms.append(E.AND(sel, va, vb, GO[(2 * y1 + c1, 2 * y2 + c2)] if a == b else KO[(a, b)]))
                        v = E.OR(*terms)
                    KO[(y1, y2)] = v; KO[(y2, y1)] = -v
        S.append(ns)
    info = dict(N=N, M=M, d=len(W), L=L)
    if mode == 'enum':
        X = bylev[K - 1][0]; diffs = [E.XOR(S[t][X], S[t + 1][X]) for t in range(L)]
        need = 2 ** K - 1
        if need > L: E.add([-T])
        else:
            card = CardEnc.atleast(lits=diffs, bound=need, top_id=E.pool.top, encoding=EncType.seqcounter)
            for c in card.clauses: E.cl.append(c)
            E.pool.top = max(E.pool.top, card.nv)
        info['X'] = X; info['need'] = need
    elif mode == 'len':
        E.add([E.XOR(S[L][x], S[L - 1][x]) for x in range(N)])
    elif mode != 'free': raise SystemExit('mode?')
    if fixg is not None: fix(E, fixg, WT, XT, P, SG, GO, S, N, M, bylev)
    return E, info, dict(WT=WT, XT=XT, P=P, SG=SG, GO=GO, S=S, lev=lev, bylev=bylev, TO=TO)

def fix(E, G, WT, XT, P, SG, GO, S, N, M, bylev):
    """checker mode: unit clauses fixing the genome to one217 genome G (same profile, degree 2)"""
    assert G["N"] == N
    pr = {o: 6 + 2 * G["br"][G["opts"][o // 2][o % 2][2]] + G["bp"][G["opts"][o // 2][o % 2][2]] for o in range(M)}
    order = sorted(range(M), key=lambda o: (pr[o], o)); rank = {o: r for r, o in enumerate(order)}
    for o in range(M):
        E.add([P[o][rank[o]]]); E.add([SG[rank[o]] if pr[o] % 2 == 0 else -SG[rank[o]]])
    for x in range(N):
        for k in (0, 1):
            wt, xt, _ = G["opts"][x][k]
            if (x, k) in WT: E.add([WT[(x, k)][wt]])
            ex, vs = XT[(x, k)]; E.add([ex] if xt < 0 else [vs[xt]])
        E.add([S[0][x]] if G["start"][x] == 1 else [-S[0][x]])
    for (a, b), v in GO.items():
        if a < b:
            ga, gb = G["gate"][a // 2][a % 2], G["gate"][b // 2][b % 2]; E.add([v] if ga < gb else [-v])

def decode(model, V, N, M, lev):
    val = set(l for l in model if l > 0)
    T_ = lambda v: (v in val) if v > 0 else (-v not in val)
    opts = []
    for x in range(N):
        oo = []
        for k in (0, 1):
            wt = -1
            if (x, k) in V['WT']: wt = [y for y, v in V['WT'][(x, k)].items() if T_(v)][0]
            ex, vs = V['XT'][(x, k)]; xt = -1 if T_(ex) else [y for y, v in vs.items() if T_(v)][0]
            oo.append([wt, xt, 2 * x + k])
        opts.append(oo)
    rank = [[r for r in range(M) if T_(V['P'][o][r])][0] for o in range(M)]
    sign = [T_(V['SG'][r]) for r in range(M)]
    br = [rank[o] for o in range(M)]; bp = [0 if sign[rank[o]] else 1 for o in range(M)]
    import functools
    def cmp(a, b):
        if lev[a // 2] != lev[b // 2]: return lev[a // 2] - lev[b // 2]
        return -1 if T_(V['GO'][(a, b)]) else 1
    gorder = sorted(range(M), key=functools.cmp_to_key(cmp)); g = {o: i for i, o in enumerate(gorder)}
    gate = [[g[2 * x], g[2 * x + 1]] for x in range(N)]
    start = [1 if T_(V['S'][0][x]) else 0 for x in range(N)]
    states = [tuple(1 if T_(v) else 0 for v in st) for st in V['S']]
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": bp, "start": start}, states

if __name__ == "__main__":
    W = [int(v) for v in sys.argv[1].split(',')]; L = int(sys.argv[2]); mode = sys.argv[3]
    K = int(sys.argv[4]) if mode == 'enum' else None
    out = sys.argv[5] if len(sys.argv) > 5 else (sys.argv[4] if mode != 'enum' and len(sys.argv) > 4 else None)
    fixg = None
    if os.environ.get('FIXG'):
        fixg = json.load(open(os.environ['FIXG'])); fixg = fixg.get('genome', fixg)
    t0 = time.time(); E, info, V = build(W, L, mode, K, fixg)
    nv = max(max(abs(l) for l in c) for c in E.cl if c)
    print('INFO', info, 'vars', nv, 'clauses', len(E.cl), 'build_s', round(time.time() - t0, 1), flush=True)
    if os.environ.get('CNF'):
        with open(os.environ['CNF'], 'w') as f:
            f.write(f'p cnf {nv} {len(E.cl)}\n')
            for c in E.cl: f.write(' '.join(map(str, c)) + ' 0\n')
        print('CNF ->', os.environ['CNF']); sys.exit()
    from pysat.solvers import Solver
    sv = Solver(name=os.environ.get('SOLVER', 'cadical195'), bootstrap_with=E.cl); t1 = time.time(); r = sv.solve()
    print('SOLVE ->', 'SAT' if r else 'UNSAT', f'{time.time() - t1:.1f}s', flush=True)
    if r:
        G, states = decode(sv.get_model(), V, info['N'], info['M'], V['lev'])
        if out:
            json.dump(G, open(out + '.json', 'w')); open(out + '.states', 'w').write('\n'.join(''.join(map(str, s)) for s in states) + '\n')
        print('RESULT SAT', out or '', flush=True)
    else: print('RESULT UNSAT', flush=True)
