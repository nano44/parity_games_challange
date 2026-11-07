"""Box 61 probe: blocked and unblocked edges inside tau-stretches (L-NEW box 118's INC). Per state k of a tau-stretch (tau constant over the
stretch's transitions): Is_k = N5's improving edges (SPEC S2, Xi), IW_k = G_tau's improving edges of sigma_k (W against tau).
An Even edge e = (y, z) is BLOCKED at k if e in IW_k minus Is_k. It is UNBLOCKED at k + 1 if blocked at k and e in Is_(k+1); the unblock KEY is
key(Xi_(k+1)(z), Xi_(k+1)(sigma_(k+1)(y))) (the level at which z now beats y's current target in Xi).
  STEPS      transitions inside tau-stretches (tau_(k+1) = tau_k);  INC  of them with Is_k != IW_k or a fallback (L-NEW's count).
  BLK        (edge, state) blocked incidences.  UNB  unblock events.  UNBK  distinct (edge, key) pairs among a stretch's unblocks (summed).
  MAXREP     max unblocks of ONE (edge, key) in one stretch (the Lead's ideal charge needs this bounded by a constant).
  MAXUNB_E   max unblocks of one edge in one stretch.  MAXINC  max INC in one stretch.  NOUNB  inconsistent steps k with no unblock at k + 1.
  MAXGAP     longest window of consecutive stretch transitions k with no unblock at k + 1.
  XIUP       unblocks at which Xi(z) changed at k (z's side moved);  SRCDN  unblocks with Xi(z) unchanged (only y's target side moved: by
             SUCC-MONO Xi of the target never falls, so SRCDN means y switched to a worse-or-equal-in-Xi target? expected 0).
  UNBKCH     unblocks whose key exceeds every key of Xi(z)-changes since the edge became blocked (KEY-RETURN-type charge fails): expected 0.
Usage: unblock.py [-v] GAME.pg [START]."""
import sys, io, contextlib, os
from collections import Counter
ANC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "anc.py")
argv = sys.argv[1:]
VERB = '-v' in argv
if VERB: argv.remove('-v')
sys.argv = [ANC] + argv
g = {'__file__': ANC, '__name__': 'x'}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(open(ANC).read(), ANC, 'exec'), g)
S, X, KEY, IS, TAU, FB, Wv, own, n, E, key, gm, K_ = g['S'], g['X'], g['KEY'], g['IS'], g['TAU'], g['FB'], g['Wv'], g['own'], g['n'], g['E'], g['key'], g['g'], g['K']
Kk = lambda v: E.key(v)
IS = list(IS) + [set()] * (K_ + 1 - len(IS))   # final state: no improving edge (S5)
def IW(k, tau):
    w = Wv(k, tau)
    return {(y, z) for y in range(n) if own[y] == 0 for z in gm.succ[y] if z != S[k][y] and Kk(w[z]) > Kk(w[S[k][y]])}
# tau-stretches: maximal windows of transitions k with TAU[k+1] == TAU[k]
stretches, cur = [], None
for k in range(K_):
    if TAU[k + 1] != TAU[k]: cur = None; continue
    if cur is None: cur = []; stretches.append(cur)
    cur.append(k)
T = dict(STEPS=0, INC=0, BLK=0, UNB=0, UNBK=0, MAXREP=0, MAXUNB_E=0, MAXINC=0, NOUNB=0, MAXGAP=0, XIUP=0, SRCDN=0, UNBKCH=0)
EX = []
for st in stretches:
    tau = TAU[st[0]]; iw = {k: IW(k, tau) for k in st + [st[-1] + 1]}
    blk = {k: iw[k] - IS[k] for k in iw}
    rep, pe, inc, gap = Counter(), Counter(), 0, 0
    since = {}
    for k in st:
        T['STEPS'] += 1
        bad = FB[k] or IS[k] != iw[k]
        inc += bool(bad); T['BLK'] += len(blk[k])
        for e in blk[k]:
            since.setdefault(e, k)
        unb = [e for e in blk[k] if e in IS[k + 1]]
        if bad and not unb: T['NOUNB'] += 1
        gap = 0 if unb else gap + 1; T['MAXGAP'] = max(T['MAXGAP'], gap)
        for (y, z) in unb:
            kk = key(X[k + 1][z], X[k + 1][S[k + 1][y]])
            T['UNB'] += 1; rep[((y, z), kk)] += 1; pe[(y, z)] += 1
            if KEY[k][z] is not None: T['XIUP'] += 1
            else: T['SRCDN'] += 1
            chs = [KEY[u][z] for u in range(since[(y, z)], k + 1) if KEY[u][z] is not None]
            if not chs or max(chs) < kk: T['UNBKCH'] += 1
            since.pop((y, z), None)
        for e in list(since):
            if e not in blk[k + 1] and e not in unb: since.pop(e)
    T['INC'] += inc; T['MAXINC'] = max(T['MAXINC'], inc); T['UNBK'] += len(rep)
    if rep:
        T['MAXREP'] = max(T['MAXREP'], max(rep.values())); T['MAXUNB_E'] = max(T['MAXUNB_E'], max(pe.values()))
        if VERB:
            (e, kk), c = rep.most_common(1)[0]; EX.append(('TOPREP', 'stretch', st[0], st[-1], 'edge', e, 'key', kk, 'count', c))
for e in EX[:3]: print(*e)
print("UNBLOCK", os.path.basename(argv[0]), " ".join(f"{a} {b}" for a, b in T.items()))
