#!/usr/bin/env python3
"""Box 45 DATA for premise (Στ) (docs/new/N5-EPR-box45.md §4): at in-phase states k with u in D_k, is (u, sigma-bar_k(u)) in I_tau_k?
Counts IT1 (such states, any |D|) and among them WXI (W_k = Xi_k everywhere) and NOTAU (G's S4b output != tau: impossible in-phase).
Usage: itcheck.py STARTS SEED (--list FILE | --rand C LO HI GSEED)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "box43")); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from multi import rand_ckO
from n5x import load, step, start_pair, Engine, dual, pg
C = dict(runs=0, inphase_D=0, IT1=0, IT1_D1=0, WXI=0, WXI_D1=0)
def wval(g, s, t):
    succ = [[t[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(g.n)]
    return Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(tuple(s))[0]
def check(g, start, cap=4000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); C["runs"] += 1
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]
    for _ in range(cap):
        vs, sb = E.evaluate(tuple(s)); vt, _ = Ed.evaluate(tuple(t)); It = set(Ed.improving(tuple(t), vt))
        r = step(g, E, Ed, s, t)
        if r is None: break
        D = [q for q in Q if sb[q] != t[q]]
        lam0 = tuple(x[0] for x in vs); vs1, _ = E.evaluate(tuple(r[0]))
        inph = list(r[1]) == list(t) and tuple(x[0] for x in vs1) == lam0
        if inph and D:
            C["inphase_D"] += 1
            hit = [u for u in D if (u, sb[u]) in It]
            if hit:
                C["IT1"] += 1; C["IT1_D1"] += len(D) == 1
                if list(wval(g, s, t)) == list(vs): C["WXI"] += 1; C["WXI_D1"] += len(D) == 1
        s, t = r[0], r[1]
if __name__ == "__main__":
    a = sys.argv[1:]; K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    if a[0] == "--list":
        R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [load(os.path.join(R0, l.split()[0])) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    else:
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        gs = [g for g in (rand_ckO(rng, lo, hi, rng.randint(2, 4)) for _ in range(cnt)) if g is not None]
    for g in gs:
        if g.n > 64: continue
        for st in [None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                             {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]:
            try: check(g, st)
            except RecursionError: pass
    print(", ".join(f"{k} {v}" for k, v in C.items()))
