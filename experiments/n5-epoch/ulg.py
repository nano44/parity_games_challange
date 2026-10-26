#!/usr/bin/env python3
"""Box 15 (Lead 17:08Z / 17:31Z): own counter for global C-intervals (P-N5-GCX §1, docs/si/P-N5-GCX-box21.md), CONJECTURE UL_G (§3 premise)
and L-RED 22's GCI-LEN (every global C-interval of a lambda_W-constant fallback-free run has length <= n - 1). L-SI's gcx.py and L-RED's
experiments/red/ul/ulx.py are references only (not imported). Engine: census.py (n5b SPEC).
Definitions (P-N5-GCX §1, RESULTS R67 setting):
  run S: maximal run of states of one phase whose transitions are all in-phase S4a steps (no fallback) with lambda_W constant ((ii)).
  U_c = lambda^{-1}(c); PLAY of z = its (sigma_t, tau)-play; A_t(c) = {z in U_c : play meets no vertex of D_t}, D_t = {Odd u : sbar(u) != tau(u)};
  DD_t(c) = {u in D_t & U_c : sbar_t(u) in A_t(c) and tau(u) in A_t(c)};  Delta_t(u) = M_t(tau u) - M_t(sbar u), M_t(z) = w(path set of Xi_t(z)),
  w(P) = sum_{v in P} eps(v) 2^{rank(v)}, eps = +1 (even priority) / -1 (odd), rank by (priority, id) (READING of R25 (C3)'s signed weight).
  GLOBAL C-INTERVAL: maximal sub-interval [a, b] of S whose every transition t -> t+1 has, for every c: A_{t+1}(c) subset of A_t(c), D_{t+1} = D_t,
  DD_{t+1} = DD_t and Delta constant on DD.  Length = b - a (transitions);  G_LEN_SLACK = (b - a) - (n - 1);  GATED = D != {} on it.
  U event: an S4a switch (k', (y, z)) of S (Even y, sigma_{k'+1}(y) = z != sigma_{k'}(y)) into an edge FORBIDDEN at some state of
  [k' - n + 1, k' - 1] & S;  (x, z) forbidden at k (level -1): COARSE(W_k(z)) > COARSE(W_k(a)) but not Xi_k(z) > Xi_k(a), a = sigma_k(x),
  COARSE = (cycle node, w(path set)) compared by the cycle node's reward, then w.
Checks: UL_G  every U event with k' in a global C-interval [a, b] (k' < b) has k' - a < n - 1.  GCI-LEN (DATA, L-RED candidate): b - a <= n - 1.
Usage: ulg.py STARTS SEED (--list FILE | FILE.pg[:START] ...) [--nmax N]"""
import os
import random
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import census as C  # noqa: E402
from census import SpecSI, EVEN, ODD, restrict  # noqa: E402

VIOL = []
QUIET = False


def wfun(g):
    order = sorted(range(g.n), key=lambda v: (g.prio[v], v)); rank = {v: i for i, v in enumerate(order)}
    return lambda P: sum((1 if g.prio[v] % 2 == 0 else -1) << rank[v] for v in P)


def lasso_path(f, v):
    return C.lasso(f, v)[0]


def analyse(g, name, states, fbs, T, top):
    n = g.n; SG = SpecSI(g); w = wfun(g)
    A = [C.state_info(g, SG, s, t) for s, t in states]
    key = [(A[k]["lam"], states[k][1]) for k in range(len(A))]
    T["runs"] += 1
    i = 0
    while i < len(A):
        j = i
        while j + 1 < len(A) and key[j + 1] == key[i]:
            j += 1
        x = i
        while x <= j:                                   # runs S: no fallback, lambda_W constant
            y = x
            while y < j and not fbs[y] and A[y + 1]["lamW"] == A[x]["lamW"]:
                y += 1
            run_S(g, name, states, A, x, y, SG, w, T, top)
            x = y + 1
        i = j + 1


def coarse_gt(SG, w, a, b):
    c = SG.rew(a[0], b[0])
    if c:
        return c > 0
    return w(a[1]) > w(b[1])


def run_S(g, name, states, A, x, y, SG, w, T, top):
    n = g.n; tau = states[x][1]; lam = A[x]["lam"]; T["S"] += 1
    classes = sorted(set(lam))
    info = []
    for k in range(x, y + 1):
        s = states[k][0]; Wf = [s[v] if g.owner[v] == EVEN else tau[v] for v in range(n)]
        D = A[k]["D"]; meets = {z: any(q in D for q in lasso_path(Wf, z)) for z in range(n)}
        Ac = {c: frozenset(z for z in range(n) if lam[z] == c and not meets[z]) for c in classes}
        DD = {}
        for c in classes:
            for u in D:
                if lam[u] == c and A[k]["sbar"][u] in Ac[c] and tau[u] in Ac[c]:
                    DD[u] = w(A[k]["Xi"][tau[u]][1]) - w(A[k]["Xi"][A[k]["sbar"][u]][1])
        forb = set()
        for v in range(n):
            if g.owner[v] == EVEN:
                a_ = s[v]
                for z in set(g.succ[v]):
                    if z != a_ and coarse_gt(SG, w, A[k]["W"][z], A[k]["W"][a_]) and not SG.nvo(A[k]["Xi"][a_], A[k]["Xi"][z]) < 0:
                        forb.add((v, z))
        info.append(dict(Ac=Ac, D=D, DD=DD, forb=forb))
    comp = []
    for t in range(x, y):
        P, N = info[t - x], info[t + 1 - x]
        comp.append(all(N["Ac"][c] <= P["Ac"][c] for c in classes) and N["D"] == P["D"] and N["DD"] == P["DD"])
    t = x
    while t < y:
        if not comp[t - x]:
            T["C_cuts"] += 1; t += 1; continue
        a = t
        while t < y and comp[t - x]:
            t += 1
        b = t; L = b - a; gated = bool(info[a - x]["D"])
        T["gcint"] += 1; T["gcint_gated"] += gated
        sl = L - (n - 1); tag = "G_LEN_SLACK_gated" if gated else "G_LEN_SLACK_free"
        if sl > top.get(tag, (-10 ** 9,))[0]:
            top[tag] = (sl, f"{name} interval[{a},{b}] n={n} len={L} |D|={len(info[a - x]['D'])}")
        if gated and sl >= 0:
            T["GCI_LEN_gated_ge0"] += 1
            if not QUIET: print(f"GCI-LEN-GATED-SLACK>=0 {name} interval[{a},{b}] n={n} len={L} slack={sl} D={sorted(info[a - x]['D'])}", flush=True)
        for kk in range(a, b):                          # U events with k' in [a, b - 1]
            s0, s1 = states[kk][0], states[kk + 1][0]
            for v in range(n):
                if g.owner[v] == EVEN and s0[v] != s1[v]:
                    e = (v, s1[v])
                    if any(e in info[q - x]["forb"] for q in range(max(x, kk - n + 1), kk)):
                        T["U_in_gcint"] += 1; idx = kk - a
                        if idx - (n - 1) > top.get("G_IDX_SLACK", (-10 ** 9,))[0]:
                            top["G_IDX_SLACK"] = (idx - (n - 1), f"{name} interval[{a},{b}] k'={kk} edge={e} n={n}")
                        if idx >= n - 1:
                            VIOL.append(f"UL_G {name} interval[{a},{b}] k'={kk} edge={e}")
                            print("VIOLATION UL_G", name, f"interval[{a},{b}] k'={kk} edge={e} n={n}", flush=True)


def main():
    argv = sys.argv[1:]; nmax = 10 ** 9
    if "--nmax" in argv:
        i = argv.index("--nmax"); nmax = int(argv[i + 1]); del argv[i:i + 2]
    starts, seed = int(argv[0]), int(argv[1]); rng = random.Random(seed); T = Counter(); top = {}
    for name, g, st in C.games_from_args(argv[2:]):
        if g.n > nmax:
            continue
        pairs = [("S3", None, None)]
        if st:
            s, t = C.full_start(g, *C.read_start(st, g)); pairs = [("start", s, t)]
        for r in range(starts):
            s, t = C.rand_start(g, rng); pairs.append((f"R{r}", s, t))
        for tag, s, t in pairs:
            try:
                states, fbs = C.run_states(g, s, t, cap=3000)
            except Exception as e:   # noqa: BLE001
                T["runs_failed"] += 1; print("RUNFAIL", name, tag, repr(e)[:150]); continue
            analyse(g, f"{name}[{tag}]", states, fbs, T, top)
    for k in sorted(T):
        print(f"{k}: {T[k]}")
    for k in sorted(top):
        print(f"max {k}: {top[k][0]} | {top[k][1]}")
    print("RESULT", "FAIL" if VIOL else "OK", f"violations={len(VIOL)}")


if __name__ == "__main__":
    main()
