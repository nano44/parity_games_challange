#!/usr/bin/env python3
"""REFEREE successor 18: own control for packet P-N5-GP (L-SI box 31, l-si d072bb28, sha1 cd4866df).
Own engine rl_engine (SPEC S1-S5 from the text; no lane code). Per N5 run:
  FRZ    frozen W-phases F = [a, b]: maximal runs inside one (lambda_Xi, tau)-phase with no S4c transition and lambda_W, sigma-bar constant
  WMON   W_{t+1} >= W_t pointwise at every transition of F (W = value of the (sigma_t, tau)-plays)
  XW     Xi_t <= W_t pointwise, and = where the (sigma_t, tau)-play avoids D_t (every state of the run)
  GPS    Lemma GP*: for every k in F, every x, every simple path r of G_tau from x (Odd steps follow tau) with L <= k - a edges to a cycle node
         of state a, none of whose Even edges (r_i, r_i+1) is BLOCKED at state k-1-i: W_k(x) >= value(r).  DFS, capped per (F, k).
  GPC    the same for TIMELY / TIMELY+ paths (Corollaries GP, GP+), counted separately (they are sub-families of the GP* paths)
  FWR    Corollary FW-R*: WCH <= (n - 1)(R*_T + 1)
MUT (the hypotheses dropped from the path family; each must produce violations somewhere):
  1 drop L <= k - a (the omission in the approved RESULTS line); 2 allow Odd steps off tau; 3 drop the BLOCKED condition (plain Lemma P).
Usage: gp_probe.py rand N lo hi seed | FILES...  (env MAXN, RANDSTARTS, CAP)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE
MUT = int(os.environ.get("MUT", "0")); CAP = int(os.environ.get("CAP", "20000"))
EX = []


def fail(cnt, tag, *a):
    cnt[tag + "_V"] += 1
    if len(EX) < 30: EX.append((tag,) + a)


def analyse(cnt, g, start, name):
    n = g.n; st = RE.run(g, start); T = len(st) - 1
    cnt["RUNS"] += 1; cnt["TRANS"] += T
    nxs = [[x["s"][v] if g.owner[v] == 0 else x["t"][v] for v in range(n)] for x in st]
    W = [[RE.play_value(g, nx, v) for v in range(n)] for nx in nxs]
    lamX = [tuple(v[0] for v in x["Xi"]) for x in st]; lamW = [tuple(v[0] for v in w) for w in W]
    tau = [tuple(x["t"][v] for v in range(n) if g.owner[v] == 1) for x in st]
    sbar = [tuple(x["sb"][v] for v in range(n) if g.owner[v] == 1) for x in st]
    key = g.key
    # XW at every state
    for t in range(T + 1):
        D = {u for u in range(n) if g.owner[u] == 1 and st[t]["sb"][u] != st[t]["t"][u]}
        for v in range(n):
            cnt["XW_chk"] += 1
            if key(st[t]["Xi"][v]) > key(W[t][v]): fail(cnt, "XW", name, t, v)
            pre, cy = RE.lasso(nxs[t], v)
            if not (set(pre) | set(cy)) & D and st[t]["Xi"][v] != W[t][v]: fail(cnt, "XW2", name, t, v)
    Is = [set(x["Is"]) for x in st]

    def blocked(t, x, z):
        return key(W[t][z]) > key(W[t][nxs[t][x]]) and (x, z) not in Is[t]

    # frozen W-phases
    a = 0
    while a <= T:
        b = a
        while b < T and lamX[b + 1] == lamX[a] and tau[b + 1] == tau[a] and not st[b]["fb"] and lamW[b + 1] == lamW[a] and sbar[b + 1] == sbar[a]:
            b += 1
        cnt["FRZ"] += 1; cnt["FRZ_len"] += b - a
        D = {u for u in range(n) if g.owner[u] == 1 and st[a]["sb"][u] != st[a]["t"][u]}
        cnt["FRZ_Dnonempty"] += bool(D)
        for t in range(a, b):
            for v in range(n):
                cnt["WMON_chk"] += 1
                if key(W[t + 1][v]) < key(W[t][v]): fail(cnt, "WMON", name, a, b, t, v)
        cyc = {u for u in range(n) if lamW[a][u] == u}
        # GP*
        for k in range(a, b + 1):
            budget = [CAP]
            for x in range(n):
                wk = key(W[k][x])
                # DFS over simple paths from x
                stack = [(x, [x])]
                while stack and budget[0] > 0:
                    y, path = stack.pop(); budget[0] -= 1
                    L = len(path) - 1
                    if y in cyc:
                        u = y; P = 0
                        for q in path[:-1]:
                            if g.rank[q] > g.rank[u]: P |= 1 << g.rank[q]
                        val = (u, P, L)
                        cnt["GPS_chk"] += 1
                        if key(val) > wk: fail(cnt, "GPS" + ("_MUT%d" % MUT if MUT else ""), name, a, b, k, x, path)
                    if MUT != 1 and L >= k - a: continue
                    if L >= n - 1: continue
                    i = L; t = k - 1 - i
                    if MUT != 1 and t < a: continue
                    succs = g.succ[y] if (g.owner[y] == 0 or MUT == 2) else [st[k]["t"][y]]
                    for z in succs:
                        if z in path: continue
                        if g.owner[y] == 0 and MUT != 3 and t >= a and blocked(t, y, z): continue
                        stack.append((z, path + [z]))
                if budget[0] <= 0: cnt["GPS_capped"] += 1
        # FW-R*
        WCH = sum(1 for t in range(a, b) if W[t + 1] != W[t])
        blk_hist = set()
        RT = 0
        for t in range(a, b):
            late = False
            for y in range(n):
                if g.owner[y] == 0 and nxs[t + 1][y] != nxs[t][y] and (y, nxs[t + 1][y]) in blk_hist: late = True
            RT += late
            for y in range(n):
                if g.owner[y] == 0:
                    for z in g.succ[y]:
                        if blocked(t, y, z): blk_hist.add((y, z))
        cnt["FWR_chk"] += 1; cnt["RT_max"] = max(cnt["RT_max"], RT); cnt["RT_pos"] += RT > 0; cnt["WCH_max"] = max(cnt["WCH_max"], WCH)
        if WCH > (n - 1) * (RT + 1): fail(cnt, "FWR", name, a, b, WCH, RT)
        if WCH > n - 1: cnt["WCH_gt_n1"] += 1
        a = b + 1


def main(a):
    import core_probe as CP, dual_probe as D
    cnt = Counter(); nst = int(os.environ.get("RANDSTARTS", "1"))
    def do(g, name, extra=None):
        r = random.Random(name)
        starts = ([extra] if extra else []) + [RE.best_reward_start(g)] + [D.rand_start(g, r) for _ in range(nst)]
        for s0 in starts:
            try: analyse(cnt, g, s0, name)
            except RuntimeError: cnt["maxit"] += 1
    if a[0] == "rand":
        N, lo, hi, seed = map(int, a[1:5]); r2 = random.Random(seed)
        for i in range(N):
            nn = r2.randint(lo, hi)
            do(D.rand_ck(r2, nn, r2.randint(0, min(5, nn - 1))), "rand%d" % i)
    else:
        for path in a:
            if path.endswith(".start"): continue
            try: g = RE.parse(path)
            except Exception: cnt["parse_err"] += 1; continue
            if g.n > int(os.environ.get("MAXN", "40")): cnt["skip_big"] += 1; continue
            sp = path[:-3] + ".start"; ex = None
            if os.path.exists(sp):
                try: ex = CP.parse_start(g, sp)
                except Exception: cnt["start_err"] += 1
            cnt["GAMES"] += 1; do(g, os.path.relpath(path), ex)
    for k in sorted(cnt): print(k, cnt[k])
    print("VIOLATIONS", sum(v for k, v in cnt.items() if k.endswith("_V")))
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
