#!/usr/bin/env python3
"""REFEREE succ. 16 probe for P-N5-DEPTH-box22 §2-§3 (sha1 549c7fb7, l-si 2201aa2d). Own engine only (rl_engine: SPEC). No lane code.
Honest next nxH = (sigma at Even, sigmabar at Odd); W next nxW = (sigma, tau). Cycles of a frame: the cycles of its functional graph.
In each phase ((lambda_Xi, tau) constant), on each maximal run of S4a transitions with lambda_W constant ((H1)), for every end state b:
a := the least state with (H2) (sigmabar constant on [a, b]) and (H3) (the cycle sets of both frames equal and constant on [a, b]); if
(H4) holds at b (H_b acyclic off the cycle vertices; H_b: Even v -> sigma_b v, Odd v not in D -> tau v, u in D -> tau u, sigmabar u;
cycle vertices are sinks), check STATIC-DEPTH on [a, b] (the least a gives the strongest instance; every a' in [a, b] is implied):
 SD     b - a <= max d*;  SDV  every non-cycle v: W-play and honest play at every t in [a + d*(v), b] equal those at b
        (a failure is classed SDV_GENW when W_t(v) = W_b(v) with a different W-play: a local GEN_W failure, outside the theorem)
 SDA    the proof's step (A)/(B) value claim for Even v: W_{t+1}(v) = W_b(v) for t in [a + d*(sigma_b v), b - 1] (needs no GEN_W)
 SHARP  b - a = max d*;  WITHGATE  D != {} on [a, b]
 PE     PURE-END at every in-phase state b at which every gate (u in D_b) is D-direct (sigmabar u, tau u in A_b, A_b := the vertices
        whose (sigma, tau)-play meets no D_b vertex): (H4) holds at b and the two cycle sets are equal
 GCI    GCI-LEN-rhoF: R1 global C-intervals (gcx_probe's transition-local reading) [s, e] of the run with sigmabar constant, (H3) on [s, e] and
        (H4) at e: e - s <= n - 1 (counted; it is STATIC-DEPTH's instance)
Mutation MUT=1: SDV from a + d*(v) - 1 (must bite).  Usage: depth_probe.py rand N nmin nmax kmax seed | files[:start]...  (RANDSTARTS, MAXN, NOS3)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, dual_probe as D, epr_probe as E
from gcx_probe import load_start
from root_probe import firstD
EX = []
MUT = int(os.environ.get("MUT", "0"))


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def cycles(nx):
    seen = {}; out = set()
    for v in range(len(nx)):
        x = v; path = []
        while x not in seen and x not in path: path.append(x); x = nx[x]
        if x in path:
            cyc = path[path.index(x):]
            m = min(cyc); i = cyc.index(m); out.add(tuple(cyc[i:] + cyc[:i]))
        for y in path: seen[y] = True
    return frozenset(out)


def play(nx, v):
    pre, cy = RE.lasso(nx, v)
    return tuple(pre), tuple(cy)


def analyse(g, start, cnt, name):
    st = RE.run(g, start); n = g.n
    Q = {v for v in range(n) if g.owner[v] == 1}
    for x in st:
        x["nxH"] = [x["s"][v] if g.owner[v] == 0 else x["sb"][v] for v in range(n)]
        x["nxW"] = [x["s"][v] if g.owner[v] == 0 else x["t"][v] for v in range(n)]
        x["W"] = E.wval(g, x["s"], x["t"])
        x["D"] = frozenset(u for u in Q if x["sb"][u] != x["t"][u])
        x["cyc"] = (cycles(x["nxH"]), cycles(x["nxW"]))
        x["lamW"] = tuple(w[0] for w in x["W"])
    K = len(st); k = 0
    while k < K:
        j = k; lam = tuple(v[0] for v in st[k]["Xi"])
        while j + 1 < K and tuple(v[0] for v in st[j + 1]["Xi"]) == lam and st[j + 1]["t"] == st[k]["t"]: j += 1
        for b in range(k, j + 1): pure_end(g, st, b, cnt, name)
        r = k
        while r <= j:
            e = r
            while e < j and not st[e]["fb"] and st[e + 1]["lamW"] == st[r]["lamW"]: e += 1
            if e > r: runH1(g, st, r, e, cnt, name)
            r = e + 1
        k = j + 1


def Hb(g, x):
    n = g.n; cv = {v for c in x["cyc"][0] for v in c}
    succ = {}
    for v in range(n):
        if v in cv: succ[v] = []
        elif g.owner[v] == 0: succ[v] = [x["s"][v]]
        elif v in x["D"]: succ[v] = sorted({x["t"][v], x["sb"][v]})
        else: succ[v] = [x["t"][v]]
    return cv, succ


def dstar(g, cv, succ):
    """d* by DFS; None if H_b has a cycle off the cycle vertices"""
    n = g.n; d = {}; state = {}
    def rec(v):
        if v in cv: return 0
        if state.get(v) == 1: raise ValueError
        if v in d: return d[v]
        state[v] = 1
        val = max(rec(y) for y in succ[v]) + (1 if g.owner[v] == 0 else 0)
        state[v] = 2; d[v] = val; return val
    try:
        for v in range(n): rec(v)
    except (ValueError, RecursionError): return None
    return d


def pure_end(g, st, b, cnt, name):
    x = st[b]; n = g.n
    fu = [firstD(g, x["s"], x["t"], x["D"], v) for v in range(n)]
    A = {v for v in range(n) if fu[v] is None}
    if not all(x["sb"][u] in A and x["t"][u] in A for u in x["D"]): return
    cnt["PE_chk"] += 1
    if x["D"]: cnt["PE_withgate"] += 1
    if x["cyc"][0] != x["cyc"][1]: fail(cnt, "PE_cyc", name, b); return
    cv, succ = Hb(g, x)
    if dstar(g, cv, succ) is None: fail(cnt, "PE_H4", name, b)


def runH1(g, st, r, e, cnt, name):
    n = g.n; cnt["H1_runs"] += 1
    for b in range(r, e + 1):
        a = b
        while a > r and st[a - 1]["sb"] == st[b]["sb"] and st[a - 1]["cyc"] == st[b]["cyc"]: a -= 1
        if st[b]["cyc"][0] != st[b]["cyc"][1]: cnt["H3_noncommon"] += 1; continue
        if a == b: continue
        cv, succ = Hb(g, st[b])
        d = dstar(g, cv, succ)
        if d is None: cnt["H4_fail"] += 1; continue
        cnt["SD_chk"] += 1; md = max(d.values()) if d else 0
        if st[b]["D"]: cnt["SD_withgate"] += 1
        if b - a > md: fail(cnt, "SD", name, a, b, md)
        if b - a == md: cnt["SD_sharp"] += 1
        cnt["MAX_len_minus_n1"] = max(cnt["MAX_len_minus_n1"], b - a - (n - 1) + 1000)
        if st[b]["D"]: cnt["MAX_len_gate"] = max(cnt["MAX_len_gate"], b - a)
        Wb = st[b]["W"]
        for v in range(n):
            if v in cv: continue
            t0 = a + d[v] - (1 if MUT == 1 else 0)
            pWb, pHb = play(st[b]["nxW"], v), play(st[b]["nxH"], v)
            for t in range(max(t0, a), b + 1):
                cnt["SDV_chk"] += 1
                if play(st[t]["nxW"], v) != pWb or play(st[t]["nxH"], v) != pHb:
                    if st[t]["W"][v] == Wb[v] and play(st[t]["nxW"], v) != pWb: cnt["SDV_GENW"] += 1
                    else: fail(cnt, "SDV", name, a, b, v, t, d[v])
                    break
            if g.owner[v] == 0:
                y = st[b]["s"][v]
                for t in range(a + d.get(y, 0), b):
                    cnt["SDA_chk"] += 1
                    if st[t + 1]["W"][v] != Wb[v]: fail(cnt, "SDA", name, a, b, v, t)
    gci(g, st, r, e, cnt, name)


def gci(g, st, r, e, cnt, name):
    """R1 global C-intervals of the run [r, e] (gcx_probe's reading), then GCI-LEN-rhoF's hypotheses"""
    n = g.n; tau = st[r]["t"]
    lam = tuple(v[0] for v in st[r]["Xi"]); cls = sorted(set(lam))
    U = {c: {v for v in range(n) if lam[v] == c} for c in cls}
    fu = {t: [firstD(g, st[t]["s"], st[t]["t"], st[t]["D"], v) for v in range(n)] for t in range(r, e + 1)}
    A = {(c, t): {v for v in U[c] if fu[t][v] is None} for c in cls for t in range(r, e + 1)}
    M = lambda t, z: g.weight(st[t]["Xi"][z][1])
    DD = {(c, t): {u for u in st[t]["D"] if u in U[c] and st[t]["sb"][u] in A[c, t] and tau[u] in A[c, t]} for c in cls for t in range(r, e + 1)}
    Dl = lambda t, u: M(t, tau[u]) - M(t, st[t]["sb"][u])
    def good(t):
        if st[t]["D"] != st[t + 1]["D"]: return False
        for c in cls:
            if not A[c, t + 1] <= A[c, t]: return False
            if any(Dl(t, u) != Dl(t + 1, u) for u in DD[c, t] & DD[c, t + 1]): return False
        return True
    t = r
    while t < e:
        if not good(t): t += 1; continue
        s = t
        while t < e and good(t): t += 1
        cnt["GCI_ints"] += 1
        if all(st[k]["sb"] == st[s]["sb"] and st[k]["cyc"] == st[s]["cyc"] for k in range(s, t + 1)) and st[t]["cyc"][0] == st[t]["cyc"][1]:
            cv, succ = Hb(g, st[t])
            if dstar(g, cv, succ) is not None:
                cnt["GCI_chk"] += 1
                if st[s]["D"]: cnt["GCI_withgate"] += 1
                cnt["MAX_GCI_len_minus_n1"] = max(cnt["MAX_GCI_len_minus_n1"], t - s - (n - 1) + 1000)
                if t - s > n - 1: fail(cnt, "GCI", name, s, t)


def main(a):
    sys.setrecursionlimit(100000)
    cnt = Counter(); rng = random.Random(2222); nst = int(os.environ.get("RANDSTARTS", "2"))
    def do(g, name, r, extra=None):
        starts = ([extra] if extra else []) + ([] if (extra and os.environ.get("NOS3")) else [RE.best_reward_start(g)]) + \
                 [D.rand_start(g, r) for _ in range(nst)]
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
            if path.endswith(".start"): continue
            try: g = RE.parse(path)
            except Exception: cnt["parse_err"] += 1; continue
            if g.n > int(os.environ.get("MAXN", "40")): cnt["skip_big"] += 1; continue
            if not sp and os.path.exists(path[:-3] + ".start"): sp = path[:-3] + ".start"
            ex = None
            if sp:
                try: ex = load_start(g, sp)
                except Exception: cnt["start_err"] += 1
            do(g, os.path.relpath(path), random.Random(os.path.relpath(path)), ex)
    for k in sorted(cnt):
        v = cnt[k] - 1000 if k.startswith("MAX_") and "minus" in k else cnt[k]
        print(k, v)
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
