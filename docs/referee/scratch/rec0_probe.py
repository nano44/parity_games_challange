#!/usr/bin/env python3
"""REFEREE succ. 13 probe for packet P-N5-REC0 (docs/new/P-N5-REC0-box45.md, pin 64506ecf, sha1 343239b5...). Own engine only (rl_engine,
SPEC from the text; epr_probe.wval). No lane code. Per phase of every N5 run (phase = (lambda_Xi, tau) constant; epochs = sigma-bar|Q constant):
 REC0   N_0 <= (f + 1)(n + 1) + 4n(n - 1) + 1          (N_0 := epochs with D_E = {}; f := in-phase fallbacks)
 EP0    len(E) <= n + m for D_E = {}                    (len(E) := in-phase transitions with source in E)
 With LEVELS=1 (exact, exponential: only n <= LEVELMAX, default 9), level(k) := max j <= n-1 such that W_k(x) >= value(r) for every simple
 path r of G_tau with <= j edges from x to a cycle node u of lambda:
 STEP1  in-phase S4a step k -> k+1, k D={} (hence all-unsplit), k+1 all-unsplit => level(k+1) >= min(level(k) + 1, n - 1)
 STEP2  in-phase S4a step, k and k+1 all-unsplit => level(k+1) >= level(k)
 BASE   every all-unsplit state has level >= 0 (the empty path)
 SAT    at an all-unsplit state W <= B pointwise; a D={} state of level n-1 has W = B
 RUNIII per fallback-free run, the epoch-last S4a transitions from a D={} state of U(R) into U(R) with source < t number <= n - 1
 T4     t* - t <= 4n(n - 1)
Usage: rec0_probe.py rand N nmin nmax kmax seed | files...   (env RANDSTARTS=N default 3, LEVELS=0/1, LEVELMAX, MAXN)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rho_probe as RP, dual_probe as D, epr_probe as E
EX = []


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def paths_info(g, t, lam, W, n):
    """returns (level, B): level = max j <= n-1 with W(x) >= value(r) for all simple r (<= j edges) to cycle nodes of lam; B(x) = best value"""
    cyc = {u for u in range(g.n) if lam[u] == u}
    succ = [[t[v]] if g.owner[v] == 1 else g.succ[v] for v in range(g.n)]
    first_bad = n  # smallest edge count of a violating path
    B = [None] * g.n
    for x in range(g.n):
        best = None
        # enumerate simple paths from x; value computed backwards, so store the path
        stack = [(x, [x])]
        while stack:
            v, p = stack.pop()
            if v in cyc:
                val = (v, 0, 0)
                for w in reversed(p[:-1]): val = g.ext(w, val)
                L = len(p) - 1
                if best is None or g.key(val) > g.key(best): best = val
                if g.key(W[x]) < g.key(val) and L < first_bad: first_bad = L
            if len(p) - 1 >= n - 1: continue
            for w in succ[v]:
                if w not in p: stack.append((w, p + [w]))
        B[x] = best
    return min(first_bad - 1, n - 1), B


def analyse(g, st, cnt, name, levels):
    states = RE.run(g, st)
    n, m = g.n, sum(len(s) for s in g.succ)
    Q = [v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1]
    info = []
    for x in states:
        lam = [v[0] for v in x["Xi"]]
        W = E.wval(g, x["s"], x["t"])
        lamW = [v[0] for v in W]
        D0 = all(x["sb"][q] == x["t"][q] for q in Q)
        info.append(dict(lam=lam, W=W, unsplit=(lamW == lam), D0=D0, sbQ=tuple(x["sb"][q] for q in Q), t=tuple(x["t"]), fb=x["fb"]))
    # phases
    K = len(states); k = 0
    while k < K:
        j = k
        while j + 1 < K and info[j + 1]["lam"] == info[k]["lam"] and info[j + 1]["t"] == info[k]["t"]: j += 1
        phase(g, states, info, k, j, cnt, name, levels, n, m)
        k = j + 1


def phase(g, states, info, a, b, cnt, name, levels, n, m):
    cnt["PHASES"] += 1
    f = sum(1 for k in range(a, b) if info[k]["fb"])
    # epochs
    eps = []; k = a
    while k <= b:
        j = k
        while j + 1 <= b and info[j + 1]["sbQ"] == info[k]["sbQ"]: j += 1
        eps.append((k, j)); k = j + 1
    N0 = 0
    for (x, y) in eps:
        if info[x]["D0"]:
            N0 += 1
            ln = (y - x) + (1 if y < b else 0)
            cnt["EP0_chk"] += 1
            if ln > n + m: fail(cnt, "EP0", name, x, ln)
    bound = (f + 1) * (n + 1) + 4 * n * (n - 1) + 1
    cnt["REC0_chk"] += 1; cnt["MAX_N0"] = max(cnt["MAX_N0"], N0)
    if N0 > bound: fail(cnt, "REC0", name, a, N0, f, bound)
    if f + 1 and N0 / (f + 1) > cnt.get("MAX_N0_per_f1x100", 0) / 100: cnt["MAX_N0_per_f1x100"] = int(100 * N0 / (f + 1))
    if not levels or n > int(os.environ.get("LEVELMAX", "9")): return
    lev, Bs = {}, {}
    for k in range(a, b + 1):
        if info[k]["unsplit"]:
            L, B = paths_info(g, states[k]["t"], info[k]["lam"], info[k]["W"], n)
            lev[k], Bs[k] = L, B
            cnt["BASE_chk"] += 1
            if L < 0: fail(cnt, "BASE", name, k)
            cnt["SAT_chk"] += 1
            if any(g.key(info[k]["W"][x]) > g.key(B[x]) for x in range(n)): fail(cnt, "SAT", name, k, "W>B")
            if info[k]["D0"] and L >= n - 1 and info[k]["W"] != B: fail(cnt, "SAT", name, k, "lev n-1 but W != B")
    for k in range(a, b):
        if info[k]["fb"] or not (info[k]["unsplit"] and info[k + 1]["unsplit"]): continue
        cnt["STEP2_chk"] += 1
        if lev[k + 1] < lev[k]: fail(cnt, "STEP2", name, k, lev[k], lev[k + 1])
        if info[k]["D0"]:
            cnt["STEP1_chk"] += 1
            if lev[k + 1] < min(lev[k] + 1, n - 1): fail(cnt, "STEP1", name, k, lev[k], lev[k + 1])
    # t, t*
    d0 = [k for k in range(a, b + 1) if info[k]["D0"]]
    sat = [k for k in d0 if lev[k] >= n - 1]
    t = sat[0] if sat else None
    if t is not None:
        cnt["T4_chk"] += 1
        if d0[-1] - t > 4 * n * (n - 1): fail(cnt, "T4", name, t, d0[-1])
    # runs and kind (iii)
    k = a
    while k < b:
        if info[k]["fb"]: k += 1; continue
        r0 = k
        while k < b and not info[k]["fb"]: k += 1
        run = list(range(r0, k + 1))  # states of the run
        U = []
        for s in run:
            if info[s]["unsplit"]: U.append(s)
            else: break
        if any(info[s]["unsplit"] for s in run[len(U):]): fail(cnt, "PREFIX", name, r0)
        Uset = set(U); kiii = 0
        epoch_last = {y for (x, y) in eps}
        for s in U:
            if s + 1 in Uset and s < k and info[s]["D0"] and s in epoch_last and (t is None or s < t): kiii += 1
        cnt["RUNIII_chk"] += 1; cnt["MAX_KIII"] = max(cnt["MAX_KIII"], kiii)
        if kiii > n - 1: fail(cnt, "RUNIII", name, r0, kiii)


def main(a):
    cnt = Counter(); rng = random.Random(1313); levels = os.environ.get("LEVELS", "0") == "1"
    nst = int(os.environ.get("RANDSTARTS", "3"))
    def do(g, name, r):
        for j, st in enumerate([RE.best_reward_start(g)] + [D.rand_start(g, r) for _ in range(nst)]):
            cnt["RUNS"] += 1; analyse(g, st, cnt, "%s/%d" % (name, j), levels)
    if a[0] == "rand":
        N, lo, hi, km, seed = map(int, a[1:6]); r2 = random.Random(seed)
        for i in range(N):
            n = r2.randint(lo, hi)
            do(D.rand_ck(r2, n, r2.randint(0, min(km, n - 1))), "rand%d" % i, rng)
    else:
        for f in a:
            g = RE.parse(f)
            if g.n > int(os.environ.get("MAXN", "64")): cnt["skip_big"] += 1; continue
            do(g, os.path.relpath(f), random.Random(os.path.relpath(f)))
    for k in sorted(cnt): print(k, cnt[k])
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
