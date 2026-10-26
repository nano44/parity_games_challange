#!/usr/bin/env python3
"""Box 45 (2) (L-RED successor 19): Lemma DUAL (docs/new/P-N5-DUAL-box43.md, sha1 a51f7c30) on our own engine (o1_19.trace, own copy of
n5.py's loop with an N5^OF switch). For G and a start vector st (st[v] for every v; None = S3 start):
  A = N5 on G from st;  B = N5^OF on G^d from st (G^d's Even = G's Odd, so the same per-vertex vector is the mirrored pair);
  C = N5 on G^d from st.
DUAL: len(A) = len(B) and A_k = mirror(B_k) for every k (mirror(σ, τ) = (τ, σ)). Second sentence: first k with A_k ≠ mirror(C_k) is
j + 1 for j → j + 1 the first two-sided fallback of A (Iσ ≠ ∅ and Iτ ≠ ∅ at an S4c fallback); none if A has no two-sided fallback.
Any class (random games with k Odd choice vertices, k = 1..4, and arbitrary Even degrees). Usage: dual19.py seed secs nmin nmax R  |  dual19.py lib seed R files..."""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import o1_19 as O, pg, n5
from si import Engine

def twosided(g, S, FB):
    E, Ed = Engine(g), Engine(n5.dual(g))
    for k, f in enumerate(FB):
        if f:
            s, t = S[k]
            if E.improving(s, E.evaluate(s)[0]) and Ed.improving(t, Ed.evaluate(t)[0]): return k
    return None

def check(g, st):
    gd = n5.dual(g)
    A, FA, _ = O.trace(g, st, "n5"); B, _, _ = O.trace(gd, st, "of"); C, _, _ = O.trace(gd, st, "n5")
    mir = lambda X: [(t, s) for s, t in X]
    dual_ok = A == mir(B)
    j = twosided(g, A, FA); Cm = mir(C)
    first = next((k for k in range(min(len(A), len(Cm))) if A[k] != Cm[k]), None)
    if first is None and len(A) != len(Cm): first = min(len(A), len(Cm))
    second_ok = (first is None) if j is None else (first == j + 1)
    return dual_ok, second_ok, j, first, len(A), len(C)

if __name__ == "__main__" and sys.argv[1] == "lib":
    pass
elif __name__ == "__main__":
    seed, secs, nmin, nmax, R = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    rng = random.Random(seed); t0 = time.time(); c = dict(runs=0, dual_fail=0, second_fail=0, twosided=0, plain_differs=0)
    while time.time() - t0 < secs:
        n = rng.randint(nmin, nmax); k = rng.randint(1, 4)
        prio = [rng.randrange(2 * n) for _ in range(n)]; owner = [0 if rng.random() < 0.6 else 1 for _ in range(n)]
        succ = [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3)) if owner[v] == 0 else 1))) for v in range(n)]
        for o in rng.sample(range(n), min(k, n)): owner[o] = 1; succ[o] = sorted(set(rng.sample(range(n), rng.randint(2, max(2, n // 2)))))
        g = pg.Game(prio, owner, succ)
        for r in range(R + 1):
            st = None if r == 0 else [rng.choice(g.succ[v]) for v in range(n)]
            d, s2, j, first, la, lc = check(g, st); c["runs"] += 1
            c["twosided"] += j is not None; c["plain_differs"] += first is not None
            if not d or not s2:
                c["dual_fail" if not d else "second_fail"] += 1
                print("FAIL", "DUAL" if not d else "SECOND", dict(prio=prio, owner=owner, succ=succ, start=st, j=j, first=first, la=la, lc=lc), flush=True)
    print("COUNTS", c, flush=True)

def libmain(seed, R, files):
    rng = random.Random(seed); c = dict(files=0, runs=0, dual_fail=0, second_fail=0, twosided=0, plain_differs=0)
    for f in files:
        try: g = pg.parse("".join(l for l in open(f) if not l.lstrip().startswith("%")))
        except Exception: continue
        if g.n > 80: continue
        c["files"] += 1
        for r in range(R + 1):
            st = None if r == 0 else [rng.choice(g.succ[v]) for v in range(g.n)]
            d, s2, j, first, la, lc = check(g, st); c["runs"] += 1
            c["twosided"] += j is not None; c["plain_differs"] += first is not None
            if not d or not s2:
                c["dual_fail" if not d else "second_fail"] += 1; print("FAIL", f, st, j, first, la, lc, flush=True)
    print("LIBCOUNTS", c, flush=True)

if __name__ == "__main__" and sys.argv[1] == "lib": libmain(int(sys.argv[2]), int(sys.argv[3]), sys.argv[4:])
