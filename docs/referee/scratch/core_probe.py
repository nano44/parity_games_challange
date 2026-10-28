#!/usr/bin/env python3
"""REFEREE successor 17: checks of packet P-N5-CORE (docs/si/P-N5-CORE-box23.md, sha1 7b66f1ba...) on the own engine rl_engine
(written from SPEC S1-S5 + FIX 1-4 only; no lane code imported). Run with python3 -I from this directory.
Per in-phase transition t -> t+1 (phase = maximal run with lambda_Xi and tau constant):
  C1   sigma_{t+1} != sigma_t                       (+ premises: (SW) switches into I_sigma, R15 pointwise monotone, (V1) Xi = honest play value)
  C2   |P| (transitions) <= sum_w SW_P(w)
  C3   Even w switching, off honest cycle at t and t+1 => Xi_{t+1}(w) > Xi_t(w); intermediate steps checked separately
  C4   Odd u in Q cap U_c, u != c, off honest cycle at t, t+1, clean change y1 -> y2 => kappa_{t+1}(y1) >= kappa_t(y1), strict unless tie at t+1
  C5   every interval I of a phase (all of them when the phase has <= ALLI transitions, else all prefixes/suffixes + random): |I| <= m_E + NOFRESH
  C6   global C-intervals (transition-local reading, GCX F2), scope = whole phase and = fallback-free sub-runs: three counts
MUT=1: C3 demanded of the ABANDONED option sigma_t(w) (Xi_{t+1}(sigma_t w) > Xi_t(sigma_t w)); expected to fail.
MUT=2: C4 demanded strictly (no tie exception); bites iff a clean tie occurs.
MUT=3: C1 demanded at the phase-leaving transitions too; expected to fail (tau-only moves).
MUT=4: C6 third count over arbitrary in-phase intervals (A may grow) against the bound sum_c |A_i(U_c)|; necessity of goodness.
MUT=6: C5 without the NOFRESH term (|I| <= m_E); expected to fail on l121reader_n41 (phase 121 > m_E 103).
MUT=5: C5 with fresh measured against the FIRST state of I only (no injectivity); expected to fail on long phases."""
import sys, os, random, time
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE

MUT = int(os.environ.get("MUT", "0"))
ALLI = int(os.environ.get("ALLI", "40"))
NMAX = int(os.environ.get("NMAX", "200"))
FAILS = []


def fail(cnt, key, *info):
    cnt["FAIL_" + key] += 1
    if cnt["FAIL_" + key] <= 3: FAILS.append((key,) + info)


def parse_start(g, path):
    s = [None] * g.n; t = [None] * g.n
    for l in open(path):
        l = l.split("#")[0].strip()
        if not l: continue
        toks = l.replace(",", " ").split()
        pairs = [x for x in toks if ":" in x or "->" in x]
        if pairs:
            for p in pairs:
                v, w = p.replace("->", ":").split(":"); v, w = int(v), int(w)
                (s if g.owner[v] == 0 else t)[v] = w
        elif len(toks) == 2 and toks[0].lstrip("-").isdigit():
            v, w = int(toks[0]), int(toks[1]); (s if g.owner[v] == 0 else t)[v] = w
    for v in range(g.n):
        x = s if g.owner[v] == 0 else t
        if len(g.succ[v]) == 1:
            if x[v] is not None and x[v] != g.succ[v][0]: print("NOTE start file %s gives forced vertex %d -> %d; using %d" % (path, v, x[v], g.succ[v][0]))
            x[v] = g.succ[v][0]
    if not all((s[v] if g.owner[v] == 0 else t[v]) in g.succ[v] for v in range(g.n)):
        print("NOTE start file %s invalid for its game (move not an edge, or missing); given start skipped" % path); return None
    return s, t


def rand_start(g, r):
    s = [r.choice(g.succ[v]) if g.owner[v] == 0 else None for v in range(g.n)]
    t = [r.choice(g.succ[v]) if g.owner[v] == 1 else None for v in range(g.n)]
    return s, t


def honest_next(g, x):
    return [x["s"][v] if g.owner[v] == 0 else x["sb"][v] for v in range(g.n)]


def oncycle(nx, n):
    """set of vertices on a cycle of the functional graph nx"""
    res = set()
    for v in range(n):
        pre, cyc = RE.lasso(nx, v); res.update(cyc)
    return res


def kap(g, x):
    k = g.key(x); return (k[1], k[2])


def first_D(g, s, t, D, v):
    """first vertex of D on v's (sigma, tau)-play, or None"""
    nx = [s[u] if g.owner[u] == 0 else t[u] for u in range(g.n)]
    seen = set(); x = v
    while x not in seen:
        if x in D: return x
        seen.add(x); x = nx[x]
    return None


def analyse(g, start, cnt, name):
    n = g.n
    st = RE.run(g, start)
    Ev = [v for v in range(n) if g.owner[v] == 0]
    mE = sum(len(g.succ[v]) for v in Ev); nE = len(Ev)
    Q = [u for u in range(n) if g.owner[u] == 1 and len(g.succ[u]) >= 2]
    for x in st:
        x["nx"] = honest_next(g, x)
        x["cyc"] = oncycle(x["nx"], n)
        x["lam"] = tuple(v[0] for v in x["Xi"])
    # (V1): Xi equals the value of the honest play, at every vertex of every state
    for k, x in enumerate(st):
        cnt["V1_chk"] += 1
        if any(RE.play_value(g, x["nx"], v) != x["Xi"][v] for v in range(n)): fail(cnt, "V1", name, k)
    K = len(st); k = 0
    while k < K:
        j = k
        while j + 1 < K and st[j + 1]["lam"] == st[k]["lam"] and st[j + 1]["t"] == st[k]["t"]: j += 1
        phase(g, st, k, j, cnt, name, mE, nE, Q, Ev)
        if MUT == 3 and j + 1 < K:
            cnt["C1m_chk"] += 1
            if st[j + 1]["s"] == st[j]["s"]: fail(cnt, "C1_MUT3", name, j)
        k = j + 1
    cnt["RUN_STATES"] += K


def phase(g, st, a, b, cnt, name, mE, nE, Q, Ev):
    n = g.n
    L = b - a
    cnt["PHASES"] += 1
    if L == 0: cnt["PHASES_L0"] += 1; return
    cnt["TRANS"] += L
    lam = st[a]["lam"]; tau = st[a]["t"]
    classes = sorted(set(lam)); U = {c: {v for v in range(n) if lam[v] == c} for c in classes}
    SW = Counter()
    for t in range(a, b):
        x0, x1 = st[t], st[t + 1]
        sw = [w for w in Ev if x0["s"][w] != x1["s"][w]]
        for w in sw: SW[w] += 1
        # C1
        cnt["C1_chk"] += 1
        if not sw: fail(cnt, "C1", name, t)
        if x0["fb"]: cnt["C1_fb"] += 1
        # (SW)
        Is = set(x0["Is"])
        for w in sw:
            if (w, x1["s"][w]) not in Is: fail(cnt, "SW", name, t, w)
        # R15 pointwise monotone
        if any(g.key(x1["Xi"][v]) < g.key(x0["Xi"][v]) for v in range(n)): fail(cnt, "R15mono", name, t)
        # C3
        for w in sw:
            if w in x0["cyc"] or w in x1["cyc"]:
                cnt["C3_skip_cycle"] += 1
                if not g.key(x1["Xi"][w]) > g.key(x0["Xi"][w]): cnt["C3_cycle_norise"] += 1
                continue
            cnt["C3_chk"] += 1
            y, y0 = x1["s"][w], x0["s"][w]
            if not g.key(x0["Xi"][y]) > g.key(x0["Xi"][y0]): fail(cnt, "C3_step1", name, t, w)
            if not g.key(x1["Xi"][y]) > g.key(x0["Xi"][y0]): fail(cnt, "C3_step2", name, t, w)
            pre1, _ = RE.lasso(x1["nx"], y); pre0, _ = RE.lasso(x0["nx"], y0)
            if w in RE.lasso(x1["nx"], y)[0] + RE.lasso(x1["nx"], y)[1]: fail(cnt, "C3_wfree1", name, t, w)
            if w in RE.lasso(x0["nx"], y0)[0] + RE.lasso(x0["nx"], y0)[1]: fail(cnt, "C3_wfree0", name, t, w)
            if x1["Xi"][y][0] != lam[w] or x0["Xi"][y0][0] != lam[w]: fail(cnt, "C3_cnode", name, t, w)
            # does y's honest t-play pass through w? (the Remark's case)
            if w in sum(RE.lasso(x0["nx"], y), []): cnt["C3_remark_case"] += 1
            if MUT == 1:
                if not g.key(x1["Xi"][y0]) > g.key(x0["Xi"][y0]): fail(cnt, "C3_MUT1", name, t, w)
            else:
                if not g.key(x1["Xi"][w]) > g.key(x0["Xi"][w]): fail(cnt, "C3", name, t, w)
        # C4
        for u in Q:
            c = lam[u]
            if u == c: continue
            y1, y2 = x0["sb"][u], x1["sb"][u]
            if y1 == y2: continue
            cnt["C4_gatechg"] += 1
            if u in x0["cyc"] or u in x1["cyc"]: cnt["C4_skip_cycle"] += 1; continue
            def Y(x):
                return {y for y in g.succ[u] if y in U[c] and u not in sum(RE.lasso(x["nx"], y), [])}
            Y0, Y1 = Y(x0), Y(x1)
            k0 = {y: kap(g, x0["Xi"][y]) for y in g.succ[u] if y in U[c]}
            k1 = {y: kap(g, x1["Xi"][y]) for y in g.succ[u] if y in U[c]}
            # kappa-Y-FORM_D and (A kappa) at both ends (premise checks)
            for x, Yx, kx in ((x0, Y0, k0), (x1, Y1, k1)):
                if not Yx: fail(cnt, "C4_Yempty", name, t, u); continue
                ku = kap(g, x["Xi"][u])
                wt = (g.weight(1 << g.rank[u]) if g.rank[u] > g.rank[c] else 0, 1 if g.prio[c] % 2 else -1)
                if ku != (wt[0] + kx[x["sb"][u]][0], wt[1] + kx[x["sb"][u]][1]): fail(cnt, "C4_Akappa", name, t, u)
                if ku != (wt[0] + min(kx[y] for y in Yx)[0], wt[1] + min(kx[y] for y in Yx)[1]): fail(cnt, "C4_YFORM", name, t, u)
            clean = y2 in Y0 and y1 in Y1
            if not clean:
                cnt["C4_unclean"] += 1
                if y1 in U[c] and not k1[y1] > k0[y1]:
                    cnt["C4_unclean_norise"] += 1
                    if k1[y1] < k0[y1]: cnt["C4_unclean_drop"] += 1
                continue
            cnt["C4_clean"] += 1
            if k1[y2] < k0[y2]: fail(cnt, "C4_M2", name, t, u)
            tie = k1[y1] == k1[y2]
            if tie: cnt["C4_tie"] += 1
            if k1[y1] < k0[y1]: fail(cnt, "C4", name, t, u)
            elif k1[y1] == k0[y1]:
                cnt["C4_eq"] += 1
                if not tie: fail(cnt, "C4_strict", name, t, u)
                if MUT == 2: fail(cnt, "C4_MUT2", name, t, u)
            # hypothesis thin spots: drop "u off cycle at t+1" ? (already excluded); half-clean counts
    # C2
    cnt["C2_chk"] += 1
    if L > sum(SW.values()): fail(cnt, "C2", name, a)
    cnt["C2_maxratio_x1000"] = max(cnt["C2_maxratio_x1000"], 1000 * L // max(1, sum(SW.values())))
    if SW: cnt["MAX_SW1"] = max(cnt["MAX_SW1"], max(SW.values()))
    cnt["MAX_L"] = max(cnt["MAX_L"], L)
    # C5
    held = lambda t: {(w, st[t]["s"][w]) for w in Ev}
    def check_int(i, j):
        """transitions i..j-1 (states i..j)"""
        seen = set(held(i)); nof = 0; fr = 0
        for t in range(i, j):
            new = [(w, st[t + 1]["s"][w]) for w in Ev if st[t]["s"][w] != st[t + 1]["s"][w]]
            f = [e for e in new if e not in seen]
            if f: fr += 1
            else:
                nof += 1
                if not all(e in seen for e in new) or not new: fail(cnt, "C5_paren", name, t)
            if MUT != 5: seen.update(new)
        cnt["C5_chk"] += 1
        bound = mE + (0 if MUT == 6 else nof)
        if j - i > bound: fail(cnt, "C5" + ("_MUT%d" % MUT if MUT in (5, 6) else ""), name, i, j)
        if MUT == 5 and fr > mE: fail(cnt, "C5fr_MUT5", name, i, j)
        cnt["C5_maxfresh"] = max(cnt["C5_maxfresh"], fr)
        cnt["C5_maxnof"] = max(cnt["C5_maxnof"], nof)
    if L <= ALLI:
        for i in range(a, b):
            for j in range(i + 1, b + 1): check_int(i, j)
    else:
        r = random.Random(a * 7919 + b)
        for i in range(a, b): check_int(i, b)
        for j in range(a + 1, b + 1): check_int(a, j)
        for _ in range(200):
            i = r.randrange(a, b); j = r.randrange(i + 1, b + 1); check_int(i, j)
    # C6: global C-intervals in two scopes
    D = {t: frozenset(u for u in Q if st[t]["sb"][u] != tau[u]) for t in range(a, b + 1)}
    A = {}
    for t in range(a, b + 1):
        fd = [first_D(g, st[t]["s"], tau, D[t], v) for v in range(n)]
        for c in classes: A[c, t] = frozenset(v for v in U[c] if fd[v] is None)
    M = lambda t, z: g.weight(st[t]["Xi"][z][1])
    def DD(c, t): return frozenset(u for u in D[t] if u in U[c] and st[t]["sb"][u] in A[c, t] and tau[u] in A[c, t])
    DDs = {(c, t): DD(c, t) for c in classes for t in range(a, b + 1)}
    Dl = lambda t, u: M(t, tau[u]) - M(t, st[t]["sb"][u])
    def good(t):
        if D[t] != D[t + 1]: return False
        for c in classes:
            if not A[c, t + 1] <= A[c, t]: return False
            if DDs[c, t] != DDs[c, t + 1]: return False
            if any(Dl(t, u) != Dl(t + 1, u) for u in DDs[c, t]): return False
        return True
    gd = [good(t) for t in range(a, b)]
    cnt["C6_good"] += sum(gd); cnt["C6_cut"] += L - sum(gd)
    scopes = [("ph", [(a, b)])]
    subs = []; r0 = a
    while r0 < b:
        e = r0
        while e < b and not st[e]["fb"]: e += 1
        if e > r0: subs.append((r0, e))
        r0 = e + 1
    scopes.append(("ff", subs))
    for tag, ranges in scopes:
        for (s0, s1) in ranges:
            ints = []; cur = None
            for t in range(s0, s1):
                if gd[t - a]:
                    if cur is None: cur = t
                else:
                    if cur is not None: ints.append((cur, t)); cur = None
            if cur is not None: ints.append((cur, s1))
            for (i, j) in ints:
                c6(g, st, i, j, A, classes, Ev, Q, mE, cnt, name, tag)
    if MUT == 4:
        for i in range(a, b):
            for j in range(i + 1, min(b, i + ALLI) + 1):
                sh = sum(1 for t in range(i, j) if any(A[c, t + 1] < A[c, t] for c in classes))
                cnt["C6m_chk"] += 1
                if sh > sum(len(A[c, i]) for c in classes): fail(cnt, "C6_MUT4", name, i, j, sh)
                cnt["C6m_maxshrink"] = max(cnt["C6m_maxshrink"], sh)


def c6(g, st, i, j, A, classes, Ev, Q, mE, cnt, name, tag):
    cnt["C6_int_" + tag] += 1; cnt["C6_trans_" + tag] += j - i
    seenE = {(w, st[i]["s"][w]) for w in Ev}; seenO = {(u, st[i]["sb"][u]) for u in Q}
    fe = fo = sh = 0; allthree = 0; sbchg = 0
    for t in range(i, j):
        newE = [(w, st[t + 1]["s"][w]) for w in Ev if st[t]["s"][w] != st[t + 1]["s"][w]]
        newO = [(u, st[t + 1]["sb"][u]) for u in Q if st[t]["sb"][u] != st[t + 1]["sb"][u]]
        a1 = any(e not in seenE for e in newE); a2 = any(e not in seenO for e in newO)
        a3 = any(A[c, t + 1] < A[c, t] for c in classes)
        if any(not A[c, t + 1] <= A[c, t] for c in classes): fail(cnt, "C6_grow", name, t)
        fe += a1; fo += a2; sh += a3
        if newO:
            sbchg += 1
            if a1 or a2 or a3: allthree += 1
        seenE.update(newE); seenO.update(newO)
    bO = sum(len(g.succ[u]) - 1 for u in Q)
    bA = sum(len(A[c, i]) for c in classes)
    if fe > mE: fail(cnt, "C6a", name, tag, i, j)
    if fo > bO: fail(cnt, "C6b", name, tag, i, j)
    if sh > bA or bA > g.n: fail(cnt, "C6c", name, tag, i, j)
    cnt["C6_maxfe"] = max(cnt["C6_maxfe"], fe); cnt["C6_maxfo"] = max(cnt["C6_maxfo"], fo); cnt["C6_maxsh"] = max(cnt["C6_maxsh"], sh)
    cnt["C6_sbchg"] += sbchg; cnt["C6_sbchg_with3"] += allthree


def main(a):
    cnt = Counter(); rng = random.Random(1717); nst = int(os.environ.get("RANDSTARTS", "1"))
    T0 = time.time()
    def do(g, name, extra=None):
        starts = ([("given", extra)] if extra else []) + [("br", RE.best_reward_start(g))] + \
                 [("r%d" % i, rand_start(g, rng)) for i in range(nst)]
        for tag, s0 in starts:
            cnt["RUNS"] += 1
            try: analyse(g, s0, cnt, "%s/%s" % (name, tag))
            except RuntimeError as e: cnt["MAXIT"] += 1
    if a[0] == "list":
        base = a[2] if len(a) > 2 else "."
        for l in open(a[1]):
            p = l.split()
            if not p: continue
            path = os.path.join(base, p[0])
            g = RE.parse(path)
            if g.n > NMAX: cnt["SKIP_N"] += 1; continue
            extra = parse_start(g, os.path.join(base, p[1])) if len(p) > 1 else None
            cnt["GAMES"] += 1; do(g, p[0], extra)
    elif a[0] == "rand":
        N, lo, hi, km, seed = map(int, a[1:6]); r2 = random.Random(seed)
        for i in range(N):
            nn = r2.randint(lo, hi)
            prio = [r2.randrange(nn) for _ in range(nn)]; owner = [r2.randrange(2) for _ in range(nn)]
            succ = [sorted(set(r2.randrange(nn) for _ in range(r2.randint(1, km)))) for _ in range(nn)]
            g = RE.Game(prio, owner, succ); cnt["GAMES"] += 1; do(g, "rand%d" % i)
    else:
        for path in a:
            g = RE.parse(path); st = path[:-3] + ".start"
            extra = parse_start(g, st) if os.path.exists(st) else None
            cnt["GAMES"] += 1; do(g, path, extra)
    print("MUT=%d ALLI=%d NMAX=%d secs=%d" % (MUT, ALLI, NMAX, time.time() - T0))
    for k in sorted(cnt): print(k, cnt[k])
    for f in FAILS: print("FAILEX", f)
    print("CORE", "FAIL" if any(k.startswith("FAIL_") for k in cnt) else "PASS")


if __name__ == "__main__":
    main(sys.argv[1:])
