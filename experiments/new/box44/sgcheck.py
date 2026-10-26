#!/usr/bin/env python3
"""Box 44 DATA for Lemma ACCEL (docs/new/N5-FBF-box44.md §8): at every in-phase transition ((lambda_Xi, tau) unchanged), every
switched Even vertex z with lambda(z) != z gains strictly (R19 (d) (SG)); counts switching transitions per phase (ST) and the max
number of distinct kappa-values a single vertex takes in one phase (KV), against n. Usage: sgcheck.py --list FILE | --rand C LO HI SEED | files"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box43")); sys.path.insert(0, HERE)
from multi import rand_ckO
from n5x import load, step, start_pair, Engine, dual
C = dict(trans=0, SG_n=0, SG_V=0, STMAX=0, KVMAX=0)
def check(g, cap=4000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, None); prev = None; st = 0; kv = {}
    while True:
        vs, _ = E.evaluate(tuple(s)); lam = tuple(x[0] for x in vs); key = (lam, tuple(t))
        if prev is not None and key == prev[0]:
            C["trans"] += 1; ps, pvs = prev[1], prev[2]; sw = False
            for z in range(g.n):
                if g.owner[z] == 0 and s[z] != ps[z] and lam[z] != z:
                    sw = True; C["SG_n"] += 1; C["SG_V"] += not (E.key(vs[z]) > E.key(pvs[z]))
            st += sw
        else:
            st = 0; kv = {}
        for z in range(g.n): kv.setdefault(z, set()).add(vs[z])
        C["STMAX"] = max(C["STMAX"], st); C["KVMAX"] = max(C["KVMAX"], max(len(x) for x in kv.values()))
        r = step(g, E, Ed, s, t)
        if r is None or C["trans"] > 10 ** 7: break
        prev = (key, list(s), vs); s, t = r[0], r[1]
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
