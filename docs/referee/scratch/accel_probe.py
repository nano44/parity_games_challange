#!/usr/bin/env python3
"""REFEREE succ. 12 probe for packet P-N5-ACCEL (docs/new/P-N5-ACCEL-box44.md, pin e7febdc2, sha1 301f0be0...). Own engine (rl_engine via
dual_probe.run5; kappa / kwt from fbred_probe). Any game. Per phase ((lambda_Xi, tau) constant), C, Q, T, U_c as in the packet.
 SG     at every in-phase transition, every switched Even y with lambda(y) != y: kappa_{L+1}(y) > kappa_L(y)  (R19 (d) key step)
 ACA    ACCEL (a): kappa_t(z) in K_c(z) (simple paths of G[U_c] from z to c)                         [n <= PATHN]
 ACB    ACCEL (b): #in-phase transitions switching some Even z with lambda(z) != z <= N_K                [n <= PATHN]
 ACC    ACCEL (c): f <= 1 + N_K                                                                           [n <= PATHN]
 EPA    EPOCH (a): t in E, t > e_j: kappa_t(z) >= best simple path of G_E[U_c] with <= j edges; kappa_t(z) <= opt_E(z)  [n <= PATHN]
 EPB    EPOCH (b): t, t+1 in E, t > e_{n-1}: no switched Even z with lambda(z) != z; frozen part of E has <= 4n(n-1)+1 transitions
 EPC    EPOCH (c): f <= 1 + n * N_ep
 CN_NONSTRICT  count (not a failure): switched Even cycle nodes (lambda(y) = y) whose kappa does not rise (why SG needs lambda(y) != y)
 CTRL   EPA lower bound with j+1 edges: count of states where it fails (shows the bound is not slack everywhere; not a failure)
Usage: accel_probe.py lib | rand N nmin nmax kmax seed | files...   (env RANDSTARTS=N, PATHN=12; starts seeded by relative path / fixed seed)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, rho_probe as RP, dual_probe as D, fbred_probe as F
EX = []
PATHN = int(os.environ.get("PATHN", "12"))


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def paths(g, Uc, c, z, odd_fix=None):
    """list of (edges, kwt-sum excluding c) over simple paths from z to c inside Uc; odd_fix: dict Odd v -> its only successor"""
    out = []
    def dfs(x, seen, acc, ne):
        if x == c: out.append((ne, acc)); return
        succ = [odd_fix[x]] if (odd_fix is not None and g.owner[x] == 1) else g.succ[x]
        for y in succ:
            if y in Uc and y not in seen: dfs(y, seen | {y}, F.add(acc, F.kwt(g, x, c)), ne + 1)
    dfs(z, {z}, (0, 0), 0)
    return out


def run_check(g, start, cnt, name):
    A = D.run5(g, start); n = g.n; small = n <= PATHN
    Q = {v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1}
    info = []
    for a in A:
        Xi, sb = RE.evaluate(g, a["s"])
        info.append(dict(Xi=Xi, sb=sb))
    T_ = len(A) - 1
    key = [(tuple(x[0] for x in info[k]["Xi"]), tuple(A[k]["t"])) for k in range(T_ + 1)]
    k = 0
    while k <= T_:
        j = k
        while j < T_ and key[j] == key[j + 1]: j += 1
        p0, p1 = k, j; k = j + 1
        lam = key[p0][0]; C = set(lam)
        U = {c: {v for v in range(n) if lam[v] == c} for c in C}
        fbs = [x for x in range(p0, p1) if A[x]["fb"]]; f = len(fbs)
        cnt["phases"] += 1; cnt["max_f"] = max(cnt["max_f"], f)
        # SG and switching transitions
        nsw = 0
        for L in range(p0, p1):
            sw = [y for y in range(n) if g.owner[y] == 0 and A[L]["s"][y] != A[L + 1]["s"][y] and lam[y] != y]
            nsw += bool(sw)
            for y in sw:
                cnt["SG_chk"] += 1
                if not F.kap(g, info[L + 1]["Xi"][y], lam[y]) > F.kap(g, info[L]["Xi"][y], lam[y]): fail(cnt, "SG", name, L, y)
        for L in range(p0, p1):
            for y in range(n):
                if g.owner[y] == 0 and A[L]["s"][y] != A[L + 1]["s"][y] and lam[y] == y:
                    cnt["CN_switch"] += 1
                    if not F.kap(g, info[L + 1]["Xi"][y], y) > F.kap(g, info[L]["Xi"][y], y): cnt["CN_NONSTRICT"] += 1
        cnt["max_switch_trans"] = max(cnt["max_switch_trans"], nsw)
        # epochs: sigma-bar|Q constant
        ep = []
        for t in range(p0, p1 + 1):
            sig = tuple(info[t]["sb"][q] for q in sorted(Q))
            if ep and ep[-1][0] == sig: ep[-1][1].append(t)
            else: ep.append((sig, [t]))
        Nep = len(ep); cnt["max_epochs"] = max(cnt["max_epochs"], Nep)
        if f > 1 + n * Nep: fail(cnt, "EPC", name, p0, f, Nep)
        cnt["EPC_chk"] += 1
        for sig, E in ep:
            es = [x for x in fbs if x in E]
            frozen = [t for t in E if len(es) >= n - 1 and t > es[n - 2]] if n >= 2 else []
            if frozen:
                cnt["EPB_hyp"] += 1
                tr = [t for t in frozen if t + 1 in E]
                for t in tr:
                    if any(g.owner[y] == 0 and A[t]["s"][y] != A[t + 1]["s"][y] and lam[y] != y for y in range(n)): fail(cnt, "EPB", name, t)
                if len(tr) + 1 > 4 * n * (n - 1) + 1: fail(cnt, "EPB_len", name, E[0])
        if not small: continue
        # ACCEL (a), N_K
        K = {}
        for c in C:
            for z in U[c]:
                K[z] = {acc for _, acc in paths(g, U[c], c, z)}
        NK = sum(len(K[z]) - 1 for c in C for z in U[c] - {c} if g.owner[z] == 0)
        cnt["ACB_chk"] += 1
        if nsw > NK: fail(cnt, "ACB", name, p0, nsw, NK)
        if f > 1 + NK: fail(cnt, "ACC", name, p0, f, NK)
        for t in range(p0, p1 + 1):
            for c in C:
                for z in U[c]:
                    cnt["ACA_chk"] += 1
                    if F.kap(g, info[t]["Xi"][z], c) not in K[z]: fail(cnt, "ACA", name, t, z)
        # EPOCH (a)
        for sig, E in ep:
            es = [x for x in fbs if x in E]
            fix = {v: info[E[0]]["sb"][v] for v in range(n) if g.owner[v] == 1}
            for c in C:
                PE = {z: paths(g, U[c], c, z, fix) for z in U[c]}
                for t in E:
                    jt = sum(1 for x in es if x < t)
                    for z in U[c]:
                        kz = F.kap(g, info[t]["Xi"][z], c)
                        lo = [acc for ne, acc in PE[z] if ne <= jt]
                        lo1 = [acc for ne, acc in PE[z] if ne <= jt + 1]
                        cnt["EPA_chk"] += 1
                        if lo and kz < max(lo): fail(cnt, "EPA_lo", name, t, z)
                        if PE[z] and kz > max(acc for _, acc in PE[z]): fail(cnt, "EPA_hi", name, t, z)
                        if not PE[z]: fail(cnt, "EPA_nopath", name, t, z)
                        if lo1 and kz < max(lo1): cnt["CTRL_jplus1"] += 1
                        if lo and kz == max(lo): cnt["EPA_tight"] += 1


def main(a):
    nr = int(os.environ.get("RANDSTARTS", "0")); cnt = Counter()
    if a and a[0] == "rand":
        N, lo, hi, km, seed = map(int, a[1:6]); rng = random.Random(seed)
        gs = [("rand%d_%d" % (seed, i), D.rand_ck(rng, rng.randint(lo, hi), rng.randint(0, km))) for i in range(N)]
    else:
        gs = [(os.path.relpath(f, P.ROOT), RE.parse(f)) for f in (RP.lib() if a == ["lib"] else a)]
    for name, g in gs:
        if g.n > 64: cnt["skip_big"] += 1; continue
        cnt["games"] += 1; cnt["games_pathchecked"] += g.n <= PATHN
        for i, st in enumerate([RE.best_reward_start(g)] + [D.rand_start(g, random.Random(name + str(i))) for i in range(nr)]):
            try: run_check(g, st, cnt, name + ("@r%d" % i if i else ""))
            except RuntimeError: cnt["maxit"] += 1
    for k in sorted(cnt): print("%-26s %d" % (k, cnt[k]))
    print("FAILS", sum(v for k, v in cnt.items() if k.endswith("_FAIL")))
    for e in EX[:40]: print("EX (", e)


if __name__ == "__main__":
    main(sys.argv[1:])
