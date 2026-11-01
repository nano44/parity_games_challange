"""Box 59 probe: REPAIRED W-REOPEN (L-RED R166's suggestion). Between consecutive escapes u1 < u2 of one (s, x) in one W-run, with
escaped cycles Z1 (at u1) and Z2 (at u2) (Z = s followed by x's NEW play back to s, as anc.py's ROOT_CL), does W(x) or W(x2) strictly rise
(x2 over s's other choices in (u1, u2], as wrise.py)? Scopes, by an Even vertex e on the cycle(s) whose sigma SWITCHES at a transition t:
  SW_OPEN    e in Z1 u Z2, u1 < t < u2          SW_HALF   e in Z1 u Z2, u1 <= t < u2        SW_CLOSED  e in Z1 u Z2, u1 <= t <= u2
  SW_Z1      e in Z1, u1 <= t <= u2             SW_Z2     e in Z2, u1 <= t <= u2            SW_BOTH    e in Z1 n Z2, u1 <= t <= u2
  EVEN_NOSW  both cycles have an Even vertex but none in Z1 u Z2 switches in [u1, u2] (R166's shape)
For each scope: <scope> = in-scope repeats, <scope>_NOWRISE = those without the rise (the repaired conjecture: 0).
Usage: wrise2.py GAME.pg [START]  (execs anc.py, so startcheck applies)."""
import sys, io, contextlib, os
ANC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "anc.py")
argv = sys.argv[1:]
sys.argv = [ANC] + argv
g = {'__file__': ANC, '__name__': 'x'}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(open(ANC).read(), ANC, 'exec'), g)
ROOT, ROOT_CL, runs, B, S, TAU, Wv, E, n, own = g['ROOT'], g['ROOT_CL'], g['runs'], g['B'], g['S'], g['TAU'], g['Wv'], g['E'], g['n'], g['own']
runof = g['runof']
K = lambda v: E.key(v)
esc = {}
for (u, z), r in ROOT.items():
    if r[0] == 'O' and r[2] is not None and u in runof: esc[(r[1], u)] = r[2]
seqs = {}
for (s, u), og in sorted(esc.items(), key=lambda t: t[0][1]): seqs.setdefault((runof[u], s, B[u][s]), []).append((u, og))
def cyc(u, s): return [s] + ROOT_CL[(u, s)]
def esw(e, a, b): return own[e] == 0 and any(S[t][e] != S[t + 1][e] for t in range(a, b + 1) if t + 1 < len(S))
SC = ['SW_OPEN', 'SW_HALF', 'SW_CLOSED', 'SW_Z1', 'SW_Z2', 'SW_BOTH', 'EVEN_NOSW']
T = {'REP': 0, 'EQ': 0}
for c in SC: T[c] = 0; T[c + '_NOWRISE'] = 0; T[c + '_EQNOWRISE'] = 0
EX = []
for (ri, s, x), L in seqs.items():
    tau = TAU[runs[ri][0]]
    for (u1, o1), (u2, o2) in zip(L, L[1:]):
        x2s = {B[t + 1][s] for t in range(u1, u2)} - {x}
        rise = K(Wv(u2, tau)[x]) > K(Wv(u1, tau)[x]) or any(K(Wv(u2, tau)[y]) > K(Wv(u1, tau)[y]) for y in x2s)
        Z1, Z2 = cyc(u1, s), cyc(u2, s); U, I = set(Z1) | set(Z2), set(Z1) & set(Z2)
        eq = o1 == o2; T['REP'] += 1; T['EQ'] += eq
        hit = {'SW_OPEN': any(esw(e, u1 + 1, u2 - 1) for e in U), 'SW_HALF': any(esw(e, u1, u2 - 1) for e in U),
               'SW_CLOSED': any(esw(e, u1, u2) for e in U), 'SW_Z1': any(esw(e, u1, u2) for e in Z1),
               'SW_Z2': any(esw(e, u1, u2) for e in Z2), 'SW_BOTH': any(esw(e, u1, u2) for e in I)}
        hit['EVEN_NOSW'] = any(own[e] == 0 for e in Z1) and any(own[e] == 0 for e in Z2) and not hit['SW_CLOSED']
        for c in SC:
            if hit[c]:
                T[c] += 1
                if not rise:
                    T[c + '_NOWRISE'] += 1; T[c + '_EQNOWRISE'] += eq
                    if c == 'SW_CLOSED' and len(EX) < 3:
                        sw = sorted((e, t) for e in U if own[e] == 0 for t in range(u1, u2 + 1) if t + 1 < len(S) and S[t][e] != S[t + 1][e])
                        EX.append(('NOWRISE_SW', s, x, u1, u2, o1, o2, 'Z1', Z1, 'Z2', Z2, 'switches', sw))
for e in EX: print(*e)
print("WRISE2", os.path.basename(argv[0]), " ".join(f"{a} {b}" for a, b in T.items()))
