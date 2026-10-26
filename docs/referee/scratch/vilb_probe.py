#!/usr/bin/env python3
"""REFEREE succ. 12 probe for packet P-N5-VILB (docs/new/P-N5-VILB-box44.md, pin e7febdc2, sha1 872d4400...). Own engine (rl_engine via
dual_probe.run5; kappa / kwt from fbred_probe). Any game.
Per phase ((lambda_Xi, tau) constant), per cycle node c, U_c = lambda^{-1}(c):
 AK      (A kappa): kappa_t(z) = kwt_c(z) + kappa_t(next_t z), next_t z in U_c, z in U_c - {c}
 M2      (M2 kappa): kappa_t(z) <= kappa_{t+1}(z) at in-phase transitions
 FBR     kappa-FB-ROUND at every in-phase fallback (every Even v in U_c - {c}, successor x in U_c)
 VILB    Lemma VI-LB: kappa_t(z) >= Val^{<=j}_c(z) for every state t of the phase with t > g_j, j = #in-phase fallbacks before t
 CTRL    count (not a failure): states where kappa_t(z) >= Val^{<=j+1}_c(z) fails
 MUT     env VILB_MUT=oddmax: every Odd vertex maximises in Val (must bite: VILB failures expected)
Val^{<=j}: Val(c) = (0,0); others -inf at j = 0; Even z: kwt + max over succ in U_c; Odd z (every Odd vertex): kwt + min. -inf = None.
Usage: vilb_probe.py lib | rand N nmin nmax kmax seed | files...   (env RANDSTARTS=N; starts seeded by relative path / fixed seed)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, rho_probe as RP, dual_probe as D, fbred_probe as F
EX = []
MUT = os.environ.get("VILB_MUT", "")


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def vi(g, Uc, c, J):
    """[Val^{<=0}, ..., Val^{<=J}] as dicts z -> pair or None (-inf)"""
    cur = {z: None for z in Uc}; cur[c] = (0, 0); out = [cur]
    for _ in range(J):
        nxt = {c: (0, 0)}
        for z in Uc:
            if z == c: continue
            vals = [cur[x] for x in g.succ[z] if x in Uc]
            if g.owner[z] == 0 or MUT == "oddmax":
                fin = [v for v in vals if v is not None]
                best = max(fin) if fin else None
            else:
                best = None if (not vals or any(v is None for v in vals)) else min(vals)
            nxt[z] = None if best is None else F.add(F.kwt(g, z, c), best)
        out.append(nxt); cur = nxt
    return out


def ge(a, b):  # a >= b with None = -inf
    return b is None or (a is not None and a >= b)


def run_check(g, start, cnt, name):
    A = D.run5(g, start); n = g.n
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
        lam = key[p0][0]; C = set(lam)
        U = {c: {v for v in range(n) if lam[v] == c} for c in C}
        fbs = [x for x in range(p0, p1) if A[x]["fb"]]
        cnt["phases"] += 1; cnt["max_f"] = max(cnt["max_f"], len(fbs))
        VI = {c: vi(g, U[c], c, len(fbs) + 1) for c in C}
        for t in range(p0, p1 + 1):
            Xi = info[t]["Xi"]; hg = info[t]["hg"]
            jt = sum(1 for x in fbs if x < t)
            for c in C:
                for z in U[c]:
                    kz = F.kap(g, Xi[z], c)
                    if z != c:
                        nz = hg[z]
                        if nz not in U[c] or kz != F.add(F.kwt(g, z, c), F.kap(g, Xi[nz], c)): fail(cnt, "AK", name, t, z)
                    if t < p1 and kz > F.kap(g, info[t + 1]["Xi"][z], c): fail(cnt, "M2", name, t, z)
                    cnt["VILB_chk"] += 1
                    if not ge(kz, VI[c][jt][z]): fail(cnt, "VILB", name, t, z, jt)
                    if VI[c][jt][z] is not None: cnt["VILB_finite"] += 1
                    if kz == VI[c][jt][z]: cnt["VILB_tight"] += 1
                    if not ge(kz, VI[c][jt + 1][z]): cnt["CTRL_jplus1_bites"] += 1
        for x in fbs:
            Xi0, Xi1 = info[x]["Xi"], info[x + 1]["Xi"]
            for c in C:
                for v in U[c] - {c}:
                    if g.owner[v] != 0: continue
                    for xx in g.succ[v]:
                        if xx not in U[c]: continue
                        cnt["FBR_chk"] += 1
                        if F.kap(g, Xi1[v], c) < F.add(F.kwt(g, v, c), F.kap(g, Xi0[xx], c)): fail(cnt, "FBR", name, x, v, xx)


def main(a):
    nr = int(os.environ.get("RANDSTARTS", "0")); cnt = Counter()
    if a and a[0] == "rand":
        N, lo, hi, km, seed = map(int, a[1:6]); rng = random.Random(seed)
        gs = [("rand%d_%d" % (seed, i), D.rand_ck(rng, rng.randint(lo, hi), rng.randint(0, km))) for i in range(N)]
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
