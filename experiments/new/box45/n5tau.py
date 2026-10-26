#!/usr/bin/env python3
"""Box 45 DATA for premise (Στ) (docs/new/P-N5-EPR-box45.md §3-§4): run N5^tau (S4b keeps tau when tau is value-optimal in its arena)
on 𝒞^1O games and check the per-phase fallback bound of RESULTS R48 (i), f <= 1 + (n - 2)(2n - 1), on every N5^tau phase.
Counts: TIEKEEP (iterations where N5^tau keeps tau although SPEC's S4b would move it: N5 and N5^tau differ there), FB_V (R48 (i) violated),
max f per phase, max phase length (transitions), phases. Usage: n5tau.py STARTS SEED (--list FILE | --rand C LO HI GSEED | files)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "box43")); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from multi import rand_ckO
from n5x import load, start_pair, Engine, dual
from eprestrict import step_tau
C = dict(runs=0, phases=0, TIEKEEP=0, TIEPH=0, FB_V=0, FMAX=0, LMAX=0, LMAX_n=0)
def check(g, start, cap=20000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); C["runs"] += 1; n = g.n
    lam = tuple(x[0] for x in E.evaluate(tuple(s))[0]); f = L = 0; tie = 0
    for _ in range(cap):
        r = step_tau(g, E, Ed, s, t)
        if r is None: break
        ns, nt, fb, moved = r; lam1 = tuple(x[0] for x in E.evaluate(tuple(ns))[0])
        if moved == "tie": C["TIEKEEP"] += 1; tie = 1
        if list(nt) == list(t) and lam1 == lam:
            L += 1; f += fb
        else:
            close(n, f, L, tie); f = L = tie = 0
        s, t, lam = ns, nt, lam1
    close(n, f, L, tie)
def close(n, f, L, tie):
    C["phases"] += 1; C["TIEPH"] += tie; C["FMAX"] = max(C["FMAX"], f)
    if L > C["LMAX"]: C["LMAX"], C["LMAX_n"] = L, n
    if f > 1 + (n - 2) * (2 * n - 1) and n >= 2: C["FB_V"] += 1
if __name__ == "__main__":
    a = sys.argv[1:]; K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    if a[0] == "--list":
        R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [load(os.path.join(R0, l.split()[0])) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    elif a[0] == "--rand":
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        gs = [g for g in (rand_ckO(rng, lo, hi, 1) for _ in range(cnt)) if g is not None]
    else: gs = [load(f) for f in a]
    gs = [g for g in gs if sum(1 for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1) == 1 and g.n <= 64]
    for g in gs:
        for st in [None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                             {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]:
            try: check(g, st)
            except RecursionError: pass
    print(f"games {len(gs)}: " + ", ".join(f"{k} {v}" for k, v in C.items()))
