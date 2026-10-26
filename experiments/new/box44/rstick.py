#!/usr/bin/env python3
"""Box 44 DATA for R-STICK_D / SN-PREFIX_D (docs/new/N5-FBF-box44.md §12). D_k, R_D as in R55 (P-N5-GD). W_k := valuation of sigma_k in
G_tau; lambda := honest cycle-node map; a vertex v is SPLIT at k if lambda_W(v) != lambda(v). Per phase ((lambda, tau) constant):
  RS    at every S4a transition s -> s+1: every split v in R_D(s) lies in R_D(s+1)                     (R-STICK_D; viol. RS_V)
  SP    along every run of consecutive in-phase S4a transitions, once v is split it stays split        (SN-PREFIX_D; viol. SP_V)
  X     crossings := in-phase transitions with R_D(s) != R_D(s+1); XSN := those at which some UNSPLIT vertex (at s) changes membership;
        bound X <= (f + 1) * n + f + XSN                                                             (Corollary; viol. XB_V)
  QC    XSN transitions at which a membership-changing unsplit vertex has an Odd-choice honest cycle node (TOGGLE's failure point)
Usage: rstick.py --list FILE | --rand C LO HI SEED | files"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box43")); sys.path.insert(0, HERE)
from multi import rand_ckO, pg
from n5x import load, step, start_pair, Engine, dual
from dset import meets
C = dict(phases=0, RS_n=0, RS_V=0, SP_V=0, XMAX=0, XSNMAX=0, XSN_tot=0, X_tot=0, XB_V=0, QC=0, XSN_front=0)
def check(g, cap=4000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, None); rows = []
    Q = {v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2}
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s))
        D = frozenset(u for u in range(g.n) if g.owner[u] == 1 and sb[u] != t[u]); R = set(meets(g, s, t, D))
        gt = pg.Game(list(g.prio), list(g.owner), [list(g.succ[v]) if g.owner[v] == 0 else [t[v]] for v in range(g.n)])
        W, _ = Engine(gt).evaluate(tuple(s[v] if g.owner[v] == 0 else -1 for v in range(g.n)))
        lam = tuple(x[0] for x in vs); split = {v for v in range(g.n) if W[v][0] != lam[v]}
        r = step(g, E, Ed, s, t)
        rows.append((lam, tuple(t), R, split, r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1][:2] == rows[i][:2]: j += 1
        C["phases"] += 1; f = sum(1 for k in range(i, j) if rows[k][4]); X = XSN = 0
        for k in range(i, j):
            a, b = rows[k], rows[k + 1]
            if not a[4]:
                for v in a[3]:
                    if v in a[2]:
                        C["RS_n"] += 1; C["RS_V"] += v not in b[2]
                    if v not in b[3]: C["SP_V"] += 1
            if a[2] != b[2]:
                X += 1; chg = a[2] ^ b[2]; uns = [v for v in chg if v not in a[3]]
                if uns:
                    XSN += 1
                    if any(a[0][v] in Q for v in uns): C["QC"] += 1
        C["XMAX"] = max(C["XMAX"], X); C["XSNMAX"] = max(C["XSNMAX"], XSN); C["X_tot"] += X; C["XSN_tot"] += XSN
        if X > (f + 1) * g.n + f + XSN: C["XB_V"] += 1
        i = j + 1
if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--list":
        R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [load(os.path.join(R0, l.split()[0])) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    elif a[0] == "--rand":
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        gs = [g for g in (rand_ckO(rng, lo, hi, rng.randint(2, 4)) for _ in range(cnt)) if g is not None]
    else: gs = [load(f) for f in a]
    for g in gs: check(g)
    print(f"runs {len(gs)}: " + ", ".join(f"{k} {v}" for k, v in C.items()))
