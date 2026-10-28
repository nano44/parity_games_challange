#!/usr/bin/env python3
"""L-NEW box 49 (successor 30), DATA for docs/new/N5-READER-box49.md §6: the W*-potential on fallback-free runs. For a phase with Odd strategy
τ, W* := the valuation of Even's optimum σ* in the one-player game G_τ (S1's procedure on the dual of G with Odd fixed to τ, exactly as
n5x.step builds S4a's arena game, with all edges). F_t := {v : W_t(v) = W*(v)}. W is non-decreasing on a fallback-free run (wamort.py WMONO)
and W_t ⊴ W* (σ* optimal), so F_t only grows: CHECKED here (FSHRINK). STALL counts the transitions of fallback-free runs at which F does not
grow; if STALL were 0, a fallback-free run would have at most n transitions.
Usage: wstar.py STARTS SEED (--list FILE | files) [--nmax N]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root")); sys.path.insert(0, HERE)
from common import rows, phases, load, readstart, wplay
from wamort import runs_of
import pg
from n5x import Engine, dual
from collections import Counter
C = Counter(); MAX = {}
def mx(k, v, tag):
    if v > MAX.get(k, (-1,))[0]: MAX[k] = (v, tag)

def wstar(g, E, tau):
    n = g.n; succ = [list(g.succ[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
    Er = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ)))
    _, best = Er.evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
    s = [best[v] if g.owner[v] == 0 else tau[v] for v in range(n)]
    W, _ = wplay(E, g, s, tau)
    return [E.key(W[v]) for v in range(n)]

def run(g, st, nm):
    E, R = rows(g, st); n = g.n
    for i, j in phases(R):
        Ws = wstar(g, E, R[i]["t"])
        for a, b in runs_of(R, i, j):
            L = b - a; C["runs_ff"] += 1; C["L"] += L; stall = 0
            F = [{v for v in range(n) if E.key(R[k]["W"][v]) == Ws[v]} for k in range(a, b + 1)]
            for k in range(L):
                if any(E.key(R[a + k]["W"][v]) > Ws[v] for v in range(n)): C["ABOVE_WSTAR"] += 1
                if not F[k] <= F[k + 1]: C["FSHRINK"] += 1
                if len(F[k + 1]) == len(F[k]): stall += 1
            C["STALL"] += stall
            mx("stall_run", stall, (nm, (a, b), n, L)); mx("L_run", L, (nm, (a, b), n))
            mx("frac_stall", stall / L, (nm, (a, b), n, stall, L))

if __name__ == "__main__":
    a = sys.argv[1:]; nmax = 10 ** 9
    if "--nmax" in a: i = a.index("--nmax"); nmax = int(a[i + 1]); del a[i:i + 2]
    K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    files = [os.path.join(ROOT, l.split()[0]) for l in open(a[1]) if l.strip() and not l.startswith("#")] if a[0] == "--list" else a
    for f in files:
        g = load(f)
        if g.n > nmax: continue
        sf = f[:-3] + ".start"
        sts = [readstart(sf) if os.path.exists(sf) else None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                                                  {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]
        for st in sts:
            try: run(g, st, os.path.relpath(f, ROOT)); C["games_runs"] += 1
            except RecursionError: C["RECERR"] += 1
    print(" ".join(f"{k} {v}" for k, v in sorted(C.items())))
    for k, v in sorted(MAX.items()): print("max", k, v)
