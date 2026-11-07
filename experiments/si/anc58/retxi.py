"""Box 60 probe: Lemma KEY-RETURN (note docs/si/N5-RET-box60.md). For an Even y that leaves a for b at t0 and next enters a again at t1 > t0
(a RETURN of y to a), with c := sigma_t1(y) and g := key(Xi_t0(a), Xi_t0(b)) (the gain of leaving a):
  RET        returns (inside W-runs; --si: the whole classical switch-all run).
  PASSV      violations of Xi_t1(a) > Xi_t0(b) (Xi(a) rose strictly past b's value at the leave).   CURV  violations of Xi_t1(a) > Xi_t1(c).
  KEYV       violations of «some change of Xi(a) at a transition in [t0, t1) has key >= g».
  CHARGEV    pairs (y, a) per W-run whose returns exceed the changes of Xi(a) in the W-run (R95 RET-XIRISE: 0).
  MAXRET     max returns of one (y, a) per W-run.   SHARE  max number of distinct (y, a) returns charged to one change (a, t) (the first
             key->=g change in the window): the fan-out of one Xi-change over the returns it pays.
Usage: retxi.py [--si] GAME.pg [START]."""
import sys, io, contextlib, os
from collections import Counter
ANC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "anc.py")
argv = sys.argv[1:]
sys.argv = [ANC] + argv
g = {'__file__': ANC, '__name__': 'x'}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(open(ANC).read(), ANC, 'exec'), g)
S, X, KEY, runs, own, n, E, key = g['S'], g['X'], g['KEY'], g['runs'], g['own'], g['n'], g['E'], g['key']
K = lambda v: E.key(v)
T = dict(RET=0, PASSV=0, CURV=0, KEYV=0, CHARGEV=0, MAXRET=0, SHARE=0)
for run in runs:
    rs = run[0]; share = Counter(); per = Counter()
    for y in range(n):
        if own[y] != 0: continue
        left = {}
        for t in run:
            a, b = S[t][y], S[t + 1][y]
            if a == b: continue
            if b in left:
                t0, b0 = left[b]; T['RET'] += 1; per[(y, b)] += 1
                T['PASSV'] += not K(X[t][b]) > K(X[t0][b0]); T['CURV'] += not K(X[t][b]) > K(X[t][a])
                gn = key(X[t0][b], X[t0][b0])
                ch = [u for u in range(t0, t) if KEY[u][b] is not None and gn is not None and KEY[u][b] >= gn]
                if not ch: T['KEYV'] += 1
                else: share[(b, ch[0])] += 1
            left[a] = (t, b)
    for (y, a), c in per.items():
        T['MAXRET'] = max(T['MAXRET'], c)
        if c > sum(1 for u in run if KEY[u][a] is not None): T['CHARGEV'] += 1
    T['SHARE'] = max([T['SHARE']] + list(share.values()))
print("RETXI", os.path.basename(argv[-1] if not argv[-1].endswith('.start') else argv[-2]), " ".join(f"{a} {b}" for a, b in T.items()))
