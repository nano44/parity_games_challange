#!/usr/bin/env python3
"""REFEREE succ. 11 probe for packet P-N5-GD (docs/new/P-N5-GD-box43.md, pin 3c6f6c16, sha1 b898ff82...). Own engine (rl_engine,
dual_probe.run5 = rl_engine.run with a start pair; no lane code). Every game, any number of Odd choice vertices.
Per state k: D_k = {Odd u : sigmabar(u) != tau(u)}, u(v) = first D vertex on v's (sigma, tau)-play, R_D, F_D, pi_v.
 GA     v in F_D: Xi(v) = W(v)
 GB     (h_D): Xi(v) = pi_v (+) Xi(u), W(v) = pi_v (+) W(u), u's honest and W-plays avoid pi_v
 GC1    (h_D), (h3_D): same terminal u => the orders of pi_y (+) Xi(u) vs pi_z (+) Xi(u) and with W(u) agree
 GC2    (h_D), (h3_D): COARSE_L(Xi(v)) = COARSE_L(W(v)) for every v and every L in {M_D, ..., n-1}
 F1D    per phase, per maximal run with (D, R_D) constant: transitions with a Xi-change on F_D <= max(0, |F_D| - 1)
 WOD    tau(u) same, u in D_k and D_{k+1}, (h_D) at k and k+1: W_{k+1}(u) >= W_k(u)
Usage: gd_probe.py lib | rand N nmin nmax kmax seed   (env RANDSTARTS=N)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, rho_probe as RP, dual_probe as D
EX = []
INF, BOT = 10 ** 6, -2


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def lev(x, y):
    if x == y: return BOT
    if x[0] != y[0]: return INF
    d = x[1] ^ y[1]
    return d.bit_length() - 1 if d else -1


def coarse(x, L):
    if L <= BOT: return x
    return (x[0], x[1] & ~((1 << (L + 1)) - 1)) if L >= 0 else (x[0], x[1])


def play(nx, v):
    seq, pos, x = [], {}, v
    while x not in pos: pos[x] = len(seq); seq.append(x); x = nx[x]
    return seq


def state_info(g, s, t):
    n = g.n
    Xi, sb = RE.evaluate(g, s)
    nx = [s[v] if g.owner[v] == 0 else t[v] for v in range(n)]
    hg = [s[v] if g.owner[v] == 0 else sb[v] for v in range(n)]
    W = [RE.play_value(g, nx, v) for v in range(n)]
    Dk = frozenset(v for v in range(n) if g.owner[v] == 1 and sb[v] != t[v])
    uo, pi = {}, {}
    for v in range(n):
        p = play(nx, v); path = []
        for x in p:
            if x in Dk: uo[v] = x; pi[v] = path; break
            path.append(x)
    hD = True
    for u in Dk:
        for nn in (hg, nx):
            seq = play(nn, u)
            # after leaving u: the play's vertices after index 0, and the return to the cycle
            rest = seq[1:]
            back = nn[seq[-1]]
            if any(x in Dk for x in rest) or back in Dk: hD = False
    h3 = all(Xi[u][0] == W[u][0] for u in Dk)
    return dict(Xi=Xi, sb=sb, nx=nx, hg=hg, W=W, D=Dk, u=uo, pi=pi, RD=frozenset(uo), hD=hD, h3=h3)


def check_run(g, start, cnt, name):
    A = D.run5(g, start)
    n = g.n
    S = [state_info(g, a["s"], a["t"]) for a in A]
    for k, si in enumerate(S):
        Xi, W = si["Xi"], si["W"]
        for v in range(n):
            if v not in si["RD"]:
                cnt["GA_chk"] += 1
                if Xi[v] != W[v]: fail(cnt, "GA", name, k, v)
        if si["D"]: cnt["states_D_nonempty"] += 1
        if not si["hD"]: continue
        cnt["states_hD"] += 1
        for v in si["RD"]:
            u = si["u"][v]; pv = si["pi"][v]
            cnt["GB_chk"] += 1
            if Xi[v] != P.extp(g, pv, Xi[u]) or W[v] != P.extp(g, pv, W[u]): fail(cnt, "GB", name, k, v)
            for nn in (si["hg"], si["nx"]):
                if set(play(nn, u)[1:]) & set(pv): fail(cnt, "GB_avoid", name, k, v)
        if not si["h3"] or not si["D"]: continue
        cnt["states_hD_h3"] += 1
        RD = sorted(si["RD"])
        for i, y in enumerate(RD):
            for z in RD[i + 1:]:
                if si["u"][y] != si["u"][z]: continue
                u = si["u"][y]
                a1 = g.key(P.extp(g, si["pi"][y], Xi[u])) <= g.key(P.extp(g, si["pi"][z], Xi[u]))
                a2 = g.key(P.extp(g, si["pi"][y], W[u])) <= g.key(P.extp(g, si["pi"][z], W[u]))
                cnt["GC1_chk"] += 1
                if a1 != a2: fail(cnt, "GC1", name, k, y, z)
        MD = max(lev(Xi[u], W[u]) for u in si["D"])
        for L in range(max(MD, -1), n):
            for v in range(n):
                cnt["GC2_chk"] += 1
                if coarse(Xi[v], L) != coarse(W[v], L): fail(cnt, "GC2", name, k, v, L, MD)
        if MD == BOT:
            for v in range(n):
                if Xi[v] != W[v]: fail(cnt, "GC2_bot", name, k, v)
    # phases and F1_D
    T = len(A) - 1
    key = [(tuple(x[0] for x in S[k]["Xi"]), tuple(A[k]["t"])) for k in range(T + 1)]
    k = 0
    while k <= T:
        j = k
        while j < T and key[j] == key[j + 1]: j += 1
        x = k
        while x <= j:
            y = x
            while y < j and S[y + 1]["D"] == S[x]["D"] and S[y + 1]["RD"] == S[x]["RD"]: y += 1
            FD = set(range(n)) - S[x]["RD"]
            ch = sum(any(S[z]["Xi"][v] != S[z + 1]["Xi"][v] for v in FD) for z in range(x, y))
            cnt["F1D_chk"] += 1; cnt["F1D_trs"] += y - x
            if ch > max(0, len(FD) - 1): fail(cnt, "F1D", name, x, ch, len(FD))
            x = y + 1
        k = j + 1
    for k in range(T):
        if A[k]["t"] != A[k + 1]["t"]: continue
        if not (S[k]["hD"] and S[k + 1]["hD"]): continue
        for u in S[k]["D"] & S[k + 1]["D"]:
            cnt["WOD_chk"] += 1
            if g.key(S[k + 1]["W"][u]) < g.key(S[k]["W"][u]): fail(cnt, "WOD", name, k, u)
    cnt["runs"] += 1


def main(a):
    nr = int(os.environ.get("RANDSTARTS", "0")); cnt = Counter()
    if a and a[0] == "rand":
        N, lo, hi, km, seed = map(int, a[1:6]); rng = random.Random(seed)
        gs = [("rand%d" % i, D.rand_ck(rng, rng.randint(lo, hi), rng.randint(2, km))) for i in range(N)]
    else:
        gs = [(os.path.relpath(f, P.ROOT), RE.parse(f)) for f in (RP.lib() if a == ["lib"] else a)]
    for name, g in gs:
        if g.n > 64: cnt["skip_big"] += 1; continue
        cnt["games"] += 1
        for i, st in enumerate([RE.best_reward_start(g)] + [D.rand_start(g, random.Random(name + str(i))) for i in range(nr)]):
            try: check_run(g, st, cnt, name + ("@r%d" % i if i else ""))
            except RuntimeError: cnt["maxit"] += 1
    for k in sorted(cnt): print("%-28s %d" % (k, cnt[k]))
    print("FAILS", sum(v for k, v in cnt.items() if k.endswith("_FAIL")))
    for e in EX[:40]: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
