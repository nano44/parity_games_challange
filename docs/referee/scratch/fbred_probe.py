#!/usr/bin/env python3
"""REFEREE succ. 11 probe for packet P-N5-FBRED (docs/new/P-N5-FBRED-box44.md, pin c3f6f2bf, sha1 11b15455...). Own engine
(rl_engine via dual_probe.run5 for start pairs; no lane code). Every game.
Per phase (lambda_Xi, tau constant): C = honest cycle nodes, Q = Odd vertices of out-degree >= 2, T = C u Q, classes U_c, kappa per class.
 FBR    kappa-FB-ROUND_D at every in-phase fallback: kappa_{k+1}(v) >= kwt_c(v) + kappa_k(x), Even v in U_c - {c}, successor x in U_c
 YF     kappa-Y-FORM_D: q in Q n U_c, q != c, q on no honest cycle: Xi(q) = min_{y in Y^q} q (+) Xi(y) (same as the kappa form)
 EXS    EXIT-SWITCH_D: at a fallback with S_c != {}, some u in S_c whose x*_u's k-play meets T n U_c before u
 FEX    FREEZE-EXIT_D: g_j, j >= |U_c|, i-th fallback (by source state) of its Q_c-run, i >= |U_c|  =>  S_c = {}
 CNO    CN-ONLY_D: a fallback with S = {}: every gate (y, z) has lambda(y) = y and lev = -1, and k+1 is the last state of the phase
 RED    f <= 1 + (n-1)(2 + rho); REDL f <= 1 + (n-1) + (n-1) N_late
 TV     Lemma TV at qualifying states (z in U_c - T): kappa_t(z) = max(kopt_c(z), max_q kopt^q(z) + kappa(q)) (brute-force simple paths, n <= 16)
Usage: fbred_probe.py lib | rand N nmin nmax kmax seed | files...   (env RANDSTARTS=N)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, rho_probe as RP, dual_probe as D
EX = []


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def kap(g, x, c):
    s = 1 if g.prio[c] % 2 else -1
    return (g.weight(x[1]), s * x[2])


def kwt(g, v, c):
    s = 1 if g.prio[c] % 2 else -1
    w = 0
    if g.rank[v] > g.rank[c]: w = (1 << g.rank[v]) if g.prio[v] % 2 == 0 else -(1 << g.rank[v])
    return (w, s)


def add(a, b): return (a[0] + b[0], a[1] + b[1])


def lev(x, y):
    if x == y: return -2
    if x[0] != y[0]: return 10 ** 6
    d = x[1] ^ y[1]
    return d.bit_length() - 1 if d else -1


def kopt_paths(g, Uc, nodes, src, sink, c):
    """max kwt-sum over simple paths in the graph on `nodes` (Even: edges inside, Odd non-sink: forced edge inside) from src to sink,
    excluding the sink's weight; None if no path"""
    best = [None]
    def dfs(x, seen, acc):
        if x == sink:
            if best[0] is None or acc > best[0]: best[0] = acc
            return
        succ = g.succ[x]
        if g.owner[x] == 1 and len(succ) > 1: return
        for y in succ:
            if y in nodes and y not in seen:
                dfs(y, seen | {y}, add(acc, kwt(g, x, c)))
    dfs(src, {src}, (0, 0))
    return best[0]


def run_check(g, start, cnt, name):
    A = D.run5(g, start)
    n = g.n
    Q = {v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1}
    info = []
    for a in A:
        Xi, sb = RE.evaluate(g, a["s"])
        hg = [a["s"][v] if g.owner[v] == 0 else sb[v] for v in range(n)]
        info.append(dict(Xi=Xi, sb=sb, hg=hg))
    T_ = len(A) - 1
    key = [(tuple(x[0] for x in info[k]["Xi"]), tuple(A[k]["t"])) for k in range(T_ + 1)]
    k = 0
    while k <= T_:
        j = k
        while j < T_ and key[j] == key[j + 1]: j += 1
        p0, p1 = k, j; k = j + 1
        lam = key[p0][0]
        C = set(lam[v] for v in range(n)); T = C | Q
        U = {c: {v for v in range(n) if lam[v] == c} for c in C}
        fbs = [x for x in range(p0, p1) if A[x]["fb"]]
        f = len(fbs)
        # Q-runs, Q_c-runs, rho
        rho = sum(1 for x in range(p0, p1) for q in Q if info[x]["Xi"][q] != info[x + 1]["Xi"][q])
        def runid(x, qs):
            r = 0
            for y in range(p0, x):
                if any(info[y]["Xi"][q] != info[y + 1]["Xi"][q] for q in qs): r += 1
            return r
        cnt["phases"] += 1; cnt["fb_total"] += f
        cnt["max_f"] = max(cnt["max_f"], f); cnt["max_rho"] = max(cnt["max_rho"], rho)
        if f > 1 + (n - 1) * (2 + rho): fail(cnt, "RED", name, p0, f, rho)
        late = [x for jj, x in enumerate(fbs, 1) if jj >= n]
        Nlate = len({runid(x, Q) for x in late})
        if f > 1 + (n - 1) + (n - 1) * Nlate: fail(cnt, "REDL", name, p0)
        cnt["late_fallbacks"] += len(late)
        for jj, x in enumerate(fbs, 1):
            a, b = A[x], A[x + 1]; Xi0, Xi1 = info[x]["Xi"], info[x + 1]["Xi"]
            Sk = {v for v in range(n) if g.owner[v] == 0 and a["s"][v] != b["s"][v]}
            S = Sk - T
            # FB-ROUND
            for c in C:
                for v in U[c] - {c}:
                    if g.owner[v] != 0: continue
                    for xx in g.succ[v]:
                        if xx not in U[c]: continue
                        cnt["FBR_chk"] += 1
                        if kap(g, Xi1[v], c) < add(kwt(g, v, c), kap(g, Xi0[xx], c)): fail(cnt, "FBR", name, x, v, xx)
            if not S:
                cnt["CNO_chk"] += 1
                for (y, z) in a["Is"]:
                    if lam[y] != y or lev(Xi0[a["s"][y]], Xi0[z]) != -1: fail(cnt, "CNO", name, x, y, z)
                if x + 1 != p1: fail(cnt, "CNO_last", name, x)
            for c in C:
                Sc = S & U[c]
                if not Sc: continue
                cnt["EXS_chk"] += 1
                ok = False
                for u in Sc:
                    y = b["s"][u]; seen = set()
                    while y not in seen:
                        seen.add(y)
                        if y in T and y in U[c]: ok = True; break
                        if y == u: break
                        y = info[x]["hg"][y]
                    if ok: break
                if not ok: fail(cnt, "EXS", name, x, c)
                # FREEZE-EXIT (conservative): Q_c-run index by source state
                Qc = Q & U[c]
                rid = runid(x, Qc)
                i = sum(1 for y in fbs if y <= x and runid(y, Qc) == rid)
                if jj >= len(U[c]) and i >= len(U[c]): fail(cnt, "FEX", name, x, c, jj, i)
                if jj >= len(U[c]) and i >= len(U[c]) - 0: cnt["FEX_hyp"] += 1
        # Y-FORM and TV at every state of the phase
        for t in range(p0, p1 + 1):
            Xi = info[t]["Xi"]; hg = info[t]["hg"]
            for q in Q:
                c = lam[q]
                if c == q: continue
                pre, cyc = RE.lasso(hg, q)
                if q in cyc: continue
                Y = []
                for y in g.succ[q]:
                    if lam[y] != c: continue
                    pre2, cyc2 = RE.lasso(hg, y)
                    if q not in pre2 and q not in cyc2: Y.append(y)
                cnt["YF_chk"] += 1
                if not Y: fail(cnt, "YF_empty", name, t, q); continue
                m = min((add(kwt(g, q, c), kap(g, Xi[y], c)) for y in Y))
                if kap(g, Xi[q], c) != m: fail(cnt, "YF", name, t, q)
            if n <= 16:
                for c in C:
                    Uc = U[c]
                    fb_before = sum(1 for y in fbs if y < t)
                    if fb_before < len(Uc): continue      # t > g_{|U_c| - 1}
                    rid = runid(t, Q)
                    fq = sum(1 for y in fbs if y < t and runid(y, Q) == rid)
                    if fq < len(Uc): continue           # t > f^Theta_{|U_c| - 1}
                    for z in Uc - T:
                        G_c = Uc - (Q - {c})
                        cand = []
                        kc = kopt_paths(g, Uc, G_c, z, c, c)
                        if kc is not None: cand.append(kc)
                        for q in (Q & Uc) - {c}:
                            Gq = Uc - (T - {q})
                            kq = kopt_paths(g, Uc, Gq, z, q, c)
                            if kq is not None: cand.append(add(kq, kap(g, Xi[q], c)))
                        cnt["TV_chk"] += 1
                        if cand and kap(g, Xi[z], c) != max(cand): fail(cnt, "TV", name, t, z)
    cnt["runs"] += 1


def main(a):
    nr = int(os.environ.get("RANDSTARTS", "0")); cnt = Counter()
    if a and a[0] == "rand":
        N, lo, hi, km, seed = map(int, a[1:6]); rng = random.Random(seed)
        gs = [("rand%d" % i, D.rand_ck(rng, rng.randint(lo, hi), rng.randint(1, km))) for i in range(N)]
    else:
        gs = [(os.path.relpath(f, P.ROOT), RE.parse(f)) for f in (RP.lib() if a == ["lib"] else a)]
    for name, g in gs:
        if g.n > 64: cnt["skip_big"] += 1; continue
        cnt["games"] += 1
        for i, st in enumerate([RE.best_reward_start(g)] + [D.rand_start(g, random.Random(name + str(i))) for i in range(nr)]):
            try: run_check(g, st, cnt, name + ("@r%d" % i if i else ""))
            except RuntimeError: cnt["maxit"] += 1
    for k in sorted(cnt): print("%-26s %d" % (k, cnt[k]))
    print("FAILS", sum(v for k, v in cnt.items() if k.endswith("_FAIL")))
    for e in EX[:40]: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
