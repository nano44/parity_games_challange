#!/usr/bin/env python3
"""REFEREE successor 21: own control for packet P-N5-ODD (L-SI box 57, l-si 0afc0d70a, sha1 03eec41d). Own engine rl_engine; no lane code.
Checks, at every transition k -> k+1 of an N5 run (Xi_k, sbar_k from S1; values (c, mask, d)):
  OLD   Xi_(k+1)(x) != Xi_k(x)  =>  some Even vertex of x's (s_k, sbar_k)-play switches at k            (Lemma OLD-PLAY)
  STEP  Odd o, x := sbar_k(o): Xi_(k+1)(x) = Xi_k(x) => Xi_(k+1)(o) = Xi_k(o); CII counts o on x's new play (Lemma ODD-STEP / NO-RET)
Inside W-runs F (RESULTS R89; tau, C fixed; D_k = {Odd o : sbar_k(o) != tau(o)}):
  ROOT  Corollary SRC-ROOT: from every Odd o0 with a Xi change, follow u_k(.) while o_j is Odd with no prefix event; every o_j changes,
        the chain never repeats, and it ends (a) at an Odd o_t with a prefix event or (b) at an Even o_t in C
  LEX   Lemma FUEL-LEX on consecutive fuel re-routes of each pair (y, z); CNT Corollary FUEL-COUNT N <= n(n+2)(HC+n)
MUT 1: OLD reads only the play's prefix before its cycle (must bite). MUT 2: LEX without the EQHI clause (must bite where EQHI occurs).
FSONLY=1: fuel re-routes only for y on FS_k(o), o in D_k u D_(k+1) (the lane's box-56 selector, to reconcile with srcfuel.py).
MUT 3: ROOT without the Odd sigma-bar prefix event (only Even switches count; bites iff Odd choice changes are needed).
Usage: odd_probe.py FILES... | rand N lo hi seed     (env MUT, MAXN; a FILE.start next to FILE.pg is used, else best-reward start)"""
import sys, os, random
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE
MUT = int(os.environ.get("MUT", "0"))
EX = []


def fail(cnt, tag, *a):
    cnt[tag + "_V"] += 1
    if len(EX) < 30: EX.append((tag,) + a)


def nxs(g, s, t): return [s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)]


def playlist(nx, x):
    pre, cyc = RE.lasso(nx, x)
    return pre + cyc, pre


def key(g, a, b):
    if a[0] != b[0]: return (2, 0)
    if a[1] != b[1]: return (1, (a[1] ^ b[1]).bit_length() - 1)
    return (0, 0)


def analyse(cnt, g, start, name):
    st = RE.run(g, start); n = g.n; T = len(st) - 1
    Ev = [v for v in range(n) if g.owner[v] == 0]; Od = [v for v in range(n) if g.owner[v] == 1]
    Xi = [s["Xi"] for s in st]
    for k in range(T):
        s0, s1, b0, b1 = st[k]["s"], st[k + 1]["s"], st[k]["sb"], st[k + 1]["sb"]
        sw = {y for y in Ev if s0[y] != s1[y]}
        nx0 = nxs(g, s0, b0); nx1 = nxs(g, s1, b1)
        for x in range(n):
            if Xi[k + 1][x] != Xi[k][x]:
                cnt["OLD_chk"] += 1
                pl, pre = playlist(nx0, x)
                if not any(y in sw for y in (pre if MUT == 1 else pl)): fail(cnt, "OLD", name, k, x)
        for o in Od:
            x = b0[o]
            cnt["STEP_chk"] += 1
            if o in playlist(nx1, x)[0]: cnt["STEP_caseII"] += 1
            if Xi[k + 1][x] == Xi[k][x] and Xi[k + 1][o] != Xi[k][o]: fail(cnt, "STEP", name, k, o)
    # W-runs
    W = [[RE.play_value(g, nxs(g, s["s"], s["t"]), v) for v in range(n)] for s in st]
    runs, a = [], 0
    for k in range(T):
        if st[k]["t"] != st[k + 1]["t"] or st[k]["fb"] or [x[0] for x in W[k]] != [x[0] for x in W[k + 1]]: runs.append((a, k)); a = k + 1
    runs.append((a, T))
    for (a, b) in runs:
        if b == a: continue
        cnt["wruns"] += 1; cnt["trans"] += b - a
        tau = st[a]["t"]; C = {v for v in range(n) if W[a][v][0] == v}
        for k in range(a, b):
            s0, s1, b0, b1 = st[k]["s"], st[k + 1]["s"], st[k]["sb"], st[k + 1]["sb"]
            Dk = {o for o in Od if b0[o] != tau[o]}
            sw = {y for y in Ev if s0[y] != s1[y]}; obc = {z for z in Od if b0[z] != b1[z]}
            nx0 = nxs(g, s0, b0)

            def useg(o):
                fs = []; v = b0[o]; seen = set()
                while v not in Dk and v not in C:
                    if v in seen: return None, fs
                    seen.add(v); fs.append(v); v = nx0[v]
                return v, fs
            for o0 in Od:
                if Xi[k + 1][o0] == Xi[k][o0]: continue
                cnt["ROOT_chk"] += 1
                o, seen, pl0 = o0, [], set(playlist(nx0, o0)[0])
                while True:
                    if o in seen: fail(cnt, "ROOTREP", name, k, o0); break
                    seen.append(o)
                    if Xi[k + 1][o] == Xi[k][o]: fail(cnt, "ROOTCH", name, k, o0, o); break
                    if o not in pl0: fail(cnt, "ROOTPL", name, k, o0, o); break
                    if g.owner[o] == 0:
                        if o in C: cnt["ROOT_endC"] += 1
                        else: fail(cnt, "ROOTEND", name, k, o0, o)
                        break
                    u, fs = useg(o)
                    if u is None: fail(cnt, "ROOTU", name, k, o); break
                    pe = any(v in sw for v in fs) or (MUT != 3 and any(v in obc for v in fs))
                    if pe:
                        cnt["ROOT_endPE"] += 1
                        if not any(v in sw for v in fs): cnt["ROOT_endPE_oddonly"] += 1
                        break
                    o = u
                cnt["ROOT_maxlen"] = max(cnt["ROOT_maxlen"], len(seen))
        # fuel re-routes
        fr = defaultdict(list)
        for k in range(a + 1, b):
            sp, s0, s1 = st[k - 1]["s"], st[k]["s"], st[k + 1]["s"]
            Isp = set(st[k - 1]["Is"])
            if os.environ.get("FSONLY"):
                tau_ = st[k]["t"]; b0 = st[k]["sb"]; nx0 = nxs(g, s0, b0)
                Dk = {o for o in Od if b0[o] != tau_[o]}; Dk1 = {o for o in Od if st[k + 1]["sb"][o] != tau_[o]}
                FSV = set()
                for o in Dk | Dk1:
                    v, seen = b0[o], set()
                    while v not in Dk and v not in C and v not in seen: seen.add(v); FSV.add(v); v = nx0[v]
            for y in Ev:
                if os.environ.get("FSONLY") and y not in FSV: continue
                z = s1[y]
                if z != s0[y] and z != sp[y] and (y, z) not in Isp and Xi[k - 1][z] != Xi[k][z]:
                    fr[(y, z)].append((k, key(g, Xi[k - 1][z], Xi[k][z])))
        for (y, z), L in fr.items():
            cnt["FR"] += len(L)
            for (k, ka), (k2, kb) in zip(L, L[1:]):
                if kb < ka: continue
                t, t2 = k - 1, k2 - 1
                if kb > ka: cnt["ASC"] += 1; continue
                hi = [u for u in range(t + 1, t2) if Xi[u][z] != Xi[u + 1][z] and key(g, Xi[u][z], Xi[u + 1][z]) > ka]
                if hi and MUT != 2: cnt["EQHI"] += 1; continue
                if ka in ((2, 0), (0, 0)): cnt["REP"] += 1; continue
                fail(cnt, "LEX", name, (y, z), k, k2, ka)
            # FUEL-COUNT
            HC = 0
            for u in range(a, b):
                if Xi[u][z] == Xi[u + 1][z]: continue
                last = [kk for kk, _ in L if kk <= u]
                if last and key(g, Xi[u][z], Xi[u + 1][z]) > dict(L)[last[-1]]: HC += 1
            cnt["CNT_chk"] += 1
            if len(L) > n * (n + 2) * (HC + n): fail(cnt, "CNT", name, (y, z))
            cnt["FR_maxpair"] = max(cnt["FR_maxpair"], len(L))


def main(a):
    import core_probe as CP
    cnt = Counter()
    def do(g, name, extra=None):
        try: analyse(cnt, g, extra, name)
        except RuntimeError: cnt["maxit"] += 1
    if a and a[0] == "rand":
        import dual_probe as D
        N, lo, hi, seed = map(int, a[1:5]); r2 = random.Random(seed)
        for i in range(N):
            nn = r2.randint(lo, hi)
            cnt["GAMES"] += 1; do(D.rand_ck(r2, nn, r2.randint(0, min(5, nn - 1))), "rand%d" % i)
    else:
        for p in a:
            if p.endswith(".start"): continue
            try: g = RE.parse(p)
            except Exception: cnt["parse_err"] += 1; continue
            if g.n > int(os.environ.get("MAXN", "100")): cnt["skip_big"] += 1; continue
            sp = p[:-3] + ".start"; ex = None
            if os.path.exists(sp):
                try: ex = CP.parse_start(g, sp)
                except Exception: cnt["start_err"] += 1
            cnt["GAMES"] += 1; do(g, os.path.basename(p), ex)
    for k in sorted(cnt): print(k, cnt[k])
    print("VIOLATIONS", sum(v for k, v in cnt.items() if k.endswith("_V")))
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
