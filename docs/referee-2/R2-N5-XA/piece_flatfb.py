#!/usr/bin/env python3
"""REFEREE-2 check of REFEREE R-N5-XA §C5 / R2-N5-XA §C.5: PIECE with value-flat fallbacks INSIDE pieces.
A piece here = maximal run of transitions in one joint lambda-phase with tau, theta, w constant, (h) at both ends, R constant,
and either an S4a step or an S4c fallback that changes no Xi and no W value (a flat fallback). Checks: value-changing
transitions <= (|R| - 1) + (|F| - 1), separately R <= |R| - 1 and F <= |F| - 1; counts the flat fallbacks inside pieces.
Usage: piece_flatfb.py random N nmin nmax seed [own|spec] | piece_flatfb.py inst game.pg [own|spec] [runs]"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2-N5-RE"))
import re_check as rc

def run(g, o, states, fbs, c, bad, name):
    T = len(states) - 1; A = [rc.analyse(g, o, *s) for s in states]
    def flat(k): return A[k].Xi == A[k + 1].Xi and A[k].W == A[k + 1].W
    def good(k):
        return (A[k].lamX == A[k + 1].lamX and A[k].lamU == A[k + 1].lamU and states[k][1][o] == states[k + 1][1][o]
                and A[k].theta == A[k + 1].theta and A[k].w == A[k + 1].w and A[k].h and A[k + 1].h and A[k].R == A[k + 1].R
                and (not fbs[k] or flat(k)))
    k = 0
    while k < T:
        if not good(k): k += 1; continue
        k0 = k
        while k < T and good(k): k += 1
        R = A[k0].R; F = set(range(g.n)) - R
        vR = vF = v = nfb = 0
        for j in range(k0, k):
            nfb += fbs[j]
            cR = any(A[j].Xi[x] != A[j + 1].Xi[x] or A[j].W[x] != A[j + 1].W[x] for x in R)
            cF = any(A[j].Xi[x] != A[j + 1].Xi[x] or A[j].W[x] != A[j + 1].W[x] for x in F)
            vR += cR; vF += cF; v += cR or cF
        c["pieces"] += 1; c["flat_fb_inside"] += nfb; c["pieces_with_flat_fb"] += nfb > 0
        if nfb: c["vc_in_pieces_with_flat_fb"] += v
        if vR > max(len(R) - 1, 0) or vF > max(len(F) - 1, 0): bad.append(f"{name} piece {k0}..{k} vR={vR} vF={vF} |R|={len(R)}")

def main():
    c, bad = Counter(), []
    if sys.argv[1] == "random":
        N, nmin, nmax, seed = map(int, sys.argv[2:6]); mode = sys.argv[6] if len(sys.argv) > 6 else "own"
        rng = random.Random(seed)
        for i in range(N):
            g, o = rc.rand_game(rng, rng.randint(nmin, nmax)); s, t = rc.rand_start(rng, g)
            st, fb = rc.n5_spec(g, o, s, t) if mode == "spec" else rc.n5_own(g, o, s, t, rng)
            run(g, o, st, fb, c, bad, f"seed{seed}#{i}"); c["runs"] += 1
    else:
        g = rc.parse(open(sys.argv[2]).read()); oc = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1]; assert len(oc) == 1, f'not C^1O: Odd choice vertices {oc}'; o = oc[0]
        mode = sys.argv[3] if len(sys.argv) > 3 else "own"; runs = int(sys.argv[4]) if len(sys.argv) > 4 else 30
        rng = random.Random(1)
        for r in range(1 if mode == "spec" else runs):
            s, t = rc.rand_start(rng, g)
            st, fb = rc.n5_spec(g, o, s, t) if mode == "spec" else rc.n5_own(g, o, s, t, rng)
            run(g, o, st, fb, c, bad, f"{os.path.basename(sys.argv[2])}#{r}"); c["runs"] += 1
    for k in sorted(c): print(f"{k}: {c[k]}")
    for b in bad[:20]: print("VIOLATION", b)
    print("RESULT", "FAIL" if bad else "OK", f"violations={len(bad)}")

if __name__ == "__main__":
    main()
