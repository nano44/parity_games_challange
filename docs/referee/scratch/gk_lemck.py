#!/usr/bin/env python3
"""REFEREE successor 35: the lemmas of P-N5-REACH §6 and the induction step of Theorem REACH3, tested one N5 transition at a time
on Gamma3(G_k) from the standard state of an ARBITRARY mover state s (the lemmas are stated for every s, not only the states of
the run). Engine: this lane's rl_engine.py (evaluate / improving); the transition below is SPEC S4a-S4c written out again.
Named counters (must be 0), unit = one standard state unless said otherwise:
  SBAR   sigma-bar at some gate != pbeta_g, or at K2 != r                     (Lemma SBAR3)
  TAU    I_tau nonempty                                                       (Lemma TAU3)
  ESC0   (K0, K1) not in I_sigma                                              (Lemma ESC3, first clause)
  ESC    sigma_new != sigma at some Even non-mover                            (Lemma ESC3)
  W      play value of the (sigma, tau)-play at some mover != (c_W, {}, 5 lev + 5)   (Lemma W3 (i))
  XI     Xi_sigma(m_(x,k)) has cycle node != K1 or path set != B_s(x,k) + {K0, K3} for some option  (PLAY3 (a) with SBAR3)
  AV     {sigma(x)} + I_sigma(x) != {m_(x,k) : k in A_s(x)} at some mover     (Lemma KEY3 (a))
  STEP   sigma_new at the movers != the standard state of the IDEAL step s' (or, when the IDEAL run stops at s: sigma_new != sigma,
         tau_new != tau, or no fallback)                                      (the induction step of REACH3)
usage: gk_lemck.py k nstates seed [revE]     (revE: the firing control, e-indices in REVERSED gate order)"""
import random
import sys
import rl_engine as eng
import gk_ideal as ideal
import gk_gamma3 as g3
import gk_build as B


def transition(g, gd, s, t):
    """one SPEC S4 pass from (s, t): returns dict(Xi, sb, Is, It, sn, tn, fb)."""
    n = g.n
    Xi, sb = eng.evaluate(g, s)
    Ut, tb = eng.evaluate(gd, [t[v] if g.owner[v] == 1 else None for v in range(n)])
    Is = eng.improving(g, Xi, s, 0)
    It = [(v, w) for v in range(n) if g.owner[v] == 1 for w in g.succ[v] if w != t[v] and gd.key(Ut[w]) > gd.key(Ut[t[v]])]
    if Is:
        A = {v: {s[v]} for v in range(n) if g.owner[v] == 0}
        for v, w in Is: A[v].add(w)
        keep = [sorted(A[v]) if g.owner[v] == 0 else [t[v]] for v in range(n)]
        _, ch = eng.evaluate(g.restrict(keep).dual(), [t[v] if g.owner[v] == 1 else None for v in range(n)])
        sn = [ch[v] if g.owner[v] == 0 else None for v in range(n)]
    else: sn = list(s)
    if It:
        A = {v: {t[v]} for v in range(n) if g.owner[v] == 1}
        for v, w in It: A[v].add(w)
        keep = [sorted(A[v]) if g.owner[v] == 1 else [s[v]] for v in range(n)]
        _, ch = eng.evaluate(g.restrict(keep), s)
        tn = [ch[v] if g.owner[v] == 1 else None for v in range(n)]
    else: tn = list(t)
    fb = (sn == s and tn == t)
    return dict(Xi=Xi, sb=sb, Is=Is, It=It, sn=sn, tn=tn, fb=fb)


def check_state(G, g, gd, idx, prio, owner, succ, s, c):
    N = G['N']; n3 = g.n
    sig, tau = g3.standard(G, idx, s, n3)
    for v in range(n3):
        if owner[v] == 0 and sig[v] is None: sig[v] = succ[v][0]
    T = transition(g, gd, sig, tau)
    opts = [(x, k) for x in range(N) for k in range(G['deg'][x])]
    # SBAR
    if any(T['sb'][idx[('g', o)]] != idx[('pbeta', o)] for o in opts) or T['sb'][idx['K2']] != idx['r']: c['SBAR'] += 1
    if T['It']: c['TAU'] += 1
    if (idx['K0'], idx['K1']) not in T['Is']: c['ESC0'] += 1
    if any(T['sn'][v] != sig[v] for v in range(n3) if owner[v] == 0 and v >= N): c['ESC'] += 1
    nx = [sig[v] if owner[v] == 0 else tau[v] for v in range(n3)]
    if any(eng.play_value(g, nx, x) != (idx['cW'], 0, 5 * G['lev'][x] + 5) for x in range(N)): c['W'] += 1
    bad = False
    for (x, k) in opts:
        Bs = ideal.bset(G, s, x, k)
        mask = (1 << g.rank[idx['K0']]) | (1 << g.rank[idx['K3']])
        for (y, j) in opts:
            if G['bid'][y][j] in Bs: mask |= 1 << g.rank[idx[('b', (y, j))]]
        val = T['Xi'][idx[('m', (x, k))]]
        if val[0] != idx['K1'] or val[1] != mask: bad = True
    if bad: c['XI'] += 1
    bad = False
    for x in range(N):
        Rx = {sig[x]} | {w for (v, w) in T['Is'] if v == x}
        if Rx != {idx[('m', (x, k))] for k in ideal.avail(G, s, x)}: bad = True
    if bad: c['AV'] += 1
    s2, why = ideal.step(G, s)
    if why is None:
        sig2, tau2 = g3.standard(G, idx, s2, n3)
        if any(T['sn'][x] != sig2[x] for x in range(N)) or T['tn'] != tau or T['fb']: c['STEP'] += 1
        c['moved'] += 1
    else:
        if T['sn'] != sig or T['tn'] != tau or not T['fb']: c['STEP'] += 1
        c['stopped'] += 1


if __name__ == '__main__':
    k, ns, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    rev = len(sys.argv) > 4 and sys.argv[4] == 'revE'
    G = B.genome(k)
    Gb = G
    if rev:                                   # firing control: e-indices in REVERSED gate order (P-N5-REALIZE fixes entry 2)
        import copy
        Gb = copy.deepcopy(G)
        M = sum(G['deg'])
        prio, owner, succ, names, idx = g3.build3(G)
        N = G['N']
        # swap the e-vertices' index positions: e of gate i <-> e of gate M-1-i (relabel vertices N+2M+i <-> N+2M+M-1-i)
        perm = list(range(len(prio)))
        for i in range(M): perm[N + 2 * M + i] = N + 2 * M + (M - 1 - i)
        inv = [0] * len(perm)
        for a, b in enumerate(perm): inv[b] = a
        prio = [prio[inv[v]] for v in range(len(perm))]; owner = [owner[inv[v]] for v in range(len(perm))]
        succ = [[perm[w] for w in succ[inv[v]]] for v in range(len(perm))]
        idx = {key: (perm[val] if key not in ('top', 'n0', 'n3') else val) for key, val in idx.items()}
    else:
        prio, owner, succ, names, idx = g3.build3(G)
    assert max(prio) <= len(prio), 'TARGET §1: priorities in {0..n}'
    g = eng.Game(prio, owner, succ); gd = g.dual()
    rnd = random.Random(seed)
    c = dict(SBAR=0, TAU=0, ESC0=0, ESC=0, W=0, XI=0, AV=0, STEP=0, moved=0, stopped=0)
    L, why, S = ideal.run(G, keep=True)
    states = []
    for i in range(ns):
        r = rnd.random()
        if r < 0.5: states.append([rnd.randrange(2) for _ in range(G['N'])])           # arbitrary state
        else:
            s = list(S[rnd.randrange(L + 1)])                                           # a run state with a few flips
            for _ in range(rnd.randrange(0, 4)): x = rnd.randrange(G['N']); s[x] = 1 - s[x]
            states.append(s)
    for s in states: check_state(G, g, gd, idx, prio, owner, succ, s, c)
    print('G_%d%s n3 %d max priority %d: %d standard states (seed %d): SBAR %d TAU %d ESC0 %d ESC %d W %d XI %d AV %d STEP %d | IDEAL moved %d, stopped %d' % (
        k, ' [control revE]' if rev else '', len(prio), max(prio), ns, seed, c['SBAR'], c['TAU'], c['ESC0'], c['ESC'], c['W'], c['XI'], c['AV'], c['STEP'], c['moved'], c['stopped']))
