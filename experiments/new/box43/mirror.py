#!/usr/bin/env python3
"""Box 43, Lemma DUAL check (DATA): N5 on G from (sigma0, tau0) vs N5 on G^d (n5.dual) from (tau0, sigma0), roles swapped.
Claim tested: the two state sequences agree up to and including the first TWO-SIDED fallback transition's source state (S4c with
I_sigma and I_tau both non-empty), and agree entirely if there is none. Also checks the Odd-first variant N5^OF on G^d (S4c falls
back for G^d's Odd first) reproduces N5's run on G exactly.
Usage: mirror.py --list FILE | --rand COUNT NLO NHI SEED"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from multi import rand_ckO, pg
from n5x import load, step, start_pair, Engine, dual

def runN5(g, s, t, oddfirst=False, cap=3000):
    E, Ed = Engine(g), Engine(dual(g)); out = [(tuple(s), tuple(t))]; two = []
    while len(out) <= cap:
        vs, _ = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs)
        vt, _ = Ed.evaluate(tuple(t)); It = Ed.improving(tuple(t), vt)
        r = step(g, E, Ed, s, t)
        if r is None: break
        ns, nt, Is, It, fb, vs, vt = r
        if fb and Is and It:
            two.append(len(out) - 1)
            if oddfirst:                      # S4c with Odd first: switch-all for Odd on I_tau, sigma unchanged
                ns, nt = list(s), list(t)
                for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
        s, t = ns, nt; out.append((tuple(s), tuple(t)))
    return out, two

def check(g, st=None):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st)
    A, twoA = runN5(g, list(s), list(t))
    d = dual(g)
    B, twoB = runN5(d, list(t), list(s)); B = [(b, a) for a, b in B]
    C, _ = runN5(d, list(t), list(s), oddfirst=True); C = [(b, a) for a, b in C]
    first = next((i for i in range(min(len(A), len(B))) if A[i] != B[i]), None)
    if first is None and len(A) != len(B): first = min(len(A), len(B))
    ok = first is None or (twoA and first == twoA[0] + 1)
    return ok, A == C, bool(twoA)

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--list":
        R = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [load(os.path.join(R, l.split()[0])) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    else:
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        gs = [g for g in (rand_ckO(rng, lo, hi, rng.randint(1, 4)) for _ in range(cnt)) if g is not None]
    tot = bad = badOF = withtwo = 0
    for g in gs:
        ok, okOF, two = check(g); tot += 1; bad += not ok; badOF += not okOF; withtwo += two
    print(f"runs {tot}: runs with a two-sided fallback {withtwo}; DUAL violations {bad}; N5 on G != N5^OF on G^d mirrored: {badOF}")
