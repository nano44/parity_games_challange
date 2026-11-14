#!/usr/bin/env python3
"""L-SI box 104: N5'-xi on F_n by two implementations (1 = box190 n5v.py mode xi on si.py's Engine; 2 = box190 n5bxi.py on L-COMP's
n5b / pgsolver_si), both from S3; regions against harness Zielonka; both strategy outputs through harness verify.check.
Usage: xck104.py n...   (env LNEW, LRED as free104.py)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import free104 as F
import n5v, n5bxi, zielonka, verify
for n in map(int, sys.argv[1:]):
    T, _ = F.fried.howard(F.fried.game(n)); g = F.F(n)[0]
    st, fb1, E = n5v.run(g, "xi"); w1, s1 = n5v.solution(g, st, E)
    w2, s2, it2, fb2 = n5bxi.N5xi(g, mode="spec").run()
    ref = zielonka.solve(g); s1w = [s1[v] if w1[v] == g.owner[v] else None for v in range(g.n)]
    e1, e2 = verify.check(g, w1, s1w), verify.check(g, w2, s2)
    ok = (len(st) - 1, fb1, w1) == (it2, fb2, w2) and w1 == ref and not e1 and not e2
    print(f"XCK104 n {n}: Howard T {T}; |V| {g.n}; impl1 iterations {len(st) - 1} fallbacks {fb1}; impl2 iterations {it2} fallbacks {fb2}; regions equal "
          f"{w1 == w2}; vs Zielonka {w1 == ref}/{w2 == ref}; verify errors {len(e1)}/{len(e2)}; {'AGREE+CORRECT' if ok else 'MISMATCH'}", flush=True)
