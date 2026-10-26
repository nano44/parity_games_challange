#!/usr/bin/env python3
"""REFEREE succ. 14 probe for packet P-N5-HONFF (docs/new/P-N5-HONFF-box47.md, pin 4a0a8aba, sha1 98101d1f...). Own engine only (rl_engine,
hon_probe's exact LEV by simple-path enumeration in G_tau; epr_probe.wval). No lane code. Per phase ((lambda_Xi, tau) constant):
 GEN    FB-RISE (a): every in-phase fallback t -> t+1: LEV(t+1) >= min(LEV(t) + 1, LEV_odd(t), n - 1)
 FBR    FB-RISE (b): ... and every W-honest h <= t in the phase: LEV(t+1) >= min(LEV(h) + 1, n - 1)
 ODDH   the step inside (b): LEV_odd(t) >= min(LEV(h) + 1, n - 1)
 HFF    Theorem HON-FF: W-honest states <= 4n^2 - 3n; and its content: every gap between consecutive unsaturated honest states rises (GAPR),
        saturated honest states span <= 4n(n - 1) transitions
 H0FF   D = {} states, N_0, D = {}-epoch transitions <= 4n^2 - 3n;  R1FF  {u}-intervals <= 1 + 4n^2 - 3n + X_dir + X_big
 CTRL   control (not claimed): LEV(t+1) >= min(LEV(t) + 1, n - 1) without the Odd term: must fail somewhere (packet §3 CTRL_T)
 MUT=1  control: FBR asks LEV(h) + 2
LEV is computed only when the path enumeration stays under BUDGET (env, default 2e6 path extensions per phase); else the phase is UNK.
Usage: ff_probe.py rand N nmin nmax kmax seed | files[:start]...   (env RANDSTARTS default 2, MAXN 40)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, dual_probe as D, epr_probe as E, hon_probe as HP
EX = []
MUT = int(os.environ.get("MUT", "0"))


class Over(Exception): pass


def best_le_budget(g, succ, cyc, n, budget):
    best = [[None] * n for _ in range(g.n)]; used = 0
    for x in range(g.n):
        byL = [None] * n
        stack = [(x, (x,))]
        while stack:
            v, p = stack.pop(); used += 1
            if used > budget: raise Over()
            if v in cyc:
                val = (v, 0, 0)
                for w in reversed(p[:-1]): val = g.ext(w, val)
                L = len(p) - 1
                if byL[L] is None or g.key(val) > g.key(byL[L]): byL[L] = val
            if len(p) - 1 >= n - 1: continue
            for w in succ[v]:
                if w not in p: stack.append((w, p + (w,)))
        cur = None
        for j in range(n):
            if byL[j] is not None and (cur is None or g.key(byL[j]) > g.key(cur)): cur = byL[j]
            best[x][j] = cur
    return best


def level(g, V, best, n, xs):
    lv = -1
    for j in range(n):
        if all(best[x][j] is None or g.key(V[x]) >= g.key(best[x][j]) for x in xs): lv = j
        else: break
    return lv


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def analyse(g, start, cnt, name):
    st = RE.run(g, start); n = g.n
    Q = [v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1]
    odd = [v for v in range(n) if g.owner[v] == 1]
    info = []
    for x in st:
        W = E.wval(g, x["s"], x["t"])
        info.append(dict(lam=tuple(v[0] for v in x["Xi"]), t=tuple(x["t"]), hon=(list(x["Xi"]) == list(W)),
                         D=frozenset(q for q in Q if x["sb"][q] != x["t"][q]), sbQ=tuple(x["sb"][q] for q in Q)))
    K = len(st); k = 0
    while k < K:
        j = k
        while j + 1 < K and info[j + 1]["lam"] == info[k]["lam"] and info[j + 1]["t"] == info[k]["t"]: j += 1
        phase(g, st, info, k, j, cnt, name, n, Q, odd)
        k = j + 1


def phase(g, st, info, a, b, cnt, name, n, Q, odd):
    cnt["PHASES"] += 1; bnd = 4 * n * n - 3 * n
    H = [k for k in range(a, b + 1) if info[k]["hon"]]
    cnt["HFF_chk"] += 1; cnt["MAX_HONEST"] = max(cnt["MAX_HONEST"], len(H))
    if len(H) > bnd: fail(cnt, "HFF", name, a, len(H))
    d0 = [k for k in range(a, b + 1) if not info[k]["D"]]
    eps = []; k = a
    while k <= b:
        j = k
        while j + 1 <= b and info[j + 1]["sbQ"] == info[k]["sbQ"]: j += 1
        eps.append((k, j)); k = j + 1
    N0 = sum(1 for (x, y) in eps if not info[x]["D"])
    tr0 = sum(1 for (x, y) in eps if not info[x]["D"] for kk in range(x, y + 1) if kk < b)
    cnt["H0FF_chk"] += 1
    if max(len(d0), N0, tr0) > bnd: fail(cnt, "H0FF", name, a)
    ints = []; k = a
    while k <= b:
        if len(info[k]["D"]) == 1:
            j = k
            while j + 1 <= b and info[j + 1]["D"] == info[k]["D"]: j += 1
            ints.append((k, j)); k = j + 1
        else: k += 1
    xd = sum(1 for (x, y) in ints if x > a and len(info[x - 1]["D"]) == 1)
    xb = sum(1 for (x, y) in ints if x > a and len(info[x - 1]["D"]) >= 2)
    cnt["R1FF_chk"] += 1
    if len(ints) > 1 + bnd + xd + xb: fail(cnt, "R1FF", name, a)
    fbs = [t for t in range(a, b) if st[t]["fb"]]
    if not fbs and len(H) < 2: return
    if n > int(os.environ.get("LEVMAX", "40")): cnt["SKIP_N"] += 1; return
    lam = info[a]["lam"]; t0 = list(st[a]["t"])
    succ_t = [list(g.succ[v]) if g.owner[v] == 0 else [t0[v]] for v in range(n)]
    try: best = best_le_budget(g, succ_t, {u for u in range(n) if lam[u] == u}, n, float(os.environ.get("BUDGET", "2e6")))
    except Over: cnt["UNK_PHASES"] += 1; return
    LEV = {k: level(g, st[k]["Xi"], best, n, range(n)) for k in range(a, b + 1)}
    LO = {k: level(g, st[k]["Xi"], best, n, odd) for k in range(a, b + 1)}
    for t in fbs:
        cnt["GEN_chk"] += 1; cnt["FB_nonhonest"] += not info[t]["hon"]
        if LEV[t + 1] < min(LEV[t] + 1, LO[t], n - 1): fail(cnt, "GEN", name, t, LEV[t], LO[t], LEV[t + 1])
        if LEV[t + 1] < min(LEV[t] + 1, n - 1):
            cnt["CTRL_fails"] += 1
            if LO[t] > LEV[t]: fail(cnt, "CTRLODD", name, t)  # every control failure must have the Odd term binding
        for h in H:
            if h > t: break
            cnt["FBR_chk"] += 1
            if LEV[t + 1] < min(LEV[h] + (2 if MUT == 1 else 1), n - 1): fail(cnt, "FBR", name, t, h, LEV[h], LEV[t + 1])
            if LO[t] < min(LEV[h] + 1, n - 1): fail(cnt, "ODDH", name, t, h)
        if H and H[0] < t and not info[t]["hon"] and any(H[i] < t < H[i + 1] for i in range(len(H) - 1)): cnt["FB_inside_gap"] += 1
    uns = [h for h in H if LEV[h] < n - 1]; sat = [h for h in H if LEV[h] >= n - 1]
    for i in range(len(uns) - 1):
        cnt["GAPR_chk"] += 1
        if any(uns[i] <= t < uns[i + 1] and not info[t]["hon"] for t in fbs): cnt["GAPR_withinsidefb"] += 1
        if LEV[uns[i + 1]] < LEV[uns[i]] + 1: fail(cnt, "GAPR", name, uns[i], uns[i + 1])
    if uns and sat and min(sat) < max(uns): fail(cnt, "HFF", name, a, "order")
    if sat and sat[-1] - sat[0] > 4 * n * (n - 1): fail(cnt, "HFF", name, a, "tail")


def main(a):
    cnt = Counter(); rng = random.Random(1447); nst = int(os.environ.get("RANDSTARTS", "2"))
    def do(g, name, r, extra=None):
        starts = ([extra] if extra else []) + [RE.best_reward_start(g)] + [D.rand_start(g, r) for _ in range(nst)]
        for j, s0 in enumerate(starts):
            cnt["RUNS"] += 1; analyse(g, s0, cnt, "%s/%d" % (name, j))
    if a[0] == "rand":
        N, lo, hi, km, seed = map(int, a[1:6]); r2 = random.Random(seed)
        for i in range(N):
            nn = r2.randint(lo, hi)
            do(D.rand_ck(r2, nn, r2.randint(0, min(km, nn - 1))), "rand%d" % i, rng)
    else:
        for f in a:
            path, _, sp = f.partition(":")
            g = RE.parse(path)
            if g.n > int(os.environ.get("MAXN", "40")): cnt["skip_big"] += 1; continue
            do(g, os.path.relpath(path), random.Random(os.path.relpath(path)), HP.parse_start(g, sp) if sp else None)
    for k in sorted(cnt): print(k, cnt[k])
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
