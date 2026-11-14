#!/usr/bin/env python3
"""REFEREE-2 succ. 31: own replay of P-N5-ASC §3, §5, §6 on IDEAL-CYC (R118 (a)): Γ(G) from REFEREE-2's own builder
(R2-N5-REALIZE/realize_check.py build, from R104 §3.1; e-priorities in (level, gate) order, so [E-LEV] holds), Howard steps at the
movers as in R2-P-N5-XICYC/r2howcyc.py, VJ values / Odd's optimal counterstrategy from the fleet reference experiments/si/si.py Engine
(no L-NEW code read or imported). Plays, Λ, Π, e-sets, seq, ascents are computed HERE from (σ_t, σ̄_t); Λ cross-checked with the Engine.
Checks (violation counters, all must be 0 without CTRL):
  EDOM   every vertex with priority above the least e-priority is an e-vertex, c_W, K0 or K3 (per genome)
  EMON   E_t(v) ≤ E_(t+1)(v) (lex = integer order by priority) whenever Λ_t(v) = Λ_(t+1)(v)  (every vertex v, every step)
  CDEC   seq_t(v) = (f, …): y_f is a mover, Λ_t(y_f) = Λ_t(v), seq_t(v) = (f, seq_t(y_f))   (every (t, v) with seq nonempty)
  UPJ    every ascent (a, b) of seq_t(v): the play from a to b has a β of an option (x, k) entered from mover x, followed by its Ξ-target
         mover of level > lev(x) and ≥ lev(a's mover)
  UPB    ascents(seq_t(v)) ≤ U(G)                                                              (every (t, v))
  HUBG   per vertex v and Λ-interval I: D_E,I(v) ≤ F′_B(M_w), B = max ascents on I, M_w = #e-vertices more relevant than w
  LAMX   my Λ = the Engine's Λ (every (t, v))
CTRL=elevrev: e-priorities in DECREASING level order ([E-LEV] false; §3-§5 must still hold, §6 may fail).
Usage: r2asc.py GENOME.json ... | r2asc.py noup COUNT SEED   (random genomes with no strictly upward Ξ-edge, own generator)"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [os.path.join(H, '..', 'R2-N5-REALIZE')]
import realize_check as R
pg, Engine = R.pg, R.Engine
CTRL = os.environ.get('CTRL', '')
def Fp(B, M): return 1 + M * (M + 1) // 2 if B == 0 else (M * M + 3 * M + 1) * (1 + M * Fp(B - 1, M) ** 2)
def replay(G, C, I):
    g, sig, tau, m = R.build(G, esc=True); N = G['N']; n = g.n; lev = G['lev']
    prio = list(g.prio); faces = m['faces']; ev, bv, gv = m['ev'], m['bv'], m['gv']; cW, K = m['cW'], m['K']
    if CTRL == 'elevrev':
        es = sorted(prio[ev[f]] for f in faces)
        for p, f in zip(es, sorted(faces, key=lambda f: (-lev[f[0]], G['gate'][f[0]][f[1]]))): prio[ev[f]] = p
    E_of = {ev[f]: f for f in faces}; B_of = {bv[f]: f for f in faces}
    emin = min(prio[ev[f]] for f in faces)
    C['EDOM_units'] += 1
    C['EDOM'] += any(prio[v] > emin and v not in E_of and v not in (cW, K[0], K[3]) for v in range(n))
    U = sum(1 for x in range(N) for o in G['opts'][x] if o[1] >= 0 and lev[o[1]] > lev[x])
    succ = [list(s) if (g.owner[v] == 1 or v < N) else [sig[v]] for v, s in enumerate(g.succ)]
    h = pg.Game(prio, list(g.owner), succ); E = Engine(h)
    s = tuple(sig[v] if h.owner[v] == 0 else -1 for v in range(n)); st = []
    while True:
        vs, tu = E.evaluate(s); st.append((s, vs, tu))
        ns = list(s)
        for x in range(N): ns[x] = max(h.succ[x], key=lambda w: (E.key(vs[w]), w == s[x], w))
        ns = tuple(ns)
        if ns == s or len(st) > 100000: break
        s = ns
    I['runs'] += 1; I['states'] += len(st); I['maxU'] = max(I['maxU'], U)
    rank = {ev[f]: i for i, f in enumerate(sorted(faces, key=lambda f: prio[ev[f]]))}
    hist = [dict() for _ in range(n)]   # per vertex: Λ -> (set of e-set ints, max ascents)
    prevL = prevE = None
    for t, (s, vs, tu) in enumerate(st):
        nxt = [s[v] if h.owner[v] == 0 else tu[v] for v in range(n)]
        L = [None] * n; play = [None] * n
        for v in range(n):
            seen = {}; p = [v]; u = v
            while True:
                seen[u] = len(p) - 1; u = nxt[u]
                if u in seen: break
                p.append(u)
            cyc = p[seen[u]:]; w = max(cyc, key=lambda z: prio[z]); L[v] = w; play[v] = p
            C['LAMX'] += vs[v][0] != w; C['LAMX_units'] += 1
        SEQ = [[z for z in play[v] if z in E_of and prio[z] > prio[L[v]]] for v in range(n)]
        Ei = [sum(1 << rank[z] for z in q) for q in SEQ]
        for v in range(n):
            q = SEQ[v]; a = sum(1 for x, y in zip(q, q[1:]) if prio[y] > prio[x])
            C['UPB_units'] += 1; C['UPB'] += a > U; I['maxasc'] = max(I['maxasc'], a)
            if U == 0: I['noup_plays'] += 1; I['noup_maxasc'] = max(I['noup_maxasc'], a)
            rec = hist[v].setdefault(L[v], [set(), 0]); rec[0].add(Ei[v]); rec[1] = max(rec[1], a)
            if q:
                f = q[0]; yf = nxt[f]; C['CDEC_units'] += 1
                C['CDEC'] += not (yf < N and L[yf] == L[v] and SEQ[yf] == q[1:])
            for x, y in zip(q, q[1:]):
                if prio[y] > prio[x]:
                    C['UPJ_units'] += 1; pv = play[v]; seg = pv[pv.index(x):pv.index(y) + 1]; la = lev[E_of[x][0]]; ok = False
                    for i, z in enumerate(seg[:-1]):
                        if z in B_of:
                            xx = B_of[z][0]; nz = seg[i + 1]
                            if nz < N and lev[nz] > lev[xx] and lev[nz] >= la: ok = True
                    C['UPJ'] += not ok
        if prevL is not None:
            for v in range(n):
                if prevL[v] == L[v]: C['EMON_units'] += 1; C['EMON'] += Ei[v] < prevE[v]
        prevL, prevE = L, Ei
    for v in range(n):
        for w, (sets, B) in hist[v].items():
            Mw = sum(1 for f in faces if prio[ev[f]] > prio[w]); C['HUBG_units'] += 1; C['HUBG'] += len(sets) > Fp(B, Mw)
            I['maxDE'] = max(I['maxDE'], len(sets))
            if B == 0: I['maxDE_B0'] = max(I['maxDE_B0'], len(sets))
    return U
def rand_noup(rng):
    d = rng.randint(1, 4); w = [rng.randint(1, 3) for _ in range(d)]
    lev = [l for l in range(d) for _ in range(w[l])]; N = len(lev); byl = [[x for x in range(N) if lev[x] == l] for l in range(d)]
    opts = []; b = 0
    for x in range(N):
        k = rng.randint(1, 2); ox = []
        for _ in range(k):
            wt = rng.choice(byl[lev[x] - 1]) if lev[x] else -1
            xt = rng.choice([-1] + [y for y in range(N) if lev[y] <= lev[x] and y != x])
            ox.append([wt, xt, b]); b += 1
        opts.append(ox)
    M = b; br = rng.sample(range(M), M); bp = [rng.randint(0, 1) for _ in range(M)]; gp = rng.sample(range(M), M); gate = []; i = 0
    for x in range(N): gate.append(gp[i:i + len(opts[x])]); i += len(opts[x])
    return dict(N=N, lev=lev, opts=opts, gate=gate, br=br, bp=bp, start=[rng.randrange(len(opts[x])) for x in range(N)])
def xicyclic(G):
    adj = {x: [o[1] for o in G['opts'][x] if o[1] >= 0] for x in range(G['N'])}; col = {}
    def dfs(u):
        col[u] = 1
        for v in adj[u]:
            if col.get(v) == 1 or (v not in col and dfs(v)): return True
        col[u] = 2; return False
    return any(x not in col and dfs(x) for x in range(G['N']))
if __name__ == '__main__':
    from collections import Counter
    C = Counter(); I = Counter()
    if sys.argv[1] == 'noup':
        rng = random.Random(int(sys.argv[3])); cyc = 0
        for _ in range(int(sys.argv[2])):
            G = rand_noup(rng); cyc += xicyclic(G); assert replay(G, C, I) == 0
        print('NOUP random genomes', sys.argv[2], 'seed', sys.argv[3], 'Xi-cyclic', cyc, 'CTRL', CTRL or '-')
    else:
        for f in sys.argv[1:]:
            c0 = Counter(C); i0 = dict(maxasc=I['maxasc']); I['maxasc'] = 0
            U = replay(json.load(open(f)), C, I)
            print(os.path.basename(f), 'U(G)', U, 'max ascents', I['maxasc'], 'UPB viol', C['UPB'] - c0['UPB'], flush=True)
            I['maxasc_all'] = max(I['maxasc_all'], I['maxasc'])
    print('CTRL', CTRL or '-', ' '.join('%s %d' % kv for kv in sorted(C.items())))
    print('INFO', ' '.join('%s %d' % kv for kv in sorted(I.items())))
