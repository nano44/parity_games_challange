#!/usr/bin/env python3
"""REFEREE-2 succ. 30: own IDEAL-CYC Howard run (P-N5-XICYC §2) on Γ(G) built by REFEREE-2's own builder
(R2-N5-REALIZE/realize_check.py build, from R104's packet §3.1), VJ values and Odd's optimal counterstrategy from the fleet reference
experiments/si/si.py Engine (no L-NEW code). Every non-mover Even vertex frozen at R104's start; a step: every mover to a successor of
largest value (ties: keep current, then larger index); stop when no mover has a strictly better successor.
Per genome: T, labels (C/R/p), C, R, P, longest Λ-keeping run, longest p-run, and checks:
  F1 (Ω_t ⊴ Ω_(t+1) at every vertex), F6 (no mover its own cycle node), STRICT (switched movers strictly improve),
  DOM (Ω_(t+1)(x) ⊵ ext(x, Ω_t(y)) for every mover x, successor y), BRSEG (p-run ≤ N), CYC (C ≤ n(2M+2)),
  TCYC (T ≤ C+R+(C+R+1)N), LEVEL0 (σ̄ = β-face at every level-0 gate, every state), K2 (σ̄(K2) = K1 every state).
Usage: r2howcyc.py GENOME.json ...   (ONEP=1: every gate keeps only its β-face)"""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(H, '..', '..', '..'))
sys.path[:0] = [os.path.join(H, '..', 'R2-N5-REALIZE')]
import realize_check as R
pg, Engine = R.pg, R.Engine
ONEP = os.environ.get('ONEP') == '1'
def howard(G):
    g, sig, tau, m = R.build(G, esc=True); N = G['N']; n = g.n; M = m['M']
    movers = list(range(N))
    succ = [list(s) if (g.owner[v] == 1 or v < N) else [sig[v]] for v, s in enumerate(g.succ)]
    if ONEP:
        for f in m['faces']: succ[m['gv'][f]] = [m['bv'][f]]
    h = pg.Game(list(g.prio), list(g.owner), succ); E = Engine(h)
    s = tuple(sig[v] if h.owner[v] == 0 else -1 for v in range(n))
    st = []; C = {k: 0 for k in 'F1 F6 STRICT DOM LEVEL0 K2'.split()}
    lev0g = [m['gv'][f] for f in m['faces'] if G['lev'][f[0]] == 0]; K1, K2 = m['K'][1], m['K'][2]
    while True:
        vs, tu = E.evaluate(s); st.append((s, vs, tu))
        C['LEVEL0'] += sum(tu[gq] != m['bv'][[f for f in m['faces'] if m['gv'][f] == gq][0]] for gq in lev0g) if not ONEP else 0
        C['K2'] += tu[K2] != K1
        C['F6'] += sum(vs[x][0] == x for x in movers)
        ns = list(s)
        for x in movers: ns[x] = max(h.succ[x], key=lambda w: (E.key(vs[w]), w == s[x], w))
        ns = tuple(ns)
        if ns == s or len(st) > 100000: break
        s = ns
    T = len(st) - 1; lab = []
    for t in range(T):
        (s1, v1, t1), (s2, v2, t2) = st[t], st[t + 1]
        lab.append('C' if any(v1[v][0] != v2[v][0] for v in range(n)) else 'R' if any(t1[v] != t2[v] for v in range(n) if h.owner[v] == 1) else 'p')
        C['F1'] += sum(E.key(v2[v]) < E.key(v1[v]) for v in range(n))
        for x in movers:
            if s1[x] != s2[x] and not E.key(v2[x]) > E.key(v1[x]): C['STRICT'] += 1
            for y in h.succ[x]:
                if E.key(v2[x]) < E.key(E.extend(x, v1[y])): C['DOM'] += 1
    L = ''.join(lab); runs = lambda ch: max([len(r) for r in ''.join(c if c in ch else ' ' for c in L).split()] + [0])
    c, r = L.count('C'), L.count('R')
    out = dict(N=N, n=n, M=M, T=T, labels=L, C=c, R=r, P=L.count('p'), longest_Lambda_keeping=runs('Rp'), longest_p=runs('p'),
               BRSEG_ok=runs('p') <= N, CYC_ok=c <= n * (2 * M + 2), TCYC_ok=T <= c + r + (c + r + 1) * N,
               movers_end=[ [k for k in range(len(G['opts'][x])) if m['gv'][(x, k)] == st[-1][0][x]][0] for x in movers])
    out.update(C); return out
if __name__ == '__main__':
    for f in sys.argv[1:]:
        print(os.path.basename(f), json.dumps(howard(json.load(open(f)))), flush=True)
