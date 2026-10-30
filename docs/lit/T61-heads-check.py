#!/usr/bin/env python3
"""L-LIT T61 (docs/lit/T61-order-charging.md §4): the Gimbert-Horn / Auger et al. order-charging template read on N5's upward heads.
W-runs as in docs/lit/T59-dz-check.py (tau fixed, no fallback, W's cycle nodes fixed). Per state k of a W-run:
  U_k := {sigma-bar_k(g) : g Odd, sigma-bar_k(g) != tau(g)} | {the Xi-successor of c : c in C}   (L-RED R143's upward heads; C := W-cycle
         nodes, the Xi-successor of c is sigma_k(c) for Even c and sigma-bar_k(c) for Odd c);
  ORD_k := (U_k, the weak order of Xi_k on U_k)                          (the [GH]/[ABS] datum: which head set, in which order);
  TYP_k := (U_k, ORD, and for each pair of heads the level at which their Xi-values first differ: the cycle node if it differs,
            else the top rank of the symmetric difference of the path sets, else 'len')  (the ordered-ultrametric type, T61 §3).
Reports maxima over W-runs: LEN, UMAX = max_k |U_k|, NORD / NTYP = distinct ORD_k / TYP_k in the run, SBT = transitions at which
sigma-bar changes anywhere, ORDREP / TYPREP = the number of states whose ORD / TYP already occurred EARLIER in the run with a DIFFERENT
sigma-bar (0 means sigma-bar is a function of ORD / TYP on that run); ORDRET / TYPRET = the number of states whose ORD / TYP
occurred earlier in the run but not at the previous state (a RETURN: the [GH] no-repeat property fails exactly when this is > 0).
Usage (repo root): python3 -I docs/lit/T61-heads-check.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
import importlib.util
def _load(name, fn):
    sp = importlib.util.spec_from_file_location(name, os.path.join(HERE, fn)); m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m); return m
t59 = _load("t59", "T59-dz-check.py")
from n5x import load, readstart, Engine
import pg

def run(g, start=None):
    n = g.n; own = g.owner; E = Engine(g)
    c = dict(RUNS=0, LEN=0, UMAX=0, NORD=0, NTYP=0, SBT=0, ORDREP=0, TYPREP=0, ORDRET=0, TYPRET=0)
    for F, tau in t59.wruns_t(g, start):
        if len(F) < 2: continue
        c['RUNS'] += 1; c['LEN'] = max(c['LEN'], len(F) - 1)
        Ew = Engine(pg.Game(list(g.prio), list(g.owner), [[tau[v]] if own[v] == 1 else list(g.succ[v]) for v in range(n)]))
        lamW = [w for (w, _, _) in Ew.evaluate(F[0])[0]]; C = [v for v in range(n) if lamW[v] == v]
        seen_o, seen_t = {}, {}; prev = None; nord, ntyp = set(), set(); po = pt = None
        for s in F:
            val, sb = E.evaluate(s); sbt = tuple(sb[v] if own[v] == 1 else -1 for v in range(n))
            U = {sb[o] for o in range(n) if own[o] == 1 and sb[o] != tau[o]} | {(s[x] if own[x] == 0 else sb[x]) for x in C}
            U = sorted(U); c['UMAX'] = max(c['UMAX'], len(U))
            K = {u: E.key(val[u]) for u in U}
            ordk = (tuple(U), tuple(sorted(range(len(U)), key=lambda i: (K[U[i]], i))),
                    tuple(K[U[i]] == K[U[i + 1]] for i in range(len(U) - 1)))
            lev = []
            for i in range(len(U)):
                for j in range(i + 1, len(U)):
                    (w1, p1, l1), (w2, p2, l2) = val[U[i]], val[U[j]]
                    lev.append(('c', E.rank[w1], E.rank[w2]) if w1 != w2 else (((p1 ^ p2).bit_length(),) if p1 != p2 else ('len',)))
            typ = (ordk, tuple(lev))
            nord.add(ordk); ntyp.add(typ)
            if ordk in seen_o and seen_o[ordk] != sbt: c['ORDREP'] += 1
            if typ in seen_t and seen_t[typ] != sbt: c['TYPREP'] += 1
            if ordk in seen_o and ordk != po: c['ORDRET'] += 1
            if typ in seen_t and typ != pt: c['TYPRET'] += 1
            po, pt = ordk, typ
            seen_o.setdefault(ordk, sbt); seen_t.setdefault(typ, sbt)
            if prev is not None and prev != sbt: c['SBT'] += 1
            prev = sbt
        c['NORD'] = max(c['NORD'], len(nord)); c['NTYP'] = max(c['NTYP'], len(ntyp))
    return c

if __name__ == '__main__':
    a = sys.argv[1:]; g = load(a[0]); c = run(g, readstart(a[1]) if len(a) > 1 else None)
    print(f"T61 {os.path.basename(a[0])} n {g.n} " + " ".join(f"{k} {v}" for k, v in c.items()))
