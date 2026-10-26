#!/usr/bin/env python3
"""Box 43: duality symmetry of N5 (DATA). Run N5 on G from the best-reward start (sigma0, tau0) and on G^d (n5.dual: owners
swapped, priorities + 1) from (tau0, sigma0); compare the state sequences with roles swapped. Reports the first index where they
differ and whether a fallback (S4c) happened at or before it in either run.
Usage: dualsym.py --rand COUNT NLO NHI SEED"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from multi import run, rand_ckO, pg, dual

def check(g):
    s1, _, _, f1 = run(g)
    st0 = s1[0]
    d = dual(g)
    st = ({v: st0[1][v] for v in range(g.n) if d.owner[v] == 0}, {v: st0[0][v] for v in range(g.n) if d.owner[v] == 1})
    s2, _, _, f2 = run(d, st)
    sw = [(b, a) for a, b in s2]
    def norm(s): return tuple(tuple(x if x is not None and x >= 0 else -1 for x in y) for y in s)
    A = [ (tuple(s[0][v] for v in range(g.n) if g.owner[v] == 0), tuple(s[1][v] for v in range(g.n) if g.owner[v] == 1)) for s in s1]
    B = [ (tuple(s[1][v] for v in range(g.n) if g.owner[v] == 0), tuple(s[0][v] for v in range(g.n) if g.owner[v] == 1)) for s in s2]
    for i in range(min(len(A), len(B))):
        if A[i] != B[i]:
            return i, int(any(f1[:i]) or any(f2[:i])), int((i - 1 < len(f1) and f1[i - 1]) or (i - 1 < len(f2) and f2[i - 1]))
    return (None, 0, 0) if len(A) == len(B) else (min(len(A), len(B)), 0, 0)

if __name__ == "__main__":
    cnt, lo, hi, seed = map(int, sys.argv[2:6]); rng = random.Random(seed)
    same = diff_fb = diff_nofb = 0; ex = None
    for c in range(cnt):
        k = rng.randint(1, 4); g = rand_ckO(rng, lo, hi, k, 0.15)
        if g is None: continue
        i, anyfb, fbat = check(g)
        if i is None: same += 1
        elif fbat: diff_fb += 1
        else:
            diff_nofb += 1
            if ex is None: ex = (g.prio, g.owner, g.succ, i)
    print(f"identical {same}; first difference right after a fallback {diff_fb}; other differences {diff_nofb}; example {ex}")
