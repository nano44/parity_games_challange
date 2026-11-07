"""Box 59 probe: W-TIGHTNESS between repeat escapes. For consecutive escapes u1 < u2 of (s, x) in one W-run (as wrise.py):
  TIGHT_X     some state k in [u1 + 1, u2] has Xi_k(x) = W_k(x) (x is W-tight).   TIGHT_X2  the same for some x2 (s's other choices in (u1, u2]).
  TIGHT_ANY   TIGHT_X or TIGHT_X2.
  RISE1       W(x) or W(x2) strictly rises from state u1 to state u2 + 1 (transitions u1 .. u2; Lemma TIGHT-REOPEN's conclusion).
  TIGHTV      TIGHT_X (or TIGHT_X2) holds but the corresponding W(x) (W(x2)) does not strictly rise from u1 to u2 + 1 (Lemma TIGHT-REOPEN: 0).
Split by scope (wrise2.py): SW (Even vertex of Z1 u Z2 switching in [u1, u2]), NOSW (Even vertex on both cycles, none switching), OO
(Odd-only cycles).  <scope>, <scope>_TIGHT, <scope>_NOTIGHT.  TIGHT1: x is tight at u1 + 1 already.
Usage: tight.py GAME.pg [START]."""
import sys, io, contextlib, os
ANC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "anc.py")
argv = sys.argv[1:]
VERB = '-v' in argv
if VERB: argv.remove('-v')
sys.argv = [ANC] + argv
g = {'__file__': ANC, '__name__': 'x'}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(open(ANC).read(), ANC, 'exec'), g)
ROOT, ROOT_CL, runs, B, S, TAU, Wv, E, n, own, X = g['ROOT'], g['ROOT_CL'], g['runs'], g['B'], g['S'], g['TAU'], g['Wv'], g['E'], g['n'], g['own'], g['X']
runof = g['runof']
K = lambda v: E.key(v)
esc = {}
for (u, z), r in ROOT.items():
    if r[0] == 'O' and r[2] is not None and u in runof: esc[(r[1], u)] = r[2]
seqs = {}
for (s, u), og in sorted(esc.items(), key=lambda t: t[0][1]): seqs.setdefault((runof[u], s, B[u][s]), []).append((u, og))
T = dict(REP=0, TIGHT_X=0, TIGHT_X2=0, TIGHT_ANY=0, TIGHT1=0, RISE1=0, TIGHTV=0)
for c in ('SW', 'NOSW', 'OO'): T[c] = 0; T[c + '_TIGHT'] = 0; T[c + '_NOTIGHT'] = 0
EX = []
for (ri, s, x), L in seqs.items():
    tau = TAU[runs[ri][0]]
    for (u1, o1), (u2, o2) in zip(L, L[1:]):
        x2s = {B[t + 1][s] for t in range(u1, u2)} - {x}
        tight = lambda y: any(X[k][y] == Wv(k, tau)[y] for k in range(u1 + 1, u2 + 1))
        rise = lambda y: K(Wv(u2 + 1, tau)[y]) > K(Wv(u1, tau)[y])
        tx = tight(x); tx2 = [y for y in x2s if tight(y)]
        T['REP'] += 1; T['TIGHT_X'] += tx; T['TIGHT_X2'] += bool(tx2); T['TIGHT_ANY'] += tx or bool(tx2)
        T['TIGHT1'] += X[u1 + 1][x] == Wv(u1 + 1, tau)[x]
        T['RISE1'] += rise(x) or any(rise(y) for y in x2s)
        T['TIGHTV'] += (tx and not rise(x)) + sum(1 for y in tx2 if not rise(y))
        Z1, Z2 = [s] + ROOT_CL[(u1, s)], [s] + ROOT_CL[(u2, s)]; U = set(Z1) | set(Z2)
        sw = any(own[e] == 0 and S[t][e] != S[t + 1][e] for e in U for t in range(u1, u2 + 1) if t + 1 < len(S))
        ev = any(own[e] == 0 for e in Z1) and any(own[e] == 0 for e in Z2)
        c = 'SW' if sw else ('NOSW' if ev else 'OO')
        T[c] += 1; T[c + ('_TIGHT' if (tx or tx2) else '_NOTIGHT')] += 1
        if VERB and not (tx or tx2) and len(EX) < 4: EX.append(('NOTIGHT', c, s, x, sorted(x2s), u1, u2, 'tau(s)', tau[s], 'Z1', Z1, 'Z2', Z2))
for e in EX: print(*e)
print("TIGHT", os.path.basename(argv[0]), " ".join(f"{a} {b}" for a, b in T.items()))
