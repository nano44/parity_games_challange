#!/usr/bin/env python3
"""L-NEW box 97 (docs/new/N5-ORD-box97.md): ORDER-DET and NO-REPEAT (L-LIT T60 §3.3) on the W-runs of N5.
W-run segmentation as box92/xirun.py (tau fixed, no S4c fallback, lambda_W fixed). Per state k of a W-run F:
  Xi_k, sbar_k := E.evaluate(sigma_k); C := {v : lambda_W(v) = v}; D_k := {Odd o : sbar_k(o) != tau(o)};
  U_k := {sbar_k(g) : g in D_k} u {Xi-successor of c : c in C} (L-RED R143 verbatim);
  O_F := the Odd vertices whose sbar changes in F;  A_F := U_F u tau(O_F), U_F := the union of the U_k over F (a FIXED set);
  NON-OWN o at k: the cycle node of Xi_k(o) is not o (L-SI box 53).
  refined key r_k(t) := (E.key(Xi_k(t)), tb_k(t)), tb = (index,) if the cycle node of Xi_k(t) is even, else key_k(t) = t's
  (sigma_k, sbar_k)-path to its cycle node read from the cycle-node end (L-SI box 53 SEL). Odd prefers the smaller r_k.
Checks (counts over W-runs; a violation of an exact claim is a kill):
  REFMINX  non-own o in O_F with sbar_k(o) != the r_k-least element of succ(o) n A_F   (Lemma ORDER-DET-R, claimed PROVED: must be 0)
  REFMINUX non-own Odd o with sbar_k(o) != the r_k-least element of succ(o) n U'_k, U'_k := U_k u tau(Odd)  (ORDER-DET-U', must be 0)
  ODU      ORDER-DET, T60 literal U-form: two states of F with equal (U_k, <=-preorder of Xi_k on U_k) and different sbar at an Odd
           vertex non-own at both (a conflict = a kill of the U-form)
  ODA      the same for the <=-preorder of Xi_k on A_F (kill of the unrefined A-form)
  ODR      the same for the refined order on A_F (must be 0 by ORDER-DET-R)
  NRU/NRA/NRR  NO-REPEAT: W-runs whose compressed sequence of U-form / A-form / refined orders revisits an earlier order
  NRRS     W-runs where the refined order revisits an order with a sbar change in between (the case NO-REPEAT must exclude)
  Stats: W-runs, max |F|, max |U_k|, max |A_F|, max sbar-change transitions per W-run (SBT), max distinct refined orders per W-run.
Usage: orderdet.py GAME.pg [START]   (VERBOSE=1 prints the first witness of each kind; PERRUN=1 prints one line per W-run:
  F, max |U_k|, |A_F|, |O_F|, SBT, ORDCH = refined-order changes, ORD = distinct refined orders)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
VB = os.environ.get('VERBOSE') == '1'; PR = os.environ.get('PERRUN') == '1'
g = load(sys.argv[1]); start = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); S = [tuple(s)]; TAU = [tuple(t)]; FB = []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
T = len(S) - 1; ODD = [o for o in range(n) if own[o] == 1]; SU = [sorted(set(x)) for x in g.succ]
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(g.owner), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
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
        if len(p) > n + 1: raise RuntimeError("no cycle node")
    return p
def rkey(k, y):
    val = EV(k)[0][y]
    return (E.key(val), (y,) if E.par[val[0]] == 0 else tuple(reversed(path(k, y)[:-1])))
def prerank(k, X):
    ks = [E.key(EV(k)[0][x]) for x in X]; srt = sorted(set(ks))
    return tuple(srt.index(q) for q in ks)
c = dict(STATES=len(S), WRUNS=len(runs), REFMINX=0, REFMINUX=0, ODU=0, ODA=0, ODR=0, NRU=0, NRA=0, NRR=0, NRRS=0)
mx = dict(F=0, U=0, A=0, SBT=0, ORD=0)
wit = {}
def witness(kind, txt):
    if kind not in wit: wit[kind] = txt
for a, b in runs:
    tau = TAU[a]; lw = Wv(a, tau); C = [v for v in range(n) if lw[v][0] == v]
    U = []
    for k in range(a, b + 1):
        val, sb = EV(k)
        u = {sb[o] for o in ODD if sb[o] != tau[o]} | {(S[k][x] if own[x] == 0 else sb[x]) for x in C}
        U.append(frozenset(u))
    OF = [o for o in ODD if len({EV(k)[1][o] for k in range(a, b + 1)}) > 1]
    A = sorted(set().union(*U) | {tau[o] for o in OF})
    mx['F'] = max(mx['F'], b - a); mx['U'] = max(mx['U'], max(len(x) for x in U)); mx['A'] = max(mx['A'], len(A))
    nonown = lambda k, o: EV(k)[0][o][0] != o
    seen = {'U': {}, 'A': {}, 'R': {}}; seq = {'U': [], 'A': [], 'R': []}; sbt = 0
    for k in range(a, b + 1):
        val, sb = EV(k)
        if k > a and any(EV(k - 1)[1][o] != sb[o] for o in ODD): sbt += 1
        Up = U[k - a] | {tau[o] for o in ODD}
        for o in ODD:
            if nonown(k, o) and sb[o] != min((x for x in SU[o] if x in Up), key=lambda x: rkey(k, x)):
                c['REFMINUX'] += 1; witness('REFMINUX', f"k {k} o {o}")
        for o in OF:
            if nonown(k, o):
                best = min((x for x in SU[o] if x in set(A)), key=lambda x: rkey(k, x))
                if best != sb[o]:
                    c['REFMINX'] += 1; witness('REFMINX', f"k {k} o {o} sbar {sb[o]} refmin {best}")
        Uk = sorted(U[k - a])
        keys = {'U': (tuple(Uk), prerank(k, Uk)), 'A': prerank(k, A), 'R': tuple(sorted(A, key=lambda x: rkey(k, x)))}
        nb = {o: sb[o] for o in ODD if nonown(k, o)}
        for typ, kk in keys.items():
            if kk in seen[typ]:
                k0, nb0 = seen[typ][kk]
                bad = [o for o in nb if o in nb0 and nb0[o] != nb[o]]
                if bad:
                    c['OD' + typ] += 1; witness('OD' + typ, f"states {k0},{k} o {bad[0]} sbar {nb0[bad[0]]}->{nb[bad[0]]} |U| {len(Uk)}")
            else: seen[typ][kk] = (k, nb)
            if not seq[typ] or seq[typ][-1][0] != kk: seq[typ].append((kk, k))
    mx['SBT'] = max(mx['SBT'], sbt); mx['ORD'] = max(mx['ORD'], len({x for x, _ in seq['R']}))
    if PR: print(f"  RUN {a}-{b} F {b - a} maxU {max(len(x) for x in U)} A {len(A)} OF {len(OF)} SBT {sbt} ORDCH {len(seq['R']) - 1} ORD {len({x for x, _ in seq['R']})}")
    for typ in 'UAR':
        first = {}; hit = False; hits = False
        for kk, k in seq[typ]:
            if kk in first:
                hit = True
                k0 = first[kk]
                if any(EV(q)[1] != EV(k0)[1] for q in range(k0, k + 1)): hits = True
                if typ == 'R' and hits: witness('NRRS', f"run {a}-{b}: refined order at state {k0} recurs at {k}")
                witness('NR' + typ, f"run {a}-{b}: order at state {k0} recurs at {k} |U| {len(U[k - a])} |A| {len(A)}")
            else: first[kk] = k
        c['NR' + typ] += hit
        if typ == 'R': c['NRRS'] += hits
print(f"ORDDET {os.path.basename(sys.argv[1])} n {n} " + " ".join(f"{k} {v}" for k, v in c.items()) + " max " + " ".join(f"{k} {v}" for k, v in mx.items()))
if VB:
    for k, v in wit.items(): print(f"  WIT {k}: {v}")
