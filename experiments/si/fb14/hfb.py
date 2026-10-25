#!/usr/bin/env python3
"""L-SI succ. 9, box 14 item (2) (docs/si/N5-LEDGER-box14.md §4 item 1 (b)): DATA on in-phase fallbacks by state type.
For every in-phase S4c fallback k -> k+1 (tau and lambda_Xi constant): state type at k ((h), HN, Q, notH1 (= not H1)), its index j among the
in-phase fallbacks of its phase (1-based), |U| (U = lambda^{-1}(c_theta)), and every switched Even vertex v classified as
  ev   : v in R_k (R excl. o), sigma_{k+1}(v) in F_k            (eviction switch, R -> F)
  rr   : v in R_k, sigma_{k+1}(v) in Rbar_k                     (route change inside Rbar)
  fr   : v in F_k, sigma_{k+1}(v) in Rbar_k                     (F -> Rbar)
  ffU  : v in F_k cap U, sigma_{k+1}(v) in F_k                  (F cap U -> F)
  ffO  : v in F_k, v not in U, target in F_k                    (outside U)
  plus "cyc" if lambda_k(v) = v or v lies on c_theta's honest cycle.
Counters split by j <= |U| - 2 ("pre") and j >= |U| - 1 ("post", after g_{|U|-2}); FBCAP-route (iii) says ev never occurs post.
Per phase: max in-phase fallbacks, max at (h) states, max of (#fb - (|U| - 2)).
Traces: REFEREE-2's tracer (read only). Usage: hfb.py R seed game.pg ..."""
import sys, os, random
from collections import Counter
R2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "docs", "referee-2")
for d in ("R2-N5-OUT", "R2-N5-FRZ"): sys.path.insert(0, os.path.join(R2, d))
import out_check as OC
FC, RC = OC.FC, OC.RC

def stype(S):
    if not S.H1: return "notH1"
    if not S.H2: return "HN"
    return "(h)" if S.H3 else "Q"

def ccycle(g, S, c):
    cyc, v = {c}, S.fh[c]
    while v != c and v not in cyc: cyc.add(v); v = S.fh[v]
    return cyc if v == c else {c}

def scan(g, o, A, fbs, C, M, ex, tag):
    T = len(fbs); inph = [OC.key(A[k], o) == OC.key(A[k + 1], o) for k in range(T)]
    k = 0
    while k < T:
        if not inph[k]: k += 1; continue
        a = k
        while k < T and inph[k]: k += 1
        nfb, nh, U = 0, 0, None
        for s in range(a, k):
            if not fbs[s]: continue
            S, S1 = A[s], A[s + 1]; nfb += 1; ty = stype(S)
            ct = S.Xi[o][0]; U = {z for z in range(g.n) if S.Xi[z][0] == ct}; post = nfb >= len(U) - 1
            if ty == "(h)": nh += 1
            C[f"fb {ty} {'post' if post else 'pre'}"] += 1
            cyc = ccycle(g, S, ct)
            for v in range(g.n):
                if g.owner[v] != 0 or S.sg[v] == S1.sg[v]: continue
                x = S1.sg[v]; vR = v in S.Rr; xR = x in S.Rbar
                c = ("ev" if vR and not xR else "rr" if vR else "fr" if xR else "ffU" if v in U else "ffO")
                if S.Xi[v][0] == v or v in cyc: c += "+cyc"
                C[f"sw {ty} {'post' if post else 'pre'} {c}"] += 1
                if post and c.split("+")[0] in ("ev", "fr", "ffU") and len(ex) < 12: ex.append((tag, s, ty, nfb, len(U), v, x, c))
            if S1.Rbar < S.Rbar or not (S1.Rbar >= S.Rbar): C[f"fb {ty} crossing {'post' if post else 'pre'}"] += 1
        if U is not None:
            M["max fb/phase"] = max(M["max fb/phase"], nfb); M["max (h)-fb/phase"] = max(M["max (h)-fb/phase"], nh)
            M["max fb-(|U|-2)"] = max(M["max fb-(|U|-2)"], nfb - (len(U) - 2))
            C["phases with fb"] += 1

def main():
    Rn, seed, files = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3:]
    C, M, ex = Counter(), Counter(), []
    M["max fb-(|U|-2)"] = -99
    for p in files:
        g = RC.parse(open(p).read())
        try: o = FC.odd_vertex(g)
        except AssertionError: C["skipped (not C^1O)"] += 1; continue
        rng = random.Random(f"{seed}:{os.path.basename(p)}"); C["files"] += 1
        starts = [FC.s3_start(g)] + [RC.rand_start(rng, g) for _ in range(Rn)]
        for i, (s, t) in enumerate(starts):
            A, fbs = OC.run_trace(g, o, s, t, rng, "spec"); C["traces"] += 1
            scan(g, o, A, fbs, C, M, ex, (os.path.basename(p), i))
    for kk in sorted(C): print(f"{kk:40s} {C[kk]}")
    print("MAX", dict(M)); print("EXAMPLES post ev/fr/ffU:", ex)
if __name__ == "__main__": main()
