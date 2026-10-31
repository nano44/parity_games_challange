#!/usr/bin/env python3
"""L-NEW box 117: Odd-side separators between N5, TBR and ARSB (box115/abl.py's variants, same VJ engine via box21/n5x.py).
O_k := the Odd strategy Even's step is taken against (N5, TBR: tau_k; ARSB: sigma-bar_k).
Prints per variant: iters; OMV Odd moves; ONI Odd moves (o, O_(k+1)(o)) NOT in Itau(O_k) (dual improving set of O_k on G^d);
DDROP transitions with some v whose dual valuation of O drops (Xi^d_(O_(k+1))(v) <^d Xi^d_(O_k)(v)); ORET Odd returns and ORETBAD
returns of o to x with no strict dual rise of Xi^d(x) between leaving and returning (ODD-RETURN violated);
Even fuel re-routes FR (box115/abl.py's run-level definition) split by whether the pair's previous re-route lies in the same O-stretch.
Usage: sep.py G.pg VARIANT [START] [cap]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); VAR = sys.argv[2]
st = readstart(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3] != "-" else None
cap = int(sys.argv[4]) if len(sys.argv) > 4 else 100000
n = g.n; own = g.owner; E, Ed = Engine(g), Engine(dual(g))
def even_opt(sig, odd, Is):
    opt = {v: {sig[v]} for v in range(n) if own[v] == 0}
    for v, w in Is: opt[v].add(w)
    succ = [sorted(opt[v]) if own[v] == 0 else [odd[v]] for v in range(n)]
    Er = Engine(dual(pg.Game(list(g.prio), list(own), succ)))
    _, best = Er.evaluate(tuple(odd[v] if own[v] == 1 else -1 for v in range(n)))
    return tuple(best[v] if own[v] == 0 else sig[v] for v in range(n))
s0, t0 = start_pair(g, E, Ed, st); S, T, SB = [tuple(s0)], [tuple(t0)], []
while len(S) <= cap:
    sig, tau = S[-1], T[-1]
    vs, sb = E.evaluate(sig); Is = E.improving(sig, vs); SB.append(tuple(sb))
    if VAR == "ARSB":
        if not Is: break
        S.append(even_opt(sig, sb, Is)); T.append(tau)
    elif VAR == "TBR":
        vt, tb = Ed.evaluate(tau); It = Ed.improving(tau, vt)
        if not Is and not It: break
        ns = even_opt(sig, tau, Is) if Is else sig
        nt = tuple(sb[v] if own[v] == 1 else tau[v] for v in range(n))
        if ns == sig and nt == tau: break
        S.append(ns); T.append(nt)
    elif VAR == "N5":
        r = step(g, E, Ed, list(sig), list(tau))
        if r is None: break
        S.append(tuple(r[0])); T.append(tuple(r[1]))
K = len(S) - 1
O = SB[:K + 1] if VAR == "ARSB" else T[:K + 1]
if VAR == "ARSB" and len(O) < K + 1: O.append(tuple(E.evaluate(S[K])[1]))
DV = {}
def dv(k):
    if k not in DV: vt, _ = Ed.evaluate(tuple(O[k][v] if own[v] == 1 else -1 for v in range(n))); DV[k] = (vt, set(Ed.improving(tuple(O[k][v] if own[v] == 1 else -1 for v in range(n)), vt)))
    return DV[k]
OMV = ONI = DDROP = ORET = ORETBAD = 0; held = {}
for k in range(K):
    if O[k + 1] == O[k]: continue
    vt0, It0 = dv(k); vt1, _ = dv(k + 1)
    if any(Ed.key(vt1[v]) < Ed.key(vt0[v]) for v in range(n)): DDROP += 1
    for o in range(n):
        if own[o] != 1 or O[k + 1][o] == O[k][o]: continue
        OMV += 1; x = O[k + 1][o]
        if (o, x) not in It0: ONI += 1
        h = held.setdefault(o, {})
        h[O[k][o]] = k  # o leaves O[k][o] at k
        if x in h:
            ORET += 1
            kl = h[x]  # left x at kl; dual rise of Xi^d(x) strictly between kl and k (states kl .. k)
            if not Ed.key(dv(k)[0][x]) > Ed.key(dv(kl)[0][x]): ORETBAD += 1
# Even fuel re-routes (abl.py definition), split by O-stretch of the previous re-route of the same pair
stretch = [0] * (K + 1)
for k in range(1, K + 1): stretch[k] = stretch[k - 1] + (O[k] != O[k - 1])
XI = {}
def xi(k):
    if k not in XI: vs, _ = E.evaluate(S[k]); XI[k] = (vs, set(E.improving(S[k], vs)))
    return XI[k]
last = {}; FR = IN = CROSS = 0; MAXFR = {}
for k in range(1, K):
    for y in range(n):
        if own[y] != 0 or S[k + 1][y] == S[k][y]: continue
        z = S[k + 1][y]
        if z != S[k - 1][y] and (y, z) not in xi(k - 1)[1] and xi(k - 1)[0][z] != xi(k)[0][z]:
            FR += 1; MAXFR[(y, z)] = MAXFR.get((y, z), 0) + 1
            if (y, z) in last: IN += stretch[last[(y, z)]] == stretch[k]; CROSS += stretch[last[(y, z)]] != stretch[k]
            last[(y, z)] = k
m = max(MAXFR.values()) if MAXFR else 0
print(f"SEP {os.path.basename(sys.argv[1])} {VAR} n {n} iters {K}{' CAPPED' if K >= cap else ''} ostretches {stretch[K] + 1} OMV {OMV} ONI {ONI} DDROP {DDROP} ORET {ORET} ORETBAD {ORETBAD} FR {FR} REIN {IN} RECROSS {CROSS} MAXFR {m}")
