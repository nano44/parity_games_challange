#!/usr/bin/env python3
"""Box 43: count S4c fallbacks with BOTH I_sigma and I_tau non-empty ("two-sided fallbacks"): the only place where N5's run on G
and the mirrored run on G^d can differ (Lemma DUAL, docs/new/N5-MULTI-box43.md). DATA.
Usage: dblfb.py --list FILE | --rand COUNT NLO NHI K SEED"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from multi import rand_ckO, pg
from n5x import load, step, start_pair, Engine, dual

def count(g, start=None, cap=5000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); fb = two = it = 0
    while it < cap:
        r = step(g, E, Ed, s, t)
        if r is None: break
        s, t, Is, It, f, _, _ = r; it += 1
        if f: fb += 1; two += int(bool(Is) and bool(It))
    return it, fb, two

if __name__ == "__main__":
    a = sys.argv[1:]; tot = [0, 0, 0, 0]; files = 0
    if a[0] == "--list":
        R = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [load(os.path.join(R, l.split()[0])) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    else:
        cnt, lo, hi, k, seed = map(int, a[1:6]); rng = random.Random(seed)
        gs = [g for g in (rand_ckO(rng, lo, hi, k) for _ in range(cnt)) if g is not None]
    for g in gs:
        it, fb, two = count(g); tot[0] += it; tot[1] += fb; tot[2] += two; tot[3] += int(two > 0); files += 1
    print(f"runs {files}: iterations {tot[0]}, fallbacks {tot[1]}, two-sided fallbacks {tot[2]} (in {tot[3]} runs)")
