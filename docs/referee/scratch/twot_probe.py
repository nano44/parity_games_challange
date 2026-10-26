#!/usr/bin/env python3
"""REFEREE succ. 12 probe for packet P-N5-2T (docs/si/P-N5-2T-box16.md, pin cbb3b738, sha1 fcb91130...). Own engine (rl_engine via
dual_probe.run5; kappa / kwt from fbred_probe; ARITHMETIC kappa sums). Any game; per phase, per class U_c, Q_c := (Q n U_c) - {c}.
States t compare with fallback SOURCES (g_j = source of the j-th in-phase fallback; f^Theta_j likewise inside a q-run).
 YB     (YB_q): q in Q_c on its own honest cycle => kappa_t(q) in Cyc_c = {(0, s_c l) : 1 <= l <= |U_c| - 1}
 PFZ    PFZ-q: t in q-run Theta, j = #fallbacks with source in Theta and < t; z in (U_c - T) u {q}; every simple path p of G_c^q from z to q with
        <= j edges: kappa_t(z) >= kwt(p - {q}) + kappa_t(q)                                                          [n <= PATHN]
 ROUTE  ROUTE-2: |Q_c| = 2 => at every state some q in Q_c is direct
 DIR    DIR (any |Q_c|): t > g_{|U_c|-1}, q in Q_c direct => kappa_t(q) in A_q                                       [n <= PATHN]
 SAT    SAT-2: Q_c = {q, q'}, t in q-run Theta, t > g_{|U_c|-1}, t > f^Theta_{|U_c|-1} => kappa_t(q') in V_{q'}(kappa_Theta(q))  [n <= PATHN]
 FB2T   Theorem FB-2T: phases with (2T): N_late (distinct (kappa(q))_{q in Q} at late fallback sources) <= 1 + sum_c (N_c - 1)
 MUT    env TWOT_MUT=1: DIR / SAT without Cyc_c, PFZ with j + 1 edges (controls; must bite where the regime occurs)
Usage: twot_probe.py lib | rand N nmin nmax k seed | files...   (env RANDSTARTS=N, PATHN=14; starts seeded by relative path / fixed seed)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, rho_probe as RP, dual_probe as D, fbred_probe as F
EX = []
PATHN = int(os.environ.get("PATHN", "14"))
MUT = os.environ.get("TWOT_MUT", "") == "1"


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def spaths(g, nodes, sink, z, c):
    """(edges, kwt_c-sum excluding sink) over simple paths from z to sink in the graph on `nodes` (sink kept; Even: edges inside;
    Odd non-sink: only if forced, its edge if inside)"""
    out = []
    def dfs(x, seen, acc, ne):
        if x == sink: out.append((ne, acc)); return
        if g.owner[x] == 1 and len(g.succ[x]) > 1: return
        for y in g.succ[x]:
            if y in nodes and y not in seen: dfs(y, seen | {y}, F.add(acc, F.kwt(g, x, c)), ne + 1)
    if z in nodes: dfs(z, {z}, (0, 0), 0)
    return out


def best(lst):
    return max(a for _, a in lst) if lst else None


def run_check(g, start, cnt, name):
    A = D.run5(g, start); n = g.n; small = n <= PATHN
    Q = {v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1}
    info = []
    for a in A:
        Xi, sb = RE.evaluate(g, a["s"])
        info.append(dict(Xi=Xi, hg=[a["s"][v] if g.owner[v] == 0 else sb[v] for v in range(n)]))
    T_ = len(A) - 1
    key = [(tuple(x[0] for x in info[k]["Xi"]), tuple(A[k]["t"])) for k in range(T_ + 1)]
    k = 0
    while k <= T_:
        j = k
        while j < T_ and key[j] == key[j + 1]: j += 1
        p0, p1 = k, j; k = j + 1
        lam = key[p0][0]; C = set(lam); T = C | Q
        U = {c: {v for v in range(n) if lam[v] == c} for c in C}
        fbs = [x for x in range(p0, p1) if A[x]["fb"]]; f = len(fbs)
        cnt["phases"] += 1
        Qc = {c: (Q & U[c]) - {c} for c in C}
        twoT = all(len(Qc[c]) <= 2 for c in C)
        cnt["phases_2T"] += twoT
        def kap(t, z): return F.kap(g, info[t]["Xi"][z], lam[z])
        def play(t, v):
            seq, seen = [], set()
            while v not in seen: seen.add(v); seq.append(v); v = info[t]["hg"][v]
            return seq, v  # v = first repeated vertex
        def on_cycle(t, q):
            seq, r = play(t, q); return r == q
        def direct(t, q, c):
            if on_cycle(t, q): return True
            for v in play(t, q)[0][1:]:
                if v == c: return True
                if v in Qc[c]: return False
            return False
        def gsrc(i):  # source of the i-th fallback (1-based); None if fewer
            return fbs[i - 1] if 1 <= i <= f else None
        def after_g(t, i):
            if i <= 0: return True
            s = gsrc(i); return s is not None and t > s
        # precompute value sets (small)
        if small:
            Gc = {c: U[c] - (Q - {c}) for c in C}
            kopt_c = {c: {z: best(spaths(g, Gc[c], c, z, c)) for z in U[c]} for c in C}
            kopt_q, PQ = {}, {}
            for c in C:
                for q in Qc[c]:
                    nodes = U[c] - (T - {q})
                    PQ[q] = {z: spaths(g, nodes, q, z, c) for z in U[c]}
                    kopt_q[q] = {z: best(PQ[q][z]) for z in U[c]}
        for c in C:
            w = len(U[c]) - 1; sc = 1 if g.prio[c] % 2 else -1
            Cyc = set() if MUT else {(0, sc * l) for l in range(1, w + 1)}
            for q in Qc[c]:
                # q-runs
                runs, cur = [], []
                for t in range(p0, p1 + 1):
                    if cur and info[t]["Xi"][q] != info[cur[-1]]["Xi"][q]: runs.append(cur); cur = []
                    cur.append(t)
                runs.append(cur)
                for t in range(p0, p1 + 1):
                    if on_cycle(t, q):
                        cnt["YB_chk"] += 1
                        if kap(t, q) not in {(0, sc * l) for l in range(1, w + 1)}: fail(cnt, "YB", name, t, q)
                if small:
                    Aq = {F.add(F.kwt(g, q, c), kopt_c[c][y]) for y in g.succ[q] if y in U[c] and y not in Q and kopt_c[c][y] is not None}
                    if c in g.succ[q]: Aq.add(F.kwt(g, q, c))
                    Aq |= Cyc
                    for Th in runs:
                        fTh = [x for x in fbs if x in Th]
                        for t in Th:
                            jt = sum(1 for x in fTh if x < t) + (1 if MUT else 0)
                            for z in (U[c] - T) | {q}:
                                for ne, acc in PQ[q][z]:
                                    if ne <= jt:
                                        cnt["PFZ_chk"] += 1
                                        if kap(t, z) < F.add(acc, kap(t, q)): fail(cnt, "PFZ", name, t, q, z, ne)
                    for t in range(p0, p1 + 1):
                        if after_g(t, w) and direct(t, q, c):
                            cnt["DIR_chk"] += 1
                            if kap(t, q) not in Aq: fail(cnt, "DIR", name, t, q)
            if len(Qc[c]) == 2:
                q1, q2 = sorted(Qc[c])
                for t in range(p0, p1 + 1):
                    cnt["ROUTE_chk"] += 1
                    if not (direct(t, q1, c) or direct(t, q2, c)): fail(cnt, "ROUTE", name, t)
                if small:
                    for q, qq in ((q1, q2), (q2, q1)):
                        runs, cur = [], []
                        for t in range(p0, p1 + 1):
                            if cur and info[t]["Xi"][q] != info[cur[-1]]["Xi"][q]: runs.append(cur); cur = []
                            cur.append(t)
                        runs.append(cur)
                        for Th in runs:
                            fTh = [x for x in fbs if x in Th]
                            al = kap(Th[0], q)
                            V = set(Cyc)
                            for y in g.succ[qq]:
                                if y not in U[c] or y == qq: continue
                                if y == q: b = al
                                elif y == c: b = (0, 0)
                                else:
                                    cand = [x for x in (kopt_c[c][y], None if kopt_q[q][y] is None else F.add(kopt_q[q][y], al)) if x is not None]
                                    b = max(cand) if cand else None
                                if b is not None: V.add(F.add(F.kwt(g, qq, c), b))
                            for t in Th:
                                if after_g(t, w) and (w <= 0 or (len(fTh) >= w and t > fTh[w - 1])):
                                    cnt["SAT_chk"] += 1
                                    if kap(t, qq) not in V: fail(cnt, "SAT", name, t, q, qq)
        # FB-2T
        if twoT and small:
            late = [x for jj, x in enumerate(fbs, 1) if jj >= n]
            if late:
                cnt["FB2T_chk"] += 1
                Nl = len({tuple(info[x]["Xi"][q] for q in sorted(Q)) for x in late})
                bound = 1
                for c in C:
                    if not Qc[c]: continue
                    w = len(U[c]) - 1; ds = [len([y for y in g.succ[q] if y in U[c]]) for q in Qc[c]]; d = max(ds)
                    Nc = (d + w) if len(Qc[c]) == 1 else 2 * (d + w) * (d + 2 * w)
                    bound += Nc - 1
                if Nl > bound: fail(cnt, "FB2T", name, p0, Nl, bound)


def main(a):
    nr = int(os.environ.get("RANDSTARTS", "0")); cnt = Counter()
    if a and a[0] == "rand":
        N, lo, hi, kk, seed = map(int, a[1:6]); rng = random.Random(seed)
        gs = [("rand%d_%d" % (seed, i), D.rand_ck(rng, rng.randint(lo, hi), kk)) for i in range(N)]
    elif a and a[0] == "list":
        gs = [(l.split()[0], RE.parse(os.path.join(P.ROOT, l.split()[0]))) for l in open(a[1]) if l.strip()]
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
    for e in EX[:40]: print("EX (", e)


if __name__ == "__main__":
    main(sys.argv[1:])
