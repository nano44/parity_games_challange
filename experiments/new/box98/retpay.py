#!/usr/bin/env python3
"""L-NEW box 98 (docs/new/N5-RET-box98.md): what pays for a RETURN of the head order / type inside a W-run (L-LIT T61 §2.6)?
W-runs as box92/xirun.py; U_k, A_F and the refined order r_k as box97/orderdet.py. Per W-run F:
  an ENTRY is (y, z, k): Even y switches to z at k -> k + 1. It is FRESH if y has not held z at any earlier state of F, else a RETURN
  of the Even edge (y, z) (P-N5-WRUN §4.1's RET_F).
  an ORDER RETURN is a transition k -> k + 1 at which the refined order of A_F becomes one already seen at an earlier state of F (not the
  one at k).
Prints: F, entries, FRESH, RET (Even returns), transitions with no Even return (NORET; each has a fresh entry, so NORET <= m_E),
ORDRET (order returns), ORDRET_NR (order returns whose interval since the previous occurrence of that order contains no Even return),
ORDRET_FR (order returns whose interval contains a fresh entry), and FLIPS (sbar-changing transitions).
Usage: retpay.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); start = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); S = [tuple(s)]; TAU = [tuple(t)]; FB = []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
T = len(S) - 1; ODD = [o for o in range(n) if own[o] == 1]; EV_ = [v for v in range(n) if own[v] == 0]
mE = sum(len(set(g.succ[v])) for v in EV_)
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
runs = []; cur = None
for k in range(T):
    ok = TAU[k + 1] == TAU[k] and not FB[k] and [x[0] for x in Wv(k, TAU[k])] == [x[0] for x in Wv(k + 1, TAU[k])]
    if not ok: cur = None; continue
    if cur is None: cur = [k, k]; runs.append(cur)
    cur[1] = k + 1
EVc = {}
def EV(k):
    if k not in EVc: EVc[k] = E.evaluate(S[k])
    return EVc[k]
def path(k, y):
    val, sb = EV(k); c = val[y][0]; p = [y]; x = y
    while x != c:
        x = S[k][x] if own[x] == 0 else sb[x]; p.append(x)
    return p
def rkey(k, y):
    val = EV(k)[0][y]
    return (E.key(val), (y,) if E.par[val[0]] == 0 else tuple(reversed(path(k, y)[:-1])))
for a, b in runs:
    tau = TAU[a]; lw = Wv(a, tau); C = [v for v in range(n) if lw[v][0] == v]
    U = [frozenset({EV(k)[1][o] for o in ODD if EV(k)[1][o] != tau[o]} | {(S[k][x] if own[x] == 0 else EV(k)[1][x]) for x in C}) for k in range(a, b + 1)]
    OF = [o for o in ODD if len({EV(k)[1][o] for k in range(a, b + 1)}) > 1]
    A = sorted(set().union(*U) | {tau[o] for o in OF})
    ordk = [tuple(sorted(A, key=lambda x: rkey(k, x))) for k in range(a, b + 1)]
    held = {(y, S[a][y]) for y in EV_}; isret = []; fresh = []; ent = 0
    for k in range(a, b):
        mv = [(y, S[k + 1][y]) for y in EV_ if S[k + 1][y] != S[k][y]]; ent += len(mv)
        isret.append(any(e in held for e in mv)); fresh.append(any(e not in held for e in mv)); held |= set(mv)
    seen = {ordk[0]: 0}; ordret = nr = fr = 0
    for k in range(a, b):
        o = ordk[k + 1 - a]
        if o != ordk[k - a] and o in seen:
            ordret += 1; j = seen[o]
            if not any(isret[j:k + 1 - a]): nr += 1
            if any(fresh[j:k + 1 - a]): fr += 1
        seen[o] = k + 1 - a
    flips = sum(1 for k in range(a, b) if any(EV(k)[1][o] != EV(k + 1)[1][o] for o in ODD))
    print(f"RUN {a}-{b} F {b - a} mE {mE} entries {ent} FRESH {sum(fresh)} RET {sum(isret)} NORET {sum(1 for x in isret if not x)} "
          f"ORDRET {ordret} ORDRET_NR {nr} ORDRET_FR {fr} FLIPS {flips} |A| {len(A)}")
