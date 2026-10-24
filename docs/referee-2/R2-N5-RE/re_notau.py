#!/usr/bin/env python3
"""Addendum check (R2-N5-RE §A): Lemma RE WITHOUT the tau-constant hypothesis (REFEREE §C3 reading).
Hypotheses kept: one joint lambda-phase over [L, E+1], (h) at L and at E+1. Counts the re-entries whose interval contains a
tau-change, and checks steps 2-3 (strict gain at y and at x) at every leave with (h) at L and phase at L -> L+1, any tau.
Usage: re_notau.py random N nmin nmax seed [own|spec] | re_notau.py inst game.pg [own|spec] [runs]"""
import sys, os, random
from collections import Counter
import re_check as rc

def run(g, o, states, fbs, c, bad, name):
    T = len(states) - 1; A = [rc.analyse(g, o, *s) for s in states]
    inph = [A[k].lamX == A[k + 1].lamX and A[k].lamU == A[k + 1].lamU for k in range(T)]
    tauc = [states[k][1][o] == states[k + 1][1][o] for k in range(T)]
    c["tau_changes"] += T - sum(tauc)
    for L in range(T):
        if not (inph[L] and A[L].h): continue
        S0, S1 = A[L], A[L + 1]
        sw = {v for v in range(g.n) if g.owner[v] == 0 and S0.f[v] != S1.f[v]}
        for x in S0.R - S1.R:
            c["leaves" + ("" if tauc[L] else "_at_tau_change")] += 1
            ys = [u for u in S0.pi[x] if u in sw]
            if not ys: bad.append(f"{name} L={L} x={x} no switched vertex on the route"); continue
            y = ys[0]
            if g.cmp(S1.Xi[y], S0.Xi[y]) <= 0 or g.cmp(S1.Xi[x], S0.Xi[x]) <= 0: bad.append(f"{name} L={L} x={x} y={y} no strict gain")
    for x in range(g.n):
        k = 0
        while k < T:
            if x in A[k].R and x not in A[k + 1].R:
                L = k; E1 = L + 1
                while E1 <= T and x not in A[E1].R: E1 += 1
                if E1 > T: break
                if all(inph[j] for j in range(L, E1)) and A[L].h and A[E1].h:
                    tc = not all(tauc[j] for j in range(L, E1))
                    c["reentries" + ("_tau_changed" if tc else "")] += 1
                    if A[E1].theta == A[L].theta:
                        c["theta_equal" + ("_tau_changed" if tc else "")] += 1
                        if g.cmp(rc.prefix(g, A[E1].pi[x], A[L].theta), rc.prefix(g, A[L].pi[x], A[L].theta)) <= 0:
                            bad.append(f"{name} RE x={x} L={L} E+1={E1} tau_changed={tc}")
                k = E1
            else:
                k += 1

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
        g = rc.parse(open(sys.argv[2]).read()); o = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1][0]
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
