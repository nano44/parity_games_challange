#!/usr/bin/env python3
"""REFEREE s20: FLAT-SW strong form (no DEPTH hypothesis). At every transition k -> k+1 with tau_{k+1} = tau_k and Xi_{k+1} != Xi_k,
some Even x with sigma_{k+1}(x) != sigma_k(x) has Xi_{k+1}(x) != Xi_k(x).  Also classifies switched x that keep Xi(x):
own cycle node at k / k+1, on the cycle (not node), off-cycle (should be 0 by the x (+) injectivity argument).
Usage: fsw_strong.py [--lzc] FILES... | rand N lo hi seed"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, wch_probe as WP
LZ = "--lzc" in sys.argv
cnt = Counter(); EX = []
def oncyc(g, s, sb, x):
    nx = [s[v] if g.owner[v] == 0 else sb[v] for v in range(g.n)]
    pre, cyc = RE.lasso(nx, x); return x in cyc
def analyse(g, start, name):
    st = (WP.run_lzc if LZ else RE.run)(g, start)
    for k in range(len(st) - 1):
        A, B = st[k], st[k + 1]
        if A["t"] != B["t"]: continue
        sw = [x for x in range(g.n) if g.owner[x] == 0 and A["s"][x] != B["s"][x]]
        cnt["trans"] += 1
        for x in sw:
            if A["Xi"][x] == B["Xi"][x]:
                c0 = A["Xi"][x][0] == x; c1 = B["Xi"][x][0] == x
                o0 = oncyc(g, A["s"], A["sb"], x); o1 = oncyc(g, B["s"], B["sb"], x)
                cnt["keep_" + ("node" if (c0 or c1) else "cyc" if (o0 or o1) else "OFF")] += 1
                if not (o0 or o1) and len(EX) < 20: EX.append(("OFF", name, k, x))
        if A["Xi"] == B["Xi"]: continue
        cnt["xich"] += 1
        if not any(A["Xi"][x] != B["Xi"][x] for x in sw):
            cnt["STRONG_V"] += 1
            if len(EX) < 20: EX.append(("STRONG", name, k, sw, [v for v in range(g.n) if A["Xi"][v] != B["Xi"][v]][:8]))
def main(a):
    import core_probe as CP, dual_probe as D
    a = [x for x in a if x != "--lzc"]
    def do(g, name, ex=None):
        for s0 in ([ex] if ex else []) + [RE.best_reward_start(g)] + [D.rand_start(g, random.Random(name + str(i))) for i in range(int(os.environ.get("RANDSTARTS", "0")))]:
            try: analyse(g, s0, name)
            except RuntimeError: cnt["maxit"] += 1
    if a[0] == "rand":
        N, lo, hi, seed = map(int, a[1:5]); r2 = random.Random(seed)
        for i in range(N):
            nn = r2.randint(lo, hi); do(D.rand_ck(r2, nn, r2.randint(0, min(5, nn - 1))), "rand%d" % i)
    else:
        for p in a:
            if p.endswith(".start"): continue
            g = RE.parse(p); sp = p[:-3] + ".start"
            do(g, p, CP.parse_start(g, sp) if os.path.exists(sp) else None)
    for k in sorted(cnt): print(k, cnt[k])
    for e in EX: print("EX", e)
main(sys.argv[1:])
