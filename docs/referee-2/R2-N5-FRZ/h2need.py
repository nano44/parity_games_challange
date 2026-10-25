#!/usr/bin/env python3
"""REFEREE-2 succ. 7: print the first state t >= F(l) of a phase with NO H2 state at or after t where COARSE_l(Xi_t) != COARSE_l(Xi_F)
(FREEZE (a) makes no claim there; this shows its hypothesis is used). Usage: h2need.py game.pg [runs] [--rand]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import frz_check as FC
RC = FC.RC
args = [a for a in sys.argv[1:] if a != "--rand"]; rand = "--rand" in sys.argv
g = RC.parse(open(args[0]).read()); o = FC.odd_vertex(g); rng = random.Random(7)
for r in range(int(args[1]) if len(args) > 1 else 3):
    s, t = FC.s3_start(g) if r == 0 else RC.rand_start(rng, g)
    A, fbs = FC.run_n5(g, o, s, t, rng, rand); T = len(fbs)
    inph = [A[k].lamX == A[k + 1].lamX and A[k].tu[o] == A[k + 1].tu[o] for k in range(T)]
    k = 0
    while k < T:
        if not inph[k]: k += 1; continue
        j = k
        while j < T and inph[j]: j += 1
        a, b = k, j
        for L in FC.levels(g.n):
            F = FC.first_F(A, a, b, L, g.n)
            if F is None: continue
            for t2 in range(F + 1, b + 1):
                if any(A[u].H2 for u in range(t2, b + 1)): continue
                d = [v for v in range(g.n) if FC.coarse(g, A[t2].Xi[v], L) != FC.coarse(g, A[F].Xi[v], L)]
                if d:
                    print(f"run {r} phase states [{a},{b}] L={L} F={F} t={t2}: H1={A[t2].H1} H2={A[t2].H2} H3={A[t2].H3} fallback(t-1)={fbs[t2-1]}"
                          f" differs at {len(d)} vertices, e.g. v={d[0]}: Xi_F={A[F].Xi[d[0]][0]},{sorted(A[F].Xi[d[0]][1])} Xi_t={A[t2].Xi[d[0]][0]},{sorted(A[t2].Xi[d[0]][1])};"
                          f" phase ends at {b} ({'run end' if b == T else 'phase change'})")
                    sys.exit(0)
        k = j
print("none")
