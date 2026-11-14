#!/usr/bin/env python3
"""REFEREE-2 succ. 30: §7 REACH3-CYC replay. N5'-xi (box190 §2.1 text: after S4a, at every Even v with |A(v)| >= 2 that is not its own
H-cycle node, σ_new(v) := Ξσ-best element of TIE(v) = {w in A(v): W*(v) = v ⊕ W*(w)}, ties: SPEC's choice, then larger index) written
here on REFEREE-2's SPEC step (R2-N5-REALIZE/realize_check.py step) and Γ3 builder (R2-P-N5-REACH/r2reach.py pad3/std3), from S3
(r2reach.s3). Compared with my IDEAL-CYC Howard run on Γ (r2howcyc.py). Per genome: every state 0..T3 standard (σ standard off the
movers, τ = standard), mover parts = Howard's states, transition T3+1 a fallback (S4c), iterations. Usage: r2xi3.py GENOME.json ..."""
import sys, os, json
H0 = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H0, '..', 'R2-P-N5-REACH'), H0]
import r2reach as RR, r2howcyc as HC
R = RR.R; pg, Engine, dual = R.pg, R.Engine, R.dual
def step_xi(g, E, Ed, sg, tu):
    n = g.n
    vs, sb = E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n))); Is = E.improving(tuple(sg), vs)
    vt, tb = Ed.evaluate(tuple(tu[v] if g.owner[v] == 1 else -1 for v in range(n))); It = Ed.improving(tuple(tu), vt)
    if not Is and not It: return None, 0
    ns, nt = list(sg), list(tu)
    if Is:
        opt = {v: {sg[v]} for v in range(n) if g.owner[v] == 0}
        for v, w in Is: opt[v].add(w)
        succ = [sorted(opt[v]) if g.owner[v] == 0 else [tu[v]] for v in range(n)]
        Er = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ)))
        vh, best = Er.evaluate(tuple(tu[v] if g.owner[v] == 1 else -1 for v in range(n)))
        for v in range(n):
            if g.owner[v] == 0: ns[v] = best[v]
        for v in range(n):           # the xi rule
            if g.owner[v] != 0 or len(opt[v]) < 2 or vh[v][0] == v: continue
            tie = [w for w in opt[v] if Er.extend(v, vh[w]) == vh[v]]
            if tie: ns[v] = max(tie, key=lambda w: (E.key(vs[w]), w == best[v], w))
    if It:
        opt = {v: {tu[v]} for v in range(n) if g.owner[v] == 1}
        for v, w in It: opt[v].add(w)
        succ = [sorted(opt[v]) if g.owner[v] == 1 else [sg[v]] for v in range(n)]
        _, best = Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
        for v in range(n):
            if g.owner[v] == 1: nt[v] = best[v]
    fb = 0
    if ns == list(sg) and nt == list(tu):
        fb = 1
        if Is:
            for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
        else:
            for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
    return (ns, nt), fb
def check(G, cap=2000):
    g3, M3 = RR.pad3(G); M3['g3'] = g3; P = M3['P']; N = G['N']
    E, Ed = Engine(g3), Engine(dual(g3)); sg, tu = RR.s3(g3)
    states = [(list(sg), list(tu))]; fbs = []
    while len(fbs) < cap:
        nxt, fb = step_xi(g3, E, Ed, *states[-1]); 
        if nxt is None: break
        fbs.append(fb); states.append((list(nxt[0]), list(nxt[1])))
    inv = {P[('m', f)]: f[1] for f in M3['faces']}
    def mov(st): return [inv.get(st[0][x], None) for x in range(N)]
    hw = HC.howard(G)
    # Howard mover states on Γ: re-run to get the sequence
    g, sig, tau, m = R.build(G, esc=True); succ = [list(s) if (g.owner[v] == 1 or v < N) else [sig[v]] for v, s in enumerate(g.succ)]
    h = pg.Game(list(g.prio), list(g.owner), succ); EH = Engine(h); s = tuple(sig[v] if h.owner[v] == 0 else -1 for v in range(h.n))
    ginv = {m['gv'][f]: f[1] for f in m['faces']}; seq = []
    while True:
        seq.append([ginv[s[x]] for x in range(N)]); vs, _ = EH.evaluate(s); ns = list(s)
        for x in range(N): ns[x] = max(h.succ[x], key=lambda w: (EH.key(vs[w]), w == s[x], w))
        ns = tuple(ns)
        if ns == s: break
        s = ns
    T3 = len(seq) - 1
    stdl = [ (states[j][0], states[j][1]) == tuple(RR.std3(G, M3, mov(states[j]))) for j in range(min(T3 + 1, len(states))) ]
    movers_eq = [mov(states[j]) for j in range(min(T3 + 1, len(states)))] == seq
    # Howard on Γ3 itself (IDEAL-CYC on Γ3: movers choose pads, every other Even vertex frozen at the standard state)
    sgs, _ = RR.std3(G, M3, G['start']); succ3 = [list(s_) if (g3.owner[v] == 1 or v < N) else [sgs[v]] for v, s_ in enumerate(g3.succ)]
    h3 = pg.Game(list(g3.prio), list(g3.owner), succ3); E3 = Engine(h3); s = tuple(sgs[v] if h3.owner[v] == 0 else -1 for v in range(h3.n))
    seq3 = []
    while True:
        seq3.append([inv[s[x]] for x in range(N)]); vs, _ = E3.evaluate(s); ns = list(s)
        for x in range(N): ns[x] = max(h3.succ[x], key=lambda w: (E3.key(vs[w]), w == s[x], w))
        ns = tuple(ns)
        if ns == s: break
        s = ns
    T33 = len(seq3) - 1
    stdl3 = [(states[j][0], states[j][1]) == tuple(RR.std3(G, M3, mov(states[j]))) for j in range(min(T33 + 1, len(states)))]
    # direct check on the xi run: until its first fallback every state standard, every transition a Howard step on Γ3's movers
    # (each mover to a ⊴-best successor under Ξσ, keeping σ(x) when it is one; non-movers unchanged), first fallback exactly when
    # no mover has a strictly better successor
    nonstd = nonhow = badstop = 0; j = 0
    while j < len(fbs):
        st = states[j]
        if (st[0], st[1]) != tuple(RR.std3(G, M3, mov(st))): nonstd += 1
        vs, _ = E.evaluate(tuple(st[0][v] if g3.owner[v] == 0 else -1 for v in range(g3.n)))
        anybetter = any(E.key(vs[w]) > E.key(vs[st[0][x]]) for x in range(N) for w in g3.succ[x])
        if fbs[j] == 1:
            badstop += anybetter; break
        if not anybetter: badstop += 1
        nxt = states[j + 1]
        for x in range(N):
            bestk = max(E.key(vs[w]) for w in g3.succ[x])
            if E.key(vs[nxt[0][x]]) != bestk or (E.key(vs[st[0][x]]) == bestk and nxt[0][x] != st[0][x]): nonhow += 1
        if any(nxt[0][v] != st[0][v] for v in range(N, g3.n) if g3.owner[v] == 0) or nxt[1] != st[1]: nonhow += 1
        j += 1
    out_direct = dict(mover_transitions=j, nonstd=nonstd, nonhoward=nonhow, badstop=badstop, fb_found=j < len(fbs), iters_after=len(fbs) - j)
    return dict(direct=out_direct, N=N, n3=g3.n, T_howard3=T33, movers_equal_howard3=[mov(states[j]) for j in range(min(T33 + 1, len(states)))] == seq3,
                standard_0_T33=all(stdl3), no_fb_before_T33=sum(fbs[:T33]) == 0, fb_at_T33plus1=(len(fbs) > T33 and fbs[T33] == 1),
                xi_eq_T33_plus3=len(fbs) == T33 + 3, gamma_equals_gamma3=seq == seq3, T_howard=T3, xi_iterations=len(fbs), standard_0_T3=all(stdl), movers_equal_howard=movers_eq,
                no_fb_before_T3=sum(fbs[:T3]) == 0, fb_at_T3plus1=(len(fbs) > T3 and fbs[T3] == 1))
if __name__ == '__main__':
    for f in sys.argv[1:]: print(os.path.basename(f), json.dumps(check(json.load(open(f)))), flush=True)
