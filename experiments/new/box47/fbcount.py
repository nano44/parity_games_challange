#!/usr/bin/env python3
"""Box 47 DATA for the fallback count f (docs/new/N5-FB-box47.md): per phase, classify every in-phase S4c fallback t -> t+1 by FB-RISE's terms
(LEV, LEV_odd: docs/new/P-N5-HONFF-box47.md §0):
  NB   LEV(t) < n-1 and LEV_odd(t) > LEV(t)   (FB-RISE (a): LEV rises; at most n-1 per phase, PROVED)
  OB   LEV(t) < n-1 and LEV_odd(t) <= LEV(t)  (Odd-binding)
  SAT  LEV(t) = n-1
Checks NB_V (LEV(t+1) <= LEV(t) at an NB fallback: must be 0) and NBC_V (#NB > n-1 in a phase: must be 0). For each OB fallback:
  BIND   the binding Odd vertices q (Xi_t(q) < value(r) for some G_tau path r from q with <= LEV(t)+1 edges): in D_t? (BIND_NOTD counts q not in D)
  RHO    some Xi(q), q in Q, changed since the previous fallback of the phase (or the phase start): a rho event to charge it to
  RHOB   some binding q changed Xi since the previous fallback
  EPO    sigma-bar|Q changed since the previous fallback (an epoch boundary between them)
Per phase also: rho := transitions changing Xi(q) for some q in Q; LEV_odd changes. Reports max f, max OB, totals, and max of
OB - (#phase transitions with a rho event) (OB charged to rho events one-to-one fails if > 0: CHARGE_V).
Usage: fbcount.py STARTS SEED (--list FILE | --rand C LO HI GSEED | files) [--nmax N] [--budget B] [--start F]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
for p in ("../box46", "../box43", "../box21"): sys.path.insert(0, os.path.join(HERE, p))
from fbwlev import wlev
from ffdeep import levsub
from levels import load, step, start_pair, Engine, dual, rand_ckO, Unknown
from n5x import readstart
C = {}; M = {}
def inc(k, v=1): C[k] = C.get(k, 0) + v
def mx(k, v, tag=None):
    if v > M.get(k, (-1,))[0]: M[k] = (v, tag)
VERB = os.environ.get("VERB") == "1"

def binders(E, g, frame, xi, lam, L, budget):
    """Odd q with Xi(q) < value(r) for a simple G_tau path r from q (<= L+1 edges) to a cycle node of lam."""
    n = g.n; pred = [[] for _ in range(n)]
    for v in range(n):
        for z in frame[v]: pred[z].append(v)
    out = set(); cnt = 0
    for c in [c for c in range(n) if lam[c] == c]:
        rc = E.rank[c]; stack = [(c, 0, 0, 1 << c)]
        while stack:
            x, mask, ln, vis = stack.pop(); cnt += 1
            if cnt > budget: raise Unknown()
            if g.owner[x] == 1 and ln >= 1 and E.key((c, mask, ln)) > E.key(xi[x]): out.add(x)
            if ln >= L + 1: continue
            for p in pred[x]:
                if vis >> p & 1: continue
                stack.append((p, mask | (E.bit[p] if E.rank[p] > rc else 0), ln + 1, vis | 1 << p))
    return out

def run(g, start, budget, nm, cap=3000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []; inc("runs")
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        rows.append(dict(lam=tuple(x[0] for x in vs), t=tuple(t), xi=vs, sb=tuple(sb), fb=r[4] if r else 0,
                         D=frozenset(q for q in Q if sb[q] != t[q])))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and (rows[j + 1]["lam"], rows[j + 1]["t"]) == (rows[i]["lam"], rows[i]["t"]): j += 1
        if any(rows[k]["fb"] for k in range(i, j)):
            try: phase(g, E, rows, i, j, Q, budget, nm, start)
            except Unknown: inc("UNK_phases")
        i = j + 1

def phase(g, E, rows, a, b, Q, budget, nm, start):
    n = g.n; lam = rows[a]["lam"]; tau = rows[a]["t"]
    frame = [[tau[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(n)]
    rho_t = [any(rows[k]["xi"][q] != rows[k + 1]["xi"][q] for q in Q) for k in range(a, b)]
    f = nb = ob = sat = 0; prev = a; lodd_prev = None; lodd_ch = 0
    for t in range(a, b):
        if not rows[t]["fb"]: continue
        f += 1
        L = wlev(E, g, frame, rows[t]["xi"], lam, budget); Lo = levsub(E, g, frame, rows[t]["xi"], lam, budget, 1)
        if lodd_prev is not None and Lo != lodd_prev: lodd_ch += 1
        lodd_prev = Lo
        if L >= n - 1: sat += 1; inc("SAT")
        elif Lo > L:
            nb += 1; inc("NB")
            if wlev(E, g, frame, rows[t + 1]["xi"], lam, budget) <= L: inc("NB_V")
        else:
            ob += 1; inc("OB")
            B = binders(E, g, frame, rows[t]["xi"], lam, L, budget)
            if any(q not in rows[t]["D"] for q in B): inc("BIND_NOTD")
            if not B: inc("BIND_EMPTY")
            rh = any(rho_t[k - a] for k in range(prev, t)); inc("RHO", rh)
            rb = any(rows[k]["xi"][q] != rows[k + 1]["xi"][q] for k in range(prev, t) for q in B); inc("RHOB", rb)
            ep = any(tuple(rows[k]["sb"][q] for q in Q) != tuple(rows[k + 1]["sb"][q] for q in Q) for k in range(prev, t)); inc("EPO", ep)
            if not rh: inc("OB_NORHO")
            if not rh and not ep: inc("OB_NORHO_NOEPO")
            if VERB and not rh:
                print(f"OB_NORHO {nm} {'S3' if start is None else 'rand'} phase [{a},{b}] fallback {t} prev {prev} LEV {L} LEVodd {Lo} "
                      f"binders {sorted(B)} D {sorted(rows[t]['D'])} epoch-change {int(ep)}", flush=True)
        prev = t + 1
    inc("phases_with_fb"); inc("f", f)
    if nb > n - 1: inc("NBC_V")
    mx("f_max", f, (nm, n)); mx("OB_max", ob, (nm, n)); mx("SAT_max", sat, (nm, n))
    mx("OB_minus_rhoT", ob - sum(rho_t), (nm, n))
    if ob > sum(rho_t): inc("CHARGE_V")

if __name__ == "__main__":
    a = sys.argv[1:]; nmax, budget = 34, 1000000; fixed = None
    if "--nmax" in a: i = a.index("--nmax"); nmax = int(a[i + 1]); del a[i:i + 2]
    if "--budget" in a: i = a.index("--budget"); budget = int(a[i + 1]); del a[i:i + 2]
    if "--start" in a: i = a.index("--start"); fixed = readstart(a[i + 1]); del a[i:i + 2]
    K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    if a[0] == "--list":
        R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [(l.split()[0], load(os.path.join(R0, l.split()[0]))) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    elif a[0] == "--rand":
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        gs = [(f"rand{i}", g) for i, g in enumerate(rand_ckO(rng, lo, hi, rng.randint(2, 4)) for _ in range(cnt)) if g is not None]
    else: gs = [(f, load(f)) for f in a]
    for nm, g in gs:
        if g.n > nmax: continue
        sts = [fixed] if fixed else [None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                                {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]
        for st in sts:
            try: run(g, st, budget, nm)
            except RecursionError: inc("RECERR")
    print(" ".join(f"{k} {v}" for k, v in sorted(C.items())))
    print(" ".join(f"{k} {v[0]} {v[1]}" for k, v in sorted(M.items())))
