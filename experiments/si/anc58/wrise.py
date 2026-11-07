"""Box 58 §8 probe (ODDONLY: both escaped cycles have no Even vertex; EVEN_NOWRISE: a cycle with an Even vertex and no rise): between consecutive escapes of one (s, x) in one W-run (u1 < u2), does W(x) or W(x2) strictly rise?
Also WMONV: W-monotonicity violations inside W-runs (R164 lane lemma)."""
import sys, io, contextlib, os
ANC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "anc.py")
argv = sys.argv[1:]
sys.argv = [ANC] + argv
g = {'__file__': ANC, '__name__': 'x'}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(open(ANC).read(), ANC, 'exec'), g)
ROOT, runs, B, S, TAU, Wv, E, n = g['ROOT'], g['runs'], g['B'], g['S'], g['TAU'], g['Wv'], g['E'], g['n']
runof = g['runof']
K = lambda v: E.key(v)
esc = {}
for (u, z), r in ROOT.items():
    if r[0] == 'O' and r[2] is not None and u in runof: esc[(r[1], u)] = (r[2], any(g['own'][q] == 0 for q in r[3]))
seqs = {}
for (s, u), og in sorted(esc.items(), key=lambda t: t[0][1]): seqs.setdefault((runof[u], s, B[u][s]), []).append((u, og))
T = dict(ODDONLY=0, ODDONLY_NOWRISE=0, EVEN_NOWRISE=0, REP=0, EQ=0, EQ_WRISE=0, EQ_NOWRISE=0, NEQ_WRISE=0, NEQ_NOWRISE=0, WMONV=0)
for r in runs:
    tau = TAU[r[0]]
    for k in r:
        a, b = Wv(k, tau), Wv(k + 1, tau)
        T['WMONV'] += sum(1 for v in range(n) if K(b[v]) < K(a[v]))
EX = []
for (ri, s, x), L in seqs.items():
    tau = TAU[runs[ri][0]]
    for (u1, (o1, ev1)), (u2, (o2, ev2)) in zip(L, L[1:]):
        x2s = {B[t + 1][s] for t in range(u1, u2)} - {x}
        rise = K(Wv(u2, tau)[x]) > K(Wv(u1, tau)[x]) or any(K(Wv(u2, tau)[y]) > K(Wv(u1, tau)[y]) for y in x2s)
        T['REP'] += 1; eq = o1 == o2; T['EQ'] += eq
        T[('EQ' if eq else 'NEQ') + ('_WRISE' if rise else '_NOWRISE')] += 1
        if eq and not rise and len(EX) < 3: EX.append((s, x, u1, u2, o1))
        odd_only = not ev1 and not ev2; T['ODDONLY'] += odd_only
        if not rise: T['ODDONLY_NOWRISE' if odd_only else 'EVEN_NOWRISE'] += 1
for e in EX: print("NOWRISE", *e)
print("WRISE", os.path.basename(argv[0]), " ".join(f"{a} {b}" for a, b in T.items()))
