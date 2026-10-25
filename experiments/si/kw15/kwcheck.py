#!/usr/bin/env python3
"""L-SI succ. 10, box 15: DATA for the K / (E) / (K_W) attack (docs/si/N5-KW-box15.md). N5 (SPEC mode, REFEREE-2's tracer, read only)
on C^1O. Phase = maximal run with (lambda_Xi, tau(o)) constant. Stretch = maximal run of states of a phase with Rbar, theta, w constant.
Run S = maximal run of consecutive NON-fallback transitions inside a stretch (states k0..kT). m* := the more relevant of c_theta, c_w.
kappa(v) := vertices of pi_v (route to o, o excluded) of rank > rank m*.
Checks:
  WONCE   (any game) in a phase, transitions k, k+1 both non-fallback, Xi_{k+1} == Xi_k  =>  W_{k+2} == W_{k+1}.
  AGREE   on every stretch state: for v in R, P(Xi(v)) above m* == kappa(pi_v) + (P(theta) above m*) and P(W(v)) above m* == kappa(pi_v)
          + (P(w) above m*), with Xi / W cycle nodes c_theta / c_w.
  FRZ     in every run S: kappa(pi_v) constant on R for states >= k0 + |Rbar| - 1.
  LEN     post-freeze: if c_theta >= c_w (rank): P(Xi(v)) constant on R; if c_w > c_theta: P(W(v)) constant on R.
  KIND    post-freeze, c_w > c_theta, not H2, c_w != o: per vertex, kind (c_w in pi_v) changes <= 1 time and only in the direction
          favoured by c_w's parity (even: B -> A; odd: A -> B).
  CWINT   post-freeze, c_w > c_theta, not H2: between two transitions with a kind change or a kind-B switch, c_w switches <= deg(c_w) - 1.
Counts: per run S the transitions with a Xi-change on R, a W-change on R, kind changes, c_w switches (maxima printed).
Usage: kwcheck.py R seed game.pg ...   (S3 start + R random starts per file)"""
import sys, os, random
from collections import Counter
R2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "docs", "referee-2")
for d in ("R2-N5-OUT", "R2-N5-FRZ"): sys.path.insert(0, os.path.join(R2, d))
import out_check as OC
FC, RC = OC.FC, OC.RC

def above(g, P, m): return frozenset(x for x in P if g.rank[x] > g.rank[m])

def scan(g, o, A, fbs, C, M, bad, tag):
    T = len(fbs); n = g.n
    inph = [OC.key(A[k], o) == OC.key(A[k + 1], o) for k in range(T)]
    # WONCE
    for k in range(T):
        if inph[k] and not fbs[k] and A[k + 1].Xi == A[k].Xi: C["Xi-flat S4a transitions"] += 1
    for k in range(T - 1):
        if inph[k] and inph[k + 1] and not fbs[k] and not fbs[k + 1]:
            if A[k + 1].Xi == A[k].Xi:
                C["WONCE checks"] += 1
                if A[k + 2].W != A[k + 1].W: C["WONCE FAIL"] += 1; bad.append(("WONCE", tag, k))
    # stretches
    same = lambda a: inph[a] and A[a].Rbar == A[a + 1].Rbar and A[a].theta == A[a + 1].theta and A[a].w == A[a + 1].w
    k = 0
    while k < T:
        if not (same(k) and not fbs[k]): k += 1; continue
        a = k
        while k < T and same(k) and not fbs[k]: k += 1
        b = k            # run S: states a..b, transitions a..b-1, all non-fallback, inside one stretch
        S0 = A[a]; ct, cw = S0.theta[0], S0.w[0]
        ms = ct if g.rank[ct] >= g.rank[cw] else cw
        R = S0.Rr; Rb = S0.Rbar
        C["runs"] += 1; C[f"runs {'cth>=cw' if ms == ct else 'cw>cth'} {'H2' if S0.H2 else 'notH2'} {'H1' if S0.H1 else 'notH1'}"] += 1
        if ms == cw and cw != ct and not S0.H2 and cw != o:
            C["cw>cth notH2 runs (any length)"] += 1
            if not g.even[cw]: C["cw>cth notH2 runs c_w odd (any length)"] += 1
            M["max cw>cth notH2 run length"] = max(M["max cw>cth notH2 run length"], b - a)
        kap = lambda S, v: above(g, S.pi[v], ms)
        for t in range(a, b + 1):
            S = A[t]; C["AGREE states"] += 1
            Pt, Pw = above(g, S.theta[1], ms), above(g, S.w[1], ms)
            for v in R:
                if S.Xi[v][0] != ct or above(g, S.Xi[v][1], ms) != kap(S, v) | Pt: C["AGREE FAIL Xi"] += 1; bad.append(("AGXi", tag, t, v))
                if S.W[v][0] != cw or above(g, S.W[v][1], ms) != kap(S, v) | Pw: C["AGREE FAIL W"] += 1; bad.append(("AGW", tag, t, v))
        f0 = a + len(Rb) - 1
        if f0 > b: C["runs shorter than freeze"] += 1
        else:
            C["post-freeze runs"] += 1; M["max post-freeze length"] = max(M["max post-freeze length"], b - f0)
            # actual freeze point
            last = a
            for t in range(a + 1, b + 1):
                if any(kap(A[t], v) != kap(A[t - 1], v) for v in R): last = t
            M["max kappa-freeze delay (t - k0)"] = max(M["max kappa-freeze delay (t - k0)"], last - a)
            M["max kappa-freeze delay / (|Rbar|-1)"] = max(M["max kappa-freeze delay / (|Rbar|-1)"], round((last - a) / max(1, len(Rb) - 1), 3))
            for t in range(f0 + 1, b + 1):
                C["FRZ state checks"] += 1
                if any(kap(A[t], v) != kap(A[f0], v) for v in R): C["FRZ FAIL"] += 1; bad.append(("FRZ", tag, a, f0, t))
                if ms == ct:
                    if any(A[t].Xi[v][1] != A[f0].Xi[v][1] for v in R): C["LEN FAIL Xi path set"] += 1; bad.append(("LENXi", tag, f0, t))
                else:
                    if any(A[t].W[v][1] != A[f0].W[v][1] for v in R): C["LEN FAIL W path set"] += 1; bad.append(("LENW", tag, f0, t))
            if ms == cw and cw != ct and not S0.H2 and cw != o:
                C["KIND runs"] += 1; M["max KIND post-freeze length"] = max(M["max KIND post-freeze length"], b - f0)
                if not g.even[cw]: C["KIND runs c_w odd"] += 1
                kind = lambda S, v: cw in S.pi[v]
                ch = Counter(); kc_tr = []; kb_tr = []; cw_sw = []
                for t in range(f0, b):
                    S, S1 = A[t], A[t + 1]
                    kc = [v for v in R if kind(S, v) != kind(S1, v)]
                    for v in kc:
                        ch[v] += 1; C["KIND changes"] += 1
                        good = kind(S1, v) if g.even[cw] else not kind(S1, v)
                        if not good: C["KIND FAIL direction"] += 1; bad.append(("KINDdir", tag, t, v))
                    if kc: kc_tr.append(t)
                    if any(g.owner[v] == 0 and S.sg[v] != S1.sg[v] and not kind(S, v) for v in R): kb_tr.append(t)
                    if S.sg[cw] != S1.sg[cw]: cw_sw.append(t)
                if any(c > 1 for c in ch.values()): C["KIND FAIL >1 change"] += 1; bad.append(("KIND2", tag, a))
                cuts = sorted(set(kc_tr) | set(kb_tr)); dg = len(set(g.succ[cw]))
                lo = f0
                for c in cuts + [b]:
                    m = sum(1 for t in cw_sw if lo <= t < c)
                    C["CWINT intervals"] += 1
                    if m > dg - 1: C["CWINT FAIL"] += 1; bad.append(("CWINT", tag, lo, c, m, dg))
                    lo = c + 1
                M["max kind changes / run"] = max(M["max kind changes / run"], len(kc_tr))
                M["max c_w switches / run"] = max(M["max c_w switches / run"], len(cw_sw))
        xr = sum(1 for t in range(a, b) if any(A[t].Xi[v] != A[t + 1].Xi[v] for v in Rb))
        wr = sum(1 for t in range(a, b) if any(A[t].W[v] != A[t + 1].W[v] for v in Rb))
        M["max Xi-changes on R / run"] = max(M["max Xi-changes on R / run"], xr)
        M["max W-changes on R / run"] = max(M["max W-changes on R / run"], wr)
        M["max run length"] = max(M["max run length"], b - a)

def main():
    Rn, seed, files = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3:]
    C, M, bad = Counter(), Counter(), []
    for p in files:
        try: g = RC.parse(open(p).read())
        except Exception: C["unparsable"] += 1; continue
        try: o = FC.odd_vertex(g)
        except AssertionError: C["skipped (not C^1O)"] += 1; continue
        rng = random.Random(f"{seed}:{os.path.basename(p)}"); C["files"] += 1
        starts = [FC.s3_start(g)] + [RC.rand_start(rng, g) for _ in range(Rn)]
        for i, (s, t) in enumerate(starts):
            A, fbs = OC.run_trace(g, o, s, t, rng, "spec"); C["traces"] += 1; C["transitions"] += len(fbs)
            scan(g, o, A, fbs, C, M, bad, (os.path.basename(p), i))
    for kk in sorted(C): print(f"{kk:45s} {C[kk]}")
    for kk in sorted(M): print(f"MAX {kk:41s} {M[kk]}")
    print("FAILURES (first 20):", bad[:20])
    print("KWCHECK", "PASS" if not bad else "FAIL")
if __name__ == "__main__": main()
