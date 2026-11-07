"""Box 62 probe: is I_tau empty inside tau-stretches? And the deviation squeeze at states with I_tau = {} (note docs/si/N5-ITAU-box62.md).
  STEPS     tau-stretch transitions (tau_(k+1) = tau_k).   ITNE   those whose state k has I_tau != {} (S4b ran and kept tau).
  ITNE_NOFB of them not a fallback.   STATES0  stretch states k with I_tau = {}.
  DEV       (state, Odd o) with o in D_k (sigma-bar_k(o) != tau(o)) at stretch states with I_tau = {}.
  SQV       violations of the dual-side inequality at those deviations: Xi^d(x) at least Xi^d(tau(o)) for Even, x = sigma-bar(o) (definitional
            from I_tau = {}: expected 0).   XIV  violations of Xi(x) <= Xi(tau(o)) (R57: expected 0).
  STRICTXI  deviations with Xi(x) strictly below Xi(tau(o)) (Odd strictly prefers the escape in Xi);  STRICTD  with Xi^d(x) strictly above
            Xi^d(tau(o)) (the escape strictly worse for Odd under tau-bar). BOTH: both strict (a deviation that I_tau = {} keeps alive only
            because tau-bar values it differently from sigma).
  DEVIT     (state, o) at stretch states with I_tau != {} (tau kept) where the deviation edge (o, sigma-bar(o)) is itself in I_tau;
            DEVIT_ST  such states.  ITNE_W / DEVIT_W: the same restricted to W-run transitions (anc.py's runs).
Usage: itau.py GAME.pg [START]."""
import sys, io, contextlib, os
ANC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "anc.py")
argv = sys.argv[1:]
sys.argv = [ANC] + argv
g = {'__file__': ANC, '__name__': 'x'}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(open(ANC).read(), ANC, 'exec'), g)
S, X, B, TAU, FB, own, n, E, Ed, K_ = g['S'], g['X'], g['B'], g['TAU'], g['FB'], g['own'], g['n'], g['E'], g['Ed'], g['K']
Kk, Kd = (lambda v: E.key(v)), (lambda v: Ed.key(v))
VT = {}
def dual(k):
    t = TAU[k]
    if t not in VT:
        vt = Ed.evaluate(t)[0]; VT[t] = (vt, set(Ed.improving(t, vt)))
    return VT[t]
T = dict(STEPS=0, ITNE=0, ITNE_NOFB=0, STATES0=0, DEV=0, SQV=0, XIV=0, STRICTXI=0, STRICTD=0, BOTH=0, DEVIT=0, DEVIT_ST=0, ITNE_W=0, DEVIT_W=0)
for k in range(K_):
    if TAU[k + 1] != TAU[k]: continue
    T['STEPS'] += 1; vt, it = dual(k); tau = TAU[k]
    if it:
        T['ITNE'] += 1; T['ITNE_NOFB'] += not FB[k]
        dv = [o for o in range(n) if own[o] == 1 and B[k][o] != tau[o] and (o, B[k][o]) in it]
        T['DEVIT'] += len(dv); T['DEVIT_ST'] += bool(dv)
        if k in g['runof']: T['ITNE_W'] += 1; T['DEVIT_W'] += bool(dv)
        continue
    T['STATES0'] += 1
    for o in range(n):
        if own[o] != 1 or B[k][o] == tau[o]: continue
        x, t = B[k][o], tau[o]; T['DEV'] += 1
        # dual valuations are ordered for the dual's Even player (= Odd of G): larger Kd = better for Odd.
        if Kd(vt[x]) > Kd(vt[t]): T['SQV'] += 1
        if Kk(X[k][x]) > Kk(X[k][t]): T['XIV'] += 1
        sx, sd = Kk(X[k][x]) < Kk(X[k][t]), Kd(vt[x]) < Kd(vt[t])
        T['STRICTXI'] += sx; T['STRICTD'] += sd; T['BOTH'] += sx and sd
print("ITAU", os.path.basename(argv[0]), " ".join(f"{a} {b}" for a, b in T.items()))
