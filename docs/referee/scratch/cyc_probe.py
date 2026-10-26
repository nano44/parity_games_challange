#!/usr/bin/env python3
"""REFEREE succ. 8: checks for the P-N5-RL fixes file (sha1 ac027458) Lemma CYC-EV's ingredients (docs/si/N5-TEV-box11.md §1-§2, sha1
58a0b3cf): in setting (Sigma) = consecutive fallbacks k0 < k of a scope run, L = M_{k0} >= 0, r > L on [k0+1, k]:
 FZ   v in F_k => v in F_s on [k0+1, k] and COARSE_L(Xi_k v) = COARSE_L(Xi_{k0} v)
 BF   Even v in R_{k0} & F_k: COARSE_L(b_k v) = COARSE_L(Xi_{k0} sigma_{k0} v), cycle node c
 RB   ... and a = sigma_{k0}(v) in Rbar_k: COARSE_L(Xi_k a) = COARSE_L(Xi_{k0} a)
 WALK from every v0 in R_{k0} & F_k: the last free vertex is Even, and (pi^k_aj & H) + B = (pi^k0_aj & H) + A
 S4   M_k <= L;   CYC  no Ev vertex on c's sigma_k-cycle (all (Sigma) pairs, rise or not)
Own engine (rl_engine / rl_probe). Usage: cyc_probe.py lib|named|files..."""
import sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P


def run(g, cnt, name):
    o, st = P.states(g); P.OO[0] = o; inph, runs = P.scope_runs(st)
    def Hset(L, c): return {v for v in range(g.n) if g.rank[v] > max(L, g.rank[c])}
    def hp(x, Hs): return {v for v in Hs if x[1] >> g.rank[v] & 1}
    for S in runs:
        fbs = [k for k in S if st[k]["fb"]]
        for k0, k in zip(fbs, fbs[1:]):
            L = st[k0]["M"]
            if L < 0 or not all(st[s]["r"] > L and st[s]["r"] < P.INF for s in range(k0 + 1, k + 1)): continue
            cnt["pairs"] += 1; a0, ak = st[k0], st[k]; c = a0["Xi"][o][0]; Hs = Hset(L, c)
            if ak["M"] > L: cnt["S4_FAIL"] += 1
            A, B = hp(a0["Xi"][o], Hs), hp(ak["Xi"][o], Hs)
            cnt["rise"] += A != B
            for v in ak["F"]:
                cnt["FZ_chk"] += 1
                if any(v not in st[s]["F"] for s in range(k0 + 1, k + 1)) or P.coarse(ak["Xi"][v], L) != P.coarse(a0["Xi"][v], L):
                    cnt["FZ_FAIL"] += 1; P.EX.append((name, "FZ", k0, k, v))
            RF = [v for v in ak["F"] if v in a0["Rb"] and v != o]
            Ev = st[k0 + 1]["F"] - a0["F"]
            if set(RE.lasso(ak["nx"], c)[1]) & Ev: cnt["CYC_FAIL"] += 1; P.EX.append((name, "CYC", k0, k))
            for v in RF:
                if g.owner[v] == 0:
                    a = a0["s"][v]; cnt["BF_chk"] += 1
                    bk = ak["Xi"][ak["s"][v]]
                    if P.coarse(bk, L) != P.coarse(a0["Xi"][a], L) or bk[0] != c: cnt["BF_FAIL"] += 1; P.EX.append((name, "BF", k0, k, v))
                    if a in ak["Rb"]:
                        cnt["RB_chk"] += 1
                        if P.coarse(ak["Xi"][a], L) != P.coarse(a0["Xi"][a], L): cnt["RB_FAIL"] += 1; P.EX.append((name, "RB", k0, k, v))
                route = [v] + P.route(a0["nx"], a0["nx"][v], o) if v != o else []
                seq = route + [o]
                j = next(i for i in range(1, len(seq)) if seq[i] in ak["Rb"])
                w, aj = seq[j - 1], seq[j]; cnt["WALK_chk"] += 1
                if g.owner[w] != 0: cnt["WALK_a_FAIL"] += 1
                pk = set(P.route(ak["nx"], aj, o)) if aj != o else set()
                p0 = set(P.route(a0["nx"], aj, o)) if aj != o else set()
                if (pk & Hs) | B != (p0 & Hs) | A or (pk & Hs) & B or (p0 & Hs) & A: cnt["WALK_b_FAIL"] += 1; P.EX.append((name, "WALKb", k0, k, v))


cnt = Counter()
a = sys.argv[1:]
files = P.lib() if a == ["lib"] else P.named() if a == ["named"] else a
for f in files:
    g = RE.parse(f)
    try: P.assert_c1o(g)
    except AssertionError: cnt["skip_not_c1o"] += 1; continue
    if g.n > 64: continue
    cnt["games"] += 1; run(g, cnt, os.path.relpath(f, P.ROOT))
for k in sorted(cnt): print("%-14s %d" % (k, cnt[k]))
print("FAILS", sum(v for k, v in cnt.items() if k.endswith("_FAIL")))
for e in P.EX[:10]: print("EX", e)
