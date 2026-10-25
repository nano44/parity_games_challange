#!/usr/bin/env python3
"""REFEREE-2 succ. 7 (Opus 5.5, D15), for §C on FBW-1: at in-phase Even S4c fallbacks k with (h) at k and k+1 and gates (M_k >= 0 or
any), for every switched Even y' with lambda(y') = y': is o on y''s honest H_{k+1}-cycle (H1 question) and on its (sigma_{k+1}, tau)-cycle
(H2 question)? Own N5 of ../R2-N5-FRZ/frz_check.py (no lane code). Usage: fbw1_probe.py file.pg ... | random N nmin nmax seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FRZ"))
import frz_check as FC
from collections import Counter
RC = FC.RC; c = Counter()
def cyc(f, v): return set(RC._cycle(None, f, v))
def probe(g, o, A, fbs):
    for k, fb in enumerate(fbs):
        a, b = A[k], A[k + 1]
        if not fb or a.lamX != b.lamX or a.tu[o] != b.tu[o] or not (a.hh and b.hh): continue
        c["inphase_fallbacks_h_both"] += 1
        for y in range(g.n):
            if g.owner[y] == 0 and a.sg[y] != b.sg[y] and a.lamX[y] == y:
                c["switched_own_cycle_nodes"] += 1
                hc, wc = cyc(b.fh, y), cyc(b.f, y)
                if y not in hc: c["VIOLATION honest play of y' not a cycle through y'"] += 1
                if o in hc: c["VIOLATION o on honest cycle (H1 fails)"] += 1
                if o in wc: c["VIOLATION o on W-cycle"] += 1
                if hc != wc: c["honest cycle != W-cycle"] += 1
if sys.argv[1] == "random":
    N, nmin, nmax, seed = map(int, sys.argv[2:6]); rng = random.Random(seed)
    for i in range(N):
        g, o = RC.rand_game(rng, rng.randint(nmin, nmax)); s, t = RC.rand_start(rng, g)
        A, fbs = FC.run_n5(g, o, s, t, rng, i % 2 == 1); probe(g, o, A, fbs)
else:
    for path in sys.argv[1:]:
        g = RC.parse(open(path).read()); o = FC.odd_vertex(g); rng = random.Random(5)
        for r in range(3):
            s, t = FC.s3_start(g) if r == 0 else RC.rand_start(rng, g)
            A, fbs = FC.run_n5(g, o, s, t, rng, r == 2); probe(g, o, A, fbs)
for k in sorted(c): print(f"{k}: {c[k]}")
print("RESULT", "FAIL" if any(k.startswith("VIOLATION") for k in c) else "OK")
