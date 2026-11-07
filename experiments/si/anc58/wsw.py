"""Box 59 probe (mechanism of the repaired W-REOPEN). Fields:
  WSW          Even switches at transitions of W-runs;  WSW_FLAT  those with W(e) not strictly rising at the switch (W_(t+1)(e) = W_t(e)).
  For each repeat escape u1 < u2 of (s, x) in scope SW_CLOSED (wrise2.py): switching Even e in Z1 u Z2 at t in [u1, u2].
  SCOPE        in-scope repeats.
  CH_X         some switching (e, t) has e on x's (sigma_(t+1), tau)-play (the W-play) at t + 1, with W(e) strictly rising at t.
  CH_X2        the same on the W-play of some x2 (s's other choices in (u1, u2]).
  CH_NONE      neither (the repeat's W-rise is not carried by a switching vertex of the cycle along a W-play).
  RISE_X / RISE_X2   which of W(x), W(x2) strictly rises from u1 to u2.   XTAU / X2TAU: x = tau(s) / some x2 = tau(s).
  SIND1 / SIND2      s in D at u1 / u2 (sigma-bar(s) != tau(s)).
  CH_SIM       W(x) strictly rises at a transition t in [u1, u2) at which some Even e of Z1 u Z2 switches; CH_SIMSTRICT: and W(e) rises at t.
  CH_PFX       some switching e (W(e) rising at t < u2) is on x's W-play at t + 1 with a prefix pi that is x's W-play at t too (no Even
               vertex of pi switches at t), so W_j(x) = Phi(pi; W_j(e)) for j = t, t + 1.
  CH_PFXC      CH_PFX with the W-cycle node of x off pi (Lemma W-PROP's hypothesis; then W(x) strictly rises at t). WIT_Z1: such a witness e
               lies on Z1 (WIT_Z2ONLY: only on Z2). WIT_BEFORE_D: pi has no Odd vertex off tau at t + 1 (x's Xi-play at t + 1 follows pi too).
Usage: wsw.py [-v] GAME.pg [START]."""
import sys, io, contextlib, os
ANC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "anc.py")
argv = sys.argv[1:]
VERB = '-v' in argv
if VERB: argv.remove('-v')
sys.argv = [ANC] + argv
g = {'__file__': ANC, '__name__': 'x'}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(open(ANC).read(), ANC, 'exec'), g)
ROOT, ROOT_CL, runs, B, S, TAU, Wv, E, n, own = g['ROOT'], g['ROOT_CL'], g['runs'], g['B'], g['S'], g['TAU'], g['Wv'], g['E'], g['n'], g['own']
runof = g['runof']
K = lambda v: E.key(v)
T = dict(WSW=0, WSW_FLAT=0, SCOPE=0, CH_X=0, CH_X2=0, CH_NONE=0, RISE_X=0, RISE_X2=0, XTAU=0, X2TAU=0, SIND1=0, SIND2=0, CH_SIM=0, CH_SIMSTRICT=0, CH_PFX=0, CH_PFXC=0, WIT_Z1=0, WIT_Z2ONLY=0, WIT_BEFORE_D=0)
for r in runs:
    tau = TAU[r[0]]
    for t in r:
        for e in range(n):
            if own[e] == 0 and S[t][e] != S[t + 1][e]:
                T['WSW'] += 1; T['WSW_FLAT'] += K(Wv(t + 1, tau)[e]) == K(Wv(t, tau)[e])
esc = {}
for (u, z), r in ROOT.items():
    if r[0] == 'O' and r[2] is not None and u in runof: esc[(r[1], u)] = r[2]
seqs = {}
for (s, u), og in sorted(esc.items(), key=lambda t: t[0][1]): seqs.setdefault((runof[u], s, B[u][s]), []).append((u, og))
def wplay(k, tau, x):
    out, seen = [], set()
    while x not in seen:
        seen.add(x); out.append(x); x = S[k][x] if own[x] == 0 else tau[x]
    return out
EX = []
for (ri, s, x), L in seqs.items():
    tau = TAU[runs[ri][0]]
    for (u1, o1), (u2, o2) in zip(L, L[1:]):
        x2s = {B[t + 1][s] for t in range(u1, u2)} - {x}
        U = set([s] + ROOT_CL[(u1, s)]) | set([s] + ROOT_CL[(u2, s)])
        sw = [(e, t) for e in U if own[e] == 0 for t in range(u1, u2 + 1) if t + 1 < len(S) and S[t][e] != S[t + 1][e]]
        if not sw: continue
        T['SCOPE'] += 1
        rx = K(Wv(u2, tau)[x]) > K(Wv(u1, tau)[x]); rx2 = any(K(Wv(u2, tau)[y]) > K(Wv(u1, tau)[y]) for y in x2s)
        T['RISE_X'] += rx; T['RISE_X2'] += rx2; T['XTAU'] += x == tau[s]; T['X2TAU'] += tau[s] in x2s
        T['SIND1'] += B[u1][s] != tau[s]; T['SIND2'] += B[u2][s] != tau[s]
        up = [(e, t) for e, t in sw if K(Wv(t + 1, tau)[e]) > K(Wv(t, tau)[e])]
        cx = any(e in wplay(t + 1, tau, x) for e, t in up); cx2 = any(e in wplay(t + 1, tau, y) for e, t in up for y in x2s)
        T['CH_X'] += cx; T['CH_X2'] += cx2
        sim = [t for e, t in sw if t < u2 and K(Wv(t + 1, tau)[x]) > K(Wv(t, tau)[x])]
        T['CH_SIM'] += bool(sim); T['CH_SIMSTRICT'] += any(t < u2 for e, t in up if K(Wv(t + 1, tau)[x]) > K(Wv(t, tau)[x]))
        def pfx_ok(e, t):
            P = wplay(t + 1, tau, x)
            if e not in P: return False
            pi = P[:P.index(e)]
            return all(own[q] == 1 or S[t][q] == S[t + 1][q] for q in pi) and wplay(t, tau, x)[:len(pi) + 1] == pi + [e]
        T['CH_PFX'] += any(t < u2 and pfx_ok(e, t) for e, t in up)
        wits = [(e, t) for e, t in up if t < u2 and pfx_ok(e, t) and Wv(t, tau)[x][0] not in wplay(t + 1, tau, x)[:wplay(t + 1, tau, x).index(e)]]
        T['CH_PFXC'] += bool(wits)
        Z1 = [s] + ROOT_CL[(u1, s)]
        T['WIT_Z1'] += any(e in Z1 for e, t in wits); T['WIT_Z2ONLY'] += bool(wits) and not any(e in Z1 for e, t in wits)
        def before_d(e, t):
            P = wplay(t + 1, tau, x); pi = P[:P.index(e)]
            return all(own[q] == 0 or B[t + 1][q] == tau[q] for q in pi)
        T['WIT_BEFORE_D'] += any(before_d(e, t) for e, t in wits)
        if VERB and len(EX) < 4:
            EX.append(('WIT', s, x, 'tau(s)', tau[s], u1, u2, 'Z1', Z1, 'Z2', [s] + ROOT_CL[(u2, s)], 'wits', wits[:3], 'Wplay_x', wplay(wits[0][1] + 1, tau, x) if wits else None, 'D', sorted(q for q in range(n) if own[q] == 1 and B[wits[0][1] + 1][q] != tau[q]) if wits else None))
        if not cx and not cx2:
            T['CH_NONE'] += 1
            if len(EX) < 3: EX.append(('CHNONE', s, x, sorted(x2s), u1, u2, 'tau(s)', tau[s], 'sw', sorted(sw), 'up', sorted(up), 'rx', rx, 'rx2', rx2))
for e in EX: print(*e)
print("WSW", os.path.basename(argv[0]), " ".join(f"{a} {b}" for a, b in T.items()))
