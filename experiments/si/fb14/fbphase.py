#!/usr/bin/env python3
"""L-SI succ. 9, box 14: DATA for Theorem FB-PHASE (docs/si/N5-FBPHASE-box14.md). Per phase of N5 (SPEC) on C^1O:
 (SG)   every Even v switched at an in-phase fallback with lambda(v) != v strictly rises: Xi_{k+1}(v) > Xi_k(v);
 (PF)   kappa-P-FREEZE: in a theta-run Theta, at states after the (|U|-1)-th fallback of Theta, Xi is constant on U; and no fallback of
        Theta after that switches a vertex of U minus {c_theta};
 (CF)   class freeze: for a class U'' = lambda^{-1}(c''), c'' != c_theta, Xi is constant on U'' after the phase's (|U''|-1)-th fallback;
 (TH)   after the phase's (|U|-2)-th fallback, theta takes <= d_o + n distinct values;
 (FB)   #fallbacks <= N0 + (d_o + n)(|U| - 1) + (d_o + n - 1) + 1, N0 = max(|U| - 2, max |U''| - 1).
Also counts how often the post-freeze hypotheses occur (vacuity). Traces: REFEREE-2's tracer, read only. Usage: fbphase.py R seed game.pg ..."""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hfb
OC, FC, RC = hfb.OC, hfb.FC, hfb.RC

def scan(g, o, A, fbs, C, M, bad, tag):
    T = len(fbs); inph = [OC.key(A[k], o) == OC.key(A[k + 1], o) for k in range(T)]
    gt = lambda x, y: g.key(x) > g.key(y)
    k = 0
    while k < T:
        if not inph[k]: k += 1; continue
        a = k
        while k < T and inph[k]: k += 1
        b = k  # states a..b, transitions a..b-1
        lam = [A[a].Xi[z][0] for z in range(g.n)]; ct = lam[o]
        cls = {}
        for z in range(g.n): cls.setdefault(lam[z], set()).add(z)
        U = cls[ct]; fl = [s for s in range(a, b) if fbs[s]]
        if not fl: continue
        C["phases with fb"] += 1
        d_o = len(set(g.succ[o])); n = g.n
        # SG
        for s in fl:
            for v in range(n):
                if g.owner[v] == 0 and A[s].sg[v] != A[s + 1].sg[v] and lam[v] != v:
                    C["SG checks"] += 1
                    if not gt(A[s + 1].Xi[v], A[s].Xi[v]): C["SG FAIL"] += 1; bad.append(("SG", tag, s, v))
        # theta-runs and PF
        s = a
        while s < b:
            e = s
            while e < b and A[e + 1].theta == A[s].theta: e += 1
            fr = [x for x in fl if s <= x < e]          # fallbacks with both ends in the run [s, e]
            if len(fr) >= len(U) - 1 and len(U) >= 2:
                f0 = fr[len(U) - 2] if len(U) >= 2 else s - 1   # the (|U|-1)-th fallback
                ts = range(f0 + 1, e + 1)
                C["PF post-freeze theta-runs"] += 1
                for t in ts:
                    C["PF state checks"] += 1
                    if any(A[t].Xi[z] != A[f0 + 1].Xi[z] for z in U): C["PF FAIL (Xi moves on U)"] += 1; bad.append(("PF", tag, f0, t))
                for x in fr[len(U) - 1:]:
                    C["PF post-freeze fallbacks"] += 1
                    if any(g.owner[v] == 0 and v in U and v != ct and A[x].sg[v] != A[x + 1].sg[v] for v in range(n)):
                        C["PF FAIL (U switch)"] += 1; bad.append(("PFsw", tag, x))
            s = e + 1
        # CF
        for c, Uc in cls.items():
            if c == ct or len(fl) < len(Uc) - 1 or len(Uc) < 2: continue
            f0 = fl[len(Uc) - 2]; C["CF post-freeze classes"] += 1
            for t in range(f0 + 1, b + 1):
                C["CF state checks"] += 1
                if any(A[t].Xi[z] != A[f0 + 1].Xi[z] for z in Uc): C["CF FAIL"] += 1; bad.append(("CF", tag, c, t))
        # TH
        if len(fl) >= max(len(U) - 2, 1):
            st = fl[len(U) - 3] + 1 if len(U) >= 3 else a
            vals = {A[t].theta for t in range(st, b + 1)}
            M["max distinct theta post-HAT / (d_o+n)"] = max(M["max distinct theta post-HAT / (d_o+n)"], len(vals) / (d_o + n))
            if len(vals) > d_o + n: C["TH FAIL"] += 1; bad.append(("TH", tag, len(vals)))
        N0 = max([len(U) - 2] + [len(Uc) - 1 for c, Uc in cls.items() if c != ct])
        bound = N0 + (d_o + n) * (len(U) - 1) + (d_o + n - 1) + 1
        M["max fb/phase"] = max(M["max fb/phase"], len(fl)); M["max fb/bound"] = max(M["max fb/bound"], len(fl) / bound)
        if len(fl) > bound: C["FB FAIL"] += 1; bad.append(("FB", tag, len(fl), bound))

def main():
    Rn, seed, files = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3:]
    C, M, bad = Counter(), Counter(), []
    for p in files:
        g = RC.parse(open(p).read())
        try: o = FC.odd_vertex(g)
        except AssertionError: C["skipped (not C^1O)"] += 1; continue
        rng = random.Random(f"{seed}:{os.path.basename(p)}"); C["files"] += 1
        for i, (s, t) in enumerate([FC.s3_start(g)] + [RC.rand_start(rng, g) for _ in range(Rn)]):
            A, fbs = OC.run_trace(g, o, s, t, rng, "spec"); C["traces"] += 1
            scan(g, o, A, fbs, C, M, bad, (os.path.basename(p), i))
    for kk in sorted(C): print(f"{kk:40s} {C[kk]}")
    print("MAX", {k: round(v, 3) for k, v in M.items()}); print("FAILS (first 10):", bad[:10])
    print("RESULT", "FAIL" if any("FAIL" in k for k in C) else "OK")
if __name__ == "__main__": main()
