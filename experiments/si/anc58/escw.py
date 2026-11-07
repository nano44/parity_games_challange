"""Box 59 probe: per-escape W-rise (CONJECTURE CLOSE-W). For every escape (s, u) in a W-run (anc.py's escape roots; x := sigma-bar_u(s),
Z := s followed by x's NEW Xi-play back to s):
  ESC        escapes.   CLOSE   some Even vertex of Z switches at u (a closing switch).   NOCLOSE  none does.
  CLOSE_WX   CLOSE and W(x) strictly rises at u.            CLOSE_NOWX   CLOSE and W(x) does not (CONJECTURE CLOSE-W: 0).
  CLOSE_WIT  CLOSE and some switching Even e of Z (W(e) strictly rising at u) is on x's W-play at u + 1 with a prefix pi that is x's
             W-play at u as well and avoids x's W-cycle node (Lemma W-PROP's hypothesis).   CLOSE_NOWIT  CLOSE without such an e.
  CLOSE_EFLAT  CLOSE and every switching Even vertex of Z has W(e) unchanged at u.
  NOCLOSE_WX   NOCLOSE and W(x) strictly rises at u.  XTAU: x = tau(s);  X2TAU: the new choice is tau(s).
  REP_CLOSE  repeat escapes u1 < u2 of one (s, x) whose FIRST escape u1 is CLOSE.   SW_NOCLOSE  repeats in wrise2's SW_CLOSED scope whose
             first escape is not CLOSE.
Usage: escw.py [-v] GAME.pg [START]."""
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
def wplay(k, tau, x):
    out, seen = [], set()
    while x not in seen:
        seen.add(x); out.append(x); x = S[k][x] if own[x] == 0 else tau[x]
    return out
esc = {}
for (u, z), r in ROOT.items():
    if r[0] == 'O' and r[2] is not None and u in runof: esc[(r[1], u)] = r[2]
T = dict(ESC=0, CLOSE=0, NOCLOSE=0, CLOSE_WX=0, CLOSE_NOWX=0, CLOSE_WIT=0, CLOSE_NOWIT=0, CLOSE_EFLAT=0, NOCLOSE_WX=0, XTAU=0, X2TAU=0, REP_CLOSE=0, SW_NOCLOSE=0)
EX, CL = [], {}
for (s, u) in sorted(esc, key=lambda t: t[1]):
    tau = TAU[runs[runof[u]][0]]; x = B[u][s]; Z = [s] + ROOT_CL[(u, s)]
    sw = [e for e in Z if own[e] == 0 and S[u][e] != S[u + 1][e]]
    T['ESC'] += 1; T['XTAU'] += x == tau[s]; T['X2TAU'] += B[u + 1][s] == tau[s]
    wx = K(Wv(u + 1, tau)[x]) > K(Wv(u, tau)[x])
    CL[(s, u)] = bool(sw)
    if not sw: T['NOCLOSE'] += 1; T['NOCLOSE_WX'] += wx; continue
    T['CLOSE'] += 1; T['CLOSE_WX' if wx else 'CLOSE_NOWX'] += 1
    up = [e for e in sw if K(Wv(u + 1, tau)[e]) > K(Wv(u, tau)[e])]
    T['CLOSE_EFLAT'] += not up
    def ok(e):
        P1 = wplay(u + 1, tau, x)
        if e not in P1: return False
        pi = P1[:P1.index(e)]
        return wplay(u, tau, x)[:len(pi) + 1] == pi + [e] and Wv(u, tau)[x][0] not in pi
    w = any(ok(e) for e in up)
    T['CLOSE_WIT' if w else 'CLOSE_NOWIT'] += 1
    if VERB and (not wx or not w) and len(EX) < 4: EX.append(('CASE', s, x, u, 'tau(s)', tau[s], 'Z', Z, 'sw', sw, 'up', up, 'wx', wx, 'Wx', wplay(u + 1, tau, x)))
seqs = {}
for (s, u) in sorted(esc, key=lambda t: t[1]): seqs.setdefault((runof[u], s, B[u][s]), []).append(u)
for (ri, s, x), L in seqs.items():
    for u1, u2 in zip(L, L[1:]):
        T['REP_CLOSE'] += CL[(s, u1)]
        U = set([s] + ROOT_CL[(u1, s)]) | set([s] + ROOT_CL[(u2, s)])
        if any(own[e] == 0 and S[t][e] != S[t + 1][e] for e in U for t in range(u1, u2 + 1) if t + 1 < len(S)) and not CL[(s, u1)]: T['SW_NOCLOSE'] += 1
for e in EX: print(*e)
print("ESCW", os.path.basename(argv[0]), " ".join(f"{a} {b}" for a, b in T.items()))
