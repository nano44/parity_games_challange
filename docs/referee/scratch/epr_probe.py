#!/usr/bin/env python3
"""REFEREE succ. 12 probe for packet P-N5-EPR (docs/new/P-N5-EPR-box45.md, pin a3b1cff3, sha1 8fecca79...). Own engine (rl_engine; N5 via
dual_probe.run5; N5^tau written here from SPEC with S4b^tau). Any game.
Per phase of the N5 run on G, per epoch E = (x..y) (sigma-bar|Q constant), D := {u in Q : sigma-bar_E(u) != tau(u)}, G'_E := Odd v not in D keeps
only tau(v), u in D keeps {tau(u), sigma-bar_E(u)}; len(E) := (y - x) + [y -> y+1 in-phase].
 R1     RESTRICT_E (i): Xi'_k = Xi_k and W'_k = W_k for k in E
 R2     RESTRICT_E (ii): Is'_k = Is_k; S4a's output on G'_E = on G
 R3     RESTRICT_E (iii): It'_k = It_k n E(G'_E)
 R4     RESTRICT_E (iv): k -> k+1 in-phase and It'_k != {} => tau value-optimal against sigma_k in S4b's arena on G'_E
 REP    REPRO: N5^tau on G'_E from (sigma_x, tau) visits (sigma_x, tau), ..., (sigma_{y'}, tau) with the same fallback flags
 EXITLAM (count, the check of REPRO's "ONE phase" claim at y' = y + 1, which lies outside E): lambda' at (sigma_{y+1}, tau) on G'_E != lambda;
        then the transition y -> y+1 leaves the N5^tau phase on G'_E
 EP0    D = {} => len(E) <= n + m
 DIV    (count) SPEC's own S4b on G'_E would move tau at some k in [x, y'-1] (N5 and N5^tau on G'_E differ)
Usage: epr_probe.py lib | rand N nmin nmax kmin kmax seed | files...   (env RANDSTARTS=N, MAXN=64; starts seeded by relative path / fixed seed)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, rho_probe as RP, dual_probe as D
EX = []


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def wval(g, s, t):
    nx = [s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)]
    return [RE.play_value(g, nx, v) for v in range(g.n)]


def s4a(g, s, t, Is):
    A = {v: {s[v]} for v in range(g.n) if g.owner[v] == 0}
    for v, w in Is: A[v].add(w)
    keep = [sorted(A[v]) if g.owner[v] == 0 else [t[v]] for v in range(g.n)]
    _, ch = RE.evaluate(g.restrict(keep).dual(), [t[v] if g.owner[v] == 1 else None for v in range(g.n)])
    return [ch[v] if g.owner[v] == 0 else None for v in range(g.n)]


def s4b_arena(g, s, t, It):
    A = {v: {t[v]} for v in range(g.n) if g.owner[v] == 1}
    for v, w in It: A[v].add(w)
    keep = [sorted(A[v]) if g.owner[v] == 1 else [s[v]] for v in range(g.n)]
    H = g.restrict(keep)
    val, ch = RE.evaluate(H, s)
    tn = [ch[v] if g.owner[v] == 1 else None for v in range(g.n)]
    return H, val, tn


def gates(g, s, t):
    gd = g.dual()
    Xi, sb = RE.evaluate(g, s)
    tt = [t[v] if g.owner[v] == 1 else None for v in range(g.n)]
    Ut, _ = RE.evaluate(gd, tt)
    Is = RE.improving(g, Xi, s, 0)
    It = [(v, w) for v in range(g.n) if g.owner[v] == 1 for w in g.succ[v] if w != t[v] and gd.key(Ut[w]) > gd.key(Ut[t[v]])]
    return Xi, sb, Is, It, Ut


def n5tau_step(g, s, t):
    """one N5^tau iteration (SPEC with S4b^tau); returns (s_new, t_new, fb, div) or None if stopped"""
    Xi, sb, Is, It, Ut = gates(g, s, t)
    if not Is and not It: return None
    sn = s4a(g, s, t, Is) if Is else list(s)
    div = False
    if It:
        H, val, tn = s4b_arena(g, s, t, It)
        wt = wval(H, s, t)
        if wt == val:                  # tau value-optimal in S4b's arena: S4b^tau keeps it
            div = tn != list(t)
            tn = list(t)
    else: tn = list(t)
    fb = False
    if sn == list(s) and tn == list(t):
        fb = True
        if Is:
            for v in range(g.n):
                cand = [w for (x, w) in Is if x == v]
                if cand: sn[v] = max(cand, key=lambda w: (g.key(Xi[w]), w))
        else:
            for v in range(g.n):
                cand = [w for (x, w) in It if x == v]
                if cand: tn[v] = max(cand, key=lambda w: (g.dual().key(Ut[w]), w))
    return sn, tn, fb, div


def run_check(g, start, cnt, name):
    A = D.run5(g, start); n = g.n; m = sum(len(x) for x in g.succ)
    Q = {v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1}
    info = []
    for a in A:
        Xi, sb = RE.evaluate(g, a["s"]); info.append(dict(Xi=Xi, sb=sb, lam=tuple(x[0] for x in Xi)))
    T_ = len(A) - 1
    key = [(info[k]["lam"], tuple(A[k]["t"])) for k in range(T_ + 1)]
    k = 0
    while k <= T_:
        j = k
        while j < T_ and key[j] == key[j + 1]: j += 1
        p0, p1 = k, j; k = j + 1
        cnt["phases"] += 1
        eps, cur = [], [p0]
        for s in range(p0 + 1, p1 + 1):
            if any(info[s]["sb"][q] != info[s - 1]["sb"][q] for q in Q): eps.append(cur); cur = [s]
            else: cur.append(s)
        eps.append(cur)
        for E in eps:
            x, y = E[0], E[-1]; t = list(A[x]["t"])
            inph = y < p1
            L = (y - x) + (1 if inph else 0)
            Dset = {u for u in Q if info[x]["sb"][u] != t[u]}
            succ = [list(g.succ[v]) if g.owner[v] == 0 else ([t[v]] if v not in Dset else sorted({t[v], info[x]["sb"][v]})) for v in range(n)]
            gp = RE.Game(list(g.prio), list(g.owner), succ)
            cnt["epochs"] += 1; cnt["epochs_D%d" % min(len(Dset), 3)] += 1
            cnt["max_len_D%d" % min(len(Dset), 3)] = max(cnt["max_len_D%d" % min(len(Dset), 3)], L)
            if not Dset and L > n + m: fail(cnt, "EP0", name, x, L)
            for kk in E:
                s = A[kk]["s"]
                Xi, sb, Is, It, _ = gates(g, s, t)
                Xp, sbp, Isp, Itp, _ = gates(gp, s, t)
                cnt["R_chk"] += 1
                if Xp != Xi or wval(gp, s, t) != wval(g, s, t): fail(cnt, "R1", name, kk)
                if sorted(Isp) != sorted(Is): fail(cnt, "R2", name, kk)
                elif Is and s4a(gp, s, t, Isp) != s4a(g, s, t, Is): fail(cnt, "R2out", name, kk)
                Eg = {(v, w) for v in range(n) for w in gp.succ[v]}
                if sorted(Itp) != sorted(e for e in It if e in Eg): fail(cnt, "R3", name, kk)
                if kk < p1 and Itp:
                    H, val, _ = s4b_arena(gp, s, t, Itp)
                    cnt["R4_chk"] += 1
                    if wval(H, s, t) != val: fail(cnt, "R4", name, kk)
            # REPRO
            s, tt = list(A[x]["s"]), list(t); ok = True; div = False
            for kk in range(x, x + L):
                r = n5tau_step(gp, s, tt)
                if r is None: ok = False; break
                sn, tn, fb, dv = r; div = div or dv
                if sn != list(A[kk + 1]["s"]) or tn != list(t) or fb != bool(A[kk]["fb"]): ok = False; break
                s, tt = sn, tn
            cnt["REP_chk"] += 1; cnt["DIV"] += div
            if not ok: fail(cnt, "REP", name, x)
            if inph:
                Xy, _ = RE.evaluate(gp, A[y + 1]["s"])
                cnt["EXIT_chk"] += 1
                if tuple(v[0] for v in Xy) != info[y + 1]["lam"]:
                    cnt["EXITLAM"] += 1; cnt["EXITLAM_D%d" % min(len(Dset), 3)] += 1
                    if len(EX) < 40: EX.append(("EXITLAM", name, x, y, len(Dset)))


def main(a):
    nr = int(os.environ.get("RANDSTARTS", "0")); cnt = Counter(); maxn = int(os.environ.get("MAXN", "64"))
    if a and a[0] == "rand":
        N, lo, hi, kl, kh, seed = map(int, a[1:7]); rng = random.Random(seed)
        gs = [("rand%d_%d" % (seed, i), D.rand_ck(rng, rng.randint(lo, hi), rng.randint(kl, kh))) for i in range(N)]
    else:
        gs = [(os.path.relpath(f, P.ROOT), RE.parse(f)) for f in (RP.lib() if a == ["lib"] else a)]
    for name, g in gs:
        if g.n > maxn: cnt["skip_big"] += 1; continue
        cnt["games"] += 1
        for i, st in enumerate([RE.best_reward_start(g)] + [D.rand_start(g, random.Random(name + str(i))) for i in range(nr)]):
            try: run_check(g, st, cnt, name + ("@r%d" % i if i else ""))
            except RuntimeError: cnt["maxit"] += 1
    for k in sorted(cnt): print("%-26s %d" % (k, cnt[k]))
    print("FAILS", sum(v for k, v in cnt.items() if k.endswith("_FAIL")))
    for e in EX[:40]: print("EX (", e)


if __name__ == "__main__":
    main(sys.argv[1:])
